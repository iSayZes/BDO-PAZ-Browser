from __future__ import annotations

from pathlib import Path

import pytest

from format_docs import check_doc, converted_docs
from format_docs.markdown import split_row
from format_docs.model import Field
from format_docs.names import name_problems
from format_docs.type_grammar import fixed_part, fixed_size, parse_type

DOCS_DIR = Path(__file__).resolve().parents[2] / "docs" / "file-formats"
VERSIONS = (
    "## Versions\n\n"
    "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->\n\n"
    "<!-- versions:end -->\n"
)
FILE_LAYOUT = (
    "### File Layout\n\n"
    "| Offset  | Type           | Field     | Notes |\n"
    "| ------- | -------------- | --------- | ----- |\n"
    "| `+0x00` | u32            | row_count |       |\n"
    "| `+0x04` | Row[row_count] | rows      |       |\n"
)


def _doc(*structures: str, layouts: str | None = None, extra: str = "") -> str:
    """A doc with Purpose, Versions and one layout made of `structures`."""
    body = layouts if layouts is not None else "## Layout 1\n\n" + "\n".join(structures)
    return f"# `test.bss` Format\n\n## Purpose\n\nRows.\n\n{VERSIONS}\n{body}\n{extra}"


def _structure(heading: str, *rows: tuple[str, str, str]) -> str:
    lines = [f"### {heading}", "", "| Offset | Type | Field | Notes |", "| --- | --- | --- | --- |"]
    lines += [f"| `{offset}` | {type_text} | {name} |  |" for offset, type_text, name in rows]
    return "\n".join(lines) + "\n"


def _messages(text: str) -> list[str]:
    return [problem.message for problem in check_doc(text)]


ROW = _structure("Row (8 bytes)", ("+0x00", "u32", "key"), ("+0x04", "u32", "unknown_04"))


def test_a_doc_in_the_layout_format_has_no_problems() -> None:
    assert _messages(_doc(FILE_LAYOUT, ROW)) == []


def test_the_repo_has_converted_docs() -> None:
    assert converted_docs(DOCS_DIR)


@pytest.mark.parametrize("path", converted_docs(DOCS_DIR), ids=lambda path: path.name)
def test_every_converted_doc_passes(path: Path) -> None:
    assert [str(problem) for problem in check_doc(path.read_text(encoding="utf-8"))] == []


def test_a_fixed_size_must_equal_the_sum_of_the_fields() -> None:
    row = _structure("Row (12 bytes)", ("+0x00", "u32", "key"), ("+0x04", "u32", "unknown_04"))

    assert _messages(_doc(FILE_LAYOUT, row)) == ["`Row` states 12 bytes, its fields add up to 8"]


def test_a_gap_between_offsets_names_the_expected_offset() -> None:
    row = _structure("Row (8 bytes)", ("+0x00", "u32", "key"), ("+0x08", "u32", "unknown_08"))

    assert "offset should be `+0x04`" in _messages(_doc(FILE_LAYOUT, row))


def test_offsets_after_a_string_count_from_the_string() -> None:
    good = _structure("Row (variable: 16 bytes + name)", ("+0x00", "u32", "key"), ("+0x04", "str16", "name_kr"), ("name_kr+0x00", "u32", "item_id"))
    bad = _structure("Row (variable: 16 bytes + name)", ("+0x00", "u32", "key"), ("+0x04", "str16", "name_kr"), ("+0x0C", "u32", "item_id"))

    assert _messages(_doc(FILE_LAYOUT, good)) == []
    assert "offset should be `name_kr+0x00`" in _messages(_doc(FILE_LAYOUT, bad))


def test_a_variable_heading_states_the_fixed_part() -> None:
    row = _structure("Row (variable: 4 bytes + name)", ("+0x00", "u32", "key"), ("+0x04", "str16", "name_kr"))

    assert _messages(_doc(FILE_LAYOUT, row)) == ["`Row` states a fixed part of 4 bytes, its fields give 12"]


def test_types_outside_the_grammar_are_reported() -> None:
    row = _structure("Row (8 bytes)", ("+0x00", "u32", "key"), ("+0x04", "row[]", "unknown_04"))

    assert "`row[]` is not a type" in _messages(_doc(FILE_LAYOUT, row))


def test_a_structure_type_needs_its_heading() -> None:
    assert _messages(_doc(FILE_LAYOUT)) == ["`Row` has no `### Row (...)` heading in this layout or a newer one"]


def test_a_count_reads_an_earlier_field() -> None:
    row = _structure("Row (variable: 0 bytes + list)", ("+0x00", "u32[later]", "values"), ("values+0x00", "u32", "later"))

    assert "`later` is not an earlier field of `Row`" in _messages(_doc(FILE_LAYOUT, row))


def test_a_size_condition_needs_a_size_from_an_offset_file() -> None:
    plain = _structure("Row (variable: 4 bytes + tail)", ("+0x00", "u32", "key"), ("+0x04", "u8 if size = 5", "unknown_04"))
    sized = plain.replace("(variable: 4 bytes + tail)", "(variable: 4 bytes, size from `testoffset.dbss`)")

    assert "`size` and `[rest]` need `size from <offset file>` in the heading" in _messages(_doc(FILE_LAYOUT, plain))
    assert _messages(_doc(FILE_LAYOUT, sized)) == []


def test_offsets_from_the_end_must_meet_at_the_end() -> None:
    good = _structure(
        "Row (variable: 8 bytes, size from `testoffset.dbss`)",
        ("+0x00", "u32", "key"), ("+0x04", "bytes[rest]", "unknown_04"), ("end-0x04", "u32", "unknown_end"),
    )
    bad = good.replace("end-0x04", "end-0x08")

    assert _messages(_doc(FILE_LAYOUT, good)) == []
    assert "`end-0x08` minus its 4 bytes does not reach the next row" in _messages(_doc(FILE_LAYOUT, bad))


def test_dropped_sections_and_example_blocks_are_reported() -> None:
    text = _doc(FILE_LAYOUT, ROW, extra="## Suggested UI Layout\n\nColumns.\n")
    example = text.replace("Rows.\n", "Rows.\n\n```text\nkey 1\n```\n")

    assert "`## Suggested UI Layout` is no longer part of a format doc" in _messages(text)
    assert "Purpose holds an example block; the layout tables show every field" in _messages(example)


def test_the_versions_markers_are_required() -> None:
    text = _doc(FILE_LAYOUT, ROW).replace("<!-- versions:end -->\n", "")

    assert _messages(text) == ["`## Versions` needs the `versions:begin` and `versions:end` markers"]


def test_layouts_run_newest_first_and_older_ones_list_known_structures() -> None:
    old_row = _structure("Old Row (4 bytes)", ("+0x00", "u32", "key"))
    layouts = f"## Layout 1\n\n{FILE_LAYOUT}\n{ROW}\n## Layout 2\n\n{old_row}"

    assert _messages(_doc(layouts=layouts)) == [
        "layouts should be numbered 2, 1 from the top",
        "`Old Row` is not in a newer layout; an older layout lists only what changed",
    ]


def test_an_older_layout_uses_the_newer_layouts_structures() -> None:
    old_row = _structure("Row (6 bytes)", ("+0x00", "u16", "key"), ("+0x02", "u32", "unknown_04"))
    layouts = f"## Layout 2\n\n{FILE_LAYOUT}\n{ROW}\n## Layout 1\n\n{old_row}"

    assert _messages(_doc(layouts=layouts)) == []


@pytest.mark.parametrize("name", ["reserved", "reserved_05", "pad0", "padding", "const1", "zero_a", "tail_zero", "flag_17", "unknown", "name_ko", "unknown_0A", "x, y"])
def test_names_that_state_a_value_or_break_the_form_are_rejected(name: str) -> None:
    assert name_problems(Field(1, "`+0x00`", "u32", name, ""), frozenset({name}), is_top_level=False)


@pytest.mark.parametrize("name", ["item_id", "unknown_0c", "unknown_2d5", "unknown_end", "unknown_str_ref", "name_kr", "key_dup"])
def test_names_for_a_meaning_or_an_unknown_are_accepted(name: str) -> None:
    assert name_problems(Field(1, "`+0x00`", "u32", name, ""), frozenset({name, "key"}), is_top_level=False) == ()


def test_padding_needs_its_proof_and_zero_only_names_the_trailer() -> None:
    def problems(name: str, notes: str, is_top_level: bool) -> tuple[str, ...]:
        return name_problems(Field(1, "`+0x00`", "u8", name, notes), frozenset({name}), is_top_level)

    assert problems("padding_05", "Always 0", False)
    assert problems("padding_05", "No member there in the 2016 PDB struct", False) == ()
    assert problems("zero", "", False)
    assert problems("zero", "", True) == ()


def test_unknown_after_and_dup_names_point_at_a_field_of_the_structure() -> None:
    assert name_problems(Field(1, "", "u8", "unknown_after_path", ""), frozenset({"unknown_after_path"}), False)
    assert name_problems(Field(1, "", "u8", "unknown_after_path", ""), frozenset({"unknown_after_path", "path"}), False) == ()


@pytest.mark.parametrize(
    ("text", "size", "part"),
    [
        ("u32", 4, 4),
        ("u16[10]", 20, 20),
        ("f32[7][3]", 84, 84),
        ("bytes[16]", 16, 16),
        ("char16[4]", 8, 8),
        ("str16", None, 8),
        ("pstr", None, 5),
        ("pstr[string_count]", None, 0),
        ("u8 if size = 190", None, 0),
        ("Row[3]", 24, 24),
        ("Row[row_count]", None, 0),
        ("Row[..table_start]", None, 0),
        ("Row[while key != 200]", None, 0),
        ("bytes[rest]", None, 0),
    ],
)
def test_type_sizes(text: str, size: int | None, part: int) -> None:
    spec = parse_type(text)

    assert not isinstance(spec, str), spec
    assert fixed_size(spec, {"Row": 8}) == size
    assert fixed_part(spec, {"Row": 8}) == part


@pytest.mark.parametrize("text", ["row[]", "u24", "bytes", "str16[2][2]", "char[rest]", "Row[a b]"])
def test_types_outside_the_grammar_are_rejected(text: str) -> None:
    assert isinstance(parse_type(text), str)


def test_a_table_row_keeps_escaped_and_quoted_pipes_in_their_cell() -> None:
    assert split_row(r"| `a | b` | c \| d | e |") == ("`a | b`", r"c \| d", "e")
