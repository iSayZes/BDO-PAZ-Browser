# `arshadebuff.bss` Format

## Purpose

The Arena of Arsha debuff steps: one row per step with its timer and two
values that are `0` on every row. On client 3474 the file has 3 rows with
timers `0`, `330000` and `660000`. The client Lua turns the debuff on and
off with `ToClient_ArshaDebuffOnOff(isOn)` (`panel_window_arsha_func_all`)
and listens for `FromClient_ArshaDebuff`; it reads no row of this file by
name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------- | --------- |
| 1      | 1230 and later | 3474    | `arshadebuff.bss` | 56    | 3 Row   | 12        |

| Layout | File              | Known        | Unknown      |
| ------ | ----------------- | ------------ | ------------ |
| 1      | `arshadebuff.bss` | 32 B (57.1%) | 24 B (42.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | Layout 1             |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

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

### Row (12 bytes)

| Offset  | Type | Field        | Notes                                                               |
| ------- | ---- | ------------ | ------------------------------------------------------------------- |
| `+0x00` | u32  | debuff_timer | `0`, `330000`, `660000` on every client checked; see Field Names    |
| `+0x04` | u32  | unknown_04   | `0` on every row; see Open Questions                                |
| `+0x08` | u32  | unknown_08   | `0` on every row; see Open Questions                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `ArshaDebuff_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `debuffTimer`, `decreaseMaxHp` and
`decreaseRecoveryHp` and 3 rows, `330000` and `660000` after a first row of
`0`. `debuff_timer` matches 3 of 3 rows of the client 1784 file, and the
file is the same on client 3474. The sheet's other two columns are `0` on
every row, as are `unknown_04` and `unknown_08`, so the values do not tell
which column is which.

## Notes

- The file is 56 bytes and the same on clients 1784, 2107, 2519, 3002, 3251
  and 3474.
- The server reads the sheet in `ArshaStaticStatus` next to the personal
  match HP debuff (`ArshaPersonalMatchHPDebuff`: `WinCount`,
  `DebuffHPRate`, `RemainTimeMultiplier`), which has no client file.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.

## Open Questions

### Max HP and Recovery Columns

Which of `unknown_04` and `unknown_08` is `decreaseMaxHp` and which
`decreaseRecoveryHp`. Both are `0` on every row of every client checked,
and the sheet order and the order of the server's column strings disagree.
A file with a non-zero value in one of them would tell.

### Timer Unit

The unit of `debuff_timer`. As milliseconds, `330000` and `660000` are
5 min 30 s and 11 min of a match; no Lua shows the value.
