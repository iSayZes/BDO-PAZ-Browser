"""`characterspawntype.dbss`: one row of NPC role flags per character.

    u32 count | count x (u16 character_id | u8[46] role flags)

Each flag byte is 0 or 1 and its index is the client's `CppEnums.SpawnType`
value. Full layout in docs/file-formats/dbss/characterspawntype_dbss.md.
"""

from __future__ import annotations

import struct

_RECORD_SIZE = 48

# CppEnums.SpawnType from luacscript/x64/include/global_define_cpp_enum.luac,
# without the "eSpawnType_" prefix and in the client's spelling. The enum skips
# value 41, which still appears in the data.
SPAWN_TYPE_NAMES: tuple[str, ...] = (
    "NormalNpc", "SkillTrainer", "ItemRepairer", "ShopMerchant", "ImportantNpc",
    "TradeMerchant", "WareHouse", "Stable", "Wharf", "Transfer",
    "Intimacy", "Guild", "Explorer", "Inn", "Auction",
    "Mating", "Potion", "Weapon", "Jewel", "Furniture",
    "Collect", "Fish", "Worker", "Alchemy", "GuildShop",
    "ItemMarket", "TerritorySupply", "TerritoryTrade", "Smuggle", "Cook",
    "PC", "Grocery", "RandomShop", "SupplyShop", "RandomShopDay",
    "FishSupplyShop", "GuildSupplyShop", "GuildStable", "GuildWharf", "PcRoomStable",
    "Instrument", "Unknown41", "TraningVehicleShop", "AbyssOneEnterPosGuide", "ChangeMarniStone",
    "ChurchBuff",
)
ROLE_COUNT = len(SPAWN_TYPE_NAMES)

_RECORD = struct.Struct(f"<H{ROLE_COUNT}s")
assert _RECORD.size == _RECORD_SIZE


def parse_characterspawntype_records(data: bytes) -> list[dict]:
    """Every record in file order: `character_id` and its 46 role flags.

    Raises ValueError when the declared count does not fit the file.
    """
    if len(data) < 4:
        raise ValueError("characterspawntype.dbss is too short for its row count")

    (count,) = struct.unpack_from("<I", data, 0)
    end = 4 + count * _RECORD_SIZE
    if end > len(data):
        raise ValueError(
            f"characterspawntype.dbss declares {count:,} rows but only has room "
            f"for {(len(data) - 4) // _RECORD_SIZE:,}"
        )

    return [
        {"character_id": character_id, "roles": list(roles)}
        for character_id, roles in _RECORD.iter_unpack(data[4:end])
    ]
