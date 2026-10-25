# `petequipskillaquire.dbss` Format

## Purpose

Defines the skill roll table for pet equip skills, keyed by `acquire_type_id` from [pet.dbss](pet_dbss.md). Each record holds a weight for every skill in [petequipskill.bss](../bss/petequipskill_bss.md), and a weight of `0` means that acquire type cannot roll that skill.

Each acquire type is a themed pool: some favour life skills, others combat and gathering. 21 records cover 5 key groups (`0`–`4`, `101`–`104`, `201`–`204`, `301`–`304`, `401`–`404`), of which key `0` is an empty placeholder.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records          | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | ---------------- | --------- |
| 1      | 1346 and later | `petequipskillaquire.dbss`       | 3,700 | 21 Record        | 176       |
| 1      | 1346 and later | `petequipskillaquireoffset.dbss` | 214   | 21 Offset Record | 10        |

| Layout | File                             | Known            | Unknown      |
| ------ | -------------------------------- | ---------------- | ------------ |
| 1      | `petequipskillaquire.dbss`       | 3,700 B (100.0%) | 0 B (0.0%)   |
| 1      | `petequipskillaquireoffset.dbss` | 172 B (80.4%)    | 42 B (19.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `17bc4786f1cb`  |
| 3482   | Layout 1             | `17bc4786f1cb`  |
| 3474   | Layout 1             | `17bc4786f1cb`  |
| 3473   | Layout 1             | `17bc4786f1cb`  |
| 3464   | Layout 1             | `17bc4786f1cb`  |
| 3458   | Layout 1             | `17bc4786f1cb`  |
| 3454   | Layout 1             | `17bc4786f1cb`  |
| 3444   | Layout 1             | `17bc4786f1cb`  |
| 3435   | Layout 1             | `17bc4786f1cb`  |
| 3426   | Layout 1             | `17bc4786f1cb`  |
| 3418   | Layout 1             | `17bc4786f1cb`  |
| 3412   | Layout 1             | `17bc4786f1cb`  |
| 3402   | Layout 1             | `17bc4786f1cb`  |
| 3396   | Layout 1             | `17bc4786f1cb`  |
| 3387   | Layout 1             | `17bc4786f1cb`  |
| 3381   | Layout 1             | `17bc4786f1cb`  |
| 3373   | Layout 1             | `17bc4786f1cb`  |
| 3364   | Layout 1             | `17bc4786f1cb`  |
| 3356   | Layout 1             | `17bc4786f1cb`  |
| 3349   | Layout 1             | `17bc4786f1cb`  |
| 3342   | Layout 1             | `17bc4786f1cb`  |
| 3335   | Layout 1             | `17bc4786f1cb`  |
| 3326   | Layout 1             | `17bc4786f1cb`  |
| 3321   | Layout 1             | `17bc4786f1cb`  |
| 3314   | Layout 1             | `17bc4786f1cb`  |
| 3303   | Layout 1             | `17bc4786f1cb`  |
| 3302   | Layout 1             | `17bc4786f1cb`  |
| 3293   | Layout 1             | `17bc4786f1cb`  |
| 3283   | Layout 1             | `17bc4786f1cb`  |
| 3275   | Layout 1             | `17bc4786f1cb`  |
| 3267   | Layout 1             | `17bc4786f1cb`  |
| 3258   | Layout 1             | `17bc4786f1cb`  |
| 3251   | Layout 1             | `17bc4786f1cb`  |
| 3242   | Layout 1             | `17bc4786f1cb`  |
| 3235   | Layout 1             | `17bc4786f1cb`  |
| 3229   | Layout 1             | `17bc4786f1cb`  |
| 3212   | Layout 1             | `17bc4786f1cb`  |
| 3203   | Layout 1             | `17bc4786f1cb`  |
| 3193   | Layout 1             | `17bc4786f1cb`  |
| 3186   | Layout 1             | `17bc4786f1cb`  |
| 3177   | Layout 1             | `17bc4786f1cb`  |
| 3169   | Layout 1             | `17bc4786f1cb`  |
| 3158   | Layout 1             | `17bc4786f1cb`  |
| 3151   | Layout 1             | `17bc4786f1cb`  |
| 3144   | Layout 1             | `17bc4786f1cb`  |
| 3133   | Layout 1             | `17bc4786f1cb`  |
| 3125   | Layout 1             | `17bc4786f1cb`  |
| 3118   | Layout 1             | `17bc4786f1cb`  |
| 3111   | Layout 1             | `17bc4786f1cb`  |
| 3103   | Layout 1             | `17bc4786f1cb`  |
| 3095   | Layout 1             | `17bc4786f1cb`  |
| 3086   | Layout 1             | `17bc4786f1cb`  |
| 3072   | Layout 1             | `17bc4786f1cb`  |
| 3062   | Layout 1             | `17bc4786f1cb`  |
| 3052   | Layout 1             | `17bc4786f1cb`  |
| 3045   | Layout 1             | `17bc4786f1cb`  |
| 3037   | Layout 1             | `17bc4786f1cb`  |
| 3030   | Layout 1             | `17bc4786f1cb`  |
| 3021   | Layout 1             | `17bc4786f1cb`  |
| 3012   | Layout 1             | `17bc4786f1cb`  |
| 3002   | Layout 1             | `17bc4786f1cb`  |
| 2995   | Layout 1             | `17bc4786f1cb`  |
| 2987   | Layout 1             | `17bc4786f1cb`  |
| 2978   | Layout 1             | `17bc4786f1cb`  |
| 2970   | Layout 1             | `17bc4786f1cb`  |
| 2959   | Layout 1             | `17bc4786f1cb`  |
| 2951   | Layout 1             | `17bc4786f1cb`  |
| 2942   | Layout 1             | `17bc4786f1cb`  |
| 2935   | Layout 1             | `17bc4786f1cb`  |
| 2932   | Layout 1             | `17bc4786f1cb`  |
| 2923   | Layout 1             | `17bc4786f1cb`  |
| 2919   | Layout 1             | `17bc4786f1cb`  |
| 2907   | Layout 1             | `17bc4786f1cb`  |
| 2900   | Layout 1             | `17bc4786f1cb`  |
| 2891   | Layout 1             | `17bc4786f1cb`  |
| 2882   | Layout 1             | `17bc4786f1cb`  |
| 2872   | Layout 1             | `17bc4786f1cb`  |
| 2863   | Layout 1             | `17bc4786f1cb`  |
| 2855   | Layout 1             | `17bc4786f1cb`  |
| 2849   | Layout 1             | `17bc4786f1cb`  |
| 2844   | Layout 1             | `17bc4786f1cb`  |
| 2834   | Layout 1             | `17bc4786f1cb`  |
| 2825   | Layout 1             | `17bc4786f1cb`  |
| 2819   | Layout 1             | `17bc4786f1cb`  |
| 2811   | Layout 1             | `17bc4786f1cb`  |
| 2803   | Layout 1             | `17bc4786f1cb`  |
| 2794   | Layout 1             | `17bc4786f1cb`  |
| 2783   | Layout 1             | `17bc4786f1cb`  |
| 2774   | Layout 1             | `17bc4786f1cb`  |
| 2765   | Layout 1             | `17bc4786f1cb`  |
| 2756   | Layout 1             | `17bc4786f1cb`  |
| 2750   | Layout 1             | `17bc4786f1cb`  |
| 2743   | Layout 1             | `17bc4786f1cb`  |
| 2736   | Layout 1             | `17bc4786f1cb`  |
| 2726   | Layout 1             | `17bc4786f1cb`  |
| 2717   | Layout 1             | `17bc4786f1cb`  |
| 2709   | Layout 1             | `17bc4786f1cb`  |
| 2703   | Layout 1             | `17bc4786f1cb`  |
| 2695   | Layout 1             | `17bc4786f1cb`  |
| 2684   | Layout 1             | `17bc4786f1cb`  |
| 2672   | Layout 1             | `17bc4786f1cb`  |
| 2665   | Layout 1             | `17bc4786f1cb`  |
| 2657   | Layout 1             | `17bc4786f1cb`  |
| 2649   | Layout 1             | `17bc4786f1cb`  |
| 2644   | Layout 1             | `17bc4786f1cb`  |
| 2637   | Layout 1             | `17bc4786f1cb`  |
| 2629   | Layout 1             | `17bc4786f1cb`  |
| 2619   | Layout 1             | `17bc4786f1cb`  |
| 2612   | Layout 1             | `17bc4786f1cb`  |
| 2606   | Layout 1             | `17bc4786f1cb`  |
| 2602   | Layout 1             | `17bc4786f1cb`  |
| 2601   | Layout 1             | `17bc4786f1cb`  |
| 2592   | Layout 1             | `17bc4786f1cb`  |
| 2583   | Layout 1             | `17bc4786f1cb`  |
| 2575   | Layout 1             | `17bc4786f1cb`  |
| 2567   | Layout 1             | `17bc4786f1cb`  |
| 2560   | Layout 1             | `17bc4786f1cb`  |
| 2553   | Layout 1             | `17bc4786f1cb`  |
| 2545   | Layout 1             | `17bc4786f1cb`  |
| 2538   | Layout 1             | `17bc4786f1cb`  |
| 2529   | Layout 1             | `17bc4786f1cb`  |
| 2519   | Layout 1             | `17bc4786f1cb`  |
| 2513   | Layout 1             | `17bc4786f1cb`  |
| 2510   | Layout 1             | `17bc4786f1cb`  |
| 2507   | Layout 1             | `17bc4786f1cb`  |
| 2503   | Layout 1             | `17bc4786f1cb`  |
| 2498   | Layout 1             | `17bc4786f1cb`  |
| 2492   | Layout 1             | `17bc4786f1cb`  |
| 2487   | Layout 1             | `17bc4786f1cb`  |
| 2480   | Layout 1             | `17bc4786f1cb`  |
| 2474   | Layout 1             | `17bc4786f1cb`  |
| 2468   | Layout 1             | `17bc4786f1cb`  |
| 2460   | Layout 1             | `17bc4786f1cb`  |
| 2453   | Layout 1             | `17bc4786f1cb`  |
| 2444   | Layout 1             | `17bc4786f1cb`  |
| 2438   | Layout 1             | `17bc4786f1cb`  |
| 2434   | Layout 1             | `17bc4786f1cb`  |
| 2429   | Layout 1             | `17bc4786f1cb`  |
| 2421   | Layout 1             | `17bc4786f1cb`  |
| 2414   | Layout 1             | `17bc4786f1cb`  |
| 2407   | Layout 1             | `17bc4786f1cb`  |
| 2401   | Layout 1             | `17bc4786f1cb`  |
| 2397   | Layout 1             | `17bc4786f1cb`  |
| 2393   | Layout 1             | `17bc4786f1cb`  |
| 2384   | Layout 1             | `17bc4786f1cb`  |
| 2378   | Layout 1             | `17bc4786f1cb`  |
| 2372   | Layout 1             | `17bc4786f1cb`  |
| 2358   | Layout 1             | `17bc4786f1cb`  |
| 2352   | Layout 1             | `17bc4786f1cb`  |
| 2347   | Layout 1             | `17bc4786f1cb`  |
| 2343   | Layout 1             | `17bc4786f1cb`  |
| 2335   | Layout 1             | `17bc4786f1cb`  |
| 2327   | Layout 1             | `17bc4786f1cb`  |
| 2324   | Layout 1             | `17bc4786f1cb`  |
| 2319   | Layout 1             | `17bc4786f1cb`  |
| 2313   | Layout 1             | `17bc4786f1cb`  |
| 2308   | Layout 1             | `17bc4786f1cb`  |
| 2302   | Layout 1             | `17bc4786f1cb`  |
| 2295   | Layout 1             | `17bc4786f1cb`  |
| 2290   | Layout 1             | `17bc4786f1cb`  |
| 2284   | Layout 1             | `17bc4786f1cb`  |
| 2276   | Layout 1             | `17bc4786f1cb`  |
| 2269   | Layout 1             | `17bc4786f1cb`  |
| 2259   | Layout 1             | `17bc4786f1cb`  |
| 2250   | Layout 1             | `17bc4786f1cb`  |
| 2243   | Layout 1             | `17bc4786f1cb`  |
| 2235   | Layout 1             | `17bc4786f1cb`  |
| 2229   | Layout 1             | `17bc4786f1cb`  |
| 2224   | Layout 1             | `17bc4786f1cb`  |
| 2218   | Layout 1             | `17bc4786f1cb`  |
| 2215   | Layout 1             | `17bc4786f1cb`  |
| 2207   | Layout 1             | `17bc4786f1cb`  |
| 2203   | Layout 1             | `17bc4786f1cb`  |
| 2196   | Layout 1             | `17bc4786f1cb`  |
| 2192   | Layout 1             | `17bc4786f1cb`  |
| 2189   | Layout 1             | `17bc4786f1cb`  |
| 2183   | Layout 1             | `17bc4786f1cb`  |
| 2179   | Layout 1             | `17bc4786f1cb`  |
| 2171   | Layout 1             | `17bc4786f1cb`  |
| 2163   | Layout 1             | `17bc4786f1cb`  |
| 2156   | Layout 1             | `17bc4786f1cb`  |
| 2151   | Layout 1             | `17bc4786f1cb`  |
| 2147   | Layout 1             | `17bc4786f1cb`  |
| 2142   | Layout 1             | `17bc4786f1cb`  |
| 2138   | Layout 1             | `17bc4786f1cb`  |
| 2134   | Layout 1             | `17bc4786f1cb`  |
| 2130   | Layout 1             | `17bc4786f1cb`  |
| 2122   | Layout 1             | `17bc4786f1cb`  |
| 2107   | Layout 1             | `17bc4786f1cb`  |
| 2098   | Layout 1             | `17bc4786f1cb`  |
| 2089   | Layout 1             | `17bc4786f1cb`  |
| 2081   | Layout 1             | `17bc4786f1cb`  |
| 2073   | Layout 1             | `17bc4786f1cb`  |
| 2067   | Layout 1             | `17bc4786f1cb`  |
| 2063   | Layout 1             | `17bc4786f1cb`  |
| 2059   | Layout 1             | `17bc4786f1cb`  |
| 2052   | Layout 1             | `17bc4786f1cb`  |
| 2044   | Layout 1             | `17bc4786f1cb`  |
| 2039   | Layout 1             | `17bc4786f1cb`  |
| 2032   | Layout 1             | `17bc4786f1cb`  |
| 2025   | Layout 1             | `17bc4786f1cb`  |
| 2011   | Layout 1             | `17bc4786f1cb`  |
| 2005   | Layout 1             | `17bc4786f1cb`  |
| 2000   | Layout 1             | `17bc4786f1cb`  |
| 1996   | Layout 1             | `17bc4786f1cb`  |
| 1991   | Layout 1             | `17bc4786f1cb`  |
| 1985   | Layout 1             | `17bc4786f1cb`  |
| 1980   | Layout 1             | `17bc4786f1cb`  |
| 1969   | Layout 1             | `17bc4786f1cb`  |
| 1964   | Layout 1             | `17bc4786f1cb`  |
| 1958   | Layout 1             | `17bc4786f1cb`  |
| 1950   | Layout 1             | `17bc4786f1cb`  |
| 1945   | Layout 1             | `17bc4786f1cb`  |
| 1937   | Layout 1             | `17bc4786f1cb`  |
| 1933   | Layout 1             | `17bc4786f1cb`  |
| 1927   | Layout 1             | `17bc4786f1cb`  |
| 1921   | Layout 1             | `17bc4786f1cb`  |
| 1914   | Layout 1             | `17bc4786f1cb`  |
| 1908   | Layout 1             | `17bc4786f1cb`  |
| 1897   | Layout 1             | `17bc4786f1cb`  |
| 1892   | Layout 1             | `17bc4786f1cb`  |
| 1886   | Layout 1             | `17bc4786f1cb`  |
| 1881   | Layout 1             | `17bc4786f1cb`  |
| 1871   | Layout 1             | `17bc4786f1cb`  |
| 1866   | Layout 1             | `17bc4786f1cb`  |
| 1862   | Layout 1             | `17bc4786f1cb`  |
| 1854   | Layout 1             | `17bc4786f1cb`  |
| 1846   | Layout 1             | `17bc4786f1cb`  |
| 1838   | Layout 1             | `17bc4786f1cb`  |
| 1832   | Layout 1             | `17bc4786f1cb`  |
| 1826   | Layout 1             | `17bc4786f1cb`  |
| 1822   | Layout 1             | `17bc4786f1cb`  |
| 1818   | Layout 1             | `17bc4786f1cb`  |
| 1804   | Layout 1             | `17bc4786f1cb`  |
| 1794   | Layout 1             | `17bc4786f1cb`  |
| 1790   | Layout 1             | `17bc4786f1cb`  |
| 1784   | Layout 1             | `17bc4786f1cb`  |
| 1774   | Layout 1             | `17bc4786f1cb`  |
| 1771   | Layout 1             | `17bc4786f1cb`  |
| 1762   | Layout 1             | `17bc4786f1cb`  |
| 1759   | Layout 1             | `17bc4786f1cb`  |
| 1754   | Layout 1             | `17bc4786f1cb`  |
| 1749   | Layout 1             | `17bc4786f1cb`  |
| 1743   | Layout 1             | `17bc4786f1cb`  |
| 1737   | Layout 1             | `17bc4786f1cb`  |
| 1731   | Layout 1             | `17bc4786f1cb`  |
| 1725   | Layout 1             | `17bc4786f1cb`  |
| 1717   | Layout 1             | `17bc4786f1cb`  |
| 1710   | Layout 1             | `17bc4786f1cb`  |
| 1704   | Layout 1             | `17bc4786f1cb`  |
| 1698   | Layout 1             | `17bc4786f1cb`  |
| 1690   | Layout 1             | `17bc4786f1cb`  |
| 1685   | Layout 1             | `17bc4786f1cb`  |
| 1680   | Layout 1             | `17bc4786f1cb`  |
| 1674   | Layout 1             | `17bc4786f1cb`  |
| 1668   | Layout 1             | `17bc4786f1cb`  |
| 1659   | Layout 1             | `17bc4786f1cb`  |
| 1649   | Layout 1             | `17bc4786f1cb`  |
| 1642   | Layout 1             | `17bc4786f1cb`  |
| 1636   | Layout 1             | `17bc4786f1cb`  |
| 1628   | Layout 1             | `17bc4786f1cb`  |
| 1622   | Layout 1             | `17bc4786f1cb`  |
| 1614   | Layout 1             | `17bc4786f1cb`  |
| 1608   | Layout 1             | `17bc4786f1cb`  |
| 1602   | Layout 1             | `17bc4786f1cb`  |
| 1598   | Layout 1             | `17bc4786f1cb`  |
| 1594   | Layout 1             | `17bc4786f1cb`  |
| 1590   | Layout 1             | `17bc4786f1cb`  |
| 1587   | Layout 1             | `17bc4786f1cb`  |
| 1584   | Layout 1             | `17bc4786f1cb`  |
| 1579   | Layout 1             | `17bc4786f1cb`  |
| 1572   | Layout 1             | `17bc4786f1cb`  |
| 1565   | Layout 1             | `17bc4786f1cb`  |
| 1559   | Layout 1             | `17bc4786f1cb`  |
| 1554   | Layout 1             | `17bc4786f1cb`  |
| 1547   | Layout 1             | `17bc4786f1cb`  |
| 1537   | Layout 1             | `17bc4786f1cb`  |
| 1529   | Layout 1             | `17bc4786f1cb`  |
| 1524   | Layout 1             | `17bc4786f1cb`  |
| 1519   | Layout 1             | `17bc4786f1cb`  |
| 1509   | Layout 1             | `17bc4786f1cb`  |
| 1506   | Layout 1             | `17bc4786f1cb`  |
| 1504   | Layout 1             | `17bc4786f1cb`  |
| 1500   | Layout 1             | `17bc4786f1cb`  |
| 1493   | Layout 1             | `17bc4786f1cb`  |
| 1489   | Layout 1             | `17bc4786f1cb`  |
| 1485   | Layout 1             | `17bc4786f1cb`  |
| 1481   | Layout 1             | `17bc4786f1cb`  |
| 1474   | Layout 1             | `17bc4786f1cb`  |
| 1466   | Layout 1             | `17bc4786f1cb`  |
| 1462   | Layout 1             | `17bc4786f1cb`  |
| 1459   | Layout 1             | `17bc4786f1cb`  |
| 1453   | Layout 1             | `17bc4786f1cb`  |
| 1450   | Layout 1             | `17bc4786f1cb`  |
| 1445   | Layout 1             | `17bc4786f1cb`  |
| 1439   | Layout 1             | `17bc4786f1cb`  |
| 1433   | Layout 1             | `17bc4786f1cb`  |
| 1430   | Layout 1             | `17bc4786f1cb`  |
| 1426   | Layout 1             | `17bc4786f1cb`  |
| 1421   | Layout 1             | `17bc4786f1cb`  |
| 1417   | Layout 1             | `17bc4786f1cb`  |
| 1416   | Layout 1             | `17bc4786f1cb`  |
| 1409   | Layout 1             | `17bc4786f1cb`  |
| 1405   | Layout 1             | `17bc4786f1cb`  |
| 1401   | Layout 1             | `17bc4786f1cb`  |
| 1396   | Layout 1             | `17bc4786f1cb`  |
| 1391   | Layout 1             | `17bc4786f1cb`  |
| 1390   | Layout 1             | `17bc4786f1cb`  |
| 1386   | Layout 1             | `17bc4786f1cb`  |
| 1381   | Layout 1             | `17bc4786f1cb`  |
| 1379   | Layout 1             | `17bc4786f1cb`  |
| 1372   | Layout 1             | `17bc4786f1cb`  |
| 1366   | Layout 1             | `17bc4786f1cb`  |
| 1364   | Layout 1             | `17bc4786f1cb`  |
| 1363   | Layout 1             | `17bc4786f1cb`  |
| 1360   | Layout 1             | `17bc4786f1cb`  |
| 1358   | Layout 1             | `17bc4786f1cb`  |
| 1355   | Layout 1             | `17bc4786f1cb`  |
| 1351   | Layout 1             | `17bc4786f1cb`  |
| 1348   | Layout 1             | `17bc4786f1cb`  |
| 1346   | Layout 1             | `17bc4786f1cb`  |
| 1341   | No documented layout | `17bc4786f1cb`  |
| 1340   | No documented layout | `17bc4786f1cb`  |
| 1338   | No documented layout | `17bc4786f1cb`  |
| 1335   | No documented layout | `17bc4786f1cb`  |
| 1333   | No documented layout | `17bc4786f1cb`  |
| 1329   | No documented layout | `17bc4786f1cb`  |
| 1327   | No documented layout | `17bc4786f1cb`  |
| 1324   | No documented layout | `17bc4786f1cb`  |
| 1321   | No documented layout | `17bc4786f1cb`  |
| 1319   | No documented layout | `17bc4786f1cb`  |
| 1318   | No documented layout | `17bc4786f1cb`  |
| 1316   | No documented layout | `17bc4786f1cb`  |
| 1313   | No documented layout | `17bc4786f1cb`  |
| 1311   | No documented layout | `17bc4786f1cb`  |
| 1309   | No documented layout | `17bc4786f1cb`  |
| 1304   | No documented layout | `17bc4786f1cb`  |
| 1292   | No documented layout | `17bc4786f1cb`  |
| 1286   | No documented layout | `17bc4786f1cb`  |
| 1280   | No file              | `17bc4786f1cb`  |
| 1276   | No file              | `17bc4786f1cb`  |
| 1267   | No documented layout | `17bc4786f1cb`  |
| 1261   | No documented layout | `17bc4786f1cb`  |
| 1256   | No file              | `17bc4786f1cb`  |
| 1250   | No file              | `17bc4786f1cb`  |
| 1246   | No file              | `17bc4786f1cb`  |
| 1239   | No file              | `17bc4786f1cb`  |
| 1230   | No file              | `17bc4786f1cb`  |
| 1226   | No file              | `17bc4786f1cb`  |
| 1220   | No file              | `17bc4786f1cb`  |
| 1217   | No file              | `17bc4786f1cb`  |
| 1211   | No file              | `17bc4786f1cb`  |
| 1210   | No file              | `17bc4786f1cb`  |
| 1208   | No file              | `17bc4786f1cb`  |
| 1203   | No file              | `17bc4786f1cb`  |
| 1197   | No file              | `17bc4786f1cb`  |
| 1194   | No file              | `17bc4786f1cb`  |
| 1192   | No file              | `17bc4786f1cb`  |
| 1187   | No file              | `17bc4786f1cb`  |
| 1183   | No file              | `17bc4786f1cb`  |
| 1177   | No file              | `17bc4786f1cb`  |
| 1173   | No file              | `17bc4786f1cb`  |
| 1167   | No file              | `17bc4786f1cb`  |
| 1164   | No file              | `17bc4786f1cb`  |
| 1156   | No file              | `17bc4786f1cb`  |
| 1149   | No file              | `17bc4786f1cb`  |
| 1144   | No file              | `17bc4786f1cb`  |
| 1137   | No file              | `17bc4786f1cb`  |
| 1132   | No file              | `17bc4786f1cb`  |
| 1127   | No file              | `17bc4786f1cb`  |
| 1122   | No file              | `17bc4786f1cb`  |
| 1118   | No file              | `17bc4786f1cb`  |
| 1114   | No file              | `17bc4786f1cb`  |
| 1109   | No file              | `17bc4786f1cb`  |
| 1102   | No file              | `17bc4786f1cb`  |
| 1096   | No file              | `17bc4786f1cb`  |
| 1088   | No file              | `17bc4786f1cb`  |
| 1081   | No file              | `17bc4786f1cb`  |
| 1076   | No file              | `17bc4786f1cb`  |
| 1069   | No file              | `17bc4786f1cb`  |
| 1064   | No file              | `17bc4786f1cb`  |
| 1058   | No file              | `17bc4786f1cb`  |
| 1051   | No file              | `17bc4786f1cb`  |
| 1044   | No file              | `17bc4786f1cb`  |
| 1036   | No file              | `17bc4786f1cb`  |
| 1026   | No file              | `17bc4786f1cb`  |
| 1016   | No file              | `17bc4786f1cb`  |
| 1009   | No file              | `17bc4786f1cb`  |
| 1005   | No file              | `17bc4786f1cb`  |
| 1000   | No file              | `17bc4786f1cb`  |
| 998    | No file              | `17bc4786f1cb`  |
| 990    | No file              | `17bc4786f1cb`  |
| 979    | No file              | `17bc4786f1cb`  |
| 972    | No file              | `17bc4786f1cb`  |
| 963    | No file              | `17bc4786f1cb`  |
| 955    | No file              | `17bc4786f1cb`  |
| 946    | No file              | `17bc4786f1cb`  |
| 938    | No file              | `17bc4786f1cb`  |
| 927    | No file              | `17bc4786f1cb`  |
| 911    | No file              | `17bc4786f1cb`  |
| 904    | No file              | `17bc4786f1cb`  |
| 899    | No file              | `17bc4786f1cb`  |
| 894    | No file              | `17bc4786f1cb`  |
| 885    | No file              | `17bc4786f1cb`  |
| 879    | No file              | `17bc4786f1cb`  |
| 872    | No file              | `17bc4786f1cb`  |
| 864    | No file              | `17bc4786f1cb`  |
| 855    | No file              | `17bc4786f1cb`  |
| 853    | No file              | `17bc4786f1cb`  |
| 845    | No file              | `17bc4786f1cb`  |
| 837    | No file              | `17bc4786f1cb`  |
| 829    | No file              | `17bc4786f1cb`  |
| 822    | No file              | `17bc4786f1cb`  |
| 814    | No file              | `17bc4786f1cb`  |
| 805    | No file              | `17bc4786f1cb`  |
| 794    | No file              | `17bc4786f1cb`  |
| 787    | No file              | `17bc4786f1cb`  |
| 780    | No file              | `17bc4786f1cb`  |
| 771    | No file              | `17bc4786f1cb`  |
| 760    | No file              | `17bc4786f1cb`  |
| 748    | No file              | `17bc4786f1cb`  |
| 741    | No file              | `17bc4786f1cb`  |
| 736    | No file              | `17bc4786f1cb`  |
| 731    | No file              | `17bc4786f1cb`  |
| 723    | No file              | `17bc4786f1cb`  |
| 711    | No file              | `17bc4786f1cb`  |
| 707    | No file              | `17bc4786f1cb`  |
| 697    | No file              | `17bc4786f1cb`  |
| 689    | No file              | `17bc4786f1cb`  |
| 683    | No file              | `17bc4786f1cb`  |
| 678    | No file              | `17bc4786f1cb`  |
| 670    | No file              | `17bc4786f1cb`  |
| 661    | No file              | `17bc4786f1cb`  |
| 656    | No file              | `17bc4786f1cb`  |
| 652    | No file              | `17bc4786f1cb`  |
| 643    | No file              | `17bc4786f1cb`  |
| 637    | No file              | `17bc4786f1cb`  |
| 630    | No file              | `17bc4786f1cb`  |
| 627    | No file              | `17bc4786f1cb`  |
| 621    | No file              | `17bc4786f1cb`  |
| 617    | No file              | `17bc4786f1cb`  |
| 615    | No file              | `17bc4786f1cb`  |
| 606    | No file              | `17bc4786f1cb`  |
| 599    | No file              | `17bc4786f1cb`  |
| 592    | No file              | `17bc4786f1cb`  |
| 586    | No file              | `17bc4786f1cb`  |
| 577    | No file              | `17bc4786f1cb`  |
| 569    | No file              | `17bc4786f1cb`  |
| 561    | No file              | `17bc4786f1cb`  |
| 554    | No file              | `17bc4786f1cb`  |
| 542    | No file              | `17bc4786f1cb`  |
| 532    | No file              | `17bc4786f1cb`  |
| 531    | No file              | `17bc4786f1cb`  |
| 526    | No file              | `17bc4786f1cb`  |
| 521    | No file              | `17bc4786f1cb`  |
| 517    | No file              | `17bc4786f1cb`  |
| 510    | No file              | `17bc4786f1cb`  |
| 508    | No file              | `17bc4786f1cb`  |
| 504    | No file              | `17bc4786f1cb`  |
| 497    | No file              | `17bc4786f1cb`  |
| 491    | No file              | `17bc4786f1cb`  |
| 485    | No file              | `17bc4786f1cb`  |
| 478    | No file              | `17bc4786f1cb`  |
| 472    | No file              | `17bc4786f1cb`  |
| 466    | No file              | `17bc4786f1cb`  |
| 457    | No file              | `17bc4786f1cb`  |
| 452    | No file              | `17bc4786f1cb`  |
| 449    | No file              | `17bc4786f1cb`  |
| 435    | No file              | `17bc4786f1cb`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                 |
| -------------------------------- | -------- | ---------------------------------------------------- |
| `petequipskillaquireoffset.dbss` | Required | `acquire_type_id → (data_offset, data_size)` index   |
| `petequipskill.bss`              | Optional | Resolves a weight's `equip_skill_id` to a skill name |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                            |
| ------- | ------------- | ------- | -------------------------------- |
| `+0x00` | u32           | count   | Number of records; observed `21` |
| `+0x04` | Record[count] | records | See Record                       |

### Record (176 bytes)

| Offset  | Type    | Field      | Notes                                          |
| ------- | ------- | ---------- | ---------------------------------------------- |
| `+0x00` | u32     | packed_key | `(acquire_type_id << 16) \| acquire_type_id`   |
| `+0x04` | u32[43] | weights    | Roll weight per `equip_skill_id`               |

`4 + 43 × 4 = 176` bytes exactly. `weights[i]` is the weight of the skill whose `equip_skill_id` is `i` in Section 1 of the catalog; index `0` is the first weight, **not** a reserved field.

The first 2 bytes of each record are the file key prefix. The offset companion points to `record_start + 2`, so use `record_start = data_offset - 2` to read the full u32-aligned record.

### `petequipskillaquireoffset.dbss`

| Offset  | Type                 | Field | Notes                                              |
| ------- | -------------------- | ----- | -------------------------------------------------- |
| `+0x00` | u32                  | count | Must equal `petequipskillaquire.dbss` count (`21`) |
| `+0x04` | Offset Record[count] | rows  | See Offset Record                                  |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | key         | `acquire_type_id`                                            |
| `+0x02` | u32  | data_offset | Absolute byte offset in the main file past the 2-byte prefix |
| `+0x06` | u16  | data_size   | Always `174` (`176 - 2-byte key prefix`)                     |
| `+0x08` | u16  | unknown_08  | Always `0`                                                   |

## Acquire Type IDs

Keys decompose as `group × 100 + tier`, except the low keys `0`–`4` which have group `0`.

| Key group   | Meaning                                              |
| ----------- | ---------------------------------------------------- |
| `0`         | Empty placeholder, all 43 weights are `0`           |
| `1`–`4`     | Life-skill oriented pool                             |
| `101`–`104` | Hunting / Training / Trading / Fishing oriented pool |
| `201`–`204` | Combat, Gathering and Fishing oriented pool          |
| `301`–`304` | Byte-identical to `201`–`204`                        |
| `401`–`404` | Broad, near-even pool across most skills             |

## Rollable Skills

Only 14 of the catalog's 43 Section 1 entries carry a non-zero weight in any record, and the same 14 appear in every populated record. Each is the middle entry of its three-entry skill type group, the `+5%` tier, or the sole entry where the group has only one.

| equip_skill_id | skill_type | Skill               |
| -------------- | ---------- | ------------------- |
| 1              | 1          | Karma Recovery +5%  |
| 4              | 2          | Combat EXP +5%      |
| 7              | 3          | Gathering EXP +5%   |
| 9              | 4          | Luck +1             |
| 10             | 5          | Fishing Speed +1    |
| 11             | 6          | Gathering Speed +1  |
| 15             | 8          | Fishing EXP +5%     |
| 18             | 9          | Hunting EXP +5%     |
| 21             | 10         | Cooking EXP +5%     |
| 24             | 11         | Alchemy EXP +5%     |
| 27             | 12         | Processing EXP +5%  |
| 30             | 13         | Training EXP +5%    |
| 33             | 14         | Trading EXP +5%     |
| 36             | 15         | Farming EXP +5%     |

Skill types 7, 16, 17, 18, 19 and 20 (Death Penalty Resist, Life EXP, Weight Limit, Durability Resistance, Skill EXP, Knowledge Gain) have no weight in any record and are never rolled here.

## Roll Chances

Chance is `weight / total_weight` for that record. Values below are percentages.

| Skill                  | 1    | 2    | 3    | 4    | 101  | 102  | 103  | 104  | 201  | 202  | 203  | 204  | 301  | 302  | 303  | 304  | 401  | 402  | 403  | 404  |
| ---------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Karma Recovery +5%     | 12.4 | 12.4 | 15.8 | 15.8 | 14.5 | 14.1 | 18.0 | 18.0 | 16.9 | 16.9 | 21.3 | 21.3 | 16.9 | 16.9 | 21.3 | 21.3 | 1.4  | 1.4  | 1.4  | 1.4  |
| Combat EXP +5%         | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Gathering EXP +5%      | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Luck +1                | 3.1  | 3.1  | 3.0  | 3.0  | 3.6  | 3.5  | 3.4  | 3.4  | 4.2  | 4.2  | 4.0  | 4.0  | 4.2  | 4.2  | 4.0  | 4.0  | 7.1  | 7.1  | 7.1  | 7.1  |
| Fishing Speed +1       | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 3.5  | 3.4  | 3.4  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 7.1  | 7.1  | 7.1  | 7.1  |
| Gathering Speed +1     | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 4.2  | 4.2  | 4.0  | 4.0  | 4.2  | 4.2  | 4.0  | 4.0  | 7.1  | 7.1  | 7.1  | 7.1  |
| Fishing EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 18.1 | 17.6 | 16.9 | 16.9 | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Hunting EXP +5%        | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 17.1 | 17.1 | 17.1 | 17.1 |
| Cooking EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Alchemy EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Processing EXP +5%     | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Training EXP +5%       | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Trading EXP +5%        | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Farming EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |

### Record Totals

Unlike the fairy table, pet weights are **not** normalised to `1,000,000`:

| Total weight | Acquire types                          |
| ------------ | -------------------------------------- |
| `700,000`    | `401`, `402`, `403`, `404`             |
| `710,000`    | `201`, `202`, `301`, `302`             |
| `750,000`    | `203`, `204`, `303`, `304`             |
| `830,000`    | `101`                                  |
| `850,000`    | `102`                                  |
| `890,000`    | `103`, `104`                           |
| `970,000`    | `1`, `2`                               |
| `1,010,000`  | `3`, `4`                               |
| `0`          | `0` (placeholder)                      |

Because `3` and `4` exceed `1,000,000`, these cannot be parts-per-million probabilities the way the fairy weights are. Treat them as relative weights and normalise by the record total.

## Notes

- Weights are roll weights, not costs. Earlier revisions of this document described the record as a cost table with `cost_a`/`cost_b`/`cost_c` triples and a `reserved` field; that reading was wrong. The record is a flat 43-element weight array and the "reserved" u32 is `weights[0]`.
- The layout is shared with [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), where the same structure is confirmed against published per-grade skill availability and every record sums to exactly `1,000,000`.
- Weights index Section 1 of `petequipskill.bss` (`equip_skill_id` `0`–`42`), which is exactly the 43 available slots. The extended Section 2 catalog is not addressable here.
- `301`–`304` are byte-identical to `201`–`204`, and `401`–`404` are identical to each other. Several other keys pair up (`1`=`2`, `3`=`4`, `103`=`104`).
- Only the `+5%` mid-tier of each skill group is rollable; the `+7%` and duplicate `+5%` entries never appear.
- Observed: 21 records and 280 non-zero weights (20 populated records × 14 skills) in the pre-2026-09-27 fixture and in the 2026-09-27 client; both files are byte-identical between the two.

## Open Questions

### Weight normalisation

Fairy records sum to exactly `1,000,000`, but pet totals range from `700,000` to `1,010,000`. Whether the shortfall is a chance of no skill being granted, whether the client normalises by the record total, or whether `3`/`4` exceeding a million is a data error, is unconfirmed.

### Acquire type grouping

The `group × 100 + tier` split fits the key values, and the pools are themed by skill category, but which pet species or grade maps to which group has not been traced through `pet.dbss`. The exact duplication of `201`–`204` by `301`–`304` suggests one group is a reserved or legacy copy.

### Sub-entry semantic mapping

Resolved. The former "14 sub-entries with `cost_a`/`cost_b`/`cost_c`" structure does not exist; the apparent triples were an artifact of grouping a dense 43-element array into 12-byte rows, and the 14 "active" sub-entries were the 14 rollable skills. This entry is retained so the disproven reading is not re-derived.
