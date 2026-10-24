"""Layouts of the Conquest War (major siege) tables that fit the PABR value tables.

`majorsiegerewardstaticstatus.bss` and `siegerewarddata.bss` nest their
reward lists and have their own handlers.
"""

from __future__ import annotations

from _common.rate import rate_percent
from .fields import CHARACTER_KEY
from .layout import RowCount, ValueField, ValueTable, unknown_fields


MAJOR_SIEGE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "majorsiegecommonrewardratestaticstatusmanager.bss",
        (
            *unknown_fields((0x00, "I")),
            ValueField("reward_rate", "I", "rewardRate", display=rate_percent),
        ),
        RowCount.COUNTED,
    ),
    # The file name keeps the client's spelling "seige".
    ValueTable(
        "majorseigereleaseobjectpoint.bss",
        (
            CHARACTER_KEY,
            ValueField("object_point", "I", "objectPoint"),
        ),
        RowCount.COUNTED,
    ),
)
