# `timeattackranking.bss` Format

## Purpose

The characters of the time attack rankings: a u32 count after the PABR
magic, then one u16 character key per entry. On client 3474 the list is
the Advanced Altar of Training (`27284`), five Kzarka variants (`24385` to
`24381`) and the two Mirumok Offin characters (`23751`, `23767`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 1230 and later | 3474    | `timeattackranking.bss` | 36    | 1 String Table | 4         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `timeattackranking.bss` | 36 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | Layout 1 |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                    | Field           | Notes                                                      |
| -------------------- | ----------------------- | --------------- | ---------------------------------------------------------- |
| `+0x00`              | char[4]                 | magic           | ASCII `PABR`                                               |
| `+0x04`              | u32                     | character_count | Number of character keys                                   |
| `+0x08`              | u16[character_count]    | character_key   | `characterstatic.dbss` key; the handler shows its LOC type 6 name |
| `character_key+0x00` | String Table            | string_table    | See String Table                                           |
| `string_table+0x00`  | u32                     | table_start     | Offset of the string table, where `character_key` ends     |
| `string_table+0x04`  | u32                     | zero            | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is
named after the file. The server dump of that client reads it in
`CharacterStaticStatusManager::readFromBinary()` ("timeattackRanking Open
Failed."), and every key resolves to a character name (LOC type 6), so
`character_key` names the meaning.

The keys line up with the `TimeAttackType` column of the
`Character_Table` sheet on client 1784: all 8 of 8 keys of the client 1784
file have a time attack type, and the client 1784 file is byte for byte
the private server's compiled `binary/timeattackranking.bss`. The sheet
sets a type on 9 more characters that the file leaves out.

| Key (client 1784 and 3474) | Name (LOC type 6, client 3474) | `TimeAttackType` | `TimeAttackLimitMinute` |
| -------------------------- | ------------------------------ | ---------------- | ----------------------- |
| `27284`                    | Advanced Altar of Training     | `2`              | `30`                    |
| `24385` to `24381`         | Transcended, Consumed, Restrained, Transmuting and Deprived Kzarka | `3` | `7` |
| `23751`                    | Mirumok Watcher Offin          | `1`              | `30`                    |
| `23767`                    | Mirumok Destroyer Offin        | `1`              | `30`                    |

The sheet's rows with a type that the file does not list are `23754` and
`23769` (Watcher Offin Tett, type `1`), `27134` to `27138` (the five
Sacraments) and `27337` (Ancient Puturum, type `2`), and `28571` (type `0`,
no LOC type 6 name on client 3474).

## Notes

- Raw bytes on clients 1784 to 3474:
  `50 41 42 52 08 00 00 00 94 6A 41 5F 40 5F 3F 5F 3E 5F 3D 5F C7 5C D7 5C 00 00 00 00 18 00 00 00 00 00 00 00`
  (36 bytes). Clients 1230 and 1485 list 3 keys: `27284`, `23751` and
  `23767`. The file is not in the archives of client 794.
- The boss ranking window (`panel_window_monsterranking.luac`, client 3474)
  lists time attack groups with `ToClient_GetTimeAttackListCount()` and
  `ToClient_GetTimeAttackGroupInfo(index)`, each with a group name and a
  family or guild ranking; no Lua call reads a character key list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per character key.
