# `instancefieldcommonlimitentertime.bss` Format

## Purpose

Per game service type (`CppEnums.GameServiceType`: `KOR_REAL`, `NA_REAL`,
`CS_REAL`, ...) a set of entries, each with seven pairs of hour values
(`0` to `23`). The file name and the server class that loads it on client
1784, `InstanceFieldCommonLimitEnterTimeManager`, point at the times an
instance field can be entered; two entries carry the instance field keys
of `Yonggung` (`27`) and `PAPUCRIO_ARENA` (`30`). On client 3474 the file
has 26 rows and 232 entries. The file is a u32 count and variable rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                    | Bytes | Records                      | Row bytes |
| ------ | -------------- | --------------------------------------- | ----- | ---------------------------- | --------- |
| 1      | 1969 and later | `instancefieldcommonlimitentertime.bss` | 5,750 | 232 Entry, 122 Group, 26 Row | 20        |

| Layout | File                                    | Known         | Unknown         |
| ------ | --------------------------------------- | ------------- | --------------- |
| 1      | `instancefieldcommonlimitentertime.bss` | 622 B (10.8%) | 5,128 B (89.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `94f68de38b86`  |
| 3482   | Layout 1 | `94f68de38b86`  |
| 3474   | Layout 1 | `94f68de38b86`  |
| 3473   | Layout 1 | `94f68de38b86`  |
| 3464   | Layout 1 | `94f68de38b86`  |
| 3458   | Layout 1 | `94f68de38b86`  |
| 3454   | Layout 1 | `94f68de38b86`  |
| 3444   | Layout 1 | `94f68de38b86`  |
| 3435   | Layout 1 | `94f68de38b86`  |
| 3426   | Layout 1 | `94f68de38b86`  |
| 3418   | Layout 1 | `94f68de38b86`  |
| 3412   | Layout 1 | `94f68de38b86`  |
| 3402   | Layout 1 | `94f68de38b86`  |
| 3396   | Layout 1 | `94f68de38b86`  |
| 3387   | Layout 1 | `94f68de38b86`  |
| 3381   | Layout 1 | `94f68de38b86`  |
| 3373   | Layout 1 | `94f68de38b86`  |
| 3364   | Layout 1 | `94f68de38b86`  |
| 3356   | Layout 1 | `94f68de38b86`  |
| 3349   | Layout 1 | `94f68de38b86`  |
| 3342   | Layout 1 | `94f68de38b86`  |
| 3335   | Layout 1 | `94f68de38b86`  |
| 3326   | Layout 1 | `94f68de38b86`  |
| 3321   | Layout 1 | `94f68de38b86`  |
| 3314   | Layout 1 | `94f68de38b86`  |
| 3303   | Layout 1 | `94f68de38b86`  |
| 3302   | Layout 1 | `94f68de38b86`  |
| 3293   | Layout 1 | `94f68de38b86`  |
| 3283   | Layout 1 | `94f68de38b86`  |
| 3275   | Layout 1 | `94f68de38b86`  |
| 3267   | Layout 1 | `94f68de38b86`  |
| 3258   | Layout 1 | `94f68de38b86`  |
| 3251   | Layout 1 | `94f68de38b86`  |
| 3242   | Layout 1 | `94f68de38b86`  |
| 3235   | Layout 1 | `94f68de38b86`  |
| 3229   | Layout 1 | `94f68de38b86`  |
| 3212   | Layout 1 | `94f68de38b86`  |
| 3203   | Layout 1 | `94f68de38b86`  |
| 3193   | Layout 1 | `94f68de38b86`  |
| 3186   | Layout 1 | `94f68de38b86`  |
| 3177   | Layout 1 | `94f68de38b86`  |
| 3169   | Layout 1 | `94f68de38b86`  |
| 3158   | Layout 1 | `94f68de38b86`  |
| 3151   | Layout 1 | `94f68de38b86`  |
| 3144   | Layout 1 | `94f68de38b86`  |
| 3133   | Layout 1 | `94f68de38b86`  |
| 3125   | Layout 1 | `94f68de38b86`  |
| 3118   | Layout 1 | `94f68de38b86`  |
| 3111   | Layout 1 | `94f68de38b86`  |
| 3103   | Layout 1 | `94f68de38b86`  |
| 3095   | Layout 1 | `94f68de38b86`  |
| 3086   | Layout 1 | `94f68de38b86`  |
| 3072   | Layout 1 | `94f68de38b86`  |
| 3062   | Layout 1 | `94f68de38b86`  |
| 3052   | Layout 1 | `94f68de38b86`  |
| 3045   | Layout 1 | `94f68de38b86`  |
| 3037   | Layout 1 | `94f68de38b86`  |
| 3030   | Layout 1 | `94f68de38b86`  |
| 3021   | Layout 1 | `94f68de38b86`  |
| 3012   | Layout 1 | `94f68de38b86`  |
| 3002   | Layout 1 | `94f68de38b86`  |
| 2995   | Layout 1 | `94f68de38b86`  |
| 2987   | Layout 1 | `94f68de38b86`  |
| 2978   | Layout 1 | `94f68de38b86`  |
| 2970   | Layout 1 | `94f68de38b86`  |
| 2959   | Layout 1 | `94f68de38b86`  |
| 2951   | Layout 1 | `94f68de38b86`  |
| 2942   | Layout 1 | `94f68de38b86`  |
| 2935   | Layout 1 | `94f68de38b86`  |
| 2932   | Layout 1 | `94f68de38b86`  |
| 2923   | Layout 1 | `94f68de38b86`  |
| 2919   | Layout 1 | `94f68de38b86`  |
| 2907   | Layout 1 | `94f68de38b86`  |
| 2900   | Layout 1 | `94f68de38b86`  |
| 2891   | Layout 1 | `94f68de38b86`  |
| 2882   | Layout 1 | `94f68de38b86`  |
| 2872   | Layout 1 | `94f68de38b86`  |
| 2863   | Layout 1 | `94f68de38b86`  |
| 2855   | Layout 1 | `94f68de38b86`  |
| 2849   | Layout 1 | `94f68de38b86`  |
| 2844   | Layout 1 | `94f68de38b86`  |
| 2834   | Layout 1 | `94f68de38b86`  |
| 2825   | Layout 1 | `94f68de38b86`  |
| 2819   | Layout 1 | `94f68de38b86`  |
| 2811   | Layout 1 | `94f68de38b86`  |
| 2803   | Layout 1 | `94f68de38b86`  |
| 2794   | Layout 1 | `94f68de38b86`  |
| 2783   | Layout 1 | `94f68de38b86`  |
| 2774   | Layout 1 | `94f68de38b86`  |
| 2765   | Layout 1 | `94f68de38b86`  |
| 2756   | Layout 1 | `94f68de38b86`  |
| 2750   | Layout 1 | `94f68de38b86`  |
| 2743   | Layout 1 | `94f68de38b86`  |
| 2736   | Layout 1 | `94f68de38b86`  |
| 2726   | Layout 1 | `94f68de38b86`  |
| 2717   | Layout 1 | `94f68de38b86`  |
| 2709   | Layout 1 | `94f68de38b86`  |
| 2703   | Layout 1 | `94f68de38b86`  |
| 2695   | Layout 1 | `94f68de38b86`  |
| 2684   | Layout 1 | `94f68de38b86`  |
| 2672   | Layout 1 | `94f68de38b86`  |
| 2665   | Layout 1 | `94f68de38b86`  |
| 2657   | Layout 1 | `94f68de38b86`  |
| 2649   | Layout 1 | `94f68de38b86`  |
| 2644   | Layout 1 | `94f68de38b86`  |
| 2637   | Layout 1 | `94f68de38b86`  |
| 2629   | Layout 1 | `94f68de38b86`  |
| 2619   | Layout 1 | `94f68de38b86`  |
| 2612   | Layout 1 | `94f68de38b86`  |
| 2606   | Layout 1 | `94f68de38b86`  |
| 2602   | Layout 1 | `94f68de38b86`  |
| 2601   | Layout 1 | `94f68de38b86`  |
| 2592   | Layout 1 | `94f68de38b86`  |
| 2583   | Layout 1 | `94f68de38b86`  |
| 2575   | Layout 1 | `94f68de38b86`  |
| 2567   | Layout 1 | `94f68de38b86`  |
| 2560   | Layout 1 | `94f68de38b86`  |
| 2553   | Layout 1 | `94f68de38b86`  |
| 2545   | Layout 1 | `94f68de38b86`  |
| 2538   | Layout 1 | `94f68de38b86`  |
| 2529   | Layout 1 | `94f68de38b86`  |
| 2519   | Layout 1 | `94f68de38b86`  |
| 2513   | Layout 1 | `94f68de38b86`  |
| 2510   | Layout 1 | `94f68de38b86`  |
| 2507   | Layout 1 | `94f68de38b86`  |
| 2503   | Layout 1 | `94f68de38b86`  |
| 2498   | Layout 1 | `94f68de38b86`  |
| 2492   | Layout 1 | `94f68de38b86`  |
| 2487   | Layout 1 | `94f68de38b86`  |
| 2480   | Layout 1 | `94f68de38b86`  |
| 2474   | Layout 1 | `94f68de38b86`  |
| 2468   | Layout 1 | `94f68de38b86`  |
| 2460   | Layout 1 | `94f68de38b86`  |
| 2453   | Layout 1 | `94f68de38b86`  |
| 2444   | Layout 1 | `94f68de38b86`  |
| 2438   | Layout 1 | `94f68de38b86`  |
| 2434   | Layout 1 | `94f68de38b86`  |
| 2429   | Layout 1 | `94f68de38b86`  |
| 2421   | Layout 1 | `94f68de38b86`  |
| 2414   | Layout 1 | `94f68de38b86`  |
| 2407   | Layout 1 | `94f68de38b86`  |
| 2401   | Layout 1 | `94f68de38b86`  |
| 2397   | Layout 1 | `94f68de38b86`  |
| 2393   | Layout 1 | `94f68de38b86`  |
| 2384   | Layout 1 | `94f68de38b86`  |
| 2378   | Layout 1 | `94f68de38b86`  |
| 2372   | Layout 1 | `94f68de38b86`  |
| 2358   | Layout 1 | `94f68de38b86`  |
| 2352   | Layout 1 | `94f68de38b86`  |
| 2347   | Layout 1 | `94f68de38b86`  |
| 2343   | Layout 1 | `94f68de38b86`  |
| 2335   | Layout 1 | `94f68de38b86`  |
| 2327   | Layout 1 | `94f68de38b86`  |
| 2324   | Layout 1 | `94f68de38b86`  |
| 2319   | Layout 1 | `94f68de38b86`  |
| 2313   | Layout 1 | `94f68de38b86`  |
| 2308   | Layout 1 | `94f68de38b86`  |
| 2302   | Layout 1 | `94f68de38b86`  |
| 2295   | Layout 1 | `94f68de38b86`  |
| 2290   | Layout 1 | `94f68de38b86`  |
| 2284   | Layout 1 | `94f68de38b86`  |
| 2276   | Layout 1 | `94f68de38b86`  |
| 2269   | Layout 1 | `94f68de38b86`  |
| 2259   | Layout 1 | `94f68de38b86`  |
| 2250   | Layout 1 | `94f68de38b86`  |
| 2243   | Layout 1 | `94f68de38b86`  |
| 2235   | Layout 1 | `94f68de38b86`  |
| 2229   | Layout 1 | `94f68de38b86`  |
| 2224   | Layout 1 | `94f68de38b86`  |
| 2218   | Layout 1 | `94f68de38b86`  |
| 2215   | Layout 1 | `94f68de38b86`  |
| 2207   | Layout 1 | `94f68de38b86`  |
| 2203   | Layout 1 | `94f68de38b86`  |
| 2196   | Layout 1 | `94f68de38b86`  |
| 2192   | Layout 1 | `94f68de38b86`  |
| 2189   | Layout 1 | `94f68de38b86`  |
| 2183   | Layout 1 | `94f68de38b86`  |
| 2179   | Layout 1 | `94f68de38b86`  |
| 2171   | Layout 1 | `94f68de38b86`  |
| 2163   | Layout 1 | `94f68de38b86`  |
| 2156   | Layout 1 | `94f68de38b86`  |
| 2151   | Layout 1 | `94f68de38b86`  |
| 2147   | Layout 1 | `94f68de38b86`  |
| 2142   | Layout 1 | `94f68de38b86`  |
| 2138   | Layout 1 | `94f68de38b86`  |
| 2134   | Layout 1 | `94f68de38b86`  |
| 2130   | Layout 1 | `94f68de38b86`  |
| 2122   | Layout 1 | `94f68de38b86`  |
| 2107   | Layout 1 | `94f68de38b86`  |
| 2098   | Layout 1 | `94f68de38b86`  |
| 2089   | Layout 1 | `94f68de38b86`  |
| 2081   | Layout 1 | `94f68de38b86`  |
| 2073   | Layout 1 | `94f68de38b86`  |
| 2067   | Layout 1 | `94f68de38b86`  |
| 2063   | Layout 1 | `94f68de38b86`  |
| 2059   | Layout 1 | `94f68de38b86`  |
| 2052   | Layout 1 | `94f68de38b86`  |
| 2044   | Layout 1 | `94f68de38b86`  |
| 2039   | Layout 1 | `94f68de38b86`  |
| 2032   | Layout 1 | `94f68de38b86`  |
| 2025   | Layout 1 | `94f68de38b86`  |
| 2011   | Layout 1 | `94f68de38b86`  |
| 2005   | Layout 1 | `94f68de38b86`  |
| 2000   | Layout 1 | `94f68de38b86`  |
| 1996   | Layout 1 | `94f68de38b86`  |
| 1991   | Layout 1 | `94f68de38b86`  |
| 1985   | Layout 1 | `94f68de38b86`  |
| 1980   | Layout 1 | `94f68de38b86`  |
| 1969   | Layout 1 | `94f68de38b86`  |
| 1964   | No file  | `94f68de38b86`  |
| 1958   | No file  | `94f68de38b86`  |
| 1950   | No file  | `94f68de38b86`  |
| 1945   | No file  | `94f68de38b86`  |
| 1937   | No file  | `94f68de38b86`  |
| 1933   | No file  | `94f68de38b86`  |
| 1927   | No file  | `94f68de38b86`  |
| 1921   | No file  | `94f68de38b86`  |
| 1914   | No file  | `94f68de38b86`  |
| 1908   | No file  | `94f68de38b86`  |
| 1897   | No file  | `94f68de38b86`  |
| 1892   | No file  | `94f68de38b86`  |
| 1886   | No file  | `94f68de38b86`  |
| 1881   | No file  | `94f68de38b86`  |
| 1871   | No file  | `94f68de38b86`  |
| 1866   | No file  | `94f68de38b86`  |
| 1862   | No file  | `94f68de38b86`  |
| 1854   | No file  | `94f68de38b86`  |
| 1846   | No file  | `94f68de38b86`  |
| 1838   | No file  | `94f68de38b86`  |
| 1832   | No file  | `94f68de38b86`  |
| 1826   | No file  | `94f68de38b86`  |
| 1822   | No file  | `94f68de38b86`  |
| 1818   | No file  | `94f68de38b86`  |
| 1804   | No file  | `94f68de38b86`  |
| 1794   | No file  | `94f68de38b86`  |
| 1790   | No file  | `94f68de38b86`  |
| 1784   | No file  | `94f68de38b86`  |
| 1774   | No file  | `94f68de38b86`  |
| 1771   | No file  | `94f68de38b86`  |
| 1762   | No file  | `94f68de38b86`  |
| 1759   | No file  | `94f68de38b86`  |
| 1754   | No file  | `94f68de38b86`  |
| 1749   | No file  | `94f68de38b86`  |
| 1743   | No file  | `94f68de38b86`  |
| 1737   | No file  | `94f68de38b86`  |
| 1731   | No file  | `94f68de38b86`  |
| 1725   | No file  | `94f68de38b86`  |
| 1717   | No file  | `94f68de38b86`  |
| 1710   | No file  | `94f68de38b86`  |
| 1704   | No file  | `94f68de38b86`  |
| 1698   | No file  | `94f68de38b86`  |
| 1690   | No file  | `94f68de38b86`  |
| 1685   | No file  | `94f68de38b86`  |
| 1680   | No file  | `94f68de38b86`  |
| 1674   | No file  | `94f68de38b86`  |
| 1668   | No file  | `94f68de38b86`  |
| 1659   | No file  | `94f68de38b86`  |
| 1649   | No file  | `94f68de38b86`  |
| 1642   | No file  | `94f68de38b86`  |
| 1636   | No file  | `94f68de38b86`  |
| 1628   | No file  | `94f68de38b86`  |
| 1622   | No file  | `94f68de38b86`  |
| 1614   | No file  | `94f68de38b86`  |
| 1608   | No file  | `94f68de38b86`  |
| 1602   | No file  | `94f68de38b86`  |
| 1598   | No file  | `94f68de38b86`  |
| 1594   | No file  | `94f68de38b86`  |
| 1590   | No file  | `94f68de38b86`  |
| 1587   | No file  | `94f68de38b86`  |
| 1584   | No file  | `94f68de38b86`  |
| 1579   | No file  | `94f68de38b86`  |
| 1572   | No file  | `94f68de38b86`  |
| 1565   | No file  | `94f68de38b86`  |
| 1559   | No file  | `94f68de38b86`  |
| 1554   | No file  | `94f68de38b86`  |
| 1547   | No file  | `94f68de38b86`  |
| 1537   | No file  | `94f68de38b86`  |
| 1529   | No file  | `94f68de38b86`  |
| 1524   | No file  | `94f68de38b86`  |
| 1519   | No file  | `94f68de38b86`  |
| 1509   | No file  | `94f68de38b86`  |
| 1506   | No file  | `94f68de38b86`  |
| 1504   | No file  | `94f68de38b86`  |
| 1500   | No file  | `94f68de38b86`  |
| 1493   | No file  | `94f68de38b86`  |
| 1489   | No file  | `94f68de38b86`  |
| 1485   | No file  | `94f68de38b86`  |
| 1481   | No file  | `94f68de38b86`  |
| 1474   | No file  | `94f68de38b86`  |
| 1466   | No file  | `94f68de38b86`  |
| 1462   | No file  | `94f68de38b86`  |
| 1459   | No file  | `94f68de38b86`  |
| 1453   | No file  | `94f68de38b86`  |
| 1450   | No file  | `94f68de38b86`  |
| 1445   | No file  | `94f68de38b86`  |
| 1439   | No file  | `94f68de38b86`  |
| 1433   | No file  | `94f68de38b86`  |
| 1430   | No file  | `94f68de38b86`  |
| 1426   | No file  | `94f68de38b86`  |
| 1421   | No file  | `94f68de38b86`  |
| 1417   | No file  | `94f68de38b86`  |
| 1416   | No file  | `94f68de38b86`  |
| 1409   | No file  | `94f68de38b86`  |
| 1405   | No file  | `94f68de38b86`  |
| 1401   | No file  | `94f68de38b86`  |
| 1396   | No file  | `94f68de38b86`  |
| 1391   | No file  | `94f68de38b86`  |
| 1390   | No file  | `94f68de38b86`  |
| 1386   | No file  | `94f68de38b86`  |
| 1381   | No file  | `94f68de38b86`  |
| 1379   | No file  | `94f68de38b86`  |
| 1372   | No file  | `94f68de38b86`  |
| 1366   | No file  | `94f68de38b86`  |
| 1364   | No file  | `94f68de38b86`  |
| 1363   | No file  | `94f68de38b86`  |
| 1360   | No file  | `94f68de38b86`  |
| 1358   | No file  | `94f68de38b86`  |
| 1355   | No file  | `94f68de38b86`  |
| 1351   | No file  | `94f68de38b86`  |
| 1348   | No file  | `94f68de38b86`  |
| 1346   | No file  | `94f68de38b86`  |
| 1341   | No file  | `94f68de38b86`  |
| 1340   | No file  | `94f68de38b86`  |
| 1338   | No file  | `94f68de38b86`  |
| 1335   | No file  | `94f68de38b86`  |
| 1333   | No file  | `94f68de38b86`  |
| 1329   | No file  | `94f68de38b86`  |
| 1327   | No file  | `94f68de38b86`  |
| 1324   | No file  | `94f68de38b86`  |
| 1321   | No file  | `94f68de38b86`  |
| 1319   | No file  | `94f68de38b86`  |
| 1318   | No file  | `94f68de38b86`  |
| 1316   | No file  | `94f68de38b86`  |
| 1313   | No file  | `94f68de38b86`  |
| 1311   | No file  | `94f68de38b86`  |
| 1309   | No file  | `94f68de38b86`  |
| 1304   | No file  | `94f68de38b86`  |
| 1292   | No file  | `94f68de38b86`  |
| 1286   | No file  | `94f68de38b86`  |
| 1280   | No file  | `94f68de38b86`  |
| 1276   | No file  | `94f68de38b86`  |
| 1267   | No file  | `94f68de38b86`  |
| 1261   | No file  | `94f68de38b86`  |
| 1256   | No file  | `94f68de38b86`  |
| 1250   | No file  | `94f68de38b86`  |
| 1246   | No file  | `94f68de38b86`  |
| 1239   | No file  | `94f68de38b86`  |
| 1230   | No file  | `94f68de38b86`  |
| 1226   | No file  | `94f68de38b86`  |
| 1220   | No file  | `94f68de38b86`  |
| 1217   | No file  | `94f68de38b86`  |
| 1211   | No file  | `94f68de38b86`  |
| 1210   | No file  | `94f68de38b86`  |
| 1208   | No file  | `94f68de38b86`  |
| 1203   | No file  | `94f68de38b86`  |
| 1197   | No file  | `94f68de38b86`  |
| 1194   | No file  | `94f68de38b86`  |
| 1192   | No file  | `94f68de38b86`  |
| 1187   | No file  | `94f68de38b86`  |
| 1183   | No file  | `94f68de38b86`  |
| 1177   | No file  | `94f68de38b86`  |
| 1173   | No file  | `94f68de38b86`  |
| 1167   | No file  | `94f68de38b86`  |
| 1164   | No file  | `94f68de38b86`  |
| 1156   | No file  | `94f68de38b86`  |
| 1149   | No file  | `94f68de38b86`  |
| 1144   | No file  | `94f68de38b86`  |
| 1137   | No file  | `94f68de38b86`  |
| 1132   | No file  | `94f68de38b86`  |
| 1127   | No file  | `94f68de38b86`  |
| 1122   | No file  | `94f68de38b86`  |
| 1118   | No file  | `94f68de38b86`  |
| 1114   | No file  | `94f68de38b86`  |
| 1109   | No file  | `94f68de38b86`  |
| 1102   | No file  | `94f68de38b86`  |
| 1096   | No file  | `94f68de38b86`  |
| 1088   | No file  | `94f68de38b86`  |
| 1081   | No file  | `94f68de38b86`  |
| 1076   | No file  | `94f68de38b86`  |
| 1069   | No file  | `94f68de38b86`  |
| 1064   | No file  | `94f68de38b86`  |
| 1058   | No file  | `94f68de38b86`  |
| 1051   | No file  | `94f68de38b86`  |
| 1044   | No file  | `94f68de38b86`  |
| 1036   | No file  | `94f68de38b86`  |
| 1026   | No file  | `94f68de38b86`  |
| 1016   | No file  | `94f68de38b86`  |
| 1009   | No file  | `94f68de38b86`  |
| 1005   | No file  | `94f68de38b86`  |
| 1000   | No file  | `94f68de38b86`  |
| 998    | No file  | `94f68de38b86`  |
| 990    | No file  | `94f68de38b86`  |
| 979    | No file  | `94f68de38b86`  |
| 972    | No file  | `94f68de38b86`  |
| 963    | No file  | `94f68de38b86`  |
| 955    | No file  | `94f68de38b86`  |
| 946    | No file  | `94f68de38b86`  |
| 938    | No file  | `94f68de38b86`  |
| 927    | No file  | `94f68de38b86`  |
| 911    | No file  | `94f68de38b86`  |
| 904    | No file  | `94f68de38b86`  |
| 899    | No file  | `94f68de38b86`  |
| 894    | No file  | `94f68de38b86`  |
| 885    | No file  | `94f68de38b86`  |
| 879    | No file  | `94f68de38b86`  |
| 872    | No file  | `94f68de38b86`  |
| 864    | No file  | `94f68de38b86`  |
| 855    | No file  | `94f68de38b86`  |
| 853    | No file  | `94f68de38b86`  |
| 845    | No file  | `94f68de38b86`  |
| 837    | No file  | `94f68de38b86`  |
| 829    | No file  | `94f68de38b86`  |
| 822    | No file  | `94f68de38b86`  |
| 814    | No file  | `94f68de38b86`  |
| 805    | No file  | `94f68de38b86`  |
| 794    | No file  | `94f68de38b86`  |
| 787    | No file  | `94f68de38b86`  |
| 780    | No file  | `94f68de38b86`  |
| 771    | No file  | `94f68de38b86`  |
| 760    | No file  | `94f68de38b86`  |
| 748    | No file  | `94f68de38b86`  |
| 741    | No file  | `94f68de38b86`  |
| 736    | No file  | `94f68de38b86`  |
| 731    | No file  | `94f68de38b86`  |
| 723    | No file  | `94f68de38b86`  |
| 711    | No file  | `94f68de38b86`  |
| 707    | No file  | `94f68de38b86`  |
| 697    | No file  | `94f68de38b86`  |
| 689    | No file  | `94f68de38b86`  |
| 683    | No file  | `94f68de38b86`  |
| 678    | No file  | `94f68de38b86`  |
| 670    | No file  | `94f68de38b86`  |
| 661    | No file  | `94f68de38b86`  |
| 656    | No file  | `94f68de38b86`  |
| 652    | No file  | `94f68de38b86`  |
| 643    | No file  | `94f68de38b86`  |
| 637    | No file  | `94f68de38b86`  |
| 630    | No file  | `94f68de38b86`  |
| 627    | No file  | `94f68de38b86`  |
| 621    | No file  | `94f68de38b86`  |
| 617    | No file  | `94f68de38b86`  |
| 615    | No file  | `94f68de38b86`  |
| 606    | No file  | `94f68de38b86`  |
| 599    | No file  | `94f68de38b86`  |
| 592    | No file  | `94f68de38b86`  |
| 586    | No file  | `94f68de38b86`  |
| 577    | No file  | `94f68de38b86`  |
| 569    | No file  | `94f68de38b86`  |
| 561    | No file  | `94f68de38b86`  |
| 554    | No file  | `94f68de38b86`  |
| 542    | No file  | `94f68de38b86`  |
| 532    | No file  | `94f68de38b86`  |
| 531    | No file  | `94f68de38b86`  |
| 526    | No file  | `94f68de38b86`  |
| 521    | No file  | `94f68de38b86`  |
| 517    | No file  | `94f68de38b86`  |
| 510    | No file  | `94f68de38b86`  |
| 508    | No file  | `94f68de38b86`  |
| 504    | No file  | `94f68de38b86`  |
| 497    | No file  | `94f68de38b86`  |
| 491    | No file  | `94f68de38b86`  |
| 485    | No file  | `94f68de38b86`  |
| 478    | No file  | `94f68de38b86`  |
| 472    | No file  | `94f68de38b86`  |
| 466    | No file  | `94f68de38b86`  |
| 457    | No file  | `94f68de38b86`  |
| 452    | No file  | `94f68de38b86`  |
| 449    | No file  | `94f68de38b86`  |
| 435    | No file  | `94f68de38b86`  |

<!-- versions:end -->

## Companion Files

None. The service names come from `CppEnums.GameServiceType` in
`global_define_cpp_enum.luac`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 5 bytes + groups)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u8                 | service_type | `CppEnums.GameServiceType`; one row per value             |
| `+0x01` | u32                | group_count  | Number of groups: `5`, or `1` on `CS_ALPHA` and `CS_REAL` (client 3474) |
| `+0x05` | Group[group_count] | groups       | See Group                                                |

### Group (variable: 8 bytes + entries)

| Offset  | Type               | Field             | Notes                                            |
| ------- | ------------------ | ----------------- | ------------------------------------------------ |
| `+0x00` | u32                | unknown_group_key | `11`, `16`, `0`, `8` or `22`, in this order        |
| `+0x04` | u32                | entry_count       | Number of entries                                |
| `+0x08` | Entry[entry_count] | entries           | See Entry                                        |

### Entry (20 bytes)

| Offset  | Type      | Field      | Notes                                                              |
| ------- | --------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u16       | unknown_00 | Equal to the group's `unknown_group_key`                            |
| `+0x02` | u16       | unknown_02 | `27` in group `16`, `30` in group `0`, else `65535`                  |
| `+0x04` | u8        | unknown_04 | Equal to the row's `service_type`                                   |
| `+0x05` | u8        | unknown_05 | `3`, or `0` to `2` on the rows with more entries; see Rows         |
| `+0x06` | u8[7][2]  | unknown_06 | Seven pairs of values `0` to `23`; see Hour Pairs                   |

## Rows

On client 3474 the 26 rows are the `ALPHA` and `REAL` values of 13
services; `0`, `1`, `4` and `23` to `26`, `29` to `32` have no row.

| Service types                       | Groups                    | Entries per group      | `unknown_05` | Row bytes |
| ----------------------------------- | ------------------------- | ---------------------- | ------------ | --------- |
| 22 rows (`KOR`, `JPN`, `RUS`, `KR2`, `TW`, `SA`, `TH`, `ID`, `TR`, `GT`, `ASIA`) | `11`, `16`, `0`, `8`, `22` | 1, 1, 1, 4, 1 | `3`          | 205       |
| `11` `NA_ALPHA`, `12` `NA_REAL`     | `11`, `16`, `0`, `8`, `22` | 2, 2, 2, 8, 2          | `0`, `1`     | 365       |
| `33` `CS_ALPHA`, `34` `CS_REAL`     | `8`                       | 12                     | `0`, `1`, `2` | 253       |

On the `NA` and `CS` rows the entries of a group cycle through the
`unknown_05` values (`0`, `1`, `0`, `1`, ... or `0`, `1`, `2`, ...).

## Hour Pairs

`unknown_06` holds seven pairs per entry. On client 3474 every value is
`0` to `23`. Where the pairs of an entry differ, the first and the
seventh pair differ from the five between them (`13, 1` on the first and
seventh, `17, 1` on the others), the shape of a week with Sunday first and
Saturday last. Examples on the `KOR_REAL` row:

| Group | Pairs (first to seventh)                                  |
| ----- | --------------------------------------------------------- |
| `11`  | `10, 1` on all seven                                      |
| `16`  | `14, 2`, the fifth `10, 2` (also on `KOR_ALPHA` and `KR2`) |
| `0`   | `14, 2` on all seven                                      |
| `8`   | `13, 1` / `17, 1` (weekend / weekdays) and `10, 1`, twice  |
| `22`  | `13, 1` / `17, 1`                                         |

On `NA_REAL` the `unknown_05` `0` and `1` entries of a group lie 7 to 9
apart: group `11` is `17, 8` and `10, 1`, group `16` `21, 9` and `12, 0`.
The `CS_REAL` entries of group `8` run `23, 5`, `16, 22` and `10, 16` for
`unknown_05` `0` to `2`.

## Field Names

`service_type` takes its name from the value set: the 26 keys are exactly
the `ALPHA` / `REAL` pairs of `CppEnums.GameServiceType` (`2` / `3`
`KOR`, `11` / `12` `NA`, `33` / `34` `CS`, `35` / `36` `ASIA`), and every
entry repeats its row's key. The file is not in client 1784. The client
1784 server dump (`Instance_dumpFull.exe`) names the loader
`loadInstanceFieldLimitEnterTime` and the manager
`InstanceFieldCommonLimitEnterTimeManager`, but no sheet of a private
server's `DataSheets.bexcel` on client 1784 holds the table, so no column
names are known.

## Notes

- `unknown_02` values `27` and `30` are the `instancefield.dbss` keys of
  `Yonggung` and `PAPUCRIO_ARENA`. The Lua knows instance contents types
  such as `__eInstanceContentsType_RedBattleField` (with
  `__eInstanceRedBattleField_PapuCrio`) and `_DragonDungeon`, but the
  client sets their values, so the group keys cannot be matched to them
  from the Lua.

## Open Questions

### What the Groups and Hour Pairs Are

The group keys (`0`, `8`, `11`, `16`, `22`) look like instance contents
types and the pairs like an open and a close hour per weekday, Sunday
first, with `unknown_05` a service region in another time zone (`NA`
with two, `CS` with three). None of the three is confirmed: no sheet or Lua names the
fields, and the pairs could also be a start hour and a duration.

### unknown_02

`27` and `30` match instance field keys, but only two values occur, each in
one group. Whether the field is an instance field key or another key with
these values is open.
