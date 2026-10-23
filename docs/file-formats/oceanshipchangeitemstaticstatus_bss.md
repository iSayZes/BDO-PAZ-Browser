# `oceanshipchangeitemstaticstatus.bss` Format

## Purpose

The ships a wharf can turn back into their Ship License item, and the
silver fee for it. On client 3482 the five rows are the Epheria Carrack
and its four upgraded forms, each with its own license. The servant list
offers the change only for a ship of `CppEnums.VehicleType.Type_Carrack`
that `ToClient_oceanShipChangeItemPossible(characterKey)` accepts
(`panel_dialog_servantlist_all_1.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------- | ----- | ------- | --------- |
| 1      | 2703 and later | 3482    | `oceanshipchangeitemstaticstatus.bss` | 54    | 5 Row   | 6         |

| Layout | File                                  | Known         | Unknown    |
| ------ | ------------------------------------- | ------------- | ---------- |
| 1      | `oceanshipchangeitemstaticstatus.bss` | 54 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | No file  |
| 2637   | No file  |
| 2606   | No file  |
| 2583   | No file  |
| 2545   | No file  |
| 2519   | No file  |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the ship (LOC type 6) and the item (LOC type 0)
from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                                                 |
| ------------------- | -------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                          |
| `+0x04`             | u32            | fee_money    | Silver fee of the change; `100000000` on client 3482                  |
| `+0x08`             | u32            | row_count    | Number of rows                                                        |
| `+0x0C`             | Row[row_count] | rows         | See Row; byte-packed                                                  |
| `rows+0x00`         | String Table   | string_table | See String Table                                                      |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends                         |
| `string_table+0x04` | u32            | zero         | Always `0`                                                            |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The ship's character key (LOC type 6); unique per row                  |
| `+0x02` | u32  | item_id       | The Ship License the ship turns into (LOC type 0); unique per row      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order.

| `character_key` | Ship                     | `item_id` | Item                                    |
| --------------- | ------------------------ | --------- | --------------------------------------- |
| 31045           | Epheria Carrack          | 49021     | Ship License: Epheria Carrack           |
| 31054           | Epheria Carrack: Advance | 49029     | Ship License: Epheria Carrack - Advance |
| 31055           | Epheria Carrack: Balance | 49030     | Ship License: Epheria Carrack - Balance |
| 31056           | Epheria Carrack: Volante | 49031     | Ship License: Epheria Carrack - Volante |
| 31057           | Epheria Carrack: Valor   | 49032     | Ship License: Epheria Carrack - Valor   |

## Field Names

The file is newer than client 1784, and no sheet or column name of a
private server's `DataSheets.bexcel` on that client contains
`ShipChange`. The names come from the client Lua
(`panel_dialog_servantlist_all_2.luac`, client 3482): the confirm box
shows `makeDotMoney(ToClient_oceanShipChangeItemFeeMoney())` as the
`needSilver` of `LUA_OCEAN_SHIP_TRADE_ITEM_02`, so the value stored once
before the rows is `fee_money`. `character_key` resolves to the ship's
LOC type 6 name and `item_id` to the matching Ship License on every row.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`: the
  ship and its license with names and icon, and the fee on every row.
