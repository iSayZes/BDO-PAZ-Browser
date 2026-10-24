"""check_docs.py picking test client folders for --version, and its worker processes."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

import check_docs  # noqa: E402
from check_docs import CheckError, PazSource, client_folders  # noqa: E402
from format_docs.check_run import Client, Status  # noqa: E402


@pytest.fixture
def test_clients(tmp_path: Path) -> Path:
    for region, name in (("NAEU", "3251"), ("NAEU", "794"), ("KR", "1230")):
        (tmp_path / region / name / "Paz").mkdir(parents=True)
    (tmp_path / "NAEU" / "2107").mkdir()
    return tmp_path


def paz(root: Path, region: str, client: int) -> tuple[int, Path]:
    return client, root / region / str(client) / "Paz"


def test_all_takes_every_numbered_folder_with_a_paz_folder_of_every_region_oldest_first(test_clients: Path) -> None:
    found = client_folders(test_clients, "all")

    assert found == [paz(test_clients, "NAEU", 794), paz(test_clients, "KR", 1230), paz(test_clients, "NAEU", 3251)]


def test_a_number_takes_that_folder_from_its_region_and_a_missing_one_or_other_text_is_an_error(test_clients: Path) -> None:
    assert client_folders(test_clients, "1230") == [paz(test_clients, "KR", 1230)]
    for version in ("2107", "latest"):
        with pytest.raises(CheckError):
            client_folders(test_clients, version)


def test_all_from_a_number_starts_at_that_client_and_past_the_newest_is_an_error(test_clients: Path) -> None:
    assert client_folders(test_clients, "all", 1000) == [paz(test_clients, "KR", 1230), paz(test_clients, "NAEU", 3251)]
    assert client_folders(test_clients, "all", 1230)[0] == paz(test_clients, "KR", 1230)
    with pytest.raises(CheckError):
        client_folders(test_clients, "all", 4000)


def test_one_number_in_two_regions_or_a_client_outside_a_region_is_an_error(test_clients: Path, tmp_path: Path) -> None:
    (test_clients / "KR" / "3251" / "Paz").mkdir(parents=True)
    with pytest.raises(CheckError, match="3251 is in"):
        client_folders(test_clients, "all")

    loose = tmp_path / "loose"
    (loose / "1784" / "Paz").mkdir(parents=True)
    with pytest.raises(CheckError, match="not a region"):
        client_folders(loose, "1784")


def test_jobs_takes_at_least_one_worker() -> None:
    with pytest.raises(SystemExit):
        check_docs._arguments(["--all", "--jobs", "0"])
    assert check_docs._arguments(["--all", "--jobs", "1"]).jobs == 1


def test_a_worker_opens_each_client_once_and_again_after_another(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    opened: list[PazSource] = []

    def open_client(source: PazSource) -> Client:
        opened.append(source)
        return Client(source.number, lambda name: None)

    monkeypatch.setattr(check_docs, "_open_client", open_client)
    monkeypatch.setattr(check_docs, "_worker_client", None)
    doc = tmp_path / "x_bss.md"
    doc.write_text("# x.bss\n", encoding="utf-8")
    old, new = PazSource("old/Paz", 1230), PazSource("new/Paz", 3251)

    outcomes = [check_docs._check_in_worker(doc, source, False) for source in (old, old, new, old)]

    assert opened == [old, new, old]
    assert {outcome.status for outcome in outcomes} == {Status.NOT_CONVERTED}
