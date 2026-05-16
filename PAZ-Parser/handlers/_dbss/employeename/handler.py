from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_employeename_records, parse_employeenameoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


class EmployeeNameOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_employeenameoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
        ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("employeeNameId", "Employee Name ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(r["employee_name_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class EmployeeNameHandler(PreviewHandler):
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
        meta = f"{len(records):,} employee names"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("employeeNameId", "Employee Name ID"), "num", ""),
            (cols.get("name", "Name"), "", ""),
        ]
        rows = [
            [
                e(r["employee_name_id"]),
                e(r.get("name_en") or r["name_ko"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
