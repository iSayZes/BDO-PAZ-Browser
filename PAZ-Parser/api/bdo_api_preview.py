from __future__ import annotations

import html
import time
from itertools import chain
from typing import Any
from pathlib import Path

import webview

from .bdo_api_helpers import _DISK_VIRTUAL_PREFIX, _norm
from .bdo_api_state import ApiState
from .bdo_icon_images import (
    checked_region,
    open_image,
    preview_data_url,
    sprite_data_url,
    thumbnail_data_url,
)
from .bdo_config import load_table_sort, save_table_sort, table_sort_file_key
from bdo_models import PazEntry
from paz.bdo_payload_cache import cached_read_entry_payload
from paz.bdo_payload_reader import can_range_read, read_entry_range
from record_export import records_to_csv
from bdo_preview import (
    AltViewHandler,
    HEX_ROWS_PER_PAGE,
    HexHandler,
    PARSED_RECORDS_PER_PAGE,
    StreamPreviewHandler,
    get_handler,
    has_parsed_view,
)
from table_sort import TableSort
from ui_text import ui_text

_hex_handler = HexHandler()
# Decoded images kept for the icon popup; a sprite sheet serves every sprite on it.
_PREVIEW_CACHE_SIZE = 4
_HEX_BYTES_PER_PAGE = HEX_ROWS_PER_PAGE * 16

# Some icons exist only under a prefixed filename in the same folder. Handlers
# emit the canonical unprefixed path, so try these siblings before the much
# slower suffix scan over every entry.
_ICON_SIBLING_PREFIXES = ("web_",)


def _error_box(key: str, ex: Exception) -> str:
    """The preview's error box: the localized label around the raw exception text."""
    return f'<div class="error">{html.escape(ui_text(key, message=str(ex)))}</div>'


def _icon_sibling_paths(norm: str) -> list[str]:
    """Return prefixed sibling paths to try for an icon path that missed."""
    folder, sep, name = norm.rpartition("/")
    if not sep or not name:
        return []

    return [
        f"{folder}/{prefix}{name}"
        for prefix in _ICON_SIBLING_PREFIXES
        if not name.startswith(prefix)
    ]


class PreviewMixin(ApiState):
    """Preview assembly, entry loading, hex/parsed paging, and export methods."""

    def _resolve_icon_entry(self, icon_path: str) -> PazEntry | None:
        norm = _norm(icon_path).strip().lstrip("/")
        if not norm:
            return None

        cache = self._icon_entry_cache
        if norm in cache:
            return cache[norm]

        entry = self._entry_map.get(norm) or self._entry_ignoring_case(norm)

        if entry is None:
            for sibling in _icon_sibling_paths(norm):
                entry = self._entry_map.get(sibling) or self._entry_ignoring_case(sibling)
                if entry is not None:
                    break

        if entry is None:
            # Lowercase paths match in `_entry_map`, the others in the folded map.
            suffix = norm.lower()
            for key, candidate in chain(self._entry_map.items(), self._entry_map_folded.items()):
                if key.endswith(suffix):
                    entry = candidate
                    break

        cache[norm] = entry
        return entry

    def get_icon_data_url(self, icon_path: str) -> dict:
        self._mark_activity()
        self._wait_for_folder_text()
        norm = _norm(icon_path).strip()
        if not norm:
            return {"error": ui_text("errors.iconPathEmpty")}

        url = self._cached_icon_url(norm)
        if url is not None:
            return {"url": url}

        # One decode at a time. Every JS call runs in its own thread, and a
        # screen of large textures would otherwise start dozens of pure-Python
        # decrypts at once and starve the window thread of the GIL.
        with self._icon_decode_lock:
            url = self._cached_icon_url(norm)
            if url is not None:
                return {"url": url}

            entry = self._resolve_icon_entry(norm)
            if entry is None:
                # The UI renders a dash for a miss, so report it rather than
                # substituting art for an icon the client does not ship.
                return {"error": ui_text("errors.iconNotFound", path=icon_path)}

            try:
                data = self.read_entry(entry.internal_path)
                url = thumbnail_data_url(data, Path(entry.internal_path).suffix)
            except Exception as ex:
                return {"error": str(ex)}

            self._icon_data_url_cache[norm] = url
            if self._thumbnail_cache is not None:
                self._thumbnail_cache.put(norm, url)
        return {"url": url}

    def get_icon_preview(self, icon_path: str, region: list[int] | None = None) -> dict:
        """The popup a click on an icon opens: the image scaled to fit, and the sprite.

        `region` is the (x1, y1, x2, y2) sprite region for sprite cells; the
        answer then also carries the cropped sprite, and the page outlines the
        region on the sheet.
        """
        self._mark_activity()
        self._wait_for_folder_text()
        norm = _norm(icon_path).strip()
        if not norm:
            return {"error": ui_text("errors.iconPathEmpty")}

        # Its own lock, so a click is not queued behind a screen of thumbnails.
        with self._icon_preview_lock:
            try:
                cached = self._preview_image(norm)
                if cached is None:
                    return {"error": ui_text("errors.iconNotFound", path=icon_path)}
                img, url = cached
                answer: dict = {"path": norm, "url": url, "width": img.width, "height": img.height}
                if region is not None:
                    box = checked_region(region, img.size)
                    answer["sprite"] = sprite_data_url(img, box)
                    answer["region"] = list(box)
            except Exception as ex:
                return {"error": str(ex)}
        return answer

    def _preview_image(self, norm: str) -> tuple[Any, str] | None:
        """(decoded image, preview data URL) of an icon path, kept for the last few.

        None when the client does not ship the path.
        """
        cache = self._icon_preview_images
        if norm in cache:
            cache[norm] = cache.pop(norm)
            return cache[norm]

        entry = self._resolve_icon_entry(norm)
        if entry is None:
            return None
        img = open_image(self.read_entry(entry.internal_path))
        cache[norm] = (img, preview_data_url(img))
        while len(cache) > _PREVIEW_CACHE_SIZE:
            cache.pop(next(iter(cache)))
        return cache[norm]

    def _cached_icon_url(self, norm: str) -> str | None:
        """A finished thumbnail from this session or the disk cache, else None."""
        url = self._icon_data_url_cache.get(norm)
        if url is None and self._thumbnail_cache is not None:
            url = self._thumbnail_cache.get(norm)
            if url is not None:
                self._icon_data_url_cache[norm] = url
        return url

    def _build_entry_response(
        self,
        data: bytes,
        internal_path: str,
        entry: PazEntry,
        handler,
        companions: dict[str, bytes],
        meta: dict,
    ) -> dict:
        profile: dict[str, float] = {}
        is_alt   = isinstance(handler, AltViewHandler)
        has_parsed = has_parsed_view(handler)

        self._cached_path = _norm(internal_path)
        self._cached_data = data
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = companions
        self._cached_sort = None

        hex_total_pages = HexHandler.page_count(data)
        start = self._ts()
        hex_html = _hex_handler.render_page(data, 0)
        self._te(profile, "backend.hex_render_ms", start)

        html = None
        parsed_total_pages = 1
        tab_labels = None
        view_label = None

        if is_alt:
            try:
                start = self._ts()
                hex_html = handler.render(data, entry, companions)
                self._te(profile, "backend.alt_primary_render_ms", start)
            except Exception as ex:
                hex_html = _error_box("preview.renderError", ex)
            try:
                start = self._ts()
                html = handler.render_alt(data, entry, companions)
                self._te(profile, "backend.alt_secondary_render_ms", start)
            except Exception as ex:
                html = _error_box("preview.renderError", ex)
            hex_total_pages = 1
            tab_labels = [ui_text(handler.primary_label_key), ui_text(handler.alt_label_key)]
        elif has_parsed:
            self._cached_handler = handler
            self._recent_tables.viewed(handler)
            try:
                start = self._ts()
                record_count = handler.get_record_count(data, entry, companions)
                self._te(profile, "backend.lazy_count_ms", start)
                parsed_total_pages = max(1, (record_count + PARSED_RECORDS_PER_PAGE - 1) // PARSED_RECORDS_PER_PAGE)
                saved_sort = load_table_sort(
                    table_sort_file_key(internal_path), handler.sortable_fields()
                )
                self._cached_sort = saved_sort or handler.default_sort()
                start = self._ts()
                html = self._render_parsed_page(0)
                self._te(profile, "backend.lazy_page_render_ms", start)
            except Exception as ex:
                html = _error_box("preview.parseError", ex)
        elif not isinstance(handler, HexHandler):
            try:
                start = self._ts()
                html = handler.render(data, entry, companions)
                self._te(profile, "backend.render_ms", start)
            except Exception as ex:
                html = _error_box("preview.renderError", ex)
            if handler.view_label_key:
                view_label = ui_text(handler.view_label_key)

        response = {
            "html": html,
            "hex_html": hex_html,
            "has_parsed": has_parsed or is_alt,
            "tab_labels": tab_labels,
            # A text or image view: shown first, under this tab name next to Hex.
            "view_label": view_label,
            "meta": meta,
            "hex_total_pages": hex_total_pages,
            "parsed_total_pages": parsed_total_pages,
            "hex_paging": "full-buffer",
            "sort": self._cached_sort.to_dict() if self._cached_sort else None,
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

        self._cached_path = _norm(internal_path)
        self._cached_data = None
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = {}
        self._cached_sort = None

        try:
            stream_url = self.stream_url(entry.internal_path)
            html = handler.render_stream(stream_url, entry)
        except Exception as ex:
            stream_url = ""
            html = _error_box("preview.renderError", ex)

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

        Stores entry but not full data; get_hex_page will seek per-page.
        """
        self._cached_path = _norm(internal_path)
        self._cached_data = None
        self._cached_handler = None
        self._cached_entry = entry
        self._cached_companions = {}
        self._cached_sort = None

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

    def disk_entry(self, name: str) -> tuple[PazEntry, bytes] | None:
        """A loaded disk file (the LOC file) as an entry, or None when not loaded."""
        data = self._disk_companions.get(name)
        if data is None:
            return None

        fake_entry = PazEntry(
            archive_name="<disk>",
            internal_path=name,
            offset=0,
            compressed_size=len(data),
            uncompressed_size=len(data),
            compression_type=0,
            encryption_type=0,
        )
        return fake_entry, data

    def entry_companions(self, handler, entry: PazEntry) -> dict[str, bytes]:
        """The disk files plus every companion the handler asks for, by file name."""
        return {**self._disk_companions, **self._load_companions_parallel(handler, entry)}

    def _load_disk_entry(self, internal_path: str) -> dict:
        name = internal_path[len(_DISK_VIRTUAL_PREFIX) + 1:]
        disk = self.disk_entry(name)
        if disk is None:
            return {"error": ui_text("errors.diskFileNotLoaded", name=name)}

        fake_entry, data = disk
        meta = {
            "archive":      "<disk>",
            "path":         name,
            "compressed":   "-",
            "uncompressed": ui_text("units.bytes", value=f"{len(data):,}"),
            "offset":       "-",
        }
        p = Path(name)
        handler = get_handler(p.name, p.suffix)
        return self._build_entry_response(data, internal_path, fake_entry, handler, {}, meta)

    def load_entry(self, internal_path: str) -> dict:
        self._mark_activity()
        self._wait_for_folder_text()
        if internal_path.startswith(_DISK_VIRTUAL_PREFIX + "/"):
            return self._load_disk_entry(internal_path)

        entry = self._entry_map.get(_norm(internal_path))
        if not entry or not self._paz_root:
            return {"error": ui_text("errors.entryNotFound")}

        meta = {
            "archive":      entry.archive_name,
            "path":         entry.internal_path,
            "compressed":   ui_text("units.bytes", value=f"{entry.compressed_size:,}"),
            "uncompressed": ui_text("units.bytes", value=f"{entry.uncompressed_size:,}"),
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

        # Fast path: hex-only entry stored raw, so seek directly and skip the full decode.
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
        companions = self.entry_companions(handler, entry)
        load_companions_ms = (time.perf_counter() - start) * 1000 if self._profile else 0.0

        response = self._build_entry_response(data, internal_path, entry, handler, companions, meta)
        if self._profile:
            response.setdefault("profile", {})
            response["profile"]["backend.read_payload_ms"] = read_payload_ms
            response["profile"]["backend.load_companions_ms"] = load_companions_ms
        return response

    def get_hex_page(self, path: str, page: int) -> dict:
        self._mark_activity()
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
                return {"error": ui_text("errors.diskFileNotLoaded", name=name)}
        else:
            entry = self._entry_map.get(norm)
            if not entry or not self._paz_root:
                return {"error": ui_text("errors.entryNotFound")}
            try:
                data = cached_read_entry_payload(
                    archive_path=self._paz_root / entry.archive_name,
                    entry=entry,
                )
            except Exception as ex:
                return {"error": str(ex)}
        return {"hex_html": _hex_handler.render_page(data, page)}

    def _render_parsed_page(self, page: int) -> str:
        """Render one page of the cached parsed table under the active sort."""
        handler = self._cached_handler
        if handler is None or self._cached_data is None or self._cached_entry is None:
            raise RuntimeError("No parsed data cached")

        args = (self._cached_data, self._cached_entry, self._cached_companions)
        if self._cached_sort is None:
            return handler.render_data_page(*args, page, PARSED_RECORDS_PER_PAGE)
        return handler.render_sorted_page(*args, page, PARSED_RECORDS_PER_PAGE, self._cached_sort)

    def get_parsed_page(self, path: str, page: int, sort_field: str = "", sort_dir: str = "") -> dict:
        """Render a parsed page. An empty `sort_field` shows file order.

        A sort is remembered per file name in the user config, so the file
        reopens with it.
        """
        self._mark_activity()
        self._wait_for_folder_text()
        norm = _norm(path)
        if self._cached_path != norm or self._cached_handler is None:
            return {"error": ui_text("errors.pageNotCached")}
        if self._cached_data is None or self._cached_entry is None:
            return {"error": ui_text("errors.pageNotCached")}

        sort: TableSort | None = None
        if sort_field:
            sort = TableSort.parse(sort_field, sort_dir)
            if sort is None or sort.field not in self._cached_handler.sortable_fields():
                return {"error": ui_text("errors.cannotSort", field=sort_field, direction=sort_dir)}
            save_table_sort(table_sort_file_key(norm), sort)
        self._cached_sort = sort

        try:
            html = self._render_parsed_page(page)
        except Exception as ex:
            html = _error_box("preview.renderError", ex)
        return {"html": html}

    def export_file(self, path: str, tab: str) -> dict:
        self._mark_activity()
        self._wait_for_folder_text()
        if self._window is None:
            return {"error": ui_text("errors.windowNotInitialized")}

        norm = _norm(path)
        filename = norm.rsplit("/", 1)[-1]

        if tab == "parsed" and self._cached_path == norm and (
            self._cached_data is not None
            and self._cached_entry is not None
            and self._cached_handler is not None
        ):
            # File order on purpose: the parse the open table already holds,
            # without the active table sort, which would only add a reorder.
            records = self._cached_handler.all_records(
                self._cached_data,
                self._cached_entry,
                self._cached_companions,
            )
            data = records_to_csv(records).encode("utf-8-sig")
            save_filename = Path(filename).stem + ".csv"
            file_types = (ui_text("dialogs.csvFiles"), ui_text("dialogs.allFiles"))
        else:
            if self._cached_path == norm and self._cached_data is not None:
                data = self._cached_data
            elif norm in self._entry_map and self._paz_root:
                try:
                    data = self.read_entry(norm)
                except Exception as ex:
                    return {"error": str(ex)}
            else:
                return {"error": ui_text("errors.fileNotCached")}
            save_filename = filename
            file_types = (ui_text("dialogs.allFiles"),)

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
