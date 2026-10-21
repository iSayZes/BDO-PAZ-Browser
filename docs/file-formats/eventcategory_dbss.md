# `eventcategory.dbss` Format

## Purpose

The discount events of the pearl shop's event cart
(`panel_ingamecashshop_eventcart.luac`): per event index the cash shop
category, the discount period as text, up to ten discount steps (spend at
least `discount_ceiling` pearls, get `discount_price` off), the largest
discount and the event type. The Lua reads a row with
`ToClient_GetEventCategoryStaticStatusWrapperByKeyRaw(key)` and its
`getEventSize()`, `getEventlDiscountCelling(i)`,
`getEventlDiscountPrice(i)`, `getDiscountType()`, `isSellinPeriod()` and
`isDiscountPeriod()`. On client 3474 the file holds 4 events from
2018-04-13 to 2021-08-11. Companion `eventcategoryoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ----------------------- | --------- |
| 1      | 1485 and later | 3474    | `eventcategory.dbss`       | 1,040 | 40 Discount Step, 4 Row | 16        |
| 1      | 1485 and later | 3474    | `eventcategoryoffset.dbss` | 44    | 4 Offset Row            | 10        |

| Layout | File                       | Known           | Unknown    |
| ------ | -------------------------- | --------------- | ---------- |
| 1      | `eventcategory.dbss`       | 1,032 B (99.2%) | 8 B (0.8%) |
| 1      | `eventcategoryoffset.dbss` | 44 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                 |
| -------------------------- | -------- | -------------------------------------------------------------------- |
| `eventcategoryoffset.dbss` | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 195 bytes + period text)

| Offset                          | Type              | Field                       | Notes                                                       |
| ------------------------------- | ----------------- | --------------------------- | ----------------------------------------------------------- |
| `+0x00`                         | u16               | index                       | Row key; the offset file points here                        |
| `+0x02`                         | i16               | cash_coupon_category_main   | `4` on every row of clients 1784 and 3474                   |
| `+0x04`                         | i16               | cash_coupon_category_middle | `-1` (empty) on every row                                   |
| `+0x06`                         | i16               | cash_coupon_category_small  | `-1` (empty) on every row                                   |
| `+0x08`                         | str16             | discount_start_period       | `YYYY-MM-DD HH:MM`, such as `2021-07-21 09:00`              |
| `discount_start_period+0x00`    | str16             | discount_end_period         | Same form                                                   |
| `discount_end_period+0x00`      | u8                | unknown_discount_end_period_00                  | `1` on every row; `DiscountType` or `SellInPeriod`, see Field Names |
| `discount_end_period+0x01`      | Discount Step[10] | discount_steps              | See Discount Step; unused steps are `0`                     |
| `discount_end_period+0xA1`      | u8                | unknown_discount_end_period_a1                  | `1` on every row; `DiscountType` or `SellInPeriod`, see Field Names |
| `discount_end_period+0xA2`      | i64               | max_discount_pearl          | `10000` on every row                                        |
| `discount_end_period+0xAA`      | u8                | event_type                  | `0`, or `1` on index `2`                                    |

Every row of clients 1784 and 3474 has 16 characters in each period, so
the two unknown bytes sit at row offsets `+0x58` and `+0xF9` there.

### Discount Step (16 bytes)

| Offset  | Type | Field            | Notes                                                           |
| ------- | ---- | ---------------- | --------------------------------------------------------------- |
| `+0x00` | i64  | discount_ceiling | Pearls to spend for this step, rising from step to step         |
| `+0x08` | i64  | discount_price   | The discount at this step; pearls off, or a rate for `getDiscountType()` rate events (`/ 10000` in the Lua) |

### `eventcategoryoffset.dbss`

Bare offset table into `eventcategory.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `eventcategory.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u16  | index       | Key of the row it points at                     |
| `+0x02` | u32  | data_offset | Row start, at `index`                           |
| `+0x06` | u32  | data_size   | The whole row: `259` on clients 1784 and 3474   |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. On clients
1784 and 3474 every index row points at the row with its key.

## Field Names

The names follow the `EventCategory_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784: `Index`, `CashCouponCategory_Main`,
`_Middle`, `_Small`, `DiscountStartPeriod`, `DiscountEndPeriod`,
`EventType`, `DiscountType`, `MaxDiscountPearl`, `SellInPeriod` and
`DiscountCelling0` to `9` with `DiscountPrice0` to `9` (`Celling` sic,
also in the Lua getter `getEventlDiscountCelling`). Its 4 rows match the
file on all 4 keys and every value: categories `4`, empty, empty; both
periods; `EventType` `1` only on index `2`; `MaxDiscountPearl` `10000`; the
three or five filled steps. Client 1784 and client 3474 have the same file,
byte for byte.

The client 1784 server dump (`Instance_dumpFull.exe`) reads the sheet in
the function at VA `0x1408cc5d0`: the three categories into u16 members,
`EventType` and `DiscountType` into bytes, `SellInPeriod` into a bool,
`MaxDiscountPearl` widened to an i64 and the ten steps into 20 i64. Its
row order differs from the file's, so it does not tell which of the two
bytes that are `1` on every row (`unknown_discount_end_period_00`, `unknown_discount_end_period_a1`) is
`DiscountType` and which `SellInPeriod`.

## Open Questions

### The Two Bytes After the Periods

`DiscountType` and `SellInPeriod` are both `1` on all 4 rows of the sheet,
and so are the two bytes. A row with a rate discount (the Lua's
`eEventCartDiscountType_Rate`) or one outside its sell period would tell
them apart; neither client has one.
