"""Chances and rates stored on the client's 1,000,000 = 100% scale."""

from __future__ import annotations

RATE_PER_PERCENT = 10_000


def rate_percent(value: int) -> str:
    """`70000` -> `7%`, `1600` -> `0.16%`."""
    return f"{value / RATE_PER_PERCENT:g}%"
