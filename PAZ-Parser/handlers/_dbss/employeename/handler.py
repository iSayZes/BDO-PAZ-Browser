from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import parse_employeename_records, parse_employeenameoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def employee_name_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("employee_name_id", "employeeNameId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_employeenameoffset_records,
    )


class EmployeeNameHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["employeeNameId"], "num", sort_key="employee_name_id"),
            Column(cols["name"], sort_key="name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/employeenameoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("employeenameoffset.dbss")
        if offset_raw is None:
            raise ValueError("employeenameoffset.dbss companion not found.")

        records = parse_employeename_records(data, offset_raw)
        result: list[dict] = []
        for record in records:
            row = dict(record)
            if is_loc_loaded():
                row["name_en"] = strip_pa_tags(
                    loc_lookup(71, record["employee_name_id"], 0, 12)
                )
            row["name"] = row.get("name_en") or record["name_kr"]
            result.append(row)

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["employee_name_id"]),
                e(r["name"]),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
