# `itemmaxlevel.dbss` Format

## Purpose

Highest enhancement level per item, for every item with enhancement data. A
row is the item ID and one byte: `20` for gear that goes to PEN, `5` for an
accessory (PRI to PEN), `0` for an item that has an `enchant_key` but cannot
be enhanced.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------- | ---------------- | --------- |
| 1      | 3473 and later | 3473    | `itemmaxlevel.dbss`       | 151,880 | 30,372 Row       | 5         |
| 1      | 3473 and later | 3473    | `itemmaxleveloffset.dbss` | 364,484 | 30,372 Index Row | 12        |

| Layout | File                      | Known              | Unknown    |
| ------ | ------------------------- | ------------------ | ---------- |
| 1      | `itemmaxlevel.dbss`       | 151,880 B (100.0%) | 0 B (0.0%) |
| 1      | `itemmaxleveloffset.dbss` | 364,484 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`itemmaxleveloffset.dbss` (see below). Item names come from LOC type 0 and
icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                                       |
| ----------- | ---------- | ------------ | ----------------------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                                      |
| `+0x04`     | u32        | count        | Number of rows; `30,201` on client 3464                     |
| `+0x08`     | Row[count] | rows         | See Row                                                     |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table                            |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 5 * count`)                           |
| `rows+0x08` | u32        | zero         | Always `0`                                                  |

### Row (5 bytes)

| Offset  | Type | Field             | Notes                                                    |
| ------- | ---- | ----------------- | -------------------------------------------------------- |
| `+0x00` | u32  | item_id           | Unique; the rows are not in ID order                     |
| `+0x04` | u8   | max_enchant_level | Highest enhancement level; `0` to `25`                   |

Values on client 3464:

| max_enchant_level | Rows   |
| ----------------- | ------ |
| `0`               | 20,860 |
| `1`               | 4,156  |
| `2`               | 2      |
| `3`               | 4      |
| `5`               | 251    |
| `7`               | 50     |
| `10`              | 518    |
| `15`              | 105    |
| `20`              | 4,088  |
| `25`              | 167    |

### `itemmaxleveloffset.dbss`

The `PABR` index layout of `skilloffset.dbss`, read by
`parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type             | Field        | Notes                                                       |
| ----------- | ---------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`     | char[4]          | magic        | `PABR`                                                      |
| `+0x04`     | u32              | count        | Equals the `itemmaxlevel.dbss` count                        |
| `+0x08`     | Index Row[count] | rows         | See Index Row                                               |
| `rows+0x00` | u32              | string_count | `0`: the empty PABR string table                            |
| `rows+0x04` | u32              | table_start  | End of the rows (`8 + 12 * count`)                          |
| `rows+0x08` | u32              | zero         | Always `0`                                                  |

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                       |
| ------- | ---- | ------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key                                                     |
| `+0x04` | u32  | offset  | Start of the item's row in `itemmaxlevel.dbss`, at its `item_id` |
| `+0x08` | u32  | size    | Always `0`                                                  |

The index rows are in neither ID nor file order; on client 3464 each points
at the row of its own item.

## Notes

- The file is a copy of what [`itemenchant.dbss`](itemenchant_dbss.md)
  already holds. On client 3464 its 30,201 items are exactly the items with a
  non-zero `enchant_key`, and each row's value equals the highest
  `enchant_level` among that item's `itemenchant.dbss` keys (the Max Level
  column of that table). The 40,012 items without an `enchant_key` are left
  out; all of them have max level `0`.
  `test_itemmaxlevel_holds_the_max_level_of_every_item_with_an_enchant_key`
  in the `itemenchant.dbss` tests checks this against the installed client.
- The value is the stored level, not the shown one: accessories go to `5`,
  drawn as PRI to PEN in game, while gear goes to `20`, where `16` to `20` are
  PRI to PEN. So the table shows the number and not `enchant_level_text()`.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  describes the same `[u32 id][u8 maxLevel]` rows and the zero size column.
- The Central Market Lua (`panel_window_marketplace_buy`) reads a max level
  through `getMaxEnchantLevel()` on a market listing, not from this file.
