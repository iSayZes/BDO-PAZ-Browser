# `funtitureiteminfo.bss` Format

## Purpose

Furniture items: one 9-byte row per item that places a house or manor
furnishing, with the installation type of the object it places. The file
name is spelled `funtiture` in the client. Each item places one
[`characterobject.dbss`](characterobject_dbss.md) object (the record whose
item ID is the row's item), and `installation_type` equals that object's
`installation_type` on 520 of 520 rows of client 3482. No Lua file of
client 3482 names the table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 1348 and later | 3482    | `funtitureiteminfo.bss` | 4,700 | 520 Row | 9         |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 1      | `funtitureiteminfo.bss` | 4,700 B (100.0%) | 0 B (0.0%) |

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
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (9 bytes)

| Offset  | Type | Field             | Notes                                                                        |
| ------- | ---- | ----------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key          | The furniture item (LOC type 0 name); unique per row                         |
| `+0x04` | u32  | item_key_dup      | Equal to `item_key` on every row (clients 1784 and 3482)                     |
| `+0x08` | u8   | installation_type | `CppEnums.InstallationType` of the placed object; see Installation Types     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                           |
| ------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                           |

## Installation Types

`CppEnums.InstallationType` in `global_define_cpp_enum.luac` (client
3482) names the values. Rows per value are from client 3482. For `9` and
up the items match the enum name; for `1` to `8` (except `4`) they are
pieces of furniture the enum names do not describe, in the order of the
`interiorrelationpoint.dbss` relation columns.

| Value | Enum name     | Rows | Items                                                     |
| ----- | ------------- | ---- | --------------------------------------------------------- |
| 0     | Default       | 92   | [Manor] decorations                                        |
| 1     | Carpenter     | 31   | Dressers (`서랍장`)                                        |
| 2     | Alchemy1      | 29   | Bedside cabinets (`협탁`)                                  |
| 3     | Founding      | 33   | Wardrobes (`옷장`)                                         |
| 4     | Cooking       | 2    | Advanced and Supreme Cooking Utensil                       |
| 5     | Forging       | 31   | Dining tables (`식탁`)                                     |
| 6     | Treasure      | 34   | Tables (`탁자`)                                            |
| 7     | Smithing      | 33   | Chairs                                                     |
| 8     | Weaving       | 33   | Sofas                                                      |
| 9     | Bed           | 32   | Beds                                                       |
| 10    | Havest        | 2    | Cherry Blossom Seed and its [Event] copy                   |
| 17    | Buff          | 3    | [Event] 3rd Anniversary Cake, Halloween Jack-O'-Lantern, Halloween Pumpkin Doll Lamp |
| 19    | Bookcase      | 31   | Bookcases and desks                                        |
| 20    | WarehouseBox  | 1    | Premium Container                                          |
| 21    | Alchemy       | 2    | Advanced and Supreme Alchemy Tool                          |
| 22    | JukeBox       | 15   | Jukebox records                                            |
| 24    | WallPaper     | 49   | Wallpapers                                                 |
| 25    | FloorMaterial | 43   | Floor coverings                                            |
| 26    | Chandelier    | 10   | Chandeliers                                                |
| 27    | Curtain       | 4    | Curtains                                                   |
| 30    | Maid          | 2    | Maid contracts                                             |
| 31    | Curtain_Tied  | 4    | Tied curtains                                              |
| 34    | InstanceWater | 3    | Margoria Whale Hexagonal Fish Tank, L'elisir d'amore Aquarium Table and Hot Tub |
| 35    | Shelf         | 1    | L'elisir d'amore Wall Shelf                                |

## Notes

- 313 of the 520 items of client 3482 place an object that has a row in
  [`interiorrelationpoint.dbss`](interiorrelationpoint_dbss.md); every
  item of types `2`, `5`, `7`, `8` and `9` does. 17 of the 92
  type `0` items place an object listed in
  [`mansiondata.dbss`](mansiondata_dbss.md). Both tables are keyed by the
  object's character key, not by the item, so the link runs through
  `characterobject.dbss`.
- The `interiorrelationpoint.dbss` relation columns `on_dresser` to
  `on_bed`, `on_book_case` and `on_shelf` are the furniture of types `1`,
  `2`, `3`, `5` to `9`, `19` and `35` in that order.
- Client 1784 has 489 rows with the same layout; it has no type `4`, `20`
  or `21` row.

## Open Questions

### Types 1 to 8

The dressers, bedside cabinets, wardrobes, dining tables, tables, chairs
and sofas carry the `InstallationType` values `1`, `2`, `3` and `5` to `8`,
which the Lua enum names Carpenter, Alchemy1, Founding, Forging, Treasure,
Smithing and Weaving. Whether the client reads these values as furniture
kinds for this table (the `interiorrelationpoint.dbss` column order
suggests it) or the enum names are left over from older workshop types is
open.
