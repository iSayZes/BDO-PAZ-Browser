# `totalquestcountregion.bss` Format

## Purpose

Quest totals. `totalquestcountregion.bss` holds the number of quests per quest region (`CppEnums.QuestRegionType` in the client Lua) and `totalquestcounttype.bss` the number of quests per quest type (`__eQuestType`). Value N of a file counts the quests of enum value N; the files store no keys. Both files share this layout and one handler class. On client 3474 the type file's values are, value for value, how many `quest.dbss` records hold each `quest_category` (see [Quest Types](#quest-types)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `totalquestcountregion.bss` | 88    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `totalquestcounttype.bss`   | 96    | 1 String Table | 4         |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 1      | `totalquestcountregion.bss` | 88 B (100.0%) | 0 B (0.0%) |
| 1      | `totalquestcounttype.bss`   | 96 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hashes of the GAME sheet keys the quest window names regions and types with (see [stringtable](stringtable_bss.md)) |
| `languagedata_en.loc` | Optional | The text of those keys, LOC type 37                                                               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with no count after the magic: the values start at `+0x04` and fill the space up to the string table.

| Offset              | Type               | Field        | Notes                                                          |
| ------------------- | ------------------ | ------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                                   |
| `+0x04`             | u32[..table_start] | quest_count  | One per enum value, in value order; see Quest Regions and Quest Types |
| `quest_count+0x00`  | String Table       | string_table | See String Table                                               |
| `EOF-0x08`          | u32                | table_start  | Offset of the string table, where `quest_count` ends           |
| `EOF-0x04`          | u32                | zero         | Always `0`                                                     |

The parser takes the value count from the trailer: `(table_start - 4) / 4`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No value reads a string                        |

## Quest Regions

`totalquestcountregion.bss` value N is `CppEnums.QuestRegionType` N (`global_define_cpp_enum.luac`). The file has one value per enum value up to `eQuestRegionType_Count`: 18 on client 3474, 13 on client 1784, whose enum ends at `eQuestRegionType_MountainOfEternalWinter`. The name is the GAME sheet key that `_regionString` in `panel_window_quest_all.luac` gives the value, read through `stringtable.bss` and LOC type 37. The names below are the client 3474 order; the handler applies them only to a file with all 18 values (see Notes).

| Value | Enum name                 | GAME sheet key                         | Name (English LOC)                |
| ----- | ------------------------- | -------------------------------------- | --------------------------------- |
| 0     | `None`                    | `LUA_QUESTLIST_HISTORY_TXT_REGION_99`  | Etc.                              |
| 1     | `Balenos`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_1`   | Eastern Balenos                   |
| 2     | `Serendia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_2`   | Serendia                          |
| 3     | `NorthCalpheon`           | `LUA_QUESTLIST_HISTORY_TXT_REGION_3`   | Northern Calpheon                 |
| 4     | `CalpheonBigCity`         | `LUA_QUESTLIST_HISTORY_TXT_REGION_4`   | Calpheon City                     |
| 5     | `Keplan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_5`   | Keplan (Southeastern Calpheon)    |
| 6     | `SouthWestCalpheon`       | `LUA_QUESTLIST_HISTORY_TXT_REGION_6`   | Southwestern Calpheon             |
| 7     | `Media`                   | `LUA_QUESTLIST_HISTORY_TXT_REGION_7`   | Mediah                            |
| 8     | `Valencia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_8`   | Valencia                          |
| 9     | `Kamasylvia`              | `LUA_QUESTLIST_HISTORY_TXT_REGION_9`   | Kamasylvia                        |
| 10    | `Drigan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_10`  | Drieghan                          |
| 11    | `Odilita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_11`  | O'dyllita                         |
| 12    | `MountainOfEternalWinter` | `LUA_QUESTLIST_HISTORY_TXT_REGION_12`  | Mountain of Eternal Winter        |
| 13    | `AbyssOne`                | `LUA_ABYSSONE_MSG_SERVERSELECT_TITLE`  | Abyss One                         |
| 14    | `MorningLand`             | `LUA_QUESTLIST_HISTORY_TXT_REGION_13`  | Land of the Morning Light - Nampo |
| 15    | `Ulukita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_14`  | Ulukita                           |
| 16    | `Edania_1`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_17`  | Outer Edania                      |
| 17    | `Edania_2`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_20`  | Inner Edania                      |

On client 1784 the 13 values add up to 16,877, the record count of that client's `quest.dbss`. On client 3474 the 18 values add up to 18,980, 11 fewer than the 18,991 `quest.dbss` records (see Open Questions).

## Quest Types

`totalquestcounttype.bss` value N is `__eQuestType` N. The value order is the order in which `panel_window_quest_all.luac` lists the `__eQuestType_*` names, and the `_typeString` keys follow it: type N reads `LUA_QUESTLIST_HISTORY_TXT_TYPE_<N+1>`, except `DirectClear`, which reads `LUA_QUESTLIST_HISTORY_TXT_REGION_99`. On client 3474 the 20 values equal the per-category record counts of the `quest.dbss` [Quest Category](quest_dbss.md#quest-category) table for every category `0` to `19` (`16` has no record and holds `0`) and add up to all 18,991 records, so `quest_category` is the quest type. The `Adventurer's Tome` type is category `11`, the journal pages, and `Region Bonus` is category `12`, the quests of `regionmonsterkillquestlist.bss`.

| Value | Enum name                | GAME sheet key                        | Name (English LOC) |
| ----- | ------------------------ | ------------------------------------- | ------------------ |
| 0     | `BlackSpirit`            | `LUA_QUESTLIST_HISTORY_TXT_TYPE_1`    | Black Spirit       |
| 1     | `Main`                   | `LUA_QUESTLIST_HISTORY_TXT_TYPE_2`    | Main               |
| 2     | `Sub`                    | `LUA_QUESTLIST_HISTORY_TXT_TYPE_3`    | General            |
| 3     | `Repeat`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_4`    | Recurring          |
| 4     | `Adventure`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_5`    | Adventure          |
| 5     | `BaseLife`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_6`    | Life               |
| 6     | `OceanLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_7`    | Sailing            |
| 7     | `CraftLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_8`    | Production         |
| 8     | `Contents`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_9`    | Content            |
| 9     | `Event`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_10`   | Event              |
| 10    | `Guild`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_11`   | Guild              |
| 11    | `DirectAccept`           | `LUA_QUESTLIST_HISTORY_TXT_TYPE_12`   | Adventurer's Tome  |
| 12    | `Sudden`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_13`   | Region Bonus       |
| 13    | `SeasonPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_14`   | Season Pass        |
| 14    | `GrowthPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_15`   | Progression Pass   |
| 15    | `DirectClear`            | `LUA_QUESTLIST_HISTORY_TXT_REGION_99` | Etc.               |
| 16    | `Journal`                | `LUA_QUESTLIST_HISTORY_TXT_TYPE_17`   | Journal            |
| 17    | `OlviaAcademyPass`       | none                                  | none               |
| 18    | `OlviaAcademyReward`     | none                                  | none               |
| 19    | `OlviaAcademyCurriculum` | none                                  | none               |

`_typeString` has no key for the three Olvia Academy types; the handler shows their enum names. `LUA_QUESTLIST_HISTORY_TXT_TYPE_16` reads "Instant Clear", but the quest window names `DirectClear` "Etc.".

The client 1784 file holds 17 values that add up to 16,877, the record count of that client's `quest.dbss`. That client's Lua has another enum, `CppEnums.QuestType` (`BlackSpirit` `0` to `Guild` `7`, `Special` `10`, `RegionMonsterKill` `11`, `Production` `15`, `_Count` `16`), which is one value short of the file; the 1784 values are not named here (see Open Questions).

## Notes

- Decompressed sizes: `totalquestcountregion.bss` 88 bytes on client 3474 (`4 + 18 × 4 + 12`) and 68 bytes on client 1784; `totalquestcounttype.bss` 96 bytes on client 3474 (`4 + 20 × 4 + 12`) and 84 bytes on client 1784.
- The quest window (`panel_window_quest_all_2.luac`) shows a completion percentage per region or per type group in its progress tab: `ToClient_GetClearedQuestCountByQuestRegion(region) / ToClient_GetTotalQuestCountByQuestRegion(region) * 100`, and the same pair `ByQuestType` when the list is sorted by type. The totals these getters return have the shape of the two files.
- No sheet of a private server's `DataSheets.bexcel` on client 1784 has `TotalQuest` in its name or a column, while that server's `binary/` folder holds both files.
- The handler (`_bss/totalquestcount/`) gives each value its enum value as key (`quest_region` or `quest_type`), the quest window name next to it, and `quest_count`. It names the values only when the file holds at least as many values as the client 3474 enum (18 regions, 20 types); a shorter file, such as both client 1784 files, gets an empty name column, since its enum order is not checked against the client 3474 one. A value past the end of the enum, on a later client, also has no name.

## Open Questions

### Eleven Quests Without a Region Count

On client 3474 the region values add up to 18,980 and the type values to 18,991, the `quest.dbss` record count; on client 1784 both files add up to all 16,877 records. The 11 missing quests may carry a region value outside `QuestRegionType` (the enum has no value past `Edania_2` and `_Count` `18`), but `quest.dbss` has no decoded region field to check which quests they are.

### What Fills the Getters

`ToClient_GetTotalQuestCountByQuestRegion` and `ToClient_GetTotalQuestCountByQuestType` take a region or type value and return a total, which is what these files store per value, but nothing in the client Lua names the files. The client could also count the totals from `quest.dbss` itself, which on client 3474 gives the same type totals.

### Client 1784 Quest Types

The client 1784 type file has 17 values, while that client's Lua `CppEnums.QuestType` ends at `_Count` `16` and has no names for values `8`, `9` and `12` to `14`. Its value `6` holds 6,169 of the 16,877 quests, more than any other type, so the 3474 names (`6` is `OceanLife`) do not carry over. The 1784 `quest.dbss` layout has no decoded `quest_category` to count against. The handler shows no names for the client 1784 files.
