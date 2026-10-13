"""Compare two benchmark results, and say when they are not comparable."""
from __future__ import annotations

from dataclasses import dataclass

from .results import BenchResult


@dataclass(frozen=True)
class StageDelta:
    name: str
    old_min_s: float
    new_min_s: float

    @property
    def speedup(self) -> float:
        """Above 1 means the new run is faster."""
        return self.old_min_s / self.new_min_s if self.new_min_s > 0 else float("inf")


def environment_differences(old: BenchResult, new: BenchResult) -> list[str]:
    """Everything besides the code that differs between the two runs.

    Each one can move the numbers on its own, so a speedup is only the code's
    when this list is empty.
    """
    checks: list[tuple[str, object, object]] = [
        ("CPU model", old.machine.cpu_model, new.machine.cpu_model),
        ("logical CPUs", old.machine.logical_cpus, new.machine.logical_cpus),
        ("RAM bytes", old.machine.ram_bytes, new.machine.ram_bytes),
        ("power plan", old.machine.power_plan, new.machine.power_plan),
        ("OS", old.machine.os, new.machine.os),
        ("Python", old.machine.python, new.machine.python),
        ("decoders", old.machine.decoders or "unknown", new.machine.decoders or "unknown"),
        ("pinned CPU", old.pin.cpu, new.pin.cpu),
        ("high priority", old.pin.is_high_priority, new.pin.is_high_priority),
        ("fixture", old.fixture.name, new.fixture.name),
        ("fixture hash", old.fixture.sha256, new.fixture.sha256),
        ("warm-up runs", old.warmup, new.warmup),
        ("repeats", old.repeats, new.repeats),
    ]
    differences = [f"{label}: {before} -> {after}" for label, before, after in checks if before != after]
    for label, result in (("old", old), ("new", new)):
        if not result.pin.is_pinned:
            differences.append(f"the {label} run was not pinned, so the OS could move it between cores")
    return differences


def stage_deltas(old: BenchResult, new: BenchResult) -> list[StageDelta]:
    """Stages timed in both runs, in the new run's order."""
    return [
        StageDelta(name, old.stages[name].min_s, timing.min_s)
        for name, timing in new.stages.items()
        if name in old.stages
    ]


def format_comparison(old: BenchResult, new: BenchResult) -> str:
    lines = [
        f"old: {_describe(old)}",
        f"new: {_describe(new)}",
        "",
    ]
    differences = environment_differences(old, new)
    if differences:
        lines.append("Not like for like, these differ besides the code:")
        lines.extend(f"  - {difference}" for difference in differences)
        lines.append("")

    deltas = stage_deltas(old, new)
    if not deltas:
        lines.append("The two runs share no stage.")
        return "\n".join(lines)

    lines.append(f"{'stage':<12}{'old min':>10}{'new min':>10}  change")
    for delta in deltas:
        lines.append(
            f"{delta.name:<12}{delta.old_min_s:>9.3f}s{delta.new_min_s:>9.3f}s  {_change(delta.speedup)}"
        )
    return "\n".join(lines)


def _describe(result: BenchResult) -> str:
    commit = (result.machine.git_commit or "unknown commit")[:10]
    if result.machine.is_git_dirty:
        commit += " (uncommitted changes)"
    return f"{commit}, {result.created}"


def _change(speedup: float) -> str:
    if speedup >= 1:
        return f"{speedup:.2f}x faster"
    return f"{1 / speedup:.2f}x slower"
