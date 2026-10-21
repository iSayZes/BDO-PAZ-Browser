# `rosewarnodemonsterinfostaicstatus.bss` Format

## Purpose

The images of the Rose War sanctum characters: one row per character key
with two string-table indexes, the sanctum image and the tooltip image. On
client 3474 the file has 62 rows, every character of
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md):
the 20 neutral Faded Relics, the 40 team guardians and the two Mysterious
Statues.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarnodemonsterinfostaicstatus.bss` | 3,724 | 62 Row  | 10        |

| Layout | File                                    | Known            | Unknown    |
| ------ | --------------------------------------- | ---------------- | ---------- |
| 1      | `rosewarnodemonsterinfostaicstatus.bss` | 3,724 B (100.0%) | 0 B (0.0%) |

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

### Row (10 bytes)

| Offset  | Type | Field             | Notes                                                                        |
| ------- | ---- | ----------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | `characterstatic.dbss` key; the handler shows its LOC type 6 name            |
| `+0x02` | u32  | image_ref         | String table index of the sanctum image (`UI_Artwork/ElfWar_Kama_N1.dds`)    |
| `+0x06` | u32  | tooltip_image_ref | String table index of the tooltip image (`UI_Artwork/ElfWar_Kama_Neutral_Tooltip.dds`) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `40` on client 3474                   |
| `+0x04` | pstr[string_count] | strings      | Wide `.dds` paths, each stored once in first-use order   |

## Images

Client 3474. A character shares the sanctum image of the sanctum it
guards, so `image_ref` names the sanctum and `tooltip_image_ref` the
character:

| Characters                                   | `image_path`                           | `tooltip_image_path`                                          |
| -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------- |
| Faded Relic `21811` to `21820`               | `ElfWar_Kama_N1` to `N10`              | `ElfWar_Kama_Neutral_Tooltip`                                 |
| Faded Relic `21821` to `21830`               | `ElfWar_Odyl_S1` to `S10`              | `ElfWar_Odyl_Neutral_Tooltip`                                 |
| Kamasylvia guardians `21831` to `21850`      | the image of the sanctum they guard    | `ElfWar_Kama_Boss_Urugon_Tooltip`, `ElfWar_Kama_Fadus_Bow_Tooltip` and others |
| O'dyllita guardians `21851` to `21870`       | the image of the sanctum they guard    | `ElfWar_Odyl_Salun_Wolf_Tooltip`, `ElfWar_Odyl_Khalk_Tooltip` and others |
| Mysterious Statue `21699`, `21700`           | `IC_00749`                             | `IC_00749_Tooltip`                                            |

All paths start with `UI_Artwork/` and end in `.dds`.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. Every key resolves to a LOC
type 6 character name, and every key is a character of the monster table.
The two index fields are named by the strings they point to: the second
one's paths all end in `_Tooltip.dds`.

## Notes

- The file is 3,724 bytes on clients 3002, 3251 and 3474. Client 3002
  has the same characters and paths, but three O'dyllita guardians sit on
  other sanctum images: Ulutuka (`21862`) on `S6` in place of `S5`, Turo
  Berserker (`21866`) on `S7` in place of `S6`, and Ahib Salun Wolf
  Spearmaiden (`21869`) on `S5` in place of `S7`. The file is not in the
  archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with both paths as text.
