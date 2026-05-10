from __future__ import annotations

import time
from pathlib import Path

import webview

from .bdo_api_helpers import _DISK_VIRTUAL_PREFIX, _norm
from bdo_models import PazEntry
from paz.bdo_payload_cache import cached_read_entry_payload
from paz.bdo_payload_reader import can_range_read, read_entry_range
from bdo_preview import (
    AltViewHandler,
    DdsHandler,
    HEX_ROWS_PER_PAGE,
    HexHandler,
    PARSED_RECORDS_PER_PAGE,
    StreamPreviewHandler,
    TextHandler,
    get_handler,
)

_hex_handler = HexHandler()
_HEX_BYTES_PER_PAGE = HEX_ROWS_PER_PAGE * 16


class PreviewMixin:
    """Preview assembly, entry loading, hex/parsed paging, and export methods."""

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
        elif has_parsed:
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
            "hex_paging": "full-buffer",
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
            "hex_paging": "none",
            "stream": {
                "url": stream_url,
                "mime": handler.mime_type,
            },
        }

    def _build_hex_range_response(
        self,
        page_bytes: bytes,
        internal_path: str,
        entry: PazEntry,
        meta: dict,
    ) -> dict:
        """Build a load_entry response for HexHandler entries using range-reads.

        Stores entry but not full data — get_hex_page will seek per-page.
        """
        self._cached_path = _norm(internal_path)
        self._cached_data = None
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = {}

        hex_html = _hex_handler.render_bytes(page_bytes, 0)
        return {
            "html": None,
            "hex_html": hex_html,
            "has_parsed": False,
            "tab_labels": None,
            "meta": meta,
            "hex_total_pages": HexHandler.page_count_for_size(entry.uncompressed_size),
            "parsed_total_pages": 1,
            "hex_paging": "range",
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

        # Fast path: hex-only entry stored raw — seek directly, skip full decode.
        if isinstance(handler, HexHandler) and can_range_read(entry):
            try:
                start = self._ts()
                page_bytes = read_entry_range(
                    self._paz_root / entry.archive_name, entry, 0, _HEX_BYTES_PER_PAGE
                )
                read_range_ms = (time.perf_counter() - start) * 1000 if self._profile else 0.0
            except Exception as ex:
                return {"error": str(ex), "meta": meta}
            response = self._build_hex_range_response(page_bytes, internal_path, entry, meta)
            if self._profile:
                response["profile"] = {
                    "backend.read_range_ms": read_range_ms,
                    "backend.read_payload_ms": 0.0,
                    "backend.load_companions_ms": 0.0,
                }
            return response

        try:
            start = self._ts()
            data = cached_read_entry_payload(
                archive_path=self._paz_root / entry.archive_name,
                entry=entry,
            )
        except Exception as ex:
            return {"error": str(ex), "meta": meta}
        read_payload_ms = (time.perf_counter() - start) * 1000 if self._profile else 0.0

        start = self._ts()
        companions: dict[str, bytes] = {**self._disk_companions, **self._load_companions_parallel(handler, entry)}
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
            return {"hex_html": _hex_handler.render_page(data, page)}

        # Range-read path: entry loaded without full payload (HexHandler fast path).
        if (
            self._cached_path == norm
            and self._cached_data is None
            and self._cached_entry is not None
            and self._paz_root is not None
            and can_range_read(self._cached_entry)
        ):
            entry = self._cached_entry
            page_offset = page * HEX_ROWS_PER_PAGE * 16
            try:
                chunk = read_entry_range(
                    self._paz_root / entry.archive_name, entry, page_offset, _HEX_BYTES_PER_PAGE
                )
            except Exception as ex:
                return {"error": str(ex)}
            return {"hex_html": _hex_handler.render_bytes(chunk, page_offset)}

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
                data = cached_read_entry_payload(
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
        if self._cached_data is None or self._cached_entry is None:
            return {"error": "Page data not cached — reload the file first"}
        try:
            html = self._cached_handler.render_data_page(
                self._cached_data,
                self._cached_entry,
                self._cached_companions,
                page,
                PARSED_RECORDS_PER_PAGE,
            )
        except Exception as ex:
            html = f'<div class="error">Render error: {_html_mod.escape(str(ex))}</div>'
        return {"html": html}

    def export_file(self, path: str, tab: str) -> dict:
        if self._window is None:
            return {"error": "Window not initialized"}

        norm = _norm(path)
        filename = norm.rsplit("/", 1)[-1]

        if tab == "parsed" and self._cached_path == norm and (
            self._cached_data is not None
            and self._cached_entry is not None
            and self._cached_handler is not None
        ):
            import csv
            import io
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
