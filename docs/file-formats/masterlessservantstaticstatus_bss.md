# `masterlessservantstaticstatus.bss` Format

## Purpose

The Traveler's Horse, the horse a stable keeper lends to a player without a
horse of their own: five rows of three numbers, each ending with the horse's
character ID 31560. The client Lua (`panel_dialog_horsewithoutowner_all`)
holds the same ID as `_rentCharacterKeyRaw = 31560` and summons it with
`ToClient_SummonMasterLessHorse`. What the three numbers set is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------- | ----- | ------- | --------- |
| 1      | 1991 and later | 3483    | `masterlessservantstaticstatus.bss` | 90    | 5 Row   | 14        |

| Layout | File                                | Known        | Unknown      |
| ------ | ----------------------------------- | ------------ | ------------ |
| 1      | `masterlessservantstaticstatus.bss` | 30 B (33.3%) | 60 B (66.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fb8654e45d2c`  |
| 3482   | Layout 1 | `fb8654e45d2c`  |
| 3474   | Layout 1 | `fb8654e45d2c`  |
| 3473   | Layout 1 | `fb8654e45d2c`  |
| 3464   | Layout 1 | `fb8654e45d2c`  |
| 3458   | Layout 1 | `fb8654e45d2c`  |
| 3454   | Layout 1 | `fb8654e45d2c`  |
| 3444   | Layout 1 | `fb8654e45d2c`  |
| 3435   | Layout 1 | `fb8654e45d2c`  |
| 3426   | Layout 1 | `fb8654e45d2c`  |
| 3418   | Layout 1 | `fb8654e45d2c`  |
| 3412   | Layout 1 | `fb8654e45d2c`  |
| 3402   | Layout 1 | `fb8654e45d2c`  |
| 3396   | Layout 1 | `fb8654e45d2c`  |
| 3387   | Layout 1 | `fb8654e45d2c`  |
| 3381   | Layout 1 | `fb8654e45d2c`  |
| 3373   | Layout 1 | `fb8654e45d2c`  |
| 3364   | Layout 1 | `fb8654e45d2c`  |
| 3356   | Layout 1 | `fb8654e45d2c`  |
| 3349   | Layout 1 | `fb8654e45d2c`  |
| 3342   | Layout 1 | `fb8654e45d2c`  |
| 3335   | Layout 1 | `fb8654e45d2c`  |
| 3326   | Layout 1 | `fb8654e45d2c`  |
| 3321   | Layout 1 | `fb8654e45d2c`  |
| 3314   | Layout 1 | `fb8654e45d2c`  |
| 3303   | Layout 1 | `fb8654e45d2c`  |
| 3302   | Layout 1 | `fb8654e45d2c`  |
| 3293   | Layout 1 | `fb8654e45d2c`  |
| 3283   | Layout 1 | `fb8654e45d2c`  |
| 3275   | Layout 1 | `fb8654e45d2c`  |
| 3267   | Layout 1 | `fb8654e45d2c`  |
| 3258   | Layout 1 | `fb8654e45d2c`  |
| 3251   | Layout 1 | `fb8654e45d2c`  |
| 3242   | Layout 1 | `fb8654e45d2c`  |
| 3235   | Layout 1 | `fb8654e45d2c`  |
| 3229   | Layout 1 | `fb8654e45d2c`  |
| 3212   | Layout 1 | `fb8654e45d2c`  |
| 3203   | Layout 1 | `fb8654e45d2c`  |
| 3193   | Layout 1 | `fb8654e45d2c`  |
| 3186   | Layout 1 | `fb8654e45d2c`  |
| 3177   | Layout 1 | `fb8654e45d2c`  |
| 3169   | Layout 1 | `fb8654e45d2c`  |
| 3158   | Layout 1 | `fb8654e45d2c`  |
| 3151   | Layout 1 | `fb8654e45d2c`  |
| 3144   | Layout 1 | `fb8654e45d2c`  |
| 3133   | Layout 1 | `fb8654e45d2c`  |
| 3125   | Layout 1 | `fb8654e45d2c`  |
| 3118   | Layout 1 | `fb8654e45d2c`  |
| 3111   | Layout 1 | `fb8654e45d2c`  |
| 3103   | Layout 1 | `fb8654e45d2c`  |
| 3095   | Layout 1 | `fb8654e45d2c`  |
| 3086   | Layout 1 | `fb8654e45d2c`  |
| 3072   | Layout 1 | `fb8654e45d2c`  |
| 3062   | Layout 1 | `fb8654e45d2c`  |
| 3052   | Layout 1 | `fb8654e45d2c`  |
| 3045   | Layout 1 | `fb8654e45d2c`  |
| 3037   | Layout 1 | `fb8654e45d2c`  |
| 3030   | Layout 1 | `fb8654e45d2c`  |
| 3021   | Layout 1 | `fb8654e45d2c`  |
| 3012   | Layout 1 | `fb8654e45d2c`  |
| 3002   | Layout 1 | `fb8654e45d2c`  |
| 2995   | Layout 1 | `fb8654e45d2c`  |
| 2987   | Layout 1 | `fb8654e45d2c`  |
| 2978   | Layout 1 | `fb8654e45d2c`  |
| 2970   | Layout 1 | `fb8654e45d2c`  |
| 2959   | Layout 1 | `fb8654e45d2c`  |
| 2951   | Layout 1 | `fb8654e45d2c`  |
| 2942   | Layout 1 | `fb8654e45d2c`  |
| 2935   | Layout 1 | `fb8654e45d2c`  |
| 2932   | Layout 1 | `fb8654e45d2c`  |
| 2923   | Layout 1 | `fb8654e45d2c`  |
| 2919   | Layout 1 | `fb8654e45d2c`  |
| 2907   | Layout 1 | `fb8654e45d2c`  |
| 2900   | Layout 1 | `fb8654e45d2c`  |
| 2891   | Layout 1 | `fb8654e45d2c`  |
| 2882   | Layout 1 | `fb8654e45d2c`  |
| 2872   | Layout 1 | `fb8654e45d2c`  |
| 2863   | Layout 1 | `fb8654e45d2c`  |
| 2855   | Layout 1 | `fb8654e45d2c`  |
| 2849   | Layout 1 | `fb8654e45d2c`  |
| 2844   | Layout 1 | `fb8654e45d2c`  |
| 2834   | Layout 1 | `fb8654e45d2c`  |
| 2825   | Layout 1 | `fb8654e45d2c`  |
| 2819   | Layout 1 | `fb8654e45d2c`  |
| 2811   | Layout 1 | `fb8654e45d2c`  |
| 2803   | Layout 1 | `fb8654e45d2c`  |
| 2794   | Layout 1 | `fb8654e45d2c`  |
| 2783   | Layout 1 | `fb8654e45d2c`  |
| 2774   | Layout 1 | `fb8654e45d2c`  |
| 2765   | Layout 1 | `fb8654e45d2c`  |
| 2756   | Layout 1 | `fb8654e45d2c`  |
| 2750   | Layout 1 | `fb8654e45d2c`  |
| 2743   | Layout 1 | `fb8654e45d2c`  |
| 2736   | Layout 1 | `fb8654e45d2c`  |
| 2726   | Layout 1 | `fb8654e45d2c`  |
| 2717   | Layout 1 | `fb8654e45d2c`  |
| 2709   | Layout 1 | `fb8654e45d2c`  |
| 2703   | Layout 1 | `fb8654e45d2c`  |
| 2695   | Layout 1 | `fb8654e45d2c`  |
| 2684   | Layout 1 | `fb8654e45d2c`  |
| 2672   | Layout 1 | `fb8654e45d2c`  |
| 2665   | Layout 1 | `fb8654e45d2c`  |
| 2657   | Layout 1 | `fb8654e45d2c`  |
| 2649   | Layout 1 | `fb8654e45d2c`  |
| 2644   | Layout 1 | `fb8654e45d2c`  |
| 2637   | Layout 1 | `fb8654e45d2c`  |
| 2629   | Layout 1 | `fb8654e45d2c`  |
| 2619   | Layout 1 | `fb8654e45d2c`  |
| 2612   | Layout 1 | `fb8654e45d2c`  |
| 2606   | Layout 1 | `fb8654e45d2c`  |
| 2602   | Layout 1 | `fb8654e45d2c`  |
| 2601   | Layout 1 | `fb8654e45d2c`  |
| 2592   | Layout 1 | `fb8654e45d2c`  |
| 2583   | Layout 1 | `fb8654e45d2c`  |
| 2575   | Layout 1 | `fb8654e45d2c`  |
| 2567   | Layout 1 | `fb8654e45d2c`  |
| 2560   | Layout 1 | `fb8654e45d2c`  |
| 2553   | Layout 1 | `fb8654e45d2c`  |
| 2545   | Layout 1 | `fb8654e45d2c`  |
| 2538   | Layout 1 | `fb8654e45d2c`  |
| 2529   | Layout 1 | `fb8654e45d2c`  |
| 2519   | Layout 1 | `fb8654e45d2c`  |
| 2513   | Layout 1 | `fb8654e45d2c`  |
| 2510   | Layout 1 | `fb8654e45d2c`  |
| 2507   | Layout 1 | `fb8654e45d2c`  |
| 2503   | Layout 1 | `fb8654e45d2c`  |
| 2498   | Layout 1 | `fb8654e45d2c`  |
| 2492   | Layout 1 | `fb8654e45d2c`  |
| 2487   | Layout 1 | `fb8654e45d2c`  |
| 2480   | Layout 1 | `fb8654e45d2c`  |
| 2474   | Layout 1 | `fb8654e45d2c`  |
| 2468   | Layout 1 | `fb8654e45d2c`  |
| 2460   | Layout 1 | `fb8654e45d2c`  |
| 2453   | Layout 1 | `fb8654e45d2c`  |
| 2444   | Layout 1 | `fb8654e45d2c`  |
| 2438   | Layout 1 | `fb8654e45d2c`  |
| 2434   | Layout 1 | `fb8654e45d2c`  |
| 2429   | Layout 1 | `fb8654e45d2c`  |
| 2421   | Layout 1 | `fb8654e45d2c`  |
| 2414   | Layout 1 | `fb8654e45d2c`  |
| 2407   | Layout 1 | `fb8654e45d2c`  |
| 2401   | Layout 1 | `fb8654e45d2c`  |
| 2397   | Layout 1 | `fb8654e45d2c`  |
| 2393   | Layout 1 | `fb8654e45d2c`  |
| 2384   | Layout 1 | `fb8654e45d2c`  |
| 2378   | Layout 1 | `fb8654e45d2c`  |
| 2372   | Layout 1 | `fb8654e45d2c`  |
| 2358   | Layout 1 | `fb8654e45d2c`  |
| 2352   | Layout 1 | `fb8654e45d2c`  |
| 2347   | Layout 1 | `fb8654e45d2c`  |
| 2343   | Layout 1 | `fb8654e45d2c`  |
| 2335   | Layout 1 | `fb8654e45d2c`  |
| 2327   | Layout 1 | `fb8654e45d2c`  |
| 2324   | Layout 1 | `fb8654e45d2c`  |
| 2319   | Layout 1 | `fb8654e45d2c`  |
| 2313   | Layout 1 | `fb8654e45d2c`  |
| 2308   | Layout 1 | `fb8654e45d2c`  |
| 2302   | Layout 1 | `fb8654e45d2c`  |
| 2295   | Layout 1 | `fb8654e45d2c`  |
| 2290   | Layout 1 | `fb8654e45d2c`  |
| 2284   | Layout 1 | `fb8654e45d2c`  |
| 2276   | Layout 1 | `fb8654e45d2c`  |
| 2269   | Layout 1 | `fb8654e45d2c`  |
| 2259   | Layout 1 | `fb8654e45d2c`  |
| 2250   | Layout 1 | `fb8654e45d2c`  |
| 2243   | Layout 1 | `fb8654e45d2c`  |
| 2235   | Layout 1 | `fb8654e45d2c`  |
| 2229   | Layout 1 | `fb8654e45d2c`  |
| 2224   | Layout 1 | `fb8654e45d2c`  |
| 2218   | Layout 1 | `fb8654e45d2c`  |
| 2215   | Layout 1 | `fb8654e45d2c`  |
| 2207   | Layout 1 | `fb8654e45d2c`  |
| 2203   | Layout 1 | `fb8654e45d2c`  |
| 2196   | Layout 1 | `fb8654e45d2c`  |
| 2192   | Layout 1 | `fb8654e45d2c`  |
| 2189   | Layout 1 | `fb8654e45d2c`  |
| 2183   | Layout 1 | `fb8654e45d2c`  |
| 2179   | Layout 1 | `fb8654e45d2c`  |
| 2171   | Layout 1 | `fb8654e45d2c`  |
| 2163   | Layout 1 | `fb8654e45d2c`  |
| 2156   | Layout 1 | `fb8654e45d2c`  |
| 2151   | Layout 1 | `fb8654e45d2c`  |
| 2147   | Layout 1 | `fb8654e45d2c`  |
| 2142   | Layout 1 | `fb8654e45d2c`  |
| 2138   | Layout 1 | `fb8654e45d2c`  |
| 2134   | Layout 1 | `fb8654e45d2c`  |
| 2130   | Layout 1 | `fb8654e45d2c`  |
| 2122   | Layout 1 | `fb8654e45d2c`  |
| 2107   | Layout 1 | `fb8654e45d2c`  |
| 2098   | Layout 1 | `fb8654e45d2c`  |
| 2089   | Layout 1 | `fb8654e45d2c`  |
| 2081   | Layout 1 | `fb8654e45d2c`  |
| 2073   | Layout 1 | `fb8654e45d2c`  |
| 2067   | Layout 1 | `fb8654e45d2c`  |
| 2063   | Layout 1 | `fb8654e45d2c`  |
| 2059   | Layout 1 | `fb8654e45d2c`  |
| 2052   | Layout 1 | `fb8654e45d2c`  |
| 2044   | Layout 1 | `fb8654e45d2c`  |
| 2039   | Layout 1 | `fb8654e45d2c`  |
| 2032   | Layout 1 | `fb8654e45d2c`  |
| 2025   | Layout 1 | `fb8654e45d2c`  |
| 2011   | Layout 1 | `fb8654e45d2c`  |
| 2005   | Layout 1 | `fb8654e45d2c`  |
| 2000   | Layout 1 | `fb8654e45d2c`  |
| 1996   | Layout 1 | `fb8654e45d2c`  |
| 1991   | Layout 1 | `fb8654e45d2c`  |
| 1985   | No file  | `fb8654e45d2c`  |
| 1980   | No file  | `fb8654e45d2c`  |
| 1969   | No file  | `fb8654e45d2c`  |
| 1964   | No file  | `fb8654e45d2c`  |
| 1958   | No file  | `fb8654e45d2c`  |
| 1950   | No file  | `fb8654e45d2c`  |
| 1945   | No file  | `fb8654e45d2c`  |
| 1937   | No file  | `fb8654e45d2c`  |
| 1933   | No file  | `fb8654e45d2c`  |
| 1927   | No file  | `fb8654e45d2c`  |
| 1921   | No file  | `fb8654e45d2c`  |
| 1914   | No file  | `fb8654e45d2c`  |
| 1908   | No file  | `fb8654e45d2c`  |
| 1897   | No file  | `fb8654e45d2c`  |
| 1892   | No file  | `fb8654e45d2c`  |
| 1886   | No file  | `fb8654e45d2c`  |
| 1881   | No file  | `fb8654e45d2c`  |
| 1871   | No file  | `fb8654e45d2c`  |
| 1866   | No file  | `fb8654e45d2c`  |
| 1862   | No file  | `fb8654e45d2c`  |
| 1854   | No file  | `fb8654e45d2c`  |
| 1846   | No file  | `fb8654e45d2c`  |
| 1838   | No file  | `fb8654e45d2c`  |
| 1832   | No file  | `fb8654e45d2c`  |
| 1826   | No file  | `fb8654e45d2c`  |
| 1822   | No file  | `fb8654e45d2c`  |
| 1818   | No file  | `fb8654e45d2c`  |
| 1804   | No file  | `fb8654e45d2c`  |
| 1794   | No file  | `fb8654e45d2c`  |
| 1790   | No file  | `fb8654e45d2c`  |
| 1784   | No file  | `fb8654e45d2c`  |
| 1774   | No file  | `fb8654e45d2c`  |
| 1771   | No file  | `fb8654e45d2c`  |
| 1762   | No file  | `fb8654e45d2c`  |
| 1759   | No file  | `fb8654e45d2c`  |
| 1754   | No file  | `fb8654e45d2c`  |
| 1749   | No file  | `fb8654e45d2c`  |
| 1743   | No file  | `fb8654e45d2c`  |
| 1737   | No file  | `fb8654e45d2c`  |
| 1731   | No file  | `fb8654e45d2c`  |
| 1725   | No file  | `fb8654e45d2c`  |
| 1717   | No file  | `fb8654e45d2c`  |
| 1710   | No file  | `fb8654e45d2c`  |
| 1704   | No file  | `fb8654e45d2c`  |
| 1698   | No file  | `fb8654e45d2c`  |
| 1690   | No file  | `fb8654e45d2c`  |
| 1685   | No file  | `fb8654e45d2c`  |
| 1680   | No file  | `fb8654e45d2c`  |
| 1674   | No file  | `fb8654e45d2c`  |
| 1668   | No file  | `fb8654e45d2c`  |
| 1659   | No file  | `fb8654e45d2c`  |
| 1649   | No file  | `fb8654e45d2c`  |
| 1642   | No file  | `fb8654e45d2c`  |
| 1636   | No file  | `fb8654e45d2c`  |
| 1628   | No file  | `fb8654e45d2c`  |
| 1622   | No file  | `fb8654e45d2c`  |
| 1614   | No file  | `fb8654e45d2c`  |
| 1608   | No file  | `fb8654e45d2c`  |
| 1602   | No file  | `fb8654e45d2c`  |
| 1598   | No file  | `fb8654e45d2c`  |
| 1594   | No file  | `fb8654e45d2c`  |
| 1590   | No file  | `fb8654e45d2c`  |
| 1587   | No file  | `fb8654e45d2c`  |
| 1584   | No file  | `fb8654e45d2c`  |
| 1579   | No file  | `fb8654e45d2c`  |
| 1572   | No file  | `fb8654e45d2c`  |
| 1565   | No file  | `fb8654e45d2c`  |
| 1559   | No file  | `fb8654e45d2c`  |
| 1554   | No file  | `fb8654e45d2c`  |
| 1547   | No file  | `fb8654e45d2c`  |
| 1537   | No file  | `fb8654e45d2c`  |
| 1529   | No file  | `fb8654e45d2c`  |
| 1524   | No file  | `fb8654e45d2c`  |
| 1519   | No file  | `fb8654e45d2c`  |
| 1509   | No file  | `fb8654e45d2c`  |
| 1506   | No file  | `fb8654e45d2c`  |
| 1504   | No file  | `fb8654e45d2c`  |
| 1500   | No file  | `fb8654e45d2c`  |
| 1493   | No file  | `fb8654e45d2c`  |
| 1489   | No file  | `fb8654e45d2c`  |
| 1485   | No file  | `fb8654e45d2c`  |
| 1481   | No file  | `fb8654e45d2c`  |
| 1474   | No file  | `fb8654e45d2c`  |
| 1466   | No file  | `fb8654e45d2c`  |
| 1462   | No file  | `fb8654e45d2c`  |
| 1459   | No file  | `fb8654e45d2c`  |
| 1453   | No file  | `fb8654e45d2c`  |
| 1450   | No file  | `fb8654e45d2c`  |
| 1445   | No file  | `fb8654e45d2c`  |
| 1439   | No file  | `fb8654e45d2c`  |
| 1433   | No file  | `fb8654e45d2c`  |
| 1430   | No file  | `fb8654e45d2c`  |
| 1426   | No file  | `fb8654e45d2c`  |
| 1421   | No file  | `fb8654e45d2c`  |
| 1417   | No file  | `fb8654e45d2c`  |
| 1416   | No file  | `fb8654e45d2c`  |
| 1409   | No file  | `fb8654e45d2c`  |
| 1405   | No file  | `fb8654e45d2c`  |
| 1401   | No file  | `fb8654e45d2c`  |
| 1396   | No file  | `fb8654e45d2c`  |
| 1391   | No file  | `fb8654e45d2c`  |
| 1390   | No file  | `fb8654e45d2c`  |
| 1386   | No file  | `fb8654e45d2c`  |
| 1381   | No file  | `fb8654e45d2c`  |
| 1379   | No file  | `fb8654e45d2c`  |
| 1372   | No file  | `fb8654e45d2c`  |
| 1366   | No file  | `fb8654e45d2c`  |
| 1364   | No file  | `fb8654e45d2c`  |
| 1363   | No file  | `fb8654e45d2c`  |
| 1360   | No file  | `fb8654e45d2c`  |
| 1358   | No file  | `fb8654e45d2c`  |
| 1355   | No file  | `fb8654e45d2c`  |
| 1351   | No file  | `fb8654e45d2c`  |
| 1348   | No file  | `fb8654e45d2c`  |
| 1346   | No file  | `fb8654e45d2c`  |
| 1341   | No file  | `fb8654e45d2c`  |
| 1340   | No file  | `fb8654e45d2c`  |
| 1338   | No file  | `fb8654e45d2c`  |
| 1335   | No file  | `fb8654e45d2c`  |
| 1333   | No file  | `fb8654e45d2c`  |
| 1329   | No file  | `fb8654e45d2c`  |
| 1327   | No file  | `fb8654e45d2c`  |
| 1324   | No file  | `fb8654e45d2c`  |
| 1321   | No file  | `fb8654e45d2c`  |
| 1319   | No file  | `fb8654e45d2c`  |
| 1318   | No file  | `fb8654e45d2c`  |
| 1316   | No file  | `fb8654e45d2c`  |
| 1313   | No file  | `fb8654e45d2c`  |
| 1311   | No file  | `fb8654e45d2c`  |
| 1309   | No file  | `fb8654e45d2c`  |
| 1304   | No file  | `fb8654e45d2c`  |
| 1292   | No file  | `fb8654e45d2c`  |
| 1286   | No file  | `fb8654e45d2c`  |
| 1280   | No file  | `fb8654e45d2c`  |
| 1276   | No file  | `fb8654e45d2c`  |
| 1267   | No file  | `fb8654e45d2c`  |
| 1261   | No file  | `fb8654e45d2c`  |
| 1256   | No file  | `fb8654e45d2c`  |
| 1250   | No file  | `fb8654e45d2c`  |
| 1246   | No file  | `fb8654e45d2c`  |
| 1239   | No file  | `fb8654e45d2c`  |
| 1230   | No file  | `fb8654e45d2c`  |
| 1226   | No file  | `fb8654e45d2c`  |
| 1220   | No file  | `fb8654e45d2c`  |
| 1217   | No file  | `fb8654e45d2c`  |
| 1211   | No file  | `fb8654e45d2c`  |
| 1210   | No file  | `fb8654e45d2c`  |
| 1208   | No file  | `fb8654e45d2c`  |
| 1203   | No file  | `fb8654e45d2c`  |
| 1197   | No file  | `fb8654e45d2c`  |
| 1194   | No file  | `fb8654e45d2c`  |
| 1192   | No file  | `fb8654e45d2c`  |
| 1187   | No file  | `fb8654e45d2c`  |
| 1183   | No file  | `fb8654e45d2c`  |
| 1177   | No file  | `fb8654e45d2c`  |
| 1173   | No file  | `fb8654e45d2c`  |
| 1167   | No file  | `fb8654e45d2c`  |
| 1164   | No file  | `fb8654e45d2c`  |
| 1156   | No file  | `fb8654e45d2c`  |
| 1149   | No file  | `fb8654e45d2c`  |
| 1144   | No file  | `fb8654e45d2c`  |
| 1137   | No file  | `fb8654e45d2c`  |
| 1132   | No file  | `fb8654e45d2c`  |
| 1127   | No file  | `fb8654e45d2c`  |
| 1122   | No file  | `fb8654e45d2c`  |
| 1118   | No file  | `fb8654e45d2c`  |
| 1114   | No file  | `fb8654e45d2c`  |
| 1109   | No file  | `fb8654e45d2c`  |
| 1102   | No file  | `fb8654e45d2c`  |
| 1096   | No file  | `fb8654e45d2c`  |
| 1088   | No file  | `fb8654e45d2c`  |
| 1081   | No file  | `fb8654e45d2c`  |
| 1076   | No file  | `fb8654e45d2c`  |
| 1069   | No file  | `fb8654e45d2c`  |
| 1064   | No file  | `fb8654e45d2c`  |
| 1058   | No file  | `fb8654e45d2c`  |
| 1051   | No file  | `fb8654e45d2c`  |
| 1044   | No file  | `fb8654e45d2c`  |
| 1036   | No file  | `fb8654e45d2c`  |
| 1026   | No file  | `fb8654e45d2c`  |
| 1016   | No file  | `fb8654e45d2c`  |
| 1009   | No file  | `fb8654e45d2c`  |
| 1005   | No file  | `fb8654e45d2c`  |
| 1000   | No file  | `fb8654e45d2c`  |
| 998    | No file  | `fb8654e45d2c`  |
| 990    | No file  | `fb8654e45d2c`  |
| 979    | No file  | `fb8654e45d2c`  |
| 972    | No file  | `fb8654e45d2c`  |
| 963    | No file  | `fb8654e45d2c`  |
| 955    | No file  | `fb8654e45d2c`  |
| 946    | No file  | `fb8654e45d2c`  |
| 938    | No file  | `fb8654e45d2c`  |
| 927    | No file  | `fb8654e45d2c`  |
| 911    | No file  | `fb8654e45d2c`  |
| 904    | No file  | `fb8654e45d2c`  |
| 899    | No file  | `fb8654e45d2c`  |
| 894    | No file  | `fb8654e45d2c`  |
| 885    | No file  | `fb8654e45d2c`  |
| 879    | No file  | `fb8654e45d2c`  |
| 872    | No file  | `fb8654e45d2c`  |
| 864    | No file  | `fb8654e45d2c`  |
| 855    | No file  | `fb8654e45d2c`  |
| 853    | No file  | `fb8654e45d2c`  |
| 845    | No file  | `fb8654e45d2c`  |
| 837    | No file  | `fb8654e45d2c`  |
| 829    | No file  | `fb8654e45d2c`  |
| 822    | No file  | `fb8654e45d2c`  |
| 814    | No file  | `fb8654e45d2c`  |
| 805    | No file  | `fb8654e45d2c`  |
| 794    | No file  | `fb8654e45d2c`  |
| 787    | No file  | `fb8654e45d2c`  |
| 780    | No file  | `fb8654e45d2c`  |
| 771    | No file  | `fb8654e45d2c`  |
| 760    | No file  | `fb8654e45d2c`  |
| 748    | No file  | `fb8654e45d2c`  |
| 741    | No file  | `fb8654e45d2c`  |
| 736    | No file  | `fb8654e45d2c`  |
| 731    | No file  | `fb8654e45d2c`  |
| 723    | No file  | `fb8654e45d2c`  |
| 711    | No file  | `fb8654e45d2c`  |
| 707    | No file  | `fb8654e45d2c`  |
| 697    | No file  | `fb8654e45d2c`  |
| 689    | No file  | `fb8654e45d2c`  |
| 683    | No file  | `fb8654e45d2c`  |
| 678    | No file  | `fb8654e45d2c`  |
| 670    | No file  | `fb8654e45d2c`  |
| 661    | No file  | `fb8654e45d2c`  |
| 656    | No file  | `fb8654e45d2c`  |
| 652    | No file  | `fb8654e45d2c`  |
| 643    | No file  | `fb8654e45d2c`  |
| 637    | No file  | `fb8654e45d2c`  |
| 630    | No file  | `fb8654e45d2c`  |
| 627    | No file  | `fb8654e45d2c`  |
| 621    | No file  | `fb8654e45d2c`  |
| 617    | No file  | `fb8654e45d2c`  |
| 615    | No file  | `fb8654e45d2c`  |
| 606    | No file  | `fb8654e45d2c`  |
| 599    | No file  | `fb8654e45d2c`  |
| 592    | No file  | `fb8654e45d2c`  |
| 586    | No file  | `fb8654e45d2c`  |
| 577    | No file  | `fb8654e45d2c`  |
| 569    | No file  | `fb8654e45d2c`  |
| 561    | No file  | `fb8654e45d2c`  |
| 554    | No file  | `fb8654e45d2c`  |
| 542    | No file  | `fb8654e45d2c`  |
| 532    | No file  | `fb8654e45d2c`  |
| 531    | No file  | `fb8654e45d2c`  |
| 526    | No file  | `fb8654e45d2c`  |
| 521    | No file  | `fb8654e45d2c`  |
| 517    | No file  | `fb8654e45d2c`  |
| 510    | No file  | `fb8654e45d2c`  |
| 508    | No file  | `fb8654e45d2c`  |
| 504    | No file  | `fb8654e45d2c`  |
| 497    | No file  | `fb8654e45d2c`  |
| 491    | No file  | `fb8654e45d2c`  |
| 485    | No file  | `fb8654e45d2c`  |
| 478    | No file  | `fb8654e45d2c`  |
| 472    | No file  | `fb8654e45d2c`  |
| 466    | No file  | `fb8654e45d2c`  |
| 457    | No file  | `fb8654e45d2c`  |
| 452    | No file  | `fb8654e45d2c`  |
| 449    | No file  | `fb8654e45d2c`  |
| 435    | No file  | `fb8654e45d2c`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | The horse's name (LOC type 6, `str_id1` = `character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | 5 on client 3474                   |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | Present but empty                  |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; `78` |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (14 bytes)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u32  | unknown_00   | 50,000, 150,000, 300,000, 500,000, 1,000,000 (client 3474) |
| `+0x04` | u32  | unknown_04   | 45 on every row (client 3474) |
| `+0x08` | u32  | unknown_08   | 50,000, 100,000, 150,000, 200,000, 500,000 (client 3474) |
| `+0x0C` | u16  | character_id | 31560 (Traveler's Horse) on every row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | `0`        |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- Client 1784 has no such file, and the `DataSheets.bexcel` of a private
  server on that client has no sheet for it.

## Open Questions

### The Three Numbers

The rows pair a rising `unknown_00` (50,000 to 1,000,000) with a rising
`unknown_08` (50,000 to 500,000) and a constant 45 in `unknown_04`, in file
order. No client Lua reads them: the Traveler's Horse dialog only summons
and returns character 31560, and its LOC texts (`PANEL_TRAVELHORSE_*`,
`PANEL_HORSEWITHOUTOWNER_*`) name no number.
