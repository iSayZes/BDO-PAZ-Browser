# `fevertimeskill.bss` Format

## Purpose

The Agris Fever drop skills: one 10-byte row per step with the skill that
Agris Fever applies and the item drop amount bonus it gives. On client 3474
the file lists five rows, index `1` to `5`, for the skills `Item Drop
Quantity Effect +100% (On)` (58988) and `+150% (On)` to `+300% (On)` (59042
to 59045), with `description` `1000000` to `3000000` on the client's
1,000,000 = 100% scale. The plain PABR file holds a u16 after the row count,
the rows, then an empty string table. The quests that spend Agris Fever
points are in [`feverquestdatatable.bss`](feverquestdatatable_bss.md), next
to this file in the same PAZ.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records           | Row bytes |
| ------ | -------------- | -------------------- | ----- | ----------------- | --------- |
| 1      | 1324 and later | `fevertimeskill.bss` | 72    | 5 Fever Skill Row | 10        |

| Layout | File                 | Known        | Unknown    |
| ------ | -------------------- | ------------ | ---------- |
| 1      | `fevertimeskill.bss` | 70 B (97.2%) | 2 B (2.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c375d54d713f`  |
| 3482   | Layout 1 | `c375d54d713f`  |
| 3474   | Layout 1 | `c375d54d713f`  |
| 3473   | Layout 1 | `c375d54d713f`  |
| 3464   | Layout 1 | `c375d54d713f`  |
| 3458   | Layout 1 | `c375d54d713f`  |
| 3454   | Layout 1 | `c375d54d713f`  |
| 3444   | Layout 1 | `c375d54d713f`  |
| 3435   | Layout 1 | `c375d54d713f`  |
| 3426   | Layout 1 | `c375d54d713f`  |
| 3418   | Layout 1 | `c375d54d713f`  |
| 3412   | Layout 1 | `c375d54d713f`  |
| 3402   | Layout 1 | `c375d54d713f`  |
| 3396   | Layout 1 | `c375d54d713f`  |
| 3387   | Layout 1 | `c375d54d713f`  |
| 3381   | Layout 1 | `c375d54d713f`  |
| 3373   | Layout 1 | `c375d54d713f`  |
| 3364   | Layout 1 | `c375d54d713f`  |
| 3356   | Layout 1 | `c375d54d713f`  |
| 3349   | Layout 1 | `c375d54d713f`  |
| 3342   | Layout 1 | `c375d54d713f`  |
| 3335   | Layout 1 | `c375d54d713f`  |
| 3326   | Layout 1 | `c375d54d713f`  |
| 3321   | Layout 1 | `c375d54d713f`  |
| 3314   | Layout 1 | `c375d54d713f`  |
| 3303   | Layout 1 | `c375d54d713f`  |
| 3302   | Layout 1 | `c375d54d713f`  |
| 3293   | Layout 1 | `c375d54d713f`  |
| 3283   | Layout 1 | `c375d54d713f`  |
| 3275   | Layout 1 | `c375d54d713f`  |
| 3267   | Layout 1 | `c375d54d713f`  |
| 3258   | Layout 1 | `c375d54d713f`  |
| 3251   | Layout 1 | `c375d54d713f`  |
| 3242   | Layout 1 | `c375d54d713f`  |
| 3235   | Layout 1 | `c375d54d713f`  |
| 3229   | Layout 1 | `c375d54d713f`  |
| 3212   | Layout 1 | `c375d54d713f`  |
| 3203   | Layout 1 | `c375d54d713f`  |
| 3193   | Layout 1 | `c375d54d713f`  |
| 3186   | Layout 1 | `c375d54d713f`  |
| 3177   | Layout 1 | `c375d54d713f`  |
| 3169   | Layout 1 | `c375d54d713f`  |
| 3158   | Layout 1 | `c375d54d713f`  |
| 3151   | Layout 1 | `c375d54d713f`  |
| 3144   | Layout 1 | `c375d54d713f`  |
| 3133   | Layout 1 | `c375d54d713f`  |
| 3125   | Layout 1 | `c375d54d713f`  |
| 3118   | Layout 1 | `c375d54d713f`  |
| 3111   | Layout 1 | `c375d54d713f`  |
| 3103   | Layout 1 | `c375d54d713f`  |
| 3095   | Layout 1 | `c375d54d713f`  |
| 3086   | Layout 1 | `c375d54d713f`  |
| 3072   | Layout 1 | `c375d54d713f`  |
| 3062   | Layout 1 | `c375d54d713f`  |
| 3052   | Layout 1 | `c375d54d713f`  |
| 3045   | Layout 1 | `c375d54d713f`  |
| 3037   | Layout 1 | `c375d54d713f`  |
| 3030   | Layout 1 | `c375d54d713f`  |
| 3021   | Layout 1 | `c375d54d713f`  |
| 3012   | Layout 1 | `c375d54d713f`  |
| 3002   | Layout 1 | `c375d54d713f`  |
| 2995   | Layout 1 | `c375d54d713f`  |
| 2987   | Layout 1 | `c375d54d713f`  |
| 2978   | Layout 1 | `c375d54d713f`  |
| 2970   | Layout 1 | `c375d54d713f`  |
| 2959   | Layout 1 | `c375d54d713f`  |
| 2951   | Layout 1 | `c375d54d713f`  |
| 2942   | Layout 1 | `c375d54d713f`  |
| 2935   | Layout 1 | `c375d54d713f`  |
| 2932   | Layout 1 | `c375d54d713f`  |
| 2923   | Layout 1 | `c375d54d713f`  |
| 2919   | Layout 1 | `c375d54d713f`  |
| 2907   | Layout 1 | `c375d54d713f`  |
| 2900   | Layout 1 | `c375d54d713f`  |
| 2891   | Layout 1 | `c375d54d713f`  |
| 2882   | Layout 1 | `c375d54d713f`  |
| 2872   | Layout 1 | `c375d54d713f`  |
| 2863   | Layout 1 | `c375d54d713f`  |
| 2855   | Layout 1 | `c375d54d713f`  |
| 2849   | Layout 1 | `c375d54d713f`  |
| 2844   | Layout 1 | `c375d54d713f`  |
| 2834   | Layout 1 | `c375d54d713f`  |
| 2825   | Layout 1 | `c375d54d713f`  |
| 2819   | Layout 1 | `c375d54d713f`  |
| 2811   | Layout 1 | `c375d54d713f`  |
| 2803   | Layout 1 | `c375d54d713f`  |
| 2794   | Layout 1 | `c375d54d713f`  |
| 2783   | Layout 1 | `c375d54d713f`  |
| 2774   | Layout 1 | `c375d54d713f`  |
| 2765   | Layout 1 | `c375d54d713f`  |
| 2756   | Layout 1 | `c375d54d713f`  |
| 2750   | Layout 1 | `c375d54d713f`  |
| 2743   | Layout 1 | `c375d54d713f`  |
| 2736   | Layout 1 | `c375d54d713f`  |
| 2726   | Layout 1 | `c375d54d713f`  |
| 2717   | Layout 1 | `c375d54d713f`  |
| 2709   | Layout 1 | `c375d54d713f`  |
| 2703   | Layout 1 | `c375d54d713f`  |
| 2695   | Layout 1 | `c375d54d713f`  |
| 2684   | Layout 1 | `c375d54d713f`  |
| 2672   | Layout 1 | `c375d54d713f`  |
| 2665   | Layout 1 | `c375d54d713f`  |
| 2657   | Layout 1 | `c375d54d713f`  |
| 2649   | Layout 1 | `c375d54d713f`  |
| 2644   | Layout 1 | `c375d54d713f`  |
| 2637   | Layout 1 | `c375d54d713f`  |
| 2629   | Layout 1 | `c375d54d713f`  |
| 2619   | Layout 1 | `c375d54d713f`  |
| 2612   | Layout 1 | `c375d54d713f`  |
| 2606   | Layout 1 | `c375d54d713f`  |
| 2602   | Layout 1 | `c375d54d713f`  |
| 2601   | Layout 1 | `c375d54d713f`  |
| 2592   | Layout 1 | `c375d54d713f`  |
| 2583   | Layout 1 | `c375d54d713f`  |
| 2575   | Layout 1 | `c375d54d713f`  |
| 2567   | Layout 1 | `c375d54d713f`  |
| 2560   | Layout 1 | `c375d54d713f`  |
| 2553   | Layout 1 | `c375d54d713f`  |
| 2545   | Layout 1 | `c375d54d713f`  |
| 2538   | Layout 1 | `c375d54d713f`  |
| 2529   | Layout 1 | `c375d54d713f`  |
| 2519   | Layout 1 | `c375d54d713f`  |
| 2513   | Layout 1 | `c375d54d713f`  |
| 2510   | Layout 1 | `c375d54d713f`  |
| 2507   | Layout 1 | `c375d54d713f`  |
| 2503   | Layout 1 | `c375d54d713f`  |
| 2498   | Layout 1 | `c375d54d713f`  |
| 2492   | Layout 1 | `c375d54d713f`  |
| 2487   | Layout 1 | `c375d54d713f`  |
| 2480   | Layout 1 | `c375d54d713f`  |
| 2474   | Layout 1 | `c375d54d713f`  |
| 2468   | Layout 1 | `c375d54d713f`  |
| 2460   | Layout 1 | `c375d54d713f`  |
| 2453   | Layout 1 | `c375d54d713f`  |
| 2444   | Layout 1 | `c375d54d713f`  |
| 2438   | Layout 1 | `c375d54d713f`  |
| 2434   | Layout 1 | `c375d54d713f`  |
| 2429   | Layout 1 | `c375d54d713f`  |
| 2421   | Layout 1 | `c375d54d713f`  |
| 2414   | Layout 1 | `c375d54d713f`  |
| 2407   | Layout 1 | `c375d54d713f`  |
| 2401   | Layout 1 | `c375d54d713f`  |
| 2397   | Layout 1 | `c375d54d713f`  |
| 2393   | Layout 1 | `c375d54d713f`  |
| 2384   | Layout 1 | `c375d54d713f`  |
| 2378   | Layout 1 | `c375d54d713f`  |
| 2372   | Layout 1 | `c375d54d713f`  |
| 2358   | Layout 1 | `c375d54d713f`  |
| 2352   | Layout 1 | `c375d54d713f`  |
| 2347   | Layout 1 | `c375d54d713f`  |
| 2343   | Layout 1 | `c375d54d713f`  |
| 2335   | Layout 1 | `c375d54d713f`  |
| 2327   | Layout 1 | `c375d54d713f`  |
| 2324   | Layout 1 | `c375d54d713f`  |
| 2319   | Layout 1 | `c375d54d713f`  |
| 2313   | Layout 1 | `c375d54d713f`  |
| 2308   | Layout 1 | `c375d54d713f`  |
| 2302   | Layout 1 | `c375d54d713f`  |
| 2295   | Layout 1 | `c375d54d713f`  |
| 2290   | Layout 1 | `c375d54d713f`  |
| 2284   | Layout 1 | `c375d54d713f`  |
| 2276   | Layout 1 | `c375d54d713f`  |
| 2269   | Layout 1 | `c375d54d713f`  |
| 2259   | Layout 1 | `c375d54d713f`  |
| 2250   | Layout 1 | `c375d54d713f`  |
| 2243   | Layout 1 | `c375d54d713f`  |
| 2235   | Layout 1 | `c375d54d713f`  |
| 2229   | Layout 1 | `c375d54d713f`  |
| 2224   | Layout 1 | `c375d54d713f`  |
| 2218   | Layout 1 | `c375d54d713f`  |
| 2215   | Layout 1 | `c375d54d713f`  |
| 2207   | Layout 1 | `c375d54d713f`  |
| 2203   | Layout 1 | `c375d54d713f`  |
| 2196   | Layout 1 | `c375d54d713f`  |
| 2192   | Layout 1 | `c375d54d713f`  |
| 2189   | Layout 1 | `c375d54d713f`  |
| 2183   | Layout 1 | `c375d54d713f`  |
| 2179   | Layout 1 | `c375d54d713f`  |
| 2171   | Layout 1 | `c375d54d713f`  |
| 2163   | Layout 1 | `c375d54d713f`  |
| 2156   | Layout 1 | `c375d54d713f`  |
| 2151   | Layout 1 | `c375d54d713f`  |
| 2147   | Layout 1 | `c375d54d713f`  |
| 2142   | Layout 1 | `c375d54d713f`  |
| 2138   | Layout 1 | `c375d54d713f`  |
| 2134   | Layout 1 | `c375d54d713f`  |
| 2130   | Layout 1 | `c375d54d713f`  |
| 2122   | Layout 1 | `c375d54d713f`  |
| 2107   | Layout 1 | `c375d54d713f`  |
| 2098   | Layout 1 | `c375d54d713f`  |
| 2089   | Layout 1 | `c375d54d713f`  |
| 2081   | Layout 1 | `c375d54d713f`  |
| 2073   | Layout 1 | `c375d54d713f`  |
| 2067   | Layout 1 | `c375d54d713f`  |
| 2063   | Layout 1 | `c375d54d713f`  |
| 2059   | Layout 1 | `c375d54d713f`  |
| 2052   | Layout 1 | `c375d54d713f`  |
| 2044   | Layout 1 | `c375d54d713f`  |
| 2039   | Layout 1 | `c375d54d713f`  |
| 2032   | Layout 1 | `c375d54d713f`  |
| 2025   | Layout 1 | `c375d54d713f`  |
| 2011   | Layout 1 | `c375d54d713f`  |
| 2005   | Layout 1 | `c375d54d713f`  |
| 2000   | Layout 1 | `c375d54d713f`  |
| 1996   | Layout 1 | `c375d54d713f`  |
| 1991   | Layout 1 | `c375d54d713f`  |
| 1985   | Layout 1 | `c375d54d713f`  |
| 1980   | Layout 1 | `c375d54d713f`  |
| 1969   | Layout 1 | `c375d54d713f`  |
| 1964   | Layout 1 | `c375d54d713f`  |
| 1958   | Layout 1 | `c375d54d713f`  |
| 1950   | Layout 1 | `c375d54d713f`  |
| 1945   | Layout 1 | `c375d54d713f`  |
| 1937   | Layout 1 | `c375d54d713f`  |
| 1933   | Layout 1 | `c375d54d713f`  |
| 1927   | Layout 1 | `c375d54d713f`  |
| 1921   | Layout 1 | `c375d54d713f`  |
| 1914   | Layout 1 | `c375d54d713f`  |
| 1908   | Layout 1 | `c375d54d713f`  |
| 1897   | Layout 1 | `c375d54d713f`  |
| 1892   | Layout 1 | `c375d54d713f`  |
| 1886   | Layout 1 | `c375d54d713f`  |
| 1881   | Layout 1 | `c375d54d713f`  |
| 1871   | Layout 1 | `c375d54d713f`  |
| 1866   | Layout 1 | `c375d54d713f`  |
| 1862   | Layout 1 | `c375d54d713f`  |
| 1854   | Layout 1 | `c375d54d713f`  |
| 1846   | Layout 1 | `c375d54d713f`  |
| 1838   | Layout 1 | `c375d54d713f`  |
| 1832   | Layout 1 | `c375d54d713f`  |
| 1826   | Layout 1 | `c375d54d713f`  |
| 1822   | Layout 1 | `c375d54d713f`  |
| 1818   | Layout 1 | `c375d54d713f`  |
| 1804   | Layout 1 | `c375d54d713f`  |
| 1794   | Layout 1 | `c375d54d713f`  |
| 1790   | Layout 1 | `c375d54d713f`  |
| 1784   | Layout 1 | `c375d54d713f`  |
| 1774   | Layout 1 | `c375d54d713f`  |
| 1771   | Layout 1 | `c375d54d713f`  |
| 1762   | Layout 1 | `c375d54d713f`  |
| 1759   | Layout 1 | `c375d54d713f`  |
| 1754   | Layout 1 | `c375d54d713f`  |
| 1749   | Layout 1 | `c375d54d713f`  |
| 1743   | Layout 1 | `c375d54d713f`  |
| 1737   | Layout 1 | `c375d54d713f`  |
| 1731   | Layout 1 | `c375d54d713f`  |
| 1725   | Layout 1 | `c375d54d713f`  |
| 1717   | Layout 1 | `c375d54d713f`  |
| 1710   | Layout 1 | `c375d54d713f`  |
| 1704   | Layout 1 | `c375d54d713f`  |
| 1698   | Layout 1 | `c375d54d713f`  |
| 1690   | Layout 1 | `c375d54d713f`  |
| 1685   | Layout 1 | `c375d54d713f`  |
| 1680   | Layout 1 | `c375d54d713f`  |
| 1674   | Layout 1 | `c375d54d713f`  |
| 1668   | Layout 1 | `c375d54d713f`  |
| 1659   | Layout 1 | `c375d54d713f`  |
| 1649   | Layout 1 | `c375d54d713f`  |
| 1642   | Layout 1 | `c375d54d713f`  |
| 1636   | Layout 1 | `c375d54d713f`  |
| 1628   | Layout 1 | `c375d54d713f`  |
| 1622   | Layout 1 | `c375d54d713f`  |
| 1614   | Layout 1 | `c375d54d713f`  |
| 1608   | Layout 1 | `c375d54d713f`  |
| 1602   | Layout 1 | `c375d54d713f`  |
| 1598   | Layout 1 | `c375d54d713f`  |
| 1594   | Layout 1 | `c375d54d713f`  |
| 1590   | Layout 1 | `c375d54d713f`  |
| 1587   | Layout 1 | `c375d54d713f`  |
| 1584   | Layout 1 | `c375d54d713f`  |
| 1579   | Layout 1 | `c375d54d713f`  |
| 1572   | Layout 1 | `c375d54d713f`  |
| 1565   | Layout 1 | `c375d54d713f`  |
| 1559   | Layout 1 | `c375d54d713f`  |
| 1554   | Layout 1 | `c375d54d713f`  |
| 1547   | Layout 1 | `c375d54d713f`  |
| 1537   | Layout 1 | `c375d54d713f`  |
| 1529   | Layout 1 | `c375d54d713f`  |
| 1524   | Layout 1 | `c375d54d713f`  |
| 1519   | Layout 1 | `c375d54d713f`  |
| 1509   | Layout 1 | `c375d54d713f`  |
| 1506   | Layout 1 | `c375d54d713f`  |
| 1504   | Layout 1 | `c375d54d713f`  |
| 1500   | Layout 1 | `c375d54d713f`  |
| 1493   | Layout 1 | `c375d54d713f`  |
| 1489   | Layout 1 | `c375d54d713f`  |
| 1485   | Layout 1 | `c375d54d713f`  |
| 1481   | Layout 1 | `c375d54d713f`  |
| 1474   | Layout 1 | `c375d54d713f`  |
| 1466   | Layout 1 | `c375d54d713f`  |
| 1462   | Layout 1 | `c375d54d713f`  |
| 1459   | Layout 1 | `c375d54d713f`  |
| 1453   | Layout 1 | `c375d54d713f`  |
| 1450   | Layout 1 | `c375d54d713f`  |
| 1445   | Layout 1 | `c375d54d713f`  |
| 1439   | Layout 1 | `c375d54d713f`  |
| 1433   | Layout 1 | `c375d54d713f`  |
| 1430   | Layout 1 | `c375d54d713f`  |
| 1426   | Layout 1 | `c375d54d713f`  |
| 1421   | Layout 1 | `c375d54d713f`  |
| 1417   | Layout 1 | `c375d54d713f`  |
| 1416   | Layout 1 | `c375d54d713f`  |
| 1409   | Layout 1 | `c375d54d713f`  |
| 1405   | Layout 1 | `c375d54d713f`  |
| 1401   | Layout 1 | `c375d54d713f`  |
| 1396   | Layout 1 | `c375d54d713f`  |
| 1391   | Layout 1 | `c375d54d713f`  |
| 1390   | Layout 1 | `c375d54d713f`  |
| 1386   | Layout 1 | `c375d54d713f`  |
| 1381   | Layout 1 | `c375d54d713f`  |
| 1379   | Layout 1 | `c375d54d713f`  |
| 1372   | Layout 1 | `c375d54d713f`  |
| 1366   | Layout 1 | `c375d54d713f`  |
| 1364   | Layout 1 | `c375d54d713f`  |
| 1363   | Layout 1 | `c375d54d713f`  |
| 1360   | Layout 1 | `c375d54d713f`  |
| 1358   | Layout 1 | `c375d54d713f`  |
| 1355   | Layout 1 | `c375d54d713f`  |
| 1351   | Layout 1 | `c375d54d713f`  |
| 1348   | Layout 1 | `c375d54d713f`  |
| 1346   | Layout 1 | `c375d54d713f`  |
| 1341   | Layout 1 | `c375d54d713f`  |
| 1340   | Layout 1 | `c375d54d713f`  |
| 1338   | Layout 1 | `c375d54d713f`  |
| 1335   | Layout 1 | `c375d54d713f`  |
| 1333   | Layout 1 | `c375d54d713f`  |
| 1329   | Layout 1 | `c375d54d713f`  |
| 1327   | Layout 1 | `c375d54d713f`  |
| 1324   | Layout 1 | `c375d54d713f`  |
| 1321   | No file  | `c375d54d713f`  |
| 1319   | No file  | `c375d54d713f`  |
| 1318   | No file  | `c375d54d713f`  |
| 1316   | No file  | `c375d54d713f`  |
| 1313   | No file  | `c375d54d713f`  |
| 1311   | No file  | `c375d54d713f`  |
| 1309   | No file  | `c375d54d713f`  |
| 1304   | No file  | `c375d54d713f`  |
| 1292   | No file  | `c375d54d713f`  |
| 1286   | No file  | `c375d54d713f`  |
| 1280   | No file  | `c375d54d713f`  |
| 1276   | No file  | `c375d54d713f`  |
| 1267   | No file  | `c375d54d713f`  |
| 1261   | No file  | `c375d54d713f`  |
| 1256   | No file  | `c375d54d713f`  |
| 1250   | No file  | `c375d54d713f`  |
| 1246   | No file  | `c375d54d713f`  |
| 1239   | No file  | `c375d54d713f`  |
| 1230   | No file  | `c375d54d713f`  |
| 1226   | No file  | `c375d54d713f`  |
| 1220   | No file  | `c375d54d713f`  |
| 1217   | No file  | `c375d54d713f`  |
| 1211   | No file  | `c375d54d713f`  |
| 1210   | No file  | `c375d54d713f`  |
| 1208   | No file  | `c375d54d713f`  |
| 1203   | No file  | `c375d54d713f`  |
| 1197   | No file  | `c375d54d713f`  |
| 1194   | No file  | `c375d54d713f`  |
| 1192   | No file  | `c375d54d713f`  |
| 1187   | No file  | `c375d54d713f`  |
| 1183   | No file  | `c375d54d713f`  |
| 1177   | No file  | `c375d54d713f`  |
| 1173   | No file  | `c375d54d713f`  |
| 1167   | No file  | `c375d54d713f`  |
| 1164   | No file  | `c375d54d713f`  |
| 1156   | No file  | `c375d54d713f`  |
| 1149   | No file  | `c375d54d713f`  |
| 1144   | No file  | `c375d54d713f`  |
| 1137   | No file  | `c375d54d713f`  |
| 1132   | No file  | `c375d54d713f`  |
| 1127   | No file  | `c375d54d713f`  |
| 1122   | No file  | `c375d54d713f`  |
| 1118   | No file  | `c375d54d713f`  |
| 1114   | No file  | `c375d54d713f`  |
| 1109   | No file  | `c375d54d713f`  |
| 1102   | No file  | `c375d54d713f`  |
| 1096   | No file  | `c375d54d713f`  |
| 1088   | No file  | `c375d54d713f`  |
| 1081   | No file  | `c375d54d713f`  |
| 1076   | No file  | `c375d54d713f`  |
| 1069   | No file  | `c375d54d713f`  |
| 1064   | No file  | `c375d54d713f`  |
| 1058   | No file  | `c375d54d713f`  |
| 1051   | No file  | `c375d54d713f`  |
| 1044   | No file  | `c375d54d713f`  |
| 1036   | No file  | `c375d54d713f`  |
| 1026   | No file  | `c375d54d713f`  |
| 1016   | No file  | `c375d54d713f`  |
| 1009   | No file  | `c375d54d713f`  |
| 1005   | No file  | `c375d54d713f`  |
| 1000   | No file  | `c375d54d713f`  |
| 998    | No file  | `c375d54d713f`  |
| 990    | No file  | `c375d54d713f`  |
| 979    | No file  | `c375d54d713f`  |
| 972    | No file  | `c375d54d713f`  |
| 963    | No file  | `c375d54d713f`  |
| 955    | No file  | `c375d54d713f`  |
| 946    | No file  | `c375d54d713f`  |
| 938    | No file  | `c375d54d713f`  |
| 927    | No file  | `c375d54d713f`  |
| 911    | No file  | `c375d54d713f`  |
| 904    | No file  | `c375d54d713f`  |
| 899    | No file  | `c375d54d713f`  |
| 894    | No file  | `c375d54d713f`  |
| 885    | No file  | `c375d54d713f`  |
| 879    | No file  | `c375d54d713f`  |
| 872    | No file  | `c375d54d713f`  |
| 864    | No file  | `c375d54d713f`  |
| 855    | No file  | `c375d54d713f`  |
| 853    | No file  | `c375d54d713f`  |
| 845    | No file  | `c375d54d713f`  |
| 837    | No file  | `c375d54d713f`  |
| 829    | No file  | `c375d54d713f`  |
| 822    | No file  | `c375d54d713f`  |
| 814    | No file  | `c375d54d713f`  |
| 805    | No file  | `c375d54d713f`  |
| 794    | No file  | `c375d54d713f`  |
| 787    | No file  | `c375d54d713f`  |
| 780    | No file  | `c375d54d713f`  |
| 771    | No file  | `c375d54d713f`  |
| 760    | No file  | `c375d54d713f`  |
| 748    | No file  | `c375d54d713f`  |
| 741    | No file  | `c375d54d713f`  |
| 736    | No file  | `c375d54d713f`  |
| 731    | No file  | `c375d54d713f`  |
| 723    | No file  | `c375d54d713f`  |
| 711    | No file  | `c375d54d713f`  |
| 707    | No file  | `c375d54d713f`  |
| 697    | No file  | `c375d54d713f`  |
| 689    | No file  | `c375d54d713f`  |
| 683    | No file  | `c375d54d713f`  |
| 678    | No file  | `c375d54d713f`  |
| 670    | No file  | `c375d54d713f`  |
| 661    | No file  | `c375d54d713f`  |
| 656    | No file  | `c375d54d713f`  |
| 652    | No file  | `c375d54d713f`  |
| 643    | No file  | `c375d54d713f`  |
| 637    | No file  | `c375d54d713f`  |
| 630    | No file  | `c375d54d713f`  |
| 627    | No file  | `c375d54d713f`  |
| 621    | No file  | `c375d54d713f`  |
| 617    | No file  | `c375d54d713f`  |
| 615    | No file  | `c375d54d713f`  |
| 606    | No file  | `c375d54d713f`  |
| 599    | No file  | `c375d54d713f`  |
| 592    | No file  | `c375d54d713f`  |
| 586    | No file  | `c375d54d713f`  |
| 577    | No file  | `c375d54d713f`  |
| 569    | No file  | `c375d54d713f`  |
| 561    | No file  | `c375d54d713f`  |
| 554    | No file  | `c375d54d713f`  |
| 542    | No file  | `c375d54d713f`  |
| 532    | No file  | `c375d54d713f`  |
| 531    | No file  | `c375d54d713f`  |
| 526    | No file  | `c375d54d713f`  |
| 521    | No file  | `c375d54d713f`  |
| 517    | No file  | `c375d54d713f`  |
| 510    | No file  | `c375d54d713f`  |
| 508    | No file  | `c375d54d713f`  |
| 504    | No file  | `c375d54d713f`  |
| 497    | No file  | `c375d54d713f`  |
| 491    | No file  | `c375d54d713f`  |
| 485    | No file  | `c375d54d713f`  |
| 478    | No file  | `c375d54d713f`  |
| 472    | No file  | `c375d54d713f`  |
| 466    | No file  | `c375d54d713f`  |
| 457    | No file  | `c375d54d713f`  |
| 452    | No file  | `c375d54d713f`  |
| 449    | No file  | `c375d54d713f`  |
| 435    | No file  | `c375d54d713f`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10 at `str_id1=skill_no`    |

Without LOC the handler shows the Korean skill name from `skilltype.dbss`
through the skill name lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field              | Notes                                        |
| ------------------- | ---------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                    | count              | Number of rows                               |
| `+0x08`             | u16                    | unknown_08         | `5` on every client checked, equal to `count` and to the highest `index`; see Open Questions |
| `+0x0A`             | Fever Skill Row[count] | rows               | 10-byte rows repeated `count` times          |
| `rows+0x00`         | String Table           | string_table       | See String Table                             |
| `string_table+0x00` | u32                    | string_table_start | Offset of `string_count`, where the rows end (`10 + 10 * count`) |
| `string_table+0x04` | u32                    | zero               | Always `0`                                   |

The string table has the shape
[`feverquestdatatable.bss`](feverquestdatatable_bss.md) and
`specialquestinfo.bss` use (`_common/pabr_strings.py`). The rows run from
index `5` down to `1`.

### Fever Skill Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                     |
| ------- | ---- | ----------- | ------------------------------------------------------------------------- |
| `+0x00` | u16  | index       | Step, `1` to `5` on client 3474; unique                                   |
| `+0x02` | u16  | skill_level | Skill level of the `gc::SkillKey`; always `1`                             |
| `+0x04` | u16  | skill_no    | Skill number (`SkillNo`); keys the LOC type 10 name; `skill_no << 16 \| skill_level` is the `skill_key` of a `skill.dbss` record |
| `+0x06` | u32  | description | Item drop amount bonus of the skill; 1,000,000 = 100%                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Field Names

The `FeverTimeSkill` sheet of a private server's `DataSheets.bexcel` on
client 1784 has three columns: `Index` (`index`), `SkillNo` (`skill_no`)
and `Description` (`description`). Its 5 rows match the client 1784 file in
all 5 rows, and the client 3474 file is byte for byte the same as the client
1784 one. The sheet has no level column; every row stores `skill_level`
`1`, the level the private server's `FeverTime` loader also gives its
`ClearBuffSkill` key (`SkillNo << 16 | 1`). The server executable of that
private server names the record type `FeverTimeSkillStaticStatus` and its
manager `FeverTimeSkillStaticStatusManager`, which reports a missing row as
`FeverTimeSkillStaticStatusManager SkillKey(%#)`, so it looks rows up by
skill key. The 2016 PDB has no `Fever` symbol.

`description` is the drop bonus. The client Lua reads
`player:getUseFeverSkillDropDesc()`, divides it by 10000 and fills it into
`{feverDropRate}` of `LUA_AGRISSPOINT_ICON_TOOLTIP` ("Item Drop Amount for
loot or basic resources +{feverDropRate}% by consuming points ...") in
`panel_widget_agrisgaugetooltip_1.luac` and
`panel_characterinfo_cashbuff_all_1.luac`. The values `1000000` to
`3000000` give the `+100%` to `+300%` in the skill names of their rows.

## Notes

- Raw rows on client 3474, in file order: index `5` / skill 59045 /
  `3000000`, `4` / 59044 / `2500000`, `3` / 59043 / `2000000`, `2` / 59042 /
  `1500000`, `1` / 58988 / `1000000`. Clients 1485, 1784, 2107, 2519, 3002
  and 3251 ship the same 72 bytes; clients 794 and 1230 have no
  `fevertimeskill.bss`.
- Each skill has one `skill.dbss` record, level `1`, and that record applies
  one buff: 58988 buff 58941, 59042 to 59045 buffs 59467 to 59470.
- The `FeverTime` sheet of the same `DataSheets.bexcel` (one row:
  `MaxPointOfFeverTime` `500000`, `MaxPointLimit`, `MaxPointPerDay`
  `150000`, `MaxPointLimitPerDay`, `SkillNo1` 58988, `SkillNo2` 58989,
  `AcceptConditions` `834,1`, `ClearBuffSkill` 58989, `Description`
  `500000`) is not in this file. The private server's `Load_FeverTime` reads
  it into one server parameter block. Skill 58989 is `Item Drop Quantity
  Effect (Off)` (buff 58942).
- The Lua toggles the buff icon through `getIsUseFeverSkill()` and the
  `FromClient_FeverSkillToggle` event (`panel_personalicon_left_remaster.luac`,
  `panel_widget_agrisgauge_2.luac`). No Lua file names this table or reads
  an index.

## Open Questions

### Field Before the Rows

`unknown_08` is a u16 between the PABR `count` and the first row, `5` on
every client from 1485 to 3474, where `count` and the highest `index` are
`5` as well. No other `.bss` in the test fixtures has a u16 equal to its
count at `+0x08` followed by rows that fill the file up to the string
table. A patch that adds or drops a step would show whether the field
follows `count`, the highest `index`, or neither.

### What Picks the Index

The file does not say which row is active for a family. The Agris tooltip
(LOC type 37, `LUA_AGRISSPOINT_ICON_TOOLTIP`) says completing the "Book of
Margahan" adventure logs Volumes 1 and 2 enhances Agris Fever. BDFoundry's
Book of Margahan guide gives a 100% junk drop increase without the logs
and "Junk item drop amount +50% (When consuming Agris Fever points)" as the
last reward of Book 1, for 150%; Book 2 adds points and daily recovery only
and stays at 150%. In game I started at 100% and had 150% after both
books. That fits index `1` (`1000000`) and index `2` (`1500000`). What
reaches indexes `3` to `5` (200% to 300%) is unknown.
None of the 3,073 client Lua files of client 3474 holds the skill numbers
58988 or 59042 to 59045 as a constant, so the Lua does not show the rule.
