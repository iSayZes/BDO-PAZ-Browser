# `oceansiegereward.bss` Format

## Purpose

The Blue Battlefield (ocean siege) rewards: per row a u16, five reward
sets of four item lists each, one more item list and two skill keys. On
client 3482 the one row's sets hand out an Oceanstrider (Tier 3, sets 1
to 3), Oceanbreaker (Tier 4) or Oceanlord (Tier 5) Triumph Box with two
Combat Secret Books (M), 1,000 Crow Coins, three Secret Books of Florin
and an Oceanlord Triumph Box of Resilience; the last list a Waveworn
Resolve Box with two Combat Secret Books (S). The skills are Glorious
Life (Standard) and (Basic).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ----------------------- | --------- |
| 2      | 3474 and later | 3482    | `oceansiegereward.bss` | 630   | 27 Reward, 5 Reward Set | 16        |
| 1      | 3251           | 3251    | `oceansiegereward.bss` | 282   | 21 Reward, 5 Reward Set | 12        |

| Layout | File                   | Known         | Unknown       |
| ------ | ---------------------- | ------------- | ------------- |
| 2      | `oceansiegereward.bss` | 352 B (55.9%) | 278 B (44.1%) |
| 1      | `oceansiegereward.bss` | 280 B (99.3%) | 2 B (0.7%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2765   | No file  |
| 2637   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), skill names (LOC type 10) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `1` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 18 bytes + reward sets and rewards)

| Offset                 | Type                         | Field                | Notes                                                              |
| ---------------------- | ---------------------------- | -------------------- | ------------------------------------------------------------------ |
| `+0x00`                | u16                          | unknown_00           | `0`; see Open Questions                                            |
| `+0x02`                | Reward Set[5]                | reward_sets          | See Reward Set and Reward Sets                                     |
| `reward_sets+0x00`     | u64                          | unknown_reward_count | Number of `unknown_rewards`                                        |
| `reward_sets+0x08`     | Reward[unknown_reward_count] | unknown_rewards      | The Waveworn Resolve Box and its books on client 3482              |
| `unknown_rewards+0x00` | u32                          | skill_key_1          | Skill number, LOC type 10 name; `47462` Glorious Life (Standard)   |
| `unknown_rewards+0x04` | u32                          | skill_key_2          | `47463` Glorious Life (Basic)                                      |

### Reward Set (variable: 32 bytes + rewards)

| Offset                   | Type                           | Field                  | Notes                                     |
| ------------------------ | ------------------------------ | ---------------------- | ----------------------------------------- |
| `+0x00`                  | u64                            | unknown_reward_count_1 | Number of `unknown_rewards_1`             |
| `+0x08`                  | Reward[unknown_reward_count_1] | unknown_rewards_1      | A Triumph Box and Combat Secret Books     |
| `unknown_rewards_1+0x00` | u64                            | unknown_reward_count_2 | Number of `unknown_rewards_2`             |
| `unknown_rewards_1+0x08` | Reward[unknown_reward_count_2] | unknown_rewards_2      | Bundle of 1,000 Crow Coins                |
| `unknown_rewards_2+0x00` | u64                            | unknown_reward_count_3 | Number of `unknown_rewards_3`             |
| `unknown_rewards_2+0x08` | Reward[unknown_reward_count_3] | unknown_rewards_3      | Secret Book of Florin                     |
| `unknown_rewards_3+0x00` | u64                            | unknown_reward_count_4 | Number of `unknown_rewards_4`             |
| `unknown_rewards_3+0x08` | Reward[unknown_reward_count_4] | unknown_rewards_4      | Oceanlord Triumph Box of Resilience       |

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                              |
| ------- | -------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name  |
| `+0x04` | bytes[4] | unknown_04 | `A4 00 00 00` on every reward of client 3482; see Notes            |
| `+0x08` | u64      | count      | How many of the item                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (262 bytes)

| Offset  | Type          | Field           | Notes                     |
| ------- | ------------- | --------------- | ------------------------- |
| `+0x00` | u16           | unknown_00      | `0`                       |
| `+0x02` | Reward Set[5] | reward_sets     | See Reward Set            |
| `+0xF2` | Reward        | unknown_rewards | One item, no count before |
| `+0xFE` | u32           | skill_key_1     |                           |
| `+0x102` | u32          | skill_key_2     |                           |

### Reward Set (48 bytes)

| Offset  | Type   | Field             | Notes |
| ------- | ------ | ----------------- | ----- |
| `+0x00` | Reward | unknown_rewards_1 |       |
| `+0x0C` | Reward | unknown_rewards_2 |       |
| `+0x18` | Reward | unknown_rewards_3 |       |
| `+0x24` | Reward | unknown_rewards_4 |       |

### Reward (12 bytes)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id |       |
| `+0x04` | u64  | count   |       |

## Reward Sets

Client 3482; the names are LOC type 0. The sets differ in the box of
`unknown_rewards_1` only:

| Set     | `unknown_rewards_1`                                             |
| ------- | --------------------------------------------------------------- |
| 1 to 3  | Oceanstrider Triumph Box (Tier 3) x1, Combat Secret Book (M) x2 |
| 4       | Oceanbreaker Triumph Box (Tier 4) x1, Combat Secret Book (M) x2 |
| 5       | Oceanlord Triumph Box (Tier 5) x1, Combat Secret Book (M) x2    |

In every set `unknown_rewards_2` holds Bundle of 1,000 Crow Coins x1,
`unknown_rewards_3` Secret Book of Florin x3 and `unknown_rewards_4`
Oceanlord Triumph Box of Resilience x1. `unknown_rewards` holds Waveworn
Resolve Box x1 and Combat Secret Book (S) x2.

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it, and no Lua function of client 3482 reads its rewards
(the result window shows the reward item the server sends). The reward
entries have the shape of the rewards of
[`rosewarrewardstaticstatus.bss`](rosewarrewardstaticstatus_bss.md), whose
names they take: every `item_id` is an item with a LOC type 0 name, the
count a plain number. `skill_key_1` and `skill_key_2` are skill numbers:
`47462` and `47463` are 영예로운 생활 (하) and (최하), Glorious Life
(Standard) and (Basic) in LOC type 10, and the land siege table
`siege2024rewardstaticstatus.bss`, which has the same row shape, ends its
three rows with the pairs of 영예로운 전투, 생활 (Glorious Combat, Life)
`58478, 58479`, `58477, 58478` and `58475, 58476`. What each list and each
skill is for stays open.

## Notes

- Client 3251 uses Layout 1, one item per list with no counts (282
  bytes): the same boxes, Crow Coins and Florin books, without the Combat
  Secret Books, and the same two skills. Client 3474 turns each list into
  a counted list. The file is not in the archives of client 1784.
- The LOC text of every Triumph Box and of the Triumph Box of Resilience
  says it is "issued to those who achieve glorious victory on the Blue
  Battlefield"; the Waveworn Resolve Box text says "to those whose
  maritime resolve remained determined throughout".
- `unknown_04` is `A4 00 00 00` on all 27 rewards of client 3482, where
  `rosewarrewardstaticstatus.bss` has `FC 7F 00 00` and
  `siege2024rewardstaticstatus.bss` has `A4 00 00 00` too: the upper half
  of an 8-byte slot the item ID sits in, not cleared by the tool that
  wrote the file.
- The handler (`_bss/oceansiegereward/`) shows one row per reward item:
  the item with its icon, name and count, its set (1 to 5, empty for
  `unknown_rewards`), its list (1 to 4) and the row's two skills, in file
  order. It previews `siege2024rewardstaticstatus.bss` the same way; both
  read their rewards with `_common/reward_items.py`.

## Open Questions

### What the Sets and Lists Stand For

The five sets differ only in the first list's box tier (3, 3, 3, 4, 5 on
client 3482); in `siege2024rewardstaticstatus.bss` the same five sets
step through Determined Triumph Reward Tier 1 to 5. A set per result rank
or per number of held days fits, and the four lists per set may be for
different roles, but nothing names them. `unknown_rewards`, with a
Resolve Box, fits a defeat reward.

### The u16 and the Two Skills

`unknown_00` is `0` on the one row; in `siege2024rewardstaticstatus.bss`
the three rows hold `0`, `1` and `2`, which fits the siege group index:
`panel_window_villagesiegemenu_all.luac` (client 3482) has three land
groups in `_eTerritoryGroupType` and one ocean group in
`_eTerritoryOceanGroupType`. Which of the two skills goes to whom is
open.
