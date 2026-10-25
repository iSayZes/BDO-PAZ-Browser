# `redbattlefieldstaticstatusmanager.bss` Format

## Purpose

The Red Battlefield settings: 28 unnamed times and limits, the banner text
and the banner and map textures of the Red Battlefield window (client 3474
on), and the reward items for a win and a loss. On client 3474 the banner
text is "Red Battlefield: Castle Ruins", the win reward Battlefield Token
x50, Skill EXP (Red Battlefield Win) and Combat Secret Book (S), the loss
reward Battlefield Token x10 and Skill EXP (Red Battlefield Lose).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                    | Bytes | Records       | Row bytes |
| ------ | -------------- | --------------------------------------- | ----- | ------------- | --------- |
| 3      | 3275 and later | `redbattlefieldstaticstatusmanager.bss` | 488   | 5 Reward Item | 12        |
| 2      | 2819 to 3251   | `redbattlefieldstaticstatusmanager.bss` | 198   | 4 Reward Item | 12        |
| 1      | 2849 to 3229   | `redbattlefieldstaticstatusmanager.bss` | 178   | 4 Reward Item | 12        |

| Layout | File                                    | Known         | Unknown       |
| ------ | --------------------------------------- | ------------- | ------------- |
| 3      | `redbattlefieldstaticstatusmanager.bss` | 358 B (73.4%) | 130 B (26.6%) |
| 2      | `redbattlefieldstaticstatusmanager.bss` | 72 B (36.4%)  | 126 B (63.6%) |
| 1      | `redbattlefieldstaticstatusmanager.bss` | 72 B (40.4%)  | 106 B (59.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `69f98888dd39`  |
| 3482   | Layout 3             | `69f98888dd39`  |
| 3474   | Layout 3             | `69f98888dd39`  |
| 3473   | Layout 3             | `69f98888dd39`  |
| 3464   | Layout 3             | `69f98888dd39`  |
| 3458   | Layout 3             | `69f98888dd39`  |
| 3454   | Layout 3             | `69f98888dd39`  |
| 3444   | Layout 3             | `69f98888dd39`  |
| 3435   | Layout 3             | `69f98888dd39`  |
| 3426   | Layout 3             | `69f98888dd39`  |
| 3418   | Layout 3             | `69f98888dd39`  |
| 3412   | Layout 3             | `69f98888dd39`  |
| 3402   | Layout 3             | `69f98888dd39`  |
| 3396   | Layout 3             | `69f98888dd39`  |
| 3387   | Layout 3             | `69f98888dd39`  |
| 3381   | Layout 3             | `69f98888dd39`  |
| 3373   | Layout 3             | `69f98888dd39`  |
| 3364   | Layout 3             | `69f98888dd39`  |
| 3356   | Layout 3             | `69f98888dd39`  |
| 3349   | Layout 3             | `69f98888dd39`  |
| 3342   | Layout 3             | `69f98888dd39`  |
| 3335   | Layout 3             | `69f98888dd39`  |
| 3326   | Layout 3             | `69f98888dd39`  |
| 3321   | Layout 3             | `69f98888dd39`  |
| 3314   | Layout 3             | `69f98888dd39`  |
| 3303   | Layout 3             | `69f98888dd39`  |
| 3302   | Layout 3             | `69f98888dd39`  |
| 3293   | Layout 3             | `69f98888dd39`  |
| 3283   | Layout 3             | `69f98888dd39`  |
| 3275   | Layout 3             | `69f98888dd39`  |
| 3267   | No documented layout | `69f98888dd39`  |
| 3258   | No documented layout | `69f98888dd39`  |
| 3251   | Layout 2             | `69f98888dd39`  |
| 3242   | Layout 2             | `69f98888dd39`  |
| 3235   | No documented layout | `69f98888dd39`  |
| 3229   | Layout 1             | `69f98888dd39`  |
| 3212   | Layout 1             | `69f98888dd39`  |
| 3203   | Layout 1             | `69f98888dd39`  |
| 3193   | Layout 1             | `69f98888dd39`  |
| 3186   | Layout 1             | `69f98888dd39`  |
| 3177   | Layout 1             | `69f98888dd39`  |
| 3169   | Layout 1             | `69f98888dd39`  |
| 3158   | Layout 1             | `69f98888dd39`  |
| 3151   | Layout 1             | `69f98888dd39`  |
| 3144   | Layout 1             | `69f98888dd39`  |
| 3133   | Layout 1             | `69f98888dd39`  |
| 3125   | Layout 1             | `69f98888dd39`  |
| 3118   | Layout 1             | `69f98888dd39`  |
| 3111   | Layout 1             | `69f98888dd39`  |
| 3103   | Layout 1             | `69f98888dd39`  |
| 3095   | Layout 1             | `69f98888dd39`  |
| 3086   | Layout 1             | `69f98888dd39`  |
| 3072   | Layout 1             | `69f98888dd39`  |
| 3062   | Layout 1             | `69f98888dd39`  |
| 3052   | Layout 1             | `69f98888dd39`  |
| 3045   | Layout 1             | `69f98888dd39`  |
| 3037   | Layout 1             | `69f98888dd39`  |
| 3030   | Layout 1             | `69f98888dd39`  |
| 3021   | Layout 1             | `69f98888dd39`  |
| 3012   | Layout 1             | `69f98888dd39`  |
| 3002   | Layout 1             | `69f98888dd39`  |
| 2995   | Layout 1             | `69f98888dd39`  |
| 2987   | Layout 1             | `69f98888dd39`  |
| 2978   | Layout 1             | `69f98888dd39`  |
| 2970   | Layout 1             | `69f98888dd39`  |
| 2959   | Layout 1             | `69f98888dd39`  |
| 2951   | Layout 1             | `69f98888dd39`  |
| 2942   | Layout 1             | `69f98888dd39`  |
| 2935   | Layout 1             | `69f98888dd39`  |
| 2932   | Layout 1             | `69f98888dd39`  |
| 2923   | Layout 1             | `69f98888dd39`  |
| 2919   | Layout 1             | `69f98888dd39`  |
| 2907   | Layout 1             | `69f98888dd39`  |
| 2900   | Layout 1             | `69f98888dd39`  |
| 2891   | Layout 1             | `69f98888dd39`  |
| 2882   | Layout 1             | `69f98888dd39`  |
| 2872   | Layout 1             | `69f98888dd39`  |
| 2863   | Layout 1             | `69f98888dd39`  |
| 2855   | Layout 1             | `69f98888dd39`  |
| 2849   | Layout 1             | `69f98888dd39`  |
| 2844   | No documented layout | `69f98888dd39`  |
| 2834   | Layout 2             | `69f98888dd39`  |
| 2825   | Layout 2             | `69f98888dd39`  |
| 2819   | Layout 2             | `69f98888dd39`  |
| 2811   | No documented layout | `69f98888dd39`  |
| 2803   | No documented layout | `69f98888dd39`  |
| 2794   | No file              | `69f98888dd39`  |
| 2783   | No file              | `69f98888dd39`  |
| 2774   | No file              | `69f98888dd39`  |
| 2765   | No file              | `69f98888dd39`  |
| 2756   | No file              | `69f98888dd39`  |
| 2750   | No file              | `69f98888dd39`  |
| 2743   | No file              | `69f98888dd39`  |
| 2736   | No file              | `69f98888dd39`  |
| 2726   | No file              | `69f98888dd39`  |
| 2717   | No file              | `69f98888dd39`  |
| 2709   | No file              | `69f98888dd39`  |
| 2703   | No file              | `69f98888dd39`  |
| 2695   | No file              | `69f98888dd39`  |
| 2684   | No file              | `69f98888dd39`  |
| 2672   | No file              | `69f98888dd39`  |
| 2665   | No file              | `69f98888dd39`  |
| 2657   | No file              | `69f98888dd39`  |
| 2649   | No file              | `69f98888dd39`  |
| 2644   | No file              | `69f98888dd39`  |
| 2637   | No file              | `69f98888dd39`  |
| 2629   | No file              | `69f98888dd39`  |
| 2619   | No file              | `69f98888dd39`  |
| 2612   | No file              | `69f98888dd39`  |
| 2606   | No file              | `69f98888dd39`  |
| 2602   | No file              | `69f98888dd39`  |
| 2601   | No file              | `69f98888dd39`  |
| 2592   | No file              | `69f98888dd39`  |
| 2583   | No file              | `69f98888dd39`  |
| 2575   | No file              | `69f98888dd39`  |
| 2567   | No file              | `69f98888dd39`  |
| 2560   | No file              | `69f98888dd39`  |
| 2553   | No file              | `69f98888dd39`  |
| 2545   | No file              | `69f98888dd39`  |
| 2538   | No file              | `69f98888dd39`  |
| 2529   | No file              | `69f98888dd39`  |
| 2519   | No file              | `69f98888dd39`  |
| 2513   | No file              | `69f98888dd39`  |
| 2510   | No file              | `69f98888dd39`  |
| 2507   | No file              | `69f98888dd39`  |
| 2503   | No file              | `69f98888dd39`  |
| 2498   | No file              | `69f98888dd39`  |
| 2492   | No file              | `69f98888dd39`  |
| 2487   | No file              | `69f98888dd39`  |
| 2480   | No file              | `69f98888dd39`  |
| 2474   | No file              | `69f98888dd39`  |
| 2468   | No file              | `69f98888dd39`  |
| 2460   | No file              | `69f98888dd39`  |
| 2453   | No file              | `69f98888dd39`  |
| 2444   | No file              | `69f98888dd39`  |
| 2438   | No file              | `69f98888dd39`  |
| 2434   | No file              | `69f98888dd39`  |
| 2429   | No file              | `69f98888dd39`  |
| 2421   | No file              | `69f98888dd39`  |
| 2414   | No file              | `69f98888dd39`  |
| 2407   | No file              | `69f98888dd39`  |
| 2401   | No file              | `69f98888dd39`  |
| 2397   | No file              | `69f98888dd39`  |
| 2393   | No file              | `69f98888dd39`  |
| 2384   | No file              | `69f98888dd39`  |
| 2378   | No file              | `69f98888dd39`  |
| 2372   | No file              | `69f98888dd39`  |
| 2358   | No file              | `69f98888dd39`  |
| 2352   | No file              | `69f98888dd39`  |
| 2347   | No file              | `69f98888dd39`  |
| 2343   | No file              | `69f98888dd39`  |
| 2335   | No file              | `69f98888dd39`  |
| 2327   | No file              | `69f98888dd39`  |
| 2324   | No file              | `69f98888dd39`  |
| 2319   | No file              | `69f98888dd39`  |
| 2313   | No file              | `69f98888dd39`  |
| 2308   | No file              | `69f98888dd39`  |
| 2302   | No file              | `69f98888dd39`  |
| 2295   | No file              | `69f98888dd39`  |
| 2290   | No file              | `69f98888dd39`  |
| 2284   | No file              | `69f98888dd39`  |
| 2276   | No file              | `69f98888dd39`  |
| 2269   | No file              | `69f98888dd39`  |
| 2259   | No file              | `69f98888dd39`  |
| 2250   | No file              | `69f98888dd39`  |
| 2243   | No file              | `69f98888dd39`  |
| 2235   | No file              | `69f98888dd39`  |
| 2229   | No file              | `69f98888dd39`  |
| 2224   | No file              | `69f98888dd39`  |
| 2218   | No file              | `69f98888dd39`  |
| 2215   | No file              | `69f98888dd39`  |
| 2207   | No file              | `69f98888dd39`  |
| 2203   | No file              | `69f98888dd39`  |
| 2196   | No file              | `69f98888dd39`  |
| 2192   | No file              | `69f98888dd39`  |
| 2189   | No file              | `69f98888dd39`  |
| 2183   | No file              | `69f98888dd39`  |
| 2179   | No file              | `69f98888dd39`  |
| 2171   | No file              | `69f98888dd39`  |
| 2163   | No file              | `69f98888dd39`  |
| 2156   | No file              | `69f98888dd39`  |
| 2151   | No file              | `69f98888dd39`  |
| 2147   | No file              | `69f98888dd39`  |
| 2142   | No file              | `69f98888dd39`  |
| 2138   | No file              | `69f98888dd39`  |
| 2134   | No file              | `69f98888dd39`  |
| 2130   | No file              | `69f98888dd39`  |
| 2122   | No file              | `69f98888dd39`  |
| 2107   | No file              | `69f98888dd39`  |
| 2098   | No file              | `69f98888dd39`  |
| 2089   | No file              | `69f98888dd39`  |
| 2081   | No file              | `69f98888dd39`  |
| 2073   | No file              | `69f98888dd39`  |
| 2067   | No file              | `69f98888dd39`  |
| 2063   | No file              | `69f98888dd39`  |
| 2059   | No file              | `69f98888dd39`  |
| 2052   | No file              | `69f98888dd39`  |
| 2044   | No file              | `69f98888dd39`  |
| 2039   | No file              | `69f98888dd39`  |
| 2032   | No file              | `69f98888dd39`  |
| 2025   | No file              | `69f98888dd39`  |
| 2011   | No file              | `69f98888dd39`  |
| 2005   | No file              | `69f98888dd39`  |
| 2000   | No file              | `69f98888dd39`  |
| 1996   | No file              | `69f98888dd39`  |
| 1991   | No file              | `69f98888dd39`  |
| 1985   | No file              | `69f98888dd39`  |
| 1980   | No file              | `69f98888dd39`  |
| 1969   | No file              | `69f98888dd39`  |
| 1964   | No file              | `69f98888dd39`  |
| 1958   | No file              | `69f98888dd39`  |
| 1950   | No file              | `69f98888dd39`  |
| 1945   | No file              | `69f98888dd39`  |
| 1937   | No file              | `69f98888dd39`  |
| 1933   | No file              | `69f98888dd39`  |
| 1927   | No file              | `69f98888dd39`  |
| 1921   | No file              | `69f98888dd39`  |
| 1914   | No file              | `69f98888dd39`  |
| 1908   | No file              | `69f98888dd39`  |
| 1897   | No file              | `69f98888dd39`  |
| 1892   | No file              | `69f98888dd39`  |
| 1886   | No file              | `69f98888dd39`  |
| 1881   | No file              | `69f98888dd39`  |
| 1871   | No file              | `69f98888dd39`  |
| 1866   | No file              | `69f98888dd39`  |
| 1862   | No file              | `69f98888dd39`  |
| 1854   | No file              | `69f98888dd39`  |
| 1846   | No file              | `69f98888dd39`  |
| 1838   | No file              | `69f98888dd39`  |
| 1832   | No file              | `69f98888dd39`  |
| 1826   | No file              | `69f98888dd39`  |
| 1822   | No file              | `69f98888dd39`  |
| 1818   | No file              | `69f98888dd39`  |
| 1804   | No file              | `69f98888dd39`  |
| 1794   | No file              | `69f98888dd39`  |
| 1790   | No file              | `69f98888dd39`  |
| 1784   | No file              | `69f98888dd39`  |
| 1774   | No file              | `69f98888dd39`  |
| 1771   | No file              | `69f98888dd39`  |
| 1762   | No file              | `69f98888dd39`  |
| 1759   | No file              | `69f98888dd39`  |
| 1754   | No file              | `69f98888dd39`  |
| 1749   | No file              | `69f98888dd39`  |
| 1743   | No file              | `69f98888dd39`  |
| 1737   | No file              | `69f98888dd39`  |
| 1731   | No file              | `69f98888dd39`  |
| 1725   | No file              | `69f98888dd39`  |
| 1717   | No file              | `69f98888dd39`  |
| 1710   | No file              | `69f98888dd39`  |
| 1704   | No file              | `69f98888dd39`  |
| 1698   | No file              | `69f98888dd39`  |
| 1690   | No file              | `69f98888dd39`  |
| 1685   | No file              | `69f98888dd39`  |
| 1680   | No file              | `69f98888dd39`  |
| 1674   | No file              | `69f98888dd39`  |
| 1668   | No file              | `69f98888dd39`  |
| 1659   | No file              | `69f98888dd39`  |
| 1649   | No file              | `69f98888dd39`  |
| 1642   | No file              | `69f98888dd39`  |
| 1636   | No file              | `69f98888dd39`  |
| 1628   | No file              | `69f98888dd39`  |
| 1622   | No file              | `69f98888dd39`  |
| 1614   | No file              | `69f98888dd39`  |
| 1608   | No file              | `69f98888dd39`  |
| 1602   | No file              | `69f98888dd39`  |
| 1598   | No file              | `69f98888dd39`  |
| 1594   | No file              | `69f98888dd39`  |
| 1590   | No file              | `69f98888dd39`  |
| 1587   | No file              | `69f98888dd39`  |
| 1584   | No file              | `69f98888dd39`  |
| 1579   | No file              | `69f98888dd39`  |
| 1572   | No file              | `69f98888dd39`  |
| 1565   | No file              | `69f98888dd39`  |
| 1559   | No file              | `69f98888dd39`  |
| 1554   | No file              | `69f98888dd39`  |
| 1547   | No file              | `69f98888dd39`  |
| 1537   | No file              | `69f98888dd39`  |
| 1529   | No file              | `69f98888dd39`  |
| 1524   | No file              | `69f98888dd39`  |
| 1519   | No file              | `69f98888dd39`  |
| 1509   | No file              | `69f98888dd39`  |
| 1506   | No file              | `69f98888dd39`  |
| 1504   | No file              | `69f98888dd39`  |
| 1500   | No file              | `69f98888dd39`  |
| 1493   | No file              | `69f98888dd39`  |
| 1489   | No file              | `69f98888dd39`  |
| 1485   | No file              | `69f98888dd39`  |
| 1481   | No file              | `69f98888dd39`  |
| 1474   | No file              | `69f98888dd39`  |
| 1466   | No file              | `69f98888dd39`  |
| 1462   | No file              | `69f98888dd39`  |
| 1459   | No file              | `69f98888dd39`  |
| 1453   | No file              | `69f98888dd39`  |
| 1450   | No file              | `69f98888dd39`  |
| 1445   | No file              | `69f98888dd39`  |
| 1439   | No file              | `69f98888dd39`  |
| 1433   | No file              | `69f98888dd39`  |
| 1430   | No file              | `69f98888dd39`  |
| 1426   | No file              | `69f98888dd39`  |
| 1421   | No file              | `69f98888dd39`  |
| 1417   | No file              | `69f98888dd39`  |
| 1416   | No file              | `69f98888dd39`  |
| 1409   | No file              | `69f98888dd39`  |
| 1405   | No file              | `69f98888dd39`  |
| 1401   | No file              | `69f98888dd39`  |
| 1396   | No file              | `69f98888dd39`  |
| 1391   | No file              | `69f98888dd39`  |
| 1390   | No file              | `69f98888dd39`  |
| 1386   | No file              | `69f98888dd39`  |
| 1381   | No file              | `69f98888dd39`  |
| 1379   | No file              | `69f98888dd39`  |
| 1372   | No file              | `69f98888dd39`  |
| 1366   | No file              | `69f98888dd39`  |
| 1364   | No file              | `69f98888dd39`  |
| 1363   | No file              | `69f98888dd39`  |
| 1360   | No file              | `69f98888dd39`  |
| 1358   | No file              | `69f98888dd39`  |
| 1355   | No file              | `69f98888dd39`  |
| 1351   | No file              | `69f98888dd39`  |
| 1348   | No file              | `69f98888dd39`  |
| 1346   | No file              | `69f98888dd39`  |
| 1341   | No file              | `69f98888dd39`  |
| 1340   | No file              | `69f98888dd39`  |
| 1338   | No file              | `69f98888dd39`  |
| 1335   | No file              | `69f98888dd39`  |
| 1333   | No file              | `69f98888dd39`  |
| 1329   | No file              | `69f98888dd39`  |
| 1327   | No file              | `69f98888dd39`  |
| 1324   | No file              | `69f98888dd39`  |
| 1321   | No file              | `69f98888dd39`  |
| 1319   | No file              | `69f98888dd39`  |
| 1318   | No file              | `69f98888dd39`  |
| 1316   | No file              | `69f98888dd39`  |
| 1313   | No file              | `69f98888dd39`  |
| 1311   | No file              | `69f98888dd39`  |
| 1309   | No file              | `69f98888dd39`  |
| 1304   | No file              | `69f98888dd39`  |
| 1292   | No file              | `69f98888dd39`  |
| 1286   | No file              | `69f98888dd39`  |
| 1280   | No file              | `69f98888dd39`  |
| 1276   | No file              | `69f98888dd39`  |
| 1267   | No file              | `69f98888dd39`  |
| 1261   | No file              | `69f98888dd39`  |
| 1256   | No file              | `69f98888dd39`  |
| 1250   | No file              | `69f98888dd39`  |
| 1246   | No file              | `69f98888dd39`  |
| 1239   | No file              | `69f98888dd39`  |
| 1230   | No file              | `69f98888dd39`  |
| 1226   | No file              | `69f98888dd39`  |
| 1220   | No file              | `69f98888dd39`  |
| 1217   | No file              | `69f98888dd39`  |
| 1211   | No file              | `69f98888dd39`  |
| 1210   | No file              | `69f98888dd39`  |
| 1208   | No file              | `69f98888dd39`  |
| 1203   | No file              | `69f98888dd39`  |
| 1197   | No file              | `69f98888dd39`  |
| 1194   | No file              | `69f98888dd39`  |
| 1192   | No file              | `69f98888dd39`  |
| 1187   | No file              | `69f98888dd39`  |
| 1183   | No file              | `69f98888dd39`  |
| 1177   | No file              | `69f98888dd39`  |
| 1173   | No file              | `69f98888dd39`  |
| 1167   | No file              | `69f98888dd39`  |
| 1164   | No file              | `69f98888dd39`  |
| 1156   | No file              | `69f98888dd39`  |
| 1149   | No file              | `69f98888dd39`  |
| 1144   | No file              | `69f98888dd39`  |
| 1137   | No file              | `69f98888dd39`  |
| 1132   | No file              | `69f98888dd39`  |
| 1127   | No file              | `69f98888dd39`  |
| 1122   | No file              | `69f98888dd39`  |
| 1118   | No file              | `69f98888dd39`  |
| 1114   | No file              | `69f98888dd39`  |
| 1109   | No file              | `69f98888dd39`  |
| 1102   | No file              | `69f98888dd39`  |
| 1096   | No file              | `69f98888dd39`  |
| 1088   | No file              | `69f98888dd39`  |
| 1081   | No file              | `69f98888dd39`  |
| 1076   | No file              | `69f98888dd39`  |
| 1069   | No file              | `69f98888dd39`  |
| 1064   | No file              | `69f98888dd39`  |
| 1058   | No file              | `69f98888dd39`  |
| 1051   | No file              | `69f98888dd39`  |
| 1044   | No file              | `69f98888dd39`  |
| 1036   | No file              | `69f98888dd39`  |
| 1026   | No file              | `69f98888dd39`  |
| 1016   | No file              | `69f98888dd39`  |
| 1009   | No file              | `69f98888dd39`  |
| 1005   | No file              | `69f98888dd39`  |
| 1000   | No file              | `69f98888dd39`  |
| 998    | No file              | `69f98888dd39`  |
| 990    | No file              | `69f98888dd39`  |
| 979    | No file              | `69f98888dd39`  |
| 972    | No file              | `69f98888dd39`  |
| 963    | No file              | `69f98888dd39`  |
| 955    | No file              | `69f98888dd39`  |
| 946    | No file              | `69f98888dd39`  |
| 938    | No file              | `69f98888dd39`  |
| 927    | No file              | `69f98888dd39`  |
| 911    | No file              | `69f98888dd39`  |
| 904    | No file              | `69f98888dd39`  |
| 899    | No file              | `69f98888dd39`  |
| 894    | No file              | `69f98888dd39`  |
| 885    | No file              | `69f98888dd39`  |
| 879    | No file              | `69f98888dd39`  |
| 872    | No file              | `69f98888dd39`  |
| 864    | No file              | `69f98888dd39`  |
| 855    | No file              | `69f98888dd39`  |
| 853    | No file              | `69f98888dd39`  |
| 845    | No file              | `69f98888dd39`  |
| 837    | No file              | `69f98888dd39`  |
| 829    | No file              | `69f98888dd39`  |
| 822    | No file              | `69f98888dd39`  |
| 814    | No file              | `69f98888dd39`  |
| 805    | No file              | `69f98888dd39`  |
| 794    | No file              | `69f98888dd39`  |
| 787    | No file              | `69f98888dd39`  |
| 780    | No file              | `69f98888dd39`  |
| 771    | No file              | `69f98888dd39`  |
| 760    | No file              | `69f98888dd39`  |
| 748    | No file              | `69f98888dd39`  |
| 741    | No file              | `69f98888dd39`  |
| 736    | No file              | `69f98888dd39`  |
| 731    | No file              | `69f98888dd39`  |
| 723    | No file              | `69f98888dd39`  |
| 711    | No file              | `69f98888dd39`  |
| 707    | No file              | `69f98888dd39`  |
| 697    | No file              | `69f98888dd39`  |
| 689    | No file              | `69f98888dd39`  |
| 683    | No file              | `69f98888dd39`  |
| 678    | No file              | `69f98888dd39`  |
| 670    | No file              | `69f98888dd39`  |
| 661    | No file              | `69f98888dd39`  |
| 656    | No file              | `69f98888dd39`  |
| 652    | No file              | `69f98888dd39`  |
| 643    | No file              | `69f98888dd39`  |
| 637    | No file              | `69f98888dd39`  |
| 630    | No file              | `69f98888dd39`  |
| 627    | No file              | `69f98888dd39`  |
| 621    | No file              | `69f98888dd39`  |
| 617    | No file              | `69f98888dd39`  |
| 615    | No file              | `69f98888dd39`  |
| 606    | No file              | `69f98888dd39`  |
| 599    | No file              | `69f98888dd39`  |
| 592    | No file              | `69f98888dd39`  |
| 586    | No file              | `69f98888dd39`  |
| 577    | No file              | `69f98888dd39`  |
| 569    | No file              | `69f98888dd39`  |
| 561    | No file              | `69f98888dd39`  |
| 554    | No file              | `69f98888dd39`  |
| 542    | No file              | `69f98888dd39`  |
| 532    | No file              | `69f98888dd39`  |
| 531    | No file              | `69f98888dd39`  |
| 526    | No file              | `69f98888dd39`  |
| 521    | No file              | `69f98888dd39`  |
| 517    | No file              | `69f98888dd39`  |
| 510    | No file              | `69f98888dd39`  |
| 508    | No file              | `69f98888dd39`  |
| 504    | No file              | `69f98888dd39`  |
| 497    | No file              | `69f98888dd39`  |
| 491    | No file              | `69f98888dd39`  |
| 485    | No file              | `69f98888dd39`  |
| 478    | No file              | `69f98888dd39`  |
| 472    | No file              | `69f98888dd39`  |
| 466    | No file              | `69f98888dd39`  |
| 457    | No file              | `69f98888dd39`  |
| 452    | No file              | `69f98888dd39`  |
| 449    | No file              | `69f98888dd39`  |
| 435    | No file              | `69f98888dd39`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0; the banner text, LOC type 37      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                   | Type                          | Field                 | Notes                                                                    |
| ------------------------ | ----------------------------- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00`                  | char[4]                       | magic                 | ASCII `PABR`                                                             |
| `+0x04`                  | u32                           | unknown_04            | `300000` on clients 3002 to 3474                                         |
| `+0x08`                  | u64                           | unknown_08            | `120`                                                                    |
| `+0x10`                  | u16                           | unknown_10            | `1`                                                                      |
| `+0x12`                  | u16                           | unknown_12            | `426`                                                                    |
| `+0x14`                  | f32                           | unknown_14            | `200`                                                                    |
| `+0x18`                  | f32                           | unknown_18            | `180`                                                                    |
| `+0x1C`                  | f32                           | unknown_1c            | `580`                                                                    |
| `+0x20`                  | u16                           | unknown_20            | `20` on client 3474, `16` on 3002 and 3251                               |
| `+0x22`                  | u32                           | unknown_22            | `100`                                                                    |
| `+0x26`                  | f32                           | unknown_26            | `999`                                                                    |
| `+0x2A`                  | f32                           | unknown_2a            | `999`                                                                    |
| `+0x2E`                  | f32                           | unknown_2e            | `999`                                                                    |
| `+0x32`                  | u32                           | unknown_32            | `20`                                                                     |
| `+0x36`                  | u64                           | unknown_36            | `120`                                                                    |
| `+0x3E`                  | u64                           | unknown_3e            | `30`                                                                     |
| `+0x46`                  | u64                           | unknown_46            | `300`                                                                    |
| `+0x4E`                  | u32                           | unknown_4e            | `1`                                                                      |
| `+0x52`                  | u32                           | unknown_52            | `3`; not on client 3002                                                  |
| `+0x56`                  | u32                           | unknown_56            | `2`                                                                      |
| `+0x5A`                  | u32                           | unknown_5a            | `40` on client 3474, `20` on 3002 and 3251                               |
| `+0x5E`                  | u32                           | unknown_5e            | `30` on client 3474, `16` on 3002 and 3251                               |
| `+0x62`                  | u64                           | unknown_62            | `180`                                                                    |
| `+0x6A`                  | u64                           | unknown_6a            | `900`                                                                    |
| `+0x72`                  | u32                           | unknown_72            | `3`; not on client 3002                                                  |
| `+0x76`                  | u32                           | unknown_76            | `15` on client 3474, `3` on 3251                                         |
| `+0x7A`                  | u32                           | unknown_7a            | `200000` on client 3474, `1000` on 3251                                  |
| `+0x7E`                  | u32                           | unknown_7e            | `100000` on client 3474, `1200` on 3251                                  |
| `+0x82`                  | u32                           | unknown_82            | `3`; client 3474 only                                                    |
| `+0x86`                  | u32                           | banner_text_sheet_ref | String table index of the sheet of the banner text, `GAME`               |
| `+0x8A`                  | u32                           | banner_text_key_ref   | String table index of the banner text key, `LUA_WINDOW_VOICECHAT_SETTING_CHANNEL_2` ("Red Battlefield: Castle Ruins") |
| `+0x8E`                  | u32                           | banner_texture_ref    | String table index of the banner texture, `Combine_Etc_RedBattleField_War_Renewal_Img_02` |
| `+0x92`                  | u32                           | map_texture_ref       | String table index of the map texture, `Ingame_RedBattleField_War_Map_01` |
| `+0x96`                  | u32                           | win_reward_count      | Number of win rewards, up to 3 (the Lua asserts it)                      |
| `+0x9A`                  | Reward Item[win_reward_count] | win_reward_items      | See Reward Item                                                          |
| `win_reward_items+0x00`  | u32                           | lose_reward_count     | Number of loss rewards, up to 3                                          |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items    | See Reward Item                                                          |
| `lose_reward_items+0x00` | String Table                  | string_table          | See String Table                                                         |
| `string_table+0x00`      | u32                           | table_start           | Offset of the string table, where `lose_reward_items` ends               |
| `string_table+0x04`      | u32                           | zero                  | Always `0`                                                               |

Values without a client are the same on clients 3002, 3251 and 3474.

### Reward Item (12 bytes)

| Offset  | Type | Field      | Notes                                                                                     |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` |
| `+0x04` | u64  | item_count | Number of items                                                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `4` on client 3474, `0` on 3002 and 3251            |
| `+0x04` | pstr[string_count] | strings      | Wide ASCII: the sheet, the text key and the two texture names, in field order |

## Layout 2

### File Layout

| Offset                   | Type                          | Field             | Notes                                                       |
| ------------------------ | ----------------------------- | ----------------- | ----------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic             | ASCII `PABR`                                                |
| `+0x04`                  | u32                           | unknown_04        |                                                             |
| `+0x08`                  | u64                           | unknown_08        |                                                             |
| `+0x10`                  | u16                           | unknown_10        |                                                             |
| `+0x12`                  | u16                           | unknown_12        |                                                             |
| `+0x14`                  | f32                           | unknown_14        |                                                             |
| `+0x18`                  | f32                           | unknown_18        |                                                             |
| `+0x1C`                  | f32                           | unknown_1c        |                                                             |
| `+0x20`                  | u16                           | unknown_20        |                                                             |
| `+0x22`                  | u32                           | unknown_22        |                                                             |
| `+0x26`                  | f32                           | unknown_26        |                                                             |
| `+0x2A`                  | f32                           | unknown_2a        |                                                             |
| `+0x2E`                  | f32                           | unknown_2e        |                                                             |
| `+0x32`                  | u32                           | unknown_32        |                                                             |
| `+0x36`                  | u64                           | unknown_36        |                                                             |
| `+0x3E`                  | u64                           | unknown_3e        |                                                             |
| `+0x46`                  | u64                           | unknown_46        |                                                             |
| `+0x4E`                  | u32                           | unknown_4e        |                                                             |
| `+0x52`                  | u32                           | unknown_52        |                                                             |
| `+0x56`                  | u32                           | unknown_56        |                                                             |
| `+0x5A`                  | u32                           | unknown_5a        |                                                             |
| `+0x5E`                  | u32                           | unknown_5e        |                                                             |
| `+0x62`                  | u64                           | unknown_62        |                                                             |
| `+0x6A`                  | u64                           | unknown_6a        |                                                             |
| `+0x72`                  | u32                           | unknown_72        |                                                             |
| `+0x76`                  | u32                           | unknown_76        |                                                             |
| `+0x7A`                  | u32                           | unknown_7a        |                                                             |
| `+0x7E`                  | u32                           | unknown_7e        |                                                             |
| `+0x82`                  | u32                           | win_reward_count  | No `unknown_82` and no text or texture indexes before it    |
| `+0x86`                  | Reward Item[win_reward_count] | win_reward_items  | See Reward Item                                             |
| `win_reward_items+0x00`  | u32                           | lose_reward_count |                                                             |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items |                                                            |
| `lose_reward_items+0x00` | String Table                  | string_table      | No strings                                                  |
| `string_table+0x00`      | u32                           | table_start       |                                                             |
| `string_table+0x04`      | u32                           | zero              |                                                             |

## Layout 1

### File Layout

| Offset                   | Type                          | Field             | Notes                                                       |
| ------------------------ | ----------------------------- | ----------------- | ----------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic             | ASCII `PABR`                                                |
| `+0x04`                  | u32                           | unknown_04        |                                                             |
| `+0x08`                  | u64                           | unknown_08        |                                                             |
| `+0x10`                  | u16                           | unknown_10        |                                                             |
| `+0x12`                  | u16                           | unknown_12        |                                                             |
| `+0x14`                  | f32                           | unknown_14        |                                                             |
| `+0x18`                  | f32                           | unknown_18        |                                                             |
| `+0x1C`                  | f32                           | unknown_1c        |                                                             |
| `+0x20`                  | u16                           | unknown_20        |                                                             |
| `+0x22`                  | u32                           | unknown_22        |                                                             |
| `+0x26`                  | f32                           | unknown_26        |                                                             |
| `+0x2A`                  | f32                           | unknown_2a        |                                                             |
| `+0x2E`                  | f32                           | unknown_2e        |                                                             |
| `+0x32`                  | u32                           | unknown_32        |                                                             |
| `+0x36`                  | u64                           | unknown_36        |                                                             |
| `+0x3E`                  | u64                           | unknown_3e        |                                                             |
| `+0x46`                  | u64                           | unknown_46        |                                                             |
| `+0x4E`                  | u32                           | unknown_4e        |                                                             |
| `+0x52`                  | u32                           | unknown_56        | No `unknown_52` before it                                   |
| `+0x56`                  | u32                           | unknown_5a        |                                                             |
| `+0x5A`                  | u32                           | unknown_5e        |                                                             |
| `+0x5E`                  | u64                           | unknown_62        |                                                             |
| `+0x66`                  | u64                           | unknown_6a        |                                                             |
| `+0x6E`                  | u32                           | win_reward_count  | No `unknown_72` to `unknown_7e` before it                   |
| `+0x72`                  | Reward Item[win_reward_count] | win_reward_items  | See Reward Item                                             |
| `win_reward_items+0x00`  | u32                           | lose_reward_count |                                                             |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items |                                                            |
| `lose_reward_items+0x00` | String Table                  | string_table      | No strings                                                  |
| `string_table+0x00`      | u32                           | table_start       |                                                             |
| `string_table+0x04`      | u32                           | zero              |                                                             |

## Reward Items

| Client      | Win                                                                                      | Loss                                                              |
| ----------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 3002, 3251  | Weathered Battlefield Token (767689) x25, Skill EXP (Red Battlefield Win) (61) x1          | Weathered Battlefield Token x10, Skill EXP (Red Battlefield Lose) (62) x1 |
| 3474        | Battlefield Token (890002) x50, Skill EXP (Red Battlefield Win) x1, Combat Secret Book (S) (890117) x1 | Battlefield Token x10, Skill EXP (Red Battlefield Lose) x1 |

## Field Names

The Red Battlefield file is newer than client 1784 and 2107, which do not
ship it, so no sheet of a private server's `DataSheets.bexcel` covers it.
The named fields follow the client Lua of client 3474:

- `panel_redbattlefieldinfo_all` reads `ToClient_GetRedBattleFieldRewardSize(isWin)`,
  then per index `...RewardItemKey(isWin, index)` and `...RewardItemCount`,
  and asserts at most 3 rewards per side. The first list is the win side:
  its Skill EXP item is the Win one.
- `banner_Init` sets the banner title from
  `ToClient_GetRedBattleFieldBannerMapString()`, the banner from
  `...BannerTextureID()` and the minimap from `...MapTextureID()`. The four
  string-table entries are a GAME sheet key whose text names a battlefield
  map and two texture names, a banner image and a map image.

The Lua also reads `ToClient_GetPlayingTimeRedBattleField()`,
`...IntrusionTime...` (both divided by 60 for minutes),
`...MatchingPlayerCount()`, `...MaxPlayerCount()`,
`ToClient_GetAttackForLimitedRedBattleField()`, `...Defense...` and
`...ADSummary...`; which unnamed values they come from is not known.

## Notes

- The file is 178 bytes on client 3002, 198 on 3251 and 488 on 3474;
  clients 1784 to 2519 do not ship it.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  the banner text key with its text, the two textures and the reward items.

## Open Questions

### Unnamed Settings

Which of `unknown_04` to `unknown_82` are the play time, the join
(intrusion) time, the matching and maximum player counts and the AP, DP and
AP + DP limits of the limited Red Battlefield. Leads: `unknown_14` to
`unknown_1c` (200, 180, 580) and `unknown_26` to `unknown_2e` (999 each)
are float triples that fit the three limits; `unknown_6a` is 900 (15
minutes in seconds). The u64 and u16 widths follow zero high bytes and are
not confirmed.
