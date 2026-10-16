"""How stored buff amounts are scaled and written."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    """How a stored amount is scaled and suffixed for display."""

    divisor: int = 1
    suffix: str = ""
    # Writes the whole amount instead, for units the game words: `15 days`.
    formatter: Callable[[int], str] | None = None

    @property
    def is_scaled(self) -> bool:
        """True when the stored number differs from what the game shows."""
        return self.divisor != 1 or bool(self.suffix) or self.formatter is not None


FLAT = Unit()
# Percentages are stored per million: 25000 is 2.5%.
PERCENT = Unit(10_000, "%")
# Weight is stored in ten-thousandths of an LT: 1000000 is 100 LT.
WEIGHT = Unit(10_000, " LT")
# Durations are stored in milliseconds.
SECONDS = Unit(1_000, " sec")
# Distances are stored in centimetres: 1000 is 10m.
METRES = Unit(100, "m")
# Cooking and alchemy time cuts are stored per million of 20 seconds:
# 250000 is 5 sec, 50000 is 1 sec.
CRAFT_SECONDS = Unit(50_000, " sec")
# A key written as stored, without thousands separators: `Remove Group 44812`.
KEY = Unit(formatter=str)

_MINUTES_PER_HOUR = 60
_MINUTES_PER_DAY = 24 * _MINUTES_PER_HOUR


def _count(number: int, word: str) -> str:
    return f"{number:,} {word}" if number == 1 else f"{number:,} {word}s"


def minutes_text(minutes: int) -> str:
    """`15 days`, `1 day`, `10 hours`, `25 min`, as package item names word them."""
    if minutes and minutes % _MINUTES_PER_DAY == 0:
        return _count(minutes // _MINUTES_PER_DAY, "day")
    if minutes and minutes % _MINUTES_PER_HOUR == 0:
        return _count(minutes // _MINUTES_PER_HOUR, "hour")
    return f"{minutes:,} min"


# Package durations are stored in minutes: 21600 is 15 days.
MINUTES = Unit(formatter=minutes_text)

_MAX_DECIMALS = 4


def format_amount(value: int, unit: Unit, *, signed: bool) -> str:
    """`+150`, `-6`, `+2,560,350`, `+2.5%`, `+100 LT`, or `10` unsigned."""
    if unit.formatter is not None:
        return unit.formatter(value)
    sign = "+" if signed else ""
    if unit.divisor == 1:
        number = f"{value:{sign},}"
    else:
        scaled = f"{value / unit.divisor:{sign},.{_MAX_DECIMALS}f}"
        number = scaled.rstrip("0").rstrip(".")
    return number + unit.suffix


def seconds_text(milliseconds: int) -> str:
    """`10`, `1.5`."""
    return f"{milliseconds / 1_000:.3f}".rstrip("0").rstrip(".")


_MS_PER_MINUTE = 60_000


def cooldown_text(milliseconds: int) -> str:
    """`2 sec`, `3 min`, `12 hours`, as the fairy skill texts word cooldowns."""
    if milliseconds and milliseconds % _MS_PER_MINUTE == 0:
        return minutes_text(milliseconds // _MS_PER_MINUTE)
    return f"{seconds_text(milliseconds)} sec"


# Cooldowns are stored in milliseconds and worded by size: 180000 is 3 min.
COOLDOWN = Unit(formatter=cooldown_text)
