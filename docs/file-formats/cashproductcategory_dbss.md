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
| 1      | 1286 and later | 3483    | `cashproductcategory.dbss`       | 6,579 | 135 Category  | 34 to 1,976, 118 on average |
| 1      | 1286 and later | 3483    | `cashproductcategoryoffset.dbss` | 170   | 15 Offset Row | 10                          |

| Layout | File                             | Known           | Unknown         |
| ------ | -------------------------------- | --------------- | --------------- |
| 1      | `cashproductcategory.dbss`       | 5,359 B (81.5%) | 1,220 B (18.5%) |
| 1      | `cashproductcategoryoffset.dbss` | 170 B (100.0%)  | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
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
