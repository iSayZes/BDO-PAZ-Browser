"""Check the format docs, and fit their layouts to the game files of a PAZ folder.

    python check_docs.py --staged             # the docs in the commit (the pre-commit hook)
    python check_docs.py --all                # every doc in the layout format
    python check_docs.py buffsimply_bss.md    # named docs
    python check_docs.py --all --paz-folder D:/old/Paz --client 3401
    python check_docs.py --all --version 2107  # one of my test clients
    python check_docs.py --all --version all   # every test client, oldest first, then the live one

Without --paz-folder or --version the check reads the PAZ folder last opened
in the app, the live client. It writes each doc's `## Versions` section and exits 1 when
it changed one, so the hook stops the commit for a review. A staged or named
doc not in the layout format yet is listed as skipped and never stops it.
See "Versions" in docs/format-docs.md.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Iterator, Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "PAZ-Parser"), str(ROOT / "PAZ-Parser" / "handlers")]

from format_docs import TEMPLATE_PREFIX, converted_docs  # noqa: E402
from format_docs.check_run import Client, DocOutcome, Status, check_doc_file  # noqa: E402
from format_docs.doc_index import IndexRows, index_rows  # noqa: E402

DOCS_DIR = ROOT / "docs" / "file-formats"
DOCUMENTED = ROOT / "docs" / "documented-formats.md"
_HANDLER_PARSER = ("PAZ-Parser/handlers/_bss/", "PAZ-Parser/handlers/_dbss/")
# A private server or leaked client's .meta holds this in place of its client number.
_UNNUMBERED_CLIENT = 1
# My test clients: one folder per official build, named by its client number, with the archives in <client>/Paz.
TEST_CLIENTS = Path("F:/BDO Projects/_TestClient")
ALL_VERSIONS = "all"
GAME_PROCESS = "BlackDesert64.exe"


class CheckError(Exception):
    pass


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
    is_stopped = False
    try:
        # One client at a time, so each test client's PAZ index is let go before the next loads.
        for client in _each_client(args):
            is_stopped |= _check_client(docs, rows, client, args.no_write)
    except CheckError as error:
        print(f"check_docs: {error}", file=sys.stderr)
        return 1
    return 1 if is_stopped else 0


def _check_client(docs: Sequence[Path], rows: IndexRows, client: Client | None, no_write: bool) -> bool:
    """Checks `docs` against `client` and reports them; True when one of them stops the commit."""
    outcomes = [check_doc_file(doc, rows, client, write=not no_write) for doc in docs]
    for outcome in outcomes:
        _report(outcome)
    stopped = [outcome for outcome in outcomes if outcome.status.stops_commit]
    if any(outcome.status is Status.UPDATED for outcome in stopped):
        print("check_docs: Versions updated, check and `git add` again", file=sys.stderr)
    checked = "docs only" if client is None else f"client {client.number}"
    print(f"check_docs: {len(docs)} docs, {checked}, {len(stopped)} to fix", file=sys.stderr)
    return bool(stopped)


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
    parser.add_argument("--no-write", action="store_true", help="Report which layout fits; leave Versions as they are")
    args = parser.parse_args(argv)
    if args.client is not None and not args.paz_folder:
        parser.error("--client needs --paz-folder")
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


def _each_client(args: argparse.Namespace) -> Iterator[Client | None]:
    """The clients to check, opened one at a time: the test clients `--version` names, or the one other folder.

    `--version all` ends with the live client, unless the game is running or a test client had its number.
    """
    if args.version is None:
        yield _client(args.paz_folder, args.client, args.docs_only)
        return
    checked: set[int] = set()
    for number, paz in client_folders(TEST_CLIENTS, args.version):
        meta = _meta_client(paz)
        if meta != number:
            message = f"{paz.parent.name}: its .meta says client {meta}, not {number}"
            if args.version != ALL_VERSIONS:
                raise CheckError(message)
            print(f"check_docs: skipped {message}", file=sys.stderr)
            continue
        print(f"check_docs: client {number} ({paz})", file=sys.stderr)
        checked.add(number)
        yield _client(str(paz), None, False)
    if args.version == ALL_VERSIONS:
        yield from _live_client(checked)


def _live_client(checked: set[int]) -> Iterator[Client]:
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
    client = _client(str(root), None, False)
    if client is not None:
        yield client


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


def client_folders(root: Path, version: str) -> list[tuple[int, Path]]:
    """The `<client>/Paz` folders under `root`: every folder named by a number for `all`, oldest first, or `version`'s."""
    if not root.is_dir():
        raise CheckError(f"no test client folder {root}")
    if version == ALL_VERSIONS:
        found = sorted((int(folder.name), folder / "Paz") for folder in root.iterdir() if folder.name.isdigit() and (folder / "Paz").is_dir())
        if not found:
            raise CheckError(f"no <client>/Paz folder in {root}")
        return found
    if not version.isdigit():
        raise CheckError(f"--version takes a client number or {ALL_VERSIONS}, not {version}")
    paz = root / version / "Paz"
    if not paz.is_dir():
        raise CheckError(f"no test client {version}: {paz} is not a folder")
    return [(int(version), paz)]


def _meta_client(paz: Path) -> int:
    """The client number `paz`'s .meta holds, read without loading the archives."""
    from paz.bdo_cache import read_meta_version
    from paz.bdo_paz_extract import find_single_meta_file

    try:
        return read_meta_version(find_single_meta_file(paz))
    except (OSError, ValueError) as error:
        raise CheckError(f"cannot read the client number of {paz}: {error}") from error


def _client(paz_folder: str | None, number: int | None, docs_only: bool) -> Client | None:
    """The client to fit the docs to, or None to run the doc rules only."""
    if docs_only:
        return None
    from cli.errors import CliError
    from cli.game_files import GameFiles

    try:
        files = GameFiles.open(paz_folder)
    except CliError as error:
        if paz_folder:
            raise CheckError(str(error)) from error
        print(f"check_docs: no PAZ folder ({error}); game check skipped", file=sys.stderr)
        return None
    client = number if number is not None else files.client
    if client == _UNNUMBERED_CLIENT:
        raise CheckError(f"the .meta of {files.root} says client {_UNNUMBERED_CLIENT}; pass its real number with --client")
    return Client(client, files.read)


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
