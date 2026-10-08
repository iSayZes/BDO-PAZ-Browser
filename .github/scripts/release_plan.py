"""Plan an exe release: did the app core change since the last one, its date version, its notes.

    python .github/scripts/release_plan.py                  # preview for HEAD
    python .github/scripts/release_plan.py --ref staging    # what a release PR would ship

The release workflow adds `--github-output "$GITHUB_OUTPUT" --notes-file notes.md`
and publishes when `release` is true.

Releases are tags `v<date version>` (`v2026.10.07`, `v2026.10.07.2` for a
second that day). A change under `PAZ-Parser/handlers` alone makes no exe
release: it reaches the exe as a handler pack (`handler_pack.py`). The notes
list the commit subjects since the last release that touch the app, handlers
included (merge commits and tests left out), grouped by
Conventional Commit type; docs, test, ci, chore, style and build commits are
left out. Only the newest `MAX_LISTED` are listed, then a "+N more changes"
line with a link to all of them; the first release, with no tag before it,
counts every commit up to it.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "PAZ-Parser"))

from app_version import parse_version  # noqa: E402

# What ships in the exe; the release notes list commits touching these.
APP_PATHS = (
    "PAZ-Parser",
    "browser.py",
    "browser.spec",
    "build.py",
    ":(exclude)PAZ-Parser/tests",
    ":(exclude)PAZ-Parser/bench",
    ":(exclude)PAZ-Parser/conftest.py",
    ":(exclude)PAZ-Parser/requirements-dev.txt",
    ":(exclude,glob)PAZ-Parser/**/test_*.py",
)
# A change here makes an exe release: the app without the handlers, which handler packs update.
CORE_PATHS = (*APP_PATHS, ":(exclude)PAZ-Parser/handlers")
# Release note sections, in order, by commit type; None is a subject without a type.
SECTIONS: tuple[tuple[str, frozenset[str | None]], ...] = (
    ("New", frozenset({"feat"})),
    ("Fixes", frozenset({"fix"})),
    ("Performance", frozenset({"perf"})),
    ("Other", frozenset({"refactor", "revert", None})),
)
# Commits listed in the notes; older ones are counted in a "+N more" line.
MAX_LISTED = 20
_TYPE_RE = re.compile(r"^(?P<type>[a-z]+)(\([^)]*\))?!?:\s")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def release_tags() -> list[str]:
    """Every `v<date version>` tag, oldest first."""
    tags = []
    for tag in git("tag", "--list", "v*").split():
        try:
            tags.append((parse_version(tag), tag))
        except ValueError:
            continue
    return [tag for _, tag in sorted(tags)]


def next_version(tags: list[str], today: str) -> str:
    """`today`, or `today.N` when releases that day exist already."""
    taken = [parse_version(tag) for tag in tags if parse_version(tag)[:3] == parse_version(today)]
    if not taken:
        return today
    return f"{today}.{max(version[3] if len(version) > 3 else 1 for version in taken) + 1}"


def commit_type(subject: str) -> str | None:
    match = _TYPE_RE.match(subject)
    return match.group("type") if match else None


def listed_subjects(subjects: list[str]) -> list[str]:
    """The subjects of a type the notes list (SECTIONS), in their order."""
    listed_types = frozenset().union(*(types for _, types in SECTIONS))
    return [subject for subject in subjects if commit_type(subject) in listed_types]


def section_lines(subjects: list[str]) -> list[str]:
    """`### New` and the other sections for `subjects` (newest first), each listed oldest first."""
    lines: list[str] = []
    for title, types in SECTIONS:
        picked = [subject for subject in reversed(subjects) if commit_type(subject) in types]
        if picked:
            lines += [f"### {title}", "", *(f"- {subject}" for subject in picked), ""]
    return lines


def notes(subjects: list[str], previous: str | None, version: str, repo: str | None) -> str:
    """Markdown release notes; `subjects` newest first, as `git log` gives them."""
    listed = listed_subjects(subjects)
    more = len(listed) - MAX_LISTED

    lines = ["First Windows release.", ""] if previous is None else []
    lines += section_lines(listed[:MAX_LISTED])
    if not listed:
        lines += ["No app changes worth listing.", ""]
    link = _all_commits_link(repo, previous, version)
    if more > 0:
        lines.append(f"+{more} more changes" + (f": {link}" if link else ""))
    elif link:
        lines.append(f"All commits: {link}")
    return "\n".join(lines).rstrip() + "\n"


def _all_commits_link(repo: str | None, previous: str | None, version: str) -> str | None:
    if repo is None:
        return None
    if previous is None:
        return f"https://github.com/{repo}/commits/v{version}"
    return f"https://github.com/{repo}/compare/{previous}...v{version}"


def plan(ref: str, today: str) -> tuple[bool, str, str]:
    """(release?, version, notes) for `ref` against the last release tag."""
    tags = release_tags()
    previous = tags[-1] if tags else None
    span = f"{previous}..{ref}" if previous else ref
    changed = git("diff", "--name-only", f"{previous}", ref, "--", *CORE_PATHS).strip() if previous else "first"
    subjects = git("log", "--no-merges", "--format=%s", span, "--", *APP_PATHS).splitlines()
    version = next_version(tags, today)
    return bool(changed), version, notes(subjects, previous, version, os.environ.get("GITHUB_REPOSITORY"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan a release from the commits since the last one.")
    parser.add_argument("--ref", default="HEAD", help="Commit to release (default: HEAD)")
    parser.add_argument("--github-output", metavar="FILE", help="Append release=, version= for a workflow step")
    parser.add_argument("--notes-file", metavar="FILE", help="Write the notes here instead of printing them")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    is_release, version, text = plan(args.ref, today)
    if args.notes_file:
        Path(args.notes_file).write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")
    print(f"release={str(is_release).lower()} version={version}", file=sys.stderr)
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            output.write(f"release={str(is_release).lower()}\nversion={version}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
