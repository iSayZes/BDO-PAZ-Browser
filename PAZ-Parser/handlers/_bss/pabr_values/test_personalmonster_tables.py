"""Checks of the Dark Rift table in `personalmonster_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from _dbss.personalmonster.parser import FILE_NAME as PERSONAL_MONSTER_FILE, parse_personalmonster_records
from .handler import PabrValuesBssHandler
from .parser import parse_value_table
from .personalmonster_names import icon_region_text, icon_size_text
from .personalmonster_tables import DIFFICULTY_COUNT, ICON_SIZE_VALUES, LEVEL_COUNT, PERSONAL_MONSTER_TABLES


(_TABLE,) = PERSONAL_MONSTER_TABLES
_REGION_FIELDS = ("difficulty_icon_uvs", "level_icon_uvs")
# The first difficulty `personalmonster.dbss` stores (Normal); the regions count from it.
_FIRST_DIFFICULTY = 1


def _record() -> dict:
    (record,) = parse_value_table(load_binary_fixture(_TABLE.file_name), _TABLE)
    return record


def test_each_list_holds_its_sheet_columns() -> None:
    record = _record()
    assert len(record["icon_size"]) == ICON_SIZE_VALUES
    assert len(record["difficulty_icon_uvs"]) == DIFFICULTY_COUNT
    assert len(record["level_icon_uvs"]) == LEVEL_COUNT


def test_every_icon_region_is_one_icon_size() -> None:
    # Each region cuts one icon of `icon_size` out of the sheet (personalmonsteretc_bss.md, Icon Regions).
    record = _record()
    width, height = record["icon_size"]
    for field in _REGION_FIELDS:
        for x1, y1, x2, y2 in record[field]:
            assert (x2 - x1, y2 - y1) == (width, height), (field, x1, y1, x2, y2)


def test_every_icon_region_is_its_own() -> None:
    record = _record()
    regions = [tuple(region) for field in _REGION_FIELDS for region in record[field]]
    assert len(regions) == len(set(regions))


def test_every_boss_difficulty_has_an_icon_region() -> None:
    bosses = parse_personalmonster_records(load_binary_fixture(PERSONAL_MONSTER_FILE))
    assert bosses
    assert {boss["difficulty"] for boss in bosses} <= set(range(_FIRST_DIFFICULTY, _FIRST_DIFFICULTY + DIFFICULTY_COUNT))


def test_the_size_and_regions_show_as_pixels() -> None:
    assert icon_size_text([119.0, 119.0]) == "119 x 119"
    assert icon_region_text([1.0, 121.0, 120.0, 240.0]) == "1, 121, 120, 240"
    assert icon_region_text([0.5, 1.0, 2.0, 3.0]) == "0.5, 1, 2, 3"


def test_each_region_draws_on_its_own_line() -> None:
    handler = PabrValuesBssHandler(_TABLE)
    handler.lang = "en"
    record = _record()
    html = handler.render_records_page([record], 0, 1)
    assert icon_size_text(record["icon_size"]) in html
    for region in record["difficulty_icon_uvs"] + record["level_icon_uvs"]:
        assert icon_region_text(region) in html
