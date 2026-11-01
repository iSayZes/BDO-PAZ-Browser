# `oceansiegeinfo.bss` Format

## Purpose

The areas of the Blue Battlefield (ocean siege) region map, one row per
colour of `ui_texture/minimap/area/oceansiegemap.bmp`: the colour, a copy
of it, the islands (region keys) the area covers and the area number
that the [`worldmapoceansiegeregionforconquest.bss`](worldmapgrid_bss.md)
grid stores in its cells. The rows open like the 9-byte rows of
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md) and its siblings,
with a counted region list and the u16 area number in place of their
last u8.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records | Row bytes               |
| ------ | -------------- | -------------------- | ----- | ------- | ----------------------- |
| 1      | 2978 and later | `oceansiegeinfo.bss` | 480   | 29 Row  | 14 to 16, 16 on average |

| Layout | File                 | Known         | Unknown       |
| ------ | -------------------- | ------------- | ------------- |
| 1      | `oceansiegeinfo.bss` | 335 B (69.8%) | 145 B (30.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ba8be4ac6899`  |
| 3482   | Layout 1             | `ba8be4ac6899`  |
| 3474   | Layout 1             | `ba8be4ac6899`  |
| 3473   | Layout 1             | `ba8be4ac6899`  |
| 3464   | Layout 1             | `ba8be4ac6899`  |
| 3458   | Layout 1             | `ba8be4ac6899`  |
| 3454   | Layout 1             | `ba8be4ac6899`  |
| 3444   | Layout 1             | `ba8be4ac6899`  |
| 3435   | Layout 1             | `ba8be4ac6899`  |
| 3426   | Layout 1             | `ba8be4ac6899`  |
| 3418   | Layout 1             | `ba8be4ac6899`  |
| 3412   | Layout 1             | `ba8be4ac6899`  |
| 3402   | Layout 1             | `ba8be4ac6899`  |
| 3396   | Layout 1             | `ba8be4ac6899`  |
| 3387   | Layout 1             | `ba8be4ac6899`  |
| 3381   | Layout 1             | `ba8be4ac6899`  |
| 3373   | Layout 1             | `ba8be4ac6899`  |
| 3364   | Layout 1             | `ba8be4ac6899`  |
| 3356   | Layout 1             | `ba8be4ac6899`  |
| 3349   | Layout 1             | `ba8be4ac6899`  |
| 3342   | Layout 1             | `ba8be4ac6899`  |
| 3335   | Layout 1             | `ba8be4ac6899`  |
| 3326   | Layout 1             | `ba8be4ac6899`  |
| 3321   | Layout 1             | `ba8be4ac6899`  |
| 3314   | Layout 1             | `ba8be4ac6899`  |
| 3303   | Layout 1             | `ba8be4ac6899`  |
| 3302   | Layout 1             | `ba8be4ac6899`  |
| 3293   | Layout 1             | `ba8be4ac6899`  |
| 3283   | Layout 1             | `ba8be4ac6899`  |
| 3275   | Layout 1             | `ba8be4ac6899`  |
| 3267   | Layout 1             | `ba8be4ac6899`  |
| 3258   | Layout 1             | `ba8be4ac6899`  |
| 3251   | Layout 1             | `ba8be4ac6899`  |
| 3242   | Layout 1             | `ba8be4ac6899`  |
| 3235   | Layout 1             | `ba8be4ac6899`  |
| 3229   | Layout 1             | `ba8be4ac6899`  |
| 3212   | Layout 1             | `ba8be4ac6899`  |
| 3203   | Layout 1             | `ba8be4ac6899`  |
| 3193   | Layout 1             | `ba8be4ac6899`  |
| 3186   | Layout 1             | `ba8be4ac6899`  |
| 3177   | Layout 1             | `ba8be4ac6899`  |
| 3169   | Layout 1             | `ba8be4ac6899`  |
| 3158   | Layout 1             | `ba8be4ac6899`  |
| 3151   | Layout 1             | `ba8be4ac6899`  |
| 3144   | Layout 1             | `ba8be4ac6899`  |
| 3133   | Layout 1             | `ba8be4ac6899`  |
| 3125   | Layout 1             | `ba8be4ac6899`  |
| 3118   | Layout 1             | `ba8be4ac6899`  |
| 3111   | Layout 1             | `ba8be4ac6899`  |
| 3103   | Layout 1             | `ba8be4ac6899`  |
| 3095   | Layout 1             | `ba8be4ac6899`  |
| 3086   | Layout 1             | `ba8be4ac6899`  |
| 3072   | Layout 1             | `ba8be4ac6899`  |
| 3062   | Layout 1             | `ba8be4ac6899`  |
| 3052   | Layout 1             | `ba8be4ac6899`  |
| 3045   | Layout 1             | `ba8be4ac6899`  |
| 3037   | Layout 1             | `ba8be4ac6899`  |
| 3030   | Layout 1             | `ba8be4ac6899`  |
| 3021   | Layout 1             | `ba8be4ac6899`  |
| 3012   | Layout 1             | `ba8be4ac6899`  |
| 3002   | Layout 1             | `ba8be4ac6899`  |
| 2995   | Layout 1             | `ba8be4ac6899`  |
| 2987   | Layout 1             | `ba8be4ac6899`  |
| 2978   | Layout 1             | `ba8be4ac6899`  |
| 2970   | No documented layout | `ba8be4ac6899`  |
| 2959   | No file              | `ba8be4ac6899`  |
| 2951   | No file              | `ba8be4ac6899`  |
| 2942   | No file              | `ba8be4ac6899`  |
| 2935   | No file              | `ba8be4ac6899`  |
| 2932   | No file              | `ba8be4ac6899`  |
| 2923   | No file              | `ba8be4ac6899`  |
| 2919   | No file              | `ba8be4ac6899`  |
| 2907   | No file              | `ba8be4ac6899`  |
| 2900   | No file              | `ba8be4ac6899`  |
| 2891   | No file              | `ba8be4ac6899`  |
| 2882   | No file              | `ba8be4ac6899`  |
| 2872   | No file              | `ba8be4ac6899`  |
| 2863   | No file              | `ba8be4ac6899`  |
| 2855   | No file              | `ba8be4ac6899`  |
| 2849   | No file              | `ba8be4ac6899`  |
| 2844   | No file              | `ba8be4ac6899`  |
| 2834   | No file              | `ba8be4ac6899`  |
| 2825   | No file              | `ba8be4ac6899`  |
| 2819   | No file              | `ba8be4ac6899`  |
| 2811   | No file              | `ba8be4ac6899`  |
| 2803   | No file              | `ba8be4ac6899`  |
| 2794   | No file              | `ba8be4ac6899`  |
| 2783   | No file              | `ba8be4ac6899`  |
| 2774   | No file              | `ba8be4ac6899`  |
| 2765   | No file              | `ba8be4ac6899`  |
| 2756   | No file              | `ba8be4ac6899`  |
| 2750   | No file              | `ba8be4ac6899`  |
| 2743   | No file              | `ba8be4ac6899`  |
| 2736   | No file              | `ba8be4ac6899`  |
| 2726   | No file              | `ba8be4ac6899`  |
| 2717   | No file              | `ba8be4ac6899`  |
| 2709   | No file              | `ba8be4ac6899`  |
| 2703   | No file              | `ba8be4ac6899`  |
| 2695   | No file              | `ba8be4ac6899`  |
| 2684   | No file              | `ba8be4ac6899`  |
| 2672   | No file              | `ba8be4ac6899`  |
| 2665   | No file              | `ba8be4ac6899`  |
| 2657   | No file              | `ba8be4ac6899`  |
| 2649   | No file              | `ba8be4ac6899`  |
| 2644   | No file              | `ba8be4ac6899`  |
| 2637   | No file              | `ba8be4ac6899`  |
| 2629   | No file              | `ba8be4ac6899`  |
| 2619   | No file              | `ba8be4ac6899`  |
| 2612   | No file              | `ba8be4ac6899`  |
| 2606   | No file              | `ba8be4ac6899`  |
| 2602   | No file              | `ba8be4ac6899`  |
| 2601   | No file              | `ba8be4ac6899`  |
| 2592   | No file              | `ba8be4ac6899`  |
| 2583   | No file              | `ba8be4ac6899`  |
| 2575   | No file              | `ba8be4ac6899`  |
| 2567   | No file              | `ba8be4ac6899`  |
| 2560   | No file              | `ba8be4ac6899`  |
| 2553   | No file              | `ba8be4ac6899`  |
| 2545   | No file              | `ba8be4ac6899`  |
| 2538   | No file              | `ba8be4ac6899`  |
| 2529   | No file              | `ba8be4ac6899`  |
| 2519   | No file              | `ba8be4ac6899`  |
| 2513   | No file              | `ba8be4ac6899`  |
| 2510   | No file              | `ba8be4ac6899`  |
| 2507   | No file              | `ba8be4ac6899`  |
| 2503   | No file              | `ba8be4ac6899`  |
| 2498   | No file              | `ba8be4ac6899`  |
| 2492   | No file              | `ba8be4ac6899`  |
| 2487   | No file              | `ba8be4ac6899`  |
| 2480   | No file              | `ba8be4ac6899`  |
| 2474   | No file              | `ba8be4ac6899`  |
| 2468   | No file              | `ba8be4ac6899`  |
| 2460   | No file              | `ba8be4ac6899`  |
| 2453   | No file              | `ba8be4ac6899`  |
| 2444   | No file              | `ba8be4ac6899`  |
| 2438   | No file              | `ba8be4ac6899`  |
| 2434   | No file              | `ba8be4ac6899`  |
| 2429   | No file              | `ba8be4ac6899`  |
| 2421   | No file              | `ba8be4ac6899`  |
| 2414   | No file              | `ba8be4ac6899`  |
| 2407   | No file              | `ba8be4ac6899`  |
| 2401   | No file              | `ba8be4ac6899`  |
| 2397   | No file              | `ba8be4ac6899`  |
| 2393   | No file              | `ba8be4ac6899`  |
| 2384   | No file              | `ba8be4ac6899`  |
| 2378   | No file              | `ba8be4ac6899`  |
| 2372   | No file              | `ba8be4ac6899`  |
| 2358   | No file              | `ba8be4ac6899`  |
| 2352   | No file              | `ba8be4ac6899`  |
| 2347   | No file              | `ba8be4ac6899`  |
| 2343   | No file              | `ba8be4ac6899`  |
| 2335   | No file              | `ba8be4ac6899`  |
| 2327   | No file              | `ba8be4ac6899`  |
| 2324   | No file              | `ba8be4ac6899`  |
| 2319   | No file              | `ba8be4ac6899`  |
| 2313   | No file              | `ba8be4ac6899`  |
| 2308   | No file              | `ba8be4ac6899`  |
| 2302   | No file              | `ba8be4ac6899`  |
| 2295   | No file              | `ba8be4ac6899`  |
| 2290   | No file              | `ba8be4ac6899`  |
| 2284   | No file              | `ba8be4ac6899`  |
| 2276   | No file              | `ba8be4ac6899`  |
| 2269   | No file              | `ba8be4ac6899`  |
| 2259   | No file              | `ba8be4ac6899`  |
| 2250   | No file              | `ba8be4ac6899`  |
| 2243   | No file              | `ba8be4ac6899`  |
| 2235   | No file              | `ba8be4ac6899`  |
| 2229   | No file              | `ba8be4ac6899`  |
| 2224   | No file              | `ba8be4ac6899`  |
| 2218   | No file              | `ba8be4ac6899`  |
| 2215   | No file              | `ba8be4ac6899`  |
| 2207   | No file              | `ba8be4ac6899`  |
| 2203   | No file              | `ba8be4ac6899`  |
| 2196   | No file              | `ba8be4ac6899`  |
| 2192   | No file              | `ba8be4ac6899`  |
| 2189   | No file              | `ba8be4ac6899`  |
| 2183   | No file              | `ba8be4ac6899`  |
| 2179   | No file              | `ba8be4ac6899`  |
| 2171   | No file              | `ba8be4ac6899`  |
| 2163   | No file              | `ba8be4ac6899`  |
| 2156   | No file              | `ba8be4ac6899`  |
| 2151   | No file              | `ba8be4ac6899`  |
| 2147   | No file              | `ba8be4ac6899`  |
| 2142   | No file              | `ba8be4ac6899`  |
| 2138   | No file              | `ba8be4ac6899`  |
| 2134   | No file              | `ba8be4ac6899`  |
| 2130   | No file              | `ba8be4ac6899`  |
| 2122   | No file              | `ba8be4ac6899`  |
| 2107   | No file              | `ba8be4ac6899`  |
| 2098   | No file              | `ba8be4ac6899`  |
| 2089   | No file              | `ba8be4ac6899`  |
| 2081   | No file              | `ba8be4ac6899`  |
| 2073   | No file              | `ba8be4ac6899`  |
| 2067   | No file              | `ba8be4ac6899`  |
| 2063   | No file              | `ba8be4ac6899`  |
| 2059   | No file              | `ba8be4ac6899`  |
| 2052   | No file              | `ba8be4ac6899`  |
| 2044   | No file              | `ba8be4ac6899`  |
| 2039   | No file              | `ba8be4ac6899`  |
| 2032   | No file              | `ba8be4ac6899`  |
| 2025   | No file              | `ba8be4ac6899`  |
| 2011   | No file              | `ba8be4ac6899`  |
| 2005   | No file              | `ba8be4ac6899`  |
| 2000   | No file              | `ba8be4ac6899`  |
| 1996   | No file              | `ba8be4ac6899`  |
| 1991   | No file              | `ba8be4ac6899`  |
| 1985   | No file              | `ba8be4ac6899`  |
| 1980   | No file              | `ba8be4ac6899`  |
| 1969   | No file              | `ba8be4ac6899`  |
| 1964   | No file              | `ba8be4ac6899`  |
| 1958   | No file              | `ba8be4ac6899`  |
| 1950   | No file              | `ba8be4ac6899`  |
| 1945   | No file              | `ba8be4ac6899`  |
| 1937   | No file              | `ba8be4ac6899`  |
| 1933   | No file              | `ba8be4ac6899`  |
| 1927   | No file              | `ba8be4ac6899`  |
| 1921   | No file              | `ba8be4ac6899`  |
| 1914   | No file              | `ba8be4ac6899`  |
| 1908   | No file              | `ba8be4ac6899`  |
| 1897   | No file              | `ba8be4ac6899`  |
| 1892   | No file              | `ba8be4ac6899`  |
| 1886   | No file              | `ba8be4ac6899`  |
| 1881   | No file              | `ba8be4ac6899`  |
| 1871   | No file              | `ba8be4ac6899`  |
| 1866   | No file              | `ba8be4ac6899`  |
| 1862   | No file              | `ba8be4ac6899`  |
| 1854   | No file              | `ba8be4ac6899`  |
| 1846   | No file              | `ba8be4ac6899`  |
| 1838   | No file              | `ba8be4ac6899`  |
| 1832   | No file              | `ba8be4ac6899`  |
| 1826   | No file              | `ba8be4ac6899`  |
| 1822   | No file              | `ba8be4ac6899`  |
| 1818   | No file              | `ba8be4ac6899`  |
| 1804   | No file              | `ba8be4ac6899`  |
| 1794   | No file              | `ba8be4ac6899`  |
| 1790   | No file              | `ba8be4ac6899`  |
| 1784   | No file              | `ba8be4ac6899`  |
| 1774   | No file              | `ba8be4ac6899`  |
| 1771   | No file              | `ba8be4ac6899`  |
| 1762   | No file              | `ba8be4ac6899`  |
| 1759   | No file              | `ba8be4ac6899`  |
| 1754   | No file              | `ba8be4ac6899`  |
| 1749   | No file              | `ba8be4ac6899`  |
| 1743   | No file              | `ba8be4ac6899`  |
| 1737   | No file              | `ba8be4ac6899`  |
| 1731   | No file              | `ba8be4ac6899`  |
| 1725   | No file              | `ba8be4ac6899`  |
| 1717   | No file              | `ba8be4ac6899`  |
| 1710   | No file              | `ba8be4ac6899`  |
| 1704   | No file              | `ba8be4ac6899`  |
| 1698   | No file              | `ba8be4ac6899`  |
| 1690   | No file              | `ba8be4ac6899`  |
| 1685   | No file              | `ba8be4ac6899`  |
| 1680   | No file              | `ba8be4ac6899`  |
| 1674   | No file              | `ba8be4ac6899`  |
| 1668   | No file              | `ba8be4ac6899`  |
| 1659   | No file              | `ba8be4ac6899`  |
| 1649   | No file              | `ba8be4ac6899`  |
| 1642   | No file              | `ba8be4ac6899`  |
| 1636   | No file              | `ba8be4ac6899`  |
| 1628   | No file              | `ba8be4ac6899`  |
| 1622   | No file              | `ba8be4ac6899`  |
| 1614   | No file              | `ba8be4ac6899`  |
| 1608   | No file              | `ba8be4ac6899`  |
| 1602   | No file              | `ba8be4ac6899`  |
| 1598   | No file              | `ba8be4ac6899`  |
| 1594   | No file              | `ba8be4ac6899`  |
| 1590   | No file              | `ba8be4ac6899`  |
| 1587   | No file              | `ba8be4ac6899`  |
| 1584   | No file              | `ba8be4ac6899`  |
| 1579   | No file              | `ba8be4ac6899`  |
| 1572   | No file              | `ba8be4ac6899`  |
| 1565   | No file              | `ba8be4ac6899`  |
| 1559   | No file              | `ba8be4ac6899`  |
| 1554   | No file              | `ba8be4ac6899`  |
| 1547   | No file              | `ba8be4ac6899`  |
| 1537   | No file              | `ba8be4ac6899`  |
| 1529   | No file              | `ba8be4ac6899`  |
| 1524   | No file              | `ba8be4ac6899`  |
| 1519   | No file              | `ba8be4ac6899`  |
| 1509   | No file              | `ba8be4ac6899`  |
| 1506   | No file              | `ba8be4ac6899`  |
| 1504   | No file              | `ba8be4ac6899`  |
| 1500   | No file              | `ba8be4ac6899`  |
| 1493   | No file              | `ba8be4ac6899`  |
| 1489   | No file              | `ba8be4ac6899`  |
| 1485   | No file              | `ba8be4ac6899`  |
| 1481   | No file              | `ba8be4ac6899`  |
| 1474   | No file              | `ba8be4ac6899`  |
| 1466   | No file              | `ba8be4ac6899`  |
| 1462   | No file              | `ba8be4ac6899`  |
| 1459   | No file              | `ba8be4ac6899`  |
| 1453   | No file              | `ba8be4ac6899`  |
| 1450   | No file              | `ba8be4ac6899`  |
| 1445   | No file              | `ba8be4ac6899`  |
| 1439   | No file              | `ba8be4ac6899`  |
| 1433   | No file              | `ba8be4ac6899`  |
| 1430   | No file              | `ba8be4ac6899`  |
| 1426   | No file              | `ba8be4ac6899`  |
| 1421   | No file              | `ba8be4ac6899`  |
| 1417   | No file              | `ba8be4ac6899`  |
| 1416   | No file              | `ba8be4ac6899`  |
| 1409   | No file              | `ba8be4ac6899`  |
| 1405   | No file              | `ba8be4ac6899`  |
| 1401   | No file              | `ba8be4ac6899`  |
| 1396   | No file              | `ba8be4ac6899`  |
| 1391   | No file              | `ba8be4ac6899`  |
| 1390   | No file              | `ba8be4ac6899`  |
| 1386   | No file              | `ba8be4ac6899`  |
| 1381   | No file              | `ba8be4ac6899`  |
| 1379   | No file              | `ba8be4ac6899`  |
| 1372   | No file              | `ba8be4ac6899`  |
| 1366   | No file              | `ba8be4ac6899`  |
| 1364   | No file              | `ba8be4ac6899`  |
| 1363   | No file              | `ba8be4ac6899`  |
| 1360   | No file              | `ba8be4ac6899`  |
| 1358   | No file              | `ba8be4ac6899`  |
| 1355   | No file              | `ba8be4ac6899`  |
| 1351   | No file              | `ba8be4ac6899`  |
| 1348   | No file              | `ba8be4ac6899`  |
| 1346   | No file              | `ba8be4ac6899`  |
| 1341   | No file              | `ba8be4ac6899`  |
| 1340   | No file              | `ba8be4ac6899`  |
| 1338   | No file              | `ba8be4ac6899`  |
| 1335   | No file              | `ba8be4ac6899`  |
| 1333   | No file              | `ba8be4ac6899`  |
| 1329   | No file              | `ba8be4ac6899`  |
| 1327   | No file              | `ba8be4ac6899`  |
| 1324   | No file              | `ba8be4ac6899`  |
| 1321   | No file              | `ba8be4ac6899`  |
| 1319   | No file              | `ba8be4ac6899`  |
| 1318   | No file              | `ba8be4ac6899`  |
| 1316   | No file              | `ba8be4ac6899`  |
| 1313   | No file              | `ba8be4ac6899`  |
| 1311   | No file              | `ba8be4ac6899`  |
| 1309   | No file              | `ba8be4ac6899`  |
| 1304   | No file              | `ba8be4ac6899`  |
| 1292   | No file              | `ba8be4ac6899`  |
| 1286   | No file              | `ba8be4ac6899`  |
| 1280   | No file              | `ba8be4ac6899`  |
| 1276   | No file              | `ba8be4ac6899`  |
| 1267   | No file              | `ba8be4ac6899`  |
| 1261   | No file              | `ba8be4ac6899`  |
| 1256   | No file              | `ba8be4ac6899`  |
| 1250   | No file              | `ba8be4ac6899`  |
| 1246   | No file              | `ba8be4ac6899`  |
| 1239   | No file              | `ba8be4ac6899`  |
| 1230   | No file              | `ba8be4ac6899`  |
| 1226   | No file              | `ba8be4ac6899`  |
| 1220   | No file              | `ba8be4ac6899`  |
| 1217   | No file              | `ba8be4ac6899`  |
| 1211   | No file              | `ba8be4ac6899`  |
| 1210   | No file              | `ba8be4ac6899`  |
| 1208   | No file              | `ba8be4ac6899`  |
| 1203   | No file              | `ba8be4ac6899`  |
| 1197   | No file              | `ba8be4ac6899`  |
| 1194   | No file              | `ba8be4ac6899`  |
| 1192   | No file              | `ba8be4ac6899`  |
| 1187   | No file              | `ba8be4ac6899`  |
| 1183   | No file              | `ba8be4ac6899`  |
| 1177   | No file              | `ba8be4ac6899`  |
| 1173   | No file              | `ba8be4ac6899`  |
| 1167   | No file              | `ba8be4ac6899`  |
| 1164   | No file              | `ba8be4ac6899`  |
| 1156   | No file              | `ba8be4ac6899`  |
| 1149   | No file              | `ba8be4ac6899`  |
| 1144   | No file              | `ba8be4ac6899`  |
| 1137   | No file              | `ba8be4ac6899`  |
| 1132   | No file              | `ba8be4ac6899`  |
| 1127   | No file              | `ba8be4ac6899`  |
| 1122   | No file              | `ba8be4ac6899`  |
| 1118   | No file              | `ba8be4ac6899`  |
| 1114   | No file              | `ba8be4ac6899`  |
| 1109   | No file              | `ba8be4ac6899`  |
| 1102   | No file              | `ba8be4ac6899`  |
| 1096   | No file              | `ba8be4ac6899`  |
| 1088   | No file              | `ba8be4ac6899`  |
| 1081   | No file              | `ba8be4ac6899`  |
| 1076   | No file              | `ba8be4ac6899`  |
| 1069   | No file              | `ba8be4ac6899`  |
| 1064   | No file              | `ba8be4ac6899`  |
| 1058   | No file              | `ba8be4ac6899`  |
| 1051   | No file              | `ba8be4ac6899`  |
| 1044   | No file              | `ba8be4ac6899`  |
| 1036   | No file              | `ba8be4ac6899`  |
| 1026   | No file              | `ba8be4ac6899`  |
| 1016   | No file              | `ba8be4ac6899`  |
| 1009   | No file              | `ba8be4ac6899`  |
| 1005   | No file              | `ba8be4ac6899`  |
| 1000   | No file              | `ba8be4ac6899`  |
| 998    | No file              | `ba8be4ac6899`  |
| 990    | No file              | `ba8be4ac6899`  |
| 979    | No file              | `ba8be4ac6899`  |
| 972    | No file              | `ba8be4ac6899`  |
| 963    | No file              | `ba8be4ac6899`  |
| 955    | No file              | `ba8be4ac6899`  |
| 946    | No file              | `ba8be4ac6899`  |
| 938    | No file              | `ba8be4ac6899`  |
| 927    | No file              | `ba8be4ac6899`  |
| 911    | No file              | `ba8be4ac6899`  |
| 904    | No file              | `ba8be4ac6899`  |
| 899    | No file              | `ba8be4ac6899`  |
| 894    | No file              | `ba8be4ac6899`  |
| 885    | No file              | `ba8be4ac6899`  |
| 879    | No file              | `ba8be4ac6899`  |
| 872    | No file              | `ba8be4ac6899`  |
| 864    | No file              | `ba8be4ac6899`  |
| 855    | No file              | `ba8be4ac6899`  |
| 853    | No file              | `ba8be4ac6899`  |
| 845    | No file              | `ba8be4ac6899`  |
| 837    | No file              | `ba8be4ac6899`  |
| 829    | No file              | `ba8be4ac6899`  |
| 822    | No file              | `ba8be4ac6899`  |
| 814    | No file              | `ba8be4ac6899`  |
| 805    | No file              | `ba8be4ac6899`  |
| 794    | No file              | `ba8be4ac6899`  |
| 787    | No file              | `ba8be4ac6899`  |
| 780    | No file              | `ba8be4ac6899`  |
| 771    | No file              | `ba8be4ac6899`  |
| 760    | No file              | `ba8be4ac6899`  |
| 748    | No file              | `ba8be4ac6899`  |
| 741    | No file              | `ba8be4ac6899`  |
| 736    | No file              | `ba8be4ac6899`  |
| 731    | No file              | `ba8be4ac6899`  |
| 723    | No file              | `ba8be4ac6899`  |
| 711    | No file              | `ba8be4ac6899`  |
| 707    | No file              | `ba8be4ac6899`  |
| 697    | No file              | `ba8be4ac6899`  |
| 689    | No file              | `ba8be4ac6899`  |
| 683    | No file              | `ba8be4ac6899`  |
| 678    | No file              | `ba8be4ac6899`  |
| 670    | No file              | `ba8be4ac6899`  |
| 661    | No file              | `ba8be4ac6899`  |
| 656    | No file              | `ba8be4ac6899`  |
| 652    | No file              | `ba8be4ac6899`  |
| 643    | No file              | `ba8be4ac6899`  |
| 637    | No file              | `ba8be4ac6899`  |
| 630    | No file              | `ba8be4ac6899`  |
| 627    | No file              | `ba8be4ac6899`  |
| 621    | No file              | `ba8be4ac6899`  |
| 617    | No file              | `ba8be4ac6899`  |
| 615    | No file              | `ba8be4ac6899`  |
| 606    | No file              | `ba8be4ac6899`  |
| 599    | No file              | `ba8be4ac6899`  |
| 592    | No file              | `ba8be4ac6899`  |
| 586    | No file              | `ba8be4ac6899`  |
| 577    | No file              | `ba8be4ac6899`  |
| 569    | No file              | `ba8be4ac6899`  |
| 561    | No file              | `ba8be4ac6899`  |
| 554    | No file              | `ba8be4ac6899`  |
| 542    | No file              | `ba8be4ac6899`  |
| 532    | No file              | `ba8be4ac6899`  |
| 531    | No file              | `ba8be4ac6899`  |
| 526    | No file              | `ba8be4ac6899`  |
| 521    | No file              | `ba8be4ac6899`  |
| 517    | No file              | `ba8be4ac6899`  |
| 510    | No file              | `ba8be4ac6899`  |
| 508    | No file              | `ba8be4ac6899`  |
| 504    | No file              | `ba8be4ac6899`  |
| 497    | No file              | `ba8be4ac6899`  |
| 491    | No file              | `ba8be4ac6899`  |
| 485    | No file              | `ba8be4ac6899`  |
| 478    | No file              | `ba8be4ac6899`  |
| 472    | No file              | `ba8be4ac6899`  |
| 466    | No file              | `ba8be4ac6899`  |
| 457    | No file              | `ba8be4ac6899`  |
| 452    | No file              | `ba8be4ac6899`  |
| 449    | No file              | `ba8be4ac6899`  |
| 435    | No file              | `ba8be4ac6899`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names, LOC type 17, for the `region_keys` cell |

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

### Row (variable: 14 bytes + region keys)

| Offset             | Type                   | Field                  | Notes                                                                                   |
| ------------------ | ---------------------- | ---------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`            | bytes[3]               | map_color              | Region map colour, stored blue, green, red; unique per row. See Map Colours             |
| `+0x03`            | u8                     | unknown_03             | Always `0`                                                                              |
| `+0x04`            | bytes[3]               | unknown_04             | Equals `map_color` on every row                                                         |
| `+0x07`            | u8                     | unknown_07             | Always `0`                                                                              |
| `+0x08`            | u32                    | region_key_count       | Number of `region_keys`; `0` or `1` on every client checked                             |
| `+0x0C`            | u16[region_key_count]  | region_keys            | `regioninfo.bss` region keys, LOC type 17 names; each an island. See Map Colours         |
| `region_keys+0x00` | u16                    | area_number            | Cell value of `worldmapoceansiegeregionforconquest.bss` for this area; `0` to `28` on client 3482, unique per row. See Area Number |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`, the island,
its territory in `regioninfo.bss` and the area number. The `.rid`
position is the colour's place in `oceansiegemap.bmp.rid`.

| `map_color` | `region_keys`            | Territory | `area_number`            | Position in `.rid` |
| ----------- | ------------------------ | --------- | ------------------------ | ------------------ |
| `dd0b0b`    | 365 Balvege Island       | Balenos   | 7                        | 10                 |
| `100d10`    | none                     |           | 0                        | 1                  |
| `59d1c9`    | 394 Louruve Island       | Balenos   | 4                        | 13                 |
| `739bd7`    | none                     |           | 1                        | not listed         |
| `0f735f`    | 373 Invernen Island      | Balenos   | 2                        | 4                  |
| `9bb642`    | 392 Narvo Island         | Balenos   | 3                        | 2                  |
| `f6f340`    | 393 Marka Island         | Balenos   | 5                        | 12                 |
| `f06432`    | 407 Theonil Island       | Calpheon  | 26                       | 25                 |
| `1334b9`    | 366 Angie Island         | Balenos   | 6                        | 14                 |
| `617ac3`    | 364 Marlene Island       | Balenos   | 8                        | 7                  |
| `eea342`    | 367 Duch Island          | Balenos   | 9                        | 21                 |
| `61c3a9`    | 368 Eveto Island         | Balenos   | 10                       | 19                 |
| `c3b061`    | 371 Mariveno Island      | Balenos   | 11                       | 18                 |
| `ef4ccb`    | 369 Luivano Island       | Balenos   | 12                       | 22                 |
| `71c361`    | 377 Baremi Island        | Balenos   | 13                       | 5                  |
| `a661c3`    | 378 Weita Island         | Balenos   | 14                       | 11                 |
| `96c83c`    | 403 Albresser Island     | Calpheon  | 20                       | 20                 |
| `42ee7e`    | 379 Paratama Island      | Balenos   | 15                       | 15                 |
| `3c3834`    | 388 Al-Naha Island       | Balenos   | 16                       | 3                  |
| `aa321e`    | 566 Arita Island         | Calpheon  | 17                       | 6                  |
| `fabe64`    | 564 Padix Island         | Calpheon  | 18                       | 8                  |
| `1ec80a`    | 400 Oben Island          | Calpheon  | 21                       | 17                 |
| `fafa64`    | 565 Teste Island         | Calpheon  | 19                       | 9                  |
| `50fac8`    | 398 Daton Island         | Calpheon  | 22                       | 16                 |
| `0aaaf0`    | 396 Randis Island        | Calpheon  | 23                       | 26                 |
| `0a32f0`    | 405 Ginburrey Island     | Calpheon  | 24                       | 24                 |
| `c80af0`    | 409 Baeza Island         | Calpheon  | 25                       | 27                 |
| `f00aaa`    | 406 Rameda Island        | Calpheon  | 27                       | 23                 |
| `e62850`    | 410 Teyamal Island       | Calpheon  | 28                       | 28                 |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client has `Ocean` and `Siege` in its name. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `oceansiegemap.bmp.rid` lists 28 colours, and all 28 are
`map_color` values of this file, `10 0D 10` first. `region_keys` are
`regioninfo.bss` keys: all 27 are islands (region type Hunting, node war
day Friday), 15 in Balenos and 12 in Calpheon, the two territories of
`CppEnums.OceanSiegeTerritoryName` in `global_define_cpp_enum.luac`
(client 3482). `area_number` is named from the grid that stores it; see
Area Number.

## Area Number

`area_number` is the value the Blue Battlefield grid
[`worldmapoceansiegeregionforconquest.bss`](worldmapgrid_bss.md) stores
in every cell of the area (`255` outside the areas), so the grid joins
each cell to its row here. On client 3482 each island was looked up at
its `mapdata_realexplore2.bwp` waypoint's cell: the 15 Balenos islands
(`2` to `16`) read their row's `area_number`, and the 12 Calpheon islands
(`17` to `28`) read `255`, as the grid holds no number above `16`. Every
grid value other than `255` is the `area_number` of a row. The numbers
follow neither file order (`7, 0, 4, 1, 2, ...`) nor `.rid` order. The
client 3482 Lua walks the ocean siege territories with
`ToClient_GetOceanSiegeTerritoryByIndex(groupIdx, territory_idx)` and
reads no area number.

## Notes

- Clients 3002 and 3251 hold 17 rows (288 bytes): the `100d10` and
  `739bd7` rows and the 15 Balenos islands, each with the same values as on
  client 3482. Client 3482 adds the 12 Calpheon island rows.
- The `100d10` row, first in every region map palette, has no region and
  `area_number` `0`, as the shared `10 0D 10` row of the other
  map colour tables has `0`. The `739bd7` row has no region either and is
  the one colour the `.rid` does not list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/oceansiege_tables.py`: `map_color` as `rrggbb`, the
  region keys with their names and `area_number`. The world map grid
  handler (`_bss/worldmapgrid/kinds.py`) reads this file to name the
  islands of each `worldmapoceansiegeregionforconquest.bss` cell value.

## Open Questions

### Calpheon Islands Outside the Grid

On client 3482 the 12 Calpheon island rows have an `area_number` (`17`
to `28`), but no cell of `worldmapoceansiegeregionforconquest.bss` holds
one, and their waypoints read `255`. Whether a later client adds them to
the grid, or the map draws them from another source, is open.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, as in the 9-byte-row
tables, and `unknown_03` and `unknown_07` are always `0`. No source names
the copy.
