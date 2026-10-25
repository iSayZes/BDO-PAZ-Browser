# `itemtradegrouptonpc.dbss` Format

## Purpose

Trade goods per trade NPC: the goods players sell to the NPC, built from the
server's `SellingToNpc_Table` (see [Field Names](#field-names)). The file holds one group per character key of
[`itemtrade.dbss`](itemtrade_dbss.md) (the same 126 keys on client 3464, in another order), and
each group lists items with their trade category. On client 3464 every group
holds one item except 40075 Fish Dad, whose group holds 1,501: trash loot,
fish, trade crates and the old regional trade goods.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes   | Records                     | Row bytes |
| ------ | -------------- | -------------------------------- | ------- | --------------------------- | --------- |
| 2      | 2726 and later | `itemtradegrouptonpc.dbss`       | 207,262 | 1,626 Item Entry, 126 Group | 127       |
| 2      | 2726 and later | `itemtradegrouptonpcoffset.dbss` | 1,264   | 126 Index Row               | 10        |
| 1      | 1329 to 2717   | `itemtradegrouptonpc.dbss`       | 192,751 | 1,561 Item Entry, 124 Group | 123       |
| 1      | 1329 to 2717   | `itemtradegrouptonpcoffset.dbss` | 1,244   | 124 Index Row               | 10        |

| Layout | File                             | Known              | Unknown          |
| ------ | -------------------------------- | ------------------ | ---------------- |
| 2      | `itemtradegrouptonpc.dbss`       | 182,872 B (88.2%)  | 24,390 B (11.8%) |
| 2      | `itemtradegrouptonpcoffset.dbss` | 1,264 B (100.0%)   | 0 B (0.0%)       |
| 1      | `itemtradegrouptonpc.dbss`       | 192,751 B (100.0%) | 0 B (0.0%)       |
| 1      | `itemtradegrouptonpcoffset.dbss` | 1,244 B (100.0%)   | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `fbd0d9e6b76a`  |
| 3482   | Layout 2             | `fbd0d9e6b76a`  |
| 3474   | Layout 2             | `fbd0d9e6b76a`  |
| 3473   | Layout 2             | `fbd0d9e6b76a`  |
| 3464   | Layout 2             | `fbd0d9e6b76a`  |
| 3458   | Layout 2             | `fbd0d9e6b76a`  |
| 3454   | Layout 2             | `fbd0d9e6b76a`  |
| 3444   | Layout 2             | `fbd0d9e6b76a`  |
| 3435   | Layout 2             | `fbd0d9e6b76a`  |
| 3426   | Layout 2             | `fbd0d9e6b76a`  |
| 3418   | Layout 2             | `fbd0d9e6b76a`  |
| 3412   | Layout 2             | `fbd0d9e6b76a`  |
| 3402   | Layout 2             | `fbd0d9e6b76a`  |
| 3396   | Layout 2             | `fbd0d9e6b76a`  |
| 3387   | Layout 2             | `fbd0d9e6b76a`  |
| 3381   | Layout 2             | `fbd0d9e6b76a`  |
| 3373   | Layout 2             | `fbd0d9e6b76a`  |
| 3364   | Layout 2             | `fbd0d9e6b76a`  |
| 3356   | Layout 2             | `fbd0d9e6b76a`  |
| 3349   | Layout 2             | `fbd0d9e6b76a`  |
| 3342   | Layout 2             | `fbd0d9e6b76a`  |
| 3335   | Layout 2             | `fbd0d9e6b76a`  |
| 3326   | Layout 2             | `fbd0d9e6b76a`  |
| 3321   | Layout 2             | `fbd0d9e6b76a`  |
| 3314   | Layout 2             | `fbd0d9e6b76a`  |
| 3303   | Layout 2             | `fbd0d9e6b76a`  |
| 3302   | Layout 2             | `fbd0d9e6b76a`  |
| 3293   | Layout 2             | `fbd0d9e6b76a`  |
| 3283   | Layout 2             | `fbd0d9e6b76a`  |
| 3275   | Layout 2             | `fbd0d9e6b76a`  |
| 3267   | Layout 2             | `fbd0d9e6b76a`  |
| 3258   | Layout 2             | `fbd0d9e6b76a`  |
| 3251   | Layout 2             | `fbd0d9e6b76a`  |
| 3242   | Layout 2             | `fbd0d9e6b76a`  |
| 3235   | Layout 2             | `fbd0d9e6b76a`  |
| 3229   | Layout 2             | `fbd0d9e6b76a`  |
| 3212   | Layout 2             | `fbd0d9e6b76a`  |
| 3203   | Layout 2             | `fbd0d9e6b76a`  |
| 3193   | Layout 2             | `fbd0d9e6b76a`  |
| 3186   | Layout 2             | `fbd0d9e6b76a`  |
| 3177   | Layout 2             | `fbd0d9e6b76a`  |
| 3169   | Layout 2             | `fbd0d9e6b76a`  |
| 3158   | Layout 2             | `fbd0d9e6b76a`  |
| 3151   | Layout 2             | `fbd0d9e6b76a`  |
| 3144   | Layout 2             | `fbd0d9e6b76a`  |
| 3133   | Layout 2             | `fbd0d9e6b76a`  |
| 3125   | Layout 2             | `fbd0d9e6b76a`  |
| 3118   | Layout 2             | `fbd0d9e6b76a`  |
| 3111   | Layout 2             | `fbd0d9e6b76a`  |
| 3103   | Layout 2             | `fbd0d9e6b76a`  |
| 3095   | Layout 2             | `fbd0d9e6b76a`  |
| 3086   | Layout 2             | `fbd0d9e6b76a`  |
| 3072   | Layout 2             | `fbd0d9e6b76a`  |
| 3062   | Layout 2             | `fbd0d9e6b76a`  |
| 3052   | Layout 2             | `fbd0d9e6b76a`  |
| 3045   | Layout 2             | `fbd0d9e6b76a`  |
| 3037   | Layout 2             | `fbd0d9e6b76a`  |
| 3030   | Layout 2             | `fbd0d9e6b76a`  |
| 3021   | Layout 2             | `fbd0d9e6b76a`  |
| 3012   | Layout 2             | `fbd0d9e6b76a`  |
| 3002   | Layout 2             | `fbd0d9e6b76a`  |
| 2995   | Layout 2             | `fbd0d9e6b76a`  |
| 2987   | Layout 2             | `fbd0d9e6b76a`  |
| 2978   | Layout 2             | `fbd0d9e6b76a`  |
| 2970   | Layout 2             | `fbd0d9e6b76a`  |
| 2959   | Layout 2             | `fbd0d9e6b76a`  |
| 2951   | Layout 2             | `fbd0d9e6b76a`  |
| 2942   | Layout 2             | `fbd0d9e6b76a`  |
| 2935   | Layout 2             | `fbd0d9e6b76a`  |
| 2932   | Layout 2             | `fbd0d9e6b76a`  |
| 2923   | Layout 2             | `fbd0d9e6b76a`  |
| 2919   | Layout 2             | `fbd0d9e6b76a`  |
| 2907   | Layout 2             | `fbd0d9e6b76a`  |
| 2900   | Layout 2             | `fbd0d9e6b76a`  |
| 2891   | Layout 2             | `fbd0d9e6b76a`  |
| 2882   | Layout 2             | `fbd0d9e6b76a`  |
| 2872   | Layout 2             | `fbd0d9e6b76a`  |
| 2863   | Layout 2             | `fbd0d9e6b76a`  |
| 2855   | Layout 2             | `fbd0d9e6b76a`  |
| 2849   | Layout 2             | `fbd0d9e6b76a`  |
| 2844   | Layout 2             | `fbd0d9e6b76a`  |
| 2834   | Layout 2             | `fbd0d9e6b76a`  |
| 2825   | Layout 2             | `fbd0d9e6b76a`  |
| 2819   | Layout 2             | `fbd0d9e6b76a`  |
| 2811   | Layout 2             | `fbd0d9e6b76a`  |
| 2803   | Layout 2             | `fbd0d9e6b76a`  |
| 2794   | Layout 2             | `fbd0d9e6b76a`  |
| 2783   | Layout 2             | `fbd0d9e6b76a`  |
| 2774   | Layout 2             | `fbd0d9e6b76a`  |
| 2765   | Layout 2             | `fbd0d9e6b76a`  |
| 2756   | Layout 2             | `fbd0d9e6b76a`  |
| 2750   | Layout 2             | `fbd0d9e6b76a`  |
| 2743   | Layout 2             | `fbd0d9e6b76a`  |
| 2736   | Layout 2             | `fbd0d9e6b76a`  |
| 2726   | Layout 2             | `fbd0d9e6b76a`  |
| 2717   | Layout 1             | `fbd0d9e6b76a`  |
| 2709   | Layout 1             | `fbd0d9e6b76a`  |
| 2703   | Layout 1             | `fbd0d9e6b76a`  |
| 2695   | Layout 1             | `fbd0d9e6b76a`  |
| 2684   | Layout 1             | `fbd0d9e6b76a`  |
| 2672   | Layout 1             | `fbd0d9e6b76a`  |
| 2665   | Layout 1             | `fbd0d9e6b76a`  |
| 2657   | Layout 1             | `fbd0d9e6b76a`  |
| 2649   | Layout 1             | `fbd0d9e6b76a`  |
| 2644   | Layout 1             | `fbd0d9e6b76a`  |
| 2637   | Layout 1             | `fbd0d9e6b76a`  |
| 2629   | Layout 1             | `fbd0d9e6b76a`  |
| 2619   | Layout 1             | `fbd0d9e6b76a`  |
| 2612   | Layout 1             | `fbd0d9e6b76a`  |
| 2606   | Layout 1             | `fbd0d9e6b76a`  |
| 2602   | Layout 1             | `fbd0d9e6b76a`  |
| 2601   | Layout 1             | `fbd0d9e6b76a`  |
| 2592   | Layout 1             | `fbd0d9e6b76a`  |
| 2583   | Layout 1             | `fbd0d9e6b76a`  |
| 2575   | Layout 1             | `fbd0d9e6b76a`  |
| 2567   | Layout 1             | `fbd0d9e6b76a`  |
| 2560   | Layout 1             | `fbd0d9e6b76a`  |
| 2553   | Layout 1             | `fbd0d9e6b76a`  |
| 2545   | Layout 1             | `fbd0d9e6b76a`  |
| 2538   | Layout 1             | `fbd0d9e6b76a`  |
| 2529   | Layout 1             | `fbd0d9e6b76a`  |
| 2519   | Layout 1             | `fbd0d9e6b76a`  |
| 2513   | Layout 1             | `fbd0d9e6b76a`  |
| 2510   | Layout 1             | `fbd0d9e6b76a`  |
| 2507   | Layout 1             | `fbd0d9e6b76a`  |
| 2503   | Layout 1             | `fbd0d9e6b76a`  |
| 2498   | Layout 1             | `fbd0d9e6b76a`  |
| 2492   | Layout 1             | `fbd0d9e6b76a`  |
| 2487   | Layout 1             | `fbd0d9e6b76a`  |
| 2480   | Layout 1             | `fbd0d9e6b76a`  |
| 2474   | Layout 1             | `fbd0d9e6b76a`  |
| 2468   | Layout 1             | `fbd0d9e6b76a`  |
| 2460   | Layout 1             | `fbd0d9e6b76a`  |
| 2453   | Layout 1             | `fbd0d9e6b76a`  |
| 2444   | Layout 1             | `fbd0d9e6b76a`  |
| 2438   | Layout 1             | `fbd0d9e6b76a`  |
| 2434   | Layout 1             | `fbd0d9e6b76a`  |
| 2429   | Layout 1             | `fbd0d9e6b76a`  |
| 2421   | Layout 1             | `fbd0d9e6b76a`  |
| 2414   | Layout 1             | `fbd0d9e6b76a`  |
| 2407   | Layout 1             | `fbd0d9e6b76a`  |
| 2401   | Layout 1             | `fbd0d9e6b76a`  |
| 2397   | Layout 1             | `fbd0d9e6b76a`  |
| 2393   | Layout 1             | `fbd0d9e6b76a`  |
| 2384   | Layout 1             | `fbd0d9e6b76a`  |
| 2378   | Layout 1             | `fbd0d9e6b76a`  |
| 2372   | Layout 1             | `fbd0d9e6b76a`  |
| 2358   | Layout 1             | `fbd0d9e6b76a`  |
| 2352   | Layout 1             | `fbd0d9e6b76a`  |
| 2347   | Layout 1             | `fbd0d9e6b76a`  |
| 2343   | Layout 1             | `fbd0d9e6b76a`  |
| 2335   | Layout 1             | `fbd0d9e6b76a`  |
| 2327   | Layout 1             | `fbd0d9e6b76a`  |
| 2324   | Layout 1             | `fbd0d9e6b76a`  |
| 2319   | Layout 1             | `fbd0d9e6b76a`  |
| 2313   | Layout 1             | `fbd0d9e6b76a`  |
| 2308   | Layout 1             | `fbd0d9e6b76a`  |
| 2302   | Layout 1             | `fbd0d9e6b76a`  |
| 2295   | Layout 1             | `fbd0d9e6b76a`  |
| 2290   | Layout 1             | `fbd0d9e6b76a`  |
| 2284   | Layout 1             | `fbd0d9e6b76a`  |
| 2276   | Layout 1             | `fbd0d9e6b76a`  |
| 2269   | Layout 1             | `fbd0d9e6b76a`  |
| 2259   | Layout 1             | `fbd0d9e6b76a`  |
| 2250   | Layout 1             | `fbd0d9e6b76a`  |
| 2243   | Layout 1             | `fbd0d9e6b76a`  |
| 2235   | Layout 1             | `fbd0d9e6b76a`  |
| 2229   | Layout 1             | `fbd0d9e6b76a`  |
| 2224   | Layout 1             | `fbd0d9e6b76a`  |
| 2218   | Layout 1             | `fbd0d9e6b76a`  |
| 2215   | Layout 1             | `fbd0d9e6b76a`  |
| 2207   | Layout 1             | `fbd0d9e6b76a`  |
| 2203   | Layout 1             | `fbd0d9e6b76a`  |
| 2196   | Layout 1             | `fbd0d9e6b76a`  |
| 2192   | Layout 1             | `fbd0d9e6b76a`  |
| 2189   | Layout 1             | `fbd0d9e6b76a`  |
| 2183   | Layout 1             | `fbd0d9e6b76a`  |
| 2179   | Layout 1             | `fbd0d9e6b76a`  |
| 2171   | Layout 1             | `fbd0d9e6b76a`  |
| 2163   | Layout 1             | `fbd0d9e6b76a`  |
| 2156   | Layout 1             | `fbd0d9e6b76a`  |
| 2151   | Layout 1             | `fbd0d9e6b76a`  |
| 2147   | Layout 1             | `fbd0d9e6b76a`  |
| 2142   | Layout 1             | `fbd0d9e6b76a`  |
| 2138   | Layout 1             | `fbd0d9e6b76a`  |
| 2134   | Layout 1             | `fbd0d9e6b76a`  |
| 2130   | Layout 1             | `fbd0d9e6b76a`  |
| 2122   | Layout 1             | `fbd0d9e6b76a`  |
| 2107   | Layout 1             | `fbd0d9e6b76a`  |
| 2098   | Layout 1             | `fbd0d9e6b76a`  |
| 2089   | Layout 1             | `fbd0d9e6b76a`  |
| 2081   | Layout 1             | `fbd0d9e6b76a`  |
| 2073   | Layout 1             | `fbd0d9e6b76a`  |
| 2067   | Layout 1             | `fbd0d9e6b76a`  |
| 2063   | Layout 1             | `fbd0d9e6b76a`  |
| 2059   | Layout 1             | `fbd0d9e6b76a`  |
| 2052   | Layout 1             | `fbd0d9e6b76a`  |
| 2044   | Layout 1             | `fbd0d9e6b76a`  |
| 2039   | Layout 1             | `fbd0d9e6b76a`  |
| 2032   | Layout 1             | `fbd0d9e6b76a`  |
| 2025   | Layout 1             | `fbd0d9e6b76a`  |
| 2011   | Layout 1             | `fbd0d9e6b76a`  |
| 2005   | Layout 1             | `fbd0d9e6b76a`  |
| 2000   | Layout 1             | `fbd0d9e6b76a`  |
| 1996   | Layout 1             | `fbd0d9e6b76a`  |
| 1991   | Layout 1             | `fbd0d9e6b76a`  |
| 1985   | Layout 1             | `fbd0d9e6b76a`  |
| 1980   | Layout 1             | `fbd0d9e6b76a`  |
| 1969   | Layout 1             | `fbd0d9e6b76a`  |
| 1964   | Layout 1             | `fbd0d9e6b76a`  |
| 1958   | Layout 1             | `fbd0d9e6b76a`  |
| 1950   | Layout 1             | `fbd0d9e6b76a`  |
| 1945   | Layout 1             | `fbd0d9e6b76a`  |
| 1937   | Layout 1             | `fbd0d9e6b76a`  |
| 1933   | Layout 1             | `fbd0d9e6b76a`  |
| 1927   | Layout 1             | `fbd0d9e6b76a`  |
| 1921   | Layout 1             | `fbd0d9e6b76a`  |
| 1914   | Layout 1             | `fbd0d9e6b76a`  |
| 1908   | Layout 1             | `fbd0d9e6b76a`  |
| 1897   | Layout 1             | `fbd0d9e6b76a`  |
| 1892   | Layout 1             | `fbd0d9e6b76a`  |
| 1886   | Layout 1             | `fbd0d9e6b76a`  |
| 1881   | Layout 1             | `fbd0d9e6b76a`  |
| 1871   | Layout 1             | `fbd0d9e6b76a`  |
| 1866   | Layout 1             | `fbd0d9e6b76a`  |
| 1862   | Layout 1             | `fbd0d9e6b76a`  |
| 1854   | Layout 1             | `fbd0d9e6b76a`  |
| 1846   | Layout 1             | `fbd0d9e6b76a`  |
| 1838   | Layout 1             | `fbd0d9e6b76a`  |
| 1832   | Layout 1             | `fbd0d9e6b76a`  |
| 1826   | Layout 1             | `fbd0d9e6b76a`  |
| 1822   | Layout 1             | `fbd0d9e6b76a`  |
| 1818   | Layout 1             | `fbd0d9e6b76a`  |
| 1804   | Layout 1             | `fbd0d9e6b76a`  |
| 1794   | Layout 1             | `fbd0d9e6b76a`  |
| 1790   | Layout 1             | `fbd0d9e6b76a`  |
| 1784   | Layout 1             | `fbd0d9e6b76a`  |
| 1774   | Layout 1             | `fbd0d9e6b76a`  |
| 1771   | Layout 1             | `fbd0d9e6b76a`  |
| 1762   | Layout 1             | `fbd0d9e6b76a`  |
| 1759   | Layout 1             | `fbd0d9e6b76a`  |
| 1754   | Layout 1             | `fbd0d9e6b76a`  |
| 1749   | Layout 1             | `fbd0d9e6b76a`  |
| 1743   | Layout 1             | `fbd0d9e6b76a`  |
| 1737   | Layout 1             | `fbd0d9e6b76a`  |
| 1731   | Layout 1             | `fbd0d9e6b76a`  |
| 1725   | Layout 1             | `fbd0d9e6b76a`  |
| 1717   | Layout 1             | `fbd0d9e6b76a`  |
| 1710   | Layout 1             | `fbd0d9e6b76a`  |
| 1704   | Layout 1             | `fbd0d9e6b76a`  |
| 1698   | Layout 1             | `fbd0d9e6b76a`  |
| 1690   | Layout 1             | `fbd0d9e6b76a`  |
| 1685   | Layout 1             | `fbd0d9e6b76a`  |
| 1680   | Layout 1             | `fbd0d9e6b76a`  |
| 1674   | Layout 1             | `fbd0d9e6b76a`  |
| 1668   | Layout 1             | `fbd0d9e6b76a`  |
| 1659   | Layout 1             | `fbd0d9e6b76a`  |
| 1649   | Layout 1             | `fbd0d9e6b76a`  |
| 1642   | Layout 1             | `fbd0d9e6b76a`  |
| 1636   | Layout 1             | `fbd0d9e6b76a`  |
| 1628   | Layout 1             | `fbd0d9e6b76a`  |
| 1622   | Layout 1             | `fbd0d9e6b76a`  |
| 1614   | Layout 1             | `fbd0d9e6b76a`  |
| 1608   | Layout 1             | `fbd0d9e6b76a`  |
| 1602   | Layout 1             | `fbd0d9e6b76a`  |
| 1598   | Layout 1             | `fbd0d9e6b76a`  |
| 1594   | Layout 1             | `fbd0d9e6b76a`  |
| 1590   | Layout 1             | `fbd0d9e6b76a`  |
| 1587   | Layout 1             | `fbd0d9e6b76a`  |
| 1584   | Layout 1             | `fbd0d9e6b76a`  |
| 1579   | Layout 1             | `fbd0d9e6b76a`  |
| 1572   | Layout 1             | `fbd0d9e6b76a`  |
| 1565   | Layout 1             | `fbd0d9e6b76a`  |
| 1559   | Layout 1             | `fbd0d9e6b76a`  |
| 1554   | Layout 1             | `fbd0d9e6b76a`  |
| 1547   | Layout 1             | `fbd0d9e6b76a`  |
| 1537   | Layout 1             | `fbd0d9e6b76a`  |
| 1529   | Layout 1             | `fbd0d9e6b76a`  |
| 1524   | Layout 1             | `fbd0d9e6b76a`  |
| 1519   | Layout 1             | `fbd0d9e6b76a`  |
| 1509   | Layout 1             | `fbd0d9e6b76a`  |
| 1506   | Layout 1             | `fbd0d9e6b76a`  |
| 1504   | Layout 1             | `fbd0d9e6b76a`  |
| 1500   | Layout 1             | `fbd0d9e6b76a`  |
| 1493   | Layout 1             | `fbd0d9e6b76a`  |
| 1489   | Layout 1             | `fbd0d9e6b76a`  |
| 1485   | Layout 1             | `fbd0d9e6b76a`  |
| 1481   | Layout 1             | `fbd0d9e6b76a`  |
| 1474   | Layout 1             | `fbd0d9e6b76a`  |
| 1466   | Layout 1             | `fbd0d9e6b76a`  |
| 1462   | Layout 1             | `fbd0d9e6b76a`  |
| 1459   | Layout 1             | `fbd0d9e6b76a`  |
| 1453   | Layout 1             | `fbd0d9e6b76a`  |
| 1450   | Layout 1             | `fbd0d9e6b76a`  |
| 1445   | Layout 1             | `fbd0d9e6b76a`  |
| 1439   | Layout 1             | `fbd0d9e6b76a`  |
| 1433   | Layout 1             | `fbd0d9e6b76a`  |
| 1430   | Layout 1             | `fbd0d9e6b76a`  |
| 1426   | Layout 1             | `fbd0d9e6b76a`  |
| 1421   | Layout 1             | `fbd0d9e6b76a`  |
| 1417   | Layout 1             | `fbd0d9e6b76a`  |
| 1416   | Layout 1             | `fbd0d9e6b76a`  |
| 1409   | Layout 1             | `fbd0d9e6b76a`  |
| 1405   | Layout 1             | `fbd0d9e6b76a`  |
| 1401   | Layout 1             | `fbd0d9e6b76a`  |
| 1396   | Layout 1             | `fbd0d9e6b76a`  |
| 1391   | Layout 1             | `fbd0d9e6b76a`  |
| 1390   | Layout 1             | `fbd0d9e6b76a`  |
| 1386   | Layout 1             | `fbd0d9e6b76a`  |
| 1381   | Layout 1             | `fbd0d9e6b76a`  |
| 1379   | Layout 1             | `fbd0d9e6b76a`  |
| 1372   | Layout 1             | `fbd0d9e6b76a`  |
| 1366   | Layout 1             | `fbd0d9e6b76a`  |
| 1364   | Layout 1             | `fbd0d9e6b76a`  |
| 1363   | Layout 1             | `fbd0d9e6b76a`  |
| 1360   | Layout 1             | `fbd0d9e6b76a`  |
| 1358   | Layout 1             | `fbd0d9e6b76a`  |
| 1355   | Layout 1             | `fbd0d9e6b76a`  |
| 1351   | Layout 1             | `fbd0d9e6b76a`  |
| 1348   | Layout 1             | `fbd0d9e6b76a`  |
| 1346   | Layout 1             | `fbd0d9e6b76a`  |
| 1341   | Layout 1             | `fbd0d9e6b76a`  |
| 1340   | Layout 1             | `fbd0d9e6b76a`  |
| 1338   | Layout 1             | `fbd0d9e6b76a`  |
| 1335   | Layout 1             | `fbd0d9e6b76a`  |
| 1333   | Layout 1             | `fbd0d9e6b76a`  |
| 1329   | Layout 1             | `fbd0d9e6b76a`  |
| 1327   | No file              | `fbd0d9e6b76a`  |
| 1324   | No file              | `fbd0d9e6b76a`  |
| 1321   | No file              | `fbd0d9e6b76a`  |
| 1319   | No file              | `fbd0d9e6b76a`  |
| 1318   | No file              | `fbd0d9e6b76a`  |
| 1316   | No file              | `fbd0d9e6b76a`  |
| 1313   | No file              | `fbd0d9e6b76a`  |
| 1311   | No documented layout | `fbd0d9e6b76a`  |
| 1309   | No documented layout | `fbd0d9e6b76a`  |
| 1304   | No documented layout | `fbd0d9e6b76a`  |
| 1292   | No documented layout | `fbd0d9e6b76a`  |
| 1286   | No documented layout | `fbd0d9e6b76a`  |
| 1280   | No documented layout | `fbd0d9e6b76a`  |
| 1276   | No documented layout | `fbd0d9e6b76a`  |
| 1267   | No file              | `fbd0d9e6b76a`  |
| 1261   | No file              | `fbd0d9e6b76a`  |
| 1256   | No file              | `fbd0d9e6b76a`  |
| 1250   | No file              | `fbd0d9e6b76a`  |
| 1246   | No file              | `fbd0d9e6b76a`  |
| 1239   | No file              | `fbd0d9e6b76a`  |
| 1230   | No file              | `fbd0d9e6b76a`  |
| 1226   | No file              | `fbd0d9e6b76a`  |
| 1220   | No file              | `fbd0d9e6b76a`  |
| 1217   | No file              | `fbd0d9e6b76a`  |
| 1211   | No file              | `fbd0d9e6b76a`  |
| 1210   | No file              | `fbd0d9e6b76a`  |
| 1208   | No file              | `fbd0d9e6b76a`  |
| 1203   | No file              | `fbd0d9e6b76a`  |
| 1197   | No file              | `fbd0d9e6b76a`  |
| 1194   | No file              | `fbd0d9e6b76a`  |
| 1192   | No file              | `fbd0d9e6b76a`  |
| 1187   | No file              | `fbd0d9e6b76a`  |
| 1183   | No file              | `fbd0d9e6b76a`  |
| 1177   | No file              | `fbd0d9e6b76a`  |
| 1173   | No file              | `fbd0d9e6b76a`  |
| 1167   | No file              | `fbd0d9e6b76a`  |
| 1164   | No file              | `fbd0d9e6b76a`  |
| 1156   | No file              | `fbd0d9e6b76a`  |
| 1149   | No file              | `fbd0d9e6b76a`  |
| 1144   | No file              | `fbd0d9e6b76a`  |
| 1137   | No file              | `fbd0d9e6b76a`  |
| 1132   | No file              | `fbd0d9e6b76a`  |
| 1127   | No file              | `fbd0d9e6b76a`  |
| 1122   | No file              | `fbd0d9e6b76a`  |
| 1118   | No file              | `fbd0d9e6b76a`  |
| 1114   | No file              | `fbd0d9e6b76a`  |
| 1109   | No file              | `fbd0d9e6b76a`  |
| 1102   | No file              | `fbd0d9e6b76a`  |
| 1096   | No file              | `fbd0d9e6b76a`  |
| 1088   | No file              | `fbd0d9e6b76a`  |
| 1081   | No file              | `fbd0d9e6b76a`  |
| 1076   | No file              | `fbd0d9e6b76a`  |
| 1069   | No file              | `fbd0d9e6b76a`  |
| 1064   | No file              | `fbd0d9e6b76a`  |
| 1058   | No file              | `fbd0d9e6b76a`  |
| 1051   | No file              | `fbd0d9e6b76a`  |
| 1044   | No file              | `fbd0d9e6b76a`  |
| 1036   | No file              | `fbd0d9e6b76a`  |
| 1026   | No file              | `fbd0d9e6b76a`  |
| 1016   | No file              | `fbd0d9e6b76a`  |
| 1009   | No file              | `fbd0d9e6b76a`  |
| 1005   | No file              | `fbd0d9e6b76a`  |
| 1000   | No file              | `fbd0d9e6b76a`  |
| 998    | No file              | `fbd0d9e6b76a`  |
| 990    | No file              | `fbd0d9e6b76a`  |
| 979    | No file              | `fbd0d9e6b76a`  |
| 972    | No file              | `fbd0d9e6b76a`  |
| 963    | No file              | `fbd0d9e6b76a`  |
| 955    | No file              | `fbd0d9e6b76a`  |
| 946    | No file              | `fbd0d9e6b76a`  |
| 938    | No file              | `fbd0d9e6b76a`  |
| 927    | No file              | `fbd0d9e6b76a`  |
| 911    | No file              | `fbd0d9e6b76a`  |
| 904    | No file              | `fbd0d9e6b76a`  |
| 899    | No file              | `fbd0d9e6b76a`  |
| 894    | No file              | `fbd0d9e6b76a`  |
| 885    | No file              | `fbd0d9e6b76a`  |
| 879    | No file              | `fbd0d9e6b76a`  |
| 872    | No file              | `fbd0d9e6b76a`  |
| 864    | No file              | `fbd0d9e6b76a`  |
| 855    | No file              | `fbd0d9e6b76a`  |
| 853    | No file              | `fbd0d9e6b76a`  |
| 845    | No file              | `fbd0d9e6b76a`  |
| 837    | No file              | `fbd0d9e6b76a`  |
| 829    | No file              | `fbd0d9e6b76a`  |
| 822    | No file              | `fbd0d9e6b76a`  |
| 814    | No file              | `fbd0d9e6b76a`  |
| 805    | No file              | `fbd0d9e6b76a`  |
| 794    | No file              | `fbd0d9e6b76a`  |
| 787    | No file              | `fbd0d9e6b76a`  |
| 780    | No file              | `fbd0d9e6b76a`  |
| 771    | No file              | `fbd0d9e6b76a`  |
| 760    | No file              | `fbd0d9e6b76a`  |
| 748    | No file              | `fbd0d9e6b76a`  |
| 741    | No file              | `fbd0d9e6b76a`  |
| 736    | No file              | `fbd0d9e6b76a`  |
| 731    | No file              | `fbd0d9e6b76a`  |
| 723    | No file              | `fbd0d9e6b76a`  |
| 711    | No file              | `fbd0d9e6b76a`  |
| 707    | No file              | `fbd0d9e6b76a`  |
| 697    | No file              | `fbd0d9e6b76a`  |
| 689    | No file              | `fbd0d9e6b76a`  |
| 683    | No file              | `fbd0d9e6b76a`  |
| 678    | No file              | `fbd0d9e6b76a`  |
| 670    | No file              | `fbd0d9e6b76a`  |
| 661    | No file              | `fbd0d9e6b76a`  |
| 656    | No file              | `fbd0d9e6b76a`  |
| 652    | No file              | `fbd0d9e6b76a`  |
| 643    | No file              | `fbd0d9e6b76a`  |
| 637    | No file              | `fbd0d9e6b76a`  |
| 630    | No file              | `fbd0d9e6b76a`  |
| 627    | No file              | `fbd0d9e6b76a`  |
| 621    | No file              | `fbd0d9e6b76a`  |
| 617    | No file              | `fbd0d9e6b76a`  |
| 615    | No file              | `fbd0d9e6b76a`  |
| 606    | No file              | `fbd0d9e6b76a`  |
| 599    | No file              | `fbd0d9e6b76a`  |
| 592    | No file              | `fbd0d9e6b76a`  |
| 586    | No file              | `fbd0d9e6b76a`  |
| 577    | No file              | `fbd0d9e6b76a`  |
| 569    | No file              | `fbd0d9e6b76a`  |
| 561    | No file              | `fbd0d9e6b76a`  |
| 554    | No file              | `fbd0d9e6b76a`  |
| 542    | No file              | `fbd0d9e6b76a`  |
| 532    | No file              | `fbd0d9e6b76a`  |
| 531    | No file              | `fbd0d9e6b76a`  |
| 526    | No file              | `fbd0d9e6b76a`  |
| 521    | No file              | `fbd0d9e6b76a`  |
| 517    | No file              | `fbd0d9e6b76a`  |
| 510    | No file              | `fbd0d9e6b76a`  |
| 508    | No file              | `fbd0d9e6b76a`  |
| 504    | No file              | `fbd0d9e6b76a`  |
| 497    | No file              | `fbd0d9e6b76a`  |
| 491    | No file              | `fbd0d9e6b76a`  |
| 485    | No file              | `fbd0d9e6b76a`  |
| 478    | No file              | `fbd0d9e6b76a`  |
| 472    | No file              | `fbd0d9e6b76a`  |
| 466    | No file              | `fbd0d9e6b76a`  |
| 457    | No file              | `fbd0d9e6b76a`  |
| 452    | No file              | `fbd0d9e6b76a`  |
| 449    | No file              | `fbd0d9e6b76a`  |
| 435    | No file              | `fbd0d9e6b76a`  |

<!-- versions:end -->

## Companion Files

None. The handler walks the groups in file order and does not need
`itemtradegrouptonpcoffset.dbss` (see below). NPC names come from LOC type `6`
(`_common/character.py`), item names from LOC type `0`, and the category
names from LOC type `37` under the `RESOURCE` sheet keys listed in
[Commerce Types](#commerce-types).

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. The groups fill the file to its last
byte.

| Offset  | Type         | Field  | Notes                                  |
| ------- | ------------ | ------ | -------------------------------------- |
| `+0x00` | u32          | count  | Number of groups; `126` on client 3464 |
| `+0x04` | Group[count] | groups | See Group                              |

### Group (variable: 6 bytes + item entries)

| Offset  | Type                   | Field        | Notes                                  |
| ------- | ---------------------- | ------------ | -------------------------------------- |
| `+0x00` | u16                    | character_id | Character key, LOC type `6`            |
| `+0x02` | u32                    | item_count   | Number of item entries                 |
| `+0x06` | Item Entry[item_count] | entries      | See Item Entry                         |

### Item Entry (127 bytes)

| Offset  | Type      | Field                            | Notes                                                              |
| ------- | --------- | -------------------------------- | ------------------------------------------------------------------ |
| `+0x00` | u16       | character_id                     | Repeats the group key                                              |
| `+0x02` | u32       | item_id                          | Item key, LOC type `0`; the top byte is `0` in every entry         |
| `+0x06` | u64       | condition_length                 | `0` in every entry on client 3474: the count of the `condition` string of Layout 1, with no text after it |
| `+0x0E` | i32       | max_price_rate                   | `0` in every entry on client 3474, as is every field up to `trade_group_type` |
| `+0x12` | i32       | event_max_price_rate             |                                                                    |
| `+0x16` | i32       | min_price_rate                   |                                                                    |
| `+0x1A` | i32       | steady_price_rate                |                                                                    |
| `+0x1E` | i32       | vary_amount_rate_per_sell_or_buy |                                                                    |
| `+0x22` | i32       | vary_amount_rate_per_tick        |                                                                    |
| `+0x26` | i32       | event_price_rate_per_tick        |                                                                    |
| `+0x2A` | i32       | price_maintain_tick              |                                                                    |
| `+0x2E` | i64       | steady_price_tick_count          |                                                                    |
| `+0x36` | u8        | trade_group_type                 | `1`, `2`, `3` or `99`, see [Trade Group Types](#trade-group-types) |
| `+0x37` | u8        | is_sell_to_npc                   | `1` in every entry (`test_every_entry_is_sold_to_the_npc`)         |
| `+0x38` | i64       | min_price                        | `0` in every entry on client 3474, as is every field up to `territory_supply_no` |
| `+0x40` | i64       | max_price                        |                                                                    |
| `+0x48` | i64       | buyable_stock_amount_per_tick    |                                                                    |
| `+0x50` | i32       | intimacy_variation               |                                                                    |
| `+0x54` | u8        | is_individual                    |                                                                    |
| `+0x55` | i16       | exploration_point                |                                                                    |
| `+0x57` | i32       | get_exp_rate                     |                                                                    |
| `+0x5B` | i64       | min_stock_amount                 |                                                                    |
| `+0x63` | i64       | max_stock_amount                 |                                                                    |
| `+0x6B` | u16       | territory_supply_no              | `0` or a three-digit code, see Open Questions                      |
| `+0x6D` | bytes[15] | unknown_6d                       | All `0` on client 3474; Layout 1 has 11 bytes here, see [Field Names](#field-names) |
| `+0x7C` | u8        | trade_type                       | The item's `trade_type` in [`itemenchant.dbss`](itemenchant_dbss.md), `0` when it has none (`test_trade_type_is_the_item_trade_type`) |
| `+0x7D` | u8        | commerce_type                    | Trade category, see [Commerce Types](#commerce-types)              |
| `+0x7E` | u8        | price_type                       | The item's price type; `0` in every entry on client 3474           |

### `itemtradegrouptonpcoffset.dbss`

The bare u16 index layout of `petexpoffset.dbss`, read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtradegrouptonpc.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row; no trailer                   |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                               |
| ------- | ---- | ------------ | --------------------------------------------------- |
| `+0x00` | u16  | character_id | Group key                                           |
| `+0x02` | u32  | offset       | Start of the group header in the data file          |
| `+0x06` | u32  | size         | Whole group: `6 + 127 * item_count`                 |

The index rows are in neither key nor file order; each points at its own
group (`test_every_offset_row_points_at_its_group`).

## Layout 1

Client 1784 item entries hold a `condition` string at `+0x06`, and the 11
bytes after `territory_supply_no` are 15 bytes on client 3473. On client
1784, 33 entries in 11 groups hold a condition such as
`!checkTerritory(229)`; the other 1,107 hold an empty one, the 8 zero bytes of
`condition_length` in Layout 2. Only the Item Entry differs from Layout 2.

### Item Entry (variable: 123 bytes + condition text)

| Offset           | Type  | Field                            | Notes                                                        |
| ---------------- | ----- | -------------------------------- | ------------------------------------------------------------ |
| `+0x00`          | u16   | character_id                     |                                                              |
| `+0x02`          | u32   | item_id                          |                                                              |
| `+0x06`          | str16 | condition                        | Empty, or `!checkTerritory(N)` with a territory key          |
| `condition+0x00` | i32   | max_price_rate                   | `0` in every entry on client 1784, as is every field up to `trade_group_type` |
| `condition+0x04` | i32   | event_max_price_rate             |                                                              |
| `condition+0x08` | i32   | min_price_rate                   |                                                              |
| `condition+0x0C` | i32   | steady_price_rate                |                                                              |
| `condition+0x10` | i32   | vary_amount_rate_per_sell_or_buy |                                                              |
| `condition+0x14` | i32   | vary_amount_rate_per_tick        |                                                              |
| `condition+0x18` | i32   | event_price_rate_per_tick        |                                                              |
| `condition+0x1C` | i32   | price_maintain_tick              |                                                              |
| `condition+0x20` | i64   | steady_price_tick_count          |                                                              |
| `condition+0x28` | u8    | trade_group_type                 |                                                              |
| `condition+0x29` | u8    | is_sell_to_npc                   | `1` in every entry                                           |
| `condition+0x2A` | i64   | min_price                        | `0` in every entry on client 1784, as is every field up to `territory_supply_no` |
| `condition+0x32` | i64   | max_price                        |                                                              |
| `condition+0x3A` | i64   | buyable_stock_amount_per_tick    |                                                              |
| `condition+0x42` | i32   | intimacy_variation               |                                                              |
| `condition+0x46` | u8    | is_individual                    |                                                              |
| `condition+0x47` | i16   | exploration_point                |                                                              |
| `condition+0x49` | i32   | get_exp_rate                     |                                                              |
| `condition+0x4D` | i64   | min_stock_amount                 |                                                              |
| `condition+0x55` | i64   | max_stock_amount                 |                                                              |
| `condition+0x5D` | u16   | territory_supply_no              |                                                              |
| `condition+0x5F` | u16   | territory_trade_no               | `0` in every entry on client 1784, as is every field up to `trade_type` |
| `condition+0x61` | i32   | get_selling_trade_exp_rate       |                                                              |
| `condition+0x65` | i32   | event_price_rate_per_sell        |                                                              |
| `condition+0x69` | u8    | is_for_magnate                   |                                                              |
| `condition+0x6A` | u8    | trade_type                       |                                                              |
| `condition+0x6B` | u8    | commerce_type                    |                                                              |
| `condition+0x6C` | u8    | price_type                       | `0` in every entry on client 1784                            |

## Field Names

The server dump of a private server on client 1784
(`Instance_dumpFull.exe`) reads the client file into
`ItemTradeGroupStaticStatus` rows of 184 bytes:
`ItemTradeGroupToNpcStaticStatusManager::readFromBinarybyDynamic()` (from VA
`0x140b80e30`) calls the group reader at VA `0x140b7ffa0`, which reads each
entry with the row reader at VA `0x140b7ea70`. The row reader copies the
fields above in file order into members `+0x00` to `+0xb7`. The 2016 client's
debug symbols (`BlackDesert64.pdb`) list the same members in the same order
as `gc::ItemTradeGroupValue` up to `_eventPriceRatePerSell`; that struct also
holds an item pointer and the parsed condition list. The sheet
loader at VA `0x1408b66c0` fills the members from the `SellingToNpc_Table`
sheet, or from `BuyingFromNpc_Table` when its flag argument is set:

| Field                              | Member  | 2016 member                    | Sheet column                 |
| ---------------------------------- | ------- | ------------------------------ | ---------------------------- |
| `character_id`                     | `+0x00` | `_npcKey`                      | `NPCKey`                     |
| `item_id`                          | `+0x04` | `_itemKey`                     | `ItemKey`                    |
| `condition`                        | `+0x08` | `_conditionString`             | `Condition`                  |
| `max_price_rate`                   | `+0x40` | `_maxPriceRate`                | `MaxPriceRate`               |
| `event_max_price_rate`             | `+0x44` | `_eventMaxPriceRate`           | `EvnetMaxPriceRate`          |
| `min_price_rate`                   | `+0x48` | `_minPriceRate`                | `MinPriceRate`               |
| `steady_price_rate`                | `+0x4c` | `_steadyPriceRate`             | `SteadyPriceRate`            |
| `vary_amount_rate_per_sell_or_buy` | `+0x50` | `_varyAmountRatePerSellOrBuy`  | `varyAmountRatePerSellOrBuy` |
| `vary_amount_rate_per_tick`        | `+0x54` | `_varyAmountRatePerTick`       | `varyAmountRatePerTick`      |
| `event_price_rate_per_tick`        | `+0x58` | `_eventvaryAmountRatePerTick`  | `EvnetPriceRatePerTick`      |
| `price_maintain_tick`              | `+0x5c` | `_priceMaintainTick`           | `PriceMaintainTick`          |
| `steady_price_tick_count`          | `+0x60` | `_steadyPriceTickCount`        | `SteadyPriceTickCount`       |
| `trade_group_type`                 | `+0x68` | `_tradeGroupType`              | `TradeGroupType`             |
| `is_sell_to_npc`                   | `+0x69` | `_isSellToNpc`                 | none                         |
| `min_price`                        | `+0x70` | `_minPrice`                    | none                         |
| `max_price`                        | `+0x78` | `_maxPrice`                    | none                         |
| `buyable_stock_amount_per_tick`    | `+0x80` | `_buyableStockAmountPerTick`   | `BuyableStockAmountPerTick`  |
| `intimacy_variation`               | `+0x88` | `_intimacyVariation`           | `IntimacyVariation`          |
| `is_individual`                    | `+0x8c` | `_isIndividual`                | none                         |
| `exploration_point`                | `+0x8e` | `_explorationPoint`            | `ExplorationPoint`           |
| `get_exp_rate`                     | `+0x90` | `_getExpRate`                  | `GetExpRate`                 |
| `min_stock_amount`                 | `+0x98` | `_minStockAmount`              | `MinStockAmount`             |
| `max_stock_amount`                 | `+0xa0` | `_maxStockAmount`              | `MaxStockAmount`             |
| `territory_supply_no`              | `+0xa8` | `_territorySupplyNo`           | `TerritorySupply_No`         |
| `territory_trade_no`               | `+0xaa` | `_territoryTradeNo`            | `TerritoryTrade_No`          |
| `get_selling_trade_exp_rate`       | `+0xac` | `_getSellingTradeExpRate`      | `GetSellingTradeExpRate`     |
| `event_price_rate_per_sell`        | `+0xb0` | `_eventPriceRatePerSell`       | `EventPriceRatePerSell`      |
| `is_for_magnate`                   | `+0xb4` | none                           | `IsForMagnate`               |
| `trade_type`                       | `+0xb5` | none                           | `Item_Table` `TradeType`     |
| `commerce_type`                    | `+0xb6` | none                           | `Item_Table` `CommerceType`  |
| `price_type`                       | `+0xb7` | none                           | `Item_Table` `PriceType`     |

The members without a sheet column are set in code:

- For `SellingToNpc_Table` the loader writes `1` to `is_sell_to_npc` after
  the last column (VA `0x1408b751f`). For both sheets it sets
  `is_individual` when `BuyableStockAmountPerTick` is above `0` (VA
  `0x1408b752d`).
- The loader reads `BuyableStockAmountPerTick`, `IntimacyVariation`,
  `TerritoryTrade_No` and `IsForMagnate` only from `BuyingFromNpc_Table`,
  and `EvnetMaxPriceRate`, `EventPriceRatePerSell`,
  `EvnetPriceRatePerTick`, `ExplorationPoint`, `GetExpRate`,
  `MinStockAmount`, `MaxStockAmount`, `TerritorySupply_No`,
  `GetSellingTradeExpRate` and `TradeGroupType` only from
  `SellingToNpc_Table`.
- After reading the file, the reader calls the function at VA
  `0x140b7f240`, which sets `min_price` and `max_price` from `MinPriceRate`
  and `MaxPriceRate` times the item's `OriginalPrice`, and copies three item
  members into `+0xb5` to `+0xb7`. The `Item_Table` loader writes
  `TradeType` to the item's `+0x40c` (VA `0x140897c4a`), `PriceType` to
  `+0x415` (VA `0x140897dd2`) and `CommerceType` to `+0x419` (VA
  `0x14089848a`). The loader does not read the `commerceType` column of
  `SellingToNpc_Table`.

The names that rest on values:

- `condition`, `trade_group_type` and `territory_supply_no` equal the
  `Condition`, `TradeGroupType` and `TerritorySupply_No` columns of that
  private server's `SellingToNpc_Table` on all 1,140 entries of the official
  client 1784 file, joined on `NPCKey` and `ItemKey`.
- `trade_type` and `commerce_type` equal `TradeType` and `CommerceType` of
  the entry's item in the server's `Item_Table` on all 1,140 entries. On
  client 3474, `trade_type` equals the item's `trade_type` in
  `itemenchant.dbss` on all 1,626 entries.
- `is_sell_to_npc` is `1` in every entry of this file on clients 1784 and
  3474. The same byte is `0` in every entry of the client 1784
  `itemtradegroupfromnpc.dbss`, the table the `BuyingFromNpc_Table` side
  fills.
- On client 3474, the 142 items that carry a `territory_supply_no` on both
  clients carry the same code as on client 1784.

The other fields are `0` in every entry of both clients, so their names rest
on the member order and widths of the row reader alone. Their columns in the
developer sheet (`datasheet_tradedatatable.xlsm`) are server-only (`%`), or
belong to `BuyingFromNpc_Table` only, or the member has no column. The
client 1784 [`itemtradegroupfromnpc.dbss`](itemtradegroupfromnpc_dbss.md#field-names),
read by the same row reader, fills `territory_trade_no` and `is_for_magnate`
from `BuyingFromNpc_Table` and matches both columns on all 451 entries, which
places the Layout 1 members after `territory_supply_no` by value. In Layout
2, every field up to `territory_supply_no` sits where Layout 1 has it after
an empty `condition`, and the last three bytes keep their order; the names of
the zero fields there rest on that order. Layout 2 has 4 more bytes in
`unknown_6d`, so where `territory_trade_no`, `get_selling_trade_exp_rate`,
`event_price_rate_per_sell` and `is_for_magnate` sit in it is open.

## Commerce Types

`panel_tooltip_item.luac` defines `enCommerceType` and names each value with a
`RESOURCE` sheet key of `stringtable.bss`; the item tooltip adds that name
after `Trade Item`, and the trade market tabs use the same keys. Every
`commerce_type` on client 3464 is `1` to `9`.

| Value | Enum name            | Key                                           | English          |
| ----- | -------------------- | --------------------------------------------- | ---------------- |
| 1     | Luxury_Miscellaneous | `TRADEMARKET_GRAPH_BTN_MISCELL`               | General Goods    |
| 2     | Luxury               | `TRADEMARKET_GRAPH_BTN_LUXURY`                | Luxury           |
| 3     | Grocery              | `TRADEMARKET_GRAPH_BTN_GROCERY`               | Food             |
| 4     | Medicine             | `TRADEMARKET_GRAPH_BTN_MEDICINE`              | Medicine         |
| 5     | MilitarySupplies     | `PANEL_TRADEMARKET_GRAPH_BTN_MILITARYSUPPLIES` | Military Supply  |
| 6     | ObjectSaint          | `TRADEMARKET_GRAPH_BTN_OBJECT`                | Relic            |
| 7     | Cloth                | `PANEL_TRADEMARKET_GRAPH_BTN_CLOTH`           | Clothes          |
| 8     | SeaFood              | `TRADEMARKET_GRAPH_BTN_SEAFOOD`               | Seafood          |
| 9     | RawMaterial          | `PANEL_TRADEMARKET_GRAPH_BTN_RAWMATERIAL`     | Raw Material     |

`10` is `enCommerceType_Max`. The handler stores the key hashes in
`commerce_types.py`, and `test_commerce_type_hashes_match_stringtable` checks
them against `stringtable.bss`.

## Trade Group Types

`trade_group_type` is the code that
[`itemtradeetc.bss`](itemtradeetc_bss.md) pairs for the desert trade buff:
the trade sell list (`panel_dialog_trade_mybasket_all_1.luac`) passes the
trade item's `getTradeGroupType()` and the trade NPC's to
`ToClient_TradeGroupFromToAddPercent` and `ToClient_TradeGroupFromToDistance`,
and `itemtradeetc.bss` holds pairs of exactly these four codes. The client
does not name the codes. On client 3464:

| Code | Entries (client 3464)                                                                    |
| ---- | ---------------------------------------------------------------------------------------- |
| 1    | 122 of the 125 one-item groups; 233 Fish Dad entries, the regional goods 55101 to 55402  |
| 2    | The groups of 45011 Yis Kunjamin and 45012 Burita Allon, the Valencia City trade managers |
| 3    | The group of 45209 Shuriar, the Ibellab Oasis trade manager                              |
| 99   | The other 1,268 Fish Dad entries, such as 55001 Ancient Gold Coin and 8201 Mudskipper    |

Valencia City and Ibellab Oasis are the two places the client's text gives
the desert trade bonus (see the `itemtradeetc.bss` notes).

The labels the tables show with each code (`1 Other Regions`,
`2 Valencia City`, `3 Ibellab Oasis`, `99 Shared Goods`) are our wording, not
the game's: the client has no name for any code. The place names use the
client's words for the two places; `Other Regions` and `Shared Goods` are
ours. The labels live in `_common/lang/` (`tradeGroups`).

## Notes

- On client 3464 the 125 one-item groups hold items from 810442 to 810559,
  and every one of their LOC descriptions ends `This item is currently
  unavailable.` Their names read as variants of the old regional goods in
  the Fish Dad group: 40010 Bahar has 810442 Fragrant Grape Wine, which
  shows the icon of 55102 Velian Wine. Some groups share an item: 810533
  Gem-Laden Dagger sits under 47747 Isobelle Encarotia, 47651 Roig Mills,
  62137 Kario and 45306 Sophia.
- The 40075 Fish Dad group on client 3464, by `commerce_type`: 159 General
  Goods, 75 Luxury, 664 Food, 89 Medicine, 22 Military Supply, 15 Relic, 25
  Clothes, 309 Seafood, 143 Raw Material. It holds 1,481 distinct items: the
  20 items 810560 to 810579 (`Packaged Dried Leaffish` to `Packaged Dried
  Redfin Anthias`) appear twice, byte for byte.
- Its items include 55001 Ancient Gold Coin, whose description reads
  `Trade Managers would buy this for a high price.`, fish such as 8201
  Mudskipper, the Imperial cooking and alchemy boxes (9801 to 9871) and the
  six `[Guild]` trade crates (9921 to 9925 and 9943).
- `trade_type` is `0` on every one-item group. On the Fish Dad group (client
  3464) it is `3` on the 54 Imperial cooking and alchemy boxes, `4` on 108
  fish such as 8202 Tuna and `5` on the six `[Guild]` trade crates; the
  [`itemenchant.dbss`](itemenchant_dbss.md) notes list what each value means.
- `itemtradegroupfromnpc.dbss` and its offset table are empty on client
  3473 and hold groups of this file's Layout 1 shape on client 1784 (see
  [itemtradegroupfromnpc](itemtradegroupfromnpc_dbss.md)).

## Open Questions

### What the territory_supply_no Code Means

The server names the field `TerritorySupply_No` (see
[Field Names](#field-names)). It is a decimal code: `0`, or hundreds `0` to
`7` with the last two digits `11` to `15` (`11`, `111`, `213`, `515`,
`714`). An NPC group and the Fish Dad goods of the same town share a code:
40010 Bahar (Velia) and Velian Smoked Chicken, Velian Wine and Velian Plank
carry `111`; 41090 Larc and the Fogan and Glish goods carry `213`. On client
3464, 70 of the 125 one-item groups carry a code (19 of them `515`) and 142
of the 1,501 Fish Dad entries. The server's `CharacterFunction_Table` names
the NPCs with a `TerritorySupplyName` "황실 납품" (Imperial Delivery) and gives
each a `TerritoryKeyForTerritorySupply` of `0` to `8`. Which territory or
delivery the hundreds digit and the last two digits select is open.

### Why Fish Dad Holds the Shared List

40075 Fish Dad has no `characterfunction.dbss` or `npcsimply.bss` record (see
the `itemtrade.dbss` notes), yet its group holds the trash loot, fish and
crates trade managers take. Whether the client applies this group to every
trade NPC is open.
