# `instancefieldrankingmanage.bss` Format

## Purpose

The season rankings of instance contents: per ranking key the instance
type, the time the ranking starts and ends and the `GAME` sheet key of the
season name. On client 3482 all 14 rows are instance type `11`, the Old
Moon Grand Prix: ranking `1` and `2` are the test seasons of 2021-02 and
`3` to `14` the season 1 rankings of the services, which end in 2099.
[`instancefieldranking.bss`](instancefieldranking_bss.md) picks the
rankings each instance field type shows. The file is the
`InstanceRankingManage` sheet compiled into a PABR table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------- | --------- |
| 1      | 1509 and later | 3482    | `instancefieldrankingmanage.bss` | 454   | 14 Row  | 26        |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `instancefieldrankingmanage.bss` | 454 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Hash of the `ranking_name` key, for its LOC type 37 text |
| `languagedata_en.loc` | Optional | Season name in the user's language |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | Number of rows                     |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | The season name keys               |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (26 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | ranking_idx     | Row key, `1` up in file order |
| `+0x04` | u16  | instance_type   | `11` on every row (client 3482) |
| `+0x06` | u64  | start_date_rank | Start, seconds since 1970-01-01; see [Times](#times) |
| `+0x0E` | u64  | end_date_rank   | End, in the same unit |
| `+0x16` | u32  | ranking_name    | Index into `strings`: a `GAME` sheet key (`LUA_INSTANCE_SEASONRANK_NAME_1`, "Season 1") |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `2` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | `LUA_INSTANCE_SEASONRANK_NAME_1` and `_2`, UTF-8 (`is_wide` 0) |

## Times

The sheet writes the times as a date and a time of day. Read as UTC, the
values of client 3482 give the sheet's own times on all 12 rows client
1784 has (`2021-02-03 08:59` for the start of ranking `1`). The file of
client 1784 holds the same times 9 hours earlier, so they read back as
the sheet's times in Korean time (UTC+9). The tool that compiles the sheet
seems to convert the written time with its own time zone. The handler
shows the values as UTC.

## Field Names

The names follow the `InstanceRankingManage` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`RankingIdx`, `InstanceType`,
`RankingName`, `StartDateRank`, `EndDateRank`). On the 12 keys the sheet
shares with client 1784, `instance_type` and `ranking_name` equal the
sheet on every row and both times equal it read in Korean time; on client
3482 the same 12 keys equal it read as UTC. The developer notes of the
sheet's `.xlsm` copy (`#Desc`) name ranking `1` and `2` "테스트용 그믐달
그랑프리 시즌 1 / 2" (test Old Moon Grand Prix season 1 and 2) and `3` to
`12` the season 1 of one service each (`7`: NA/EU).

## Notes

- Clients 2519 to 3482 have 14 rows; clients 1784 and 2107 have rows `1`
  to `12`.
