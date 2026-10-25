"""Row fields and table columns of the life skill mastery tables.

Every row is an f32 mastery threshold followed by 4-byte fields; only the
fields differ per file. Rates are stored with 1,000,000 = 100%. The gathering
and processing tables hold one row group per type (`sub_types`). Field names
come from the client Lua that reads each table (see
docs/file-formats/bss/masterystatdata_bss.md); fields the Lua does not name are
`unknown_<offset>` and stay out of the table.
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from .alchemy import extra_item_rates
from .sub_types import GATHERING_TYPES, PROCESSING_TYPES, SubTypeLabel


class CellFormat(Enum):
    # A rate shown like PaGlobalFunc_GlobalUtil_RoundRateToSecondPoint: percent, 2 decimals.
    RATE_2 = "rate2"
    # PaGlobalFunc_GlobalUtil_RoundRateToThridPoint: percent, 3 decimals.
    RATE_3 = "rate3"
    # A whole number shown as is, such as a batch count.
    COUNT = "count"


@dataclass(frozen=True)
class ShownColumn:
    field: str
    label_key: str
    cell_format: CellFormat = CellFormat.RATE_2


@dataclass(frozen=True)
class MasteryTable:
    file_name: str
    # Fields after the f32 mastery at +0x00, in row order, each 4 bytes.
    fields: tuple[str, ...]
    # Columns after the Mastery column.
    columns: tuple[ShownColumn, ...]
    # Fields stored as f32; every other field is a u32.
    float_fields: frozenset[str] = frozenset()
    # Extra record fields computed from the parsed row.
    derive: Callable[[dict], dict] | None = None
    # Group index -> type name, for files that hold one row group per type;
    # None for files with a single row list.
    sub_types: dict[int, SubTypeLabel] | None = None

    @property
    def row(self) -> struct.Struct:
        codes = "".join("f" if name in self.float_fields else "I" for name in self.fields)
        return struct.Struct("<f" + codes)


FISHING = MasteryTable(
    file_name="fishingstatdata.bss",
    fields=("rate",),
    columns=(ShownColumn("rate", "prizeCatchRate"),),
)

COOKING = MasteryTable(
    file_name="cookingstatdata.bss",
    fields=(
        "speed_cook_rate",
        "basic_max_drop_rate",
        "add_critical_drop_rate",
        "add_critical_max_drop_rate",
        "add_royal_trade_bonus",
    ),
    columns=(
        ShownColumn("speed_cook_rate", "massCooking"),
        ShownColumn("basic_max_drop_rate", "maxDishes"),
        ShownColumn("add_critical_drop_rate", "higherGradeDish"),
        ShownColumn("add_critical_max_drop_rate", "maxHigherGradeDishes"),
        ShownColumn("add_royal_trade_bonus", "imperialProfit"),
    ),
)

HUNTING = MasteryTable(
    file_name="huntingstatdata.bss",
    fields=(
        "unknown_04",
        "hunting_rate",
        "unknown_0c",
        "unknown_10",
        "unknown_14",
        "unknown_18",
        "unknown_1c",
        "unknown_20",
    ),
    columns=(ShownColumn("hunting_rate", "butcheringRate"),),
)

ALCHEMY = MasteryTable(
    file_name="alchemystatdata.bss",
    fields=(
        "basic_max_drop_rate",
        "add_royal_trade_bonus",
        "unknown_0c",
        "event_drop_rate_0",
        "unknown_14",
        "event_drop_rate_1",
        "unknown_1c",
        "event_drop_rate_2",
        "event_drop_rate",
    ),
    columns=(
        ShownColumn("basic_max_drop_rate", "maxProducts"),
        ShownColumn("extra_basic_item_rate", "extraBasicItems", CellFormat.RATE_3),
        ShownColumn("extra_special_item_rate", "extraSpecialItems", CellFormat.RATE_3),
        ShownColumn("extra_rare_item_rate", "extraRareItems", CellFormat.RATE_3),
        ShownColumn("add_royal_trade_bonus", "imperialProfit"),
    ),
    derive=extra_item_rates,
)

# The eight values from +0x0C follow CppEnums.ServantStatType; the Lua reads
# the first four (getVariedStatByIndex 0 to 3), no UI shows the cannon four.
SAIL = MasteryTable(
    file_name="sailstatdata.bss",
    fields=(
        "unknown_04",
        "unknown_08",
        "acceleration",
        "max_move_speed",
        "cornering_speed",
        "brake_speed",
        "cannon_cool_time",
        "cannon_accuracy",
        "max_length",
        "max_angle",
    ),
    columns=(
        ShownColumn("acceleration", "accel"),
        ShownColumn("max_move_speed", "speed"),
        ShownColumn("cornering_speed", "turn"),
        ShownColumn("brake_speed", "brake"),
    ),
    float_fields=frozenset({"unknown_04"}),
)

# Columns in tooltip order (rate1 to rate3), which differs from row order.
TRAINING = MasteryTable(
    file_name="trainingstatdata.bss",
    fields=("add_horse_capture_rate", "add_mating_rate", "add_vehicle_experience_rate"),
    columns=(
        ShownColumn("add_horse_capture_rate", "horseCaptureRate"),
        ShownColumn("add_vehicle_experience_rate", "mountExp"),
        ShownColumn("add_mating_rate", "higherTierHorse"),
    ),
)

# Pairs of getCollectingStatAddDropRate(i) and getCollectingStatAddDropCountRate(i)
# for the basic, special and rare resources; the Lua does not read the fourth pair.
GATHERING = MasteryTable(
    file_name="collectingstatdata.bss",
    fields=(
        "add_drop_rate_0",
        "add_drop_count_rate_0",
        "add_drop_rate_1",
        "add_drop_count_rate_1",
        "add_drop_rate_2",
        "add_drop_count_rate_2",
        "unknown_1c",
        "unknown_20",
    ),
    columns=(
        ShownColumn("add_drop_rate_0", "basicDropRate"),
        ShownColumn("add_drop_count_rate_0", "basicQuantity"),
        ShownColumn("add_drop_rate_1", "specialDropRate"),
        ShownColumn("add_drop_count_rate_1", "specialQuantity"),
        ShownColumn("add_drop_rate_2", "rareDropRate"),
        ShownColumn("add_drop_count_rate_2", "rareQuantity"),
    ),
    sub_types=GATHERING_TYPES,
)

# count_rate is what ToClient_getManufacturingStatCountRate returns, the
# number of mass processing batches.
PROCESSING = MasteryTable(
    file_name="manufacturingstat.bss",
    fields=("unknown_04", "count_rate", "unknown_0c"),
    columns=(ShownColumn("count_rate", "massProcessBatches", CellFormat.COUNT),),
    sub_types=PROCESSING_TYPES,
)

MASTERY_TABLES: tuple[MasteryTable, ...] = (
    FISHING,
    COOKING,
    HUNTING,
    ALCHEMY,
    SAIL,
    TRAINING,
    GATHERING,
    PROCESSING,
)
