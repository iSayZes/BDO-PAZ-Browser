# `guildquest.dbss` Format

## Purpose

The guild missions of the guild quest window (`panel_guildquestlist_all`):
one row per mission with its completion script, Korean title, description
and objective, icon, time limit, the silver it costs to accept, a counted
list of item rewards, its contents groups and its mission type
(Subjugation, Life, Trading or Boss Subjugation). The English texts are LOC
type 27 under the mission number. Companion `guildquestoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes   | Records                     | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ------- | --------------------------- | --------- |
| 2      | 3474 and later | 3474    | `guildquest.dbss`       | 244,538 | 999 Reward Entry, 140 Row   | 178       |
| 2      | 3474 and later | 3474    | `guildquestoffset.dbss` | 1,684   | 140 Offset Row              | 12        |
| 1      | 1784           | 1784    | `guildquest.dbss`       | 567,578 | 2,037 Reward Entry, 339 Row | 188       |
| 1      | 1784           | 1784    | `guildquestoffset.dbss` | 4,072   | 339 Offset Row              | 12        |

| Layout | File                    | Known             | Unknown           |
| ------ | ----------------------- | ----------------- | ----------------- |
| 2      | `guildquest.dbss`       | 105,241 B (43.0%) | 139,297 B (57.0%) |
| 2      | `guildquestoffset.dbss` | 1,684 B (100.0%)  | 0 B (0.0%)        |
| 1      | `guildquest.dbss`       | 265,433 B (46.8%) | 302,145 B (53.2%) |
| 1      | `guildquestoffset.dbss` | 4,072 B (100.0%)  | 0 B (0.0%)        |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                 |
| ----------------------- | -------- | -------------------------------------------------------------------- |
| `guildquestoffset.dbss` | Optional | `quest_no -> (data_offset, data_size)` of every row; the rows carry their own counts and can be walked without it |
| `languagedata_en.loc`   | Optional | Mission texts (type `27`, `str_id1` = `quest_no`), item names (type `0`) and the mission type names (type `37`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `140` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 100 bytes + texts and lists)

Strings are a u64 character count followed by UTF-16LE code units, with no
terminator. Counts in the Notes column are from client 3474.

| Offset                              | Type                                | Field                      | Notes |
| ----------------------------------- | ----------------------------------- | -------------------------- | ----- |
| `+0x00`                             | u32                                 | quest_no                   | Mission number, unique per row; the index key and LOC type 27 `str_id1` |
| `+0x04`                             | str16                               | complete_condition         | Completion script: `killallmonster(1250);`, `gatheritem(6185,0,375);`, `killMonsterGroup(125,10);`, `gatherfishwithgrade(...)`, `barterexchange(...)`, `clearblacktemple(...)` |
| `complete_condition+0x00`           | str16                               | complete_condition_text_kr | Korean objective, e.g. `모든 몬스터 처치;`; LOC type 27 `str_id4` 2 is its translation |
| `complete_condition_text_kr+0x00`   | u16                                 | quest_level                | `1`, `6`, `8`, `12`, `13`, `17` or `18`; see [Mission Levels](#mission-levels) |
| `complete_condition_text_kr+0x02`   | str16                               | title_kr                   | Korean title, e.g. `[토벌] 영예로운 그믐달 길드의 토벌 의뢰` |
| `title_kr+0x00`                     | str16                               | description_kr             | Korean description with PAColor markup |
| `description_kr+0x00`               | str16                               | icon_path                  | `Icon/Quest/0_Guild_Combat.dds` and 14 more paths under `Icon/Quest/0_Guild_` |
| `icon_path+0x00`                    | u32                                 | limit_minute               | Time limit in minutes, `60` to `600` |
| `icon_path+0x04`                    | u32                                 | need_item_key              | Item paid to accept the mission, packed as `enchant_level << 24 \| item_id`; Silver (`1`) on every row |
| `icon_path+0x08`                    | i64                                 | need_item_count            | Amount of `need_item_key`, `10,000` to `200,000` |
| `icon_path+0x10`                    | u8                                  | is_preoccupancy            | `0` on every row |
| `icon_path+0x11`                    | u32                                 | base_reward_count          | `6` to `9` |
| `icon_path+0x15`                    | Reward Entry[base_reward_count]     | base_rewards               | See Reward Entry |
| `base_rewards+0x00`                 | u32                                 | unknown_base_rewards_00    | `0` on every row; see Open Questions |
| `base_rewards+0x04`                 | u32                                 | unknown_base_rewards_04    | `0` on every row |
| `base_rewards+0x08`                 | i64                                 | unknown_base_rewards_08    | `6,300,000` to `7,300,000`; see Open Questions |
| `base_rewards+0x10`                 | u32                                 | contents_group_count       | `1` to `8` |
| `base_rewards+0x14`                 | u32[contents_group_count]           | contents_group_hashes      | `key_hash()` of each contents group key in decimal, as in [`skillsimply.dbss`](skillsimply_dbss.md); see Notes |
| `contents_group_hashes+0x00`        | u8                                  | guild_quest_type           | See [Mission Types](#mission-types) |
| `contents_group_hashes+0x01`        | u32                                 | unknown_value_count        | `0` on 76 rows, `1` on 48, `5` on 16 |
| `contents_group_hashes+0x05`        | u32[unknown_value_count]            | unknown_values             | `5` alone, or `1, 2, 3, 4, 6`; see Open Questions |
| `unknown_values+0x00`               | u32                                 | unknown_after_unknown_values       | `1` on exactly the 64 rows with `unknown_values`, else `0` |
| `unknown_values+0x04`               | u32                                 | unknown_end                | `0` on every row; the row ends here |

### Reward Entry (178 bytes)

The `gc::QuestRewardElement` members of the 2016 client, byte-packed, then
135 bytes this file leaves zero apart from two `16` bytes. See [Field
Names](#field-names) for how the offsets were placed.

| Offset  | Type       | Field                | Notes |
| ------- | ---------- | -------------------- | ----- |
| `+0x00` | u32        | reward_type          | `gc::RewardType`: `0` exp, `1` skill exp, `2` life exp, `3` item, `4` amity; `3` on all 999 entries |
| `+0x04` | i64        | experience           | `0` on every entry |
| `+0x0C` | i32        | skill_experience     | `0` on every entry |
| `+0x10` | i32        | product_experience   | `0` on every entry |
| `+0x14` | u8         | life_experience_type | `15` on every entry |
| `+0x15` | i32        | life_experience      | `0` on every entry |
| `+0x19` | u32        | item_key             | Reward item, packed as `need_item_key`; enchant level `0` on every entry |
| `+0x1D` | i64        | item_count           | Amount of `item_key` |
| `+0x25` | u16        | intimacy_character   | `0` on every entry |
| `+0x27` | i32        | intimacy_value       | `0` on every entry |
| `+0x2B` | bytes[135] | unknown_2b           | Zero apart from `16` at `+0x36` and `+0x67` on every entry; see Open Questions |

### `guildquestoffset.dbss`

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Equals the `guildquest.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer               |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | quest_no    | Key of the row it points at             |
| `+0x04` | u32  | data_offset | Row start in `guildquest.dbss`, at `quest_no` |
| `+0x08` | u32  | data_size   | Size of the whole row                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`.
Neither the index rows nor the data rows are sorted by `quest_no`, and the
two orders differ. Sorted by `data_offset`, the index rows tile
`guildquest.dbss` from `+0x04` to the end of the file with no gap on
clients 1784 and 3474.

## Layout 1

On client 1784 a reward entry is 10 bytes longer, and the row ends with the
boss fields of the source sheet in place of `unknown_values`.

### Row (variable: 100 bytes + texts and lists)

| Offset                              | Type                                | Field                      | Notes |
| ----------------------------------- | ----------------------------------- | -------------------------- | ----- |
| `+0x00`                             | u32                                 | quest_no                   | `1` to `3619` |
| `+0x04`                             | str16                               | complete_condition         | |
| `complete_condition+0x00`           | str16                               | complete_condition_text_kr | |
| `complete_condition_text_kr+0x00`   | u16                                 | quest_level                | `1` on every row |
| `complete_condition_text_kr+0x02`   | str16                               | title_kr                   | |
| `title_kr+0x00`                     | str16                               | description_kr             | |
| `description_kr+0x00`               | str16                               | icon_path                  | `0_Guild_Combat`, `0_Guild_Product` or `0_Guild_Trade` |
| `icon_path+0x00`                    | u32                                 | limit_minute               | |
| `icon_path+0x04`                    | u32                                 | need_item_key              | |
| `icon_path+0x08`                    | i64                                 | need_item_count            | |
| `icon_path+0x10`                    | u8                                  | is_preoccupancy            | |
| `icon_path+0x11`                    | u32                                 | base_reward_count          | |
| `icon_path+0x15`                    | Reward Entry[base_reward_count]     | base_rewards               | |
| `base_rewards+0x00`                 | u32                                 | unknown_base_rewards_00    | `0` on every row |
| `base_rewards+0x04`                 | u32                                 | unknown_base_rewards_04    | `0` on every row |
| `base_rewards+0x08`                 | i64                                 | unknown_base_rewards_08    | `0` to `500,000` |
| `base_rewards+0x10`                 | u32                                 | contents_group_count       | |
| `base_rewards+0x14`                 | u32[contents_group_count]           | contents_group_hashes      | |
| `contents_group_hashes+0x00`        | u8                                  | guild_quest_type           | `0`, `1` or `2` |
| `contents_group_hashes+0x01`        | u32                                 | boss_spawn_type            | `0` on 273 rows, `1` to `5` on the other 66 |
| `contents_group_hashes+0x05`        | u32                                 | boss_spawn_cost            | `1` on the rows with a `boss_spawn_type`, else `0` |
| `contents_group_hashes+0x09`        | u32                                 | unknown_end                | `0` on every row |

### Reward Entry (188 bytes)

| Offset  | Type       | Field                | Notes |
| ------- | ---------- | -------------------- | ----- |
| `+0x00` | u32        | reward_type          | `3` on every entry |
| `+0x04` | i64        | experience           | |
| `+0x0C` | i32        | skill_experience     | |
| `+0x10` | i32        | product_experience   | |
| `+0x14` | u8         | life_experience_type | `15` on every entry |
| `+0x15` | i32        | life_experience      | |
| `+0x19` | u32        | item_key             | |
| `+0x1D` | i64        | item_count           | |
| `+0x25` | u16        | intimacy_character   | |
| `+0x27` | i32        | intimacy_value       | |
| `+0x2B` | bytes[145] | unknown_2b           | Zero apart from `16` at `+0x36` and `+0x67` on every entry |

## Mission Types

`guild_quest_type` picks the tab of the guild mission list. In
`panel_guildquestlist_all_2.luac`, `HandleEventLUp_GuildQuest_SelectType`
turns tab 1 to 3 into type 0 to 2 and the last tab (4) into type 4, and
`HandleEventOnOut_GuildQuest_Type_ShowSimpleTooltip` names each tab with a
`RESOURCE` sheet key. No tab shows type `3`. Counts and names from client 3474:

| Value | `RESOURCE` key                          | Tab name         | Rows | Completion scripts |
| ----- | --------------------------------------- | ---------------- | ---- | ------------------ |
| `0`   | `PANEL_GUILDQUEST_QUESTTYPE_BATTLE`     | Subjugation      | 32   | `killallmonster`, `killMonsterGroup` |
| `1`   | `PANEL_GUILDQUEST_QUESTTYPE_LIFE`       | Life             | 64   | `gatheritem`, `gatherfishwithgrade` |
| `2`   | `PANEL_GUILDQUEST_QUESTTYPE_TRADE`      | Trading          | 16   | `barterexchange` |
| `4`   | `PANEL_GUILDQUEST_QUESTTYPE_BOSSBATTLE` | Boss Subjugation | 28   | `clearblacktemple` |

Client 1784 has types `0` (226 rows), `1` (64) and `2` (49), the last with
45 `exchangeitem` delivery scripts and 4 `barterexchange` ones.

## Mission Levels

On client 3474 each mission type uses four `quest_level` values with the
same number of rows each: `1`, `8`, `13` and `18` for Subjugation, Trading
and Boss Subjugation, `1`, `6`, `12` and `17` for Life. Within a series
the level rises with the objective, for example `killallmonster(1250)` and
`(2500)` at `1`, `(3750)` and `(5000)` at `8`.

The mission grade that `getGuildQuestGrade()` returns (`1` to `4`, Small
to Extra Large) is the rank of `quest_level` within its type: the lowest
level is Small, the highest Extra Large. I checked in game that the grade
in the guild mission window follows the level tier.

## Field Names

The names follow the 2016 `gc::GuildQuestStaticStatus` and the
`GuildQuest_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784. The 2016 struct lists `_completeConditionString`,
`_completeConditionText`, `_activityPerDemand`, `_rewardGroup`,
`_questLevel` (`unsigned short`), `_questName`, `_questDesc`, `_questIcon`,
`_limitMinute`, `_itemKey`, `_itemCount` (`__int64`), `_isPreoccupancy`
(`bool`), `_expectedPrice`, `_restricted`, `_questNo` and
`_contentsGroupKey`. The row stores the strings, `quest_level` and the
accept fields in that order; `quest_level` is the only u16 and
`is_preoccupancy` the only u8 of the struct in their places.

All 339 rows of client 1784 are in the sheet (762 rows), and the file
matches it on all 339 for these columns:

| Field                      | Sheet column            | Notes |
| -------------------------- | ----------------------- | ----- |
| `quest_no`                 | `GuildQuestNo`          | |
| `complete_condition`       | `CompleteCondition`     | Line breaks aside |
| `complete_condition_text_kr` | `CompleteConditionText` | Line breaks aside |
| `quest_level`              | `QuestLv`               | `1` on every row of both |
| `title_kr`                 | `Title`                 | |
| `description_kr`           | `Desc`                  | Line breaks aside |
| `icon_path`                | `QuestIcon`             | |
| `limit_minute`             | `LimitMinute`           | |
| `need_item_key`            | `NeedItemKey`           | `1` on every row of both |
| `need_item_count`          | `NeeItemCount`          | |
| `is_preoccupancy`          | `Preoccupancy`          | `0` on every row of both |
| `contents_group_hashes`    | `ContentsGroupKey`      | The comma list, hashed, in sheet order |
| `guild_quest_type`         | `GuildQuestType`        | |
| `boss_spawn_type`          | `BossSpawnType`         | Empty in the sheet where the file has `0` |
| `boss_spawn_cost`          | `BossSpawnCost`         | Empty in the sheet where the file has `0` |

`base_rewards` is the sheet's `Reward` script, `item(item_id,enchant,count);`
per reward: on all 339 rows every file reward is in the script, which lists
1 to 4 more items than the file (a private server's edits). The sheet's
`ActivityPerDemand` (`200` on row 1) and `ExpectedPrice` (empty on every
row) match no field.

The Reward Entry fields are the `gc::QuestRewardElement` members in order,
pointers dropped and no padding: `_type`, `_experience` (`__int64`),
`_skillExperience`, `_productExperience`, `_lifeExperienceType` (one
byte), `_lifeExperience`, `_itemEnchantKey`, `_itemCount` (`__int64`),
`_intimacyCharacter` (`unsigned short`) and `_intimacyValue`. The same
178-byte entry holds the rewards of [`quest.dbss`](quest_dbss.md), where
every reward type is used: on client 3474 its type `0` entries hold their
value at `+0x04`, type `1` at `+0x0C`, type `2` its life skill at `+0x14`
and its amount at `+0x15`, type `3` at `+0x19` and `+0x1D`, and type `4` at
`+0x25` and `+0x27`, the offsets these sizes give. The enum values are the
2016 `gc::RewardType` (`eRewardItem` = `3`). `life_experience_type` is `15`
on every entry of a type other than `2` in both files. The client Lua reads
the entries through `getGuildQuestBaseRewardAt()`, `getType()`
(`__eRewardItem`), `getItemEnchantKey()` and `getItemCount()`.

calpheonlabs (`guildquest.dbss.mdx`, capture PAZ 3595) starts each reward 4
bytes later and reads the `03` that opens the next entry as a trailing
"controlCode174" of 0 or 3; the `gc::RewardType` enum and the
`quest.dbss` entries put `reward_type` at `+0x00`.

## Localization

LOC type 27 holds the mission texts under `str_id1` = `quest_no`, with
`str_id4` `0` the title, `1` the description and `2` the objective. All 140
missions of client 3474 have the three, for example 5001: `[Subjugation]
Glorious Old Moon Guild's Monster Mission`, `Defeat any monster;`. The
type has 1,097 missions on client 3474, more than the file holds.

## Notes

- Contents group `1177` is in the list of exactly the 56 missions with a
  `0_Guild_Honor_` icon and a `Glorious` title (`quest_no` 5001 to 6008 on
  client 3474), and `863` in that of exactly the 28 Boss Subjugation
  missions. `panel_guildquestlist_all_1.luac` shows a mission with
  `isGuildHonorBenefitQuest()` only when `_ContentsGroup_GuildHonorSystem`
  is on and the guild's honor points unlock it.
- Every contents group hash decodes to a key below `0x10000` on clients
  1784 and 3474 (`contents_group_key()` in `_common/contents_group.py`).
- Client 1784 has 339 rows, client 3474 140; no `quest_no` is in both.
- The mission list Lua names the guild size of a mission with
  `getGuildQuestGrade()` (`1` Small to `4` Extra Large, `GAME` keys
  `LUA_GUILD_QUEST_SMALL` to `LUA_GUILD_QUEST_BIGGEST`). No row field holds
  `1` to `4`.

## Open Questions

### Fields After the Rewards

In the 2016 `gc::QuestRewardGroup`, `_baseReward` is followed by
`_selectReward` (a second reward list) and `_expectedPrice` (`__int64`).
`unknown_base_rewards_00` would be the select reward count if the file
followed that order, but it is `0` on every row of both clients, and the
Lua's `ToClient_getCurrentGuildQuestSelectRewardCount()` cannot be checked
against a filled list. `unknown_base_rewards_08` holds `100,000` to
`500,000` on client 1784 where the sheet's `ExpectedPrice` is empty, so
the name does not carry over from the sheet; it does not follow
`need_item_count` or the silver reward either.

### `unknown_values`

The list holds `1, 2, 3, 4, 6` on 16 Subjugation rows (`killallmonster`)
and `5` on 48 rows (the `killMonsterGroup` Subjugation, the fishing Life
and the Trading missions); the other rows have none, and
`unknown_after_unknown_values` is `1` exactly when the list has values. calpheonlabs
reads the list as region groups, `5` the sea, and the flag as "has region
restriction". No client Lua or enum names the values, and the client 1784
rows end with `boss_spawn_type` and `boss_spawn_cost` here instead.

### `unknown_end`

The last u32 is `0` on every row of both clients. The sheet's last column,
`IsMainQuest`, is empty on every row, so a match says nothing.

### Reward Entry Tail

After `intimacy_value` the entry holds 135 bytes (145 on client 1784) that
the 2016 struct has no member for. Every guild mission entry has `16` at
`+0x36` and `+0x67`; [`quest.dbss`](quest_dbss.md) reads `+0x67` as its
Family stat type, where `16` is no stat.
