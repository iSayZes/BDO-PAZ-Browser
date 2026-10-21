# `pcgrowthsimply.bss` Format

## Purpose

One fixed row per class type with its Korean class name and a playable flag. The class types and their order are the ones of [pcgrowth](pcgrowth_dbss.md), which reads this file for its Playable column.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1485 and later | 3474    | `pcgrowthsimply.bss` | 1,038 | 47 Row  | 10        |

| Layout | File                 | Known         | Unknown       |
| ------ | -------------------- | ------------- | ------------- |
| 1      | `pcgrowthsimply.bss` | 850 B (81.9%) | 188 B (18.1%) |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Class name (LOC type 21)   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR table with one fixed 10-byte row per class type and a string table of the Korean class names (`_common/pabr_strings.py`).

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | `PABR`                                         |
| `+0x04`             | u32          | count              | Number of rows; `47` on client 3464            |
| `+0x08`             | Row[count]   | rows               | `count` rows of 10 bytes                       |
| `rows+0x00`         | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of the string table, where the rows end |
| `string_table+0x04` | u32          | zero               | Always 0                                       |

### Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u8   | class_type  | Same keys and order as `pcgrowthoffset.dbss`                             |
| `+0x01` | u32  | name_index  | String table index of the Korean class name; types 13 and 36 share `PBM` |
| `+0x05` | u8   | is_playable | `1` on 32 class types, `0` on 13, 14, 18, 22 and 36 to 46                |
| `+0x06` | u32  | unknown_06  | Always `0`                                                               |

The `is_playable` rows are exactly the class types of `PLAYABLE_CLASSES_MASK` in `_common/class_type.py`, the mask items use for "every class": 0 to 35 without 13, 14, 18 and 22. The string table holds 46 names for 47 rows.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                      |
| ------- | ------------------ | ------------ | -------------------------- |
| `+0x00` | u32                | string_count | 46 on client 3464          |
| `+0x04` | pstr[string_count] | strings      | Korean class names         |

## Localization

The class name is LOC type 21, `str_id1` = `class_type`, `str_id4` 0, as in [pcgrowth](pcgrowth_dbss.md). The handler shows the LOC name and falls back to the Korean name of the string table.

## Open Questions

### What does `unknown_06` index?

The server dump of a private server on client 1784 (`Instance_dumpFull.exe`)
builds each `PcGrowthSimplyStaticStatus` from the class's
`PcGrowthStaticStatus` (VA `0x140bbd790`): `unknown_06` is a copy of the
last u32 of the [`pcgrowth.dbss`](pcgrowth_dbss.md) record (`unknown_end`).
When a server language option is set, the dump uses it as a LOC type 21 key
for the class name (VA `0x140bbc6b0`); a `0` skips that lookup. No
`PC_Set_Table` column fills it and no message names it. It is `0` on all
82 rows of client 1784 and all 47 of client 3474.
