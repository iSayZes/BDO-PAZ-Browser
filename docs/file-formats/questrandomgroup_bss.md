# `questrandomgroup.bss` Format

## Purpose

The random quest groups that the quest condition `checkRandomGroup(group, index)` in [`quest.dbss`](quest_dbss.md) reads. Each 32-byte row names a group key, the number of quest slots in the group and the quest chain they belong to. On client 3474 the file holds one group: key `1`, 37 slots, chain 2322, the `[Academy] [Weekly ...]` quests of the Olvia Academy. The plain PABR file holds the rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | --------------------- | --------- |
| 1      | 3251 and later | 3474    | `questrandomgroup.bss` | 52    | 1 Row, 1 String Table | 32        |

| Layout | File                   | Known        | Unknown      |
| ------ | ---------------------- | ------------ | ------------ |
| 1      | `questrandomgroup.bss` | 30 B (57.7%) | 22 B (42.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

The handler reads no other file, and no field is a LOC key. The quests that call `checkRandomGroup` are in [`quest.dbss`](quest_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of rows; `1` on client 3474             |
| `+0x08`             | Row[count]   | rows               | See Row                                        |
| `rows+0x00`         | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end (`8 + 32 * count`) |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape [`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) and [`questprogressgroup.bss`](questprogressgroup_bss.md) use (`_common/pabr_strings.py`).

### Row (32 bytes)

| Offset  | Type    | Field          | Notes |
| ------- | ------- | -------------- | ----- |
| `+0x00` | u64     | unknown_00     | `0x00007FF79B368530` on client 3474, an address in the range a 64-bit Windows program image loads at; see Notes |
| `+0x08` | u32     | group_key      | The first argument of `checkRandomGroup(group_key, index)` in `quest.dbss`; `1` |
| `+0x0C` | u16     | quest_count    | Number of quest slots, the `index` values `0` to `quest_count - 1`; `37` |
| `+0x0E` | u16     | quest_chain_id | Quest chain of the slots, LOC type 18 `str_id1`; `2322` |
| `+0x10` | u16     | draw_count     | Quests of the group a student is offered per week; `3` |
| `+0x12` | u16     | unknown_12     | `115` |
| `+0x14` | u32     | unknown_14     | `168`; see Open Questions |
| `+0x18` | bytes[8] | unknown_18    | `04 00 50 00 41 00 43 00` |

The split of `+0x10` to `+0x17` into u16, u16 and u32 follows the zero bytes of the one row; nothing else confirms it.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Group 1

On client 3474, 37 records of `quest.dbss` call `checkRandomGroup`, all with group `1`: quests 1 to 37 of chain 2322, each with `checkRandomGroup(1, quest_id - 1);checkOlviaAcademyStudent();` as its `condition_script`. No other quest condition or action script calls it.

| Quest IDs (chain 2322) | Title tag                   | Quests |
| ---------------------- | --------------------------- | -----: |
| 1 to 13, 37            | `[Academy] [Weekly Combat]` | 14     |
| 14 to 26               | `[Academy] [Weekly Life]`   | 13     |
| 27 to 36               | `[Academy] [Weekly Visit]`  | 10     |

Every one of the 37 is accepted at `Bulletin Board` (`accept_dialog_key`) and handed in to an NPC (`complete_dialog_key`): Cliff for Combat quests 1 to 13, Justin Bartali for quest 37, and 18 different NPCs for the Life and Visit quests.

Chain 2321 (`[Academy] [Weekly] Bumblin' Buccaneers Brawl`, one quest) has no `checkRandomGroup` call and is not in the group.

## Field Names

The names come from the data. `group_key` is the group argument of `checkRandomGroup` (the only key the scripts use is `1`, the row's key). `quest_count` is `37`, the number of quests that call `checkRandomGroup(1, ...)` and one more than their highest index `36`. `quest_chain_id` is `2322`, the chain all 37 belong to. `draw_count` is `3`, and I checked in game that the Academy bulletin board offers 3 weekly quests per week with mixed tags (not one per Combat, Life and Visit tag). The file is not in the client 1784 archive. A private server's `DataSheets.bexcel` and `binary/` folder on client 1784 have no sheet or file for it, no `.xlsm` file there has `random` and `quest` in its name, and neither the 2016 PDB nor the server dump of client 1784 has a type or text with `RandomGroup` in it outside an instance-field loader message.

calpheonlabs (`questrandomgroup.bss.mdx`) reads the same 32-byte row and keeps it as raw bytes, since it found no count, join or consumer to split it by. The `quest.dbss` conditions above are that join for `+0x08` to `+0x0F`.

## Notes

- Decompressed size on client 3474: `52` bytes, `8 + 1 * 32 + 12`.
- `unknown_00` is not a game value. On client 3474 only two `gamecommondata/binary/` files hold a u64 between `0x00007FF79A000000` and `0x00007FF79BFFFFFF`: this row at `+0x00` (`0x00007FF79B368530`) and `guildhonorsystem.bss` (not documented yet) at file offset `0` (`0x00007FF79B062F88`). Both look like a pointer of the program that wrote the file, stored with the row.
- `unknown_18` (`04 00 50 00 41 00 43 00`) decodes as UTF-16 `4`, `P`, `A`, `C`. With the pointer at `+0x00`, this fits leftover memory written out with the row, so the two fields may hold no data.
- None of the 3,073 client Lua files (`luacscript/x64/`, client 3474) names the file or `checkRandomGroup`. `panel_widget_randomquestinfo_all.luac` is the Agris fever quest tooltip (`getQuestFeverPoint()`) and reads no random group.
- `checkRandom(n, ...)` in the conditions of 240 other quests (client 3474) is a different function with no group key.

## Open Questions

### What `unknown_12`, `unknown_14` and `unknown_18` Hold

`unknown_14` is `168`, the hours of a week (7 x 24), and the group holds the weekly Academy quests, so it may be the draw period in hours. `unknown_12` (`115`) and `unknown_18` match nothing found in `quest.dbss`, LOC or the Lua. calpheonlabs reports that the row bytes at `+12` and `+16` differ between two builds it read. Quest 37 (`[Weekly Combat] Resplendently-lit Gemstone`) comes after the Visit quests, which fits a `quest_count` that grew, but I have only the client 3474 file.
