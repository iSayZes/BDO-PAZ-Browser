# `mansionlandinfo.bss` Format

## Purpose

The manors a player rents by the day: one fixed 93-byte row per manor with
the land and building house keys, the contribution points the land costs,
the manor's region, its area as a sector box, the quest that unlocks the
rental and the daily price. Client 3474 lists Blue Maned Lion's Manor and
the three Land of the Morning Light manors Shimhyangje, Solbaram Neowa
House and Hyeollokdang. The manor contract window
(`panel_window_mansioncontract_all_1.luac`) knows the four land keys as
`_eMansionKey` and reads the contribution cost with
`ToClient_getNeenPointMansion(characterKey)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records               | Row bytes |
| ------ | -------------- | --------------------- | ----- | --------------------- | --------- |
| 3      | 1602 and later | `mansionlandinfo.bss` | 392   | 4 Row                 | 93        |
| 2      | 2189 to 2601   | `mansionlandinfo.bss` | 251   | 3 Row                 | 77        |
| 1      | 1737 to 2163   | `mansionlandinfo.bss` | 88    | 1 Row, 1 String Table | 68        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 3      | `mansionlandinfo.bss` | 180 B (45.9%) | 212 B (54.1%) |
| 2      | `mansionlandinfo.bss` | 140 B (55.8%) | 111 B (44.2%) |
| 1      | `mansionlandinfo.bss` | 60 B (68.2%)  | 28 B (31.8%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `25b1d657d893`  |
| 3482   | Layout 3             | `25b1d657d893`  |
| 3474   | Layout 3             | `25b1d657d893`  |
| 3473   | Layout 3             | `25b1d657d893`  |
| 3464   | Layout 3             | `25b1d657d893`  |
| 3458   | Layout 3             | `25b1d657d893`  |
| 3454   | Layout 3             | `25b1d657d893`  |
| 3444   | Layout 3             | `25b1d657d893`  |
| 3435   | Layout 3             | `25b1d657d893`  |
| 3426   | Layout 3             | `25b1d657d893`  |
| 3418   | Layout 3             | `25b1d657d893`  |
| 3412   | Layout 3             | `25b1d657d893`  |
| 3402   | Layout 3             | `25b1d657d893`  |
| 3396   | Layout 3             | `25b1d657d893`  |
| 3387   | Layout 3             | `25b1d657d893`  |
| 3381   | Layout 3             | `25b1d657d893`  |
| 3373   | Layout 3             | `25b1d657d893`  |
| 3364   | Layout 3             | `25b1d657d893`  |
| 3356   | Layout 3             | `25b1d657d893`  |
| 3349   | Layout 3             | `25b1d657d893`  |
| 3342   | Layout 3             | `25b1d657d893`  |
| 3335   | Layout 3             | `25b1d657d893`  |
| 3326   | Layout 3             | `25b1d657d893`  |
| 3321   | Layout 3             | `25b1d657d893`  |
| 3314   | Layout 3             | `25b1d657d893`  |
| 3303   | Layout 3             | `25b1d657d893`  |
| 3302   | Layout 3             | `25b1d657d893`  |
| 3293   | Layout 3             | `25b1d657d893`  |
| 3283   | Layout 3             | `25b1d657d893`  |
| 3275   | Layout 3             | `25b1d657d893`  |
| 3267   | Layout 3             | `25b1d657d893`  |
| 3258   | Layout 3             | `25b1d657d893`  |
| 3251   | Layout 3             | `25b1d657d893`  |
| 3242   | Layout 3             | `25b1d657d893`  |
| 3235   | Layout 3             | `25b1d657d893`  |
| 3229   | Layout 3             | `25b1d657d893`  |
| 3212   | Layout 3             | `25b1d657d893`  |
| 3203   | Layout 3             | `25b1d657d893`  |
| 3193   | Layout 3             | `25b1d657d893`  |
| 3186   | Layout 3             | `25b1d657d893`  |
| 3177   | Layout 3             | `25b1d657d893`  |
| 3169   | Layout 3             | `25b1d657d893`  |
| 3158   | Layout 3             | `25b1d657d893`  |
| 3151   | Layout 3             | `25b1d657d893`  |
| 3144   | Layout 3             | `25b1d657d893`  |
| 3133   | Layout 3             | `25b1d657d893`  |
| 3125   | Layout 3             | `25b1d657d893`  |
| 3118   | Layout 3             | `25b1d657d893`  |
| 3111   | Layout 3             | `25b1d657d893`  |
| 3103   | Layout 3             | `25b1d657d893`  |
| 3095   | Layout 3             | `25b1d657d893`  |
| 3086   | Layout 3             | `25b1d657d893`  |
| 3072   | Layout 3             | `25b1d657d893`  |
| 3062   | Layout 3             | `25b1d657d893`  |
| 3052   | Layout 3             | `25b1d657d893`  |
| 3045   | Layout 3             | `25b1d657d893`  |
| 3037   | Layout 3             | `25b1d657d893`  |
| 3030   | Layout 3             | `25b1d657d893`  |
| 3021   | Layout 3             | `25b1d657d893`  |
| 3012   | Layout 3             | `25b1d657d893`  |
| 3002   | Layout 3             | `25b1d657d893`  |
| 2995   | Layout 3             | `25b1d657d893`  |
| 2987   | Layout 3             | `25b1d657d893`  |
| 2978   | Layout 3             | `25b1d657d893`  |
| 2970   | Layout 3             | `25b1d657d893`  |
| 2959   | Layout 3             | `25b1d657d893`  |
| 2951   | Layout 3             | `25b1d657d893`  |
| 2942   | Layout 3             | `25b1d657d893`  |
| 2935   | Layout 3             | `25b1d657d893`  |
| 2932   | Layout 3             | `25b1d657d893`  |
| 2923   | Layout 3             | `25b1d657d893`  |
| 2919   | Layout 3             | `25b1d657d893`  |
| 2907   | Layout 3             | `25b1d657d893`  |
| 2900   | Layout 3             | `25b1d657d893`  |
| 2891   | Layout 3             | `25b1d657d893`  |
| 2882   | Layout 3             | `25b1d657d893`  |
| 2872   | Layout 3             | `25b1d657d893`  |
| 2863   | Layout 3             | `25b1d657d893`  |
| 2855   | Layout 3             | `25b1d657d893`  |
| 2849   | Layout 3             | `25b1d657d893`  |
| 2844   | Layout 3             | `25b1d657d893`  |
| 2834   | Layout 3             | `25b1d657d893`  |
| 2825   | Layout 3             | `25b1d657d893`  |
| 2819   | Layout 3             | `25b1d657d893`  |
| 2811   | Layout 3             | `25b1d657d893`  |
| 2803   | Layout 3             | `25b1d657d893`  |
| 2794   | Layout 3             | `25b1d657d893`  |
| 2783   | Layout 3             | `25b1d657d893`  |
| 2774   | Layout 3             | `25b1d657d893`  |
| 2765   | Layout 3             | `25b1d657d893`  |
| 2756   | Layout 3             | `25b1d657d893`  |
| 2750   | Layout 3             | `25b1d657d893`  |
| 2743   | Layout 3             | `25b1d657d893`  |
| 2736   | Layout 3             | `25b1d657d893`  |
| 2726   | Layout 3             | `25b1d657d893`  |
| 2717   | Layout 3             | `25b1d657d893`  |
| 2709   | Layout 3             | `25b1d657d893`  |
| 2703   | Layout 3             | `25b1d657d893`  |
| 2695   | Layout 3             | `25b1d657d893`  |
| 2684   | Layout 3             | `25b1d657d893`  |
| 2672   | Layout 3             | `25b1d657d893`  |
| 2665   | Layout 3             | `25b1d657d893`  |
| 2657   | Layout 3             | `25b1d657d893`  |
| 2649   | Layout 3             | `25b1d657d893`  |
| 2644   | Layout 3             | `25b1d657d893`  |
| 2637   | No documented layout | `25b1d657d893`  |
| 2629   | No documented layout | `25b1d657d893`  |
| 2619   | No documented layout | `25b1d657d893`  |
| 2612   | No documented layout | `25b1d657d893`  |
| 2606   | No documented layout | `25b1d657d893`  |
| 2602   | No documented layout | `25b1d657d893`  |
| 2601   | Layout 2             | `25b1d657d893`  |
| 2592   | Layout 2             | `25b1d657d893`  |
| 2583   | Layout 2             | `25b1d657d893`  |
| 2575   | Layout 2             | `25b1d657d893`  |
| 2567   | Layout 2             | `25b1d657d893`  |
| 2560   | Layout 2             | `25b1d657d893`  |
| 2553   | Layout 2             | `25b1d657d893`  |
| 2545   | Layout 2             | `25b1d657d893`  |
| 2538   | Layout 2             | `25b1d657d893`  |
| 2529   | Layout 2             | `25b1d657d893`  |
| 2519   | Layout 2             | `25b1d657d893`  |
| 2513   | Layout 2             | `25b1d657d893`  |
| 2510   | Layout 2             | `25b1d657d893`  |
| 2507   | Layout 2             | `25b1d657d893`  |
| 2503   | Layout 2             | `25b1d657d893`  |
| 2498   | Layout 2             | `25b1d657d893`  |
| 2492   | Layout 2             | `25b1d657d893`  |
| 2487   | Layout 2             | `25b1d657d893`  |
| 2480   | Layout 2             | `25b1d657d893`  |
| 2474   | Layout 2             | `25b1d657d893`  |
| 2468   | Layout 2             | `25b1d657d893`  |
| 2460   | Layout 2             | `25b1d657d893`  |
| 2453   | Layout 2             | `25b1d657d893`  |
| 2444   | Layout 2             | `25b1d657d893`  |
| 2438   | Layout 2             | `25b1d657d893`  |
| 2434   | Layout 2             | `25b1d657d893`  |
| 2429   | Layout 2             | `25b1d657d893`  |
| 2421   | Layout 2             | `25b1d657d893`  |
| 2414   | Layout 2             | `25b1d657d893`  |
| 2407   | Layout 2             | `25b1d657d893`  |
| 2401   | Layout 2             | `25b1d657d893`  |
| 2397   | Layout 2             | `25b1d657d893`  |
| 2393   | Layout 2             | `25b1d657d893`  |
| 2384   | Layout 2             | `25b1d657d893`  |
| 2378   | Layout 2             | `25b1d657d893`  |
| 2372   | Layout 2             | `25b1d657d893`  |
| 2358   | Layout 2             | `25b1d657d893`  |
| 2352   | Layout 2             | `25b1d657d893`  |
| 2347   | Layout 2             | `25b1d657d893`  |
| 2343   | Layout 2             | `25b1d657d893`  |
| 2335   | Layout 2             | `25b1d657d893`  |
| 2327   | Layout 2             | `25b1d657d893`  |
| 2324   | Layout 2             | `25b1d657d893`  |
| 2319   | Layout 2             | `25b1d657d893`  |
| 2313   | Layout 2             | `25b1d657d893`  |
| 2308   | Layout 2             | `25b1d657d893`  |
| 2302   | Layout 2             | `25b1d657d893`  |
| 2295   | Layout 2             | `25b1d657d893`  |
| 2290   | Layout 2             | `25b1d657d893`  |
| 2284   | Layout 2             | `25b1d657d893`  |
| 2276   | Layout 2             | `25b1d657d893`  |
| 2269   | Layout 2             | `25b1d657d893`  |
| 2259   | Layout 2             | `25b1d657d893`  |
| 2250   | Layout 2             | `25b1d657d893`  |
| 2243   | Layout 2             | `25b1d657d893`  |
| 2235   | Layout 2             | `25b1d657d893`  |
| 2229   | Layout 2             | `25b1d657d893`  |
| 2224   | Layout 2             | `25b1d657d893`  |
| 2218   | Layout 2             | `25b1d657d893`  |
| 2215   | Layout 2             | `25b1d657d893`  |
| 2207   | Layout 2             | `25b1d657d893`  |
| 2203   | Layout 2             | `25b1d657d893`  |
| 2196   | Layout 2             | `25b1d657d893`  |
| 2192   | Layout 2             | `25b1d657d893`  |
| 2189   | Layout 2             | `25b1d657d893`  |
| 2183   | No documented layout | `25b1d657d893`  |
| 2179   | No documented layout | `25b1d657d893`  |
| 2171   | No documented layout | `25b1d657d893`  |
| 2163   | Layout 1             | `25b1d657d893`  |
| 2156   | Layout 1             | `25b1d657d893`  |
| 2151   | Layout 1             | `25b1d657d893`  |
| 2147   | Layout 1             | `25b1d657d893`  |
| 2142   | Layout 1             | `25b1d657d893`  |
| 2138   | Layout 1             | `25b1d657d893`  |
| 2134   | Layout 1             | `25b1d657d893`  |
| 2130   | Layout 1             | `25b1d657d893`  |
| 2122   | Layout 1             | `25b1d657d893`  |
| 2107   | Layout 1             | `25b1d657d893`  |
| 2098   | Layout 1             | `25b1d657d893`  |
| 2089   | Layout 1             | `25b1d657d893`  |
| 2081   | Layout 1             | `25b1d657d893`  |
| 2073   | Layout 1             | `25b1d657d893`  |
| 2067   | Layout 1             | `25b1d657d893`  |
| 2063   | Layout 1             | `25b1d657d893`  |
| 2059   | Layout 1             | `25b1d657d893`  |
| 2052   | Layout 1             | `25b1d657d893`  |
| 2044   | Layout 1             | `25b1d657d893`  |
| 2039   | Layout 1             | `25b1d657d893`  |
| 2032   | Layout 1             | `25b1d657d893`  |
| 2025   | Layout 1             | `25b1d657d893`  |
| 2011   | Layout 1             | `25b1d657d893`  |
| 2005   | Layout 1             | `25b1d657d893`  |
| 2000   | Layout 1             | `25b1d657d893`  |
| 1996   | Layout 1             | `25b1d657d893`  |
| 1991   | Layout 1             | `25b1d657d893`  |
| 1985   | Layout 1             | `25b1d657d893`  |
| 1980   | Layout 1             | `25b1d657d893`  |
| 1969   | Layout 1             | `25b1d657d893`  |
| 1964   | Layout 1             | `25b1d657d893`  |
| 1958   | Layout 1             | `25b1d657d893`  |
| 1950   | Layout 1             | `25b1d657d893`  |
| 1945   | Layout 1             | `25b1d657d893`  |
| 1937   | Layout 1             | `25b1d657d893`  |
| 1933   | Layout 1             | `25b1d657d893`  |
| 1927   | Layout 1             | `25b1d657d893`  |
| 1921   | Layout 1             | `25b1d657d893`  |
| 1914   | Layout 1             | `25b1d657d893`  |
| 1908   | Layout 1             | `25b1d657d893`  |
| 1897   | Layout 1             | `25b1d657d893`  |
| 1892   | Layout 1             | `25b1d657d893`  |
| 1886   | Layout 1             | `25b1d657d893`  |
| 1881   | Layout 1             | `25b1d657d893`  |
| 1871   | Layout 1             | `25b1d657d893`  |
| 1866   | Layout 1             | `25b1d657d893`  |
| 1862   | Layout 1             | `25b1d657d893`  |
| 1854   | Layout 1             | `25b1d657d893`  |
| 1846   | Layout 1             | `25b1d657d893`  |
| 1838   | Layout 1             | `25b1d657d893`  |
| 1832   | Layout 1             | `25b1d657d893`  |
| 1826   | Layout 1             | `25b1d657d893`  |
| 1822   | Layout 1             | `25b1d657d893`  |
| 1818   | Layout 1             | `25b1d657d893`  |
| 1804   | Layout 1             | `25b1d657d893`  |
| 1794   | Layout 1             | `25b1d657d893`  |
| 1790   | Layout 1             | `25b1d657d893`  |
| 1784   | Layout 1             | `25b1d657d893`  |
| 1774   | Layout 1             | `25b1d657d893`  |
| 1771   | Layout 1             | `25b1d657d893`  |
| 1762   | Layout 1             | `25b1d657d893`  |
| 1759   | Layout 1             | `25b1d657d893`  |
| 1754   | Layout 1             | `25b1d657d893`  |
| 1749   | Layout 1             | `25b1d657d893`  |
| 1743   | Layout 1             | `25b1d657d893`  |
| 1737   | Layout 1             | `25b1d657d893`  |
| 1731   | Layout 3             | `25b1d657d893`  |
| 1725   | Layout 3             | `25b1d657d893`  |
| 1717   | Layout 3             | `25b1d657d893`  |
| 1710   | Layout 3             | `25b1d657d893`  |
| 1704   | Layout 3             | `25b1d657d893`  |
| 1698   | Layout 3             | `25b1d657d893`  |
| 1690   | Layout 3             | `25b1d657d893`  |
| 1685   | Layout 3             | `25b1d657d893`  |
| 1680   | Layout 3             | `25b1d657d893`  |
| 1674   | Layout 3             | `25b1d657d893`  |
| 1668   | Layout 3             | `25b1d657d893`  |
| 1659   | Layout 3             | `25b1d657d893`  |
| 1649   | Layout 3             | `25b1d657d893`  |
| 1642   | Layout 3             | `25b1d657d893`  |
| 1636   | Layout 3             | `25b1d657d893`  |
| 1628   | Layout 3             | `25b1d657d893`  |
| 1622   | Layout 3             | `25b1d657d893`  |
| 1614   | Layout 3             | `25b1d657d893`  |
| 1608   | Layout 3             | `25b1d657d893`  |
| 1602   | Layout 3             | `25b1d657d893`  |
| 1598   | No file              | `25b1d657d893`  |
| 1594   | No file              | `25b1d657d893`  |
| 1590   | No file              | `25b1d657d893`  |
| 1587   | No file              | `25b1d657d893`  |
| 1584   | No file              | `25b1d657d893`  |
| 1579   | No file              | `25b1d657d893`  |
| 1572   | No file              | `25b1d657d893`  |
| 1565   | No file              | `25b1d657d893`  |
| 1559   | No file              | `25b1d657d893`  |
| 1554   | No file              | `25b1d657d893`  |
| 1547   | No file              | `25b1d657d893`  |
| 1537   | No file              | `25b1d657d893`  |
| 1529   | No file              | `25b1d657d893`  |
| 1524   | No file              | `25b1d657d893`  |
| 1519   | No file              | `25b1d657d893`  |
| 1509   | No file              | `25b1d657d893`  |
| 1506   | No file              | `25b1d657d893`  |
| 1504   | No file              | `25b1d657d893`  |
| 1500   | No file              | `25b1d657d893`  |
| 1493   | No file              | `25b1d657d893`  |
| 1489   | No file              | `25b1d657d893`  |
| 1485   | No file              | `25b1d657d893`  |
| 1481   | No file              | `25b1d657d893`  |
| 1474   | No file              | `25b1d657d893`  |
| 1466   | No file              | `25b1d657d893`  |
| 1462   | No file              | `25b1d657d893`  |
| 1459   | No file              | `25b1d657d893`  |
| 1453   | No file              | `25b1d657d893`  |
| 1450   | No file              | `25b1d657d893`  |
| 1445   | No file              | `25b1d657d893`  |
| 1439   | No file              | `25b1d657d893`  |
| 1433   | No file              | `25b1d657d893`  |
| 1430   | No file              | `25b1d657d893`  |
| 1426   | No file              | `25b1d657d893`  |
| 1421   | No file              | `25b1d657d893`  |
| 1417   | No file              | `25b1d657d893`  |
| 1416   | No file              | `25b1d657d893`  |
| 1409   | No file              | `25b1d657d893`  |
| 1405   | No file              | `25b1d657d893`  |
| 1401   | No file              | `25b1d657d893`  |
| 1396   | No file              | `25b1d657d893`  |
| 1391   | No file              | `25b1d657d893`  |
| 1390   | No file              | `25b1d657d893`  |
| 1386   | No file              | `25b1d657d893`  |
| 1381   | No file              | `25b1d657d893`  |
| 1379   | No file              | `25b1d657d893`  |
| 1372   | No file              | `25b1d657d893`  |
| 1366   | No file              | `25b1d657d893`  |
| 1364   | No file              | `25b1d657d893`  |
| 1363   | No file              | `25b1d657d893`  |
| 1360   | No file              | `25b1d657d893`  |
| 1358   | No file              | `25b1d657d893`  |
| 1355   | No file              | `25b1d657d893`  |
| 1351   | No file              | `25b1d657d893`  |
| 1348   | No file              | `25b1d657d893`  |
| 1346   | No file              | `25b1d657d893`  |
| 1341   | No file              | `25b1d657d893`  |
| 1340   | No file              | `25b1d657d893`  |
| 1338   | No file              | `25b1d657d893`  |
| 1335   | No file              | `25b1d657d893`  |
| 1333   | No file              | `25b1d657d893`  |
| 1329   | No file              | `25b1d657d893`  |
| 1327   | No file              | `25b1d657d893`  |
| 1324   | No file              | `25b1d657d893`  |
| 1321   | No file              | `25b1d657d893`  |
| 1319   | No file              | `25b1d657d893`  |
| 1318   | No file              | `25b1d657d893`  |
| 1316   | No file              | `25b1d657d893`  |
| 1313   | No file              | `25b1d657d893`  |
| 1311   | No file              | `25b1d657d893`  |
| 1309   | No file              | `25b1d657d893`  |
| 1304   | No file              | `25b1d657d893`  |
| 1292   | No file              | `25b1d657d893`  |
| 1286   | No file              | `25b1d657d893`  |
| 1280   | No file              | `25b1d657d893`  |
| 1276   | No file              | `25b1d657d893`  |
| 1267   | No file              | `25b1d657d893`  |
| 1261   | No file              | `25b1d657d893`  |
| 1256   | No file              | `25b1d657d893`  |
| 1250   | No file              | `25b1d657d893`  |
| 1246   | No file              | `25b1d657d893`  |
| 1239   | No file              | `25b1d657d893`  |
| 1230   | No file              | `25b1d657d893`  |
| 1226   | No file              | `25b1d657d893`  |
| 1220   | No file              | `25b1d657d893`  |
| 1217   | No file              | `25b1d657d893`  |
| 1211   | No file              | `25b1d657d893`  |
| 1210   | No file              | `25b1d657d893`  |
| 1208   | No file              | `25b1d657d893`  |
| 1203   | No file              | `25b1d657d893`  |
| 1197   | No file              | `25b1d657d893`  |
| 1194   | No file              | `25b1d657d893`  |
| 1192   | No file              | `25b1d657d893`  |
| 1187   | No file              | `25b1d657d893`  |
| 1183   | No file              | `25b1d657d893`  |
| 1177   | No file              | `25b1d657d893`  |
| 1173   | No file              | `25b1d657d893`  |
| 1167   | No file              | `25b1d657d893`  |
| 1164   | No file              | `25b1d657d893`  |
| 1156   | No file              | `25b1d657d893`  |
| 1149   | No file              | `25b1d657d893`  |
| 1144   | No file              | `25b1d657d893`  |
| 1137   | No file              | `25b1d657d893`  |
| 1132   | No file              | `25b1d657d893`  |
| 1127   | No file              | `25b1d657d893`  |
| 1122   | No file              | `25b1d657d893`  |
| 1118   | No file              | `25b1d657d893`  |
| 1114   | No file              | `25b1d657d893`  |
| 1109   | No file              | `25b1d657d893`  |
| 1102   | No file              | `25b1d657d893`  |
| 1096   | No file              | `25b1d657d893`  |
| 1088   | No file              | `25b1d657d893`  |
| 1081   | No file              | `25b1d657d893`  |
| 1076   | No file              | `25b1d657d893`  |
| 1069   | No file              | `25b1d657d893`  |
| 1064   | No file              | `25b1d657d893`  |
| 1058   | No file              | `25b1d657d893`  |
| 1051   | No file              | `25b1d657d893`  |
| 1044   | No file              | `25b1d657d893`  |
| 1036   | No file              | `25b1d657d893`  |
| 1026   | No file              | `25b1d657d893`  |
| 1016   | No file              | `25b1d657d893`  |
| 1009   | No file              | `25b1d657d893`  |
| 1005   | No file              | `25b1d657d893`  |
| 1000   | No file              | `25b1d657d893`  |
| 998    | No file              | `25b1d657d893`  |
| 990    | No file              | `25b1d657d893`  |
| 979    | No file              | `25b1d657d893`  |
| 972    | No file              | `25b1d657d893`  |
| 963    | No file              | `25b1d657d893`  |
| 955    | No file              | `25b1d657d893`  |
| 946    | No file              | `25b1d657d893`  |
| 938    | No file              | `25b1d657d893`  |
| 927    | No file              | `25b1d657d893`  |
| 911    | No file              | `25b1d657d893`  |
| 904    | No file              | `25b1d657d893`  |
| 899    | No file              | `25b1d657d893`  |
| 894    | No file              | `25b1d657d893`  |
| 885    | No file              | `25b1d657d893`  |
| 879    | No file              | `25b1d657d893`  |
| 872    | No file              | `25b1d657d893`  |
| 864    | No file              | `25b1d657d893`  |
| 855    | No file              | `25b1d657d893`  |
| 853    | No file              | `25b1d657d893`  |
| 845    | No file              | `25b1d657d893`  |
| 837    | No file              | `25b1d657d893`  |
| 829    | No file              | `25b1d657d893`  |
| 822    | No file              | `25b1d657d893`  |
| 814    | No file              | `25b1d657d893`  |
| 805    | No file              | `25b1d657d893`  |
| 794    | No file              | `25b1d657d893`  |
| 787    | No file              | `25b1d657d893`  |
| 780    | No file              | `25b1d657d893`  |
| 771    | No file              | `25b1d657d893`  |
| 760    | No file              | `25b1d657d893`  |
| 748    | No file              | `25b1d657d893`  |
| 741    | No file              | `25b1d657d893`  |
| 736    | No file              | `25b1d657d893`  |
| 731    | No file              | `25b1d657d893`  |
| 723    | No file              | `25b1d657d893`  |
| 711    | No file              | `25b1d657d893`  |
| 707    | No file              | `25b1d657d893`  |
| 697    | No file              | `25b1d657d893`  |
| 689    | No file              | `25b1d657d893`  |
| 683    | No file              | `25b1d657d893`  |
| 678    | No file              | `25b1d657d893`  |
| 670    | No file              | `25b1d657d893`  |
| 661    | No file              | `25b1d657d893`  |
| 656    | No file              | `25b1d657d893`  |
| 652    | No file              | `25b1d657d893`  |
| 643    | No file              | `25b1d657d893`  |
| 637    | No file              | `25b1d657d893`  |
| 630    | No file              | `25b1d657d893`  |
| 627    | No file              | `25b1d657d893`  |
| 621    | No file              | `25b1d657d893`  |
| 617    | No file              | `25b1d657d893`  |
| 615    | No file              | `25b1d657d893`  |
| 606    | No file              | `25b1d657d893`  |
| 599    | No file              | `25b1d657d893`  |
| 592    | No file              | `25b1d657d893`  |
| 586    | No file              | `25b1d657d893`  |
| 577    | No file              | `25b1d657d893`  |
| 569    | No file              | `25b1d657d893`  |
| 561    | No file              | `25b1d657d893`  |
| 554    | No file              | `25b1d657d893`  |
| 542    | No file              | `25b1d657d893`  |
| 532    | No file              | `25b1d657d893`  |
| 531    | No file              | `25b1d657d893`  |
| 526    | No file              | `25b1d657d893`  |
| 521    | No file              | `25b1d657d893`  |
| 517    | No file              | `25b1d657d893`  |
| 510    | No file              | `25b1d657d893`  |
| 508    | No file              | `25b1d657d893`  |
| 504    | No file              | `25b1d657d893`  |
| 497    | No file              | `25b1d657d893`  |
| 491    | No file              | `25b1d657d893`  |
| 485    | No file              | `25b1d657d893`  |
| 478    | No file              | `25b1d657d893`  |
| 472    | No file              | `25b1d657d893`  |
| 466    | No file              | `25b1d657d893`  |
| 457    | No file              | `25b1d657d893`  |
| 452    | No file              | `25b1d657d893`  |
| 449    | No file              | `25b1d657d893`  |
| 435    | No file              | `25b1d657d893`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                   |
| ---------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `mansionpartinfo.bss`        | Optional | The installation mode parts of each manor building; see [`mansionpartinfo.bss`](mansionpartinfo_bss.md) |
| `languagedata_en.loc`        | Optional | Manor names (type 6), region names (type 17), quest titles (type 18)                   |

All multi-byte values are little-endian.

## Layout 3

### File Layout

The PABR frame of `buffsimply.bss` with fixed rows and an empty string
table.

| Offset              | Type          | Field        | Notes                                          |
| ------------------- | ------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]       | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32           | count        | Number of rows; 4 on client 3474               |
| `+0x08`             | Row[count]    | rows         | See Row                                        |
| `rows+0x00`         | String Table  | string_table | See String Table                               |
| `string_table+0x00` | u32           | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32           | zero         | Always 0                                       |

### Row (93 bytes)

| Offset  | Type   | Field                    | Notes                                                                                     |
| ------- | ------ | ------------------------ | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16    | land_character_key       | Row key: the manor land, a [`houseinfo.bss`](houseinfo_bss.md) house and `characterstatic.dbss` character |
| `+0x02` | u16    | building_character_key   | The manor building, a `houseinfo.bss` house; the manor key of `mansionpartinfo.bss`       |
| `+0x04` | u16    | need_point               | Contribution points to rent the manor; `5` on every row (client 3474)                     |
| `+0x06` | u16    | region_key               | `regioninfo.bss` region of the manor; its LOC type 17 name is the manor's name            |
| `+0x08` | i32[3] | sector_start             | Lowest sector (x, y, z) of the manor area, 12,800 units a sector                          |
| `+0x14` | i32[3] | sector_end               | Highest sector (x, y, z), inclusive                                                       |
| `+0x20` | i32[3] | unknown_20               | `sector_start` times 3 on every row; see Open Questions                                   |
| `+0x2C` | i32[3] | unknown_2c               | `sector_end` times 3 on every row                                                         |
| `+0x38` | u16    | condition_quest_chain_id | Quest that unlocks the rental: chain (LOC type 18 `str_id1`)                              |
| `+0x3A` | u16    | condition_quest_id       | Quest number in the chain (LOC type 18 `str_id2`)                                         |
| `+0x3C` | u32    | day_pay                  | Silver per day of rent; `1,000,000` or `100,000` (client 3474)                            |
| `+0x40` | f32    | unknown_40               | `0` on every row (clients 1784 and 3474)                                                  |
| `+0x44` | f32    | unknown_44               | `1000`, `0`, `500`, `0` in row order (client 3474)                                        |
| `+0x48` | f32    | unknown_48               | `0`, `0`, `0`, `600`                                                                      |
| `+0x4C` | f32    | unknown_4c               | `500`, `0`, `500`, `500`                                                                  |
| `+0x50` | u8     | unknown_50               | `1`, `2`, `0`, `3`                                                                        |
| `+0x51` | f32[3] | unknown_51               | A world position (x, y, z) inside the row's sector box on every row                       |

Rows on client 3474 in file order: Shimhyangje (land 3841), Solbaram Neowa
House (3843), Blue Maned Lion's Manor (3814), Hyeollokdang (3847).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3474          |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none in the file |

## Layout 2

Client 2519 rows have no `unknown_48` and no `unknown_51`: 77 bytes. The
file holds Shimhyangje, Solbaram Neowa House and Blue Maned Lion's Manor.
Only the Row differs from Layout 3.

### Row (77 bytes)

| Offset  | Type   | Field                    | Notes                                    |
| ------- | ------ | ------------------------ | ---------------------------------------- |
| `+0x00` | u16    | land_character_key       |                                          |
| `+0x02` | u16    | building_character_key   |                                          |
| `+0x04` | u16    | need_point               |                                          |
| `+0x06` | u16    | region_key               |                                          |
| `+0x08` | i32[3] | sector_start             |                                          |
| `+0x14` | i32[3] | sector_end               |                                          |
| `+0x20` | i32[3] | unknown_20               |                                          |
| `+0x2C` | i32[3] | unknown_2c               |                                          |
| `+0x38` | u16    | condition_quest_chain_id |                                          |
| `+0x3A` | u16    | condition_quest_id       |                                          |
| `+0x3C` | u32    | day_pay                  |                                          |
| `+0x40` | f32    | unknown_40               |                                          |
| `+0x44` | f32    | unknown_44               | Same values as client 3474 for the 3 rows |
| `+0x48` | f32    | unknown_4c               | Same values as client 3474 for the 3 rows |
| `+0x4C` | u8     | unknown_50               | Same values as client 3474 for the 3 rows |

## Layout 1

Rows of clients 1784 and 2107 end after `unknown_40`: 68 bytes, with no
`unknown_44`, `unknown_4c` and `unknown_50`. The file holds Blue Maned
Lion's Manor alone. Only the Row differs from Layout 2.

### Row (68 bytes)

| Offset  | Type   | Field                    | Notes                  |
| ------- | ------ | ------------------------ | ---------------------- |
| `+0x00` | u16    | land_character_key       |                        |
| `+0x02` | u16    | building_character_key   |                        |
| `+0x04` | u16    | need_point               |                        |
| `+0x06` | u16    | region_key               |                        |
| `+0x08` | i32[3] | sector_start             |                        |
| `+0x14` | i32[3] | sector_end               |                        |
| `+0x20` | i32[3] | unknown_20               |                        |
| `+0x2C` | i32[3] | unknown_2c               |                        |
| `+0x38` | u16    | condition_quest_chain_id |                        |
| `+0x3A` | u16    | condition_quest_id       |                        |
| `+0x3C` | u32    | day_pay                  |                        |
| `+0x40` | f32    | unknown_40               | `0` on client 1784     |

## Field Names

The `MansionLand_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has one row with the columns `LandCharacterKey` (3814),
`BuildingCharacterKey` (3815), `NeedPoint` (5), `Region` (1095),
`SectorStartPosion` (`6, -1, -4`), `SectorEndPosition` (`8, 0, -2`),
`Condition` (`2063,8;`) and `DayPay` (1000000). The one row of client 1784
and the Blue Maned Lion's Manor row of client 3474 hold these values in
this order, 1 of 1 keys on both clients. The sheet has no column for
`unknown_20` to `unknown_51`.

- `land_character_key`: the four keys are the `_eMansionKey` values of the
  manor contract window (`_hidelOut` 3814, `_simHayngOut` 3841,
  `_neoWhaOut` 3843, `_hyunRokOut` 3847). The window passes the visited
  house's character key to `ToClient_getNeenPointMansion()` and stops on
  `-1`, "house info not found".
- `condition_quest_chain_id`, `condition_quest_id`: the sheet's `Condition`
  pair. Each row's pair is a quest (client 3474): 2063/8 "[Manor] A
  Father's Heart" on Blue Maned Lion's Manor, 8516/1 "[LoML] Ruler of
  Taebaek", 8510/9 "[LoML] Dokkebi's Gift" and 8541/3 "[Traveler] Dawn That
  Banishes Darkness" on the other three.
- `region_key`: 1095, 1214, 1228 and 1431 are named Blue Maned Lion's
  Manor, Shimhyangje, Solbaram Neowa House and Hyeollokdang in LOC type 17.
- `sector_start` and `sector_end`: `unknown_51` of each row lies inside the
  box when divided by 12,800 (Blue Maned Lion's Manor: `97168, -2120,
  -30883`, sector `7, -1, -3`).

## Notes

- Each `building_character_key` is a manor of
  [`mansionpartinfo.bss`](mansionpartinfo_bss.md) (3815, 3842, 3844,
  3848), and both keys of every row are house rows of `houseinfo.bss`.
- The land and the building share one LOC type 6 name per manor.
- The contract window reads the daily price from
  `ToClient_GetMansionPricePerDay()`, which takes no manor key; whether it
  returns `day_pay` of the visited manor is not shown by the Lua.

## Open Questions

### What is the second sector box?

`unknown_20` and `unknown_2c` hold `sector_start` and `sector_end` times 3
on all four rows (client 3474) and on the row of client 1784: a box in
units of a third of a sector (4,266.67). Nothing in the client Lua reads
it, and the sheet has no column for it.

### What do `unknown_40` to `unknown_51` hold?

Client 3474 adds four f32 values, a u8 and three f32 values to each row.
The last three are a world position inside the manor's sector box; the u8
is `0` on Blue Maned Lion's Manor and `1` to `3` on the three Land of the
Morning Light manors in the order of their land keys. The four f32 values
are `0`, `500`, `600` or `1000`. No client Lua getter names them.
