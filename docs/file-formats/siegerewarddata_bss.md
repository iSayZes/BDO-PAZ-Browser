# `siegerewarddata.bss` Format

## Purpose

The siege reward items by tier and the Conquest War medals, in two
blocks with no row count. Each block opens with a medal item ID and a
u16 tier count and ends with the same 64-byte Major Rewards structure:
the Conquest War victory, defeat, liberation and score place items.
The first block (Grid Block) holds per tier only counts and a plus
item, in four identical 48-byte grids; the second (Tier Block) holds
per tier a victory, defeat and liberation item with counts. On client
3482 the Tier Block's tiers give the Fervent, Determined, Kindling and
Blazing Triumph and Resolve Rewards, and its Major Rewards the Tier 1
Conquest War boxes; the Grid Block's Major Rewards hold the older boxes
of the same names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------------------------------------ | --------- |
| 1      | 2637 and later | 3482    | `siegerewarddata.bss` | 444   | 4 Tier Grid, 10 Release Medal, 2 Major Rewards, 4 Tier | 6         |

| Layout | File                  | Known         | Unknown      |
| ------ | --------------------- | ------------- | ------------ |
| 1      | `siegerewarddata.bss` | 348 B (78.4%) | 96 B (21.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
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

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                               |
| ------------------- | ------------ | ------------ | --------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                        |
| `+0x04`             | Grid Block   | grid_block   | See Grid Block                                      |
| `grid_block+0x00`   | Tier Block   | tier_block   | See Tier Block                                      |
| `tier_block+0x00`   | String Table | string_table | See String Table                                    |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `tier_block` ends |
| `string_table+0x04` | u32          | zero         | Always `0`                                          |

### Grid Block (variable: 70 bytes + tier grids)

| Offset             | Type                       | Field           | Notes                                              |
| ------------------ | -------------------------- | --------------- | -------------------------------------------------- |
| `+0x00`            | u32                        | medal_item_id   | Item ID of the medals the `plus_medal_counts` give; `2` (Gold Bar 1G) on client 3482 |
| `+0x04`            | u16                        | tier_grid_count | Number of `tier_grids`; `4` on every client checked |
| `+0x06`            | Tier Grid[tier_grid_count] | tier_grids      | See Tier Grid; the four are byte for byte the same on client 3482 |
| `tier_grids+0x00`  | Major Rewards              | major_rewards   | See Major Rewards                                  |

### Tier Grid (48 bytes)

| Offset  | Type   | Field             | Notes                                                    |
| ------- | ------ | ----------------- | -------------------------------------------------------- |
| `+0x00` | u16[4] | unknown_00        | One per tier: `12, 16, 20, 24` on client 3482            |
| `+0x08` | u16[4] | unknown_08        | `12, 16, 20, 24`                                         |
| `+0x10` | u16[4] | unknown_10        | `12, 16, 20, 24`                                         |
| `+0x18` | u16[4] | plus_medal_counts | Medals per tier: `5, 5, 5, 5`                            |
| `+0x20` | u32[4] | plus_item_ids     | Plus item per tier: `44392, 44392, 44391, 44391` (Battlefield Honor, Battlefield Glory) |

### Tier Block (variable: 70 bytes + tiers)

| Offset        | Type             | Field         | Notes                                               |
| ------------- | ---------------- | ------------- | --------------------------------------------------- |
| `+0x00`       | u32              | medal_item_id | As in the Grid Block; `2` on client 3482            |
| `+0x04`       | u16              | tier_count    | Number of `tiers`; `4` on every client checked      |
| `+0x06`       | Tier[tier_count] | tiers         | See Tier                                            |
| `tiers+0x00`  | Major Rewards    | major_rewards | See Major Rewards                                   |

### Tier (24 bytes)

| Offset  | Type | Field                  | Notes                                                        |
| ------- | ---- | ---------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | win_reward_count       | `1` on every tier of client 3482                             |
| `+0x02` | u16  | lose_reward_count      | `1`                                                          |
| `+0x04` | u16  | release_reward_count   | `1`                                                          |
| `+0x06` | u16  | plus_medal_count       | Medals of `medal_item_id`; `5`                               |
| `+0x08` | u32  | win_reward_item_id     | A Triumph Reward: Fervent, Determined, Kindling, Blazing      |
| `+0x0C` | u32  | lose_reward_item_id    | The Resolve Reward of the same name                          |
| `+0x10` | u32  | release_reward_item_id | The same item as `lose_reward_item_id` on client 3482        |
| `+0x14` | u32  | plus_item_id           | `44392, 44392, 44391, 44391` by tier                         |

### Major Rewards (64 bytes)

| Offset  | Type             | Field                     | Notes                                                    |
| ------- | ---------------- | ------------------------- | -------------------------------------------------------- |
| `+0x00` | u16              | win_medal_count           | `1` in both blocks on client 3482                        |
| `+0x02` | u16              | lose_medal_count          | `1`                                                      |
| `+0x04` | u16              | release_medal_count       | `1`                                                      |
| `+0x06` | u16              | plus_medal_count          | `5`                                                      |
| `+0x08` | u32              | plus_item_id              | `44391` Battlefield Glory                                |
| `+0x0C` | u32              | win_medal_item_id         | Glorious Victor Reward: `45964`, `761591` (Tier Block)   |
| `+0x10` | u32              | lose_medal_item_id        | Fighting Spirit Reward: `45971`, `761598`                |
| `+0x14` | u32              | release_medal_item_id     | Burning Inspiration Reward: `45970`, `761597`            |
| `+0x18` | u32              | plus_medal_item_id        | The same as the block's `medal_item_id`                  |
| `+0x1C` | Release Medal[5] | release_medals            | Score 2nd to 6th: Burning Spirit Reward (V) to (I)       |
| `+0x3A` | u32              | release_win_medal_item_id | Score 1st: Burning Spirit Victor Reward, `59796`, `761590` |
| `+0x3E` | u16              | release_win_medal_count   | `1`                                                      |

### Release Medal (6 bytes)

| Offset  | Type | Field   | Notes                                                  |
| ------- | ---- | ------- | ------------------------------------------------------ |
| `+0x00` | u16  | count   | `1` on client 3482                                     |
| `+0x02` | u32  | item_id | `45965` to `45969` (Grid Block), `761592` to `761596` (Tier Block) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names come from the `SiegeReward` sheet of a private server's
`DataSheets.bexcel` on client 1784 (keyed by `PA_GAME_SERVICE_TYPE`; the
file is not in that client's archives). The Grid Block's Major Rewards
match its Conquest War columns by value, 21 of 21 on client 3002, where
the medal was still the sheet's `15692`: `WinMedal_Major`,
`LoseMedal_Major`, `ReleaseMedal_Major` and `PlusMedal_Major` (`1, 1, 1,
5`), `PlusItem_Major` (`44391`), `MajorWinMedal_ItemKey` (`45964`),
`MajorLoseMedal_ItemKey` (`45971`), `MajorReleaseMedal_ItemKey`
(`45970`), `MajorPlusMedal_ItemKey` (`15692`), the five
`ReleaseMedal_Major_N` and `MajorReleaseMedal_ItemKey_N` pairs (`1`,
`45965` to `45969`), `MajorReleaseWinMedal_ItemKey` (`59796`) and
`ReleaseWinMedal_Major` (`1`). `medal_item_id` is `MedalItemKey`
(`15692` on clients 2765 and 3002, `2` from client 3251). The LOC type
0 text of the Tier Block's Conquest War items gives the roles: "How to
Obtain: Tier 1 Conquest War victory", "defeat", "liberation", "Score
1st" to "Score 6th", the same as the lists of
[`majorsiegerewardstaticstatus.bss`](majorsiegerewardstaticstatus_bss.md).

A Tier holds the sheet's per-tier columns `WinRewardCount_N`,
`LoseRewardCount_N`, `ReleaseRewardCount_N`, `PlusMedal_N`,
`WinRewardItem_N`, `LoseRewardItem_N`, `ReleaseRewardItem_N` and
`PlusItem_N`: the counts (`1, 1, 1, 5`) and the plus items (`44392,
44392, 44391, 44391`) match for all four tiers; the reward items differ
(the sheet's `45185` to `45196` are older boxes), and the LOC text of the
client 3482 items fits the roles: a Triumph Reward is "issued to those
who achieve glorious victory", a Resolve Reward "to those whose resolve
remained determined". The Tier Grid's `plus_medal_counts` and
`plus_item_ids` match `PlusMedal_0` to `_3` and `PlusItem_0` to `_3`
(8 of 8 per grid).

## Notes

- Every client checked has 444 bytes. Clients 3002 to 3482 differ only
  in the four medal item IDs (`medal_item_id` and `plus_medal_item_id`
  of both blocks): `15692` (Resplendent Medal of Honor) on client 3002,
  `2` (Gold Bar 1G) from client 3251. Client 2765 also has the medal
  `15692`, and the Tier Block's Major Rewards hold other boxes of the
  same names and roles: `65309` Glorious Victor Reward ("Tier 1 Conquest
  War victory"), `65316` Fighting Spirit Reward, `65308` Burning Spirit
  Victor Reward and so on. Client 2637 has the bytes of client 2765.
- The struct packs the four u16 counts of the Major Rewards before the
  item IDs they count, and the release win medal's item ID before its
  count.
- The handler (`_bss/siegerewarddata/`) shows one row per reward slot:
  the item, its count, the reward it is, the tier, the tier grid and the
  block. Per tier and grid the Grid Block gives the medals and the plus
  item; per tier the Tier Block gives the victory, defeat and liberation
  items, the medals and the plus item; each block ends with its eleven
  Conquest War slots. A plus item has no count.

## Open Questions

### What the Tier Grid Stands For

A Tier Grid holds four values per field, one per tier, where a Tier
holds one: `plus_medal_counts` and `plus_item_ids` match the sheet's per
tier medals and plus items. The three u16 arrays before them (`12, 16,
20, 24` each) sit where a Tier holds the victory, defeat and liberation
counts, but no item IDs go with them, and the four grids are the same.
What the grid count stands for (four days, four node levels) and what
`unknown_00` to `unknown_10` count is open; no Lua of client 3482 reads
the file.

### Which Block Is in Use

The Tier Block's items are the current boxes (the Conquest War boxes'
LOC text names Tier 1), while the Grid Block's Major Rewards still hold
the client 1784 items `45964` to `45971` and `59796`, which carry no
"How to Obtain" line. Which block the server reads for which siege is
open.
