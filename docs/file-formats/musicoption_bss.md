# `musicoption.bss` Format

## Purpose

Options of the instrument performance system: the distance at which other
players hear a performance, and since client 2519 eight more bytes. The
values start right after the PABR magic, in the slot where a table keeps
its record count, and end at the string table. On client 3474 the distance
is `1500`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | -------------- | --------- |
| 2      | 2519 and later | 3474    | `musicoption.bss` | 28    | 1 String Table | 4         |
| 1      | 1784 to 2107   | 2107    | `musicoption.bss` | 20    | 1 String Table | 4         |

| Layout | File              | Known         | Unknown     |
| ------ | ----------------- | ------------- | ----------- |
| 2      | `musicoption.bss` | 20 B (71.4%)  | 8 B (28.6%) |
| 1      | `musicoption.bss` | 20 B (100.0%) | 0 B (0.0%)  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field             | Notes                                                      |
| ------------------- | ------------ | ----------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                               |
| `+0x04`             | f32          | playable_distance | `1500.0` on every client checked; see Field Names          |
| `+0x08`             | bytes[8]     | unknown_08        | `01 00 00 00 00 00 00 00` on clients 2519 to 3474          |
| `+0x10`             | String Table | string_table      | See String Table                                           |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x10`                         |
| `string_table+0x04` | u32          | zero              | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

No `unknown_08`: the string table follows the distance.

### File Layout

| Offset              | Type         | Field             | Notes                              |
| ------------------- | ------------ | ----------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                       |
| `+0x04`             | f32          | playable_distance | `1500.0`                           |
| `+0x08`             | String Table | string_table      | See String Table                   |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x08` |
| `string_table+0x04` | u32          | zero              | Always `0`                         |

## Field Names

The name follows the `MusicOption` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_MusicNoteTable.xlsm`. The sheet has one column,
`PlayableDistance`, and one row, `1500`. The server's loader reads it as a
float, and the client 1784 file is the Layout 1 file above with f32
`1500.0` (1 of 1 values). The value is the same on every client checked,
1784 to 3474.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 00 80 BB 44 01 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00`
  (28 bytes); on clients 1784 and 2107 the 20 bytes
  `50 41 42 52 00 80 BB 44 00 00 00 00 08 00 00 00 00 00 00 00`.
- The same workbook holds `MusicLevel` (`MusicLevel`, `MusicLevelEXPTable`,
  `IncreasingBarNumber`, `IncreasingNoteNumber`, `MusicRank`).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. It reads
  the newest layout and rejects the 20-byte Layout 1 file.

## Open Questions

### Bytes Added on Client 2519

`unknown_08` appeared between clients 2107 and 2519, after the sheet of
client 1784 was built, so no sheet names it. The first byte is `1`, the
other seven `0`: one flag and padding, a u32 and a `0` u32, or a u64 all fit.
The client Lua's music functions (`ToClient_GetMusicInfoByIndex`,
`ToClient_IsPlayMusicAble`, `ToClient_PlayPartyMusicReq` and others on
client 3474) return no option value that would show which.
