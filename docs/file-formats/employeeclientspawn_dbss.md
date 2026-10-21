# `employeeclientspawn.dbss` Format

## Purpose

Where the sailors stand on a ship: one row per boat character and position
index, with a position and a facing. The ships are the boat characters of
[`employeecharactership.dbss`](employeecharactership_dbss.md), and the
number of rows per ship matches its `employee_spawn_count` (see Notes).
Companion `employeeclientspawnoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `employeeclientspawn.dbss`       | 724   | 36 Row        | 20        |
| 1      | 1784 and later | 3474    | `employeeclientspawnoffset.dbss` | 436   | 36 Offset Row | 12        |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `employeeclientspawn.dbss`       | 724 B (100.0%) | 0 B (0.0%) |
| 1      | `employeeclientspawnoffset.dbss` | 436 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                                          |
| ------------------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `employeeclientspawnoffset.dbss`                  | Optional | `(character_key, index) -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row  |

Ship names come from LOC type 6, `str_id1` = `character_key`, `str_id4` 0
("Epheria Sailboat" for `31001`).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 36 x 20 = 724 bytes.

### Row (20 bytes)

| Offset  | Type | Field            | Notes                                                                  |
| ------- | ---- | ---------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | character_key    | Boat character, a `character_key` of `employeecharactership.dbss`      |
| `+0x02` | u16  | index            | Position number on that ship, from `0`                                 |
| `+0x04` | f32  | spawn_position_x | Whole numbers from `-450` to `430` (client 3474)                        |
| `+0x08` | f32  | spawn_position_y | `300` or `700` (client 3474)                                           |
| `+0x0C` | f32  | spawn_position_z | Whole numbers from `-1000` to `200` (client 3474)                       |
| `+0x10` | f32  | spawn_direction  | Whole numbers from `45` to `330` (client 3474)                          |

The rows are grouped by `index` in the order 4, 1, 0, 3, 2 on clients 1784
and 3474, and the ships within a group are in no key order (`31055` index
4 first).

### `employeeclientspawnoffset.dbss`

Bare offset table into `employeeclientspawn.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `employeeclientspawn.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Ship of the row it points at                                |
| `+0x02` | u16  | index         | Position number of that row                                 |
| `+0x04` | u32  | data_offset   | Absolute offset of the row in `employeeclientspawn.dbss`, at `character_key` |
| `+0x08` | u32  | data_size     | `20` on every row: the whole row                            |

The parser reads the first u32 as one key, `index << 16 | character_key`,
with `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py` and splits
it. The index rows are in another order than the file; on clients 1784 and
3474 every index row points at the row with its key.

## Field Names

The `EmployeeShipSpawnPosition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CharacterKey`, `Index`,
`SpawnPosition` (three numbers, `100, 300, -450`) and `SpawnDirection`; its
36 rows match the file on all 36 keys and all four values, on client 1784
and on client 3474. The `.xlsx` copy of the sheet names each ship in a note
column (`#DisplayName`, `에페리아 범선` for `31001`). The client Lua has no
getter for the table.

| Field            | Column                     |
| ---------------- | -------------------------- |
| character_key    | `CharacterKey`             |
| index            | `Index`                    |
| spawn_position_x | `SpawnPosition`, first     |
| spawn_position_y | `SpawnPosition`, second    |
| spawn_position_z | `SpawnPosition`, third     |
| spawn_direction  | `SpawnDirection`           |

## Notes

- Ships share their positions and differ in `spawn_direction`: the five
  Epheria Carracks (`31045`, `31054` to `31057`) have the same five
  positions, the Epheria Caravel (`31048`) and Galleass (`31049`) the same
  three, and the five ships with one sailor (Epheria Sailboat, Frigate,
  their Improved versions and the Bartali Sailboat) all stand it at
  `100, 300, -450`. The positions are therefore relative to the ship, not
  world coordinates.
- On client 3474, 12 of the 13 ships with an `employee_spawn_count` above
  `0` in `employeecharactership.dbss` have that many rows here (1, 3 or 5).
  The Panokseon (`31025`, `employee_spawn_count` 5) has no rows.

## Open Questions

### Panokseon Without Positions

The Panokseon (`31025`) has `employee_spawn_count` 5 in
`employeecharactership.dbss` but no row in this file on client 3474. The
client may fall back to a default position for its sailors, or the ship
does not show them.
