# `bootyitemlist.bss` Format

## Purpose

The booty items per territory: one row per territory key with a list of
item keys. On client 3483 the 14 rows (territories `0` to `13`) each hold
a temporary conquest crown, a temporary armor and `45113` [Guild]
Reminiscence of Battle. Balenos to Valencia (`0` to `4`) have their own
crown and armor (Silver Maned Horse Crown (Temp) and Silver Mane's Armor
(Temp) for Balenos); territories `5` to `13` repeat the Valencia pair,
Crown of Aal (Temp) and Armor of Aal (Temp). The permanent crowns and
armor of the same territories are the `booty_item_ids` of
[`territoryinfo.bss`](territoryinfo_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1506 and later | 3483    | `bootyitemlist.bss` | 356   | 14 Row  | 24        |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 1      | `bootyitemlist.bss` | 356 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e4b1e82315ae`  |
| 3482   | Layout 1 | `e4b1e82315ae`  |
| 3474   | Layout 1 | `e4b1e82315ae`  |
| 3473   | Layout 1 | `e4b1e82315ae`  |
| 3464   | Layout 1 | `e4b1e82315ae`  |
| 3458   | Layout 1 | `e4b1e82315ae`  |
| 3454   | Layout 1 | `e4b1e82315ae`  |
| 3444   | Layout 1 | `e4b1e82315ae`  |
| 3435   | Layout 1 | `e4b1e82315ae`  |
| 3426   | Layout 1 | `e4b1e82315ae`  |
| 3418   | Layout 1 | `e4b1e82315ae`  |
| 3412   | Layout 1 | `e4b1e82315ae`  |
| 3402   | Layout 1 | `e4b1e82315ae`  |
| 3396   | Layout 1 | `e4b1e82315ae`  |
| 3387   | Layout 1 | `e4b1e82315ae`  |
| 3381   | Layout 1 | `e4b1e82315ae`  |
| 3373   | Layout 1 | `e4b1e82315ae`  |
| 3364   | Layout 1 | `e4b1e82315ae`  |
| 3356   | Layout 1 | `e4b1e82315ae`  |
| 3349   | Layout 1 | `e4b1e82315ae`  |
| 3342   | Layout 1 | `e4b1e82315ae`  |
| 3335   | Layout 1 | `e4b1e82315ae`  |
| 3326   | Layout 1 | `e4b1e82315ae`  |
| 3321   | Layout 1 | `e4b1e82315ae`  |
| 3314   | Layout 1 | `e4b1e82315ae`  |
| 3303   | Layout 1 | `e4b1e82315ae`  |
| 3302   | Layout 1 | `e4b1e82315ae`  |
| 3293   | Layout 1 | `e4b1e82315ae`  |
| 3283   | Layout 1 | `e4b1e82315ae`  |
| 3275   | Layout 1 | `e4b1e82315ae`  |
| 3267   | Layout 1 | `e4b1e82315ae`  |
| 3258   | Layout 1 | `e4b1e82315ae`  |
| 3251   | Layout 1 | `e4b1e82315ae`  |
| 3242   | Layout 1 | `e4b1e82315ae`  |
| 3235   | Layout 1 | `e4b1e82315ae`  |
| 3229   | Layout 1 | `e4b1e82315ae`  |
| 3212   | Layout 1 | `e4b1e82315ae`  |
| 3203   | Layout 1 | `e4b1e82315ae`  |
| 3193   | Layout 1 | `e4b1e82315ae`  |
| 3186   | Layout 1 | `e4b1e82315ae`  |
| 3177   | Layout 1 | `e4b1e82315ae`  |
| 3169   | Layout 1 | `e4b1e82315ae`  |
| 3158   | Layout 1 | `e4b1e82315ae`  |
| 3151   | Layout 1 | `e4b1e82315ae`  |
| 3144   | Layout 1 | `e4b1e82315ae`  |
| 3133   | Layout 1 | `e4b1e82315ae`  |
| 3125   | Layout 1 | `e4b1e82315ae`  |
| 3118   | Layout 1 | `e4b1e82315ae`  |
| 3111   | Layout 1 | `e4b1e82315ae`  |
| 3103   | Layout 1 | `e4b1e82315ae`  |
| 3095   | Layout 1 | `e4b1e82315ae`  |
| 3086   | Layout 1 | `e4b1e82315ae`  |
| 3072   | Layout 1 | `e4b1e82315ae`  |
| 3062   | Layout 1 | `e4b1e82315ae`  |
| 3052   | Layout 1 | `e4b1e82315ae`  |
| 3045   | Layout 1 | `e4b1e82315ae`  |
| 3037   | Layout 1 | `e4b1e82315ae`  |
| 3030   | Layout 1 | `e4b1e82315ae`  |
| 3021   | Layout 1 | `e4b1e82315ae`  |
| 3012   | Layout 1 | `e4b1e82315ae`  |
| 3002   | Layout 1 | `e4b1e82315ae`  |
| 2995   | Layout 1 | `e4b1e82315ae`  |
| 2987   | Layout 1 | `e4b1e82315ae`  |
| 2978   | Layout 1 | `e4b1e82315ae`  |
| 2970   | Layout 1 | `e4b1e82315ae`  |
| 2959   | Layout 1 | `e4b1e82315ae`  |
| 2951   | Layout 1 | `e4b1e82315ae`  |
| 2942   | Layout 1 | `e4b1e82315ae`  |
| 2935   | Layout 1 | `e4b1e82315ae`  |
| 2932   | Layout 1 | `e4b1e82315ae`  |
| 2923   | Layout 1 | `e4b1e82315ae`  |
| 2919   | Layout 1 | `e4b1e82315ae`  |
| 2907   | Layout 1 | `e4b1e82315ae`  |
| 2900   | Layout 1 | `e4b1e82315ae`  |
| 2891   | Layout 1 | `e4b1e82315ae`  |
| 2882   | Layout 1 | `e4b1e82315ae`  |
| 2872   | Layout 1 | `e4b1e82315ae`  |
| 2863   | Layout 1 | `e4b1e82315ae`  |
| 2855   | Layout 1 | `e4b1e82315ae`  |
| 2849   | Layout 1 | `e4b1e82315ae`  |
| 2844   | Layout 1 | `e4b1e82315ae`  |
| 2834   | Layout 1 | `e4b1e82315ae`  |
| 2825   | Layout 1 | `e4b1e82315ae`  |
| 2819   | Layout 1 | `e4b1e82315ae`  |
| 2811   | Layout 1 | `e4b1e82315ae`  |
| 2803   | Layout 1 | `e4b1e82315ae`  |
| 2794   | Layout 1 | `e4b1e82315ae`  |
| 2783   | Layout 1 | `e4b1e82315ae`  |
| 2774   | Layout 1 | `e4b1e82315ae`  |
| 2765   | Layout 1 | `e4b1e82315ae`  |
| 2756   | Layout 1 | `e4b1e82315ae`  |
| 2750   | Layout 1 | `e4b1e82315ae`  |
| 2743   | Layout 1 | `e4b1e82315ae`  |
| 2736   | Layout 1 | `e4b1e82315ae`  |
| 2726   | Layout 1 | `e4b1e82315ae`  |
| 2717   | Layout 1 | `e4b1e82315ae`  |
| 2709   | Layout 1 | `e4b1e82315ae`  |
| 2703   | Layout 1 | `e4b1e82315ae`  |
| 2695   | Layout 1 | `e4b1e82315ae`  |
| 2684   | Layout 1 | `e4b1e82315ae`  |
| 2672   | Layout 1 | `e4b1e82315ae`  |
| 2665   | Layout 1 | `e4b1e82315ae`  |
| 2657   | Layout 1 | `e4b1e82315ae`  |
| 2649   | Layout 1 | `e4b1e82315ae`  |
| 2644   | Layout 1 | `e4b1e82315ae`  |
| 2637   | Layout 1 | `e4b1e82315ae`  |
| 2629   | Layout 1 | `e4b1e82315ae`  |
| 2619   | Layout 1 | `e4b1e82315ae`  |
| 2612   | Layout 1 | `e4b1e82315ae`  |
| 2606   | Layout 1 | `e4b1e82315ae`  |
| 2602   | Layout 1 | `e4b1e82315ae`  |
| 2601   | Layout 1 | `e4b1e82315ae`  |
| 2592   | Layout 1 | `e4b1e82315ae`  |
| 2583   | Layout 1 | `e4b1e82315ae`  |
| 2575   | Layout 1 | `e4b1e82315ae`  |
| 2567   | Layout 1 | `e4b1e82315ae`  |
| 2560   | Layout 1 | `e4b1e82315ae`  |
| 2553   | Layout 1 | `e4b1e82315ae`  |
| 2545   | Layout 1 | `e4b1e82315ae`  |
| 2538   | Layout 1 | `e4b1e82315ae`  |
| 2529   | Layout 1 | `e4b1e82315ae`  |
| 2519   | Layout 1 | `e4b1e82315ae`  |
| 2513   | Layout 1 | `e4b1e82315ae`  |
| 2510   | Layout 1 | `e4b1e82315ae`  |
| 2507   | Layout 1 | `e4b1e82315ae`  |
| 2503   | Layout 1 | `e4b1e82315ae`  |
| 2498   | Layout 1 | `e4b1e82315ae`  |
| 2492   | Layout 1 | `e4b1e82315ae`  |
| 2487   | Layout 1 | `e4b1e82315ae`  |
| 2480   | Layout 1 | `e4b1e82315ae`  |
| 2474   | Layout 1 | `e4b1e82315ae`  |
| 2468   | Layout 1 | `e4b1e82315ae`  |
| 2460   | Layout 1 | `e4b1e82315ae`  |
| 2453   | Layout 1 | `e4b1e82315ae`  |
| 2444   | Layout 1 | `e4b1e82315ae`  |
| 2438   | Layout 1 | `e4b1e82315ae`  |
| 2434   | Layout 1 | `e4b1e82315ae`  |
| 2429   | Layout 1 | `e4b1e82315ae`  |
| 2421   | Layout 1 | `e4b1e82315ae`  |
| 2414   | Layout 1 | `e4b1e82315ae`  |
| 2407   | Layout 1 | `e4b1e82315ae`  |
| 2401   | Layout 1 | `e4b1e82315ae`  |
| 2397   | Layout 1 | `e4b1e82315ae`  |
| 2393   | Layout 1 | `e4b1e82315ae`  |
| 2384   | Layout 1 | `e4b1e82315ae`  |
| 2378   | Layout 1 | `e4b1e82315ae`  |
| 2372   | Layout 1 | `e4b1e82315ae`  |
| 2358   | Layout 1 | `e4b1e82315ae`  |
| 2352   | Layout 1 | `e4b1e82315ae`  |
| 2347   | Layout 1 | `e4b1e82315ae`  |
| 2343   | Layout 1 | `e4b1e82315ae`  |
| 2335   | Layout 1 | `e4b1e82315ae`  |
| 2327   | Layout 1 | `e4b1e82315ae`  |
| 2324   | Layout 1 | `e4b1e82315ae`  |
| 2319   | Layout 1 | `e4b1e82315ae`  |
| 2313   | Layout 1 | `e4b1e82315ae`  |
| 2308   | Layout 1 | `e4b1e82315ae`  |
| 2302   | Layout 1 | `e4b1e82315ae`  |
| 2295   | Layout 1 | `e4b1e82315ae`  |
| 2290   | Layout 1 | `e4b1e82315ae`  |
| 2284   | Layout 1 | `e4b1e82315ae`  |
| 2276   | Layout 1 | `e4b1e82315ae`  |
| 2269   | Layout 1 | `e4b1e82315ae`  |
| 2259   | Layout 1 | `e4b1e82315ae`  |
| 2250   | Layout 1 | `e4b1e82315ae`  |
| 2243   | Layout 1 | `e4b1e82315ae`  |
| 2235   | Layout 1 | `e4b1e82315ae`  |
| 2229   | Layout 1 | `e4b1e82315ae`  |
| 2224   | Layout 1 | `e4b1e82315ae`  |
| 2218   | Layout 1 | `e4b1e82315ae`  |
| 2215   | Layout 1 | `e4b1e82315ae`  |
| 2207   | Layout 1 | `e4b1e82315ae`  |
| 2203   | Layout 1 | `e4b1e82315ae`  |
| 2196   | Layout 1 | `e4b1e82315ae`  |
| 2192   | Layout 1 | `e4b1e82315ae`  |
| 2189   | Layout 1 | `e4b1e82315ae`  |
| 2183   | Layout 1 | `e4b1e82315ae`  |
| 2179   | Layout 1 | `e4b1e82315ae`  |
| 2171   | Layout 1 | `e4b1e82315ae`  |
| 2163   | Layout 1 | `e4b1e82315ae`  |
| 2156   | Layout 1 | `e4b1e82315ae`  |
| 2151   | Layout 1 | `e4b1e82315ae`  |
| 2147   | Layout 1 | `e4b1e82315ae`  |
| 2142   | Layout 1 | `e4b1e82315ae`  |
| 2138   | Layout 1 | `e4b1e82315ae`  |
| 2134   | Layout 1 | `e4b1e82315ae`  |
| 2130   | Layout 1 | `e4b1e82315ae`  |
| 2122   | Layout 1 | `e4b1e82315ae`  |
| 2107   | Layout 1 | `e4b1e82315ae`  |
| 2098   | Layout 1 | `e4b1e82315ae`  |
| 2089   | Layout 1 | `e4b1e82315ae`  |
| 2081   | Layout 1 | `e4b1e82315ae`  |
| 2073   | Layout 1 | `e4b1e82315ae`  |
| 2067   | Layout 1 | `e4b1e82315ae`  |
| 2063   | Layout 1 | `e4b1e82315ae`  |
| 2059   | Layout 1 | `e4b1e82315ae`  |
| 2052   | Layout 1 | `e4b1e82315ae`  |
| 2044   | Layout 1 | `e4b1e82315ae`  |
| 2039   | Layout 1 | `e4b1e82315ae`  |
| 2032   | Layout 1 | `e4b1e82315ae`  |
| 2025   | Layout 1 | `e4b1e82315ae`  |
| 2011   | Layout 1 | `e4b1e82315ae`  |
| 2005   | Layout 1 | `e4b1e82315ae`  |
| 2000   | Layout 1 | `e4b1e82315ae`  |
| 1996   | Layout 1 | `e4b1e82315ae`  |
| 1991   | Layout 1 | `e4b1e82315ae`  |
| 1985   | Layout 1 | `e4b1e82315ae`  |
| 1980   | Layout 1 | `e4b1e82315ae`  |
| 1969   | Layout 1 | `e4b1e82315ae`  |
| 1964   | Layout 1 | `e4b1e82315ae`  |
| 1958   | Layout 1 | `e4b1e82315ae`  |
| 1950   | Layout 1 | `e4b1e82315ae`  |
| 1945   | Layout 1 | `e4b1e82315ae`  |
| 1937   | Layout 1 | `e4b1e82315ae`  |
| 1933   | Layout 1 | `e4b1e82315ae`  |
| 1927   | Layout 1 | `e4b1e82315ae`  |
| 1921   | Layout 1 | `e4b1e82315ae`  |
| 1914   | Layout 1 | `e4b1e82315ae`  |
| 1908   | Layout 1 | `e4b1e82315ae`  |
| 1897   | Layout 1 | `e4b1e82315ae`  |
| 1892   | Layout 1 | `e4b1e82315ae`  |
| 1886   | Layout 1 | `e4b1e82315ae`  |
| 1881   | Layout 1 | `e4b1e82315ae`  |
| 1871   | Layout 1 | `e4b1e82315ae`  |
| 1866   | Layout 1 | `e4b1e82315ae`  |
| 1862   | Layout 1 | `e4b1e82315ae`  |
| 1854   | Layout 1 | `e4b1e82315ae`  |
| 1846   | Layout 1 | `e4b1e82315ae`  |
| 1838   | Layout 1 | `e4b1e82315ae`  |
| 1832   | Layout 1 | `e4b1e82315ae`  |
| 1826   | Layout 1 | `e4b1e82315ae`  |
| 1822   | Layout 1 | `e4b1e82315ae`  |
| 1818   | Layout 1 | `e4b1e82315ae`  |
| 1804   | Layout 1 | `e4b1e82315ae`  |
| 1794   | Layout 1 | `e4b1e82315ae`  |
| 1790   | Layout 1 | `e4b1e82315ae`  |
| 1784   | Layout 1 | `e4b1e82315ae`  |
| 1774   | Layout 1 | `e4b1e82315ae`  |
| 1771   | Layout 1 | `e4b1e82315ae`  |
| 1762   | Layout 1 | `e4b1e82315ae`  |
| 1759   | Layout 1 | `e4b1e82315ae`  |
| 1754   | Layout 1 | `e4b1e82315ae`  |
| 1749   | Layout 1 | `e4b1e82315ae`  |
| 1743   | Layout 1 | `e4b1e82315ae`  |
| 1737   | Layout 1 | `e4b1e82315ae`  |
| 1731   | Layout 1 | `e4b1e82315ae`  |
| 1725   | Layout 1 | `e4b1e82315ae`  |
| 1717   | Layout 1 | `e4b1e82315ae`  |
| 1710   | Layout 1 | `e4b1e82315ae`  |
| 1704   | Layout 1 | `e4b1e82315ae`  |
| 1698   | Layout 1 | `e4b1e82315ae`  |
| 1690   | Layout 1 | `e4b1e82315ae`  |
| 1685   | Layout 1 | `e4b1e82315ae`  |
| 1680   | Layout 1 | `e4b1e82315ae`  |
| 1674   | Layout 1 | `e4b1e82315ae`  |
| 1668   | Layout 1 | `e4b1e82315ae`  |
| 1659   | Layout 1 | `e4b1e82315ae`  |
| 1649   | Layout 1 | `e4b1e82315ae`  |
| 1642   | Layout 1 | `e4b1e82315ae`  |
| 1636   | Layout 1 | `e4b1e82315ae`  |
| 1628   | Layout 1 | `e4b1e82315ae`  |
| 1622   | Layout 1 | `e4b1e82315ae`  |
| 1614   | Layout 1 | `e4b1e82315ae`  |
| 1608   | Layout 1 | `e4b1e82315ae`  |
| 1602   | Layout 1 | `e4b1e82315ae`  |
| 1598   | Layout 1 | `e4b1e82315ae`  |
| 1594   | Layout 1 | `e4b1e82315ae`  |
| 1590   | Layout 1 | `e4b1e82315ae`  |
| 1587   | Layout 1 | `e4b1e82315ae`  |
| 1584   | Layout 1 | `e4b1e82315ae`  |
| 1579   | Layout 1 | `e4b1e82315ae`  |
| 1572   | Layout 1 | `e4b1e82315ae`  |
| 1565   | Layout 1 | `e4b1e82315ae`  |
| 1559   | Layout 1 | `e4b1e82315ae`  |
| 1554   | Layout 1 | `e4b1e82315ae`  |
| 1547   | Layout 1 | `e4b1e82315ae`  |
| 1537   | Layout 1 | `e4b1e82315ae`  |
| 1529   | Layout 1 | `e4b1e82315ae`  |
| 1524   | Layout 1 | `e4b1e82315ae`  |
| 1519   | Layout 1 | `e4b1e82315ae`  |
| 1509   | Layout 1 | `e4b1e82315ae`  |
| 1506   | Layout 1 | `e4b1e82315ae`  |
| 1504   | No file  | `e4b1e82315ae`  |
| 1500   | No file  | `e4b1e82315ae`  |
| 1493   | No file  | `e4b1e82315ae`  |
| 1489   | No file  | `e4b1e82315ae`  |
| 1485   | No file  | `e4b1e82315ae`  |
| 1481   | No file  | `e4b1e82315ae`  |
| 1474   | No file  | `e4b1e82315ae`  |
| 1466   | No file  | `e4b1e82315ae`  |
| 1462   | No file  | `e4b1e82315ae`  |
| 1459   | No file  | `e4b1e82315ae`  |
| 1453   | No file  | `e4b1e82315ae`  |
| 1450   | No file  | `e4b1e82315ae`  |
| 1445   | No file  | `e4b1e82315ae`  |
| 1439   | No file  | `e4b1e82315ae`  |
| 1433   | No file  | `e4b1e82315ae`  |
| 1430   | No file  | `e4b1e82315ae`  |
| 1426   | No file  | `e4b1e82315ae`  |
| 1421   | No file  | `e4b1e82315ae`  |
| 1417   | No file  | `e4b1e82315ae`  |
| 1416   | No file  | `e4b1e82315ae`  |
| 1409   | No file  | `e4b1e82315ae`  |
| 1405   | No file  | `e4b1e82315ae`  |
| 1401   | No file  | `e4b1e82315ae`  |
| 1396   | No file  | `e4b1e82315ae`  |
| 1391   | No file  | `e4b1e82315ae`  |
| 1390   | No file  | `e4b1e82315ae`  |
| 1386   | No file  | `e4b1e82315ae`  |
| 1381   | No file  | `e4b1e82315ae`  |
| 1379   | No file  | `e4b1e82315ae`  |
| 1372   | No file  | `e4b1e82315ae`  |
| 1366   | No file  | `e4b1e82315ae`  |
| 1364   | No file  | `e4b1e82315ae`  |
| 1363   | No file  | `e4b1e82315ae`  |
| 1360   | No file  | `e4b1e82315ae`  |
| 1358   | No file  | `e4b1e82315ae`  |
| 1355   | No file  | `e4b1e82315ae`  |
| 1351   | No file  | `e4b1e82315ae`  |
| 1348   | No file  | `e4b1e82315ae`  |
| 1346   | No file  | `e4b1e82315ae`  |
| 1341   | No file  | `e4b1e82315ae`  |
| 1340   | No file  | `e4b1e82315ae`  |
| 1338   | No file  | `e4b1e82315ae`  |
| 1335   | No file  | `e4b1e82315ae`  |
| 1333   | No file  | `e4b1e82315ae`  |
| 1329   | No file  | `e4b1e82315ae`  |
| 1327   | No file  | `e4b1e82315ae`  |
| 1324   | No file  | `e4b1e82315ae`  |
| 1321   | No file  | `e4b1e82315ae`  |
| 1319   | No file  | `e4b1e82315ae`  |
| 1318   | No file  | `e4b1e82315ae`  |
| 1316   | No file  | `e4b1e82315ae`  |
| 1313   | No file  | `e4b1e82315ae`  |
| 1311   | No file  | `e4b1e82315ae`  |
| 1309   | No file  | `e4b1e82315ae`  |
| 1304   | No file  | `e4b1e82315ae`  |
| 1292   | No file  | `e4b1e82315ae`  |
| 1286   | No file  | `e4b1e82315ae`  |
| 1280   | No file  | `e4b1e82315ae`  |
| 1276   | No file  | `e4b1e82315ae`  |
| 1267   | No file  | `e4b1e82315ae`  |
| 1261   | No file  | `e4b1e82315ae`  |
| 1256   | No file  | `e4b1e82315ae`  |
| 1250   | No file  | `e4b1e82315ae`  |
| 1246   | No file  | `e4b1e82315ae`  |
| 1239   | No file  | `e4b1e82315ae`  |
| 1230   | No file  | `e4b1e82315ae`  |
| 1226   | No file  | `e4b1e82315ae`  |
| 1220   | No file  | `e4b1e82315ae`  |
| 1217   | No file  | `e4b1e82315ae`  |
| 1211   | No file  | `e4b1e82315ae`  |
| 1210   | No file  | `e4b1e82315ae`  |
| 1208   | No file  | `e4b1e82315ae`  |
| 1203   | No file  | `e4b1e82315ae`  |
| 1197   | No file  | `e4b1e82315ae`  |
| 1194   | No file  | `e4b1e82315ae`  |
| 1192   | No file  | `e4b1e82315ae`  |
| 1187   | No file  | `e4b1e82315ae`  |
| 1183   | No file  | `e4b1e82315ae`  |
| 1177   | No file  | `e4b1e82315ae`  |
| 1173   | No file  | `e4b1e82315ae`  |
| 1167   | No file  | `e4b1e82315ae`  |
| 1164   | No file  | `e4b1e82315ae`  |
| 1156   | No file  | `e4b1e82315ae`  |
| 1149   | No file  | `e4b1e82315ae`  |
| 1144   | No file  | `e4b1e82315ae`  |
| 1137   | No file  | `e4b1e82315ae`  |
| 1132   | No file  | `e4b1e82315ae`  |
| 1127   | No file  | `e4b1e82315ae`  |
| 1122   | No file  | `e4b1e82315ae`  |
| 1118   | No file  | `e4b1e82315ae`  |
| 1114   | No file  | `e4b1e82315ae`  |
| 1109   | No file  | `e4b1e82315ae`  |
| 1102   | No file  | `e4b1e82315ae`  |
| 1096   | No file  | `e4b1e82315ae`  |
| 1088   | No file  | `e4b1e82315ae`  |
| 1081   | No file  | `e4b1e82315ae`  |
| 1076   | No file  | `e4b1e82315ae`  |
| 1069   | No file  | `e4b1e82315ae`  |
| 1064   | No file  | `e4b1e82315ae`  |
| 1058   | No file  | `e4b1e82315ae`  |
| 1051   | No file  | `e4b1e82315ae`  |
| 1044   | No file  | `e4b1e82315ae`  |
| 1036   | No file  | `e4b1e82315ae`  |
| 1026   | No file  | `e4b1e82315ae`  |
| 1016   | No file  | `e4b1e82315ae`  |
| 1009   | No file  | `e4b1e82315ae`  |
| 1005   | No file  | `e4b1e82315ae`  |
| 1000   | No file  | `e4b1e82315ae`  |
| 998    | No file  | `e4b1e82315ae`  |
| 990    | No file  | `e4b1e82315ae`  |
| 979    | No file  | `e4b1e82315ae`  |
| 972    | No file  | `e4b1e82315ae`  |
| 963    | No file  | `e4b1e82315ae`  |
| 955    | No file  | `e4b1e82315ae`  |
| 946    | No file  | `e4b1e82315ae`  |
| 938    | No file  | `e4b1e82315ae`  |
| 927    | No file  | `e4b1e82315ae`  |
| 911    | No file  | `e4b1e82315ae`  |
| 904    | No file  | `e4b1e82315ae`  |
| 899    | No file  | `e4b1e82315ae`  |
| 894    | No file  | `e4b1e82315ae`  |
| 885    | No file  | `e4b1e82315ae`  |
| 879    | No file  | `e4b1e82315ae`  |
| 872    | No file  | `e4b1e82315ae`  |
| 864    | No file  | `e4b1e82315ae`  |
| 855    | No file  | `e4b1e82315ae`  |
| 853    | No file  | `e4b1e82315ae`  |
| 845    | No file  | `e4b1e82315ae`  |
| 837    | No file  | `e4b1e82315ae`  |
| 829    | No file  | `e4b1e82315ae`  |
| 822    | No file  | `e4b1e82315ae`  |
| 814    | No file  | `e4b1e82315ae`  |
| 805    | No file  | `e4b1e82315ae`  |
| 794    | No file  | `e4b1e82315ae`  |
| 787    | No file  | `e4b1e82315ae`  |
| 780    | No file  | `e4b1e82315ae`  |
| 771    | No file  | `e4b1e82315ae`  |
| 760    | No file  | `e4b1e82315ae`  |
| 748    | No file  | `e4b1e82315ae`  |
| 741    | No file  | `e4b1e82315ae`  |
| 736    | No file  | `e4b1e82315ae`  |
| 731    | No file  | `e4b1e82315ae`  |
| 723    | No file  | `e4b1e82315ae`  |
| 711    | No file  | `e4b1e82315ae`  |
| 707    | No file  | `e4b1e82315ae`  |
| 697    | No file  | `e4b1e82315ae`  |
| 689    | No file  | `e4b1e82315ae`  |
| 683    | No file  | `e4b1e82315ae`  |
| 678    | No file  | `e4b1e82315ae`  |
| 670    | No file  | `e4b1e82315ae`  |
| 661    | No file  | `e4b1e82315ae`  |
| 656    | No file  | `e4b1e82315ae`  |
| 652    | No file  | `e4b1e82315ae`  |
| 643    | No file  | `e4b1e82315ae`  |
| 637    | No file  | `e4b1e82315ae`  |
| 630    | No file  | `e4b1e82315ae`  |
| 627    | No file  | `e4b1e82315ae`  |
| 621    | No file  | `e4b1e82315ae`  |
| 617    | No file  | `e4b1e82315ae`  |
| 615    | No file  | `e4b1e82315ae`  |
| 606    | No file  | `e4b1e82315ae`  |
| 599    | No file  | `e4b1e82315ae`  |
| 592    | No file  | `e4b1e82315ae`  |
| 586    | No file  | `e4b1e82315ae`  |
| 577    | No file  | `e4b1e82315ae`  |
| 569    | No file  | `e4b1e82315ae`  |
| 561    | No file  | `e4b1e82315ae`  |
| 554    | No file  | `e4b1e82315ae`  |
| 542    | No file  | `e4b1e82315ae`  |
| 532    | No file  | `e4b1e82315ae`  |
| 531    | No file  | `e4b1e82315ae`  |
| 526    | No file  | `e4b1e82315ae`  |
| 521    | No file  | `e4b1e82315ae`  |
| 517    | No file  | `e4b1e82315ae`  |
| 510    | No file  | `e4b1e82315ae`  |
| 508    | No file  | `e4b1e82315ae`  |
| 504    | No file  | `e4b1e82315ae`  |
| 497    | No file  | `e4b1e82315ae`  |
| 491    | No file  | `e4b1e82315ae`  |
| 485    | No file  | `e4b1e82315ae`  |
| 478    | No file  | `e4b1e82315ae`  |
| 472    | No file  | `e4b1e82315ae`  |
| 466    | No file  | `e4b1e82315ae`  |
| 457    | No file  | `e4b1e82315ae`  |
| 452    | No file  | `e4b1e82315ae`  |
| 449    | No file  | `e4b1e82315ae`  |
| 435    | No file  | `e4b1e82315ae`  |

<!-- versions:end -->

## Companion Files

None. The handler names each territory with LOC type 12 and each item with
LOC type 0 from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of territories                         |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 12 bytes + items)

| Offset  | Type                  | Field            | Notes                                                              |
| ------- | --------------------- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u32                   | territory_key    | The `territoryinfo.bss` territory (LOC type 12 name); rows in key order |
| `+0x04` | u64                   | booty_item_count | Entries in `booty_item_ids`; `3` on every row (client 3483)        |
| `+0x0C` | u32[booty_item_count] | booty_item_ids   | Item keys (LOC type 0 names)                                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

The lists follow the `BootyItem_0` to `BootyItem_8` columns of the
`MedalTable` and `SiegeReward` sheets of a private server's
`DataSheets.bexcel` on client 1784 (`datasheet_siegedatatable.xlsm` for
`MedalTable`), one row per `PA_GAME_SERVICE_TYPE`. The 9 rows of the client
1784 file are those 9 columns in order: each list matches its column
value for value (`731901,731906,45113` for `BootyItem_0`) in 10 of the 17
`MedalTable` rows (`DEV`, `KOR_REAL`, `NA_REAL` and 7 more) and 2 of the
17 `SiegeReward` rows. The other rows list the permanent pairs
(`23381,23386` for `BootyItem_0`).

The column number is the territory key: the `Territory_Table` sheet of the
same file gives `TerritoryKey` `0` to `9` a `BootyItem` list with the
permanent crown and armor of that territory in the same order, and
client 3483 has 14 rows for the 14 territories of `territoryinfo.bss`.
`territory_key`, `booty_item_count` and `booty_item_ids` are the names
`territoryinfo.bss` uses for the same key and list.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`: the
  territory key, its name and the item list with each item's name.
