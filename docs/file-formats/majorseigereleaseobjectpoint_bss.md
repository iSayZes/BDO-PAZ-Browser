# `majorseigereleaseobjectpoint.bss` Format

## Purpose

The Conquest War (major siege) liberation points per siege object: rows
of a `characterstatic.dbss` character key and its point value. On client
3482 the 71 rows cover the guild siege buildings: command posts, field
HQs and forts are worth `150`, the Barricade and the Defense Tower `1`.
The file name keeps the client's spelling `seige`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3482    | `majorseigereleaseobjectpoint.bss` | 446   | 71 Row  | 6         |

| Layout | File                               | Known          | Unknown    |
| ------ | ---------------------------------- | -------------- | ---------- |
| 1      | `majorseigereleaseobjectpoint.bss` | 446 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

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

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                      |
| ------- | ---- | ------------- | ---------------------------------------------------------- |
| `+0x00` | u16  | character_key | `characterstatic.dbss` key of the siege object; one row each |
| `+0x02` | u32  | object_point  | Liberation points of the object; `1` to `150` on client 3482 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `MajorSiegeLiberationObjectPoint` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CharacterKey` and
`MajorSiegeObjectPoint`, and its 25 rows match the 25 rows of the
client 1784 file by key and value (25 of 25). `object_point` is
`MajorSiegeObjectPoint`; the sheet's `#CharacterKeyName` note column
names the keys `[길드] 점령전 바리케이드` ([Guild] Conquest War
barricade) and the other Conquest War buildings.

## Notes

- The rows are not sorted by key.
- Clients 1784 to 2765 have 25 rows (170 bytes); client 3002 and later have 71,
  adding keys in the `12797` to `12841` and `62403` to `62418` ranges
  that repeat the building names of the first 25. Client 3482 rates many objects lower than
  client 1784: the Medium Siege Tower Factory `2049` is worth `15`
  there and `50` on client 1784, the Big Hwacha `31078` `40` and `100`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/majorsiege_tables.py`:
  the character key with its name, and the points.
