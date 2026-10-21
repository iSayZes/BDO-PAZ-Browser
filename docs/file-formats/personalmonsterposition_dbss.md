# `personalmonsterposition.dbss` Format

## Purpose

The spawn points of the Dark Rift bosses of
[`personalmonster.dbss`](personalmonster_dbss.md): per position index a
world position and the distance around it at which a boss spawns. On
client 3474 the file has 48 points, indexes `1` to `48`, each with a
spawn distance of `5000`. No key in the client files says which boss uses
which point. Companion `personalmonsterpositionoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ------------- | --------- |
| 2      | 2519 and later | 3474    | `personalmonsterposition.dbss`       | 1,060 | 48 Row        | 22        |
| 2      | 2519 and later | 3474    | `personalmonsterpositionoffset.dbss` | 580   | 48 Offset Row | 12        |
| 1      | 1485 to 2107   | 2107    | `personalmonsterposition.dbss`       | 944   | 47 Row        | 20        |
| 1      | 1485 to 2107   | 2107    | `personalmonsterpositionoffset.dbss` | 568   | 47 Offset Row | 12        |

| Layout | File                                 | Known          | Unknown     |
| ------ | ------------------------------------ | -------------- | ----------- |
| 2      | `personalmonsterposition.dbss`       | 964 B (90.9%)  | 96 B (9.1%) |
| 2      | `personalmonsterpositionoffset.dbss` | 580 B (100.0%) | 0 B (0.0%)  |
| 1      | `personalmonsterposition.dbss`       | 944 B (100.0%) | 0 B (0.0%)  |
| 1      | `personalmonsterpositionoffset.dbss` | 568 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                 | Required | Role                                                                       |
| ------------------------------------ | -------- | -------------------------------------------------------------------------- |
| `personalmonsterpositionoffset.dbss` | Optional | `position_index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 48 x 22 = 1,060 bytes.

### Row (22 bytes)

| Offset  | Type | Field          | Notes                                                        |
| ------- | ---- | -------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | position_index | Row key; `1` to `48` on client 3474, in that order           |
| `+0x04` | f32  | x              | World position                                               |
| `+0x08` | f32  | y              | Height                                                       |
| `+0x0C` | f32  | z              |                                                              |
| `+0x10` | f32  | spawn_distance | How far from the point the boss spawns; `5000` on every row of clients 1784 and 3474 |
| `+0x14` | u16  | unknown_14     | `1` on every row of client 3474; not in client 1784          |

### `personalmonsterpositionoffset.dbss`

Bare offset table into `personalmonsterposition.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                           |
| ------- | ----------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32               | count | Equals the `personalmonsterposition.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                  |

### Offset Row (12 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u32  | position_index | Key of the row it points at                                             |
| `+0x04` | u32  | data_offset    | Absolute offset of the row in `personalmonsterposition.dbss`, at its `position_index` |
| `+0x08` | u32  | data_size      | The whole row: `22` on client 3474, `20` on client 1784                  |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 every index row points at the row with its key, and
the rows fill the file.

## Layout 1

Client 1784 has no `unknown_14`: its rows are 20 bytes, and the file is
4 + 47 x 20 = 944 bytes.

### Row (20 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u32  | position_index |       |
| `+0x04` | f32  | x              |       |
| `+0x08` | f32  | y              |       |
| `+0x0C` | f32  | z              |       |
| `+0x10` | f32  | spawn_distance |       |

## Field Names

The `PersonalMonsterPosition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`,
`SpawnPosition` (three numbers) and `SpawnDistance`. Its 47 rows match the
client 1784 file on all 47 indexes for the position (to 0.01) and the
distance. On client 3474, 37 of those 47 points are unchanged, 10 moved
(indexes `5`, `7`, `8`, `9`, `12`, `14`, `15`, `16`, `17` and `40`) and
index `48` is new. The sheet's developer note on `SpawnDistance` says it
sets how far from the place the monster spawns. `position_index` is the
sheet's `Index`, which the server-only `PositionIndex` column of
`PersonalMonster_Table` names; the 2016 client's debug symbols have no
personal monster type.

## Notes

- The client Lua of client 3474 reads no row of this file directly: it
  navigates to `ToClient_GetReservePersonalMonsterPosition(reserveIndex)`,
  the point the server reserved for a boss, and
  `ToClient_FindReservedPersonalMonsterInfoWrapper(characterKey):getSpawnPosition()`.
- The rows hold no region key. The sheet's note column (`#비고`, not
  compiled) names a place per index on client 1784, `아그리스 제단`
  (Altar of Agris) for index `1`.

## Open Questions

### unknown_14

Client 3474 added a u16 that is `1` on all 48 rows. Field `1` of
[`fieldinfo.bss`](fieldinfo_bss.md) is the open world (`월드`), and the
Lua calls `ToClient_GetPersonalMonsterFieldNobyIndex(reserveIndex)` before
it navigates to a reserved boss, so the u16 may be the field number of the
point. With one value on every row, nothing confirms it.
