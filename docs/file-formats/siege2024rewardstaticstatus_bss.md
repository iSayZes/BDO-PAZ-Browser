# `siege2024rewardstaticstatus.bss` Format

## Purpose

The Node War (2024 land siege) rewards: per row a u16, five reward sets
of four item lists each, one more item list and two skill keys. On
client 3482 the three rows (`unknown_00` `0`, `1` and `2`) hand out the
Determined, Kindling and Blazing reward boxes: each set a Triumph Reward
of its tier (Tier 1 to Tier 5), Battlefield Honor or Glory, five Gold
Bars 1G or Medals of Glory and a Triumph Reward of Resilience; the last
list a Resolve Reward with two Combat Secret Books (S).

Same layout as [`oceansiegereward.bss`](oceansiegereward_bss.md), read by
the same handler: a u32 row count, then per row the u16 `unknown_00`,
five Reward Sets of four u64-counted lists of 16-byte rewards
(`item_id`, `unknown_04`, `count`), the list `unknown_rewards` and the
u32 `skill_key_1` and `skill_key_2`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records                         | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------------------------- | --------- |
| 2      | 3474 and later | 3482    | `siege2024rewardstaticstatus.bss` | 1,658 | 69 Reward, 15 Reward Set, 3 Row | 16        |
| 1      | 3002 to 3251   | 3251    | `siege2024rewardstaticstatus.bss` | 806   | 63 Reward, 15 Reward Set, 3 Row | 12        |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 2      | `siege2024rewardstaticstatus.bss` | 872 B (52.6%) | 786 B (47.4%) |
| 1      | `siege2024rewardstaticstatus.bss` | 800 B (99.3%) | 6 B (0.7%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | No file              |
| 2637   | No file              |
| 2519   | No documented layout |
| 2313   | No file              |
| 2107   | No file              |
| 1937   | No file              |
| 1784   | No file              |
| 1636   | No file              |
| 1485   | No file              |
| 1348   | No file              |
| 1230   | No file              |
| 1156   | No file              |
| 1058   | No file              |
| 911    | No file              |
| 794    | No file              |
| 606    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                               |
| --------------------- | -------- | -------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), skill names (LOC type 10) |

All multi-byte values are little-endian.

## Reward Sets

Client 3482; the names are LOC type 0. Row `0` gives the Determined
boxes, row `1` the Kindling and row `2` the Blazing ones, so "Determined"
below stands for the row's box name:

| List                | Sets 1 and 2                                | Sets 3 to 5                                  |
| ------------------- | ------------------------------------------- | -------------------------------------------- |
| `unknown_rewards_1` | Determined Triumph Reward (Tier 1, Tier 2)  | Determined Triumph Reward (Tier 3 to Tier 5); set 5 adds Combat Secret Book (M) x2 |
| `unknown_rewards_2` | Battlefield Honor (Battlefield Glory on row `2`) | The same                                |
| `unknown_rewards_3` | Gold Bar 1G x5                              | Medal of Glory x5                            |
| `unknown_rewards_4` | Determined Triumph Reward of Resilience     | Another item of the same name                |

`unknown_rewards` holds the Determined Resolve Reward and Combat Secret
Book (S) x2. The skill pairs are Glorious Combat, Life (Standard) and
(Basic) on row `0`, (Advanced) and (Standard) on row `1` and (Ultimate)
and (Superior) on row `2`: skills `58478, 58479`, `58477, 58478` and
`58475, 58476`.

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. The rows have the shape of
[`oceansiegereward.bss`](oceansiegereward_bss.md), whose names they
take: `item_id` names an item with a LOC type 0
name on all 69 rewards of client 3482, and `skill_key_1` and
`skill_key_2` name skills with a LOC type 10 name.

## Notes

- Clients 3002 and 3251 use Layout 1 of `oceansiegereward.bss`, one
  item per list with no counts (806 bytes, three rows); client 3474
  turns each list into a counted list. Client 2519 has 254-byte rows
  (782 bytes): the Layout 1 row without the two skill keys, a layout
  neither doc lists, so the doc check finds no layout for it. The file
  is not in the archives of clients 2637 and 2765.
- `unknown_04` is `A4 00 00 00` on every reward of client 3482, as in
  `oceansiegereward.bss`.
- The handler of `oceansiegereward.bss` (`_bss/oceansiegereward/`)
  previews this file: one row per reward item with its set, list and
  the row's two skills.

## Open Questions

### What the Lists Stand For

[`siegerewarddata.bss`](siegerewarddata_bss.md) names the reward slots
of a Node War tier after the `SiegeReward` sheet of client 1784: a
victory item, a defeat item, a liberation item, a count of medals and a
plus item. The lists of each set line up with them: the Triumph Reward
of `unknown_rewards_1` is the victory item, Battlefield Honor and Glory
of `unknown_rewards_2` are the plus items `siegerewarddata.bss` names
(`44392`, `44391`), five of the medal item (`2`, Gold Bar 1G) are in
`unknown_rewards_3`, and the Resolve Reward of `unknown_rewards` matches
its defeat items. The Triumph Reward of Resilience has no slot there,
and the item IDs of `siegerewarddata.bss` are other boxes, so the names
stay open.

### The u16 and the Two Skills

`unknown_00` is `0`, `1` and `2`, one per box name (Determined, Kindling,
Blazing), which fits the three land groups of `_eTerritoryGroupType` in
`panel_window_villagesiegemenu_all.luac` (client 3482). Which of the two
skills goes to whom is open.
