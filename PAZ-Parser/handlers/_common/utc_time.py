"""Unix seconds as UTC date text, without `datetime` (not in the modules the exe bundles, handler_api.py).

The date comes from Howard Hinnant's `civil_from_days`, which turns days since
1970-01-01 into a proleptic Gregorian year, month and day.
"""

from __future__ import annotations

_SECONDS_PER_DAY = 86_400
_SECONDS_PER_HOUR = 3_600
_SECONDS_PER_MINUTE = 60
# Days from 0000-03-01 to 1970-01-01, and the lengths of a 400-year era.
_EPOCH_SHIFT_DAYS = 719_468
_DAYS_PER_ERA = 146_097
_YEARS_PER_ERA = 400


def civil_from_days(days: int) -> tuple[int, int, int]:
    """`(year, month, day)` of `days` since 1970-01-01."""
    era, day_of_era = divmod(days + _EPOCH_SHIFT_DAYS, _DAYS_PER_ERA)
    year_of_era = (day_of_era - day_of_era // 1460 + day_of_era // 36524 - day_of_era // 146096) // 365
    day_of_year = day_of_era - (365 * year_of_era + year_of_era // 4 - year_of_era // 100)
    month_index = (5 * day_of_year + 2) // 153
    day = day_of_year - (153 * month_index + 2) // 5 + 1
    month = month_index + 3 if month_index < 10 else month_index - 9
    year = year_of_era + era * _YEARS_PER_ERA + (1 if month <= 2 else 0)
    return year, month, day


def utc_text(seconds: int) -> str:
    """`2021-02-03 08:59`: seconds since 1970-01-01 read as UTC."""
    days, second_of_day = divmod(seconds, _SECONDS_PER_DAY)
    year, month, day = civil_from_days(days)
    hour, rest = divmod(second_of_day, _SECONDS_PER_HOUR)
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{rest // _SECONDS_PER_MINUTE:02d}"
