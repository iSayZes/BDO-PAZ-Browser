"""Layouts of the server option tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/<stem>_bss.md`. The field names follow
the sheets of a private server's `DataSheets.bexcel` on client 1784
(`WorldMarketVariedPrice`, `WorldMarketVariedTradeCount`,
`DynamicBSSOption_Table`, `LightUserBonus_Table`, `FamilyPointStat`,
`Water_Table` and `Underground_Table`), and the 2016
`gc::LightUserBonusStaticStatus` and `gc::BitmapDropInfo`.
"""

from __future__ import annotations

from .layout import RowCount, ValueField, ValueTable, unknown_fields
from .names import map_color_text
from .server_names import light_user_reward_text


# The reward slots of a light user bonus row (DisConnectedTime1 to 10, Bonus1 to 10).
LIGHT_USER_REWARD_SLOTS = 10
# disconnected_time (i64), bonus (u32); lightuserbonus_bss.md, Reward.
_LIGHT_USER_REWARD = "qI"


def _bitmap_drop_table(file_name: str) -> ValueTable:
    """A colour key of a server bitmap and its unread drop bytes (waterinfo_bss.md, undergroundinfo_bss.md)."""
    return ValueTable(
        file_name,
        (
            ValueField("color_key", "3s", "color", display=map_color_text),
            *unknown_fields((0x03, "B"), (0x04, "8s")),
        ),
        RowCount.COUNTED,
        count_key="colors",
    )


SERVER_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "variedprice.bss",
        (
            ValueField("start_range_price", "Q", "startRangePrice"),
            ValueField("end_range_price", "Q", "endRangePrice"),
            ValueField("unit_price", "Q", "unitPrice"),
            ValueField("pass_bidding_count", "Q", "passBiddingCount"),
            ValueField("world_market_price_point", "Q", "worldMarketPricePoint"),
        ),
        RowCount.COUNTED,
        count_key="priceRanges",
    ),
    ValueTable(
        "variedtradecount.bss",
        (
            ValueField("min_family_point", "Q", "minFamilyPoint"),
            ValueField("max_family_point", "Q", "maxFamilyPoint"),
            ValueField("add_trade_count", "Q", "addTradeCount"),
        ),
        RowCount.COUNTED,
        count_key="familyPointRanges",
    ),
    # One flag per static status type, at the type's index (dynamicbssoption_bss.md).
    ValueTable(
        "dynamicbssoption.bss",
        (ValueField("real", "B", "real"),),
        RowCount.TO_TABLE_START,
        count_key="staticStatusTypes",
        index_column="index",
    ),
    ValueTable(
        "lightuserbonus.bss",
        (
            ValueField("key", "H", "key"),
            ValueField(
                "rewards",
                _LIGHT_USER_REWARD,
                "rewards",
                fixed_count=LIGHT_USER_REWARD_SLOTS,
                list_display=light_user_reward_text,
            ),
            ValueField("valid_reward_count", "I", "validRewardCount"),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "familypointstat.bss",
        (
            ValueField("index", "H", "index"),
            ValueField("point", "I", "point"),
            ValueField("offence_point", "f", "offencePoint"),
            ValueField("defence_point", "f", "defencePoint"),
            ValueField("hp", "f", "hp"),
            ValueField("mp", "I", "mp"),
            ValueField("sp", "I", "sp"),
            ValueField("weight", "I", "weight"),
            ValueField("inventory", "B", "inventory"),
            ValueField("hit", "f", "hit"),
            ValueField("dv", "f", "dv"),
            ValueField("unknown_27", "I"),
        ),
        RowCount.COUNTED,
        count_key="familyStatSteps",
    ),
    _bitmap_drop_table("waterinfo.bss"),
    _bitmap_drop_table("undergroundinfo.bss"),
)
