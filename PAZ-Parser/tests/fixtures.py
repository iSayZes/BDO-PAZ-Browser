from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from .models import HandlerCase


PAZ_PARSER_DIR = Path(__file__).parents[1].resolve()
REPO_ROOT = PAZ_PARSER_DIR.parent
FIXTURES_DIR = Path(
    os.environ.get("PAZ_PARSER_FIXTURES_DIR", PAZ_PARSER_DIR / "tests" / "fixtures")
).resolve()


def ensure_fixtures(case: HandlerCase) -> dict[str, Path]:
    fixture_paths = resolve_fixture_paths(case)
    missing = [name for name, path in fixture_paths.items() if not path.exists()]
    if missing:
        fetch_fixtures(missing)

    missing = [name for name, path in fixture_paths.items() if not path.exists()]
    if missing:
        pytest.fail(f"fixtures unavailable after fetch: {', '.join(missing)}")

    return fixture_paths


def resolve_fixture_paths(case: HandlerCase) -> dict[str, Path]:
    paths: dict[str, Path] = {str(case.data_file): FIXTURES_DIR / case.data_file}
    for relative_path in case.companion_files.values():
        paths[str(relative_path)] = FIXTURES_DIR / relative_path
    if case.loc_file is not None:
        paths[str(case.loc_file)] = FIXTURES_DIR / case.loc_file
    return paths


def fetch_fixtures(fixture_names: list[str]) -> None:
    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    browser = REPO_ROOT / "browser.py"

    for fixture_name in fixture_names:
        command = [
            sys.executable,
            str(browser),
            "--file",
            fixture_name,
            "--output",
            str(FIXTURES_DIR),
        ]
        result = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            if copy_external_fixture(fixture_name):
                continue

            details = "\n".join(part for part in (result.stdout, result.stderr) if part)
            pytest.fail(
                f"could not fetch fixture {fixture_name!r} via browser.py --file. "
                f"Check PAZ folder config or pass --paz-folder manually once.\n{details}"
            )


def copy_external_fixture(fixture_name: str) -> bool:
    source = find_external_fixture(fixture_name)
    if source is None:
        return False

    shutil.copy2(source, FIXTURES_DIR / fixture_name)
    return True


def find_external_fixture(fixture_name: str) -> Path | None:
    config_path = PAZ_PARSER_DIR / "paz_config.json"
    try:
        paz_folder = Path(json.loads(config_path.read_text()).get("last_folder", ""))
    except Exception:
        return None

    if not paz_folder:
        return None

    game_root = paz_folder.parent
    candidates = [
        game_root / fixture_name,
        game_root / "ads" / fixture_name,
        paz_folder / fixture_name,
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None
