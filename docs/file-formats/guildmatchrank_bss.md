# `guildmatchrank.bss` Format

## Purpose

The point ranges of the Guild League ranks: one row per rank with the
lowest and highest point of its range. On client 3474 the file has 20
rows; rank `1` covers `3801` to `99999` points and each lower rank the 200
points below it, down to rank `20` at `0` to `200`. The ranges join
without a gap. The Guild League rewards and options are in
[guildmatchoption](guildmatchoption_bss.md), its EXP in
[guildmatchexp](guildmatchexp_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `guildmatchrank.bss` | 380   | 20 Row  | 18        |

| Layout | File                 | Known         | Unknown       |
| ------ | -------------------- | ------------- | ------------- |
| 1      | `guildmatchrank.bss` | 220 B (57.9%) | 160 B (42.1%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed, in rank order           |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (18 bytes)

| Offset  | Type | Field      | Notes                                                                         |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------- |
| `+0x00` | u16  | unknown_00 | `0` on every row (clients 2519 to 3474)                                        |
| `+0x02` | u32  | rank       | Row key, `1` to `row_count`; `1` has the highest range                        |
| `+0x06` | u8   | unknown_06 | `0` on every row (clients 2519 to 3474)                                        |
| `+0x07` | u16  | min_point  | Lowest point of the range; `0` on the last rank                               |
| `+0x09` | u32  | max_point  | Highest point of the range, the next higher rank's `min_point` minus 1        |
| `+0x0D` | u8   | unknown_0d | `5` on ranks 1 to 10, else `0` (client 3474)                                   |
| `+0x0E` | u8   | unknown_0e | `2` on ranks 1 to 10, else `0` (client 3474)                                   |
| `+0x0F` | u8   | unknown_0f | `50` on ranks 1 to 3, `40` on 4 to 7, `30` on 8 to 10, else `0` (client 3474)  |
| `+0x10` | u8   | unknown_10 | `3`, `5` and `7` on ranks 18, 19 and 20, else `0` (client 3474)                |
| `+0x11` | u8   | unknown_11 | Equal to `unknown_10` on every row (clients 2519 to 3474)                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it. The
names describe what the bytes hold: `rank` counts the rows from `1`, and
`min_point` and `max_point` bound one range each, the ranges joining from
`0` up to `99999` (client 3474). The client Lua shows a guild's league
points with `getRankPoint()` (`panel_window_guildmatch_rank_1.luac`); that
these ranges are in those points is the reading, not a confirmed fact.
`min_point` is a u16 next to a u32 `max_point`: a u32 at `+0x05` or `+0x07`
would take bytes of its neighbours on every row.

## Notes

- Client 2519 has 10 ranks: ranks 2 to 10 of 200 points each from `0` to
  `1800`, rank `1` at `1801` to `9999`. There `unknown_0d` and
  `unknown_0e` are `5` and `2` on ranks 1 to 3, `unknown_0f` is `50`, `40`
  and `30` on ranks 1 to 3, and `unknown_10` is `3` and `5` on ranks 9 and
  10. Clients 3002 to 3474 have the 20 ranks above.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`.

## Open Questions

### Rank Bonus Bytes

What `unknown_0d`, `unknown_0e` and `unknown_0f` set on the upper ranks
and `unknown_10` and `unknown_11` on the lowest three. They change with the
rank only, which fits a per-rank reward or matchmaking setting; the Lua
reads none of them by name.
