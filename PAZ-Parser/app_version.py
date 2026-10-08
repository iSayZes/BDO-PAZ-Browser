"""Which build of the app is running: an exe's date version and commit, or the source.

`browser.spec` writes `build_info.json` next to this module in the exe at build
time; run from source there is none. Versions are dates, `2026.10.07`, with a
`.2` for a second release that day, so they sort as tuples of numbers.
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from functools import cache
from pathlib import Path

BUILD_INFO_NAME = "build_info.json"
_BUILD_INFO_FILE = Path(__file__).parent / BUILD_INFO_NAME
_REPO_ROOT = Path(__file__).resolve().parent.parent
# Seconds; `git rev-parse` answers in milliseconds, a hung git must not hold up the app.
_GIT_TIMEOUT = 5


@dataclass(frozen=True)
class BuildInfo:
    version: str
    commit: str

    @property
    def build_id(self) -> str:
        """Stands for the core modules, which an exe holds without their source."""
        return f"{self.version}+{self.commit}"


def is_frozen() -> bool:
    """True in the PyInstaller exe."""
    return bool(getattr(sys, "frozen", False))


@cache
def build_info() -> BuildInfo | None:
    """The exe's version and commit; None when running from source."""
    try:
        saved = json.loads(_BUILD_INFO_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        logging.warning("Could not read %s", _BUILD_INFO_FILE, exc_info=True)
        return None
    version, commit = saved.get("version"), saved.get("commit")
    if not isinstance(version, str) or not isinstance(commit, str):
        logging.warning("%s has no version and commit", _BUILD_INFO_FILE)
        return None
    return BuildInfo(version, commit)


@cache
def source_commit() -> str | None:
    """The short commit of the checkout the code runs from, or None without git or a checkout.

    None in the exe too: its folder may sit inside someone else's checkout.
    """
    result = _git("rev-parse", "--short", "HEAD")
    commit = result.stdout.strip() if result is not None else ""
    return commit if result is not None and result.returncode == 0 and commit else None


def source_commit_of(paths: list[Path]) -> str | None:
    """The short commit that last changed any of `paths`, with a `+` when they have uncommitted edits.

    None without git or a checkout, in the exe, or when none of them is committed.
    """
    if not paths:
        return None
    names = [str(path) for path in paths]
    log = _git("log", "-1", "--format=%h", "--", *names)
    commit = log.stdout.strip() if log is not None and log.returncode == 0 else ""
    if not commit:
        return None
    # `git diff --quiet` exits with 1 when a file differs from HEAD.
    diff = _git("diff", "--quiet", "HEAD", "--", *names)
    return f"{commit}+" if diff is not None and diff.returncode == 1 else commit


def _git(*args: str) -> subprocess.CompletedProcess[str] | None:
    """Run git in the checkout; None in the exe or when git can't run."""
    if is_frozen():
        return None
    try:
        return subprocess.run(
            ["git", *args],
            cwd=_REPO_ROOT, capture_output=True, text=True, timeout=_GIT_TIMEOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except (OSError, subprocess.SubprocessError):
        return None


def parse_version(text: str) -> tuple[int, ...]:
    """`2026.10.07.2` as (2026, 10, 7, 2). Raises ValueError for anything else."""
    parts = text.removeprefix("v").split(".")
    if len(parts) not in (3, 4) or not all(part.isdigit() for part in parts):
        raise ValueError(f"{text!r} is not a date version like 2026.10.07")
    return tuple(int(part) for part in parts)
