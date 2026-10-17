# `encyclopedia.bss` Format

## Purpose

The entries of the Fishing Encyclopedia (`panel_window_fishencyclopedia_renewal_all`):
one fixed 104-byte row per fish with its item, category tab, rareness, base
size, Korean description and artwork path. The window reads a row through
`ToClient_GetFishEncyclopedia(index)` (`getKey()`, `getName()`,
`getImagePath()`, `getDesc()`, `getGradeType()`, `getAverageValue()`) and lists a tab with
`ToClient_GetFishCountByCategory(category)`. The source sheet is
`Encyclopedia_Table`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes   | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------- | ------------------- | --------- |
| 2      | 3473 and later | 3474    | `encyclopedia.bss` | 129,560 | 1,510 Dice, 302 Row | 12        |
| 1      | 1784           | 1784    | `encyclopedia.bss` | 70,989  | 1,010 Dice, 202 Row | 12        |

| Layout | File               | Known             | Unknown        |
| ------ | ------------------ | ----------------- | -------------- |
| 2      | `encyclopedia.bss` | 127,144 B (98.1%) | 2,416 B (1.9%) |
| 1      | `encyclopedia.bss` | 70,181 B (98.9%)  | 808 B (1.1%)   |

<!-- versions:end -->

## Companion Files

None. LOC type 30 holds the description by `key` (`str_id1`, `str_id4` 0),
and LOC type 0 names the item of `item_id`.

All multi-byte values are little-endian.

## Layout 2

### File Layout

PABR block of fixed rows, followed by the same counted string table and
8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds two strings per row, the
description and the artwork path.

| Offset              | Type         | Field              | Notes                              |
| ------------------- | ------------ | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                       |
| `+0x04`             | u32          | count              | Number of rows; 302 on client 3473 |
| `+0x08`             | Row[count]   | rows               | See Row                            |
| `rows+0x00`         | String Table | string_table       | 604 wide strings on client 3473    |
| `string_table+0x00` | u32          | string_table_start | Where the rows end                 |
| `string_table+0x04` | u32          | zero               | Always `0`                         |

Rows are sorted by key. On client 3473 the keys run from 1 to 305 with 3
gaps.

### Row (104 bytes)

| Offset  | Type    | Field         | Notes                                                                                   |
| ------- | ------- | ------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16     | key           | Entry key (`Key`, `getKey()`); LOC type 30 `str_id1` of the description                  |
| `+0x02` | u32     | item_id       | The fish item (`TypeKey`), an `Item_Table` key; LOC type 0 names it                      |
| `+0x06` | u32     | type          | Encyclopedia kind (`Type`): `0` fish on every row                                        |
| `+0x0A` | u8      | category      | Tab of the window (`Category`); see Categories                                          |
| `+0x0B` | u8      | rareness      | `1` to `10` (`Rareness`); see Rareness                                                  |
| `+0x0C` | f32     | base_size     | Smallest size in cm (`BaseSize`)                                                        |
| `+0x10` | f32     | unknown_10    | Whole numbers, 9 to 169 on client 3473; see Average Size                                |
| `+0x14` | u64     | fish_exp_rate | `0` on every row (`FishExpRate`, server only)                                            |
| `+0x1C` | u32     | fish_exp_type | `0` on every row (`FishExpType`, server only)                                            |
| `+0x20` | u32     | desc_ref      | String table index of the Korean description (`Desc`)                                   |
| `+0x24` | u32     | image_ref     | String table index of the artwork path (`Image`), relative to `ui_texture/`             |
| `+0x28` | Dice[5] | vary_sizes    | `VarySize_0` to `VarySize_4`, server only: `1D1+0` on every row                          |
| `+0x64` | u32     | unknown_64    | `0` on every row                                                                        |

### Dice (12 bytes)

A size roll written `<count>D<sides>+<bonus>` in the sheet (`1D2+2` rolls
one two-sided die and adds 2).

| Offset  | Type | Field  | Notes                                          |
| ------- | ---- | ------ | ---------------------------------------------- |
| `+0x00` | u32  | count  | Number of dice; `1` on every row of the client |
| `+0x04` | u32  | sides  | Sides per die; `1` on every row of the client  |
| `+0x08` | i32  | bonus  | Added to the roll; `0` on every row of the client |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                       |
| ------- | ------------------ | ------------ | ------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                           |
| `+0x04` | pstr[string_count] | strings      | `desc_ref` and `image_ref` index this list  |

## Layout 1

On client 1784 `base_size` is a u16 and there is no `unknown_10`, so the row
is 98 bytes. Only the Row differs from Layout 2.

### Row (98 bytes)

| Offset  | Type    | Field         | Notes                       |
| ------- | ------- | ------------- | --------------------------- |
| `+0x00` | u16     | key           |                             |
| `+0x02` | u32     | item_id       |                             |
| `+0x06` | u32     | type          |                             |
| `+0x0A` | u8      | category      |                             |
| `+0x0B` | u8      | rareness      |                             |
| `+0x0C` | u16     | base_size     | `0` on every row (server only on client 1784) |
| `+0x0E` | u64     | fish_exp_rate |                             |
| `+0x16` | u32     | fish_exp_type |                             |
| `+0x1A` | u32     | desc_ref      |                             |
| `+0x1E` | u32     | image_ref     |                             |
| `+0x22` | Dice[5] | vary_sizes    |                             |
| `+0x5E` | u32     | unknown_64    |                             |

Client 1784 has 202 rows, keys 1 to 202.

## Categories

`category` selects the tab. The window maps its four tabs to the values
`1`, `2`, `3`, `0` (`_categoryMapping` in
`panel_window_fishencyclopedia_renewal_all.lua`) and labels them with
`PANEL_FISH_RADIO_1` to `_4`. The source workbook's `#참조` sheet lists the
same names.

| Value | Tab                | Rows (client 3473) |
| ----- | ------------------ | ------------------ |
| 0     | 기타 (Others)       | 23                 |
| 1     | 민물고기 (Freshwater) | 106                |
| 2     | 바다물고기 (Saltwater) | 163                |
| 3     | 갑각류 (Crustacean)  | 10                 |

The workbook comment reserves 6 to 12 (herbs, stone, wood, mushrooms, sap,
hide, meat) for a gathering encyclopedia (`type` 1) that no row of this
file uses.

## Rareness

`rareness` is the workbook's rarity grade, 1 to 10, higher is harder to get.
The workbook comment ties it to which `VarySize_N` roll a catch uses by the
number of that fish caught so far (grade 1: 1 to 150 catches use
`VarySize_0`, 151 to 300 `VarySize_1`, and so on). The old encyclopedia
window (`panel_window_fishencyclopedia_all`) drew up to five stars from
`getRareness()`; the current window colours the name by `getGradeType()`,
which is not a field of this file.

## Average Size

The window prints Average Size from `getAverageValue()` of the entry
(`panel_window_fishencyclopedia_renewal_all.lua`), for caught and uncaught
fish alike. On client 3474 it matched `(base_size + unknown_10) / 2` on four
fish, two of them with `unknown_10` below `base_size`:

| Fish       | base_size | unknown_10 | Average Size |
| ---------- | --------- | ---------- | ------------ |
| Mudskipper | 7         | 9          | 8.000        |
| Tuna       | 40        | 169        | 104.500      |
| Sunfish    | 280       | 99         | 189.500      |
| Notch Jaw  | 25        | 9          | 17.000       |

The handler shows that value as the Average Size column. What `unknown_10`
is on its own stays open; see Open Questions.

## Field Names

The fields are the columns of the `Encyclopedia_Table` sheet that a private
server on client 1784 ships in its `DataSheets.bexcel` and in the developer
workbook `DataSheet_Encyclopedia.xlsm`. Against client 3473 the workbook
shares 202 keys:

| Field       | Column     | Matches (client 3473) |
| ----------- | ---------- | --------------------- |
| `item_id`   | `TypeKey`  | 202 of 202            |
| `type`      | `Type`     | 202 of 202 (all `0`)  |
| `category`  | `Category` | 180 of 202            |
| `rareness`  | `Rareness` | 202 of 202            |
| `base_size` | `BaseSize` | 202 of 202            |
| `desc_ref`  | `Desc`     | 183 of 202 by text    |
| `image_ref` | `Image`    | 114 of 202 by path    |

The 22 `category` misses are entries moved to another tab since. 13 of
them (keys 177 to 202, among them the sharks) are `0` in the workbook and
`2` now, and the octopus and squid rows (12, 133, 141, 151) went from `2`
to `0`. The description misses are rewritten texts. All 88 image misses are
rows whose workbook path is the `Fish_unknown.dds` placeholder; the other
114 differ only in the `Encyclopedia/` folder the client path adds.

The workbook marks `BaseSize`, `VarySize_0` to `_4`, `FishExpType` and
`FishExpRate` with `%`, server only: the client 1784 file writes `0` in
`base_size` and the default roll `1D1+0` in each `vary_sizes`. Client 3473
fills `base_size` again (7 for the Mudskipper, 40 for the Tuna, the workbook
values) and keeps the other server-only columns empty.

The private server's own `encyclopedia.bss` built from that sheet is
byte-identical to the client 1784 file. The field widths and their order
come from the private server's server dump: its `Encyclopedia_Table` loader
reads `TypeKey` and `Type` as u32, `Category` and `Rareness` as u8,
`BaseSize` as u16, `FishExpRate` as 8 bytes and `FishExpType` as u32, and
stores them in that order, the order of the client row. That fixes the
14 bytes at `+0x0C` of client 1784 (2 + 8 + 4) and so the
`fish_exp_rate` and `fish_exp_type` slots, which are `0` in both clients.
The same loader parses each `VarySize_N` string with the pattern
`(d)|(D)|(\+)|(\-)` into three 4-byte values in text order (count, sides,
bonus, negated after a `-`), and turns the string `0` into `1, 1, 0`: the
`1D1+0` of every client row.

Neither the 2016 client with debug symbols nor the server code of a private
server on client 519 has an encyclopedia type; that server's
`Encyclopedia_Table` holds 189 rows with `0` in every server-only column.

## Notes

- The Korean descriptions in the string table use real line breaks. LOC type
  30 has an entry for each of the 302 keys on client 3473, the translated
  description (key 1: "Mudskippers are known for their strong obsession with
  food. ...").
- Each `image_ref` path (`UI_Artwork/Encyclopedia/IC_08501.dds`) is a whole
  texture under `ui_texture/`, lower-cased:
  `ui_texture/ui_artwork/encyclopedia/ic_08501.dds`. All 302 exist on client
  3473. An empty slot of the window shows `fish_undiscover.dds`, which the
  Lua sets itself.
- The window search (`ToClient_SetFishListByKeyword(keyword, category)`),
  the size ranking (`ToClient_RequestFishTopRankingBody(key)`) and My
  Information's Max Size (`getMaxValue()`) and Capture Count (`getCount()`)
  come from the server; no field of this file holds a caught size. Average
  Size (`getAverageValue()`) is a value of the entry, set for caught and
  uncaught fish alike; see Average Size.
- bdo-data-extractor's FORMATS.md lists this file as 300 rows of 104 bytes
  with `id`, `knowledgeCode`, a two-f32 `sizeRange` and two string
  references. There is no knowledge field; the two f32s are `base_size` and
  `unknown_10`.

## Open Questions

### unknown_10

`unknown_10` is a whole-number f32 from 9 to 169 on client 3473, new since
client 1784. On all 202 keys the workbook shares it equals the dice count
times the sides of `VarySize_4` (`3D3+7` gives 9, `13D13+92` gives 169), the
largest roll without its bonus. No sheet column has that value, and the
only client use found is Average Size. The windows of four fish rule out
two readings:

- A size range from `base_size` to `base_size + unknown_10`: the ranking's
  top Mudskipper is 28.507 and its top Tuna 326.866, above 16 and 209.
- An upper bound: `unknown_10` is below `base_size` on 176 of 302 rows
  (client 3474), the Sunfish has 280 and 99.
