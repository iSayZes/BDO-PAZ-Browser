# `fairyequipskillaquire.dbss` Format

## Purpose

Defines the skill roll table used when a fairy's skills are changed. Each record is one fairy grade and holds a weight for every skill in [fairyequipskill.bss](fairyequipskill_bss.md), expressed in parts-per-million. A weight of `0` means that grade cannot roll that skill.

This is the data behind the "% chance to obtain the new skill" the game shows on the Change Skill window.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | --------------- | --------- |
| 1      | 1346 and later | 3483    | `fairyequipskillaquire.dbss`       | 708   | 4 Record        | 176       |
| 1      | 1346 and later | 3483    | `fairyequipskillaquireoffset.dbss` | 44    | 4 Offset Record | 10        |

| Layout | File                               | Known          | Unknown     |
| ------ | ---------------------------------- | -------------- | ----------- |
| 1      | `fairyequipskillaquire.dbss`       | 708 B (100.0%) | 0 B (0.0%)  |
| 1      | `fairyequipskillaquireoffset.dbss` | 36 B (81.8%)   | 8 B (18.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1287b22348d1`  |
| 3482   | Layout 1             | `1287b22348d1`  |
| 3474   | Layout 1             | `1287b22348d1`  |
| 3473   | Layout 1             | `1287b22348d1`  |
| 3464   | Layout 1             | `1287b22348d1`  |
| 3458   | Layout 1             | `1287b22348d1`  |
| 3454   | Layout 1             | `1287b22348d1`  |
| 3444   | Layout 1             | `1287b22348d1`  |
| 3435   | Layout 1             | `1287b22348d1`  |
| 3426   | Layout 1             | `1287b22348d1`  |
| 3418   | Layout 1             | `1287b22348d1`  |
| 3412   | Layout 1             | `1287b22348d1`  |
| 3402   | Layout 1             | `1287b22348d1`  |
| 3396   | Layout 1             | `1287b22348d1`  |
| 3387   | Layout 1             | `1287b22348d1`  |
| 3381   | Layout 1             | `1287b22348d1`  |
| 3373   | Layout 1             | `1287b22348d1`  |
| 3364   | Layout 1             | `1287b22348d1`  |
| 3356   | Layout 1             | `1287b22348d1`  |
| 3349   | Layout 1             | `1287b22348d1`  |
| 3342   | Layout 1             | `1287b22348d1`  |
| 3335   | Layout 1             | `1287b22348d1`  |
| 3326   | Layout 1             | `1287b22348d1`  |
| 3321   | Layout 1             | `1287b22348d1`  |
| 3314   | Layout 1             | `1287b22348d1`  |
| 3303   | Layout 1             | `1287b22348d1`  |
| 3302   | Layout 1             | `1287b22348d1`  |
| 3293   | Layout 1             | `1287b22348d1`  |
| 3283   | Layout 1             | `1287b22348d1`  |
| 3275   | Layout 1             | `1287b22348d1`  |
| 3267   | Layout 1             | `1287b22348d1`  |
| 3258   | Layout 1             | `1287b22348d1`  |
| 3251   | Layout 1             | `1287b22348d1`  |
| 3242   | Layout 1             | `1287b22348d1`  |
| 3235   | Layout 1             | `1287b22348d1`  |
| 3229   | Layout 1             | `1287b22348d1`  |
| 3212   | Layout 1             | `1287b22348d1`  |
| 3203   | Layout 1             | `1287b22348d1`  |
| 3193   | Layout 1             | `1287b22348d1`  |
| 3186   | Layout 1             | `1287b22348d1`  |
| 3177   | Layout 1             | `1287b22348d1`  |
| 3169   | Layout 1             | `1287b22348d1`  |
| 3158   | Layout 1             | `1287b22348d1`  |
| 3151   | Layout 1             | `1287b22348d1`  |
| 3144   | Layout 1             | `1287b22348d1`  |
| 3133   | Layout 1             | `1287b22348d1`  |
| 3125   | Layout 1             | `1287b22348d1`  |
| 3118   | Layout 1             | `1287b22348d1`  |
| 3111   | Layout 1             | `1287b22348d1`  |
| 3103   | Layout 1             | `1287b22348d1`  |
| 3095   | Layout 1             | `1287b22348d1`  |
| 3086   | Layout 1             | `1287b22348d1`  |
| 3072   | Layout 1             | `1287b22348d1`  |
| 3062   | Layout 1             | `1287b22348d1`  |
| 3052   | Layout 1             | `1287b22348d1`  |
| 3045   | Layout 1             | `1287b22348d1`  |
| 3037   | Layout 1             | `1287b22348d1`  |
| 3030   | Layout 1             | `1287b22348d1`  |
| 3021   | Layout 1             | `1287b22348d1`  |
| 3012   | Layout 1             | `1287b22348d1`  |
| 3002   | Layout 1             | `1287b22348d1`  |
| 2995   | Layout 1             | `1287b22348d1`  |
| 2987   | Layout 1             | `1287b22348d1`  |
| 2978   | Layout 1             | `1287b22348d1`  |
| 2970   | Layout 1             | `1287b22348d1`  |
| 2959   | Layout 1             | `1287b22348d1`  |
| 2951   | Layout 1             | `1287b22348d1`  |
| 2942   | Layout 1             | `1287b22348d1`  |
| 2935   | Layout 1             | `1287b22348d1`  |
| 2932   | Layout 1             | `1287b22348d1`  |
| 2923   | Layout 1             | `1287b22348d1`  |
| 2919   | Layout 1             | `1287b22348d1`  |
| 2907   | Layout 1             | `1287b22348d1`  |
| 2900   | Layout 1             | `1287b22348d1`  |
| 2891   | Layout 1             | `1287b22348d1`  |
| 2882   | Layout 1             | `1287b22348d1`  |
| 2872   | Layout 1             | `1287b22348d1`  |
| 2863   | Layout 1             | `1287b22348d1`  |
| 2855   | Layout 1             | `1287b22348d1`  |
| 2849   | Layout 1             | `1287b22348d1`  |
| 2844   | Layout 1             | `1287b22348d1`  |
| 2834   | Layout 1             | `1287b22348d1`  |
| 2825   | Layout 1             | `1287b22348d1`  |
| 2819   | Layout 1             | `1287b22348d1`  |
| 2811   | Layout 1             | `1287b22348d1`  |
| 2803   | Layout 1             | `1287b22348d1`  |
| 2794   | Layout 1             | `1287b22348d1`  |
| 2783   | Layout 1             | `1287b22348d1`  |
| 2774   | Layout 1             | `1287b22348d1`  |
| 2765   | Layout 1             | `1287b22348d1`  |
| 2756   | Layout 1             | `1287b22348d1`  |
| 2750   | Layout 1             | `1287b22348d1`  |
| 2743   | Layout 1             | `1287b22348d1`  |
| 2736   | Layout 1             | `1287b22348d1`  |
| 2726   | Layout 1             | `1287b22348d1`  |
| 2717   | Layout 1             | `1287b22348d1`  |
| 2709   | Layout 1             | `1287b22348d1`  |
| 2703   | Layout 1             | `1287b22348d1`  |
| 2695   | Layout 1             | `1287b22348d1`  |
| 2684   | Layout 1             | `1287b22348d1`  |
| 2672   | Layout 1             | `1287b22348d1`  |
| 2665   | Layout 1             | `1287b22348d1`  |
| 2657   | Layout 1             | `1287b22348d1`  |
| 2649   | Layout 1             | `1287b22348d1`  |
| 2644   | Layout 1             | `1287b22348d1`  |
| 2637   | Layout 1             | `1287b22348d1`  |
| 2629   | Layout 1             | `1287b22348d1`  |
| 2619   | Layout 1             | `1287b22348d1`  |
| 2612   | Layout 1             | `1287b22348d1`  |
| 2606   | Layout 1             | `1287b22348d1`  |
| 2602   | Layout 1             | `1287b22348d1`  |
| 2601   | Layout 1             | `1287b22348d1`  |
| 2592   | Layout 1             | `1287b22348d1`  |
| 2583   | Layout 1             | `1287b22348d1`  |
| 2575   | Layout 1             | `1287b22348d1`  |
| 2567   | Layout 1             | `1287b22348d1`  |
| 2560   | Layout 1             | `1287b22348d1`  |
| 2553   | Layout 1             | `1287b22348d1`  |
| 2545   | Layout 1             | `1287b22348d1`  |
| 2538   | Layout 1             | `1287b22348d1`  |
| 2529   | Layout 1             | `1287b22348d1`  |
| 2519   | Layout 1             | `1287b22348d1`  |
| 2513   | Layout 1             | `1287b22348d1`  |
| 2510   | Layout 1             | `1287b22348d1`  |
| 2507   | Layout 1             | `1287b22348d1`  |
| 2503   | Layout 1             | `1287b22348d1`  |
| 2498   | Layout 1             | `1287b22348d1`  |
| 2492   | Layout 1             | `1287b22348d1`  |
| 2487   | Layout 1             | `1287b22348d1`  |
| 2480   | Layout 1             | `1287b22348d1`  |
| 2474   | Layout 1             | `1287b22348d1`  |
| 2468   | Layout 1             | `1287b22348d1`  |
| 2460   | Layout 1             | `1287b22348d1`  |
| 2453   | Layout 1             | `1287b22348d1`  |
| 2444   | Layout 1             | `1287b22348d1`  |
| 2438   | Layout 1             | `1287b22348d1`  |
| 2434   | Layout 1             | `1287b22348d1`  |
| 2429   | Layout 1             | `1287b22348d1`  |
| 2421   | Layout 1             | `1287b22348d1`  |
| 2414   | Layout 1             | `1287b22348d1`  |
| 2407   | Layout 1             | `1287b22348d1`  |
| 2401   | Layout 1             | `1287b22348d1`  |
| 2397   | Layout 1             | `1287b22348d1`  |
| 2393   | Layout 1             | `1287b22348d1`  |
| 2384   | Layout 1             | `1287b22348d1`  |
| 2378   | Layout 1             | `1287b22348d1`  |
| 2372   | Layout 1             | `1287b22348d1`  |
| 2358   | Layout 1             | `1287b22348d1`  |
| 2352   | Layout 1             | `1287b22348d1`  |
| 2347   | Layout 1             | `1287b22348d1`  |
| 2343   | Layout 1             | `1287b22348d1`  |
| 2335   | Layout 1             | `1287b22348d1`  |
| 2327   | Layout 1             | `1287b22348d1`  |
| 2324   | Layout 1             | `1287b22348d1`  |
| 2319   | Layout 1             | `1287b22348d1`  |
| 2313   | Layout 1             | `1287b22348d1`  |
| 2308   | Layout 1             | `1287b22348d1`  |
| 2302   | Layout 1             | `1287b22348d1`  |
| 2295   | Layout 1             | `1287b22348d1`  |
| 2290   | Layout 1             | `1287b22348d1`  |
| 2284   | Layout 1             | `1287b22348d1`  |
| 2276   | Layout 1             | `1287b22348d1`  |
| 2269   | Layout 1             | `1287b22348d1`  |
| 2259   | Layout 1             | `1287b22348d1`  |
| 2250   | Layout 1             | `1287b22348d1`  |
| 2243   | Layout 1             | `1287b22348d1`  |
| 2235   | Layout 1             | `1287b22348d1`  |
| 2229   | Layout 1             | `1287b22348d1`  |
| 2224   | Layout 1             | `1287b22348d1`  |
| 2218   | Layout 1             | `1287b22348d1`  |
| 2215   | Layout 1             | `1287b22348d1`  |
| 2207   | Layout 1             | `1287b22348d1`  |
| 2203   | Layout 1             | `1287b22348d1`  |
| 2196   | Layout 1             | `1287b22348d1`  |
| 2192   | Layout 1             | `1287b22348d1`  |
| 2189   | Layout 1             | `1287b22348d1`  |
| 2183   | Layout 1             | `1287b22348d1`  |
| 2179   | Layout 1             | `1287b22348d1`  |
| 2171   | Layout 1             | `1287b22348d1`  |
| 2163   | Layout 1             | `1287b22348d1`  |
| 2156   | Layout 1             | `1287b22348d1`  |
| 2151   | Layout 1             | `1287b22348d1`  |
| 2147   | Layout 1             | `1287b22348d1`  |
| 2142   | Layout 1             | `1287b22348d1`  |
| 2138   | Layout 1             | `1287b22348d1`  |
| 2134   | Layout 1             | `1287b22348d1`  |
| 2130   | Layout 1             | `1287b22348d1`  |
| 2122   | Layout 1             | `1287b22348d1`  |
| 2107   | Layout 1             | `1287b22348d1`  |
| 2098   | Layout 1             | `1287b22348d1`  |
| 2089   | Layout 1             | `1287b22348d1`  |
| 2081   | Layout 1             | `1287b22348d1`  |
| 2073   | Layout 1             | `1287b22348d1`  |
| 2067   | Layout 1             | `1287b22348d1`  |
| 2063   | Layout 1             | `1287b22348d1`  |
| 2059   | Layout 1             | `1287b22348d1`  |
| 2052   | Layout 1             | `1287b22348d1`  |
| 2044   | Layout 1             | `1287b22348d1`  |
| 2039   | Layout 1             | `1287b22348d1`  |
| 2032   | Layout 1             | `1287b22348d1`  |
| 2025   | Layout 1             | `1287b22348d1`  |
| 2011   | Layout 1             | `1287b22348d1`  |
| 2005   | Layout 1             | `1287b22348d1`  |
| 2000   | Layout 1             | `1287b22348d1`  |
| 1996   | Layout 1             | `1287b22348d1`  |
| 1991   | Layout 1             | `1287b22348d1`  |
| 1985   | Layout 1             | `1287b22348d1`  |
| 1980   | Layout 1             | `1287b22348d1`  |
| 1969   | Layout 1             | `1287b22348d1`  |
| 1964   | Layout 1             | `1287b22348d1`  |
| 1958   | Layout 1             | `1287b22348d1`  |
| 1950   | Layout 1             | `1287b22348d1`  |
| 1945   | Layout 1             | `1287b22348d1`  |
| 1937   | Layout 1             | `1287b22348d1`  |
| 1933   | Layout 1             | `1287b22348d1`  |
| 1927   | Layout 1             | `1287b22348d1`  |
| 1921   | Layout 1             | `1287b22348d1`  |
| 1914   | Layout 1             | `1287b22348d1`  |
| 1908   | Layout 1             | `1287b22348d1`  |
| 1897   | Layout 1             | `1287b22348d1`  |
| 1892   | Layout 1             | `1287b22348d1`  |
| 1886   | Layout 1             | `1287b22348d1`  |
| 1881   | Layout 1             | `1287b22348d1`  |
| 1871   | Layout 1             | `1287b22348d1`  |
| 1866   | Layout 1             | `1287b22348d1`  |
| 1862   | Layout 1             | `1287b22348d1`  |
| 1854   | Layout 1             | `1287b22348d1`  |
| 1846   | Layout 1             | `1287b22348d1`  |
| 1838   | Layout 1             | `1287b22348d1`  |
| 1832   | Layout 1             | `1287b22348d1`  |
| 1826   | Layout 1             | `1287b22348d1`  |
| 1822   | Layout 1             | `1287b22348d1`  |
| 1818   | Layout 1             | `1287b22348d1`  |
| 1804   | Layout 1             | `1287b22348d1`  |
| 1794   | Layout 1             | `1287b22348d1`  |
| 1790   | Layout 1             | `1287b22348d1`  |
| 1784   | Layout 1             | `1287b22348d1`  |
| 1774   | Layout 1             | `1287b22348d1`  |
| 1771   | Layout 1             | `1287b22348d1`  |
| 1762   | Layout 1             | `1287b22348d1`  |
| 1759   | Layout 1             | `1287b22348d1`  |
| 1754   | Layout 1             | `1287b22348d1`  |
| 1749   | Layout 1             | `1287b22348d1`  |
| 1743   | Layout 1             | `1287b22348d1`  |
| 1737   | Layout 1             | `1287b22348d1`  |
| 1731   | Layout 1             | `1287b22348d1`  |
| 1725   | Layout 1             | `1287b22348d1`  |
| 1717   | Layout 1             | `1287b22348d1`  |
| 1710   | Layout 1             | `1287b22348d1`  |
| 1704   | Layout 1             | `1287b22348d1`  |
| 1698   | Layout 1             | `1287b22348d1`  |
| 1690   | Layout 1             | `1287b22348d1`  |
| 1685   | Layout 1             | `1287b22348d1`  |
| 1680   | Layout 1             | `1287b22348d1`  |
| 1674   | Layout 1             | `1287b22348d1`  |
| 1668   | Layout 1             | `1287b22348d1`  |
| 1659   | Layout 1             | `1287b22348d1`  |
| 1649   | Layout 1             | `1287b22348d1`  |
| 1642   | Layout 1             | `1287b22348d1`  |
| 1636   | Layout 1             | `1287b22348d1`  |
| 1628   | Layout 1             | `1287b22348d1`  |
| 1622   | Layout 1             | `1287b22348d1`  |
| 1614   | Layout 1             | `1287b22348d1`  |
| 1608   | Layout 1             | `1287b22348d1`  |
| 1602   | Layout 1             | `1287b22348d1`  |
| 1598   | Layout 1             | `1287b22348d1`  |
| 1594   | Layout 1             | `1287b22348d1`  |
| 1590   | Layout 1             | `1287b22348d1`  |
| 1587   | Layout 1             | `1287b22348d1`  |
| 1584   | Layout 1             | `1287b22348d1`  |
| 1579   | Layout 1             | `1287b22348d1`  |
| 1572   | Layout 1             | `1287b22348d1`  |
| 1565   | Layout 1             | `1287b22348d1`  |
| 1559   | Layout 1             | `1287b22348d1`  |
| 1554   | Layout 1             | `1287b22348d1`  |
| 1547   | Layout 1             | `1287b22348d1`  |
| 1537   | Layout 1             | `1287b22348d1`  |
| 1529   | Layout 1             | `1287b22348d1`  |
| 1524   | Layout 1             | `1287b22348d1`  |
| 1519   | Layout 1             | `1287b22348d1`  |
| 1509   | Layout 1             | `1287b22348d1`  |
| 1506   | Layout 1             | `1287b22348d1`  |
| 1504   | Layout 1             | `1287b22348d1`  |
| 1500   | Layout 1             | `1287b22348d1`  |
| 1493   | Layout 1             | `1287b22348d1`  |
| 1489   | Layout 1             | `1287b22348d1`  |
| 1485   | Layout 1             | `1287b22348d1`  |
| 1481   | Layout 1             | `1287b22348d1`  |
| 1474   | Layout 1             | `1287b22348d1`  |
| 1466   | Layout 1             | `1287b22348d1`  |
| 1462   | Layout 1             | `1287b22348d1`  |
| 1459   | Layout 1             | `1287b22348d1`  |
| 1453   | Layout 1             | `1287b22348d1`  |
| 1450   | Layout 1             | `1287b22348d1`  |
| 1445   | Layout 1             | `1287b22348d1`  |
| 1439   | Layout 1             | `1287b22348d1`  |
| 1433   | Layout 1             | `1287b22348d1`  |
| 1430   | Layout 1             | `1287b22348d1`  |
| 1426   | Layout 1             | `1287b22348d1`  |
| 1421   | Layout 1             | `1287b22348d1`  |
| 1417   | Layout 1             | `1287b22348d1`  |
| 1416   | Layout 1             | `1287b22348d1`  |
| 1409   | Layout 1             | `1287b22348d1`  |
| 1405   | Layout 1             | `1287b22348d1`  |
| 1401   | Layout 1             | `1287b22348d1`  |
| 1396   | Layout 1             | `1287b22348d1`  |
| 1391   | Layout 1             | `1287b22348d1`  |
| 1390   | Layout 1             | `1287b22348d1`  |
| 1386   | Layout 1             | `1287b22348d1`  |
| 1381   | Layout 1             | `1287b22348d1`  |
| 1379   | Layout 1             | `1287b22348d1`  |
| 1372   | Layout 1             | `1287b22348d1`  |
| 1366   | Layout 1             | `1287b22348d1`  |
| 1364   | Layout 1             | `1287b22348d1`  |
| 1363   | Layout 1             | `1287b22348d1`  |
| 1360   | Layout 1             | `1287b22348d1`  |
| 1358   | Layout 1             | `1287b22348d1`  |
| 1355   | Layout 1             | `1287b22348d1`  |
| 1351   | Layout 1             | `1287b22348d1`  |
| 1348   | Layout 1             | `1287b22348d1`  |
| 1346   | Layout 1             | `1287b22348d1`  |
| 1341   | No documented layout | `1287b22348d1`  |
| 1340   | No documented layout | `1287b22348d1`  |
| 1338   | No documented layout | `1287b22348d1`  |
| 1335   | No documented layout | `1287b22348d1`  |
| 1333   | No documented layout | `1287b22348d1`  |
| 1329   | No documented layout | `1287b22348d1`  |
| 1327   | No documented layout | `1287b22348d1`  |
| 1324   | No documented layout | `1287b22348d1`  |
| 1321   | No documented layout | `1287b22348d1`  |
| 1319   | No documented layout | `1287b22348d1`  |
| 1318   | No documented layout | `1287b22348d1`  |
| 1316   | No documented layout | `1287b22348d1`  |
| 1313   | No documented layout | `1287b22348d1`  |
| 1311   | No documented layout | `1287b22348d1`  |
| 1309   | No documented layout | `1287b22348d1`  |
| 1304   | No documented layout | `1287b22348d1`  |
| 1292   | No documented layout | `1287b22348d1`  |
| 1286   | No documented layout | `1287b22348d1`  |
| 1280   | No file              | `1287b22348d1`  |
| 1276   | No file              | `1287b22348d1`  |
| 1267   | No documented layout | `1287b22348d1`  |
| 1261   | No documented layout | `1287b22348d1`  |
| 1256   | No file              | `1287b22348d1`  |
| 1250   | No file              | `1287b22348d1`  |
| 1246   | No file              | `1287b22348d1`  |
| 1239   | No file              | `1287b22348d1`  |
| 1230   | No file              | `1287b22348d1`  |
| 1226   | No file              | `1287b22348d1`  |
| 1220   | No file              | `1287b22348d1`  |
| 1217   | No file              | `1287b22348d1`  |
| 1211   | No file              | `1287b22348d1`  |
| 1210   | No file              | `1287b22348d1`  |
| 1208   | No file              | `1287b22348d1`  |
| 1203   | No file              | `1287b22348d1`  |
| 1197   | No file              | `1287b22348d1`  |
| 1194   | No file              | `1287b22348d1`  |
| 1192   | No file              | `1287b22348d1`  |
| 1187   | No file              | `1287b22348d1`  |
| 1183   | No file              | `1287b22348d1`  |
| 1177   | No file              | `1287b22348d1`  |
| 1173   | No file              | `1287b22348d1`  |
| 1167   | No file              | `1287b22348d1`  |
| 1164   | No file              | `1287b22348d1`  |
| 1156   | No file              | `1287b22348d1`  |
| 1149   | No file              | `1287b22348d1`  |
| 1144   | No file              | `1287b22348d1`  |
| 1137   | No file              | `1287b22348d1`  |
| 1132   | No file              | `1287b22348d1`  |
| 1127   | No file              | `1287b22348d1`  |
| 1122   | No file              | `1287b22348d1`  |
| 1118   | No file              | `1287b22348d1`  |
| 1114   | No file              | `1287b22348d1`  |
| 1109   | No file              | `1287b22348d1`  |
| 1102   | No file              | `1287b22348d1`  |
| 1096   | No file              | `1287b22348d1`  |
| 1088   | No file              | `1287b22348d1`  |
| 1081   | No file              | `1287b22348d1`  |
| 1076   | No file              | `1287b22348d1`  |
| 1069   | No file              | `1287b22348d1`  |
| 1064   | No file              | `1287b22348d1`  |
| 1058   | No file              | `1287b22348d1`  |
| 1051   | No file              | `1287b22348d1`  |
| 1044   | No file              | `1287b22348d1`  |
| 1036   | No file              | `1287b22348d1`  |
| 1026   | No file              | `1287b22348d1`  |
| 1016   | No file              | `1287b22348d1`  |
| 1009   | No file              | `1287b22348d1`  |
| 1005   | No file              | `1287b22348d1`  |
| 1000   | No file              | `1287b22348d1`  |
| 998    | No file              | `1287b22348d1`  |
| 990    | No file              | `1287b22348d1`  |
| 979    | No file              | `1287b22348d1`  |
| 972    | No file              | `1287b22348d1`  |
| 963    | No file              | `1287b22348d1`  |
| 955    | No file              | `1287b22348d1`  |
| 946    | No file              | `1287b22348d1`  |
| 938    | No file              | `1287b22348d1`  |
| 927    | No file              | `1287b22348d1`  |
| 911    | No file              | `1287b22348d1`  |
| 904    | No file              | `1287b22348d1`  |
| 899    | No file              | `1287b22348d1`  |
| 894    | No file              | `1287b22348d1`  |
| 885    | No file              | `1287b22348d1`  |
| 879    | No file              | `1287b22348d1`  |
| 872    | No file              | `1287b22348d1`  |
| 864    | No file              | `1287b22348d1`  |
| 855    | No file              | `1287b22348d1`  |
| 853    | No file              | `1287b22348d1`  |
| 845    | No file              | `1287b22348d1`  |
| 837    | No file              | `1287b22348d1`  |
| 829    | No file              | `1287b22348d1`  |
| 822    | No file              | `1287b22348d1`  |
| 814    | No file              | `1287b22348d1`  |
| 805    | No file              | `1287b22348d1`  |
| 794    | No file              | `1287b22348d1`  |
| 787    | No file              | `1287b22348d1`  |
| 780    | No file              | `1287b22348d1`  |
| 771    | No file              | `1287b22348d1`  |
| 760    | No file              | `1287b22348d1`  |
| 748    | No file              | `1287b22348d1`  |
| 741    | No file              | `1287b22348d1`  |
| 736    | No file              | `1287b22348d1`  |
| 731    | No file              | `1287b22348d1`  |
| 723    | No file              | `1287b22348d1`  |
| 711    | No file              | `1287b22348d1`  |
| 707    | No file              | `1287b22348d1`  |
| 697    | No file              | `1287b22348d1`  |
| 689    | No file              | `1287b22348d1`  |
| 683    | No file              | `1287b22348d1`  |
| 678    | No file              | `1287b22348d1`  |
| 670    | No file              | `1287b22348d1`  |
| 661    | No file              | `1287b22348d1`  |
| 656    | No file              | `1287b22348d1`  |
| 652    | No file              | `1287b22348d1`  |
| 643    | No file              | `1287b22348d1`  |
| 637    | No file              | `1287b22348d1`  |
| 630    | No file              | `1287b22348d1`  |
| 627    | No file              | `1287b22348d1`  |
| 621    | No file              | `1287b22348d1`  |
| 617    | No file              | `1287b22348d1`  |
| 615    | No file              | `1287b22348d1`  |
| 606    | No file              | `1287b22348d1`  |
| 599    | No file              | `1287b22348d1`  |
| 592    | No file              | `1287b22348d1`  |
| 586    | No file              | `1287b22348d1`  |
| 577    | No file              | `1287b22348d1`  |
| 569    | No file              | `1287b22348d1`  |
| 561    | No file              | `1287b22348d1`  |
| 554    | No file              | `1287b22348d1`  |
| 542    | No file              | `1287b22348d1`  |
| 532    | No file              | `1287b22348d1`  |
| 531    | No file              | `1287b22348d1`  |
| 526    | No file              | `1287b22348d1`  |
| 521    | No file              | `1287b22348d1`  |
| 517    | No file              | `1287b22348d1`  |
| 510    | No file              | `1287b22348d1`  |
| 508    | No file              | `1287b22348d1`  |
| 504    | No file              | `1287b22348d1`  |
| 497    | No file              | `1287b22348d1`  |
| 491    | No file              | `1287b22348d1`  |
| 485    | No file              | `1287b22348d1`  |
| 478    | No file              | `1287b22348d1`  |
| 472    | No file              | `1287b22348d1`  |
| 466    | No file              | `1287b22348d1`  |
| 457    | No file              | `1287b22348d1`  |
| 452    | No file              | `1287b22348d1`  |
| 449    | No file              | `1287b22348d1`  |
| 435    | No file              | `1287b22348d1`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                  |
| ---------------------------------- | -------- | ----------------------------------------------------- |
| `fairyequipskillaquireoffset.dbss` | Required | `acquire_type_id → (data_offset, data_size)` index    |
| `fairyequipskill.bss`              | Optional | Resolves a weight's `equip_skill_id` to a skill name  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                           |
| ------- | ------------- | ------- | ------------------------------- |
| `+0x00` | u32           | count   | Number of records; observed `4` |
| `+0x04` | Record[count] | records | See Record                      |

### Record (176 bytes)

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u32     | packed_key | `(acquire_type_id << 16) \| acquire_type_id`           |
| `+0x04` | u32[43] | weights    | Roll weight per `equip_skill_id`, in parts-per-million |

`4 + 43 × 4 = 176` bytes exactly. `weights[i]` is the chance of rolling the skill whose `equip_skill_id` is `i`; index `0` is the first weight, **not** a reserved field.

The first 2 bytes of each record are the file key prefix. The offset companion points to `record_start + 2`, so use `record_start = data_offset - 2` to read the full u32-aligned record.

### `fairyequipskillaquireoffset.dbss`

| Offset  | Type                 | Field | Notes                                               |
| ------- | -------------------- | ----- | --------------------------------------------------- |
| `+0x00` | u32                  | count | Must equal `fairyequipskillaquire.dbss` count (`4`) |
| `+0x04` | Offset Record[count] | rows  | See Offset Record                                   |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | key         | `acquire_type_id`; observed `504`, `503`, `502`, `501`       |
| `+0x02` | u32  | data_offset | Absolute byte offset in the main file past the 2-byte prefix |
| `+0x06` | u16  | data_size   | Always `174` (`176 - 2-byte key prefix`)                     |
| `+0x08` | u16  | unknown_08  | Always `0`                                                   |

Rows are ordered descending by key and ascending by `data_offset`.

## Acquire Type IDs, Fairy Grades

The four keys are the four fairy grades, ascending:

| acquire_type_id | Fairy grade | Rollable skills | Max skill rank |
| --------------- | ----------- | --------------- | -------------- |
| `501`           | Faint       | 6               | I              |
| `502`           | Glimmering  | 13              | III            |
| `503`           | Brilliant   | 18              | IV             |
| `504`           | Radiant     | 30              | V              |

Every record's weights sum to exactly `1,000,000`, so each column below is a complete probability distribution.

## Roll Chances

`-` means the grade cannot roll that skill.

| equip_skill_id | Skill                  | Faint  | Glimmering | Brilliant | Radiant |
| -------------- | ---------------------- | ------ | ---------- | --------- | ------- |
| 0              | Tingling Breath I      | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 1              | Tingling Breath II     | -      | 7.0%       | 5.0%      | 2.0%    |
| 2              | Tingling Breath III    | -      | -          | 5.0%      | 3.0%    |
| 3              | Tingling Breath IV     | -      | -          | -         | 3.0%    |
| 4              | Tingling Breath V      | -      | -          | -         | 3.0%    |
| 5              | Feathery Steps I       | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 6              | Feathery Steps II      | -      | 7.0%       | 5.0%      | 2.0%    |
| 7              | Feathery Steps III     | -      | -          | 5.0%      | 3.0%    |
| 8              | Feathery Steps IV      | -      | -          | -         | 4.0%    |
| 9              | Feathery Steps V       | -      | -          | -         | 5.0%    |
| 10             | Fairy's Tear I         | 15.0%  | 7.0%       | 5.0%      | 2.0%    |
| 11             | Fairy's Tear II        | -      | 7.0%       | 5.0%      | 3.0%    |
| 12             | Fairy's Tear III       | -      | -          | 5.0%      | 4.0%    |
| 13             | Fairy's Tear IV        | -      | -          | -         | 5.0%    |
| 14             | Inexhaustible Well I   | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 15             | Inexhaustible Well II  | -      | 7.0%       | 5.0%      | 2.0%    |
| 16             | Inexhaustible Well III | -      | 7.0%       | 5.0%      | 3.0%    |
| 17             | Inexhaustible Well IV  | -      | -          | 5.0%      | 3.0%    |
| 18             | Inexhaustible Well V   | -      | -          | -         | 4.0%    |
| 19             | Morning Star           | 25.0%  | 15.0%      | 10.0%     | 3.0%    |
| 24             | Miraculous Cheer I     | 15.0%  | 8.0%       | 5.0%      | 3.0%    |
| 25             | Miraculous Cheer II    | -      | 7.0%       | 5.0%      | 4.0%    |
| 26             | Miraculous Cheer III   | -      | 7.0%       | 5.0%      | 5.0%    |
| 27             | Miraculous Cheer IV    | -      | -          | 10.0%     | 6.0%    |
| 28             | Miraculous Cheer V     | -      | -          | -         | 10.0%   |
| 30             | Continuous Care I      | -      | -          | -         | 1.0%    |
| 31             | Continuous Care II     | -      | -          | -         | 2.0%    |
| 32             | Continuous Care III    | -      | -          | -         | 3.0%    |
| 33             | Continuous Care IV     | -      | -          | -         | 4.0%    |
| 34             | Continuous Care V      | -      | -          | -         | 5.0%    |
| **Total**      |                        | 100.0% | 100.0%     | 100.0%    | 100.0%  |

### Never-rolled skills

Five catalog entries carry a weight of `0` in every grade and are therefore unreachable through a skill change:

| equip_skill_id | Skill                       | Why                                     |
| -------------- | --------------------------- | --------------------------------------- |
| 20             | Miraculous Cheer 10 Seconds | Legacy naming, superseded by `I`–`V`    |
| 21             | Miraculous Cheer 9 Seconds  | Legacy naming                           |
| 22             | Miraculous Cheer 8 Seconds  | Legacy naming                           |
| 23             | Miraculous Cheer 7 Seconds  | Legacy naming                           |
| 29             | Gift                        | Every fairy starts with it; never rolled |

## Lookup Recipe

```python
def roll_chance(record, equip_skill_id):
    weight = record["weights"][equip_skill_id]
    return weight / record["total_weight"]  # total is 1,000,000 for fairies
```

## Notes

- Weights are probabilities, not costs. Earlier revisions of this document described the record as an acquisition cost table with `cost_a`/`cost_b`/`cost_c` triples and a `reserved` field; that reading was wrong. The values are parts-per-million and the "reserved" u32 is simply `weights[0]`.
- The record is a flat 43-element array, not 14 sub-entries of 3 values. The apparent triples were an artifact of grouping a dense array into 12-byte rows.
- Three independent checks confirm the reading: every grade sums to exactly `1,000,000`; the non-zero index set per grade matches the published per-tier skill availability exactly; and the highest rank reachable per grade (I / III / IV / V) matches the published rank caps.
- 43 weight slots cover `equip_skill_id` `0`–`42`, while the fairy catalog only defines `0`–`34`. Slots `35`–`42` are zero in every record, spare capacity shared with the pet table, which uses the same 176-byte record.
- Only Radiant can roll rank IV and V skills, which the weight table encodes directly rather than through a separate cap field.
- Morning Star is weighted far above any other skill at low grades (25% for Faint) and drops to 3% at Radiant.
- Observed: 4 records and 67 non-zero weights (6 + 13 + 18 + 30) in the pre-2026-09-27 fixture and in the 2026-09-27 client; both files are byte-identical between the two.

## Open Questions

### Sub-entry semantic mapping

Resolved. The former "14 sub-entries with `cost_a`/`cost_b`/`cost_c`" structure does not exist; the record is a flat weight array indexed by `equip_skill_id`. This entry is retained so the disproven reading is not re-derived.

### Spare weight slots

Slots `35`–`42` are always zero for fairies. Whether they are reserved for future fairy skills or exist only because the record size is shared with `petequipskillaquire.dbss` is unconfirmed.
