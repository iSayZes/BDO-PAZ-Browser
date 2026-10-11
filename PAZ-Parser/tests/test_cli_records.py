"""`--records`: filters, field selection and the three output formats."""
from __future__ import annotations

import json

import pytest

from cli.errors import CliError
from cli.record_filter import Op, filter_records, parse_condition
from cli.record_output import OutputFormat, format_records, format_table, record_fields
from cli.records import parse_fields, parse_sort, select_records
from cli.values import display_text, parse_int
from record_export import csv_export_name, records_to_csv
from table_sort import TableSort

_RECORDS = [
    {
        "id": 1, "name": "Adventure's Boon", "shown": True, "buffs": (10, 11), "ratio": 0.5,
        "note": None, "path": "a.dds", "text": "line\nline",
    },
    {
        "id": 2, "name": "Guild Buff", "shown": False, "buffs": (), "ratio": 1.5,
        "note": "x", "path": "", "text": "line\\nline",
    },
    {
        "id": 0x20, "name": "고양이", "shown": False, "buffs": (11,), "ratio": 2.0,
        "note": None, "path": "  ", "text": "",
    },
]


def _ids(conditions: list[str]) -> list[int]:
    return [r["id"] for r in filter_records(_RECORDS, [parse_condition(c) for c in conditions])]


# ── Conditions ───────────────────────────────────────────────────────────────

@pytest.mark.parametrize(
    ("condition", "expected"),
    [
        ("id=2", [2]),
        ("id=0x20", [0x20]),
        ("name=guild buff", [2]),
        ("name*=BOON", [1]),
        ("shown=yes", [1]),
        ("shown=false", [2, 0x20]),
        ("buffs=11", [1, 0x20]),
        ("note=none", [1, 0x20]),
        ("note=", [1, 0x20]),
        # An empty list or blank text is as empty as None.
        ("buffs=none", [2]),
        ("path=none", [2, 0x20]),
        ("path=", [2, 0x20]),
        # None is not searched as its dash.
        ("note*=-", []),
        # Text is searched as stored, so the two-character escape does not
        # match a real newline.
        ("text*=\\n", [2]),
        ("ratio=1.5", [2]),
        ("id=2..32", [2, 0x20]),
        ("id=..1", [1]),
        ("ratio=1..", [2, 0x20]),
        ("buffs=11..11", [1, 0x20]),
        ("name=1..2", []),
    ],
)
def test_condition_matches(condition: str, expected: list[int]) -> None:
    assert _ids([condition]) == expected


def test_conditions_combine_with_and() -> None:
    assert _ids(["shown=false", "buffs=11"]) == [0x20]


def test_parse_condition_reads_the_operator() -> None:
    assert parse_condition("id=1..").op is Op.RANGE
    assert parse_condition("id=1").op is Op.EQUALS
    assert parse_condition("name*=a=b").op is Op.CONTAINS
    assert parse_condition("name*=a=b").text == "a=b"


@pytest.mark.parametrize("text", ["=1", "no operator", "id=a..b", "id=.."])
def test_parse_condition_rejects_malformed(text: str) -> None:
    with pytest.raises(CliError):
        parse_condition(text)


# ── Selection ────────────────────────────────────────────────────────────────

def test_select_filters_then_limits_then_projects() -> None:
    selection = select_records(_RECORDS, [parse_condition("shown=false")], ["name", "id"], limit=1)

    assert selection.records == [{"name": "Guild Buff", "id": 2}]
    assert selection.matched == 2
    assert selection.total == len(_RECORDS)


def test_select_rejects_unknown_fields() -> None:
    with pytest.raises(CliError, match="bogus"):
        select_records(_RECORDS, [parse_condition("bogus=1")], [], None)
    with pytest.raises(CliError, match="bogus"):
        select_records(_RECORDS, [], ["id", "bogus"], None)


def test_select_sorts_before_the_limit() -> None:
    """--limit takes the top of the sorted rows, as the GUI's first page would."""
    selection = select_records(_RECORDS, [], ["id"], limit=2, sort=parse_sort("ratio:desc"))

    assert selection.records == [{"id": 0x20}, {"id": 2}]


def test_select_sort_puts_empty_values_last_both_ways() -> None:
    for text in ("note", "note:desc"):
        ids = [r["id"] for r in select_records(_RECORDS, [], ["id"], None, parse_sort(text)).records]
        assert ids[0] == 2, text  # the only record with a note; equal empties keep file order


def test_select_rejects_an_unknown_sort_field() -> None:
    with pytest.raises(CliError, match="bogus"):
        select_records(_RECORDS, [], [], None, parse_sort("bogus"))


def test_parse_sort() -> None:
    assert parse_sort(None) is None
    assert parse_sort("id") == TableSort("id", "asc")
    assert parse_sort(" id:DESC ") == TableSort("id", "desc")
    with pytest.raises(CliError):
        parse_sort("id:sideways")
    with pytest.raises(CliError):
        parse_sort(":desc")


def test_select_accepts_any_field_on_no_records() -> None:
    assert select_records([], [parse_condition("bogus=1")], ["x"], None).records == []


def test_parse_fields() -> None:
    assert parse_fields(" a, b ,c") == ["a", "b", "c"]
    assert parse_fields(None) == []
    with pytest.raises(CliError):
        parse_fields(" , ")


# ── Output ───────────────────────────────────────────────────────────────────

def test_record_fields_keep_first_seen_order() -> None:
    assert record_fields([{"b": 1, "a": 2}, {"c": 3, "a": 4}]) == ["b", "a", "c"]


def test_table_aligns_wide_characters_and_right_aligns_numbers() -> None:
    lines = format_table([{"id": 5, "name": "고양이"}, {"id": 123, "name": "cat"}]).splitlines()

    assert lines[0].split() == ["id", "name"]
    # "고양이" takes six terminal columns, so the name column is six wide.
    assert lines[1] == "---  ------"
    assert lines[2] == "  5  고양이"
    assert lines[3] == "123  cat"


def test_table_cuts_long_cells_in_the_middle() -> None:
    """Both ends stay, so an icon path keeps its file name."""
    path = "ui_texture/icon/new_icon/04_pc_skill/03_buff/silverbless.dds"
    table = format_table([{"icon_path": path}, {"icon_path": "-"}], max_width=20)

    assert "ui_texture…bless.dds" in table
    assert path not in table


def test_table_cut_keeps_wide_characters_whole() -> None:
    table = format_table([{"name": "고양이고양이고양이"}, {"name": "-"}], max_width=9)

    # Four columns each side of the ellipsis, two characters of two columns.
    assert "고양…양이" in table


def test_single_row_is_shown_whole() -> None:
    path = "ui_texture/icon/new_icon/04_pc_skill/03_buff/silverbless.dds"

    assert path in format_records([{"id": 48724, "value": path}], OutputFormat.TABLE)


def test_display_text_flattens_values() -> None:
    assert display_text(None) == "-"
    assert display_text((1, 2)) == "1, 2"
    assert display_text("a\nb") == "a\\nb"
    assert display_text(b"\x01\xff") == "01 ff"


def test_json_keeps_full_values() -> None:
    long_text = "y" * 500
    parsed = json.loads(format_records([{"ids": (1, 2), "text": long_text, "kr": "고양이"}], OutputFormat.JSON))

    assert parsed == [{"ids": [1, 2], "text": long_text, "kr": "고양이"}]


def test_csv_matches_the_app_export() -> None:
    records = [{"id": 1, "name": "a,b"}]

    assert format_records(records, OutputFormat.CSV) == records_to_csv(records)
    assert records_to_csv(records) == 'id,name\r\n1,"a,b"\r\n'
    assert records_to_csv([]) == ""


def test_the_csv_export_name_holds_the_client_and_handler_versions() -> None:
    assert csv_export_name("buffsimply.bss", 3464, "2026.10.12") == "buffsimply_3464_2026.10.12.csv"
    assert csv_export_name("languagedata_en.loc", 3464, "0d44990+") == "languagedata_en_3464_0d44990+.csv"


def test_the_csv_export_name_leaves_out_unknown_versions() -> None:
    assert csv_export_name("buffsimply.bss", None, None) == "buffsimply.csv"
    assert csv_export_name("buffsimply.bss", 3464, None) == "buffsimply_3464.csv"


def test_parse_int_reads_hex_and_decimal() -> None:
    assert parse_int("0x1F") == 31
    assert parse_int("-12") == -12
    assert parse_int("010") == 10
    with pytest.raises(ValueError):
        parse_int("1.5")
