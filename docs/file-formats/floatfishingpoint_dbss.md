# `floatfishingpoint.dbss` Format

## Purpose

The fishing points that float on open water: per point its size, a start
and an end position, the fish drop group of
[`floatfishing.dbss`](floatfishing_dbss.md) it uses, and the character it
spawns there (`917` Fishing Point or `915` Clearwater Fishing Point) with an
action index. Companion `floatfishingpointoffset.dbss` lists where every row
sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | -------------- | --------- |
| 1      | 1485 and later | 3474    | `floatfishingpoint.dbss`       | 16,888 | 402 Row        | 42        |
| 1      | 1485 and later | 3474    | `floatfishingpointoffset.dbss` | 4,024  | 402 Offset Row | 10        |

| Layout | File                           | Known            | Unknown         |
| ------ | ------------------------------ | ---------------- | --------------- |
| 1      | `floatfishingpoint.dbss`       | 12,466 B (73.8%) | 4,422 B (26.2%) |
| 1      | `floatfishingpointoffset.dbss` | 4,024 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                                 |
| ------------------------------ | -------- | ------------------------------------------------------------------------------------ |
| `floatfishingpointoffset.dbss` | Optional | `point_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`          | Optional | Names of the spawned characters (type `6`)                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then 42-byte rows; the
file ends after the last row.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 402 x 42 = 16,888 bytes.

### Row (42 bytes)

| Offset  | Type     | Field               | Notes                                                                              |
| ------- | -------- | ------------------- | ---------------------------------------------------------------------------------- |
| `+0x00` | u16      | point_key           | Unique; `1` to `426` on client 3474                                                |
| `+0x02` | u32      | point_size          | `2000` on the 229 rows that spawn `917`, `1000` on the 173 that spawn `915` (client 3474) |
| `+0x06` | f32      | start_position_x    | World position of one end of the point's line                                      |
| `+0x0A` | f32      | start_position_y    | Height; `-8241.4` to `4003.35` on client 3474                                      |
| `+0x0E` | f32      | start_position_z    |                                                                                    |
| `+0x12` | f32      | end_position_x      | World position of the other end                                                    |
| `+0x16` | bytes[4] | unknown_16          | `0` on every row of clients 1784 and 3474                                          |
| `+0x1A` | f32      | end_position_z      |                                                                                    |
| `+0x1E` | u16      | fishing_group_key   | Drop group in [`floatfishing.dbss`](floatfishing_dbss.md); equals `point_key` on every row of clients 1784 and 3474 |
| `+0x20` | bytes[4] | unknown_20          | `0` on every row of clients 1784 and 3474; see Open Questions                      |
| `+0x24` | u16      | spawn_character_key | Character spawned at the point: `917` Fishing Point or `915` Clearwater Fishing Point (LOC type 6) |
| `+0x26` | u8       | spawn_action_index  | `1` to `7` (no `6`); `1` on 203 rows (client 3474)                                 |
| `+0x27` | bytes[3] | unknown_27          | `0` on every row of clients 1784 and 3474                                          |

The rows are not sorted by key.

### `floatfishingpointoffset.dbss`

Bare offset table into `floatfishingpoint.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `floatfishingpoint.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                            |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | point_key   | Key of the row it points at                                        |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `floatfishingpoint.dbss`, at its key |
| `+0x06` | u32  | data_size   | `42` on every row: the whole row                                   |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order, and on clients 1784 and 3474 every one points at
the row with its key.

## Field Names

The `FloatFishingPoint_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `PointKey`, `PointSize`, `StartPositionX`,
`StartPositionY`, `StartPositionZ`, `EndPositionX`, `EndPositionZ`,
`FishingGroupKey`, `SpawnRate`, `SpawnCharacterKey`, `SpawnActionIndex` and
`ContentsGroupKey`, in the order of the named fields above. Its 402 rows with
`ContentsGroupKey` `0` match the 402 rows of client 1784 on the key and all
nine named values (the positions to 0.1), 402 of 402. The developer comments
in `datasheet_regiondatatable.xlsm` call `PointSize` the point size,
`FishingGroupKey` the fish drop group, `SpawnCharacterKey` the character to
spawn at the point and `SpawnActionIndex` its action index.

## Notes

- The sheet has no `EndPositionY` column; `unknown_16` sits where a Y would
  between `end_position_x` and `end_position_z`.
- The sheet's eight rows with `ContentsGroupKey` `1633` (points `432` to
  `439`) are not in the client file; their groups are in `floatfishing.dbss`.
- Client 3474 holds the same 402 rows as client 1784, byte for byte.

## Open Questions

### unknown_20

`0` on every row of clients 1784 and 3474. It sits where the sheet's
`SpawnRate` column falls in column order, which carries the `%`
(server-only) prefix in `datasheet_regiondatatable.xlsm` and is `220000` on
point 1 there; a client build writes server-only columns as `0`. With only
zeros the file cannot confirm it.
