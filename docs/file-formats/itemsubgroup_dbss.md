# `itemsubgroup.dbss` Format

## Purpose

Item subgroups: named lists of items that other tables hand out as a group. Each record is one subgroup key followed by its item entries. Worker production reaches it through [`plantexchangegroup.bss`](plantexchangegroup_bss.md) (`exchange_key`), its `itemexchangesource.bss` exchange and that exchange's [`itemmaingroup.bss`](itemmaingroup_bss.md) drop groups; NPC shops and trade managers reach theirs through [`itemmaingroup.bss`](itemmaingroup_bss.md) groups; the other subgroups belong to tables not decoded yet (drops, boxes, trade goods). `itemsubgroupoffset.dbss` is required to address the variable-length records.

The record header and the item ID position match [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), which leaves the rest of each 135-byte entry unmapped. Their "0-100 items" range does not hold: subgroup 52001 has 11,560 entries.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes      | Records                                    | Row bytes |
| ------ | -------------- | ------------------------- | ---------- | ------------------------------------------ | --------- |
| 1      | 1529 and later | `itemsubgroup.dbss`       | 13,963,261 | 101,183 Item Entry, 16,864 Subgroup Record | 135       |
| 1      | 1529 and later | `itemsubgroupoffset.dbss` | 168,660    | 16,864 Offset Row                          | 10        |

| Layout | File                      | Known               | Unknown              |
| ------ | ------------------------- | ------------------- | -------------------- |
| 1      | `itemsubgroup.dbss`       | 3,170,406 B (22.7%) | 10,792,855 B (77.3%) |
| 1      | `itemsubgroupoffset.dbss` | 168,652 B (100.0%)  | 8 B (0.0%)           |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `68734a5e9f51`  |
| 3482   | Layout 1             | `68734a5e9f51`  |
| 3474   | Layout 1             | `68734a5e9f51`  |
| 3473   | Layout 1             | `68734a5e9f51`  |
| 3464   | Layout 1             | `68734a5e9f51`  |
| 3458   | Layout 1             | `68734a5e9f51`  |
| 3454   | Layout 1             | `68734a5e9f51`  |
| 3444   | Layout 1             | `68734a5e9f51`  |
| 3435   | Layout 1             | `68734a5e9f51`  |
| 3426   | Layout 1             | `68734a5e9f51`  |
| 3418   | Layout 1             | `68734a5e9f51`  |
| 3412   | Layout 1             | `68734a5e9f51`  |
| 3402   | Layout 1             | `68734a5e9f51`  |
| 3396   | Layout 1             | `68734a5e9f51`  |
| 3387   | Layout 1             | `68734a5e9f51`  |
| 3381   | Layout 1             | `68734a5e9f51`  |
| 3373   | Layout 1             | `68734a5e9f51`  |
| 3364   | Layout 1             | `68734a5e9f51`  |
| 3356   | Layout 1             | `68734a5e9f51`  |
| 3349   | Layout 1             | `68734a5e9f51`  |
| 3342   | Layout 1             | `68734a5e9f51`  |
| 3335   | Layout 1             | `68734a5e9f51`  |
| 3326   | Layout 1             | `68734a5e9f51`  |
| 3321   | Layout 1             | `68734a5e9f51`  |
| 3314   | Layout 1             | `68734a5e9f51`  |
| 3303   | Layout 1             | `68734a5e9f51`  |
| 3302   | Layout 1             | `68734a5e9f51`  |
| 3293   | Layout 1             | `68734a5e9f51`  |
| 3283   | Layout 1             | `68734a5e9f51`  |
| 3275   | Layout 1             | `68734a5e9f51`  |
| 3267   | Layout 1             | `68734a5e9f51`  |
| 3258   | Layout 1             | `68734a5e9f51`  |
| 3251   | Layout 1             | `68734a5e9f51`  |
| 3242   | Layout 1             | `68734a5e9f51`  |
| 3235   | Layout 1             | `68734a5e9f51`  |
| 3229   | Layout 1             | `68734a5e9f51`  |
| 3212   | Layout 1             | `68734a5e9f51`  |
| 3203   | Layout 1             | `68734a5e9f51`  |
| 3193   | Layout 1             | `68734a5e9f51`  |
| 3186   | Layout 1             | `68734a5e9f51`  |
| 3177   | Layout 1             | `68734a5e9f51`  |
| 3169   | Layout 1             | `68734a5e9f51`  |
| 3158   | Layout 1             | `68734a5e9f51`  |
| 3151   | Layout 1             | `68734a5e9f51`  |
| 3144   | Layout 1             | `68734a5e9f51`  |
| 3133   | Layout 1             | `68734a5e9f51`  |
| 3125   | Layout 1             | `68734a5e9f51`  |
| 3118   | Layout 1             | `68734a5e9f51`  |
| 3111   | Layout 1             | `68734a5e9f51`  |
| 3103   | Layout 1             | `68734a5e9f51`  |
| 3095   | Layout 1             | `68734a5e9f51`  |
| 3086   | Layout 1             | `68734a5e9f51`  |
| 3072   | Layout 1             | `68734a5e9f51`  |
| 3062   | Layout 1             | `68734a5e9f51`  |
| 3052   | Layout 1             | `68734a5e9f51`  |
| 3045   | Layout 1             | `68734a5e9f51`  |
| 3037   | Layout 1             | `68734a5e9f51`  |
| 3030   | Layout 1             | `68734a5e9f51`  |
| 3021   | Layout 1             | `68734a5e9f51`  |
| 3012   | Layout 1             | `68734a5e9f51`  |
| 3002   | Layout 1             | `68734a5e9f51`  |
| 2995   | Layout 1             | `68734a5e9f51`  |
| 2987   | Layout 1             | `68734a5e9f51`  |
| 2978   | Layout 1             | `68734a5e9f51`  |
| 2970   | Layout 1             | `68734a5e9f51`  |
| 2959   | Layout 1             | `68734a5e9f51`  |
| 2951   | Layout 1             | `68734a5e9f51`  |
| 2942   | Layout 1             | `68734a5e9f51`  |
| 2935   | Layout 1             | `68734a5e9f51`  |
| 2932   | Layout 1             | `68734a5e9f51`  |
| 2923   | Layout 1             | `68734a5e9f51`  |
| 2919   | Layout 1             | `68734a5e9f51`  |
| 2907   | Layout 1             | `68734a5e9f51`  |
| 2900   | Layout 1             | `68734a5e9f51`  |
| 2891   | Layout 1             | `68734a5e9f51`  |
| 2882   | Layout 1             | `68734a5e9f51`  |
| 2872   | Layout 1             | `68734a5e9f51`  |
| 2863   | Layout 1             | `68734a5e9f51`  |
| 2855   | Layout 1             | `68734a5e9f51`  |
| 2849   | Layout 1             | `68734a5e9f51`  |
| 2844   | Layout 1             | `68734a5e9f51`  |
| 2834   | Layout 1             | `68734a5e9f51`  |
| 2825   | Layout 1             | `68734a5e9f51`  |
| 2819   | Layout 1             | `68734a5e9f51`  |
| 2811   | Layout 1             | `68734a5e9f51`  |
| 2803   | Layout 1             | `68734a5e9f51`  |
| 2794   | Layout 1             | `68734a5e9f51`  |
| 2783   | Layout 1             | `68734a5e9f51`  |
| 2774   | Layout 1             | `68734a5e9f51`  |
| 2765   | Layout 1             | `68734a5e9f51`  |
| 2756   | Layout 1             | `68734a5e9f51`  |
| 2750   | Layout 1             | `68734a5e9f51`  |
| 2743   | Layout 1             | `68734a5e9f51`  |
| 2736   | Layout 1             | `68734a5e9f51`  |
| 2726   | Layout 1             | `68734a5e9f51`  |
| 2717   | Layout 1             | `68734a5e9f51`  |
| 2709   | Layout 1             | `68734a5e9f51`  |
| 2703   | Layout 1             | `68734a5e9f51`  |
| 2695   | Layout 1             | `68734a5e9f51`  |
| 2684   | Layout 1             | `68734a5e9f51`  |
| 2672   | Layout 1             | `68734a5e9f51`  |
| 2665   | Layout 1             | `68734a5e9f51`  |
| 2657   | Layout 1             | `68734a5e9f51`  |
| 2649   | Layout 1             | `68734a5e9f51`  |
| 2644   | Layout 1             | `68734a5e9f51`  |
| 2637   | Layout 1             | `68734a5e9f51`  |
| 2629   | Layout 1             | `68734a5e9f51`  |
| 2619   | Layout 1             | `68734a5e9f51`  |
| 2612   | Layout 1             | `68734a5e9f51`  |
| 2606   | Layout 1             | `68734a5e9f51`  |
| 2602   | Layout 1             | `68734a5e9f51`  |
| 2601   | Layout 1             | `68734a5e9f51`  |
| 2592   | Layout 1             | `68734a5e9f51`  |
| 2583   | Layout 1             | `68734a5e9f51`  |
| 2575   | Layout 1             | `68734a5e9f51`  |
| 2567   | Layout 1             | `68734a5e9f51`  |
| 2560   | Layout 1             | `68734a5e9f51`  |
| 2553   | Layout 1             | `68734a5e9f51`  |
| 2545   | Layout 1             | `68734a5e9f51`  |
| 2538   | Layout 1             | `68734a5e9f51`  |
| 2529   | Layout 1             | `68734a5e9f51`  |
| 2519   | Layout 1             | `68734a5e9f51`  |
| 2513   | Layout 1             | `68734a5e9f51`  |
| 2510   | Layout 1             | `68734a5e9f51`  |
| 2507   | Layout 1             | `68734a5e9f51`  |
| 2503   | Layout 1             | `68734a5e9f51`  |
| 2498   | Layout 1             | `68734a5e9f51`  |
| 2492   | Layout 1             | `68734a5e9f51`  |
| 2487   | Layout 1             | `68734a5e9f51`  |
| 2480   | Layout 1             | `68734a5e9f51`  |
| 2474   | Layout 1             | `68734a5e9f51`  |
| 2468   | Layout 1             | `68734a5e9f51`  |
| 2460   | Layout 1             | `68734a5e9f51`  |
| 2453   | Layout 1             | `68734a5e9f51`  |
| 2444   | Layout 1             | `68734a5e9f51`  |
| 2438   | Layout 1             | `68734a5e9f51`  |
| 2434   | Layout 1             | `68734a5e9f51`  |
| 2429   | Layout 1             | `68734a5e9f51`  |
| 2421   | Layout 1             | `68734a5e9f51`  |
| 2414   | Layout 1             | `68734a5e9f51`  |
| 2407   | Layout 1             | `68734a5e9f51`  |
| 2401   | Layout 1             | `68734a5e9f51`  |
| 2397   | Layout 1             | `68734a5e9f51`  |
| 2393   | Layout 1             | `68734a5e9f51`  |
| 2384   | Layout 1             | `68734a5e9f51`  |
| 2378   | Layout 1             | `68734a5e9f51`  |
| 2372   | Layout 1             | `68734a5e9f51`  |
| 2358   | Layout 1             | `68734a5e9f51`  |
| 2352   | Layout 1             | `68734a5e9f51`  |
| 2347   | Layout 1             | `68734a5e9f51`  |
| 2343   | Layout 1             | `68734a5e9f51`  |
| 2335   | Layout 1             | `68734a5e9f51`  |
| 2327   | Layout 1             | `68734a5e9f51`  |
| 2324   | Layout 1             | `68734a5e9f51`  |
| 2319   | Layout 1             | `68734a5e9f51`  |
| 2313   | Layout 1             | `68734a5e9f51`  |
| 2308   | Layout 1             | `68734a5e9f51`  |
| 2302   | Layout 1             | `68734a5e9f51`  |
| 2295   | Layout 1             | `68734a5e9f51`  |
| 2290   | Layout 1             | `68734a5e9f51`  |
| 2284   | Layout 1             | `68734a5e9f51`  |
| 2276   | Layout 1             | `68734a5e9f51`  |
| 2269   | Layout 1             | `68734a5e9f51`  |
| 2259   | Layout 1             | `68734a5e9f51`  |
| 2250   | Layout 1             | `68734a5e9f51`  |
| 2243   | Layout 1             | `68734a5e9f51`  |
| 2235   | Layout 1             | `68734a5e9f51`  |
| 2229   | Layout 1             | `68734a5e9f51`  |
| 2224   | Layout 1             | `68734a5e9f51`  |
| 2218   | Layout 1             | `68734a5e9f51`  |
| 2215   | Layout 1             | `68734a5e9f51`  |
| 2207   | Layout 1             | `68734a5e9f51`  |
| 2203   | Layout 1             | `68734a5e9f51`  |
| 2196   | Layout 1             | `68734a5e9f51`  |
| 2192   | Layout 1             | `68734a5e9f51`  |
| 2189   | Layout 1             | `68734a5e9f51`  |
| 2183   | Layout 1             | `68734a5e9f51`  |
| 2179   | Layout 1             | `68734a5e9f51`  |
| 2171   | Layout 1             | `68734a5e9f51`  |
| 2163   | Layout 1             | `68734a5e9f51`  |
| 2156   | Layout 1             | `68734a5e9f51`  |
| 2151   | Layout 1             | `68734a5e9f51`  |
| 2147   | Layout 1             | `68734a5e9f51`  |
| 2142   | Layout 1             | `68734a5e9f51`  |
| 2138   | Layout 1             | `68734a5e9f51`  |
| 2134   | Layout 1             | `68734a5e9f51`  |
| 2130   | Layout 1             | `68734a5e9f51`  |
| 2122   | Layout 1             | `68734a5e9f51`  |
| 2107   | Layout 1             | `68734a5e9f51`  |
| 2098   | Layout 1             | `68734a5e9f51`  |
| 2089   | Layout 1             | `68734a5e9f51`  |
| 2081   | Layout 1             | `68734a5e9f51`  |
| 2073   | Layout 1             | `68734a5e9f51`  |
| 2067   | Layout 1             | `68734a5e9f51`  |
| 2063   | Layout 1             | `68734a5e9f51`  |
| 2059   | Layout 1             | `68734a5e9f51`  |
| 2052   | Layout 1             | `68734a5e9f51`  |
| 2044   | Layout 1             | `68734a5e9f51`  |
| 2039   | Layout 1             | `68734a5e9f51`  |
| 2032   | Layout 1             | `68734a5e9f51`  |
| 2025   | Layout 1             | `68734a5e9f51`  |
| 2011   | Layout 1             | `68734a5e9f51`  |
| 2005   | Layout 1             | `68734a5e9f51`  |
| 2000   | Layout 1             | `68734a5e9f51`  |
| 1996   | Layout 1             | `68734a5e9f51`  |
| 1991   | Layout 1             | `68734a5e9f51`  |
| 1985   | Layout 1             | `68734a5e9f51`  |
| 1980   | Layout 1             | `68734a5e9f51`  |
| 1969   | Layout 1             | `68734a5e9f51`  |
| 1964   | Layout 1             | `68734a5e9f51`  |
| 1958   | Layout 1             | `68734a5e9f51`  |
| 1950   | Layout 1             | `68734a5e9f51`  |
| 1945   | Layout 1             | `68734a5e9f51`  |
| 1937   | Layout 1             | `68734a5e9f51`  |
| 1933   | Layout 1             | `68734a5e9f51`  |
| 1927   | Layout 1             | `68734a5e9f51`  |
| 1921   | Layout 1             | `68734a5e9f51`  |
| 1914   | Layout 1             | `68734a5e9f51`  |
| 1908   | Layout 1             | `68734a5e9f51`  |
| 1897   | Layout 1             | `68734a5e9f51`  |
| 1892   | Layout 1             | `68734a5e9f51`  |
| 1886   | Layout 1             | `68734a5e9f51`  |
| 1881   | Layout 1             | `68734a5e9f51`  |
| 1871   | Layout 1             | `68734a5e9f51`  |
| 1866   | Layout 1             | `68734a5e9f51`  |
| 1862   | Layout 1             | `68734a5e9f51`  |
| 1854   | Layout 1             | `68734a5e9f51`  |
| 1846   | Layout 1             | `68734a5e9f51`  |
| 1838   | Layout 1             | `68734a5e9f51`  |
| 1832   | Layout 1             | `68734a5e9f51`  |
| 1826   | Layout 1             | `68734a5e9f51`  |
| 1822   | Layout 1             | `68734a5e9f51`  |
| 1818   | Layout 1             | `68734a5e9f51`  |
| 1804   | Layout 1             | `68734a5e9f51`  |
| 1794   | Layout 1             | `68734a5e9f51`  |
| 1790   | Layout 1             | `68734a5e9f51`  |
| 1784   | Layout 1             | `68734a5e9f51`  |
| 1774   | Layout 1             | `68734a5e9f51`  |
| 1771   | Layout 1             | `68734a5e9f51`  |
| 1762   | Layout 1             | `68734a5e9f51`  |
| 1759   | Layout 1             | `68734a5e9f51`  |
| 1754   | Layout 1             | `68734a5e9f51`  |
| 1749   | Layout 1             | `68734a5e9f51`  |
| 1743   | Layout 1             | `68734a5e9f51`  |
| 1737   | Layout 1             | `68734a5e9f51`  |
| 1731   | Layout 1             | `68734a5e9f51`  |
| 1725   | Layout 1             | `68734a5e9f51`  |
| 1717   | Layout 1             | `68734a5e9f51`  |
| 1710   | Layout 1             | `68734a5e9f51`  |
| 1704   | Layout 1             | `68734a5e9f51`  |
| 1698   | Layout 1             | `68734a5e9f51`  |
| 1690   | Layout 1             | `68734a5e9f51`  |
| 1685   | Layout 1             | `68734a5e9f51`  |
| 1680   | Layout 1             | `68734a5e9f51`  |
| 1674   | Layout 1             | `68734a5e9f51`  |
| 1668   | Layout 1             | `68734a5e9f51`  |
| 1659   | Layout 1             | `68734a5e9f51`  |
| 1649   | Layout 1             | `68734a5e9f51`  |
| 1642   | Layout 1             | `68734a5e9f51`  |
| 1636   | Layout 1             | `68734a5e9f51`  |
| 1628   | Layout 1             | `68734a5e9f51`  |
| 1622   | Layout 1             | `68734a5e9f51`  |
| 1614   | Layout 1             | `68734a5e9f51`  |
| 1608   | Layout 1             | `68734a5e9f51`  |
| 1602   | Layout 1             | `68734a5e9f51`  |
| 1598   | Layout 1             | `68734a5e9f51`  |
| 1594   | Layout 1             | `68734a5e9f51`  |
| 1590   | Layout 1             | `68734a5e9f51`  |
| 1587   | Layout 1             | `68734a5e9f51`  |
| 1584   | Layout 1             | `68734a5e9f51`  |
| 1579   | Layout 1             | `68734a5e9f51`  |
| 1572   | Layout 1             | `68734a5e9f51`  |
| 1565   | Layout 1             | `68734a5e9f51`  |
| 1559   | Layout 1             | `68734a5e9f51`  |
| 1554   | Layout 1             | `68734a5e9f51`  |
| 1547   | Layout 1             | `68734a5e9f51`  |
| 1537   | Layout 1             | `68734a5e9f51`  |
| 1529   | Layout 1             | `68734a5e9f51`  |
| 1524   | No documented layout | `68734a5e9f51`  |
| 1519   | No documented layout | `68734a5e9f51`  |
| 1509   | No documented layout | `68734a5e9f51`  |
| 1506   | No documented layout | `68734a5e9f51`  |
| 1504   | No documented layout | `68734a5e9f51`  |
| 1500   | No documented layout | `68734a5e9f51`  |
| 1493   | No documented layout | `68734a5e9f51`  |
| 1489   | No documented layout | `68734a5e9f51`  |
| 1485   | No documented layout | `68734a5e9f51`  |
| 1481   | No documented layout | `68734a5e9f51`  |
| 1474   | No documented layout | `68734a5e9f51`  |
| 1466   | No documented layout | `68734a5e9f51`  |
| 1462   | No documented layout | `68734a5e9f51`  |
| 1459   | No documented layout | `68734a5e9f51`  |
| 1453   | No documented layout | `68734a5e9f51`  |
| 1450   | No documented layout | `68734a5e9f51`  |
| 1445   | No documented layout | `68734a5e9f51`  |
| 1439   | No documented layout | `68734a5e9f51`  |
| 1433   | No documented layout | `68734a5e9f51`  |
| 1430   | No documented layout | `68734a5e9f51`  |
| 1426   | No documented layout | `68734a5e9f51`  |
| 1421   | No documented layout | `68734a5e9f51`  |
| 1417   | No documented layout | `68734a5e9f51`  |
| 1416   | No documented layout | `68734a5e9f51`  |
| 1409   | No documented layout | `68734a5e9f51`  |
| 1405   | No documented layout | `68734a5e9f51`  |
| 1401   | No documented layout | `68734a5e9f51`  |
| 1396   | No documented layout | `68734a5e9f51`  |
| 1391   | No documented layout | `68734a5e9f51`  |
| 1390   | No documented layout | `68734a5e9f51`  |
| 1386   | No documented layout | `68734a5e9f51`  |
| 1381   | No documented layout | `68734a5e9f51`  |
| 1379   | No documented layout | `68734a5e9f51`  |
| 1372   | No documented layout | `68734a5e9f51`  |
| 1366   | No documented layout | `68734a5e9f51`  |
| 1364   | No documented layout | `68734a5e9f51`  |
| 1363   | No documented layout | `68734a5e9f51`  |
| 1360   | No documented layout | `68734a5e9f51`  |
| 1358   | No documented layout | `68734a5e9f51`  |
| 1355   | No documented layout | `68734a5e9f51`  |
| 1351   | No documented layout | `68734a5e9f51`  |
| 1348   | No documented layout | `68734a5e9f51`  |
| 1346   | No documented layout | `68734a5e9f51`  |
| 1341   | No documented layout | `68734a5e9f51`  |
| 1340   | No documented layout | `68734a5e9f51`  |
| 1338   | No documented layout | `68734a5e9f51`  |
| 1335   | No documented layout | `68734a5e9f51`  |
| 1333   | No documented layout | `68734a5e9f51`  |
| 1329   | No documented layout | `68734a5e9f51`  |
| 1327   | No file              | `68734a5e9f51`  |
| 1324   | No file              | `68734a5e9f51`  |
| 1321   | No file              | `68734a5e9f51`  |
| 1319   | No file              | `68734a5e9f51`  |
| 1318   | No file              | `68734a5e9f51`  |
| 1316   | No file              | `68734a5e9f51`  |
| 1313   | No file              | `68734a5e9f51`  |
| 1311   | No documented layout | `68734a5e9f51`  |
| 1309   | No documented layout | `68734a5e9f51`  |
| 1304   | No documented layout | `68734a5e9f51`  |
| 1292   | No documented layout | `68734a5e9f51`  |
| 1286   | No documented layout | `68734a5e9f51`  |
| 1280   | No documented layout | `68734a5e9f51`  |
| 1276   | No documented layout | `68734a5e9f51`  |
| 1267   | No documented layout | `68734a5e9f51`  |
| 1261   | No documented layout | `68734a5e9f51`  |
| 1256   | No documented layout | `68734a5e9f51`  |
| 1250   | No documented layout | `68734a5e9f51`  |
| 1246   | No documented layout | `68734a5e9f51`  |
| 1239   | No file              | `68734a5e9f51`  |
| 1230   | No file              | `68734a5e9f51`  |
| 1226   | No file              | `68734a5e9f51`  |
| 1220   | No file              | `68734a5e9f51`  |
| 1217   | No file              | `68734a5e9f51`  |
| 1211   | No file              | `68734a5e9f51`  |
| 1210   | No file              | `68734a5e9f51`  |
| 1208   | No file              | `68734a5e9f51`  |
| 1203   | No file              | `68734a5e9f51`  |
| 1197   | No file              | `68734a5e9f51`  |
| 1194   | No file              | `68734a5e9f51`  |
| 1192   | No file              | `68734a5e9f51`  |
| 1187   | No file              | `68734a5e9f51`  |
| 1183   | No file              | `68734a5e9f51`  |
| 1177   | No file              | `68734a5e9f51`  |
| 1173   | No file              | `68734a5e9f51`  |
| 1167   | No file              | `68734a5e9f51`  |
| 1164   | No file              | `68734a5e9f51`  |
| 1156   | No file              | `68734a5e9f51`  |
| 1149   | No file              | `68734a5e9f51`  |
| 1144   | No file              | `68734a5e9f51`  |
| 1137   | No file              | `68734a5e9f51`  |
| 1132   | No file              | `68734a5e9f51`  |
| 1127   | No file              | `68734a5e9f51`  |
| 1122   | No file              | `68734a5e9f51`  |
| 1118   | No file              | `68734a5e9f51`  |
| 1114   | No file              | `68734a5e9f51`  |
| 1109   | No file              | `68734a5e9f51`  |
| 1102   | No file              | `68734a5e9f51`  |
| 1096   | No file              | `68734a5e9f51`  |
| 1088   | No file              | `68734a5e9f51`  |
| 1081   | No file              | `68734a5e9f51`  |
| 1076   | No file              | `68734a5e9f51`  |
| 1069   | No file              | `68734a5e9f51`  |
| 1064   | No file              | `68734a5e9f51`  |
| 1058   | No file              | `68734a5e9f51`  |
| 1051   | No file              | `68734a5e9f51`  |
| 1044   | No file              | `68734a5e9f51`  |
| 1036   | No file              | `68734a5e9f51`  |
| 1026   | No file              | `68734a5e9f51`  |
| 1016   | No file              | `68734a5e9f51`  |
| 1009   | No file              | `68734a5e9f51`  |
| 1005   | No file              | `68734a5e9f51`  |
| 1000   | No file              | `68734a5e9f51`  |
| 998    | No file              | `68734a5e9f51`  |
| 990    | No file              | `68734a5e9f51`  |
| 979    | No file              | `68734a5e9f51`  |
| 972    | No file              | `68734a5e9f51`  |
| 963    | No file              | `68734a5e9f51`  |
| 955    | No file              | `68734a5e9f51`  |
| 946    | No file              | `68734a5e9f51`  |
| 938    | No file              | `68734a5e9f51`  |
| 927    | No file              | `68734a5e9f51`  |
| 911    | No file              | `68734a5e9f51`  |
| 904    | No file              | `68734a5e9f51`  |
| 899    | No file              | `68734a5e9f51`  |
| 894    | No file              | `68734a5e9f51`  |
| 885    | No file              | `68734a5e9f51`  |
| 879    | No file              | `68734a5e9f51`  |
| 872    | No file              | `68734a5e9f51`  |
| 864    | No file              | `68734a5e9f51`  |
| 855    | No file              | `68734a5e9f51`  |
| 853    | No file              | `68734a5e9f51`  |
| 845    | No file              | `68734a5e9f51`  |
| 837    | No file              | `68734a5e9f51`  |
| 829    | No file              | `68734a5e9f51`  |
| 822    | No file              | `68734a5e9f51`  |
| 814    | No file              | `68734a5e9f51`  |
| 805    | No file              | `68734a5e9f51`  |
| 794    | No file              | `68734a5e9f51`  |
| 787    | No file              | `68734a5e9f51`  |
| 780    | No file              | `68734a5e9f51`  |
| 771    | No file              | `68734a5e9f51`  |
| 760    | No file              | `68734a5e9f51`  |
| 748    | No file              | `68734a5e9f51`  |
| 741    | No file              | `68734a5e9f51`  |
| 736    | No file              | `68734a5e9f51`  |
| 731    | No file              | `68734a5e9f51`  |
| 723    | No file              | `68734a5e9f51`  |
| 711    | No file              | `68734a5e9f51`  |
| 707    | No file              | `68734a5e9f51`  |
| 697    | No file              | `68734a5e9f51`  |
| 689    | No file              | `68734a5e9f51`  |
| 683    | No file              | `68734a5e9f51`  |
| 678    | No file              | `68734a5e9f51`  |
| 670    | No file              | `68734a5e9f51`  |
| 661    | No file              | `68734a5e9f51`  |
| 656    | No file              | `68734a5e9f51`  |
| 652    | No file              | `68734a5e9f51`  |
| 643    | No file              | `68734a5e9f51`  |
| 637    | No file              | `68734a5e9f51`  |
| 630    | No file              | `68734a5e9f51`  |
| 627    | No file              | `68734a5e9f51`  |
| 621    | No file              | `68734a5e9f51`  |
| 617    | No file              | `68734a5e9f51`  |
| 615    | No file              | `68734a5e9f51`  |
| 606    | No file              | `68734a5e9f51`  |
| 599    | No file              | `68734a5e9f51`  |
| 592    | No file              | `68734a5e9f51`  |
| 586    | No file              | `68734a5e9f51`  |
| 577    | No file              | `68734a5e9f51`  |
| 569    | No file              | `68734a5e9f51`  |
| 561    | No file              | `68734a5e9f51`  |
| 554    | No file              | `68734a5e9f51`  |
| 542    | No file              | `68734a5e9f51`  |
| 532    | No file              | `68734a5e9f51`  |
| 531    | No file              | `68734a5e9f51`  |
| 526    | No file              | `68734a5e9f51`  |
| 521    | No file              | `68734a5e9f51`  |
| 517    | No file              | `68734a5e9f51`  |
| 510    | No file              | `68734a5e9f51`  |
| 508    | No file              | `68734a5e9f51`  |
| 504    | No file              | `68734a5e9f51`  |
| 497    | No file              | `68734a5e9f51`  |
| 491    | No file              | `68734a5e9f51`  |
| 485    | No file              | `68734a5e9f51`  |
| 478    | No file              | `68734a5e9f51`  |
| 472    | No file              | `68734a5e9f51`  |
| 466    | No file              | `68734a5e9f51`  |
| 457    | No file              | `68734a5e9f51`  |
| 452    | No file              | `68734a5e9f51`  |
| 449    | No file              | `68734a5e9f51`  |
| 435    | No file              | `68734a5e9f51`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                  |
| ------------------------- | -------- | ----------------------------------------------------- |
| `itemsubgroupoffset.dbss` | Required | Maps subgroup key to byte offset and record byte count |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`           |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset  | Type                           | Field         | Notes                                                  |
| ------- | ------------------------------ | ------------- | ------------------------------------------------------ |
| `+0x00` | u32                            | record_count  | Number of subgroups; `16,690` on the 2026-09-27 client |
| `+0x04` | Subgroup Record[record_count]  | record_stream | Variable-length records, packed back-to-back           |

Sorted by `data_offset`, the offset rows cover every byte from `+0x04` to EOF with no gaps or overlaps.

### Subgroup Record (variable: 18 bytes + entries)

| Offset  | Type                    | Field        | Notes                                                          |
| ------- | ----------------------- | ------------ | -------------------------------------------------------------- |
| `+0x00` | u32                     | subgroup_key | Equals the offset row `record_id` on every record; observed `1309`-`65535` |
| `+0x04` | bytes[10]               | unknown_04   | Always all zero                                                |
| `+0x0E` | u32                     | entry_count  | Number of entries; `1`-`11,560`, never `0`; unaligned           |
| `+0x12` | Item Entry[entry_count] | entries      | See Item Entry                                                 |

`18 + 135 * entry_count` equals the offset row `data_size` on all 16,690 records.

### Item Entry (135 bytes)

97,808 entries in total. Most set only `item_key` and `select_rate`; every offset not named is zero on every entry.

| Offset  | Type      | Field      | Notes                                                                  |
| ------- | --------- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u32       | item_key   | `(enchant_level << 24) \| item_id`, the same packing as the `itemenchant.dbss` key; see `item_key` Packing |
| `+0x04` | bytes[12] | unknown_04 | Always `0`                                                             |
| `+0x10` | u8        | unknown_10 | `1` on one entry, else `0`                                             |
| `+0x11` | u8        | unknown_11 | `1` on the 247 entries of subgroups 54001 and 55000, else `0`          |
| `+0x12` | i64       | min_count  | `-1` on 21,168 entries (subgroup bands 32xxx, 50xxx-52xxx, 55xxx), else `0`; see Field Names |
| `+0x1A` | i64       | max_count  | Same as `min_count` on every entry                                     |
| `+0x22` | i32       | intimacy_variation | `0` on 96,887 entries; negative on 921 (`-200` on 426, then `-370`, `-470`, `-50`, `-25`, `-100`, `-500`, `-300` and a few others) |
| `+0x26` | u8        | unknown_26 | `2` or `4` on the 247 entries of subgroups 54001 and 55000, else `0`; in 55000 `4` is every packaged dried fish, `2` everything else |
| `+0x27` | bytes[7]  | unknown_27 | Always `0`                                                             |
| `+0x2E` | u8        | is_apply_random_price | `1` on 794 entries, else `0`                                |
| `+0x2F` | u8        | rent_time  | `1`, `2` or `3` on three entries, else `0`                             |
| `+0x30` | bytes[3]  | unknown_30 | Always `0`                                                             |
| `+0x33` | u32       | select_rate | Selection weight; `1,000,000` on 96,952 entries; `0` on the 247 entries that set `unknown_83`; 226 below and 383 above one million (up to `9,000,000`); unaligned |
| `+0x37` | u8        | unknown_37 | `1` on the 247 entries of subgroups 54001 and 55000, else `0`          |
| `+0x38` | u8        | unknown_38 | Same as `unknown_37`                                                   |
| `+0x39` | bytes[2]  | unknown_39 | Always `0`                                                             |
| `+0x3B` | i64       | unknown_3b | Set on the same 247 entries, e.g. `1800` for Pepper Crate; the other price-like fields are fixed shares of it |
| `+0x43` | i64       | unknown_43 | Same entries; exactly 30%, 65%, 75%, 85% or 95% of `unknown_3b` (`1350` for Pepper Crate) |
| `+0x4B` | i64       | unknown_4b | Same entries; exactly 130% of `unknown_3b` on all of them (`2340` for Pepper Crate) |
| `+0x53` | i64       | unknown_53 | Same entries; its size is a fixed share of `unknown_3b` per floor group (65% floor: 6%, 75%: 6.5%, 85%: 7.5%, 95%: 5.8%; the 30% group mixes 6%-9%); the sign alternates +, - down the entries sorted by item ID |
| `+0x5B` | u8        | unknown_5b | Same entries; exactly 1% of `unknown_3b` (`18` for `1800`)             |
| `+0x5C` | bytes[39] | unknown_5c | Always `0`                                                             |
| `+0x83` | u32       | unknown_83 | Same entries; roughly inverse to `unknown_3b` (`unknown_3b x unknown_83` mostly 900-1,200 million), capped at `1,000,000` on all 119 entries with `unknown_3b = 900`; unaligned |

### `itemsubgroupoffset.dbss`

Standard PABR offset companion with 10-byte rows, read by `parse_pabr_offset_rows` (`handlers/_common/pabr_offset.py`).

| Offset      | Type                     | Field              | Notes                                      |
| ----------- | ------------------------ | ------------------ | ------------------------------------------ |
| `+0x00`     | char[4]                  | magic              | ASCII `PABR`                               |
| `+0x04`     | u32                      | record_count       | Equals `itemsubgroup.dbss` `record_count`  |
| `+0x08`     | Offset Row[record_count] | rows               | See Offset Row                             |
| `rows+0x00` | u32                      | unknown_trailer_00 | Always `0`                                 |
| `rows+0x04` | u32                      | end_of_rows        | Equals `8 + count * 10` (`166,908`)        |
| `rows+0x08` | u32                      | unknown_trailer_08 | Always `0`                                 |

The 12-byte trailer is the same shape as the `itemenchantoffset.dbss` one.

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                               |
| ------- | ---- | ----------- | --------------------------------------------------- |
| `+0x00` | u16  | record_id   | Subgroup key; equals the record's `subgroup_key`    |
| `+0x02` | u32  | data_offset | Absolute offset of the record, at its inline key    |
| `+0x06` | u32  | data_size   | Record byte count, `18 + 135 * entry_count`         |

Subgroup keys are u16 in the index, so no key above `65535` exists.

## `item_key` Packing

```text
item_id = item_key & 0xFFFFFF
enchant_level = item_key >> 24
```

`enchant_level` is `0` on 95,166 entries and `1`-`20` on the other 2,642: the entry hands out the item at that enhancement level. All 2,642 non-zero keys exist as `itemenchant.dbss` keys, and the levels fit the items: Manos Necklace at `1`-`5` (PRI to PEN), Kzarka Longsword at `15`, Blackstar Helmet at `19` (TET), Dim Tree Spirit's Armor at `20` (PEN).

## Notes

- Worker production subgroups use one entry shape only: `enchant_level=0`, `select_rate=1,000,000`, every other field zero (815 entries in 364 subgroups). 278 of their 281 distinct item IDs have an English LOC type 0 name; 4016, 4017 and 4415 have none.
- Subgroup 55000 (246 entries) lists trade goods: crates such as Pepper Crate (7401) and Garlic Crate (7402), packaged dried fish such as Packaged Dried Dace (55947), and items such as Mansha Goblin Mask (55026), and 54001 holds one entry (item 55151). They are the only subgroups that set `unknown_37` to `unknown_83`; the i64 fields look like a price range (`unknown_43 < unknown_3b < unknown_4b`), but that is not confirmed.
- The largest subgroups are 52001 (11,560 entries), 32001 (707) and 52003 (391).
- The 36 subgroup keys that `plantzone.dbss` zones reach but this index lacks (41208-41212, 43183-43195, 44059, 44060, 44860-44874, 45018) have no record in `bartersubgroup.bss` or `limiteditemsubgroup.bss` either (45018 matches bytes in `limiteditemsubgroup.bss` only inside unrelated rows). They are item exchange keys, not subgroup keys: each exchange's drop key is an [`itemmaingroup.bss`](itemmaingroup_bss.md) group, which lists the subgroups (see [`plantexchangegroup.bss` Field Names](plantexchangegroup_bss.md#field-names)). 44059 and 44060 are also group IDs themselves, pointing at subgroups 42339 and 42340 (client 3464).

## Field Names

The entry fields are named from two sources. The 2016 client (build of 2016-01-11) ships with debug symbols, and its `gc::ItemGroupValue` holds `_itemKey`, `_selectRate`, a condition, `_isPetAddDrop`, `_minCount` (i64), `_maxCount` (i64), `_intimacy`, `_explorationExperience`, `_isApplyRandomPrice`, four more flags, nine i64 stock fields (`_needAmountForStock`, `_minRemainAmountForStock`, `_maxRemainAmountForStock`, `_variedAmountPerTickForStock`, `_tradingCountUnitForStock`, `_maxCountOfBuyFromNpcForStock`, `_reverseAmountForStock`, `_minSteadyAmountForStock`, `_maxSteadyAmountForStock`) and `_experience`. Its `gc::ItemSubGroupStaticStatus` keeps a `_totalPercent` next to the entry list, which is why `select_rate` reads as a weight against the subgroup's total. The server-side `ItemSubGroup_Table` of a private server on client 519 has one row per subgroup, item and enchant level; 23,750 of them match an entry of client 3464:

| Field                 | `ItemSubGroup_Table` column | Matching rows                                    |
| --------------------- | --------------------------- | ------------------------------------------------ |
| `item_key` low 24 bits, high byte | `ItemKey`, `EnchantLevel` | the join key                             |
| select_rate           | `SelectRate_0`              | 17,594 of 23,730 non-zero; the server also stores weights above one million (up to `3,000,000` on 1,648 rows) |
| intimacy_variation    | `IntimacyVariation`         | 964 of 964 non-zero                              |
| is_apply_random_price | `ApplyRandomPrice`          | 18 of 18 non-zero                                |
| rent_time             | `RentTime`                  | 3 of 3 non-zero                                  |
| min_count, max_count  | `MinCount_0`, `MaxCount_0`  | 6,720 rows where the server has `-1`; where the server has a count (`1`, `20` to `40` ...) this file stores `0` |

`min_count` and `max_count` sit where the 2016 struct has `_minCount` and `_maxCount`, just before `_intimacy`, and hold the server's `-1`. The server's counts above zero are not in the client file.

## Open Questions

### Subgroup 55000 Fields

The trade goods entries set a block of i64 values that behave like a price band around `unknown_3b`: the top is always 130%, the floor is one of five shares per item group (Ancient coins 30%; Garlic, Onion, Grape crates and most dried fish 65%; Pepper, Strawberry crates 75%; Potato, Barley, Wheat crates 85%; Witch's Poison Herb and some dried fish 95%), and `unknown_5b` is a 1% step. The trade sell price is `Base Value x Distance Bonus x Trading Bonus x Bargain - Material Cost`, so `unknown_3b` would be the original Base Value and the band the range the current Base Value moves in; In-Game Checks has the test. What `unknown_53`, `unknown_26` and `unknown_83` control is open. `unknown_53` looks like a price swing size with a direction set per row. These entries leave `select_rate` at `0` and set `unknown_83` instead, so `unknown_83` may play the same role: a per-item weight, higher for cheaper goods. The 2016 stock fields (see Field Names) are nine i64 values in the same part of the entry; `unknown_3b`, `unknown_43`, `unknown_4b` and `unknown_53` may be the first four (need amount, minimum and maximum remain amount, varied amount per tick), but no server column holds them, so they keep their offsets.

## In-Game Checks

### Subgroup 55000 Price Band

Needs item (all):

- [Pepper Crate](https://bdocodex.com/us/item/7401/)
- [Ancient Gold Coin](https://bdocodex.com/us/item/55001/)

Needs NPC: any Trade Manager

Pepper Crate stores `unknown_3b` 1,800, `unknown_43` 1,350 (75%) and `unknown_4b` 2,340 (130%); Ancient Gold Coin stores 900, 270 (30%) and 1,170. Read the current Base Value the Trade Manager shows for both over several days. If Pepper Crate stays between 1,350 and 2,340 and Ancient Gold Coin drops below 585 (65% of 900), `unknown_3b` is the original Base Value and `unknown_43` and `unknown_4b` are the floor and ceiling of the current one. A Pepper Crate price outside 1,350 to 2,340 rules the band out.
