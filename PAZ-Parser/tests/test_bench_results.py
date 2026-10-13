"""bench.results and bench.compare: the result file and comparing two runs."""
from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import pytest

from bench.compare import environment_differences, format_comparison, stage_deltas
from bench.machine import Machine
from bench.pinning import UNPINNED, PinState
from bench.report import describe_fixture
from bench.results import (
    SCHEMA_VERSION,
    BenchResult,
    FixtureInfo,
    read_result,
    result_from_json,
    result_to_json,
    write_result,
)
from bench.timing import StageTiming
from cli.errors import CliError


def _result(**changes: object) -> BenchResult:
    result = BenchResult(
        created="2026-10-04T12:00:00+00:00",
        machine=Machine(
            cpu_model="Test CPU",
            logical_cpus=8,
            ram_bytes=16 * 1024**3,
            power_plan="Balanced",
            os="TestOS-1",
            python="CPython 3.12.0",
            git_commit="0123456789abcdef",
            is_git_dirty=False,
            decoders="native",
        ),
        pin=PinState(cpu=2, efficiency_class=1, top_efficiency_class=1, is_high_priority=True),
        fixture=FixtureInfo(name="pad00001.paz", files=3, stored_bytes=100, size_bytes=300, sha256="ab" * 32),
        warmup=1,
        repeats=3,
        stages={
            "decrypt": StageTiming(times_s=(2.0, 2.1, 2.2), peak_bytes=None),
            "read": StageTiming(times_s=(4.0, 4.4, 4.2), peak_bytes=1024),
        },
    )
    return replace(result, **changes)


def test_a_result_survives_the_json_round_trip() -> None:
    result = _result()

    assert result_from_json(json.loads(json.dumps(result_to_json(result)))) == result


def test_the_fixture_line_names_the_decoded_size_when_there_is_one() -> None:
    archive = FixtureInfo(name="pad00001.paz", files=3, stored_bytes=1024**2, size_bytes=3 * 1024**2, sha256="ab" * 32)
    index = replace(archive, name="pad00000.meta", size_bytes=0)

    assert describe_fixture(archive) == "pad00001.paz (3 files, 1.0 MB stored, 3.0 MB decoded)"
    assert describe_fixture(index) == "pad00000.meta (3 files, 1.0 MB stored)"


def test_write_and_read_result_use_the_same_file(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "result.json"
    write_result(path, _result())

    assert read_result(path) == _result()


def test_a_missing_field_is_named_with_its_path() -> None:
    data = result_to_json(_result())
    del data["pin"]["cpu"]

    with pytest.raises(ValueError, match=r"result\.pin\.cpu is missing"):
        result_from_json(data)


def test_a_bool_does_not_pass_as_an_integer() -> None:
    data = result_to_json(_result())
    data["repeats"] = True

    with pytest.raises(ValueError, match="repeats must be an integer"):
        result_from_json(data)


def test_another_schema_version_is_refused() -> None:
    data = result_to_json(_result())
    data["schema"] = SCHEMA_VERSION + 1

    with pytest.raises(ValueError, match="schema"):
        result_from_json(data)


def test_a_schema_1_result_reads_without_decoders() -> None:
    data = result_to_json(_result())
    data["schema"] = 1
    del data["machine"]["decoders"]

    assert result_from_json(data).machine.decoders is None


def test_comparing_python_and_native_decoders_names_the_difference() -> None:
    python = _result(machine=replace(_result().machine, decoders="python"))

    assert "decoders: python -> native" in environment_differences(python, _result())


def test_stage_times_must_be_non_negative_numbers() -> None:
    data = result_to_json(_result())
    data["stages"]["decrypt"]["times_s"] = [1.0, -1.0]

    with pytest.raises(ValueError, match="times_s"):
        result_from_json(data)


def test_read_result_reports_a_file_that_is_not_json(tmp_path: Path) -> None:
    path = tmp_path / "broken.json"
    path.write_text("{not json", encoding="utf-8")

    with pytest.raises(CliError, match="not JSON"):
        read_result(path)


def test_identical_setups_have_no_environment_differences() -> None:
    assert environment_differences(_result(), _result()) == []


def test_environment_differences_name_what_changed() -> None:
    moved = _result(pin=replace(_result().pin, cpu=4))

    differences = environment_differences(_result(), moved)

    assert any(difference.startswith("pinned CPU: 2 -> 4") for difference in differences)


def test_an_unpinned_run_is_always_flagged() -> None:
    differences = environment_differences(_result(), _result(pin=UNPINNED))

    assert any("new run was not pinned" in difference for difference in differences)


def test_stage_deltas_compare_the_fastest_runs_of_shared_stages() -> None:
    faster = _result(stages={"decrypt": StageTiming(times_s=(1.0, 1.5), peak_bytes=None)})

    deltas = stage_deltas(_result(), faster)

    assert [delta.name for delta in deltas] == ["decrypt"]
    assert deltas[0].speedup == pytest.approx(2.0)
    assert "2.00x faster" in format_comparison(_result(), faster)
