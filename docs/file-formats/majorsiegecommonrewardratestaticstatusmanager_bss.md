# `majorsiegecommonrewardratestaticstatusmanager.bss` Format

## Purpose

A Conquest War (major siege) reward rate table: rows of a u32 and a rate
on the 1,000,000 = 100% scale. On client 3482 the 10 rows step the u32
from `30` to `120` in tens and the rate from 10% to 100% in tens. What
the u32 counts is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------------------- | ----- | ------- | --------- |
| 1      | 3474 and later | 3482    | `majorsiegecommonrewardratestaticstatusmanager.bss` | 100   | 10 Row  | 8         |

| Layout | File                                                | Known        | Unknown      |
| ------ | --------------------------------------------------- | ------------ | ------------ |
| 1      | `majorsiegecommonrewardratestaticstatusmanager.bss` | 60 B (60.0%) | 40 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | No file  |
| 3002   | No file  |
| 2765   | No file  |
| 2637   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
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

None. The handler reads only this file.

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

### Row (8 bytes)

| Offset  | Type | Field       | Notes                                                                   |
| ------- | ---- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00  | `30` to `120` in steps of `10`, rising in file order (client 3482)      |
| `+0x04` | u32  | reward_rate | On the 1,000,000 = 100% scale; `100000` (10%) to `1000000` (100%)       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
holds a column of these values. No client Lua of client 3482 reads it.
`reward_rate` takes its name from the file name, `CommonRewardRate`: it
is the one field on the 1,000,000 = 100% scale the handlers read rates
on (`_common/rate.py`).

## Notes

- On client 3482 every row's `reward_rate` is `(unknown_00 - 20) x
  10000`: `30` gives 10%, `120` gives 100%. The file is on clients 3474
  and 3482 of the test clients and not on 3251.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/majorsiege_tables.py`:
  `reward_rate` as a percentage, `unknown_00` on the record only.

## Open Questions

### What the u32 Counts

`unknown_00` runs `30` to `120` and sets a reward share from 10% to
100%. Minutes of participation, a score or a kill count all fit; no Lua
of client 3482 names the table, and no LOC text gives the steps.
