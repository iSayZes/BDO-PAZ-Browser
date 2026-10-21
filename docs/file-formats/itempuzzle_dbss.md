# `itempuzzle.dbss` Format

## Purpose

The inventory puzzles: items that combine into another item when they lie
in the inventory in a given shape, such as three Ancient Pottery Fragments
in a row. Each row holds one puzzle as a 5 x 5 grid of item keys, row by
row, and the first piece and the grid bounds the client works out from it.
The item a puzzle makes is a server-only column and `0` in the client
file. Companion `itempuzzleoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ------ | -------------- | --------- |
| 1      | 1485 and later | 3474    | `itempuzzle.dbss`       | 46,324 | 386 Row        | 120       |
| 1      | 1485 and later | 3474    | `itempuzzleoffset.dbss` | 3,864  | 386 Offset Row | 10        |

| Layout | File                    | Known             | Unknown    |
| ------ | ----------------------- | ----------------- | ---------- |
| 1      | `itempuzzle.dbss`       | 46,324 B (100.0%) | 0 B (0.0%) |
| 1      | `itempuzzleoffset.dbss` | 3,864 B (100.0%)  | 0 B (0.0%) |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                          |
| ----------------------- | -------- | ----------------------------------------------------------------------------- |
| `itempuzzleoffset.dbss` | Optional | `puzzle_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`   | Optional | Item names (type `0`)                                                          |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 386 x 120 = 46,324 bytes.

### Row (120 bytes)

The 2016 `gc::ItemPuzzleStaticStatus` packed: its members in order, with no
alignment padding and without the `_makeItemEnchantStaticStatus` pointer.

| Offset  | Type    | Field                   | Notes                                                                 |
| ------- | ------- | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16     | puzzle_key              | Row key; `1` to `531` on client 3474, not every number used            |
| `+0x02` | u32[25] | puzzle_item_keys        | The 5 x 5 grid, row by row (`row x 5 + column`); item enchant keys, `0` for an empty cell; level `0` on every cell of clients 1784 and 3474 |
| `+0x66` | u32     | start_puzzle_item_key   | The first non-zero cell of the grid                                    |
| `+0x6A` | i32     | start_puzzle_item_index | Grid index of that cell                                                |
| `+0x6E` | i16     | width_max_index         | The highest column (0 to 4) holding an item                            |
| `+0x70` | i16     | height_max_index        | The highest row (0 to 4) holding an item                               |
| `+0x72` | u32     | make_item_key           | The item the puzzle makes; `0` on every row (clients 1784 and 3474), see Field Names |
| `+0x76` | i16     | line_count              | `5` on every row: the grid side                                        |

The rows are not sorted by key.

### `itempuzzleoffset.dbss`

Bare offset table into `itempuzzle.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `itempuzzle.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | puzzle_key  | Key of the row it points at                              |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `itempuzzle.dbss`, at its `puzzle_key` |
| `+0x06` | u32  | data_size   | `120` on every row: the whole row                        |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The 2016 client's debug symbols have `gc::ItemPuzzleStaticStatus` as
`_key` (u16), `_puzzle` (25 `gc::ItemEnchantKey`), `_startPuzzleItem`,
`_startPuzzleItemIndex`, `_widthMaxIndex`, `_heightMaxIndex`,
`_makeItemKey`, a pointer to the made item's `gc::ItemEnchantStaticStatus`
and `_lineCount`; the file holds every member but the pointer, in that
order. The `ItemPuzzle_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `PuzzleKey`, `Puzzle0`
to `Puzzle4`, `MakeItemKey` and `MakeItemEnchantLevel`, five sheet rows per
key (one per grid row). It matches the file:

| Field            | Column                           | Same value (client 1784) | Same value (client 3474) |
| ---------------- | -------------------------------- | ------------------------ | ------------------------ |
| puzzle_key       | `PuzzleKey`                      | 311 of 311               | 283 of 386               |
| puzzle_item_keys | `Puzzle0` to `Puzzle4`, 5 rows   | 311 of 311               | 282 of 283               |
| make_item_key    | `MakeItemKey`, `MakeItemEnchantLevel` | 311 of 311          | 283 of 283               |

The sheet has 337 keys, 26 more than client 1784 ships; client 3474 adds
103 keys and lays one shared puzzle out differently. The developer
workbook (`datasheet_itemdatatable_quest.xlsm`) marks `MakeItemKey` and
`MakeItemEnchantLevel` with `%`, server only: the compiled sheet and both
clients hold `0`. The client 519 server table `ItemPuzzle_Table` has the
same columns with the made items filled in (key `94` makes item `12034`).
`start_puzzle_item_key`, `start_puzzle_item_index`, `width_max_index`,
`height_max_index` and `line_count` have no sheet column; the 2016 names
fit what every row of clients 1784 and 3474 holds (Notes).

## Notes

- On every row of clients 1784 and 3474, `start_puzzle_item_index` is the
  first non-zero cell of `puzzle_item_keys`, `start_puzzle_item_key` the
  item in it, and `width_max_index` and `height_max_index` the highest
  column and row holding an item, counted from the grid's left and top
  edge.
- The treasure guide (`panel_window_treasure_guidebook_all_1.luac`) draws
  a treasure item's puzzle with `ToClient_GetPuzzleStaticStatusByPuzzleKey`
  and `getPuzzleItemKey(row, column)`, the grid order of
  `puzzle_item_keys`. The inventory (`panel_window_inventory_all_2.luac`
  and `_4.luac`) finds a laid-out puzzle with `findPuzzleAndReadyMake` and
  makes it with `requestMakePuzzle`; the combine bag
  (`panel_window_combine_1.luac` and `_2.luac`) has its own
  `findPuzzleAndReadyMakeCombineBag` and `requestMakePuzzleFromCombine`.
