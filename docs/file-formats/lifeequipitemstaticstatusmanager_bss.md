# `lifeequipitemstaticstatusmanager.bss` Format

## Purpose

The [`buff.dbss`](buff_dbss.md) effect types of each Life Skill tab: list
`n` is `__ePlayerLifeStatType` `n` and holds the effect types that belong
to that life skill. Every tab lists life EXP gain (`25`), display buffs
(`58`), Life EXP (`80`) and Life Skill mastery (`149`), and each tab adds
the effects of its own skill: Gathering Item Drop Rate (`107`) for
Gathering, Auto-fishing Time (`121`), Fish grade chance (`126`) and Prize
Catch Fish Rate (`200`) for Fishing, Sailor EXP (`19`) and Weather
resistance (`128`) for Sailing. Lists `10` to `14` are empty.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                   | Bytes | Records           | Row bytes             |
| ------ | -------------- | -------------------------------------- | ----- | ----------------- | --------------------- |
| 1      | 3435 and later | `lifeequipitemstaticstatusmanager.bss` | 128   | 15 Life Stat List | 4 to 12, 7 on average |

| Layout | File                                   | Known          | Unknown    |
| ------ | -------------------------------------- | -------------- | ---------- |
| 1      | `lifeequipitemstaticstatusmanager.bss` | 128 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d01df9fa181c`  |
| 3482   | Layout 1 | `d01df9fa181c`  |
| 3474   | Layout 1 | `d01df9fa181c`  |
| 3473   | Layout 1 | `d01df9fa181c`  |
| 3464   | Layout 1 | `d01df9fa181c`  |
| 3458   | Layout 1 | `d01df9fa181c`  |
| 3454   | Layout 1 | `d01df9fa181c`  |
| 3444   | Layout 1 | `d01df9fa181c`  |
| 3435   | Layout 1 | `d01df9fa181c`  |
| 3426   | No file  | `d01df9fa181c`  |
| 3418   | No file  | `d01df9fa181c`  |
| 3412   | No file  | `d01df9fa181c`  |
| 3402   | No file  | `d01df9fa181c`  |
| 3396   | No file  | `d01df9fa181c`  |
| 3387   | No file  | `d01df9fa181c`  |
| 3381   | No file  | `d01df9fa181c`  |
| 3373   | No file  | `d01df9fa181c`  |
| 3364   | No file  | `d01df9fa181c`  |
| 3356   | No file  | `d01df9fa181c`  |
| 3349   | No file  | `d01df9fa181c`  |
| 3342   | No file  | `d01df9fa181c`  |
| 3335   | No file  | `d01df9fa181c`  |
| 3326   | No file  | `d01df9fa181c`  |
| 3321   | No file  | `d01df9fa181c`  |
| 3314   | No file  | `d01df9fa181c`  |
| 3303   | No file  | `d01df9fa181c`  |
| 3302   | No file  | `d01df9fa181c`  |
| 3293   | No file  | `d01df9fa181c`  |
| 3283   | No file  | `d01df9fa181c`  |
| 3275   | No file  | `d01df9fa181c`  |
| 3267   | No file  | `d01df9fa181c`  |
| 3258   | No file  | `d01df9fa181c`  |
| 3251   | No file  | `d01df9fa181c`  |
| 3242   | No file  | `d01df9fa181c`  |
| 3235   | No file  | `d01df9fa181c`  |
| 3229   | No file  | `d01df9fa181c`  |
| 3212   | No file  | `d01df9fa181c`  |
| 3203   | No file  | `d01df9fa181c`  |
| 3193   | No file  | `d01df9fa181c`  |
| 3186   | No file  | `d01df9fa181c`  |
| 3177   | No file  | `d01df9fa181c`  |
| 3169   | No file  | `d01df9fa181c`  |
| 3158   | No file  | `d01df9fa181c`  |
| 3151   | No file  | `d01df9fa181c`  |
| 3144   | No file  | `d01df9fa181c`  |
| 3133   | No file  | `d01df9fa181c`  |
| 3125   | No file  | `d01df9fa181c`  |
| 3118   | No file  | `d01df9fa181c`  |
| 3111   | No file  | `d01df9fa181c`  |
| 3103   | No file  | `d01df9fa181c`  |
| 3095   | No file  | `d01df9fa181c`  |
| 3086   | No file  | `d01df9fa181c`  |
| 3072   | No file  | `d01df9fa181c`  |
| 3062   | No file  | `d01df9fa181c`  |
| 3052   | No file  | `d01df9fa181c`  |
| 3045   | No file  | `d01df9fa181c`  |
| 3037   | No file  | `d01df9fa181c`  |
| 3030   | No file  | `d01df9fa181c`  |
| 3021   | No file  | `d01df9fa181c`  |
| 3012   | No file  | `d01df9fa181c`  |
| 3002   | No file  | `d01df9fa181c`  |
| 2995   | No file  | `d01df9fa181c`  |
| 2987   | No file  | `d01df9fa181c`  |
| 2978   | No file  | `d01df9fa181c`  |
| 2970   | No file  | `d01df9fa181c`  |
| 2959   | No file  | `d01df9fa181c`  |
| 2951   | No file  | `d01df9fa181c`  |
| 2942   | No file  | `d01df9fa181c`  |
| 2935   | No file  | `d01df9fa181c`  |
| 2932   | No file  | `d01df9fa181c`  |
| 2923   | No file  | `d01df9fa181c`  |
| 2919   | No file  | `d01df9fa181c`  |
| 2907   | No file  | `d01df9fa181c`  |
| 2900   | No file  | `d01df9fa181c`  |
| 2891   | No file  | `d01df9fa181c`  |
| 2882   | No file  | `d01df9fa181c`  |
| 2872   | No file  | `d01df9fa181c`  |
| 2863   | No file  | `d01df9fa181c`  |
| 2855   | No file  | `d01df9fa181c`  |
| 2849   | No file  | `d01df9fa181c`  |
| 2844   | No file  | `d01df9fa181c`  |
| 2834   | No file  | `d01df9fa181c`  |
| 2825   | No file  | `d01df9fa181c`  |
| 2819   | No file  | `d01df9fa181c`  |
| 2811   | No file  | `d01df9fa181c`  |
| 2803   | No file  | `d01df9fa181c`  |
| 2794   | No file  | `d01df9fa181c`  |
| 2783   | No file  | `d01df9fa181c`  |
| 2774   | No file  | `d01df9fa181c`  |
| 2765   | No file  | `d01df9fa181c`  |
| 2756   | No file  | `d01df9fa181c`  |
| 2750   | No file  | `d01df9fa181c`  |
| 2743   | No file  | `d01df9fa181c`  |
| 2736   | No file  | `d01df9fa181c`  |
| 2726   | No file  | `d01df9fa181c`  |
| 2717   | No file  | `d01df9fa181c`  |
| 2709   | No file  | `d01df9fa181c`  |
| 2703   | No file  | `d01df9fa181c`  |
| 2695   | No file  | `d01df9fa181c`  |
| 2684   | No file  | `d01df9fa181c`  |
| 2672   | No file  | `d01df9fa181c`  |
| 2665   | No file  | `d01df9fa181c`  |
| 2657   | No file  | `d01df9fa181c`  |
| 2649   | No file  | `d01df9fa181c`  |
| 2644   | No file  | `d01df9fa181c`  |
| 2637   | No file  | `d01df9fa181c`  |
| 2629   | No file  | `d01df9fa181c`  |
| 2619   | No file  | `d01df9fa181c`  |
| 2612   | No file  | `d01df9fa181c`  |
| 2606   | No file  | `d01df9fa181c`  |
| 2602   | No file  | `d01df9fa181c`  |
| 2601   | No file  | `d01df9fa181c`  |
| 2592   | No file  | `d01df9fa181c`  |
| 2583   | No file  | `d01df9fa181c`  |
| 2575   | No file  | `d01df9fa181c`  |
| 2567   | No file  | `d01df9fa181c`  |
| 2560   | No file  | `d01df9fa181c`  |
| 2553   | No file  | `d01df9fa181c`  |
| 2545   | No file  | `d01df9fa181c`  |
| 2538   | No file  | `d01df9fa181c`  |
| 2529   | No file  | `d01df9fa181c`  |
| 2519   | No file  | `d01df9fa181c`  |
| 2513   | No file  | `d01df9fa181c`  |
| 2510   | No file  | `d01df9fa181c`  |
| 2507   | No file  | `d01df9fa181c`  |
| 2503   | No file  | `d01df9fa181c`  |
| 2498   | No file  | `d01df9fa181c`  |
| 2492   | No file  | `d01df9fa181c`  |
| 2487   | No file  | `d01df9fa181c`  |
| 2480   | No file  | `d01df9fa181c`  |
| 2474   | No file  | `d01df9fa181c`  |
| 2468   | No file  | `d01df9fa181c`  |
| 2460   | No file  | `d01df9fa181c`  |
| 2453   | No file  | `d01df9fa181c`  |
| 2444   | No file  | `d01df9fa181c`  |
| 2438   | No file  | `d01df9fa181c`  |
| 2434   | No file  | `d01df9fa181c`  |
| 2429   | No file  | `d01df9fa181c`  |
| 2421   | No file  | `d01df9fa181c`  |
| 2414   | No file  | `d01df9fa181c`  |
| 2407   | No file  | `d01df9fa181c`  |
| 2401   | No file  | `d01df9fa181c`  |
| 2397   | No file  | `d01df9fa181c`  |
| 2393   | No file  | `d01df9fa181c`  |
| 2384   | No file  | `d01df9fa181c`  |
| 2378   | No file  | `d01df9fa181c`  |
| 2372   | No file  | `d01df9fa181c`  |
| 2358   | No file  | `d01df9fa181c`  |
| 2352   | No file  | `d01df9fa181c`  |
| 2347   | No file  | `d01df9fa181c`  |
| 2343   | No file  | `d01df9fa181c`  |
| 2335   | No file  | `d01df9fa181c`  |
| 2327   | No file  | `d01df9fa181c`  |
| 2324   | No file  | `d01df9fa181c`  |
| 2319   | No file  | `d01df9fa181c`  |
| 2313   | No file  | `d01df9fa181c`  |
| 2308   | No file  | `d01df9fa181c`  |
| 2302   | No file  | `d01df9fa181c`  |
| 2295   | No file  | `d01df9fa181c`  |
| 2290   | No file  | `d01df9fa181c`  |
| 2284   | No file  | `d01df9fa181c`  |
| 2276   | No file  | `d01df9fa181c`  |
| 2269   | No file  | `d01df9fa181c`  |
| 2259   | No file  | `d01df9fa181c`  |
| 2250   | No file  | `d01df9fa181c`  |
| 2243   | No file  | `d01df9fa181c`  |
| 2235   | No file  | `d01df9fa181c`  |
| 2229   | No file  | `d01df9fa181c`  |
| 2224   | No file  | `d01df9fa181c`  |
| 2218   | No file  | `d01df9fa181c`  |
| 2215   | No file  | `d01df9fa181c`  |
| 2207   | No file  | `d01df9fa181c`  |
| 2203   | No file  | `d01df9fa181c`  |
| 2196   | No file  | `d01df9fa181c`  |
| 2192   | No file  | `d01df9fa181c`  |
| 2189   | No file  | `d01df9fa181c`  |
| 2183   | No file  | `d01df9fa181c`  |
| 2179   | No file  | `d01df9fa181c`  |
| 2171   | No file  | `d01df9fa181c`  |
| 2163   | No file  | `d01df9fa181c`  |
| 2156   | No file  | `d01df9fa181c`  |
| 2151   | No file  | `d01df9fa181c`  |
| 2147   | No file  | `d01df9fa181c`  |
| 2142   | No file  | `d01df9fa181c`  |
| 2138   | No file  | `d01df9fa181c`  |
| 2134   | No file  | `d01df9fa181c`  |
| 2130   | No file  | `d01df9fa181c`  |
| 2122   | No file  | `d01df9fa181c`  |
| 2107   | No file  | `d01df9fa181c`  |
| 2098   | No file  | `d01df9fa181c`  |
| 2089   | No file  | `d01df9fa181c`  |
| 2081   | No file  | `d01df9fa181c`  |
| 2073   | No file  | `d01df9fa181c`  |
| 2067   | No file  | `d01df9fa181c`  |
| 2063   | No file  | `d01df9fa181c`  |
| 2059   | No file  | `d01df9fa181c`  |
| 2052   | No file  | `d01df9fa181c`  |
| 2044   | No file  | `d01df9fa181c`  |
| 2039   | No file  | `d01df9fa181c`  |
| 2032   | No file  | `d01df9fa181c`  |
| 2025   | No file  | `d01df9fa181c`  |
| 2011   | No file  | `d01df9fa181c`  |
| 2005   | No file  | `d01df9fa181c`  |
| 2000   | No file  | `d01df9fa181c`  |
| 1996   | No file  | `d01df9fa181c`  |
| 1991   | No file  | `d01df9fa181c`  |
| 1985   | No file  | `d01df9fa181c`  |
| 1980   | No file  | `d01df9fa181c`  |
| 1969   | No file  | `d01df9fa181c`  |
| 1964   | No file  | `d01df9fa181c`  |
| 1958   | No file  | `d01df9fa181c`  |
| 1950   | No file  | `d01df9fa181c`  |
| 1945   | No file  | `d01df9fa181c`  |
| 1937   | No file  | `d01df9fa181c`  |
| 1933   | No file  | `d01df9fa181c`  |
| 1927   | No file  | `d01df9fa181c`  |
| 1921   | No file  | `d01df9fa181c`  |
| 1914   | No file  | `d01df9fa181c`  |
| 1908   | No file  | `d01df9fa181c`  |
| 1897   | No file  | `d01df9fa181c`  |
| 1892   | No file  | `d01df9fa181c`  |
| 1886   | No file  | `d01df9fa181c`  |
| 1881   | No file  | `d01df9fa181c`  |
| 1871   | No file  | `d01df9fa181c`  |
| 1866   | No file  | `d01df9fa181c`  |
| 1862   | No file  | `d01df9fa181c`  |
| 1854   | No file  | `d01df9fa181c`  |
| 1846   | No file  | `d01df9fa181c`  |
| 1838   | No file  | `d01df9fa181c`  |
| 1832   | No file  | `d01df9fa181c`  |
| 1826   | No file  | `d01df9fa181c`  |
| 1822   | No file  | `d01df9fa181c`  |
| 1818   | No file  | `d01df9fa181c`  |
| 1804   | No file  | `d01df9fa181c`  |
| 1794   | No file  | `d01df9fa181c`  |
| 1790   | No file  | `d01df9fa181c`  |
| 1784   | No file  | `d01df9fa181c`  |
| 1774   | No file  | `d01df9fa181c`  |
| 1771   | No file  | `d01df9fa181c`  |
| 1762   | No file  | `d01df9fa181c`  |
| 1759   | No file  | `d01df9fa181c`  |
| 1754   | No file  | `d01df9fa181c`  |
| 1749   | No file  | `d01df9fa181c`  |
| 1743   | No file  | `d01df9fa181c`  |
| 1737   | No file  | `d01df9fa181c`  |
| 1731   | No file  | `d01df9fa181c`  |
| 1725   | No file  | `d01df9fa181c`  |
| 1717   | No file  | `d01df9fa181c`  |
| 1710   | No file  | `d01df9fa181c`  |
| 1704   | No file  | `d01df9fa181c`  |
| 1698   | No file  | `d01df9fa181c`  |
| 1690   | No file  | `d01df9fa181c`  |
| 1685   | No file  | `d01df9fa181c`  |
| 1680   | No file  | `d01df9fa181c`  |
| 1674   | No file  | `d01df9fa181c`  |
| 1668   | No file  | `d01df9fa181c`  |
| 1659   | No file  | `d01df9fa181c`  |
| 1649   | No file  | `d01df9fa181c`  |
| 1642   | No file  | `d01df9fa181c`  |
| 1636   | No file  | `d01df9fa181c`  |
| 1628   | No file  | `d01df9fa181c`  |
| 1622   | No file  | `d01df9fa181c`  |
| 1614   | No file  | `d01df9fa181c`  |
| 1608   | No file  | `d01df9fa181c`  |
| 1602   | No file  | `d01df9fa181c`  |
| 1598   | No file  | `d01df9fa181c`  |
| 1594   | No file  | `d01df9fa181c`  |
| 1590   | No file  | `d01df9fa181c`  |
| 1587   | No file  | `d01df9fa181c`  |
| 1584   | No file  | `d01df9fa181c`  |
| 1579   | No file  | `d01df9fa181c`  |
| 1572   | No file  | `d01df9fa181c`  |
| 1565   | No file  | `d01df9fa181c`  |
| 1559   | No file  | `d01df9fa181c`  |
| 1554   | No file  | `d01df9fa181c`  |
| 1547   | No file  | `d01df9fa181c`  |
| 1537   | No file  | `d01df9fa181c`  |
| 1529   | No file  | `d01df9fa181c`  |
| 1524   | No file  | `d01df9fa181c`  |
| 1519   | No file  | `d01df9fa181c`  |
| 1509   | No file  | `d01df9fa181c`  |
| 1506   | No file  | `d01df9fa181c`  |
| 1504   | No file  | `d01df9fa181c`  |
| 1500   | No file  | `d01df9fa181c`  |
| 1493   | No file  | `d01df9fa181c`  |
| 1489   | No file  | `d01df9fa181c`  |
| 1485   | No file  | `d01df9fa181c`  |
| 1481   | No file  | `d01df9fa181c`  |
| 1474   | No file  | `d01df9fa181c`  |
| 1466   | No file  | `d01df9fa181c`  |
| 1462   | No file  | `d01df9fa181c`  |
| 1459   | No file  | `d01df9fa181c`  |
| 1453   | No file  | `d01df9fa181c`  |
| 1450   | No file  | `d01df9fa181c`  |
| 1445   | No file  | `d01df9fa181c`  |
| 1439   | No file  | `d01df9fa181c`  |
| 1433   | No file  | `d01df9fa181c`  |
| 1430   | No file  | `d01df9fa181c`  |
| 1426   | No file  | `d01df9fa181c`  |
| 1421   | No file  | `d01df9fa181c`  |
| 1417   | No file  | `d01df9fa181c`  |
| 1416   | No file  | `d01df9fa181c`  |
| 1409   | No file  | `d01df9fa181c`  |
| 1405   | No file  | `d01df9fa181c`  |
| 1401   | No file  | `d01df9fa181c`  |
| 1396   | No file  | `d01df9fa181c`  |
| 1391   | No file  | `d01df9fa181c`  |
| 1390   | No file  | `d01df9fa181c`  |
| 1386   | No file  | `d01df9fa181c`  |
| 1381   | No file  | `d01df9fa181c`  |
| 1379   | No file  | `d01df9fa181c`  |
| 1372   | No file  | `d01df9fa181c`  |
| 1366   | No file  | `d01df9fa181c`  |
| 1364   | No file  | `d01df9fa181c`  |
| 1363   | No file  | `d01df9fa181c`  |
| 1360   | No file  | `d01df9fa181c`  |
| 1358   | No file  | `d01df9fa181c`  |
| 1355   | No file  | `d01df9fa181c`  |
| 1351   | No file  | `d01df9fa181c`  |
| 1348   | No file  | `d01df9fa181c`  |
| 1346   | No file  | `d01df9fa181c`  |
| 1341   | No file  | `d01df9fa181c`  |
| 1340   | No file  | `d01df9fa181c`  |
| 1338   | No file  | `d01df9fa181c`  |
| 1335   | No file  | `d01df9fa181c`  |
| 1333   | No file  | `d01df9fa181c`  |
| 1329   | No file  | `d01df9fa181c`  |
| 1327   | No file  | `d01df9fa181c`  |
| 1324   | No file  | `d01df9fa181c`  |
| 1321   | No file  | `d01df9fa181c`  |
| 1319   | No file  | `d01df9fa181c`  |
| 1318   | No file  | `d01df9fa181c`  |
| 1316   | No file  | `d01df9fa181c`  |
| 1313   | No file  | `d01df9fa181c`  |
| 1311   | No file  | `d01df9fa181c`  |
| 1309   | No file  | `d01df9fa181c`  |
| 1304   | No file  | `d01df9fa181c`  |
| 1292   | No file  | `d01df9fa181c`  |
| 1286   | No file  | `d01df9fa181c`  |
| 1280   | No file  | `d01df9fa181c`  |
| 1276   | No file  | `d01df9fa181c`  |
| 1267   | No file  | `d01df9fa181c`  |
| 1261   | No file  | `d01df9fa181c`  |
| 1256   | No file  | `d01df9fa181c`  |
| 1250   | No file  | `d01df9fa181c`  |
| 1246   | No file  | `d01df9fa181c`  |
| 1239   | No file  | `d01df9fa181c`  |
| 1230   | No file  | `d01df9fa181c`  |
| 1226   | No file  | `d01df9fa181c`  |
| 1220   | No file  | `d01df9fa181c`  |
| 1217   | No file  | `d01df9fa181c`  |
| 1211   | No file  | `d01df9fa181c`  |
| 1210   | No file  | `d01df9fa181c`  |
| 1208   | No file  | `d01df9fa181c`  |
| 1203   | No file  | `d01df9fa181c`  |
| 1197   | No file  | `d01df9fa181c`  |
| 1194   | No file  | `d01df9fa181c`  |
| 1192   | No file  | `d01df9fa181c`  |
| 1187   | No file  | `d01df9fa181c`  |
| 1183   | No file  | `d01df9fa181c`  |
| 1177   | No file  | `d01df9fa181c`  |
| 1173   | No file  | `d01df9fa181c`  |
| 1167   | No file  | `d01df9fa181c`  |
| 1164   | No file  | `d01df9fa181c`  |
| 1156   | No file  | `d01df9fa181c`  |
| 1149   | No file  | `d01df9fa181c`  |
| 1144   | No file  | `d01df9fa181c`  |
| 1137   | No file  | `d01df9fa181c`  |
| 1132   | No file  | `d01df9fa181c`  |
| 1127   | No file  | `d01df9fa181c`  |
| 1122   | No file  | `d01df9fa181c`  |
| 1118   | No file  | `d01df9fa181c`  |
| 1114   | No file  | `d01df9fa181c`  |
| 1109   | No file  | `d01df9fa181c`  |
| 1102   | No file  | `d01df9fa181c`  |
| 1096   | No file  | `d01df9fa181c`  |
| 1088   | No file  | `d01df9fa181c`  |
| 1081   | No file  | `d01df9fa181c`  |
| 1076   | No file  | `d01df9fa181c`  |
| 1069   | No file  | `d01df9fa181c`  |
| 1064   | No file  | `d01df9fa181c`  |
| 1058   | No file  | `d01df9fa181c`  |
| 1051   | No file  | `d01df9fa181c`  |
| 1044   | No file  | `d01df9fa181c`  |
| 1036   | No file  | `d01df9fa181c`  |
| 1026   | No file  | `d01df9fa181c`  |
| 1016   | No file  | `d01df9fa181c`  |
| 1009   | No file  | `d01df9fa181c`  |
| 1005   | No file  | `d01df9fa181c`  |
| 1000   | No file  | `d01df9fa181c`  |
| 998    | No file  | `d01df9fa181c`  |
| 990    | No file  | `d01df9fa181c`  |
| 979    | No file  | `d01df9fa181c`  |
| 972    | No file  | `d01df9fa181c`  |
| 963    | No file  | `d01df9fa181c`  |
| 955    | No file  | `d01df9fa181c`  |
| 946    | No file  | `d01df9fa181c`  |
| 938    | No file  | `d01df9fa181c`  |
| 927    | No file  | `d01df9fa181c`  |
| 911    | No file  | `d01df9fa181c`  |
| 904    | No file  | `d01df9fa181c`  |
| 899    | No file  | `d01df9fa181c`  |
| 894    | No file  | `d01df9fa181c`  |
| 885    | No file  | `d01df9fa181c`  |
| 879    | No file  | `d01df9fa181c`  |
| 872    | No file  | `d01df9fa181c`  |
| 864    | No file  | `d01df9fa181c`  |
| 855    | No file  | `d01df9fa181c`  |
| 853    | No file  | `d01df9fa181c`  |
| 845    | No file  | `d01df9fa181c`  |
| 837    | No file  | `d01df9fa181c`  |
| 829    | No file  | `d01df9fa181c`  |
| 822    | No file  | `d01df9fa181c`  |
| 814    | No file  | `d01df9fa181c`  |
| 805    | No file  | `d01df9fa181c`  |
| 794    | No file  | `d01df9fa181c`  |
| 787    | No file  | `d01df9fa181c`  |
| 780    | No file  | `d01df9fa181c`  |
| 771    | No file  | `d01df9fa181c`  |
| 760    | No file  | `d01df9fa181c`  |
| 748    | No file  | `d01df9fa181c`  |
| 741    | No file  | `d01df9fa181c`  |
| 736    | No file  | `d01df9fa181c`  |
| 731    | No file  | `d01df9fa181c`  |
| 723    | No file  | `d01df9fa181c`  |
| 711    | No file  | `d01df9fa181c`  |
| 707    | No file  | `d01df9fa181c`  |
| 697    | No file  | `d01df9fa181c`  |
| 689    | No file  | `d01df9fa181c`  |
| 683    | No file  | `d01df9fa181c`  |
| 678    | No file  | `d01df9fa181c`  |
| 670    | No file  | `d01df9fa181c`  |
| 661    | No file  | `d01df9fa181c`  |
| 656    | No file  | `d01df9fa181c`  |
| 652    | No file  | `d01df9fa181c`  |
| 643    | No file  | `d01df9fa181c`  |
| 637    | No file  | `d01df9fa181c`  |
| 630    | No file  | `d01df9fa181c`  |
| 627    | No file  | `d01df9fa181c`  |
| 621    | No file  | `d01df9fa181c`  |
| 617    | No file  | `d01df9fa181c`  |
| 615    | No file  | `d01df9fa181c`  |
| 606    | No file  | `d01df9fa181c`  |
| 599    | No file  | `d01df9fa181c`  |
| 592    | No file  | `d01df9fa181c`  |
| 586    | No file  | `d01df9fa181c`  |
| 577    | No file  | `d01df9fa181c`  |
| 569    | No file  | `d01df9fa181c`  |
| 561    | No file  | `d01df9fa181c`  |
| 554    | No file  | `d01df9fa181c`  |
| 542    | No file  | `d01df9fa181c`  |
| 532    | No file  | `d01df9fa181c`  |
| 531    | No file  | `d01df9fa181c`  |
| 526    | No file  | `d01df9fa181c`  |
| 521    | No file  | `d01df9fa181c`  |
| 517    | No file  | `d01df9fa181c`  |
| 510    | No file  | `d01df9fa181c`  |
| 508    | No file  | `d01df9fa181c`  |
| 504    | No file  | `d01df9fa181c`  |
| 497    | No file  | `d01df9fa181c`  |
| 491    | No file  | `d01df9fa181c`  |
| 485    | No file  | `d01df9fa181c`  |
| 478    | No file  | `d01df9fa181c`  |
| 472    | No file  | `d01df9fa181c`  |
| 466    | No file  | `d01df9fa181c`  |
| 457    | No file  | `d01df9fa181c`  |
| 452    | No file  | `d01df9fa181c`  |
| 449    | No file  | `d01df9fa181c`  |
| 435    | No file  | `d01df9fa181c`  |

<!-- versions:end -->

## Companion Files

None. The handler names each life skill from the GAME sheet of
`stringtable.bss` and `languagedata_*.loc` when they are loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                  | Type                          | Field           | Notes                                                       |
| ----------------------- | ----------------------------- | --------------- | ----------------------------------------------------------- |
| `+0x00`                 | char[4]                       | magic           | ASCII `PABR`                                                |
| `+0x04`                 | Life Stat List[..table_start] | life_stat_lists | No count: list `n` is `__ePlayerLifeStatType` `n`; 15 lists on client 3482 |
| `life_stat_lists+0x00`  | String Table                  | string_table    | See String Table                                            |
| `EOF-0x08`              | u32                           | table_start     | Offset of the string table, where `life_stat_lists` ends    |
| `EOF-0x04`              | u32                           | zero            | Always `0`                                                  |

### Life Stat List (variable: 4 bytes + effect types)

| Offset  | Type                   | Field             | Notes                                          |
| ------- | ---------------------- | ----------------- | ---------------------------------------------- |
| `+0x00` | u32                    | effect_type_count | Number of effect types; `0` on lists `10` to `14` (client 3482) |
| `+0x04` | u8[effect_type_count]  | effect_types      | `buff.dbss` effect types, in ascending order   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Lists

Client 3482, with the life skill of each list (the Life Skill tab order of
`panel_window_equipment_all_4.luac`, `_lifeSlotPerType`) and the
[`buff.dbss`](buff_dbss.md) Enum Values names of the effect types:

| List | Life skill  | `effect_types`                                         |
| ---- | ----------- | ------------------------------------------------------ |
| 0    | Gathering   | `25`, `58`, `67`, `80`, `107`, `149`                   |
| 1    | Fishing     | `25`, `58`, `67`, `80`, `121`, `126`, `149`, `200`     |
| 2    | Hunting     | `25`, `58`, `80`, `149`                                |
| 3    | Cooking     | `25`, `58`, `80`, `111`, `149`                         |
| 4    | Alchemy     | `25`, `58`, `80`, `111`, `149`                         |
| 5    | Processing  | `25`, `58`, `80`, `111`, `149`                         |
| 6    | Training    | `25`, `50`, `58`, `80`, `149`                          |
| 7    | Trading     | `25`, `58`, `80`, `149`                                |
| 8    | Farming     | `25`, `58`, `80`, `149`                                |
| 9    | Sailing     | `19`, `25`, `58`, `80`, `128`, `149`                   |
| 10 to 14 | none    | Empty                                                  |

| Effect type | `buff.dbss` meaning                                      | Lists          |
| ----------- | -------------------------------------------------------- | -------------- |
| `19`        | Sailor EXP                                               | 9              |
| `25`        | Combat, skill and life EXP gain                          | 0 to 9         |
| `50`        | Mount EXP                                                | 6              |
| `58`        | Display buff (title, text and icon)                      | 0 to 9         |
| `67`        | Stat ranks (`5` Fishing Speed, `6` Gathering Speed)      | 0, 1           |
| `80`        | Life-skill EXP                                           | 0 to 9         |
| `107`       | Gathering Item Drop Rate                                 | 0              |
| `111`       | Craft time and success rate (Cooking, Alchemy, Processing) | 3, 4, 5      |
| `121`       | Auto-fishing Time                                        | 1              |
| `126`       | Fish grade chance                                        | 1              |
| `128`       | Weather resistance                                       | 9              |
| `149`       | Life skill mastery                                       | 0 to 9         |
| `200`       | Prize Catch Fish Rate                                    | 1              |

## Field Names

The file is not in client 1784, and no sheet of a private server's
`DataSheets.bexcel` on that client has `LifeEquip` in its name except
`Enchant_LifeEquipment`, an item enchant sheet. `effect_types` names what
the values are: every value is an effect type of `buff.dbss`, and the
effect types each list adds to the four shared ones are the ones of that
list's life skill (`121` and `126` only on the Fishing list, `128` only on
Sailing, `50` only on Training, `111` only on the three crafting lists).
The 15 lists match the `__ePlayerLifeStatType` values `0` to `14`, the
same count as `CppEnums.LifeExperienceType` (`gather` `0` to `temp4`
`14`); `itemenchant.dbss` stores `15` (`__ePlayerLifeStatType_Count`) as
"any tab".

## Notes

- `lifeequipitemstaticstatusmanager.bss` has its own handler
  (`_bss/lifeequipitemstaticstatusmanager/`): one row per effect type of
  a list, with the life skill name and the effect type's module name.
  Empty lists get no row.

## Open Questions

### What the Client Does With the Lists

No client Lua names the file or a getter for it. The Life Equipment
Status window (`panel_window_lifeequipment_status_1.luac`, client 3482)
lays out its slots per `__ePlayerLifeStatType` from a table of its own.
Whether the client uses the lists to pick which buffs of Life Skill gear
count for a tab (in the gear tooltip or the life stat totals) is not
known.
