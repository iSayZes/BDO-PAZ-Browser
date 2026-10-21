"""`CppEnums.ContentsEventType` names: what using an item does (`contents_event_type`).

Member names in value order from `0`, from
`luacscript/x64/include/global_define_cpp_enum.luac` on client 3474, without
the `ContentsType_` prefix (`68` to `70` spell it `ContenteType_`). The enum
ends at `86`; items also store values up to `170`, which show as the bare
number. See itemenchant_dbss.md.
"""

from __future__ import annotations

# contents_event_type on items whose use does nothing.
NO_CONTENTS_EVENT = 171
# Soul collectors (Marni's Stones): param1 is a characterstatic.dbss
# character_group, param2 the kill count. See Soul Collectors in itemenchant_dbss.md.
CONTENTS_EVENT_SOUL_COLLECT = 59

CONTENTS_EVENT_TYPE_NAMES: tuple[str, ...] = (
    "Housing",
    "SkillInitialize",
    "NpcWorker",
    "Mail",
    "GuildMark",
    "Campfire",
    "ItemBox",
    "ChangeServantName",
    "ChangeServantSkill",
    "CollectByTool",
    "CarveSeal",
    "ResetSeal",
    "PetRegister",
    "PetFeed",
    "ClearVested",
    "Respawn",
    "OrderToServant",
    "NpcWorkerRecovery",
    "ChangeNickName",
    "ClearServantDeadCount",
    "ClearServantMatingCount",
    "ImprintServant",
    "Roulette",
    "RemoveKnowledge",
    "HelpReward",
    "SummonCharacter",
    "ReleaseImprintServant",
    "HelpEndurance",
    "TransferLifeExperience",
    "ChangeFormServant",
    "ItemChange",
    "CustomizedItemBox",
    "AlchemyStone",
    "ServantSkillExpTraining",
    "ConvertEnchantFailCountToItem",
    "ConvertEnchantFailItemToCount",
    "ForgetServantSkill",
    "Rubbing",
    "ItemExchangeToClass",
    "AddGuildQuestReward",
    "SellWarehouseItemToSystem",
    "PetChangeLook",
    "LanternAttribute",
    "Seal",
    "SkillAwakeningPeriod",
    "Banquet",
    "ChannelBattleExpItem",
    "Warp",
    "ExchangeBattleAndSkillExp",
    "SealItemBox",
    "SealItemBoxKey",
    "InventoryBag",
    "PetPromotion",
    "ClearGuildSkill",
    "Coupon",
    "ServantRespawn",
    "ServantRepairKit",
    "CampingTent",
    "ClearWorkerUpgradePoint",
    "SoulCollect",
    "CampingTentShop",
    "VillaKey",
    "QuestBook___Release",
    "FairyRebirth",
    "FairyRegister",
    "WeakenEnchant",
    "MaidRegister",
    "ServantTransform",
    "SetBeginningLevelServant",
    "Release",
    "Release2",
    "DetectUser",
    "ExchangeCharacterName",
    "Grenade",
    "Emoticon",
    "BattleRoyalePrivateGameTicket",
    "NationSiegeRevivePoint",
    "Reserve3",
    "SavageDefenceDirectJoinItem",
    "SavageDefenceReGameTicket",
    "EmployeeSlot",
    "ChangeBarterInfo",
    "Employee",
    "FairyChangeLook",
    "AddBarterCount",
    "ChangeFairySkill",
    "MusicIncreaseExp",
)


def contents_event_text(contents_event_type: int) -> str:
    """`59 SoulCollect`, or the bare value past the end of the enum."""
    if 0 <= contents_event_type < len(CONTENTS_EVENT_TYPE_NAMES):
        return f"{contents_event_type} {CONTENTS_EVENT_TYPE_NAMES[contents_event_type]}"
    return str(contents_event_type)
