"""Layouts of the Edania tables that fit the PABR value tables.

`edaniaetcoptionstaticstatus.bss` and `edaniapvpdayoptionstaticstatus.bss`
nest their lists and have their own handlers; `edaniaregioninfo.bss` too.
"""

from __future__ import annotations

from _common.node import node_name
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable


EDANIA_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "edanacastleinfostaicstatusmanager.bss",
        (
            ValueField("mark_texture_ref", "I", text=TextRef("mark_texture", "markTexture")),
            ValueField("x", "f", "x"),
            ValueField("z", "f", "z"),
            ValueField("node_key", "I", "nodeKey", NameLookup("node_name", "node", node_name)),
        ),
        RowCount.TO_TABLE_START,
        count_key="edaniaCastles",
        first_fields=("node_key",),
    ),
)
