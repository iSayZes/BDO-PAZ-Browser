# `baseobject.bss` Format

## Purpose

One row per placeable world object (furniture, crops, houses, tents,
barricades and siege buildings), keyed by the object's character ID: its
armor material, object kind, installation type, collision and siege tent
flags, the six
placement flags, the two world transforms and `hosueholdall.xml` index of
a house, and the house hull: floor layers of convex hulls, each hull a
list of planes. It
holds the numeric part of the 2016 `gc::ObjectStaticStatus`; the model
paths, icons and Korean house text of the same objects are in
[`characterobject.dbss`](../dbss/characterobject_dbss.md), which has a record for
every character ID here.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes     | Records                                              | Row bytes |
| ------ | -------------- | ---------------- | --------- | ---------------------------------------------------- | --------- |
| 4      | 1762 and later | `baseobject.bss` | 4,762,336 | 5,131 Row, 28,202 Face, 2,321 Hull, 1,079 Hull Layer | 140       |
| 3      | 1333 to 1759   | `baseobject.bss` | 4,060,119 | 3,461 Row, 25,082 Face, 2,063 Hull, 978 Hull Layer   | 140       |
| 2      | 1316 to 1329   | `baseobject.bss` | 3,898,475 | 2,983 Row, 24,586 Face, 2,021 Hull, 966 Hull Layer   | 140       |
| 1      | 1267 to 1313   | `baseobject.bss` | 403,815   | 2,905 Row                                            | 139       |

| Layout | File             | Known               | Unknown          |
| ------ | ---------------- | ------------------- | ---------------- |
| 4      | `baseobject.bss` | 4,613,611 B (96.9%) | 148,725 B (3.1%) |
| 3      | `baseobject.bss` | 3,939,025 B (97.0%) | 121,094 B (3.0%) |
| 2      | `baseobject.bss` | 3,782,233 B (97.0%) | 116,242 B (3.0%) |
| 1      | `baseobject.bss` | 403,815 B (100.0%)  | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `11f53e6cc58d`  |
| 3482   | Layout 4 | `11f53e6cc58d`  |
| 3474   | Layout 4 | `11f53e6cc58d`  |
| 3473   | Layout 4 | `11f53e6cc58d`  |
| 3464   | Layout 4 | `11f53e6cc58d`  |
| 3458   | Layout 4 | `11f53e6cc58d`  |
| 3454   | Layout 4 | `11f53e6cc58d`  |
| 3444   | Layout 4 | `11f53e6cc58d`  |
| 3435   | Layout 4 | `11f53e6cc58d`  |
| 3426   | Layout 4 | `11f53e6cc58d`  |
| 3418   | Layout 4 | `11f53e6cc58d`  |
| 3412   | Layout 4 | `11f53e6cc58d`  |
| 3402   | Layout 4 | `11f53e6cc58d`  |
| 3396   | Layout 4 | `11f53e6cc58d`  |
| 3387   | Layout 4 | `11f53e6cc58d`  |
| 3381   | Layout 4 | `11f53e6cc58d`  |
| 3373   | Layout 4 | `11f53e6cc58d`  |
| 3364   | Layout 4 | `11f53e6cc58d`  |
| 3356   | Layout 4 | `11f53e6cc58d`  |
| 3349   | Layout 4 | `11f53e6cc58d`  |
| 3342   | Layout 4 | `11f53e6cc58d`  |
| 3335   | Layout 4 | `11f53e6cc58d`  |
| 3326   | Layout 4 | `11f53e6cc58d`  |
| 3321   | Layout 4 | `11f53e6cc58d`  |
| 3314   | Layout 4 | `11f53e6cc58d`  |
| 3303   | Layout 4 | `11f53e6cc58d`  |
| 3302   | Layout 4 | `11f53e6cc58d`  |
| 3293   | Layout 4 | `11f53e6cc58d`  |
| 3283   | Layout 4 | `11f53e6cc58d`  |
| 3275   | Layout 4 | `11f53e6cc58d`  |
| 3267   | Layout 4 | `11f53e6cc58d`  |
| 3258   | Layout 4 | `11f53e6cc58d`  |
| 3251   | Layout 4 | `11f53e6cc58d`  |
| 3242   | Layout 4 | `11f53e6cc58d`  |
| 3235   | Layout 4 | `11f53e6cc58d`  |
| 3229   | Layout 4 | `11f53e6cc58d`  |
| 3212   | Layout 4 | `11f53e6cc58d`  |
| 3203   | Layout 4 | `11f53e6cc58d`  |
| 3193   | Layout 4 | `11f53e6cc58d`  |
| 3186   | Layout 4 | `11f53e6cc58d`  |
| 3177   | Layout 4 | `11f53e6cc58d`  |
| 3169   | Layout 4 | `11f53e6cc58d`  |
| 3158   | Layout 4 | `11f53e6cc58d`  |
| 3151   | Layout 4 | `11f53e6cc58d`  |
| 3144   | Layout 4 | `11f53e6cc58d`  |
| 3133   | Layout 4 | `11f53e6cc58d`  |
| 3125   | Layout 4 | `11f53e6cc58d`  |
| 3118   | Layout 4 | `11f53e6cc58d`  |
| 3111   | Layout 4 | `11f53e6cc58d`  |
| 3103   | Layout 4 | `11f53e6cc58d`  |
| 3095   | Layout 4 | `11f53e6cc58d`  |
| 3086   | Layout 4 | `11f53e6cc58d`  |
| 3072   | Layout 4 | `11f53e6cc58d`  |
| 3062   | Layout 4 | `11f53e6cc58d`  |
| 3052   | Layout 4 | `11f53e6cc58d`  |
| 3045   | Layout 4 | `11f53e6cc58d`  |
| 3037   | Layout 4 | `11f53e6cc58d`  |
| 3030   | Layout 4 | `11f53e6cc58d`  |
| 3021   | Layout 4 | `11f53e6cc58d`  |
| 3012   | Layout 4 | `11f53e6cc58d`  |
| 3002   | Layout 4 | `11f53e6cc58d`  |
| 2995   | Layout 4 | `11f53e6cc58d`  |
| 2987   | Layout 4 | `11f53e6cc58d`  |
| 2978   | Layout 4 | `11f53e6cc58d`  |
| 2970   | Layout 4 | `11f53e6cc58d`  |
| 2959   | Layout 4 | `11f53e6cc58d`  |
| 2951   | Layout 4 | `11f53e6cc58d`  |
| 2942   | Layout 4 | `11f53e6cc58d`  |
| 2935   | Layout 4 | `11f53e6cc58d`  |
| 2932   | Layout 4 | `11f53e6cc58d`  |
| 2923   | Layout 4 | `11f53e6cc58d`  |
| 2919   | Layout 4 | `11f53e6cc58d`  |
| 2907   | Layout 4 | `11f53e6cc58d`  |
| 2900   | Layout 4 | `11f53e6cc58d`  |
| 2891   | Layout 4 | `11f53e6cc58d`  |
| 2882   | Layout 4 | `11f53e6cc58d`  |
| 2872   | Layout 4 | `11f53e6cc58d`  |
| 2863   | Layout 4 | `11f53e6cc58d`  |
| 2855   | Layout 4 | `11f53e6cc58d`  |
| 2849   | Layout 4 | `11f53e6cc58d`  |
| 2844   | Layout 4 | `11f53e6cc58d`  |
| 2834   | Layout 4 | `11f53e6cc58d`  |
| 2825   | Layout 4 | `11f53e6cc58d`  |
| 2819   | Layout 4 | `11f53e6cc58d`  |
| 2811   | Layout 4 | `11f53e6cc58d`  |
| 2803   | Layout 4 | `11f53e6cc58d`  |
| 2794   | Layout 4 | `11f53e6cc58d`  |
| 2783   | Layout 4 | `11f53e6cc58d`  |
| 2774   | Layout 4 | `11f53e6cc58d`  |
| 2765   | Layout 4 | `11f53e6cc58d`  |
| 2756   | Layout 4 | `11f53e6cc58d`  |
| 2750   | Layout 4 | `11f53e6cc58d`  |
| 2743   | Layout 4 | `11f53e6cc58d`  |
| 2736   | Layout 4 | `11f53e6cc58d`  |
| 2726   | Layout 4 | `11f53e6cc58d`  |
| 2717   | Layout 4 | `11f53e6cc58d`  |
| 2709   | Layout 4 | `11f53e6cc58d`  |
| 2703   | Layout 4 | `11f53e6cc58d`  |
| 2695   | Layout 4 | `11f53e6cc58d`  |
| 2684   | Layout 4 | `11f53e6cc58d`  |
| 2672   | Layout 4 | `11f53e6cc58d`  |
| 2665   | Layout 4 | `11f53e6cc58d`  |
| 2657   | Layout 4 | `11f53e6cc58d`  |
| 2649   | Layout 4 | `11f53e6cc58d`  |
| 2644   | Layout 4 | `11f53e6cc58d`  |
| 2637   | Layout 4 | `11f53e6cc58d`  |
| 2629   | Layout 4 | `11f53e6cc58d`  |
| 2619   | Layout 4 | `11f53e6cc58d`  |
| 2612   | Layout 4 | `11f53e6cc58d`  |
| 2606   | Layout 4 | `11f53e6cc58d`  |
| 2602   | Layout 4 | `11f53e6cc58d`  |
| 2601   | Layout 4 | `11f53e6cc58d`  |
| 2592   | Layout 4 | `11f53e6cc58d`  |
| 2583   | Layout 4 | `11f53e6cc58d`  |
| 2575   | Layout 4 | `11f53e6cc58d`  |
| 2567   | Layout 4 | `11f53e6cc58d`  |
| 2560   | Layout 4 | `11f53e6cc58d`  |
| 2553   | Layout 4 | `11f53e6cc58d`  |
| 2545   | Layout 4 | `11f53e6cc58d`  |
| 2538   | Layout 4 | `11f53e6cc58d`  |
| 2529   | Layout 4 | `11f53e6cc58d`  |
| 2519   | Layout 4 | `11f53e6cc58d`  |
| 2513   | Layout 4 | `11f53e6cc58d`  |
| 2510   | Layout 4 | `11f53e6cc58d`  |
| 2507   | Layout 4 | `11f53e6cc58d`  |
| 2503   | Layout 4 | `11f53e6cc58d`  |
| 2498   | Layout 4 | `11f53e6cc58d`  |
| 2492   | Layout 4 | `11f53e6cc58d`  |
| 2487   | Layout 4 | `11f53e6cc58d`  |
| 2480   | Layout 4 | `11f53e6cc58d`  |
| 2474   | Layout 4 | `11f53e6cc58d`  |
| 2468   | Layout 4 | `11f53e6cc58d`  |
| 2460   | Layout 4 | `11f53e6cc58d`  |
| 2453   | Layout 4 | `11f53e6cc58d`  |
| 2444   | Layout 4 | `11f53e6cc58d`  |
| 2438   | Layout 4 | `11f53e6cc58d`  |
| 2434   | Layout 4 | `11f53e6cc58d`  |
| 2429   | Layout 4 | `11f53e6cc58d`  |
| 2421   | Layout 4 | `11f53e6cc58d`  |
| 2414   | Layout 4 | `11f53e6cc58d`  |
| 2407   | Layout 4 | `11f53e6cc58d`  |
| 2401   | Layout 4 | `11f53e6cc58d`  |
| 2397   | Layout 4 | `11f53e6cc58d`  |
| 2393   | Layout 4 | `11f53e6cc58d`  |
| 2384   | Layout 4 | `11f53e6cc58d`  |
| 2378   | Layout 4 | `11f53e6cc58d`  |
| 2372   | Layout 4 | `11f53e6cc58d`  |
| 2358   | Layout 4 | `11f53e6cc58d`  |
| 2352   | Layout 4 | `11f53e6cc58d`  |
| 2347   | Layout 4 | `11f53e6cc58d`  |
| 2343   | Layout 4 | `11f53e6cc58d`  |
| 2335   | Layout 4 | `11f53e6cc58d`  |
| 2327   | Layout 4 | `11f53e6cc58d`  |
| 2324   | Layout 4 | `11f53e6cc58d`  |
| 2319   | Layout 4 | `11f53e6cc58d`  |
| 2313   | Layout 4 | `11f53e6cc58d`  |
| 2308   | Layout 4 | `11f53e6cc58d`  |
| 2302   | Layout 4 | `11f53e6cc58d`  |
| 2295   | Layout 4 | `11f53e6cc58d`  |
| 2290   | Layout 4 | `11f53e6cc58d`  |
| 2284   | Layout 4 | `11f53e6cc58d`  |
| 2276   | Layout 4 | `11f53e6cc58d`  |
| 2269   | Layout 4 | `11f53e6cc58d`  |
| 2259   | Layout 4 | `11f53e6cc58d`  |
| 2250   | Layout 4 | `11f53e6cc58d`  |
| 2243   | Layout 4 | `11f53e6cc58d`  |
| 2235   | Layout 4 | `11f53e6cc58d`  |
| 2229   | Layout 4 | `11f53e6cc58d`  |
| 2224   | Layout 4 | `11f53e6cc58d`  |
| 2218   | Layout 4 | `11f53e6cc58d`  |
| 2215   | Layout 4 | `11f53e6cc58d`  |
| 2207   | Layout 4 | `11f53e6cc58d`  |
| 2203   | Layout 4 | `11f53e6cc58d`  |
| 2196   | Layout 4 | `11f53e6cc58d`  |
| 2192   | Layout 4 | `11f53e6cc58d`  |
| 2189   | Layout 4 | `11f53e6cc58d`  |
| 2183   | Layout 4 | `11f53e6cc58d`  |
| 2179   | Layout 4 | `11f53e6cc58d`  |
| 2171   | Layout 4 | `11f53e6cc58d`  |
| 2163   | Layout 4 | `11f53e6cc58d`  |
| 2156   | Layout 4 | `11f53e6cc58d`  |
| 2151   | Layout 4 | `11f53e6cc58d`  |
| 2147   | Layout 4 | `11f53e6cc58d`  |
| 2142   | Layout 4 | `11f53e6cc58d`  |
| 2138   | Layout 4 | `11f53e6cc58d`  |
| 2134   | Layout 4 | `11f53e6cc58d`  |
| 2130   | Layout 4 | `11f53e6cc58d`  |
| 2122   | Layout 4 | `11f53e6cc58d`  |
| 2107   | Layout 4 | `11f53e6cc58d`  |
| 2098   | Layout 4 | `11f53e6cc58d`  |
| 2089   | Layout 4 | `11f53e6cc58d`  |
| 2081   | Layout 4 | `11f53e6cc58d`  |
| 2073   | Layout 4 | `11f53e6cc58d`  |
| 2067   | Layout 4 | `11f53e6cc58d`  |
| 2063   | Layout 4 | `11f53e6cc58d`  |
| 2059   | Layout 4 | `11f53e6cc58d`  |
| 2052   | Layout 4 | `11f53e6cc58d`  |
| 2044   | Layout 4 | `11f53e6cc58d`  |
| 2039   | Layout 4 | `11f53e6cc58d`  |
| 2032   | Layout 4 | `11f53e6cc58d`  |
| 2025   | Layout 4 | `11f53e6cc58d`  |
| 2011   | Layout 4 | `11f53e6cc58d`  |
| 2005   | Layout 4 | `11f53e6cc58d`  |
| 2000   | Layout 4 | `11f53e6cc58d`  |
| 1996   | Layout 4 | `11f53e6cc58d`  |
| 1991   | Layout 4 | `11f53e6cc58d`  |
| 1985   | Layout 4 | `11f53e6cc58d`  |
| 1980   | Layout 4 | `11f53e6cc58d`  |
| 1969   | Layout 4 | `11f53e6cc58d`  |
| 1964   | Layout 4 | `11f53e6cc58d`  |
| 1958   | Layout 4 | `11f53e6cc58d`  |
| 1950   | Layout 4 | `11f53e6cc58d`  |
| 1945   | Layout 4 | `11f53e6cc58d`  |
| 1937   | Layout 4 | `11f53e6cc58d`  |
| 1933   | Layout 4 | `11f53e6cc58d`  |
| 1927   | Layout 4 | `11f53e6cc58d`  |
| 1921   | Layout 4 | `11f53e6cc58d`  |
| 1914   | Layout 4 | `11f53e6cc58d`  |
| 1908   | Layout 4 | `11f53e6cc58d`  |
| 1897   | Layout 4 | `11f53e6cc58d`  |
| 1892   | Layout 4 | `11f53e6cc58d`  |
| 1886   | Layout 4 | `11f53e6cc58d`  |
| 1881   | Layout 4 | `11f53e6cc58d`  |
| 1871   | Layout 4 | `11f53e6cc58d`  |
| 1866   | Layout 4 | `11f53e6cc58d`  |
| 1862   | Layout 4 | `11f53e6cc58d`  |
| 1854   | Layout 4 | `11f53e6cc58d`  |
| 1846   | Layout 4 | `11f53e6cc58d`  |
| 1838   | Layout 4 | `11f53e6cc58d`  |
| 1832   | Layout 4 | `11f53e6cc58d`  |
| 1826   | Layout 4 | `11f53e6cc58d`  |
| 1822   | Layout 4 | `11f53e6cc58d`  |
| 1818   | Layout 4 | `11f53e6cc58d`  |
| 1804   | Layout 4 | `11f53e6cc58d`  |
| 1794   | Layout 4 | `11f53e6cc58d`  |
| 1790   | Layout 4 | `11f53e6cc58d`  |
| 1784   | Layout 4 | `11f53e6cc58d`  |
| 1774   | Layout 4 | `11f53e6cc58d`  |
| 1771   | Layout 4 | `11f53e6cc58d`  |
| 1762   | Layout 4 | `11f53e6cc58d`  |
| 1759   | Layout 3 | `11f53e6cc58d`  |
| 1754   | Layout 3 | `11f53e6cc58d`  |
| 1749   | Layout 3 | `11f53e6cc58d`  |
| 1743   | Layout 3 | `11f53e6cc58d`  |
| 1737   | Layout 3 | `11f53e6cc58d`  |
| 1731   | Layout 3 | `11f53e6cc58d`  |
| 1725   | Layout 3 | `11f53e6cc58d`  |
| 1717   | Layout 3 | `11f53e6cc58d`  |
| 1710   | Layout 3 | `11f53e6cc58d`  |
| 1704   | Layout 3 | `11f53e6cc58d`  |
| 1698   | Layout 3 | `11f53e6cc58d`  |
| 1690   | Layout 3 | `11f53e6cc58d`  |
| 1685   | Layout 3 | `11f53e6cc58d`  |
| 1680   | Layout 3 | `11f53e6cc58d`  |
| 1674   | Layout 3 | `11f53e6cc58d`  |
| 1668   | Layout 3 | `11f53e6cc58d`  |
| 1659   | Layout 3 | `11f53e6cc58d`  |
| 1649   | Layout 3 | `11f53e6cc58d`  |
| 1642   | Layout 3 | `11f53e6cc58d`  |
| 1636   | Layout 3 | `11f53e6cc58d`  |
| 1628   | Layout 3 | `11f53e6cc58d`  |
| 1622   | Layout 3 | `11f53e6cc58d`  |
| 1614   | Layout 3 | `11f53e6cc58d`  |
| 1608   | Layout 3 | `11f53e6cc58d`  |
| 1602   | Layout 3 | `11f53e6cc58d`  |
| 1598   | Layout 3 | `11f53e6cc58d`  |
| 1594   | Layout 3 | `11f53e6cc58d`  |
| 1590   | Layout 3 | `11f53e6cc58d`  |
| 1587   | Layout 3 | `11f53e6cc58d`  |
| 1584   | Layout 3 | `11f53e6cc58d`  |
| 1579   | Layout 3 | `11f53e6cc58d`  |
| 1572   | Layout 3 | `11f53e6cc58d`  |
| 1565   | Layout 3 | `11f53e6cc58d`  |
| 1559   | Layout 3 | `11f53e6cc58d`  |
| 1554   | Layout 3 | `11f53e6cc58d`  |
| 1547   | Layout 3 | `11f53e6cc58d`  |
| 1537   | Layout 3 | `11f53e6cc58d`  |
| 1529   | Layout 3 | `11f53e6cc58d`  |
| 1524   | Layout 3 | `11f53e6cc58d`  |
| 1519   | Layout 3 | `11f53e6cc58d`  |
| 1509   | Layout 3 | `11f53e6cc58d`  |
| 1506   | Layout 3 | `11f53e6cc58d`  |
| 1504   | Layout 3 | `11f53e6cc58d`  |
| 1500   | Layout 3 | `11f53e6cc58d`  |
| 1493   | Layout 3 | `11f53e6cc58d`  |
| 1489   | Layout 3 | `11f53e6cc58d`  |
| 1485   | Layout 3 | `11f53e6cc58d`  |
| 1481   | Layout 3 | `11f53e6cc58d`  |
| 1474   | Layout 3 | `11f53e6cc58d`  |
| 1466   | Layout 3 | `11f53e6cc58d`  |
| 1462   | Layout 3 | `11f53e6cc58d`  |
| 1459   | Layout 3 | `11f53e6cc58d`  |
| 1453   | Layout 3 | `11f53e6cc58d`  |
| 1450   | Layout 3 | `11f53e6cc58d`  |
| 1445   | Layout 3 | `11f53e6cc58d`  |
| 1439   | Layout 3 | `11f53e6cc58d`  |
| 1433   | Layout 3 | `11f53e6cc58d`  |
| 1430   | Layout 3 | `11f53e6cc58d`  |
| 1426   | Layout 3 | `11f53e6cc58d`  |
| 1421   | Layout 3 | `11f53e6cc58d`  |
| 1417   | Layout 3 | `11f53e6cc58d`  |
| 1416   | Layout 3 | `11f53e6cc58d`  |
| 1409   | Layout 3 | `11f53e6cc58d`  |
| 1405   | Layout 3 | `11f53e6cc58d`  |
| 1401   | Layout 3 | `11f53e6cc58d`  |
| 1396   | Layout 3 | `11f53e6cc58d`  |
| 1391   | Layout 3 | `11f53e6cc58d`  |
| 1390   | Layout 3 | `11f53e6cc58d`  |
| 1386   | Layout 3 | `11f53e6cc58d`  |
| 1381   | Layout 3 | `11f53e6cc58d`  |
| 1379   | Layout 3 | `11f53e6cc58d`  |
| 1372   | Layout 3 | `11f53e6cc58d`  |
| 1366   | Layout 3 | `11f53e6cc58d`  |
| 1364   | Layout 3 | `11f53e6cc58d`  |
| 1363   | Layout 3 | `11f53e6cc58d`  |
| 1360   | Layout 3 | `11f53e6cc58d`  |
| 1358   | Layout 3 | `11f53e6cc58d`  |
| 1355   | Layout 3 | `11f53e6cc58d`  |
| 1351   | Layout 3 | `11f53e6cc58d`  |
| 1348   | Layout 3 | `11f53e6cc58d`  |
| 1346   | Layout 3 | `11f53e6cc58d`  |
| 1341   | Layout 3 | `11f53e6cc58d`  |
| 1340   | Layout 3 | `11f53e6cc58d`  |
| 1338   | Layout 3 | `11f53e6cc58d`  |
| 1335   | Layout 3 | `11f53e6cc58d`  |
| 1333   | Layout 3 | `11f53e6cc58d`  |
| 1329   | Layout 2 | `11f53e6cc58d`  |
| 1327   | Layout 2 | `11f53e6cc58d`  |
| 1324   | Layout 2 | `11f53e6cc58d`  |
| 1321   | Layout 2 | `11f53e6cc58d`  |
| 1319   | Layout 2 | `11f53e6cc58d`  |
| 1318   | Layout 2 | `11f53e6cc58d`  |
| 1316   | Layout 2 | `11f53e6cc58d`  |
| 1313   | Layout 1 | `11f53e6cc58d`  |
| 1311   | Layout 1 | `11f53e6cc58d`  |
| 1309   | Layout 1 | `11f53e6cc58d`  |
| 1304   | Layout 1 | `11f53e6cc58d`  |
| 1292   | Layout 1 | `11f53e6cc58d`  |
| 1286   | Layout 1 | `11f53e6cc58d`  |
| 1280   | Layout 1 | `11f53e6cc58d`  |
| 1276   | Layout 1 | `11f53e6cc58d`  |
| 1267   | Layout 1 | `11f53e6cc58d`  |
| 1261   | No file  | `11f53e6cc58d`  |
| 1256   | No file  | `11f53e6cc58d`  |
| 1250   | No file  | `11f53e6cc58d`  |
| 1246   | No file  | `11f53e6cc58d`  |
| 1239   | No file  | `11f53e6cc58d`  |
| 1230   | No file  | `11f53e6cc58d`  |
| 1226   | No file  | `11f53e6cc58d`  |
| 1220   | No file  | `11f53e6cc58d`  |
| 1217   | No file  | `11f53e6cc58d`  |
| 1211   | No file  | `11f53e6cc58d`  |
| 1210   | No file  | `11f53e6cc58d`  |
| 1208   | No file  | `11f53e6cc58d`  |
| 1203   | No file  | `11f53e6cc58d`  |
| 1197   | No file  | `11f53e6cc58d`  |
| 1194   | No file  | `11f53e6cc58d`  |
| 1192   | No file  | `11f53e6cc58d`  |
| 1187   | No file  | `11f53e6cc58d`  |
| 1183   | No file  | `11f53e6cc58d`  |
| 1177   | No file  | `11f53e6cc58d`  |
| 1173   | No file  | `11f53e6cc58d`  |
| 1167   | No file  | `11f53e6cc58d`  |
| 1164   | No file  | `11f53e6cc58d`  |
| 1156   | No file  | `11f53e6cc58d`  |
| 1149   | No file  | `11f53e6cc58d`  |
| 1144   | No file  | `11f53e6cc58d`  |
| 1137   | No file  | `11f53e6cc58d`  |
| 1132   | No file  | `11f53e6cc58d`  |
| 1127   | No file  | `11f53e6cc58d`  |
| 1122   | No file  | `11f53e6cc58d`  |
| 1118   | No file  | `11f53e6cc58d`  |
| 1114   | No file  | `11f53e6cc58d`  |
| 1109   | No file  | `11f53e6cc58d`  |
| 1102   | No file  | `11f53e6cc58d`  |
| 1096   | No file  | `11f53e6cc58d`  |
| 1088   | No file  | `11f53e6cc58d`  |
| 1081   | No file  | `11f53e6cc58d`  |
| 1076   | No file  | `11f53e6cc58d`  |
| 1069   | No file  | `11f53e6cc58d`  |
| 1064   | No file  | `11f53e6cc58d`  |
| 1058   | No file  | `11f53e6cc58d`  |
| 1051   | No file  | `11f53e6cc58d`  |
| 1044   | No file  | `11f53e6cc58d`  |
| 1036   | No file  | `11f53e6cc58d`  |
| 1026   | No file  | `11f53e6cc58d`  |
| 1016   | No file  | `11f53e6cc58d`  |
| 1009   | No file  | `11f53e6cc58d`  |
| 1005   | No file  | `11f53e6cc58d`  |
| 1000   | No file  | `11f53e6cc58d`  |
| 998    | No file  | `11f53e6cc58d`  |
| 990    | No file  | `11f53e6cc58d`  |
| 979    | No file  | `11f53e6cc58d`  |
| 972    | No file  | `11f53e6cc58d`  |
| 963    | No file  | `11f53e6cc58d`  |
| 955    | No file  | `11f53e6cc58d`  |
| 946    | No file  | `11f53e6cc58d`  |
| 938    | No file  | `11f53e6cc58d`  |
| 927    | No file  | `11f53e6cc58d`  |
| 911    | No file  | `11f53e6cc58d`  |
| 904    | No file  | `11f53e6cc58d`  |
| 899    | No file  | `11f53e6cc58d`  |
| 894    | No file  | `11f53e6cc58d`  |
| 885    | No file  | `11f53e6cc58d`  |
| 879    | No file  | `11f53e6cc58d`  |
| 872    | No file  | `11f53e6cc58d`  |
| 864    | No file  | `11f53e6cc58d`  |
| 855    | No file  | `11f53e6cc58d`  |
| 853    | No file  | `11f53e6cc58d`  |
| 845    | No file  | `11f53e6cc58d`  |
| 837    | No file  | `11f53e6cc58d`  |
| 829    | No file  | `11f53e6cc58d`  |
| 822    | No file  | `11f53e6cc58d`  |
| 814    | No file  | `11f53e6cc58d`  |
| 805    | No file  | `11f53e6cc58d`  |
| 794    | No file  | `11f53e6cc58d`  |
| 787    | No file  | `11f53e6cc58d`  |
| 780    | No file  | `11f53e6cc58d`  |
| 771    | No file  | `11f53e6cc58d`  |
| 760    | No file  | `11f53e6cc58d`  |
| 748    | No file  | `11f53e6cc58d`  |
| 741    | No file  | `11f53e6cc58d`  |
| 736    | No file  | `11f53e6cc58d`  |
| 731    | No file  | `11f53e6cc58d`  |
| 723    | No file  | `11f53e6cc58d`  |
| 711    | No file  | `11f53e6cc58d`  |
| 707    | No file  | `11f53e6cc58d`  |
| 697    | No file  | `11f53e6cc58d`  |
| 689    | No file  | `11f53e6cc58d`  |
| 683    | No file  | `11f53e6cc58d`  |
| 678    | No file  | `11f53e6cc58d`  |
| 670    | No file  | `11f53e6cc58d`  |
| 661    | No file  | `11f53e6cc58d`  |
| 656    | No file  | `11f53e6cc58d`  |
| 652    | No file  | `11f53e6cc58d`  |
| 643    | No file  | `11f53e6cc58d`  |
| 637    | No file  | `11f53e6cc58d`  |
| 630    | No file  | `11f53e6cc58d`  |
| 627    | No file  | `11f53e6cc58d`  |
| 621    | No file  | `11f53e6cc58d`  |
| 617    | No file  | `11f53e6cc58d`  |
| 615    | No file  | `11f53e6cc58d`  |
| 606    | No file  | `11f53e6cc58d`  |
| 599    | No file  | `11f53e6cc58d`  |
| 592    | No file  | `11f53e6cc58d`  |
| 586    | No file  | `11f53e6cc58d`  |
| 577    | No file  | `11f53e6cc58d`  |
| 569    | No file  | `11f53e6cc58d`  |
| 561    | No file  | `11f53e6cc58d`  |
| 554    | No file  | `11f53e6cc58d`  |
| 542    | No file  | `11f53e6cc58d`  |
| 532    | No file  | `11f53e6cc58d`  |
| 531    | No file  | `11f53e6cc58d`  |
| 526    | No file  | `11f53e6cc58d`  |
| 521    | No file  | `11f53e6cc58d`  |
| 517    | No file  | `11f53e6cc58d`  |
| 510    | No file  | `11f53e6cc58d`  |
| 508    | No file  | `11f53e6cc58d`  |
| 504    | No file  | `11f53e6cc58d`  |
| 497    | No file  | `11f53e6cc58d`  |
| 491    | No file  | `11f53e6cc58d`  |
| 485    | No file  | `11f53e6cc58d`  |
| 478    | No file  | `11f53e6cc58d`  |
| 472    | No file  | `11f53e6cc58d`  |
| 466    | No file  | `11f53e6cc58d`  |
| 457    | No file  | `11f53e6cc58d`  |
| 452    | No file  | `11f53e6cc58d`  |
| 449    | No file  | `11f53e6cc58d`  |
| 435    | No file  | `11f53e6cc58d`  |

<!-- versions:end -->

## Companion Files

The handler reads no companion file. Names come from LOC type `6` and icons
from the character icon index, both keyed by `character_id`.

All multi-byte values are little-endian.

## Layout 4

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
| `+0x05`       | f32[4][4]               | parent_world_tm   | World transform of the house building; identity except on houses; see [House Transforms](#house-transforms) |
| `+0x45`       | f32[4][4]               | child_world_tm    | World transform of the house's household mesh; identity except on houses |
| `+0x85`       | i32                     | household_index   | Index of the house's `<info>` in `hosueholdall.xml`; `-1` except on houses |
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
| `+0x88` | i32       | unknown_88 | `0` on every face; see Open Questions                     |

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

## Layout 3

The row has no `unknown_8b` yet, so it is one byte shorter. Field names
keep Layout 4's offsets.

### Row (variable: 155 bytes + hull layers)

| Offset        | Type                    | Field             | Notes |
| ------------- | ----------------------- | ----------------- | ----- |
| `+0x00`       | u16                     | character_id      |       |
| `+0x02`       | u8                      | armor_material    |       |
| `+0x03`       | u8                      | object_kind       |       |
| `+0x04`       | u8                      | installation_type |       |
| `+0x05`       | f32[4][4]               | parent_world_tm   |       |
| `+0x45`       | f32[4][4]               | child_world_tm    |       |
| `+0x85`       | i32                     | household_index   |       |
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

## Layout 2

The row ends at `unknown_layers_00`: the six place flags come with Layout
3. Every field holds the same value as on client 1333 on all 2,983 rows of
client 1329.

### Row (variable: 149 bytes + hull layers)

| Offset        | Type                    | Field             | Notes |
| ------------- | ----------------------- | ----------------- | ----- |
| `+0x00`       | u16                     | character_id      |       |
| `+0x02`       | u8                      | armor_material    |       |
| `+0x03`       | u8                      | object_kind       |       |
| `+0x04`       | u8                      | installation_type |       |
| `+0x05`       | f32[4][4]               | parent_world_tm   |       |
| `+0x45`       | f32[4][4]               | child_world_tm    |       |
| `+0x85`       | i32                     | household_index   |       |
| `+0x89`       | u8                      | is_collision      |       |
| `+0x8A`       | u8                      | is_siege_tent     |       |
| `+0x8B`       | u32                     | layer_count       |       |
| `+0x8F`       | u32                     | unknown_90        |       |
| `+0x93`       | Hull Layer[layer_count] | layers            |       |
| `layers+0x00` | u16                     | unknown_layers_00 | The row's own `character_id` on the maid dolls 18951 to 18967 (client 1329), else `0` |

## Layout 1

The row has no hull layers and no `unknown_layers_00`, so every row is 139
bytes. All 2,905 rows of client 1313 hold the same values as on client
1333 in the fields both layouts have.

### Row (139 bytes)

| Offset  | Type      | Field             | Notes |
| ------- | --------- | ----------------- | ----- |
| `+0x00` | u16       | character_id      |       |
| `+0x02` | u8        | armor_material    |       |
| `+0x03` | u8        | object_kind       |       |
| `+0x04` | u8        | installation_type |       |
| `+0x05` | f32[4][4] | parent_world_tm   |       |
| `+0x45` | f32[4][4] | child_world_tm    |       |
| `+0x85` | i32       | household_index   |       |
| `+0x89` | u8        | is_collision      |       |
| `+0x8A` | u8        | is_siege_tent     |       |

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

## House Transforms

`parent_world_tm`, `child_world_tm` and `household_index` are set on the
same 865 rows of client 3483, the house kinds `5` (815), `1` (25), `9`
(17) and `36` (8): the rows whose `characterobject.dbss` record ends in a
House Tail. On the other 4,266 rows both matrices are the identity and
`household_index` is `-1`.

`gamecommondata/hosueholdall.xml` (the client's spelling) holds one
`<info>` per house scene, 872 on client 3483, each with its floors, doors
and windows. `household_index` is the position of the house's `<info>` in
that file, counted from `0`, and that `<info>` has the row's
`character_id` as `_householdHashCode`: 865 of 865 house rows. Morning
Light Nampo 1 (3823) is the first `<info>`, Arehaza 1-1 to 2-2 the last
four (`868` to `871`). No row points at the other 7, `433` to `439`, whose
`_householdHashCode` is no `baseobject.bss` key (`22_Mention/STR/` meshes).

On a house row both matrices are a rotation with a translation in world
coordinates in the fourth row. The first three rows of the two matrices are
the same on every row; the translations are up to 4,539 units apart. The
`<info>` the index points at holds both:

| Field             | `hosueholdall.xml` attribute               | Matching house rows (client 3483) |
| ----------------- | ------------------------------------------ | --------------------------------- |
| `parent_world_tm` | `_matParentInfo.11` to `_matParentInfo.44` | 865 of 865, all 16 values         |
| `child_world_tm`  | `_position.x`, `.y`, `.z`                  | 865 of 865, the translation       |

Morning Light Nampo 1 has its `parent_world_tm` translation at x
`-1290587`, y `-7794`, z `1135967`, where its `<info>` places the building
(`_parentMeshName` `Ori_Str_FarmHouse_01.pam`), and its `child_world_tm`
translation at `-1290747`, `-7526`, `1135993`, the household mesh
(`_householdMeshName` `Ori_Str_FarmHouse_01_HH.pam`). On client 1329 the file
writes `_matParentPos` (the translation only) in place of
`_matParentInfo`, and all 793 house rows match it and `_position` the same
way.

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

The house fields have no sheet column; they are named from the client's
`hosueholdall.xml` (see House Transforms) and the 2016 structs. The 2016
`PAHouseSceneBaseInfo` holds `_householdName`, `_householdMeshName`,
`_parentMeshName`, the floor and door lists, `_matParentWorldTM`,
`_householdHashCode` and `_position`, the attributes of an `<info>` (the
XML writes the matrix as `_matParentInfo`). The 2016
`gc::ObjectStaticStatus` points at its house with `_paHouseSceneBaseInfo`,
the field `household_index` stands for, and holds `_matParentWorldTM` and
`_matChildWorldTM`. `parent_world_tm` equals the `<info>` matrix.
`child_world_tm` carries `_position`, and the 2016
`ObjectStaticStatusWrapper::getHousePosX` to `getHousePosZ` return
`_matChildWorldTM` `_41` to `_43`, its translation.

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
everywhere else. The other two, 18972 and 18973 (added on client 2107),
also have a `maid.dbss` row but no English LOC name. The 2016 struct has a
`_maidStaticStatus` pointer, which a `maid.dbss` key would stand for. The
`Install_Maid` column of the client 1784 sheet is `1` on the 21 maid rows
it has and on 535 rows of installation type `0`, so it does not match;
`SummonCharacterKey` holds the maid NPC (`39801` on 18951), not the doll.

### Face Tail

`unknown_88` of every face is `0`, where the 2016 plane has
`_negNormBitMask`. A sign mask of the normal would not be `0` everywhere:
15,332 of the 28,202 faces of client 3483 have a negative `normal`
component. The planes of `household/household.xml` and `tent.xml` carry no
such attribute.

### Siege Building Flag

`unknown_8b` comes with Layout 4 (client 1762) and is `1` on 193 rows of
client 3483, all of installation type `0` and siege object kinds such as
`3`, `17` and `18`. No `Object_Table` column of the client 1784 sheet
matches it as a flag; the closest, `RentalFee`, agrees on 3,458 of the
3,497 shared rows.
