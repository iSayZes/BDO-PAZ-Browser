# `petoldfusion.dbss` Format

## Purpose

The result tiers of the old pet exchange, one row per fusion key (variant,
species and tier of the main pet, the four bytes `pet.dbss` stores at
payload `+0x02`): up to four result tiers, each with a chance. It is the
per-species table that [`petfusionnew.dbss`](petfusionnew_dbss.md) (one
row per tier) stands next to. Companion `petoldfusionoffset.dbss` lists
where every row sits. Tiers are stored from 0, as `tier` of
[`pet.dbss`](pet_dbss.md) stores them: `0` is Tier 1. Rates are on the
1,000,000 = 100% scale.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | --------- |
| 1      | 1346 and later | 3483    | `petoldfusion.dbss`       | 15,364 | 384 Row        | 40        |
| 1      | 1346 and later | 3483    | `petoldfusionoffset.dbss` | 4,612  | 384 Offset Row | 12        |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 1      | `petoldfusion.dbss`       | 14,980 B (97.5%) | 384 B (2.5%) |
| 1      | `petoldfusionoffset.dbss` | 4,612 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No file              |
| 1276   | No file              |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                       |
| ------------------------- | -------- | -------------------------------------------------------------------------- |
| `petoldfusionoffset.dbss` | Optional | `fusion key -> (offset, size)` of every row; the parser walks the main file without it |
| `pet.dbss` + `petoffset.dbss` | Optional | The LOC names of the pets with the row's fusion key                    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 384 x 40 = 15,364 bytes.

### Row (40 bytes)

A 4-byte copy of the fusion key, then the 36 bytes the offset row
addresses.

| Offset  | Type     | Field         | Notes                                                                     |
| ------- | -------- | ------------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | key_prefix    | The fusion key `variant`, `species`, `unknown_06`, `tier` read as one u32 |
| `+0x04` | u8       | variant       | Fusion key byte 0: `variant` of the main pet in `pet.dbss` (sheet `Kind`) |
| `+0x05` | u8       | species       | Fusion key byte 1: `species` (sheet `Race`)                               |
| `+0x06` | u8       | unknown_06    | Fusion key byte 2: `0` on every row, as `unknown_04` of `pet.dbss`         |
| `+0x07` | u8       | tier          | Fusion key byte 3: the main pet's tier, from 0                            |
| `+0x08` | u8       | select_tier_0 | First result tier, from 0                                                 |
| `+0x09` | bytes[3] | padding_09    | Alignment bytes of the `select_tier_0` entry, see Notes                   |
| `+0x0C` | u32      | select_rate_0 | Chance of `select_tier_0`                                                 |
| `+0x10` | u8       | select_tier_1 | Second result tier, from 0; `0` with `select_rate_1` `0` when unused       |
| `+0x11` | bytes[3] | padding_11    | Alignment bytes of the `select_tier_1` entry                              |
| `+0x14` | u32      | select_rate_1 | `1000000` when used, else `0`                                             |
| `+0x18` | u8       | select_tier_2 | `0` on every row (client 3474)                                            |
| `+0x19` | bytes[3] | padding_19    | Alignment bytes of the `select_tier_2` entry                              |
| `+0x1C` | u32      | select_rate_2 | `0` on every row (client 3474)                                            |
| `+0x20` | u8       | select_tier_3 | `0` on every row (client 3474)                                            |
| `+0x21` | bytes[3] | padding_21    | Alignment bytes of the `select_tier_3` entry                              |
| `+0x24` | u32      | select_rate_3 | `0` on every row (client 3474)                                            |

### `petoldfusionoffset.dbss`

Bare offset table into `petoldfusion.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `petoldfusion.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (12 bytes)

| Offset  | Type | Field      | Notes                                                                       |
| ------- | ---- | ---------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | fusion_key | Key of the row it points at, equal to its `key_prefix`                      |
| `+0x04` | u32  | offset     | Absolute byte offset in `petoldfusion.dbss` of the row's `variant`, past the key prefix |
| `+0x08` | u32  | size       | `36` on every row: the row without its key prefix                          |

Both files list the keys in the same order, which is not sorted.

## Exchange Results

On client 3474 the 384 rows cover 96 variant and species pairs of 42
species, four tiers each. With tiers as the game numbers them:

| Main pet | First result | Chance | Second result | Rows (client 3474) |
| -------- | ------------ | ------ | ------------- | ------------------ |
| Tier 1   | Tier 3       | 50%    | Tier 2        | 95                 |
| Tier 2   | Tier 3       | 70%    | Tier 2        | 94                 |
| Tier 3   | Tier 4       | 30%    | Tier 3        | 94                 |
| Tier 4   | Tier 4       | 100%   | none          | 96                 |

Five rows differ: one Tier 1 row with Tier 2 at 100%, one Tier 2 row with
Tier 3 at 100%, one Tier 2 row with Tier 3 at 40%, one Tier 3 row with
Tier 4 at 100% and one Tier 3 row with Tier 4 at 10%.

## Field Names

The `Pet_OldFusion_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Race`, `Kind`, `Tier`, `SelectRate_0` to
`SelectRate_3` and `SelectTier_0` to `SelectTier_3`, and its 380 rows match
the file on all 380 keys (`Race` = `species`, `Kind` = `variant`) and all
eight value columns, on client 1784 (380 rows) and on client 3474 (384
rows; the four more are species `84`, variant `1`). The file stores each
tier before its rate; the sheet lists the rate first, and its empty cells
(`<null>`) are the zeros of the file. The developer workbook
(`datasheet_petdatatable.xlsm`) adds the note columns
`#SelectCharacterName_0` to `#SelectCharacterName_3`, which name each select
tier as a generation (`3세대` for `2`), and `#참조 : 합성 세대 정보`
("reference: fusion generation info") with the tier pairs a row stands for
(`1+1` on tier `0`, `1+2, 2+2` on tier `1`).

The client 1784 server dump names the type `gc::PetOldFusionStaticStatus`,
held in a `BinaryUnorderedMap` keyed by `gc::PetFusionKey`, with the manager
`PetOldFusionStaticStatusManager`. The 2016 client's debug symbols have
`gc::PetFusionKey` as one u32 `_value`, and `gc::PetStaticStatus` stores the
same four bytes as `_fusionKey`; `pet.dbss` names them `variant`, `species`,
a zero byte and `tier`, and this doc takes those names.

## Notes

- `padding_09`, `padding_11`, `padding_19` and `padding_21` are the 3 bytes
  between a u8 tier and its 4-byte aligned rate, as in `petfusionnew.dbss`:
  each select is an 8-byte entry copied whole. On client 3474 they read
  `7F 00 00` in the first three entries and `00 00 00` in the fourth, in
  every row; on client 1784 `00 00 00`, `01 00 00`, `00 00 00` and
  `00 00 00`, while the sheet values are the same.
- Clients 1485, 1784, 2107, 2519, 3002 and 3251 ship both files.
- 20 rows on client 3474, all four tiers of five species and variant pairs
  (species `36` variant `1`, `39` and `6`, `84` and `1`, `99` and `99`,
  `100` and `100`), have no pet with their fusion key in `pet.dbss`; the
  handler's Pets column is empty for them.
- No client Lua reads the file: the exchange window
  (`panel_window_petfusion_all_1.luac`) shows the chances of
  [`petfusionnew.dbss`](petfusionnew_dbss.md) and
  [`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md)
  (`ToClient_getMainFusionRate`, `ToClient_getAddFusionRate`).

## Open Questions

### Whether the Server Still Reads the Table

The live exchange window shows the per-tier chances of `petfusionnew.dbss`,
and Garmoth's pets guide gives chances that match those. Whether the
server still uses the per-species rows here (the name says "old"), and
whether `select_rate_1` `1000000` is a cumulative bound or a chance of its
own, is not in the client data.
