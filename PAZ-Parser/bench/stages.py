"""What a benchmark decodes, and the stages it times on it.

A workload is one PAZ entry (`--entry`), one whole archive (`--archive`),
the client's file index (`--index`), one LOC file (`--loc`) or the folder's
entry list (`--folder`).

On an entry, `decrypt` and `decompress` work on bytes already in memory, so
disk speed and the OS file cache stay out of their numbers. `read` is the
whole path the app takes to open a file, disk read included. `extract` is what
`extract_all` does per file: `read`, then the size check and the write to disk.
`parse` is the handler's `all_records()`, the parse the app's table runs, on
the decoded file, with LOC and the lookup indexes loaded as in the app; it only
exists for a file with a parsed view.

On an archive, `extract` runs `extract_all`'s loop over every entry in it. It
leaves out `extract_all`'s meta file parse (the `index` stage below), which
reads every archive's file table on each call and would swamp the decode time.

On the index, `index` is that meta file parse on its own: the file table and
decrypted path block of every archive, which the app runs when the client
changed and its index cache is out of date. The warm-up reads every archive
header, so the timed runs see a warm file cache.

On a LOC file, `loc` is `init_loc()` on the file's bytes in memory: the
decompress and the text index every table's game text comes from, which the
app builds on every start and language switch.

On the folder, `entries` is what a start does before the page gets the tree:
the PAZ index cache load, the entry maps and the tree, without LOC and the
lookup indexes (`--loc` times LOC).
"""
from __future__ import annotations

import hashlib
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

from bdo_models import PazEntry
from cli.errors import CliError
from api.bdo_api import Api
from bdo_preview import get_handler, has_parsed_view
from cli.parsed_file import ParsedFile, find_entry, load_parsed_file
from api.bdo_config import load_config
from api.bdo_languages import loc_path
from cli.session import open_session, resolve_paz_root
from _common.loc import decompress_loc, init_loc
from paz.bdo_cache import CACHE_FILE
from paz.bdo_decompress import bdo_decompress
from paz.bdo_meta_reader import read_bdo_meta
from paz.bdo_paz_extract import extract_entries, extract_entry, find_single_meta_file, parse_meta_file
from paz.bdo_payload_reader import (
    ice_decrypt_bytes,
    is_encrypted,
    needs_decompress,
    read_entry_payload,
    read_raw_payload,
)

from .results import FixtureInfo

# A 14 MB texture (4.4 MB stored) that is both encrypted and compressed, so
# every entry stage has work to do.
DEFAULT_ENTRY = "morningland_boss_03_02_full.dds"
# A median-size archive (9 MB, about 800 files) mixing .bwp, .xml, .bss,
# .dbss and more, compressed and stored, encrypted and plain.
DEFAULT_ARCHIVE = "pad05889.paz"
STAGE_NAMES = ("decrypt", "decompress", "read", "extract", "parse", "index", "loc", "entries")
_HASH_CHUNK_BYTES = 1024 * 1024


@dataclass(frozen=True)
class Stage:
    name: str
    run: Callable[[], object]
    # Untimed, before every run: undoes what a run leaves behind that would
    # make the next one cheaper.
    prepare: Callable[[], None] | None = None
    # Time with the garbage collector on, as the app runs.
    with_gc: bool = False


@dataclass(frozen=True)
class Workload:
    info: FixtureInfo
    # Builds the stages; `extract` writes into the scratch folder it is given.
    build_stages: Callable[[Path], list[Stage]]


def load_entry_workload(paz_folder: str | None, name: str, wanted: Sequence[str] | None) -> Workload:
    """Find `name` in the PAZ folder and read its stored bytes into memory.

    LOC and the lookup indexes, about 5 s more, only load when the `parse`
    stage will run: `wanted` (None for every stage) asks for it and the file
    has a parsed view.
    """
    api = _open_api(paz_folder)
    entry = find_entry(api.entries, name)
    parsed: ParsedFile | None = None
    if _will_parse(entry, wanted):
        api = _open_api(paz_folder, with_loc_and_indexes=True)
        parsed = load_parsed_file(api, entry.internal_path)
    paz_root = _paz_root(api)
    archive_path = paz_root / entry.archive_name
    try:
        raw = read_raw_payload(archive_path, entry)
    except (OSError, ValueError) as ex:
        raise CliError(f"cannot read {entry.internal_path}: {ex}") from ex
    decrypted = ice_decrypt_bytes(raw) if is_encrypted(entry) else raw

    info = FixtureInfo(
        name=entry.internal_path,
        files=1,
        stored_bytes=entry.compressed_size,
        size_bytes=entry.uncompressed_size,
        sha256=hashlib.sha256(raw).hexdigest(),
    )
    return Workload(info, lambda scratch: _entry_stages(archive_path, entry, raw, decrypted, parsed, scratch))


def load_archive_workload(paz_folder: str | None, archive: str) -> Workload:
    """Every entry stored in `archive` (`pad05889.paz`, any case, extension optional)."""
    api = _open_api(paz_folder)
    paz_root = _paz_root(api)
    wanted = archive_file_name(archive)
    in_archive = [entry for entry in api.entries if entry.archive_name.lower() == wanted]
    if not in_archive:
        raise CliError(f"no file of the client is stored in {wanted}.")
    archive_path = paz_root / in_archive[0].archive_name

    info = FixtureInfo(
        name=wanted,
        files=len(in_archive),
        stored_bytes=sum(entry.compressed_size for entry in in_archive),
        size_bytes=sum(entry.uncompressed_size for entry in in_archive),
        sha256=_file_sha256(archive_path),
    )
    return Workload(
        info,
        lambda scratch: [Stage("extract", lambda: _extract_archive(paz_root, scratch, in_archive))],
    )


def load_index_workload(paz_folder: str | None) -> Workload:
    """The client's `.meta` file and every archive it lists."""
    paz_root = resolve_paz_root(paz_folder)
    try:
        meta_path = find_single_meta_file(paz_root)
        meta = read_bdo_meta(meta_path)
    except (OSError, ValueError) as ex:
        raise CliError(f"cannot read the meta file in {paz_root}: {ex}") from ex

    info = FixtureInfo(
        name=meta_path.name,
        files=meta.paz_file_count,
        stored_bytes=sum(table.size for table in meta.paz_files),
        size_bytes=0,
        sha256=_file_sha256(meta_path),
    )
    # The collector stays on, as in the app: the parse builds one PazEntry
    # per file of the client.
    return Workload(info, lambda _scratch: [Stage("index", lambda: parse_meta_file(meta_path), with_gc=True)])


def load_loc_workload(paz_folder: str | None, language: str | None) -> Workload:
    """The LOC file of `language`, or of the language picked in the app."""
    code = language or load_config().get("language", "en")
    path = loc_path(resolve_paz_root(paz_folder), code)
    if path is None:
        raise CliError(f"the language '{code}' has no LOC file to read.")
    try:
        raw = path.read_bytes()
    except OSError as ex:
        raise CliError(f"cannot read {path}: {ex}") from ex
    decompressed = decompress_loc(raw)
    if decompressed is None:
        raise CliError(f"{path.name} does not decompress.")

    info = FixtureInfo(
        name=path.name,
        files=1,
        stored_bytes=len(raw),
        size_bytes=len(decompressed),
        sha256=hashlib.sha256(raw).hexdigest(),
    )
    # The collector stays on, as in the app: the index holds one string and
    # one key tuple per text.
    return Workload(info, lambda _scratch: [Stage("loc", lambda: init_loc(raw), with_gc=True)])


def load_folder_workload(paz_folder: str | None) -> Workload:
    """The folder's PAZ index cache, which must match the client already."""
    api = _open_api(paz_folder)
    paz_root = _paz_root(api)
    if api.cache_dir is None:
        raise CliError("the PAZ folder did not load.")
    cache_path = api.cache_dir / CACHE_FILE
    if not cache_path.is_file():
        raise CliError(f"no {CACHE_FILE} in {api.cache_dir}; open the folder once first.")

    info = FixtureInfo(
        name=CACHE_FILE,
        files=len(api.entries),
        stored_bytes=cache_path.stat().st_size,
        size_bytes=0,
        sha256=_file_sha256(cache_path),
    )

    def load_entries() -> None:
        Api().load_folder(paz_root, load_loc=False, load_indexes=False)

    # The collector stays on, as in the app.
    return Workload(info, lambda _scratch: [Stage("entries", load_entries, with_gc=True)])


def archive_file_name(text: str) -> str:
    name = text.strip().lower()
    return name if name.endswith(".paz") else f"{name}.paz"


def parse_stage_names(text: str | None) -> list[str] | None:
    """`--stages decrypt,read` as a list; None (every stage) when not given."""
    if text is None:
        return None
    names = [name.strip().lower() for name in text.split(",") if name.strip()]
    unknown = [name for name in names if name not in STAGE_NAMES]
    if unknown or not names:
        raise CliError(f"--stages takes a comma list of {', '.join(STAGE_NAMES)}, got '{text}'.")
    return names


def select_stages(stages: Sequence[Stage], wanted: Sequence[str] | None, workload_name: str) -> list[Stage]:
    """The `wanted` stages in pipeline order, or every stage when None."""
    if wanted is None:
        return list(stages)
    available = [stage.name for stage in stages]
    missing = [name for name in wanted if name not in available]
    if missing:
        raise CliError(
            f"{workload_name} has no {', '.join(missing)} stage; it has {', '.join(available)}."
        )
    return [stage for stage in stages if stage.name in wanted]


def _open_api(paz_folder: str | None, *, with_loc_and_indexes: bool = False) -> Api:
    return open_session(paz_folder, load_loc=with_loc_and_indexes, load_indexes=with_loc_and_indexes)


def _paz_root(api: Api) -> Path:
    if api.paz_root is None:
        raise CliError("the PAZ folder did not load.")
    return api.paz_root


def _will_parse(entry: PazEntry, wanted: Sequence[str] | None) -> bool:
    if wanted is not None and "parse" not in wanted:
        return False
    path = Path(entry.internal_path)
    return has_parsed_view(get_handler(path.name, path.suffix))


def _entry_stages(
    archive_path: Path,
    entry: PazEntry,
    raw: bytes,
    decrypted: bytes,
    parsed: ParsedFile | None,
    scratch: Path,
) -> list[Stage]:
    """The stages that apply to the entry, in pipeline order."""
    stages: list[Stage] = []
    if is_encrypted(entry):
        stages.append(Stage("decrypt", lambda: ice_decrypt_bytes(raw)))
    if needs_decompress(entry, decrypted):
        stages.append(Stage("decompress", lambda: bdo_decompress(decrypted, expected_size=entry.uncompressed_size)))
    stages.append(Stage("read", lambda: read_entry_payload(archive_path, entry)))
    stages.append(
        Stage(
            "extract",
            lambda: extract_entry(
                paz_root=archive_path.parent,
                output_root=scratch,
                entry=entry,
                overwrite=True,
                flat=True,
            ),
        )
    )
    if parsed is not None:
        # Every run parses cold: a handler keeps its records and index per
        # payload, so the second call on the same bytes would skip building
        # them. The collector stays on as in the app, so the run pays for
        # whatever the handler cache does not pause it around.
        stages.append(Stage("parse", parsed.records, prepare=parsed.handler.clear_data_cache, with_gc=True))
    return stages


def _extract_archive(paz_root: Path, scratch: Path, entries: list[PazEntry]) -> None:
    counts = extract_entries(paz_root, scratch, entries, overwrite=True)
    if counts.failed:
        raise CliError(f"{counts.failed} of {len(entries)} files failed to extract; the log above names them.")


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            while chunk := stream.read(_HASH_CHUNK_BYTES):
                digest.update(chunk)
    except OSError as ex:
        raise CliError(f"cannot read {path}: {ex}") from ex
    return digest.hexdigest()
