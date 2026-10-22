# `siegegovernorcarriagespawnposition.bss` Format

## Purpose

The spawn positions of the Conquest War supply wagon: rows of an index
and a world position. The `spawn_position_list` of
[`siegegovernorcarriagespawn.bss`](siegegovernorcarriagespawn_bss.md)
points at the indexes. Client 3482 has nine rows, three positions repeated
three times.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3482    | `siegegovernorcarriagespawnposition.bss` | 164   | 9 Row   | 16        |

| Layout | File                                     | Known          | Unknown    |
| ------ | ---------------------------------------- | -------------- | ---------- |
| 1      | `siegegovernorcarriagespawnposition.bss` | 164 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads only this file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients that ship the file empty |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field      | Notes                                |
| ------- | ---- | ---------- | ------------------------------------ |
| `+0x00` | u32  | index      | `0` to `row_count - 1` in file order |
| `+0x04` | f32  | position_x | World X                              |
| `+0x08` | f32  | position_y | World Y (height)                     |
| `+0x0C` | f32  | position_z | World Z                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `TankSpawnPosition` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `PositionX`, `PositionY` and
`PositionZ`, and its nine rows match the nine rows of the client 3482 file
in order and value (9 of 9); client 1784 ships the file empty. That
server's dump (client 1784) names the member
`TankSpawnPositionStaticStatus _index`.

## Notes

- Clients 1784 to 2765 ship the file with `row_count` `0`; client 3002
  and later hold the nine rows.
- Indexes `0` to `2`, `3` to `5` and `6` to `8` hold the same three
  positions (`-347644, 1854, -53615`, `-347038, 1854, -54532` and
  `-346340, 1803, -55563`). Each lies within 3,000 units (X and Z) of
  Calpheon's first castle gate attack position in the
  `SiegeCastleTeleportPos` sheet (client 1784, `-348487, 2287, -56349`),
  so the Mediah and Valencia rows of `siegegovernorcarriagespawn.bss`
  point at positions at Calpheon too.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`.
