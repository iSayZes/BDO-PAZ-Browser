# Empty BSS Tables Format

## Purpose

PABR `.bss` tables the client ships with no records. Each is 20 bytes: the
`PABR` magic, a record count of `0`, a string table with no strings and the
8-byte PABR trailer. Every file below is that on client 3474. On the two
older clients checked it is the same 20 bytes, not in the archive, or (four
files) a table with records that this doc does not cover:

| File                                  | Client 1784 | Client 1485 |
| ------------------------------------- | ----------- | ----------- |
| `audiorenewal.bss`                    | empty       | empty       |
| `beginnerroadmaplinkurldata.bss`      | absent      | absent      |
| `cashproduct_discountperiodcheck.bss` | empty       | empty       |
| `cashproductcachedata.bss`            | records     | records     |
| `charactertrigger.bss`                | records     | records     |
| `commonskill.bss`                     | empty       | empty       |
| `dropuiurlinfo.bss`                   | absent      | absent      |
| `enchantlightstone.bss`               | absent      | absent      |
| `equipitemchanage.bss`                | records     | absent      |
| `fishinginfo.bss`                     | empty       | empty       |
| `instancefieldenteroption.bss`        | empty       | absent      |
| `instancefieldmanagement.bss`         | empty       | empty       |
| `itembundle.bss`                      | empty       | empty       |
| `lightstoneenchantgroup.bss`          | absent      | absent      |
| `naktype.bss`                         | empty       | records     |
| `normalgroupquest.bss`                | empty       | empty       |
| `openuiwhennak.bss`                   | absent      | absent      |
| `preloadpcactioncharacter.bss`        | empty       | empty       |
| `shadowarenalist.bss`                 | empty       | empty       |
| `skillselectuiinfo.bss`               | absent      | absent      |
| `spawngroup.bss`                      | empty       | empty       |
| `tempcashstaticstatus.bss`            | absent      | absent      |

The Lightstone names point at Lightstone enhancement and Lightstone
enhancement groups, but no record, Lua function or reference source shows
what a row would hold. `normalgroupquest.bss` is the quest list of the
quest widget's group quest line, a feature the live client keeps off; see
[Normal Group Quests](#normal-group-quests).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------------- | ----- | -------------- | --------- |
| 1      | 1230 and later | 3474    | `audiorenewal.bss`                    | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `beginnerroadmaplinkurldata.bss`      | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `cashproduct_discountperiodcheck.bss` | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `cashproductcachedata.bss`            | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `charactertrigger.bss`                | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `commonskill.bss`                     | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `dropuiurlinfo.bss`                   | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `enchantlightstone.bss`               | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `equipitemchanage.bss`                | 20    | 1 String Table | 4         |
| 1      | 1230 and later | 3474    | `fishinginfo.bss`                     | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `instancefieldenteroption.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `instancefieldmanagement.bss`         | 20    | 1 String Table | 4         |
| 1      | 1230 and later | 3474    | `itembundle.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `lightstoneenchantgroup.bss`          | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `naktype.bss`                         | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `normalgroupquest.bss`                | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `openuiwhennak.bss`                   | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `preloadpcactioncharacter.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3474    | `shadowarenalist.bss`                 | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `skillselectuiinfo.bss`               | 20    | 1 String Table | 4         |
| 1      | 1230 and later | 3474    | `spawngroup.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3251 and later | 3474    | `tempcashstaticstatus.bss`            | 20    | 1 String Table | 4         |

| Layout | File                                  | Known         | Unknown    |
| ------ | ------------------------------------- | ------------- | ---------- |
| 1      | `audiorenewal.bss`                    | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `beginnerroadmaplinkurldata.bss`      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproduct_discountperiodcheck.bss` | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproductcachedata.bss`            | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `charactertrigger.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `commonskill.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `dropuiurlinfo.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `enchantlightstone.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `equipitemchanage.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `fishinginfo.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldenteroption.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldmanagement.bss`         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `itembundle.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `lightstoneenchantgroup.bss`          | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `naktype.bss`                         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `normalgroupquest.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `openuiwhennak.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `preloadpcactioncharacter.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `shadowarenalist.bss`                 | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `skillselectuiinfo.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `spawngroup.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `tempcashstaticstatus.bss`            | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | No documented layout |
| 2519   | No documented layout |
| 2107   | No documented layout |
| 1784   | No documented layout |
| 1485   | No documented layout |
| 1230   | Layout 1             |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`)
with no rows. No record structure can be inferred because the files hold no
records.

| Offset              | Type         | Field        | Notes                                              |
| ------------------- | ------------ | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                       |
| `+0x04`             | u32          | count        | Number of records; `0` in every file               |
| `+0x08`             | String Table | string_table | See String Table                                   |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x08` in every file   |
| `string_table+0x04` | u32          | zero         | Always 0                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | `0` in every file    |
| `+0x04` | pstr[string_count] | strings      | Empty                |

## Normal Group Quests

The client Lua on client 3474 reads `normalgroupquest.bss` through four
functions, all behind one switch: `global_contentsoptions.luac` sets
`_ContentsGroup_NormalGroupQuest = ToClient_IsContentsGroupOpen("1684")`,
and contents group `1684` is closed on client 3474
([`contentsgroupoptionstaticstatusmanager.bss`](contentsgroupoptionstaticstatusmanager_bss.md)).
The two quest widgets, `panel_widget_checkedquest.luac` and
`panel_widget_questlist_abyssone.luac`, use them the same way:

| Lua function                                 | Use in the quest widget                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `ToClient_GetNormalGroupQuestCount(group, quest)` | Quest count of the quest's group; the first recent quest with a count other than `0` becomes the group quest |
| `ToClient_GetNormalGroupQuestIndex(group, quest)` | The quest's position in its group, from `0`; shown as `index + 1` of the count                           |
| `ToClient_GetNormalGroupName(group, quest)`  | The group name in the `LUA_GROUPQUEST_WORDS_TITLE` line (`group_quest_name`, `group_quest_now`, `group_quest_total`) |
| `ToClient_GetGroupQuestInfo(group, quest)`   | On `FromClient_ClearNormalGroupQuestInformation`, the next quest of the group; `(0, 0)` ends the line         |

While a group quest is set, the widget shows the next quest under
`ToClient_GetGroupQuestTitle(group, quest)` as acceptable and hides it again
on `FromClient_AcceptNormalGroupQuestInformation` for that quest.

On client 1784 the source sheet and the struct name agree with that:

- The `New_Group_Quest` sheet of a private server's
  `DataSheet_QuestRecommendationTable.xlsm` on client 1784 has the columns
  `QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID` and
  `ContentsGroupKey`, the note columns `#~Title` and `#^E_Merge Index`, and
  no rows. The same sheet in its `DataSheets.bexcel` holds the five compiled
  columns and 0 rows, and its compiled `binary/normalgroupquest.bss` is the
  20 bytes above. The loader's file list names the workbook, which also
  holds the sheets `NewQuest_Table`, `MainQuest_Table`,
  `RecommendationQuest_Table` and `RepetitionQuest_Table`.
- The server dump of that build has four load errors for
  `NormalGroupQuestStaticStatus`: quest `(%#, %#)` has no group name, has a
  wrong key, has a wrong `QuestNo(%#, %#)`, and has no data. A row so holds a
  group name and a quest number `(group, quest)`.
- The same dump's list of string sheet names puts `NormalGroupQuestName`
  between `YachtDiceHandRank` and `SeasonPassQuickQuest`, then
  `SiegeBuildKit` and `YachtGameBoardString`. On client 3474 LOC type 105
  holds the Yar! hand names (`Straight Shot`, `Double Trouble`), 108 the
  Conquest War object descriptions and 109 the Yar! mode descriptions, which
  puts `NormalGroupQuestName` at type 106. The English LOC on client 3474 has
  no type 106 entry.

## Notes

- Raw bytes of every file on client 3474, and of every file marked empty on
  clients 1784 and 1485:
  `50 41 42 52 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The list comes from a scan of every `.bss` under `gamecommondata/binary/`
  on client 3474 for files of at most 40 bytes. The spawn grid files under
  `mapdata_*/spawnplacementfieldgrid/` are left out.
- Four files with these 20 bytes on client 3474 hold records on an older
  client: `cashproductcachedata.bss` (1,509,235 bytes on client 1784,
  1,097.1 KB on client 1485), `charactertrigger.bss` (307 bytes, count 9, on
  clients 1784 and 1485), `equipitemchanage.bss` (464 bytes, count 37, on
  client 1784) and `naktype.bss` (empty on client 1784, 455 bytes and count 4
  on client 1485). The handler reads the live empty layout and rejects the
  older files; their record layouts wait for multi-version support.
- Two 20-byte PABR files are not empty tables: `cashproduct_newbieproduct.bss`
  holds `0x18CAD` at `+0x04` and `petfeedcount.bss` holds `10` there, each
  with no row bytes before the string table, so the u32 is a single value.
  They have their own docs,
  [cashproduct_newbieproduct](cashproduct_newbieproduct_bss.md) and
  [petfeedcount](petfeedcount_bss.md).
- Neither Lightstone file is in the client 1784 archive. The 2016 PDB, a
  private server's `DataSheets.bexcel`, `.xlsm` sheets, compiled `binary/`
  folder and server dump on client 1784 hold no table, file, struct or
  loader with `LightStone` in its name. That `ContentsGroupOption` sheet has
  no key between `1795` and `2000`, so contents group `1801` (below) is newer
  than client 1784 too.
- The installed `BlackDesert64.exe` (client 3473) holds neither Lightstone
  file name as ASCII or UTF-16 text, so it does not show the loader or its
  struct.
- The client Lua on client 3473 (3,073 `.luac` files) names neither
  Lightstone file. `global_contentsoptions.luac` sets
  `_ContentsGroup_EnchantLightStone = ToClient_IsContentsGroupOpen("1801")`,
  and no other Lua file reads `_ContentsGroup_EnchantLightStone`. The
  Lightstone bag (`_ContentsGroup_LightStoneBag`, contents group `1815`) and
  the set lookups (`ToClient_getLightStoneSet`, read from
  [`lightstoneset.bss`](lightstoneset_bss.md)) are separate features.
- The 2016 PDB has no `NormalGroupQuest` type.
- calpheonlabs lists `normalgroupquest.bss` with a decoder but no field
  ledger, so it gives no layout to compare.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) with the
  PABR reader in `_bss/empty_tables/parser.py` previews every file in
  `_bss/empty_tables/tables.py`. A file that declares a record or a string
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- The zero-count `.dbss` tables have their own doc:
  [empty](empty_dbss.md).

## Open Questions

### Record Layout

No client checked has a record in any of these files, so every row layout
is unknown. When a client ships `count > 0`, the file moves to its own doc
and handler, with rows starting at `+0x08` and ending at `table_start`. For
`normalgroupquest.bss` the five compiled `New_Group_Quest` columns are the
lead (`QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID`,
`ContentsGroupKey`); their types and order in the file are unknown. Whether
the group names come from LOC type 106 keyed by `QuestGroupKey`, as the
group names of the four quest lists of [`newquest.bss`](newquest_bss.md)
come from their own LOC types, is open too.

### Contents Group 1801

The Lua defines `_ContentsGroup_EnchantLightStone` for contents group `1801`
but never reads it. Whether that group gates whatever reads these two tables
is unknown.
