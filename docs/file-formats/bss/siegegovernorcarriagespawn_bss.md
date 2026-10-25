# `siegegovernorcarriagespawn.bss` Format

## Purpose

The Conquest War supply wagon spawns per territory: rows of the wagon's
character key, the territory key, a start time, an action index, a u32,
a maximum term and a list of spawn position indexes into
[`siegegovernorcarriagespawnposition.bss`](siegegovernorcarriagespawnposition_bss.md).
On client 3482 the three rows are Calpheon, Mediah and Valencia, each
with the Military Supply Wagon (`59670`) and three positions.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | ------- | --------- |
| 1      | 1743 and later | `siegegovernorcarriagespawn.bss` | 152   | 3 Row   | 44        |

| Layout | File                             | Known         | Unknown     |
| ------ | -------------------------------- | ------------- | ----------- |
| 1      | `siegegovernorcarriagespawn.bss` | 140 B (92.1%) | 12 B (7.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `63b5cd3972bf`  |
| 3482   | Layout 1 | `63b5cd3972bf`  |
| 3474   | Layout 1 | `63b5cd3972bf`  |
| 3473   | Layout 1 | `63b5cd3972bf`  |
| 3464   | Layout 1 | `63b5cd3972bf`  |
| 3458   | Layout 1 | `63b5cd3972bf`  |
| 3454   | Layout 1 | `63b5cd3972bf`  |
| 3444   | Layout 1 | `63b5cd3972bf`  |
| 3435   | Layout 1 | `63b5cd3972bf`  |
| 3426   | Layout 1 | `63b5cd3972bf`  |
| 3418   | Layout 1 | `63b5cd3972bf`  |
| 3412   | Layout 1 | `63b5cd3972bf`  |
| 3402   | Layout 1 | `63b5cd3972bf`  |
| 3396   | Layout 1 | `63b5cd3972bf`  |
| 3387   | Layout 1 | `63b5cd3972bf`  |
| 3381   | Layout 1 | `63b5cd3972bf`  |
| 3373   | Layout 1 | `63b5cd3972bf`  |
| 3364   | Layout 1 | `63b5cd3972bf`  |
| 3356   | Layout 1 | `63b5cd3972bf`  |
| 3349   | Layout 1 | `63b5cd3972bf`  |
| 3342   | Layout 1 | `63b5cd3972bf`  |
| 3335   | Layout 1 | `63b5cd3972bf`  |
| 3326   | Layout 1 | `63b5cd3972bf`  |
| 3321   | Layout 1 | `63b5cd3972bf`  |
| 3314   | Layout 1 | `63b5cd3972bf`  |
| 3303   | Layout 1 | `63b5cd3972bf`  |
| 3302   | Layout 1 | `63b5cd3972bf`  |
| 3293   | Layout 1 | `63b5cd3972bf`  |
| 3283   | Layout 1 | `63b5cd3972bf`  |
| 3275   | Layout 1 | `63b5cd3972bf`  |
| 3267   | Layout 1 | `63b5cd3972bf`  |
| 3258   | Layout 1 | `63b5cd3972bf`  |
| 3251   | Layout 1 | `63b5cd3972bf`  |
| 3242   | Layout 1 | `63b5cd3972bf`  |
| 3235   | Layout 1 | `63b5cd3972bf`  |
| 3229   | Layout 1 | `63b5cd3972bf`  |
| 3212   | Layout 1 | `63b5cd3972bf`  |
| 3203   | Layout 1 | `63b5cd3972bf`  |
| 3193   | Layout 1 | `63b5cd3972bf`  |
| 3186   | Layout 1 | `63b5cd3972bf`  |
| 3177   | Layout 1 | `63b5cd3972bf`  |
| 3169   | Layout 1 | `63b5cd3972bf`  |
| 3158   | Layout 1 | `63b5cd3972bf`  |
| 3151   | Layout 1 | `63b5cd3972bf`  |
| 3144   | Layout 1 | `63b5cd3972bf`  |
| 3133   | Layout 1 | `63b5cd3972bf`  |
| 3125   | Layout 1 | `63b5cd3972bf`  |
| 3118   | Layout 1 | `63b5cd3972bf`  |
| 3111   | Layout 1 | `63b5cd3972bf`  |
| 3103   | Layout 1 | `63b5cd3972bf`  |
| 3095   | Layout 1 | `63b5cd3972bf`  |
| 3086   | Layout 1 | `63b5cd3972bf`  |
| 3072   | Layout 1 | `63b5cd3972bf`  |
| 3062   | Layout 1 | `63b5cd3972bf`  |
| 3052   | Layout 1 | `63b5cd3972bf`  |
| 3045   | Layout 1 | `63b5cd3972bf`  |
| 3037   | Layout 1 | `63b5cd3972bf`  |
| 3030   | Layout 1 | `63b5cd3972bf`  |
| 3021   | Layout 1 | `63b5cd3972bf`  |
| 3012   | Layout 1 | `63b5cd3972bf`  |
| 3002   | Layout 1 | `63b5cd3972bf`  |
| 2995   | Layout 1 | `63b5cd3972bf`  |
| 2987   | Layout 1 | `63b5cd3972bf`  |
| 2978   | Layout 1 | `63b5cd3972bf`  |
| 2970   | Layout 1 | `63b5cd3972bf`  |
| 2959   | Layout 1 | `63b5cd3972bf`  |
| 2951   | Layout 1 | `63b5cd3972bf`  |
| 2942   | Layout 1 | `63b5cd3972bf`  |
| 2935   | Layout 1 | `63b5cd3972bf`  |
| 2932   | Layout 1 | `63b5cd3972bf`  |
| 2923   | Layout 1 | `63b5cd3972bf`  |
| 2919   | Layout 1 | `63b5cd3972bf`  |
| 2907   | Layout 1 | `63b5cd3972bf`  |
| 2900   | Layout 1 | `63b5cd3972bf`  |
| 2891   | Layout 1 | `63b5cd3972bf`  |
| 2882   | Layout 1 | `63b5cd3972bf`  |
| 2872   | Layout 1 | `63b5cd3972bf`  |
| 2863   | Layout 1 | `63b5cd3972bf`  |
| 2855   | Layout 1 | `63b5cd3972bf`  |
| 2849   | Layout 1 | `63b5cd3972bf`  |
| 2844   | Layout 1 | `63b5cd3972bf`  |
| 2834   | Layout 1 | `63b5cd3972bf`  |
| 2825   | Layout 1 | `63b5cd3972bf`  |
| 2819   | Layout 1 | `63b5cd3972bf`  |
| 2811   | Layout 1 | `63b5cd3972bf`  |
| 2803   | Layout 1 | `63b5cd3972bf`  |
| 2794   | Layout 1 | `63b5cd3972bf`  |
| 2783   | Layout 1 | `63b5cd3972bf`  |
| 2774   | Layout 1 | `63b5cd3972bf`  |
| 2765   | Layout 1 | `63b5cd3972bf`  |
| 2756   | Layout 1 | `63b5cd3972bf`  |
| 2750   | Layout 1 | `63b5cd3972bf`  |
| 2743   | Layout 1 | `63b5cd3972bf`  |
| 2736   | Layout 1 | `63b5cd3972bf`  |
| 2726   | Layout 1 | `63b5cd3972bf`  |
| 2717   | Layout 1 | `63b5cd3972bf`  |
| 2709   | Layout 1 | `63b5cd3972bf`  |
| 2703   | Layout 1 | `63b5cd3972bf`  |
| 2695   | Layout 1 | `63b5cd3972bf`  |
| 2684   | Layout 1 | `63b5cd3972bf`  |
| 2672   | Layout 1 | `63b5cd3972bf`  |
| 2665   | Layout 1 | `63b5cd3972bf`  |
| 2657   | Layout 1 | `63b5cd3972bf`  |
| 2649   | Layout 1 | `63b5cd3972bf`  |
| 2644   | Layout 1 | `63b5cd3972bf`  |
| 2637   | Layout 1 | `63b5cd3972bf`  |
| 2629   | Layout 1 | `63b5cd3972bf`  |
| 2619   | Layout 1 | `63b5cd3972bf`  |
| 2612   | Layout 1 | `63b5cd3972bf`  |
| 2606   | Layout 1 | `63b5cd3972bf`  |
| 2602   | Layout 1 | `63b5cd3972bf`  |
| 2601   | Layout 1 | `63b5cd3972bf`  |
| 2592   | Layout 1 | `63b5cd3972bf`  |
| 2583   | Layout 1 | `63b5cd3972bf`  |
| 2575   | Layout 1 | `63b5cd3972bf`  |
| 2567   | Layout 1 | `63b5cd3972bf`  |
| 2560   | Layout 1 | `63b5cd3972bf`  |
| 2553   | Layout 1 | `63b5cd3972bf`  |
| 2545   | Layout 1 | `63b5cd3972bf`  |
| 2538   | Layout 1 | `63b5cd3972bf`  |
| 2529   | Layout 1 | `63b5cd3972bf`  |
| 2519   | Layout 1 | `63b5cd3972bf`  |
| 2513   | Layout 1 | `63b5cd3972bf`  |
| 2510   | Layout 1 | `63b5cd3972bf`  |
| 2507   | Layout 1 | `63b5cd3972bf`  |
| 2503   | Layout 1 | `63b5cd3972bf`  |
| 2498   | Layout 1 | `63b5cd3972bf`  |
| 2492   | Layout 1 | `63b5cd3972bf`  |
| 2487   | Layout 1 | `63b5cd3972bf`  |
| 2480   | Layout 1 | `63b5cd3972bf`  |
| 2474   | Layout 1 | `63b5cd3972bf`  |
| 2468   | Layout 1 | `63b5cd3972bf`  |
| 2460   | Layout 1 | `63b5cd3972bf`  |
| 2453   | Layout 1 | `63b5cd3972bf`  |
| 2444   | Layout 1 | `63b5cd3972bf`  |
| 2438   | Layout 1 | `63b5cd3972bf`  |
| 2434   | Layout 1 | `63b5cd3972bf`  |
| 2429   | Layout 1 | `63b5cd3972bf`  |
| 2421   | Layout 1 | `63b5cd3972bf`  |
| 2414   | Layout 1 | `63b5cd3972bf`  |
| 2407   | Layout 1 | `63b5cd3972bf`  |
| 2401   | Layout 1 | `63b5cd3972bf`  |
| 2397   | Layout 1 | `63b5cd3972bf`  |
| 2393   | Layout 1 | `63b5cd3972bf`  |
| 2384   | Layout 1 | `63b5cd3972bf`  |
| 2378   | Layout 1 | `63b5cd3972bf`  |
| 2372   | Layout 1 | `63b5cd3972bf`  |
| 2358   | Layout 1 | `63b5cd3972bf`  |
| 2352   | Layout 1 | `63b5cd3972bf`  |
| 2347   | Layout 1 | `63b5cd3972bf`  |
| 2343   | Layout 1 | `63b5cd3972bf`  |
| 2335   | Layout 1 | `63b5cd3972bf`  |
| 2327   | Layout 1 | `63b5cd3972bf`  |
| 2324   | Layout 1 | `63b5cd3972bf`  |
| 2319   | Layout 1 | `63b5cd3972bf`  |
| 2313   | Layout 1 | `63b5cd3972bf`  |
| 2308   | Layout 1 | `63b5cd3972bf`  |
| 2302   | Layout 1 | `63b5cd3972bf`  |
| 2295   | Layout 1 | `63b5cd3972bf`  |
| 2290   | Layout 1 | `63b5cd3972bf`  |
| 2284   | Layout 1 | `63b5cd3972bf`  |
| 2276   | Layout 1 | `63b5cd3972bf`  |
| 2269   | Layout 1 | `63b5cd3972bf`  |
| 2259   | Layout 1 | `63b5cd3972bf`  |
| 2250   | Layout 1 | `63b5cd3972bf`  |
| 2243   | Layout 1 | `63b5cd3972bf`  |
| 2235   | Layout 1 | `63b5cd3972bf`  |
| 2229   | Layout 1 | `63b5cd3972bf`  |
| 2224   | Layout 1 | `63b5cd3972bf`  |
| 2218   | Layout 1 | `63b5cd3972bf`  |
| 2215   | Layout 1 | `63b5cd3972bf`  |
| 2207   | Layout 1 | `63b5cd3972bf`  |
| 2203   | Layout 1 | `63b5cd3972bf`  |
| 2196   | Layout 1 | `63b5cd3972bf`  |
| 2192   | Layout 1 | `63b5cd3972bf`  |
| 2189   | Layout 1 | `63b5cd3972bf`  |
| 2183   | Layout 1 | `63b5cd3972bf`  |
| 2179   | Layout 1 | `63b5cd3972bf`  |
| 2171   | Layout 1 | `63b5cd3972bf`  |
| 2163   | Layout 1 | `63b5cd3972bf`  |
| 2156   | Layout 1 | `63b5cd3972bf`  |
| 2151   | Layout 1 | `63b5cd3972bf`  |
| 2147   | Layout 1 | `63b5cd3972bf`  |
| 2142   | Layout 1 | `63b5cd3972bf`  |
| 2138   | Layout 1 | `63b5cd3972bf`  |
| 2134   | Layout 1 | `63b5cd3972bf`  |
| 2130   | Layout 1 | `63b5cd3972bf`  |
| 2122   | Layout 1 | `63b5cd3972bf`  |
| 2107   | Layout 1 | `63b5cd3972bf`  |
| 2098   | Layout 1 | `63b5cd3972bf`  |
| 2089   | Layout 1 | `63b5cd3972bf`  |
| 2081   | Layout 1 | `63b5cd3972bf`  |
| 2073   | Layout 1 | `63b5cd3972bf`  |
| 2067   | Layout 1 | `63b5cd3972bf`  |
| 2063   | Layout 1 | `63b5cd3972bf`  |
| 2059   | Layout 1 | `63b5cd3972bf`  |
| 2052   | Layout 1 | `63b5cd3972bf`  |
| 2044   | Layout 1 | `63b5cd3972bf`  |
| 2039   | Layout 1 | `63b5cd3972bf`  |
| 2032   | Layout 1 | `63b5cd3972bf`  |
| 2025   | Layout 1 | `63b5cd3972bf`  |
| 2011   | Layout 1 | `63b5cd3972bf`  |
| 2005   | Layout 1 | `63b5cd3972bf`  |
| 2000   | Layout 1 | `63b5cd3972bf`  |
| 1996   | Layout 1 | `63b5cd3972bf`  |
| 1991   | Layout 1 | `63b5cd3972bf`  |
| 1985   | Layout 1 | `63b5cd3972bf`  |
| 1980   | Layout 1 | `63b5cd3972bf`  |
| 1969   | Layout 1 | `63b5cd3972bf`  |
| 1964   | Layout 1 | `63b5cd3972bf`  |
| 1958   | Layout 1 | `63b5cd3972bf`  |
| 1950   | Layout 1 | `63b5cd3972bf`  |
| 1945   | Layout 1 | `63b5cd3972bf`  |
| 1937   | Layout 1 | `63b5cd3972bf`  |
| 1933   | Layout 1 | `63b5cd3972bf`  |
| 1927   | Layout 1 | `63b5cd3972bf`  |
| 1921   | Layout 1 | `63b5cd3972bf`  |
| 1914   | Layout 1 | `63b5cd3972bf`  |
| 1908   | Layout 1 | `63b5cd3972bf`  |
| 1897   | Layout 1 | `63b5cd3972bf`  |
| 1892   | Layout 1 | `63b5cd3972bf`  |
| 1886   | Layout 1 | `63b5cd3972bf`  |
| 1881   | Layout 1 | `63b5cd3972bf`  |
| 1871   | Layout 1 | `63b5cd3972bf`  |
| 1866   | Layout 1 | `63b5cd3972bf`  |
| 1862   | Layout 1 | `63b5cd3972bf`  |
| 1854   | Layout 1 | `63b5cd3972bf`  |
| 1846   | Layout 1 | `63b5cd3972bf`  |
| 1838   | Layout 1 | `63b5cd3972bf`  |
| 1832   | Layout 1 | `63b5cd3972bf`  |
| 1826   | Layout 1 | `63b5cd3972bf`  |
| 1822   | Layout 1 | `63b5cd3972bf`  |
| 1818   | Layout 1 | `63b5cd3972bf`  |
| 1804   | Layout 1 | `63b5cd3972bf`  |
| 1794   | Layout 1 | `63b5cd3972bf`  |
| 1790   | Layout 1 | `63b5cd3972bf`  |
| 1784   | Layout 1 | `63b5cd3972bf`  |
| 1774   | Layout 1 | `63b5cd3972bf`  |
| 1771   | Layout 1 | `63b5cd3972bf`  |
| 1762   | Layout 1 | `63b5cd3972bf`  |
| 1759   | Layout 1 | `63b5cd3972bf`  |
| 1754   | Layout 1 | `63b5cd3972bf`  |
| 1749   | Layout 1 | `63b5cd3972bf`  |
| 1743   | Layout 1 | `63b5cd3972bf`  |
| 1737   | No file  | `63b5cd3972bf`  |
| 1731   | No file  | `63b5cd3972bf`  |
| 1725   | No file  | `63b5cd3972bf`  |
| 1717   | No file  | `63b5cd3972bf`  |
| 1710   | No file  | `63b5cd3972bf`  |
| 1704   | No file  | `63b5cd3972bf`  |
| 1698   | No file  | `63b5cd3972bf`  |
| 1690   | No file  | `63b5cd3972bf`  |
| 1685   | No file  | `63b5cd3972bf`  |
| 1680   | No file  | `63b5cd3972bf`  |
| 1674   | No file  | `63b5cd3972bf`  |
| 1668   | No file  | `63b5cd3972bf`  |
| 1659   | No file  | `63b5cd3972bf`  |
| 1649   | No file  | `63b5cd3972bf`  |
| 1642   | No file  | `63b5cd3972bf`  |
| 1636   | No file  | `63b5cd3972bf`  |
| 1628   | No file  | `63b5cd3972bf`  |
| 1622   | No file  | `63b5cd3972bf`  |
| 1614   | No file  | `63b5cd3972bf`  |
| 1608   | No file  | `63b5cd3972bf`  |
| 1602   | No file  | `63b5cd3972bf`  |
| 1598   | No file  | `63b5cd3972bf`  |
| 1594   | No file  | `63b5cd3972bf`  |
| 1590   | No file  | `63b5cd3972bf`  |
| 1587   | No file  | `63b5cd3972bf`  |
| 1584   | No file  | `63b5cd3972bf`  |
| 1579   | No file  | `63b5cd3972bf`  |
| 1572   | No file  | `63b5cd3972bf`  |
| 1565   | No file  | `63b5cd3972bf`  |
| 1559   | No file  | `63b5cd3972bf`  |
| 1554   | No file  | `63b5cd3972bf`  |
| 1547   | No file  | `63b5cd3972bf`  |
| 1537   | No file  | `63b5cd3972bf`  |
| 1529   | No file  | `63b5cd3972bf`  |
| 1524   | No file  | `63b5cd3972bf`  |
| 1519   | No file  | `63b5cd3972bf`  |
| 1509   | No file  | `63b5cd3972bf`  |
| 1506   | No file  | `63b5cd3972bf`  |
| 1504   | No file  | `63b5cd3972bf`  |
| 1500   | No file  | `63b5cd3972bf`  |
| 1493   | No file  | `63b5cd3972bf`  |
| 1489   | No file  | `63b5cd3972bf`  |
| 1485   | No file  | `63b5cd3972bf`  |
| 1481   | No file  | `63b5cd3972bf`  |
| 1474   | No file  | `63b5cd3972bf`  |
| 1466   | No file  | `63b5cd3972bf`  |
| 1462   | No file  | `63b5cd3972bf`  |
| 1459   | No file  | `63b5cd3972bf`  |
| 1453   | No file  | `63b5cd3972bf`  |
| 1450   | No file  | `63b5cd3972bf`  |
| 1445   | No file  | `63b5cd3972bf`  |
| 1439   | No file  | `63b5cd3972bf`  |
| 1433   | No file  | `63b5cd3972bf`  |
| 1430   | No file  | `63b5cd3972bf`  |
| 1426   | No file  | `63b5cd3972bf`  |
| 1421   | No file  | `63b5cd3972bf`  |
| 1417   | No file  | `63b5cd3972bf`  |
| 1416   | No file  | `63b5cd3972bf`  |
| 1409   | No file  | `63b5cd3972bf`  |
| 1405   | No file  | `63b5cd3972bf`  |
| 1401   | No file  | `63b5cd3972bf`  |
| 1396   | No file  | `63b5cd3972bf`  |
| 1391   | No file  | `63b5cd3972bf`  |
| 1390   | No file  | `63b5cd3972bf`  |
| 1386   | No file  | `63b5cd3972bf`  |
| 1381   | No file  | `63b5cd3972bf`  |
| 1379   | No file  | `63b5cd3972bf`  |
| 1372   | No file  | `63b5cd3972bf`  |
| 1366   | No file  | `63b5cd3972bf`  |
| 1364   | No file  | `63b5cd3972bf`  |
| 1363   | No file  | `63b5cd3972bf`  |
| 1360   | No file  | `63b5cd3972bf`  |
| 1358   | No file  | `63b5cd3972bf`  |
| 1355   | No file  | `63b5cd3972bf`  |
| 1351   | No file  | `63b5cd3972bf`  |
| 1348   | No file  | `63b5cd3972bf`  |
| 1346   | No file  | `63b5cd3972bf`  |
| 1341   | No file  | `63b5cd3972bf`  |
| 1340   | No file  | `63b5cd3972bf`  |
| 1338   | No file  | `63b5cd3972bf`  |
| 1335   | No file  | `63b5cd3972bf`  |
| 1333   | No file  | `63b5cd3972bf`  |
| 1329   | No file  | `63b5cd3972bf`  |
| 1327   | No file  | `63b5cd3972bf`  |
| 1324   | No file  | `63b5cd3972bf`  |
| 1321   | No file  | `63b5cd3972bf`  |
| 1319   | No file  | `63b5cd3972bf`  |
| 1318   | No file  | `63b5cd3972bf`  |
| 1316   | No file  | `63b5cd3972bf`  |
| 1313   | No file  | `63b5cd3972bf`  |
| 1311   | No file  | `63b5cd3972bf`  |
| 1309   | No file  | `63b5cd3972bf`  |
| 1304   | No file  | `63b5cd3972bf`  |
| 1292   | No file  | `63b5cd3972bf`  |
| 1286   | No file  | `63b5cd3972bf`  |
| 1280   | No file  | `63b5cd3972bf`  |
| 1276   | No file  | `63b5cd3972bf`  |
| 1267   | No file  | `63b5cd3972bf`  |
| 1261   | No file  | `63b5cd3972bf`  |
| 1256   | No file  | `63b5cd3972bf`  |
| 1250   | No file  | `63b5cd3972bf`  |
| 1246   | No file  | `63b5cd3972bf`  |
| 1239   | No file  | `63b5cd3972bf`  |
| 1230   | No file  | `63b5cd3972bf`  |
| 1226   | No file  | `63b5cd3972bf`  |
| 1220   | No file  | `63b5cd3972bf`  |
| 1217   | No file  | `63b5cd3972bf`  |
| 1211   | No file  | `63b5cd3972bf`  |
| 1210   | No file  | `63b5cd3972bf`  |
| 1208   | No file  | `63b5cd3972bf`  |
| 1203   | No file  | `63b5cd3972bf`  |
| 1197   | No file  | `63b5cd3972bf`  |
| 1194   | No file  | `63b5cd3972bf`  |
| 1192   | No file  | `63b5cd3972bf`  |
| 1187   | No file  | `63b5cd3972bf`  |
| 1183   | No file  | `63b5cd3972bf`  |
| 1177   | No file  | `63b5cd3972bf`  |
| 1173   | No file  | `63b5cd3972bf`  |
| 1167   | No file  | `63b5cd3972bf`  |
| 1164   | No file  | `63b5cd3972bf`  |
| 1156   | No file  | `63b5cd3972bf`  |
| 1149   | No file  | `63b5cd3972bf`  |
| 1144   | No file  | `63b5cd3972bf`  |
| 1137   | No file  | `63b5cd3972bf`  |
| 1132   | No file  | `63b5cd3972bf`  |
| 1127   | No file  | `63b5cd3972bf`  |
| 1122   | No file  | `63b5cd3972bf`  |
| 1118   | No file  | `63b5cd3972bf`  |
| 1114   | No file  | `63b5cd3972bf`  |
| 1109   | No file  | `63b5cd3972bf`  |
| 1102   | No file  | `63b5cd3972bf`  |
| 1096   | No file  | `63b5cd3972bf`  |
| 1088   | No file  | `63b5cd3972bf`  |
| 1081   | No file  | `63b5cd3972bf`  |
| 1076   | No file  | `63b5cd3972bf`  |
| 1069   | No file  | `63b5cd3972bf`  |
| 1064   | No file  | `63b5cd3972bf`  |
| 1058   | No file  | `63b5cd3972bf`  |
| 1051   | No file  | `63b5cd3972bf`  |
| 1044   | No file  | `63b5cd3972bf`  |
| 1036   | No file  | `63b5cd3972bf`  |
| 1026   | No file  | `63b5cd3972bf`  |
| 1016   | No file  | `63b5cd3972bf`  |
| 1009   | No file  | `63b5cd3972bf`  |
| 1005   | No file  | `63b5cd3972bf`  |
| 1000   | No file  | `63b5cd3972bf`  |
| 998    | No file  | `63b5cd3972bf`  |
| 990    | No file  | `63b5cd3972bf`  |
| 979    | No file  | `63b5cd3972bf`  |
| 972    | No file  | `63b5cd3972bf`  |
| 963    | No file  | `63b5cd3972bf`  |
| 955    | No file  | `63b5cd3972bf`  |
| 946    | No file  | `63b5cd3972bf`  |
| 938    | No file  | `63b5cd3972bf`  |
| 927    | No file  | `63b5cd3972bf`  |
| 911    | No file  | `63b5cd3972bf`  |
| 904    | No file  | `63b5cd3972bf`  |
| 899    | No file  | `63b5cd3972bf`  |
| 894    | No file  | `63b5cd3972bf`  |
| 885    | No file  | `63b5cd3972bf`  |
| 879    | No file  | `63b5cd3972bf`  |
| 872    | No file  | `63b5cd3972bf`  |
| 864    | No file  | `63b5cd3972bf`  |
| 855    | No file  | `63b5cd3972bf`  |
| 853    | No file  | `63b5cd3972bf`  |
| 845    | No file  | `63b5cd3972bf`  |
| 837    | No file  | `63b5cd3972bf`  |
| 829    | No file  | `63b5cd3972bf`  |
| 822    | No file  | `63b5cd3972bf`  |
| 814    | No file  | `63b5cd3972bf`  |
| 805    | No file  | `63b5cd3972bf`  |
| 794    | No file  | `63b5cd3972bf`  |
| 787    | No file  | `63b5cd3972bf`  |
| 780    | No file  | `63b5cd3972bf`  |
| 771    | No file  | `63b5cd3972bf`  |
| 760    | No file  | `63b5cd3972bf`  |
| 748    | No file  | `63b5cd3972bf`  |
| 741    | No file  | `63b5cd3972bf`  |
| 736    | No file  | `63b5cd3972bf`  |
| 731    | No file  | `63b5cd3972bf`  |
| 723    | No file  | `63b5cd3972bf`  |
| 711    | No file  | `63b5cd3972bf`  |
| 707    | No file  | `63b5cd3972bf`  |
| 697    | No file  | `63b5cd3972bf`  |
| 689    | No file  | `63b5cd3972bf`  |
| 683    | No file  | `63b5cd3972bf`  |
| 678    | No file  | `63b5cd3972bf`  |
| 670    | No file  | `63b5cd3972bf`  |
| 661    | No file  | `63b5cd3972bf`  |
| 656    | No file  | `63b5cd3972bf`  |
| 652    | No file  | `63b5cd3972bf`  |
| 643    | No file  | `63b5cd3972bf`  |
| 637    | No file  | `63b5cd3972bf`  |
| 630    | No file  | `63b5cd3972bf`  |
| 627    | No file  | `63b5cd3972bf`  |
| 621    | No file  | `63b5cd3972bf`  |
| 617    | No file  | `63b5cd3972bf`  |
| 615    | No file  | `63b5cd3972bf`  |
| 606    | No file  | `63b5cd3972bf`  |
| 599    | No file  | `63b5cd3972bf`  |
| 592    | No file  | `63b5cd3972bf`  |
| 586    | No file  | `63b5cd3972bf`  |
| 577    | No file  | `63b5cd3972bf`  |
| 569    | No file  | `63b5cd3972bf`  |
| 561    | No file  | `63b5cd3972bf`  |
| 554    | No file  | `63b5cd3972bf`  |
| 542    | No file  | `63b5cd3972bf`  |
| 532    | No file  | `63b5cd3972bf`  |
| 531    | No file  | `63b5cd3972bf`  |
| 526    | No file  | `63b5cd3972bf`  |
| 521    | No file  | `63b5cd3972bf`  |
| 517    | No file  | `63b5cd3972bf`  |
| 510    | No file  | `63b5cd3972bf`  |
| 508    | No file  | `63b5cd3972bf`  |
| 504    | No file  | `63b5cd3972bf`  |
| 497    | No file  | `63b5cd3972bf`  |
| 491    | No file  | `63b5cd3972bf`  |
| 485    | No file  | `63b5cd3972bf`  |
| 478    | No file  | `63b5cd3972bf`  |
| 472    | No file  | `63b5cd3972bf`  |
| 466    | No file  | `63b5cd3972bf`  |
| 457    | No file  | `63b5cd3972bf`  |
| 452    | No file  | `63b5cd3972bf`  |
| 449    | No file  | `63b5cd3972bf`  |
| 435    | No file  | `63b5cd3972bf`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | Character names (LOC type 6) and territory names (LOC type 12) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients that ship the file empty |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 32 bytes + positions)

| Offset  | Type                          | Field                     | Notes                                                                 |
| ------- | ----------------------------- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16                           | character_key             | `characterstatic.dbss` key of the wagon; `59670` on every row         |
| `+0x02` | u16                           | territory_key             | `territoryinfo.bss` key (LOC type 12); one row each                   |
| `+0x04` | u64                           | start_time                | `1800` on every row of client 3482                                    |
| `+0x0C` | u32                           | action_index              | `0`, `1`, `2`: the row's place in file order                          |
| `+0x10` | u32                           | unknown_10                | `1` on every row of client 3482                                       |
| `+0x14` | u64                           | max_term                  | `3600` on every row of client 3482                                    |
| `+0x1C` | u32                           | spawn_position_count      | Number of spawn positions; `3` on every row of client 3482            |
| `+0x20` | u32[spawn_position_count]     | spawn_position_list       | `index` values of `siegegovernorcarriagespawnposition.bss`            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order. Every row has `character_key` `59670`
(Military Supply Wagon), `start_time` `1800`, `unknown_10` `1` and
`max_term` `3600`.

| `territory_key` | Territory | `action_index` | `spawn_position_list` |
| --------------- | --------- | -------------- | --------------------- |
| 2               | Calpheon  | 0              | 0, 1, 2               |
| 3               | Mediah    | 1              | 3, 4, 5               |
| 4               | Valencia  | 2              | 6, 7, 8               |

## Field Names

The `MajorSiegeTankSpawn` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `MajorSiegeRegion`, `CharacterKey`,
`ActionIndex`, `StartTime`, `MaxTerm` and `IndexPosition` and three rows.
Client 1784 ships the file empty, so the sheet is checked against client
3482: `CharacterKey` (`59670`), `MajorSiegeRegion` (`2`, `3`, `4`),
`ActionIndex` (`0`, `1`, `2`), `MaxTerm` (`3600`) and `IndexPosition`
(`0,1,2`, `3,4,5`, `6,7,8`) match all three rows; `StartTime` is `7200`
in the sheet and `1800` in the file. That server's dump (client 1784)
names the members `MajorSiegeTankSpawnStaticStatus _territoryKey`,
`_characterKey`, `_startTime` and `_spawnPositionList`. The u64 at
`+0x04` is the only field left for `StartTime`; `start_time` and the
other names follow the members, `action_index` and `max_term` the sheet.
The server calls the wagon a tank (`MajorSiegeTank`); the client file
name calls it the governor's carriage.

## Notes

- Clients 1784 to 2765 ship the file with `row_count` `0`; client 3002
  and later hold the three rows.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the territory with its name first, then the wagon with its name and the
  other fields.

## Open Questions

### The u32 After the Action Index

`unknown_10` is `1` on every row of client 3482 and has no sheet column on
client 1784.

### The Units of start_time and max_term

The Pearl Abyss console notice
([board 13255](https://blackdesert.pearlabyss.com/Console/en-us/News/Notice/Detail?_boardNo=13255))
says the Military Supply Wagon spawns at a random time between 1 hour and
1 hour 30 minutes after the start of the Conquest War. In seconds, that is
`max_term` `3600` plus up to `start_time` `1800`. Which field is the fixed
delay and which the random window, and whether the PC client uses the same
times, is not confirmed.
