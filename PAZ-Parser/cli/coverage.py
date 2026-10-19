"""`browser.py --coverage`: parse every file that has a parsed view and list the ones that fail.

Run over an old client, the failures are the tables whose layout differs
from the one the handlers read, so two clients' reports can be diffed.
"""
from __future__ import annotations

import argparse
import time
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

from api.bdo_api import Api
from api.bdo_api_helpers import _norm, path_matcher
from bdo_models import PazEntry
from bdo_preview import PreviewHandler, get_handler, handler_key, has_parsed_view

from .errors import CliError
from .record_output import OutputFormat, format_json, write_records
from .records import output_format
from .session import open_session
from .stdio import error, progress, write_raw

# A progress line on stderr every this many files.
_PROGRESS_EVERY = 250
# Error texts are cut to this many characters.
_MAX_ERROR_LENGTH = 300

# (entry, handler) -> the file's bytes and its companions.
ReadFile = Callable[[PazEntry, PreviewHandler], tuple[bytes, dict[str, bytes]]]


@dataclass(frozen=True)
class FileResult:
    """One file's outcome: `records` when it parsed, `error` when it did not."""

    file: str
    handler: str | None
    ok: bool
    records: int | None
    error: str | None
    seconds: float


def parsed_handler(entry: PazEntry) -> PreviewHandler | None:
    """The handler that builds records for `entry`, or None for hex, text and image views."""
    path = Path(entry.internal_path)
    handler = get_handler(path.name, path.suffix)
    return handler if has_parsed_view(handler) else None


def coverage_targets(
    entries: Iterable[PazEntry],
    pattern: str | None,
    handler_for: Callable[[PazEntry], PreviewHandler | None] = parsed_handler,
) -> list[tuple[PazEntry, PreviewHandler]]:
    """Every entry with a parsed view, in path order; only those matching `pattern` when given."""
    is_hit = path_matcher(pattern) if pattern else None
    targets: list[tuple[PazEntry, PreviewHandler]] = []
    for entry in sorted(entries, key=lambda e: e.internal_path):
        if is_hit is not None and not is_hit(_norm(entry.internal_path)):
            continue
        handler = handler_for(entry)
        if handler is not None:
            targets.append((entry, handler))
    return targets


def check_file(read: ReadFile, entry: PazEntry, handler: PreviewHandler) -> FileResult:
    """Parse one file as the GUI table does.

    Any exception, from reading or parsing, is that file's result, so one
    broken table does not end the run. The handler's cached parse is dropped
    afterwards, so a run over thousands of tables keeps only one in memory.
    """
    started = time.perf_counter()
    path = Path(entry.internal_path)
    key = handler_key(path.name, path.suffix)
    try:
        data, companions = read(entry, handler)
    except Exception as ex:  # a read failure is the file's result too
        return FileResult(entry.internal_path, key, False, None, describe_error(ex), _elapsed(started))
    try:
        records = handler.all_records(data, entry, companions)
    except Exception as ex:  # every handler failure is reported, none stops the run
        return FileResult(entry.internal_path, key, False, None, describe_error(ex), _elapsed(started))
    finally:
        handler.release_data(data)
    return FileResult(entry.internal_path, key, True, len(records), None, _elapsed(started))


def describe_error(ex: BaseException) -> str:
    """`Type: message` on one line, cut to `_MAX_ERROR_LENGTH`."""
    text = " ".join(f"{type(ex).__name__}: {ex}".split())
    return text if len(text) <= _MAX_ERROR_LENGTH else text[: _MAX_ERROR_LENGTH - 1] + "…"


def coverage_document(results: list[FileResult], client_version: int | None) -> dict:
    """The `--coverage --json` document: the client version, the counts and every file's result."""
    failed = sum(1 for result in results if not result.ok)
    return {
        "client_version": client_version,
        "files": len(results),
        "passed": len(results) - failed,
        "failed": failed,
        "results": [asdict(result) for result in results],
    }


def check_files(read: ReadFile, targets: list[tuple[PazEntry, PreviewHandler]]) -> list[FileResult]:
    results: list[FileResult] = []
    for done, (entry, handler) in enumerate(targets, start=1):
        results.append(check_file(read, entry, handler))
        if done % _PROGRESS_EVERY == 0:
            progress(f"{done:,} of {len(targets):,} files checked…")
    return results


def run_coverage(args: argparse.Namespace) -> int:
    output = output_format(args)
    try:
        api = open_session(args.paz_folder, load_loc=False, load_indexes=False)
    except CliError as ex:
        error(str(ex))
        return 1

    targets = coverage_targets(api.entries, args.coverage or None)
    if not targets:
        error(f"no file with a parsed view matches '{args.coverage}'." if args.coverage else "no file has a parsed view.")
        return 1
    progress(f"Parsing {len(targets):,} files…")
    results = check_files(_reader(api), targets)
    _write_results(results, output, api.meta_version)

    failed = sum(1 for result in results if not result.ok)
    progress(
        f"{len(results) - failed:,} of {len(results):,} parsed files pass, {failed:,} fail "
        f"(client version {api.meta_version})."
    )
    return 0


def _reader(api: Api) -> ReadFile:
    def read(entry: PazEntry, handler: PreviewHandler) -> tuple[bytes, dict[str, bytes]]:
        return api.read_entry(entry.internal_path), api.entry_companions(handler, entry)

    return read


def _write_results(results: list[FileResult], output: OutputFormat, client_version: int | None) -> None:
    """JSON and CSV hold every file; the text table only the failures."""
    if output is OutputFormat.JSON:
        write_raw(format_json(coverage_document(results, client_version)))
    elif output is OutputFormat.CSV:
        write_records([asdict(result) for result in results], output)
    else:
        failures = [{"file": r.file, "handler": r.handler, "error": r.error} for r in results if not r.ok]
        if failures:
            write_records(failures, output)


def _elapsed(started: float) -> float:
    return round(time.perf_counter() - started, 3)
