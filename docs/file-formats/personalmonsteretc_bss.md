# `personalmonsteretc.bss` Format

## Purpose

The world map settings of the Dark Rift bosses of
[`personalmonster.dbss`](personalmonster_dbss.md), one PABR value block:
the range within which the map shows a boss, the highest boss level, and
the icon sheet with the regions of its three difficulty frames and five
level marks. The file is the same 236 bytes on clients 1784 and 3474.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `personalmonsteretc.bss` | 236   | 1 String Table | 72        |

| Layout | File                     | Known         | Unknown    |
| ------ | ------------------------ | ------------- | ---------- |
| 1      | `personalmonsteretc.bss` | 228 B (96.6%) | 8 B (3.4%) |

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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field               | Notes                                                                |
| ------------------- | ------------ | ------------------- | -------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic               | ASCII `PABR`                                                         |
| `+0x04`             | u32          | unknown_04          | `0` on clients 1784 and 3474                                         |
| `+0x08`             | f32          | detect_range        | `2000000`; the world map shows a boss once an adventurer is this close |
| `+0x0C`             | u32          | max_level           | `5`; the highest boss level                                          |
| `+0x10`             | f32[2]       | icon_size           | `119, 119`: width and height of the world map icon                   |
| `+0x18`             | f32[3][4]    | difficulty_icon_uvs | Per difficulty `1` to `3` a region `x1, y1, x2, y2` of the icon sheet |
| `+0x48`             | f32[5][4]    | level_icon_uvs      | Per level `1` to `5` a region `x1, y1, x2, y2` of the icon sheet     |
| `+0x98`             | u32          | unknown_98          | `1` on clients 1784 and 3474                                         |
| `+0x9C`             | String Table | string_table        | See String Table                                                     |
| `string_table+0x00` | u32          | table_start         | Offset of the string table; `0x9C` on clients 1784 and 3474          |
| `string_table+0x04` | u32          | zero                | Always `0`                                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `2` on clients 1784 and 3474 |
| `+0x04` | pstr[string_count] | strings      | See Strings                               |

## Strings

| Index | Wide | Text (clients 1784 and 3474)                                   |
| ----- | ---- | -------------------------------------------------------------- |
| 0     | `0`  | `renewal/PcRemaster/Remaster_Icon_Worldmap_AutoBoss_All.dds`   |
| 1     | `1`  | Empty                                                          |

String 0 is the sheet's `MonsterIconImage`, the icon sheet the regions
below cut from.

## Icon Regions

The regions on clients 1784 and 3474, in pixels of the icon sheet. The
sheet's notes call the three difficulty frames normal, hard and very hard;
the LOC labels of `personalmonster.dbss` difficulties `1` to `3` read
Normal, Difficult and Very Difficult.

| Field                 | Entry | x1  | y1  | x2  | y2  |
| --------------------- | ----- | --- | --- | --- | --- |
| `difficulty_icon_uvs` | 1     | 1   | 1   | 120 | 120 |
| `difficulty_icon_uvs` | 2     | 121 | 1   | 240 | 120 |
| `difficulty_icon_uvs` | 3     | 241 | 1   | 360 | 120 |
| `level_icon_uvs`      | 1     | 361 | 1   | 480 | 120 |
| `level_icon_uvs`      | 2     | 1   | 121 | 120 | 240 |
| `level_icon_uvs`      | 3     | 121 | 121 | 240 | 240 |
| `level_icon_uvs`      | 4     | 241 | 121 | 360 | 240 |
| `level_icon_uvs`      | 5     | 361 | 121 | 480 | 240 |

## Field Names

The `PersonalMonsterOption_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row. Its client columns are
`DetectRange`, `MonsterIcon`, `MonsterIconImage`, `IconSize`,
`UV Difficulty1` to `UV Difficulty3`, `UV Level1` to `UV Level5`,
`MaxLevel` and `TotalAcceptCondition`; `MaxSpawnMonster`,
`DailySpawnMonster`, `DailySpawnTime`, `DailySpawnVariableTime`,
`LevelUpCycle`, `APDecreaseRate` and `DPDecreaseRate` are server-only
(`%`) and not in the file. The file matches the row on every value it
holds: `DetectRange` `2000000`, `MaxLevel` `5`, `IconSize` `119,119`, the
32 numbers of the eight `UV` columns in column order, and
`MonsterIconImage` as string 0. The sheet's developer notes call
`DetectRange` the distance at which the world map shows the monster,
`MaxLevel` the highest number of Dark Rift level-ups, and the `UV` columns
the difficulty and level regions of the world map boss icon. The 2016
client's debug symbols have no personal monster type.

## Notes

- `MonsterIcon` lists three `.dds` paths in the sheet; the file holds none
  of them.
- The Dark Rift window's Lua (`panel_window_personalmonster_all.luac`,
  client 3474) has its own copy of the regions (`x2 = 480`, `y2 = 240`)
  and names levels `I` to `VII` in `_difficultyRoma`, two more than
  `max_level`.

## Open Questions

### unknown_04 and unknown_98

The two u32 fields are `0` and `1`, the indexes of the two strings. The
sheet's two text columns that the file could hold are `MonsterIconImage`
(string 0) and `TotalAcceptCondition` (`<null>`, which a PABR table would
store as an empty string such as string 1), so `unknown_04` may be the
string index of the icon sheet and `unknown_98` that of the condition. A
second client with other values would tell them apart from counts or
flags that happen to be `0` and `1`.
