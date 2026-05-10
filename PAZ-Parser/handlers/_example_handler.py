# Example custom handler — rename to something like myformat_handler.py and implement.
#
# Drop any *.py file (not starting with _) here and it is loaded at browser startup.
# Each file can call register_handler() for one or more filenames or extensions.
#
# Keys:
#   "somefile.dbss"  — exact filename match (checked first)
#   ".dbss"          — extension fallback (used if no filename match exists)
#
# Companion files:
#   Override companions() to declare additional files the handler needs.
#   The browser will load them from the PAZ archive (by internal path) and pass
#   them to get_records() in the `companions` dict, keyed by filename (basename).
#   Disk files pre-loaded by the browser (e.g. languagedata_en.loc) are also merged
#   in automatically.
#
# from __future__ import annotations
# from pathlib import Path
# from bdo_models import PazEntry
# from bdo_preview import PreviewHandler, register_handler
# from _common.html import e, table
#
#
# _HEADERS = [
#     ("ID",   "num", ""),
#     ("Name", "",    ""),
# ]
#
#
# ── Simple handler ─────────────────────────────────────────────────────────────
#
# Implement get_records() and render_records_page().  The base class handles
# lazy caching, paging, search, and CSV export automatically.
#
# class MyHandler(PreviewHandler):
#
#     def companions(self, entry: PazEntry) -> list[str]:
#         # Return internal PAZ paths of files needed alongside the main file.
#         # folder = entry.internal_path.rsplit("/", 1)[0]
#         # return [f"{folder}/myindex.dbss"]
#         return []
#
#     def get_records(
#         self,
#         data: bytes,
#         entry: PazEntry,
#         companions: dict[str, bytes],
#     ) -> list[dict]:
#         # Parse all records once. Return plain dicts — no HTML.
#         # companions["myindex.dbss"]        — PAZ-internal companion (if loaded)
#         # companions["languagedata_en.loc"]  — pre-loaded disk file (if found)
#         return [{"id": i, "value": b} for i, b in enumerate(data)]
#
#     def render_records_page(
#         self,
#         records: list[dict],
#         page: int,
#         page_size: int,
#     ) -> str:
#         start  = page * page_size
#         slice_ = records[start : start + page_size]
#         rows   = [[e(r["id"]), e(r["value"])] for r in slice_]
#         return table(f"{len(records):,} records", _HEADERS, rows)
#
#
# register_handler("myfile.myext", MyHandler())   # by filename
# register_handler(".myext",       MyHandler())   # by extension (fallback)
#
#
# ── Index-based handler (heavy parse, page on demand) ─────────────────────────
#
# When parsing builds a large internal structure (an offset table, a packed index,
# etc.), use _data_cache() to build it once per data object and reuse it across
# paging, count, and search calls.  The cache invalidates automatically when a
# different file is selected.
#
# class MyIndexedHandler(PreviewHandler):
#
#     def _get_index(self, data: bytes):
#         # Build once; rebuild only when data object identity changes.
#         return self._data_cache(data, "index", lambda: _build_index(data))
#
#     def get_record_count(self, data, entry, companions) -> int:
#         return self._get_index(data).count
#
#     def render_data_page(self, data, entry, companions, page, page_size) -> str:
#         # Parse only the requested page from the index — skip materialising all records.
#         records = self._get_index(data).records_for_page(page, page_size)
#         return _render_table(records, page, page_size)
#
#     def search_records(self, data, entry, companions, query) -> list[int]:
#         return self._get_index(data).search(query)
#
#     def get_records(self, data, entry, companions) -> list[dict]:
#         # Compatibility fallback — used by CSV export and test assertions.
#         return self._get_index(data).all_records()
#
#     def render_records_page(self, records, page, page_size) -> str:
#         start  = page * page_size
#         slice_ = records[start : start + page_size]
#         return _render_table(slice_, page, page_size)
#
#
# register_handler("myfile.dbss", MyIndexedHandler())
