# `seasonpass.dbss` Format

## Purpose

The rows of the Black Spirit Pass (season pass) window: per row its number,
the free and the premium (Black Spirit Pass) quest, a season type, and a
replacement title and text that the window shows while a condition quest
is not done. Since client 2519 the rows are followed by the quest chain
range of each pass season. `panel_window_blackspiritpass_1.luac` reads a
row by its number through `ToClient_GetSeasonPassQuestAt(listIdx,
__eSeasonPassQuest_Normal)` and `__eSeasonPassQuest_SeasonPass`, and the
replacement texts through `ToClient_CanShowChangedSeasonPass(listIdx)`,
`ToClient_GetSeasonPassChangedTitle(listIdx)` and
`ToClient_GetSeasonPassChangedDesc(listIdx)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                 | Row bytes                |
| ------ | -------------- | ------- | ----------------- | ----- | ----------------------- | ------------------------ |
| 3      | 2519 and later | 3482    | `seasonpass.dbss` | 7,737 | 205 Row, 5 Season Range | 37 to 149, 38 on average |
| 2      | 1348 to 2313   | 2313    | `seasonpass.dbss` | 2,262 | 58 Row                  | 37 to 149, 39 on average |
| 1      | 1485           | 1485    | `seasonpass.dbss` | 654   | 50 Row                  | 13                       |

| Layout | File              | Known           | Unknown       |
| ------ | ----------------- | --------------- | ------------- |
| 3      | `seasonpass.dbss` | 6,905 B (89.2%) | 832 B (10.8%) |
| 2      | `seasonpass.dbss` | 2,030 B (89.7%) | 232 B (10.3%) |
| 1      | `seasonpass.dbss` | 654 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3251   | Layout 3 |
| 3002   | Layout 3 |
| 2765   | Layout 3 |
| 2519   | Layout 3 |
| 2313   | Layout 2 |
| 2107   | Layout 2 |
| 1937   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 2 |
| 1485   | Layout 1 |
| 1348   | Layout 2 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Quest titles (LOC type 18)  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset             | Type                             | Field              | Notes                                                    |
| ------------------ | -------------------------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`            | u32                              | count              | Number of rows                                           |
| `+0x04`            | Row[count]                       | rows               | See Row                                                  |
| `rows+0x00`        | u16                              | unknown_rows_00    | Equals `season_range_count` on every client checked; see Open Questions |
| `rows+0x02`        | u32                              | season_range_count | Number of `season_ranges`                                |
| `rows+0x06`        | Season Range[season_range_count] | season_ranges      | See Season Range                                         |

### Row (variable: 37 bytes + changed texts)

| Offset                  | Type  | Field                      | Notes                                                                                 |
| ----------------------- | ----- | -------------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`                 | u32   | pass_no                    | Row key, the window's `listIdx`; `0` to `count - 1`                                    |
| `+0x04`                 | u32   | base_reward_quest          | Free quest, a packed quest ID (low u16 chain, high u16 quest); `__eSeasonPassQuest_Normal` |
| `+0x08`                 | u32   | premium_reward_quest       | Black Spirit Pass quest, same chain as `base_reward_quest`; `__eSeasonPassQuest_SeasonPass` |
| `+0x0C`                 | u8    | season_type                | `1` on every row (clients 1784 and 3482)                                               |
| `+0x0D`                 | str16 | changed_title_kr           | Korean title the window shows while `condition_quest` is open; empty on most rows     |
| `changed_title_kr+0x00` | str16 | changed_desc_kr            | Korean text shown with it                                                              |
| `changed_desc_kr+0x00`  | u32   | condition_quest            | Packed quest ID; `0` for none                                                          |
| `changed_desc_kr+0x04`  | u32   | unknown_changed_desc_kr_04 | `0` on every row (clients 1784 and 3482)                                               |

### Season Range (6 bytes)

| Offset  | Type | Field             | Notes                                               |
| ------- | ---- | ----------------- | --------------------------------------------------- |
| `+0x00` | u16  | unknown_00        | `1` to `season_range_count`, descending in the file  |
| `+0x02` | u16  | first_quest_chain | First quest chain of the range                       |
| `+0x04` | u16  | last_quest_chain  | Last quest chain of the range                        |

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                           |
| ------- | ---------- | ----- | ------------------------------- |
| `+0x00` | u32        | count | Number of rows                  |
| `+0x04` | Row[count] | rows  | The rows end at the end of file |

## Layout 1

### Row (13 bytes)

| Offset  | Type | Field                | Notes                                         |
| ------- | ---- | -------------------- | --------------------------------------------- |
| `+0x00` | u32  | pass_no              |                                               |
| `+0x04` | u32  | base_reward_quest    |                                               |
| `+0x08` | u32  | premium_reward_quest |                                               |
| `+0x0C` | u8   | season_type          | No changed texts and no condition quest after it |

## Season Ranges

Client 3482; every row's quest chain falls in one range.

| `unknown_00` | Chains         | Rows |
| ------------ | -------------- | ---- |
| 1            | 50000 to 50057 | 58   |
| 2            | 50100 to 50146 | 47   |
| 3            | 50150          | 37   |
| 4            | 50151          | 37   |
| 5            | 50152          | 26   |

Client 2107 (Layout 2) has the 58 rows of range 1; client 2519 adds range
2 and its rows and ranges 1 and 2 after them, client 3251 has four ranges.

## Field Names

The `Seasonpass_UI` sheet of a private server's `DataSheets.bexcel` on
client 1784 matches the file of that client on all 50 of 50 rows and every
column:

| Field                | Column                                                        |
| -------------------- | ------------------------------------------------------------- |
| pass_no              | `No`                                                          |
| base_reward_quest    | `Sp_BaseReward_QuestGroup`, `Sp_BaseReward_QuestID`           |
| premium_reward_quest | `Sp_PremiumReward_QuestGroup`, `Sp_PremiumReward_QuestID`     |
| season_type          | `Season_Type`                                                 |
| condition_quest      | `Condition` (`40022,1`, group and quest)                      |
| changed_title_kr     | `Changed_Tilte`                                               |
| changed_desc_kr      | `Changed_CompletedText`                                       |

The Lua names (`ChangedTitle`, `ChangedDesc`, `Normal` and `SeasonPass`
quest types) come from `panel_window_blackspiritpass_1.luac` of client
3482. The range fields are newer than client 1784 and have no column.

## Notes

- On client 3482 the free quests of the 205 rows are the quest set of
  `seasonpassquestlistfornormal.bss` and the premium quests the set of
  `seasonpassquestlistforcash.bss` ([`seasonpassquestlist.bss`](seasonpassquestlist_bss.md)).
  Each row pairs quest `n` (free) and `n + 1` (premium) of one chain.
- Client 1485 (Layout 1) has 50 rows of 13 bytes, without the changed
  texts and the condition quest; clients 1636 to 2313 (Layout 2) add them,
  and client 2519 (Layout 3) the season ranges. Client 1348 ships an empty
  file (a count of `0`).
- One row of client 3482 (`pass_no` 6, chain 50006) has a changed title
  (스스로 성장하는 즐거움) and condition quest `40022/1`; client 1784 has two
  such rows with the same condition.
- The handler (`_dbss/seasonpass/`) shows one row per pass row with the
  chain, quest and LOC title of its three quests.

## Open Questions

### What the Season Range Number and the u16 Before It Are

`unknown_00` counts the ranges from `1`, the oldest chains first, and the
u16 before the count equals the count on clients 2519 to 3482. A pass
season number and the current season fit, but no Lua getter reads either
value and client 1784's sheets have no column for them.
