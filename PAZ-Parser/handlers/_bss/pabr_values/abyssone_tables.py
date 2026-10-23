"""Layouts of the Magnus (`AbyssOne`) tables that fit the PABR value tables.

The four files have no PABR magic: a u32 count, then the rows.
`abyssoneaudioinfo.bss` is not one of them.
"""

from __future__ import annotations

from _common.knowledge import knowledge_name
from _common.town import town_name
from .abyssone_names import equip_slot_text, move_text, preset_text
from .layout import Framing, NameLookup, RowCount, ValueField, ValueTable, unknown_fields


ABYSS_ONE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "abyssonewarehouse.bss",
        (
            ValueField("region_key", "H", "regionKey", NameLookup("region_name", "region", town_name)),
            ValueField("knowledge_key", "I", "knowledgeKey", NameLookup("knowledge_name", "knowledge", knowledge_name)),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "abyssStorages",
    ),
    ValueTable("abyssonecoin.bss", unknown_fields((0x00, "H"), (0x02, "Q")), RowCount.COUNTED, Framing.BARE),
    ValueTable(
        "abyssoneequipmentpreset.bss",
        (
            ValueField("equip_slot", "B", "equipSlot", display=equip_slot_text),
            # class_type, unknown_01 (the row's equip_slot), unknown_02, item_key, unknown_07, abyss_coin.
            ValueField("presets", "BBBIiQ", "presets", display=preset_text, is_counted_list=True),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "equipSlots",
    ),
    ValueTable(
        "abyssmovecost.bss",
        # move_cost, region_key_1, region_key_2.
        (ValueField("moves", "QHH", "moves", display=move_text, is_counted_list=True),),
        RowCount.COUNTED,
        Framing.BARE,
    ),
)
