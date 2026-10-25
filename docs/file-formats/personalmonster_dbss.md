# `personalmonster.dbss` Format

## Purpose

The Dark Rift bosses (`어둠의 틈`, `panel_window_personalmonster_all`):
per boss character a Korean description, a difficulty, a world map image
and the items it drops. On client 3474 the file has 6 rows, Red Nose,
Dastard Bheg, Ahib Griffon, Muskan, Dim Tree Spirit and Ferrid, all with
the same 13 drop items. The spawn points are in
[`personalmonsterposition.dbss`](personalmonsterposition_dbss.md) and the
world map icon settings in
[`personalmonsteretc.bss`](personalmonsteretc_bss.md). Companion
`personalmonsteroffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records      | Row bytes                  |
| ------ | -------------- | ---------------------------- | ----- | ------------ | -------------------------- |
| 1      | 1280 and later | `personalmonster.dbss`       | 1,120 | 6 Row        | 179 to 197, 186 on average |
| 1      | 1280 and later | `personalmonsteroffset.dbss` | 64    | 6 Offset Row | 10                         |

| Layout | File                         | Known           | Unknown     |
| ------ | ---------------------------- | --------------- | ----------- |
| 1      | `personalmonster.dbss`       | 1,096 B (97.9%) | 24 B (2.1%) |
| 1      | `personalmonsteroffset.dbss` | 64 B (100.0%)   | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `45866aeee5ee`  |
| 3482   | Layout 1 | `45866aeee5ee`  |
| 3474   | Layout 1 | `45866aeee5ee`  |
| 3473   | Layout 1 | `45866aeee5ee`  |
| 3464   | Layout 1 | `45866aeee5ee`  |
| 3458   | Layout 1 | `45866aeee5ee`  |
| 3454   | Layout 1 | `45866aeee5ee`  |
| 3444   | Layout 1 | `45866aeee5ee`  |
| 3435   | Layout 1 | `45866aeee5ee`  |
| 3426   | Layout 1 | `45866aeee5ee`  |
| 3418   | Layout 1 | `45866aeee5ee`  |
| 3412   | Layout 1 | `45866aeee5ee`  |
| 3402   | Layout 1 | `45866aeee5ee`  |
| 3396   | Layout 1 | `45866aeee5ee`  |
| 3387   | Layout 1 | `45866aeee5ee`  |
| 3381   | Layout 1 | `45866aeee5ee`  |
| 3373   | Layout 1 | `45866aeee5ee`  |
| 3364   | Layout 1 | `45866aeee5ee`  |
| 3356   | Layout 1 | `45866aeee5ee`  |
| 3349   | Layout 1 | `45866aeee5ee`  |
| 3342   | Layout 1 | `45866aeee5ee`  |
| 3335   | Layout 1 | `45866aeee5ee`  |
| 3326   | Layout 1 | `45866aeee5ee`  |
| 3321   | Layout 1 | `45866aeee5ee`  |
| 3314   | Layout 1 | `45866aeee5ee`  |
| 3303   | Layout 1 | `45866aeee5ee`  |
| 3302   | Layout 1 | `45866aeee5ee`  |
| 3293   | Layout 1 | `45866aeee5ee`  |
| 3283   | Layout 1 | `45866aeee5ee`  |
| 3275   | Layout 1 | `45866aeee5ee`  |
| 3267   | Layout 1 | `45866aeee5ee`  |
| 3258   | Layout 1 | `45866aeee5ee`  |
| 3251   | Layout 1 | `45866aeee5ee`  |
| 3242   | Layout 1 | `45866aeee5ee`  |
| 3235   | Layout 1 | `45866aeee5ee`  |
| 3229   | Layout 1 | `45866aeee5ee`  |
| 3212   | Layout 1 | `45866aeee5ee`  |
| 3203   | Layout 1 | `45866aeee5ee`  |
| 3193   | Layout 1 | `45866aeee5ee`  |
| 3186   | Layout 1 | `45866aeee5ee`  |
| 3177   | Layout 1 | `45866aeee5ee`  |
| 3169   | Layout 1 | `45866aeee5ee`  |
| 3158   | Layout 1 | `45866aeee5ee`  |
| 3151   | Layout 1 | `45866aeee5ee`  |
| 3144   | Layout 1 | `45866aeee5ee`  |
| 3133   | Layout 1 | `45866aeee5ee`  |
| 3125   | Layout 1 | `45866aeee5ee`  |
| 3118   | Layout 1 | `45866aeee5ee`  |
| 3111   | Layout 1 | `45866aeee5ee`  |
| 3103   | Layout 1 | `45866aeee5ee`  |
| 3095   | Layout 1 | `45866aeee5ee`  |
| 3086   | Layout 1 | `45866aeee5ee`  |
| 3072   | Layout 1 | `45866aeee5ee`  |
| 3062   | Layout 1 | `45866aeee5ee`  |
| 3052   | Layout 1 | `45866aeee5ee`  |
| 3045   | Layout 1 | `45866aeee5ee`  |
| 3037   | Layout 1 | `45866aeee5ee`  |
| 3030   | Layout 1 | `45866aeee5ee`  |
| 3021   | Layout 1 | `45866aeee5ee`  |
| 3012   | Layout 1 | `45866aeee5ee`  |
| 3002   | Layout 1 | `45866aeee5ee`  |
| 2995   | Layout 1 | `45866aeee5ee`  |
| 2987   | Layout 1 | `45866aeee5ee`  |
| 2978   | Layout 1 | `45866aeee5ee`  |
| 2970   | Layout 1 | `45866aeee5ee`  |
| 2959   | Layout 1 | `45866aeee5ee`  |
| 2951   | Layout 1 | `45866aeee5ee`  |
| 2942   | Layout 1 | `45866aeee5ee`  |
| 2935   | Layout 1 | `45866aeee5ee`  |
| 2932   | Layout 1 | `45866aeee5ee`  |
| 2923   | Layout 1 | `45866aeee5ee`  |
| 2919   | Layout 1 | `45866aeee5ee`  |
| 2907   | Layout 1 | `45866aeee5ee`  |
| 2900   | Layout 1 | `45866aeee5ee`  |
| 2891   | Layout 1 | `45866aeee5ee`  |
| 2882   | Layout 1 | `45866aeee5ee`  |
| 2872   | Layout 1 | `45866aeee5ee`  |
| 2863   | Layout 1 | `45866aeee5ee`  |
| 2855   | Layout 1 | `45866aeee5ee`  |
| 2849   | Layout 1 | `45866aeee5ee`  |
| 2844   | Layout 1 | `45866aeee5ee`  |
| 2834   | Layout 1 | `45866aeee5ee`  |
| 2825   | Layout 1 | `45866aeee5ee`  |
| 2819   | Layout 1 | `45866aeee5ee`  |
| 2811   | Layout 1 | `45866aeee5ee`  |
| 2803   | Layout 1 | `45866aeee5ee`  |
| 2794   | Layout 1 | `45866aeee5ee`  |
| 2783   | Layout 1 | `45866aeee5ee`  |
| 2774   | Layout 1 | `45866aeee5ee`  |
| 2765   | Layout 1 | `45866aeee5ee`  |
| 2756   | Layout 1 | `45866aeee5ee`  |
| 2750   | Layout 1 | `45866aeee5ee`  |
| 2743   | Layout 1 | `45866aeee5ee`  |
| 2736   | Layout 1 | `45866aeee5ee`  |
| 2726   | Layout 1 | `45866aeee5ee`  |
| 2717   | Layout 1 | `45866aeee5ee`  |
| 2709   | Layout 1 | `45866aeee5ee`  |
| 2703   | Layout 1 | `45866aeee5ee`  |
| 2695   | Layout 1 | `45866aeee5ee`  |
| 2684   | Layout 1 | `45866aeee5ee`  |
| 2672   | Layout 1 | `45866aeee5ee`  |
| 2665   | Layout 1 | `45866aeee5ee`  |
| 2657   | Layout 1 | `45866aeee5ee`  |
| 2649   | Layout 1 | `45866aeee5ee`  |
| 2644   | Layout 1 | `45866aeee5ee`  |
| 2637   | Layout 1 | `45866aeee5ee`  |
| 2629   | Layout 1 | `45866aeee5ee`  |
| 2619   | Layout 1 | `45866aeee5ee`  |
| 2612   | Layout 1 | `45866aeee5ee`  |
| 2606   | Layout 1 | `45866aeee5ee`  |
| 2602   | Layout 1 | `45866aeee5ee`  |
| 2601   | Layout 1 | `45866aeee5ee`  |
| 2592   | Layout 1 | `45866aeee5ee`  |
| 2583   | Layout 1 | `45866aeee5ee`  |
| 2575   | Layout 1 | `45866aeee5ee`  |
| 2567   | Layout 1 | `45866aeee5ee`  |
| 2560   | Layout 1 | `45866aeee5ee`  |
| 2553   | Layout 1 | `45866aeee5ee`  |
| 2545   | Layout 1 | `45866aeee5ee`  |
| 2538   | Layout 1 | `45866aeee5ee`  |
| 2529   | Layout 1 | `45866aeee5ee`  |
| 2519   | Layout 1 | `45866aeee5ee`  |
| 2513   | Layout 1 | `45866aeee5ee`  |
| 2510   | Layout 1 | `45866aeee5ee`  |
| 2507   | Layout 1 | `45866aeee5ee`  |
| 2503   | Layout 1 | `45866aeee5ee`  |
| 2498   | Layout 1 | `45866aeee5ee`  |
| 2492   | Layout 1 | `45866aeee5ee`  |
| 2487   | Layout 1 | `45866aeee5ee`  |
| 2480   | Layout 1 | `45866aeee5ee`  |
| 2474   | Layout 1 | `45866aeee5ee`  |
| 2468   | Layout 1 | `45866aeee5ee`  |
| 2460   | Layout 1 | `45866aeee5ee`  |
| 2453   | Layout 1 | `45866aeee5ee`  |
| 2444   | Layout 1 | `45866aeee5ee`  |
| 2438   | Layout 1 | `45866aeee5ee`  |
| 2434   | Layout 1 | `45866aeee5ee`  |
| 2429   | Layout 1 | `45866aeee5ee`  |
| 2421   | Layout 1 | `45866aeee5ee`  |
| 2414   | Layout 1 | `45866aeee5ee`  |
| 2407   | Layout 1 | `45866aeee5ee`  |
| 2401   | Layout 1 | `45866aeee5ee`  |
| 2397   | Layout 1 | `45866aeee5ee`  |
| 2393   | Layout 1 | `45866aeee5ee`  |
| 2384   | Layout 1 | `45866aeee5ee`  |
| 2378   | Layout 1 | `45866aeee5ee`  |
| 2372   | Layout 1 | `45866aeee5ee`  |
| 2358   | Layout 1 | `45866aeee5ee`  |
| 2352   | Layout 1 | `45866aeee5ee`  |
| 2347   | Layout 1 | `45866aeee5ee`  |
| 2343   | Layout 1 | `45866aeee5ee`  |
| 2335   | Layout 1 | `45866aeee5ee`  |
| 2327   | Layout 1 | `45866aeee5ee`  |
| 2324   | Layout 1 | `45866aeee5ee`  |
| 2319   | Layout 1 | `45866aeee5ee`  |
| 2313   | Layout 1 | `45866aeee5ee`  |
| 2308   | Layout 1 | `45866aeee5ee`  |
| 2302   | Layout 1 | `45866aeee5ee`  |
| 2295   | Layout 1 | `45866aeee5ee`  |
| 2290   | Layout 1 | `45866aeee5ee`  |
| 2284   | Layout 1 | `45866aeee5ee`  |
| 2276   | Layout 1 | `45866aeee5ee`  |
| 2269   | Layout 1 | `45866aeee5ee`  |
| 2259   | Layout 1 | `45866aeee5ee`  |
| 2250   | Layout 1 | `45866aeee5ee`  |
| 2243   | Layout 1 | `45866aeee5ee`  |
| 2235   | Layout 1 | `45866aeee5ee`  |
| 2229   | Layout 1 | `45866aeee5ee`  |
| 2224   | Layout 1 | `45866aeee5ee`  |
| 2218   | Layout 1 | `45866aeee5ee`  |
| 2215   | Layout 1 | `45866aeee5ee`  |
| 2207   | Layout 1 | `45866aeee5ee`  |
| 2203   | Layout 1 | `45866aeee5ee`  |
| 2196   | Layout 1 | `45866aeee5ee`  |
| 2192   | Layout 1 | `45866aeee5ee`  |
| 2189   | Layout 1 | `45866aeee5ee`  |
| 2183   | Layout 1 | `45866aeee5ee`  |
| 2179   | Layout 1 | `45866aeee5ee`  |
| 2171   | Layout 1 | `45866aeee5ee`  |
| 2163   | Layout 1 | `45866aeee5ee`  |
| 2156   | Layout 1 | `45866aeee5ee`  |
| 2151   | Layout 1 | `45866aeee5ee`  |
| 2147   | Layout 1 | `45866aeee5ee`  |
| 2142   | Layout 1 | `45866aeee5ee`  |
| 2138   | Layout 1 | `45866aeee5ee`  |
| 2134   | Layout 1 | `45866aeee5ee`  |
| 2130   | Layout 1 | `45866aeee5ee`  |
| 2122   | Layout 1 | `45866aeee5ee`  |
| 2107   | Layout 1 | `45866aeee5ee`  |
| 2098   | Layout 1 | `45866aeee5ee`  |
| 2089   | Layout 1 | `45866aeee5ee`  |
| 2081   | Layout 1 | `45866aeee5ee`  |
| 2073   | Layout 1 | `45866aeee5ee`  |
| 2067   | Layout 1 | `45866aeee5ee`  |
| 2063   | Layout 1 | `45866aeee5ee`  |
| 2059   | Layout 1 | `45866aeee5ee`  |
| 2052   | Layout 1 | `45866aeee5ee`  |
| 2044   | Layout 1 | `45866aeee5ee`  |
| 2039   | Layout 1 | `45866aeee5ee`  |
| 2032   | Layout 1 | `45866aeee5ee`  |
| 2025   | Layout 1 | `45866aeee5ee`  |
| 2011   | Layout 1 | `45866aeee5ee`  |
| 2005   | Layout 1 | `45866aeee5ee`  |
| 2000   | Layout 1 | `45866aeee5ee`  |
| 1996   | Layout 1 | `45866aeee5ee`  |
| 1991   | Layout 1 | `45866aeee5ee`  |
| 1985   | Layout 1 | `45866aeee5ee`  |
| 1980   | Layout 1 | `45866aeee5ee`  |
| 1969   | Layout 1 | `45866aeee5ee`  |
| 1964   | Layout 1 | `45866aeee5ee`  |
| 1958   | Layout 1 | `45866aeee5ee`  |
| 1950   | Layout 1 | `45866aeee5ee`  |
| 1945   | Layout 1 | `45866aeee5ee`  |
| 1937   | Layout 1 | `45866aeee5ee`  |
| 1933   | Layout 1 | `45866aeee5ee`  |
| 1927   | Layout 1 | `45866aeee5ee`  |
| 1921   | Layout 1 | `45866aeee5ee`  |
| 1914   | Layout 1 | `45866aeee5ee`  |
| 1908   | Layout 1 | `45866aeee5ee`  |
| 1897   | Layout 1 | `45866aeee5ee`  |
| 1892   | Layout 1 | `45866aeee5ee`  |
| 1886   | Layout 1 | `45866aeee5ee`  |
| 1881   | Layout 1 | `45866aeee5ee`  |
| 1871   | Layout 1 | `45866aeee5ee`  |
| 1866   | Layout 1 | `45866aeee5ee`  |
| 1862   | Layout 1 | `45866aeee5ee`  |
| 1854   | Layout 1 | `45866aeee5ee`  |
| 1846   | Layout 1 | `45866aeee5ee`  |
| 1838   | Layout 1 | `45866aeee5ee`  |
| 1832   | Layout 1 | `45866aeee5ee`  |
| 1826   | Layout 1 | `45866aeee5ee`  |
| 1822   | Layout 1 | `45866aeee5ee`  |
| 1818   | Layout 1 | `45866aeee5ee`  |
| 1804   | Layout 1 | `45866aeee5ee`  |
| 1794   | Layout 1 | `45866aeee5ee`  |
| 1790   | Layout 1 | `45866aeee5ee`  |
| 1784   | Layout 1 | `45866aeee5ee`  |
| 1774   | Layout 1 | `45866aeee5ee`  |
| 1771   | Layout 1 | `45866aeee5ee`  |
| 1762   | Layout 1 | `45866aeee5ee`  |
| 1759   | Layout 1 | `45866aeee5ee`  |
| 1754   | Layout 1 | `45866aeee5ee`  |
| 1749   | Layout 1 | `45866aeee5ee`  |
| 1743   | Layout 1 | `45866aeee5ee`  |
| 1737   | Layout 1 | `45866aeee5ee`  |
| 1731   | Layout 1 | `45866aeee5ee`  |
| 1725   | Layout 1 | `45866aeee5ee`  |
| 1717   | Layout 1 | `45866aeee5ee`  |
| 1710   | Layout 1 | `45866aeee5ee`  |
| 1704   | Layout 1 | `45866aeee5ee`  |
| 1698   | Layout 1 | `45866aeee5ee`  |
| 1690   | Layout 1 | `45866aeee5ee`  |
| 1685   | Layout 1 | `45866aeee5ee`  |
| 1680   | Layout 1 | `45866aeee5ee`  |
| 1674   | Layout 1 | `45866aeee5ee`  |
| 1668   | Layout 1 | `45866aeee5ee`  |
| 1659   | Layout 1 | `45866aeee5ee`  |
| 1649   | Layout 1 | `45866aeee5ee`  |
| 1642   | Layout 1 | `45866aeee5ee`  |
| 1636   | Layout 1 | `45866aeee5ee`  |
| 1628   | Layout 1 | `45866aeee5ee`  |
| 1622   | Layout 1 | `45866aeee5ee`  |
| 1614   | Layout 1 | `45866aeee5ee`  |
| 1608   | Layout 1 | `45866aeee5ee`  |
| 1602   | Layout 1 | `45866aeee5ee`  |
| 1598   | Layout 1 | `45866aeee5ee`  |
| 1594   | Layout 1 | `45866aeee5ee`  |
| 1590   | Layout 1 | `45866aeee5ee`  |
| 1587   | Layout 1 | `45866aeee5ee`  |
| 1584   | Layout 1 | `45866aeee5ee`  |
| 1579   | Layout 1 | `45866aeee5ee`  |
| 1572   | Layout 1 | `45866aeee5ee`  |
| 1565   | Layout 1 | `45866aeee5ee`  |
| 1559   | Layout 1 | `45866aeee5ee`  |
| 1554   | Layout 1 | `45866aeee5ee`  |
| 1547   | Layout 1 | `45866aeee5ee`  |
| 1537   | Layout 1 | `45866aeee5ee`  |
| 1529   | Layout 1 | `45866aeee5ee`  |
| 1524   | Layout 1 | `45866aeee5ee`  |
| 1519   | Layout 1 | `45866aeee5ee`  |
| 1509   | Layout 1 | `45866aeee5ee`  |
| 1506   | Layout 1 | `45866aeee5ee`  |
| 1504   | Layout 1 | `45866aeee5ee`  |
| 1500   | Layout 1 | `45866aeee5ee`  |
| 1493   | Layout 1 | `45866aeee5ee`  |
| 1489   | Layout 1 | `45866aeee5ee`  |
| 1485   | Layout 1 | `45866aeee5ee`  |
| 1481   | Layout 1 | `45866aeee5ee`  |
| 1474   | Layout 1 | `45866aeee5ee`  |
| 1466   | Layout 1 | `45866aeee5ee`  |
| 1462   | Layout 1 | `45866aeee5ee`  |
| 1459   | Layout 1 | `45866aeee5ee`  |
| 1453   | Layout 1 | `45866aeee5ee`  |
| 1450   | Layout 1 | `45866aeee5ee`  |
| 1445   | Layout 1 | `45866aeee5ee`  |
| 1439   | Layout 1 | `45866aeee5ee`  |
| 1433   | Layout 1 | `45866aeee5ee`  |
| 1430   | Layout 1 | `45866aeee5ee`  |
| 1426   | Layout 1 | `45866aeee5ee`  |
| 1421   | Layout 1 | `45866aeee5ee`  |
| 1417   | Layout 1 | `45866aeee5ee`  |
| 1416   | Layout 1 | `45866aeee5ee`  |
| 1409   | Layout 1 | `45866aeee5ee`  |
| 1405   | Layout 1 | `45866aeee5ee`  |
| 1401   | Layout 1 | `45866aeee5ee`  |
| 1396   | Layout 1 | `45866aeee5ee`  |
| 1391   | Layout 1 | `45866aeee5ee`  |
| 1390   | Layout 1 | `45866aeee5ee`  |
| 1386   | Layout 1 | `45866aeee5ee`  |
| 1381   | Layout 1 | `45866aeee5ee`  |
| 1379   | Layout 1 | `45866aeee5ee`  |
| 1372   | Layout 1 | `45866aeee5ee`  |
| 1366   | Layout 1 | `45866aeee5ee`  |
| 1364   | Layout 1 | `45866aeee5ee`  |
| 1363   | Layout 1 | `45866aeee5ee`  |
| 1360   | Layout 1 | `45866aeee5ee`  |
| 1358   | Layout 1 | `45866aeee5ee`  |
| 1355   | Layout 1 | `45866aeee5ee`  |
| 1351   | Layout 1 | `45866aeee5ee`  |
| 1348   | Layout 1 | `45866aeee5ee`  |
| 1346   | Layout 1 | `45866aeee5ee`  |
| 1341   | Layout 1 | `45866aeee5ee`  |
| 1340   | Layout 1 | `45866aeee5ee`  |
| 1338   | Layout 1 | `45866aeee5ee`  |
| 1335   | Layout 1 | `45866aeee5ee`  |
| 1333   | Layout 1 | `45866aeee5ee`  |
| 1329   | Layout 1 | `45866aeee5ee`  |
| 1327   | Layout 1 | `45866aeee5ee`  |
| 1324   | Layout 1 | `45866aeee5ee`  |
| 1321   | Layout 1 | `45866aeee5ee`  |
| 1319   | Layout 1 | `45866aeee5ee`  |
| 1318   | Layout 1 | `45866aeee5ee`  |
| 1316   | Layout 1 | `45866aeee5ee`  |
| 1313   | Layout 1 | `45866aeee5ee`  |
| 1311   | Layout 1 | `45866aeee5ee`  |
| 1309   | Layout 1 | `45866aeee5ee`  |
| 1304   | Layout 1 | `45866aeee5ee`  |
| 1292   | Layout 1 | `45866aeee5ee`  |
| 1286   | Layout 1 | `45866aeee5ee`  |
| 1280   | Layout 1 | `45866aeee5ee`  |
| 1276   | No file  | `45866aeee5ee`  |
| 1267   | No file  | `45866aeee5ee`  |
| 1261   | No file  | `45866aeee5ee`  |
| 1256   | No file  | `45866aeee5ee`  |
| 1250   | No file  | `45866aeee5ee`  |
| 1246   | No file  | `45866aeee5ee`  |
| 1239   | No file  | `45866aeee5ee`  |
| 1230   | No file  | `45866aeee5ee`  |
| 1226   | No file  | `45866aeee5ee`  |
| 1220   | No file  | `45866aeee5ee`  |
| 1217   | No file  | `45866aeee5ee`  |
| 1211   | No file  | `45866aeee5ee`  |
| 1210   | No file  | `45866aeee5ee`  |
| 1208   | No file  | `45866aeee5ee`  |
| 1203   | No file  | `45866aeee5ee`  |
| 1197   | No file  | `45866aeee5ee`  |
| 1194   | No file  | `45866aeee5ee`  |
| 1192   | No file  | `45866aeee5ee`  |
| 1187   | No file  | `45866aeee5ee`  |
| 1183   | No file  | `45866aeee5ee`  |
| 1177   | No file  | `45866aeee5ee`  |
| 1173   | No file  | `45866aeee5ee`  |
| 1167   | No file  | `45866aeee5ee`  |
| 1164   | No file  | `45866aeee5ee`  |
| 1156   | No file  | `45866aeee5ee`  |
| 1149   | No file  | `45866aeee5ee`  |
| 1144   | No file  | `45866aeee5ee`  |
| 1137   | No file  | `45866aeee5ee`  |
| 1132   | No file  | `45866aeee5ee`  |
| 1127   | No file  | `45866aeee5ee`  |
| 1122   | No file  | `45866aeee5ee`  |
| 1118   | No file  | `45866aeee5ee`  |
| 1114   | No file  | `45866aeee5ee`  |
| 1109   | No file  | `45866aeee5ee`  |
| 1102   | No file  | `45866aeee5ee`  |
| 1096   | No file  | `45866aeee5ee`  |
| 1088   | No file  | `45866aeee5ee`  |
| 1081   | No file  | `45866aeee5ee`  |
| 1076   | No file  | `45866aeee5ee`  |
| 1069   | No file  | `45866aeee5ee`  |
| 1064   | No file  | `45866aeee5ee`  |
| 1058   | No file  | `45866aeee5ee`  |
| 1051   | No file  | `45866aeee5ee`  |
| 1044   | No file  | `45866aeee5ee`  |
| 1036   | No file  | `45866aeee5ee`  |
| 1026   | No file  | `45866aeee5ee`  |
| 1016   | No file  | `45866aeee5ee`  |
| 1009   | No file  | `45866aeee5ee`  |
| 1005   | No file  | `45866aeee5ee`  |
| 1000   | No file  | `45866aeee5ee`  |
| 998    | No file  | `45866aeee5ee`  |
| 990    | No file  | `45866aeee5ee`  |
| 979    | No file  | `45866aeee5ee`  |
| 972    | No file  | `45866aeee5ee`  |
| 963    | No file  | `45866aeee5ee`  |
| 955    | No file  | `45866aeee5ee`  |
| 946    | No file  | `45866aeee5ee`  |
| 938    | No file  | `45866aeee5ee`  |
| 927    | No file  | `45866aeee5ee`  |
| 911    | No file  | `45866aeee5ee`  |
| 904    | No file  | `45866aeee5ee`  |
| 899    | No file  | `45866aeee5ee`  |
| 894    | No file  | `45866aeee5ee`  |
| 885    | No file  | `45866aeee5ee`  |
| 879    | No file  | `45866aeee5ee`  |
| 872    | No file  | `45866aeee5ee`  |
| 864    | No file  | `45866aeee5ee`  |
| 855    | No file  | `45866aeee5ee`  |
| 853    | No file  | `45866aeee5ee`  |
| 845    | No file  | `45866aeee5ee`  |
| 837    | No file  | `45866aeee5ee`  |
| 829    | No file  | `45866aeee5ee`  |
| 822    | No file  | `45866aeee5ee`  |
| 814    | No file  | `45866aeee5ee`  |
| 805    | No file  | `45866aeee5ee`  |
| 794    | No file  | `45866aeee5ee`  |
| 787    | No file  | `45866aeee5ee`  |
| 780    | No file  | `45866aeee5ee`  |
| 771    | No file  | `45866aeee5ee`  |
| 760    | No file  | `45866aeee5ee`  |
| 748    | No file  | `45866aeee5ee`  |
| 741    | No file  | `45866aeee5ee`  |
| 736    | No file  | `45866aeee5ee`  |
| 731    | No file  | `45866aeee5ee`  |
| 723    | No file  | `45866aeee5ee`  |
| 711    | No file  | `45866aeee5ee`  |
| 707    | No file  | `45866aeee5ee`  |
| 697    | No file  | `45866aeee5ee`  |
| 689    | No file  | `45866aeee5ee`  |
| 683    | No file  | `45866aeee5ee`  |
| 678    | No file  | `45866aeee5ee`  |
| 670    | No file  | `45866aeee5ee`  |
| 661    | No file  | `45866aeee5ee`  |
| 656    | No file  | `45866aeee5ee`  |
| 652    | No file  | `45866aeee5ee`  |
| 643    | No file  | `45866aeee5ee`  |
| 637    | No file  | `45866aeee5ee`  |
| 630    | No file  | `45866aeee5ee`  |
| 627    | No file  | `45866aeee5ee`  |
| 621    | No file  | `45866aeee5ee`  |
| 617    | No file  | `45866aeee5ee`  |
| 615    | No file  | `45866aeee5ee`  |
| 606    | No file  | `45866aeee5ee`  |
| 599    | No file  | `45866aeee5ee`  |
| 592    | No file  | `45866aeee5ee`  |
| 586    | No file  | `45866aeee5ee`  |
| 577    | No file  | `45866aeee5ee`  |
| 569    | No file  | `45866aeee5ee`  |
| 561    | No file  | `45866aeee5ee`  |
| 554    | No file  | `45866aeee5ee`  |
| 542    | No file  | `45866aeee5ee`  |
| 532    | No file  | `45866aeee5ee`  |
| 531    | No file  | `45866aeee5ee`  |
| 526    | No file  | `45866aeee5ee`  |
| 521    | No file  | `45866aeee5ee`  |
| 517    | No file  | `45866aeee5ee`  |
| 510    | No file  | `45866aeee5ee`  |
| 508    | No file  | `45866aeee5ee`  |
| 504    | No file  | `45866aeee5ee`  |
| 497    | No file  | `45866aeee5ee`  |
| 491    | No file  | `45866aeee5ee`  |
| 485    | No file  | `45866aeee5ee`  |
| 478    | No file  | `45866aeee5ee`  |
| 472    | No file  | `45866aeee5ee`  |
| 466    | No file  | `45866aeee5ee`  |
| 457    | No file  | `45866aeee5ee`  |
| 452    | No file  | `45866aeee5ee`  |
| 449    | No file  | `45866aeee5ee`  |
| 435    | No file  | `45866aeee5ee`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `personalmonsteroffset.dbss` | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | Which character keys have a `characterstatic.dbss` row, for the key link |
| `languagedata_en.loc`        | Optional | Boss names (type `6`), descriptions (type `61`), item names (type `0`) and the difficulty labels (type `37`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 30 bytes + description, image path and drop items)

| Offset                | Type                    | Field                     | Notes                                                                      |
| --------------------- | ----------------------- | ------------------------- | -------------------------------------------------------------------------- |
| `+0x00`               | u16                     | character_key             | The boss, a `characterstatic.dbss` key                                     |
| `+0x02`               | str16                   | description_kr            | Korean description; LOC type `61` holds it under `character_key`           |
| `description_kr+0x00` | u32                     | difficulty                | `1` to `3`; see Difficulty                                                 |
| `description_kr+0x04` | str8                    | monster_image             | Image path under `ui_texture/` (`UI_Artwork/IC_04013.dds`), or empty       |
| `monster_image+0x00`  | u32                     | drop_item_count           | Number of `drop_item_keys`                                                 |
| `monster_image+0x04`  | u32[drop_item_count]    | drop_item_keys            | Item enchant keys (`enchant_level << 24 \| item_id`); every level is `0` on clients 1784 and 3474 |
| `drop_item_keys+0x00` | u32                     | unknown_drop_item_keys_00 | `0` on every row of clients 1784 and 3474                                  |

The rows are not sorted by key.

### `personalmonsteroffset.dbss`

Bare offset table into `personalmonster.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `personalmonster.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | character_key | Key of the row it points at                                  |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `personalmonster.dbss`, at its `character_key` |
| `+0x06` | u32  | data_size     | The whole row                                                |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key, and the rows fill the file.

## Difficulty

`panel_window_personalmonster_all_1.luac` shows `difficulty` through the
`_difficultyText` table of `panel_window_personalmonster_all.luac`, which
reads the GAME sheet keys `LUA_PERSONALMONSTER_DIFFICULTY_1` to `_3`;
difficulty `3` also turns on the special background of the list row.

| Value | GAME key                           | LOC English    | Rows (client 3474) |
| ----- | ---------------------------------- | -------------- | ------------------ |
| 1     | `LUA_PERSONALMONSTER_DIFFICULTY_1` | Normal         | 2                  |
| 2     | `LUA_PERSONALMONSTER_DIFFICULTY_2` | Difficult      | 2                  |
| 3     | `LUA_PERSONALMONSTER_DIFFICULTY_3` | Very Difficult | 2                  |

## Field Names

The `PersonalMonster_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `Difficulty`,
`Description`, `MonsterImage` and `DropItemList`, and the server-only
(`%`) columns `FirstSpawnTime`, `FirstVariableTime`, `SpawnCoolTime`,
`SpawnVariableTime`, `PositionIndex` and `AcceptCondition`, which the file
does not hold. The client 1784 file has 12 rows, and the sheet matches it on
all 12 keys for `Difficulty`, `Description`, `MonsterImage` (empty where
the sheet has none) and `DropItemList` in order. On client 3474 the 6 rows
still match on `Difficulty`, `Description` and `MonsterImage`; every drop
list changed. The sheet's developer notes call the columns the monster key,
the difficulty (`1` easy, `2` normal, `3` hard), the description and image
shown on world map mouse-over, and the item keys the monster drops.

The client Lua of client 3474 reads the row through
`ToClient_GetPersonalMonsterWrapper(characterKey)`: `getDescription()`,
`getDifficult()`, `getDropItemCount()` and `getDropItemKey(index)`, which
it passes to `getItemEnchantStaticStatus(ItemEnchantKey(itemKey))`. The
boss name comes from `ToClient_GetCharacterStaticStatusWrapper`. The 2016
client's debug symbols have no personal monster type.

## Notes

- The sheet on client 1784 has 30 rows; the client file holds the 12 whose
  `ContentsGroupKey` list contains `585` (`585`, `234, 585` or
  `585, 722`), and none of the 18 without it.
- On client 3474 all 6 rows drop the same 13 items, Dawn Black Stone
  (`820984`) to Gold Bar 1,000G (`5`) and Gold Bar 100G (`4`). Every one
  has a LOC type `0` name.
- LOC type `61` has an English description for each of the 6 keys of
  client 3474; it is the text `getDescription()` shows in the loaded
  language.
- The 6 keys of client 3474 all have a `characterstatic.dbss` row and a
  LOC type `6` name.
- `drop_item_count` is a u32 and `difficulty` a u32 by the byte count of
  the row; no value on clients 1784 and 3474 needs more than one byte.

## Open Questions

### unknown_drop_item_keys_00

The last u32 of every row is `0` on clients 1784 and 3474. The sheet's
last client column is `ContentsGroupKey` (`585` on every row the file
holds), so the field is not that list unless the build leaves it out; it
could be the count of a list that is always empty. No Lua getter reads a
fifth value.
