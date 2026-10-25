# `employeespawnposition.dbss` Format

## Purpose

Spawn positions of the hireable sailors (the client calls sailors "employees") in the three port towns where they wait to be hired: Velia, Port Epheria and Iliya Island. Each row is a world position, a facing direction and the region the spot lies in. `employeespawninfo.dbss` lists, per sailor character, the spawn position keys that sailor can appear on. Companion `employeespawnpositionoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records               | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | --------------------- | --------- |
| 1      | 1267 and later | `employeespawnposition.dbss`       | 514   | 15 Spawn Position Row | 34        |
| 1      | 1267 and later | `employeespawnpositionoffset.dbss` | 184   | 15 Offset Row         | 12        |

| Layout | File                               | Known          | Unknown      |
| ------ | ---------------------------------- | -------------- | ------------ |
| 1      | `employeespawnposition.dbss`       | 454 B (88.3%)  | 60 B (11.7%) |
| 1      | `employeespawnpositionoffset.dbss` | 184 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e63452022211`  |
| 3482   | Layout 1 | `e63452022211`  |
| 3474   | Layout 1 | `e63452022211`  |
| 3473   | Layout 1 | `e63452022211`  |
| 3464   | Layout 1 | `e63452022211`  |
| 3458   | Layout 1 | `e63452022211`  |
| 3454   | Layout 1 | `e63452022211`  |
| 3444   | Layout 1 | `e63452022211`  |
| 3435   | Layout 1 | `e63452022211`  |
| 3426   | Layout 1 | `e63452022211`  |
| 3418   | Layout 1 | `e63452022211`  |
| 3412   | Layout 1 | `e63452022211`  |
| 3402   | Layout 1 | `e63452022211`  |
| 3396   | Layout 1 | `e63452022211`  |
| 3387   | Layout 1 | `e63452022211`  |
| 3381   | Layout 1 | `e63452022211`  |
| 3373   | Layout 1 | `e63452022211`  |
| 3364   | Layout 1 | `e63452022211`  |
| 3356   | Layout 1 | `e63452022211`  |
| 3349   | Layout 1 | `e63452022211`  |
| 3342   | Layout 1 | `e63452022211`  |
| 3335   | Layout 1 | `e63452022211`  |
| 3326   | Layout 1 | `e63452022211`  |
| 3321   | Layout 1 | `e63452022211`  |
| 3314   | Layout 1 | `e63452022211`  |
| 3303   | Layout 1 | `e63452022211`  |
| 3302   | Layout 1 | `e63452022211`  |
| 3293   | Layout 1 | `e63452022211`  |
| 3283   | Layout 1 | `e63452022211`  |
| 3275   | Layout 1 | `e63452022211`  |
| 3267   | Layout 1 | `e63452022211`  |
| 3258   | Layout 1 | `e63452022211`  |
| 3251   | Layout 1 | `e63452022211`  |
| 3242   | Layout 1 | `e63452022211`  |
| 3235   | Layout 1 | `e63452022211`  |
| 3229   | Layout 1 | `e63452022211`  |
| 3212   | Layout 1 | `e63452022211`  |
| 3203   | Layout 1 | `e63452022211`  |
| 3193   | Layout 1 | `e63452022211`  |
| 3186   | Layout 1 | `e63452022211`  |
| 3177   | Layout 1 | `e63452022211`  |
| 3169   | Layout 1 | `e63452022211`  |
| 3158   | Layout 1 | `e63452022211`  |
| 3151   | Layout 1 | `e63452022211`  |
| 3144   | Layout 1 | `e63452022211`  |
| 3133   | Layout 1 | `e63452022211`  |
| 3125   | Layout 1 | `e63452022211`  |
| 3118   | Layout 1 | `e63452022211`  |
| 3111   | Layout 1 | `e63452022211`  |
| 3103   | Layout 1 | `e63452022211`  |
| 3095   | Layout 1 | `e63452022211`  |
| 3086   | Layout 1 | `e63452022211`  |
| 3072   | Layout 1 | `e63452022211`  |
| 3062   | Layout 1 | `e63452022211`  |
| 3052   | Layout 1 | `e63452022211`  |
| 3045   | Layout 1 | `e63452022211`  |
| 3037   | Layout 1 | `e63452022211`  |
| 3030   | Layout 1 | `e63452022211`  |
| 3021   | Layout 1 | `e63452022211`  |
| 3012   | Layout 1 | `e63452022211`  |
| 3002   | Layout 1 | `e63452022211`  |
| 2995   | Layout 1 | `e63452022211`  |
| 2987   | Layout 1 | `e63452022211`  |
| 2978   | Layout 1 | `e63452022211`  |
| 2970   | Layout 1 | `e63452022211`  |
| 2959   | Layout 1 | `e63452022211`  |
| 2951   | Layout 1 | `e63452022211`  |
| 2942   | Layout 1 | `e63452022211`  |
| 2935   | Layout 1 | `e63452022211`  |
| 2932   | Layout 1 | `e63452022211`  |
| 2923   | Layout 1 | `e63452022211`  |
| 2919   | Layout 1 | `e63452022211`  |
| 2907   | Layout 1 | `e63452022211`  |
| 2900   | Layout 1 | `e63452022211`  |
| 2891   | Layout 1 | `e63452022211`  |
| 2882   | Layout 1 | `e63452022211`  |
| 2872   | Layout 1 | `e63452022211`  |
| 2863   | Layout 1 | `e63452022211`  |
| 2855   | Layout 1 | `e63452022211`  |
| 2849   | Layout 1 | `e63452022211`  |
| 2844   | Layout 1 | `e63452022211`  |
| 2834   | Layout 1 | `e63452022211`  |
| 2825   | Layout 1 | `e63452022211`  |
| 2819   | Layout 1 | `e63452022211`  |
| 2811   | Layout 1 | `e63452022211`  |
| 2803   | Layout 1 | `e63452022211`  |
| 2794   | Layout 1 | `e63452022211`  |
| 2783   | Layout 1 | `e63452022211`  |
| 2774   | Layout 1 | `e63452022211`  |
| 2765   | Layout 1 | `e63452022211`  |
| 2756   | Layout 1 | `e63452022211`  |
| 2750   | Layout 1 | `e63452022211`  |
| 2743   | Layout 1 | `e63452022211`  |
| 2736   | Layout 1 | `e63452022211`  |
| 2726   | Layout 1 | `e63452022211`  |
| 2717   | Layout 1 | `e63452022211`  |
| 2709   | Layout 1 | `e63452022211`  |
| 2703   | Layout 1 | `e63452022211`  |
| 2695   | Layout 1 | `e63452022211`  |
| 2684   | Layout 1 | `e63452022211`  |
| 2672   | Layout 1 | `e63452022211`  |
| 2665   | Layout 1 | `e63452022211`  |
| 2657   | Layout 1 | `e63452022211`  |
| 2649   | Layout 1 | `e63452022211`  |
| 2644   | Layout 1 | `e63452022211`  |
| 2637   | Layout 1 | `e63452022211`  |
| 2629   | Layout 1 | `e63452022211`  |
| 2619   | Layout 1 | `e63452022211`  |
| 2612   | Layout 1 | `e63452022211`  |
| 2606   | Layout 1 | `e63452022211`  |
| 2602   | Layout 1 | `e63452022211`  |
| 2601   | Layout 1 | `e63452022211`  |
| 2592   | Layout 1 | `e63452022211`  |
| 2583   | Layout 1 | `e63452022211`  |
| 2575   | Layout 1 | `e63452022211`  |
| 2567   | Layout 1 | `e63452022211`  |
| 2560   | Layout 1 | `e63452022211`  |
| 2553   | Layout 1 | `e63452022211`  |
| 2545   | Layout 1 | `e63452022211`  |
| 2538   | Layout 1 | `e63452022211`  |
| 2529   | Layout 1 | `e63452022211`  |
| 2519   | Layout 1 | `e63452022211`  |
| 2513   | Layout 1 | `e63452022211`  |
| 2510   | Layout 1 | `e63452022211`  |
| 2507   | Layout 1 | `e63452022211`  |
| 2503   | Layout 1 | `e63452022211`  |
| 2498   | Layout 1 | `e63452022211`  |
| 2492   | Layout 1 | `e63452022211`  |
| 2487   | Layout 1 | `e63452022211`  |
| 2480   | Layout 1 | `e63452022211`  |
| 2474   | Layout 1 | `e63452022211`  |
| 2468   | Layout 1 | `e63452022211`  |
| 2460   | Layout 1 | `e63452022211`  |
| 2453   | Layout 1 | `e63452022211`  |
| 2444   | Layout 1 | `e63452022211`  |
| 2438   | Layout 1 | `e63452022211`  |
| 2434   | Layout 1 | `e63452022211`  |
| 2429   | Layout 1 | `e63452022211`  |
| 2421   | Layout 1 | `e63452022211`  |
| 2414   | Layout 1 | `e63452022211`  |
| 2407   | Layout 1 | `e63452022211`  |
| 2401   | Layout 1 | `e63452022211`  |
| 2397   | Layout 1 | `e63452022211`  |
| 2393   | Layout 1 | `e63452022211`  |
| 2384   | Layout 1 | `e63452022211`  |
| 2378   | Layout 1 | `e63452022211`  |
| 2372   | Layout 1 | `e63452022211`  |
| 2358   | Layout 1 | `e63452022211`  |
| 2352   | Layout 1 | `e63452022211`  |
| 2347   | Layout 1 | `e63452022211`  |
| 2343   | Layout 1 | `e63452022211`  |
| 2335   | Layout 1 | `e63452022211`  |
| 2327   | Layout 1 | `e63452022211`  |
| 2324   | Layout 1 | `e63452022211`  |
| 2319   | Layout 1 | `e63452022211`  |
| 2313   | Layout 1 | `e63452022211`  |
| 2308   | Layout 1 | `e63452022211`  |
| 2302   | Layout 1 | `e63452022211`  |
| 2295   | Layout 1 | `e63452022211`  |
| 2290   | Layout 1 | `e63452022211`  |
| 2284   | Layout 1 | `e63452022211`  |
| 2276   | Layout 1 | `e63452022211`  |
| 2269   | Layout 1 | `e63452022211`  |
| 2259   | Layout 1 | `e63452022211`  |
| 2250   | Layout 1 | `e63452022211`  |
| 2243   | Layout 1 | `e63452022211`  |
| 2235   | Layout 1 | `e63452022211`  |
| 2229   | Layout 1 | `e63452022211`  |
| 2224   | Layout 1 | `e63452022211`  |
| 2218   | Layout 1 | `e63452022211`  |
| 2215   | Layout 1 | `e63452022211`  |
| 2207   | Layout 1 | `e63452022211`  |
| 2203   | Layout 1 | `e63452022211`  |
| 2196   | Layout 1 | `e63452022211`  |
| 2192   | Layout 1 | `e63452022211`  |
| 2189   | Layout 1 | `e63452022211`  |
| 2183   | Layout 1 | `e63452022211`  |
| 2179   | Layout 1 | `e63452022211`  |
| 2171   | Layout 1 | `e63452022211`  |
| 2163   | Layout 1 | `e63452022211`  |
| 2156   | Layout 1 | `e63452022211`  |
| 2151   | Layout 1 | `e63452022211`  |
| 2147   | Layout 1 | `e63452022211`  |
| 2142   | Layout 1 | `e63452022211`  |
| 2138   | Layout 1 | `e63452022211`  |
| 2134   | Layout 1 | `e63452022211`  |
| 2130   | Layout 1 | `e63452022211`  |
| 2122   | Layout 1 | `e63452022211`  |
| 2107   | Layout 1 | `e63452022211`  |
| 2098   | Layout 1 | `e63452022211`  |
| 2089   | Layout 1 | `e63452022211`  |
| 2081   | Layout 1 | `e63452022211`  |
| 2073   | Layout 1 | `e63452022211`  |
| 2067   | Layout 1 | `e63452022211`  |
| 2063   | Layout 1 | `e63452022211`  |
| 2059   | Layout 1 | `e63452022211`  |
| 2052   | Layout 1 | `e63452022211`  |
| 2044   | Layout 1 | `e63452022211`  |
| 2039   | Layout 1 | `e63452022211`  |
| 2032   | Layout 1 | `e63452022211`  |
| 2025   | Layout 1 | `e63452022211`  |
| 2011   | Layout 1 | `e63452022211`  |
| 2005   | Layout 1 | `e63452022211`  |
| 2000   | Layout 1 | `e63452022211`  |
| 1996   | Layout 1 | `e63452022211`  |
| 1991   | Layout 1 | `e63452022211`  |
| 1985   | Layout 1 | `e63452022211`  |
| 1980   | Layout 1 | `e63452022211`  |
| 1969   | Layout 1 | `e63452022211`  |
| 1964   | Layout 1 | `e63452022211`  |
| 1958   | Layout 1 | `e63452022211`  |
| 1950   | Layout 1 | `e63452022211`  |
| 1945   | Layout 1 | `e63452022211`  |
| 1937   | Layout 1 | `e63452022211`  |
| 1933   | Layout 1 | `e63452022211`  |
| 1927   | Layout 1 | `e63452022211`  |
| 1921   | Layout 1 | `e63452022211`  |
| 1914   | Layout 1 | `e63452022211`  |
| 1908   | Layout 1 | `e63452022211`  |
| 1897   | Layout 1 | `e63452022211`  |
| 1892   | Layout 1 | `e63452022211`  |
| 1886   | Layout 1 | `e63452022211`  |
| 1881   | Layout 1 | `e63452022211`  |
| 1871   | Layout 1 | `e63452022211`  |
| 1866   | Layout 1 | `e63452022211`  |
| 1862   | Layout 1 | `e63452022211`  |
| 1854   | Layout 1 | `e63452022211`  |
| 1846   | Layout 1 | `e63452022211`  |
| 1838   | Layout 1 | `e63452022211`  |
| 1832   | Layout 1 | `e63452022211`  |
| 1826   | Layout 1 | `e63452022211`  |
| 1822   | Layout 1 | `e63452022211`  |
| 1818   | Layout 1 | `e63452022211`  |
| 1804   | Layout 1 | `e63452022211`  |
| 1794   | Layout 1 | `e63452022211`  |
| 1790   | Layout 1 | `e63452022211`  |
| 1784   | Layout 1 | `e63452022211`  |
| 1774   | Layout 1 | `e63452022211`  |
| 1771   | Layout 1 | `e63452022211`  |
| 1762   | Layout 1 | `e63452022211`  |
| 1759   | Layout 1 | `e63452022211`  |
| 1754   | Layout 1 | `e63452022211`  |
| 1749   | Layout 1 | `e63452022211`  |
| 1743   | Layout 1 | `e63452022211`  |
| 1737   | Layout 1 | `e63452022211`  |
| 1731   | Layout 1 | `e63452022211`  |
| 1725   | Layout 1 | `e63452022211`  |
| 1717   | Layout 1 | `e63452022211`  |
| 1710   | Layout 1 | `e63452022211`  |
| 1704   | Layout 1 | `e63452022211`  |
| 1698   | Layout 1 | `e63452022211`  |
| 1690   | Layout 1 | `e63452022211`  |
| 1685   | Layout 1 | `e63452022211`  |
| 1680   | Layout 1 | `e63452022211`  |
| 1674   | Layout 1 | `e63452022211`  |
| 1668   | Layout 1 | `e63452022211`  |
| 1659   | Layout 1 | `e63452022211`  |
| 1649   | Layout 1 | `e63452022211`  |
| 1642   | Layout 1 | `e63452022211`  |
| 1636   | Layout 1 | `e63452022211`  |
| 1628   | Layout 1 | `e63452022211`  |
| 1622   | Layout 1 | `e63452022211`  |
| 1614   | Layout 1 | `e63452022211`  |
| 1608   | Layout 1 | `e63452022211`  |
| 1602   | Layout 1 | `e63452022211`  |
| 1598   | Layout 1 | `e63452022211`  |
| 1594   | Layout 1 | `e63452022211`  |
| 1590   | Layout 1 | `e63452022211`  |
| 1587   | Layout 1 | `e63452022211`  |
| 1584   | Layout 1 | `e63452022211`  |
| 1579   | Layout 1 | `e63452022211`  |
| 1572   | Layout 1 | `e63452022211`  |
| 1565   | Layout 1 | `e63452022211`  |
| 1559   | Layout 1 | `e63452022211`  |
| 1554   | Layout 1 | `e63452022211`  |
| 1547   | Layout 1 | `e63452022211`  |
| 1537   | Layout 1 | `e63452022211`  |
| 1529   | Layout 1 | `e63452022211`  |
| 1524   | Layout 1 | `e63452022211`  |
| 1519   | Layout 1 | `e63452022211`  |
| 1509   | Layout 1 | `e63452022211`  |
| 1506   | Layout 1 | `e63452022211`  |
| 1504   | Layout 1 | `e63452022211`  |
| 1500   | Layout 1 | `e63452022211`  |
| 1493   | Layout 1 | `e63452022211`  |
| 1489   | Layout 1 | `e63452022211`  |
| 1485   | Layout 1 | `e63452022211`  |
| 1481   | Layout 1 | `e63452022211`  |
| 1474   | Layout 1 | `e63452022211`  |
| 1466   | Layout 1 | `e63452022211`  |
| 1462   | Layout 1 | `e63452022211`  |
| 1459   | Layout 1 | `e63452022211`  |
| 1453   | Layout 1 | `e63452022211`  |
| 1450   | Layout 1 | `e63452022211`  |
| 1445   | Layout 1 | `e63452022211`  |
| 1439   | Layout 1 | `e63452022211`  |
| 1433   | Layout 1 | `e63452022211`  |
| 1430   | Layout 1 | `e63452022211`  |
| 1426   | Layout 1 | `e63452022211`  |
| 1421   | Layout 1 | `e63452022211`  |
| 1417   | Layout 1 | `e63452022211`  |
| 1416   | Layout 1 | `e63452022211`  |
| 1409   | Layout 1 | `e63452022211`  |
| 1405   | Layout 1 | `e63452022211`  |
| 1401   | Layout 1 | `e63452022211`  |
| 1396   | Layout 1 | `e63452022211`  |
| 1391   | Layout 1 | `e63452022211`  |
| 1390   | Layout 1 | `e63452022211`  |
| 1386   | Layout 1 | `e63452022211`  |
| 1381   | Layout 1 | `e63452022211`  |
| 1379   | Layout 1 | `e63452022211`  |
| 1372   | Layout 1 | `e63452022211`  |
| 1366   | Layout 1 | `e63452022211`  |
| 1364   | Layout 1 | `e63452022211`  |
| 1363   | Layout 1 | `e63452022211`  |
| 1360   | Layout 1 | `e63452022211`  |
| 1358   | Layout 1 | `e63452022211`  |
| 1355   | Layout 1 | `e63452022211`  |
| 1351   | Layout 1 | `e63452022211`  |
| 1348   | Layout 1 | `e63452022211`  |
| 1346   | Layout 1 | `e63452022211`  |
| 1341   | Layout 1 | `e63452022211`  |
| 1340   | Layout 1 | `e63452022211`  |
| 1338   | Layout 1 | `e63452022211`  |
| 1335   | Layout 1 | `e63452022211`  |
| 1333   | Layout 1 | `e63452022211`  |
| 1329   | Layout 1 | `e63452022211`  |
| 1327   | Layout 1 | `e63452022211`  |
| 1324   | Layout 1 | `e63452022211`  |
| 1321   | Layout 1 | `e63452022211`  |
| 1319   | Layout 1 | `e63452022211`  |
| 1318   | Layout 1 | `e63452022211`  |
| 1316   | Layout 1 | `e63452022211`  |
| 1313   | Layout 1 | `e63452022211`  |
| 1311   | Layout 1 | `e63452022211`  |
| 1309   | Layout 1 | `e63452022211`  |
| 1304   | Layout 1 | `e63452022211`  |
| 1292   | Layout 1 | `e63452022211`  |
| 1286   | Layout 1 | `e63452022211`  |
| 1280   | Layout 1 | `e63452022211`  |
| 1276   | Layout 1 | `e63452022211`  |
| 1267   | Layout 1 | `e63452022211`  |
| 1261   | No file  | `e63452022211`  |
| 1256   | No file  | `e63452022211`  |
| 1250   | No file  | `e63452022211`  |
| 1246   | No file  | `e63452022211`  |
| 1239   | No file  | `e63452022211`  |
| 1230   | No file  | `e63452022211`  |
| 1226   | No file  | `e63452022211`  |
| 1220   | No file  | `e63452022211`  |
| 1217   | No file  | `e63452022211`  |
| 1211   | No file  | `e63452022211`  |
| 1210   | No file  | `e63452022211`  |
| 1208   | No file  | `e63452022211`  |
| 1203   | No file  | `e63452022211`  |
| 1197   | No file  | `e63452022211`  |
| 1194   | No file  | `e63452022211`  |
| 1192   | No file  | `e63452022211`  |
| 1187   | No file  | `e63452022211`  |
| 1183   | No file  | `e63452022211`  |
| 1177   | No file  | `e63452022211`  |
| 1173   | No file  | `e63452022211`  |
| 1167   | No file  | `e63452022211`  |
| 1164   | No file  | `e63452022211`  |
| 1156   | No file  | `e63452022211`  |
| 1149   | No file  | `e63452022211`  |
| 1144   | No file  | `e63452022211`  |
| 1137   | No file  | `e63452022211`  |
| 1132   | No file  | `e63452022211`  |
| 1127   | No file  | `e63452022211`  |
| 1122   | No file  | `e63452022211`  |
| 1118   | No file  | `e63452022211`  |
| 1114   | No file  | `e63452022211`  |
| 1109   | No file  | `e63452022211`  |
| 1102   | No file  | `e63452022211`  |
| 1096   | No file  | `e63452022211`  |
| 1088   | No file  | `e63452022211`  |
| 1081   | No file  | `e63452022211`  |
| 1076   | No file  | `e63452022211`  |
| 1069   | No file  | `e63452022211`  |
| 1064   | No file  | `e63452022211`  |
| 1058   | No file  | `e63452022211`  |
| 1051   | No file  | `e63452022211`  |
| 1044   | No file  | `e63452022211`  |
| 1036   | No file  | `e63452022211`  |
| 1026   | No file  | `e63452022211`  |
| 1016   | No file  | `e63452022211`  |
| 1009   | No file  | `e63452022211`  |
| 1005   | No file  | `e63452022211`  |
| 1000   | No file  | `e63452022211`  |
| 998    | No file  | `e63452022211`  |
| 990    | No file  | `e63452022211`  |
| 979    | No file  | `e63452022211`  |
| 972    | No file  | `e63452022211`  |
| 963    | No file  | `e63452022211`  |
| 955    | No file  | `e63452022211`  |
| 946    | No file  | `e63452022211`  |
| 938    | No file  | `e63452022211`  |
| 927    | No file  | `e63452022211`  |
| 911    | No file  | `e63452022211`  |
| 904    | No file  | `e63452022211`  |
| 899    | No file  | `e63452022211`  |
| 894    | No file  | `e63452022211`  |
| 885    | No file  | `e63452022211`  |
| 879    | No file  | `e63452022211`  |
| 872    | No file  | `e63452022211`  |
| 864    | No file  | `e63452022211`  |
| 855    | No file  | `e63452022211`  |
| 853    | No file  | `e63452022211`  |
| 845    | No file  | `e63452022211`  |
| 837    | No file  | `e63452022211`  |
| 829    | No file  | `e63452022211`  |
| 822    | No file  | `e63452022211`  |
| 814    | No file  | `e63452022211`  |
| 805    | No file  | `e63452022211`  |
| 794    | No file  | `e63452022211`  |
| 787    | No file  | `e63452022211`  |
| 780    | No file  | `e63452022211`  |
| 771    | No file  | `e63452022211`  |
| 760    | No file  | `e63452022211`  |
| 748    | No file  | `e63452022211`  |
| 741    | No file  | `e63452022211`  |
| 736    | No file  | `e63452022211`  |
| 731    | No file  | `e63452022211`  |
| 723    | No file  | `e63452022211`  |
| 711    | No file  | `e63452022211`  |
| 707    | No file  | `e63452022211`  |
| 697    | No file  | `e63452022211`  |
| 689    | No file  | `e63452022211`  |
| 683    | No file  | `e63452022211`  |
| 678    | No file  | `e63452022211`  |
| 670    | No file  | `e63452022211`  |
| 661    | No file  | `e63452022211`  |
| 656    | No file  | `e63452022211`  |
| 652    | No file  | `e63452022211`  |
| 643    | No file  | `e63452022211`  |
| 637    | No file  | `e63452022211`  |
| 630    | No file  | `e63452022211`  |
| 627    | No file  | `e63452022211`  |
| 621    | No file  | `e63452022211`  |
| 617    | No file  | `e63452022211`  |
| 615    | No file  | `e63452022211`  |
| 606    | No file  | `e63452022211`  |
| 599    | No file  | `e63452022211`  |
| 592    | No file  | `e63452022211`  |
| 586    | No file  | `e63452022211`  |
| 577    | No file  | `e63452022211`  |
| 569    | No file  | `e63452022211`  |
| 561    | No file  | `e63452022211`  |
| 554    | No file  | `e63452022211`  |
| 542    | No file  | `e63452022211`  |
| 532    | No file  | `e63452022211`  |
| 531    | No file  | `e63452022211`  |
| 526    | No file  | `e63452022211`  |
| 521    | No file  | `e63452022211`  |
| 517    | No file  | `e63452022211`  |
| 510    | No file  | `e63452022211`  |
| 508    | No file  | `e63452022211`  |
| 504    | No file  | `e63452022211`  |
| 497    | No file  | `e63452022211`  |
| 491    | No file  | `e63452022211`  |
| 485    | No file  | `e63452022211`  |
| 478    | No file  | `e63452022211`  |
| 472    | No file  | `e63452022211`  |
| 466    | No file  | `e63452022211`  |
| 457    | No file  | `e63452022211`  |
| 452    | No file  | `e63452022211`  |
| 449    | No file  | `e63452022211`  |
| 435    | No file  | `e63452022211`  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                      |
| ---------------------------------- | -------- | --------------------------------------------------------- |
| `employeespawnpositionoffset.dbss` | Required | `spawn_position_key -> (offset, size)` of every row       |
| `employeespawninfo.dbss`           | Optional | Sailors that list each spawn position, for the Sailors column |
| `employeespawninfooffset.dbss`     | Optional | Offset table of `employeespawninfo.dbss`                  |
| `languagedata_en.loc`              | Optional | Region names (LOC type 17, `str_id1` = `region_key`), sailor names and titles (type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                      | Field | Notes                                    |
| ------- | ------------------------- | ----- | ---------------------------------------- |
| `+0x00` | u32                       | count | Number of spawn positions (observed: 15) |
| `+0x04` | Spawn Position Row[count] | rows  | See Spawn Position Row                   |

The rows fill the file exactly: 4 + 15 x 34 = 514 bytes on client 3458.

### Spawn Position Row (34 bytes)

| Offset  | Type | Field              | Notes                                                                                    |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------------------------- |
| `+0x00` | u32  | spawn_position_key | Row key; `1` to `5` in Velia, `41` to `45` in Port Epheria, `46` to `50` in Iliya Island |
| `+0x04` | f32  | pos_x              | World X                                                                                  |
| `+0x08` | f32  | pos_y              | World Y (height)                                                                         |
| `+0x0C` | f32  | pos_z              | World Z                                                                                  |
| `+0x10` | f32  | dir_x              | Facing direction, X part                                                                 |
| `+0x14` | f32  | dir_y              | Facing direction, Y part; always `0`                                                     |
| `+0x18` | f32  | dir_z              | Facing direction, Z part                                                                 |
| `+0x1C` | f32  | unknown_1c         | Always `5000.0`; see Open Questions                                                      |
| `+0x20` | u16  | region_key         | Region the spot lies in, LOC type 17: `5` Velia, `120` Port Epheria, `182` Iliya Island  |

`(dir_x, dir_y, dir_z)` is a unit vector in the horizontal plane on every row (`dir_x² + dir_z² = 1`, every angle a multiple of 5 degrees, such as `(-0.7071, 0, 0.7071)` and `(0.1736, 0, 0.9848)`), so it reads as the way the sailor faces. The positions are world coordinates in centimetres, like `teleport.dbss` and the waypoint files. Velia's five spots lie within 12 m of each other, Port Epheria's within 28 m and Iliya Island's within 106 m.

### `employeespawnpositionoffset.dbss`

Bare offset table into `employeespawnposition.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field              | Notes                                                |
| ------- | ---- | ------------------ | ---------------------------------------------------- |
| `+0x00` | u32  | spawn_position_key | Key of the row it points at                          |
| `+0x04` | u32  | data_offset        | Absolute byte offset in `employeespawnposition.dbss` |
| `+0x08` | u32  | data_size          | Always 34                                            |

The rows are in file order, which is not key order (41, 1, 42, 2, 43, 3, 4, 5, 44, 45, 46 to 50). The parser reads the main file through these rows and checks that every row holds the key of the offset row that points at it.

## Notes

- "Employee" in these file names means sailor: the client's sailor windows (`panel_window_sailormanager_all_*.luac`) work on `ToClient_getEmployeeWrapperByIndex`, `getEmployeeKey` and the `__eEmployeeAbility_*` ship stats, and the characters `employeespawninfo.dbss` places here (`59053` to `59072`) are all named Sailor in `characterstatic.dbss` with model `npc/employee_sailor`.
- `employeespawninfo.dbss` rows (one per sailor character, keyed by a u16 character key) hold a sailor key, a u32 count and that many u32 spawn position keys, see [employeespawninfo](employeespawninfo_dbss.md). Examples: character `59061` lists `1` and `41` (Velia and Port Epheria), `59054` lists `46` (Iliya Island only), `59068` lists `44` and `50`. Every key 1 to 5 and 41 to 50 appears there.
- The spawn position keys are their own key space. They overlap employee name IDs in `employeename.dbss` (1 to 60) only by value; nothing links the two.
- The three regions match the towns where sailors can be hired in game: Velia, Port Epheria and Iliya Island.

## Open Questions

### unknown_1c

Every row stores `5000.0` at `+0x1C`. It could be a spawn or interaction radius (5000 cm is 50 m), a respawn delay in milliseconds, or a distance at which the client spawns the sailor. No client Lua string names it, and a constant column cannot be told apart from the data alone. A row with a different value after a patch, or a client function that reads the spawn position table, would settle it.
