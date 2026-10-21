# `rosewarinfo.bss` Format

## Purpose

Two 9-byte rows for the Rose War, fought between the Kamasylvia and
Odyllita teams (`__eRoseWarTeam_Kamasylvia`, `__eRoseWarTeam_Odyllita`
in the client Lua). A u32 count follows the PABR magic. Each row has the
shape of an [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md) row: a
3-byte value and a zero byte twice, then a u8. On client 3474 the rows are
`10 0D 10` with `0` and `E8 1B 18` with `1`. No field is named yet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarinfo.bss` | 38    | 2 Row   | 9         |

| Layout | File              | Known        | Unknown      |
| ------ | ----------------- | ------------ | ------------ |
| 1      | `rosewarinfo.bss` | 20 B (52.6%) | 18 B (47.4%) |

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

| Offset  | Type     | Field      | Notes                                                              |
| ------- | -------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | bytes[3] | unknown_00 | `10 0D 10` and `E8 1B 18` on client 3474                           |
| `+0x03` | u8       | unknown_03 | Always `0`                                                         |
| `+0x04` | bytes[3] | unknown_04 | Equals `unknown_00` on every row                                   |
| `+0x07` | u8       | unknown_07 | Always `0`                                                         |
| `+0x08` | u8       | unknown_08 | `0` and `1`, one per row                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 10 0D 10 00 10 0D 10 00 00 E8 1B 18 00 E8 1B 18 00 01 00 00 00 00 1A 00 00 00 00 00 00 00`
  (38 bytes). The file is not in the archives of clients 794 to 2519.
- The same two rows close `hardcorechannelinfo.bss` on client 3474, a
  15-row file of this row shape: `E8 1B 18` with `1`, then `10 0D 10`
  with `0`. `10 0D 10` is also the 3-byte value of the `_Count` row of
  `edaniaregioninfo.bss`.
- In `edaniaregioninfo.bss` the 3-byte value of five rows equals the
  `regioninfo.bss` `color` (stored blue, green, red) of the castle region
  of the same name. Read that way, the rows here are `100d10` (near black)
  and `181be8` (blue).
- The file is newer than client 1784: no sheet of a private server's
  `DataSheets.bexcel` on that client and no string of its server dump has
  `RoseWar` in the name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`.
  With no confirmed field, the preview shows each row's raw bytes.

## Open Questions

### Team Colours

The shape and the values point to one colour per Rose War team, with
`unknown_08` as the team number, but no source names a field. The client
3474 Lua has `getRoseWarTeamNo` and the two `__eRoseWarTeam_*` names
without their values, and no Lua call returns a colour for a team.
[`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md) puts
the Kamasylvia characters on team `0` and the O'dyllita ones on `1`, so if
`unknown_08` is the team number, `100d10` is Kamasylvia's and `181be8`
O'dyllita's. Whether it is, and what the second copy of the 3-byte value
is for, are open.
