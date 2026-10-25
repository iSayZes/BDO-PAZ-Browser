# `baseobject.bss` Format

## Purpose

One row per placeable world object (furniture, crops, houses, tents,
barricades and siege buildings), keyed by the object's character ID: its
armor material, object kind, installation type, collision and siege tent
flags, the six
placement flags, two 4x4 matrices that are set on houses only, and the
house hull: floor layers of convex hulls, each hull a list of planes. It
holds the numeric part of the 2016 `gc::ObjectStaticStatus`; the model
paths, icons and Korean house text of the same objects are in
[`characterobject.dbss`](../dbss/characterobject_dbss.md), which has a record for
every character ID here.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes     | Records                                              | Row bytes |
| ------ | -------------- | ---------------- | --------- | ---------------------------------------------------- | --------- |
| 2      | 1762 and later | `baseobject.bss` | 4,762,336 | 5,131 Row, 28,202 Face, 2,321 Hull, 1,079 Hull Layer | 140       |
| 1      | 1333 to 1759   | `baseobject.bss` | 4,060,119 | 3,461 Row, 25,082 Face, 2,063 Hull, 978 Hull Layer   | 140       |

| Layout | File             | Known               | Unknown           |
| ------ | ---------------- | ------------------- | ----------------- |
| 2      | `baseobject.bss` | 3,936,319 B (82.7%) | 826,017 B (17.3%) |
| 1      | `baseobject.bss` | 3,482,173 B (85.8%) | 577,946 B (14.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `3a7f890b64d5`  |
| 3482   | Layout 2             | `3a7f890b64d5`  |
| 3474   | Layout 2             | `3a7f890b64d5`  |
| 3473   | Layout 2             | `3a7f890b64d5`  |
| 3464   | Layout 2             | `3a7f890b64d5`  |
| 3458   | Layout 2             | `3a7f890b64d5`  |
| 3454   | Layout 2             | `3a7f890b64d5`  |
| 3444   | Layout 2             | `3a7f890b64d5`  |
| 3435   | Layout 2             | `3a7f890b64d5`  |
| 3426   | Layout 2             | `3a7f890b64d5`  |
| 3418   | Layout 2             | `3a7f890b64d5`  |
| 3412   | Layout 2             | `3a7f890b64d5`  |
| 3402   | Layout 2             | `3a7f890b64d5`  |
| 3396   | Layout 2             | `3a7f890b64d5`  |
| 3387   | Layout 2             | `3a7f890b64d5`  |
| 3381   | Layout 2             | `3a7f890b64d5`  |
| 3373   | Layout 2             | `3a7f890b64d5`  |
| 3364   | Layout 2             | `3a7f890b64d5`  |
| 3356   | Layout 2             | `3a7f890b64d5`  |
| 3349   | Layout 2             | `3a7f890b64d5`  |
| 3342   | Layout 2             | `3a7f890b64d5`  |
| 3335   | Layout 2             | `3a7f890b64d5`  |
| 3326   | Layout 2             | `3a7f890b64d5`  |
| 3321   | Layout 2             | `3a7f890b64d5`  |
| 3314   | Layout 2             | `3a7f890b64d5`  |
| 3303   | Layout 2             | `3a7f890b64d5`  |
| 3302   | Layout 2             | `3a7f890b64d5`  |
| 3293   | Layout 2             | `3a7f890b64d5`  |
| 3283   | Layout 2             | `3a7f890b64d5`  |
| 3275   | Layout 2             | `3a7f890b64d5`  |
| 3267   | Layout 2             | `3a7f890b64d5`  |
| 3258   | Layout 2             | `3a7f890b64d5`  |
| 3251   | Layout 2             | `3a7f890b64d5`  |
| 3242   | Layout 2             | `3a7f890b64d5`  |
| 3235   | Layout 2             | `3a7f890b64d5`  |
| 3229   | Layout 2             | `3a7f890b64d5`  |
| 3212   | Layout 2             | `3a7f890b64d5`  |
| 3203   | Layout 2             | `3a7f890b64d5`  |
| 3193   | Layout 2             | `3a7f890b64d5`  |
| 3186   | Layout 2             | `3a7f890b64d5`  |
| 3177   | Layout 2             | `3a7f890b64d5`  |
| 3169   | Layout 2             | `3a7f890b64d5`  |
| 3158   | Layout 2             | `3a7f890b64d5`  |
| 3151   | Layout 2             | `3a7f890b64d5`  |
| 3144   | Layout 2             | `3a7f890b64d5`  |
| 3133   | Layout 2             | `3a7f890b64d5`  |
| 3125   | Layout 2             | `3a7f890b64d5`  |
| 3118   | Layout 2             | `3a7f890b64d5`  |
| 3111   | Layout 2             | `3a7f890b64d5`  |
| 3103   | Layout 2             | `3a7f890b64d5`  |
| 3095   | Layout 2             | `3a7f890b64d5`  |
| 3086   | Layout 2             | `3a7f890b64d5`  |
| 3072   | Layout 2             | `3a7f890b64d5`  |
| 3062   | Layout 2             | `3a7f890b64d5`  |
| 3052   | Layout 2             | `3a7f890b64d5`  |
| 3045   | Layout 2             | `3a7f890b64d5`  |
| 3037   | Layout 2             | `3a7f890b64d5`  |
| 3030   | Layout 2             | `3a7f890b64d5`  |
| 3021   | Layout 2             | `3a7f890b64d5`  |
| 3012   | Layout 2             | `3a7f890b64d5`  |
| 3002   | Layout 2             | `3a7f890b64d5`  |
| 2995   | Layout 2             | `3a7f890b64d5`  |
| 2987   | Layout 2             | `3a7f890b64d5`  |
| 2978   | Layout 2             | `3a7f890b64d5`  |
| 2970   | Layout 2             | `3a7f890b64d5`  |
| 2959   | Layout 2             | `3a7f890b64d5`  |
| 2951   | Layout 2             | `3a7f890b64d5`  |
| 2942   | Layout 2             | `3a7f890b64d5`  |
| 2935   | Layout 2             | `3a7f890b64d5`  |
| 2932   | Layout 2             | `3a7f890b64d5`  |
| 2923   | Layout 2             | `3a7f890b64d5`  |
| 2919   | Layout 2             | `3a7f890b64d5`  |
| 2907   | Layout 2             | `3a7f890b64d5`  |
| 2900   | Layout 2             | `3a7f890b64d5`  |
| 2891   | Layout 2             | `3a7f890b64d5`  |
| 2882   | Layout 2             | `3a7f890b64d5`  |
| 2872   | Layout 2             | `3a7f890b64d5`  |
| 2863   | Layout 2             | `3a7f890b64d5`  |
| 2855   | Layout 2             | `3a7f890b64d5`  |
| 2849   | Layout 2             | `3a7f890b64d5`  |
| 2844   | Layout 2             | `3a7f890b64d5`  |
| 2834   | Layout 2             | `3a7f890b64d5`  |
| 2825   | Layout 2             | `3a7f890b64d5`  |
| 2819   | Layout 2             | `3a7f890b64d5`  |
| 2811   | Layout 2             | `3a7f890b64d5`  |
| 2803   | Layout 2             | `3a7f890b64d5`  |
| 2794   | Layout 2             | `3a7f890b64d5`  |
| 2783   | Layout 2             | `3a7f890b64d5`  |
| 2774   | Layout 2             | `3a7f890b64d5`  |
| 2765   | Layout 2             | `3a7f890b64d5`  |
| 2756   | Layout 2             | `3a7f890b64d5`  |
| 2750   | Layout 2             | `3a7f890b64d5`  |
| 2743   | Layout 2             | `3a7f890b64d5`  |
| 2736   | Layout 2             | `3a7f890b64d5`  |
| 2726   | Layout 2             | `3a7f890b64d5`  |
| 2717   | Layout 2             | `3a7f890b64d5`  |
| 2709   | Layout 2             | `3a7f890b64d5`  |
| 2703   | Layout 2             | `3a7f890b64d5`  |
| 2695   | Layout 2             | `3a7f890b64d5`  |
| 2684   | Layout 2             | `3a7f890b64d5`  |
| 2672   | Layout 2             | `3a7f890b64d5`  |
| 2665   | Layout 2             | `3a7f890b64d5`  |
| 2657   | Layout 2             | `3a7f890b64d5`  |
| 2649   | Layout 2             | `3a7f890b64d5`  |
| 2644   | Layout 2             | `3a7f890b64d5`  |
| 2637   | Layout 2             | `3a7f890b64d5`  |
| 2629   | Layout 2             | `3a7f890b64d5`  |
| 2619   | Layout 2             | `3a7f890b64d5`  |
| 2612   | Layout 2             | `3a7f890b64d5`  |
| 2606   | Layout 2             | `3a7f890b64d5`  |
| 2602   | Layout 2             | `3a7f890b64d5`  |
| 2601   | Layout 2             | `3a7f890b64d5`  |
| 2592   | Layout 2             | `3a7f890b64d5`  |
| 2583   | Layout 2             | `3a7f890b64d5`  |
| 2575   | Layout 2             | `3a7f890b64d5`  |
| 2567   | Layout 2             | `3a7f890b64d5`  |
| 2560   | Layout 2             | `3a7f890b64d5`  |
| 2553   | Layout 2             | `3a7f890b64d5`  |
| 2545   | Layout 2             | `3a7f890b64d5`  |
| 2538   | Layout 2             | `3a7f890b64d5`  |
| 2529   | Layout 2             | `3a7f890b64d5`  |
| 2519   | Layout 2             | `3a7f890b64d5`  |
| 2513   | Layout 2             | `3a7f890b64d5`  |
| 2510   | Layout 2             | `3a7f890b64d5`  |
| 2507   | Layout 2             | `3a7f890b64d5`  |
| 2503   | Layout 2             | `3a7f890b64d5`  |
| 2498   | Layout 2             | `3a7f890b64d5`  |
| 2492   | Layout 2             | `3a7f890b64d5`  |
| 2487   | Layout 2             | `3a7f890b64d5`  |
| 2480   | Layout 2             | `3a7f890b64d5`  |
| 2474   | Layout 2             | `3a7f890b64d5`  |
| 2468   | Layout 2             | `3a7f890b64d5`  |
| 2460   | Layout 2             | `3a7f890b64d5`  |
| 2453   | Layout 2             | `3a7f890b64d5`  |
| 2444   | Layout 2             | `3a7f890b64d5`  |
| 2438   | Layout 2             | `3a7f890b64d5`  |
| 2434   | Layout 2             | `3a7f890b64d5`  |
| 2429   | Layout 2             | `3a7f890b64d5`  |
| 2421   | Layout 2             | `3a7f890b64d5`  |
| 2414   | Layout 2             | `3a7f890b64d5`  |
| 2407   | Layout 2             | `3a7f890b64d5`  |
| 2401   | Layout 2             | `3a7f890b64d5`  |
| 2397   | Layout 2             | `3a7f890b64d5`  |
| 2393   | Layout 2             | `3a7f890b64d5`  |
| 2384   | Layout 2             | `3a7f890b64d5`  |
| 2378   | Layout 2             | `3a7f890b64d5`  |
| 2372   | Layout 2             | `3a7f890b64d5`  |
| 2358   | Layout 2             | `3a7f890b64d5`  |
| 2352   | Layout 2             | `3a7f890b64d5`  |
| 2347   | Layout 2             | `3a7f890b64d5`  |
| 2343   | Layout 2             | `3a7f890b64d5`  |
| 2335   | Layout 2             | `3a7f890b64d5`  |
| 2327   | Layout 2             | `3a7f890b64d5`  |
| 2324   | Layout 2             | `3a7f890b64d5`  |
| 2319   | Layout 2             | `3a7f890b64d5`  |
| 2313   | Layout 2             | `3a7f890b64d5`  |
| 2308   | Layout 2             | `3a7f890b64d5`  |
| 2302   | Layout 2             | `3a7f890b64d5`  |
| 2295   | Layout 2             | `3a7f890b64d5`  |
| 2290   | Layout 2             | `3a7f890b64d5`  |
| 2284   | Layout 2             | `3a7f890b64d5`  |
| 2276   | Layout 2             | `3a7f890b64d5`  |
| 2269   | Layout 2             | `3a7f890b64d5`  |
| 2259   | Layout 2             | `3a7f890b64d5`  |
| 2250   | Layout 2             | `3a7f890b64d5`  |
| 2243   | Layout 2             | `3a7f890b64d5`  |
| 2235   | Layout 2             | `3a7f890b64d5`  |
| 2229   | Layout 2             | `3a7f890b64d5`  |
| 2224   | Layout 2             | `3a7f890b64d5`  |
| 2218   | Layout 2             | `3a7f890b64d5`  |
| 2215   | Layout 2             | `3a7f890b64d5`  |
| 2207   | Layout 2             | `3a7f890b64d5`  |
| 2203   | Layout 2             | `3a7f890b64d5`  |
| 2196   | Layout 2             | `3a7f890b64d5`  |
| 2192   | Layout 2             | `3a7f890b64d5`  |
| 2189   | Layout 2             | `3a7f890b64d5`  |
| 2183   | Layout 2             | `3a7f890b64d5`  |
| 2179   | Layout 2             | `3a7f890b64d5`  |
| 2171   | Layout 2             | `3a7f890b64d5`  |
| 2163   | Layout 2             | `3a7f890b64d5`  |
| 2156   | Layout 2             | `3a7f890b64d5`  |
| 2151   | Layout 2             | `3a7f890b64d5`  |
| 2147   | Layout 2             | `3a7f890b64d5`  |
| 2142   | Layout 2             | `3a7f890b64d5`  |
| 2138   | Layout 2             | `3a7f890b64d5`  |
| 2134   | Layout 2             | `3a7f890b64d5`  |
| 2130   | Layout 2             | `3a7f890b64d5`  |
| 2122   | Layout 2             | `3a7f890b64d5`  |
| 2107   | Layout 2             | `3a7f890b64d5`  |
| 2098   | Layout 2             | `3a7f890b64d5`  |
| 2089   | Layout 2             | `3a7f890b64d5`  |
| 2081   | Layout 2             | `3a7f890b64d5`  |
| 2073   | Layout 2             | `3a7f890b64d5`  |
| 2067   | Layout 2             | `3a7f890b64d5`  |
| 2063   | Layout 2             | `3a7f890b64d5`  |
| 2059   | Layout 2             | `3a7f890b64d5`  |
| 2052   | Layout 2             | `3a7f890b64d5`  |
| 2044   | Layout 2             | `3a7f890b64d5`  |
| 2039   | Layout 2             | `3a7f890b64d5`  |
| 2032   | Layout 2             | `3a7f890b64d5`  |
| 2025   | Layout 2             | `3a7f890b64d5`  |
| 2011   | Layout 2             | `3a7f890b64d5`  |
| 2005   | Layout 2             | `3a7f890b64d5`  |
| 2000   | Layout 2             | `3a7f890b64d5`  |
| 1996   | Layout 2             | `3a7f890b64d5`  |
| 1991   | Layout 2             | `3a7f890b64d5`  |
| 1985   | Layout 2             | `3a7f890b64d5`  |
| 1980   | Layout 2             | `3a7f890b64d5`  |
| 1969   | Layout 2             | `3a7f890b64d5`  |
| 1964   | Layout 2             | `3a7f890b64d5`  |
| 1958   | Layout 2             | `3a7f890b64d5`  |
| 1950   | Layout 2             | `3a7f890b64d5`  |
| 1945   | Layout 2             | `3a7f890b64d5`  |
| 1937   | Layout 2             | `3a7f890b64d5`  |
| 1933   | Layout 2             | `3a7f890b64d5`  |
| 1927   | Layout 2             | `3a7f890b64d5`  |
| 1921   | Layout 2             | `3a7f890b64d5`  |
| 1914   | Layout 2             | `3a7f890b64d5`  |
| 1908   | Layout 2             | `3a7f890b64d5`  |
| 1897   | Layout 2             | `3a7f890b64d5`  |
| 1892   | Layout 2             | `3a7f890b64d5`  |
| 1886   | Layout 2             | `3a7f890b64d5`  |
| 1881   | Layout 2             | `3a7f890b64d5`  |
| 1871   | Layout 2             | `3a7f890b64d5`  |
| 1866   | Layout 2             | `3a7f890b64d5`  |
| 1862   | Layout 2             | `3a7f890b64d5`  |
| 1854   | Layout 2             | `3a7f890b64d5`  |
| 1846   | Layout 2             | `3a7f890b64d5`  |
| 1838   | Layout 2             | `3a7f890b64d5`  |
| 1832   | Layout 2             | `3a7f890b64d5`  |
| 1826   | Layout 2             | `3a7f890b64d5`  |
| 1822   | Layout 2             | `3a7f890b64d5`  |
| 1818   | Layout 2             | `3a7f890b64d5`  |
| 1804   | Layout 2             | `3a7f890b64d5`  |
| 1794   | Layout 2             | `3a7f890b64d5`  |
| 1790   | Layout 2             | `3a7f890b64d5`  |
| 1784   | Layout 2             | `3a7f890b64d5`  |
| 1774   | Layout 2             | `3a7f890b64d5`  |
| 1771   | Layout 2             | `3a7f890b64d5`  |
| 1762   | Layout 2             | `3a7f890b64d5`  |
| 1759   | Layout 1             | `3a7f890b64d5`  |
| 1754   | Layout 1             | `3a7f890b64d5`  |
| 1749   | Layout 1             | `3a7f890b64d5`  |
| 1743   | Layout 1             | `3a7f890b64d5`  |
| 1737   | Layout 1             | `3a7f890b64d5`  |
| 1731   | Layout 1             | `3a7f890b64d5`  |
| 1725   | Layout 1             | `3a7f890b64d5`  |
| 1717   | Layout 1             | `3a7f890b64d5`  |
| 1710   | Layout 1             | `3a7f890b64d5`  |
| 1704   | Layout 1             | `3a7f890b64d5`  |
| 1698   | Layout 1             | `3a7f890b64d5`  |
| 1690   | Layout 1             | `3a7f890b64d5`  |
| 1685   | Layout 1             | `3a7f890b64d5`  |
| 1680   | Layout 1             | `3a7f890b64d5`  |
| 1674   | Layout 1             | `3a7f890b64d5`  |
| 1668   | Layout 1             | `3a7f890b64d5`  |
| 1659   | Layout 1             | `3a7f890b64d5`  |
| 1649   | Layout 1             | `3a7f890b64d5`  |
| 1642   | Layout 1             | `3a7f890b64d5`  |
| 1636   | Layout 1             | `3a7f890b64d5`  |
| 1628   | Layout 1             | `3a7f890b64d5`  |
| 1622   | Layout 1             | `3a7f890b64d5`  |
| 1614   | Layout 1             | `3a7f890b64d5`  |
| 1608   | Layout 1             | `3a7f890b64d5`  |
| 1602   | Layout 1             | `3a7f890b64d5`  |
| 1598   | Layout 1             | `3a7f890b64d5`  |
| 1594   | Layout 1             | `3a7f890b64d5`  |
| 1590   | Layout 1             | `3a7f890b64d5`  |
| 1587   | Layout 1             | `3a7f890b64d5`  |
| 1584   | Layout 1             | `3a7f890b64d5`  |
| 1579   | Layout 1             | `3a7f890b64d5`  |
| 1572   | Layout 1             | `3a7f890b64d5`  |
| 1565   | Layout 1             | `3a7f890b64d5`  |
| 1559   | Layout 1             | `3a7f890b64d5`  |
| 1554   | Layout 1             | `3a7f890b64d5`  |
| 1547   | Layout 1             | `3a7f890b64d5`  |
| 1537   | Layout 1             | `3a7f890b64d5`  |
| 1529   | Layout 1             | `3a7f890b64d5`  |
| 1524   | Layout 1             | `3a7f890b64d5`  |
| 1519   | Layout 1             | `3a7f890b64d5`  |
| 1509   | Layout 1             | `3a7f890b64d5`  |
| 1506   | Layout 1             | `3a7f890b64d5`  |
| 1504   | Layout 1             | `3a7f890b64d5`  |
| 1500   | Layout 1             | `3a7f890b64d5`  |
| 1493   | Layout 1             | `3a7f890b64d5`  |
| 1489   | Layout 1             | `3a7f890b64d5`  |
| 1485   | Layout 1             | `3a7f890b64d5`  |
| 1481   | Layout 1             | `3a7f890b64d5`  |
| 1474   | Layout 1             | `3a7f890b64d5`  |
| 1466   | Layout 1             | `3a7f890b64d5`  |
| 1462   | Layout 1             | `3a7f890b64d5`  |
| 1459   | Layout 1             | `3a7f890b64d5`  |
| 1453   | Layout 1             | `3a7f890b64d5`  |
| 1450   | Layout 1             | `3a7f890b64d5`  |
| 1445   | Layout 1             | `3a7f890b64d5`  |
| 1439   | Layout 1             | `3a7f890b64d5`  |
| 1433   | Layout 1             | `3a7f890b64d5`  |
| 1430   | Layout 1             | `3a7f890b64d5`  |
| 1426   | Layout 1             | `3a7f890b64d5`  |
| 1421   | Layout 1             | `3a7f890b64d5`  |
| 1417   | Layout 1             | `3a7f890b64d5`  |
| 1416   | Layout 1             | `3a7f890b64d5`  |
| 1409   | Layout 1             | `3a7f890b64d5`  |
| 1405   | Layout 1             | `3a7f890b64d5`  |
| 1401   | Layout 1             | `3a7f890b64d5`  |
| 1396   | Layout 1             | `3a7f890b64d5`  |
| 1391   | Layout 1             | `3a7f890b64d5`  |
| 1390   | Layout 1             | `3a7f890b64d5`  |
| 1386   | Layout 1             | `3a7f890b64d5`  |
| 1381   | Layout 1             | `3a7f890b64d5`  |
| 1379   | Layout 1             | `3a7f890b64d5`  |
| 1372   | Layout 1             | `3a7f890b64d5`  |
| 1366   | Layout 1             | `3a7f890b64d5`  |
| 1364   | Layout 1             | `3a7f890b64d5`  |
| 1363   | Layout 1             | `3a7f890b64d5`  |
| 1360   | Layout 1             | `3a7f890b64d5`  |
| 1358   | Layout 1             | `3a7f890b64d5`  |
| 1355   | Layout 1             | `3a7f890b64d5`  |
| 1351   | Layout 1             | `3a7f890b64d5`  |
| 1348   | Layout 1             | `3a7f890b64d5`  |
| 1346   | Layout 1             | `3a7f890b64d5`  |
| 1341   | Layout 1             | `3a7f890b64d5`  |
| 1340   | Layout 1             | `3a7f890b64d5`  |
| 1338   | Layout 1             | `3a7f890b64d5`  |
| 1335   | Layout 1             | `3a7f890b64d5`  |
| 1333   | Layout 1             | `3a7f890b64d5`  |
| 1329   | No documented layout | `3a7f890b64d5`  |
| 1327   | No documented layout | `3a7f890b64d5`  |
| 1324   | No documented layout | `3a7f890b64d5`  |
| 1321   | No documented layout | `3a7f890b64d5`  |
| 1319   | No documented layout | `3a7f890b64d5`  |
| 1318   | No documented layout | `3a7f890b64d5`  |
| 1316   | No documented layout | `3a7f890b64d5`  |
| 1313   | No documented layout | `3a7f890b64d5`  |
| 1311   | No documented layout | `3a7f890b64d5`  |
| 1309   | No documented layout | `3a7f890b64d5`  |
| 1304   | No documented layout | `3a7f890b64d5`  |
| 1292   | No documented layout | `3a7f890b64d5`  |
| 1286   | No documented layout | `3a7f890b64d5`  |
| 1280   | No documented layout | `3a7f890b64d5`  |
| 1276   | No documented layout | `3a7f890b64d5`  |
| 1267   | No documented layout | `3a7f890b64d5`  |
| 1261   | No file              | `3a7f890b64d5`  |
| 1256   | No file              | `3a7f890b64d5`  |
| 1250   | No file              | `3a7f890b64d5`  |
| 1246   | No file              | `3a7f890b64d5`  |
| 1239   | No file              | `3a7f890b64d5`  |
| 1230   | No file              | `3a7f890b64d5`  |
| 1226   | No file              | `3a7f890b64d5`  |
| 1220   | No file              | `3a7f890b64d5`  |
| 1217   | No file              | `3a7f890b64d5`  |
| 1211   | No file              | `3a7f890b64d5`  |
| 1210   | No file              | `3a7f890b64d5`  |
| 1208   | No file              | `3a7f890b64d5`  |
| 1203   | No file              | `3a7f890b64d5`  |
| 1197   | No file              | `3a7f890b64d5`  |
| 1194   | No file              | `3a7f890b64d5`  |
| 1192   | No file              | `3a7f890b64d5`  |
| 1187   | No file              | `3a7f890b64d5`  |
| 1183   | No file              | `3a7f890b64d5`  |
| 1177   | No file              | `3a7f890b64d5`  |
| 1173   | No file              | `3a7f890b64d5`  |
| 1167   | No file              | `3a7f890b64d5`  |
| 1164   | No file              | `3a7f890b64d5`  |
| 1156   | No file              | `3a7f890b64d5`  |
| 1149   | No file              | `3a7f890b64d5`  |
| 1144   | No file              | `3a7f890b64d5`  |
| 1137   | No file              | `3a7f890b64d5`  |
| 1132   | No file              | `3a7f890b64d5`  |
| 1127   | No file              | `3a7f890b64d5`  |
| 1122   | No file              | `3a7f890b64d5`  |
| 1118   | No file              | `3a7f890b64d5`  |
| 1114   | No file              | `3a7f890b64d5`  |
| 1109   | No file              | `3a7f890b64d5`  |
| 1102   | No file              | `3a7f890b64d5`  |
| 1096   | No file              | `3a7f890b64d5`  |
| 1088   | No file              | `3a7f890b64d5`  |
| 1081   | No file              | `3a7f890b64d5`  |
| 1076   | No file              | `3a7f890b64d5`  |
| 1069   | No file              | `3a7f890b64d5`  |
| 1064   | No file              | `3a7f890b64d5`  |
| 1058   | No file              | `3a7f890b64d5`  |
| 1051   | No file              | `3a7f890b64d5`  |
| 1044   | No file              | `3a7f890b64d5`  |
| 1036   | No file              | `3a7f890b64d5`  |
| 1026   | No file              | `3a7f890b64d5`  |
| 1016   | No file              | `3a7f890b64d5`  |
| 1009   | No file              | `3a7f890b64d5`  |
| 1005   | No file              | `3a7f890b64d5`  |
| 1000   | No file              | `3a7f890b64d5`  |
| 998    | No file              | `3a7f890b64d5`  |
| 990    | No file              | `3a7f890b64d5`  |
| 979    | No file              | `3a7f890b64d5`  |
| 972    | No file              | `3a7f890b64d5`  |
| 963    | No file              | `3a7f890b64d5`  |
| 955    | No file              | `3a7f890b64d5`  |
| 946    | No file              | `3a7f890b64d5`  |
| 938    | No file              | `3a7f890b64d5`  |
| 927    | No file              | `3a7f890b64d5`  |
| 911    | No file              | `3a7f890b64d5`  |
| 904    | No file              | `3a7f890b64d5`  |
| 899    | No file              | `3a7f890b64d5`  |
| 894    | No file              | `3a7f890b64d5`  |
| 885    | No file              | `3a7f890b64d5`  |
| 879    | No file              | `3a7f890b64d5`  |
| 872    | No file              | `3a7f890b64d5`  |
| 864    | No file              | `3a7f890b64d5`  |
| 855    | No file              | `3a7f890b64d5`  |
| 853    | No file              | `3a7f890b64d5`  |
| 845    | No file              | `3a7f890b64d5`  |
| 837    | No file              | `3a7f890b64d5`  |
| 829    | No file              | `3a7f890b64d5`  |
| 822    | No file              | `3a7f890b64d5`  |
| 814    | No file              | `3a7f890b64d5`  |
| 805    | No file              | `3a7f890b64d5`  |
| 794    | No file              | `3a7f890b64d5`  |
| 787    | No file              | `3a7f890b64d5`  |
| 780    | No file              | `3a7f890b64d5`  |
| 771    | No file              | `3a7f890b64d5`  |
| 760    | No file              | `3a7f890b64d5`  |
| 748    | No file              | `3a7f890b64d5`  |
| 741    | No file              | `3a7f890b64d5`  |
| 736    | No file              | `3a7f890b64d5`  |
| 731    | No file              | `3a7f890b64d5`  |
| 723    | No file              | `3a7f890b64d5`  |
| 711    | No file              | `3a7f890b64d5`  |
| 707    | No file              | `3a7f890b64d5`  |
| 697    | No file              | `3a7f890b64d5`  |
| 689    | No file              | `3a7f890b64d5`  |
| 683    | No file              | `3a7f890b64d5`  |
| 678    | No file              | `3a7f890b64d5`  |
| 670    | No file              | `3a7f890b64d5`  |
| 661    | No file              | `3a7f890b64d5`  |
| 656    | No file              | `3a7f890b64d5`  |
| 652    | No file              | `3a7f890b64d5`  |
| 643    | No file              | `3a7f890b64d5`  |
| 637    | No file              | `3a7f890b64d5`  |
| 630    | No file              | `3a7f890b64d5`  |
| 627    | No file              | `3a7f890b64d5`  |
| 621    | No file              | `3a7f890b64d5`  |
| 617    | No file              | `3a7f890b64d5`  |
| 615    | No file              | `3a7f890b64d5`  |
| 606    | No file              | `3a7f890b64d5`  |
| 599    | No file              | `3a7f890b64d5`  |
| 592    | No file              | `3a7f890b64d5`  |
| 586    | No file              | `3a7f890b64d5`  |
| 577    | No file              | `3a7f890b64d5`  |
| 569    | No file              | `3a7f890b64d5`  |
| 561    | No file              | `3a7f890b64d5`  |
| 554    | No file              | `3a7f890b64d5`  |
| 542    | No file              | `3a7f890b64d5`  |
| 532    | No file              | `3a7f890b64d5`  |
| 531    | No file              | `3a7f890b64d5`  |
| 526    | No file              | `3a7f890b64d5`  |
| 521    | No file              | `3a7f890b64d5`  |
| 517    | No file              | `3a7f890b64d5`  |
| 510    | No file              | `3a7f890b64d5`  |
| 508    | No file              | `3a7f890b64d5`  |
| 504    | No file              | `3a7f890b64d5`  |
| 497    | No file              | `3a7f890b64d5`  |
| 491    | No file              | `3a7f890b64d5`  |
| 485    | No file              | `3a7f890b64d5`  |
| 478    | No file              | `3a7f890b64d5`  |
| 472    | No file              | `3a7f890b64d5`  |
| 466    | No file              | `3a7f890b64d5`  |
| 457    | No file              | `3a7f890b64d5`  |
| 452    | No file              | `3a7f890b64d5`  |
| 449    | No file              | `3a7f890b64d5`  |
| 435    | No file              | `3a7f890b64d5`  |

<!-- versions:end -->

## Companion Files

The handler reads no companion file. Names come from LOC type `6` and icons
from the character icon index, both keyed by `character_id`.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 156 bytes + hull layers)

| Offset        | Type                    | Field             | Notes                                                                 |
| ------------- | ----------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`       | u16                     | character_id      | Object character; unique, rows not sorted                             |
| `+0x02`       | u8                      | armor_material    | `100` on houses and furniture, `4`, `6`, `7` or `0` on the other kinds; see Notes |
| `+0x03`       | u8                      | object_kind       | Same value as `object_kind` in `characterobject.dbss`; see [Object Kinds](../dbss/characterobject_dbss.md#object-kinds) |
| `+0x04`       | u8                      | installation_type | `CppEnums.InstallationType`; see [Installation Types](#installation-types) |
| `+0x05`       | f32[4][4]               | unknown_05        | Identity matrix except on houses; see House Matrices                  |
| `+0x45`       | f32[4][4]               | unknown_45        | Identity matrix except on houses; see House Matrices                  |
| `+0x85`       | i32                     | unknown_85        | `-1` except on houses; see House Matrices                             |
| `+0x89`       | u8                      | is_collision      | `0` or `1`                                                            |
| `+0x8A`       | u8                      | is_siege_tent     | `1` on 45 rows, all of kinds `4`, `6` and `8` (King, Lord and Village tents), else `0` |
| `+0x8B`       | u8                      | unknown_8b        | `1` on siege buildings, else `0`; same value as `unknown_04` in `characterobject.dbss` |
| `+0x8C`       | u32                     | layer_count       | Hull layers that follow; `0` to `4`                                   |
| `+0x90`       | u32                     | unknown_90        | Always equal to `layer_count`                                         |
| `+0x94`       | Hull Layer[layer_count] | layers            | See Hull Layer                                                        |
| `layers+0x00` | u16                     | unknown_layers_00 | The row's own `character_id` on 25 maid rows, else `0`; see Open Questions |
| `layers+0x02` | u8                      | is_inside         | Place flag: can be placed inside a house                              |
| `layers+0x03` | u8                      | is_outside        | Place flag: can be placed outside                                     |
| `layers+0x04` | u8                      | is_floor          | Place flag                                                            |
| `layers+0x05` | u8                      | is_wall           | Place flag                                                            |
| `layers+0x06` | u8                      | is_on_the_table   | Place flag                                                            |
| `layers+0x07` | u8                      | is_carpet         | Place flag                                                            |

The six place flags hold the same values as `is_inside` to `is_carpet` in
the `characterobject.dbss` Furniture Block, on all 3,971 furniture rows of
client 3483. `is_siege_tent` and `unknown_8b` hold the same values as
`characterobject.dbss` `+0x03` and `+0x04` on all 5,131 rows.

### Hull Layer (variable: 4 bytes + hulls)

| Offset  | Type             | Field      | Notes                            |
| ------- | ---------------- | ---------- | -------------------------------- |
| `+0x00` | u32              | hull_count | Hulls in this layer; `1` to `17` |
| `+0x04` | Hull[hull_count] | hulls      | See Hull                         |

### Hull (variable: 4 bytes + faces)

| Offset  | Type             | Field      | Notes              |
| ------- | ---------------- | ---------- | ------------------ |
| `+0x00` | u32              | face_count | Faces in this hull |
| `+0x04` | Face[face_count] | faces      | See Face           |

### Face (140 bytes)

One bounding plane of a convex hull.

| Offset  | Type      | Field      | Notes                                                     |
| ------- | --------- | ---------- | --------------------------------------------------------- |
| `+0x00` | f32       | distance   | Plane distance: `-(normal . origin)` on every face        |
| `+0x04` | f32[3]    | normal     | Unit normal (x, y, z) of the plane                        |
| `+0x10` | f32[3]    | origin     | A point on the plane                                      |
| `+0x1C` | f32[9][3] | points     | Nine points (x, y, z), all on the plane; the first equals `origin` |
| `+0x88` | i32       | unknown_88 | `0` on every face                                         |

On client 3483 all 28,202 faces have a unit `normal`, a `distance` equal to
`-(normal . origin)` and nine `points` that satisfy the plane equation. The
2016 `pa::PlaneExtended` holds `_distance`, `_normal`, `_origin`, a
three-point `_pointList` and `_negNormBitMask` in that order, 68 bytes; the
current face stores nine points.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                  |
| ------- | ------------------ | ------------ | ---------------------- |
| `+0x00` | u32                | string_count | `0`                    |
| `+0x04` | pstr[string_count] | strings      | Empty; no field points here |

## Layout 1

The row has no `unknown_8b` yet, so it is one byte shorter. Field names
keep Layout 2's offsets. The files of clients 1267 to 1329 fit neither
layout.

### Row (variable: 155 bytes + hull layers)

| Offset        | Type                    | Field             | Notes |
| ------------- | ----------------------- | ----------------- | ----- |
| `+0x00`       | u16                     | character_id      |       |
| `+0x02`       | u8                      | armor_material    |       |
| `+0x03`       | u8                      | object_kind       |       |
| `+0x04`       | u8                      | installation_type |       |
| `+0x05`       | f32[4][4]               | unknown_05        |       |
| `+0x45`       | f32[4][4]               | unknown_45        |       |
| `+0x85`       | i32                     | unknown_85        |       |
| `+0x89`       | u8                      | is_collision      | Same value as on client 1784 on all 3,461 rows client 1759 shares with it |
| `+0x8A`       | u8                      | is_siege_tent     | Same check, 3,461 of 3,461 |
| `+0x8B`       | u32                     | layer_count       |       |
| `+0x8F`       | u32                     | unknown_90        |       |
| `+0x93`       | Hull Layer[layer_count] | layers            |       |
| `layers+0x00` | u16                     | unknown_layers_00 |       |
| `layers+0x02` | u8                      | is_inside         |       |
| `layers+0x03` | u8                      | is_outside        |       |
| `layers+0x04` | u8                      | is_floor          |       |
| `layers+0x05` | u8                      | is_wall           |       |
| `layers+0x06` | u8                      | is_on_the_table   |       |
| `layers+0x07` | u8                      | is_carpet         |       |

## Installation Types

`CppEnums.InstallationType` in `global_define_cpp_enum.luac` (client 3482)
names the values `0` Default to `39` EventPersonalTent. Rows per value on
client 3483:

| Value | Enum name     | Rows  | Value | Enum name          | Rows |
| ----- | ------------- | ----- | ----- | ------------------ | ---- |
| 0     | Default       | 2,648 | 21    | Alchemy            | 13   |
| 1     | Carpenter     | 78    | 22    | JukeBox            | 58   |
| 2     | Alchemy1      | 72    | 23    | Pet                | 1    |
| 3     | Founding      | 74    | 24    | WallPaper          | 95   |
| 4     | Cooking       | 12    | 25    | FloorMaterial      | 89   |
| 5     | Forging       | 85    | 26    | Chandelier         | 88   |
| 6     | Treasure      | 102   | 27    | Curtain            | 20   |
| 7     | Smithing      | 97    | 28    | Scarecrow          | 1    |
| 8     | Weaving       | 75    | 29    | Waterway           | 1    |
| 9     | Bed           | 73    | 30    | Maid               | 27   |
| 10    | Havest        | 375   | 31    | Curtain_Tied       | 16   |
| 11    | Mortar        | 1     | 32    | LivestockHarvest   | 11   |
| 12    | Anvil         | 1     | 33    | FirePlace          | 3    |
| 13    | Stump         | 1     | 34    | InstanceWater      | 5    |
| 14    | FireBowl      | 1     | 35    | Shelf              | 9    |
| 17    | Buff          | 635   | 36    | Bath               | 3    |
| 19    | Bookcase      | 115   | 38    | MansionTree        | 243  |
| 20    | WarehouseBox  | 2     | 39    | EventPersonalTent  | 1    |

Values `15`, `16` and `18` (`Reserve_15`, `Reserve_16`, `Reserve_18`) and
`37` (`FurnitureWarehouse`) hold no row.

## House Matrices

`unknown_05`, `unknown_45` and `unknown_85` are set on the same 865 rows of
client 3483, the house kinds `5` (815), `1` (25), `9` (17) and `36` (8):
the rows whose `characterobject.dbss` record ends in a House Tail. On the
other 4,266 rows both matrices are the identity and `unknown_85` is `-1`.

On a house row both matrices are a rotation about the y axis with a
translation in world coordinates in the fourth row (Morning Light Nampo 1,
character 3823: x `-1290587`, y `-7794`, z `1135967`). The two share the
rotation; their translations are up to 4,539 units apart.
`unknown_85` holds 865 different values from `0` to `871`, one per house;
the houses of one town are numbered in a run (Morning Light Nampo 1 to 4 are
`0` to `3`, Arehaza 1-1 to 2-2 `868` to `871`). No `houseinfo.bss` field
holds the same number.

## Field Names

The `Object_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 shares 3,497 character IDs with client 3483:

| Field             | `Object_Table` column | Matching rows    |
| ----------------- | --------------------- | ---------------- |
| armor_material    | `ArmorMaterial`       | 156 of 157 set cells; `100` in all 3,332 empty ones |
| object_kind       | `ObjectKind`          | 3,497 of 3,497   |
| installation_type | `InstallationType`    | 3,497 of 3,497   |
| is_collision      | `IsCollision`         | 3,497 of 3,497   |
| is_inside         | `IsInside`            | 3,497 of 3,497   |
| is_outside        | `IsOutside`           | 3,497 of 3,497   |
| is_floor          | `IsFloor`             | 3,492 of 3,497   |
| is_wall           | `IsWall`              | 3,497 of 3,497   |
| is_on_the_table   | `IsOnTheTable`        | 3,275 of 3,497   |
| is_carpet         | `IsCarpet`            | 3,497 of 3,497   |

The other nine match on every shared row of the client 1784
`baseobject.bss` (3,480 rows) and of the `baseobject.bss` the private
server compiled from the same sheets (3,523 rows), so the misses on client
3483 are values changed since. `ArmorMaterial` is empty on most rows; the
compiled file holds `100` for every empty cell and the cell's value for
the other 160. The one miss on client 3483 is Field Command Post (2097):
`7` in the sheet, `6` in the client. On 8 house rows (2111 to 2113, 2229,
2230, 2411 to 2413) the `ArmorMaterial` cell reads as description text;
they are left out of the counts. `is_siege_tent` has no column; it keeps the name
`characterobject.dbss` gives the same byte. `layer_count`, the hulls and the
faces follow the `characterobject.dbss` Structure Body names. The 2016
`gc::ObjectStaticStatus` holds `_isCollision`, then `_numberFloor` and
`_floorBound`, a list of lists of `pa::Convex` (each a list of
`pa::PlaneExtended`): the same nesting as layers, hulls and faces.

## Notes

- `character_id` is the low u16 of what looks like a u32 key; the high half
  is `armor_material` and `object_kind`. The rows keep no key order.
- The character IDs are the same set as the `characterobject.dbss` keys:
  5,131 on client 3483, with no ID in only one of the two files.
- Furniture rows (kind `2`) have no hull layers. On client 3483, 940 rows
  have layers: `layer_count` is `1` in 820 rows, `2` in 102, `3` in 17 and
  `4` in 1. 2,267 of the 2,321 hulls have 12 faces. The 1,079 layers,
  2,321 hulls and 28,202 faces equal the hull counts of the
  `characterobject.dbss` Structure Body on the same client.
- `armor_material` on client 3483 is `100` on 4,815 rows of kinds `1`,
  `2`, `5`, `9` and `36`, and `0` on 21 rows of kinds `2` and `5`; the
  other kinds (siege objects, tents, traps) hold `4`, `6` or `7`. It holds
  the same value as `characterobject.dbss` `armor_material` on every
  furniture row, the byte at the place of `_armorMaterial` in the 2016
  order.

## Open Questions

### Unknown Row Bytes

`unknown_layers_00` is the row's own `character_id` on 25 of the 27
installation type `30` (Maid) rows, the maid dolls 18951 to 18977, and `0`
everywhere else. The other two, 18972 and 18973, also have a `maid.dbss`
row but no English LOC name. The 2016 struct has a `_maidStaticStatus`
pointer; the `Install_Maid` column of the client 1784 sheet is a `0`/`1`
flag on 556 rows and does not match. `unknown_88` of every face is `0`,
where the 2016 plane has `_negNormBitMask`.

### House Matrix Fields

The 2016 `gc::ObjectStaticStatus` holds `_matParentWorldTM` and
`_matChildWorldTM`, which fit `unknown_05` and `unknown_45` (see House
Matrices), but no value source confirms which is which or what the second
transform places. What the house number `unknown_85` indexes is also open.
