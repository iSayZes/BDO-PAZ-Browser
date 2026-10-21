# `hardcorechanneletcoptionstaticstatus.bss` Format

## Purpose

The settings of the Hardcore channel: 83 bytes of unnamed numbers, a
counted list of two (u8, f32, u16) entries, an f32 and the class types that
can create a Hardcore character. On client 3474 that class list holds 29
class types, every playable class but Wukong, Seraph and Agent. The class
types are those of [`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md),
which holds a stat row per class type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------ | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `hardcorechanneletcoptionstaticstatus.bss` | 154   | 2 Entry | 7         |

| Layout | File                                       | Known        | Unknown       |
| ------ | ------------------------------------------ | ------------ | ------------- |
| 1      | `hardcorechanneletcoptionstaticstatus.bss` | 49 B (31.8%) | 105 B (68.2%) |

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

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Class names, LOC type 21    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                         | Field                | Notes                                                              |
| ---------------------------- | ---------------------------- | -------------------- | ------------------------------------------------------------------ |
| `+0x00`                      | char[4]                      | magic                | ASCII `PABR`                                                       |
| `+0x04`                      | u32                          | unknown_04           | `60` on client 3474                                                |
| `+0x08`                      | u32                          | unknown_08           | `2` on client 3474                                                 |
| `+0x0C`                      | u16                          | unknown_0c           | `60` on client 3474                                                |
| `+0x0E`                      | u8                           | unknown_0e           | `1` on client 3474                                                 |
| `+0x0F`                      | u32                          | unknown_0f           | `60` on client 3474                                                |
| `+0x13`                      | u32                          | unknown_13           | `50` on client 3474                                                |
| `+0x17`                      | u32                          | unknown_17           | `100000` on client 3474                                            |
| `+0x1B`                      | u32                          | unknown_1b           | `300000` on client 3474                                            |
| `+0x1F`                      | u32                          | unknown_1f           | `10000` on client 3474                                             |
| `+0x23`                      | u32                          | unknown_23           | `3000` on client 3474                                              |
| `+0x27`                      | u32                          | unknown_27           | `200000` on client 3474                                            |
| `+0x2B`                      | u32                          | unknown_2b           | `300000` on client 3474                                            |
| `+0x2F`                      | u32                          | unknown_2f           | `3` on client 3474                                                 |
| `+0x33`                      | u32                          | unknown_33           | `500` on client 3474                                               |
| `+0x37`                      | u32                          | unknown_37           | `300` on client 3474                                               |
| `+0x3B`                      | i32                          | unknown_3b           | `-40` on client 3474                                               |
| `+0x3F`                      | u64                          | unknown_3f           | `100` on client 3474                                               |
| `+0x47`                      | u64                          | unknown_47           | `50` on client 3474                                                |
| `+0x4F`                      | u64                          | unknown_4f           | `20` on client 3474                                                |
| `+0x57`                      | u32                          | unknown_entry_count  | Number of `unknown_entries`; `2` on client 3474                     |
| `+0x5B`                      | Entry[unknown_entry_count]   | unknown_entries      | See Entry                                                          |
| `unknown_entries+0x00`       | f32                          | unknown_entries_00   | `74.0` on client 3474, the f32 of entry `1`                        |
| `unknown_entries+0x04`       | u32                          | class_count          | Number of `possible_class_types`                                   |
| `unknown_entries+0x08`       | u8[class_count]              | possible_class_types | Class types that can create a Hardcore character; see Classes      |
| `possible_class_types+0x00`  | String Table                 | string_table         | See String Table                                                   |
| `string_table+0x00`          | u32                          | table_start          | Offset of the string table, where `possible_class_types` ends      |
| `string_table+0x04`          | u32                          | zero                 | Always `0`                                                         |

### Entry (7 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | `1` and `2` on client 3474                               |
| `+0x01` | f32  | unknown_01 | `74.0` with `1`, `37.0` with `2` on client 3474          |
| `+0x05` | u16  | unknown_05 | `1` on both entries                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Classes

`possible_class_types` on client 3474, by LOC type 21 name: Warrior (0),
Hashashin (1), Sage (2), Ranger (4), Guardian (5), Scholar (6), Drakania
(7), Sorceress (8), Nova (9), Corsair (10), Lahn (11), Berserker (12),
Maegu (15), Tamer (16), Shai (17), Striker (19), Musa (20), Maehwa (21),
Mystic (23), Valkyrie (24), Kunoichi (25), Ninja (26), Dark Knight (27),
Wizard (28), Archer (29), Woosa (30), Witch (31), Dosa (33) and Deadeye
(34). Wukong (3), Seraph (32) and Agent (35) are missing, besides the
unused class types 13, 14, 18 and 22.

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. `possible_class_types` follows the client
Lua of client 3474: the class select windows
(`panel_lobby_classselect_renew.luac` and `panel_lobby_main.luac`) read
the classes a Hardcore character can take with
`ToClient_getHardCorePossbieClassCount()` and
`ToClient_getHardCorePossbieClassFromIndex(index)`, a count and a class
type per index, and every value of the list has a LOC type 21 class name.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The LOC type 37 server text that opened Hardcore characters to Warrior,
  Ranger, Sorceress and Berserker
  ([`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md)
  Notes) names fewer classes than this list, which holds the same 29 on
  clients 3002 to 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  the class list by name.

## Open Questions

### Unnamed Settings

Which value each Hardcore getter of the client 3474 Lua returns. The Lua
reads `ToClient_isHardCoreChannelEnterPossibleLevel()` (the level in
"LUA_HARDCORECHANNEL_CANTPLAY_NOTIFY"), `ToClient_getHardCoreMaxBossCount()`,
`ToClient_getHardCoreHighRankerMaxCount()`,
`ToClient_getHardCoreRepeatQuestCountMax()`,
`ToClient_getHardCoreExchangeCoinMaxCount()` and
`ToClient_GetHardCoreCharacterRespawnTime()`, and none of them is a plain
match: `60` appears three times, `2` fits the two bosses of
[`hardcorerandomspawncharacterstaticstatusmanager.bss`](hardcorerandomspawncharacterstaticstatusmanager_bss.md),
`3` the three top ranks, `500` and `300` a coin cap and a respawn time.

### Alert Entries

What `unknown_entries` and `unknown_entries_00` hold. The enemy alert
widget (`panel_widget_enemyalert_hardcore_1.luac`) reads
`ToClient_GetHardCoreNearPlayerAlertLevel()` and shows one effect for level
`1` and another for `2`. The entries are numbered `1` and `2`, the f32 of
`2` is half that of `1` (`37.0` and `74.0`), and `unknown_entries_00`
repeats `74.0`, which fits a distance per alert level, but no Lua reads the
values.
