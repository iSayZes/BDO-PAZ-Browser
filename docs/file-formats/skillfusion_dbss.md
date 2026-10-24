# `skillfusion.dbss` Format

## Purpose

The Skill Enhancement choices: each enhanced skill with the main skill and
the sub skill it combines, the enhancement slot it belongs to and its
order among the choices for one main skill. The Skill window's enhancement
panel (`panel_window_skill_combination.luac`) lists a slot's rows through
`ToClient_getFusionSkillListCount(slot)`, `ToClient_getFusionMainSkillNo`,
`ToClient_getFusionSubSkillNo` and `ToClient_getFusionSkillNo`. Companion
`skillfusionoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1346 and later | 3483    | `skillfusion.dbss`       | 4,612 | 192 Row        | 24        |
| 1      | 1346 and later | 3483    | `skillfusionoffset.dbss` | 2,308 | 192 Offset Row | 12        |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `skillfusion.dbss`       | 4,612 B (100.0%) | 0 B (0.0%) |
| 1      | `skillfusionoffset.dbss` | 2,308 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ed564a62f8ec`  |
| 3482   | Layout 1             | `ed564a62f8ec`  |
| 3474   | Layout 1             | `ed564a62f8ec`  |
| 3473   | Layout 1             | `ed564a62f8ec`  |
| 3464   | Layout 1             | `ed564a62f8ec`  |
| 3458   | Layout 1             | `ed564a62f8ec`  |
| 3454   | Layout 1             | `ed564a62f8ec`  |
| 3444   | Layout 1             | `ed564a62f8ec`  |
| 3435   | Layout 1             | `ed564a62f8ec`  |
| 3426   | Layout 1             | `ed564a62f8ec`  |
| 3418   | Layout 1             | `ed564a62f8ec`  |
| 3412   | Layout 1             | `ed564a62f8ec`  |
| 3402   | Layout 1             | `ed564a62f8ec`  |
| 3396   | Layout 1             | `ed564a62f8ec`  |
| 3387   | Layout 1             | `ed564a62f8ec`  |
| 3381   | Layout 1             | `ed564a62f8ec`  |
| 3373   | Layout 1             | `ed564a62f8ec`  |
| 3364   | Layout 1             | `ed564a62f8ec`  |
| 3356   | Layout 1             | `ed564a62f8ec`  |
| 3349   | Layout 1             | `ed564a62f8ec`  |
| 3342   | Layout 1             | `ed564a62f8ec`  |
| 3335   | Layout 1             | `ed564a62f8ec`  |
| 3326   | Layout 1             | `ed564a62f8ec`  |
| 3321   | Layout 1             | `ed564a62f8ec`  |
| 3314   | Layout 1             | `ed564a62f8ec`  |
| 3303   | Layout 1             | `ed564a62f8ec`  |
| 3302   | Layout 1             | `ed564a62f8ec`  |
| 3293   | Layout 1             | `ed564a62f8ec`  |
| 3283   | Layout 1             | `ed564a62f8ec`  |
| 3275   | Layout 1             | `ed564a62f8ec`  |
| 3267   | Layout 1             | `ed564a62f8ec`  |
| 3258   | Layout 1             | `ed564a62f8ec`  |
| 3251   | Layout 1             | `ed564a62f8ec`  |
| 3242   | Layout 1             | `ed564a62f8ec`  |
| 3235   | Layout 1             | `ed564a62f8ec`  |
| 3229   | Layout 1             | `ed564a62f8ec`  |
| 3212   | Layout 1             | `ed564a62f8ec`  |
| 3203   | Layout 1             | `ed564a62f8ec`  |
| 3193   | Layout 1             | `ed564a62f8ec`  |
| 3186   | Layout 1             | `ed564a62f8ec`  |
| 3177   | Layout 1             | `ed564a62f8ec`  |
| 3169   | Layout 1             | `ed564a62f8ec`  |
| 3158   | Layout 1             | `ed564a62f8ec`  |
| 3151   | Layout 1             | `ed564a62f8ec`  |
| 3144   | Layout 1             | `ed564a62f8ec`  |
| 3133   | Layout 1             | `ed564a62f8ec`  |
| 3125   | Layout 1             | `ed564a62f8ec`  |
| 3118   | Layout 1             | `ed564a62f8ec`  |
| 3111   | Layout 1             | `ed564a62f8ec`  |
| 3103   | Layout 1             | `ed564a62f8ec`  |
| 3095   | Layout 1             | `ed564a62f8ec`  |
| 3086   | Layout 1             | `ed564a62f8ec`  |
| 3072   | Layout 1             | `ed564a62f8ec`  |
| 3062   | Layout 1             | `ed564a62f8ec`  |
| 3052   | Layout 1             | `ed564a62f8ec`  |
| 3045   | Layout 1             | `ed564a62f8ec`  |
| 3037   | Layout 1             | `ed564a62f8ec`  |
| 3030   | Layout 1             | `ed564a62f8ec`  |
| 3021   | Layout 1             | `ed564a62f8ec`  |
| 3012   | Layout 1             | `ed564a62f8ec`  |
| 3002   | Layout 1             | `ed564a62f8ec`  |
| 2995   | Layout 1             | `ed564a62f8ec`  |
| 2987   | Layout 1             | `ed564a62f8ec`  |
| 2978   | Layout 1             | `ed564a62f8ec`  |
| 2970   | Layout 1             | `ed564a62f8ec`  |
| 2959   | Layout 1             | `ed564a62f8ec`  |
| 2951   | Layout 1             | `ed564a62f8ec`  |
| 2942   | Layout 1             | `ed564a62f8ec`  |
| 2935   | Layout 1             | `ed564a62f8ec`  |
| 2932   | Layout 1             | `ed564a62f8ec`  |
| 2923   | Layout 1             | `ed564a62f8ec`  |
| 2919   | Layout 1             | `ed564a62f8ec`  |
| 2907   | Layout 1             | `ed564a62f8ec`  |
| 2900   | Layout 1             | `ed564a62f8ec`  |
| 2891   | Layout 1             | `ed564a62f8ec`  |
| 2882   | Layout 1             | `ed564a62f8ec`  |
| 2872   | Layout 1             | `ed564a62f8ec`  |
| 2863   | Layout 1             | `ed564a62f8ec`  |
| 2855   | Layout 1             | `ed564a62f8ec`  |
| 2849   | Layout 1             | `ed564a62f8ec`  |
| 2844   | Layout 1             | `ed564a62f8ec`  |
| 2834   | Layout 1             | `ed564a62f8ec`  |
| 2825   | Layout 1             | `ed564a62f8ec`  |
| 2819   | Layout 1             | `ed564a62f8ec`  |
| 2811   | Layout 1             | `ed564a62f8ec`  |
| 2803   | Layout 1             | `ed564a62f8ec`  |
| 2794   | Layout 1             | `ed564a62f8ec`  |
| 2783   | Layout 1             | `ed564a62f8ec`  |
| 2774   | Layout 1             | `ed564a62f8ec`  |
| 2765   | Layout 1             | `ed564a62f8ec`  |
| 2756   | Layout 1             | `ed564a62f8ec`  |
| 2750   | Layout 1             | `ed564a62f8ec`  |
| 2743   | Layout 1             | `ed564a62f8ec`  |
| 2736   | Layout 1             | `ed564a62f8ec`  |
| 2726   | Layout 1             | `ed564a62f8ec`  |
| 2717   | Layout 1             | `ed564a62f8ec`  |
| 2709   | Layout 1             | `ed564a62f8ec`  |
| 2703   | Layout 1             | `ed564a62f8ec`  |
| 2695   | Layout 1             | `ed564a62f8ec`  |
| 2684   | Layout 1             | `ed564a62f8ec`  |
| 2672   | Layout 1             | `ed564a62f8ec`  |
| 2665   | Layout 1             | `ed564a62f8ec`  |
| 2657   | Layout 1             | `ed564a62f8ec`  |
| 2649   | Layout 1             | `ed564a62f8ec`  |
| 2644   | Layout 1             | `ed564a62f8ec`  |
| 2637   | Layout 1             | `ed564a62f8ec`  |
| 2629   | Layout 1             | `ed564a62f8ec`  |
| 2619   | Layout 1             | `ed564a62f8ec`  |
| 2612   | Layout 1             | `ed564a62f8ec`  |
| 2606   | Layout 1             | `ed564a62f8ec`  |
| 2602   | Layout 1             | `ed564a62f8ec`  |
| 2601   | Layout 1             | `ed564a62f8ec`  |
| 2592   | Layout 1             | `ed564a62f8ec`  |
| 2583   | Layout 1             | `ed564a62f8ec`  |
| 2575   | Layout 1             | `ed564a62f8ec`  |
| 2567   | Layout 1             | `ed564a62f8ec`  |
| 2560   | Layout 1             | `ed564a62f8ec`  |
| 2553   | Layout 1             | `ed564a62f8ec`  |
| 2545   | Layout 1             | `ed564a62f8ec`  |
| 2538   | Layout 1             | `ed564a62f8ec`  |
| 2529   | Layout 1             | `ed564a62f8ec`  |
| 2519   | Layout 1             | `ed564a62f8ec`  |
| 2513   | Layout 1             | `ed564a62f8ec`  |
| 2510   | Layout 1             | `ed564a62f8ec`  |
| 2507   | Layout 1             | `ed564a62f8ec`  |
| 2503   | Layout 1             | `ed564a62f8ec`  |
| 2498   | Layout 1             | `ed564a62f8ec`  |
| 2492   | Layout 1             | `ed564a62f8ec`  |
| 2487   | Layout 1             | `ed564a62f8ec`  |
| 2480   | Layout 1             | `ed564a62f8ec`  |
| 2474   | Layout 1             | `ed564a62f8ec`  |
| 2468   | Layout 1             | `ed564a62f8ec`  |
| 2460   | Layout 1             | `ed564a62f8ec`  |
| 2453   | Layout 1             | `ed564a62f8ec`  |
| 2444   | Layout 1             | `ed564a62f8ec`  |
| 2438   | Layout 1             | `ed564a62f8ec`  |
| 2434   | Layout 1             | `ed564a62f8ec`  |
| 2429   | Layout 1             | `ed564a62f8ec`  |
| 2421   | Layout 1             | `ed564a62f8ec`  |
| 2414   | Layout 1             | `ed564a62f8ec`  |
| 2407   | Layout 1             | `ed564a62f8ec`  |
| 2401   | Layout 1             | `ed564a62f8ec`  |
| 2397   | Layout 1             | `ed564a62f8ec`  |
| 2393   | Layout 1             | `ed564a62f8ec`  |
| 2384   | Layout 1             | `ed564a62f8ec`  |
| 2378   | Layout 1             | `ed564a62f8ec`  |
| 2372   | Layout 1             | `ed564a62f8ec`  |
| 2358   | Layout 1             | `ed564a62f8ec`  |
| 2352   | Layout 1             | `ed564a62f8ec`  |
| 2347   | Layout 1             | `ed564a62f8ec`  |
| 2343   | Layout 1             | `ed564a62f8ec`  |
| 2335   | Layout 1             | `ed564a62f8ec`  |
| 2327   | Layout 1             | `ed564a62f8ec`  |
| 2324   | Layout 1             | `ed564a62f8ec`  |
| 2319   | Layout 1             | `ed564a62f8ec`  |
| 2313   | Layout 1             | `ed564a62f8ec`  |
| 2308   | Layout 1             | `ed564a62f8ec`  |
| 2302   | Layout 1             | `ed564a62f8ec`  |
| 2295   | Layout 1             | `ed564a62f8ec`  |
| 2290   | Layout 1             | `ed564a62f8ec`  |
| 2284   | Layout 1             | `ed564a62f8ec`  |
| 2276   | Layout 1             | `ed564a62f8ec`  |
| 2269   | Layout 1             | `ed564a62f8ec`  |
| 2259   | Layout 1             | `ed564a62f8ec`  |
| 2250   | Layout 1             | `ed564a62f8ec`  |
| 2243   | Layout 1             | `ed564a62f8ec`  |
| 2235   | Layout 1             | `ed564a62f8ec`  |
| 2229   | Layout 1             | `ed564a62f8ec`  |
| 2224   | Layout 1             | `ed564a62f8ec`  |
| 2218   | Layout 1             | `ed564a62f8ec`  |
| 2215   | Layout 1             | `ed564a62f8ec`  |
| 2207   | Layout 1             | `ed564a62f8ec`  |
| 2203   | Layout 1             | `ed564a62f8ec`  |
| 2196   | Layout 1             | `ed564a62f8ec`  |
| 2192   | Layout 1             | `ed564a62f8ec`  |
| 2189   | Layout 1             | `ed564a62f8ec`  |
| 2183   | Layout 1             | `ed564a62f8ec`  |
| 2179   | Layout 1             | `ed564a62f8ec`  |
| 2171   | Layout 1             | `ed564a62f8ec`  |
| 2163   | Layout 1             | `ed564a62f8ec`  |
| 2156   | Layout 1             | `ed564a62f8ec`  |
| 2151   | Layout 1             | `ed564a62f8ec`  |
| 2147   | Layout 1             | `ed564a62f8ec`  |
| 2142   | Layout 1             | `ed564a62f8ec`  |
| 2138   | Layout 1             | `ed564a62f8ec`  |
| 2134   | Layout 1             | `ed564a62f8ec`  |
| 2130   | Layout 1             | `ed564a62f8ec`  |
| 2122   | Layout 1             | `ed564a62f8ec`  |
| 2107   | Layout 1             | `ed564a62f8ec`  |
| 2098   | Layout 1             | `ed564a62f8ec`  |
| 2089   | Layout 1             | `ed564a62f8ec`  |
| 2081   | Layout 1             | `ed564a62f8ec`  |
| 2073   | Layout 1             | `ed564a62f8ec`  |
| 2067   | Layout 1             | `ed564a62f8ec`  |
| 2063   | Layout 1             | `ed564a62f8ec`  |
| 2059   | Layout 1             | `ed564a62f8ec`  |
| 2052   | Layout 1             | `ed564a62f8ec`  |
| 2044   | Layout 1             | `ed564a62f8ec`  |
| 2039   | Layout 1             | `ed564a62f8ec`  |
| 2032   | Layout 1             | `ed564a62f8ec`  |
| 2025   | Layout 1             | `ed564a62f8ec`  |
| 2011   | Layout 1             | `ed564a62f8ec`  |
| 2005   | Layout 1             | `ed564a62f8ec`  |
| 2000   | Layout 1             | `ed564a62f8ec`  |
| 1996   | Layout 1             | `ed564a62f8ec`  |
| 1991   | Layout 1             | `ed564a62f8ec`  |
| 1985   | Layout 1             | `ed564a62f8ec`  |
| 1980   | Layout 1             | `ed564a62f8ec`  |
| 1969   | Layout 1             | `ed564a62f8ec`  |
| 1964   | Layout 1             | `ed564a62f8ec`  |
| 1958   | Layout 1             | `ed564a62f8ec`  |
| 1950   | Layout 1             | `ed564a62f8ec`  |
| 1945   | Layout 1             | `ed564a62f8ec`  |
| 1937   | Layout 1             | `ed564a62f8ec`  |
| 1933   | Layout 1             | `ed564a62f8ec`  |
| 1927   | Layout 1             | `ed564a62f8ec`  |
| 1921   | Layout 1             | `ed564a62f8ec`  |
| 1914   | Layout 1             | `ed564a62f8ec`  |
| 1908   | Layout 1             | `ed564a62f8ec`  |
| 1897   | Layout 1             | `ed564a62f8ec`  |
| 1892   | Layout 1             | `ed564a62f8ec`  |
| 1886   | Layout 1             | `ed564a62f8ec`  |
| 1881   | Layout 1             | `ed564a62f8ec`  |
| 1871   | Layout 1             | `ed564a62f8ec`  |
| 1866   | Layout 1             | `ed564a62f8ec`  |
| 1862   | Layout 1             | `ed564a62f8ec`  |
| 1854   | Layout 1             | `ed564a62f8ec`  |
| 1846   | Layout 1             | `ed564a62f8ec`  |
| 1838   | Layout 1             | `ed564a62f8ec`  |
| 1832   | Layout 1             | `ed564a62f8ec`  |
| 1826   | Layout 1             | `ed564a62f8ec`  |
| 1822   | Layout 1             | `ed564a62f8ec`  |
| 1818   | Layout 1             | `ed564a62f8ec`  |
| 1804   | Layout 1             | `ed564a62f8ec`  |
| 1794   | Layout 1             | `ed564a62f8ec`  |
| 1790   | Layout 1             | `ed564a62f8ec`  |
| 1784   | Layout 1             | `ed564a62f8ec`  |
| 1774   | Layout 1             | `ed564a62f8ec`  |
| 1771   | Layout 1             | `ed564a62f8ec`  |
| 1762   | Layout 1             | `ed564a62f8ec`  |
| 1759   | Layout 1             | `ed564a62f8ec`  |
| 1754   | Layout 1             | `ed564a62f8ec`  |
| 1749   | Layout 1             | `ed564a62f8ec`  |
| 1743   | Layout 1             | `ed564a62f8ec`  |
| 1737   | Layout 1             | `ed564a62f8ec`  |
| 1731   | Layout 1             | `ed564a62f8ec`  |
| 1725   | Layout 1             | `ed564a62f8ec`  |
| 1717   | Layout 1             | `ed564a62f8ec`  |
| 1710   | Layout 1             | `ed564a62f8ec`  |
| 1704   | Layout 1             | `ed564a62f8ec`  |
| 1698   | Layout 1             | `ed564a62f8ec`  |
| 1690   | Layout 1             | `ed564a62f8ec`  |
| 1685   | Layout 1             | `ed564a62f8ec`  |
| 1680   | Layout 1             | `ed564a62f8ec`  |
| 1674   | Layout 1             | `ed564a62f8ec`  |
| 1668   | Layout 1             | `ed564a62f8ec`  |
| 1659   | Layout 1             | `ed564a62f8ec`  |
| 1649   | Layout 1             | `ed564a62f8ec`  |
| 1642   | Layout 1             | `ed564a62f8ec`  |
| 1636   | Layout 1             | `ed564a62f8ec`  |
| 1628   | Layout 1             | `ed564a62f8ec`  |
| 1622   | Layout 1             | `ed564a62f8ec`  |
| 1614   | Layout 1             | `ed564a62f8ec`  |
| 1608   | Layout 1             | `ed564a62f8ec`  |
| 1602   | Layout 1             | `ed564a62f8ec`  |
| 1598   | Layout 1             | `ed564a62f8ec`  |
| 1594   | Layout 1             | `ed564a62f8ec`  |
| 1590   | Layout 1             | `ed564a62f8ec`  |
| 1587   | Layout 1             | `ed564a62f8ec`  |
| 1584   | Layout 1             | `ed564a62f8ec`  |
| 1579   | Layout 1             | `ed564a62f8ec`  |
| 1572   | Layout 1             | `ed564a62f8ec`  |
| 1565   | Layout 1             | `ed564a62f8ec`  |
| 1559   | Layout 1             | `ed564a62f8ec`  |
| 1554   | Layout 1             | `ed564a62f8ec`  |
| 1547   | Layout 1             | `ed564a62f8ec`  |
| 1537   | Layout 1             | `ed564a62f8ec`  |
| 1529   | Layout 1             | `ed564a62f8ec`  |
| 1524   | Layout 1             | `ed564a62f8ec`  |
| 1519   | Layout 1             | `ed564a62f8ec`  |
| 1509   | Layout 1             | `ed564a62f8ec`  |
| 1506   | Layout 1             | `ed564a62f8ec`  |
| 1504   | Layout 1             | `ed564a62f8ec`  |
| 1500   | Layout 1             | `ed564a62f8ec`  |
| 1493   | Layout 1             | `ed564a62f8ec`  |
| 1489   | Layout 1             | `ed564a62f8ec`  |
| 1485   | Layout 1             | `ed564a62f8ec`  |
| 1481   | Layout 1             | `ed564a62f8ec`  |
| 1474   | Layout 1             | `ed564a62f8ec`  |
| 1466   | Layout 1             | `ed564a62f8ec`  |
| 1462   | Layout 1             | `ed564a62f8ec`  |
| 1459   | Layout 1             | `ed564a62f8ec`  |
| 1453   | Layout 1             | `ed564a62f8ec`  |
| 1450   | Layout 1             | `ed564a62f8ec`  |
| 1445   | Layout 1             | `ed564a62f8ec`  |
| 1439   | Layout 1             | `ed564a62f8ec`  |
| 1433   | Layout 1             | `ed564a62f8ec`  |
| 1430   | Layout 1             | `ed564a62f8ec`  |
| 1426   | Layout 1             | `ed564a62f8ec`  |
| 1421   | Layout 1             | `ed564a62f8ec`  |
| 1417   | Layout 1             | `ed564a62f8ec`  |
| 1416   | Layout 1             | `ed564a62f8ec`  |
| 1409   | Layout 1             | `ed564a62f8ec`  |
| 1405   | Layout 1             | `ed564a62f8ec`  |
| 1401   | Layout 1             | `ed564a62f8ec`  |
| 1396   | Layout 1             | `ed564a62f8ec`  |
| 1391   | Layout 1             | `ed564a62f8ec`  |
| 1390   | Layout 1             | `ed564a62f8ec`  |
| 1386   | Layout 1             | `ed564a62f8ec`  |
| 1381   | Layout 1             | `ed564a62f8ec`  |
| 1379   | Layout 1             | `ed564a62f8ec`  |
| 1372   | Layout 1             | `ed564a62f8ec`  |
| 1366   | Layout 1             | `ed564a62f8ec`  |
| 1364   | Layout 1             | `ed564a62f8ec`  |
| 1363   | Layout 1             | `ed564a62f8ec`  |
| 1360   | Layout 1             | `ed564a62f8ec`  |
| 1358   | Layout 1             | `ed564a62f8ec`  |
| 1355   | Layout 1             | `ed564a62f8ec`  |
| 1351   | Layout 1             | `ed564a62f8ec`  |
| 1348   | Layout 1             | `ed564a62f8ec`  |
| 1346   | Layout 1             | `ed564a62f8ec`  |
| 1341   | No documented layout | `ed564a62f8ec`  |
| 1340   | No documented layout | `ed564a62f8ec`  |
| 1338   | No documented layout | `ed564a62f8ec`  |
| 1335   | No documented layout | `ed564a62f8ec`  |
| 1333   | No documented layout | `ed564a62f8ec`  |
| 1329   | No documented layout | `ed564a62f8ec`  |
| 1327   | No documented layout | `ed564a62f8ec`  |
| 1324   | No documented layout | `ed564a62f8ec`  |
| 1321   | No documented layout | `ed564a62f8ec`  |
| 1319   | No documented layout | `ed564a62f8ec`  |
| 1318   | No documented layout | `ed564a62f8ec`  |
| 1316   | No documented layout | `ed564a62f8ec`  |
| 1313   | No documented layout | `ed564a62f8ec`  |
| 1311   | No documented layout | `ed564a62f8ec`  |
| 1309   | No documented layout | `ed564a62f8ec`  |
| 1304   | No documented layout | `ed564a62f8ec`  |
| 1292   | No documented layout | `ed564a62f8ec`  |
| 1286   | No file              | `ed564a62f8ec`  |
| 1280   | No file              | `ed564a62f8ec`  |
| 1276   | No file              | `ed564a62f8ec`  |
| 1267   | No file              | `ed564a62f8ec`  |
| 1261   | No file              | `ed564a62f8ec`  |
| 1256   | No file              | `ed564a62f8ec`  |
| 1250   | No file              | `ed564a62f8ec`  |
| 1246   | No file              | `ed564a62f8ec`  |
| 1239   | No file              | `ed564a62f8ec`  |
| 1230   | No file              | `ed564a62f8ec`  |
| 1226   | No file              | `ed564a62f8ec`  |
| 1220   | No file              | `ed564a62f8ec`  |
| 1217   | No file              | `ed564a62f8ec`  |
| 1211   | No file              | `ed564a62f8ec`  |
| 1210   | No file              | `ed564a62f8ec`  |
| 1208   | No file              | `ed564a62f8ec`  |
| 1203   | No file              | `ed564a62f8ec`  |
| 1197   | No file              | `ed564a62f8ec`  |
| 1194   | No file              | `ed564a62f8ec`  |
| 1192   | No file              | `ed564a62f8ec`  |
| 1187   | No file              | `ed564a62f8ec`  |
| 1183   | No file              | `ed564a62f8ec`  |
| 1177   | No file              | `ed564a62f8ec`  |
| 1173   | No file              | `ed564a62f8ec`  |
| 1167   | No file              | `ed564a62f8ec`  |
| 1164   | No file              | `ed564a62f8ec`  |
| 1156   | No file              | `ed564a62f8ec`  |
| 1149   | No file              | `ed564a62f8ec`  |
| 1144   | No file              | `ed564a62f8ec`  |
| 1137   | No file              | `ed564a62f8ec`  |
| 1132   | No file              | `ed564a62f8ec`  |
| 1127   | No file              | `ed564a62f8ec`  |
| 1122   | No file              | `ed564a62f8ec`  |
| 1118   | No file              | `ed564a62f8ec`  |
| 1114   | No file              | `ed564a62f8ec`  |
| 1109   | No file              | `ed564a62f8ec`  |
| 1102   | No file              | `ed564a62f8ec`  |
| 1096   | No file              | `ed564a62f8ec`  |
| 1088   | No file              | `ed564a62f8ec`  |
| 1081   | No file              | `ed564a62f8ec`  |
| 1076   | No file              | `ed564a62f8ec`  |
| 1069   | No file              | `ed564a62f8ec`  |
| 1064   | No file              | `ed564a62f8ec`  |
| 1058   | No file              | `ed564a62f8ec`  |
| 1051   | No file              | `ed564a62f8ec`  |
| 1044   | No file              | `ed564a62f8ec`  |
| 1036   | No file              | `ed564a62f8ec`  |
| 1026   | No file              | `ed564a62f8ec`  |
| 1016   | No file              | `ed564a62f8ec`  |
| 1009   | No file              | `ed564a62f8ec`  |
| 1005   | No file              | `ed564a62f8ec`  |
| 1000   | No file              | `ed564a62f8ec`  |
| 998    | No file              | `ed564a62f8ec`  |
| 990    | No file              | `ed564a62f8ec`  |
| 979    | No file              | `ed564a62f8ec`  |
| 972    | No file              | `ed564a62f8ec`  |
| 963    | No file              | `ed564a62f8ec`  |
| 955    | No file              | `ed564a62f8ec`  |
| 946    | No file              | `ed564a62f8ec`  |
| 938    | No file              | `ed564a62f8ec`  |
| 927    | No file              | `ed564a62f8ec`  |
| 911    | No file              | `ed564a62f8ec`  |
| 904    | No file              | `ed564a62f8ec`  |
| 899    | No file              | `ed564a62f8ec`  |
| 894    | No file              | `ed564a62f8ec`  |
| 885    | No file              | `ed564a62f8ec`  |
| 879    | No file              | `ed564a62f8ec`  |
| 872    | No file              | `ed564a62f8ec`  |
| 864    | No file              | `ed564a62f8ec`  |
| 855    | No file              | `ed564a62f8ec`  |
| 853    | No file              | `ed564a62f8ec`  |
| 845    | No file              | `ed564a62f8ec`  |
| 837    | No file              | `ed564a62f8ec`  |
| 829    | No file              | `ed564a62f8ec`  |
| 822    | No file              | `ed564a62f8ec`  |
| 814    | No file              | `ed564a62f8ec`  |
| 805    | No file              | `ed564a62f8ec`  |
| 794    | No file              | `ed564a62f8ec`  |
| 787    | No file              | `ed564a62f8ec`  |
| 780    | No file              | `ed564a62f8ec`  |
| 771    | No file              | `ed564a62f8ec`  |
| 760    | No file              | `ed564a62f8ec`  |
| 748    | No file              | `ed564a62f8ec`  |
| 741    | No file              | `ed564a62f8ec`  |
| 736    | No file              | `ed564a62f8ec`  |
| 731    | No file              | `ed564a62f8ec`  |
| 723    | No file              | `ed564a62f8ec`  |
| 711    | No file              | `ed564a62f8ec`  |
| 707    | No file              | `ed564a62f8ec`  |
| 697    | No file              | `ed564a62f8ec`  |
| 689    | No file              | `ed564a62f8ec`  |
| 683    | No file              | `ed564a62f8ec`  |
| 678    | No file              | `ed564a62f8ec`  |
| 670    | No file              | `ed564a62f8ec`  |
| 661    | No file              | `ed564a62f8ec`  |
| 656    | No file              | `ed564a62f8ec`  |
| 652    | No file              | `ed564a62f8ec`  |
| 643    | No file              | `ed564a62f8ec`  |
| 637    | No file              | `ed564a62f8ec`  |
| 630    | No file              | `ed564a62f8ec`  |
| 627    | No file              | `ed564a62f8ec`  |
| 621    | No file              | `ed564a62f8ec`  |
| 617    | No file              | `ed564a62f8ec`  |
| 615    | No file              | `ed564a62f8ec`  |
| 606    | No file              | `ed564a62f8ec`  |
| 599    | No file              | `ed564a62f8ec`  |
| 592    | No file              | `ed564a62f8ec`  |
| 586    | No file              | `ed564a62f8ec`  |
| 577    | No file              | `ed564a62f8ec`  |
| 569    | No file              | `ed564a62f8ec`  |
| 561    | No file              | `ed564a62f8ec`  |
| 554    | No file              | `ed564a62f8ec`  |
| 542    | No file              | `ed564a62f8ec`  |
| 532    | No file              | `ed564a62f8ec`  |
| 531    | No file              | `ed564a62f8ec`  |
| 526    | No file              | `ed564a62f8ec`  |
| 521    | No file              | `ed564a62f8ec`  |
| 517    | No file              | `ed564a62f8ec`  |
| 510    | No file              | `ed564a62f8ec`  |
| 508    | No file              | `ed564a62f8ec`  |
| 504    | No file              | `ed564a62f8ec`  |
| 497    | No file              | `ed564a62f8ec`  |
| 491    | No file              | `ed564a62f8ec`  |
| 485    | No file              | `ed564a62f8ec`  |
| 478    | No file              | `ed564a62f8ec`  |
| 472    | No file              | `ed564a62f8ec`  |
| 466    | No file              | `ed564a62f8ec`  |
| 457    | No file              | `ed564a62f8ec`  |
| 452    | No file              | `ed564a62f8ec`  |
| 449    | No file              | `ed564a62f8ec`  |
| 435    | No file              | `ed564a62f8ec`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                                   |
| ------------------------ | -------- | ---------------------------------------------------------------------- |
| `skillfusionoffset.dbss` | Optional | `skill_fusion_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`    | Optional | Skill names, LOC type `10`, `str_id1 = skill_no`                        |

The skills are rows of [`skill.dbss`](skill_dbss.md); the handler links each
skill number to it.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 192 x 24 = 4,612 bytes.

### Row (24 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | skill_fusion_key     | The enhanced skill, a skill key `skill_no << 16 \| level`; the row key    |
| `+0x04` | u32  | skill_fusion_key_dup | Equal to `skill_fusion_key` on every row; the offset index points here    |
| `+0x08` | u32  | main_skill_key       | The main skill, a skill key                                               |
| `+0x0C` | u32  | sub_skill_key        | The sub skill, a skill key                                                |
| `+0x10` | u32  | slot_no              | Enhancement slot, `0` to `2`                                              |
| `+0x14` | u32  | order_no             | Position among the choices with the same main skill, `0` or `1`           |

The level half of all three skill keys is `1` on every row of clients
1784 and 3474. The rows are in no key order.

### `skillfusionoffset.dbss`

Bare offset table into `skillfusion.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `skillfusion.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (12 bytes)

| Offset  | Type | Field            | Notes                                        |
| ------- | ---- | ---------------- | -------------------------------------------- |
| `+0x00` | u32  | skill_fusion_key | Key of the row it points at                  |
| `+0x04` | u32  | data_offset      | Row start + 4, at `skill_fusion_key_dup`     |
| `+0x08` | u32  | data_size        | `20` on every row: the row less its key      |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

## Field Names

The `SkillFusion` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `SkillFusionKey`, `MainSkillNo`, `SubSkillNo`,
`SlotNo`, `OrderNo` and `ContentsGroup`. The file stores the three skill
numbers as level 1 skill keys; the table compares the skill number half.
`ContentsGroup` (`947` for the Warrior rows) is not in the client file.
The 2016 client's debug symbols have no struct for the table.

| Field            | Column           | Same value (client 1784) | Same value (client 3474) |
| ---------------- | ---------------- | ------------------------ | ------------------------ |
| skill_fusion_key | `SkillFusionKey` | 138 of 138               | 138 of 192               |
| main_skill_key   | `MainSkillNo`    | 138 of 138               | 138 of 138               |
| sub_skill_key    | `SubSkillNo`     | 138 of 138               | 137 of 138               |
| slot_no          | `SlotNo`         | 138 of 138               | 138 of 138               |
| order_no         | `OrderNo`        | 138 of 138               | 138 of 138               |

Client 3474 adds 54 rows, and enhanced skill `3981` takes sub skill `3379`
where client 1784 has `3436`.

## Notes

- On client 3474 each slot has 64 rows. 88 main skills have two rows
  (`order_no` `0` and `1`); 4 (`789`, `855`, `898`, `984`) have four rows
  in one slot, each `order_no` twice.
- `ToClient_requestLearnFusionSkill(fusionSkillNo, mainSkillNo,
  subSkillNo)` learns a row. The panel disables a row's Learn button while
  the main or the sub skill is not learned, once the enhanced skill is
  learned, or while `ToClient_isUsedSkillForFusionSkill(mainSkillNo)`
  holds.
- The panel's tip `PANEL_COMBINATIONSKILL_TIP` reads "※ Enhanced Skills can
  keep the Main Skill's key commands."
