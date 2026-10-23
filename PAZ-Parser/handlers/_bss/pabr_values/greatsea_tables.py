"""Layouts of the Great Ocean tables that fit the PABR value tables.

`greatseaevent.dbss` has an offset file and is not one of them.
"""

from __future__ import annotations

from _common.vehicle_type import vehicle_type_text
from .fields import CHARACTER_KEY, ITEM_ID, MAP_COLOR
from .layout import RowCount, ValueField, ValueTable, unknown_fields


GREAT_SEA_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "greatsea.bss",
        (
            MAP_COLOR,
            *unknown_fields((0x03, "B"), (0x04, "3s"), (0x07, "B")),
            ValueField("x", "f", "x"),
            ValueField("y", "f", "y"),
            ValueField("z", "f", "z"),
            ValueField("magnification", "f", "magnification"),
            ValueField(
                "vehicle_types",
                "B",
                "vehicleTypes",
                display=vehicle_type_text,
                is_counted_list=True,
                count_fmt="Q",
            ),
            ValueField("restricted_area_state", "B", "restrictedAreaState"),
            ValueField("wind_impact", "I", "windImpact"),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    # The IslandExplore_Option columns of a private server on client 1784
    # (greatseaoption_bss.md, Field Names).
    ValueTable(
        "greatseaoption.bss",
        (
            ValueField("food_consume", "I", "foodConsume"),
            ValueField("explore_cool_time", "I", "exploreCoolTime"),
            ValueField("ship_management_range", "f", "shipManagementRange"),
            ValueField("barter_range", "f", "barterRange"),
            ValueField("reset_cool_time", "B", "resetCoolTime"),
            ValueField("unknown_15", "B"),
            ValueField("max_exchange_count", "I", "maxExchangeCount"),
            ValueField("over_max_count", "I", "overMaxCount"),
            ValueField("max_reset_count", "I", "maxResetCount"),
            ValueField("barter_reset_time", "H", "barterResetTime"),
            ValueField("discount_rate", "I", "discountRate"),
            ValueField("add_reset_count", "I", "addResetCount"),
            ValueField("reset_need_count", "I", "resetNeedCount"),
            ValueField("time_discount", "I", "timeDiscount"),
            ValueField("time_discount_limit", "I", "timeDiscountLimit"),
            ValueField("sub_employee_exp", "I", "subEmployeeExp"),
            ValueField("unknown_3c", "I"),
            ValueField("sub_trade_exp", "I", "subTradeExp"),
            *unknown_fields((0x44, "I"), (0x48, "I")),
        ),
    ),
    # The Epheria Carracks that can turn back into their Ship License, with
    # the silver fee of ToClient_oceanShipChangeItemFeeMoney().
    ValueTable(
        "oceanshipchangeitemstaticstatus.bss",
        (CHARACTER_KEY, ITEM_ID),
        RowCount.COUNTED,
        count_key="ships",
        head=(ValueField("fee_money", "I", "feeMoney"),),
    ),
)
