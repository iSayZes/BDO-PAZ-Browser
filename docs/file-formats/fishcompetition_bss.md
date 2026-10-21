# `fishcompetition.bss` Format

## Purpose

The fish of the fishing contest (the Fish Competition window opened from the
Fishing Encyclopedia): per fish item its grade, the reward box of each of
the six rank tiers and the title item for the biggest catch. After the rows
the file lists the last rank of each reward tier.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `fishcompetition.bss` | 5,765 | 173 Row | 33        |

| Layout | File                  | Known           | Unknown     |
| ------ | --------------------- | --------------- | ----------- |
| 1      | `fishcompetition.bss` | 5,753 B (99.8%) | 12 B (0.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. Item names come from LOC type `0`, else the `ITEM_NAME_KR` lookup
index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field           | Notes                                                       |
| ------------------- | ----------------- | --------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic           | ASCII `PABR`                                                |
| `+0x04`             | u32               | count           | Number of rows                                              |
| `+0x08`             | Row[count]        | rows            | See Row                                                     |
| `rows+0x00`         | u32               | unknown_rows_00 | `1` on clients 3002 and 3474                                |
| `rows+0x04`         | u32               | unknown_rows_04 | `1` on clients 3002 and 3474                                |
| `rows+0x08`         | u32               | unknown_rows_08 | `1` on clients 3002 and 3474                                |
| `rows+0x0C`         | u32[6]            | rank_tiers      | Last rank of each reward tier: `1`, `2`, `3`, `30`, `100`, `300` on clients 3002 and 3474 |
| `rows+0x24`         | String Table      | string_table    | See String Table                                            |
| `string_table+0x00` | u32               | table_start     | Offset of the string table                                  |
| `string_table+0x04` | u32               | zero            | Always `0`                                                  |

On client 3474 the file is 8 + 173 x 33 + 36 + 4 + 8 = 5,765 bytes.

### Row (33 bytes)

| Offset  | Type   | Field                 | Notes                                                                       |
| ------- | ------ | --------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32    | fish_item_key         | The fish (`8330` Tilefish, `821017` Mantis Shrimp); unique                  |
| `+0x04` | u8     | grade                 | Grade of the fish: `2`, `3` or `4`; equals the fish item's grade on 173 of 173 rows (client 3474) |
| `+0x05` | u32[6] | rank_reward_item_keys | Reward item per rank tier, in `rank_tiers` order                            |
| `+0x1D` | u32    | title_item_key        | The `[Title] The Biggest <fish>` item; unique per row                       |

The rows are not sorted by key.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 3002 and 3474                   |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rank Tiers

The reward info window (`panel_window_fishcompetitionrewardinfo.luac`) shows
`_rewardCount = 6` tiers. For tier `i` it calls
`ToClient_GetFishCompetitionRankByIndex(i - 1)`, prints the first
`_singleRankCount = 3` as single ranks (`PANEL_FISHEVENT_MYRANK`) and the
rest as ranges (`PANEL_FISHEVENT_RANKARRANGE`). The six `rank_tiers` values
are those ranks. Every row of clients 3002 and 3474 holds the same six
reward boxes:

| Tier | `rank_tiers` | `rank_reward_item_keys` | Item (LOC type 0)     |
| ---- | ------------ | ----------------------- | --------------------- |
| 1    | 1            | 767697                  | Waveswept Gold Box    |
| 2    | 2            | 767698                  | Waveswept Silver Box  |
| 3    | 3            | 767699                  | Waveswept Bronze Box  |
| 4    | 30           | 767700                  | Waveswept Blue Box    |
| 5    | 100          | 767701                  | Waveswept Green Box   |
| 6    | 300          | 767702                  | Waveswept Gray Box    |

## Field Names

No reference source has this table: the file is not in clients 1784, 2107
and 2519, and neither the 2016 symbols nor the client 1784 sheets name it.
The names follow the client Lua of client 3474:

- `grade`: the contest window colours each fish by
  `ToClient_GetFishCompetitionRareness(index)` and shows that many plus one
  rarity icons; the reward window has grades `_startGrade = 2` to
  `_endGrade = 4` (blue, yellow and red slots). The byte is `2` to `4` and
  matches the item grade of the fish on every row.
- `title_item_key`: the my-reward window asks a reward for
  `getRewardItemKey()` and `getRewardTitleKey()`; the row's last u32 is the
  title item of its fish.

## Notes

- Client 3474 has 173 rows (46 of grade `2`, 65 of grade `3`, 62 of grade
  `4`); client 3002 has 171.
- The reward window reads its items with
  `ToClient_GetCompetitionRewardByGradeAndIndex(grade, index)`; since every
  row holds the same boxes, the file does not show whether the client picks
  them per grade or per fish.

## Open Questions

### unknown_rows_00 to unknown_rows_08

Three u32 between the rows and `rank_tiers`, `1` each on clients 3002 and
3474. One of them may be a count of rank tier sets (with `rank_tiers` its
only entry), but nothing in the Lua reads more than one set.
