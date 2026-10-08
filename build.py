"""Build the Windows exe: PyInstaller with browser.spec, a handler check, then the zip.

    python -m pip install -r PAZ-Parser/requirements-build.txt
    python build.py                        # version: today's date
    python build.py --version 2026.10.12   # what the release workflow passes

Writes dist/BDO-PAZ-Browser/ and dist/BDO-PAZ-Browser-v<version>-windows.zip,
with a .sha256 file next to the zip. PyInstaller's work folder, build/, is
deleted after a successful run and kept after a failed one for its logs.

The bundled handler pack gets its manifest.json: the release workflow's
(`--handler-manifest`, the pack it publishes) or, for a local build, one made
here with every handler at the build's version. The build fails when the
bundled handler files differ from the manifest.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import time
import zipfile
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "PAZ-Parser"))

from app_version import parse_version, source_commit  # noqa: E402
from bdo_preview import BUNDLED_HANDLERS_DIR, load_plugins  # noqa: E402
from handler_api import HANDLER_API  # noqa: E402
from updates.handler_manifest import (  # noqa: E402
    MANIFEST_NAME,
    HandlerManifest,
    ManifestError,
    file_hashes,
    read_manifest,
    write_manifest,
)
from updates.handler_sets import pack_manifest  # noqa: E402

APP_NAME = "BDO-PAZ-Browser"
CLI_EXE = "bdo-paz-cli.exe"
SPEC = ROOT / "browser.spec"
DIST_DIR = ROOT / "dist"
WORK_DIR = ROOT / "build"
# Where PyInstaller puts the bundled handler pack, under the dist folder.
BUNDLED_PACK = Path("_internal") / "handlers"
# Lines of the handler list diff shown when the exe and the source disagree.
_MAX_DIFF_LINES = 40
_HASH_CHUNK = 1024 * 1024


class BuildError(Exception):
    """A build step failed; the message says which and what to do."""


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    version = args.version or time.strftime("%Y.%m.%d")
    try:
        _check_version(version)
        _check_environment()
        manifest = _handler_manifest(args.handler_manifest, version)
        app_dir = _run_pyinstaller(version)
        _check_handlers(app_dir)
        _bundle_manifest(app_dir, manifest)
        print(f"build: {app_dir}")
        if not args.no_zip:
            zip_path = _write_zip(app_dir, version)
            print(f"build: {zip_path}")
            print(f"build: {_write_sha256(zip_path)}")
    except BuildError as ex:
        print(f"build: {ex}", file=sys.stderr)
        return 1
    return 0


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="build", description="Build the Windows exe and its zip.")
    parser.add_argument("--version", metavar="YYYY.MM.DD[.N]", help="Date version (default: today)")
    parser.add_argument("--no-zip", action="store_true", help="Stop after the checked dist folder")
    parser.add_argument(
        "--handler-manifest", metavar="FILE",
        help="manifest.json of the bundled handler pack (default: made here, every handler at --version)",
    )
    return parser.parse_args(argv)


def _check_version(version: str) -> None:
    try:
        parse_version(version)
    except ValueError as ex:
        raise BuildError(str(ex)) from ex


def _check_environment() -> None:
    if sys.platform != "win32":
        raise BuildError("the exe builds on Windows only")
    if importlib.util.find_spec("PyInstaller") is None:
        raise BuildError("PyInstaller is missing: python -m pip install -r PAZ-Parser/requirements-build.txt")


def _run_pyinstaller(version: str) -> Path:
    command = [
        sys.executable, "-m", "PyInstaller", str(SPEC),
        "--noconfirm", "--clean", "--distpath", str(DIST_DIR), "--workpath", str(WORK_DIR),
    ]
    result = subprocess.run(command, cwd=ROOT, env={**os.environ, "BDO_APP_VERSION": version})
    if result.returncode != 0:
        raise BuildError(f"PyInstaller failed with exit code {result.returncode}; its logs are in {WORK_DIR}")
    shutil.rmtree(WORK_DIR, ignore_errors=True)
    return DIST_DIR / APP_NAME


def _handler_keys(command: list[str]) -> list[str]:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise BuildError(f"{Path(command[-2]).name} --handlers failed:\n{result.stdout}{result.stderr}")
    return result.stdout.splitlines()


def _check_handlers(app_dir: Path) -> None:
    """The exe must register the same handlers as the source; a failed import would drop one."""
    source = _handler_keys([sys.executable, str(ROOT / "browser.py"), "--handlers"])
    built = _handler_keys([str(app_dir / CLI_EXE), "--handlers"])
    if built != source:
        diff = list(difflib.unified_diff(source, built, "source", "exe", lineterm=""))
        raise BuildError("the exe's handlers differ from the source:\n" + "\n".join(diff[:_MAX_DIFF_LINES]))
    print(f"build: the exe registers all {len(built)} handlers")


def _handler_manifest(path: str | None, version: str) -> HandlerManifest:
    """The given manifest, or one for the handlers of this checkout."""
    if path is None:
        load_plugins(BUNDLED_HANDLERS_DIR)
        return pack_manifest(BUNDLED_HANDLERS_DIR, version, source_commit() or "unknown", HANDLER_API)
    try:
        manifest = read_manifest(Path(path))
    except (OSError, ManifestError) as ex:
        raise BuildError(f"could not read the handler manifest {path}: {ex}") from ex
    if manifest.handler_api != HANDLER_API:
        raise BuildError(f"{path} is for handler API {manifest.handler_api}, this code has {HANDLER_API}")
    return manifest


def _bundle_manifest(app_dir: Path, manifest: HandlerManifest) -> None:
    """Write manifest.json into the bundled pack, whose files must be the manifest's."""
    pack_dir = app_dir / BUNDLED_PACK
    bundled = file_hashes(pack_dir)
    if bundled != dict(manifest.files):
        names = sorted({name for name, _ in set(bundled.items()) ^ set(manifest.files.items())})
        listed = "\n".join(names[:_MAX_DIFF_LINES])
        raise BuildError(f"the bundled handler files differ from the manifest in {len(names)} files:\n{listed}")
    write_manifest(manifest, pack_dir / MANIFEST_NAME)
    print(f"build: handler pack {manifest.version} with {len(manifest.files)} files")


def _write_zip(app_dir: Path, version: str) -> Path:
    """The dist folder as `BDO-PAZ-Browser-v<version>-windows.zip`, with the folder inside."""
    zip_path = DIST_DIR / f"{APP_NAME}-v{version}-windows.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(app_dir.rglob("*")):
            if path.is_file():
                archive.write(path, Path(APP_NAME) / path.relative_to(app_dir))
    return zip_path


def _write_sha256(path: Path) -> Path:
    """`<hash>  <name>` in `<name>.sha256`, the format `sha256sum -c` reads."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        while chunk := file.read(_HASH_CHUNK):
            digest.update(chunk)
    sha_path = path.with_name(f"{path.name}.sha256")
    # LF even on Windows: `sha256sum -c` reads a CR as part of the file name.
    sha_path.write_text(f"{digest.hexdigest()}  {path.name}\n", encoding="utf-8", newline="\n")
    return sha_path


if __name__ == "__main__":
    sys.exit(main())
