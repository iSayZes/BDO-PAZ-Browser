"""The preview of a keyed Yar! `*offset.dbss` index: key, data offset and size per row."""

from __future__ import annotations

from pathlib import Path

from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows


def yacht_offset_handler(lang_dir: Path) -> OffsetTableHandler:
    """An offset table read with `parse_bare_u32_offset_rows()`, labelled from `lang_dir`."""
    return OffsetTableHandler(
        lang_dir,
        [
            OffsetColumn("key", "key"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "key", "data_offset", "data_size"),
    )
