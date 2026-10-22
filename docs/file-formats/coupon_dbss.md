# `coupon.dbss` Format

## Purpose

The Pearl Shop discount coupons: per coupon its Korean name, how many days
it stays valid, the discount (a rate, or a Pearl amount off a minimum
price), the cap of a rate discount, the icon and the Pearl Shop category it
applies to. The coupon window Lua (`panel_ingamecashshop_coupon.luac`)
reads a held coupon through `ToClient_GetCouponInfoWrapper(index)` and the
getters `getCouponKey()`, `getCouponName()`, `getCouponDisCountRate()`,
`getCouponDisCountPearl()`, `getCouponMaxDisCountPearl()`,
`getCouponMinProductPearl()` and `getCouponCategoryExpression()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records        | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ------ | -------------- | -------------------------- |
| 1      | 1348 and later | 3482    | `coupon.dbss`       | 21,557 | 117 Row        | 155 to 239, 184 on average |
| 1      | 1348 and later | 3482    | `couponoffset.dbss` | 1,174  | 117 Offset Row | 10                         |

| Layout | File                | Known            | Unknown      |
| ------ | ------------------- | ---------------- | ------------ |
| 1      | `coupon.dbss`       | 20,972 B (97.3%) | 585 B (2.7%) |
| 1      | `couponoffset.dbss` | 1,174 B (100.0%) | 0 B (0.0%)   |

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

| File                       | Required | Role                                                                                 |
| -------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `couponoffset.dbss`        | Optional | `coupon_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`      | Optional | Coupon names (LOC type 47) and the category names (LOC type 51)                      |

The handler names the category in the loaded language from LOC type 51,
the key layout of [`cashproductcategory.dbss`](cashproductcategory_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes             |
| ------- | ---------- | ----- | ----------------- |
| `+0x00` | u32        | count | Number of coupons |
| `+0x04` | Row[count] | rows  | See Row           |

### Row (variable: 69 bytes + texts)

| Offset                        | Type  | Field                             | Notes                                                                                          |
| ----------------------------- | ----- | --------------------------------- | ---------------------------------------------------------------------------------------------- |
| `+0x00`                       | u16   | coupon_key                        | Row key; LOC type 47 `str_id1` of the name                                                     |
| `+0x02`                       | u8    | unknown_02                        | `2` on every coupon of clients 1784 and 3482                                                   |
| `+0x03`                       | u64   | max_discount_pearl                | Cap of a rate discount in Pearls, `0` for none; `1000` and `2000` on four coupons of client 3482 |
| `+0x0B`                       | u64   | min_product_pearl                 | Lowest product price a Pearl discount applies to, `0` for none                                  |
| `+0x13`                       | str16 | name_kr                           | Korean name                                                                                    |
| `name_kr+0x00`                | u32   | expiration_days                   | Days the coupon stays valid after it is given, `1` to `365` on client 3482                     |
| `name_kr+0x04`                | u32   | discount_rate                     | Discount on the 1,000,000 = 100% scale (`300000` is 30%), `0` on Pearl discount coupons        |
| `name_kr+0x08`                | u64   | discount_pearl                    | Pearls off the price, `0` on rate coupons                                                      |
| `name_kr+0x10`                | str16 | icon_path                         | Icon under `ui_texture/icon/` (`New_Icon/09_Cash/00017718.dds` on all 117 coupons of client 3482) |
| `icon_path+0x00`              | str16 | category_expression_kr            | Korean category text: the category path as `main(middle(small))`, else the all-categories name of `cashproductcategory.dbss` |
| `category_expression_kr+0x00` | u16   | category_main                     | `cashproductcategory.dbss` main key, `65535` for every category                                |
| `category_expression_kr+0x02` | u16   | category_middle                   | Middle key under it, `65535` for none                                                          |
| `category_expression_kr+0x04` | u16   | category_small                    | Small key under that, `65535` for none                                                         |
| `category_expression_kr+0x06` | u32   | unknown_category_expression_kr_06 | `0` on every coupon of clients 1784 and 3482                                                   |

On client 3482 the file holds 117 coupons; 52 apply to every category, 33
to a main category, 28 to a middle and 4 to a small one. Every category
path the coupons name is a category of `cashproductcategory.dbss` on
clients 1784 and 3482.

### `couponoffset.dbss`

Bare offset table into `coupon.dbss` (no PABR magic, no trailer), read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Equals the `coupon.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                  |
| ------- | ---- | ----------- | ------------------------------------------------------ |
| `+0x00` | u16  | coupon_key  | Key of the row it points at                            |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `coupon.dbss`, at `coupon_key` |
| `+0x06` | u32  | data_size   | The whole row                                          |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Field Names

The `Coupon_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CouponKey`, `Name`, `ExpirationDate`,
`DisCountRate`, `MaxDiscountPearl`, `MinProductPearl`, `DiscountPearl`,
`Categorys`, `CouponCategory_Main`, `CouponCategory_Middle`,
`CouponCategory_Small` and `IconPath`, 65 rows. An empty cell compares as
`0`, an empty category as `65535`.

| Field              | Column                  | Same value (client 1784) | Same value (client 3482) |
| ------------------ | ----------------------- | ------------------------ | ------------------------ |
| coupon_key         | `CouponKey`             | 65 of 65                 | 65 of 65                 |
| name_kr            | `Name`                  | 65 of 65                 | 65 of 65                 |
| expiration_days    | `ExpirationDate`        | 65 of 65                 | 65 of 65                 |
| discount_rate      | `DisCountRate`          | 65 of 65                 | 65 of 65                 |
| max_discount_pearl | `MaxDiscountPearl`      | 65 of 65                 | 65 of 65                 |
| min_product_pearl  | `MinProductPearl`       | 65 of 65                 | 65 of 65                 |
| discount_pearl     | `DiscountPearl`         | 65 of 65                 | 65 of 65                 |
| icon_path          | `IconPath`              | 65 of 65                 | 65 of 65                 |
| category_main      | `CouponCategory_Main`   | 65 of 65                 | 65 of 65                 |
| category_middle    | `CouponCategory_Middle` | 65 of 65                 | 65 of 65                 |
| category_small     | `CouponCategory_Small`  | 65 of 65                 | 65 of 65                 |

`Categorys` is empty on all 65 rows; it may be the list that
`unknown_category_expression_kr_06` counts.

## Notes

- LOC type 47 holds the coupon names under `coupon_key`: all 117 coupons of
  client 3482 have an English name (`Mount 30% DC` for `1507`).
- The category text of a coupon for every category is LOC type 51 key
  `(99, 65535, 255)`, `All (Except for Pearl, Loyalty)`; see LOC Names in
  [`cashproductcategory.dbss`](cashproductcategory_dbss.md).

## Open Questions

### What `unknown_02` Holds

The byte after the key is `2` on every coupon of clients 1784 and 3482,
rate and Pearl coupons alike, and no sheet column holds a `2`. The Lua
tells the two kinds apart with `isDisCountPearl()`, which the
`discount_pearl` field answers on its own.

### What the Trailing u32 Counts

`unknown_category_expression_kr_06` is `0` on every coupon. The empty
`Categorys` sheet column suggests a list of further categories; a coupon
with a second category would show whether it is a count.
