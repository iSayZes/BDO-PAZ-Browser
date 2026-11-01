# `uifusionskilltreelayout.bss` Format

## Purpose

The fusion skill grid of the skill window: a 5 by 2 grid with three skill
cells, each holding skill number `0` (clients 1784 and 3482, the same file
on both). The skill window reads it through `getFusionSkillTree()` and asks
the client for the fusion skills of each skill cell by its index, so the
cells only count the fusion skill lists (see Client Use).

Same layout as [`uiguildskilltreelayout.bss`](uiguildskilltreelayout_bss.md), read by the same handler: a `PABR` header with the grid's width and height, `width * height` 4-byte cells column by column, an empty string table and the 8-byte trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                          | Bytes | Records | Row bytes |
| ------ | ------------- | ----------------------------- | ----- | ------- | --------- |
| 2      | 805 and later | `uifusionskilltreelayout.bss` | 64    | 10 Cell | 4         |
| 1      | 485 to 794    | `uifusionskilltreelayout.bss` | 32    | 6 Cell  | 4         |

| Layout | File                          | Known         | Unknown    |
| ------ | ----------------------------- | ------------- | ---------- |
| 2      | `uifusionskilltreelayout.bss` | 64 B (100.0%) | 0 B (0.0%) |
| 1      | `uifusionskilltreelayout.bss` | 32 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `07f96aabc438`  |
| 3482   | Layout 2 | `07f96aabc438`  |
| 3474   | Layout 2 | `07f96aabc438`  |
| 3473   | Layout 2 | `07f96aabc438`  |
| 3464   | Layout 2 | `07f96aabc438`  |
| 3458   | Layout 2 | `07f96aabc438`  |
| 3454   | Layout 2 | `07f96aabc438`  |
| 3444   | Layout 2 | `07f96aabc438`  |
| 3435   | Layout 2 | `07f96aabc438`  |
| 3426   | Layout 2 | `07f96aabc438`  |
| 3418   | Layout 2 | `07f96aabc438`  |
| 3412   | Layout 2 | `07f96aabc438`  |
| 3402   | Layout 2 | `07f96aabc438`  |
| 3396   | Layout 2 | `07f96aabc438`  |
| 3387   | Layout 2 | `07f96aabc438`  |
| 3381   | Layout 2 | `07f96aabc438`  |
| 3373   | Layout 2 | `07f96aabc438`  |
| 3364   | Layout 2 | `07f96aabc438`  |
| 3356   | Layout 2 | `07f96aabc438`  |
| 3349   | Layout 2 | `07f96aabc438`  |
| 3342   | Layout 2 | `07f96aabc438`  |
| 3335   | Layout 2 | `07f96aabc438`  |
| 3326   | Layout 2 | `07f96aabc438`  |
| 3321   | Layout 2 | `07f96aabc438`  |
| 3314   | Layout 2 | `07f96aabc438`  |
| 3303   | Layout 2 | `07f96aabc438`  |
| 3302   | Layout 2 | `07f96aabc438`  |
| 3293   | Layout 2 | `07f96aabc438`  |
| 3283   | Layout 2 | `07f96aabc438`  |
| 3275   | Layout 2 | `07f96aabc438`  |
| 3267   | Layout 2 | `07f96aabc438`  |
| 3258   | Layout 2 | `07f96aabc438`  |
| 3251   | Layout 2 | `07f96aabc438`  |
| 3242   | Layout 2 | `07f96aabc438`  |
| 3235   | Layout 2 | `07f96aabc438`  |
| 3229   | Layout 2 | `07f96aabc438`  |
| 3212   | Layout 2 | `07f96aabc438`  |
| 3203   | Layout 2 | `07f96aabc438`  |
| 3193   | Layout 2 | `07f96aabc438`  |
| 3186   | Layout 2 | `07f96aabc438`  |
| 3177   | Layout 2 | `07f96aabc438`  |
| 3169   | Layout 2 | `07f96aabc438`  |
| 3158   | Layout 2 | `07f96aabc438`  |
| 3151   | Layout 2 | `07f96aabc438`  |
| 3144   | Layout 2 | `07f96aabc438`  |
| 3133   | Layout 2 | `07f96aabc438`  |
| 3125   | Layout 2 | `07f96aabc438`  |
| 3118   | Layout 2 | `07f96aabc438`  |
| 3111   | Layout 2 | `07f96aabc438`  |
| 3103   | Layout 2 | `07f96aabc438`  |
| 3095   | Layout 2 | `07f96aabc438`  |
| 3086   | Layout 2 | `07f96aabc438`  |
| 3072   | Layout 2 | `07f96aabc438`  |
| 3062   | Layout 2 | `07f96aabc438`  |
| 3052   | Layout 2 | `07f96aabc438`  |
| 3045   | Layout 2 | `07f96aabc438`  |
| 3037   | Layout 2 | `07f96aabc438`  |
| 3030   | Layout 2 | `07f96aabc438`  |
| 3021   | Layout 2 | `07f96aabc438`  |
| 3012   | Layout 2 | `07f96aabc438`  |
| 3002   | Layout 2 | `07f96aabc438`  |
| 2995   | Layout 2 | `07f96aabc438`  |
| 2987   | Layout 2 | `07f96aabc438`  |
| 2978   | Layout 2 | `07f96aabc438`  |
| 2970   | Layout 2 | `07f96aabc438`  |
| 2959   | Layout 2 | `07f96aabc438`  |
| 2951   | Layout 2 | `07f96aabc438`  |
| 2942   | Layout 2 | `07f96aabc438`  |
| 2935   | Layout 2 | `07f96aabc438`  |
| 2932   | Layout 2 | `07f96aabc438`  |
| 2923   | Layout 2 | `07f96aabc438`  |
| 2919   | Layout 2 | `07f96aabc438`  |
| 2907   | Layout 2 | `07f96aabc438`  |
| 2900   | Layout 2 | `07f96aabc438`  |
| 2891   | Layout 2 | `07f96aabc438`  |
| 2882   | Layout 2 | `07f96aabc438`  |
| 2872   | Layout 2 | `07f96aabc438`  |
| 2863   | Layout 2 | `07f96aabc438`  |
| 2855   | Layout 2 | `07f96aabc438`  |
| 2849   | Layout 2 | `07f96aabc438`  |
| 2844   | Layout 2 | `07f96aabc438`  |
| 2834   | Layout 2 | `07f96aabc438`  |
| 2825   | Layout 2 | `07f96aabc438`  |
| 2819   | Layout 2 | `07f96aabc438`  |
| 2811   | Layout 2 | `07f96aabc438`  |
| 2803   | Layout 2 | `07f96aabc438`  |
| 2794   | Layout 2 | `07f96aabc438`  |
| 2783   | Layout 2 | `07f96aabc438`  |
| 2774   | Layout 2 | `07f96aabc438`  |
| 2765   | Layout 2 | `07f96aabc438`  |
| 2756   | Layout 2 | `07f96aabc438`  |
| 2750   | Layout 2 | `07f96aabc438`  |
| 2743   | Layout 2 | `07f96aabc438`  |
| 2736   | Layout 2 | `07f96aabc438`  |
| 2726   | Layout 2 | `07f96aabc438`  |
| 2717   | Layout 2 | `07f96aabc438`  |
| 2709   | Layout 2 | `07f96aabc438`  |
| 2703   | Layout 2 | `07f96aabc438`  |
| 2695   | Layout 2 | `07f96aabc438`  |
| 2684   | Layout 2 | `07f96aabc438`  |
| 2672   | Layout 2 | `07f96aabc438`  |
| 2665   | Layout 2 | `07f96aabc438`  |
| 2657   | Layout 2 | `07f96aabc438`  |
| 2649   | Layout 2 | `07f96aabc438`  |
| 2644   | Layout 2 | `07f96aabc438`  |
| 2637   | Layout 2 | `07f96aabc438`  |
| 2629   | Layout 2 | `07f96aabc438`  |
| 2619   | Layout 2 | `07f96aabc438`  |
| 2612   | Layout 2 | `07f96aabc438`  |
| 2606   | Layout 2 | `07f96aabc438`  |
| 2602   | Layout 2 | `07f96aabc438`  |
| 2601   | Layout 2 | `07f96aabc438`  |
| 2592   | Layout 2 | `07f96aabc438`  |
| 2583   | Layout 2 | `07f96aabc438`  |
| 2575   | Layout 2 | `07f96aabc438`  |
| 2567   | Layout 2 | `07f96aabc438`  |
| 2560   | Layout 2 | `07f96aabc438`  |
| 2553   | Layout 2 | `07f96aabc438`  |
| 2545   | Layout 2 | `07f96aabc438`  |
| 2538   | Layout 2 | `07f96aabc438`  |
| 2529   | Layout 2 | `07f96aabc438`  |
| 2519   | Layout 2 | `07f96aabc438`  |
| 2513   | Layout 2 | `07f96aabc438`  |
| 2510   | Layout 2 | `07f96aabc438`  |
| 2507   | Layout 2 | `07f96aabc438`  |
| 2503   | Layout 2 | `07f96aabc438`  |
| 2498   | Layout 2 | `07f96aabc438`  |
| 2492   | Layout 2 | `07f96aabc438`  |
| 2487   | Layout 2 | `07f96aabc438`  |
| 2480   | Layout 2 | `07f96aabc438`  |
| 2474   | Layout 2 | `07f96aabc438`  |
| 2468   | Layout 2 | `07f96aabc438`  |
| 2460   | Layout 2 | `07f96aabc438`  |
| 2453   | Layout 2 | `07f96aabc438`  |
| 2444   | Layout 2 | `07f96aabc438`  |
| 2438   | Layout 2 | `07f96aabc438`  |
| 2434   | Layout 2 | `07f96aabc438`  |
| 2429   | Layout 2 | `07f96aabc438`  |
| 2421   | Layout 2 | `07f96aabc438`  |
| 2414   | Layout 2 | `07f96aabc438`  |
| 2407   | Layout 2 | `07f96aabc438`  |
| 2401   | Layout 2 | `07f96aabc438`  |
| 2397   | Layout 2 | `07f96aabc438`  |
| 2393   | Layout 2 | `07f96aabc438`  |
| 2384   | Layout 2 | `07f96aabc438`  |
| 2378   | Layout 2 | `07f96aabc438`  |
| 2372   | Layout 2 | `07f96aabc438`  |
| 2358   | Layout 2 | `07f96aabc438`  |
| 2352   | Layout 2 | `07f96aabc438`  |
| 2347   | Layout 2 | `07f96aabc438`  |
| 2343   | Layout 2 | `07f96aabc438`  |
| 2335   | Layout 2 | `07f96aabc438`  |
| 2327   | Layout 2 | `07f96aabc438`  |
| 2324   | Layout 2 | `07f96aabc438`  |
| 2319   | Layout 2 | `07f96aabc438`  |
| 2313   | Layout 2 | `07f96aabc438`  |
| 2308   | Layout 2 | `07f96aabc438`  |
| 2302   | Layout 2 | `07f96aabc438`  |
| 2295   | Layout 2 | `07f96aabc438`  |
| 2290   | Layout 2 | `07f96aabc438`  |
| 2284   | Layout 2 | `07f96aabc438`  |
| 2276   | Layout 2 | `07f96aabc438`  |
| 2269   | Layout 2 | `07f96aabc438`  |
| 2259   | Layout 2 | `07f96aabc438`  |
| 2250   | Layout 2 | `07f96aabc438`  |
| 2243   | Layout 2 | `07f96aabc438`  |
| 2235   | Layout 2 | `07f96aabc438`  |
| 2229   | Layout 2 | `07f96aabc438`  |
| 2224   | Layout 2 | `07f96aabc438`  |
| 2218   | Layout 2 | `07f96aabc438`  |
| 2215   | Layout 2 | `07f96aabc438`  |
| 2207   | Layout 2 | `07f96aabc438`  |
| 2203   | Layout 2 | `07f96aabc438`  |
| 2196   | Layout 2 | `07f96aabc438`  |
| 2192   | Layout 2 | `07f96aabc438`  |
| 2189   | Layout 2 | `07f96aabc438`  |
| 2183   | Layout 2 | `07f96aabc438`  |
| 2179   | Layout 2 | `07f96aabc438`  |
| 2171   | Layout 2 | `07f96aabc438`  |
| 2163   | Layout 2 | `07f96aabc438`  |
| 2156   | Layout 2 | `07f96aabc438`  |
| 2151   | Layout 2 | `07f96aabc438`  |
| 2147   | Layout 2 | `07f96aabc438`  |
| 2142   | Layout 2 | `07f96aabc438`  |
| 2138   | Layout 2 | `07f96aabc438`  |
| 2134   | Layout 2 | `07f96aabc438`  |
| 2130   | Layout 2 | `07f96aabc438`  |
| 2122   | Layout 2 | `07f96aabc438`  |
| 2107   | Layout 2 | `07f96aabc438`  |
| 2098   | Layout 2 | `07f96aabc438`  |
| 2089   | Layout 2 | `07f96aabc438`  |
| 2081   | Layout 2 | `07f96aabc438`  |
| 2073   | Layout 2 | `07f96aabc438`  |
| 2067   | Layout 2 | `07f96aabc438`  |
| 2063   | Layout 2 | `07f96aabc438`  |
| 2059   | Layout 2 | `07f96aabc438`  |
| 2052   | Layout 2 | `07f96aabc438`  |
| 2044   | Layout 2 | `07f96aabc438`  |
| 2039   | Layout 2 | `07f96aabc438`  |
| 2032   | Layout 2 | `07f96aabc438`  |
| 2025   | Layout 2 | `07f96aabc438`  |
| 2011   | Layout 2 | `07f96aabc438`  |
| 2005   | Layout 2 | `07f96aabc438`  |
| 2000   | Layout 2 | `07f96aabc438`  |
| 1996   | Layout 2 | `07f96aabc438`  |
| 1991   | Layout 2 | `07f96aabc438`  |
| 1985   | Layout 2 | `07f96aabc438`  |
| 1980   | Layout 2 | `07f96aabc438`  |
| 1969   | Layout 2 | `07f96aabc438`  |
| 1964   | Layout 2 | `07f96aabc438`  |
| 1958   | Layout 2 | `07f96aabc438`  |
| 1950   | Layout 2 | `07f96aabc438`  |
| 1945   | Layout 2 | `07f96aabc438`  |
| 1937   | Layout 2 | `07f96aabc438`  |
| 1933   | Layout 2 | `07f96aabc438`  |
| 1927   | Layout 2 | `07f96aabc438`  |
| 1921   | Layout 2 | `07f96aabc438`  |
| 1914   | Layout 2 | `07f96aabc438`  |
| 1908   | Layout 2 | `07f96aabc438`  |
| 1897   | Layout 2 | `07f96aabc438`  |
| 1892   | Layout 2 | `07f96aabc438`  |
| 1886   | Layout 2 | `07f96aabc438`  |
| 1881   | Layout 2 | `07f96aabc438`  |
| 1871   | Layout 2 | `07f96aabc438`  |
| 1866   | Layout 2 | `07f96aabc438`  |
| 1862   | Layout 2 | `07f96aabc438`  |
| 1854   | Layout 2 | `07f96aabc438`  |
| 1846   | Layout 2 | `07f96aabc438`  |
| 1838   | Layout 2 | `07f96aabc438`  |
| 1832   | Layout 2 | `07f96aabc438`  |
| 1826   | Layout 2 | `07f96aabc438`  |
| 1822   | Layout 2 | `07f96aabc438`  |
| 1818   | Layout 2 | `07f96aabc438`  |
| 1804   | Layout 2 | `07f96aabc438`  |
| 1794   | Layout 2 | `07f96aabc438`  |
| 1790   | Layout 2 | `07f96aabc438`  |
| 1784   | Layout 2 | `07f96aabc438`  |
| 1774   | Layout 2 | `07f96aabc438`  |
| 1771   | Layout 2 | `07f96aabc438`  |
| 1762   | Layout 2 | `07f96aabc438`  |
| 1759   | Layout 2 | `07f96aabc438`  |
| 1754   | Layout 2 | `07f96aabc438`  |
| 1749   | Layout 2 | `07f96aabc438`  |
| 1743   | Layout 2 | `07f96aabc438`  |
| 1737   | Layout 2 | `07f96aabc438`  |
| 1731   | Layout 2 | `07f96aabc438`  |
| 1725   | Layout 2 | `07f96aabc438`  |
| 1717   | Layout 2 | `07f96aabc438`  |
| 1710   | Layout 2 | `07f96aabc438`  |
| 1704   | Layout 2 | `07f96aabc438`  |
| 1698   | Layout 2 | `07f96aabc438`  |
| 1690   | Layout 2 | `07f96aabc438`  |
| 1685   | Layout 2 | `07f96aabc438`  |
| 1680   | Layout 2 | `07f96aabc438`  |
| 1674   | Layout 2 | `07f96aabc438`  |
| 1668   | Layout 2 | `07f96aabc438`  |
| 1659   | Layout 2 | `07f96aabc438`  |
| 1649   | Layout 2 | `07f96aabc438`  |
| 1642   | Layout 2 | `07f96aabc438`  |
| 1636   | Layout 2 | `07f96aabc438`  |
| 1628   | Layout 2 | `07f96aabc438`  |
| 1622   | Layout 2 | `07f96aabc438`  |
| 1614   | Layout 2 | `07f96aabc438`  |
| 1608   | Layout 2 | `07f96aabc438`  |
| 1602   | Layout 2 | `07f96aabc438`  |
| 1598   | Layout 2 | `07f96aabc438`  |
| 1594   | Layout 2 | `07f96aabc438`  |
| 1590   | Layout 2 | `07f96aabc438`  |
| 1587   | Layout 2 | `07f96aabc438`  |
| 1584   | Layout 2 | `07f96aabc438`  |
| 1579   | Layout 2 | `07f96aabc438`  |
| 1572   | Layout 2 | `07f96aabc438`  |
| 1565   | Layout 2 | `07f96aabc438`  |
| 1559   | Layout 2 | `07f96aabc438`  |
| 1554   | Layout 2 | `07f96aabc438`  |
| 1547   | Layout 2 | `07f96aabc438`  |
| 1537   | Layout 2 | `07f96aabc438`  |
| 1529   | Layout 2 | `07f96aabc438`  |
| 1524   | Layout 2 | `07f96aabc438`  |
| 1519   | Layout 2 | `07f96aabc438`  |
| 1509   | Layout 2 | `07f96aabc438`  |
| 1506   | Layout 2 | `07f96aabc438`  |
| 1504   | Layout 2 | `07f96aabc438`  |
| 1500   | Layout 2 | `07f96aabc438`  |
| 1493   | Layout 2 | `07f96aabc438`  |
| 1489   | Layout 2 | `07f96aabc438`  |
| 1485   | Layout 2 | `07f96aabc438`  |
| 1481   | Layout 2 | `07f96aabc438`  |
| 1474   | Layout 2 | `07f96aabc438`  |
| 1466   | Layout 2 | `07f96aabc438`  |
| 1462   | Layout 2 | `07f96aabc438`  |
| 1459   | Layout 2 | `07f96aabc438`  |
| 1453   | Layout 2 | `07f96aabc438`  |
| 1450   | Layout 2 | `07f96aabc438`  |
| 1445   | Layout 2 | `07f96aabc438`  |
| 1439   | Layout 2 | `07f96aabc438`  |
| 1433   | Layout 2 | `07f96aabc438`  |
| 1430   | Layout 2 | `07f96aabc438`  |
| 1426   | Layout 2 | `07f96aabc438`  |
| 1421   | Layout 2 | `07f96aabc438`  |
| 1417   | Layout 2 | `07f96aabc438`  |
| 1416   | Layout 2 | `07f96aabc438`  |
| 1409   | Layout 2 | `07f96aabc438`  |
| 1405   | Layout 2 | `07f96aabc438`  |
| 1401   | Layout 2 | `07f96aabc438`  |
| 1396   | Layout 2 | `07f96aabc438`  |
| 1391   | Layout 2 | `07f96aabc438`  |
| 1390   | Layout 2 | `07f96aabc438`  |
| 1386   | Layout 2 | `07f96aabc438`  |
| 1381   | Layout 2 | `07f96aabc438`  |
| 1379   | Layout 2 | `07f96aabc438`  |
| 1372   | Layout 2 | `07f96aabc438`  |
| 1366   | Layout 2 | `07f96aabc438`  |
| 1364   | Layout 2 | `07f96aabc438`  |
| 1363   | Layout 2 | `07f96aabc438`  |
| 1360   | Layout 2 | `07f96aabc438`  |
| 1358   | Layout 2 | `07f96aabc438`  |
| 1355   | Layout 2 | `07f96aabc438`  |
| 1351   | Layout 2 | `07f96aabc438`  |
| 1348   | Layout 2 | `07f96aabc438`  |
| 1346   | Layout 2 | `07f96aabc438`  |
| 1341   | Layout 2 | `07f96aabc438`  |
| 1340   | Layout 2 | `07f96aabc438`  |
| 1338   | Layout 2 | `07f96aabc438`  |
| 1335   | Layout 2 | `07f96aabc438`  |
| 1333   | Layout 2 | `07f96aabc438`  |
| 1329   | Layout 2 | `07f96aabc438`  |
| 1327   | Layout 2 | `07f96aabc438`  |
| 1324   | Layout 2 | `07f96aabc438`  |
| 1321   | Layout 2 | `07f96aabc438`  |
| 1319   | Layout 2 | `07f96aabc438`  |
| 1318   | Layout 2 | `07f96aabc438`  |
| 1316   | Layout 2 | `07f96aabc438`  |
| 1313   | Layout 2 | `07f96aabc438`  |
| 1311   | Layout 2 | `07f96aabc438`  |
| 1309   | Layout 2 | `07f96aabc438`  |
| 1304   | Layout 2 | `07f96aabc438`  |
| 1292   | Layout 2 | `07f96aabc438`  |
| 1286   | Layout 2 | `07f96aabc438`  |
| 1280   | Layout 2 | `07f96aabc438`  |
| 1276   | Layout 2 | `07f96aabc438`  |
| 1267   | Layout 2 | `07f96aabc438`  |
| 1261   | Layout 2 | `07f96aabc438`  |
| 1256   | Layout 2 | `07f96aabc438`  |
| 1250   | Layout 2 | `07f96aabc438`  |
| 1246   | Layout 2 | `07f96aabc438`  |
| 1239   | Layout 2 | `07f96aabc438`  |
| 1230   | Layout 2 | `07f96aabc438`  |
| 1226   | Layout 2 | `07f96aabc438`  |
| 1220   | Layout 2 | `07f96aabc438`  |
| 1217   | Layout 2 | `07f96aabc438`  |
| 1211   | Layout 2 | `07f96aabc438`  |
| 1210   | Layout 2 | `07f96aabc438`  |
| 1208   | Layout 2 | `07f96aabc438`  |
| 1203   | Layout 2 | `07f96aabc438`  |
| 1197   | Layout 2 | `07f96aabc438`  |
| 1194   | Layout 2 | `07f96aabc438`  |
| 1192   | Layout 2 | `07f96aabc438`  |
| 1187   | Layout 2 | `07f96aabc438`  |
| 1183   | Layout 2 | `07f96aabc438`  |
| 1177   | Layout 2 | `07f96aabc438`  |
| 1173   | Layout 2 | `07f96aabc438`  |
| 1167   | Layout 2 | `07f96aabc438`  |
| 1164   | Layout 2 | `07f96aabc438`  |
| 1156   | Layout 2 | `07f96aabc438`  |
| 1149   | Layout 2 | `07f96aabc438`  |
| 1144   | Layout 2 | `07f96aabc438`  |
| 1137   | Layout 2 | `07f96aabc438`  |
| 1132   | Layout 2 | `07f96aabc438`  |
| 1127   | Layout 2 | `07f96aabc438`  |
| 1122   | Layout 2 | `07f96aabc438`  |
| 1118   | Layout 2 | `07f96aabc438`  |
| 1114   | Layout 2 | `07f96aabc438`  |
| 1109   | Layout 2 | `07f96aabc438`  |
| 1102   | Layout 2 | `07f96aabc438`  |
| 1096   | Layout 2 | `07f96aabc438`  |
| 1088   | Layout 2 | `07f96aabc438`  |
| 1081   | Layout 2 | `07f96aabc438`  |
| 1076   | Layout 2 | `07f96aabc438`  |
| 1069   | Layout 2 | `07f96aabc438`  |
| 1064   | Layout 2 | `07f96aabc438`  |
| 1058   | Layout 2 | `07f96aabc438`  |
| 1051   | Layout 2 | `07f96aabc438`  |
| 1044   | Layout 2 | `07f96aabc438`  |
| 1036   | Layout 2 | `07f96aabc438`  |
| 1026   | Layout 2 | `07f96aabc438`  |
| 1016   | Layout 2 | `07f96aabc438`  |
| 1009   | Layout 2 | `07f96aabc438`  |
| 1005   | Layout 2 | `07f96aabc438`  |
| 1000   | Layout 2 | `07f96aabc438`  |
| 998    | Layout 2 | `07f96aabc438`  |
| 990    | Layout 2 | `07f96aabc438`  |
| 979    | Layout 2 | `07f96aabc438`  |
| 972    | Layout 2 | `07f96aabc438`  |
| 963    | Layout 2 | `07f96aabc438`  |
| 955    | Layout 2 | `07f96aabc438`  |
| 946    | Layout 2 | `07f96aabc438`  |
| 938    | Layout 2 | `07f96aabc438`  |
| 927    | Layout 2 | `07f96aabc438`  |
| 911    | Layout 2 | `07f96aabc438`  |
| 904    | Layout 2 | `07f96aabc438`  |
| 899    | Layout 2 | `07f96aabc438`  |
| 894    | Layout 2 | `07f96aabc438`  |
| 885    | Layout 2 | `07f96aabc438`  |
| 879    | Layout 2 | `07f96aabc438`  |
| 872    | Layout 2 | `07f96aabc438`  |
| 864    | Layout 2 | `07f96aabc438`  |
| 855    | Layout 2 | `07f96aabc438`  |
| 853    | Layout 2 | `07f96aabc438`  |
| 845    | Layout 2 | `07f96aabc438`  |
| 837    | Layout 2 | `07f96aabc438`  |
| 829    | Layout 2 | `07f96aabc438`  |
| 822    | Layout 2 | `07f96aabc438`  |
| 814    | Layout 2 | `07f96aabc438`  |
| 805    | Layout 2 | `07f96aabc438`  |
| 794    | Layout 1 | `07f96aabc438`  |
| 787    | Layout 1 | `07f96aabc438`  |
| 780    | Layout 1 | `07f96aabc438`  |
| 771    | Layout 1 | `07f96aabc438`  |
| 760    | Layout 1 | `07f96aabc438`  |
| 748    | Layout 1 | `07f96aabc438`  |
| 741    | Layout 1 | `07f96aabc438`  |
| 736    | Layout 1 | `07f96aabc438`  |
| 731    | Layout 1 | `07f96aabc438`  |
| 723    | Layout 1 | `07f96aabc438`  |
| 711    | Layout 1 | `07f96aabc438`  |
| 707    | Layout 1 | `07f96aabc438`  |
| 697    | Layout 1 | `07f96aabc438`  |
| 689    | Layout 1 | `07f96aabc438`  |
| 683    | Layout 1 | `07f96aabc438`  |
| 678    | Layout 1 | `07f96aabc438`  |
| 670    | Layout 1 | `07f96aabc438`  |
| 661    | Layout 1 | `07f96aabc438`  |
| 656    | Layout 1 | `07f96aabc438`  |
| 652    | Layout 1 | `07f96aabc438`  |
| 643    | Layout 1 | `07f96aabc438`  |
| 637    | Layout 1 | `07f96aabc438`  |
| 630    | Layout 1 | `07f96aabc438`  |
| 627    | Layout 1 | `07f96aabc438`  |
| 621    | Layout 1 | `07f96aabc438`  |
| 617    | Layout 1 | `07f96aabc438`  |
| 615    | Layout 1 | `07f96aabc438`  |
| 606    | Layout 1 | `07f96aabc438`  |
| 599    | Layout 1 | `07f96aabc438`  |
| 592    | Layout 1 | `07f96aabc438`  |
| 586    | Layout 1 | `07f96aabc438`  |
| 577    | Layout 1 | `07f96aabc438`  |
| 569    | Layout 1 | `07f96aabc438`  |
| 561    | Layout 1 | `07f96aabc438`  |
| 554    | Layout 1 | `07f96aabc438`  |
| 542    | Layout 1 | `07f96aabc438`  |
| 532    | Layout 1 | `07f96aabc438`  |
| 531    | Layout 1 | `07f96aabc438`  |
| 526    | Layout 1 | `07f96aabc438`  |
| 521    | Layout 1 | `07f96aabc438`  |
| 517    | Layout 1 | `07f96aabc438`  |
| 510    | Layout 1 | `07f96aabc438`  |
| 508    | Layout 1 | `07f96aabc438`  |
| 504    | Layout 1 | `07f96aabc438`  |
| 497    | Layout 1 | `07f96aabc438`  |
| 491    | Layout 1 | `07f96aabc438`  |
| 485    | Layout 1 | `07f96aabc438`  |
| 478    | No file  | `07f96aabc438`  |
| 472    | No file  | `07f96aabc438`  |
| 466    | No file  | `07f96aabc438`  |
| 457    | No file  | `07f96aabc438`  |
| 452    | No file  | `07f96aabc438`  |
| 449    | No file  | `07f96aabc438`  |
| 435    | No file  | `07f96aabc438`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Client Use

`Window_SkillInfo:GetFusionSkillFromCell()` in `panel_window_skill_renew.luac`
(client 3482) walks the grid row by row and counts the skill cells from
`0`. For the `n`-th skill cell it asks `ToClient_getFusionSkillListCount(n)`
and, for each entry, `ToClient_getFusionSkillNo(n, i)`,
`ToClient_getFusionMainSkillNo(n, i)` and `ToClient_getFusionSubSkillNo(n, i)`.
The cell's own `skill_no` is not read.
`panel_window_skill_global.luac`, `panel_window_skill_cooltimeslot.luac`,
`panel_window_skillgroup_cooltimeslot_1.luac` and
`panel_quickmenusetting.luac` call `getFusionSkillTree()` too.

The three skill cells sit in row `0`, columns `0`, `2` and `4`, so `n` runs
from `0` to `2`. [`skillfusionslotlist.bss`](skillfusionslotlist_bss.md)
fills slots `0` to `2` for every class on client 3482 and leaves `3` and `4`
empty, which matches three cells; the Lua does not name `n` a slot.

## Notes

- The source sheet `FusionSkill` of a private server's
  `uifusionskilltreelayout.xlsm` on client 1784 holds `0` in A1, C1 and E1
  (see [`uiguildskilltreelayout.bss` Field Names](uiguildskilltreelayout_bss.md#field-names)).
