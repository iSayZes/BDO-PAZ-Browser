from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from .parser import parse_petexp_records, parse_petexpoffset_records


class PetExpOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petexpoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} pet exp offset records"
        headers: list[tuple[str, str, str]] = [
            ("EXP Table ID", "num", ""),
            ("Data Offset", "num", ""),
            ("Data Size", "num", ""),
        ]
        rows = [
            [
                e(r["exp_table_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class PetExpHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/petexpoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petexpoffset.dbss")
        if offset_raw is None:
            raise ValueError("petexpoffset.dbss companion not found.")

        return parse_petexp_records(data, offset_raw)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        table_count = len({r["exp_table_id"] for r in records})
        meta = f"{len(records):,} level thresholds · {table_count:,} EXP tables"
        headers: list[tuple[str, str, str]] = [
            ("EXP Table ID", "num", ""),
            ("Max Level", "num", ""),
            ("Level", "num", ""),
            ("Required EXP", "num", ""),
        ]
        rows = [
            [
                e(r["exp_table_id"]),
                e(r["max_level"]),
                e(r["level"]),
                e(r["required_exp"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
