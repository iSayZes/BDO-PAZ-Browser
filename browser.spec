# PyInstaller spec for the Windows build. From the repo root:
#
#     python -m pip install -r PAZ-Parser/requirements-build.txt
#     python build.py
#
# build.py runs PyInstaller with this spec, checks the result and zips it.
# Output: dist/BDO-PAZ-Browser/ with BDO-PAZ-Browser.exe (windowed) and
# bdo-paz-cli.exe (console, since a windowed exe has no stdout), sharing one
# _internal folder. BDO_APP_VERSION and BDO_APP_COMMIT set the version and
# commit (build.py passes them); without them, today's date and git's HEAD.
#
# The handlers go in as loose files under _internal/handlers (the bundled
# handler pack), not into the archive, so their source is hashed for the
# caches and a downloaded pack can stand in for them. They go in as a pack
# ships (updates/handler_manifest.py: no tests, LF line endings), and build.py
# adds the pack's manifest.json. The archive holds the core plus the standard
# library modules handler code may import (handler_api.py).

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(SPECPATH)
SRC = ROOT / "PAZ-Parser"
sys.path.insert(0, str(SRC))

from app_version import BUILD_INFO_NAME, parse_version, source_commit  # noqa: E402
from handler_api import STDLIB_MODULES  # noqa: E402
from updates.handler_manifest import pack_file_bytes, pack_files  # noqa: E402

APP_NAME = "BDO-PAZ-Browser"
CLI_NAME = "bdo-paz-cli"
ICON = str(SRC / "ui" / "favicon.ico")
# Top-level names under handlers/: they must come from the loose files, never the archive.
HANDLER_MODULES = sorted(
    path.stem if path.is_file() else path.name
    for path in (SRC / "handlers").iterdir()
    if path.suffix == ".py" or (path.is_dir() and path.name != "__pycache__")
)


def _build_info_file() -> str:
    version = os.environ.get("BDO_APP_VERSION") or time.strftime("%Y.%m.%d")
    parse_version(version)  # fail the build on a malformed version
    commit = os.environ.get("BDO_APP_COMMIT") or source_commit() or "unknown"
    path = Path(workpath) / BUILD_INFO_NAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"version": version, "commit": commit}), encoding="utf-8")
    return str(path)


a = Analysis(
    [str(ROOT / "browser.py")],
    pathex=[str(SRC)],
    datas=[(_build_info_file(), ".")],
    hiddenimports=sorted(STDLIB_MODULES),
    excludes=[*HANDLER_MODULES, "tests", "conftest", "bench", "pytest", "_pytest", "pyright"],
    noarchive=False,
)
pyz = PYZ(a.pure)

gui = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    console=False,
    icon=ICON,
)
cli = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=CLI_NAME,
    console=True,
    icon=ICON,
)


def _handler_pack() -> list[tuple[str, str, str]]:
    """handlers/ as a pack ships, copied to the work folder first: the
    checkout may have CRLF line endings, the pack's hashes are of LF files."""
    staged_dir = Path(workpath) / "handler-pack"
    entries = []
    for name, source in pack_files(SRC / "handlers").items():
        staged = staged_dir / name
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_bytes(pack_file_bytes(source))
        entries.append((str(Path("handlers") / name), str(staged), "DATA"))
    return entries


ui = Tree(str(SRC / "ui"), prefix="ui")

coll = COLLECT(
    gui,
    cli,
    a.binaries,
    a.datas,
    ui,
    _handler_pack(),
    name=APP_NAME,
)
