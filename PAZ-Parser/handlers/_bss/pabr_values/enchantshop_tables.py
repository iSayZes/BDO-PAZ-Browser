"""Layouts of the small enchant and shop tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/<stem>_bss.md`
(`cashproductcategorytagorder_dbss.md` for the one `.dbss`). The names of
`enchant_blackstonestack.bss` and `mansionrentaldiscount.bss` follow the
`Enchant_BlackStoneStack`, `MantionRental_Percent` and
`MantionReturn_Percent` sheets of a private server's `DataSheets.bexcel` on
client 1784. Those of `reforgestonestaticstatusmanager.bss`,
`drawitemstaticstatus.bss` and `pearlusedchallengegroup.bss` follow the
getters of the client Lua; `cashproductcategorytagorder.dbss` has neither
and takes its name from the file.
"""

from __future__ import annotations

from .enchantshop_names import challenge_name, challenge_text, day_percent_text, reforge_level_text, stack_text
from .fields import ITEM_KEY, item_field
from .layout import NameLookup, RowCount, ValueField, ValueTable, unknown_fields
from .world_names import item_key_entry_text


# need_stack_item_count, stack, padding_0c (enchant_blackstonestack_bss.md, Stack).
_STACK_ENTRY = "QI4s"
# item_enchant_key, unknown_04, material_item_enchant_key, padding_0c,
# material_item_count (reforgestonestaticstatusmanager_bss.md, Level).
_LEVEL_ENTRY = "III4sQ"
# day, then discount_percent or return_percent (mansionrentaldiscount_bss.md).
_DAY_PERCENT_ENTRY = "HI"


ENCHANT_SHOP_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "enchant_blackstonestack.bss",
        (
            item_field("need_stack_item_key"),
            ValueField("stacks", _STACK_ENTRY, "stacks", display=stack_text, is_counted_list=True, count_fmt="Q"),
        ),
        RowCount.COUNTED,
        count_key="stackItems",
    ),
    ValueTable(
        "reforgestonestaticstatusmanager.bss",
        (ValueField("levels", _LEVEL_ENTRY, "reforgeLevels", display=reforge_level_text, is_counted_list=True),),
        RowCount.COUNTED,
        count_key="reforgeStones",
        index_column="index",
    ),
    ValueTable(
        "drawitemstaticstatus.bss",
        (
            ITEM_KEY,
            ValueField("coin_item_key", "I", "coinItem", display=item_key_entry_text),
            ValueField("lose_item_key", "I", "loseItem", display=item_key_entry_text),
            *unknown_fields((0x0C, "I")),
            ValueField("index", "H", "index"),
            ValueField("item_count", "H", "itemCount"),
            *unknown_fields((0x14, "H"), (0x16, "H"), (0x18, "B"), (0x19, "B")),
        ),
        RowCount.COUNTED,
        count_key="drawItems",
        first_fields=("index",),
    ),
    ValueTable(
        "pearlusedchallengegroup.bss",
        (
            ValueField(
                "main_challenge_key",
                "H",
                "mainChallengeId",
                NameLookup("main_challenge_name", "mainChallenge", challenge_name),
            ),
            *unknown_fields((0x02, "I")),
            ValueField("challenge_keys", "H", "challenges", display=challenge_text, is_counted_list=True),
        ),
        RowCount.COUNTED,
        count_key="challengeGroupRows",
    ),
    ValueTable(
        "cashproductcategorytagorder.dbss",
        (ValueField("tag_order", "i", "tagOrder"),),
        RowCount.COUNTED,
        count_key="productTags",
        index_column="productTag",
    ),
    ValueTable(
        "mansionrentaldiscount.bss",
        (
            ValueField(
                "rental_percents", _DAY_PERCENT_ENTRY, "rentalDiscounts", display=day_percent_text, is_counted_list=True
            ),
            ValueField(
                "return_percents", _DAY_PERCENT_ENTRY, "returnPercents", display=day_percent_text, is_counted_list=True
            ),
        ),
    ),
)
