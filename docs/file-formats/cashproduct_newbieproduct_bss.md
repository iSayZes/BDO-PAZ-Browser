# `cashproduct_newbieproduct.bss` Format

## Purpose

The Pearl Shop product of the newbie banner. The file holds one product ID
of [`cashproduct.dbss`](cashproduct_dbss.md) in the slot where a PABR table
keeps its record count. On client 3474 it is `101549`, the Black Spirit Pass
(`흑정령 패스`, item `320185`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | -------------- | --------- |
| 1      | 2107 and later | 3474    | `cashproduct_newbieproduct.bss` | 20    | 1 String Table | 4         |

| Layout | File                            | Known         | Unknown    |
| ------ | ------------------------------- | ------------- | ---------- |
| 1      | `cashproduct_newbieproduct.bss` | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The product ID is a key of [`cashproduct.dbss`](cashproduct_dbss.md),
which the handler does not load.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                        |
| ------------------- | ------------ | ------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                                 |
| `+0x04`             | u32          | product_id   | `cashproduct.dbss` product ID; see Field Names               |
| `+0x08`             | String Table | string_table | See String Table                                             |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x08` on every client checked   |
| `string_table+0x04` | u32          | zero         | Always `0`                                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

On client 3474 `product_id` is `101549`, a key of that client's
`cashproduct.dbss` (Black Spirit Pass). Clients 2107, 2519 and 3002 hold
`97868`, client 3251 `101549`.

The client Lua reads one Pearl Shop product number for new players:
`panel_window_banner_2.luac` (client 3474) calls
`ToClient_GetNewbieCashProductNoRaw()`, shows the banner only when it is
above `0`, and passes it to
`getIngameCashMall():getCashProductStaticStatusByProductNoRaw()`. The banner
also requires `getMyAdmissionToSpeedServer()` to be `2`. No other file name
or table holds a newbie product, so the Lua number is this value; the file
name and the `cashproduct.dbss` match name the field, not a source sheet.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 AD 8C 01 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The file is not in the client 1784 archive, and no sheet of a private
  server's `DataSheets.bexcel` on client 1784 has `Newbie` in a sheet or
  column name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.

## Open Questions

### Admission Type 2

The banner shows only when `getMyAdmissionToSpeedServer()` returns `2`. The
client Lua uses the global `__eEAdmissionSpeedChannelType_Newbie`, but no
Lua file assigns it, so whether `2` is that newbie type is unconfirmed.
