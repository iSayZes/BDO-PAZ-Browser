from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from .specs import TestSpec


@dataclass(frozen=True)
class HandlerCase:
    handler_name: str
    data_file: str | Path
    companion_files: dict[str, str | Path]
    loc_file: str | Path | None
    uses_loc: bool
    loc_fields: list[str]
    internal_path: str
    tests: list[TestSpec]
    record_mapper: Callable[[dict], dict] | None = None


@dataclass
class HandlerResult:
    row_count: int
    elapsed_ms: float
    loc_total_calls: int | None
    loc_fallback_count: int | None
    records: list[dict] = field(default_factory=list, repr=False)
    passed: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        return "passed" if not self.failed else "failed"

    @property
    def loc_summary(self) -> str:
        if self.loc_total_calls is None or self.loc_fallback_count is None:
            return "loc: disabled"

        return f"loc: {self.loc_fallback_count:,} misses / {self.loc_total_calls:,} lookups"

    def summary(self) -> str:
        return (
            f"{self.status}\n"
            f"  rows:  {self.row_count:,}\n"
            f"  parse: {self.elapsed_ms:.0f} ms\n"
            f"  {self.loc_summary}"
        )
