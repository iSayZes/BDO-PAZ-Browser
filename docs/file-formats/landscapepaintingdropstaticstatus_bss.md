# `landscapepaintingdropstaticstatus.bss` Format

## Purpose

The landscape paintings of the `Panel_Window_LandscapePaintingDrop`
window: one row per painting with its Korean name, a list of u32 keys and
the treasure item piece the window names for it. The window Lua
(`panel_window_landscapepaintingdrop_1.luac`) reads a painting by its type
through `ToClient_landscapePaintingDropString(type)` (the name) and
`ToClient_landscapePaintingDropItemEnchantKey(type)` (the drop item), and
the paints that charge it through
`ToClient_getItemLandScapePaintingChargeByIndex(type, index)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes  | Records | Row bytes                      |
| ------ | -------------- | ------- | --------------------------------------- | ------ | ------- | ------------------------------ |
| 2      | 3474 and later | 3482    | `landscapepaintingdropstaticstatus.bss` | 15,776 | 14 Row  | 953 to 1,153, 1,106 on average |
| 1      | 3251           | 3251    | `landscapepaintingdropstaticstatus.bss` | 10,734 | 12 Row  | 833 to 909, 873 on average     |

| Layout | File                                    | Known        | Unknown          |
| ------ | --------------------------------------- | ------------ | ---------------- |
| 2      | `landscapepaintingdropstaticstatus.bss` | 424 B (2.7%) | 15,352 B (97.3%) |
| 1      | `landscapepaintingdropstaticstatus.bss` | 318 B (3.0%) | 10,416 B (97.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2765   | No file  |
| 2637   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Painting names (type 126) and drop item names (type 0)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of paintings; `14` on client 3482      |
| `+0x08`             | Row[row_count] | rows         | See Row; in type order                        |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 17 bytes + unknown_0d list)

| Offset            | Type             | Field                   | Notes                                                                          |
| ----------------- | ---------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00`           | u8               | landscape_painting_type | The painting, `0` to `13`; LOC type 126 name. See Paintings                    |
| `+0x01`           | u32              | unknown_01              | `30009` plus `landscape_painting_type` on every row (client 3482)              |
| `+0x05`           | u32              | name_index              | Index into `strings`: the Korean name; equal to the type on every row          |
| `+0x09`           | u32              | unknown_09              | Number of `unknown_0d` entries; `234` to `284` on client 3482                  |
| `+0x0D`           | u32[unknown_09]  | unknown_0d              | Keys `217619` to `226141` on client 3482; see Open Questions                   |
| `unknown_0d+0x00` | u32              | drop_item_key           | The treasure piece (LOC type 0 name); the window opens the drop search on its name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                            |
| ------- | ------------------ | ------------ | ------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `14` on client 3482           |
| `+0x04` | pstr[string_count] | strings      | The Korean painting names, UTF-16LE, in row order |

## Layout 1

No `drop_item_key`: the row ends with the `unknown_0d` list. 12 paintings
on client 3251. Only the Row differs from Layout 2.

### Row (variable: 13 bytes + unknown_0d list)

| Offset  | Type            | Field                   | Notes |
| ------- | --------------- | ----------------------- | ----- |
| `+0x00` | u8              | landscape_painting_type |       |
| `+0x01` | u32             | unknown_01              |       |
| `+0x05` | u32             | name_index              |       |
| `+0x09` | u32             | unknown_09              |       |
| `+0x0D` | u32[unknown_09] | unknown_0d              |       |

## Paintings

Client 3482, in file order. The type is the index the window Lua passes
to every `ToClient_*LandScapePainting*` call; its `_indexForType` table
names the same order with the `__eLandscapePaintingType_*` members, whose
numbers are not in the Lua. LOC type 126 `str_id1` is the type.

| Type | LOC type 126 name         | Lua member               | `drop_item_key`                                    |
| ---- | ------------------------- | ------------------------ | -------------------------------------------------- |
| 0    | Roud Sulfur Mine          | `Sulfur`                 | 44273 Archaeologist's Map Piece                    |
| 1    | Pila Ku Jail              | `PilaKu`                 | 44273 Archaeologist's Map Piece                    |
| 2    | Aakman Temple             | `Aakman`                 | 44278 Lafi Bedmountain's Upgraded Compass Parts    |
| 3    | Hystria Ruins             | `Hystria`                | 44278 Lafi Bedmountain's Upgraded Compass Parts    |
| 4    | Sycraia Underwater Ruins  | `SycraiaUpper`           | 44270 Al Yurad's Ring Piece                        |
| 5    | Padix Island              | `Padix`                  | 44270 Al Yurad's Ring Piece                        |
| 6    | Ash Forest                | `AshForest`              | 44270 Al Yurad's Ring Piece                        |
| 7    | Crypt of Resting Thoughts | `CryptOfRestingThoughts` | 44270 Al Yurad's Ring Piece                        |
| 8    | Olun's Valley             | `OlunsValley`            | 44270 Al Yurad's Ring Piece                        |
| 9    | City of the Dead          | `CityOfTheDead`          | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 10   | Tungrad Ruins             | `Tungrad`                | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 11   | Darkseekers' Retreat      | `Darkseekers`            | 65331 Lafi Bedmountain's Upgraded Telescope Parts  |
| 12   | Gavinya Coastal Cliff     | `SulfurGolem`            | 44270 Al Yurad's Ring Piece                        |
| 13   | La Orzeca                 | `LaOrzeca`               | 45013 Quturan's Left Lung                          |

## Notes

- The paints that charge a painting (Roud Sulfur Mine Paint `761714`,
  Pila Ku Jail Paint `761715`, Aakman Temple Paint `761716`) are items
  with `contents_event_type` `154` in `itemenchant.dbss`, their
  `contents_event_param1` the painting type and `contents_event_param2`
  the points (`10000`). The window reads the points with
  `getContentsEventParam2()`.
- The file is not in client 1784.

## Open Questions

### What `unknown_0d` Lists

Each row lists 234 to 284 u32 keys between `217619` and `226141` (client
3482); the lists of the 14 paintings are nearly the same, so they do not
name the monsters of one area. No other `gamecommondata/binary` table of
client 3482 holds these values, and they are no item or character keys.

### What `unknown_01` Is

`unknown_01` runs from `30009` to `30022`, one per painting. LOC type 0
and 10 have names under these numbers (`30009` Tachros), which do not fit
the paintings, so the key is from another table.
