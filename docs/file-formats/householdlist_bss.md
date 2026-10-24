# `householdlist.bss` Format

## Purpose

Every house character: a u32 count after the PABR magic, then one u16
character key per house. On client 3482 the 865 keys are the 823 node
houses of [`houseinfo.bss`](houseinfo_bss.md), 25 guild houses and the 17
villas; on client 1784 the list holds 801 keys. The same keys are the room
list of [`innstaticstatus.dbss`](innstaticstatus_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | -------------- | --------- |
| 1      | 1109 and later | 3483    | `householdlist.bss` | 1,750 | 1 String Table | 4         |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 1      | `householdlist.bss` | 1,750 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `dc5d8194589b`  |
| 3482   | Layout 1 | `dc5d8194589b`  |
| 3474   | Layout 1 | `dc5d8194589b`  |
| 3473   | Layout 1 | `dc5d8194589b`  |
| 3464   | Layout 1 | `dc5d8194589b`  |
| 3458   | Layout 1 | `dc5d8194589b`  |
| 3454   | Layout 1 | `dc5d8194589b`  |
| 3444   | Layout 1 | `dc5d8194589b`  |
| 3435   | Layout 1 | `dc5d8194589b`  |
| 3426   | Layout 1 | `dc5d8194589b`  |
| 3418   | Layout 1 | `dc5d8194589b`  |
| 3412   | Layout 1 | `dc5d8194589b`  |
| 3402   | Layout 1 | `dc5d8194589b`  |
| 3396   | Layout 1 | `dc5d8194589b`  |
| 3387   | Layout 1 | `dc5d8194589b`  |
| 3381   | Layout 1 | `dc5d8194589b`  |
| 3373   | Layout 1 | `dc5d8194589b`  |
| 3364   | Layout 1 | `dc5d8194589b`  |
| 3356   | Layout 1 | `dc5d8194589b`  |
| 3349   | Layout 1 | `dc5d8194589b`  |
| 3342   | Layout 1 | `dc5d8194589b`  |
| 3335   | Layout 1 | `dc5d8194589b`  |
| 3326   | Layout 1 | `dc5d8194589b`  |
| 3321   | Layout 1 | `dc5d8194589b`  |
| 3314   | Layout 1 | `dc5d8194589b`  |
| 3303   | Layout 1 | `dc5d8194589b`  |
| 3302   | Layout 1 | `dc5d8194589b`  |
| 3293   | Layout 1 | `dc5d8194589b`  |
| 3283   | Layout 1 | `dc5d8194589b`  |
| 3275   | Layout 1 | `dc5d8194589b`  |
| 3267   | Layout 1 | `dc5d8194589b`  |
| 3258   | Layout 1 | `dc5d8194589b`  |
| 3251   | Layout 1 | `dc5d8194589b`  |
| 3242   | Layout 1 | `dc5d8194589b`  |
| 3235   | Layout 1 | `dc5d8194589b`  |
| 3229   | Layout 1 | `dc5d8194589b`  |
| 3212   | Layout 1 | `dc5d8194589b`  |
| 3203   | Layout 1 | `dc5d8194589b`  |
| 3193   | Layout 1 | `dc5d8194589b`  |
| 3186   | Layout 1 | `dc5d8194589b`  |
| 3177   | Layout 1 | `dc5d8194589b`  |
| 3169   | Layout 1 | `dc5d8194589b`  |
| 3158   | Layout 1 | `dc5d8194589b`  |
| 3151   | Layout 1 | `dc5d8194589b`  |
| 3144   | Layout 1 | `dc5d8194589b`  |
| 3133   | Layout 1 | `dc5d8194589b`  |
| 3125   | Layout 1 | `dc5d8194589b`  |
| 3118   | Layout 1 | `dc5d8194589b`  |
| 3111   | Layout 1 | `dc5d8194589b`  |
| 3103   | Layout 1 | `dc5d8194589b`  |
| 3095   | Layout 1 | `dc5d8194589b`  |
| 3086   | Layout 1 | `dc5d8194589b`  |
| 3072   | Layout 1 | `dc5d8194589b`  |
| 3062   | Layout 1 | `dc5d8194589b`  |
| 3052   | Layout 1 | `dc5d8194589b`  |
| 3045   | Layout 1 | `dc5d8194589b`  |
| 3037   | Layout 1 | `dc5d8194589b`  |
| 3030   | Layout 1 | `dc5d8194589b`  |
| 3021   | Layout 1 | `dc5d8194589b`  |
| 3012   | Layout 1 | `dc5d8194589b`  |
| 3002   | Layout 1 | `dc5d8194589b`  |
| 2995   | Layout 1 | `dc5d8194589b`  |
| 2987   | Layout 1 | `dc5d8194589b`  |
| 2978   | Layout 1 | `dc5d8194589b`  |
| 2970   | Layout 1 | `dc5d8194589b`  |
| 2959   | Layout 1 | `dc5d8194589b`  |
| 2951   | Layout 1 | `dc5d8194589b`  |
| 2942   | Layout 1 | `dc5d8194589b`  |
| 2935   | Layout 1 | `dc5d8194589b`  |
| 2932   | Layout 1 | `dc5d8194589b`  |
| 2923   | Layout 1 | `dc5d8194589b`  |
| 2919   | Layout 1 | `dc5d8194589b`  |
| 2907   | Layout 1 | `dc5d8194589b`  |
| 2900   | Layout 1 | `dc5d8194589b`  |
| 2891   | Layout 1 | `dc5d8194589b`  |
| 2882   | Layout 1 | `dc5d8194589b`  |
| 2872   | Layout 1 | `dc5d8194589b`  |
| 2863   | Layout 1 | `dc5d8194589b`  |
| 2855   | Layout 1 | `dc5d8194589b`  |
| 2849   | Layout 1 | `dc5d8194589b`  |
| 2844   | Layout 1 | `dc5d8194589b`  |
| 2834   | Layout 1 | `dc5d8194589b`  |
| 2825   | Layout 1 | `dc5d8194589b`  |
| 2819   | Layout 1 | `dc5d8194589b`  |
| 2811   | Layout 1 | `dc5d8194589b`  |
| 2803   | Layout 1 | `dc5d8194589b`  |
| 2794   | Layout 1 | `dc5d8194589b`  |
| 2783   | Layout 1 | `dc5d8194589b`  |
| 2774   | Layout 1 | `dc5d8194589b`  |
| 2765   | Layout 1 | `dc5d8194589b`  |
| 2756   | Layout 1 | `dc5d8194589b`  |
| 2750   | Layout 1 | `dc5d8194589b`  |
| 2743   | Layout 1 | `dc5d8194589b`  |
| 2736   | Layout 1 | `dc5d8194589b`  |
| 2726   | Layout 1 | `dc5d8194589b`  |
| 2717   | Layout 1 | `dc5d8194589b`  |
| 2709   | Layout 1 | `dc5d8194589b`  |
| 2703   | Layout 1 | `dc5d8194589b`  |
| 2695   | Layout 1 | `dc5d8194589b`  |
| 2684   | Layout 1 | `dc5d8194589b`  |
| 2672   | Layout 1 | `dc5d8194589b`  |
| 2665   | Layout 1 | `dc5d8194589b`  |
| 2657   | Layout 1 | `dc5d8194589b`  |
| 2649   | Layout 1 | `dc5d8194589b`  |
| 2644   | Layout 1 | `dc5d8194589b`  |
| 2637   | Layout 1 | `dc5d8194589b`  |
| 2629   | Layout 1 | `dc5d8194589b`  |
| 2619   | Layout 1 | `dc5d8194589b`  |
| 2612   | Layout 1 | `dc5d8194589b`  |
| 2606   | Layout 1 | `dc5d8194589b`  |
| 2602   | Layout 1 | `dc5d8194589b`  |
| 2601   | Layout 1 | `dc5d8194589b`  |
| 2592   | Layout 1 | `dc5d8194589b`  |
| 2583   | Layout 1 | `dc5d8194589b`  |
| 2575   | Layout 1 | `dc5d8194589b`  |
| 2567   | Layout 1 | `dc5d8194589b`  |
| 2560   | Layout 1 | `dc5d8194589b`  |
| 2553   | Layout 1 | `dc5d8194589b`  |
| 2545   | Layout 1 | `dc5d8194589b`  |
| 2538   | Layout 1 | `dc5d8194589b`  |
| 2529   | Layout 1 | `dc5d8194589b`  |
| 2519   | Layout 1 | `dc5d8194589b`  |
| 2513   | Layout 1 | `dc5d8194589b`  |
| 2510   | Layout 1 | `dc5d8194589b`  |
| 2507   | Layout 1 | `dc5d8194589b`  |
| 2503   | Layout 1 | `dc5d8194589b`  |
| 2498   | Layout 1 | `dc5d8194589b`  |
| 2492   | Layout 1 | `dc5d8194589b`  |
| 2487   | Layout 1 | `dc5d8194589b`  |
| 2480   | Layout 1 | `dc5d8194589b`  |
| 2474   | Layout 1 | `dc5d8194589b`  |
| 2468   | Layout 1 | `dc5d8194589b`  |
| 2460   | Layout 1 | `dc5d8194589b`  |
| 2453   | Layout 1 | `dc5d8194589b`  |
| 2444   | Layout 1 | `dc5d8194589b`  |
| 2438   | Layout 1 | `dc5d8194589b`  |
| 2434   | Layout 1 | `dc5d8194589b`  |
| 2429   | Layout 1 | `dc5d8194589b`  |
| 2421   | Layout 1 | `dc5d8194589b`  |
| 2414   | Layout 1 | `dc5d8194589b`  |
| 2407   | Layout 1 | `dc5d8194589b`  |
| 2401   | Layout 1 | `dc5d8194589b`  |
| 2397   | Layout 1 | `dc5d8194589b`  |
| 2393   | Layout 1 | `dc5d8194589b`  |
| 2384   | Layout 1 | `dc5d8194589b`  |
| 2378   | Layout 1 | `dc5d8194589b`  |
| 2372   | Layout 1 | `dc5d8194589b`  |
| 2358   | Layout 1 | `dc5d8194589b`  |
| 2352   | Layout 1 | `dc5d8194589b`  |
| 2347   | Layout 1 | `dc5d8194589b`  |
| 2343   | Layout 1 | `dc5d8194589b`  |
| 2335   | Layout 1 | `dc5d8194589b`  |
| 2327   | Layout 1 | `dc5d8194589b`  |
| 2324   | Layout 1 | `dc5d8194589b`  |
| 2319   | Layout 1 | `dc5d8194589b`  |
| 2313   | Layout 1 | `dc5d8194589b`  |
| 2308   | Layout 1 | `dc5d8194589b`  |
| 2302   | Layout 1 | `dc5d8194589b`  |
| 2295   | Layout 1 | `dc5d8194589b`  |
| 2290   | Layout 1 | `dc5d8194589b`  |
| 2284   | Layout 1 | `dc5d8194589b`  |
| 2276   | Layout 1 | `dc5d8194589b`  |
| 2269   | Layout 1 | `dc5d8194589b`  |
| 2259   | Layout 1 | `dc5d8194589b`  |
| 2250   | Layout 1 | `dc5d8194589b`  |
| 2243   | Layout 1 | `dc5d8194589b`  |
| 2235   | Layout 1 | `dc5d8194589b`  |
| 2229   | Layout 1 | `dc5d8194589b`  |
| 2224   | Layout 1 | `dc5d8194589b`  |
| 2218   | Layout 1 | `dc5d8194589b`  |
| 2215   | Layout 1 | `dc5d8194589b`  |
| 2207   | Layout 1 | `dc5d8194589b`  |
| 2203   | Layout 1 | `dc5d8194589b`  |
| 2196   | Layout 1 | `dc5d8194589b`  |
| 2192   | Layout 1 | `dc5d8194589b`  |
| 2189   | Layout 1 | `dc5d8194589b`  |
| 2183   | Layout 1 | `dc5d8194589b`  |
| 2179   | Layout 1 | `dc5d8194589b`  |
| 2171   | Layout 1 | `dc5d8194589b`  |
| 2163   | Layout 1 | `dc5d8194589b`  |
| 2156   | Layout 1 | `dc5d8194589b`  |
| 2151   | Layout 1 | `dc5d8194589b`  |
| 2147   | Layout 1 | `dc5d8194589b`  |
| 2142   | Layout 1 | `dc5d8194589b`  |
| 2138   | Layout 1 | `dc5d8194589b`  |
| 2134   | Layout 1 | `dc5d8194589b`  |
| 2130   | Layout 1 | `dc5d8194589b`  |
| 2122   | Layout 1 | `dc5d8194589b`  |
| 2107   | Layout 1 | `dc5d8194589b`  |
| 2098   | Layout 1 | `dc5d8194589b`  |
| 2089   | Layout 1 | `dc5d8194589b`  |
| 2081   | Layout 1 | `dc5d8194589b`  |
| 2073   | Layout 1 | `dc5d8194589b`  |
| 2067   | Layout 1 | `dc5d8194589b`  |
| 2063   | Layout 1 | `dc5d8194589b`  |
| 2059   | Layout 1 | `dc5d8194589b`  |
| 2052   | Layout 1 | `dc5d8194589b`  |
| 2044   | Layout 1 | `dc5d8194589b`  |
| 2039   | Layout 1 | `dc5d8194589b`  |
| 2032   | Layout 1 | `dc5d8194589b`  |
| 2025   | Layout 1 | `dc5d8194589b`  |
| 2011   | Layout 1 | `dc5d8194589b`  |
| 2005   | Layout 1 | `dc5d8194589b`  |
| 2000   | Layout 1 | `dc5d8194589b`  |
| 1996   | Layout 1 | `dc5d8194589b`  |
| 1991   | Layout 1 | `dc5d8194589b`  |
| 1985   | Layout 1 | `dc5d8194589b`  |
| 1980   | Layout 1 | `dc5d8194589b`  |
| 1969   | Layout 1 | `dc5d8194589b`  |
| 1964   | Layout 1 | `dc5d8194589b`  |
| 1958   | Layout 1 | `dc5d8194589b`  |
| 1950   | Layout 1 | `dc5d8194589b`  |
| 1945   | Layout 1 | `dc5d8194589b`  |
| 1937   | Layout 1 | `dc5d8194589b`  |
| 1933   | Layout 1 | `dc5d8194589b`  |
| 1927   | Layout 1 | `dc5d8194589b`  |
| 1921   | Layout 1 | `dc5d8194589b`  |
| 1914   | Layout 1 | `dc5d8194589b`  |
| 1908   | Layout 1 | `dc5d8194589b`  |
| 1897   | Layout 1 | `dc5d8194589b`  |
| 1892   | Layout 1 | `dc5d8194589b`  |
| 1886   | Layout 1 | `dc5d8194589b`  |
| 1881   | Layout 1 | `dc5d8194589b`  |
| 1871   | Layout 1 | `dc5d8194589b`  |
| 1866   | Layout 1 | `dc5d8194589b`  |
| 1862   | Layout 1 | `dc5d8194589b`  |
| 1854   | Layout 1 | `dc5d8194589b`  |
| 1846   | Layout 1 | `dc5d8194589b`  |
| 1838   | Layout 1 | `dc5d8194589b`  |
| 1832   | Layout 1 | `dc5d8194589b`  |
| 1826   | Layout 1 | `dc5d8194589b`  |
| 1822   | Layout 1 | `dc5d8194589b`  |
| 1818   | Layout 1 | `dc5d8194589b`  |
| 1804   | Layout 1 | `dc5d8194589b`  |
| 1794   | Layout 1 | `dc5d8194589b`  |
| 1790   | Layout 1 | `dc5d8194589b`  |
| 1784   | Layout 1 | `dc5d8194589b`  |
| 1774   | Layout 1 | `dc5d8194589b`  |
| 1771   | Layout 1 | `dc5d8194589b`  |
| 1762   | Layout 1 | `dc5d8194589b`  |
| 1759   | Layout 1 | `dc5d8194589b`  |
| 1754   | Layout 1 | `dc5d8194589b`  |
| 1749   | Layout 1 | `dc5d8194589b`  |
| 1743   | Layout 1 | `dc5d8194589b`  |
| 1737   | Layout 1 | `dc5d8194589b`  |
| 1731   | Layout 1 | `dc5d8194589b`  |
| 1725   | Layout 1 | `dc5d8194589b`  |
| 1717   | Layout 1 | `dc5d8194589b`  |
| 1710   | Layout 1 | `dc5d8194589b`  |
| 1704   | Layout 1 | `dc5d8194589b`  |
| 1698   | Layout 1 | `dc5d8194589b`  |
| 1690   | Layout 1 | `dc5d8194589b`  |
| 1685   | Layout 1 | `dc5d8194589b`  |
| 1680   | Layout 1 | `dc5d8194589b`  |
| 1674   | Layout 1 | `dc5d8194589b`  |
| 1668   | Layout 1 | `dc5d8194589b`  |
| 1659   | Layout 1 | `dc5d8194589b`  |
| 1649   | Layout 1 | `dc5d8194589b`  |
| 1642   | Layout 1 | `dc5d8194589b`  |
| 1636   | Layout 1 | `dc5d8194589b`  |
| 1628   | Layout 1 | `dc5d8194589b`  |
| 1622   | Layout 1 | `dc5d8194589b`  |
| 1614   | Layout 1 | `dc5d8194589b`  |
| 1608   | Layout 1 | `dc5d8194589b`  |
| 1602   | Layout 1 | `dc5d8194589b`  |
| 1598   | Layout 1 | `dc5d8194589b`  |
| 1594   | Layout 1 | `dc5d8194589b`  |
| 1590   | Layout 1 | `dc5d8194589b`  |
| 1587   | Layout 1 | `dc5d8194589b`  |
| 1584   | Layout 1 | `dc5d8194589b`  |
| 1579   | Layout 1 | `dc5d8194589b`  |
| 1572   | Layout 1 | `dc5d8194589b`  |
| 1565   | Layout 1 | `dc5d8194589b`  |
| 1559   | Layout 1 | `dc5d8194589b`  |
| 1554   | Layout 1 | `dc5d8194589b`  |
| 1547   | Layout 1 | `dc5d8194589b`  |
| 1537   | Layout 1 | `dc5d8194589b`  |
| 1529   | Layout 1 | `dc5d8194589b`  |
| 1524   | Layout 1 | `dc5d8194589b`  |
| 1519   | Layout 1 | `dc5d8194589b`  |
| 1509   | Layout 1 | `dc5d8194589b`  |
| 1506   | Layout 1 | `dc5d8194589b`  |
| 1504   | Layout 1 | `dc5d8194589b`  |
| 1500   | Layout 1 | `dc5d8194589b`  |
| 1493   | Layout 1 | `dc5d8194589b`  |
| 1489   | Layout 1 | `dc5d8194589b`  |
| 1485   | Layout 1 | `dc5d8194589b`  |
| 1481   | Layout 1 | `dc5d8194589b`  |
| 1474   | Layout 1 | `dc5d8194589b`  |
| 1466   | Layout 1 | `dc5d8194589b`  |
| 1462   | Layout 1 | `dc5d8194589b`  |
| 1459   | Layout 1 | `dc5d8194589b`  |
| 1453   | Layout 1 | `dc5d8194589b`  |
| 1450   | Layout 1 | `dc5d8194589b`  |
| 1445   | Layout 1 | `dc5d8194589b`  |
| 1439   | Layout 1 | `dc5d8194589b`  |
| 1433   | Layout 1 | `dc5d8194589b`  |
| 1430   | Layout 1 | `dc5d8194589b`  |
| 1426   | Layout 1 | `dc5d8194589b`  |
| 1421   | Layout 1 | `dc5d8194589b`  |
| 1417   | Layout 1 | `dc5d8194589b`  |
| 1416   | Layout 1 | `dc5d8194589b`  |
| 1409   | Layout 1 | `dc5d8194589b`  |
| 1405   | Layout 1 | `dc5d8194589b`  |
| 1401   | Layout 1 | `dc5d8194589b`  |
| 1396   | Layout 1 | `dc5d8194589b`  |
| 1391   | Layout 1 | `dc5d8194589b`  |
| 1390   | Layout 1 | `dc5d8194589b`  |
| 1386   | Layout 1 | `dc5d8194589b`  |
| 1381   | Layout 1 | `dc5d8194589b`  |
| 1379   | Layout 1 | `dc5d8194589b`  |
| 1372   | Layout 1 | `dc5d8194589b`  |
| 1366   | Layout 1 | `dc5d8194589b`  |
| 1364   | Layout 1 | `dc5d8194589b`  |
| 1363   | Layout 1 | `dc5d8194589b`  |
| 1360   | Layout 1 | `dc5d8194589b`  |
| 1358   | Layout 1 | `dc5d8194589b`  |
| 1355   | Layout 1 | `dc5d8194589b`  |
| 1351   | Layout 1 | `dc5d8194589b`  |
| 1348   | Layout 1 | `dc5d8194589b`  |
| 1346   | Layout 1 | `dc5d8194589b`  |
| 1341   | Layout 1 | `dc5d8194589b`  |
| 1340   | Layout 1 | `dc5d8194589b`  |
| 1338   | Layout 1 | `dc5d8194589b`  |
| 1335   | Layout 1 | `dc5d8194589b`  |
| 1333   | Layout 1 | `dc5d8194589b`  |
| 1329   | Layout 1 | `dc5d8194589b`  |
| 1327   | Layout 1 | `dc5d8194589b`  |
| 1324   | Layout 1 | `dc5d8194589b`  |
| 1321   | Layout 1 | `dc5d8194589b`  |
| 1319   | Layout 1 | `dc5d8194589b`  |
| 1318   | Layout 1 | `dc5d8194589b`  |
| 1316   | Layout 1 | `dc5d8194589b`  |
| 1313   | Layout 1 | `dc5d8194589b`  |
| 1311   | Layout 1 | `dc5d8194589b`  |
| 1309   | Layout 1 | `dc5d8194589b`  |
| 1304   | Layout 1 | `dc5d8194589b`  |
| 1292   | Layout 1 | `dc5d8194589b`  |
| 1286   | Layout 1 | `dc5d8194589b`  |
| 1280   | Layout 1 | `dc5d8194589b`  |
| 1276   | Layout 1 | `dc5d8194589b`  |
| 1267   | Layout 1 | `dc5d8194589b`  |
| 1261   | Layout 1 | `dc5d8194589b`  |
| 1256   | Layout 1 | `dc5d8194589b`  |
| 1250   | Layout 1 | `dc5d8194589b`  |
| 1246   | No file  | `dc5d8194589b`  |
| 1239   | No file  | `dc5d8194589b`  |
| 1230   | No file  | `dc5d8194589b`  |
| 1226   | No file  | `dc5d8194589b`  |
| 1220   | No file  | `dc5d8194589b`  |
| 1217   | No file  | `dc5d8194589b`  |
| 1211   | No file  | `dc5d8194589b`  |
| 1210   | No file  | `dc5d8194589b`  |
| 1208   | No file  | `dc5d8194589b`  |
| 1203   | No file  | `dc5d8194589b`  |
| 1197   | No file  | `dc5d8194589b`  |
| 1194   | No file  | `dc5d8194589b`  |
| 1192   | No file  | `dc5d8194589b`  |
| 1187   | No file  | `dc5d8194589b`  |
| 1183   | No file  | `dc5d8194589b`  |
| 1177   | No file  | `dc5d8194589b`  |
| 1173   | No file  | `dc5d8194589b`  |
| 1167   | No file  | `dc5d8194589b`  |
| 1164   | No file  | `dc5d8194589b`  |
| 1156   | No file  | `dc5d8194589b`  |
| 1149   | No file  | `dc5d8194589b`  |
| 1144   | Layout 1 | `dc5d8194589b`  |
| 1137   | Layout 1 | `dc5d8194589b`  |
| 1132   | Layout 1 | `dc5d8194589b`  |
| 1127   | Layout 1 | `dc5d8194589b`  |
| 1122   | Layout 1 | `dc5d8194589b`  |
| 1118   | Layout 1 | `dc5d8194589b`  |
| 1114   | Layout 1 | `dc5d8194589b`  |
| 1109   | Layout 1 | `dc5d8194589b`  |
| 1102   | No file  | `dc5d8194589b`  |
| 1096   | No file  | `dc5d8194589b`  |
| 1088   | No file  | `dc5d8194589b`  |
| 1081   | No file  | `dc5d8194589b`  |
| 1076   | No file  | `dc5d8194589b`  |
| 1069   | No file  | `dc5d8194589b`  |
| 1064   | No file  | `dc5d8194589b`  |
| 1058   | No file  | `dc5d8194589b`  |
| 1051   | No file  | `dc5d8194589b`  |
| 1044   | No file  | `dc5d8194589b`  |
| 1036   | No file  | `dc5d8194589b`  |
| 1026   | No file  | `dc5d8194589b`  |
| 1016   | No file  | `dc5d8194589b`  |
| 1009   | No file  | `dc5d8194589b`  |
| 1005   | No file  | `dc5d8194589b`  |
| 1000   | No file  | `dc5d8194589b`  |
| 998    | No file  | `dc5d8194589b`  |
| 990    | No file  | `dc5d8194589b`  |
| 979    | No file  | `dc5d8194589b`  |
| 972    | No file  | `dc5d8194589b`  |
| 963    | No file  | `dc5d8194589b`  |
| 955    | No file  | `dc5d8194589b`  |
| 946    | No file  | `dc5d8194589b`  |
| 938    | No file  | `dc5d8194589b`  |
| 927    | No file  | `dc5d8194589b`  |
| 911    | No file  | `dc5d8194589b`  |
| 904    | No file  | `dc5d8194589b`  |
| 899    | No file  | `dc5d8194589b`  |
| 894    | No file  | `dc5d8194589b`  |
| 885    | No file  | `dc5d8194589b`  |
| 879    | No file  | `dc5d8194589b`  |
| 872    | No file  | `dc5d8194589b`  |
| 864    | No file  | `dc5d8194589b`  |
| 855    | No file  | `dc5d8194589b`  |
| 853    | No file  | `dc5d8194589b`  |
| 845    | No file  | `dc5d8194589b`  |
| 837    | No file  | `dc5d8194589b`  |
| 829    | No file  | `dc5d8194589b`  |
| 822    | No file  | `dc5d8194589b`  |
| 814    | No file  | `dc5d8194589b`  |
| 805    | No file  | `dc5d8194589b`  |
| 794    | No file  | `dc5d8194589b`  |
| 787    | No file  | `dc5d8194589b`  |
| 780    | No file  | `dc5d8194589b`  |
| 771    | No file  | `dc5d8194589b`  |
| 760    | No file  | `dc5d8194589b`  |
| 748    | No file  | `dc5d8194589b`  |
| 741    | No file  | `dc5d8194589b`  |
| 736    | No file  | `dc5d8194589b`  |
| 731    | No file  | `dc5d8194589b`  |
| 723    | No file  | `dc5d8194589b`  |
| 711    | No file  | `dc5d8194589b`  |
| 707    | No file  | `dc5d8194589b`  |
| 697    | No file  | `dc5d8194589b`  |
| 689    | No file  | `dc5d8194589b`  |
| 683    | No file  | `dc5d8194589b`  |
| 678    | No file  | `dc5d8194589b`  |
| 670    | No file  | `dc5d8194589b`  |
| 661    | No file  | `dc5d8194589b`  |
| 656    | No file  | `dc5d8194589b`  |
| 652    | No file  | `dc5d8194589b`  |
| 643    | No file  | `dc5d8194589b`  |
| 637    | No file  | `dc5d8194589b`  |
| 630    | No file  | `dc5d8194589b`  |
| 627    | No file  | `dc5d8194589b`  |
| 621    | No file  | `dc5d8194589b`  |
| 617    | No file  | `dc5d8194589b`  |
| 615    | No file  | `dc5d8194589b`  |
| 606    | No file  | `dc5d8194589b`  |
| 599    | No file  | `dc5d8194589b`  |
| 592    | No file  | `dc5d8194589b`  |
| 586    | No file  | `dc5d8194589b`  |
| 577    | No file  | `dc5d8194589b`  |
| 569    | No file  | `dc5d8194589b`  |
| 561    | No file  | `dc5d8194589b`  |
| 554    | No file  | `dc5d8194589b`  |
| 542    | No file  | `dc5d8194589b`  |
| 532    | No file  | `dc5d8194589b`  |
| 531    | No file  | `dc5d8194589b`  |
| 526    | No file  | `dc5d8194589b`  |
| 521    | No file  | `dc5d8194589b`  |
| 517    | No file  | `dc5d8194589b`  |
| 510    | No file  | `dc5d8194589b`  |
| 508    | No file  | `dc5d8194589b`  |
| 504    | No file  | `dc5d8194589b`  |
| 497    | No file  | `dc5d8194589b`  |
| 491    | No file  | `dc5d8194589b`  |
| 485    | No file  | `dc5d8194589b`  |
| 478    | No file  | `dc5d8194589b`  |
| 472    | No file  | `dc5d8194589b`  |
| 466    | No file  | `dc5d8194589b`  |
| 457    | No file  | `dc5d8194589b`  |
| 452    | No file  | `dc5d8194589b`  |
| 449    | No file  | `dc5d8194589b`  |
| 435    | No file  | `dc5d8194589b`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | House names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                 | Field           | Notes                                                       |
| -------------------- | -------------------- | --------------- | ----------------------------------------------------------- |
| `+0x00`              | char[4]              | magic           | ASCII `PABR`                                                |
| `+0x04`              | u32                  | character_count | Number of house keys; 865 on client 3482                    |
| `+0x08`              | u16[character_count] | character_key   | A house, a `characterstatic.dbss` key; each key once        |
| `character_key+0x00` | String Table         | string_table    | See String Table                                            |
| `string_table+0x00`  | u32                  | table_start     | Offset of the string table, where `character_key` ends      |
| `string_table+0x04`  | u32                  | zero            | Always `0`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482              |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                   |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after the file; the server dump of that client holds the string
`houseHoldList`. Every key resolves to a house name (LOC type 6), so
`character_key` names the meaning.

## Notes

- On client 3482 the keys are, in file order, the 823 `houseinfo.bss` keys
  in that file's row order, with 42 more keys among them: the 23 guild
  houses of [`guildhouseinfo.dbss`](guildhouseinfo_dbss.md), Grána (`3520`)
  and O'draxxia (`3806`) Guild Houses and the villas `3371` to `3387`
  (Kunid's Villa to Oberin's Villa).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per character key.
