# `petexp.dbss` Format

## Purpose

Defines pet experience curves keyed by EXP table ID. Each record stores a maximum pet level and per-level u64 EXP thresholds. Companion `petexpoffset.dbss` provides keyed lookup into this fixed-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------------------------ | --------- |
| 2      | 1964 and later | 3483    | `petexp.dbss`       | 3,676 | 9 Data Payload, 9 Record | 406       |
| 2      | 1964 and later | 3483    | `petexpoffset.dbss` | 94    | 9 Offset Row             | 10        |
| 1      | 1346 to 1958   | 1958    | `petexp.dbss`       | 2,956 | 9 Data Payload, 9 Record | 326       |
| 1      | 1346 to 1958   | 1958    | `petexpoffset.dbss` | 94    | 9 Offset Row             | 10        |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 2      | `petexp.dbss`       | 3,676 B (100.0%) | 0 B (0.0%) |
| 2      | `petexpoffset.dbss` | 94 B (100.0%)    | 0 B (0.0%) |
| 1      | `petexp.dbss`       | 2,956 B (100.0%) | 0 B (0.0%) |
| 1      | `petexpoffset.dbss` | 94 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
| 2717   | Layout 2             |
| 2709   | Layout 2             |
| 2703   | Layout 2             |
| 2695   | Layout 2             |
| 2684   | Layout 2             |
| 2672   | Layout 2             |
| 2665   | Layout 2             |
| 2657   | Layout 2             |
| 2649   | Layout 2             |
| 2644   | Layout 2             |
| 2637   | Layout 2             |
| 2629   | Layout 2             |
| 2619   | Layout 2             |
| 2612   | Layout 2             |
| 2606   | Layout 2             |
| 2602   | Layout 2             |
| 2601   | Layout 2             |
| 2592   | Layout 2             |
| 2583   | Layout 2             |
| 2575   | Layout 2             |
| 2567   | Layout 2             |
| 2560   | Layout 2             |
| 2553   | Layout 2             |
| 2545   | Layout 2             |
| 2538   | Layout 2             |
| 2529   | Layout 2             |
| 2519   | Layout 2             |
| 2513   | Layout 2             |
| 2510   | Layout 2             |
| 2507   | Layout 2             |
| 2503   | Layout 2             |
| 2498   | Layout 2             |
| 2492   | Layout 2             |
| 2487   | Layout 2             |
| 2480   | Layout 2             |
| 2474   | Layout 2             |
| 2468   | Layout 2             |
| 2460   | Layout 2             |
| 2453   | Layout 2             |
| 2444   | Layout 2             |
| 2438   | Layout 2             |
| 2434   | Layout 2             |
| 2429   | Layout 2             |
| 2421   | Layout 2             |
| 2414   | Layout 2             |
| 2407   | Layout 2             |
| 2401   | Layout 2             |
| 2397   | Layout 2             |
| 2393   | Layout 2             |
| 2384   | Layout 2             |
| 2378   | Layout 2             |
| 2372   | Layout 2             |
| 2358   | Layout 2             |
| 2352   | Layout 2             |
| 2347   | Layout 2             |
| 2343   | Layout 2             |
| 2335   | Layout 2             |
| 2327   | Layout 2             |
| 2324   | Layout 2             |
| 2319   | Layout 2             |
| 2313   | Layout 2             |
| 2308   | Layout 2             |
| 2302   | Layout 2             |
| 2295   | Layout 2             |
| 2290   | Layout 2             |
| 2284   | Layout 2             |
| 2276   | Layout 2             |
| 2269   | Layout 2             |
| 2259   | Layout 2             |
| 2250   | Layout 2             |
| 2243   | Layout 2             |
| 2235   | Layout 2             |
| 2229   | Layout 2             |
| 2224   | Layout 2             |
| 2218   | Layout 2             |
| 2215   | Layout 2             |
| 2207   | Layout 2             |
| 2203   | Layout 2             |
| 2196   | Layout 2             |
| 2192   | Layout 2             |
| 2189   | Layout 2             |
| 2183   | Layout 2             |
| 2179   | Layout 2             |
| 2171   | Layout 2             |
| 2163   | Layout 2             |
| 2156   | Layout 2             |
| 2151   | Layout 2             |
| 2147   | Layout 2             |
| 2142   | Layout 2             |
| 2138   | Layout 2             |
| 2134   | Layout 2             |
| 2130   | Layout 2             |
| 2122   | Layout 2             |
| 2107   | Layout 2             |
| 2098   | Layout 2             |
| 2089   | Layout 2             |
| 2081   | Layout 2             |
| 2073   | Layout 2             |
| 2067   | Layout 2             |
| 2063   | Layout 2             |
| 2059   | Layout 2             |
| 2052   | Layout 2             |
| 2044   | Layout 2             |
| 2039   | Layout 2             |
| 2032   | Layout 2             |
| 2025   | Layout 2             |
| 2011   | Layout 2             |
| 2005   | Layout 2             |
| 2000   | Layout 2             |
| 1996   | Layout 2             |
| 1991   | Layout 2             |
| 1985   | Layout 2             |
| 1980   | Layout 2             |
| 1969   | Layout 2             |
| 1964   | Layout 2             |
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

| File                 | Required | Role                                                     |
| -------------------- | -------- | -------------------------------------------------------- |
| `petexpoffset.dbss`  | Required | `exp_table_id -> (data_offset, data_size)` lookup index |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of EXP table records (observed: 9) |
| `+0x04` | Record[count] | records | See Record                                |

Records begin immediately after the u32 count. The two bytes at `+0x04` are
the first record's key prefix (`first_record_key` in earlier versions of this
doc), not header payload.

### Record (408 bytes)

Each record is stored as `[u16 key_prefix][data_bytes]`. The companion offset points to `data_bytes`, so `record_start = data_offset - 2`.

| Offset  | Type         | Field      | Notes                                               |
| ------- | ------------ | ---------- | --------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Equals `exp_table_id` in the following data payload |
| `+0x02` | Data Payload | data_bytes | 406-byte payload; see Data Payload                  |

### Data Payload (406 bytes)

Offsets are relative to `data_offset` from `petexpoffset.dbss`.

| Offset  | Type    | Field        | Notes                                                                                  |
| ------- | ------- | ------------ | -------------------------------------------------------------------------------------- |
| `+0x00` | u16     | exp_table_id | Matches the 2-byte key prefix and the companion offset key                              |
| `+0x02` | u32     | max_level    | Number of valid EXP thresholds in `level_exp` (observed: 10, 20, 30, 50)               |
| `+0x06` | u64[50] | level_exp    | Fixed-capacity threshold array; only first `max_level` values are populated            |

Unused `level_exp` slots after `max_level` are zero-filled. Data size is always 406 bytes (`2 + 4 + 50 * 8`) even when `max_level` is less than 50.

### `petexpoffset.dbss`

Provides keyed lookup into `petexp.dbss`.

| Offset  | Type              | Field | Notes                          |
| ------- | ----------------- | ----- | ------------------------------ |
| `+0x00` | u32               | count | Must equal `petexp.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                 |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                               |
| ------- | ---- | ------------ | ----------------------------------------------------------------------------------- |
| `+0x00` | u16  | exp_table_id | Matches `key_prefix` and data payload `exp_table_id`                                |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petexp.dbss` to the data payload, after the 2-byte prefix  |
| `+0x06` | u32  | data_size    | Size of data payload in bytes (observed: 406 for every record)                      |

Offset records are ordered by descending key: 9, 8, 7, 6, 5, 4, 3, 2, 1.

The rows are the same `[u16 id][u32 offset][u32 size]` rows as a PABR offset table, but the file has no `PABR` magic and no 12-byte trailer (94 bytes = 4 + 9 x 10). The parser reads it with `parse_bare_offset_rows` from `_common/pabr_offset.py`.

## Layout 1

On client 1784 `level_exp` holds 40 slots, so every payload is 326 bytes
(`2 + 4 + 40 * 8`) and `data_size` is 326. The Record and Data Payload
differ from Layout 2.

### Record (328 bytes)

| Offset  | Type         | Field      | Notes                                               |
| ------- | ------------ | ---------- | --------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Equals `exp_table_id` in the following data payload |
| `+0x02` | Data Payload | data_bytes | 326-byte payload; see Data Payload                  |

### Data Payload (326 bytes)

| Offset  | Type    | Field        | Notes                                                    |
| ------- | ------- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16     | exp_table_id | Matches the 2-byte key prefix and the companion offset key |
| `+0x02` | u32     | max_level    | 10 to 40 on client 1784                                  |
| `+0x06` | u64[40] | level_exp    | Only the first `max_level` values are populated          |

## Observed Records

| EXP Table ID | Max Level | First EXP Values                       | Last Populated EXP Values |
| ------------ | --------- | -------------------------------------- | ------------------------- |
| 9            | 50        | 2055, 2260, 2599, 2989, 3437          | 13588, 13724, 13861       |
| 8            | 30        | 1746, 1921, 2209, 2541, 2922          | 9105, 9196, 9288          |
| 7            | 20        | 2055, 2260, 2599, 2989, 3437          | 9328, 9794, 10284         |
| 6            | 10        | 2055, 2260, 2599, 2989, 3437          | 5228, 6012, 6914          |
| 5            | 10        | 100, 300, 500, 700, 900               | 1500, 1700, 1900          |
| 4            | 10        | 300, 450, 660, 860, 860               | 1760, 2020, 3020          |
| 3            | 10        | 216, 324, 468, 612, 756               | 1260, 1440, 2160          |
| 2            | 10        | 144, 216, 312, 408, 504               | 840, 960, 1440            |
| 1            | 10        | 120, 180, 260, 340, 420               | 700, 800, 1200            |

Together the nine tables hold 160 level thresholds. Both files are byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Notes

- `pet.dbss` selects the table with `exp_key` (header `+0x0F`, the `Pet_Table` sheet's `RequireEXPType`): keys 1 to 4 for pets, 6 to 9 for Laila. Its `max_level` matches the table's `max_level` on every record.
- Tables 6 to 9 are the fairy curves: 6 Faint, 7 Glimmering, 8 Brilliant, 9 Radiant, matching the grade level caps 10, 20, 30 and 50 in [fairyskillchange.dbss](fairyskillchange_dbss.md). The Ornette's Dark Honey Wine tooltip confirms the split: its `13,300` EXP from [fairyfeedingitem.dbss](fairyfeedingitem_dbss.md) lands on Lv. 5 98.84% on tables 6, 7 and 9 (the tooltip's Faint, Glimmering and Radiant line) and on Lv. 6 58.36% on table 8 (its Brilliant line).
- Records are fixed-capacity, not variable length. `petexpoffset.dbss` still stores offsets and sizes, following the same keyed-index pattern as other DBSS companions.
- The first bytes after the main count (`09 00`) are the first record key prefix, so the apparent 6-byte header should be treated as u32 count plus record 0 prefix.
