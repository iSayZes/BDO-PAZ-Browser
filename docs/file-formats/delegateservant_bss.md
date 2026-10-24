# `delegateservant.bss` Format

## Purpose

The model character of each servant kind: entry `n` is the character key
the client returns for `CppEnums.ServantKind` `n`, `0` for a kind with
none. The Pearl Shop preview (`panel_pearlshop_displaycontroller.luac`
and `panel_ingamecashshop_setequip.luac`, client 3482) reads it with
`getIngameCashMall():getDelegateServantKey(servantType)` to pick the
character it puts a mount outfit on, and overrides it for some kinds and
products (`31025` for `Type_CashPersonalBattleShip`, `31054` up for
`Type_Carrack`, other horses for some horse products).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records  | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------- | --------- |
| 1      | 1250 and later | 3483    | `delegateservant.bss` | 80    | 32 Entry | 2         |

| Layout | File                  | Known         | Unknown    |
| ------ | --------------------- | ------------- | ---------- |
| 1      | `delegateservant.bss` | 80 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `f47d7db5e430`  |
| 3482   | Layout 1 | `f47d7db5e430`  |
| 3474   | Layout 1 | `f47d7db5e430`  |
| 3473   | Layout 1 | `f47d7db5e430`  |
| 3464   | Layout 1 | `f47d7db5e430`  |
| 3458   | Layout 1 | `f47d7db5e430`  |
| 3454   | Layout 1 | `f47d7db5e430`  |
| 3444   | Layout 1 | `f47d7db5e430`  |
| 3435   | Layout 1 | `f47d7db5e430`  |
| 3426   | Layout 1 | `f47d7db5e430`  |
| 3418   | Layout 1 | `f47d7db5e430`  |
| 3412   | Layout 1 | `f47d7db5e430`  |
| 3402   | Layout 1 | `f47d7db5e430`  |
| 3396   | Layout 1 | `f47d7db5e430`  |
| 3387   | Layout 1 | `f47d7db5e430`  |
| 3381   | Layout 1 | `f47d7db5e430`  |
| 3373   | Layout 1 | `f47d7db5e430`  |
| 3364   | Layout 1 | `f47d7db5e430`  |
| 3356   | Layout 1 | `f47d7db5e430`  |
| 3349   | Layout 1 | `f47d7db5e430`  |
| 3342   | Layout 1 | `f47d7db5e430`  |
| 3335   | Layout 1 | `f47d7db5e430`  |
| 3326   | Layout 1 | `f47d7db5e430`  |
| 3321   | Layout 1 | `f47d7db5e430`  |
| 3314   | Layout 1 | `f47d7db5e430`  |
| 3303   | Layout 1 | `f47d7db5e430`  |
| 3302   | Layout 1 | `f47d7db5e430`  |
| 3293   | Layout 1 | `f47d7db5e430`  |
| 3283   | Layout 1 | `f47d7db5e430`  |
| 3275   | Layout 1 | `f47d7db5e430`  |
| 3267   | Layout 1 | `f47d7db5e430`  |
| 3258   | Layout 1 | `f47d7db5e430`  |
| 3251   | Layout 1 | `f47d7db5e430`  |
| 3242   | Layout 1 | `f47d7db5e430`  |
| 3235   | Layout 1 | `f47d7db5e430`  |
| 3229   | Layout 1 | `f47d7db5e430`  |
| 3212   | Layout 1 | `f47d7db5e430`  |
| 3203   | Layout 1 | `f47d7db5e430`  |
| 3193   | Layout 1 | `f47d7db5e430`  |
| 3186   | Layout 1 | `f47d7db5e430`  |
| 3177   | Layout 1 | `f47d7db5e430`  |
| 3169   | Layout 1 | `f47d7db5e430`  |
| 3158   | Layout 1 | `f47d7db5e430`  |
| 3151   | Layout 1 | `f47d7db5e430`  |
| 3144   | Layout 1 | `f47d7db5e430`  |
| 3133   | Layout 1 | `f47d7db5e430`  |
| 3125   | Layout 1 | `f47d7db5e430`  |
| 3118   | Layout 1 | `f47d7db5e430`  |
| 3111   | Layout 1 | `f47d7db5e430`  |
| 3103   | Layout 1 | `f47d7db5e430`  |
| 3095   | Layout 1 | `f47d7db5e430`  |
| 3086   | Layout 1 | `f47d7db5e430`  |
| 3072   | Layout 1 | `f47d7db5e430`  |
| 3062   | Layout 1 | `f47d7db5e430`  |
| 3052   | Layout 1 | `f47d7db5e430`  |
| 3045   | Layout 1 | `f47d7db5e430`  |
| 3037   | Layout 1 | `f47d7db5e430`  |
| 3030   | Layout 1 | `f47d7db5e430`  |
| 3021   | Layout 1 | `f47d7db5e430`  |
| 3012   | Layout 1 | `f47d7db5e430`  |
| 3002   | Layout 1 | `f47d7db5e430`  |
| 2995   | Layout 1 | `f47d7db5e430`  |
| 2987   | Layout 1 | `f47d7db5e430`  |
| 2978   | Layout 1 | `f47d7db5e430`  |
| 2970   | Layout 1 | `f47d7db5e430`  |
| 2959   | Layout 1 | `f47d7db5e430`  |
| 2951   | Layout 1 | `f47d7db5e430`  |
| 2942   | Layout 1 | `f47d7db5e430`  |
| 2935   | Layout 1 | `f47d7db5e430`  |
| 2932   | Layout 1 | `f47d7db5e430`  |
| 2923   | Layout 1 | `f47d7db5e430`  |
| 2919   | Layout 1 | `f47d7db5e430`  |
| 2907   | Layout 1 | `f47d7db5e430`  |
| 2900   | Layout 1 | `f47d7db5e430`  |
| 2891   | Layout 1 | `f47d7db5e430`  |
| 2882   | Layout 1 | `f47d7db5e430`  |
| 2872   | Layout 1 | `f47d7db5e430`  |
| 2863   | Layout 1 | `f47d7db5e430`  |
| 2855   | Layout 1 | `f47d7db5e430`  |
| 2849   | Layout 1 | `f47d7db5e430`  |
| 2844   | Layout 1 | `f47d7db5e430`  |
| 2834   | Layout 1 | `f47d7db5e430`  |
| 2825   | Layout 1 | `f47d7db5e430`  |
| 2819   | Layout 1 | `f47d7db5e430`  |
| 2811   | Layout 1 | `f47d7db5e430`  |
| 2803   | Layout 1 | `f47d7db5e430`  |
| 2794   | Layout 1 | `f47d7db5e430`  |
| 2783   | Layout 1 | `f47d7db5e430`  |
| 2774   | Layout 1 | `f47d7db5e430`  |
| 2765   | Layout 1 | `f47d7db5e430`  |
| 2756   | Layout 1 | `f47d7db5e430`  |
| 2750   | Layout 1 | `f47d7db5e430`  |
| 2743   | Layout 1 | `f47d7db5e430`  |
| 2736   | Layout 1 | `f47d7db5e430`  |
| 2726   | Layout 1 | `f47d7db5e430`  |
| 2717   | Layout 1 | `f47d7db5e430`  |
| 2709   | Layout 1 | `f47d7db5e430`  |
| 2703   | Layout 1 | `f47d7db5e430`  |
| 2695   | Layout 1 | `f47d7db5e430`  |
| 2684   | Layout 1 | `f47d7db5e430`  |
| 2672   | Layout 1 | `f47d7db5e430`  |
| 2665   | Layout 1 | `f47d7db5e430`  |
| 2657   | Layout 1 | `f47d7db5e430`  |
| 2649   | Layout 1 | `f47d7db5e430`  |
| 2644   | Layout 1 | `f47d7db5e430`  |
| 2637   | Layout 1 | `f47d7db5e430`  |
| 2629   | Layout 1 | `f47d7db5e430`  |
| 2619   | Layout 1 | `f47d7db5e430`  |
| 2612   | Layout 1 | `f47d7db5e430`  |
| 2606   | Layout 1 | `f47d7db5e430`  |
| 2602   | Layout 1 | `f47d7db5e430`  |
| 2601   | Layout 1 | `f47d7db5e430`  |
| 2592   | Layout 1 | `f47d7db5e430`  |
| 2583   | Layout 1 | `f47d7db5e430`  |
| 2575   | Layout 1 | `f47d7db5e430`  |
| 2567   | Layout 1 | `f47d7db5e430`  |
| 2560   | Layout 1 | `f47d7db5e430`  |
| 2553   | Layout 1 | `f47d7db5e430`  |
| 2545   | Layout 1 | `f47d7db5e430`  |
| 2538   | Layout 1 | `f47d7db5e430`  |
| 2529   | Layout 1 | `f47d7db5e430`  |
| 2519   | Layout 1 | `f47d7db5e430`  |
| 2513   | Layout 1 | `f47d7db5e430`  |
| 2510   | Layout 1 | `f47d7db5e430`  |
| 2507   | Layout 1 | `f47d7db5e430`  |
| 2503   | Layout 1 | `f47d7db5e430`  |
| 2498   | Layout 1 | `f47d7db5e430`  |
| 2492   | Layout 1 | `f47d7db5e430`  |
| 2487   | Layout 1 | `f47d7db5e430`  |
| 2480   | Layout 1 | `f47d7db5e430`  |
| 2474   | Layout 1 | `f47d7db5e430`  |
| 2468   | Layout 1 | `f47d7db5e430`  |
| 2460   | Layout 1 | `f47d7db5e430`  |
| 2453   | Layout 1 | `f47d7db5e430`  |
| 2444   | Layout 1 | `f47d7db5e430`  |
| 2438   | Layout 1 | `f47d7db5e430`  |
| 2434   | Layout 1 | `f47d7db5e430`  |
| 2429   | Layout 1 | `f47d7db5e430`  |
| 2421   | Layout 1 | `f47d7db5e430`  |
| 2414   | Layout 1 | `f47d7db5e430`  |
| 2407   | Layout 1 | `f47d7db5e430`  |
| 2401   | Layout 1 | `f47d7db5e430`  |
| 2397   | Layout 1 | `f47d7db5e430`  |
| 2393   | Layout 1 | `f47d7db5e430`  |
| 2384   | Layout 1 | `f47d7db5e430`  |
| 2378   | Layout 1 | `f47d7db5e430`  |
| 2372   | Layout 1 | `f47d7db5e430`  |
| 2358   | Layout 1 | `f47d7db5e430`  |
| 2352   | Layout 1 | `f47d7db5e430`  |
| 2347   | Layout 1 | `f47d7db5e430`  |
| 2343   | Layout 1 | `f47d7db5e430`  |
| 2335   | Layout 1 | `f47d7db5e430`  |
| 2327   | Layout 1 | `f47d7db5e430`  |
| 2324   | Layout 1 | `f47d7db5e430`  |
| 2319   | Layout 1 | `f47d7db5e430`  |
| 2313   | Layout 1 | `f47d7db5e430`  |
| 2308   | Layout 1 | `f47d7db5e430`  |
| 2302   | Layout 1 | `f47d7db5e430`  |
| 2295   | Layout 1 | `f47d7db5e430`  |
| 2290   | Layout 1 | `f47d7db5e430`  |
| 2284   | Layout 1 | `f47d7db5e430`  |
| 2276   | Layout 1 | `f47d7db5e430`  |
| 2269   | Layout 1 | `f47d7db5e430`  |
| 2259   | Layout 1 | `f47d7db5e430`  |
| 2250   | Layout 1 | `f47d7db5e430`  |
| 2243   | Layout 1 | `f47d7db5e430`  |
| 2235   | Layout 1 | `f47d7db5e430`  |
| 2229   | Layout 1 | `f47d7db5e430`  |
| 2224   | Layout 1 | `f47d7db5e430`  |
| 2218   | Layout 1 | `f47d7db5e430`  |
| 2215   | Layout 1 | `f47d7db5e430`  |
| 2207   | Layout 1 | `f47d7db5e430`  |
| 2203   | Layout 1 | `f47d7db5e430`  |
| 2196   | Layout 1 | `f47d7db5e430`  |
| 2192   | Layout 1 | `f47d7db5e430`  |
| 2189   | Layout 1 | `f47d7db5e430`  |
| 2183   | Layout 1 | `f47d7db5e430`  |
| 2179   | Layout 1 | `f47d7db5e430`  |
| 2171   | Layout 1 | `f47d7db5e430`  |
| 2163   | Layout 1 | `f47d7db5e430`  |
| 2156   | Layout 1 | `f47d7db5e430`  |
| 2151   | Layout 1 | `f47d7db5e430`  |
| 2147   | Layout 1 | `f47d7db5e430`  |
| 2142   | Layout 1 | `f47d7db5e430`  |
| 2138   | Layout 1 | `f47d7db5e430`  |
| 2134   | Layout 1 | `f47d7db5e430`  |
| 2130   | Layout 1 | `f47d7db5e430`  |
| 2122   | Layout 1 | `f47d7db5e430`  |
| 2107   | Layout 1 | `f47d7db5e430`  |
| 2098   | Layout 1 | `f47d7db5e430`  |
| 2089   | Layout 1 | `f47d7db5e430`  |
| 2081   | Layout 1 | `f47d7db5e430`  |
| 2073   | Layout 1 | `f47d7db5e430`  |
| 2067   | Layout 1 | `f47d7db5e430`  |
| 2063   | Layout 1 | `f47d7db5e430`  |
| 2059   | Layout 1 | `f47d7db5e430`  |
| 2052   | Layout 1 | `f47d7db5e430`  |
| 2044   | Layout 1 | `f47d7db5e430`  |
| 2039   | Layout 1 | `f47d7db5e430`  |
| 2032   | Layout 1 | `f47d7db5e430`  |
| 2025   | Layout 1 | `f47d7db5e430`  |
| 2011   | Layout 1 | `f47d7db5e430`  |
| 2005   | Layout 1 | `f47d7db5e430`  |
| 2000   | Layout 1 | `f47d7db5e430`  |
| 1996   | Layout 1 | `f47d7db5e430`  |
| 1991   | Layout 1 | `f47d7db5e430`  |
| 1985   | Layout 1 | `f47d7db5e430`  |
| 1980   | Layout 1 | `f47d7db5e430`  |
| 1969   | Layout 1 | `f47d7db5e430`  |
| 1964   | Layout 1 | `f47d7db5e430`  |
| 1958   | Layout 1 | `f47d7db5e430`  |
| 1950   | Layout 1 | `f47d7db5e430`  |
| 1945   | Layout 1 | `f47d7db5e430`  |
| 1937   | Layout 1 | `f47d7db5e430`  |
| 1933   | Layout 1 | `f47d7db5e430`  |
| 1927   | Layout 1 | `f47d7db5e430`  |
| 1921   | Layout 1 | `f47d7db5e430`  |
| 1914   | Layout 1 | `f47d7db5e430`  |
| 1908   | Layout 1 | `f47d7db5e430`  |
| 1897   | Layout 1 | `f47d7db5e430`  |
| 1892   | Layout 1 | `f47d7db5e430`  |
| 1886   | Layout 1 | `f47d7db5e430`  |
| 1881   | Layout 1 | `f47d7db5e430`  |
| 1871   | Layout 1 | `f47d7db5e430`  |
| 1866   | Layout 1 | `f47d7db5e430`  |
| 1862   | Layout 1 | `f47d7db5e430`  |
| 1854   | Layout 1 | `f47d7db5e430`  |
| 1846   | Layout 1 | `f47d7db5e430`  |
| 1838   | Layout 1 | `f47d7db5e430`  |
| 1832   | Layout 1 | `f47d7db5e430`  |
| 1826   | Layout 1 | `f47d7db5e430`  |
| 1822   | Layout 1 | `f47d7db5e430`  |
| 1818   | Layout 1 | `f47d7db5e430`  |
| 1804   | Layout 1 | `f47d7db5e430`  |
| 1794   | Layout 1 | `f47d7db5e430`  |
| 1790   | Layout 1 | `f47d7db5e430`  |
| 1784   | Layout 1 | `f47d7db5e430`  |
| 1774   | Layout 1 | `f47d7db5e430`  |
| 1771   | Layout 1 | `f47d7db5e430`  |
| 1762   | Layout 1 | `f47d7db5e430`  |
| 1759   | Layout 1 | `f47d7db5e430`  |
| 1754   | Layout 1 | `f47d7db5e430`  |
| 1749   | Layout 1 | `f47d7db5e430`  |
| 1743   | Layout 1 | `f47d7db5e430`  |
| 1737   | Layout 1 | `f47d7db5e430`  |
| 1731   | Layout 1 | `f47d7db5e430`  |
| 1725   | Layout 1 | `f47d7db5e430`  |
| 1717   | Layout 1 | `f47d7db5e430`  |
| 1710   | Layout 1 | `f47d7db5e430`  |
| 1704   | Layout 1 | `f47d7db5e430`  |
| 1698   | Layout 1 | `f47d7db5e430`  |
| 1690   | Layout 1 | `f47d7db5e430`  |
| 1685   | Layout 1 | `f47d7db5e430`  |
| 1680   | Layout 1 | `f47d7db5e430`  |
| 1674   | Layout 1 | `f47d7db5e430`  |
| 1668   | Layout 1 | `f47d7db5e430`  |
| 1659   | Layout 1 | `f47d7db5e430`  |
| 1649   | Layout 1 | `f47d7db5e430`  |
| 1642   | Layout 1 | `f47d7db5e430`  |
| 1636   | Layout 1 | `f47d7db5e430`  |
| 1628   | Layout 1 | `f47d7db5e430`  |
| 1622   | Layout 1 | `f47d7db5e430`  |
| 1614   | Layout 1 | `f47d7db5e430`  |
| 1608   | Layout 1 | `f47d7db5e430`  |
| 1602   | Layout 1 | `f47d7db5e430`  |
| 1598   | Layout 1 | `f47d7db5e430`  |
| 1594   | Layout 1 | `f47d7db5e430`  |
| 1590   | Layout 1 | `f47d7db5e430`  |
| 1587   | Layout 1 | `f47d7db5e430`  |
| 1584   | Layout 1 | `f47d7db5e430`  |
| 1579   | Layout 1 | `f47d7db5e430`  |
| 1572   | Layout 1 | `f47d7db5e430`  |
| 1565   | Layout 1 | `f47d7db5e430`  |
| 1559   | Layout 1 | `f47d7db5e430`  |
| 1554   | Layout 1 | `f47d7db5e430`  |
| 1547   | Layout 1 | `f47d7db5e430`  |
| 1537   | Layout 1 | `f47d7db5e430`  |
| 1529   | Layout 1 | `f47d7db5e430`  |
| 1524   | Layout 1 | `f47d7db5e430`  |
| 1519   | Layout 1 | `f47d7db5e430`  |
| 1509   | Layout 1 | `f47d7db5e430`  |
| 1506   | Layout 1 | `f47d7db5e430`  |
| 1504   | Layout 1 | `f47d7db5e430`  |
| 1500   | Layout 1 | `f47d7db5e430`  |
| 1493   | Layout 1 | `f47d7db5e430`  |
| 1489   | Layout 1 | `f47d7db5e430`  |
| 1485   | Layout 1 | `f47d7db5e430`  |
| 1481   | Layout 1 | `f47d7db5e430`  |
| 1474   | Layout 1 | `f47d7db5e430`  |
| 1466   | Layout 1 | `f47d7db5e430`  |
| 1462   | Layout 1 | `f47d7db5e430`  |
| 1459   | Layout 1 | `f47d7db5e430`  |
| 1453   | Layout 1 | `f47d7db5e430`  |
| 1450   | Layout 1 | `f47d7db5e430`  |
| 1445   | Layout 1 | `f47d7db5e430`  |
| 1439   | Layout 1 | `f47d7db5e430`  |
| 1433   | Layout 1 | `f47d7db5e430`  |
| 1430   | Layout 1 | `f47d7db5e430`  |
| 1426   | Layout 1 | `f47d7db5e430`  |
| 1421   | Layout 1 | `f47d7db5e430`  |
| 1417   | Layout 1 | `f47d7db5e430`  |
| 1416   | Layout 1 | `f47d7db5e430`  |
| 1409   | Layout 1 | `f47d7db5e430`  |
| 1405   | Layout 1 | `f47d7db5e430`  |
| 1401   | Layout 1 | `f47d7db5e430`  |
| 1396   | Layout 1 | `f47d7db5e430`  |
| 1391   | Layout 1 | `f47d7db5e430`  |
| 1390   | Layout 1 | `f47d7db5e430`  |
| 1386   | Layout 1 | `f47d7db5e430`  |
| 1381   | Layout 1 | `f47d7db5e430`  |
| 1379   | Layout 1 | `f47d7db5e430`  |
| 1372   | Layout 1 | `f47d7db5e430`  |
| 1366   | Layout 1 | `f47d7db5e430`  |
| 1364   | Layout 1 | `f47d7db5e430`  |
| 1363   | Layout 1 | `f47d7db5e430`  |
| 1360   | Layout 1 | `f47d7db5e430`  |
| 1358   | Layout 1 | `f47d7db5e430`  |
| 1355   | Layout 1 | `f47d7db5e430`  |
| 1351   | Layout 1 | `f47d7db5e430`  |
| 1348   | Layout 1 | `f47d7db5e430`  |
| 1346   | Layout 1 | `f47d7db5e430`  |
| 1341   | Layout 1 | `f47d7db5e430`  |
| 1340   | Layout 1 | `f47d7db5e430`  |
| 1338   | Layout 1 | `f47d7db5e430`  |
| 1335   | Layout 1 | `f47d7db5e430`  |
| 1333   | Layout 1 | `f47d7db5e430`  |
| 1329   | Layout 1 | `f47d7db5e430`  |
| 1327   | Layout 1 | `f47d7db5e430`  |
| 1324   | Layout 1 | `f47d7db5e430`  |
| 1321   | Layout 1 | `f47d7db5e430`  |
| 1319   | Layout 1 | `f47d7db5e430`  |
| 1318   | Layout 1 | `f47d7db5e430`  |
| 1316   | Layout 1 | `f47d7db5e430`  |
| 1313   | Layout 1 | `f47d7db5e430`  |
| 1311   | Layout 1 | `f47d7db5e430`  |
| 1309   | Layout 1 | `f47d7db5e430`  |
| 1304   | Layout 1 | `f47d7db5e430`  |
| 1292   | Layout 1 | `f47d7db5e430`  |
| 1286   | Layout 1 | `f47d7db5e430`  |
| 1280   | Layout 1 | `f47d7db5e430`  |
| 1276   | Layout 1 | `f47d7db5e430`  |
| 1267   | Layout 1 | `f47d7db5e430`  |
| 1261   | Layout 1 | `f47d7db5e430`  |
| 1256   | Layout 1 | `f47d7db5e430`  |
| 1250   | Layout 1 | `f47d7db5e430`  |
| 1246   | No file  | `f47d7db5e430`  |
| 1239   | No file  | `f47d7db5e430`  |
| 1230   | No file  | `f47d7db5e430`  |
| 1226   | No file  | `f47d7db5e430`  |
| 1220   | No file  | `f47d7db5e430`  |
| 1217   | No file  | `f47d7db5e430`  |
| 1211   | No file  | `f47d7db5e430`  |
| 1210   | No file  | `f47d7db5e430`  |
| 1208   | No file  | `f47d7db5e430`  |
| 1203   | No file  | `f47d7db5e430`  |
| 1197   | No file  | `f47d7db5e430`  |
| 1194   | No file  | `f47d7db5e430`  |
| 1192   | No file  | `f47d7db5e430`  |
| 1187   | No file  | `f47d7db5e430`  |
| 1183   | No file  | `f47d7db5e430`  |
| 1177   | No file  | `f47d7db5e430`  |
| 1173   | No file  | `f47d7db5e430`  |
| 1167   | No file  | `f47d7db5e430`  |
| 1164   | No file  | `f47d7db5e430`  |
| 1156   | No file  | `f47d7db5e430`  |
| 1149   | No file  | `f47d7db5e430`  |
| 1144   | No file  | `f47d7db5e430`  |
| 1137   | No file  | `f47d7db5e430`  |
| 1132   | No file  | `f47d7db5e430`  |
| 1127   | No file  | `f47d7db5e430`  |
| 1122   | No file  | `f47d7db5e430`  |
| 1118   | No file  | `f47d7db5e430`  |
| 1114   | No file  | `f47d7db5e430`  |
| 1109   | No file  | `f47d7db5e430`  |
| 1102   | No file  | `f47d7db5e430`  |
| 1096   | No file  | `f47d7db5e430`  |
| 1088   | No file  | `f47d7db5e430`  |
| 1081   | No file  | `f47d7db5e430`  |
| 1076   | No file  | `f47d7db5e430`  |
| 1069   | No file  | `f47d7db5e430`  |
| 1064   | No file  | `f47d7db5e430`  |
| 1058   | No file  | `f47d7db5e430`  |
| 1051   | No file  | `f47d7db5e430`  |
| 1044   | No file  | `f47d7db5e430`  |
| 1036   | No file  | `f47d7db5e430`  |
| 1026   | No file  | `f47d7db5e430`  |
| 1016   | No file  | `f47d7db5e430`  |
| 1009   | No file  | `f47d7db5e430`  |
| 1005   | No file  | `f47d7db5e430`  |
| 1000   | No file  | `f47d7db5e430`  |
| 998    | No file  | `f47d7db5e430`  |
| 990    | No file  | `f47d7db5e430`  |
| 979    | No file  | `f47d7db5e430`  |
| 972    | No file  | `f47d7db5e430`  |
| 963    | No file  | `f47d7db5e430`  |
| 955    | No file  | `f47d7db5e430`  |
| 946    | No file  | `f47d7db5e430`  |
| 938    | No file  | `f47d7db5e430`  |
| 927    | No file  | `f47d7db5e430`  |
| 911    | No file  | `f47d7db5e430`  |
| 904    | No file  | `f47d7db5e430`  |
| 899    | No file  | `f47d7db5e430`  |
| 894    | No file  | `f47d7db5e430`  |
| 885    | No file  | `f47d7db5e430`  |
| 879    | No file  | `f47d7db5e430`  |
| 872    | No file  | `f47d7db5e430`  |
| 864    | No file  | `f47d7db5e430`  |
| 855    | No file  | `f47d7db5e430`  |
| 853    | No file  | `f47d7db5e430`  |
| 845    | No file  | `f47d7db5e430`  |
| 837    | No file  | `f47d7db5e430`  |
| 829    | No file  | `f47d7db5e430`  |
| 822    | No file  | `f47d7db5e430`  |
| 814    | No file  | `f47d7db5e430`  |
| 805    | No file  | `f47d7db5e430`  |
| 794    | No file  | `f47d7db5e430`  |
| 787    | No file  | `f47d7db5e430`  |
| 780    | No file  | `f47d7db5e430`  |
| 771    | No file  | `f47d7db5e430`  |
| 760    | No file  | `f47d7db5e430`  |
| 748    | No file  | `f47d7db5e430`  |
| 741    | No file  | `f47d7db5e430`  |
| 736    | No file  | `f47d7db5e430`  |
| 731    | No file  | `f47d7db5e430`  |
| 723    | No file  | `f47d7db5e430`  |
| 711    | No file  | `f47d7db5e430`  |
| 707    | No file  | `f47d7db5e430`  |
| 697    | No file  | `f47d7db5e430`  |
| 689    | No file  | `f47d7db5e430`  |
| 683    | No file  | `f47d7db5e430`  |
| 678    | No file  | `f47d7db5e430`  |
| 670    | No file  | `f47d7db5e430`  |
| 661    | No file  | `f47d7db5e430`  |
| 656    | No file  | `f47d7db5e430`  |
| 652    | No file  | `f47d7db5e430`  |
| 643    | No file  | `f47d7db5e430`  |
| 637    | No file  | `f47d7db5e430`  |
| 630    | No file  | `f47d7db5e430`  |
| 627    | No file  | `f47d7db5e430`  |
| 621    | No file  | `f47d7db5e430`  |
| 617    | No file  | `f47d7db5e430`  |
| 615    | No file  | `f47d7db5e430`  |
| 606    | No file  | `f47d7db5e430`  |
| 599    | No file  | `f47d7db5e430`  |
| 592    | No file  | `f47d7db5e430`  |
| 586    | No file  | `f47d7db5e430`  |
| 577    | No file  | `f47d7db5e430`  |
| 569    | No file  | `f47d7db5e430`  |
| 561    | No file  | `f47d7db5e430`  |
| 554    | No file  | `f47d7db5e430`  |
| 542    | No file  | `f47d7db5e430`  |
| 532    | No file  | `f47d7db5e430`  |
| 531    | No file  | `f47d7db5e430`  |
| 526    | No file  | `f47d7db5e430`  |
| 521    | No file  | `f47d7db5e430`  |
| 517    | No file  | `f47d7db5e430`  |
| 510    | No file  | `f47d7db5e430`  |
| 508    | No file  | `f47d7db5e430`  |
| 504    | No file  | `f47d7db5e430`  |
| 497    | No file  | `f47d7db5e430`  |
| 491    | No file  | `f47d7db5e430`  |
| 485    | No file  | `f47d7db5e430`  |
| 478    | No file  | `f47d7db5e430`  |
| 472    | No file  | `f47d7db5e430`  |
| 466    | No file  | `f47d7db5e430`  |
| 457    | No file  | `f47d7db5e430`  |
| 452    | No file  | `f47d7db5e430`  |
| 449    | No file  | `f47d7db5e430`  |
| 435    | No file  | `f47d7db5e430`  |

<!-- versions:end -->

## Companion Files

None. The handler names each character with LOC type 6 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset         | Type                 | Field        | Notes                                             |
| -------------- | -------------------- | ------------ | ------------------------------------------------- |
| `+0x00`        | char[4]              | magic        | ASCII `PABR`                                      |
| `+0x04`        | Entry[..table_start] | entries      | No count: entry `n` is `CppEnums.ServantKind` `n` |
| `entries+0x00` | String Table         | string_table | See String Table                                  |
| `EOF-0x08`     | u32                  | table_start  | Offset of the string table, where `entries` ends  |
| `EOF-0x04`     | u32                  | zero         | Always `0`                                        |

The parser takes the entry count from the trailer: `(table_start - 4) / 2`.

### Entry (2 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16  | character_key | Model character of the servant kind; `0` for none        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Servant Kinds

The entry count follows `CppEnums.ServantKind`: 32 entries on client 3482,
whose `global_define_cpp_enum.luac` ends the enum with `Type_Count = 32`,
and 31 on client 1784. The entries with a character on client 3482, with
their LOC type 6 names:

| Entry | `CppEnums.ServantKind`       | `character_key`                   |
| ----- | ---------------------------- | --------------------------------- |
| 0     | `Type_Horse`                 | `9909` Horse                      |
| 1     | `Type_Camel`                 | `9010` Brown Camel                |
| 2     | `Type_Donkey`                | `9113` Donkey                     |
| 5     | `Type_FourWheeledCarriage`   | `9052` Merchant Wagon             |
| 6     | `Type_Ship`                  | `9032` Rowboat                    |
| 11    | `Type_FishingBoat`           | `9065` Fishing Boat               |
| 15    | `Type_PersonalTradeShip`     | `31001` Epheria Sailboat          |
| 23    | `Type_Carrack`               | `31054` Epheria Carrack: Advance  |

Client 1784 has the same entries without `23`.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has
`Delegate` in its name. `character_key` follows the getter: the Lua passes
a servant kind to `getDelegateServantKey` and uses the result as
`characterKeyRaw`, and every non-zero entry is the LOC type 6 character
of that kind.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/servant_tables.py`: one
  row per servant kind with its enum name (`23 Carrack`), the character
  key and its LOC name.
