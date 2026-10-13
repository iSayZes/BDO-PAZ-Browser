"""The machine and code a benchmark ran on, so results compare like with like."""
from __future__ import annotations

import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from paz import native_backend

_GIT_TIMEOUT_S = 10


@dataclass(frozen=True)
class Machine:
    cpu_model: str | None
    logical_cpus: int | None
    ram_bytes: int | None
    power_plan: str | None
    os: str
    python: str
    git_commit: str | None
    # Tracked files changed since the commit; untracked files do not count.
    is_git_dirty: bool | None
    # "native" with `_bdo_native` installed, else "python"; None in a schema 1 file.
    decoders: str | None


def describe_machine(repo_root: Path) -> Machine:
    commit, is_dirty = _git_state(repo_root)
    return Machine(
        cpu_model=_cpu_model(),
        logical_cpus=os.cpu_count(),
        ram_bytes=_total_ram_bytes(),
        power_plan=_power_plan(),
        os=platform.platform(),
        python=f"{platform.python_implementation()} {platform.python_version()}",
        git_commit=commit,
        is_git_dirty=is_dirty,
        decoders=native_backend.NAME,
    )


def _cpu_model() -> str | None:
    if sys.platform == "win32":
        from . import win32

        return win32.cpu_model()
    if sys.platform == "linux":
        try:
            for line in Path("/proc/cpuinfo").read_text(encoding="utf-8").splitlines():
                key, _, value = line.partition(":")
                if key.strip() == "model name":
                    return value.strip()
        except OSError:
            return None
    return platform.processor() or None


def _total_ram_bytes() -> int | None:
    if sys.platform == "win32":
        from . import win32

        try:
            return win32.total_ram_bytes()
        except OSError:
            return None
    if sys.platform == "linux":
        try:
            return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
        except (OSError, ValueError):
            return None
    return None


def _power_plan() -> str | None:
    if sys.platform == "win32":
        from . import win32

        return win32.power_plan()
    return None


def _git_state(repo_root: Path) -> tuple[str | None, bool | None]:
    commit = _git(repo_root, "rev-parse", "HEAD")
    status = _git(repo_root, "status", "--porcelain", "--untracked-files=no")
    return commit, (None if status is None else bool(status))


def _git(repo_root: Path, *args: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=_GIT_TIMEOUT_S,
            check=True,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return completed.stdout.strip()
