# `monstergroup.dbss` Format

## Purpose

Monster groups: per group key a list of monster character keys, each with a
`percent` on the 1,000,000 = 100% scale. The groups are hunting zones: on
client 3474, 29 of the 35 groups with members have every member in one
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) hunting ground
(see Notes). The file stores no hunting ground itself; the Hunting Grounds
column shows the zones that list a member (see Hunting Grounds Column).
`monstergroupoffset.dbss` is required to address the variable-length records.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | -------------------------------------- | --------- |
| 1      | 1346 and later | 3483    | `monstergroup.dbss`       | 1,402 | 185 Member, 36 Group Record, 36 Record | 6         |
| 1      | 1346 and later | 3483    | `monstergroupoffset.dbss` | 364   | 36 Offset Row                          | 10        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `monstergroup.dbss`       | 1,402 B (100.0%) | 0 B (0.0%) |
| 1      | `monstergroupoffset.dbss` | 364 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `81757f35219e`  |
| 3482   | Layout 1             | `81757f35219e`  |
| 3474   | Layout 1             | `81757f35219e`  |
| 3473   | Layout 1             | `81757f35219e`  |
| 3464   | Layout 1             | `81757f35219e`  |
| 3458   | Layout 1             | `81757f35219e`  |
| 3454   | Layout 1             | `81757f35219e`  |
| 3444   | Layout 1             | `81757f35219e`  |
| 3435   | Layout 1             | `81757f35219e`  |
| 3426   | Layout 1             | `81757f35219e`  |
| 3418   | Layout 1             | `81757f35219e`  |
| 3412   | Layout 1             | `81757f35219e`  |
| 3402   | Layout 1             | `81757f35219e`  |
| 3396   | Layout 1             | `81757f35219e`  |
| 3387   | Layout 1             | `81757f35219e`  |
| 3381   | Layout 1             | `81757f35219e`  |
| 3373   | Layout 1             | `81757f35219e`  |
| 3364   | Layout 1             | `81757f35219e`  |
| 3356   | Layout 1             | `81757f35219e`  |
| 3349   | Layout 1             | `81757f35219e`  |
| 3342   | Layout 1             | `81757f35219e`  |
| 3335   | Layout 1             | `81757f35219e`  |
| 3326   | Layout 1             | `81757f35219e`  |
| 3321   | Layout 1             | `81757f35219e`  |
| 3314   | Layout 1             | `81757f35219e`  |
| 3303   | Layout 1             | `81757f35219e`  |
| 3302   | Layout 1             | `81757f35219e`  |
| 3293   | Layout 1             | `81757f35219e`  |
| 3283   | Layout 1             | `81757f35219e`  |
| 3275   | Layout 1             | `81757f35219e`  |
| 3267   | Layout 1             | `81757f35219e`  |
| 3258   | Layout 1             | `81757f35219e`  |
| 3251   | Layout 1             | `81757f35219e`  |
| 3242   | Layout 1             | `81757f35219e`  |
| 3235   | Layout 1             | `81757f35219e`  |
| 3229   | Layout 1             | `81757f35219e`  |
| 3212   | Layout 1             | `81757f35219e`  |
| 3203   | Layout 1             | `81757f35219e`  |
| 3193   | Layout 1             | `81757f35219e`  |
| 3186   | Layout 1             | `81757f35219e`  |
| 3177   | Layout 1             | `81757f35219e`  |
| 3169   | Layout 1             | `81757f35219e`  |
| 3158   | Layout 1             | `81757f35219e`  |
| 3151   | Layout 1             | `81757f35219e`  |
| 3144   | Layout 1             | `81757f35219e`  |
| 3133   | Layout 1             | `81757f35219e`  |
| 3125   | Layout 1             | `81757f35219e`  |
| 3118   | Layout 1             | `81757f35219e`  |
| 3111   | Layout 1             | `81757f35219e`  |
| 3103   | Layout 1             | `81757f35219e`  |
| 3095   | Layout 1             | `81757f35219e`  |
| 3086   | Layout 1             | `81757f35219e`  |
| 3072   | Layout 1             | `81757f35219e`  |
| 3062   | Layout 1             | `81757f35219e`  |
| 3052   | Layout 1             | `81757f35219e`  |
| 3045   | Layout 1             | `81757f35219e`  |
| 3037   | Layout 1             | `81757f35219e`  |
| 3030   | Layout 1             | `81757f35219e`  |
| 3021   | Layout 1             | `81757f35219e`  |
| 3012   | Layout 1             | `81757f35219e`  |
| 3002   | Layout 1             | `81757f35219e`  |
| 2995   | Layout 1             | `81757f35219e`  |
| 2987   | Layout 1             | `81757f35219e`  |
| 2978   | Layout 1             | `81757f35219e`  |
| 2970   | Layout 1             | `81757f35219e`  |
| 2959   | Layout 1             | `81757f35219e`  |
| 2951   | Layout 1             | `81757f35219e`  |
| 2942   | Layout 1             | `81757f35219e`  |
| 2935   | Layout 1             | `81757f35219e`  |
| 2932   | Layout 1             | `81757f35219e`  |
| 2923   | Layout 1             | `81757f35219e`  |
| 2919   | Layout 1             | `81757f35219e`  |
| 2907   | Layout 1             | `81757f35219e`  |
| 2900   | Layout 1             | `81757f35219e`  |
| 2891   | Layout 1             | `81757f35219e`  |
| 2882   | Layout 1             | `81757f35219e`  |
| 2872   | Layout 1             | `81757f35219e`  |
| 2863   | Layout 1             | `81757f35219e`  |
| 2855   | Layout 1             | `81757f35219e`  |
| 2849   | Layout 1             | `81757f35219e`  |
| 2844   | Layout 1             | `81757f35219e`  |
| 2834   | Layout 1             | `81757f35219e`  |
| 2825   | Layout 1             | `81757f35219e`  |
| 2819   | Layout 1             | `81757f35219e`  |
| 2811   | Layout 1             | `81757f35219e`  |
| 2803   | Layout 1             | `81757f35219e`  |
| 2794   | Layout 1             | `81757f35219e`  |
| 2783   | Layout 1             | `81757f35219e`  |
| 2774   | Layout 1             | `81757f35219e`  |
| 2765   | Layout 1             | `81757f35219e`  |
| 2756   | Layout 1             | `81757f35219e`  |
| 2750   | Layout 1             | `81757f35219e`  |
| 2743   | Layout 1             | `81757f35219e`  |
| 2736   | Layout 1             | `81757f35219e`  |
| 2726   | Layout 1             | `81757f35219e`  |
| 2717   | Layout 1             | `81757f35219e`  |
| 2709   | Layout 1             | `81757f35219e`  |
| 2703   | Layout 1             | `81757f35219e`  |
| 2695   | Layout 1             | `81757f35219e`  |
| 2684   | Layout 1             | `81757f35219e`  |
| 2672   | Layout 1             | `81757f35219e`  |
| 2665   | Layout 1             | `81757f35219e`  |
| 2657   | Layout 1             | `81757f35219e`  |
| 2649   | Layout 1             | `81757f35219e`  |
| 2644   | Layout 1             | `81757f35219e`  |
| 2637   | Layout 1             | `81757f35219e`  |
| 2629   | Layout 1             | `81757f35219e`  |
| 2619   | Layout 1             | `81757f35219e`  |
| 2612   | Layout 1             | `81757f35219e`  |
| 2606   | Layout 1             | `81757f35219e`  |
| 2602   | Layout 1             | `81757f35219e`  |
| 2601   | Layout 1             | `81757f35219e`  |
| 2592   | Layout 1             | `81757f35219e`  |
| 2583   | Layout 1             | `81757f35219e`  |
| 2575   | Layout 1             | `81757f35219e`  |
| 2567   | Layout 1             | `81757f35219e`  |
| 2560   | Layout 1             | `81757f35219e`  |
| 2553   | Layout 1             | `81757f35219e`  |
| 2545   | Layout 1             | `81757f35219e`  |
| 2538   | Layout 1             | `81757f35219e`  |
| 2529   | Layout 1             | `81757f35219e`  |
| 2519   | Layout 1             | `81757f35219e`  |
| 2513   | Layout 1             | `81757f35219e`  |
| 2510   | Layout 1             | `81757f35219e`  |
| 2507   | Layout 1             | `81757f35219e`  |
| 2503   | Layout 1             | `81757f35219e`  |
| 2498   | Layout 1             | `81757f35219e`  |
| 2492   | Layout 1             | `81757f35219e`  |
| 2487   | Layout 1             | `81757f35219e`  |
| 2480   | Layout 1             | `81757f35219e`  |
| 2474   | Layout 1             | `81757f35219e`  |
| 2468   | Layout 1             | `81757f35219e`  |
| 2460   | Layout 1             | `81757f35219e`  |
| 2453   | Layout 1             | `81757f35219e`  |
| 2444   | Layout 1             | `81757f35219e`  |
| 2438   | Layout 1             | `81757f35219e`  |
| 2434   | Layout 1             | `81757f35219e`  |
| 2429   | Layout 1             | `81757f35219e`  |
| 2421   | Layout 1             | `81757f35219e`  |
| 2414   | Layout 1             | `81757f35219e`  |
| 2407   | Layout 1             | `81757f35219e`  |
| 2401   | Layout 1             | `81757f35219e`  |
| 2397   | Layout 1             | `81757f35219e`  |
| 2393   | Layout 1             | `81757f35219e`  |
| 2384   | Layout 1             | `81757f35219e`  |
| 2378   | Layout 1             | `81757f35219e`  |
| 2372   | Layout 1             | `81757f35219e`  |
| 2358   | Layout 1             | `81757f35219e`  |
| 2352   | Layout 1             | `81757f35219e`  |
| 2347   | Layout 1             | `81757f35219e`  |
| 2343   | Layout 1             | `81757f35219e`  |
| 2335   | Layout 1             | `81757f35219e`  |
| 2327   | Layout 1             | `81757f35219e`  |
| 2324   | Layout 1             | `81757f35219e`  |
| 2319   | Layout 1             | `81757f35219e`  |
| 2313   | Layout 1             | `81757f35219e`  |
| 2308   | Layout 1             | `81757f35219e`  |
| 2302   | Layout 1             | `81757f35219e`  |
| 2295   | Layout 1             | `81757f35219e`  |
| 2290   | Layout 1             | `81757f35219e`  |
| 2284   | Layout 1             | `81757f35219e`  |
| 2276   | Layout 1             | `81757f35219e`  |
| 2269   | Layout 1             | `81757f35219e`  |
| 2259   | Layout 1             | `81757f35219e`  |
| 2250   | Layout 1             | `81757f35219e`  |
| 2243   | Layout 1             | `81757f35219e`  |
| 2235   | Layout 1             | `81757f35219e`  |
| 2229   | Layout 1             | `81757f35219e`  |
| 2224   | Layout 1             | `81757f35219e`  |
| 2218   | Layout 1             | `81757f35219e`  |
| 2215   | Layout 1             | `81757f35219e`  |
| 2207   | Layout 1             | `81757f35219e`  |
| 2203   | Layout 1             | `81757f35219e`  |
| 2196   | Layout 1             | `81757f35219e`  |
| 2192   | Layout 1             | `81757f35219e`  |
| 2189   | Layout 1             | `81757f35219e`  |
| 2183   | Layout 1             | `81757f35219e`  |
| 2179   | Layout 1             | `81757f35219e`  |
| 2171   | Layout 1             | `81757f35219e`  |
| 2163   | Layout 1             | `81757f35219e`  |
| 2156   | Layout 1             | `81757f35219e`  |
| 2151   | Layout 1             | `81757f35219e`  |
| 2147   | Layout 1             | `81757f35219e`  |
| 2142   | Layout 1             | `81757f35219e`  |
| 2138   | Layout 1             | `81757f35219e`  |
| 2134   | Layout 1             | `81757f35219e`  |
| 2130   | Layout 1             | `81757f35219e`  |
| 2122   | Layout 1             | `81757f35219e`  |
| 2107   | Layout 1             | `81757f35219e`  |
| 2098   | Layout 1             | `81757f35219e`  |
| 2089   | Layout 1             | `81757f35219e`  |
| 2081   | Layout 1             | `81757f35219e`  |
| 2073   | Layout 1             | `81757f35219e`  |
| 2067   | Layout 1             | `81757f35219e`  |
| 2063   | Layout 1             | `81757f35219e`  |
| 2059   | Layout 1             | `81757f35219e`  |
| 2052   | Layout 1             | `81757f35219e`  |
| 2044   | Layout 1             | `81757f35219e`  |
| 2039   | Layout 1             | `81757f35219e`  |
| 2032   | Layout 1             | `81757f35219e`  |
| 2025   | Layout 1             | `81757f35219e`  |
| 2011   | Layout 1             | `81757f35219e`  |
| 2005   | Layout 1             | `81757f35219e`  |
| 2000   | Layout 1             | `81757f35219e`  |
| 1996   | Layout 1             | `81757f35219e`  |
| 1991   | Layout 1             | `81757f35219e`  |
| 1985   | Layout 1             | `81757f35219e`  |
| 1980   | Layout 1             | `81757f35219e`  |
| 1969   | Layout 1             | `81757f35219e`  |
| 1964   | Layout 1             | `81757f35219e`  |
| 1958   | Layout 1             | `81757f35219e`  |
| 1950   | Layout 1             | `81757f35219e`  |
| 1945   | Layout 1             | `81757f35219e`  |
| 1937   | Layout 1             | `81757f35219e`  |
| 1933   | Layout 1             | `81757f35219e`  |
| 1927   | Layout 1             | `81757f35219e`  |
| 1921   | Layout 1             | `81757f35219e`  |
| 1914   | Layout 1             | `81757f35219e`  |
| 1908   | Layout 1             | `81757f35219e`  |
| 1897   | Layout 1             | `81757f35219e`  |
| 1892   | Layout 1             | `81757f35219e`  |
| 1886   | Layout 1             | `81757f35219e`  |
| 1881   | Layout 1             | `81757f35219e`  |
| 1871   | Layout 1             | `81757f35219e`  |
| 1866   | Layout 1             | `81757f35219e`  |
| 1862   | Layout 1             | `81757f35219e`  |
| 1854   | Layout 1             | `81757f35219e`  |
| 1846   | Layout 1             | `81757f35219e`  |
| 1838   | Layout 1             | `81757f35219e`  |
| 1832   | Layout 1             | `81757f35219e`  |
| 1826   | Layout 1             | `81757f35219e`  |
| 1822   | Layout 1             | `81757f35219e`  |
| 1818   | Layout 1             | `81757f35219e`  |
| 1804   | Layout 1             | `81757f35219e`  |
| 1794   | Layout 1             | `81757f35219e`  |
| 1790   | Layout 1             | `81757f35219e`  |
| 1784   | Layout 1             | `81757f35219e`  |
| 1774   | Layout 1             | `81757f35219e`  |
| 1771   | Layout 1             | `81757f35219e`  |
| 1762   | Layout 1             | `81757f35219e`  |
| 1759   | Layout 1             | `81757f35219e`  |
| 1754   | Layout 1             | `81757f35219e`  |
| 1749   | Layout 1             | `81757f35219e`  |
| 1743   | Layout 1             | `81757f35219e`  |
| 1737   | Layout 1             | `81757f35219e`  |
| 1731   | Layout 1             | `81757f35219e`  |
| 1725   | Layout 1             | `81757f35219e`  |
| 1717   | Layout 1             | `81757f35219e`  |
| 1710   | Layout 1             | `81757f35219e`  |
| 1704   | Layout 1             | `81757f35219e`  |
| 1698   | Layout 1             | `81757f35219e`  |
| 1690   | Layout 1             | `81757f35219e`  |
| 1685   | Layout 1             | `81757f35219e`  |
| 1680   | Layout 1             | `81757f35219e`  |
| 1674   | Layout 1             | `81757f35219e`  |
| 1668   | Layout 1             | `81757f35219e`  |
| 1659   | Layout 1             | `81757f35219e`  |
| 1649   | Layout 1             | `81757f35219e`  |
| 1642   | Layout 1             | `81757f35219e`  |
| 1636   | Layout 1             | `81757f35219e`  |
| 1628   | Layout 1             | `81757f35219e`  |
| 1622   | Layout 1             | `81757f35219e`  |
| 1614   | Layout 1             | `81757f35219e`  |
| 1608   | Layout 1             | `81757f35219e`  |
| 1602   | Layout 1             | `81757f35219e`  |
| 1598   | Layout 1             | `81757f35219e`  |
| 1594   | Layout 1             | `81757f35219e`  |
| 1590   | Layout 1             | `81757f35219e`  |
| 1587   | Layout 1             | `81757f35219e`  |
| 1584   | Layout 1             | `81757f35219e`  |
| 1579   | Layout 1             | `81757f35219e`  |
| 1572   | Layout 1             | `81757f35219e`  |
| 1565   | Layout 1             | `81757f35219e`  |
| 1559   | Layout 1             | `81757f35219e`  |
| 1554   | Layout 1             | `81757f35219e`  |
| 1547   | Layout 1             | `81757f35219e`  |
| 1537   | Layout 1             | `81757f35219e`  |
| 1529   | Layout 1             | `81757f35219e`  |
| 1524   | Layout 1             | `81757f35219e`  |
| 1519   | Layout 1             | `81757f35219e`  |
| 1509   | Layout 1             | `81757f35219e`  |
| 1506   | Layout 1             | `81757f35219e`  |
| 1504   | Layout 1             | `81757f35219e`  |
| 1500   | Layout 1             | `81757f35219e`  |
| 1493   | Layout 1             | `81757f35219e`  |
| 1489   | Layout 1             | `81757f35219e`  |
| 1485   | Layout 1             | `81757f35219e`  |
| 1481   | Layout 1             | `81757f35219e`  |
| 1474   | Layout 1             | `81757f35219e`  |
| 1466   | Layout 1             | `81757f35219e`  |
| 1462   | Layout 1             | `81757f35219e`  |
| 1459   | Layout 1             | `81757f35219e`  |
| 1453   | Layout 1             | `81757f35219e`  |
| 1450   | Layout 1             | `81757f35219e`  |
| 1445   | Layout 1             | `81757f35219e`  |
| 1439   | Layout 1             | `81757f35219e`  |
| 1433   | Layout 1             | `81757f35219e`  |
| 1430   | Layout 1             | `81757f35219e`  |
| 1426   | Layout 1             | `81757f35219e`  |
| 1421   | Layout 1             | `81757f35219e`  |
| 1417   | Layout 1             | `81757f35219e`  |
| 1416   | Layout 1             | `81757f35219e`  |
| 1409   | Layout 1             | `81757f35219e`  |
| 1405   | Layout 1             | `81757f35219e`  |
| 1401   | Layout 1             | `81757f35219e`  |
| 1396   | Layout 1             | `81757f35219e`  |
| 1391   | Layout 1             | `81757f35219e`  |
| 1390   | Layout 1             | `81757f35219e`  |
| 1386   | Layout 1             | `81757f35219e`  |
| 1381   | Layout 1             | `81757f35219e`  |
| 1379   | Layout 1             | `81757f35219e`  |
| 1372   | Layout 1             | `81757f35219e`  |
| 1366   | Layout 1             | `81757f35219e`  |
| 1364   | Layout 1             | `81757f35219e`  |
| 1363   | Layout 1             | `81757f35219e`  |
| 1360   | Layout 1             | `81757f35219e`  |
| 1358   | Layout 1             | `81757f35219e`  |
| 1355   | Layout 1             | `81757f35219e`  |
| 1351   | Layout 1             | `81757f35219e`  |
| 1348   | Layout 1             | `81757f35219e`  |
| 1346   | Layout 1             | `81757f35219e`  |
| 1341   | No documented layout | `81757f35219e`  |
| 1340   | No documented layout | `81757f35219e`  |
| 1338   | No documented layout | `81757f35219e`  |
| 1335   | No documented layout | `81757f35219e`  |
| 1333   | No documented layout | `81757f35219e`  |
| 1329   | No documented layout | `81757f35219e`  |
| 1327   | No documented layout | `81757f35219e`  |
| 1324   | No documented layout | `81757f35219e`  |
| 1321   | No documented layout | `81757f35219e`  |
| 1319   | No documented layout | `81757f35219e`  |
| 1318   | No documented layout | `81757f35219e`  |
| 1316   | No documented layout | `81757f35219e`  |
| 1313   | No documented layout | `81757f35219e`  |
| 1311   | No documented layout | `81757f35219e`  |
| 1309   | No documented layout | `81757f35219e`  |
| 1304   | No documented layout | `81757f35219e`  |
| 1292   | No documented layout | `81757f35219e`  |
| 1286   | No documented layout | `81757f35219e`  |
| 1280   | No documented layout | `81757f35219e`  |
| 1276   | No file              | `81757f35219e`  |
| 1267   | No file              | `81757f35219e`  |
| 1261   | No file              | `81757f35219e`  |
| 1256   | No file              | `81757f35219e`  |
| 1250   | No file              | `81757f35219e`  |
| 1246   | No file              | `81757f35219e`  |
| 1239   | No file              | `81757f35219e`  |
| 1230   | No file              | `81757f35219e`  |
| 1226   | No file              | `81757f35219e`  |
| 1220   | No file              | `81757f35219e`  |
| 1217   | No file              | `81757f35219e`  |
| 1211   | No file              | `81757f35219e`  |
| 1210   | No file              | `81757f35219e`  |
| 1208   | No file              | `81757f35219e`  |
| 1203   | No file              | `81757f35219e`  |
| 1197   | No file              | `81757f35219e`  |
| 1194   | No file              | `81757f35219e`  |
| 1192   | No file              | `81757f35219e`  |
| 1187   | No file              | `81757f35219e`  |
| 1183   | No file              | `81757f35219e`  |
| 1177   | No file              | `81757f35219e`  |
| 1173   | No file              | `81757f35219e`  |
| 1167   | No file              | `81757f35219e`  |
| 1164   | No file              | `81757f35219e`  |
| 1156   | No file              | `81757f35219e`  |
| 1149   | No file              | `81757f35219e`  |
| 1144   | No file              | `81757f35219e`  |
| 1137   | No file              | `81757f35219e`  |
| 1132   | No file              | `81757f35219e`  |
| 1127   | No file              | `81757f35219e`  |
| 1122   | No file              | `81757f35219e`  |
| 1118   | No file              | `81757f35219e`  |
| 1114   | No file              | `81757f35219e`  |
| 1109   | No file              | `81757f35219e`  |
| 1102   | No file              | `81757f35219e`  |
| 1096   | No file              | `81757f35219e`  |
| 1088   | No file              | `81757f35219e`  |
| 1081   | No file              | `81757f35219e`  |
| 1076   | No file              | `81757f35219e`  |
| 1069   | No file              | `81757f35219e`  |
| 1064   | No file              | `81757f35219e`  |
| 1058   | No file              | `81757f35219e`  |
| 1051   | No file              | `81757f35219e`  |
| 1044   | No file              | `81757f35219e`  |
| 1036   | No file              | `81757f35219e`  |
| 1026   | No file              | `81757f35219e`  |
| 1016   | No file              | `81757f35219e`  |
| 1009   | No file              | `81757f35219e`  |
| 1005   | No file              | `81757f35219e`  |
| 1000   | No file              | `81757f35219e`  |
| 998    | No file              | `81757f35219e`  |
| 990    | No file              | `81757f35219e`  |
| 979    | No file              | `81757f35219e`  |
| 972    | No file              | `81757f35219e`  |
| 963    | No file              | `81757f35219e`  |
| 955    | No file              | `81757f35219e`  |
| 946    | No file              | `81757f35219e`  |
| 938    | No file              | `81757f35219e`  |
| 927    | No file              | `81757f35219e`  |
| 911    | No file              | `81757f35219e`  |
| 904    | No file              | `81757f35219e`  |
| 899    | No file              | `81757f35219e`  |
| 894    | No file              | `81757f35219e`  |
| 885    | No file              | `81757f35219e`  |
| 879    | No file              | `81757f35219e`  |
| 872    | No file              | `81757f35219e`  |
| 864    | No file              | `81757f35219e`  |
| 855    | No file              | `81757f35219e`  |
| 853    | No file              | `81757f35219e`  |
| 845    | No file              | `81757f35219e`  |
| 837    | No file              | `81757f35219e`  |
| 829    | No file              | `81757f35219e`  |
| 822    | No file              | `81757f35219e`  |
| 814    | No file              | `81757f35219e`  |
| 805    | No file              | `81757f35219e`  |
| 794    | No file              | `81757f35219e`  |
| 787    | No file              | `81757f35219e`  |
| 780    | No file              | `81757f35219e`  |
| 771    | No file              | `81757f35219e`  |
| 760    | No file              | `81757f35219e`  |
| 748    | No file              | `81757f35219e`  |
| 741    | No file              | `81757f35219e`  |
| 736    | No file              | `81757f35219e`  |
| 731    | No file              | `81757f35219e`  |
| 723    | No file              | `81757f35219e`  |
| 711    | No file              | `81757f35219e`  |
| 707    | No file              | `81757f35219e`  |
| 697    | No file              | `81757f35219e`  |
| 689    | No file              | `81757f35219e`  |
| 683    | No file              | `81757f35219e`  |
| 678    | No file              | `81757f35219e`  |
| 670    | No file              | `81757f35219e`  |
| 661    | No file              | `81757f35219e`  |
| 656    | No file              | `81757f35219e`  |
| 652    | No file              | `81757f35219e`  |
| 643    | No file              | `81757f35219e`  |
| 637    | No file              | `81757f35219e`  |
| 630    | No file              | `81757f35219e`  |
| 627    | No file              | `81757f35219e`  |
| 621    | No file              | `81757f35219e`  |
| 617    | No file              | `81757f35219e`  |
| 615    | No file              | `81757f35219e`  |
| 606    | No file              | `81757f35219e`  |
| 599    | No file              | `81757f35219e`  |
| 592    | No file              | `81757f35219e`  |
| 586    | No file              | `81757f35219e`  |
| 577    | No file              | `81757f35219e`  |
| 569    | No file              | `81757f35219e`  |
| 561    | No file              | `81757f35219e`  |
| 554    | No file              | `81757f35219e`  |
| 542    | No file              | `81757f35219e`  |
| 532    | No file              | `81757f35219e`  |
| 531    | No file              | `81757f35219e`  |
| 526    | No file              | `81757f35219e`  |
| 521    | No file              | `81757f35219e`  |
| 517    | No file              | `81757f35219e`  |
| 510    | No file              | `81757f35219e`  |
| 508    | No file              | `81757f35219e`  |
| 504    | No file              | `81757f35219e`  |
| 497    | No file              | `81757f35219e`  |
| 491    | No file              | `81757f35219e`  |
| 485    | No file              | `81757f35219e`  |
| 478    | No file              | `81757f35219e`  |
| 472    | No file              | `81757f35219e`  |
| 466    | No file              | `81757f35219e`  |
| 457    | No file              | `81757f35219e`  |
| 452    | No file              | `81757f35219e`  |
| 449    | No file              | `81757f35219e`  |
| 435    | No file              | `81757f35219e`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `monstergroupoffset.dbss` | Required | Bare u16-keyed index: group key -> record offset and size |
| `languagedata_en.loc`     | Optional | Monster names, LOC type 6 at `str_id1` = `character_key`; hunting ground names, LOC type 116 |
| [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) | Optional | The hunting grounds that list each member, through the `CHARACTER_HUNTING_GROUNDS` and `HUNTING_GROUND_NAME_KR` lookup indexes |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | Same count as the offset table         |
| `+0x04` | Record[count] | records | See Record; in offset-table order      |

The records end exactly at the end of the file.

### Record (variable: 2 bytes + group)

Each record is preceded by a copy of its u16 key. The offset of a row points
past that copy, at the group's own key, as in
[`worldmapmonster.dbss`](worldmapmonster_dbss.md).

| Offset  | Type         | Field      | Notes                                                    |
| ------- | ------------ | ---------- | -------------------------------------------------------- |
| `+0x00` | u16          | key_prefix | Copy of the group's `group_key`                          |
| `+0x02` | Group Record | group      | `size` bytes of the offset row; the offset row points here |

### Group Record (variable: 6 bytes + members)

| Offset  | Type                  | Field        | Notes                                              |
| ------- | --------------------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16                   | group_key    | Same as the offset row `group_key`                 |
| `+0x02` | u32                   | member_count | Number of members; `0` on group 18 (client 3474)   |
| `+0x06` | Member[member_count]  | members      | See Member; ascending `character_key` in every group |

`6 + 6 * member_count` equals the offset row `size` on every record.

### Member (6 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Monster character key; LOC type 6 names it                            |
| `+0x02` | u32  | percent       | On the 1,000,000 = 100% scale; `1,000,000` on the last member of every group, see `percent` Values |

### `monstergroupoffset.dbss`

No magic and no trailer (`parse_bare_offset_rows()`).

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Number of rows |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

The rows are in file order, which is not key order: on client 3474 the keys
run 36 to 32, 15 to 1, then 31 to 16.

### Offset Row (10 bytes)

| Offset  | Type | Field     | Notes                                                        |
| ------- | ---- | --------- | ------------------------------------------------------------ |
| `+0x00` | u16  | group_key | Group key                                                    |
| `+0x02` | u32  | offset    | Start of the group record in `monstergroup.dbss`, past the key copy |
| `+0x06` | u32  | size      | Length of the group record, the key copy left out           |

## `percent` Values

Each member's `percent` is `1,000,000 / k` rounded, where `k` counts the
members from this one to the end of the group (within 2 on all 185 members,
client 3474). A group of five stores `200,000`, `250,000`, `333,334`,
`500,001`, `1,000,000`. Picking each member in list order with its own
chance, and moving on when it is not picked, gives every member the same
chance of `1 / member_count`. Read as cumulative chances, the values would
have to rise by equal steps (`200,000`, `400,000` ...); they do not.

## Hunting Grounds Column

The Hunting Grounds column lists every
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) hunting
ground whose `monster_ids` hold at least one member of the group, in
ascending hunting ground key order. It picks no best match and shows no
member counts: a group whose members appear in two zones shows both. Each
zone shows its name as stored, LOC type 116 (`Lv. 51 Abandoned Iron Mine`,
the level is part of the name), else the Korean string table name, else the
key, and links to its row in the `dropuihuntinggroundinfo.bss` view. The
cell shows three zones and a hoverable `... (+N)`; `hunting_grounds` keeps
every name for search and CSV export and `hunting_ground_keys` the keys. A
group whose members appear in no zone shows `-`.

The handler reads the zones from the `CHARACTER_HUNTING_GROUNDS` lookup index
(character key -> hunting ground keys, see `docs/handler.md`), so the table
opens no companion for them.

## Field Names

The fields are named from the `MonsterGroup` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `Group`, `Character`,
`Percent`). All 185 (group, character) pairs of client 3474 are sheet rows,
and all 185 have the same `Percent`. The sheet has 188 rows; the 3 extra are
group 18 (`21035` to `21037`, the Basilisk Den monsters), which has no
members in the client file on clients 1784 and 3474. None of the three keys
has a `characterstatic.dbss` row on either client, so the client build leaves
out members whose character it does not ship.

The `.xlsm` copy of the sheet has two note columns that are not compiled:
`#GroupName`, a hunting zone name per group (`폐철광산`, Abandoned Iron Mine,
for group 2; group 1 is `세렌디아 북부 평원 (테스트용)`, marked as a test
group), and `#MonsterName`. The 2016 client has no monster group table: its
PDB holds `gc::KillMonsterGroup` (the quest condition) but no
`gc::MonsterGroup*` struct or loader.

## Regions per Group

The regions whose `MonsterGroupForTotem` column in the `Region_Table` sheet
(client 1784) names each group. Region names and territories come from
[`regioninfo.bss`](regioninfo_bss.md) on client 3474. No region names groups
1 (the Altar Imp test group), 5 (Helm) or 9 (Shultz Guard).

| Group | Regions                                                                                         | Territory  | Members                                     |
| ----: | ----------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------- |
| 2     | 211 Abandoned Iron Mine, 555 Rhutum District, 556 Saunil District, 557 Entrance (same mine)     | Mediah     | Rhutum, Red Orc, Saunil and Khuruto (11)    |
| 3     | 35 Northern Plain of Serendia (Serendia), 213 Manes Hideout                                     | Mediah     | Manes (4)                                   |
| 4     | 214 Wandering Rogue Den                                                                         | Mediah     | Wandering Rogues, Servant of Darkness (4)   |
| 6     | 210 Canyon of Corruption                                                                        | Mediah     | Elric cultists, Decayed Swamp Monster (6)   |
| 7     | 417 Soldier's Cemetery                                                                          | Mediah     | Frenzied and Grudged Skeletons (6)          |
| 8     | 327 Sausan Garrison, 415 Sausan Garrison Wharf                                                  | Mediah     | Sausan soldiers (8)                         |
| 10    | 216 Hasrah Cliff                                                                                | Mediah     | Kamol, Balten, Kukuri, Buruko, Kamel (5)    |
| 11    | 241 Bashim Base, 585 and 674 Pujiya Canyon                                                      | Valencia   | Ohonsey, Terruda and Khala (10)             |
| 12    | 623 Titium Valley                                                                               | Valencia   | Desert Fogans (4)                           |
| 13    | 607 Desert Naga Temple                                                                          | Valencia   | Desert Nagas (3)                            |
| 14    | 603 and 678 Gahaz Bandits' Lair                                                                 | Valencia   | Sandstorm bandits (4)                       |
| 15    | 579 and 631 Cadry Ruins                                                                         | Valencia   | Cadry Fighter, Black Mage, Armored Fighter  |
| 16    | 622 Crescent Shrine, 625 Crescent Mountains                                                     | Valencia   | Crescent Watcher, Follower, Guardian        |
| 17    | 243 Taphtar Plain                                                                               | Valencia   | Centaurus (3)                               |
| 18    | 578 and 630 Gorgo Rock Belt, 632 Basilisk Den, 655 Basilisk Cave                                | Valencia   | none in the client file                     |
| 19    | 691 Pila Ku Jail                                                                                | Valencia   | Pila Ku Jail inmates and warders (6)        |
| 20    | 420 Roud Sulfur Works, 690 Roud Sulfur Mine                                                     | Valencia   | Lava monsters (6)                           |
| 21    | 688 Aakman Temple                                                                               | Valencia   | Aakman (7)                                  |
| 22    | 689 Hystria Ruins                                                                               | Valencia   | Kalqueesh, Vodkhan, Tukars and others (8)   |
| 23    | 736 and 747 Polly's Forest                                                                      | Kamasylvia | Poison mushrooms (5)                        |
| 24    | 728 and 746 Loopy Tree Forest                                                                   | Kamasylvia | Fadus (5)                                   |
| 25    | 708 Navarn Steppe                                                                               | Kamasylvia | Belladonna Elephant, Feather Wolf and others (5) |
| 26    | 711 Manshaum Forest, 723 Manshaum Forest Path                                                   | Kamasylvia | Manshaum (5)                                |
| 27    | 729 and 745 Tooth Fairy Forest                                                                  | Kamasylvia | Forest Ronaros (4)                          |
| 28    | 712 Mirumok Ruins, 722 Mirumok Ruins Entrance                                                   | Kamasylvia | Mirumok, Treants, Voraro (5)                |
| 29    | 739 and 755 Gyfin Rhasia Temple                                                                 | Kamasylvia | Gyfin Rhasia (4)                            |
| 30    | 895 and 934 Tshira Ruins                                                                        | Drieghan   | Tree Hermit, Keepers and others (7)         |
| 31    | 876 and 930 Blood Wolf Settlement                                                               | Drieghan   | Kagtum (6)                                  |
| 32    | 875 and 927 Sherekhan Necropolis                                                                | Drieghan   | Garud, Lateh, Belcadas, Nybrica, Federik    |
| 33    | 948 Protty Cave                                                                                 | Balenos    | Protty, Zera Protty, Kaz Protty             |
| 34    | 952 Sycraia Underwater Ruins                                                                    | Balenos    | Damaged Pirash, Lykin, Kureba               |
| 35    | 949 Sycraia Underwater Ruins                                                                    | Balenos    | Pirash, Lykin, Kureba, Elmermol             |
| 36    | 971 and 977 Star's End                                                                          | Calpheon   | Apostles and Harbingers (6)                 |

Group 3 is the only one that spans two territories: region 35 is in
Serendia, region 213 in Mediah.

## Notes

- The `Region_Table` sheet of the same `DataSheets.bexcel` points 57 regions
  at 33 groups (all but 1, 5 and 9) through its `MonsterGroupForTotem`
  column; see Regions per Group. That column is not in the client
  [`regioninfo.bss`](regioninfo_bss.md), so on the client nothing links a
  region to its group.
- Group to hunting ground, matched by members against
  [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) on client
  3474: 29 of the 35 non-empty groups have every member in one hunting ground
  (group 2 in `Lv.51 폐철광산`, 11 of 11). Groups 4 and 12 have all but one
  member in one hunting ground (3 of 4). Groups 1 (Altar Imp and four
  more), 34 (Damaged Pirash and two more), 35 (Pirash and three more) and 36
  (Apostle of Corruption and five more) share no member with any hunting
  ground. Group 6 is the one group with members in two zones: all 6 in
  `Lv. 53 Canyon of Corruption` and 5 of them in `Lv. 53 Elric Shrine`, so
  its Hunting Grounds cell names both. The cell of groups 1, 18, 34, 35 and
  36 is empty.
- `<Violent>` monsters: LOC type 6 gives 111 characters the title prefix
  `<Violent>` (`str_id4` = 1, client 3474), each a separate character key
  with the name of a regular monster. Every member of groups 13, 14, 16,
  19, 21 and 22 has a `<Violent>` character with the same name, and 3 of 4
  members of group 12 do. These seven groups belong to the seven zones that
  LOC type 10 lists as `[Hardcore] Violent ... Teleport` (49502 to 49507,
  49523): Titium Valley, Desert Naga Temple, Gahaz Bandits' Lair, Crescent
  Shrine, Pila Ku Jail, Aakman Temple and Hystria Ruins. In the other groups
  at most 2 members have one.
- The client Lua does not name the file: no `.luac` file of client 3474
  holds the string `monstergroup` or `totem`.
- The bytes are the same on clients 1784 and 3474 (1,402 and 364 bytes).
- The quest condition `killMonsterGroup(group, count)` does not read this
  file: its key is the `character_group` of
  [`characterstatic.dbss`](characterstatic_dbss.md#character-group). The
  2016 `gc::KillMonsterGroup` stores the first argument as
  `_characterGroupKey` (`gc::KeyType<short,-1>`, the type of the
  character's `_groupKey`), and on client 3474 every key of the 878
  `killMonsterGroup` calls in `quest.dbss` and the 16 in
  [`guildquest.dbss`](guildquest_dbss.md) (`84` and `125`) is a
  `character_group` value. The two key sets overlap without matching: Star's
  End is group 36 here and character group 116, and character group 36 is
  the Calpheon Shrine.
- The soul collectors' `monsterGroupKey` (`panel_whereuseitemdirection.luac`)
  is not a key of this file either: it is a `character_group`, see
  [`itemenchant.dbss`](itemenchant_dbss.md#soul-collectors). Bashim is
  group 11 here and character group 70 there.

## Open Questions

### What Reads the Groups

The server column `MonsterGroupForTotem` says a region uses its group for a
totem, and the `percent` values make one member pick with equal chances.
Nothing on the client names the feature: the Lua never names the file, and
the first 40 English LOC matches for `totem` are item names (Manshaum Totem,
Totem of the Sea). Which monster a region's totem spawns or targets, and
whether the client uses the file at all, is open.
