# `uipracticeskilltreelayout.bss` Format

## Purpose

A skill tree grid per class for a "practice" skill window, in the cell
format of the 2016 client's skill trees. Every grid of clients 1784 and
3482 is blank: eight classes, 23 by 51 cells each, every cell of type
Blank and no skill placed. The file is the same on both clients.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | ------------------------ | --------- |
| 1      | 1156 and later | 3482    | `uipracticeskilltreelayout.bss` | 37,628 | 9,384 Cell, 8 Class Grid | 4         |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 1      | `uipracticeskilltreelayout.bss` | 37,628 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2637   | Layout 1             |
| 2519   | Layout 1             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | Layout 1             |
| 1156   | Layout 1             |
| 1058   | No file              |
| 911    | No file              |
| 794    | No documented layout |
| 606    | No documented layout |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and the names of placed skills
(none on clients 1784 and 3482) from LOC type 10.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                     | Field        | Notes                                              |
| ------------------- | ------------------------ | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]                  | magic        | `PABR`                                             |
| `+0x04`             | u32                      | class_count  | Number of class grids; `8`                         |
| `+0x08`             | Class Grid[class_count]  | grids        | See Class Grid                                     |
| `grids+0x00`        | String Table             | string_table | See String Table                                   |
| `string_table+0x00` | u32                      | table_start  | Offset of the string table, where `grids` ends     |
| `string_table+0x04` | u32                      | zero         | Always `0`                                         |

### Class Grid (variable: 9 bytes + cells)

| Offset  | Type                | Field      | Notes                                                       |
| ------- | ------------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u8                  | class_type | Class, LOC type `21`: `0`, `4`, `8`, `12`, `13`, `16`, `20`, `24` |
| `+0x01` | u32                 | width      | Sheet columns; `23` on every grid                           |
| `+0x05` | u32                 | height     | Sheet rows; `51` on every grid                              |
| `+0x09` | Cell[width][height] | cells      | `width * height` cells; see Cell                            |

### Cell (4 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u8   | cell_type  | See Cell Types; `1` (Blank) on every cell                       |
| `+0x01` | u8   | arrow_type | See Arrow Types; `0` on every cell                              |
| `+0x02` | u16  | skill_no   | Skill number when `cell_type` is `2`; `0` on every cell         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string               |

## Cell Types

`ge::UISkillTreeLayout_CellValueType` of the 2016 PDB, the same values as
the [`ui_skillgroup_*.bss` Cell Types](ui_skillgroup_bss.md#cell-types):
`0` Undefined, `1` Blank, `2` Skill, `3` to `11` the corner and junction
pieces `LT` to `RB`, `12` Hori, `13` Vert.

## Arrow Types

`ge::UISkillTreeLayout_CellValueArrowType` of the 2016 PDB: `0` None, `1`
Left, `2` Right, `3` Top, `4` Bottom.

## Field Names

The cell is the 2016 `ge::UISkillTreeLayout_CellValue`, 4 bytes: u8
`_cellType`, u8 `_arrowType`, u16 `_skillNo`, in that order. The current
`ui_skillgroup_*.bss` files use a longer cell (a counted type list, a
group number and a tab band); this file keeps the 2016 one.

The developer workbook `UIPracticeSkillTreeLayout.xlsm` of a private
server on client 1784 has one sheet per grid, named `0_SKill`, `4_Skill`,
`8_Skill`, `12_Skill`, `13_Skill`, `16_Skill`, `20_Skill` and `24_Skill`:
the eight `class_type` values in file order. Each sheet marks its right
edge with `END` in the first row of column X, which leaves 23 columns, the
`width`. Every sheet holds no cell value, only the line templates beside
the grid, which is why every cell is Blank.

## Notes

- The eight class types are Warrior, Ranger, Sorceress, Berserker, `13`,
  Tamer, Musa and Valkyrie; type `13` has the LOC type 21 name `PBM` on
  client 3482.
- With every cell Blank, the walk cannot tell whether cells run column by
  column, as in `ui_skillgroup_*.bss`, or row by row.
- No compiled Lua file of client 3482 contains the text `PracticeSkill`.

## Open Questions

### What Window the Practice Tree Belongs To

The grids are empty and no Lua names them. The name and the 2016 cell
format suggest a skill tree window of the 2016 client that the game no
longer fills.
