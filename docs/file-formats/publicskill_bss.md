# `publicskill.bss` Format

## Purpose

The skill key of every item and event skill: one u32 `skill_key` per skill
number at level `1`, for every `skill.dbss` skill whose `kind` is `0`
(`eItemSkillType`) and whose `skill_owner_type` is `0`. The active and
passive skills are in [`privateskill.bss`](privateskill_bss.md), which has
its own layout.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | -------------- | --------- |
| 1      | 1194 and later | 3483    | `publicskill.bss` | 57,644 | 1 String Table | 4         |

| Layout | File              | Known             | Unknown    |
| ------ | ----------------- | ----------------- | ---------- |
| 1      | `publicskill.bss` | 57,640 B (100.0%) | 4 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cb6841b27f56`  |
| 3482   | Layout 1 | `cb6841b27f56`  |
| 3474   | Layout 1 | `cb6841b27f56`  |
| 3473   | Layout 1 | `cb6841b27f56`  |
| 3464   | Layout 1 | `cb6841b27f56`  |
| 3458   | Layout 1 | `cb6841b27f56`  |
| 3454   | Layout 1 | `cb6841b27f56`  |
| 3444   | Layout 1 | `cb6841b27f56`  |
| 3435   | Layout 1 | `cb6841b27f56`  |
| 3426   | Layout 1 | `cb6841b27f56`  |
| 3418   | Layout 1 | `cb6841b27f56`  |
| 3412   | Layout 1 | `cb6841b27f56`  |
| 3402   | Layout 1 | `cb6841b27f56`  |
| 3396   | Layout 1 | `cb6841b27f56`  |
| 3387   | Layout 1 | `cb6841b27f56`  |
| 3381   | Layout 1 | `cb6841b27f56`  |
| 3373   | Layout 1 | `cb6841b27f56`  |
| 3364   | Layout 1 | `cb6841b27f56`  |
| 3356   | Layout 1 | `cb6841b27f56`  |
| 3349   | Layout 1 | `cb6841b27f56`  |
| 3342   | Layout 1 | `cb6841b27f56`  |
| 3335   | Layout 1 | `cb6841b27f56`  |
| 3326   | Layout 1 | `cb6841b27f56`  |
| 3321   | Layout 1 | `cb6841b27f56`  |
| 3314   | Layout 1 | `cb6841b27f56`  |
| 3303   | Layout 1 | `cb6841b27f56`  |
| 3302   | Layout 1 | `cb6841b27f56`  |
| 3293   | Layout 1 | `cb6841b27f56`  |
| 3283   | Layout 1 | `cb6841b27f56`  |
| 3275   | Layout 1 | `cb6841b27f56`  |
| 3267   | Layout 1 | `cb6841b27f56`  |
| 3258   | Layout 1 | `cb6841b27f56`  |
| 3251   | Layout 1 | `cb6841b27f56`  |
| 3242   | Layout 1 | `cb6841b27f56`  |
| 3235   | Layout 1 | `cb6841b27f56`  |
| 3229   | Layout 1 | `cb6841b27f56`  |
| 3212   | Layout 1 | `cb6841b27f56`  |
| 3203   | Layout 1 | `cb6841b27f56`  |
| 3193   | Layout 1 | `cb6841b27f56`  |
| 3186   | Layout 1 | `cb6841b27f56`  |
| 3177   | Layout 1 | `cb6841b27f56`  |
| 3169   | Layout 1 | `cb6841b27f56`  |
| 3158   | Layout 1 | `cb6841b27f56`  |
| 3151   | Layout 1 | `cb6841b27f56`  |
| 3144   | Layout 1 | `cb6841b27f56`  |
| 3133   | Layout 1 | `cb6841b27f56`  |
| 3125   | Layout 1 | `cb6841b27f56`  |
| 3118   | Layout 1 | `cb6841b27f56`  |
| 3111   | Layout 1 | `cb6841b27f56`  |
| 3103   | Layout 1 | `cb6841b27f56`  |
| 3095   | Layout 1 | `cb6841b27f56`  |
| 3086   | Layout 1 | `cb6841b27f56`  |
| 3072   | Layout 1 | `cb6841b27f56`  |
| 3062   | Layout 1 | `cb6841b27f56`  |
| 3052   | Layout 1 | `cb6841b27f56`  |
| 3045   | Layout 1 | `cb6841b27f56`  |
| 3037   | Layout 1 | `cb6841b27f56`  |
| 3030   | Layout 1 | `cb6841b27f56`  |
| 3021   | Layout 1 | `cb6841b27f56`  |
| 3012   | Layout 1 | `cb6841b27f56`  |
| 3002   | Layout 1 | `cb6841b27f56`  |
| 2995   | Layout 1 | `cb6841b27f56`  |
| 2987   | Layout 1 | `cb6841b27f56`  |
| 2978   | Layout 1 | `cb6841b27f56`  |
| 2970   | Layout 1 | `cb6841b27f56`  |
| 2959   | Layout 1 | `cb6841b27f56`  |
| 2951   | Layout 1 | `cb6841b27f56`  |
| 2942   | Layout 1 | `cb6841b27f56`  |
| 2935   | Layout 1 | `cb6841b27f56`  |
| 2932   | Layout 1 | `cb6841b27f56`  |
| 2923   | Layout 1 | `cb6841b27f56`  |
| 2919   | Layout 1 | `cb6841b27f56`  |
| 2907   | Layout 1 | `cb6841b27f56`  |
| 2900   | Layout 1 | `cb6841b27f56`  |
| 2891   | Layout 1 | `cb6841b27f56`  |
| 2882   | Layout 1 | `cb6841b27f56`  |
| 2872   | Layout 1 | `cb6841b27f56`  |
| 2863   | Layout 1 | `cb6841b27f56`  |
| 2855   | Layout 1 | `cb6841b27f56`  |
| 2849   | Layout 1 | `cb6841b27f56`  |
| 2844   | Layout 1 | `cb6841b27f56`  |
| 2834   | Layout 1 | `cb6841b27f56`  |
| 2825   | Layout 1 | `cb6841b27f56`  |
| 2819   | Layout 1 | `cb6841b27f56`  |
| 2811   | Layout 1 | `cb6841b27f56`  |
| 2803   | Layout 1 | `cb6841b27f56`  |
| 2794   | Layout 1 | `cb6841b27f56`  |
| 2783   | Layout 1 | `cb6841b27f56`  |
| 2774   | Layout 1 | `cb6841b27f56`  |
| 2765   | Layout 1 | `cb6841b27f56`  |
| 2756   | Layout 1 | `cb6841b27f56`  |
| 2750   | Layout 1 | `cb6841b27f56`  |
| 2743   | Layout 1 | `cb6841b27f56`  |
| 2736   | Layout 1 | `cb6841b27f56`  |
| 2726   | Layout 1 | `cb6841b27f56`  |
| 2717   | Layout 1 | `cb6841b27f56`  |
| 2709   | Layout 1 | `cb6841b27f56`  |
| 2703   | Layout 1 | `cb6841b27f56`  |
| 2695   | Layout 1 | `cb6841b27f56`  |
| 2684   | Layout 1 | `cb6841b27f56`  |
| 2672   | Layout 1 | `cb6841b27f56`  |
| 2665   | Layout 1 | `cb6841b27f56`  |
| 2657   | Layout 1 | `cb6841b27f56`  |
| 2649   | Layout 1 | `cb6841b27f56`  |
| 2644   | Layout 1 | `cb6841b27f56`  |
| 2637   | Layout 1 | `cb6841b27f56`  |
| 2629   | Layout 1 | `cb6841b27f56`  |
| 2619   | Layout 1 | `cb6841b27f56`  |
| 2612   | Layout 1 | `cb6841b27f56`  |
| 2606   | Layout 1 | `cb6841b27f56`  |
| 2602   | Layout 1 | `cb6841b27f56`  |
| 2601   | Layout 1 | `cb6841b27f56`  |
| 2592   | Layout 1 | `cb6841b27f56`  |
| 2583   | Layout 1 | `cb6841b27f56`  |
| 2575   | Layout 1 | `cb6841b27f56`  |
| 2567   | Layout 1 | `cb6841b27f56`  |
| 2560   | Layout 1 | `cb6841b27f56`  |
| 2553   | Layout 1 | `cb6841b27f56`  |
| 2545   | Layout 1 | `cb6841b27f56`  |
| 2538   | Layout 1 | `cb6841b27f56`  |
| 2529   | Layout 1 | `cb6841b27f56`  |
| 2519   | Layout 1 | `cb6841b27f56`  |
| 2513   | Layout 1 | `cb6841b27f56`  |
| 2510   | Layout 1 | `cb6841b27f56`  |
| 2507   | Layout 1 | `cb6841b27f56`  |
| 2503   | Layout 1 | `cb6841b27f56`  |
| 2498   | Layout 1 | `cb6841b27f56`  |
| 2492   | Layout 1 | `cb6841b27f56`  |
| 2487   | Layout 1 | `cb6841b27f56`  |
| 2480   | Layout 1 | `cb6841b27f56`  |
| 2474   | Layout 1 | `cb6841b27f56`  |
| 2468   | Layout 1 | `cb6841b27f56`  |
| 2460   | Layout 1 | `cb6841b27f56`  |
| 2453   | Layout 1 | `cb6841b27f56`  |
| 2444   | Layout 1 | `cb6841b27f56`  |
| 2438   | Layout 1 | `cb6841b27f56`  |
| 2434   | Layout 1 | `cb6841b27f56`  |
| 2429   | Layout 1 | `cb6841b27f56`  |
| 2421   | Layout 1 | `cb6841b27f56`  |
| 2414   | Layout 1 | `cb6841b27f56`  |
| 2407   | Layout 1 | `cb6841b27f56`  |
| 2401   | Layout 1 | `cb6841b27f56`  |
| 2397   | Layout 1 | `cb6841b27f56`  |
| 2393   | Layout 1 | `cb6841b27f56`  |
| 2384   | Layout 1 | `cb6841b27f56`  |
| 2378   | Layout 1 | `cb6841b27f56`  |
| 2372   | Layout 1 | `cb6841b27f56`  |
| 2358   | Layout 1 | `cb6841b27f56`  |
| 2352   | Layout 1 | `cb6841b27f56`  |
| 2347   | Layout 1 | `cb6841b27f56`  |
| 2343   | Layout 1 | `cb6841b27f56`  |
| 2335   | Layout 1 | `cb6841b27f56`  |
| 2327   | Layout 1 | `cb6841b27f56`  |
| 2324   | Layout 1 | `cb6841b27f56`  |
| 2319   | Layout 1 | `cb6841b27f56`  |
| 2313   | Layout 1 | `cb6841b27f56`  |
| 2308   | Layout 1 | `cb6841b27f56`  |
| 2302   | Layout 1 | `cb6841b27f56`  |
| 2295   | Layout 1 | `cb6841b27f56`  |
| 2290   | Layout 1 | `cb6841b27f56`  |
| 2284   | Layout 1 | `cb6841b27f56`  |
| 2276   | Layout 1 | `cb6841b27f56`  |
| 2269   | Layout 1 | `cb6841b27f56`  |
| 2259   | Layout 1 | `cb6841b27f56`  |
| 2250   | Layout 1 | `cb6841b27f56`  |
| 2243   | Layout 1 | `cb6841b27f56`  |
| 2235   | Layout 1 | `cb6841b27f56`  |
| 2229   | Layout 1 | `cb6841b27f56`  |
| 2224   | Layout 1 | `cb6841b27f56`  |
| 2218   | Layout 1 | `cb6841b27f56`  |
| 2215   | Layout 1 | `cb6841b27f56`  |
| 2207   | Layout 1 | `cb6841b27f56`  |
| 2203   | Layout 1 | `cb6841b27f56`  |
| 2196   | Layout 1 | `cb6841b27f56`  |
| 2192   | Layout 1 | `cb6841b27f56`  |
| 2189   | Layout 1 | `cb6841b27f56`  |
| 2183   | Layout 1 | `cb6841b27f56`  |
| 2179   | Layout 1 | `cb6841b27f56`  |
| 2171   | Layout 1 | `cb6841b27f56`  |
| 2163   | Layout 1 | `cb6841b27f56`  |
| 2156   | Layout 1 | `cb6841b27f56`  |
| 2151   | Layout 1 | `cb6841b27f56`  |
| 2147   | Layout 1 | `cb6841b27f56`  |
| 2142   | Layout 1 | `cb6841b27f56`  |
| 2138   | Layout 1 | `cb6841b27f56`  |
| 2134   | Layout 1 | `cb6841b27f56`  |
| 2130   | Layout 1 | `cb6841b27f56`  |
| 2122   | Layout 1 | `cb6841b27f56`  |
| 2107   | Layout 1 | `cb6841b27f56`  |
| 2098   | Layout 1 | `cb6841b27f56`  |
| 2089   | Layout 1 | `cb6841b27f56`  |
| 2081   | Layout 1 | `cb6841b27f56`  |
| 2073   | Layout 1 | `cb6841b27f56`  |
| 2067   | Layout 1 | `cb6841b27f56`  |
| 2063   | Layout 1 | `cb6841b27f56`  |
| 2059   | Layout 1 | `cb6841b27f56`  |
| 2052   | Layout 1 | `cb6841b27f56`  |
| 2044   | Layout 1 | `cb6841b27f56`  |
| 2039   | Layout 1 | `cb6841b27f56`  |
| 2032   | Layout 1 | `cb6841b27f56`  |
| 2025   | Layout 1 | `cb6841b27f56`  |
| 2011   | Layout 1 | `cb6841b27f56`  |
| 2005   | Layout 1 | `cb6841b27f56`  |
| 2000   | Layout 1 | `cb6841b27f56`  |
| 1996   | Layout 1 | `cb6841b27f56`  |
| 1991   | Layout 1 | `cb6841b27f56`  |
| 1985   | Layout 1 | `cb6841b27f56`  |
| 1980   | Layout 1 | `cb6841b27f56`  |
| 1969   | Layout 1 | `cb6841b27f56`  |
| 1964   | Layout 1 | `cb6841b27f56`  |
| 1958   | Layout 1 | `cb6841b27f56`  |
| 1950   | Layout 1 | `cb6841b27f56`  |
| 1945   | Layout 1 | `cb6841b27f56`  |
| 1937   | Layout 1 | `cb6841b27f56`  |
| 1933   | Layout 1 | `cb6841b27f56`  |
| 1927   | Layout 1 | `cb6841b27f56`  |
| 1921   | Layout 1 | `cb6841b27f56`  |
| 1914   | Layout 1 | `cb6841b27f56`  |
| 1908   | Layout 1 | `cb6841b27f56`  |
| 1897   | Layout 1 | `cb6841b27f56`  |
| 1892   | Layout 1 | `cb6841b27f56`  |
| 1886   | Layout 1 | `cb6841b27f56`  |
| 1881   | Layout 1 | `cb6841b27f56`  |
| 1871   | Layout 1 | `cb6841b27f56`  |
| 1866   | Layout 1 | `cb6841b27f56`  |
| 1862   | Layout 1 | `cb6841b27f56`  |
| 1854   | Layout 1 | `cb6841b27f56`  |
| 1846   | Layout 1 | `cb6841b27f56`  |
| 1838   | Layout 1 | `cb6841b27f56`  |
| 1832   | Layout 1 | `cb6841b27f56`  |
| 1826   | Layout 1 | `cb6841b27f56`  |
| 1822   | Layout 1 | `cb6841b27f56`  |
| 1818   | Layout 1 | `cb6841b27f56`  |
| 1804   | Layout 1 | `cb6841b27f56`  |
| 1794   | Layout 1 | `cb6841b27f56`  |
| 1790   | Layout 1 | `cb6841b27f56`  |
| 1784   | Layout 1 | `cb6841b27f56`  |
| 1774   | Layout 1 | `cb6841b27f56`  |
| 1771   | Layout 1 | `cb6841b27f56`  |
| 1762   | Layout 1 | `cb6841b27f56`  |
| 1759   | Layout 1 | `cb6841b27f56`  |
| 1754   | Layout 1 | `cb6841b27f56`  |
| 1749   | Layout 1 | `cb6841b27f56`  |
| 1743   | Layout 1 | `cb6841b27f56`  |
| 1737   | Layout 1 | `cb6841b27f56`  |
| 1731   | Layout 1 | `cb6841b27f56`  |
| 1725   | Layout 1 | `cb6841b27f56`  |
| 1717   | Layout 1 | `cb6841b27f56`  |
| 1710   | Layout 1 | `cb6841b27f56`  |
| 1704   | Layout 1 | `cb6841b27f56`  |
| 1698   | Layout 1 | `cb6841b27f56`  |
| 1690   | Layout 1 | `cb6841b27f56`  |
| 1685   | Layout 1 | `cb6841b27f56`  |
| 1680   | Layout 1 | `cb6841b27f56`  |
| 1674   | Layout 1 | `cb6841b27f56`  |
| 1668   | Layout 1 | `cb6841b27f56`  |
| 1659   | Layout 1 | `cb6841b27f56`  |
| 1649   | Layout 1 | `cb6841b27f56`  |
| 1642   | Layout 1 | `cb6841b27f56`  |
| 1636   | Layout 1 | `cb6841b27f56`  |
| 1628   | Layout 1 | `cb6841b27f56`  |
| 1622   | Layout 1 | `cb6841b27f56`  |
| 1614   | Layout 1 | `cb6841b27f56`  |
| 1608   | Layout 1 | `cb6841b27f56`  |
| 1602   | Layout 1 | `cb6841b27f56`  |
| 1598   | Layout 1 | `cb6841b27f56`  |
| 1594   | Layout 1 | `cb6841b27f56`  |
| 1590   | Layout 1 | `cb6841b27f56`  |
| 1587   | Layout 1 | `cb6841b27f56`  |
| 1584   | Layout 1 | `cb6841b27f56`  |
| 1579   | Layout 1 | `cb6841b27f56`  |
| 1572   | Layout 1 | `cb6841b27f56`  |
| 1565   | Layout 1 | `cb6841b27f56`  |
| 1559   | Layout 1 | `cb6841b27f56`  |
| 1554   | Layout 1 | `cb6841b27f56`  |
| 1547   | Layout 1 | `cb6841b27f56`  |
| 1537   | Layout 1 | `cb6841b27f56`  |
| 1529   | Layout 1 | `cb6841b27f56`  |
| 1524   | Layout 1 | `cb6841b27f56`  |
| 1519   | Layout 1 | `cb6841b27f56`  |
| 1509   | Layout 1 | `cb6841b27f56`  |
| 1506   | Layout 1 | `cb6841b27f56`  |
| 1504   | Layout 1 | `cb6841b27f56`  |
| 1500   | Layout 1 | `cb6841b27f56`  |
| 1493   | Layout 1 | `cb6841b27f56`  |
| 1489   | Layout 1 | `cb6841b27f56`  |
| 1485   | Layout 1 | `cb6841b27f56`  |
| 1481   | Layout 1 | `cb6841b27f56`  |
| 1474   | Layout 1 | `cb6841b27f56`  |
| 1466   | Layout 1 | `cb6841b27f56`  |
| 1462   | Layout 1 | `cb6841b27f56`  |
| 1459   | Layout 1 | `cb6841b27f56`  |
| 1453   | Layout 1 | `cb6841b27f56`  |
| 1450   | Layout 1 | `cb6841b27f56`  |
| 1445   | Layout 1 | `cb6841b27f56`  |
| 1439   | Layout 1 | `cb6841b27f56`  |
| 1433   | Layout 1 | `cb6841b27f56`  |
| 1430   | Layout 1 | `cb6841b27f56`  |
| 1426   | Layout 1 | `cb6841b27f56`  |
| 1421   | Layout 1 | `cb6841b27f56`  |
| 1417   | Layout 1 | `cb6841b27f56`  |
| 1416   | Layout 1 | `cb6841b27f56`  |
| 1409   | Layout 1 | `cb6841b27f56`  |
| 1405   | Layout 1 | `cb6841b27f56`  |
| 1401   | Layout 1 | `cb6841b27f56`  |
| 1396   | Layout 1 | `cb6841b27f56`  |
| 1391   | Layout 1 | `cb6841b27f56`  |
| 1390   | Layout 1 | `cb6841b27f56`  |
| 1386   | Layout 1 | `cb6841b27f56`  |
| 1381   | Layout 1 | `cb6841b27f56`  |
| 1379   | Layout 1 | `cb6841b27f56`  |
| 1372   | Layout 1 | `cb6841b27f56`  |
| 1366   | Layout 1 | `cb6841b27f56`  |
| 1364   | Layout 1 | `cb6841b27f56`  |
| 1363   | Layout 1 | `cb6841b27f56`  |
| 1360   | Layout 1 | `cb6841b27f56`  |
| 1358   | Layout 1 | `cb6841b27f56`  |
| 1355   | Layout 1 | `cb6841b27f56`  |
| 1351   | Layout 1 | `cb6841b27f56`  |
| 1348   | Layout 1 | `cb6841b27f56`  |
| 1346   | Layout 1 | `cb6841b27f56`  |
| 1341   | Layout 1 | `cb6841b27f56`  |
| 1340   | Layout 1 | `cb6841b27f56`  |
| 1338   | Layout 1 | `cb6841b27f56`  |
| 1335   | Layout 1 | `cb6841b27f56`  |
| 1333   | Layout 1 | `cb6841b27f56`  |
| 1329   | Layout 1 | `cb6841b27f56`  |
| 1327   | Layout 1 | `cb6841b27f56`  |
| 1324   | Layout 1 | `cb6841b27f56`  |
| 1321   | Layout 1 | `cb6841b27f56`  |
| 1319   | Layout 1 | `cb6841b27f56`  |
| 1318   | Layout 1 | `cb6841b27f56`  |
| 1316   | Layout 1 | `cb6841b27f56`  |
| 1313   | Layout 1 | `cb6841b27f56`  |
| 1311   | Layout 1 | `cb6841b27f56`  |
| 1309   | Layout 1 | `cb6841b27f56`  |
| 1304   | Layout 1 | `cb6841b27f56`  |
| 1292   | Layout 1 | `cb6841b27f56`  |
| 1286   | Layout 1 | `cb6841b27f56`  |
| 1280   | Layout 1 | `cb6841b27f56`  |
| 1276   | Layout 1 | `cb6841b27f56`  |
| 1267   | Layout 1 | `cb6841b27f56`  |
| 1261   | Layout 1 | `cb6841b27f56`  |
| 1256   | Layout 1 | `cb6841b27f56`  |
| 1250   | Layout 1 | `cb6841b27f56`  |
| 1246   | Layout 1 | `cb6841b27f56`  |
| 1239   | Layout 1 | `cb6841b27f56`  |
| 1230   | Layout 1 | `cb6841b27f56`  |
| 1226   | Layout 1 | `cb6841b27f56`  |
| 1220   | Layout 1 | `cb6841b27f56`  |
| 1217   | Layout 1 | `cb6841b27f56`  |
| 1211   | Layout 1 | `cb6841b27f56`  |
| 1210   | Layout 1 | `cb6841b27f56`  |
| 1208   | Layout 1 | `cb6841b27f56`  |
| 1203   | Layout 1 | `cb6841b27f56`  |
| 1197   | Layout 1 | `cb6841b27f56`  |
| 1194   | Layout 1 | `cb6841b27f56`  |
| 1192   | No file  | `cb6841b27f56`  |
| 1187   | No file  | `cb6841b27f56`  |
| 1183   | No file  | `cb6841b27f56`  |
| 1177   | No file  | `cb6841b27f56`  |
| 1173   | No file  | `cb6841b27f56`  |
| 1167   | No file  | `cb6841b27f56`  |
| 1164   | No file  | `cb6841b27f56`  |
| 1156   | No file  | `cb6841b27f56`  |
| 1149   | No file  | `cb6841b27f56`  |
| 1144   | No file  | `cb6841b27f56`  |
| 1137   | No file  | `cb6841b27f56`  |
| 1132   | No file  | `cb6841b27f56`  |
| 1127   | No file  | `cb6841b27f56`  |
| 1122   | No file  | `cb6841b27f56`  |
| 1118   | No file  | `cb6841b27f56`  |
| 1114   | No file  | `cb6841b27f56`  |
| 1109   | No file  | `cb6841b27f56`  |
| 1102   | No file  | `cb6841b27f56`  |
| 1096   | No file  | `cb6841b27f56`  |
| 1088   | No file  | `cb6841b27f56`  |
| 1081   | No file  | `cb6841b27f56`  |
| 1076   | No file  | `cb6841b27f56`  |
| 1069   | No file  | `cb6841b27f56`  |
| 1064   | No file  | `cb6841b27f56`  |
| 1058   | No file  | `cb6841b27f56`  |
| 1051   | No file  | `cb6841b27f56`  |
| 1044   | No file  | `cb6841b27f56`  |
| 1036   | No file  | `cb6841b27f56`  |
| 1026   | No file  | `cb6841b27f56`  |
| 1016   | No file  | `cb6841b27f56`  |
| 1009   | No file  | `cb6841b27f56`  |
| 1005   | No file  | `cb6841b27f56`  |
| 1000   | No file  | `cb6841b27f56`  |
| 998    | No file  | `cb6841b27f56`  |
| 990    | No file  | `cb6841b27f56`  |
| 979    | No file  | `cb6841b27f56`  |
| 972    | No file  | `cb6841b27f56`  |
| 963    | No file  | `cb6841b27f56`  |
| 955    | No file  | `cb6841b27f56`  |
| 946    | No file  | `cb6841b27f56`  |
| 938    | No file  | `cb6841b27f56`  |
| 927    | No file  | `cb6841b27f56`  |
| 911    | No file  | `cb6841b27f56`  |
| 904    | No file  | `cb6841b27f56`  |
| 899    | No file  | `cb6841b27f56`  |
| 894    | No file  | `cb6841b27f56`  |
| 885    | No file  | `cb6841b27f56`  |
| 879    | No file  | `cb6841b27f56`  |
| 872    | No file  | `cb6841b27f56`  |
| 864    | No file  | `cb6841b27f56`  |
| 855    | No file  | `cb6841b27f56`  |
| 853    | No file  | `cb6841b27f56`  |
| 845    | No file  | `cb6841b27f56`  |
| 837    | No file  | `cb6841b27f56`  |
| 829    | No file  | `cb6841b27f56`  |
| 822    | No file  | `cb6841b27f56`  |
| 814    | No file  | `cb6841b27f56`  |
| 805    | No file  | `cb6841b27f56`  |
| 794    | No file  | `cb6841b27f56`  |
| 787    | No file  | `cb6841b27f56`  |
| 780    | No file  | `cb6841b27f56`  |
| 771    | No file  | `cb6841b27f56`  |
| 760    | No file  | `cb6841b27f56`  |
| 748    | No file  | `cb6841b27f56`  |
| 741    | No file  | `cb6841b27f56`  |
| 736    | No file  | `cb6841b27f56`  |
| 731    | No file  | `cb6841b27f56`  |
| 723    | No file  | `cb6841b27f56`  |
| 711    | No file  | `cb6841b27f56`  |
| 707    | No file  | `cb6841b27f56`  |
| 697    | No file  | `cb6841b27f56`  |
| 689    | No file  | `cb6841b27f56`  |
| 683    | No file  | `cb6841b27f56`  |
| 678    | No file  | `cb6841b27f56`  |
| 670    | No file  | `cb6841b27f56`  |
| 661    | No file  | `cb6841b27f56`  |
| 656    | No file  | `cb6841b27f56`  |
| 652    | No file  | `cb6841b27f56`  |
| 643    | No file  | `cb6841b27f56`  |
| 637    | No file  | `cb6841b27f56`  |
| 630    | No file  | `cb6841b27f56`  |
| 627    | No file  | `cb6841b27f56`  |
| 621    | No file  | `cb6841b27f56`  |
| 617    | No file  | `cb6841b27f56`  |
| 615    | No file  | `cb6841b27f56`  |
| 606    | No file  | `cb6841b27f56`  |
| 599    | No file  | `cb6841b27f56`  |
| 592    | No file  | `cb6841b27f56`  |
| 586    | No file  | `cb6841b27f56`  |
| 577    | No file  | `cb6841b27f56`  |
| 569    | No file  | `cb6841b27f56`  |
| 561    | No file  | `cb6841b27f56`  |
| 554    | No file  | `cb6841b27f56`  |
| 542    | No file  | `cb6841b27f56`  |
| 532    | No file  | `cb6841b27f56`  |
| 531    | No file  | `cb6841b27f56`  |
| 526    | No file  | `cb6841b27f56`  |
| 521    | No file  | `cb6841b27f56`  |
| 517    | No file  | `cb6841b27f56`  |
| 510    | No file  | `cb6841b27f56`  |
| 508    | No file  | `cb6841b27f56`  |
| 504    | No file  | `cb6841b27f56`  |
| 497    | No file  | `cb6841b27f56`  |
| 491    | No file  | `cb6841b27f56`  |
| 485    | No file  | `cb6841b27f56`  |
| 478    | No file  | `cb6841b27f56`  |
| 472    | No file  | `cb6841b27f56`  |
| 466    | No file  | `cb6841b27f56`  |
| 457    | No file  | `cb6841b27f56`  |
| 452    | No file  | `cb6841b27f56`  |
| 449    | No file  | `cb6841b27f56`  |
| 435    | No file  | `cb6841b27f56`  |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads names through the shared LOC
lookup and the skill icons through the skill icon index:

| File                  | Required | Role                                                     |
| --------------------- | -------- | -------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names (LOC type `10`, `str_id1` = skill number)    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type             | Field        | Notes                                                              |
| ------------------- | ---------------- | ------------ | ------------------------------------------------------------------ |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                                       |
| `+0x04`             | u32              | unknown_04   | `0` on every client from 1194 to 3482; see [Open Questions](#open-questions) |
| `+0x08`             | u32              | skill_count  | Number of skill keys; `14405` on client 3482, `11327` on client 1784 |
| `+0x0c`             | u32[skill_count] | skill_keys   | `skill_no << 16 \| level`; see [Skill Keys](#skill-keys)           |
| `skill_keys+0x00`   | String Table     | string_table | Empty: `string_count` is `0`                                       |
| `string_table+0x00` | u32              | table_start  | Offset of the string table, where `skill_keys` ends                |
| `string_table+0x04` | u32              | zero         | Always `0`                                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | No field reads a string      |

## Skill Keys

On client 3482 every key is level `1`, every skill number appears once, and
the keys are in no key order (the first are `57005`, `57004`, `57007`,
`57006`). All 14,405 keys have a `skill.dbss`, `skillsimply.dbss` and
`skilltype.dbss` row, and on all of them `kind` is `0` and
`skill_owner_type` is `0`, such as `57005` "[Event] Energy of Happiness".

Together with the two lists of `privateskill.bss` the file holds every
level `1` key of `skillsimply.dbss` with `skill_owner_type` `0`, each in
one list, by `kind`:

| File               | List             | `kind`    | Keys (client 3482) |
| ------------------ | ---------------- | --------- | ------------------ |
| `publicskill.bss`  | `skill_keys`     | `0` Other | 14,405             |
| `privateskill.bss` | `active_skills`  | `1` Active | 10,044            |
| `privateskill.bss` | `passive_skills` | `2` Passive | 5,250            |

None of the three lists holds the 766 guild skills (`skill_owner_type`
`1`) or the 10 `skilltype.dbss` keys without a `skill.dbss` row, such as
`52185` "Olvia Academy Life EXP - Barter (324.5)".

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has a
publicskill or privateskill name, and no client Lua on client 3482 names
either file. The `binary/` folder of that private server holds both files,
compiled from its sheets with the same layouts, so the client builds them
from the skill sheets.

| Field      | Source                                                                   |
| ---------- | ------------------------------------------------------------------------ |
| skill_key  | The `skill_no << 16 \| level` key of every skill table; 14,405 of 14,405 keys are `skill.dbss` keys (client 3482) |
| skill_keys | Every key's `kind` is `0`, the 2016 enum `SkillType` value `eItemSkillType` |

## Notes

- The handler shows one row per key: the skill number linked to its
  `skill.dbss` row, then the skill icon and LOC type `10` name, as the
  `skillawakeningability2.bss` handler does.
- The 2016 exe binds `isPrivateSkill` on `SkillTypeStaticStatusWrapper` for
  the Lua; no `.luac` on client 3482 calls it.

## Open Questions

### What a Non-Zero `unknown_04` Holds

The u32 at `0x04` sits where `privateskill.bss` keeps its first list count,
`active_count`, so it may count a list that is empty in every checked
file: it is `0` on all 356 test clients from 1194, where the file first
appears, to 3482. With no rows to read, the row size of such a list is not
known, and the parser rejects a file where the value is not `0`.

No source names the field:

| Source                                                 | What it holds                                                   |
| ------------------------------------------------------ | --------------------------------------------------------------- |
| Client Lua on client 3482                              | No call names `publicskill` or `privateskill`                   |
| A private server's `DataSheets.bexcel` on client 1784  | No sheet or column named for either file                        |
| That private server's server exe                       | No record loader and no string for either file                  |
| The client 519 private server's tables and server code | No table or class named for either file                         |
| The 2016 exe and PDB                                   | Only `isPrivateSkill` on `SkillTypeStaticStatusWrapper`; they predate client 1194 |
