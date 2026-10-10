"""HTML of the built-in text and image previews: a toolbar line, then the view.

TextHandler and DdsHandler (bdo_preview.py) call these. The controls carry
data-action attributes that ui/js/features/preview-views.js handles.
"""
from __future__ import annotations

import html as _html
import struct

from ui_text import ui_text

# DDS file layout: the "DDS " magic, then a 124-byte DDS_HEADER whose fields
# sit at these offsets from the start of the file.
_DDS_MAGIC = b"DDS "
_DDS_HEADER_END = 128
_DDS_MIP_COUNT = 28
_DDS_PF_FLAGS = 80
_DDS_FOURCC = 84
_DDS_RGB_BIT_COUNT = 88
_DDPF_ALPHAPIXELS = 0x1
_DDPF_FOURCC = 0x4

_ENCODING_NAMES = {"utf-8": "UTF-8", "cp949": "CP949"}


def _icon(name: str) -> str:
    return f'<svg class="icon" aria-hidden="true"><use href="#icon-{name}"></use></svg>'


def _count(key: str, count: int) -> str:
    return ui_text(f"{key}One" if count == 1 else f"{key}Many", count=f"{count:,}")


# ── Text ──────────────────────────────────────────────────────────────────────

def line_ending(text: str) -> str | None:
    """`CRLF`, `LF` or `CR`, whichever ends the first line; None for one line."""
    first_break = next((i for i, ch in enumerate(text) if ch in "\r\n"), None)
    if first_break is None:
        return None
    if text[first_break] == "\n":
        return "LF"
    return "CRLF" if text[first_break + 1:first_break + 2] == "\n" else "CR"


def text_lines(text: str) -> list[str]:
    """The lines of `text`; a final line break does not start another line."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if len(lines) > 1 and lines[-1] == "":
        lines.pop()
    return lines


def text_view_html(text: str, encoding: str, note_html: str = "") -> str:
    """Numbered lines under `N lines · UTF-8 · CRLF` and a Wrap lines toggle."""
    lines = text_lines(text)
    meta = [_count("preview.line", len(lines)), _ENCODING_NAMES.get(encoding, encoding.upper())]
    ending = line_ending(text)
    if ending:
        meta.append(ending)
    rows = "".join(f'<div class="text-line">{_html.escape(line)}</div>' for line in lines)
    return (
        '<div class="text-view-wrap">'
        '<div class="view-toolbar">'
        f'<span class="view-meta">{_html.escape(" · ".join(meta))}</span>'
        '<button type="button" class="with-icon" data-action="toggle-wrap" aria-pressed="false">'
        f'{_icon("wrap")}<span>{_html.escape(ui_text("preview.wrapLines"))}</span></button>'
        '</div>'
        f'<div class="text-view text-lines">{rows}</div>'
        f'{note_html}'
        '</div>'
    )


# ── Image ─────────────────────────────────────────────────────────────────────

def dds_format(data: bytes) -> tuple[str, int] | None:
    """(pixel format, mip count) from a DDS header, or None when `data` is no DDS.

    The format is the FourCC (`DXT1`, `DXT5`, `DX10` ...) for block-compressed
    textures, else the uncompressed layout such as `RGBA 32-bit`.
    """
    if len(data) < _DDS_HEADER_END or data[:4] != _DDS_MAGIC:
        return None
    mips = max(1, struct.unpack_from("<I", data, _DDS_MIP_COUNT)[0])
    flags = struct.unpack_from("<I", data, _DDS_PF_FLAGS)[0]
    if flags & _DDPF_FOURCC:
        fourcc = data[_DDS_FOURCC:_DDS_FOURCC + 4].decode("ascii", errors="replace").rstrip("\0 ")
        return (fourcc or "?"), mips
    bits = struct.unpack_from("<I", data, _DDS_RGB_BIT_COUNT)[0]
    layout = "RGBA" if flags & _DDPF_ALPHAPIXELS else "RGB"
    return f"{layout} {bits}-bit", mips


def image_meta(width: int | None, height: int | None, data: bytes, kind: str = "") -> str:
    """`1024 × 1024 px · DXT5 · 11 mips`; the DDS parts only for DDS data."""
    parts = []
    if width is not None and height is not None:
        parts.append(ui_text("iconPreview.size", width=width, height=height))
    if kind:
        parts.append(kind)
    dds = dds_format(data)
    if dds:
        fmt, mips = dds
        parts += [fmt, _count("preview.mip", mips)]
    return " · ".join(parts)


def _segmented(action: str, label_key: str, options: list[tuple[str, str]], active: str) -> str:
    buttons = "".join(
        f'<button type="button" class="{"active" if value == active else ""}" '
        f'data-action="{action}" data-value="{value}" aria-pressed="{"true" if value == active else "false"}">'
        f'{_html.escape(label)}</button>'
        for value, label in options
    )
    label = _html.escape(ui_text(label_key))
    return (f'<span class="view-label">{label}</span>'
            f'<div class="segmented" role="group" aria-label="{label}">{buttons}</div>')


def image_view_html(src: str, name: str, meta: str) -> str:
    """The image with zoom (Fit, 100%, 200%), background and a pixel readout."""
    zoom = _segmented("image-zoom", "preview.zoom",
                      [("fit", ui_text("preview.zoomFit")), ("1", "100%"), ("2", "200%")], "fit")
    background = _segmented("image-background", "preview.background",
                            [("checker", ui_text("preview.bgChecker")),
                             ("dark", ui_text("preview.bgDark")),
                             ("light", ui_text("preview.bgLight"))], "checker")
    return (
        '<div class="img-view zoom-fit">'
        '<div class="view-toolbar">'
        f'<span class="view-meta">{_html.escape(meta)}</span>'
        f'<span class="view-toolbar-gap"></span>{zoom}{background}'
        '</div>'
        '<div class="img-scroll bg-checker">'
        f'<img src="{src}" alt="{_html.escape(name)}">'
        '</div>'
        '<div class="img-readout" aria-live="off"></div>'
        '</div>'
    )
