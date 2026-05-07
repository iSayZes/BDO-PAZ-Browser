from __future__ import annotations

from .models import HandlerCase, HandlerResult
from .runner import run_case
from .specs import CountTest, PosTest, RangeTest, SchemaTest, TargetTest, TestSpec


def case_id(spec: object) -> str:
    if isinstance(spec, CountTest):
        return "row count"
    if isinstance(spec, PosTest):
        return f"position = {spec.pos}"
    if isinstance(spec, TargetTest):
        if isinstance(spec.value, tuple):
            values = [str(item) for item in spec.value]
            if len(values) == 2:
                return f"{spec.col} in {values[0]}-{values[1]}"
            return f"{spec.col} in {', '.join(values)}"
        return f"{spec.col} = {spec.value}"
    return spec.__class__.__name__.lower()


__all__ = [
    "CountTest",
    "HandlerCase",
    "HandlerResult",
    "PosTest",
    "RangeTest",
    "SchemaTest",
    "TargetTest",
    "TestSpec",
    "case_id",
    "run_case",
]
