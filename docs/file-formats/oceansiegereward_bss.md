# `oceansiegereward.bss` Format

## Purpose

The Blue Battlefield (ocean siege) rewards: per row a u16, five reward
sets of four item lists each, one more item list and two skill keys. On
client 3482 the one row's sets hand out an Oceanstrider (Tier 3, sets 1
to 3), Oceanbreaker (Tier 4) or Oceanlord (Tier 5) Triumph Box with two
Combat Secret Books (M), 1,000 Crow Coins, three Secret Books of Florin
and an Oceanlord Triumph Box of Resilience; the last list a Waveworn
Resolve Box with two Combat Secret Books (S). The skills are Glorious
Life (Standard) and (Basic).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ----------------------- | --------- |
| 2      | 3473 and later | 3483    | `oceansiegereward.bss` | 630   | 27 Reward, 5 Reward Set | 16        |
| 1      | 3111 to 3464   | 3464    | `oceansiegereward.bss` | 282   | 21 Reward, 5 Reward Set | 12        |

| Layout | File                   | Known         | Unknown       |
| ------ | ---------------------- | ------------- | ------------- |
| 2      | `oceansiegereward.bss` | 352 B (55.9%) | 278 B (44.1%) |
| 1      | `oceansiegereward.bss` | 280 B (99.3%) | 2 B (0.7%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `5ad725c4f21f`  |
| 3482   | Layout 2 | `5ad725c4f21f`  |
| 3474   | Layout 2 | `5ad725c4f21f`  |
| 3473   | Layout 2 | `5ad725c4f21f`  |
| 3464   | Layout 1 | `5ad725c4f21f`  |
| 3458   | Layout 1 | `5ad725c4f21f`  |
| 3454   | Layout 1 | `5ad725c4f21f`  |
| 3444   | Layout 1 | `5ad725c4f21f`  |
| 3435   | Layout 1 | `5ad725c4f21f`  |
| 3426   | Layout 1 | `5ad725c4f21f`  |
| 3418   | Layout 1 | `5ad725c4f21f`  |
| 3412   | Layout 1 | `5ad725c4f21f`  |
| 3402   | Layout 1 | `5ad725c4f21f`  |
| 3396   | Layout 1 | `5ad725c4f21f`  |
| 3387   | Layout 1 | `5ad725c4f21f`  |
| 3381   | Layout 1 | `5ad725c4f21f`  |
| 3373   | Layout 1 | `5ad725c4f21f`  |
| 3364   | Layout 1 | `5ad725c4f21f`  |
| 3356   | Layout 1 | `5ad725c4f21f`  |
| 3349   | Layout 1 | `5ad725c4f21f`  |
| 3342   | Layout 1 | `5ad725c4f21f`  |
| 3335   | Layout 1 | `5ad725c4f21f`  |
| 3326   | Layout 1 | `5ad725c4f21f`  |
| 3321   | Layout 1 | `5ad725c4f21f`  |
| 3314   | Layout 1 | `5ad725c4f21f`  |
| 3303   | Layout 1 | `5ad725c4f21f`  |
| 3302   | Layout 1 | `5ad725c4f21f`  |
| 3293   | Layout 1 | `5ad725c4f21f`  |
| 3283   | Layout 1 | `5ad725c4f21f`  |
| 3275   | Layout 1 | `5ad725c4f21f`  |
| 3267   | Layout 1 | `5ad725c4f21f`  |
| 3258   | Layout 1 | `5ad725c4f21f`  |
| 3251   | Layout 1 | `5ad725c4f21f`  |
| 3242   | Layout 1 | `5ad725c4f21f`  |
| 3235   | Layout 1 | `5ad725c4f21f`  |
| 3229   | Layout 1 | `5ad725c4f21f`  |
| 3212   | Layout 1 | `5ad725c4f21f`  |
| 3203   | Layout 1 | `5ad725c4f21f`  |
| 3193   | Layout 1 | `5ad725c4f21f`  |
| 3186   | Layout 1 | `5ad725c4f21f`  |
| 3177   | Layout 1 | `5ad725c4f21f`  |
| 3169   | Layout 1 | `5ad725c4f21f`  |
| 3158   | Layout 1 | `5ad725c4f21f`  |
| 3151   | Layout 1 | `5ad725c4f21f`  |
| 3144   | Layout 1 | `5ad725c4f21f`  |
| 3133   | Layout 1 | `5ad725c4f21f`  |
| 3125   | Layout 1 | `5ad725c4f21f`  |
| 3118   | Layout 1 | `5ad725c4f21f`  |
| 3111   | Layout 1 | `5ad725c4f21f`  |
| 3103   | No file  | `5ad725c4f21f`  |
| 3095   | No file  | `5ad725c4f21f`  |
| 3086   | No file  | `5ad725c4f21f`  |
| 3072   | No file  | `5ad725c4f21f`  |
| 3062   | No file  | `5ad725c4f21f`  |
| 3052   | No file  | `5ad725c4f21f`  |
| 3045   | No file  | `5ad725c4f21f`  |
| 3037   | No file  | `5ad725c4f21f`  |
| 3030   | No file  | `5ad725c4f21f`  |
| 3021   | No file  | `5ad725c4f21f`  |
| 3012   | No file  | `5ad725c4f21f`  |
| 3002   | No file  | `5ad725c4f21f`  |
| 2995   | No file  | `5ad725c4f21f`  |
| 2987   | No file  | `5ad725c4f21f`  |
| 2978   | No file  | `5ad725c4f21f`  |
| 2970   | No file  | `5ad725c4f21f`  |
| 2959   | No file  | `5ad725c4f21f`  |
| 2951   | No file  | `5ad725c4f21f`  |
| 2942   | No file  | `5ad725c4f21f`  |
| 2935   | No file  | `5ad725c4f21f`  |
| 2932   | No file  | `5ad725c4f21f`  |
| 2923   | No file  | `5ad725c4f21f`  |
| 2919   | No file  | `5ad725c4f21f`  |
| 2907   | No file  | `5ad725c4f21f`  |
| 2900   | No file  | `5ad725c4f21f`  |
| 2891   | No file  | `5ad725c4f21f`  |
| 2882   | No file  | `5ad725c4f21f`  |
| 2872   | No file  | `5ad725c4f21f`  |
| 2863   | No file  | `5ad725c4f21f`  |
| 2855   | No file  | `5ad725c4f21f`  |
| 2849   | No file  | `5ad725c4f21f`  |
| 2844   | No file  | `5ad725c4f21f`  |
| 2834   | No file  | `5ad725c4f21f`  |
| 2825   | No file  | `5ad725c4f21f`  |
| 2819   | No file  | `5ad725c4f21f`  |
| 2811   | No file  | `5ad725c4f21f`  |
| 2803   | No file  | `5ad725c4f21f`  |
| 2794   | No file  | `5ad725c4f21f`  |
| 2783   | No file  | `5ad725c4f21f`  |
| 2774   | No file  | `5ad725c4f21f`  |
| 2765   | No file  | `5ad725c4f21f`  |
| 2756   | No file  | `5ad725c4f21f`  |
| 2750   | No file  | `5ad725c4f21f`  |
| 2743   | No file  | `5ad725c4f21f`  |
| 2736   | No file  | `5ad725c4f21f`  |
| 2726   | No file  | `5ad725c4f21f`  |
| 2717   | No file  | `5ad725c4f21f`  |
| 2709   | No file  | `5ad725c4f21f`  |
| 2703   | No file  | `5ad725c4f21f`  |
| 2695   | No file  | `5ad725c4f21f`  |
| 2684   | No file  | `5ad725c4f21f`  |
| 2672   | No file  | `5ad725c4f21f`  |
| 2665   | No file  | `5ad725c4f21f`  |
| 2657   | No file  | `5ad725c4f21f`  |
| 2649   | No file  | `5ad725c4f21f`  |
| 2644   | No file  | `5ad725c4f21f`  |
| 2637   | No file  | `5ad725c4f21f`  |
| 2629   | No file  | `5ad725c4f21f`  |
| 2619   | No file  | `5ad725c4f21f`  |
| 2612   | No file  | `5ad725c4f21f`  |
| 2606   | No file  | `5ad725c4f21f`  |
| 2602   | No file  | `5ad725c4f21f`  |
| 2601   | No file  | `5ad725c4f21f`  |
| 2592   | No file  | `5ad725c4f21f`  |
| 2583   | No file  | `5ad725c4f21f`  |
| 2575   | No file  | `5ad725c4f21f`  |
| 2567   | No file  | `5ad725c4f21f`  |
| 2560   | No file  | `5ad725c4f21f`  |
| 2553   | No file  | `5ad725c4f21f`  |
| 2545   | No file  | `5ad725c4f21f`  |
| 2538   | No file  | `5ad725c4f21f`  |
| 2529   | No file  | `5ad725c4f21f`  |
| 2519   | No file  | `5ad725c4f21f`  |
| 2513   | No file  | `5ad725c4f21f`  |
| 2510   | No file  | `5ad725c4f21f`  |
| 2507   | No file  | `5ad725c4f21f`  |
| 2503   | No file  | `5ad725c4f21f`  |
| 2498   | No file  | `5ad725c4f21f`  |
| 2492   | No file  | `5ad725c4f21f`  |
| 2487   | No file  | `5ad725c4f21f`  |
| 2480   | No file  | `5ad725c4f21f`  |
| 2474   | No file  | `5ad725c4f21f`  |
| 2468   | No file  | `5ad725c4f21f`  |
| 2460   | No file  | `5ad725c4f21f`  |
| 2453   | No file  | `5ad725c4f21f`  |
| 2444   | No file  | `5ad725c4f21f`  |
| 2438   | No file  | `5ad725c4f21f`  |
| 2434   | No file  | `5ad725c4f21f`  |
| 2429   | No file  | `5ad725c4f21f`  |
| 2421   | No file  | `5ad725c4f21f`  |
| 2414   | No file  | `5ad725c4f21f`  |
| 2407   | No file  | `5ad725c4f21f`  |
| 2401   | No file  | `5ad725c4f21f`  |
| 2397   | No file  | `5ad725c4f21f`  |
| 2393   | No file  | `5ad725c4f21f`  |
| 2384   | No file  | `5ad725c4f21f`  |
| 2378   | No file  | `5ad725c4f21f`  |
| 2372   | No file  | `5ad725c4f21f`  |
| 2358   | No file  | `5ad725c4f21f`  |
| 2352   | No file  | `5ad725c4f21f`  |
| 2347   | No file  | `5ad725c4f21f`  |
| 2343   | No file  | `5ad725c4f21f`  |
| 2335   | No file  | `5ad725c4f21f`  |
| 2327   | No file  | `5ad725c4f21f`  |
| 2324   | No file  | `5ad725c4f21f`  |
| 2319   | No file  | `5ad725c4f21f`  |
| 2313   | No file  | `5ad725c4f21f`  |
| 2308   | No file  | `5ad725c4f21f`  |
| 2302   | No file  | `5ad725c4f21f`  |
| 2295   | No file  | `5ad725c4f21f`  |
| 2290   | No file  | `5ad725c4f21f`  |
| 2284   | No file  | `5ad725c4f21f`  |
| 2276   | No file  | `5ad725c4f21f`  |
| 2269   | No file  | `5ad725c4f21f`  |
| 2259   | No file  | `5ad725c4f21f`  |
| 2250   | No file  | `5ad725c4f21f`  |
| 2243   | No file  | `5ad725c4f21f`  |
| 2235   | No file  | `5ad725c4f21f`  |
| 2229   | No file  | `5ad725c4f21f`  |
| 2224   | No file  | `5ad725c4f21f`  |
| 2218   | No file  | `5ad725c4f21f`  |
| 2215   | No file  | `5ad725c4f21f`  |
| 2207   | No file  | `5ad725c4f21f`  |
| 2203   | No file  | `5ad725c4f21f`  |
| 2196   | No file  | `5ad725c4f21f`  |
| 2192   | No file  | `5ad725c4f21f`  |
| 2189   | No file  | `5ad725c4f21f`  |
| 2183   | No file  | `5ad725c4f21f`  |
| 2179   | No file  | `5ad725c4f21f`  |
| 2171   | No file  | `5ad725c4f21f`  |
| 2163   | No file  | `5ad725c4f21f`  |
| 2156   | No file  | `5ad725c4f21f`  |
| 2151   | No file  | `5ad725c4f21f`  |
| 2147   | No file  | `5ad725c4f21f`  |
| 2142   | No file  | `5ad725c4f21f`  |
| 2138   | No file  | `5ad725c4f21f`  |
| 2134   | No file  | `5ad725c4f21f`  |
| 2130   | No file  | `5ad725c4f21f`  |
| 2122   | No file  | `5ad725c4f21f`  |
| 2107   | No file  | `5ad725c4f21f`  |
| 2098   | No file  | `5ad725c4f21f`  |
| 2089   | No file  | `5ad725c4f21f`  |
| 2081   | No file  | `5ad725c4f21f`  |
| 2073   | No file  | `5ad725c4f21f`  |
| 2067   | No file  | `5ad725c4f21f`  |
| 2063   | No file  | `5ad725c4f21f`  |
| 2059   | No file  | `5ad725c4f21f`  |
| 2052   | No file  | `5ad725c4f21f`  |
| 2044   | No file  | `5ad725c4f21f`  |
| 2039   | No file  | `5ad725c4f21f`  |
| 2032   | No file  | `5ad725c4f21f`  |
| 2025   | No file  | `5ad725c4f21f`  |
| 2011   | No file  | `5ad725c4f21f`  |
| 2005   | No file  | `5ad725c4f21f`  |
| 2000   | No file  | `5ad725c4f21f`  |
| 1996   | No file  | `5ad725c4f21f`  |
| 1991   | No file  | `5ad725c4f21f`  |
| 1985   | No file  | `5ad725c4f21f`  |
| 1980   | No file  | `5ad725c4f21f`  |
| 1969   | No file  | `5ad725c4f21f`  |
| 1964   | No file  | `5ad725c4f21f`  |
| 1958   | No file  | `5ad725c4f21f`  |
| 1950   | No file  | `5ad725c4f21f`  |
| 1945   | No file  | `5ad725c4f21f`  |
| 1937   | No file  | `5ad725c4f21f`  |
| 1933   | No file  | `5ad725c4f21f`  |
| 1927   | No file  | `5ad725c4f21f`  |
| 1921   | No file  | `5ad725c4f21f`  |
| 1914   | No file  | `5ad725c4f21f`  |
| 1908   | No file  | `5ad725c4f21f`  |
| 1897   | No file  | `5ad725c4f21f`  |
| 1892   | No file  | `5ad725c4f21f`  |
| 1886   | No file  | `5ad725c4f21f`  |
| 1881   | No file  | `5ad725c4f21f`  |
| 1871   | No file  | `5ad725c4f21f`  |
| 1866   | No file  | `5ad725c4f21f`  |
| 1862   | No file  | `5ad725c4f21f`  |
| 1854   | No file  | `5ad725c4f21f`  |
| 1846   | No file  | `5ad725c4f21f`  |
| 1838   | No file  | `5ad725c4f21f`  |
| 1832   | No file  | `5ad725c4f21f`  |
| 1826   | No file  | `5ad725c4f21f`  |
| 1822   | No file  | `5ad725c4f21f`  |
| 1818   | No file  | `5ad725c4f21f`  |
| 1804   | No file  | `5ad725c4f21f`  |
| 1794   | No file  | `5ad725c4f21f`  |
| 1790   | No file  | `5ad725c4f21f`  |
| 1784   | No file  | `5ad725c4f21f`  |
| 1774   | No file  | `5ad725c4f21f`  |
| 1771   | No file  | `5ad725c4f21f`  |
| 1762   | No file  | `5ad725c4f21f`  |
| 1759   | No file  | `5ad725c4f21f`  |
| 1754   | No file  | `5ad725c4f21f`  |
| 1749   | No file  | `5ad725c4f21f`  |
| 1743   | No file  | `5ad725c4f21f`  |
| 1737   | No file  | `5ad725c4f21f`  |
| 1731   | No file  | `5ad725c4f21f`  |
| 1725   | No file  | `5ad725c4f21f`  |
| 1717   | No file  | `5ad725c4f21f`  |
| 1710   | No file  | `5ad725c4f21f`  |
| 1704   | No file  | `5ad725c4f21f`  |
| 1698   | No file  | `5ad725c4f21f`  |
| 1690   | No file  | `5ad725c4f21f`  |
| 1685   | No file  | `5ad725c4f21f`  |
| 1680   | No file  | `5ad725c4f21f`  |
| 1674   | No file  | `5ad725c4f21f`  |
| 1668   | No file  | `5ad725c4f21f`  |
| 1659   | No file  | `5ad725c4f21f`  |
| 1649   | No file  | `5ad725c4f21f`  |
| 1642   | No file  | `5ad725c4f21f`  |
| 1636   | No file  | `5ad725c4f21f`  |
| 1628   | No file  | `5ad725c4f21f`  |
| 1622   | No file  | `5ad725c4f21f`  |
| 1614   | No file  | `5ad725c4f21f`  |
| 1608   | No file  | `5ad725c4f21f`  |
| 1602   | No file  | `5ad725c4f21f`  |
| 1598   | No file  | `5ad725c4f21f`  |
| 1594   | No file  | `5ad725c4f21f`  |
| 1590   | No file  | `5ad725c4f21f`  |
| 1587   | No file  | `5ad725c4f21f`  |
| 1584   | No file  | `5ad725c4f21f`  |
| 1579   | No file  | `5ad725c4f21f`  |
| 1572   | No file  | `5ad725c4f21f`  |
| 1565   | No file  | `5ad725c4f21f`  |
| 1559   | No file  | `5ad725c4f21f`  |
| 1554   | No file  | `5ad725c4f21f`  |
| 1547   | No file  | `5ad725c4f21f`  |
| 1537   | No file  | `5ad725c4f21f`  |
| 1529   | No file  | `5ad725c4f21f`  |
| 1524   | No file  | `5ad725c4f21f`  |
| 1519   | No file  | `5ad725c4f21f`  |
| 1509   | No file  | `5ad725c4f21f`  |
| 1506   | No file  | `5ad725c4f21f`  |
| 1504   | No file  | `5ad725c4f21f`  |
| 1500   | No file  | `5ad725c4f21f`  |
| 1493   | No file  | `5ad725c4f21f`  |
| 1489   | No file  | `5ad725c4f21f`  |
| 1485   | No file  | `5ad725c4f21f`  |
| 1481   | No file  | `5ad725c4f21f`  |
| 1474   | No file  | `5ad725c4f21f`  |
| 1466   | No file  | `5ad725c4f21f`  |
| 1462   | No file  | `5ad725c4f21f`  |
| 1459   | No file  | `5ad725c4f21f`  |
| 1453   | No file  | `5ad725c4f21f`  |
| 1450   | No file  | `5ad725c4f21f`  |
| 1445   | No file  | `5ad725c4f21f`  |
| 1439   | No file  | `5ad725c4f21f`  |
| 1433   | No file  | `5ad725c4f21f`  |
| 1430   | No file  | `5ad725c4f21f`  |
| 1426   | No file  | `5ad725c4f21f`  |
| 1421   | No file  | `5ad725c4f21f`  |
| 1417   | No file  | `5ad725c4f21f`  |
| 1416   | No file  | `5ad725c4f21f`  |
| 1409   | No file  | `5ad725c4f21f`  |
| 1405   | No file  | `5ad725c4f21f`  |
| 1401   | No file  | `5ad725c4f21f`  |
| 1396   | No file  | `5ad725c4f21f`  |
| 1391   | No file  | `5ad725c4f21f`  |
| 1390   | No file  | `5ad725c4f21f`  |
| 1386   | No file  | `5ad725c4f21f`  |
| 1381   | No file  | `5ad725c4f21f`  |
| 1379   | No file  | `5ad725c4f21f`  |
| 1372   | No file  | `5ad725c4f21f`  |
| 1366   | No file  | `5ad725c4f21f`  |
| 1364   | No file  | `5ad725c4f21f`  |
| 1363   | No file  | `5ad725c4f21f`  |
| 1360   | No file  | `5ad725c4f21f`  |
| 1358   | No file  | `5ad725c4f21f`  |
| 1355   | No file  | `5ad725c4f21f`  |
| 1351   | No file  | `5ad725c4f21f`  |
| 1348   | No file  | `5ad725c4f21f`  |
| 1346   | No file  | `5ad725c4f21f`  |
| 1341   | No file  | `5ad725c4f21f`  |
| 1340   | No file  | `5ad725c4f21f`  |
| 1338   | No file  | `5ad725c4f21f`  |
| 1335   | No file  | `5ad725c4f21f`  |
| 1333   | No file  | `5ad725c4f21f`  |
| 1329   | No file  | `5ad725c4f21f`  |
| 1327   | No file  | `5ad725c4f21f`  |
| 1324   | No file  | `5ad725c4f21f`  |
| 1321   | No file  | `5ad725c4f21f`  |
| 1319   | No file  | `5ad725c4f21f`  |
| 1318   | No file  | `5ad725c4f21f`  |
| 1316   | No file  | `5ad725c4f21f`  |
| 1313   | No file  | `5ad725c4f21f`  |
| 1311   | No file  | `5ad725c4f21f`  |
| 1309   | No file  | `5ad725c4f21f`  |
| 1304   | No file  | `5ad725c4f21f`  |
| 1292   | No file  | `5ad725c4f21f`  |
| 1286   | No file  | `5ad725c4f21f`  |
| 1280   | No file  | `5ad725c4f21f`  |
| 1276   | No file  | `5ad725c4f21f`  |
| 1267   | No file  | `5ad725c4f21f`  |
| 1261   | No file  | `5ad725c4f21f`  |
| 1256   | No file  | `5ad725c4f21f`  |
| 1250   | No file  | `5ad725c4f21f`  |
| 1246   | No file  | `5ad725c4f21f`  |
| 1239   | No file  | `5ad725c4f21f`  |
| 1230   | No file  | `5ad725c4f21f`  |
| 1226   | No file  | `5ad725c4f21f`  |
| 1220   | No file  | `5ad725c4f21f`  |
| 1217   | No file  | `5ad725c4f21f`  |
| 1211   | No file  | `5ad725c4f21f`  |
| 1210   | No file  | `5ad725c4f21f`  |
| 1208   | No file  | `5ad725c4f21f`  |
| 1203   | No file  | `5ad725c4f21f`  |
| 1197   | No file  | `5ad725c4f21f`  |
| 1194   | No file  | `5ad725c4f21f`  |
| 1192   | No file  | `5ad725c4f21f`  |
| 1187   | No file  | `5ad725c4f21f`  |
| 1183   | No file  | `5ad725c4f21f`  |
| 1177   | No file  | `5ad725c4f21f`  |
| 1173   | No file  | `5ad725c4f21f`  |
| 1167   | No file  | `5ad725c4f21f`  |
| 1164   | No file  | `5ad725c4f21f`  |
| 1156   | No file  | `5ad725c4f21f`  |
| 1149   | No file  | `5ad725c4f21f`  |
| 1144   | No file  | `5ad725c4f21f`  |
| 1137   | No file  | `5ad725c4f21f`  |
| 1132   | No file  | `5ad725c4f21f`  |
| 1127   | No file  | `5ad725c4f21f`  |
| 1122   | No file  | `5ad725c4f21f`  |
| 1118   | No file  | `5ad725c4f21f`  |
| 1114   | No file  | `5ad725c4f21f`  |
| 1109   | No file  | `5ad725c4f21f`  |
| 1102   | No file  | `5ad725c4f21f`  |
| 1096   | No file  | `5ad725c4f21f`  |
| 1088   | No file  | `5ad725c4f21f`  |
| 1081   | No file  | `5ad725c4f21f`  |
| 1076   | No file  | `5ad725c4f21f`  |
| 1069   | No file  | `5ad725c4f21f`  |
| 1064   | No file  | `5ad725c4f21f`  |
| 1058   | No file  | `5ad725c4f21f`  |
| 1051   | No file  | `5ad725c4f21f`  |
| 1044   | No file  | `5ad725c4f21f`  |
| 1036   | No file  | `5ad725c4f21f`  |
| 1026   | No file  | `5ad725c4f21f`  |
| 1016   | No file  | `5ad725c4f21f`  |
| 1009   | No file  | `5ad725c4f21f`  |
| 1005   | No file  | `5ad725c4f21f`  |
| 1000   | No file  | `5ad725c4f21f`  |
| 998    | No file  | `5ad725c4f21f`  |
| 990    | No file  | `5ad725c4f21f`  |
| 979    | No file  | `5ad725c4f21f`  |
| 972    | No file  | `5ad725c4f21f`  |
| 963    | No file  | `5ad725c4f21f`  |
| 955    | No file  | `5ad725c4f21f`  |
| 946    | No file  | `5ad725c4f21f`  |
| 938    | No file  | `5ad725c4f21f`  |
| 927    | No file  | `5ad725c4f21f`  |
| 911    | No file  | `5ad725c4f21f`  |
| 904    | No file  | `5ad725c4f21f`  |
| 899    | No file  | `5ad725c4f21f`  |
| 894    | No file  | `5ad725c4f21f`  |
| 885    | No file  | `5ad725c4f21f`  |
| 879    | No file  | `5ad725c4f21f`  |
| 872    | No file  | `5ad725c4f21f`  |
| 864    | No file  | `5ad725c4f21f`  |
| 855    | No file  | `5ad725c4f21f`  |
| 853    | No file  | `5ad725c4f21f`  |
| 845    | No file  | `5ad725c4f21f`  |
| 837    | No file  | `5ad725c4f21f`  |
| 829    | No file  | `5ad725c4f21f`  |
| 822    | No file  | `5ad725c4f21f`  |
| 814    | No file  | `5ad725c4f21f`  |
| 805    | No file  | `5ad725c4f21f`  |
| 794    | No file  | `5ad725c4f21f`  |
| 787    | No file  | `5ad725c4f21f`  |
| 780    | No file  | `5ad725c4f21f`  |
| 771    | No file  | `5ad725c4f21f`  |
| 760    | No file  | `5ad725c4f21f`  |
| 748    | No file  | `5ad725c4f21f`  |
| 741    | No file  | `5ad725c4f21f`  |
| 736    | No file  | `5ad725c4f21f`  |
| 731    | No file  | `5ad725c4f21f`  |
| 723    | No file  | `5ad725c4f21f`  |
| 711    | No file  | `5ad725c4f21f`  |
| 707    | No file  | `5ad725c4f21f`  |
| 697    | No file  | `5ad725c4f21f`  |
| 689    | No file  | `5ad725c4f21f`  |
| 683    | No file  | `5ad725c4f21f`  |
| 678    | No file  | `5ad725c4f21f`  |
| 670    | No file  | `5ad725c4f21f`  |
| 661    | No file  | `5ad725c4f21f`  |
| 656    | No file  | `5ad725c4f21f`  |
| 652    | No file  | `5ad725c4f21f`  |
| 643    | No file  | `5ad725c4f21f`  |
| 637    | No file  | `5ad725c4f21f`  |
| 630    | No file  | `5ad725c4f21f`  |
| 627    | No file  | `5ad725c4f21f`  |
| 621    | No file  | `5ad725c4f21f`  |
| 617    | No file  | `5ad725c4f21f`  |
| 615    | No file  | `5ad725c4f21f`  |
| 606    | No file  | `5ad725c4f21f`  |
| 599    | No file  | `5ad725c4f21f`  |
| 592    | No file  | `5ad725c4f21f`  |
| 586    | No file  | `5ad725c4f21f`  |
| 577    | No file  | `5ad725c4f21f`  |
| 569    | No file  | `5ad725c4f21f`  |
| 561    | No file  | `5ad725c4f21f`  |
| 554    | No file  | `5ad725c4f21f`  |
| 542    | No file  | `5ad725c4f21f`  |
| 532    | No file  | `5ad725c4f21f`  |
| 531    | No file  | `5ad725c4f21f`  |
| 526    | No file  | `5ad725c4f21f`  |
| 521    | No file  | `5ad725c4f21f`  |
| 517    | No file  | `5ad725c4f21f`  |
| 510    | No file  | `5ad725c4f21f`  |
| 508    | No file  | `5ad725c4f21f`  |
| 504    | No file  | `5ad725c4f21f`  |
| 497    | No file  | `5ad725c4f21f`  |
| 491    | No file  | `5ad725c4f21f`  |
| 485    | No file  | `5ad725c4f21f`  |
| 478    | No file  | `5ad725c4f21f`  |
| 472    | No file  | `5ad725c4f21f`  |
| 466    | No file  | `5ad725c4f21f`  |
| 457    | No file  | `5ad725c4f21f`  |
| 452    | No file  | `5ad725c4f21f`  |
| 449    | No file  | `5ad725c4f21f`  |
| 435    | No file  | `5ad725c4f21f`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), skill names (LOC type 10) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `1` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 18 bytes + reward sets and rewards)

| Offset                 | Type                         | Field                | Notes                                                              |
| ---------------------- | ---------------------------- | -------------------- | ------------------------------------------------------------------ |
| `+0x00`                | u16                          | unknown_00           | `0`; see Open Questions                                            |
| `+0x02`                | Reward Set[5]                | reward_sets          | See Reward Set and Reward Sets                                     |
| `reward_sets+0x00`     | u64                          | unknown_reward_count | Number of `unknown_rewards`                                        |
| `reward_sets+0x08`     | Reward[unknown_reward_count] | unknown_rewards      | The Waveworn Resolve Box and its books on client 3482              |
| `unknown_rewards+0x00` | u32                          | skill_key_1          | Skill number, LOC type 10 name; `47462` Glorious Life (Standard)   |
| `unknown_rewards+0x04` | u32                          | skill_key_2          | `47463` Glorious Life (Basic)                                      |

### Reward Set (variable: 32 bytes + rewards)

| Offset                   | Type                           | Field                  | Notes                                     |
| ------------------------ | ------------------------------ | ---------------------- | ----------------------------------------- |
| `+0x00`                  | u64                            | unknown_reward_count_1 | Number of `unknown_rewards_1`             |
| `+0x08`                  | Reward[unknown_reward_count_1] | unknown_rewards_1      | A Triumph Box and Combat Secret Books     |
| `unknown_rewards_1+0x00` | u64                            | unknown_reward_count_2 | Number of `unknown_rewards_2`             |
| `unknown_rewards_1+0x08` | Reward[unknown_reward_count_2] | unknown_rewards_2      | Bundle of 1,000 Crow Coins                |
| `unknown_rewards_2+0x00` | u64                            | unknown_reward_count_3 | Number of `unknown_rewards_3`             |
| `unknown_rewards_2+0x08` | Reward[unknown_reward_count_3] | unknown_rewards_3      | Secret Book of Florin                     |
| `unknown_rewards_3+0x00` | u64                            | unknown_reward_count_4 | Number of `unknown_rewards_4`             |
| `unknown_rewards_3+0x08` | Reward[unknown_reward_count_4] | unknown_rewards_4      | Oceanlord Triumph Box of Resilience       |

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                              |
| ------- | -------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name  |
| `+0x04` | bytes[4] | unknown_04 | `A4 00 00 00` on every reward of client 3482; see Notes            |
| `+0x08` | u64      | count      | How many of the item                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (262 bytes)

| Offset  | Type          | Field           | Notes                     |
| ------- | ------------- | --------------- | ------------------------- |
| `+0x00` | u16           | unknown_00      | `0`                       |
| `+0x02` | Reward Set[5] | reward_sets     | See Reward Set            |
| `+0xF2` | Reward        | unknown_rewards | One item, no count before |
| `+0xFE` | u32           | skill_key_1     |                           |
| `+0x102` | u32          | skill_key_2     |                           |

### Reward Set (48 bytes)

| Offset  | Type   | Field             | Notes |
| ------- | ------ | ----------------- | ----- |
| `+0x00` | Reward | unknown_rewards_1 |       |
| `+0x0C` | Reward | unknown_rewards_2 |       |
| `+0x18` | Reward | unknown_rewards_3 |       |
| `+0x24` | Reward | unknown_rewards_4 |       |

### Reward (12 bytes)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id |       |
| `+0x04` | u64  | count   |       |

## Reward Sets

Client 3482; the names are LOC type 0. The sets differ in the box of
`unknown_rewards_1` only:

| Set     | `unknown_rewards_1`                                             |
| ------- | --------------------------------------------------------------- |
| 1 to 3  | Oceanstrider Triumph Box (Tier 3) x1, Combat Secret Book (M) x2 |
| 4       | Oceanbreaker Triumph Box (Tier 4) x1, Combat Secret Book (M) x2 |
| 5       | Oceanlord Triumph Box (Tier 5) x1, Combat Secret Book (M) x2    |

In every set `unknown_rewards_2` holds Bundle of 1,000 Crow Coins x1,
`unknown_rewards_3` Secret Book of Florin x3 and `unknown_rewards_4`
Oceanlord Triumph Box of Resilience x1. `unknown_rewards` holds Waveworn
Resolve Box x1 and Combat Secret Book (S) x2.

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it, and no Lua function of client 3482 reads its rewards
(the result window shows the reward item the server sends). The reward
entries have the shape of the rewards of
[`rosewarrewardstaticstatus.bss`](rosewarrewardstaticstatus_bss.md), whose
names they take: every `item_id` is an item with a LOC type 0 name, the
count a plain number. `skill_key_1` and `skill_key_2` are skill numbers:
`47462` and `47463` are 영예로운 생활 (하) and (최하), Glorious Life
(Standard) and (Basic) in LOC type 10, and the land siege table
`siege2024rewardstaticstatus.bss`, which has the same row shape, ends its
three rows with the pairs of 영예로운 전투, 생활 (Glorious Combat, Life)
`58478, 58479`, `58477, 58478` and `58475, 58476`. What each list and each
skill is for stays open.

## Notes

- Client 3251 uses Layout 1, one item per list with no counts (282
  bytes): the same boxes, Crow Coins and Florin books, without the Combat
  Secret Books, and the same two skills. Client 3474 turns each list into
  a counted list. The file is not in the archives of client 1784.
- The LOC text of every Triumph Box and of the Triumph Box of Resilience
  says it is "issued to those who achieve glorious victory on the Blue
  Battlefield"; the Waveworn Resolve Box text says "to those whose
  maritime resolve remained determined throughout".
- `unknown_04` is `A4 00 00 00` on all 27 rewards of client 3482, where
  `rosewarrewardstaticstatus.bss` has `FC 7F 00 00` and
  `siege2024rewardstaticstatus.bss` has `A4 00 00 00` too: the upper half
  of an 8-byte slot the item ID sits in, not cleared by the tool that
  wrote the file.
- The handler (`_bss/oceansiegereward/`) shows one row per reward item:
  the item with its icon, name and count, its set (1 to 5, empty for
  `unknown_rewards`), its list (1 to 4) and the row's two skills, in file
  order. It previews `siege2024rewardstaticstatus.bss` the same way; both
  read their rewards with `_common/reward_items.py`.

## Open Questions

### What the Sets and Lists Stand For

The five sets differ only in the first list's box tier (3, 3, 3, 4, 5 on
client 3482); in `siege2024rewardstaticstatus.bss` the same five sets
step through Determined Triumph Reward Tier 1 to 5. A set per result rank
or per number of held days fits, and the four lists per set may be for
different roles, but nothing names them. `unknown_rewards`, with a
Resolve Box, fits a defeat reward.

### The u16 and the Two Skills

`unknown_00` is `0` on the one row; in `siege2024rewardstaticstatus.bss`
the three rows hold `0`, `1` and `2`, which fits the siege group index:
`panel_window_villagesiegemenu_all.luac` (client 3482) has three land
groups in `_eTerritoryGroupType` and one ocean group in
`_eTerritoryOceanGroupType`. Which of the two skills goes to whom is
open.
