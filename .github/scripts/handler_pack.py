"""Plan the handler pack for HEAD: write its manifest.json and say whether it is new.

    python .github/scripts/handler_pack.py                    # preview, prints the plan
    python .github/scripts/handler_pack.py --previous previous/manifest.json --output pack/manifest.json

The release workflow passes the manifest of the `handlers-latest` release as
`--previous` (none before the first pack), adds `--github-output
"$GITHUB_OUTPUT" --notes-file pack-notes.md`, and uploads `--output` there
when `pack` is true. With the same files and handler API as the previous
pack, `--output` is the previous manifest unchanged and `pack` is false; the
exe bundles it either way (`build.py --handler-manifest`).

The pack is the checkout's `PAZ-Parser/handlers` and must be committed as it
is: the app downloads changed files from raw.githubusercontent.com at the
manifest's commit, so each file's LF content has to be git's blob at HEAD.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "PAZ-Parser"))

from bdo_preview import BUNDLED_HANDLERS_DIR, load_plugins  # noqa: E402
from handler_api import HANDLER_API  # noqa: E402
from release_plan import MAX_LISTED, git, listed_subjects, section_lines  # noqa: E402
from updates.handler_manifest import (  # noqa: E402
    HandlerManifest,
    next_pack_version,
    pack_file_bytes,
    pack_files,
    read_manifest,
    write_manifest,
)
from updates.handler_sets import pack_manifest  # noqa: E402

HANDLERS_PATH = "PAZ-Parser/handlers"
# The commits a pack's notes list: handler changes, tests left out.
PACK_PATHS = (HANDLERS_PATH, ":(exclude,glob)PAZ-Parser/**/test_*.py")


class PackError(Exception):
    """The pack can't be planned; the message says why."""


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the handler pack manifest for HEAD.")
    parser.add_argument("--previous", metavar="FILE", help="manifest.json of the published pack, if there is one")
    parser.add_argument("--output", metavar="FILE", help="Where to write manifest.json")
    parser.add_argument("--github-output", metavar="FILE", help="Append pack=, pack_version= for a workflow step")
    parser.add_argument("--notes-file", metavar="FILE", help="Write the handlers-latest release text here")
    args = parser.parse_args()

    try:
        previous = _previous(args.previous)
        manifest, is_new = plan(previous, datetime.now(timezone.utc).strftime("%Y.%m.%d"))
    except PackError as ex:
        print(f"handler_pack: {ex}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        write_manifest(manifest, Path(args.output))
    if args.notes_file:
        Path(args.notes_file).write_text(release_text(manifest), encoding="utf-8", newline="\n")
    _print_plan(manifest, is_new)
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            output.write(f"pack={str(is_new).lower()}\npack_version={manifest.version}\n")
    return 0


def _previous(path: str | None) -> HandlerManifest | None:
    if path is None or not Path(path).is_file():
        return None
    try:
        return read_manifest(Path(path))
    except (OSError, ValueError) as ex:
        raise PackError(f"the published manifest {path} is unreadable: {ex}") from ex


def plan(previous: HandlerManifest | None, today: str) -> tuple[HandlerManifest, bool]:
    """(manifest, new?) for the checkout's handlers against the published pack."""
    check_committed()
    load_plugins(BUNDLED_HANDLERS_DIR)
    commit = git("rev-parse", "HEAD").strip()
    version = next_pack_version(previous, today)
    manifest = pack_manifest(BUNDLED_HANDLERS_DIR, version, commit, HANDLER_API, previous, pack_notes(previous))
    if previous is not None and manifest.is_same_pack(previous):
        return previous, False
    return manifest, True


def check_committed() -> None:
    """Every pack file, with LF line endings, must be git's blob at HEAD."""
    committed = _blob_ids()
    files = pack_files(BUNDLED_HANDLERS_DIR)
    differing = sorted(name for name, path in files.items() if committed.get(name) != _blob_id(pack_file_bytes(path)))
    if differing:
        listed = "\n  ".join(differing[:MAX_LISTED])
        raise PackError(f"{len(differing)} handler files differ from HEAD; commit them first:\n  {listed}")


def _blob_ids() -> dict[str, str]:
    """Path under handlers/ -> git blob id, for every file at HEAD."""
    found: dict[str, str] = {}
    for line in git("ls-tree", "-r", "HEAD", "--", HANDLERS_PATH).splitlines():
        meta, path = line.split("\t", 1)
        found[path.removeprefix(f"{HANDLERS_PATH}/")] = meta.split()[2]
    return found


def _blob_id(data: bytes) -> str:
    """The id git gives a blob with this content."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def pack_notes(previous: HandlerManifest | None) -> str:
    """The handler commits since the previous pack, grouped as in the release notes."""
    if previous is None:
        return "First handler pack.\n"
    if not _is_ancestor(previous.commit):
        return "Handler changes since a commit no longer in the history.\n"
    subjects = git("log", "--no-merges", "--format=%s", f"{previous.commit}..HEAD", "--", *PACK_PATHS).splitlines()
    listed = listed_subjects(subjects)
    lines = section_lines(listed[:MAX_LISTED])
    if not listed:
        lines.append("No handler changes worth listing.")
    if len(listed) > MAX_LISTED:
        lines.append(f"+{len(listed) - MAX_LISTED} more changes")
    return "\n".join(lines).rstrip() + "\n"


def _is_ancestor(commit: str) -> bool:
    try:
        git("merge-base", "--is-ancestor", commit, "HEAD")
    except subprocess.CalledProcessError:
        # Not an ancestor, or a commit this clone doesn't have.
        return False
    return True


def release_text(manifest: HandlerManifest) -> str:
    """The text of the handlers-latest release."""
    return (
        f"Handler pack {manifest.version}, commit {manifest.commit[:7]}. The Windows exe downloads it "
        "on start (Settings, Update handlers on start), so there is nothing to download here.\n\n"
        f"{manifest.notes}"
    )


def _print_plan(manifest: HandlerManifest, is_new: bool) -> None:
    changed = sorted(key for key, handler in manifest.handlers.items() if handler.version == manifest.version)
    print(f"pack={str(is_new).lower()} pack_version={manifest.version} files={len(manifest.files)}", file=sys.stderr)
    if is_new:
        print(f"handlers at {manifest.version}: {', '.join(changed) or 'none'}", file=sys.stderr)
    print(manifest.notes, end="")


if __name__ == "__main__":
    sys.exit(main())
