"""Cell text for mastery table values, rounded the way the Life Skill tooltip rounds them.

`global_util_ui.luac` turns a rate (1,000,000 = 100%) into a percent with
`PaGlobalFunc_GlobalUtil_RoundRateToSecondPoint` (floor((rate + 50) / 100)
/ 100, two decimals) or `PaGlobalFunc_GlobalUtil_RoundRateToThridPoint`
(floor((rate + 5) / 10) / 1000, three decimals). Both treat a rate below 0
as 0. Counts, such as the mass processing batches, are shown as stored.
"""

from __future__ import annotations

import math

from .spec import CellFormat


def rate_text(rate: float, cell_format: CellFormat) -> str:
    rate = max(rate, 0)
    if cell_format is CellFormat.RATE_3:
        return f"{math.floor((rate + 5) / 10) / 1000:.3f}%"
    return f"{math.floor((rate + 50) / 100) / 100:.2f}%"


def cell_text(value: int | float, cell_format: CellFormat) -> str:
    if cell_format is CellFormat.COUNT:
        return str(value)
    return rate_text(value, cell_format)


def mastery_text(mastery: float) -> str:
    return f"{mastery:g}"
