from __future__ import annotations

import fnmatch
import json
import threading
import time
from pathlib import Path
from typing import Any

import webview

_CONFIG_FILE = Path(__file__).parent / "paz_config.json"


def _load_config() -> dict:
    try:
        return json.loads(_CONFIG_FILE.read_text()) if _CONFIG_FILE.exists() else {}
    except Exception:
        return {}


def _save_last_folder(path: Path) -> None:
    cfg = _load_config()
    cfg["last_folder"] = str(path)
    try:
        _CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
    except Exception:
        pass

from bdo_cache import load_cache, read_meta_version, save_cache
from bdo_models import PazEntry
from bdo_paz_extract import extract_entry, find_single_meta_file, parse_meta_file
from bdo_payload_reader import read_entry_payload
from bdo_preview import (
    DdsHandler, HexHandler, PARSED_RECORDS_PER_PAGE, TextHandler, get_handler,
)

_hex_handler = HexHandler()


_ICON_MAP: dict[str, str] = {
    ".dds": "🖼", ".png": "🖼", ".jpg": "🖼", ".jpeg": "🖼", ".bmp": "🖼", ".tga": "🖼",
    ".xml": "📋", ".json": "📋", ".yaml": "📋", ".yml": "📋",
    ".txt": "📄", ".log": "📄", ".csv": "📄", ".ini": "📄", ".cfg": "📄",
    ".htm": "🌐", ".html": "🌐",
    ".lua": "📜",
    ".pac": "📦", ".bss": "🔒", ".dbss": "🔒",
    ".loc": "💬",
}

_DISK_VIRTUAL_PREFIX = "__disk__"

_LOC_CANDIDATES: dict[str, tuple[str, ...]] = {
    "languagedata_en.loc": ("ads", "languagedata_en.loc"),
}


def _norm(path: str) -> str:
    return path.replace("\\", "/")


def _file_icon(ext: str) -> str:
    return _ICON_MAP.get(ext.lower(), "·")


def _count_entries(node: dict) -> int:
    total = 0
    for v in node.values():
        if isinstance(v, PazEntry):
            total += 1
        elif isinstance(v, dict):
            total += _count_entries(v)
    return total


class Api:
    def __init__(self) -> None:
        self._window: webview.Window | None = None
        self._paz_root: Path | None = None
        self._entries: list[PazEntry] = []
        self._entry_map: dict[str, PazEntry] = {}
        self._tree_data: dict = {}
        self._disk_companions: dict[str, bytes] = {}
        self._status = "Open a PAZ folder to begin."
        self._cached_path: str | None = None
        self._cached_data: bytes | None = None
        self._cached_records: list[dict] | None = None
        self._cached_handler = None

    def set_window(self, window: webview.Window) -> None:
        self._window = window

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _push_js(self, js: str) -> None:
        if self._window is not None:
            try:
                self._window.evaluate_js(js)
            except Exception:
                pass

    def _push_status(self, msg: str, progress: tuple[int, int] | None = None) -> None:
        self._status = msg
        payload = json.dumps({"message": msg, "progress": list(progress) if progress else None})
        self._push_js(f"app.setStatus({payload})")

    # ── Folder ────────────────────────────────────────────────────────────────

    def open_folder(self) -> dict:
        if self._window is None:
            return {"ok": False, "error": "Window not initialized"}
        result = self._window.create_file_dialog(webview.FileDialog.FOLDER)
        if not result:
            return {"ok": False}
        self._paz_root = Path(result[0])
        _save_last_folder(self._paz_root)
        threading.Thread(target=self._load_entries, daemon=True).start()
        return {"ok": True, "path": str(self._paz_root)}

    def get_last_folder(self) -> dict:
        path = _load_config().get("last_folder")
        if path and Path(path).is_dir():
            return {"path": path}
        return {}

    def open_folder_path(self, path: str) -> dict:
        p = Path(path)
        if not p.is_dir():
            return {"ok": False, "error": "Folder not found"}
        self._paz_root = p
        threading.Thread(target=self._load_entries, daemon=True).start()
        return {"ok": True, "path": str(self._paz_root)}

    def _load_entries(self) -> None:
        assert self._paz_root is not None
        try:
            meta_path = find_single_meta_file(self._paz_root)
            current_version = read_meta_version(meta_path)
            cached = load_cache(self._paz_root)

            if cached and cached[0] == current_version:
                _, entries = cached
                msg = f"Loaded {len(entries):,} entries from cache  (game version {current_version})"
            else:
                stop_ticker = threading.Event()
                start = time.monotonic()

                def _ticker(stop: threading.Event, t0: float) -> None:
                    while not stop.is_set():
                        elapsed = int(time.monotonic() - t0)
                        self._push_status(
                            f"Parsing PAZ files… {elapsed}s elapsed  (first run only — result will be cached)"
                        )
                        stop.wait(0.5)

                threading.Thread(target=_ticker, args=(stop_ticker, start), daemon=True).start()
                try:
                    entries = parse_meta_file(meta_path)
                finally:
                    stop_ticker.set()

                save_cache(self._paz_root, current_version, entries)
                msg = f"Parsed and cached {len(entries):,} entries  (game version {current_version})"

            self._entries = entries
            self._entry_map = {_norm(e.internal_path): e for e in entries}
            self._tree_data = self._build_tree_data(entries)
            self._load_disk_companions()
            self._push_status(msg)
            self._push_js("app.onFolderLoaded()")

        except Exception as ex:
            self._push_status(f"Error: {ex}")
            self._push_js(f"app.showError({json.dumps(str(ex))})")

    def _load_disk_companions(self) -> None:
        if not self._paz_root:
            return
        for name, rel_parts in _LOC_CANDIDATES.items():
            path = self._paz_root.parent.joinpath(*rel_parts)
            if path.exists():
                try:
                    raw = path.read_bytes()
                    self._disk_companions[name] = raw
                    if name == "languagedata_en.loc":
                        from _common.loc import init_loc  # noqa: PLC0415
                        init_loc(raw)
                except Exception:
                    pass

    def _load_companion_sync(self, internal_path: str) -> bytes | None:
        entry = self._entry_map.get(_norm(internal_path))
        if not entry or not self._paz_root:
            return None
        try:
            return read_entry_payload(
                archive_path=self._paz_root / entry.archive_name,
                entry=entry,
            )
        except Exception:
            return None

    # ── Tree ──────────────────────────────────────────────────────────────────

    def _build_tree_data(self, entries: list[PazEntry]) -> dict:
        root: dict = {}
        for entry in entries:
            parts = _norm(entry.internal_path).split("/")
            node = root
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = entry
        return root

    def get_children(self, node_path: str) -> list[dict]:
        """Return immediate children of a tree node for lazy loading."""
        node: Any = self._tree_data
        if node_path:
            for part in node_path.split("/"):
                if isinstance(node, dict):
                    node = node.get(part, {})
                else:
                    return []

        if not isinstance(node, dict):
            return []

        dirs  = sorted((k, v) for k, v in node.items() if isinstance(v, dict))
        files = sorted((k, v) for k, v in node.items() if isinstance(v, PazEntry))

        result: list[dict] = []

        if not node_path:
            for name in sorted(self._disk_companions):
                result.append({
                    "id":   f"{_DISK_VIRTUAL_PREFIX}/{name}",
                    "name": name,
                    "type": "file",
                    "icon": _file_icon(Path(name).suffix),
                    "disk": True,
                })

        for name, child_node in dirs:
            child_path = f"{node_path}/{name}" if node_path else name
            result.append({
                "id":          child_path,
                "name":        name,
                "type":        "dir",
                "count":       _count_entries(child_node),
                "icon":        "📁",
                "has_children": bool(child_node),
            })
        for name, entry in files:
            result.append({
                "id":   _norm(entry.internal_path),
                "name": name,
                "type": "file",
                "icon": _file_icon(Path(name).suffix),
            })
        return result

    def search(self, query: str) -> list[dict]:
        """Return up to 500 entries matching `query`.

        Glob patterns (containing *, ?, or [) are matched against the full
        path and against the filename alone.  Plain strings do substring match.
        """
        q = query.replace("\\", "/").lower()
        is_glob = any(c in q for c in ("*", "?", "["))
        results: list[dict] = []
        for entry in self._entries:
            path = _norm(entry.internal_path)
            name = path.rsplit("/", 1)[-1]
            path_lc = path.lower()
            name_lc = name.lower()
            if is_glob:
                hit = fnmatch.fnmatch(path_lc, q) or fnmatch.fnmatch(name_lc, q)
            else:
                hit = q in path_lc
            if hit:
                results.append({
                    "id":   path,
                    "name": name,
                    "path": path,
                    "icon": _file_icon(Path(name).suffix),
                })
                if len(results) == 500:
                    break
        return results

    # ── Entry loading ─────────────────────────────────────────────────────────

    def _build_entry_response(
        self,
        data: bytes,
        internal_path: str,
        entry: PazEntry,
        handler,
        companions: dict[str, bytes],
        meta: dict,
    ) -> dict:
        import html as _html_mod
        is_plain = isinstance(handler, (HexHandler, TextHandler, DdsHandler))
        has_parsed = not is_plain

        self._cached_path = _norm(internal_path)
        self._cached_data = data
        self._cached_records = None
        self._cached_handler = None

        hex_total_pages = HexHandler.page_count(data)
        hex_html = _hex_handler.render_page(data, 0)

        html = None
        parsed_total_pages = 1
        if has_parsed:
            try:
                records = handler.get_records(data, entry, companions)
            except Exception as ex:
                records = None
                html = f'<div class="error">Parse error: {_html_mod.escape(str(ex))}</div>'

            if records is not None:
                self._cached_records = records
                self._cached_handler = handler
                parsed_total_pages = max(1, (len(records) + PARSED_RECORDS_PER_PAGE - 1) // PARSED_RECORDS_PER_PAGE)
                try:
                    html = handler.render_records_page(records, 0, PARSED_RECORDS_PER_PAGE)
                except Exception as ex:
                    html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
        elif not isinstance(handler, HexHandler):
            try:
                html = handler.render(data, entry, companions)
            except Exception as ex:
                html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'

        return {
            "html": html,
            "hex_html": hex_html,
            "has_parsed": has_parsed,
            "meta": meta,
            "hex_total_pages": hex_total_pages,
            "parsed_total_pages": parsed_total_pages,
        }

    def _load_disk_entry(self, internal_path: str) -> dict:
        name = internal_path[len(_DISK_VIRTUAL_PREFIX) + 1:]
        data = self._disk_companions.get(name)
        if data is None:
            return {"error": f"Disk file not loaded: {name}"}

        fake_entry = PazEntry(
            archive_name="<disk>",
            internal_path=name,
            offset=0,
            compressed_size=len(data),
            uncompressed_size=len(data),
            compression_type=0,
            encryption_type=0,
        )
        meta = {
            "archive":      "<disk>",
            "path":         name,
            "compressed":   "—",
            "uncompressed": f"{len(data):,} B",
            "offset":       "—",
        }
        p = Path(name)
        handler = get_handler(p.name, p.suffix)
        return self._build_entry_response(data, internal_path, fake_entry, handler, {}, meta)

    def load_entry(self, internal_path: str) -> dict:
        if internal_path.startswith(_DISK_VIRTUAL_PREFIX + "/"):
            return self._load_disk_entry(internal_path)

        entry = self._entry_map.get(_norm(internal_path))
        if not entry or not self._paz_root:
            return {"error": "Entry not found"}

        meta = {
            "archive":      entry.archive_name,
            "path":         entry.internal_path,
            "compressed":   f"{entry.compressed_size:,} B",
            "uncompressed": f"{entry.uncompressed_size:,} B",
            "offset":       f"0x{entry.offset:08X}",
        }

        try:
            data = read_entry_payload(
                archive_path=self._paz_root / entry.archive_name,
                entry=entry,
            )
        except Exception as ex:
            return {"error": str(ex), "meta": meta}

        p = Path(entry.internal_path)
        handler = get_handler(p.name, p.suffix)

        companions: dict[str, bytes] = dict(self._disk_companions)
        for cp in handler.companions(entry):
            raw = self._load_companion_sync(cp)
            if raw is not None:
                companions[Path(cp).name] = raw

        return self._build_entry_response(data, internal_path, entry, handler, companions, meta)

    def get_hex_page(self, path: str, page: int) -> dict:
        norm = _norm(path)
        if self._cached_path == norm and self._cached_data is not None:
            data = self._cached_data
        elif path.startswith(_DISK_VIRTUAL_PREFIX + "/"):
            name = path[len(_DISK_VIRTUAL_PREFIX) + 1:]
            data = self._disk_companions.get(name)
            if data is None:
                return {"error": f"Disk file not loaded: {name}"}
        else:
            entry = self._entry_map.get(norm)
            if not entry or not self._paz_root:
                return {"error": "Entry not found"}
            try:
                data = read_entry_payload(
                    archive_path=self._paz_root / entry.archive_name,
                    entry=entry,
                )
            except Exception as ex:
                return {"error": str(ex)}
        return {"hex_html": _hex_handler.render_page(data, page)}

    def get_parsed_page(self, path: str, page: int) -> dict:
        import html as _html_mod
        norm = _norm(path)
        if self._cached_path != norm or self._cached_records is None or self._cached_handler is None:
            return {"error": "Page data not cached — reload the file first"}
        try:
            html = self._cached_handler.render_records_page(
                self._cached_records, page, PARSED_RECORDS_PER_PAGE
            )
        except Exception as ex:
            html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
        return {"html": html}

    # ── Extraction ────────────────────────────────────────────────────────────

    def pick_output_folder(self) -> str | None:
        if self._window is None:
            return None
        result = self._window.create_file_dialog(webview.FileDialog.FOLDER)
        return result[0] if result else None

    def extract_entries(self, paths: list[str], output_dir: str) -> dict:
        if not self._paz_root:
            return {"error": "No PAZ folder loaded"}

        entries: list[PazEntry] = []
        seen: set[str] = set()

        for path in paths:
            path = _norm(path)
            if path in self._entry_map:
                if path not in seen:
                    seen.add(path)
                    entries.append(self._entry_map[path])
            else:
                node: Any = self._tree_data
                for part in path.split("/"):
                    node = node.get(part, {}) if isinstance(node, dict) else {}
                collect: list[PazEntry] = []
                self._collect_recursive(node, collect)
                for e in collect:
                    ep = _norm(e.internal_path)
                    if ep not in seen:
                        seen.add(ep)
                        entries.append(e)

        if not entries:
            return {"error": "No entries to extract"}

        paz_root    = self._paz_root
        output_root = Path(output_dir)
        total       = len(entries)

        def run() -> None:
            extracted = skipped = failed = 0
            for i, entry in enumerate(entries, 1):
                try:
                    result = extract_entry(
                        paz_root=paz_root, output_root=output_root,
                        entry=entry, overwrite=False,
                    )
                    if result == "skipped":
                        skipped += 1
                    else:
                        extracted += 1
                except Exception:
                    failed += 1

                if i % 25 == 0 or i == total:
                    self._push_status(
                        f"Extracting… {i}/{total}  —  {extracted} ok  {skipped} skipped  {failed} failed",
                        (i, total),
                    )

            self._push_status(f"✓  Done — {extracted} extracted, {skipped} skipped, {failed} failed.")
            self._push_js("app.onExtractionDone()")

        threading.Thread(target=run, daemon=True).start()
        return {"total": total}

    def _collect_recursive(self, node: Any, out: list[PazEntry]) -> None:
        if isinstance(node, PazEntry):
            out.append(node)
        elif isinstance(node, dict):
            for v in node.values():
                self._collect_recursive(v, out)

    def get_selection_size(self, paths: list[str]) -> dict:
        seen: set[str] = set()
        total_bytes = 0

        for path in paths:
            path = _norm(path)
            if path in self._entry_map:
                if path not in seen:
                    seen.add(path)
                    total_bytes += self._entry_map[path].uncompressed_size
            else:
                node: Any = self._tree_data
                for part in path.split("/"):
                    node = node.get(part, {}) if isinstance(node, dict) else {}
                entries: list[PazEntry] = []
                self._collect_recursive(node, entries)
                for e in entries:
                    ep = _norm(e.internal_path)
                    if ep not in seen:
                        seen.add(ep)
                        total_bytes += e.uncompressed_size

        return {"count": len(seen), "bytes": total_bytes}

    # ── Plugins ───────────────────────────────────────────────────────────────

    def reload_plugins(self) -> None:
        import bdo_preview
        bdo_preview.reload_plugins(Path(__file__).parent / "handlers")
        self._push_js("app.onPluginsReloaded()")

    # ── Status ────────────────────────────────────────────────────────────────

    def search_content(self, path: str, query: str, mode: str, tab: str) -> dict:
        """Search file content.

        mode: "hex" | "string"
        tab:  "hex" | "parsed"
        Returns {"offsets": [...]} (byte offsets) for hex tab,
                {"record_indices": [...]} for parsed tab.
        """
        norm = _norm(path)

        if tab == "parsed":
            if self._cached_path != norm or self._cached_records is None:
                return {"error": "No parsed data cached — reload the file"}
            q = query.lower()
            indices = [
                i for i, rec in enumerate(self._cached_records)
                if any(q in str(v).lower() for v in rec.values())
            ]
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

        if mode == "hex":
            hex_clean = query.replace(" ", "")
            if not hex_clean or len(hex_clean) % 2 != 0:
                return {"offsets": [], "total": 0}
            try:
                needles = [bytes.fromhex(hex_clean)]
            except ValueError:
                return {"offsets": [], "total": 0}
        else:
            if not query:
                return {"offsets": [], "total": 0}
            needles = [query.encode("utf-8")]
            try:
                utf16 = query.encode("utf-16-le")
                if utf16 != needles[0]:
                    needles.append(utf16)
            except Exception:
                pass

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

    def export_file(self, path: str, tab: str) -> dict:
        if self._window is None:
            return {"error": "Window not initialized"}

        norm = _norm(path)
        filename = norm.rsplit("/", 1)[-1]

        if tab == "parsed" and self._cached_path == norm and self._cached_records is not None:
            import csv
            import io
            records = self._cached_records
            buf = io.StringIO()
            if records:
                writer = csv.DictWriter(buf, fieldnames=list(records[0].keys()))
                writer.writeheader()
                writer.writerows(records)
            data = buf.getvalue().encode("utf-8-sig")
            save_filename = Path(filename).stem + ".csv"
            file_types = ("CSV files (*.csv)", "All files (*.*)")
        else:
            if self._cached_path == norm and self._cached_data is not None:
                data = self._cached_data
            else:
                return {"error": "File data not cached — reload the file"}
            save_filename = filename
            file_types = ("All files (*.*)",)

        result = self._window.create_file_dialog(
            webview.FileDialog.SAVE,
            save_filename=save_filename,
            file_types=file_types,
        )
        if not result:
            return {"cancelled": True}

        out_path = Path(result[0] if isinstance(result, (list, tuple)) else result)
        try:
            out_path.write_bytes(data)
        except Exception as ex:
            return {"error": str(ex)}
        return {"ok": True, "path": str(out_path)}

    def get_status(self) -> dict:
        return {"message": self._status, "progress": None}
