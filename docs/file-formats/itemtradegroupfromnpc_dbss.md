# `itemtradegroupfromnpc.dbss` Format

## Purpose

Item groups per NPC, the counterpart by name of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md). On client 3473
the file holds no records: it is a u32 count of `0`, and so is its offset
file. On client 1784 it holds 125 groups of item entries with a trade
category, keyed by character key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes  | Records                   | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------------- | ------ | ------------------------- | -------------------------- |
| 2      | 2519 and later | 3474    | `itemtradegroupfromnpc.dbss`       | 4      | -                         | -                          |
| 2      | 2519 and later | 3474    | `itemtradegroupfromnpcoffset.dbss` | 4      | -                         | -                          |
| 1      | 1485 to 2107   | 2107    | `itemtradegroupfromnpc.dbss`       | 69,376 | 462 Item Entry, 129 Group | 123 to 159, 148 on average |
| 1      | 1485 to 2107   | 2107    | `itemtradegroupfromnpcoffset.dbss` | 1,294  | 129 Index Row             | 10                         |

| Layout | File                               | Known             | Unknown    |
| ------ | ---------------------------------- | ----------------- | ---------- |
| 2      | `itemtradegroupfromnpc.dbss`       | 4 B (100.0%)      | 0 B (0.0%) |
| 2      | `itemtradegroupfromnpcoffset.dbss` | 4 B (100.0%)      | 0 B (0.0%) |
| 1      | `itemtradegroupfromnpc.dbss`       | 69,376 B (100.0%) | 0 B (0.0%) |
| 1      | `itemtradegroupfromnpcoffset.dbss` | 1,294 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. `itemtradegroupfromnpcoffset.dbss` is the offset file of this table;
the PAZ Browser reads both with the Layout 1 groups and the
`itemtradegrouptonpc.dbss` columns, so client 3473 shows an empty table and
client 1784 its 451 item entries.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                |
| ------- | ---- | ----- | ------------------------------------ |
| `+0x00` | u32  | count | Number of groups; `0` on client 3473 |

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type | Field | Notes                                         |
| ------- | ---- | ----- | --------------------------------------------- |
| `+0x00` | u32  | count | Equals the `itemtradegroupfromnpc.dbss` count |

## Layout 1

The structures below match the Layout 1 structures of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md#layout-1): groups
of item entries that open with a counted condition string.

### File Layout

| Offset  | Type         | Field  | Notes                |
| ------- | ------------ | ------ | -------------------- |
| `+0x00` | u32          | count  | `125` on client 1784 |
| `+0x04` | Group[count] | groups | See Group            |

### Group (variable: 6 bytes + item entries)

| Offset  | Type                   | Field        | Notes                       |
| ------- | ---------------------- | ------------ | --------------------------- |
| `+0x00` | u16                    | character_id | Character key, LOC type `6` |
| `+0x02` | u32                    | item_count   | Number of item entries      |
| `+0x06` | Item Entry[item_count] | entries      | See Item Entry              |

### Item Entry (variable: 123 bytes + condition text)

The fields after the condition are the members of the
[`itemtradegrouptonpc.dbss` Layout 1](itemtradegrouptonpc_dbss.md#layout-1)
entry, which the server reads with the same row reader; see Field Names.
Counts are from client 1784.

| Offset           | Type  | Field                            | Notes                                                                 |
| ---------------- | ----- | -------------------------------- | --------------------------------------------------------------------- |
| `+0x00`          | u16   | character_id                     | Repeats the group key                                                 |
| `+0x02`          | u32   | item_id                          | Item key, LOC type `0`                                                |
| `+0x06`          | str16 | condition                        | Empty, or a condition such as `getlifeLevel(7)>41`; 316 of the 451 entries hold one |
| `condition+0x00` | i32   | max_price_rate                   | `0` in every entry, as is every field up to `trade_group_type`        |
| `condition+0x04` | i32   | event_max_price_rate             |                                                                       |
| `condition+0x08` | i32   | min_price_rate                   |                                                                       |
| `condition+0x0C` | i32   | steady_price_rate                |                                                                       |
| `condition+0x10` | i32   | vary_amount_rate_per_sell_or_buy |                                                                       |
| `condition+0x14` | i32   | vary_amount_rate_per_tick        |                                                                       |
| `condition+0x18` | i32   | event_price_rate_per_tick        |                                                                       |
| `condition+0x1C` | i32   | price_maintain_tick              |                                                                       |
| `condition+0x20` | i64   | steady_price_tick_count          |                                                                       |
| `condition+0x28` | u8    | trade_group_type                 | `0` in every entry                                                    |
| `condition+0x29` | u8    | is_sell_to_npc                   | `0` in every entry; `1` in every `itemtradegrouptonpc.dbss` entry     |
| `condition+0x2A` | i64   | min_price                        | `0` in every entry, as is every field up to `territory_supply_no`     |
| `condition+0x32` | i64   | max_price                        |                                                                       |
| `condition+0x3A` | i64   | buyable_stock_amount_per_tick    |                                                                       |
| `condition+0x42` | i32   | intimacy_variation               |                                                                       |
| `condition+0x46` | u8    | is_individual                    |                                                                       |
| `condition+0x47` | i16   | exploration_point                |                                                                       |
| `condition+0x49` | i32   | get_exp_rate                     |                                                                       |
| `condition+0x4D` | i64   | min_stock_amount                 |                                                                       |
| `condition+0x55` | i64   | max_stock_amount                 |                                                                       |
| `condition+0x5D` | u16   | territory_supply_no              |                                                                       |
| `condition+0x5F` | u16   | territory_trade_no               | Non-zero on 60 entries, such as `301` to `303`                        |
| `condition+0x61` | i32   | get_selling_trade_exp_rate       | `1000000` in every entry                                              |
| `condition+0x65` | i32   | event_price_rate_per_sell        | `0` in every entry                                                    |
| `condition+0x69` | u8    | is_for_magnate                   | `1` on 14 entries                                                     |
| `condition+0x6A` | u8    | trade_type                       | `0`, `1` or `2`                                                       |
| `condition+0x6B` | u8    | commerce_type                    | `1` to `9`                                                            |
| `condition+0x6C` | u8    | price_type                       | `0` in every entry                                                    |

Earlier versions of this doc called `condition` `unknown_condition`, the
members up to `trade_group_type` `unknown_condition_00`, `is_sell_to_npc`
`unknown_37`, the members up to `territory_supply_no` `unknown_38`,
`territory_supply_no` `unknown_6b`, the four members from
`territory_trade_no` to `is_for_magnate` `unknown_6d`, `trade_type`
`unknown_7c` and `price_type` `unknown_7e`.

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtradegroupfromnpc.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                 |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                     |
| ------- | ---- | ------------ | ------------------------- |
| `+0x00` | u16  | character_id | Group key                 |
| `+0x02` | u32  | offset       | Start of the group header |
| `+0x06` | u32  | size         | Length of the whole group |

## Field Names

The server dump of a private server on client 1784 reads this file and
`itemtradegrouptonpc.dbss` into the same `ItemTradeGroupStaticStatus` rows
with the same row reader; the member list, the 2016 names and the sheet
columns are in the
[`itemtradegrouptonpc.dbss` Field Names](itemtradegrouptonpc_dbss.md#field-names).
Its sheet loader fills them for this file from `BuyingFromNpc_Table`, the
only sheet it reads `BuyableStockAmountPerTick`, `IntimacyVariation`,
`TerritoryTrade_No` and `IsForMagnate` from.

On the official client 1784 file all 451 entries are in the
`BuyingFromNpc_Table` sheet of that server's `DataSheets.bexcel` by
(`NPCKey`, `ItemKey`), and the bytes match the sheet:

- `territory_trade_no` equals `TerritoryTrade_No` on all 451, 60 of them
  non-zero, and `is_for_magnate` equals `IsForMagnate` on all 451, 14 of
  them `1`. These two place the four members after `territory_supply_no`
  by value; in `itemtradegrouptonpc.dbss`, where all four are `0`, only
  order and width place them.
- `MaxPriceRate`, `MinPriceRate`, `SteadyPriceRate`,
  `varyAmountRatePerSellOrBuy`, `varyAmountRatePerTick`,
  `PriceMaintainTick`, `SteadyPriceTickCount`,
  `BuyableStockAmountPerTick` and `IntimacyVariation` are `0` on every
  sheet row, as are their bytes.
- `is_sell_to_npc` is `0` in every entry; the loader writes `1` for
  `SellingToNpc_Table` rows only.
- `get_selling_trade_exp_rate` is `1000000` in every entry. This sheet has
  no such column, so the value is not from the sheet.
- `trade_type`, `commerce_type` and `price_type` are the item's
  `Item_Table` columns, as in `itemtradegrouptonpc.dbss`. The sheet's own
  `commerceType` column equals `commerce_type` on 341 of the 451 entries
  only, so the file does not take it from the sheet.

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would read as
the client 1784 groups or as the 127-byte Item Entry of
`itemtradegrouptonpc.dbss` Layout 2 is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.
