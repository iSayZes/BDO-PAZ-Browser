# `servantwhistledistance.bss` Format

## Purpose

A PABR file with two bytes in the slot where a table keeps its record
count, then an empty string table. The name points at the distance a
servant whistle reaches; no source confirms what the two bytes hold, and
they are `0` on every client checked (2107 to 3474).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | -------------- | --------- |
| 1      | 2107 and later | 3474    | `servantwhistledistance.bss` | 18    | 1 String Table | 4         |

| Layout | File                         | Known        | Unknown     |
| ------ | ---------------------------- | ------------ | ----------- |
| 1      | `servantwhistledistance.bss` | 16 B (88.9%) | 2 B (11.1%) |

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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | bytes[2]     | unknown_04   | `00 00` on every client checked                            |
| `+0x06`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x06` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 2107, 2519, 3002, 3251 and 3474:
  `50 41 42 52 00 00 00 00 00 00 06 00 00 00 00 00 00 00` (18 bytes).
- The file is not in the client 1784 archive.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### Whistle Distance

The `ServantOption` sheet of a private server's `DataSheets.bexcel` on
client 1784 has `PCRoomWhistleDistance` (read as a float by that server's
loader) and `PCRoomWhistleType`, but that client has no
`servantwhistledistance.bss`, and two bytes cannot hold the float. The
client Lua (client 3474) has no whistle distance function; it only checks
`_ContentsGroup_PremeumPCRoomSuperWhistle` and the whistle type. Whether
`unknown_04` is one u16, two u8 values or a flag, and what reads it, is
unknown.
