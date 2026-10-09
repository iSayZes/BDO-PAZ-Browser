from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .labels import life_skill_name, rank_text
from .parser import parse_lifeexp_records, parse_lifeexpoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "lifeexpoffset.dbss"
_EMPTY = "-"


def _skill_count(records: list[dict]) -> int:
    return len({record["life_skill"] for record in records})


def _offset_meta(records: list[dict], lang: str) -> str:
    return handler_text(lang, _LANG_DIR, "meta.offsetCount", count=len(records), skills=_skill_count(records))


def life_exp_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("life_skill", "lifeSkillId"),
            OffsetColumn("level", "level"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_lifeexpoffset_records,
        meta=_offset_meta,
    )


class LifeExpHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["lifeSkillId"], "num", sort_key="life_skill"),
            Column(cols["lifeSkill"], sort_key="life_skill_name"),
            Column(cols["level"], "num", sort_key="level"),
            # Sorting by Level gives the rank order.
            Column(cols["rank"]),
            Column(cols["exp"], "num", sort_key="exp"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        records = parse_lifeexp_records(data, offset_raw)
        names = {skill: life_skill_name(skill) for skill in {record["life_skill"] for record in records}}
        return [
            {**record, "life_skill_name": names[record["life_skill"]], "rank": rank_text(record["level"])}
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), skills=_skill_count(records))
        rows = [
            [
                e(r["life_skill"]),
                e(r["life_skill_name"]),
                e(r["level"]),
                e(r["rank"] or _EMPTY),
                e(f"{r['exp']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
