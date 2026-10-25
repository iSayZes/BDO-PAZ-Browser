# `villagesiegeinfo.bss` Format

## Purpose

The areas of the Node War (village siege) region map, one row per colour
of `ui_texture/minimap/area/villagesiegemap_2024.bmp`: the colour, a copy
of it, the node war region the area covers and the area number that the
[`worldmapsiegeregionforconquest.bss`](worldmapgrid_bss.md) grid stores
in its cells. Client 3482 has 41 rows: 36 node war nodes,
the four capitals and the `0d0d0d` row with no region. The rows have the
shape of the [`oceansiegeinfo.bss`](oceansiegeinfo_bss.md) rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records | Row bytes               |
| ------ | -------------- | ---------------------- | ----- | ------- | ----------------------- |
| 2      | 2978 and later | `villagesiegeinfo.bss` | 674   | 41 Row  | 14 to 16, 16 on average |
| 1      | 1276 to 2970   | `villagesiegeinfo.bss` | 1,820 | 59 Row  | 22 to 24, 24 on average |

| Layout | File                   | Known           | Unknown       |
| ------ | ---------------------- | --------------- | ------------- |
| 2      | `villagesiegeinfo.bss` | 592 B (87.8%)   | 82 B (12.2%)  |
| 1      | `villagesiegeinfo.bss` | 1,230 B (67.6%) | 590 B (32.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `5efd632ca03a`  |
| 3482   | Layout 2             | `5efd632ca03a`  |
| 3474   | Layout 2             | `5efd632ca03a`  |
| 3473   | Layout 2             | `5efd632ca03a`  |
| 3464   | Layout 2             | `5efd632ca03a`  |
| 3458   | Layout 2             | `5efd632ca03a`  |
| 3454   | Layout 2             | `5efd632ca03a`  |
| 3444   | Layout 2             | `5efd632ca03a`  |
| 3435   | Layout 2             | `5efd632ca03a`  |
| 3426   | Layout 2             | `5efd632ca03a`  |
| 3418   | Layout 2             | `5efd632ca03a`  |
| 3412   | Layout 2             | `5efd632ca03a`  |
| 3402   | Layout 2             | `5efd632ca03a`  |
| 3396   | Layout 2             | `5efd632ca03a`  |
| 3387   | Layout 2             | `5efd632ca03a`  |
| 3381   | Layout 2             | `5efd632ca03a`  |
| 3373   | Layout 2             | `5efd632ca03a`  |
| 3364   | Layout 2             | `5efd632ca03a`  |
| 3356   | Layout 2             | `5efd632ca03a`  |
| 3349   | Layout 2             | `5efd632ca03a`  |
| 3342   | Layout 2             | `5efd632ca03a`  |
| 3335   | Layout 2             | `5efd632ca03a`  |
| 3326   | Layout 2             | `5efd632ca03a`  |
| 3321   | Layout 2             | `5efd632ca03a`  |
| 3314   | Layout 2             | `5efd632ca03a`  |
| 3303   | Layout 2             | `5efd632ca03a`  |
| 3302   | Layout 2             | `5efd632ca03a`  |
| 3293   | Layout 2             | `5efd632ca03a`  |
| 3283   | Layout 2             | `5efd632ca03a`  |
| 3275   | Layout 2             | `5efd632ca03a`  |
| 3267   | Layout 2             | `5efd632ca03a`  |
| 3258   | Layout 2             | `5efd632ca03a`  |
| 3251   | Layout 2             | `5efd632ca03a`  |
| 3242   | Layout 2             | `5efd632ca03a`  |
| 3235   | Layout 2             | `5efd632ca03a`  |
| 3229   | Layout 2             | `5efd632ca03a`  |
| 3212   | Layout 2             | `5efd632ca03a`  |
| 3203   | Layout 2             | `5efd632ca03a`  |
| 3193   | Layout 2             | `5efd632ca03a`  |
| 3186   | Layout 2             | `5efd632ca03a`  |
| 3177   | Layout 2             | `5efd632ca03a`  |
| 3169   | Layout 2             | `5efd632ca03a`  |
| 3158   | Layout 2             | `5efd632ca03a`  |
| 3151   | Layout 2             | `5efd632ca03a`  |
| 3144   | Layout 2             | `5efd632ca03a`  |
| 3133   | Layout 2             | `5efd632ca03a`  |
| 3125   | Layout 2             | `5efd632ca03a`  |
| 3118   | Layout 2             | `5efd632ca03a`  |
| 3111   | Layout 2             | `5efd632ca03a`  |
| 3103   | Layout 2             | `5efd632ca03a`  |
| 3095   | Layout 2             | `5efd632ca03a`  |
| 3086   | Layout 2             | `5efd632ca03a`  |
| 3072   | Layout 2             | `5efd632ca03a`  |
| 3062   | Layout 2             | `5efd632ca03a`  |
| 3052   | Layout 2             | `5efd632ca03a`  |
| 3045   | Layout 2             | `5efd632ca03a`  |
| 3037   | Layout 2             | `5efd632ca03a`  |
| 3030   | Layout 2             | `5efd632ca03a`  |
| 3021   | Layout 2             | `5efd632ca03a`  |
| 3012   | Layout 2             | `5efd632ca03a`  |
| 3002   | Layout 2             | `5efd632ca03a`  |
| 2995   | Layout 2             | `5efd632ca03a`  |
| 2987   | Layout 2             | `5efd632ca03a`  |
| 2978   | Layout 2             | `5efd632ca03a`  |
| 2970   | Layout 1             | `5efd632ca03a`  |
| 2959   | Layout 1             | `5efd632ca03a`  |
| 2951   | Layout 1             | `5efd632ca03a`  |
| 2942   | Layout 1             | `5efd632ca03a`  |
| 2935   | Layout 1             | `5efd632ca03a`  |
| 2932   | Layout 1             | `5efd632ca03a`  |
| 2923   | Layout 1             | `5efd632ca03a`  |
| 2919   | Layout 1             | `5efd632ca03a`  |
| 2907   | Layout 1             | `5efd632ca03a`  |
| 2900   | Layout 1             | `5efd632ca03a`  |
| 2891   | Layout 1             | `5efd632ca03a`  |
| 2882   | Layout 1             | `5efd632ca03a`  |
| 2872   | Layout 1             | `5efd632ca03a`  |
| 2863   | Layout 1             | `5efd632ca03a`  |
| 2855   | Layout 1             | `5efd632ca03a`  |
| 2849   | Layout 1             | `5efd632ca03a`  |
| 2844   | Layout 1             | `5efd632ca03a`  |
| 2834   | Layout 1             | `5efd632ca03a`  |
| 2825   | Layout 1             | `5efd632ca03a`  |
| 2819   | Layout 1             | `5efd632ca03a`  |
| 2811   | Layout 1             | `5efd632ca03a`  |
| 2803   | Layout 1             | `5efd632ca03a`  |
| 2794   | Layout 1             | `5efd632ca03a`  |
| 2783   | Layout 1             | `5efd632ca03a`  |
| 2774   | Layout 1             | `5efd632ca03a`  |
| 2765   | Layout 1             | `5efd632ca03a`  |
| 2756   | Layout 1             | `5efd632ca03a`  |
| 2750   | Layout 1             | `5efd632ca03a`  |
| 2743   | Layout 1             | `5efd632ca03a`  |
| 2736   | Layout 1             | `5efd632ca03a`  |
| 2726   | Layout 1             | `5efd632ca03a`  |
| 2717   | Layout 1             | `5efd632ca03a`  |
| 2709   | Layout 1             | `5efd632ca03a`  |
| 2703   | Layout 1             | `5efd632ca03a`  |
| 2695   | Layout 1             | `5efd632ca03a`  |
| 2684   | Layout 1             | `5efd632ca03a`  |
| 2672   | Layout 1             | `5efd632ca03a`  |
| 2665   | Layout 1             | `5efd632ca03a`  |
| 2657   | Layout 1             | `5efd632ca03a`  |
| 2649   | Layout 1             | `5efd632ca03a`  |
| 2644   | Layout 1             | `5efd632ca03a`  |
| 2637   | Layout 1             | `5efd632ca03a`  |
| 2629   | Layout 1             | `5efd632ca03a`  |
| 2619   | Layout 1             | `5efd632ca03a`  |
| 2612   | Layout 1             | `5efd632ca03a`  |
| 2606   | Layout 1             | `5efd632ca03a`  |
| 2602   | Layout 1             | `5efd632ca03a`  |
| 2601   | Layout 1             | `5efd632ca03a`  |
| 2592   | Layout 1             | `5efd632ca03a`  |
| 2583   | Layout 1             | `5efd632ca03a`  |
| 2575   | Layout 1             | `5efd632ca03a`  |
| 2567   | Layout 1             | `5efd632ca03a`  |
| 2560   | Layout 1             | `5efd632ca03a`  |
| 2553   | Layout 1             | `5efd632ca03a`  |
| 2545   | Layout 1             | `5efd632ca03a`  |
| 2538   | Layout 1             | `5efd632ca03a`  |
| 2529   | Layout 1             | `5efd632ca03a`  |
| 2519   | Layout 1             | `5efd632ca03a`  |
| 2513   | Layout 1             | `5efd632ca03a`  |
| 2510   | Layout 1             | `5efd632ca03a`  |
| 2507   | Layout 1             | `5efd632ca03a`  |
| 2503   | Layout 1             | `5efd632ca03a`  |
| 2498   | Layout 1             | `5efd632ca03a`  |
| 2492   | Layout 1             | `5efd632ca03a`  |
| 2487   | Layout 1             | `5efd632ca03a`  |
| 2480   | Layout 1             | `5efd632ca03a`  |
| 2474   | Layout 1             | `5efd632ca03a`  |
| 2468   | Layout 1             | `5efd632ca03a`  |
| 2460   | Layout 1             | `5efd632ca03a`  |
| 2453   | Layout 1             | `5efd632ca03a`  |
| 2444   | Layout 1             | `5efd632ca03a`  |
| 2438   | Layout 1             | `5efd632ca03a`  |
| 2434   | Layout 1             | `5efd632ca03a`  |
| 2429   | Layout 1             | `5efd632ca03a`  |
| 2421   | Layout 1             | `5efd632ca03a`  |
| 2414   | Layout 1             | `5efd632ca03a`  |
| 2407   | Layout 1             | `5efd632ca03a`  |
| 2401   | Layout 1             | `5efd632ca03a`  |
| 2397   | Layout 1             | `5efd632ca03a`  |
| 2393   | Layout 1             | `5efd632ca03a`  |
| 2384   | Layout 1             | `5efd632ca03a`  |
| 2378   | Layout 1             | `5efd632ca03a`  |
| 2372   | Layout 1             | `5efd632ca03a`  |
| 2358   | Layout 1             | `5efd632ca03a`  |
| 2352   | Layout 1             | `5efd632ca03a`  |
| 2347   | Layout 1             | `5efd632ca03a`  |
| 2343   | Layout 1             | `5efd632ca03a`  |
| 2335   | Layout 1             | `5efd632ca03a`  |
| 2327   | Layout 1             | `5efd632ca03a`  |
| 2324   | Layout 1             | `5efd632ca03a`  |
| 2319   | Layout 1             | `5efd632ca03a`  |
| 2313   | Layout 1             | `5efd632ca03a`  |
| 2308   | Layout 1             | `5efd632ca03a`  |
| 2302   | Layout 1             | `5efd632ca03a`  |
| 2295   | Layout 1             | `5efd632ca03a`  |
| 2290   | Layout 1             | `5efd632ca03a`  |
| 2284   | Layout 1             | `5efd632ca03a`  |
| 2276   | Layout 1             | `5efd632ca03a`  |
| 2269   | Layout 1             | `5efd632ca03a`  |
| 2259   | Layout 1             | `5efd632ca03a`  |
| 2250   | Layout 1             | `5efd632ca03a`  |
| 2243   | Layout 1             | `5efd632ca03a`  |
| 2235   | Layout 1             | `5efd632ca03a`  |
| 2229   | Layout 1             | `5efd632ca03a`  |
| 2224   | Layout 1             | `5efd632ca03a`  |
| 2218   | Layout 1             | `5efd632ca03a`  |
| 2215   | Layout 1             | `5efd632ca03a`  |
| 2207   | Layout 1             | `5efd632ca03a`  |
| 2203   | Layout 1             | `5efd632ca03a`  |
| 2196   | Layout 1             | `5efd632ca03a`  |
| 2192   | Layout 1             | `5efd632ca03a`  |
| 2189   | Layout 1             | `5efd632ca03a`  |
| 2183   | Layout 1             | `5efd632ca03a`  |
| 2179   | Layout 1             | `5efd632ca03a`  |
| 2171   | Layout 1             | `5efd632ca03a`  |
| 2163   | Layout 1             | `5efd632ca03a`  |
| 2156   | Layout 1             | `5efd632ca03a`  |
| 2151   | Layout 1             | `5efd632ca03a`  |
| 2147   | Layout 1             | `5efd632ca03a`  |
| 2142   | Layout 1             | `5efd632ca03a`  |
| 2138   | Layout 1             | `5efd632ca03a`  |
| 2134   | Layout 1             | `5efd632ca03a`  |
| 2130   | Layout 1             | `5efd632ca03a`  |
| 2122   | Layout 1             | `5efd632ca03a`  |
| 2107   | Layout 1             | `5efd632ca03a`  |
| 2098   | Layout 1             | `5efd632ca03a`  |
| 2089   | Layout 1             | `5efd632ca03a`  |
| 2081   | Layout 1             | `5efd632ca03a`  |
| 2073   | Layout 1             | `5efd632ca03a`  |
| 2067   | Layout 1             | `5efd632ca03a`  |
| 2063   | Layout 1             | `5efd632ca03a`  |
| 2059   | Layout 1             | `5efd632ca03a`  |
| 2052   | Layout 1             | `5efd632ca03a`  |
| 2044   | Layout 1             | `5efd632ca03a`  |
| 2039   | Layout 1             | `5efd632ca03a`  |
| 2032   | Layout 1             | `5efd632ca03a`  |
| 2025   | Layout 1             | `5efd632ca03a`  |
| 2011   | Layout 1             | `5efd632ca03a`  |
| 2005   | Layout 1             | `5efd632ca03a`  |
| 2000   | Layout 1             | `5efd632ca03a`  |
| 1996   | Layout 1             | `5efd632ca03a`  |
| 1991   | Layout 1             | `5efd632ca03a`  |
| 1985   | Layout 1             | `5efd632ca03a`  |
| 1980   | Layout 1             | `5efd632ca03a`  |
| 1969   | Layout 1             | `5efd632ca03a`  |
| 1964   | Layout 1             | `5efd632ca03a`  |
| 1958   | Layout 1             | `5efd632ca03a`  |
| 1950   | Layout 1             | `5efd632ca03a`  |
| 1945   | Layout 1             | `5efd632ca03a`  |
| 1937   | Layout 1             | `5efd632ca03a`  |
| 1933   | Layout 1             | `5efd632ca03a`  |
| 1927   | Layout 1             | `5efd632ca03a`  |
| 1921   | Layout 1             | `5efd632ca03a`  |
| 1914   | Layout 1             | `5efd632ca03a`  |
| 1908   | Layout 1             | `5efd632ca03a`  |
| 1897   | Layout 1             | `5efd632ca03a`  |
| 1892   | Layout 1             | `5efd632ca03a`  |
| 1886   | Layout 1             | `5efd632ca03a`  |
| 1881   | Layout 1             | `5efd632ca03a`  |
| 1871   | Layout 1             | `5efd632ca03a`  |
| 1866   | Layout 1             | `5efd632ca03a`  |
| 1862   | Layout 1             | `5efd632ca03a`  |
| 1854   | Layout 1             | `5efd632ca03a`  |
| 1846   | Layout 1             | `5efd632ca03a`  |
| 1838   | Layout 1             | `5efd632ca03a`  |
| 1832   | Layout 1             | `5efd632ca03a`  |
| 1826   | Layout 1             | `5efd632ca03a`  |
| 1822   | Layout 1             | `5efd632ca03a`  |
| 1818   | Layout 1             | `5efd632ca03a`  |
| 1804   | Layout 1             | `5efd632ca03a`  |
| 1794   | Layout 1             | `5efd632ca03a`  |
| 1790   | Layout 1             | `5efd632ca03a`  |
| 1784   | Layout 1             | `5efd632ca03a`  |
| 1774   | Layout 1             | `5efd632ca03a`  |
| 1771   | Layout 1             | `5efd632ca03a`  |
| 1762   | Layout 1             | `5efd632ca03a`  |
| 1759   | Layout 1             | `5efd632ca03a`  |
| 1754   | Layout 1             | `5efd632ca03a`  |
| 1749   | Layout 1             | `5efd632ca03a`  |
| 1743   | Layout 1             | `5efd632ca03a`  |
| 1737   | Layout 1             | `5efd632ca03a`  |
| 1731   | Layout 1             | `5efd632ca03a`  |
| 1725   | Layout 1             | `5efd632ca03a`  |
| 1717   | Layout 1             | `5efd632ca03a`  |
| 1710   | Layout 1             | `5efd632ca03a`  |
| 1704   | Layout 1             | `5efd632ca03a`  |
| 1698   | Layout 1             | `5efd632ca03a`  |
| 1690   | Layout 1             | `5efd632ca03a`  |
| 1685   | Layout 1             | `5efd632ca03a`  |
| 1680   | Layout 1             | `5efd632ca03a`  |
| 1674   | Layout 1             | `5efd632ca03a`  |
| 1668   | Layout 1             | `5efd632ca03a`  |
| 1659   | Layout 1             | `5efd632ca03a`  |
| 1649   | Layout 1             | `5efd632ca03a`  |
| 1642   | Layout 1             | `5efd632ca03a`  |
| 1636   | Layout 1             | `5efd632ca03a`  |
| 1628   | Layout 1             | `5efd632ca03a`  |
| 1622   | Layout 1             | `5efd632ca03a`  |
| 1614   | Layout 1             | `5efd632ca03a`  |
| 1608   | Layout 1             | `5efd632ca03a`  |
| 1602   | Layout 1             | `5efd632ca03a`  |
| 1598   | Layout 1             | `5efd632ca03a`  |
| 1594   | Layout 1             | `5efd632ca03a`  |
| 1590   | Layout 1             | `5efd632ca03a`  |
| 1587   | Layout 1             | `5efd632ca03a`  |
| 1584   | Layout 1             | `5efd632ca03a`  |
| 1579   | Layout 1             | `5efd632ca03a`  |
| 1572   | Layout 1             | `5efd632ca03a`  |
| 1565   | Layout 1             | `5efd632ca03a`  |
| 1559   | Layout 1             | `5efd632ca03a`  |
| 1554   | Layout 1             | `5efd632ca03a`  |
| 1547   | Layout 1             | `5efd632ca03a`  |
| 1537   | Layout 1             | `5efd632ca03a`  |
| 1529   | Layout 1             | `5efd632ca03a`  |
| 1524   | Layout 1             | `5efd632ca03a`  |
| 1519   | Layout 1             | `5efd632ca03a`  |
| 1509   | Layout 1             | `5efd632ca03a`  |
| 1506   | Layout 1             | `5efd632ca03a`  |
| 1504   | Layout 1             | `5efd632ca03a`  |
| 1500   | Layout 1             | `5efd632ca03a`  |
| 1493   | Layout 1             | `5efd632ca03a`  |
| 1489   | Layout 1             | `5efd632ca03a`  |
| 1485   | Layout 1             | `5efd632ca03a`  |
| 1481   | Layout 1             | `5efd632ca03a`  |
| 1474   | Layout 1             | `5efd632ca03a`  |
| 1466   | Layout 1             | `5efd632ca03a`  |
| 1462   | Layout 1             | `5efd632ca03a`  |
| 1459   | Layout 1             | `5efd632ca03a`  |
| 1453   | Layout 1             | `5efd632ca03a`  |
| 1450   | Layout 1             | `5efd632ca03a`  |
| 1445   | Layout 1             | `5efd632ca03a`  |
| 1439   | Layout 1             | `5efd632ca03a`  |
| 1433   | Layout 1             | `5efd632ca03a`  |
| 1430   | Layout 1             | `5efd632ca03a`  |
| 1426   | Layout 1             | `5efd632ca03a`  |
| 1421   | Layout 1             | `5efd632ca03a`  |
| 1417   | Layout 1             | `5efd632ca03a`  |
| 1416   | Layout 1             | `5efd632ca03a`  |
| 1409   | Layout 1             | `5efd632ca03a`  |
| 1405   | Layout 1             | `5efd632ca03a`  |
| 1401   | Layout 1             | `5efd632ca03a`  |
| 1396   | Layout 1             | `5efd632ca03a`  |
| 1391   | Layout 1             | `5efd632ca03a`  |
| 1390   | Layout 1             | `5efd632ca03a`  |
| 1386   | Layout 1             | `5efd632ca03a`  |
| 1381   | Layout 1             | `5efd632ca03a`  |
| 1379   | Layout 1             | `5efd632ca03a`  |
| 1372   | Layout 1             | `5efd632ca03a`  |
| 1366   | Layout 1             | `5efd632ca03a`  |
| 1364   | Layout 1             | `5efd632ca03a`  |
| 1363   | Layout 1             | `5efd632ca03a`  |
| 1360   | Layout 1             | `5efd632ca03a`  |
| 1358   | Layout 1             | `5efd632ca03a`  |
| 1355   | Layout 1             | `5efd632ca03a`  |
| 1351   | Layout 1             | `5efd632ca03a`  |
| 1348   | Layout 1             | `5efd632ca03a`  |
| 1346   | Layout 1             | `5efd632ca03a`  |
| 1341   | Layout 1             | `5efd632ca03a`  |
| 1340   | Layout 1             | `5efd632ca03a`  |
| 1338   | Layout 1             | `5efd632ca03a`  |
| 1335   | Layout 1             | `5efd632ca03a`  |
| 1333   | Layout 1             | `5efd632ca03a`  |
| 1329   | Layout 1             | `5efd632ca03a`  |
| 1327   | Layout 1             | `5efd632ca03a`  |
| 1324   | Layout 1             | `5efd632ca03a`  |
| 1321   | Layout 1             | `5efd632ca03a`  |
| 1319   | Layout 1             | `5efd632ca03a`  |
| 1318   | Layout 1             | `5efd632ca03a`  |
| 1316   | Layout 1             | `5efd632ca03a`  |
| 1313   | Layout 1             | `5efd632ca03a`  |
| 1311   | Layout 1             | `5efd632ca03a`  |
| 1309   | Layout 1             | `5efd632ca03a`  |
| 1304   | Layout 1             | `5efd632ca03a`  |
| 1292   | Layout 1             | `5efd632ca03a`  |
| 1286   | Layout 1             | `5efd632ca03a`  |
| 1280   | Layout 1             | `5efd632ca03a`  |
| 1276   | Layout 1             | `5efd632ca03a`  |
| 1267   | No documented layout | `5efd632ca03a`  |
| 1261   | No documented layout | `5efd632ca03a`  |
| 1256   | No documented layout | `5efd632ca03a`  |
| 1250   | No documented layout | `5efd632ca03a`  |
| 1246   | No documented layout | `5efd632ca03a`  |
| 1239   | No documented layout | `5efd632ca03a`  |
| 1230   | No documented layout | `5efd632ca03a`  |
| 1226   | No documented layout | `5efd632ca03a`  |
| 1220   | No documented layout | `5efd632ca03a`  |
| 1217   | No documented layout | `5efd632ca03a`  |
| 1211   | No documented layout | `5efd632ca03a`  |
| 1210   | No documented layout | `5efd632ca03a`  |
| 1208   | No documented layout | `5efd632ca03a`  |
| 1203   | No documented layout | `5efd632ca03a`  |
| 1197   | No documented layout | `5efd632ca03a`  |
| 1194   | No documented layout | `5efd632ca03a`  |
| 1192   | No documented layout | `5efd632ca03a`  |
| 1187   | No documented layout | `5efd632ca03a`  |
| 1183   | No documented layout | `5efd632ca03a`  |
| 1177   | No documented layout | `5efd632ca03a`  |
| 1173   | No documented layout | `5efd632ca03a`  |
| 1167   | No documented layout | `5efd632ca03a`  |
| 1164   | No documented layout | `5efd632ca03a`  |
| 1156   | No documented layout | `5efd632ca03a`  |
| 1149   | No documented layout | `5efd632ca03a`  |
| 1144   | No documented layout | `5efd632ca03a`  |
| 1137   | No documented layout | `5efd632ca03a`  |
| 1132   | No documented layout | `5efd632ca03a`  |
| 1127   | No documented layout | `5efd632ca03a`  |
| 1122   | No documented layout | `5efd632ca03a`  |
| 1118   | No documented layout | `5efd632ca03a`  |
| 1114   | No documented layout | `5efd632ca03a`  |
| 1109   | No documented layout | `5efd632ca03a`  |
| 1102   | No documented layout | `5efd632ca03a`  |
| 1096   | No documented layout | `5efd632ca03a`  |
| 1088   | No documented layout | `5efd632ca03a`  |
| 1081   | No documented layout | `5efd632ca03a`  |
| 1076   | No documented layout | `5efd632ca03a`  |
| 1069   | No documented layout | `5efd632ca03a`  |
| 1064   | No documented layout | `5efd632ca03a`  |
| 1058   | No documented layout | `5efd632ca03a`  |
| 1051   | No documented layout | `5efd632ca03a`  |
| 1044   | No documented layout | `5efd632ca03a`  |
| 1036   | No documented layout | `5efd632ca03a`  |
| 1026   | No documented layout | `5efd632ca03a`  |
| 1016   | No documented layout | `5efd632ca03a`  |
| 1009   | No documented layout | `5efd632ca03a`  |
| 1005   | No documented layout | `5efd632ca03a`  |
| 1000   | No documented layout | `5efd632ca03a`  |
| 998    | No documented layout | `5efd632ca03a`  |
| 990    | No documented layout | `5efd632ca03a`  |
| 979    | No documented layout | `5efd632ca03a`  |
| 972    | No documented layout | `5efd632ca03a`  |
| 963    | No documented layout | `5efd632ca03a`  |
| 955    | No documented layout | `5efd632ca03a`  |
| 946    | No documented layout | `5efd632ca03a`  |
| 938    | No documented layout | `5efd632ca03a`  |
| 927    | No documented layout | `5efd632ca03a`  |
| 911    | No documented layout | `5efd632ca03a`  |
| 904    | No documented layout | `5efd632ca03a`  |
| 899    | No documented layout | `5efd632ca03a`  |
| 894    | No documented layout | `5efd632ca03a`  |
| 885    | No documented layout | `5efd632ca03a`  |
| 879    | No documented layout | `5efd632ca03a`  |
| 872    | No documented layout | `5efd632ca03a`  |
| 864    | No documented layout | `5efd632ca03a`  |
| 855    | No documented layout | `5efd632ca03a`  |
| 853    | No documented layout | `5efd632ca03a`  |
| 845    | No documented layout | `5efd632ca03a`  |
| 837    | No documented layout | `5efd632ca03a`  |
| 829    | No documented layout | `5efd632ca03a`  |
| 822    | No documented layout | `5efd632ca03a`  |
| 814    | No documented layout | `5efd632ca03a`  |
| 805    | No documented layout | `5efd632ca03a`  |
| 794    | No documented layout | `5efd632ca03a`  |
| 787    | No documented layout | `5efd632ca03a`  |
| 780    | No documented layout | `5efd632ca03a`  |
| 771    | No documented layout | `5efd632ca03a`  |
| 760    | No documented layout | `5efd632ca03a`  |
| 748    | No documented layout | `5efd632ca03a`  |
| 741    | No documented layout | `5efd632ca03a`  |
| 736    | No documented layout | `5efd632ca03a`  |
| 731    | No documented layout | `5efd632ca03a`  |
| 723    | No documented layout | `5efd632ca03a`  |
| 711    | No documented layout | `5efd632ca03a`  |
| 707    | No documented layout | `5efd632ca03a`  |
| 697    | No documented layout | `5efd632ca03a`  |
| 689    | No documented layout | `5efd632ca03a`  |
| 683    | No documented layout | `5efd632ca03a`  |
| 678    | No documented layout | `5efd632ca03a`  |
| 670    | No documented layout | `5efd632ca03a`  |
| 661    | No documented layout | `5efd632ca03a`  |
| 656    | No documented layout | `5efd632ca03a`  |
| 652    | No documented layout | `5efd632ca03a`  |
| 643    | No documented layout | `5efd632ca03a`  |
| 637    | No documented layout | `5efd632ca03a`  |
| 630    | No documented layout | `5efd632ca03a`  |
| 627    | No documented layout | `5efd632ca03a`  |
| 621    | No documented layout | `5efd632ca03a`  |
| 617    | No documented layout | `5efd632ca03a`  |
| 615    | No documented layout | `5efd632ca03a`  |
| 606    | No documented layout | `5efd632ca03a`  |
| 599    | No documented layout | `5efd632ca03a`  |
| 592    | No documented layout | `5efd632ca03a`  |
| 586    | No documented layout | `5efd632ca03a`  |
| 577    | No documented layout | `5efd632ca03a`  |
| 569    | No documented layout | `5efd632ca03a`  |
| 561    | No documented layout | `5efd632ca03a`  |
| 554    | No documented layout | `5efd632ca03a`  |
| 542    | No documented layout | `5efd632ca03a`  |
| 532    | No documented layout | `5efd632ca03a`  |
| 531    | No documented layout | `5efd632ca03a`  |
| 526    | No documented layout | `5efd632ca03a`  |
| 521    | No documented layout | `5efd632ca03a`  |
| 517    | No documented layout | `5efd632ca03a`  |
| 510    | No documented layout | `5efd632ca03a`  |
| 508    | No documented layout | `5efd632ca03a`  |
| 504    | No documented layout | `5efd632ca03a`  |
| 497    | No documented layout | `5efd632ca03a`  |
| 491    | No documented layout | `5efd632ca03a`  |
| 485    | No documented layout | `5efd632ca03a`  |
| 478    | No documented layout | `5efd632ca03a`  |
| 472    | No documented layout | `5efd632ca03a`  |
| 466    | No documented layout | `5efd632ca03a`  |
| 457    | No documented layout | `5efd632ca03a`  |
| 452    | No documented layout | `5efd632ca03a`  |
| 449    | No documented layout | `5efd632ca03a`  |
| 435    | No documented layout | `5efd632ca03a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Region names, LOC type 17, for the `region_keys` cell |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 14 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                                      |
| ------------------ | --------------------- | ---------------------- | -------------------------------------------------------------------------- |
| `+0x00`            | bytes[3]              | map_color              | Region map colour, stored blue, green, red; unique per row. See Map Colours |
| `+0x03`            | u8                    | unknown_03             | Always `0`                                                                 |
| `+0x04`            | bytes[3]              | map_color_dup          | Equals `map_color` on every row; see Field Names                           |
| `+0x07`            | u8                    | unknown_07             | Always `0`                                                                 |
| `+0x08`            | u32                   | region_key_count       | Number of `region_keys`; `0` or `1` on client 3482                         |
| `+0x0C`            | u16[region_key_count] | region_keys            | `regioninfo.bss` region keys, LOC type 17 names. See Map Colours           |
| `region_keys+0x00` | u16                   | area_number            | Cell value of `worldmapsiegeregionforconquest.bss` for this area; `0` to `40` on client 3482, unique per row. See Area Number |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482, `27` on client 1784 |
| `+0x04` | pstr[string_count] | strings      | Read by `unknown_str_ref` in Layout 1 only                |

## Layout 1

### Row (variable: 22 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                              |
| ------------------ | --------------------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`            | bytes[3]              | map_color              |                                                                    |
| `+0x03`            | u8                    | unknown_03             |                                                                    |
| `+0x04`            | bytes[3]              | map_color_dup          |                                                                    |
| `+0x07`            | u8                    | unknown_07             |                                                                    |
| `+0x08`            | u32                   | region_key_count       |                                                                    |
| `+0x0C`            | u16[region_key_count] | region_keys            |                                                                    |
| `region_keys+0x00` | u32                   | unknown_str_ref        | Index into the string table: 27 Korean town names on client 1784   |
| `region_keys+0x04` | u16                   | area_number            | As in Layout 2; `0` to `81` on client 1784, unique per row         |
| `region_keys+0x06` | u32                   | unknown_region_keys_06 | `0` on every row of client 1784                                    |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`, the region,
its territory in `regioninfo.bss` and the area number. The `.rid`
position is the colour's place in `villagesiegemap_2024.bmp.rid` (2024),
or for the four capitals in `villagesiegemap.bmp.rid` (old map).

| `map_color` | `region_keys`                 | Territory    | `area_number`            | Position in `.rid` |
| ----------- | ----------------------------- | ------------ | ------------------------ | ------------------ |
| `3c784b`    | 1556 Great Red Spot           | Outer Edania | 39                       | 2024: 5            |
| `781ecd`    | 12 Forest of Plunder          | Balenos      | 2                        | 2024: 16           |
| `0d0d0d`    | none                          |              | 0                        | 2024: 1            |
| `1ecdcd`    | 16 Bartali Farm               | Balenos      | 3                        | 2024: 20           |
| `3cc8c8`    | 1574 Great White Spot         | Outer Edania | 36                       | 2024: 6            |
| `d5ffa4`    | 32 Heidel                     | Serendia     | 26                       | old map: 19        |
| `1e2dcd`    | 15 Cron Castle                | Balenos      | 1                        | 2024: 14           |
| `a573cd`    | 343 Wolf Hills                | Balenos      | 4                        | 2024: 15           |
| `9696fa`    | 186 Quint Hill                | Calpheon     | 17                       | 2024: 18           |
| `7878fa`    | 113 Hexe Sanctuary            | Calpheon     | 16                       | 2024: 31           |
| `e6e6fa`    | 290 Longleaf Tree Sentry Post | Calpheon     | 15                       | 2024: 30           |
| `782dcd`    | 7 Altar of Agris              | Balenos      | 5                        | 2024: 17           |
| `78787d`    | 73 Biraghi Den                | Serendia     | 7                        | 2024: 24           |
| `6464cd`    | 9 Western Guard Camp          | Balenos      | 6                        | 2024: 19           |
| `5680c1`    | 1349 City of the Dead         | Ulukita      | 34                       | 2024: 35           |
| `4b4b7d`    | 37 Glish Swamp                | Serendia     | 12                       | 2024: 25           |
| `a5a57d`    | 60 Alejandro Farm             | Serendia     | 8                        | 2024: 22           |
| `e1e17d`    | 67 Bloody Monastery           | Serendia     | 9                        | 2024: 29           |
| `b4b47d`    | 71 Castle Ruins               | Serendia     | 10                       | 2024: 26           |
| `ffe4f6`    | 5 Velia                       | Balenos      | 25                       | old map: 7         |
| `c8c87d`    | 74 Orc Camp                   | Serendia     | 11                       | 2024: 27           |
| `b4b4fa`    | 198 Khuruto Cave              | Calpheon     | 13                       | 2024: 21           |
| `8c2323`    | 638 Altas Farmland            | Valencia     | 24                       | 2024: 9            |
| `fafafa`    | 247 Calpheon Castle Site      | Calpheon     | 14                       | 2024: 23           |
| `e1e1fa`    | 127 Trina Fort                | Calpheon     | 18                       | 2024: 28           |
| `8ce6e6`    | 616 Rakshan Observatory       | Valencia     | 23                       | 2024: 11           |
| `8c9696`    | 692 Areha Palm Forest         | Valencia     | 19                       | 2024: 12           |
| `8c5050`    | 682 Ancado Coast              | Valencia     | 20                       | 2024: 8            |
| `8ca5a5`    | 615 Pilgrim's Sanctum: Fast   | Valencia     | 21                       | 2024: 13           |
| `561e0c`    | 1379 Karasi Canyon            | Ulukita      | 32                       | 2024: 36           |
| `8cfafa`    | 617 Valencia Castle           | Valencia     | 22                       | 2024: 10           |
| `fefec7`    | 202 Altinova                  | Mediah       | 27                       | old map: 12        |
| `ffc8ff`    | 229 Valencia City             | Valencia     | 28                       | old map: 2         |
| `560032`    | 1347 Atessahra                | Ulukita      | 30                       | 2024: 32           |
| `563c96`    | 1367 Neruda Plain             | Ulukita      | 29                       | 2024: 33           |
| `5600c8`    | 1350 Tungrad Ruins            | Ulukita      | 31                       | 2024: 34           |
| `561e70`    | 1381 Shakhtar Wilds           | Ulukita      | 33                       | 2024: 37           |
| `3ca032`    | 1559 Neftak Outpost           | Outer Edania | 35                       | 2024: 4            |
| `3c6464`    | 1563 Escar Mountains          | Outer Edania | 37                       | 2024: 7            |
| `3cf0d2`    | 1599 Crossroads of Defiance   | Outer Edania | 38                       | 2024: 3            |
| `3cb4f0`    | 1584 Azure Battlefield        | Outer Edania | 40                       | 2024: 2            |

## Field Names

The 2016 `gc::VillageSiegeInfo` holds `pa::Color _colorKey` (members `b`,
`g`, `r`, `a`) and `gc::KeyType<unsigned short> _regionKey`. The row is
the colour the table is keyed by, then the struct's own `_colorKey`
(`map_color_dup`, with `unknown_07` its `a` byte), then the region keys,
now a u32-counted list. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `villagesiegemap_2024.bmp.rid` lists 37 colours, and all 37
are `map_color` values of this file; the other four rows are the capitals
Velia, Heidel, Altinova and Valencia City, whose colours
`villagesiegemap.bmp.rid` lists. `villagesiegemap_2024.bmp` is the map
`fieldinfo.bss` names in `unknown_73` (`regionmapinfo.bss` key 12).
`region_keys` are `regioninfo.bss` keys: on client 3482 all 40 are regions
with a `max_participants` above `0`, the node war regions and the four
capitals.

The `VillageSiege_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 (`VillageSiegeKey`, `R`, `G`, `B`, `RegionKey`,
`RegionName`) holds 33 rows with up to six region keys each, while the
client 1784 file has 82 rows with one region each; the sheet does not
match the file and names no field here. `area_number` is named from
the grid that stores it; see Area Number.

## Area Number

`area_number` is the value the Node War grid
[`worldmapsiegeregionforconquest.bss`](worldmapgrid_bss.md) stores in
every cell of the area, so the grid joins each cell to its row here.
Each row's region was looked up at its `mapdata_realexplore2.bwp`
waypoint's cell:

| Client | Regions | Cell reads `area_number` | Capital, number not in the grid | Cell reads `0` | Cell reads another area |
| ------ | ------- | ------------------------ | ------------------------------- | -------------- | ----------------------- |
| 3482   | 40      | 30                       | 4 (`25` to `28`)                | 6              | 0                       |
| 1784   | 79      | 68                       | 3 (`79` to `81`)                | 6              | 2                       |

On both clients every value of the grid is the `area_number` of a row.
Client 1784 was checked with its own grid and the client 3482 region
waypoints; its capitals are Calpheon City (77), Altinova (202) and
Valencia City (229), and its numbers
`77` and `78` belong to rows without a region. On client 3482 the
numbers run territory by territory: `1` to `6` the Balenos nodes, `7`
to `12` Serendia, `13` to `18` Calpheon, `19` to `24` Valencia, `25` to
`28` the capitals Velia, Heidel, Altinova and Valencia City, `29` to
`34` Ulukita and `35` to `40` Outer Edania.

## Notes

- Layout 1 (clients 1348 to 2765) adds a u32 string-table index and a u32 that is
  always `0` around `area_number`, and its string table holds 27 Korean town
  names (`타리프 마을`, `벨리아 마을`, `알티노바`, ...). Layout 2 drops
  both and the strings.
- The `0d0d0d` row, first in the 2024 palette, has no region and
  `area_number` `0`, as the shared first-palette row of the
  other map colour tables.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `map_color` as `rrggbb`, the
  region keys with their names and `area_number`. The world map grid
  handler (`_bss/worldmapgrid/kinds.py`) reads this file to name the
  regions of each `worldmapsiegeregionforconquest.bss` cell value.

## Open Questions

### Capitals Outside the Grid

The four capital rows (`25` to `28` on client 3482) have an
`area_number`, but no cell of `worldmapsiegeregionforconquest.bss`
holds it. Which map draws the capital areas (the old
`villagesiegemap.bmp`, whose `.rid` lists their colours, is a lead) is
open.

### The Town Names of Client 1784

In Layout 1, `unknown_str_ref` points 82 rows at 27 town names. Which
town a node gets (the nearest town, its supply town or its tax town) is
open, and so is why Layout 2 dropped it.
