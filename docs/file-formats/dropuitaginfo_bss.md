# `dropuitaginfo.bss` Format

## Purpose

The tags of the drop item window hunting grounds: one fixed row per tag with
its Korean name and tooltip, the Dehkia's Lantern guide image and the tag's
background and text colours.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) lists the
tag keys of each zone (`tag_keys`). LOC type 117 names the tags by key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes  | Records    | Row bytes |
| ------ | -------------- | ------------------- | ------ | ---------- | --------- |
| 1      | 2290 and later | `dropuitaginfo.bss` | 13,190 | 45 Tag Row | 32        |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `dropuitaginfo.bss` | 13,190 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `8a393a7ed24b`  |
| 3482   | Layout 1             | `8a393a7ed24b`  |
| 3474   | Layout 1             | `8a393a7ed24b`  |
| 3473   | Layout 1             | `8a393a7ed24b`  |
| 3464   | Layout 1             | `8a393a7ed24b`  |
| 3458   | Layout 1             | `8a393a7ed24b`  |
| 3454   | Layout 1             | `8a393a7ed24b`  |
| 3444   | Layout 1             | `8a393a7ed24b`  |
| 3435   | Layout 1             | `8a393a7ed24b`  |
| 3426   | Layout 1             | `8a393a7ed24b`  |
| 3418   | Layout 1             | `8a393a7ed24b`  |
| 3412   | Layout 1             | `8a393a7ed24b`  |
| 3402   | Layout 1             | `8a393a7ed24b`  |
| 3396   | Layout 1             | `8a393a7ed24b`  |
| 3387   | Layout 1             | `8a393a7ed24b`  |
| 3381   | Layout 1             | `8a393a7ed24b`  |
| 3373   | Layout 1             | `8a393a7ed24b`  |
| 3364   | Layout 1             | `8a393a7ed24b`  |
| 3356   | Layout 1             | `8a393a7ed24b`  |
| 3349   | Layout 1             | `8a393a7ed24b`  |
| 3342   | Layout 1             | `8a393a7ed24b`  |
| 3335   | Layout 1             | `8a393a7ed24b`  |
| 3326   | Layout 1             | `8a393a7ed24b`  |
| 3321   | Layout 1             | `8a393a7ed24b`  |
| 3314   | Layout 1             | `8a393a7ed24b`  |
| 3303   | Layout 1             | `8a393a7ed24b`  |
| 3302   | Layout 1             | `8a393a7ed24b`  |
| 3293   | Layout 1             | `8a393a7ed24b`  |
| 3283   | Layout 1             | `8a393a7ed24b`  |
| 3275   | Layout 1             | `8a393a7ed24b`  |
| 3267   | Layout 1             | `8a393a7ed24b`  |
| 3258   | Layout 1             | `8a393a7ed24b`  |
| 3251   | Layout 1             | `8a393a7ed24b`  |
| 3242   | Layout 1             | `8a393a7ed24b`  |
| 3235   | Layout 1             | `8a393a7ed24b`  |
| 3229   | Layout 1             | `8a393a7ed24b`  |
| 3212   | Layout 1             | `8a393a7ed24b`  |
| 3203   | Layout 1             | `8a393a7ed24b`  |
| 3193   | Layout 1             | `8a393a7ed24b`  |
| 3186   | Layout 1             | `8a393a7ed24b`  |
| 3177   | Layout 1             | `8a393a7ed24b`  |
| 3169   | Layout 1             | `8a393a7ed24b`  |
| 3158   | Layout 1             | `8a393a7ed24b`  |
| 3151   | Layout 1             | `8a393a7ed24b`  |
| 3144   | Layout 1             | `8a393a7ed24b`  |
| 3133   | Layout 1             | `8a393a7ed24b`  |
| 3125   | Layout 1             | `8a393a7ed24b`  |
| 3118   | Layout 1             | `8a393a7ed24b`  |
| 3111   | Layout 1             | `8a393a7ed24b`  |
| 3103   | Layout 1             | `8a393a7ed24b`  |
| 3095   | Layout 1             | `8a393a7ed24b`  |
| 3086   | Layout 1             | `8a393a7ed24b`  |
| 3072   | Layout 1             | `8a393a7ed24b`  |
| 3062   | Layout 1             | `8a393a7ed24b`  |
| 3052   | Layout 1             | `8a393a7ed24b`  |
| 3045   | Layout 1             | `8a393a7ed24b`  |
| 3037   | Layout 1             | `8a393a7ed24b`  |
| 3030   | Layout 1             | `8a393a7ed24b`  |
| 3021   | Layout 1             | `8a393a7ed24b`  |
| 3012   | Layout 1             | `8a393a7ed24b`  |
| 3002   | Layout 1             | `8a393a7ed24b`  |
| 2995   | Layout 1             | `8a393a7ed24b`  |
| 2987   | Layout 1             | `8a393a7ed24b`  |
| 2978   | Layout 1             | `8a393a7ed24b`  |
| 2970   | Layout 1             | `8a393a7ed24b`  |
| 2959   | Layout 1             | `8a393a7ed24b`  |
| 2951   | Layout 1             | `8a393a7ed24b`  |
| 2942   | Layout 1             | `8a393a7ed24b`  |
| 2935   | Layout 1             | `8a393a7ed24b`  |
| 2932   | Layout 1             | `8a393a7ed24b`  |
| 2923   | Layout 1             | `8a393a7ed24b`  |
| 2919   | Layout 1             | `8a393a7ed24b`  |
| 2907   | Layout 1             | `8a393a7ed24b`  |
| 2900   | Layout 1             | `8a393a7ed24b`  |
| 2891   | Layout 1             | `8a393a7ed24b`  |
| 2882   | Layout 1             | `8a393a7ed24b`  |
| 2872   | Layout 1             | `8a393a7ed24b`  |
| 2863   | Layout 1             | `8a393a7ed24b`  |
| 2855   | Layout 1             | `8a393a7ed24b`  |
| 2849   | Layout 1             | `8a393a7ed24b`  |
| 2844   | Layout 1             | `8a393a7ed24b`  |
| 2834   | Layout 1             | `8a393a7ed24b`  |
| 2825   | Layout 1             | `8a393a7ed24b`  |
| 2819   | Layout 1             | `8a393a7ed24b`  |
| 2811   | Layout 1             | `8a393a7ed24b`  |
| 2803   | Layout 1             | `8a393a7ed24b`  |
| 2794   | Layout 1             | `8a393a7ed24b`  |
| 2783   | Layout 1             | `8a393a7ed24b`  |
| 2774   | Layout 1             | `8a393a7ed24b`  |
| 2765   | Layout 1             | `8a393a7ed24b`  |
| 2756   | Layout 1             | `8a393a7ed24b`  |
| 2750   | Layout 1             | `8a393a7ed24b`  |
| 2743   | Layout 1             | `8a393a7ed24b`  |
| 2736   | Layout 1             | `8a393a7ed24b`  |
| 2726   | Layout 1             | `8a393a7ed24b`  |
| 2717   | Layout 1             | `8a393a7ed24b`  |
| 2709   | Layout 1             | `8a393a7ed24b`  |
| 2703   | Layout 1             | `8a393a7ed24b`  |
| 2695   | Layout 1             | `8a393a7ed24b`  |
| 2684   | Layout 1             | `8a393a7ed24b`  |
| 2672   | Layout 1             | `8a393a7ed24b`  |
| 2665   | Layout 1             | `8a393a7ed24b`  |
| 2657   | Layout 1             | `8a393a7ed24b`  |
| 2649   | Layout 1             | `8a393a7ed24b`  |
| 2644   | Layout 1             | `8a393a7ed24b`  |
| 2637   | Layout 1             | `8a393a7ed24b`  |
| 2629   | Layout 1             | `8a393a7ed24b`  |
| 2619   | Layout 1             | `8a393a7ed24b`  |
| 2612   | Layout 1             | `8a393a7ed24b`  |
| 2606   | Layout 1             | `8a393a7ed24b`  |
| 2602   | Layout 1             | `8a393a7ed24b`  |
| 2601   | Layout 1             | `8a393a7ed24b`  |
| 2592   | Layout 1             | `8a393a7ed24b`  |
| 2583   | Layout 1             | `8a393a7ed24b`  |
| 2575   | Layout 1             | `8a393a7ed24b`  |
| 2567   | Layout 1             | `8a393a7ed24b`  |
| 2560   | Layout 1             | `8a393a7ed24b`  |
| 2553   | Layout 1             | `8a393a7ed24b`  |
| 2545   | Layout 1             | `8a393a7ed24b`  |
| 2538   | Layout 1             | `8a393a7ed24b`  |
| 2529   | Layout 1             | `8a393a7ed24b`  |
| 2519   | Layout 1             | `8a393a7ed24b`  |
| 2513   | Layout 1             | `8a393a7ed24b`  |
| 2510   | Layout 1             | `8a393a7ed24b`  |
| 2507   | Layout 1             | `8a393a7ed24b`  |
| 2503   | Layout 1             | `8a393a7ed24b`  |
| 2498   | Layout 1             | `8a393a7ed24b`  |
| 2492   | Layout 1             | `8a393a7ed24b`  |
| 2487   | Layout 1             | `8a393a7ed24b`  |
| 2480   | Layout 1             | `8a393a7ed24b`  |
| 2474   | Layout 1             | `8a393a7ed24b`  |
| 2468   | Layout 1             | `8a393a7ed24b`  |
| 2460   | Layout 1             | `8a393a7ed24b`  |
| 2453   | Layout 1             | `8a393a7ed24b`  |
| 2444   | Layout 1             | `8a393a7ed24b`  |
| 2438   | Layout 1             | `8a393a7ed24b`  |
| 2434   | Layout 1             | `8a393a7ed24b`  |
| 2429   | Layout 1             | `8a393a7ed24b`  |
| 2421   | Layout 1             | `8a393a7ed24b`  |
| 2414   | Layout 1             | `8a393a7ed24b`  |
| 2407   | Layout 1             | `8a393a7ed24b`  |
| 2401   | Layout 1             | `8a393a7ed24b`  |
| 2397   | Layout 1             | `8a393a7ed24b`  |
| 2393   | Layout 1             | `8a393a7ed24b`  |
| 2384   | Layout 1             | `8a393a7ed24b`  |
| 2378   | Layout 1             | `8a393a7ed24b`  |
| 2372   | Layout 1             | `8a393a7ed24b`  |
| 2358   | Layout 1             | `8a393a7ed24b`  |
| 2352   | Layout 1             | `8a393a7ed24b`  |
| 2347   | Layout 1             | `8a393a7ed24b`  |
| 2343   | Layout 1             | `8a393a7ed24b`  |
| 2335   | Layout 1             | `8a393a7ed24b`  |
| 2327   | Layout 1             | `8a393a7ed24b`  |
| 2324   | Layout 1             | `8a393a7ed24b`  |
| 2319   | Layout 1             | `8a393a7ed24b`  |
| 2313   | Layout 1             | `8a393a7ed24b`  |
| 2308   | Layout 1             | `8a393a7ed24b`  |
| 2302   | Layout 1             | `8a393a7ed24b`  |
| 2295   | Layout 1             | `8a393a7ed24b`  |
| 2290   | Layout 1             | `8a393a7ed24b`  |
| 2284   | No documented layout | `8a393a7ed24b`  |
| 2276   | No documented layout | `8a393a7ed24b`  |
| 2269   | No documented layout | `8a393a7ed24b`  |
| 2259   | No documented layout | `8a393a7ed24b`  |
| 2250   | No documented layout | `8a393a7ed24b`  |
| 2243   | No documented layout | `8a393a7ed24b`  |
| 2235   | No documented layout | `8a393a7ed24b`  |
| 2229   | No documented layout | `8a393a7ed24b`  |
| 2224   | No documented layout | `8a393a7ed24b`  |
| 2218   | No documented layout | `8a393a7ed24b`  |
| 2215   | No documented layout | `8a393a7ed24b`  |
| 2207   | No documented layout | `8a393a7ed24b`  |
| 2203   | No documented layout | `8a393a7ed24b`  |
| 2196   | No documented layout | `8a393a7ed24b`  |
| 2192   | No documented layout | `8a393a7ed24b`  |
| 2189   | No documented layout | `8a393a7ed24b`  |
| 2183   | No documented layout | `8a393a7ed24b`  |
| 2179   | No documented layout | `8a393a7ed24b`  |
| 2171   | No documented layout | `8a393a7ed24b`  |
| 2163   | No documented layout | `8a393a7ed24b`  |
| 2156   | No documented layout | `8a393a7ed24b`  |
| 2151   | No documented layout | `8a393a7ed24b`  |
| 2147   | No documented layout | `8a393a7ed24b`  |
| 2142   | No documented layout | `8a393a7ed24b`  |
| 2138   | No documented layout | `8a393a7ed24b`  |
| 2134   | No documented layout | `8a393a7ed24b`  |
| 2130   | No documented layout | `8a393a7ed24b`  |
| 2122   | No documented layout | `8a393a7ed24b`  |
| 2107   | No documented layout | `8a393a7ed24b`  |
| 2098   | No documented layout | `8a393a7ed24b`  |
| 2089   | No documented layout | `8a393a7ed24b`  |
| 2081   | No documented layout | `8a393a7ed24b`  |
| 2073   | No documented layout | `8a393a7ed24b`  |
| 2067   | No documented layout | `8a393a7ed24b`  |
| 2063   | No documented layout | `8a393a7ed24b`  |
| 2059   | No documented layout | `8a393a7ed24b`  |
| 2052   | No documented layout | `8a393a7ed24b`  |
| 2044   | No documented layout | `8a393a7ed24b`  |
| 2039   | No documented layout | `8a393a7ed24b`  |
| 2032   | No documented layout | `8a393a7ed24b`  |
| 2025   | No documented layout | `8a393a7ed24b`  |
| 2011   | No documented layout | `8a393a7ed24b`  |
| 2005   | No documented layout | `8a393a7ed24b`  |
| 2000   | No documented layout | `8a393a7ed24b`  |
| 1996   | No documented layout | `8a393a7ed24b`  |
| 1991   | No documented layout | `8a393a7ed24b`  |
| 1985   | No documented layout | `8a393a7ed24b`  |
| 1980   | No documented layout | `8a393a7ed24b`  |
| 1969   | No documented layout | `8a393a7ed24b`  |
| 1964   | No documented layout | `8a393a7ed24b`  |
| 1958   | No documented layout | `8a393a7ed24b`  |
| 1950   | No documented layout | `8a393a7ed24b`  |
| 1945   | No documented layout | `8a393a7ed24b`  |
| 1937   | No documented layout | `8a393a7ed24b`  |
| 1933   | No documented layout | `8a393a7ed24b`  |
| 1927   | No documented layout | `8a393a7ed24b`  |
| 1921   | No documented layout | `8a393a7ed24b`  |
| 1914   | No documented layout | `8a393a7ed24b`  |
| 1908   | No file              | `8a393a7ed24b`  |
| 1897   | No file              | `8a393a7ed24b`  |
| 1892   | No file              | `8a393a7ed24b`  |
| 1886   | No file              | `8a393a7ed24b`  |
| 1881   | No file              | `8a393a7ed24b`  |
| 1871   | No file              | `8a393a7ed24b`  |
| 1866   | No file              | `8a393a7ed24b`  |
| 1862   | No file              | `8a393a7ed24b`  |
| 1854   | No file              | `8a393a7ed24b`  |
| 1846   | No file              | `8a393a7ed24b`  |
| 1838   | No file              | `8a393a7ed24b`  |
| 1832   | No file              | `8a393a7ed24b`  |
| 1826   | No file              | `8a393a7ed24b`  |
| 1822   | No file              | `8a393a7ed24b`  |
| 1818   | No file              | `8a393a7ed24b`  |
| 1804   | No file              | `8a393a7ed24b`  |
| 1794   | No file              | `8a393a7ed24b`  |
| 1790   | No file              | `8a393a7ed24b`  |
| 1784   | No file              | `8a393a7ed24b`  |
| 1774   | No file              | `8a393a7ed24b`  |
| 1771   | No file              | `8a393a7ed24b`  |
| 1762   | No file              | `8a393a7ed24b`  |
| 1759   | No file              | `8a393a7ed24b`  |
| 1754   | No file              | `8a393a7ed24b`  |
| 1749   | No file              | `8a393a7ed24b`  |
| 1743   | No file              | `8a393a7ed24b`  |
| 1737   | No file              | `8a393a7ed24b`  |
| 1731   | No file              | `8a393a7ed24b`  |
| 1725   | No file              | `8a393a7ed24b`  |
| 1717   | No file              | `8a393a7ed24b`  |
| 1710   | No file              | `8a393a7ed24b`  |
| 1704   | No file              | `8a393a7ed24b`  |
| 1698   | No file              | `8a393a7ed24b`  |
| 1690   | No file              | `8a393a7ed24b`  |
| 1685   | No file              | `8a393a7ed24b`  |
| 1680   | No file              | `8a393a7ed24b`  |
| 1674   | No file              | `8a393a7ed24b`  |
| 1668   | No file              | `8a393a7ed24b`  |
| 1659   | No file              | `8a393a7ed24b`  |
| 1649   | No file              | `8a393a7ed24b`  |
| 1642   | No file              | `8a393a7ed24b`  |
| 1636   | No file              | `8a393a7ed24b`  |
| 1628   | No file              | `8a393a7ed24b`  |
| 1622   | No file              | `8a393a7ed24b`  |
| 1614   | No file              | `8a393a7ed24b`  |
| 1608   | No file              | `8a393a7ed24b`  |
| 1602   | No file              | `8a393a7ed24b`  |
| 1598   | No file              | `8a393a7ed24b`  |
| 1594   | No file              | `8a393a7ed24b`  |
| 1590   | No file              | `8a393a7ed24b`  |
| 1587   | No file              | `8a393a7ed24b`  |
| 1584   | No file              | `8a393a7ed24b`  |
| 1579   | No file              | `8a393a7ed24b`  |
| 1572   | No file              | `8a393a7ed24b`  |
| 1565   | No file              | `8a393a7ed24b`  |
| 1559   | No file              | `8a393a7ed24b`  |
| 1554   | No file              | `8a393a7ed24b`  |
| 1547   | No file              | `8a393a7ed24b`  |
| 1537   | No file              | `8a393a7ed24b`  |
| 1529   | No file              | `8a393a7ed24b`  |
| 1524   | No file              | `8a393a7ed24b`  |
| 1519   | No file              | `8a393a7ed24b`  |
| 1509   | No file              | `8a393a7ed24b`  |
| 1506   | No file              | `8a393a7ed24b`  |
| 1504   | No file              | `8a393a7ed24b`  |
| 1500   | No file              | `8a393a7ed24b`  |
| 1493   | No file              | `8a393a7ed24b`  |
| 1489   | No file              | `8a393a7ed24b`  |
| 1485   | No file              | `8a393a7ed24b`  |
| 1481   | No file              | `8a393a7ed24b`  |
| 1474   | No file              | `8a393a7ed24b`  |
| 1466   | No file              | `8a393a7ed24b`  |
| 1462   | No file              | `8a393a7ed24b`  |
| 1459   | No file              | `8a393a7ed24b`  |
| 1453   | No file              | `8a393a7ed24b`  |
| 1450   | No file              | `8a393a7ed24b`  |
| 1445   | No file              | `8a393a7ed24b`  |
| 1439   | No file              | `8a393a7ed24b`  |
| 1433   | No file              | `8a393a7ed24b`  |
| 1430   | No file              | `8a393a7ed24b`  |
| 1426   | No file              | `8a393a7ed24b`  |
| 1421   | No file              | `8a393a7ed24b`  |
| 1417   | No file              | `8a393a7ed24b`  |
| 1416   | No file              | `8a393a7ed24b`  |
| 1409   | No file              | `8a393a7ed24b`  |
| 1405   | No file              | `8a393a7ed24b`  |
| 1401   | No file              | `8a393a7ed24b`  |
| 1396   | No file              | `8a393a7ed24b`  |
| 1391   | No file              | `8a393a7ed24b`  |
| 1390   | No file              | `8a393a7ed24b`  |
| 1386   | No file              | `8a393a7ed24b`  |
| 1381   | No file              | `8a393a7ed24b`  |
| 1379   | No file              | `8a393a7ed24b`  |
| 1372   | No file              | `8a393a7ed24b`  |
| 1366   | No file              | `8a393a7ed24b`  |
| 1364   | No file              | `8a393a7ed24b`  |
| 1363   | No file              | `8a393a7ed24b`  |
| 1360   | No file              | `8a393a7ed24b`  |
| 1358   | No file              | `8a393a7ed24b`  |
| 1355   | No file              | `8a393a7ed24b`  |
| 1351   | No file              | `8a393a7ed24b`  |
| 1348   | No file              | `8a393a7ed24b`  |
| 1346   | No file              | `8a393a7ed24b`  |
| 1341   | No file              | `8a393a7ed24b`  |
| 1340   | No file              | `8a393a7ed24b`  |
| 1338   | No file              | `8a393a7ed24b`  |
| 1335   | No file              | `8a393a7ed24b`  |
| 1333   | No file              | `8a393a7ed24b`  |
| 1329   | No file              | `8a393a7ed24b`  |
| 1327   | No file              | `8a393a7ed24b`  |
| 1324   | No file              | `8a393a7ed24b`  |
| 1321   | No file              | `8a393a7ed24b`  |
| 1319   | No file              | `8a393a7ed24b`  |
| 1318   | No file              | `8a393a7ed24b`  |
| 1316   | No file              | `8a393a7ed24b`  |
| 1313   | No file              | `8a393a7ed24b`  |
| 1311   | No file              | `8a393a7ed24b`  |
| 1309   | No file              | `8a393a7ed24b`  |
| 1304   | No file              | `8a393a7ed24b`  |
| 1292   | No file              | `8a393a7ed24b`  |
| 1286   | No file              | `8a393a7ed24b`  |
| 1280   | No file              | `8a393a7ed24b`  |
| 1276   | No file              | `8a393a7ed24b`  |
| 1267   | No file              | `8a393a7ed24b`  |
| 1261   | No file              | `8a393a7ed24b`  |
| 1256   | No file              | `8a393a7ed24b`  |
| 1250   | No file              | `8a393a7ed24b`  |
| 1246   | No file              | `8a393a7ed24b`  |
| 1239   | No file              | `8a393a7ed24b`  |
| 1230   | No file              | `8a393a7ed24b`  |
| 1226   | No file              | `8a393a7ed24b`  |
| 1220   | No file              | `8a393a7ed24b`  |
| 1217   | No file              | `8a393a7ed24b`  |
| 1211   | No file              | `8a393a7ed24b`  |
| 1210   | No file              | `8a393a7ed24b`  |
| 1208   | No file              | `8a393a7ed24b`  |
| 1203   | No file              | `8a393a7ed24b`  |
| 1197   | No file              | `8a393a7ed24b`  |
| 1194   | No file              | `8a393a7ed24b`  |
| 1192   | No file              | `8a393a7ed24b`  |
| 1187   | No file              | `8a393a7ed24b`  |
| 1183   | No file              | `8a393a7ed24b`  |
| 1177   | No file              | `8a393a7ed24b`  |
| 1173   | No file              | `8a393a7ed24b`  |
| 1167   | No file              | `8a393a7ed24b`  |
| 1164   | No file              | `8a393a7ed24b`  |
| 1156   | No file              | `8a393a7ed24b`  |
| 1149   | No file              | `8a393a7ed24b`  |
| 1144   | No file              | `8a393a7ed24b`  |
| 1137   | No file              | `8a393a7ed24b`  |
| 1132   | No file              | `8a393a7ed24b`  |
| 1127   | No file              | `8a393a7ed24b`  |
| 1122   | No file              | `8a393a7ed24b`  |
| 1118   | No file              | `8a393a7ed24b`  |
| 1114   | No file              | `8a393a7ed24b`  |
| 1109   | No file              | `8a393a7ed24b`  |
| 1102   | No file              | `8a393a7ed24b`  |
| 1096   | No file              | `8a393a7ed24b`  |
| 1088   | No file              | `8a393a7ed24b`  |
| 1081   | No file              | `8a393a7ed24b`  |
| 1076   | No file              | `8a393a7ed24b`  |
| 1069   | No file              | `8a393a7ed24b`  |
| 1064   | No file              | `8a393a7ed24b`  |
| 1058   | No file              | `8a393a7ed24b`  |
| 1051   | No file              | `8a393a7ed24b`  |
| 1044   | No file              | `8a393a7ed24b`  |
| 1036   | No file              | `8a393a7ed24b`  |
| 1026   | No file              | `8a393a7ed24b`  |
| 1016   | No file              | `8a393a7ed24b`  |
| 1009   | No file              | `8a393a7ed24b`  |
| 1005   | No file              | `8a393a7ed24b`  |
| 1000   | No file              | `8a393a7ed24b`  |
| 998    | No file              | `8a393a7ed24b`  |
| 990    | No file              | `8a393a7ed24b`  |
| 979    | No file              | `8a393a7ed24b`  |
| 972    | No file              | `8a393a7ed24b`  |
| 963    | No file              | `8a393a7ed24b`  |
| 955    | No file              | `8a393a7ed24b`  |
| 946    | No file              | `8a393a7ed24b`  |
| 938    | No file              | `8a393a7ed24b`  |
| 927    | No file              | `8a393a7ed24b`  |
| 911    | No file              | `8a393a7ed24b`  |
| 904    | No file              | `8a393a7ed24b`  |
| 899    | No file              | `8a393a7ed24b`  |
| 894    | No file              | `8a393a7ed24b`  |
| 885    | No file              | `8a393a7ed24b`  |
| 879    | No file              | `8a393a7ed24b`  |
| 872    | No file              | `8a393a7ed24b`  |
| 864    | No file              | `8a393a7ed24b`  |
| 855    | No file              | `8a393a7ed24b`  |
| 853    | No file              | `8a393a7ed24b`  |
| 845    | No file              | `8a393a7ed24b`  |
| 837    | No file              | `8a393a7ed24b`  |
| 829    | No file              | `8a393a7ed24b`  |
| 822    | No file              | `8a393a7ed24b`  |
| 814    | No file              | `8a393a7ed24b`  |
| 805    | No file              | `8a393a7ed24b`  |
| 794    | No file              | `8a393a7ed24b`  |
| 787    | No file              | `8a393a7ed24b`  |
| 780    | No file              | `8a393a7ed24b`  |
| 771    | No file              | `8a393a7ed24b`  |
| 760    | No file              | `8a393a7ed24b`  |
| 748    | No file              | `8a393a7ed24b`  |
| 741    | No file              | `8a393a7ed24b`  |
| 736    | No file              | `8a393a7ed24b`  |
| 731    | No file              | `8a393a7ed24b`  |
| 723    | No file              | `8a393a7ed24b`  |
| 711    | No file              | `8a393a7ed24b`  |
| 707    | No file              | `8a393a7ed24b`  |
| 697    | No file              | `8a393a7ed24b`  |
| 689    | No file              | `8a393a7ed24b`  |
| 683    | No file              | `8a393a7ed24b`  |
| 678    | No file              | `8a393a7ed24b`  |
| 670    | No file              | `8a393a7ed24b`  |
| 661    | No file              | `8a393a7ed24b`  |
| 656    | No file              | `8a393a7ed24b`  |
| 652    | No file              | `8a393a7ed24b`  |
| 643    | No file              | `8a393a7ed24b`  |
| 637    | No file              | `8a393a7ed24b`  |
| 630    | No file              | `8a393a7ed24b`  |
| 627    | No file              | `8a393a7ed24b`  |
| 621    | No file              | `8a393a7ed24b`  |
| 617    | No file              | `8a393a7ed24b`  |
| 615    | No file              | `8a393a7ed24b`  |
| 606    | No file              | `8a393a7ed24b`  |
| 599    | No file              | `8a393a7ed24b`  |
| 592    | No file              | `8a393a7ed24b`  |
| 586    | No file              | `8a393a7ed24b`  |
| 577    | No file              | `8a393a7ed24b`  |
| 569    | No file              | `8a393a7ed24b`  |
| 561    | No file              | `8a393a7ed24b`  |
| 554    | No file              | `8a393a7ed24b`  |
| 542    | No file              | `8a393a7ed24b`  |
| 532    | No file              | `8a393a7ed24b`  |
| 531    | No file              | `8a393a7ed24b`  |
| 526    | No file              | `8a393a7ed24b`  |
| 521    | No file              | `8a393a7ed24b`  |
| 517    | No file              | `8a393a7ed24b`  |
| 510    | No file              | `8a393a7ed24b`  |
| 508    | No file              | `8a393a7ed24b`  |
| 504    | No file              | `8a393a7ed24b`  |
| 497    | No file              | `8a393a7ed24b`  |
| 491    | No file              | `8a393a7ed24b`  |
| 485    | No file              | `8a393a7ed24b`  |
| 478    | No file              | `8a393a7ed24b`  |
| 472    | No file              | `8a393a7ed24b`  |
| 466    | No file              | `8a393a7ed24b`  |
| 457    | No file              | `8a393a7ed24b`  |
| 452    | No file              | `8a393a7ed24b`  |
| 449    | No file              | `8a393a7ed24b`  |
| 435    | No file              | `8a393a7ed24b`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                    |
| ----------------------------- | -------- | ----------------------------------------------------------------------- |
| `dropuihuntinggroundinfo.bss` | Optional | Hunting grounds per tag, for the Hunting Grounds column                 |
| `languagedata_en.loc`         | Optional | Tag names and tooltips (117), hunting ground names (116)                |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of 45 fixed 32-byte rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds 118 strings: the Korean
names and tooltips, the guide image names and the colours as hex text.

| Offset              | Type           | Field              | Notes                             |
| ------------------- | -------------- | ------------------ | --------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                      |
| `+0x04`             | u32            | count              | Number of rows; 45 on client 3458 |
| `+0x08`             | Tag Row[count] | rows               | See Tag Row                       |
| `rows+0x00`         | String Table   | string_table       | 118 wide strings                  |
| `string_table+0x00` | u32            | string_table_start | Where the rows end                |
| `string_table+0x04` | u32            | zero               | Always `0`                        |

Rows are sorted by key, 1 to 45 with no gaps.

### Tag Row (32 bytes)

| Offset  | Type | Field             | Notes                                                                                                               |
| ------- | ---- | ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key               | Tag key, as in `tag_keys`; LOC type 117 `str_id1`                                                                   |
| `+0x04` | u32  | name_ref          | String table index of the Korean name (`#다수의 몬스터와 전투`); LOC `str_id4` 0 is the English one (`#LotsOfMobs`) |
| `+0x08` | u32  | guide_texture_ref | String table index of the guide image name; the empty string on 32 rows                                             |
| `+0x0C` | u32  | desc_ref          | String table index of the Korean tooltip, with `<PAColor>` tags; LOC `str_id4` 1 is the English one                 |
| `+0x10` | u32  | texture_color_ref | String table index of `texture_color` as hex text (`ffe1ba65`)                                                      |
| `+0x14` | u32  | font_color_ref    | String table index of `font_color` as hex text                                                                      |
| `+0x18` | u32  | texture_color     | Tag background colour, ARGB (`0xFFE1BA65`)                                                                          |
| `+0x1C` | u32  | font_color        | Tag text colour, ARGB                                                                                               |

The two hex strings always equal the two ARGB values (case aside: `ffD2691E`,
`ff3CB371`), so the strings carry nothing extra. The colours are the same on
34 rows; the other 11 have a darker background and a lighter text:

| Keys                     | Tag                         | `texture_color` | `font_color` |
| ------------------------ | --------------------------- | --------------- | ------------ |
| 20, 21, 23, 25 to 32, 42, 43 | `#FixedLanternSpot`     | `0xFF5384D5`    | `0xFFA6C0EA` |
| 38, 39, 40               | Stun, knockdown, knockback  | `0xFFD2691E`    | `0xFFFFA500` |
| 41                       | `#AllanSerbinsLandscape`    | `0xFF3CB371`    | `0xFF98FB98` |

Some colours are shared: `0xFF63B6E6` on `#NoItemCollectGauge`,
`#NoAgrisFever`, both Golden Pig Caves, Atoraxxion and Orzekea, and
`0xFFCB6768` on `#TreasurePieces`, `#RedArtifacts` and `#HighestTier`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Guide Images

`guide_texture_ref` is set only on the 13 `#FixedLanternSpot` rows, one image
per zone (`Combine_Etc_DekiaLanterns_GroundTooltip_01` to `_13`): a map of
where the Dehkia's Lantern can be summoned, shown when the tag is clicked.
Each name is a whole texture of the same name, lower-cased, in the folder its
first two parts name: `ui_texture/combine/etc/combine_etc_dekialanterns_groundtooltip_01.dds`.
All 13 exist on client 3458 (717.8 KB each).

## Notes

- The Korean tooltips store a line break as the two characters `\n`, where
  LOC has a real newline.
- Only tag 17 (`#PartyOf4`) is on no hunting ground on client 3458; LOC type
  117 names all 45 plus a key 46 with the same `#DivineAuthority` text as 45.
- The drop item window Lua (`window/dropitem/panel_window_renewdropitem_all_1`)
  draws each tag through `ToClient_getDropUITagStaticStatusWrapper`:
  `tagControl:SetColor(getTextureColor())`, `SetFontColor(getFontColor())`,
  the text from `getTagString`, the tooltip from `getTagTooltipDescString`
  under the `LUA_DROPITEMUI_TOOLTIP_TAG_TITLE` heading, and on click the
  guide image from `getTagGuideTextureId` when `isExistGuideTextureId`.
- Which slot is which colour comes from
  [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  (`DecodeTags`: `+0x18` texture, `+0x1C` font) and fits the data: wherever
  the two differ, `+0x1C` is the lighter shade, as text on a tinted
  background would be. The getters alone do not show the order; the game
  confirms it: on Aakman, `#Knockdown/Bound` is orange text on a brown pill.
- The tag control's texture (`StaticText_Tag_Templete` in
  `ui_data/window/dropitem/panel_window_dropitem_all_renew.xml`) is
  `Combine_Etc_DropItem_Tag_BG`, a pill in `combine/etc/combine_etc_dropitem.dds`
  (UV 128,314 to 228,339) that is white at alpha 51. `SetColor` tints it, so
  the background shows `texture_color` at about 20% over the window, and a
  tag whose two colours are equal (34 of 45) still reads.

## Open Questions

### Where the Client Resolves a Guide Image Name

The window Lua hands `getTagGuideTextureId` to
`PaGlobalFunc_DropItemImageToolTip_Open` as a texture ID. I have not found the
table that maps such an ID to a file, so the handler takes the file of the
same name in the folder the first two name parts give. That holds for all 13
names on client 3458, but `Combine_Etc_DropItem_Tag_BG` is a sprite inside
`combine_etc_dropitem.dds`, so a later guide image could be a sprite too and
then show a dash.
