# `limiteditemsubgroup.bss` Format

## Purpose

The purchase limits of shop items: one row per item subgroup, each a list
of the items in it that a character or family can buy only so many times
before a reset. Every `subgroup_key` is an
[`itemsubgroup.dbss`](../dbss/itemsubgroup_dbss.md) key (53 of 53 on client 3482).
The NPC shop Lua (`panel_dialog_npcshop_all_1.luac`) shows a limited item
through the shop item wrapper's `isLimitedBuyableCount()`,
`getRemainingCount()`, `getBuyableMaxCount()`, `getResetType()` and
`isLimitedByUser()`, and picks the `LUA_LIMITEDITEMSHOP_FAMILY_*` or
`LUA_LIMITEDITEMSHOP_CHARACTER_*` text by the last one.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------------------------- | ------ | ----------------- | --------- |
| 2      | 1321 and later | `limiteditemsubgroup.bss` | 11,512 | 705 Entry, 53 Row | 16        |
| 1      | 1327 to 1590   | `limiteditemsubgroup.bss` | 3,376  | 273 Entry, 20 Row | 12        |

| Layout | File                      | Known            | Unknown         |
| ------ | ------------------------- | ---------------- | --------------- |
| 2      | `limiteditemsubgroup.bss` | 8,692 B (75.5%)  | 2,820 B (24.5%) |
| 1      | `limiteditemsubgroup.bss` | 3,376 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `76410f9f4827`  |
| 3482   | Layout 2 | `76410f9f4827`  |
| 3474   | Layout 2 | `76410f9f4827`  |
| 3473   | Layout 2 | `76410f9f4827`  |
| 3464   | Layout 2 | `76410f9f4827`  |
| 3458   | Layout 2 | `76410f9f4827`  |
| 3454   | Layout 2 | `76410f9f4827`  |
| 3444   | Layout 2 | `76410f9f4827`  |
| 3435   | Layout 2 | `76410f9f4827`  |
| 3426   | Layout 2 | `76410f9f4827`  |
| 3418   | Layout 2 | `76410f9f4827`  |
| 3412   | Layout 2 | `76410f9f4827`  |
| 3402   | Layout 2 | `76410f9f4827`  |
| 3396   | Layout 2 | `76410f9f4827`  |
| 3387   | Layout 2 | `76410f9f4827`  |
| 3381   | Layout 2 | `76410f9f4827`  |
| 3373   | Layout 2 | `76410f9f4827`  |
| 3364   | Layout 2 | `76410f9f4827`  |
| 3356   | Layout 2 | `76410f9f4827`  |
| 3349   | Layout 2 | `76410f9f4827`  |
| 3342   | Layout 2 | `76410f9f4827`  |
| 3335   | Layout 2 | `76410f9f4827`  |
| 3326   | Layout 2 | `76410f9f4827`  |
| 3321   | Layout 2 | `76410f9f4827`  |
| 3314   | Layout 2 | `76410f9f4827`  |
| 3303   | Layout 2 | `76410f9f4827`  |
| 3302   | Layout 2 | `76410f9f4827`  |
| 3293   | Layout 2 | `76410f9f4827`  |
| 3283   | Layout 2 | `76410f9f4827`  |
| 3275   | Layout 2 | `76410f9f4827`  |
| 3267   | Layout 2 | `76410f9f4827`  |
| 3258   | Layout 2 | `76410f9f4827`  |
| 3251   | Layout 2 | `76410f9f4827`  |
| 3242   | Layout 2 | `76410f9f4827`  |
| 3235   | Layout 2 | `76410f9f4827`  |
| 3229   | Layout 2 | `76410f9f4827`  |
| 3212   | Layout 2 | `76410f9f4827`  |
| 3203   | Layout 2 | `76410f9f4827`  |
| 3193   | Layout 2 | `76410f9f4827`  |
| 3186   | Layout 2 | `76410f9f4827`  |
| 3177   | Layout 2 | `76410f9f4827`  |
| 3169   | Layout 2 | `76410f9f4827`  |
| 3158   | Layout 2 | `76410f9f4827`  |
| 3151   | Layout 2 | `76410f9f4827`  |
| 3144   | Layout 2 | `76410f9f4827`  |
| 3133   | Layout 2 | `76410f9f4827`  |
| 3125   | Layout 2 | `76410f9f4827`  |
| 3118   | Layout 2 | `76410f9f4827`  |
| 3111   | Layout 2 | `76410f9f4827`  |
| 3103   | Layout 2 | `76410f9f4827`  |
| 3095   | Layout 2 | `76410f9f4827`  |
| 3086   | Layout 2 | `76410f9f4827`  |
| 3072   | Layout 2 | `76410f9f4827`  |
| 3062   | Layout 2 | `76410f9f4827`  |
| 3052   | Layout 2 | `76410f9f4827`  |
| 3045   | Layout 2 | `76410f9f4827`  |
| 3037   | Layout 2 | `76410f9f4827`  |
| 3030   | Layout 2 | `76410f9f4827`  |
| 3021   | Layout 2 | `76410f9f4827`  |
| 3012   | Layout 2 | `76410f9f4827`  |
| 3002   | Layout 2 | `76410f9f4827`  |
| 2995   | Layout 2 | `76410f9f4827`  |
| 2987   | Layout 2 | `76410f9f4827`  |
| 2978   | Layout 2 | `76410f9f4827`  |
| 2970   | Layout 2 | `76410f9f4827`  |
| 2959   | Layout 2 | `76410f9f4827`  |
| 2951   | Layout 2 | `76410f9f4827`  |
| 2942   | Layout 2 | `76410f9f4827`  |
| 2935   | Layout 2 | `76410f9f4827`  |
| 2932   | Layout 2 | `76410f9f4827`  |
| 2923   | Layout 2 | `76410f9f4827`  |
| 2919   | Layout 2 | `76410f9f4827`  |
| 2907   | Layout 2 | `76410f9f4827`  |
| 2900   | Layout 2 | `76410f9f4827`  |
| 2891   | Layout 2 | `76410f9f4827`  |
| 2882   | Layout 2 | `76410f9f4827`  |
| 2872   | Layout 2 | `76410f9f4827`  |
| 2863   | Layout 2 | `76410f9f4827`  |
| 2855   | Layout 2 | `76410f9f4827`  |
| 2849   | Layout 2 | `76410f9f4827`  |
| 2844   | Layout 2 | `76410f9f4827`  |
| 2834   | Layout 2 | `76410f9f4827`  |
| 2825   | Layout 2 | `76410f9f4827`  |
| 2819   | Layout 2 | `76410f9f4827`  |
| 2811   | Layout 2 | `76410f9f4827`  |
| 2803   | Layout 2 | `76410f9f4827`  |
| 2794   | Layout 2 | `76410f9f4827`  |
| 2783   | Layout 2 | `76410f9f4827`  |
| 2774   | Layout 2 | `76410f9f4827`  |
| 2765   | Layout 2 | `76410f9f4827`  |
| 2756   | Layout 2 | `76410f9f4827`  |
| 2750   | Layout 2 | `76410f9f4827`  |
| 2743   | Layout 2 | `76410f9f4827`  |
| 2736   | Layout 2 | `76410f9f4827`  |
| 2726   | Layout 2 | `76410f9f4827`  |
| 2717   | Layout 2 | `76410f9f4827`  |
| 2709   | Layout 2 | `76410f9f4827`  |
| 2703   | Layout 2 | `76410f9f4827`  |
| 2695   | Layout 2 | `76410f9f4827`  |
| 2684   | Layout 2 | `76410f9f4827`  |
| 2672   | Layout 2 | `76410f9f4827`  |
| 2665   | Layout 2 | `76410f9f4827`  |
| 2657   | Layout 2 | `76410f9f4827`  |
| 2649   | Layout 2 | `76410f9f4827`  |
| 2644   | Layout 2 | `76410f9f4827`  |
| 2637   | Layout 2 | `76410f9f4827`  |
| 2629   | Layout 2 | `76410f9f4827`  |
| 2619   | Layout 2 | `76410f9f4827`  |
| 2612   | Layout 2 | `76410f9f4827`  |
| 2606   | Layout 2 | `76410f9f4827`  |
| 2602   | Layout 2 | `76410f9f4827`  |
| 2601   | Layout 2 | `76410f9f4827`  |
| 2592   | Layout 2 | `76410f9f4827`  |
| 2583   | Layout 2 | `76410f9f4827`  |
| 2575   | Layout 2 | `76410f9f4827`  |
| 2567   | Layout 2 | `76410f9f4827`  |
| 2560   | Layout 2 | `76410f9f4827`  |
| 2553   | Layout 2 | `76410f9f4827`  |
| 2545   | Layout 2 | `76410f9f4827`  |
| 2538   | Layout 2 | `76410f9f4827`  |
| 2529   | Layout 2 | `76410f9f4827`  |
| 2519   | Layout 2 | `76410f9f4827`  |
| 2513   | Layout 2 | `76410f9f4827`  |
| 2510   | Layout 2 | `76410f9f4827`  |
| 2507   | Layout 2 | `76410f9f4827`  |
| 2503   | Layout 2 | `76410f9f4827`  |
| 2498   | Layout 2 | `76410f9f4827`  |
| 2492   | Layout 2 | `76410f9f4827`  |
| 2487   | Layout 2 | `76410f9f4827`  |
| 2480   | Layout 2 | `76410f9f4827`  |
| 2474   | Layout 2 | `76410f9f4827`  |
| 2468   | Layout 2 | `76410f9f4827`  |
| 2460   | Layout 2 | `76410f9f4827`  |
| 2453   | Layout 2 | `76410f9f4827`  |
| 2444   | Layout 2 | `76410f9f4827`  |
| 2438   | Layout 2 | `76410f9f4827`  |
| 2434   | Layout 2 | `76410f9f4827`  |
| 2429   | Layout 2 | `76410f9f4827`  |
| 2421   | Layout 2 | `76410f9f4827`  |
| 2414   | Layout 2 | `76410f9f4827`  |
| 2407   | Layout 2 | `76410f9f4827`  |
| 2401   | Layout 2 | `76410f9f4827`  |
| 2397   | Layout 2 | `76410f9f4827`  |
| 2393   | Layout 2 | `76410f9f4827`  |
| 2384   | Layout 2 | `76410f9f4827`  |
| 2378   | Layout 2 | `76410f9f4827`  |
| 2372   | Layout 2 | `76410f9f4827`  |
| 2358   | Layout 2 | `76410f9f4827`  |
| 2352   | Layout 2 | `76410f9f4827`  |
| 2347   | Layout 2 | `76410f9f4827`  |
| 2343   | Layout 2 | `76410f9f4827`  |
| 2335   | Layout 2 | `76410f9f4827`  |
| 2327   | Layout 2 | `76410f9f4827`  |
| 2324   | Layout 2 | `76410f9f4827`  |
| 2319   | Layout 2 | `76410f9f4827`  |
| 2313   | Layout 2 | `76410f9f4827`  |
| 2308   | Layout 2 | `76410f9f4827`  |
| 2302   | Layout 2 | `76410f9f4827`  |
| 2295   | Layout 2 | `76410f9f4827`  |
| 2290   | Layout 2 | `76410f9f4827`  |
| 2284   | Layout 2 | `76410f9f4827`  |
| 2276   | Layout 2 | `76410f9f4827`  |
| 2269   | Layout 2 | `76410f9f4827`  |
| 2259   | Layout 2 | `76410f9f4827`  |
| 2250   | Layout 2 | `76410f9f4827`  |
| 2243   | Layout 2 | `76410f9f4827`  |
| 2235   | Layout 2 | `76410f9f4827`  |
| 2229   | Layout 2 | `76410f9f4827`  |
| 2224   | Layout 2 | `76410f9f4827`  |
| 2218   | Layout 2 | `76410f9f4827`  |
| 2215   | Layout 2 | `76410f9f4827`  |
| 2207   | Layout 2 | `76410f9f4827`  |
| 2203   | Layout 2 | `76410f9f4827`  |
| 2196   | Layout 2 | `76410f9f4827`  |
| 2192   | Layout 2 | `76410f9f4827`  |
| 2189   | Layout 2 | `76410f9f4827`  |
| 2183   | Layout 2 | `76410f9f4827`  |
| 2179   | Layout 2 | `76410f9f4827`  |
| 2171   | Layout 2 | `76410f9f4827`  |
| 2163   | Layout 2 | `76410f9f4827`  |
| 2156   | Layout 2 | `76410f9f4827`  |
| 2151   | Layout 2 | `76410f9f4827`  |
| 2147   | Layout 2 | `76410f9f4827`  |
| 2142   | Layout 2 | `76410f9f4827`  |
| 2138   | Layout 2 | `76410f9f4827`  |
| 2134   | Layout 2 | `76410f9f4827`  |
| 2130   | Layout 2 | `76410f9f4827`  |
| 2122   | Layout 2 | `76410f9f4827`  |
| 2107   | Layout 2 | `76410f9f4827`  |
| 2098   | Layout 2 | `76410f9f4827`  |
| 2089   | Layout 2 | `76410f9f4827`  |
| 2081   | Layout 2 | `76410f9f4827`  |
| 2073   | Layout 2 | `76410f9f4827`  |
| 2067   | Layout 2 | `76410f9f4827`  |
| 2063   | Layout 2 | `76410f9f4827`  |
| 2059   | Layout 2 | `76410f9f4827`  |
| 2052   | Layout 2 | `76410f9f4827`  |
| 2044   | Layout 2 | `76410f9f4827`  |
| 2039   | Layout 2 | `76410f9f4827`  |
| 2032   | Layout 2 | `76410f9f4827`  |
| 2025   | Layout 2 | `76410f9f4827`  |
| 2011   | Layout 2 | `76410f9f4827`  |
| 2005   | Layout 2 | `76410f9f4827`  |
| 2000   | Layout 2 | `76410f9f4827`  |
| 1996   | Layout 2 | `76410f9f4827`  |
| 1991   | Layout 2 | `76410f9f4827`  |
| 1985   | Layout 2 | `76410f9f4827`  |
| 1980   | Layout 2 | `76410f9f4827`  |
| 1969   | Layout 2 | `76410f9f4827`  |
| 1964   | Layout 2 | `76410f9f4827`  |
| 1958   | Layout 2 | `76410f9f4827`  |
| 1950   | Layout 2 | `76410f9f4827`  |
| 1945   | Layout 2 | `76410f9f4827`  |
| 1937   | Layout 2 | `76410f9f4827`  |
| 1933   | Layout 2 | `76410f9f4827`  |
| 1927   | Layout 2 | `76410f9f4827`  |
| 1921   | Layout 2 | `76410f9f4827`  |
| 1914   | Layout 2 | `76410f9f4827`  |
| 1908   | Layout 2 | `76410f9f4827`  |
| 1897   | Layout 2 | `76410f9f4827`  |
| 1892   | Layout 2 | `76410f9f4827`  |
| 1886   | Layout 2 | `76410f9f4827`  |
| 1881   | Layout 2 | `76410f9f4827`  |
| 1871   | Layout 2 | `76410f9f4827`  |
| 1866   | Layout 2 | `76410f9f4827`  |
| 1862   | Layout 2 | `76410f9f4827`  |
| 1854   | Layout 2 | `76410f9f4827`  |
| 1846   | Layout 2 | `76410f9f4827`  |
| 1838   | Layout 2 | `76410f9f4827`  |
| 1832   | Layout 2 | `76410f9f4827`  |
| 1826   | Layout 2 | `76410f9f4827`  |
| 1822   | Layout 2 | `76410f9f4827`  |
| 1818   | Layout 2 | `76410f9f4827`  |
| 1804   | Layout 2 | `76410f9f4827`  |
| 1794   | Layout 2 | `76410f9f4827`  |
| 1790   | Layout 2 | `76410f9f4827`  |
| 1784   | Layout 2 | `76410f9f4827`  |
| 1774   | Layout 2 | `76410f9f4827`  |
| 1771   | Layout 2 | `76410f9f4827`  |
| 1762   | Layout 2 | `76410f9f4827`  |
| 1759   | Layout 2 | `76410f9f4827`  |
| 1754   | Layout 2 | `76410f9f4827`  |
| 1749   | Layout 2 | `76410f9f4827`  |
| 1743   | Layout 2 | `76410f9f4827`  |
| 1737   | Layout 2 | `76410f9f4827`  |
| 1731   | Layout 2 | `76410f9f4827`  |
| 1725   | Layout 2 | `76410f9f4827`  |
| 1717   | Layout 2 | `76410f9f4827`  |
| 1710   | Layout 2 | `76410f9f4827`  |
| 1704   | Layout 2 | `76410f9f4827`  |
| 1698   | Layout 2 | `76410f9f4827`  |
| 1690   | Layout 2 | `76410f9f4827`  |
| 1685   | Layout 2 | `76410f9f4827`  |
| 1680   | Layout 2 | `76410f9f4827`  |
| 1674   | Layout 2 | `76410f9f4827`  |
| 1668   | Layout 2 | `76410f9f4827`  |
| 1659   | Layout 2 | `76410f9f4827`  |
| 1649   | Layout 2 | `76410f9f4827`  |
| 1642   | Layout 2 | `76410f9f4827`  |
| 1636   | Layout 2 | `76410f9f4827`  |
| 1628   | Layout 2 | `76410f9f4827`  |
| 1622   | Layout 2 | `76410f9f4827`  |
| 1614   | Layout 2 | `76410f9f4827`  |
| 1608   | Layout 2 | `76410f9f4827`  |
| 1602   | Layout 2 | `76410f9f4827`  |
| 1598   | Layout 2 | `76410f9f4827`  |
| 1594   | Layout 2 | `76410f9f4827`  |
| 1590   | Layout 1 | `76410f9f4827`  |
| 1587   | Layout 1 | `76410f9f4827`  |
| 1584   | Layout 1 | `76410f9f4827`  |
| 1579   | Layout 1 | `76410f9f4827`  |
| 1572   | Layout 1 | `76410f9f4827`  |
| 1565   | Layout 1 | `76410f9f4827`  |
| 1559   | Layout 1 | `76410f9f4827`  |
| 1554   | Layout 1 | `76410f9f4827`  |
| 1547   | Layout 1 | `76410f9f4827`  |
| 1537   | Layout 1 | `76410f9f4827`  |
| 1529   | Layout 1 | `76410f9f4827`  |
| 1524   | Layout 1 | `76410f9f4827`  |
| 1519   | Layout 1 | `76410f9f4827`  |
| 1509   | Layout 1 | `76410f9f4827`  |
| 1506   | Layout 1 | `76410f9f4827`  |
| 1504   | Layout 1 | `76410f9f4827`  |
| 1500   | Layout 1 | `76410f9f4827`  |
| 1493   | Layout 1 | `76410f9f4827`  |
| 1489   | Layout 1 | `76410f9f4827`  |
| 1485   | Layout 1 | `76410f9f4827`  |
| 1481   | Layout 1 | `76410f9f4827`  |
| 1474   | Layout 1 | `76410f9f4827`  |
| 1466   | Layout 1 | `76410f9f4827`  |
| 1462   | Layout 1 | `76410f9f4827`  |
| 1459   | Layout 1 | `76410f9f4827`  |
| 1453   | Layout 1 | `76410f9f4827`  |
| 1450   | Layout 1 | `76410f9f4827`  |
| 1445   | Layout 1 | `76410f9f4827`  |
| 1439   | Layout 1 | `76410f9f4827`  |
| 1433   | Layout 1 | `76410f9f4827`  |
| 1430   | Layout 1 | `76410f9f4827`  |
| 1426   | Layout 1 | `76410f9f4827`  |
| 1421   | Layout 1 | `76410f9f4827`  |
| 1417   | Layout 1 | `76410f9f4827`  |
| 1416   | Layout 1 | `76410f9f4827`  |
| 1409   | Layout 1 | `76410f9f4827`  |
| 1405   | Layout 1 | `76410f9f4827`  |
| 1401   | Layout 1 | `76410f9f4827`  |
| 1396   | Layout 1 | `76410f9f4827`  |
| 1391   | Layout 1 | `76410f9f4827`  |
| 1390   | Layout 1 | `76410f9f4827`  |
| 1386   | Layout 1 | `76410f9f4827`  |
| 1381   | Layout 1 | `76410f9f4827`  |
| 1379   | Layout 1 | `76410f9f4827`  |
| 1372   | Layout 1 | `76410f9f4827`  |
| 1366   | Layout 1 | `76410f9f4827`  |
| 1364   | Layout 1 | `76410f9f4827`  |
| 1363   | Layout 1 | `76410f9f4827`  |
| 1360   | Layout 1 | `76410f9f4827`  |
| 1358   | Layout 1 | `76410f9f4827`  |
| 1355   | Layout 1 | `76410f9f4827`  |
| 1351   | Layout 1 | `76410f9f4827`  |
| 1348   | Layout 1 | `76410f9f4827`  |
| 1346   | Layout 1 | `76410f9f4827`  |
| 1341   | Layout 1 | `76410f9f4827`  |
| 1340   | Layout 1 | `76410f9f4827`  |
| 1338   | Layout 1 | `76410f9f4827`  |
| 1335   | Layout 1 | `76410f9f4827`  |
| 1333   | Layout 1 | `76410f9f4827`  |
| 1329   | Layout 1 | `76410f9f4827`  |
| 1327   | Layout 1 | `76410f9f4827`  |
| 1324   | Layout 2 | `76410f9f4827`  |
| 1321   | Layout 2 | `76410f9f4827`  |
| 1319   | No file  | `76410f9f4827`  |
| 1318   | No file  | `76410f9f4827`  |
| 1316   | No file  | `76410f9f4827`  |
| 1313   | No file  | `76410f9f4827`  |
| 1311   | No file  | `76410f9f4827`  |
| 1309   | No file  | `76410f9f4827`  |
| 1304   | No file  | `76410f9f4827`  |
| 1292   | No file  | `76410f9f4827`  |
| 1286   | No file  | `76410f9f4827`  |
| 1280   | No file  | `76410f9f4827`  |
| 1276   | No file  | `76410f9f4827`  |
| 1267   | No file  | `76410f9f4827`  |
| 1261   | No file  | `76410f9f4827`  |
| 1256   | No file  | `76410f9f4827`  |
| 1250   | No file  | `76410f9f4827`  |
| 1246   | No file  | `76410f9f4827`  |
| 1239   | No file  | `76410f9f4827`  |
| 1230   | No file  | `76410f9f4827`  |
| 1226   | No file  | `76410f9f4827`  |
| 1220   | No file  | `76410f9f4827`  |
| 1217   | No file  | `76410f9f4827`  |
| 1211   | No file  | `76410f9f4827`  |
| 1210   | No file  | `76410f9f4827`  |
| 1208   | No file  | `76410f9f4827`  |
| 1203   | No file  | `76410f9f4827`  |
| 1197   | No file  | `76410f9f4827`  |
| 1194   | No file  | `76410f9f4827`  |
| 1192   | No file  | `76410f9f4827`  |
| 1187   | No file  | `76410f9f4827`  |
| 1183   | No file  | `76410f9f4827`  |
| 1177   | No file  | `76410f9f4827`  |
| 1173   | No file  | `76410f9f4827`  |
| 1167   | No file  | `76410f9f4827`  |
| 1164   | No file  | `76410f9f4827`  |
| 1156   | No file  | `76410f9f4827`  |
| 1149   | No file  | `76410f9f4827`  |
| 1144   | No file  | `76410f9f4827`  |
| 1137   | No file  | `76410f9f4827`  |
| 1132   | No file  | `76410f9f4827`  |
| 1127   | No file  | `76410f9f4827`  |
| 1122   | No file  | `76410f9f4827`  |
| 1118   | No file  | `76410f9f4827`  |
| 1114   | No file  | `76410f9f4827`  |
| 1109   | No file  | `76410f9f4827`  |
| 1102   | No file  | `76410f9f4827`  |
| 1096   | No file  | `76410f9f4827`  |
| 1088   | No file  | `76410f9f4827`  |
| 1081   | No file  | `76410f9f4827`  |
| 1076   | No file  | `76410f9f4827`  |
| 1069   | No file  | `76410f9f4827`  |
| 1064   | No file  | `76410f9f4827`  |
| 1058   | No file  | `76410f9f4827`  |
| 1051   | No file  | `76410f9f4827`  |
| 1044   | No file  | `76410f9f4827`  |
| 1036   | No file  | `76410f9f4827`  |
| 1026   | No file  | `76410f9f4827`  |
| 1016   | No file  | `76410f9f4827`  |
| 1009   | No file  | `76410f9f4827`  |
| 1005   | No file  | `76410f9f4827`  |
| 1000   | No file  | `76410f9f4827`  |
| 998    | No file  | `76410f9f4827`  |
| 990    | No file  | `76410f9f4827`  |
| 979    | No file  | `76410f9f4827`  |
| 972    | No file  | `76410f9f4827`  |
| 963    | No file  | `76410f9f4827`  |
| 955    | No file  | `76410f9f4827`  |
| 946    | No file  | `76410f9f4827`  |
| 938    | No file  | `76410f9f4827`  |
| 927    | No file  | `76410f9f4827`  |
| 911    | No file  | `76410f9f4827`  |
| 904    | No file  | `76410f9f4827`  |
| 899    | No file  | `76410f9f4827`  |
| 894    | No file  | `76410f9f4827`  |
| 885    | No file  | `76410f9f4827`  |
| 879    | No file  | `76410f9f4827`  |
| 872    | No file  | `76410f9f4827`  |
| 864    | No file  | `76410f9f4827`  |
| 855    | No file  | `76410f9f4827`  |
| 853    | No file  | `76410f9f4827`  |
| 845    | No file  | `76410f9f4827`  |
| 837    | No file  | `76410f9f4827`  |
| 829    | No file  | `76410f9f4827`  |
| 822    | No file  | `76410f9f4827`  |
| 814    | No file  | `76410f9f4827`  |
| 805    | No file  | `76410f9f4827`  |
| 794    | No file  | `76410f9f4827`  |
| 787    | No file  | `76410f9f4827`  |
| 780    | No file  | `76410f9f4827`  |
| 771    | No file  | `76410f9f4827`  |
| 760    | No file  | `76410f9f4827`  |
| 748    | No file  | `76410f9f4827`  |
| 741    | No file  | `76410f9f4827`  |
| 736    | No file  | `76410f9f4827`  |
| 731    | No file  | `76410f9f4827`  |
| 723    | No file  | `76410f9f4827`  |
| 711    | No file  | `76410f9f4827`  |
| 707    | No file  | `76410f9f4827`  |
| 697    | No file  | `76410f9f4827`  |
| 689    | No file  | `76410f9f4827`  |
| 683    | No file  | `76410f9f4827`  |
| 678    | No file  | `76410f9f4827`  |
| 670    | No file  | `76410f9f4827`  |
| 661    | No file  | `76410f9f4827`  |
| 656    | No file  | `76410f9f4827`  |
| 652    | No file  | `76410f9f4827`  |
| 643    | No file  | `76410f9f4827`  |
| 637    | No file  | `76410f9f4827`  |
| 630    | No file  | `76410f9f4827`  |
| 627    | No file  | `76410f9f4827`  |
| 621    | No file  | `76410f9f4827`  |
| 617    | No file  | `76410f9f4827`  |
| 615    | No file  | `76410f9f4827`  |
| 606    | No file  | `76410f9f4827`  |
| 599    | No file  | `76410f9f4827`  |
| 592    | No file  | `76410f9f4827`  |
| 586    | No file  | `76410f9f4827`  |
| 577    | No file  | `76410f9f4827`  |
| 569    | No file  | `76410f9f4827`  |
| 561    | No file  | `76410f9f4827`  |
| 554    | No file  | `76410f9f4827`  |
| 542    | No file  | `76410f9f4827`  |
| 532    | No file  | `76410f9f4827`  |
| 531    | No file  | `76410f9f4827`  |
| 526    | No file  | `76410f9f4827`  |
| 521    | No file  | `76410f9f4827`  |
| 517    | No file  | `76410f9f4827`  |
| 510    | No file  | `76410f9f4827`  |
| 508    | No file  | `76410f9f4827`  |
| 504    | No file  | `76410f9f4827`  |
| 497    | No file  | `76410f9f4827`  |
| 491    | No file  | `76410f9f4827`  |
| 485    | No file  | `76410f9f4827`  |
| 478    | No file  | `76410f9f4827`  |
| 472    | No file  | `76410f9f4827`  |
| 466    | No file  | `76410f9f4827`  |
| 457    | No file  | `76410f9f4827`  |
| 452    | No file  | `76410f9f4827`  |
| 449    | No file  | `76410f9f4827`  |
| 435    | No file  | `76410f9f4827`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                 |
| --------------------- | -------- | -------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0)  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of subgroups                           |
| `+0x08`             | Row[row_count] | rows         | See Row; in no key order                      |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                 |
| ------- | ------------------ | ----------- | ------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `1` to `44` on client 3482 |
| `+0x04` | Entry[entry_count] | entries     | See Entry; one per limited shop item  |

### Entry (16 bytes)

| Offset  | Type | Field                | Notes                                                                                     |
| ------- | ---- | -------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | subgroup_key         | The `itemsubgroup.dbss` key; the same on every entry of one row                          |
| `+0x02` | u32  | item_key             | The item, a packed item key as in `itemsubgroup.dbss` (LOC type 0 name); see Open Questions |
| `+0x06` | u8   | purchase_subject     | `2` on 704 of 705 entries, `1` on one (client 3482); see Open Questions                   |
| `+0x07` | u32  | purchase_count_limit | How many the character or family can buy before the reset                                |
| `+0x0B` | u8   | reset_type           | When the count resets; see Reset Types                                                    |
| `+0x0C` | u32  | unknown_0c           | `0` on every entry (clients 1784 and 3482); see Open Questions                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                         |
| ------- | ------------------ | ------------ | --------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                         |

## Layout 1

No `unknown_0c`: an entry is 12 bytes. Only the Entry differs from
Layout 2.

### Entry (12 bytes)

| Offset  | Type | Field                | Notes |
| ------- | ---- | -------------------- | ----- |
| `+0x00` | u16  | subgroup_key         |       |
| `+0x02` | u32  | item_key             |       |
| `+0x06` | u8   | purchase_subject     |       |
| `+0x07` | u32  | purchase_count_limit |       |
| `+0x0B` | u8   | reset_type           |       |

## Reset Types

The NPC shop Lua appends `DAY`, `WEEK`, `MONTH` or `SIEGE` to the limit
text key for `getResetType()` `1` to `4`. Entry counts are from client
3482.

| Value | Lua text key suffix | Sheet `ResetType` | Entries |
| ----- | ------------------- | ----------------- | ------- |
| 1     | `DAY`               | `Day`             | 360     |
| 2     | `WEEK`              | `Week`            | 54      |
| 3     | `MONTH`             | `Month`           | 220     |
| 4     | `SIEGE`             | `Siege`           | 71      |

With `4` the shop also shows its guild limit time line
(`_txt_GuildLimitTime`).

## Field Names

The `LimitedItemSubGroup_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `ItemSubGroupKey`,
`ItemKey`, `EnchantLevel`, `PurchaseSubject`, `PurchaseCountLimit`,
`ResetType` and `ADSummary`, 322 rows. 313 of the 324 entries of the
client 1784 file have a row with the same subgroup and item.

| Field                | Column               | Same value (client 1784 file) |
| -------------------- | -------------------- | ----------------------------- |
| subgroup_key         | `ItemSubGroupKey`    | 313 of 313                    |
| item_key             | `ItemKey`            | 313 of 313                    |
| purchase_subject     | `PurchaseSubject`    | 313 of 313                    |
| purchase_count_limit | `PurchaseCountLimit` | 312 of 313                    |
| reset_type           | `ResetType`          | 313 of 313 (`Day` 260 as `1`, `Siege` 49 as `4`, `Week` 3 as `2`, `Month` 1 as `3`) |

The client 1784 server dump names the sheet's checks
(`LimitedItemSubGroup_Table(ItemSubGroupKey : %#)`,
`(ItemKey : %#, EnchantLevel : %#)`, `ResetType(%#)`,
`PurchaseCountLimit(%#)`, `AdSummary`).

## Notes

- 696 of the 705 entries of client 3482 name an item that the subgroup's
  `itemsubgroup.dbss` record lists. The other nine are items `756300`
  (subgroup 51660), `756301` (51661), `3560` to `3564` (51891) and
  `757010` (51761 and 51762).
- The one entry with `purchase_subject` `1` on client 3482 is Weight Limit
  +400 LT (`450126`, subgroup 51884), 7 per month.
- Client 1784 has 26 rows and 324 entries, every `purchase_subject` `2`.

## Open Questions

### Purchase Subject Values

`purchase_subject` decides whether the limit counts per character or per
family (`isLimitedByUser()` picks the `FAMILY` or `CHARACTER` text), but
which of `1` and `2` is the family is not in the Lua. The single `1`
entry is Weight Limit +400 LT (`450126`).

### Enchant Level and the Last Field

The sheet has seven columns and the entry six fields. `item_key` equals
the packed item keys of `itemsubgroup.dbss`, which hold the enhancement
level in the top byte, but every `item_key` has a top byte of `0` and
every sheet `EnchantLevel` is `0`, so the data cannot tell whether the
level is in `item_key` or in `unknown_0c`. If the level is packed,
`unknown_0c` would be the `ADSummary` text, whose cells are all
`<null>`; the string table is empty on both clients. Clients 1348 and
1485 have no `unknown_0c` at all (Layout 1).
