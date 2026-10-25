# `guildhonorsystem.bss` Format

## Purpose

The Guild Fame system (`_ContentsGroup_GuildHonorSystem`): how many points each guild activity earns or costs, the benefits a guild unlocks at a Guild Fame threshold, and the Bonus Guild Daily Pay steps. The Guild Fame Benefits window (`panel_window_guildhonorbenefitguide_all`) lists all three. The file has no PABR magic and no string table: a head of eight u64 values, then three u32-counted lists. On client 3482 they hold 26 change reasons (12 gains, 14 costs), 22 benefits and 10 daily pay steps. Clients 3356 to 3387 store the gains and the costs as lists of their own, and clients 3356 to 3381 write an address before every row (Layouts 1 to 3).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records                                          | Row bytes               |
| ------ | -------------- | ---------------------- | ----- | ------------------------------------------------ | ----------------------- |
| 4      | 3402 and later | `guildhonorsystem.bss` | 3,472 | 26 Change Reason, 22 Benefit, 10 Daily Incentive | 46 to 78, 57 on average |
| 3      | 3387           | `guildhonorsystem.bss` | 1,591 | 20 Change Reason, 13 Benefit, 6 Daily Incentive  | 16                      |
| 2      | 3373 to 3381   | `guildhonorsystem.bss` | 1,236 | 20 Change Reason, 13 Benefit, 6 Daily Incentive  | 24                      |
| 1      | 3356 to 3364   | `guildhonorsystem.bss` | 732   | 20 Change Reason, 6 Unknown Row                  | 24                      |

| Layout | File                   | Known           | Unknown       |
| ------ | ---------------------- | --------------- | ------------- |
| 4      | `guildhonorsystem.bss` | 3,464 B (99.8%) | 8 B (0.2%)    |
| 3      | `guildhonorsystem.bss` | 1,527 B (96.0%) | 64 B (4.0%)   |
| 2      | `guildhonorsystem.bss` | 868 B (70.2%)   | 368 B (29.8%) |
| 1      | `guildhonorsystem.bss` | 370 B (50.5%)   | 362 B (49.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `3f441f74159c`  |
| 3482   | Layout 4 | `d6ba5a352381`  |
| 3474   | Layout 4 | `d6ba5a352381`  |
| 3473   | Layout 4 | `d6ba5a352381`  |
| 3464   | Layout 4 | `d6ba5a352381`  |
| 3458   | Layout 4 | `d6ba5a352381`  |
| 3454   | Layout 4 | `d6ba5a352381`  |
| 3444   | Layout 4 | `d6ba5a352381`  |
| 3435   | Layout 4 | `d6ba5a352381`  |
| 3426   | Layout 4 | `d6ba5a352381`  |
| 3418   | Layout 4 | `d6ba5a352381`  |
| 3412   | Layout 4 | `d6ba5a352381`  |
| 3402   | Layout 4 | `d6ba5a352381`  |
| 3396   | No file  | `d6ba5a352381`  |
| 3387   | Layout 3 | `d6ba5a352381`  |
| 3381   | Layout 2 | `d6ba5a352381`  |
| 3373   | Layout 2 | `d6ba5a352381`  |
| 3364   | Layout 1 | `d6ba5a352381`  |
| 3356   | Layout 1 | `d6ba5a352381`  |
| 3349   | No file  | `d6ba5a352381`  |
| 3342   | No file  | `d6ba5a352381`  |
| 3335   | No file  | `d6ba5a352381`  |
| 3326   | No file  | `d6ba5a352381`  |
| 3321   | No file  | `d6ba5a352381`  |
| 3314   | No file  | `d6ba5a352381`  |
| 3303   | No file  | `d6ba5a352381`  |
| 3302   | No file  | `d6ba5a352381`  |
| 3293   | No file  | `d6ba5a352381`  |
| 3283   | No file  | `d6ba5a352381`  |
| 3275   | No file  | `d6ba5a352381`  |
| 3267   | No file  | `d6ba5a352381`  |
| 3258   | No file  | `d6ba5a352381`  |
| 3251   | No file  | `d6ba5a352381`  |
| 3242   | No file  | `d6ba5a352381`  |
| 3235   | No file  | `d6ba5a352381`  |
| 3229   | No file  | `d6ba5a352381`  |
| 3212   | No file  | `d6ba5a352381`  |
| 3203   | No file  | `d6ba5a352381`  |
| 3193   | No file  | `d6ba5a352381`  |
| 3186   | No file  | `d6ba5a352381`  |
| 3177   | No file  | `d6ba5a352381`  |
| 3169   | No file  | `d6ba5a352381`  |
| 3158   | No file  | `d6ba5a352381`  |
| 3151   | No file  | `d6ba5a352381`  |
| 3144   | No file  | `d6ba5a352381`  |
| 3133   | No file  | `d6ba5a352381`  |
| 3125   | No file  | `d6ba5a352381`  |
| 3118   | No file  | `d6ba5a352381`  |
| 3111   | No file  | `d6ba5a352381`  |
| 3103   | No file  | `d6ba5a352381`  |
| 3095   | No file  | `d6ba5a352381`  |
| 3086   | No file  | `d6ba5a352381`  |
| 3072   | No file  | `d6ba5a352381`  |
| 3062   | No file  | `d6ba5a352381`  |
| 3052   | No file  | `d6ba5a352381`  |
| 3045   | No file  | `d6ba5a352381`  |
| 3037   | No file  | `d6ba5a352381`  |
| 3030   | No file  | `d6ba5a352381`  |
| 3021   | No file  | `d6ba5a352381`  |
| 3012   | No file  | `d6ba5a352381`  |
| 3002   | No file  | `d6ba5a352381`  |
| 2995   | No file  | `d6ba5a352381`  |
| 2987   | No file  | `d6ba5a352381`  |
| 2978   | No file  | `d6ba5a352381`  |
| 2970   | No file  | `d6ba5a352381`  |
| 2959   | No file  | `d6ba5a352381`  |
| 2951   | No file  | `d6ba5a352381`  |
| 2942   | No file  | `d6ba5a352381`  |
| 2935   | No file  | `d6ba5a352381`  |
| 2932   | No file  | `d6ba5a352381`  |
| 2923   | No file  | `d6ba5a352381`  |
| 2919   | No file  | `d6ba5a352381`  |
| 2907   | No file  | `d6ba5a352381`  |
| 2900   | No file  | `d6ba5a352381`  |
| 2891   | No file  | `d6ba5a352381`  |
| 2882   | No file  | `d6ba5a352381`  |
| 2872   | No file  | `d6ba5a352381`  |
| 2863   | No file  | `d6ba5a352381`  |
| 2855   | No file  | `d6ba5a352381`  |
| 2849   | No file  | `d6ba5a352381`  |
| 2844   | No file  | `d6ba5a352381`  |
| 2834   | No file  | `d6ba5a352381`  |
| 2825   | No file  | `d6ba5a352381`  |
| 2819   | No file  | `d6ba5a352381`  |
| 2811   | No file  | `d6ba5a352381`  |
| 2803   | No file  | `d6ba5a352381`  |
| 2794   | No file  | `d6ba5a352381`  |
| 2783   | No file  | `d6ba5a352381`  |
| 2774   | No file  | `d6ba5a352381`  |
| 2765   | No file  | `d6ba5a352381`  |
| 2756   | No file  | `d6ba5a352381`  |
| 2750   | No file  | `d6ba5a352381`  |
| 2743   | No file  | `d6ba5a352381`  |
| 2736   | No file  | `d6ba5a352381`  |
| 2726   | No file  | `d6ba5a352381`  |
| 2717   | No file  | `d6ba5a352381`  |
| 2709   | No file  | `d6ba5a352381`  |
| 2703   | No file  | `d6ba5a352381`  |
| 2695   | No file  | `d6ba5a352381`  |
| 2684   | No file  | `d6ba5a352381`  |
| 2672   | No file  | `d6ba5a352381`  |
| 2665   | No file  | `d6ba5a352381`  |
| 2657   | No file  | `d6ba5a352381`  |
| 2649   | No file  | `d6ba5a352381`  |
| 2644   | No file  | `d6ba5a352381`  |
| 2637   | No file  | `d6ba5a352381`  |
| 2629   | No file  | `d6ba5a352381`  |
| 2619   | No file  | `d6ba5a352381`  |
| 2612   | No file  | `d6ba5a352381`  |
| 2606   | No file  | `d6ba5a352381`  |
| 2602   | No file  | `d6ba5a352381`  |
| 2601   | No file  | `d6ba5a352381`  |
| 2592   | No file  | `d6ba5a352381`  |
| 2583   | No file  | `d6ba5a352381`  |
| 2575   | No file  | `d6ba5a352381`  |
| 2567   | No file  | `d6ba5a352381`  |
| 2560   | No file  | `d6ba5a352381`  |
| 2553   | No file  | `d6ba5a352381`  |
| 2545   | No file  | `d6ba5a352381`  |
| 2538   | No file  | `d6ba5a352381`  |
| 2529   | No file  | `d6ba5a352381`  |
| 2519   | No file  | `d6ba5a352381`  |
| 2513   | No file  | `d6ba5a352381`  |
| 2510   | No file  | `d6ba5a352381`  |
| 2507   | No file  | `d6ba5a352381`  |
| 2503   | No file  | `d6ba5a352381`  |
| 2498   | No file  | `d6ba5a352381`  |
| 2492   | No file  | `d6ba5a352381`  |
| 2487   | No file  | `d6ba5a352381`  |
| 2480   | No file  | `d6ba5a352381`  |
| 2474   | No file  | `d6ba5a352381`  |
| 2468   | No file  | `d6ba5a352381`  |
| 2460   | No file  | `d6ba5a352381`  |
| 2453   | No file  | `d6ba5a352381`  |
| 2444   | No file  | `d6ba5a352381`  |
| 2438   | No file  | `d6ba5a352381`  |
| 2434   | No file  | `d6ba5a352381`  |
| 2429   | No file  | `d6ba5a352381`  |
| 2421   | No file  | `d6ba5a352381`  |
| 2414   | No file  | `d6ba5a352381`  |
| 2407   | No file  | `d6ba5a352381`  |
| 2401   | No file  | `d6ba5a352381`  |
| 2397   | No file  | `d6ba5a352381`  |
| 2393   | No file  | `d6ba5a352381`  |
| 2384   | No file  | `d6ba5a352381`  |
| 2378   | No file  | `d6ba5a352381`  |
| 2372   | No file  | `d6ba5a352381`  |
| 2358   | No file  | `d6ba5a352381`  |
| 2352   | No file  | `d6ba5a352381`  |
| 2347   | No file  | `d6ba5a352381`  |
| 2343   | No file  | `d6ba5a352381`  |
| 2335   | No file  | `d6ba5a352381`  |
| 2327   | No file  | `d6ba5a352381`  |
| 2324   | No file  | `d6ba5a352381`  |
| 2319   | No file  | `d6ba5a352381`  |
| 2313   | No file  | `d6ba5a352381`  |
| 2308   | No file  | `d6ba5a352381`  |
| 2302   | No file  | `d6ba5a352381`  |
| 2295   | No file  | `d6ba5a352381`  |
| 2290   | No file  | `d6ba5a352381`  |
| 2284   | No file  | `d6ba5a352381`  |
| 2276   | No file  | `d6ba5a352381`  |
| 2269   | No file  | `d6ba5a352381`  |
| 2259   | No file  | `d6ba5a352381`  |
| 2250   | No file  | `d6ba5a352381`  |
| 2243   | No file  | `d6ba5a352381`  |
| 2235   | No file  | `d6ba5a352381`  |
| 2229   | No file  | `d6ba5a352381`  |
| 2224   | No file  | `d6ba5a352381`  |
| 2218   | No file  | `d6ba5a352381`  |
| 2215   | No file  | `d6ba5a352381`  |
| 2207   | No file  | `d6ba5a352381`  |
| 2203   | No file  | `d6ba5a352381`  |
| 2196   | No file  | `d6ba5a352381`  |
| 2192   | No file  | `d6ba5a352381`  |
| 2189   | No file  | `d6ba5a352381`  |
| 2183   | No file  | `d6ba5a352381`  |
| 2179   | No file  | `d6ba5a352381`  |
| 2171   | No file  | `d6ba5a352381`  |
| 2163   | No file  | `d6ba5a352381`  |
| 2156   | No file  | `d6ba5a352381`  |
| 2151   | No file  | `d6ba5a352381`  |
| 2147   | No file  | `d6ba5a352381`  |
| 2142   | No file  | `d6ba5a352381`  |
| 2138   | No file  | `d6ba5a352381`  |
| 2134   | No file  | `d6ba5a352381`  |
| 2130   | No file  | `d6ba5a352381`  |
| 2122   | No file  | `d6ba5a352381`  |
| 2107   | No file  | `d6ba5a352381`  |
| 2098   | No file  | `d6ba5a352381`  |
| 2089   | No file  | `d6ba5a352381`  |
| 2081   | No file  | `d6ba5a352381`  |
| 2073   | No file  | `d6ba5a352381`  |
| 2067   | No file  | `d6ba5a352381`  |
| 2063   | No file  | `d6ba5a352381`  |
| 2059   | No file  | `d6ba5a352381`  |
| 2052   | No file  | `d6ba5a352381`  |
| 2044   | No file  | `d6ba5a352381`  |
| 2039   | No file  | `d6ba5a352381`  |
| 2032   | No file  | `d6ba5a352381`  |
| 2025   | No file  | `d6ba5a352381`  |
| 2011   | No file  | `d6ba5a352381`  |
| 2005   | No file  | `d6ba5a352381`  |
| 2000   | No file  | `d6ba5a352381`  |
| 1996   | No file  | `d6ba5a352381`  |
| 1991   | No file  | `d6ba5a352381`  |
| 1985   | No file  | `d6ba5a352381`  |
| 1980   | No file  | `d6ba5a352381`  |
| 1969   | No file  | `d6ba5a352381`  |
| 1964   | No file  | `d6ba5a352381`  |
| 1958   | No file  | `d6ba5a352381`  |
| 1950   | No file  | `d6ba5a352381`  |
| 1945   | No file  | `d6ba5a352381`  |
| 1937   | No file  | `d6ba5a352381`  |
| 1933   | No file  | `d6ba5a352381`  |
| 1927   | No file  | `d6ba5a352381`  |
| 1921   | No file  | `d6ba5a352381`  |
| 1914   | No file  | `d6ba5a352381`  |
| 1908   | No file  | `d6ba5a352381`  |
| 1897   | No file  | `d6ba5a352381`  |
| 1892   | No file  | `d6ba5a352381`  |
| 1886   | No file  | `d6ba5a352381`  |
| 1881   | No file  | `d6ba5a352381`  |
| 1871   | No file  | `d6ba5a352381`  |
| 1866   | No file  | `d6ba5a352381`  |
| 1862   | No file  | `d6ba5a352381`  |
| 1854   | No file  | `d6ba5a352381`  |
| 1846   | No file  | `d6ba5a352381`  |
| 1838   | No file  | `d6ba5a352381`  |
| 1832   | No file  | `d6ba5a352381`  |
| 1826   | No file  | `d6ba5a352381`  |
| 1822   | No file  | `d6ba5a352381`  |
| 1818   | No file  | `d6ba5a352381`  |
| 1804   | No file  | `d6ba5a352381`  |
| 1794   | No file  | `d6ba5a352381`  |
| 1790   | No file  | `d6ba5a352381`  |
| 1784   | No file  | `d6ba5a352381`  |
| 1774   | No file  | `d6ba5a352381`  |
| 1771   | No file  | `d6ba5a352381`  |
| 1762   | No file  | `d6ba5a352381`  |
| 1759   | No file  | `d6ba5a352381`  |
| 1754   | No file  | `d6ba5a352381`  |
| 1749   | No file  | `d6ba5a352381`  |
| 1743   | No file  | `d6ba5a352381`  |
| 1737   | No file  | `d6ba5a352381`  |
| 1731   | No file  | `d6ba5a352381`  |
| 1725   | No file  | `d6ba5a352381`  |
| 1717   | No file  | `d6ba5a352381`  |
| 1710   | No file  | `d6ba5a352381`  |
| 1704   | No file  | `d6ba5a352381`  |
| 1698   | No file  | `d6ba5a352381`  |
| 1690   | No file  | `d6ba5a352381`  |
| 1685   | No file  | `d6ba5a352381`  |
| 1680   | No file  | `d6ba5a352381`  |
| 1674   | No file  | `d6ba5a352381`  |
| 1668   | No file  | `d6ba5a352381`  |
| 1659   | No file  | `d6ba5a352381`  |
| 1649   | No file  | `d6ba5a352381`  |
| 1642   | No file  | `d6ba5a352381`  |
| 1636   | No file  | `d6ba5a352381`  |
| 1628   | No file  | `d6ba5a352381`  |
| 1622   | No file  | `d6ba5a352381`  |
| 1614   | No file  | `d6ba5a352381`  |
| 1608   | No file  | `d6ba5a352381`  |
| 1602   | No file  | `d6ba5a352381`  |
| 1598   | No file  | `d6ba5a352381`  |
| 1594   | No file  | `d6ba5a352381`  |
| 1590   | No file  | `d6ba5a352381`  |
| 1587   | No file  | `d6ba5a352381`  |
| 1584   | No file  | `d6ba5a352381`  |
| 1579   | No file  | `d6ba5a352381`  |
| 1572   | No file  | `d6ba5a352381`  |
| 1565   | No file  | `d6ba5a352381`  |
| 1559   | No file  | `d6ba5a352381`  |
| 1554   | No file  | `d6ba5a352381`  |
| 1547   | No file  | `d6ba5a352381`  |
| 1537   | No file  | `d6ba5a352381`  |
| 1529   | No file  | `d6ba5a352381`  |
| 1524   | No file  | `d6ba5a352381`  |
| 1519   | No file  | `d6ba5a352381`  |
| 1509   | No file  | `d6ba5a352381`  |
| 1506   | No file  | `d6ba5a352381`  |
| 1504   | No file  | `d6ba5a352381`  |
| 1500   | No file  | `d6ba5a352381`  |
| 1493   | No file  | `d6ba5a352381`  |
| 1489   | No file  | `d6ba5a352381`  |
| 1485   | No file  | `d6ba5a352381`  |
| 1481   | No file  | `d6ba5a352381`  |
| 1474   | No file  | `d6ba5a352381`  |
| 1466   | No file  | `d6ba5a352381`  |
| 1462   | No file  | `d6ba5a352381`  |
| 1459   | No file  | `d6ba5a352381`  |
| 1453   | No file  | `d6ba5a352381`  |
| 1450   | No file  | `d6ba5a352381`  |
| 1445   | No file  | `d6ba5a352381`  |
| 1439   | No file  | `d6ba5a352381`  |
| 1433   | No file  | `d6ba5a352381`  |
| 1430   | No file  | `d6ba5a352381`  |
| 1426   | No file  | `d6ba5a352381`  |
| 1421   | No file  | `d6ba5a352381`  |
| 1417   | No file  | `d6ba5a352381`  |
| 1416   | No file  | `d6ba5a352381`  |
| 1409   | No file  | `d6ba5a352381`  |
| 1405   | No file  | `d6ba5a352381`  |
| 1401   | No file  | `d6ba5a352381`  |
| 1396   | No file  | `d6ba5a352381`  |
| 1391   | No file  | `d6ba5a352381`  |
| 1390   | No file  | `d6ba5a352381`  |
| 1386   | No file  | `d6ba5a352381`  |
| 1381   | No file  | `d6ba5a352381`  |
| 1379   | No file  | `d6ba5a352381`  |
| 1372   | No file  | `d6ba5a352381`  |
| 1366   | No file  | `d6ba5a352381`  |
| 1364   | No file  | `d6ba5a352381`  |
| 1363   | No file  | `d6ba5a352381`  |
| 1360   | No file  | `d6ba5a352381`  |
| 1358   | No file  | `d6ba5a352381`  |
| 1355   | No file  | `d6ba5a352381`  |
| 1351   | No file  | `d6ba5a352381`  |
| 1348   | No file  | `d6ba5a352381`  |
| 1346   | No file  | `d6ba5a352381`  |
| 1341   | No file  | `d6ba5a352381`  |
| 1340   | No file  | `d6ba5a352381`  |
| 1338   | No file  | `d6ba5a352381`  |
| 1335   | No file  | `d6ba5a352381`  |
| 1333   | No file  | `d6ba5a352381`  |
| 1329   | No file  | `d6ba5a352381`  |
| 1327   | No file  | `d6ba5a352381`  |
| 1324   | No file  | `d6ba5a352381`  |
| 1321   | No file  | `d6ba5a352381`  |
| 1319   | No file  | `d6ba5a352381`  |
| 1318   | No file  | `d6ba5a352381`  |
| 1316   | No file  | `d6ba5a352381`  |
| 1313   | No file  | `d6ba5a352381`  |
| 1311   | No file  | `d6ba5a352381`  |
| 1309   | No file  | `d6ba5a352381`  |
| 1304   | No file  | `d6ba5a352381`  |
| 1292   | No file  | `d6ba5a352381`  |
| 1286   | No file  | `d6ba5a352381`  |
| 1280   | No file  | `d6ba5a352381`  |
| 1276   | No file  | `d6ba5a352381`  |
| 1267   | No file  | `d6ba5a352381`  |
| 1261   | No file  | `d6ba5a352381`  |
| 1256   | No file  | `d6ba5a352381`  |
| 1250   | No file  | `d6ba5a352381`  |
| 1246   | No file  | `3f441f74159c`  |
| 1239   | No file  | `3f441f74159c`  |
| 1230   | No file  | `3f441f74159c`  |
| 1226   | No file  | `3f441f74159c`  |
| 1220   | No file  | `3f441f74159c`  |
| 1217   | No file  | `3f441f74159c`  |
| 1211   | No file  | `3f441f74159c`  |
| 1210   | No file  | `3f441f74159c`  |
| 1208   | No file  | `3f441f74159c`  |
| 1203   | No file  | `3f441f74159c`  |
| 1197   | No file  | `3f441f74159c`  |
| 1194   | No file  | `3f441f74159c`  |
| 1192   | No file  | `3f441f74159c`  |
| 1187   | No file  | `3f441f74159c`  |
| 1183   | No file  | `3f441f74159c`  |
| 1177   | No file  | `3f441f74159c`  |
| 1173   | No file  | `3f441f74159c`  |
| 1167   | No file  | `3f441f74159c`  |
| 1164   | No file  | `3f441f74159c`  |
| 1156   | No file  | `3f441f74159c`  |
| 1149   | No file  | `3f441f74159c`  |
| 1144   | No file  | `3f441f74159c`  |
| 1137   | No file  | `3f441f74159c`  |
| 1132   | No file  | `3f441f74159c`  |
| 1127   | No file  | `3f441f74159c`  |
| 1122   | No file  | `3f441f74159c`  |
| 1118   | No file  | `3f441f74159c`  |
| 1114   | No file  | `3f441f74159c`  |
| 1109   | No file  | `3f441f74159c`  |
| 1102   | No file  | `3f441f74159c`  |
| 1096   | No file  | `3f441f74159c`  |
| 1088   | No file  | `3f441f74159c`  |
| 1081   | No file  | `3f441f74159c`  |
| 1076   | No file  | `3f441f74159c`  |
| 1069   | No file  | `3f441f74159c`  |
| 1064   | No file  | `3f441f74159c`  |
| 1058   | No file  | `3f441f74159c`  |
| 1051   | No file  | `3f441f74159c`  |
| 1044   | No file  | `3f441f74159c`  |
| 1036   | No file  | `3f441f74159c`  |
| 1026   | No file  | `3f441f74159c`  |
| 1016   | No file  | `3f441f74159c`  |
| 1009   | No file  | `3f441f74159c`  |
| 1005   | No file  | `3f441f74159c`  |
| 1000   | No file  | `3f441f74159c`  |
| 998    | No file  | `3f441f74159c`  |
| 990    | No file  | `3f441f74159c`  |
| 979    | No file  | `3f441f74159c`  |
| 972    | No file  | `3f441f74159c`  |
| 963    | No file  | `3f441f74159c`  |
| 955    | No file  | `3f441f74159c`  |
| 946    | No file  | `3f441f74159c`  |
| 938    | No file  | `3f441f74159c`  |
| 927    | No file  | `3f441f74159c`  |
| 911    | No file  | `3f441f74159c`  |
| 904    | No file  | `3f441f74159c`  |
| 899    | No file  | `3f441f74159c`  |
| 894    | No file  | `3f441f74159c`  |
| 885    | No file  | `3f441f74159c`  |
| 879    | No file  | `3f441f74159c`  |
| 872    | No file  | `3f441f74159c`  |
| 864    | No file  | `3f441f74159c`  |
| 855    | No file  | `3f441f74159c`  |
| 853    | No file  | `3f441f74159c`  |
| 845    | No file  | `3f441f74159c`  |
| 837    | No file  | `3f441f74159c`  |
| 829    | No file  | `3f441f74159c`  |
| 822    | No file  | `3f441f74159c`  |
| 814    | No file  | `3f441f74159c`  |
| 805    | No file  | `3f441f74159c`  |
| 794    | No file  | `3f441f74159c`  |
| 787    | No file  | `3f441f74159c`  |
| 780    | No file  | `3f441f74159c`  |
| 771    | No file  | `3f441f74159c`  |
| 760    | No file  | `3f441f74159c`  |
| 748    | No file  | `3f441f74159c`  |
| 741    | No file  | `3f441f74159c`  |
| 736    | No file  | `3f441f74159c`  |
| 731    | No file  | `3f441f74159c`  |
| 723    | No file  | `3f441f74159c`  |
| 711    | No file  | `3f441f74159c`  |
| 707    | No file  | `3f441f74159c`  |
| 697    | No file  | `3f441f74159c`  |
| 689    | No file  | `3f441f74159c`  |
| 683    | No file  | `3f441f74159c`  |
| 678    | No file  | `3f441f74159c`  |
| 670    | No file  | `3f441f74159c`  |
| 661    | No file  | `3f441f74159c`  |
| 656    | No file  | `3f441f74159c`  |
| 652    | No file  | `3f441f74159c`  |
| 643    | No file  | `3f441f74159c`  |
| 637    | No file  | `3f441f74159c`  |
| 630    | No file  | `3f441f74159c`  |
| 627    | No file  | `3f441f74159c`  |
| 621    | No file  | `3f441f74159c`  |
| 617    | No file  | `3f441f74159c`  |
| 615    | No file  | `3f441f74159c`  |
| 606    | No file  | `3f441f74159c`  |
| 599    | No file  | `3f441f74159c`  |
| 592    | No file  | `3f441f74159c`  |
| 586    | No file  | `3f441f74159c`  |
| 577    | No file  | `3f441f74159c`  |
| 569    | No file  | `3f441f74159c`  |
| 561    | No file  | `3f441f74159c`  |
| 554    | No file  | `3f441f74159c`  |
| 542    | No file  | `3f441f74159c`  |
| 532    | No file  | `3f441f74159c`  |
| 531    | No file  | `3f441f74159c`  |
| 526    | No file  | `3f441f74159c`  |
| 521    | No file  | `3f441f74159c`  |
| 517    | No file  | `3f441f74159c`  |
| 510    | No file  | `3f441f74159c`  |
| 508    | No file  | `3f441f74159c`  |
| 504    | No file  | `3f441f74159c`  |
| 497    | No file  | `3f441f74159c`  |
| 491    | No file  | `3f441f74159c`  |
| 485    | No file  | `3f441f74159c`  |
| 478    | No file  | `3f441f74159c`  |
| 472    | No file  | `3f441f74159c`  |
| 466    | No file  | `3f441f74159c`  |
| 457    | No file  | `3f441f74159c`  |
| 452    | No file  | `3f441f74159c`  |
| 449    | No file  | `3f441f74159c`  |
| 435    | No file  | `3f441f74159c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `boss_spawnlevel.bss` | Optional | The boss character of a [`boss_spawn.bss`](boss_spawn_bss.md) key, for the boss summon reasons |
| `languagedata_en.loc` | Optional | Change reason text (type 141), benefit text (type 140), skill names (type 10), the daily pay text (type 37), boss names (type 6) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type                                   | Field                 | Notes                                          |
| ------------------- | -------------------------------------- | --------------------- | ---------------------------------------------- |
| `+0x00`             | u64                                    | unknown_00            | A different address on every client; see Notes |
| `+0x08`             | i64                                    | min_guild_fame        | `-2,000,000`, the lowest Guild Fame            |
| `+0x10`             | i64                                    | max_guild_fame        | `1,000,000`, the highest Guild Fame            |
| `+0x18`             | u64                                    | war_duration          | `21,600` seconds, 6 hours                      |
| `+0x20`             | u64                                    | response_war_duration | `604,800` seconds, 7 days                      |
| `+0x28`             | u64                                    | war_cooldown          | `172,800` seconds, 48 hours                    |
| `+0x30`             | u64                                    | war_guild_age         | `604,800` seconds, 7 days                      |
| `+0x38`             | u64                                    | war_online_members    | `10`                                           |
| `+0x40`             | u32                                    | change_reason_count   | Number of change reasons                       |
| `+0x44`             | Change Reason[change_reason_count]     | change_reasons        | See Change Reason                              |
| `change_reasons+0x00` | u32                                  | benefit_count         | Number of benefits                             |
| `change_reasons+0x04` | Benefit[benefit_count]               | benefits              | See Benefit                                    |
| `benefits+0x00`     | u32                                    | daily_incentive_count | Number of daily pay steps                      |
| `benefits+0x04`     | Daily Incentive[daily_incentive_count] | daily_incentives      | See Daily Incentive; they end at the last byte |

The head values are the ones of clients 3402 to 3482.

### Change Reason (variable: 36 bytes + description text)

One way to gain or spend Guild Fame. The How to Obtain and Uses tabs of the Guild Fame Benefits window list these rows by `ToClient_GetGuildHonorGainValueByIndex` / `ToClient_GetGuildHonorConsumeValueByIndex` and their `...DescByIndex` text.

| Offset                | Type  | Field          | Notes                                                                   |
| --------------------- | ----- | -------------- | ----------------------------------------------------------------------- |
| `+0x00`               | u32   | key            | `0` up, in file order; LOC type 141 `str_id1` of the English text       |
| `+0x04`               | str16 | description_kr | Korean text, `길드원 접속` (`Guild Member Login`) for key `0`            |
| `description_kr+0x00` | i64   | point          | Guild Fame gained (positive) or spent (negative): `50` for a member login, `-400,000` for a war declaration |
| `description_kr+0x08` | u64   | reason_param   | The second argument of `ToClient_GetGuildHonorChangePointByReason(reason_type, reason_param)`: a `boss_spawn.bss` key or a skill key; `0` for the other reasons |
| `description_kr+0x10` | u32   | key_dup        | Same as `key` on every row (client 3482)                                |
| `description_kr+0x14` | u32   | reason_type    | The change reason, see Change Reason Types                              |

### Benefit (variable: 41 bytes + description text)

A benefit a guild gets while its Guild Fame is at or above `point`, read by `ToClient_GetGuildHonorBenefitConditionByIndex`, `ToClient_GetGuildHonorBenefitTypeByIndex` and `ToClient_GetGuildHonorBenefitDescriptionByIndex`.

| Offset                | Type  | Field          | Notes                                                                   |
| --------------------- | ----- | -------------- | ----------------------------------------------------------------------- |
| `+0x00`               | u32   | key            | `0` up, in file order; LOC type 140 `str_id1` of the English text       |
| `+0x04`               | str16 | description_kr | Korean text, `일일 임무 충전 <b>+10</b>` (`Daily Missions <b>+10</b>`) for key `0` |
| `description_kr+0x00` | i64   | point          | The Guild Fame the benefit needs, `50,000` to `900,000` (client 3482)   |
| `description_kr+0x08` | u64   | param_1        | By `benefit_type`, see Benefit Types                                    |
| `description_kr+0x10` | u64   | param_2        | By `benefit_type`, see Benefit Types                                    |
| `description_kr+0x18` | u32   | key_dup        | Same as `key` on every row (client 3482)                                |
| `description_kr+0x1C` | u8    | benefit_type   | See Benefit Types                                                       |

### Daily Incentive (12 bytes)

A Bonus Guild Daily Pay step, read by `ToClient_GetGuildHonorDailyIncentiveBenefitConditionByIndex` and `ToClient_GetGuildHonorDailyIncentiveBenefitPercentByIndex`.

| Offset  | Type | Field         | Notes                                                                    |
| ------- | ---- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | i64  | point         | The Guild Fame the step needs, `50,000` to `900,000` (client 3482)       |
| `+0x08` | u32  | bonus_percent | The bonus on the `CppDefine.e1Percent` scale (`10000` is 1%): `9,000,000` shows as `+900%` |

## Layout 3

The gains, the costs and the guild skill costs are three lists without text. Benefit and Daily Incentive are the ones of Layout 4.

### File Layout

| Offset                | Type                                   | Field                 | Notes                                          |
| --------------------- | -------------------------------------- | --------------------- | ---------------------------------------------- |
| `+0x00`               | u64                                    | unknown_00            | An address, as in Layout 4                     |
| `+0x08`               | i64                                    | min_guild_fame        | `-3,000,000` (client 3387)                     |
| `+0x10`               | i64                                    | max_guild_fame        | `1,000,000`                                    |
| `+0x18`               | u64                                    | war_duration          | `21,600` seconds, 6 hours                      |
| `+0x20`               | u64                                    | response_war_duration | `604,800` seconds, 7 days                      |
| `+0x28`               | u64                                    | war_cooldown          | `172,800` seconds, 48 hours                    |
| `+0x30`               | u64                                    | war_guild_age         | `604,800` seconds, 7 days                      |
| `+0x38`               | u64                                    | war_online_members    | `10`                                           |
| `+0x40`               | u32                                    | gain_count            | Number of reasons that earn Guild Fame         |
| `+0x44`               | Change Reason[gain_count]              | gains                 | See Change Reason                              |
| `gains+0x00`          | u32                                    | consume_count         | Number of reasons that cost Guild Fame         |
| `gains+0x04`          | Change Reason[consume_count]           | consumes              | See Change Reason                              |
| `consumes+0x00`       | u32                                    | consume_skill_count   | Number of guild skills that cost Guild Fame    |
| `consumes+0x04`       | Consume Skill[consume_skill_count]     | consume_skills        | See Consume Skill                              |
| `consume_skills+0x00` | u32                                    | benefit_count         | Number of benefits                             |
| `consume_skills+0x04` | Benefit[benefit_count]                 | benefits              | See Benefit in Layout 4                        |
| `benefits+0x00`       | u32                                    | daily_incentive_count | Number of daily pay steps                      |
| `benefits+0x04`       | Daily Incentive[daily_incentive_count] | daily_incentives      | See Daily Incentive in Layout 4; they end at the last byte |

### Change Reason (16 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | key         | Same as `reason_type` on every row (client 3387)                            |
| `+0x04` | i64  | point       | Guild Fame gained or spent, as in Layout 4                                  |
| `+0x0C` | u32  | reason_type | `0` to `11` in `gains`, `1000` to `1007` in `consumes` (client 3387); see Change Reason Types |

### Consume Skill (16 bytes)

A guild skill whose use costs Guild Fame. Layout 4 stores it as a change reason with `reason_type` `1007` and the skill key in `reason_param`.

| Offset  | Type | Field         | Notes                                                                    |
| ------- | ---- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | skill_key     | `skill_no << 16 \| level`: skill 62874 Glorious Command to Gather, level 1, the only row (client 3387) |
| `+0x04` | u32  | skill_key_dup | Same as `skill_key`                                                      |
| `+0x08` | i64  | point         | `-30,000`, the Guild Fame the skill costs                                |

## Layout 2

The lists are those of Layout 3, but every row starts with an address, the change reason rows have no `key`, and the benefit rows have no `key`, text or `key_dup`. Each row starts at an 8-byte boundary, and a field of 8 bytes sits at one, so a row that ends in a u32 or a u8 is padded to the next row. The padding bytes are not zeroed: `padding_14` of the gain rows holds `65 00 6C 00`, `30 00 5F 00` and `6F 00 72 00` on client 3373, pieces of UTF-16 text. The address is the same in every row of one list and differs between the lists and the head, `0x60` apart (`0x00007FF66D71BB38` in the head, `...BB98` in the gain rows, `...BBF8` in the cost rows on client 3373). The head has six values.

### File Layout

| Offset                | Type                                   | Field                 | Notes                                          |
| --------------------- | -------------------------------------- | --------------------- | ---------------------------------------------- |
| `+0x00`               | u64                                    | unknown_00            | An address, as in Layout 4                     |
| `+0x08`               | i64                                    | min_guild_fame        | `-1,000,000` on client 3373, `-3,000,000` on 3381 |
| `+0x10`               | i64                                    | max_guild_fame        | `300,000` on client 3373, `1,000,000` on 3381  |
| `+0x18`               | u64                                    | war_duration          | `21,600` seconds, 6 hours                      |
| `+0x20`               | u64                                    | response_war_duration | `604,800` seconds, 7 days                      |
| `+0x28`               | u64                                    | war_cooldown          | `172,800` seconds, 48 hours                    |
| `+0x30`               | u32                                    | gain_count            | Number of reasons that earn Guild Fame         |
| `+0x34`               | Change Reason[gain_count]              | gains                 | See Change Reason                              |
| `gains+0x00`          | u32                                    | consume_count         | Number of reasons that cost Guild Fame         |
| `gains+0x04`          | Change Reason[consume_count]           | consumes              | See Change Reason                              |
| `consumes+0x00`       | u32                                    | consume_skill_count   | Number of guild skills that cost Guild Fame    |
| `consumes+0x04`       | Consume Skill[consume_skill_count]     | consume_skills        | See Consume Skill                              |
| `consume_skills+0x00` | u32                                    | benefit_count         | Number of benefits                             |
| `consume_skills+0x04` | Benefit[benefit_count]                 | benefits              | See Benefit                                    |
| `benefits+0x00`       | u32                                    | daily_incentive_count | Number of daily pay steps                      |
| `benefits+0x04`       | Daily Incentive[daily_incentive_count] | daily_incentives      | See Daily Incentive; they end at the last byte |

### Change Reason (24 bytes)

| Offset  | Type     | Field       | Notes                                                                 |
| ------- | -------- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u64      | unknown_00  | An address, the same in every row of the list                         |
| `+0x08` | i64      | point       | Guild Fame gained or spent, as in Layout 4                            |
| `+0x10` | u32      | reason_type | `0` to `11` in `gains`, `1000` to `1007` in `consumes` (client 3381); see Change Reason Types |
| `+0x14` | bytes[4] | padding_14  | Alignment of the next row to 8 bytes; not zeroed                      |

### Consume Skill (24 bytes)

| Offset  | Type     | Field      | Notes                                                                  |
| ------- | -------- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u64      | unknown_00 | An address, the same in every row of the list                          |
| `+0x08` | u32      | skill_key  | Skill 62874 Glorious Command to Gather, level 1, the only row (client 3381) |
| `+0x0C` | bytes[4] | padding_0c | Alignment of `point` to 8 bytes; not zeroed                            |
| `+0x10` | i64      | point      | `-30,000`                                                              |

### Benefit (40 bytes)

| Offset  | Type     | Field        | Notes                                                                |
| ------- | -------- | ------------ | -------------------------------------------------------------------- |
| `+0x00` | u64      | unknown_00   | An address, the same in every row of the list                        |
| `+0x08` | i64      | point        | The Guild Fame the benefit needs, `30,000` to `220,000` (client 3381) |
| `+0x10` | u64      | param_1      | By `benefit_type`, see Benefit Types                                 |
| `+0x18` | u64      | param_2      | By `benefit_type`, see Benefit Types                                 |
| `+0x20` | u8       | benefit_type | `1` to `3` (client 3381); see Benefit Types                          |
| `+0x21` | bytes[7] | padding_21   | Alignment of the next row to 8 bytes                                 |

### Daily Incentive (24 bytes)

| Offset  | Type     | Field         | Notes                                                               |
| ------- | -------- | ------------- | ------------------------------------------------------------------- |
| `+0x00` | u64      | unknown_00    | An address, the same in every row of the list                       |
| `+0x08` | i64      | point         | The Guild Fame the step needs, `50,000` to `300,000` (client 3381)  |
| `+0x10` | u32      | bonus_percent | `500,000` to `10,000,000`, on the scale of Layout 4                 |
| `+0x14` | bytes[4] | padding_14    | Alignment of the next row to 8 bytes; not zeroed                    |

## Layout 1

The head and Change Reason are those of Layout 2. After the gains and the costs comes one list of rows with two Guild Fame sized values and two small numbers, and no list of guild skill costs, benefits or daily pay steps.

### File Layout

| Offset              | Type                                   | Field                 | Notes                                          |
| ------------------- | -------------------------------------- | --------------------- | ---------------------------------------------- |
| `+0x00`             | u64                                    | unknown_00            | An address, as in Layout 4                     |
| `+0x08`             | i64                                    | min_guild_fame        | `-1,000,000` (clients 3356 and 3364)           |
| `+0x10`             | i64                                    | max_guild_fame        | `300,000`                                      |
| `+0x18`             | u64                                    | war_duration          | `21,600` seconds, 6 hours                      |
| `+0x20`             | u64                                    | response_war_duration | `604,800` on client 3364, `172,800` on 3356    |
| `+0x28`             | u64                                    | war_cooldown          | `172,800` on client 3364, `604,800` on 3356    |
| `+0x30`             | u32                                    | gain_count            | Number of reasons that earn Guild Fame         |
| `+0x34`             | Change Reason[gain_count]              | gains                 | See Change Reason in Layout 2                  |
| `gains+0x00`        | u32                                    | consume_count         | Number of reasons that cost Guild Fame         |
| `gains+0x04`        | Change Reason[consume_count]           | consumes              | See Change Reason in Layout 2                  |
| `consumes+0x00`     | u32                                    | unknown_list_count    | Number of Unknown Row entries                  |
| `consumes+0x04`     | Unknown Row[unknown_list_count]        | unknown_list          | See Unknown Row; they end at the last byte     |

### Unknown Row (32 bytes)

Six rows on clients 3356 and 3364, the same values on both.

| Offset  | Type     | Field      | Notes                                                                  |
| ------- | -------- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u64      | unknown_00 | An address, the same in every row of the list                          |
| `+0x08` | i64      | unknown_08 | `800,000`, `600,000`, `500,000`, `100,000`, `50,000`, `30,000` in file order |
| `+0x10` | u32      | unknown_10 | `1,000,000`, `750,000`, `750,000`, `500,000`, `250,000`, `100,000`; above `unknown_08` on every row |
| `+0x14` | u32      | unknown_14 | `1` on the two rows whose `unknown_18` is `3`, else `0`                |
| `+0x18` | u8       | unknown_18 | `0`, `3`, `1`, `2`, `3`, `4` in file order                             |
| `+0x19` | bytes[7] | padding_19 | Alignment of the next row to 8 bytes; UTF-16 text pieces from `+0x1A` on client 3356, zero on 3364 |

## Change Reason Types

`reason_type` on client 3482. The rows that earn Guild Fame have `reason_type` equal to their `key`, `0` to `11`; the rows that spend it have `1000` up. LOC type 141 also holds English text with `str_id1 = reason_type` (`str_id2` `8` for `1005`, `1` for `1007`, else `0`), which may be the text of a Guild Fame history line. The Lua names come from the calls of `ToClient_GetGuildHonorChangePointByReason` in `panel_guilddeclarewar_all`, `panel_guild_bosssummon_all_1` and `panel_window_guildmainserverset_1`, matched by their `reason_param` and the LOC text.

| reason_type | Rows (client 3482)                                      | `reason_param`      | Lua name                                                          |
| ----------- | ------------------------------------------------------- | ------------------- | ----------------------------------------------------------------- |
| 0 to 11     | Member login, guild mission, guild boss, Guild League, Blue Battlefield, Node War and Conquest War tiers, War of the Roses | `0` | none found                                                        |
| 1000 to 1003 | Guild maintenance cost by guild size, `-2,500` to `-10,000` | `0`             | none found                                                        |
| 1004        | War Declaration                                         | `0`                 | `__eGuildHonorPointChangeReasonType_Consume_DeclareWar`           |
| 1005        | Gumiho & Duoksini Summon                                | `8`, a `boss_spawn.bss` key | `__eGuildHonorPointChangeReasonType_Consume_CompleteGuildBossSpawnCondition` |
| 1006        | Additional Ferrid, Moghulis, Giant Mudster, Org and Khan Summon | `1` to `5`, `boss_spawn.bss` keys | `__eGuildHonorPointChangeReasonType_Consume_AddGuildBossSpawnCountMax` |
| 1007        | Use Guild Skill: Glorious Command to Gather, Glorious Golden Bell | skill keys of skills 62874 and 62875, level 1 | none found; `ToClient_GetUseGuildHonorPointConsumeSkillNeedPoint(skillNo)` reads the cost |
| 1009        | Reset Guild Base Server Cooldown                        | `0`                 | `__eGuildHonorPointChangeReasonType_Consume_ResetGuildMainServerCooltime` |

No row has `reason_type` `1008`, and LOC type 141 has no text for it.

## Benefit Types

`benefit_type` on client 3482. A skill key is `skill_no << 16 | level`, as in [`guildskill.bss`](guildskill_bss.md); every key here has level `1`.

| benefit_type | Lua name                                       | Rows (client 3482)                        | `param_1`                 | `param_2`                     |
| ------------ | ---------------------------------------------- | ----------------------------------------- | ------------------------- | ----------------------------- |
| 0            | none found                                     | 3: `[Mission] Glorious Subjugation`, `Life` and `Trading` `Unlocked` | First [`guildquest.dbss`](../dbss/guildquest_dbss.md) `quest_no` of the unlocked missions | Last `quest_no`: `5001` to `5016`, `5501` to `5540`, `6001` to `6008` |
| 1            | `__eGuildHonorBenefitType_MissionChargeIncrease` | 10: `Daily Missions +1` to `+10`        | `1`, the daily mission charges the step adds | `0`                |
| 2            | `__eGuildHonorBenefitType_UnlockGuildSkill`    | 6: `[Skill] ... Unlocked`                 | Skill key of the unlocked skill | `0`                     |
| 3            | `__eGuildHonorBenefitType_UpgradeGuildSkill`   | 3: `[Skill] ... Enhanced`                 | Skill key of the base skill | Skill key of the enhanced skill: `62858` Blessing of Fortuna becomes `62864` Generous Blessing of Fortuna |

The `MissionChargeIncrease` steps add up: Garmoth's New Guild Fame guide lists `+1` at each of the ten steps from `50,000` to `900,000` Guild Fame, for a total of 11 to 20 daily mission charges, so the `+1` to `+10` of the row texts is the sum of the `param_1` of every step reached. The Lua shows only the highest `MissionChargeIncrease` benefit the guild has reached as applied, and lists the type 2 and 3 benefits in a list of their own. The guild mission list (`panel_guildquestlist_all_1`) hides a mission whose `isGuildHonorBenefitQuest()` is true until `isUnlockedGuildHonorBenefitQuest(currentGuildHonorPoint)` is. On client 3482, 56 of the 64 `quest_no` in the three type 0 ranges have a `guildquest.dbss` row (`5501` to `5508` have none), and those 56 are every mission with `Glorious` in its title.

## Field Names

The names come from the client Lua (client 3482) and the data. `point` is the `_point` the Lua builds each of the three lists with. `reason_type` and `reason_param` are the two arguments of `ToClient_GetGuildHonorChangePointByReason`, which the boss summon window calls with a boss key and the war declaration window with `0`, the values these rows store. `benefit_type` takes the values the Lua compares with the `__eGuildHonorBenefitType_*` names, and each type's rows have the LOC text of that type. `bonus_percent` is the value the Lua divides by `CppDefine.e1Percent` for the `{percent}` of `LUA_GUILDHONOR_DAILYINCENTIVE_BENEFIT_GUIDE` (`Bonus Guild Daily Pay +{percent}%`). `param_1` and `param_2` hold a mission range or skill keys by type, so they keep a neutral name. The list names of Layouts 1 to 3 follow the Lua getters of the two tabs and of the skill cost: `ToClient_GetGuildHonorGainTypeCount` for `gains`, `ToClient_GetGuildHonorConsumeTypeCount` for `consumes` and `ToClient_IsGuildHonorPointConsumeSkill` / `ToClient_GetUseGuildHonorPointConsumeSkillNeedPoint(skillNo)` for `consume_skills`, whose `skill_key` holds that skill. The seven head values after `unknown_00` have no Lua getter, and the client exe has no `guildhonorsystem` string to find the loader by, so their names come from the values. `min_guild_fame` and `max_guild_fame`: I read the floor of `-2,000,000` and the cap of `1,000,000` in my own game on client 3483, the values these fields store. `war_duration`, `response_war_duration` and `war_cooldown` hold `21,600`, `604,800` and `172,800` seconds, the 6 hours, 7 days and 48 hours of the client's War Declaration tooltip in that order (a declared war lasts 6 hours, declaring war in response extends it to 7 days, a guild cannot declare war on the same guild for 48 hours after a war ends). `war_guild_age` (`604,800` seconds) and `war_online_members` (`10`) match two client LOC messages that name no number, `You cannot declare war for a certain period after creating a guild.` and `Not enough guild members are online to declare war.`; Garmoth's New Guild Fame guide gives the numbers: at least 7 days after creating a guild and at least 10 guild members online.

The file is not in the archive of client 1784, and neither a private server's `DataSheets.bexcel` on client 1784 nor the 2016 PDB has a sheet, column or type with `Honor` in its name.

## Notes

- Decompressed size on client 3482: `3,472` bytes, `0x40` head, 26 change reasons, 22 benefits and 10 daily pay steps.
- `unknown_00` is not a game value: `0x00007FF659C7ADE8` on client 3482, `0x00007FF79B062F88` on client 3474, an address in the range a 64-bit Windows program image loads at. The files of clients 3412 to 3482 differ in these 8 bytes only. [`questrandomgroup.bss`](questrandomgroup_bss.md) stores the same kind of address at row `+0x00`.
- Client 3402 has the same layout with 21 change reasons: one `Additional Guild Boss Summon` row (key `17`, `reason_type` `1006`, `reason_param` `0`) where client 3412 has the Gumiho & Duoksini row and the five boss rows, so the three rows after it have keys `18` to `20` in place of `23` to `25`.
- Clients 3356 and 3364 (Layout 1) hold 12 gains and 9 or 8 costs: `reason_type` `1000` to `1008` on client 3356, where `1007` costs `-50,000` and `1008` `-30,000`, and `1000` to `1007` on 3364. Clients 3373 to 3387 (Layouts 2 and 3) hold 12 gains, 8 costs, one guild skill cost, 13 benefits and 6 daily pay steps; the benefit keys of client 3387 run `4` to `16`. The benefits of client 3373 differ from those of 3381 and 3387 in the first `point` (`250,000` against `220,000`) and in `param_2` of the three type 3 rows.
- The gains keep their points from client 3356 to 3387 (`15` for a member login to `45,000` for `reason_type` `11`); client 3402 has other points (`50` to `150,000`).
- No client the doc check read before 3356 has the file in its `.meta`, and neither has client 3396, between 3387 and 3402.
- The head values by client: `min_guild_fame` is `-1,000,000` on clients 3356 to 3373, `-3,000,000` on 3381 and 3387 and `-2,000,000` from 3402; `max_guild_fame` is `300,000` on clients 3356 to 3373 and `1,000,000` from 3381, the amount skill 62872's LOC text names (`Applies upon reaching 1,000,000 Guild Fame`). Client 3356 stores `172,800` in `response_war_duration` and `604,800` in `war_cooldown`, the reverse of every later client. `war_guild_age` and `war_online_members` first appear on client 3387.

## Open Questions

### The Unknown Row of Layout 1

The six rows after the costs on clients 3356 and 3364 hold two Guild Fame sized values (`800,000` / `1,000,000` down to `30,000` / `100,000`), a `0` / `1` field and a type of `0` to `4`. They may be an early form of the benefits, which these clients lack; no Lua on client 3356 reads them.
