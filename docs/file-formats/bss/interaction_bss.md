# `interaction.bss` Format

## Purpose

Interactions set on single characters, one row per interaction: the
interaction type, a value the interaction executes and the character key. On client
3474 the file has 2 rows, both `InteractionType_Awake` (`61`) on the two
Mirumok Offin characters (`23751` Mirumok Watcher Offin, `23767` Mirumok
Destroyer Offin) with the value `40414`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File              | Bytes | Records | Row bytes |
| ------ | ------------- | ----------------- | ----- | ------- | --------- |
| 1      | 805 and later | `interaction.bss` | 42    | 2 Row   | 11        |

| Layout | File              | Known        | Unknown    |
| ------ | ----------------- | ------------ | ---------- |
| 1      | `interaction.bss` | 40 B (95.2%) | 2 B (4.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `50873c1d1049`  |
| 3482   | Layout 1             | `50873c1d1049`  |
| 3474   | Layout 1             | `50873c1d1049`  |
| 3473   | Layout 1             | `50873c1d1049`  |
| 3464   | Layout 1             | `50873c1d1049`  |
| 3458   | Layout 1             | `50873c1d1049`  |
| 3454   | Layout 1             | `50873c1d1049`  |
| 3444   | Layout 1             | `50873c1d1049`  |
| 3435   | Layout 1             | `50873c1d1049`  |
| 3426   | Layout 1             | `50873c1d1049`  |
| 3418   | Layout 1             | `50873c1d1049`  |
| 3412   | Layout 1             | `50873c1d1049`  |
| 3402   | Layout 1             | `50873c1d1049`  |
| 3396   | Layout 1             | `50873c1d1049`  |
| 3387   | Layout 1             | `50873c1d1049`  |
| 3381   | Layout 1             | `50873c1d1049`  |
| 3373   | Layout 1             | `50873c1d1049`  |
| 3364   | Layout 1             | `50873c1d1049`  |
| 3356   | Layout 1             | `50873c1d1049`  |
| 3349   | Layout 1             | `50873c1d1049`  |
| 3342   | Layout 1             | `50873c1d1049`  |
| 3335   | Layout 1             | `50873c1d1049`  |
| 3326   | Layout 1             | `50873c1d1049`  |
| 3321   | Layout 1             | `50873c1d1049`  |
| 3314   | Layout 1             | `50873c1d1049`  |
| 3303   | Layout 1             | `50873c1d1049`  |
| 3302   | Layout 1             | `50873c1d1049`  |
| 3293   | Layout 1             | `50873c1d1049`  |
| 3283   | Layout 1             | `50873c1d1049`  |
| 3275   | Layout 1             | `50873c1d1049`  |
| 3267   | Layout 1             | `50873c1d1049`  |
| 3258   | Layout 1             | `50873c1d1049`  |
| 3251   | Layout 1             | `50873c1d1049`  |
| 3242   | Layout 1             | `50873c1d1049`  |
| 3235   | Layout 1             | `50873c1d1049`  |
| 3229   | Layout 1             | `50873c1d1049`  |
| 3212   | Layout 1             | `50873c1d1049`  |
| 3203   | Layout 1             | `50873c1d1049`  |
| 3193   | Layout 1             | `50873c1d1049`  |
| 3186   | Layout 1             | `50873c1d1049`  |
| 3177   | Layout 1             | `50873c1d1049`  |
| 3169   | Layout 1             | `50873c1d1049`  |
| 3158   | Layout 1             | `50873c1d1049`  |
| 3151   | Layout 1             | `50873c1d1049`  |
| 3144   | Layout 1             | `50873c1d1049`  |
| 3133   | Layout 1             | `50873c1d1049`  |
| 3125   | Layout 1             | `50873c1d1049`  |
| 3118   | Layout 1             | `50873c1d1049`  |
| 3111   | Layout 1             | `50873c1d1049`  |
| 3103   | Layout 1             | `50873c1d1049`  |
| 3095   | Layout 1             | `50873c1d1049`  |
| 3086   | Layout 1             | `50873c1d1049`  |
| 3072   | Layout 1             | `50873c1d1049`  |
| 3062   | Layout 1             | `50873c1d1049`  |
| 3052   | Layout 1             | `50873c1d1049`  |
| 3045   | Layout 1             | `50873c1d1049`  |
| 3037   | Layout 1             | `50873c1d1049`  |
| 3030   | Layout 1             | `50873c1d1049`  |
| 3021   | Layout 1             | `50873c1d1049`  |
| 3012   | Layout 1             | `50873c1d1049`  |
| 3002   | Layout 1             | `50873c1d1049`  |
| 2995   | Layout 1             | `50873c1d1049`  |
| 2987   | Layout 1             | `50873c1d1049`  |
| 2978   | Layout 1             | `50873c1d1049`  |
| 2970   | Layout 1             | `50873c1d1049`  |
| 2959   | Layout 1             | `50873c1d1049`  |
| 2951   | Layout 1             | `50873c1d1049`  |
| 2942   | Layout 1             | `50873c1d1049`  |
| 2935   | Layout 1             | `50873c1d1049`  |
| 2932   | Layout 1             | `50873c1d1049`  |
| 2923   | Layout 1             | `50873c1d1049`  |
| 2919   | Layout 1             | `50873c1d1049`  |
| 2907   | Layout 1             | `50873c1d1049`  |
| 2900   | Layout 1             | `50873c1d1049`  |
| 2891   | Layout 1             | `50873c1d1049`  |
| 2882   | Layout 1             | `50873c1d1049`  |
| 2872   | Layout 1             | `50873c1d1049`  |
| 2863   | Layout 1             | `50873c1d1049`  |
| 2855   | Layout 1             | `50873c1d1049`  |
| 2849   | Layout 1             | `50873c1d1049`  |
| 2844   | Layout 1             | `50873c1d1049`  |
| 2834   | Layout 1             | `50873c1d1049`  |
| 2825   | Layout 1             | `50873c1d1049`  |
| 2819   | Layout 1             | `50873c1d1049`  |
| 2811   | Layout 1             | `50873c1d1049`  |
| 2803   | Layout 1             | `50873c1d1049`  |
| 2794   | Layout 1             | `50873c1d1049`  |
| 2783   | Layout 1             | `50873c1d1049`  |
| 2774   | Layout 1             | `50873c1d1049`  |
| 2765   | Layout 1             | `50873c1d1049`  |
| 2756   | Layout 1             | `50873c1d1049`  |
| 2750   | Layout 1             | `50873c1d1049`  |
| 2743   | Layout 1             | `50873c1d1049`  |
| 2736   | Layout 1             | `50873c1d1049`  |
| 2726   | Layout 1             | `50873c1d1049`  |
| 2717   | Layout 1             | `50873c1d1049`  |
| 2709   | Layout 1             | `50873c1d1049`  |
| 2703   | Layout 1             | `50873c1d1049`  |
| 2695   | Layout 1             | `50873c1d1049`  |
| 2684   | Layout 1             | `50873c1d1049`  |
| 2672   | Layout 1             | `50873c1d1049`  |
| 2665   | Layout 1             | `50873c1d1049`  |
| 2657   | Layout 1             | `50873c1d1049`  |
| 2649   | Layout 1             | `50873c1d1049`  |
| 2644   | Layout 1             | `50873c1d1049`  |
| 2637   | Layout 1             | `50873c1d1049`  |
| 2629   | Layout 1             | `50873c1d1049`  |
| 2619   | Layout 1             | `50873c1d1049`  |
| 2612   | Layout 1             | `50873c1d1049`  |
| 2606   | Layout 1             | `50873c1d1049`  |
| 2602   | Layout 1             | `50873c1d1049`  |
| 2601   | Layout 1             | `50873c1d1049`  |
| 2592   | Layout 1             | `50873c1d1049`  |
| 2583   | Layout 1             | `50873c1d1049`  |
| 2575   | Layout 1             | `50873c1d1049`  |
| 2567   | Layout 1             | `50873c1d1049`  |
| 2560   | Layout 1             | `50873c1d1049`  |
| 2553   | Layout 1             | `50873c1d1049`  |
| 2545   | Layout 1             | `50873c1d1049`  |
| 2538   | Layout 1             | `50873c1d1049`  |
| 2529   | Layout 1             | `50873c1d1049`  |
| 2519   | Layout 1             | `50873c1d1049`  |
| 2513   | Layout 1             | `50873c1d1049`  |
| 2510   | Layout 1             | `50873c1d1049`  |
| 2507   | Layout 1             | `50873c1d1049`  |
| 2503   | Layout 1             | `50873c1d1049`  |
| 2498   | Layout 1             | `50873c1d1049`  |
| 2492   | Layout 1             | `50873c1d1049`  |
| 2487   | Layout 1             | `50873c1d1049`  |
| 2480   | Layout 1             | `50873c1d1049`  |
| 2474   | Layout 1             | `50873c1d1049`  |
| 2468   | Layout 1             | `50873c1d1049`  |
| 2460   | Layout 1             | `50873c1d1049`  |
| 2453   | Layout 1             | `50873c1d1049`  |
| 2444   | Layout 1             | `50873c1d1049`  |
| 2438   | Layout 1             | `50873c1d1049`  |
| 2434   | Layout 1             | `50873c1d1049`  |
| 2429   | Layout 1             | `50873c1d1049`  |
| 2421   | Layout 1             | `50873c1d1049`  |
| 2414   | Layout 1             | `50873c1d1049`  |
| 2407   | Layout 1             | `50873c1d1049`  |
| 2401   | Layout 1             | `50873c1d1049`  |
| 2397   | Layout 1             | `50873c1d1049`  |
| 2393   | Layout 1             | `50873c1d1049`  |
| 2384   | Layout 1             | `50873c1d1049`  |
| 2378   | Layout 1             | `50873c1d1049`  |
| 2372   | Layout 1             | `50873c1d1049`  |
| 2358   | Layout 1             | `50873c1d1049`  |
| 2352   | Layout 1             | `50873c1d1049`  |
| 2347   | Layout 1             | `50873c1d1049`  |
| 2343   | Layout 1             | `50873c1d1049`  |
| 2335   | Layout 1             | `50873c1d1049`  |
| 2327   | Layout 1             | `50873c1d1049`  |
| 2324   | Layout 1             | `50873c1d1049`  |
| 2319   | Layout 1             | `50873c1d1049`  |
| 2313   | Layout 1             | `50873c1d1049`  |
| 2308   | Layout 1             | `50873c1d1049`  |
| 2302   | Layout 1             | `50873c1d1049`  |
| 2295   | Layout 1             | `50873c1d1049`  |
| 2290   | Layout 1             | `50873c1d1049`  |
| 2284   | Layout 1             | `50873c1d1049`  |
| 2276   | Layout 1             | `50873c1d1049`  |
| 2269   | Layout 1             | `50873c1d1049`  |
| 2259   | Layout 1             | `50873c1d1049`  |
| 2250   | Layout 1             | `50873c1d1049`  |
| 2243   | Layout 1             | `50873c1d1049`  |
| 2235   | Layout 1             | `50873c1d1049`  |
| 2229   | Layout 1             | `50873c1d1049`  |
| 2224   | Layout 1             | `50873c1d1049`  |
| 2218   | Layout 1             | `50873c1d1049`  |
| 2215   | Layout 1             | `50873c1d1049`  |
| 2207   | Layout 1             | `50873c1d1049`  |
| 2203   | Layout 1             | `50873c1d1049`  |
| 2196   | Layout 1             | `50873c1d1049`  |
| 2192   | Layout 1             | `50873c1d1049`  |
| 2189   | Layout 1             | `50873c1d1049`  |
| 2183   | Layout 1             | `50873c1d1049`  |
| 2179   | Layout 1             | `50873c1d1049`  |
| 2171   | Layout 1             | `50873c1d1049`  |
| 2163   | Layout 1             | `50873c1d1049`  |
| 2156   | Layout 1             | `50873c1d1049`  |
| 2151   | Layout 1             | `50873c1d1049`  |
| 2147   | Layout 1             | `50873c1d1049`  |
| 2142   | Layout 1             | `50873c1d1049`  |
| 2138   | Layout 1             | `50873c1d1049`  |
| 2134   | Layout 1             | `50873c1d1049`  |
| 2130   | Layout 1             | `50873c1d1049`  |
| 2122   | Layout 1             | `50873c1d1049`  |
| 2107   | Layout 1             | `50873c1d1049`  |
| 2098   | Layout 1             | `50873c1d1049`  |
| 2089   | Layout 1             | `50873c1d1049`  |
| 2081   | Layout 1             | `50873c1d1049`  |
| 2073   | Layout 1             | `50873c1d1049`  |
| 2067   | Layout 1             | `50873c1d1049`  |
| 2063   | Layout 1             | `50873c1d1049`  |
| 2059   | Layout 1             | `50873c1d1049`  |
| 2052   | Layout 1             | `50873c1d1049`  |
| 2044   | Layout 1             | `50873c1d1049`  |
| 2039   | Layout 1             | `50873c1d1049`  |
| 2032   | Layout 1             | `50873c1d1049`  |
| 2025   | Layout 1             | `50873c1d1049`  |
| 2011   | Layout 1             | `50873c1d1049`  |
| 2005   | Layout 1             | `50873c1d1049`  |
| 2000   | Layout 1             | `50873c1d1049`  |
| 1996   | Layout 1             | `50873c1d1049`  |
| 1991   | Layout 1             | `50873c1d1049`  |
| 1985   | Layout 1             | `50873c1d1049`  |
| 1980   | Layout 1             | `50873c1d1049`  |
| 1969   | Layout 1             | `50873c1d1049`  |
| 1964   | Layout 1             | `50873c1d1049`  |
| 1958   | Layout 1             | `50873c1d1049`  |
| 1950   | Layout 1             | `50873c1d1049`  |
| 1945   | Layout 1             | `50873c1d1049`  |
| 1937   | Layout 1             | `50873c1d1049`  |
| 1933   | Layout 1             | `50873c1d1049`  |
| 1927   | Layout 1             | `50873c1d1049`  |
| 1921   | Layout 1             | `50873c1d1049`  |
| 1914   | Layout 1             | `50873c1d1049`  |
| 1908   | Layout 1             | `50873c1d1049`  |
| 1897   | Layout 1             | `50873c1d1049`  |
| 1892   | Layout 1             | `50873c1d1049`  |
| 1886   | Layout 1             | `50873c1d1049`  |
| 1881   | Layout 1             | `50873c1d1049`  |
| 1871   | Layout 1             | `50873c1d1049`  |
| 1866   | Layout 1             | `50873c1d1049`  |
| 1862   | Layout 1             | `50873c1d1049`  |
| 1854   | Layout 1             | `50873c1d1049`  |
| 1846   | Layout 1             | `50873c1d1049`  |
| 1838   | Layout 1             | `50873c1d1049`  |
| 1832   | Layout 1             | `50873c1d1049`  |
| 1826   | Layout 1             | `50873c1d1049`  |
| 1822   | Layout 1             | `50873c1d1049`  |
| 1818   | Layout 1             | `50873c1d1049`  |
| 1804   | Layout 1             | `50873c1d1049`  |
| 1794   | Layout 1             | `50873c1d1049`  |
| 1790   | Layout 1             | `50873c1d1049`  |
| 1784   | Layout 1             | `50873c1d1049`  |
| 1774   | Layout 1             | `50873c1d1049`  |
| 1771   | Layout 1             | `50873c1d1049`  |
| 1762   | Layout 1             | `50873c1d1049`  |
| 1759   | Layout 1             | `50873c1d1049`  |
| 1754   | Layout 1             | `50873c1d1049`  |
| 1749   | Layout 1             | `50873c1d1049`  |
| 1743   | Layout 1             | `50873c1d1049`  |
| 1737   | Layout 1             | `50873c1d1049`  |
| 1731   | Layout 1             | `50873c1d1049`  |
| 1725   | Layout 1             | `50873c1d1049`  |
| 1717   | Layout 1             | `50873c1d1049`  |
| 1710   | Layout 1             | `50873c1d1049`  |
| 1704   | Layout 1             | `50873c1d1049`  |
| 1698   | Layout 1             | `50873c1d1049`  |
| 1690   | Layout 1             | `50873c1d1049`  |
| 1685   | Layout 1             | `50873c1d1049`  |
| 1680   | Layout 1             | `50873c1d1049`  |
| 1674   | Layout 1             | `50873c1d1049`  |
| 1668   | Layout 1             | `50873c1d1049`  |
| 1659   | Layout 1             | `50873c1d1049`  |
| 1649   | Layout 1             | `50873c1d1049`  |
| 1642   | Layout 1             | `50873c1d1049`  |
| 1636   | Layout 1             | `50873c1d1049`  |
| 1628   | Layout 1             | `50873c1d1049`  |
| 1622   | Layout 1             | `50873c1d1049`  |
| 1614   | Layout 1             | `50873c1d1049`  |
| 1608   | Layout 1             | `50873c1d1049`  |
| 1602   | Layout 1             | `50873c1d1049`  |
| 1598   | Layout 1             | `50873c1d1049`  |
| 1594   | Layout 1             | `50873c1d1049`  |
| 1590   | Layout 1             | `50873c1d1049`  |
| 1587   | Layout 1             | `50873c1d1049`  |
| 1584   | Layout 1             | `50873c1d1049`  |
| 1579   | Layout 1             | `50873c1d1049`  |
| 1572   | Layout 1             | `50873c1d1049`  |
| 1565   | Layout 1             | `50873c1d1049`  |
| 1559   | Layout 1             | `50873c1d1049`  |
| 1554   | Layout 1             | `50873c1d1049`  |
| 1547   | Layout 1             | `50873c1d1049`  |
| 1537   | Layout 1             | `50873c1d1049`  |
| 1529   | Layout 1             | `50873c1d1049`  |
| 1524   | Layout 1             | `50873c1d1049`  |
| 1519   | Layout 1             | `50873c1d1049`  |
| 1509   | Layout 1             | `50873c1d1049`  |
| 1506   | Layout 1             | `50873c1d1049`  |
| 1504   | Layout 1             | `50873c1d1049`  |
| 1500   | Layout 1             | `50873c1d1049`  |
| 1493   | Layout 1             | `50873c1d1049`  |
| 1489   | Layout 1             | `50873c1d1049`  |
| 1485   | Layout 1             | `50873c1d1049`  |
| 1481   | Layout 1             | `50873c1d1049`  |
| 1474   | Layout 1             | `50873c1d1049`  |
| 1466   | Layout 1             | `50873c1d1049`  |
| 1462   | Layout 1             | `50873c1d1049`  |
| 1459   | Layout 1             | `50873c1d1049`  |
| 1453   | Layout 1             | `50873c1d1049`  |
| 1450   | Layout 1             | `50873c1d1049`  |
| 1445   | Layout 1             | `50873c1d1049`  |
| 1439   | Layout 1             | `50873c1d1049`  |
| 1433   | Layout 1             | `50873c1d1049`  |
| 1430   | Layout 1             | `50873c1d1049`  |
| 1426   | Layout 1             | `50873c1d1049`  |
| 1421   | Layout 1             | `50873c1d1049`  |
| 1417   | Layout 1             | `50873c1d1049`  |
| 1416   | Layout 1             | `50873c1d1049`  |
| 1409   | Layout 1             | `50873c1d1049`  |
| 1405   | Layout 1             | `50873c1d1049`  |
| 1401   | Layout 1             | `50873c1d1049`  |
| 1396   | Layout 1             | `50873c1d1049`  |
| 1391   | Layout 1             | `50873c1d1049`  |
| 1390   | Layout 1             | `50873c1d1049`  |
| 1386   | Layout 1             | `50873c1d1049`  |
| 1381   | Layout 1             | `50873c1d1049`  |
| 1379   | Layout 1             | `50873c1d1049`  |
| 1372   | Layout 1             | `50873c1d1049`  |
| 1366   | Layout 1             | `50873c1d1049`  |
| 1364   | Layout 1             | `50873c1d1049`  |
| 1363   | Layout 1             | `50873c1d1049`  |
| 1360   | Layout 1             | `50873c1d1049`  |
| 1358   | Layout 1             | `50873c1d1049`  |
| 1355   | Layout 1             | `50873c1d1049`  |
| 1351   | Layout 1             | `50873c1d1049`  |
| 1348   | Layout 1             | `50873c1d1049`  |
| 1346   | Layout 1             | `50873c1d1049`  |
| 1341   | Layout 1             | `50873c1d1049`  |
| 1340   | Layout 1             | `50873c1d1049`  |
| 1338   | Layout 1             | `50873c1d1049`  |
| 1335   | Layout 1             | `50873c1d1049`  |
| 1333   | Layout 1             | `50873c1d1049`  |
| 1329   | Layout 1             | `50873c1d1049`  |
| 1327   | Layout 1             | `50873c1d1049`  |
| 1324   | Layout 1             | `50873c1d1049`  |
| 1321   | Layout 1             | `50873c1d1049`  |
| 1319   | Layout 1             | `50873c1d1049`  |
| 1318   | Layout 1             | `50873c1d1049`  |
| 1316   | Layout 1             | `50873c1d1049`  |
| 1313   | Layout 1             | `50873c1d1049`  |
| 1311   | Layout 1             | `50873c1d1049`  |
| 1309   | Layout 1             | `50873c1d1049`  |
| 1304   | Layout 1             | `50873c1d1049`  |
| 1292   | Layout 1             | `50873c1d1049`  |
| 1286   | Layout 1             | `50873c1d1049`  |
| 1280   | Layout 1             | `50873c1d1049`  |
| 1276   | Layout 1             | `50873c1d1049`  |
| 1267   | Layout 1             | `50873c1d1049`  |
| 1261   | Layout 1             | `50873c1d1049`  |
| 1256   | Layout 1             | `50873c1d1049`  |
| 1250   | Layout 1             | `50873c1d1049`  |
| 1246   | Layout 1             | `50873c1d1049`  |
| 1239   | Layout 1             | `50873c1d1049`  |
| 1230   | Layout 1             | `50873c1d1049`  |
| 1226   | Layout 1             | `50873c1d1049`  |
| 1220   | Layout 1             | `50873c1d1049`  |
| 1217   | Layout 1             | `50873c1d1049`  |
| 1211   | Layout 1             | `50873c1d1049`  |
| 1210   | Layout 1             | `50873c1d1049`  |
| 1208   | Layout 1             | `50873c1d1049`  |
| 1203   | Layout 1             | `50873c1d1049`  |
| 1197   | Layout 1             | `50873c1d1049`  |
| 1194   | Layout 1             | `50873c1d1049`  |
| 1192   | Layout 1             | `50873c1d1049`  |
| 1187   | Layout 1             | `50873c1d1049`  |
| 1183   | Layout 1             | `50873c1d1049`  |
| 1177   | Layout 1             | `50873c1d1049`  |
| 1173   | Layout 1             | `50873c1d1049`  |
| 1167   | Layout 1             | `50873c1d1049`  |
| 1164   | Layout 1             | `50873c1d1049`  |
| 1156   | Layout 1             | `50873c1d1049`  |
| 1149   | Layout 1             | `50873c1d1049`  |
| 1144   | Layout 1             | `50873c1d1049`  |
| 1137   | Layout 1             | `50873c1d1049`  |
| 1132   | Layout 1             | `50873c1d1049`  |
| 1127   | Layout 1             | `50873c1d1049`  |
| 1122   | Layout 1             | `50873c1d1049`  |
| 1118   | Layout 1             | `50873c1d1049`  |
| 1114   | Layout 1             | `50873c1d1049`  |
| 1109   | Layout 1             | `50873c1d1049`  |
| 1102   | Layout 1             | `50873c1d1049`  |
| 1096   | Layout 1             | `50873c1d1049`  |
| 1088   | Layout 1             | `50873c1d1049`  |
| 1081   | Layout 1             | `50873c1d1049`  |
| 1076   | Layout 1             | `50873c1d1049`  |
| 1069   | Layout 1             | `50873c1d1049`  |
| 1064   | Layout 1             | `50873c1d1049`  |
| 1058   | Layout 1             | `50873c1d1049`  |
| 1051   | Layout 1             | `50873c1d1049`  |
| 1044   | Layout 1             | `50873c1d1049`  |
| 1036   | Layout 1             | `50873c1d1049`  |
| 1026   | Layout 1             | `50873c1d1049`  |
| 1016   | Layout 1             | `50873c1d1049`  |
| 1009   | Layout 1             | `50873c1d1049`  |
| 1005   | Layout 1             | `50873c1d1049`  |
| 1000   | Layout 1             | `50873c1d1049`  |
| 998    | Layout 1             | `50873c1d1049`  |
| 990    | Layout 1             | `50873c1d1049`  |
| 979    | Layout 1             | `50873c1d1049`  |
| 972    | Layout 1             | `50873c1d1049`  |
| 963    | Layout 1             | `50873c1d1049`  |
| 955    | Layout 1             | `50873c1d1049`  |
| 946    | Layout 1             | `50873c1d1049`  |
| 938    | Layout 1             | `50873c1d1049`  |
| 927    | Layout 1             | `50873c1d1049`  |
| 911    | Layout 1             | `50873c1d1049`  |
| 904    | Layout 1             | `50873c1d1049`  |
| 899    | Layout 1             | `50873c1d1049`  |
| 894    | Layout 1             | `50873c1d1049`  |
| 885    | Layout 1             | `50873c1d1049`  |
| 879    | Layout 1             | `50873c1d1049`  |
| 872    | Layout 1             | `50873c1d1049`  |
| 864    | Layout 1             | `50873c1d1049`  |
| 855    | Layout 1             | `50873c1d1049`  |
| 853    | Layout 1             | `50873c1d1049`  |
| 845    | Layout 1             | `50873c1d1049`  |
| 837    | Layout 1             | `50873c1d1049`  |
| 829    | Layout 1             | `50873c1d1049`  |
| 822    | Layout 1             | `50873c1d1049`  |
| 814    | Layout 1             | `50873c1d1049`  |
| 805    | Layout 1             | `50873c1d1049`  |
| 794    | No documented layout | `50873c1d1049`  |
| 787    | No documented layout | `50873c1d1049`  |
| 780    | No documented layout | `50873c1d1049`  |
| 771    | No documented layout | `50873c1d1049`  |
| 760    | No documented layout | `50873c1d1049`  |
| 748    | No documented layout | `50873c1d1049`  |
| 741    | No documented layout | `50873c1d1049`  |
| 736    | No documented layout | `50873c1d1049`  |
| 731    | No documented layout | `50873c1d1049`  |
| 723    | No documented layout | `50873c1d1049`  |
| 711    | No documented layout | `50873c1d1049`  |
| 707    | No documented layout | `50873c1d1049`  |
| 697    | No documented layout | `50873c1d1049`  |
| 689    | No documented layout | `50873c1d1049`  |
| 683    | No documented layout | `50873c1d1049`  |
| 678    | No documented layout | `50873c1d1049`  |
| 670    | No documented layout | `50873c1d1049`  |
| 661    | No documented layout | `50873c1d1049`  |
| 656    | No documented layout | `50873c1d1049`  |
| 652    | No documented layout | `50873c1d1049`  |
| 643    | No documented layout | `50873c1d1049`  |
| 637    | No documented layout | `50873c1d1049`  |
| 630    | No documented layout | `50873c1d1049`  |
| 627    | No documented layout | `50873c1d1049`  |
| 621    | No documented layout | `50873c1d1049`  |
| 617    | No documented layout | `50873c1d1049`  |
| 615    | No documented layout | `50873c1d1049`  |
| 606    | No documented layout | `50873c1d1049`  |
| 599    | No documented layout | `50873c1d1049`  |
| 592    | No documented layout | `50873c1d1049`  |
| 586    | No documented layout | `50873c1d1049`  |
| 577    | No documented layout | `50873c1d1049`  |
| 569    | No documented layout | `50873c1d1049`  |
| 561    | No documented layout | `50873c1d1049`  |
| 554    | No documented layout | `50873c1d1049`  |
| 542    | No documented layout | `50873c1d1049`  |
| 532    | No documented layout | `50873c1d1049`  |
| 531    | No documented layout | `50873c1d1049`  |
| 526    | No documented layout | `50873c1d1049`  |
| 521    | No documented layout | `50873c1d1049`  |
| 517    | No documented layout | `50873c1d1049`  |
| 510    | No file              | `50873c1d1049`  |
| 508    | No file              | `50873c1d1049`  |
| 504    | No file              | `50873c1d1049`  |
| 497    | No file              | `50873c1d1049`  |
| 491    | No file              | `50873c1d1049`  |
| 485    | No file              | `50873c1d1049`  |
| 478    | No file              | `50873c1d1049`  |
| 472    | No file              | `50873c1d1049`  |
| 466    | No file              | `50873c1d1049`  |
| 457    | No file              | `50873c1d1049`  |
| 452    | No file              | `50873c1d1049`  |
| 449    | No file              | `50873c1d1049`  |
| 435    | No file              | `50873c1d1049`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (11 bytes)

| Offset  | Type | Field            | Notes                                                                    |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | interaction_type | `CppEnums.InteractionType` value; see Interaction Types                   |
| `+0x04` | u8   | unknown_04       | `0` on every row; see Open Questions                                     |
| `+0x05` | u32  | execute          | Item key the interaction uses; `40414` on every row, see Notes           |
| `+0x09` | u16  | character_key    | `characterstatic.dbss` key; the handler shows its LOC type 6 name         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Interaction Types

`interaction_type` is the client's `CppEnums.InteractionType`
(`global_define_cpp_enum.luac`, client 3474), `InteractionType_GamePlay`
`0` to `InteractionType_ImmediatelySwapCharacter` `76`. The only value in
the file:

| Value | Lua name                |
| ----- | ----------------------- |
| `61`  | `InteractionType_Awake` |

## Field Names

The names follow the `Interaction_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_Interaction.xlsm`: `InteractionType`, `Condition`, `Excute` and
`CharacterKey`, in this order. Its 2 rows (`61`, `<NULL>`, `40414`,
`23751` and `61`, `<NULL>`, `40414`, `23767`) equal the 2 rows of the
client 1784 file value by value, and the client 1784 file is byte for byte
the private server's compiled `binary/interaction.bss`. `execute` spells
out the sheet's `Excute`. The `Condition` column is `<NULL>` on both rows,
so no value shows where it sits; `unknown_04` stays unnamed. The column
comments in the workbook belong to another sheet (`0: 퀘스트 전용`, a
dungeon and a desert prison).

## Notes

- Raw bytes on clients 1230 to 3474:
  `50 41 42 52 02 00 00 00 3D 00 00 00 00 DE 9D 00 00 C7 5C 3D 00 00 00 00 DE 9D 00 00 D7 5C 00 00 00 00 1E 00 00 00 00 00 00 00`
  (42 bytes). The file is not in the archives of client 794.
- `40414` is the item "[Guild] Ancient Contract: Mirumok Watcher" (LOC type
  0) and the skill "Final Damage 400%+Debuff" (LOC type 10, `skill.dbss`
  skill 40414 level 1). The `charactersimply.bss` interaction condition of
  both characters is `getitemcount(40414,0)>0;` (see
  [charactersimply](charactersimply_bss.md)), so the interaction needs that
  item. The item's own description (LOC type 0, 40414, `str_id4` 1) says
  "It awakens Guild Raid Bosses Mirumok Watcher Offin and Mirumok Destroyer
  Offin", the two characters of the file with `InteractionType_Awake`, so
  `execute` is the item. In game the quest that gives it reads "Talk to the
  Trembling Spirit NPC at Mirumok Ruins to complete the quest and receive
  the item". The handler shows the item's name and icon next to the key.
- The server dump on client 1784 holds the column names `InteractionType`
  and `Excute` next to the error `인터렉션 정보를 등록할 수 없습니다!` ("cannot
  register the interaction info").
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per row of the file.

## Open Questions

### Where the Condition Sits

The first five bytes of each row are `3D 00 00 00 00`. They read as a u32
`interaction_type` and a u8 `unknown_04`, or as a u8 `interaction_type`
and a u32. The sheet's `Condition` column is `<NULL>` on both rows, so the
data shows neither its width nor whether a condition is stored here at
all; a PABR string reference would point into the string table, which is
empty.
