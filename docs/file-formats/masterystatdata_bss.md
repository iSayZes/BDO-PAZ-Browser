# `{alchemy,collecting,cooking,fishing,hunting,sail,training}statdata.bss` and `manufacturingstat.bss` Format

## Purpose

The life skill mastery tables: for each mastery step, the bonuses that the
Life Skill tab tooltips show. Eight files share the layout and differ only
in the fields after the mastery value and in the number of row groups:

| File                     | Life skill | Row groups      | Row size | Fields after mastery |
| ------------------------ | ---------- | --------------- | -------- | -------------------- |
| `fishingstatdata.bss`    | Fishing    | 1               | 8        | 1                    |
| `cookingstatdata.bss`    | Cooking    | 1               | 24       | 5                    |
| `huntingstatdata.bss`    | Hunting    | 1               | 36       | 8                    |
| `alchemystatdata.bss`    | Alchemy    | 1               | 40       | 9                    |
| `sailstatdata.bss`       | Sailing    | 1               | 44       | 10                   |
| `trainingstatdata.bss`   | Training   | 1               | 16       | 3                    |
| `collectingstatdata.bss` | Gathering  | one per type    | 36       | 8                    |
| `manufacturingstat.bss`  | Processing | one per type    | 16       | 3                    |

The six single-group files step by 50 mastery from 3000 down to 0. The
gathering table does the same once per gathering type; the processing table
runs up from 1 to 2999 once per processing type.

The Gathering and Processing mastery that life levels give is in
[`commonlifestatdata.bss`](commonlifestatdata_bss.md), which has its own
layout.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes  | Records                                | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------ | -------------------------------------- | --------- |
| 2      | 2726 and later | 3483    | `alchemystatdata.bss`    | 2,460  | 61 Alchemy Row                         | 40        |
| 2      | 2726 and later | 3483    | `collectingstatdata.bss` | 15,464 | 19 Gathering Group, 427 Gathering Row  | 36        |
| 2      | 2726 and later | 3483    | `cookingstatdata.bss`    | 1,484  | 61 Cooking Row                         | 24        |
| 2      | 2726 and later | 3483    | `fishingstatdata.bss`    | 508    | 61 Fishing Row                         | 8         |
| 2      | 2726 and later | 3483    | `huntingstatdata.bss`    | 2,216  | 61 Hunting Row                         | 36        |
| 2      | 2726 and later | 3483    | `manufacturingstat.bss`  | 7,340  | 7 Processing Group, 456 Processing Row | 16        |
| 2      | 2726 and later | 3483    | `sailstatdata.bss`       | 2,704  | 61 Sailing Row                         | 44        |
| 2      | 2726 and later | 3483    | `trainingstatdata.bss`   | 996    | 61 Training Row                        | 16        |
| 1      | 1338 to 2717   | 2717    | `alchemystatdata.bss`    | 1,414  | 41 Alchemy Row                         | 34        |
| 1      | 1338 to 2717   | 2717    | `collectingstatdata.bss` | 10,412 | 16 Gathering Group, 287 Gathering Row  | 36        |
| 1      | 1338 to 2717   | 2717    | `cookingstatdata.bss`    | 1,004  | 41 Cooking Row                         | 24        |
| 1      | 1338 to 2717   | 2717    | `fishingstatdata.bss`    | 348    | 41 Fishing Row                         | 8         |
| 1      | 1338 to 2717   | 2717    | `huntingstatdata.bss`    | 1,496  | 41 Hunting Row                         | 36        |
| 1      | 1338 to 2717   | 2717    | `manufacturingstat.bss`  | 6,380  | 7 Processing Group, 396 Processing Row | 16        |
| 1      | 1338 to 2717   | 2717    | `sailstatdata.bss`       | 1,824  | 41 Sailing Row                         | 44        |
| 1      | 1338 to 2717   | 2717    | `trainingstatdata.bss`   | 676    | 41 Training Row                        | 16        |

| Layout | File                     | Known            | Unknown         |
| ------ | ------------------------ | ---------------- | --------------- |
| 2      | `alchemystatdata.bss`    | 1,728 B (70.2%)  | 732 B (29.8%)   |
| 2      | `collectingstatdata.bss` | 12,048 B (77.9%) | 3,416 B (22.1%) |
| 2      | `cookingstatdata.bss`    | 1,484 B (100.0%) | 0 B (0.0%)      |
| 2      | `fishingstatdata.bss`    | 508 B (100.0%)   | 0 B (0.0%)      |
| 2      | `huntingstatdata.bss`    | 508 B (22.9%)    | 1,708 B (77.1%) |
| 2      | `manufacturingstat.bss`  | 3,692 B (50.3%)  | 3,648 B (49.7%) |
| 2      | `sailstatdata.bss`       | 2,216 B (82.0%)  | 488 B (18.0%)   |
| 2      | `trainingstatdata.bss`   | 996 B (100.0%)   | 0 B (0.0%)      |
| 1      | `alchemystatdata.bss`    | 1,168 B (82.6%)  | 246 B (17.4%)   |
| 1      | `collectingstatdata.bss` | 8,116 B (77.9%)  | 2,296 B (22.1%) |
| 1      | `cookingstatdata.bss`    | 1,004 B (100.0%) | 0 B (0.0%)      |
| 1      | `fishingstatdata.bss`    | 348 B (100.0%)   | 0 B (0.0%)      |
| 1      | `huntingstatdata.bss`    | 348 B (23.3%)    | 1,148 B (76.7%) |
| 1      | `manufacturingstat.bss`  | 3,212 B (50.3%)  | 3,168 B (49.7%) |
| 1      | `sailstatdata.bss`       | 1,496 B (82.0%)  | 328 B (18.0%)   |
| 1      | `trainingstatdata.bss`   | 676 B (100.0%)   | 0 B (0.0%)      |

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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
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
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
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
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
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

None. The files are self-contained. All multi-byte values are little-endian.

## Layout 2

Each of the eight files has its own top-level table: `### File Layout` is
`fishingstatdata.bss`, and the other seven files have a table under their
own name.

Every row opens with `mastery`, the f32 mastery threshold: `3000.0` down to
`0.0` in steps of 50 on client 3464; `1.0` up to `2999.0` in
`manufacturingstat.bss`. The fields after it are u32 rates unless noted,
with `1,000,000` = 100%. `PaGlobalFunc_GlobalUtil_RoundRateToSecondPoint` in
`global_util_ui.luac` turns a rate into the tooltip percent:
floor((rate + 50) / 100) / 100, two decimals.

The field names are the members the Life Skill tab script reads,
`HandleEventOnOut_CharInfoLife_All_LifeType_Tooltip` in
`panel_characterinfo_life_all_2.luac` (decompiled with unluac), from the
`ToClient_get*StatStaticStatus()` wrapper of each skill. The tooltip text
is the LOC type 37 row of the `LUA_CHARACTERINFO_LIFE_*_DESC*` key in
`stringtable.bss`.

### File Layout

The PABR layout of [`blizzardregioninfo.bss`](blizzardregioninfo_bss.md):
fixed rows, an empty string table and the 8-byte trailer. The rows come in
groups, each with its own row count; a single-group file is the plain PABR
table. The six single-group files (`fishingstatdata.bss` here, and
`cookingstatdata.bss`, `huntingstatdata.bss`, `alchemystatdata.bss`,
`sailstatdata.bss`, `trainingstatdata.bss` below) differ only in the row
type.

| Offset         | Type               | Field        | Notes                                           |
| -------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Fishing Row[count] | rows         | See Fishing Row                                 |
| `rows+0x00`    | u32                | string_count | Always `0`                                      |
| `rows+0x04`    | u32                | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                | zero         | Always `0`                                      |

### Fishing Row (8 bytes)

| Offset  | Type | Field   | Notes                                                    |
| ------- | ---- | ------- | -------------------------------------------------------- |
| `+0x00` | f32  | mastery | Mastery threshold                                        |
| `+0x04` | u32  | rate    | `_rate`, "Prize Catch Fish Rate" (`LUA_CHARACTERINFO_LIFE_FISHINGSTAT_DESC`) |

### `cookingstatdata.bss`

| Offset         | Type               | Field        | Notes                                           |
| -------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Cooking Row[count] | rows         | See Cooking Row                                 |
| `rows+0x00`    | u32                | string_count | Always `0`                                      |
| `rows+0x04`    | u32                | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                | zero         | Always `0`                                      |

### Cooking Row (24 bytes)

| Offset  | Type | Field                      | Notes                                         |
| ------- | ---- | -------------------------- | --------------------------------------------- |
| `+0x00` | f32  | mastery                    | Mastery threshold                             |
| `+0x04` | u32  | speed_cook_rate            | `_speedCookRate`, "Chance of mass cooking activating" |
| `+0x08` | u32  | basic_max_drop_rate        | `_basicMaxDropRate`, "Chance of max dishes"   |
| `+0x0C` | u32  | add_critical_drop_rate     | `_addCriticalDropRate`, "Chance of cooking higher grade dish" |
| `+0x10` | u32  | add_critical_max_drop_rate | `_addCriticalMaxDropRate`, "Chance of cooking max higher grade dishes" |
| `+0x14` | u32  | add_royal_trade_bonus      | `_addRoyalTradeBonus`, Imperial Delivery "Extra Profit" |

The tooltip reads the five members in this order and fills `rate1` to `rate4`
of `LUA_CHARACTERINFO_LIFE_COOK_DESC_1` and `rate1` of `_DESC_2` with them.
Two facts from the data fit the order: `+0x08` and `+0x10`, the two "max"
fields, hold the same value in every row on client 3464, and `+0x14` equals
the Alchemy `add_royal_trade_bonus` in every row. The in-game tooltip at
Cooking Mastery 595 shows 21.16%, 6.76%, 2.25%, 6.76% and 24.60%, the
mastery 550 row in this order (client 3464).

### `huntingstatdata.bss`

| Offset         | Type               | Field        | Notes                                           |
| -------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Hunting Row[count] | rows         | See Hunting Row                                 |
| `rows+0x00`    | u32                | string_count | Always `0`                                      |
| `rows+0x04`    | u32                | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                | zero         | Always `0`                                      |

### Hunting Row (36 bytes)

| Offset  | Type | Field        | Notes                                              |
| ------- | ---- | ------------ | -------------------------------------------------- |
| `+0x00` | f32  | mastery      | Mastery threshold                                  |
| `+0x04` | u32  | unknown_04   | Always `0` on client 3464                          |
| `+0x08` | u32  | hunting_rate | "Chance of butchering more items"                  |
| `+0x0C` | u32  | unknown_0c   | Always `0` on client 3464                          |
| `+0x10` | u32  | unknown_10   | Always `0` on client 3464                          |
| `+0x14` | u32  | unknown_14   | Always `0` on client 3464                          |
| `+0x18` | u32  | unknown_18   | Always `0` on client 3464                          |
| `+0x1C` | u32  | unknown_1c   | Always `0` on client 3464                          |
| `+0x20` | u32  | unknown_20   | Always `0` on client 3464                          |

The hunting tooltip shows one mastery value, `ToClient_getHuntingRate()`, in
`LUA_CHARACTERINFO_LIFE_HUNTING_DESC`; there is no hunting static status
wrapper in the Lua. `+0x08` is the only field that is not always 0, so it
takes the getter's name. The in-game tooltip at Hunting Mastery 405 shows
"Chance of butchering more items: +43.91%", the mastery 400 row's `439,091`
(client 3464).

### `alchemystatdata.bss`

| Offset         | Type               | Field        | Notes                                           |
| -------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Alchemy Row[count] | rows         | See Alchemy Row                                 |
| `rows+0x00`    | u32                | string_count | Always `0`                                      |
| `rows+0x04`    | u32                | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                | zero         | Always `0`                                      |

### Alchemy Row (40 bytes)

| Offset  | Type | Field                 | Notes                                                    |
| ------- | ---- | --------------------- | -------------------------------------------------------- |
| `+0x00` | f32  | mastery               | Mastery threshold                                        |
| `+0x04` | u32  | basic_max_drop_rate   | `_basicMaxDropRate`, "Chance of max products"            |
| `+0x08` | u32  | add_royal_trade_bonus | `_addRoyalTradeBonus`, Imperial Delivery "Extra Profit"  |
| `+0x0C` | u32  | unknown_0c            | `15690` in every row on client 3464                      |
| `+0x10` | u32  | event_drop_rate_0     | `getEventDropRateForTooltip(0)`; `1,000,000` in every row on client 3464 |
| `+0x14` | u32  | unknown_14            | `15691` in every row on client 3464                      |
| `+0x18` | u32  | event_drop_rate_1     | `getEventDropRateForTooltip(1)`, special item share      |
| `+0x1C` | u32  | unknown_1c            | `15692` in every row on client 3464                      |
| `+0x20` | u32  | event_drop_rate_2     | `getEventDropRateForTooltip(2)`, rare item share         |
| `+0x24` | u32  | event_drop_rate       | `_eventDropRate`, chance of an extra item                |

The tooltip splits `event_drop_rate` into the three "Chance of extra ...
items" lines of `LUA_CHARACTERINFO_LIFE_ALCHEMY_DESC_1`:

```text
basic   = event_drop_rate * (1 - share_2) * (1 - share_1)
special = event_drop_rate * (1 - share_2) * share_1
rare    = event_drop_rate * share_2
```

and rounds them with `PaGlobalFunc_GlobalUtil_RoundRateToThridPoint`
(floor((rate + 5) / 10) / 1000, three decimals). Share 0 is read but not
used. The handler stores the three results as `extra_basic_item_rate`,
`extra_special_item_rate` and `extra_rare_item_rate`.

The tooltip reads `_basicMaxDropRate` first and `_addRoyalTradeBonus` last,
so the read order does not match the file here. `+0x08` is the royal trade
bonus because it equals the Cooking `add_royal_trade_bonus` in every row; the
Lua describes both as the Imperial Delivery "Extra Profit". Of `+0x04` and
`+0x24`, `+0x04` is 0 at mastery 0 and has the shape and size of the Cooking
`basic_max_drop_rate` (`500,000` against `611,524` at mastery 2000), while
`+0x24` is `3,000` at mastery 0 like the event shares, which are not 0 there
either (`150,000` and `20,000`).

### `sailstatdata.bss`

| Offset         | Type               | Field        | Notes                                           |
| -------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Sailing Row[count] | rows         | See Sailing Row                                 |
| `rows+0x00`    | u32                | string_count | Always `0`                                      |
| `rows+0x04`    | u32                | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                | zero         | Always `0`                                      |

### Sailing Row (44 bytes)

| Offset  | Type | Field            | Notes                                                    |
| ------- | ---- | ---------------- | -------------------------------------------------------- |
| `+0x00` | f32  | mastery          | Mastery threshold                                        |
| `+0x04` | f32  | unknown_04       | Mastery / 50 on client 3464 (`60.0` at 3000)              |
| `+0x08` | u32  | unknown_08       | Always `8`, the number of `CppEnums.ServantStatType` entries |
| `+0x0C` | u32  | acceleration     | `getVariedStatByIndex(0)`, "Accel."                      |
| `+0x10` | u32  | max_move_speed   | `getVariedStatByIndex(1)`, "Speed"                       |
| `+0x14` | u32  | cornering_speed  | `getVariedStatByIndex(2)`, "Turn"                        |
| `+0x18` | u32  | brake_speed      | `getVariedStatByIndex(3)`, "Brake"                       |
| `+0x1C` | u32  | cannon_cool_time | Mastery / 50 on client 3464; not a rate                  |
| `+0x20` | u32  | cannon_accuracy  | Same values as `cannon_cool_time`                        |
| `+0x24` | u32  | max_length       | Same values as `cannon_cool_time`                        |
| `+0x28` | u32  | max_angle        | Same values as `cannon_cool_time`                        |

The eight values from `+0x0C` follow `CppEnums.ServantStatType` in
`global_define_cpp_enum.luac`: `Type_Acceleration` 0, `Type_MaxMoveSpeed` 1,
`Type_CorneringSpeed` 2, `Type_BrakeSpeed` 3, `Type_CannonCoolTime` 4,
`Type_CannonAccuracy` 5, `Type_MaxLength` 6, `Type_MaxAngle` 7. The Life
Skill tab and `panel_window_shipinfo_all_1.luac` /
`panel_window_shipinfo_renewal_all_1.luac` read index 0 as acceleration and
1 as speed, the enum order. `PaGlobal_SailStatToolTip` in
`panel_window_servantinfo_workership.luac` reads index 0 for speed and 1 for
acceleration. All four are equal in every row on client 3464, so the shown
values do not depend on it. No Lua reads indices 4 to 7.

The four rates match `LUA_CHARACTERINFO_LIFE_SAILSTAT_DESC_1`: +0.5% per 50
mastery up to 2000 and +0.25% per 50 above, `250,000` (25%) at 3000.

### `trainingstatdata.bss`

| Offset         | Type                | Field        | Notes                                           |
| -------------- | ------------------- | ------------ | ----------------------------------------------- |
| `+0x00`        | char[4]             | magic        | ASCII `PABR`                                    |
| `+0x04`        | u32                 | count        | Number of rows; `61` on client 3464             |
| `+0x08`        | Training Row[count] | rows         | See Training Row                                |
| `rows+0x00`    | u32                 | string_count | Always `0`                                      |
| `rows+0x04`    | u32                 | table_start  | Offset of `string_count`, where the rows end    |
| `rows+0x08`    | u32                 | zero         | Always `0`                                      |

### Training Row (16 bytes)

| Offset  | Type | Field                        | Notes                                                       |
| ------- | ---- | ---------------------------- | ----------------------------------------------------------- |
| `+0x00` | f32  | mastery                      | Mastery threshold                                           |
| `+0x04` | u32  | add_horse_capture_rate       | `_addHorseCaptureRate`, "Horse Capture Rate"; `437,500` at 3000 (client 3464) |
| `+0x08` | u32  | add_mating_rate              | `_addMatingRate`, "Chance of getting a higher tier horse from breeding or exchange"; rises by `10,000` every 200 mastery |
| `+0x0C` | u32  | add_vehicle_experience_rate  | `_addVehicleExperienceRate`, "Mount EXP"; `937,500` at 3000 |

The tooltip (`LUA_CHARACTERINFO_LIFE_TRAINING_DESC_1`) fills `rate1` to
`rate3` with capture rate, mount EXP and higher tier chance. The in-game
tooltip at Training Mastery 385 shows 3.84%, 5.62% and 2.00%: the mastery 350
row's `+0x04`, `+0x0C` and `+0x08` (client 3464).

### `collectingstatdata.bss`

| Offset     | Type                   | Field        | Notes                                           |
| ---------- | ---------------------- | ------------ | ----------------------------------------------- |
| `+0x00`    | char[4]                | magic        | ASCII `PABR`                                    |
| `+0x04`    | Gathering Group[..table_start] | groups       | Groups back to back until `table_start`         |
| `EOF-0x0C` | u32                    | string_count | Always `0`                                      |
| `EOF-0x08` | u32                    | table_start  | Offset of `string_count`, where the groups end  |
| `EOF-0x04` | u32                    | zero         | Always `0`                                      |

### Gathering Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field | Notes                         |
| ------- | -------------------- | ----- | ----------------------------- |
| `+0x00` | u32                  | count | Number of rows in the group   |
| `+0x04` | Gathering Row[count] | rows  | `count` rows                  |

The group index, counted from 0, is the type `subType` that the Lua passes to
the table's getter (see [Gathering Row](#gathering-row-36-bytes) and
[Processing Row](#processing-row-16-bytes)). Group counts on client 3464:

| File                     | Groups | Group counts                           |
| ------------------------ | ------ | -------------------------------------- |
| six single-group files   | 1      | `61`                                   |
| `collectingstatdata.bss` | 19     | `0`, then `61` for groups 1 to 7, then `0` for groups 8 to 18 |
| `manufacturingstat.bss`  | 7      | `0`, then `76` for groups 1 to 6       |

The seven gathering groups are byte-identical on client 3464, and so are
the six processing groups.

### Gathering Row (36 bytes)

| Offset  | Type | Field                 | Notes                                                 |
| ------- | ---- | --------------------- | ----------------------------------------------------- |
| `+0x00` | f32  | mastery               | Mastery threshold                                     |
| `+0x04` | u32  | add_drop_rate_0       | `getCollectingStatAddDropRate(0)`, Basic Resources "Drop rate" |
| `+0x08` | u32  | add_drop_count_rate_0 | `getCollectingStatAddDropCountRate(0)`, Basic Resources "Quantity" |
| `+0x0C` | u32  | add_drop_rate_1       | Same getters with index 1, Special Resources          |
| `+0x10` | u32  | add_drop_count_rate_1 |                                                       |
| `+0x14` | u32  | add_drop_rate_2       | Same getters with index 2, Rare Resources             |
| `+0x18` | u32  | add_drop_count_rate_2 |                                                       |
| `+0x1C` | u32  | unknown_1c            | `500,000` in every row on client 3464                 |
| `+0x20` | u32  | unknown_20            | `0` in every row on client 3464                       |

The gathering tooltip in `panel_characterinfo_life_all_2.luac` calls
`ToClient_LoadCollectingStatData(subType)` for the hovered gathering type,
then reads `ToClient_getCollectingStatAddDropRate(ii)` and
`ToClient_getCollectingStatAddDropCountRate(ii)` for `ii` = 0 to count - 2
into `LUA_COLLECTING_POWER_DESC_1` to `_3` ("Basic Resources", "Special
Resources", "Rare Resources", each with "Drop rate +{rate1}%" and "Quantity
+{rate2}%"). Three tiers read up to count - 2 leave a fourth entry, and the
32 bytes after the mastery hold four (drop rate, quantity) pairs.

The pairs read in row order, not as four drop rates followed by four
quantities. With pairs, all six tooltip values are 0 at mastery 0 and rise
with mastery, as `LUA_COLLECTING_POWER_DESC_MAIN` says ("Higher Gathering
Mastery increases the gathered drop rate and quantity of basic, special, and
rare resources"). Read as two arrays, the rare quantity would be `+0x1C`,
`500,000` (+50%) at every mastery including 0 (client 3464). The fourth pair
(`+0x1C`, `+0x20`) is constant and nothing reads it. The in-game tooltips of
Lumbering, Fluid Collecting and Butchering at Gathering Mastery 440 show
Basic +80.00% / +50.49%, Special +25.25% / +12.62% and Rare +31.56% /
+10.52%, the mastery 400 row read as pairs (client 3464).

On client 3464 the basic drop rate is 0 at mastery 0 and 50 and `800,000`
(+80%) from 100 up; the other five values rise to 500%, 250%, 125%, 312.31%
and 105.80% at 3000.

The group index is the `subType`: the Life Skill tab names group `n` with
`_SUBLIFE_COLLECT_STRING[n]` in `panel_characterinfo_life_all.luac`, keys of
the `RESOURCE` sheet:

| Group | Key                                                  | Name (English LOC) |
| ----- | ---------------------------------------------------- | ------------------ |
| 1     | `PANEL_CHARACTERINFO_RENEW_WATERING_TITLE`            | Water Scooping     |
| 2     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FELLING`      | Lumbering          |
| 3     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SAP`          | Fluid Collecting   |
| 4     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HOMMY`        | Hoe Gathering      |
| 5     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SLAUGHTER`    | Butchering         |
| 6     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_TANNING`      | Tanning            |
| 7     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_MINING`       | Mining             |

The buff detail panel (`panel_characterinfo_buffdetail_all.luac`) passes
`__eCollectToolType_Axe` and the other tool types to the same
`ToClient_LoadCollectingStatData`, so the group index is also the
`CollectToolType`: `CppEnums.CollectToolTypeName` lists BareHands,
EmptyBottle, Axe, Syringe, Hoe, ButcheryKnife, SkinKnife and Pickax first,
and group 0 (bare hands) is empty. `LUA_COLLECTING_POWER_DESC_SUB_1` to `_7`
list the resources of each type ("Basic Resources: Timber, Plank, Log" for
group 2).

### `manufacturingstat.bss`

| Offset     | Type                    | Field        | Notes                                           |
| ---------- | ----------------------- | ------------ | ----------------------------------------------- |
| `+0x00`    | char[4]                 | magic        | ASCII `PABR`                                    |
| `+0x04`    | Processing Group[..table_start] | groups       | Groups back to back until `table_start`         |
| `EOF-0x0C` | u32                     | string_count | Always `0`                                      |
| `EOF-0x08` | u32                     | table_start  | Offset of `string_count`, where the groups end  |
| `EOF-0x04` | u32                     | zero         | Always `0`                                      |

### Processing Group (variable: 4 bytes + rows)

The same shape as the Gathering Group, with Processing Rows.

| Offset  | Type                  | Field | Notes                         |
| ------- | --------------------- | ----- | ----------------------------- |
| `+0x00` | u32                   | count | Number of rows in the group   |
| `+0x04` | Processing Row[count] | rows  | `count` rows                  |

### Processing Row (16 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | f32  | mastery    | Mastery threshold                                            |
| `+0x04` | u32  | unknown_04 | 1,000,000 x (1 - 10 / `count_rate`) in every row on client 3464 |
| `+0x08` | u32  | count_rate | `ToClient_getManufacturingStatCountRate(subType)`, mass processing batches |
| `+0x0C` | u32  | unknown_0c | `0` in every row on client 3464                              |

The processing tooltip fills `data2` of `LUA_MANUFACTURING_POWER_TOOLTIP_DESC`
("You can mass process {data2} batches of materials at once") with
`tostring(ToClient_getManufacturingStatCountRate(subType))`, and the
processing window (`panel_window_manufacture_all_2.luac`) puts the same
value in `LUA_MANUFACTURING_POWER_DESC` ("(Mass Process {count} times)").
`+0x08` is the only whole-number count in the row: `10` at mastery 1 up to
`315` at 2999 on client 3464. `+0x04` follows from it (`90,909` for 11
batches, `968,253` for 315), and no Lua reads a second processing value.

The rows run up: mastery `1.0`, then `19.0` to `779.0` in steps of 20, and
larger steps up to `2999.0` (client 3464). At Processing Mastery 480 every
type shows "(Mass Process 34 times)", the `479.0` row; the `499.0` row would
give 35, so the client takes the row at or below the mastery here too. The group index is the `subType`,
named by `_SUBLIFE_MANUFACTURE[n]`; the processing window passes its tab
index + 1:

| Group | Key                                                  | Name (English LOC) |
| ----- | ---------------------------------------------------- | ------------------ |
| 1     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SHAKING`      | Shaking            |
| 2     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_GRIDING`      | Grinding           |
| 3     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FIREWOOD`     | Chopping           |
| 4     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_DRYING`       | Drying             |
| 5     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_THINOUT`      | Filtering          |
| 6     | `PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HEATING`      | Heating            |

## Layout 1

On client 1784 `unknown_0c`, `unknown_14` and `unknown_1c` of the Alchemy
Row are u16, so the row is 34 bytes and each later field sits 2, 4 or 6 bytes
earlier. Only the Alchemy Row differs from Layout 2. Field names keep Layout
2's offsets, so `unknown_14` sits at `+0x0E` here.

### Alchemy Row (34 bytes)

| Offset  | Type | Field                 | Notes                                  |
| ------- | ---- | --------------------- | -------------------------------------- |
| `+0x00` | f32  | mastery               | Mastery threshold                      |
| `+0x04` | u32  | basic_max_drop_rate   |                                        |
| `+0x08` | u32  | add_royal_trade_bonus |                                        |
| `+0x0C` | u16  | unknown_0c            | `15690` in every row on client 1784    |
| `+0x0E` | u32  | event_drop_rate_0     |                                        |
| `+0x12` | u16  | unknown_14            | `15691` in every row on client 1784    |
| `+0x14` | u32  | event_drop_rate_1     |                                        |
| `+0x18` | u16  | unknown_1c            | `15692` in every row on client 1784    |
| `+0x1A` | u32  | event_drop_rate_2     |                                        |
| `+0x1E` | u32  | event_drop_rate       |                                        |

## Notes

- The handler is one class, `_bss/masterystatdata/handler.py`; the fields and
  columns of each file are a `MasteryTable` in `spec.py`. The type names
  resolve through the `stringtable.bss` key hashes stored in `sub_types.py`.
- The client takes the row at or below the player's mastery and does not
  interpolate: the in-game tooltips at Cooking 595, Hunting 405,
  Training 385, Gathering 440 and Processing 480 match the 550, 400, 350,
  400 and 479 rows exactly (client 3464); the 600 cooking row would give
  mass cooking 22.37% instead of 21.16%.
- Most curves change slope at mastery 2000: below it many values are perfect
  squares (Cooking `+0x0C` at 1200 is `78,400` = 280²), above it they rise by
  a fixed step per 50 mastery.
- `15690`, `15691` and `15692` in the Alchemy rows are not the extra items:
  item 15690 is "Glorious Crystal of Gallantry - Ah'krad", 15691 the Olucas
  crystal and 15692 "Resplendent Medal of Honor". They are not
  `itemsubgroup.dbss` keys, and `itemmaingroup.bss` holds none of them as a
  u32 or u16 at any byte offset, nor as ASCII digits (client 3464).
- bdo-data-extractor (`FORMATS.md`, "Life-skill mastery and level-effect
  tables") lists the eight shapes and the `1,000,000` = 100% scale, and calls
  the gathering pairs dropRate / quantityRate and the processing fields
  procRate / batchSize. The names here come from the client Lua instead.

## Open Questions

### The Alchemy Keys

`unknown_0c`, `unknown_14` and `unknown_1c` pair a constant (`15690` to
`15692`) with each event share. They read like keys of the basic, special
and rare extra item groups, but no decoded table holds them.

### The Sailing Cannon Fields And `unknown_04`

The enum names the four values from `+0x1C`, but they hold mastery / 50 like
`unknown_04`, not a rate, and no UI reads them. Whether sailing mastery
changes cannon stats is not shown anywhere in the client.

### The Processing Rate `unknown_04`

`unknown_04` in `manufacturingstat.bss` is 1 - 10 / batches, scaled to
1,000,000. It could be the share of processing time a mass process saves
over ten single runs, but no Lua or tooltip reads it.

### The Gathering Groups 8 To 18 And The Fourth Pair

`collectingstatdata.bss` ends with eleven empty groups after Mining. The
tool types after Pickax in `CppEnums.CollectToolTypeName` (Tweezers, Pray,
MagnifyingLens, MassStone, FishingChair, Whip, Oar, Reserve) are eight, not
eleven. The constant fourth pair (`unknown_1c`, `unknown_20`) has no reader.
