"""The parsed records disk cache as the app uses it: keys, dependencies, writes.

`paz/bdo_records_cache.py` stores one row per table. This module decides what
a row is keyed on and is installed as the `RecordsSource` of `bdo_preview`, so
every `all_records()` parse goes through it.

A row's input key covers the table's own inputs:

- the handler's code (`source_fingerprint`), taken once per handler while its
  source still matches the loaded code
- the handler's language
- the PAZ identity of the table and of every companion it declares: archive
  name, the archive's CRC and size from the meta file, offset and sizes

Shared data is not in the key. LOC, the lookup indexes and the client version
change with nearly every patch, so a row instead records the digest of only
what its build read (`_common/data_deps.py`), and a patch that leaves a table
and that data alone keeps its row.
"""

from __future__ import annotations

import hashlib
import json
import logging
import threading
from array import array
from collections.abc import Callable, Iterable, Mapping
from concurrent.futures import ThreadPoolExecutor
from weakref import WeakKeyDictionary

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
# The handlers folder the entry point put on the path (bdo_preview.use_handlers_dir).
from _common.data_deps import (
    CLIENT,
    CLIENT_RANGES_PREFIX,
    INDEX_PREFIX,
    LOC,
    client_ranges_digest,
    index_dep,
    note_read,
    recording,
)
from paz.bdo_records_cache import RecordsCache, RecordsStamp
from paz.source_fingerprint import project_module_of, source_fingerprints
from table_sort import TableSort

# Part of every input key; bump when what goes into a key changes.
_KEY_FORMAT = "records-key-1"
# Digest of shared data that is not loaded, and identity of a missing companion.
ABSENT = "absent"

# A PAZ entry's identity (`paz_entry_identity`), or None when it has none.
EntryIdentity = Callable[[PazEntry], "str | None"]
ResolveEntry = Callable[[str], "PazEntry | None"]
Records = list[dict]


def sort_name(sort: TableSort) -> str:
    """How a sort is named in the cache, such as `id:desc`."""
    return f"{sort.field}:{sort.direction}"


def paz_entry_identity(entry: PazEntry, archive_crc: int, archive_size: int) -> str:
    """What identifies an entry's bytes without reading them.

    A patch writes changed files into new archives and leaves old archives
    alone, so an unchanged archive CRC and size mean unchanged bytes at the
    same offset.
    """
    return (
        f"{entry.archive_name.lower()}:{archive_crc:08x}:{archive_size}:{entry.offset}:"
        f"{entry.compressed_size}:{entry.uncompressed_size}:"
        f"{entry.compression_type}:{entry.encryption_type}"
    )


class DataDigests:
    """Today's digest of each piece of shared data a records build can read.

    `generation` goes up on every change, so a build that overlapped one is
    not saved with digests it did not see.
    """

    def __init__(self) -> None:
        self._digests: dict[str, str] = {}
        self._client: int | None = None
        self._generation = 0
        self._lock = threading.Lock()

    @property
    def generation(self) -> int:
        return self._generation

    def get(self, name: str) -> str:
        if name.startswith(CLIENT_RANGES_PREFIX):
            # Named by the layout ranges it covers, so derived from the client.
            return client_ranges_digest(name, self._client)
        return self._digests.get(name, ABSENT)

    def set_loc(self, raw: bytes | None) -> None:
        """The LOC file now installed, or None when there is none."""
        values = {} if raw is None else {LOC: hashlib.sha256(raw).hexdigest()}
        self._replace(lambda name: name == LOC, values)

    def set_indexes(self, digests: Mapping[str, str]) -> None:
        """The lookup indexes now installed, as digests by kind value."""
        values = {index_dep(kind_value): digest for kind_value, digest in digests.items()}
        self._replace(lambda name: name.startswith(INDEX_PREFIX), values)

    def set_client(self, client: int | None) -> None:
        """The client version handlers now read files as, or None when there is none."""
        with self._lock:
            self._client = client
        values = {} if client is None else {CLIENT: str(client)}
        self._replace(lambda name: name == CLIENT, values)

    def _replace(self, owns: Callable[[str], bool], values: Mapping[str, str]) -> None:
        with self._lock:
            kept = {name: digest for name, digest in self._digests.items() if not owns(name)}
            updated = {**kept, **values}
            if updated != self._digests:
                self._digests = updated
                self._generation += 1


class RecordStore:
    """Serves `all_records()` from the disk cache and fills it on a miss."""

    def __init__(
        self,
        cache: RecordsCache,
        digests: DataDigests,
        identity: EntryIdentity,
        resolve: ResolveEntry,
    ) -> None:
        self._cache = cache
        self._digests = digests
        self._identity = identity
        self._resolve = resolve
        self._fingerprints: WeakKeyDictionary[PreviewHandler, str] = WeakKeyDictionary()
        # Stamp of the records `records()` last returned per table path: the
        # ones in the handler's memory, which a cached sort order must match.
        self._served: dict[str, RecordsStamp] = {}
        # One writer, so a pickle never runs on the thread that opened the table.
        self._writer = ThreadPoolExecutor(max_workers=1, thread_name_prefix="records-cache")

    @property
    def error(self) -> str:
        return self._cache.error

    def prepare(self, handlers: Iterable[PreviewHandler]) -> None:
        """Fingerprint `handlers` now, while their source matches the loaded code.

        A fingerprint taken later could hash a file edited since it was
        imported, and file records the old code built under the new code.
        """
        missing = {handler: _code_roots(handler) for handler in handlers if handler not in self._fingerprints}
        for handler, fingerprint in source_fingerprints(missing).items():
            self._fingerprints[handler] = fingerprint

    def records(self, handler: PreviewHandler, entry: PazEntry, build: Callable[[], Records]) -> Records:
        """`RecordsSource`: the cached records, else `build()` saved in the background."""
        path = entry.internal_path
        try:
            key = self._input_key(handler, entry)
            cached = None if key is None else self._cache.get(path, key, self._digests.get)
        except Exception:
            logging.warning("Records cache lookup failed for %s", path, exc_info=True)
            return build()
        if cached is not None:
            self._served[path] = cached.stamp
            # A build that reads these records read what they were built from.
            for name in json.loads(cached.stamp.deps):
                note_read(name)
            return cached.records

        self._served.pop(path, None)
        records, deps = self._build(build)
        if key is not None and deps is not None:
            stamp = RecordsStamp.of(key, deps)
            self._served[path] = stamp
            self._submit(self._cache.put, path, stamp, records)
        return records

    def sort_order(self, handler: PreviewHandler, entry: PazEntry, sort: TableSort, build: Callable[[], array]) -> array:
        """`RecordsSource`: the cached order of the records `records()` last returned, else `build()`."""
        path = entry.internal_path
        stamp = self._served.get(path)
        if stamp is None:
            return build()
        try:
            cached = self._cache.get_order(path, sort_name(sort), stamp)
        except Exception:
            logging.warning("Sort order cache lookup failed for %s", path, exc_info=True)
            cached = None
        if cached is not None:
            return cached
        order = build()
        self._submit(self._cache.put_order, path, sort_name(sort), stamp, order)
        return order

    def is_current(self, handler: PreviewHandler, entry: PazEntry, sort: TableSort | None = None) -> bool:
        """True when the records of `entry`, and the order of `sort` if it is cacheable, are cached."""
        key = self._input_key(handler, entry)
        if key is None:
            return False
        name = sort_name(sort) if sort is not None and handler.sorts_records_only() else None
        return self._cache.is_current(entry.internal_path, key, self._digests.get, name)

    def fill(self, handler: PreviewHandler, entry: PazEntry, build: Callable[[], Records], sort: TableSort | None) -> None:
        """Cache the records of `entry`, and the order of `sort`, on this thread.

        For the background fill. It leaves the stamps of the records the UI
        holds alone, so a fill can never pair an open table with another order.
        """
        path = entry.internal_path
        key = self._input_key(handler, entry)
        if key is None:
            return
        cached = self._cache.get(path, key, self._digests.get)
        if cached is None:
            records, deps = self._build(build)
            if deps is None:
                return
            stamp = RecordsStamp.of(key, deps)
            self._cache.put(path, stamp, records)
        else:
            records, stamp = cached.records, cached.stamp
        if sort is None or not handler.sorts_records_only():
            return
        if self._cache.get_order(path, sort_name(sort), stamp) is None:
            order = array("I", handler.records_sort_order(records, sort))
            self._cache.put_order(path, sort_name(sort), stamp, order)

    def close(self) -> None:
        """Finish pending writes and close the store."""
        self._writer.shutdown(wait=True)
        self._cache.close()

    def _build(self, build: Callable[[], Records]) -> tuple[Records, dict[str, str] | None]:
        """The records, and the digests of what they read; None when that changed meanwhile."""
        generation = self._digests.generation
        with recording() as names:
            records = build()
        if self._digests.generation != generation:
            return records, None
        return records, {name: self._digests.get(name) for name in names}

    def _submit(self, write: Callable[..., None], path: str, *args: object) -> None:
        """Run a cache write on the writer thread; a failure is logged, never raised."""

        def run() -> None:
            try:
                write(path, *args)
            except Exception:
                logging.warning("Could not write the records cache for %s", path, exc_info=True)

        try:
            self._writer.submit(run)
        except RuntimeError:
            # Closed while this table parsed: the folder changed or the caches
            # were deleted, so there is nothing to save into.
            pass

    def _input_key(self, handler: PreviewHandler, entry: PazEntry) -> str | None:
        """Hash of the table's own inputs, or None when it is not read from a PAZ archive."""
        table = self._identity(entry)
        if table is None:
            return None
        parts = [_KEY_FORMAT, self._fingerprint(handler), handler.lang, table]
        for path in sorted(handler.companions(entry)):
            companion = self._resolve(path)
            identity = None if companion is None else self._identity(companion)
            parts.append(f"{path}={identity or ABSENT}")
        return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()

    def _fingerprint(self, handler: PreviewHandler) -> str:
        fingerprint = self._fingerprints.get(handler)
        if fingerprint is None:
            self.prepare([handler])
            fingerprint = self._fingerprints[handler]
        return fingerprint


def _code_roots(handler: PreviewHandler) -> list[object]:
    """The handler's class plus the project code it was configured with.

    Shared classes such as `OffsetTableHandler` take their parser and labels
    as constructor arguments, which live in the table's own package.
    """
    configured = (project_module_of(value) for value in getattr(handler, "__dict__", {}).values())
    return [type(handler), *(module for module in configured if module is not None)]
