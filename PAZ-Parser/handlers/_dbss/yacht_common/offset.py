"""The preview of a keyed Yar! `*offset.dbss` index: key, data offset and size per row."""

from __future__ import annotations

from pathlib import Path

from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pabr_offset import parse_bare_u32_offset_rows


def yacht_offset_handler(lang_dir: Path) -> OffsetTableHandler:
    """An offset table read with `parse_bare_u32_offset_rows()`, labelled from `lang_dir`."""
    return keyed_offset_handler(lang_dir, parse_bare_u32_offset_rows)
