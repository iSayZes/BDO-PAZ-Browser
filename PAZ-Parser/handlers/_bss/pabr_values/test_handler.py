from __future__ import annotations

import json
import math
import struct
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _common.pa_text import pa_key
from _dbss.cashproduct.parser import parse_cashproductoffset_records
from _dbss.pet.parser import parse_pet_records
from .handler import VALUE_BYTES_FIELD, PabrValuesBssHandler
from .names import ELEMENT_TYPE_NAMES, aura_name, utc_time
from .parser import PABR_VALUES_START, parse_value_table, row_value_bytes
from .tables import VALUE_TABLES, Framing, NameLookup, RowCount, ValueField, ValueTable


_U32 = struct.Struct("<I")
_TABLE_START_AT = -8
_ROW_SIZE_TO_TABLE_START = 4
_TABLES = {value_table.file_name: value_table for value_table in VALUE_TABLES}
_NEWBIE_PRODUCT = "cashproduct_newbieproduct.bss"
_ELEMENTAL_STAT = "elementalstat.bss"
_PET_LEADER_BUFF = "petleaderbuff.bss"
_SOLARE_ETC_OPTION = "solareetcoptionstaticstatus.bss"
_BARTER_RESET = "barterresetoption.bss"
# Stored pet tier of Tier 5, the tier an alpha pet has (petleaderbuff_bss.md).
_TIER_5 = 4
# A cooldown cut on the 1,000,000 = 100% scale.
_FULL_RATE = 1_000_000
_ARCHAEOLOGISTS_MAP = 16019
_ELEMENTAL_SERVER_BUFF = "elementalserverbuff.bss"
_OLVIA_SEASON = "olviaacademyseasonss.bss"
_PET_UPGRADE = "petupgrade.bss"
# Stored pet tier of Tier 4, the tier that trains into Tier 5 (petupgrade_bss.md).
_TIER_4 = 3
_ROYAL_PLUME = 59376
# Packed quest IDs (quest_id << 16 | quest_chain_id) of 2308/1 and 2309/1.
_FIRST_STEPS_IN = 1 << 16 | 2308
_GRADUATION_WITH_HONOR = 1 << 16 | 2309
_EN_LANG = Path(__file__).parent / "lang" / "en.json"


def _values_start(value_table: ValueTable) -> int:
    return PABR_VALUES_START if value_table.framing is Framing.PABR else 0


def _rows_to_table_start(source: CaseInput) -> int:
    """The 4-byte rows between the magic and the trailer's `table_start`."""
    (table_start,) = _U32.unpack_from(source.data, _TABLE_START_AT)
    return (table_start - PABR_VALUES_START) // _ROW_SIZE_TO_TABLE_START


def _lookups(name: str) -> list[NameLookup]:
    return [field.lookup for field in _TABLES[name].fields if field.lookup is not None]


def _lookup_fields(name: str) -> list[str]:
    return [lookup.field for lookup in _lookups(name)]


def _required_keys(value_table: ValueTable) -> list[str]:
    name = value_table.file_name
    keys = [field.name for field in value_table.fields] + _lookup_fields(name)
    keys += [pa_key(lookup.field) for lookup in _lookups(name) if lookup.is_tagged]
    keys += [field.icon.field for field in value_table.fields if field.icon is not None]
    if not value_table.has_named_field:
        keys.append(VALUE_BYTES_FIELD)
    return keys


def _count_tests(value_table: ValueTable) -> list[Any]:
    if value_table.rows is RowCount.COUNTED:
        return [DeclaredCountTest(declared=header_count(offset=_values_start(value_table)))]
    if value_table.rows is RowCount.TO_TABLE_START:
        return [DeclaredCountTest(declared=_rows_to_table_start)]
    return [DeclaredCountTest(declared=lambda _source: 1)]


# Identity anchors: keys and the LOC names they resolve to.
_TARGETS: dict[str, list[TargetTest]] = {
    _ELEMENTAL_STAT: [
        TargetTest(col="element_type", value=0, expected={"aura": "Sun Aura"}),
        TargetTest(col="element_type", value=1, expected={"aura": "Moon Aura"}),
        TargetTest(col="element_type", value=2, expected={"aura": "Earth Aura"}),
    ],
    "interaction.bss": [
        # InteractionType_Awake (CppEnums.InteractionType 61) on both Offin characters.
        TargetTest(col="character_key", value=23751, expected={"interaction_type": 61, "character_name": "Mirumok Watcher Offin"}),
        TargetTest(col="character_key", value=23767, expected={"interaction_type": 61, "character_name": "Mirumok Destroyer Offin"}),
    ],
    "othertownnotmovableitem.bss": [
        TargetTest(col="item_id", value=_ARCHAEOLOGISTS_MAP, expected={"item_name": "Archaeologist's Map"}),
    ],
    _PET_LEADER_BUFF: [TargetTest(col="pet_tier", value=_TIER_5, expected={"pet_tier": _TIER_5})],
    "servantchecktitle.bss": [
        TargetTest(
            col="title_id",
            value=2705,
            expected={"title_name": "Captain Epheria", "character_key": 31020, "character_name": "Epheria Galleon"},
        ),
    ],
    "timeattackranking.bss": [
        TargetTest(col="character_key", value=23751, expected={"character_name": "Mirumok Watcher Offin"}),
        TargetTest(col="character_key", value=24385, expected={"character_name": "Transcended Kzarka"}),
    ],
    "vehicletrainingskill.bss": [
        TargetTest(col="skill_key", value=49, expected={"skill_name": "Skill"}),
        TargetTest(col="skill_key", value=50, expected={"skill_name": "Elegance"}),
        TargetTest(col="skill_key", value=51, expected={"skill_name": "Strength"}),
    ],
    "voxelregionskillstaticstatusmanager.bss": [
        # skill_no 42501 and 42502, level 1.
        TargetTest(col="skill_key", value=0xA6050001, expected={"skill_name": "All-Consuming Heat"}),
        TargetTest(col="skill_key", value=0xA6060001, expected={"skill_name": "Dead Soul's Chill"}),
    ],
    _OLVIA_SEASON: [
        TargetTest(
            col="enter_quest",
            value=_FIRST_STEPS_IN,
            expected={
                "enter_quest_title": "[Olvia Academy] Your First Steps In",
                "graduation_quest": _GRADUATION_WITH_HONOR,
                "graduation_quest_title": "[Olvia Academy] Graduation with Honor",
            },
        ),
    ],
    _PET_UPGRADE: [
        TargetTest(col="pet_tier", value=_TIER_4, expected={"item_id": _ROYAL_PLUME, "item_name": "Royal Plume"}),
    ],
}

_RANGES: dict[str, list[RangeTest]] = {
    # __eElementalStat_Sun, _Moon, _Land.
    _ELEMENTAL_STAT: [RangeTest(col="element_type", min_val=0, max_val=len(ELEMENT_TYPE_NAMES) - 1)],
    _PET_LEADER_BUFF: [RangeTest(col="leader_buff_rate", min_val=0, max_val=_FULL_RATE)],
    _ELEMENTAL_SERVER_BUFF: [RangeTest(col="earth_blessing_drop_rate", min_val=0, max_val=_FULL_RATE)],
}


def _case(value_table: ValueTable) -> HandlerCase:
    name = value_table.file_name
    lookup_fields = _lookup_fields(name)
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc" if lookup_fields else None,
        uses_loc=bool(lookup_fields),
        loc_fields=lookup_fields,
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=_required_keys(value_table)),
            *_count_tests(value_table),
            *_RANGES.get(name, []),
            *_TARGETS.get(name, []),
        ],
    )


CASES = {value_table.file_name: _case(value_table) for value_table in VALUE_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


def _render(name: str, records: list[dict]) -> str:
    handler = PabrValuesBssHandler(_TABLES[name])
    handler.lang = "en"
    return handler.render_records_page(records, 0, len(records))


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_pabr_values(name: str, spec: Any) -> None:
    _result(name).check(spec)


@pytest.mark.parametrize("name", [name for name in _TABLES if _lookup_fields(name)])
def test_every_key_has_a_loc_name(name: str) -> None:
    for record in _result(name).records:
        for field in _lookup_fields(name):
            assert record[field], f"{name}: no LOC name for {record}"


def test_every_table_has_its_labels() -> None:
    strings = json.loads(_EN_LANG.read_text(encoding="utf-8"))
    for value_table in VALUE_TABLES:
        assert value_table.count_key in strings["meta"], value_table.file_name
        for field in value_table.fields:
            columns = [field.column, *(lookup.column for lookup in (field.lookup, field.icon) if lookup is not None)]
            assert all(column in strings["columns"] for column in columns if column is not None), field.name


def test_the_newbie_product_is_a_cash_product() -> None:
    (record,) = _result(_NEWBIE_PRODUCT).records
    product_ids = {row["product_id"] for row in parse_cashproductoffset_records(load_binary_fixture("cashproductoffset.dbss"))}
    assert record["product_id"] in product_ids


def test_cultivation_event_types_are_unique() -> None:
    types = [record["cultivation_event_type"] for record in _result("cultivationevent.bss").records]
    assert len(types) == len(set(types))


def test_each_aura_row_repeats_its_key() -> None:
    for record in _result(_ELEMENTAL_STAT).records:
        assert record["element_type_dup"] == record["element_type"]


def test_each_aura_has_one_row() -> None:
    types = [record["element_type"] for record in _result(_ELEMENTAL_STAT).records]
    assert len(types) == len(set(types))


def test_an_aura_type_outside_the_enum_shows_its_value() -> None:
    assert aura_name(7) == "7"


def test_every_pet_tier_is_a_pet_dbss_tier() -> None:
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    pet_tiers = {pet["tier"] for pet in pets}
    assert {record["pet_tier"] for record in _result(_PET_LEADER_BUFF).records} <= pet_tiers


def test_the_loot_cooldown_shows_as_a_cut() -> None:
    record = {"pet_tier": _TIER_5, "unknown_01": _TIER_5, "leader_buff_rate": 150_000}
    assert '<td class="num">-15%</td>' in _render(_PET_LEADER_BUFF, [record])


def test_solare_values_are_finite_floats() -> None:
    (record,) = _result(_SOLARE_ETC_OPTION).records
    floats = [value for key, value in record.items() if key.startswith("unknown_")]
    assert floats and all(isinstance(value, float) and math.isfinite(value) for value in floats)


def test_solare_value_bytes_hold_the_whole_file() -> None:
    (record,) = _result(_SOLARE_ETC_OPTION).records
    assert bytes.fromhex(record[VALUE_BYTES_FIELD]) == _result(_SOLARE_ETC_OPTION).source.data


def test_each_barter_list_holds_its_count() -> None:
    (record,) = _result(_BARTER_RESET).records
    data = _result(_BARTER_RESET).source.data
    general_count = _U32.unpack_from(data, PABR_VALUES_START)[0]
    material_at = PABR_VALUES_START + _U32.size * (1 + general_count)
    assert len(record["general_barter"]) == general_count
    assert len(record["material_barter"]) == _U32.unpack_from(data, material_at)[0]


def test_a_barter_list_shows_its_values_in_order() -> None:
    record = {"general_barter": [20, 40, 50], "material_barter": []}
    html = _render(_BARTER_RESET, [record])
    assert '<td class="num">20, 40, 50</td>' in html
    assert '<td class="num">-</td>' in html


def test_the_academy_class_title_names_its_class() -> None:
    (record,) = _result(_OLVIA_SEASON).records
    assert record["title_name"] == f"Olvia Academy Class {record['season_no']}"


def test_enrollment_closes_before_graduation_opens() -> None:
    (record,) = _result(_OLVIA_SEASON).records
    assert record["start_time"] <= record["close_time"] < record["graduation_time"] <= record["end_time"]


def test_the_academy_cells_show_dates_and_quest_ids() -> None:
    record = {
        "season_no": 3,
        "start_time": 1_785_402_000,
        "graduation_time": 0,
        "close_time": 0,
        "end_time": 1_794_474_000,
        "enter_quest": _FIRST_STEPS_IN,
        "graduation_quest": _GRADUATION_WITH_HONOR,
        "title_id": 3687,
        "enter_quest_title": "",
        "graduation_quest_title": "",
        "title_name": "",
    }
    html = _render(_OLVIA_SEASON, [record])
    assert '<td class="num">2026-07-30 09:00 UTC</td>' in html
    assert '<td class="num">2026-11-12 09:00 UTC</td>' in html
    assert '<td class="num">2308/1</td>' in html
    assert '<td class="num">2309/1</td>' in html


@pytest.mark.parametrize(
    ("seconds", "text"),
    [
        (0, "1970-01-01 00:00 UTC"),
        (951_782_400, "2000-02-29 00:00 UTC"),
        (1_709_251_199, "2024-02-29 23:59 UTC"),
        (4_102_444_800, "2100-01-01 00:00 UTC"),
    ],
)
def test_unix_seconds_read_as_utc_dates(seconds: int, text: str) -> None:
    assert utc_time(seconds) == text


def test_each_pet_upgrade_row_repeats_its_tier() -> None:
    for record in _result(_PET_UPGRADE).records:
        assert record["pet_tier_dup"] == record["pet_tier"]


def test_every_pet_upgrade_tier_is_a_pet_dbss_tier() -> None:
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    pet_tiers = {pet["tier"] for pet in pets}
    assert {record["pet_tier"] for record in _result(_PET_UPGRADE).records} <= pet_tiers


def test_each_blessing_row_repeats_its_key() -> None:
    records = _result(_ELEMENTAL_SERVER_BUFF).records
    assert all(record["unknown_01"] == record["unknown_00"] for record in records)
    assert len({record["unknown_00"] for record in records}) == len(records)


def test_the_blessing_cells_show_a_bonus_and_a_duration() -> None:
    record = {
        "unknown_00": 9,
        "unknown_01": 9,
        "sun_blessing_ap": 1.0,
        "moon_blessing_dp": 1.0,
        "earth_blessing_drop_rate": 200_000,
        "buff_duration": 10_800,
        "unknown_12": 0,
    }
    html = _render(_ELEMENTAL_SERVER_BUFF, [record])
    assert '<td class="num">+20%</td>' in html
    assert '<td class="num">3h</td>' in html
    assert '<td class="num">1</td>' in html


# Synthetic files: PABR, the values, an empty string table and the trailer.
def _pabr(values: bytes) -> bytes:
    table_start = PABR_VALUES_START + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


_ONE = ValueTable("one.bss", (ValueField("a", "I", "productId"), ValueField("unknown_04", "2s")))
_COUNTED = ValueTable("counted.bss", (ValueField("key", "B", "skillId"),), RowCount.COUNTED)
_COUNTED_PAIRS = ValueTable("pairs.bss", (ValueField("unknown_00", "B"), ValueField("unknown_01", "B")), RowCount.COUNTED)
_ROWS = ValueTable("rows.bss", (ValueField("a", "H", "regionKey"), ValueField("b", "H")), RowCount.TO_TABLE_START)
_LISTS = ValueTable(
    "lists.bss",
    (ValueField("a", "I", "generalBarter", is_counted_list=True), ValueField("b", "I", "materialBarter", is_counted_list=True)),
)
_BARE_ONE = ValueTable("bare.bss", (ValueField("a", "Q", "statResetCost"), ValueField("unknown_08", "B")), framing=Framing.BARE)
_BARE_COUNTED = ValueTable(
    "bare_counted.bss",
    (ValueField("key", "B", "elementType"), ValueField("value", "I", "apPerOrb")),
    RowCount.COUNTED,
    Framing.BARE,
)


def test_one_value_set_reads_one_record_with_hex_bytes() -> None:
    data = _pabr(_U32.pack(7) + b"\x01\x0a")
    assert parse_value_table(data, _ONE) == [{"a": 7, "unknown_04": "01 0a"}]


def test_a_counted_list_reads_one_record_per_entry() -> None:
    data = _pabr(_U32.pack(3) + bytes([49, 50, 51]))
    assert parse_value_table(data, _COUNTED) == [{"key": 49}, {"key": 50}, {"key": 51}]


def test_row_value_bytes_split_a_counted_list_into_rows() -> None:
    data = _pabr(_U32.pack(2) + bytes([1, 2, 3, 4]))
    assert row_value_bytes(data, _COUNTED_PAIRS) == ["01 02", "03 04"]


def test_row_value_bytes_of_one_value_set_hold_every_value_byte() -> None:
    data = _pabr(_U32.pack(7) + bytes([1, 10]))
    assert row_value_bytes(data, _ONE) == ["07 00 00 00 01 0a"]


def test_rows_run_up_to_the_string_table() -> None:
    data = _pabr(struct.pack("<HHHH", 1176, 1, 1484, 2))
    assert parse_value_table(data, _ROWS) == [{"a": 1176, "b": 1}, {"a": 1484, "b": 2}]


def test_counted_list_fields_read_one_after_the_other() -> None:
    data = _pabr(struct.pack("<IIII", 2, 20, 40, 1) + _U32.pack(10))
    assert parse_value_table(data, _LISTS) == [{"a": [20, 40], "b": [10]}]


def test_a_bare_file_is_the_values_alone() -> None:
    assert parse_value_table(struct.pack("<QB", 1 << 40, 5), _BARE_ONE) == [{"a": 1 << 40, "unknown_08": 5}]


def test_a_bare_count_opens_the_file() -> None:
    data = _U32.pack(2) + struct.pack("<BIBI", 1, 50, 0, 7)
    assert parse_value_table(data, _BARE_COUNTED) == [{"key": 1, "value": 50}, {"key": 0, "value": 7}]


def test_a_count_past_the_string_table_raises() -> None:
    data = _pabr(_U32.pack(4) + bytes([49, 50, 51]))
    with pytest.raises(ValueError, match="string table starts"):
        parse_value_table(data, _COUNTED)


def test_a_list_count_past_the_string_table_raises() -> None:
    data = _pabr(struct.pack("<III", 3, 20, 40))
    with pytest.raises(ValueError, match="a count 3 runs past"):
        parse_value_table(data, _LISTS)


def test_values_that_stop_short_of_the_string_table_raise() -> None:
    data = _pabr(_U32.pack(7) + b"\x01\x0a\x00")
    with pytest.raises(ValueError, match="string table starts"):
        parse_value_table(data, _ONE)


def test_rows_that_split_at_the_string_table_raise() -> None:
    data = _pabr(struct.pack("<HHH", 1176, 1, 1484))
    with pytest.raises(ValueError, match="not whole 4-byte rows"):
        parse_value_table(data, _ROWS)


def test_a_bad_magic_raises() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_value_table(b"XXXX" + _pabr(_U32.pack(7) + b"\x01\x0a")[4:], _ONE)


@pytest.mark.parametrize("size", [8, 10, 0])
def test_a_bare_file_of_another_size_raises(size: int) -> None:
    with pytest.raises(ValueError, match="the file ends"):
        parse_value_table(bytes(size), _BARE_ONE)


@pytest.mark.parametrize(
    "data",
    [b"\x01\x00", _U32.pack(1) + bytes(4), _U32.pack(1) + bytes(6), _U32.pack(2) + bytes(5)],
    ids=["short_count", "short_row", "extra_bytes", "missing_row"],
)
def test_a_bare_count_that_does_not_fill_the_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError, match="the file ends"):
        parse_value_table(data, _BARE_COUNTED)


def test_rows_up_to_the_string_table_take_no_counted_list() -> None:
    with pytest.raises(ValueError, match="fixed row size"):
        ValueTable("bad.bss", (ValueField("a", "I", "productId", is_counted_list=True),), RowCount.TO_TABLE_START)


def test_a_counted_list_takes_no_lookup() -> None:
    with pytest.raises(ValueError, match="no name or icon lookup"):
        ValueField("a", "I", "skillId", NameLookup("name", "skill", str), is_counted_list=True)
