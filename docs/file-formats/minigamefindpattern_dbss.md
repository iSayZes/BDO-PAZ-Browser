# `minigamefindpattern.dbss` Format

## Purpose

The tile patterns of the Lakiaro digging minigame
([`minigamefind.bss`](minigamefind_bss.md)), grouped by slot index: per
pattern its picture (an image path and a pixel rectangle), the root size,
the patterns that may follow it and in which direction the root goes on. On
client 3482 the file holds 307 patterns in 9 slot groups: 242 root tiles
(slot 0), five sub objects in each of slots 11 to 16 and two lists of
directions only (slots 101 and 102). A game type names the slot groups it
uses in `use_slot_indexes`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes  | Records                       | Row bytes                 |
| ------ | -------------- | ------- | -------------------------------- | ------ | ----------------------------- | ------------------------- |
| 1      | 1348 and later | 3482    | `minigamefindpattern.dbss`       | 49,415 | 307 Pattern Row, 9 Slot Group | 54 to 186, 161 on average |
| 1      | 1348 and later | 3482    | `minigamefindpatternoffset.dbss` | 3,119  | 307 Index Row, 9 Index Group  | 10                        |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 1      | `minigamefindpattern.dbss`       | 49,415 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamefindpatternoffset.dbss` | 3,119 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                      |
| --------------------------------- | -------- | ------------------------------------------------------------------------- |
| `minigamefindpatternoffset.dbss`  | Optional | `(slot_index, pattern_index) -> (data_offset, data_size)`; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table.

| Offset  | Type                    | Field       | Notes                                  |
| ------- | ----------------------- | ----------- | -------------------------------------- |
| `+0x00` | u32                     | group_count | `9` on client 3482                     |
| `+0x04` | Slot Group[group_count] | groups      | See Slot Group                         |

### Slot Group (variable: 5 bytes + rows)

| Offset  | Type                   | Field      | Notes                                                  |
| ------- | ---------------------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u8                     | slot_index | Group key: `0`, `11` to `16`, `101` or `102` (client 3482) |
| `+0x01` | u32                    | row_count  | Patterns in the group                                  |
| `+0x05` | Pattern Row[row_count] | rows       | See Pattern Row                                        |

The groups are stored in the order 16, 0, 11, 12, 101, 13, 14, 15, 102
(clients 1784 and 3482).

### Pattern Row (variable: 46 bytes + image paths and next patterns)

| Offset             | Type                       | Field                      | Notes                                                       |
| ------------------ | -------------------------- | -------------------------- | ----------------------------------------------------------- |
| `+0x00`            | u16                        | pattern_index              | Row key within the group, `1` up                            |
| `+0x02`            | u16                        | pattern_index_dup          | Equal to `pattern_index`; the index's `data_offset` points here |
| `+0x04`            | u16                        | change_pattern             | `pattern_index` of slot 0; `0` for none                     |
| `+0x06`            | u16                        | root_begin_no              | `pattern_index` of slot 0; `0` for none                     |
| `+0x08`            | u8                         | root_size                  | `0` to `5`                                                  |
| `+0x09`            | str8                       | image_file                 | Image path; `None` in slots 101 and 102                     |
| `image_file+0x00`  | str8                       | image_file2                | Second image path; `None` in slots 101 and 102              |
| `image_file2+0x00` | u16[4]                     | slot_coordinate            | Pixel rectangle (x1, y1, x2, y2) in the images; all `0` in slots 101 and 102 |
| `image_file2+0x08` | u8                         | next_pattern_end_direction | See Directions; `4` for none                                |
| `image_file2+0x09` | u8[4]                      | root_begin_direction       | One flag per direction (see Directions); all `0` for none   |
| `image_file2+0x0D` | u64                        | next_pattern_count         | Number of `next_pattern_indexes`                            |
| `image_file2+0x15` | u16[next_pattern_count]    | next_pattern_indexes       | `pattern_index` values of the same slot group that may follow |

The paths are relative to `ui_texture/`, with backslashes and in mixed case:
`New_UI_Common_forLua\Window\MiniGame\MiniGameFind_00.dds` is
`ui_texture/new_ui_common_forlua/window/minigame/minigamefind_00.dds` in the
PAZ index. Slot 0 draws its tiles from `MiniGameFind_00.dds` and
`MiniGameFind_04.dds` in 54 x 54 rectangles, slots 11 to 16 from
`MiniGameFind_01.dds` in 49 x 49 ones (client 3482).

### `minigamefindpatternoffset.dbss`

Index into `minigamefindpattern.dbss` with the same groups in the same
order, no magic and no trailer.

| Offset  | Type                     | Field       | Notes                                |
| ------- | ------------------------ | ----------- | ------------------------------------ |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count` |
| `+0x04` | Index Group[group_count] | groups      | See Index Group                      |

### Index Group (variable: 5 bytes + rows)

| Offset  | Type                 | Field      | Notes                                  |
| ------- | -------------------- | ---------- | -------------------------------------- |
| `+0x00` | u8                   | slot_index | Equals the main group's `slot_index`   |
| `+0x01` | u32                  | row_count  | Equals the main group's `row_count`    |
| `+0x05` | Index Row[row_count] | rows       | See Index Row                          |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | pattern_index | Row key together with the group's `slot_index`              |
| `+0x02` | u32  | data_offset   | Row start + 2, at `pattern_index_dup`                       |
| `+0x06` | u32  | data_size     | Row size - 2: `156` to `184` in slots 0 to 16, `52` or `54` in slots 101 and 102 |

On clients 1784 and 3482 every index row points at the row with its slot
and key; the index rows of slot 0 are in key order, the main rows too.

## Directions

`next_pattern_end_direction` holds one value and `root_begin_direction` one
flag byte per value, in this order. The names come from the sheet (see Field
Names):

| Value | Direction | `next_pattern_end_direction` rows (client 3482) | `root_begin_direction` flag rows |
| ----- | --------- | ----------------------------------------------- | -------------------------------- |
| `0`   | Left      | 72                                              | 5                                |
| `1`   | Right     | 72                                              | 6                                |
| `2`   | Top       | 63                                              | 7                                |
| `3`   | Bottom    | 67                                              | 7                                |
| `4`   | none      | 33                                              |                                  |

No row sets more than one flag. The sheet's `Mid` (10 rows) and an empty
cell both store four `0` flags.

## Field Names

The rows are the `MiniGameFindData` sheet of a private server's
`DataSheets.bexcel` on client 1784, keyed by `SlotIndex` and
`PatternIndex`. The client 1784 and 3482 files are the same bytes, and
every column matches on 307 of 307 keys:

| Field                        | Column                    |
| ---------------------------- | ------------------------- |
| `slot_index`                 | `SlotIndex`               |
| `pattern_index`              | `PatternIndex`            |
| `slot_coordinate`            | `SlotCoordinate`          |
| `root_size`                  | `RootSize`                |
| `next_pattern_indexes`       | `NextPatternIndex`        |
| `next_pattern_end_direction` | `NextPatternEndDirection` |
| `change_pattern`             | `ChangePattern`           |
| `root_begin_no`              | `RootBeginNo`             |
| `root_begin_direction`       | `RootBeginDirection`      |
| `image_file`                 | `ImageFile`               |
| `image_file2`                | `ImageFile2`              |

An empty cell is `0` in `change_pattern`, `root_begin_no` and
`next_pattern_count`, and `4` in `next_pattern_end_direction`.

## Notes

- On client 3482 `change_pattern` is set on the 106 slot 0 rows with
  `root_size` `2` and names one of 12 patterns (108, 111, 112, 115, 117,
  118, 120, 123, 124, 127, 129, 130), each of which is its own change
  pattern and has no next patterns.
- `root_size` is `2`, `3` or `4` in slot 0, `0` in slots 11 to 16 and `5`
  in slots 101 and 102 (client 3482).
- `root_begin_no` (`135`, `152`, `216` or `233`) and a
  `root_begin_direction` flag are set on 25 rows, all in slots 101 and 102.
- Every `next_pattern_indexes` value is a `pattern_index` of the same slot
  group.
