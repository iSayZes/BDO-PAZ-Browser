# `barterlifelevelinfo.bss` Format

## Purpose

The parley discount per Barter level: one row per level from 1 with the
share of parley that level takes off each barter. The Barter window shows it
in the parley tooltip as "Barter Level: {value}%".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `barterlifelevelinfo.bss` | 1,460 | 180 Level Row | 8         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `barterlifelevelinfo.bss` | 1,460 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                   |
| ------------------- | ----------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32               | level_count        | Number of rows; `180` on client 3474                    |
| `+0x08`             | Level Row[level_count] | levels        | See Level Row                                           |
| `levels+0x00`       | String Table      | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 8 × level_count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                              |

### Level Row (8 bytes)

| Offset  | Type | Field          | Notes                                                        |
| ------- | ---- | -------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | level          | Barter level, `1` to `level_count` in order                  |
| `+0x04` | u32  | discount_point | Parley discount in units of 0.0001%: `27329` is 2.73%       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The row is the `BarterLifeLevel_Option` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `Level` and
`DiscountPoint`. The sheet stores `DiscountPoint` with decimals
(`27329.009460`); the file holds the whole part.

| Field          | Column          | Same value (client 1784) | Same value (client 3474) |
| -------------- | --------------- | ------------------------ | ------------------------ |
| level          | `Level`         | 130 of 130               | 130 of 180               |
| discount_point | `DiscountPoint` | 130 of 130               | 63 of 130                |

Client 3474 adds levels 131 to 180 and holds other values from level 64 on
(level 80 is `199366` on client 1784, `202700` on client 3474).

## Notes

- `PaGlobal_BarterInfoSearch_TicketTooltip_Show` in
  `panel_window_barterinfosearch_2.luac` shows
  `ToClient_discountPointByBarterLevel() / CppDefine.e1Percent` with two
  decimals as the `{value}` of `LUA_BARTER_INFO_POINTCALCULATION` ("Default
  Parley: {point} - Barter Level: {value}%"). `global_define_cpp_enum.luac`
  sets `CppDefine.e1Percent` to `10000`, so `discount_point` 10,000 is 1%.
  The function takes no level argument; the client reads the player's
  Barter level itself.
- On client 3474 level 1 is `0`, level 2 `27329` (2.73%) and level 50
  `171017` (17.10%). The values never fall, and from level 130 to 180 they
  stay at `252700` (25.27%). On client 1784 they stop at `212132` (21.21%)
  from level 121.
