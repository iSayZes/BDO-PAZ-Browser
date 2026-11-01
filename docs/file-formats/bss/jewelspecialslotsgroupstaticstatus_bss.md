# `jewelspecialslotsgroupstaticstatus.bss` Format

## Purpose

The crystal groups each special crystal preset slot accepts: one row per
special slot with its list of [`jewelgroupstaticstatus.bss`](jewelgroupstaticstatus_bss.md)
group numbers. The crystal inventory window greys out a crystal whose group
the selected slot does not accept (`ToClient_IsJewelInSpecialGroup` in
`panel_window_jewelinven_all_1.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                     | Bytes | Records            | Row bytes |
| ------ | -------------- | ---------------------------------------- | ----- | ------------------ | --------- |
| 1      | 2089 and later | `jewelspecialslotsgroupstaticstatus.bss` | 69    | 7 Special Slot Row | 7         |

| Layout | File                                     | Known         | Unknown    |
| ------ | ---------------------------------------- | ------------- | ---------- |
| 1      | `jewelspecialslotsgroupstaticstatus.bss` | 69 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `aecb3e220336`  |
| 3482   | Layout 1 | `aecb3e220336`  |
| 3474   | Layout 1 | `aecb3e220336`  |
| 3473   | Layout 1 | `aecb3e220336`  |
| 3464   | Layout 1 | `aecb3e220336`  |
| 3458   | Layout 1 | `aecb3e220336`  |
| 3454   | Layout 1 | `aecb3e220336`  |
| 3444   | Layout 1 | `aecb3e220336`  |
| 3435   | Layout 1 | `aecb3e220336`  |
| 3426   | Layout 1 | `aecb3e220336`  |
| 3418   | Layout 1 | `aecb3e220336`  |
| 3412   | Layout 1 | `aecb3e220336`  |
| 3402   | Layout 1 | `aecb3e220336`  |
| 3396   | Layout 1 | `aecb3e220336`  |
| 3387   | Layout 1 | `aecb3e220336`  |
| 3381   | Layout 1 | `aecb3e220336`  |
| 3373   | Layout 1 | `aecb3e220336`  |
| 3364   | Layout 1 | `aecb3e220336`  |
| 3356   | Layout 1 | `aecb3e220336`  |
| 3349   | Layout 1 | `aecb3e220336`  |
| 3342   | Layout 1 | `aecb3e220336`  |
| 3335   | Layout 1 | `aecb3e220336`  |
| 3326   | Layout 1 | `aecb3e220336`  |
| 3321   | Layout 1 | `aecb3e220336`  |
| 3314   | Layout 1 | `aecb3e220336`  |
| 3303   | Layout 1 | `aecb3e220336`  |
| 3302   | Layout 1 | `aecb3e220336`  |
| 3293   | Layout 1 | `aecb3e220336`  |
| 3283   | Layout 1 | `aecb3e220336`  |
| 3275   | Layout 1 | `aecb3e220336`  |
| 3267   | Layout 1 | `aecb3e220336`  |
| 3258   | Layout 1 | `aecb3e220336`  |
| 3251   | Layout 1 | `aecb3e220336`  |
| 3242   | Layout 1 | `aecb3e220336`  |
| 3235   | Layout 1 | `aecb3e220336`  |
| 3229   | Layout 1 | `aecb3e220336`  |
| 3212   | Layout 1 | `aecb3e220336`  |
| 3203   | Layout 1 | `aecb3e220336`  |
| 3193   | Layout 1 | `aecb3e220336`  |
| 3186   | Layout 1 | `aecb3e220336`  |
| 3177   | Layout 1 | `aecb3e220336`  |
| 3169   | Layout 1 | `aecb3e220336`  |
| 3158   | Layout 1 | `aecb3e220336`  |
| 3151   | Layout 1 | `aecb3e220336`  |
| 3144   | Layout 1 | `aecb3e220336`  |
| 3133   | Layout 1 | `aecb3e220336`  |
| 3125   | Layout 1 | `aecb3e220336`  |
| 3118   | Layout 1 | `aecb3e220336`  |
| 3111   | Layout 1 | `aecb3e220336`  |
| 3103   | Layout 1 | `aecb3e220336`  |
| 3095   | Layout 1 | `aecb3e220336`  |
| 3086   | Layout 1 | `aecb3e220336`  |
| 3072   | Layout 1 | `aecb3e220336`  |
| 3062   | Layout 1 | `aecb3e220336`  |
| 3052   | Layout 1 | `aecb3e220336`  |
| 3045   | Layout 1 | `aecb3e220336`  |
| 3037   | Layout 1 | `aecb3e220336`  |
| 3030   | Layout 1 | `aecb3e220336`  |
| 3021   | Layout 1 | `aecb3e220336`  |
| 3012   | Layout 1 | `aecb3e220336`  |
| 3002   | Layout 1 | `aecb3e220336`  |
| 2995   | Layout 1 | `aecb3e220336`  |
| 2987   | Layout 1 | `aecb3e220336`  |
| 2978   | Layout 1 | `aecb3e220336`  |
| 2970   | Layout 1 | `aecb3e220336`  |
| 2959   | Layout 1 | `aecb3e220336`  |
| 2951   | Layout 1 | `aecb3e220336`  |
| 2942   | Layout 1 | `aecb3e220336`  |
| 2935   | Layout 1 | `aecb3e220336`  |
| 2932   | Layout 1 | `aecb3e220336`  |
| 2923   | Layout 1 | `aecb3e220336`  |
| 2919   | Layout 1 | `aecb3e220336`  |
| 2907   | Layout 1 | `aecb3e220336`  |
| 2900   | Layout 1 | `aecb3e220336`  |
| 2891   | Layout 1 | `aecb3e220336`  |
| 2882   | Layout 1 | `aecb3e220336`  |
| 2872   | Layout 1 | `aecb3e220336`  |
| 2863   | Layout 1 | `aecb3e220336`  |
| 2855   | Layout 1 | `aecb3e220336`  |
| 2849   | Layout 1 | `aecb3e220336`  |
| 2844   | Layout 1 | `aecb3e220336`  |
| 2834   | Layout 1 | `aecb3e220336`  |
| 2825   | Layout 1 | `aecb3e220336`  |
| 2819   | Layout 1 | `aecb3e220336`  |
| 2811   | Layout 1 | `aecb3e220336`  |
| 2803   | Layout 1 | `aecb3e220336`  |
| 2794   | Layout 1 | `aecb3e220336`  |
| 2783   | Layout 1 | `aecb3e220336`  |
| 2774   | Layout 1 | `aecb3e220336`  |
| 2765   | Layout 1 | `aecb3e220336`  |
| 2756   | Layout 1 | `aecb3e220336`  |
| 2750   | Layout 1 | `aecb3e220336`  |
| 2743   | Layout 1 | `aecb3e220336`  |
| 2736   | Layout 1 | `aecb3e220336`  |
| 2726   | Layout 1 | `aecb3e220336`  |
| 2717   | Layout 1 | `aecb3e220336`  |
| 2709   | Layout 1 | `aecb3e220336`  |
| 2703   | Layout 1 | `aecb3e220336`  |
| 2695   | Layout 1 | `aecb3e220336`  |
| 2684   | Layout 1 | `aecb3e220336`  |
| 2672   | Layout 1 | `aecb3e220336`  |
| 2665   | Layout 1 | `aecb3e220336`  |
| 2657   | Layout 1 | `aecb3e220336`  |
| 2649   | Layout 1 | `aecb3e220336`  |
| 2644   | Layout 1 | `aecb3e220336`  |
| 2637   | Layout 1 | `aecb3e220336`  |
| 2629   | Layout 1 | `aecb3e220336`  |
| 2619   | Layout 1 | `aecb3e220336`  |
| 2612   | Layout 1 | `aecb3e220336`  |
| 2606   | Layout 1 | `aecb3e220336`  |
| 2602   | Layout 1 | `aecb3e220336`  |
| 2601   | Layout 1 | `aecb3e220336`  |
| 2592   | Layout 1 | `aecb3e220336`  |
| 2583   | Layout 1 | `aecb3e220336`  |
| 2575   | Layout 1 | `aecb3e220336`  |
| 2567   | Layout 1 | `aecb3e220336`  |
| 2560   | Layout 1 | `aecb3e220336`  |
| 2553   | Layout 1 | `aecb3e220336`  |
| 2545   | Layout 1 | `aecb3e220336`  |
| 2538   | Layout 1 | `aecb3e220336`  |
| 2529   | Layout 1 | `aecb3e220336`  |
| 2519   | Layout 1 | `aecb3e220336`  |
| 2513   | Layout 1 | `aecb3e220336`  |
| 2510   | Layout 1 | `aecb3e220336`  |
| 2507   | Layout 1 | `aecb3e220336`  |
| 2503   | Layout 1 | `aecb3e220336`  |
| 2498   | Layout 1 | `aecb3e220336`  |
| 2492   | Layout 1 | `aecb3e220336`  |
| 2487   | Layout 1 | `aecb3e220336`  |
| 2480   | Layout 1 | `aecb3e220336`  |
| 2474   | Layout 1 | `aecb3e220336`  |
| 2468   | Layout 1 | `aecb3e220336`  |
| 2460   | Layout 1 | `aecb3e220336`  |
| 2453   | Layout 1 | `aecb3e220336`  |
| 2444   | Layout 1 | `aecb3e220336`  |
| 2438   | Layout 1 | `aecb3e220336`  |
| 2434   | Layout 1 | `aecb3e220336`  |
| 2429   | Layout 1 | `aecb3e220336`  |
| 2421   | Layout 1 | `aecb3e220336`  |
| 2414   | Layout 1 | `aecb3e220336`  |
| 2407   | Layout 1 | `aecb3e220336`  |
| 2401   | Layout 1 | `aecb3e220336`  |
| 2397   | Layout 1 | `aecb3e220336`  |
| 2393   | Layout 1 | `aecb3e220336`  |
| 2384   | Layout 1 | `aecb3e220336`  |
| 2378   | Layout 1 | `aecb3e220336`  |
| 2372   | Layout 1 | `aecb3e220336`  |
| 2358   | Layout 1 | `aecb3e220336`  |
| 2352   | Layout 1 | `aecb3e220336`  |
| 2347   | Layout 1 | `aecb3e220336`  |
| 2343   | Layout 1 | `aecb3e220336`  |
| 2335   | Layout 1 | `aecb3e220336`  |
| 2327   | Layout 1 | `aecb3e220336`  |
| 2324   | Layout 1 | `aecb3e220336`  |
| 2319   | Layout 1 | `aecb3e220336`  |
| 2313   | Layout 1 | `aecb3e220336`  |
| 2308   | Layout 1 | `aecb3e220336`  |
| 2302   | Layout 1 | `aecb3e220336`  |
| 2295   | Layout 1 | `aecb3e220336`  |
| 2290   | Layout 1 | `aecb3e220336`  |
| 2284   | Layout 1 | `aecb3e220336`  |
| 2276   | Layout 1 | `aecb3e220336`  |
| 2269   | Layout 1 | `aecb3e220336`  |
| 2259   | Layout 1 | `aecb3e220336`  |
| 2250   | Layout 1 | `aecb3e220336`  |
| 2243   | Layout 1 | `aecb3e220336`  |
| 2235   | Layout 1 | `aecb3e220336`  |
| 2229   | Layout 1 | `aecb3e220336`  |
| 2224   | Layout 1 | `aecb3e220336`  |
| 2218   | Layout 1 | `aecb3e220336`  |
| 2215   | Layout 1 | `aecb3e220336`  |
| 2207   | Layout 1 | `aecb3e220336`  |
| 2203   | Layout 1 | `aecb3e220336`  |
| 2196   | Layout 1 | `aecb3e220336`  |
| 2192   | Layout 1 | `aecb3e220336`  |
| 2189   | Layout 1 | `aecb3e220336`  |
| 2183   | Layout 1 | `aecb3e220336`  |
| 2179   | Layout 1 | `aecb3e220336`  |
| 2171   | Layout 1 | `aecb3e220336`  |
| 2163   | Layout 1 | `aecb3e220336`  |
| 2156   | Layout 1 | `aecb3e220336`  |
| 2151   | Layout 1 | `aecb3e220336`  |
| 2147   | Layout 1 | `aecb3e220336`  |
| 2142   | Layout 1 | `aecb3e220336`  |
| 2138   | Layout 1 | `aecb3e220336`  |
| 2134   | Layout 1 | `aecb3e220336`  |
| 2130   | Layout 1 | `aecb3e220336`  |
| 2122   | Layout 1 | `aecb3e220336`  |
| 2107   | Layout 1 | `aecb3e220336`  |
| 2098   | Layout 1 | `aecb3e220336`  |
| 2089   | Layout 1 | `aecb3e220336`  |
| 2081   | No file  | `aecb3e220336`  |
| 2073   | No file  | `aecb3e220336`  |
| 2067   | No file  | `aecb3e220336`  |
| 2063   | No file  | `aecb3e220336`  |
| 2059   | No file  | `aecb3e220336`  |
| 2052   | No file  | `aecb3e220336`  |
| 2044   | No file  | `aecb3e220336`  |
| 2039   | No file  | `aecb3e220336`  |
| 2032   | No file  | `aecb3e220336`  |
| 2025   | No file  | `aecb3e220336`  |
| 2011   | No file  | `aecb3e220336`  |
| 2005   | No file  | `aecb3e220336`  |
| 2000   | No file  | `aecb3e220336`  |
| 1996   | No file  | `aecb3e220336`  |
| 1991   | No file  | `aecb3e220336`  |
| 1985   | No file  | `aecb3e220336`  |
| 1980   | No file  | `aecb3e220336`  |
| 1969   | No file  | `aecb3e220336`  |
| 1964   | No file  | `aecb3e220336`  |
| 1958   | No file  | `aecb3e220336`  |
| 1950   | No file  | `aecb3e220336`  |
| 1945   | No file  | `aecb3e220336`  |
| 1937   | No file  | `aecb3e220336`  |
| 1933   | No file  | `aecb3e220336`  |
| 1927   | No file  | `aecb3e220336`  |
| 1921   | No file  | `aecb3e220336`  |
| 1914   | No file  | `aecb3e220336`  |
| 1908   | No file  | `aecb3e220336`  |
| 1897   | No file  | `aecb3e220336`  |
| 1892   | No file  | `aecb3e220336`  |
| 1886   | No file  | `aecb3e220336`  |
| 1881   | No file  | `aecb3e220336`  |
| 1871   | No file  | `aecb3e220336`  |
| 1866   | No file  | `aecb3e220336`  |
| 1862   | No file  | `aecb3e220336`  |
| 1854   | No file  | `aecb3e220336`  |
| 1846   | No file  | `aecb3e220336`  |
| 1838   | No file  | `aecb3e220336`  |
| 1832   | No file  | `aecb3e220336`  |
| 1826   | No file  | `aecb3e220336`  |
| 1822   | No file  | `aecb3e220336`  |
| 1818   | No file  | `aecb3e220336`  |
| 1804   | No file  | `aecb3e220336`  |
| 1794   | No file  | `aecb3e220336`  |
| 1790   | No file  | `aecb3e220336`  |
| 1784   | No file  | `aecb3e220336`  |
| 1774   | No file  | `aecb3e220336`  |
| 1771   | No file  | `aecb3e220336`  |
| 1762   | No file  | `aecb3e220336`  |
| 1759   | No file  | `aecb3e220336`  |
| 1754   | No file  | `aecb3e220336`  |
| 1749   | No file  | `aecb3e220336`  |
| 1743   | No file  | `aecb3e220336`  |
| 1737   | No file  | `aecb3e220336`  |
| 1731   | No file  | `aecb3e220336`  |
| 1725   | No file  | `aecb3e220336`  |
| 1717   | No file  | `aecb3e220336`  |
| 1710   | No file  | `aecb3e220336`  |
| 1704   | No file  | `aecb3e220336`  |
| 1698   | No file  | `aecb3e220336`  |
| 1690   | No file  | `aecb3e220336`  |
| 1685   | No file  | `aecb3e220336`  |
| 1680   | No file  | `aecb3e220336`  |
| 1674   | No file  | `aecb3e220336`  |
| 1668   | No file  | `aecb3e220336`  |
| 1659   | No file  | `aecb3e220336`  |
| 1649   | No file  | `aecb3e220336`  |
| 1642   | No file  | `aecb3e220336`  |
| 1636   | No file  | `aecb3e220336`  |
| 1628   | No file  | `aecb3e220336`  |
| 1622   | No file  | `aecb3e220336`  |
| 1614   | No file  | `aecb3e220336`  |
| 1608   | No file  | `aecb3e220336`  |
| 1602   | No file  | `aecb3e220336`  |
| 1598   | No file  | `aecb3e220336`  |
| 1594   | No file  | `aecb3e220336`  |
| 1590   | No file  | `aecb3e220336`  |
| 1587   | No file  | `aecb3e220336`  |
| 1584   | No file  | `aecb3e220336`  |
| 1579   | No file  | `aecb3e220336`  |
| 1572   | No file  | `aecb3e220336`  |
| 1565   | No file  | `aecb3e220336`  |
| 1559   | No file  | `aecb3e220336`  |
| 1554   | No file  | `aecb3e220336`  |
| 1547   | No file  | `aecb3e220336`  |
| 1537   | No file  | `aecb3e220336`  |
| 1529   | No file  | `aecb3e220336`  |
| 1524   | No file  | `aecb3e220336`  |
| 1519   | No file  | `aecb3e220336`  |
| 1509   | No file  | `aecb3e220336`  |
| 1506   | No file  | `aecb3e220336`  |
| 1504   | No file  | `aecb3e220336`  |
| 1500   | No file  | `aecb3e220336`  |
| 1493   | No file  | `aecb3e220336`  |
| 1489   | No file  | `aecb3e220336`  |
| 1485   | No file  | `aecb3e220336`  |
| 1481   | No file  | `aecb3e220336`  |
| 1474   | No file  | `aecb3e220336`  |
| 1466   | No file  | `aecb3e220336`  |
| 1462   | No file  | `aecb3e220336`  |
| 1459   | No file  | `aecb3e220336`  |
| 1453   | No file  | `aecb3e220336`  |
| 1450   | No file  | `aecb3e220336`  |
| 1445   | No file  | `aecb3e220336`  |
| 1439   | No file  | `aecb3e220336`  |
| 1433   | No file  | `aecb3e220336`  |
| 1430   | No file  | `aecb3e220336`  |
| 1426   | No file  | `aecb3e220336`  |
| 1421   | No file  | `aecb3e220336`  |
| 1417   | No file  | `aecb3e220336`  |
| 1416   | No file  | `aecb3e220336`  |
| 1409   | No file  | `aecb3e220336`  |
| 1405   | No file  | `aecb3e220336`  |
| 1401   | No file  | `aecb3e220336`  |
| 1396   | No file  | `aecb3e220336`  |
| 1391   | No file  | `aecb3e220336`  |
| 1390   | No file  | `aecb3e220336`  |
| 1386   | No file  | `aecb3e220336`  |
| 1381   | No file  | `aecb3e220336`  |
| 1379   | No file  | `aecb3e220336`  |
| 1372   | No file  | `aecb3e220336`  |
| 1366   | No file  | `aecb3e220336`  |
| 1364   | No file  | `aecb3e220336`  |
| 1363   | No file  | `aecb3e220336`  |
| 1360   | No file  | `aecb3e220336`  |
| 1358   | No file  | `aecb3e220336`  |
| 1355   | No file  | `aecb3e220336`  |
| 1351   | No file  | `aecb3e220336`  |
| 1348   | No file  | `aecb3e220336`  |
| 1346   | No file  | `aecb3e220336`  |
| 1341   | No file  | `aecb3e220336`  |
| 1340   | No file  | `aecb3e220336`  |
| 1338   | No file  | `aecb3e220336`  |
| 1335   | No file  | `aecb3e220336`  |
| 1333   | No file  | `aecb3e220336`  |
| 1329   | No file  | `aecb3e220336`  |
| 1327   | No file  | `aecb3e220336`  |
| 1324   | No file  | `aecb3e220336`  |
| 1321   | No file  | `aecb3e220336`  |
| 1319   | No file  | `aecb3e220336`  |
| 1318   | No file  | `aecb3e220336`  |
| 1316   | No file  | `aecb3e220336`  |
| 1313   | No file  | `aecb3e220336`  |
| 1311   | No file  | `aecb3e220336`  |
| 1309   | No file  | `aecb3e220336`  |
| 1304   | No file  | `aecb3e220336`  |
| 1292   | No file  | `aecb3e220336`  |
| 1286   | No file  | `aecb3e220336`  |
| 1280   | No file  | `aecb3e220336`  |
| 1276   | No file  | `aecb3e220336`  |
| 1267   | No file  | `aecb3e220336`  |
| 1261   | No file  | `aecb3e220336`  |
| 1256   | No file  | `aecb3e220336`  |
| 1250   | No file  | `aecb3e220336`  |
| 1246   | No file  | `aecb3e220336`  |
| 1239   | No file  | `aecb3e220336`  |
| 1230   | No file  | `aecb3e220336`  |
| 1226   | No file  | `aecb3e220336`  |
| 1220   | No file  | `aecb3e220336`  |
| 1217   | No file  | `aecb3e220336`  |
| 1211   | No file  | `aecb3e220336`  |
| 1210   | No file  | `aecb3e220336`  |
| 1208   | No file  | `aecb3e220336`  |
| 1203   | No file  | `aecb3e220336`  |
| 1197   | No file  | `aecb3e220336`  |
| 1194   | No file  | `aecb3e220336`  |
| 1192   | No file  | `aecb3e220336`  |
| 1187   | No file  | `aecb3e220336`  |
| 1183   | No file  | `aecb3e220336`  |
| 1177   | No file  | `aecb3e220336`  |
| 1173   | No file  | `aecb3e220336`  |
| 1167   | No file  | `aecb3e220336`  |
| 1164   | No file  | `aecb3e220336`  |
| 1156   | No file  | `aecb3e220336`  |
| 1149   | No file  | `aecb3e220336`  |
| 1144   | No file  | `aecb3e220336`  |
| 1137   | No file  | `aecb3e220336`  |
| 1132   | No file  | `aecb3e220336`  |
| 1127   | No file  | `aecb3e220336`  |
| 1122   | No file  | `aecb3e220336`  |
| 1118   | No file  | `aecb3e220336`  |
| 1114   | No file  | `aecb3e220336`  |
| 1109   | No file  | `aecb3e220336`  |
| 1102   | No file  | `aecb3e220336`  |
| 1096   | No file  | `aecb3e220336`  |
| 1088   | No file  | `aecb3e220336`  |
| 1081   | No file  | `aecb3e220336`  |
| 1076   | No file  | `aecb3e220336`  |
| 1069   | No file  | `aecb3e220336`  |
| 1064   | No file  | `aecb3e220336`  |
| 1058   | No file  | `aecb3e220336`  |
| 1051   | No file  | `aecb3e220336`  |
| 1044   | No file  | `aecb3e220336`  |
| 1036   | No file  | `aecb3e220336`  |
| 1026   | No file  | `aecb3e220336`  |
| 1016   | No file  | `aecb3e220336`  |
| 1009   | No file  | `aecb3e220336`  |
| 1005   | No file  | `aecb3e220336`  |
| 1000   | No file  | `aecb3e220336`  |
| 998    | No file  | `aecb3e220336`  |
| 990    | No file  | `aecb3e220336`  |
| 979    | No file  | `aecb3e220336`  |
| 972    | No file  | `aecb3e220336`  |
| 963    | No file  | `aecb3e220336`  |
| 955    | No file  | `aecb3e220336`  |
| 946    | No file  | `aecb3e220336`  |
| 938    | No file  | `aecb3e220336`  |
| 927    | No file  | `aecb3e220336`  |
| 911    | No file  | `aecb3e220336`  |
| 904    | No file  | `aecb3e220336`  |
| 899    | No file  | `aecb3e220336`  |
| 894    | No file  | `aecb3e220336`  |
| 885    | No file  | `aecb3e220336`  |
| 879    | No file  | `aecb3e220336`  |
| 872    | No file  | `aecb3e220336`  |
| 864    | No file  | `aecb3e220336`  |
| 855    | No file  | `aecb3e220336`  |
| 853    | No file  | `aecb3e220336`  |
| 845    | No file  | `aecb3e220336`  |
| 837    | No file  | `aecb3e220336`  |
| 829    | No file  | `aecb3e220336`  |
| 822    | No file  | `aecb3e220336`  |
| 814    | No file  | `aecb3e220336`  |
| 805    | No file  | `aecb3e220336`  |
| 794    | No file  | `aecb3e220336`  |
| 787    | No file  | `aecb3e220336`  |
| 780    | No file  | `aecb3e220336`  |
| 771    | No file  | `aecb3e220336`  |
| 760    | No file  | `aecb3e220336`  |
| 748    | No file  | `aecb3e220336`  |
| 741    | No file  | `aecb3e220336`  |
| 736    | No file  | `aecb3e220336`  |
| 731    | No file  | `aecb3e220336`  |
| 723    | No file  | `aecb3e220336`  |
| 711    | No file  | `aecb3e220336`  |
| 707    | No file  | `aecb3e220336`  |
| 697    | No file  | `aecb3e220336`  |
| 689    | No file  | `aecb3e220336`  |
| 683    | No file  | `aecb3e220336`  |
| 678    | No file  | `aecb3e220336`  |
| 670    | No file  | `aecb3e220336`  |
| 661    | No file  | `aecb3e220336`  |
| 656    | No file  | `aecb3e220336`  |
| 652    | No file  | `aecb3e220336`  |
| 643    | No file  | `aecb3e220336`  |
| 637    | No file  | `aecb3e220336`  |
| 630    | No file  | `aecb3e220336`  |
| 627    | No file  | `aecb3e220336`  |
| 621    | No file  | `aecb3e220336`  |
| 617    | No file  | `aecb3e220336`  |
| 615    | No file  | `aecb3e220336`  |
| 606    | No file  | `aecb3e220336`  |
| 599    | No file  | `aecb3e220336`  |
| 592    | No file  | `aecb3e220336`  |
| 586    | No file  | `aecb3e220336`  |
| 577    | No file  | `aecb3e220336`  |
| 569    | No file  | `aecb3e220336`  |
| 561    | No file  | `aecb3e220336`  |
| 554    | No file  | `aecb3e220336`  |
| 542    | No file  | `aecb3e220336`  |
| 532    | No file  | `aecb3e220336`  |
| 531    | No file  | `aecb3e220336`  |
| 526    | No file  | `aecb3e220336`  |
| 521    | No file  | `aecb3e220336`  |
| 517    | No file  | `aecb3e220336`  |
| 510    | No file  | `aecb3e220336`  |
| 508    | No file  | `aecb3e220336`  |
| 504    | No file  | `aecb3e220336`  |
| 497    | No file  | `aecb3e220336`  |
| 491    | No file  | `aecb3e220336`  |
| 485    | No file  | `aecb3e220336`  |
| 478    | No file  | `aecb3e220336`  |
| 472    | No file  | `aecb3e220336`  |
| 466    | No file  | `aecb3e220336`  |
| 457    | No file  | `aecb3e220336`  |
| 452    | No file  | `aecb3e220336`  |
| 449    | No file  | `aecb3e220336`  |
| 435    | No file  | `aecb3e220336`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                            |
| ---------------------------- | -------- | ----------------------------------------------- |
| `jewelgroupstaticstatus.bss` | Optional | Group limit and Korean name for the LOC lookup  |
| `languagedata_en.loc`        | Optional | Group names (type 121) and equipment slot names |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of variable rows, followed by the counted string table and
8-byte trailer of [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table is empty on client 3473.

| Offset              | Type                    | Field              | Notes                            |
| ------------------- | ----------------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]                 | magic              | ASCII `PABR`                     |
| `+0x04`             | u32                     | count              | Number of rows; 7 on client 3473 |
| `+0x08`             | Special Slot Row[count] | rows               | See Special Slot Row             |
| `rows+0x00`         | String Table            | string_table       | No strings on client 3473        |
| `string_table+0x00` | u32                     | string_table_start | Where the rows end               |
| `string_table+0x04` | u32                     | zero               | Always `0`                       |

The rows are not sorted by slot.

### Special Slot Row (variable: 5 bytes + groups)

| Offset  | Type              | Field       | Notes                                                    |
| ------- | ----------------- | ----------- | -------------------------------------------------------- |
| `+0x00` | u8                | slot        | Special preset slot, see Special Slots                   |
| `+0x01` | u32               | group_count | Number of `groups`; 1 on every row (client 3473)         |
| `+0x05` | u16[group_count]  | groups      | Accepted crystal groups, `jewelgroupstaticstatus.bss` `group` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Special Slots

A crystal preset has 23 slots, 0 to 22. Slots 0 to 11 are the normal ones,
12 to 22 the `__eJewelSpecialSlot*` ones. The equipment slot is the one the
preset window reads the item from (`panel_window_jewelpreset_all_1.luac`).
Rows on client 3473:

| Slot | `__eJewelSpecialSlot*` | Equipment slot          | Groups                |
| ---- | ---------------------- | ----------------------- | --------------------- |
| 12   | AwakenWeapon1          | 29 AwakenWeapon         | No row                |
| 13   | AwakenWeapon2          | 29 AwakenWeapon         | No row                |
| 14   | PearlAvatarChest       | 14 AvatarChest          | 101 Ancient Spirit    |
| 15   | 1MorningLand           | None                    | No row                |
| 16   | 2MorningLand           | None                    | No row                |
| 17   | Necklace               | 7 Necklace              | 103 Dawn              |
| 18   | Ring1                  | 8 Ring1                 | 103 Dawn              |
| 19   | Ring2                  | 9 Ring2                 | 103 Dawn              |
| 20   | Earing1                | 10 Earing1              | 103 Dawn              |
| 21   | Earing2                | 11 Earing2              | 103 Dawn              |
| 22   | Belt                   | 12 Belt                 | 103 Dawn              |

The numbers come from the client Lua and UI XML, and match where the
slots unlock in game:

- `panel_window_jewelpreset_all.xml` has 12 `Static_NormalSlotBg_NN` and
  11 `Static_SpecialSlotBg_NN` controls. `PaGlobal_JewelPreset:initialize()`
  gives slot `idx` below `__eJewelSpecialSlotAwakenWeapon1` the control
  `Static_NormalSlotBg_<idx + 1>` and the others `Static_SpecialSlotBg_<idx - 11>`,
  with a leading `0` below `__eJewelSpecialSlotEaring2`. Every slot finds
  a control, and all 23 controls get a slot, only with `AwakenWeapon1` = 12
  and `Earing2` = 21.
- The other nine values follow the order of `_lockSlotTooltip` in
  `panel_window_jewelpreset_all.luac`, which lists the eleven slots from
  `AwakenWeapon1` to `Belt`, with `Earing2` tenth.
- The control positions in the XML (`Pan`, all `Center Top`, 85 x 85) put
  each slot where Black Desert Foundry's
  [crystal socket guide](https://www.blackdesertfoundry.com/crystal-sockets-guide/)
  places its unlock: `_01` (12) top left at `-256 20`, unlocked by a Storm
  Devoured or Fiery Awakening Weapon; `_02` (13) top right at `256 20`,
  Fiery Awakening Weapon only; `_03` (14) in the middle at `0 266`, the
  outfit; `_04` (15) and `_05` (16) bottom left and right at `-256 510` and
  `256 510`, one Kkebiwater each from the Land of the Morning Light quests;
  `_06` to `_11` (17 to 22) the bottom row at `y 620`, Kharazad
  accessories. Any other order of 13, 15 and 16 puts a Morning Land slot
  top right.
- The rows agree for 14 and 17 to 22: the Ancient Spirit crystals are
  transfused into "a crystal outfit socket" and the Dawn crystals into "an
  accessory's crystal socket" (item descriptions, LOC type 0 `str_id4` 1).
  The preset window lists the effect of a crystal in the necklace, ring,
  earring and belt slots only when the equipped item's
  `isKarazardAccessory()` is true.
- In game, the outfit slot takes only Ancient Spirit crystals, the six
  bottom slots take only Dawn crystals while Kharazad accessories are
  equipped, and the awakening weapon and Morning Land slots take any
  crystal once unlocked.

## Notes

- The rows hold only the special slots that limit their groups. Slots 12,
  13, 15 and 16 have no row on client 3473 and take any crystal; their
  unlock condition (awakening weapon, Kkebiwater) is not in this file.
- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `jewelspecialslotsgroupstaticstatus.bss`. The field names come from the
  Lua (`ToClient_IsJewelInSpecialGroup`, `__eJewelSpecialSlot*`).
