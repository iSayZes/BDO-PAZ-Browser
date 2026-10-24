# `bloodaltar.bss` Format

## Purpose

The stages of the Blood Altar, a party instance
(`__eInstanceContentsType_BloodAltar`). A PABR file: four option values,
then one row per stage with its Korean stage texts and boss banner
texture (string-table indices), the minimum and recommended AP and DP,
and two reward lists,
the first clear rewards and the weekly rewards. On client 3482 it holds
24 stages, `제1의 환상` ("the 1st Illusion") to `제 24의 환상`; the
first clear reward of stage N is Bloodstained Welcome - The Nth Illusion
(`980010 + N`) and the weekly rewards are Bloodstained Spoils - The Nth
Illusion (`980040 + N`) and Combat Secret Book (M) (`890118`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------------------------- | --------- |
| 2      | 3473 and later | 3483    | `bloodaltar.bss` | 3,363 | 72 Reward Entry, 24 Stage | 16        |
| 1      | 3283 to 3464   | 3464    | `bloodaltar.bss` | 2,211 | 24 Stage                  | 40        |

| Layout | File             | Known           | Unknown      |
| ------ | ---------------- | --------------- | ------------ |
| 2      | `bloodaltar.bss` | 3,157 B (93.9%) | 206 B (6.1%) |
| 1      | `bloodaltar.bss` | 2,005 B (90.7%) | 206 B (9.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `5fdd34d4d217`  |
| 3482   | Layout 2 | `5fdd34d4d217`  |
| 3474   | Layout 2 | `5fdd34d4d217`  |
| 3473   | Layout 2 | `5fdd34d4d217`  |
| 3464   | Layout 1 | `5fdd34d4d217`  |
| 3458   | Layout 1 | `5fdd34d4d217`  |
| 3454   | Layout 1 | `5fdd34d4d217`  |
| 3444   | Layout 1 | `5fdd34d4d217`  |
| 3435   | Layout 1 | `5fdd34d4d217`  |
| 3426   | Layout 1 | `5fdd34d4d217`  |
| 3418   | Layout 1 | `5fdd34d4d217`  |
| 3412   | Layout 1 | `5fdd34d4d217`  |
| 3402   | Layout 1 | `5fdd34d4d217`  |
| 3396   | Layout 1 | `5fdd34d4d217`  |
| 3387   | Layout 1 | `5fdd34d4d217`  |
| 3381   | Layout 1 | `5fdd34d4d217`  |
| 3373   | Layout 1 | `5fdd34d4d217`  |
| 3364   | Layout 1 | `5fdd34d4d217`  |
| 3356   | Layout 1 | `5fdd34d4d217`  |
| 3349   | Layout 1 | `5fdd34d4d217`  |
| 3342   | Layout 1 | `5fdd34d4d217`  |
| 3335   | Layout 1 | `5fdd34d4d217`  |
| 3326   | Layout 1 | `5fdd34d4d217`  |
| 3321   | Layout 1 | `5fdd34d4d217`  |
| 3314   | Layout 1 | `5fdd34d4d217`  |
| 3303   | Layout 1 | `5fdd34d4d217`  |
| 3302   | Layout 1 | `5fdd34d4d217`  |
| 3293   | Layout 1 | `5fdd34d4d217`  |
| 3283   | Layout 1 | `5fdd34d4d217`  |
| 3275   | No file  | `5fdd34d4d217`  |
| 3267   | No file  | `5fdd34d4d217`  |
| 3258   | No file  | `5fdd34d4d217`  |
| 3251   | No file  | `5fdd34d4d217`  |
| 3242   | No file  | `5fdd34d4d217`  |
| 3235   | No file  | `5fdd34d4d217`  |
| 3229   | No file  | `5fdd34d4d217`  |
| 3212   | No file  | `5fdd34d4d217`  |
| 3203   | No file  | `5fdd34d4d217`  |
| 3193   | No file  | `5fdd34d4d217`  |
| 3186   | No file  | `5fdd34d4d217`  |
| 3177   | No file  | `5fdd34d4d217`  |
| 3169   | No file  | `5fdd34d4d217`  |
| 3158   | No file  | `5fdd34d4d217`  |
| 3151   | No file  | `5fdd34d4d217`  |
| 3144   | No file  | `5fdd34d4d217`  |
| 3133   | No file  | `5fdd34d4d217`  |
| 3125   | No file  | `5fdd34d4d217`  |
| 3118   | No file  | `5fdd34d4d217`  |
| 3111   | No file  | `5fdd34d4d217`  |
| 3103   | No file  | `5fdd34d4d217`  |
| 3095   | No file  | `5fdd34d4d217`  |
| 3086   | No file  | `5fdd34d4d217`  |
| 3072   | No file  | `5fdd34d4d217`  |
| 3062   | No file  | `5fdd34d4d217`  |
| 3052   | No file  | `5fdd34d4d217`  |
| 3045   | No file  | `5fdd34d4d217`  |
| 3037   | No file  | `5fdd34d4d217`  |
| 3030   | No file  | `5fdd34d4d217`  |
| 3021   | No file  | `5fdd34d4d217`  |
| 3012   | No file  | `5fdd34d4d217`  |
| 3002   | No file  | `5fdd34d4d217`  |
| 2995   | No file  | `5fdd34d4d217`  |
| 2987   | No file  | `5fdd34d4d217`  |
| 2978   | No file  | `5fdd34d4d217`  |
| 2970   | No file  | `5fdd34d4d217`  |
| 2959   | No file  | `5fdd34d4d217`  |
| 2951   | No file  | `5fdd34d4d217`  |
| 2942   | No file  | `5fdd34d4d217`  |
| 2935   | No file  | `5fdd34d4d217`  |
| 2932   | No file  | `5fdd34d4d217`  |
| 2923   | No file  | `5fdd34d4d217`  |
| 2919   | No file  | `5fdd34d4d217`  |
| 2907   | No file  | `5fdd34d4d217`  |
| 2900   | No file  | `5fdd34d4d217`  |
| 2891   | No file  | `5fdd34d4d217`  |
| 2882   | No file  | `5fdd34d4d217`  |
| 2872   | No file  | `5fdd34d4d217`  |
| 2863   | No file  | `5fdd34d4d217`  |
| 2855   | No file  | `5fdd34d4d217`  |
| 2849   | No file  | `5fdd34d4d217`  |
| 2844   | No file  | `5fdd34d4d217`  |
| 2834   | No file  | `5fdd34d4d217`  |
| 2825   | No file  | `5fdd34d4d217`  |
| 2819   | No file  | `5fdd34d4d217`  |
| 2811   | No file  | `5fdd34d4d217`  |
| 2803   | No file  | `5fdd34d4d217`  |
| 2794   | No file  | `5fdd34d4d217`  |
| 2783   | No file  | `5fdd34d4d217`  |
| 2774   | No file  | `5fdd34d4d217`  |
| 2765   | No file  | `5fdd34d4d217`  |
| 2756   | No file  | `5fdd34d4d217`  |
| 2750   | No file  | `5fdd34d4d217`  |
| 2743   | No file  | `5fdd34d4d217`  |
| 2736   | No file  | `5fdd34d4d217`  |
| 2726   | No file  | `5fdd34d4d217`  |
| 2717   | No file  | `5fdd34d4d217`  |
| 2709   | No file  | `5fdd34d4d217`  |
| 2703   | No file  | `5fdd34d4d217`  |
| 2695   | No file  | `5fdd34d4d217`  |
| 2684   | No file  | `5fdd34d4d217`  |
| 2672   | No file  | `5fdd34d4d217`  |
| 2665   | No file  | `5fdd34d4d217`  |
| 2657   | No file  | `5fdd34d4d217`  |
| 2649   | No file  | `5fdd34d4d217`  |
| 2644   | No file  | `5fdd34d4d217`  |
| 2637   | No file  | `5fdd34d4d217`  |
| 2629   | No file  | `5fdd34d4d217`  |
| 2619   | No file  | `5fdd34d4d217`  |
| 2612   | No file  | `5fdd34d4d217`  |
| 2606   | No file  | `5fdd34d4d217`  |
| 2602   | No file  | `5fdd34d4d217`  |
| 2601   | No file  | `5fdd34d4d217`  |
| 2592   | No file  | `5fdd34d4d217`  |
| 2583   | No file  | `5fdd34d4d217`  |
| 2575   | No file  | `5fdd34d4d217`  |
| 2567   | No file  | `5fdd34d4d217`  |
| 2560   | No file  | `5fdd34d4d217`  |
| 2553   | No file  | `5fdd34d4d217`  |
| 2545   | No file  | `5fdd34d4d217`  |
| 2538   | No file  | `5fdd34d4d217`  |
| 2529   | No file  | `5fdd34d4d217`  |
| 2519   | No file  | `5fdd34d4d217`  |
| 2513   | No file  | `5fdd34d4d217`  |
| 2510   | No file  | `5fdd34d4d217`  |
| 2507   | No file  | `5fdd34d4d217`  |
| 2503   | No file  | `5fdd34d4d217`  |
| 2498   | No file  | `5fdd34d4d217`  |
| 2492   | No file  | `5fdd34d4d217`  |
| 2487   | No file  | `5fdd34d4d217`  |
| 2480   | No file  | `5fdd34d4d217`  |
| 2474   | No file  | `5fdd34d4d217`  |
| 2468   | No file  | `5fdd34d4d217`  |
| 2460   | No file  | `5fdd34d4d217`  |
| 2453   | No file  | `5fdd34d4d217`  |
| 2444   | No file  | `5fdd34d4d217`  |
| 2438   | No file  | `5fdd34d4d217`  |
| 2434   | No file  | `5fdd34d4d217`  |
| 2429   | No file  | `5fdd34d4d217`  |
| 2421   | No file  | `5fdd34d4d217`  |
| 2414   | No file  | `5fdd34d4d217`  |
| 2407   | No file  | `5fdd34d4d217`  |
| 2401   | No file  | `5fdd34d4d217`  |
| 2397   | No file  | `5fdd34d4d217`  |
| 2393   | No file  | `5fdd34d4d217`  |
| 2384   | No file  | `5fdd34d4d217`  |
| 2378   | No file  | `5fdd34d4d217`  |
| 2372   | No file  | `5fdd34d4d217`  |
| 2358   | No file  | `5fdd34d4d217`  |
| 2352   | No file  | `5fdd34d4d217`  |
| 2347   | No file  | `5fdd34d4d217`  |
| 2343   | No file  | `5fdd34d4d217`  |
| 2335   | No file  | `5fdd34d4d217`  |
| 2327   | No file  | `5fdd34d4d217`  |
| 2324   | No file  | `5fdd34d4d217`  |
| 2319   | No file  | `5fdd34d4d217`  |
| 2313   | No file  | `5fdd34d4d217`  |
| 2308   | No file  | `5fdd34d4d217`  |
| 2302   | No file  | `5fdd34d4d217`  |
| 2295   | No file  | `5fdd34d4d217`  |
| 2290   | No file  | `5fdd34d4d217`  |
| 2284   | No file  | `5fdd34d4d217`  |
| 2276   | No file  | `5fdd34d4d217`  |
| 2269   | No file  | `5fdd34d4d217`  |
| 2259   | No file  | `5fdd34d4d217`  |
| 2250   | No file  | `5fdd34d4d217`  |
| 2243   | No file  | `5fdd34d4d217`  |
| 2235   | No file  | `5fdd34d4d217`  |
| 2229   | No file  | `5fdd34d4d217`  |
| 2224   | No file  | `5fdd34d4d217`  |
| 2218   | No file  | `5fdd34d4d217`  |
| 2215   | No file  | `5fdd34d4d217`  |
| 2207   | No file  | `5fdd34d4d217`  |
| 2203   | No file  | `5fdd34d4d217`  |
| 2196   | No file  | `5fdd34d4d217`  |
| 2192   | No file  | `5fdd34d4d217`  |
| 2189   | No file  | `5fdd34d4d217`  |
| 2183   | No file  | `5fdd34d4d217`  |
| 2179   | No file  | `5fdd34d4d217`  |
| 2171   | No file  | `5fdd34d4d217`  |
| 2163   | No file  | `5fdd34d4d217`  |
| 2156   | No file  | `5fdd34d4d217`  |
| 2151   | No file  | `5fdd34d4d217`  |
| 2147   | No file  | `5fdd34d4d217`  |
| 2142   | No file  | `5fdd34d4d217`  |
| 2138   | No file  | `5fdd34d4d217`  |
| 2134   | No file  | `5fdd34d4d217`  |
| 2130   | No file  | `5fdd34d4d217`  |
| 2122   | No file  | `5fdd34d4d217`  |
| 2107   | No file  | `5fdd34d4d217`  |
| 2098   | No file  | `5fdd34d4d217`  |
| 2089   | No file  | `5fdd34d4d217`  |
| 2081   | No file  | `5fdd34d4d217`  |
| 2073   | No file  | `5fdd34d4d217`  |
| 2067   | No file  | `5fdd34d4d217`  |
| 2063   | No file  | `5fdd34d4d217`  |
| 2059   | No file  | `5fdd34d4d217`  |
| 2052   | No file  | `5fdd34d4d217`  |
| 2044   | No file  | `5fdd34d4d217`  |
| 2039   | No file  | `5fdd34d4d217`  |
| 2032   | No file  | `5fdd34d4d217`  |
| 2025   | No file  | `5fdd34d4d217`  |
| 2011   | No file  | `5fdd34d4d217`  |
| 2005   | No file  | `5fdd34d4d217`  |
| 2000   | No file  | `5fdd34d4d217`  |
| 1996   | No file  | `5fdd34d4d217`  |
| 1991   | No file  | `5fdd34d4d217`  |
| 1985   | No file  | `5fdd34d4d217`  |
| 1980   | No file  | `5fdd34d4d217`  |
| 1969   | No file  | `5fdd34d4d217`  |
| 1964   | No file  | `5fdd34d4d217`  |
| 1958   | No file  | `5fdd34d4d217`  |
| 1950   | No file  | `5fdd34d4d217`  |
| 1945   | No file  | `5fdd34d4d217`  |
| 1937   | No file  | `5fdd34d4d217`  |
| 1933   | No file  | `5fdd34d4d217`  |
| 1927   | No file  | `5fdd34d4d217`  |
| 1921   | No file  | `5fdd34d4d217`  |
| 1914   | No file  | `5fdd34d4d217`  |
| 1908   | No file  | `5fdd34d4d217`  |
| 1897   | No file  | `5fdd34d4d217`  |
| 1892   | No file  | `5fdd34d4d217`  |
| 1886   | No file  | `5fdd34d4d217`  |
| 1881   | No file  | `5fdd34d4d217`  |
| 1871   | No file  | `5fdd34d4d217`  |
| 1866   | No file  | `5fdd34d4d217`  |
| 1862   | No file  | `5fdd34d4d217`  |
| 1854   | No file  | `5fdd34d4d217`  |
| 1846   | No file  | `5fdd34d4d217`  |
| 1838   | No file  | `5fdd34d4d217`  |
| 1832   | No file  | `5fdd34d4d217`  |
| 1826   | No file  | `5fdd34d4d217`  |
| 1822   | No file  | `5fdd34d4d217`  |
| 1818   | No file  | `5fdd34d4d217`  |
| 1804   | No file  | `5fdd34d4d217`  |
| 1794   | No file  | `5fdd34d4d217`  |
| 1790   | No file  | `5fdd34d4d217`  |
| 1784   | No file  | `5fdd34d4d217`  |
| 1774   | No file  | `5fdd34d4d217`  |
| 1771   | No file  | `5fdd34d4d217`  |
| 1762   | No file  | `5fdd34d4d217`  |
| 1759   | No file  | `5fdd34d4d217`  |
| 1754   | No file  | `5fdd34d4d217`  |
| 1749   | No file  | `5fdd34d4d217`  |
| 1743   | No file  | `5fdd34d4d217`  |
| 1737   | No file  | `5fdd34d4d217`  |
| 1731   | No file  | `5fdd34d4d217`  |
| 1725   | No file  | `5fdd34d4d217`  |
| 1717   | No file  | `5fdd34d4d217`  |
| 1710   | No file  | `5fdd34d4d217`  |
| 1704   | No file  | `5fdd34d4d217`  |
| 1698   | No file  | `5fdd34d4d217`  |
| 1690   | No file  | `5fdd34d4d217`  |
| 1685   | No file  | `5fdd34d4d217`  |
| 1680   | No file  | `5fdd34d4d217`  |
| 1674   | No file  | `5fdd34d4d217`  |
| 1668   | No file  | `5fdd34d4d217`  |
| 1659   | No file  | `5fdd34d4d217`  |
| 1649   | No file  | `5fdd34d4d217`  |
| 1642   | No file  | `5fdd34d4d217`  |
| 1636   | No file  | `5fdd34d4d217`  |
| 1628   | No file  | `5fdd34d4d217`  |
| 1622   | No file  | `5fdd34d4d217`  |
| 1614   | No file  | `5fdd34d4d217`  |
| 1608   | No file  | `5fdd34d4d217`  |
| 1602   | No file  | `5fdd34d4d217`  |
| 1598   | No file  | `5fdd34d4d217`  |
| 1594   | No file  | `5fdd34d4d217`  |
| 1590   | No file  | `5fdd34d4d217`  |
| 1587   | No file  | `5fdd34d4d217`  |
| 1584   | No file  | `5fdd34d4d217`  |
| 1579   | No file  | `5fdd34d4d217`  |
| 1572   | No file  | `5fdd34d4d217`  |
| 1565   | No file  | `5fdd34d4d217`  |
| 1559   | No file  | `5fdd34d4d217`  |
| 1554   | No file  | `5fdd34d4d217`  |
| 1547   | No file  | `5fdd34d4d217`  |
| 1537   | No file  | `5fdd34d4d217`  |
| 1529   | No file  | `5fdd34d4d217`  |
| 1524   | No file  | `5fdd34d4d217`  |
| 1519   | No file  | `5fdd34d4d217`  |
| 1509   | No file  | `5fdd34d4d217`  |
| 1506   | No file  | `5fdd34d4d217`  |
| 1504   | No file  | `5fdd34d4d217`  |
| 1500   | No file  | `5fdd34d4d217`  |
| 1493   | No file  | `5fdd34d4d217`  |
| 1489   | No file  | `5fdd34d4d217`  |
| 1485   | No file  | `5fdd34d4d217`  |
| 1481   | No file  | `5fdd34d4d217`  |
| 1474   | No file  | `5fdd34d4d217`  |
| 1466   | No file  | `5fdd34d4d217`  |
| 1462   | No file  | `5fdd34d4d217`  |
| 1459   | No file  | `5fdd34d4d217`  |
| 1453   | No file  | `5fdd34d4d217`  |
| 1450   | No file  | `5fdd34d4d217`  |
| 1445   | No file  | `5fdd34d4d217`  |
| 1439   | No file  | `5fdd34d4d217`  |
| 1433   | No file  | `5fdd34d4d217`  |
| 1430   | No file  | `5fdd34d4d217`  |
| 1426   | No file  | `5fdd34d4d217`  |
| 1421   | No file  | `5fdd34d4d217`  |
| 1417   | No file  | `5fdd34d4d217`  |
| 1416   | No file  | `5fdd34d4d217`  |
| 1409   | No file  | `5fdd34d4d217`  |
| 1405   | No file  | `5fdd34d4d217`  |
| 1401   | No file  | `5fdd34d4d217`  |
| 1396   | No file  | `5fdd34d4d217`  |
| 1391   | No file  | `5fdd34d4d217`  |
| 1390   | No file  | `5fdd34d4d217`  |
| 1386   | No file  | `5fdd34d4d217`  |
| 1381   | No file  | `5fdd34d4d217`  |
| 1379   | No file  | `5fdd34d4d217`  |
| 1372   | No file  | `5fdd34d4d217`  |
| 1366   | No file  | `5fdd34d4d217`  |
| 1364   | No file  | `5fdd34d4d217`  |
| 1363   | No file  | `5fdd34d4d217`  |
| 1360   | No file  | `5fdd34d4d217`  |
| 1358   | No file  | `5fdd34d4d217`  |
| 1355   | No file  | `5fdd34d4d217`  |
| 1351   | No file  | `5fdd34d4d217`  |
| 1348   | No file  | `5fdd34d4d217`  |
| 1346   | No file  | `5fdd34d4d217`  |
| 1341   | No file  | `5fdd34d4d217`  |
| 1340   | No file  | `5fdd34d4d217`  |
| 1338   | No file  | `5fdd34d4d217`  |
| 1335   | No file  | `5fdd34d4d217`  |
| 1333   | No file  | `5fdd34d4d217`  |
| 1329   | No file  | `5fdd34d4d217`  |
| 1327   | No file  | `5fdd34d4d217`  |
| 1324   | No file  | `5fdd34d4d217`  |
| 1321   | No file  | `5fdd34d4d217`  |
| 1319   | No file  | `5fdd34d4d217`  |
| 1318   | No file  | `5fdd34d4d217`  |
| 1316   | No file  | `5fdd34d4d217`  |
| 1313   | No file  | `5fdd34d4d217`  |
| 1311   | No file  | `5fdd34d4d217`  |
| 1309   | No file  | `5fdd34d4d217`  |
| 1304   | No file  | `5fdd34d4d217`  |
| 1292   | No file  | `5fdd34d4d217`  |
| 1286   | No file  | `5fdd34d4d217`  |
| 1280   | No file  | `5fdd34d4d217`  |
| 1276   | No file  | `5fdd34d4d217`  |
| 1267   | No file  | `5fdd34d4d217`  |
| 1261   | No file  | `5fdd34d4d217`  |
| 1256   | No file  | `5fdd34d4d217`  |
| 1250   | No file  | `5fdd34d4d217`  |
| 1246   | No file  | `5fdd34d4d217`  |
| 1239   | No file  | `5fdd34d4d217`  |
| 1230   | No file  | `5fdd34d4d217`  |
| 1226   | No file  | `5fdd34d4d217`  |
| 1220   | No file  | `5fdd34d4d217`  |
| 1217   | No file  | `5fdd34d4d217`  |
| 1211   | No file  | `5fdd34d4d217`  |
| 1210   | No file  | `5fdd34d4d217`  |
| 1208   | No file  | `5fdd34d4d217`  |
| 1203   | No file  | `5fdd34d4d217`  |
| 1197   | No file  | `5fdd34d4d217`  |
| 1194   | No file  | `5fdd34d4d217`  |
| 1192   | No file  | `5fdd34d4d217`  |
| 1187   | No file  | `5fdd34d4d217`  |
| 1183   | No file  | `5fdd34d4d217`  |
| 1177   | No file  | `5fdd34d4d217`  |
| 1173   | No file  | `5fdd34d4d217`  |
| 1167   | No file  | `5fdd34d4d217`  |
| 1164   | No file  | `5fdd34d4d217`  |
| 1156   | No file  | `5fdd34d4d217`  |
| 1149   | No file  | `5fdd34d4d217`  |
| 1144   | No file  | `5fdd34d4d217`  |
| 1137   | No file  | `5fdd34d4d217`  |
| 1132   | No file  | `5fdd34d4d217`  |
| 1127   | No file  | `5fdd34d4d217`  |
| 1122   | No file  | `5fdd34d4d217`  |
| 1118   | No file  | `5fdd34d4d217`  |
| 1114   | No file  | `5fdd34d4d217`  |
| 1109   | No file  | `5fdd34d4d217`  |
| 1102   | No file  | `5fdd34d4d217`  |
| 1096   | No file  | `5fdd34d4d217`  |
| 1088   | No file  | `5fdd34d4d217`  |
| 1081   | No file  | `5fdd34d4d217`  |
| 1076   | No file  | `5fdd34d4d217`  |
| 1069   | No file  | `5fdd34d4d217`  |
| 1064   | No file  | `5fdd34d4d217`  |
| 1058   | No file  | `5fdd34d4d217`  |
| 1051   | No file  | `5fdd34d4d217`  |
| 1044   | No file  | `5fdd34d4d217`  |
| 1036   | No file  | `5fdd34d4d217`  |
| 1026   | No file  | `5fdd34d4d217`  |
| 1016   | No file  | `5fdd34d4d217`  |
| 1009   | No file  | `5fdd34d4d217`  |
| 1005   | No file  | `5fdd34d4d217`  |
| 1000   | No file  | `5fdd34d4d217`  |
| 998    | No file  | `5fdd34d4d217`  |
| 990    | No file  | `5fdd34d4d217`  |
| 979    | No file  | `5fdd34d4d217`  |
| 972    | No file  | `5fdd34d4d217`  |
| 963    | No file  | `5fdd34d4d217`  |
| 955    | No file  | `5fdd34d4d217`  |
| 946    | No file  | `5fdd34d4d217`  |
| 938    | No file  | `5fdd34d4d217`  |
| 927    | No file  | `5fdd34d4d217`  |
| 911    | No file  | `5fdd34d4d217`  |
| 904    | No file  | `5fdd34d4d217`  |
| 899    | No file  | `5fdd34d4d217`  |
| 894    | No file  | `5fdd34d4d217`  |
| 885    | No file  | `5fdd34d4d217`  |
| 879    | No file  | `5fdd34d4d217`  |
| 872    | No file  | `5fdd34d4d217`  |
| 864    | No file  | `5fdd34d4d217`  |
| 855    | No file  | `5fdd34d4d217`  |
| 853    | No file  | `5fdd34d4d217`  |
| 845    | No file  | `5fdd34d4d217`  |
| 837    | No file  | `5fdd34d4d217`  |
| 829    | No file  | `5fdd34d4d217`  |
| 822    | No file  | `5fdd34d4d217`  |
| 814    | No file  | `5fdd34d4d217`  |
| 805    | No file  | `5fdd34d4d217`  |
| 794    | No file  | `5fdd34d4d217`  |
| 787    | No file  | `5fdd34d4d217`  |
| 780    | No file  | `5fdd34d4d217`  |
| 771    | No file  | `5fdd34d4d217`  |
| 760    | No file  | `5fdd34d4d217`  |
| 748    | No file  | `5fdd34d4d217`  |
| 741    | No file  | `5fdd34d4d217`  |
| 736    | No file  | `5fdd34d4d217`  |
| 731    | No file  | `5fdd34d4d217`  |
| 723    | No file  | `5fdd34d4d217`  |
| 711    | No file  | `5fdd34d4d217`  |
| 707    | No file  | `5fdd34d4d217`  |
| 697    | No file  | `5fdd34d4d217`  |
| 689    | No file  | `5fdd34d4d217`  |
| 683    | No file  | `5fdd34d4d217`  |
| 678    | No file  | `5fdd34d4d217`  |
| 670    | No file  | `5fdd34d4d217`  |
| 661    | No file  | `5fdd34d4d217`  |
| 656    | No file  | `5fdd34d4d217`  |
| 652    | No file  | `5fdd34d4d217`  |
| 643    | No file  | `5fdd34d4d217`  |
| 637    | No file  | `5fdd34d4d217`  |
| 630    | No file  | `5fdd34d4d217`  |
| 627    | No file  | `5fdd34d4d217`  |
| 621    | No file  | `5fdd34d4d217`  |
| 617    | No file  | `5fdd34d4d217`  |
| 615    | No file  | `5fdd34d4d217`  |
| 606    | No file  | `5fdd34d4d217`  |
| 599    | No file  | `5fdd34d4d217`  |
| 592    | No file  | `5fdd34d4d217`  |
| 586    | No file  | `5fdd34d4d217`  |
| 577    | No file  | `5fdd34d4d217`  |
| 569    | No file  | `5fdd34d4d217`  |
| 561    | No file  | `5fdd34d4d217`  |
| 554    | No file  | `5fdd34d4d217`  |
| 542    | No file  | `5fdd34d4d217`  |
| 532    | No file  | `5fdd34d4d217`  |
| 531    | No file  | `5fdd34d4d217`  |
| 526    | No file  | `5fdd34d4d217`  |
| 521    | No file  | `5fdd34d4d217`  |
| 517    | No file  | `5fdd34d4d217`  |
| 510    | No file  | `5fdd34d4d217`  |
| 508    | No file  | `5fdd34d4d217`  |
| 504    | No file  | `5fdd34d4d217`  |
| 497    | No file  | `5fdd34d4d217`  |
| 491    | No file  | `5fdd34d4d217`  |
| 485    | No file  | `5fdd34d4d217`  |
| 478    | No file  | `5fdd34d4d217`  |
| 472    | No file  | `5fdd34d4d217`  |
| 466    | No file  | `5fdd34d4d217`  |
| 457    | No file  | `5fdd34d4d217`  |
| 452    | No file  | `5fdd34d4d217`  |
| 449    | No file  | `5fdd34d4d217`  |
| 435    | No file  | `5fdd34d4d217`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type               | Field        | Notes                                           |
| ------------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`             | Options            | options      | See Options                                     |
| `+0x12`             | u32                | stage_count  | Number of stages                                |
| `+0x16`             | Stage[stage_count] | stages       | See Stage                                       |
| `stages+0x00`       | String Table       | string_table | See String Table                                |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `stages` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                      |

### Options (14 bytes)

| Offset  | Type | Field      | Notes                                            |
| ------- | ---- | ---------- | ------------------------------------------------ |
| `+0x00` | u32  | unknown_00 | `24` on client 3482, equal to `stage_count`      |
| `+0x04` | u32  | unknown_04 | `3` on client 3482                               |
| `+0x08` | u32  | unknown_08 | `56` on client 3482                              |
| `+0x0C` | u16  | unknown_0c | `10` on client 3482                              |

### Stage (variable: 40 bytes + reward entries)

| Offset               | Type                              | Field               | Notes                                                                         |
| -------------------- | --------------------------------- | ------------------- | ----------------------------------------------------------------------------- |
| `+0x00`              | u32                               | stage_key           | `1` to `stage_count` in file order; the stage key the Lua getters take        |
| `+0x04`              | u32                               | unknown_str_ref_04  | String-table index of a Korean stage text with a space after `제` (`제 1의 환상`) |
| `+0x08`              | u32                               | unknown_str_ref_08  | String-table index of a Korean stage text, `제1의 환상` on stages 1 to 21, the `unknown_str_ref_04` text on stages 22 to 24 |
| `+0x0C`              | u32                               | boss_texture_ref    | String-table index of the boss banner texture name; an empty string on the stages that keep the boss of the stage before |
| `+0x10`              | f32                               | match_min_offence   | Minimum AP to match: `300` to `415` on client 3482, `+5` per stage            |
| `+0x14`              | f32                               | match_min_defence   | Minimum DP to match: `390` to `475` on client 3482                            |
| `+0x18`              | f32                               | recommended_offence | Recommended AP: `1070` to `2290` on client 3482                               |
| `+0x1C`              | f32                               | recommended_defence | Recommended DP: `420` to `820` on client 3482                                 |
| `+0x20`              | u32                               | first_reward_count  | Number of `first_rewards`; `1` on every stage of client 3482                  |
| `+0x24`              | Reward Entry[first_reward_count]  | first_rewards       | The first clear rewards; see Reward Entry                                     |
| `first_rewards+0x00` | u32                               | weekly_reward_count | Number of `weekly_rewards`; `2` on every stage of client 3482                 |
| `first_rewards+0x04` | Reward Entry[weekly_reward_count] | weekly_rewards      | The weekly rewards; see Reward Entry                                          |

### Reward Entry (16 bytes)

| Offset  | Type     | Field            | Notes                                                                                   |
| ------- | -------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32      | item_enchant_key | `enchant_level << 24 \| item_id`; `ToClient_getBloodAltarRewardItemEnchantKey`          |
| `+0x04` | bytes[4] | padding_04       | Alignment of the u64 `item_count` to 8 bytes; `f6 7f 00 00` in every entry of client 3482 |
| `+0x08` | u64      | item_count       | `ToClient_getBloodAltarRewardItemCount`; `1` in every entry of client 3482              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                              |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; 54 on client 3482                               |
| `+0x04` | pstr[string_count] | strings      | UTF-16 stage texts and boss texture names, in stage order          |

## Layout 1

### Stage (40 bytes)

| Offset  | Type | Field                  | Notes                                                                  |
| ------- | ---- | ---------------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | stage_key              | `1` to `stage_count` in file order                                     |
| `+0x04` | u32  | unknown_str_ref_04     | String-table index of a Korean stage text                              |
| `+0x08` | u32  | unknown_str_ref_08     | String-table index of a Korean stage text                              |
| `+0x0C` | u32  | boss_texture_ref       | String-table index of the boss banner texture name                     |
| `+0x10` | f32  | match_min_offence      | Same as Layout 2                                                       |
| `+0x14` | f32  | match_min_defence      | Same as Layout 2                                                       |
| `+0x18` | f32  | recommended_offence    | Same as Layout 2                                                       |
| `+0x1C` | f32  | recommended_defence    | Same as Layout 2                                                       |
| `+0x20` | u32  | weekly_reward_item_key | One item key, Bloodstained Spoils - The Nth Illusion (`980040 + N`) on stage N |
| `+0x24` | u32  | first_reward_item_key  | One item key, Bloodstained Welcome - The Nth Illusion (`980010 + N`) on stage N |

## Boss Textures

Client 3482: the stages with a non-empty `boss_texture_ref` string; the
other stages, 1 and 2 among them, point at an empty string. Each texture
is a `Combine_Etc_BloodAltar_PopUpImg_Boss_<n>` UI texture ID.

| Stage | Boss texture                             |
| ----- | ---------------------------------------- |
| 3     | `Combine_Etc_BloodAltar_PopUpImg_Boss_2` |
| 6     | `Combine_Etc_BloodAltar_PopUpImg_Boss_3` |
| 9     | `Combine_Etc_BloodAltar_PopUpImg_Boss_4` |
| 12    | `Combine_Etc_BloodAltar_PopUpImg_Boss_8` |
| 15    | `Combine_Etc_BloodAltar_PopUpImg_Boss_9` |
| 18    | `Combine_Etc_BloodAltar_PopUpImg_Boss_6` |
| 21    | `Combine_Etc_BloodAltar_PopUpImg_Boss_1` |
| 24    | `Combine_Etc_BloodAltar_PopUpImg_Boss_10` |

## Field Names

Blood Altar is newer than client 1784: the file is not in its archives
and no sheet of a private server's `DataSheets.bexcel` on that client has
`Blood` or `Altar` in its name. The names come from the getters of the
stage menu Lua (`panel_window_bloodaltarmenu_all_1.luac`, client 3482):

- `stage_key`: the menu lists `ToClient_getBloodAltarStageSize()` stages
  and passes `index + 1` as the stage key to every getter, so the keys run
  from `1` in file order.
- `boss_texture_ref`: `ToClient_getBloodAltarBossTextureID(stageKey)`
  goes to `setRenderTexture` of the boss banner; the string is a UI
  texture ID.
- `first_rewards` and `weekly_rewards`: `ToClient_getBloodAltarRewardSize(stageKey, isFirst)`
  with `true` and `false`, then `ToClient_getBloodAltarRewardItemEnchantKey`
  and `ToClient_getBloodAltarRewardItemCount` per entry. The first list
  holds Bloodstained Welcome items, the second Bloodstained Spoils items,
  the item names of the first clear and the weekly reward.
- `match_min_offence` and `match_min_defence`:
  `ToClient_getBloodAltarMatchMinStatOffence` and `...Defence`;
  `recommended_offence` and `recommended_defence`:
  `ToClient_getBloodAltarRecommandStatOffence` and `...Defence`. In game
  the stage 1 window shows a minimum AP of 300 and DP of 390 and a
  recommended AP of 1070 and DP of 420, the values at `+0x10` to `+0x1C`
  in that order.

The Lua also calls `ToClient_getBloodAltarStageName(stageKey)`; which
stage text it reads is open (see Open Questions).

## Notes

- Layout 1 (clients 3283 to 3454) stores one weekly reward item key and
  one first clear item key per stage in place of the two reward lists.
  Layout 2 (client 3474) turns them into lists and adds Combat Secret
  Book (M) to every stage's weekly rewards.
- `padding_04` is the alignment gap of an in-memory entry (u32 key, then a
  u64 count at `+0x08`). `0x00007FF6` is the high half of an x64 image
  address, so the bytes are left over from memory, not set by the data.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`: the
  stage key, the boss texture, the four AP and DP values and both reward
  lists.

## Open Questions

### Which Stage Text Is the Name

`ToClient_getBloodAltarStageName(stageKey)` fills the stage list and the
title of the selected stage, and `ToClient_getBloodAltarStageTitle()` the
HUD title while a stage runs. Both stage texts read as the stage name,
one with a space after `제` and one without, so either getter can read
either string.

### What the Options Are

`unknown_00` equals the stage count on client 3482. The HUD shows
`ToClient_getBloodAltarPlayableCount()` of
`ToClient_getMaxBloodaltarPlayableCount()` retries
(`LUA_BLOODALTAR_HUD_RETRY_LEFT`), but in game a run has 5 retries and no
option holds `5`, so the retry count is not in this file. A party in
the Blood Altar has at most 3 players, the value of `unknown_04`; no Lua
getter ties the two together yet. No Lua call names `unknown_08` (`56`)
or `unknown_0c` (`10`).
