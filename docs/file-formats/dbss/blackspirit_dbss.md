# `blackspirit.dbss` Format

## Purpose

The Black Spirit forms (looks) a character can pick at the Black Spirit's
skin select window, and the condition script that unlocks each: one row per
form, a u8 index and a UTF-16 condition. Form `0` has no condition; the
others ask for cleared quests (`clearQuest(122,5);`) or a level
(`getLevel()>92;`), with `<or>` between alternatives. On client 3482 the
file holds 15 forms, `0` to `7` and `10` to `16` (10 on client 1784).
Companion `blackspiritoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records       | Row bytes                |
| ------ | -------------- | ------------------------ | ----- | ------------- | ------------------------ |
| 1      | 1280 and later | `blackspirit.dbss`       | 2,971 | 15 Row        | 9 to 693, 198 on average |
| 1      | 1280 and later | `blackspiritoffset.dbss` | 139   | 15 Offset Row | 9                        |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `blackspirit.dbss`       | 2,971 B (100.0%) | 0 B (0.0%) |
| 1      | `blackspiritoffset.dbss` | 139 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fe4fa7411ca3`  |
| 3482   | Layout 1 | `fe4fa7411ca3`  |
| 3474   | Layout 1 | `fe4fa7411ca3`  |
| 3473   | Layout 1 | `fe4fa7411ca3`  |
| 3464   | Layout 1 | `fe4fa7411ca3`  |
| 3458   | Layout 1 | `fe4fa7411ca3`  |
| 3454   | Layout 1 | `fe4fa7411ca3`  |
| 3444   | Layout 1 | `fe4fa7411ca3`  |
| 3435   | Layout 1 | `fe4fa7411ca3`  |
| 3426   | Layout 1 | `fe4fa7411ca3`  |
| 3418   | Layout 1 | `fe4fa7411ca3`  |
| 3412   | Layout 1 | `fe4fa7411ca3`  |
| 3402   | Layout 1 | `fe4fa7411ca3`  |
| 3396   | Layout 1 | `fe4fa7411ca3`  |
| 3387   | Layout 1 | `fe4fa7411ca3`  |
| 3381   | Layout 1 | `fe4fa7411ca3`  |
| 3373   | Layout 1 | `fe4fa7411ca3`  |
| 3364   | Layout 1 | `fe4fa7411ca3`  |
| 3356   | Layout 1 | `fe4fa7411ca3`  |
| 3349   | Layout 1 | `fe4fa7411ca3`  |
| 3342   | Layout 1 | `fe4fa7411ca3`  |
| 3335   | Layout 1 | `fe4fa7411ca3`  |
| 3326   | Layout 1 | `fe4fa7411ca3`  |
| 3321   | Layout 1 | `fe4fa7411ca3`  |
| 3314   | Layout 1 | `fe4fa7411ca3`  |
| 3303   | Layout 1 | `fe4fa7411ca3`  |
| 3302   | Layout 1 | `fe4fa7411ca3`  |
| 3293   | Layout 1 | `fe4fa7411ca3`  |
| 3283   | Layout 1 | `fe4fa7411ca3`  |
| 3275   | Layout 1 | `fe4fa7411ca3`  |
| 3267   | Layout 1 | `fe4fa7411ca3`  |
| 3258   | Layout 1 | `fe4fa7411ca3`  |
| 3251   | Layout 1 | `fe4fa7411ca3`  |
| 3242   | Layout 1 | `fe4fa7411ca3`  |
| 3235   | Layout 1 | `fe4fa7411ca3`  |
| 3229   | Layout 1 | `fe4fa7411ca3`  |
| 3212   | Layout 1 | `fe4fa7411ca3`  |
| 3203   | Layout 1 | `fe4fa7411ca3`  |
| 3193   | Layout 1 | `fe4fa7411ca3`  |
| 3186   | Layout 1 | `fe4fa7411ca3`  |
| 3177   | Layout 1 | `fe4fa7411ca3`  |
| 3169   | Layout 1 | `fe4fa7411ca3`  |
| 3158   | Layout 1 | `fe4fa7411ca3`  |
| 3151   | Layout 1 | `fe4fa7411ca3`  |
| 3144   | Layout 1 | `fe4fa7411ca3`  |
| 3133   | Layout 1 | `fe4fa7411ca3`  |
| 3125   | Layout 1 | `fe4fa7411ca3`  |
| 3118   | Layout 1 | `fe4fa7411ca3`  |
| 3111   | Layout 1 | `fe4fa7411ca3`  |
| 3103   | Layout 1 | `fe4fa7411ca3`  |
| 3095   | Layout 1 | `fe4fa7411ca3`  |
| 3086   | Layout 1 | `fe4fa7411ca3`  |
| 3072   | Layout 1 | `fe4fa7411ca3`  |
| 3062   | Layout 1 | `fe4fa7411ca3`  |
| 3052   | Layout 1 | `fe4fa7411ca3`  |
| 3045   | Layout 1 | `fe4fa7411ca3`  |
| 3037   | Layout 1 | `fe4fa7411ca3`  |
| 3030   | Layout 1 | `fe4fa7411ca3`  |
| 3021   | Layout 1 | `fe4fa7411ca3`  |
| 3012   | Layout 1 | `fe4fa7411ca3`  |
| 3002   | Layout 1 | `fe4fa7411ca3`  |
| 2995   | Layout 1 | `fe4fa7411ca3`  |
| 2987   | Layout 1 | `fe4fa7411ca3`  |
| 2978   | Layout 1 | `fe4fa7411ca3`  |
| 2970   | Layout 1 | `fe4fa7411ca3`  |
| 2959   | Layout 1 | `fe4fa7411ca3`  |
| 2951   | Layout 1 | `fe4fa7411ca3`  |
| 2942   | Layout 1 | `fe4fa7411ca3`  |
| 2935   | Layout 1 | `fe4fa7411ca3`  |
| 2932   | Layout 1 | `fe4fa7411ca3`  |
| 2923   | Layout 1 | `fe4fa7411ca3`  |
| 2919   | Layout 1 | `fe4fa7411ca3`  |
| 2907   | Layout 1 | `fe4fa7411ca3`  |
| 2900   | Layout 1 | `fe4fa7411ca3`  |
| 2891   | Layout 1 | `fe4fa7411ca3`  |
| 2882   | Layout 1 | `fe4fa7411ca3`  |
| 2872   | Layout 1 | `fe4fa7411ca3`  |
| 2863   | Layout 1 | `fe4fa7411ca3`  |
| 2855   | Layout 1 | `fe4fa7411ca3`  |
| 2849   | Layout 1 | `fe4fa7411ca3`  |
| 2844   | Layout 1 | `fe4fa7411ca3`  |
| 2834   | Layout 1 | `fe4fa7411ca3`  |
| 2825   | Layout 1 | `fe4fa7411ca3`  |
| 2819   | Layout 1 | `fe4fa7411ca3`  |
| 2811   | Layout 1 | `fe4fa7411ca3`  |
| 2803   | Layout 1 | `fe4fa7411ca3`  |
| 2794   | Layout 1 | `fe4fa7411ca3`  |
| 2783   | Layout 1 | `fe4fa7411ca3`  |
| 2774   | Layout 1 | `fe4fa7411ca3`  |
| 2765   | Layout 1 | `fe4fa7411ca3`  |
| 2756   | Layout 1 | `fe4fa7411ca3`  |
| 2750   | Layout 1 | `fe4fa7411ca3`  |
| 2743   | Layout 1 | `fe4fa7411ca3`  |
| 2736   | Layout 1 | `fe4fa7411ca3`  |
| 2726   | Layout 1 | `fe4fa7411ca3`  |
| 2717   | Layout 1 | `fe4fa7411ca3`  |
| 2709   | Layout 1 | `fe4fa7411ca3`  |
| 2703   | Layout 1 | `fe4fa7411ca3`  |
| 2695   | Layout 1 | `fe4fa7411ca3`  |
| 2684   | Layout 1 | `fe4fa7411ca3`  |
| 2672   | Layout 1 | `fe4fa7411ca3`  |
| 2665   | Layout 1 | `fe4fa7411ca3`  |
| 2657   | Layout 1 | `fe4fa7411ca3`  |
| 2649   | Layout 1 | `fe4fa7411ca3`  |
| 2644   | Layout 1 | `fe4fa7411ca3`  |
| 2637   | Layout 1 | `fe4fa7411ca3`  |
| 2629   | Layout 1 | `fe4fa7411ca3`  |
| 2619   | Layout 1 | `fe4fa7411ca3`  |
| 2612   | Layout 1 | `fe4fa7411ca3`  |
| 2606   | Layout 1 | `fe4fa7411ca3`  |
| 2602   | Layout 1 | `fe4fa7411ca3`  |
| 2601   | Layout 1 | `fe4fa7411ca3`  |
| 2592   | Layout 1 | `fe4fa7411ca3`  |
| 2583   | Layout 1 | `fe4fa7411ca3`  |
| 2575   | Layout 1 | `fe4fa7411ca3`  |
| 2567   | Layout 1 | `fe4fa7411ca3`  |
| 2560   | Layout 1 | `fe4fa7411ca3`  |
| 2553   | Layout 1 | `fe4fa7411ca3`  |
| 2545   | Layout 1 | `fe4fa7411ca3`  |
| 2538   | Layout 1 | `fe4fa7411ca3`  |
| 2529   | Layout 1 | `fe4fa7411ca3`  |
| 2519   | Layout 1 | `fe4fa7411ca3`  |
| 2513   | Layout 1 | `fe4fa7411ca3`  |
| 2510   | Layout 1 | `fe4fa7411ca3`  |
| 2507   | Layout 1 | `fe4fa7411ca3`  |
| 2503   | Layout 1 | `fe4fa7411ca3`  |
| 2498   | Layout 1 | `fe4fa7411ca3`  |
| 2492   | Layout 1 | `fe4fa7411ca3`  |
| 2487   | Layout 1 | `fe4fa7411ca3`  |
| 2480   | Layout 1 | `fe4fa7411ca3`  |
| 2474   | Layout 1 | `fe4fa7411ca3`  |
| 2468   | Layout 1 | `fe4fa7411ca3`  |
| 2460   | Layout 1 | `fe4fa7411ca3`  |
| 2453   | Layout 1 | `fe4fa7411ca3`  |
| 2444   | Layout 1 | `fe4fa7411ca3`  |
| 2438   | Layout 1 | `fe4fa7411ca3`  |
| 2434   | Layout 1 | `fe4fa7411ca3`  |
| 2429   | Layout 1 | `fe4fa7411ca3`  |
| 2421   | Layout 1 | `fe4fa7411ca3`  |
| 2414   | Layout 1 | `fe4fa7411ca3`  |
| 2407   | Layout 1 | `fe4fa7411ca3`  |
| 2401   | Layout 1 | `fe4fa7411ca3`  |
| 2397   | Layout 1 | `fe4fa7411ca3`  |
| 2393   | Layout 1 | `fe4fa7411ca3`  |
| 2384   | Layout 1 | `fe4fa7411ca3`  |
| 2378   | Layout 1 | `fe4fa7411ca3`  |
| 2372   | Layout 1 | `fe4fa7411ca3`  |
| 2358   | Layout 1 | `fe4fa7411ca3`  |
| 2352   | Layout 1 | `fe4fa7411ca3`  |
| 2347   | Layout 1 | `fe4fa7411ca3`  |
| 2343   | Layout 1 | `fe4fa7411ca3`  |
| 2335   | Layout 1 | `fe4fa7411ca3`  |
| 2327   | Layout 1 | `fe4fa7411ca3`  |
| 2324   | Layout 1 | `fe4fa7411ca3`  |
| 2319   | Layout 1 | `fe4fa7411ca3`  |
| 2313   | Layout 1 | `fe4fa7411ca3`  |
| 2308   | Layout 1 | `fe4fa7411ca3`  |
| 2302   | Layout 1 | `fe4fa7411ca3`  |
| 2295   | Layout 1 | `fe4fa7411ca3`  |
| 2290   | Layout 1 | `fe4fa7411ca3`  |
| 2284   | Layout 1 | `fe4fa7411ca3`  |
| 2276   | Layout 1 | `fe4fa7411ca3`  |
| 2269   | Layout 1 | `fe4fa7411ca3`  |
| 2259   | Layout 1 | `fe4fa7411ca3`  |
| 2250   | Layout 1 | `fe4fa7411ca3`  |
| 2243   | Layout 1 | `fe4fa7411ca3`  |
| 2235   | Layout 1 | `fe4fa7411ca3`  |
| 2229   | Layout 1 | `fe4fa7411ca3`  |
| 2224   | Layout 1 | `fe4fa7411ca3`  |
| 2218   | Layout 1 | `fe4fa7411ca3`  |
| 2215   | Layout 1 | `fe4fa7411ca3`  |
| 2207   | Layout 1 | `fe4fa7411ca3`  |
| 2203   | Layout 1 | `fe4fa7411ca3`  |
| 2196   | Layout 1 | `fe4fa7411ca3`  |
| 2192   | Layout 1 | `fe4fa7411ca3`  |
| 2189   | Layout 1 | `fe4fa7411ca3`  |
| 2183   | Layout 1 | `fe4fa7411ca3`  |
| 2179   | Layout 1 | `fe4fa7411ca3`  |
| 2171   | Layout 1 | `fe4fa7411ca3`  |
| 2163   | Layout 1 | `fe4fa7411ca3`  |
| 2156   | Layout 1 | `fe4fa7411ca3`  |
| 2151   | Layout 1 | `fe4fa7411ca3`  |
| 2147   | Layout 1 | `fe4fa7411ca3`  |
| 2142   | Layout 1 | `fe4fa7411ca3`  |
| 2138   | Layout 1 | `fe4fa7411ca3`  |
| 2134   | Layout 1 | `fe4fa7411ca3`  |
| 2130   | Layout 1 | `fe4fa7411ca3`  |
| 2122   | Layout 1 | `fe4fa7411ca3`  |
| 2107   | Layout 1 | `fe4fa7411ca3`  |
| 2098   | Layout 1 | `fe4fa7411ca3`  |
| 2089   | Layout 1 | `fe4fa7411ca3`  |
| 2081   | Layout 1 | `fe4fa7411ca3`  |
| 2073   | Layout 1 | `fe4fa7411ca3`  |
| 2067   | Layout 1 | `fe4fa7411ca3`  |
| 2063   | Layout 1 | `fe4fa7411ca3`  |
| 2059   | Layout 1 | `fe4fa7411ca3`  |
| 2052   | Layout 1 | `fe4fa7411ca3`  |
| 2044   | Layout 1 | `fe4fa7411ca3`  |
| 2039   | Layout 1 | `fe4fa7411ca3`  |
| 2032   | Layout 1 | `fe4fa7411ca3`  |
| 2025   | Layout 1 | `fe4fa7411ca3`  |
| 2011   | Layout 1 | `fe4fa7411ca3`  |
| 2005   | Layout 1 | `fe4fa7411ca3`  |
| 2000   | Layout 1 | `fe4fa7411ca3`  |
| 1996   | Layout 1 | `fe4fa7411ca3`  |
| 1991   | Layout 1 | `fe4fa7411ca3`  |
| 1985   | Layout 1 | `fe4fa7411ca3`  |
| 1980   | Layout 1 | `fe4fa7411ca3`  |
| 1969   | Layout 1 | `fe4fa7411ca3`  |
| 1964   | Layout 1 | `fe4fa7411ca3`  |
| 1958   | Layout 1 | `fe4fa7411ca3`  |
| 1950   | Layout 1 | `fe4fa7411ca3`  |
| 1945   | Layout 1 | `fe4fa7411ca3`  |
| 1937   | Layout 1 | `fe4fa7411ca3`  |
| 1933   | Layout 1 | `fe4fa7411ca3`  |
| 1927   | Layout 1 | `fe4fa7411ca3`  |
| 1921   | Layout 1 | `fe4fa7411ca3`  |
| 1914   | Layout 1 | `fe4fa7411ca3`  |
| 1908   | Layout 1 | `fe4fa7411ca3`  |
| 1897   | Layout 1 | `fe4fa7411ca3`  |
| 1892   | Layout 1 | `fe4fa7411ca3`  |
| 1886   | Layout 1 | `fe4fa7411ca3`  |
| 1881   | Layout 1 | `fe4fa7411ca3`  |
| 1871   | Layout 1 | `fe4fa7411ca3`  |
| 1866   | Layout 1 | `fe4fa7411ca3`  |
| 1862   | Layout 1 | `fe4fa7411ca3`  |
| 1854   | Layout 1 | `fe4fa7411ca3`  |
| 1846   | Layout 1 | `fe4fa7411ca3`  |
| 1838   | Layout 1 | `fe4fa7411ca3`  |
| 1832   | Layout 1 | `fe4fa7411ca3`  |
| 1826   | Layout 1 | `fe4fa7411ca3`  |
| 1822   | Layout 1 | `fe4fa7411ca3`  |
| 1818   | Layout 1 | `fe4fa7411ca3`  |
| 1804   | Layout 1 | `fe4fa7411ca3`  |
| 1794   | Layout 1 | `fe4fa7411ca3`  |
| 1790   | Layout 1 | `fe4fa7411ca3`  |
| 1784   | Layout 1 | `fe4fa7411ca3`  |
| 1774   | Layout 1 | `fe4fa7411ca3`  |
| 1771   | Layout 1 | `fe4fa7411ca3`  |
| 1762   | Layout 1 | `fe4fa7411ca3`  |
| 1759   | Layout 1 | `fe4fa7411ca3`  |
| 1754   | Layout 1 | `fe4fa7411ca3`  |
| 1749   | Layout 1 | `fe4fa7411ca3`  |
| 1743   | Layout 1 | `fe4fa7411ca3`  |
| 1737   | Layout 1 | `fe4fa7411ca3`  |
| 1731   | Layout 1 | `fe4fa7411ca3`  |
| 1725   | Layout 1 | `fe4fa7411ca3`  |
| 1717   | Layout 1 | `fe4fa7411ca3`  |
| 1710   | Layout 1 | `fe4fa7411ca3`  |
| 1704   | Layout 1 | `fe4fa7411ca3`  |
| 1698   | Layout 1 | `fe4fa7411ca3`  |
| 1690   | Layout 1 | `fe4fa7411ca3`  |
| 1685   | Layout 1 | `fe4fa7411ca3`  |
| 1680   | Layout 1 | `fe4fa7411ca3`  |
| 1674   | Layout 1 | `fe4fa7411ca3`  |
| 1668   | Layout 1 | `fe4fa7411ca3`  |
| 1659   | Layout 1 | `fe4fa7411ca3`  |
| 1649   | Layout 1 | `fe4fa7411ca3`  |
| 1642   | Layout 1 | `fe4fa7411ca3`  |
| 1636   | Layout 1 | `fe4fa7411ca3`  |
| 1628   | Layout 1 | `fe4fa7411ca3`  |
| 1622   | Layout 1 | `fe4fa7411ca3`  |
| 1614   | Layout 1 | `fe4fa7411ca3`  |
| 1608   | Layout 1 | `fe4fa7411ca3`  |
| 1602   | Layout 1 | `fe4fa7411ca3`  |
| 1598   | Layout 1 | `fe4fa7411ca3`  |
| 1594   | Layout 1 | `fe4fa7411ca3`  |
| 1590   | Layout 1 | `fe4fa7411ca3`  |
| 1587   | Layout 1 | `fe4fa7411ca3`  |
| 1584   | Layout 1 | `fe4fa7411ca3`  |
| 1579   | Layout 1 | `fe4fa7411ca3`  |
| 1572   | Layout 1 | `fe4fa7411ca3`  |
| 1565   | Layout 1 | `fe4fa7411ca3`  |
| 1559   | Layout 1 | `fe4fa7411ca3`  |
| 1554   | Layout 1 | `fe4fa7411ca3`  |
| 1547   | Layout 1 | `fe4fa7411ca3`  |
| 1537   | Layout 1 | `fe4fa7411ca3`  |
| 1529   | Layout 1 | `fe4fa7411ca3`  |
| 1524   | Layout 1 | `fe4fa7411ca3`  |
| 1519   | Layout 1 | `fe4fa7411ca3`  |
| 1509   | Layout 1 | `fe4fa7411ca3`  |
| 1506   | Layout 1 | `fe4fa7411ca3`  |
| 1504   | Layout 1 | `fe4fa7411ca3`  |
| 1500   | Layout 1 | `fe4fa7411ca3`  |
| 1493   | Layout 1 | `fe4fa7411ca3`  |
| 1489   | Layout 1 | `fe4fa7411ca3`  |
| 1485   | Layout 1 | `fe4fa7411ca3`  |
| 1481   | Layout 1 | `fe4fa7411ca3`  |
| 1474   | Layout 1 | `fe4fa7411ca3`  |
| 1466   | Layout 1 | `fe4fa7411ca3`  |
| 1462   | Layout 1 | `fe4fa7411ca3`  |
| 1459   | Layout 1 | `fe4fa7411ca3`  |
| 1453   | Layout 1 | `fe4fa7411ca3`  |
| 1450   | Layout 1 | `fe4fa7411ca3`  |
| 1445   | Layout 1 | `fe4fa7411ca3`  |
| 1439   | Layout 1 | `fe4fa7411ca3`  |
| 1433   | Layout 1 | `fe4fa7411ca3`  |
| 1430   | Layout 1 | `fe4fa7411ca3`  |
| 1426   | Layout 1 | `fe4fa7411ca3`  |
| 1421   | Layout 1 | `fe4fa7411ca3`  |
| 1417   | Layout 1 | `fe4fa7411ca3`  |
| 1416   | Layout 1 | `fe4fa7411ca3`  |
| 1409   | Layout 1 | `fe4fa7411ca3`  |
| 1405   | Layout 1 | `fe4fa7411ca3`  |
| 1401   | Layout 1 | `fe4fa7411ca3`  |
| 1396   | Layout 1 | `fe4fa7411ca3`  |
| 1391   | Layout 1 | `fe4fa7411ca3`  |
| 1390   | Layout 1 | `fe4fa7411ca3`  |
| 1386   | Layout 1 | `fe4fa7411ca3`  |
| 1381   | Layout 1 | `fe4fa7411ca3`  |
| 1379   | Layout 1 | `fe4fa7411ca3`  |
| 1372   | Layout 1 | `fe4fa7411ca3`  |
| 1366   | Layout 1 | `fe4fa7411ca3`  |
| 1364   | Layout 1 | `fe4fa7411ca3`  |
| 1363   | Layout 1 | `fe4fa7411ca3`  |
| 1360   | Layout 1 | `fe4fa7411ca3`  |
| 1358   | Layout 1 | `fe4fa7411ca3`  |
| 1355   | Layout 1 | `fe4fa7411ca3`  |
| 1351   | Layout 1 | `fe4fa7411ca3`  |
| 1348   | Layout 1 | `fe4fa7411ca3`  |
| 1346   | Layout 1 | `fe4fa7411ca3`  |
| 1341   | Layout 1 | `fe4fa7411ca3`  |
| 1340   | Layout 1 | `fe4fa7411ca3`  |
| 1338   | Layout 1 | `fe4fa7411ca3`  |
| 1335   | Layout 1 | `fe4fa7411ca3`  |
| 1333   | Layout 1 | `fe4fa7411ca3`  |
| 1329   | Layout 1 | `fe4fa7411ca3`  |
| 1327   | Layout 1 | `fe4fa7411ca3`  |
| 1324   | Layout 1 | `fe4fa7411ca3`  |
| 1321   | Layout 1 | `fe4fa7411ca3`  |
| 1319   | Layout 1 | `fe4fa7411ca3`  |
| 1318   | Layout 1 | `fe4fa7411ca3`  |
| 1316   | Layout 1 | `fe4fa7411ca3`  |
| 1313   | Layout 1 | `fe4fa7411ca3`  |
| 1311   | Layout 1 | `fe4fa7411ca3`  |
| 1309   | Layout 1 | `fe4fa7411ca3`  |
| 1304   | Layout 1 | `fe4fa7411ca3`  |
| 1292   | Layout 1 | `fe4fa7411ca3`  |
| 1286   | Layout 1 | `fe4fa7411ca3`  |
| 1280   | Layout 1 | `fe4fa7411ca3`  |
| 1276   | No file  | `fe4fa7411ca3`  |
| 1267   | No file  | `fe4fa7411ca3`  |
| 1261   | No file  | `fe4fa7411ca3`  |
| 1256   | No file  | `fe4fa7411ca3`  |
| 1250   | No file  | `fe4fa7411ca3`  |
| 1246   | No file  | `fe4fa7411ca3`  |
| 1239   | No file  | `fe4fa7411ca3`  |
| 1230   | No file  | `fe4fa7411ca3`  |
| 1226   | No file  | `fe4fa7411ca3`  |
| 1220   | No file  | `fe4fa7411ca3`  |
| 1217   | No file  | `fe4fa7411ca3`  |
| 1211   | No file  | `fe4fa7411ca3`  |
| 1210   | No file  | `fe4fa7411ca3`  |
| 1208   | No file  | `fe4fa7411ca3`  |
| 1203   | No file  | `fe4fa7411ca3`  |
| 1197   | No file  | `fe4fa7411ca3`  |
| 1194   | No file  | `fe4fa7411ca3`  |
| 1192   | No file  | `fe4fa7411ca3`  |
| 1187   | No file  | `fe4fa7411ca3`  |
| 1183   | No file  | `fe4fa7411ca3`  |
| 1177   | No file  | `fe4fa7411ca3`  |
| 1173   | No file  | `fe4fa7411ca3`  |
| 1167   | No file  | `fe4fa7411ca3`  |
| 1164   | No file  | `fe4fa7411ca3`  |
| 1156   | No file  | `fe4fa7411ca3`  |
| 1149   | No file  | `fe4fa7411ca3`  |
| 1144   | No file  | `fe4fa7411ca3`  |
| 1137   | No file  | `fe4fa7411ca3`  |
| 1132   | No file  | `fe4fa7411ca3`  |
| 1127   | No file  | `fe4fa7411ca3`  |
| 1122   | No file  | `fe4fa7411ca3`  |
| 1118   | No file  | `fe4fa7411ca3`  |
| 1114   | No file  | `fe4fa7411ca3`  |
| 1109   | No file  | `fe4fa7411ca3`  |
| 1102   | No file  | `fe4fa7411ca3`  |
| 1096   | No file  | `fe4fa7411ca3`  |
| 1088   | No file  | `fe4fa7411ca3`  |
| 1081   | No file  | `fe4fa7411ca3`  |
| 1076   | No file  | `fe4fa7411ca3`  |
| 1069   | No file  | `fe4fa7411ca3`  |
| 1064   | No file  | `fe4fa7411ca3`  |
| 1058   | No file  | `fe4fa7411ca3`  |
| 1051   | No file  | `fe4fa7411ca3`  |
| 1044   | No file  | `fe4fa7411ca3`  |
| 1036   | No file  | `fe4fa7411ca3`  |
| 1026   | No file  | `fe4fa7411ca3`  |
| 1016   | No file  | `fe4fa7411ca3`  |
| 1009   | No file  | `fe4fa7411ca3`  |
| 1005   | No file  | `fe4fa7411ca3`  |
| 1000   | No file  | `fe4fa7411ca3`  |
| 998    | No file  | `fe4fa7411ca3`  |
| 990    | No file  | `fe4fa7411ca3`  |
| 979    | No file  | `fe4fa7411ca3`  |
| 972    | No file  | `fe4fa7411ca3`  |
| 963    | No file  | `fe4fa7411ca3`  |
| 955    | No file  | `fe4fa7411ca3`  |
| 946    | No file  | `fe4fa7411ca3`  |
| 938    | No file  | `fe4fa7411ca3`  |
| 927    | No file  | `fe4fa7411ca3`  |
| 911    | No file  | `fe4fa7411ca3`  |
| 904    | No file  | `fe4fa7411ca3`  |
| 899    | No file  | `fe4fa7411ca3`  |
| 894    | No file  | `fe4fa7411ca3`  |
| 885    | No file  | `fe4fa7411ca3`  |
| 879    | No file  | `fe4fa7411ca3`  |
| 872    | No file  | `fe4fa7411ca3`  |
| 864    | No file  | `fe4fa7411ca3`  |
| 855    | No file  | `fe4fa7411ca3`  |
| 853    | No file  | `fe4fa7411ca3`  |
| 845    | No file  | `fe4fa7411ca3`  |
| 837    | No file  | `fe4fa7411ca3`  |
| 829    | No file  | `fe4fa7411ca3`  |
| 822    | No file  | `fe4fa7411ca3`  |
| 814    | No file  | `fe4fa7411ca3`  |
| 805    | No file  | `fe4fa7411ca3`  |
| 794    | No file  | `fe4fa7411ca3`  |
| 787    | No file  | `fe4fa7411ca3`  |
| 780    | No file  | `fe4fa7411ca3`  |
| 771    | No file  | `fe4fa7411ca3`  |
| 760    | No file  | `fe4fa7411ca3`  |
| 748    | No file  | `fe4fa7411ca3`  |
| 741    | No file  | `fe4fa7411ca3`  |
| 736    | No file  | `fe4fa7411ca3`  |
| 731    | No file  | `fe4fa7411ca3`  |
| 723    | No file  | `fe4fa7411ca3`  |
| 711    | No file  | `fe4fa7411ca3`  |
| 707    | No file  | `fe4fa7411ca3`  |
| 697    | No file  | `fe4fa7411ca3`  |
| 689    | No file  | `fe4fa7411ca3`  |
| 683    | No file  | `fe4fa7411ca3`  |
| 678    | No file  | `fe4fa7411ca3`  |
| 670    | No file  | `fe4fa7411ca3`  |
| 661    | No file  | `fe4fa7411ca3`  |
| 656    | No file  | `fe4fa7411ca3`  |
| 652    | No file  | `fe4fa7411ca3`  |
| 643    | No file  | `fe4fa7411ca3`  |
| 637    | No file  | `fe4fa7411ca3`  |
| 630    | No file  | `fe4fa7411ca3`  |
| 627    | No file  | `fe4fa7411ca3`  |
| 621    | No file  | `fe4fa7411ca3`  |
| 617    | No file  | `fe4fa7411ca3`  |
| 615    | No file  | `fe4fa7411ca3`  |
| 606    | No file  | `fe4fa7411ca3`  |
| 599    | No file  | `fe4fa7411ca3`  |
| 592    | No file  | `fe4fa7411ca3`  |
| 586    | No file  | `fe4fa7411ca3`  |
| 577    | No file  | `fe4fa7411ca3`  |
| 569    | No file  | `fe4fa7411ca3`  |
| 561    | No file  | `fe4fa7411ca3`  |
| 554    | No file  | `fe4fa7411ca3`  |
| 542    | No file  | `fe4fa7411ca3`  |
| 532    | No file  | `fe4fa7411ca3`  |
| 531    | No file  | `fe4fa7411ca3`  |
| 526    | No file  | `fe4fa7411ca3`  |
| 521    | No file  | `fe4fa7411ca3`  |
| 517    | No file  | `fe4fa7411ca3`  |
| 510    | No file  | `fe4fa7411ca3`  |
| 508    | No file  | `fe4fa7411ca3`  |
| 504    | No file  | `fe4fa7411ca3`  |
| 497    | No file  | `fe4fa7411ca3`  |
| 491    | No file  | `fe4fa7411ca3`  |
| 485    | No file  | `fe4fa7411ca3`  |
| 478    | No file  | `fe4fa7411ca3`  |
| 472    | No file  | `fe4fa7411ca3`  |
| 466    | No file  | `fe4fa7411ca3`  |
| 457    | No file  | `fe4fa7411ca3`  |
| 452    | No file  | `fe4fa7411ca3`  |
| 449    | No file  | `fe4fa7411ca3`  |
| 435    | No file  | `fe4fa7411ca3`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                                                 |
| ------------------------ | -------- | ------------------------------------------------------------------------------------ |
| `blackspiritoffset.dbss` | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 9 bytes + condition text)

| Offset  | Type  | Field     | Notes                                                                    |
| ------- | ----- | --------- | ------------------------------------------------------------------------ |
| `+0x00` | u8    | index     | Row key: the form, as `ToClient_getBlackSpiritFromInfoByIndex()` returns it |
| `+0x01` | str16 | condition | Unlock condition script; empty for form `0`                               |

The rows are in no key order; client 3482 opens with 15, 14, 13 and ends
with 0 and 16.

### `blackspiritoffset.dbss`

Bare offset table into `blackspirit.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `blackspirit.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (9 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u8   | index       | Key of the row it points at                        |
| `+0x01` | u32  | data_offset | Absolute offset of the row in `blackspirit.dbss`, at `index` |
| `+0x05` | u32  | data_size   | The whole row: 9 + 2 x the condition length        |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `index` is its key.

## Field Names

The `BlackSpirit_InfoTable` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Index` and `Condition`, 10 rows.

| Field     | Column      | Same value (client 1784) |
| --------- | ----------- | ------------------------ |
| index     | `Index`     | 10 of 10                 |
| condition | `Condition` | 6 of 10                  |

The four conditions that differ (forms `2`, `3`, `4` and `7`) end with one
more `<or>clearquest(40022,N);` alternative in the client file, which the
private server's sheet leaves out. The 2016 client's debug symbols have no
struct for the table; the server dump of client 1784 names its loader
`BlackSpiritStaticStatusManager`.

## Notes

- `panel_widget_blackspirit_skillselect.luac` (client 3482) walks the forms
  with `ToClient_getBlackSpiritFromInfoList()` (the count of unlocked forms)
  and `ToClient_getBlackSpiritFromInfoByIndex(i)` (the form index), marks
  the one equal to `ToClient_getCurrentFormIndex()` as applied, and sets a
  new one with `ToClient_setCurrentFormIndex(index)`. Its `_texUV` table
  cuts a portrait out of `renewal/pcremaster/remaster_blackspirit_00.dds`
  for forms `0` to `4`, `10` and `11` only; the window hides any other form.
- [`blackspiritchangeformcondition.bss`](../bss/blackspiritchangeformcondition_bss.md)
  holds the condition to open the form change at all.
- On client 3482 forms `13` to `15` count three quests: chain `9102` quest
  35 or 37, chain `9104` quest 29 and chain `9105` quest 29. Form `13` needs exactly one of them
  cleared, form `14` exactly two (`!clearQuest(...)` rules out the third)
  and form `15` all three.
