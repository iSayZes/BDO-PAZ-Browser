# `itemchange.bss` Format

## Purpose

The Change Item conversions: per row an armor item and the costume it turns
into in the Change Item window (`[Warrior] Calpheon Noble Suit` to
`[Warrior] Calpheon Noble Suit (Costume)`). The window
(`panel_window_changeitem_renew.luac`) offers an inventory item only when
`getItemChange(itemKey)` finds a row for it and shows the item that row
makes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File             | Bytes | Records | Row bytes |
| ------ | ------------- | ------- | ---------------- | ----- | ------- | --------- |
| 2      | 805 and later | 3483    | `itemchange.bss` | 6,548 | 408 Row | 16        |
| 1      | 435 to 794    | 794     | `itemchange.bss` | 3,908 | 244 Row | 16        |

| Layout | File             | Known            | Unknown    |
| ------ | ---------------- | ---------------- | ---------- |
| 2      | `itemchange.bss` | 6,548 B (100.0%) | 0 B (0.0%) |
| 1      | `itemchange.bss` | 3,908 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ce77eef42343`  |
| 3482   | Layout 2 | `ce77eef42343`  |
| 3474   | Layout 2 | `ce77eef42343`  |
| 3473   | Layout 2 | `ce77eef42343`  |
| 3464   | Layout 2 | `ce77eef42343`  |
| 3458   | Layout 2 | `ce77eef42343`  |
| 3454   | Layout 2 | `ce77eef42343`  |
| 3444   | Layout 2 | `ce77eef42343`  |
| 3435   | Layout 2 | `ce77eef42343`  |
| 3426   | Layout 2 | `ce77eef42343`  |
| 3418   | Layout 2 | `ce77eef42343`  |
| 3412   | Layout 2 | `ce77eef42343`  |
| 3402   | Layout 2 | `ce77eef42343`  |
| 3396   | Layout 2 | `ce77eef42343`  |
| 3387   | Layout 2 | `ce77eef42343`  |
| 3381   | Layout 2 | `ce77eef42343`  |
| 3373   | Layout 2 | `ce77eef42343`  |
| 3364   | Layout 2 | `ce77eef42343`  |
| 3356   | Layout 2 | `ce77eef42343`  |
| 3349   | Layout 2 | `ce77eef42343`  |
| 3342   | Layout 2 | `ce77eef42343`  |
| 3335   | Layout 2 | `ce77eef42343`  |
| 3326   | Layout 2 | `ce77eef42343`  |
| 3321   | Layout 2 | `ce77eef42343`  |
| 3314   | Layout 2 | `ce77eef42343`  |
| 3303   | Layout 2 | `ce77eef42343`  |
| 3302   | Layout 2 | `ce77eef42343`  |
| 3293   | Layout 2 | `ce77eef42343`  |
| 3283   | Layout 2 | `ce77eef42343`  |
| 3275   | Layout 2 | `ce77eef42343`  |
| 3267   | Layout 2 | `ce77eef42343`  |
| 3258   | Layout 2 | `ce77eef42343`  |
| 3251   | Layout 2 | `ce77eef42343`  |
| 3242   | Layout 2 | `ce77eef42343`  |
| 3235   | Layout 2 | `ce77eef42343`  |
| 3229   | Layout 2 | `ce77eef42343`  |
| 3212   | Layout 2 | `ce77eef42343`  |
| 3203   | Layout 2 | `ce77eef42343`  |
| 3193   | Layout 2 | `ce77eef42343`  |
| 3186   | Layout 2 | `ce77eef42343`  |
| 3177   | Layout 2 | `ce77eef42343`  |
| 3169   | Layout 2 | `ce77eef42343`  |
| 3158   | Layout 2 | `ce77eef42343`  |
| 3151   | Layout 2 | `ce77eef42343`  |
| 3144   | Layout 2 | `ce77eef42343`  |
| 3133   | Layout 2 | `ce77eef42343`  |
| 3125   | Layout 2 | `ce77eef42343`  |
| 3118   | Layout 2 | `ce77eef42343`  |
| 3111   | Layout 2 | `ce77eef42343`  |
| 3103   | Layout 2 | `ce77eef42343`  |
| 3095   | Layout 2 | `ce77eef42343`  |
| 3086   | Layout 2 | `ce77eef42343`  |
| 3072   | Layout 2 | `ce77eef42343`  |
| 3062   | Layout 2 | `ce77eef42343`  |
| 3052   | Layout 2 | `ce77eef42343`  |
| 3045   | Layout 2 | `ce77eef42343`  |
| 3037   | Layout 2 | `ce77eef42343`  |
| 3030   | Layout 2 | `ce77eef42343`  |
| 3021   | Layout 2 | `ce77eef42343`  |
| 3012   | Layout 2 | `ce77eef42343`  |
| 3002   | Layout 2 | `ce77eef42343`  |
| 2995   | Layout 2 | `ce77eef42343`  |
| 2987   | Layout 2 | `ce77eef42343`  |
| 2978   | Layout 2 | `ce77eef42343`  |
| 2970   | Layout 2 | `ce77eef42343`  |
| 2959   | Layout 2 | `ce77eef42343`  |
| 2951   | Layout 2 | `ce77eef42343`  |
| 2942   | Layout 2 | `ce77eef42343`  |
| 2935   | Layout 2 | `ce77eef42343`  |
| 2932   | Layout 2 | `ce77eef42343`  |
| 2923   | Layout 2 | `ce77eef42343`  |
| 2919   | Layout 2 | `ce77eef42343`  |
| 2907   | Layout 2 | `ce77eef42343`  |
| 2900   | Layout 2 | `ce77eef42343`  |
| 2891   | Layout 2 | `ce77eef42343`  |
| 2882   | Layout 2 | `ce77eef42343`  |
| 2872   | Layout 2 | `ce77eef42343`  |
| 2863   | Layout 2 | `ce77eef42343`  |
| 2855   | Layout 2 | `ce77eef42343`  |
| 2849   | Layout 2 | `ce77eef42343`  |
| 2844   | Layout 2 | `ce77eef42343`  |
| 2834   | Layout 2 | `ce77eef42343`  |
| 2825   | Layout 2 | `ce77eef42343`  |
| 2819   | Layout 2 | `ce77eef42343`  |
| 2811   | Layout 2 | `ce77eef42343`  |
| 2803   | Layout 2 | `ce77eef42343`  |
| 2794   | Layout 2 | `ce77eef42343`  |
| 2783   | Layout 2 | `ce77eef42343`  |
| 2774   | Layout 2 | `ce77eef42343`  |
| 2765   | Layout 2 | `ce77eef42343`  |
| 2756   | Layout 2 | `ce77eef42343`  |
| 2750   | Layout 2 | `ce77eef42343`  |
| 2743   | Layout 2 | `ce77eef42343`  |
| 2736   | Layout 2 | `ce77eef42343`  |
| 2726   | Layout 2 | `ce77eef42343`  |
| 2717   | Layout 2 | `ce77eef42343`  |
| 2709   | Layout 2 | `ce77eef42343`  |
| 2703   | Layout 2 | `ce77eef42343`  |
| 2695   | Layout 2 | `ce77eef42343`  |
| 2684   | Layout 2 | `ce77eef42343`  |
| 2672   | Layout 2 | `ce77eef42343`  |
| 2665   | Layout 2 | `ce77eef42343`  |
| 2657   | Layout 2 | `ce77eef42343`  |
| 2649   | Layout 2 | `ce77eef42343`  |
| 2644   | Layout 2 | `ce77eef42343`  |
| 2637   | Layout 2 | `ce77eef42343`  |
| 2629   | Layout 2 | `ce77eef42343`  |
| 2619   | Layout 2 | `ce77eef42343`  |
| 2612   | Layout 2 | `ce77eef42343`  |
| 2606   | Layout 2 | `ce77eef42343`  |
| 2602   | Layout 2 | `ce77eef42343`  |
| 2601   | Layout 2 | `ce77eef42343`  |
| 2592   | Layout 2 | `ce77eef42343`  |
| 2583   | Layout 2 | `ce77eef42343`  |
| 2575   | Layout 2 | `ce77eef42343`  |
| 2567   | Layout 2 | `ce77eef42343`  |
| 2560   | Layout 2 | `ce77eef42343`  |
| 2553   | Layout 2 | `ce77eef42343`  |
| 2545   | Layout 2 | `ce77eef42343`  |
| 2538   | Layout 2 | `ce77eef42343`  |
| 2529   | Layout 2 | `ce77eef42343`  |
| 2519   | Layout 2 | `ce77eef42343`  |
| 2513   | Layout 2 | `ce77eef42343`  |
| 2510   | Layout 2 | `ce77eef42343`  |
| 2507   | Layout 2 | `ce77eef42343`  |
| 2503   | Layout 2 | `ce77eef42343`  |
| 2498   | Layout 2 | `ce77eef42343`  |
| 2492   | Layout 2 | `ce77eef42343`  |
| 2487   | Layout 2 | `ce77eef42343`  |
| 2480   | Layout 2 | `ce77eef42343`  |
| 2474   | Layout 2 | `ce77eef42343`  |
| 2468   | Layout 2 | `ce77eef42343`  |
| 2460   | Layout 2 | `ce77eef42343`  |
| 2453   | Layout 2 | `ce77eef42343`  |
| 2444   | Layout 2 | `ce77eef42343`  |
| 2438   | Layout 2 | `ce77eef42343`  |
| 2434   | Layout 2 | `ce77eef42343`  |
| 2429   | Layout 2 | `ce77eef42343`  |
| 2421   | Layout 2 | `ce77eef42343`  |
| 2414   | Layout 2 | `ce77eef42343`  |
| 2407   | Layout 2 | `ce77eef42343`  |
| 2401   | Layout 2 | `ce77eef42343`  |
| 2397   | Layout 2 | `ce77eef42343`  |
| 2393   | Layout 2 | `ce77eef42343`  |
| 2384   | Layout 2 | `ce77eef42343`  |
| 2378   | Layout 2 | `ce77eef42343`  |
| 2372   | Layout 2 | `ce77eef42343`  |
| 2358   | Layout 2 | `ce77eef42343`  |
| 2352   | Layout 2 | `ce77eef42343`  |
| 2347   | Layout 2 | `ce77eef42343`  |
| 2343   | Layout 2 | `ce77eef42343`  |
| 2335   | Layout 2 | `ce77eef42343`  |
| 2327   | Layout 2 | `ce77eef42343`  |
| 2324   | Layout 2 | `ce77eef42343`  |
| 2319   | Layout 2 | `ce77eef42343`  |
| 2313   | Layout 2 | `ce77eef42343`  |
| 2308   | Layout 2 | `ce77eef42343`  |
| 2302   | Layout 2 | `ce77eef42343`  |
| 2295   | Layout 2 | `ce77eef42343`  |
| 2290   | Layout 2 | `ce77eef42343`  |
| 2284   | Layout 2 | `ce77eef42343`  |
| 2276   | Layout 2 | `ce77eef42343`  |
| 2269   | Layout 2 | `ce77eef42343`  |
| 2259   | Layout 2 | `ce77eef42343`  |
| 2250   | Layout 2 | `ce77eef42343`  |
| 2243   | Layout 2 | `ce77eef42343`  |
| 2235   | Layout 2 | `ce77eef42343`  |
| 2229   | Layout 2 | `ce77eef42343`  |
| 2224   | Layout 2 | `ce77eef42343`  |
| 2218   | Layout 2 | `ce77eef42343`  |
| 2215   | Layout 2 | `ce77eef42343`  |
| 2207   | Layout 2 | `ce77eef42343`  |
| 2203   | Layout 2 | `ce77eef42343`  |
| 2196   | Layout 2 | `ce77eef42343`  |
| 2192   | Layout 2 | `ce77eef42343`  |
| 2189   | Layout 2 | `ce77eef42343`  |
| 2183   | Layout 2 | `ce77eef42343`  |
| 2179   | Layout 2 | `ce77eef42343`  |
| 2171   | Layout 2 | `ce77eef42343`  |
| 2163   | Layout 2 | `ce77eef42343`  |
| 2156   | Layout 2 | `ce77eef42343`  |
| 2151   | Layout 2 | `ce77eef42343`  |
| 2147   | Layout 2 | `ce77eef42343`  |
| 2142   | Layout 2 | `ce77eef42343`  |
| 2138   | Layout 2 | `ce77eef42343`  |
| 2134   | Layout 2 | `ce77eef42343`  |
| 2130   | Layout 2 | `ce77eef42343`  |
| 2122   | Layout 2 | `ce77eef42343`  |
| 2107   | Layout 2 | `ce77eef42343`  |
| 2098   | Layout 2 | `ce77eef42343`  |
| 2089   | Layout 2 | `ce77eef42343`  |
| 2081   | Layout 2 | `ce77eef42343`  |
| 2073   | Layout 2 | `ce77eef42343`  |
| 2067   | Layout 2 | `ce77eef42343`  |
| 2063   | Layout 2 | `ce77eef42343`  |
| 2059   | Layout 2 | `ce77eef42343`  |
| 2052   | Layout 2 | `ce77eef42343`  |
| 2044   | Layout 2 | `ce77eef42343`  |
| 2039   | Layout 2 | `ce77eef42343`  |
| 2032   | Layout 2 | `ce77eef42343`  |
| 2025   | Layout 2 | `ce77eef42343`  |
| 2011   | Layout 2 | `ce77eef42343`  |
| 2005   | Layout 2 | `ce77eef42343`  |
| 2000   | Layout 2 | `ce77eef42343`  |
| 1996   | Layout 2 | `ce77eef42343`  |
| 1991   | Layout 2 | `ce77eef42343`  |
| 1985   | Layout 2 | `ce77eef42343`  |
| 1980   | Layout 2 | `ce77eef42343`  |
| 1969   | Layout 2 | `ce77eef42343`  |
| 1964   | Layout 2 | `ce77eef42343`  |
| 1958   | Layout 2 | `ce77eef42343`  |
| 1950   | Layout 2 | `ce77eef42343`  |
| 1945   | Layout 2 | `ce77eef42343`  |
| 1937   | Layout 2 | `ce77eef42343`  |
| 1933   | Layout 2 | `ce77eef42343`  |
| 1927   | Layout 2 | `ce77eef42343`  |
| 1921   | Layout 2 | `ce77eef42343`  |
| 1914   | Layout 2 | `ce77eef42343`  |
| 1908   | Layout 2 | `ce77eef42343`  |
| 1897   | Layout 2 | `ce77eef42343`  |
| 1892   | Layout 2 | `ce77eef42343`  |
| 1886   | Layout 2 | `ce77eef42343`  |
| 1881   | Layout 2 | `ce77eef42343`  |
| 1871   | Layout 2 | `ce77eef42343`  |
| 1866   | Layout 2 | `ce77eef42343`  |
| 1862   | Layout 2 | `ce77eef42343`  |
| 1854   | Layout 2 | `ce77eef42343`  |
| 1846   | Layout 2 | `ce77eef42343`  |
| 1838   | Layout 2 | `ce77eef42343`  |
| 1832   | Layout 2 | `ce77eef42343`  |
| 1826   | Layout 2 | `ce77eef42343`  |
| 1822   | Layout 2 | `ce77eef42343`  |
| 1818   | Layout 2 | `ce77eef42343`  |
| 1804   | Layout 2 | `ce77eef42343`  |
| 1794   | Layout 2 | `ce77eef42343`  |
| 1790   | Layout 2 | `ce77eef42343`  |
| 1784   | Layout 2 | `ce77eef42343`  |
| 1774   | Layout 2 | `ce77eef42343`  |
| 1771   | Layout 2 | `ce77eef42343`  |
| 1762   | Layout 2 | `ce77eef42343`  |
| 1759   | Layout 2 | `ce77eef42343`  |
| 1754   | Layout 2 | `ce77eef42343`  |
| 1749   | Layout 2 | `ce77eef42343`  |
| 1743   | Layout 2 | `ce77eef42343`  |
| 1737   | Layout 2 | `ce77eef42343`  |
| 1731   | Layout 2 | `ce77eef42343`  |
| 1725   | Layout 2 | `ce77eef42343`  |
| 1717   | Layout 2 | `ce77eef42343`  |
| 1710   | Layout 2 | `ce77eef42343`  |
| 1704   | Layout 2 | `ce77eef42343`  |
| 1698   | Layout 2 | `ce77eef42343`  |
| 1690   | Layout 2 | `ce77eef42343`  |
| 1685   | Layout 2 | `ce77eef42343`  |
| 1680   | Layout 2 | `ce77eef42343`  |
| 1674   | Layout 2 | `ce77eef42343`  |
| 1668   | Layout 2 | `ce77eef42343`  |
| 1659   | Layout 2 | `ce77eef42343`  |
| 1649   | Layout 2 | `ce77eef42343`  |
| 1642   | Layout 2 | `ce77eef42343`  |
| 1636   | Layout 2 | `ce77eef42343`  |
| 1628   | Layout 2 | `ce77eef42343`  |
| 1622   | Layout 2 | `ce77eef42343`  |
| 1614   | Layout 2 | `ce77eef42343`  |
| 1608   | Layout 2 | `ce77eef42343`  |
| 1602   | Layout 2 | `ce77eef42343`  |
| 1598   | Layout 2 | `ce77eef42343`  |
| 1594   | Layout 2 | `ce77eef42343`  |
| 1590   | Layout 2 | `ce77eef42343`  |
| 1587   | Layout 2 | `ce77eef42343`  |
| 1584   | Layout 2 | `ce77eef42343`  |
| 1579   | Layout 2 | `ce77eef42343`  |
| 1572   | Layout 2 | `ce77eef42343`  |
| 1565   | Layout 2 | `ce77eef42343`  |
| 1559   | Layout 2 | `ce77eef42343`  |
| 1554   | Layout 2 | `ce77eef42343`  |
| 1547   | Layout 2 | `ce77eef42343`  |
| 1537   | Layout 2 | `ce77eef42343`  |
| 1529   | Layout 2 | `ce77eef42343`  |
| 1524   | Layout 2 | `ce77eef42343`  |
| 1519   | Layout 2 | `ce77eef42343`  |
| 1509   | Layout 2 | `ce77eef42343`  |
| 1506   | Layout 2 | `ce77eef42343`  |
| 1504   | Layout 2 | `ce77eef42343`  |
| 1500   | Layout 2 | `ce77eef42343`  |
| 1493   | Layout 2 | `ce77eef42343`  |
| 1489   | Layout 2 | `ce77eef42343`  |
| 1485   | Layout 2 | `ce77eef42343`  |
| 1481   | Layout 2 | `ce77eef42343`  |
| 1474   | Layout 2 | `ce77eef42343`  |
| 1466   | Layout 2 | `ce77eef42343`  |
| 1462   | Layout 2 | `ce77eef42343`  |
| 1459   | Layout 2 | `ce77eef42343`  |
| 1453   | Layout 2 | `ce77eef42343`  |
| 1450   | Layout 2 | `ce77eef42343`  |
| 1445   | Layout 2 | `ce77eef42343`  |
| 1439   | Layout 2 | `ce77eef42343`  |
| 1433   | Layout 2 | `ce77eef42343`  |
| 1430   | Layout 2 | `ce77eef42343`  |
| 1426   | Layout 2 | `ce77eef42343`  |
| 1421   | Layout 2 | `ce77eef42343`  |
| 1417   | Layout 2 | `ce77eef42343`  |
| 1416   | Layout 2 | `ce77eef42343`  |
| 1409   | Layout 2 | `ce77eef42343`  |
| 1405   | Layout 2 | `ce77eef42343`  |
| 1401   | Layout 2 | `ce77eef42343`  |
| 1396   | Layout 2 | `ce77eef42343`  |
| 1391   | Layout 2 | `ce77eef42343`  |
| 1390   | Layout 2 | `ce77eef42343`  |
| 1386   | Layout 2 | `ce77eef42343`  |
| 1381   | Layout 2 | `ce77eef42343`  |
| 1379   | Layout 2 | `ce77eef42343`  |
| 1372   | Layout 2 | `ce77eef42343`  |
| 1366   | Layout 2 | `ce77eef42343`  |
| 1364   | Layout 2 | `ce77eef42343`  |
| 1363   | Layout 2 | `ce77eef42343`  |
| 1360   | Layout 2 | `ce77eef42343`  |
| 1358   | Layout 2 | `ce77eef42343`  |
| 1355   | Layout 2 | `ce77eef42343`  |
| 1351   | Layout 2 | `ce77eef42343`  |
| 1348   | Layout 2 | `ce77eef42343`  |
| 1346   | Layout 2 | `ce77eef42343`  |
| 1341   | Layout 2 | `ce77eef42343`  |
| 1340   | Layout 2 | `ce77eef42343`  |
| 1338   | Layout 2 | `ce77eef42343`  |
| 1335   | Layout 2 | `ce77eef42343`  |
| 1333   | Layout 2 | `ce77eef42343`  |
| 1329   | Layout 2 | `ce77eef42343`  |
| 1327   | Layout 2 | `ce77eef42343`  |
| 1324   | Layout 2 | `ce77eef42343`  |
| 1321   | Layout 2 | `ce77eef42343`  |
| 1319   | Layout 2 | `ce77eef42343`  |
| 1318   | Layout 2 | `ce77eef42343`  |
| 1316   | Layout 2 | `ce77eef42343`  |
| 1313   | Layout 2 | `ce77eef42343`  |
| 1311   | Layout 2 | `ce77eef42343`  |
| 1309   | Layout 2 | `ce77eef42343`  |
| 1304   | Layout 2 | `ce77eef42343`  |
| 1292   | Layout 2 | `ce77eef42343`  |
| 1286   | Layout 2 | `ce77eef42343`  |
| 1280   | Layout 2 | `ce77eef42343`  |
| 1276   | Layout 2 | `ce77eef42343`  |
| 1267   | Layout 2 | `ce77eef42343`  |
| 1261   | Layout 2 | `ce77eef42343`  |
| 1256   | Layout 2 | `ce77eef42343`  |
| 1250   | Layout 2 | `ce77eef42343`  |
| 1246   | Layout 2 | `ce77eef42343`  |
| 1239   | Layout 2 | `ce77eef42343`  |
| 1230   | Layout 2 | `ce77eef42343`  |
| 1226   | Layout 2 | `ce77eef42343`  |
| 1220   | Layout 2 | `ce77eef42343`  |
| 1217   | Layout 2 | `ce77eef42343`  |
| 1211   | Layout 2 | `ce77eef42343`  |
| 1210   | Layout 2 | `ce77eef42343`  |
| 1208   | Layout 2 | `ce77eef42343`  |
| 1203   | Layout 2 | `ce77eef42343`  |
| 1197   | Layout 2 | `ce77eef42343`  |
| 1194   | Layout 2 | `ce77eef42343`  |
| 1192   | Layout 2 | `ce77eef42343`  |
| 1187   | Layout 2 | `ce77eef42343`  |
| 1183   | Layout 2 | `ce77eef42343`  |
| 1177   | Layout 2 | `ce77eef42343`  |
| 1173   | Layout 2 | `ce77eef42343`  |
| 1167   | Layout 2 | `ce77eef42343`  |
| 1164   | Layout 2 | `ce77eef42343`  |
| 1156   | Layout 2 | `ce77eef42343`  |
| 1149   | Layout 2 | `ce77eef42343`  |
| 1144   | Layout 2 | `ce77eef42343`  |
| 1137   | Layout 2 | `ce77eef42343`  |
| 1132   | Layout 2 | `ce77eef42343`  |
| 1127   | Layout 2 | `ce77eef42343`  |
| 1122   | Layout 2 | `ce77eef42343`  |
| 1118   | Layout 2 | `ce77eef42343`  |
| 1114   | Layout 2 | `ce77eef42343`  |
| 1109   | Layout 2 | `ce77eef42343`  |
| 1102   | No file  | `ce77eef42343`  |
| 1096   | No file  | `ce77eef42343`  |
| 1088   | No file  | `ce77eef42343`  |
| 1081   | No file  | `ce77eef42343`  |
| 1076   | No file  | `ce77eef42343`  |
| 1069   | No file  | `ce77eef42343`  |
| 1064   | No file  | `ce77eef42343`  |
| 1058   | No file  | `ce77eef42343`  |
| 1051   | No file  | `ce77eef42343`  |
| 1044   | No file  | `ce77eef42343`  |
| 1036   | No file  | `ce77eef42343`  |
| 1026   | No file  | `ce77eef42343`  |
| 1016   | No file  | `ce77eef42343`  |
| 1009   | No file  | `ce77eef42343`  |
| 1005   | No file  | `ce77eef42343`  |
| 1000   | No file  | `ce77eef42343`  |
| 998    | No file  | `ce77eef42343`  |
| 990    | No file  | `ce77eef42343`  |
| 979    | No file  | `ce77eef42343`  |
| 972    | No file  | `ce77eef42343`  |
| 963    | No file  | `ce77eef42343`  |
| 955    | No file  | `ce77eef42343`  |
| 946    | No file  | `ce77eef42343`  |
| 938    | No file  | `ce77eef42343`  |
| 927    | No file  | `ce77eef42343`  |
| 911    | No file  | `ce77eef42343`  |
| 904    | No file  | `ce77eef42343`  |
| 899    | No file  | `ce77eef42343`  |
| 894    | No file  | `ce77eef42343`  |
| 885    | No file  | `ce77eef42343`  |
| 879    | No file  | `ce77eef42343`  |
| 872    | No file  | `ce77eef42343`  |
| 864    | No file  | `ce77eef42343`  |
| 855    | No file  | `ce77eef42343`  |
| 853    | No file  | `ce77eef42343`  |
| 845    | No file  | `ce77eef42343`  |
| 837    | No file  | `ce77eef42343`  |
| 829    | Layout 2 | `ce77eef42343`  |
| 822    | Layout 2 | `ce77eef42343`  |
| 814    | Layout 2 | `ce77eef42343`  |
| 805    | Layout 2 | `ce77eef42343`  |
| 794    | Layout 1 | `ce77eef42343`  |
| 787    | Layout 1 | `ce77eef42343`  |
| 780    | Layout 1 | `ce77eef42343`  |
| 771    | Layout 1 | `ce77eef42343`  |
| 760    | Layout 1 | `ce77eef42343`  |
| 748    | Layout 1 | `ce77eef42343`  |
| 741    | Layout 1 | `ce77eef42343`  |
| 736    | Layout 1 | `ce77eef42343`  |
| 731    | Layout 1 | `ce77eef42343`  |
| 723    | Layout 1 | `ce77eef42343`  |
| 711    | Layout 1 | `ce77eef42343`  |
| 707    | Layout 1 | `ce77eef42343`  |
| 697    | Layout 1 | `ce77eef42343`  |
| 689    | Layout 1 | `ce77eef42343`  |
| 683    | Layout 1 | `ce77eef42343`  |
| 678    | Layout 1 | `ce77eef42343`  |
| 670    | Layout 1 | `ce77eef42343`  |
| 661    | Layout 1 | `ce77eef42343`  |
| 656    | Layout 1 | `ce77eef42343`  |
| 652    | Layout 1 | `ce77eef42343`  |
| 643    | Layout 1 | `ce77eef42343`  |
| 637    | Layout 1 | `ce77eef42343`  |
| 630    | Layout 1 | `ce77eef42343`  |
| 627    | Layout 1 | `ce77eef42343`  |
| 621    | Layout 1 | `ce77eef42343`  |
| 617    | Layout 1 | `ce77eef42343`  |
| 615    | Layout 1 | `ce77eef42343`  |
| 606    | Layout 1 | `ce77eef42343`  |
| 599    | Layout 1 | `ce77eef42343`  |
| 592    | Layout 1 | `ce77eef42343`  |
| 586    | Layout 1 | `ce77eef42343`  |
| 577    | Layout 1 | `ce77eef42343`  |
| 569    | Layout 1 | `ce77eef42343`  |
| 561    | Layout 1 | `ce77eef42343`  |
| 554    | Layout 1 | `ce77eef42343`  |
| 542    | Layout 1 | `ce77eef42343`  |
| 532    | Layout 1 | `ce77eef42343`  |
| 531    | Layout 1 | `ce77eef42343`  |
| 526    | Layout 1 | `ce77eef42343`  |
| 521    | Layout 1 | `ce77eef42343`  |
| 517    | Layout 1 | `ce77eef42343`  |
| 510    | Layout 1 | `ce77eef42343`  |
| 508    | Layout 1 | `ce77eef42343`  |
| 504    | Layout 1 | `ce77eef42343`  |
| 497    | Layout 1 | `ce77eef42343`  |
| 491    | Layout 1 | `ce77eef42343`  |
| 485    | Layout 1 | `ce77eef42343`  |
| 478    | Layout 1 | `ce77eef42343`  |
| 472    | Layout 1 | `ce77eef42343`  |
| 466    | Layout 1 | `ce77eef42343`  |
| 457    | Layout 1 | `ce77eef42343`  |
| 452    | Layout 1 | `ce77eef42343`  |
| 449    | Layout 1 | `ce77eef42343`  |
| 435    | Layout 1 | `ce77eef42343`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

The 2016 `gc::ItemChangeStaticStatus` packed, after its u16 map key: its
members in order, without the alignment padding after `_key` and without the
two `gc::ItemEnchantStaticStatus` pointers.

| Offset  | Type | Field         | Notes                                                                                  |
| ------- | ---- | ------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u16  | key           | Row key; unique, the rows are in no key order                                          |
| `+0x02` | u16  | key_dup       | Equals `key` on every row of clients 1784 and 3482                                     |
| `+0x04` | u32  | from_item_key | Item the conversion takes, a packed item key (`enchant_level << 24 \| item_id`)          |
| `+0x08` | u32  | to_item_key   | Item it makes, a packed item key; enhancement level `0` on every row of clients 1784 and 3482 |
| `+0x0C` | i32  | type          | `0` on every row of clients 1784 and 3482                                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

A bare row count and the rows: no PABR magic and no string table. Only the
File Layout differs from Layout 2.

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

## Field Names

The 2016 `gc::ItemChangeStaticStatus` holds `_key` (u16), `_fromItemKey`
and `_toItemKey` (`gc::ItemEnchantKey`), `_type` (int) and a pointer to each
item's `gc::ItemEnchantStaticStatus`; its manager keys the rows by a u16
`gc::KeyType`, which the file stores before the row. The `ItemChange_Table`
sheet of a private server's `DataSheets.bexcel` on client 1784 has the
columns `Index`, `FromItemKey`, `FromEnchantLevel`, `ToItemKey`,
`ToEnchantLevel` and `Type`:

| Field         | Column                              | Same value (client 1784) | Same value (client 3482) |
| ------------- | ----------------------------------- | ------------------------ | ------------------------ |
| key, key_dup  | `Index`                             | 324 of 324               | 317 of 408               |
| from_item_key | `FromItemKey`, `FromEnchantLevel`   | 324 of 324               | 317 of 317               |
| to_item_key   | `ToItemKey`, `ToEnchantLevel`       | 324 of 324               | 317 of 317               |
| type          | `Type`                              | 324 of 324               | 317 of 317               |

The sheet has 327 keys; client 3482 adds 91 keys the sheet does not have.
Both enhancement levels and `Type` are `0` on every sheet row, so the
column match places `type` by the 2016 member order only.

## Notes

- On client 3482, 406 of the 408 rows take a different item; two items have
  two rows each, as in the sheet (`FromItemKey` 12581 and 12597).
- The made item is the costume of the item it takes on every row checked:
  `12672` [Mystic] Delphe Knight Armor makes `12683` [Mystic] Delphe Knight
  Armor (Costume), `933420` [Agent] Serendian Smith Garb makes `933421`.
- The handler (`_bss/itemchange/`) shows one row per conversion with both
  items.

## Open Questions

### What `type` Selects

`type` is `0` on every row of clients 1784 and 3482 and in every sheet row.
The client 3482 Lua reads `getItemChange(itemKey)` and the item it returns,
never a type.
