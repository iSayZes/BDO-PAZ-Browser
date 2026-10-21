# `elementalmonsterreward.bss` Format

## Purpose

The ranking rewards of the Black Shrine (검은 사당) bosses in the Land of the
Morning Light: per boss character, the items of each rank tier ("#1",
"#2 ~ #5") and the items of the "Bonus Rewards" row for players outside the
ranks. The detailed reward window
(`panel_window_morningland_detailreward_all.luac`) reads it per boss through
`ToClient_getElementalMonsterRankReward*` and
`ToClient_getElementalMonsterBaseReward*`, with a flag that picks the
second table for the Hwanghae (Party) ranking.

On client 3474 the first table has a record for each of the 108 bosses of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md): the 94 Donghae
(Solo) bosses with the tiers `1`, `5` and `20` and two base items, the 14
Hwanghae (Party) bosses with two base items and no tiers. The second table
has the 14 Hwanghae (Party) bosses with their party tiers and no base items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records                                    | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | ------------------------------------------ | --------- |
| 3      | 3474 and later | 3474    | `elementalmonsterreward.bss` | 18,952 | 829 Reward Item, 331 Rank Tier, 122 Record | 16        |
| 2      | 3002 to 3251   | 3251    | `elementalmonsterreward.bss` | 4,530  | 429 Reward Item, 313 Rank Tier, 116 Record | 6         |
| 1      | 2519           | 2519    | `elementalmonsterreward.bss` | 4,204  | 400 Reward Item, 300 Rank Tier, 100 Record | 6         |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 3      | `elementalmonsterreward.bss` | 18,952 B (100.0%) | 0 B (0.0%) |
| 2      | `elementalmonsterreward.bss` | 4,530 B (100.0%)  | 0 B (0.0%) |
| 1      | `elementalmonsterreward.bss` | 4,204 B (100.0%)  | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                        |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `elementalmonsterstat.bss` | Optional | The part and difficulty of each boss, by `character_key`    |
| `languagedata_*.loc`       | Optional | Boss and item names, and the rank labels of the window      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset         | Type                 | Field         | Notes                                                     |
| -------------- | -------------------- | ------------- | --------------------------------------------------------- |
| `+0x00`        | u32                  | count         | Number of `records`                                       |
| `+0x04`        | Record[count]        | records       | The rewards the window reads with the Part 2 flag off     |
| `records+0x00` | u32                  | part2_count   | Number of `part2_records`                                 |
| `records+0x04` | Record[part2_count]  | part2_records | The rewards the window reads with the Part 2 flag on      |

### Record (variable: 14 bytes + rank tiers and base rewards)

| Offset            | Type                            | Field             | Notes                                                                 |
| ----------------- | ------------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`           | u16                             | character_key     | The boss, the `character_key` of `elementalmonsterstat.bss`           |
| `+0x02`           | u32                             | rank_tier_count   | Number of `rank_tiers`; `ToClient_getElementalMonsterRankRewardListCount` |
| `+0x06`           | Rank Tier[rank_tier_count]      | rank_tiers        | See Rank Tier                                                         |
| `rank_tiers+0x00` | u64                             | base_reward_count | Number of `base_rewards`; `ToClient_getElementalMonsterBaseRewardSize` |
| `rank_tiers+0x08` | Reward Item[base_reward_count]  | base_rewards      | The "Bonus Rewards" row, for players outside the ranks                |

### Rank Tier (variable: 12 bytes + rewards)

| Offset  | Type                       | Field        | Notes                                                                 |
| ------- | -------------------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                        | rank         | Lowest rank of the tier; `ToClient_getElementalMonsterRankByIndex`    |
| `+0x04` | u64                        | reward_count | Number of `rewards`; `ToClient_getElementalMonsterRankRewardSizeByIndex` |
| `+0x0c` | Reward Item[reward_count]  | rewards      | See Reward Item                                                       |

### Reward Item (16 bytes)

Same structure as the Reward Item of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md#reward-item-16-bytes).

| Offset  | Type     | Field      | Notes                                                                     |
| ------- | -------- | ---------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | item_key   | Item key, `enchant_level << 24 \| item_id`; `...RewardItemKeyByIndex`     |
| `+0x04` | bytes[4] | padding_04 | Alignment of `count`; `fc 7f 00 00` or `f7 7f 00 00` (client 3474), see Notes |
| `+0x08` | i64      | count      | Number of the item; `...RewardItemCountByIndex`, `1` on every entry (client 3474) |

## Layout 2

### Record (variable: 12 bytes + rank tiers)

| Offset            | Type                        | Field           | Notes                                    |
| ----------------- | --------------------------- | --------------- | ---------------------------------------- |
| `+0x00`           | u16                         | character_key   |                                          |
| `+0x02`           | u32                         | rank_tier_count |                                          |
| `+0x06`           | Rank Tier[rank_tier_count]  | rank_tiers      |                                          |
| `rank_tiers+0x00` | Reward Item                 | base_rewards    | Exactly one item, no count before it     |

### Rank Tier (10 bytes)

| Offset  | Type        | Field   | Notes                                |
| ------- | ----------- | ------- | ------------------------------------ |
| `+0x00` | u32         | rank    |                                      |
| `+0x04` | Reward Item | rewards | Exactly one item, no count before it |

### Reward Item (6 bytes)

| Offset  | Type | Field    | Notes                              |
| ------- | ---- | -------- | ---------------------------------- |
| `+0x00` | u32  | item_key |                                    |
| `+0x04` | u16  | count    | `1` on every entry (client 3251)   |

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                       |
| ------- | ------------- | ------- | --------------------------- |
| `+0x00` | u32           | count   | Number of `records`         |
| `+0x04` | Record[count] | records | The only table; see Notes   |

## Rank Tiers

The window labels a tier with the GAME sheet key `LUA_MORNING_ATTRBOSS_RANK`
("#{rank}"). A tier whose `rank` is above 1 reads from one past the
previous tier's `rank` to its own (`#2 ~ #5`, and `#2 ~ #2` for the tiers
`1`, `2`), or `~ #50` when it is the first tier; the base rewards row reads
`LUA_MORNING_ATTRBOSS_OUTOFRANKREWARD` ("Bonus Rewards"). The window shows
the base rewards only for a boss that has rank tiers and only with the Part
2 flag off.

| Table           | Bosses (client 3474) | `rank` of the tiers        | Items per tier | Base rewards |
| --------------- | -------------------- | -------------------------- | -------------- | ------------ |
| `records`       | 94 Donghae (Solo)    | `1`, `5`, `20`             | 2              | 2            |
| `records`       | 14 Hwanghae (Party)  | None                       |                | 2            |
| `part2_records` | 7 Hwanghae (Party)   | `1`, `2`, `3`, `10`, `25`, `50` | 1         | 0            |
| `part2_records` | 7 Hwanghae (Party)   | `50`                       | 1              | 0            |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, and the
2016 client and the client 519 server tables predate it.

The names follow the client Lua of client 3474
(`panel_window_morningland_detailreward_all.luac`): per boss character
key and Part 2 flag it reads `ToClient_getElementalMonsterRankRewardListCount`,
then per tier `ToClient_getElementalMonsterRankByIndex`,
`ToClient_getElementalMonsterRankRewardSizeByIndex` and per item
`...RankRewardItemKeyByIndex` and `...RankRewardItemCountByIndex`; for the
base row `ToClient_getElementalMonsterBaseRewardSize`,
`...BaseRewardItemKey` and `...BaseRewardItemCount`. The counts, ranks and
items sit in the file in that order, and the item names match the tiers:
`790001` "C-1 Boss Blitz Reward: Golden Pig King (Rank 1)" is the tier `1`
item of the Calamity 1 Golden Pig King `23608`, `790011` "(Rank 2)" its
tier `5` item.

`part2_count` and `part2_records` are named after the Lua flag
`isMorningLandMonsterPart2`: its 14 keys are the Hwanghae (Party) bosses
(`monster_part` `2` in `elementalmonsterstat.bss`), and their tier items
are "Boss Blitz Reward (Rank 1)" `761108` to "(Rank 6)" `761113`.

## Notes

- The second item of every `records` tier and base row is `890117`
  (Korean name 전투 비급서(소형); no English LOC name on client 3474).
- The base items of the Hwanghae (Party) bosses in `records` are their
  "Boss Slayer's Haul" boxes, the same item as their `show_rewards` in
  `elementalmonsterstat.bss` (`761337` "Boss Slayer's Haul - Jigwi
  (Normal)" for `24562`). The window does not show them, as it skips the
  base row with the Part 2 flag on and the tier list is empty with it off.
- The handler (`_bss/elementalmonsterreward/`) shows one row per rank tier
  and per non-empty base rewards row, labelled as the window labels them,
  with a Party Ranking flag on the `part2_records` rows. It links each boss
  to its `elementalmonsterstat.bss` row and takes the part and difficulty
  from there.
- `padding_04` is the 4 bytes between the u32 `item_key` and the 8-aligned
  i64 `count`, as in `elementalmonsterstat.bss`.
- Layout 2 (clients 3002 and 3251) has one item per tier and one base item,
  with a u16 count; Layout 1 (client 2519) has the same records and no
  second table, as the Hwanghae (Party) bosses came later.
- The Layout 2 `count` is a u16 that holds `1` on every entry; it takes its
  name from the Layout 3 `count` at the same place after `item_key`.
