# `employeespawnposition.dbss` Format

## Purpose

Spawn positions of the hireable sailors (the client calls sailors "employees") in the three port towns where they wait to be hired: Velia, Port Epheria and Iliya Island. Each row is a world position, a facing direction and the region the spot lies in. `employeespawninfo.dbss` lists, per sailor character, the spawn position keys that sailor can appear on. Companion `employeespawnpositionoffset.dbss` lists where every row sits.

Example:

```text
spawn position 1    Velia          ( 14,090, -6,567,  75,950)  facing (-0.71, 0, -0.71)
spawn position 41   Port Epheria   (-361,473, -8,000,  31,106)  facing (-0.71, 0,  0.71)
spawn position 46   Iliya Island   (162,702, -4,856, 301,174)   facing ( 0.17, 0,  0.98)
```

## Companion Files

| File                               | Required | Role                                                      |
| ---------------------------------- | -------- | --------------------------------------------------------- |
| `employeespawnpositionoffset.dbss` | Required | `spawn_position_key -> (offset, size)` of every row       |
| `employeespawninfo.dbss`           | Optional | Sailors that list each spawn position, for the Sailors column |
| `employeespawninfooffset.dbss`     | Optional | Offset table of `employeespawninfo.dbss`                  |
| `languagedata_en.loc`              | Optional | Region names (LOC type 17, `str_id1` = `region_key`), sailor names and titles (type 6) |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type      | Field | Notes                                         |
| ------- | --------- | ----- | --------------------------------------------- |
| `+0x00` | u32       | count | Number of spawn positions (observed: 15)      |
| `+0x04` | row[]     | rows  | `count` rows of 34 bytes                      |

The rows fill the file exactly: 4 + 15 x 34 = 514 bytes on client 3458.

## Record Structure

### Spawn Position Row (34 bytes)

| Offset  | Type | Field              | Notes                                                                                           |
| ------- | ---- | ------------------ | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | spawn_position_key | Row key; `1` to `5` in Velia, `41` to `45` in Port Epheria, `46` to `50` in Iliya Island         |
| `+0x04` | f32  | pos_x              | World X                                                                                         |
| `+0x08` | f32  | pos_y              | World Y (height)                                                                                |
| `+0x0C` | f32  | pos_z              | World Z                                                                                         |
| `+0x10` | f32  | dir_x              | Facing direction, X part                                                                        |
| `+0x14` | f32  | dir_y              | Facing direction, Y part; always `0`                                                            |
| `+0x18` | f32  | dir_z              | Facing direction, Z part                                                                        |
| `+0x1C` | f32  | unknown_1c         | Always `5000.0`; see Open Questions                                                             |
| `+0x20` | u16  | region_key         | Region the spot lies in, LOC type 17: `5` Velia, `120` Port Epheria, `182` Iliya Island         |

`(dir_x, dir_y, dir_z)` is a unit vector in the horizontal plane on every row (`dir_x² + dir_z² = 1`, every angle a multiple of 5 degrees, such as `(-0.7071, 0, 0.7071)` and `(0.1736, 0, 0.9848)`), so it reads as the way the sailor faces. The positions are world coordinates in centimetres, like `teleport.dbss` and the waypoint files. Velia's five spots lie within 12 m of each other, Port Epheria's within 28 m and Iliya Island's within 106 m.

## employeespawnpositionoffset.dbss

Bare offset table into `employeespawnposition.dbss` (no PABR magic, no trailer).

### Header (4 bytes)

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Number of offset rows; equals the main file count  |

### Offset Row (12 bytes, repeated `count` times)

| Offset  | Type | Field              | Notes                                                           |
| ------- | ---- | ------------------ | --------------------------------------------------------------- |
| `+0x00` | u32  | spawn_position_key | Key of the row it points at                                     |
| `+0x04` | u32  | data_offset        | Absolute byte offset in `employeespawnposition.dbss`            |
| `+0x08` | u32  | data_size          | Always 34                                                       |

The rows are in file order, which is not key order (41, 1, 42, 2, 43, 3, 4, 5, 44, 45, 46 to 50). The parser reads the main file through these rows and checks that every row holds the key of the offset row that points at it.

## Suggested UI Layout

### employeespawnposition.dbss

| Column         | Type | Notes                                                        |
| -------------- | ---- | ------------------------------------------------------------ |
| Spawn Position | num  | `spawn_position_key`                                         |
| Region         | text | LOC type 17 name of `region_key`, falling back to the key    |
| Sailors        | text | `Sailor <Ambitious>` for every `employeespawninfo.dbss` row whose `spawn_position_keys` hold this key, in that file's order; dash without both sailor files |
| X              | num  | `pos_x`, whole number                                        |
| Y              | num  | `pos_y`, whole number                                        |
| Z              | num  | `pos_z`, whole number                                        |
| Direction      | text | `dir_x, dir_y, dir_z` rounded to two decimals                |

`unknown_1c` stays on the record but out of the table.

### employeespawnpositionoffset.dbss

| Column         | Type | Notes                          |
| -------------- | ---- | ------------------------------ |
| Spawn Position | num  | `spawn_position_key`           |
| Data Offset    | num  | `data_offset`, as hex          |
| Data Size      | num  | `data_size`                    |

## Notes

- "Employee" in these file names means sailor: the client's sailor windows (`panel_window_sailormanager_all_*.luac`) work on `ToClient_getEmployeeWrapperByIndex`, `getEmployeeKey` and the `__eEmployeeAbility_*` ship stats, and the characters `employeespawninfo.dbss` places here (`59053` to `59072`) are all named Sailor in `characterstatic.dbss` with model `npc/employee_sailor`.
- `employeespawninfo.dbss` rows (one per sailor character, keyed by a u16 character key) hold a sailor key, a u32 count and that many u32 spawn position keys, see [employeespawninfo](employeespawninfo_dbss.md). Examples: character `59061` lists `1` and `41` (Velia and Port Epheria), `59054` lists `46` (Iliya Island only), `59068` lists `44` and `50`. Every key 1 to 5 and 41 to 50 appears there.
- The spawn position keys are their own key space. They overlap employee name IDs in `employeename.dbss` (1 to 60) only by value; nothing links the two.
- The three regions match the towns where sailors can be hired in game: Velia, Port Epheria and Iliya Island.

## Open Questions

### unknown_1c

Every row stores `5000.0` at `+0x1C`. It could be a spawn or interaction radius (5000 cm is 50 m), a respawn delay in milliseconds, or a distance at which the client spawns the sailor. No client Lua string names it, and a constant column cannot be told apart from the data alone. A row with a different value after a patch, or a client function that reads the spawn position table, would settle it.
