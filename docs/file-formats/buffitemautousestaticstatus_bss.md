# `buffitemautousestaticstatus.bss` Format

## Purpose

The items the auto-use of buff items (a Fairy skill) can use: one 9-byte
row per item with its category. The categories are the rows of
[`autousebuffitemcategoryinfo.bss`](autousebuffitemcategoryinfo_bss.md). The auto-use window
(`panel_window_autousebuffitem_1.luac`) walks
`ToClient_getAutoUseBuffItemCategoryCount()` and
`ToClient_getAutoUseBuffItemCategoryKey(index)`, names each category with
`ToClient_getAutoUseBuffItemCategoryStaticStatusWrapper(categoryKey):getCategoryName()`
and lists its items with
`ToClient_getAutoUseBuffItemElement(categoryKey, buffCategory, index)`,
whose `getItemKey()` is the item.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 2637 and later | 3483    | `buffitemautousestaticstatus.bss` | 8,228 | 912 Row | 9         |
| 1      | 2107 to 2519   | 2519    | `buffitemautousestaticstatus.bss` | 4,980 | 620 Row | 8         |

| Layout | File                              | Known            | Unknown       |
| ------ | --------------------------------- | ---------------- | ------------- |
| 2      | `buffitemautousestaticstatus.bss` | 7,316 B (88.9%)  | 912 B (11.1%) |
| 1      | `buffitemautousestaticstatus.bss` | 4,980 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2637   | Layout 2 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
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

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed, in no key order         |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (9 bytes)

| Offset  | Type | Field        | Notes                                                                      |
| ------- | ---- | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32  | category_key | The `autousebuffitemcategoryinfo.bss` category; see Categories             |
| `+0x04` | u32  | item_key     | The item (LOC type 0 name); unique per row, top byte `0` on every row      |
| `+0x08` | u8   | unknown_08   | `1` on 892 of 912 rows (client 3482); see Open Questions                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                              |
| ------- | ------------------ | ------------ | ---------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                              |

## Layout 1

No `unknown_08`: a row is 8 bytes. Only the Row differs from Layout 2.

### Row (8 bytes)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u32  | category_key |       |
| `+0x04` | u32  | item_key     |       |

## Categories

`autousebuffitemcategoryinfo.bss` holds the nine category keys `1` to `9`,
each with a Korean name in its string table and an English name in LOC
type 118. Every `category_key` of this file is one of them, and the items
of each key fit its name. Counts are from client 3482.

| `category_key` | Korean name (`autousebuffitemcategoryinfo.bss`) | Items | Examples                                       |
| -------------- | ----------------------------------------------- | ----- | ---------------------------------------------- |
| 1              | `크론 정식 /음식` (Cron Meal / food)            | 270   | Crispy Stir-Fried Vegetables, Savory Sungnyung |
| 2              | `영약 / 비약` (draughts / elixirs)              | 263   | [Party] Merciless Sky Elixir                   |
| 3              | `향수` (perfumes)                               | 36    | Perfume of Charm                               |
| 4              | `별채 주문서` (annex scrolls)                   | 2     | [Scroll] Turning Gates, [Scroll] Body Enhancement |
| 5              | `모험의 가호 주문서` (adventure boon scroll)    | 1     | [Scroll] Adventure's Boon                      |
| 6              | `영물의 축복` (mystic beast blessings)          | 6     | Blessing of Mystic Beasts - All AP             |
| 7              | `황금 축복` (golden blessings)                  | 8     | [Event] Golden Blessing of Agris               |
| 8              | `주문서` (scrolls)                              | 107   | Max HP Increase Scroll, Mercenary's Skill (60 min) |
| 9              | `기타` (other)                                  | 219   | [Event] Pineapple Skewer                       |

## Open Questions

### What `unknown_08` Holds

`unknown_08` is `1` on 892 rows, `15` on the ten Harmony Draughts (item
keys `1399` to `1408`) and `4` on the ten Draughts `1389` to `1398`
(Fury, Adaptation, Potential, Corruption, Berserk and their Immortal
versions) on client 3482. The window groups each category's items by a
`buffCategory` (`ToClient_getAutoUseBuffItemBuffCategory(categoryKey,
groupIndex)`), which could be this byte or come from the item's buff.
