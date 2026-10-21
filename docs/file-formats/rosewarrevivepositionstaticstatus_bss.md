# `rosewarrevivepositionstaticstatus.bss` Format

## Purpose

Where Rose War players revive: two counted groups after the PABR magic.
The first holds the team revive points by `respawn_position_type`, the
second the sanctum revive points by fierce battle key. Each point is a list
of x, y, z positions and an f32. On client 3474 the file has 6 team points
(types `1` to `3` near Grána, `4` to `6` near O'draxxia) and 14 sanctum
points, one for each linked sanctum.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records                                     | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------------------------------------------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarrevivepositionstaticstatus.bss` | 674   | 38 Position, 6 Team Point, 14 Sanctum Point | 12        |

| Layout | File                                    | Known         | Unknown      |
| ------ | --------------------------------------- | ------------- | ------------ |
| 1      | `rosewarrevivepositionstaticstatus.bss` | 594 B (88.1%) | 80 B (11.9%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                          | Field              | Notes                                         |
| -------------------- | ----------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`              | char[4]                       | magic              | ASCII `PABR`                                  |
| `+0x04`              | u32                           | team_point_count   | Number of team points                         |
| `+0x08`              | Team Point[team_point_count]  | team_points        | See Team Point                                |
| `team_points+0x00`   | u32                           | sanctum_point_count| Number of sanctum points                      |
| `team_points+0x04`   | Sanctum Point[sanctum_point_count] | sanctum_points | See Sanctum Point                             |
| `sanctum_points+0x00`| String Table                  | string_table       | See String Table                              |
| `string_table+0x00`  | u32                           | table_start        | Offset of the string table, where `sanctum_points` ends |
| `string_table+0x04`  | u32                           | zero               | Always `0`                                    |

### Team Point (variable: 9 bytes + positions)

| Offset            | Type                     | Field                 | Notes                                                       |
| ----------------- | ------------------------ | --------------------- | ----------------------------------------------------------- |
| `+0x00`           | u8                       | respawn_position_type | `1` to `6` on client 3474; see Revive Point Types           |
| `+0x01`           | u32                      | position_count        | Number of positions, `1` or `3`                             |
| `+0x05`           | Position[position_count] | positions             | See Position                                                |
| `positions+0x00`  | f32                      | unknown_positions_00  | `500` on every team point                                   |

### Sanctum Point (variable: 10 bytes + positions)

| Offset            | Type                     | Field                 | Notes                                                       |
| ----------------- | ------------------------ | --------------------- | ----------------------------------------------------------- |
| `+0x00`           | u16                      | fierce_battle_key     | Sanctum key of the monster table                            |
| `+0x02`           | u32                      | position_count        | Number of positions, `2` on client 3474                     |
| `+0x06`           | Position[position_count] | positions             | See Position                                                |
| `positions+0x00`  | f32                      | unknown_positions_00  | `500`, `400` on sanctums `12` and `14` (client 3474)        |

### Position (12 bytes)

| Offset  | Type | Field | Notes                         |
| ------- | ---- | ----- | ----------------------------- |
| `+0x00` | f32  | x     | World x                       |
| `+0x04` | f32  | y     | Height                        |
| `+0x08` | f32  | z     | World z                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Revive Point Types

The client Lua names seven `__eRoseWarRespawnPositionType_*` values without
their numbers: `Kamasylvia_Plaza`, `Kamasylvia_InsideCastleGate`,
`Kamasylvia_OuterCastleGate`, the same three for `Odyllita`, and
`FierceBattle`. The six team points split by place (client 3474):

| `respawn_position_type` | Positions | Area (x, z)                         |
| ----------------------- | --------- | ----------------------------------- |
| `1`, `2`                | 1 each    | Near Grána (x about -550,000)       |
| `3`                     | 3         | Near Grána                          |
| `4`, `5`                | 1 each    | Near O'draxxia (x about -295,000)   |
| `6`                     | 3         | Near O'draxxia                      |

Which of plaza, inner gate and outer gate each of `1` to `3` is stays open.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. `respawn_position_type`
follows the Lua enum, whose six team names match the six team points and
whose `FierceBattle` value matches the second group; the Lua error
`eErrNoSelectRoseWarRevivePositionType` names the revive position type.
`fierce_battle_key` matches the keys of
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md):
on client 3474 the sanctum points are `1` to `7` and `11` to `17`, the
sanctums [`rosewarfiercebattlenodestaticstatus.bss`](rosewarfiercebattlenodestaticstatus_bss.md)
links. The positions read as BDO world coordinates (y is the height,
`-5,288` to `7,074`).

## Notes

- Client 3002 has the same 6 team points and 20 sanctum points, one per
  sanctum `1` to `20` (866 bytes), matching its three-lane sanctum graph.
  The file is not in the archives of client 1784.
- The handler (`_bss/rosewarrevivepositionstaticstatus/`) shows one row per
  point: the type or the sanctum key, then its positions rounded to whole
  units, in file order.

## Open Questions

### The f32 After the Positions

`unknown_positions_00` is `500` on every team point and on 12 of the 14
sanctum points, `400` on sanctums `12` and `14` (client 3474). A spread
radius around the positions fits the values, but no Lua reads it.
