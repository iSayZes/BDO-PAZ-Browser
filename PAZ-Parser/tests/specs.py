from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class TestSpec(Protocol):
    def check(self, records: list[dict]) -> str:
        ...


@dataclass(frozen=True)
class CountTest:
    expected: int

    def check(self, records: list[dict]) -> str:
        actual = len(records)
        if actual != self.expected:
            raise AssertionError(f"CountTest expected {self.expected}, got {actual}")
        return f"CountTest rows == {self.expected}"


@dataclass(frozen=True)
class PosTest:
    pos: int
    expected: dict[str, Any]

    def check(self, records: list[dict]) -> str:
        if self.pos >= len(records) or self.pos < -len(records):
            raise AssertionError(f"PosTest pos {self.pos} outside {len(records)} records")
        _assert_subset(records[self.pos], self.expected, f"records[{self.pos}]")
        return f"PosTest records[{self.pos}] matched"


@dataclass(frozen=True)
class TargetTest:
    col: str
    value: Any
    expected: dict[str, Any] | list[dict[str, Any]]

    def check(self, records: list[dict]) -> str:
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

    def check(self, records: list[dict]) -> str:
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

    def check(self, records: list[dict]) -> str:
        for pos, record in enumerate(records):
            value = record.get(self.col)
            if value < self.min_val or value > self.max_val:
                raise AssertionError(
                    f"RangeTest records[{pos}].{self.col}={value!r} outside "
                    f"[{self.min_val!r}, {self.max_val!r}]"
                )
        return f"RangeTest {self.col} within [{self.min_val!r}, {self.max_val!r}]"


def _assert_subset(record: dict, expected: dict[str, Any], label: str) -> None:
    for key, expected_value in expected.items():
        if key not in record:
            raise AssertionError(f"{label} missing key {key!r}")
        actual_value = record[key]
        if actual_value != expected_value:
            raise AssertionError(
                f"{label}.{key} expected {expected_value!r}, got {actual_value!r}"
            )
