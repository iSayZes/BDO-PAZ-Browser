# `skilltype.dbss` Format

## Purpose

The presentation record of every skill: the Korean skill name, its family
name, whether it is active or passive, the skill icon, and a long action
configuration (animation, targeting and combat behaviour) that is not decoded.
This is where a skill's icon comes from.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes     | Records                       | Row bytes                    |
| ------ | -------------- | ------- | ---------------------- | --------- | ----------------------------- | ---------------------------- |
| 1      | 1346 and later | 3483    | `skilltype.dbss`       | 8,685,956 | 30,475 Payload, 30,475 Record | 153 to 1,041, 281 on average |
| 1      | 1346 and later | 3483    | `skilltypeoffset.dbss` | 365,720   | 30,475 Index Row              | 12                           |

| Layout | File                   | Known                | Unknown    |
| ------ | ---------------------- | -------------------- | ---------- |
| 1      | `skilltype.dbss`       | 8,685,956 B (100.0%) | 0 B (0.0%) |
| 1      | `skilltypeoffset.dbss` | 365,720 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `7df072972907`  |
| 3482   | Layout 1             | `7df072972907`  |
| 3474   | Layout 1             | `7df072972907`  |
| 3473   | Layout 1             | `7df072972907`  |
| 3464   | Layout 1             | `7df072972907`  |
| 3458   | Layout 1             | `7df072972907`  |
| 3454   | Layout 1             | `7df072972907`  |
| 3444   | Layout 1             | `7df072972907`  |
| 3435   | Layout 1             | `7df072972907`  |
| 3426   | Layout 1             | `7df072972907`  |
| 3418   | Layout 1             | `7df072972907`  |
| 3412   | Layout 1             | `7df072972907`  |
| 3402   | Layout 1             | `7df072972907`  |
| 3396   | Layout 1             | `7df072972907`  |
| 3387   | Layout 1             | `7df072972907`  |
| 3381   | Layout 1             | `7df072972907`  |
| 3373   | Layout 1             | `7df072972907`  |
| 3364   | Layout 1             | `7df072972907`  |
| 3356   | Layout 1             | `7df072972907`  |
| 3349   | Layout 1             | `7df072972907`  |
| 3342   | Layout 1             | `7df072972907`  |
| 3335   | Layout 1             | `7df072972907`  |
| 3326   | Layout 1             | `7df072972907`  |
| 3321   | Layout 1             | `7df072972907`  |
| 3314   | Layout 1             | `7df072972907`  |
| 3303   | Layout 1             | `7df072972907`  |
| 3302   | Layout 1             | `7df072972907`  |
| 3293   | Layout 1             | `7df072972907`  |
| 3283   | Layout 1             | `7df072972907`  |
| 3275   | Layout 1             | `7df072972907`  |
| 3267   | Layout 1             | `7df072972907`  |
| 3258   | Layout 1             | `7df072972907`  |
| 3251   | Layout 1             | `7df072972907`  |
| 3242   | Layout 1             | `7df072972907`  |
| 3235   | Layout 1             | `7df072972907`  |
| 3229   | Layout 1             | `7df072972907`  |
| 3212   | Layout 1             | `7df072972907`  |
| 3203   | Layout 1             | `7df072972907`  |
| 3193   | Layout 1             | `7df072972907`  |
| 3186   | Layout 1             | `7df072972907`  |
| 3177   | Layout 1             | `7df072972907`  |
| 3169   | Layout 1             | `7df072972907`  |
| 3158   | Layout 1             | `7df072972907`  |
| 3151   | Layout 1             | `7df072972907`  |
| 3144   | Layout 1             | `7df072972907`  |
| 3133   | Layout 1             | `7df072972907`  |
| 3125   | Layout 1             | `7df072972907`  |
| 3118   | Layout 1             | `7df072972907`  |
| 3111   | Layout 1             | `7df072972907`  |
| 3103   | Layout 1             | `7df072972907`  |
| 3095   | Layout 1             | `7df072972907`  |
| 3086   | Layout 1             | `7df072972907`  |
| 3072   | Layout 1             | `7df072972907`  |
| 3062   | Layout 1             | `7df072972907`  |
| 3052   | Layout 1             | `7df072972907`  |
| 3045   | Layout 1             | `7df072972907`  |
| 3037   | Layout 1             | `7df072972907`  |
| 3030   | Layout 1             | `7df072972907`  |
| 3021   | Layout 1             | `7df072972907`  |
| 3012   | Layout 1             | `7df072972907`  |
| 3002   | Layout 1             | `7df072972907`  |
| 2995   | Layout 1             | `7df072972907`  |
| 2987   | Layout 1             | `7df072972907`  |
| 2978   | Layout 1             | `7df072972907`  |
| 2970   | Layout 1             | `7df072972907`  |
| 2959   | Layout 1             | `7df072972907`  |
| 2951   | Layout 1             | `7df072972907`  |
| 2942   | Layout 1             | `7df072972907`  |
| 2935   | Layout 1             | `7df072972907`  |
| 2932   | Layout 1             | `7df072972907`  |
| 2923   | Layout 1             | `7df072972907`  |
| 2919   | Layout 1             | `7df072972907`  |
| 2907   | Layout 1             | `7df072972907`  |
| 2900   | Layout 1             | `7df072972907`  |
| 2891   | Layout 1             | `7df072972907`  |
| 2882   | Layout 1             | `7df072972907`  |
| 2872   | Layout 1             | `7df072972907`  |
| 2863   | Layout 1             | `7df072972907`  |
| 2855   | Layout 1             | `7df072972907`  |
| 2849   | Layout 1             | `7df072972907`  |
| 2844   | Layout 1             | `7df072972907`  |
| 2834   | Layout 1             | `7df072972907`  |
| 2825   | Layout 1             | `7df072972907`  |
| 2819   | Layout 1             | `7df072972907`  |
| 2811   | Layout 1             | `7df072972907`  |
| 2803   | Layout 1             | `7df072972907`  |
| 2794   | Layout 1             | `7df072972907`  |
| 2783   | Layout 1             | `7df072972907`  |
| 2774   | Layout 1             | `7df072972907`  |
| 2765   | Layout 1             | `7df072972907`  |
| 2756   | Layout 1             | `7df072972907`  |
| 2750   | Layout 1             | `7df072972907`  |
| 2743   | Layout 1             | `7df072972907`  |
| 2736   | Layout 1             | `7df072972907`  |
| 2726   | Layout 1             | `7df072972907`  |
| 2717   | Layout 1             | `7df072972907`  |
| 2709   | Layout 1             | `7df072972907`  |
| 2703   | Layout 1             | `7df072972907`  |
| 2695   | Layout 1             | `7df072972907`  |
| 2684   | Layout 1             | `7df072972907`  |
| 2672   | Layout 1             | `7df072972907`  |
| 2665   | Layout 1             | `7df072972907`  |
| 2657   | Layout 1             | `7df072972907`  |
| 2649   | Layout 1             | `7df072972907`  |
| 2644   | Layout 1             | `7df072972907`  |
| 2637   | Layout 1             | `7df072972907`  |
| 2629   | Layout 1             | `7df072972907`  |
| 2619   | Layout 1             | `7df072972907`  |
| 2612   | Layout 1             | `7df072972907`  |
| 2606   | Layout 1             | `7df072972907`  |
| 2602   | Layout 1             | `7df072972907`  |
| 2601   | Layout 1             | `7df072972907`  |
| 2592   | Layout 1             | `7df072972907`  |
| 2583   | Layout 1             | `7df072972907`  |
| 2575   | Layout 1             | `7df072972907`  |
| 2567   | Layout 1             | `7df072972907`  |
| 2560   | Layout 1             | `7df072972907`  |
| 2553   | Layout 1             | `7df072972907`  |
| 2545   | Layout 1             | `7df072972907`  |
| 2538   | Layout 1             | `7df072972907`  |
| 2529   | Layout 1             | `7df072972907`  |
| 2519   | Layout 1             | `7df072972907`  |
| 2513   | Layout 1             | `7df072972907`  |
| 2510   | Layout 1             | `7df072972907`  |
| 2507   | Layout 1             | `7df072972907`  |
| 2503   | Layout 1             | `7df072972907`  |
| 2498   | Layout 1             | `7df072972907`  |
| 2492   | Layout 1             | `7df072972907`  |
| 2487   | Layout 1             | `7df072972907`  |
| 2480   | Layout 1             | `7df072972907`  |
| 2474   | Layout 1             | `7df072972907`  |
| 2468   | Layout 1             | `7df072972907`  |
| 2460   | Layout 1             | `7df072972907`  |
| 2453   | Layout 1             | `7df072972907`  |
| 2444   | Layout 1             | `7df072972907`  |
| 2438   | Layout 1             | `7df072972907`  |
| 2434   | Layout 1             | `7df072972907`  |
| 2429   | Layout 1             | `7df072972907`  |
| 2421   | Layout 1             | `7df072972907`  |
| 2414   | Layout 1             | `7df072972907`  |
| 2407   | Layout 1             | `7df072972907`  |
| 2401   | Layout 1             | `7df072972907`  |
| 2397   | Layout 1             | `7df072972907`  |
| 2393   | Layout 1             | `7df072972907`  |
| 2384   | Layout 1             | `7df072972907`  |
| 2378   | Layout 1             | `7df072972907`  |
| 2372   | Layout 1             | `7df072972907`  |
| 2358   | Layout 1             | `7df072972907`  |
| 2352   | Layout 1             | `7df072972907`  |
| 2347   | Layout 1             | `7df072972907`  |
| 2343   | Layout 1             | `7df072972907`  |
| 2335   | Layout 1             | `7df072972907`  |
| 2327   | Layout 1             | `7df072972907`  |
| 2324   | Layout 1             | `7df072972907`  |
| 2319   | Layout 1             | `7df072972907`  |
| 2313   | Layout 1             | `7df072972907`  |
| 2308   | Layout 1             | `7df072972907`  |
| 2302   | Layout 1             | `7df072972907`  |
| 2295   | Layout 1             | `7df072972907`  |
| 2290   | Layout 1             | `7df072972907`  |
| 2284   | Layout 1             | `7df072972907`  |
| 2276   | Layout 1             | `7df072972907`  |
| 2269   | Layout 1             | `7df072972907`  |
| 2259   | Layout 1             | `7df072972907`  |
| 2250   | Layout 1             | `7df072972907`  |
| 2243   | Layout 1             | `7df072972907`  |
| 2235   | Layout 1             | `7df072972907`  |
| 2229   | Layout 1             | `7df072972907`  |
| 2224   | Layout 1             | `7df072972907`  |
| 2218   | Layout 1             | `7df072972907`  |
| 2215   | Layout 1             | `7df072972907`  |
| 2207   | Layout 1             | `7df072972907`  |
| 2203   | Layout 1             | `7df072972907`  |
| 2196   | Layout 1             | `7df072972907`  |
| 2192   | Layout 1             | `7df072972907`  |
| 2189   | Layout 1             | `7df072972907`  |
| 2183   | Layout 1             | `7df072972907`  |
| 2179   | Layout 1             | `7df072972907`  |
| 2171   | Layout 1             | `7df072972907`  |
| 2163   | Layout 1             | `7df072972907`  |
| 2156   | Layout 1             | `7df072972907`  |
| 2151   | Layout 1             | `7df072972907`  |
| 2147   | Layout 1             | `7df072972907`  |
| 2142   | Layout 1             | `7df072972907`  |
| 2138   | Layout 1             | `7df072972907`  |
| 2134   | Layout 1             | `7df072972907`  |
| 2130   | Layout 1             | `7df072972907`  |
| 2122   | Layout 1             | `7df072972907`  |
| 2107   | Layout 1             | `7df072972907`  |
| 2098   | Layout 1             | `7df072972907`  |
| 2089   | Layout 1             | `7df072972907`  |
| 2081   | Layout 1             | `7df072972907`  |
| 2073   | Layout 1             | `7df072972907`  |
| 2067   | Layout 1             | `7df072972907`  |
| 2063   | Layout 1             | `7df072972907`  |
| 2059   | Layout 1             | `7df072972907`  |
| 2052   | Layout 1             | `7df072972907`  |
| 2044   | Layout 1             | `7df072972907`  |
| 2039   | Layout 1             | `7df072972907`  |
| 2032   | Layout 1             | `7df072972907`  |
| 2025   | Layout 1             | `7df072972907`  |
| 2011   | Layout 1             | `7df072972907`  |
| 2005   | Layout 1             | `7df072972907`  |
| 2000   | Layout 1             | `7df072972907`  |
| 1996   | Layout 1             | `7df072972907`  |
| 1991   | Layout 1             | `7df072972907`  |
| 1985   | Layout 1             | `7df072972907`  |
| 1980   | Layout 1             | `7df072972907`  |
| 1969   | Layout 1             | `7df072972907`  |
| 1964   | Layout 1             | `7df072972907`  |
| 1958   | Layout 1             | `7df072972907`  |
| 1950   | Layout 1             | `7df072972907`  |
| 1945   | Layout 1             | `7df072972907`  |
| 1937   | Layout 1             | `7df072972907`  |
| 1933   | Layout 1             | `7df072972907`  |
| 1927   | Layout 1             | `7df072972907`  |
| 1921   | Layout 1             | `7df072972907`  |
| 1914   | Layout 1             | `7df072972907`  |
| 1908   | Layout 1             | `7df072972907`  |
| 1897   | Layout 1             | `7df072972907`  |
| 1892   | Layout 1             | `7df072972907`  |
| 1886   | Layout 1             | `7df072972907`  |
| 1881   | Layout 1             | `7df072972907`  |
| 1871   | Layout 1             | `7df072972907`  |
| 1866   | Layout 1             | `7df072972907`  |
| 1862   | Layout 1             | `7df072972907`  |
| 1854   | Layout 1             | `7df072972907`  |
| 1846   | Layout 1             | `7df072972907`  |
| 1838   | Layout 1             | `7df072972907`  |
| 1832   | Layout 1             | `7df072972907`  |
| 1826   | Layout 1             | `7df072972907`  |
| 1822   | Layout 1             | `7df072972907`  |
| 1818   | Layout 1             | `7df072972907`  |
| 1804   | Layout 1             | `7df072972907`  |
| 1794   | Layout 1             | `7df072972907`  |
| 1790   | Layout 1             | `7df072972907`  |
| 1784   | Layout 1             | `7df072972907`  |
| 1774   | Layout 1             | `7df072972907`  |
| 1771   | Layout 1             | `7df072972907`  |
| 1762   | Layout 1             | `7df072972907`  |
| 1759   | Layout 1             | `7df072972907`  |
| 1754   | Layout 1             | `7df072972907`  |
| 1749   | Layout 1             | `7df072972907`  |
| 1743   | Layout 1             | `7df072972907`  |
| 1737   | Layout 1             | `7df072972907`  |
| 1731   | Layout 1             | `7df072972907`  |
| 1725   | Layout 1             | `7df072972907`  |
| 1717   | Layout 1             | `7df072972907`  |
| 1710   | Layout 1             | `7df072972907`  |
| 1704   | Layout 1             | `7df072972907`  |
| 1698   | Layout 1             | `7df072972907`  |
| 1690   | Layout 1             | `7df072972907`  |
| 1685   | Layout 1             | `7df072972907`  |
| 1680   | Layout 1             | `7df072972907`  |
| 1674   | Layout 1             | `7df072972907`  |
| 1668   | Layout 1             | `7df072972907`  |
| 1659   | Layout 1             | `7df072972907`  |
| 1649   | Layout 1             | `7df072972907`  |
| 1642   | Layout 1             | `7df072972907`  |
| 1636   | Layout 1             | `7df072972907`  |
| 1628   | Layout 1             | `7df072972907`  |
| 1622   | Layout 1             | `7df072972907`  |
| 1614   | Layout 1             | `7df072972907`  |
| 1608   | Layout 1             | `7df072972907`  |
| 1602   | Layout 1             | `7df072972907`  |
| 1598   | Layout 1             | `7df072972907`  |
| 1594   | Layout 1             | `7df072972907`  |
| 1590   | Layout 1             | `7df072972907`  |
| 1587   | Layout 1             | `7df072972907`  |
| 1584   | Layout 1             | `7df072972907`  |
| 1579   | Layout 1             | `7df072972907`  |
| 1572   | Layout 1             | `7df072972907`  |
| 1565   | Layout 1             | `7df072972907`  |
| 1559   | Layout 1             | `7df072972907`  |
| 1554   | Layout 1             | `7df072972907`  |
| 1547   | Layout 1             | `7df072972907`  |
| 1537   | Layout 1             | `7df072972907`  |
| 1529   | Layout 1             | `7df072972907`  |
| 1524   | Layout 1             | `7df072972907`  |
| 1519   | Layout 1             | `7df072972907`  |
| 1509   | Layout 1             | `7df072972907`  |
| 1506   | Layout 1             | `7df072972907`  |
| 1504   | Layout 1             | `7df072972907`  |
| 1500   | Layout 1             | `7df072972907`  |
| 1493   | Layout 1             | `7df072972907`  |
| 1489   | Layout 1             | `7df072972907`  |
| 1485   | Layout 1             | `7df072972907`  |
| 1481   | Layout 1             | `7df072972907`  |
| 1474   | Layout 1             | `7df072972907`  |
| 1466   | Layout 1             | `7df072972907`  |
| 1462   | Layout 1             | `7df072972907`  |
| 1459   | Layout 1             | `7df072972907`  |
| 1453   | Layout 1             | `7df072972907`  |
| 1450   | Layout 1             | `7df072972907`  |
| 1445   | Layout 1             | `7df072972907`  |
| 1439   | Layout 1             | `7df072972907`  |
| 1433   | Layout 1             | `7df072972907`  |
| 1430   | Layout 1             | `7df072972907`  |
| 1426   | Layout 1             | `7df072972907`  |
| 1421   | Layout 1             | `7df072972907`  |
| 1417   | Layout 1             | `7df072972907`  |
| 1416   | Layout 1             | `7df072972907`  |
| 1409   | Layout 1             | `7df072972907`  |
| 1405   | Layout 1             | `7df072972907`  |
| 1401   | Layout 1             | `7df072972907`  |
| 1396   | Layout 1             | `7df072972907`  |
| 1391   | Layout 1             | `7df072972907`  |
| 1390   | Layout 1             | `7df072972907`  |
| 1386   | Layout 1             | `7df072972907`  |
| 1381   | Layout 1             | `7df072972907`  |
| 1379   | Layout 1             | `7df072972907`  |
| 1372   | Layout 1             | `7df072972907`  |
| 1366   | Layout 1             | `7df072972907`  |
| 1364   | Layout 1             | `7df072972907`  |
| 1363   | Layout 1             | `7df072972907`  |
| 1360   | Layout 1             | `7df072972907`  |
| 1358   | Layout 1             | `7df072972907`  |
| 1355   | Layout 1             | `7df072972907`  |
| 1351   | Layout 1             | `7df072972907`  |
| 1348   | Layout 1             | `7df072972907`  |
| 1346   | Layout 1             | `7df072972907`  |
| 1341   | No documented layout | `7df072972907`  |
| 1340   | No documented layout | `7df072972907`  |
| 1338   | No documented layout | `7df072972907`  |
| 1335   | No documented layout | `7df072972907`  |
| 1333   | No documented layout | `7df072972907`  |
| 1329   | No documented layout | `7df072972907`  |
| 1327   | No documented layout | `7df072972907`  |
| 1324   | No documented layout | `7df072972907`  |
| 1321   | No documented layout | `7df072972907`  |
| 1319   | No documented layout | `7df072972907`  |
| 1318   | No documented layout | `7df072972907`  |
| 1316   | No documented layout | `7df072972907`  |
| 1313   | No documented layout | `7df072972907`  |
| 1311   | No documented layout | `7df072972907`  |
| 1309   | No documented layout | `7df072972907`  |
| 1304   | No documented layout | `7df072972907`  |
| 1292   | No documented layout | `7df072972907`  |
| 1286   | No file              | `7df072972907`  |
| 1280   | No file              | `7df072972907`  |
| 1276   | No file              | `7df072972907`  |
| 1267   | No file              | `7df072972907`  |
| 1261   | No file              | `7df072972907`  |
| 1256   | No file              | `7df072972907`  |
| 1250   | No file              | `7df072972907`  |
| 1246   | No file              | `7df072972907`  |
| 1239   | No file              | `7df072972907`  |
| 1230   | No file              | `7df072972907`  |
| 1226   | No file              | `7df072972907`  |
| 1220   | No file              | `7df072972907`  |
| 1217   | No file              | `7df072972907`  |
| 1211   | No file              | `7df072972907`  |
| 1210   | No file              | `7df072972907`  |
| 1208   | No file              | `7df072972907`  |
| 1203   | No file              | `7df072972907`  |
| 1197   | No file              | `7df072972907`  |
| 1194   | No file              | `7df072972907`  |
| 1192   | No file              | `7df072972907`  |
| 1187   | No file              | `7df072972907`  |
| 1183   | No file              | `7df072972907`  |
| 1177   | No file              | `7df072972907`  |
| 1173   | No file              | `7df072972907`  |
| 1167   | No file              | `7df072972907`  |
| 1164   | No file              | `7df072972907`  |
| 1156   | No file              | `7df072972907`  |
| 1149   | No file              | `7df072972907`  |
| 1144   | No file              | `7df072972907`  |
| 1137   | No file              | `7df072972907`  |
| 1132   | No file              | `7df072972907`  |
| 1127   | No file              | `7df072972907`  |
| 1122   | No file              | `7df072972907`  |
| 1118   | No file              | `7df072972907`  |
| 1114   | No file              | `7df072972907`  |
| 1109   | No file              | `7df072972907`  |
| 1102   | No file              | `7df072972907`  |
| 1096   | No file              | `7df072972907`  |
| 1088   | No file              | `7df072972907`  |
| 1081   | No file              | `7df072972907`  |
| 1076   | No file              | `7df072972907`  |
| 1069   | No file              | `7df072972907`  |
| 1064   | No file              | `7df072972907`  |
| 1058   | No file              | `7df072972907`  |
| 1051   | No file              | `7df072972907`  |
| 1044   | No file              | `7df072972907`  |
| 1036   | No file              | `7df072972907`  |
| 1026   | No file              | `7df072972907`  |
| 1016   | No file              | `7df072972907`  |
| 1009   | No file              | `7df072972907`  |
| 1005   | No file              | `7df072972907`  |
| 1000   | No file              | `7df072972907`  |
| 998    | No file              | `7df072972907`  |
| 990    | No file              | `7df072972907`  |
| 979    | No file              | `7df072972907`  |
| 972    | No file              | `7df072972907`  |
| 963    | No file              | `7df072972907`  |
| 955    | No file              | `7df072972907`  |
| 946    | No file              | `7df072972907`  |
| 938    | No file              | `7df072972907`  |
| 927    | No file              | `7df072972907`  |
| 911    | No file              | `7df072972907`  |
| 904    | No file              | `7df072972907`  |
| 899    | No file              | `7df072972907`  |
| 894    | No file              | `7df072972907`  |
| 885    | No file              | `7df072972907`  |
| 879    | No file              | `7df072972907`  |
| 872    | No file              | `7df072972907`  |
| 864    | No file              | `7df072972907`  |
| 855    | No file              | `7df072972907`  |
| 853    | No file              | `7df072972907`  |
| 845    | No file              | `7df072972907`  |
| 837    | No file              | `7df072972907`  |
| 829    | No file              | `7df072972907`  |
| 822    | No file              | `7df072972907`  |
| 814    | No file              | `7df072972907`  |
| 805    | No file              | `7df072972907`  |
| 794    | No file              | `7df072972907`  |
| 787    | No file              | `7df072972907`  |
| 780    | No file              | `7df072972907`  |
| 771    | No file              | `7df072972907`  |
| 760    | No file              | `7df072972907`  |
| 748    | No file              | `7df072972907`  |
| 741    | No file              | `7df072972907`  |
| 736    | No file              | `7df072972907`  |
| 731    | No file              | `7df072972907`  |
| 723    | No file              | `7df072972907`  |
| 711    | No file              | `7df072972907`  |
| 707    | No file              | `7df072972907`  |
| 697    | No file              | `7df072972907`  |
| 689    | No file              | `7df072972907`  |
| 683    | No file              | `7df072972907`  |
| 678    | No file              | `7df072972907`  |
| 670    | No file              | `7df072972907`  |
| 661    | No file              | `7df072972907`  |
| 656    | No file              | `7df072972907`  |
| 652    | No file              | `7df072972907`  |
| 643    | No file              | `7df072972907`  |
| 637    | No file              | `7df072972907`  |
| 630    | No file              | `7df072972907`  |
| 627    | No file              | `7df072972907`  |
| 621    | No file              | `7df072972907`  |
| 617    | No file              | `7df072972907`  |
| 615    | No file              | `7df072972907`  |
| 606    | No file              | `7df072972907`  |
| 599    | No file              | `7df072972907`  |
| 592    | No file              | `7df072972907`  |
| 586    | No file              | `7df072972907`  |
| 577    | No file              | `7df072972907`  |
| 569    | No file              | `7df072972907`  |
| 561    | No file              | `7df072972907`  |
| 554    | No file              | `7df072972907`  |
| 542    | No file              | `7df072972907`  |
| 532    | No file              | `7df072972907`  |
| 531    | No file              | `7df072972907`  |
| 526    | No file              | `7df072972907`  |
| 521    | No file              | `7df072972907`  |
| 517    | No file              | `7df072972907`  |
| 510    | No file              | `7df072972907`  |
| 508    | No file              | `7df072972907`  |
| 504    | No file              | `7df072972907`  |
| 497    | No file              | `7df072972907`  |
| 491    | No file              | `7df072972907`  |
| 485    | No file              | `7df072972907`  |
| 478    | No file              | `7df072972907`  |
| 472    | No file              | `7df072972907`  |
| 466    | No file              | `7df072972907`  |
| 457    | No file              | `7df072972907`  |
| 452    | No file              | `7df072972907`  |
| 449    | No file              | `7df072972907`  |
| 435    | No file              | `7df072972907`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                             |
| ---------------------- | -------- | ---------------------------------------------------------------- |
| `skilltypeoffset.dbss` | Required | `skill_key → (offset, size)` index into this file                |
| `languagedata_en.loc`  | Optional | English names, LOC type `10`, `str_id1 = skill_no`               |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## Layout 1

### File Layout

The records tile the file like `skill.dbss`: each starts 4 bytes after the
previous one ends, the first at `8`, and the last ends at end of file. Strings
are a `u64` count followed by UTF-16LE units (text) or ASCII bytes (paths).

Every key is level `1`. 30,342 of the 30,352 keys are also in `skill.dbss`;
the 82 `skill.dbss` keys above level 1 have no record here.

| Offset  | Type          | Field   | Notes                                      |
| ------- | ------------- | ------- | ------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file |
| `+0x04` | Record[count] | records | See Record                                 |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                                       |
| ------- | ------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Each record is preceded by a repeated copy of its key       |
| `+0x04` | Payload | payload    | `size` bytes; the index row's `offset` points at this field |

### Payload (variable: 24 bytes + names and config, size from `skilltypeoffset.dbss`)

| Offset            | Type        | Field      | Notes                                                    |
| ----------------- | ----------- | ---------- | -------------------------------------------------------- |
| `+0x00`           | u32         | skill_key  | Equals the index key                                     |
| `+0x04`           | str16       | name       | Korean skill name, e.g. `거대한 진노 III`                 |
| `name+0x00`       | str16       | group_name | Korean family name, see [`group_name`](#group_name)      |
| `group_name+0x00` | u32         | kind       | `0` other, `1` active, `2` passive; see [`kind`](#kind)  |
| `group_name+0x04` | bytes[rest] | config     | Action configuration, not decoded; holds `icon_path`, see [`icon_path`](#icon_path) |

### `skilltypeoffset.dbss`

The layout of [`skilloffset.dbss`](skill_dbss.md#skilloffsetdbss). Read it with
`parse_pabr_u32_offset_rows()`.

| Offset              | Type             | Field        | Notes                                    |
| ------------------- | ---------------- | ------------ | ---------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                             |
| `+0x04`             | u32              | count        | Number of index rows; `30352` on client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                            |
| `rows+0x00`         | String Table     | string_table | Empty: `string_count` is `0`             |
| `string_table+0x00` | u32              | table_start  | End of the rows, `8 + 12 * count`        |
| `string_table+0x04` | u32              | zero         | Always 0                                 |

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                                  |
| ------- | ---- | --------- | ------------------------------------------------------ |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                              |
| `+0x04` | u32  | offset    | Byte offset of the record's `payload` in `skilltype.dbss` |
| `+0x08` | u32  | size      | Payload size in bytes                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes            |
| ------- | ------------------ | ------------ | ---------------- |
| `+0x00` | u32                | string_count | `0`              |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## `group_name`

Equal to `name` on 16,847 records. On the other 13,505 it is the name without
the rank or a qualifier: `거대한 진노 III` -> `거대한 진노`, `탈것 속도 증가 1.0%`
-> `속도 +1.0%`. Some are cut mid-phrase (`극 : 매화의 정신` -> `극 : 매화의`), so it
reads like a short label rather than a clean family name.

## `kind`

| Value | Meaning | Records | Example                                  |
| ----- | ------- | ------- | ---------------------------------------- |
| 0     | Other   | 14,382  | Item and event skills, "[Event] Energy of Happiness" (57005) |
| 1     | Active  | 10,219  | "Seismic Strike", "Fist Fury I"          |
| 2     | Passive | 5,751   | "Mountain Aura IX" to "XVI"              |

## `icon_path`

The skill icon is the first length-prefixed ASCII string in `config`, a `.dds`
path relative to `ui_texture/icon/`. `find_prefixed_ascii()` finds it, as for
`itemenchant.dbss`. Its position is not fixed: it follows a variable part of
the configuration, 49 to 69 bytes after `kind`.

| Kind    | With icon | Without |
| ------- | --------- | ------- |
| Other   | 186       | 14,196  |
| Active  | 7,654     | 2,565   |
| Passive | 1,562     | 4,189   |

9,402 records have an icon, never more than one, over 3,530 distinct paths.
Lower-cased under `ui_texture/icon/`, 3,452 of those paths exist in the
client's PAZ files on client 3458; the other 78 point at missing files
(for example `new_icon/04_pc_skill/01_pc_skill/31_prsa_skill/prsa_skill_8827.dds`).

`config` also holds 7,355 `.png` paths such as
`Real_ETC/Scroll/Icon_ETC_Scroll_00000000.png`; what they are for is not
known.

## Notes

- The first keys (`0xDEAD0001`, `0xDEAC0001`) look like sentinels but are
  real skills; see [`skill.dbss` Skill Keys](skill_dbss.md#skill-keys).
- The record layout of the first four fields and the `kind` meaning come from
  bdo-data-extractor; the counts, the icon rule and the `group_name` reading
  were checked against client 3458.
- LOC type `10` covers 28,343 of its 29,398 IDs with a skill number from this
  table or `skill.dbss`; 2,009 skill numbers have no type `10` row and 1,055
  type `10` IDs have no skill.

## Open Questions

### How is `config` laid out?

The configuration opens with small counts and lists (a run of `ff ff ff ff ff
7f`, the skill key again, and skill numbers and keys on class skills) before
the icon, which is why the icon moves between 49 and 69 bytes after `kind`.
Decoding it would give the icon a fixed place and expose the animation and
targeting fields, but nothing that is needed so far depends on it.
