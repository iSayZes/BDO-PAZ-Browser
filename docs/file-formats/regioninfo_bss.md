# `regioninfo.bss` Format

## Purpose

Stores every world region: towns, hunting grounds, castles, arenas, caves and sea areas. The primary key is a region key that resolves through LOC `str_type=17` (the region name). Each record also carries the region type, the node war day, the territory and its capital, the region group, the worldmap node the region belongs to, the zone flags (safe zone, sea, desert, prison and others), the region buff skills by day and night, the return point and, for 20 port regions, the Guild Wharf Manager NPC.

The layout follows [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, section 11). I walked it against the client 3458 file: every record tiles exactly up to the string table and every span it calls reserved is zero in all 1594 records. One tail field is split wrongly there (see Region Tail). Field meanings marked confirmed below were checked against LOC, the client's Lua enums and the linked tables; the extractor's other names stay `unknown_*` here.

Most of the zone flags and keys are named from two more sources (see Field Names below): the 2016 client's debug symbols, whose `gc::RegionInfo` lists its members in the order this record stores them, and the server-side `Region_Table` of a private server on client 519, whose columns match these offsets value for value. Five more of the extractor's names turned out wrong that way (`+0x0E`, `+0x10`, `+0x11`, `+0x1B`, `+0x66`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes   | Records                                            | Row bytes |
| ------ | -------------- | ---------------- | ------- | -------------------------------------------------- | --------- |
| 2      | 2978 and later | `regioninfo.bss` | 643,669 | 1,595 Region Head, 1,595 Region Tail, 1,595 Region | 210       |
| 1      | 1762 to 1838   | `regioninfo.bss` | 555,972 | 1,063 Region Head, 1,063 Region Tail, 1,063 Region | 361       |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 2      | `regioninfo.bss` | 244,883 B (38.0%) | 398,786 B (62.0%) |
| 1      | `regioninfo.bss` | 161,067 B (29.0%) | 394,905 B (71.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `a17e5f1d2955`  |
| 3482   | Layout 2             | `a17e5f1d2955`  |
| 3474   | Layout 2             | `a17e5f1d2955`  |
| 3473   | Layout 2             | `a17e5f1d2955`  |
| 3464   | Layout 2             | `a17e5f1d2955`  |
| 3458   | Layout 2             | `a17e5f1d2955`  |
| 3454   | Layout 2             | `a17e5f1d2955`  |
| 3444   | Layout 2             | `a17e5f1d2955`  |
| 3435   | Layout 2             | `a17e5f1d2955`  |
| 3426   | Layout 2             | `a17e5f1d2955`  |
| 3418   | Layout 2             | `a17e5f1d2955`  |
| 3412   | Layout 2             | `a17e5f1d2955`  |
| 3402   | Layout 2             | `a17e5f1d2955`  |
| 3396   | Layout 2             | `a17e5f1d2955`  |
| 3387   | Layout 2             | `a17e5f1d2955`  |
| 3381   | Layout 2             | `a17e5f1d2955`  |
| 3373   | Layout 2             | `a17e5f1d2955`  |
| 3364   | Layout 2             | `a17e5f1d2955`  |
| 3356   | Layout 2             | `a17e5f1d2955`  |
| 3349   | Layout 2             | `a17e5f1d2955`  |
| 3342   | Layout 2             | `a17e5f1d2955`  |
| 3335   | Layout 2             | `a17e5f1d2955`  |
| 3326   | Layout 2             | `a17e5f1d2955`  |
| 3321   | Layout 2             | `a17e5f1d2955`  |
| 3314   | Layout 2             | `a17e5f1d2955`  |
| 3303   | Layout 2             | `a17e5f1d2955`  |
| 3302   | Layout 2             | `a17e5f1d2955`  |
| 3293   | Layout 2             | `a17e5f1d2955`  |
| 3283   | Layout 2             | `a17e5f1d2955`  |
| 3275   | Layout 2             | `a17e5f1d2955`  |
| 3267   | Layout 2             | `a17e5f1d2955`  |
| 3258   | Layout 2             | `a17e5f1d2955`  |
| 3251   | Layout 2             | `a17e5f1d2955`  |
| 3242   | Layout 2             | `a17e5f1d2955`  |
| 3235   | Layout 2             | `a17e5f1d2955`  |
| 3229   | Layout 2             | `a17e5f1d2955`  |
| 3212   | Layout 2             | `a17e5f1d2955`  |
| 3203   | Layout 2             | `a17e5f1d2955`  |
| 3193   | Layout 2             | `a17e5f1d2955`  |
| 3186   | Layout 2             | `a17e5f1d2955`  |
| 3177   | Layout 2             | `a17e5f1d2955`  |
| 3169   | Layout 2             | `a17e5f1d2955`  |
| 3158   | Layout 2             | `a17e5f1d2955`  |
| 3151   | Layout 2             | `a17e5f1d2955`  |
| 3144   | Layout 2             | `a17e5f1d2955`  |
| 3133   | Layout 2             | `a17e5f1d2955`  |
| 3125   | Layout 2             | `a17e5f1d2955`  |
| 3118   | Layout 2             | `a17e5f1d2955`  |
| 3111   | Layout 2             | `a17e5f1d2955`  |
| 3103   | Layout 2             | `a17e5f1d2955`  |
| 3095   | Layout 2             | `a17e5f1d2955`  |
| 3086   | Layout 2             | `a17e5f1d2955`  |
| 3072   | Layout 2             | `a17e5f1d2955`  |
| 3062   | Layout 2             | `a17e5f1d2955`  |
| 3052   | Layout 2             | `a17e5f1d2955`  |
| 3045   | Layout 2             | `a17e5f1d2955`  |
| 3037   | Layout 2             | `a17e5f1d2955`  |
| 3030   | Layout 2             | `a17e5f1d2955`  |
| 3021   | Layout 2             | `a17e5f1d2955`  |
| 3012   | Layout 2             | `a17e5f1d2955`  |
| 3002   | Layout 2             | `a17e5f1d2955`  |
| 2995   | Layout 2             | `a17e5f1d2955`  |
| 2987   | Layout 2             | `a17e5f1d2955`  |
| 2978   | Layout 2             | `a17e5f1d2955`  |
| 2970   | No documented layout | `a17e5f1d2955`  |
| 2959   | No documented layout | `a17e5f1d2955`  |
| 2951   | No documented layout | `a17e5f1d2955`  |
| 2942   | No documented layout | `a17e5f1d2955`  |
| 2935   | No documented layout | `a17e5f1d2955`  |
| 2932   | No documented layout | `a17e5f1d2955`  |
| 2923   | No documented layout | `a17e5f1d2955`  |
| 2919   | No documented layout | `a17e5f1d2955`  |
| 2907   | No documented layout | `a17e5f1d2955`  |
| 2900   | No documented layout | `a17e5f1d2955`  |
| 2891   | No documented layout | `a17e5f1d2955`  |
| 2882   | No documented layout | `a17e5f1d2955`  |
| 2872   | No documented layout | `a17e5f1d2955`  |
| 2863   | No documented layout | `a17e5f1d2955`  |
| 2855   | No documented layout | `a17e5f1d2955`  |
| 2849   | No documented layout | `a17e5f1d2955`  |
| 2844   | No documented layout | `a17e5f1d2955`  |
| 2834   | No documented layout | `a17e5f1d2955`  |
| 2825   | No documented layout | `a17e5f1d2955`  |
| 2819   | No documented layout | `a17e5f1d2955`  |
| 2811   | No documented layout | `a17e5f1d2955`  |
| 2803   | No documented layout | `a17e5f1d2955`  |
| 2794   | No documented layout | `a17e5f1d2955`  |
| 2783   | No documented layout | `a17e5f1d2955`  |
| 2774   | No documented layout | `a17e5f1d2955`  |
| 2765   | No documented layout | `a17e5f1d2955`  |
| 2756   | No documented layout | `a17e5f1d2955`  |
| 2750   | No documented layout | `a17e5f1d2955`  |
| 2743   | No documented layout | `a17e5f1d2955`  |
| 2736   | No documented layout | `a17e5f1d2955`  |
| 2726   | No documented layout | `a17e5f1d2955`  |
| 2717   | No documented layout | `a17e5f1d2955`  |
| 2709   | No documented layout | `a17e5f1d2955`  |
| 2703   | No documented layout | `a17e5f1d2955`  |
| 2695   | No documented layout | `a17e5f1d2955`  |
| 2684   | No documented layout | `a17e5f1d2955`  |
| 2672   | No documented layout | `a17e5f1d2955`  |
| 2665   | No documented layout | `a17e5f1d2955`  |
| 2657   | No documented layout | `a17e5f1d2955`  |
| 2649   | No documented layout | `a17e5f1d2955`  |
| 2644   | No documented layout | `a17e5f1d2955`  |
| 2637   | No documented layout | `a17e5f1d2955`  |
| 2629   | No documented layout | `a17e5f1d2955`  |
| 2619   | No documented layout | `a17e5f1d2955`  |
| 2612   | No documented layout | `a17e5f1d2955`  |
| 2606   | No documented layout | `a17e5f1d2955`  |
| 2602   | No documented layout | `a17e5f1d2955`  |
| 2601   | No documented layout | `a17e5f1d2955`  |
| 2592   | No documented layout | `a17e5f1d2955`  |
| 2583   | No documented layout | `a17e5f1d2955`  |
| 2575   | No documented layout | `a17e5f1d2955`  |
| 2567   | No documented layout | `a17e5f1d2955`  |
| 2560   | No documented layout | `a17e5f1d2955`  |
| 2553   | No documented layout | `a17e5f1d2955`  |
| 2545   | No documented layout | `a17e5f1d2955`  |
| 2538   | No documented layout | `a17e5f1d2955`  |
| 2529   | No documented layout | `a17e5f1d2955`  |
| 2519   | No documented layout | `a17e5f1d2955`  |
| 2513   | No documented layout | `a17e5f1d2955`  |
| 2510   | No documented layout | `a17e5f1d2955`  |
| 2507   | No documented layout | `a17e5f1d2955`  |
| 2503   | No documented layout | `a17e5f1d2955`  |
| 2498   | No documented layout | `a17e5f1d2955`  |
| 2492   | No documented layout | `a17e5f1d2955`  |
| 2487   | No documented layout | `a17e5f1d2955`  |
| 2480   | No documented layout | `a17e5f1d2955`  |
| 2474   | No documented layout | `a17e5f1d2955`  |
| 2468   | No documented layout | `a17e5f1d2955`  |
| 2460   | No documented layout | `a17e5f1d2955`  |
| 2453   | No documented layout | `a17e5f1d2955`  |
| 2444   | No documented layout | `a17e5f1d2955`  |
| 2438   | No documented layout | `a17e5f1d2955`  |
| 2434   | No documented layout | `a17e5f1d2955`  |
| 2429   | No documented layout | `a17e5f1d2955`  |
| 2421   | No documented layout | `a17e5f1d2955`  |
| 2414   | No documented layout | `a17e5f1d2955`  |
| 2407   | No documented layout | `a17e5f1d2955`  |
| 2401   | No documented layout | `a17e5f1d2955`  |
| 2397   | No documented layout | `a17e5f1d2955`  |
| 2393   | No documented layout | `a17e5f1d2955`  |
| 2384   | No documented layout | `a17e5f1d2955`  |
| 2378   | No documented layout | `a17e5f1d2955`  |
| 2372   | No documented layout | `a17e5f1d2955`  |
| 2358   | No documented layout | `a17e5f1d2955`  |
| 2352   | No documented layout | `a17e5f1d2955`  |
| 2347   | No documented layout | `a17e5f1d2955`  |
| 2343   | No documented layout | `a17e5f1d2955`  |
| 2335   | No documented layout | `a17e5f1d2955`  |
| 2327   | No documented layout | `a17e5f1d2955`  |
| 2324   | No documented layout | `a17e5f1d2955`  |
| 2319   | No documented layout | `a17e5f1d2955`  |
| 2313   | No documented layout | `a17e5f1d2955`  |
| 2308   | No documented layout | `a17e5f1d2955`  |
| 2302   | No documented layout | `a17e5f1d2955`  |
| 2295   | No documented layout | `a17e5f1d2955`  |
| 2290   | No documented layout | `a17e5f1d2955`  |
| 2284   | No documented layout | `a17e5f1d2955`  |
| 2276   | No documented layout | `a17e5f1d2955`  |
| 2269   | No documented layout | `a17e5f1d2955`  |
| 2259   | No documented layout | `a17e5f1d2955`  |
| 2250   | No documented layout | `a17e5f1d2955`  |
| 2243   | No documented layout | `a17e5f1d2955`  |
| 2235   | No documented layout | `a17e5f1d2955`  |
| 2229   | No documented layout | `a17e5f1d2955`  |
| 2224   | No documented layout | `a17e5f1d2955`  |
| 2218   | No documented layout | `a17e5f1d2955`  |
| 2215   | No documented layout | `a17e5f1d2955`  |
| 2207   | No documented layout | `a17e5f1d2955`  |
| 2203   | No documented layout | `a17e5f1d2955`  |
| 2196   | No documented layout | `a17e5f1d2955`  |
| 2192   | No documented layout | `a17e5f1d2955`  |
| 2189   | No documented layout | `a17e5f1d2955`  |
| 2183   | No documented layout | `a17e5f1d2955`  |
| 2179   | No documented layout | `a17e5f1d2955`  |
| 2171   | No documented layout | `a17e5f1d2955`  |
| 2163   | No documented layout | `a17e5f1d2955`  |
| 2156   | No documented layout | `a17e5f1d2955`  |
| 2151   | No documented layout | `a17e5f1d2955`  |
| 2147   | No documented layout | `a17e5f1d2955`  |
| 2142   | No documented layout | `a17e5f1d2955`  |
| 2138   | No documented layout | `a17e5f1d2955`  |
| 2134   | No documented layout | `a17e5f1d2955`  |
| 2130   | No documented layout | `a17e5f1d2955`  |
| 2122   | No documented layout | `a17e5f1d2955`  |
| 2107   | No documented layout | `a17e5f1d2955`  |
| 2098   | No documented layout | `a17e5f1d2955`  |
| 2089   | No documented layout | `a17e5f1d2955`  |
| 2081   | No documented layout | `a17e5f1d2955`  |
| 2073   | No documented layout | `a17e5f1d2955`  |
| 2067   | No documented layout | `a17e5f1d2955`  |
| 2063   | No documented layout | `a17e5f1d2955`  |
| 2059   | No documented layout | `a17e5f1d2955`  |
| 2052   | No documented layout | `a17e5f1d2955`  |
| 2044   | No documented layout | `a17e5f1d2955`  |
| 2039   | No documented layout | `a17e5f1d2955`  |
| 2032   | No documented layout | `a17e5f1d2955`  |
| 2025   | No documented layout | `a17e5f1d2955`  |
| 2011   | No documented layout | `a17e5f1d2955`  |
| 2005   | No documented layout | `a17e5f1d2955`  |
| 2000   | No documented layout | `a17e5f1d2955`  |
| 1996   | No documented layout | `a17e5f1d2955`  |
| 1991   | No documented layout | `a17e5f1d2955`  |
| 1985   | No documented layout | `a17e5f1d2955`  |
| 1980   | No documented layout | `a17e5f1d2955`  |
| 1969   | No documented layout | `a17e5f1d2955`  |
| 1964   | No documented layout | `a17e5f1d2955`  |
| 1958   | No documented layout | `a17e5f1d2955`  |
| 1950   | No documented layout | `a17e5f1d2955`  |
| 1945   | No documented layout | `a17e5f1d2955`  |
| 1937   | No documented layout | `a17e5f1d2955`  |
| 1933   | No documented layout | `a17e5f1d2955`  |
| 1927   | No documented layout | `a17e5f1d2955`  |
| 1921   | No documented layout | `a17e5f1d2955`  |
| 1914   | No documented layout | `a17e5f1d2955`  |
| 1908   | No documented layout | `a17e5f1d2955`  |
| 1897   | No documented layout | `a17e5f1d2955`  |
| 1892   | No documented layout | `a17e5f1d2955`  |
| 1886   | No documented layout | `a17e5f1d2955`  |
| 1881   | No documented layout | `a17e5f1d2955`  |
| 1871   | No documented layout | `a17e5f1d2955`  |
| 1866   | No documented layout | `a17e5f1d2955`  |
| 1862   | No documented layout | `a17e5f1d2955`  |
| 1854   | No documented layout | `a17e5f1d2955`  |
| 1846   | No documented layout | `a17e5f1d2955`  |
| 1838   | Layout 1             | `a17e5f1d2955`  |
| 1832   | Layout 1             | `a17e5f1d2955`  |
| 1826   | Layout 1             | `a17e5f1d2955`  |
| 1822   | Layout 1             | `a17e5f1d2955`  |
| 1818   | Layout 1             | `a17e5f1d2955`  |
| 1804   | Layout 1             | `a17e5f1d2955`  |
| 1794   | Layout 1             | `a17e5f1d2955`  |
| 1790   | Layout 1             | `a17e5f1d2955`  |
| 1784   | Layout 1             | `a17e5f1d2955`  |
| 1774   | Layout 1             | `a17e5f1d2955`  |
| 1771   | Layout 1             | `a17e5f1d2955`  |
| 1762   | Layout 1             | `a17e5f1d2955`  |
| 1759   | No documented layout | `a17e5f1d2955`  |
| 1754   | No documented layout | `a17e5f1d2955`  |
| 1749   | No documented layout | `a17e5f1d2955`  |
| 1743   | No documented layout | `a17e5f1d2955`  |
| 1737   | No documented layout | `a17e5f1d2955`  |
| 1731   | No documented layout | `a17e5f1d2955`  |
| 1725   | No documented layout | `a17e5f1d2955`  |
| 1717   | No documented layout | `a17e5f1d2955`  |
| 1710   | No documented layout | `a17e5f1d2955`  |
| 1704   | No documented layout | `a17e5f1d2955`  |
| 1698   | No documented layout | `a17e5f1d2955`  |
| 1690   | No documented layout | `a17e5f1d2955`  |
| 1685   | No documented layout | `a17e5f1d2955`  |
| 1680   | No documented layout | `a17e5f1d2955`  |
| 1674   | No documented layout | `a17e5f1d2955`  |
| 1668   | No documented layout | `a17e5f1d2955`  |
| 1659   | No documented layout | `a17e5f1d2955`  |
| 1649   | No documented layout | `a17e5f1d2955`  |
| 1642   | No documented layout | `a17e5f1d2955`  |
| 1636   | No documented layout | `a17e5f1d2955`  |
| 1628   | No documented layout | `a17e5f1d2955`  |
| 1622   | No documented layout | `a17e5f1d2955`  |
| 1614   | No documented layout | `a17e5f1d2955`  |
| 1608   | No documented layout | `a17e5f1d2955`  |
| 1602   | No documented layout | `a17e5f1d2955`  |
| 1598   | No documented layout | `a17e5f1d2955`  |
| 1594   | No documented layout | `a17e5f1d2955`  |
| 1590   | No documented layout | `a17e5f1d2955`  |
| 1587   | No documented layout | `a17e5f1d2955`  |
| 1584   | No documented layout | `a17e5f1d2955`  |
| 1579   | No documented layout | `a17e5f1d2955`  |
| 1572   | No documented layout | `a17e5f1d2955`  |
| 1565   | No documented layout | `a17e5f1d2955`  |
| 1559   | No documented layout | `a17e5f1d2955`  |
| 1554   | No documented layout | `a17e5f1d2955`  |
| 1547   | No documented layout | `a17e5f1d2955`  |
| 1537   | No documented layout | `a17e5f1d2955`  |
| 1529   | No documented layout | `a17e5f1d2955`  |
| 1524   | No documented layout | `a17e5f1d2955`  |
| 1519   | No documented layout | `a17e5f1d2955`  |
| 1509   | No documented layout | `a17e5f1d2955`  |
| 1506   | No documented layout | `a17e5f1d2955`  |
| 1504   | No documented layout | `a17e5f1d2955`  |
| 1500   | No documented layout | `a17e5f1d2955`  |
| 1493   | No documented layout | `a17e5f1d2955`  |
| 1489   | No documented layout | `a17e5f1d2955`  |
| 1485   | No documented layout | `a17e5f1d2955`  |
| 1481   | No documented layout | `a17e5f1d2955`  |
| 1474   | No documented layout | `a17e5f1d2955`  |
| 1466   | No documented layout | `a17e5f1d2955`  |
| 1462   | No documented layout | `a17e5f1d2955`  |
| 1459   | No documented layout | `a17e5f1d2955`  |
| 1453   | No documented layout | `a17e5f1d2955`  |
| 1450   | No documented layout | `a17e5f1d2955`  |
| 1445   | No documented layout | `a17e5f1d2955`  |
| 1439   | No documented layout | `a17e5f1d2955`  |
| 1433   | No documented layout | `a17e5f1d2955`  |
| 1430   | No documented layout | `a17e5f1d2955`  |
| 1426   | No documented layout | `a17e5f1d2955`  |
| 1421   | No documented layout | `a17e5f1d2955`  |
| 1417   | No documented layout | `a17e5f1d2955`  |
| 1416   | No documented layout | `a17e5f1d2955`  |
| 1409   | No documented layout | `a17e5f1d2955`  |
| 1405   | No documented layout | `a17e5f1d2955`  |
| 1401   | No documented layout | `a17e5f1d2955`  |
| 1396   | No documented layout | `a17e5f1d2955`  |
| 1391   | No documented layout | `a17e5f1d2955`  |
| 1390   | No documented layout | `a17e5f1d2955`  |
| 1386   | No documented layout | `a17e5f1d2955`  |
| 1381   | No documented layout | `a17e5f1d2955`  |
| 1379   | No documented layout | `a17e5f1d2955`  |
| 1372   | No documented layout | `a17e5f1d2955`  |
| 1366   | No documented layout | `a17e5f1d2955`  |
| 1364   | No documented layout | `a17e5f1d2955`  |
| 1363   | No documented layout | `a17e5f1d2955`  |
| 1360   | No documented layout | `a17e5f1d2955`  |
| 1358   | No documented layout | `a17e5f1d2955`  |
| 1355   | No documented layout | `a17e5f1d2955`  |
| 1351   | No documented layout | `a17e5f1d2955`  |
| 1348   | No documented layout | `a17e5f1d2955`  |
| 1346   | No documented layout | `a17e5f1d2955`  |
| 1341   | No documented layout | `a17e5f1d2955`  |
| 1340   | No documented layout | `a17e5f1d2955`  |
| 1338   | No documented layout | `a17e5f1d2955`  |
| 1335   | No documented layout | `a17e5f1d2955`  |
| 1333   | No documented layout | `a17e5f1d2955`  |
| 1329   | No documented layout | `a17e5f1d2955`  |
| 1327   | No documented layout | `a17e5f1d2955`  |
| 1324   | No documented layout | `a17e5f1d2955`  |
| 1321   | No documented layout | `a17e5f1d2955`  |
| 1319   | No documented layout | `a17e5f1d2955`  |
| 1318   | No documented layout | `a17e5f1d2955`  |
| 1316   | No documented layout | `a17e5f1d2955`  |
| 1313   | No documented layout | `a17e5f1d2955`  |
| 1311   | No documented layout | `a17e5f1d2955`  |
| 1309   | No documented layout | `a17e5f1d2955`  |
| 1304   | No documented layout | `a17e5f1d2955`  |
| 1292   | No documented layout | `a17e5f1d2955`  |
| 1286   | No documented layout | `a17e5f1d2955`  |
| 1280   | No documented layout | `a17e5f1d2955`  |
| 1276   | No documented layout | `a17e5f1d2955`  |
| 1267   | No documented layout | `a17e5f1d2955`  |
| 1261   | No documented layout | `a17e5f1d2955`  |
| 1256   | No documented layout | `a17e5f1d2955`  |
| 1250   | No documented layout | `a17e5f1d2955`  |
| 1246   | No documented layout | `a17e5f1d2955`  |
| 1239   | No documented layout | `a17e5f1d2955`  |
| 1230   | No documented layout | `a17e5f1d2955`  |
| 1226   | No documented layout | `a17e5f1d2955`  |
| 1220   | No documented layout | `a17e5f1d2955`  |
| 1217   | No documented layout | `a17e5f1d2955`  |
| 1211   | No documented layout | `a17e5f1d2955`  |
| 1210   | No documented layout | `a17e5f1d2955`  |
| 1208   | No documented layout | `a17e5f1d2955`  |
| 1203   | No documented layout | `a17e5f1d2955`  |
| 1197   | No documented layout | `a17e5f1d2955`  |
| 1194   | No documented layout | `a17e5f1d2955`  |
| 1192   | No documented layout | `a17e5f1d2955`  |
| 1187   | No documented layout | `a17e5f1d2955`  |
| 1183   | No documented layout | `a17e5f1d2955`  |
| 1177   | No documented layout | `a17e5f1d2955`  |
| 1173   | No documented layout | `a17e5f1d2955`  |
| 1167   | No documented layout | `a17e5f1d2955`  |
| 1164   | No documented layout | `a17e5f1d2955`  |
| 1156   | No documented layout | `a17e5f1d2955`  |
| 1149   | No documented layout | `a17e5f1d2955`  |
| 1144   | No documented layout | `a17e5f1d2955`  |
| 1137   | No documented layout | `a17e5f1d2955`  |
| 1132   | No documented layout | `a17e5f1d2955`  |
| 1127   | No documented layout | `a17e5f1d2955`  |
| 1122   | No documented layout | `a17e5f1d2955`  |
| 1118   | No documented layout | `a17e5f1d2955`  |
| 1114   | No documented layout | `a17e5f1d2955`  |
| 1109   | No documented layout | `a17e5f1d2955`  |
| 1102   | No file              | `a17e5f1d2955`  |
| 1096   | No file              | `a17e5f1d2955`  |
| 1088   | No file              | `a17e5f1d2955`  |
| 1081   | No file              | `a17e5f1d2955`  |
| 1076   | No file              | `a17e5f1d2955`  |
| 1069   | No file              | `a17e5f1d2955`  |
| 1064   | No file              | `a17e5f1d2955`  |
| 1058   | No file              | `a17e5f1d2955`  |
| 1051   | No file              | `a17e5f1d2955`  |
| 1044   | No file              | `a17e5f1d2955`  |
| 1036   | No file              | `a17e5f1d2955`  |
| 1026   | No file              | `a17e5f1d2955`  |
| 1016   | No file              | `a17e5f1d2955`  |
| 1009   | No file              | `a17e5f1d2955`  |
| 1005   | No file              | `a17e5f1d2955`  |
| 1000   | No file              | `a17e5f1d2955`  |
| 998    | No file              | `a17e5f1d2955`  |
| 990    | No file              | `a17e5f1d2955`  |
| 979    | No file              | `a17e5f1d2955`  |
| 972    | No file              | `a17e5f1d2955`  |
| 963    | No file              | `a17e5f1d2955`  |
| 955    | No file              | `a17e5f1d2955`  |
| 946    | No file              | `a17e5f1d2955`  |
| 938    | No file              | `a17e5f1d2955`  |
| 927    | No file              | `a17e5f1d2955`  |
| 911    | No file              | `a17e5f1d2955`  |
| 904    | No file              | `a17e5f1d2955`  |
| 899    | No file              | `a17e5f1d2955`  |
| 894    | No file              | `a17e5f1d2955`  |
| 885    | No file              | `a17e5f1d2955`  |
| 879    | No file              | `a17e5f1d2955`  |
| 872    | No file              | `a17e5f1d2955`  |
| 864    | No file              | `a17e5f1d2955`  |
| 855    | No file              | `a17e5f1d2955`  |
| 853    | No file              | `a17e5f1d2955`  |
| 845    | No file              | `a17e5f1d2955`  |
| 837    | No file              | `a17e5f1d2955`  |
| 829    | No documented layout | `a17e5f1d2955`  |
| 822    | No documented layout | `a17e5f1d2955`  |
| 814    | No documented layout | `a17e5f1d2955`  |
| 805    | No documented layout | `a17e5f1d2955`  |
| 794    | No documented layout | `a17e5f1d2955`  |
| 787    | No documented layout | `a17e5f1d2955`  |
| 780    | No documented layout | `a17e5f1d2955`  |
| 771    | No documented layout | `a17e5f1d2955`  |
| 760    | No documented layout | `a17e5f1d2955`  |
| 748    | No documented layout | `a17e5f1d2955`  |
| 741    | No documented layout | `a17e5f1d2955`  |
| 736    | No documented layout | `a17e5f1d2955`  |
| 731    | No documented layout | `a17e5f1d2955`  |
| 723    | No documented layout | `a17e5f1d2955`  |
| 711    | No documented layout | `a17e5f1d2955`  |
| 707    | No documented layout | `a17e5f1d2955`  |
| 697    | No documented layout | `a17e5f1d2955`  |
| 689    | No documented layout | `a17e5f1d2955`  |
| 683    | No documented layout | `a17e5f1d2955`  |
| 678    | No documented layout | `a17e5f1d2955`  |
| 670    | No documented layout | `a17e5f1d2955`  |
| 661    | No documented layout | `a17e5f1d2955`  |
| 656    | No documented layout | `a17e5f1d2955`  |
| 652    | No documented layout | `a17e5f1d2955`  |
| 643    | No documented layout | `a17e5f1d2955`  |
| 637    | No documented layout | `a17e5f1d2955`  |
| 630    | No documented layout | `a17e5f1d2955`  |
| 627    | No documented layout | `a17e5f1d2955`  |
| 621    | No documented layout | `a17e5f1d2955`  |
| 617    | No documented layout | `a17e5f1d2955`  |
| 615    | No documented layout | `a17e5f1d2955`  |
| 606    | No documented layout | `a17e5f1d2955`  |
| 599    | No documented layout | `a17e5f1d2955`  |
| 592    | No documented layout | `a17e5f1d2955`  |
| 586    | No documented layout | `a17e5f1d2955`  |
| 577    | No documented layout | `a17e5f1d2955`  |
| 569    | No documented layout | `a17e5f1d2955`  |
| 561    | No documented layout | `a17e5f1d2955`  |
| 554    | No documented layout | `a17e5f1d2955`  |
| 542    | No documented layout | `a17e5f1d2955`  |
| 532    | No documented layout | `a17e5f1d2955`  |
| 531    | No documented layout | `a17e5f1d2955`  |
| 526    | No documented layout | `a17e5f1d2955`  |
| 521    | No documented layout | `a17e5f1d2955`  |
| 517    | No documented layout | `a17e5f1d2955`  |
| 510    | No documented layout | `a17e5f1d2955`  |
| 508    | No documented layout | `a17e5f1d2955`  |
| 504    | No documented layout | `a17e5f1d2955`  |
| 497    | No documented layout | `a17e5f1d2955`  |
| 491    | No documented layout | `a17e5f1d2955`  |
| 485    | No documented layout | `a17e5f1d2955`  |
| 478    | No documented layout | `a17e5f1d2955`  |
| 472    | No documented layout | `a17e5f1d2955`  |
| 466    | No documented layout | `a17e5f1d2955`  |
| 457    | No documented layout | `a17e5f1d2955`  |
| 452    | No documented layout | `a17e5f1d2955`  |
| 449    | No documented layout | `a17e5f1d2955`  |
| 435    | No documented layout | `a17e5f1d2955`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                       |
| --------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Region names (type 17), territory names (type 12), node names (type 29), NPC names (type 6) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset              | Type                 | Field              | Notes                                                          |
| ------------------- | -------------------- | ------------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]              | magic              | `PABR` (ASCII)                                                 |
| `+0x04`             | u32                  | record_count       | Observed `1594` (client 3458; the extractor documents `1572`)  |
| `+0x08`             | Region[record_count] | records            | Variable records packed back-to-back with no alignment; see Region |
| `records+0x00`      | String Table         | string_table       | Korean strings (shared `pabr_strings` layout); see String Table |
| `string_table+0x00` | u32                  | string_table_start | Absolute file offset of `string_table.count`; observed `623714` |
| `string_table+0x04` | u32                  | zero               | Observed `0`                                                   |

A record is a 210-byte head, two counted lists and a 171-byte tail, so its size is `389 + 2 * key_count + 12 * vector_count`. The walk ends exactly at `string_table_start`; the parser raises an error when it does not.

### Region (variable: 389 bytes + key and vector lists)

| Offset                    | Type                     | Field              | Notes |
| ------------------------- | ------------------------ | ------------------ | ----- |
| `+0x00`                   | Region Head              | head               | See Region Head |
| `+0xD2`                   | u32                      | key_count          | |
| `+0xD6`                   | u16[key_count]           | pc_delivery_region_keys | Regions a character can be sent to by PC delivery; set on 58 town regions and always includes the region itself (Field Names). Velia's list holds the mainland towns from Velia to Muzgar; Hakinza Sanctuary's holds Altinova, Asparkan, Shakatu, Sand Grain Bazaar, Muzgar, Velandir, Aal's Revelation and Angavu Outpost |
| `pc_delivery_region_keys+0x00` | u32                      | vector_count       | |
| `pc_delivery_region_keys+0x04` | f32[vector_count][3]     | unknown_d2_vectors | World positions; only The Great Desert of Valencia (region 230) has any (3) |
| `unknown_d2_vectors+0x00` | Region Tail              | tail               | See Region Tail |

### Region Head (210 bytes)

Offsets are hex; the extractor's decimal offset is in the notes where it named the field.

| Offset  | Type      | Field              | Notes |
| ------- | --------- | ------------------ | ----- |
| `+0x00` | u16       | region_key         | LOC `str_type=17`, `str_id1=region_key`; unique; all 1594 resolve |
| `+0x02` | u8[3]     | color              | Region colour stored blue, green, red; the parser returns `rrggbb` (Velia `820000`). `edaniaregioninfo.bss` stores the same value for the five first-group Edania castles |
| `+0x05` | u8        | color_alpha        | Always `0`; the alpha byte of `color`, which the 2016 PDB types as a 4-byte `pa::Color` (`_colorKey`) |
| `+0x06` | u8        | region_type        | `CppEnums.RegionType`; see Enum Values |
| `+0x07` | u8        | node_war_day       | `CppEnums.VillageSiegeType`, Sunday `0` to Saturday `6`; `7` (the enum's `_Count`) for no node war |
| `+0x08` | bytes[3]  | unknown_08         | Always `0` |
| `+0x0B` | u8        | unknown_0b         | Values `0`, `1`, `3`, `4`; `3` on Velia, Heidel, Altinova and Valencia City, `4` on the Margoria islands |
| `+0x0C` | u8        | is_safe_zone       | Set on 318 regions, among them Velia, Glish, Ossuary, Heidel Castle and Lake Flondor |
| `+0x0D` | u8        | is_arena_zone      | Set on the 9 arena regions. Named from the 2016 member order (`_isArenaZone` between `_isSafeZone` and `_isSea`); the client Lua reads `isArenaZone` |
| `+0x0E` | u8        | is_sea             | Set on 199 regions, mostly islands and sea. The extractor calls it `ocean` |
| `+0x0F` | u8        | is_desert          | Set on 43 regions, all in Valencia (territory 4): the Great Desert, the sand dunes, Pilgrim's Sanctums, Cantusa, Aakman |
| `+0x10` | u8        | is_not_dig         | Set on 8 desert regions: Aakman Temple, Scarlet Sand Chamber, Ibellab Oasis, Hystria Ruins, Roud Sulfur Mine, Pila Ku Jail, Muiquun, Jail. The extractor calls it `prison`. Likely turns off Shabby Shovel digging, see Notes |
| `+0x11` | u8        | is_ocean           | Set on 62 regions: Sea, Margoria, Oquilla's Eye, Crow Merchants' Vessel. The extractor calls it `sea`; the client Lua has `isOceanZone` next to the sea checks |
| `+0x12` | u8        | is_prison          | Set on Jail (697) only |
| `+0x13` | u8        | unknown_13         | Several mirror `region_type` (`0x13` = Siege or CastleInSiege, `0x14` = Fortress, `0x18` = MainTown, `0x19` = MinorTown, `0x1A` = either town); see Open Questions |
| `+0x14` | u8        | unknown_14         | Mirrors `region_type` Fortress; see `unknown_13` |
| `+0x15` | u8        | unknown_15         | See `unknown_13` |
| `+0x16` | u8        | unknown_16         | See `unknown_13` |
| `+0x17` | u8        | unknown_17         | See `unknown_13` |
| `+0x18` | u8        | unknown_18         | Mirrors `region_type` MainTown; see `unknown_13` |
| `+0x19` | u8        | unknown_19         | Mirrors `region_type` MinorTown; see `unknown_13` |
| `+0x1A` | u8        | unknown_1a         | Set on either town type; see `unknown_13` |
| `+0x1B` | u8        | is_accessible_area | Set on 1514 regions. The extractor calls it `locator`; the client Lua reads `isAccessibleArea` |
| `+0x1C` | u8        | is_node_access     | Set on 118 regions |
| `+0x1D` | u16       | unknown_1d         | |
| `+0x1F` | u8        | unknown_1f         | Set on 54 regions (Rameda Island, Altar of Agris, Western Guard Camp) |
| `+0x20` | u32       | unknown_20         | `22950` in every record (the extractor saw `19950`), so it changes between patches |
| `+0x24` | u8        | unknown_24         | Always `0` |
| `+0x25` | u8        | is_locator         | |
| `+0x26` | u32       | villain_respawn_node_key | Exploration node key where an outlaw respawns. Set on 204 records, all exploration node keys (Muiquun for several desert regions) |
| `+0x2A` | f32[3]    | villain_respawn_position | The position paired with `villain_respawn_node_key`. Named from the 2016 member order (`_villainRespawnPosition` follows the key); no server column to check it against |
| `+0x36` | u8        | is_ancient_dungeon | Set on Aakman Temple (688) and Hystria Ruins (689) |
| `+0x37` | u8        | is_escape          | Set on most regions; clear on Atoraxion, the arenas and battlefields, Oquilla's Eye, Kamasylvia, Duvencrune, Muiquun and a few caves |
| `+0x38` | u8        | is_special_zone    | Set on Atoraxion, the arenas and battlefields, Sea Palace, Mountain of Eternal Winter, Pit of the Undying, Aakman Temple, Hystria Ruins, Ruins of Tzol |
| `+0x39` | u8        | is_vehicle_dead_zone | Set only on `is_special_zone` regions |
| `+0x3A` | u8        | unknown_3a         | |
| `+0x3B` | u8        | unknown_3b         | Always `0` |
| `+0x3C` | u16       | skill_no           | Region buff skill by day; see Notes |
| `+0x3E` | u32       | skill_apply_rate   | Apply rate of `skill_no` |
| `+0x42` | u8        | unknown_42         | |
| `+0x43` | u8        | unknown_43         | Always `0` |
| `+0x44` | u16       | skill_no_2         | A second region skill; set on the Margoria regions only |
| `+0x46` | u32       | skill_apply_rate_2 | Apply rate of `skill_no_2` |
| `+0x4A` | bytes[8]  | unknown_4a         | Always `0` |
| `+0x52` | u8        | unknown_52         | |
| `+0x53` | u8        | unknown_53         | Always `0` |
| `+0x54` | u16       | night_skill_no     | Region buff skill at night; see Notes |
| `+0x56` | u32       | night_skill_apply_rate | Apply rate of `night_skill_no` |
| `+0x5A` | u8        | territory_key      | Territory 0 to 13; LOC `str_type=12`, `str_id4=1` names it (Balenos, Serendia ... Inner Edania). The key of `territoryinfo.bss` |
| `+0x5B` | u8        | unknown_5b         | Always `0` |
| `+0x5C` | u32       | name_index         | Index into `string_table`; the region's Korean name (`벨리아 마을` for Velia) |
| `+0x60` | u32       | return_position_name | Index into `string_table`; the Korean name of the region's return point, see Notes. The extractor calls it the capital's name, which it is not |
| `+0x64` | u16       | capital_region_key | Region key of the territory capital: the same in every region of a territory and always that territory's `MainTown` (Velia, Heidel, Calpheon City ... Angavu Outpost) |
| `+0x66` | u16       | trade_origin_region_key | A region key: the trade origin (`getTradeOriginRegion` in the client Lua). The extractor calls it the affiliated town. Often the region itself or a nearby town, but also non-town regions (Evergart Falls points to 417) |
| `+0x68` | u16       | region_group_key   | Key of `regiongroupinfo.bss`: the file has 250 records and this field 250 distinct values (`0` on 32 regions) |
| `+0x6A` | u8        | unknown_6a         | Always `0` |
| `+0x6B` | u16       | waypoint_key       | Non-zero on 628 records; equals `node_key` on 873 (zero included) |
| `+0x6D` | bytes[2]  | unknown_6d         | Always `0` |
| `+0x6F` | u16       | node_key           | `exploration.bss` node key; non-zero on 1331 records and every one is a node. The node that covers the region (Lumbering 1 -> Trent) |
| `+0x71` | bytes[2]  | unknown_71         | Always `0` |
| `+0x73` | u8        | region_attribute_type | `1` on Velia (5) and Velia Beach (444), `0` elsewhere (client 3464) |
| `+0x74` | bytes[3]  | unknown_74         | Always `0` |
| `+0x77` | f32[3]    | unknown_77         | Extractor: waypoint position. Zero on 1580 records |
| `+0x83` | f32[3]    | return_position    | The return point's world position, shared by many regions; pairs with `return_position_name`, see Notes. The extractor calls it the region position, which it is not |
| `+0x8F` | bytes[4]  | unknown_8f         | Always `0` |
| `+0x93` | u8        | exploration_point  | `1` except on Velia (1), Sea (2), Deep Sea (175) and Valencia City (229) (client 3464) |
| `+0x94` | u8        | unknown_94         | Always `0` |
| `+0x95` | u32       | unknown_95         | |
| `+0x99` | f32[5]    | unknown_99         | Velia: `45, 38, 0, 55, 0.6` |
| `+0xAD` | u32       | unknown_ad         | |
| `+0xB1` | u32       | unknown_b1         | |
| `+0xB5` | u32       | unknown_b5         | `0xFFFFFFFF` in every record |
| `+0xB9` | u32[6]    | unknown_b9         | Set mainly on towns; Velia `105580, 105554, 105551, 105607, 105547, 105580` |
| `+0xD1` | u8        | is_free_revival_area | The client Lua reads `isFreeRevivalArea` |

### Region Tail (171 bytes)

Offsets are relative to the start of the tail. The parser keeps every field that is not zero in all records; the unconfirmed ones are `unknown_tail_<offset>`, kept on the record for search and CSV export but not shown in the table.

I walked the extractor's tail list (`unknownTail1` to `unknownTail162`, 46 values once its arrays are counted out) against client 3458. Its reserved spans at tail `+0x00`, `+0x50`, `+0x8A` (7 bytes), `+0x92` (8 bytes) and `+0xA6` (3 bytes) are zero in every record, and five of its fields are too (`+0x16`, `+0x31`, `+0x41`, `+0x87`, `+0x9E`), so they are listed as reserved here. One split is wrong: the extractor reads `+0x4D` as a u16, a u8 (`unknownTail79`, which looks like a tier 1 to 4 or 15) and a reserved byte, but the four bytes are one u32 (`70000`, `140000`, `220000`, `280000`, `1000000`); the "tier" byte is just its third byte.

`FLT_MAX` and `0x7FFFFFFF` mean "no value" in several fields below. They are set on every region except a group of 67: the 63 node war regions (`node_war_day` 0 to 6) and the territory capitals Velia, Heidel, Altinova and Valencia City. I call this group the siege regions below.

| Offset  | Type      | Field                   | Notes |
| ------- | --------- | ----------------------- | ----- |
| `+0x00` | u8        | unknown_tail_00         | Always `0` |
| `+0x01` | u16       | unknown_tail_01         | `0xFFFF` in every record |
| `+0x03` | u16       | max_participants        | Node war participant cap: `0` except on the siege regions, `30` to `80` on node war regions, `100` on the four capitals. Matches the published per-node participant table on all 24 Calpheon, Ulukita, Valencia and Edania nodes; the game can override it (City of the Dead: `35` here and in that table, `40` in its tooltip) |
| `+0x05` | f32       | siege_ap_limit          | Node war AP limit; `FLT_MAX` (no limit) except on the siege regions. See Notes for the five sets |
| `+0x09` | f32       | siege_dr_limit          | Node war damage reduction (DP) limit |
| `+0x0D` | f32       | siege_evasion_limit     | Node war evasion limit |
| `+0x11` | u32       | unknown_tail_11         | `0x7FFFFFFF` except on the siege regions: `150000`, `200000` or `1000000`, `0` on Velia and Heidel. The accuracy rate or the evasion rate limit; always equal to `unknown_tail_55`, so which is which is open |
| `+0x15` | u8        | unknown_tail_15         | `3` on the 63 node war regions, `5` elsewhere. Possibly the max war heroes, which the node tooltip shows as 3 |
| `+0x16` | u8        | unknown_tail_16         | Always `0` |
| `+0x17` | u8        | unknown_tail_17         | `3` in every record |
| `+0x18` | u8        | is_world_boss_reward    | Set on Margoria (Vell's Realm) (871) only |
| `+0x19` | f32[6]    | unknown_tail_19         | Two world positions, set on 117 regions; on 84 both are the same point, on 31 the second is zero (Pit of the Undying among them), on 2 they differ |
| `+0x31` | u64       | unknown_tail_31         | Always `0` |
| `+0x39` | f32       | unknown_tail_39         | `FLT_MAX`, or on the siege regions the same value as `siege_ap_limit` |
| `+0x3D` | f32       | unknown_tail_3d         | `FLT_MAX`, or `100000000` on the siege regions |
| `+0x41` | u32       | unknown_tail_41         | Always `0` |
| `+0x45` | u8        | unknown_tail_45         | Set on exactly the region type 7 records (Pit of the Undying 950 and 1070) |
| `+0x46` | u8        | unknown_tail_46         | Set on exactly the region type 8 record (Battle Arena 1072) |
| `+0x47` | u32       | unknown_tail_47         | `10011` on the 63 node war regions, `0` elsewhere |
| `+0x4B` | u16       | unknown_tail_4b         | `0xFFFF` except on the 40 Atoraxion regions: `151` on Vaha's areas, `153` on Syca's, `155` on Yolu's, `157` on Orze's; two dungeon regions break the pattern (Sycrakea `151`, Orzekea `153`) |
| `+0x4D` | u32       | siege_dr_rate_limit     | Node war damage reduction rate limit, `1000000` = 100%. `658` on every other region |
| `+0x51` | f32       | siege_accuracy_limit    | Node war accuracy limit |
| `+0x55` | u32       | unknown_tail_55         | The other one of the accuracy rate and evasion rate limits, see `unknown_tail_11` |
| `+0x59` | u32[4]    | siege_resistance_limits | Node war resistance limits, `1000000` = 100%; the four values are equal in every record (likely stun, grapple, knockdown and knockback, order unconfirmed) |
| `+0x69` | u32       | unknown_tail_69         | `0x7FFFFFFF`, or `0` on the siege regions |
| `+0x6D` | u8        | unknown_tail_6d         | Set on 7 separated PvP areas: both Battle Arenas of type 6 (436, 437), Battle Arena 1072, Arena of Arsha, Battlefield of Honor, The Red Battlefield, Undiscovered Area (435) |
| `+0x6E` | f32[3]    | unknown_tail_6e         | A world position on 49 instance regions: all Atoraxion regions point to Velia's `(-1226, -7012, 81647)`, the Oquilla's Eye regions and the Land of the Morning Light houses to their own town |
| `+0x7A` | f32[3]    | unknown_tail_7a         | A distinct world position on 36 node war regions, Altinova and Valencia City |
| `+0x86` | u8        | unknown_tail_86         | On the siege regions only: `100` on the capitals; on node war regions `0`, `5` or `15` |
| `+0x87` | u8        | unknown_tail_87         | Always `0` |
| `+0x88` | u8        | unknown_tail_88         | Set on the 63 node war regions |
| `+0x89` | u8        | unknown_tail_89         | `10` on the 63 node war regions |
| `+0x8A` | bytes[7]  | unknown_tail_8a         | Always `0` |
| `+0x91` | u8        | unknown_tail_91         | `49` on the 63 node war regions |
| `+0x92` | bytes[8]  | unknown_tail_92         | Always `0` |
| `+0x9A` | u32       | unknown_tail_9a         | On the siege regions only; node war regions `15625000` to `39062500`, the capitals `117187500` to `234375000`. Multiples of `1953125` (`10^9 / 512`) |
| `+0x9E` | u32       | unknown_tail_9e         | Always `0` |
| `+0xA2` | u32       | unknown_tail_a2         | On the siege regions only; always `unknown_tail_9a + 7812500` on node war regions, `+39062500` on the capitals |
| `+0xA6` | bytes[3]  | unknown_tail_a6         | Always `0` |
| `+0xA9` | u16       | guild_wharf_manager_key | NPC character key; set on 20 regions and every NPC is titled `<Guild Wharf Manager>` in LOC (Robert in Velia, Sebastian in Port Epheria, Elro in Oquilla's Eye) |


### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | Observed `1108` entries |
| `+0x04` | pstr[string_count] | strings      | Korean strings |

## Layout 1

On client 1784 the head has no `unknown_16`, so the fields from
`unknown_17` sit 1 byte earlier, and 152 bytes (`unknown_b8`) sit between
`unknown_b5` and `unknown_b9`. In the tail, `unknown_tail_31` (always `0`
in Layout 2) counts a list of u16 region keys that follows it, and the
fields after the list have a u8 and an f32 more before `unknown_tail_45`
and end after `unknown_tail_7a`, without the 37 bytes from
`unknown_tail_86` to `guild_wharf_manager_key`.

### Region (variable: 369 bytes + key and vector lists)

| Offset                    | Type                 | Field              | Notes           |
| ------------------------- | -------------------- | ------------------ | --------------- |
| `+0x00`                   | Region Head          | head               | See Region Head |
| `+0x169`                  | u32                  | key_count          |                 |
| `+0x16D`                  | u16[key_count]       | pc_delivery_region_keys |            |
| `pc_delivery_region_keys+0x00` | u32                  | vector_count       |                 |
| `pc_delivery_region_keys+0x04` | f32[vector_count][3] | unknown_d2_vectors |                 |
| `unknown_d2_vectors+0x00` | Region Tail          | tail               | See Region Tail |

### Region Head (361 bytes)

| Offset   | Type      | Field                    | Notes |
| -------- | --------- | ------------------------ | ----- |
| `+0x00`  | u16       | region_key               |  |
| `+0x02`  | u8[3]     | color                    |  |
| `+0x05`  | u8        | color_alpha              |  |
| `+0x06`  | u8        | region_type              |  |
| `+0x07`  | u8        | node_war_day             |  |
| `+0x08`  | bytes[3]  | unknown_08               |  |
| `+0x0B`  | u8        | unknown_0b               |  |
| `+0x0C`  | u8        | is_safe_zone             |  |
| `+0x0D`  | u8        | is_arena_zone            |  |
| `+0x0E`  | u8        | is_sea                   |  |
| `+0x0F`  | u8        | is_desert                |  |
| `+0x10`  | u8        | is_not_dig               |  |
| `+0x11`  | u8        | is_ocean                 |  |
| `+0x12`  | u8        | is_prison                |  |
| `+0x13`  | u8        | unknown_13               |  |
| `+0x14`  | u8        | unknown_14               |  |
| `+0x15`  | u8        | unknown_15               |  |
| `+0x16`  | u8        | unknown_17               |  |
| `+0x17`  | u8        | unknown_18               |  |
| `+0x18`  | u8        | unknown_19               |  |
| `+0x19`  | u8        | unknown_1a               |  |
| `+0x1A`  | u8        | is_accessible_area       |  |
| `+0x1B`  | u8        | is_node_access           |  |
| `+0x1C`  | u16       | unknown_1d               |  |
| `+0x1E`  | u8        | unknown_1f               |  |
| `+0x1F`  | u32       | unknown_20               | `22130` in every record on client 1784 |
| `+0x23`  | u8        | unknown_24               |  |
| `+0x24`  | u8        | is_locator               |  |
| `+0x25`  | u32       | villain_respawn_node_key |  |
| `+0x29`  | f32[3]    | villain_respawn_position |  |
| `+0x35`  | u8        | is_ancient_dungeon       |  |
| `+0x36`  | u8        | is_escape                |  |
| `+0x37`  | u8        | is_special_zone          |  |
| `+0x38`  | u8        | is_vehicle_dead_zone     |  |
| `+0x39`  | u8        | unknown_3a               |  |
| `+0x3A`  | u8        | unknown_3b               |  |
| `+0x3B`  | u16       | skill_no                 |  |
| `+0x3D`  | u32       | skill_apply_rate         |  |
| `+0x41`  | u8        | unknown_42               |  |
| `+0x42`  | u8        | unknown_43               |  |
| `+0x43`  | u16       | skill_no_2               |  |
| `+0x45`  | u32       | skill_apply_rate_2       |  |
| `+0x49`  | bytes[8]  | unknown_4a               |  |
| `+0x51`  | u8        | unknown_52               |  |
| `+0x52`  | u8        | unknown_53               |  |
| `+0x53`  | u16       | night_skill_no           |  |
| `+0x55`  | u32       | night_skill_apply_rate   |  |
| `+0x59`  | u8        | territory_key            |  |
| `+0x5A`  | u8        | unknown_5b               |  |
| `+0x5B`  | u32       | name_index               |  |
| `+0x5F`  | u32       | return_position_name     |  |
| `+0x63`  | u16       | capital_region_key       |  |
| `+0x65`  | u16       | trade_origin_region_key  |  |
| `+0x67`  | u16       | region_group_key         |  |
| `+0x69`  | u8        | unknown_6a               |  |
| `+0x6A`  | u16       | waypoint_key             |  |
| `+0x6C`  | bytes[2]  | unknown_6d               |  |
| `+0x6E`  | u16       | node_key                 |  |
| `+0x70`  | bytes[2]  | unknown_71               |  |
| `+0x72`  | u8        | region_attribute_type    |  |
| `+0x73`  | bytes[3]  | unknown_74               |  |
| `+0x76`  | f32[3]    | unknown_77               |  |
| `+0x82`  | f32[3]    | return_position          |  |
| `+0x8E`  | bytes[4]  | unknown_8f               |  |
| `+0x92`  | u8        | exploration_point        |  |
| `+0x93`  | u8        | unknown_94               |  |
| `+0x94`  | u32       | unknown_95               |  |
| `+0x98`  | f32[5]    | unknown_99               |  |
| `+0xAC`  | u32       | unknown_ad               |  |
| `+0xB0`  | u32       | unknown_b1               |  |
| `+0xB4`  | u32       | unknown_b5               |  |
| `+0xB8`  | u32[38]   | unknown_b8               | Not in Layout 2; see below |
| `+0x150` | u32[6]    | unknown_b9               |  |
| `+0x168` | u8        | is_free_revival_area     |  |

`unknown_b8` is 38 u32: one from `0` to `43`, 18 values of the form
`1001`, `2001` ... `8001` (or `0`), 18 values from `0` to `265`, and `1` in
every record on client 1784.

### Region Tail (variable: 139 bytes + region keys)

| Offset                   | Type                 | Field                   | Notes |
| ------------------------ | -------------------- | ----------------------- | ----- |
| `+0x00`                  | u8                   | unknown_tail_00         |  |
| `+0x01`                  | u16                  | unknown_tail_01         |  |
| `+0x03`                  | u16                  | max_participants        |  |
| `+0x05`                  | f32                  | siege_ap_limit          |  |
| `+0x09`                  | f32                  | siege_dr_limit          |  |
| `+0x0D`                  | f32                  | siege_evasion_limit     |  |
| `+0x11`                  | u32                  | unknown_tail_11         |  |
| `+0x15`                  | u8                   | unknown_tail_15         |  |
| `+0x16`                  | u8                   | unknown_tail_16         |  |
| `+0x17`                  | u8                   | unknown_tail_17         |  |
| `+0x18`                  | u8                   | is_world_boss_reward    |  |
| `+0x19`                  | f32[6]               | unknown_tail_19         |  |
| `+0x31`                  | u64                  | unknown_tail_31         | Count of `unknown_tail_list`; `0` to `7` on client 1784 |
| `+0x39`                  | u16[unknown_tail_31] | unknown_tail_list       | Region keys, mostly neighbours: region 214 holds `211, 212, 213`; set on 77 regions |
| `unknown_tail_list+0x00` | f32                  | unknown_tail_39         |  |
| `unknown_tail_list+0x04` | f32                  | unknown_tail_3d         |  |
| `unknown_tail_list+0x08` | u32                  | unknown_tail_41         |  |
| `unknown_tail_list+0x0C` | u8                   | unknown_tail_list_0c    | Set on regions 78, 203 and 230 |
| `unknown_tail_list+0x0D` | f32                  | unknown_tail_list_0d    | `1000.0` on 82 regions, all with `node_war_day` `7`, else `0` |
| `unknown_tail_list+0x11` | u8                   | unknown_tail_45         | Set on regions 950 and 1070 |
| `unknown_tail_list+0x12` | u8                   | unknown_tail_46         | Set on region 1072 |
| `unknown_tail_list+0x13` | u32                  | unknown_tail_47         | `0`, `100`, `1001`, `10011` or `100111` |
| `unknown_tail_list+0x17` | u16                  | unknown_tail_4b         |  |
| `unknown_tail_list+0x19` | u32                  | siege_dr_rate_limit     |  |
| `unknown_tail_list+0x1D` | f32                  | siege_accuracy_limit    |  |
| `unknown_tail_list+0x21` | u32                  | unknown_tail_55         |  |
| `unknown_tail_list+0x25` | u32[4]               | siege_resistance_limits |  |
| `unknown_tail_list+0x35` | u32                  | unknown_tail_69         |  |
| `unknown_tail_list+0x39` | u8                   | unknown_tail_6d         |  |
| `unknown_tail_list+0x3A` | f32[3]               | unknown_tail_6e         |  |
| `unknown_tail_list+0x46` | f32[3]               | unknown_tail_7a         |  |

On client 1784 the file holds 1,062 records. Of the 1,056 region keys it
shares with client 3473, at least 932 hold the same value in each field
named here, apart from the string indices, `unknown_20`, `unknown_95` and
`siege_dr_rate_limit`.

## Field Names

Two sources name most of the head fields:

- The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::RegionInfo` lists the members `_regionKey`, `_colorKey`, `_regionType`, `_isSafeZone`, `_isArenaZone`, `_isSea`, `_isDesert`, `_isPrison`, seven town and war flags, `_accessibleArea`, `_villageTaxLevel`, `_dropGroupRerollCountOfSieger`, `_isLocator`, `_villainRespawnExploreKey`, `_villainRespawnPosition`, `_isAncientDungeon`, `_isEscape`, the day and night region skills, `_territoryKey`, `_areaName`, `_returnRegionName`, `_tradeOriginRegionKey`, `_regionGroupKey`, `_waypointKey`, `_exploreKey`, `_regionAttributeType`, `_returnPosition`, `_explorationPoint` ... `_isFreeRevivalArea` in this order. Today's record stores them in the same order without padding or pointers, with newer fields in between. Its loader, `GameCommonParameterLoaderFromExcel::LoadRegionInformation`, reads them from the columns of `Region_Table`.
- A private server on client 519 ships the developers' `Region_Table` with its original column names and values. I matched every column against every head and tail offset over the 896 region keys it shares with the client file.

Matches on client 3464 (896 shared region keys). The mismatches are regions changed since 2021:

| Offset      | Field                     | `Region_Table` column      | Matching regions |
| ----------- | ------------------------- | -------------------------- | ---------------- |
| `+0x02`     | color                     | `B`, `G`, `R`              | 895              |
| `+0x0C`     | is_safe_zone              | `IsSafe`                   | 889              |
| `+0x0E`     | is_sea                    | `IsSea`                    | 893              |
| `+0x0F`     | is_desert                 | `IsDesert`                 | 896              |
| `+0x10`     | is_not_dig                | `IsNotDig`                 | 896              |
| `+0x11`     | is_ocean                  | `IsOcean`                  | 895              |
| `+0x12`     | is_prison                 | `IsPrison`                 | 896              |
| `+0x1B`     | is_accessible_area        | `AccessibleArea`           | 867              |
| `+0x1C`     | is_node_access            | `isNodeAccess`             | 891              |
| `+0x25`     | is_locator                | `Locator`                  | 894              |
| `+0x26`     | villain_respawn_node_key  | `VillainRespawnExploreKey` | 822              |
| `+0x36`     | is_ancient_dungeon        | `IsAncientDungeon`         | 896              |
| `+0x37`     | is_escape                 | `Isescape`                 | 895              |
| `+0x38`     | is_special_zone           | `IsSpecialZone`            | 896              |
| `+0x39`     | is_vehicle_dead_zone      | `VehicleDeadZone`          | 896              |
| `+0x3C`     | skill_no                  | `SkillNo`                  | 896              |
| `+0x3E`     | skill_apply_rate          | `SkillApplyRate`           | 896              |
| `+0x44`     | skill_no_2                | `SkillNo2`                 | 896              |
| `+0x46`     | skill_apply_rate_2        | `SkillApplyRate2`          | 896              |
| `+0x54`     | night_skill_no            | `NightSkillNo`             | 896              |
| `+0x56`     | night_skill_apply_rate    | `NightSkillApplyRate`      | 896              |
| `+0x5A`     | territory_key             | `TerritoryKey`             | 886              |
| `+0x5C`     | name_index                | `AreaName`                 | 838              |
| `+0x60`     | return_position_name      | `ReturnPositionName`       | 752              |
| `+0x66`     | trade_origin_region_key   | `TradeOriginRegion`        | 868              |
| `+0x68`     | region_group_key          | `RegionGroupKey`           | 890              |
| `+0x6B`     | waypoint_key              | `WaypointKey`              | 890              |
| `+0x6F`     | node_key                  | `ExploreKey`               | 889              |
| `+0x73`     | region_attribute_type     | `RegionAttributeType`      | 896              |
| `+0x83`     | return_position           | `ReturnPositionX`, `Y`     | 838              |
| `+0x93`     | exploration_point         | `ExplorationPoint`         | 896              |
| `+0xD1`     | is_free_revival_area      | `FreeRevivalArea`          | 884              |
| tail `+0x18`| is_world_boss_reward      | `WorldBossReward`          | 896              |

`villain_respawn_node_key` matches less often because the node keys were renumbered: the server's `1001` is `1727` here. The server's `ReturnPositionZ` column holds place-name text, so only X and Y were compared. Columns with no match in this file: the music columns (`BankNo_*`, `MusicIdx_*`), `Temperature`, `Humility`, `WindDir`, `OilRate`, `WaterRate` (constant on the server), `VillageTaxLevel`, `IsChallengeSiege`, `LimitMemberAtSiege`, `MonsterGroupForTotem` and the node war day (`VillageSiegeType`, changed since 2021; `node_war_day` stays on the client Lua enum).

`is_arena_zone` (`+0x0D`) and `villain_respawn_position` (`+0x2A`) have no column; they are named from their place in the 2016 member order between two matched fields.


`pc_delivery_region_keys` is the 2016 `gc::RegionInfo`
`_pcDeliveryRegionKeyList`; the client 1784 server builds it from waypoint
paths and checks a PC delivery request against it, see
[`regioninfo_linkandcheckvalid2.bss`](regioninfo_linkandcheckvalid2_bss.md)
Field Names. The extractor's "warehouse group" reading does not fit that
use.

## Enum Values

### `region_type` (`CppEnums.RegionType`)

Names from `global_define_cpp_enum.luac`, without the `eRegionType_` prefix. The enum ends with `_Count` = 7, but the file also uses 7 and 8; no client Lua names them, so the table shows the number (see Open Questions).

| ID  | Name          | Records | Examples |
| --- | ------------- | ------- | -------- |
| 0   | MinorTown     | 45      | Glish, Olvia, Keplan, Port Epheria, Western Guard Camp |
| 1   | MainTown      | 14      | The territory capitals: Velia, Heidel, Calpheon City ... Angavu Outpost |
| 2   | Hunting       | 1489    | Every field region |
| 3   | Siege         | 14      | Calpheon Castle Site, Lake Kaia, Mediah Shore, Treant Forest |
| 4   | Fortress      | 8       | Balenos Forest, Southern Neutral Zone, Naga Marsh |
| 5   | CastleInSiege | 13      | Calpheon Castle, Mediah Castle, Kamasylvia Castle, Duvencrune |
| 6   | Arena         | 8       | Velia Duel Arena, Battle Arena, Valencia Arena |
| 7   | (not in enum) | 2       | Pit of the Undying (950, 1070); `unknown_tail_45` is set on exactly these |
| 8   | (not in enum) | 1       | Battle Arena (1072); `unknown_tail_46` is set on exactly this one |

### `node_war_day` (`CppEnums.VillageSiegeType`)

`0` Sunday, `1` Monday, `2` Tuesday, `3` Wednesday, `4` Thursday, `5` Friday, `6` Saturday, `7` none. Client 3458 has 6 regions on each day from Sunday to Thursday, 33 on Friday (most of them Margoria islands) and none on Saturday, the conquest war day.

## Notes

- **LOC type 17 is the region name.** All 1594 region keys resolve in LOC type 17, which has 1658 IDs; the other 64 (750, 807 to 809, 821, 1177, 1178, 1417 ...) have no region in this client and look like retired regions. The `plantworkerselect.bss` selection IDs are region keys too: all 31 are towns of type `MainTown` or `MinorTown`. So both readings hold: type 17 names regions, and the worker-selection towns are regions; the `buff.dbss` town keys name towns through the same type. [`languagedata_loc.md`](languagedata_loc.md) says so.
- **`region_info.xml`** (`gamecommondata/`) keys its boxes by the same region key: `<box region_index=...>` matches `region_key`, and every one of its 183 region keys exists here. It is not a box per region: it holds 721 boxes (AABB plus an oriented box, `fieldNo="1"` on all) for 183 regions, nearly all caves, interiors and other small enclosed regions (Ossuary, Coastal Cave, Imp Cave, Secret Cave, Basement Cellar). Each box has a `property_index` into a 187-entry `propertyArray` of `WeatherTable`/`WeatherTime` values, and a `binArray` of 10626 grid cells indexes the boxes spatially. The `return_position` falls inside the region's own boxes for only 18 of the 183, so it is not the region position.
- **The return point.** `return_position_name` and `return_position` are `Region_Table`'s `ReturnPositionName` and `ReturnPositionX/Y/Z` (`_returnRegionName` and `_returnPosition` in the 2016 client). Grouping the records by the position gives 230 groups, and 214 of them share a single name: 90 regions point to `벨리아 마을` (Velia) at `(-1226, -7012, 81647)`, 107 to `하킨자 성전` (Hakinza Sanctuary), 81 to `알티노바` (Altinova). The name is often the territory capital or the `trade_origin_region_key` region, but matches neither consistently (463 and 470 of 1594, client 3458).
- The node war regions are field regions plus a few castles and towns: each day from Sunday to Thursday lists one region from each of six territories, for example Sunday holds Forest of Plunder, Orc Camp, Quint Hill, Valencia Castle, Neruda Plain and Neftak Outpost.
- Several flag bytes repeat `region_type` (see `unknown_13` .. `unknown_1a`), so they may be the client's per-type properties expanded into the record. The tail does the same for the two types past the enum: `unknown_tail_45` marks type 7 and `unknown_tail_46` type 8.
- **Region buff skills.** `skill_no` applies by day and `night_skill_no` at night, each with its apply rate. On client 3464 the set records are: the Valencia desert regions with `40338` Debuff Desert Morning (rate `50000`) by day and `40339` Debuff Desert Evening (`45000`) at night; Mountain of Eternal Winter with `41517` (no LOC skill name) by day and `40339` at night; the Margoria regions and the Crow Merchants' Vessel with `40434` Summon Phantom Ship by day and night, plus `40452` Summon Margoria Grim Reaper in `skill_no_2`. The scale of the apply rates is not known.
- **`is_not_dig` and the Shabby Shovel.** The Shabby Shovel (item `16139`, sold by the Valencia material vendors) says "You can dig the sand with this in the desert" and yields a Bag of Muddy Water (`6657`). Every `is_not_dig` region also has `is_desert` set, and all eight are enclosed or special spots inside the desert (temples, ruins, a mine, two jails, the Ibellab Oasis, Muiquun). So the flag likely turns off shovel digging where `is_desert` would allow it. Neither the client Lua nor the server code reads it, so this rests on the region list; see In-Game Checks.
- **The siege block in the tail.** `max_participants`, the `siege_*` limits and `unknown_tail_11`, `_39`, `_3d`, `_55`, `_86`, `_9a` and `_a2` are filled only on the 63 node war regions and the four capitals Velia, Heidel, Altinova and Valencia City; every other region carries `FLT_MAX`, `0x7FFFFFFF` or `0` there, and `+0x4D` holds `658`; the parser leaves every `siege_*` limit `None` where `max_participants` is 0. The client reads the same limits per region through `ToClient_getLimitSiegeDDByRegionKey`, `...HitByRegionKey`, `...DVByRegionKey`, `...PVByRegionKey`, `...DVRateByRegionKey`, `...HitRateByRegionKey` and `...StunResistByRegionKey` (`panel_worldmap_nodetooltip_villagewar_all_1.luac`, `new_worldmap_territorytooltip.luac`), and the participant cap through `getMaxMemberAtSiege`.
- **How the limit fields were mapped.** The node war regions use five fixed limit sets:

  | AP   | DR   | Evasion | Accuracy | DR rate | Acc. / eva. rate | Resistance |
  | ---- | ---- | ------- | -------- | ------- | ---------------- | ---------- |
  | 245  | 223  | 741     | 645      | 7%      | 15% / 15%        | 20%        |
  | 362  | 327  | 847     | 715      | 14%     | 15% / 15%        | 30%        |
  | 485  | 365  | 913     | 781      | 22%     | 20% / 20%        | 50%        |
  | 540  | 407  | 966     | 824      | 28%     | 100% / 100%      | 100%       |
  | 9999 | 9999 | 9999    | 9999     | 100%    | 100% / 100%      | 100%       |

  Black Desert Foundry's node war guide lists the old Tier 1 Beginner limits as AP 245, damage reduction 223, accuracy 645, evasion 741, damage reduction rate 7%, accuracy and evasion rate 15% and resistance 20%: the first set, field for field. Its Tier 1 Intermediate rates (14%, 15%, 15%, 30%) match the second set, whose flat values have been raised since. The `9999` set is the uncapped one. Velia (`560 / 410 / 768 / 680`) and Heidel (`680 / 530 / 908 / 820`) have their own. The sets no longer follow today's node tiers (Hexe Sanctuary and Longleaf Tree Sentry Post are both Tier 4 but use the 485 and 362 sets), and neither the tier nor the 550 / 720 gear score limit of the construction mode node wars is stored in this file.
- **The capital records hold the live limits.** In game, Trina Fort (Calpheon) and City of the Dead (Ulukita) both show AP limit 680, damage reduction 530, evasion 908, accuracy 820 and damage reduction rate 30%: exactly Heidel's record, not their own `9999` and `540` sets. So the four capital records look like the limit sets per territory pair of the construction mode node wars: Heidel for Calpheon and Ulukita (gear score limit 720, confirmed by both nodes), Altinova and Valencia City (`9999`, uncapped) for Valencia and Edania (no gear score limit, consistent but not checked in game), Velia (`560` set) unconfirmed. The per-node sets in the table above look like leftovers from the older tier system. Both tooltips also show an HP limit of 11,000, which this file has no field for.
- **Occupation mode overrides these values.** Balenos and Serendia run their node wars in occupation mode, and there the in-game node tooltip ignores this file: Castle Ruins, Glish Swamp, Orc Camp and Wolf Hills all show AP limit 395, evasion 738, damage reduction 335, damage reduction rate 20%, accuracy 650, 25 max participants and 3 max war heroes, while this file gives them four different limit sets and 55, 45, 65 and 80 participants. [`siegeterritoryoptionstaticstatus.bss`](siegeterritoryoptionstaticstatus_bss.md) holds them: its Balenos and Serendia row has HP 6,500, AP 395, damage reduction 335, accuracy 650, evasion 738 and damage reduction rate 20%, and its Calpheon and Ulukita row has HP 11,000 and Heidel's set. The tooltip also lists limits this file has no field for (critical hit rate and damage, back / down / air attack damage at 20%, HP 6,500, HP recovery 5, Black Spirit's Rage 100% and its recovery 0.15%, stamina 2,100).
- `unknown_tail_86` (`0`, `5`, `15`) follows the territory pairs of the construction mode node wars on the land nodes: `0` on Balenos and Serendia (gear score limit 550), `5` on Calpheon and Ulukita (720), `15` on Valencia and Edania (no limit). The island nodes carry `0` in every territory.
- `unknown_tail_9a` and `unknown_tail_a2` hold silver-sized amounts on the siege regions (node war regions `15.6M` to `46.9M`, capitals up to `273.4M`), always a fixed step apart; they may be the node war participation fee or reward, but nothing in the client names them.
- Related files out of scope here: `regionclientdata.xml` and its per-service variants (`regionclientdata_<code>_.xml`) place NPCs and monsters per region and key them by `<RegionInfo Key=...>`, the same region key.
- [`regioninfo_linkandcheckvalid2.bss`](regioninfo_linkandcheckvalid2_bss.md) stores `pc_delivery_region_keys` again, one record per region; its lists equal this file's in every record of client 3458, and the links are mutual (when A lists B, B lists A).

## Open Questions

### Where the live node war values come from

Several values the node tooltip shows are not in this file, or differ from it:

- **Participant cap.** City of the Dead shows 40 max participants in game, while `max_participants` and the published construction mode table both say 35. Something overrides the cap per node.
- **Limits with no field here.** Critical hit rate and damage, back / down / air attack damage, Black Spirit's Rage and its recovery. HP, HP recovery and stamina are in [`siegeterritoryoptionstaticstatus.bss`](siegeterritoryoptionstaticstatus_bss.md), per territory group.

The remaining tooltip limits may be among the unnamed tail values of [`siegeterritoryoptionstaticstatus.bss`](siegeterritoryoptionstaticstatus_bss.md).

### Max war heroes

Every node tooltip shows 3 max war heroes. `unknown_tail_15` is `3` on every node war region and `5` elsewhere, which makes it the only candidate, but a node with a different hero count is needed to confirm it.

### Accuracy rate or evasion rate

`unknown_tail_11` and `unknown_tail_55` are the accuracy rate and evasion rate limits, but they hold the same value in every set, so which offset is which cannot be told from the data. A patch that gives the two different values, checked against a node tooltip, would settle it.

### Other tail fields

`unknown_tail_47` (`10011`), `unknown_tail_89` (`10`) and `unknown_tail_91` (`49`) are constant across the node war regions; `unknown_tail_86` (`0`, `5`, `15`) follows the territory pairs (see Notes) and `unknown_tail_9a` / `unknown_tail_a2` (silver-sized amounts) vary by node. `unknown_tail_39` repeats `siege_ap_limit` and `unknown_tail_3d` is `100000000` on every siege region; both may be limits the current node wars do not use. `unknown_tail_4b` groups the Atoraxion regions, `unknown_tail_6d` the separated PvP areas, `unknown_tail_6e` points instance regions to a town (all of Atoraxion to Velia), and `unknown_tail_19` / `unknown_tail_7a` are world positions. None of these has a name in the client yet.

### Town and War Flags

`unknown_13` .. `unknown_1a` have no `Region_Table` column. The 2016 `gc::RegionInfo` has seven computed flags at this place: `_isKingWarZoneOnly`, `_isLordWarZoneOnly`, `_isVillageWarZone`, `_isKingOrLordWarZone`, `_isMainTown`, `_isMinorTown` and `_isMainOrMinorTown`. That fits what the bytes hold (`0x13` on Siege and CastleInSiege, `0x14` on Fortress, `0x18` to `0x1A` on the towns), but this file has eight bytes for the seven, so which one is new is open. The client Lua reads `isVillageWarZone` and `isKingOrLordWarZone`.

### Remaining Unknown Head Fields

`unknown_0b`, `unknown_1d`, `unknown_1f`, `unknown_20`, `unknown_3a`, `unknown_42`, `unknown_52`, `unknown_77`, `unknown_95`, `unknown_99`, `unknown_ad`, `unknown_b1`, `unknown_b5` and `unknown_b9` match no `Region_Table` column. `unknown_0b` (`3` on the capitals) does not match `VillageTaxLevel` either.

## In-Game Checks

### Shabby Shovel in a No-Dig Region

This checks whether `is_not_dig` turns off desert digging.

1. Buy a Shabby Shovel from a material vendor in Valencia.
2. Use it in the open desert, for example in the Great Desert of Valencia. Note that you get a Bag of Muddy Water.
3. Go to Ibellab Oasis or Roud Sulfur Mine (both have `is_not_dig` set) and use it again.

Expected result: the shovel works in step 2 and is refused or yields nothing in step 3. If it works in step 3 too, the flag does something else.

### Region Types 7 and 8

Needs zone (all):

- Pit of the Undying (`950` or `1070`, type 7)
- Battle Arena (`1072`, type 8)

`CppEnums.RegionType` ends at Arena (6) with `_Count` = 7, but Pit of the Undying (950, 1070) has type 7 and one Battle Arena (1072) type 8. I searched all 3060 client Lua scripts: no `eRegionType_` value past Arena exists, and the only scripts that touch region types compare against `Siege`, `Fortress` and `MinorTown`.

What the client does have are region getters that fit the two types: `isPVEArenaZone` (used by the death message, game exit, manufacture and Morning Land boss panels) next to `isArenaZone` and `isArenaArea`. Pit of the Undying is a PvE arena, so type 7 is probably a PvE arena. `is_arena_zone` is set on every type 6 arena and on 1072, not on Pit of the Undying. Type 8 is a third Battle Arena on Rema Island next to 436 and 437 (type 6); the only differences from 436 in the record are the type, the colour and `unknown_tail_46` (437 also sets `is_safe_zone`), so I cannot tell what sets it apart. Possibly the Battle Arena that Trial Characters are locked into.

Enter both and note the death message and the exit prompt. If Pit of the Undying shows the PvE arena handling that `isPVEArenaZone` drives, type 7 is the PvE arena. If 1072 shows the same as Battle Arena 436, the difference of type 8 is not visible there; anything else (for example a Trial Character notice) names it.

### Node War Limits Outside Calpheon and Ulukita

Needs zone (any one):

- a node war node in Valencia
- a node war node in Edania

Heidel's limit set is what Calpheon and Ulukita nodes show in game (see Notes). Read the node tooltip of one Valencia or Edania node. The expected result is the uncapped set of Altinova and Valencia City (`9999`). That would confirm the capital records as the limits per territory pair, and `unknown_tail_86` (`5` on Calpheon and Ulukita, `15` on Valencia and Edania) as the key that picks which capital's set a node uses. Velia's set (AP 560, damage reduction 410, evasion 768, accuracy 680, damage reduction rate 20%) matches no node seen so far: the occupation mode nodes of Balenos and Serendia show other values. Note any node that shows it.
