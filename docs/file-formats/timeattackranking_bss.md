# `timeattackranking.bss` Format

## Purpose

The characters of the time attack rankings: a u32 count after the PABR
magic, then one u16 character key per entry. On client 3474 the list is
the Advanced Altar of Training (`27284`), five Kzarka variants (`24385` to
`24381`) and the two Mirumok Offin characters (`23751`, `23767`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 1220 and later | 3483    | `timeattackranking.bss` | 36    | 1 String Table | 4         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `timeattackranking.bss` | 36 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3ec11ed0acaf`  |
| 3482   | Layout 1 | `3ec11ed0acaf`  |
| 3474   | Layout 1 | `3ec11ed0acaf`  |
| 3473   | Layout 1 | `3ec11ed0acaf`  |
| 3464   | Layout 1 | `3ec11ed0acaf`  |
| 3458   | Layout 1 | `3ec11ed0acaf`  |
| 3454   | Layout 1 | `3ec11ed0acaf`  |
| 3444   | Layout 1 | `3ec11ed0acaf`  |
| 3435   | Layout 1 | `3ec11ed0acaf`  |
| 3426   | Layout 1 | `3ec11ed0acaf`  |
| 3418   | Layout 1 | `3ec11ed0acaf`  |
| 3412   | Layout 1 | `3ec11ed0acaf`  |
| 3402   | Layout 1 | `3ec11ed0acaf`  |
| 3396   | Layout 1 | `3ec11ed0acaf`  |
| 3387   | Layout 1 | `3ec11ed0acaf`  |
| 3381   | Layout 1 | `3ec11ed0acaf`  |
| 3373   | Layout 1 | `3ec11ed0acaf`  |
| 3364   | Layout 1 | `3ec11ed0acaf`  |
| 3356   | Layout 1 | `3ec11ed0acaf`  |
| 3349   | Layout 1 | `3ec11ed0acaf`  |
| 3342   | Layout 1 | `3ec11ed0acaf`  |
| 3335   | Layout 1 | `3ec11ed0acaf`  |
| 3326   | Layout 1 | `3ec11ed0acaf`  |
| 3321   | Layout 1 | `3ec11ed0acaf`  |
| 3314   | Layout 1 | `3ec11ed0acaf`  |
| 3303   | Layout 1 | `3ec11ed0acaf`  |
| 3302   | Layout 1 | `3ec11ed0acaf`  |
| 3293   | Layout 1 | `3ec11ed0acaf`  |
| 3283   | Layout 1 | `3ec11ed0acaf`  |
| 3275   | Layout 1 | `3ec11ed0acaf`  |
| 3267   | Layout 1 | `3ec11ed0acaf`  |
| 3258   | Layout 1 | `3ec11ed0acaf`  |
| 3251   | Layout 1 | `3ec11ed0acaf`  |
| 3242   | Layout 1 | `3ec11ed0acaf`  |
| 3235   | Layout 1 | `3ec11ed0acaf`  |
| 3229   | Layout 1 | `3ec11ed0acaf`  |
| 3212   | Layout 1 | `3ec11ed0acaf`  |
| 3203   | Layout 1 | `3ec11ed0acaf`  |
| 3193   | Layout 1 | `3ec11ed0acaf`  |
| 3186   | Layout 1 | `3ec11ed0acaf`  |
| 3177   | Layout 1 | `3ec11ed0acaf`  |
| 3169   | Layout 1 | `3ec11ed0acaf`  |
| 3158   | Layout 1 | `3ec11ed0acaf`  |
| 3151   | Layout 1 | `3ec11ed0acaf`  |
| 3144   | Layout 1 | `3ec11ed0acaf`  |
| 3133   | Layout 1 | `3ec11ed0acaf`  |
| 3125   | Layout 1 | `3ec11ed0acaf`  |
| 3118   | Layout 1 | `3ec11ed0acaf`  |
| 3111   | Layout 1 | `3ec11ed0acaf`  |
| 3103   | Layout 1 | `3ec11ed0acaf`  |
| 3095   | Layout 1 | `3ec11ed0acaf`  |
| 3086   | Layout 1 | `3ec11ed0acaf`  |
| 3072   | Layout 1 | `3ec11ed0acaf`  |
| 3062   | Layout 1 | `3ec11ed0acaf`  |
| 3052   | Layout 1 | `3ec11ed0acaf`  |
| 3045   | Layout 1 | `3ec11ed0acaf`  |
| 3037   | Layout 1 | `3ec11ed0acaf`  |
| 3030   | Layout 1 | `3ec11ed0acaf`  |
| 3021   | Layout 1 | `3ec11ed0acaf`  |
| 3012   | Layout 1 | `3ec11ed0acaf`  |
| 3002   | Layout 1 | `3ec11ed0acaf`  |
| 2995   | Layout 1 | `3ec11ed0acaf`  |
| 2987   | Layout 1 | `3ec11ed0acaf`  |
| 2978   | Layout 1 | `3ec11ed0acaf`  |
| 2970   | Layout 1 | `3ec11ed0acaf`  |
| 2959   | Layout 1 | `3ec11ed0acaf`  |
| 2951   | Layout 1 | `3ec11ed0acaf`  |
| 2942   | Layout 1 | `3ec11ed0acaf`  |
| 2935   | Layout 1 | `3ec11ed0acaf`  |
| 2932   | Layout 1 | `3ec11ed0acaf`  |
| 2923   | Layout 1 | `3ec11ed0acaf`  |
| 2919   | Layout 1 | `3ec11ed0acaf`  |
| 2907   | Layout 1 | `3ec11ed0acaf`  |
| 2900   | Layout 1 | `3ec11ed0acaf`  |
| 2891   | Layout 1 | `3ec11ed0acaf`  |
| 2882   | Layout 1 | `3ec11ed0acaf`  |
| 2872   | Layout 1 | `3ec11ed0acaf`  |
| 2863   | Layout 1 | `3ec11ed0acaf`  |
| 2855   | Layout 1 | `3ec11ed0acaf`  |
| 2849   | Layout 1 | `3ec11ed0acaf`  |
| 2844   | Layout 1 | `3ec11ed0acaf`  |
| 2834   | Layout 1 | `3ec11ed0acaf`  |
| 2825   | Layout 1 | `3ec11ed0acaf`  |
| 2819   | Layout 1 | `3ec11ed0acaf`  |
| 2811   | Layout 1 | `3ec11ed0acaf`  |
| 2803   | Layout 1 | `3ec11ed0acaf`  |
| 2794   | Layout 1 | `3ec11ed0acaf`  |
| 2783   | Layout 1 | `3ec11ed0acaf`  |
| 2774   | Layout 1 | `3ec11ed0acaf`  |
| 2765   | Layout 1 | `3ec11ed0acaf`  |
| 2756   | Layout 1 | `3ec11ed0acaf`  |
| 2750   | Layout 1 | `3ec11ed0acaf`  |
| 2743   | Layout 1 | `3ec11ed0acaf`  |
| 2736   | Layout 1 | `3ec11ed0acaf`  |
| 2726   | Layout 1 | `3ec11ed0acaf`  |
| 2717   | Layout 1 | `3ec11ed0acaf`  |
| 2709   | Layout 1 | `3ec11ed0acaf`  |
| 2703   | Layout 1 | `3ec11ed0acaf`  |
| 2695   | Layout 1 | `3ec11ed0acaf`  |
| 2684   | Layout 1 | `3ec11ed0acaf`  |
| 2672   | Layout 1 | `3ec11ed0acaf`  |
| 2665   | Layout 1 | `3ec11ed0acaf`  |
| 2657   | Layout 1 | `3ec11ed0acaf`  |
| 2649   | Layout 1 | `3ec11ed0acaf`  |
| 2644   | Layout 1 | `3ec11ed0acaf`  |
| 2637   | Layout 1 | `3ec11ed0acaf`  |
| 2629   | Layout 1 | `3ec11ed0acaf`  |
| 2619   | Layout 1 | `3ec11ed0acaf`  |
| 2612   | Layout 1 | `3ec11ed0acaf`  |
| 2606   | Layout 1 | `3ec11ed0acaf`  |
| 2602   | Layout 1 | `3ec11ed0acaf`  |
| 2601   | Layout 1 | `3ec11ed0acaf`  |
| 2592   | Layout 1 | `3ec11ed0acaf`  |
| 2583   | Layout 1 | `3ec11ed0acaf`  |
| 2575   | Layout 1 | `3ec11ed0acaf`  |
| 2567   | Layout 1 | `3ec11ed0acaf`  |
| 2560   | Layout 1 | `3ec11ed0acaf`  |
| 2553   | Layout 1 | `3ec11ed0acaf`  |
| 2545   | Layout 1 | `3ec11ed0acaf`  |
| 2538   | Layout 1 | `3ec11ed0acaf`  |
| 2529   | Layout 1 | `3ec11ed0acaf`  |
| 2519   | Layout 1 | `3ec11ed0acaf`  |
| 2513   | Layout 1 | `3ec11ed0acaf`  |
| 2510   | Layout 1 | `3ec11ed0acaf`  |
| 2507   | Layout 1 | `3ec11ed0acaf`  |
| 2503   | Layout 1 | `3ec11ed0acaf`  |
| 2498   | Layout 1 | `3ec11ed0acaf`  |
| 2492   | Layout 1 | `3ec11ed0acaf`  |
| 2487   | Layout 1 | `3ec11ed0acaf`  |
| 2480   | Layout 1 | `3ec11ed0acaf`  |
| 2474   | Layout 1 | `3ec11ed0acaf`  |
| 2468   | Layout 1 | `3ec11ed0acaf`  |
| 2460   | Layout 1 | `3ec11ed0acaf`  |
| 2453   | Layout 1 | `3ec11ed0acaf`  |
| 2444   | Layout 1 | `3ec11ed0acaf`  |
| 2438   | Layout 1 | `3ec11ed0acaf`  |
| 2434   | Layout 1 | `3ec11ed0acaf`  |
| 2429   | Layout 1 | `3ec11ed0acaf`  |
| 2421   | Layout 1 | `3ec11ed0acaf`  |
| 2414   | Layout 1 | `3ec11ed0acaf`  |
| 2407   | Layout 1 | `3ec11ed0acaf`  |
| 2401   | Layout 1 | `3ec11ed0acaf`  |
| 2397   | Layout 1 | `3ec11ed0acaf`  |
| 2393   | Layout 1 | `3ec11ed0acaf`  |
| 2384   | Layout 1 | `3ec11ed0acaf`  |
| 2378   | Layout 1 | `3ec11ed0acaf`  |
| 2372   | Layout 1 | `3ec11ed0acaf`  |
| 2358   | Layout 1 | `3ec11ed0acaf`  |
| 2352   | Layout 1 | `3ec11ed0acaf`  |
| 2347   | Layout 1 | `3ec11ed0acaf`  |
| 2343   | Layout 1 | `3ec11ed0acaf`  |
| 2335   | Layout 1 | `3ec11ed0acaf`  |
| 2327   | Layout 1 | `3ec11ed0acaf`  |
| 2324   | Layout 1 | `3ec11ed0acaf`  |
| 2319   | Layout 1 | `3ec11ed0acaf`  |
| 2313   | Layout 1 | `3ec11ed0acaf`  |
| 2308   | Layout 1 | `3ec11ed0acaf`  |
| 2302   | Layout 1 | `3ec11ed0acaf`  |
| 2295   | Layout 1 | `3ec11ed0acaf`  |
| 2290   | Layout 1 | `3ec11ed0acaf`  |
| 2284   | Layout 1 | `3ec11ed0acaf`  |
| 2276   | Layout 1 | `3ec11ed0acaf`  |
| 2269   | Layout 1 | `3ec11ed0acaf`  |
| 2259   | Layout 1 | `3ec11ed0acaf`  |
| 2250   | Layout 1 | `3ec11ed0acaf`  |
| 2243   | Layout 1 | `3ec11ed0acaf`  |
| 2235   | Layout 1 | `3ec11ed0acaf`  |
| 2229   | Layout 1 | `3ec11ed0acaf`  |
| 2224   | Layout 1 | `3ec11ed0acaf`  |
| 2218   | Layout 1 | `3ec11ed0acaf`  |
| 2215   | Layout 1 | `3ec11ed0acaf`  |
| 2207   | Layout 1 | `3ec11ed0acaf`  |
| 2203   | Layout 1 | `3ec11ed0acaf`  |
| 2196   | Layout 1 | `3ec11ed0acaf`  |
| 2192   | Layout 1 | `3ec11ed0acaf`  |
| 2189   | Layout 1 | `3ec11ed0acaf`  |
| 2183   | Layout 1 | `3ec11ed0acaf`  |
| 2179   | Layout 1 | `3ec11ed0acaf`  |
| 2171   | Layout 1 | `3ec11ed0acaf`  |
| 2163   | Layout 1 | `3ec11ed0acaf`  |
| 2156   | Layout 1 | `3ec11ed0acaf`  |
| 2151   | Layout 1 | `3ec11ed0acaf`  |
| 2147   | Layout 1 | `3ec11ed0acaf`  |
| 2142   | Layout 1 | `3ec11ed0acaf`  |
| 2138   | Layout 1 | `3ec11ed0acaf`  |
| 2134   | Layout 1 | `3ec11ed0acaf`  |
| 2130   | Layout 1 | `3ec11ed0acaf`  |
| 2122   | Layout 1 | `3ec11ed0acaf`  |
| 2107   | Layout 1 | `3ec11ed0acaf`  |
| 2098   | Layout 1 | `3ec11ed0acaf`  |
| 2089   | Layout 1 | `3ec11ed0acaf`  |
| 2081   | Layout 1 | `3ec11ed0acaf`  |
| 2073   | Layout 1 | `3ec11ed0acaf`  |
| 2067   | Layout 1 | `3ec11ed0acaf`  |
| 2063   | Layout 1 | `3ec11ed0acaf`  |
| 2059   | Layout 1 | `3ec11ed0acaf`  |
| 2052   | Layout 1 | `3ec11ed0acaf`  |
| 2044   | Layout 1 | `3ec11ed0acaf`  |
| 2039   | Layout 1 | `3ec11ed0acaf`  |
| 2032   | Layout 1 | `3ec11ed0acaf`  |
| 2025   | Layout 1 | `3ec11ed0acaf`  |
| 2011   | Layout 1 | `3ec11ed0acaf`  |
| 2005   | Layout 1 | `3ec11ed0acaf`  |
| 2000   | Layout 1 | `3ec11ed0acaf`  |
| 1996   | Layout 1 | `3ec11ed0acaf`  |
| 1991   | Layout 1 | `3ec11ed0acaf`  |
| 1985   | Layout 1 | `3ec11ed0acaf`  |
| 1980   | Layout 1 | `3ec11ed0acaf`  |
| 1969   | Layout 1 | `3ec11ed0acaf`  |
| 1964   | Layout 1 | `3ec11ed0acaf`  |
| 1958   | Layout 1 | `3ec11ed0acaf`  |
| 1950   | Layout 1 | `3ec11ed0acaf`  |
| 1945   | Layout 1 | `3ec11ed0acaf`  |
| 1937   | Layout 1 | `3ec11ed0acaf`  |
| 1933   | Layout 1 | `3ec11ed0acaf`  |
| 1927   | Layout 1 | `3ec11ed0acaf`  |
| 1921   | Layout 1 | `3ec11ed0acaf`  |
| 1914   | Layout 1 | `3ec11ed0acaf`  |
| 1908   | Layout 1 | `3ec11ed0acaf`  |
| 1897   | Layout 1 | `3ec11ed0acaf`  |
| 1892   | Layout 1 | `3ec11ed0acaf`  |
| 1886   | Layout 1 | `3ec11ed0acaf`  |
| 1881   | Layout 1 | `3ec11ed0acaf`  |
| 1871   | Layout 1 | `3ec11ed0acaf`  |
| 1866   | Layout 1 | `3ec11ed0acaf`  |
| 1862   | Layout 1 | `3ec11ed0acaf`  |
| 1854   | Layout 1 | `3ec11ed0acaf`  |
| 1846   | Layout 1 | `3ec11ed0acaf`  |
| 1838   | Layout 1 | `3ec11ed0acaf`  |
| 1832   | Layout 1 | `3ec11ed0acaf`  |
| 1826   | Layout 1 | `3ec11ed0acaf`  |
| 1822   | Layout 1 | `3ec11ed0acaf`  |
| 1818   | Layout 1 | `3ec11ed0acaf`  |
| 1804   | Layout 1 | `3ec11ed0acaf`  |
| 1794   | Layout 1 | `3ec11ed0acaf`  |
| 1790   | Layout 1 | `3ec11ed0acaf`  |
| 1784   | Layout 1 | `3ec11ed0acaf`  |
| 1774   | Layout 1 | `3ec11ed0acaf`  |
| 1771   | Layout 1 | `3ec11ed0acaf`  |
| 1762   | Layout 1 | `3ec11ed0acaf`  |
| 1759   | Layout 1 | `3ec11ed0acaf`  |
| 1754   | Layout 1 | `3ec11ed0acaf`  |
| 1749   | Layout 1 | `3ec11ed0acaf`  |
| 1743   | Layout 1 | `3ec11ed0acaf`  |
| 1737   | Layout 1 | `3ec11ed0acaf`  |
| 1731   | Layout 1 | `3ec11ed0acaf`  |
| 1725   | Layout 1 | `3ec11ed0acaf`  |
| 1717   | Layout 1 | `3ec11ed0acaf`  |
| 1710   | Layout 1 | `3ec11ed0acaf`  |
| 1704   | Layout 1 | `3ec11ed0acaf`  |
| 1698   | Layout 1 | `3ec11ed0acaf`  |
| 1690   | Layout 1 | `3ec11ed0acaf`  |
| 1685   | Layout 1 | `3ec11ed0acaf`  |
| 1680   | Layout 1 | `3ec11ed0acaf`  |
| 1674   | Layout 1 | `3ec11ed0acaf`  |
| 1668   | Layout 1 | `3ec11ed0acaf`  |
| 1659   | Layout 1 | `3ec11ed0acaf`  |
| 1649   | Layout 1 | `3ec11ed0acaf`  |
| 1642   | Layout 1 | `3ec11ed0acaf`  |
| 1636   | Layout 1 | `3ec11ed0acaf`  |
| 1628   | Layout 1 | `3ec11ed0acaf`  |
| 1622   | Layout 1 | `3ec11ed0acaf`  |
| 1614   | Layout 1 | `3ec11ed0acaf`  |
| 1608   | Layout 1 | `3ec11ed0acaf`  |
| 1602   | Layout 1 | `3ec11ed0acaf`  |
| 1598   | Layout 1 | `3ec11ed0acaf`  |
| 1594   | Layout 1 | `3ec11ed0acaf`  |
| 1590   | Layout 1 | `3ec11ed0acaf`  |
| 1587   | Layout 1 | `3ec11ed0acaf`  |
| 1584   | Layout 1 | `3ec11ed0acaf`  |
| 1579   | Layout 1 | `3ec11ed0acaf`  |
| 1572   | Layout 1 | `3ec11ed0acaf`  |
| 1565   | Layout 1 | `3ec11ed0acaf`  |
| 1559   | Layout 1 | `3ec11ed0acaf`  |
| 1554   | Layout 1 | `3ec11ed0acaf`  |
| 1547   | Layout 1 | `3ec11ed0acaf`  |
| 1537   | Layout 1 | `3ec11ed0acaf`  |
| 1529   | Layout 1 | `3ec11ed0acaf`  |
| 1524   | Layout 1 | `3ec11ed0acaf`  |
| 1519   | Layout 1 | `3ec11ed0acaf`  |
| 1509   | Layout 1 | `3ec11ed0acaf`  |
| 1506   | Layout 1 | `3ec11ed0acaf`  |
| 1504   | Layout 1 | `3ec11ed0acaf`  |
| 1500   | Layout 1 | `3ec11ed0acaf`  |
| 1493   | Layout 1 | `3ec11ed0acaf`  |
| 1489   | Layout 1 | `3ec11ed0acaf`  |
| 1485   | Layout 1 | `3ec11ed0acaf`  |
| 1481   | Layout 1 | `3ec11ed0acaf`  |
| 1474   | Layout 1 | `3ec11ed0acaf`  |
| 1466   | Layout 1 | `3ec11ed0acaf`  |
| 1462   | Layout 1 | `3ec11ed0acaf`  |
| 1459   | Layout 1 | `3ec11ed0acaf`  |
| 1453   | Layout 1 | `3ec11ed0acaf`  |
| 1450   | Layout 1 | `3ec11ed0acaf`  |
| 1445   | Layout 1 | `3ec11ed0acaf`  |
| 1439   | Layout 1 | `3ec11ed0acaf`  |
| 1433   | Layout 1 | `3ec11ed0acaf`  |
| 1430   | Layout 1 | `3ec11ed0acaf`  |
| 1426   | Layout 1 | `3ec11ed0acaf`  |
| 1421   | Layout 1 | `3ec11ed0acaf`  |
| 1417   | Layout 1 | `3ec11ed0acaf`  |
| 1416   | Layout 1 | `3ec11ed0acaf`  |
| 1409   | Layout 1 | `3ec11ed0acaf`  |
| 1405   | Layout 1 | `3ec11ed0acaf`  |
| 1401   | Layout 1 | `3ec11ed0acaf`  |
| 1396   | Layout 1 | `3ec11ed0acaf`  |
| 1391   | Layout 1 | `3ec11ed0acaf`  |
| 1390   | Layout 1 | `3ec11ed0acaf`  |
| 1386   | Layout 1 | `3ec11ed0acaf`  |
| 1381   | Layout 1 | `3ec11ed0acaf`  |
| 1379   | Layout 1 | `3ec11ed0acaf`  |
| 1372   | Layout 1 | `3ec11ed0acaf`  |
| 1366   | Layout 1 | `3ec11ed0acaf`  |
| 1364   | Layout 1 | `3ec11ed0acaf`  |
| 1363   | Layout 1 | `3ec11ed0acaf`  |
| 1360   | Layout 1 | `3ec11ed0acaf`  |
| 1358   | Layout 1 | `3ec11ed0acaf`  |
| 1355   | Layout 1 | `3ec11ed0acaf`  |
| 1351   | Layout 1 | `3ec11ed0acaf`  |
| 1348   | Layout 1 | `3ec11ed0acaf`  |
| 1346   | Layout 1 | `3ec11ed0acaf`  |
| 1341   | Layout 1 | `3ec11ed0acaf`  |
| 1340   | Layout 1 | `3ec11ed0acaf`  |
| 1338   | Layout 1 | `3ec11ed0acaf`  |
| 1335   | Layout 1 | `3ec11ed0acaf`  |
| 1333   | Layout 1 | `3ec11ed0acaf`  |
| 1329   | Layout 1 | `3ec11ed0acaf`  |
| 1327   | Layout 1 | `3ec11ed0acaf`  |
| 1324   | Layout 1 | `3ec11ed0acaf`  |
| 1321   | Layout 1 | `3ec11ed0acaf`  |
| 1319   | Layout 1 | `3ec11ed0acaf`  |
| 1318   | Layout 1 | `3ec11ed0acaf`  |
| 1316   | Layout 1 | `3ec11ed0acaf`  |
| 1313   | Layout 1 | `3ec11ed0acaf`  |
| 1311   | Layout 1 | `3ec11ed0acaf`  |
| 1309   | Layout 1 | `3ec11ed0acaf`  |
| 1304   | Layout 1 | `3ec11ed0acaf`  |
| 1292   | Layout 1 | `3ec11ed0acaf`  |
| 1286   | Layout 1 | `3ec11ed0acaf`  |
| 1280   | Layout 1 | `3ec11ed0acaf`  |
| 1276   | Layout 1 | `3ec11ed0acaf`  |
| 1267   | Layout 1 | `3ec11ed0acaf`  |
| 1261   | Layout 1 | `3ec11ed0acaf`  |
| 1256   | Layout 1 | `3ec11ed0acaf`  |
| 1250   | Layout 1 | `3ec11ed0acaf`  |
| 1246   | Layout 1 | `3ec11ed0acaf`  |
| 1239   | Layout 1 | `3ec11ed0acaf`  |
| 1230   | Layout 1 | `3ec11ed0acaf`  |
| 1226   | Layout 1 | `3ec11ed0acaf`  |
| 1220   | Layout 1 | `3ec11ed0acaf`  |
| 1217   | No file  | `3ec11ed0acaf`  |
| 1211   | No file  | `3ec11ed0acaf`  |
| 1210   | No file  | `3ec11ed0acaf`  |
| 1208   | No file  | `3ec11ed0acaf`  |
| 1203   | No file  | `3ec11ed0acaf`  |
| 1197   | No file  | `3ec11ed0acaf`  |
| 1194   | No file  | `3ec11ed0acaf`  |
| 1192   | No file  | `3ec11ed0acaf`  |
| 1187   | No file  | `3ec11ed0acaf`  |
| 1183   | No file  | `3ec11ed0acaf`  |
| 1177   | No file  | `3ec11ed0acaf`  |
| 1173   | No file  | `3ec11ed0acaf`  |
| 1167   | No file  | `3ec11ed0acaf`  |
| 1164   | No file  | `3ec11ed0acaf`  |
| 1156   | No file  | `3ec11ed0acaf`  |
| 1149   | No file  | `3ec11ed0acaf`  |
| 1144   | No file  | `3ec11ed0acaf`  |
| 1137   | No file  | `3ec11ed0acaf`  |
| 1132   | No file  | `3ec11ed0acaf`  |
| 1127   | No file  | `3ec11ed0acaf`  |
| 1122   | No file  | `3ec11ed0acaf`  |
| 1118   | No file  | `3ec11ed0acaf`  |
| 1114   | No file  | `3ec11ed0acaf`  |
| 1109   | No file  | `3ec11ed0acaf`  |
| 1102   | No file  | `3ec11ed0acaf`  |
| 1096   | No file  | `3ec11ed0acaf`  |
| 1088   | No file  | `3ec11ed0acaf`  |
| 1081   | No file  | `3ec11ed0acaf`  |
| 1076   | No file  | `3ec11ed0acaf`  |
| 1069   | No file  | `3ec11ed0acaf`  |
| 1064   | No file  | `3ec11ed0acaf`  |
| 1058   | No file  | `3ec11ed0acaf`  |
| 1051   | No file  | `3ec11ed0acaf`  |
| 1044   | No file  | `3ec11ed0acaf`  |
| 1036   | No file  | `3ec11ed0acaf`  |
| 1026   | No file  | `3ec11ed0acaf`  |
| 1016   | No file  | `3ec11ed0acaf`  |
| 1009   | No file  | `3ec11ed0acaf`  |
| 1005   | No file  | `3ec11ed0acaf`  |
| 1000   | No file  | `3ec11ed0acaf`  |
| 998    | No file  | `3ec11ed0acaf`  |
| 990    | No file  | `3ec11ed0acaf`  |
| 979    | No file  | `3ec11ed0acaf`  |
| 972    | No file  | `3ec11ed0acaf`  |
| 963    | No file  | `3ec11ed0acaf`  |
| 955    | No file  | `3ec11ed0acaf`  |
| 946    | No file  | `3ec11ed0acaf`  |
| 938    | No file  | `3ec11ed0acaf`  |
| 927    | No file  | `3ec11ed0acaf`  |
| 911    | No file  | `3ec11ed0acaf`  |
| 904    | No file  | `3ec11ed0acaf`  |
| 899    | No file  | `3ec11ed0acaf`  |
| 894    | No file  | `3ec11ed0acaf`  |
| 885    | No file  | `3ec11ed0acaf`  |
| 879    | No file  | `3ec11ed0acaf`  |
| 872    | No file  | `3ec11ed0acaf`  |
| 864    | No file  | `3ec11ed0acaf`  |
| 855    | No file  | `3ec11ed0acaf`  |
| 853    | No file  | `3ec11ed0acaf`  |
| 845    | No file  | `3ec11ed0acaf`  |
| 837    | No file  | `3ec11ed0acaf`  |
| 829    | No file  | `3ec11ed0acaf`  |
| 822    | No file  | `3ec11ed0acaf`  |
| 814    | No file  | `3ec11ed0acaf`  |
| 805    | No file  | `3ec11ed0acaf`  |
| 794    | No file  | `3ec11ed0acaf`  |
| 787    | No file  | `3ec11ed0acaf`  |
| 780    | No file  | `3ec11ed0acaf`  |
| 771    | No file  | `3ec11ed0acaf`  |
| 760    | No file  | `3ec11ed0acaf`  |
| 748    | No file  | `3ec11ed0acaf`  |
| 741    | No file  | `3ec11ed0acaf`  |
| 736    | No file  | `3ec11ed0acaf`  |
| 731    | No file  | `3ec11ed0acaf`  |
| 723    | No file  | `3ec11ed0acaf`  |
| 711    | No file  | `3ec11ed0acaf`  |
| 707    | No file  | `3ec11ed0acaf`  |
| 697    | No file  | `3ec11ed0acaf`  |
| 689    | No file  | `3ec11ed0acaf`  |
| 683    | No file  | `3ec11ed0acaf`  |
| 678    | No file  | `3ec11ed0acaf`  |
| 670    | No file  | `3ec11ed0acaf`  |
| 661    | No file  | `3ec11ed0acaf`  |
| 656    | No file  | `3ec11ed0acaf`  |
| 652    | No file  | `3ec11ed0acaf`  |
| 643    | No file  | `3ec11ed0acaf`  |
| 637    | No file  | `3ec11ed0acaf`  |
| 630    | No file  | `3ec11ed0acaf`  |
| 627    | No file  | `3ec11ed0acaf`  |
| 621    | No file  | `3ec11ed0acaf`  |
| 617    | No file  | `3ec11ed0acaf`  |
| 615    | No file  | `3ec11ed0acaf`  |
| 606    | No file  | `3ec11ed0acaf`  |
| 599    | No file  | `3ec11ed0acaf`  |
| 592    | No file  | `3ec11ed0acaf`  |
| 586    | No file  | `3ec11ed0acaf`  |
| 577    | No file  | `3ec11ed0acaf`  |
| 569    | No file  | `3ec11ed0acaf`  |
| 561    | No file  | `3ec11ed0acaf`  |
| 554    | No file  | `3ec11ed0acaf`  |
| 542    | No file  | `3ec11ed0acaf`  |
| 532    | No file  | `3ec11ed0acaf`  |
| 531    | No file  | `3ec11ed0acaf`  |
| 526    | No file  | `3ec11ed0acaf`  |
| 521    | No file  | `3ec11ed0acaf`  |
| 517    | No file  | `3ec11ed0acaf`  |
| 510    | No file  | `3ec11ed0acaf`  |
| 508    | No file  | `3ec11ed0acaf`  |
| 504    | No file  | `3ec11ed0acaf`  |
| 497    | No file  | `3ec11ed0acaf`  |
| 491    | No file  | `3ec11ed0acaf`  |
| 485    | No file  | `3ec11ed0acaf`  |
| 478    | No file  | `3ec11ed0acaf`  |
| 472    | No file  | `3ec11ed0acaf`  |
| 466    | No file  | `3ec11ed0acaf`  |
| 457    | No file  | `3ec11ed0acaf`  |
| 452    | No file  | `3ec11ed0acaf`  |
| 449    | No file  | `3ec11ed0acaf`  |
| 435    | No file  | `3ec11ed0acaf`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                    | Field           | Notes                                                      |
| -------------------- | ----------------------- | --------------- | ---------------------------------------------------------- |
| `+0x00`              | char[4]                 | magic           | ASCII `PABR`                                               |
| `+0x04`              | u32                     | character_count | Number of character keys                                   |
| `+0x08`              | u16[character_count]    | character_key   | `characterstatic.dbss` key; the handler shows its LOC type 6 name |
| `character_key+0x00` | String Table            | string_table    | See String Table                                           |
| `string_table+0x00`  | u32                     | table_start     | Offset of the string table, where `character_key` ends     |
| `string_table+0x04`  | u32                     | zero            | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is
named after the file. The server dump of that client reads it in
`CharacterStaticStatusManager::readFromBinary()` ("timeattackRanking Open
Failed."), and every key resolves to a character name (LOC type 6), so
`character_key` names the meaning.

The keys line up with the `TimeAttackType` column of the
`Character_Table` sheet on client 1784: all 8 of 8 keys of the client 1784
file have a time attack type, and the client 1784 file is byte for byte
the private server's compiled `binary/timeattackranking.bss`. The sheet
sets a type on 9 more characters that the file leaves out.

| Key (client 1784 and 3474) | Name (LOC type 6, client 3474) | `TimeAttackType` | `TimeAttackLimitMinute` |
| -------------------------- | ------------------------------ | ---------------- | ----------------------- |
| `27284`                    | Advanced Altar of Training     | `2`              | `30`                    |
| `24385` to `24381`         | Transcended, Consumed, Restrained, Transmuting and Deprived Kzarka | `3` | `7` |
| `23751`                    | Mirumok Watcher Offin          | `1`              | `30`                    |
| `23767`                    | Mirumok Destroyer Offin        | `1`              | `30`                    |

The sheet's rows with a type that the file does not list are `23754` and
`23769` (Watcher Offin Tett, type `1`), `27134` to `27138` (the five
Sacraments) and `27337` (Ancient Puturum, type `2`), and `28571` (type `0`,
no LOC type 6 name on client 3474).

## Notes

- Raw bytes on clients 1784 to 3474:
  `50 41 42 52 08 00 00 00 94 6A 41 5F 40 5F 3F 5F 3E 5F 3D 5F C7 5C D7 5C 00 00 00 00 18 00 00 00 00 00 00 00`
  (36 bytes). Clients 1230 and 1485 list 3 keys: `27284`, `23751` and
  `23767`. The file is not in the archives of client 794.
- The boss ranking window (`panel_window_monsterranking.luac`, client 3474)
  lists time attack groups with `ToClient_GetTimeAttackListCount()` and
  `ToClient_GetTimeAttackGroupInfo(index)`, each with a group name and a
  family or guild ranking; no Lua call reads a character key list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per character key.
