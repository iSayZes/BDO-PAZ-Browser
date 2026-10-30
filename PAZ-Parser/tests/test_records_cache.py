"""The parsed records disk cache: storage, dependency keys, sort orders, the hooks."""

from __future__ import annotations

import sqlite3
from array import array
from collections.abc import Callable, Iterator
from pathlib import Path

import pytest

from _common.client_versions import ClientRange, client_order
from _common.data_deps import CLIENT, LOC, index_dep, recording
from _common.effective_client import effective_client
from _common.loc import loc_text
from _common.lookup_index import IndexKind, lookup
from api.bdo_records_prefill import PrefillProgress, RecordsPrefill
from api.bdo_records_store import ABSENT, DataDigests, RecordStore, paz_entry_identity
from bdo_models import PazEntry
from bdo_preview import PreviewHandler, set_records_source
from paz.bdo_records_cache import CACHE_FILE, CachedRecords, CurrentDigest, RecordsCache, RecordsStamp
from table_sort import SORT_ASC, SORT_DESC, TableSort

_ARCHIVE = "pad00001.paz"
_TABLE = PazEntry(_ARCHIVE, "gamecommondata/binary/table.dbss", 64, 10, 10, 0, 0)
_COMPANION = PazEntry(_ARCHIVE, "gamecommondata/binary/tableoffset.dbss", 128, 4, 4, 0, 0)
_DISK = PazEntry("<disk>", "languagedata_en.loc", 0, 4, 4, 0, 0)
_RECORDS = [{"id": 1, "name": "Alpha"}, {"id": 2, "name": "Beta"}]
_BY_ID_DESC = TableSort("id", SORT_DESC)
_BY_ID_ASC = TableSort("id", SORT_ASC)


class _Handler(PreviewHandler):
    """Builds `_RECORDS`, reading whatever shared data `reads` asks for."""

    def __init__(self, reads: Callable[[], object] = lambda: None) -> None:
        self._reads = reads
        self.builds = 0
        self.sorts = 0

    def companions(self, entry: PazEntry) -> list[str]:
        return [_COMPANION.internal_path]

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        self.builds += 1
        self._reads()
        return [dict(record) for record in _RECORDS]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        return ""

    def sortable_fields(self) -> tuple[str, ...]:
        return ("id",)

    def records_sort_order(self, records: list[dict], sort: TableSort) -> list[int]:
        self.sorts += 1
        return super().records_sort_order(records, sort)


class _IndexSortHandler(_Handler):
    """Sorts from its own index, so its orders are never cached."""

    def _build_sort_order(
        self, data: bytes, entry: PazEntry, companions: dict[str, bytes], sort: TableSort
    ) -> list[int]:
        self.sorts += 1
        return [1, 0]


class _Archives:
    """The PAZ side of the keys: one archive whose CRC a test can change."""

    def __init__(self) -> None:
        self.crc = 0x1234

    def identity(self, entry: PazEntry) -> str | None:
        return paz_entry_identity(entry, self.crc, 4096) if entry.archive_name == _ARCHIVE else None

    def resolve(self, path: str) -> PazEntry | None:
        return {e.internal_path: e for e in (_TABLE, _COMPANION)}.get(path)


@pytest.fixture
def archives() -> _Archives:
    return _Archives()


@pytest.fixture
def digests() -> DataDigests:
    return DataDigests()


@pytest.fixture
def store(tmp_path: Path, archives: _Archives, digests: DataDigests) -> Iterator[RecordStore]:
    store = _open_store(tmp_path, archives, digests)
    yield store
    store.close()


def _open_store(root: Path, archives: _Archives, digests: DataDigests) -> RecordStore:
    return RecordStore(RecordsCache(root), digests, archives.identity, archives.resolve)


def _records_through(store: RecordStore, handler: _Handler, entry: PazEntry = _TABLE) -> list[dict]:
    """One parse through the store, with its background write finished."""
    records = store.records(handler, entry, lambda: handler.get_records(b"", entry, {}))
    store._writer.submit(lambda: None).result()
    return records


# ── RecordsCache ─────────────────────────────────────────────────────────────


def _records_of(cached: CachedRecords | None) -> list[dict] | None:
    return None if cached is None else cached.records


def _today(digests: dict[str, str]) -> CurrentDigest:
    """Today's digests for a test, with everything else absent."""
    return lambda name: digests.get(name, ABSENT)


def test_cache_round_trips_records(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {LOC: "loc1"}), _RECORDS)

    assert _records_of(cache.get("a.dbss", "key", _today({LOC: "loc1"}))) == _RECORDS
    cache.close()


def test_cache_misses_on_another_input_key(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {}), _RECORDS)

    assert cache.get("a.dbss", "other", _today({})) is None
    cache.close()


def test_cache_misses_when_a_read_dependency_changed(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {LOC: "loc1"}), _RECORDS)

    assert cache.get("a.dbss", "key", _today({LOC: "loc2"})) is None
    assert not cache.is_current("a.dbss", "key", _today({LOC: "loc2"}))
    cache.close()


def test_cache_ignores_dependencies_the_build_did_not_read(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {LOC: "loc1"}), _RECORDS)
    today = {LOC: "loc1", index_dep("item_icon"): "changed"}

    assert _records_of(cache.get("a.dbss", "key", _today(today))) == _RECORDS
    cache.close()


def test_cache_drops_an_unreadable_row(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {}), _RECORDS)
    assert cache._conn is not None
    cache._conn.execute("UPDATE records SET records = ?", (b"not a pickle",))

    assert cache.get("a.dbss", "key", _today({})) is None
    assert not cache.is_current("a.dbss", "key", _today({}))
    cache.close()


def test_an_outdated_store_is_emptied_and_shrunk(tmp_path: Path) -> None:
    conn = sqlite3.connect(tmp_path / CACHE_FILE)
    conn.execute("CREATE TABLE records (path TEXT, blob BLOB)")
    conn.execute("INSERT INTO records VALUES (?, ?)", ("a.dbss", b"x" * 1_000_000))
    conn.execute("PRAGMA user_version = 0")
    conn.commit()
    conn.close()
    before = (tmp_path / CACHE_FILE).stat().st_size

    RecordsCache(tmp_path).close()

    assert (tmp_path / CACHE_FILE).stat().st_size < before


def test_a_store_that_cannot_open_is_disabled(tmp_path: Path) -> None:
    (tmp_path / CACHE_FILE).mkdir()

    cache = RecordsCache(tmp_path)
    cache.put("a.dbss", RecordsStamp.of("key", {}), _RECORDS)

    assert cache.error
    assert cache.get("a.dbss", "key", _today({})) is None


def test_an_order_is_served_only_for_its_records_stamp(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    stamp = RecordsStamp.of("key", {LOC: "loc1"})
    cache.put("a.dbss", stamp, _RECORDS)
    cache.put_order("a.dbss", "id:desc", stamp, array("I", [1, 0]))

    assert list(cache.get_order("a.dbss", "id:desc", stamp) or []) == [1, 0]
    assert cache.get_order("a.dbss", "id:desc", RecordsStamp.of("key", {LOC: "loc2"})) is None
    assert cache.get_order("a.dbss", "id:asc", stamp) is None
    cache.close()


def test_new_records_drop_the_orders_of_the_old_ones(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    old = RecordsStamp.of("key", {LOC: "loc1"})
    cache.put("a.dbss", old, _RECORDS)
    cache.put_order("a.dbss", "id:desc", old, array("I", [1, 0]))

    cache.put("a.dbss", RecordsStamp.of("key", {LOC: "loc2"}), _RECORDS)

    assert cache.get_order("a.dbss", "id:desc", old) is None
    cache.close()


def test_is_current_with_a_sort_needs_its_order(tmp_path: Path) -> None:
    cache = RecordsCache(tmp_path)
    stamp = RecordsStamp.of("key", {})
    cache.put("a.dbss", stamp, _RECORDS)

    assert cache.is_current("a.dbss", "key", _today({}))
    assert not cache.is_current("a.dbss", "key", _today({}), "id:desc")

    cache.put_order("a.dbss", "id:desc", stamp, array("I", [1, 0]))

    assert cache.is_current("a.dbss", "key", _today({}), "id:desc")
    cache.close()


# ── data_deps ────────────────────────────────────────────────────────────────


def test_recording_collects_loc_and_index_reads() -> None:
    with recording() as deps:
        loc_text(0, 1)
        lookup(IndexKind.ITEM_ICON, 1)

    assert deps == {LOC, index_dep(IndexKind.ITEM_ICON.value)}


def test_reads_outside_a_recording_are_not_collected() -> None:
    loc_text(0, 1)

    with recording() as deps:
        pass

    assert deps == set()


# ── DataDigests ──────────────────────────────────────────────────────────────


def test_digests_report_absent_until_set(digests: DataDigests) -> None:
    assert digests.get(LOC) == ABSENT

    digests.set_loc(b"loc bytes")

    assert digests.get(LOC) != ABSENT


def test_setting_the_same_data_keeps_the_generation(digests: DataDigests) -> None:
    digests.set_indexes({"item_icon": "d1"})
    generation = digests.generation

    digests.set_indexes({"item_icon": "d1"})

    assert digests.generation == generation


def test_setting_indexes_replaces_every_index_digest(digests: DataDigests) -> None:
    digests.set_loc(b"loc bytes")
    digests.set_indexes({"item_icon": "d1"})

    digests.set_indexes({"quest_icon": "d2"})

    assert digests.get(index_dep("item_icon")) == ABSENT
    assert digests.get(index_dep("quest_icon")) == "d2"
    assert digests.get(LOC) != ABSENT


def test_the_client_digest_is_its_version_until_cleared(digests: DataDigests) -> None:
    digests.set_client(1784)
    assert digests.get(CLIENT) == "1784"

    digests.set_client(None)
    assert digests.get(CLIENT) == ABSENT


# ── RecordStore ──────────────────────────────────────────────────────────────


def test_a_saved_parse_is_served_without_building(store: RecordStore) -> None:
    handler = _Handler()
    _records_through(store, handler)

    assert _records_through(store, handler) == _RECORDS
    assert handler.builds == 1


def test_a_changed_archive_rebuilds(store: RecordStore, archives: _Archives) -> None:
    handler = _Handler()
    _records_through(store, handler)

    archives.crc = 0x5678
    _records_through(store, handler)

    assert handler.builds == 2


def test_another_language_rebuilds(store: RecordStore) -> None:
    handler = _Handler()
    _records_through(store, handler)

    handler.lang = "de"
    _records_through(store, handler)

    assert handler.builds == 2


def test_new_loc_rebuilds_only_tables_that_read_it(store: RecordStore, digests: DataDigests) -> None:
    digests.set_loc(b"patch 1")
    reads_loc = _Handler(lambda: loc_text(0, 1))
    reads_nothing = _Handler()
    _records_through(store, reads_loc)
    _records_through(store, reads_nothing, _COMPANION)

    digests.set_loc(b"patch 2")
    _records_through(store, reads_loc)
    _records_through(store, reads_nothing, _COMPANION)

    assert reads_loc.builds == 2
    assert reads_nothing.builds == 1


def test_another_client_rebuilds_only_tables_that_read_it(store: RecordStore, digests: DataDigests) -> None:
    digests.set_client(1784)
    reads_client = _Handler(effective_client)
    reads_nothing = _Handler()
    _records_through(store, reads_client)
    _records_through(store, reads_nothing, _COMPANION)

    digests.set_client(3483)
    _records_through(store, reads_client)
    _records_through(store, reads_nothing, _COMPANION)

    assert reads_client.builds == 2
    assert reads_nothing.builds == 1


def test_a_patch_keeps_tables_that_only_ordered_layouts_by_the_client(
    store: RecordStore, digests: DataDigests
) -> None:
    layouts = ((ClientRange(3251),), (ClientRange(1717, 2000),))
    orders_layouts = _Handler(lambda: client_order(layouts, lambda clients: clients))
    digests.set_client(3483)
    _records_through(store, orders_layouts)

    digests.set_client(3484)  # a patch: still the newest layout's range
    _records_through(store, orders_layouts)
    assert orders_layouts.builds == 1

    digests.set_client(1784)  # another layout's range
    _records_through(store, orders_layouts)
    assert orders_layouts.builds == 2


def test_a_build_that_overlapped_a_data_change_is_not_saved(store: RecordStore, digests: DataDigests) -> None:
    handler = _Handler(lambda: digests.set_loc(b"switched language"))
    _records_through(store, handler)

    handler._reads = lambda: None
    _records_through(store, handler)

    assert handler.builds == 2


def test_tables_outside_a_paz_archive_are_never_cached(store: RecordStore) -> None:
    handler = _Handler()
    _records_through(store, handler, _DISK)
    _records_through(store, handler, _DISK)

    assert handler.builds == 2


def test_the_cache_survives_reopening(tmp_path: Path, archives: _Archives, digests: DataDigests) -> None:
    handler = _Handler()
    first = _open_store(tmp_path, archives, digests)
    _records_through(first, handler)
    first.close()

    second = _open_store(tmp_path, archives, digests)
    assert second.is_current(handler, _TABLE)
    assert _records_through(second, handler) == _RECORDS
    second.close()
    assert handler.builds == 1


# ── PreviewHandler hook ──────────────────────────────────────────────────────


def test_all_records_goes_through_the_installed_source(store: RecordStore) -> None:
    handler = _Handler()
    _records_through(store, handler)
    set_records_source(store)
    try:
        records = handler.all_records(b"payload", _TABLE, {})
    finally:
        set_records_source(None)

    assert records == _RECORDS
    assert handler.builds == 1


def _sorted_through(store: RecordStore, handler: _Handler, payload: bytes) -> list[int]:
    """Open the table and sort it as the app does, with the store installed."""
    set_records_source(store)
    try:
        handler.all_records(payload, _TABLE, {})
        order = list(handler.sorted_order(payload, _TABLE, {}, _BY_ID_DESC))
    finally:
        set_records_source(None)
    store._writer.submit(lambda: None).result()
    return order


def test_a_sort_order_is_cached_with_the_records(store: RecordStore) -> None:
    handler = _Handler()
    first = _sorted_through(store, handler, b"first open")

    # A new payload object, as after a restart: nothing left in memory.
    second = _sorted_through(store, handler, b"second open")

    assert second == first == [1, 0]
    assert (handler.builds, handler.sorts) == (1, 1)


def test_an_index_sort_is_never_cached(store: RecordStore) -> None:
    handler = _IndexSortHandler()
    _sorted_through(store, handler, b"first open")
    _sorted_through(store, handler, b"second open")

    assert handler.sorts == 2


def test_an_order_needs_records_from_the_same_store(store: RecordStore) -> None:
    handler = _Handler()
    order = store.sort_order(handler, _TABLE, _BY_ID_DESC, lambda: array("I", [1, 0]))

    assert list(order) == [1, 0]
    assert not store.is_current(handler, _TABLE, _BY_ID_DESC)


def test_release_data_keeps_slots_of_other_payloads() -> None:
    handler = _Handler()
    kept, released = b"kept payload", b"released payload"
    handler._data_cache(kept, "a", lambda: "kept")
    handler._data_cache(released, "b", lambda: "released")

    handler.release_data(released)

    assert handler._data_cache(kept, "a", lambda: "rebuilt") == "kept"
    assert handler._data_cache(released, "b", lambda: "rebuilt") == "rebuilt"


# ── RecordsPrefill ───────────────────────────────────────────────────────────


def test_prefill_builds_only_tables_without_a_current_row(store: RecordStore) -> None:
    cached, missing = _Handler(), _Handler()
    _records_through(store, cached)
    prefill = RecordsPrefill(
        store,
        targets=lambda: [(cached, _TABLE), (missing, _COMPANION)],
        load=lambda handler, entry: (b"payload", {}),
        opening_sort=lambda handler, entry: _BY_ID_DESC,
        is_idle=lambda: True,
        report=lambda progress: None,
        finished=lambda: None,
    )

    prefill._run(prefill._stop)

    assert (cached.builds, missing.builds) == (1, 1)
    assert store.is_current(missing, _COMPANION, _BY_ID_DESC)
    # The cached table only lacked its opening order, so it is counted too.
    assert store.is_current(cached, _TABLE, _BY_ID_DESC)


def test_prefill_skips_the_order_of_an_index_sort(store: RecordStore) -> None:
    handler = _IndexSortHandler()
    prefill = RecordsPrefill(
        store,
        targets=lambda: [(handler, _TABLE)],
        load=lambda handler, entry: (b"payload", {}),
        opening_sort=lambda handler, entry: _BY_ID_ASC,
        is_idle=lambda: True,
        report=lambda progress: None,
        finished=lambda: None,
    )

    prefill._run(prefill._stop)

    assert handler.sorts == 0
    assert store.is_current(handler, _TABLE, _BY_ID_ASC)


def test_prefill_stops_while_waiting_for_idle(store: RecordStore) -> None:
    handler = _Handler()
    prefill = RecordsPrefill(
        store,
        targets=lambda: [(handler, _TABLE)],
        load=lambda handler, entry: (b"payload", {}),
        opening_sort=lambda handler, entry: None,
        is_idle=lambda: False,
        report=lambda progress: None,
        finished=lambda: None,
    )
    prefill.stop()

    prefill._run(prefill._stop)

    assert handler.builds == 0


def test_prefill_reports_the_end_of_a_pass_with_nothing_to_build(store: RecordStore) -> None:
    handler = _Handler()
    finished: list[bool] = []
    prefill = RecordsPrefill(
        store,
        targets=lambda: [],
        load=lambda handler, entry: (b"payload", {}),
        opening_sort=lambda handler, entry: None,
        is_idle=lambda: True,
        report=lambda progress: None,
        finished=lambda: finished.append(True),
    )

    prefill._run(prefill._stop)

    assert finished == [True]
    assert handler.builds == 0


def test_prefill_shows_the_table_it_works_on_and_when_it_waits(store: RecordStore) -> None:
    seen: list[PrefillProgress | None] = []
    busy = iter([False, True])
    prefill = RecordsPrefill(
        store,
        targets=lambda: [(_Handler(), _TABLE)],
        load=lambda handler, entry: (b"payload", {}),
        opening_sort=lambda handler, entry: None,
        is_idle=lambda: next(busy, True),
        report=lambda progress: None,
        finished=lambda: None,
    )
    original_build = prefill._build

    def build(handler: PreviewHandler, entry: PazEntry, sort: TableSort | None) -> None:
        seen.append(prefill._progress)
        original_build(handler, entry, sort)

    prefill._build = build  # type: ignore[method-assign]
    prefill._wait_until_idle(prefill._stop, 0, 1)
    paused = prefill._progress
    prefill._fill([(_Handler(), _TABLE)], prefill._stop)

    assert paused == PrefillProgress(0, 1, "", paused=True)
    assert seen == [PrefillProgress(0, 1, _TABLE.internal_path)]


def test_the_folder_status_returns_after_a_pass() -> None:
    from api.bdo_api import Api

    api = Api()
    loaded = {"key": "status.loadedFromCache", "args": {"count": "3", "version": 1}}
    pushed: list[dict] = []
    api._folder_status = loaded
    api._push_status = lambda msg, progress=None: pushed.append(msg)  # type: ignore[method-assign]

    api._show_folder_status()

    assert pushed == [loaded]


def test_deleting_the_caches_does_not_restart_the_background_pass(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import api.bdo_api_caches as caches
    from api.bdo_api import Api

    class _RunningPass:
        def stop(self) -> None:
            pass

    monkeypatch.setattr(caches, "records_cache_setting", lambda cfg: "all")
    api = Api()
    api._paz_root = tmp_path
    api._cache_dir = tmp_path
    api._folder_status = {"key": "status.loadedFromCache", "args": {}}
    api._records_prefill = _RunningPass()  # type: ignore[assignment]
    pushed: list[dict] = []
    api._push_status = lambda msg, progress=None: pushed.append(msg)  # type: ignore[method-assign]

    try:
        result = api.delete_caches()

        assert result["ok"]
        assert api._records_prefill is None
        # Tables opened from now on are still cached.
        assert api._records_store is not None
        assert pushed == [api._folder_status]
    finally:
        api._close_records_cache()
