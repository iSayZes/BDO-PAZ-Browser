"""A benchmark result and its JSON file, read back with every field checked."""
from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from cli.errors import CliError

from .machine import Machine
from .pinning import PinState
from .timing import StageTiming

# Bumped when a field changes meaning or is added. Schema 1 files still read,
# without `machine.decoders`; other versions are refused.
SCHEMA_VERSION = 2
_DECODERS_SCHEMA = 2
_READABLE_SCHEMAS = (1, SCHEMA_VERSION)


@dataclass(frozen=True)
class FixtureInfo:
    """What a run decoded; the hash catches a client patch changing it.

    `name` is the entry's internal path, the archive's file name or the meta
    file's. `size_bytes` is 0 for the index, which decodes no file.
    """

    name: str
    files: int
    stored_bytes: int
    size_bytes: int
    sha256: str


@dataclass(frozen=True)
class BenchResult:
    created: str
    machine: Machine
    pin: PinState
    fixture: FixtureInfo
    warmup: int
    repeats: int
    # Stage name to timing, in pipeline order.
    stages: Mapping[str, StageTiming]


def result_to_json(result: BenchResult) -> dict[str, Any]:
    return {
        "schema": SCHEMA_VERSION,
        "created": result.created,
        "machine": asdict(result.machine),
        "pin": asdict(result.pin),
        "fixture": asdict(result.fixture),
        "warmup": result.warmup,
        "repeats": result.repeats,
        "stages": {
            name: {
                "times_s": list(timing.times_s),
                "peak_bytes": timing.peak_bytes,
                # Derived, written for readers of the file; ignored on load.
                "min_s": timing.min_s,
                "median_s": timing.median_s,
                "stdev_s": timing.stdev_s,
            }
            for name, timing in result.stages.items()
        },
    }


def write_result(path: Path, result: BenchResult) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result_to_json(result), indent=2) + "\n", encoding="utf-8")
    except OSError as ex:
        raise CliError(f"cannot write {path}: {ex}") from ex


def read_result(path: Path) -> BenchResult:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as ex:
        raise CliError(f"cannot read {path}: {ex}") from ex
    except json.JSONDecodeError as ex:
        raise CliError(f"{path} is not JSON: {ex}") from ex
    try:
        return result_from_json(data)
    except ValueError as ex:
        raise CliError(f"{path} is not a benchmark result: {ex}") from ex


def result_from_json(data: object) -> BenchResult:
    """Raises ValueError naming the first missing or mistyped field."""
    root = _Fields(data, "result")
    schema = root.integer("schema")
    if schema not in _READABLE_SCHEMAS:
        raise ValueError(f"schema {schema}, this benchmark reads schema {' and '.join(map(str, _READABLE_SCHEMAS))}")

    machine = root.child("machine")
    pin = root.child("pin")
    fixture = root.child("fixture")
    stages = root.child("stages")
    return BenchResult(
        created=root.text("created"),
        machine=Machine(
            cpu_model=machine.optional_text("cpu_model"),
            logical_cpus=machine.optional_integer("logical_cpus"),
            ram_bytes=machine.optional_integer("ram_bytes"),
            power_plan=machine.optional_text("power_plan"),
            os=machine.text("os"),
            python=machine.text("python"),
            git_commit=machine.optional_text("git_commit"),
            is_git_dirty=machine.optional_flag("is_git_dirty"),
            decoders=machine.optional_text("decoders") if schema >= _DECODERS_SCHEMA else None,
        ),
        pin=PinState(
            cpu=pin.optional_integer("cpu"),
            efficiency_class=pin.optional_integer("efficiency_class"),
            top_efficiency_class=pin.optional_integer("top_efficiency_class"),
            is_high_priority=pin.flag("is_high_priority"),
        ),
        fixture=FixtureInfo(
            name=fixture.text("name"),
            files=fixture.integer("files"),
            stored_bytes=fixture.integer("stored_bytes"),
            size_bytes=fixture.integer("size_bytes"),
            sha256=fixture.text("sha256"),
        ),
        warmup=root.integer("warmup"),
        repeats=root.integer("repeats"),
        stages={name: _stage_timing(stages.child(name)) for name in stages.keys()},
    )


def _stage_timing(fields: _Fields) -> StageTiming:
    times = fields.array("times_s")
    if not times or not all(_is_number(value) and value >= 0 for value in times):
        raise ValueError(f"{fields.where}.times_s must be a non-empty list of non-negative numbers")
    return StageTiming(times_s=tuple(float(value) for value in times), peak_bytes=fields.optional_integer("peak_bytes"))


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


class _Fields:
    """Typed reads from one JSON object, with the path to it in every error."""

    def __init__(self, data: object, where: str) -> None:
        if not isinstance(data, dict):
            raise ValueError(f"{where} must be an object")
        self._data: dict[str, Any] = data
        self.where = where

    def keys(self) -> list[str]:
        return list(self._data)

    def child(self, key: str) -> _Fields:
        return _Fields(self._get(key), f"{self.where}.{key}")

    def text(self, key: str) -> str:
        return self._typed(key, str, "text")

    def integer(self, key: str) -> int:
        value = self._get(key)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{self.where}.{key} must be an integer")
        return value

    def flag(self, key: str) -> bool:
        return self._typed(key, bool, "true or false")

    def array(self, key: str) -> list[Any]:
        return self._typed(key, list, "a list")

    def optional_text(self, key: str) -> str | None:
        return None if self._get(key) is None else self.text(key)

    def optional_integer(self, key: str) -> int | None:
        return None if self._get(key) is None else self.integer(key)

    def optional_flag(self, key: str) -> bool | None:
        return None if self._get(key) is None else self.flag(key)

    def _typed(self, key: str, kind: type, label: str) -> Any:
        value = self._get(key)
        if not isinstance(value, kind):
            raise ValueError(f"{self.where}.{key} must be {label}")
        return value

    def _get(self, key: str) -> Any:
        if key not in self._data:
            raise ValueError(f"{self.where}.{key} is missing")
        return self._data[key]
