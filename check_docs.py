"""Check the format docs, and fit their layouts to the game files of a PAZ folder.

    python check_docs.py --staged             # the docs in the commit (the pre-commit hook)
    python check_docs.py --all                # every doc in the layout format
    python check_docs.py buffsimply_bss.md    # named docs
    python check_docs.py --all --paz-folder D:/old/Paz --client 3401

Without --paz-folder the check reads the PAZ folder last opened in the app,
the live client. It writes each doc's `## Versions` section and exits 1 when
it changed one, so the hook stops the commit for a review. See "Versions" in
docs/format-docs.md.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / "PAZ-Parser"), str(ROOT / "PAZ-Parser" / "handlers")]

from format_docs import converted_docs  # noqa: E402
from format_docs.check_run import Client, DocOutcome, Status, check_doc_file  # noqa: E402
from format_docs.doc_index import index_rows  # noqa: E402

DOCS_DIR = ROOT / "docs" / "file-formats"
DOCUMENTED = ROOT / "docs" / "documented-formats.md"
_HANDLER_PARSER = ("PAZ-Parser/handlers/_bss/", "PAZ-Parser/handlers/_dbss/")
# A private server or leaked client's .meta holds this in place of its client number.
_UNNUMBERED_CLIENT = 1


class CheckError(Exception):
    pass


def main(argv: Sequence[str] | None = None) -> int:
    args = _arguments(argv)
    try:
        docs = _docs(args)
        client = _client(args.paz_folder, args.client, args.docs_only)
    except CheckError as error:
        print(f"check_docs: {error}", file=sys.stderr)
        return 1
    if args.staged:
        _warn_parser_without_doc()
    rows = index_rows(DOCUMENTED.read_text(encoding="utf-8"))
    outcomes = [check_doc_file(doc, rows, client) for doc in docs]
    for outcome in outcomes:
        _report(outcome)
    stopped = [outcome for outcome in outcomes if outcome.status.stops_commit]
    if any(outcome.status is Status.UPDATED for outcome in stopped):
        print("check_docs: Versions updated, check and `git add` again", file=sys.stderr)
    checked = "docs only" if client is None else f"client {client.number}"
    print(f"check_docs: {len(docs)} docs, {checked}, {len(stopped)} to fix", file=sys.stderr)
    return 1 if stopped else 0


def _arguments(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the format docs and fit them to the game files.")
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--staged", action="store_true", help="The docs staged for commit")
    which.add_argument("--all", action="store_true", help="Every doc in the layout format")
    which.add_argument("docs", nargs="*", default=[], help="Doc file names, e.g. buffsimply_bss.md")
    parser.add_argument("--paz-folder", help="A PAZ folder other than the one last opened in the app")
    parser.add_argument("--client", type=int, help="The client number of --paz-folder, when its .meta does not hold it")
    parser.add_argument("--docs-only", action="store_true", help="Skip the game files")
    args = parser.parse_args(argv)
    if args.client is not None and not args.paz_folder:
        parser.error("--client needs --paz-folder")
    return args


def _docs(args: argparse.Namespace) -> list[Path]:
    if args.all:
        return list(converted_docs(DOCS_DIR))
    if args.staged:
        staged = _git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "docs/file-formats/*.md")
        return [ROOT / name for name in staged if not Path(name).name.startswith("_")]
    paths = [DOCS_DIR / Path(name).name for name in args.docs]
    missing = [path.name for path in paths if not path.is_file()]
    if missing:
        raise CheckError(f"no such doc: {', '.join(missing)}")
    return paths


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
