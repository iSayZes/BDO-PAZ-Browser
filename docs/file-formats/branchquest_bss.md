# `branchquest.bss` Format

## Purpose

Defines the crossroad quests: per branch group the quest whose completion opens the crossroad, the quests the player picks between, and a later quest of the same story. 42 groups and 161 quest references on client 3474, among them the `[Serendia] [Crossroad]`, `[Balenos] [Crossroad]` and Morning Light `[Crossroad]` choices and the nine `[Crossroad] Adonna's Fortune Telling` cards. The file holds no text; the quest titles come from LOC type 18.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------------------------ | --------- |
| 1      | 1784 and later | 3474    | `branchquest.bss` | 1,637 | 161 Branch Row, 42 Group | 9         |

| Layout | File              | Known            | Unknown    |
| ------ | ----------------- | ---------------- | ---------- |
| 1      | `branchquest.bss` | 1,637 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler reads the quest titles from LOC type 18, keyed by `quest_chain_id` and `quest_id` as in [`quest.dbss`](quest_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A header, the groups back to back, an empty PABR string table and the file trailer.

| Offset              | Type               | Field        | Notes                                                       |
| ------------------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | `PABR` (ASCII)                                              |
| `+0x04`             | u32                | group_count  | Number of branch groups                                     |
| `+0x08`             | Group[group_count] | groups       | See Group                                                   |
| `groups+0x00`       | String Table       | string_table | See String Table                                            |
| `string_table+0x00` | u32                | table_start  | File offset of the string table's `string_count`, where the groups end |
| `string_table+0x04` | u32                | zero         | Observed `0`                                                |

### Group (variable: 4 bytes + rows)

| Offset  | Type                     | Field     | Notes                                                    |
| ------- | ------------------------ | --------- | -------------------------------------------------------- |
| `+0x00` | u32                      | row_count | Number of following rows; `3` to `5` on client 3474      |
| `+0x04` | Branch Row[row_count]    | rows      | See Branch Row                                           |

### Branch Row (9 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | group_key      | The branch group's key; the same in every row of a group, unique per group |
| `+0x04` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form the quest key |
| `+0x06` | u16  | quest_id       | LOC type 18 `str_id2`                                                 |
| `+0x08` | u8   | is_root_quest  | The quest's place in the branch, `0`, `1` or `2`; see Branch Roles    |

Derived packed quest ID, as in [`quest.dbss`](quest_dbss.md):

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### String Table (variable: 4 bytes + strings)

The counted PABR string table of [`newquest.bss`](newquest_bss.md), here with no strings.

| Offset  | Type               | Field        | Notes        |
| ------- | ------------------ | ------------ | ------------ |
| `+0x00` | u32                | string_count | Observed `0` |
| `+0x04` | pstr[string_count] | strings      | Empty        |

## Branch Roles

Every group on client 3474 has one row with `is_root_quest = 0`, one with `2`, and one to three with `1`. The rows are not sorted by role: the `0` row comes first in some groups and after the `1` rows in others.

| Value | Role | Evidence |
| ----- | ---- | -------- |
| `0` | The quest whose completion opens the crossroad | Each `1` quest's accept condition in `quest.dbss` is `clearquest` of this quest. The crossroad window script `panel_window_questbranch` opens its choice after the same quests (`isClearedQuestList`: Mediah 21403 / 6, Blackstar 3408 / 8, the Adonna cards 9022 / 1 to 9) |
| `1` | A crossroad choice | The quest titles carry `[Crossroad]`, and each one's accept condition rules out the other choices of the group (`!progressquest` / `!clearquest`). `panel_window_questbranch` starts the same quests (`startGroupNo`, `startQuestNo`: 21404 / 1 and 21501 / 1 for Mediah) |
| `2` | A later quest of the same story | On 26 of 42 groups its accept condition names the end of the group's branches (`clearQuest(21131,2);<or>clearQuest(21132,2);` for 21130 / 5 `[Serendia] A Friendly Face`); see Open Questions for the rest |

Example, group key 39:

| `is_root_quest` | Quest | Title |
| --------------- | ----- | ----- |
| `0` | 21130 / 4 | `[Serendia] Jarette's Guest` |
| `1` | 21131 / 1 | `[Serendia] [Crossroad] Mine Imp Subjugation` |
| `1` | 21132 / 1 | `[Serendia] [Crossroad] Negotiation with the Imp Boss` |
| `2` | 21130 / 5 | `[Serendia] A Friendly Face` |

## Field Names

The `QuestBranch` sheet of a private server's `DataSheets.bexcel` on client 1784 names the columns `QuestBranchGroupKey` (`group_key`), `QuestBranchKey` (the quest as `chain,quest`, split into `quest_chain_id` and `quest_id`) and `isRootQuest` (`is_root_quest`). Its developer comment calls `isRootQuest` the parent/child setting of the quests bundled into one branch. On client 3474, 59 of 59 shared rows (17 shared groups) carry the same group key and `isRootQuest`; the sheet's groups 1, 4 and 7 are not in the live file, and groups 24 to 51 are newer than the sheet. The sheet's fourth column, `ContentsGroupKey`, is not compiled into the file.

## Notes

- The file is `1,637` bytes on client 3474 (`717` bytes with 19 groups on client 1784, the same layout).
- The groups are not in key order (10, 2, 11, 3, 5, ...), and keys skip numbers (no 1, 4, 7, 17, 22, 23, 28 to 30).
- Quest 9024 / 1 `Wanderer's Star` is the `2` row of all nine Adonna card groups (keys 10 to 19).
- With the `_ContentsGroup_BranchQuestCountCheck` option on, `panel_window_questbranch` shows a number on each choice from `ToClient_GetBranchQuestProgressAndClearedCount(groupNo, questNo)`, called with the choice's start quest (a `1` row).

## Open Questions

### What Does `is_root_quest` 2 Mark?

On client 3474, on 26 of 42 groups the `2` quest's accept condition names the group's branches: 25 with one quest of each branch joined by `<or>`, and Adonna key 10 with its one choice 9023 / 1. On the other 16 it needs one fixed earlier quest: the six Blackstar groups (`[Blackstar Weapon] Blackstar Weapon Piece` 3408 / 14 needs `clearquest(3408,13);`), the Mediah group (21411 / 14 `[Mediah] Apocalyptic Prophecy` needs 21411 / 13), the Sage group (368 / 28 needs 368 / 27, while the `0` quest 368 / 29 needs 368 / 24), and eight of the nine Adonna groups, whose `2` quest 9024 / 1 needs the `1` quest of key 10 only. What the client or server does with this quest is not confirmed; no Lua reads the rows of this file directly.
