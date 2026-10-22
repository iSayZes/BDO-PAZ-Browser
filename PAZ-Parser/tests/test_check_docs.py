"""check_docs.py picking test client folders for --version."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from check_docs import CheckError, client_folders  # noqa: E402


@pytest.fixture
def test_clients(tmp_path: Path) -> Path:
    for name in ("3251", "794", "1230"):
        (tmp_path / name / "Paz").mkdir(parents=True)
    (tmp_path / "2107").mkdir()
    return tmp_path


def test_all_takes_every_folder_named_by_a_number_with_a_paz_folder_oldest_first(test_clients: Path) -> None:
    found = client_folders(test_clients, "all")

    assert found == [(794, test_clients / "794" / "Paz"), (1230, test_clients / "1230" / "Paz"), (3251, test_clients / "3251" / "Paz")]


def test_a_number_takes_that_folder_and_a_missing_one_or_other_text_is_an_error(test_clients: Path) -> None:
    assert client_folders(test_clients, "1230") == [(1230, test_clients / "1230" / "Paz")]
    for version in ("2107", "latest"):
        with pytest.raises(CheckError):
            client_folders(test_clients, version)
