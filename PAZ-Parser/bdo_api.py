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


def _save_config(updates: dict) -> None:
    cfg = _load_config()
    cfg.update(updates)
    try:
        _CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
    except Exception:
        pass

from bdo_cache import load_cache, read_meta_version, save_cache
from bdo_models import PazEntry
from bdo_paz_extract import extract_entry, find_single_meta_file, parse_meta_file
from bdo_payload_reader import read_entry_payload
from bdo_preview import (
    AltViewHandler, DdsHandler, HEX_ROWS_PER_PAGE, HexHandler, PARSED_RECORDS_PER_PAGE,
    StreamPreviewHandler, TextHandler, get_handler, set_handler_lang,
)

_hex_handler = HexHandler()
_HEX_BYTES_PER_PAGE = HEX_ROWS_PER_PAGE * 16


_ICON_MAP: dict[str, str] = {
    ".dds": "🖼", ".png": "🖼", ".jpg": "🖼", ".jpeg": "🖼", ".bmp": "🖼", ".tga": "🖼",
    ".xml": "📋", ".json": "📋", ".yaml": "📋", ".yml": "📋",
    ".txt": "📄", ".log": "📄", ".csv": "📄", ".ini": "📄", ".cfg": "📄",
    ".htm": "🌐", ".html": "🌐",
    ".lua": "📜",
    ".webm": "🎬",
    ".pac": "📦", ".bss": "🔒", ".dbss": "🔒",
    ".loc": "💬",
}

_DISK_VIRTUAL_PREFIX = "__disk__"

_LOC_LANG_MAP: dict[str, tuple[str, ...] | None] = {
    "en": ("ads", "languagedata_en.loc"),
    "de": ("ads", "languagedata_de.loc"),
    "fr": ("ads", "languagedata_fr.loc"),
    "sp": ("ads", "languagedata_sp.loc"),
    "ru": ("ads", "languagedata_ru.loc"),
    "kr": None,
}
_VALID_LANGUAGES = frozenset(_LOC_LANG_MAP)


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


class Api:
    def __init__(self, profile: bool = False, server: Any | None = None) -> None:
        self._profile = profile
        self._server = server
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
        self._cached_record_search_text: list[str] | None = None
        self._cached_handler = None
        self._cached_entry: PazEntry | None = None
        self._cached_companions: dict[str, bytes] = {}
        self._global_search_cancel: threading.Event = threading.Event()

    def set_window(self, window: webview.Window) -> None:
        self._window = window
        set_handler_lang(_load_config().get("language", "en"))

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _ts(self) -> float:
        return time.perf_counter() if self._profile else 0.0

    def _te(self, profile: dict, key: str, start: float) -> None:
        if self._profile:
            profile[key] = (time.perf_counter() - start) * 1000

    def _push_js(self, js: str) -> None:
        if self._window is not None:
            try:
                self._window.evaluate_js(js)
            except Exception:
                pass

    def _push_status(self, msg: str | dict, progress: tuple[int, int] | None = None) -> None:
        self._status = msg if isinstance(msg, str) else msg.get("key", "")
        data: dict = msg if isinstance(msg, dict) else {"message": msg}
        data["progress"] = list(progress) if progress else None
        self._push_js(f"app.setStatus({json.dumps(data)})")

    # ── Folder ────────────────────────────────────────────────────────────────

    def open_folder(self) -> dict:
        if self._window is None:
            return {"ok": False, "error": "Window not initialized"}
        result = self._window.create_file_dialog(webview.FileDialog.FOLDER)
        if not result:
            return {"ok": False}
        self._paz_root = Path(result[0])
        _save_config({"last_folder": str(self._paz_root)})
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

    def browse_folder(self) -> dict:
        """Open a folder picker without side effects — for use in the settings modal."""
        if self._window is None:
            return {"ok": False, "error": "Window not initialized"}
        result = self._window.create_file_dialog(webview.FileDialog.FOLDER)
        if not result:
            return {"ok": False}
        return {"ok": True, "path": str(Path(result[0]))}

    # ── Settings ──────────────────────────────────────────────────────────────

    def get_settings(self) -> dict:
        cfg = _load_config()
        return {
            "paz_path": cfg.get("last_folder", ""),
            "language": cfg.get("language", "en"),
        }

    def save_settings(self, paz_path: str, language: str) -> dict:
        if language not in _VALID_LANGUAGES:
            return {"ok": False, "error": f"Invalid language: {language}"}
        old_cfg = _load_config()
        _save_config({"last_folder": paz_path, "language": language})
        self._reload_loc(language)
        if paz_path != old_cfg.get("last_folder", "") and Path(paz_path).is_dir():
            self._paz_root = Path(paz_path)
            threading.Thread(target=self._load_entries, daemon=True).start()
        return {"ok": True}

    def _reload_loc(self, language: str) -> None:
        from _common.loc import init_loc  # noqa: PLC0415
        set_handler_lang(language)
        rel = _LOC_LANG_MAP.get(language)
        if rel is None or not self._paz_root:
            init_loc(None)
            return
        path = self._paz_root.parent.joinpath(*rel)
        if path.exists():
            try:
                init_loc(path.read_bytes())
            except Exception:
                pass
        else:
            init_loc(None)

    def _load_entries(self) -> None:
        assert self._paz_root is not None
        try:
            meta_path = find_single_meta_file(self._paz_root)
            current_version = read_meta_version(meta_path)
            cached = load_cache(self._paz_root)

            if cached and cached[0] == current_version:
                _, entries = cached
                msg = {"key": "status.loadedFromCache", "args": {"count": f"{len(entries):,}", "version": current_version}}
            else:
                stop_ticker = threading.Event()
                start = time.monotonic()

                def _ticker(stop: threading.Event, t0: float) -> None:
                    while not stop.is_set():
                        elapsed = int(time.monotonic() - t0)
                        self._push_status(
                            {"key": "status.parsing", "args": {"elapsed": elapsed}}
                        )
                        stop.wait(0.5)

                threading.Thread(target=_ticker, args=(stop_ticker, start), daemon=True).start()
                try:
                    entries = parse_meta_file(meta_path)
                finally:
                    stop_ticker.set()

                save_cache(self._paz_root, current_version, entries)
                msg = {"key": "status.parsedAndCached", "args": {"count": f"{len(entries):,}", "version": current_version}}

            self._entries = entries
            self._entry_map = {_norm(e.internal_path): e for e in entries}
            self._tree_data = self._build_tree_data(entries)
            self._load_disk_companions()
            self._push_status(msg)
            self._push_js("app.onFolderLoaded()")

        except Exception as ex:
            self._push_status({"key": "status.error", "args": {"message": str(ex)}})
            self._push_js(f"app.showError({json.dumps(str(ex))})")

    def _load_disk_companions(self) -> None:
        if not self._paz_root:
            return
        language = _load_config().get("language", "en")
        rel = _LOC_LANG_MAP.get(language)
        if rel is not None:
            path = self._paz_root.parent.joinpath(*rel)
            if path.exists():
                try:
                    raw = path.read_bytes()
                    self._disk_companions[rel[-1]] = raw
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

    def get_entry(self, internal_path: str) -> PazEntry | None:
        return self._entry_map.get(_norm(internal_path))

    def read_entry(self, internal_path: str) -> bytes:
        entry = self.get_entry(internal_path)
        if not entry or not self._paz_root:
            raise FileNotFoundError(internal_path)
        return read_entry_payload(
            archive_path=self._paz_root / entry.archive_name,
            entry=entry,
        )

    def get_stream_mime_type(self, internal_path: str) -> str:
        p = Path(internal_path)
        handler = get_handler(p.name, p.suffix)
        if isinstance(handler, StreamPreviewHandler):
            return handler.mime_type
        return "application/octet-stream"

    def is_streamable(self, internal_path: str) -> bool:
        p = Path(internal_path)
        return isinstance(get_handler(p.name, p.suffix), StreamPreviewHandler)

    def stream_url(self, internal_path: str) -> str:
        if self._server is None:
            raise RuntimeError("Local stream server not available")
        return self._server.stream_url(_norm(internal_path))

    def get_server_info(self) -> dict:
        if self._server is None:
            return {}
        return {"port": self._server.port, "token": self._server.token}

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
        profile: dict[str, float] = {}
        is_alt   = isinstance(handler, AltViewHandler)
        is_plain = isinstance(handler, (HexHandler, TextHandler, DdsHandler))
        has_parsed = not is_plain and not is_alt

        self._cached_path = _norm(internal_path)
        self._cached_data = data
        self._cached_records = None
        self._cached_record_search_text = None
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = companions

        hex_total_pages = HexHandler.page_count(data)
        start = self._ts()
        hex_html = _hex_handler.render_page(data, 0)
        self._te(profile, "backend.hex_render_ms", start)

        html = None
        parsed_total_pages = 1
        tab_labels = None

        if is_alt:
            try:
                start = self._ts()
                hex_html = handler.render(data, entry, companions)
                self._te(profile, "backend.alt_primary_render_ms", start)
            except Exception as ex:
                hex_html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
            try:
                start = self._ts()
                html = handler.render_alt(data, entry, companions)
                self._te(profile, "backend.alt_secondary_render_ms", start)
            except Exception as ex:
                html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
            hex_total_pages = 1
            tab_labels = [handler.primary_label, handler.alt_label]
        elif has_parsed and handler.supports_lazy_records():
            self._cached_handler = handler
            try:
                start = self._ts()
                record_count = handler.get_record_count(data, entry, companions)
                self._te(profile, "backend.lazy_count_ms", start)
                parsed_total_pages = max(1, (record_count + PARSED_RECORDS_PER_PAGE - 1) // PARSED_RECORDS_PER_PAGE)
                start = self._ts()
                html = handler.render_data_page(data, entry, companions, 0, PARSED_RECORDS_PER_PAGE)
                self._te(profile, "backend.lazy_page_render_ms", start)
            except Exception as ex:
                html = f'<div class="error">Parse error: {_html_mod.escape(str(ex))}</div>'
        elif has_parsed:
            try:
                start = self._ts()
                records = handler.get_records(data, entry, companions)
                self._te(profile, "backend.parse_records_ms", start)
            except Exception as ex:
                records = None
                html = f'<div class="error">Parse error: {_html_mod.escape(str(ex))}</div>'

            if records is not None:
                self._cached_records = records
                self._cached_handler = handler
                parsed_total_pages = max(1, (len(records) + PARSED_RECORDS_PER_PAGE - 1) // PARSED_RECORDS_PER_PAGE)
                try:
                    start = self._ts()
                    html = handler.render_records_page(records, 0, PARSED_RECORDS_PER_PAGE)
                    self._te(profile, "backend.parsed_page_render_ms", start)
                except Exception as ex:
                    html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
        elif not isinstance(handler, HexHandler):
            try:
                start = self._ts()
                html = handler.render(data, entry, companions)
                self._te(profile, "backend.render_ms", start)
            except Exception as ex:
                html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'

        response = {
            "html": html,
            "hex_html": hex_html,
            "has_parsed": has_parsed or is_alt,
            "tab_labels": tab_labels,
            "meta": meta,
            "hex_total_pages": hex_total_pages,
            "parsed_total_pages": parsed_total_pages,
        }
        if self._profile:
            response["profile"] = profile
        return response

    def _build_stream_response(
        self,
        internal_path: str,
        entry: PazEntry,
        handler: StreamPreviewHandler,
        meta: dict,
    ) -> dict:
        import html as _html_mod

        self._cached_path = _norm(internal_path)
        self._cached_data = None
        self._cached_records = None
        self._cached_record_search_text = None
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = {}

        try:
            stream_url = self.stream_url(entry.internal_path)
            html = handler.render_stream(stream_url, entry)
        except Exception as ex:
            stream_url = ""
            html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'

        return {
            "html": html,
            "hex_html": "",
            "has_parsed": False,
            "tab_labels": None,
            "meta": meta,
            "hex_total_pages": max(1, (entry.uncompressed_size + _HEX_BYTES_PER_PAGE - 1) // _HEX_BYTES_PER_PAGE),
            "parsed_total_pages": 1,
            "stream": {
                "url": stream_url,
                "mime": handler.mime_type,
            },
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

        p = Path(entry.internal_path)
        handler = get_handler(p.name, p.suffix)

        if isinstance(handler, StreamPreviewHandler):
            response = self._build_stream_response(internal_path, entry, handler, meta)
            if self._profile:
                response["profile"] = {
                    "backend.read_payload_ms": 0.0,
                    "backend.load_companions_ms": 0.0,
                }
            return response

        try:
            start = self._ts()
            data = read_entry_payload(
                archive_path=self._paz_root / entry.archive_name,
                entry=entry,
            )
        except Exception as ex:
            return {"error": str(ex), "meta": meta}
        read_payload_ms = (time.perf_counter() - start) * 1000 if self._profile else 0.0

        companions: dict[str, bytes] = dict(self._disk_companions)
        start = self._ts()
        for cp in handler.companions(entry):
            raw = self._load_companion_sync(cp)
            if raw is not None:
                companions[Path(cp).name] = raw
        load_companions_ms = (time.perf_counter() - start) * 1000 if self._profile else 0.0

        response = self._build_entry_response(data, internal_path, entry, handler, companions, meta)
        if self._profile:
            response.setdefault("profile", {})
            response["profile"]["backend.read_payload_ms"] = read_payload_ms
            response["profile"]["backend.load_companions_ms"] = load_companions_ms
        return response

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
        if self._cached_path != norm or self._cached_handler is None:
            return {"error": "Page data not cached — reload the file first"}
        try:
            if self._cached_records is not None:
                html = self._cached_handler.render_records_page(
                    self._cached_records, page, PARSED_RECORDS_PER_PAGE
                )
            elif (
                self._cached_data is not None
                and self._cached_entry is not None
                and self._cached_handler.supports_lazy_records()
            ):
                html = self._cached_handler.render_data_page(
                    self._cached_data,
                    self._cached_entry,
                    self._cached_companions,
                    page,
                    PARSED_RECORDS_PER_PAGE,
                )
            else:
                return {"error": "Page data not cached — reload the file first"}
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
                        {"key": "status.extracting", "args": {"done": i, "total": total, "extracted": extracted, "skipped": skipped, "failed": failed}},
                        (i, total),
                    )

            self._push_status({"key": "status.extractDone", "args": {"extracted": extracted, "skipped": skipped, "failed": failed}})
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
            if self._cached_path != norm:
                return {"error": "No parsed data cached — reload the file"}
            if (
                self._cached_records is None
                and self._cached_data is not None
                and self._cached_entry is not None
                and self._cached_handler is not None
                and self._cached_handler.supports_lazy_records()
            ):
                indices = self._cached_handler.search_records(
                    self._cached_data,
                    self._cached_entry,
                    self._cached_companions,
                    query,
                )
                return {"record_indices": indices, "total": len(indices)}
            if self._cached_records is None:
                return {"error": "No parsed data cached — reload the file"}
            q = query.lower()
            if self._cached_record_search_text is None:
                self._cached_record_search_text = [
                    "\t".join(str(value).lower() for value in rec.values())
                    for rec in self._cached_records
                ]
            indices = [
                i for i, text in enumerate(self._cached_record_search_text)
                if q in text
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

        if tab == "parsed" and self._cached_path == norm and (
            self._cached_records is not None
            or (
                self._cached_data is not None
                and self._cached_entry is not None
                and self._cached_handler is not None
                and self._cached_handler.supports_lazy_records()
            )
        ):
            import csv
            import io
            records = self._cached_records
            if records is None:
                records = self._cached_handler.get_records(
                    self._cached_data,
                    self._cached_entry,
                    self._cached_companions,
                )
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
            elif norm in self._entry_map and self._paz_root:
                try:
                    data = self.read_entry(norm)
                except Exception as ex:
                    return {"error": str(ex)}
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

        path_str = result[0] if isinstance(result, (list, tuple)) else result
        out_path = Path(str(path_str))
        try:
            out_path.write_bytes(data)
        except Exception as ex:
            return {"error": str(ex)}
        return {"ok": True, "path": str(out_path)}

    def get_status(self) -> dict:
        return {"message": self._status, "progress": None}

    # ── Global content search ─────────────────────────────────────────────────

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

    def _run_global_search(
        self,
        needles: list[bytes],
        candidates: list,
        paz_root: Path,
        cancel: threading.Event,
    ) -> None:
        results: list[dict] = []
        total = len(candidates)

        for i, entry in enumerate(candidates):
            if cancel.is_set():
                return

            if i % 50 == 0:
                self._push_status({"key": "status.searching", "args": {"done": i, "total": total, "matches": len(results)}})

            try:
                data = read_entry_payload(
                    archive_path=paz_root / entry.archive_name,
                    entry=entry,
                )
            except Exception:
                continue

            offsets: list[int] = []
            seen: set[int] = set()
            for needle in needles:
                pos = 0
                while (idx := data.find(needle, pos)) != -1:
                    if idx not in seen:
                        seen.add(idx)
                        offsets.append(idx)
                    pos = idx + 1

            if offsets:
                offsets.sort()
                results.append({
                    "path":  _norm(entry.internal_path),
                    "name":  Path(entry.internal_path).name,
                    "count": len(offsets),
                    "first": offsets[0],
                    "icon":  _file_icon(Path(entry.internal_path).suffix),
                })

        self._push_status({"key": "status.searchDone", "args": {"matches": len(results), "total": total}})
        self._push_js(f"app.onGlobalSearchDone({json.dumps(results)})")
