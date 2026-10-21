# `uigrowthpasslayout.bss` Format

## Purpose

The quest grid of each Growth Pass category: a column and row count per [`growthpasscategory.dbss`](growthpasscategory_dbss.md) key, then one cell per grid position that is blank, a quest, or a piece of the line that links the quests. `panel_window_growthpass_1.luac` builds the window from it through `ToClient_getGrowthPassLayoutWrapper(categoryKey)`, `getColCount()`, `getRowCount()` and `getCellObjectWrapper(row, col)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------ | --------- |
| 1      | 1784 and later | 3474    | `uigrowthpasslayout.bss` | 1,724 | 280 Cell, 2 Layout | 6         |

| Layout | File                     | Known           | Unknown       |
| ------ | ------------------------ | --------------- | ------------- |
| 1      | `uigrowthpasslayout.bss` | 1,444 B (83.8%) | 280 B (16.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field        | Notes                                              |
| ------------------- | -------------------- | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                       |
| `+0x04`             | u32                  | layout_count | `2` on client 3464                                 |
| `+0x08`             | Layout[layout_count] | layouts      | See Layout; back to back                           |
| `layouts+0x00`      | String Table         | string_table | The PABR string table, here with no strings        |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the grids end    |
| `string_table+0x04` | u32                  | zero         | Always `0`                                         |

### Layout (variable: 12 bytes + cells)

| Offset  | Type        | Field        | Notes                                                  |
| ------- | ----------- | ------------ | ------------------------------------------------------ |
| `+0x00` | u32         | category_key | `growthpasscategory.dbss` key                          |
| `+0x04` | u32         | col_count    | `7` on both layouts                                    |
| `+0x08` | u32         | row_count    | `27` (category 7), `13` (category 9) on client 3464   |
| `+0x0C` | Cell[row_count][col_count] | cells | `row_count * col_count` cells, row by row; the layout ends after the last cell |

### Cell (6 bytes)

| Offset  | Type | Field          | Notes                                                       |
| ------- | ---- | -------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | `getQuestGroup()`; `0` on every cell that is not a quest    |
| `+0x02` | u16  | quest_id       | `getQuestId()`; `0` on every cell that is not a quest       |
| `+0x04` | u8   | cell_type      | `getCellType()`, see Cell Types                             |
| `+0x05` | u8   | unknown_05     | `1` on two cells, see Open Questions                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

The Lua draws even rows quest-tall and odd rows as thin line rows, even columns quest-wide and odd columns as thin line columns. Every quest cell sits on an even row and an even column.

## Cell Types

`cell_type` holds a `__eGrowthPass_CellType_*` value. The Lua compares against the names only; the game code sets the numbers, and `global_define_cpp_enum.luac` does not list them. Each value below is matched to a name by the cells around it in the two grids:

| Value | Name           | Where it sits (client 3464)                                              |
| ----- | -------------- | ------------------------------------------------------------------------ |
| 1     | `Blank`        | Empty cells; the Lua draws nothing                                       |
| 2     | `Value`        | A quest button                                                           |
| 3     | `Vertical`     | Line through an even (tall) row, with lines above and below              |
| 4     | `Horizon`      | Line between two quests in one row                                       |
| 5     | `TR`           | Bottom-left corner: line above and to the right                          |
| 6     | `LT`           | Bottom-right corner: line to the left and above                          |
| 7     | `RB`           | Top-left corner: line to the right and below                             |
| 8     | `BL`           | Top-right corner: line below and to the left                             |
| 11    | `LTRB`         | Crossing with a quest on both sides                                      |
| 12    | `LTB`          | Mirror of 13 on the right-hand line                                      |
| 13    | `TRB`          | Junction on the left-hand line with a quest to its right and none to its left |
| 14    | `MiniVertical` | Line through an odd (thin) row; the Lua draws it with `originalLine_Small` |

`InvalidValue`, `LTR` and `LRB` do not occur. The Lua has a branch for `InvalidValue` (it draws a quest button) and asserts on any value outside the list.

## Notes

- Decompressed size on client 3464: `1,724` bytes; the grids end at `0x6B0`, the offset in the trailer.
- On client 3464 category 7 holds quests 4470 / 1 to 40 in rows of four with no linking lines between rows, and category 9 holds quests 4472 / 1 to 13 between two vertical lines that branch into each row.
- Some LOC titles are `{StringTableBind(TextBind:...)}` placeholders (4470 / 3); the Title column shows the LOC type 59 text they name (`languagedata_loc.md`, Type 59).
- calpheonlabs has no page for this table.

## Open Questions

### Cell Byte `unknown_05`

`1` on quests 4472 / 11 (`[Content Stats] Stats from Quests and Logs`) and 4472 / 12 (row 4 and row 6 of column 6), `0` on every other cell (client 3464). Both sit in the right-hand column next to the right line; 4472 / 13 in the same column has `0`.

### LTR and LRB Values

9 and 10 are the two unused values and `LTR` / `LRB` the two unused names, so the pair is likely, but which is which needs a grid that uses one.
