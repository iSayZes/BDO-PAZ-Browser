# `itemexchangetoclass.dbss` Format

## Purpose

The weapon exchange groups behind the Weapon Exchange window
(`Panel_Window_ChangeItem_All`): each row is one group of equivalent
weapons, such as the Rusty weapons (key `1`) or the Tuvala main weapons
(key `165`), with one item key per class type. Exchanging an item for
another class gives the item in that class's slot of the item's group.
`itemexchangetoclassoffset.dbss` is the index into it, and
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) maps
each item back to its group.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ------ | -------------- | --------- |
| 2      | 3381 and later | 3483    | `itemexchangetoclass.dbss`       | 39,404 | 200 Row        | 197       |
| 2      | 3381 and later | 3483    | `itemexchangetoclassoffset.dbss` | 2,404  | 200 Offset Row | 12        |
| 1      | 1622 to 2243   | 2243    | `itemexchangetoclass.dbss`       | 26,171 | 191 Row        | 137       |
| 1      | 1622 to 2243   | 2243    | `itemexchangetoclassoffset.dbss` | 2,296  | 191 Offset Row | 12        |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 2      | `itemexchangetoclass.dbss`       | 39,404 B (100.0%) | 0 B (0.0%) |
| 2      | `itemexchangetoclassoffset.dbss` | 2,404 B (100.0%)  | 0 B (0.0%) |
| 1      | `itemexchangetoclass.dbss`       | 26,171 B (100.0%) | 0 B (0.0%) |
| 1      | `itemexchangetoclassoffset.dbss` | 2,296 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `026ba6a65ac7`  |
| 3482   | Layout 2             | `026ba6a65ac7`  |
| 3474   | Layout 2             | `026ba6a65ac7`  |
| 3473   | Layout 2             | `026ba6a65ac7`  |
| 3464   | Layout 2             | `026ba6a65ac7`  |
| 3458   | Layout 2             | `026ba6a65ac7`  |
| 3454   | Layout 2             | `026ba6a65ac7`  |
| 3444   | Layout 2             | `026ba6a65ac7`  |
| 3435   | Layout 2             | `026ba6a65ac7`  |
| 3426   | Layout 2             | `026ba6a65ac7`  |
| 3418   | Layout 2             | `026ba6a65ac7`  |
| 3412   | Layout 2             | `026ba6a65ac7`  |
| 3402   | Layout 2             | `026ba6a65ac7`  |
| 3396   | Layout 2             | `026ba6a65ac7`  |
| 3387   | Layout 2             | `026ba6a65ac7`  |
| 3381   | Layout 2             | `026ba6a65ac7`  |
| 3373   | No documented layout | `026ba6a65ac7`  |
| 3364   | No documented layout | `026ba6a65ac7`  |
| 3356   | No documented layout | `026ba6a65ac7`  |
| 3349   | No documented layout | `026ba6a65ac7`  |
| 3342   | No documented layout | `026ba6a65ac7`  |
| 3335   | No documented layout | `026ba6a65ac7`  |
| 3326   | No documented layout | `026ba6a65ac7`  |
| 3321   | No documented layout | `026ba6a65ac7`  |
| 3314   | No documented layout | `026ba6a65ac7`  |
| 3303   | No documented layout | `026ba6a65ac7`  |
| 3302   | No documented layout | `026ba6a65ac7`  |
| 3293   | No documented layout | `026ba6a65ac7`  |
| 3283   | No documented layout | `026ba6a65ac7`  |
| 3275   | No documented layout | `026ba6a65ac7`  |
| 3267   | No documented layout | `026ba6a65ac7`  |
| 3258   | No documented layout | `026ba6a65ac7`  |
| 3251   | No documented layout | `026ba6a65ac7`  |
| 3242   | No documented layout | `026ba6a65ac7`  |
| 3235   | No documented layout | `026ba6a65ac7`  |
| 3229   | No documented layout | `026ba6a65ac7`  |
| 3212   | No documented layout | `026ba6a65ac7`  |
| 3203   | No documented layout | `026ba6a65ac7`  |
| 3193   | No documented layout | `026ba6a65ac7`  |
| 3186   | No documented layout | `026ba6a65ac7`  |
| 3177   | No documented layout | `026ba6a65ac7`  |
| 3169   | No documented layout | `026ba6a65ac7`  |
| 3158   | No documented layout | `026ba6a65ac7`  |
| 3151   | No documented layout | `026ba6a65ac7`  |
| 3144   | No documented layout | `026ba6a65ac7`  |
| 3133   | No documented layout | `026ba6a65ac7`  |
| 3125   | No documented layout | `026ba6a65ac7`  |
| 3118   | No documented layout | `026ba6a65ac7`  |
| 3111   | No documented layout | `026ba6a65ac7`  |
| 3103   | No documented layout | `026ba6a65ac7`  |
| 3095   | No documented layout | `026ba6a65ac7`  |
| 3086   | No documented layout | `026ba6a65ac7`  |
| 3072   | No documented layout | `026ba6a65ac7`  |
| 3062   | No documented layout | `026ba6a65ac7`  |
| 3052   | No documented layout | `026ba6a65ac7`  |
| 3045   | No documented layout | `026ba6a65ac7`  |
| 3037   | No documented layout | `026ba6a65ac7`  |
| 3030   | No documented layout | `026ba6a65ac7`  |
| 3021   | No documented layout | `026ba6a65ac7`  |
| 3012   | No documented layout | `026ba6a65ac7`  |
| 3002   | No documented layout | `026ba6a65ac7`  |
| 2995   | No documented layout | `026ba6a65ac7`  |
| 2987   | No documented layout | `026ba6a65ac7`  |
| 2978   | No documented layout | `026ba6a65ac7`  |
| 2970   | No documented layout | `026ba6a65ac7`  |
| 2959   | No documented layout | `026ba6a65ac7`  |
| 2951   | No documented layout | `026ba6a65ac7`  |
| 2942   | No documented layout | `026ba6a65ac7`  |
| 2935   | No documented layout | `026ba6a65ac7`  |
| 2932   | No documented layout | `026ba6a65ac7`  |
| 2923   | No documented layout | `026ba6a65ac7`  |
| 2919   | No documented layout | `026ba6a65ac7`  |
| 2907   | No documented layout | `026ba6a65ac7`  |
| 2900   | No documented layout | `026ba6a65ac7`  |
| 2891   | No documented layout | `026ba6a65ac7`  |
| 2882   | No documented layout | `026ba6a65ac7`  |
| 2872   | No documented layout | `026ba6a65ac7`  |
| 2863   | No documented layout | `026ba6a65ac7`  |
| 2855   | No documented layout | `026ba6a65ac7`  |
| 2849   | No documented layout | `026ba6a65ac7`  |
| 2844   | No documented layout | `026ba6a65ac7`  |
| 2834   | No documented layout | `026ba6a65ac7`  |
| 2825   | No documented layout | `026ba6a65ac7`  |
| 2819   | No documented layout | `026ba6a65ac7`  |
| 2811   | No documented layout | `026ba6a65ac7`  |
| 2803   | No documented layout | `026ba6a65ac7`  |
| 2794   | No documented layout | `026ba6a65ac7`  |
| 2783   | No documented layout | `026ba6a65ac7`  |
| 2774   | No documented layout | `026ba6a65ac7`  |
| 2765   | No documented layout | `026ba6a65ac7`  |
| 2756   | No documented layout | `026ba6a65ac7`  |
| 2750   | No documented layout | `026ba6a65ac7`  |
| 2743   | No documented layout | `026ba6a65ac7`  |
| 2736   | No documented layout | `026ba6a65ac7`  |
| 2726   | No documented layout | `026ba6a65ac7`  |
| 2717   | No documented layout | `026ba6a65ac7`  |
| 2709   | No documented layout | `026ba6a65ac7`  |
| 2703   | No documented layout | `026ba6a65ac7`  |
| 2695   | No documented layout | `026ba6a65ac7`  |
| 2684   | No documented layout | `026ba6a65ac7`  |
| 2672   | No documented layout | `026ba6a65ac7`  |
| 2665   | No documented layout | `026ba6a65ac7`  |
| 2657   | No documented layout | `026ba6a65ac7`  |
| 2649   | No documented layout | `026ba6a65ac7`  |
| 2644   | No documented layout | `026ba6a65ac7`  |
| 2637   | No documented layout | `026ba6a65ac7`  |
| 2629   | No documented layout | `026ba6a65ac7`  |
| 2619   | No documented layout | `026ba6a65ac7`  |
| 2612   | No documented layout | `026ba6a65ac7`  |
| 2606   | No documented layout | `026ba6a65ac7`  |
| 2602   | No documented layout | `026ba6a65ac7`  |
| 2601   | No documented layout | `026ba6a65ac7`  |
| 2592   | No documented layout | `026ba6a65ac7`  |
| 2583   | No documented layout | `026ba6a65ac7`  |
| 2575   | No documented layout | `026ba6a65ac7`  |
| 2567   | No documented layout | `026ba6a65ac7`  |
| 2560   | No documented layout | `026ba6a65ac7`  |
| 2553   | No documented layout | `026ba6a65ac7`  |
| 2545   | No documented layout | `026ba6a65ac7`  |
| 2538   | No documented layout | `026ba6a65ac7`  |
| 2529   | No documented layout | `026ba6a65ac7`  |
| 2519   | No documented layout | `026ba6a65ac7`  |
| 2513   | No documented layout | `026ba6a65ac7`  |
| 2510   | No documented layout | `026ba6a65ac7`  |
| 2507   | No documented layout | `026ba6a65ac7`  |
| 2503   | No documented layout | `026ba6a65ac7`  |
| 2498   | No documented layout | `026ba6a65ac7`  |
| 2492   | No documented layout | `026ba6a65ac7`  |
| 2487   | No documented layout | `026ba6a65ac7`  |
| 2480   | No documented layout | `026ba6a65ac7`  |
| 2474   | No documented layout | `026ba6a65ac7`  |
| 2468   | No documented layout | `026ba6a65ac7`  |
| 2460   | No documented layout | `026ba6a65ac7`  |
| 2453   | No documented layout | `026ba6a65ac7`  |
| 2444   | No documented layout | `026ba6a65ac7`  |
| 2438   | No documented layout | `026ba6a65ac7`  |
| 2434   | No documented layout | `026ba6a65ac7`  |
| 2429   | No documented layout | `026ba6a65ac7`  |
| 2421   | No documented layout | `026ba6a65ac7`  |
| 2414   | No documented layout | `026ba6a65ac7`  |
| 2407   | No documented layout | `026ba6a65ac7`  |
| 2401   | No documented layout | `026ba6a65ac7`  |
| 2397   | No documented layout | `026ba6a65ac7`  |
| 2393   | No documented layout | `026ba6a65ac7`  |
| 2384   | No documented layout | `026ba6a65ac7`  |
| 2378   | No documented layout | `026ba6a65ac7`  |
| 2372   | No documented layout | `026ba6a65ac7`  |
| 2358   | No documented layout | `026ba6a65ac7`  |
| 2352   | No documented layout | `026ba6a65ac7`  |
| 2347   | No documented layout | `026ba6a65ac7`  |
| 2343   | No documented layout | `026ba6a65ac7`  |
| 2335   | No documented layout | `026ba6a65ac7`  |
| 2327   | No documented layout | `026ba6a65ac7`  |
| 2324   | No documented layout | `026ba6a65ac7`  |
| 2319   | No documented layout | `026ba6a65ac7`  |
| 2313   | No documented layout | `026ba6a65ac7`  |
| 2308   | No documented layout | `026ba6a65ac7`  |
| 2302   | No documented layout | `026ba6a65ac7`  |
| 2295   | No documented layout | `026ba6a65ac7`  |
| 2290   | No documented layout | `026ba6a65ac7`  |
| 2284   | No documented layout | `026ba6a65ac7`  |
| 2276   | No documented layout | `026ba6a65ac7`  |
| 2269   | No documented layout | `026ba6a65ac7`  |
| 2259   | No documented layout | `026ba6a65ac7`  |
| 2250   | No documented layout | `026ba6a65ac7`  |
| 2243   | Layout 1             | `026ba6a65ac7`  |
| 2235   | Layout 1             | `026ba6a65ac7`  |
| 2229   | Layout 1             | `026ba6a65ac7`  |
| 2224   | Layout 1             | `026ba6a65ac7`  |
| 2218   | Layout 1             | `026ba6a65ac7`  |
| 2215   | Layout 1             | `026ba6a65ac7`  |
| 2207   | Layout 1             | `026ba6a65ac7`  |
| 2203   | Layout 1             | `026ba6a65ac7`  |
| 2196   | Layout 1             | `026ba6a65ac7`  |
| 2192   | Layout 1             | `026ba6a65ac7`  |
| 2189   | Layout 1             | `026ba6a65ac7`  |
| 2183   | Layout 1             | `026ba6a65ac7`  |
| 2179   | Layout 1             | `026ba6a65ac7`  |
| 2171   | Layout 1             | `026ba6a65ac7`  |
| 2163   | Layout 1             | `026ba6a65ac7`  |
| 2156   | Layout 1             | `026ba6a65ac7`  |
| 2151   | Layout 1             | `026ba6a65ac7`  |
| 2147   | Layout 1             | `026ba6a65ac7`  |
| 2142   | Layout 1             | `026ba6a65ac7`  |
| 2138   | Layout 1             | `026ba6a65ac7`  |
| 2134   | Layout 1             | `026ba6a65ac7`  |
| 2130   | Layout 1             | `026ba6a65ac7`  |
| 2122   | Layout 1             | `026ba6a65ac7`  |
| 2107   | Layout 1             | `026ba6a65ac7`  |
| 2098   | Layout 1             | `026ba6a65ac7`  |
| 2089   | Layout 1             | `026ba6a65ac7`  |
| 2081   | Layout 1             | `026ba6a65ac7`  |
| 2073   | Layout 1             | `026ba6a65ac7`  |
| 2067   | Layout 1             | `026ba6a65ac7`  |
| 2063   | Layout 1             | `026ba6a65ac7`  |
| 2059   | Layout 1             | `026ba6a65ac7`  |
| 2052   | Layout 1             | `026ba6a65ac7`  |
| 2044   | Layout 1             | `026ba6a65ac7`  |
| 2039   | Layout 1             | `026ba6a65ac7`  |
| 2032   | Layout 1             | `026ba6a65ac7`  |
| 2025   | Layout 1             | `026ba6a65ac7`  |
| 2011   | Layout 1             | `026ba6a65ac7`  |
| 2005   | Layout 1             | `026ba6a65ac7`  |
| 2000   | Layout 1             | `026ba6a65ac7`  |
| 1996   | Layout 1             | `026ba6a65ac7`  |
| 1991   | Layout 1             | `026ba6a65ac7`  |
| 1985   | Layout 1             | `026ba6a65ac7`  |
| 1980   | Layout 1             | `026ba6a65ac7`  |
| 1969   | Layout 1             | `026ba6a65ac7`  |
| 1964   | Layout 1             | `026ba6a65ac7`  |
| 1958   | Layout 1             | `026ba6a65ac7`  |
| 1950   | Layout 1             | `026ba6a65ac7`  |
| 1945   | Layout 1             | `026ba6a65ac7`  |
| 1937   | Layout 1             | `026ba6a65ac7`  |
| 1933   | Layout 1             | `026ba6a65ac7`  |
| 1927   | Layout 1             | `026ba6a65ac7`  |
| 1921   | Layout 1             | `026ba6a65ac7`  |
| 1914   | Layout 1             | `026ba6a65ac7`  |
| 1908   | Layout 1             | `026ba6a65ac7`  |
| 1897   | Layout 1             | `026ba6a65ac7`  |
| 1892   | Layout 1             | `026ba6a65ac7`  |
| 1886   | Layout 1             | `026ba6a65ac7`  |
| 1881   | Layout 1             | `026ba6a65ac7`  |
| 1871   | Layout 1             | `026ba6a65ac7`  |
| 1866   | Layout 1             | `026ba6a65ac7`  |
| 1862   | Layout 1             | `026ba6a65ac7`  |
| 1854   | Layout 1             | `026ba6a65ac7`  |
| 1846   | Layout 1             | `026ba6a65ac7`  |
| 1838   | Layout 1             | `026ba6a65ac7`  |
| 1832   | Layout 1             | `026ba6a65ac7`  |
| 1826   | Layout 1             | `026ba6a65ac7`  |
| 1822   | Layout 1             | `026ba6a65ac7`  |
| 1818   | Layout 1             | `026ba6a65ac7`  |
| 1804   | Layout 1             | `026ba6a65ac7`  |
| 1794   | Layout 1             | `026ba6a65ac7`  |
| 1790   | Layout 1             | `026ba6a65ac7`  |
| 1784   | Layout 1             | `026ba6a65ac7`  |
| 1774   | Layout 1             | `026ba6a65ac7`  |
| 1771   | Layout 1             | `026ba6a65ac7`  |
| 1762   | Layout 1             | `026ba6a65ac7`  |
| 1759   | Layout 1             | `026ba6a65ac7`  |
| 1754   | Layout 1             | `026ba6a65ac7`  |
| 1749   | Layout 1             | `026ba6a65ac7`  |
| 1743   | Layout 1             | `026ba6a65ac7`  |
| 1737   | Layout 1             | `026ba6a65ac7`  |
| 1731   | Layout 1             | `026ba6a65ac7`  |
| 1725   | Layout 1             | `026ba6a65ac7`  |
| 1717   | Layout 1             | `026ba6a65ac7`  |
| 1710   | Layout 1             | `026ba6a65ac7`  |
| 1704   | Layout 1             | `026ba6a65ac7`  |
| 1698   | Layout 1             | `026ba6a65ac7`  |
| 1690   | Layout 1             | `026ba6a65ac7`  |
| 1685   | Layout 1             | `026ba6a65ac7`  |
| 1680   | Layout 1             | `026ba6a65ac7`  |
| 1674   | Layout 1             | `026ba6a65ac7`  |
| 1668   | Layout 1             | `026ba6a65ac7`  |
| 1659   | Layout 1             | `026ba6a65ac7`  |
| 1649   | Layout 1             | `026ba6a65ac7`  |
| 1642   | Layout 1             | `026ba6a65ac7`  |
| 1636   | Layout 1             | `026ba6a65ac7`  |
| 1628   | Layout 1             | `026ba6a65ac7`  |
| 1622   | Layout 1             | `026ba6a65ac7`  |
| 1614   | No documented layout | `026ba6a65ac7`  |
| 1608   | No documented layout | `026ba6a65ac7`  |
| 1602   | No documented layout | `026ba6a65ac7`  |
| 1598   | No documented layout | `026ba6a65ac7`  |
| 1594   | No documented layout | `026ba6a65ac7`  |
| 1590   | No documented layout | `026ba6a65ac7`  |
| 1587   | No documented layout | `026ba6a65ac7`  |
| 1584   | No documented layout | `026ba6a65ac7`  |
| 1579   | No documented layout | `026ba6a65ac7`  |
| 1572   | No documented layout | `026ba6a65ac7`  |
| 1565   | No documented layout | `026ba6a65ac7`  |
| 1559   | No documented layout | `026ba6a65ac7`  |
| 1554   | No documented layout | `026ba6a65ac7`  |
| 1547   | No documented layout | `026ba6a65ac7`  |
| 1537   | No documented layout | `026ba6a65ac7`  |
| 1529   | No documented layout | `026ba6a65ac7`  |
| 1524   | No documented layout | `026ba6a65ac7`  |
| 1519   | No documented layout | `026ba6a65ac7`  |
| 1509   | No documented layout | `026ba6a65ac7`  |
| 1506   | No documented layout | `026ba6a65ac7`  |
| 1504   | No documented layout | `026ba6a65ac7`  |
| 1500   | No documented layout | `026ba6a65ac7`  |
| 1493   | No documented layout | `026ba6a65ac7`  |
| 1489   | No documented layout | `026ba6a65ac7`  |
| 1485   | No documented layout | `026ba6a65ac7`  |
| 1481   | No documented layout | `026ba6a65ac7`  |
| 1474   | No documented layout | `026ba6a65ac7`  |
| 1466   | No documented layout | `026ba6a65ac7`  |
| 1462   | No documented layout | `026ba6a65ac7`  |
| 1459   | No documented layout | `026ba6a65ac7`  |
| 1453   | No documented layout | `026ba6a65ac7`  |
| 1450   | No documented layout | `026ba6a65ac7`  |
| 1445   | No documented layout | `026ba6a65ac7`  |
| 1439   | No documented layout | `026ba6a65ac7`  |
| 1433   | No documented layout | `026ba6a65ac7`  |
| 1430   | No documented layout | `026ba6a65ac7`  |
| 1426   | No documented layout | `026ba6a65ac7`  |
| 1421   | No documented layout | `026ba6a65ac7`  |
| 1417   | No documented layout | `026ba6a65ac7`  |
| 1416   | No documented layout | `026ba6a65ac7`  |
| 1409   | No documented layout | `026ba6a65ac7`  |
| 1405   | No documented layout | `026ba6a65ac7`  |
| 1401   | No documented layout | `026ba6a65ac7`  |
| 1396   | No documented layout | `026ba6a65ac7`  |
| 1391   | No documented layout | `026ba6a65ac7`  |
| 1390   | No documented layout | `026ba6a65ac7`  |
| 1386   | No documented layout | `026ba6a65ac7`  |
| 1381   | No documented layout | `026ba6a65ac7`  |
| 1379   | No documented layout | `026ba6a65ac7`  |
| 1372   | No documented layout | `026ba6a65ac7`  |
| 1366   | No documented layout | `026ba6a65ac7`  |
| 1364   | No documented layout | `026ba6a65ac7`  |
| 1363   | No documented layout | `026ba6a65ac7`  |
| 1360   | No documented layout | `026ba6a65ac7`  |
| 1358   | No documented layout | `026ba6a65ac7`  |
| 1355   | No documented layout | `026ba6a65ac7`  |
| 1351   | No documented layout | `026ba6a65ac7`  |
| 1348   | No documented layout | `026ba6a65ac7`  |
| 1346   | No documented layout | `026ba6a65ac7`  |
| 1341   | No documented layout | `026ba6a65ac7`  |
| 1340   | No documented layout | `026ba6a65ac7`  |
| 1338   | No documented layout | `026ba6a65ac7`  |
| 1335   | No documented layout | `026ba6a65ac7`  |
| 1333   | No documented layout | `026ba6a65ac7`  |
| 1329   | No documented layout | `026ba6a65ac7`  |
| 1327   | No documented layout | `026ba6a65ac7`  |
| 1324   | No documented layout | `026ba6a65ac7`  |
| 1321   | No documented layout | `026ba6a65ac7`  |
| 1319   | No documented layout | `026ba6a65ac7`  |
| 1318   | No documented layout | `026ba6a65ac7`  |
| 1316   | No documented layout | `026ba6a65ac7`  |
| 1313   | No documented layout | `026ba6a65ac7`  |
| 1311   | No documented layout | `026ba6a65ac7`  |
| 1309   | No documented layout | `026ba6a65ac7`  |
| 1304   | No documented layout | `026ba6a65ac7`  |
| 1292   | No documented layout | `026ba6a65ac7`  |
| 1286   | No documented layout | `026ba6a65ac7`  |
| 1280   | No documented layout | `026ba6a65ac7`  |
| 1276   | No documented layout | `026ba6a65ac7`  |
| 1267   | No file              | `026ba6a65ac7`  |
| 1261   | No file              | `026ba6a65ac7`  |
| 1256   | No file              | `026ba6a65ac7`  |
| 1250   | No file              | `026ba6a65ac7`  |
| 1246   | No file              | `026ba6a65ac7`  |
| 1239   | No file              | `026ba6a65ac7`  |
| 1230   | No file              | `026ba6a65ac7`  |
| 1226   | No file              | `026ba6a65ac7`  |
| 1220   | No file              | `026ba6a65ac7`  |
| 1217   | No file              | `026ba6a65ac7`  |
| 1211   | No file              | `026ba6a65ac7`  |
| 1210   | No file              | `026ba6a65ac7`  |
| 1208   | No file              | `026ba6a65ac7`  |
| 1203   | No file              | `026ba6a65ac7`  |
| 1197   | No file              | `026ba6a65ac7`  |
| 1194   | No file              | `026ba6a65ac7`  |
| 1192   | No file              | `026ba6a65ac7`  |
| 1187   | No file              | `026ba6a65ac7`  |
| 1183   | No file              | `026ba6a65ac7`  |
| 1177   | No file              | `026ba6a65ac7`  |
| 1173   | No file              | `026ba6a65ac7`  |
| 1167   | No file              | `026ba6a65ac7`  |
| 1164   | No file              | `026ba6a65ac7`  |
| 1156   | No file              | `026ba6a65ac7`  |
| 1149   | No file              | `026ba6a65ac7`  |
| 1144   | No file              | `026ba6a65ac7`  |
| 1137   | No file              | `026ba6a65ac7`  |
| 1132   | No file              | `026ba6a65ac7`  |
| 1127   | No file              | `026ba6a65ac7`  |
| 1122   | No file              | `026ba6a65ac7`  |
| 1118   | No file              | `026ba6a65ac7`  |
| 1114   | No file              | `026ba6a65ac7`  |
| 1109   | No file              | `026ba6a65ac7`  |
| 1102   | No file              | `026ba6a65ac7`  |
| 1096   | No file              | `026ba6a65ac7`  |
| 1088   | No file              | `026ba6a65ac7`  |
| 1081   | No file              | `026ba6a65ac7`  |
| 1076   | No file              | `026ba6a65ac7`  |
| 1069   | No file              | `026ba6a65ac7`  |
| 1064   | No file              | `026ba6a65ac7`  |
| 1058   | No file              | `026ba6a65ac7`  |
| 1051   | No file              | `026ba6a65ac7`  |
| 1044   | No file              | `026ba6a65ac7`  |
| 1036   | No file              | `026ba6a65ac7`  |
| 1026   | No file              | `026ba6a65ac7`  |
| 1016   | No file              | `026ba6a65ac7`  |
| 1009   | No file              | `026ba6a65ac7`  |
| 1005   | No file              | `026ba6a65ac7`  |
| 1000   | No file              | `026ba6a65ac7`  |
| 998    | No file              | `026ba6a65ac7`  |
| 990    | No file              | `026ba6a65ac7`  |
| 979    | No file              | `026ba6a65ac7`  |
| 972    | No file              | `026ba6a65ac7`  |
| 963    | No file              | `026ba6a65ac7`  |
| 955    | No file              | `026ba6a65ac7`  |
| 946    | No file              | `026ba6a65ac7`  |
| 938    | No file              | `026ba6a65ac7`  |
| 927    | No file              | `026ba6a65ac7`  |
| 911    | No file              | `026ba6a65ac7`  |
| 904    | No file              | `026ba6a65ac7`  |
| 899    | No file              | `026ba6a65ac7`  |
| 894    | No file              | `026ba6a65ac7`  |
| 885    | No file              | `026ba6a65ac7`  |
| 879    | No file              | `026ba6a65ac7`  |
| 872    | No file              | `026ba6a65ac7`  |
| 864    | No file              | `026ba6a65ac7`  |
| 855    | No file              | `026ba6a65ac7`  |
| 853    | No file              | `026ba6a65ac7`  |
| 845    | No file              | `026ba6a65ac7`  |
| 837    | No file              | `026ba6a65ac7`  |
| 829    | No file              | `026ba6a65ac7`  |
| 822    | No file              | `026ba6a65ac7`  |
| 814    | No file              | `026ba6a65ac7`  |
| 805    | No file              | `026ba6a65ac7`  |
| 794    | No file              | `026ba6a65ac7`  |
| 787    | No file              | `026ba6a65ac7`  |
| 780    | No file              | `026ba6a65ac7`  |
| 771    | No file              | `026ba6a65ac7`  |
| 760    | No file              | `026ba6a65ac7`  |
| 748    | No file              | `026ba6a65ac7`  |
| 741    | No file              | `026ba6a65ac7`  |
| 736    | No file              | `026ba6a65ac7`  |
| 731    | No file              | `026ba6a65ac7`  |
| 723    | No file              | `026ba6a65ac7`  |
| 711    | No file              | `026ba6a65ac7`  |
| 707    | No file              | `026ba6a65ac7`  |
| 697    | No file              | `026ba6a65ac7`  |
| 689    | No file              | `026ba6a65ac7`  |
| 683    | No file              | `026ba6a65ac7`  |
| 678    | No file              | `026ba6a65ac7`  |
| 670    | No file              | `026ba6a65ac7`  |
| 661    | No file              | `026ba6a65ac7`  |
| 656    | No file              | `026ba6a65ac7`  |
| 652    | No file              | `026ba6a65ac7`  |
| 643    | No file              | `026ba6a65ac7`  |
| 637    | No file              | `026ba6a65ac7`  |
| 630    | No file              | `026ba6a65ac7`  |
| 627    | No file              | `026ba6a65ac7`  |
| 621    | No file              | `026ba6a65ac7`  |
| 617    | No file              | `026ba6a65ac7`  |
| 615    | No file              | `026ba6a65ac7`  |
| 606    | No file              | `026ba6a65ac7`  |
| 599    | No file              | `026ba6a65ac7`  |
| 592    | No file              | `026ba6a65ac7`  |
| 586    | No file              | `026ba6a65ac7`  |
| 577    | No file              | `026ba6a65ac7`  |
| 569    | No file              | `026ba6a65ac7`  |
| 561    | No file              | `026ba6a65ac7`  |
| 554    | No file              | `026ba6a65ac7`  |
| 542    | No file              | `026ba6a65ac7`  |
| 532    | No file              | `026ba6a65ac7`  |
| 531    | No file              | `026ba6a65ac7`  |
| 526    | No file              | `026ba6a65ac7`  |
| 521    | No file              | `026ba6a65ac7`  |
| 517    | No file              | `026ba6a65ac7`  |
| 510    | No file              | `026ba6a65ac7`  |
| 508    | No file              | `026ba6a65ac7`  |
| 504    | No file              | `026ba6a65ac7`  |
| 497    | No file              | `026ba6a65ac7`  |
| 491    | No file              | `026ba6a65ac7`  |
| 485    | No file              | `026ba6a65ac7`  |
| 478    | No file              | `026ba6a65ac7`  |
| 472    | No file              | `026ba6a65ac7`  |
| 466    | No file              | `026ba6a65ac7`  |
| 457    | No file              | `026ba6a65ac7`  |
| 452    | No file              | `026ba6a65ac7`  |
| 449    | No file              | `026ba6a65ac7`  |
| 435    | No file              | `026ba6a65ac7`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                |
| -------------------------------- | -------- | ------------------------------------------------------------------- |
| `itemexchangetoclassoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |
| `languagedata_en.loc`            | Optional | Class name (type `21`, `str_id1` = class type) and item name (type `0`, `str_id1` = item ID) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `200` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (197 bytes)

| Offset  | Type    | Field         | Notes                                                            |
| ------- | ------- | ------------- | ---------------------------------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                                        |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row; the offset file points here         |
| `+0x08` | u32[47] | item_keys     | Item key (`enchant_level << 24 \| item_id`) per class type, index = class type; `0` for a class without an item |
| `+0xC4` | u8      | exchange_type | See Exchange Types                                               |

The rows are not sorted by key: on client 3474 they start `203`, `202`,
`201` and run down in runs that restart higher (`192` is followed by
`219`).

### `itemexchangetoclassoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemexchangetoclass.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                      |
| ------- | ---- | ----------- | ---------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                                |
| `+0x04` | u32  | data_offset | Row start + 4, at `key_dup`                                |
| `+0x08` | u32  | data_size   | The row without its leading `key`: `193` on client 3474    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are not in file order (`139`, `203`, `138`, `202` on client
3474); on clients 1784 and 3474 every index row points at the row with its
key.

## Layout 1

On client 1784 the row holds 32 class slots where Layout 2 has 47, and
`data_size` is `133`. The file has 171 rows.

### Row (137 bytes)

| Offset  | Type    | Field         | Notes                                    |
| ------- | ------- | ------------- | ---------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row              |
| `+0x08` | u32[32] | item_keys     | Item key per class type, index = class type |
| `+0x88` | u8      | exchange_type | See Exchange Types                       |

## Class Slots

The slot index is the class type `getClassType()` returns, so slot `0` is
Warrior, `4` Ranger, `8` Sorceress and `32` Seraph: in every row the class
whose LOC type 21 name matches the item's weapon (Hashashin a Shamshir,
Sage a Kyve, Lahn a Crescent Pendulum). On client 3474 the rows fill class
types 0 to 35 without 13, 14, 18 and 22, the same set as
`PLAYABLE_CLASSES_MASK` in `_common/class_type.py`; slots 36 to 46 are `0`
in every row. Classes that share a weapon share the item: Musa (`20`) and
Maehwa (`21`) both get `13301` Rusty Blade in row `1`.

An item key carries no enhancement level in any row on clients 1784 and
3474 (every `item_keys` value is below `1 << 24`).

## Exchange Types

| Value | Meaning      | Rows on client 3474                             |
| ----- | ------------ | ----------------------------------------------- |
| `0`   | Normal item  | 191                                             |
| `1`   | Season item  | 9: `105` to `107`, `165` to `167`, `170` to `172` |

The names come from the developer note on the `ExchangeType` column of the
`Item_Exchange` sheet in a private server's `.xlsm` on client 1784: the
column tells whether a group is exchanged with a normal weapon exchange
coupon or a season one. Both coupons use `ContentsEventType` `38`
(`ContentsType_ItemExchangeToClass` in the client 3474 Lua enum) and
`ContentsEventParam1` `-1`; `ContentsEventParam2` `0`, `1` and `2` (main,
awakening, sub-weapon) are the normal coupons, `3`, `4` and `5` the season
ones. The client data agrees: rows `165` to `167` hold the Tuvala main,
sub-weapon and awakening weapons and rows `170` to `172` Combatant's
Tuvala weapons, both season server gear.

## Field Names

The row is the 2016 `gc::ItemExchangeToClassStaticStatus`: `_key`
(`gc::KeyType<int,0>`, an i32) and `_itemKey`, a `pa::Array` of 32
`gc::ItemEnchantKey`. The file writes the key before the struct as the
index key and again as `_key`. The 2016 struct has no exchange type; the
`ItemExchangeToClassStaticStatusManager` around it also holds
`_mapKeyFromItemKey`, the item to group map that
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) stores.

The values match the `Item_Exchange` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`. Its item columns are named
`ClassType0` to `ClassType32` after the class type, each followed by a note
column with the Korean class name; slot `n` matches the column
`ClassTypeN`. The sheet lists `ClassType26` and `ClassType27` twice, an
empty pair first, and the second pair matches.

| Field         | Column                           | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------------- | ------------------------ | ------------------------ |
| key           | `Index`                          | 171 of 171 rows          | 167 of 171 sheet rows    |
| item_keys     | `ClassType0` to `ClassType32`    | 170 of 171               | 161 of 167 shared rows   |
| exchange_type | `ExchangeType`                   | 171 of 171               | 164 of 167               |

- Client 1784 row `171` holds no item, while the sheet lists the Godr-Ayed
  sub-weapons (`738301` up).
- On client 3474 the sheet rows `173` to `176` have no row, and the 33
  rows `177` to `219` have none in the sheet. The 161 matching rows also
  fill class types the sheet leaves empty (3 Wukong, 6 Scholar, 7
  Drakania, 15 Maegu, 30 Woosa, 32 to 35); the comparison skips those. The
  six other rows are `105` to `107`, which the sheet fills with the Tuvala
  weapons `694113` up and client 3474 empties, and `170` to `172`, which
  hold Godr-Ayed sub-weapons and type `0` in the sheet and Combatant's
  Tuvala weapons and type `1` on client 3474.

## Notes

- The Weapon Exchange window Lua (`panel_window_changeitem_all_1.luac` and
  `_2.luac`) opens on `FromClient_UseItemExchangeToClass`, asks
  `getExchangeItem()` for the result of each inventory item and exchanges
  with `exchangeItemToClass()`; it reads no table field itself. The coupon's
  `getContentsEventParam1()` picks the target class, `-1` meaning the
  player's own class.
- On client 3474 rows `105` and `106` hold no item, and row `107` only
  `695193` Tuvala Pendant at class type 35 (Agent), which row `167` holds
  in the same slot. `931802` Ultimate Krea Clavis sits in rows `68` and
  `71` at class type 32. These two are the only items in two rows.
