# `questprogressgroup.bss` Format

## Purpose

Groups of quest chains, each chain with the quest it starts at and the quest that finishes its story. Groups 1 and 2 are the chains of the two Land of the Morning Light quest boards: in every chain of group 1, `final_quest_id` is the quest the board's Lua treats as the end of the story (it shows the chain at 100% once that quest is cleared). The plain PABR file holds the groups, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ----------------- | --------- |
| 1      | 3474 and later | 3474    | `questprogressgroup.bss` | 342   | 25 Entry, 9 Group | 10        |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 1      | `questprogressgroup.bss` | 342 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                              |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                           |
| ------------------- | ------------ | ------------------ | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                    |
| `+0x04`             | u32          | count              | Number of groups                                |
| `+0x08`             | Group[count] | groups             | Variable-size groups, back to back; see Group   |
| `groups+0x00`       | String Table | string_table       | See String Table                                |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the groups end  |
| `string_table+0x04` | u32          | zero               | Always `0`                                      |

The string table has the shape `itemequipgroup.bss` and `exploration.bss` use (`_common/pabr_strings.py`). Walking `count` groups ends exactly at `string_table_start`.

### Group (variable: 8 bytes + entries)

| Offset  | Type               | Field       | Notes                                      |
| ------- | ------------------ | ----------- | ------------------------------------------ |
| `+0x00` | u32                | group_key   | Unique                                     |
| `+0x04` | u32                | quest_count | Number of entries                          |
| `+0x08` | Entry[quest_count] | entries     | One quest chain each; see Entry            |

### Entry (10 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | group_key      | Equal to the enclosing Group's `group_key` in every entry             |
| `+0x04` | u16  | quest_chain_id | LOC type 18 `str_id1`; no chain is in two entries                     |
| `+0x06` | u16  | quest_id       | LOC type 18 `str_id2`; `1` except for chain 5901 (`101`)              |
| `+0x08` | u16  | final_quest_id | A quest of the same chain, the one that finishes it; see Final Quests |

`quest_chain_id` and `quest_id` together are the quest key, the `(quest_id << 16) | quest_chain_id` of `allquestlist.bss` read as two u16 values.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No entry reads a string                        |

## Groups

On client 3474 the file holds 9 groups with 25 entries. Key 4 is not used.

| Group Key | Chains                     | Quests                                                                        |
| --------: | -------------------------- | ----------------------------------------------------------------------------- |
| 1         | 8503 to 8509, 8511         | The eight story chains of the first Land of the Morning Light quest board     |
| 2         | 8529 to 8536               | The eight story chains of the second board, each ending with `Back to Yuunru` |
| 3         | 5901                       | `[Main] Defeat Ancient Weapons` (101) to `[Main] Defeat <Furious> Aakman Temple monsters` (701), quests picked by `gethardcorerankpoint()` |
| 5 to 8    | 9500, 9501, 9502, 9503     | One `[Bonus] Skill Up for ...` chain each: Cooking, Alchemy, Hunting, Training |
| 9         | 9103, 9104, 9105           | The Edania story chains of Orbita, Nymphamaré and Tenebraum                   |
| 10        | 9110                       | `[Edana's Defense Gear] A Piece of Secret` to `[Crafting] NOV (IX) Edana - Furystride` |

## Final Quests

`final_quest_id` names a quest of the entry's own chain in all 25 entries, and both quests have a LOC type 18 title (client 3474). The final quest is not always the highest quest ID of the chain: side quests can follow it.

The Land of the Morning Light board Lua (`panel_morningland_questboard_all.luac`, `panel_morningland_questboard2_all.luac`) keeps its own table per chain: a weight per quest and a `_finalId`. `getProgressPercent(index)` adds the weights of the cleared quests and returns 100 once `_finalId` is cleared.

| Group | Chains | Against the Lua `_finalId` (client 3474)                                                       |
| ----: | -----: | ---------------------------------------------------------------------------------------------- |
| 1     | 8      | Equal in all 8 (8511: `16` of 18 quests, 8508: `30` of 37)                                     |
| 2     | 8      | The file names `Back to Yuunru`, the highest quest of each chain, whose condition is clearing the Lua `_finalId` (8529: `26`, condition `clearquest(8529,22)<or>clearquest(8529,25)`, `_finalId` 25) |

In `quest.dbss` the final quest ends the chain's main line and the higher quest IDs branch off earlier quests: 8511/16 `Deep Night, Suspicious Dolswe` ends the 1 to 16 line, while 8511/17 and 8511/18 require quests 8 and 9; in group 9, 9104/29 `Grim Tidings` ends the 1 to 29 line, while 9104/30 requires quest 15.

## Field Names

The names come from the data. The file is not in the client 1784 archive. A private server's `DataSheets.bexcel` and compiled `binary/` folder on client 1784 have no sheet or file for it, and no text in the server dump or the 2016 PDB has `ProgressGroup` in it; their `QuestProgress` names are the quest state flags (`gc::QuestProgressType`, `QuestProgressingState`, `IsQuestProgressing`). `final_quest_id` follows the group 1 match with the board's `_finalId` and the group 2 conditions above.

## Notes

- Decompressed size on client 3474: `342` bytes, 9 groups and 25 entries, `8 + 9 * 8 + 25 * 10 + 12`.
- The Land of the Morning Light hidden chains on the boards' `_hiddenPercentInfo` lists (8510, 8512 to 8515, 8524, 8537 to 8541) are not in the file.
- The entries of group 1 are not in board order: the file lists 8511, 8504, 8505, 8506, 8508, 8507, 8503, 8509, the board 8503 to 8509, then 8511.
- None of the 3,073 client Lua files (`luacscript/x64/`, client 3474) names the file or calls a function with `QuestProgressGroup` in its name. `progressGroup` in `panel_window_quest_all_2.luac` (`makeProgressGroup`, `setProgressGroup`) groups the quests in progress in the quest window and reads no group key.

## Open Questions

### Which Code Reads the Group Keys

The board Lua hard-codes its chains, weights and `_finalId` values and does not read this file, so the reader is client or server code that the Lua does not show. Group key 4 is missing, and why groups 5 to 8 hold one chain each instead of one group for the four `[Bonus] Skill Up` chains is not known. On group 2 the Lua `_finalId` is one to four quests before the file's `final_quest_id`, and the second board's `getProgressPercent` returns 100 at `_finalId`, so whatever reads the file's `Back to Yuunru` value is not the board's percentage.
