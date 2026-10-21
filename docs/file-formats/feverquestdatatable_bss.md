# `feverquestdatatable.bss` Format

## Purpose

The Agris Fever quests: one 8-byte row per quest with the Agris Fever
points that accepting it costs. On client 3474 the file lists the eleven
quests of chain 9026 (`Agris: Challenging the Bashims` to `Agris: Tensions
at the Sulfur Mine`), each at `15000`. The quest window and the world map
quest widget show the cost as `Consume {point} Agris Point(s)`. The plain
PABR file holds the rows, then an empty string table. The drop skills that
Agris Fever applies are in [`fevertimeskill.bss`](fevertimeskill_bss.md),
next to this file in the same PAZ.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 1      | 1784 and later | 3474    | `feverquestdatatable.bss` | 108   | 11 Fever Quest Row | 8         |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `feverquestdatatable.bss` | 108 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                      |
| --------------------- | -------- | ------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field              | Notes                                        |
| ------------------- | ---------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                    | count              | Number of rows                               |
| `+0x08`             | Fever Quest Row[count] | rows               | 8-byte rows repeated `count` times           |
| `rows+0x00`         | String Table           | string_table       | See String Table                             |
| `string_table+0x00` | u32                    | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32                    | zero               | Always `0`                                   |

The string table has the shape `specialquestinfo.bss` and
`questjournalvideoinfo.bss` use (`_common/pabr_strings.py`). The rows are in
quest order, chain first.

### Fever Quest Row (8 bytes)

| Offset  | Type | Field                   | Notes                                                                    |
| ------- | ---- | ----------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | quest_chain_id          | Quest chain (main ID); `quest_id << 16 \| quest_chain_id` is the `packed_quest_id` of a `quest.dbss` record |
| `+0x02` | u16  | quest_id                | Quest within the chain (sub ID)                                          |
| `+0x04` | u32  | consumption_fever_point | Agris Fever points that accepting the quest costs                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Field Names

The `FeverQuest` sheet of a private server's `DataSheets.bexcel` on client
1784 has three columns: `QuestGroup` (`quest_chain_id`, the name the other
quest tables use), `QuestID` (`quest_id`) and `ConsumptionFeverPoint`
(`consumption_fever_point`). Its 18 rows match the client 1784 file in all
18 rows, in order. The client 3474 file keeps the first 11 of them (chain
9026) with the same values. The server executable of that private server
names the record type `FeverQuestStaticStatus` and its manager
`FeverQuestStaticStatusManager`, which links each row to a quest by
`QuestNo`. The 2016 PDB has no `Fever` symbol.

## Notes

- On client 3474 the file is `108` bytes: 11 rows for quests 9026 / 1 to
  9026 / 11, each at `15000`. Every row is a `quest.dbss` record of category
  9 (Event), and each of them has `checkFeverPoint()>14999` in its
  `condition_script`, the same threshold as the row's cost. No other
  `quest.dbss` record calls `checkFeverPoint`; quests 4465 / 2 and 50041 / 1
  spend points through `checkusefeverpoint(N)` in their action script and
  have no row here.
- Client 1784 has the same layout: `164` bytes, 18 rows. The 7 rows the
  live file dropped are 9030 / 3 to 9030 / 5 (the Vaha weekly quests) and
  9035 / 1 to 9035 / 4 (the Sycrakea weekly chests), each at `20000`. On
  client 3474 those quests are in `quest.dbss` with `getLevel()>99` as their
  only condition, while the item texts of the Vaha quest items (LOC type 0,
  `757175` and `757188`) still say they need 10,000 Agris Fever points.
- The client Lua reads the cost per quest as
  `questStaticInfo:getQuestFeverPoint()`. `panel_window_questinfo_all_1.luac`
  and `panel_widget_randomquestinfo_all_1.luac` show it with the string
  `LUA_WINDOW_QUEST_AGRISDESC` (`Consume {point} Agris Point(s)`) when it is
  above `0`; on the world map the quest window gets an accept button that
  calls `ToClient_AcceptQuest`. Both need contents group `1651`
  (`_ContentsGroup_FeverQuest`), the world map widget also `1654`
  (`_ContentsGroup_WorldmapFeverQuest`). No Lua file names this table.
