"""The text and image previews: the facts in their toolbar line and the lines shown."""
from __future__ import annotations

import re
import struct

import pytest

from bdo_models import PazEntry
from bdo_preview import TextHandler, decode_text_with_encoding
from preview_views import dds_format, image_meta, line_ending, text_lines, text_view_html
from ui_text import ui_text

_DDPF_ALPHAPIXELS = 0x1
_DDPF_FOURCC = 0x4


def _dds_header(*, mips: int, flags: int, fourcc: bytes = b"\0\0\0\0", bits: int = 0) -> bytes:
    header = bytearray(128)
    header[:4] = b"DDS "
    struct.pack_into("<I", header, 28, mips)
    struct.pack_into("<I", header, 80, flags)
    header[84:88] = fourcc
    struct.pack_into("<I", header, 88, bits)
    return bytes(header)


def _meta(html: str) -> str:
    match = re.search(r'<span class="view-meta">([^<]*)</span>', html)
    assert match
    return match.group(1)


@pytest.mark.parametrize(
    ("text", "ending"),
    [("a\r\nb\r\n", "CRLF"), ("a\nb", "LF"), ("a\rb", "CR"), ("one line", None)],
)
def test_line_ending_is_the_first_line_break(text: str, ending: str | None) -> None:
    assert line_ending(text) == ending


def test_a_final_line_break_starts_no_extra_line() -> None:
    assert text_lines("a\r\nb\r\n") == ["a", "b"]
    assert text_lines("a\n\nb") == ["a", "", "b"]


def test_text_view_numbers_every_line_and_names_encoding_and_ending() -> None:
    html = text_view_html("<root>\r\n  <a/>\r\n</root>\r\n", "cp949")

    assert html.count('<div class="text-line">') == 3
    assert _meta(html) == " · ".join([ui_text("preview.lineMany", count="3"), "CP949", "CRLF"])
    assert 'data-action="toggle-wrap"' in html


def test_text_handler_reports_the_encoding_that_read_the_file() -> None:
    korean = "<!-- 설명 -->\n".encode("cp949")
    entry = PazEntry("t.paz", "character/x.xml", 0, len(korean), len(korean), 0, 0)

    assert decode_text_with_encoding(korean)[1] == "cp949"
    assert "CP949" in _meta(TextHandler().render(korean, entry, {}))


def test_dds_format_reads_fourcc_and_mip_count() -> None:
    assert dds_format(_dds_header(mips=11, flags=_DDPF_FOURCC, fourcc=b"DXT5")) == ("DXT5", 11)


def test_dds_format_names_an_uncompressed_layout() -> None:
    header = _dds_header(mips=0, flags=0x40 | _DDPF_ALPHAPIXELS, bits=32)
    assert dds_format(header) == ("RGBA 32-bit", 1)


def test_dds_format_ignores_other_data() -> None:
    assert dds_format(b"\x89PNG" + bytes(200)) is None
    assert dds_format(b"DDS ") is None


def test_image_meta_adds_dds_facts_after_the_size() -> None:
    header = _dds_header(mips=11, flags=_DDPF_FOURCC, fourcc=b"DXT5")
    size = ui_text("iconPreview.size", width=1024, height=1024)

    assert image_meta(1024, 1024, header) == " · ".join([size, "DXT5", ui_text("preview.mipMany", count="11")])
    assert image_meta(None, None, b"GIF89a", "GIF") == "GIF"
