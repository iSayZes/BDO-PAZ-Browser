# `audioinfo.bss` Format

## Purpose

The world's background music and ambience by area: per area colour of
the audio map image (`AudioMap.bmp`, the `audio_map_index` `7` of
[`fieldinfo.bss`](fieldinfo_bss.md)) the four Wwise `BGM` states
the area plays and its ambience index. Since the Wwise sound system
(client 1866) the file also lists the `BGM` states of a few special
situations and the radio channels of the radio player. Client 1784 holds
the older layout with sound bank and music numbers per situation.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File            | Bytes   | Records                                   | Row bytes |
| ------ | -------------- | --------------- | ------- | ----------------------------------------- | --------- |
| 6      | 2665 and later | `audioinfo.bss` | 40,977  | 1,256 Row, 10 State Entry, 10 Radio Entry | 28        |
| 5      | 2000 to 2657   | `audioinfo.bss` | 36,534  | 1,113 Row, 10 State Entry, 10 Radio Entry | 28        |
| 4      | 1958 to 1996   | `audioinfo.bss` | 28,374  | 831 Row, 9 State Entry, 10 Radio Entry    | 28        |
| 3      | 1914 to 1937   | `audioinfo.bss` | 27,671  | 831 Row, 8 State Entry                    | 28        |
| 2      | 1866 to 1908   | `audioinfo.bss` | 27,546  | 831 Row, 5 State Entry                    | 28        |
| 1      | 1069 to 1862   | `audioinfo.bss` | 132,980 | 831 Row                                   | 160       |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 6      | `audioinfo.bss` | 40,846 B (99.7%)  | 131 B (0.3%)   |
| 5      | `audioinfo.bss` | 36,443 B (99.8%)  | 91 B (0.2%)    |
| 4      | `audioinfo.bss` | 28,285 B (99.7%)  | 89 B (0.3%)    |
| 3      | `audioinfo.bss` | 27,655 B (99.9%)  | 16 B (0.1%)    |
| 2      | `audioinfo.bss` | 27,536 B (100.0%) | 10 B (0.0%)    |
| 1      | `audioinfo.bss` | 129,656 B (97.5%) | 3,324 B (2.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 6             | `af52924c6778`  |
| 3482   | Layout 6             | `af52924c6778`  |
| 3474   | Layout 6             | `af52924c6778`  |
| 3473   | Layout 6             | `af52924c6778`  |
| 3464   | Layout 6             | `af52924c6778`  |
| 3458   | Layout 6             | `af52924c6778`  |
| 3454   | Layout 6             | `af52924c6778`  |
| 3444   | Layout 6             | `af52924c6778`  |
| 3435   | Layout 6             | `af52924c6778`  |
| 3426   | Layout 6             | `af52924c6778`  |
| 3418   | Layout 6             | `af52924c6778`  |
| 3412   | Layout 6             | `af52924c6778`  |
| 3402   | Layout 6             | `af52924c6778`  |
| 3396   | Layout 6             | `af52924c6778`  |
| 3387   | Layout 6             | `af52924c6778`  |
| 3381   | Layout 6             | `af52924c6778`  |
| 3373   | Layout 6             | `af52924c6778`  |
| 3364   | Layout 6             | `af52924c6778`  |
| 3356   | Layout 6             | `af52924c6778`  |
| 3349   | Layout 6             | `af52924c6778`  |
| 3342   | Layout 6             | `af52924c6778`  |
| 3335   | Layout 6             | `af52924c6778`  |
| 3326   | Layout 6             | `af52924c6778`  |
| 3321   | Layout 6             | `af52924c6778`  |
| 3314   | Layout 6             | `af52924c6778`  |
| 3303   | Layout 6             | `af52924c6778`  |
| 3302   | Layout 6             | `af52924c6778`  |
| 3293   | Layout 6             | `af52924c6778`  |
| 3283   | Layout 6             | `af52924c6778`  |
| 3275   | Layout 6             | `af52924c6778`  |
| 3267   | Layout 6             | `af52924c6778`  |
| 3258   | Layout 6             | `af52924c6778`  |
| 3251   | Layout 6             | `af52924c6778`  |
| 3242   | Layout 6             | `af52924c6778`  |
| 3235   | Layout 6             | `af52924c6778`  |
| 3229   | Layout 6             | `af52924c6778`  |
| 3212   | Layout 6             | `af52924c6778`  |
| 3203   | Layout 6             | `af52924c6778`  |
| 3193   | Layout 6             | `af52924c6778`  |
| 3186   | Layout 6             | `af52924c6778`  |
| 3177   | Layout 6             | `af52924c6778`  |
| 3169   | Layout 6             | `af52924c6778`  |
| 3158   | Layout 6             | `af52924c6778`  |
| 3151   | Layout 6             | `af52924c6778`  |
| 3144   | Layout 6             | `af52924c6778`  |
| 3133   | Layout 6             | `af52924c6778`  |
| 3125   | Layout 6             | `af52924c6778`  |
| 3118   | Layout 6             | `af52924c6778`  |
| 3111   | Layout 6             | `af52924c6778`  |
| 3103   | Layout 6             | `af52924c6778`  |
| 3095   | Layout 6             | `af52924c6778`  |
| 3086   | Layout 6             | `af52924c6778`  |
| 3072   | Layout 6             | `af52924c6778`  |
| 3062   | Layout 6             | `af52924c6778`  |
| 3052   | Layout 6             | `af52924c6778`  |
| 3045   | Layout 6             | `af52924c6778`  |
| 3037   | Layout 6             | `af52924c6778`  |
| 3030   | Layout 6             | `af52924c6778`  |
| 3021   | Layout 6             | `af52924c6778`  |
| 3012   | Layout 6             | `af52924c6778`  |
| 3002   | Layout 6             | `af52924c6778`  |
| 2995   | Layout 6             | `af52924c6778`  |
| 2987   | Layout 6             | `af52924c6778`  |
| 2978   | Layout 6             | `af52924c6778`  |
| 2970   | Layout 6             | `af52924c6778`  |
| 2959   | Layout 6             | `af52924c6778`  |
| 2951   | Layout 6             | `af52924c6778`  |
| 2942   | Layout 6             | `af52924c6778`  |
| 2935   | Layout 6             | `af52924c6778`  |
| 2932   | Layout 6             | `af52924c6778`  |
| 2923   | Layout 6             | `af52924c6778`  |
| 2919   | Layout 6             | `af52924c6778`  |
| 2907   | Layout 6             | `af52924c6778`  |
| 2900   | Layout 6             | `af52924c6778`  |
| 2891   | Layout 6             | `af52924c6778`  |
| 2882   | Layout 6             | `af52924c6778`  |
| 2872   | Layout 6             | `af52924c6778`  |
| 2863   | Layout 6             | `af52924c6778`  |
| 2855   | Layout 6             | `af52924c6778`  |
| 2849   | Layout 6             | `af52924c6778`  |
| 2844   | Layout 6             | `af52924c6778`  |
| 2834   | Layout 6             | `af52924c6778`  |
| 2825   | Layout 6             | `af52924c6778`  |
| 2819   | Layout 6             | `af52924c6778`  |
| 2811   | Layout 6             | `af52924c6778`  |
| 2803   | Layout 6             | `af52924c6778`  |
| 2794   | Layout 6             | `af52924c6778`  |
| 2783   | Layout 6             | `af52924c6778`  |
| 2774   | Layout 6             | `af52924c6778`  |
| 2765   | Layout 6             | `af52924c6778`  |
| 2756   | Layout 6             | `af52924c6778`  |
| 2750   | Layout 6             | `af52924c6778`  |
| 2743   | Layout 6             | `af52924c6778`  |
| 2736   | Layout 6             | `af52924c6778`  |
| 2726   | Layout 6             | `af52924c6778`  |
| 2717   | Layout 6             | `af52924c6778`  |
| 2709   | Layout 6             | `af52924c6778`  |
| 2703   | Layout 6             | `af52924c6778`  |
| 2695   | Layout 6             | `af52924c6778`  |
| 2684   | Layout 6             | `af52924c6778`  |
| 2672   | Layout 6             | `af52924c6778`  |
| 2665   | Layout 6             | `af52924c6778`  |
| 2657   | Layout 5             | `af52924c6778`  |
| 2649   | Layout 5             | `af52924c6778`  |
| 2644   | Layout 5             | `af52924c6778`  |
| 2637   | Layout 5             | `af52924c6778`  |
| 2629   | Layout 5             | `af52924c6778`  |
| 2619   | Layout 5             | `af52924c6778`  |
| 2612   | Layout 5             | `af52924c6778`  |
| 2606   | Layout 5             | `af52924c6778`  |
| 2602   | Layout 5             | `af52924c6778`  |
| 2601   | Layout 5             | `af52924c6778`  |
| 2592   | Layout 5             | `af52924c6778`  |
| 2583   | Layout 5             | `af52924c6778`  |
| 2575   | Layout 5             | `af52924c6778`  |
| 2567   | Layout 5             | `af52924c6778`  |
| 2560   | Layout 5             | `af52924c6778`  |
| 2553   | Layout 5             | `af52924c6778`  |
| 2545   | Layout 5             | `af52924c6778`  |
| 2538   | Layout 5             | `af52924c6778`  |
| 2529   | Layout 5             | `af52924c6778`  |
| 2519   | Layout 5             | `af52924c6778`  |
| 2513   | Layout 5             | `af52924c6778`  |
| 2510   | Layout 5             | `af52924c6778`  |
| 2507   | Layout 5             | `af52924c6778`  |
| 2503   | Layout 5             | `af52924c6778`  |
| 2498   | Layout 5             | `af52924c6778`  |
| 2492   | Layout 5             | `af52924c6778`  |
| 2487   | Layout 5             | `af52924c6778`  |
| 2480   | Layout 5             | `af52924c6778`  |
| 2474   | Layout 5             | `af52924c6778`  |
| 2468   | Layout 5             | `af52924c6778`  |
| 2460   | Layout 5             | `af52924c6778`  |
| 2453   | Layout 5             | `af52924c6778`  |
| 2444   | Layout 5             | `af52924c6778`  |
| 2438   | Layout 5             | `af52924c6778`  |
| 2434   | Layout 5             | `af52924c6778`  |
| 2429   | Layout 5             | `af52924c6778`  |
| 2421   | Layout 5             | `af52924c6778`  |
| 2414   | Layout 5             | `af52924c6778`  |
| 2407   | Layout 5             | `af52924c6778`  |
| 2401   | Layout 5             | `af52924c6778`  |
| 2397   | Layout 5             | `af52924c6778`  |
| 2393   | Layout 5             | `af52924c6778`  |
| 2384   | Layout 5             | `af52924c6778`  |
| 2378   | Layout 5             | `af52924c6778`  |
| 2372   | Layout 5             | `af52924c6778`  |
| 2358   | Layout 5             | `af52924c6778`  |
| 2352   | Layout 5             | `af52924c6778`  |
| 2347   | Layout 5             | `af52924c6778`  |
| 2343   | Layout 5             | `af52924c6778`  |
| 2335   | Layout 5             | `af52924c6778`  |
| 2327   | Layout 5             | `af52924c6778`  |
| 2324   | Layout 5             | `af52924c6778`  |
| 2319   | Layout 5             | `af52924c6778`  |
| 2313   | Layout 5             | `af52924c6778`  |
| 2308   | Layout 5             | `af52924c6778`  |
| 2302   | Layout 5             | `af52924c6778`  |
| 2295   | Layout 5             | `af52924c6778`  |
| 2290   | Layout 5             | `af52924c6778`  |
| 2284   | Layout 5             | `af52924c6778`  |
| 2276   | Layout 5             | `af52924c6778`  |
| 2269   | Layout 5             | `af52924c6778`  |
| 2259   | Layout 5             | `af52924c6778`  |
| 2250   | Layout 5             | `af52924c6778`  |
| 2243   | Layout 5             | `af52924c6778`  |
| 2235   | Layout 5             | `af52924c6778`  |
| 2229   | Layout 5             | `af52924c6778`  |
| 2224   | Layout 5             | `af52924c6778`  |
| 2218   | Layout 5             | `af52924c6778`  |
| 2215   | Layout 5             | `af52924c6778`  |
| 2207   | Layout 5             | `af52924c6778`  |
| 2203   | Layout 5             | `af52924c6778`  |
| 2196   | Layout 5             | `af52924c6778`  |
| 2192   | Layout 5             | `af52924c6778`  |
| 2189   | Layout 5             | `af52924c6778`  |
| 2183   | Layout 5             | `af52924c6778`  |
| 2179   | Layout 5             | `af52924c6778`  |
| 2171   | Layout 5             | `af52924c6778`  |
| 2163   | Layout 5             | `af52924c6778`  |
| 2156   | Layout 5             | `af52924c6778`  |
| 2151   | Layout 5             | `af52924c6778`  |
| 2147   | Layout 5             | `af52924c6778`  |
| 2142   | Layout 5             | `af52924c6778`  |
| 2138   | Layout 5             | `af52924c6778`  |
| 2134   | Layout 5             | `af52924c6778`  |
| 2130   | Layout 5             | `af52924c6778`  |
| 2122   | Layout 5             | `af52924c6778`  |
| 2107   | Layout 5             | `af52924c6778`  |
| 2098   | Layout 5             | `af52924c6778`  |
| 2089   | Layout 5             | `af52924c6778`  |
| 2081   | Layout 5             | `af52924c6778`  |
| 2073   | Layout 5             | `af52924c6778`  |
| 2067   | Layout 5             | `af52924c6778`  |
| 2063   | Layout 5             | `af52924c6778`  |
| 2059   | Layout 5             | `af52924c6778`  |
| 2052   | Layout 5             | `af52924c6778`  |
| 2044   | Layout 5             | `af52924c6778`  |
| 2039   | Layout 5             | `af52924c6778`  |
| 2032   | Layout 5             | `af52924c6778`  |
| 2025   | Layout 5             | `af52924c6778`  |
| 2011   | Layout 5             | `af52924c6778`  |
| 2005   | Layout 5             | `af52924c6778`  |
| 2000   | Layout 5             | `af52924c6778`  |
| 1996   | Layout 4             | `af52924c6778`  |
| 1991   | Layout 4             | `af52924c6778`  |
| 1985   | Layout 4             | `af52924c6778`  |
| 1980   | Layout 4             | `af52924c6778`  |
| 1969   | Layout 4             | `af52924c6778`  |
| 1964   | Layout 4             | `af52924c6778`  |
| 1958   | Layout 4             | `af52924c6778`  |
| 1950   | No documented layout | `af52924c6778`  |
| 1945   | No documented layout | `af52924c6778`  |
| 1937   | Layout 3             | `af52924c6778`  |
| 1933   | Layout 3             | `af52924c6778`  |
| 1927   | Layout 3             | `af52924c6778`  |
| 1921   | Layout 3             | `af52924c6778`  |
| 1914   | Layout 3             | `af52924c6778`  |
| 1908   | Layout 2             | `af52924c6778`  |
| 1897   | Layout 2             | `af52924c6778`  |
| 1892   | Layout 2             | `af52924c6778`  |
| 1886   | Layout 2             | `af52924c6778`  |
| 1881   | Layout 2             | `af52924c6778`  |
| 1871   | Layout 2             | `af52924c6778`  |
| 1866   | Layout 2             | `af52924c6778`  |
| 1862   | Layout 1             | `af52924c6778`  |
| 1854   | Layout 1             | `af52924c6778`  |
| 1846   | Layout 1             | `af52924c6778`  |
| 1838   | Layout 1             | `af52924c6778`  |
| 1832   | Layout 1             | `af52924c6778`  |
| 1826   | Layout 1             | `af52924c6778`  |
| 1822   | Layout 1             | `af52924c6778`  |
| 1818   | Layout 1             | `af52924c6778`  |
| 1804   | Layout 1             | `af52924c6778`  |
| 1794   | Layout 1             | `af52924c6778`  |
| 1790   | Layout 1             | `af52924c6778`  |
| 1784   | Layout 1             | `af52924c6778`  |
| 1774   | Layout 1             | `af52924c6778`  |
| 1771   | Layout 1             | `af52924c6778`  |
| 1762   | Layout 1             | `af52924c6778`  |
| 1759   | Layout 1             | `af52924c6778`  |
| 1754   | Layout 1             | `af52924c6778`  |
| 1749   | Layout 1             | `af52924c6778`  |
| 1743   | Layout 1             | `af52924c6778`  |
| 1737   | Layout 1             | `af52924c6778`  |
| 1731   | Layout 1             | `af52924c6778`  |
| 1725   | Layout 1             | `af52924c6778`  |
| 1717   | Layout 1             | `af52924c6778`  |
| 1710   | Layout 1             | `af52924c6778`  |
| 1704   | Layout 1             | `af52924c6778`  |
| 1698   | Layout 1             | `af52924c6778`  |
| 1690   | Layout 1             | `af52924c6778`  |
| 1685   | Layout 1             | `af52924c6778`  |
| 1680   | Layout 1             | `af52924c6778`  |
| 1674   | Layout 1             | `af52924c6778`  |
| 1668   | Layout 1             | `af52924c6778`  |
| 1659   | Layout 1             | `af52924c6778`  |
| 1649   | Layout 1             | `af52924c6778`  |
| 1642   | Layout 1             | `af52924c6778`  |
| 1636   | Layout 1             | `af52924c6778`  |
| 1628   | Layout 1             | `af52924c6778`  |
| 1622   | Layout 1             | `af52924c6778`  |
| 1614   | Layout 1             | `af52924c6778`  |
| 1608   | Layout 1             | `af52924c6778`  |
| 1602   | Layout 1             | `af52924c6778`  |
| 1598   | Layout 1             | `af52924c6778`  |
| 1594   | Layout 1             | `af52924c6778`  |
| 1590   | Layout 1             | `af52924c6778`  |
| 1587   | Layout 1             | `af52924c6778`  |
| 1584   | Layout 1             | `af52924c6778`  |
| 1579   | Layout 1             | `af52924c6778`  |
| 1572   | Layout 1             | `af52924c6778`  |
| 1565   | Layout 1             | `af52924c6778`  |
| 1559   | Layout 1             | `af52924c6778`  |
| 1554   | Layout 1             | `af52924c6778`  |
| 1547   | Layout 1             | `af52924c6778`  |
| 1537   | Layout 1             | `af52924c6778`  |
| 1529   | Layout 1             | `af52924c6778`  |
| 1524   | Layout 1             | `af52924c6778`  |
| 1519   | Layout 1             | `af52924c6778`  |
| 1509   | Layout 1             | `af52924c6778`  |
| 1506   | Layout 1             | `af52924c6778`  |
| 1504   | Layout 1             | `af52924c6778`  |
| 1500   | Layout 1             | `af52924c6778`  |
| 1493   | Layout 1             | `af52924c6778`  |
| 1489   | Layout 1             | `af52924c6778`  |
| 1485   | Layout 1             | `af52924c6778`  |
| 1481   | Layout 1             | `af52924c6778`  |
| 1474   | Layout 1             | `af52924c6778`  |
| 1466   | Layout 1             | `af52924c6778`  |
| 1462   | Layout 1             | `af52924c6778`  |
| 1459   | Layout 1             | `af52924c6778`  |
| 1453   | Layout 1             | `af52924c6778`  |
| 1450   | Layout 1             | `af52924c6778`  |
| 1445   | Layout 1             | `af52924c6778`  |
| 1439   | Layout 1             | `af52924c6778`  |
| 1433   | Layout 1             | `af52924c6778`  |
| 1430   | Layout 1             | `af52924c6778`  |
| 1426   | Layout 1             | `af52924c6778`  |
| 1421   | Layout 1             | `af52924c6778`  |
| 1417   | Layout 1             | `af52924c6778`  |
| 1416   | Layout 1             | `af52924c6778`  |
| 1409   | Layout 1             | `af52924c6778`  |
| 1405   | Layout 1             | `af52924c6778`  |
| 1401   | Layout 1             | `af52924c6778`  |
| 1396   | Layout 1             | `af52924c6778`  |
| 1391   | Layout 1             | `af52924c6778`  |
| 1390   | Layout 1             | `af52924c6778`  |
| 1386   | Layout 1             | `af52924c6778`  |
| 1381   | Layout 1             | `af52924c6778`  |
| 1379   | Layout 1             | `af52924c6778`  |
| 1372   | Layout 1             | `af52924c6778`  |
| 1366   | Layout 1             | `af52924c6778`  |
| 1364   | Layout 1             | `af52924c6778`  |
| 1363   | Layout 1             | `af52924c6778`  |
| 1360   | Layout 1             | `af52924c6778`  |
| 1358   | Layout 1             | `af52924c6778`  |
| 1355   | Layout 1             | `af52924c6778`  |
| 1351   | Layout 1             | `af52924c6778`  |
| 1348   | Layout 1             | `af52924c6778`  |
| 1346   | Layout 1             | `af52924c6778`  |
| 1341   | Layout 1             | `af52924c6778`  |
| 1340   | Layout 1             | `af52924c6778`  |
| 1338   | Layout 1             | `af52924c6778`  |
| 1335   | Layout 1             | `af52924c6778`  |
| 1333   | Layout 1             | `af52924c6778`  |
| 1329   | Layout 1             | `af52924c6778`  |
| 1327   | Layout 1             | `af52924c6778`  |
| 1324   | Layout 1             | `af52924c6778`  |
| 1321   | Layout 1             | `af52924c6778`  |
| 1319   | Layout 1             | `af52924c6778`  |
| 1318   | Layout 1             | `af52924c6778`  |
| 1316   | Layout 1             | `af52924c6778`  |
| 1313   | Layout 1             | `af52924c6778`  |
| 1311   | Layout 1             | `af52924c6778`  |
| 1309   | Layout 1             | `af52924c6778`  |
| 1304   | Layout 1             | `af52924c6778`  |
| 1292   | Layout 1             | `af52924c6778`  |
| 1286   | Layout 1             | `af52924c6778`  |
| 1280   | Layout 1             | `af52924c6778`  |
| 1276   | Layout 1             | `af52924c6778`  |
| 1267   | Layout 1             | `af52924c6778`  |
| 1261   | Layout 1             | `af52924c6778`  |
| 1256   | Layout 1             | `af52924c6778`  |
| 1250   | Layout 1             | `af52924c6778`  |
| 1246   | Layout 1             | `af52924c6778`  |
| 1239   | Layout 1             | `af52924c6778`  |
| 1230   | Layout 1             | `af52924c6778`  |
| 1226   | Layout 1             | `af52924c6778`  |
| 1220   | Layout 1             | `af52924c6778`  |
| 1217   | Layout 1             | `af52924c6778`  |
| 1211   | Layout 1             | `af52924c6778`  |
| 1210   | Layout 1             | `af52924c6778`  |
| 1208   | Layout 1             | `af52924c6778`  |
| 1203   | Layout 1             | `af52924c6778`  |
| 1197   | Layout 1             | `af52924c6778`  |
| 1194   | Layout 1             | `af52924c6778`  |
| 1192   | Layout 1             | `af52924c6778`  |
| 1187   | Layout 1             | `af52924c6778`  |
| 1183   | Layout 1             | `af52924c6778`  |
| 1177   | Layout 1             | `af52924c6778`  |
| 1173   | Layout 1             | `af52924c6778`  |
| 1167   | Layout 1             | `af52924c6778`  |
| 1164   | Layout 1             | `af52924c6778`  |
| 1156   | Layout 1             | `af52924c6778`  |
| 1149   | Layout 1             | `af52924c6778`  |
| 1144   | Layout 1             | `af52924c6778`  |
| 1137   | Layout 1             | `af52924c6778`  |
| 1132   | Layout 1             | `af52924c6778`  |
| 1127   | Layout 1             | `af52924c6778`  |
| 1122   | Layout 1             | `af52924c6778`  |
| 1118   | Layout 1             | `af52924c6778`  |
| 1114   | Layout 1             | `af52924c6778`  |
| 1109   | Layout 1             | `af52924c6778`  |
| 1102   | Layout 1             | `af52924c6778`  |
| 1096   | Layout 1             | `af52924c6778`  |
| 1088   | Layout 1             | `af52924c6778`  |
| 1081   | Layout 1             | `af52924c6778`  |
| 1076   | Layout 1             | `af52924c6778`  |
| 1069   | Layout 1             | `af52924c6778`  |
| 1064   | No documented layout | `af52924c6778`  |
| 1058   | No documented layout | `af52924c6778`  |
| 1051   | No documented layout | `af52924c6778`  |
| 1044   | No documented layout | `af52924c6778`  |
| 1036   | No documented layout | `af52924c6778`  |
| 1026   | No documented layout | `af52924c6778`  |
| 1016   | No documented layout | `af52924c6778`  |
| 1009   | No documented layout | `af52924c6778`  |
| 1005   | No documented layout | `af52924c6778`  |
| 1000   | No documented layout | `af52924c6778`  |
| 998    | No documented layout | `af52924c6778`  |
| 990    | No documented layout | `af52924c6778`  |
| 979    | No documented layout | `af52924c6778`  |
| 972    | No documented layout | `af52924c6778`  |
| 963    | No documented layout | `af52924c6778`  |
| 955    | No documented layout | `af52924c6778`  |
| 946    | No documented layout | `af52924c6778`  |
| 938    | No documented layout | `af52924c6778`  |
| 927    | No documented layout | `af52924c6778`  |
| 911    | No documented layout | `af52924c6778`  |
| 904    | No documented layout | `af52924c6778`  |
| 899    | No documented layout | `af52924c6778`  |
| 894    | No documented layout | `af52924c6778`  |
| 885    | No documented layout | `af52924c6778`  |
| 879    | No documented layout | `af52924c6778`  |
| 872    | No documented layout | `af52924c6778`  |
| 864    | No documented layout | `af52924c6778`  |
| 855    | No documented layout | `af52924c6778`  |
| 853    | No documented layout | `af52924c6778`  |
| 845    | No documented layout | `af52924c6778`  |
| 837    | No documented layout | `af52924c6778`  |
| 829    | No documented layout | `af52924c6778`  |
| 822    | No documented layout | `af52924c6778`  |
| 814    | No documented layout | `af52924c6778`  |
| 805    | No documented layout | `af52924c6778`  |
| 794    | No documented layout | `af52924c6778`  |
| 787    | No documented layout | `af52924c6778`  |
| 780    | No documented layout | `af52924c6778`  |
| 771    | No documented layout | `af52924c6778`  |
| 760    | No documented layout | `af52924c6778`  |
| 748    | No documented layout | `af52924c6778`  |
| 741    | No documented layout | `af52924c6778`  |
| 736    | No documented layout | `af52924c6778`  |
| 731    | No documented layout | `af52924c6778`  |
| 723    | No documented layout | `af52924c6778`  |
| 711    | No documented layout | `af52924c6778`  |
| 707    | No documented layout | `af52924c6778`  |
| 697    | No documented layout | `af52924c6778`  |
| 689    | No documented layout | `af52924c6778`  |
| 683    | No documented layout | `af52924c6778`  |
| 678    | No documented layout | `af52924c6778`  |
| 670    | No documented layout | `af52924c6778`  |
| 661    | No documented layout | `af52924c6778`  |
| 656    | No documented layout | `af52924c6778`  |
| 652    | No documented layout | `af52924c6778`  |
| 643    | No documented layout | `af52924c6778`  |
| 637    | No documented layout | `af52924c6778`  |
| 630    | No documented layout | `af52924c6778`  |
| 627    | No documented layout | `af52924c6778`  |
| 621    | No documented layout | `af52924c6778`  |
| 617    | No documented layout | `af52924c6778`  |
| 615    | No documented layout | `af52924c6778`  |
| 606    | No documented layout | `af52924c6778`  |
| 599    | No documented layout | `af52924c6778`  |
| 592    | No documented layout | `af52924c6778`  |
| 586    | No documented layout | `af52924c6778`  |
| 577    | No documented layout | `af52924c6778`  |
| 569    | No documented layout | `af52924c6778`  |
| 561    | No documented layout | `af52924c6778`  |
| 554    | No documented layout | `af52924c6778`  |
| 542    | No documented layout | `af52924c6778`  |
| 532    | No documented layout | `af52924c6778`  |
| 531    | No documented layout | `af52924c6778`  |
| 526    | No documented layout | `af52924c6778`  |
| 521    | No documented layout | `af52924c6778`  |
| 517    | No documented layout | `af52924c6778`  |
| 510    | No documented layout | `af52924c6778`  |
| 508    | No documented layout | `af52924c6778`  |
| 504    | No documented layout | `af52924c6778`  |
| 497    | No documented layout | `af52924c6778`  |
| 491    | No documented layout | `af52924c6778`  |
| 485    | No documented layout | `af52924c6778`  |
| 478    | No documented layout | `af52924c6778`  |
| 472    | No documented layout | `af52924c6778`  |
| 466    | No documented layout | `af52924c6778`  |
| 457    | No documented layout | `af52924c6778`  |
| 452    | No documented layout | `af52924c6778`  |
| 449    | No documented layout | `af52924c6778`  |
| 435    | No documented layout | `af52924c6778`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[10]          | state_entries      | No count in the file; see State Entry Count             |
| `rows+0x64`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x68`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | 17 values from `0` to `60` in rising order on client 3482 |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table, where `unknown_tail` ends    |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

### Row (28 bytes)

| Offset  | Type   | Field               | Notes                                                                                     |
| ------- | ------ | ------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32    | color               | Area colour as `0x00RRGGBB`; each colour once                                             |
| `+0x04` | u32    | color_dup           | Equals `color` on every row                                                               |
| `+0x08` | u32[4] | bgm_states          | Indexes into `strings`: four states of the Wwise `BGM` state group (`W01_Balenos_Exploration_Motivated`); see BGM State Slots |
| `+0x18` | u32    | bank_no_environment | Ambience: the Wwise `ENV_INDEX_<n>` state; `0` on 226 of 1,256 rows (client 3482)         |

The rows are in no colour order.

### State Entry (10 bytes)

| Offset  | Type | Field       | Notes                                                                             |
| ------- | ---- | ----------- | --------------------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00  | `0` to `9`, each once, in no order (client 3482)                                  |
| `+0x01` | u8   | unknown_01  | `51` to `55`, or `255` on four entries                                             |
| `+0x02` | u32  | state_group | Index into `strings`: the Wwise state group, `BGM` on every entry                 |
| `+0x06` | u32  | state_name  | Index into `strings`: the state (`W00_ArenaOfSolare_Round_Start`)                 |

### Radio Entry (17 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00   | `1` to `10` in file order on client 3482                                                |
| `+0x04` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or an empty string                      |
| `+0x08` | u32  | channel_name | Index into `strings`: the channel title (`City Jazz Vibes (feat. Jazz in Black Desert)`), UTF-16LE; empty for entries 1 and 2 |
| `+0x0C` | u32  | event_name   | Index into `strings`: the Wwise event (`BGM_Radio_Chanel_01`, `BGM_Radio_off`)           |
| `+0x10` | u8   | unknown_10   | `1` on the eight channels, `0` on entries 1 and 2                                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | State and event names, UTF-8; the channel titles and one empty string UTF-16LE; a string several rows use is stored once |

## Layout 5

The radio entries have no leading `unknown_00`. Only the Radio Entry
differs from Layout 6.

### Radio Entry (13 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or empty |
| `+0x04` | u32  | channel_name | Index into `strings`: the channel title                  |
| `+0x08` | u32  | event_name   | Index into `strings`: the Wwise event                    |
| `+0x0C` | u8   | unknown_10   | `1` on the eight channels                                |

## Layout 4

Nine state entries. Only the File Layout differs from Layout 5.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[9]           | state_entries      | No count in the file; keys `0` to `8`                    |
| `rows+0x5A`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x5E`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | The same 17 values as on client 3482                     |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 3

Eight state entries and no radio entries or tail. Only the File Layout
differs from Layout 4.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[8]           | state_entries      | No count in the file; keys `0` to `7`                    |
| `rows+0x50`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 2

Five state entries and no radio entries or tail. Only the File Layout
differs from Layout 3.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[5]           | state_entries      | No count in the file; keys `0` to `4`                    |
| `rows+0x32`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 1

The sound bank system before Wwise: per area colour a sound bank and a
music number for each of 18 situations, and no state entries. The string
table is empty. The File Layout and the Row differ from Layout 2.

### File Layout

| Offset              | Type           | Field              | Notes                                   |
| ------------------- | -------------- | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                            |
| `+0x04`             | u32            | row_count          | Number of area colours                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                 |
| `rows+0x00`         | String Table   | string_table       | `string_count` `0` on client 1784       |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table              |
| `string_table+0x04` | u32            | zero               | `0`                                     |

### Row (160 bytes)

| Offset  | Type    | Field               | Notes                                                           |
| ------- | ------- | ------------------- | --------------------------------------------------------------- |
| `+0x00` | u32     | color               | Area colour as `0x00RRGGBB`; each colour once                   |
| `+0x04` | u32     | color_dup           | Equals `color` on every row                                     |
| `+0x08` | u32[18] | bank_nos            | Sound bank per situation, in the order of Situations            |
| `+0x50` | u32[18] | music_indexes       | Music number in that bank per situation, same order             |
| `+0x98` | u32     | unknown_98          | `1` on every row of client 1784                                 |
| `+0x9C` | u32     | bank_no_environment | Ambience bank                                                   |

## Situations

The order of `bank_nos` and `music_indexes` in Layout 1, with the column
pair of the client 1784 sheet each slot matches:

| Slot | Columns                                              |
| ---- | ---------------------------------------------------- |
| 0    | `BankNo_NormaiDay`, `MusicIdx_NormaiDay`             |
| 1    | `BankNo_NormaiNight`, `MusicIdx_NormaiNight`         |
| 2    | `BankNo_CombatLv1`, `MusicIdx_CombatLv1`             |
| 3    | `BankNo_CombatLv2`, `MusicIdx_CombatLv2`             |
| 4    | `BankNo_CombatNightLv1`, `MusicIdx_CombatNightLv1`   |
| 5    | `BankNo_CombatNightLv2`, `MusicIdx_CombatNightLv2`   |
| 6    | `BankNo_CombatBoss`, `MusicIdx_CombatBoss`           |
| 7    | `BankNo_CombatHpLow`, `MusicIdx_CombatHpLow`         |
| 8    | `BankNo_Riding`, `MusicIdx_Riding`                   |
| 9    | `BankNo_Racing`, `MusicIdx_Racing`                   |
| 10   | `BankNo_VillageSiege`, `MusicIdx_VillageSiege`       |
| 11   | `BankNo_Siegewarfare`, `MusicIdx_Siegewarfare`       |
| 12   | `BankNo_GuildTeamBattle`, `MusicIdx_GuildTeamBattle` |
| 13   | `BankNo_BattleRoyale`, `MusicIdx_BattleRoyale`       |
| 14   | `BankNo_BattleRoyaleLobby`, `MusicIdx_BattleRoyaleLobby` |
| 15   | `BankNo_BattleRoyaleLostRegion`, `MusicIdx_BattleRoyaleLostRegion` |
| 16   | `BankNo_NationSiegeStart`, `MusicIdx_NationSiegeStart` |
| 17   | `BankNo_Undersea`, `MusicIdx_Undersea`               |

## State Entry Count

No field holds the number of state entries; it grew from 5 (clients 1866
and 1886) to 8, 9 and 10 (client 2107 and later), one entry per new key,
so each count is its own layout. A reader can only check a count by
walking the rest of the file to the string table.

## BGM State Slots

The names the four `bgm_states` slots hold most often on client 3482
(the part after the area prefix, `W01_Balenos_`):

| Slot | Most frequent names                                                        |
| ---- | -------------------------------------------------------------------------- |
| 0    | `Exploration_Motivated` (294 rows), `Exploration_Peaceful` (105)           |
| 1    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Battle_General` (84) |
| 2    | `Battle_Boss` (866)                                                        |
| 3    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Diving` (83) |

Areas with combat or underwater music fill slot 1 with a `Battle_General`
and slot 3 with a `Diving` state; elsewhere slots 0, 1 and 3 hold the same
state.

## Field Names

The `AudioMap_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `RegionGroupKey`, `R`, `G`, `B`,
`AreaName`, `BankNo_Environment` and a `BankNo_` and `MusicIdx_` pair per
situation. Joined on `R`, `G`, `B` = `color`, 811 of 811 sheet rows have a
Layout 1 row (client 1784). `bank_no_environment` matches on 811 of 811,
the 18 `music_indexes` on 811 of 811 each. `bank_nos` slot 7 matches on
811 of 811 and the other 17 slots on 810: the sheet row `1087` holds bank
`109` in them where the file holds `110`.
`Index`, `RegionGroupKey` and the `AreaName` note are not in the file.

In Layout 3, `bank_no_environment` equals the client 1784 value on 810 of
the 811 colours both clients have (client 3482), and every value is an
`ENV_INDEX_<n>` state of `sound2022/wwise_ids.h`. That header lists the
`bgm_states` and `state_name` strings under the `BGM` state group, and
the radio `event_name` strings under its events. The `AudioRenewal_Table`
sheet of client 1784 has the columns `Index`, `AudioStateGroupName`,
`AudioStateName` and `ContentsGroupKey` and no rows; it fits the State
Entry, but with no rows no value can confirm it.

## Open Questions

### BGM State Slot Meaning

Which situation each `bgm_states` slot plays is not confirmed. The names
point at normal play (slot 0), combat (slot 1), boss fights (slot 2) and
underwater (slot 3), the Layout 1 situations `NormaiDay`, `CombatLv1`,
`CombatBoss` and `Undersea`.

### State Entry Keys

`unknown_00` of the state entries runs `0` to `9` and `unknown_01` holds
`51` to `55` or `255`. The states (`W00_ArenaOfSolare_Round_Start`,
`W00_Ocean_Battle_PVP`, `W01_PapuCrioWar_Default`) suggest a key per
special situation (an arena round, a sea battle); `unknown_01` may be a
contents group or a priority.

### Radio Tail

`unknown_tail` (17 rising values up to `60`) follows the radio entries and
matches no key in the file.

### Layout Before Client 1109

Clients 435 to 822 hold a file no layout reads (85,652 bytes on client
822); clients 855 to 1076 have none. Its rows are larger than the Layout 1
row.
