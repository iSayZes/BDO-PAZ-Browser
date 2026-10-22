# `edaniapvpdayoptionstaticstatus.bss` Format

## Purpose

An Edania (Throne of Edana) schedule: three rows, each a list of entries
that hold a u8 and two times of the week (day, hour, minute), then one u8.
No client Lua call reads this file; the Edania window prints its times
with `ToClient_GetEdanaTimeString(__eEdaniaModeByTime_<mode>)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ----------------------- | --------- |
| 1      | 3002 and later | 3482    | `edaniapvpdayoptionstaticstatus.bss` | 179   | 12 Time, 6 Entry, 3 Row | 12        |

| Layout | File                                 | Known         | Unknown    |
| ------ | ------------------------------------ | ------------- | ---------- |
| 1      | `edaniapvpdayoptionstaticstatus.bss` | 172 B (96.1%) | 7 B (3.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type         | Field           | Notes                                                    |
| ----------- | ------------ | --------------- | -------------------------------------------------------- |
| `+0x00`     | char[4]      | magic           | ASCII `PABR`                                             |
| `+0x04`     | Row[3]       | rows            | See Row; no row count                                    |
| `rows+0x00` | u8           | unknown_rows_00 | `1` on clients 3002, 3474 and 3482, `0` on client 3251   |
| `rows+0x01` | String Table | string_table    | See String Table                                         |
| `EOF-0x08`  | u32          | table_start     | Offset of the string table, where `unknown_rows_00` ends |
| `EOF-0x04`  | u32          | zero            | Always `0`                                               |

### Row (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                       |
| ------- | ------------------ | ----------- | ------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `2` on every client checked |
| `+0x04` | Entry[entry_count] | entries     | See Entry                                   |

### Entry (25 bytes)

| Offset  | Type    | Field      | Notes                                  |
| ------- | ------- | ---------- | -------------------------------------- |
| `+0x00` | u8      | unknown_00 | `0` on the first entry, `1` on the second |
| `+0x01` | Time[2] | times      | See Time and Schedule                  |

### Time (12 bytes)

| Offset  | Type | Field       | Notes       |
| ------- | ---- | ----------- | ----------- |
| `+0x00` | u32  | day_of_week | `0` Sunday to `6` Saturday |
| `+0x04` | u32  | hour        | `0` to `23` |
| `+0x08` | u32  | minute      | `0` to `59` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Schedule

The two times of each entry as day, hour and minute (client 3482):

| Row | `unknown_00` | Time 1    | Time 2    |
| --- | ------------ | --------- | --------- |
| 0   | `0`          | `1` 07:00 | `0` 07:00 |
| 0   | `1`          | `0` 22:00 | `6` 22:00 |
| 1   | `0`          | `1` 00:10 | `1` 00:20 |
| 1   | `1`          | `0` 17:10 | `0` 17:20 |
| 2   | `0`          | `1` 00:30 | `1` 00:50 |
| 2   | `1`          | `0` 17:30 | `0` 17:50 |

On client 3251 every hour of the `1` entries is one later (`0` 23:00,
`0` 18:10, `0` 18:30), the shift of a daylight saving change; the `0`
entries are the same. Client 3002 holds other times in row `0` (`4` 07:00
to `1` 00:00, and `4` 00:00 to `0` 17:00) and the same rows `1` and `2`.

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. `day_of_week`,
`hour` and `minute` follow the Time of
[`rosewarstaticstatus.bss`](rosewarstaticstatus_bss.md), which has the
same u8-then-times entries: the values stay in `0` to `6`, `0` to `23` and
`0` to `59`, and a client update moves the hours of one entry by a whole
hour.

## Notes

- The file is 179 bytes on clients 3002, 3251, 3474 and 3482. It is not in
  the archives of client 1784.
- Within rows `1` and `2` the second time is 10 and 20 minutes after the
  first, on the same day.
- The official Throne of Edana page of the NA/EU game wiki (wikiNo 457)
  sets the EU battles on Sunday in UTC: the 10-challenger battle ("Game of
  the Edanas - Candidates") 17:10 to 17:20 and the final challenger vs.
  Edana battle ("Selection") from 17:30. Those are the times of the `1`
  entries of rows `1` and `2` on client 3482 (`0` 17:10 to `0` 17:20, `0`
  17:30 to `0` 17:50), which makes `0` Sunday, row `1` the challenger
  battle and row `2` the Edana battle. The handler shows the days by name.
- The handler shows one row per entry: the row number and both times as
  `<day name> <hh:mm>`.

## Open Questions

### Row 0

Row `0` spans most of a week (`1` 07:00 to `0` 07:00, and `0` 22:00 to
`6` 22:00), which fits the application period. The official wiki page
gives Monday 00:00 to Sunday 00:00 (UTC) for applications, with the NA
deadline Sunday 00:00 and the EU deadline Sunday 17:00 (UTC); neither
entry of row `0` matches those times.

### The Two Entries

`unknown_00` is `0` and `1` in every row. The `1` entries hold the EU
battle times in UTC (see Notes), and only they moved by an hour on client
3251, a daylight saving change. The `0` entries (`1` 00:10 and `1` 00:30,
Monday) match neither the NA times on the official wiki page (Sunday
00:10 and 00:30 UTC) nor the EU ones, so which region they serve is
open; `unknown_rows_00` is open too.
