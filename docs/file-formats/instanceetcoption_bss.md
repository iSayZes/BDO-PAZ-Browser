# `instanceetcoption.bss` Format

## Purpose

Instance options: two u32 values in the slot where a PABR table keeps its
record count, then an empty string table. On client 3474 they are
`5,000,000` and `0`; no source confirms what either holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 2519 and later | 3474    | `instanceetcoption.bss` | 24    | 1 String Table | 4         |

| Layout | File                    | Known        | Unknown     |
| ------ | ----------------------- | ------------ | ----------- |
| 1      | `instanceetcoption.bss` | 16 B (66.7%) | 8 B (33.3%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32          | unknown_04   | `1` on client 2519, `5000000` on clients 3002 to 3474      |
| `+0x08`             | u32          | unknown_08   | `0` on every client checked                                |
| `+0x0C`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x0C` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 40 4B 4C 00 00 00 00 00 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes).
- The file is not in the archives of clients 1784 and 2107.
- The two u32 fields are a reading of the bytes. `unknown_08` is `0` on
  every client checked, so its width is not shown by the data.
- The `InstanceCommonOption` and `InstanceCamoDisableOption` sheets of a
  private server's `DataSheets.bexcel` on client 1784 start with
  `InstanceType` and `InstanceMode`; that client has no
  `instanceetcoption.bss`, so neither sheet can be matched.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### Instance Option Values

`unknown_04` changed from `1` (client 2519) to `5000000` (client 3002 and
later). No client Lua function on client 3474 has `InstanceEtc` in its name,
and no sheet or loader on client 1784 has `EtcOption` for instances (the
`EtcOption` sheet there is the general option sheet, with house auction,
trade and worker columns). What the two values limit or price is unknown.
