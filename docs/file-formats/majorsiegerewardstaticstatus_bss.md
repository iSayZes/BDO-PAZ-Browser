# `majorsiegerewardstaticstatus.bss` Format

## Purpose

The Conquest War (major siege) rewards: per row a u8, eleven item lists
(victory, defeat, score places 1st to 6th, liberation, a medal and a
plus item), a u32 and three item IDs; after the rows one booty list of
item IDs per territory. On client 3482 the three rows (`unknown_00`
`5`, `6` and `7`) hold the Tier 1, Tier 2 and Unlimited Conquest War
reward boxes, and the five booty lists the temporary crown and armor of
Balenos to Valencia with [Guild] Reminiscence of Battle.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------------------- | --------- |
| 3      | 3474 and later | 3482    | `majorsiegerewardstaticstatus.bss` | 1,409 | 60 Reward, 3 Row, 5 Booty | 16        |
| 2      | 3251           | 3251    | `majorsiegerewardstaticstatus.bss` | 581   | 33 Reward, 3 Row, 5 Booty | 12        |
| 1      | 3002           | 3002    | `majorsiegerewardstaticstatus.bss` | 533   | 33 Reward, 3 Row, 5 Booty | 12        |

| Layout | File                               | Known           | Unknown       |
| ------ | ---------------------------------- | --------------- | ------------- |
| 3      | `majorsiegerewardstaticstatus.bss` | 1,154 B (81.9%) | 255 B (18.1%) |
| 2      | `majorsiegerewardstaticstatus.bss` | 566 B (97.4%)   | 15 B (2.6%)   |
| 1      | `majorsiegerewardstaticstatus.bss` | 530 B (99.4%)   | 3 B (0.6%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3251   | Layout 2 |
| 3002   | Layout 1 |
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

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), territory names (LOC type 12) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type               | Field        | Notes                                               |
| ------------------- | ------------------ | ------------ | --------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                        |
| `+0x04`             | u32                | row_count    | Number of rows                                      |
| `+0x08`             | Row[row_count]     | rows         | See Row                                             |
| `rows+0x00`         | u32                | booty_count  | Number of booty lists                               |
| `rows+0x04`         | Booty[booty_count] | booty_items  | See Booty                                           |
| `booty_items+0x00`  | String Table       | string_table | See String Table                                    |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `booty_items` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                          |

### Row (variable: 105 bytes + rewards)

| Offset                   | Type                           | Field                        | Notes                                                    |
| ------------------------ | ------------------------------ | ---------------------------- | -------------------------------------------------------- |
| `+0x00`                  | u8                             | unknown_00                   | `5`, `6`, `7` on client 3482; see Open Questions         |
| `+0x01`                  | u64                            | win_reward_count             | Number of `win_rewards`                                  |
| `+0x09`                  | Reward[win_reward_count]       | win_rewards                  | Victory: Glorious Victor Reward and a Combat Secret Book |
| `win_rewards+0x00`       | u64                            | lose_reward_count            | Number of `lose_rewards`                                 |
| `win_rewards+0x08`       | Reward[lose_reward_count]      | lose_rewards                 | Defeat: Fighting Spirit Reward and a Combat Secret Book  |
| `lose_rewards+0x00`      | u64                            | release_win_reward_count     | Number of `release_win_rewards`                          |
| `lose_rewards+0x08`      | Reward[release_win_reward_count] | release_win_rewards        | Score 1st: Burning Spirit Victor Reward                  |
| `release_win_rewards+0x00` | u64                          | release_reward_count_0       | Number of `release_rewards_0`                            |
| `release_win_rewards+0x08` | Reward[release_reward_count_0] | release_rewards_0          | Score 2nd: Burning Spirit Reward (V)                     |
| `release_rewards_0+0x00` | u64                            | release_reward_count_1       | Number of `release_rewards_1`                            |
| `release_rewards_0+0x08` | Reward[release_reward_count_1] | release_rewards_1            | Score 3rd: Burning Spirit Reward (IV)                    |
| `release_rewards_1+0x00` | u64                            | release_reward_count_2       | Number of `release_rewards_2`                            |
| `release_rewards_1+0x08` | Reward[release_reward_count_2] | release_rewards_2            | Score 4th: Burning Spirit Reward (III)                   |
| `release_rewards_2+0x00` | u64                            | release_reward_count_3       | Number of `release_rewards_3`                            |
| `release_rewards_2+0x08` | Reward[release_reward_count_3] | release_rewards_3            | Score 5th: Burning Spirit Reward (II)                    |
| `release_rewards_3+0x00` | u64                            | release_reward_count_4       | Number of `release_rewards_4`                            |
| `release_rewards_3+0x08` | Reward[release_reward_count_4] | release_rewards_4            | Score 6th: Burning Spirit Reward (I)                     |
| `release_rewards_4+0x00` | u64                            | release_reward_count         | Number of `release_rewards`                              |
| `release_rewards_4+0x08` | Reward[release_reward_count]   | release_rewards              | Liberation: Burning Inspiration Reward                   |
| `release_rewards+0x00`   | u64                            | plus_medal_reward_count      | Number of `plus_medal_rewards`                           |
| `release_rewards+0x08`   | Reward[plus_medal_reward_count] | plus_medal_rewards          | Medal of Glory x5 on client 3482                         |
| `plus_medal_rewards+0x00` | u64                           | plus_item_reward_count       | Number of `plus_item_rewards`                            |
| `plus_medal_rewards+0x08` | Reward[plus_item_reward_count] | plus_item_rewards           | Battlefield Glory x1 on client 3482                      |
| `plus_item_rewards+0x00` | u32                            | unknown_plus_item_rewards_00 | `200000`, `300000`, `500000` by row on client 3482      |
| `plus_item_rewards+0x04` | u32                            | item_id_1                    | Item ID; `44732` [Guild] Valencia/Edania Elephant Nursery |
| `plus_item_rewards+0x08` | u32                            | item_id_2                    | Item ID; `44733` [Guild] Balenos/Serendia Indomitable Flag Factory |
| `plus_item_rewards+0x0C` | u32                            | item_id_3                    | Item ID; `44734` [Guild] Calpheon/Ulukita Indomitable Flag Factory |

The names are the client 3482 boxes of row `5`; rows `6` and `7` hold
the Tier 2 and Unlimited boxes of the same kinds.

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                             |
| ------- | -------- | ---------- | ----------------------------------------------------------------- |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name |
| `+0x04` | bytes[4] | unknown_04 | `00 00 00 00` in the first three lists, `A4 00 00 00` in the others on client 3482 |
| `+0x08` | u64      | count      | How many of the item                                              |

### Booty (variable: 10 bytes + item IDs)

| Offset  | Type            | Field         | Notes                                                           |
| ------- | --------------- | ------------- | --------------------------------------------------------------- |
| `+0x00` | u16             | territory_key | `territoryinfo.bss` key, LOC type 12 name; `0` to `4` on client 3482 |
| `+0x02` | u64             | item_count    | Number of `item_ids`; `3` on every list of client 3482          |
| `+0x0A` | u32[item_count] | item_ids      | The territory's crown and armor (Temp) and [Guild] Reminiscence of Battle |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

### Row (149 bytes)

| Offset  | Type   | Field                        | Notes                     |
| ------- | ------ | ---------------------------- | ------------------------- |
| `+0x00` | u8     | unknown_00                   | `5`, `6`, `7`             |
| `+0x01` | Reward | win_rewards                  | One item, no count before |
| `+0x0D` | Reward | lose_rewards                 |                           |
| `+0x19` | Reward | release_win_rewards          |                           |
| `+0x25` | Reward | release_rewards_0            |                           |
| `+0x31` | Reward | release_rewards_1            |                           |
| `+0x3D` | Reward | release_rewards_2            |                           |
| `+0x49` | Reward | release_rewards_3            |                           |
| `+0x55` | Reward | release_rewards_4            |                           |
| `+0x61` | Reward | release_rewards              |                           |
| `+0x6D` | Reward | plus_medal_rewards           |                           |
| `+0x79` | Reward | plus_item_rewards            |                           |
| `+0x85` | u32    | unknown_plus_item_rewards_00 |                           |
| `+0x89` | u32    | item_id_1                    |                           |
| `+0x8D` | u32    | item_id_2                    |                           |
| `+0x91` | u32    | item_id_3                    |                           |

### Reward (12 bytes)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id |       |
| `+0x04` | u64  | count   |       |

## Layout 1

### Row (133 bytes)

| Offset  | Type   | Field               | Notes                     |
| ------- | ------ | ------------------- | ------------------------- |
| `+0x00` | u8     | unknown_00          | `5`, `6`, `7`             |
| `+0x01` | Reward | win_rewards         | One item, no count before |
| `+0x0D` | Reward | lose_rewards        |                           |
| `+0x19` | Reward | release_win_rewards |                           |
| `+0x25` | Reward | release_rewards_0   |                           |
| `+0x31` | Reward | release_rewards_1   |                           |
| `+0x3D` | Reward | release_rewards_2   |                           |
| `+0x49` | Reward | release_rewards_3   |                           |
| `+0x55` | Reward | release_rewards_4   |                           |
| `+0x61` | Reward | release_rewards     |                           |
| `+0x6D` | Reward | plus_medal_rewards  |                           |
| `+0x79` | Reward | plus_item_rewards   |                           |

## Field Names

The lists take the names of the Conquest War columns of the
`SiegeReward` sheet of a private server's `DataSheets.bexcel` on client
1784, where they are single items: `MajorWinMedal_ItemKey`,
`MajorLoseMedal_ItemKey`, `MajorReleaseWinMedal_ItemKey`,
`MajorReleaseMedal_ItemKey_0` to `_4`, `MajorReleaseMedal_ItemKey`,
`MajorPlusMedal_ItemKey` with `PlusMedal_Major` (`5`) and
`PlusItem_Major` (`44391`, Battlefield Glory, the same item as client
3482's `plus_item_rewards`). That sheet's item IDs are older boxes of
the same names (Glorious Victor Reward `45964`, Fighting Spirit Reward
`45971`, Burning Spirit Reward (V) to (I) `45965` to `45969`). The LOC
type 0 text of each client 3482 box confirms the list: "How to Obtain:
Tier 1 Conquest War victory", "defeat", "Score 1st" to "Score 6th" and
"liberation", so `Release` is the liberation and `ReleaseWin` the
first score place. The same columns name the Major Rewards of
[`siegerewarddata.bss`](siegerewarddata_bss.md).

The booty lists match the `BootyItem_0` to `BootyItem_4` columns of the
same sheet's service type `1` (DEV) and `3` (KOR_REAL) rows
(`731901,731906,45113` to `731905,731910,45113`, 5 of 5; the other
service types list the permanent `23381,23386` and so on), and
`territory_key` the suffix: each list holds the Temp copies of the crown
and armor that `territoryinfo.bss` gives the lord of that territory in
`booty_item_ids` (Silver Mane for `0` Balenos, Blue Lion for `1`
Serendia, Golden Eagle for `2` Calpheon, Asula for `3` Mediah, Aal for
`4` Valencia).

## Notes

- Clients 3474 and later use Layout 3 (1,409 bytes on client 3482).
  Client 3251 uses Layout 2: one item per list with no counts (581
  bytes). Client 3002 uses Layout 1, without the u32 and the three item
  IDs (533 bytes), and the Resplendent Medal of Honor (`15692`) as the
  medal. The file is not in the archives of client 2765 or 1784.
- The three item IDs are the same on all three rows of client 3482: the
  Elephant Nursery and the two Indomitable Flag Factories, guild siege
  buildings.
- The handler (`_bss/majorsiegerewardstaticstatus/`) shows one row per
  item: each row's list items with their count and list, then the three
  item IDs, then each booty list's items with the territory name, in
  file order.

## Open Questions

### The Row u8

`unknown_00` is `5`, `6` and `7`, and the rows' boxes say Tier 1, Tier 2
and Unlimited Conquest War in their LOC text. A siege tier enum where
`1` to `4` are the Node War tiers fits, but no Lua of client 3482 names
such an enum.

### The u32 and the Three Item IDs

`unknown_plus_item_rewards_00` grows by row (`200000`, `300000`,
`500000`), which fits a silver or guild fund amount. The three item IDs
are guild siege building items; whether the row gives them, or allows
them in that tier, is open.
