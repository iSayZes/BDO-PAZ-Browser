# `hardcorechanneltitlestaticstatusmanager.bss` Format

## Purpose

The titles of the Hardcore channel, one 47-byte row each: a title key, the
number of kills it needs, the Korean name, description and condition text
in the string table, and the colour the title shows in. On client 3474 the
75 titles come in tiers of 100 to 10,000 kills of one monster group each
(Ancient Weapons, Desert Naga, Desert Fogan, Crescent Shrine, Gahaz Bandits,
Pila Ku Jail, Aakman Temple, Hystria Ancient Weapons), and the colour
rises with the tier: white, green, blue, yellow, orange. The keys are the
Hardcore window's own: [`title.dbss`](title_dbss.md) title 1 is Battle
Ready and title 65 Destroyer of Blind Faith, where this file has an Ancient
Weapon and an Aakman title.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                          | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------------------------------- | ----- | ------- | --------- |
| 1      | 2834 and later | `hardcorechanneltitlestaticstatusmanager.bss` | 9,461 | 75 Row  | 47        |

| Layout | File                                          | Known           | Unknown         |
| ------ | --------------------------------------------- | --------------- | --------------- |
| 1      | `hardcorechanneltitlestaticstatusmanager.bss` | 7,586 B (80.2%) | 1,875 B (19.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5140b2044235`  |
| 3482   | Layout 1 | `5140b2044235`  |
| 3474   | Layout 1 | `5140b2044235`  |
| 3473   | Layout 1 | `5140b2044235`  |
| 3464   | Layout 1 | `5140b2044235`  |
| 3458   | Layout 1 | `5140b2044235`  |
| 3454   | Layout 1 | `5140b2044235`  |
| 3444   | Layout 1 | `5140b2044235`  |
| 3435   | Layout 1 | `5140b2044235`  |
| 3426   | Layout 1 | `5140b2044235`  |
| 3418   | Layout 1 | `5140b2044235`  |
| 3412   | Layout 1 | `5140b2044235`  |
| 3402   | Layout 1 | `5140b2044235`  |
| 3396   | Layout 1 | `5140b2044235`  |
| 3387   | Layout 1 | `5140b2044235`  |
| 3381   | Layout 1 | `5140b2044235`  |
| 3373   | Layout 1 | `5140b2044235`  |
| 3364   | Layout 1 | `5140b2044235`  |
| 3356   | Layout 1 | `5140b2044235`  |
| 3349   | Layout 1 | `5140b2044235`  |
| 3342   | Layout 1 | `5140b2044235`  |
| 3335   | Layout 1 | `5140b2044235`  |
| 3326   | Layout 1 | `5140b2044235`  |
| 3321   | Layout 1 | `5140b2044235`  |
| 3314   | Layout 1 | `5140b2044235`  |
| 3303   | Layout 1 | `5140b2044235`  |
| 3302   | Layout 1 | `5140b2044235`  |
| 3293   | Layout 1 | `5140b2044235`  |
| 3283   | Layout 1 | `5140b2044235`  |
| 3275   | Layout 1 | `5140b2044235`  |
| 3267   | Layout 1 | `5140b2044235`  |
| 3258   | Layout 1 | `5140b2044235`  |
| 3251   | Layout 1 | `5140b2044235`  |
| 3242   | Layout 1 | `5140b2044235`  |
| 3235   | Layout 1 | `5140b2044235`  |
| 3229   | Layout 1 | `5140b2044235`  |
| 3212   | Layout 1 | `5140b2044235`  |
| 3203   | Layout 1 | `5140b2044235`  |
| 3193   | Layout 1 | `5140b2044235`  |
| 3186   | Layout 1 | `5140b2044235`  |
| 3177   | Layout 1 | `5140b2044235`  |
| 3169   | Layout 1 | `5140b2044235`  |
| 3158   | Layout 1 | `5140b2044235`  |
| 3151   | Layout 1 | `5140b2044235`  |
| 3144   | Layout 1 | `5140b2044235`  |
| 3133   | Layout 1 | `5140b2044235`  |
| 3125   | Layout 1 | `5140b2044235`  |
| 3118   | Layout 1 | `5140b2044235`  |
| 3111   | Layout 1 | `5140b2044235`  |
| 3103   | Layout 1 | `5140b2044235`  |
| 3095   | Layout 1 | `5140b2044235`  |
| 3086   | Layout 1 | `5140b2044235`  |
| 3072   | Layout 1 | `5140b2044235`  |
| 3062   | Layout 1 | `5140b2044235`  |
| 3052   | Layout 1 | `5140b2044235`  |
| 3045   | Layout 1 | `5140b2044235`  |
| 3037   | Layout 1 | `5140b2044235`  |
| 3030   | Layout 1 | `5140b2044235`  |
| 3021   | Layout 1 | `5140b2044235`  |
| 3012   | Layout 1 | `5140b2044235`  |
| 3002   | Layout 1 | `5140b2044235`  |
| 2995   | Layout 1 | `5140b2044235`  |
| 2987   | Layout 1 | `5140b2044235`  |
| 2978   | Layout 1 | `5140b2044235`  |
| 2970   | Layout 1 | `5140b2044235`  |
| 2959   | Layout 1 | `5140b2044235`  |
| 2951   | Layout 1 | `5140b2044235`  |
| 2942   | Layout 1 | `5140b2044235`  |
| 2935   | Layout 1 | `5140b2044235`  |
| 2932   | Layout 1 | `5140b2044235`  |
| 2923   | Layout 1 | `5140b2044235`  |
| 2919   | Layout 1 | `5140b2044235`  |
| 2907   | Layout 1 | `5140b2044235`  |
| 2900   | Layout 1 | `5140b2044235`  |
| 2891   | Layout 1 | `5140b2044235`  |
| 2882   | Layout 1 | `5140b2044235`  |
| 2872   | Layout 1 | `5140b2044235`  |
| 2863   | Layout 1 | `5140b2044235`  |
| 2855   | Layout 1 | `5140b2044235`  |
| 2849   | Layout 1 | `5140b2044235`  |
| 2844   | Layout 1 | `5140b2044235`  |
| 2834   | Layout 1 | `5140b2044235`  |
| 2825   | No file  | `5140b2044235`  |
| 2819   | No file  | `5140b2044235`  |
| 2811   | No file  | `5140b2044235`  |
| 2803   | No file  | `5140b2044235`  |
| 2794   | No file  | `5140b2044235`  |
| 2783   | No file  | `5140b2044235`  |
| 2774   | No file  | `5140b2044235`  |
| 2765   | No file  | `5140b2044235`  |
| 2756   | No file  | `5140b2044235`  |
| 2750   | No file  | `5140b2044235`  |
| 2743   | No file  | `5140b2044235`  |
| 2736   | No file  | `5140b2044235`  |
| 2726   | No file  | `5140b2044235`  |
| 2717   | No file  | `5140b2044235`  |
| 2709   | No file  | `5140b2044235`  |
| 2703   | No file  | `5140b2044235`  |
| 2695   | No file  | `5140b2044235`  |
| 2684   | No file  | `5140b2044235`  |
| 2672   | No file  | `5140b2044235`  |
| 2665   | No file  | `5140b2044235`  |
| 2657   | No file  | `5140b2044235`  |
| 2649   | No file  | `5140b2044235`  |
| 2644   | No file  | `5140b2044235`  |
| 2637   | No file  | `5140b2044235`  |
| 2629   | No file  | `5140b2044235`  |
| 2619   | No file  | `5140b2044235`  |
| 2612   | No file  | `5140b2044235`  |
| 2606   | No file  | `5140b2044235`  |
| 2602   | No file  | `5140b2044235`  |
| 2601   | No file  | `5140b2044235`  |
| 2592   | No file  | `5140b2044235`  |
| 2583   | No file  | `5140b2044235`  |
| 2575   | No file  | `5140b2044235`  |
| 2567   | No file  | `5140b2044235`  |
| 2560   | No file  | `5140b2044235`  |
| 2553   | No file  | `5140b2044235`  |
| 2545   | No file  | `5140b2044235`  |
| 2538   | No file  | `5140b2044235`  |
| 2529   | No file  | `5140b2044235`  |
| 2519   | No file  | `5140b2044235`  |
| 2513   | No file  | `5140b2044235`  |
| 2510   | No file  | `5140b2044235`  |
| 2507   | No file  | `5140b2044235`  |
| 2503   | No file  | `5140b2044235`  |
| 2498   | No file  | `5140b2044235`  |
| 2492   | No file  | `5140b2044235`  |
| 2487   | No file  | `5140b2044235`  |
| 2480   | No file  | `5140b2044235`  |
| 2474   | No file  | `5140b2044235`  |
| 2468   | No file  | `5140b2044235`  |
| 2460   | No file  | `5140b2044235`  |
| 2453   | No file  | `5140b2044235`  |
| 2444   | No file  | `5140b2044235`  |
| 2438   | No file  | `5140b2044235`  |
| 2434   | No file  | `5140b2044235`  |
| 2429   | No file  | `5140b2044235`  |
| 2421   | No file  | `5140b2044235`  |
| 2414   | No file  | `5140b2044235`  |
| 2407   | No file  | `5140b2044235`  |
| 2401   | No file  | `5140b2044235`  |
| 2397   | No file  | `5140b2044235`  |
| 2393   | No file  | `5140b2044235`  |
| 2384   | No file  | `5140b2044235`  |
| 2378   | No file  | `5140b2044235`  |
| 2372   | No file  | `5140b2044235`  |
| 2358   | No file  | `5140b2044235`  |
| 2352   | No file  | `5140b2044235`  |
| 2347   | No file  | `5140b2044235`  |
| 2343   | No file  | `5140b2044235`  |
| 2335   | No file  | `5140b2044235`  |
| 2327   | No file  | `5140b2044235`  |
| 2324   | No file  | `5140b2044235`  |
| 2319   | No file  | `5140b2044235`  |
| 2313   | No file  | `5140b2044235`  |
| 2308   | No file  | `5140b2044235`  |
| 2302   | No file  | `5140b2044235`  |
| 2295   | No file  | `5140b2044235`  |
| 2290   | No file  | `5140b2044235`  |
| 2284   | No file  | `5140b2044235`  |
| 2276   | No file  | `5140b2044235`  |
| 2269   | No file  | `5140b2044235`  |
| 2259   | No file  | `5140b2044235`  |
| 2250   | No file  | `5140b2044235`  |
| 2243   | No file  | `5140b2044235`  |
| 2235   | No file  | `5140b2044235`  |
| 2229   | No file  | `5140b2044235`  |
| 2224   | No file  | `5140b2044235`  |
| 2218   | No file  | `5140b2044235`  |
| 2215   | No file  | `5140b2044235`  |
| 2207   | No file  | `5140b2044235`  |
| 2203   | No file  | `5140b2044235`  |
| 2196   | No file  | `5140b2044235`  |
| 2192   | No file  | `5140b2044235`  |
| 2189   | No file  | `5140b2044235`  |
| 2183   | No file  | `5140b2044235`  |
| 2179   | No file  | `5140b2044235`  |
| 2171   | No file  | `5140b2044235`  |
| 2163   | No file  | `5140b2044235`  |
| 2156   | No file  | `5140b2044235`  |
| 2151   | No file  | `5140b2044235`  |
| 2147   | No file  | `5140b2044235`  |
| 2142   | No file  | `5140b2044235`  |
| 2138   | No file  | `5140b2044235`  |
| 2134   | No file  | `5140b2044235`  |
| 2130   | No file  | `5140b2044235`  |
| 2122   | No file  | `5140b2044235`  |
| 2107   | No file  | `5140b2044235`  |
| 2098   | No file  | `5140b2044235`  |
| 2089   | No file  | `5140b2044235`  |
| 2081   | No file  | `5140b2044235`  |
| 2073   | No file  | `5140b2044235`  |
| 2067   | No file  | `5140b2044235`  |
| 2063   | No file  | `5140b2044235`  |
| 2059   | No file  | `5140b2044235`  |
| 2052   | No file  | `5140b2044235`  |
| 2044   | No file  | `5140b2044235`  |
| 2039   | No file  | `5140b2044235`  |
| 2032   | No file  | `5140b2044235`  |
| 2025   | No file  | `5140b2044235`  |
| 2011   | No file  | `5140b2044235`  |
| 2005   | No file  | `5140b2044235`  |
| 2000   | No file  | `5140b2044235`  |
| 1996   | No file  | `5140b2044235`  |
| 1991   | No file  | `5140b2044235`  |
| 1985   | No file  | `5140b2044235`  |
| 1980   | No file  | `5140b2044235`  |
| 1969   | No file  | `5140b2044235`  |
| 1964   | No file  | `5140b2044235`  |
| 1958   | No file  | `5140b2044235`  |
| 1950   | No file  | `5140b2044235`  |
| 1945   | No file  | `5140b2044235`  |
| 1937   | No file  | `5140b2044235`  |
| 1933   | No file  | `5140b2044235`  |
| 1927   | No file  | `5140b2044235`  |
| 1921   | No file  | `5140b2044235`  |
| 1914   | No file  | `5140b2044235`  |
| 1908   | No file  | `5140b2044235`  |
| 1897   | No file  | `5140b2044235`  |
| 1892   | No file  | `5140b2044235`  |
| 1886   | No file  | `5140b2044235`  |
| 1881   | No file  | `5140b2044235`  |
| 1871   | No file  | `5140b2044235`  |
| 1866   | No file  | `5140b2044235`  |
| 1862   | No file  | `5140b2044235`  |
| 1854   | No file  | `5140b2044235`  |
| 1846   | No file  | `5140b2044235`  |
| 1838   | No file  | `5140b2044235`  |
| 1832   | No file  | `5140b2044235`  |
| 1826   | No file  | `5140b2044235`  |
| 1822   | No file  | `5140b2044235`  |
| 1818   | No file  | `5140b2044235`  |
| 1804   | No file  | `5140b2044235`  |
| 1794   | No file  | `5140b2044235`  |
| 1790   | No file  | `5140b2044235`  |
| 1784   | No file  | `5140b2044235`  |
| 1774   | No file  | `5140b2044235`  |
| 1771   | No file  | `5140b2044235`  |
| 1762   | No file  | `5140b2044235`  |
| 1759   | No file  | `5140b2044235`  |
| 1754   | No file  | `5140b2044235`  |
| 1749   | No file  | `5140b2044235`  |
| 1743   | No file  | `5140b2044235`  |
| 1737   | No file  | `5140b2044235`  |
| 1731   | No file  | `5140b2044235`  |
| 1725   | No file  | `5140b2044235`  |
| 1717   | No file  | `5140b2044235`  |
| 1710   | No file  | `5140b2044235`  |
| 1704   | No file  | `5140b2044235`  |
| 1698   | No file  | `5140b2044235`  |
| 1690   | No file  | `5140b2044235`  |
| 1685   | No file  | `5140b2044235`  |
| 1680   | No file  | `5140b2044235`  |
| 1674   | No file  | `5140b2044235`  |
| 1668   | No file  | `5140b2044235`  |
| 1659   | No file  | `5140b2044235`  |
| 1649   | No file  | `5140b2044235`  |
| 1642   | No file  | `5140b2044235`  |
| 1636   | No file  | `5140b2044235`  |
| 1628   | No file  | `5140b2044235`  |
| 1622   | No file  | `5140b2044235`  |
| 1614   | No file  | `5140b2044235`  |
| 1608   | No file  | `5140b2044235`  |
| 1602   | No file  | `5140b2044235`  |
| 1598   | No file  | `5140b2044235`  |
| 1594   | No file  | `5140b2044235`  |
| 1590   | No file  | `5140b2044235`  |
| 1587   | No file  | `5140b2044235`  |
| 1584   | No file  | `5140b2044235`  |
| 1579   | No file  | `5140b2044235`  |
| 1572   | No file  | `5140b2044235`  |
| 1565   | No file  | `5140b2044235`  |
| 1559   | No file  | `5140b2044235`  |
| 1554   | No file  | `5140b2044235`  |
| 1547   | No file  | `5140b2044235`  |
| 1537   | No file  | `5140b2044235`  |
| 1529   | No file  | `5140b2044235`  |
| 1524   | No file  | `5140b2044235`  |
| 1519   | No file  | `5140b2044235`  |
| 1509   | No file  | `5140b2044235`  |
| 1506   | No file  | `5140b2044235`  |
| 1504   | No file  | `5140b2044235`  |
| 1500   | No file  | `5140b2044235`  |
| 1493   | No file  | `5140b2044235`  |
| 1489   | No file  | `5140b2044235`  |
| 1485   | No file  | `5140b2044235`  |
| 1481   | No file  | `5140b2044235`  |
| 1474   | No file  | `5140b2044235`  |
| 1466   | No file  | `5140b2044235`  |
| 1462   | No file  | `5140b2044235`  |
| 1459   | No file  | `5140b2044235`  |
| 1453   | No file  | `5140b2044235`  |
| 1450   | No file  | `5140b2044235`  |
| 1445   | No file  | `5140b2044235`  |
| 1439   | No file  | `5140b2044235`  |
| 1433   | No file  | `5140b2044235`  |
| 1430   | No file  | `5140b2044235`  |
| 1426   | No file  | `5140b2044235`  |
| 1421   | No file  | `5140b2044235`  |
| 1417   | No file  | `5140b2044235`  |
| 1416   | No file  | `5140b2044235`  |
| 1409   | No file  | `5140b2044235`  |
| 1405   | No file  | `5140b2044235`  |
| 1401   | No file  | `5140b2044235`  |
| 1396   | No file  | `5140b2044235`  |
| 1391   | No file  | `5140b2044235`  |
| 1390   | No file  | `5140b2044235`  |
| 1386   | No file  | `5140b2044235`  |
| 1381   | No file  | `5140b2044235`  |
| 1379   | No file  | `5140b2044235`  |
| 1372   | No file  | `5140b2044235`  |
| 1366   | No file  | `5140b2044235`  |
| 1364   | No file  | `5140b2044235`  |
| 1363   | No file  | `5140b2044235`  |
| 1360   | No file  | `5140b2044235`  |
| 1358   | No file  | `5140b2044235`  |
| 1355   | No file  | `5140b2044235`  |
| 1351   | No file  | `5140b2044235`  |
| 1348   | No file  | `5140b2044235`  |
| 1346   | No file  | `5140b2044235`  |
| 1341   | No file  | `5140b2044235`  |
| 1340   | No file  | `5140b2044235`  |
| 1338   | No file  | `5140b2044235`  |
| 1335   | No file  | `5140b2044235`  |
| 1333   | No file  | `5140b2044235`  |
| 1329   | No file  | `5140b2044235`  |
| 1327   | No file  | `5140b2044235`  |
| 1324   | No file  | `5140b2044235`  |
| 1321   | No file  | `5140b2044235`  |
| 1319   | No file  | `5140b2044235`  |
| 1318   | No file  | `5140b2044235`  |
| 1316   | No file  | `5140b2044235`  |
| 1313   | No file  | `5140b2044235`  |
| 1311   | No file  | `5140b2044235`  |
| 1309   | No file  | `5140b2044235`  |
| 1304   | No file  | `5140b2044235`  |
| 1292   | No file  | `5140b2044235`  |
| 1286   | No file  | `5140b2044235`  |
| 1280   | No file  | `5140b2044235`  |
| 1276   | No file  | `5140b2044235`  |
| 1267   | No file  | `5140b2044235`  |
| 1261   | No file  | `5140b2044235`  |
| 1256   | No file  | `5140b2044235`  |
| 1250   | No file  | `5140b2044235`  |
| 1246   | No file  | `5140b2044235`  |
| 1239   | No file  | `5140b2044235`  |
| 1230   | No file  | `5140b2044235`  |
| 1226   | No file  | `5140b2044235`  |
| 1220   | No file  | `5140b2044235`  |
| 1217   | No file  | `5140b2044235`  |
| 1211   | No file  | `5140b2044235`  |
| 1210   | No file  | `5140b2044235`  |
| 1208   | No file  | `5140b2044235`  |
| 1203   | No file  | `5140b2044235`  |
| 1197   | No file  | `5140b2044235`  |
| 1194   | No file  | `5140b2044235`  |
| 1192   | No file  | `5140b2044235`  |
| 1187   | No file  | `5140b2044235`  |
| 1183   | No file  | `5140b2044235`  |
| 1177   | No file  | `5140b2044235`  |
| 1173   | No file  | `5140b2044235`  |
| 1167   | No file  | `5140b2044235`  |
| 1164   | No file  | `5140b2044235`  |
| 1156   | No file  | `5140b2044235`  |
| 1149   | No file  | `5140b2044235`  |
| 1144   | No file  | `5140b2044235`  |
| 1137   | No file  | `5140b2044235`  |
| 1132   | No file  | `5140b2044235`  |
| 1127   | No file  | `5140b2044235`  |
| 1122   | No file  | `5140b2044235`  |
| 1118   | No file  | `5140b2044235`  |
| 1114   | No file  | `5140b2044235`  |
| 1109   | No file  | `5140b2044235`  |
| 1102   | No file  | `5140b2044235`  |
| 1096   | No file  | `5140b2044235`  |
| 1088   | No file  | `5140b2044235`  |
| 1081   | No file  | `5140b2044235`  |
| 1076   | No file  | `5140b2044235`  |
| 1069   | No file  | `5140b2044235`  |
| 1064   | No file  | `5140b2044235`  |
| 1058   | No file  | `5140b2044235`  |
| 1051   | No file  | `5140b2044235`  |
| 1044   | No file  | `5140b2044235`  |
| 1036   | No file  | `5140b2044235`  |
| 1026   | No file  | `5140b2044235`  |
| 1016   | No file  | `5140b2044235`  |
| 1009   | No file  | `5140b2044235`  |
| 1005   | No file  | `5140b2044235`  |
| 1000   | No file  | `5140b2044235`  |
| 998    | No file  | `5140b2044235`  |
| 990    | No file  | `5140b2044235`  |
| 979    | No file  | `5140b2044235`  |
| 972    | No file  | `5140b2044235`  |
| 963    | No file  | `5140b2044235`  |
| 955    | No file  | `5140b2044235`  |
| 946    | No file  | `5140b2044235`  |
| 938    | No file  | `5140b2044235`  |
| 927    | No file  | `5140b2044235`  |
| 911    | No file  | `5140b2044235`  |
| 904    | No file  | `5140b2044235`  |
| 899    | No file  | `5140b2044235`  |
| 894    | No file  | `5140b2044235`  |
| 885    | No file  | `5140b2044235`  |
| 879    | No file  | `5140b2044235`  |
| 872    | No file  | `5140b2044235`  |
| 864    | No file  | `5140b2044235`  |
| 855    | No file  | `5140b2044235`  |
| 853    | No file  | `5140b2044235`  |
| 845    | No file  | `5140b2044235`  |
| 837    | No file  | `5140b2044235`  |
| 829    | No file  | `5140b2044235`  |
| 822    | No file  | `5140b2044235`  |
| 814    | No file  | `5140b2044235`  |
| 805    | No file  | `5140b2044235`  |
| 794    | No file  | `5140b2044235`  |
| 787    | No file  | `5140b2044235`  |
| 780    | No file  | `5140b2044235`  |
| 771    | No file  | `5140b2044235`  |
| 760    | No file  | `5140b2044235`  |
| 748    | No file  | `5140b2044235`  |
| 741    | No file  | `5140b2044235`  |
| 736    | No file  | `5140b2044235`  |
| 731    | No file  | `5140b2044235`  |
| 723    | No file  | `5140b2044235`  |
| 711    | No file  | `5140b2044235`  |
| 707    | No file  | `5140b2044235`  |
| 697    | No file  | `5140b2044235`  |
| 689    | No file  | `5140b2044235`  |
| 683    | No file  | `5140b2044235`  |
| 678    | No file  | `5140b2044235`  |
| 670    | No file  | `5140b2044235`  |
| 661    | No file  | `5140b2044235`  |
| 656    | No file  | `5140b2044235`  |
| 652    | No file  | `5140b2044235`  |
| 643    | No file  | `5140b2044235`  |
| 637    | No file  | `5140b2044235`  |
| 630    | No file  | `5140b2044235`  |
| 627    | No file  | `5140b2044235`  |
| 621    | No file  | `5140b2044235`  |
| 617    | No file  | `5140b2044235`  |
| 615    | No file  | `5140b2044235`  |
| 606    | No file  | `5140b2044235`  |
| 599    | No file  | `5140b2044235`  |
| 592    | No file  | `5140b2044235`  |
| 586    | No file  | `5140b2044235`  |
| 577    | No file  | `5140b2044235`  |
| 569    | No file  | `5140b2044235`  |
| 561    | No file  | `5140b2044235`  |
| 554    | No file  | `5140b2044235`  |
| 542    | No file  | `5140b2044235`  |
| 532    | No file  | `5140b2044235`  |
| 531    | No file  | `5140b2044235`  |
| 526    | No file  | `5140b2044235`  |
| 521    | No file  | `5140b2044235`  |
| 517    | No file  | `5140b2044235`  |
| 510    | No file  | `5140b2044235`  |
| 508    | No file  | `5140b2044235`  |
| 504    | No file  | `5140b2044235`  |
| 497    | No file  | `5140b2044235`  |
| 491    | No file  | `5140b2044235`  |
| 485    | No file  | `5140b2044235`  |
| 478    | No file  | `5140b2044235`  |
| 472    | No file  | `5140b2044235`  |
| 466    | No file  | `5140b2044235`  |
| 457    | No file  | `5140b2044235`  |
| 452    | No file  | `5140b2044235`  |
| 449    | No file  | `5140b2044235`  |
| 435    | No file  | `5140b2044235`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (47 bytes)

| Offset  | Type | Field           | Notes                                                                                     |
| ------- | ---- | --------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | title_key       | Hardcore title key, unique; `1` to `80` with gaps on client 3474                          |
| `+0x02` | u8   | unknown_02      | Always `0`                                                                                |
| `+0x03` | u32  | unknown_03      | One value per monster group and kind (`241` to `259`); see Open Questions                 |
| `+0x07` | u32  | kill_count      | Kills the title needs; the number in the condition text on all 75 rows (client 3474)      |
| `+0x0B` | u32  | unknown_0b      | Always `0`                                                                                |
| `+0x0F` | u32  | unknown_0f      | `0` to `39`; shared by the same step of several groups; see Open Questions                      |
| `+0x13` | u32  | unknown_13      | Equals `unknown_03` on every row                                                          |
| `+0x17` | u32  | unknown_17      | Equals `kill_count` on every row                                                          |
| `+0x1B` | u32  | name_ref        | String-table index of the Korean title name; `ToClient_getHardCoreTitleNameByKey`         |
| `+0x1F` | u32  | description_ref | String-table index of the Korean description; `ToClient_getHardCoreTitleDescByKey`        |
| `+0x23` | u32  | condition_ref   | String-table index of the Korean condition; `ToClient_getHardCoreTitleConditionByKey`     |
| `+0x27` | u32  | unknown_27      | `3` on every row                                                                          |
| `+0x2B` | u32  | grade_color     | ARGB colour of the title name; `ToClient_GetHardCoreTitleGradeColor`                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                                 |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `166` on client 3474                                               |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean text; rows of one monster group share their description string         |

## Grade Colours

`grade_color` by `kill_count` (client 3474). The Ancient Weapon titles
(`unknown_03` `247`) step 100, 500, 1,000, 2,000 and 5,000; every other
group 100, 1,000, 3,000, 5,000 and 10,000.

| `grade_color` | Colour | Ancient Weapons | Other groups |
| ------------- | ------ | --------------- | ------------ |
| `0xFFFFFFFF`  | White  | 100             | 100          |
| `0xFF2DC200`  | Green  | 500             | 1,000        |
| `0xFF0F47FF`  | Blue   | 1,000           | 3,000        |
| `0xFFF3D900`  | Yellow | 2,000           | 5,000        |
| `0xFFF32200`  | Orange | 5,000           | 10,000       |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The names follow the Hardcore character
window of client 3474 (`panel_characterinfo_hardcore_basic_all_1.luac` and
`_2.luac`): it lists the titles with `ToClient_getHardCoreTitleCount()` and
`ToClient_getHardCoreTitleKeyByIndex(index)`, then shows each key's
`ToClient_getHardCoreTitleNameByKey`, `...DescByKey` and
`...ConditionByKey` text and colours the name with
`ToClient_GetHardCoreTitleGradeColor`. The three strings of every row are
a name, a description ("<난폭한> 사막 나가 처치", defeat the Desert Naga) and
a condition with a count ("... 100마리 처치", defeat 100), in that order.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- `unknown_03` pairs per monster group: the "<난폭한>" (violent) titles of a
  group hold one value and the "<격노한>" (enraged) titles another, ten
  apart (Desert Naga `251` and `241`, Hystria `256` and `246`); the
  Ancient Weapon titles hold `247` only and the Gahaz Bandits `259` and
  `258`.
- No field points into LOC, so the handler shows the Korean name,
  description and condition.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`.

## Open Questions

### Monster Group Value

What `unknown_03` names. One value per monster group and kind fits a kill
group key, but no Lua call reads it, no LOC type 116 hunting ground has the
key, and the second copy at `unknown_13` shows no difference on any row.

### Title Rank Value

What `unknown_0f` is. It runs `0` to `4` for the Ancient Weapon titles,
`10` to `19` for the Naga, Fogan, Crescent and Gahaz titles, `20` to `29`
for Pila Ku and Aakman and `30` to `39` for Hystria, one step per title
of a group, so the Naga, Fogan, Crescent and Gahaz "Tracker" titles all hold
`10`. It may pick the title's look in `ToClient_insertNewTitleUI(key32,
content)`, which the title list calls with the key.
