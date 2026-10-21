# `itempalette.dbss` Format

## Purpose

The dye colour each dye item applies: per item key a palette type (a row
of [`dyeingpalette.dbss`](dyeingpalette_dbss.md)) and the index of the
colour in that palette. Palette types `1` to `8` are the eight tabs of the
dye window, Basic Dye to Valencian Dye. Companion `itempaletteoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------ | ---------------- | --------- |
| 1      | 1485 and later | 3474    | `itempalette.dbss`       | 6,766  | 1,127 Row        | 6         |
| 1      | 1485 and later | 3474    | `itempaletteoffset.dbss` | 13,528 | 1,127 Offset Row | 12        |

| Layout | File                     | Known             | Unknown    |
| ------ | ------------------------ | ----------------- | ---------- |
| 1      | `itempalette.dbss`       | 6,766 B (100.0%)  | 0 B (0.0%) |
| 1      | `itempaletteoffset.dbss` | 13,528 B (100.0%) | 0 B (0.0%) |

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

| File                     | Required | Role                                                                          |
| ------------------------ | -------- | ----------------------------------------------------------------------------- |
| `itempaletteoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `dyeingpalette.dbss`     | Optional | The colour at `palette_type` and `palette_index`, for the Color column         |
| `languagedata_en.loc`    | Optional | Item names (type `0`) and the dye window's tab names (type `37`)               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 1,127 x 6 = 6,766 bytes.

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                                  |
| ------- | ---- | ------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key      | The dye item, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x04` | u8   | palette_type  | `palette_type` of a [`dyeingpalette.dbss`](dyeingpalette_dbss.md) row; `1` to `8`      |
| `+0x05` | u8   | palette_index | Position of the colour in that row's `colors`, from 0                                  |

The rows are not sorted by key.

### `itempaletteoffset.dbss`

Bare offset table into `itempalette.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `itempalette.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                  |
| ------- | ---- | ----------- | ------------------------------------------------------ |
| `+0x00` | u32  | item_key    | Key of the row it points at                            |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itempalette.dbss`, at its `item_key` |
| `+0x08` | u32  | data_size   | `6` on every row: the whole row                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

## Palette Types

The dye window (`panel_window_dyeingpalette_renew.luac`) names its tabs
`LUA_PALETTE_TAB_MATERIAL_0` to `LUA_PALETTE_TAB_MATERIAL_7`, and the dye
items of palette type N are the dyes of tab N - 1: type `2` holds the
`[Olvian Dye]` items, type `8` the `[Valencian Dye]` items.

| Type | Tab (LOC English) | Rows (client 3474) |
| ---- | ----------------- | ------------------ |
| 1    | Basic Dye         | 196                |
| 2    | Olvian Dye        | 133                |
| 3    | Velian Dye        | 133                |
| 4    | Heidelian Dye     | 133                |
| 5    | Keplanian Dye     | 133                |
| 6    | Calpheonian Dye   | 133                |
| 7    | Mediahn Dye       | 133                |
| 8    | Valencian Dye     | 133                |

## Field Names

The 2016 client's debug symbols have `gc::ItemPaletteStaticStatus` as
`_key` (a `gc::ItemEnchantKey`), `_paletteType` and `_paletteIndex`, then a
pointer to the `gc::DyeingPaletteStaticStauts` (sic) it resolves to; the
file holds the first three. The `DyeingItem_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `ItemKey`,
`PaletteType` and `PaletteIndex`, and its 1,127 rows match the file on all
1,127 keys and both values, on client 1784 and on client 3474.

## Notes

- On client 3474, 1,119 of the 1,161 `dyeingpalette.dbss` colours have a
  dye item; 8 of them have two.
- Every row of clients 1784 and 3474 points at a colour that
  `dyeingpalette.dbss` holds.
