# `dyeingpalette.dbss` Format

## Purpose

The colours of every dye palette: one row per palette type, each a list of
colours with an environment and a specular value. A dye item in
[`itempalette.dbss`](itempalette_dbss.md) points at one colour by palette
type and index. Types `1` to `8` are the eight tabs of the dye window
(Basic Dye, then the seven town dyes from Olvian to Valencian Dye); type
`100` holds six lantern colours. Companion `dyeingpaletteoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records            | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ------ | ------------------ | --------- |
| 1      | 1485 and later | 3474    | `dyeingpalette.dbss`       | 14,026 | 1,161 Color, 9 Row | 12        |
| 1      | 1485 and later | 3474    | `dyeingpaletteoffset.dbss` | 85     | 9 Offset Row       | 9         |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `dyeingpalette.dbss`       | 14,017 B (99.9%) | 9 B (0.1%) |
| 1      | `dyeingpaletteoffset.dbss` | 85 B (100.0%)    | 0 B (0.0%) |

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

| File                       | Required | Role                                                                          |
| -------------------------- | -------- | ----------------------------------------------------------------------------- |
| `dyeingpaletteoffset.dbss` | Optional | `palette_type -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `itempalette.dbss`         | Optional | The dye items of each colour, for the Dye Items column                         |
| `languagedata_en.loc`      | Optional | Item names (type `0`) and the dye window's tab names (type `37`)               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `9` on client 3474      |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 10 bytes + colors)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u8                 | palette_type | Row key, the `palette_type` of `itempalette.dbss`                      |
| `+0x01` | u8                 | unknown_01   | `0` on every row (clients 1784 and 3474); the offset index points here |
| `+0x02` | u64                | color_count  | Number of colours                                                      |
| `+0x0A` | Color[color_count] | colors       | See Color; a colour's position is its `palette_index`                  |

### Color (12 bytes)

The 2016 `gc::DyeingPaletteValue`: a `pa::Color` (blue, green, red, alpha)
and two floats.

| Offset  | Type | Field       | Notes                                                               |
| ------- | ---- | ----------- | ------------------------------------------------------------------- |
| `+0x00` | u8   | color_b     | Blue                                                                |
| `+0x01` | u8   | color_g     | Green                                                               |
| `+0x02` | u8   | color_r     | Red                                                                 |
| `+0x03` | u8   | color_a     | Alpha of the `pa::Color`; `0` on every colour (clients 1784 and 3474) |
| `+0x04` | f32  | environment | One value per palette type, see Palette Types                       |
| `+0x08` | f32  | specular    | One value per palette type, see Palette Types                       |

### `dyeingpaletteoffset.dbss`

Bare offset table into `dyeingpalette.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `dyeingpalette.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (9 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u8   | palette_type | Key of the row it points at                                  |
| `+0x01` | u32  | data_offset  | Row start + 1, at `unknown_01`                               |
| `+0x05` | u32  | data_size    | The row size - 1: `9 + 12 x color_count`                     |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`. The
index lists type `100` between types `3` and `4`; the main file stores the
rows by type. On clients 1784 and 3474 every index row points at the row
with its key.

## Palette Types

On client 3474 (the same on client 1784):

| Type | Dye window tab (LOC English) | Colours | Environment | Specular |
| ---- | ---------------------------- | ------- | ----------- | -------- |
| 1    | Basic Dye                    | 224     | `-1`        | `-1`     |
| 2    | Olvian Dye                   | 133     | `0`         | `0.02`   |
| 3    | Velian Dye                   | 133     | `0`         | `0.8`    |
| 4    | Heidelian Dye                | 133     | `0.63`      | `0.02`   |
| 5    | Keplanian Dye                | 133     | `0.94`      | `0.39`   |
| 6    | Calpheonian Dye              | 133     | `0.51`      | `0.63`   |
| 7    | Mediahn Dye                  | 133     | `0.57`      | `0.91`   |
| 8    | Valencian Dye                | 133     | `0.94`      | `0.97`   |
| 100  | none                         | 6       | `0`         | `0`      |

The tab names are `LUA_PALETTE_TAB_MATERIAL_0` to `_7` of the dye window
(`panel_window_dyeingpalette_renew.luac`), and the dye items of type N are
the dyes of tab N - 1 (see [`itempalette.dbss`](itempalette_dbss.md)). The
tab descriptions (`LUA_PALETTE_TAB_MATERIAL_DESC_0` to `_7`) name a
material per tab: any material for Basic Dye, then cloth, glossy cloth,
silk, leather, glossy leather, metal and shiny metal.

## Field Names

The `DyeingPalette_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Type`, `Env`, `Specular`, `ColorR`, `ColorG`
and `ColorB`, one sheet row per colour in file order. Its 1,161 rows match
all 1,161 colours of the file on all six columns, on client 1784 and on
client 3474: `Type` is `palette_type`, the colour's position among the rows
of its type is `palette_index`. The 2016 client's debug symbols name the
colour `gc::DyeingPaletteValue` (`_color`, `_environment`, `_specular`, the
`pa::Color` with the members `b`, `g`, `r`, `a`) and the row
`gc::DyeingPaletteStaticStauts` (sic) with `_dyeingPaletteValueList` and a
u8 `_type`, held in a map by u8 type. The developer workbook
(`datasheet_itemdatatable_cash.xlsm`) adds the note columns `#참조 -Index`
(the palette index), `#참조 -RGB색상표` (the colour as `#867e7e`) and
`#참조-색상명` with the colour's name: `염색약 - 탁한 빨강 #1` ("dye - dull
red #1") in type 1, `Type1 스노우 레드` ("Type1 snow red") in type 2, and
`노란색 랜턴` ("yellow lantern") to `아타니스 반딧불` ("Atanis firefly")
in type 100.

## Notes

- The colour is stored as blue, green, red, alpha, the byte order of
  `pa::Color`; the sheet has no alpha column.

## Open Questions

### What `unknown_01` Holds

The byte after the palette type is `0` in all 9 rows of clients 1784 and
3474, and the offset index points at it, so the index sees it as the
first byte of the record. The 2016 struct has a u8 `_type` after the
colour list, which the file does not store there; whether this byte is a
second type byte, a flag, or the high byte of a u16 key is not in the
client data.

### What Reads Palette Type 100

Type `100` holds six lantern colours (the workbook notes name them) and
no `itempalette.dbss` row points at it. The dye window's Lua
(`panel_window_dyeingpalette_renew.luac`) has tabs for types 1 to 8 only;
which feature offers the lantern colours is not in the client data
checked so far.
