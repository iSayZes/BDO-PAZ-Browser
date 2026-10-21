# `cutscenecharacterdata.bss` Format

## Purpose

The character keys set aside as cutscene actors: the player stand-ins
(`401` PC, `410` Player), the tutorial actors `411` to `430`, the
`Sequence_NPC_*` library from `62001` up, and story characters added later
(`29472` Kalqueesh, `25696` Bari). Each entry is one u16 key of
[`characterstatic.dbss`](characterstatic_dbss.md). The file holds the
`Index` column of the `Character_Table_CutScene` sheet, packed as a PABR
list with an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `cutscenecharacterdata.bss` | 264   | 1 String Table | 4         |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 1      | `cutscenecharacterdata.bss` | 264 B (100.0%) | 0 B (0.0%) |

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

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key; a key without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Character name (type `6`, `str_id1` = `character_key`)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u16 rows with an empty string table, the shape of
[`itemimprovementdefaultdisplaylist.bss`](itemimprovementdefaultdisplaylist_bss.md)
with u16 rows in place of u32.

| Offset              | Type         | Field              | Notes                                   |
| ------------------- | ------------ | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                            |
| `+0x04`             | u32          | count              | Number of keys; `122` on client 3474    |
| `+0x08`             | u16[count]   | character_keys     | `characterstatic.dbss` keys; unique     |
| `character_keys+0x00` | String Table | string_table     | Empty string table                      |
| `string_table+0x00` | u32          | string_table_start | End of the keys (`8 + 2 * count`)       |
| `string_table+0x04` | u32          | zero               | `0`                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Key Groups

Key ranges and the developer notes of the `Character_Table_CutScene` sheet
in a private server's `.xlsm` on client 1784; counts and LOC names from
client 3474.

| Keys             | Keys in file | Sheet note (translated)                     | LOC type 6 names                                   |
| ---------------- | ------------ | ------------------------------------------- | -------------------------------------------------- |
| `400` to `410`   | 10           | For cutscenes: PC, object, villagers of each region, boss | Object, PC, Villager, Player          |
| `411` to `430`   | 13           | Tutorial NPCs for staging                   | Tutorial_Illezra_Move, Everfrost_Rare_Fixed        |
| `61032`, `61989` to `61999` | 12 | Not in the sheet                          | A1 Sequence NPC, Sequence NPC                      |
| `44711` to `44714` | 4          | Not in the sheet                            | MediahSequence                                     |
| `62001` to `62047` | 47         | Sequence NPC library, `62001` to `62050`    | Human_Male_Adult_Normal, Other_Mount               |
| `62051` to `62071` | 21         | Sequence monster library, `62051` to `62100` | Monster_Ogre, Monster_Red Nose                    |
| `22914` to `29475` | 15         | Not in the sheet                            | Kalqueesh, Elten, Gumiho, Bari, Lee Duksoo         |

## Field Names

`character_keys` is the `Index` column of the `Character_Table_CutScene`
sheet in a private server's `DataSheets.bexcel` on client 1784, its only
compiled column: the 79 rows match the 79 keys of that client's file in
order, and all 79 are in the client 3474 file. The sheet's note columns
(`#참조1(캐릭터)`, character reference) name each row by its character.

## Notes

- Client 3474 holds the 79 keys of client 1784 plus 43 more. Client 1784
  lists them in ascending order; client 3474 does not (it starts `410`,
  `61990` to `61999`, `61989`, `61032`, `400`), and the order carries no
  meaning found so far.
- On client 3474, `62070` and `62071` have no `characterstatic.dbss` row
  and no LOC type 6 name; every other key has both.
- The server dump of a private server on client 1784 holds the error text
  `CutSceneCharacterStaticStatusManager - linkAndCheckValid` (UTF-16), so
  the server builds a manager over these keys and checks them against the
  character table.
- No client Lua file on client 3474 names the file, the sheet or a
  cutscene character function.

## Open Questions

### What the Client Reads the List For

The client Lua does not read the list, and nothing in the data shows what
membership changes for a character. The 2016 PDB names a function
`PACharacterScene::isCutsceneCharacter`; whether it reads this list is
unknown, since no loader in the PDB names the file.
