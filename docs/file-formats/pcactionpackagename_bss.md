# `pcactionpackagename.bss` Format

## Purpose

The action chart package each player class loads for a held weapon, a
vehicle, a vehicle with a weapon and cutscenes. A package is a lower-case
path without extension, such as `pc/1_phm/fighteraction_onehandsword`
(Warrior, Longsword) or
`pc/vehicle/riding_ground/horse/fighteraction_ridinghorse` (Warrior on a
horse). On client 3483 the no-weapon packages of 33 classes are files
`character/binaryactionchart/<package>.paac`, such as
`character/binaryactionchart/pc/1_phm/fighteraction_noweapon.paac`; the
other packages have no file of their own. The file is a plain PABR table
with no row count: one block per class type, in class type order, then a
short list keyed by class type, then the PABR string table that holds every
path and vehicle type name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records                                                                                                | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------ | --------- |
| 2      | 3381 and later | 3483    | `pcactionpackagename.bss` | 548,981 | 11,640 Package Cell, 5,444 Vehicle Row, 11,543 Equip Vehicle List, 97 Class Block, 3 Class Package Row | 8         |
| 1      | 1774 to 1784   | 1784    | `pcactionpackagename.bss` | 362,622 | 7,626 Package Cell, 5,839 Vehicle Row, 7,544 Equip Vehicle List, 82 Class Block                        | 8         |

| Layout | File                      | Known              | Unknown    |
| ------ | ------------------------- | ------------------ | ---------- |
| 2      | `pcactionpackagename.bss` | 548,977 B (100.0%) | 4 B (0.0%) |
| 1      | `pcactionpackagename.bss` | 362,622 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `9655200fe39d`  |
| 3482   | Layout 2             | `9655200fe39d`  |
| 3474   | Layout 2             | `9655200fe39d`  |
| 3473   | Layout 2             | `9655200fe39d`  |
| 3464   | Layout 2             | `9655200fe39d`  |
| 3458   | Layout 2             | `9655200fe39d`  |
| 3454   | Layout 2             | `9655200fe39d`  |
| 3444   | Layout 2             | `9655200fe39d`  |
| 3435   | Layout 2             | `9655200fe39d`  |
| 3426   | Layout 2             | `9655200fe39d`  |
| 3418   | Layout 2             | `9655200fe39d`  |
| 3412   | Layout 2             | `9655200fe39d`  |
| 3402   | Layout 2             | `9655200fe39d`  |
| 3396   | Layout 2             | `9655200fe39d`  |
| 3387   | Layout 2             | `9655200fe39d`  |
| 3381   | Layout 2             | `9655200fe39d`  |
| 3373   | No documented layout | `9655200fe39d`  |
| 3364   | No documented layout | `9655200fe39d`  |
| 3356   | No documented layout | `9655200fe39d`  |
| 3349   | No documented layout | `9655200fe39d`  |
| 3342   | No documented layout | `9655200fe39d`  |
| 3335   | No documented layout | `9655200fe39d`  |
| 3326   | No documented layout | `9655200fe39d`  |
| 3321   | No documented layout | `9655200fe39d`  |
| 3314   | No documented layout | `9655200fe39d`  |
| 3303   | No documented layout | `9655200fe39d`  |
| 3302   | No documented layout | `9655200fe39d`  |
| 3293   | No documented layout | `9655200fe39d`  |
| 3283   | No documented layout | `9655200fe39d`  |
| 3275   | No documented layout | `9655200fe39d`  |
| 3267   | No documented layout | `9655200fe39d`  |
| 3258   | No documented layout | `9655200fe39d`  |
| 3251   | No documented layout | `9655200fe39d`  |
| 3242   | No documented layout | `9655200fe39d`  |
| 3235   | No documented layout | `9655200fe39d`  |
| 3229   | No documented layout | `9655200fe39d`  |
| 3212   | No documented layout | `9655200fe39d`  |
| 3203   | No documented layout | `9655200fe39d`  |
| 3193   | No documented layout | `9655200fe39d`  |
| 3186   | No documented layout | `9655200fe39d`  |
| 3177   | No documented layout | `9655200fe39d`  |
| 3169   | No documented layout | `9655200fe39d`  |
| 3158   | No documented layout | `9655200fe39d`  |
| 3151   | No documented layout | `9655200fe39d`  |
| 3144   | No documented layout | `9655200fe39d`  |
| 3133   | No documented layout | `9655200fe39d`  |
| 3125   | No documented layout | `9655200fe39d`  |
| 3118   | No documented layout | `9655200fe39d`  |
| 3111   | No documented layout | `9655200fe39d`  |
| 3103   | No documented layout | `9655200fe39d`  |
| 3095   | No documented layout | `9655200fe39d`  |
| 3086   | No documented layout | `9655200fe39d`  |
| 3072   | No documented layout | `9655200fe39d`  |
| 3062   | No documented layout | `9655200fe39d`  |
| 3052   | No documented layout | `9655200fe39d`  |
| 3045   | No documented layout | `9655200fe39d`  |
| 3037   | No documented layout | `9655200fe39d`  |
| 3030   | No documented layout | `9655200fe39d`  |
| 3021   | No documented layout | `9655200fe39d`  |
| 3012   | No documented layout | `9655200fe39d`  |
| 3002   | No documented layout | `9655200fe39d`  |
| 2995   | No documented layout | `9655200fe39d`  |
| 2987   | No documented layout | `9655200fe39d`  |
| 2978   | No documented layout | `9655200fe39d`  |
| 2970   | No documented layout | `9655200fe39d`  |
| 2959   | No documented layout | `9655200fe39d`  |
| 2951   | No documented layout | `9655200fe39d`  |
| 2942   | No documented layout | `9655200fe39d`  |
| 2935   | No documented layout | `9655200fe39d`  |
| 2932   | No documented layout | `9655200fe39d`  |
| 2923   | No documented layout | `9655200fe39d`  |
| 2919   | No documented layout | `9655200fe39d`  |
| 2907   | No documented layout | `9655200fe39d`  |
| 2900   | No documented layout | `9655200fe39d`  |
| 2891   | No documented layout | `9655200fe39d`  |
| 2882   | No documented layout | `9655200fe39d`  |
| 2872   | No documented layout | `9655200fe39d`  |
| 2863   | No documented layout | `9655200fe39d`  |
| 2855   | No documented layout | `9655200fe39d`  |
| 2849   | No documented layout | `9655200fe39d`  |
| 2844   | No documented layout | `9655200fe39d`  |
| 2834   | No documented layout | `9655200fe39d`  |
| 2825   | No documented layout | `9655200fe39d`  |
| 2819   | No documented layout | `9655200fe39d`  |
| 2811   | No documented layout | `9655200fe39d`  |
| 2803   | No documented layout | `9655200fe39d`  |
| 2794   | No documented layout | `9655200fe39d`  |
| 2783   | No documented layout | `9655200fe39d`  |
| 2774   | No documented layout | `9655200fe39d`  |
| 2765   | No documented layout | `9655200fe39d`  |
| 2756   | No documented layout | `9655200fe39d`  |
| 2750   | No documented layout | `9655200fe39d`  |
| 2743   | No documented layout | `9655200fe39d`  |
| 2736   | No documented layout | `9655200fe39d`  |
| 2726   | No documented layout | `9655200fe39d`  |
| 2717   | No documented layout | `9655200fe39d`  |
| 2709   | No documented layout | `9655200fe39d`  |
| 2703   | No documented layout | `9655200fe39d`  |
| 2695   | No documented layout | `9655200fe39d`  |
| 2684   | No documented layout | `9655200fe39d`  |
| 2672   | No documented layout | `9655200fe39d`  |
| 2665   | No documented layout | `9655200fe39d`  |
| 2657   | No documented layout | `9655200fe39d`  |
| 2649   | No documented layout | `9655200fe39d`  |
| 2644   | No documented layout | `9655200fe39d`  |
| 2637   | No documented layout | `9655200fe39d`  |
| 2629   | No documented layout | `9655200fe39d`  |
| 2619   | No documented layout | `9655200fe39d`  |
| 2612   | No documented layout | `9655200fe39d`  |
| 2606   | No documented layout | `9655200fe39d`  |
| 2602   | No documented layout | `9655200fe39d`  |
| 2601   | No documented layout | `9655200fe39d`  |
| 2592   | No documented layout | `9655200fe39d`  |
| 2583   | No documented layout | `9655200fe39d`  |
| 2575   | No documented layout | `9655200fe39d`  |
| 2567   | No documented layout | `9655200fe39d`  |
| 2560   | No documented layout | `9655200fe39d`  |
| 2553   | No documented layout | `9655200fe39d`  |
| 2545   | No documented layout | `9655200fe39d`  |
| 2538   | No documented layout | `9655200fe39d`  |
| 2529   | No documented layout | `9655200fe39d`  |
| 2519   | No documented layout | `9655200fe39d`  |
| 2513   | No documented layout | `9655200fe39d`  |
| 2510   | No documented layout | `9655200fe39d`  |
| 2507   | No documented layout | `9655200fe39d`  |
| 2503   | No documented layout | `9655200fe39d`  |
| 2498   | No documented layout | `9655200fe39d`  |
| 2492   | No documented layout | `9655200fe39d`  |
| 2487   | No documented layout | `9655200fe39d`  |
| 2480   | No documented layout | `9655200fe39d`  |
| 2474   | No documented layout | `9655200fe39d`  |
| 2468   | No documented layout | `9655200fe39d`  |
| 2460   | No documented layout | `9655200fe39d`  |
| 2453   | No documented layout | `9655200fe39d`  |
| 2444   | No documented layout | `9655200fe39d`  |
| 2438   | No documented layout | `9655200fe39d`  |
| 2434   | No documented layout | `9655200fe39d`  |
| 2429   | No documented layout | `9655200fe39d`  |
| 2421   | No documented layout | `9655200fe39d`  |
| 2414   | No documented layout | `9655200fe39d`  |
| 2407   | No documented layout | `9655200fe39d`  |
| 2401   | No documented layout | `9655200fe39d`  |
| 2397   | No documented layout | `9655200fe39d`  |
| 2393   | No documented layout | `9655200fe39d`  |
| 2384   | No documented layout | `9655200fe39d`  |
| 2378   | No documented layout | `9655200fe39d`  |
| 2372   | No documented layout | `9655200fe39d`  |
| 2358   | No documented layout | `9655200fe39d`  |
| 2352   | No documented layout | `9655200fe39d`  |
| 2347   | No documented layout | `9655200fe39d`  |
| 2343   | No documented layout | `9655200fe39d`  |
| 2335   | No documented layout | `9655200fe39d`  |
| 2327   | No documented layout | `9655200fe39d`  |
| 2324   | No documented layout | `9655200fe39d`  |
| 2319   | No documented layout | `9655200fe39d`  |
| 2313   | No documented layout | `9655200fe39d`  |
| 2308   | No documented layout | `9655200fe39d`  |
| 2302   | No documented layout | `9655200fe39d`  |
| 2295   | No documented layout | `9655200fe39d`  |
| 2290   | No documented layout | `9655200fe39d`  |
| 2284   | No documented layout | `9655200fe39d`  |
| 2276   | No documented layout | `9655200fe39d`  |
| 2269   | No documented layout | `9655200fe39d`  |
| 2259   | No documented layout | `9655200fe39d`  |
| 2250   | No documented layout | `9655200fe39d`  |
| 2243   | No documented layout | `9655200fe39d`  |
| 2235   | No documented layout | `9655200fe39d`  |
| 2229   | No documented layout | `9655200fe39d`  |
| 2224   | No documented layout | `9655200fe39d`  |
| 2218   | No documented layout | `9655200fe39d`  |
| 2215   | No documented layout | `9655200fe39d`  |
| 2207   | No documented layout | `9655200fe39d`  |
| 2203   | No documented layout | `9655200fe39d`  |
| 2196   | No documented layout | `9655200fe39d`  |
| 2192   | No documented layout | `9655200fe39d`  |
| 2189   | No documented layout | `9655200fe39d`  |
| 2183   | No documented layout | `9655200fe39d`  |
| 2179   | No documented layout | `9655200fe39d`  |
| 2171   | No documented layout | `9655200fe39d`  |
| 2163   | No documented layout | `9655200fe39d`  |
| 2156   | No documented layout | `9655200fe39d`  |
| 2151   | No documented layout | `9655200fe39d`  |
| 2147   | No documented layout | `9655200fe39d`  |
| 2142   | No documented layout | `9655200fe39d`  |
| 2138   | No documented layout | `9655200fe39d`  |
| 2134   | No documented layout | `9655200fe39d`  |
| 2130   | No documented layout | `9655200fe39d`  |
| 2122   | No documented layout | `9655200fe39d`  |
| 2107   | No documented layout | `9655200fe39d`  |
| 2098   | No documented layout | `9655200fe39d`  |
| 2089   | No documented layout | `9655200fe39d`  |
| 2081   | No documented layout | `9655200fe39d`  |
| 2073   | No documented layout | `9655200fe39d`  |
| 2067   | No documented layout | `9655200fe39d`  |
| 2063   | No documented layout | `9655200fe39d`  |
| 2059   | No documented layout | `9655200fe39d`  |
| 2052   | No documented layout | `9655200fe39d`  |
| 2044   | No documented layout | `9655200fe39d`  |
| 2039   | No documented layout | `9655200fe39d`  |
| 2032   | No documented layout | `9655200fe39d`  |
| 2025   | No documented layout | `9655200fe39d`  |
| 2011   | No documented layout | `9655200fe39d`  |
| 2005   | No documented layout | `9655200fe39d`  |
| 2000   | No documented layout | `9655200fe39d`  |
| 1996   | No documented layout | `9655200fe39d`  |
| 1991   | No documented layout | `9655200fe39d`  |
| 1985   | No documented layout | `9655200fe39d`  |
| 1980   | No documented layout | `9655200fe39d`  |
| 1969   | No documented layout | `9655200fe39d`  |
| 1964   | No documented layout | `9655200fe39d`  |
| 1958   | No documented layout | `9655200fe39d`  |
| 1950   | No documented layout | `9655200fe39d`  |
| 1945   | No documented layout | `9655200fe39d`  |
| 1937   | No documented layout | `9655200fe39d`  |
| 1933   | No documented layout | `9655200fe39d`  |
| 1927   | No documented layout | `9655200fe39d`  |
| 1921   | No documented layout | `9655200fe39d`  |
| 1914   | No documented layout | `9655200fe39d`  |
| 1908   | No documented layout | `9655200fe39d`  |
| 1897   | No documented layout | `9655200fe39d`  |
| 1892   | No documented layout | `9655200fe39d`  |
| 1886   | No documented layout | `9655200fe39d`  |
| 1881   | No documented layout | `9655200fe39d`  |
| 1871   | No documented layout | `9655200fe39d`  |
| 1866   | No documented layout | `9655200fe39d`  |
| 1862   | No documented layout | `9655200fe39d`  |
| 1854   | No documented layout | `9655200fe39d`  |
| 1846   | No documented layout | `9655200fe39d`  |
| 1838   | No documented layout | `9655200fe39d`  |
| 1832   | No documented layout | `9655200fe39d`  |
| 1826   | No documented layout | `9655200fe39d`  |
| 1822   | No documented layout | `9655200fe39d`  |
| 1818   | No documented layout | `9655200fe39d`  |
| 1804   | No documented layout | `9655200fe39d`  |
| 1794   | No documented layout | `9655200fe39d`  |
| 1790   | No documented layout | `9655200fe39d`  |
| 1784   | Layout 1             | `9655200fe39d`  |
| 1774   | Layout 1             | `9655200fe39d`  |
| 1771   | No documented layout | `9655200fe39d`  |
| 1762   | No documented layout | `9655200fe39d`  |
| 1759   | No documented layout | `9655200fe39d`  |
| 1754   | No documented layout | `9655200fe39d`  |
| 1749   | No documented layout | `9655200fe39d`  |
| 1743   | No documented layout | `9655200fe39d`  |
| 1737   | No documented layout | `9655200fe39d`  |
| 1731   | No documented layout | `9655200fe39d`  |
| 1725   | No documented layout | `9655200fe39d`  |
| 1717   | No documented layout | `9655200fe39d`  |
| 1710   | No documented layout | `9655200fe39d`  |
| 1704   | No documented layout | `9655200fe39d`  |
| 1698   | No documented layout | `9655200fe39d`  |
| 1690   | No documented layout | `9655200fe39d`  |
| 1685   | No documented layout | `9655200fe39d`  |
| 1680   | No documented layout | `9655200fe39d`  |
| 1674   | No documented layout | `9655200fe39d`  |
| 1668   | No documented layout | `9655200fe39d`  |
| 1659   | No documented layout | `9655200fe39d`  |
| 1649   | No documented layout | `9655200fe39d`  |
| 1642   | No documented layout | `9655200fe39d`  |
| 1636   | No documented layout | `9655200fe39d`  |
| 1628   | No documented layout | `9655200fe39d`  |
| 1622   | No documented layout | `9655200fe39d`  |
| 1614   | No documented layout | `9655200fe39d`  |
| 1608   | No documented layout | `9655200fe39d`  |
| 1602   | No documented layout | `9655200fe39d`  |
| 1598   | No documented layout | `9655200fe39d`  |
| 1594   | No documented layout | `9655200fe39d`  |
| 1590   | No documented layout | `9655200fe39d`  |
| 1587   | No documented layout | `9655200fe39d`  |
| 1584   | No documented layout | `9655200fe39d`  |
| 1579   | No documented layout | `9655200fe39d`  |
| 1572   | No documented layout | `9655200fe39d`  |
| 1565   | No documented layout | `9655200fe39d`  |
| 1559   | No documented layout | `9655200fe39d`  |
| 1554   | No documented layout | `9655200fe39d`  |
| 1547   | No documented layout | `9655200fe39d`  |
| 1537   | No documented layout | `9655200fe39d`  |
| 1529   | No documented layout | `9655200fe39d`  |
| 1524   | No documented layout | `9655200fe39d`  |
| 1519   | No documented layout | `9655200fe39d`  |
| 1509   | No documented layout | `9655200fe39d`  |
| 1506   | No documented layout | `9655200fe39d`  |
| 1504   | No documented layout | `9655200fe39d`  |
| 1500   | No documented layout | `9655200fe39d`  |
| 1493   | No documented layout | `9655200fe39d`  |
| 1489   | No documented layout | `9655200fe39d`  |
| 1485   | No documented layout | `9655200fe39d`  |
| 1481   | No documented layout | `9655200fe39d`  |
| 1474   | No documented layout | `9655200fe39d`  |
| 1466   | No documented layout | `9655200fe39d`  |
| 1462   | No documented layout | `9655200fe39d`  |
| 1459   | No documented layout | `9655200fe39d`  |
| 1453   | No documented layout | `9655200fe39d`  |
| 1450   | No documented layout | `9655200fe39d`  |
| 1445   | No documented layout | `9655200fe39d`  |
| 1439   | No documented layout | `9655200fe39d`  |
| 1433   | No documented layout | `9655200fe39d`  |
| 1430   | No documented layout | `9655200fe39d`  |
| 1426   | No documented layout | `9655200fe39d`  |
| 1421   | No documented layout | `9655200fe39d`  |
| 1417   | No documented layout | `9655200fe39d`  |
| 1416   | No documented layout | `9655200fe39d`  |
| 1409   | No documented layout | `9655200fe39d`  |
| 1405   | No documented layout | `9655200fe39d`  |
| 1401   | No documented layout | `9655200fe39d`  |
| 1396   | No documented layout | `9655200fe39d`  |
| 1391   | No documented layout | `9655200fe39d`  |
| 1390   | No documented layout | `9655200fe39d`  |
| 1386   | No documented layout | `9655200fe39d`  |
| 1381   | No documented layout | `9655200fe39d`  |
| 1379   | No documented layout | `9655200fe39d`  |
| 1372   | No documented layout | `9655200fe39d`  |
| 1366   | No documented layout | `9655200fe39d`  |
| 1364   | No documented layout | `9655200fe39d`  |
| 1363   | No documented layout | `9655200fe39d`  |
| 1360   | No documented layout | `9655200fe39d`  |
| 1358   | No documented layout | `9655200fe39d`  |
| 1355   | No documented layout | `9655200fe39d`  |
| 1351   | No documented layout | `9655200fe39d`  |
| 1348   | No documented layout | `9655200fe39d`  |
| 1346   | No documented layout | `9655200fe39d`  |
| 1341   | No documented layout | `9655200fe39d`  |
| 1340   | No documented layout | `9655200fe39d`  |
| 1338   | No documented layout | `9655200fe39d`  |
| 1335   | No documented layout | `9655200fe39d`  |
| 1333   | No documented layout | `9655200fe39d`  |
| 1329   | No documented layout | `9655200fe39d`  |
| 1327   | No documented layout | `9655200fe39d`  |
| 1324   | No documented layout | `9655200fe39d`  |
| 1321   | No documented layout | `9655200fe39d`  |
| 1319   | No documented layout | `9655200fe39d`  |
| 1318   | No documented layout | `9655200fe39d`  |
| 1316   | No documented layout | `9655200fe39d`  |
| 1313   | No documented layout | `9655200fe39d`  |
| 1311   | No documented layout | `9655200fe39d`  |
| 1309   | No documented layout | `9655200fe39d`  |
| 1304   | No documented layout | `9655200fe39d`  |
| 1292   | No documented layout | `9655200fe39d`  |
| 1286   | No documented layout | `9655200fe39d`  |
| 1280   | No documented layout | `9655200fe39d`  |
| 1276   | No documented layout | `9655200fe39d`  |
| 1267   | No documented layout | `9655200fe39d`  |
| 1261   | No documented layout | `9655200fe39d`  |
| 1256   | No documented layout | `9655200fe39d`  |
| 1250   | No documented layout | `9655200fe39d`  |
| 1246   | No documented layout | `9655200fe39d`  |
| 1239   | No documented layout | `9655200fe39d`  |
| 1230   | No documented layout | `9655200fe39d`  |
| 1226   | No documented layout | `9655200fe39d`  |
| 1220   | No documented layout | `9655200fe39d`  |
| 1217   | No documented layout | `9655200fe39d`  |
| 1211   | No documented layout | `9655200fe39d`  |
| 1210   | No documented layout | `9655200fe39d`  |
| 1208   | No documented layout | `9655200fe39d`  |
| 1203   | No documented layout | `9655200fe39d`  |
| 1197   | No documented layout | `9655200fe39d`  |
| 1194   | No documented layout | `9655200fe39d`  |
| 1192   | No documented layout | `9655200fe39d`  |
| 1187   | No documented layout | `9655200fe39d`  |
| 1183   | No documented layout | `9655200fe39d`  |
| 1177   | No documented layout | `9655200fe39d`  |
| 1173   | No documented layout | `9655200fe39d`  |
| 1167   | No documented layout | `9655200fe39d`  |
| 1164   | No documented layout | `9655200fe39d`  |
| 1156   | No documented layout | `9655200fe39d`  |
| 1149   | No documented layout | `9655200fe39d`  |
| 1144   | No documented layout | `9655200fe39d`  |
| 1137   | No documented layout | `9655200fe39d`  |
| 1132   | No documented layout | `9655200fe39d`  |
| 1127   | No documented layout | `9655200fe39d`  |
| 1122   | No documented layout | `9655200fe39d`  |
| 1118   | No documented layout | `9655200fe39d`  |
| 1114   | No documented layout | `9655200fe39d`  |
| 1109   | No documented layout | `9655200fe39d`  |
| 1102   | No file              | `9655200fe39d`  |
| 1096   | No file              | `9655200fe39d`  |
| 1088   | No file              | `9655200fe39d`  |
| 1081   | No file              | `9655200fe39d`  |
| 1076   | No file              | `9655200fe39d`  |
| 1069   | No file              | `9655200fe39d`  |
| 1064   | No file              | `9655200fe39d`  |
| 1058   | No file              | `9655200fe39d`  |
| 1051   | No file              | `9655200fe39d`  |
| 1044   | No file              | `9655200fe39d`  |
| 1036   | No file              | `9655200fe39d`  |
| 1026   | No file              | `9655200fe39d`  |
| 1016   | No file              | `9655200fe39d`  |
| 1009   | No file              | `9655200fe39d`  |
| 1005   | No file              | `9655200fe39d`  |
| 1000   | No file              | `9655200fe39d`  |
| 998    | No file              | `9655200fe39d`  |
| 990    | No file              | `9655200fe39d`  |
| 979    | No file              | `9655200fe39d`  |
| 972    | No file              | `9655200fe39d`  |
| 963    | No file              | `9655200fe39d`  |
| 955    | No file              | `9655200fe39d`  |
| 946    | No file              | `9655200fe39d`  |
| 938    | No file              | `9655200fe39d`  |
| 927    | No file              | `9655200fe39d`  |
| 911    | No file              | `9655200fe39d`  |
| 904    | No file              | `9655200fe39d`  |
| 899    | No file              | `9655200fe39d`  |
| 894    | No file              | `9655200fe39d`  |
| 885    | No file              | `9655200fe39d`  |
| 879    | No file              | `9655200fe39d`  |
| 872    | No file              | `9655200fe39d`  |
| 864    | No file              | `9655200fe39d`  |
| 855    | No file              | `9655200fe39d`  |
| 853    | No file              | `9655200fe39d`  |
| 845    | No file              | `9655200fe39d`  |
| 837    | No file              | `9655200fe39d`  |
| 829    | No documented layout | `9655200fe39d`  |
| 822    | No documented layout | `9655200fe39d`  |
| 814    | No documented layout | `9655200fe39d`  |
| 805    | No documented layout | `9655200fe39d`  |
| 794    | No documented layout | `9655200fe39d`  |
| 787    | No documented layout | `9655200fe39d`  |
| 780    | No documented layout | `9655200fe39d`  |
| 771    | No documented layout | `9655200fe39d`  |
| 760    | No documented layout | `9655200fe39d`  |
| 748    | No documented layout | `9655200fe39d`  |
| 741    | No documented layout | `9655200fe39d`  |
| 736    | No documented layout | `9655200fe39d`  |
| 731    | No documented layout | `9655200fe39d`  |
| 723    | No documented layout | `9655200fe39d`  |
| 711    | No documented layout | `9655200fe39d`  |
| 707    | No documented layout | `9655200fe39d`  |
| 697    | No documented layout | `9655200fe39d`  |
| 689    | No documented layout | `9655200fe39d`  |
| 683    | No documented layout | `9655200fe39d`  |
| 678    | No documented layout | `9655200fe39d`  |
| 670    | No documented layout | `9655200fe39d`  |
| 661    | No documented layout | `9655200fe39d`  |
| 656    | No documented layout | `9655200fe39d`  |
| 652    | No documented layout | `9655200fe39d`  |
| 643    | No documented layout | `9655200fe39d`  |
| 637    | No documented layout | `9655200fe39d`  |
| 630    | No documented layout | `9655200fe39d`  |
| 627    | No documented layout | `9655200fe39d`  |
| 621    | No documented layout | `9655200fe39d`  |
| 617    | No documented layout | `9655200fe39d`  |
| 615    | No documented layout | `9655200fe39d`  |
| 606    | No documented layout | `9655200fe39d`  |
| 599    | No documented layout | `9655200fe39d`  |
| 592    | No documented layout | `9655200fe39d`  |
| 586    | No documented layout | `9655200fe39d`  |
| 577    | No documented layout | `9655200fe39d`  |
| 569    | No documented layout | `9655200fe39d`  |
| 561    | No documented layout | `9655200fe39d`  |
| 554    | No documented layout | `9655200fe39d`  |
| 542    | No documented layout | `9655200fe39d`  |
| 532    | No documented layout | `9655200fe39d`  |
| 531    | No documented layout | `9655200fe39d`  |
| 526    | No documented layout | `9655200fe39d`  |
| 521    | No documented layout | `9655200fe39d`  |
| 517    | No documented layout | `9655200fe39d`  |
| 510    | No documented layout | `9655200fe39d`  |
| 508    | No documented layout | `9655200fe39d`  |
| 504    | No documented layout | `9655200fe39d`  |
| 497    | No documented layout | `9655200fe39d`  |
| 491    | No documented layout | `9655200fe39d`  |
| 485    | No documented layout | `9655200fe39d`  |
| 478    | No documented layout | `9655200fe39d`  |
| 472    | No documented layout | `9655200fe39d`  |
| 466    | No documented layout | `9655200fe39d`  |
| 457    | No documented layout | `9655200fe39d`  |
| 452    | No documented layout | `9655200fe39d`  |
| 449    | No documented layout | `9655200fe39d`  |
| 435    | No documented layout | `9655200fe39d`  |

<!-- versions:end -->

## Companion Files

The handler reads no other file. Class names come from LOC type 21
(`languagedata_*.loc`) when LOC is loaded.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                        | Type                                            | Field                       | Notes                                                                      |
| ----------------------------- | ----------------------------------------------- | --------------------------- | -------------------------------------------------------------------------- |
| `+0x00`                       | char[4]                                         | magic                       | ASCII `PABR`; no row count follows                                         |
| `+0x04`                       | Class Block[97]                                 | classes                     | One block per class type, `0` to `96`; see Class Block                     |
| `classes+0x00`                | u32                                             | unknown_class_package_count | `3` on client 3483                                                         |
| `classes+0x04`                | Class Package Row[unknown_class_package_count]  | unknown_class_packages      | See Class Package Row and [Open Questions](#open-questions)                |
| `unknown_class_packages+0x00` | String Table                                    | string_table                | See String Table                                                           |
| `string_table+0x00`           | u32                                             | string_table_start          | Offset of `string_count`, where `unknown_class_packages` ends              |
| `string_table+0x04`           | u32                                             | zero                        | Always `0`                                                                 |

Both block counts are fixed by the client, not stored: 97 class types and
119 equip types (`0` to `118`, the `equip_type` range of
[`itemenchant.dbss`](itemenchant_dbss.md#equip_type)). Walking 97 blocks
and the list ends exactly at `string_table_start`.

### Class Block (variable: 964 bytes + vehicle rows)

| Offset                         | Type                         | Field                   | Notes                                                                  |
| ------------------------------ | ---------------------------- | ----------------------- | ---------------------------------------------------------------------- |
| `+0x00`                        | Package Cell[119]            | weapon_packages         | One cell per equip type; see [Equip Types](#equip-types)               |
| `+0x3B8`                       | u32                          | vehicle_count           | `0`, `66`, `137`, `140` or `141` (client 3483)                         |
| `+0x3BC`                       | Vehicle Row[vehicle_count]   | vehicle_packages        | One row per vehicle type name                                          |
| `vehicle_packages+0x00`        | Equip Vehicle List[119]      | vehicle_weapon_packages | One list per equip type: the package on a vehicle with that weapon     |
| `vehicle_weapon_packages+0x00` | Package Cell                 | cutscene_package        | The class's cutscene package, such as `pc/cutscene/fighteraction_cutscene` |

### Package Cell (8 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | package_index | Index into the string table; an empty cell points at the empty string       |
| `+0x04` | u32  | package_hash  | Hash of the package path, see [Package Hash](#package-hash); `0` when empty |

### Vehicle Row (12 bytes)

| Offset  | Type | Field              | Notes                                                                   |
| ------- | ---- | ------------------ | ----------------------------------------------------------------------- |
| `+0x00` | u32  | vehicle_name_index | Index into the string table of a vehicle type name, such as `Horse`     |
| `+0x04` | u32  | package_index      | Index into the string table                                             |
| `+0x08` | u32  | package_hash       | Hash of the package path; never `0`                                     |

### Equip Vehicle List (variable: 4 bytes + vehicle rows)

| Offset  | Type                       | Field            | Notes                                                    |
| ------- | -------------------------- | ---------------- | -------------------------------------------------------- |
| `+0x00` | u32                        | vehicle_count    | `0` or `1` on client 3483                                |
| `+0x04` | Vehicle Row[vehicle_count] | vehicle_packages | Same row as the vehicle packages of the block            |

### Class Package Row (9 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u8   | class_type    | The class type of the block whose packages the path follows |
| `+0x01` | u32  | package_index | Index into the string table; unaligned                      |
| `+0x05` | u32  | package_hash  | Hash of the package path; unaligned                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `4,739` on client 3483      |
| `+0x04` | pstr[string_count] | strings      | `u8 is_wide`, `u32 byte_length`, then the text |

The string table has the shape `manufacture.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). Every string is narrow (`is_wide = 0`). The
package paths are lower case; the vehicle type names keep their case
(`FrigateShip`). Index `2` is the empty string on clients 1784 and 3483.

## Layout 1

Client 1784 has 82 class types and 92 equip types, and no
`unknown_class_packages` list: the last class block ends at
`string_table_start`. The cells and rows are the same as in Layout 2.

### File Layout

| Offset              | Type            | Field              | Notes                                         |
| ------------------- | --------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                                  |
| `+0x04`             | Class Block[82] | classes            | One block per class type, `0` to `81`         |
| `classes+0x00`      | String Table    | string_table       | `3,237` strings on client 1784                |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`, where `classes` ends |
| `string_table+0x04` | u32             | zero               | Always `0`                                    |

### Class Block (variable: 748 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                  |
| ------------------------------ | -------------------------- | ----------------------- | -------------------------------------- |
| `+0x00`                        | Package Cell[92]           | weapon_packages         | One cell per equip type, `0` to `91`   |
| `+0x2E0`                       | u32                        | vehicle_count           | `0` to `123` on client 1784            |
| `+0x2E4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                        |
| `vehicle_packages+0x00`        | Equip Vehicle List[92]     | vehicle_weapon_packages |                                        |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                        |

## Package Hash

`package_hash` is Bob Jenkins' lookup3 `hashlittle` of the path's ASCII
bytes with seed `0xC5EDE`, the hash `manufacture.bss` stores for its
action names (`ascii_key_hash` in `_common/string_hash.py`). It matches on
every non-empty cell and row of clients 1784 and 3483. Empty cells store
`0`, not the hash of the empty string (`0xDEBA1DCD`). Vehicle type names
have no hash.

## Equip Types

The cell position in `weapon_packages` and the list position in
`vehicle_weapon_packages` is the item `equip_type` of
[`itemenchant.dbss`](itemenchant_dbss.md#equip_type): Longsword `1` holds
`pc/1_phm/fighteraction_onehandsword` for the Warrior, matchlock `53` the
`commonchart_huntrifle` packages. On client 3483, 45 of the 119 equip types
hold a package for at least one class. The sheet column is the
`PcActionWeapon_Table` column of a private server's `DataSheets.bexcel` on
client 1784 whose cells match that position in the client 1784 file, with
the number of classes that match; types `93` and up have no column there.

| Equip type | Sheet column (client 1784) | Classes (client 3483) | Example package (client 3483) |
| ---------- | -------------------------- | --------------------- | ----------------------------- |
| 0   | `None` (39)              | 47 | `pc/1_phm/fighteraction_noweapon` |
| 1   | `LongSword` (13)         | 2  | `pc/1_phm/fighteraction_onehandsword` |
| 2   | `ElBlade` (3)            | 3  | `pc/5_pbw/tameraction_wavesword` |
| 3   | `Blade` (3)              | 3  | `pc/6_pkm/blademasteraction_blade` |
| 4   | `Bow`, `BowOneHanded` (1) | 1 | `pc/3_pew/elfaction_bow` |
| 6   | `Staff` (3)              | 2  | `pc/8_pwmm/whitemageaction_weaponmain_m` |
| 28  | `EnchantArm` (1)         | 1  | `pc/2_phw/sorceressaction_enchantarm` |
| 29  | `DoubleAxe` (1)          | 1  | `pc/4_pgm/giantaction_doubleaxe` |
| 31  | `Bow`, `BowOneHanded` (1) | 1 | `pc/3_pew/elfaction_bow` |
| 43  | `Rifle` (25)             | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_rifle` |
| 44  | `FishingRod` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingrod` |
| 45  | `Flute` (25)             | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_flute` |
| 47  | `Cane` (25)              | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_cane` |
| 48  | `FishingHarpoon` (25)    | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingharpoon` |
| 49  | `FishingNet` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingnet` |
| 50  | `Drum` (25)              | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_drum` |
| 53  | `HuntRifle` (25)         | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_huntrifle` |
| 60  | `Cymbals` (25)           | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_cymbals` |
| 61  | `Guitar` (25)            | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_guitar` |
| 62  | `Trumpet` (25)           | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_trumpet` |
| 63  | `Kriegsmesser` (1)       | 1  | `pc/15_pdew/darkelfaction_blade` |
| 64  | `SiegeRifle` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_siegerifle` |
| 65  | `Gauntlet` (2)           | 2  | `pc/16_pcm/combattantaction_gauntlet` |
| 67  | `Sherry_Main` (1)        | 1  | `pc/17_psw/chineseaction_enchantarm` |
| 69  | `SiegeAxe` (25)          | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_siegeaxe` |
| 71  | `HandGrenade` (25)       | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_handgrenade` |
| 73  | `CrossBow_Main` (1)      | 1  | `pc/9_pem/elfmanaction_crossbow` |
| 75  | `WaterBomb` (25)         | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_waterbomb` |
| 77  | `SniperRifle` (25)       | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_sniperrifle` |
| 78  | `Boomerang` (1)          | 1  | `pc/14_plw/shytribeaction_weaponmain_w` |
| 80  | `Scimitar` (1)           | 1  | `pc/18_pam/valenciafighteraction_weapon` |
| 82  | `BroadSword` (1)         | 1  | `pc/19_prum/rutumaction_broadsword` |
| 83  | `OneHandAxe` (1)         | 1  | `pc/11_pgw/giantwomenaction_onehandaxe` |
| 86  | `Mace` (1)               | 1  | `pc/21_phwb/blackfighterwomenaction_mace` |
| 88  | `PPM_Main` (1)           | 1  | `pc/23_ppm/ppmaction_weapon` |
| 89  | `PFW_Main` (1)           | 1  | `pc/24_pfw/pfwaction_mainweapon` |
| 93  |                          | 1  | `pc/25_pqw/pqwaction_weapon` |
| 95  |                          | 1  | `pc/26_pbm/pbmaction_weapon` |
| 96  |                          | 1  | `pc/27_pkow/pkowaction_weapon` |
| 97  |                          | 6  | `pc/28_pmyf/pmyfaction_weapon` |
| 100 |                          | 1  | `pc/29_pnyw/pnywaction_weapon` |
| 109 |                          | 6  | `pc/31_prsa/prsaaction_weapon` |
| 112 |                          | 2  | `pc/32_pwge/pwgeaction_weapon` |
| 114 |                          | 1  | `pc/20_pjkd/pjkdaction_weapon` |
| 116 |                          | 1  | `pc/30_pdkl/pdklaction_weapon` |

The only `vehicle_weapon_packages` entries on clients 1784 and 3483 are
`Horse` under equip type `53`, the `horsehuntrifle` package of each class
(34 classes on client 3483). The sheet's one `PcActionVehicleWithWeapon_Table`
row is `Horse` with `HuntRifle`.

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) declare
`gc::PcActionPackageNameManager` with the members
`_packageNameArray_Weapon[32][63]`, `_packageNameArray_Vehicle[32][37]` and
`_packageNameMap_VehicleWithWeapon[32]`, a map keyed by
`(gc::VehicleType, gc::ItemEquipType::Type)`, each next to a matching
`_packageHash*` member of `unsigned int`. The outer index is the class type.
The live file stores each name and hash as one Package Cell; the vehicle
array became rows keyed by the vehicle type name, and the map one list per
equip type.

The `PcActionPackage_Table` workbook of a private server's
`DataSheets.bexcel` on client 1784 has the four sheets the dump of that
server (`Instance_dumpFull.exe`) loads with it: `PcActionWeapon_Table` (one
row per class type, one column per weapon), `PcActionVehicle_Table` (one
row per `VehicleTypeName`, one column per class type),
`PcActionVehicleWithWeapon_Table` (`VehicleTypeName`, `WeaponTypeName`, a
column per class type) and `CutScenePcAction_Table` (`classType`,
`cutSceneAction`). The private server's paths are edited, so the values
match in part only: on client 1784, 32 of the 32 `cutSceneAction` cells
and 3,208 of the 5,565 filled `PcActionVehicle_Table` cells match the file
by file name (26 of 32 and 2,137 of 5,809 on client 3483). Each weapon
column that matches lands on one equip type, listed under
[Equip Types](#equip-types), except `Bow` and `BowOneHanded`: class type
`4` holds the same `elfaction_bow` package at `4` and `31`, so both columns
match both.

`class_type` in Class Package Row is named by value: rows `6`, `15` and
`32` (client 3483) hold `pc/29_pnyw/`, `pc/27_pkow/` and `pc/30_pdkl/`
paths, the folders of class blocks `6`, `15` and `32`.

## Notes

- On client 3483, class blocks `47` to `96` are empty: every cell points at
  the empty string and every count is `0`. Blocks `36` to `46` hold 66
  vehicle rows each and repeat the packages of other classes
  (`pc/35_pyfm/` and `pc/36_pyfw/` alternate from block `37`). Block `14`
  also holds 66, block `16` 141, block `17` 137 and the other filled blocks
  140.
- Blocks `18` and `22` have no vehicle rows on client 3483; block `18`
  repeats the Tamer's `pc/5_pbw/` weapon packages.
- On client 1784 each of the 82 blocks holds at least one weapon package;
  33 of them have no vehicle rows.

## Open Questions

### What the Class Package List Is For

`unknown_class_packages` holds three paths on client 3483, each named
`*action_weapon_copy` (`pc/29_pnyw/pnywaction_weapon_copy` for block `6`).
Client 1784 has no such list, and no 1784 sheet holds the names. Which
weapon state loads the copy package is not in the file.

### Where the Packages Without a File Live

Of the 4,594 `pc/` paths in the string table (client 3483), 33 are
`.paac` files under `character/binaryactionchart/`, all of them equip type
`0` packages. The other 34th file there,
`character/binaryactionchart/pc/pc_actionchartpackagepcraw.paac`
(131 MB), is not named here and may hold the weapon, vehicle and cutscene
packages; that needs a `.paac` doc first.
