"""Layouts of the mount tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/bss/<stem>_bss.md`. The names follow the
sheets of a private server's `DataSheets.bexcel` on client 1784:
`HorseRace_CourseSpeed` (`horsemap.bss`), `ServantFantasy_Table`
(`servantfantasymix.bss`), `VehicleTrainingSkill_Item_Table`
(`vehicletraining.bss`) and `VehicleTypeName_Table` (`vehicletypename.bss`).
`delegateservant.bss` has no sheet; its view follows the Pearl Shop getter
`getDelegateServantKey(servantKind)` of the client Lua.
"""

from __future__ import annotations

from _common.character import character_name
from _common.rate import rate_percent
from .fields import CHARACTER_KEY, CHARACTER_NAME, ITEM_KEY, MAP_COLOR
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable
from .names import vehicle_skill_name
from .servant_names import servant_kind_text


def _character_key(prefix: str, column: str) -> ValueField:
    """A u16 character key with its LOC name, as `<prefix>_character_key`."""
    return ValueField(
        f"{prefix}_character_key",
        "H",
        f"{column}Id",
        NameLookup(f"{prefix}_character_name", column, character_name),
    )


SERVANT_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "horsemap.bss",
        (
            MAP_COLOR,
            ValueField("unknown_03", "B"),
            ValueField("map_color_dup", "3s"),
            ValueField("unknown_07", "B"),
            ValueField("horse_speed_apply_rate", "I", "horseSpeedApplyRate", display=rate_percent),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "servantfantasymix.bss",
        (
            _character_key("male", "maleCharacter"),
            _character_key("female", "femaleCharacter"),
            ValueField("result_character_count", "I", "resultCharacterCount"),
            _character_key("upgrade", "upgradeCharacter"),
            ValueField("upgrade_rate", "I", "upgradeRate", display=rate_percent),
        ),
        RowCount.COUNTED,
        count_key="fantasyMixPairs",
    ),
    ValueTable(
        "delegateservant.bss",
        (CHARACTER_KEY,),
        RowCount.TO_TABLE_START,
        count_key="servantKinds",
        index_column="servantKind",
        index_display=servant_kind_text,
    ),
    ValueTable(
        "vehicletraining.bss",
        (
            ITEM_KEY,
            ValueField("item_key_dup", "I"),
            ValueField("skill_key", "B", "skillId", NameLookup("skill_name", "skill", vehicle_skill_name)),
            ValueField("experience", "I", "experience"),
            ValueField("desc_ref", "I", text=TextRef("desc_kr", "description")),
            ValueField("unknown_11", "I"),
        ),
        RowCount.COUNTED,
        count_key="trainingItems",
    ),
    ValueTable(
        "vehicletypename.bss",
        (
            ValueField("character_key", "I", "characterId", CHARACTER_NAME),
            ValueField("vehicle_type_name_ref", "I", text=TextRef("vehicle_type_name", "vehicleTypeName")),
        ),
        RowCount.COUNTED,
        count_key="vehicleCharacters",
    ),
)
