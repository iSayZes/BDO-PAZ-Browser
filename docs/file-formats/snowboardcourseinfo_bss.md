# `snowboardcourseinfo.bss` Format

## Purpose

Two 9-byte rows of the snowboard race content (the courses themselves are
in `snowboard.bss`, 3.2 KB). A u32 count follows the PABR magic. Each row holds a 3-byte value and a zero
byte, a u8, and the same 3-byte value and zero byte again. On client 3474
the rows are `FF FF 14` with `1` and `10 0D 10` with `0`. No field is
named yet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `snowboardcourseinfo.bss` | 38    | 2 Row   | 9         |

| Layout | File                      | Known        | Unknown      |
| ------ | ------------------------- | ------------ | ------------ |
| 1      | `snowboardcourseinfo.bss` | 20 B (52.6%) | 18 B (47.4%) |

<!-- versions:end -->

## Companion Files

None.

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

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                       |
| ------- | -------- | ---------- | ------------------------------------------- |
| `+0x00` | bytes[3] | unknown_00 | `FF FF 14` and `10 0D 10` on client 3474    |
| `+0x03` | u8       | unknown_03 | Always `0`                                  |
| `+0x04` | u8       | unknown_04 | `1` and `0`, one per row                    |
| `+0x05` | bytes[3] | unknown_05 | Equals `unknown_00` on every row            |
| `+0x08` | u8       | unknown_08 | Always `0`                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 FF FF 14 00 01 FF FF 14 00 10 0D 10 00 00 10 0D 10 00 00 00 00 00 1A 00 00 00 00 00 00 00`
  (38 bytes). The file is not in the archives of clients 794 to 2519.
- The 3-byte values recur in other small tables of this client:
  `FF FF 14` in the 9-byte rows of `hardcorechannelinfo.bss`, and
  `10 0D 10` there, in [`rosewarinfo.bss`](rosewarinfo_bss.md) and in the
  `_Count` row of [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md). Those
  files put the u8 after both copies; this file puts it between them.
- The snowboard menu (`panel_window_snowboard_menu_all_1.luac`, client
  3474) reads each course with `ToClient_GetSnowBoardStaticStatusByIndex`
  and `getKeyRaw()`, `getMode()` (`__eSnowBoardCourseMode_Item` or
  `_Speed`), `getName()` and `getCheckPointCount()`. None of these returns
  a 3-byte value.
- The file is newer than client 1784: no sheet of a private server's
  `DataSheets.bexcel` on that client has `Snowboard` in its name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows each row's raw bytes.

## Open Questions

### What the Rows Hold

Read as colours stored blue, green, red (the reading of
`edaniaregioninfo.bss`), the rows are `14ffff` (cyan) with `1` and
`100d10` (near black) with `0`. Whether `unknown_04` is a course mode, a
course key or a flag, and what the two copies of each value are for, is
not known; no client Lua call reads the file.
