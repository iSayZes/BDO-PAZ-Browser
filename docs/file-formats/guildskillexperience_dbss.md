# `guildskillexperience.dbss` Format

## Purpose

EXP table of the guild points (skill point pool `3`, the points guild skills cost): the EXP a guild needs to go from one guild point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) (`guildskillexperiencemaxlevel.bss`). Companion `guildskillexperienceoffset.dbss` lists where every row sits. The container and offset table are the ones of [skillexperience](skillexperience_dbss.md); only the row differs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ------ | ---------------- | --------- |
| 1      | 1784 and later | 3473    | `guildskillexperience.dbss`       | 13,017 | 1,001 Level Row  | 13        |
| 1      | 1784 and later | 3473    | `guildskillexperienceoffset.dbss` | 10,014 | 1,001 Offset Row | 10        |

| Layout | File                              | Known             | Unknown        |
| ------ | --------------------------------- | ----------------- | -------------- |
| 1      | `guildskillexperience.dbss`       | 12,016 B (92.3%)  | 1,001 B (7.7%) |
| 1      | `guildskillexperienceoffset.dbss` | 10,014 B (100.0%) | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                     |
| ---------------------------------- | -------- | ------------------------------------------------------------------------ |
| `guildskillexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row                                   |
| `guildskillexperiencemaxlevel.bss` | Optional | Max level, see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                   |
| ------- | -------------------- | --------- | ------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 1,001 (levels 0 to 1000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | See Level Row; not in level order                       |

The rows fill the file exactly: 4 + 1,001 x 13 = 13,017 bytes on client 3464.

### Level Row (13 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u32  | level      | Guild point level; equals the offset row's key           |
| `+0x04` | u64  | exp        | EXP to go from `level` to `level + 1`, as in [skillexperience](skillexperience_dbss.md) |
| `+0x0C` | u8   | unknown_0c | `1` on every row (client 3464)                           |

### `guildskillexperienceoffset.dbss`

The layout of `skillexperienceoffset.dbss` (see [skillexperience](skillexperience_dbss.md)), with no magic and no trailer.

| Offset  | Type                  | Field     | Notes                              |
| ------- | --------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                   | row_count | Equals the main file's `row_count` |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row                     |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                          |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | level       | Level of the row it points at                                                  |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `guildskillexperience.dbss`       |
| `+0x06` | u32  | data_size   | Always 13                                                                      |

The rows are not in level order (0, 399, 944, ...); the parser returns the main rows sorted by level.

## Notes

- The guild window (`panel_guildskill_all_1.luac`, `panel_guildinfo_all_1.luac`) reads `ToClient_getSkillPointInfo(3)` and shows `_remainPoint` / `_acquirePoint - 1` with the bar `_currentExp / _nextLevelExp`; `acquire.luac` announces a new point as `GainGuildSkillPoint` with `ACQUIRE_OBJECTMESSAGE_3` ("Guild Points Obtained"). See the [skillexperience](skillexperience_dbss.md) Notes for the three pools and the row direction, which follows `lifeexp.dbss`.
- Curve on client 3464: level N needs (700 + 550 x N) x a multiplier that steps up with the level: x1 on levels 0 to 14, x1.3 on 15 to 20, x1.4 on 21 to 30, x1.5 on 31 to 40, x1.8 on 41 to 49, x2.2 on 50 to 70 and x3 on 71 to 1000. Level 1000 is (700 + 550,000) x 3 = 1,652,100.
- `unknown_0c` matches the last byte of the [productexperience](productexperience_dbss.md) row, also `1` on every row; [skillexperience](skillexperience_dbss.md) has a u32 `0` there instead.

## Open Questions

### unknown_0c

The trailing u8 is `1` on all 1,001 rows of client 3464, and the last byte of every `productexperience.dbss` row is `1` too. With no row that differs, the data cannot tell an enable flag from a constant, and the Lua reads only the current and next-level EXP of the pool.
