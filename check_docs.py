"""Check the format docs, and fit their layouts to the game files of a PAZ folder.

    python check_docs.py --staged             # the docs in the commit (the pre-commit hook)
    python check_docs.py --all                # every doc in the layout format
    python check_docs.py buffsimply_bss.md    # named docs
    python check_docs.py --all --paz-folder D:/old/Paz --client 3401
    python check_docs.py --all --version 2107  # one of my test clients, in whichever region folder holds it
    python check_docs.py --all --version all   # the live client, then every test client, newest first
    python check_docs.py --all --version all --from 2063  # resume a stopped run at client 2063 and go on to older ones
    python check_docs.py --all --version 2107 --jobs 4     # four worker processes instead of sixteen
    python check_docs.py --all --version all --recheck     # read every client again, also those checked before

Without --paz-folder or --version the check reads the PAZ folder last opened
in the app, the live client. It writes each doc's `## Versions` section and exits 1 when
it changed one, so the hook stops the commit for a review. A staged or named
doc not in the layout format yet is listed as skipped and never stops it.
Several docs are checked on worker processes, sixteen (fewer on a smaller machine) unless --jobs says otherwise.
A client a doc's Versions already lists, read against the same layouts, is skipped;
--recheck reads it again (after a change to the walk, for one client or with
--version all for every one).
See "Versions" in docs/format-docs.md.
"""

from __future__ import annotations

import argparse
import contextlib
import faulthandler
import io
import multiprocessing
import os
import subprocess
import sys
import threading
import time
from collections import OrderedDict, deque
from collections.abc import Iterator, Sequence
from concurrent.futures import Future, ProcessPoolExecutor
from dataclasses import dataclass
from multiprocessing.process import BaseProcess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "PAZ-Parser"), str(ROOT / "PAZ-Parser" / "handlers")]
# numpy's OpenBLAS commits buffers for every core when it is imported (740 MB on 32 cores), in each
# worker process. The check does no matrix math; one thread keeps the import at 24 MB. Workers inherit it.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from format_docs import TEMPLATE_PREFIX, converted_docs  # noqa: E402
from format_docs.check_run import (  # noqa: E402
    Client,
    DocOutcome,
    Status,
    UnreadableFile,
    VersionsUpdate,
    apply_updates,
    check_doc_file,
    write_doc,
)
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
# Worker processes by default: half the 32 threads of my machine. With all 32 busy for a whole
# --version all sweep its CPU crashed; 16 ran a sweep fine.
DEFAULT_JOBS = min(16, os.cpu_count() or 1)
# A run on worker processes writes the docs this often, at the end and when it stops: a write per doc per
# client is 250,000 writes for a sweep over every test client, each one a chance to meet a virus scanner.
FLUSH_SECONDS = 120
# Clients whose docs the workers check at once; each worker keeps their PAZ indexes open. With one,
# the workers wait for every client's slowest doc (itemenchantbackendtest.dbss walks for 14 s).
CLIENTS_IN_FLIGHT = 3


class CheckError(Exception):
    pass


@dataclass(frozen=True)
class PazSource:
    """A PAZ folder to check, by its path and the client number Versions names it with."""

    root: str
    number: int


# Set in each worker process: the doc index, and the clients it opened last (at most CLIENTS_IN_FLIGHT).
_worker_rows: IndexRows = {}
_worker_clients: OrderedDict[PazSource, Client] = OrderedDict()


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
    pending = PendingDocs()
    is_stopped = False
    try:
        is_stopped = _check_clients(docs, rows, _each_client(args), args, pool, pending)
    except CheckError as error:
        print(f"check_docs: {error}", file=sys.stderr)
        return 1
    finally:
        if pool is not None:
            pool.shutdown(cancel_futures=True)
        pending.flush()
    return 1 if is_stopped else 0


class PendingDocs:
    """The Versions changes the workers hand back, kept here and written every `FLUSH_SECONDS`.

    Each client's changes are only collected; `flush` merges a doc's changes in one go and writes
    it, also when the run stops, so a stopped run loses at most `FLUSH_SECONDS` of clients, which the
    next run reads again. Merging per client parsed and rewrote every doc's Versions on one core
    between clients, which held up the workers.
    """

    def __init__(self, flush_seconds: float = FLUSH_SECONDS) -> None:
        self._updates: dict[Path, list[VersionsUpdate]] = {}
        self._flush_seconds = flush_seconds
        self._last_flush = time.monotonic()

    def add(self, outcomes: Sequence[DocOutcome]) -> None:
        for outcome in outcomes:
            if outcome.update is not None:
                self._updates.setdefault(outcome.doc, []).append(outcome.update)

    def flush_if_due(self) -> None:
        if time.monotonic() - self._last_flush >= self._flush_seconds:
            self.flush()

    def flush(self) -> None:
        for doc, updates in self._updates.items():
            write_doc(doc, apply_updates(doc.read_text(encoding="utf-8"), updates))
        self._updates.clear()
        self._last_flush = time.monotonic()


def _pool(args: argparse.Namespace, rows: IndexRows, doc_count: int) -> ProcessPoolExecutor | None:
    """Worker processes for the doc checks, or None to check them in this process."""
    workers = min(args.jobs, doc_count)
    if workers <= 1 or args.docs_only:
        return None
    return ProcessPoolExecutor(workers, initializer=_start_worker, initargs=(rows,))


def _check_clients(
    docs: Sequence[Path],
    rows: IndexRows,
    sources: Iterator[PazSource | None],
    args: argparse.Namespace,
    pool: ProcessPoolExecutor | None,
    pending: PendingDocs,
) -> bool:
    """Checks `docs` against each source and reports them in order; True when one of them stops the commit.

    On the pool, the docs of up to `CLIENTS_IN_FLIGHT` clients are queued at once, so the workers go on
    with the next client while one walks a large file of the last.
    """
    write = not args.no_write
    is_stopped = False
    in_flight: deque[tuple[PazSource, list[Future[DocOutcome]]]] = deque()
    for source in sources:
        if pool is None or source is None:
            is_stopped |= _finish_client(docs, source, _outcomes(docs, rows, source, write, args.recheck, pool), pending)
            continue
        futures = [pool.submit(_check_in_worker, doc, source, write, args.recheck) for doc in docs]
        in_flight.append((source, futures))
        if len(in_flight) >= CLIENTS_IN_FLIGHT:
            is_stopped |= _finish_queued(docs, in_flight.popleft(), pending)
    while in_flight:
        is_stopped |= _finish_queued(docs, in_flight.popleft(), pending)
    return is_stopped


def _finish_queued(docs: Sequence[Path], queued: tuple[PazSource, list[Future[DocOutcome]]], pending: PendingDocs) -> bool:
    source, futures = queued
    return _finish_client(docs, source, [future.result() for future in futures], pending)


def _finish_client(docs: Sequence[Path], source: PazSource | None, outcomes: Sequence[DocOutcome], pending: PendingDocs) -> bool:
    """Reports one client's outcomes and keeps their Versions changes; True when one of them stops the commit."""
    pending.add(outcomes)
    pending.flush_if_due()
    for outcome in outcomes:
        _report(outcome)
    stopped = [outcome for outcome in outcomes if outcome.status.stops_commit]
    if any(outcome.status is Status.UPDATED for outcome in stopped):
        print("check_docs: Versions updated, check and `git add` again", file=sys.stderr)
    checked = "docs only" if source is None else f"client {source.number}"
    before = sum(outcome.status is Status.CHECKED_BEFORE for outcome in outcomes)
    skipped = f", {before} checked before" if before else ""
    print(f"check_docs: {len(docs)} docs, {checked}, {len(stopped)} to fix{skipped}", file=sys.stderr)
    return bool(stopped)


def _outcomes(
    docs: Sequence[Path], rows: IndexRows, source: PazSource | None, write: bool, recheck: bool, pool: ProcessPoolExecutor | None
) -> list[DocOutcome]:
    """Each doc's outcome on `source`, in `docs` order; on the pool's workers when there is a pool."""
    if source is None:
        return [check_doc_file(doc, rows, None, write=write) for doc in docs]
    if pool is None:
        client = _open_client(source)
        return [check_doc_file(doc, rows, client, write=write, recheck=recheck) for doc in docs]
    # The workers hand their changes back (PendingDocs): a worker may read any doc as another doc's shared layout.
    return [future.result() for future in [pool.submit(_check_in_worker, doc, source, write, recheck) for doc in docs]]


def _start_worker(rows: IndexRows) -> None:
    global _worker_rows
    _worker_rows = rows
    faulthandler.enable()  # a worker that dies in native code prints where, instead of only breaking the pool
    parent = multiprocessing.parent_process()
    if parent is not None:
        threading.Thread(target=_exit_with, args=(parent,), daemon=True).start()


def _exit_with(parent: BaseProcess) -> None:
    """Ends the worker once `parent` ends: Windows leaves a killed process's children running, each holding its client."""
    parent.join()
    os._exit(1)


def _check_in_worker(doc: Path, source: PazSource, write: bool, recheck: bool = False) -> DocOutcome:
    """Checks one doc in a worker process, which keeps the clients in flight open and its progress lines quiet.

    The doc's Versions change comes back in the outcome for the main process to merge and write.
    """
    return check_doc_file(doc, _worker_rows, _worker_client(source), write=write, recheck=recheck, defer_write=True)


def _worker_client(source: PazSource) -> Client:
    """`source` opened in this worker; the oldest client is let go once more than `CLIENTS_IN_FLIGHT` are open."""
    client = _worker_clients.get(source)
    if client is not None:
        _worker_clients.move_to_end(source)
        return client
    while len(_worker_clients) >= CLIENTS_IN_FLIGHT:
        _worker_clients.popitem(last=False)
    client = _open_client(source, quiet=True)
    _worker_clients[source] = client
    return client


def _arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the format docs and fit them to the game files.")
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--staged", action="store_true", help="The docs staged for commit")
    which.add_argument("--all", action="store_true", help="Every doc in the layout format")
    which.add_argument("docs", nargs="*", default=[], help="Doc file names, e.g. buffsimply_bss.md")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--paz-folder", help="A PAZ folder other than the one last opened in the app")
    source.add_argument(
        "--version", help=f"A test client in {TEST_CLIENTS} by its client number, or {ALL_VERSIONS} for the live client and then every one"
    )
    source.add_argument("--docs-only", action="store_true", help="Skip the game files")
    parser.add_argument("--client", type=int, help="The client number of --paz-folder, when its .meta does not hold it")
    parser.add_argument("--from", dest="first", type=int, help=f"With --version {ALL_VERSIONS}: start at this client number and go on to older ones, to resume a stopped run")
    parser.add_argument("--no-write", action="store_true", help="Report which layout fits; leave Versions as they are")
    parser.add_argument(
        "--recheck", action="store_true", help="Read the clients again that a doc's Versions already list against the same layouts"
    )
    parser.add_argument(
        "--jobs", type=int, default=DEFAULT_JOBS, help=f"Worker processes for the doc checks; 1 checks them here (default: {DEFAULT_JOBS})"
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

    `--version all` goes newest first and starts with the live client, unless the game is running, a test
    client has its number or `--from` names an older client. Sizes come from the newest client of a layout,
    so after a layout renumber each stale size row is dropped before an older client's row could merge into it.
    """
    if args.version is None:
        yield _source(args.paz_folder, args.client, args.docs_only)
        return
    folders = client_folders(TEST_CLIENTS, args.version, args.first)
    if args.version == ALL_VERSIONS:
        yield from _live_client({number for number, _ in folders}, args.first)
    for number, paz in folders:
        meta = _meta_client(paz)
        if meta != number:
            message = f"{paz.parent.name}: its .meta says client {meta}, not {number}"
            if args.version != ALL_VERSIONS:
                raise CheckError(message)
            print(f"check_docs: skipped {message}", file=sys.stderr)
            continue
        print(f"check_docs: client {number} ({paz})", file=sys.stderr)
        yield PazSource(str(paz), number)


def _live_client(test_clients: set[int], first: int | None) -> Iterator[PazSource]:
    """The PAZ folder last opened in the app, when the game is closed, no test client has its number and `first` is not older."""
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
    if number in test_clients:
        print(f"check_docs: skipped the live client, test client {number} has its number", file=sys.stderr)
        return
    if first is not None and number > first:
        print(f"check_docs: skipped the live client {number}, the run starts at {first}", file=sys.stderr)
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
    """The `<region>/<client>/Paz` folders under `root`: every client of every region for `all`, newest first, or `version`'s.

    `first` drops the `all` folders newer than that client.
    """
    found = _region_clients(root)
    if version == ALL_VERSIONS:
        if first is not None:
            found = [(number, paz) for number, paz in found if number <= first]
        if not found:
            raise CheckError(f"no <region>/<client>/Paz folder in {root}" + ("" if first is None else f" at or before client {first}"))
        return found[::-1]
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


def _open_client(source: PazSource, quiet: bool = False) -> Client:
    """Reads `source`'s files by name, loading its PAZ index on the first read.

    A client every doc checked before is never loaded. The payload cache is emptied before the
    index loads: the last client's files are of no use to this one. `quiet` drops the loading
    lines, which each worker would print once.
    """
    from cli.errors import CliError
    from cli.game_files import GameFiles
    from paz.bdo_payload_cache import clear_payload_cache

    opened: list[GameFiles] = []

    def read_file(name: str) -> bytes | None:
        if not opened:
            clear_payload_cache()
            try:
                with contextlib.redirect_stderr(io.StringIO()) if quiet else contextlib.nullcontext():
                    opened.append(GameFiles.open(source.root))
            except CliError as error:
                raise CheckError(str(error)) from error
        try:
            return opened[0].read(name)
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
    if outcome.status in (Status.OK, Status.CHECKED_BEFORE) and not outcome.messages:
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
