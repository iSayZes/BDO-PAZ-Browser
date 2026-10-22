# `tax.bss` Format

## Purpose

The tax bounds of each territory: for each of eight tax types, a minimum
and a maximum rate or price and a system rate.
One 100-byte row per territory; client 3482 has 14 rows, territory keys
`13` down to `0`, all with the same values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File      | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | --------- | ----- | --------------- | --------- |
| 1      | 1230 and later | 3482    | `tax.bss` | 1,420 | 112 Tax, 14 Row | 12        |

| Layout | File      | Known            | Unknown    |
| ------ | --------- | ---------------- | ---------- |
| 1      | `tax.bss` | 1,420 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2519   | Layout 1             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | Layout 1             |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (100 bytes)

| Offset  | Type   | Field             | Notes                                                                 |
| ------- | ------ | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | i16    | territory_key     | `territoryinfo.bss` key, LOC type 12 name; the key the table is read by |
| `+0x02` | i16    | territory_key_dup | Equals `territory_key` on every row; the 2016 struct's `_key`         |
| `+0x04` | Tax[8] | taxes             | One per tax type, in `TaxType` order; see Tax Types                   |

### Tax (12 bytes)

| Offset  | Type | Field                | Notes                                                     |
| ------- | ---- | -------------------- | --------------------------------------------------------- |
| `+0x00` | i32  | min_percent_or_price | `0` on every row of client 3482                           |
| `+0x04` | i32  | max_percent_or_price | `100000`, or `500` for tax type 4                         |
| `+0x08` | i32  | system_percent       | `0`, `200`, `250000` or `300000` by tax type              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Tax Types

The index of a `Tax` in `taxes`. Names 0 to 5 are `CppEnums.TaxType` in
`global_define_cpp_enum.luac` (client 3482), which ends with
`eTaxType_Count = 6`; 6 and 7 come from the 2016 `gc::TaxType`, which has
eight types and calls 1 `eTaxTypeBuyItemFromConsignment`. The values are
those of every territory on client 3482.

| Index | Name                          | `min_percent_or_price` | `max_percent_or_price` | `system_percent` |
| ----- | ----------------------------- | ---------------------- | ---------------------- | ---------------- |
| 0     | `eTaxType_BuyItemFromSystem`  | 0                      | 100000                 | 0                |
| 1     | `eTaxType_ReserveTemp`        | 0                      | 100000                 | 0                |
| 2     | `eTaxType_BuyHorseFromServantMarket` | 0               | 100000                 | 300000           |
| 3     | `eTaxType_BuyHorseFromServantMating` | 0               | 100000                 | 300000           |
| 4     | `eTaxType_DeliverItemByPublicWagon`  | 0               | 500                    | 200              |
| 5     | `eTaxTypeSellItemToItemMarket`       | 0               | 100000                 | 0                |
| 6     | `eTaxTypeSellWorkerToMarket` (2016)  | 0               | 100000                 | 300000           |
| 7     | `eTaxTypeSellPetInAuction` (2016)    | 0               | 100000                 | 250000           |

## Field Names

The 2016 `gc::TaxStaticStatus` (100 bytes) holds `gc::KeyType<short, -1>
_key`, two bytes of padding and `pa::Array<gc::TaxStaticStatus::value, 8>
_tax`; each `value` is `int _minPercentOrPrice`, `int _maxPercentOrPrice`
and `int _systemPercent`. The file packs the key the table is read by,
then `_key` in place of the padding, then the eight values.

The `Tax` sheet of a private server's `DataSheets.bexcel` on client 1784
has the columns `TerritoryKey`, `TaxType`, `MinPercentOrPrice`,
`MaxPercentOrPrice` and `SystemPercent`, one row per territory and tax
type. Its 80 rows (territories `0` to `9`, types `0` to `7`) match the
80 values of the client 1784 file (10 rows) by territory, type and value.

## Notes

- Client 1784 holds 10 rows (territories `9` down to `0`) with the same
  values; client 3482 adds territories `10` to `13`.
- The scale of the rates is not confirmed; the Lua reads the lord's set
  rate with `getTaxRateForFortress` and does not read this file.
- The tax handler (`_bss/tax/`) shows one row per territory and tax type,
  with the territory name and the tax type name.
