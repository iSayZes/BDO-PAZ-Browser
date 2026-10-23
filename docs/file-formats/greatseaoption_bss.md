# `greatseaoption.bss` Format

## Purpose

One record of Great Ocean and island barter options: food use, the
explore cooldown, the ship management and barter ranges, barter exchange
and reset counts, discount values and two EXP values. The fields are the
client side of the `IslandExplore_Option` sheet (see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | -------------- | --------- |
| 4      | 2736 and later | 3482    | `greatseaoption.bss` | 88    | 1 String Table | 4         |
| 3      | 1316 to 2703   | 2703    | `greatseaoption.bss` | 86    | 1 String Table | 4         |
| 2      | 1309           | 1309    | `greatseaoption.bss` | 82    | 1 String Table | 4         |
| 1      | 1286           | 1286    | `greatseaoption.bss` | 54    | 1 String Table | 4         |

| Layout | File                 | Known        | Unknown      |
| ------ | -------------------- | ------------ | ------------ |
| 4      | `greatseaoption.bss` | 75 B (85.2%) | 13 B (14.8%) |
| 3      | `greatseaoption.bss` | 73 B (84.9%) | 13 B (15.1%) |
| 2      | `greatseaoption.bss` | 73 B (89.0%) | 9 B (11.0%)  |
| 1      | `greatseaoption.bss` | 53 B (98.1%) | 1 B (1.9%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 4             |
| 3474   | Layout 4             |
| 3454   | Layout 4             |
| 3412   | Layout 4             |
| 3381   | Layout 4             |
| 3349   | Layout 4             |
| 3314   | Layout 4             |
| 3283   | Layout 4             |
| 3251   | Layout 4             |
| 3212   | Layout 4             |
| 3177   | Layout 4             |
| 3144   | Layout 4             |
| 3103   | Layout 4             |
| 3062   | Layout 4             |
| 3037   | Layout 4             |
| 3002   | Layout 4             |
| 2959   | Layout 4             |
| 2923   | Layout 4             |
| 2900   | Layout 4             |
| 2872   | Layout 4             |
| 2834   | Layout 4             |
| 2803   | Layout 4             |
| 2765   | Layout 4             |
| 2736   | Layout 4             |
| 2703   | Layout 3             |
| 2665   | Layout 3             |
| 2637   | Layout 3             |
| 2606   | Layout 3             |
| 2583   | Layout 3             |
| 2545   | Layout 3             |
| 2519   | Layout 3             |
| 2498   | Layout 3             |
| 2468   | Layout 3             |
| 2438   | Layout 3             |
| 2414   | Layout 3             |
| 2384   | Layout 3             |
| 2358   | Layout 3             |
| 2335   | Layout 3             |
| 2313   | Layout 3             |
| 2290   | Layout 3             |
| 2250   | Layout 3             |
| 2224   | Layout 3             |
| 2203   | Layout 3             |
| 2179   | Layout 3             |
| 2151   | Layout 3             |
| 2134   | Layout 3             |
| 2107   | Layout 3             |
| 2073   | Layout 3             |
| 2052   | Layout 3             |
| 2011   | Layout 3             |
| 1996   | Layout 3             |
| 1969   | Layout 3             |
| 1937   | Layout 3             |
| 1914   | Layout 3             |
| 1886   | Layout 3             |
| 1866   | Layout 3             |
| 1838   | Layout 3             |
| 1818   | Layout 3             |
| 1794   | Layout 3             |
| 1784   | Layout 3             |
| 1749   | Layout 3             |
| 1717   | Layout 3             |
| 1698   | Layout 3             |
| 1674   | Layout 3             |
| 1636   | Layout 3             |
| 1608   | Layout 3             |
| 1587   | Layout 3             |
| 1565   | Layout 3             |
| 1537   | Layout 3             |
| 1509   | Layout 3             |
| 1485   | Layout 3             |
| 1466   | Layout 3             |
| 1445   | Layout 3             |
| 1426   | Layout 3             |
| 1409   | Layout 3             |
| 1390   | Layout 3             |
| 1372   | Layout 3             |
| 1360   | Layout 3             |
| 1348   | Layout 3             |
| 1338   | Layout 3             |
| 1324   | Layout 3             |
| 1316   | Layout 3             |
| 1309   | Layout 2             |
| 1286   | Layout 1             |
| 1256   | No documented layout |
| 1230   | No file              |
| 1211   | No file              |
| 1194   | No file              |
| 1177   | No file              |
| 1156   | No file              |
| 1127   | No file              |
| 1109   | No file              |
| 1076   | No file              |
| 1058   | No file              |
| 1016   | No file              |
| 990    | No file              |
| 955    | No file              |
| 911    | No file              |
| 885    | No file              |
| 855    | No file              |
| 822    | No file              |
| 794    | No file              |
| 748    | No file              |
| 711    | No file              |
| 683    | No file              |
| 656    | No file              |
| 630    | No file              |
| 606    | No file              |
| 577    | No file              |
| 542    | No file              |
| 526    | No file              |
| 508    | No file              |
| 485    | No file              |
| 457    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type         | Field                 | Notes                                                               |
| ------------------- | ------------ | --------------------- | ------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                                                        |
| `+0x04`             | u32          | food_consume          | `100000` on clients 1784 and 3482                                   |
| `+0x08`             | u32          | explore_cool_time     | `1200` on clients 1784 and 3482                                     |
| `+0x0C`             | f32          | ship_management_range | `15000` on client 1784, `20000` on client 3482                      |
| `+0x10`             | f32          | barter_range          | `5000` on clients 1784 and 3482                                     |
| `+0x14`             | u8           | reset_cool_time       | `4` on client 1784, `2` on client 3482                              |
| `+0x15`             | u8           | unknown_15            | `0` on every client checked                                         |
| `+0x16`             | u32          | max_exchange_count    | `1000000` on clients 1784 and 3482                                  |
| `+0x1A`             | u32          | over_max_count        | `1000000` on clients 1784 and 3482                                  |
| `+0x1E`             | u32          | max_reset_count       | `100` on clients 1784 and 3482                                      |
| `+0x22`             | u16          | barter_reset_time     | `6` on client 3482                                                  |
| `+0x24`             | u32          | discount_rate         | `100000` on clients 1784 and 3482                                   |
| `+0x28`             | u32          | add_reset_count       | `50` on clients 1784 and 3482                                       |
| `+0x2C`             | u32          | reset_need_count      | `30` on clients 1784 and 3482                                       |
| `+0x30`             | u32          | time_discount         | `10000` on clients 1784 and 3482                                    |
| `+0x34`             | u32          | time_discount_limit   | `50000` on clients 1784 and 3482                                    |
| `+0x38`             | u32          | sub_employee_exp      | `20` on clients 1784 and 3482                                       |
| `+0x3C`             | u32          | unknown_3c            | `0` on every client checked                                         |
| `+0x40`             | u32          | sub_trade_exp         | `499` on clients 1784 and 3482                                      |
| `+0x44`             | u32          | unknown_44            | `0` on every client checked                                         |
| `+0x48`             | u32          | unknown_48            | `500000` on every client checked; see Open Questions                |
| `+0x4C`             | String Table | string_table          | See String Table                                                    |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4C`                                  |
| `string_table+0x04` | u32          | zero                  | Always `0`                                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 3

No `barter_reset_time`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | u32          | reset_need_count      |                                    |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | u32          | unknown_48            |                                    |
| `+0x4A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 2

No `unknown_48`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       | `3` on client 1309                 |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       | `1` on client 1309                 |
| `+0x2A`             | u32          | reset_need_count      | `1` on client 1309                 |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x46` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 1

The values end after `add_reset_count`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x2A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Field Names

The `IslandExplore_Option` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 24 columns and one row. The client
1784 file holds 19 values; 15 of them are sheet values, in close to sheet
order: `FoodConsume` (`100000`), `ExploreCoolTime` (`1200`),
`ShipManagementRange` (`15000`), `BarterRange` (`5000`), `ResetCoolTime`
(`4`), `MaxExchangeCount` and `OverMaxCount` (both `1000000`),
`MaxResetCount` (`100`), `DiscountRate` (`100000`), `AddResetCount`
(`50`), `ResetNeedCount` (`30`), `TimeDiscount` (`10000`),
`TimeDiscountLimit` (`50000`), `SubEmployeeExp` (`20`) and `SubTradeExp`
(`499`). `BarterResetTime` is `6` in that sheet and absent from the client
1784 file; Layout 4 adds a u16 `6` at `+0x22`, the only sheet column with
that value.

Three pairs share one value, so the sheet's column order decides:
`FoodConsume` and `DiscountRate` (`100000`), `MaxExchangeCount` and
`OverMaxCount` (`1000000`), and `BarterRange` and
`SpecialBarterInvokationCost` (`5000`), where the f32 type, the same as
`ShipManagementRange`, picks the range. That server's dump holds the
sheet's column names as UTF-16 strings in this order: `FoodConsume`, `ExploreCoolTime`,
`ShipManagementRange`, `VoyageExploreCoolTime`,
`SpecialBarterInvokationCost`, `BarterRange`, `MaxExchangeCount`,
`ResetCoolTime`, `MaxResetCount`, `OverMaxCount`, `AddResetCount`,
`BarterResetTime`, `TimeDiscount`, `ResetNeedCount`, `SubTradeExp`,
`TimeDiscountLimit`, then `KamasylveDiscount`, `SubEmployeeExp`,
`OceanPenaltyMin`, `OceanPenaltyRate` and `OceanPenaltyMax`.

The sheet's `VoyageExploreCoolTime` (`300`), `ResetBarter` (`45504`),
`SpecialBarterInvokationCost`, `ShipMoveEmployeeExp` (`1`) and the three
`OceanPenalty` columns (`1`, `1`, `500000`) have no other match in the
file.

## Notes

- Client 1286 holds Layout 1 (54 bytes), client 1309 Layout 2 (82
  bytes), clients 1316 to 2703 Layout 3 (86 bytes) and clients 2736 to
  3482 Layout 4 (88 bytes). Between them `reset_cool_time` drops from
  `4` to `2` (client 2519) and `ship_management_range` rises from `15000`
  to `20000` (client 3474).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`: one
  row with every named field. It reads Layout 4 only.

## Open Questions

### The Client 1256 Record

Client 1256 holds a 42-byte file: `food_consume`, `explore_cool_time`,
`ship_management_range`, an f32 `8000`, a u8 `4`, a u8 `0` and two u32
(`100`, then `1000000`), 26 bytes of values. Which of the later fields
the last two are is open, so no layout covers that client.

### The Value After `sub_trade_exp`

`unknown_48` is `500000`, the value of two sheet columns,
`KamasylveDiscount` and `OceanPenaltyRate`, so the value alone does not
name it. The column strings put `KamasylveDiscount` next to
`SubEmployeeExp`, but the file stores `sub_trade_exp` between them.

### The Zero Fields

`unknown_15`, `unknown_3c` and `unknown_44` are `0` on every client
checked. No column of the sheet is `0`; `ShipMoveEmployeeExp`,
`OceanPenaltyMin` and `OceanPenaltyMax` are `1` there and may read `0` in
the client build.
