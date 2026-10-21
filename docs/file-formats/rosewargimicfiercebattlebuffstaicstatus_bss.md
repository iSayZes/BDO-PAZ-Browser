# `rosewargimicfiercebattlebuffstaicstatus.bss` Format

## Purpose

The Rose War gimmick sanctums and what they hand out: one row per gimmick
character with five (character key, u32) pairs and a u8. On client 3474
the file has one row, for Mysterious Statue (`21699`), the statue of the
Altar of Spirits sanctum in
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md).
Its pairs are Cannon with `4`, Elephant with `3`, Ballista with `1`,
Ancient Chariot with `1`, and an empty pair.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                          | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | --------------------------------------------- | ----- | --------------------- | --------- |
| 1      | 3002 and later | 3474    | `rosewargimicfiercebattlebuffstaicstatus.bss` | 63    | 1 Row, 1 String Table | 43        |

| Layout | File                                          | Known        | Unknown      |
| ------ | --------------------------------------------- | ------------ | ------------ |
| 1      | `rosewargimicfiercebattlebuffstaicstatus.bss` | 42 B (66.7%) | 21 B (33.3%) |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (43 bytes)

| Offset  | Type | Field                 | Notes                                                                    |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | character_key_1       | `characterstatic.dbss` key; `31111` Cannon on client 3474                |
| `+0x04` | u32  | unknown_04            | `4` on client 3474; see Open Questions                                   |
| `+0x08` | u32  | character_key_2       | `31116` Elephant                                                         |
| `+0x0C` | u32  | unknown_0c            | `3`                                                                      |
| `+0x10` | u32  | character_key_3       | `31112` Ballista                                                         |
| `+0x14` | u32  | unknown_14            | `1`                                                                      |
| `+0x18` | u32  | character_key_4       | `31113` Ancient Chariot                                                  |
| `+0x1C` | u32  | unknown_1c            | `1`                                                                      |
| `+0x20` | u32  | character_key_5       | `0`, no character                                                        |
| `+0x24` | u32  | unknown_24            | `0`                                                                      |
| `+0x28` | u16  | gimmick_character_key | `21699` Mysterious Statue, a `neutral_character_key` of the monster table |
| `+0x2A` | u8   | unknown_2a            | `1`; see Open Questions                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The five `character_key_*`
values and `gimmick_character_key` resolve to LOC type 6 character names.
The minimap Lua (`panel_rosewar_minimap_*.luac`, client 3474) checks a
sanctum with `ToClient_IsRoseWarGimicFierceBattle(characterKeyRaw)` and
reads its buff with `ToClient_GetRoseWarGimicFierceBattleBuffStaticStatusWrapper(fierceBattleKeyRaw):getBuffType()`,
so the row is keyed by the gimmick sanctum's character. The u16 key sits
after the pairs in the row.

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 01 00 00 00 87 79 00 00 04 00 00 00 8C 79 00 00 03 00 00 00 88 79 00 00 01 00 00 00 89 79 00 00 01 00 00 00 00 00 00 00 00 00 00 00 C3 54 01 00 00 00 00 33 00 00 00 00 00 00 00`
  (63 bytes). The file is not in the archives of client 1784.
- The second gimmick sanctum, Ocean Sanctum (`22` in the monster table,
  Mysterious Statue `21700`), has no row.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the gimmick character first.

## Open Questions

### The Buff Type and the Pair Values

The Lua names three gimmick buff types, `__eRoseWarGimicFierceBattleBuffType_Skill`,
`_Spawn` and `_Item`, with the icons `Combine_Etc_RoseWar_Command_Wight_Icon_Buff_1`
to `_3`, but not their values. The pairs name siege objects (Cannon,
Elephant, Ballista, Ancient Chariot), which reads as a Spawn buff with
`unknown_04` to `unknown_24` as how many of each spawn, and `unknown_2a`
(`1`) as the buff type. Neither the type value nor the counts are
confirmed.
