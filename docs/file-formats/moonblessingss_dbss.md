# `moonblessingss.dbss` Format

## Purpose

The Moon's Blessing events of the Pearl Shop: per event its period, the
Pearl total of its top level, a Korean description and its levels. Each
level has a Korean title (`800펄 사용`, "use 800 Pearls"), its item rewards
as quest reward entries and the Pearls spent that unlock it.
`panel_ingamecashshop_moonblessing_renew_all_1.luac` shows the levels
through `ToClient_GetMoonBlessingRewardAt()` (`getTitle()`,
`getBaseRewardCount()`, `getBaseRewardAt(i)`, `getTargetUsedPearl()`) and
the event text through `ToClient_GetMoonBlessingDesc()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records                            | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | ---------------------------------- | --------- |
| 1      | 3002 and later | 3482    | `moonblessingss.dbss` | 46,627 | 221 Reward Entry, 92 Level, 11 Row | 178       |

| Layout | File                  | Known            | Unknown          |
| ------ | --------------------- | ---------------- | ---------------- |
| 1      | `moonblessingss.dbss` | 33,334 B (71.5%) | 13,293 B (28.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Item names (LOC type 0)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 41 bytes + description and levels)

| Offset                | Type               | Field                     | Notes                                                                                |
| --------------------- | ------------------ | ------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`               | u16                | key                       | Row key; `1` to `14` on client 3482, `7` to `9` missing                               |
| `+0x02`               | u64                | start_time                | Unix seconds (UTC); the start date the description names on 10 of 11 rows (client 3482) |
| `+0x0A`               | u64                | end_time                  | Unix seconds (UTC), after `start_time` on every row                                   |
| `+0x12`               | u64                | max_used_pearl            | Equals the last level's `target_used_pearl` on all 11 rows (client 3482); see Field Names |
| `+0x1A`               | u16                | unknown_1a                | `2` on the rows with 7 levels, `4` on those with 8 or 9 (client 3482); see Open Questions |
| `+0x1C`               | str16              | description_kr            | Korean period and rules text with `<PAColor>` tags; `ToClient_GetMoonBlessingDesc()`   |
| `description_kr+0x00` | u8                 | unknown_description_kr_00 | `1` on every row (clients 3002 to 3482)                                               |
| `description_kr+0x01` | u32                | level_count               | Number of `levels`; 7 to 9                                                            |
| `description_kr+0x05` | Level[level_count] | levels                    | See Level                                                                            |

### Level (variable: 22 bytes + title and rewards)

| Offset              | Type                       | Field             | Notes                                                                 |
| ------------------- | -------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`             | str16                      | title_kr          | Korean level title, `<n>펄 사용`; `getTitle()`                         |
| `title_kr+0x00`     | u32                        | reward_count      | Number of `base_rewards`; `getBaseRewardCount()`                       |
| `title_kr+0x04`     | Reward Entry[reward_count] | base_rewards      | See Reward Entry; `getBaseRewardAt(i)`                                 |
| `base_rewards+0x00` | u16                        | level_no          | The level's 1-based position in the row, on every level (client 3482) |
| `base_rewards+0x02` | u64                        | target_used_pearl | Pearls spent that unlock the level, rising level by level; `getTargetUsedPearl()` |

### Reward Entry (178 bytes)

The 178-byte entry of the [`quest.dbss` Reward Entry](quest_dbss.md#reward-entry-178-bytes),
read by `_common/quest/reward_entry.py`. On client 3482 all 221 entries
are items (type `3`) and hold the values of the guild mission entries of
[`guildquest.dbss`](guildquest_dbss.md#reward-entry-178-bytes) outside the
item fields.

| Offset  | Type      | Field                | Notes |
| ------- | --------- | -------------------- | ----- |
| `+0x00` | u32       | reward_type          | `gc::RewardType`; `3` (item) on every entry of client 3482 |
| `+0x04` | i64       | experience           | `0` on every entry |
| `+0x0C` | i32       | skill_experience     | `0` on every entry |
| `+0x10` | i32       | product_experience   | `0` on every entry |
| `+0x14` | u8        | life_experience_type | `15` on every entry |
| `+0x15` | i32       | life_experience      | `0` on every entry |
| `+0x19` | u32       | item_key             | Reward item, packed as `enchant_level << 24 \| item_id`; `getItemEnchantKey()` |
| `+0x1D` | i64       | item_count           | Amount of `item_key` |
| `+0x25` | u16       | intimacy_character   | NPC of an Amity reward; `getIntimacyCharacter()`; `0` on every entry |
| `+0x27` | i32       | intimacy_value       | `0` on every entry |
| `+0x2B` | i32       | mental_card_key      | `0` on every entry |
| `+0x2F` | bytes[2]  | unknown_2f           | Zero on every entry |
| `+0x31` | u8        | exp_grade            | `0` on every entry |
| `+0x32` | bytes[4]  | unknown_32           | Zero on every entry |
| `+0x36` | bytes[49] | unknown_36           | u32 `16`, then 45 zero bytes, on every entry |
| `+0x67` | bytes[53] | family_stat          | The `quest.dbss` [Family Stat Union](quest_dbss.md#family-stat-union-53-bytes); `family_stat_type` `16` (no stat) on every entry |
| `+0x9C` | bytes[4]  | unknown_9c           | Zero on every entry |
| `+0xA0` | u32       | max_fever_point      | `0` on every entry |
| `+0xA4` | u32       | add_fever_point      | `0` on every entry |
| `+0xA8` | u8        | unknown_a8           | `0` on every entry |
| `+0xA9` | u8        | season_no            | `0` on every entry |
| `+0xAA` | i64       | explore_exp          | `0` on every entry; ends the entry |

## Field Names

The Moon's Blessing is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it. The level and reward names are the getters of
`panel_ingamecashshop_moonblessing_renew_all_1.luac` (client 3482).
`max_used_pearl` follows `ToClient_GetCurrentMoonblessingMaxUsedPearl()`,
which the same Lua multiplies by the reset count for the progress bar; the
field equals the top level's target on all 11 rows. `start_time` and
`end_time` are named by their values: Unix seconds at 09:00 or 10:00 UTC
on maintenance days, and on 10 of 11 rows `start_time` is the start date of
the description (`기간 : 2025년 3월 13일 정기 점검 후 ~ ...`). Row 1 runs
from 2025-02-20 to 2025-02-23 while its text names 27 February to
20 March 2025.

## Notes

- Client 3002 has 4 rows, 3251 has 7, 3474 and 3482 have 11; clients 2765
  and older do not ship the file. The layout is the same on all of them.
- The handler (`_dbss/moonblessingss/`) shows one row per level, in file
  order, with its event's key, period, top target and description and the
  level's rewards as item icons with counts.

## Open Questions

### What `unknown_1a` and `unknown_description_kr_00` Hold

`unknown_1a` is `2` on the three 2025 rows with 7 levels and `4` on the
eight rows with 8 or 9; the Lua reads a reset count and its maximum
(`ToClient_GetCurrentMoonblessingResetCount()`,
`ToClient_GetCurrentMoonblessingMaxResetCount()`), and the maximum fits,
but the descriptions do not state a number to check it against.
`unknown_description_kr_00` is `1` on every row of every client checked.
