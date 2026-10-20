# `specialquestinfo.bss` Format

## Purpose

Special quest groups: each group key lists packed quest IDs. The `quest.dbss` action script call `alreadyclearspecialquest(group)` names a group by its key, and each quest that calls it asks for the content the group lists: quest 4464 / 12 `[Suggested] Complete [Pet] Lauren's Fluffy` calls group 2, which lists four `[Pet] Lauren's Fluffy` quests of chain 21416, and quest 4464 / 18 `[Succession/Awakening] Continue to Grow Strong After Succession/Awakening` calls group 4, which lists one awakening, succession or ascension quest per class. The plain PABR file holds the groups, then an empty string table.

Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, as in [`allquestlist.bss`](allquestlist_bss.md) and [`specialquestlist.bss`](specialquestlist_bss.md), and is the `packed_quest_id` of a [`quest.dbss`](quest_dbss.md) record.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records  | Row bytes                |
| ------ | -------------- | ------- | ---------------------- | ----- | -------- | ------------------------ |
| 1      | 1784 and later | 3474    | `specialquestinfo.bss` | 1,560 | 36 Group | 12 to 140, 43 on average |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `specialquestinfo.bss` | 1,560 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                             |
| --------------------- | -------- | ---------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of groups                               |
| `+0x08`             | Group[count] | groups             | Variable-size groups, back to back; see Group  |
| `groups+0x00`       | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the groups end |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape `itemequipgroup.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` groups ends exactly at `string_table_start`.

### Group (variable: 12 bytes + quests)

| Offset  | Type             | Field            | Notes                                                                  |
| ------- | ---------------- | ---------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32              | group_key        | Unique; the argument of `alreadyclearspecialquest`                     |
| `+0x04` | u64              | quest_count      | Number of quests; `0` on groups 11 and 24 (client 3474)                |
| `+0x0C` | u32[quest_count] | packed_quest_ids | `(quest_id << 16) \| quest_chain_id`, a `quest.dbss` `packed_quest_id` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No group reads a string                        |

## Script Use

`alreadyclearspecialquest(group)` sits alone in the `action_script` of the quests that call it, except for quest 50032 / 1, which adds `clearQuest(50031,1)`. No `condition_script`, no `detail_dialog.dbss` script and no client Lua file (`luacscript/`) names the call or the file; `specialQuestInfo` in `panel_window_achievement.luac` is a local holding an Adventure Log page quest. On client 3474, 37 `quest.dbss` quests call it with 29 of the 36 group keys; groups 11, 12, 14, 19, 24, 34 and 36 have no caller.

Callers and groups on client 3474, grouped by what the group lists:

| Group Keys | Group Lists                                                          | Called By                                                                                   |
| ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 2, 3, 20, 21, 31 | `[Pet]` quests of chain 21416, one pet each                    | 4464 / 11 to 15, `[Suggested] Complete [Pet] ...` for the same pet                           |
| 4          | Awakening, succession or ascension quests, one per class (32)        | 4464 / 18; 50032 / 1, 50129 / 1 and 50150 to 50152 `A Whole New Me`                         |
| 7, 8       | `Old Moon's Resplendent` armor (chains 41005 to 41008) and weapon (41009 to 41011) quests | 4471 / 12 and 4471 / 3, the boss gear exchange quests                   |
| 26 to 30   | The Calamity 1 to 5 boss quests of chains 897 to 901                 | 897 / 10 to 901 / 10, `Calamity N Boss - Footsteps of Conquest`                              |
| 18         | Pages 1 to 3 of Igor Bartali's Adventures Vol. I (chain 748)         | 4464 / 17, `[Adventure Log] Complete Igor Bartali's Adventures Vol. I`                       |

## Field Names

The `Quest_Special_Group` sheet of a private server's `DataSheets.bexcel` on client 1784 has two compiled columns: `Group_Index` (`group_key`) and `QuestNoList` (`packed_quest_ids`, as `(chain,quest);` pairs). It matches the client 1784 file in all 17 groups, quest for quest and in order. A `#참조` note column (not compiled) names each group after its quest; group 2 is `로렌의 토실이` (Lauren's Fluffy), the pet of the quests it lists and of its caller 4464 / 12. The server executable of that private server names the record type `SpecialQuestInfoStaticStatus`, its manager `SpecialQuestInfoStaticStatusManager` and the script function `AlreadyClearSpecialQuest`. The 2016 PDB has no `SpecialQuest` symbol.

On client 3474, 10 of the 17 shared groups still match the sheet. Groups 1 and 4 append quests and group 10 adds quest 41013 / 1 in front. Groups 2 and 16 drop quest 21416 / 23 and add other `[Pet]` quests of chain 21416. Group 11 is empty, and group 14 lists quest 40022 / 5 in place of the three quests of chain 21119. Groups 18 to 36 are newer than the sheet.

## Notes

- On client 3474 the file is `1,560` bytes: 36 groups with keys 1 to 36 in key order, 277 quest entries, 237 distinct. No group lists a quest twice; groups 23 and 25 list the same two quests, and groups 16 and 34 differ only by quest 40022 / 12 at the end of group 34.
- Every packed quest ID is a `quest.dbss` record on client 3474. 65 of the 277 entries (60 distinct quests) are Adventure Log pages of `specialquestlist.bss` (`quest_category` 11), in groups 18, 19, 26 to 30 and 32.
- Client 1784 has the same layout: `852` bytes, 17 groups with keys 1 to 17 and 157 quest entries.

## Open Questions

### Any or Every Quest of the Group

The call name says the player has already cleared a special quest, but nothing in the data says whether one quest of the group is enough or every quest is needed. Group 4 lists one awakening, succession or ascension quest per class, and a character clears only its own class's, so it points to one quest being enough; groups 26 to 30 list the ten bosses of one Calamity level, where every quest reads just as well.
