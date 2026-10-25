# `houseinfoviewposition.dbss` Format

## Purpose

A world position and a facing per house and house use type: one 32-byte
row for each pair of a house character and an `eHouseUseType` value (`3`
Ranch, `12` CannonWorkshop, `13` Shipyard, `14` CarriageWorkshop). The rows
cover node houses of [`houseinfo.bss`](houseinfo_bss.md) and guild houses of
[`guildhouseinfo.dbss`](guildhouseinfo_dbss.md); a guild house holds up to
two rows, one per use type. Companion `houseinfoviewpositionoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | ------------- | --------- |
| 1      | 1292 and later | `houseinfoviewposition.dbss`       | 2,708 | 84 Row        | 32        |
| 1      | 1292 and later | `houseinfoviewpositionoffset.dbss` | 1,348 | 84 Offset Row | 16        |

| Layout | File                               | Known            | Unknown    |
| ------ | ---------------------------------- | ---------------- | ---------- |
| 1      | `houseinfoviewposition.dbss`       | 2,708 B (100.0%) | 0 B (0.0%) |
| 1      | `houseinfoviewpositionoffset.dbss` | 1,348 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `da749b0343c7`  |
| 3482   | Layout 1 | `da749b0343c7`  |
| 3474   | Layout 1 | `da749b0343c7`  |
| 3473   | Layout 1 | `da749b0343c7`  |
| 3464   | Layout 1 | `da749b0343c7`  |
| 3458   | Layout 1 | `da749b0343c7`  |
| 3454   | Layout 1 | `da749b0343c7`  |
| 3444   | Layout 1 | `da749b0343c7`  |
| 3435   | Layout 1 | `da749b0343c7`  |
| 3426   | Layout 1 | `da749b0343c7`  |
| 3418   | Layout 1 | `da749b0343c7`  |
| 3412   | Layout 1 | `da749b0343c7`  |
| 3402   | Layout 1 | `da749b0343c7`  |
| 3396   | Layout 1 | `da749b0343c7`  |
| 3387   | Layout 1 | `da749b0343c7`  |
| 3381   | Layout 1 | `da749b0343c7`  |
| 3373   | Layout 1 | `da749b0343c7`  |
| 3364   | Layout 1 | `da749b0343c7`  |
| 3356   | Layout 1 | `da749b0343c7`  |
| 3349   | Layout 1 | `da749b0343c7`  |
| 3342   | Layout 1 | `da749b0343c7`  |
| 3335   | Layout 1 | `da749b0343c7`  |
| 3326   | Layout 1 | `da749b0343c7`  |
| 3321   | Layout 1 | `da749b0343c7`  |
| 3314   | Layout 1 | `da749b0343c7`  |
| 3303   | Layout 1 | `da749b0343c7`  |
| 3302   | Layout 1 | `da749b0343c7`  |
| 3293   | Layout 1 | `da749b0343c7`  |
| 3283   | Layout 1 | `da749b0343c7`  |
| 3275   | Layout 1 | `da749b0343c7`  |
| 3267   | Layout 1 | `da749b0343c7`  |
| 3258   | Layout 1 | `da749b0343c7`  |
| 3251   | Layout 1 | `da749b0343c7`  |
| 3242   | Layout 1 | `da749b0343c7`  |
| 3235   | Layout 1 | `da749b0343c7`  |
| 3229   | Layout 1 | `da749b0343c7`  |
| 3212   | Layout 1 | `da749b0343c7`  |
| 3203   | Layout 1 | `da749b0343c7`  |
| 3193   | Layout 1 | `da749b0343c7`  |
| 3186   | Layout 1 | `da749b0343c7`  |
| 3177   | Layout 1 | `da749b0343c7`  |
| 3169   | Layout 1 | `da749b0343c7`  |
| 3158   | Layout 1 | `da749b0343c7`  |
| 3151   | Layout 1 | `da749b0343c7`  |
| 3144   | Layout 1 | `da749b0343c7`  |
| 3133   | Layout 1 | `da749b0343c7`  |
| 3125   | Layout 1 | `da749b0343c7`  |
| 3118   | Layout 1 | `da749b0343c7`  |
| 3111   | Layout 1 | `da749b0343c7`  |
| 3103   | Layout 1 | `da749b0343c7`  |
| 3095   | Layout 1 | `da749b0343c7`  |
| 3086   | Layout 1 | `da749b0343c7`  |
| 3072   | Layout 1 | `da749b0343c7`  |
| 3062   | Layout 1 | `da749b0343c7`  |
| 3052   | Layout 1 | `da749b0343c7`  |
| 3045   | Layout 1 | `da749b0343c7`  |
| 3037   | Layout 1 | `da749b0343c7`  |
| 3030   | Layout 1 | `da749b0343c7`  |
| 3021   | Layout 1 | `da749b0343c7`  |
| 3012   | Layout 1 | `da749b0343c7`  |
| 3002   | Layout 1 | `da749b0343c7`  |
| 2995   | Layout 1 | `da749b0343c7`  |
| 2987   | Layout 1 | `da749b0343c7`  |
| 2978   | Layout 1 | `da749b0343c7`  |
| 2970   | Layout 1 | `da749b0343c7`  |
| 2959   | Layout 1 | `da749b0343c7`  |
| 2951   | Layout 1 | `da749b0343c7`  |
| 2942   | Layout 1 | `da749b0343c7`  |
| 2935   | Layout 1 | `da749b0343c7`  |
| 2932   | Layout 1 | `da749b0343c7`  |
| 2923   | Layout 1 | `da749b0343c7`  |
| 2919   | Layout 1 | `da749b0343c7`  |
| 2907   | Layout 1 | `da749b0343c7`  |
| 2900   | Layout 1 | `da749b0343c7`  |
| 2891   | Layout 1 | `da749b0343c7`  |
| 2882   | Layout 1 | `da749b0343c7`  |
| 2872   | Layout 1 | `da749b0343c7`  |
| 2863   | Layout 1 | `da749b0343c7`  |
| 2855   | Layout 1 | `da749b0343c7`  |
| 2849   | Layout 1 | `da749b0343c7`  |
| 2844   | Layout 1 | `da749b0343c7`  |
| 2834   | Layout 1 | `da749b0343c7`  |
| 2825   | Layout 1 | `da749b0343c7`  |
| 2819   | Layout 1 | `da749b0343c7`  |
| 2811   | Layout 1 | `da749b0343c7`  |
| 2803   | Layout 1 | `da749b0343c7`  |
| 2794   | Layout 1 | `da749b0343c7`  |
| 2783   | Layout 1 | `da749b0343c7`  |
| 2774   | Layout 1 | `da749b0343c7`  |
| 2765   | Layout 1 | `da749b0343c7`  |
| 2756   | Layout 1 | `da749b0343c7`  |
| 2750   | Layout 1 | `da749b0343c7`  |
| 2743   | Layout 1 | `da749b0343c7`  |
| 2736   | Layout 1 | `da749b0343c7`  |
| 2726   | Layout 1 | `da749b0343c7`  |
| 2717   | Layout 1 | `da749b0343c7`  |
| 2709   | Layout 1 | `da749b0343c7`  |
| 2703   | Layout 1 | `da749b0343c7`  |
| 2695   | Layout 1 | `da749b0343c7`  |
| 2684   | Layout 1 | `da749b0343c7`  |
| 2672   | Layout 1 | `da749b0343c7`  |
| 2665   | Layout 1 | `da749b0343c7`  |
| 2657   | Layout 1 | `da749b0343c7`  |
| 2649   | Layout 1 | `da749b0343c7`  |
| 2644   | Layout 1 | `da749b0343c7`  |
| 2637   | Layout 1 | `da749b0343c7`  |
| 2629   | Layout 1 | `da749b0343c7`  |
| 2619   | Layout 1 | `da749b0343c7`  |
| 2612   | Layout 1 | `da749b0343c7`  |
| 2606   | Layout 1 | `da749b0343c7`  |
| 2602   | Layout 1 | `da749b0343c7`  |
| 2601   | Layout 1 | `da749b0343c7`  |
| 2592   | Layout 1 | `da749b0343c7`  |
| 2583   | Layout 1 | `da749b0343c7`  |
| 2575   | Layout 1 | `da749b0343c7`  |
| 2567   | Layout 1 | `da749b0343c7`  |
| 2560   | Layout 1 | `da749b0343c7`  |
| 2553   | Layout 1 | `da749b0343c7`  |
| 2545   | Layout 1 | `da749b0343c7`  |
| 2538   | Layout 1 | `da749b0343c7`  |
| 2529   | Layout 1 | `da749b0343c7`  |
| 2519   | Layout 1 | `da749b0343c7`  |
| 2513   | Layout 1 | `da749b0343c7`  |
| 2510   | Layout 1 | `da749b0343c7`  |
| 2507   | Layout 1 | `da749b0343c7`  |
| 2503   | Layout 1 | `da749b0343c7`  |
| 2498   | Layout 1 | `da749b0343c7`  |
| 2492   | Layout 1 | `da749b0343c7`  |
| 2487   | Layout 1 | `da749b0343c7`  |
| 2480   | Layout 1 | `da749b0343c7`  |
| 2474   | Layout 1 | `da749b0343c7`  |
| 2468   | Layout 1 | `da749b0343c7`  |
| 2460   | Layout 1 | `da749b0343c7`  |
| 2453   | Layout 1 | `da749b0343c7`  |
| 2444   | Layout 1 | `da749b0343c7`  |
| 2438   | Layout 1 | `da749b0343c7`  |
| 2434   | Layout 1 | `da749b0343c7`  |
| 2429   | Layout 1 | `da749b0343c7`  |
| 2421   | Layout 1 | `da749b0343c7`  |
| 2414   | Layout 1 | `da749b0343c7`  |
| 2407   | Layout 1 | `da749b0343c7`  |
| 2401   | Layout 1 | `da749b0343c7`  |
| 2397   | Layout 1 | `da749b0343c7`  |
| 2393   | Layout 1 | `da749b0343c7`  |
| 2384   | Layout 1 | `da749b0343c7`  |
| 2378   | Layout 1 | `da749b0343c7`  |
| 2372   | Layout 1 | `da749b0343c7`  |
| 2358   | Layout 1 | `da749b0343c7`  |
| 2352   | Layout 1 | `da749b0343c7`  |
| 2347   | Layout 1 | `da749b0343c7`  |
| 2343   | Layout 1 | `da749b0343c7`  |
| 2335   | Layout 1 | `da749b0343c7`  |
| 2327   | Layout 1 | `da749b0343c7`  |
| 2324   | Layout 1 | `da749b0343c7`  |
| 2319   | Layout 1 | `da749b0343c7`  |
| 2313   | Layout 1 | `da749b0343c7`  |
| 2308   | Layout 1 | `da749b0343c7`  |
| 2302   | Layout 1 | `da749b0343c7`  |
| 2295   | Layout 1 | `da749b0343c7`  |
| 2290   | Layout 1 | `da749b0343c7`  |
| 2284   | Layout 1 | `da749b0343c7`  |
| 2276   | Layout 1 | `da749b0343c7`  |
| 2269   | Layout 1 | `da749b0343c7`  |
| 2259   | Layout 1 | `da749b0343c7`  |
| 2250   | Layout 1 | `da749b0343c7`  |
| 2243   | Layout 1 | `da749b0343c7`  |
| 2235   | Layout 1 | `da749b0343c7`  |
| 2229   | Layout 1 | `da749b0343c7`  |
| 2224   | Layout 1 | `da749b0343c7`  |
| 2218   | Layout 1 | `da749b0343c7`  |
| 2215   | Layout 1 | `da749b0343c7`  |
| 2207   | Layout 1 | `da749b0343c7`  |
| 2203   | Layout 1 | `da749b0343c7`  |
| 2196   | Layout 1 | `da749b0343c7`  |
| 2192   | Layout 1 | `da749b0343c7`  |
| 2189   | Layout 1 | `da749b0343c7`  |
| 2183   | Layout 1 | `da749b0343c7`  |
| 2179   | Layout 1 | `da749b0343c7`  |
| 2171   | Layout 1 | `da749b0343c7`  |
| 2163   | Layout 1 | `da749b0343c7`  |
| 2156   | Layout 1 | `da749b0343c7`  |
| 2151   | Layout 1 | `da749b0343c7`  |
| 2147   | Layout 1 | `da749b0343c7`  |
| 2142   | Layout 1 | `da749b0343c7`  |
| 2138   | Layout 1 | `da749b0343c7`  |
| 2134   | Layout 1 | `da749b0343c7`  |
| 2130   | Layout 1 | `da749b0343c7`  |
| 2122   | Layout 1 | `da749b0343c7`  |
| 2107   | Layout 1 | `da749b0343c7`  |
| 2098   | Layout 1 | `da749b0343c7`  |
| 2089   | Layout 1 | `da749b0343c7`  |
| 2081   | Layout 1 | `da749b0343c7`  |
| 2073   | Layout 1 | `da749b0343c7`  |
| 2067   | Layout 1 | `da749b0343c7`  |
| 2063   | Layout 1 | `da749b0343c7`  |
| 2059   | Layout 1 | `da749b0343c7`  |
| 2052   | Layout 1 | `da749b0343c7`  |
| 2044   | Layout 1 | `da749b0343c7`  |
| 2039   | Layout 1 | `da749b0343c7`  |
| 2032   | Layout 1 | `da749b0343c7`  |
| 2025   | Layout 1 | `da749b0343c7`  |
| 2011   | Layout 1 | `da749b0343c7`  |
| 2005   | Layout 1 | `da749b0343c7`  |
| 2000   | Layout 1 | `da749b0343c7`  |
| 1996   | Layout 1 | `da749b0343c7`  |
| 1991   | Layout 1 | `da749b0343c7`  |
| 1985   | Layout 1 | `da749b0343c7`  |
| 1980   | Layout 1 | `da749b0343c7`  |
| 1969   | Layout 1 | `da749b0343c7`  |
| 1964   | Layout 1 | `da749b0343c7`  |
| 1958   | Layout 1 | `da749b0343c7`  |
| 1950   | Layout 1 | `da749b0343c7`  |
| 1945   | Layout 1 | `da749b0343c7`  |
| 1937   | Layout 1 | `da749b0343c7`  |
| 1933   | Layout 1 | `da749b0343c7`  |
| 1927   | Layout 1 | `da749b0343c7`  |
| 1921   | Layout 1 | `da749b0343c7`  |
| 1914   | Layout 1 | `da749b0343c7`  |
| 1908   | Layout 1 | `da749b0343c7`  |
| 1897   | Layout 1 | `da749b0343c7`  |
| 1892   | Layout 1 | `da749b0343c7`  |
| 1886   | Layout 1 | `da749b0343c7`  |
| 1881   | Layout 1 | `da749b0343c7`  |
| 1871   | Layout 1 | `da749b0343c7`  |
| 1866   | Layout 1 | `da749b0343c7`  |
| 1862   | Layout 1 | `da749b0343c7`  |
| 1854   | Layout 1 | `da749b0343c7`  |
| 1846   | Layout 1 | `da749b0343c7`  |
| 1838   | Layout 1 | `da749b0343c7`  |
| 1832   | Layout 1 | `da749b0343c7`  |
| 1826   | Layout 1 | `da749b0343c7`  |
| 1822   | Layout 1 | `da749b0343c7`  |
| 1818   | Layout 1 | `da749b0343c7`  |
| 1804   | Layout 1 | `da749b0343c7`  |
| 1794   | Layout 1 | `da749b0343c7`  |
| 1790   | Layout 1 | `da749b0343c7`  |
| 1784   | Layout 1 | `da749b0343c7`  |
| 1774   | Layout 1 | `da749b0343c7`  |
| 1771   | Layout 1 | `da749b0343c7`  |
| 1762   | Layout 1 | `da749b0343c7`  |
| 1759   | Layout 1 | `da749b0343c7`  |
| 1754   | Layout 1 | `da749b0343c7`  |
| 1749   | Layout 1 | `da749b0343c7`  |
| 1743   | Layout 1 | `da749b0343c7`  |
| 1737   | Layout 1 | `da749b0343c7`  |
| 1731   | Layout 1 | `da749b0343c7`  |
| 1725   | Layout 1 | `da749b0343c7`  |
| 1717   | Layout 1 | `da749b0343c7`  |
| 1710   | Layout 1 | `da749b0343c7`  |
| 1704   | Layout 1 | `da749b0343c7`  |
| 1698   | Layout 1 | `da749b0343c7`  |
| 1690   | Layout 1 | `da749b0343c7`  |
| 1685   | Layout 1 | `da749b0343c7`  |
| 1680   | Layout 1 | `da749b0343c7`  |
| 1674   | Layout 1 | `da749b0343c7`  |
| 1668   | Layout 1 | `da749b0343c7`  |
| 1659   | Layout 1 | `da749b0343c7`  |
| 1649   | Layout 1 | `da749b0343c7`  |
| 1642   | Layout 1 | `da749b0343c7`  |
| 1636   | Layout 1 | `da749b0343c7`  |
| 1628   | Layout 1 | `da749b0343c7`  |
| 1622   | Layout 1 | `da749b0343c7`  |
| 1614   | Layout 1 | `da749b0343c7`  |
| 1608   | Layout 1 | `da749b0343c7`  |
| 1602   | Layout 1 | `da749b0343c7`  |
| 1598   | Layout 1 | `da749b0343c7`  |
| 1594   | Layout 1 | `da749b0343c7`  |
| 1590   | Layout 1 | `da749b0343c7`  |
| 1587   | Layout 1 | `da749b0343c7`  |
| 1584   | Layout 1 | `da749b0343c7`  |
| 1579   | Layout 1 | `da749b0343c7`  |
| 1572   | Layout 1 | `da749b0343c7`  |
| 1565   | Layout 1 | `da749b0343c7`  |
| 1559   | Layout 1 | `da749b0343c7`  |
| 1554   | Layout 1 | `da749b0343c7`  |
| 1547   | Layout 1 | `da749b0343c7`  |
| 1537   | Layout 1 | `da749b0343c7`  |
| 1529   | Layout 1 | `da749b0343c7`  |
| 1524   | Layout 1 | `da749b0343c7`  |
| 1519   | Layout 1 | `da749b0343c7`  |
| 1509   | Layout 1 | `da749b0343c7`  |
| 1506   | Layout 1 | `da749b0343c7`  |
| 1504   | Layout 1 | `da749b0343c7`  |
| 1500   | Layout 1 | `da749b0343c7`  |
| 1493   | Layout 1 | `da749b0343c7`  |
| 1489   | Layout 1 | `da749b0343c7`  |
| 1485   | Layout 1 | `da749b0343c7`  |
| 1481   | Layout 1 | `da749b0343c7`  |
| 1474   | Layout 1 | `da749b0343c7`  |
| 1466   | Layout 1 | `da749b0343c7`  |
| 1462   | Layout 1 | `da749b0343c7`  |
| 1459   | Layout 1 | `da749b0343c7`  |
| 1453   | Layout 1 | `da749b0343c7`  |
| 1450   | Layout 1 | `da749b0343c7`  |
| 1445   | Layout 1 | `da749b0343c7`  |
| 1439   | Layout 1 | `da749b0343c7`  |
| 1433   | Layout 1 | `da749b0343c7`  |
| 1430   | Layout 1 | `da749b0343c7`  |
| 1426   | Layout 1 | `da749b0343c7`  |
| 1421   | Layout 1 | `da749b0343c7`  |
| 1417   | Layout 1 | `da749b0343c7`  |
| 1416   | Layout 1 | `da749b0343c7`  |
| 1409   | Layout 1 | `da749b0343c7`  |
| 1405   | Layout 1 | `da749b0343c7`  |
| 1401   | Layout 1 | `da749b0343c7`  |
| 1396   | Layout 1 | `da749b0343c7`  |
| 1391   | Layout 1 | `da749b0343c7`  |
| 1390   | Layout 1 | `da749b0343c7`  |
| 1386   | Layout 1 | `da749b0343c7`  |
| 1381   | Layout 1 | `da749b0343c7`  |
| 1379   | Layout 1 | `da749b0343c7`  |
| 1372   | Layout 1 | `da749b0343c7`  |
| 1366   | Layout 1 | `da749b0343c7`  |
| 1364   | Layout 1 | `da749b0343c7`  |
| 1363   | Layout 1 | `da749b0343c7`  |
| 1360   | Layout 1 | `da749b0343c7`  |
| 1358   | Layout 1 | `da749b0343c7`  |
| 1355   | Layout 1 | `da749b0343c7`  |
| 1351   | Layout 1 | `da749b0343c7`  |
| 1348   | Layout 1 | `da749b0343c7`  |
| 1346   | Layout 1 | `da749b0343c7`  |
| 1341   | Layout 1 | `da749b0343c7`  |
| 1340   | Layout 1 | `da749b0343c7`  |
| 1338   | Layout 1 | `da749b0343c7`  |
| 1335   | Layout 1 | `da749b0343c7`  |
| 1333   | Layout 1 | `da749b0343c7`  |
| 1329   | Layout 1 | `da749b0343c7`  |
| 1327   | Layout 1 | `da749b0343c7`  |
| 1324   | Layout 1 | `da749b0343c7`  |
| 1321   | Layout 1 | `da749b0343c7`  |
| 1319   | Layout 1 | `da749b0343c7`  |
| 1318   | Layout 1 | `da749b0343c7`  |
| 1316   | Layout 1 | `da749b0343c7`  |
| 1313   | Layout 1 | `da749b0343c7`  |
| 1311   | Layout 1 | `da749b0343c7`  |
| 1309   | Layout 1 | `da749b0343c7`  |
| 1304   | Layout 1 | `da749b0343c7`  |
| 1292   | Layout 1 | `da749b0343c7`  |
| 1286   | No file  | `da749b0343c7`  |
| 1280   | No file  | `da749b0343c7`  |
| 1276   | No file  | `da749b0343c7`  |
| 1267   | No file  | `da749b0343c7`  |
| 1261   | No file  | `da749b0343c7`  |
| 1256   | No file  | `da749b0343c7`  |
| 1250   | No file  | `da749b0343c7`  |
| 1246   | No file  | `da749b0343c7`  |
| 1239   | No file  | `da749b0343c7`  |
| 1230   | No file  | `da749b0343c7`  |
| 1226   | No file  | `da749b0343c7`  |
| 1220   | No file  | `da749b0343c7`  |
| 1217   | No file  | `da749b0343c7`  |
| 1211   | No file  | `da749b0343c7`  |
| 1210   | No file  | `da749b0343c7`  |
| 1208   | No file  | `da749b0343c7`  |
| 1203   | No file  | `da749b0343c7`  |
| 1197   | No file  | `da749b0343c7`  |
| 1194   | No file  | `da749b0343c7`  |
| 1192   | No file  | `da749b0343c7`  |
| 1187   | No file  | `da749b0343c7`  |
| 1183   | No file  | `da749b0343c7`  |
| 1177   | No file  | `da749b0343c7`  |
| 1173   | No file  | `da749b0343c7`  |
| 1167   | No file  | `da749b0343c7`  |
| 1164   | No file  | `da749b0343c7`  |
| 1156   | No file  | `da749b0343c7`  |
| 1149   | No file  | `da749b0343c7`  |
| 1144   | No file  | `da749b0343c7`  |
| 1137   | No file  | `da749b0343c7`  |
| 1132   | No file  | `da749b0343c7`  |
| 1127   | No file  | `da749b0343c7`  |
| 1122   | No file  | `da749b0343c7`  |
| 1118   | No file  | `da749b0343c7`  |
| 1114   | No file  | `da749b0343c7`  |
| 1109   | No file  | `da749b0343c7`  |
| 1102   | No file  | `da749b0343c7`  |
| 1096   | No file  | `da749b0343c7`  |
| 1088   | No file  | `da749b0343c7`  |
| 1081   | No file  | `da749b0343c7`  |
| 1076   | No file  | `da749b0343c7`  |
| 1069   | No file  | `da749b0343c7`  |
| 1064   | No file  | `da749b0343c7`  |
| 1058   | No file  | `da749b0343c7`  |
| 1051   | No file  | `da749b0343c7`  |
| 1044   | No file  | `da749b0343c7`  |
| 1036   | No file  | `da749b0343c7`  |
| 1026   | No file  | `da749b0343c7`  |
| 1016   | No file  | `da749b0343c7`  |
| 1009   | No file  | `da749b0343c7`  |
| 1005   | No file  | `da749b0343c7`  |
| 1000   | No file  | `da749b0343c7`  |
| 998    | No file  | `da749b0343c7`  |
| 990    | No file  | `da749b0343c7`  |
| 979    | No file  | `da749b0343c7`  |
| 972    | No file  | `da749b0343c7`  |
| 963    | No file  | `da749b0343c7`  |
| 955    | No file  | `da749b0343c7`  |
| 946    | No file  | `da749b0343c7`  |
| 938    | No file  | `da749b0343c7`  |
| 927    | No file  | `da749b0343c7`  |
| 911    | No file  | `da749b0343c7`  |
| 904    | No file  | `da749b0343c7`  |
| 899    | No file  | `da749b0343c7`  |
| 894    | No file  | `da749b0343c7`  |
| 885    | No file  | `da749b0343c7`  |
| 879    | No file  | `da749b0343c7`  |
| 872    | No file  | `da749b0343c7`  |
| 864    | No file  | `da749b0343c7`  |
| 855    | No file  | `da749b0343c7`  |
| 853    | No file  | `da749b0343c7`  |
| 845    | No file  | `da749b0343c7`  |
| 837    | No file  | `da749b0343c7`  |
| 829    | No file  | `da749b0343c7`  |
| 822    | No file  | `da749b0343c7`  |
| 814    | No file  | `da749b0343c7`  |
| 805    | No file  | `da749b0343c7`  |
| 794    | No file  | `da749b0343c7`  |
| 787    | No file  | `da749b0343c7`  |
| 780    | No file  | `da749b0343c7`  |
| 771    | No file  | `da749b0343c7`  |
| 760    | No file  | `da749b0343c7`  |
| 748    | No file  | `da749b0343c7`  |
| 741    | No file  | `da749b0343c7`  |
| 736    | No file  | `da749b0343c7`  |
| 731    | No file  | `da749b0343c7`  |
| 723    | No file  | `da749b0343c7`  |
| 711    | No file  | `da749b0343c7`  |
| 707    | No file  | `da749b0343c7`  |
| 697    | No file  | `da749b0343c7`  |
| 689    | No file  | `da749b0343c7`  |
| 683    | No file  | `da749b0343c7`  |
| 678    | No file  | `da749b0343c7`  |
| 670    | No file  | `da749b0343c7`  |
| 661    | No file  | `da749b0343c7`  |
| 656    | No file  | `da749b0343c7`  |
| 652    | No file  | `da749b0343c7`  |
| 643    | No file  | `da749b0343c7`  |
| 637    | No file  | `da749b0343c7`  |
| 630    | No file  | `da749b0343c7`  |
| 627    | No file  | `da749b0343c7`  |
| 621    | No file  | `da749b0343c7`  |
| 617    | No file  | `da749b0343c7`  |
| 615    | No file  | `da749b0343c7`  |
| 606    | No file  | `da749b0343c7`  |
| 599    | No file  | `da749b0343c7`  |
| 592    | No file  | `da749b0343c7`  |
| 586    | No file  | `da749b0343c7`  |
| 577    | No file  | `da749b0343c7`  |
| 569    | No file  | `da749b0343c7`  |
| 561    | No file  | `da749b0343c7`  |
| 554    | No file  | `da749b0343c7`  |
| 542    | No file  | `da749b0343c7`  |
| 532    | No file  | `da749b0343c7`  |
| 531    | No file  | `da749b0343c7`  |
| 526    | No file  | `da749b0343c7`  |
| 521    | No file  | `da749b0343c7`  |
| 517    | No file  | `da749b0343c7`  |
| 510    | No file  | `da749b0343c7`  |
| 508    | No file  | `da749b0343c7`  |
| 504    | No file  | `da749b0343c7`  |
| 497    | No file  | `da749b0343c7`  |
| 491    | No file  | `da749b0343c7`  |
| 485    | No file  | `da749b0343c7`  |
| 478    | No file  | `da749b0343c7`  |
| 472    | No file  | `da749b0343c7`  |
| 466    | No file  | `da749b0343c7`  |
| 457    | No file  | `da749b0343c7`  |
| 452    | No file  | `da749b0343c7`  |
| 449    | No file  | `da749b0343c7`  |
| 435    | No file  | `da749b0343c7`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                                 |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `houseinfoviewpositionoffset.dbss` | Optional | `(character_key, house_group_type) -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinfo.bss`                    | Optional | The node house rows, for the House link and the Town column                          |
| `guildhouseinfo.dbss`              | Optional | The guild house rows, for the House link and the Town column                         |
| `languagedata_en.loc`              | Optional | House names (type 6) and town names (type 17)                                        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                    |
| ----------- | ---------- | ------------ | ---------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                   |
| `+0x04`     | u32        | count        | Number of rows; 84 on client 3482        |
| `+0x08`     | Row[count] | rows         | See Row                                  |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table         |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 32 * count`)       |
| `rows+0x08` | u32        | zero         | Always `0`                               |

### Row (32 bytes)

| Offset  | Type   | Field            | Notes                                                                       |
| ------- | ------ | ---------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16    | character_key    | The house, a `characterstatic.dbss` key; with `house_group_type` the row key |
| `+0x02` | i16    | padding_02       | The 2016 PDB key member `_reserve`; `0` on every row (clients 1784 and 3482) |
| `+0x04` | u32    | house_group_type | A `CppEnums.eHouseUseType` value; see House Use Types                       |
| `+0x08` | f32[3] | position         | World position x, y, z; `0, 0, 0` on the 19 Ranch rows (client 3482)       |
| `+0x14` | f32[3] | direction        | Facing as a unit vector `(-sin yaw, 0, -cos yaw)`, yaw in degrees           |

Every (`character_key`, `house_group_type`) pair is unique. The rows are
in no key order.

### `houseinfoviewpositionoffset.dbss`

Bare offset table into `houseinfoviewposition.dbss` (no PABR magic, no
trailer), keyed by the same 8 bytes the row starts with.

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `houseinfoviewposition.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                |

### Offset Row (16 bytes)

| Offset  | Type | Field            | Notes                                                       |
| ------- | ---- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key    | Key of the row it points at                                 |
| `+0x02` | i16  | padding_02       | The 2016 PDB key member `_reserve`; `0` on every row        |
| `+0x04` | u32  | house_group_type | Key of the row it points at                                 |
| `+0x08` | u32  | data_offset      | Absolute offset of the row in `houseinfoviewposition.dbss`, at `character_key` |
| `+0x0C` | u32  | data_size        | `32` on every row: the whole row                            |

The index rows are in another order than the file; on clients 1784 and 3482 every index row
points at the row with its key.

## House Use Types

`house_group_type` takes values of `CppEnums.eHouseUseType`
(`global_define_cpp_enum.luac`), the enum of the `house_use_type` field of
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md).

| Value | `eHouseUseType`    | Rows (client 3482) |
| ----- | ------------------ | ------------------ |
| `3`   | `Ranch`            | 19                 |
| `12`  | `CannonWorkshop`   | 11                 |
| `13`  | `Shipyard`         | 34                 |
| `14`  | `CarriageWorkshop` | 20                 |

On client 3482, 68 of the 84 rows belong to a house with a use of that
`house_use_type`: a Shipyard row (`13`) sits on a house with a Shipyard or
Guild Shipyard use, a CarriageWorkshop row (`14`) on a house with a Wagon
Workshop use. The other 16 are the 11 CannonWorkshop rows, the Ranch row of
house `2246` and the CarriageWorkshop rows of the four guild houses `2110`,
`2140`, `2880` and `2905`; none of those houses has a use of that type.

## Field Names

The `HouseViewPostion` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `TerritoryKey`, `HouseKey`, `HouseGroupType`,
`position` and `rotationYaw`. The 2016 `gc::HouseInfoViewPositionStaticStatus`
holds `_position`, `_direction` and the 8-byte key
`gc::HouseInfoViewPositionKey` (`_characterKey`, `_reserve`,
`_housegrouptype`); the client stores the key first.

| Field            | Column / member                          | Same value (client 1784) |
| ---------------- | ---------------------------------------- | ------------------------ |
| character_key    | `HouseKey`                               | 76 of 76                 |
| house_group_type | `HouseGroupType`                         | 76 of 76                 |
| position         | `position`                               | 76 of 76                 |
| direction        | `rotationYaw`, as `(-sin, 0, -cos)`      | 76 of 76                 |

`padding_02` is the 2016 key's `_reserve` member, `0` on every row.
`TerritoryKey` (`0` to `8`) has no field: the client file leaves it out.

## Notes

- The direction is the sheet's `rotationYaw` in degrees turned into a
  vector: yaw `84` gives `(-0.9945, 0, -0.1045)`, yaw `0` gives `(0, 0, -1)`.
  The view shows the yaw back in degrees.
- The four rows of each Valencia guild house group (`3355` to `3358`, and
  `3351` to `3354`) share one position and direction per use type.
- No Lua file of client 3482 calls a getter for this table.
