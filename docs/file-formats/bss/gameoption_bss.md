# `gameoption.bss` Format

## Purpose

The client's copy of the game option values in one PABR record. The record
holds the one-row option sheets one after another, each in its loader's read
order: the `BattleOption` columns in the head, then, after twelve arrays of
1000 values, the `ServantOption`, `MovementVerifyOption` and `EtcOption`
runs, later the `GuildOption` and `ItemMarket` runs, part of the
`LocalizingOption` run and the `EtcOption` and `BattleOption` arena values
near the end. The bytes between these runs are unknown runs (see Runs Past
the Head and Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes   | Records                                                    | Row bytes |
| ------ | -------------- | ---------------- | ------- | ---------------------------------------------------------- | --------- |
| 6      | 3464 and later | `gameoption.bss` | 123,989 | 12 Int Float Pair, 18 Byte Int Pair                        | 5         |
| 5      | 3435 to 3454   | `gameoption.bss` | 124,109 | 1 Servant Option, 1 Movement Verify Option, 1 String Table | 430       |
| 4      | 3002           | `gameoption.bss` | 241,041 | 1 Servant Option, 1 Movement Verify Option, 1 String Table | 430       |
| 3      | 2736           | `gameoption.bss` | 343,627 | 1 Servant Option, 1 Movement Verify Option, 1 String Table | 434       |
| 2      | 2414           | `gameoption.bss` | 340,961 | 1 Servant Option, 1 Movement Verify Option, 1 String Table | 434       |
| 1      | 1784           | `gameoption.bss` | 329,469 | 1 Servant Option, 1 Movement Verify Option, 1 String Table | 426       |

| Layout | File             | Known            | Unknown           |
| ------ | ---------------- | ---------------- | ----------------- |
| 6      | `gameoption.bss` | 3,590 B (2.9%)   | 120,399 B (97.1%) |
| 5      | `gameoption.bss` | 2,176 B (1.8%)   | 121,933 B (98.2%) |
| 4      | `gameoption.bss` | 31,689 B (13.1%) | 209,352 B (86.9%) |
| 3      | `gameoption.bss` | 25,905 B (7.5%)  | 317,722 B (92.5%) |
| 2      | `gameoption.bss` | 24,558 B (7.2%)  | 316,403 B (92.8%) |
| 1      | `gameoption.bss` | 20,493 B (6.2%)  | 308,976 B (93.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 6             | `1d96a417b5bf`  |
| 3482   | Layout 6             | `1d96a417b5bf`  |
| 3474   | Layout 6             | `1d96a417b5bf`  |
| 3473   | Layout 6             | `1d96a417b5bf`  |
| 3464   | Layout 6             | `1d96a417b5bf`  |
| 3458   | No documented layout | `1d96a417b5bf`  |
| 3454   | Layout 5             | `1d96a417b5bf`  |
| 3444   | Layout 5             | `1d96a417b5bf`  |
| 3435   | Layout 5             | `1d96a417b5bf`  |
| 3426   | No documented layout | `1d96a417b5bf`  |
| 3418   | No documented layout | `1d96a417b5bf`  |
| 3412   | No documented layout | `1d96a417b5bf`  |
| 3402   | No documented layout | `1d96a417b5bf`  |
| 3396   | No documented layout | `1d96a417b5bf`  |
| 3387   | No documented layout | `1d96a417b5bf`  |
| 3381   | No documented layout | `1d96a417b5bf`  |
| 3373   | No documented layout | `1d96a417b5bf`  |
| 3364   | No documented layout | `1d96a417b5bf`  |
| 3356   | No documented layout | `1d96a417b5bf`  |
| 3349   | No documented layout | `1d96a417b5bf`  |
| 3342   | No documented layout | `1d96a417b5bf`  |
| 3335   | No documented layout | `1d96a417b5bf`  |
| 3326   | No documented layout | `1d96a417b5bf`  |
| 3321   | No documented layout | `1d96a417b5bf`  |
| 3314   | No documented layout | `1d96a417b5bf`  |
| 3303   | No documented layout | `1d96a417b5bf`  |
| 3302   | No documented layout | `1d96a417b5bf`  |
| 3293   | No documented layout | `1d96a417b5bf`  |
| 3283   | No documented layout | `1d96a417b5bf`  |
| 3275   | No documented layout | `1d96a417b5bf`  |
| 3267   | No documented layout | `1d96a417b5bf`  |
| 3258   | No documented layout | `1d96a417b5bf`  |
| 3251   | No documented layout | `1d96a417b5bf`  |
| 3242   | No documented layout | `1d96a417b5bf`  |
| 3235   | No documented layout | `1d96a417b5bf`  |
| 3229   | No documented layout | `1d96a417b5bf`  |
| 3212   | No documented layout | `1d96a417b5bf`  |
| 3203   | No documented layout | `1d96a417b5bf`  |
| 3193   | No documented layout | `1d96a417b5bf`  |
| 3186   | No documented layout | `1d96a417b5bf`  |
| 3177   | No documented layout | `1d96a417b5bf`  |
| 3169   | No documented layout | `1d96a417b5bf`  |
| 3158   | No documented layout | `1d96a417b5bf`  |
| 3151   | No documented layout | `1d96a417b5bf`  |
| 3144   | No documented layout | `1d96a417b5bf`  |
| 3133   | No documented layout | `1d96a417b5bf`  |
| 3125   | No documented layout | `1d96a417b5bf`  |
| 3118   | No documented layout | `1d96a417b5bf`  |
| 3111   | No documented layout | `1d96a417b5bf`  |
| 3103   | No documented layout | `1d96a417b5bf`  |
| 3095   | No documented layout | `1d96a417b5bf`  |
| 3086   | No documented layout | `1d96a417b5bf`  |
| 3072   | No documented layout | `1d96a417b5bf`  |
| 3062   | No documented layout | `1d96a417b5bf`  |
| 3052   | No documented layout | `1d96a417b5bf`  |
| 3045   | No documented layout | `1d96a417b5bf`  |
| 3037   | No documented layout | `1d96a417b5bf`  |
| 3030   | No documented layout | `1d96a417b5bf`  |
| 3021   | No documented layout | `1d96a417b5bf`  |
| 3012   | No documented layout | `1d96a417b5bf`  |
| 3002   | Layout 4             | `1d96a417b5bf`  |
| 2995   | No documented layout | `1d96a417b5bf`  |
| 2987   | No documented layout | `1d96a417b5bf`  |
| 2978   | No documented layout | `1d96a417b5bf`  |
| 2970   | No documented layout | `1d96a417b5bf`  |
| 2959   | No documented layout | `1d96a417b5bf`  |
| 2951   | No documented layout | `1d96a417b5bf`  |
| 2942   | No documented layout | `1d96a417b5bf`  |
| 2935   | No documented layout | `1d96a417b5bf`  |
| 2932   | No documented layout | `1d96a417b5bf`  |
| 2923   | No documented layout | `1d96a417b5bf`  |
| 2919   | No documented layout | `1d96a417b5bf`  |
| 2907   | No documented layout | `1d96a417b5bf`  |
| 2900   | No documented layout | `1d96a417b5bf`  |
| 2891   | No documented layout | `1d96a417b5bf`  |
| 2882   | No documented layout | `1d96a417b5bf`  |
| 2872   | No documented layout | `1d96a417b5bf`  |
| 2863   | No documented layout | `1d96a417b5bf`  |
| 2855   | No documented layout | `1d96a417b5bf`  |
| 2849   | No documented layout | `1d96a417b5bf`  |
| 2844   | No documented layout | `1d96a417b5bf`  |
| 2834   | No documented layout | `1d96a417b5bf`  |
| 2825   | No documented layout | `1d96a417b5bf`  |
| 2819   | No documented layout | `1d96a417b5bf`  |
| 2811   | No documented layout | `1d96a417b5bf`  |
| 2803   | No documented layout | `1d96a417b5bf`  |
| 2794   | No documented layout | `1d96a417b5bf`  |
| 2783   | No documented layout | `1d96a417b5bf`  |
| 2774   | No documented layout | `1d96a417b5bf`  |
| 2765   | No documented layout | `1d96a417b5bf`  |
| 2756   | No documented layout | `1d96a417b5bf`  |
| 2750   | No documented layout | `1d96a417b5bf`  |
| 2743   | No documented layout | `1d96a417b5bf`  |
| 2736   | Layout 3             | `1d96a417b5bf`  |
| 2726   | No documented layout | `1d96a417b5bf`  |
| 2717   | No documented layout | `1d96a417b5bf`  |
| 2709   | No documented layout | `1d96a417b5bf`  |
| 2703   | No documented layout | `1d96a417b5bf`  |
| 2695   | No documented layout | `1d96a417b5bf`  |
| 2684   | No documented layout | `1d96a417b5bf`  |
| 2672   | No documented layout | `1d96a417b5bf`  |
| 2665   | No documented layout | `1d96a417b5bf`  |
| 2657   | No documented layout | `1d96a417b5bf`  |
| 2649   | No documented layout | `1d96a417b5bf`  |
| 2644   | No documented layout | `1d96a417b5bf`  |
| 2637   | No documented layout | `1d96a417b5bf`  |
| 2629   | No documented layout | `1d96a417b5bf`  |
| 2619   | No documented layout | `1d96a417b5bf`  |
| 2612   | No documented layout | `1d96a417b5bf`  |
| 2606   | No documented layout | `1d96a417b5bf`  |
| 2602   | No documented layout | `1d96a417b5bf`  |
| 2601   | No documented layout | `1d96a417b5bf`  |
| 2592   | No documented layout | `1d96a417b5bf`  |
| 2583   | No documented layout | `1d96a417b5bf`  |
| 2575   | No documented layout | `1d96a417b5bf`  |
| 2567   | No documented layout | `1d96a417b5bf`  |
| 2560   | No documented layout | `1d96a417b5bf`  |
| 2553   | No documented layout | `1d96a417b5bf`  |
| 2545   | No documented layout | `1d96a417b5bf`  |
| 2538   | No documented layout | `1d96a417b5bf`  |
| 2529   | No documented layout | `1d96a417b5bf`  |
| 2519   | No documented layout | `1d96a417b5bf`  |
| 2513   | No documented layout | `1d96a417b5bf`  |
| 2510   | No documented layout | `1d96a417b5bf`  |
| 2507   | No documented layout | `1d96a417b5bf`  |
| 2503   | No documented layout | `1d96a417b5bf`  |
| 2498   | No documented layout | `1d96a417b5bf`  |
| 2492   | No documented layout | `1d96a417b5bf`  |
| 2487   | No documented layout | `1d96a417b5bf`  |
| 2480   | No documented layout | `1d96a417b5bf`  |
| 2474   | No documented layout | `1d96a417b5bf`  |
| 2468   | No documented layout | `1d96a417b5bf`  |
| 2460   | No documented layout | `1d96a417b5bf`  |
| 2453   | No documented layout | `1d96a417b5bf`  |
| 2444   | No documented layout | `1d96a417b5bf`  |
| 2438   | No documented layout | `1d96a417b5bf`  |
| 2434   | No documented layout | `1d96a417b5bf`  |
| 2429   | No documented layout | `1d96a417b5bf`  |
| 2421   | No documented layout | `1d96a417b5bf`  |
| 2414   | Layout 2             | `1d96a417b5bf`  |
| 2407   | No documented layout | `1d96a417b5bf`  |
| 2401   | No documented layout | `1d96a417b5bf`  |
| 2397   | No documented layout | `1d96a417b5bf`  |
| 2393   | No documented layout | `1d96a417b5bf`  |
| 2384   | No documented layout | `1d96a417b5bf`  |
| 2378   | No documented layout | `1d96a417b5bf`  |
| 2372   | No documented layout | `1d96a417b5bf`  |
| 2358   | No documented layout | `1d96a417b5bf`  |
| 2352   | No documented layout | `1d96a417b5bf`  |
| 2347   | No documented layout | `1d96a417b5bf`  |
| 2343   | No documented layout | `1d96a417b5bf`  |
| 2335   | No documented layout | `1d96a417b5bf`  |
| 2327   | No documented layout | `1d96a417b5bf`  |
| 2324   | No documented layout | `1d96a417b5bf`  |
| 2319   | No documented layout | `1d96a417b5bf`  |
| 2313   | No documented layout | `1d96a417b5bf`  |
| 2308   | No documented layout | `1d96a417b5bf`  |
| 2302   | No documented layout | `1d96a417b5bf`  |
| 2295   | No documented layout | `1d96a417b5bf`  |
| 2290   | No documented layout | `1d96a417b5bf`  |
| 2284   | No documented layout | `1d96a417b5bf`  |
| 2276   | No documented layout | `1d96a417b5bf`  |
| 2269   | No documented layout | `1d96a417b5bf`  |
| 2259   | No documented layout | `1d96a417b5bf`  |
| 2250   | No documented layout | `1d96a417b5bf`  |
| 2243   | No documented layout | `1d96a417b5bf`  |
| 2235   | No documented layout | `1d96a417b5bf`  |
| 2229   | No documented layout | `1d96a417b5bf`  |
| 2224   | No documented layout | `1d96a417b5bf`  |
| 2218   | No documented layout | `1d96a417b5bf`  |
| 2215   | No documented layout | `1d96a417b5bf`  |
| 2207   | No documented layout | `1d96a417b5bf`  |
| 2203   | No documented layout | `1d96a417b5bf`  |
| 2196   | No documented layout | `1d96a417b5bf`  |
| 2192   | No documented layout | `1d96a417b5bf`  |
| 2189   | No documented layout | `1d96a417b5bf`  |
| 2183   | No documented layout | `1d96a417b5bf`  |
| 2179   | No documented layout | `1d96a417b5bf`  |
| 2171   | No documented layout | `1d96a417b5bf`  |
| 2163   | No documented layout | `1d96a417b5bf`  |
| 2156   | No documented layout | `1d96a417b5bf`  |
| 2151   | No documented layout | `1d96a417b5bf`  |
| 2147   | No documented layout | `1d96a417b5bf`  |
| 2142   | No documented layout | `1d96a417b5bf`  |
| 2138   | No documented layout | `1d96a417b5bf`  |
| 2134   | No documented layout | `1d96a417b5bf`  |
| 2130   | No documented layout | `1d96a417b5bf`  |
| 2122   | No documented layout | `1d96a417b5bf`  |
| 2107   | No documented layout | `1d96a417b5bf`  |
| 2098   | No documented layout | `1d96a417b5bf`  |
| 2089   | No documented layout | `1d96a417b5bf`  |
| 2081   | No documented layout | `1d96a417b5bf`  |
| 2073   | No documented layout | `1d96a417b5bf`  |
| 2067   | No documented layout | `1d96a417b5bf`  |
| 2063   | No documented layout | `1d96a417b5bf`  |
| 2059   | No documented layout | `1d96a417b5bf`  |
| 2052   | No documented layout | `1d96a417b5bf`  |
| 2044   | No documented layout | `1d96a417b5bf`  |
| 2039   | No documented layout | `1d96a417b5bf`  |
| 2032   | No documented layout | `1d96a417b5bf`  |
| 2025   | No documented layout | `1d96a417b5bf`  |
| 2011   | No documented layout | `1d96a417b5bf`  |
| 2005   | No documented layout | `1d96a417b5bf`  |
| 2000   | No documented layout | `1d96a417b5bf`  |
| 1996   | No documented layout | `1d96a417b5bf`  |
| 1991   | No documented layout | `1d96a417b5bf`  |
| 1985   | No documented layout | `1d96a417b5bf`  |
| 1980   | No documented layout | `1d96a417b5bf`  |
| 1969   | No documented layout | `1d96a417b5bf`  |
| 1964   | No documented layout | `1d96a417b5bf`  |
| 1958   | No documented layout | `1d96a417b5bf`  |
| 1950   | No documented layout | `1d96a417b5bf`  |
| 1945   | No documented layout | `1d96a417b5bf`  |
| 1937   | No documented layout | `1d96a417b5bf`  |
| 1933   | No documented layout | `1d96a417b5bf`  |
| 1927   | No documented layout | `1d96a417b5bf`  |
| 1921   | No documented layout | `1d96a417b5bf`  |
| 1914   | No documented layout | `1d96a417b5bf`  |
| 1908   | No documented layout | `1d96a417b5bf`  |
| 1897   | No documented layout | `1d96a417b5bf`  |
| 1892   | No documented layout | `1d96a417b5bf`  |
| 1886   | No documented layout | `1d96a417b5bf`  |
| 1881   | No documented layout | `1d96a417b5bf`  |
| 1871   | No documented layout | `1d96a417b5bf`  |
| 1866   | No documented layout | `1d96a417b5bf`  |
| 1862   | No documented layout | `1d96a417b5bf`  |
| 1854   | No documented layout | `1d96a417b5bf`  |
| 1846   | No documented layout | `1d96a417b5bf`  |
| 1838   | No documented layout | `1d96a417b5bf`  |
| 1832   | No documented layout | `1d96a417b5bf`  |
| 1826   | No documented layout | `1d96a417b5bf`  |
| 1822   | No documented layout | `1d96a417b5bf`  |
| 1818   | No documented layout | `1d96a417b5bf`  |
| 1804   | No documented layout | `1d96a417b5bf`  |
| 1794   | No documented layout | `1d96a417b5bf`  |
| 1790   | No documented layout | `1d96a417b5bf`  |
| 1784   | Layout 1             | `1d96a417b5bf`  |
| 1774   | No documented layout | `1d96a417b5bf`  |
| 1771   | No documented layout | `1d96a417b5bf`  |
| 1762   | No documented layout | `1d96a417b5bf`  |
| 1759   | No documented layout | `1d96a417b5bf`  |
| 1754   | No documented layout | `1d96a417b5bf`  |
| 1749   | No documented layout | `1d96a417b5bf`  |
| 1743   | No documented layout | `1d96a417b5bf`  |
| 1737   | No documented layout | `1d96a417b5bf`  |
| 1731   | No documented layout | `1d96a417b5bf`  |
| 1725   | No documented layout | `1d96a417b5bf`  |
| 1717   | No documented layout | `1d96a417b5bf`  |
| 1710   | No documented layout | `1d96a417b5bf`  |
| 1704   | No documented layout | `1d96a417b5bf`  |
| 1698   | No documented layout | `1d96a417b5bf`  |
| 1690   | No documented layout | `1d96a417b5bf`  |
| 1685   | No documented layout | `1d96a417b5bf`  |
| 1680   | No documented layout | `1d96a417b5bf`  |
| 1674   | No documented layout | `1d96a417b5bf`  |
| 1668   | No documented layout | `1d96a417b5bf`  |
| 1659   | No documented layout | `1d96a417b5bf`  |
| 1649   | No documented layout | `1d96a417b5bf`  |
| 1642   | No documented layout | `1d96a417b5bf`  |
| 1636   | No documented layout | `1d96a417b5bf`  |
| 1628   | No documented layout | `1d96a417b5bf`  |
| 1622   | No documented layout | `1d96a417b5bf`  |
| 1614   | No documented layout | `1d96a417b5bf`  |
| 1608   | No documented layout | `1d96a417b5bf`  |
| 1602   | No documented layout | `1d96a417b5bf`  |
| 1598   | No documented layout | `1d96a417b5bf`  |
| 1594   | No documented layout | `1d96a417b5bf`  |
| 1590   | No documented layout | `1d96a417b5bf`  |
| 1587   | No documented layout | `1d96a417b5bf`  |
| 1584   | No documented layout | `1d96a417b5bf`  |
| 1579   | No documented layout | `1d96a417b5bf`  |
| 1572   | No documented layout | `1d96a417b5bf`  |
| 1565   | No documented layout | `1d96a417b5bf`  |
| 1559   | No documented layout | `1d96a417b5bf`  |
| 1554   | No documented layout | `1d96a417b5bf`  |
| 1547   | No documented layout | `1d96a417b5bf`  |
| 1537   | No documented layout | `1d96a417b5bf`  |
| 1529   | No documented layout | `1d96a417b5bf`  |
| 1524   | No documented layout | `1d96a417b5bf`  |
| 1519   | No documented layout | `1d96a417b5bf`  |
| 1509   | No documented layout | `1d96a417b5bf`  |
| 1506   | No documented layout | `1d96a417b5bf`  |
| 1504   | No documented layout | `1d96a417b5bf`  |
| 1500   | No documented layout | `1d96a417b5bf`  |
| 1493   | No documented layout | `1d96a417b5bf`  |
| 1489   | No documented layout | `1d96a417b5bf`  |
| 1485   | No documented layout | `1d96a417b5bf`  |
| 1481   | No documented layout | `1d96a417b5bf`  |
| 1474   | No documented layout | `1d96a417b5bf`  |
| 1466   | No documented layout | `1d96a417b5bf`  |
| 1462   | No documented layout | `1d96a417b5bf`  |
| 1459   | No documented layout | `1d96a417b5bf`  |
| 1453   | No documented layout | `1d96a417b5bf`  |
| 1450   | No documented layout | `1d96a417b5bf`  |
| 1445   | No documented layout | `1d96a417b5bf`  |
| 1439   | No documented layout | `1d96a417b5bf`  |
| 1433   | No documented layout | `1d96a417b5bf`  |
| 1430   | No documented layout | `1d96a417b5bf`  |
| 1426   | No documented layout | `1d96a417b5bf`  |
| 1421   | No documented layout | `1d96a417b5bf`  |
| 1417   | No documented layout | `1d96a417b5bf`  |
| 1416   | No documented layout | `1d96a417b5bf`  |
| 1409   | No documented layout | `1d96a417b5bf`  |
| 1405   | No documented layout | `1d96a417b5bf`  |
| 1401   | No documented layout | `1d96a417b5bf`  |
| 1396   | No documented layout | `1d96a417b5bf`  |
| 1391   | No documented layout | `1d96a417b5bf`  |
| 1390   | No documented layout | `1d96a417b5bf`  |
| 1386   | No documented layout | `1d96a417b5bf`  |
| 1381   | No documented layout | `1d96a417b5bf`  |
| 1379   | No documented layout | `1d96a417b5bf`  |
| 1372   | No documented layout | `1d96a417b5bf`  |
| 1366   | No documented layout | `1d96a417b5bf`  |
| 1364   | No documented layout | `1d96a417b5bf`  |
| 1363   | No documented layout | `1d96a417b5bf`  |
| 1360   | No documented layout | `1d96a417b5bf`  |
| 1358   | No documented layout | `1d96a417b5bf`  |
| 1355   | No documented layout | `1d96a417b5bf`  |
| 1351   | No documented layout | `1d96a417b5bf`  |
| 1348   | No documented layout | `1d96a417b5bf`  |
| 1346   | No documented layout | `1d96a417b5bf`  |
| 1341   | No documented layout | `1d96a417b5bf`  |
| 1340   | No documented layout | `1d96a417b5bf`  |
| 1338   | No documented layout | `1d96a417b5bf`  |
| 1335   | No documented layout | `1d96a417b5bf`  |
| 1333   | No documented layout | `1d96a417b5bf`  |
| 1329   | No documented layout | `1d96a417b5bf`  |
| 1327   | No documented layout | `1d96a417b5bf`  |
| 1324   | No documented layout | `1d96a417b5bf`  |
| 1321   | No documented layout | `1d96a417b5bf`  |
| 1319   | No documented layout | `1d96a417b5bf`  |
| 1318   | No documented layout | `1d96a417b5bf`  |
| 1316   | No documented layout | `1d96a417b5bf`  |
| 1313   | No documented layout | `1d96a417b5bf`  |
| 1311   | No documented layout | `1d96a417b5bf`  |
| 1309   | No documented layout | `1d96a417b5bf`  |
| 1304   | No documented layout | `1d96a417b5bf`  |
| 1292   | No documented layout | `1d96a417b5bf`  |
| 1286   | No documented layout | `1d96a417b5bf`  |
| 1280   | No documented layout | `1d96a417b5bf`  |
| 1276   | No documented layout | `1d96a417b5bf`  |
| 1267   | No documented layout | `1d96a417b5bf`  |
| 1261   | No documented layout | `1d96a417b5bf`  |
| 1256   | No documented layout | `1d96a417b5bf`  |
| 1250   | No documented layout | `1d96a417b5bf`  |
| 1246   | No documented layout | `1d96a417b5bf`  |
| 1239   | No documented layout | `1d96a417b5bf`  |
| 1230   | No documented layout | `1d96a417b5bf`  |
| 1226   | No documented layout | `1d96a417b5bf`  |
| 1220   | No documented layout | `1d96a417b5bf`  |
| 1217   | No documented layout | `1d96a417b5bf`  |
| 1211   | No documented layout | `1d96a417b5bf`  |
| 1210   | No documented layout | `1d96a417b5bf`  |
| 1208   | No documented layout | `1d96a417b5bf`  |
| 1203   | No documented layout | `1d96a417b5bf`  |
| 1197   | No documented layout | `1d96a417b5bf`  |
| 1194   | No documented layout | `1d96a417b5bf`  |
| 1192   | No documented layout | `1d96a417b5bf`  |
| 1187   | No documented layout | `1d96a417b5bf`  |
| 1183   | No documented layout | `1d96a417b5bf`  |
| 1177   | No documented layout | `1d96a417b5bf`  |
| 1173   | No documented layout | `1d96a417b5bf`  |
| 1167   | No documented layout | `1d96a417b5bf`  |
| 1164   | No documented layout | `1d96a417b5bf`  |
| 1156   | No documented layout | `1d96a417b5bf`  |
| 1149   | No documented layout | `1d96a417b5bf`  |
| 1144   | No documented layout | `1d96a417b5bf`  |
| 1137   | No documented layout | `1d96a417b5bf`  |
| 1132   | No documented layout | `1d96a417b5bf`  |
| 1127   | No documented layout | `1d96a417b5bf`  |
| 1122   | No documented layout | `1d96a417b5bf`  |
| 1118   | No documented layout | `1d96a417b5bf`  |
| 1114   | No documented layout | `1d96a417b5bf`  |
| 1109   | No documented layout | `1d96a417b5bf`  |
| 1102   | No documented layout | `1d96a417b5bf`  |
| 1096   | No documented layout | `1d96a417b5bf`  |
| 1088   | No documented layout | `1d96a417b5bf`  |
| 1081   | No documented layout | `1d96a417b5bf`  |
| 1076   | No documented layout | `1d96a417b5bf`  |
| 1069   | No documented layout | `1d96a417b5bf`  |
| 1064   | No documented layout | `1d96a417b5bf`  |
| 1058   | No documented layout | `1d96a417b5bf`  |
| 1051   | No documented layout | `1d96a417b5bf`  |
| 1044   | No documented layout | `1d96a417b5bf`  |
| 1036   | No documented layout | `1d96a417b5bf`  |
| 1026   | No documented layout | `1d96a417b5bf`  |
| 1016   | No documented layout | `1d96a417b5bf`  |
| 1009   | No documented layout | `1d96a417b5bf`  |
| 1005   | No documented layout | `1d96a417b5bf`  |
| 1000   | No documented layout | `1d96a417b5bf`  |
| 998    | No documented layout | `1d96a417b5bf`  |
| 990    | No documented layout | `1d96a417b5bf`  |
| 979    | No documented layout | `1d96a417b5bf`  |
| 972    | No documented layout | `1d96a417b5bf`  |
| 963    | No documented layout | `1d96a417b5bf`  |
| 955    | No documented layout | `1d96a417b5bf`  |
| 946    | No documented layout | `1d96a417b5bf`  |
| 938    | No documented layout | `1d96a417b5bf`  |
| 927    | No documented layout | `1d96a417b5bf`  |
| 911    | No documented layout | `1d96a417b5bf`  |
| 904    | No documented layout | `1d96a417b5bf`  |
| 899    | No documented layout | `1d96a417b5bf`  |
| 894    | No documented layout | `1d96a417b5bf`  |
| 885    | No documented layout | `1d96a417b5bf`  |
| 879    | No documented layout | `1d96a417b5bf`  |
| 872    | No documented layout | `1d96a417b5bf`  |
| 864    | No documented layout | `1d96a417b5bf`  |
| 855    | No documented layout | `1d96a417b5bf`  |
| 853    | No documented layout | `1d96a417b5bf`  |
| 845    | No documented layout | `1d96a417b5bf`  |
| 837    | No documented layout | `1d96a417b5bf`  |
| 829    | No documented layout | `1d96a417b5bf`  |
| 822    | No documented layout | `1d96a417b5bf`  |
| 814    | No documented layout | `1d96a417b5bf`  |
| 805    | No documented layout | `1d96a417b5bf`  |
| 794    | No documented layout | `1d96a417b5bf`  |
| 787    | No documented layout | `1d96a417b5bf`  |
| 780    | No documented layout | `1d96a417b5bf`  |
| 771    | No documented layout | `1d96a417b5bf`  |
| 760    | No documented layout | `1d96a417b5bf`  |
| 748    | No documented layout | `1d96a417b5bf`  |
| 741    | No documented layout | `1d96a417b5bf`  |
| 736    | No documented layout | `1d96a417b5bf`  |
| 731    | No documented layout | `1d96a417b5bf`  |
| 723    | No documented layout | `1d96a417b5bf`  |
| 711    | No documented layout | `1d96a417b5bf`  |
| 707    | No documented layout | `1d96a417b5bf`  |
| 697    | No documented layout | `1d96a417b5bf`  |
| 689    | No documented layout | `1d96a417b5bf`  |
| 683    | No documented layout | `1d96a417b5bf`  |
| 678    | No documented layout | `1d96a417b5bf`  |
| 670    | No documented layout | `1d96a417b5bf`  |
| 661    | No documented layout | `1d96a417b5bf`  |
| 656    | No documented layout | `1d96a417b5bf`  |
| 652    | No documented layout | `1d96a417b5bf`  |
| 643    | No documented layout | `1d96a417b5bf`  |
| 637    | No documented layout | `1d96a417b5bf`  |
| 630    | No documented layout | `1d96a417b5bf`  |
| 627    | No documented layout | `1d96a417b5bf`  |
| 621    | No documented layout | `1d96a417b5bf`  |
| 617    | No documented layout | `1d96a417b5bf`  |
| 615    | No documented layout | `1d96a417b5bf`  |
| 606    | No documented layout | `1d96a417b5bf`  |
| 599    | No documented layout | `1d96a417b5bf`  |
| 592    | No documented layout | `1d96a417b5bf`  |
| 586    | No documented layout | `1d96a417b5bf`  |
| 577    | No documented layout | `1d96a417b5bf`  |
| 569    | No documented layout | `1d96a417b5bf`  |
| 561    | No documented layout | `1d96a417b5bf`  |
| 554    | No documented layout | `1d96a417b5bf`  |
| 542    | No documented layout | `1d96a417b5bf`  |
| 532    | No documented layout | `1d96a417b5bf`  |
| 531    | No documented layout | `1d96a417b5bf`  |
| 526    | No documented layout | `1d96a417b5bf`  |
| 521    | No documented layout | `1d96a417b5bf`  |
| 517    | No documented layout | `1d96a417b5bf`  |
| 510    | No documented layout | `1d96a417b5bf`  |
| 508    | No documented layout | `1d96a417b5bf`  |
| 504    | No documented layout | `1d96a417b5bf`  |
| 497    | No documented layout | `1d96a417b5bf`  |
| 491    | No documented layout | `1d96a417b5bf`  |
| 485    | No documented layout | `1d96a417b5bf`  |
| 478    | No documented layout | `1d96a417b5bf`  |
| 472    | No documented layout | `1d96a417b5bf`  |
| 466    | No documented layout | `1d96a417b5bf`  |
| 457    | No documented layout | `1d96a417b5bf`  |
| 452    | No documented layout | `1d96a417b5bf`  |
| 449    | No documented layout | `1d96a417b5bf`  |
| 435    | No documented layout | `1d96a417b5bf`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset                           | Type                                   | Field                                    | Notes                                                                                        |
| -------------------------------- | -------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| `+0x00`                          | char[4]                                | magic                                    | ASCII `PABR`                                                                                 |
| `+0x04`                          | bytes[36]                              | unknown_04                               | All `0` on client 3482; see Open Questions                                                   |
| `+0x28`                          | i64                                    | inn_rental_time                          | `216000` on client 3482: the sheet's `3600` times 60                                         |
| `+0x30`                          | i16                                    | inn_room_service_time                    | `1` on client 3482                                                                           |
| `+0x32`                          | bytes[10]                              | unknown_32                               | All `0` on client 3482; see Open Questions                                                   |
| `+0x3C`                          | u32                                    | summon_monster_count_limit               | `10` on client 3482                                                                          |
| `+0x40`                          | f32                                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 3482                                                                        |
| `+0x44`                          | i32                                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 3482                                                                        |
| `+0x48`                          | bytes[13]                              | unknown_48                               | A u32 `0`, a u32 `1500000`, a u32 `100000` and a u8 `0` on client 3482 if read in that order |
| `+0x55`                          | u64                                    | saving_buff_time                         | `10000` on client 3482                                                                       |
| `+0x5D`                          | u64                                    | saving_cool_time                         | `60000` on client 3482                                                                       |
| `+0x65`                          | bytes[24]                              | unknown_65                               | All `0` on client 3482                                                                       |
| `+0x7D`                          | u8                                     | authentic_password_limit                 | `3` on client 3482                                                                           |
| `+0x7E`                          | u8                                     | password_length_min                      | `6` on client 3482                                                                           |
| `+0x7F`                          | u8                                     | password_length_max                      | `12` on client 3482                                                                          |
| `+0x80`                          | u32                                    | revival_product_no                       | `5017` on client 3482                                                                        |
| `+0x84`                          | u64                                    | rescue_cool_time                         | `1800000` on client 3482                                                                     |
| `+0x8C`                          | u32                                    | final_level_up_condition_ref             | Index into `strings`; string `0` (`"0"`) on client 3482                                      |
| `+0x90`                          | u64                                    | mail_remain_time                         | `864000` on client 3482                                                                      |
| `+0x98`                          | u64                                    | unknown_98                               | `259200` on client 3482; see Open Questions                                                  |
| `+0xA0`                          | i64                                    | reset_awakening_need_exp                 | `31000000` on client 3482                                                                    |
| `+0xA8`                          | u8                                     | expired_tent_check_day                   | `28` on client 3482, `14` on client 3283                                                     |
| `+0xA9`                          | bytes[20]                              | unknown_a9                               | All `0` on client 3482                                                                       |
| `+0xBD`                          | i32                                    | attack_to_servant_rate                   | `100000` on client 3482                                                                      |
| `+0xC1`                          | u32                                    | re_awakening_item_key                    | Item key; `44195` (Memory Fragment) on client 3482                                           |
| `+0xC5`                          | bytes[48000]                           | unknown_c5                               | Twelve arrays of 1000 4-byte values; see Notes                                               |
| `+0xBC45`                        | Unknown Lists                          | unknown_bc45                             | See Unknown Lists                                                                            |
| `unknown_bc45+0x00`              | Servant Option                         | servant_option                           | The `ServantOption` run; at `0xBCC9` on client 3482                                          |
| `servant_option+0x00`            | Movement Verify Option                 | movement_verify_option                   | The `MovementVerifyOption` run                                                               |
| `servant_option+0x72`            | Etc Option                             | etc_option                               | The first `EtcOption` run                                                                    |
| `etc_option+0x00`                | bytes[2800]                            | unknown_etc_option_00                    | Seven arrays of 100 i32; see Notes                                                           |
| `etc_option+0xAF0`               | Guild Option                           | guild_option                             | The `GuildOption` run; at `0xCBDE` on client 3482                                            |
| `guild_option+0x00`              | u32                                    | unknown_guild_option_00                  | Number of `unknown_guild_option_04`; `18` on client 3482                                     |
| `guild_option+0x04`              | Byte Int Pair[unknown_guild_option_00] | unknown_guild_option_04                  | See Byte Int Pair                                                                            |
| `unknown_guild_option_04+0x00`   | Item Market                            | item_market                              | The `ItemMarket` run                                                                         |
| `unknown_guild_option_04+0x53`   | bytes[26618]                           | unknown_guild_option_04_53               | See Open Questions                                                                           |
| `unknown_guild_option_04+0x684D` | Localizing Option                      | localizing_option                        | Part of the `LocalizingOption` run; at `0x13507` on client 3482                              |
| `localizing_option+0x00`         | bytes[38186]                           | unknown_localizing_option_00             | See Open Questions                                                                           |
| `localizing_option+0x952A`       | Arena                                  | arena                                    | The arena values; at `0x1CD3D` on client 3482                                                |
| `arena+0x00`                     | bytes[4248]                            | unknown_arena_00                         | The rest of the record up to the string table                                                |
| `arena+0x1098`                   | String Table                           | string_table                             | See String Table                                                                             |
| `EOF-0x08`                       | u32                                    | table_start                              | Offset of the string table                                                                   |
| `EOF-0x04`                       | u32                                    | zero                                     | Always `0`                                                                                   |

### Unknown Lists (variable: 20 bytes + entries)

Three counted lists and two i32 between the arrays of `unknown_c5` and the
`ServantOption` run, first on client 3464; client 3458 holds 8 `0` bytes in
their place.

| Offset                  | Type                          | Field               | Notes                                                                    |
| ----------------------- | ----------------------------- | ------------------- | ------------------------------------------------------------------------ |
| `+0x00`                 | u32                           | unknown_00          | Number of `unknown_04`; `6` on client 3482                               |
| `+0x04`                 | Int Float Pair[unknown_00]    | unknown_04          | `(70, 3), (71, 6), (72, 9), (73, 12), (74, 15), (75, 18)` on client 3482 |
| `unknown_04+0x00`       | u32                           | unknown_04_00       | Number of `unknown_04_04`; `6` on client 3482                            |
| `unknown_04+0x04`       | Int Float Pair[unknown_04_00] | unknown_04_04       | `(70, 3), (71, 6), (72, 9), (73, 12), (74, 15), (75, 18)` on client 3482 |
| `unknown_04_04+0x00`    | u32                           | unknown_04_04_00    | Number of `unknown_04_04_04`; `4` on client 3482                         |
| `unknown_04_04+0x04`    | f32[unknown_04_04_00]         | unknown_04_04_04    | `9, 6, 3, 0` on client 3482                                              |
| `unknown_04_04_04+0x00` | i32                           | unknown_04_04_04_00 | `-3` on client 3482                                                      |
| `unknown_04_04_04+0x04` | i32                           | unknown_04_04_04_04 | `0` on client 3482                                                       |

### Int Float Pair (8 bytes)

| Offset  | Type | Field      | Notes                                      |
| ------- | ---- | ---------- | ------------------------------------------ |
| `+0x00` | u32  | unknown_00 | `70` to `75` on client 3482                |
| `+0x04` | f32  | unknown_04 | `3` to `18` in steps of `3` on client 3482 |

### Servant Option (variable: 350 bytes + revive costs)

| Offset              | Type                   | Field                                               | Notes                                                                                |
| ------------------- | ---------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`             | u64                    | mating_time                                         | `8640` on client 3482; the sheet's `8640000` divided by 1000                         |
| `+0x08`             | u64                    | mating_regist_time                                  | `43200000` on client 3482                                                            |
| `+0x10`             | i32                    | taming_rate                                         | `300000` on client 3482                                                              |
| `+0x14`             | i32                    | taming_value                                        | `1000000` on client 3482, `200000` on client 1784                                    |
| `+0x18`             | u32                    | elephant_taming_item_key                            | Item key; `54019` ([Guild] Desert Peanut) on client 3482                             |
| `+0x1C`             | i32                    | elephant_taming_value                               | `100000` on client 3482                                                              |
| `+0x20`             | i32                    | elephant_taming_rate                                | `50000` on client 3482                                                               |
| `+0x24`             | i32                    | elephant_taming_fail_rate                           | `150000` on client 3482                                                              |
| `+0x28`             | i32                    | taming_max_level                                    | `20` on client 3482, `10` on client 1784                                             |
| `+0x2C`             | u64                    | market_regist_time                                  | `0` on client 3482                                                                   |
| `+0x34`             | i64                    | vehicle_seal_cost                                   | `1000` on client 3482                                                                |
| `+0x3C`             | i64                    | vehicle_recovery_cost                               | `500` on client 3482                                                                 |
| `+0x44`             | i32                    | vehicle_mating_mp                                   | `1000000` on client 3482                                                             |
| `+0x48`             | i64                    | vehicle_sell_cost                                   | `20` on client 3482                                                                  |
| `+0x50`             | i64                    | vehicle_emission_experience                         | `255` on client 3482                                                                 |
| `+0x58`             | i16                    | stable_slot_limit                                   | `3` on client 3482                                                                   |
| `+0x5A`             | i32                    | discount_percent_for_servant_mating_place           | `700000` on client 3482                                                              |
| `+0x5E`             | i32                    | discount_percent_for_servant_imprint                | `300000` on client 3482                                                              |
| `+0x62`             | i64                    | taming_life_experience                              | `15300` on client 3482                                                               |
| `+0x6A`             | i64                    | vehicle_level_up_life_experience                    | `17` on client 3482                                                                  |
| `+0x72`             | i64                    | register_delay_from_mating                          | `0` on client 3482                                                                   |
| `+0x7A`             | i64                    | register_delay_from_market                          | `0` on client 3482                                                                   |
| `+0x82`             | i64                    | vehicle_self_mating_price                           | `35000` on client 3482                                                               |
| `+0x8A`             | f32                    | vehicle_add_exp_by_training                         | `1.5` on client 3482                                                                 |
| `+0x8E`             | i32                    | vehicle_add_taming_by_training                      | `3000` on client 3482                                                                |
| `+0x92`             | i32                    | vehicle_learn_skill_add_rate_from_imprint           | `100000` on client 3482                                                              |
| `+0x96`             | f32                    | vehicle_seal_distance                               | `3000` on client 3482                                                                |
| `+0x9A`             | f32                    | idle_vehicle_seal_distance                          | `4000` on client 3482                                                                |
| `+0x9E`             | i64                    | idle_vehicle_seal_time                              | `3600` on client 3482, `7200` on client 1784                                         |
| `+0xA6`             | i32                    | vehicle_decrease_cost_by_mating_count               | `250000` on client 3482                                                              |
| `+0xAA`             | i32                    | vehicle_decrease_cost_by_mating_clear               | `150000` on client 3482                                                              |
| `+0xAE`             | i32                    | vehicle_decrease_cost_by_dead_clear                 | `50000` on client 3482                                                               |
| `+0xB2`             | i32                    | vehicle_learn_skill_by_level                        | `0` on client 3482, `50000` on client 1784                                           |
| `+0xB6`             | i32                    | vehicle_skill_change_value                          | `250000` on client 3482                                                              |
| `+0xBA`             | i32                    | vehicle_min_price                                   | `0` on client 3482                                                                   |
| `+0xBE`             | i32                    | vehicle_max_price                                   | `0` on client 3482                                                                   |
| `+0xC2`             | i32                    | vehicle_change_form_with_skill_rate                 | `300000` on client 3482                                                              |
| `+0xC6`             | i64                    | vehicle_change_form_with_skill_vary_experience      | `200000` on client 3482                                                              |
| `+0xCE`             | i32                    | vehicle_register_price_rate                         | `300000` on client 3482                                                              |
| `+0xD2`             | i64                    | skill_exp_training_time                             | `0` on client 3482, `3600` on client 1784 (the sheet's `3600000` divided by 1000)    |
| `+0xDA`             | i64                    | stallion_skill_exp_training_time                    | `0` on client 3482                                                                   |
| `+0xE2`             | u32                    | exchange_elephant_item                              | Item key; `9916` ([Guild] Baby Elephant) on client 3482                              |
| `+0xE6`             | i32                    | down_grade_from_dead_count                          | `5000` on client 3482                                                                |
| `+0xEA`             | u64                    | unseal_delay_time                                   | `300000` on client 3482                                                              |
| `+0xF2`             | f32                    | pc_room_whistle_distance                            | `30000` on client 3482                                                               |
| `+0xF6`             | i32                    | pc_room_whistle_type                                | `15` on client 3482                                                                  |
| `+0xFA`             | i32                    | add_percent_for_stallion_market_price               | `1700000` on client 3482, `2600000` on client 1784                                   |
| `+0xFE`             | i32                    | add_percent_for_stallion_mating_market_price        | `1700000` on client 3482, `2600000` on client 1784                                   |
| `+0x102`            | i32                    | stallion_child_base_skill_add_rate                  | `500000` on client 3482                                                              |
| `+0x106`            | i32                    | stallion_training_complete_required_experience      | `60000` on client 3482                                                               |
| `+0x10A`            | i32                    | nine_tier_horse_acquisition_rate                    | `0` on client 3482                                                                   |
| `+0x10E`            | i32                    | stallion_training_skill_default_rate                | `300000` on client 3482                                                              |
| `+0x112`            | i32                    | stallion_training_skill_add_rate                    | `100000` on client 3482                                                              |
| `+0x116`            | u32                    | stallion_training_complete_required_item            | Item key; `50801` (Krogdalo's Origin Stone) on client 3482                           |
| `+0x11A`            | i64                    | stallion_training_complete_required_item_count      | `1` on client 3482                                                                   |
| `+0x122`            | u32                    | prevent_stallion_training_skill_exp_down_item       | Item key; `16080` (Cron Stone) on client 3482                                        |
| `+0x126`            | i64                    | prevent_stallion_training_skill_exp_down_item_count | `100` on client 3482                                                                 |
| `+0x12E`            | i32                    | prevent_stallion_training_skill_exp_down_item_rate  | `500000` on client 3482                                                              |
| `+0x132`            | u64                    | revive_cost_count                                   | Number of `revive_costs`; `10` on client 3482                                        |
| `+0x13A`            | i64[revive_cost_count] | revive_costs                                        | `100000, 2000, 4000, 7000, 10000, 15000, 20000, 25000, 35000, 100000` on client 3482 |
| `revive_costs+0x00` | i64                    | clear_guild_servant_dead_count_cost                 | `100000000` on client 3482                                                           |
| `revive_costs+0x08` | u64                    | unknown_revive_costs_08                             | `300000000` on client 3482; not on client 1784                                       |
| `revive_costs+0x10` | u32                    | fantasy_upgrade_need_item_key                       | Item key; `757008` (Mythical Censer) on client 3482                                  |
| `revive_costs+0x14` | i64                    | fantasy_upgrade_item_max_count                      | `1` on client 3482                                                                   |
| `revive_costs+0x1C` | i32                    | fantasy_upgrade_item_success_rate                   | `3` on client 3482                                                                   |
| `revive_costs+0x20` | i32                    | fantasy_upgrade_max_success_rate                    | `30000` on client 3482                                                               |

### Movement Verify Option (114 bytes)

| Offset  | Type | Field                          | Notes                   |
| ------- | ---- | ------------------------------ | ----------------------- |
| `+0x00` | f32  | pc_move_tr_send_term           | `0.8` on client 3482    |
| `+0x04` | f32  | pc_rotation_tr_send_term       | `0.2` on client 3482    |
| `+0x08` | i32  | send_direction_threshold       | `150` on client 3482    |
| `+0x0C` | f32  | movement_limit                 | `0` on client 3482      |
| `+0x10` | f32  | movement_limit_on_vehicle      | `0` on client 3482      |
| `+0x14` | f32  | once_rate                      | `0` on client 3482      |
| `+0x18` | f32  | once_tolerance                 | `0` on client 3482      |
| `+0x1C` | u64  | once_tick_tolerance            | `0` on client 3482      |
| `+0x24` | i32  | term_skip_count                | `0` on client 3482      |
| `+0x28` | f32  | term_rate                      | `0` on client 3482      |
| `+0x2C` | f32  | term_tolerance                 | `0` on client 3482      |
| `+0x30` | u64  | term_tick_tolerance            | `0` on client 3482      |
| `+0x38` | u64  | action_verify_count            | `100` on client 3482    |
| `+0x40` | f32  | action_verify_fast_value       | `1000` on client 3482   |
| `+0x44` | f32  | action_verify_slow_value       | `60000` on client 3482  |
| `+0x48` | i32  | action_verify_once             | `3000` on client 3482   |
| `+0x4C` | u64  | action_verify_stun_time        | `5000` on client 3482   |
| `+0x54` | u8   | buff_speed_verify_active_check | `1` on client 3482      |
| `+0x55` | u64  | buff_speed_verify_check_tick   | `600000` on client 3482 |
| `+0x5D` | u8   | is_rough_check_to_attack       | `1` on client 3482      |
| `+0x5E` | i32  | tolerance_to_attack_front_rate | `300000` on client 3482 |
| `+0x62` | f32  | tolerance_to_attack_back_value | `200` on client 3482    |
| `+0x66` | i32  | speed_hack_check_count         | `0` on client 3482      |
| `+0x6A` | i64  | client_version                 | `51` on client 3482     |

### Etc Option (variable: 459 bytes + keys and values)

| Offset                                      | Type                                           | Field                                          | Notes                                                                                                                                                        |
| ------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `+0x00`                                     | u64                                            | house_auction_sale_time                        | `86400000` on client 3482                                                                                                                                    |
| `+0x08`                                     | u32                                            | tutorial_condition_ref                         | Index into `strings`; `1` on client 3482, string `getLevel()<5`                                                                                              |
| `+0x0C`                                     | i32                                            | delivery_price_per_distance                    | `100` on client 3482                                                                                                                                         |
| `+0x10`                                     | i32                                            | delivery_link_node_penalty                     | `3000000` on client 3482                                                                                                                                     |
| `+0x14`                                     | i32                                            | delivery_trade_penalty                         | `3` on client 3482                                                                                                                                           |
| `+0x18`                                     | i32                                            | delivery_packing_weight                        | `500000` on client 3482                                                                                                                                      |
| `+0x1C`                                     | f32                                            | trade_distance_vehicle                         | `3000` on client 3482                                                                                                                                        |
| `+0x20`                                     | f32                                            | trade_distance_ship                            | `30000` on client 3482                                                                                                                                       |
| `+0x24`                                     | i32                                            | working_base_work_time                         | `600000` on client 3482                                                                                                                                      |
| `+0x28`                                     | i32                                            | working_base_work_time_for_house               | `300000` on client 3482                                                                                                                                      |
| `+0x2C`                                     | i32                                            | npc_upgrade_time                               | `28800000` on client 3482, `86400000` on client 1784                                                                                                         |
| `+0x30`                                     | i32                                            | npc_house_party_time                           | `600000` on client 3482                                                                                                                                      |
| `+0x34`                                     | i64                                            | npc_working_exp                                | `10` on client 3482, `0` on client 1784                                                                                                                      |
| `+0x3C`                                     | i64                                            | npc_working_time_exp                           | `1` on client 3482, `0` on client 1784                                                                                                                       |
| `+0x44`                                     | i64                                            | npc_working_time_rate                          | `50` on client 3482, `0` on client 1784                                                                                                                      |
| `+0x4C`                                     | i64                                            | npc_working_harvesting_exp                     | `3` on client 3482, `0` on client 1784                                                                                                                       |
| `+0x54`                                     | i32                                            | npc_worker_min_max_price_percent               | `0` on client 3482                                                                                                                                           |
| `+0x58`                                     | i64                                            | npc_worker_upgrade_point_price                 | `300000` on client 3482                                                                                                                                      |
| `+0x60`                                     | u64                                            | npc_worker_auction_expire_time                 | `86400000` on client 3482                                                                                                                                    |
| `+0x68`                                     | i32                                            | guild_house_craft_max_working_count            | `200` on client 3482                                                                                                                                         |
| `+0x6C`                                     | u32                                            | unknown_6c                                     | `0` on client 3482                                                                                                                                           |
| `+0x70`                                     | i32                                            | unknown_70                                     | `330000` on client 3482, `0` on client 1784                                                                                                                  |
| `+0x74`                                     | i64                                            | detect_player_price                            | `10000` on client 3482                                                                                                                                       |
| `+0x7C`                                     | i32                                            | tendency_from_seal                             | `-2000` on client 3482                                                                                                                                       |
| `+0x80`                                     | i32                                            | tendency_from_trade                            | `-5000` on client 3482                                                                                                                                       |
| `+0x84`                                     | u8                                             | is_check_for_operation                         | `0` on client 3482                                                                                                                                           |
| `+0x85`                                     | u8                                             | is_calculate_interior_point_all                | `0` on client 3482                                                                                                                                           |
| `+0x86`                                     | i16                                            | limited_bid_count_for_house_auction            | `3` on client 3482                                                                                                                                           |
| `+0x88`                                     | f32                                            | add_hit_by_knowledge                           | `6` on client 3482, `0` on client 1784                                                                                                                       |
| `+0x8C`                                     | f32                                            | guard_pvp_rate                                 | `2.4` on client 3482, `0` on client 1784                                                                                                                     |
| `+0x90`                                     | f32                                            | guard_rate                                     | `1` on client 3482, `0` on client 1784                                                                                                                       |
| `+0x94`                                     | f32                                            | guard_pvp_rate_in_battle_royal                 | `2` on client 3482, `0` on client 1784                                                                                                                       |
| `+0x98`                                     | i16                                            | collect_consume_wp                             | `1` on client 3482                                                                                                                                           |
| `+0x9A`                                     | f32                                            | quote_view_consume_wp                          | `1500000` on client 3482                                                                                                                                     |
| `+0x9E`                                     | i32                                            | unknown_9e                                     | `1000000` on client 3482; not on client 1784                                                                                                                 |
| `+0xA2`                                     | i32                                            | unknown_a2                                     | `500000` on client 3482; not on client 1784                                                                                                                  |
| `+0xA6`                                     | i32                                            | world_chat_condition                           | `99` on client 3482                                                                                                                                          |
| `+0xAA`                                     | i32                                            | max_endurance_increase_rate                    | `100000` on client 3482, `0` on client 1784                                                                                                                  |
| `+0xAE`                                     | i32                                            | trade_bonus_exp_percent                        | `200` on client 3482                                                                                                                                         |
| `+0xB2`                                     | i32                                            | trade_bonus_gold_percent                       | `68` on client 3482                                                                                                                                          |
| `+0xB6`                                     | i32                                            | max_distance_bonus                             | `1500000` on client 3482                                                                                                                                     |
| `+0xBA`                                     | u64                                            | catch_resistance_time                          | `12000` on client 3482                                                                                                                                       |
| `+0xC2`                                     | i32                                            | catch_resistance_rate                          | `30000` on client 3482                                                                                                                                       |
| `+0xC6`                                     | i32                                            | catch_resistance_extra_rate                    | `5000000` on client 3482                                                                                                                                     |
| `+0xCA`                                     | i32                                            | reduce_repair_price_for_seal                   | `670000` on client 3482                                                                                                                                      |
| `+0xCE`                                     | i32                                            | endurance_decrease_percent_equip_item_for_seal | `500000` on client 3482                                                                                                                                      |
| `+0xD2`                                     | u16                                            | worker_shop_consume_wp                         | `5` on client 3482                                                                                                                                           |
| `+0xD4`                                     | u16                                            | world_item_market_consume_wp                   | `1` on client 3482                                                                                                                                           |
| `+0xD6`                                     | i32                                            | trade_game_bonus_percent                       | `50000` on client 3482                                                                                                                                       |
| `+0xDA`                                     | u16                                            | trade_game_consume_wp                          | `5` on client 3482                                                                                                                                           |
| `+0xDC`                                     | i32                                            | trade_game_try_count                           | `3` on client 3482                                                                                                                                           |
| `+0xE0`                                     | i32                                            | trade_game_goal_interval                       | `3` on client 3482                                                                                                                                           |
| `+0xE4`                                     | u16                                            | other_region_trade_graph_show_wp               | `1` on client 3482                                                                                                                                           |
| `+0xE6`                                     | i32                                            | territory_supply_max_sell_rate                 | `2500000` on client 3482                                                                                                                                     |
| `+0xEA`                                     | i32                                            | trade_supply_max_sell_rate                     | `2500000` on client 3482                                                                                                                                     |
| `+0xEE`                                     | u32                                            | dyeing_combine_item                            | Item key; `17030` (Unknown Dye Box) on client 3482                                                                                                           |
| `+0xF2`                                     | f32                                            | unknown_f2                                     | `-0.4` on client 3482; see Open Questions                                                                                                                    |
| `+0xF6`                                     | f32                                            | unknown_f6                                     | `120` on client 3482; see Open Questions                                                                                                                     |
| `+0xFA`                                     | f32                                            | unknown_fa                                     | `1.8` on client 3482; see Open Questions                                                                                                                     |
| `+0xFE`                                     | f32                                            | unknown_fe                                     | `100` on client 3482; not on client 1784; see Open Questions                                                                                                 |
| `+0x102`                                    | u16                                            | day_random_shop_consume_wp                     | `10` on client 3482                                                                                                                                          |
| `+0x104`                                    | i32                                            | free_revival_level                             | `20` on client 3482                                                                                                                                          |
| `+0x108`                                    | f32                                            | fishing_add_rate                               | `2.5` on client 3482                                                                                                                                         |
| `+0x10C`                                    | i32                                            | fishing_decrease_endurance_rate                | `900000` on client 3482                                                                                                                                      |
| `+0x110`                                    | i32                                            | fishing_decrease_endurance_rate_add_per_level  | `5000` on client 3482                                                                                                                                        |
| `+0x114`                                    | i32                                            | fishing_minimum_decrease_endurance_rate        | `400000` on client 3482                                                                                                                                      |
| `+0x118`                                    | u32                                            | alchemy_residue_item_key                       | Item key; `9725` (Burnt Reagent) on client 3482                                                                                                              |
| `+0x11C`                                    | i32                                            | alchemy_residue_error_count                    | `3` on client 3482                                                                                                                                           |
| `+0x120`                                    | u32                                            | cook_residue_item_key                          | Item key; `9724` (Failed Dish) on client 3482                                                                                                                |
| `+0x124`                                    | i32                                            | cook_residue_error_count                       | `3` on client 3482                                                                                                                                           |
| `+0x128`                                    | i32                                            | node_increase_item_drop_percent                | `50000` on client 3482                                                                                                                                       |
| `+0x12C`                                    | i32                                            | unknown_12c                                    | `5000` on client 3482; not on client 1784                                                                                                                    |
| `+0x130`                                    | i32                                            | unknown_130                                    | `2000000` on client 3482; not on client 1784                                                                                                                 |
| `+0x134`                                    | i16                                            | supply_shop_interval                           | `3` on client 3482                                                                                                                                           |
| `+0x136`                                    | i32                                            | supply_shop_refresh_percent                    | `100` on client 3482                                                                                                                                         |
| `+0x13A`                                    | i16                                            | territory_supply_shop_interval                 | `4` on client 3482                                                                                                                                           |
| `+0x13C`                                    | i32[8]                                         | alchemy_stone_up_grade_rate                    | `3000, 1000, 750, 2000, 800, 700, 500, 0` on client 3482, `3000, 1000, 750, 250, 65, 13, 2, 0` on client 1784; see Field Names                               |
| `+0x15C`                                    | u32                                            | pruning                                        | `57965` on client 3482                                                                                                                                       |
| `+0x160`                                    | u32                                            | catchbug                                       | `57966` on client 3482                                                                                                                                       |
| `+0x164`                                    | u32                                            | prevent_downgrade_item_key                     | Item key; `16080` (Cron Stone) on client 3482                                                                                                                |
| `+0x168`                                    | u32                                            | promotion_enchant_item_key                     | Item key; `721003` (Caphras Stone) on client 3482                                                                                                            |
| `+0x16C`                                    | i32                                            | accessory_broken_rate                          | `400000` on client 3482                                                                                                                                      |
| `+0x170`                                    | i32                                            | min_random_price                               | `1000000` on client 3482                                                                                                                                     |
| `+0x174`                                    | i32                                            | added_pet_collect_drop_rate                    | `-700000` on client 3482                                                                                                                                     |
| `+0x178`                                    | u8                                             | commerce_type_for_trade_game                   | `7` on client 3482                                                                                                                                           |
| `+0x179`                                    | i32                                            | commerce_type_for_trade_game_percent           | `2000000` on client 3482                                                                                                                                     |
| `+0x17D`                                    | u64                                            | world_chat_item_key_count                      | Number of `world_chat_item_keys`; `2` on client 3482                                                                                                         |
| `+0x185`                                    | u32[world_chat_item_key_count]                 | world_chat_item_keys                           | `17645, 18851` on client 3482; item keys ([Event] Megaphone, Megaphone)                                                                                      |
| `world_chat_item_keys+0x00`                 | u64                                            | desert_storm_shielder_character_key_count      | Number of `desert_storm_shielder_character_keys`; `1` on client 3482                                                                                         |
| `world_chat_item_keys+0x08`                 | u16[desert_storm_shielder_character_key_count] | desert_storm_shielder_character_keys           | `910` on client 3482; character keys                                                                                                                         |
| `desert_storm_shielder_character_keys+0x00` | u32                                            | resist_desert_count                            | Number of `resist_desert`; `6` on client 3482, `5` on client 1784                                                                                            |
| `desert_storm_shielder_character_keys+0x04` | u32[resist_desert_count]                       | resist_desert                                  | `16012, 16016, 18858, 608814, 750567, 751503` on client 3482, `16012, 16016, 18858, 750567, 751503` on client 1784; item keys (compasses) in ascending order |
| `resist_desert+0x00`                        | u64                                            | add_resist_value_count                         | Number of `add_resist_values`; `6` on client 3482                                                                                                            |
| `resist_desert+0x08`                        | i32[add_resist_value_count]                    | add_resist_values                              | `1, 1, 1, 1, 1, 1` on client 3482                                                                                                                            |
| `add_resist_values+0x00`                    | u64                                            | keep_resist_time                               | `5000` on client 3482; see Field Names                                                                                                                       |
| `add_resist_values+0x08`                    | u64                                            | ignore_resist_overlap_time                     | `1000` on client 3482                                                                                                                                        |
| `add_resist_values+0x10`                    | i32                                            | comeback_standard_time                         | `720` on client 3482, `0` on client 1784                                                                                                                     |
| `add_resist_values+0x14`                    | i32                                            | manufacture_cook_validity_time                 | `20` on client 3482                                                                                                                                          |
| `add_resist_values+0x18`                    | i32                                            | manufacture_cook_add_exp                       | `20` on client 3482                                                                                                                                          |
| `add_resist_values+0x1C`                    | i32                                            | item_upgrade_need_count_percent                | `200000` on client 3482                                                                                                                                      |
| `add_resist_values+0x20`                    | i32                                            | unknown_add_resist_values_20                   | `100000` on client 3482                                                                                                                                      |
| `add_resist_values+0x24`                    | i32                                            | unknown_add_resist_values_24                   | `180` on client 3482, `600` on client 1784                                                                                                                   |
| `add_resist_values+0x28`                    | i16                                            | unknown_add_resist_values_28                   | `0` on client 3482                                                                                                                                           |
| `add_resist_values+0x2A`                    | i64                                            | keep_random_item_time                          | `900` on client 3482                                                                                                                                         |

### Guild Option (variable: 118 bytes + percents)

| Offset                                   | Type                                        | Field                                        | Notes                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+0x00`                                  | u64                                         | king_or_lord_tent_attack_message_cycle       | `30000` on client 3482, `60000` on client 1784                                                                                                       |
| `+0x08`                                  | u64                                         | king_or_lord_tent_attack_percent_count       | Number of `king_or_lord_tent_attack_percents`; `2` on client 3482                                                                                    |
| `+0x10`                                  | i32[king_or_lord_tent_attack_percent_count] | king_or_lord_tent_attack_percents            | `300000, 600000` on client 3482                                                                                                                      |
| `king_or_lord_tent_attack_percents+0x00` | i64                                         | guild_first_level_comporate_tax              | `0` on client 3482                                                                                                                                   |
| `king_or_lord_tent_attack_percents+0x08` | i64                                         | guild_second_level_comporate_tax             | `100000` on client 3482                                                                                                                              |
| `king_or_lord_tent_attack_percents+0x10` | i64                                         | guild_third_level_comporate_tax              | `250000` on client 3482                                                                                                                              |
| `king_or_lord_tent_attack_percents+0x18` | i64                                         | guild_fourth_level_comporate_tax             | `500000` on client 3482                                                                                                                              |
| `king_or_lord_tent_attack_percents+0x20` | u64                                         | next_guild_joinable_time                     | `86400` on client 3482                                                                                                                               |
| `king_or_lord_tent_attack_percents+0x28` | u64                                         | unknown_king_or_lord_tent_attack_percents_28 | `1` on client 3482; not on client 1784                                                                                                               |
| `king_or_lord_tent_attack_percents+0x30` | i32                                         | guild_tendency_convert_percent_for_explore   | `100000` on client 3482                                                                                                                              |
| `king_or_lord_tent_attack_percents+0x34` | i32                                         | guild_tendency_convert_percent_for_player    | `0` on client 3482                                                                                                                                   |
| `king_or_lord_tent_attack_percents+0x38` | i32                                         | guild_tendency_convert_percent_for_guild_war | `0` on client 3482                                                                                                                                   |
| `king_or_lord_tent_attack_percents+0x3C` | i32                                         | consume_guild_tendency_for_guild_war         | `100000` on client 3482                                                                                                                              |
| `king_or_lord_tent_attack_percents+0x40` | i64                                         | increase_exp_member_level_up                 | `1` on client 3482                                                                                                                                   |
| `king_or_lord_tent_attack_percents+0x48` | i16                                         | increase_activity_member_level_up            | `3` on client 3482                                                                                                                                   |
| `king_or_lord_tent_attack_percents+0x4A` | u32[5]                                      | cheer_guild_buffs                            | `4262264833, 4262330369, 4262395905, 4262461441, 4262526977` on client 3482; buff keys `65037` to `65041`, each stored as the key times 65536 plus 1 |
| `king_or_lord_tent_attack_percents+0x5E` | i64                                         | reservation_arsha_price                      | `10000000` on client 3482                                                                                                                            |

### Byte Int Pair (5 bytes)

| Offset  | Type | Field      | Notes                           |
| ------- | ---- | ---------- | ------------------------------- |
| `+0x00` | u8   | unknown_00 | `1` to `85` on client 3482      |
| `+0x01` | u32  | unknown_01 | `3`, `6` or `12` on client 3482 |

### Item Market (83 bytes)

| Offset  | Type      | Field                                                      | Notes                  |
| ------- | --------- | ---------------------------------------------------------- | ---------------------- |
| `+0x00` | i32       | item_market_trade_fee_percent                              | `0` on client 3482     |
| `+0x04` | i32       | item_market_refund_percent_for_pc_room                     | `0` on client 3482     |
| `+0x08` | i32       | item_market_refund_percent_for_premium_package             | `0` on client 3482     |
| `+0x0C` | i32       | item_market_refund_percent_for_pc_room_and_premium_package | `0` on client 3482     |
| `+0x10` | u64       | item_market_register_waiting_tick                          | `0` on client 3482     |
| `+0x18` | u64       | item_market_register_random_tick                           | `0` on client 3482     |
| `+0x20` | u64       | item_market_display_tick                                   | `0` on client 3482     |
| `+0x28` | i16       | item_market_register_count_per_user                        | `30` on client 3482    |
| `+0x2A` | bytes[41] | unknown_2a                                                 | All `0` on client 3482 |

### Localizing Option (variable: 256 bytes + classes and region groups)

| Offset                              | Type                                   | Field                                   | Notes                                                                                |
| ----------------------------------- | -------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`                             | i32                                    | item_market_rate                        | `40000` on client 3482                                                               |
| `+0x04`                             | i32                                    | item_market_price                       | `750000` on client 3482                                                              |
| `+0x08`                             | u64                                    | special_stock_tic                       | `600000` on client 3482                                                              |
| `+0x10`                             | i32                                    | special_stock_down_rate                 | `30000` on client 3482                                                               |
| `+0x14`                             | i32                                    | item_market_reservation_rate            | `450000` on client 3482                                                              |
| `+0x18`                             | i32                                    | item_market_reservation_count           | `1` on client 3482                                                                   |
| `+0x1C`                             | u64                                    | item_market_reservation_reset_time      | `43200` on client 3482                                                               |
| `+0x24`                             | i32                                    | item_market_reservation_bonus           | `200000` on client 3482                                                              |
| `+0x28`                             | i32                                    | cash_item_restriction_day               | `3` on client 3482                                                                   |
| `+0x2C`                             | u8                                     | unknown_2c                              | `0` on client 3482; see Runs Past the Head                                           |
| `+0x2D`                             | i16                                    | trade_supply_count_shop                 | `2` on client 3482                                                                   |
| `+0x2F`                             | i32                                    | growth_channel_level_limit              | `62` on client 3482                                                                  |
| `+0x33`                             | i32                                    | skill_free_reset_level_limit            | `57` on client 3482                                                                  |
| `+0x37`                             | u8                                     | unknown_37                              | `0` on client 3482                                                                   |
| `+0x38`                             | u32                                    | possible_class_count                    | Number of `possible_classes`; `32` on client 3482, `23` on client 1784               |
| `+0x3C`                             | u8[possible_class_count]               | possible_classes                        | Class types; 32 on client 3482, the sheet's 23 on client 1784                        |
| `possible_classes+0x00`             | u32                                    | unknown_possible_classes_00             | `0` on client 3482                                                                   |
| `possible_classes+0x04`             | u32                                    | accessible_region_group_key_count       | Number of `accessible_region_group_keys`; `246` on client 3482, `149` on client 1784 |
| `possible_classes+0x08`             | u16[accessible_region_group_key_count] | accessible_region_group_keys            | Region group keys in ascending order; on client 1784 the sheet's 149 keys            |
| `accessible_region_group_keys+0x00` | u8                                     | use_password                            | `0` on client 3482; the sheet holds `1`                                              |
| `accessible_region_group_keys+0x01` | u8                                     | use_pc_exchange                         | `1` on client 3482                                                                   |
| `accessible_region_group_keys+0x02` | u8                                     | use_wp_at_life_activity                 | `0` on client 3482                                                                   |
| `accessible_region_group_keys+0x03` | u8                                     | use_wp_at_life_activity_manufacture     | `0` on client 3482                                                                   |
| `accessible_region_group_keys+0x04` | i32                                    | none_decrease_wp_percent_life_level     | `10000` on client 3482                                                               |
| `accessible_region_group_keys+0x08` | i32                                    | none_decrease_wp_max_percent            | `330000` on client 3482, `300000` on client 1784                                     |
| `accessible_region_group_keys+0x0C` | u64                                    | pc_loot_authority_time                  | `90000` on client 3482                                                               |
| `accessible_region_group_keys+0x14` | u8                                     | pop_up_toggle                           | `1` on client 3482                                                                   |
| `accessible_region_group_keys+0x15` | bytes[90]                              | unknown_accessible_region_group_keys_15 | `76`, `180`, `2`, `600` and `1` among `0` bytes on client 3482; see Open Questions   |
| `accessible_region_group_keys+0x6F` | i32                                    | awakening_level                         | `47` on client 3482                                                                  |
| `accessible_region_group_keys+0x73` | i32                                    | reset_awakening_level                   | `49` on client 3482                                                                  |
| `accessible_region_group_keys+0x77` | u32                                    | pvp_condition_ref                       | Index into `strings`; `0` on client 3482, string `0`                                 |
| `accessible_region_group_keys+0x7B` | u8                                     | default_character_slot                  | `6` on client 3482                                                                   |
| `accessible_region_group_keys+0x7C` | u8                                     | character_slot_limit                    | `47` on client 3482, `26` on client 1784                                             |
| `accessible_region_group_keys+0x7D` | u8                                     | default_special_character_slot          | `3` on client 3482                                                                   |
| `accessible_region_group_keys+0x7E` | u8                                     | special_character_slot_limit            | `5` on client 3482                                                                   |
| `accessible_region_group_keys+0x7F` | u8[3]                                  | unknown_accessible_region_group_keys_7f | `1, 1, 1` on client 3482, `1` on client 1784                                         |
| `accessible_region_group_keys+0x82` | i32                                    | unknown_accessible_region_group_keys_82 | `3` on client 3482                                                                   |
| `accessible_region_group_keys+0x86` | i32                                    | penalty_index_in_desert                 | `2` on client 3482                                                                   |
| `accessible_region_group_keys+0x8A` | i32                                    | preemptive_attack_tendency              | `-3000` on client 3482; the sheet holds `0`                                          |
| `accessible_region_group_keys+0x8E` | i32                                    | preemptive_attack_ocean_tendency        | `-50000` on client 3482                                                              |
| `accessible_region_group_keys+0x92` | i32                                    | pk_tendency_penalty                     | `-1000` on client 3482                                                               |
| `accessible_region_group_keys+0x96` | u64                                    | preemptive_strike_keeping_time          | `30000` on client 3482                                                               |
| `accessible_region_group_keys+0x9E` | i64                                    | consume_guild_money_for_guild_war       | `0` on client 3482, `150000` on client 1784                                          |
| `accessible_region_group_keys+0xA6` | i64                                    | penalty_time_for_guild_war              | `0` on client 3482                                                                   |
| `accessible_region_group_keys+0xAE` | i64                                    | absence_time_for_change_guild_master    | `1296000` on client 3482                                                             |
| `accessible_region_group_keys+0xB6` | i32                                    | commission_rate_for_guild_duel          | `200000` on client 3482                                                              |
| `accessible_region_group_keys+0xBA` | u16                                    | daily_available_count_for_guild_duel    | `1` on client 3482                                                                   |

### Arena (variable: 68 bytes + region keys)

| Offset                                    | Type                                         | Field                                   | Notes                                                                                    |
| ----------------------------------------- | -------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------- |
| `+0x00`                                   | i16                                          | pve_arena_limited_quest_group           | `3722` on client 3482                                                                    |
| `+0x02`                                   | i16                                          | pve_arena_limited_quest_id              | `26` on client 3482                                                                      |
| `+0x04`                                   | u32                                          | pve_arena_can_teleport_region_key_count | Number of `pve_arena_can_teleport_region_keys`; `19` on client 3482, `11` on client 1784 |
| `+0x08`                                   | u16[pve_arena_can_teleport_region_key_count] | pve_arena_can_teleport_region_keys      | Region keys, `5` to `1444` on client 3482; the sheet's 11 keys on client 1784            |
| `pve_arena_can_teleport_region_keys+0x00` | u32                                          | pve_arena_region_key_count              | Number of `pve_arena_region_keys`; `2` on client 3482                                    |
| `pve_arena_can_teleport_region_keys+0x04` | u16[pve_arena_region_key_count]              | pve_arena_region_keys                   | `950, 1070` on client 3482; region keys                                                  |
| `pve_arena_region_keys+0x00`              | f32[3]                                       | pvp_arena_return_position               | `140974, -763, 347416` on client 3482                                                    |
| `pve_arena_region_keys+0x0C`              | u64                                          | pvp_arena_battle_time                   | `180000` on client 3482                                                                  |
| `pve_arena_region_keys+0x14`              | f32[3]                                       | play_ground_enter_position              | `138476, 357, 337361` on client 3482                                                     |
| `pve_arena_region_keys+0x20`              | f32[3]                                       | pvp_arena_champion_position             | `137989, -1003, 345971` on client 3482                                                   |
| `pve_arena_region_keys+0x2C`              | f32[3]                                       | pvp_arena_challenger_position           | `137800, -1000, 347949` on client 3482                                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                         |
| ------- | ------------------ | ------------ | ------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `21` on client 3482, `1579` on client 1784 |
| `+0x04` | pstr[string_count] | strings      | Every `*_ref` field is an index into `strings`                |

## Layout 5

The Layout 6 head and runs without the Unknown Lists block. The record past
the `MovementVerifyOption` run is one byte run here.

### File Layout

| Offset                   | Type                   | Field                                    | Notes                                                                 |
| ------------------------ | ---------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`                  | char[4]                | magic                                    | ASCII `PABR`                                                          |
| `+0x04`                  | bytes[36]              | unknown_04                               | All `0` on client 3454                                                |
| `+0x28`                  | i64                    | inn_rental_time                          | `216000` on client 3454                                               |
| `+0x30`                  | i16                    | inn_room_service_time                    | `1` on client 3454                                                    |
| `+0x32`                  | bytes[10]              | unknown_32                               | All `0` on client 3454                                                |
| `+0x3C`                  | u32                    | summon_monster_count_limit               | `10` on client 3454                                                   |
| `+0x40`                  | f32                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 3454                                                 |
| `+0x44`                  | i32                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 3454                                                 |
| `+0x48`                  | bytes[13]              | unknown_48                               | As in Layout 6                                                        |
| `+0x55`                  | u64                    | saving_buff_time                         | `10000` on client 3454                                                |
| `+0x5D`                  | u64                    | saving_cool_time                         | `60000` on client 3454                                                |
| `+0x65`                  | bytes[24]              | unknown_65                               | All `0` on client 3454                                                |
| `+0x7D`                  | u8                     | authentic_password_limit                 | `3` on client 3454                                                    |
| `+0x7E`                  | u8                     | password_length_min                      | `6` on client 3454                                                    |
| `+0x7F`                  | u8                     | password_length_max                      | `12` on client 3454                                                   |
| `+0x80`                  | u32                    | revival_product_no                       | `5017` on client 3454                                                 |
| `+0x84`                  | u64                    | rescue_cool_time                         | `1800000` on client 3454                                              |
| `+0x8C`                  | u32                    | final_level_up_condition_ref             | Index into `strings`                                                  |
| `+0x90`                  | u64                    | mail_remain_time                         | `864000` on client 3454                                               |
| `+0x98`                  | u64                    | unknown_98                               | `259200` on client 3454                                               |
| `+0xA0`                  | i64                    | reset_awakening_need_exp                 | `31000000` on client 3454                                             |
| `+0xA8`                  | u8                     | expired_tent_check_day                   | `28` on client 3454                                                   |
| `+0xA9`                  | bytes[20]              | unknown_a9                               | All `0` on client 3454                                                |
| `+0xBD`                  | i32                    | attack_to_servant_rate                   | `100000` on client 3454                                               |
| `+0xC1`                  | u32                    | re_awakening_item_key                    | Item key; `44195` on client 3454                                      |
| `+0xC5`                  | bytes[48000]           | unknown_c5                               | As in Layout 6                                                        |
| `+0xBC45`                | Servant Option         | servant_option                           | The `ServantOption` run                                               |
| `servant_option+0x00`    | Movement Verify Option | movement_verify_option                   | The `MovementVerifyOption` run                                        |
| `servant_option+0x72`    | bytes[73814]           | unknown_servant_option_72                | The rest of the record up to the string table; see Runs Past the Head |
| `servant_option+0x120C8` | String Table           | string_table                             | See String Table                                                      |
| `EOF-0x08`               | u32                    | table_start                              | Offset of the string table                                            |
| `EOF-0x04`               | u32                    | zero                                     | Always `0`                                                            |

## Layout 4

The Layout 5 head with `percent_damage_pv_rate` after
`summon_monster_count_limit`, and twenty-six arrays in `unknown_c5`.

### File Layout

| Offset                   | Type                   | Field                                    | Notes                                                                 |
| ------------------------ | ---------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`                  | char[4]                | magic                                    | ASCII `PABR`                                                          |
| `+0x04`                  | bytes[36]              | unknown_04                               | All `0` on client 3002                                                |
| `+0x28`                  | i64                    | inn_rental_time                          | `216000` on client 3002                                               |
| `+0x30`                  | i16                    | inn_room_service_time                    | `1` on client 3002                                                    |
| `+0x32`                  | bytes[10]              | unknown_32                               | All `0` on client 3002                                                |
| `+0x3C`                  | u32                    | summon_monster_count_limit               | `10` on client 3002                                                   |
| `+0x40`                  | i32                    | percent_damage_pv_rate                   | `3200` on client 3002                                                 |
| `+0x44`                  | f32                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 3002                                                 |
| `+0x48`                  | i32                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 3002                                                 |
| `+0x4C`                  | bytes[13]              | unknown_48                               | A u32 `100000` among `0` bytes on client 3002                         |
| `+0x59`                  | u64                    | saving_buff_time                         | `10000` on client 3002                                                |
| `+0x61`                  | u64                    | saving_cool_time                         | `60000` on client 3002                                                |
| `+0x69`                  | bytes[24]              | unknown_65                               | All `0` on client 3002                                                |
| `+0x81`                  | u8                     | authentic_password_limit                 | `3` on client 3002                                                    |
| `+0x82`                  | u8                     | password_length_min                      | `6` on client 3002                                                    |
| `+0x83`                  | u8                     | password_length_max                      | `12` on client 3002                                                   |
| `+0x84`                  | u32                    | revival_product_no                       | `5017` on client 3002                                                 |
| `+0x88`                  | u64                    | rescue_cool_time                         | `1800000` on client 3002                                              |
| `+0x90`                  | u32                    | final_level_up_condition_ref             | Index into `strings`                                                  |
| `+0x94`                  | u64                    | mail_remain_time                         | `864000` on client 3002                                               |
| `+0x9C`                  | u64                    | unknown_98                               | `259200` on client 3002                                               |
| `+0xA4`                  | i64                    | reset_awakening_need_exp                 | `31000000` on client 3002                                             |
| `+0xAC`                  | u8                     | expired_tent_check_day                   | `14` on client 3002                                                   |
| `+0xAD`                  | bytes[20]              | unknown_a9                               | All `0` on client 3002                                                |
| `+0xC1`                  | i32                    | attack_to_servant_rate                   | `100000` on client 3002                                               |
| `+0xC5`                  | u32                    | re_awakening_item_key                    | Item key; `44195` on client 3002                                      |
| `+0xC9`                  | bytes[104000]          | unknown_c5                               | Twenty-six arrays of 1000 4-byte values                               |
| `+0x19709`               | Servant Option         | servant_option                           | The `ServantOption` run                                               |
| `servant_option+0x00`    | Movement Verify Option | movement_verify_option                   | The `MovementVerifyOption` run                                        |
| `servant_option+0x72`    | bytes[105233]          | unknown_servant_option_72                | The rest of the record up to the string table; see Runs Past the Head |
| `servant_option+0x19B83` | String Table           | string_table                             | See String Table                                                      |
| `EOF-0x08`               | u32                    | table_start                              | Offset of the string table                                            |
| `EOF-0x04`               | u32                    | zero                                     | Always `0`                                                            |

## Layout 3

The Layout 1 head with `unknown_98` after `mail_remain_time` and the Layout
6 tail from `expired_tent_check_day` on. The `ServantOption` run has
`taming_item_key`.

### File Layout

| Offset                   | Type                   | Field                                    | Notes                                                                 |
| ------------------------ | ---------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`                  | char[4]                | magic                                    | ASCII `PABR`                                                          |
| `+0x04`                  | bytes[28]              | unknown_04                               | All `0` on client 2736                                                |
| `+0x20`                  | i64                    | inn_rental_time                          | `216000` on client 2736                                               |
| `+0x28`                  | i16                    | inn_room_service_time                    | `1` on client 2736                                                    |
| `+0x2A`                  | bytes[12]              | unknown_32                               | A u64 `1` and a u32 `0` on client 2736                                |
| `+0x36`                  | u32                    | summon_monster_count_limit               | `10` on client 2736                                                   |
| `+0x3A`                  | i32                    | percent_damage_pv_rate                   | `3200` on client 2736                                                 |
| `+0x3E`                  | f32                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 2736                                                 |
| `+0x42`                  | i32                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 2736                                                 |
| `+0x46`                  | i32                    | max_local_war_player                     | `30` on client 2736                                                   |
| `+0x4A`                  | bytes[13]              | unknown_48                               | A u32 `100000` among `0` bytes on client 2736                         |
| `+0x57`                  | u64                    | saving_buff_time                         | `10000` on client 2736                                                |
| `+0x5F`                  | u64                    | saving_cool_time                         | `60000` on client 2736                                                |
| `+0x67`                  | bytes[24]              | unknown_65                               | All `0` on client 2736                                                |
| `+0x7F`                  | u8                     | authentic_password_limit                 | `3` on client 2736                                                    |
| `+0x80`                  | u8                     | password_length_min                      | `6` on client 2736                                                    |
| `+0x81`                  | u8                     | password_length_max                      | `12` on client 2736                                                   |
| `+0x82`                  | u32                    | revival_product_no                       | `5017` on client 2736                                                 |
| `+0x86`                  | u64                    | rescue_cool_time                         | `1800000` on client 2736                                              |
| `+0x8E`                  | u32                    | final_level_up_condition_ref             | Index into `strings`                                                  |
| `+0x92`                  | u64                    | mail_remain_time                         | `864000` on client 2736                                               |
| `+0x9A`                  | u64                    | unknown_98                               | `259200` on client 2736                                               |
| `+0xA2`                  | i64                    | reset_awakening_need_exp                 | `31000000` on client 2736                                             |
| `+0xAA`                  | bytes[4]               | unknown_after_reset_awakening_need_exp   | All `0` on client 2736                                                |
| `+0xAE`                  | u8                     | expired_tent_check_day                   | `14` on client 2736                                                   |
| `+0xAF`                  | bytes[20]              | unknown_a9                               | All `0` on client 2736                                                |
| `+0xC3`                  | i32                    | attack_to_servant_rate                   | `100000` on client 2736                                               |
| `+0xC7`                  | u32                    | re_awakening_item_key                    | Item key; `44195` on client 2736                                      |
| `+0xCB`                  | bytes[56000]           | unknown_c5                               | Fourteen arrays of 1000 4-byte values                                 |
| `+0xDB8B`                | Servant Option         | servant_option                           | The `ServantOption` run                                               |
| `servant_option+0x00`    | Movement Verify Option | movement_verify_option                   | The `MovementVerifyOption` run                                        |
| `servant_option+0x72`    | bytes[261605]          | unknown_servant_option_72                | The rest of the record up to the string table; see Runs Past the Head |
| `servant_option+0x3FE57` | String Table           | string_table                             | See String Table                                                      |
| `EOF-0x08`               | u32                    | table_start                              | Offset of the string table                                            |
| `EOF-0x04`               | u32                    | zero                                     | Always `0`                                                            |

### Servant Option (variable: 354 bytes + revive costs)

| Offset              | Type                   | Field                                               | Notes                                                                                |
| ------------------- | ---------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`             | u64                    | mating_time                                         | `8640` on client 2736; the sheet's `8640000` divided by 1000                         |
| `+0x08`             | u64                    | mating_regist_time                                  | `43200000` on client 2736                                                            |
| `+0x10`             | i32                    | taming_rate                                         | `300000` on client 2736                                                              |
| `+0x14`             | i32                    | taming_value                                        | `1000000` on client 2736                                                             |
| `+0x18`             | u32                    | taming_item_key                                     | Item key; `54003` (Lump of Raw Sugar) on client 2736                                 |
| `+0x1C`             | u32                    | elephant_taming_item_key                            | Item key; `54019` ([Guild] Desert Peanut) on client 2736                             |
| `+0x20`             | i32                    | elephant_taming_value                               | `100000` on client 2736                                                              |
| `+0x24`             | i32                    | elephant_taming_rate                                | `50000` on client 2736                                                               |
| `+0x28`             | i32                    | elephant_taming_fail_rate                           | `150000` on client 2736                                                              |
| `+0x2C`             | i32                    | taming_max_level                                    | `10` on client 2736                                                                  |
| `+0x30`             | u64                    | market_regist_time                                  | `0` on client 2736                                                                   |
| `+0x38`             | i64                    | vehicle_seal_cost                                   | `1000` on client 2736                                                                |
| `+0x40`             | i64                    | vehicle_recovery_cost                               | `500` on client 2736                                                                 |
| `+0x48`             | i32                    | vehicle_mating_mp                                   | `1000000` on client 2736                                                             |
| `+0x4C`             | i64                    | vehicle_sell_cost                                   | `20` on client 2736                                                                  |
| `+0x54`             | i64                    | vehicle_emission_experience                         | `255` on client 2736                                                                 |
| `+0x5C`             | i16                    | stable_slot_limit                                   | `3` on client 2736                                                                   |
| `+0x5E`             | i32                    | discount_percent_for_servant_mating_place           | `700000` on client 2736                                                              |
| `+0x62`             | i32                    | discount_percent_for_servant_imprint                | `300000` on client 2736                                                              |
| `+0x66`             | i64                    | taming_life_experience                              | `15300` on client 2736                                                               |
| `+0x6E`             | i64                    | vehicle_level_up_life_experience                    | `17` on client 2736                                                                  |
| `+0x76`             | i64                    | register_delay_from_mating                          | `0` on client 2736                                                                   |
| `+0x7E`             | i64                    | register_delay_from_market                          | `0` on client 2736                                                                   |
| `+0x86`             | i64                    | vehicle_self_mating_price                           | `35000` on client 2736                                                               |
| `+0x8E`             | f32                    | vehicle_add_exp_by_training                         | `1.5` on client 2736                                                                 |
| `+0x92`             | i32                    | vehicle_add_taming_by_training                      | `3000` on client 2736                                                                |
| `+0x96`             | i32                    | vehicle_learn_skill_add_rate_from_imprint           | `100000` on client 2736                                                              |
| `+0x9A`             | f32                    | vehicle_seal_distance                               | `3000` on client 2736                                                                |
| `+0x9E`             | f32                    | idle_vehicle_seal_distance                          | `4000` on client 2736                                                                |
| `+0xA2`             | i64                    | idle_vehicle_seal_time                              | `3600` on client 2736                                                                |
| `+0xAA`             | i32                    | vehicle_decrease_cost_by_mating_count               | `250000` on client 2736                                                              |
| `+0xAE`             | i32                    | vehicle_decrease_cost_by_mating_clear               | `150000` on client 2736                                                              |
| `+0xB2`             | i32                    | vehicle_decrease_cost_by_dead_clear                 | `50000` on client 2736                                                               |
| `+0xB6`             | i32                    | vehicle_learn_skill_by_level                        | `0` on client 2736                                                                   |
| `+0xBA`             | i32                    | vehicle_skill_change_value                          | `250000` on client 2736                                                              |
| `+0xBE`             | i32                    | vehicle_min_price                                   | `0` on client 2736                                                                   |
| `+0xC2`             | i32                    | vehicle_max_price                                   | `0` on client 2736                                                                   |
| `+0xC6`             | i32                    | vehicle_change_form_with_skill_rate                 | `300000` on client 2736                                                              |
| `+0xCA`             | i64                    | vehicle_change_form_with_skill_vary_experience      | `200000` on client 2736                                                              |
| `+0xD2`             | i32                    | vehicle_register_price_rate                         | `300000` on client 2736                                                              |
| `+0xD6`             | i64                    | skill_exp_training_time                             | `3600` on client 2736 (the sheet's `3600000` divided by 1000)                        |
| `+0xDE`             | i64                    | stallion_skill_exp_training_time                    | `0` on client 2736                                                                   |
| `+0xE6`             | u32                    | exchange_elephant_item                              | Item key; `9916` ([Guild] Baby Elephant) on client 2736                              |
| `+0xEA`             | i32                    | down_grade_from_dead_count                          | `5000` on client 2736                                                                |
| `+0xEE`             | u64                    | unseal_delay_time                                   | `300000` on client 2736                                                              |
| `+0xF6`             | f32                    | pc_room_whistle_distance                            | `30000` on client 2736                                                               |
| `+0xFA`             | i32                    | pc_room_whistle_type                                | `15` on client 2736                                                                  |
| `+0xFE`             | i32                    | add_percent_for_stallion_market_price               | `1700000` on client 2736                                                             |
| `+0x102`            | i32                    | add_percent_for_stallion_mating_market_price        | `1700000` on client 2736                                                             |
| `+0x106`            | i32                    | stallion_child_base_skill_add_rate                  | `500000` on client 2736                                                              |
| `+0x10A`            | i32                    | stallion_training_complete_required_experience      | `60000` on client 2736                                                               |
| `+0x10E`            | i32                    | nine_tier_horse_acquisition_rate                    | `0` on client 2736                                                                   |
| `+0x112`            | i32                    | stallion_training_skill_default_rate                | `300000` on client 2736                                                              |
| `+0x116`            | i32                    | stallion_training_skill_add_rate                    | `100000` on client 2736                                                              |
| `+0x11A`            | u32                    | stallion_training_complete_required_item            | Item key; `50801` (Krogdalo's Origin Stone) on client 2736                           |
| `+0x11E`            | i64                    | stallion_training_complete_required_item_count      | `1` on client 2736                                                                   |
| `+0x126`            | u32                    | prevent_stallion_training_skill_exp_down_item       | Item key; `16080` (Cron Stone) on client 2736                                        |
| `+0x12A`            | i64                    | prevent_stallion_training_skill_exp_down_item_count | `100` on client 2736                                                                 |
| `+0x132`            | i32                    | prevent_stallion_training_skill_exp_down_item_rate  | `500000` on client 2736                                                              |
| `+0x136`            | u64                    | revive_cost_count                                   | Number of `revive_costs`; `10` on client 2736                                        |
| `+0x13E`            | i64[revive_cost_count] | revive_costs                                        | `100000, 2000, 4000, 7000, 10000, 15000, 20000, 25000, 35000, 100000` on client 2736 |
| `revive_costs+0x00` | i64                    | clear_guild_servant_dead_count_cost                 | `100000000` on client 2736                                                           |
| `revive_costs+0x08` | u64                    | unknown_revive_costs_08                             | `300000000` on client 2736                                                           |
| `revive_costs+0x10` | u32                    | fantasy_upgrade_need_item_key                       | Item key; `757008` (Mythical Censer) on client 2736                                  |
| `revive_costs+0x14` | i64                    | fantasy_upgrade_item_max_count                      | `1` on client 2736                                                                   |
| `revive_costs+0x1C` | i32                    | fantasy_upgrade_item_success_rate                   | `3` on client 2736                                                                   |
| `revive_costs+0x20` | i32                    | fantasy_upgrade_max_success_rate                    | `30000` on client 2736                                                               |

## Layout 2

The Layout 3 head with `siege_bonus_damage_rate` still between
`expired_tent_check_day` and `attack_to_servant_rate`, as in Layout 1.

### File Layout

| Offset                   | Type                   | Field                                    | Notes                                                                 |
| ------------------------ | ---------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`                  | char[4]                | magic                                    | ASCII `PABR`                                                          |
| `+0x04`                  | bytes[28]              | unknown_04                               | All `0` on client 2414                                                |
| `+0x20`                  | i64                    | inn_rental_time                          | `216000` on client 2414                                               |
| `+0x28`                  | i16                    | inn_room_service_time                    | `1` on client 2414                                                    |
| `+0x2A`                  | bytes[12]              | unknown_32                               | A u64 `1` and a u32 `0` on client 2414                                |
| `+0x36`                  | u32                    | summon_monster_count_limit               | `10` on client 2414                                                   |
| `+0x3A`                  | i32                    | percent_damage_pv_rate                   | `3200` on client 2414                                                 |
| `+0x3E`                  | f32                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 2414                                                 |
| `+0x42`                  | i32                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 2414                                                 |
| `+0x46`                  | i32                    | max_local_war_player                     | `30` on client 2414                                                   |
| `+0x4A`                  | bytes[13]              | unknown_48                               | A u32 `100000` among `0` bytes on client 2414                         |
| `+0x57`                  | u64                    | saving_buff_time                         | `10000` on client 2414                                                |
| `+0x5F`                  | u64                    | saving_cool_time                         | `60000` on client 2414                                                |
| `+0x67`                  | bytes[24]              | unknown_65                               | All `0` on client 2414                                                |
| `+0x7F`                  | u8                     | authentic_password_limit                 | `3` on client 2414                                                    |
| `+0x80`                  | u8                     | password_length_min                      | `6` on client 2414                                                    |
| `+0x81`                  | u8                     | password_length_max                      | `12` on client 2414                                                   |
| `+0x82`                  | u32                    | revival_product_no                       | `5017` on client 2414                                                 |
| `+0x86`                  | u64                    | rescue_cool_time                         | `1800000` on client 2414                                              |
| `+0x8E`                  | u32                    | final_level_up_condition_ref             | Index into `strings`                                                  |
| `+0x92`                  | u64                    | mail_remain_time                         | `864000` on client 2414                                               |
| `+0x9A`                  | u64                    | unknown_98                               | `259200` on client 2414                                               |
| `+0xA2`                  | i64                    | reset_awakening_need_exp                 | `31000000` on client 2414                                             |
| `+0xAA`                  | bytes[4]               | unknown_after_reset_awakening_need_exp   | All `0` on client 2414                                                |
| `+0xAE`                  | u8                     | expired_tent_check_day                   | `14` on client 2414                                                   |
| `+0xAF`                  | bytes[12]              | unknown_a9                               | All `0` on client 2414                                                |
| `+0xBB`                  | i32                    | siege_bonus_damage_rate                  | `500000` on client 2414                                               |
| `+0xBF`                  | bytes[8]               | unknown_after_siege_bonus_damage_rate    | All `0` on client 2414                                                |
| `+0xC7`                  | i32                    | attack_to_servant_rate                   | `100000` on client 2414                                               |
| `+0xCB`                  | u32                    | re_awakening_item_key                    | Item key; `44195` on client 2414                                      |
| `+0xCF`                  | bytes[56000]           | unknown_c5                               | Fourteen arrays of 1000 4-byte values                                 |
| `+0xDB8F`                | Servant Option         | servant_option                           | The `ServantOption` run                                               |
| `servant_option+0x00`    | Movement Verify Option | movement_verify_option                   | The `MovementVerifyOption` run                                        |
| `servant_option+0x72`    | bytes[260286]          | unknown_servant_option_72                | The rest of the record up to the string table; see Runs Past the Head |
| `servant_option+0x3F930` | String Table           | string_table                             | See String Table                                                      |
| `EOF-0x08`               | u32                    | table_start                              | Offset of the string table                                            |
| `EOF-0x04`               | u32                    | zero                                     | Always `0`                                                            |

## Layout 1

The head of client 1784: `unknown_04` is 28 bytes, `unknown_32` 12 bytes,
`percent_damage_pv_rate`, `max_local_war_player` and
`siege_bonus_damage_rate` are still in it, `unknown_98` is not, and 4 bytes
sit between `reset_awakening_need_exp` and `expired_tent_check_day`. The
`ServantOption` run has `taming_item_key` and no
`unknown_revive_costs_08`.

### File Layout

| Offset                   | Type                   | Field                                    | Notes                                                                 |
| ------------------------ | ---------------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`                  | char[4]                | magic                                    | ASCII `PABR`                                                          |
| `+0x04`                  | bytes[28]              | unknown_04                               | All `0` on client 1784                                                |
| `+0x20`                  | i64                    | inn_rental_time                          | `216000` on client 1784                                               |
| `+0x28`                  | i16                    | inn_room_service_time                    | `1` on client 1784                                                    |
| `+0x2A`                  | bytes[12]              | unknown_32                               | A u64 `1` and a u32 `0` on client 1784; see Open Questions            |
| `+0x36`                  | u32                    | summon_monster_count_limit               | `10` on client 1784                                                   |
| `+0x3A`                  | i32                    | percent_damage_pv_rate                   | `3200` on client 1784                                                 |
| `+0x3E`                  | f32                    | max_decreasable_hp_by_damage_rate_module | `2000` on client 1784                                                 |
| `+0x42`                  | i32                    | max_decreasable_mp_by_damage_rate_module | `1500` on client 1784                                                 |
| `+0x46`                  | i32                    | max_local_war_player                     | `30` on client 1784                                                   |
| `+0x4A`                  | bytes[13]              | unknown_48                               | All `0` on client 1784                                                |
| `+0x57`                  | u64                    | saving_buff_time                         | `10000` on client 1784                                                |
| `+0x5F`                  | u64                    | saving_cool_time                         | `60000` on client 1784                                                |
| `+0x67`                  | bytes[24]              | unknown_65                               | All `0` on client 1784                                                |
| `+0x7F`                  | u8                     | authentic_password_limit                 | `3` on client 1784                                                    |
| `+0x80`                  | u8                     | password_length_min                      | `6` on client 1784                                                    |
| `+0x81`                  | u8                     | password_length_max                      | `12` on client 1784                                                   |
| `+0x82`                  | u32                    | revival_product_no                       | `5017` on client 1784                                                 |
| `+0x86`                  | u64                    | rescue_cool_time                         | `1800000` on client 1784                                              |
| `+0x8E`                  | u32                    | final_level_up_condition_ref             | String `0` (`"0"`) on client 1784                                     |
| `+0x92`                  | u64                    | mail_remain_time                         | `864000` on client 1784                                               |
| `+0x9A`                  | i64                    | reset_awakening_need_exp                 | `31000000` on client 1784                                             |
| `+0xA2`                  | bytes[4]               | unknown_after_reset_awakening_need_exp   | All `0` on client 1784                                                |
| `+0xA6`                  | u8                     | expired_tent_check_day                   | `7` on client 1784                                                    |
| `+0xA7`                  | bytes[12]              | unknown_a9                               | All `0` on client 1784                                                |
| `+0xB3`                  | i32                    | siege_bonus_damage_rate                  | `500000` on client 1784                                               |
| `+0xB7`                  | bytes[8]               | unknown_after_siege_bonus_damage_rate    | All `0` on client 1784                                                |
| `+0xBF`                  | i32                    | attack_to_servant_rate                   | `100000` on client 1784                                               |
| `+0xC3`                  | u32                    | re_awakening_item_key                    | `44195` on client 1784                                                |
| `+0xC7`                  | bytes[56000]           | unknown_c5                               | Fourteen arrays of 1000 4-byte values                                 |
| `+0xDB87`                | Servant Option         | servant_option                           | The `ServantOption` run                                               |
| `servant_option+0x00`    | Movement Verify Option | movement_verify_option                   | The `MovementVerifyOption` run                                        |
| `servant_option+0x72`    | bytes[252875]          | unknown_servant_option_72                | The rest of the record up to the string table; see Runs Past the Head |
| `servant_option+0x3DC3D` | String Table           | string_table                             | See String Table                                                      |
| `EOF-0x08`               | u32                    | table_start                              | Offset of the string table                                            |
| `EOF-0x04`               | u32                    | zero                                     | Always `0`                                                            |

### Servant Option (variable: 346 bytes + revive costs)

| Offset              | Type                   | Field                                               | Notes                                                                                |
| ------------------- | ---------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`             | u64                    | mating_time                                         | `8640` on client 1784; the sheet's `8640000` divided by 1000                         |
| `+0x08`             | u64                    | mating_regist_time                                  | `43200000` on client 1784                                                            |
| `+0x10`             | i32                    | taming_rate                                         | `300000` on client 1784                                                              |
| `+0x14`             | i32                    | taming_value                                        | `200000` on client 1784                                                              |
| `+0x18`             | u32                    | taming_item_key                                     | Item key; `54003` (Lump of Raw Sugar) on client 1784                                 |
| `+0x1C`             | u32                    | elephant_taming_item_key                            | Item key; `54019` ([Guild] Desert Peanut) on client 1784                             |
| `+0x20`             | i32                    | elephant_taming_value                               | `100000` on client 1784                                                              |
| `+0x24`             | i32                    | elephant_taming_rate                                | `50000` on client 1784                                                               |
| `+0x28`             | i32                    | elephant_taming_fail_rate                           | `150000` on client 1784                                                              |
| `+0x2C`             | i32                    | taming_max_level                                    | `10` on client 1784                                                                  |
| `+0x30`             | u64                    | market_regist_time                                  | `0` on client 1784                                                                   |
| `+0x38`             | i64                    | vehicle_seal_cost                                   | `1000` on client 1784                                                                |
| `+0x40`             | i64                    | vehicle_recovery_cost                               | `500` on client 1784                                                                 |
| `+0x48`             | i32                    | vehicle_mating_mp                                   | `1000000` on client 1784                                                             |
| `+0x4C`             | i64                    | vehicle_sell_cost                                   | `20` on client 1784                                                                  |
| `+0x54`             | i64                    | vehicle_emission_experience                         | `255` on client 1784                                                                 |
| `+0x5C`             | i16                    | stable_slot_limit                                   | `3` on client 1784                                                                   |
| `+0x5E`             | i32                    | discount_percent_for_servant_mating_place           | `700000` on client 1784                                                              |
| `+0x62`             | i32                    | discount_percent_for_servant_imprint                | `300000` on client 1784                                                              |
| `+0x66`             | i64                    | taming_life_experience                              | `15300` on client 1784                                                               |
| `+0x6E`             | i64                    | vehicle_level_up_life_experience                    | `17` on client 1784                                                                  |
| `+0x76`             | i64                    | register_delay_from_mating                          | `0` on client 1784                                                                   |
| `+0x7E`             | i64                    | register_delay_from_market                          | `0` on client 1784                                                                   |
| `+0x86`             | i64                    | vehicle_self_mating_price                           | `35000` on client 1784                                                               |
| `+0x8E`             | f32                    | vehicle_add_exp_by_training                         | `1.5` on client 1784                                                                 |
| `+0x92`             | i32                    | vehicle_add_taming_by_training                      | `3000` on client 1784                                                                |
| `+0x96`             | i32                    | vehicle_learn_skill_add_rate_from_imprint           | `100000` on client 1784                                                              |
| `+0x9A`             | f32                    | vehicle_seal_distance                               | `3000` on client 1784                                                                |
| `+0x9E`             | f32                    | idle_vehicle_seal_distance                          | `4000` on client 1784                                                                |
| `+0xA2`             | i64                    | idle_vehicle_seal_time                              | `7200` on client 1784                                                                |
| `+0xAA`             | i32                    | vehicle_decrease_cost_by_mating_count               | `250000` on client 1784                                                              |
| `+0xAE`             | i32                    | vehicle_decrease_cost_by_mating_clear               | `150000` on client 1784                                                              |
| `+0xB2`             | i32                    | vehicle_decrease_cost_by_dead_clear                 | `50000` on client 1784                                                               |
| `+0xB6`             | i32                    | vehicle_learn_skill_by_level                        | `50000` on client 1784                                                               |
| `+0xBA`             | i32                    | vehicle_skill_change_value                          | `250000` on client 1784                                                              |
| `+0xBE`             | i32                    | vehicle_min_price                                   | `0` on client 1784                                                                   |
| `+0xC2`             | i32                    | vehicle_max_price                                   | `0` on client 1784                                                                   |
| `+0xC6`             | i32                    | vehicle_change_form_with_skill_rate                 | `300000` on client 1784                                                              |
| `+0xCA`             | i64                    | vehicle_change_form_with_skill_vary_experience      | `200000` on client 1784                                                              |
| `+0xD2`             | i32                    | vehicle_register_price_rate                         | `300000` on client 1784                                                              |
| `+0xD6`             | i64                    | skill_exp_training_time                             | `3600` on client 1784 (the sheet's `3600000` divided by 1000)                        |
| `+0xDE`             | i64                    | stallion_skill_exp_training_time                    | `0` on client 1784                                                                   |
| `+0xE6`             | u32                    | exchange_elephant_item                              | Item key; `9916` ([Guild] Baby Elephant) on client 1784                              |
| `+0xEA`             | i32                    | down_grade_from_dead_count                          | `5000` on client 1784                                                                |
| `+0xEE`             | u64                    | unseal_delay_time                                   | `300000` on client 1784                                                              |
| `+0xF6`             | f32                    | pc_room_whistle_distance                            | `30000` on client 1784                                                               |
| `+0xFA`             | i32                    | pc_room_whistle_type                                | `15` on client 1784                                                                  |
| `+0xFE`             | i32                    | add_percent_for_stallion_market_price               | `2600000` on client 1784                                                             |
| `+0x102`            | i32                    | add_percent_for_stallion_mating_market_price        | `2600000` on client 1784                                                             |
| `+0x106`            | i32                    | stallion_child_base_skill_add_rate                  | `500000` on client 1784                                                              |
| `+0x10A`            | i32                    | stallion_training_complete_required_experience      | `60000` on client 1784                                                               |
| `+0x10E`            | i32                    | nine_tier_horse_acquisition_rate                    | `0` on client 1784                                                                   |
| `+0x112`            | i32                    | stallion_training_skill_default_rate                | `300000` on client 1784                                                              |
| `+0x116`            | i32                    | stallion_training_skill_add_rate                    | `100000` on client 1784                                                              |
| `+0x11A`            | u32                    | stallion_training_complete_required_item            | Item key; `50801` (Krogdalo's Origin Stone) on client 1784                           |
| `+0x11E`            | i64                    | stallion_training_complete_required_item_count      | `1` on client 1784                                                                   |
| `+0x126`            | u32                    | prevent_stallion_training_skill_exp_down_item       | Item key; `16080` (Cron Stone) on client 1784                                        |
| `+0x12A`            | i64                    | prevent_stallion_training_skill_exp_down_item_count | `100` on client 1784                                                                 |
| `+0x132`            | i32                    | prevent_stallion_training_skill_exp_down_item_rate  | `500000` on client 1784                                                              |
| `+0x136`            | u64                    | revive_cost_count                                   | Number of `revive_costs`; `10` on client 1784                                        |
| `+0x13E`            | i64[revive_cost_count] | revive_costs                                        | `100000, 2000, 4000, 7000, 10000, 15000, 20000, 25000, 35000, 100000` on client 1784 |
| `revive_costs+0x00` | i64                    | clear_guild_servant_dead_count_cost                 | `100000000` on client 1784                                                           |
| `revive_costs+0x08` | u32                    | fantasy_upgrade_need_item_key                       | Item key; `757008` (Mythical Censer) on client 1784                                  |
| `revive_costs+0x0C` | i64                    | fantasy_upgrade_item_max_count                      | `1` on client 1784                                                                   |
| `revive_costs+0x14` | i32                    | fantasy_upgrade_item_success_rate                   | `3` on client 1784                                                                   |
| `revive_costs+0x18` | i32                    | fantasy_upgrade_max_success_rate                    | `30000` on client 1784                                                               |

## Runs Past the Head

Where each structure of Layout 6 starts on clients 3482 and 1784. On client
1784 the runs after the Movement Verify Option are inside
`unknown_servant_option_72` of Layout 1.

| Structure              | Sheet                       | Client 3482 | Client 1784 |
| ---------------------- | --------------------------- | ----------- | ----------- |
| Unknown Lists          | -                           | `0xBC45`    | -           |
| Servant Option         | `ServantOption`             | `0xBCC9`    | `0xDB87`    |
| Movement Verify Option | `MovementVerifyOption`      | `0xBE77`    | `0xDD31`    |
| Etc Option             | `EtcOption`                 | `0xBEE9`    | `0xDDA3`    |
| Guild Option           | `GuildOption`               | `0xCBDE`    | `0x36BAE`   |
| Item Market            | `ItemMarket`                | `0xCCBA`    | `0x36CC5`   |
| Localizing Option      | `LocalizingOption`          | `0x13507`   | `0x3D3F0`   |
| Arena                  | `EtcOption`, `BattleOption` | `0x1CD3D`   | `0x4ADDE`   |

The Etc Option run of client 1784 differs from Layout 6's:

- `territory_trade_authority_auction_sale_time` (u64 `86400000`) follows
  `tendency_from_trade`.
- `normal_trade_drop_rate`, `smuggling_trade_drop_rate`,
  `territory_trade_drop_rate` (i32 each) and
  `territory_trade_authority_bidder_count` (i16) sit where Layout 6 has
  `unknown_9e` and `unknown_a2`, all `0`.
- `unknown_fe`, `unknown_12c` and `unknown_130` are not there.
- `pruning` and `catchbug` are u16.
- `localwar_item_rate` (`750000`), `localwar_item_key` (`450`, Red Seal)
  and `horserace_item_key` (`1001`, Horse Race Seal) come before
  `prevent_downgrade_item_key`.
- `user_chat_block_with_item` (`65208`, Deputy Token) follows
  `world_chat_item_keys`.
- `defence_pose_decrease_guard_rate` (`500000`),
  `defence_pose_decrease_damage_rate` (`800000`) and
  `balance_channel_decrease_damage_rate` (`1000000`) come before
  `comeback_standard_time`. Client 3002 still has them.

The Guild Option run of client 1784 has no
`unknown_king_or_lord_tent_attack_percents_28`, and 18 u32 `1` sit between
it and the Byte Int Pair list, which holds 17 pairs there. Its Localizing
Option run has `like_name_filter` (u8 `0`) and `bonus_dd_type` (i32 `1`)
where Layout 6 has `unknown_2c`, 86 bytes in place of
`unknown_accessible_region_group_keys_15`, and one u8 in place of
`unknown_accessible_region_group_keys_7f`. After
`daily_available_count_for_guild_duel` client 1784 goes on with
`installable_siege_tent_count` (`0`), the guild war continue values
(`0`, `5000`, `30000`, `86400`) and `GuildWarRetryTime` (`259200`); client
3482 holds `0` bytes there and then other values.

## Field Names

The names come from the one-row option sheets of a private server's
`DataSheets.bexcel` on client 1784 (`BattleOption`, `ServantOption`,
`MovementVerifyOption`, `EtcOption`, `GuildOption`, `ItemMarket`) and the
`LocalizingOption` row with `PA_GAME_SERVICE_TYPE` `8`, matched by value
against the client 1784 file, and from the loaders of that private server's
game server build on client 1784, which read the columns in the order the
file stores them. The private server's values are edited, so only the column
names carry over.

A field takes its column's name when its value on client 1784 equals the
sheet's. A field between two such fields takes the loader's column in read
order when the widths the loader reads fill the bytes between them exactly;
most of these hold `0` on client 1784, as the sheet does. Two of them hold
other values: `use_password` (`0`, the sheet `1`) and
`preemptive_attack_tendency` (`-3000`, the sheet `0`). Bytes where neither
rule holds are `unknown_<offset>`. Some values differ from the sheet's in a
fixed way:

- `mating_time` and `skill_exp_training_time` hold the sheet's milliseconds
  divided by 1000 (`8640000` and `3600000` on client 1784).
- `cheer_guild_buffs` holds each buff key times 65536 plus 1, as the loader
  stores it.
- `resist_desert` and `accessible_region_group_keys` hold the sheet's keys
  in ascending order.
- `alchemy_stone_up_grade_rate` holds the sheet's seven numbers of
  `AlchemyStoneUpGradeRate_1` and a `0`.
- The loader reads `keep_resist_time` from a column it picks at run time;
  the sheet's `KeepResistTime` and `KeepResistTime_GT` both hold `5000`, the
  file's value.
- `possible_classes` and the PVE arena region keys hold the sheet's lists
  on client 1784, `pve_arena_limited_quest_group` the sheet's `3722`.

The fields keep their name on client 3482 where the bytes around them line
up with the client 1784 file. `comeback_standard_time` lines up through
client 3002, which still has the three rates before it and holds `720`
there, as client 3482 does.

The named head fields follow the `BattleOption` loader's read order:
`InnRentalTime`, `InnRoomServiceTime`, `DecreaseDropRate`,
`SummonMonsterCountLimit`, `PersentDamegePvRate`,
`MaxDecreasableHpByDamageRateModule`, `MaxDecreasableMpByDamageRateModule`,
`MaxLocalWarPlayer`, then (after `GuildWareHouseSlotDefault`,
`MonsterPowerInNight`, `MonsterExperienceInNight` and `UseChannelInstance`)
`SavingBuffTime`, `SavingCoolTime`, `TradeSummaryInterval`,
`CollectSpawnPercentInServerBeginning`, `CollectAwakeDelay`,
`CollectSpawnPercentForDelay`, `AuthenticPasswordLimit`,
`PasswordLengthMin`, `PasswordLengthMax`, `RevivalProductNo`,
`RescueCoolTime`, `FinalLevelUpCondition`, `MailRemainTime`,
`ResetAwakeningNeedExp`, `SuperSkillBaseRate`, `ExpiredTentCheckDay`, six
rate columns with `SiegeBonusDamageRate` fourth, `AttackToServantRate` and
`ReAwakeningItemKey`. The loader multiplies `InnRentalTime` by 60 and
stores it as an i64, which is why the file holds `216000` for the sheet's
`3600`. The client 1784 file matches the sheet for every named head field:
`3600` (times 60), `1`, `10`, `3200`, `2000`, `1500`, `30`, `10000`,
`60000`, `3`, `6`, `12`, `5017`, `1800000`, `"0"`, `864000`, `31000000`,
`7`, `500000`, `100000` and `44195`. The 28 bytes of `unknown_04` on
client 1784 are as long as the five i32 and the u64 the loader reads before
`InnRentalTime` (`BackAttackDamageRate` to `SpeedAttackDamageRate`, then
`ActionRestrictionRemainTick`), all `0` in the sheet; on client 3482 the
block is 36 bytes, so the head keeps them unknown. `percent_damage_pv_rate`
is the column `PersentDamegePvRate`.

The arena values are the `EtcOption` columns `PVEArenaLimitedQuestGroup`,
`PVEArenaLimitedQuestID`, `PVEArenaCanTeleportRegionKey` and
`PVEArenaRegionKey`, then the `BattleOption` columns
`PvpArenaReturnPosition`, `PvpArenaBattleTime`, `PlayGroundEnterPosition`,
`PvpArenaChampionPosition` and `PvpArenaChallengerPosition`. In the loaders
they are far apart; the file keeps them together.

## Notes

- `unknown_c5` is arrays of 1000 4-byte values: twelve on clients 3454 and
  3482, fourteen on clients 1784 to 2736 and twenty-six on client 3002. On
  client 3482 the first array is f32 `0`, then `5` 40 times, `10` 30 times
  and on up; the last holds `300000` 1000 times. `unknown_etc_option_00` is
  seven arrays of 100 i32 (`50000`, `90000`, `120000`, `150000`, then
  `200000` and on).
- Each layout gives its unknown runs the sizes of the client it was written
  from: Layout 6 client 3482, Layout 5 client 3454, Layout 4 client 3002,
  Layout 3 client 2736, Layout 2 client 2414 and Layout 1 client 1784. The
  last run changes size with most patches, so a layout fits few clients. A
  last run up to `table_start` instead walks the zero bytes of other
  clients' records: with it the doc check put clients 805 to 3454 in the
  newest layouts, whatever their head.
- The handler (`_bss/gameoption/`) walks Layout 6 up to the end of the Item
  Market run and shows one row per named head and run field, with the sheet
  each comes from, item names for item keys, the strings of the `*_ref`
  fields and the cheer buff keys, then one row per string. Count fields,
  `unknown_*` fields and the rest of the record are only counted. When the
  runs do not walk (another client), it shows the head and says where the
  walk stopped.
- On client 3482, string `1` is `getLevel()<5`, the text of
  `EtcOption.TutorialCondition` (`tutorial_condition_ref`), and strings `18`
  and `19` are `checkPeriod(...)` conditions; the fields that point at them
  are in the unknown runs.

## Open Questions

### The Unknown Runs

`unknown_c5` and `unknown_etc_option_00` are arrays none of the loaders named
here fills (see Notes). Unknown Lists, first on client 3464, holds two lists of
the numbers `70` to `75` with the f32 `3` to `18`, the f32 `9`, `6`, `3`, `0`,
then `-3` and `0`. The Byte Int Pair list after the Guild Option run pairs
a number from `1` to `85` with `3`, `6` or `12`. `unknown_guild_option_04_53`
starts with a list of 11 i32 pairs (`1000000, 1000000` down to
`0, 300000`) and ends with 22 i32 where the `LocalizingOption` loader reads
its 22 experience and drop rate columns (`AquireItemDropRate` to
`TradingExpRateForQuest`): `1000000` 7 times, `0` 8 times and `1000000` 7
times on clients 1784 and 3482, where every sheet row holds `0`.
`unknown_localizing_option_00` and `unknown_arena_00` hold the rest of the
`LocalizingOption` and `EtcOption` loaders and other blocks. On client 1784
the `EtcOption` values from `TPitemKey` (`16001`, just before the arena
values) back to `SpecialCharacterLevel` do not line up with the loader.

### The Four f32 After `dyeing_combine_item`

`unknown_f2`, `unknown_f6` and `unknown_fa` hold `-0.4`, `120` and `1.8` on
clients 1784 and 3482, and `unknown_fe` `100` on client 3482. The
`EtcOption` sheet's `CampBottomScale`, `CampSlopeLimit`, `CampAreaScale` and
`CampSlopeLimitRelieve` hold `-0.2`, `120`, `1.3` and `80`, which the loader
reads much later; only `120` matches.

### Fields Added After Client 1784

Client 3482 holds fields client 1784 does not have: `unknown_revive_costs_08`
(`300000000`, from client 2384 on; client 2378 does not have it),
`unknown_king_or_lord_tent_attack_percents_28` (`1`), `unknown_9e` and
`unknown_a2` (`1000000`, `500000`), `unknown_12c` and `unknown_130` (`5000`,
`2000000`) and `unknown_fe`. No column of the private server's sheets holds
these values next to the fields around them.

### The Unknown Fields Inside the Runs

`unknown_6c` and `unknown_70` sit where the `EtcOption` loader reads
`WorkingTrashExchangeKeyList` (a list of 12 keys in the sheet) and
`WeakenItemRateInSiege`; client 1784 holds 8 `0` bytes there, so the list's
form is open. `unknown_add_resist_values_20` to `_28` sit where the loader
reads only `DecreaseMaxEnduranceToUpgradeItem` (i16). In the Localizing
Option run, `unknown_37` sits where the loader reads `ContentsServiceType`
(an i32), `unknown_possible_classes_00` is a count of `0` where the sheet
has `PossibleSpecialCharacterClass` filled and `CustomizeOnlyClass` empty,
and `unknown_accessible_region_group_keys_7f` and `_82` sit where the loader
reads `DeathPenaltyType` and `PenaltyIndex` (two i32).

### The Zero Blocks of the Head

`unknown_04`, `unknown_48`, `unknown_65` and `unknown_a9` sit where the
`BattleOption` loader reads columns that are `0` in the sheet, so no value
confirms them. `unknown_04` grows from 28 bytes (client 1784) to 36 (client
3482), so 8 bytes were inserted in it. `unknown_32` sits where the loader
reads `DecreaseDropRate`: on client 1784 a u64 `1` and a u32 `0`, which
reads as a counted list holding the sheet's one value `0`; on client 3482
it is 10 zero bytes, which a u64 count of `0` and two more bytes would
explain. On client 3482 `unknown_48` holds `1500000` and `100000`, where
client 1784 has zero bytes.

### `unknown_98`

A u64 `259200` between `mail_remain_time` and `reset_awakening_need_exp`,
from Layout 2 on. No `BattleOption` or `EtcOption` column holds that value;
`LocalizingOption.GuildWarRetryTime` does (`259200` on client 1784), which
the `LocalizingOption` run of client 1784 also holds.
