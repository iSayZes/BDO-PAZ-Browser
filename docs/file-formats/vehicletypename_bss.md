# `vehicletypename.bss` Format

## Purpose

The vehicle type name of each rideable character that is not a plain
servant: siege weapons, ships, monsters a player rides, event mounts. Per
character key the file gives a type name such as `MonsterRideOgre` or
`NationCannon`. The names are the `VehicleTypeName` keys of the
`PcActionVehicle_Table` sheet, which lists the player action chart of each
class for each vehicle type (68 of the 69 names of client 1784 are
`PcActionVehicle_Table` rows on that client).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 1109 and later | 3483    | `vehicletypename.bss` | 3,043 | 112 Row | 8         |

| Layout | File                  | Known            | Unknown    |
| ------ | --------------------- | ---------------- | ---------- |
| 1      | `vehicletypename.bss` | 3,043 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `96a842568da3`  |
| 3482   | Layout 1 | `96a842568da3`  |
| 3474   | Layout 1 | `96a842568da3`  |
| 3473   | Layout 1 | `96a842568da3`  |
| 3464   | Layout 1 | `96a842568da3`  |
| 3458   | Layout 1 | `96a842568da3`  |
| 3454   | Layout 1 | `96a842568da3`  |
| 3444   | Layout 1 | `96a842568da3`  |
| 3435   | Layout 1 | `96a842568da3`  |
| 3426   | Layout 1 | `96a842568da3`  |
| 3418   | Layout 1 | `96a842568da3`  |
| 3412   | Layout 1 | `96a842568da3`  |
| 3402   | Layout 1 | `96a842568da3`  |
| 3396   | Layout 1 | `96a842568da3`  |
| 3387   | Layout 1 | `96a842568da3`  |
| 3381   | Layout 1 | `96a842568da3`  |
| 3373   | Layout 1 | `96a842568da3`  |
| 3364   | Layout 1 | `96a842568da3`  |
| 3356   | Layout 1 | `96a842568da3`  |
| 3349   | Layout 1 | `96a842568da3`  |
| 3342   | Layout 1 | `96a842568da3`  |
| 3335   | Layout 1 | `96a842568da3`  |
| 3326   | Layout 1 | `96a842568da3`  |
| 3321   | Layout 1 | `96a842568da3`  |
| 3314   | Layout 1 | `96a842568da3`  |
| 3303   | Layout 1 | `96a842568da3`  |
| 3302   | Layout 1 | `96a842568da3`  |
| 3293   | Layout 1 | `96a842568da3`  |
| 3283   | Layout 1 | `96a842568da3`  |
| 3275   | Layout 1 | `96a842568da3`  |
| 3267   | Layout 1 | `96a842568da3`  |
| 3258   | Layout 1 | `96a842568da3`  |
| 3251   | Layout 1 | `96a842568da3`  |
| 3242   | Layout 1 | `96a842568da3`  |
| 3235   | Layout 1 | `96a842568da3`  |
| 3229   | Layout 1 | `96a842568da3`  |
| 3212   | Layout 1 | `96a842568da3`  |
| 3203   | Layout 1 | `96a842568da3`  |
| 3193   | Layout 1 | `96a842568da3`  |
| 3186   | Layout 1 | `96a842568da3`  |
| 3177   | Layout 1 | `96a842568da3`  |
| 3169   | Layout 1 | `96a842568da3`  |
| 3158   | Layout 1 | `96a842568da3`  |
| 3151   | Layout 1 | `96a842568da3`  |
| 3144   | Layout 1 | `96a842568da3`  |
| 3133   | Layout 1 | `96a842568da3`  |
| 3125   | Layout 1 | `96a842568da3`  |
| 3118   | Layout 1 | `96a842568da3`  |
| 3111   | Layout 1 | `96a842568da3`  |
| 3103   | Layout 1 | `96a842568da3`  |
| 3095   | Layout 1 | `96a842568da3`  |
| 3086   | Layout 1 | `96a842568da3`  |
| 3072   | Layout 1 | `96a842568da3`  |
| 3062   | Layout 1 | `96a842568da3`  |
| 3052   | Layout 1 | `96a842568da3`  |
| 3045   | Layout 1 | `96a842568da3`  |
| 3037   | Layout 1 | `96a842568da3`  |
| 3030   | Layout 1 | `96a842568da3`  |
| 3021   | Layout 1 | `96a842568da3`  |
| 3012   | Layout 1 | `96a842568da3`  |
| 3002   | Layout 1 | `96a842568da3`  |
| 2995   | Layout 1 | `96a842568da3`  |
| 2987   | Layout 1 | `96a842568da3`  |
| 2978   | Layout 1 | `96a842568da3`  |
| 2970   | Layout 1 | `96a842568da3`  |
| 2959   | Layout 1 | `96a842568da3`  |
| 2951   | Layout 1 | `96a842568da3`  |
| 2942   | Layout 1 | `96a842568da3`  |
| 2935   | Layout 1 | `96a842568da3`  |
| 2932   | Layout 1 | `96a842568da3`  |
| 2923   | Layout 1 | `96a842568da3`  |
| 2919   | Layout 1 | `96a842568da3`  |
| 2907   | Layout 1 | `96a842568da3`  |
| 2900   | Layout 1 | `96a842568da3`  |
| 2891   | Layout 1 | `96a842568da3`  |
| 2882   | Layout 1 | `96a842568da3`  |
| 2872   | Layout 1 | `96a842568da3`  |
| 2863   | Layout 1 | `96a842568da3`  |
| 2855   | Layout 1 | `96a842568da3`  |
| 2849   | Layout 1 | `96a842568da3`  |
| 2844   | Layout 1 | `96a842568da3`  |
| 2834   | Layout 1 | `96a842568da3`  |
| 2825   | Layout 1 | `96a842568da3`  |
| 2819   | Layout 1 | `96a842568da3`  |
| 2811   | Layout 1 | `96a842568da3`  |
| 2803   | Layout 1 | `96a842568da3`  |
| 2794   | Layout 1 | `96a842568da3`  |
| 2783   | Layout 1 | `96a842568da3`  |
| 2774   | Layout 1 | `96a842568da3`  |
| 2765   | Layout 1 | `96a842568da3`  |
| 2756   | Layout 1 | `96a842568da3`  |
| 2750   | Layout 1 | `96a842568da3`  |
| 2743   | Layout 1 | `96a842568da3`  |
| 2736   | Layout 1 | `96a842568da3`  |
| 2726   | Layout 1 | `96a842568da3`  |
| 2717   | Layout 1 | `96a842568da3`  |
| 2709   | Layout 1 | `96a842568da3`  |
| 2703   | Layout 1 | `96a842568da3`  |
| 2695   | Layout 1 | `96a842568da3`  |
| 2684   | Layout 1 | `96a842568da3`  |
| 2672   | Layout 1 | `96a842568da3`  |
| 2665   | Layout 1 | `96a842568da3`  |
| 2657   | Layout 1 | `96a842568da3`  |
| 2649   | Layout 1 | `96a842568da3`  |
| 2644   | Layout 1 | `96a842568da3`  |
| 2637   | Layout 1 | `96a842568da3`  |
| 2629   | Layout 1 | `96a842568da3`  |
| 2619   | Layout 1 | `96a842568da3`  |
| 2612   | Layout 1 | `96a842568da3`  |
| 2606   | Layout 1 | `96a842568da3`  |
| 2602   | Layout 1 | `96a842568da3`  |
| 2601   | Layout 1 | `96a842568da3`  |
| 2592   | Layout 1 | `96a842568da3`  |
| 2583   | Layout 1 | `96a842568da3`  |
| 2575   | Layout 1 | `96a842568da3`  |
| 2567   | Layout 1 | `96a842568da3`  |
| 2560   | Layout 1 | `96a842568da3`  |
| 2553   | Layout 1 | `96a842568da3`  |
| 2545   | Layout 1 | `96a842568da3`  |
| 2538   | Layout 1 | `96a842568da3`  |
| 2529   | Layout 1 | `96a842568da3`  |
| 2519   | Layout 1 | `96a842568da3`  |
| 2513   | Layout 1 | `96a842568da3`  |
| 2510   | Layout 1 | `96a842568da3`  |
| 2507   | Layout 1 | `96a842568da3`  |
| 2503   | Layout 1 | `96a842568da3`  |
| 2498   | Layout 1 | `96a842568da3`  |
| 2492   | Layout 1 | `96a842568da3`  |
| 2487   | Layout 1 | `96a842568da3`  |
| 2480   | Layout 1 | `96a842568da3`  |
| 2474   | Layout 1 | `96a842568da3`  |
| 2468   | Layout 1 | `96a842568da3`  |
| 2460   | Layout 1 | `96a842568da3`  |
| 2453   | Layout 1 | `96a842568da3`  |
| 2444   | Layout 1 | `96a842568da3`  |
| 2438   | Layout 1 | `96a842568da3`  |
| 2434   | Layout 1 | `96a842568da3`  |
| 2429   | Layout 1 | `96a842568da3`  |
| 2421   | Layout 1 | `96a842568da3`  |
| 2414   | Layout 1 | `96a842568da3`  |
| 2407   | Layout 1 | `96a842568da3`  |
| 2401   | Layout 1 | `96a842568da3`  |
| 2397   | Layout 1 | `96a842568da3`  |
| 2393   | Layout 1 | `96a842568da3`  |
| 2384   | Layout 1 | `96a842568da3`  |
| 2378   | Layout 1 | `96a842568da3`  |
| 2372   | Layout 1 | `96a842568da3`  |
| 2358   | Layout 1 | `96a842568da3`  |
| 2352   | Layout 1 | `96a842568da3`  |
| 2347   | Layout 1 | `96a842568da3`  |
| 2343   | Layout 1 | `96a842568da3`  |
| 2335   | Layout 1 | `96a842568da3`  |
| 2327   | Layout 1 | `96a842568da3`  |
| 2324   | Layout 1 | `96a842568da3`  |
| 2319   | Layout 1 | `96a842568da3`  |
| 2313   | Layout 1 | `96a842568da3`  |
| 2308   | Layout 1 | `96a842568da3`  |
| 2302   | Layout 1 | `96a842568da3`  |
| 2295   | Layout 1 | `96a842568da3`  |
| 2290   | Layout 1 | `96a842568da3`  |
| 2284   | Layout 1 | `96a842568da3`  |
| 2276   | Layout 1 | `96a842568da3`  |
| 2269   | Layout 1 | `96a842568da3`  |
| 2259   | Layout 1 | `96a842568da3`  |
| 2250   | Layout 1 | `96a842568da3`  |
| 2243   | Layout 1 | `96a842568da3`  |
| 2235   | Layout 1 | `96a842568da3`  |
| 2229   | Layout 1 | `96a842568da3`  |
| 2224   | Layout 1 | `96a842568da3`  |
| 2218   | Layout 1 | `96a842568da3`  |
| 2215   | Layout 1 | `96a842568da3`  |
| 2207   | Layout 1 | `96a842568da3`  |
| 2203   | Layout 1 | `96a842568da3`  |
| 2196   | Layout 1 | `96a842568da3`  |
| 2192   | Layout 1 | `96a842568da3`  |
| 2189   | Layout 1 | `96a842568da3`  |
| 2183   | Layout 1 | `96a842568da3`  |
| 2179   | Layout 1 | `96a842568da3`  |
| 2171   | Layout 1 | `96a842568da3`  |
| 2163   | Layout 1 | `96a842568da3`  |
| 2156   | Layout 1 | `96a842568da3`  |
| 2151   | Layout 1 | `96a842568da3`  |
| 2147   | Layout 1 | `96a842568da3`  |
| 2142   | Layout 1 | `96a842568da3`  |
| 2138   | Layout 1 | `96a842568da3`  |
| 2134   | Layout 1 | `96a842568da3`  |
| 2130   | Layout 1 | `96a842568da3`  |
| 2122   | Layout 1 | `96a842568da3`  |
| 2107   | Layout 1 | `96a842568da3`  |
| 2098   | Layout 1 | `96a842568da3`  |
| 2089   | Layout 1 | `96a842568da3`  |
| 2081   | Layout 1 | `96a842568da3`  |
| 2073   | Layout 1 | `96a842568da3`  |
| 2067   | Layout 1 | `96a842568da3`  |
| 2063   | Layout 1 | `96a842568da3`  |
| 2059   | Layout 1 | `96a842568da3`  |
| 2052   | Layout 1 | `96a842568da3`  |
| 2044   | Layout 1 | `96a842568da3`  |
| 2039   | Layout 1 | `96a842568da3`  |
| 2032   | Layout 1 | `96a842568da3`  |
| 2025   | Layout 1 | `96a842568da3`  |
| 2011   | Layout 1 | `96a842568da3`  |
| 2005   | Layout 1 | `96a842568da3`  |
| 2000   | Layout 1 | `96a842568da3`  |
| 1996   | Layout 1 | `96a842568da3`  |
| 1991   | Layout 1 | `96a842568da3`  |
| 1985   | Layout 1 | `96a842568da3`  |
| 1980   | Layout 1 | `96a842568da3`  |
| 1969   | Layout 1 | `96a842568da3`  |
| 1964   | Layout 1 | `96a842568da3`  |
| 1958   | Layout 1 | `96a842568da3`  |
| 1950   | Layout 1 | `96a842568da3`  |
| 1945   | Layout 1 | `96a842568da3`  |
| 1937   | Layout 1 | `96a842568da3`  |
| 1933   | Layout 1 | `96a842568da3`  |
| 1927   | Layout 1 | `96a842568da3`  |
| 1921   | Layout 1 | `96a842568da3`  |
| 1914   | Layout 1 | `96a842568da3`  |
| 1908   | Layout 1 | `96a842568da3`  |
| 1897   | Layout 1 | `96a842568da3`  |
| 1892   | Layout 1 | `96a842568da3`  |
| 1886   | Layout 1 | `96a842568da3`  |
| 1881   | Layout 1 | `96a842568da3`  |
| 1871   | Layout 1 | `96a842568da3`  |
| 1866   | Layout 1 | `96a842568da3`  |
| 1862   | Layout 1 | `96a842568da3`  |
| 1854   | Layout 1 | `96a842568da3`  |
| 1846   | Layout 1 | `96a842568da3`  |
| 1838   | Layout 1 | `96a842568da3`  |
| 1832   | Layout 1 | `96a842568da3`  |
| 1826   | Layout 1 | `96a842568da3`  |
| 1822   | Layout 1 | `96a842568da3`  |
| 1818   | Layout 1 | `96a842568da3`  |
| 1804   | Layout 1 | `96a842568da3`  |
| 1794   | Layout 1 | `96a842568da3`  |
| 1790   | Layout 1 | `96a842568da3`  |
| 1784   | Layout 1 | `96a842568da3`  |
| 1774   | Layout 1 | `96a842568da3`  |
| 1771   | Layout 1 | `96a842568da3`  |
| 1762   | Layout 1 | `96a842568da3`  |
| 1759   | Layout 1 | `96a842568da3`  |
| 1754   | Layout 1 | `96a842568da3`  |
| 1749   | Layout 1 | `96a842568da3`  |
| 1743   | Layout 1 | `96a842568da3`  |
| 1737   | Layout 1 | `96a842568da3`  |
| 1731   | Layout 1 | `96a842568da3`  |
| 1725   | Layout 1 | `96a842568da3`  |
| 1717   | Layout 1 | `96a842568da3`  |
| 1710   | Layout 1 | `96a842568da3`  |
| 1704   | Layout 1 | `96a842568da3`  |
| 1698   | Layout 1 | `96a842568da3`  |
| 1690   | Layout 1 | `96a842568da3`  |
| 1685   | Layout 1 | `96a842568da3`  |
| 1680   | Layout 1 | `96a842568da3`  |
| 1674   | Layout 1 | `96a842568da3`  |
| 1668   | Layout 1 | `96a842568da3`  |
| 1659   | Layout 1 | `96a842568da3`  |
| 1649   | Layout 1 | `96a842568da3`  |
| 1642   | Layout 1 | `96a842568da3`  |
| 1636   | Layout 1 | `96a842568da3`  |
| 1628   | Layout 1 | `96a842568da3`  |
| 1622   | Layout 1 | `96a842568da3`  |
| 1614   | Layout 1 | `96a842568da3`  |
| 1608   | Layout 1 | `96a842568da3`  |
| 1602   | Layout 1 | `96a842568da3`  |
| 1598   | Layout 1 | `96a842568da3`  |
| 1594   | Layout 1 | `96a842568da3`  |
| 1590   | Layout 1 | `96a842568da3`  |
| 1587   | Layout 1 | `96a842568da3`  |
| 1584   | Layout 1 | `96a842568da3`  |
| 1579   | Layout 1 | `96a842568da3`  |
| 1572   | Layout 1 | `96a842568da3`  |
| 1565   | Layout 1 | `96a842568da3`  |
| 1559   | Layout 1 | `96a842568da3`  |
| 1554   | Layout 1 | `96a842568da3`  |
| 1547   | Layout 1 | `96a842568da3`  |
| 1537   | Layout 1 | `96a842568da3`  |
| 1529   | Layout 1 | `96a842568da3`  |
| 1524   | Layout 1 | `96a842568da3`  |
| 1519   | Layout 1 | `96a842568da3`  |
| 1509   | Layout 1 | `96a842568da3`  |
| 1506   | Layout 1 | `96a842568da3`  |
| 1504   | Layout 1 | `96a842568da3`  |
| 1500   | Layout 1 | `96a842568da3`  |
| 1493   | Layout 1 | `96a842568da3`  |
| 1489   | Layout 1 | `96a842568da3`  |
| 1485   | Layout 1 | `96a842568da3`  |
| 1481   | Layout 1 | `96a842568da3`  |
| 1474   | Layout 1 | `96a842568da3`  |
| 1466   | Layout 1 | `96a842568da3`  |
| 1462   | Layout 1 | `96a842568da3`  |
| 1459   | Layout 1 | `96a842568da3`  |
| 1453   | Layout 1 | `96a842568da3`  |
| 1450   | Layout 1 | `96a842568da3`  |
| 1445   | Layout 1 | `96a842568da3`  |
| 1439   | Layout 1 | `96a842568da3`  |
| 1433   | Layout 1 | `96a842568da3`  |
| 1430   | Layout 1 | `96a842568da3`  |
| 1426   | Layout 1 | `96a842568da3`  |
| 1421   | Layout 1 | `96a842568da3`  |
| 1417   | Layout 1 | `96a842568da3`  |
| 1416   | Layout 1 | `96a842568da3`  |
| 1409   | Layout 1 | `96a842568da3`  |
| 1405   | Layout 1 | `96a842568da3`  |
| 1401   | Layout 1 | `96a842568da3`  |
| 1396   | Layout 1 | `96a842568da3`  |
| 1391   | Layout 1 | `96a842568da3`  |
| 1390   | Layout 1 | `96a842568da3`  |
| 1386   | Layout 1 | `96a842568da3`  |
| 1381   | Layout 1 | `96a842568da3`  |
| 1379   | Layout 1 | `96a842568da3`  |
| 1372   | Layout 1 | `96a842568da3`  |
| 1366   | Layout 1 | `96a842568da3`  |
| 1364   | Layout 1 | `96a842568da3`  |
| 1363   | Layout 1 | `96a842568da3`  |
| 1360   | Layout 1 | `96a842568da3`  |
| 1358   | Layout 1 | `96a842568da3`  |
| 1355   | Layout 1 | `96a842568da3`  |
| 1351   | Layout 1 | `96a842568da3`  |
| 1348   | Layout 1 | `96a842568da3`  |
| 1346   | Layout 1 | `96a842568da3`  |
| 1341   | Layout 1 | `96a842568da3`  |
| 1340   | Layout 1 | `96a842568da3`  |
| 1338   | Layout 1 | `96a842568da3`  |
| 1335   | Layout 1 | `96a842568da3`  |
| 1333   | Layout 1 | `96a842568da3`  |
| 1329   | Layout 1 | `96a842568da3`  |
| 1327   | Layout 1 | `96a842568da3`  |
| 1324   | Layout 1 | `96a842568da3`  |
| 1321   | Layout 1 | `96a842568da3`  |
| 1319   | Layout 1 | `96a842568da3`  |
| 1318   | Layout 1 | `96a842568da3`  |
| 1316   | Layout 1 | `96a842568da3`  |
| 1313   | Layout 1 | `96a842568da3`  |
| 1311   | Layout 1 | `96a842568da3`  |
| 1309   | Layout 1 | `96a842568da3`  |
| 1304   | Layout 1 | `96a842568da3`  |
| 1292   | Layout 1 | `96a842568da3`  |
| 1286   | Layout 1 | `96a842568da3`  |
| 1280   | Layout 1 | `96a842568da3`  |
| 1276   | Layout 1 | `96a842568da3`  |
| 1267   | Layout 1 | `96a842568da3`  |
| 1261   | Layout 1 | `96a842568da3`  |
| 1256   | Layout 1 | `96a842568da3`  |
| 1250   | Layout 1 | `96a842568da3`  |
| 1246   | Layout 1 | `96a842568da3`  |
| 1239   | Layout 1 | `96a842568da3`  |
| 1230   | Layout 1 | `96a842568da3`  |
| 1226   | Layout 1 | `96a842568da3`  |
| 1220   | Layout 1 | `96a842568da3`  |
| 1217   | Layout 1 | `96a842568da3`  |
| 1211   | Layout 1 | `96a842568da3`  |
| 1210   | Layout 1 | `96a842568da3`  |
| 1208   | Layout 1 | `96a842568da3`  |
| 1203   | Layout 1 | `96a842568da3`  |
| 1197   | Layout 1 | `96a842568da3`  |
| 1194   | Layout 1 | `96a842568da3`  |
| 1192   | Layout 1 | `96a842568da3`  |
| 1187   | Layout 1 | `96a842568da3`  |
| 1183   | Layout 1 | `96a842568da3`  |
| 1177   | Layout 1 | `96a842568da3`  |
| 1173   | Layout 1 | `96a842568da3`  |
| 1167   | Layout 1 | `96a842568da3`  |
| 1164   | Layout 1 | `96a842568da3`  |
| 1156   | Layout 1 | `96a842568da3`  |
| 1149   | Layout 1 | `96a842568da3`  |
| 1144   | Layout 1 | `96a842568da3`  |
| 1137   | Layout 1 | `96a842568da3`  |
| 1132   | Layout 1 | `96a842568da3`  |
| 1127   | Layout 1 | `96a842568da3`  |
| 1122   | Layout 1 | `96a842568da3`  |
| 1118   | Layout 1 | `96a842568da3`  |
| 1114   | Layout 1 | `96a842568da3`  |
| 1109   | Layout 1 | `96a842568da3`  |
| 1102   | No file  | `96a842568da3`  |
| 1096   | No file  | `96a842568da3`  |
| 1088   | No file  | `96a842568da3`  |
| 1081   | No file  | `96a842568da3`  |
| 1076   | No file  | `96a842568da3`  |
| 1069   | No file  | `96a842568da3`  |
| 1064   | No file  | `96a842568da3`  |
| 1058   | No file  | `96a842568da3`  |
| 1051   | No file  | `96a842568da3`  |
| 1044   | No file  | `96a842568da3`  |
| 1036   | No file  | `96a842568da3`  |
| 1026   | No file  | `96a842568da3`  |
| 1016   | No file  | `96a842568da3`  |
| 1009   | No file  | `96a842568da3`  |
| 1005   | No file  | `96a842568da3`  |
| 1000   | No file  | `96a842568da3`  |
| 998    | No file  | `96a842568da3`  |
| 990    | No file  | `96a842568da3`  |
| 979    | No file  | `96a842568da3`  |
| 972    | No file  | `96a842568da3`  |
| 963    | No file  | `96a842568da3`  |
| 955    | No file  | `96a842568da3`  |
| 946    | No file  | `96a842568da3`  |
| 938    | No file  | `96a842568da3`  |
| 927    | No file  | `96a842568da3`  |
| 911    | No file  | `96a842568da3`  |
| 904    | No file  | `96a842568da3`  |
| 899    | No file  | `96a842568da3`  |
| 894    | No file  | `96a842568da3`  |
| 885    | No file  | `96a842568da3`  |
| 879    | No file  | `96a842568da3`  |
| 872    | No file  | `96a842568da3`  |
| 864    | No file  | `96a842568da3`  |
| 855    | No file  | `96a842568da3`  |
| 853    | No file  | `96a842568da3`  |
| 845    | No file  | `96a842568da3`  |
| 837    | No file  | `96a842568da3`  |
| 829    | No file  | `96a842568da3`  |
| 822    | No file  | `96a842568da3`  |
| 814    | No file  | `96a842568da3`  |
| 805    | No file  | `96a842568da3`  |
| 794    | No file  | `96a842568da3`  |
| 787    | No file  | `96a842568da3`  |
| 780    | No file  | `96a842568da3`  |
| 771    | No file  | `96a842568da3`  |
| 760    | No file  | `96a842568da3`  |
| 748    | No file  | `96a842568da3`  |
| 741    | No file  | `96a842568da3`  |
| 736    | No file  | `96a842568da3`  |
| 731    | No file  | `96a842568da3`  |
| 723    | No file  | `96a842568da3`  |
| 711    | No file  | `96a842568da3`  |
| 707    | No file  | `96a842568da3`  |
| 697    | No file  | `96a842568da3`  |
| 689    | No file  | `96a842568da3`  |
| 683    | No file  | `96a842568da3`  |
| 678    | No file  | `96a842568da3`  |
| 670    | No file  | `96a842568da3`  |
| 661    | No file  | `96a842568da3`  |
| 656    | No file  | `96a842568da3`  |
| 652    | No file  | `96a842568da3`  |
| 643    | No file  | `96a842568da3`  |
| 637    | No file  | `96a842568da3`  |
| 630    | No file  | `96a842568da3`  |
| 627    | No file  | `96a842568da3`  |
| 621    | No file  | `96a842568da3`  |
| 617    | No file  | `96a842568da3`  |
| 615    | No file  | `96a842568da3`  |
| 606    | No file  | `96a842568da3`  |
| 599    | No file  | `96a842568da3`  |
| 592    | No file  | `96a842568da3`  |
| 586    | No file  | `96a842568da3`  |
| 577    | No file  | `96a842568da3`  |
| 569    | No file  | `96a842568da3`  |
| 561    | No file  | `96a842568da3`  |
| 554    | No file  | `96a842568da3`  |
| 542    | No file  | `96a842568da3`  |
| 532    | No file  | `96a842568da3`  |
| 531    | No file  | `96a842568da3`  |
| 526    | No file  | `96a842568da3`  |
| 521    | No file  | `96a842568da3`  |
| 517    | No file  | `96a842568da3`  |
| 510    | No file  | `96a842568da3`  |
| 508    | No file  | `96a842568da3`  |
| 504    | No file  | `96a842568da3`  |
| 497    | No file  | `96a842568da3`  |
| 491    | No file  | `96a842568da3`  |
| 485    | No file  | `96a842568da3`  |
| 478    | No file  | `96a842568da3`  |
| 472    | No file  | `96a842568da3`  |
| 466    | No file  | `96a842568da3`  |
| 457    | No file  | `96a842568da3`  |
| 452    | No file  | `96a842568da3`  |
| 449    | No file  | `96a842568da3`  |
| 435    | No file  | `96a842568da3`  |

<!-- versions:end -->

## Companion Files

None. The handler names each character with LOC type 6 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of characters                          |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field                 | Notes                                                        |
| ------- | ---- | --------------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | character_key         | Rideable character; unique per file                          |
| `+0x04` | u32  | vehicle_type_name_ref | String table index of its vehicle type name                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                           |
| `+0x04` | pstr[string_count] | strings      | UTF-8 type names, each once, in the order of the first row that uses it     |

## Type Names

Client 3482 has 112 rows and 90 names, client 1784 87 rows and 69 names.
Several characters share a name: `MonsterRideCrioBasic` is the name of 7
characters on client 3482, `MonsterRideOgre`, `MonsterRideTrolla`,
`MonsterRideTerrCrio` and `MonsterRideTerrCrio2` of 3 each.

12 character keys of client 3482 have no LOC type 6 name and no
`characterstatic.dbss` record: `31036` NationElephant, `31037`
NationCannon, `31038` NationSiegeLargeTower, `31039`
NationSiegeMiddleTower, `31042` NationGalleyShip, `31047` GaliotShip,
`29898` MonsterRideLandSpider, `31093` Alpaca2, `29128` MonsterRideDokev,
`31654` and `31655` CamaOstrich, `31656` Dragon2.

## Field Names

The names follow the `VehicleTypeName_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_actiondatatable.xlsm`: columns `CharacterKey` and
`VehicleTypeName`, 120 rows. All 87 rows of the client 1784 file match a
sheet row on both columns, and all 94 rows of the client 3482 file whose
key the sheet has (the sheet has none of the other 18 keys). The 33 sheet
rows the client 1784 file leaves out are mostly the `Monster_T_*` and
`MonsterRideAtoraxion*` rows. The `VehicleTypeName_Table` of a private
server on client 519 has the same columns and 4 rows (`31036`
NationElephant to `31039` NationSiegeMiddleTower), all 4 in the client
3482 file. The xlsm's `#VehicleTypeName` column (the servant kind, such as
`Elephant`) and `#이름` column (the Korean name) are not compiled.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/servant_tables.py`: the
  character key, its LOC name and the type name.
