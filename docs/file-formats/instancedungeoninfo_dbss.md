# `instancedungeoninfo.dbss` Format

## Purpose

The entry point of each instance dungeon: the field the dungeon runs in
(`field_no`, a `Field_Table` key), the world position a character enters
at and the direction it faces. The table holds 4 records on client 3474,
byte for byte the same as on client 1784. Companion
`instancedungeoninfooffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records             | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------------- | --------- |
| 1      | 1784 and later | 3474    | `instancedungeoninfo.dbss`       | 92    | 4 Dungeon Entry Row | 22        |
| 1      | 1784 and later | 3474    | `instancedungeoninfooffset.dbss` | 52    | 4 Index Row         | 12        |

| Layout | File                             | Known         | Unknown    |
| ------ | -------------------------------- | ------------- | ---------- |
| 1      | `instancedungeoninfo.dbss`       | 92 B (100.0%) | 0 B (0.0%) |
| 1      | `instancedungeoninfooffset.dbss` | 52 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. `instancedungeoninfooffset.dbss` is the offset file of this table;
the handler reads the records straight from the main file, since every
record has the same size.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                     | Field | Notes                                 |
| ------- | ------------------------ | ----- | ------------------------------------- |
| `+0x00` | u32                      | count | Number of records; `4` on client 3474 |
| `+0x04` | Dungeon Entry Row[count] | rows  | See Dungeon Entry Row                 |

The rows fill the file exactly: 4 + 4 x 22 = 92 bytes on client 3474.

### Dungeon Entry Row (22 bytes)

| Offset  | Type | Field          | Notes                                                                       |
| ------- | ---- | -------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | key            | Record key, `0` to `3` on client 3474; equals the index row key             |
| `+0x04` | u16  | field_no       | Field the dungeon runs in, a `Field_Table` key: `1238`, `1239`, `700`, `701` on client 3474 |
| `+0x06` | f32  | enter_x        | Entry position, world X                                                     |
| `+0x0A` | f32  | enter_y        | Entry position, world Y (height)                                            |
| `+0x0E` | f32  | enter_z        | Entry position, world Z                                                     |
| `+0x12` | f32  | enter_rotation | Facing direction at entry in radians; the sheet column holds degrees        |

### `instancedungeoninfooffset.dbss`

Bare offset table into `instancedungeoninfo.dbss` (no PABR magic, no
trailer).

| Offset  | Type             | Field | Notes                                           |
| ------- | ---------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32              | count | Number of index rows; equals the main file count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                   |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                  |
| ------- | ---- | ------ | ------------------------------------------------------ |
| `+0x00` | u32  | key    | The record's `key`                                     |
| `+0x04` | u32  | offset | Absolute byte offset of the record in the main file    |
| `+0x08` | u32  | size   | Record length including `key`; `22` on every row       |

## Field Names

The record is the `InstanceDungeonInfo_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784. Every column matches on all 4 keys of
client 3474:

| Field                           | Sheet column       | Match                                                        |
| ------------------------------- | ------------------ | ------------------------------------------------------------ |
| `key`                           | `Index`            | 4 of 4                                                       |
| `field_no`                      | `FieldNo`          | 4 of 4                                                       |
| `enter_x`, `enter_y`, `enter_z` | `EnterPosition`    | 4 of 4; the sheet writes the three as `768000,11542,102400`   |
| `enter_rotation`                | `EnterRotationDeg` | 4 of 4 once converted: the sheet's `90` is `1.5707964` (pi / 2) here, its `0` is `0` |

The `InstanceDungeonInfo_Table` of a private server on client 519 has the
same columns and rows, except that it gives `EnterRotationDeg` `0` for key
`1`. The server's loader for the sheet (`loadInstanceDungeonInformation`
in its log strings) reads `EnterPosition` as a string and
`EnterRotationDeg` as a float, and logs "인던필드의 EnterPosition의 Y값이
비정상입니다" ("the instance field's EnterPosition Y value is invalid"), and
the same for Z, when a coordinate is bad. The 2016 PDB has no instance
dungeon struct.

`FieldNo` is the key column of the `Field_Table` sheet of the same 1784
source, whose client copy is [fieldinfo.bss](fieldinfo_bss.md). The sheet
and the client 3474 file give the four fields the same names:

| `field_no` | `FieldName` in the sheet | Translation                       |
| ---------- | ------------------------ | --------------------------------- |
| `700`      | 칼페온 크자카 인던       | Calpheon Kzarka instance dungeon  |
| `701`      | 아쳐 튜토리얼 인던       | Archer tutorial instance dungeon  |
| `1238`     | 트리거 테스트 인던1      | Trigger test instance dungeon 1   |
| `1239`     | 트리거 테스트 인던2      | Trigger test instance dungeon 2   |

## Notes

- Keys `0` and `1` share the entry position `(768000, 11542, 102400)` and
  differ in `field_no` and `enter_rotation` (`0` and pi / 2).
- The client Lua enters an instance dungeon with
  `ToClient_EnterIntanceDungeon(indunKey, true)`
  (`panel_window_storyinstancedungeon.luac`), where `indunKey` comes from the
  server event `FromClient_ShowIndunMessage`.

## Open Questions

### Whether the Lua Instance Dungeon Key Is This Key

`panel_window_storyinstancedungeon.luac` passes an `indunKey` from the
server to `ToClient_EnterIntanceDungeon`. Whether that key is this table's
`key` (`0` to `3`), a `field_no` or another key space is open; the Lua
shows no literal key.
