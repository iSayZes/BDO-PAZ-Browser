"""minigamefind.bss preview handler: one row per Lakiaro minigame game type, with its Lakiaro rows."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e, text_list_cell
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_minigamefind


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 6
_NUMBER_SEPARATOR = ", "
# begin_root_count is stored Left, Right, Top, Bottom.
_SIDE_LABEL_KEYS = ("left", "right", "top", "bottom")


def _present(keys: Sequence[int]) -> list[int]:
    """The set item keys of a slot list; `0` marks a free slot."""
    return [key for key in keys if key]


def _numbers_text(values: Sequence[int]) -> str:
    return _NUMBER_SEPARATOR.join(str(value) for value in values)


def lakiaro_text(collect_rate: Mapping[str, int], depth_format: str) -> str:
    """`Lakiaro (27621), depth 1` for one Lakiaro row."""
    key = collect_rate["character_key"]
    name = character_name(key) or str(key)
    return depth_format.format(name=name, key=key, depth=collect_rate["depth"])


class MiniGameFindBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["gameType"], "num", sort_key="game_type"),
            Column(labels["nextGame"], "num", sort_key="next_game"),
            Column(labels["minDamageRate"], "num", sort_key="min_damage_rate"),
            Column(labels["nextRate"], "num", sort_key="next_rate"),
            Column(labels["lifeType"], "num", sort_key="life_type"),
            Column(labels["lifeRate"], "num", sort_key="life_rate"),
            # List columns would only sort by their string form.
            Column(labels["tools"]),
            Column(labels["toolRate"], "num", sort_key="tool_rate"),
            Column(labels["stoneRate"], "num", sort_key="stone_rate"),
            Column(labels["stoneDrop"]),
            Column(labels["grid"], sort_key="col"),
            Column(labels["startPos"]),
            Column(labels["minRootCount"]),
            Column(labels["beginRootCount"]),
            Column(labels["useSlots"]),
            Column(labels["rewards"]),
            Column(labels["lakiaros"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        tables = parse_minigamefind(data)
        strings = self._strings()
        side_labels = [strings["sides"][key] for key in _SIDE_LABEL_KEYS]
        return [
            _type_fields(
                record,
                [rate for rate in tables.collect_rates if rate["main_game_type"] == record["game_type"]],
                strings["lakiaro"]["depth"],
                side_labels,
            )
            for record in tables.types
        ]

    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def cells(self, record: dict) -> list[str]:
        next_game = record["next_game"]
        return [
            e(record["game_type"]),
            e(next_game) if next_game is not None else _EMPTY,
            e(f"{record['min_damage_rate']:,}"),
            e(f"{record['next_rate']:,}"),
            e(record["life_type"]),
            e(f"{record['life_rate']:,}"),
            item_key_list_cell(_present(record["tool_item_keys"]), _LIST_PREVIEW_ITEMS) or _EMPTY,
            e(f"{record['tool_rate']:,}"),
            e(f"{record['stone_rate']:,}"),
            item_key_list_cell(_present([record["stone_drop_item_key"]]), 1) or _EMPTY,
            e(record["grid"]),
            e(_numbers_text(record["start_pos"])),
            e(_numbers_text(record["min_root_count"])),
            e(record["begin_root_text"]),
            e(_numbers_text(_present(record["use_slot_indexes"]))),
            item_key_list_cell(_present(record["reward_item_keys"]), _LIST_PREVIEW_ITEMS) or _EMPTY,
            text_list_cell(record["lakiaro_names"], _LIST_PREVIEW_ITEMS) or _EMPTY,
        ]


def _type_fields(
    record: dict,
    collect_rates: list[dict],
    depth_format: str,
    side_labels: Sequence[str],
) -> dict:
    begin_root_text = _NUMBER_SEPARATOR.join(
        f"{label} {count}" for label, count in zip(side_labels, record["begin_root_count"], strict=True)
    )
    return {
        **record,
        "grid": f"{record['col']} x {record['row']}",
        "begin_root_text": begin_root_text,
        # Item and character names as text, so tab search and CSV export see them.
        "tool_names": [item_key_text(key) for key in _present(record["tool_item_keys"])],
        "stone_drop_name": item_key_text(record["stone_drop_item_key"]) if record["stone_drop_item_key"] else "",
        "reward_names": [item_key_text(key) for key in _present(record["reward_item_keys"])],
        "lakiaros": collect_rates,
        "lakiaro_names": [lakiaro_text(rate, depth_format) for rate in collect_rates],
    }
