# `hardcorechanneletcoptionstaticstatus.bss` Format

## Purpose

The settings of the Hardcore channel: 83 bytes of unnamed numbers, a
counted list of two (u8, f32, u16) entries, an f32 and the class types that
can create a Hardcore character. On client 3474 that class list holds 29
class types, every playable class but Wukong, Seraph and Agent. The class
types are those of [`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md),
which holds a stat row per class type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------ | ----- | ------- | --------- |
| 1      | 2834 and later | 3483    | `hardcorechanneletcoptionstaticstatus.bss` | 154   | 2 Entry | 7         |

| Layout | File                                       | Known        | Unknown       |
| ------ | ------------------------------------------ | ------------ | ------------- |
| 1      | `hardcorechanneletcoptionstaticstatus.bss` | 49 B (31.8%) | 105 B (68.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `09c5b527390c`  |
| 3482   | Layout 1 | `09c5b527390c`  |
| 3474   | Layout 1 | `09c5b527390c`  |
| 3473   | Layout 1 | `09c5b527390c`  |
| 3464   | Layout 1 | `09c5b527390c`  |
| 3458   | Layout 1 | `09c5b527390c`  |
| 3454   | Layout 1 | `09c5b527390c`  |
| 3444   | Layout 1 | `09c5b527390c`  |
| 3435   | Layout 1 | `09c5b527390c`  |
| 3426   | Layout 1 | `09c5b527390c`  |
| 3418   | Layout 1 | `09c5b527390c`  |
| 3412   | Layout 1 | `09c5b527390c`  |
| 3402   | Layout 1 | `09c5b527390c`  |
| 3396   | Layout 1 | `09c5b527390c`  |
| 3387   | Layout 1 | `09c5b527390c`  |
| 3381   | Layout 1 | `09c5b527390c`  |
| 3373   | Layout 1 | `09c5b527390c`  |
| 3364   | Layout 1 | `09c5b527390c`  |
| 3356   | Layout 1 | `09c5b527390c`  |
| 3349   | Layout 1 | `09c5b527390c`  |
| 3342   | Layout 1 | `09c5b527390c`  |
| 3335   | Layout 1 | `09c5b527390c`  |
| 3326   | Layout 1 | `09c5b527390c`  |
| 3321   | Layout 1 | `09c5b527390c`  |
| 3314   | Layout 1 | `09c5b527390c`  |
| 3303   | Layout 1 | `09c5b527390c`  |
| 3302   | Layout 1 | `09c5b527390c`  |
| 3293   | Layout 1 | `09c5b527390c`  |
| 3283   | Layout 1 | `09c5b527390c`  |
| 3275   | Layout 1 | `09c5b527390c`  |
| 3267   | Layout 1 | `09c5b527390c`  |
| 3258   | Layout 1 | `09c5b527390c`  |
| 3251   | Layout 1 | `09c5b527390c`  |
| 3242   | Layout 1 | `09c5b527390c`  |
| 3235   | Layout 1 | `09c5b527390c`  |
| 3229   | Layout 1 | `09c5b527390c`  |
| 3212   | Layout 1 | `09c5b527390c`  |
| 3203   | Layout 1 | `09c5b527390c`  |
| 3193   | Layout 1 | `09c5b527390c`  |
| 3186   | Layout 1 | `09c5b527390c`  |
| 3177   | Layout 1 | `09c5b527390c`  |
| 3169   | Layout 1 | `09c5b527390c`  |
| 3158   | Layout 1 | `09c5b527390c`  |
| 3151   | Layout 1 | `09c5b527390c`  |
| 3144   | Layout 1 | `09c5b527390c`  |
| 3133   | Layout 1 | `09c5b527390c`  |
| 3125   | Layout 1 | `09c5b527390c`  |
| 3118   | Layout 1 | `09c5b527390c`  |
| 3111   | Layout 1 | `09c5b527390c`  |
| 3103   | Layout 1 | `09c5b527390c`  |
| 3095   | Layout 1 | `09c5b527390c`  |
| 3086   | Layout 1 | `09c5b527390c`  |
| 3072   | Layout 1 | `09c5b527390c`  |
| 3062   | Layout 1 | `09c5b527390c`  |
| 3052   | Layout 1 | `09c5b527390c`  |
| 3045   | Layout 1 | `09c5b527390c`  |
| 3037   | Layout 1 | `09c5b527390c`  |
| 3030   | Layout 1 | `09c5b527390c`  |
| 3021   | Layout 1 | `09c5b527390c`  |
| 3012   | Layout 1 | `09c5b527390c`  |
| 3002   | Layout 1 | `09c5b527390c`  |
| 2995   | Layout 1 | `09c5b527390c`  |
| 2987   | Layout 1 | `09c5b527390c`  |
| 2978   | Layout 1 | `09c5b527390c`  |
| 2970   | Layout 1 | `09c5b527390c`  |
| 2959   | Layout 1 | `09c5b527390c`  |
| 2951   | Layout 1 | `09c5b527390c`  |
| 2942   | Layout 1 | `09c5b527390c`  |
| 2935   | Layout 1 | `09c5b527390c`  |
| 2932   | Layout 1 | `09c5b527390c`  |
| 2923   | Layout 1 | `09c5b527390c`  |
| 2919   | Layout 1 | `09c5b527390c`  |
| 2907   | Layout 1 | `09c5b527390c`  |
| 2900   | Layout 1 | `09c5b527390c`  |
| 2891   | Layout 1 | `09c5b527390c`  |
| 2882   | Layout 1 | `09c5b527390c`  |
| 2872   | Layout 1 | `09c5b527390c`  |
| 2863   | Layout 1 | `09c5b527390c`  |
| 2855   | Layout 1 | `09c5b527390c`  |
| 2849   | Layout 1 | `09c5b527390c`  |
| 2844   | Layout 1 | `09c5b527390c`  |
| 2834   | Layout 1 | `09c5b527390c`  |
| 2825   | No file  | `09c5b527390c`  |
| 2819   | No file  | `09c5b527390c`  |
| 2811   | No file  | `09c5b527390c`  |
| 2803   | No file  | `09c5b527390c`  |
| 2794   | No file  | `09c5b527390c`  |
| 2783   | No file  | `09c5b527390c`  |
| 2774   | No file  | `09c5b527390c`  |
| 2765   | No file  | `09c5b527390c`  |
| 2756   | No file  | `09c5b527390c`  |
| 2750   | No file  | `09c5b527390c`  |
| 2743   | No file  | `09c5b527390c`  |
| 2736   | No file  | `09c5b527390c`  |
| 2726   | No file  | `09c5b527390c`  |
| 2717   | No file  | `09c5b527390c`  |
| 2709   | No file  | `09c5b527390c`  |
| 2703   | No file  | `09c5b527390c`  |
| 2695   | No file  | `09c5b527390c`  |
| 2684   | No file  | `09c5b527390c`  |
| 2672   | No file  | `09c5b527390c`  |
| 2665   | No file  | `09c5b527390c`  |
| 2657   | No file  | `09c5b527390c`  |
| 2649   | No file  | `09c5b527390c`  |
| 2644   | No file  | `09c5b527390c`  |
| 2637   | No file  | `09c5b527390c`  |
| 2629   | No file  | `09c5b527390c`  |
| 2619   | No file  | `09c5b527390c`  |
| 2612   | No file  | `09c5b527390c`  |
| 2606   | No file  | `09c5b527390c`  |
| 2602   | No file  | `09c5b527390c`  |
| 2601   | No file  | `09c5b527390c`  |
| 2592   | No file  | `09c5b527390c`  |
| 2583   | No file  | `09c5b527390c`  |
| 2575   | No file  | `09c5b527390c`  |
| 2567   | No file  | `09c5b527390c`  |
| 2560   | No file  | `09c5b527390c`  |
| 2553   | No file  | `09c5b527390c`  |
| 2545   | No file  | `09c5b527390c`  |
| 2538   | No file  | `09c5b527390c`  |
| 2529   | No file  | `09c5b527390c`  |
| 2519   | No file  | `09c5b527390c`  |
| 2513   | No file  | `09c5b527390c`  |
| 2510   | No file  | `09c5b527390c`  |
| 2507   | No file  | `09c5b527390c`  |
| 2503   | No file  | `09c5b527390c`  |
| 2498   | No file  | `09c5b527390c`  |
| 2492   | No file  | `09c5b527390c`  |
| 2487   | No file  | `09c5b527390c`  |
| 2480   | No file  | `09c5b527390c`  |
| 2474   | No file  | `09c5b527390c`  |
| 2468   | No file  | `09c5b527390c`  |
| 2460   | No file  | `09c5b527390c`  |
| 2453   | No file  | `09c5b527390c`  |
| 2444   | No file  | `09c5b527390c`  |
| 2438   | No file  | `09c5b527390c`  |
| 2434   | No file  | `09c5b527390c`  |
| 2429   | No file  | `09c5b527390c`  |
| 2421   | No file  | `09c5b527390c`  |
| 2414   | No file  | `09c5b527390c`  |
| 2407   | No file  | `09c5b527390c`  |
| 2401   | No file  | `09c5b527390c`  |
| 2397   | No file  | `09c5b527390c`  |
| 2393   | No file  | `09c5b527390c`  |
| 2384   | No file  | `09c5b527390c`  |
| 2378   | No file  | `09c5b527390c`  |
| 2372   | No file  | `09c5b527390c`  |
| 2358   | No file  | `09c5b527390c`  |
| 2352   | No file  | `09c5b527390c`  |
| 2347   | No file  | `09c5b527390c`  |
| 2343   | No file  | `09c5b527390c`  |
| 2335   | No file  | `09c5b527390c`  |
| 2327   | No file  | `09c5b527390c`  |
| 2324   | No file  | `09c5b527390c`  |
| 2319   | No file  | `09c5b527390c`  |
| 2313   | No file  | `09c5b527390c`  |
| 2308   | No file  | `09c5b527390c`  |
| 2302   | No file  | `09c5b527390c`  |
| 2295   | No file  | `09c5b527390c`  |
| 2290   | No file  | `09c5b527390c`  |
| 2284   | No file  | `09c5b527390c`  |
| 2276   | No file  | `09c5b527390c`  |
| 2269   | No file  | `09c5b527390c`  |
| 2259   | No file  | `09c5b527390c`  |
| 2250   | No file  | `09c5b527390c`  |
| 2243   | No file  | `09c5b527390c`  |
| 2235   | No file  | `09c5b527390c`  |
| 2229   | No file  | `09c5b527390c`  |
| 2224   | No file  | `09c5b527390c`  |
| 2218   | No file  | `09c5b527390c`  |
| 2215   | No file  | `09c5b527390c`  |
| 2207   | No file  | `09c5b527390c`  |
| 2203   | No file  | `09c5b527390c`  |
| 2196   | No file  | `09c5b527390c`  |
| 2192   | No file  | `09c5b527390c`  |
| 2189   | No file  | `09c5b527390c`  |
| 2183   | No file  | `09c5b527390c`  |
| 2179   | No file  | `09c5b527390c`  |
| 2171   | No file  | `09c5b527390c`  |
| 2163   | No file  | `09c5b527390c`  |
| 2156   | No file  | `09c5b527390c`  |
| 2151   | No file  | `09c5b527390c`  |
| 2147   | No file  | `09c5b527390c`  |
| 2142   | No file  | `09c5b527390c`  |
| 2138   | No file  | `09c5b527390c`  |
| 2134   | No file  | `09c5b527390c`  |
| 2130   | No file  | `09c5b527390c`  |
| 2122   | No file  | `09c5b527390c`  |
| 2107   | No file  | `09c5b527390c`  |
| 2098   | No file  | `09c5b527390c`  |
| 2089   | No file  | `09c5b527390c`  |
| 2081   | No file  | `09c5b527390c`  |
| 2073   | No file  | `09c5b527390c`  |
| 2067   | No file  | `09c5b527390c`  |
| 2063   | No file  | `09c5b527390c`  |
| 2059   | No file  | `09c5b527390c`  |
| 2052   | No file  | `09c5b527390c`  |
| 2044   | No file  | `09c5b527390c`  |
| 2039   | No file  | `09c5b527390c`  |
| 2032   | No file  | `09c5b527390c`  |
| 2025   | No file  | `09c5b527390c`  |
| 2011   | No file  | `09c5b527390c`  |
| 2005   | No file  | `09c5b527390c`  |
| 2000   | No file  | `09c5b527390c`  |
| 1996   | No file  | `09c5b527390c`  |
| 1991   | No file  | `09c5b527390c`  |
| 1985   | No file  | `09c5b527390c`  |
| 1980   | No file  | `09c5b527390c`  |
| 1969   | No file  | `09c5b527390c`  |
| 1964   | No file  | `09c5b527390c`  |
| 1958   | No file  | `09c5b527390c`  |
| 1950   | No file  | `09c5b527390c`  |
| 1945   | No file  | `09c5b527390c`  |
| 1937   | No file  | `09c5b527390c`  |
| 1933   | No file  | `09c5b527390c`  |
| 1927   | No file  | `09c5b527390c`  |
| 1921   | No file  | `09c5b527390c`  |
| 1914   | No file  | `09c5b527390c`  |
| 1908   | No file  | `09c5b527390c`  |
| 1897   | No file  | `09c5b527390c`  |
| 1892   | No file  | `09c5b527390c`  |
| 1886   | No file  | `09c5b527390c`  |
| 1881   | No file  | `09c5b527390c`  |
| 1871   | No file  | `09c5b527390c`  |
| 1866   | No file  | `09c5b527390c`  |
| 1862   | No file  | `09c5b527390c`  |
| 1854   | No file  | `09c5b527390c`  |
| 1846   | No file  | `09c5b527390c`  |
| 1838   | No file  | `09c5b527390c`  |
| 1832   | No file  | `09c5b527390c`  |
| 1826   | No file  | `09c5b527390c`  |
| 1822   | No file  | `09c5b527390c`  |
| 1818   | No file  | `09c5b527390c`  |
| 1804   | No file  | `09c5b527390c`  |
| 1794   | No file  | `09c5b527390c`  |
| 1790   | No file  | `09c5b527390c`  |
| 1784   | No file  | `09c5b527390c`  |
| 1774   | No file  | `09c5b527390c`  |
| 1771   | No file  | `09c5b527390c`  |
| 1762   | No file  | `09c5b527390c`  |
| 1759   | No file  | `09c5b527390c`  |
| 1754   | No file  | `09c5b527390c`  |
| 1749   | No file  | `09c5b527390c`  |
| 1743   | No file  | `09c5b527390c`  |
| 1737   | No file  | `09c5b527390c`  |
| 1731   | No file  | `09c5b527390c`  |
| 1725   | No file  | `09c5b527390c`  |
| 1717   | No file  | `09c5b527390c`  |
| 1710   | No file  | `09c5b527390c`  |
| 1704   | No file  | `09c5b527390c`  |
| 1698   | No file  | `09c5b527390c`  |
| 1690   | No file  | `09c5b527390c`  |
| 1685   | No file  | `09c5b527390c`  |
| 1680   | No file  | `09c5b527390c`  |
| 1674   | No file  | `09c5b527390c`  |
| 1668   | No file  | `09c5b527390c`  |
| 1659   | No file  | `09c5b527390c`  |
| 1649   | No file  | `09c5b527390c`  |
| 1642   | No file  | `09c5b527390c`  |
| 1636   | No file  | `09c5b527390c`  |
| 1628   | No file  | `09c5b527390c`  |
| 1622   | No file  | `09c5b527390c`  |
| 1614   | No file  | `09c5b527390c`  |
| 1608   | No file  | `09c5b527390c`  |
| 1602   | No file  | `09c5b527390c`  |
| 1598   | No file  | `09c5b527390c`  |
| 1594   | No file  | `09c5b527390c`  |
| 1590   | No file  | `09c5b527390c`  |
| 1587   | No file  | `09c5b527390c`  |
| 1584   | No file  | `09c5b527390c`  |
| 1579   | No file  | `09c5b527390c`  |
| 1572   | No file  | `09c5b527390c`  |
| 1565   | No file  | `09c5b527390c`  |
| 1559   | No file  | `09c5b527390c`  |
| 1554   | No file  | `09c5b527390c`  |
| 1547   | No file  | `09c5b527390c`  |
| 1537   | No file  | `09c5b527390c`  |
| 1529   | No file  | `09c5b527390c`  |
| 1524   | No file  | `09c5b527390c`  |
| 1519   | No file  | `09c5b527390c`  |
| 1509   | No file  | `09c5b527390c`  |
| 1506   | No file  | `09c5b527390c`  |
| 1504   | No file  | `09c5b527390c`  |
| 1500   | No file  | `09c5b527390c`  |
| 1493   | No file  | `09c5b527390c`  |
| 1489   | No file  | `09c5b527390c`  |
| 1485   | No file  | `09c5b527390c`  |
| 1481   | No file  | `09c5b527390c`  |
| 1474   | No file  | `09c5b527390c`  |
| 1466   | No file  | `09c5b527390c`  |
| 1462   | No file  | `09c5b527390c`  |
| 1459   | No file  | `09c5b527390c`  |
| 1453   | No file  | `09c5b527390c`  |
| 1450   | No file  | `09c5b527390c`  |
| 1445   | No file  | `09c5b527390c`  |
| 1439   | No file  | `09c5b527390c`  |
| 1433   | No file  | `09c5b527390c`  |
| 1430   | No file  | `09c5b527390c`  |
| 1426   | No file  | `09c5b527390c`  |
| 1421   | No file  | `09c5b527390c`  |
| 1417   | No file  | `09c5b527390c`  |
| 1416   | No file  | `09c5b527390c`  |
| 1409   | No file  | `09c5b527390c`  |
| 1405   | No file  | `09c5b527390c`  |
| 1401   | No file  | `09c5b527390c`  |
| 1396   | No file  | `09c5b527390c`  |
| 1391   | No file  | `09c5b527390c`  |
| 1390   | No file  | `09c5b527390c`  |
| 1386   | No file  | `09c5b527390c`  |
| 1381   | No file  | `09c5b527390c`  |
| 1379   | No file  | `09c5b527390c`  |
| 1372   | No file  | `09c5b527390c`  |
| 1366   | No file  | `09c5b527390c`  |
| 1364   | No file  | `09c5b527390c`  |
| 1363   | No file  | `09c5b527390c`  |
| 1360   | No file  | `09c5b527390c`  |
| 1358   | No file  | `09c5b527390c`  |
| 1355   | No file  | `09c5b527390c`  |
| 1351   | No file  | `09c5b527390c`  |
| 1348   | No file  | `09c5b527390c`  |
| 1346   | No file  | `09c5b527390c`  |
| 1341   | No file  | `09c5b527390c`  |
| 1340   | No file  | `09c5b527390c`  |
| 1338   | No file  | `09c5b527390c`  |
| 1335   | No file  | `09c5b527390c`  |
| 1333   | No file  | `09c5b527390c`  |
| 1329   | No file  | `09c5b527390c`  |
| 1327   | No file  | `09c5b527390c`  |
| 1324   | No file  | `09c5b527390c`  |
| 1321   | No file  | `09c5b527390c`  |
| 1319   | No file  | `09c5b527390c`  |
| 1318   | No file  | `09c5b527390c`  |
| 1316   | No file  | `09c5b527390c`  |
| 1313   | No file  | `09c5b527390c`  |
| 1311   | No file  | `09c5b527390c`  |
| 1309   | No file  | `09c5b527390c`  |
| 1304   | No file  | `09c5b527390c`  |
| 1292   | No file  | `09c5b527390c`  |
| 1286   | No file  | `09c5b527390c`  |
| 1280   | No file  | `09c5b527390c`  |
| 1276   | No file  | `09c5b527390c`  |
| 1267   | No file  | `09c5b527390c`  |
| 1261   | No file  | `09c5b527390c`  |
| 1256   | No file  | `09c5b527390c`  |
| 1250   | No file  | `09c5b527390c`  |
| 1246   | No file  | `09c5b527390c`  |
| 1239   | No file  | `09c5b527390c`  |
| 1230   | No file  | `09c5b527390c`  |
| 1226   | No file  | `09c5b527390c`  |
| 1220   | No file  | `09c5b527390c`  |
| 1217   | No file  | `09c5b527390c`  |
| 1211   | No file  | `09c5b527390c`  |
| 1210   | No file  | `09c5b527390c`  |
| 1208   | No file  | `09c5b527390c`  |
| 1203   | No file  | `09c5b527390c`  |
| 1197   | No file  | `09c5b527390c`  |
| 1194   | No file  | `09c5b527390c`  |
| 1192   | No file  | `09c5b527390c`  |
| 1187   | No file  | `09c5b527390c`  |
| 1183   | No file  | `09c5b527390c`  |
| 1177   | No file  | `09c5b527390c`  |
| 1173   | No file  | `09c5b527390c`  |
| 1167   | No file  | `09c5b527390c`  |
| 1164   | No file  | `09c5b527390c`  |
| 1156   | No file  | `09c5b527390c`  |
| 1149   | No file  | `09c5b527390c`  |
| 1144   | No file  | `09c5b527390c`  |
| 1137   | No file  | `09c5b527390c`  |
| 1132   | No file  | `09c5b527390c`  |
| 1127   | No file  | `09c5b527390c`  |
| 1122   | No file  | `09c5b527390c`  |
| 1118   | No file  | `09c5b527390c`  |
| 1114   | No file  | `09c5b527390c`  |
| 1109   | No file  | `09c5b527390c`  |
| 1102   | No file  | `09c5b527390c`  |
| 1096   | No file  | `09c5b527390c`  |
| 1088   | No file  | `09c5b527390c`  |
| 1081   | No file  | `09c5b527390c`  |
| 1076   | No file  | `09c5b527390c`  |
| 1069   | No file  | `09c5b527390c`  |
| 1064   | No file  | `09c5b527390c`  |
| 1058   | No file  | `09c5b527390c`  |
| 1051   | No file  | `09c5b527390c`  |
| 1044   | No file  | `09c5b527390c`  |
| 1036   | No file  | `09c5b527390c`  |
| 1026   | No file  | `09c5b527390c`  |
| 1016   | No file  | `09c5b527390c`  |
| 1009   | No file  | `09c5b527390c`  |
| 1005   | No file  | `09c5b527390c`  |
| 1000   | No file  | `09c5b527390c`  |
| 998    | No file  | `09c5b527390c`  |
| 990    | No file  | `09c5b527390c`  |
| 979    | No file  | `09c5b527390c`  |
| 972    | No file  | `09c5b527390c`  |
| 963    | No file  | `09c5b527390c`  |
| 955    | No file  | `09c5b527390c`  |
| 946    | No file  | `09c5b527390c`  |
| 938    | No file  | `09c5b527390c`  |
| 927    | No file  | `09c5b527390c`  |
| 911    | No file  | `09c5b527390c`  |
| 904    | No file  | `09c5b527390c`  |
| 899    | No file  | `09c5b527390c`  |
| 894    | No file  | `09c5b527390c`  |
| 885    | No file  | `09c5b527390c`  |
| 879    | No file  | `09c5b527390c`  |
| 872    | No file  | `09c5b527390c`  |
| 864    | No file  | `09c5b527390c`  |
| 855    | No file  | `09c5b527390c`  |
| 853    | No file  | `09c5b527390c`  |
| 845    | No file  | `09c5b527390c`  |
| 837    | No file  | `09c5b527390c`  |
| 829    | No file  | `09c5b527390c`  |
| 822    | No file  | `09c5b527390c`  |
| 814    | No file  | `09c5b527390c`  |
| 805    | No file  | `09c5b527390c`  |
| 794    | No file  | `09c5b527390c`  |
| 787    | No file  | `09c5b527390c`  |
| 780    | No file  | `09c5b527390c`  |
| 771    | No file  | `09c5b527390c`  |
| 760    | No file  | `09c5b527390c`  |
| 748    | No file  | `09c5b527390c`  |
| 741    | No file  | `09c5b527390c`  |
| 736    | No file  | `09c5b527390c`  |
| 731    | No file  | `09c5b527390c`  |
| 723    | No file  | `09c5b527390c`  |
| 711    | No file  | `09c5b527390c`  |
| 707    | No file  | `09c5b527390c`  |
| 697    | No file  | `09c5b527390c`  |
| 689    | No file  | `09c5b527390c`  |
| 683    | No file  | `09c5b527390c`  |
| 678    | No file  | `09c5b527390c`  |
| 670    | No file  | `09c5b527390c`  |
| 661    | No file  | `09c5b527390c`  |
| 656    | No file  | `09c5b527390c`  |
| 652    | No file  | `09c5b527390c`  |
| 643    | No file  | `09c5b527390c`  |
| 637    | No file  | `09c5b527390c`  |
| 630    | No file  | `09c5b527390c`  |
| 627    | No file  | `09c5b527390c`  |
| 621    | No file  | `09c5b527390c`  |
| 617    | No file  | `09c5b527390c`  |
| 615    | No file  | `09c5b527390c`  |
| 606    | No file  | `09c5b527390c`  |
| 599    | No file  | `09c5b527390c`  |
| 592    | No file  | `09c5b527390c`  |
| 586    | No file  | `09c5b527390c`  |
| 577    | No file  | `09c5b527390c`  |
| 569    | No file  | `09c5b527390c`  |
| 561    | No file  | `09c5b527390c`  |
| 554    | No file  | `09c5b527390c`  |
| 542    | No file  | `09c5b527390c`  |
| 532    | No file  | `09c5b527390c`  |
| 531    | No file  | `09c5b527390c`  |
| 526    | No file  | `09c5b527390c`  |
| 521    | No file  | `09c5b527390c`  |
| 517    | No file  | `09c5b527390c`  |
| 510    | No file  | `09c5b527390c`  |
| 508    | No file  | `09c5b527390c`  |
| 504    | No file  | `09c5b527390c`  |
| 497    | No file  | `09c5b527390c`  |
| 491    | No file  | `09c5b527390c`  |
| 485    | No file  | `09c5b527390c`  |
| 478    | No file  | `09c5b527390c`  |
| 472    | No file  | `09c5b527390c`  |
| 466    | No file  | `09c5b527390c`  |
| 457    | No file  | `09c5b527390c`  |
| 452    | No file  | `09c5b527390c`  |
| 449    | No file  | `09c5b527390c`  |
| 435    | No file  | `09c5b527390c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Class names, LOC type 21    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                         | Field                | Notes                                                              |
| ---------------------------- | ---------------------------- | -------------------- | ------------------------------------------------------------------ |
| `+0x00`                      | char[4]                      | magic                | ASCII `PABR`                                                       |
| `+0x04`                      | u32                          | unknown_04           | `60` on client 3474                                                |
| `+0x08`                      | u32                          | unknown_08           | `2` on client 3474                                                 |
| `+0x0C`                      | u16                          | unknown_0c           | `60` on client 3474                                                |
| `+0x0E`                      | u8                           | unknown_0e           | `1` on client 3474                                                 |
| `+0x0F`                      | u32                          | unknown_0f           | `60` on client 3474                                                |
| `+0x13`                      | u32                          | unknown_13           | `50` on client 3474                                                |
| `+0x17`                      | u32                          | unknown_17           | `100000` on client 3474                                            |
| `+0x1B`                      | u32                          | unknown_1b           | `300000` on client 3474                                            |
| `+0x1F`                      | u32                          | unknown_1f           | `10000` on client 3474                                             |
| `+0x23`                      | u32                          | unknown_23           | `3000` on client 3474                                              |
| `+0x27`                      | u32                          | unknown_27           | `200000` on client 3474                                            |
| `+0x2B`                      | u32                          | unknown_2b           | `300000` on client 3474                                            |
| `+0x2F`                      | u32                          | unknown_2f           | `3` on client 3474                                                 |
| `+0x33`                      | u32                          | unknown_33           | `500` on client 3474                                               |
| `+0x37`                      | u32                          | unknown_37           | `300` on client 3474                                               |
| `+0x3B`                      | i32                          | unknown_3b           | `-40` on client 3474                                               |
| `+0x3F`                      | u64                          | unknown_3f           | `100` on client 3474                                               |
| `+0x47`                      | u64                          | unknown_47           | `50` on client 3474                                                |
| `+0x4F`                      | u64                          | unknown_4f           | `20` on client 3474                                                |
| `+0x57`                      | u32                          | unknown_entry_count  | Number of `unknown_entries`; `2` on client 3474                     |
| `+0x5B`                      | Entry[unknown_entry_count]   | unknown_entries      | See Entry                                                          |
| `unknown_entries+0x00`       | f32                          | unknown_entries_00   | `74.0` on client 3474, the f32 of entry `1`                        |
| `unknown_entries+0x04`       | u32                          | class_count          | Number of `possible_class_types`                                   |
| `unknown_entries+0x08`       | u8[class_count]              | possible_class_types | Class types that can create a Hardcore character; see Classes      |
| `possible_class_types+0x00`  | String Table                 | string_table         | See String Table                                                   |
| `string_table+0x00`          | u32                          | table_start          | Offset of the string table, where `possible_class_types` ends      |
| `string_table+0x04`          | u32                          | zero                 | Always `0`                                                         |

### Entry (7 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | `1` and `2` on client 3474                               |
| `+0x01` | f32  | unknown_01 | `74.0` with `1`, `37.0` with `2` on client 3474          |
| `+0x05` | u16  | unknown_05 | `1` on both entries                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Classes

`possible_class_types` on client 3474, by LOC type 21 name: Warrior (0),
Hashashin (1), Sage (2), Ranger (4), Guardian (5), Scholar (6), Drakania
(7), Sorceress (8), Nova (9), Corsair (10), Lahn (11), Berserker (12),
Maegu (15), Tamer (16), Shai (17), Striker (19), Musa (20), Maehwa (21),
Mystic (23), Valkyrie (24), Kunoichi (25), Ninja (26), Dark Knight (27),
Wizard (28), Archer (29), Woosa (30), Witch (31), Dosa (33) and Deadeye
(34). Wukong (3), Seraph (32) and Agent (35) are missing, besides the
unused class types 13, 14, 18 and 22.

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. `possible_class_types` follows the client
Lua of client 3474: the class select windows
(`panel_lobby_classselect_renew.luac` and `panel_lobby_main.luac`) read
the classes a Hardcore character can take with
`ToClient_getHardCorePossbieClassCount()` and
`ToClient_getHardCorePossbieClassFromIndex(index)`, a count and a class
type per index, and every value of the list has a LOC type 21 class name.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The LOC type 37 server text that opened Hardcore characters to Warrior,
  Ranger, Sorceress and Berserker
  ([`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md)
  Notes) names fewer classes than this list, which holds the same 29 on
  clients 3002 to 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  the class list by name.

## Open Questions

### Unnamed Settings

Which value each Hardcore getter of the client 3474 Lua returns. The Lua
reads `ToClient_isHardCoreChannelEnterPossibleLevel()` (the level in
"LUA_HARDCORECHANNEL_CANTPLAY_NOTIFY"), `ToClient_getHardCoreMaxBossCount()`,
`ToClient_getHardCoreHighRankerMaxCount()`,
`ToClient_getHardCoreRepeatQuestCountMax()`,
`ToClient_getHardCoreExchangeCoinMaxCount()` and
`ToClient_GetHardCoreCharacterRespawnTime()`, and none of them is a plain
match: `60` appears three times, `2` fits the two bosses of
[`hardcorerandomspawncharacterstaticstatusmanager.bss`](hardcorerandomspawncharacterstaticstatusmanager_bss.md),
`3` the three top ranks, `500` and `300` a coin cap and a respawn time.

### Alert Entries

What `unknown_entries` and `unknown_entries_00` hold. The enemy alert
widget (`panel_widget_enemyalert_hardcore_1.luac`) reads
`ToClient_GetHardCoreNearPlayerAlertLevel()` and shows one effect for level
`1` and another for `2`. The entries are numbered `1` and `2`, the f32 of
`2` is half that of `1` (`37.0` and `74.0`), and `unknown_entries_00`
repeats `74.0`, which fits a distance per alert level, but no Lua reads the
values.
