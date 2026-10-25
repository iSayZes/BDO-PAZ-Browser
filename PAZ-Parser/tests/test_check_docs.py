"""check_docs.py picking test client folders for --version, and its worker processes."""
from __future__ import annotations

import struct
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

import check_docs  # noqa: E402
from check_docs import CheckError, PazSource, client_folders  # noqa: E402
from format_docs.check_run import Client, Status  # noqa: E402

_TABLE = "| Offset | Type | Field | Notes |\n| --- | --- | --- | --- |\n"
DOC = (
    "# `test.bss` Format\n\n## Purpose\n\nRows.\n\n## Versions\n\n"
    "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->\n\n"
    "<!-- versions:end -->\n\n## Layout 1\n\n"
    f"### File Layout\n\n{_TABLE}| `+0x00` | u32 | count | note |\n| `+0x04` | Row[count] | rows | note |\n\n"
    f"### Row (8 bytes)\n\n{_TABLE}| `+0x00` | u32 | key | note |\n| `+0x04` | u32 | unknown_04 | note |\n"
)
ROW_FILE = struct.pack("<I", 1) + struct.pack("<II", 1, 0)


@pytest.fixture
def test_clients(tmp_path: Path) -> Path:
    for region, name in (("NAEU", "3251"), ("NAEU", "794"), ("KR", "1230")):
        (tmp_path / region / name / "Paz").mkdir(parents=True)
    (tmp_path / "NAEU" / "2107").mkdir()
    return tmp_path


def paz(root: Path, region: str, client: int) -> tuple[int, Path]:
    return client, root / region / str(client) / "Paz"


def test_all_takes_every_numbered_folder_with_a_paz_folder_of_every_region_newest_first(test_clients: Path) -> None:
    found = client_folders(test_clients, "all")

    assert found == [paz(test_clients, "NAEU", 3251), paz(test_clients, "KR", 1230), paz(test_clients, "NAEU", 794)]


def test_a_number_takes_that_folder_from_its_region_and_a_missing_one_or_other_text_is_an_error(test_clients: Path) -> None:
    assert client_folders(test_clients, "1230") == [paz(test_clients, "KR", 1230)]
    for version in ("2107", "latest"):
        with pytest.raises(CheckError):
            client_folders(test_clients, version)


def test_all_from_a_number_starts_at_that_client_and_goes_on_to_older_ones(test_clients: Path) -> None:
    assert client_folders(test_clients, "all", 3000) == [paz(test_clients, "KR", 1230), paz(test_clients, "NAEU", 794)]
    assert client_folders(test_clients, "all", 1230)[0] == paz(test_clients, "KR", 1230)
    with pytest.raises(CheckError):
        client_folders(test_clients, "all", 500)


def test_all_starts_with_the_live_client_unless_the_run_resumes_at_an_older_one(
    test_clients: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    live = PazSource("live", 3483)
    monkeypatch.setattr(check_docs, "TEST_CLIENTS", test_clients)
    monkeypatch.setattr(check_docs, "_meta_client", lambda folder: int(folder.parent.name))
    monkeypatch.setattr(
        check_docs, "_live_client", lambda numbers, first: iter([live] if first is None or first >= live.number else [])
    )

    every = list(check_docs._each_client(check_docs._arguments(["--all", "--version", "all"])))
    resumed = list(check_docs._each_client(check_docs._arguments(["--all", "--version", "all", "--from", "1230"])))

    assert [source.number for source in every if source is not None] == [3483, 3251, 1230, 794]
    assert [source.number for source in resumed if source is not None] == [1230, 794]


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


def test_a_worker_keeps_the_clients_in_flight_open_and_lets_the_oldest_go(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    opened: list[PazSource] = []

    def open_client(source: PazSource, quiet: bool = False) -> Client:
        opened.append(source)
        return Client(source.number, lambda name: None)

    monkeypatch.setattr(check_docs, "_open_client", open_client)
    monkeypatch.setattr(check_docs, "_worker_clients", check_docs.OrderedDict())
    monkeypatch.setattr(check_docs, "CLIENTS_IN_FLIGHT", 3)
    doc = tmp_path / "x_bss.md"
    doc.write_text("# x.bss\n", encoding="utf-8")
    a, b, c, d = (PazSource(f"{number}/Paz", number) for number in (1230, 1784, 2107, 3251))

    outcomes = [check_docs._check_in_worker(doc, source, False) for source in (a, b, a, c, a, d, a, b)]

    assert opened == [a, b, c, d, b]  # d lets b go (a was used since), so b opens again
    assert {outcome.status for outcome in outcomes} == {Status.NOT_CONVERTED}


def test_pending_docs_merge_each_clients_change_and_write_them_on_flush(tmp_path: Path) -> None:
    from format_docs.check_run import check_doc_file
    from format_docs.versions import ClientCheck, read_clients

    doc = tmp_path / "test_bss.md"
    doc.write_text(DOC, encoding="utf-8")
    before = doc.read_text(encoding="utf-8")
    rows = {"test_bss.md": [("test.bss", "Rows")]}
    pending = check_docs.PendingDocs(flush_seconds=3600)

    for number in (1784, 3473):
        client = Client(number, lambda name: ROW_FILE if name == "test.bss" else None)
        pending.add([check_doc_file(doc, rows, client, defer_write=True)])
        pending.flush_if_due()

    assert doc.read_text(encoding="utf-8") == before
    pending.flush()
    assert read_clients(doc.read_text(encoding="utf-8")) == (ClientCheck(3473, 1, True), ClientCheck(1784, 1, True))
