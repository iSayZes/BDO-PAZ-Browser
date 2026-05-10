from __future__ import annotations

import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .bdo_api_helpers import _DISK_VIRTUAL_PREFIX, _file_icon, _norm
from paz.bdo_payload_reader import read_entry_payload


def _build_needles(query: str, mode: str) -> list[bytes] | None:
    """Parse a search query into a list of byte sequences to search for.

    Returns None when the query is invalid for the given mode.
    For "string" mode, returns both UTF-8 and UTF-16-LE variants.
    For "hex" mode, returns a single bytes object.
    """
    if not query:
        return None
    if mode == "hex":
        hex_clean = query.replace(" ", "")
        if not hex_clean or len(hex_clean) % 2 != 0:
            return None
        try:
            return [bytes.fromhex(hex_clean)]
        except ValueError:
            return None
    # string mode
    needles = [query.encode("utf-8")]
    try:
        utf16 = query.encode("utf-16-le")
        if utf16 != needles[0]:
            needles.append(utf16)
    except Exception:
        pass
    return needles


_SEARCH_WORKERS = 8
_RESULT_BATCH = 20


class SearchMixin:
    """Content search methods — single-file and cross-file — for Api."""

    def search_content(self, path: str, query: str, mode: str, tab: str) -> dict:
        """Search file content.

        mode: "hex" | "string"
        tab:  "hex" | "parsed"
        Returns {"offsets": [...]} (byte offsets) for hex tab,
                {"record_indices": [...]} for parsed tab.
        """
        norm = _norm(path)

        if tab == "parsed":
            if self._cached_path != norm:
                return {"error": "No parsed data cached — reload the file"}
            if self._cached_data is None or self._cached_entry is None or self._cached_handler is None:
                return {"error": "No parsed data cached — reload the file"}
            indices = self._cached_handler.search_records(
                self._cached_data,
                self._cached_entry,
                self._cached_companions,
                query,
            )
            return {"record_indices": indices, "total": len(indices)}

        # hex tab — search raw bytes
        if self._cached_path == norm and self._cached_data is not None:
            data = self._cached_data
        elif path.startswith(_DISK_VIRTUAL_PREFIX + "/"):
            name = path[len(_DISK_VIRTUAL_PREFIX) + 1:]
            data = self._disk_companions.get(name)
            if data is None:
                return {"error": f"Disk file not loaded: {name}"}
        else:
            return {"error": "File data not cached — reload the file"}

        needles = _build_needles(query, mode)
        if needles is None:
            return {"offsets": [], "total": 0}

        seen: set[int] = set()
        offsets: list[int] = []
        for needle in needles:
            start = 0
            while (idx := data.find(needle, start)) != -1:
                if idx not in seen:
                    seen.add(idx)
                    offsets.append(idx)
                start = idx + 1
        offsets.sort()

        return {"offsets": offsets, "total": len(offsets)}

    def search_all_files(self, query: str, mode: str, extensions: list[str] | None = None) -> dict:
        """Start a background cross-file content search.

        mode:       "hex" | "string"
        extensions: list of lowercase dotted extensions to scan, e.g. [".bss", ".dbss"].
                    Defaults to [".bss", ".dbss"].
        Fires app.onGlobalSearchDone(results) when complete.
        """
        if not self._entries or not self._paz_root:
            return {"error": "No PAZ folder loaded"}

        needles = _build_needles(query, mode)
        if needles is None:
            return {"error": "Invalid search pattern"}

        exts = {e.lower() for e in (extensions or [".bss", ".dbss"])}
        candidates = [e for e in self._entries if Path(e.internal_path).suffix.lower() in exts]
        if not candidates:
            return {"error": "No files match the selected extensions"}

        self._global_search_cancel.set()
        cancel = threading.Event()
        self._global_search_cancel = cancel

        threading.Thread(
            target=self._run_global_search,
            args=(needles, candidates, self._paz_root, cancel),
            daemon=True,
        ).start()
        return {"total": len(candidates)}

    def cancel_global_search(self) -> None:
        self._global_search_cancel.set()

    def _search_entry(
        self,
        entry,
        needles: list[bytes],
        paz_root: Path,
        cancel: threading.Event,
    ) -> dict | None:
        if cancel.is_set():
            return None
        try:
            data = read_entry_payload(
                archive_path=paz_root / entry.archive_name,
                entry=entry,
            )
        except Exception:
            return None
        offsets: list[int] = []
        seen: set[int] = set()
        for needle in needles:
            pos = 0
            while (idx := data.find(needle, pos)) != -1:
                if idx not in seen:
                    seen.add(idx)
                    offsets.append(idx)
                pos = idx + 1
        if not offsets:
            return None
        offsets.sort()
        return {
            "path":  _norm(entry.internal_path),
            "name":  Path(entry.internal_path).name,
            "count": len(offsets),
            "first": offsets[0],
            "icon":  _file_icon(Path(entry.internal_path).suffix),
        }

    def _run_global_search(
        self,
        needles: list[bytes],
        candidates: list,
        paz_root: Path,
        cancel: threading.Event,
    ) -> None:
        total = len(candidates)
        pending: list[dict] = []
        completed = 0
        total_matched = 0

        pool = ThreadPoolExecutor(max_workers=_SEARCH_WORKERS, thread_name_prefix="gsearch")
        try:
            futures = {
                pool.submit(self._search_entry, e, needles, paz_root, cancel): e
                for e in candidates
            }
            for future in as_completed(futures):
                completed += 1
                if cancel.is_set():
                    break
                result = future.result()
                if result:
                    pending.append(result)
                    total_matched += 1
                flush = len(pending) >= _RESULT_BATCH or completed == total
                if completed % 50 == 0 or flush:
                    self._push_status({"key": "status.searching", "args": {
                        "done": completed, "total": total, "matches": total_matched,
                    }})
                if pending and flush:
                    self._push_js(f"app.onGlobalSearchResult({json.dumps(pending)})")
                    pending = []
        finally:
            pool.shutdown(wait=False, cancel_futures=True)

        if cancel.is_set():
            return

        self._push_status({"key": "status.searchDone", "args": {"matches": total_matched, "total": total}})
        self._push_js(f"app.onGlobalSearchDone({json.dumps({'total': total_matched})})")
