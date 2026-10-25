# `regiongroupinfo.bss` Format

## Purpose

Lists the region groups that map regions belong to. Every region in `regioninfo.bss` carries a `regionGroupKey` (`+104` of its record head) that joins one row here, and each row here is used by at least one region. A row names the worldmap node of the group's main town or area, a concurrent user limit, three enable flags and a display position near the node.

The region group key is the value the client reads with `getRegionGroupKey()` on a region (`panel_lobby_characterselect_all_2.luac`, where it picks the login queue of the character's region). bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), `FORMATS.md`, section 11) documents only the `regionGroupKey` join on the `regioninfo.bss` side; the layout below is my own reading of this file, with field names from the sources in Field Names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records | Row bytes |
| ------ | -------------- | --------------------- | ------ | ------- | --------- |
| 2      | 2122 and later | `regiongroupinfo.bss` | 12,770 | 250 Row | 51        |
| 1      | 805 to 2107    | `regiongroupinfo.bss` | 8,595  | 175 Row | 49        |

| Layout | File                  | Known            | Unknown      |
| ------ | --------------------- | ---------------- | ------------ |
| 2      | `regiongroupinfo.bss` | 12,270 B (96.1%) | 500 B (3.9%) |
| 1      | `regiongroupinfo.bss` | 8,595 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `a3cafa7f7243`  |
| 3482   | Layout 2             | `a3cafa7f7243`  |
| 3474   | Layout 2             | `a3cafa7f7243`  |
| 3473   | Layout 2             | `a3cafa7f7243`  |
| 3464   | Layout 2             | `a3cafa7f7243`  |
| 3458   | Layout 2             | `a3cafa7f7243`  |
| 3454   | Layout 2             | `a3cafa7f7243`  |
| 3444   | Layout 2             | `a3cafa7f7243`  |
| 3435   | Layout 2             | `a3cafa7f7243`  |
| 3426   | Layout 2             | `a3cafa7f7243`  |
| 3418   | Layout 2             | `a3cafa7f7243`  |
| 3412   | Layout 2             | `a3cafa7f7243`  |
| 3402   | Layout 2             | `a3cafa7f7243`  |
| 3396   | Layout 2             | `a3cafa7f7243`  |
| 3387   | Layout 2             | `a3cafa7f7243`  |
| 3381   | Layout 2             | `a3cafa7f7243`  |
| 3373   | Layout 2             | `a3cafa7f7243`  |
| 3364   | Layout 2             | `a3cafa7f7243`  |
| 3356   | Layout 2             | `a3cafa7f7243`  |
| 3349   | Layout 2             | `a3cafa7f7243`  |
| 3342   | Layout 2             | `a3cafa7f7243`  |
| 3335   | Layout 2             | `a3cafa7f7243`  |
| 3326   | Layout 2             | `a3cafa7f7243`  |
| 3321   | Layout 2             | `a3cafa7f7243`  |
| 3314   | Layout 2             | `a3cafa7f7243`  |
| 3303   | Layout 2             | `a3cafa7f7243`  |
| 3302   | Layout 2             | `a3cafa7f7243`  |
| 3293   | Layout 2             | `a3cafa7f7243`  |
| 3283   | Layout 2             | `a3cafa7f7243`  |
| 3275   | Layout 2             | `a3cafa7f7243`  |
| 3267   | Layout 2             | `a3cafa7f7243`  |
| 3258   | Layout 2             | `a3cafa7f7243`  |
| 3251   | Layout 2             | `a3cafa7f7243`  |
| 3242   | Layout 2             | `a3cafa7f7243`  |
| 3235   | Layout 2             | `a3cafa7f7243`  |
| 3229   | Layout 2             | `a3cafa7f7243`  |
| 3212   | Layout 2             | `a3cafa7f7243`  |
| 3203   | Layout 2             | `a3cafa7f7243`  |
| 3193   | Layout 2             | `a3cafa7f7243`  |
| 3186   | Layout 2             | `a3cafa7f7243`  |
| 3177   | Layout 2             | `a3cafa7f7243`  |
| 3169   | Layout 2             | `a3cafa7f7243`  |
| 3158   | Layout 2             | `a3cafa7f7243`  |
| 3151   | Layout 2             | `a3cafa7f7243`  |
| 3144   | Layout 2             | `a3cafa7f7243`  |
| 3133   | Layout 2             | `a3cafa7f7243`  |
| 3125   | Layout 2             | `a3cafa7f7243`  |
| 3118   | Layout 2             | `a3cafa7f7243`  |
| 3111   | Layout 2             | `a3cafa7f7243`  |
| 3103   | Layout 2             | `a3cafa7f7243`  |
| 3095   | Layout 2             | `a3cafa7f7243`  |
| 3086   | Layout 2             | `a3cafa7f7243`  |
| 3072   | Layout 2             | `a3cafa7f7243`  |
| 3062   | Layout 2             | `a3cafa7f7243`  |
| 3052   | Layout 2             | `a3cafa7f7243`  |
| 3045   | Layout 2             | `a3cafa7f7243`  |
| 3037   | Layout 2             | `a3cafa7f7243`  |
| 3030   | Layout 2             | `a3cafa7f7243`  |
| 3021   | Layout 2             | `a3cafa7f7243`  |
| 3012   | Layout 2             | `a3cafa7f7243`  |
| 3002   | Layout 2             | `a3cafa7f7243`  |
| 2995   | Layout 2             | `a3cafa7f7243`  |
| 2987   | Layout 2             | `a3cafa7f7243`  |
| 2978   | Layout 2             | `a3cafa7f7243`  |
| 2970   | Layout 2             | `a3cafa7f7243`  |
| 2959   | Layout 2             | `a3cafa7f7243`  |
| 2951   | Layout 2             | `a3cafa7f7243`  |
| 2942   | Layout 2             | `a3cafa7f7243`  |
| 2935   | Layout 2             | `a3cafa7f7243`  |
| 2932   | Layout 2             | `a3cafa7f7243`  |
| 2923   | Layout 2             | `a3cafa7f7243`  |
| 2919   | Layout 2             | `a3cafa7f7243`  |
| 2907   | Layout 2             | `a3cafa7f7243`  |
| 2900   | Layout 2             | `a3cafa7f7243`  |
| 2891   | Layout 2             | `a3cafa7f7243`  |
| 2882   | Layout 2             | `a3cafa7f7243`  |
| 2872   | Layout 2             | `a3cafa7f7243`  |
| 2863   | Layout 2             | `a3cafa7f7243`  |
| 2855   | Layout 2             | `a3cafa7f7243`  |
| 2849   | Layout 2             | `a3cafa7f7243`  |
| 2844   | Layout 2             | `a3cafa7f7243`  |
| 2834   | Layout 2             | `a3cafa7f7243`  |
| 2825   | Layout 2             | `a3cafa7f7243`  |
| 2819   | Layout 2             | `a3cafa7f7243`  |
| 2811   | Layout 2             | `a3cafa7f7243`  |
| 2803   | Layout 2             | `a3cafa7f7243`  |
| 2794   | Layout 2             | `a3cafa7f7243`  |
| 2783   | Layout 2             | `a3cafa7f7243`  |
| 2774   | Layout 2             | `a3cafa7f7243`  |
| 2765   | Layout 2             | `a3cafa7f7243`  |
| 2756   | Layout 2             | `a3cafa7f7243`  |
| 2750   | Layout 2             | `a3cafa7f7243`  |
| 2743   | Layout 2             | `a3cafa7f7243`  |
| 2736   | Layout 2             | `a3cafa7f7243`  |
| 2726   | Layout 2             | `a3cafa7f7243`  |
| 2717   | Layout 2             | `a3cafa7f7243`  |
| 2709   | Layout 2             | `a3cafa7f7243`  |
| 2703   | Layout 2             | `a3cafa7f7243`  |
| 2695   | Layout 2             | `a3cafa7f7243`  |
| 2684   | Layout 2             | `a3cafa7f7243`  |
| 2672   | Layout 2             | `a3cafa7f7243`  |
| 2665   | Layout 2             | `a3cafa7f7243`  |
| 2657   | Layout 2             | `a3cafa7f7243`  |
| 2649   | Layout 2             | `a3cafa7f7243`  |
| 2644   | Layout 2             | `a3cafa7f7243`  |
| 2637   | Layout 2             | `a3cafa7f7243`  |
| 2629   | Layout 2             | `a3cafa7f7243`  |
| 2619   | Layout 2             | `a3cafa7f7243`  |
| 2612   | Layout 2             | `a3cafa7f7243`  |
| 2606   | Layout 2             | `a3cafa7f7243`  |
| 2602   | Layout 2             | `a3cafa7f7243`  |
| 2601   | Layout 2             | `a3cafa7f7243`  |
| 2592   | Layout 2             | `a3cafa7f7243`  |
| 2583   | Layout 2             | `a3cafa7f7243`  |
| 2575   | Layout 2             | `a3cafa7f7243`  |
| 2567   | Layout 2             | `a3cafa7f7243`  |
| 2560   | Layout 2             | `a3cafa7f7243`  |
| 2553   | Layout 2             | `a3cafa7f7243`  |
| 2545   | Layout 2             | `a3cafa7f7243`  |
| 2538   | Layout 2             | `a3cafa7f7243`  |
| 2529   | Layout 2             | `a3cafa7f7243`  |
| 2519   | Layout 2             | `a3cafa7f7243`  |
| 2513   | Layout 2             | `a3cafa7f7243`  |
| 2510   | Layout 2             | `a3cafa7f7243`  |
| 2507   | Layout 2             | `a3cafa7f7243`  |
| 2503   | Layout 2             | `a3cafa7f7243`  |
| 2498   | Layout 2             | `a3cafa7f7243`  |
| 2492   | Layout 2             | `a3cafa7f7243`  |
| 2487   | Layout 2             | `a3cafa7f7243`  |
| 2480   | Layout 2             | `a3cafa7f7243`  |
| 2474   | Layout 2             | `a3cafa7f7243`  |
| 2468   | Layout 2             | `a3cafa7f7243`  |
| 2460   | Layout 2             | `a3cafa7f7243`  |
| 2453   | Layout 2             | `a3cafa7f7243`  |
| 2444   | Layout 2             | `a3cafa7f7243`  |
| 2438   | Layout 2             | `a3cafa7f7243`  |
| 2434   | Layout 2             | `a3cafa7f7243`  |
| 2429   | Layout 2             | `a3cafa7f7243`  |
| 2421   | Layout 2             | `a3cafa7f7243`  |
| 2414   | Layout 2             | `a3cafa7f7243`  |
| 2407   | Layout 2             | `a3cafa7f7243`  |
| 2401   | Layout 2             | `a3cafa7f7243`  |
| 2397   | Layout 2             | `a3cafa7f7243`  |
| 2393   | Layout 2             | `a3cafa7f7243`  |
| 2384   | Layout 2             | `a3cafa7f7243`  |
| 2378   | Layout 2             | `a3cafa7f7243`  |
| 2372   | Layout 2             | `a3cafa7f7243`  |
| 2358   | Layout 2             | `a3cafa7f7243`  |
| 2352   | Layout 2             | `a3cafa7f7243`  |
| 2347   | Layout 2             | `a3cafa7f7243`  |
| 2343   | Layout 2             | `a3cafa7f7243`  |
| 2335   | Layout 2             | `a3cafa7f7243`  |
| 2327   | Layout 2             | `a3cafa7f7243`  |
| 2324   | Layout 2             | `a3cafa7f7243`  |
| 2319   | Layout 2             | `a3cafa7f7243`  |
| 2313   | Layout 2             | `a3cafa7f7243`  |
| 2308   | Layout 2             | `a3cafa7f7243`  |
| 2302   | Layout 2             | `a3cafa7f7243`  |
| 2295   | Layout 2             | `a3cafa7f7243`  |
| 2290   | Layout 2             | `a3cafa7f7243`  |
| 2284   | Layout 2             | `a3cafa7f7243`  |
| 2276   | Layout 2             | `a3cafa7f7243`  |
| 2269   | Layout 2             | `a3cafa7f7243`  |
| 2259   | Layout 2             | `a3cafa7f7243`  |
| 2250   | Layout 2             | `a3cafa7f7243`  |
| 2243   | Layout 2             | `a3cafa7f7243`  |
| 2235   | Layout 2             | `a3cafa7f7243`  |
| 2229   | Layout 2             | `a3cafa7f7243`  |
| 2224   | Layout 2             | `a3cafa7f7243`  |
| 2218   | Layout 2             | `a3cafa7f7243`  |
| 2215   | Layout 2             | `a3cafa7f7243`  |
| 2207   | Layout 2             | `a3cafa7f7243`  |
| 2203   | Layout 2             | `a3cafa7f7243`  |
| 2196   | Layout 2             | `a3cafa7f7243`  |
| 2192   | Layout 2             | `a3cafa7f7243`  |
| 2189   | Layout 2             | `a3cafa7f7243`  |
| 2183   | Layout 2             | `a3cafa7f7243`  |
| 2179   | Layout 2             | `a3cafa7f7243`  |
| 2171   | Layout 2             | `a3cafa7f7243`  |
| 2163   | Layout 2             | `a3cafa7f7243`  |
| 2156   | Layout 2             | `a3cafa7f7243`  |
| 2151   | Layout 2             | `a3cafa7f7243`  |
| 2147   | Layout 2             | `a3cafa7f7243`  |
| 2142   | Layout 2             | `a3cafa7f7243`  |
| 2138   | Layout 2             | `a3cafa7f7243`  |
| 2134   | Layout 2             | `a3cafa7f7243`  |
| 2130   | Layout 2             | `a3cafa7f7243`  |
| 2122   | Layout 2             | `a3cafa7f7243`  |
| 2107   | Layout 1             | `a3cafa7f7243`  |
| 2098   | Layout 1             | `a3cafa7f7243`  |
| 2089   | Layout 1             | `a3cafa7f7243`  |
| 2081   | Layout 1             | `a3cafa7f7243`  |
| 2073   | Layout 1             | `a3cafa7f7243`  |
| 2067   | Layout 1             | `a3cafa7f7243`  |
| 2063   | Layout 1             | `a3cafa7f7243`  |
| 2059   | Layout 1             | `a3cafa7f7243`  |
| 2052   | Layout 1             | `a3cafa7f7243`  |
| 2044   | Layout 1             | `a3cafa7f7243`  |
| 2039   | Layout 1             | `a3cafa7f7243`  |
| 2032   | Layout 1             | `a3cafa7f7243`  |
| 2025   | Layout 1             | `a3cafa7f7243`  |
| 2011   | Layout 1             | `a3cafa7f7243`  |
| 2005   | Layout 1             | `a3cafa7f7243`  |
| 2000   | Layout 1             | `a3cafa7f7243`  |
| 1996   | Layout 1             | `a3cafa7f7243`  |
| 1991   | Layout 1             | `a3cafa7f7243`  |
| 1985   | Layout 1             | `a3cafa7f7243`  |
| 1980   | Layout 1             | `a3cafa7f7243`  |
| 1969   | Layout 1             | `a3cafa7f7243`  |
| 1964   | Layout 1             | `a3cafa7f7243`  |
| 1958   | Layout 1             | `a3cafa7f7243`  |
| 1950   | Layout 1             | `a3cafa7f7243`  |
| 1945   | Layout 1             | `a3cafa7f7243`  |
| 1937   | Layout 1             | `a3cafa7f7243`  |
| 1933   | Layout 1             | `a3cafa7f7243`  |
| 1927   | Layout 1             | `a3cafa7f7243`  |
| 1921   | Layout 1             | `a3cafa7f7243`  |
| 1914   | Layout 1             | `a3cafa7f7243`  |
| 1908   | Layout 1             | `a3cafa7f7243`  |
| 1897   | Layout 1             | `a3cafa7f7243`  |
| 1892   | Layout 1             | `a3cafa7f7243`  |
| 1886   | Layout 1             | `a3cafa7f7243`  |
| 1881   | Layout 1             | `a3cafa7f7243`  |
| 1871   | Layout 1             | `a3cafa7f7243`  |
| 1866   | Layout 1             | `a3cafa7f7243`  |
| 1862   | Layout 1             | `a3cafa7f7243`  |
| 1854   | Layout 1             | `a3cafa7f7243`  |
| 1846   | Layout 1             | `a3cafa7f7243`  |
| 1838   | Layout 1             | `a3cafa7f7243`  |
| 1832   | Layout 1             | `a3cafa7f7243`  |
| 1826   | Layout 1             | `a3cafa7f7243`  |
| 1822   | Layout 1             | `a3cafa7f7243`  |
| 1818   | Layout 1             | `a3cafa7f7243`  |
| 1804   | Layout 1             | `a3cafa7f7243`  |
| 1794   | Layout 1             | `a3cafa7f7243`  |
| 1790   | Layout 1             | `a3cafa7f7243`  |
| 1784   | Layout 1             | `a3cafa7f7243`  |
| 1774   | Layout 1             | `a3cafa7f7243`  |
| 1771   | Layout 1             | `a3cafa7f7243`  |
| 1762   | Layout 1             | `a3cafa7f7243`  |
| 1759   | Layout 1             | `a3cafa7f7243`  |
| 1754   | Layout 1             | `a3cafa7f7243`  |
| 1749   | Layout 1             | `a3cafa7f7243`  |
| 1743   | Layout 1             | `a3cafa7f7243`  |
| 1737   | Layout 1             | `a3cafa7f7243`  |
| 1731   | Layout 1             | `a3cafa7f7243`  |
| 1725   | Layout 1             | `a3cafa7f7243`  |
| 1717   | Layout 1             | `a3cafa7f7243`  |
| 1710   | Layout 1             | `a3cafa7f7243`  |
| 1704   | Layout 1             | `a3cafa7f7243`  |
| 1698   | Layout 1             | `a3cafa7f7243`  |
| 1690   | Layout 1             | `a3cafa7f7243`  |
| 1685   | Layout 1             | `a3cafa7f7243`  |
| 1680   | Layout 1             | `a3cafa7f7243`  |
| 1674   | Layout 1             | `a3cafa7f7243`  |
| 1668   | Layout 1             | `a3cafa7f7243`  |
| 1659   | Layout 1             | `a3cafa7f7243`  |
| 1649   | Layout 1             | `a3cafa7f7243`  |
| 1642   | Layout 1             | `a3cafa7f7243`  |
| 1636   | Layout 1             | `a3cafa7f7243`  |
| 1628   | Layout 1             | `a3cafa7f7243`  |
| 1622   | Layout 1             | `a3cafa7f7243`  |
| 1614   | Layout 1             | `a3cafa7f7243`  |
| 1608   | Layout 1             | `a3cafa7f7243`  |
| 1602   | Layout 1             | `a3cafa7f7243`  |
| 1598   | Layout 1             | `a3cafa7f7243`  |
| 1594   | Layout 1             | `a3cafa7f7243`  |
| 1590   | Layout 1             | `a3cafa7f7243`  |
| 1587   | Layout 1             | `a3cafa7f7243`  |
| 1584   | Layout 1             | `a3cafa7f7243`  |
| 1579   | Layout 1             | `a3cafa7f7243`  |
| 1572   | Layout 1             | `a3cafa7f7243`  |
| 1565   | Layout 1             | `a3cafa7f7243`  |
| 1559   | Layout 1             | `a3cafa7f7243`  |
| 1554   | Layout 1             | `a3cafa7f7243`  |
| 1547   | Layout 1             | `a3cafa7f7243`  |
| 1537   | Layout 1             | `a3cafa7f7243`  |
| 1529   | Layout 1             | `a3cafa7f7243`  |
| 1524   | Layout 1             | `a3cafa7f7243`  |
| 1519   | Layout 1             | `a3cafa7f7243`  |
| 1509   | Layout 1             | `a3cafa7f7243`  |
| 1506   | Layout 1             | `a3cafa7f7243`  |
| 1504   | Layout 1             | `a3cafa7f7243`  |
| 1500   | Layout 1             | `a3cafa7f7243`  |
| 1493   | Layout 1             | `a3cafa7f7243`  |
| 1489   | Layout 1             | `a3cafa7f7243`  |
| 1485   | Layout 1             | `a3cafa7f7243`  |
| 1481   | Layout 1             | `a3cafa7f7243`  |
| 1474   | Layout 1             | `a3cafa7f7243`  |
| 1466   | Layout 1             | `a3cafa7f7243`  |
| 1462   | Layout 1             | `a3cafa7f7243`  |
| 1459   | Layout 1             | `a3cafa7f7243`  |
| 1453   | Layout 1             | `a3cafa7f7243`  |
| 1450   | Layout 1             | `a3cafa7f7243`  |
| 1445   | Layout 1             | `a3cafa7f7243`  |
| 1439   | Layout 1             | `a3cafa7f7243`  |
| 1433   | Layout 1             | `a3cafa7f7243`  |
| 1430   | Layout 1             | `a3cafa7f7243`  |
| 1426   | Layout 1             | `a3cafa7f7243`  |
| 1421   | Layout 1             | `a3cafa7f7243`  |
| 1417   | Layout 1             | `a3cafa7f7243`  |
| 1416   | Layout 1             | `a3cafa7f7243`  |
| 1409   | Layout 1             | `a3cafa7f7243`  |
| 1405   | Layout 1             | `a3cafa7f7243`  |
| 1401   | Layout 1             | `a3cafa7f7243`  |
| 1396   | Layout 1             | `a3cafa7f7243`  |
| 1391   | Layout 1             | `a3cafa7f7243`  |
| 1390   | Layout 1             | `a3cafa7f7243`  |
| 1386   | Layout 1             | `a3cafa7f7243`  |
| 1381   | Layout 1             | `a3cafa7f7243`  |
| 1379   | Layout 1             | `a3cafa7f7243`  |
| 1372   | Layout 1             | `a3cafa7f7243`  |
| 1366   | Layout 1             | `a3cafa7f7243`  |
| 1364   | Layout 1             | `a3cafa7f7243`  |
| 1363   | Layout 1             | `a3cafa7f7243`  |
| 1360   | Layout 1             | `a3cafa7f7243`  |
| 1358   | Layout 1             | `a3cafa7f7243`  |
| 1355   | Layout 1             | `a3cafa7f7243`  |
| 1351   | Layout 1             | `a3cafa7f7243`  |
| 1348   | Layout 1             | `a3cafa7f7243`  |
| 1346   | Layout 1             | `a3cafa7f7243`  |
| 1341   | Layout 1             | `a3cafa7f7243`  |
| 1340   | Layout 1             | `a3cafa7f7243`  |
| 1338   | Layout 1             | `a3cafa7f7243`  |
| 1335   | Layout 1             | `a3cafa7f7243`  |
| 1333   | Layout 1             | `a3cafa7f7243`  |
| 1329   | Layout 1             | `a3cafa7f7243`  |
| 1327   | Layout 1             | `a3cafa7f7243`  |
| 1324   | Layout 1             | `a3cafa7f7243`  |
| 1321   | Layout 1             | `a3cafa7f7243`  |
| 1319   | Layout 1             | `a3cafa7f7243`  |
| 1318   | Layout 1             | `a3cafa7f7243`  |
| 1316   | Layout 1             | `a3cafa7f7243`  |
| 1313   | Layout 1             | `a3cafa7f7243`  |
| 1311   | Layout 1             | `a3cafa7f7243`  |
| 1309   | Layout 1             | `a3cafa7f7243`  |
| 1304   | Layout 1             | `a3cafa7f7243`  |
| 1292   | Layout 1             | `a3cafa7f7243`  |
| 1286   | Layout 1             | `a3cafa7f7243`  |
| 1280   | Layout 1             | `a3cafa7f7243`  |
| 1276   | Layout 1             | `a3cafa7f7243`  |
| 1267   | Layout 1             | `a3cafa7f7243`  |
| 1261   | Layout 1             | `a3cafa7f7243`  |
| 1256   | Layout 1             | `a3cafa7f7243`  |
| 1250   | Layout 1             | `a3cafa7f7243`  |
| 1246   | Layout 1             | `a3cafa7f7243`  |
| 1239   | Layout 1             | `a3cafa7f7243`  |
| 1230   | Layout 1             | `a3cafa7f7243`  |
| 1226   | Layout 1             | `a3cafa7f7243`  |
| 1220   | Layout 1             | `a3cafa7f7243`  |
| 1217   | Layout 1             | `a3cafa7f7243`  |
| 1211   | Layout 1             | `a3cafa7f7243`  |
| 1210   | Layout 1             | `a3cafa7f7243`  |
| 1208   | Layout 1             | `a3cafa7f7243`  |
| 1203   | Layout 1             | `a3cafa7f7243`  |
| 1197   | Layout 1             | `a3cafa7f7243`  |
| 1194   | Layout 1             | `a3cafa7f7243`  |
| 1192   | Layout 1             | `a3cafa7f7243`  |
| 1187   | Layout 1             | `a3cafa7f7243`  |
| 1183   | Layout 1             | `a3cafa7f7243`  |
| 1177   | Layout 1             | `a3cafa7f7243`  |
| 1173   | Layout 1             | `a3cafa7f7243`  |
| 1167   | Layout 1             | `a3cafa7f7243`  |
| 1164   | Layout 1             | `a3cafa7f7243`  |
| 1156   | Layout 1             | `a3cafa7f7243`  |
| 1149   | Layout 1             | `a3cafa7f7243`  |
| 1144   | Layout 1             | `a3cafa7f7243`  |
| 1137   | Layout 1             | `a3cafa7f7243`  |
| 1132   | Layout 1             | `a3cafa7f7243`  |
| 1127   | Layout 1             | `a3cafa7f7243`  |
| 1122   | Layout 1             | `a3cafa7f7243`  |
| 1118   | Layout 1             | `a3cafa7f7243`  |
| 1114   | Layout 1             | `a3cafa7f7243`  |
| 1109   | Layout 1             | `a3cafa7f7243`  |
| 1102   | Layout 1             | `a3cafa7f7243`  |
| 1096   | Layout 1             | `a3cafa7f7243`  |
| 1088   | Layout 1             | `a3cafa7f7243`  |
| 1081   | Layout 1             | `a3cafa7f7243`  |
| 1076   | Layout 1             | `a3cafa7f7243`  |
| 1069   | Layout 1             | `a3cafa7f7243`  |
| 1064   | Layout 1             | `a3cafa7f7243`  |
| 1058   | Layout 1             | `a3cafa7f7243`  |
| 1051   | Layout 1             | `a3cafa7f7243`  |
| 1044   | Layout 1             | `a3cafa7f7243`  |
| 1036   | Layout 1             | `a3cafa7f7243`  |
| 1026   | Layout 1             | `a3cafa7f7243`  |
| 1016   | Layout 1             | `a3cafa7f7243`  |
| 1009   | Layout 1             | `a3cafa7f7243`  |
| 1005   | Layout 1             | `a3cafa7f7243`  |
| 1000   | Layout 1             | `a3cafa7f7243`  |
| 998    | Layout 1             | `a3cafa7f7243`  |
| 990    | Layout 1             | `a3cafa7f7243`  |
| 979    | Layout 1             | `a3cafa7f7243`  |
| 972    | Layout 1             | `a3cafa7f7243`  |
| 963    | Layout 1             | `a3cafa7f7243`  |
| 955    | Layout 1             | `a3cafa7f7243`  |
| 946    | Layout 1             | `a3cafa7f7243`  |
| 938    | Layout 1             | `a3cafa7f7243`  |
| 927    | Layout 1             | `a3cafa7f7243`  |
| 911    | Layout 1             | `a3cafa7f7243`  |
| 904    | Layout 1             | `a3cafa7f7243`  |
| 899    | Layout 1             | `a3cafa7f7243`  |
| 894    | Layout 1             | `a3cafa7f7243`  |
| 885    | Layout 1             | `a3cafa7f7243`  |
| 879    | Layout 1             | `a3cafa7f7243`  |
| 872    | Layout 1             | `a3cafa7f7243`  |
| 864    | Layout 1             | `a3cafa7f7243`  |
| 855    | Layout 1             | `a3cafa7f7243`  |
| 853    | Layout 1             | `a3cafa7f7243`  |
| 845    | Layout 1             | `a3cafa7f7243`  |
| 837    | Layout 1             | `a3cafa7f7243`  |
| 829    | Layout 1             | `a3cafa7f7243`  |
| 822    | Layout 1             | `a3cafa7f7243`  |
| 814    | Layout 1             | `a3cafa7f7243`  |
| 805    | Layout 1             | `a3cafa7f7243`  |
| 794    | No documented layout | `a3cafa7f7243`  |
| 787    | No documented layout | `a3cafa7f7243`  |
| 780    | No documented layout | `a3cafa7f7243`  |
| 771    | No documented layout | `a3cafa7f7243`  |
| 760    | No documented layout | `a3cafa7f7243`  |
| 748    | No documented layout | `a3cafa7f7243`  |
| 741    | No documented layout | `a3cafa7f7243`  |
| 736    | No documented layout | `a3cafa7f7243`  |
| 731    | No documented layout | `a3cafa7f7243`  |
| 723    | No documented layout | `a3cafa7f7243`  |
| 711    | No documented layout | `a3cafa7f7243`  |
| 707    | No documented layout | `a3cafa7f7243`  |
| 697    | No documented layout | `a3cafa7f7243`  |
| 689    | No documented layout | `a3cafa7f7243`  |
| 683    | No documented layout | `a3cafa7f7243`  |
| 678    | No documented layout | `a3cafa7f7243`  |
| 670    | No documented layout | `a3cafa7f7243`  |
| 661    | No documented layout | `a3cafa7f7243`  |
| 656    | No documented layout | `a3cafa7f7243`  |
| 652    | No documented layout | `a3cafa7f7243`  |
| 643    | No documented layout | `a3cafa7f7243`  |
| 637    | No documented layout | `a3cafa7f7243`  |
| 630    | No documented layout | `a3cafa7f7243`  |
| 627    | No documented layout | `a3cafa7f7243`  |
| 621    | No documented layout | `a3cafa7f7243`  |
| 617    | No documented layout | `a3cafa7f7243`  |
| 615    | No documented layout | `a3cafa7f7243`  |
| 606    | No documented layout | `a3cafa7f7243`  |
| 599    | No documented layout | `a3cafa7f7243`  |
| 592    | No documented layout | `a3cafa7f7243`  |
| 586    | No documented layout | `a3cafa7f7243`  |
| 577    | No documented layout | `a3cafa7f7243`  |
| 569    | No documented layout | `a3cafa7f7243`  |
| 561    | No documented layout | `a3cafa7f7243`  |
| 554    | No documented layout | `a3cafa7f7243`  |
| 542    | No documented layout | `a3cafa7f7243`  |
| 532    | No documented layout | `a3cafa7f7243`  |
| 531    | No documented layout | `a3cafa7f7243`  |
| 526    | No documented layout | `a3cafa7f7243`  |
| 521    | No documented layout | `a3cafa7f7243`  |
| 517    | No documented layout | `a3cafa7f7243`  |
| 510    | No documented layout | `a3cafa7f7243`  |
| 508    | No documented layout | `a3cafa7f7243`  |
| 504    | No documented layout | `a3cafa7f7243`  |
| 497    | No documented layout | `a3cafa7f7243`  |
| 491    | No documented layout | `a3cafa7f7243`  |
| 485    | No documented layout | `a3cafa7f7243`  |
| 478    | No documented layout | `a3cafa7f7243`  |
| 472    | No documented layout | `a3cafa7f7243`  |
| 466    | No documented layout | `a3cafa7f7243`  |
| 457    | No documented layout | `a3cafa7f7243`  |
| 452    | No documented layout | `a3cafa7f7243`  |
| 449    | No documented layout | `a3cafa7f7243`  |
| 435    | No documented layout | `a3cafa7f7243`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29, keyed by `node_key`)         |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                                          |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                                 |
| `+0x04`             | u32               | record_count       | Observed `250`                                                 |
| `+0x08`             | Row[record_count] | records            | `record_count` rows of 51 bytes, byte-packed                   |
| `records+0x00`      | String Table      | string_table       | Always empty: the PABR string table is present but empty       |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 51 × count`     |
| `string_table+0x04` | u32               | zero               | Always `0`                                                     |

The file is `8 + 51 × 250 + 12 = 12770` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (51 bytes)

| Offset  | Type   | Field            | Notes                                                                                              |
| ------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| `+0x00` | u16    | region_group_key | Unique; joins `regionGroupKey` of `regioninfo.bss`; `0` to `302`, with gaps, not in key order      |
| `+0x02` | u8     | is_blocked_managing | Always `0`                                                                                      |
| `+0x03` | u16    | concurrent_playable_user_count | `500`, `999`, `1000`, `1300`, `2000`, `3000` (Velia) or `10000` (key 0), see below |
| `+0x05` | u32    | node_key         | Worldmap node (`exploration.bss` key, LOC type 29); `0` on 19 rows                                 |
| `+0x09` | u8     | enable_corp_productivity | `0` on 20 rows, nearly all without a node or position                                      |
| `+0x0A` | u8     | enable_fishing_productivity | Equals `enable_corp_productivity` on every row                                          |
| `+0x0B` | u8     | enable_loyalty   | `1` on 14 rows, all main towns, see below                                                          |
| `+0x0C` | f32[3] | display_graph_position | World `x, y, z`; all zero on 19 rows                                                         |
| `+0x18` | u8     | is_productivity_changed | Always `0`                                                                                  |
| `+0x19` | i32    | corp_productivity | Always `1000000`, the 2016 loader's default                                                       |
| `+0x1D` | i32    | fishing_productivity | Always `1000000`, the 2016 loader's default                                                    |
| `+0x21` | i32    | loyalty          | Always `1000000`, the 2016 loader's default                                                        |
| `+0x25` | i32[3] | varied_productivity | Always `0`: `_variedCorpProductivity`, `_variedFishingProductivity`, `_variedLoyalty`           |
| `+0x31` | u8     | unknown_31       | Always `1`; after the 2016 members, see Open Questions                                             |
| `+0x32` | u8     | unknown_32       | Always `0`                                                                                         |

Earlier versions of this doc read `+0x05` as a u16 with two bytes of padding and called the fields from `+0x03` to `+0x21` `unknown_03` to `unknown_21`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 a Row was 49 bytes: it ended after `varied_productivity`,
without `unknown_31` and `unknown_32`. Only the Row differs from Layout 2.
The file holds `170` rows on client 1784.

### Row (49 bytes)

| Offset  | Type   | Field                          | Notes |
| ------- | ------ | ------------------------------ | ----- |
| `+0x00` | u16    | region_group_key               |       |
| `+0x02` | u8     | is_blocked_managing            |       |
| `+0x03` | u16    | concurrent_playable_user_count |       |
| `+0x05` | u32    | node_key                       |       |
| `+0x09` | u8     | enable_corp_productivity       |       |
| `+0x0A` | u8     | enable_fishing_productivity    |       |
| `+0x0B` | u8     | enable_loyalty                 |       |
| `+0x0C` | f32[3] | display_graph_position         |       |
| `+0x18` | u8     | is_productivity_changed        |       |
| `+0x19` | i32    | corp_productivity              |       |
| `+0x1D` | i32    | fishing_productivity           |       |
| `+0x21` | i32    | loyalty                        |       |
| `+0x25` | i32[3] | varied_productivity            |       |

## Row Values

### `concurrent_playable_user_count` Values (client 3473)

| Value   | Rows | Groups |
| ------- | ---- | ------ |
| `10000` | 1    | Group 0 |
| `3000`  | 1    | Velia |
| `2000`  | 8    | Heidel, Calpheon, Calpheon Castle, Behr, Mediah Shore, Loopy Tree Forest, Valencia City and the node-less group 40 |
| `1300`  | 2    | Olvia and Olvia Academy |
| `1000`  | 41   | Kamasylvia, Drieghan and the newer regions |
| `999`   | 49   | Most of Mediah (Altinova included), Valencia and the open sea |
| `500`   | 148  | All other groups |

The character select screen asks for the login queue of a character's region group (`getTicketCountByRegion`), which fits a per-group user limit.

### `enable_loyalty` Groups

Set on 14 groups: Velia, Heidel, Glish, Calpheon, Trent, Keplan, Altinova, Olvia, Valencia City, Shakatu, Sand Grain Bazaar, Duvencrune, O'draxxia and Olvia Academy. Other main towns such as Iliya Island, Tarif, Port Epheria, Grána and Arehaza are not.

The parser stores `node_key` as `None` when it is `0`, and `display_graph_position` as `pos_x`, `pos_y`, `pos_z`, each `None` when all three are `0`. It keeps the fields with a value other than `0` and leaves out `is_blocked_managing`, `is_productivity_changed` and `varied_productivity`.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::RegionGroupInfo` holds `_key`, `_isBlockedManaging`, `_concurrentPlayableUserCount`, `_waypointKey` (i32), `_enableCorpProductivity`, `_enableFishingProductivity`, `_enableLoyalty`, `_regionPosition`, `_isProductivityChanged`, `_corpProductivity`, `_fishingProductivity`, `_loyalty`, `_variedCorpProductivity`, `_variedFishingProductivity` and `_variedLoyalty` (all i32), with pointers in between. The row stores them in this order without the pointers or padding, from `+0x00` to `+0x30`. `GameCommonParameterLoaderFromExcel::LoadRegionGroupInformation` reads `RegionGroupKey`, `WaypointKey`, `DisplayGraphPositionX` to `Z`, `CorpProductivity`, `FishingProductivity`, `Loyalty` (as bools) and `ConcurrentPlayableUserCount` from `RegionGroup_Table` into those members, and sets `_corpProductivity`, `_fishingProductivity` and `_loyalty` to `1000000` and the three varied values to `0` for every row: the values this file stores.

The `RegionGroup_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 and the same table of a second private server on client 519 match the file by value over the group keys each shares with client 3473:

| Column | Field | Equal (client 1784, 169 keys) | Equal (client 519, 150 keys) |
| ------ | ----- | ------------------------ | ------------------------ |
| `WaypointKey` | `node_key` | 168 | 148 |
| `CorpProductivity` | `enable_corp_productivity` | 168 | 149 |
| `FishingProductivity` | `enable_fishing_productivity` | 168 | 149 |
| `Loyalty` | `enable_loyalty` | 169 | 150 |
| `ConcurrentPlayableUserCount` | `concurrent_playable_user_count` | 139 | 118 |
| `DisplayGraphPositionX` to `Z` | `display_graph_position` | 168 | 149 |

The two productivity flags hold the same value on every row in all three sources, so they are told apart by the 2016 order alone. The other `ConcurrentPlayableUserCount` rows are raises (`500` to `1000` on 25 bexcel rows, `500` or `999` to `2000` on 5); the file and both tables use the same seven values. Group 179 has both productivity flags set here and clear in both tables. `is_blocked_managing` and `is_productivity_changed` have no column; they are named from their place in the 2016 member order.

## Notes

- Joining `regioninfo.bss` on `regionGroupKey` (record head `+104`) uses every one of the 250 keys and no other: no region points at a missing group and no group is unused.
- `node_key` is the `explorationKey` (`regioninfo.bss` head `+111`) of one of the group's own regions on 218 of the 231 groups that have a node. The other 13 are group `101` (node `1024`) and the open-sea groups `181` to `192` (nodes `1721` to `1733`, which have no LOC name), whose regions point at other sea nodes.
- The node is the group's main town or area: group 1 is Velia (node 1) and holds region 5 Velia (a town region), group 11 is Heidel (node 301) for Serendia, group 31 is Calpheon (node 601), group 55 Altinova (node 1101), group 202 Valencia City (node 1301).
- `display_graph_position` is near the node but is not the node's position from `mapdata_realexplore2.bwp`: the distance is usually 5,000 to 50,000 units (Velia: group `7542, -6548, 72626`, node `13800, -6715, 76996`). Groups 160 to 176 and 194 to 198 share one position (`-127640, 8789, -446513`) although their nodes lie far apart, and groups 215 to 220 share another. The sheet column is `DisplayGraphPosition` and the 2016 member `_regionPosition`.
- The file has no strings of its own and the client has no LOC type for region group names, so a group is shown by its node.
- The client Lua uses the group key in only three places: the login queue (`getRegionGroupKey`, `getTicketCountByRegion`), the NPC navigator filter (`regionGroup`) and a worker `RegionWork` result (`regionGroupInfo`). None of them reads a field of this file by name.
- The client 519 private server loads `CorpProductivity`, `FishingProductivity` and `Loyalty` but never reads them back. Every 15 minutes its `RegionProductivityService` picks a random value from 500,000 to 1,000,000 per group for each of `Loyalty`, `Farming` and `Fishing` and sends all groups in one packet, as fishing, farming, loyalty per group. It calls corp productivity "Farming", which is its own name and no client source confirms it.

## Open Questions

### What the Productivity and Loyalty Flags Drive

The client Lua reads none of the three enable flags or the productivity values. It registers `FromClient_NotifyChangeRegionProductivity`, which only refreshes the worker and node product windows (`new_worldmap_workmanager_plant.luac`, `panel_worldmap_nodeproduct_renew.luac`), so the server can change a region's productivity at run time. The 2016 `_varied*` members suggest it adjusts the `1000000` base per group; which game feature the corp, fishing and loyalty values stand for is unknown.

### unknown_31

A u8 of `1` on every row, after the last 2016 member. A constant cannot be told apart from the data alone, and no sheet column is left to match it.
