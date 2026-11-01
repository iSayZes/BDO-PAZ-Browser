# `sequence_skill.bss` and `cutscene_skill.bss` Format

## Purpose

Skill lists of tutorial sequences and cutscenes: per sequence or cutscene
file, and per class type, a list of skill numbers (`2831` Absolute: Slash
for the Warrior). A row names its file by the hash of the file name only.
Two files share the format:

| File                 | Rows name                                         |
| -------------------- | ------------------------------------------------- |
| `sequence_skill.bss` | Sequences under `sequence/` (`IllezraTutorial/CS_Tutorial_Illezra_00`) |
| `cutscene_skill.bss` | Cutscenes under `character/cutscene/` (`CS_Tutorial_00_Illezra_0008`) |

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records                | Row bytes               |
| ------ | -------------- | -------------------- | ----- | ---------------------- | ----------------------- |
| 1      | 1914 and later | `cutscene_skill.bss` | 4,955 | 93 Class Skills, 3 Row | 33 to 77, 53 on average |
| 1      | 2192 and later | `sequence_skill.bss` | 3,420 | 64 Class Skills, 2 Row | 33 to 77, 53 on average |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 1      | `cutscene_skill.bss` | 4,955 B (100.0%) | 0 B (0.0%) |
| 1      | `sequence_skill.bss` | 3,420 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `659f71c751d9`  |
| 3482   | Layout 1 | `659f71c751d9`  |
| 3474   | Layout 1 | `659f71c751d9`  |
| 3473   | Layout 1 | `659f71c751d9`  |
| 3464   | Layout 1 | `659f71c751d9`  |
| 3458   | Layout 1 | `659f71c751d9`  |
| 3454   | Layout 1 | `659f71c751d9`  |
| 3444   | Layout 1 | `659f71c751d9`  |
| 3435   | Layout 1 | `659f71c751d9`  |
| 3426   | Layout 1 | `659f71c751d9`  |
| 3418   | Layout 1 | `659f71c751d9`  |
| 3412   | Layout 1 | `659f71c751d9`  |
| 3402   | Layout 1 | `659f71c751d9`  |
| 3396   | Layout 1 | `659f71c751d9`  |
| 3387   | Layout 1 | `659f71c751d9`  |
| 3381   | Layout 1 | `659f71c751d9`  |
| 3373   | Layout 1 | `659f71c751d9`  |
| 3364   | Layout 1 | `659f71c751d9`  |
| 3356   | Layout 1 | `659f71c751d9`  |
| 3349   | Layout 1 | `659f71c751d9`  |
| 3342   | Layout 1 | `659f71c751d9`  |
| 3335   | Layout 1 | `659f71c751d9`  |
| 3326   | Layout 1 | `659f71c751d9`  |
| 3321   | Layout 1 | `659f71c751d9`  |
| 3314   | Layout 1 | `659f71c751d9`  |
| 3303   | Layout 1 | `659f71c751d9`  |
| 3302   | Layout 1 | `659f71c751d9`  |
| 3293   | Layout 1 | `659f71c751d9`  |
| 3283   | Layout 1 | `659f71c751d9`  |
| 3275   | Layout 1 | `659f71c751d9`  |
| 3267   | Layout 1 | `659f71c751d9`  |
| 3258   | Layout 1 | `659f71c751d9`  |
| 3251   | Layout 1 | `659f71c751d9`  |
| 3242   | Layout 1 | `659f71c751d9`  |
| 3235   | Layout 1 | `659f71c751d9`  |
| 3229   | Layout 1 | `659f71c751d9`  |
| 3212   | Layout 1 | `659f71c751d9`  |
| 3203   | Layout 1 | `659f71c751d9`  |
| 3193   | Layout 1 | `659f71c751d9`  |
| 3186   | Layout 1 | `659f71c751d9`  |
| 3177   | Layout 1 | `659f71c751d9`  |
| 3169   | Layout 1 | `659f71c751d9`  |
| 3158   | Layout 1 | `659f71c751d9`  |
| 3151   | Layout 1 | `659f71c751d9`  |
| 3144   | Layout 1 | `659f71c751d9`  |
| 3133   | Layout 1 | `659f71c751d9`  |
| 3125   | Layout 1 | `659f71c751d9`  |
| 3118   | Layout 1 | `659f71c751d9`  |
| 3111   | Layout 1 | `659f71c751d9`  |
| 3103   | Layout 1 | `659f71c751d9`  |
| 3095   | Layout 1 | `659f71c751d9`  |
| 3086   | Layout 1 | `659f71c751d9`  |
| 3072   | Layout 1 | `659f71c751d9`  |
| 3062   | Layout 1 | `659f71c751d9`  |
| 3052   | Layout 1 | `659f71c751d9`  |
| 3045   | Layout 1 | `659f71c751d9`  |
| 3037   | Layout 1 | `659f71c751d9`  |
| 3030   | Layout 1 | `659f71c751d9`  |
| 3021   | Layout 1 | `659f71c751d9`  |
| 3012   | Layout 1 | `659f71c751d9`  |
| 3002   | Layout 1 | `659f71c751d9`  |
| 2995   | Layout 1 | `659f71c751d9`  |
| 2987   | Layout 1 | `659f71c751d9`  |
| 2978   | Layout 1 | `659f71c751d9`  |
| 2970   | Layout 1 | `659f71c751d9`  |
| 2959   | Layout 1 | `659f71c751d9`  |
| 2951   | Layout 1 | `659f71c751d9`  |
| 2942   | Layout 1 | `659f71c751d9`  |
| 2935   | Layout 1 | `659f71c751d9`  |
| 2932   | Layout 1 | `659f71c751d9`  |
| 2923   | Layout 1 | `659f71c751d9`  |
| 2919   | Layout 1 | `659f71c751d9`  |
| 2907   | Layout 1 | `659f71c751d9`  |
| 2900   | Layout 1 | `659f71c751d9`  |
| 2891   | Layout 1 | `659f71c751d9`  |
| 2882   | Layout 1 | `659f71c751d9`  |
| 2872   | Layout 1 | `659f71c751d9`  |
| 2863   | Layout 1 | `659f71c751d9`  |
| 2855   | Layout 1 | `659f71c751d9`  |
| 2849   | Layout 1 | `659f71c751d9`  |
| 2844   | Layout 1 | `659f71c751d9`  |
| 2834   | Layout 1 | `659f71c751d9`  |
| 2825   | Layout 1 | `659f71c751d9`  |
| 2819   | Layout 1 | `659f71c751d9`  |
| 2811   | Layout 1 | `659f71c751d9`  |
| 2803   | Layout 1 | `659f71c751d9`  |
| 2794   | Layout 1 | `659f71c751d9`  |
| 2783   | Layout 1 | `659f71c751d9`  |
| 2774   | Layout 1 | `659f71c751d9`  |
| 2765   | Layout 1 | `659f71c751d9`  |
| 2756   | Layout 1 | `659f71c751d9`  |
| 2750   | Layout 1 | `659f71c751d9`  |
| 2743   | Layout 1 | `659f71c751d9`  |
| 2736   | Layout 1 | `659f71c751d9`  |
| 2726   | Layout 1 | `659f71c751d9`  |
| 2717   | Layout 1 | `659f71c751d9`  |
| 2709   | Layout 1 | `659f71c751d9`  |
| 2703   | Layout 1 | `659f71c751d9`  |
| 2695   | Layout 1 | `659f71c751d9`  |
| 2684   | Layout 1 | `659f71c751d9`  |
| 2672   | Layout 1 | `659f71c751d9`  |
| 2665   | Layout 1 | `659f71c751d9`  |
| 2657   | Layout 1 | `659f71c751d9`  |
| 2649   | Layout 1 | `659f71c751d9`  |
| 2644   | Layout 1 | `659f71c751d9`  |
| 2637   | Layout 1 | `659f71c751d9`  |
| 2629   | Layout 1 | `659f71c751d9`  |
| 2619   | Layout 1 | `659f71c751d9`  |
| 2612   | Layout 1 | `659f71c751d9`  |
| 2606   | Layout 1 | `659f71c751d9`  |
| 2602   | Layout 1 | `659f71c751d9`  |
| 2601   | Layout 1 | `659f71c751d9`  |
| 2592   | Layout 1 | `659f71c751d9`  |
| 2583   | Layout 1 | `659f71c751d9`  |
| 2575   | Layout 1 | `659f71c751d9`  |
| 2567   | Layout 1 | `659f71c751d9`  |
| 2560   | Layout 1 | `659f71c751d9`  |
| 2553   | Layout 1 | `659f71c751d9`  |
| 2545   | Layout 1 | `659f71c751d9`  |
| 2538   | Layout 1 | `659f71c751d9`  |
| 2529   | Layout 1 | `659f71c751d9`  |
| 2519   | Layout 1 | `659f71c751d9`  |
| 2513   | Layout 1 | `659f71c751d9`  |
| 2510   | Layout 1 | `659f71c751d9`  |
| 2507   | Layout 1 | `659f71c751d9`  |
| 2503   | Layout 1 | `659f71c751d9`  |
| 2498   | Layout 1 | `659f71c751d9`  |
| 2492   | Layout 1 | `659f71c751d9`  |
| 2487   | Layout 1 | `659f71c751d9`  |
| 2480   | Layout 1 | `659f71c751d9`  |
| 2474   | Layout 1 | `659f71c751d9`  |
| 2468   | Layout 1 | `659f71c751d9`  |
| 2460   | Layout 1 | `659f71c751d9`  |
| 2453   | Layout 1 | `659f71c751d9`  |
| 2444   | Layout 1 | `659f71c751d9`  |
| 2438   | Layout 1 | `659f71c751d9`  |
| 2434   | Layout 1 | `659f71c751d9`  |
| 2429   | Layout 1 | `659f71c751d9`  |
| 2421   | Layout 1 | `659f71c751d9`  |
| 2414   | Layout 1 | `659f71c751d9`  |
| 2407   | Layout 1 | `659f71c751d9`  |
| 2401   | Layout 1 | `659f71c751d9`  |
| 2397   | Layout 1 | `659f71c751d9`  |
| 2393   | Layout 1 | `659f71c751d9`  |
| 2384   | Layout 1 | `659f71c751d9`  |
| 2378   | Layout 1 | `659f71c751d9`  |
| 2372   | Layout 1 | `659f71c751d9`  |
| 2358   | Layout 1 | `659f71c751d9`  |
| 2352   | Layout 1 | `659f71c751d9`  |
| 2347   | Layout 1 | `659f71c751d9`  |
| 2343   | Layout 1 | `659f71c751d9`  |
| 2335   | Layout 1 | `659f71c751d9`  |
| 2327   | Layout 1 | `659f71c751d9`  |
| 2324   | Layout 1 | `659f71c751d9`  |
| 2319   | Layout 1 | `659f71c751d9`  |
| 2313   | Layout 1 | `659f71c751d9`  |
| 2308   | Layout 1 | `659f71c751d9`  |
| 2302   | Layout 1 | `659f71c751d9`  |
| 2295   | Layout 1 | `659f71c751d9`  |
| 2290   | Layout 1 | `659f71c751d9`  |
| 2284   | Layout 1 | `659f71c751d9`  |
| 2276   | Layout 1 | `659f71c751d9`  |
| 2269   | Layout 1 | `659f71c751d9`  |
| 2259   | Layout 1 | `659f71c751d9`  |
| 2250   | Layout 1 | `659f71c751d9`  |
| 2243   | Layout 1 | `659f71c751d9`  |
| 2235   | Layout 1 | `659f71c751d9`  |
| 2229   | Layout 1 | `659f71c751d9`  |
| 2224   | Layout 1 | `659f71c751d9`  |
| 2218   | Layout 1 | `659f71c751d9`  |
| 2215   | Layout 1 | `659f71c751d9`  |
| 2207   | Layout 1 | `659f71c751d9`  |
| 2203   | Layout 1 | `659f71c751d9`  |
| 2196   | Layout 1 | `659f71c751d9`  |
| 2192   | Layout 1 | `659f71c751d9`  |
| 2189   | Layout 1 | `659f71c751d9`  |
| 2183   | Layout 1 | `659f71c751d9`  |
| 2179   | Layout 1 | `659f71c751d9`  |
| 2171   | Layout 1 | `659f71c751d9`  |
| 2163   | Layout 1 | `659f71c751d9`  |
| 2156   | Layout 1 | `659f71c751d9`  |
| 2151   | Layout 1 | `659f71c751d9`  |
| 2147   | Layout 1 | `659f71c751d9`  |
| 2142   | Layout 1 | `659f71c751d9`  |
| 2138   | Layout 1 | `659f71c751d9`  |
| 2134   | Layout 1 | `659f71c751d9`  |
| 2130   | Layout 1 | `659f71c751d9`  |
| 2122   | Layout 1 | `659f71c751d9`  |
| 2107   | Layout 1 | `659f71c751d9`  |
| 2098   | Layout 1 | `659f71c751d9`  |
| 2089   | Layout 1 | `659f71c751d9`  |
| 2081   | Layout 1 | `659f71c751d9`  |
| 2073   | Layout 1 | `659f71c751d9`  |
| 2067   | Layout 1 | `659f71c751d9`  |
| 2063   | Layout 1 | `659f71c751d9`  |
| 2059   | Layout 1 | `659f71c751d9`  |
| 2052   | Layout 1 | `659f71c751d9`  |
| 2044   | Layout 1 | `659f71c751d9`  |
| 2039   | Layout 1 | `659f71c751d9`  |
| 2032   | Layout 1 | `659f71c751d9`  |
| 2025   | Layout 1 | `659f71c751d9`  |
| 2011   | Layout 1 | `659f71c751d9`  |
| 2005   | Layout 1 | `659f71c751d9`  |
| 2000   | Layout 1 | `659f71c751d9`  |
| 1996   | Layout 1 | `659f71c751d9`  |
| 1991   | Layout 1 | `659f71c751d9`  |
| 1985   | Layout 1 | `659f71c751d9`  |
| 1980   | Layout 1 | `659f71c751d9`  |
| 1969   | Layout 1 | `659f71c751d9`  |
| 1964   | Layout 1 | `659f71c751d9`  |
| 1958   | Layout 1 | `659f71c751d9`  |
| 1950   | Layout 1 | `659f71c751d9`  |
| 1945   | Layout 1 | `659f71c751d9`  |
| 1937   | Layout 1 | `659f71c751d9`  |
| 1933   | Layout 1 | `659f71c751d9`  |
| 1927   | Layout 1 | `659f71c751d9`  |
| 1921   | Layout 1 | `659f71c751d9`  |
| 1914   | Layout 1 | `659f71c751d9`  |
| 1908   | No file  | `659f71c751d9`  |
| 1897   | No file  | `659f71c751d9`  |
| 1892   | No file  | `659f71c751d9`  |
| 1886   | No file  | `659f71c751d9`  |
| 1881   | No file  | `659f71c751d9`  |
| 1871   | No file  | `659f71c751d9`  |
| 1866   | No file  | `659f71c751d9`  |
| 1862   | No file  | `659f71c751d9`  |
| 1854   | No file  | `659f71c751d9`  |
| 1846   | No file  | `659f71c751d9`  |
| 1838   | No file  | `659f71c751d9`  |
| 1832   | No file  | `659f71c751d9`  |
| 1826   | No file  | `659f71c751d9`  |
| 1822   | No file  | `659f71c751d9`  |
| 1818   | No file  | `659f71c751d9`  |
| 1804   | No file  | `659f71c751d9`  |
| 1794   | No file  | `659f71c751d9`  |
| 1790   | No file  | `659f71c751d9`  |
| 1784   | No file  | `659f71c751d9`  |
| 1774   | No file  | `659f71c751d9`  |
| 1771   | No file  | `659f71c751d9`  |
| 1762   | No file  | `659f71c751d9`  |
| 1759   | No file  | `659f71c751d9`  |
| 1754   | No file  | `659f71c751d9`  |
| 1749   | No file  | `659f71c751d9`  |
| 1743   | No file  | `659f71c751d9`  |
| 1737   | No file  | `659f71c751d9`  |
| 1731   | No file  | `659f71c751d9`  |
| 1725   | No file  | `659f71c751d9`  |
| 1717   | No file  | `659f71c751d9`  |
| 1710   | No file  | `659f71c751d9`  |
| 1704   | No file  | `659f71c751d9`  |
| 1698   | No file  | `659f71c751d9`  |
| 1690   | No file  | `659f71c751d9`  |
| 1685   | No file  | `659f71c751d9`  |
| 1680   | No file  | `659f71c751d9`  |
| 1674   | No file  | `659f71c751d9`  |
| 1668   | No file  | `659f71c751d9`  |
| 1659   | No file  | `659f71c751d9`  |
| 1649   | No file  | `659f71c751d9`  |
| 1642   | No file  | `659f71c751d9`  |
| 1636   | No file  | `659f71c751d9`  |
| 1628   | No file  | `659f71c751d9`  |
| 1622   | No file  | `659f71c751d9`  |
| 1614   | No file  | `659f71c751d9`  |
| 1608   | No file  | `659f71c751d9`  |
| 1602   | No file  | `659f71c751d9`  |
| 1598   | No file  | `659f71c751d9`  |
| 1594   | No file  | `659f71c751d9`  |
| 1590   | No file  | `659f71c751d9`  |
| 1587   | No file  | `659f71c751d9`  |
| 1584   | No file  | `659f71c751d9`  |
| 1579   | No file  | `659f71c751d9`  |
| 1572   | No file  | `659f71c751d9`  |
| 1565   | No file  | `659f71c751d9`  |
| 1559   | No file  | `659f71c751d9`  |
| 1554   | No file  | `659f71c751d9`  |
| 1547   | No file  | `659f71c751d9`  |
| 1537   | No file  | `659f71c751d9`  |
| 1529   | No file  | `659f71c751d9`  |
| 1524   | No file  | `659f71c751d9`  |
| 1519   | No file  | `659f71c751d9`  |
| 1509   | No file  | `659f71c751d9`  |
| 1506   | No file  | `659f71c751d9`  |
| 1504   | No file  | `659f71c751d9`  |
| 1500   | No file  | `659f71c751d9`  |
| 1493   | No file  | `659f71c751d9`  |
| 1489   | No file  | `659f71c751d9`  |
| 1485   | No file  | `659f71c751d9`  |
| 1481   | No file  | `659f71c751d9`  |
| 1474   | No file  | `659f71c751d9`  |
| 1466   | No file  | `659f71c751d9`  |
| 1462   | No file  | `659f71c751d9`  |
| 1459   | No file  | `659f71c751d9`  |
| 1453   | No file  | `659f71c751d9`  |
| 1450   | No file  | `659f71c751d9`  |
| 1445   | No file  | `659f71c751d9`  |
| 1439   | No file  | `659f71c751d9`  |
| 1433   | No file  | `659f71c751d9`  |
| 1430   | No file  | `659f71c751d9`  |
| 1426   | No file  | `659f71c751d9`  |
| 1421   | No file  | `659f71c751d9`  |
| 1417   | No file  | `659f71c751d9`  |
| 1416   | No file  | `659f71c751d9`  |
| 1409   | No file  | `659f71c751d9`  |
| 1405   | No file  | `659f71c751d9`  |
| 1401   | No file  | `659f71c751d9`  |
| 1396   | No file  | `659f71c751d9`  |
| 1391   | No file  | `659f71c751d9`  |
| 1390   | No file  | `659f71c751d9`  |
| 1386   | No file  | `659f71c751d9`  |
| 1381   | No file  | `659f71c751d9`  |
| 1379   | No file  | `659f71c751d9`  |
| 1372   | No file  | `659f71c751d9`  |
| 1366   | No file  | `659f71c751d9`  |
| 1364   | No file  | `659f71c751d9`  |
| 1363   | No file  | `659f71c751d9`  |
| 1360   | No file  | `659f71c751d9`  |
| 1358   | No file  | `659f71c751d9`  |
| 1355   | No file  | `659f71c751d9`  |
| 1351   | No file  | `659f71c751d9`  |
| 1348   | No file  | `659f71c751d9`  |
| 1346   | No file  | `659f71c751d9`  |
| 1341   | No file  | `659f71c751d9`  |
| 1340   | No file  | `659f71c751d9`  |
| 1338   | No file  | `659f71c751d9`  |
| 1335   | No file  | `659f71c751d9`  |
| 1333   | No file  | `659f71c751d9`  |
| 1329   | No file  | `659f71c751d9`  |
| 1327   | No file  | `659f71c751d9`  |
| 1324   | No file  | `659f71c751d9`  |
| 1321   | No file  | `659f71c751d9`  |
| 1319   | No file  | `659f71c751d9`  |
| 1318   | No file  | `659f71c751d9`  |
| 1316   | No file  | `659f71c751d9`  |
| 1313   | No file  | `659f71c751d9`  |
| 1311   | No file  | `659f71c751d9`  |
| 1309   | No file  | `659f71c751d9`  |
| 1304   | No file  | `659f71c751d9`  |
| 1292   | No file  | `659f71c751d9`  |
| 1286   | No file  | `659f71c751d9`  |
| 1280   | No file  | `659f71c751d9`  |
| 1276   | No file  | `659f71c751d9`  |
| 1267   | No file  | `659f71c751d9`  |
| 1261   | No file  | `659f71c751d9`  |
| 1256   | No file  | `659f71c751d9`  |
| 1250   | No file  | `659f71c751d9`  |
| 1246   | No file  | `659f71c751d9`  |
| 1239   | No file  | `659f71c751d9`  |
| 1230   | No file  | `659f71c751d9`  |
| 1226   | No file  | `659f71c751d9`  |
| 1220   | No file  | `659f71c751d9`  |
| 1217   | No file  | `659f71c751d9`  |
| 1211   | No file  | `659f71c751d9`  |
| 1210   | No file  | `659f71c751d9`  |
| 1208   | No file  | `659f71c751d9`  |
| 1203   | No file  | `659f71c751d9`  |
| 1197   | No file  | `659f71c751d9`  |
| 1194   | No file  | `659f71c751d9`  |
| 1192   | No file  | `659f71c751d9`  |
| 1187   | No file  | `659f71c751d9`  |
| 1183   | No file  | `659f71c751d9`  |
| 1177   | No file  | `659f71c751d9`  |
| 1173   | No file  | `659f71c751d9`  |
| 1167   | No file  | `659f71c751d9`  |
| 1164   | No file  | `659f71c751d9`  |
| 1156   | No file  | `659f71c751d9`  |
| 1149   | No file  | `659f71c751d9`  |
| 1144   | No file  | `659f71c751d9`  |
| 1137   | No file  | `659f71c751d9`  |
| 1132   | No file  | `659f71c751d9`  |
| 1127   | No file  | `659f71c751d9`  |
| 1122   | No file  | `659f71c751d9`  |
| 1118   | No file  | `659f71c751d9`  |
| 1114   | No file  | `659f71c751d9`  |
| 1109   | No file  | `659f71c751d9`  |
| 1102   | No file  | `659f71c751d9`  |
| 1096   | No file  | `659f71c751d9`  |
| 1088   | No file  | `659f71c751d9`  |
| 1081   | No file  | `659f71c751d9`  |
| 1076   | No file  | `659f71c751d9`  |
| 1069   | No file  | `659f71c751d9`  |
| 1064   | No file  | `659f71c751d9`  |
| 1058   | No file  | `659f71c751d9`  |
| 1051   | No file  | `659f71c751d9`  |
| 1044   | No file  | `659f71c751d9`  |
| 1036   | No file  | `659f71c751d9`  |
| 1026   | No file  | `659f71c751d9`  |
| 1016   | No file  | `659f71c751d9`  |
| 1009   | No file  | `659f71c751d9`  |
| 1005   | No file  | `659f71c751d9`  |
| 1000   | No file  | `659f71c751d9`  |
| 998    | No file  | `659f71c751d9`  |
| 990    | No file  | `659f71c751d9`  |
| 979    | No file  | `659f71c751d9`  |
| 972    | No file  | `659f71c751d9`  |
| 963    | No file  | `659f71c751d9`  |
| 955    | No file  | `659f71c751d9`  |
| 946    | No file  | `659f71c751d9`  |
| 938    | No file  | `659f71c751d9`  |
| 927    | No file  | `659f71c751d9`  |
| 911    | No file  | `659f71c751d9`  |
| 904    | No file  | `659f71c751d9`  |
| 899    | No file  | `659f71c751d9`  |
| 894    | No file  | `659f71c751d9`  |
| 885    | No file  | `659f71c751d9`  |
| 879    | No file  | `659f71c751d9`  |
| 872    | No file  | `659f71c751d9`  |
| 864    | No file  | `659f71c751d9`  |
| 855    | No file  | `659f71c751d9`  |
| 853    | No file  | `659f71c751d9`  |
| 845    | No file  | `659f71c751d9`  |
| 837    | No file  | `659f71c751d9`  |
| 829    | No file  | `659f71c751d9`  |
| 822    | No file  | `659f71c751d9`  |
| 814    | No file  | `659f71c751d9`  |
| 805    | No file  | `659f71c751d9`  |
| 794    | No file  | `659f71c751d9`  |
| 787    | No file  | `659f71c751d9`  |
| 780    | No file  | `659f71c751d9`  |
| 771    | No file  | `659f71c751d9`  |
| 760    | No file  | `659f71c751d9`  |
| 748    | No file  | `659f71c751d9`  |
| 741    | No file  | `659f71c751d9`  |
| 736    | No file  | `659f71c751d9`  |
| 731    | No file  | `659f71c751d9`  |
| 723    | No file  | `659f71c751d9`  |
| 711    | No file  | `659f71c751d9`  |
| 707    | No file  | `659f71c751d9`  |
| 697    | No file  | `659f71c751d9`  |
| 689    | No file  | `659f71c751d9`  |
| 683    | No file  | `659f71c751d9`  |
| 678    | No file  | `659f71c751d9`  |
| 670    | No file  | `659f71c751d9`  |
| 661    | No file  | `659f71c751d9`  |
| 656    | No file  | `659f71c751d9`  |
| 652    | No file  | `659f71c751d9`  |
| 643    | No file  | `659f71c751d9`  |
| 637    | No file  | `659f71c751d9`  |
| 630    | No file  | `659f71c751d9`  |
| 627    | No file  | `659f71c751d9`  |
| 621    | No file  | `659f71c751d9`  |
| 617    | No file  | `659f71c751d9`  |
| 615    | No file  | `659f71c751d9`  |
| 606    | No file  | `659f71c751d9`  |
| 599    | No file  | `659f71c751d9`  |
| 592    | No file  | `659f71c751d9`  |
| 586    | No file  | `659f71c751d9`  |
| 577    | No file  | `659f71c751d9`  |
| 569    | No file  | `659f71c751d9`  |
| 561    | No file  | `659f71c751d9`  |
| 554    | No file  | `659f71c751d9`  |
| 542    | No file  | `659f71c751d9`  |
| 532    | No file  | `659f71c751d9`  |
| 531    | No file  | `659f71c751d9`  |
| 526    | No file  | `659f71c751d9`  |
| 521    | No file  | `659f71c751d9`  |
| 517    | No file  | `659f71c751d9`  |
| 510    | No file  | `659f71c751d9`  |
| 508    | No file  | `659f71c751d9`  |
| 504    | No file  | `659f71c751d9`  |
| 497    | No file  | `659f71c751d9`  |
| 491    | No file  | `659f71c751d9`  |
| 485    | No file  | `659f71c751d9`  |
| 478    | No file  | `659f71c751d9`  |
| 472    | No file  | `659f71c751d9`  |
| 466    | No file  | `659f71c751d9`  |
| 457    | No file  | `659f71c751d9`  |
| 452    | No file  | `659f71c751d9`  |
| 449    | No file  | `659f71c751d9`  |
| 435    | No file  | `659f71c751d9`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                                              |
| -------------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `sequencetriggerdata.bss`        | Optional | For `sequence_skill.bss`: sequence folder and file name by hash ([format](sequencetriggerdata_bss.md)) |
| `cutscenetutorial_equipment.bss` | Optional | For `cutscene_skill.bss`: cutscene file names by hash ([format](tutorial_equipment_bss.md))       |
| `languagedata_en.loc`            | Optional | Class names (type `21`) and skill names (type `10`)                                               |

A hash the companion does not hold shows without a name.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | Empty                                         |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 8 bytes + class lists)

| Offset  | Type                       | Field          | Notes                                                                                                      |
| ------- | -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32                        | file_name_hash | ASCII key hash (lookup3, seed `0xC5EDE`) of the sequence or cutscene file name without `.pas`; see File Names |
| `+0x04` | u32                        | class_count    | Number of `classes`                                                                                        |
| `+0x08` | Class Skills[class_count]  | classes        | See Class Skills                                                                                           |

### Class Skills (variable: 9 bytes + skill numbers)

| Offset  | Type               | Field       | Notes                                                           |
| ------- | ------------------ | ----------- | --------------------------------------------------------------- |
| `+0x00` | u8                 | class_type  | Class type (`0` Warrior, LOC type 21); once per row             |
| `+0x01` | u64                | skill_count | Number of `skill_nos`                                           |
| `+0x09` | u16[skill_count]   | skill_nos   | Skill numbers (LOC type 10, `skill.dbss` `skill_no`), in no order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## File Names

The rows of client 3482 and the names their hashes match. Every
`sequence_skill.bss` hash is the `file_name_hash` of a
`sequencetriggerdata.bss` row, which holds the sequence's folder and file
name; the handler joins them with `/`, as the Sequence File column of
that table does. A `cutscene_skill.bss` hash has no trigger row. One is
in `cutscenetutorial_equipment.bss`; the other two match no table and
were found by hashing the `character/cutscene/` file names of the PAZ
index, which are lower case, with the case the other tables of the family
use (`CS_Tutorial_00_IllezraCH_0008`). The handler shows those two
without a name.

| File                 | `file_name_hash` | File name                                | Classes | Named by                         |
| -------------------- | ---------------- | ---------------------------------------- | ------- | -------------------------------- |
| `sequence_skill.bss` | `0xDEFE7AE1`     | `IllezraTutorial/CS_Tutorial_Illezra_00` | 32      | `sequencetriggerdata.bss`        |
| `sequence_skill.bss` | `0x4B724300`     | `IllezraTutorial/CS_Tutorial_Illezra_01` | 32      | `sequencetriggerdata.bss`        |
| `cutscene_skill.bss` | `0x90DDA72B`     | `CS_Test_00_Skill_0001`                  | 31      | PAZ index only                   |
| `cutscene_skill.bss` | `0xB5DDE516`     | `CS_Tutorial_00_Illezra_0008`            | 31      | `cutscenetutorial_equipment.bss` |
| `cutscene_skill.bss` | `0xA1DE7B15`     | `CS_Tutorial_00_IllezraCH_0008`          | 31      | PAZ index only                   |

The two sequences are also rows of `sequencetutorial_equipment.bss`, which
stores them as `CS_Tutorial_Illezra_00.pas` and `CS_Tutorial_Illezra_01.pas`.
The trigger table holds both hashes on client 2421 and every later client
searched, and the handler reads every layout of it, so the rows show their
sequence from client 2421 on. Clients 2401 to 2414 hold neither hash;
there the rows show without a name.

## Notes

- On client 3482 every row of one file holds the same lists. The two files
  differ in a few classes: `cutscene_skill.bss` has no class type `3`
  (Wukong), and its lists for class types `2`, `28` and `35` add or drop
  one or two skills.
- A list may repeat a skill: class type `21` lists `3183` twice in both
  files (client 3482).
- Neither file is in client 1784, and no sheet of a private server's
  `DataSheets.bexcel` on that client named for sequences, cutscenes or
  tutorials holds skill lists.
- The client Lua has a skill command panel for each kind:
  `panel_sequence_skillcommandguide.luac` calls
  `ToClient_RequestCommandListForSequence()` and
  `ui_widget_skillcommand_cutscene.luac` calls
  `ToClient_RequestCommandListForCutscene()`. The client answers with one
  `FromClient_SkillCommandList_Sequence(skillNo, isAwaken)` or
  `FromClient_SkillCommandList_Cutscene(skillNo, isAwaken)` event per
  skill, and the panel lists each skill's name and key command.

## In-Game Checks

### The Skill Lists Fill the Tutorial Skill Panel

Needs class: Warrior

Checks whether the skill command panel of the Illezra tutorial shows this
table's Warrior list.

1. Create a Warrior and play the tutorial up to the first fight in the
   Illezra sequence.
2. Read the skill names in the skill command panel right of the screen
   centre.

Expected result: the panel names skills from the Warrior list of
`0xDEFE7AE1` in `sequence_skill.bss` (Absolute: Slash, Prime: Heavy
Strike III). Other skills mean the panel reads its list elsewhere.
