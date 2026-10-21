# `itemmarketcategory.bss` Format

## Purpose

The Central Market category tree: one row per main category (Main Weapon,
Sub-weapon, Awakening, Armor and on to Artifact/Lightstone) with its
sub-categories, the entries of the market's category list, and two filter
lists per main category. Filter 1 holds the enhancement levels on gear rows,
the stone tiers on Alchemy Stone, the classes on Pearl Item and the colours
on Dye; filter 2 holds the grade colours on Main Weapon and Alchemy Stone.
The market sends the main and sub category numbers to the server as they
stand here (`ToClient_requestListByWorldMarket(__eWorldMarketKeyType_Item,
mainCategoryValue:getCategoryNo(), subCategoryValue:getCategoryNo())` in
`panel_window_marketplace_itemmarket_renew.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records                    | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | -------------------------- | --------- |
| 1      | 1485 and later | 3474    | `itemmarketcategory.bss` | 5,999 | 420 Category Value, 18 Row | 5         |

| Layout | File                     | Known           | Unknown     |
| ------ | ------------------------ | --------------- | ----------- |
| 1      | `itemmarketcategory.bss` | 5,927 B (98.8%) | 72 B (1.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | No documented layout |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Category names, type 44 keyed (main, sub, filter 1, filter 2); see Notes |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field              | Notes                                                   |
| ------------------- | --------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32             | row_count          | Number of main categories; `18` on client 3474          |
| `+0x08`             | Row[row_count]  | rows               | See Row; sorted by `key`                                |
| `rows+0x00`         | String Table    | string_table       | The Korean category names                               |
| `string_table+0x00` | u32             | string_table_start | Absolute offset of `string_count` (`0x96E` on client 3474) |
| `string_table+0x04` | u32             | zero               | Always `0`                                              |

### Row (variable: 22 bytes + lists)

A list is a u32 count followed by that many Category Values.

| Offset                  | Type                               | Field                     | Notes                                                                 |
| ----------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00`                 | u8                                 | key                       | Main category number; equals `main_category.category_no` on every row (clients 1784 and 3474) |
| `+0x01`                 | Category Value                     | main_category             | `getMainCategoryValue()`; `1`, then `5` to `85` in steps of 5       |
| `+0x06`                 | u32                                | sub_category_count        | Number of `sub_categories`; `getSubCategoryListCount()`               |
| `+0x0A`                 | Category Value[sub_category_count] | sub_categories            | `getSubCategoryAt(i)`; the entries of the market's category list      |
| `sub_categories+0x00`   | u32                                | filter1_count             | Number of `filter1_values`; `0` on 6 of 18 rows (client 3474)         |
| `sub_categories+0x04`   | Category Value[filter1_count]      | filter1_values            | Enhancement levels (`+ 0` to `PEN (V)`), stone tiers, classes or dye colours |
| `filter1_values+0x00`   | u32                                | filter2_count             | Number of `filter2_values`; only Main Weapon (3) and Alchemy Stone (4) have any |
| `filter1_values+0x04`   | Category Value[filter2_count]      | filter2_values            | Grade colours: `2` green, `3` blue, `4` yellow, and `1` white on Alchemy Stone |
| `filter2_values+0x00`   | u32                                | unknown_filter2_values_00 | `7` on 10 of 18 rows (client 3474); see Open Questions                |

### Category Value (5 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u8   | category_no | `getCategoryNo()`; unique within its list, from 1 with gaps            |
| `+0x01` | u32  | name_ref    | String table index of the Korean name (`getCategoryName()` text in the Korean client) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | `291` on client 3474                                     |
| `+0x04` | pstr[string_count] | strings      | All wide; `name_ref` indexes them, each string once      |

## Field Names

The names are the `MarketCategoryNameTag` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `MarketCategory1`,
`MarketCategory2`, `MarketFilter1`, `MarketFilter2` and `NameTag`. A sheet
row with only `MarketCategory1` set is a `main_category`, one with
`MarketCategory2` set a `sub_categories` entry, and one with `MarketFilter1`
or `MarketFilter2` set a `filter1_values` or `filter2_values` entry; its
`NameTag` is the string `name_ref` points at.

| Keys compared                          | Same name (client 1784) | Same name (client 3474) |
| -------------------------------------- | ----------------------- | ----------------------- |
| (category, sub-category, filter 1, filter 2) | 359 of 359        | 328 of 344              |

The sheet has 360 rows; its one row with no entry in the file is
`MarketCategory1` 10, `MarketCategory2` 18 (`악기`), and both clients skip
sub-category 18 under Awakening. The 16 misses on client 3474 are lists
that were re-sorted after client 1784: Material, Enhancement, Consumables
and Magic Crystal (Magic Crystal's sub-categories were gear slots on
client 1784 and are crystal types on client 3474).

## Notes

- LOC type 44 holds the English names, keyed `str_id1` main category,
  `str_id2` sub-category, `str_id3` filter 1 and `str_id4` filter 2, with
  `0` for the parts a row does not have: (1, 0, 0, 0) is `Main Weapon`,
  (10, 17, 0, 0) `Greatbow`, (1, 0, 17, 0) `PRI (I)`. On client 3474 it
  covers 413 of the 420 keys of the file; the 7 others are the
  `filter2_values` grade colours, which have no LOC text. LOC also keeps 8
  keys the file no longer has (Magic Crystal's old gear-slot entries and
  Dye filter 1 `Real Red`).
- The market lists the categories through
  `PaGlobalFunc_getItemMarketCategoryListAndSetUI` in
  `global_util_itemacquirehelper.luac`, in file order: each row, then its
  `sub_categories`. The Lua reads `getFilterListCount(0)` in two places and
  uses the result nowhere; no Lua reads a filter entry.
- The sheet `MarketCategoryOrder` of the same client 1784 source has a
  `ContentsGroupKey` per (`MarketCategory1`, `MarketCategory2`); the file
  holds no such column.

## Open Questions

### `unknown_filter2_values_00`

The u32 after the lists is `7` on 10 of 18 rows on client 3474 and on 13
of 17 rows on client 1784 (`0` on 3 more there). The other rows hold values
whose bytes read as UTF-16 text fragments (`72 00 71 00` is `rq`, `75 00 65
00` is `ue`), which points at memory the build did not clear. No Lua call
returns it.
