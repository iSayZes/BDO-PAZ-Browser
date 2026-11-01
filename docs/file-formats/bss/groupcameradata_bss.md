# `groupcameradata.bss` Format

## Purpose

The summaries shown when a story cutscene is skipped: one fixed 28-byte row per
cutscene with its title, a short recap, a quoted line and a region symbol icon,
all as indices into a shared string table. The Korean text is the source; LOC
type 97 holds the translations.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records                                 | Row bytes |
| ------ | -------------- | --------------------- | ------ | --------------------------------------- | --------- |
| 2      | 2142 and later | `groupcameradata.bss` | 25,147 | 92 Cutscene Row                         | 28        |
| 1      | 1579 to 1784   | `groupcameradata.bss` | 12,760 | 6 Cutscene Row, 170 Line, 12 Line Group | 16        |

| Layout | File                  | Known            | Unknown         |
| ------ | --------------------- | ---------------- | --------------- |
| 2      | `groupcameradata.bss` | 24,411 B (97.1%) | 736 B (2.9%)    |
| 1      | `groupcameradata.bss` | 11,400 B (89.3%) | 1,360 B (10.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `2b0582ef7809`  |
| 3482   | Layout 2             | `2b0582ef7809`  |
| 3474   | Layout 2             | `2b0582ef7809`  |
| 3473   | Layout 2             | `2b0582ef7809`  |
| 3464   | Layout 2             | `2b0582ef7809`  |
| 3458   | Layout 2             | `2b0582ef7809`  |
| 3454   | Layout 2             | `2b0582ef7809`  |
| 3444   | Layout 2             | `2b0582ef7809`  |
| 3435   | Layout 2             | `2b0582ef7809`  |
| 3426   | Layout 2             | `2b0582ef7809`  |
| 3418   | Layout 2             | `2b0582ef7809`  |
| 3412   | Layout 2             | `2b0582ef7809`  |
| 3402   | Layout 2             | `2b0582ef7809`  |
| 3396   | Layout 2             | `2b0582ef7809`  |
| 3387   | Layout 2             | `2b0582ef7809`  |
| 3381   | Layout 2             | `2b0582ef7809`  |
| 3373   | Layout 2             | `2b0582ef7809`  |
| 3364   | Layout 2             | `2b0582ef7809`  |
| 3356   | Layout 2             | `2b0582ef7809`  |
| 3349   | Layout 2             | `2b0582ef7809`  |
| 3342   | Layout 2             | `2b0582ef7809`  |
| 3335   | Layout 2             | `2b0582ef7809`  |
| 3326   | Layout 2             | `2b0582ef7809`  |
| 3321   | Layout 2             | `2b0582ef7809`  |
| 3314   | Layout 2             | `2b0582ef7809`  |
| 3303   | Layout 2             | `2b0582ef7809`  |
| 3302   | Layout 2             | `2b0582ef7809`  |
| 3293   | Layout 2             | `2b0582ef7809`  |
| 3283   | Layout 2             | `2b0582ef7809`  |
| 3275   | Layout 2             | `2b0582ef7809`  |
| 3267   | Layout 2             | `2b0582ef7809`  |
| 3258   | Layout 2             | `2b0582ef7809`  |
| 3251   | Layout 2             | `2b0582ef7809`  |
| 3242   | Layout 2             | `2b0582ef7809`  |
| 3235   | Layout 2             | `2b0582ef7809`  |
| 3229   | Layout 2             | `2b0582ef7809`  |
| 3212   | Layout 2             | `2b0582ef7809`  |
| 3203   | Layout 2             | `2b0582ef7809`  |
| 3193   | Layout 2             | `2b0582ef7809`  |
| 3186   | Layout 2             | `2b0582ef7809`  |
| 3177   | Layout 2             | `2b0582ef7809`  |
| 3169   | Layout 2             | `2b0582ef7809`  |
| 3158   | Layout 2             | `2b0582ef7809`  |
| 3151   | Layout 2             | `2b0582ef7809`  |
| 3144   | Layout 2             | `2b0582ef7809`  |
| 3133   | Layout 2             | `2b0582ef7809`  |
| 3125   | Layout 2             | `2b0582ef7809`  |
| 3118   | Layout 2             | `2b0582ef7809`  |
| 3111   | Layout 2             | `2b0582ef7809`  |
| 3103   | Layout 2             | `2b0582ef7809`  |
| 3095   | Layout 2             | `2b0582ef7809`  |
| 3086   | Layout 2             | `2b0582ef7809`  |
| 3072   | Layout 2             | `2b0582ef7809`  |
| 3062   | Layout 2             | `2b0582ef7809`  |
| 3052   | Layout 2             | `2b0582ef7809`  |
| 3045   | Layout 2             | `2b0582ef7809`  |
| 3037   | Layout 2             | `2b0582ef7809`  |
| 3030   | Layout 2             | `2b0582ef7809`  |
| 3021   | Layout 2             | `2b0582ef7809`  |
| 3012   | Layout 2             | `2b0582ef7809`  |
| 3002   | Layout 2             | `2b0582ef7809`  |
| 2995   | Layout 2             | `2b0582ef7809`  |
| 2987   | Layout 2             | `2b0582ef7809`  |
| 2978   | Layout 2             | `2b0582ef7809`  |
| 2970   | Layout 2             | `2b0582ef7809`  |
| 2959   | Layout 2             | `2b0582ef7809`  |
| 2951   | Layout 2             | `2b0582ef7809`  |
| 2942   | Layout 2             | `2b0582ef7809`  |
| 2935   | Layout 2             | `2b0582ef7809`  |
| 2932   | Layout 2             | `2b0582ef7809`  |
| 2923   | Layout 2             | `2b0582ef7809`  |
| 2919   | Layout 2             | `2b0582ef7809`  |
| 2907   | Layout 2             | `2b0582ef7809`  |
| 2900   | Layout 2             | `2b0582ef7809`  |
| 2891   | Layout 2             | `2b0582ef7809`  |
| 2882   | Layout 2             | `2b0582ef7809`  |
| 2872   | Layout 2             | `2b0582ef7809`  |
| 2863   | Layout 2             | `2b0582ef7809`  |
| 2855   | Layout 2             | `2b0582ef7809`  |
| 2849   | Layout 2             | `2b0582ef7809`  |
| 2844   | Layout 2             | `2b0582ef7809`  |
| 2834   | Layout 2             | `2b0582ef7809`  |
| 2825   | Layout 2             | `2b0582ef7809`  |
| 2819   | Layout 2             | `2b0582ef7809`  |
| 2811   | Layout 2             | `2b0582ef7809`  |
| 2803   | Layout 2             | `2b0582ef7809`  |
| 2794   | Layout 2             | `2b0582ef7809`  |
| 2783   | Layout 2             | `2b0582ef7809`  |
| 2774   | Layout 2             | `2b0582ef7809`  |
| 2765   | Layout 2             | `2b0582ef7809`  |
| 2756   | Layout 2             | `2b0582ef7809`  |
| 2750   | Layout 2             | `2b0582ef7809`  |
| 2743   | Layout 2             | `2b0582ef7809`  |
| 2736   | Layout 2             | `2b0582ef7809`  |
| 2726   | Layout 2             | `2b0582ef7809`  |
| 2717   | Layout 2             | `2b0582ef7809`  |
| 2709   | Layout 2             | `2b0582ef7809`  |
| 2703   | Layout 2             | `2b0582ef7809`  |
| 2695   | Layout 2             | `2b0582ef7809`  |
| 2684   | Layout 2             | `2b0582ef7809`  |
| 2672   | Layout 2             | `2b0582ef7809`  |
| 2665   | Layout 2             | `2b0582ef7809`  |
| 2657   | Layout 2             | `2b0582ef7809`  |
| 2649   | Layout 2             | `2b0582ef7809`  |
| 2644   | Layout 2             | `2b0582ef7809`  |
| 2637   | Layout 2             | `2b0582ef7809`  |
| 2629   | Layout 2             | `2b0582ef7809`  |
| 2619   | Layout 2             | `2b0582ef7809`  |
| 2612   | Layout 2             | `2b0582ef7809`  |
| 2606   | Layout 2             | `2b0582ef7809`  |
| 2602   | Layout 2             | `2b0582ef7809`  |
| 2601   | Layout 2             | `2b0582ef7809`  |
| 2592   | Layout 2             | `2b0582ef7809`  |
| 2583   | Layout 2             | `2b0582ef7809`  |
| 2575   | Layout 2             | `2b0582ef7809`  |
| 2567   | Layout 2             | `2b0582ef7809`  |
| 2560   | Layout 2             | `2b0582ef7809`  |
| 2553   | Layout 2             | `2b0582ef7809`  |
| 2545   | Layout 2             | `2b0582ef7809`  |
| 2538   | Layout 2             | `2b0582ef7809`  |
| 2529   | Layout 2             | `2b0582ef7809`  |
| 2519   | Layout 2             | `2b0582ef7809`  |
| 2513   | Layout 2             | `2b0582ef7809`  |
| 2510   | Layout 2             | `2b0582ef7809`  |
| 2507   | Layout 2             | `2b0582ef7809`  |
| 2503   | Layout 2             | `2b0582ef7809`  |
| 2498   | Layout 2             | `2b0582ef7809`  |
| 2492   | Layout 2             | `2b0582ef7809`  |
| 2487   | Layout 2             | `2b0582ef7809`  |
| 2480   | Layout 2             | `2b0582ef7809`  |
| 2474   | Layout 2             | `2b0582ef7809`  |
| 2468   | Layout 2             | `2b0582ef7809`  |
| 2460   | Layout 2             | `2b0582ef7809`  |
| 2453   | Layout 2             | `2b0582ef7809`  |
| 2444   | Layout 2             | `2b0582ef7809`  |
| 2438   | Layout 2             | `2b0582ef7809`  |
| 2434   | Layout 2             | `2b0582ef7809`  |
| 2429   | Layout 2             | `2b0582ef7809`  |
| 2421   | Layout 2             | `2b0582ef7809`  |
| 2414   | Layout 2             | `2b0582ef7809`  |
| 2407   | Layout 2             | `2b0582ef7809`  |
| 2401   | Layout 2             | `2b0582ef7809`  |
| 2397   | Layout 2             | `2b0582ef7809`  |
| 2393   | Layout 2             | `2b0582ef7809`  |
| 2384   | Layout 2             | `2b0582ef7809`  |
| 2378   | Layout 2             | `2b0582ef7809`  |
| 2372   | Layout 2             | `2b0582ef7809`  |
| 2358   | Layout 2             | `2b0582ef7809`  |
| 2352   | Layout 2             | `2b0582ef7809`  |
| 2347   | Layout 2             | `2b0582ef7809`  |
| 2343   | Layout 2             | `2b0582ef7809`  |
| 2335   | Layout 2             | `2b0582ef7809`  |
| 2327   | Layout 2             | `2b0582ef7809`  |
| 2324   | Layout 2             | `2b0582ef7809`  |
| 2319   | Layout 2             | `2b0582ef7809`  |
| 2313   | Layout 2             | `2b0582ef7809`  |
| 2308   | Layout 2             | `2b0582ef7809`  |
| 2302   | Layout 2             | `2b0582ef7809`  |
| 2295   | Layout 2             | `2b0582ef7809`  |
| 2290   | Layout 2             | `2b0582ef7809`  |
| 2284   | Layout 2             | `2b0582ef7809`  |
| 2276   | Layout 2             | `2b0582ef7809`  |
| 2269   | Layout 2             | `2b0582ef7809`  |
| 2259   | Layout 2             | `2b0582ef7809`  |
| 2250   | Layout 2             | `2b0582ef7809`  |
| 2243   | Layout 2             | `2b0582ef7809`  |
| 2235   | Layout 2             | `2b0582ef7809`  |
| 2229   | Layout 2             | `2b0582ef7809`  |
| 2224   | Layout 2             | `2b0582ef7809`  |
| 2218   | Layout 2             | `2b0582ef7809`  |
| 2215   | Layout 2             | `2b0582ef7809`  |
| 2207   | Layout 2             | `2b0582ef7809`  |
| 2203   | Layout 2             | `2b0582ef7809`  |
| 2196   | Layout 2             | `2b0582ef7809`  |
| 2192   | Layout 2             | `2b0582ef7809`  |
| 2189   | Layout 2             | `2b0582ef7809`  |
| 2183   | Layout 2             | `2b0582ef7809`  |
| 2179   | Layout 2             | `2b0582ef7809`  |
| 2171   | Layout 2             | `2b0582ef7809`  |
| 2163   | Layout 2             | `2b0582ef7809`  |
| 2156   | Layout 2             | `2b0582ef7809`  |
| 2151   | Layout 2             | `2b0582ef7809`  |
| 2147   | Layout 2             | `2b0582ef7809`  |
| 2142   | Layout 2             | `2b0582ef7809`  |
| 2138   | No documented layout | `2b0582ef7809`  |
| 2134   | No documented layout | `2b0582ef7809`  |
| 2130   | No documented layout | `2b0582ef7809`  |
| 2122   | No documented layout | `2b0582ef7809`  |
| 2107   | No documented layout | `2b0582ef7809`  |
| 2098   | No documented layout | `2b0582ef7809`  |
| 2089   | No documented layout | `2b0582ef7809`  |
| 2081   | No documented layout | `2b0582ef7809`  |
| 2073   | No documented layout | `2b0582ef7809`  |
| 2067   | No documented layout | `2b0582ef7809`  |
| 2063   | No documented layout | `2b0582ef7809`  |
| 2059   | No documented layout | `2b0582ef7809`  |
| 2052   | No documented layout | `2b0582ef7809`  |
| 2044   | No documented layout | `2b0582ef7809`  |
| 2039   | No documented layout | `2b0582ef7809`  |
| 2032   | No documented layout | `2b0582ef7809`  |
| 2025   | No documented layout | `2b0582ef7809`  |
| 2011   | No documented layout | `2b0582ef7809`  |
| 2005   | No documented layout | `2b0582ef7809`  |
| 2000   | No documented layout | `2b0582ef7809`  |
| 1996   | No documented layout | `2b0582ef7809`  |
| 1991   | No documented layout | `2b0582ef7809`  |
| 1985   | No documented layout | `2b0582ef7809`  |
| 1980   | No documented layout | `2b0582ef7809`  |
| 1969   | No documented layout | `2b0582ef7809`  |
| 1964   | No documented layout | `2b0582ef7809`  |
| 1958   | No documented layout | `2b0582ef7809`  |
| 1950   | No documented layout | `2b0582ef7809`  |
| 1945   | No documented layout | `2b0582ef7809`  |
| 1937   | No documented layout | `2b0582ef7809`  |
| 1933   | No documented layout | `2b0582ef7809`  |
| 1927   | No documented layout | `2b0582ef7809`  |
| 1921   | No documented layout | `2b0582ef7809`  |
| 1914   | No documented layout | `2b0582ef7809`  |
| 1908   | No documented layout | `2b0582ef7809`  |
| 1897   | No documented layout | `2b0582ef7809`  |
| 1892   | No documented layout | `2b0582ef7809`  |
| 1886   | No documented layout | `2b0582ef7809`  |
| 1881   | No documented layout | `2b0582ef7809`  |
| 1871   | No documented layout | `2b0582ef7809`  |
| 1866   | No documented layout | `2b0582ef7809`  |
| 1862   | No documented layout | `2b0582ef7809`  |
| 1854   | No documented layout | `2b0582ef7809`  |
| 1846   | No documented layout | `2b0582ef7809`  |
| 1838   | No documented layout | `2b0582ef7809`  |
| 1832   | No documented layout | `2b0582ef7809`  |
| 1826   | No documented layout | `2b0582ef7809`  |
| 1822   | No documented layout | `2b0582ef7809`  |
| 1818   | No documented layout | `2b0582ef7809`  |
| 1804   | No documented layout | `2b0582ef7809`  |
| 1794   | No documented layout | `2b0582ef7809`  |
| 1790   | No documented layout | `2b0582ef7809`  |
| 1784   | Layout 1             | `2b0582ef7809`  |
| 1774   | Layout 1             | `2b0582ef7809`  |
| 1771   | Layout 1             | `2b0582ef7809`  |
| 1762   | Layout 1             | `2b0582ef7809`  |
| 1759   | Layout 1             | `2b0582ef7809`  |
| 1754   | Layout 1             | `2b0582ef7809`  |
| 1749   | Layout 1             | `2b0582ef7809`  |
| 1743   | Layout 1             | `2b0582ef7809`  |
| 1737   | Layout 1             | `2b0582ef7809`  |
| 1731   | Layout 1             | `2b0582ef7809`  |
| 1725   | Layout 1             | `2b0582ef7809`  |
| 1717   | Layout 1             | `2b0582ef7809`  |
| 1710   | Layout 1             | `2b0582ef7809`  |
| 1704   | Layout 1             | `2b0582ef7809`  |
| 1698   | Layout 1             | `2b0582ef7809`  |
| 1690   | Layout 1             | `2b0582ef7809`  |
| 1685   | Layout 1             | `2b0582ef7809`  |
| 1680   | Layout 1             | `2b0582ef7809`  |
| 1674   | Layout 1             | `2b0582ef7809`  |
| 1668   | Layout 1             | `2b0582ef7809`  |
| 1659   | Layout 1             | `2b0582ef7809`  |
| 1649   | Layout 1             | `2b0582ef7809`  |
| 1642   | Layout 1             | `2b0582ef7809`  |
| 1636   | Layout 1             | `2b0582ef7809`  |
| 1628   | Layout 1             | `2b0582ef7809`  |
| 1622   | Layout 1             | `2b0582ef7809`  |
| 1614   | Layout 1             | `2b0582ef7809`  |
| 1608   | Layout 1             | `2b0582ef7809`  |
| 1602   | Layout 1             | `2b0582ef7809`  |
| 1598   | Layout 1             | `2b0582ef7809`  |
| 1594   | Layout 1             | `2b0582ef7809`  |
| 1590   | Layout 1             | `2b0582ef7809`  |
| 1587   | Layout 1             | `2b0582ef7809`  |
| 1584   | Layout 1             | `2b0582ef7809`  |
| 1579   | Layout 1             | `2b0582ef7809`  |
| 1572   | No file              | `2b0582ef7809`  |
| 1565   | No file              | `2b0582ef7809`  |
| 1559   | No file              | `2b0582ef7809`  |
| 1554   | No file              | `2b0582ef7809`  |
| 1547   | No file              | `2b0582ef7809`  |
| 1537   | No file              | `2b0582ef7809`  |
| 1529   | No file              | `2b0582ef7809`  |
| 1524   | No file              | `2b0582ef7809`  |
| 1519   | No file              | `2b0582ef7809`  |
| 1509   | No file              | `2b0582ef7809`  |
| 1506   | No file              | `2b0582ef7809`  |
| 1504   | No file              | `2b0582ef7809`  |
| 1500   | No file              | `2b0582ef7809`  |
| 1493   | No file              | `2b0582ef7809`  |
| 1489   | No file              | `2b0582ef7809`  |
| 1485   | No file              | `2b0582ef7809`  |
| 1481   | No file              | `2b0582ef7809`  |
| 1474   | No file              | `2b0582ef7809`  |
| 1466   | No file              | `2b0582ef7809`  |
| 1462   | No file              | `2b0582ef7809`  |
| 1459   | No file              | `2b0582ef7809`  |
| 1453   | No file              | `2b0582ef7809`  |
| 1450   | No file              | `2b0582ef7809`  |
| 1445   | No file              | `2b0582ef7809`  |
| 1439   | No file              | `2b0582ef7809`  |
| 1433   | No file              | `2b0582ef7809`  |
| 1430   | No file              | `2b0582ef7809`  |
| 1426   | No file              | `2b0582ef7809`  |
| 1421   | No file              | `2b0582ef7809`  |
| 1417   | No file              | `2b0582ef7809`  |
| 1416   | No file              | `2b0582ef7809`  |
| 1409   | No file              | `2b0582ef7809`  |
| 1405   | No file              | `2b0582ef7809`  |
| 1401   | No file              | `2b0582ef7809`  |
| 1396   | No file              | `2b0582ef7809`  |
| 1391   | No file              | `2b0582ef7809`  |
| 1390   | No file              | `2b0582ef7809`  |
| 1386   | No file              | `2b0582ef7809`  |
| 1381   | No file              | `2b0582ef7809`  |
| 1379   | No file              | `2b0582ef7809`  |
| 1372   | No file              | `2b0582ef7809`  |
| 1366   | No file              | `2b0582ef7809`  |
| 1364   | No file              | `2b0582ef7809`  |
| 1363   | No file              | `2b0582ef7809`  |
| 1360   | No file              | `2b0582ef7809`  |
| 1358   | No file              | `2b0582ef7809`  |
| 1355   | No file              | `2b0582ef7809`  |
| 1351   | No file              | `2b0582ef7809`  |
| 1348   | No file              | `2b0582ef7809`  |
| 1346   | No file              | `2b0582ef7809`  |
| 1341   | No file              | `2b0582ef7809`  |
| 1340   | No file              | `2b0582ef7809`  |
| 1338   | No file              | `2b0582ef7809`  |
| 1335   | No file              | `2b0582ef7809`  |
| 1333   | No file              | `2b0582ef7809`  |
| 1329   | No file              | `2b0582ef7809`  |
| 1327   | No file              | `2b0582ef7809`  |
| 1324   | No file              | `2b0582ef7809`  |
| 1321   | No file              | `2b0582ef7809`  |
| 1319   | No file              | `2b0582ef7809`  |
| 1318   | No file              | `2b0582ef7809`  |
| 1316   | No file              | `2b0582ef7809`  |
| 1313   | No file              | `2b0582ef7809`  |
| 1311   | No file              | `2b0582ef7809`  |
| 1309   | No file              | `2b0582ef7809`  |
| 1304   | No file              | `2b0582ef7809`  |
| 1292   | No file              | `2b0582ef7809`  |
| 1286   | No file              | `2b0582ef7809`  |
| 1280   | No file              | `2b0582ef7809`  |
| 1276   | No file              | `2b0582ef7809`  |
| 1267   | No file              | `2b0582ef7809`  |
| 1261   | No file              | `2b0582ef7809`  |
| 1256   | No file              | `2b0582ef7809`  |
| 1250   | No file              | `2b0582ef7809`  |
| 1246   | No file              | `2b0582ef7809`  |
| 1239   | No file              | `2b0582ef7809`  |
| 1230   | No file              | `2b0582ef7809`  |
| 1226   | No file              | `2b0582ef7809`  |
| 1220   | No file              | `2b0582ef7809`  |
| 1217   | No file              | `2b0582ef7809`  |
| 1211   | No file              | `2b0582ef7809`  |
| 1210   | No file              | `2b0582ef7809`  |
| 1208   | No file              | `2b0582ef7809`  |
| 1203   | No file              | `2b0582ef7809`  |
| 1197   | No file              | `2b0582ef7809`  |
| 1194   | No file              | `2b0582ef7809`  |
| 1192   | No file              | `2b0582ef7809`  |
| 1187   | No file              | `2b0582ef7809`  |
| 1183   | No file              | `2b0582ef7809`  |
| 1177   | No file              | `2b0582ef7809`  |
| 1173   | No file              | `2b0582ef7809`  |
| 1167   | No file              | `2b0582ef7809`  |
| 1164   | No file              | `2b0582ef7809`  |
| 1156   | No file              | `2b0582ef7809`  |
| 1149   | No file              | `2b0582ef7809`  |
| 1144   | No file              | `2b0582ef7809`  |
| 1137   | No file              | `2b0582ef7809`  |
| 1132   | No file              | `2b0582ef7809`  |
| 1127   | No file              | `2b0582ef7809`  |
| 1122   | No file              | `2b0582ef7809`  |
| 1118   | No file              | `2b0582ef7809`  |
| 1114   | No file              | `2b0582ef7809`  |
| 1109   | No file              | `2b0582ef7809`  |
| 1102   | No file              | `2b0582ef7809`  |
| 1096   | No file              | `2b0582ef7809`  |
| 1088   | No file              | `2b0582ef7809`  |
| 1081   | No file              | `2b0582ef7809`  |
| 1076   | No file              | `2b0582ef7809`  |
| 1069   | No file              | `2b0582ef7809`  |
| 1064   | No file              | `2b0582ef7809`  |
| 1058   | No file              | `2b0582ef7809`  |
| 1051   | No file              | `2b0582ef7809`  |
| 1044   | No file              | `2b0582ef7809`  |
| 1036   | No file              | `2b0582ef7809`  |
| 1026   | No file              | `2b0582ef7809`  |
| 1016   | No file              | `2b0582ef7809`  |
| 1009   | No file              | `2b0582ef7809`  |
| 1005   | No file              | `2b0582ef7809`  |
| 1000   | No file              | `2b0582ef7809`  |
| 998    | No file              | `2b0582ef7809`  |
| 990    | No file              | `2b0582ef7809`  |
| 979    | No file              | `2b0582ef7809`  |
| 972    | No file              | `2b0582ef7809`  |
| 963    | No file              | `2b0582ef7809`  |
| 955    | No file              | `2b0582ef7809`  |
| 946    | No file              | `2b0582ef7809`  |
| 938    | No file              | `2b0582ef7809`  |
| 927    | No file              | `2b0582ef7809`  |
| 911    | No file              | `2b0582ef7809`  |
| 904    | No file              | `2b0582ef7809`  |
| 899    | No file              | `2b0582ef7809`  |
| 894    | No file              | `2b0582ef7809`  |
| 885    | No file              | `2b0582ef7809`  |
| 879    | No file              | `2b0582ef7809`  |
| 872    | No file              | `2b0582ef7809`  |
| 864    | No file              | `2b0582ef7809`  |
| 855    | No file              | `2b0582ef7809`  |
| 853    | No file              | `2b0582ef7809`  |
| 845    | No file              | `2b0582ef7809`  |
| 837    | No file              | `2b0582ef7809`  |
| 829    | No file              | `2b0582ef7809`  |
| 822    | No file              | `2b0582ef7809`  |
| 814    | No file              | `2b0582ef7809`  |
| 805    | No file              | `2b0582ef7809`  |
| 794    | No file              | `2b0582ef7809`  |
| 787    | No file              | `2b0582ef7809`  |
| 780    | No file              | `2b0582ef7809`  |
| 771    | No file              | `2b0582ef7809`  |
| 760    | No file              | `2b0582ef7809`  |
| 748    | No file              | `2b0582ef7809`  |
| 741    | No file              | `2b0582ef7809`  |
| 736    | No file              | `2b0582ef7809`  |
| 731    | No file              | `2b0582ef7809`  |
| 723    | No file              | `2b0582ef7809`  |
| 711    | No file              | `2b0582ef7809`  |
| 707    | No file              | `2b0582ef7809`  |
| 697    | No file              | `2b0582ef7809`  |
| 689    | No file              | `2b0582ef7809`  |
| 683    | No file              | `2b0582ef7809`  |
| 678    | No file              | `2b0582ef7809`  |
| 670    | No file              | `2b0582ef7809`  |
| 661    | No file              | `2b0582ef7809`  |
| 656    | No file              | `2b0582ef7809`  |
| 652    | No file              | `2b0582ef7809`  |
| 643    | No file              | `2b0582ef7809`  |
| 637    | No file              | `2b0582ef7809`  |
| 630    | No file              | `2b0582ef7809`  |
| 627    | No file              | `2b0582ef7809`  |
| 621    | No file              | `2b0582ef7809`  |
| 617    | No file              | `2b0582ef7809`  |
| 615    | No file              | `2b0582ef7809`  |
| 606    | No file              | `2b0582ef7809`  |
| 599    | No file              | `2b0582ef7809`  |
| 592    | No file              | `2b0582ef7809`  |
| 586    | No file              | `2b0582ef7809`  |
| 577    | No file              | `2b0582ef7809`  |
| 569    | No file              | `2b0582ef7809`  |
| 561    | No file              | `2b0582ef7809`  |
| 554    | No file              | `2b0582ef7809`  |
| 542    | No file              | `2b0582ef7809`  |
| 532    | No file              | `2b0582ef7809`  |
| 531    | No file              | `2b0582ef7809`  |
| 526    | No file              | `2b0582ef7809`  |
| 521    | No file              | `2b0582ef7809`  |
| 517    | No file              | `2b0582ef7809`  |
| 510    | No file              | `2b0582ef7809`  |
| 508    | No file              | `2b0582ef7809`  |
| 504    | No file              | `2b0582ef7809`  |
| 497    | No file              | `2b0582ef7809`  |
| 491    | No file              | `2b0582ef7809`  |
| 485    | No file              | `2b0582ef7809`  |
| 478    | No file              | `2b0582ef7809`  |
| 472    | No file              | `2b0582ef7809`  |
| 466    | No file              | `2b0582ef7809`  |
| 457    | No file              | `2b0582ef7809`  |
| 452    | No file              | `2b0582ef7809`  |
| 449    | No file              | `2b0582ef7809`  |
| 435    | No file              | `2b0582ef7809`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                   |
| --------------------- | -------- | ---------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 97, `str_id1` = `scene_id`, `str_id4` 0 / 1 / 2 = title / description / quote |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                | Field        | Notes                                          |
| ------------------- | ------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                 | count        | Number of rows; 92 on client 3458              |
| `+0x08`             | Cutscene Row[count] | rows         | See Cutscene Row                               |
| `rows+0x00`         | String Table        | string_table | See String Table                               |
| `string_table+0x00` | u32                 | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                 | zero         | Always 0                                       |

Rows are not sorted by ID (the first three are 65, 66 and 2).

### Cutscene Row (28 bytes)

| Offset  | Type     | Field           | Notes                                                             |
| ------- | -------- | --------------- | ----------------------------------------------------------------- |
| `+0x00` | u32      | scene_id        | Unique; 2 to 260 on client 3458, with gaps                        |
| `+0x04` | u32      | title_ref       | String table index of the Korean title                            |
| `+0x08` | u32      | description_ref | String table index of the Korean recap, with stored line breaks   |
| `+0x0C` | u32      | quote_ref       | String table index of the Korean quoted line                      |
| `+0x10` | u32      | icon_ref        | String table index of the region symbol, relative to `ui_texture/` |
| `+0x14` | bytes[8] | unknown_14      | Always `0`                                                        |

### String Table (variable: 4 bytes + strings)

251 strings on client 3458, all referenced. Scenes that repeat a summary
share its entries: 43 to 47, 197 and 198, and 253 to 256 share their title,
recap and quote, 248 and 249 their title and quote, and 257 to 260 their
title. The four icons are stored once each.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 251 on client 3458  |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

Client 1784 rows are 20 bytes, without `unknown_14`, and a second table of
timed voice lines follows the rows, before the string table. Only the File
Layout and the Cutscene Row differ from Layout 2; Line Group and Line exist
only here. The parser reads only Layout 2.

### File Layout

| Offset             | Type                         | Field            | Notes                                                 |
| ------------------ | ---------------------------- | ---------------- | ----------------------------------------------------- |
| `+0x00`            | char[4]                      | magic            | ASCII `PABR`                                          |
| `+0x04`            | u32                          | count            | Number of rows; 6 on client 1784                      |
| `+0x08`            | Cutscene Row[count]          | rows             | See Cutscene Row                                      |
| `rows+0x00`        | u32                          | line_group_count | 12 on client 1784                                     |
| `rows+0x04`        | Line Group[line_group_count] | line_groups      | See Line Group                                        |
| `line_groups+0x00` | String Table                 | string_table     | See String Table                                      |
| `EOF-0x08`         | u32                          | table_start      | Offset of the string table, where the line groups end |
| `EOF-0x04`         | u32                          | zero             | Always 0                                              |

### Line Group (variable: 4 bytes + lines)

2 to 36 lines per group on client 1784.

| Offset  | Type             | Field      | Notes            |
| ------- | ---------------- | ---------- | ---------------- |
| `+0x00` | u32              | line_count | Number of lines  |
| `+0x04` | Line[line_count] | lines      | See Line         |

### Line (16 bytes)

| Offset  | Type | Field      | Notes                                                                                           |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00 | 1 to 15 on client 1784, the same value in every line of a group and unique per group; 1 to 5 and 14 are also `scene_id` values of the rows |
| `+0x04` | u32  | unknown_04 | Rises within a group in steps of thousands (0 to 165000), a time in milliseconds by its values  |
| `+0x08` | u32  | voice_ref  | String table index of a voice key (`QUEST_VCE_NEW_9027_43_1_Illezra`, `NPC_VCE_NEW_0_0_Mute_1`) |
| `+0x0C` | u32  | line_ref   | String table index of the Korean line spoken                                                    |

### Cutscene Row (20 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | scene_id        |       |
| `+0x04` | u32  | title_ref       |       |
| `+0x08` | u32  | description_ref |       |
| `+0x0C` | u32  | quote_ref       |       |
| `+0x10` | u32  | icon_ref        | String table index of the icon path; on client 1784 also quest icons (`Icon/Quest/405_1.dds`) |

## Notes

- The cutscene skip panel (`window/cutscene/panel_window_cutsceneskip_1`)
  opens in `eRenderMode_GroupCamera` and fills its title, main text, sub text
  and territory icon from `getTitle`, `getMainDescription`,
  `getSubDescription` and `getIconPath`, the four strings of a row.
- The icons mark the story region. On client 3458:
  `SymbolIcon_SnowMountain.dds` (Drieghan, 40 scenes),
  `SymbolIcon_AbyssOne.dds` (The Magnus, 19), `SymbolIcon_Valenos.dds`
  (Balenos, 18) and `SymbolIcon_Feather.dds` (Atoraxxion, 15). All four
  exist under `ui_texture/combine/icon/symbolicon/`.
- The app indexes the region icons by scene ID (`IndexKind.CUTSCENE_ICON`,
  read through `IconKind.CUTSCENE`).
