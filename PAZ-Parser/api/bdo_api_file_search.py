"""File name search in the tree (FileSearchMixin).

A query sorts every match by folder, then file name, and keeps the list, so
the page loads it SEARCH_PAGE_SIZE rows at a time as the results scroll. On
client 3464, `*` matches 871,657 files: about 165 MB of rows in one answer.
"""

from __future__ import annotations

from .bdo_api_helpers import FileSearchHits, _norm, folder_then_name, path_matcher, search_result
from .bdo_api_state import ApiState

SEARCH_PAGE_SIZE = 1000


class FileSearchMixin(ApiState):
    def search(self, query: str, offset: int = 0) -> dict:
        """The match count and rows `offset` to `offset + SEARCH_PAGE_SIZE` of
        the entries matching `query`, as {"total", "items"}.

        Glob patterns (containing *, ?, or [) are matched against the full
        path and against the filename alone.  Plain strings do substring match.
        """
        if not isinstance(query, str):
            raise TypeError(f"query must be a string, got {type(query).__name__}")
        if type(offset) is not int or offset < 0:
            raise ValueError(f"offset must be an int of 0 or more, got {offset!r}")
        self._mark_activity()
        paths = self._file_search_hits(query).paths
        page = paths[offset:offset + SEARCH_PAGE_SIZE]
        return {"total": len(paths), "items": [search_result(path) for path in page]}

    def _file_search_hits(self, query: str) -> FileSearchHits:
        """Every match of `query`, searched again only for a new query or entry list."""
        entries = self._visible_entries()
        last = self._file_search
        if last is not None and last.query == query and last.entries is entries:
            return last
        is_hit = path_matcher(query)
        all_paths = (_norm(entry.internal_path) for entry in entries)
        hits = FileSearchHits(query, entries, tuple(sorted((p for p in all_paths if is_hit(p)), key=folder_then_name)))
        self._file_search = hits
        return hits
