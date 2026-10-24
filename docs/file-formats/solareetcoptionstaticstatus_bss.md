# `solareetcoptionstaticstatus.bss` Format

## Purpose

Arena of Solare options: five f32 values with no magic, no count and no
string table. On client 3474 they are `60`, `115`, `400`, `37` and `57`; no
source confirms what any of them holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 3086 and later | 3483    | `solareetcoptionstaticstatus.bss` | 20    | -       | -         |
| 1      | 2900 to 3062   | 3062    | `solareetcoptionstaticstatus.bss` | 12    | -       | -         |

| Layout | File                              | Known      | Unknown       |
| ------ | --------------------------------- | ---------- | ------------- |
| 2      | `solareetcoptionstaticstatus.bss` | 0 B (0.0%) | 20 B (100.0%) |
| 1      | `solareetcoptionstaticstatus.bss` | 0 B (0.0%) | 12 B (100.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `0bbd0e12886f`  |
| 3482   | Layout 2             | `0bbd0e12886f`  |
| 3474   | Layout 2             | `0bbd0e12886f`  |
| 3473   | Layout 2             | `0bbd0e12886f`  |
| 3464   | Layout 2             | `0bbd0e12886f`  |
| 3458   | Layout 2             | `0bbd0e12886f`  |
| 3454   | Layout 2             | `0bbd0e12886f`  |
| 3444   | Layout 2             | `0bbd0e12886f`  |
| 3435   | Layout 2             | `0bbd0e12886f`  |
| 3426   | Layout 2             | `0bbd0e12886f`  |
| 3418   | Layout 2             | `0bbd0e12886f`  |
| 3412   | Layout 2             | `0bbd0e12886f`  |
| 3402   | Layout 2             | `0bbd0e12886f`  |
| 3396   | Layout 2             | `0bbd0e12886f`  |
| 3387   | Layout 2             | `0bbd0e12886f`  |
| 3381   | Layout 2             | `0bbd0e12886f`  |
| 3373   | Layout 2             | `0bbd0e12886f`  |
| 3364   | Layout 2             | `0bbd0e12886f`  |
| 3356   | Layout 2             | `0bbd0e12886f`  |
| 3349   | Layout 2             | `0bbd0e12886f`  |
| 3342   | Layout 2             | `0bbd0e12886f`  |
| 3335   | Layout 2             | `0bbd0e12886f`  |
| 3326   | Layout 2             | `0bbd0e12886f`  |
| 3321   | Layout 2             | `0bbd0e12886f`  |
| 3314   | Layout 2             | `0bbd0e12886f`  |
| 3303   | Layout 2             | `0bbd0e12886f`  |
| 3302   | Layout 2             | `0bbd0e12886f`  |
| 3293   | Layout 2             | `0bbd0e12886f`  |
| 3283   | Layout 2             | `0bbd0e12886f`  |
| 3275   | Layout 2             | `0bbd0e12886f`  |
| 3267   | Layout 2             | `0bbd0e12886f`  |
| 3258   | Layout 2             | `0bbd0e12886f`  |
| 3251   | Layout 2             | `0bbd0e12886f`  |
| 3242   | Layout 2             | `0bbd0e12886f`  |
| 3235   | Layout 2             | `0bbd0e12886f`  |
| 3229   | Layout 2             | `0bbd0e12886f`  |
| 3212   | Layout 2             | `0bbd0e12886f`  |
| 3203   | Layout 2             | `0bbd0e12886f`  |
| 3193   | Layout 2             | `0bbd0e12886f`  |
| 3186   | Layout 2             | `0bbd0e12886f`  |
| 3177   | Layout 2             | `0bbd0e12886f`  |
| 3169   | Layout 2             | `0bbd0e12886f`  |
| 3158   | Layout 2             | `0bbd0e12886f`  |
| 3151   | Layout 2             | `0bbd0e12886f`  |
| 3144   | Layout 2             | `0bbd0e12886f`  |
| 3133   | Layout 2             | `0bbd0e12886f`  |
| 3125   | Layout 2             | `0bbd0e12886f`  |
| 3118   | Layout 2             | `0bbd0e12886f`  |
| 3111   | Layout 2             | `0bbd0e12886f`  |
| 3103   | Layout 2             | `0bbd0e12886f`  |
| 3095   | Layout 2             | `0bbd0e12886f`  |
| 3086   | Layout 2             | `0bbd0e12886f`  |
| 3072   | No documented layout | `0bbd0e12886f`  |
| 3062   | Layout 1             | `0bbd0e12886f`  |
| 3052   | Layout 1             | `0bbd0e12886f`  |
| 3045   | Layout 1             | `0bbd0e12886f`  |
| 3037   | Layout 1             | `0bbd0e12886f`  |
| 3030   | Layout 1             | `0bbd0e12886f`  |
| 3021   | Layout 1             | `0bbd0e12886f`  |
| 3012   | Layout 1             | `0bbd0e12886f`  |
| 3002   | Layout 1             | `0bbd0e12886f`  |
| 2995   | Layout 1             | `0bbd0e12886f`  |
| 2987   | Layout 1             | `0bbd0e12886f`  |
| 2978   | Layout 1             | `0bbd0e12886f`  |
| 2970   | Layout 1             | `0bbd0e12886f`  |
| 2959   | Layout 1             | `0bbd0e12886f`  |
| 2951   | Layout 1             | `0bbd0e12886f`  |
| 2942   | Layout 1             | `0bbd0e12886f`  |
| 2935   | Layout 1             | `0bbd0e12886f`  |
| 2932   | Layout 1             | `0bbd0e12886f`  |
| 2923   | Layout 1             | `0bbd0e12886f`  |
| 2919   | Layout 1             | `0bbd0e12886f`  |
| 2907   | Layout 1             | `0bbd0e12886f`  |
| 2900   | Layout 1             | `0bbd0e12886f`  |
| 2891   | No file              | `0bbd0e12886f`  |
| 2882   | No file              | `0bbd0e12886f`  |
| 2872   | No file              | `0bbd0e12886f`  |
| 2863   | No file              | `0bbd0e12886f`  |
| 2855   | No file              | `0bbd0e12886f`  |
| 2849   | No file              | `0bbd0e12886f`  |
| 2844   | No file              | `0bbd0e12886f`  |
| 2834   | No file              | `0bbd0e12886f`  |
| 2825   | No file              | `0bbd0e12886f`  |
| 2819   | No file              | `0bbd0e12886f`  |
| 2811   | No file              | `0bbd0e12886f`  |
| 2803   | No file              | `0bbd0e12886f`  |
| 2794   | No file              | `0bbd0e12886f`  |
| 2783   | No file              | `0bbd0e12886f`  |
| 2774   | No file              | `0bbd0e12886f`  |
| 2765   | No file              | `0bbd0e12886f`  |
| 2756   | No file              | `0bbd0e12886f`  |
| 2750   | No file              | `0bbd0e12886f`  |
| 2743   | No file              | `0bbd0e12886f`  |
| 2736   | No file              | `0bbd0e12886f`  |
| 2726   | No file              | `0bbd0e12886f`  |
| 2717   | No file              | `0bbd0e12886f`  |
| 2709   | No file              | `0bbd0e12886f`  |
| 2703   | No file              | `0bbd0e12886f`  |
| 2695   | No file              | `0bbd0e12886f`  |
| 2684   | No file              | `0bbd0e12886f`  |
| 2672   | No file              | `0bbd0e12886f`  |
| 2665   | No file              | `0bbd0e12886f`  |
| 2657   | No file              | `0bbd0e12886f`  |
| 2649   | No file              | `0bbd0e12886f`  |
| 2644   | No file              | `0bbd0e12886f`  |
| 2637   | No file              | `0bbd0e12886f`  |
| 2629   | No file              | `0bbd0e12886f`  |
| 2619   | No file              | `0bbd0e12886f`  |
| 2612   | No file              | `0bbd0e12886f`  |
| 2606   | No file              | `0bbd0e12886f`  |
| 2602   | No file              | `0bbd0e12886f`  |
| 2601   | No file              | `0bbd0e12886f`  |
| 2592   | No file              | `0bbd0e12886f`  |
| 2583   | No file              | `0bbd0e12886f`  |
| 2575   | No file              | `0bbd0e12886f`  |
| 2567   | No file              | `0bbd0e12886f`  |
| 2560   | No file              | `0bbd0e12886f`  |
| 2553   | No file              | `0bbd0e12886f`  |
| 2545   | No file              | `0bbd0e12886f`  |
| 2538   | No file              | `0bbd0e12886f`  |
| 2529   | No file              | `0bbd0e12886f`  |
| 2519   | No file              | `0bbd0e12886f`  |
| 2513   | No file              | `0bbd0e12886f`  |
| 2510   | No file              | `0bbd0e12886f`  |
| 2507   | No file              | `0bbd0e12886f`  |
| 2503   | No file              | `0bbd0e12886f`  |
| 2498   | No file              | `0bbd0e12886f`  |
| 2492   | No file              | `0bbd0e12886f`  |
| 2487   | No file              | `0bbd0e12886f`  |
| 2480   | No file              | `0bbd0e12886f`  |
| 2474   | No file              | `0bbd0e12886f`  |
| 2468   | No file              | `0bbd0e12886f`  |
| 2460   | No file              | `0bbd0e12886f`  |
| 2453   | No file              | `0bbd0e12886f`  |
| 2444   | No file              | `0bbd0e12886f`  |
| 2438   | No file              | `0bbd0e12886f`  |
| 2434   | No file              | `0bbd0e12886f`  |
| 2429   | No file              | `0bbd0e12886f`  |
| 2421   | No file              | `0bbd0e12886f`  |
| 2414   | No file              | `0bbd0e12886f`  |
| 2407   | No file              | `0bbd0e12886f`  |
| 2401   | No file              | `0bbd0e12886f`  |
| 2397   | No file              | `0bbd0e12886f`  |
| 2393   | No file              | `0bbd0e12886f`  |
| 2384   | No file              | `0bbd0e12886f`  |
| 2378   | No file              | `0bbd0e12886f`  |
| 2372   | No file              | `0bbd0e12886f`  |
| 2358   | No file              | `0bbd0e12886f`  |
| 2352   | No file              | `0bbd0e12886f`  |
| 2347   | No file              | `0bbd0e12886f`  |
| 2343   | No file              | `0bbd0e12886f`  |
| 2335   | No file              | `0bbd0e12886f`  |
| 2327   | No file              | `0bbd0e12886f`  |
| 2324   | No file              | `0bbd0e12886f`  |
| 2319   | No file              | `0bbd0e12886f`  |
| 2313   | No file              | `0bbd0e12886f`  |
| 2308   | No file              | `0bbd0e12886f`  |
| 2302   | No file              | `0bbd0e12886f`  |
| 2295   | No file              | `0bbd0e12886f`  |
| 2290   | No file              | `0bbd0e12886f`  |
| 2284   | No file              | `0bbd0e12886f`  |
| 2276   | No file              | `0bbd0e12886f`  |
| 2269   | No file              | `0bbd0e12886f`  |
| 2259   | No file              | `0bbd0e12886f`  |
| 2250   | No file              | `0bbd0e12886f`  |
| 2243   | No file              | `0bbd0e12886f`  |
| 2235   | No file              | `0bbd0e12886f`  |
| 2229   | No file              | `0bbd0e12886f`  |
| 2224   | No file              | `0bbd0e12886f`  |
| 2218   | No file              | `0bbd0e12886f`  |
| 2215   | No file              | `0bbd0e12886f`  |
| 2207   | No file              | `0bbd0e12886f`  |
| 2203   | No file              | `0bbd0e12886f`  |
| 2196   | No file              | `0bbd0e12886f`  |
| 2192   | No file              | `0bbd0e12886f`  |
| 2189   | No file              | `0bbd0e12886f`  |
| 2183   | No file              | `0bbd0e12886f`  |
| 2179   | No file              | `0bbd0e12886f`  |
| 2171   | No file              | `0bbd0e12886f`  |
| 2163   | No file              | `0bbd0e12886f`  |
| 2156   | No file              | `0bbd0e12886f`  |
| 2151   | No file              | `0bbd0e12886f`  |
| 2147   | No file              | `0bbd0e12886f`  |
| 2142   | No file              | `0bbd0e12886f`  |
| 2138   | No file              | `0bbd0e12886f`  |
| 2134   | No file              | `0bbd0e12886f`  |
| 2130   | No file              | `0bbd0e12886f`  |
| 2122   | No file              | `0bbd0e12886f`  |
| 2107   | No file              | `0bbd0e12886f`  |
| 2098   | No file              | `0bbd0e12886f`  |
| 2089   | No file              | `0bbd0e12886f`  |
| 2081   | No file              | `0bbd0e12886f`  |
| 2073   | No file              | `0bbd0e12886f`  |
| 2067   | No file              | `0bbd0e12886f`  |
| 2063   | No file              | `0bbd0e12886f`  |
| 2059   | No file              | `0bbd0e12886f`  |
| 2052   | No file              | `0bbd0e12886f`  |
| 2044   | No file              | `0bbd0e12886f`  |
| 2039   | No file              | `0bbd0e12886f`  |
| 2032   | No file              | `0bbd0e12886f`  |
| 2025   | No file              | `0bbd0e12886f`  |
| 2011   | No file              | `0bbd0e12886f`  |
| 2005   | No file              | `0bbd0e12886f`  |
| 2000   | No file              | `0bbd0e12886f`  |
| 1996   | No file              | `0bbd0e12886f`  |
| 1991   | No file              | `0bbd0e12886f`  |
| 1985   | No file              | `0bbd0e12886f`  |
| 1980   | No file              | `0bbd0e12886f`  |
| 1969   | No file              | `0bbd0e12886f`  |
| 1964   | No file              | `0bbd0e12886f`  |
| 1958   | No file              | `0bbd0e12886f`  |
| 1950   | No file              | `0bbd0e12886f`  |
| 1945   | No file              | `0bbd0e12886f`  |
| 1937   | No file              | `0bbd0e12886f`  |
| 1933   | No file              | `0bbd0e12886f`  |
| 1927   | No file              | `0bbd0e12886f`  |
| 1921   | No file              | `0bbd0e12886f`  |
| 1914   | No file              | `0bbd0e12886f`  |
| 1908   | No file              | `0bbd0e12886f`  |
| 1897   | No file              | `0bbd0e12886f`  |
| 1892   | No file              | `0bbd0e12886f`  |
| 1886   | No file              | `0bbd0e12886f`  |
| 1881   | No file              | `0bbd0e12886f`  |
| 1871   | No file              | `0bbd0e12886f`  |
| 1866   | No file              | `0bbd0e12886f`  |
| 1862   | No file              | `0bbd0e12886f`  |
| 1854   | No file              | `0bbd0e12886f`  |
| 1846   | No file              | `0bbd0e12886f`  |
| 1838   | No file              | `0bbd0e12886f`  |
| 1832   | No file              | `0bbd0e12886f`  |
| 1826   | No file              | `0bbd0e12886f`  |
| 1822   | No file              | `0bbd0e12886f`  |
| 1818   | No file              | `0bbd0e12886f`  |
| 1804   | No file              | `0bbd0e12886f`  |
| 1794   | No file              | `0bbd0e12886f`  |
| 1790   | No file              | `0bbd0e12886f`  |
| 1784   | No file              | `0bbd0e12886f`  |
| 1774   | No file              | `0bbd0e12886f`  |
| 1771   | No file              | `0bbd0e12886f`  |
| 1762   | No file              | `0bbd0e12886f`  |
| 1759   | No file              | `0bbd0e12886f`  |
| 1754   | No file              | `0bbd0e12886f`  |
| 1749   | No file              | `0bbd0e12886f`  |
| 1743   | No file              | `0bbd0e12886f`  |
| 1737   | No file              | `0bbd0e12886f`  |
| 1731   | No file              | `0bbd0e12886f`  |
| 1725   | No file              | `0bbd0e12886f`  |
| 1717   | No file              | `0bbd0e12886f`  |
| 1710   | No file              | `0bbd0e12886f`  |
| 1704   | No file              | `0bbd0e12886f`  |
| 1698   | No file              | `0bbd0e12886f`  |
| 1690   | No file              | `0bbd0e12886f`  |
| 1685   | No file              | `0bbd0e12886f`  |
| 1680   | No file              | `0bbd0e12886f`  |
| 1674   | No file              | `0bbd0e12886f`  |
| 1668   | No file              | `0bbd0e12886f`  |
| 1659   | No file              | `0bbd0e12886f`  |
| 1649   | No file              | `0bbd0e12886f`  |
| 1642   | No file              | `0bbd0e12886f`  |
| 1636   | No file              | `0bbd0e12886f`  |
| 1628   | No file              | `0bbd0e12886f`  |
| 1622   | No file              | `0bbd0e12886f`  |
| 1614   | No file              | `0bbd0e12886f`  |
| 1608   | No file              | `0bbd0e12886f`  |
| 1602   | No file              | `0bbd0e12886f`  |
| 1598   | No file              | `0bbd0e12886f`  |
| 1594   | No file              | `0bbd0e12886f`  |
| 1590   | No file              | `0bbd0e12886f`  |
| 1587   | No file              | `0bbd0e12886f`  |
| 1584   | No file              | `0bbd0e12886f`  |
| 1579   | No file              | `0bbd0e12886f`  |
| 1572   | No file              | `0bbd0e12886f`  |
| 1565   | No file              | `0bbd0e12886f`  |
| 1559   | No file              | `0bbd0e12886f`  |
| 1554   | No file              | `0bbd0e12886f`  |
| 1547   | No file              | `0bbd0e12886f`  |
| 1537   | No file              | `0bbd0e12886f`  |
| 1529   | No file              | `0bbd0e12886f`  |
| 1524   | No file              | `0bbd0e12886f`  |
| 1519   | No file              | `0bbd0e12886f`  |
| 1509   | No file              | `0bbd0e12886f`  |
| 1506   | No file              | `0bbd0e12886f`  |
| 1504   | No file              | `0bbd0e12886f`  |
| 1500   | No file              | `0bbd0e12886f`  |
| 1493   | No file              | `0bbd0e12886f`  |
| 1489   | No file              | `0bbd0e12886f`  |
| 1485   | No file              | `0bbd0e12886f`  |
| 1481   | No file              | `0bbd0e12886f`  |
| 1474   | No file              | `0bbd0e12886f`  |
| 1466   | No file              | `0bbd0e12886f`  |
| 1462   | No file              | `0bbd0e12886f`  |
| 1459   | No file              | `0bbd0e12886f`  |
| 1453   | No file              | `0bbd0e12886f`  |
| 1450   | No file              | `0bbd0e12886f`  |
| 1445   | No file              | `0bbd0e12886f`  |
| 1439   | No file              | `0bbd0e12886f`  |
| 1433   | No file              | `0bbd0e12886f`  |
| 1430   | No file              | `0bbd0e12886f`  |
| 1426   | No file              | `0bbd0e12886f`  |
| 1421   | No file              | `0bbd0e12886f`  |
| 1417   | No file              | `0bbd0e12886f`  |
| 1416   | No file              | `0bbd0e12886f`  |
| 1409   | No file              | `0bbd0e12886f`  |
| 1405   | No file              | `0bbd0e12886f`  |
| 1401   | No file              | `0bbd0e12886f`  |
| 1396   | No file              | `0bbd0e12886f`  |
| 1391   | No file              | `0bbd0e12886f`  |
| 1390   | No file              | `0bbd0e12886f`  |
| 1386   | No file              | `0bbd0e12886f`  |
| 1381   | No file              | `0bbd0e12886f`  |
| 1379   | No file              | `0bbd0e12886f`  |
| 1372   | No file              | `0bbd0e12886f`  |
| 1366   | No file              | `0bbd0e12886f`  |
| 1364   | No file              | `0bbd0e12886f`  |
| 1363   | No file              | `0bbd0e12886f`  |
| 1360   | No file              | `0bbd0e12886f`  |
| 1358   | No file              | `0bbd0e12886f`  |
| 1355   | No file              | `0bbd0e12886f`  |
| 1351   | No file              | `0bbd0e12886f`  |
| 1348   | No file              | `0bbd0e12886f`  |
| 1346   | No file              | `0bbd0e12886f`  |
| 1341   | No file              | `0bbd0e12886f`  |
| 1340   | No file              | `0bbd0e12886f`  |
| 1338   | No file              | `0bbd0e12886f`  |
| 1335   | No file              | `0bbd0e12886f`  |
| 1333   | No file              | `0bbd0e12886f`  |
| 1329   | No file              | `0bbd0e12886f`  |
| 1327   | No file              | `0bbd0e12886f`  |
| 1324   | No file              | `0bbd0e12886f`  |
| 1321   | No file              | `0bbd0e12886f`  |
| 1319   | No file              | `0bbd0e12886f`  |
| 1318   | No file              | `0bbd0e12886f`  |
| 1316   | No file              | `0bbd0e12886f`  |
| 1313   | No file              | `0bbd0e12886f`  |
| 1311   | No file              | `0bbd0e12886f`  |
| 1309   | No file              | `0bbd0e12886f`  |
| 1304   | No file              | `0bbd0e12886f`  |
| 1292   | No file              | `0bbd0e12886f`  |
| 1286   | No file              | `0bbd0e12886f`  |
| 1280   | No file              | `0bbd0e12886f`  |
| 1276   | No file              | `0bbd0e12886f`  |
| 1267   | No file              | `0bbd0e12886f`  |
| 1261   | No file              | `0bbd0e12886f`  |
| 1256   | No file              | `0bbd0e12886f`  |
| 1250   | No file              | `0bbd0e12886f`  |
| 1246   | No file              | `0bbd0e12886f`  |
| 1239   | No file              | `0bbd0e12886f`  |
| 1230   | No file              | `0bbd0e12886f`  |
| 1226   | No file              | `0bbd0e12886f`  |
| 1220   | No file              | `0bbd0e12886f`  |
| 1217   | No file              | `0bbd0e12886f`  |
| 1211   | No file              | `0bbd0e12886f`  |
| 1210   | No file              | `0bbd0e12886f`  |
| 1208   | No file              | `0bbd0e12886f`  |
| 1203   | No file              | `0bbd0e12886f`  |
| 1197   | No file              | `0bbd0e12886f`  |
| 1194   | No file              | `0bbd0e12886f`  |
| 1192   | No file              | `0bbd0e12886f`  |
| 1187   | No file              | `0bbd0e12886f`  |
| 1183   | No file              | `0bbd0e12886f`  |
| 1177   | No file              | `0bbd0e12886f`  |
| 1173   | No file              | `0bbd0e12886f`  |
| 1167   | No file              | `0bbd0e12886f`  |
| 1164   | No file              | `0bbd0e12886f`  |
| 1156   | No file              | `0bbd0e12886f`  |
| 1149   | No file              | `0bbd0e12886f`  |
| 1144   | No file              | `0bbd0e12886f`  |
| 1137   | No file              | `0bbd0e12886f`  |
| 1132   | No file              | `0bbd0e12886f`  |
| 1127   | No file              | `0bbd0e12886f`  |
| 1122   | No file              | `0bbd0e12886f`  |
| 1118   | No file              | `0bbd0e12886f`  |
| 1114   | No file              | `0bbd0e12886f`  |
| 1109   | No file              | `0bbd0e12886f`  |
| 1102   | No file              | `0bbd0e12886f`  |
| 1096   | No file              | `0bbd0e12886f`  |
| 1088   | No file              | `0bbd0e12886f`  |
| 1081   | No file              | `0bbd0e12886f`  |
| 1076   | No file              | `0bbd0e12886f`  |
| 1069   | No file              | `0bbd0e12886f`  |
| 1064   | No file              | `0bbd0e12886f`  |
| 1058   | No file              | `0bbd0e12886f`  |
| 1051   | No file              | `0bbd0e12886f`  |
| 1044   | No file              | `0bbd0e12886f`  |
| 1036   | No file              | `0bbd0e12886f`  |
| 1026   | No file              | `0bbd0e12886f`  |
| 1016   | No file              | `0bbd0e12886f`  |
| 1009   | No file              | `0bbd0e12886f`  |
| 1005   | No file              | `0bbd0e12886f`  |
| 1000   | No file              | `0bbd0e12886f`  |
| 998    | No file              | `0bbd0e12886f`  |
| 990    | No file              | `0bbd0e12886f`  |
| 979    | No file              | `0bbd0e12886f`  |
| 972    | No file              | `0bbd0e12886f`  |
| 963    | No file              | `0bbd0e12886f`  |
| 955    | No file              | `0bbd0e12886f`  |
| 946    | No file              | `0bbd0e12886f`  |
| 938    | No file              | `0bbd0e12886f`  |
| 927    | No file              | `0bbd0e12886f`  |
| 911    | No file              | `0bbd0e12886f`  |
| 904    | No file              | `0bbd0e12886f`  |
| 899    | No file              | `0bbd0e12886f`  |
| 894    | No file              | `0bbd0e12886f`  |
| 885    | No file              | `0bbd0e12886f`  |
| 879    | No file              | `0bbd0e12886f`  |
| 872    | No file              | `0bbd0e12886f`  |
| 864    | No file              | `0bbd0e12886f`  |
| 855    | No file              | `0bbd0e12886f`  |
| 853    | No file              | `0bbd0e12886f`  |
| 845    | No file              | `0bbd0e12886f`  |
| 837    | No file              | `0bbd0e12886f`  |
| 829    | No file              | `0bbd0e12886f`  |
| 822    | No file              | `0bbd0e12886f`  |
| 814    | No file              | `0bbd0e12886f`  |
| 805    | No file              | `0bbd0e12886f`  |
| 794    | No file              | `0bbd0e12886f`  |
| 787    | No file              | `0bbd0e12886f`  |
| 780    | No file              | `0bbd0e12886f`  |
| 771    | No file              | `0bbd0e12886f`  |
| 760    | No file              | `0bbd0e12886f`  |
| 748    | No file              | `0bbd0e12886f`  |
| 741    | No file              | `0bbd0e12886f`  |
| 736    | No file              | `0bbd0e12886f`  |
| 731    | No file              | `0bbd0e12886f`  |
| 723    | No file              | `0bbd0e12886f`  |
| 711    | No file              | `0bbd0e12886f`  |
| 707    | No file              | `0bbd0e12886f`  |
| 697    | No file              | `0bbd0e12886f`  |
| 689    | No file              | `0bbd0e12886f`  |
| 683    | No file              | `0bbd0e12886f`  |
| 678    | No file              | `0bbd0e12886f`  |
| 670    | No file              | `0bbd0e12886f`  |
| 661    | No file              | `0bbd0e12886f`  |
| 656    | No file              | `0bbd0e12886f`  |
| 652    | No file              | `0bbd0e12886f`  |
| 643    | No file              | `0bbd0e12886f`  |
| 637    | No file              | `0bbd0e12886f`  |
| 630    | No file              | `0bbd0e12886f`  |
| 627    | No file              | `0bbd0e12886f`  |
| 621    | No file              | `0bbd0e12886f`  |
| 617    | No file              | `0bbd0e12886f`  |
| 615    | No file              | `0bbd0e12886f`  |
| 606    | No file              | `0bbd0e12886f`  |
| 599    | No file              | `0bbd0e12886f`  |
| 592    | No file              | `0bbd0e12886f`  |
| 586    | No file              | `0bbd0e12886f`  |
| 577    | No file              | `0bbd0e12886f`  |
| 569    | No file              | `0bbd0e12886f`  |
| 561    | No file              | `0bbd0e12886f`  |
| 554    | No file              | `0bbd0e12886f`  |
| 542    | No file              | `0bbd0e12886f`  |
| 532    | No file              | `0bbd0e12886f`  |
| 531    | No file              | `0bbd0e12886f`  |
| 526    | No file              | `0bbd0e12886f`  |
| 521    | No file              | `0bbd0e12886f`  |
| 517    | No file              | `0bbd0e12886f`  |
| 510    | No file              | `0bbd0e12886f`  |
| 508    | No file              | `0bbd0e12886f`  |
| 504    | No file              | `0bbd0e12886f`  |
| 497    | No file              | `0bbd0e12886f`  |
| 491    | No file              | `0bbd0e12886f`  |
| 485    | No file              | `0bbd0e12886f`  |
| 478    | No file              | `0bbd0e12886f`  |
| 472    | No file              | `0bbd0e12886f`  |
| 466    | No file              | `0bbd0e12886f`  |
| 457    | No file              | `0bbd0e12886f`  |
| 452    | No file              | `0bbd0e12886f`  |
| 449    | No file              | `0bbd0e12886f`  |
| 435    | No file              | `0bbd0e12886f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field      | Notes                          |
| ------- | ---- | ---------- | ------------------------------ |
| `+0x00` | f32  | unknown_00 | `60` on clients 3251 and 3474  |
| `+0x04` | f32  | unknown_04 | `115` on clients 3251 and 3474 |
| `+0x08` | f32  | unknown_08 | `400` on clients 3251 and 3474 |
| `+0x0C` | f32  | unknown_0c | `37` on clients 3251 and 3474  |
| `+0x10` | f32  | unknown_10 | `57` on clients 3251 and 3474  |

## Layout 1

### File Layout

| Offset  | Type | Field      | Notes                |
| ------- | ---- | ---------- | -------------------- |
| `+0x00` | f32  | unknown_00 | `200` on client 3002 |
| `+0x04` | f32  | unknown_04 | `200` on client 3002 |
| `+0x08` | f32  | unknown_08 | `200` on client 3002 |

## Notes

- Raw bytes on client 3474:
  `00 00 70 42 00 00 E6 42 00 00 C8 43 00 00 14 42 00 00 64 42`
  (20 bytes). Client 3251 has the same bytes; client 3002 has
  `00 00 48 43` three times (12 bytes).
- Every value is a whole number as f32. Read as u32 they lie between
  `1108606976` and `1137180672`, so f32 is the reading.
- The file is not in the archives of clients 1784, 2107 and 2519.
- Layout 1 gives its three fields the names of the first three Layout 2
  fields by offset. Whether they hold the same options is not shown by the
  data: all three changed from `200` between clients 3002 and 3251.
- The other `*etcoptionstaticstatus.bss` files (`edania`,
  `hardcorechannel`) start with the PABR magic; this file does not.
- The handler for the option tables (`_bss/pabr_values/`) previews Layout 2
  with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, and raises on a file of any other size. With no confirmed
  field, the preview shows the raw value bytes.

## Open Questions

### Solare Option Values

No source names the five values. The client Lua on client 3473 (152 of the
3,073 `.luac` files name Solare) has no function with `SolareEtc` or
`SolareOption` in its name; the only `EtcOption` getter is
`ToClient_GetEdaniaEtcOption`. The installed `BlackDesert64.exe` (client
3474) holds no `Solare` text as ASCII or UTF-16, so it does not show the
loader or its struct. The 2016 PDB has no `Solare` text. A private
server's `DataSheets.bexcel` on client 1784 has no sheet or column with
`Solare` in its name, its `.xlsm` folders no such file, and its server dump
no such text; the `EtcOption` sheet there is the general option sheet, with
house auction, trade and worker columns.
