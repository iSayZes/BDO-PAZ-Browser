# `instancefieldranking.bss` Format

## Purpose

Which season rankings each instance field type shows on the client's
service: per instance field type a list of `ranking_idx` keys of
[`instancefieldrankingmanage.bss`](instancefieldrankingmanage_bss.md). On
client 3482 types `0` to `23` have a row; types `11` to `23` list ranking
`7`, the NA/EU season 1 ranking of the Old Moon Grand Prix (instance
type `11`), and the others list none. The file is the `InstanceRanking`
sheet compiled into a PABR table, with the sheet's row for one service.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes             |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | --------------------- |
| 1      | 1509 and later | 3482    | `instancefieldranking.bss` | 216   | 24 Row  | 6 to 10, 8 on average |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `instancefieldranking.bss` | 216 B (100.0%) | 0 B (0.0%) |

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
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | Layout 1 |
| 1969   | Layout 1 |
| 1937   | Layout 1 |
| 1914   | Layout 1 |
| 1886   | Layout 1 |
| 1866   | Layout 1 |
| 1838   | Layout 1 |
| 1818   | Layout 1 |
| 1794   | Layout 1 |
| 1784   | Layout 1 |
| 1749   | Layout 1 |
| 1717   | Layout 1 |
| 1698   | Layout 1 |
| 1674   | Layout 1 |
| 1636   | Layout 1 |
| 1608   | Layout 1 |
| 1587   | Layout 1 |
| 1565   | Layout 1 |
| 1537   | Layout 1 |
| 1509   | Layout 1 |
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

None. The keys point into
[`instancefieldrankingmanage.bss`](instancefieldrankingmanage_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                             |
| ------------------- | ----------------- | ------------------ | --------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                            |
| `+0x04`             | u32               | record_count       | Number of rows                    |
| `+0x08`             | Row[record_count] | records            | See Row                           |
| `records+0x00`      | String Table      | string_table       | Empty                             |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count` |
| `string_table+0x04` | u32               | zero               | `0`                               |

### Row (variable: 6 bytes + list)

| Offset  | Type                | Field               | Notes |
| ------- | ------------------- | ------------------- | ----- |
| `+0x00` | u16                 | instance_field_type | Row key, `0` up, one row per type in key order |
| `+0x02` | u32                 | ranking_count       | Number of rankings |
| `+0x06` | u32[ranking_count]  | ranking_idxs        | `ranking_idx` keys of `instancefieldrankingmanage.bss` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

The `InstanceRanking` sheet of a private server's `DataSheets.bexcel` on
client 1784 has one row per `PA_GAME_SERVICE_TYPE` and the columns
`instanceFieldType_0` to `instanceFieldType_23`; each cell is a list of
`RankingIdx` values of the `InstanceRankingManage` sheet. The file of the
NA/EU client 1784 holds the cells of the `NA_REAL` row (service type
`12`): `instanceFieldType_11` is `7` there and in the file. The row key is
the `N` of the column name, so it is named `instance_field_type`.

## Notes

- Row counts: 20 on client 1784 (types `0` to `19`), 23 on clients 2107 to 2765 and
  24 from client 3002 on. Every row from type `11` on lists ranking `7` on
  each of those clients.

## Open Questions

### Rankings on Types 12 and Up

On client 1784 the sheet fills only `instanceFieldType_11`; `12` to `19`
are `<null>` there, yet the file gives types `12` to `19` the same list
`7`. Whether the build tool copies an empty cell from the column before
it, or the live sheet holds these lists, is open. No instance field type
other than `11` has a row in `instancefieldrankingmanage.bss`.
