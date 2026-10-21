# `voxelregionskillstaticstatusmanager.bss` Format

## Purpose

Skills tied to a voxel region type: a u32 count after the PABR magic, then
one 5-byte row per entry, a u8 value and a `skill.dbss` skill key. On
client 3474 the file has 2 rows, `4` with All-Consuming Heat (skill 42501,
"Edania (Demon Realm) Region Red Lava Debuff") and `8` with Dead Soul's
Chill (skill 42502, "Edania (Demon Realm) Region Blue Ice Debuff").

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `voxelregionskillstaticstatusmanager.bss` | 30    | 2 Row   | 5         |

| Layout | File                                      | Known        | Unknown    |
| ------ | ----------------------------------------- | ------------ | ---------- |
| 1      | `voxelregionskillstaticstatusmanager.bss` | 28 B (93.3%) | 2 B (6.7%) |

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

| File                  | Required | Role                          |
| --------------------- | -------- | ----------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (5 bytes)

| Offset  | Type | Field      | Notes                                                                                   |
| ------- | ---- | ---------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | `4` and `8` on client 3474; unique                                                      |
| `+0x01` | u32  | skill_key  | `skill.dbss` key, `skill_no << 16 \| level`; the handler shows the LOC type 10 skill name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: no sheet of a private server's
`DataSheets.bexcel` on that client and no string of its server dump has
`Voxel` in the name, and the 2016 client predates it. `skill_key` is named
by value: both values (`2785345537` and `2785411073`) are row keys of
`skill.dbss` on client 3474, skills 42501 and 42502 at level 1, and the
LOC type 10 description of each names an Edania region debuff.

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 04 01 00 05 A6 08 01 00 06 A6 00 00 00 00 12 00 00 00 00 00 00 00`
  (30 bytes). The file is not in the archives of clients 794 to 2519.
- `skill.dbss` on client 3474 links buff 42859 (All-Consuming Heat) to
  skill 42501, and buffs 42860 (Dead Soul's Chill) and 40035 (Movement
  Speed -25% for 5 sec) to skill 42502.
- No client Lua file on client 3474 has `VoxelRegion` in a string.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per skill.

## Open Questions

### Region Type Values

`unknown_00` is `4` for the lava debuff and `8` for the ice debuff. The
values look like voxel region types or bit flags (`4` and `8` are single
bits), but no client enum or Lua call with `Voxel` in its name lists them.
