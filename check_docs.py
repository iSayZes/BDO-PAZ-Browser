"""Check the format docs, and fit their layouts to the game files of a PAZ folder.

    python check_docs.py --staged             # the docs in the commit (the pre-commit hook)
    python check_docs.py --all                # every doc in the layout format
    python check_docs.py buffsimply_bss.md    # named docs
    python check_docs.py --all --paz-folder D:/old/Paz --client 3401
    python check_docs.py --all --version 2107  # one of my test clients, in whichever region folder holds it
    python check_docs.py --all --version all   # every test client, oldest first, then the live one
    python check_docs.py --all --version all --from 2063  # resume a stopped run at client 2063
    python check_docs.py --all --version 2107 --jobs 4     # four worker processes instead of one per core

Without --paz-folder or --version the check reads the PAZ folder last opened
in the app, the live client. It writes each doc's `## Versions` section and exits 1 when
it changed one, so the hook stops the commit for a review. A staged or named
doc not in the layout format yet is listed as skipped and never stops it.
Several docs are checked on worker processes, one per core unless --jobs says otherwise.
See "Versions" in docs/format-docs.md.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import multiprocessing
import os
import subprocess
import sys
import threading
from collections.abc import Iterator, Sequence
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from itertools import repeat
from multiprocessing.process import BaseProcess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "PAZ-Parser"), str(ROOT / "PAZ-Parser" / "handlers")]
# numpy's OpenBLAS commits buffers for every core when it is imported (740 MB on 32 cores), in each
# worker process. The check does no matrix math; one thread keeps the import at 24 MB. Workers inherit it.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from format_docs import TEMPLATE_PREFIX, converted_docs  # noqa: E402
from format_docs.check_run import Client, DocOutcome, Status, UnreadableFile, check_doc_file  # noqa: E402
from format_docs.doc_index import IndexRows, index_rows  # noqa: E402

DOCS_DIR = ROOT / "docs" / "file-formats"
DOCUMENTED = ROOT / "docs" / "documented-formats.md"
_HANDLER_PARSER = ("PAZ-Parser/handlers/_bss/", "PAZ-Parser/handlers/_dbss/")
# A private server or leaked client's .meta holds this in place of its client number.
_UNNUMBERED_CLIENT = 1
# My test clients: a folder per region (NAEU), in it one folder per official build named by its client number,
# with the archives in <region>/<client>/Paz.
TEST_CLIENTS = Path("F:/BDO Projects/_TestClient")
ALL_VERSIONS = "all"
GAME_PROCESS = "BlackDesert64.exe"


class CheckError(Exception):
    pass


@dataclass(frozen=True)
class PazSource:
    """A PAZ folder to check, by its path and the client number Versions names it with."""

    root: str
    number: int


# Set in each worker process: the doc index, and the client it opened last.
_worker_rows: IndexRows = {}
_worker_client: tuple[PazSource, Client] | None = None


def main(argv: Sequence[str] | None = None) -> int:
    args = _arguments(argv)
    try:
        docs = _docs(args)
    except CheckError as error:
        print(f"check_docs: {error}", file=sys.stderr)
        return 1
    if args.staged:
        _warn_parser_without_doc()
    rows = index_rows(DOCUMENTED.read_text(encoding="utf-8"))
    pool = _pool(args, rows, len(docs))
    is_stopped = False
    try:
        # One client at a time, so each test client's PAZ index is let go before the next loads.
        for source in _each_client(args):
            is_stopped |= _check_client(docs, rows, source, args.no_write, pool)
    except CheckError as error:
        print(f"check_docs: {error}", file=sys.stderr)
        return 1
    finally:
        if pool is not None:
            pool.shutdown(cancel_futures=True)
    return 1 if is_stopped else 0


def _pool(args: argparse.Namespace, rows: IndexRows, doc_count: int) -> ProcessPoolExecutor | None:
    """Worker processes for the doc checks, or None to check them in this process."""
    workers = min(args.jobs, doc_count)
    if workers <= 1 or args.docs_only:
        return None
    return ProcessPoolExecutor(workers, initializer=_start_worker, initargs=(rows,))


def _check_client(
    docs: Sequence[Path], rows: IndexRows, source: PazSource | None, no_write: bool, pool: ProcessPoolExecutor | None
) -> bool:
    """Checks `docs` against `source` and reports them; True when one of them stops the commit."""
    outcomes = _outcomes(docs, rows, source, not no_write, pool)
    for outcome in outcomes:
        _report(outcome)
    stopped = [outcome for outcome in outcomes if outcome.status.stops_commit]
    if any(outcome.status is Status.UPDATED for outcome in stopped):
        print("check_docs: Versions updated, check and `git add` again", file=sys.stderr)
    checked = "docs only" if source is None else f"client {source.number}"
    print(f"check_docs: {len(docs)} docs, {checked}, {len(stopped)} to fix", file=sys.stderr)
    return bool(stopped)


def _outcomes(
    docs: Sequence[Path], rows: IndexRows, source: PazSource | None, write: bool, pool: ProcessPoolExecutor | None
) -> list[DocOutcome]:
    """Each doc's outcome on `source`, in `docs` order; on the pool's workers when there is a pool."""
    if source is None:
        return [check_doc_file(doc, rows, None, write=write) for doc in docs]
    if pool is None:
        client = _open_client(source)
        return [check_doc_file(doc, rows, client, write=write) for doc in docs]
    return list(pool.map(_check_in_worker, docs, repeat(source), repeat(write)))


def _start_worker(rows: IndexRows) -> None:
    global _worker_rows
    _worker_rows = rows
    parent = multiprocessing.parent_process()
    if parent is not None:
        threading.Thread(target=_exit_with, args=(parent,), daemon=True).start()


def _exit_with(parent: BaseProcess) -> None:
    """Ends the worker once `parent` ends: Windows leaves a killed process's children running, each holding its client."""
    parent.join()
    os._exit(1)


def _check_in_worker(doc: Path, source: PazSource, write: bool) -> DocOutcome:
    """Checks one doc in a worker process, which opens each client once and keeps its progress lines quiet."""
    global _worker_client
    if _worker_client is None or _worker_client[0] != source:
        _worker_client = None  # let the last client's PAZ index go before the next loads
        with contextlib.redirect_stderr(io.StringIO()):
            _worker_client = (source, _open_client(source))
    return check_doc_file(doc, _worker_rows, _worker_client[1], write=write)


def _arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the format docs and fit them to the game files.")
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--staged", action="store_true", help="The docs staged for commit")
    which.add_argument("--all", action="store_true", help="Every doc in the layout format")
    which.add_argument("docs", nargs="*", default=[], help="Doc file names, e.g. buffsimply_bss.md")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--paz-folder", help="A PAZ folder other than the one last opened in the app")
    source.add_argument(
        "--version", help=f"A test client in {TEST_CLIENTS} by its client number, or {ALL_VERSIONS} for every one and then the live client"
    )
    source.add_argument("--docs-only", action="store_true", help="Skip the game files")
    parser.add_argument("--client", type=int, help="The client number of --paz-folder, when its .meta does not hold it")
    parser.add_argument("--from", dest="first", type=int, help=f"With --version {ALL_VERSIONS}: start at this client number, to resume a stopped run")
    parser.add_argument("--no-write", action="store_true", help="Report which layout fits; leave Versions as they are")
    parser.add_argument(
        "--jobs", type=int, default=os.cpu_count() or 1, help="Worker processes for the doc checks; 1 checks them here (default: one per core)"
    )
    args = parser.parse_args(argv)
    if args.client is not None and not args.paz_folder:
        parser.error("--client needs --paz-folder")
    if args.first is not None and args.version != ALL_VERSIONS:
        parser.error(f"--from needs --version {ALL_VERSIONS}")
    if args.jobs < 1:
        parser.error("--jobs needs at least 1")
    return args


def _docs(args: argparse.Namespace) -> list[Path]:
    if args.all:
        return list(converted_docs(DOCS_DIR))
    if args.staged:
        staged = _git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "docs/file-formats/*.md")
        return [ROOT / name for name in staged if not Path(name).name.startswith(TEMPLATE_PREFIX)]
    paths = [DOCS_DIR / Path(name).name for name in args.docs]
    missing = [path.name for path in paths if not path.is_file()]
    if missing:
        raise CheckError(f"no such doc: {', '.join(missing)}")
    return paths


def _each_client(args: argparse.Namespace) -> Iterator[PazSource | None]:
    """The clients to check, opened one at a time: the test clients `--version` names, or the one other folder.

    `--version all` ends with the live client, unless the game is running or a test client had its number.
    """
    if args.version is None:
        yield _source(args.paz_folder, args.client, args.docs_only)
        return
    checked: set[int] = set()
    for number, paz in client_folders(TEST_CLIENTS, args.version, args.first):
        meta = _meta_client(paz)
        if meta != number:
            message = f"{paz.parent.name}: its .meta says client {meta}, not {number}"
            if args.version != ALL_VERSIONS:
                raise CheckError(message)
            print(f"check_docs: skipped {message}", file=sys.stderr)
            continue
        print(f"check_docs: client {number} ({paz})", file=sys.stderr)
        checked.add(number)
        yield PazSource(str(paz), number)
    if args.version == ALL_VERSIONS:
        yield from _live_client(checked)


def _live_client(checked: set[int]) -> Iterator[PazSource]:
    """The PAZ folder last opened in the app, when the game is closed and no test client had its number."""
    from cli.errors import CliError
    from cli.session import resolve_paz_root

    if _is_game_running():
        print(f"check_docs: skipped the live client, {GAME_PROCESS} is running", file=sys.stderr)
        return
    try:
        root = resolve_paz_root(None)
    except CliError as error:
        print(f"check_docs: skipped the live client: {error}", file=sys.stderr)
        return
    number = _meta_client(root)
    if number in checked:
        print(f"check_docs: skipped the live client, client {number} is checked above", file=sys.stderr)
        return
    print(f"check_docs: live client {number} ({root})", file=sys.stderr)
    yield PazSource(str(root), number)


def _is_game_running() -> bool:
    """True when the game's process is in the Windows task list."""
    try:
        done = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {GAME_PROCESS}", "/NH", "/FO", "CSV"],
            capture_output=True, text=True, check=False,
        )
    except OSError as error:
        raise CheckError(f"cannot list the running programs: {error}") from error
    return GAME_PROCESS.lower() in done.stdout.lower()


def client_folders(root: Path, version: str, first: int | None = None) -> list[tuple[int, Path]]:
    """The `<region>/<client>/Paz` folders under `root`: every client of every region for `all`, oldest first, or `version`'s.

    `first` drops the `all` folders older than that client.
    """
    found = _region_clients(root)
    if version == ALL_VERSIONS:
        if first is not None:
            found = [(number, paz) for number, paz in found if number >= first]
        if not found:
            raise CheckError(f"no <region>/<client>/Paz folder in {root}" + ("" if first is None else f" from client {first} on"))
        return found
    if not version.isdigit():
        raise CheckError(f"--version takes a client number or {ALL_VERSIONS}, not {version}")
    wanted = [(number, paz) for number, paz in found if number == int(version)]
    if not wanted:
        raise CheckError(f"no test client {version} in a region folder of {root}")
    return wanted


def _region_clients(root: Path) -> list[tuple[int, Path]]:
    """Every `<region>/<client>/Paz` folder under `root`, oldest client first.

    Each folder under `root` is a region (`NAEU`). Versions names a client by its number alone, so one
    number in two regions is an error, and so is a client folder left directly under `root`.
    """
    if not root.is_dir():
        raise CheckError(f"no test client folder {root}")
    found: dict[int, Path] = {}
    for region in sorted(folder for folder in root.iterdir() if folder.is_dir()):
        if (region / "Paz").is_dir():
            raise CheckError(f"{region} is a client, not a region; move it to {root}/<region>/{region.name}")
        for client in sorted(region.iterdir()):
            if not (client.name.isdigit() and (client / "Paz").is_dir()):
                continue
            number = int(client.name)
            if number in found:
                raise CheckError(f"client {number} is in {found[number].parent.parent.name} and {region.name}; Versions names a client by its number alone")
            found[number] = client / "Paz"
    return sorted(found.items())


def _meta_client(paz: Path) -> int:
    """The client number `paz`'s .meta holds, read without loading the archives."""
    from paz.bdo_cache import read_meta_version
    from paz.bdo_paz_extract import find_single_meta_file

    try:
        return read_meta_version(find_single_meta_file(paz))
    except (OSError, ValueError) as error:
        raise CheckError(f"cannot read the client number of {paz}: {error}") from error


def _source(paz_folder: str | None, number: int | None, docs_only: bool) -> PazSource | None:
    """The PAZ folder to fit the docs to, found without loading its archives, or None to run the doc rules only."""
    if docs_only:
        return None
    from cli.errors import CliError
    from cli.session import resolve_paz_root

    try:
        root = resolve_paz_root(paz_folder)
    except CliError as error:
        if paz_folder:
            raise CheckError(str(error)) from error
        print(f"check_docs: no PAZ folder ({error}); game check skipped", file=sys.stderr)
        return None
    client = number if number is not None else _meta_client(root)
    if client == _UNNUMBERED_CLIENT:
        raise CheckError(f"the .meta of {root} says client {_UNNUMBERED_CLIENT}; pass its real number with --client")
    return PazSource(str(root), client)


def _open_client(source: PazSource) -> Client:
    """Loads `source`'s PAZ index and reads its files by name.

    The payload cache is emptied first: the last client's files are of no use to this one.
    """
    from cli.errors import CliError
    from cli.game_files import GameFiles
    from paz.bdo_payload_cache import clear_payload_cache

    clear_payload_cache()
    try:
        files = GameFiles.open(source.root)
    except CliError as error:
        raise CheckError(str(error)) from error

    def read_file(name: str) -> bytes | None:
        try:
            return files.read(name)
        except CliError as error:
            raise UnreadableFile(str(error)) from error

    return Client(source.number, read_file)


def _warn_parser_without_doc() -> None:
    staged = _git("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    docs = {Path(name).stem for name in staged if name.startswith("docs/file-formats/")}
    for name in staged:
        if not (name.startswith(_HANDLER_PARSER) and name.endswith("/parser.py")):
            continue
        folder = name.split("/")[3]
        ext = name.split("/")[2].lstrip("_")
        if f"{folder}_{ext}" not in docs and (DOCS_DIR / f"{folder}_{ext}.md").is_file():
            print(f"check_docs: parser of {folder}.{ext} changed, its doc is not in this commit", file=sys.stderr)


def _report(outcome: DocOutcome) -> None:
    if outcome.status is Status.OK and not outcome.messages:
        return
    print(f"{outcome.doc.name}: {outcome.status.value}", file=sys.stderr)
    for message in outcome.messages:
        print(f"  {message}", file=sys.stderr)


def _git(*args: str) -> list[str]:
    done = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)
    if done.returncode != 0:
        raise CheckError(f"git {' '.join(args)} failed: {done.stderr.strip()}")
    return [line for line in done.stdout.splitlines() if line]


if __name__ == "__main__":
    sys.exit(main())
