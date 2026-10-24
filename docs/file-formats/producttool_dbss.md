# `producttool.dbss` Format

## Purpose

One value per fishing rod or float and enhancement level, named
`AutofishingTimePercents` in the source sheet. On client 3474 the file holds
22 records: Cedar Float at each level from 0 to 10, and eleven fishing rods
at level 0. The value is `1,000,000` for Cedar Float, the Triple-Float
Fishing Rod and four rods that catch several fish at once, and `500,000`
for the Splendid and Lucky Silver and Golden Fishing Rods. What the client
does with it is open (see Open Questions). "Product" is the client's word
for life skills; the item descriptions call a fishing rod "a gathering
tool". Companion `producttooloffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------ | --------- |
| 1      | 1346 and later | 3483    | `producttool.dbss`       | 620   | 22 Record    | 28        |
| 1      | 1346 and later | 3483    | `producttooloffset.dbss` | 268   | 22 Index Row | 12        |

| Layout | File                     | Known          | Unknown       |
| ------ | ------------------------ | -------------- | ------------- |
| 1      | `producttool.dbss`       | 268 B (43.2%)  | 352 B (56.8%) |
| 1      | `producttooloffset.dbss` | 268 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `4b4a8fb55c0d`  |
| 3482   | Layout 1             | `4b4a8fb55c0d`  |
| 3474   | Layout 1             | `4b4a8fb55c0d`  |
| 3473   | Layout 1             | `4b4a8fb55c0d`  |
| 3464   | Layout 1             | `4b4a8fb55c0d`  |
| 3458   | Layout 1             | `4b4a8fb55c0d`  |
| 3454   | Layout 1             | `4b4a8fb55c0d`  |
| 3444   | Layout 1             | `4b4a8fb55c0d`  |
| 3435   | Layout 1             | `4b4a8fb55c0d`  |
| 3426   | Layout 1             | `4b4a8fb55c0d`  |
| 3418   | Layout 1             | `4b4a8fb55c0d`  |
| 3412   | Layout 1             | `4b4a8fb55c0d`  |
| 3402   | Layout 1             | `4b4a8fb55c0d`  |
| 3396   | Layout 1             | `4b4a8fb55c0d`  |
| 3387   | Layout 1             | `4b4a8fb55c0d`  |
| 3381   | Layout 1             | `4b4a8fb55c0d`  |
| 3373   | Layout 1             | `4b4a8fb55c0d`  |
| 3364   | Layout 1             | `4b4a8fb55c0d`  |
| 3356   | Layout 1             | `4b4a8fb55c0d`  |
| 3349   | Layout 1             | `4b4a8fb55c0d`  |
| 3342   | Layout 1             | `4b4a8fb55c0d`  |
| 3335   | Layout 1             | `4b4a8fb55c0d`  |
| 3326   | Layout 1             | `4b4a8fb55c0d`  |
| 3321   | Layout 1             | `4b4a8fb55c0d`  |
| 3314   | Layout 1             | `4b4a8fb55c0d`  |
| 3303   | Layout 1             | `4b4a8fb55c0d`  |
| 3302   | Layout 1             | `4b4a8fb55c0d`  |
| 3293   | Layout 1             | `4b4a8fb55c0d`  |
| 3283   | Layout 1             | `4b4a8fb55c0d`  |
| 3275   | Layout 1             | `4b4a8fb55c0d`  |
| 3267   | Layout 1             | `4b4a8fb55c0d`  |
| 3258   | Layout 1             | `4b4a8fb55c0d`  |
| 3251   | Layout 1             | `4b4a8fb55c0d`  |
| 3242   | Layout 1             | `4b4a8fb55c0d`  |
| 3235   | Layout 1             | `4b4a8fb55c0d`  |
| 3229   | Layout 1             | `4b4a8fb55c0d`  |
| 3212   | Layout 1             | `4b4a8fb55c0d`  |
| 3203   | Layout 1             | `4b4a8fb55c0d`  |
| 3193   | Layout 1             | `4b4a8fb55c0d`  |
| 3186   | Layout 1             | `4b4a8fb55c0d`  |
| 3177   | Layout 1             | `4b4a8fb55c0d`  |
| 3169   | Layout 1             | `4b4a8fb55c0d`  |
| 3158   | Layout 1             | `4b4a8fb55c0d`  |
| 3151   | Layout 1             | `4b4a8fb55c0d`  |
| 3144   | Layout 1             | `4b4a8fb55c0d`  |
| 3133   | Layout 1             | `4b4a8fb55c0d`  |
| 3125   | Layout 1             | `4b4a8fb55c0d`  |
| 3118   | Layout 1             | `4b4a8fb55c0d`  |
| 3111   | Layout 1             | `4b4a8fb55c0d`  |
| 3103   | Layout 1             | `4b4a8fb55c0d`  |
| 3095   | Layout 1             | `4b4a8fb55c0d`  |
| 3086   | Layout 1             | `4b4a8fb55c0d`  |
| 3072   | Layout 1             | `4b4a8fb55c0d`  |
| 3062   | Layout 1             | `4b4a8fb55c0d`  |
| 3052   | Layout 1             | `4b4a8fb55c0d`  |
| 3045   | Layout 1             | `4b4a8fb55c0d`  |
| 3037   | Layout 1             | `4b4a8fb55c0d`  |
| 3030   | Layout 1             | `4b4a8fb55c0d`  |
| 3021   | Layout 1             | `4b4a8fb55c0d`  |
| 3012   | Layout 1             | `4b4a8fb55c0d`  |
| 3002   | Layout 1             | `4b4a8fb55c0d`  |
| 2995   | Layout 1             | `4b4a8fb55c0d`  |
| 2987   | Layout 1             | `4b4a8fb55c0d`  |
| 2978   | Layout 1             | `4b4a8fb55c0d`  |
| 2970   | Layout 1             | `4b4a8fb55c0d`  |
| 2959   | Layout 1             | `4b4a8fb55c0d`  |
| 2951   | Layout 1             | `4b4a8fb55c0d`  |
| 2942   | Layout 1             | `4b4a8fb55c0d`  |
| 2935   | Layout 1             | `4b4a8fb55c0d`  |
| 2932   | Layout 1             | `4b4a8fb55c0d`  |
| 2923   | Layout 1             | `4b4a8fb55c0d`  |
| 2919   | Layout 1             | `4b4a8fb55c0d`  |
| 2907   | Layout 1             | `4b4a8fb55c0d`  |
| 2900   | Layout 1             | `4b4a8fb55c0d`  |
| 2891   | Layout 1             | `4b4a8fb55c0d`  |
| 2882   | Layout 1             | `4b4a8fb55c0d`  |
| 2872   | Layout 1             | `4b4a8fb55c0d`  |
| 2863   | Layout 1             | `4b4a8fb55c0d`  |
| 2855   | Layout 1             | `4b4a8fb55c0d`  |
| 2849   | Layout 1             | `4b4a8fb55c0d`  |
| 2844   | Layout 1             | `4b4a8fb55c0d`  |
| 2834   | Layout 1             | `4b4a8fb55c0d`  |
| 2825   | Layout 1             | `4b4a8fb55c0d`  |
| 2819   | Layout 1             | `4b4a8fb55c0d`  |
| 2811   | Layout 1             | `4b4a8fb55c0d`  |
| 2803   | Layout 1             | `4b4a8fb55c0d`  |
| 2794   | Layout 1             | `4b4a8fb55c0d`  |
| 2783   | Layout 1             | `4b4a8fb55c0d`  |
| 2774   | Layout 1             | `4b4a8fb55c0d`  |
| 2765   | Layout 1             | `4b4a8fb55c0d`  |
| 2756   | Layout 1             | `4b4a8fb55c0d`  |
| 2750   | Layout 1             | `4b4a8fb55c0d`  |
| 2743   | Layout 1             | `4b4a8fb55c0d`  |
| 2736   | Layout 1             | `4b4a8fb55c0d`  |
| 2726   | Layout 1             | `4b4a8fb55c0d`  |
| 2717   | Layout 1             | `4b4a8fb55c0d`  |
| 2709   | Layout 1             | `4b4a8fb55c0d`  |
| 2703   | Layout 1             | `4b4a8fb55c0d`  |
| 2695   | Layout 1             | `4b4a8fb55c0d`  |
| 2684   | Layout 1             | `4b4a8fb55c0d`  |
| 2672   | Layout 1             | `4b4a8fb55c0d`  |
| 2665   | Layout 1             | `4b4a8fb55c0d`  |
| 2657   | Layout 1             | `4b4a8fb55c0d`  |
| 2649   | Layout 1             | `4b4a8fb55c0d`  |
| 2644   | Layout 1             | `4b4a8fb55c0d`  |
| 2637   | Layout 1             | `4b4a8fb55c0d`  |
| 2629   | Layout 1             | `4b4a8fb55c0d`  |
| 2619   | Layout 1             | `4b4a8fb55c0d`  |
| 2612   | Layout 1             | `4b4a8fb55c0d`  |
| 2606   | Layout 1             | `4b4a8fb55c0d`  |
| 2602   | Layout 1             | `4b4a8fb55c0d`  |
| 2601   | Layout 1             | `4b4a8fb55c0d`  |
| 2592   | Layout 1             | `4b4a8fb55c0d`  |
| 2583   | Layout 1             | `4b4a8fb55c0d`  |
| 2575   | Layout 1             | `4b4a8fb55c0d`  |
| 2567   | Layout 1             | `4b4a8fb55c0d`  |
| 2560   | Layout 1             | `4b4a8fb55c0d`  |
| 2553   | Layout 1             | `4b4a8fb55c0d`  |
| 2545   | Layout 1             | `4b4a8fb55c0d`  |
| 2538   | Layout 1             | `4b4a8fb55c0d`  |
| 2529   | Layout 1             | `4b4a8fb55c0d`  |
| 2519   | Layout 1             | `4b4a8fb55c0d`  |
| 2513   | Layout 1             | `4b4a8fb55c0d`  |
| 2510   | Layout 1             | `4b4a8fb55c0d`  |
| 2507   | Layout 1             | `4b4a8fb55c0d`  |
| 2503   | Layout 1             | `4b4a8fb55c0d`  |
| 2498   | Layout 1             | `4b4a8fb55c0d`  |
| 2492   | Layout 1             | `4b4a8fb55c0d`  |
| 2487   | Layout 1             | `4b4a8fb55c0d`  |
| 2480   | Layout 1             | `4b4a8fb55c0d`  |
| 2474   | Layout 1             | `4b4a8fb55c0d`  |
| 2468   | Layout 1             | `4b4a8fb55c0d`  |
| 2460   | Layout 1             | `4b4a8fb55c0d`  |
| 2453   | Layout 1             | `4b4a8fb55c0d`  |
| 2444   | Layout 1             | `4b4a8fb55c0d`  |
| 2438   | Layout 1             | `4b4a8fb55c0d`  |
| 2434   | Layout 1             | `4b4a8fb55c0d`  |
| 2429   | Layout 1             | `4b4a8fb55c0d`  |
| 2421   | Layout 1             | `4b4a8fb55c0d`  |
| 2414   | Layout 1             | `4b4a8fb55c0d`  |
| 2407   | Layout 1             | `4b4a8fb55c0d`  |
| 2401   | Layout 1             | `4b4a8fb55c0d`  |
| 2397   | Layout 1             | `4b4a8fb55c0d`  |
| 2393   | Layout 1             | `4b4a8fb55c0d`  |
| 2384   | Layout 1             | `4b4a8fb55c0d`  |
| 2378   | Layout 1             | `4b4a8fb55c0d`  |
| 2372   | Layout 1             | `4b4a8fb55c0d`  |
| 2358   | Layout 1             | `4b4a8fb55c0d`  |
| 2352   | Layout 1             | `4b4a8fb55c0d`  |
| 2347   | Layout 1             | `4b4a8fb55c0d`  |
| 2343   | Layout 1             | `4b4a8fb55c0d`  |
| 2335   | Layout 1             | `4b4a8fb55c0d`  |
| 2327   | Layout 1             | `4b4a8fb55c0d`  |
| 2324   | Layout 1             | `4b4a8fb55c0d`  |
| 2319   | Layout 1             | `4b4a8fb55c0d`  |
| 2313   | Layout 1             | `4b4a8fb55c0d`  |
| 2308   | Layout 1             | `4b4a8fb55c0d`  |
| 2302   | Layout 1             | `4b4a8fb55c0d`  |
| 2295   | Layout 1             | `4b4a8fb55c0d`  |
| 2290   | Layout 1             | `4b4a8fb55c0d`  |
| 2284   | Layout 1             | `4b4a8fb55c0d`  |
| 2276   | Layout 1             | `4b4a8fb55c0d`  |
| 2269   | Layout 1             | `4b4a8fb55c0d`  |
| 2259   | Layout 1             | `4b4a8fb55c0d`  |
| 2250   | Layout 1             | `4b4a8fb55c0d`  |
| 2243   | Layout 1             | `4b4a8fb55c0d`  |
| 2235   | Layout 1             | `4b4a8fb55c0d`  |
| 2229   | Layout 1             | `4b4a8fb55c0d`  |
| 2224   | Layout 1             | `4b4a8fb55c0d`  |
| 2218   | Layout 1             | `4b4a8fb55c0d`  |
| 2215   | Layout 1             | `4b4a8fb55c0d`  |
| 2207   | Layout 1             | `4b4a8fb55c0d`  |
| 2203   | Layout 1             | `4b4a8fb55c0d`  |
| 2196   | Layout 1             | `4b4a8fb55c0d`  |
| 2192   | Layout 1             | `4b4a8fb55c0d`  |
| 2189   | Layout 1             | `4b4a8fb55c0d`  |
| 2183   | Layout 1             | `4b4a8fb55c0d`  |
| 2179   | Layout 1             | `4b4a8fb55c0d`  |
| 2171   | Layout 1             | `4b4a8fb55c0d`  |
| 2163   | Layout 1             | `4b4a8fb55c0d`  |
| 2156   | Layout 1             | `4b4a8fb55c0d`  |
| 2151   | Layout 1             | `4b4a8fb55c0d`  |
| 2147   | Layout 1             | `4b4a8fb55c0d`  |
| 2142   | Layout 1             | `4b4a8fb55c0d`  |
| 2138   | Layout 1             | `4b4a8fb55c0d`  |
| 2134   | Layout 1             | `4b4a8fb55c0d`  |
| 2130   | Layout 1             | `4b4a8fb55c0d`  |
| 2122   | Layout 1             | `4b4a8fb55c0d`  |
| 2107   | Layout 1             | `4b4a8fb55c0d`  |
| 2098   | Layout 1             | `4b4a8fb55c0d`  |
| 2089   | Layout 1             | `4b4a8fb55c0d`  |
| 2081   | Layout 1             | `4b4a8fb55c0d`  |
| 2073   | Layout 1             | `4b4a8fb55c0d`  |
| 2067   | Layout 1             | `4b4a8fb55c0d`  |
| 2063   | Layout 1             | `4b4a8fb55c0d`  |
| 2059   | Layout 1             | `4b4a8fb55c0d`  |
| 2052   | Layout 1             | `4b4a8fb55c0d`  |
| 2044   | Layout 1             | `4b4a8fb55c0d`  |
| 2039   | Layout 1             | `4b4a8fb55c0d`  |
| 2032   | Layout 1             | `4b4a8fb55c0d`  |
| 2025   | Layout 1             | `4b4a8fb55c0d`  |
| 2011   | Layout 1             | `4b4a8fb55c0d`  |
| 2005   | Layout 1             | `4b4a8fb55c0d`  |
| 2000   | Layout 1             | `4b4a8fb55c0d`  |
| 1996   | Layout 1             | `4b4a8fb55c0d`  |
| 1991   | Layout 1             | `4b4a8fb55c0d`  |
| 1985   | Layout 1             | `4b4a8fb55c0d`  |
| 1980   | Layout 1             | `4b4a8fb55c0d`  |
| 1969   | Layout 1             | `4b4a8fb55c0d`  |
| 1964   | Layout 1             | `4b4a8fb55c0d`  |
| 1958   | Layout 1             | `4b4a8fb55c0d`  |
| 1950   | Layout 1             | `4b4a8fb55c0d`  |
| 1945   | Layout 1             | `4b4a8fb55c0d`  |
| 1937   | Layout 1             | `4b4a8fb55c0d`  |
| 1933   | Layout 1             | `4b4a8fb55c0d`  |
| 1927   | Layout 1             | `4b4a8fb55c0d`  |
| 1921   | Layout 1             | `4b4a8fb55c0d`  |
| 1914   | Layout 1             | `4b4a8fb55c0d`  |
| 1908   | Layout 1             | `4b4a8fb55c0d`  |
| 1897   | Layout 1             | `4b4a8fb55c0d`  |
| 1892   | Layout 1             | `4b4a8fb55c0d`  |
| 1886   | Layout 1             | `4b4a8fb55c0d`  |
| 1881   | Layout 1             | `4b4a8fb55c0d`  |
| 1871   | Layout 1             | `4b4a8fb55c0d`  |
| 1866   | Layout 1             | `4b4a8fb55c0d`  |
| 1862   | Layout 1             | `4b4a8fb55c0d`  |
| 1854   | Layout 1             | `4b4a8fb55c0d`  |
| 1846   | Layout 1             | `4b4a8fb55c0d`  |
| 1838   | Layout 1             | `4b4a8fb55c0d`  |
| 1832   | Layout 1             | `4b4a8fb55c0d`  |
| 1826   | Layout 1             | `4b4a8fb55c0d`  |
| 1822   | Layout 1             | `4b4a8fb55c0d`  |
| 1818   | Layout 1             | `4b4a8fb55c0d`  |
| 1804   | Layout 1             | `4b4a8fb55c0d`  |
| 1794   | Layout 1             | `4b4a8fb55c0d`  |
| 1790   | Layout 1             | `4b4a8fb55c0d`  |
| 1784   | Layout 1             | `4b4a8fb55c0d`  |
| 1774   | Layout 1             | `4b4a8fb55c0d`  |
| 1771   | Layout 1             | `4b4a8fb55c0d`  |
| 1762   | Layout 1             | `4b4a8fb55c0d`  |
| 1759   | Layout 1             | `4b4a8fb55c0d`  |
| 1754   | Layout 1             | `4b4a8fb55c0d`  |
| 1749   | Layout 1             | `4b4a8fb55c0d`  |
| 1743   | Layout 1             | `4b4a8fb55c0d`  |
| 1737   | Layout 1             | `4b4a8fb55c0d`  |
| 1731   | Layout 1             | `4b4a8fb55c0d`  |
| 1725   | Layout 1             | `4b4a8fb55c0d`  |
| 1717   | Layout 1             | `4b4a8fb55c0d`  |
| 1710   | Layout 1             | `4b4a8fb55c0d`  |
| 1704   | Layout 1             | `4b4a8fb55c0d`  |
| 1698   | Layout 1             | `4b4a8fb55c0d`  |
| 1690   | Layout 1             | `4b4a8fb55c0d`  |
| 1685   | Layout 1             | `4b4a8fb55c0d`  |
| 1680   | Layout 1             | `4b4a8fb55c0d`  |
| 1674   | Layout 1             | `4b4a8fb55c0d`  |
| 1668   | Layout 1             | `4b4a8fb55c0d`  |
| 1659   | Layout 1             | `4b4a8fb55c0d`  |
| 1649   | Layout 1             | `4b4a8fb55c0d`  |
| 1642   | Layout 1             | `4b4a8fb55c0d`  |
| 1636   | Layout 1             | `4b4a8fb55c0d`  |
| 1628   | Layout 1             | `4b4a8fb55c0d`  |
| 1622   | Layout 1             | `4b4a8fb55c0d`  |
| 1614   | Layout 1             | `4b4a8fb55c0d`  |
| 1608   | Layout 1             | `4b4a8fb55c0d`  |
| 1602   | Layout 1             | `4b4a8fb55c0d`  |
| 1598   | Layout 1             | `4b4a8fb55c0d`  |
| 1594   | Layout 1             | `4b4a8fb55c0d`  |
| 1590   | Layout 1             | `4b4a8fb55c0d`  |
| 1587   | Layout 1             | `4b4a8fb55c0d`  |
| 1584   | Layout 1             | `4b4a8fb55c0d`  |
| 1579   | Layout 1             | `4b4a8fb55c0d`  |
| 1572   | Layout 1             | `4b4a8fb55c0d`  |
| 1565   | Layout 1             | `4b4a8fb55c0d`  |
| 1559   | Layout 1             | `4b4a8fb55c0d`  |
| 1554   | Layout 1             | `4b4a8fb55c0d`  |
| 1547   | Layout 1             | `4b4a8fb55c0d`  |
| 1537   | Layout 1             | `4b4a8fb55c0d`  |
| 1529   | Layout 1             | `4b4a8fb55c0d`  |
| 1524   | Layout 1             | `4b4a8fb55c0d`  |
| 1519   | Layout 1             | `4b4a8fb55c0d`  |
| 1509   | Layout 1             | `4b4a8fb55c0d`  |
| 1506   | Layout 1             | `4b4a8fb55c0d`  |
| 1504   | Layout 1             | `4b4a8fb55c0d`  |
| 1500   | Layout 1             | `4b4a8fb55c0d`  |
| 1493   | Layout 1             | `4b4a8fb55c0d`  |
| 1489   | Layout 1             | `4b4a8fb55c0d`  |
| 1485   | Layout 1             | `4b4a8fb55c0d`  |
| 1481   | Layout 1             | `4b4a8fb55c0d`  |
| 1474   | Layout 1             | `4b4a8fb55c0d`  |
| 1466   | Layout 1             | `4b4a8fb55c0d`  |
| 1462   | Layout 1             | `4b4a8fb55c0d`  |
| 1459   | Layout 1             | `4b4a8fb55c0d`  |
| 1453   | Layout 1             | `4b4a8fb55c0d`  |
| 1450   | Layout 1             | `4b4a8fb55c0d`  |
| 1445   | Layout 1             | `4b4a8fb55c0d`  |
| 1439   | Layout 1             | `4b4a8fb55c0d`  |
| 1433   | Layout 1             | `4b4a8fb55c0d`  |
| 1430   | Layout 1             | `4b4a8fb55c0d`  |
| 1426   | Layout 1             | `4b4a8fb55c0d`  |
| 1421   | Layout 1             | `4b4a8fb55c0d`  |
| 1417   | Layout 1             | `4b4a8fb55c0d`  |
| 1416   | Layout 1             | `4b4a8fb55c0d`  |
| 1409   | Layout 1             | `4b4a8fb55c0d`  |
| 1405   | Layout 1             | `4b4a8fb55c0d`  |
| 1401   | Layout 1             | `4b4a8fb55c0d`  |
| 1396   | Layout 1             | `4b4a8fb55c0d`  |
| 1391   | Layout 1             | `4b4a8fb55c0d`  |
| 1390   | Layout 1             | `4b4a8fb55c0d`  |
| 1386   | Layout 1             | `4b4a8fb55c0d`  |
| 1381   | Layout 1             | `4b4a8fb55c0d`  |
| 1379   | Layout 1             | `4b4a8fb55c0d`  |
| 1372   | Layout 1             | `4b4a8fb55c0d`  |
| 1366   | Layout 1             | `4b4a8fb55c0d`  |
| 1364   | Layout 1             | `4b4a8fb55c0d`  |
| 1363   | Layout 1             | `4b4a8fb55c0d`  |
| 1360   | Layout 1             | `4b4a8fb55c0d`  |
| 1358   | Layout 1             | `4b4a8fb55c0d`  |
| 1355   | Layout 1             | `4b4a8fb55c0d`  |
| 1351   | Layout 1             | `4b4a8fb55c0d`  |
| 1348   | Layout 1             | `4b4a8fb55c0d`  |
| 1346   | Layout 1             | `4b4a8fb55c0d`  |
| 1341   | No documented layout | `4b4a8fb55c0d`  |
| 1340   | No documented layout | `4b4a8fb55c0d`  |
| 1338   | No documented layout | `4b4a8fb55c0d`  |
| 1335   | No documented layout | `4b4a8fb55c0d`  |
| 1333   | No documented layout | `4b4a8fb55c0d`  |
| 1329   | No documented layout | `4b4a8fb55c0d`  |
| 1327   | No documented layout | `4b4a8fb55c0d`  |
| 1324   | No documented layout | `4b4a8fb55c0d`  |
| 1321   | No documented layout | `4b4a8fb55c0d`  |
| 1319   | No documented layout | `4b4a8fb55c0d`  |
| 1318   | No documented layout | `4b4a8fb55c0d`  |
| 1316   | No documented layout | `4b4a8fb55c0d`  |
| 1313   | No documented layout | `4b4a8fb55c0d`  |
| 1311   | No documented layout | `4b4a8fb55c0d`  |
| 1309   | No documented layout | `4b4a8fb55c0d`  |
| 1304   | No documented layout | `4b4a8fb55c0d`  |
| 1292   | No documented layout | `4b4a8fb55c0d`  |
| 1286   | No documented layout | `4b4a8fb55c0d`  |
| 1280   | No documented layout | `4b4a8fb55c0d`  |
| 1276   | No documented layout | `4b4a8fb55c0d`  |
| 1267   | No documented layout | `4b4a8fb55c0d`  |
| 1261   | No file              | `4b4a8fb55c0d`  |
| 1256   | No file              | `4b4a8fb55c0d`  |
| 1250   | No file              | `4b4a8fb55c0d`  |
| 1246   | No file              | `4b4a8fb55c0d`  |
| 1239   | No file              | `4b4a8fb55c0d`  |
| 1230   | No file              | `4b4a8fb55c0d`  |
| 1226   | No file              | `4b4a8fb55c0d`  |
| 1220   | No file              | `4b4a8fb55c0d`  |
| 1217   | No file              | `4b4a8fb55c0d`  |
| 1211   | No file              | `4b4a8fb55c0d`  |
| 1210   | No file              | `4b4a8fb55c0d`  |
| 1208   | No file              | `4b4a8fb55c0d`  |
| 1203   | No file              | `4b4a8fb55c0d`  |
| 1197   | No file              | `4b4a8fb55c0d`  |
| 1194   | No file              | `4b4a8fb55c0d`  |
| 1192   | No file              | `4b4a8fb55c0d`  |
| 1187   | No file              | `4b4a8fb55c0d`  |
| 1183   | No file              | `4b4a8fb55c0d`  |
| 1177   | No file              | `4b4a8fb55c0d`  |
| 1173   | No file              | `4b4a8fb55c0d`  |
| 1167   | No file              | `4b4a8fb55c0d`  |
| 1164   | No file              | `4b4a8fb55c0d`  |
| 1156   | No file              | `4b4a8fb55c0d`  |
| 1149   | No file              | `4b4a8fb55c0d`  |
| 1144   | No file              | `4b4a8fb55c0d`  |
| 1137   | No file              | `4b4a8fb55c0d`  |
| 1132   | No file              | `4b4a8fb55c0d`  |
| 1127   | No file              | `4b4a8fb55c0d`  |
| 1122   | No file              | `4b4a8fb55c0d`  |
| 1118   | No file              | `4b4a8fb55c0d`  |
| 1114   | No file              | `4b4a8fb55c0d`  |
| 1109   | No file              | `4b4a8fb55c0d`  |
| 1102   | No file              | `4b4a8fb55c0d`  |
| 1096   | No file              | `4b4a8fb55c0d`  |
| 1088   | No file              | `4b4a8fb55c0d`  |
| 1081   | No file              | `4b4a8fb55c0d`  |
| 1076   | No file              | `4b4a8fb55c0d`  |
| 1069   | No file              | `4b4a8fb55c0d`  |
| 1064   | No file              | `4b4a8fb55c0d`  |
| 1058   | No file              | `4b4a8fb55c0d`  |
| 1051   | No file              | `4b4a8fb55c0d`  |
| 1044   | No file              | `4b4a8fb55c0d`  |
| 1036   | No file              | `4b4a8fb55c0d`  |
| 1026   | No file              | `4b4a8fb55c0d`  |
| 1016   | No file              | `4b4a8fb55c0d`  |
| 1009   | No file              | `4b4a8fb55c0d`  |
| 1005   | No file              | `4b4a8fb55c0d`  |
| 1000   | No file              | `4b4a8fb55c0d`  |
| 998    | No file              | `4b4a8fb55c0d`  |
| 990    | No file              | `4b4a8fb55c0d`  |
| 979    | No file              | `4b4a8fb55c0d`  |
| 972    | No file              | `4b4a8fb55c0d`  |
| 963    | No file              | `4b4a8fb55c0d`  |
| 955    | No file              | `4b4a8fb55c0d`  |
| 946    | No file              | `4b4a8fb55c0d`  |
| 938    | No file              | `4b4a8fb55c0d`  |
| 927    | No file              | `4b4a8fb55c0d`  |
| 911    | No file              | `4b4a8fb55c0d`  |
| 904    | No file              | `4b4a8fb55c0d`  |
| 899    | No file              | `4b4a8fb55c0d`  |
| 894    | No file              | `4b4a8fb55c0d`  |
| 885    | No file              | `4b4a8fb55c0d`  |
| 879    | No file              | `4b4a8fb55c0d`  |
| 872    | No file              | `4b4a8fb55c0d`  |
| 864    | No file              | `4b4a8fb55c0d`  |
| 855    | No file              | `4b4a8fb55c0d`  |
| 853    | No file              | `4b4a8fb55c0d`  |
| 845    | No file              | `4b4a8fb55c0d`  |
| 837    | No file              | `4b4a8fb55c0d`  |
| 829    | No file              | `4b4a8fb55c0d`  |
| 822    | No file              | `4b4a8fb55c0d`  |
| 814    | No file              | `4b4a8fb55c0d`  |
| 805    | No file              | `4b4a8fb55c0d`  |
| 794    | No file              | `4b4a8fb55c0d`  |
| 787    | No file              | `4b4a8fb55c0d`  |
| 780    | No file              | `4b4a8fb55c0d`  |
| 771    | No file              | `4b4a8fb55c0d`  |
| 760    | No file              | `4b4a8fb55c0d`  |
| 748    | No file              | `4b4a8fb55c0d`  |
| 741    | No file              | `4b4a8fb55c0d`  |
| 736    | No file              | `4b4a8fb55c0d`  |
| 731    | No file              | `4b4a8fb55c0d`  |
| 723    | No file              | `4b4a8fb55c0d`  |
| 711    | No file              | `4b4a8fb55c0d`  |
| 707    | No file              | `4b4a8fb55c0d`  |
| 697    | No file              | `4b4a8fb55c0d`  |
| 689    | No file              | `4b4a8fb55c0d`  |
| 683    | No file              | `4b4a8fb55c0d`  |
| 678    | No file              | `4b4a8fb55c0d`  |
| 670    | No file              | `4b4a8fb55c0d`  |
| 661    | No file              | `4b4a8fb55c0d`  |
| 656    | No file              | `4b4a8fb55c0d`  |
| 652    | No file              | `4b4a8fb55c0d`  |
| 643    | No file              | `4b4a8fb55c0d`  |
| 637    | No file              | `4b4a8fb55c0d`  |
| 630    | No file              | `4b4a8fb55c0d`  |
| 627    | No file              | `4b4a8fb55c0d`  |
| 621    | No file              | `4b4a8fb55c0d`  |
| 617    | No file              | `4b4a8fb55c0d`  |
| 615    | No file              | `4b4a8fb55c0d`  |
| 606    | No file              | `4b4a8fb55c0d`  |
| 599    | No file              | `4b4a8fb55c0d`  |
| 592    | No file              | `4b4a8fb55c0d`  |
| 586    | No file              | `4b4a8fb55c0d`  |
| 577    | No file              | `4b4a8fb55c0d`  |
| 569    | No file              | `4b4a8fb55c0d`  |
| 561    | No file              | `4b4a8fb55c0d`  |
| 554    | No file              | `4b4a8fb55c0d`  |
| 542    | No file              | `4b4a8fb55c0d`  |
| 532    | No file              | `4b4a8fb55c0d`  |
| 531    | No file              | `4b4a8fb55c0d`  |
| 526    | No file              | `4b4a8fb55c0d`  |
| 521    | No file              | `4b4a8fb55c0d`  |
| 517    | No file              | `4b4a8fb55c0d`  |
| 510    | No file              | `4b4a8fb55c0d`  |
| 508    | No file              | `4b4a8fb55c0d`  |
| 504    | No file              | `4b4a8fb55c0d`  |
| 497    | No file              | `4b4a8fb55c0d`  |
| 491    | No file              | `4b4a8fb55c0d`  |
| 485    | No file              | `4b4a8fb55c0d`  |
| 478    | No file              | `4b4a8fb55c0d`  |
| 472    | No file              | `4b4a8fb55c0d`  |
| 466    | No file              | `4b4a8fb55c0d`  |
| 457    | No file              | `4b4a8fb55c0d`  |
| 452    | No file              | `4b4a8fb55c0d`  |
| 449    | No file              | `4b4a8fb55c0d`  |
| 435    | No file              | `4b4a8fb55c0d`  |

<!-- versions:end -->

## Companion Files

None. `producttooloffset.dbss` is the offset file of this table; the
records fill the main file, so the handler reads them in file order without
it. Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup
index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                    |
| ------- | ------------- | ------- | ---------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `22` on client 3474   |
| `+0x04` | Record[count] | records | See Record; not in item or level order   |

There is no `PABR` magic and no trailer: the file is `4 + count x 28` bytes
(620 on client 3474).

### Record (28 bytes)

| Offset  | Type | Field                     | Notes                                                                                   |
| ------- | ---- | ------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key                  | `enchant_level << 24 \| item_id`, as in `itemenchant.dbss`; equals the index row key    |
| `+0x04` | u32  | item_key_dup              | Repeats `item_key` on every record; the index row's `data_offset` points here           |
| `+0x08` | u32  | unknown_08                | `0` on every record (client 3474)                                                       |
| `+0x0C` | u32  | unknown_0c                | `0` on every record (client 3474)                                                       |
| `+0x10` | u32  | unknown_10                | `0` on every record (client 3474)                                                       |
| `+0x14` | u32  | unknown_14                | `0` on every record (client 3474)                                                       |
| `+0x18` | u32  | autofishing_time_percents | Sheet column `AutofishingTimePercents`; `500,000` or `1,000,000` (client 3474)          |

`item_key` is unique. The parser splits it into `item_id` (low 24 bits) and
`enchant_level` (high 8 bits) with `split_item_key()` in
`_common/item_key.py`, and raises an error when `item_key_dup` differs.

### `producttooloffset.dbss`

| Offset  | Type             | Field | Notes                               |
| ------- | ---------------- | ----- | ----------------------------------- |
| `+0x00` | u32              | count | Equals the `producttool.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                       |

The rows are the `[u32 key][u32 offset][u32 size]` rows of a PABR offset
table with no `PABR` magic and no trailer (268 bytes = 4 + 22 x 12 on
client 3474), read by `parse_bare_u32_offset_rows` in
`_common/pabr_offset.py`. They are not in the order of the main file.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | item_key    | The record's `item_key`                                                |
| `+0x04` | u32  | data_offset | Start of the record in the main file plus 4: points at `item_key_dup`  |
| `+0x08` | u32  | data_size   | Record length minus the 4-byte `item_key`: `24`                        |

## Records

The records on client 3474, by item.

| Item ID | Item                                   | Levels | `autofishing_time_percents` |
| ------: | -------------------------------------- | ------ | --------------------------: |
| 16153   | Triple-Float Fishing Rod               | 0      | 1,000,000                   |
| 16169   | Cedar Float                            | 0-10   | 1,000,000                   |
| 17591   | Splendid Silver Fishing Rod            | 0      | 500,000                     |
| 17592   | Splendid Golden Fishing Rod            | 0      | 500,000                     |
| 17596   | [Event] Splendid Golden Fishing Rod    | 0      | 500,000                     |
| 17612   | Lucky Silver Fishing Rod               | 0      | 500,000                     |
| 17613   | Lucky Golden Fishing Rod               | 0      | 500,000                     |
| 17669   | [Event] Splendid Golden Fishing Rod    | 0      | 500,000                     |
| 767158  | Grandpa Cron's Fishing Rod             | 0      | 1,000,000                   |
| 767187  | Cool Wind Fishing Rod                  | 0      | 1,000,000                   |
| 767277  | Dreamy Starlight Fishing Rod (30 Days) | 0      | 1,000,000                   |
| 767671  | Crio's Miraculous Fishing Rod          | 0      | 1,000,000                   |

The item descriptions of 767158, 767187 and 767671 say the rod catches
several fish at once "like with the Triple-Float Fishing Rod". Client 1784
has the same 18 records without the four 767xxx rods.

## Field Names

The record is the `ProductTool_Property` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `ItemKey`, `EnchantLevel`,
`ItemName`, `Param_0` to `Param_3`, `AutofishingTimePercents`). Its 18 rows
match the live file on all 18 shared keys (client 3474): `ItemKey` and
`EnchantLevel` are `item_id` and `enchant_level`, `AutofishingTimePercents`
is `autofishing_time_percents`, and `Param_0` to `Param_3` are `0` as
`unknown_08` to `unknown_14` are. The client 1784 file holds exactly these
18 records. The four 767xxx rods are newer than the sheet. The server dump
(`Instance_dumpFull.exe`) of the same private server names the loader
`LoadProductToolStaticInformation` and stores each record as a
`gc::ProductToolStaticStatus` in a `ProductToolStaticStatusManager` keyed by
`gc::ItemEnchantKey`. The 2016 PDB has no `ProductTool` type.

## Notes

- `1,000,000` is the client's 100% value, `CppDefine.e100Percent` (see
  [guaranteeenchantss](guaranteeenchantss_dbss.md) Notes), and the column
  name ends in `Percents`.
- The value is not the tooltip's auto-fishing line. In my game, the Grandpa
  Cron's Fishing Rod tooltip lists "Auto-fishing Time -80%" under Item
  Effect while its record holds `1,000,000`, the Balenos Fishing Rod
  (16162) lists 25% less auto-fishing time when enhanced and has no record
  here at any level, and the
  Splendid and Lucky Silver and Golden Fishing Rods, which hold `500,000`,
  list no auto-fishing line at all.
- The client calls the stat "Auto-fishing Time": pet items carry
  "(Auto-fishing Time Reduction)" and buff scrolls list "Auto-fishing Time
  -10%" (LOC type 0). `CppEnums.ShowParamBuffType.AutoFishingRate` (`8`) in
  `global_define_cpp_enum.luac` is the buff detail window's auto-fishing
  line; its description list in `panel_characterinfo_buffdetail_all.luac`
  includes `LUA_BUFFDETAIL_DESC_FISHINGROD`.
- Cedar Float is a float, not a rod. Its eleven records store
  `1,000,000` at every level.

## Open Questions

### What `autofishing_time_percents` Does

The sheet names the column `AutofishingTimePercents`, but the tooltips do
not show it (see Notes): a rod with `1,000,000` lists "Auto-fishing Time
-80%", the enhanced Balenos Fishing Rod lists 25% less with no record in this file,
and the rods with `500,000` list no auto-fishing line. It may be a
hidden multiplier on the auto-fishing time that the tooltip leaves out, or
a value the current client no longer uses. No client 3474 `.luac` file
contains the string `ProductTool`. The server dump's `LoadProductToolStaticInformation`
and its callers would show where the value is applied.

### The Four Zero Fields

`unknown_08` to `unknown_14` are `0` on every record of clients 1784 and
3474. The sheet has four columns in that place, `Param_0` to `Param_3`,
also `0` on every row, so the column names carry no meaning to match. A
record with a non-zero value, or the server dump's row reader for
`gc::ProductToolStaticStatus`, would show what they hold.
