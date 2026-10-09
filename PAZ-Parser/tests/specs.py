from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any, Protocol

from _common.pa_text import pa_key, strip_pa_tags

from .case_input import CaseInput
from .declared import DeclaredCount


class TestSpec(Protocol):
    def check(self, records: list[dict], source: CaseInput) -> str:
        ...


@dataclass(frozen=True)
class DeclaredCountTest:
    """The row count equals the count the input declares (a header field or offset-table rows)."""

    declared: DeclaredCount

    def check(self, records: list[dict], source: CaseInput) -> str:
        expected = self.declared(source)
        actual = len(records)
        if actual != expected:
            raise AssertionError(f"DeclaredCountTest input declares {expected} rows, parsed {actual}")
        return f"DeclaredCountTest rows == declared {expected}"


@dataclass(frozen=True)
class TargetTest:
    col: str
    value: Any
    expected: dict[str, Any] | list[dict[str, Any]]

    def check(self, records: list[dict], source: CaseInput) -> str:
        if isinstance(self.value, (list, tuple, set, frozenset)):
            found = [record for record in records if record.get(self.col) in self.value]
        else:
            found = [record for record in records if record.get(self.col) == self.value]
        if not found:
            raise AssertionError(f"TargetTest found no rows where {self.col} == {self.value!r}")

        if isinstance(self.expected, list):
            if len(found) != len(self.expected):
                raise AssertionError(
                    f"TargetTest {self.col} == {self.value!r} expected "
                    f"{len(self.expected)} rows, got {len(found)}"
                )
            for index, expected in enumerate(self.expected):
                _assert_subset(found[index], expected, f"target[{index}]")
            return f"TargetTest {self.col} == {self.value!r} matched {len(found)} rows"

        _assert_subset(found[0], self.expected, "target[0]")
        return f"TargetTest {self.col} == {self.value!r} matched first row"


@dataclass(frozen=True)
class SchemaTest:
    required_keys: list[str]

    def check(self, records: list[dict], source: CaseInput) -> str:
        missing_by_pos: list[str] = []
        for pos, record in enumerate(records):
            missing = [key for key in self.required_keys if key not in record]
            if missing:
                missing_by_pos.append(f"records[{pos}] missing {missing}")
        if missing_by_pos:
            raise AssertionError("; ".join(missing_by_pos[:5]))
        return f"SchemaTest required keys present: {', '.join(self.required_keys)}"


@dataclass(frozen=True)
class RangeTest:
    col: str
    min_val: Any
    max_val: Any

    def check(self, records: list[dict], source: CaseInput) -> str:
        for pos, record in enumerate(records):
            value = record.get(self.col)
            # None is an empty cell (a 0 ID shown as a dash), not out of range.
            if value is None:
                continue
            if value < self.min_val or value > self.max_val:
                raise AssertionError(
                    f"RangeTest records[{pos}].{self.col}={value!r} outside "
                    f"[{self.min_val!r}, {self.max_val!r}]"
                )
        return f"RangeTest {self.col} within [{self.min_val!r}, {self.max_val!r}]"


@dataclass(frozen=True)
class PaFieldTest:
    """A `pa_fields` text: the plain field is its tagged copy without tags, and
    some rows keep a game colour in the copy."""

    field: str

    def check(self, records: list[dict], source: CaseInput) -> str:
        tagged_key = pa_key(self.field)
        for pos, record in enumerate(records):
            plain = strip_pa_tags(record[tagged_key]).strip()
            if record[self.field] != plain:
                raise AssertionError(
                    f"PaFieldTest records[{pos}].{self.field}={record[self.field]!r} "
                    f"is not its tagged copy without tags ({plain!r})"
                )
        if not any("<PAColor" in record[tagged_key] for record in records):
            raise AssertionError(f"PaFieldTest no {tagged_key} holds a <PAColor> tag")
        return f"PaFieldTest {self.field} keeps its game colours"


# Hangul syllables. English text can hold other non-ASCII letters (`Nymphamaré`).
_HANGUL = re.compile("[가-힣]")


@dataclass(frozen=True)
class UserLanguageTest:
    """With English LOC loaded, no row shows Korean in these text fields.

    Each field is a user-facing column that reads LOC first and falls back to
    the inline Korean, so a Korean value means the LOC lookup was missed. A
    field may hold a string or a list of strings; `None` (an empty cell) is
    skipped.
    """

    fields: list[str]

    def check(self, records: list[dict], source: CaseInput) -> str:
        for pos, record in enumerate(records):
            for field in self.fields:
                value = record[field]
                texts = value if isinstance(value, list) else [value]
                if any(_HANGUL.search(text) for text in texts if text is not None):
                    raise AssertionError(f"UserLanguageTest records[{pos}].{field}={value!r} is Korean")
        return f"UserLanguageTest no Korean in {', '.join(self.fields)}"


def _assert_subset(record: dict, expected: dict[str, Any], label: str) -> None:
    for key, expected_value in expected.items():
        if key not in record:
            raise AssertionError(f"{label} missing key {key!r}")
        actual_value = record[key]
        if actual_value != expected_value:
            raise AssertionError(
                f"{label}.{key} expected {expected_value!r}, got {actual_value!r}"
            )
