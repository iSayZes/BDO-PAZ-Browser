# `rosewargimicfiercebattlebuffstaicstatus.bss` Format

## Purpose

The Rose War gimmick sanctums and what they hand out: one row per gimmick
character with five (character key, u32) pairs and a u8. On client 3474
the file has one row, for Mysterious Statue (`21699`), the statue of the
Altar of Spirits sanctum in
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md).
Its pairs are Cannon with `4`, Elephant with `3`, Ballista with `1`,
Ancient Chariot with `1`, and an empty pair.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                          | Bytes | Records               | Row bytes |
| ------ | -------------- | --------------------------------------------- | ----- | --------------------- | --------- |
| 1      | 2545 and later | `rosewargimicfiercebattlebuffstaicstatus.bss` | 63    | 1 Row, 1 String Table | 43        |

| Layout | File                                          | Known        | Unknown      |
| ------ | --------------------------------------------- | ------------ | ------------ |
| 1      | `rosewargimicfiercebattlebuffstaicstatus.bss` | 42 B (66.7%) | 21 B (33.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `04bf2bebe19a`  |
| 3482   | Layout 1 | `04bf2bebe19a`  |
| 3474   | Layout 1 | `04bf2bebe19a`  |
| 3473   | Layout 1 | `04bf2bebe19a`  |
| 3464   | Layout 1 | `04bf2bebe19a`  |
| 3458   | Layout 1 | `04bf2bebe19a`  |
| 3454   | Layout 1 | `04bf2bebe19a`  |
| 3444   | Layout 1 | `04bf2bebe19a`  |
| 3435   | Layout 1 | `04bf2bebe19a`  |
| 3426   | Layout 1 | `04bf2bebe19a`  |
| 3418   | Layout 1 | `04bf2bebe19a`  |
| 3412   | Layout 1 | `04bf2bebe19a`  |
| 3402   | Layout 1 | `04bf2bebe19a`  |
| 3396   | Layout 1 | `04bf2bebe19a`  |
| 3387   | Layout 1 | `04bf2bebe19a`  |
| 3381   | Layout 1 | `04bf2bebe19a`  |
| 3373   | Layout 1 | `04bf2bebe19a`  |
| 3364   | Layout 1 | `04bf2bebe19a`  |
| 3356   | Layout 1 | `04bf2bebe19a`  |
| 3349   | Layout 1 | `04bf2bebe19a`  |
| 3342   | Layout 1 | `04bf2bebe19a`  |
| 3335   | Layout 1 | `04bf2bebe19a`  |
| 3326   | Layout 1 | `04bf2bebe19a`  |
| 3321   | Layout 1 | `04bf2bebe19a`  |
| 3314   | Layout 1 | `04bf2bebe19a`  |
| 3303   | Layout 1 | `04bf2bebe19a`  |
| 3302   | Layout 1 | `04bf2bebe19a`  |
| 3293   | Layout 1 | `04bf2bebe19a`  |
| 3283   | Layout 1 | `04bf2bebe19a`  |
| 3275   | Layout 1 | `04bf2bebe19a`  |
| 3267   | Layout 1 | `04bf2bebe19a`  |
| 3258   | Layout 1 | `04bf2bebe19a`  |
| 3251   | Layout 1 | `04bf2bebe19a`  |
| 3242   | Layout 1 | `04bf2bebe19a`  |
| 3235   | Layout 1 | `04bf2bebe19a`  |
| 3229   | Layout 1 | `04bf2bebe19a`  |
| 3212   | Layout 1 | `04bf2bebe19a`  |
| 3203   | Layout 1 | `04bf2bebe19a`  |
| 3193   | Layout 1 | `04bf2bebe19a`  |
| 3186   | Layout 1 | `04bf2bebe19a`  |
| 3177   | Layout 1 | `04bf2bebe19a`  |
| 3169   | Layout 1 | `04bf2bebe19a`  |
| 3158   | Layout 1 | `04bf2bebe19a`  |
| 3151   | Layout 1 | `04bf2bebe19a`  |
| 3144   | Layout 1 | `04bf2bebe19a`  |
| 3133   | Layout 1 | `04bf2bebe19a`  |
| 3125   | Layout 1 | `04bf2bebe19a`  |
| 3118   | Layout 1 | `04bf2bebe19a`  |
| 3111   | Layout 1 | `04bf2bebe19a`  |
| 3103   | Layout 1 | `04bf2bebe19a`  |
| 3095   | Layout 1 | `04bf2bebe19a`  |
| 3086   | Layout 1 | `04bf2bebe19a`  |
| 3072   | Layout 1 | `04bf2bebe19a`  |
| 3062   | Layout 1 | `04bf2bebe19a`  |
| 3052   | Layout 1 | `04bf2bebe19a`  |
| 3045   | Layout 1 | `04bf2bebe19a`  |
| 3037   | Layout 1 | `04bf2bebe19a`  |
| 3030   | Layout 1 | `04bf2bebe19a`  |
| 3021   | Layout 1 | `04bf2bebe19a`  |
| 3012   | Layout 1 | `04bf2bebe19a`  |
| 3002   | Layout 1 | `04bf2bebe19a`  |
| 2995   | Layout 1 | `04bf2bebe19a`  |
| 2987   | Layout 1 | `04bf2bebe19a`  |
| 2978   | Layout 1 | `04bf2bebe19a`  |
| 2970   | Layout 1 | `04bf2bebe19a`  |
| 2959   | Layout 1 | `04bf2bebe19a`  |
| 2951   | Layout 1 | `04bf2bebe19a`  |
| 2942   | Layout 1 | `04bf2bebe19a`  |
| 2935   | Layout 1 | `04bf2bebe19a`  |
| 2932   | Layout 1 | `04bf2bebe19a`  |
| 2923   | Layout 1 | `04bf2bebe19a`  |
| 2919   | Layout 1 | `04bf2bebe19a`  |
| 2907   | Layout 1 | `04bf2bebe19a`  |
| 2900   | Layout 1 | `04bf2bebe19a`  |
| 2891   | Layout 1 | `04bf2bebe19a`  |
| 2882   | Layout 1 | `04bf2bebe19a`  |
| 2872   | Layout 1 | `04bf2bebe19a`  |
| 2863   | Layout 1 | `04bf2bebe19a`  |
| 2855   | Layout 1 | `04bf2bebe19a`  |
| 2849   | Layout 1 | `04bf2bebe19a`  |
| 2844   | Layout 1 | `04bf2bebe19a`  |
| 2834   | Layout 1 | `04bf2bebe19a`  |
| 2825   | Layout 1 | `04bf2bebe19a`  |
| 2819   | Layout 1 | `04bf2bebe19a`  |
| 2811   | Layout 1 | `04bf2bebe19a`  |
| 2803   | Layout 1 | `04bf2bebe19a`  |
| 2794   | Layout 1 | `04bf2bebe19a`  |
| 2783   | Layout 1 | `04bf2bebe19a`  |
| 2774   | Layout 1 | `04bf2bebe19a`  |
| 2765   | Layout 1 | `04bf2bebe19a`  |
| 2756   | Layout 1 | `04bf2bebe19a`  |
| 2750   | Layout 1 | `04bf2bebe19a`  |
| 2743   | Layout 1 | `04bf2bebe19a`  |
| 2736   | Layout 1 | `04bf2bebe19a`  |
| 2726   | Layout 1 | `04bf2bebe19a`  |
| 2717   | Layout 1 | `04bf2bebe19a`  |
| 2709   | Layout 1 | `04bf2bebe19a`  |
| 2703   | Layout 1 | `04bf2bebe19a`  |
| 2695   | Layout 1 | `04bf2bebe19a`  |
| 2684   | Layout 1 | `04bf2bebe19a`  |
| 2672   | Layout 1 | `04bf2bebe19a`  |
| 2665   | Layout 1 | `04bf2bebe19a`  |
| 2657   | Layout 1 | `04bf2bebe19a`  |
| 2649   | Layout 1 | `04bf2bebe19a`  |
| 2644   | Layout 1 | `04bf2bebe19a`  |
| 2637   | Layout 1 | `04bf2bebe19a`  |
| 2629   | Layout 1 | `04bf2bebe19a`  |
| 2619   | Layout 1 | `04bf2bebe19a`  |
| 2612   | Layout 1 | `04bf2bebe19a`  |
| 2606   | Layout 1 | `04bf2bebe19a`  |
| 2602   | Layout 1 | `04bf2bebe19a`  |
| 2601   | Layout 1 | `04bf2bebe19a`  |
| 2592   | Layout 1 | `04bf2bebe19a`  |
| 2583   | Layout 1 | `04bf2bebe19a`  |
| 2575   | Layout 1 | `04bf2bebe19a`  |
| 2567   | Layout 1 | `04bf2bebe19a`  |
| 2560   | Layout 1 | `04bf2bebe19a`  |
| 2553   | Layout 1 | `04bf2bebe19a`  |
| 2545   | Layout 1 | `04bf2bebe19a`  |
| 2538   | No file  | `04bf2bebe19a`  |
| 2529   | No file  | `04bf2bebe19a`  |
| 2519   | No file  | `04bf2bebe19a`  |
| 2513   | No file  | `04bf2bebe19a`  |
| 2510   | No file  | `04bf2bebe19a`  |
| 2507   | No file  | `04bf2bebe19a`  |
| 2503   | No file  | `04bf2bebe19a`  |
| 2498   | No file  | `04bf2bebe19a`  |
| 2492   | No file  | `04bf2bebe19a`  |
| 2487   | No file  | `04bf2bebe19a`  |
| 2480   | No file  | `04bf2bebe19a`  |
| 2474   | No file  | `04bf2bebe19a`  |
| 2468   | No file  | `04bf2bebe19a`  |
| 2460   | No file  | `04bf2bebe19a`  |
| 2453   | No file  | `04bf2bebe19a`  |
| 2444   | No file  | `04bf2bebe19a`  |
| 2438   | No file  | `04bf2bebe19a`  |
| 2434   | No file  | `04bf2bebe19a`  |
| 2429   | No file  | `04bf2bebe19a`  |
| 2421   | No file  | `04bf2bebe19a`  |
| 2414   | No file  | `04bf2bebe19a`  |
| 2407   | No file  | `04bf2bebe19a`  |
| 2401   | No file  | `04bf2bebe19a`  |
| 2397   | No file  | `04bf2bebe19a`  |
| 2393   | No file  | `04bf2bebe19a`  |
| 2384   | No file  | `04bf2bebe19a`  |
| 2378   | No file  | `04bf2bebe19a`  |
| 2372   | No file  | `04bf2bebe19a`  |
| 2358   | No file  | `04bf2bebe19a`  |
| 2352   | No file  | `04bf2bebe19a`  |
| 2347   | No file  | `04bf2bebe19a`  |
| 2343   | No file  | `04bf2bebe19a`  |
| 2335   | No file  | `04bf2bebe19a`  |
| 2327   | No file  | `04bf2bebe19a`  |
| 2324   | No file  | `04bf2bebe19a`  |
| 2319   | No file  | `04bf2bebe19a`  |
| 2313   | No file  | `04bf2bebe19a`  |
| 2308   | No file  | `04bf2bebe19a`  |
| 2302   | No file  | `04bf2bebe19a`  |
| 2295   | No file  | `04bf2bebe19a`  |
| 2290   | No file  | `04bf2bebe19a`  |
| 2284   | No file  | `04bf2bebe19a`  |
| 2276   | No file  | `04bf2bebe19a`  |
| 2269   | No file  | `04bf2bebe19a`  |
| 2259   | No file  | `04bf2bebe19a`  |
| 2250   | No file  | `04bf2bebe19a`  |
| 2243   | No file  | `04bf2bebe19a`  |
| 2235   | No file  | `04bf2bebe19a`  |
| 2229   | No file  | `04bf2bebe19a`  |
| 2224   | No file  | `04bf2bebe19a`  |
| 2218   | No file  | `04bf2bebe19a`  |
| 2215   | No file  | `04bf2bebe19a`  |
| 2207   | No file  | `04bf2bebe19a`  |
| 2203   | No file  | `04bf2bebe19a`  |
| 2196   | No file  | `04bf2bebe19a`  |
| 2192   | No file  | `04bf2bebe19a`  |
| 2189   | No file  | `04bf2bebe19a`  |
| 2183   | No file  | `04bf2bebe19a`  |
| 2179   | No file  | `04bf2bebe19a`  |
| 2171   | No file  | `04bf2bebe19a`  |
| 2163   | No file  | `04bf2bebe19a`  |
| 2156   | No file  | `04bf2bebe19a`  |
| 2151   | No file  | `04bf2bebe19a`  |
| 2147   | No file  | `04bf2bebe19a`  |
| 2142   | No file  | `04bf2bebe19a`  |
| 2138   | No file  | `04bf2bebe19a`  |
| 2134   | No file  | `04bf2bebe19a`  |
| 2130   | No file  | `04bf2bebe19a`  |
| 2122   | No file  | `04bf2bebe19a`  |
| 2107   | No file  | `04bf2bebe19a`  |
| 2098   | No file  | `04bf2bebe19a`  |
| 2089   | No file  | `04bf2bebe19a`  |
| 2081   | No file  | `04bf2bebe19a`  |
| 2073   | No file  | `04bf2bebe19a`  |
| 2067   | No file  | `04bf2bebe19a`  |
| 2063   | No file  | `04bf2bebe19a`  |
| 2059   | No file  | `04bf2bebe19a`  |
| 2052   | No file  | `04bf2bebe19a`  |
| 2044   | No file  | `04bf2bebe19a`  |
| 2039   | No file  | `04bf2bebe19a`  |
| 2032   | No file  | `04bf2bebe19a`  |
| 2025   | No file  | `04bf2bebe19a`  |
| 2011   | No file  | `04bf2bebe19a`  |
| 2005   | No file  | `04bf2bebe19a`  |
| 2000   | No file  | `04bf2bebe19a`  |
| 1996   | No file  | `04bf2bebe19a`  |
| 1991   | No file  | `04bf2bebe19a`  |
| 1985   | No file  | `04bf2bebe19a`  |
| 1980   | No file  | `04bf2bebe19a`  |
| 1969   | No file  | `04bf2bebe19a`  |
| 1964   | No file  | `04bf2bebe19a`  |
| 1958   | No file  | `04bf2bebe19a`  |
| 1950   | No file  | `04bf2bebe19a`  |
| 1945   | No file  | `04bf2bebe19a`  |
| 1937   | No file  | `04bf2bebe19a`  |
| 1933   | No file  | `04bf2bebe19a`  |
| 1927   | No file  | `04bf2bebe19a`  |
| 1921   | No file  | `04bf2bebe19a`  |
| 1914   | No file  | `04bf2bebe19a`  |
| 1908   | No file  | `04bf2bebe19a`  |
| 1897   | No file  | `04bf2bebe19a`  |
| 1892   | No file  | `04bf2bebe19a`  |
| 1886   | No file  | `04bf2bebe19a`  |
| 1881   | No file  | `04bf2bebe19a`  |
| 1871   | No file  | `04bf2bebe19a`  |
| 1866   | No file  | `04bf2bebe19a`  |
| 1862   | No file  | `04bf2bebe19a`  |
| 1854   | No file  | `04bf2bebe19a`  |
| 1846   | No file  | `04bf2bebe19a`  |
| 1838   | No file  | `04bf2bebe19a`  |
| 1832   | No file  | `04bf2bebe19a`  |
| 1826   | No file  | `04bf2bebe19a`  |
| 1822   | No file  | `04bf2bebe19a`  |
| 1818   | No file  | `04bf2bebe19a`  |
| 1804   | No file  | `04bf2bebe19a`  |
| 1794   | No file  | `04bf2bebe19a`  |
| 1790   | No file  | `04bf2bebe19a`  |
| 1784   | No file  | `04bf2bebe19a`  |
| 1774   | No file  | `04bf2bebe19a`  |
| 1771   | No file  | `04bf2bebe19a`  |
| 1762   | No file  | `04bf2bebe19a`  |
| 1759   | No file  | `04bf2bebe19a`  |
| 1754   | No file  | `04bf2bebe19a`  |
| 1749   | No file  | `04bf2bebe19a`  |
| 1743   | No file  | `04bf2bebe19a`  |
| 1737   | No file  | `04bf2bebe19a`  |
| 1731   | No file  | `04bf2bebe19a`  |
| 1725   | No file  | `04bf2bebe19a`  |
| 1717   | No file  | `04bf2bebe19a`  |
| 1710   | No file  | `04bf2bebe19a`  |
| 1704   | No file  | `04bf2bebe19a`  |
| 1698   | No file  | `04bf2bebe19a`  |
| 1690   | No file  | `04bf2bebe19a`  |
| 1685   | No file  | `04bf2bebe19a`  |
| 1680   | No file  | `04bf2bebe19a`  |
| 1674   | No file  | `04bf2bebe19a`  |
| 1668   | No file  | `04bf2bebe19a`  |
| 1659   | No file  | `04bf2bebe19a`  |
| 1649   | No file  | `04bf2bebe19a`  |
| 1642   | No file  | `04bf2bebe19a`  |
| 1636   | No file  | `04bf2bebe19a`  |
| 1628   | No file  | `04bf2bebe19a`  |
| 1622   | No file  | `04bf2bebe19a`  |
| 1614   | No file  | `04bf2bebe19a`  |
| 1608   | No file  | `04bf2bebe19a`  |
| 1602   | No file  | `04bf2bebe19a`  |
| 1598   | No file  | `04bf2bebe19a`  |
| 1594   | No file  | `04bf2bebe19a`  |
| 1590   | No file  | `04bf2bebe19a`  |
| 1587   | No file  | `04bf2bebe19a`  |
| 1584   | No file  | `04bf2bebe19a`  |
| 1579   | No file  | `04bf2bebe19a`  |
| 1572   | No file  | `04bf2bebe19a`  |
| 1565   | No file  | `04bf2bebe19a`  |
| 1559   | No file  | `04bf2bebe19a`  |
| 1554   | No file  | `04bf2bebe19a`  |
| 1547   | No file  | `04bf2bebe19a`  |
| 1537   | No file  | `04bf2bebe19a`  |
| 1529   | No file  | `04bf2bebe19a`  |
| 1524   | No file  | `04bf2bebe19a`  |
| 1519   | No file  | `04bf2bebe19a`  |
| 1509   | No file  | `04bf2bebe19a`  |
| 1506   | No file  | `04bf2bebe19a`  |
| 1504   | No file  | `04bf2bebe19a`  |
| 1500   | No file  | `04bf2bebe19a`  |
| 1493   | No file  | `04bf2bebe19a`  |
| 1489   | No file  | `04bf2bebe19a`  |
| 1485   | No file  | `04bf2bebe19a`  |
| 1481   | No file  | `04bf2bebe19a`  |
| 1474   | No file  | `04bf2bebe19a`  |
| 1466   | No file  | `04bf2bebe19a`  |
| 1462   | No file  | `04bf2bebe19a`  |
| 1459   | No file  | `04bf2bebe19a`  |
| 1453   | No file  | `04bf2bebe19a`  |
| 1450   | No file  | `04bf2bebe19a`  |
| 1445   | No file  | `04bf2bebe19a`  |
| 1439   | No file  | `04bf2bebe19a`  |
| 1433   | No file  | `04bf2bebe19a`  |
| 1430   | No file  | `04bf2bebe19a`  |
| 1426   | No file  | `04bf2bebe19a`  |
| 1421   | No file  | `04bf2bebe19a`  |
| 1417   | No file  | `04bf2bebe19a`  |
| 1416   | No file  | `04bf2bebe19a`  |
| 1409   | No file  | `04bf2bebe19a`  |
| 1405   | No file  | `04bf2bebe19a`  |
| 1401   | No file  | `04bf2bebe19a`  |
| 1396   | No file  | `04bf2bebe19a`  |
| 1391   | No file  | `04bf2bebe19a`  |
| 1390   | No file  | `04bf2bebe19a`  |
| 1386   | No file  | `04bf2bebe19a`  |
| 1381   | No file  | `04bf2bebe19a`  |
| 1379   | No file  | `04bf2bebe19a`  |
| 1372   | No file  | `04bf2bebe19a`  |
| 1366   | No file  | `04bf2bebe19a`  |
| 1364   | No file  | `04bf2bebe19a`  |
| 1363   | No file  | `04bf2bebe19a`  |
| 1360   | No file  | `04bf2bebe19a`  |
| 1358   | No file  | `04bf2bebe19a`  |
| 1355   | No file  | `04bf2bebe19a`  |
| 1351   | No file  | `04bf2bebe19a`  |
| 1348   | No file  | `04bf2bebe19a`  |
| 1346   | No file  | `04bf2bebe19a`  |
| 1341   | No file  | `04bf2bebe19a`  |
| 1340   | No file  | `04bf2bebe19a`  |
| 1338   | No file  | `04bf2bebe19a`  |
| 1335   | No file  | `04bf2bebe19a`  |
| 1333   | No file  | `04bf2bebe19a`  |
| 1329   | No file  | `04bf2bebe19a`  |
| 1327   | No file  | `04bf2bebe19a`  |
| 1324   | No file  | `04bf2bebe19a`  |
| 1321   | No file  | `04bf2bebe19a`  |
| 1319   | No file  | `04bf2bebe19a`  |
| 1318   | No file  | `04bf2bebe19a`  |
| 1316   | No file  | `04bf2bebe19a`  |
| 1313   | No file  | `04bf2bebe19a`  |
| 1311   | No file  | `04bf2bebe19a`  |
| 1309   | No file  | `04bf2bebe19a`  |
| 1304   | No file  | `04bf2bebe19a`  |
| 1292   | No file  | `04bf2bebe19a`  |
| 1286   | No file  | `04bf2bebe19a`  |
| 1280   | No file  | `04bf2bebe19a`  |
| 1276   | No file  | `04bf2bebe19a`  |
| 1267   | No file  | `04bf2bebe19a`  |
| 1261   | No file  | `04bf2bebe19a`  |
| 1256   | No file  | `04bf2bebe19a`  |
| 1250   | No file  | `04bf2bebe19a`  |
| 1246   | No file  | `04bf2bebe19a`  |
| 1239   | No file  | `04bf2bebe19a`  |
| 1230   | No file  | `04bf2bebe19a`  |
| 1226   | No file  | `04bf2bebe19a`  |
| 1220   | No file  | `04bf2bebe19a`  |
| 1217   | No file  | `04bf2bebe19a`  |
| 1211   | No file  | `04bf2bebe19a`  |
| 1210   | No file  | `04bf2bebe19a`  |
| 1208   | No file  | `04bf2bebe19a`  |
| 1203   | No file  | `04bf2bebe19a`  |
| 1197   | No file  | `04bf2bebe19a`  |
| 1194   | No file  | `04bf2bebe19a`  |
| 1192   | No file  | `04bf2bebe19a`  |
| 1187   | No file  | `04bf2bebe19a`  |
| 1183   | No file  | `04bf2bebe19a`  |
| 1177   | No file  | `04bf2bebe19a`  |
| 1173   | No file  | `04bf2bebe19a`  |
| 1167   | No file  | `04bf2bebe19a`  |
| 1164   | No file  | `04bf2bebe19a`  |
| 1156   | No file  | `04bf2bebe19a`  |
| 1149   | No file  | `04bf2bebe19a`  |
| 1144   | No file  | `04bf2bebe19a`  |
| 1137   | No file  | `04bf2bebe19a`  |
| 1132   | No file  | `04bf2bebe19a`  |
| 1127   | No file  | `04bf2bebe19a`  |
| 1122   | No file  | `04bf2bebe19a`  |
| 1118   | No file  | `04bf2bebe19a`  |
| 1114   | No file  | `04bf2bebe19a`  |
| 1109   | No file  | `04bf2bebe19a`  |
| 1102   | No file  | `04bf2bebe19a`  |
| 1096   | No file  | `04bf2bebe19a`  |
| 1088   | No file  | `04bf2bebe19a`  |
| 1081   | No file  | `04bf2bebe19a`  |
| 1076   | No file  | `04bf2bebe19a`  |
| 1069   | No file  | `04bf2bebe19a`  |
| 1064   | No file  | `04bf2bebe19a`  |
| 1058   | No file  | `04bf2bebe19a`  |
| 1051   | No file  | `04bf2bebe19a`  |
| 1044   | No file  | `04bf2bebe19a`  |
| 1036   | No file  | `04bf2bebe19a`  |
| 1026   | No file  | `04bf2bebe19a`  |
| 1016   | No file  | `04bf2bebe19a`  |
| 1009   | No file  | `04bf2bebe19a`  |
| 1005   | No file  | `04bf2bebe19a`  |
| 1000   | No file  | `04bf2bebe19a`  |
| 998    | No file  | `04bf2bebe19a`  |
| 990    | No file  | `04bf2bebe19a`  |
| 979    | No file  | `04bf2bebe19a`  |
| 972    | No file  | `04bf2bebe19a`  |
| 963    | No file  | `04bf2bebe19a`  |
| 955    | No file  | `04bf2bebe19a`  |
| 946    | No file  | `04bf2bebe19a`  |
| 938    | No file  | `04bf2bebe19a`  |
| 927    | No file  | `04bf2bebe19a`  |
| 911    | No file  | `04bf2bebe19a`  |
| 904    | No file  | `04bf2bebe19a`  |
| 899    | No file  | `04bf2bebe19a`  |
| 894    | No file  | `04bf2bebe19a`  |
| 885    | No file  | `04bf2bebe19a`  |
| 879    | No file  | `04bf2bebe19a`  |
| 872    | No file  | `04bf2bebe19a`  |
| 864    | No file  | `04bf2bebe19a`  |
| 855    | No file  | `04bf2bebe19a`  |
| 853    | No file  | `04bf2bebe19a`  |
| 845    | No file  | `04bf2bebe19a`  |
| 837    | No file  | `04bf2bebe19a`  |
| 829    | No file  | `04bf2bebe19a`  |
| 822    | No file  | `04bf2bebe19a`  |
| 814    | No file  | `04bf2bebe19a`  |
| 805    | No file  | `04bf2bebe19a`  |
| 794    | No file  | `04bf2bebe19a`  |
| 787    | No file  | `04bf2bebe19a`  |
| 780    | No file  | `04bf2bebe19a`  |
| 771    | No file  | `04bf2bebe19a`  |
| 760    | No file  | `04bf2bebe19a`  |
| 748    | No file  | `04bf2bebe19a`  |
| 741    | No file  | `04bf2bebe19a`  |
| 736    | No file  | `04bf2bebe19a`  |
| 731    | No file  | `04bf2bebe19a`  |
| 723    | No file  | `04bf2bebe19a`  |
| 711    | No file  | `04bf2bebe19a`  |
| 707    | No file  | `04bf2bebe19a`  |
| 697    | No file  | `04bf2bebe19a`  |
| 689    | No file  | `04bf2bebe19a`  |
| 683    | No file  | `04bf2bebe19a`  |
| 678    | No file  | `04bf2bebe19a`  |
| 670    | No file  | `04bf2bebe19a`  |
| 661    | No file  | `04bf2bebe19a`  |
| 656    | No file  | `04bf2bebe19a`  |
| 652    | No file  | `04bf2bebe19a`  |
| 643    | No file  | `04bf2bebe19a`  |
| 637    | No file  | `04bf2bebe19a`  |
| 630    | No file  | `04bf2bebe19a`  |
| 627    | No file  | `04bf2bebe19a`  |
| 621    | No file  | `04bf2bebe19a`  |
| 617    | No file  | `04bf2bebe19a`  |
| 615    | No file  | `04bf2bebe19a`  |
| 606    | No file  | `04bf2bebe19a`  |
| 599    | No file  | `04bf2bebe19a`  |
| 592    | No file  | `04bf2bebe19a`  |
| 586    | No file  | `04bf2bebe19a`  |
| 577    | No file  | `04bf2bebe19a`  |
| 569    | No file  | `04bf2bebe19a`  |
| 561    | No file  | `04bf2bebe19a`  |
| 554    | No file  | `04bf2bebe19a`  |
| 542    | No file  | `04bf2bebe19a`  |
| 532    | No file  | `04bf2bebe19a`  |
| 531    | No file  | `04bf2bebe19a`  |
| 526    | No file  | `04bf2bebe19a`  |
| 521    | No file  | `04bf2bebe19a`  |
| 517    | No file  | `04bf2bebe19a`  |
| 510    | No file  | `04bf2bebe19a`  |
| 508    | No file  | `04bf2bebe19a`  |
| 504    | No file  | `04bf2bebe19a`  |
| 497    | No file  | `04bf2bebe19a`  |
| 491    | No file  | `04bf2bebe19a`  |
| 485    | No file  | `04bf2bebe19a`  |
| 478    | No file  | `04bf2bebe19a`  |
| 472    | No file  | `04bf2bebe19a`  |
| 466    | No file  | `04bf2bebe19a`  |
| 457    | No file  | `04bf2bebe19a`  |
| 452    | No file  | `04bf2bebe19a`  |
| 449    | No file  | `04bf2bebe19a`  |
| 435    | No file  | `04bf2bebe19a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (43 bytes)

| Offset  | Type | Field                 | Notes                                                                    |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | character_key_1       | `characterstatic.dbss` key; `31111` Cannon on client 3474                |
| `+0x04` | u32  | unknown_04            | `4` on client 3474; see Open Questions                                   |
| `+0x08` | u32  | character_key_2       | `31116` Elephant                                                         |
| `+0x0C` | u32  | unknown_0c            | `3`                                                                      |
| `+0x10` | u32  | character_key_3       | `31112` Ballista                                                         |
| `+0x14` | u32  | unknown_14            | `1`                                                                      |
| `+0x18` | u32  | character_key_4       | `31113` Ancient Chariot                                                  |
| `+0x1C` | u32  | unknown_1c            | `1`                                                                      |
| `+0x20` | u32  | character_key_5       | `0`, no character                                                        |
| `+0x24` | u32  | unknown_24            | `0`                                                                      |
| `+0x28` | u16  | gimmick_character_key | `21699` Mysterious Statue, a `neutral_character_key` of the monster table |
| `+0x2A` | u8   | unknown_2a            | `1`; see Open Questions                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The five `character_key_*`
values and `gimmick_character_key` resolve to LOC type 6 character names.
The minimap Lua (`panel_rosewar_minimap_*.luac`, client 3474) checks a
sanctum with `ToClient_IsRoseWarGimicFierceBattle(characterKeyRaw)` and
reads its buff with `ToClient_GetRoseWarGimicFierceBattleBuffStaticStatusWrapper(fierceBattleKeyRaw):getBuffType()`,
so the row is keyed by the gimmick sanctum's character. The u16 key sits
after the pairs in the row.

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 01 00 00 00 87 79 00 00 04 00 00 00 8C 79 00 00 03 00 00 00 88 79 00 00 01 00 00 00 89 79 00 00 01 00 00 00 00 00 00 00 00 00 00 00 C3 54 01 00 00 00 00 33 00 00 00 00 00 00 00`
  (63 bytes). The file is not in the archives of client 1784.
- The second gimmick sanctum, Ocean Sanctum (`22` in the monster table,
  Mysterious Statue `21700`), has no row.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the gimmick character first.

## Open Questions

### The Buff Type and the Pair Values

The Lua names three gimmick buff types, `__eRoseWarGimicFierceBattleBuffType_Skill`,
`_Spawn` and `_Item`, with the icons `Combine_Etc_RoseWar_Command_Wight_Icon_Buff_1`
to `_3`, but not their values. The pairs name siege objects (Cannon,
Elephant, Ballista, Ancient Chariot), which reads as a Spawn buff with
`unknown_04` to `unknown_24` as how many of each spawn, and `unknown_2a`
(`1`) as the buff type. Neither the type value nor the counts are
confirmed.
