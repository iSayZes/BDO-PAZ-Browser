# `cashproduct_grouplist.bss` Format

## Purpose

The Pearl Shop offer groups: per offer group the
[`cashproduct.dbss`](cashproduct_dbss.md) products that share it, such as
the pieces of one outfit set or the stack sizes of one item. The Pearl Shop
Lua (`panel_ingamecashshop.luac`, `panel_pearlshop.luac`) reads a
product's group with `cashProduct:getOfferGroup()`, then the members with
`getCashProductStaticStatusGroupListCount(offerGroup)` and
`getCashProductStaticStatusGroupByIndex(offerGroup, index)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes  | Records   | Row bytes                |
| ------ | -------------- | ------- | --------------------------- | ------ | --------- | ------------------------ |
| 1      | 1348 and later | 3482    | `cashproduct_grouplist.bss` | 89,704 | 3,007 Row | 12 to 128, 30 on average |

| Layout | File                        | Known             | Unknown    |
| ------ | --------------------------- | ----------------- | ---------- |
| 1      | `cashproduct_grouplist.bss` | 89,704 B (100.0%) | 0 B (0.0%) |

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

None. The handler names each product from LOC type 50, as
[`cashproduct.dbss`](cashproduct_dbss.md) does, and links it to its
`cashproduct.dbss` row.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                       |
| ------------------- | -------------- | ------------ | ------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                |
| `+0x04`             | u32            | row_count    | Number of offer groups, `3007` on client 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row                                     |
| `rows+0x00`         | String Table   | string_table | See String Table                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                  |

### Row (variable: 8 bytes + products)

| Offset  | Type                | Field         | Notes                                                                                    |
| ------- | ------------------- | ------------- | ---------------------------------------------------------------------------------------- |
| `+0x00` | u32                 | product_count | Number of `product_nos`, `1` to `30` on client 3482                                      |
| `+0x04` | u32                 | offer_group   | The group the products share; a product number of the group on 2,832 of 3,007 rows (client 3482) |
| `+0x08` | u32[product_count]  | product_nos   | `cashproduct.dbss` product IDs; all 16,407 of client 3482 have a row there               |

The offer groups are unique and in no key order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | None                         |

## Field Names

The `CashProduct_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 gives each product an `OfferGroup`. Each of the 939 rows of the
client 1784 file is an `OfferGroup` of the sheet with the products that
name it:

| Field       | Sheet                                    | Same value (client 1784) |
| ----------- | ---------------------------------------- | ------------------------ |
| offer_group | `OfferGroup`                             | 939 of 939               |
| product_nos | `ProductNo` of the rows with that group  | 872 of 939 as a set      |

On the other 67 groups the file lists a subset of the sheet's products; 458
groups keep the sheet's row order. 359 sheet groups have no row in the
file.

## Open Questions

### Which Products Drop Out of a Group

On client 1784 the file leaves out some sheet products of 67 groups and 359
whole groups. Sale periods (`SalesStartPeriod`, `SalesEndPeriod`) or
`IsMallDisplay` may decide it; `cashproduct.dbss` does not yet expose them
to compare.
