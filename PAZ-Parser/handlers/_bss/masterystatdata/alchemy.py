"""The extra item chances the Alchemy tooltip derives from an `alchemystatdata.bss` row.

`HandleEventOnOut_CharInfoLife_All_LifeType_Tooltip` in
`panel_characterinfo_life_all_2.luac` splits the extra item chance
(`_eventDropRate`) into three tiers with the shares that
`getEventDropRateForTooltip(1)` and `(2)` return:

    basic   = event * (1 - share_2) * (1 - share_1)
    special = event * (1 - share_2) * share_1
    rare    = event * share_2

Share 0 is read but not used. The results stay in the file's unit,
1,000,000 = 100%.
"""

from __future__ import annotations

RATE_SCALE = 1_000_000


def extra_item_rates(record: dict) -> dict:
    event = record["event_drop_rate"] / RATE_SCALE
    special_share = record["event_drop_rate_1"] / RATE_SCALE
    rare_share = record["event_drop_rate_2"] / RATE_SCALE
    return {
        "extra_basic_item_rate": event * (1 - rare_share) * (1 - special_share) * RATE_SCALE,
        "extra_special_item_rate": event * (1 - rare_share) * special_share * RATE_SCALE,
        "extra_rare_item_rate": event * rare_share * RATE_SCALE,
    }
