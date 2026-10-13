"""Plain-text summaries of a benchmark run for the console."""
from __future__ import annotations

from .machine import Machine
from .pinning import PinState
from .results import BenchResult, FixtureInfo

_MB = 1024 * 1024
_GB = 1024 * _MB


def describe_machine_line(machine: Machine) -> str:
    """One line: CPU, logical CPUs, RAM, power plan, Python, decoders."""
    parts = [
        machine.cpu_model or "unknown CPU",
        f"{machine.logical_cpus} logical CPUs" if machine.logical_cpus else None,
        f"{machine.ram_bytes / _GB:.1f} GB RAM" if machine.ram_bytes else None,
        f"power plan {machine.power_plan}" if machine.power_plan else None,
        machine.python,
        f"{machine.decoders} decoders" if machine.decoders else None,
    ]
    return ", ".join(part for part in parts if part)


def describe_pin(pin: PinState) -> str:
    if not pin.is_pinned:
        return "not pinned, the OS picks the core (numbers can drift)"
    priority = "high priority" if pin.is_high_priority else "normal priority"
    return f"CPU {pin.cpu}, {priority}"


def describe_fixture(fixture: FixtureInfo) -> str:
    files = "" if fixture.files == 1 else f"{fixture.files:,} files, "
    decoded = f", {fixture.size_bytes / _MB:.1f} MB decoded" if fixture.size_bytes else ""
    return f"{fixture.name} ({files}{fixture.stored_bytes / _MB:.1f} MB stored{decoded})"


def format_timings(result: BenchResult) -> str:
    lines = [
        f"fixture: {describe_fixture(result.fixture)}",
        f"pinned:  {describe_pin(result.pin)}",
        f"runs:    {result.warmup} warm-up, {result.repeats} timed",
        "",
        f"{'stage':<12}{'min':>9}{'median':>10}{'stdev':>9}{'peak mem':>11}",
    ]
    for name, timing in result.stages.items():
        lines.append(
            f"{name:<12}{timing.min_s:>8.3f}s{timing.median_s:>9.3f}s{timing.stdev_s:>8.3f}s"
            f"{_megabytes(timing.peak_bytes):>11}"
        )
    return "\n".join(lines)


def _megabytes(size: int | None) -> str:
    return "-" if size is None else f"{size / _MB:.1f} MB"
