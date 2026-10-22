# `cashproductcategory.dbss` Format

## Purpose

The Pearl Shop category tree: the main categories (the shop tabs), their
middle categories and the small categories under those, each with its
Korean name, price type, tag and the unique number coupons and products
point at. The Pearl Shop Lua (`panel_pearlshop_category.luac`,
`panel_ingamecashshop.luac`) reads a main category through
`ToClient_GetMainCategoryStaticStatusWrapperByKeyRaw(key)` and the names
through `getCashCategoryName(main, middle)`; the main keys are
`CppEnums.CashProductCategory` (`1` Pearl, `2` Mileage, `3` Normal, `4`
Costumes, `5` Furniture, `6` Servant, `7` Pet, `8` Beauty, `9` HotNew, `15`
StepUp). [`coupon.dbss`](coupon_dbss.md) names its category by these keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records       | Row bytes                   |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------- | --------------------------- |
| 1      | 1348 and later | 3482    | `cashproductcategory.dbss`       | 6,579 | 135 Category  | 34 to 1,976, 118 on average |
| 1      | 1348 and later | 3482    | `cashproductcategoryoffset.dbss` | 170   | 15 Offset Row | 10                          |

| Layout | File                             | Known           | Unknown         |
| ------ | -------------------------------- | --------------- | --------------- |
| 1      | `cashproductcategory.dbss`       | 5,359 B (81.5%) | 1,220 B (18.5%) |
| 1      | `cashproductcategoryoffset.dbss` | 170 B (100.0%)  | 0 B (0.0%)      |

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

| File                             | Required | Role                                                                                      |
| -------------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `cashproductcategoryoffset.dbss` | Optional | `main_key -> (data_offset, data_size)` of every main category; the parser walks the main file without it |
| `languagedata_en.loc`            | Optional | Category names, LOC type 51                                                               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic. The name of the all-categories entry, then the main
categories, each followed by its children.

| Offset             | Type            | Field                  | Notes                                                                  |
| ------------------ | --------------- | ---------------------- | ---------------------------------------------------------------------- |
| `+0x00`            | str16           | all_name_kr            | `전체(펄 상자, 마일리지 제외)` (all, Pearl Box and Mileage excluded); see Notes |
| `all_name_kr+0x00` | u32             | unknown_all_name_kr_00 | `0` on clients 1784 and 3482                                           |
| `all_name_kr+0x04` | u8              | unknown_all_name_kr_04 | `1` on clients 1784 and 3482                                           |
| `all_name_kr+0x05` | u32             | count                  | Number of main categories, `15` on client 3482                         |
| `all_name_kr+0x09` | Category[count] | categories             | See Category                                                           |

### Category (variable: 32 bytes + name and children)

One category; its children follow inside it. A main category's children
are middle categories, theirs small categories; no small category of
clients 1784 and 3482 has children.

| Offset          | Type                  | Field                 | Notes                                                                                        |
| --------------- | --------------------- | --------------------- | -------------------------------------------------------------------------------------------- |
| `+0x00`         | u16                   | category_key          | Main key (`CppEnums.CashProductCategory`), else the key under the parent, from `1`          |
| `+0x02`         | str16                 | name_kr               | Korean name; main names start with a space, `\n` (two characters) breaks a line              |
| `name_kr+0x00`  | u8                    | is_useable            | `0` on main categories `1` and `13` of client 3482, `1` on the other 133 categories          |
| `name_kr+0x01`  | u8                    | price_type            | See Price Types                                                                              |
| `name_kr+0x02`  | u8                    | special_category_type | `2` on main 5 (Furniture) and its seven children and on Step Up 1 to 10, `3` on the appearance change coupons (8, 2), `1` on Hot&New Special (9, 7), else `0` (client 3482) |
| `name_kr+0x03`  | u8                    | tag_type              | Hot&New tag: `1` New, `2` Hot, `3` Event, `4` Sale, `5` Best, `7` Special, `8` to `17` Step Up 1 to 10; `0` elsewhere |
| `name_kr+0x04`  | u8                    | tag_order             | Order of the tag, `1` to `7`; `0` where `tag_type` is `0`                                    |
| `name_kr+0x05`  | bytes[3]              | unknown_name_kr_05    | `0` on every category of clients 1784 and 3482                                               |
| `name_kr+0x08`  | u32                   | unique_no             | Unique number of the category, `1` to `999` on client 3482                                   |
| `name_kr+0x0C`  | u32                   | child_count           | Number of `children`                                                                         |
| `name_kr+0x10`  | Category[child_count] | children              | The categories one level down                                                                |
| `children+0x00` | u16                   | unknown_children_00   | `65535` on every category of clients 1784 and 3482                                           |
| `children+0x02` | u32                   | unknown_children_02   | `0` on every category                                                                        |

On client 3482 the file holds 15 main, 54 middle and 66 small categories.

### `cashproductcategoryoffset.dbss`

The `PABR` index layout of `characterstaticoffset.dbss`, read by
`parse_pabr_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                          |
| ----------- | ----------------- | ------------ | ---------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                         |
| `+0x04`     | u32               | count        | Equals the main category count                 |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                                 |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table               |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 10 * count`)             |
| `rows+0x08` | u32               | zero         | Always `0`                                     |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                       |
| ------- | ---- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u16  | main_key    | `category_key` of the main category it points at            |
| `+0x02` | u32  | data_offset | Absolute offset of that main category, at its `category_key` |
| `+0x06` | u32  | data_size   | The main category with all its children                     |

On clients 1784 and 3482 the index rows follow the file order and every
one points at the main category with its key.

## Price Types

`price_type` against the `PriceType` text of the client 1784 sheet (see
Field Names), 88 of 88 categories. The Lua knows the same four as
`__ePriceType_Cash`, `__ePriceType_Pearl`, `__ePriceType_Mileage` and
`__ePriceType_Sliver`.

| Value | Sheet `PriceType` | Categories (client 3482)                      |
| ----- | ----------------- | --------------------------------------------- |
| 0     | `Silver`          | Silver Event Items (main 2, middle 2)          |
| 1     | `Cash`            | Pearl Box (main 1)                             |
| 2     | `Pearl`           | The other 132                                  |
| 3     | `Mileage`         | Loyalties (main 2, middle 1)                   |

## LOC Names

LOC type 51 holds each category's name under `(main, middle, small)`: a
main category writes middle `65535` and small `255`, a middle category
small `255`. All 135 categories of client 3482 have an English name. The
key `(99, 65535, 255)` names the all-categories entry of the file head
(`All (Except for Pearl, Loyalty)`). Older rows with middle or small `0`
(`(1, 0, 0)` `Pearl Box`) are not used by the file.

## Field Names

The `CouponCategory_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CashCouponCategory_Main`, `_Middle` and
`_Small` (the path), `IsUseable`, `MoneyType`, `PriceType`, `TagType`,
`TagOrder`, `specialCategoryType`, `CashCouponCategory_Name`, `UniqueNo` and
`IsHighLightCategory`, 89 rows. 88 of them are the categories of the client
1784 file; row `99` (`UniqueNo` 70) has the text of `all_name_kr`.

| Field                 | Column                    | Same value (client 1784) | Same value (client 3482) |
| --------------------- | ------------------------- | ------------------------ | ------------------------ |
| category_key          | the path columns          | 88 of 88                 | 83 of 88                 |
| name_kr               | `CashCouponCategory_Name` | 88 of 88                 | 71 of 83                 |
| is_useable            | `IsUseable`               | 88 of 88                 | 82 of 83                 |
| price_type            | `PriceType`               | 88 of 88                 | 82 of 83                 |
| special_category_type | `specialCategoryType`     | 88 of 88                 | 82 of 83                 |
| tag_type              | `TagType`                 | 88 of 88                 | 83 of 83                 |
| tag_order             | `TagOrder`                | 88 of 88                 | 79 of 83                 |
| unique_no             | `UniqueNo`                | 88 of 88                 | 83 of 83                 |

Client 3482 renames 12 of the 83 shared categories, turns main 2 into
`마일리지/\n 은화 상품` with two middle categories (Mileage and the Silver
event items, which the sheet keeps under main 10) and moves the Hot&New
tag orders up by one for Step Up. `MoneyType` (`0` Cash, `1` Pearl, `2`
Mileage, `3` Silver) names the same four in another order, so
`price_type` matches it as well; no other byte holds it.

## Notes

- The name of the all-categories entry is the coupon category text of a
  coupon valid in every category: [`coupon.dbss`](coupon_dbss.md) stores it
  as `category_expression_kr` of 52 of its 117 coupons on client 3482.

## Open Questions

### What the Zero and 65535 Fields Hold

`unknown_name_kr_05` is `0` on every category of clients 1784 and 3482,
`unknown_children_00` `65535` and `unknown_children_02` `0`. The sheet's
`IsHighLightCategory` is `0` on all 89 rows, so it may be one of the zero
bytes; no value differs to confirm it.

### What the Head Fields Hold

`unknown_all_name_kr_00` (`0`) and `unknown_all_name_kr_04` (`1`) follow
the all-categories name on clients 1784 and 3482. They may be the
`is_useable` and other flags of that entry in another order, which a
client with other values would show.
