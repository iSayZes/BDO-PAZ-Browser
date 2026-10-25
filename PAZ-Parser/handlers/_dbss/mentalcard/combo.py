"""How a knowledge card's combo effect is shown.

The amity tooltip's "Next combo effect" line reads "After {apply_turn + 1}
turns, {stat} will increase by {varied_value} for {valid_turn} turns", or
"None" when `buff_type` is 4. Checked in game on 19 cards (see
docs/file-formats/dbss/mentalcard_dbss.md). Records keep the raw values, so sorting
and export stay exact.
"""

from __future__ import annotations

from enum import IntEnum

from .parser import MentalCardRecord


class BuffType(IntEnum):
    FAVOR = 0
    INTEREST = 1
    NONE = 4


BUFF_TYPE_LABELS: dict[BuffType, str] = {
    BuffType.FAVOR: "Favor",
    BuffType.INTEREST: "Interest Level",
}


def has_combo(record: MentalCardRecord) -> bool:
    return record.buff_type != BuffType.NONE


def combo_text(record: MentalCardRecord) -> str:
    """`After 2 turns: Favor +4 for 3 turns`, or "" without a combo.

    A buff type no card uses yet shows as `Type N`.
    """
    if not has_combo(record):
        return ""

    try:
        stat = BUFF_TYPE_LABELS[BuffType(record.buff_type)]
    except (ValueError, KeyError):
        stat = f"Type {record.buff_type}"
    # The tooltip shows the stored delay plus one.
    shown_delay = record.apply_turn + 1
    value = round(record.varied_value)
    return f"After {shown_delay} turns: {stat} +{value} for {record.valid_turn} turns"
