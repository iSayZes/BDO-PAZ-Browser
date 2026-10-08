"""`--check-app-update`, `--update-app [ZIP]` and `--update-handlers`: updates from the command line."""
from __future__ import annotations

import argparse
from pathlib import Path

from app_version import build_info, parse_version
from updates.install import (
    PreparedUpdate,
    fetch_release,
    install_from_zip,
    other_instances_running,
    running_app_dir,
    start_swap,
    unpack,
)
from updates.handler_packs import PackCheck, check_for_update, clean_up_packs
from updates.releases import RELEASES_PAGE, UpdateError, newer_release, newest_release

from .stdio import error, progress

# Megabytes between download progress lines.
_PROGRESS_STEP_MB = 5


def run_check_app_update(args: argparse.Namespace) -> int:
    """Print this app's version and the newest release; never installs."""
    info = build_info()
    try:
        release = newest_release()
    except UpdateError as ex:
        error(str(ex))
        return 1

    print(f"This app: {'v' + info.version if info else 'running from source'}")
    if release is None:
        print("No release published yet.")
        return 0
    print(f"Newest release: v{release.version}  {release.page_url}")
    if info is None:
        print("From source, update with git pull.")
    elif parse_version(release.version) > parse_version(info.version):
        print("Update with: bdo-paz-cli.exe --update-app")
    else:
        print("Up to date.")
    return 0


def run_update_app(args: argparse.Namespace) -> int:
    """Install the newest release, or the release zip given, once this command exits."""
    info = build_info()
    if info is None:
        error("--update-app works in the Windows exe; from source, update with git pull")
        return 1
    if other_instances_running():
        error("close the other BDO PAZ Browser windows and commands first")
        return 1
    try:
        update = _install_zip(Path(args.update_app), info.version) if args.update_app else _install_newest(info.version)
    except UpdateError as ex:
        error(str(ex))
        return 1
    if update is None:
        print(f"v{info.version} is the newest release.")
        return 0
    print(f"v{update.version} installs when this command exits; the log is %TEMP%\\BDO-PAZ-Browser-update.log")
    return 0


def _install_zip(zip_path: Path, current: str) -> PreparedUpdate:
    progress(f"Checking {zip_path.name}")
    return install_from_zip(zip_path, current, restart_gui=False)


def _install_newest(current: str) -> PreparedUpdate | None:
    release = newer_release(current)
    if release is None:
        return None
    app_dir = running_app_dir()
    reported = [0]

    def report(done: int, total: int) -> None:
        mb = done // 1_048_576
        if mb >= reported[0] + _PROGRESS_STEP_MB or done == total:
            reported[0] = mb
            progress(f"Downloading v{release.version}: {mb} of {total // 1_048_576} MB")

    zip_path = fetch_release(release, app_dir, report)
    update = unpack(zip_path, release.version, app_dir)
    zip_path.unlink(missing_ok=True)
    start_swap(update, restart_gui=False)
    return update


def update_handlers() -> tuple[int, bool]:
    """`--update-handlers`: install a newer handler pack. Returns (exit code, installed?).

    The only CLI path that asks GitHub for handlers, so scripted runs
    without it behave the same every time.
    """
    if build_info() is None:
        error("--update-handlers works in the Windows exe; from source the handlers are PAZ-Parser/handlers")
        return 1, False
    clean_up_packs()
    progress("Checking for handler updates")
    try:
        check = check_for_update()
    except UpdateError as ex:
        error(str(ex))
        return 1, False
    print(describe_pack_check(check))
    return 0, check.outcome == "installed"


def describe_pack_check(check: PackCheck) -> str:
    version = check.latest.version
    if check.outcome == "installed":
        return f"Installed handler pack {version} ({check.downloaded} files downloaded)."
    if check.outcome == "needs_app":
        return f"Handler pack {version} needs a newer app: {RELEASES_PAGE}"
    if check.outcome == "bad":
        return f"Handler pack {version} failed to load before; keeping the current handlers."
    return f"Handlers are up to date ({version})."
