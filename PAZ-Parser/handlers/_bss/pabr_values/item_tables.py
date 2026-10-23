"""Layouts of the small item tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/<stem>_bss.md` (`itemprotector_dbss.md`
for the one `.dbss`). The names follow the sheets of a private server's
`DataSheets.bexcel` on client 1784: `Enchant_Protect` (`itemprotector.dbss`),
`Auto_Warehouse_Order_Filter` (`itemmovedata.bss`), `MedalTable`
(`bootyitemlist.bss`, its row key named after `territoryinfo.bss`) and
`Notice_Table` (`notifyexpirationperioditem.bss`).
`autousebuffitemcategoryinfo.bss` has no sheet; its names follow the
auto-use window's getters in the client Lua. `itemsortprioritytype.bss` has
neither, and its two bytes stay `unknown_*`.
"""

from __future__ import annotations

from _common.territory import territory_name
from _dbss.itemenchant.contents_event import contents_event_text
from .fields import ITEM_KEY
from .item_names import auto_use_category_name, item_classify_text, item_type_text, move_filter_name
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .world_names import item_key_entry_text


ITEM_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "itemsortprioritytype.bss",
        unknown_fields((0x00, "B"), (0x01, "B")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "itemprotector.dbss",
        (ITEM_KEY, ValueField("protect_type", "B", "protectType")),
        RowCount.COUNTED,
        count_key="protectorItems",
    ),
    ValueTable(
        "itemmovedata.bss",
        (
            ValueField(
                "index",
                "B",
                "index",
                NameLookup("filter_name", "moveFilter", move_filter_name, is_row_lookup=True),
            ),
            ValueField("contents_event_type", "H", "contentsEventType", display=contents_event_text),
            ValueField("item_classify", "B", "itemClassify", display=item_classify_text),
            ValueField("item_type", "B", "itemType", display=item_type_text),
            ValueField("exception_filter_name_tag_ref", "I", text=TextRef("exception_filter_name_tag_kr")),
        ),
        RowCount.COUNTED,
        count_key="moveFilters",
    ),
    ValueTable(
        "autousebuffitemcategoryinfo.bss",
        (
            ValueField(
                "category_key",
                "I",
                "categoryKey",
                NameLookup("category_name", "category", auto_use_category_name, is_row_lookup=True),
            ),
            ValueField("category_name_ref", "I", text=TextRef("category_name_kr")),
        ),
        RowCount.COUNTED,
        count_key="autoUseCategories",
    ),
    ValueTable(
        "bootyitemlist.bss",
        (
            ValueField("territory_key", "I", "territoryKey", NameLookup("territory_name", "territory", territory_name)),
            ValueField(
                "booty_item_ids",
                "I",
                "bootyItem",
                display=item_key_entry_text,
                is_counted_list=True,
                count_fmt="Q",
            ),
        ),
        RowCount.COUNTED,
        count_key="bootyLists",
    ),
    ValueTable(
        "notifyexpirationperioditem.bss",
        (ITEM_KEY, ValueField("expiration_period_notify", "I", "expirationPeriodNotify")),
        RowCount.COUNTED,
        count_key="notifyItems",
    ),
)
