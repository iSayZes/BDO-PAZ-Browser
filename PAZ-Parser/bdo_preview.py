from __future__ import annotations

import base64
import html as _html
import importlib.util
import io
import re as _re
from abc import ABC, abstractmethod
from pathlib import Path
import sys

from bdo_models import PazEntry

_TEXT_LIMIT = 512 * 1024   # bytes shown in text view

HEX_ROWS_PER_PAGE    = 512   # 512 × 16 bytes = 8 KB per page
PARSED_RECORDS_PER_PAGE = 500


class PreviewHandler(ABC):
    def companions(self, entry: PazEntry) -> list[str]:
        """Return internal PAZ paths of files this handler needs alongside the main file."""
        return []

    @abstractmethod
    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        """Return all records as plain dicts (raw values — no HTML).

        Parsed-view handlers must implement this. Raise NotImplementedError for
        handlers that only produce hex/text/image output (HexHandler, TextHandler,
        DdsHandler) — those are excluded from the parsed tab by `has_parsed` in
        bdo_api.py and this method is never called on them.
        """
        raise NotImplementedError

    @abstractmethod
    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        """Render HTML for one page of records.

        `records` is the full list returned by get_records(). Slice with
        ``records[page * page_size : (page + 1) * page_size]`` inside this method.
        """
        raise NotImplementedError


# ── Text ──────────────────────────────────────────────────────────────────────

class TextHandler(PreviewHandler):
    """Renders plain text files. Does not produce a parsed view."""

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        raise NotImplementedError

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        raise NotImplementedError

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        truncated = len(data) > _TEXT_LIMIT
        content   = data[:_TEXT_LIMIT].decode("utf-8", errors="replace")
        note      = ""
        if truncated:
            note = (
                f'\n<span class="hex-note">… truncated — showing first '
                f'{_TEXT_LIMIT // 1024} KB of {len(data) // 1024} KB</span>'
            )
        return f'<pre class="text-view">{_html.escape(content)}</pre>{note}'


# ── DDS / Image ───────────────────────────────────────────────────────────────

class DdsHandler(PreviewHandler):
    """Renders DDS / image files. Does not produce a parsed view."""

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        raise NotImplementedError

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        raise NotImplementedError

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        name = _html.escape(Path(entry.internal_path).name)
        ext  = Path(entry.internal_path).suffix.lower()

        if ext == ".gif":
            b64 = base64.b64encode(data).decode()
            return (
                f'<div class="img-view">'
                f'<div class="img-meta">GIF</div>'
                f'<div class="img-scroll">'
                f'<img src="data:image/gif;base64,{b64}" alt="{name}">'
                f'</div></div>'
            )

        try:
            from PIL import Image
        except ImportError:
            return '<div class="error">Pillow not installed — pip install pillow</div>'

        try:
            img = Image.open(io.BytesIO(data)).convert("RGBA")
        except Exception:
            return HexHandler().render(data, entry, companions)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        b64  = base64.b64encode(buf.getvalue()).decode()
        return (
            f'<div class="img-view">'
            f'<div class="img-meta">{img.width} × {img.height} px</div>'
            f'<div class="img-scroll">'
            f'<img src="data:image/png;base64,{b64}" alt="{name}">'
            f'</div></div>'
        )


# ── Hex dump ──────────────────────────────────────────────────────────────────

class HexHandler(PreviewHandler):
    """Renders raw hex dump. Does not produce a parsed view."""

    _ROW = 16

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        raise NotImplementedError

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        raise NotImplementedError

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        return self.render_page(data, 0)

    def render_page(self, data: bytes, page: int, rows_per_page: int = HEX_ROWS_PER_PAGE) -> str:
        byte_start = page * rows_per_page * self._ROW
        byte_end   = byte_start + rows_per_page * self._ROW
        chunk      = data[byte_start:byte_end]
        rows       = "".join(
            self._row_html(byte_start + i, chunk[i:i + self._ROW])
            for i in range(0, len(chunk), self._ROW)
        )
        return f'<div class="hex-view">{rows}</div>'

    @staticmethod
    def page_count(data: bytes, rows_per_page: int = HEX_ROWS_PER_PAGE) -> int:
        total_rows = (len(data) + HexHandler._ROW - 1) // HexHandler._ROW
        return max(1, (total_rows + rows_per_page - 1) // rows_per_page)

    def _row_html(self, offset: int, chunk: bytes) -> str:
        hex_part   = " ".join(f"{b:02X}" for b in chunk)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        n          = self._ROW
        return (
            f'<div class="hex-row">'
            f'<span class="hex-offset">{offset:08X}</span>'
            f'<span class="hex-bytes">{_html.escape(f"{hex_part:<{n * 3}}")}</span>'
            f'<span class="hex-ascii">{_html.escape(ascii_part)}</span>'
            f'</div>'
        )


# ── Alt-view (two-tab: primary render + alternate render) ─────────────────────

class AltViewHandler(PreviewHandler):
    """Two-tab handler with a primary view (e.g. text) and an alternate view (e.g. rendered).

    Override render() for the primary tab and render_alt() for the secondary tab.
    Set primary_label / alt_label class attributes to name the tabs.
    """

    primary_label: str = "Text"
    alt_label: str = "Rendered"

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:  # noqa: ARG002
        raise NotImplementedError

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:  # noqa: ARG002
        raise NotImplementedError

    @abstractmethod
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str: ...

    @abstractmethod
    def render_alt(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str: ...


class SvgHandler(AltViewHandler):
    """SVG files: Text tab shows source, Rendered tab shows the image inline."""

    primary_label = "Text"
    alt_label = "Rendered"

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        content = data.decode("utf-8", errors="replace")
        return f'<pre class="text-view">{_html.escape(content)}</pre>'

    def render_alt(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        import re as _re
        text = data.decode("utf-8", errors="replace")
        # Strip XML declaration and DOCTYPE — external DTD references block Chromium data-URI rendering
        text = _re.sub(r"<\?xml[^?]*\?>", "", text)
        text = _re.sub(r"<!DOCTYPE[^>]*>", "", text)
        b64  = base64.b64encode(text.encode("utf-8")).decode()
        name = _html.escape(Path(entry.internal_path).name)
        return (
            f'<div class="img-view">'
            f'<div class="img-scroll">'
            f'<img src="data:image/svg+xml;base64,{b64}" alt="{name}">'
            f'</div></div>'
        )


# ── Registry ──────────────────────────────────────────────────────────────────

_image_handler = DdsHandler()

_REGISTRY: dict[str, PreviewHandler] = {
    **{ext: TextHandler() for ext in (
        ".xml", ".json", ".txt", ".csv", ".ini", ".cfg",
        ".log", ".htm", ".html", ".yaml", ".yml", ".lua",
        ".ai", ".css", ".js", ".h", ".srt",
        ".mxml", ".weathercolortablexml", ".xmp",
    )},
    **{ext: _image_handler for ext in (
        ".dds", ".dds1", ".dds11",
        ".png", ".jpg", ".bmp", ".gif", ".tga", ".tif",
    )},
    ".svg": SvgHandler(),
}

_BUILTIN_KEYS: frozenset[str] = frozenset(_REGISTRY)
_PLUGIN_MODULE_NAMES: list[str] = []
_PLUGIN_SYS_MODULES: set[str] = set()

_hex_handler = HexHandler()


def get_handler(name: str, ext: str) -> PreviewHandler:
    """Return best handler for a file: filename match → extension → HexHandler."""
    return (
        _REGISTRY.get(name.lower())
        or _REGISTRY.get(ext.lower())
        or _hex_handler
    )


def register_handler(key: str, handler: PreviewHandler) -> None:
    """Register by filename (e.g. 'titleoffset.dbss') or extension (e.g. '.dbss')."""
    _REGISTRY[key.lower()] = handler


def get_binary_handlers() -> list[str]:
    """Return sorted list of registered binary (non-builtin) handler keys."""
    return sorted(k for k in _REGISTRY if k not in _BUILTIN_KEYS)


def get_builtin_formats() -> list[str]:
    """Return sorted list of built-in (text/image) format extensions."""
    return sorted(_BUILTIN_KEYS)


def unique_format_keys(entries: list[PazEntry]) -> list[str]:
    """Return sorted unique format keys derived from PAZ entries.

    Formats with a named registry entry (e.g. 'title.dbss') are keyed by
    full filename so each is counted separately. Everything else is keyed by
    extension (e.g. '.pac'), grouping unknown variants together.
    """
    _numeric_bss = _re.compile(r"^\d+_\d+\.bss$")

    keys: set[str] = set()
    for entry in entries:
        name = entry.internal_path.replace("\\", "/").rsplit("/", 1)[-1].lower()
        if "." not in name:
            continue
        ext  = "." + name.rsplit(".", 1)[-1]
        if name in _REGISTRY:
            keys.add(name)
        elif _numeric_bss.match(name):
            keys.add("x_y.bss")
        elif ext in (".bss", ".dbss"):
            keys.add(name)
        else:
            keys.add(ext)
    return sorted(keys)


# ── Plugin auto-loader ────────────────────────────────────────────────────────

def load_plugins(handlers_dir: Path) -> None:
    """Import every *.py file in handlers_dir that doesn't start with '_'."""
    if not handlers_dir.is_dir():
        return

    handlers_path = str(handlers_dir.resolve())

    if handlers_path not in sys.path:
        sys.path.insert(0, handlers_path)

    before = set(sys.modules)

    for py_file in sorted(handlers_dir.glob("*.py")):
        if py_file.name.startswith("_"):
            continue

        spec = importlib.util.spec_from_file_location(py_file.stem, py_file)

        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)

        try:
            sys.modules[py_file.stem] = module
            spec.loader.exec_module(module)
            _PLUGIN_MODULE_NAMES.append(py_file.stem)
        except Exception as ex:
            print(f"[handlers] Failed to load {py_file.name}: {ex}")

    _PLUGIN_SYS_MODULES.update(set(sys.modules) - before)


def reload_plugins(handlers_dir: Path) -> None:
    """Clear plugin-registered handlers and re-import all plugins."""
    for key in list(_REGISTRY):
        if key not in _BUILTIN_KEYS:
            del _REGISTRY[key]
    for name in _PLUGIN_SYS_MODULES:
        sys.modules.pop(name, None)
    _PLUGIN_SYS_MODULES.clear()
    _PLUGIN_MODULE_NAMES.clear()
    load_plugins(handlers_dir)


load_plugins(Path(__file__).parent / "handlers")
