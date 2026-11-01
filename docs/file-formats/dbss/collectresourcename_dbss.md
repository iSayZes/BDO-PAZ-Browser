# `collectresourcename.dbss` Format

## Purpose

Gathering models: each record names one world model (a rock, ore vein, tree,
herb or other plant) and the gathering character it stands for, a
`characterstatic.dbss` character with `npc_kind` Collect. Several models map
to one character: on client 3473, 30 models map to Red Coral (`10931`), 23
of them `01_nature/sea/nature_sea_coralreefs_*` and 7 SpeedTree corals
(`bush_seacoral_01`, `weed_seacoral_01` and their variants). The record key is the hash of
the model name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes  | Records         | Row bytes               |
| ------ | -------------- | -------------------------------- | ------ | --------------- | ----------------------- |
| 1      | 1346 and later | `collectresourcename.dbss`       | 52,109 | 1,112 Record    | 30 to 84, 47 on average |
| 1      | 1346 and later | `collectresourcenameoffset.dbss` | 13,348 | 1,112 Index Row | 12                      |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 1      | `collectresourcename.dbss`       | 52,109 B (100.0%) | 0 B (0.0%) |
| 1      | `collectresourcenameoffset.dbss` | 13,348 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `3aa431185231`  |
| 3482   | Layout 1             | `3aa431185231`  |
| 3474   | Layout 1             | `3aa431185231`  |
| 3473   | Layout 1             | `3aa431185231`  |
| 3464   | Layout 1             | `3aa431185231`  |
| 3458   | Layout 1             | `3aa431185231`  |
| 3454   | Layout 1             | `3aa431185231`  |
| 3444   | Layout 1             | `3aa431185231`  |
| 3435   | Layout 1             | `3aa431185231`  |
| 3426   | Layout 1             | `3aa431185231`  |
| 3418   | Layout 1             | `3aa431185231`  |
| 3412   | Layout 1             | `3aa431185231`  |
| 3402   | Layout 1             | `3aa431185231`  |
| 3396   | Layout 1             | `3aa431185231`  |
| 3387   | Layout 1             | `3aa431185231`  |
| 3381   | Layout 1             | `3aa431185231`  |
| 3373   | Layout 1             | `3aa431185231`  |
| 3364   | Layout 1             | `3aa431185231`  |
| 3356   | Layout 1             | `3aa431185231`  |
| 3349   | Layout 1             | `3aa431185231`  |
| 3342   | Layout 1             | `3aa431185231`  |
| 3335   | Layout 1             | `3aa431185231`  |
| 3326   | Layout 1             | `3aa431185231`  |
| 3321   | Layout 1             | `3aa431185231`  |
| 3314   | Layout 1             | `3aa431185231`  |
| 3303   | Layout 1             | `3aa431185231`  |
| 3302   | Layout 1             | `3aa431185231`  |
| 3293   | Layout 1             | `3aa431185231`  |
| 3283   | Layout 1             | `3aa431185231`  |
| 3275   | Layout 1             | `3aa431185231`  |
| 3267   | Layout 1             | `3aa431185231`  |
| 3258   | Layout 1             | `3aa431185231`  |
| 3251   | Layout 1             | `3aa431185231`  |
| 3242   | Layout 1             | `3aa431185231`  |
| 3235   | Layout 1             | `3aa431185231`  |
| 3229   | Layout 1             | `3aa431185231`  |
| 3212   | Layout 1             | `3aa431185231`  |
| 3203   | Layout 1             | `3aa431185231`  |
| 3193   | Layout 1             | `3aa431185231`  |
| 3186   | Layout 1             | `3aa431185231`  |
| 3177   | Layout 1             | `3aa431185231`  |
| 3169   | Layout 1             | `3aa431185231`  |
| 3158   | Layout 1             | `3aa431185231`  |
| 3151   | Layout 1             | `3aa431185231`  |
| 3144   | Layout 1             | `3aa431185231`  |
| 3133   | Layout 1             | `3aa431185231`  |
| 3125   | Layout 1             | `3aa431185231`  |
| 3118   | Layout 1             | `3aa431185231`  |
| 3111   | Layout 1             | `3aa431185231`  |
| 3103   | Layout 1             | `3aa431185231`  |
| 3095   | Layout 1             | `3aa431185231`  |
| 3086   | Layout 1             | `3aa431185231`  |
| 3072   | Layout 1             | `3aa431185231`  |
| 3062   | Layout 1             | `3aa431185231`  |
| 3052   | Layout 1             | `3aa431185231`  |
| 3045   | Layout 1             | `3aa431185231`  |
| 3037   | Layout 1             | `3aa431185231`  |
| 3030   | Layout 1             | `3aa431185231`  |
| 3021   | Layout 1             | `3aa431185231`  |
| 3012   | Layout 1             | `3aa431185231`  |
| 3002   | Layout 1             | `3aa431185231`  |
| 2995   | Layout 1             | `3aa431185231`  |
| 2987   | Layout 1             | `3aa431185231`  |
| 2978   | Layout 1             | `3aa431185231`  |
| 2970   | Layout 1             | `3aa431185231`  |
| 2959   | Layout 1             | `3aa431185231`  |
| 2951   | Layout 1             | `3aa431185231`  |
| 2942   | Layout 1             | `3aa431185231`  |
| 2935   | Layout 1             | `3aa431185231`  |
| 2932   | Layout 1             | `3aa431185231`  |
| 2923   | Layout 1             | `3aa431185231`  |
| 2919   | Layout 1             | `3aa431185231`  |
| 2907   | Layout 1             | `3aa431185231`  |
| 2900   | Layout 1             | `3aa431185231`  |
| 2891   | Layout 1             | `3aa431185231`  |
| 2882   | Layout 1             | `3aa431185231`  |
| 2872   | Layout 1             | `3aa431185231`  |
| 2863   | Layout 1             | `3aa431185231`  |
| 2855   | Layout 1             | `3aa431185231`  |
| 2849   | Layout 1             | `3aa431185231`  |
| 2844   | Layout 1             | `3aa431185231`  |
| 2834   | Layout 1             | `3aa431185231`  |
| 2825   | Layout 1             | `3aa431185231`  |
| 2819   | Layout 1             | `3aa431185231`  |
| 2811   | Layout 1             | `3aa431185231`  |
| 2803   | Layout 1             | `3aa431185231`  |
| 2794   | Layout 1             | `3aa431185231`  |
| 2783   | Layout 1             | `3aa431185231`  |
| 2774   | Layout 1             | `3aa431185231`  |
| 2765   | Layout 1             | `3aa431185231`  |
| 2756   | Layout 1             | `3aa431185231`  |
| 2750   | Layout 1             | `3aa431185231`  |
| 2743   | Layout 1             | `3aa431185231`  |
| 2736   | Layout 1             | `3aa431185231`  |
| 2726   | Layout 1             | `3aa431185231`  |
| 2717   | Layout 1             | `3aa431185231`  |
| 2709   | Layout 1             | `3aa431185231`  |
| 2703   | Layout 1             | `3aa431185231`  |
| 2695   | Layout 1             | `3aa431185231`  |
| 2684   | Layout 1             | `3aa431185231`  |
| 2672   | Layout 1             | `3aa431185231`  |
| 2665   | Layout 1             | `3aa431185231`  |
| 2657   | Layout 1             | `3aa431185231`  |
| 2649   | Layout 1             | `3aa431185231`  |
| 2644   | Layout 1             | `3aa431185231`  |
| 2637   | Layout 1             | `3aa431185231`  |
| 2629   | Layout 1             | `3aa431185231`  |
| 2619   | Layout 1             | `3aa431185231`  |
| 2612   | Layout 1             | `3aa431185231`  |
| 2606   | Layout 1             | `3aa431185231`  |
| 2602   | Layout 1             | `3aa431185231`  |
| 2601   | Layout 1             | `3aa431185231`  |
| 2592   | Layout 1             | `3aa431185231`  |
| 2583   | Layout 1             | `3aa431185231`  |
| 2575   | Layout 1             | `3aa431185231`  |
| 2567   | Layout 1             | `3aa431185231`  |
| 2560   | Layout 1             | `3aa431185231`  |
| 2553   | Layout 1             | `3aa431185231`  |
| 2545   | Layout 1             | `3aa431185231`  |
| 2538   | Layout 1             | `3aa431185231`  |
| 2529   | Layout 1             | `3aa431185231`  |
| 2519   | Layout 1             | `3aa431185231`  |
| 2513   | Layout 1             | `3aa431185231`  |
| 2510   | Layout 1             | `3aa431185231`  |
| 2507   | Layout 1             | `3aa431185231`  |
| 2503   | Layout 1             | `3aa431185231`  |
| 2498   | Layout 1             | `3aa431185231`  |
| 2492   | Layout 1             | `3aa431185231`  |
| 2487   | Layout 1             | `3aa431185231`  |
| 2480   | Layout 1             | `3aa431185231`  |
| 2474   | Layout 1             | `3aa431185231`  |
| 2468   | Layout 1             | `3aa431185231`  |
| 2460   | Layout 1             | `3aa431185231`  |
| 2453   | Layout 1             | `3aa431185231`  |
| 2444   | Layout 1             | `3aa431185231`  |
| 2438   | Layout 1             | `3aa431185231`  |
| 2434   | Layout 1             | `3aa431185231`  |
| 2429   | Layout 1             | `3aa431185231`  |
| 2421   | Layout 1             | `3aa431185231`  |
| 2414   | Layout 1             | `3aa431185231`  |
| 2407   | Layout 1             | `3aa431185231`  |
| 2401   | Layout 1             | `3aa431185231`  |
| 2397   | Layout 1             | `3aa431185231`  |
| 2393   | Layout 1             | `3aa431185231`  |
| 2384   | Layout 1             | `3aa431185231`  |
| 2378   | Layout 1             | `3aa431185231`  |
| 2372   | Layout 1             | `3aa431185231`  |
| 2358   | Layout 1             | `3aa431185231`  |
| 2352   | Layout 1             | `3aa431185231`  |
| 2347   | Layout 1             | `3aa431185231`  |
| 2343   | Layout 1             | `3aa431185231`  |
| 2335   | Layout 1             | `3aa431185231`  |
| 2327   | Layout 1             | `3aa431185231`  |
| 2324   | Layout 1             | `3aa431185231`  |
| 2319   | Layout 1             | `3aa431185231`  |
| 2313   | Layout 1             | `3aa431185231`  |
| 2308   | Layout 1             | `3aa431185231`  |
| 2302   | Layout 1             | `3aa431185231`  |
| 2295   | Layout 1             | `3aa431185231`  |
| 2290   | Layout 1             | `3aa431185231`  |
| 2284   | Layout 1             | `3aa431185231`  |
| 2276   | Layout 1             | `3aa431185231`  |
| 2269   | Layout 1             | `3aa431185231`  |
| 2259   | Layout 1             | `3aa431185231`  |
| 2250   | Layout 1             | `3aa431185231`  |
| 2243   | Layout 1             | `3aa431185231`  |
| 2235   | Layout 1             | `3aa431185231`  |
| 2229   | Layout 1             | `3aa431185231`  |
| 2224   | Layout 1             | `3aa431185231`  |
| 2218   | Layout 1             | `3aa431185231`  |
| 2215   | Layout 1             | `3aa431185231`  |
| 2207   | Layout 1             | `3aa431185231`  |
| 2203   | Layout 1             | `3aa431185231`  |
| 2196   | Layout 1             | `3aa431185231`  |
| 2192   | Layout 1             | `3aa431185231`  |
| 2189   | Layout 1             | `3aa431185231`  |
| 2183   | Layout 1             | `3aa431185231`  |
| 2179   | Layout 1             | `3aa431185231`  |
| 2171   | Layout 1             | `3aa431185231`  |
| 2163   | Layout 1             | `3aa431185231`  |
| 2156   | Layout 1             | `3aa431185231`  |
| 2151   | Layout 1             | `3aa431185231`  |
| 2147   | Layout 1             | `3aa431185231`  |
| 2142   | Layout 1             | `3aa431185231`  |
| 2138   | Layout 1             | `3aa431185231`  |
| 2134   | Layout 1             | `3aa431185231`  |
| 2130   | Layout 1             | `3aa431185231`  |
| 2122   | Layout 1             | `3aa431185231`  |
| 2107   | Layout 1             | `3aa431185231`  |
| 2098   | Layout 1             | `3aa431185231`  |
| 2089   | Layout 1             | `3aa431185231`  |
| 2081   | Layout 1             | `3aa431185231`  |
| 2073   | Layout 1             | `3aa431185231`  |
| 2067   | Layout 1             | `3aa431185231`  |
| 2063   | Layout 1             | `3aa431185231`  |
| 2059   | Layout 1             | `3aa431185231`  |
| 2052   | Layout 1             | `3aa431185231`  |
| 2044   | Layout 1             | `3aa431185231`  |
| 2039   | Layout 1             | `3aa431185231`  |
| 2032   | Layout 1             | `3aa431185231`  |
| 2025   | Layout 1             | `3aa431185231`  |
| 2011   | Layout 1             | `3aa431185231`  |
| 2005   | Layout 1             | `3aa431185231`  |
| 2000   | Layout 1             | `3aa431185231`  |
| 1996   | Layout 1             | `3aa431185231`  |
| 1991   | Layout 1             | `3aa431185231`  |
| 1985   | Layout 1             | `3aa431185231`  |
| 1980   | Layout 1             | `3aa431185231`  |
| 1969   | Layout 1             | `3aa431185231`  |
| 1964   | Layout 1             | `3aa431185231`  |
| 1958   | Layout 1             | `3aa431185231`  |
| 1950   | Layout 1             | `3aa431185231`  |
| 1945   | Layout 1             | `3aa431185231`  |
| 1937   | Layout 1             | `3aa431185231`  |
| 1933   | Layout 1             | `3aa431185231`  |
| 1927   | Layout 1             | `3aa431185231`  |
| 1921   | Layout 1             | `3aa431185231`  |
| 1914   | Layout 1             | `3aa431185231`  |
| 1908   | Layout 1             | `3aa431185231`  |
| 1897   | Layout 1             | `3aa431185231`  |
| 1892   | Layout 1             | `3aa431185231`  |
| 1886   | Layout 1             | `3aa431185231`  |
| 1881   | Layout 1             | `3aa431185231`  |
| 1871   | Layout 1             | `3aa431185231`  |
| 1866   | Layout 1             | `3aa431185231`  |
| 1862   | Layout 1             | `3aa431185231`  |
| 1854   | Layout 1             | `3aa431185231`  |
| 1846   | Layout 1             | `3aa431185231`  |
| 1838   | Layout 1             | `3aa431185231`  |
| 1832   | Layout 1             | `3aa431185231`  |
| 1826   | Layout 1             | `3aa431185231`  |
| 1822   | Layout 1             | `3aa431185231`  |
| 1818   | Layout 1             | `3aa431185231`  |
| 1804   | Layout 1             | `3aa431185231`  |
| 1794   | Layout 1             | `3aa431185231`  |
| 1790   | Layout 1             | `3aa431185231`  |
| 1784   | Layout 1             | `3aa431185231`  |
| 1774   | Layout 1             | `3aa431185231`  |
| 1771   | Layout 1             | `3aa431185231`  |
| 1762   | Layout 1             | `3aa431185231`  |
| 1759   | Layout 1             | `3aa431185231`  |
| 1754   | Layout 1             | `3aa431185231`  |
| 1749   | Layout 1             | `3aa431185231`  |
| 1743   | Layout 1             | `3aa431185231`  |
| 1737   | Layout 1             | `3aa431185231`  |
| 1731   | Layout 1             | `3aa431185231`  |
| 1725   | Layout 1             | `3aa431185231`  |
| 1717   | Layout 1             | `3aa431185231`  |
| 1710   | Layout 1             | `3aa431185231`  |
| 1704   | Layout 1             | `3aa431185231`  |
| 1698   | Layout 1             | `3aa431185231`  |
| 1690   | Layout 1             | `3aa431185231`  |
| 1685   | Layout 1             | `3aa431185231`  |
| 1680   | Layout 1             | `3aa431185231`  |
| 1674   | Layout 1             | `3aa431185231`  |
| 1668   | Layout 1             | `3aa431185231`  |
| 1659   | Layout 1             | `3aa431185231`  |
| 1649   | Layout 1             | `3aa431185231`  |
| 1642   | Layout 1             | `3aa431185231`  |
| 1636   | Layout 1             | `3aa431185231`  |
| 1628   | Layout 1             | `3aa431185231`  |
| 1622   | Layout 1             | `3aa431185231`  |
| 1614   | Layout 1             | `3aa431185231`  |
| 1608   | Layout 1             | `3aa431185231`  |
| 1602   | Layout 1             | `3aa431185231`  |
| 1598   | Layout 1             | `3aa431185231`  |
| 1594   | Layout 1             | `3aa431185231`  |
| 1590   | Layout 1             | `3aa431185231`  |
| 1587   | Layout 1             | `3aa431185231`  |
| 1584   | Layout 1             | `3aa431185231`  |
| 1579   | Layout 1             | `3aa431185231`  |
| 1572   | Layout 1             | `3aa431185231`  |
| 1565   | Layout 1             | `3aa431185231`  |
| 1559   | Layout 1             | `3aa431185231`  |
| 1554   | Layout 1             | `3aa431185231`  |
| 1547   | Layout 1             | `3aa431185231`  |
| 1537   | Layout 1             | `3aa431185231`  |
| 1529   | Layout 1             | `3aa431185231`  |
| 1524   | Layout 1             | `3aa431185231`  |
| 1519   | Layout 1             | `3aa431185231`  |
| 1509   | Layout 1             | `3aa431185231`  |
| 1506   | Layout 1             | `3aa431185231`  |
| 1504   | Layout 1             | `3aa431185231`  |
| 1500   | Layout 1             | `3aa431185231`  |
| 1493   | Layout 1             | `3aa431185231`  |
| 1489   | Layout 1             | `3aa431185231`  |
| 1485   | Layout 1             | `3aa431185231`  |
| 1481   | Layout 1             | `3aa431185231`  |
| 1474   | Layout 1             | `3aa431185231`  |
| 1466   | Layout 1             | `3aa431185231`  |
| 1462   | Layout 1             | `3aa431185231`  |
| 1459   | Layout 1             | `3aa431185231`  |
| 1453   | Layout 1             | `3aa431185231`  |
| 1450   | Layout 1             | `3aa431185231`  |
| 1445   | Layout 1             | `3aa431185231`  |
| 1439   | Layout 1             | `3aa431185231`  |
| 1433   | Layout 1             | `3aa431185231`  |
| 1430   | Layout 1             | `3aa431185231`  |
| 1426   | Layout 1             | `3aa431185231`  |
| 1421   | Layout 1             | `3aa431185231`  |
| 1417   | Layout 1             | `3aa431185231`  |
| 1416   | Layout 1             | `3aa431185231`  |
| 1409   | Layout 1             | `3aa431185231`  |
| 1405   | Layout 1             | `3aa431185231`  |
| 1401   | Layout 1             | `3aa431185231`  |
| 1396   | Layout 1             | `3aa431185231`  |
| 1391   | Layout 1             | `3aa431185231`  |
| 1390   | Layout 1             | `3aa431185231`  |
| 1386   | Layout 1             | `3aa431185231`  |
| 1381   | Layout 1             | `3aa431185231`  |
| 1379   | Layout 1             | `3aa431185231`  |
| 1372   | Layout 1             | `3aa431185231`  |
| 1366   | Layout 1             | `3aa431185231`  |
| 1364   | Layout 1             | `3aa431185231`  |
| 1363   | Layout 1             | `3aa431185231`  |
| 1360   | Layout 1             | `3aa431185231`  |
| 1358   | Layout 1             | `3aa431185231`  |
| 1355   | Layout 1             | `3aa431185231`  |
| 1351   | Layout 1             | `3aa431185231`  |
| 1348   | Layout 1             | `3aa431185231`  |
| 1346   | Layout 1             | `3aa431185231`  |
| 1341   | No documented layout | `3aa431185231`  |
| 1340   | No documented layout | `3aa431185231`  |
| 1338   | No documented layout | `3aa431185231`  |
| 1335   | No documented layout | `3aa431185231`  |
| 1333   | No documented layout | `3aa431185231`  |
| 1329   | No documented layout | `3aa431185231`  |
| 1327   | No documented layout | `3aa431185231`  |
| 1324   | No documented layout | `3aa431185231`  |
| 1321   | No documented layout | `3aa431185231`  |
| 1319   | No documented layout | `3aa431185231`  |
| 1318   | No documented layout | `3aa431185231`  |
| 1316   | No documented layout | `3aa431185231`  |
| 1313   | No documented layout | `3aa431185231`  |
| 1311   | No documented layout | `3aa431185231`  |
| 1309   | No documented layout | `3aa431185231`  |
| 1304   | No documented layout | `3aa431185231`  |
| 1292   | No documented layout | `3aa431185231`  |
| 1286   | No documented layout | `3aa431185231`  |
| 1280   | No documented layout | `3aa431185231`  |
| 1276   | No documented layout | `3aa431185231`  |
| 1267   | No documented layout | `3aa431185231`  |
| 1261   | No documented layout | `3aa431185231`  |
| 1256   | No documented layout | `3aa431185231`  |
| 1250   | No file              | `3aa431185231`  |
| 1246   | No file              | `3aa431185231`  |
| 1239   | No file              | `3aa431185231`  |
| 1230   | No file              | `3aa431185231`  |
| 1226   | No file              | `3aa431185231`  |
| 1220   | No file              | `3aa431185231`  |
| 1217   | No file              | `3aa431185231`  |
| 1211   | No file              | `3aa431185231`  |
| 1210   | No file              | `3aa431185231`  |
| 1208   | No file              | `3aa431185231`  |
| 1203   | No file              | `3aa431185231`  |
| 1197   | No file              | `3aa431185231`  |
| 1194   | No file              | `3aa431185231`  |
| 1192   | No file              | `3aa431185231`  |
| 1187   | No file              | `3aa431185231`  |
| 1183   | No file              | `3aa431185231`  |
| 1177   | No file              | `3aa431185231`  |
| 1173   | No file              | `3aa431185231`  |
| 1167   | No file              | `3aa431185231`  |
| 1164   | No file              | `3aa431185231`  |
| 1156   | No file              | `3aa431185231`  |
| 1149   | No file              | `3aa431185231`  |
| 1144   | No file              | `3aa431185231`  |
| 1137   | No file              | `3aa431185231`  |
| 1132   | No file              | `3aa431185231`  |
| 1127   | No file              | `3aa431185231`  |
| 1122   | No file              | `3aa431185231`  |
| 1118   | No file              | `3aa431185231`  |
| 1114   | No file              | `3aa431185231`  |
| 1109   | No file              | `3aa431185231`  |
| 1102   | No file              | `3aa431185231`  |
| 1096   | No file              | `3aa431185231`  |
| 1088   | No file              | `3aa431185231`  |
| 1081   | No file              | `3aa431185231`  |
| 1076   | No file              | `3aa431185231`  |
| 1069   | No file              | `3aa431185231`  |
| 1064   | No file              | `3aa431185231`  |
| 1058   | No file              | `3aa431185231`  |
| 1051   | No file              | `3aa431185231`  |
| 1044   | No file              | `3aa431185231`  |
| 1036   | No file              | `3aa431185231`  |
| 1026   | No file              | `3aa431185231`  |
| 1016   | No file              | `3aa431185231`  |
| 1009   | No file              | `3aa431185231`  |
| 1005   | No file              | `3aa431185231`  |
| 1000   | No file              | `3aa431185231`  |
| 998    | No file              | `3aa431185231`  |
| 990    | No file              | `3aa431185231`  |
| 979    | No file              | `3aa431185231`  |
| 972    | No file              | `3aa431185231`  |
| 963    | No file              | `3aa431185231`  |
| 955    | No file              | `3aa431185231`  |
| 946    | No file              | `3aa431185231`  |
| 938    | No file              | `3aa431185231`  |
| 927    | No file              | `3aa431185231`  |
| 911    | No file              | `3aa431185231`  |
| 904    | No file              | `3aa431185231`  |
| 899    | No file              | `3aa431185231`  |
| 894    | No file              | `3aa431185231`  |
| 885    | No file              | `3aa431185231`  |
| 879    | No file              | `3aa431185231`  |
| 872    | No file              | `3aa431185231`  |
| 864    | No file              | `3aa431185231`  |
| 855    | No file              | `3aa431185231`  |
| 853    | No file              | `3aa431185231`  |
| 845    | No file              | `3aa431185231`  |
| 837    | No file              | `3aa431185231`  |
| 829    | No file              | `3aa431185231`  |
| 822    | No file              | `3aa431185231`  |
| 814    | No file              | `3aa431185231`  |
| 805    | No file              | `3aa431185231`  |
| 794    | No file              | `3aa431185231`  |
| 787    | No file              | `3aa431185231`  |
| 780    | No file              | `3aa431185231`  |
| 771    | No file              | `3aa431185231`  |
| 760    | No file              | `3aa431185231`  |
| 748    | No file              | `3aa431185231`  |
| 741    | No file              | `3aa431185231`  |
| 736    | No file              | `3aa431185231`  |
| 731    | No file              | `3aa431185231`  |
| 723    | No file              | `3aa431185231`  |
| 711    | No file              | `3aa431185231`  |
| 707    | No file              | `3aa431185231`  |
| 697    | No file              | `3aa431185231`  |
| 689    | No file              | `3aa431185231`  |
| 683    | No file              | `3aa431185231`  |
| 678    | No file              | `3aa431185231`  |
| 670    | No file              | `3aa431185231`  |
| 661    | No file              | `3aa431185231`  |
| 656    | No file              | `3aa431185231`  |
| 652    | No file              | `3aa431185231`  |
| 643    | No file              | `3aa431185231`  |
| 637    | No file              | `3aa431185231`  |
| 630    | No file              | `3aa431185231`  |
| 627    | No file              | `3aa431185231`  |
| 621    | No file              | `3aa431185231`  |
| 617    | No file              | `3aa431185231`  |
| 615    | No file              | `3aa431185231`  |
| 606    | No file              | `3aa431185231`  |
| 599    | No file              | `3aa431185231`  |
| 592    | No file              | `3aa431185231`  |
| 586    | No file              | `3aa431185231`  |
| 577    | No file              | `3aa431185231`  |
| 569    | No file              | `3aa431185231`  |
| 561    | No file              | `3aa431185231`  |
| 554    | No file              | `3aa431185231`  |
| 542    | No file              | `3aa431185231`  |
| 532    | No file              | `3aa431185231`  |
| 531    | No file              | `3aa431185231`  |
| 526    | No file              | `3aa431185231`  |
| 521    | No file              | `3aa431185231`  |
| 517    | No file              | `3aa431185231`  |
| 510    | No file              | `3aa431185231`  |
| 508    | No file              | `3aa431185231`  |
| 504    | No file              | `3aa431185231`  |
| 497    | No file              | `3aa431185231`  |
| 491    | No file              | `3aa431185231`  |
| 485    | No file              | `3aa431185231`  |
| 478    | No file              | `3aa431185231`  |
| 472    | No file              | `3aa431185231`  |
| 466    | No file              | `3aa431185231`  |
| 457    | No file              | `3aa431185231`  |
| 452    | No file              | `3aa431185231`  |
| 449    | No file              | `3aa431185231`  |
| 435    | No file              | `3aa431185231`  |

<!-- versions:end -->

## Companion Files

| File                                 | Required | Role                                                                 |
| ------------------------------------ | -------- | -------------------------------------------------------------------- |
| `collectresourcenameoffset.dbss`     | Optional | `name_hash -> (data_offset, data_size)` index, see below; the records can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Character names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                |
| ------- | ------------- | ------- | ---------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `1,112` on client 3473            |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record      |

### Record (variable: 18 bytes + name text)

| Offset                    | Type | Field              | Notes                                                                  |
| ------------------------- | ---- | ------------------ | ---------------------------------------------------------------------- |
| `+0x00`                   | u32  | name_hash          | lookup3 `hashlittle` of the `resource_file_name` bytes with seed `0xC5EDE`; unique per record, the index key |
| `+0x04`                   | u32  | name_hash_dup      | Equal to `name_hash` in every record; the index's `data_offset` points here |
| `+0x08`                   | str8 | resource_file_name | Model name, lower case, no file extension; unique per record           |
| `resource_file_name+0x00` | u16  | character_key      | Gathering character, a `characterstatic.dbss` `character_id`           |

`name_hash` is the same hash `_common/string_hash.py` computes for
`stringtable.bss` keys, run over the ASCII name bytes instead of UTF-16LE:
`weed_seasphere_b_01` hashes to `0xDEA23636`. It matches all 1,112 records
on client 3473 and all 1,017 on client 1784. The records are not sorted by
hash, name or character.

### `collectresourcenameoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `collectresourcename.dbss` count |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row        |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                      |
| ------- | ---- | ----------- | ------------------------------------------ |
| `+0x00` | u32  | name_hash   | Record key                                 |
| `+0x04` | u32  | data_offset | Record start + 4, at `name_hash_dup`       |
| `+0x08` | u32  | data_size   | Record size - 4: `14` + the name length    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3473 every row matches the record walked
from the start of the file.

## Field Names

The record is the `CollectResourceName_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `ResourceFileName` and
`CharacterObjectIndex`. The compiled name is the sheet's `ResourceFileName`
in lower case, trimmed, with its last extension (`.pam`, `.srt`) cut off:
`00_Common/Lamp/Lamp_Stand_FirePot_01.On.pam` is stored as
`00_common/lamp/lamp_stand_firepot_01.on`, and the sheet's
`tree_alaskacedar_short_b_01.srt ` (with a trailing space) as
`tree_alaskacedar_short_b_01`.

| Field              | Column                 | Shared names, same value |
| ------------------ | ---------------------- | ------------------------ |
| resource_file_name | `ResourceFileName`     | 1,017 of 1,017 (client 1784), 1,011 of 1,011 (client 3473) |
| character_key      | `CharacterObjectIndex` | 1,017 of 1,017 (client 1784), 1,011 of 1,011 (client 3473) |

Client 3473 has 101 names the sheet lacks, and 6 of the sheet's names
(`collecting_mushroom_14_c` to `_17`, `08_dri_stone_set01_04`,
`drigan_yeti_jade_04`) are gone.

## Notes

- On client 3473 the 1,112 records name 561 distinct characters. Every one
  is a `characterstatic.dbss` character with `npc_kind` Collect, and every
  one is also the u16 key that starts a row of [`collect.dbss`](collect_dbss.md) (713 rows on
  client 3474). The character's `label_kr` is often one of its
  model names in another case (`Weed_Seasphere_01` for Agar `10369`, whose
  four models are `weed_seasphere_01`, `_02`, `_b_01` and `_c_01`).
- The name has two forms (client 3473). 423 names hold a folder and are a
  model path below `object/` without `.pam`: 394 of them exist as
  `object/<name>.pam`, the other 29 have no file. The 689 names without a
  folder are SpeedTree basenames: 662 exist as `speedtreedata/**/<name>.srt`,
  15 only as a `.pam` basename (`07_dri_stone_set*`, `collecting_oldtree_*`),
  12 have no file.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `collect.dbss` as "gatherable identity and internal
  mesh names; no yields or rates", which fits: the record holds no item,
  rate or position.
