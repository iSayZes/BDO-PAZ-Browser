# `worldbossnonpkregion.bss` Format

## Purpose

The non-PK regions of each world boss: one row per boss character key with
a list of `regioninfo.bss` region keys. On client 3474 the file has 35
rows: the world bosses (Kzarka, Nouver, Karanda, Kutum, Offin, Garmoth,
Vell, Quint, Muraka) and their stronger forms, Black Wings, the Land of the
Morning Light bosses (Golden Pig King, Sangoon, Uturi, Bulgasal and the
four Dark Bonghwang), and event bosses such as Isabella, Targargo, Piku and
Gift Box, each with the regions around its spawn (Serendia Shrine for
Kzarka, Garmoth's Nest for Garmoth, Margoria for Vell).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | ----------------------- |
| 1      | 1485 and later | 3474    | `worldbossnonpkregion.bss` | 408   | 35 Row  | 10 to 18, 11 on average |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `worldbossnonpkregion.bss` | 408 B (100.0%) | 0 B (0.0%) |

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
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                     |
| --------------------- | -------- | -------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6; region names, LOC type 17   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 8 bytes + region keys)

| Offset  | Type              | Field         | Notes                                                                     |
| ------- | ----------------- | ------------- | ------------------------------------------------------------------------- |
| `+0x00` | u16               | key           | Row key; equals `character_key` on every row                              |
| `+0x02` | u16               | character_key | `characterstatic.dbss` key of the boss; the handler shows its LOC type 6 name |
| `+0x04` | u32               | region_count  | Number of region keys, `1` to `5` (client 3474)                           |
| `+0x08` | u16[region_count] | region_keys   | `regioninfo.bss` keys, ascending; the handler shows their LOC type 17 names |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `WorldBossNonPkRegion` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `RegionKey` (a list) and
`ContentsGroupKey` (`1` on every row). Its 17 character keys are the 17 rows
of the client 1784 file. Its region lists are the file's lists with region
877 (Garmoth's Nest) added to each, except Garmoth's own row, which lists
877 alone in both; the private server's compiled file has the same extra
877, so the sheet was edited after the client file was built. The file does
not store `ContentsGroupKey`. The private server's server executable logs
`WorldBossNonPkRegionStaticStatus::set() _key, key(%#)`, which names `key`.

## Notes

- The file grew from 17 rows (214 bytes, client 1784) to 35 (408 bytes,
  client 3474); clients 2107, 2519, 3002 and 3251 lie between.
- Several bosses share a region list: the three Isabella rows list Naga
  Marsh and Costa Farm, Vell (`23080`, `23162`) lists the three Margoria
  regions, Golden Pig King and Dark Bonghwang `28736` list Golden Pig Cave.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.
  `test_pvp_tables.py` checks that `key` equals `character_key`.

## Open Questions

### Non-PK Rule

What the client does with the list. The sheet and file name say the regions
turn non-PK while the boss is up, but no client Lua reads the file, so the
rule is unconfirmed in game.
