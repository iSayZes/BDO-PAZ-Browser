# `matchingcongestionstaticstatusmanager.bss` Format

## Purpose

Matching queue rows: a key counting from `0`, a byte and two numbers per
row. The name and the client Lua tie the file to the queue activity shown
on the Red Battlefield and Guild League matching buttons
(`ToClient_RequestMatchingCongestion`, `ToClient_GetMatchingCongestionString`,
`ToClient_GetMatchingCongestionCount`); which row belongs to which content
is not known. On client 3474 the file has 6 rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                        | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------- | ----- | ------- | --------- |
| 1      | 3474 and later | 3474    | `matchingcongestionstaticstatusmanager.bss` | 98    | 6 Row   | 13        |

| Layout | File                                        | Known        | Unknown      |
| ------ | ------------------------------------------- | ------------ | ------------ |
| 1      | `matchingcongestionstaticstatusmanager.bss` | 20 B (20.4%) | 78 B (79.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | No file  |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

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
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (13 bytes)

| Offset  | Type | Field      | Notes                                                                   |
| ------- | ---- | ---------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00 | `0` to `5` in row order (client 3474); see Open Questions               |
| `+0x04` | u8   | unknown_04 | `0` on every row                                                        |
| `+0x05` | u32  | unknown_05 | `2`, `15`, `15`, `1`, `2`, `1` by row (client 3474)                     |
| `+0x09` | u32  | unknown_09 | `4`, `29`, `29`, `2`, `3`, `2` by row; above `unknown_05` on every row  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which clients 1784 to 3251 do not ship. The client Lua names two
members of the enum the queue calls take, `__eMatchingContentsType_GuildMatch`
and `__eMatchingContentsType_RedBattleField`, without their values, so no
field is named yet.

## Notes

- The file is 98 bytes on client 3474, the only client checked that ships
  it.
- The Lua asks for a fresh queue count every 30 seconds
  (`_matchingCongestionTime > 30` in `panel_guildmatch_all` and
  `panel_redbattlefieldinfo_all`) and passes `0` to
  `ToClient_GetMatchingCongestionString` and `...Count`.
- With no named field, the handler for the PABR option tables
  (`_bss/pabr_values/`) shows each row's bytes, with the shared layout
  table in `_bss/pabr_values/pvp_tables.py`. `test_pvp_tables.py` checks
  that `unknown_00` counts up from `0`.

## Open Questions

### Row Key and Thresholds

Whether `unknown_00` is the `__eMatchingContentsType_*` value of a matching
content and `unknown_05` and `unknown_09` the queue counts at which the
queue text changes from one activity level to the next. Each row's
`unknown_09` is above its `unknown_05`, which fits two rising thresholds;
the enum values are not in the Lua.
