# `icefisingregionstaticstatus.bss` Format

## Purpose

The regions where the ice fishing mini-game runs and which mini-game group
each one uses. Each 4-byte row holds a [`regioninfo.bss`](regioninfo_bss.md)
region key and a mini-game group. The rows start right after the PABR magic
and run up to the string table; no count is stored. On client 3474 the two
rows are Snowfall Crasher: Alpine Glide (`1176`, group `1`) and Gyeonghoeru
Pavilion (`1484`, group `2`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `icefisingregionstaticstatus.bss` | 24    | 2 Row   | 4         |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `icefisingregionstaticstatus.bss` | 24 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                              |
| --------------------- | -------- | --------------------------------- |
| `languagedata_en.loc` | Optional | Region names, LOC type 17         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset          | Type               | Field        | Notes                                                |
| --------------- | ------------------ | ------------ | ---------------------------------------------------- |
| `+0x00`         | char[4]            | magic        | ASCII `PABR`                                         |
| `+0x04`         | Row[..table_start] | rows         | See Row                                              |
| `rows+0x00`     | String Table       | string_table | See String Table                                     |
| `EOF-0x08`      | u32                | table_start  | Offset of the string table, where `rows` ends        |
| `EOF-0x04`      | u32                | zero         | Always `0`                                           |

The parser takes the row count from the trailer: `(table_start - 4) / 4`.

### Row (4 bytes)

| Offset  | Type | Field                 | Notes                                                                 |
| ------- | ---- | --------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | region_key            | `regioninfo.bss` region key; the handler shows its LOC type 17 name    |
| `+0x02` | u16  | mini_game_group_index | Mini-game group the region uses                                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names follow the `IceFishing_Region` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_minigame_2.xlsm`. The sheet has the columns `MiniGameRegionGroup`
and `MiniGameGroupIndex` and one row, `326` and `1`, with the note
`2021년 크리스마스 고요한 샘` (2021 Christmas, Serene Spring). The client 1784
archive's file holds that row: `46 01 01 00`, u16 `326` and u16 `1` (1 of 1
rows). Region `326` is Serene Spring in `regioninfo.bss` and in LOC type 17,
so `MiniGameRegionGroup` holds a region key and the field is `region_key`.

Rows on the clients checked, `region_key` / `mini_game_group_index`, with
the LOC type 17 names of client 3474:

| Client | Rows                              |
| ------ | --------------------------------- |
| 1784   | `326` / `1`                       |
| 2107   | `1191` / `1`                      |
| 2519   | `1191` / `1`                      |
| 3002   | `1176` / `1`                      |
| 3251   | `1176` / `1`, `1484` / `2`        |
| 3474   | `1176` / `1`, `1484` / `2`        |

`326` and `1191` are both Serene Spring, `1176` Snowfall Crasher: Alpine
Glide and `1484` Gyeonghoeru Pavilion.

The same sheet file holds the `IceFishing` sheet, whose first column is
`MiniGameGroup` (`1` on client 1784) followed by the mini-game timings, HP
and rewards. Its compiled file is `icefisingstaticstatus.bss` (not
documented yet), whose header count is `1` on client 1784 and `2` on client
3474, one per group above.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 98 04 01 00 CC 05 02 00 00 00 00 00 0C 00 00 00 00 00 00 00`.
- The server dump of the private server on client 1784 has a loader for
  `IceFishing_Region` that reads `MiniGameRegionGroup` as a number and
  `MiniGameGroupIndex` through the text reader, and an
  `IceFishingStaticStatusManager` that names `MinigameGroup` in its error
  messages.
- The client Lua opens the mini-game through `Panel_MiniGame_IceFishing_All`
  behind `_ContentsGroup_IceFishingGame`; it reads no region list.
- `icefising` is the client's spelling.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.
