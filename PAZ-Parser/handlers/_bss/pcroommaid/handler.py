from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import parse_bare_offset_rows
from _dbss.maid.parser import FILE_NAME as MAID_FILE, OFFSET_FILE as MAID_OFFSET_FILE
from .parser import parse_pcroommaid


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAID_PATH = f"gamecommondata/binary/{MAID_FILE}"
_LINK_CLASS = "record-link"


def maid_offset_companion(internal_path: str) -> str:
    """The `maidoffset.dbss` path next to a file in the same folder."""
    folder = internal_path.rsplit("/", 1)[0]
    return f"{folder}/{MAID_OFFSET_FILE}"


def maid_row_keys(companions: dict[str, bytes]) -> frozenset[int] | None:
    """Every `maid.dbss` key, or None when `maidoffset.dbss` is missing.

    Raises ValueError, naming the companion, when its rows do not parse.
    """
    offset_raw = companions.get(MAID_OFFSET_FILE)
    if offset_raw is None:
        return None
    try:
        rows = parse_bare_offset_rows(offset_raw)
    except ValueError as ex:
        raise ValueError(f"{MAID_OFFSET_FILE}: {ex}") from ex
    return frozenset(row.entry_id for row in rows)


def maid_key_cell(character_key: int, has_maid_row: bool) -> str:
    """The key as a link to its `maid.dbss` row, or plain text without one."""
    if not has_maid_row:
        return e(character_key)
    return record_link(str(character_key), _MAID_PATH, "character_key", character_key, _LINK_CLASS)


class PcRoomMaidBssHandler(PreviewHandler):
    """Each key links to its `maid.dbss` row, which links on to `characterstatic.dbss`."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [maid_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        maid_keys = maid_row_keys(companions)
        return [
            {
                **record,
                "name": character_name(record["character_key"]),
                # True when maidoffset.dbss is missing, so the link stays.
                "has_maid_row": maid_keys is None or record["character_key"] in maid_keys,
            }
            for record in parse_pcroommaid(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                maid_key_cell(r["character_key"], r["has_maid_row"]),
                e(r["name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
