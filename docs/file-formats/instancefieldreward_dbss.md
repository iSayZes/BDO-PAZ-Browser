# `instancefieldreward.dbss` Format

## Purpose

The rewards of an instance dungeon: per dungeon number a skill to learn,
five reward item groups (`itemmaingroup.bss` keys, one per grade), three
push item slots and a list of related regions. On client 3474 the file has
2 rows, dungeons `199` and `291`, both with the item groups `56001` to
`56005`; `291` lists the regions Moretti Plantation (`62`), Lynch Farm
Ruins (`63`) and Glish Swamp (`37`). Companion
`instancefieldrewardoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------------ | --------- |
| 2      | 2726 and later | 3483    | `instancefieldreward.dbss`       | 154   | 6 Push Item, 2 Row | 12        |
| 2      | 2726 and later | 3483    | `instancefieldrewardoffset.dbss` | 24    | 2 Offset Row       | 10        |
| 1      | 1346 to 2717   | 2717    | `instancefieldreward.dbss`       | 134   | 6 Push Item, 2 Row | 12        |
| 1      | 1346 to 2717   | 2717    | `instancefieldrewardoffset.dbss` | 24    | 2 Offset Row       | 10        |

| Layout | File                             | Known         | Unknown      |
| ------ | -------------------------------- | ------------- | ------------ |
| 2      | `instancefieldreward.dbss`       | 82 B (53.2%)  | 72 B (46.8%) |
| 2      | `instancefieldrewardoffset.dbss` | 24 B (100.0%) | 0 B (0.0%)   |
| 1      | `instancefieldreward.dbss`       | 62 B (46.3%)  | 72 B (53.7%) |
| 1      | `instancefieldrewardoffset.dbss` | 24 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `30afaf02e26c`  |
| 3482   | Layout 2             | `30afaf02e26c`  |
| 3474   | Layout 2             | `30afaf02e26c`  |
| 3473   | Layout 2             | `30afaf02e26c`  |
| 3464   | Layout 2             | `30afaf02e26c`  |
| 3458   | Layout 2             | `30afaf02e26c`  |
| 3454   | Layout 2             | `30afaf02e26c`  |
| 3444   | Layout 2             | `30afaf02e26c`  |
| 3435   | Layout 2             | `30afaf02e26c`  |
| 3426   | Layout 2             | `30afaf02e26c`  |
| 3418   | Layout 2             | `30afaf02e26c`  |
| 3412   | Layout 2             | `30afaf02e26c`  |
| 3402   | Layout 2             | `30afaf02e26c`  |
| 3396   | Layout 2             | `30afaf02e26c`  |
| 3387   | Layout 2             | `30afaf02e26c`  |
| 3381   | Layout 2             | `30afaf02e26c`  |
| 3373   | Layout 2             | `30afaf02e26c`  |
| 3364   | Layout 2             | `30afaf02e26c`  |
| 3356   | Layout 2             | `30afaf02e26c`  |
| 3349   | Layout 2             | `30afaf02e26c`  |
| 3342   | Layout 2             | `30afaf02e26c`  |
| 3335   | Layout 2             | `30afaf02e26c`  |
| 3326   | Layout 2             | `30afaf02e26c`  |
| 3321   | Layout 2             | `30afaf02e26c`  |
| 3314   | Layout 2             | `30afaf02e26c`  |
| 3303   | Layout 2             | `30afaf02e26c`  |
| 3302   | Layout 2             | `30afaf02e26c`  |
| 3293   | Layout 2             | `30afaf02e26c`  |
| 3283   | Layout 2             | `30afaf02e26c`  |
| 3275   | Layout 2             | `30afaf02e26c`  |
| 3267   | Layout 2             | `30afaf02e26c`  |
| 3258   | Layout 2             | `30afaf02e26c`  |
| 3251   | Layout 2             | `30afaf02e26c`  |
| 3242   | Layout 2             | `30afaf02e26c`  |
| 3235   | Layout 2             | `30afaf02e26c`  |
| 3229   | Layout 2             | `30afaf02e26c`  |
| 3212   | Layout 2             | `30afaf02e26c`  |
| 3203   | Layout 2             | `30afaf02e26c`  |
| 3193   | Layout 2             | `30afaf02e26c`  |
| 3186   | Layout 2             | `30afaf02e26c`  |
| 3177   | Layout 2             | `30afaf02e26c`  |
| 3169   | Layout 2             | `30afaf02e26c`  |
| 3158   | Layout 2             | `30afaf02e26c`  |
| 3151   | Layout 2             | `30afaf02e26c`  |
| 3144   | Layout 2             | `30afaf02e26c`  |
| 3133   | Layout 2             | `30afaf02e26c`  |
| 3125   | Layout 2             | `30afaf02e26c`  |
| 3118   | Layout 2             | `30afaf02e26c`  |
| 3111   | Layout 2             | `30afaf02e26c`  |
| 3103   | Layout 2             | `30afaf02e26c`  |
| 3095   | Layout 2             | `30afaf02e26c`  |
| 3086   | Layout 2             | `30afaf02e26c`  |
| 3072   | Layout 2             | `30afaf02e26c`  |
| 3062   | Layout 2             | `30afaf02e26c`  |
| 3052   | Layout 2             | `30afaf02e26c`  |
| 3045   | Layout 2             | `30afaf02e26c`  |
| 3037   | Layout 2             | `30afaf02e26c`  |
| 3030   | Layout 2             | `30afaf02e26c`  |
| 3021   | Layout 2             | `30afaf02e26c`  |
| 3012   | Layout 2             | `30afaf02e26c`  |
| 3002   | Layout 2             | `30afaf02e26c`  |
| 2995   | Layout 2             | `30afaf02e26c`  |
| 2987   | Layout 2             | `30afaf02e26c`  |
| 2978   | Layout 2             | `30afaf02e26c`  |
| 2970   | Layout 2             | `30afaf02e26c`  |
| 2959   | Layout 2             | `30afaf02e26c`  |
| 2951   | Layout 2             | `30afaf02e26c`  |
| 2942   | Layout 2             | `30afaf02e26c`  |
| 2935   | Layout 2             | `30afaf02e26c`  |
| 2932   | Layout 2             | `30afaf02e26c`  |
| 2923   | Layout 2             | `30afaf02e26c`  |
| 2919   | Layout 2             | `30afaf02e26c`  |
| 2907   | Layout 2             | `30afaf02e26c`  |
| 2900   | Layout 2             | `30afaf02e26c`  |
| 2891   | Layout 2             | `30afaf02e26c`  |
| 2882   | Layout 2             | `30afaf02e26c`  |
| 2872   | Layout 2             | `30afaf02e26c`  |
| 2863   | Layout 2             | `30afaf02e26c`  |
| 2855   | Layout 2             | `30afaf02e26c`  |
| 2849   | Layout 2             | `30afaf02e26c`  |
| 2844   | Layout 2             | `30afaf02e26c`  |
| 2834   | Layout 2             | `30afaf02e26c`  |
| 2825   | Layout 2             | `30afaf02e26c`  |
| 2819   | Layout 2             | `30afaf02e26c`  |
| 2811   | Layout 2             | `30afaf02e26c`  |
| 2803   | Layout 2             | `30afaf02e26c`  |
| 2794   | Layout 2             | `30afaf02e26c`  |
| 2783   | Layout 2             | `30afaf02e26c`  |
| 2774   | Layout 2             | `30afaf02e26c`  |
| 2765   | Layout 2             | `30afaf02e26c`  |
| 2756   | Layout 2             | `30afaf02e26c`  |
| 2750   | Layout 2             | `30afaf02e26c`  |
| 2743   | Layout 2             | `30afaf02e26c`  |
| 2736   | Layout 2             | `30afaf02e26c`  |
| 2726   | Layout 2             | `30afaf02e26c`  |
| 2717   | Layout 1             | `30afaf02e26c`  |
| 2709   | Layout 1             | `30afaf02e26c`  |
| 2703   | Layout 1             | `30afaf02e26c`  |
| 2695   | Layout 1             | `30afaf02e26c`  |
| 2684   | Layout 1             | `30afaf02e26c`  |
| 2672   | Layout 1             | `30afaf02e26c`  |
| 2665   | Layout 1             | `30afaf02e26c`  |
| 2657   | Layout 1             | `30afaf02e26c`  |
| 2649   | Layout 1             | `30afaf02e26c`  |
| 2644   | Layout 1             | `30afaf02e26c`  |
| 2637   | Layout 1             | `30afaf02e26c`  |
| 2629   | Layout 1             | `30afaf02e26c`  |
| 2619   | Layout 1             | `30afaf02e26c`  |
| 2612   | Layout 1             | `30afaf02e26c`  |
| 2606   | Layout 1             | `30afaf02e26c`  |
| 2602   | Layout 1             | `30afaf02e26c`  |
| 2601   | Layout 1             | `30afaf02e26c`  |
| 2592   | Layout 1             | `30afaf02e26c`  |
| 2583   | Layout 1             | `30afaf02e26c`  |
| 2575   | Layout 1             | `30afaf02e26c`  |
| 2567   | Layout 1             | `30afaf02e26c`  |
| 2560   | Layout 1             | `30afaf02e26c`  |
| 2553   | Layout 1             | `30afaf02e26c`  |
| 2545   | Layout 1             | `30afaf02e26c`  |
| 2538   | Layout 1             | `30afaf02e26c`  |
| 2529   | Layout 1             | `30afaf02e26c`  |
| 2519   | Layout 1             | `30afaf02e26c`  |
| 2513   | Layout 1             | `30afaf02e26c`  |
| 2510   | Layout 1             | `30afaf02e26c`  |
| 2507   | Layout 1             | `30afaf02e26c`  |
| 2503   | Layout 1             | `30afaf02e26c`  |
| 2498   | Layout 1             | `30afaf02e26c`  |
| 2492   | Layout 1             | `30afaf02e26c`  |
| 2487   | Layout 1             | `30afaf02e26c`  |
| 2480   | Layout 1             | `30afaf02e26c`  |
| 2474   | Layout 1             | `30afaf02e26c`  |
| 2468   | Layout 1             | `30afaf02e26c`  |
| 2460   | Layout 1             | `30afaf02e26c`  |
| 2453   | Layout 1             | `30afaf02e26c`  |
| 2444   | Layout 1             | `30afaf02e26c`  |
| 2438   | Layout 1             | `30afaf02e26c`  |
| 2434   | Layout 1             | `30afaf02e26c`  |
| 2429   | Layout 1             | `30afaf02e26c`  |
| 2421   | Layout 1             | `30afaf02e26c`  |
| 2414   | Layout 1             | `30afaf02e26c`  |
| 2407   | Layout 1             | `30afaf02e26c`  |
| 2401   | Layout 1             | `30afaf02e26c`  |
| 2397   | Layout 1             | `30afaf02e26c`  |
| 2393   | Layout 1             | `30afaf02e26c`  |
| 2384   | Layout 1             | `30afaf02e26c`  |
| 2378   | Layout 1             | `30afaf02e26c`  |
| 2372   | Layout 1             | `30afaf02e26c`  |
| 2358   | Layout 1             | `30afaf02e26c`  |
| 2352   | Layout 1             | `30afaf02e26c`  |
| 2347   | Layout 1             | `30afaf02e26c`  |
| 2343   | Layout 1             | `30afaf02e26c`  |
| 2335   | Layout 1             | `30afaf02e26c`  |
| 2327   | Layout 1             | `30afaf02e26c`  |
| 2324   | Layout 1             | `30afaf02e26c`  |
| 2319   | Layout 1             | `30afaf02e26c`  |
| 2313   | Layout 1             | `30afaf02e26c`  |
| 2308   | Layout 1             | `30afaf02e26c`  |
| 2302   | Layout 1             | `30afaf02e26c`  |
| 2295   | Layout 1             | `30afaf02e26c`  |
| 2290   | Layout 1             | `30afaf02e26c`  |
| 2284   | Layout 1             | `30afaf02e26c`  |
| 2276   | Layout 1             | `30afaf02e26c`  |
| 2269   | Layout 1             | `30afaf02e26c`  |
| 2259   | Layout 1             | `30afaf02e26c`  |
| 2250   | Layout 1             | `30afaf02e26c`  |
| 2243   | Layout 1             | `30afaf02e26c`  |
| 2235   | Layout 1             | `30afaf02e26c`  |
| 2229   | Layout 1             | `30afaf02e26c`  |
| 2224   | Layout 1             | `30afaf02e26c`  |
| 2218   | Layout 1             | `30afaf02e26c`  |
| 2215   | Layout 1             | `30afaf02e26c`  |
| 2207   | Layout 1             | `30afaf02e26c`  |
| 2203   | Layout 1             | `30afaf02e26c`  |
| 2196   | Layout 1             | `30afaf02e26c`  |
| 2192   | Layout 1             | `30afaf02e26c`  |
| 2189   | Layout 1             | `30afaf02e26c`  |
| 2183   | Layout 1             | `30afaf02e26c`  |
| 2179   | Layout 1             | `30afaf02e26c`  |
| 2171   | Layout 1             | `30afaf02e26c`  |
| 2163   | Layout 1             | `30afaf02e26c`  |
| 2156   | Layout 1             | `30afaf02e26c`  |
| 2151   | Layout 1             | `30afaf02e26c`  |
| 2147   | Layout 1             | `30afaf02e26c`  |
| 2142   | Layout 1             | `30afaf02e26c`  |
| 2138   | Layout 1             | `30afaf02e26c`  |
| 2134   | Layout 1             | `30afaf02e26c`  |
| 2130   | Layout 1             | `30afaf02e26c`  |
| 2122   | Layout 1             | `30afaf02e26c`  |
| 2107   | Layout 1             | `30afaf02e26c`  |
| 2098   | Layout 1             | `30afaf02e26c`  |
| 2089   | Layout 1             | `30afaf02e26c`  |
| 2081   | Layout 1             | `30afaf02e26c`  |
| 2073   | Layout 1             | `30afaf02e26c`  |
| 2067   | Layout 1             | `30afaf02e26c`  |
| 2063   | Layout 1             | `30afaf02e26c`  |
| 2059   | Layout 1             | `30afaf02e26c`  |
| 2052   | Layout 1             | `30afaf02e26c`  |
| 2044   | Layout 1             | `30afaf02e26c`  |
| 2039   | Layout 1             | `30afaf02e26c`  |
| 2032   | Layout 1             | `30afaf02e26c`  |
| 2025   | Layout 1             | `30afaf02e26c`  |
| 2011   | Layout 1             | `30afaf02e26c`  |
| 2005   | Layout 1             | `30afaf02e26c`  |
| 2000   | Layout 1             | `30afaf02e26c`  |
| 1996   | Layout 1             | `30afaf02e26c`  |
| 1991   | Layout 1             | `30afaf02e26c`  |
| 1985   | Layout 1             | `30afaf02e26c`  |
| 1980   | Layout 1             | `30afaf02e26c`  |
| 1969   | Layout 1             | `30afaf02e26c`  |
| 1964   | Layout 1             | `30afaf02e26c`  |
| 1958   | Layout 1             | `30afaf02e26c`  |
| 1950   | Layout 1             | `30afaf02e26c`  |
| 1945   | Layout 1             | `30afaf02e26c`  |
| 1937   | Layout 1             | `30afaf02e26c`  |
| 1933   | Layout 1             | `30afaf02e26c`  |
| 1927   | Layout 1             | `30afaf02e26c`  |
| 1921   | Layout 1             | `30afaf02e26c`  |
| 1914   | Layout 1             | `30afaf02e26c`  |
| 1908   | Layout 1             | `30afaf02e26c`  |
| 1897   | Layout 1             | `30afaf02e26c`  |
| 1892   | Layout 1             | `30afaf02e26c`  |
| 1886   | Layout 1             | `30afaf02e26c`  |
| 1881   | Layout 1             | `30afaf02e26c`  |
| 1871   | Layout 1             | `30afaf02e26c`  |
| 1866   | Layout 1             | `30afaf02e26c`  |
| 1862   | Layout 1             | `30afaf02e26c`  |
| 1854   | Layout 1             | `30afaf02e26c`  |
| 1846   | Layout 1             | `30afaf02e26c`  |
| 1838   | Layout 1             | `30afaf02e26c`  |
| 1832   | Layout 1             | `30afaf02e26c`  |
| 1826   | Layout 1             | `30afaf02e26c`  |
| 1822   | Layout 1             | `30afaf02e26c`  |
| 1818   | Layout 1             | `30afaf02e26c`  |
| 1804   | Layout 1             | `30afaf02e26c`  |
| 1794   | Layout 1             | `30afaf02e26c`  |
| 1790   | Layout 1             | `30afaf02e26c`  |
| 1784   | Layout 1             | `30afaf02e26c`  |
| 1774   | Layout 1             | `30afaf02e26c`  |
| 1771   | Layout 1             | `30afaf02e26c`  |
| 1762   | Layout 1             | `30afaf02e26c`  |
| 1759   | Layout 1             | `30afaf02e26c`  |
| 1754   | Layout 1             | `30afaf02e26c`  |
| 1749   | Layout 1             | `30afaf02e26c`  |
| 1743   | Layout 1             | `30afaf02e26c`  |
| 1737   | Layout 1             | `30afaf02e26c`  |
| 1731   | Layout 1             | `30afaf02e26c`  |
| 1725   | Layout 1             | `30afaf02e26c`  |
| 1717   | Layout 1             | `30afaf02e26c`  |
| 1710   | Layout 1             | `30afaf02e26c`  |
| 1704   | Layout 1             | `30afaf02e26c`  |
| 1698   | Layout 1             | `30afaf02e26c`  |
| 1690   | Layout 1             | `30afaf02e26c`  |
| 1685   | Layout 1             | `30afaf02e26c`  |
| 1680   | Layout 1             | `30afaf02e26c`  |
| 1674   | Layout 1             | `30afaf02e26c`  |
| 1668   | Layout 1             | `30afaf02e26c`  |
| 1659   | Layout 1             | `30afaf02e26c`  |
| 1649   | Layout 1             | `30afaf02e26c`  |
| 1642   | Layout 1             | `30afaf02e26c`  |
| 1636   | Layout 1             | `30afaf02e26c`  |
| 1628   | Layout 1             | `30afaf02e26c`  |
| 1622   | Layout 1             | `30afaf02e26c`  |
| 1614   | Layout 1             | `30afaf02e26c`  |
| 1608   | Layout 1             | `30afaf02e26c`  |
| 1602   | Layout 1             | `30afaf02e26c`  |
| 1598   | Layout 1             | `30afaf02e26c`  |
| 1594   | Layout 1             | `30afaf02e26c`  |
| 1590   | Layout 1             | `30afaf02e26c`  |
| 1587   | Layout 1             | `30afaf02e26c`  |
| 1584   | Layout 1             | `30afaf02e26c`  |
| 1579   | Layout 1             | `30afaf02e26c`  |
| 1572   | Layout 1             | `30afaf02e26c`  |
| 1565   | Layout 1             | `30afaf02e26c`  |
| 1559   | Layout 1             | `30afaf02e26c`  |
| 1554   | Layout 1             | `30afaf02e26c`  |
| 1547   | Layout 1             | `30afaf02e26c`  |
| 1537   | Layout 1             | `30afaf02e26c`  |
| 1529   | Layout 1             | `30afaf02e26c`  |
| 1524   | Layout 1             | `30afaf02e26c`  |
| 1519   | Layout 1             | `30afaf02e26c`  |
| 1509   | Layout 1             | `30afaf02e26c`  |
| 1506   | Layout 1             | `30afaf02e26c`  |
| 1504   | Layout 1             | `30afaf02e26c`  |
| 1500   | Layout 1             | `30afaf02e26c`  |
| 1493   | Layout 1             | `30afaf02e26c`  |
| 1489   | Layout 1             | `30afaf02e26c`  |
| 1485   | Layout 1             | `30afaf02e26c`  |
| 1481   | Layout 1             | `30afaf02e26c`  |
| 1474   | Layout 1             | `30afaf02e26c`  |
| 1466   | Layout 1             | `30afaf02e26c`  |
| 1462   | Layout 1             | `30afaf02e26c`  |
| 1459   | Layout 1             | `30afaf02e26c`  |
| 1453   | Layout 1             | `30afaf02e26c`  |
| 1450   | Layout 1             | `30afaf02e26c`  |
| 1445   | Layout 1             | `30afaf02e26c`  |
| 1439   | Layout 1             | `30afaf02e26c`  |
| 1433   | Layout 1             | `30afaf02e26c`  |
| 1430   | Layout 1             | `30afaf02e26c`  |
| 1426   | Layout 1             | `30afaf02e26c`  |
| 1421   | Layout 1             | `30afaf02e26c`  |
| 1417   | Layout 1             | `30afaf02e26c`  |
| 1416   | Layout 1             | `30afaf02e26c`  |
| 1409   | Layout 1             | `30afaf02e26c`  |
| 1405   | Layout 1             | `30afaf02e26c`  |
| 1401   | Layout 1             | `30afaf02e26c`  |
| 1396   | Layout 1             | `30afaf02e26c`  |
| 1391   | Layout 1             | `30afaf02e26c`  |
| 1390   | Layout 1             | `30afaf02e26c`  |
| 1386   | Layout 1             | `30afaf02e26c`  |
| 1381   | Layout 1             | `30afaf02e26c`  |
| 1379   | Layout 1             | `30afaf02e26c`  |
| 1372   | Layout 1             | `30afaf02e26c`  |
| 1366   | Layout 1             | `30afaf02e26c`  |
| 1364   | Layout 1             | `30afaf02e26c`  |
| 1363   | Layout 1             | `30afaf02e26c`  |
| 1360   | Layout 1             | `30afaf02e26c`  |
| 1358   | Layout 1             | `30afaf02e26c`  |
| 1355   | Layout 1             | `30afaf02e26c`  |
| 1351   | Layout 1             | `30afaf02e26c`  |
| 1348   | Layout 1             | `30afaf02e26c`  |
| 1346   | Layout 1             | `30afaf02e26c`  |
| 1341   | No documented layout | `30afaf02e26c`  |
| 1340   | No documented layout | `30afaf02e26c`  |
| 1338   | No documented layout | `30afaf02e26c`  |
| 1335   | No documented layout | `30afaf02e26c`  |
| 1333   | No documented layout | `30afaf02e26c`  |
| 1329   | No documented layout | `30afaf02e26c`  |
| 1327   | No documented layout | `30afaf02e26c`  |
| 1324   | No documented layout | `30afaf02e26c`  |
| 1321   | No documented layout | `30afaf02e26c`  |
| 1319   | No documented layout | `30afaf02e26c`  |
| 1318   | No documented layout | `30afaf02e26c`  |
| 1316   | No documented layout | `30afaf02e26c`  |
| 1313   | No documented layout | `30afaf02e26c`  |
| 1311   | No documented layout | `30afaf02e26c`  |
| 1309   | No documented layout | `30afaf02e26c`  |
| 1304   | No documented layout | `30afaf02e26c`  |
| 1292   | No documented layout | `30afaf02e26c`  |
| 1286   | No documented layout | `30afaf02e26c`  |
| 1280   | No documented layout | `30afaf02e26c`  |
| 1276   | No documented layout | `30afaf02e26c`  |
| 1267   | No file              | `30afaf02e26c`  |
| 1261   | No file              | `30afaf02e26c`  |
| 1256   | No file              | `30afaf02e26c`  |
| 1250   | No file              | `30afaf02e26c`  |
| 1246   | No file              | `30afaf02e26c`  |
| 1239   | No file              | `30afaf02e26c`  |
| 1230   | No file              | `30afaf02e26c`  |
| 1226   | No file              | `30afaf02e26c`  |
| 1220   | No file              | `30afaf02e26c`  |
| 1217   | No file              | `30afaf02e26c`  |
| 1211   | No file              | `30afaf02e26c`  |
| 1210   | No file              | `30afaf02e26c`  |
| 1208   | No file              | `30afaf02e26c`  |
| 1203   | No file              | `30afaf02e26c`  |
| 1197   | No file              | `30afaf02e26c`  |
| 1194   | No file              | `30afaf02e26c`  |
| 1192   | No file              | `30afaf02e26c`  |
| 1187   | No file              | `30afaf02e26c`  |
| 1183   | No file              | `30afaf02e26c`  |
| 1177   | No file              | `30afaf02e26c`  |
| 1173   | No file              | `30afaf02e26c`  |
| 1167   | No file              | `30afaf02e26c`  |
| 1164   | No file              | `30afaf02e26c`  |
| 1156   | No file              | `30afaf02e26c`  |
| 1149   | No file              | `30afaf02e26c`  |
| 1144   | No file              | `30afaf02e26c`  |
| 1137   | No file              | `30afaf02e26c`  |
| 1132   | No file              | `30afaf02e26c`  |
| 1127   | No file              | `30afaf02e26c`  |
| 1122   | No file              | `30afaf02e26c`  |
| 1118   | No file              | `30afaf02e26c`  |
| 1114   | No file              | `30afaf02e26c`  |
| 1109   | No file              | `30afaf02e26c`  |
| 1102   | No file              | `30afaf02e26c`  |
| 1096   | No file              | `30afaf02e26c`  |
| 1088   | No file              | `30afaf02e26c`  |
| 1081   | No file              | `30afaf02e26c`  |
| 1076   | No file              | `30afaf02e26c`  |
| 1069   | No file              | `30afaf02e26c`  |
| 1064   | No file              | `30afaf02e26c`  |
| 1058   | No file              | `30afaf02e26c`  |
| 1051   | No file              | `30afaf02e26c`  |
| 1044   | No file              | `30afaf02e26c`  |
| 1036   | No file              | `30afaf02e26c`  |
| 1026   | No file              | `30afaf02e26c`  |
| 1016   | No file              | `30afaf02e26c`  |
| 1009   | No file              | `30afaf02e26c`  |
| 1005   | No file              | `30afaf02e26c`  |
| 1000   | No file              | `30afaf02e26c`  |
| 998    | No file              | `30afaf02e26c`  |
| 990    | No file              | `30afaf02e26c`  |
| 979    | No file              | `30afaf02e26c`  |
| 972    | No file              | `30afaf02e26c`  |
| 963    | No file              | `30afaf02e26c`  |
| 955    | No file              | `30afaf02e26c`  |
| 946    | No file              | `30afaf02e26c`  |
| 938    | No file              | `30afaf02e26c`  |
| 927    | No file              | `30afaf02e26c`  |
| 911    | No file              | `30afaf02e26c`  |
| 904    | No file              | `30afaf02e26c`  |
| 899    | No file              | `30afaf02e26c`  |
| 894    | No file              | `30afaf02e26c`  |
| 885    | No file              | `30afaf02e26c`  |
| 879    | No file              | `30afaf02e26c`  |
| 872    | No file              | `30afaf02e26c`  |
| 864    | No file              | `30afaf02e26c`  |
| 855    | No file              | `30afaf02e26c`  |
| 853    | No file              | `30afaf02e26c`  |
| 845    | No file              | `30afaf02e26c`  |
| 837    | No file              | `30afaf02e26c`  |
| 829    | No file              | `30afaf02e26c`  |
| 822    | No file              | `30afaf02e26c`  |
| 814    | No file              | `30afaf02e26c`  |
| 805    | No file              | `30afaf02e26c`  |
| 794    | No file              | `30afaf02e26c`  |
| 787    | No file              | `30afaf02e26c`  |
| 780    | No file              | `30afaf02e26c`  |
| 771    | No file              | `30afaf02e26c`  |
| 760    | No file              | `30afaf02e26c`  |
| 748    | No file              | `30afaf02e26c`  |
| 741    | No file              | `30afaf02e26c`  |
| 736    | No file              | `30afaf02e26c`  |
| 731    | No file              | `30afaf02e26c`  |
| 723    | No file              | `30afaf02e26c`  |
| 711    | No file              | `30afaf02e26c`  |
| 707    | No file              | `30afaf02e26c`  |
| 697    | No file              | `30afaf02e26c`  |
| 689    | No file              | `30afaf02e26c`  |
| 683    | No file              | `30afaf02e26c`  |
| 678    | No file              | `30afaf02e26c`  |
| 670    | No file              | `30afaf02e26c`  |
| 661    | No file              | `30afaf02e26c`  |
| 656    | No file              | `30afaf02e26c`  |
| 652    | No file              | `30afaf02e26c`  |
| 643    | No file              | `30afaf02e26c`  |
| 637    | No file              | `30afaf02e26c`  |
| 630    | No file              | `30afaf02e26c`  |
| 627    | No file              | `30afaf02e26c`  |
| 621    | No file              | `30afaf02e26c`  |
| 617    | No file              | `30afaf02e26c`  |
| 615    | No file              | `30afaf02e26c`  |
| 606    | No file              | `30afaf02e26c`  |
| 599    | No file              | `30afaf02e26c`  |
| 592    | No file              | `30afaf02e26c`  |
| 586    | No file              | `30afaf02e26c`  |
| 577    | No file              | `30afaf02e26c`  |
| 569    | No file              | `30afaf02e26c`  |
| 561    | No file              | `30afaf02e26c`  |
| 554    | No file              | `30afaf02e26c`  |
| 542    | No file              | `30afaf02e26c`  |
| 532    | No file              | `30afaf02e26c`  |
| 531    | No file              | `30afaf02e26c`  |
| 526    | No file              | `30afaf02e26c`  |
| 521    | No file              | `30afaf02e26c`  |
| 517    | No file              | `30afaf02e26c`  |
| 510    | No file              | `30afaf02e26c`  |
| 508    | No file              | `30afaf02e26c`  |
| 504    | No file              | `30afaf02e26c`  |
| 497    | No file              | `30afaf02e26c`  |
| 491    | No file              | `30afaf02e26c`  |
| 485    | No file              | `30afaf02e26c`  |
| 478    | No file              | `30afaf02e26c`  |
| 472    | No file              | `30afaf02e26c`  |
| 466    | No file              | `30afaf02e26c`  |
| 457    | No file              | `30afaf02e26c`  |
| 452    | No file              | `30afaf02e26c`  |
| 449    | No file              | `30afaf02e26c`  |
| 435    | No file              | `30afaf02e26c`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                     |
| -------------------------------- | -------- | ------------------------------------------------------------------------ |
| `instancefieldrewardoffset.dbss` | Optional | `instance_dungeon_no -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`            | Optional | Region names (LOC type 17)                                               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 36 bytes + push items and regions)

| Offset                 | Type                        | Field                   | Notes                                                       |
| ---------------------- | --------------------------- | ----------------------- | ----------------------------------------------------------- |
| `+0x00`                | u16                         | instance_dungeon_no     | Row key                                                     |
| `+0x02`                | u16                         | instance_dungeon_no_dup | Equal to `instance_dungeon_no`; the offset file points here |
| `+0x04`                | u32                         | learn_skill             | `0` (no skill) on both rows of clients 1784 and 3474         |
| `+0x08`                | u32[5]                      | item_groups             | `itemmaingroup.bss` keys, the sheet's `Grade1` to `Grade5`   |
| `+0x1C`                | u32                         | push_item_count         | `3` on both rows                                            |
| `+0x20`                | Push Item[push_item_count]  | push_items              | See Push Item                                               |
| `push_items+0x00`      | u32                         | related_region_count    | Number of regions                                           |
| `push_items+0x04`      | u16[related_region_count]   | related_regions         | `regioninfo.bss` region keys, the sheet's `RegionNo`        |

### Push Item (12 bytes)

| Offset  | Type | Field      | Notes                                       |
| ------- | ---- | ---------- | ------------------------------------------- |
| `+0x00` | u32  | unknown_00 | `0` in every slot of clients 1784 and 3474  |
| `+0x04` | i64  | unknown_04 | `0` in every slot of clients 1784 and 3474  |

### `instancefieldrewardoffset.dbss`

Bare offset table into `instancefieldreward.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `instancefieldreward.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                               |

### Offset Row (10 bytes)

| Offset  | Type | Field               | Notes                                                         |
| ------- | ---- | ------------------- | ------------------------------------------------------------- |
| `+0x00` | u16  | instance_dungeon_no | Key of the row it points at                                   |
| `+0x02` | u32  | data_offset         | Row start + 2, at `instance_dungeon_no_dup`                   |
| `+0x06` | u32  | data_size           | The row without its leading `instance_dungeon_no`             |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. On clients
1784 and 3474 every index row points at the row with its key.

## Layout 1

Client 1784 stores the five item groups as u16.

### Row (variable: 26 bytes + push items and regions)

| Offset            | Type                       | Field                   | Notes |
| ----------------- | -------------------------- | ----------------------- | ----- |
| `+0x00`           | u16                        | instance_dungeon_no     |       |
| `+0x02`           | u16                        | instance_dungeon_no_dup |       |
| `+0x04`           | u32                        | learn_skill             |       |
| `+0x08`           | u16[5]                     | item_groups             |       |
| `+0x12`           | u32                        | push_item_count         |       |
| `+0x16`           | Push Item[push_item_count] | push_items              |       |
| `push_items+0x00` | u32                        | related_region_count    |       |
| `push_items+0x04` | u16[related_region_count]  | related_regions         |       |

## Field Names

The 2016 client's debug symbols have `gc::InstanceFieldRewardStaticStatus`
as `_fieldNo` (short), `_itemGroupList` (5 u16 keys), resolved pointers, a
`_pushItemStaticList` of 3 `gc::ItemStaticInformation`, `_learnSkillKey`
and `_relatedRegion` (a vector of u16 region keys). The
`Instance_Reward` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `InstanceDundeonNo` (sic), `LearnSkill`, `RegionNo`,
`PushItem1` to `PushItem3` and `Grade1` to `Grade5`. Its 2 rows match the
client 1784 file on both keys: `LearnSkill` and the push items are empty
(`0`), `Grade1` to `Grade5` are `56001` to `56005`, and `RegionNo` of `291`
is `62, 63, 37`. The u32 before the item groups is `LearnSkill` by the
2016 member list; the file moves it ahead of the groups.

## Notes

- `199` and `291` are not keys of `instancefield.dbss`,
  `instancefieldmapinfo.bss` or `fieldinfo.bss` on client 3474.
- The push item slots hold 12 bytes each, the size of an item key and an
  item count; with every slot `0` the two parts cannot be told apart, so
  they stay `unknown_00` and `unknown_04`.

## Open Questions

### What the Dungeon Number Keys

`InstanceDundeonNo` `199` and `291` match no key of the instance field,
instance field map or field tables. Which content the two reward rows
belong to is open.
