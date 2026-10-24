# `plantworker.bss` Format

## Purpose

Worker definition table. The file stores one fixed-size record per worker type/grade, with worker IDs, LOC-backed display names, basic worker stats, upgrade links, and a shared DDS icon path table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | ----------------- | --------- |
| 2      | 2726 and later | 3483    | `plantworker.bss` | 99,484 | 106 Worker Record | 912       |
| 1      | 805 to 2138    | 2138    | `plantworker.bss` | 66,794 | 91 Worker Record  | 707       |

| Layout | File              | Known          | Unknown          |
| ------ | ----------------- | -------------- | ---------------- |
| 2      | `plantworker.bss` | 5,780 B (5.8%) | 93,704 B (94.2%) |
| 1      | `plantworker.bss` | 4,823 B (7.2%) | 61,971 B (92.8%) |

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
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | Layout 1             |
| 1261   | Layout 1             |
| 1256   | Layout 1             |
| 1250   | Layout 1             |
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | Layout 1             |
| 1137   | Layout 1             |
| 1132   | Layout 1             |
| 1127   | Layout 1             |
| 1122   | Layout 1             |
| 1118   | Layout 1             |
| 1114   | Layout 1             |
| 1109   | Layout 1             |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | Layout 1             |
| 805    | Layout 1             |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
| 652    | No documented layout |
| 643    | No documented layout |
| 637    | No documented layout |
| 630    | No documented layout |
| 627    | No documented layout |
| 621    | No documented layout |
| 617    | No documented layout |
| 615    | No documented layout |
| 606    | No documented layout |
| 599    | No documented layout |
| 592    | No documented layout |
| 586    | No documented layout |
| 577    | No documented layout |
| 569    | No documented layout |
| 561    | No documented layout |
| 554    | No documented layout |
| 542    | No documented layout |
| 532    | No documented layout |
| 531    | No documented layout |
| 526    | No documented layout |
| 521    | No documented layout |
| 517    | No documented layout |
| 510    | No documented layout |
| 508    | No documented layout |
| 504    | No documented layout |
| 497    | No documented layout |
| 491    | No documented layout |
| 485    | No documented layout |
| 478    | No documented layout |
| 472    | No documented layout |
| 466    | No documented layout |
| 457    | No documented layout |
| 452    | No documented layout |
| 449    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides worker display names via LOC type `6`, `str_id4=0` |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout (`_common/pabr_strings.py`): the header,
the fixed-size worker records, the icon path table and the 8-byte trailer.

| Offset             | Type                  | Field       | Notes                                                  |
| ------------------ | --------------------- | ----------- | ------------------------------------------------------ |
| `+0x00`            | char[4]               | magic       | `PABR` (ASCII)                                         |
| `+0x04`            | u32                   | count       | Number of worker records; observed `106`               |
| `+0x08`            | Worker Record[count]  | records     | See Worker Record                                      |
| `records+0x00`     | Icon Path Table       | icon_paths  | See Icon Path Table                                    |
| `icon_paths+0x00`  | u32                   | table_start | Offset of the icon path table, where the records end   |
| `icon_paths+0x04`  | u32                   | zero        | Always 0                                               |

The first record begins at offset `0x08`, immediately after the header. The
fixed block ends at `0x179A8` for the observed file, where the icon table
begins.

### Icon Path Table (variable: 4 bytes + strings)

Follows the worker record block.

| Offset  | Type        | Field | Notes                                      |
| ------- | ----------- | ----- | ------------------------------------------ |
| `+0x00` | u32         | count | Number of icon path entries; observed `38` |
| `+0x04` | pstr[count] | paths | UTF-8/ASCII DDS paths                      |

Each icon entry has one leading zero byte before the length (the `is_wide`
byte of a `pstr`, observed `0`). The length is the byte count including the
trailing NUL.

### Worker Record (912 bytes)

| Offset   | Type       | Field           | Notes                                              |
| -------- | ---------- | --------------- | -------------------------------------------------- |
| `+0x00`  | u16        | worker_id       | Worker/NPC ID; LOC type `6` name key               |
| `+0x02`  | u16        | next_worker_id  | Next-grade/linked worker ID, or `0`                |
| `+0x04`  | u16        | unknown_04      | Non-zero on 34 of 106 records on client 3473 (1011, 2001 to 2018), `0` on the rest |
| `+0x06`  | u32        | grade_class     | Grade the game colors the name by, see Grade Class |
| `+0x0A`  | u32        | unknown_0a      | Always `grade_class + 5`; meaning unresolved       |
| `+0x0E`  | u32        | move_speed      | Move speed × 100 (`200` is 2.00 in game)            |
| `+0x12`  | u32        | stamina         | Worker stamina                                     |
| `+0x16`  | u32        | luck            | Luck × 10,000 (`50000` is 5.00 in game)             |
| `+0x1A`  | u8         | unknown_1a      |                                                    |
| `+0x1B`  | u32        | icon_index      | Zero-based index into the trailing icon path table |
| `+0x1F`  | bytes[336] | unknown_1f      | See Open Questions                                 |
| `+0x16F` | u32        | base_work_speed | Work speed × 1,000,000 (`30000000` is 30.00)        |
| `+0x173` | bytes[541] | unknown_173     | See Open Questions                                 |

Records are fixed-size `0x390` byte structs. Remaining bytes contain many stat/progression values that are not fully named yet.

Earlier versions of this doc called `grade_class` `unknown_06`, and before that `unknown_loc_a`; `unknown_0a` was `unknown_loc_b`.

## Layout 1

On client 1784 a Worker Record was 707 bytes: `grade_class` and
`unknown_0a` were u16, which moved every later field 4 bytes earlier, and
the two unknown blocks were shorter (`unknown_1f` 256 bytes instead of 336,
`unknown_173` 420 instead of 541). Only the Worker Record differs from
Layout 2. Field names keep Layout 2's offsets, so `icon_index` sits at
`+0x17` here. On client 1784 the file holds 89 records.

### Worker Record (707 bytes)

| Offset   | Type       | Field           | Notes |
| -------- | ---------- | --------------- | ----- |
| `+0x00`  | u16        | worker_id       |       |
| `+0x02`  | u16        | next_worker_id  |       |
| `+0x04`  | u16        | unknown_04      |       |
| `+0x06`  | u16        | grade_class     |       |
| `+0x08`  | u16        | unknown_0a      |       |
| `+0x0A`  | u32        | move_speed      |       |
| `+0x0E`  | u32        | stamina         |       |
| `+0x12`  | u32        | luck            |       |
| `+0x16`  | u8         | unknown_1a      |       |
| `+0x17`  | u32        | icon_index      |       |
| `+0x1B`  | bytes[256] | unknown_1f      |       |
| `+0x11B` | u32        | base_work_speed |       |
| `+0x11F` | bytes[420] | unknown_173     |       |

## Grade Class

`grade_class` takes five values, one per name color in game (checked against the worker names on 2026-09-28):

| `grade_class` | Grade          | Color  | Workers (2026-09-27 client)                                      |
| ------------- | -------------- | ------ | ---------------------------------------------------------------- |
| `28023`       | Base or Naive  | green, white for Naive | 27: every plain `... Worker`, every `Naive ...` and the dev workers |
| `28024`       | Skilled        | blue   | 15, including `Demibeast Worker` (`8007`), which is white         |
| `28025`       | Professional   | yellow | 15                                                                |
| `28026`       | Artisan        | red    | 20, including the 115 WS Torres, Darifu, Zobadi and Afuaru        |
| `28027`       | Named          | yellow | 29 named workers such as Acher, Tirol and Tiny Nose               |

Naive and base workers share `28023`, and no other field in the record tells them apart, so inside that class the handler checks the English name for `Naive`. The five dev workers (`7996` QA Worker: Time, `7997` QA Worker: Luck, `7998` Grand Chamberlain, `7999` Temporary Laborer, `8000` QA Super Worker) are also `28023` but white in game, and `Demibeast Worker` (`8007`) is `28024` but white too: it is an unused worker with a goblin icon that upgrades into `Artisan Fadus Worker` (`8006`), per [BDO Codex](https://bdocodex.com/us/npc/8007/). The handler lists these six by ID. The values are not LOC keys: LOC type 6 rows with these IDs are unrelated monsters (`28023` Goblin Thrower).

Derived fields:

```text
name = LOC type 6, str_id1=worker_id, str_id4=0
icon_path = icon_paths[icon_index]
```

## Reference Rows

| Slot | Worker ID | Name           | Next Tier | Move | Stamina | Luck  | Icon Index | Base Work Speed |
| ---- | --------- | -------------- | --------- | ---- | ------- | ----- | ---------- | --------------- |
| 0    | `8047`    | Dokkebi Worker | `8048`    | 350  | 8       | 50000 | 0          | 60000000        |
| 100  | `7502`    | Giant Worker   | `7551`    | 200  | 25      | 50000 | 10         | 30000000        |
| 105  | `7504`    | Goblin Worker  | `7552`    | 350  | 8       | 50000 | 2          | 60000000        |

## Notes

- Observed decompressed size is `99,484` bytes, byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.
- File size matches `8 + (106 * 0x390) + 4 + encoded icon path table`.
- The trailing icon table contains `38` DDS paths under `New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/`.

## Open Questions

### Remaining Progression/Stat Arrays

The arrays between `+0x20` and `+0x38F` are not fully identified.

### `unknown_0a` Meaning

`unknown_0a` is always `grade_class + 5` (`28028` to `28032`). It resolves to unrelated LOC rows, and no other worker file references either value.
