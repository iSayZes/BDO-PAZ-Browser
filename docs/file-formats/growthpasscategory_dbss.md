# `growthpasscategory.dbss` Format

## Purpose

The tabs of the Growth Pass window (`panel_window_growthpass*.luac`): per category a key, a Korean name, an icon texture key and the quest chain its grid holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records                 | Row bytes                        |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------------- | -------------------------------- |
| 2      | 1680 and later | 3483    | `growthpasscategory.dbss`       | 251   | 2 Record Body, 2 Record | 87 to 152, 120 on average        |
| 2      | 1680 and later | 3483    | `growthpasscategoryoffset.dbss` | 28    | 2 Offset Row            | 12                               |
| 1      | 1717 to 2545   | 2545    | `growthpasscategory.dbss`       | 8,409 | 8 Record Body, 8 Record | 1,042 to 1,052, 1,047 on average |
| 1      | 1717 to 2545   | 2545    | `growthpasscategoryoffset.dbss` | 100   | 8 Offset Row            | 12                               |

| Layout | File                            | Known          | Unknown         |
| ------ | ------------------------------- | -------------- | --------------- |
| 2      | `growthpasscategory.dbss`       | 211 B (84.1%)  | 40 B (15.9%)    |
| 2      | `growthpasscategoryoffset.dbss` | 28 B (100.0%)  | 0 B (0.0%)      |
| 1      | `growthpasscategory.dbss`       | 569 B (6.8%)   | 7,840 B (93.2%) |
| 1      | `growthpasscategoryoffset.dbss` | 100 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `baa131892627`  |
| 3482   | Layout 2             | `baa131892627`  |
| 3474   | Layout 2             | `baa131892627`  |
| 3473   | Layout 2             | `baa131892627`  |
| 3464   | Layout 2             | `baa131892627`  |
| 3458   | Layout 2             | `baa131892627`  |
| 3454   | Layout 2             | `baa131892627`  |
| 3444   | Layout 2             | `baa131892627`  |
| 3435   | Layout 2             | `baa131892627`  |
| 3426   | Layout 2             | `baa131892627`  |
| 3418   | Layout 2             | `baa131892627`  |
| 3412   | No documented layout | `baa131892627`  |
| 3402   | No documented layout | `baa131892627`  |
| 3396   | No documented layout | `baa131892627`  |
| 3387   | No documented layout | `baa131892627`  |
| 3381   | No documented layout | `baa131892627`  |
| 3373   | No documented layout | `baa131892627`  |
| 3364   | No documented layout | `baa131892627`  |
| 3356   | No documented layout | `baa131892627`  |
| 3349   | No documented layout | `baa131892627`  |
| 3342   | No documented layout | `baa131892627`  |
| 3335   | No documented layout | `baa131892627`  |
| 3326   | No documented layout | `baa131892627`  |
| 3321   | No documented layout | `baa131892627`  |
| 3314   | No documented layout | `baa131892627`  |
| 3303   | No documented layout | `baa131892627`  |
| 3302   | No documented layout | `baa131892627`  |
| 3293   | No documented layout | `baa131892627`  |
| 3283   | No documented layout | `baa131892627`  |
| 3275   | No documented layout | `baa131892627`  |
| 3267   | No documented layout | `baa131892627`  |
| 3258   | No documented layout | `baa131892627`  |
| 3251   | No documented layout | `baa131892627`  |
| 3242   | No documented layout | `baa131892627`  |
| 3235   | No documented layout | `baa131892627`  |
| 3229   | No documented layout | `baa131892627`  |
| 3212   | No documented layout | `baa131892627`  |
| 3203   | No documented layout | `baa131892627`  |
| 3193   | No documented layout | `baa131892627`  |
| 3186   | No documented layout | `baa131892627`  |
| 3177   | No documented layout | `baa131892627`  |
| 3169   | No documented layout | `baa131892627`  |
| 3158   | No documented layout | `baa131892627`  |
| 3151   | No documented layout | `baa131892627`  |
| 3144   | No documented layout | `baa131892627`  |
| 3133   | No documented layout | `baa131892627`  |
| 3125   | No documented layout | `baa131892627`  |
| 3118   | No documented layout | `baa131892627`  |
| 3111   | No documented layout | `baa131892627`  |
| 3103   | No documented layout | `baa131892627`  |
| 3095   | No documented layout | `baa131892627`  |
| 3086   | No documented layout | `baa131892627`  |
| 3072   | No documented layout | `baa131892627`  |
| 3062   | No documented layout | `baa131892627`  |
| 3052   | No documented layout | `baa131892627`  |
| 3045   | No documented layout | `baa131892627`  |
| 3037   | No documented layout | `baa131892627`  |
| 3030   | No documented layout | `baa131892627`  |
| 3021   | No documented layout | `baa131892627`  |
| 3012   | No documented layout | `baa131892627`  |
| 3002   | No documented layout | `baa131892627`  |
| 2995   | No documented layout | `baa131892627`  |
| 2987   | No documented layout | `baa131892627`  |
| 2978   | No documented layout | `baa131892627`  |
| 2970   | No documented layout | `baa131892627`  |
| 2959   | No documented layout | `baa131892627`  |
| 2951   | No documented layout | `baa131892627`  |
| 2942   | No documented layout | `baa131892627`  |
| 2935   | No documented layout | `baa131892627`  |
| 2932   | No documented layout | `baa131892627`  |
| 2923   | No documented layout | `baa131892627`  |
| 2919   | No documented layout | `baa131892627`  |
| 2907   | No documented layout | `baa131892627`  |
| 2900   | No documented layout | `baa131892627`  |
| 2891   | No documented layout | `baa131892627`  |
| 2882   | No documented layout | `baa131892627`  |
| 2872   | No documented layout | `baa131892627`  |
| 2863   | No documented layout | `baa131892627`  |
| 2855   | No documented layout | `baa131892627`  |
| 2849   | No documented layout | `baa131892627`  |
| 2844   | No documented layout | `baa131892627`  |
| 2834   | No documented layout | `baa131892627`  |
| 2825   | No documented layout | `baa131892627`  |
| 2819   | No documented layout | `baa131892627`  |
| 2811   | No documented layout | `baa131892627`  |
| 2803   | No documented layout | `baa131892627`  |
| 2794   | No documented layout | `baa131892627`  |
| 2783   | No documented layout | `baa131892627`  |
| 2774   | No documented layout | `baa131892627`  |
| 2765   | No documented layout | `baa131892627`  |
| 2756   | No documented layout | `baa131892627`  |
| 2750   | No documented layout | `baa131892627`  |
| 2743   | No documented layout | `baa131892627`  |
| 2736   | No documented layout | `baa131892627`  |
| 2726   | No documented layout | `baa131892627`  |
| 2717   | No documented layout | `baa131892627`  |
| 2709   | No documented layout | `baa131892627`  |
| 2703   | No documented layout | `baa131892627`  |
| 2695   | No documented layout | `baa131892627`  |
| 2684   | No documented layout | `baa131892627`  |
| 2672   | No documented layout | `baa131892627`  |
| 2665   | No documented layout | `baa131892627`  |
| 2657   | No documented layout | `baa131892627`  |
| 2649   | No documented layout | `baa131892627`  |
| 2644   | No documented layout | `baa131892627`  |
| 2637   | No documented layout | `baa131892627`  |
| 2629   | No documented layout | `baa131892627`  |
| 2619   | No documented layout | `baa131892627`  |
| 2612   | No documented layout | `baa131892627`  |
| 2606   | No documented layout | `baa131892627`  |
| 2602   | No documented layout | `baa131892627`  |
| 2601   | No documented layout | `baa131892627`  |
| 2592   | No documented layout | `baa131892627`  |
| 2583   | No documented layout | `baa131892627`  |
| 2575   | No documented layout | `baa131892627`  |
| 2567   | No documented layout | `baa131892627`  |
| 2560   | No documented layout | `baa131892627`  |
| 2553   | No documented layout | `baa131892627`  |
| 2545   | Layout 1             | `baa131892627`  |
| 2538   | Layout 1             | `baa131892627`  |
| 2529   | Layout 1             | `baa131892627`  |
| 2519   | Layout 1             | `baa131892627`  |
| 2513   | Layout 1             | `baa131892627`  |
| 2510   | Layout 1             | `baa131892627`  |
| 2507   | Layout 1             | `baa131892627`  |
| 2503   | Layout 1             | `baa131892627`  |
| 2498   | Layout 1             | `baa131892627`  |
| 2492   | Layout 1             | `baa131892627`  |
| 2487   | Layout 1             | `baa131892627`  |
| 2480   | Layout 1             | `baa131892627`  |
| 2474   | Layout 1             | `baa131892627`  |
| 2468   | Layout 1             | `baa131892627`  |
| 2460   | Layout 1             | `baa131892627`  |
| 2453   | Layout 1             | `baa131892627`  |
| 2444   | Layout 1             | `baa131892627`  |
| 2438   | Layout 1             | `baa131892627`  |
| 2434   | Layout 1             | `baa131892627`  |
| 2429   | Layout 1             | `baa131892627`  |
| 2421   | Layout 1             | `baa131892627`  |
| 2414   | Layout 1             | `baa131892627`  |
| 2407   | Layout 1             | `baa131892627`  |
| 2401   | Layout 1             | `baa131892627`  |
| 2397   | Layout 1             | `baa131892627`  |
| 2393   | Layout 1             | `baa131892627`  |
| 2384   | Layout 1             | `baa131892627`  |
| 2378   | Layout 1             | `baa131892627`  |
| 2372   | Layout 1             | `baa131892627`  |
| 2358   | Layout 1             | `baa131892627`  |
| 2352   | Layout 1             | `baa131892627`  |
| 2347   | Layout 1             | `baa131892627`  |
| 2343   | Layout 1             | `baa131892627`  |
| 2335   | Layout 1             | `baa131892627`  |
| 2327   | Layout 1             | `baa131892627`  |
| 2324   | Layout 1             | `baa131892627`  |
| 2319   | Layout 1             | `baa131892627`  |
| 2313   | Layout 1             | `baa131892627`  |
| 2308   | Layout 1             | `baa131892627`  |
| 2302   | Layout 1             | `baa131892627`  |
| 2295   | Layout 1             | `baa131892627`  |
| 2290   | Layout 1             | `baa131892627`  |
| 2284   | Layout 1             | `baa131892627`  |
| 2276   | Layout 1             | `baa131892627`  |
| 2269   | Layout 1             | `baa131892627`  |
| 2259   | Layout 1             | `baa131892627`  |
| 2250   | Layout 1             | `baa131892627`  |
| 2243   | Layout 1             | `baa131892627`  |
| 2235   | Layout 1             | `baa131892627`  |
| 2229   | Layout 1             | `baa131892627`  |
| 2224   | Layout 1             | `baa131892627`  |
| 2218   | Layout 1             | `baa131892627`  |
| 2215   | Layout 1             | `baa131892627`  |
| 2207   | Layout 1             | `baa131892627`  |
| 2203   | Layout 1             | `baa131892627`  |
| 2196   | Layout 1             | `baa131892627`  |
| 2192   | Layout 1             | `baa131892627`  |
| 2189   | Layout 1             | `baa131892627`  |
| 2183   | Layout 1             | `baa131892627`  |
| 2179   | Layout 1             | `baa131892627`  |
| 2171   | Layout 1             | `baa131892627`  |
| 2163   | Layout 1             | `baa131892627`  |
| 2156   | Layout 1             | `baa131892627`  |
| 2151   | Layout 1             | `baa131892627`  |
| 2147   | Layout 1             | `baa131892627`  |
| 2142   | Layout 1             | `baa131892627`  |
| 2138   | Layout 1             | `baa131892627`  |
| 2134   | Layout 1             | `baa131892627`  |
| 2130   | Layout 1             | `baa131892627`  |
| 2122   | Layout 1             | `baa131892627`  |
| 2107   | Layout 1             | `baa131892627`  |
| 2098   | Layout 1             | `baa131892627`  |
| 2089   | Layout 1             | `baa131892627`  |
| 2081   | Layout 1             | `baa131892627`  |
| 2073   | Layout 1             | `baa131892627`  |
| 2067   | Layout 1             | `baa131892627`  |
| 2063   | Layout 1             | `baa131892627`  |
| 2059   | Layout 1             | `baa131892627`  |
| 2052   | Layout 1             | `baa131892627`  |
| 2044   | Layout 1             | `baa131892627`  |
| 2039   | Layout 1             | `baa131892627`  |
| 2032   | Layout 1             | `baa131892627`  |
| 2025   | Layout 1             | `baa131892627`  |
| 2011   | Layout 1             | `baa131892627`  |
| 2005   | Layout 1             | `baa131892627`  |
| 2000   | Layout 1             | `baa131892627`  |
| 1996   | Layout 1             | `baa131892627`  |
| 1991   | Layout 1             | `baa131892627`  |
| 1985   | Layout 1             | `baa131892627`  |
| 1980   | Layout 1             | `baa131892627`  |
| 1969   | Layout 1             | `baa131892627`  |
| 1964   | Layout 1             | `baa131892627`  |
| 1958   | Layout 1             | `baa131892627`  |
| 1950   | Layout 1             | `baa131892627`  |
| 1945   | Layout 1             | `baa131892627`  |
| 1937   | Layout 1             | `baa131892627`  |
| 1933   | Layout 1             | `baa131892627`  |
| 1927   | Layout 1             | `baa131892627`  |
| 1921   | Layout 1             | `baa131892627`  |
| 1914   | Layout 1             | `baa131892627`  |
| 1908   | Layout 1             | `baa131892627`  |
| 1897   | Layout 1             | `baa131892627`  |
| 1892   | Layout 1             | `baa131892627`  |
| 1886   | Layout 1             | `baa131892627`  |
| 1881   | Layout 1             | `baa131892627`  |
| 1871   | Layout 1             | `baa131892627`  |
| 1866   | Layout 1             | `baa131892627`  |
| 1862   | Layout 1             | `baa131892627`  |
| 1854   | Layout 1             | `baa131892627`  |
| 1846   | Layout 1             | `baa131892627`  |
| 1838   | Layout 1             | `baa131892627`  |
| 1832   | Layout 1             | `baa131892627`  |
| 1826   | Layout 1             | `baa131892627`  |
| 1822   | Layout 1             | `baa131892627`  |
| 1818   | Layout 1             | `baa131892627`  |
| 1804   | Layout 1             | `baa131892627`  |
| 1794   | Layout 1             | `baa131892627`  |
| 1790   | Layout 1             | `baa131892627`  |
| 1784   | Layout 1             | `baa131892627`  |
| 1774   | Layout 1             | `baa131892627`  |
| 1771   | Layout 1             | `baa131892627`  |
| 1762   | Layout 1             | `baa131892627`  |
| 1759   | Layout 1             | `baa131892627`  |
| 1754   | Layout 1             | `baa131892627`  |
| 1749   | Layout 1             | `baa131892627`  |
| 1743   | Layout 1             | `baa131892627`  |
| 1737   | Layout 1             | `baa131892627`  |
| 1731   | Layout 1             | `baa131892627`  |
| 1725   | Layout 1             | `baa131892627`  |
| 1717   | Layout 1             | `baa131892627`  |
| 1710   | No file              | `baa131892627`  |
| 1704   | No file              | `baa131892627`  |
| 1698   | Layout 2             | `baa131892627`  |
| 1690   | Layout 2             | `baa131892627`  |
| 1685   | Layout 2             | `baa131892627`  |
| 1680   | Layout 2             | `baa131892627`  |
| 1674   | No file              | `baa131892627`  |
| 1668   | No file              | `baa131892627`  |
| 1659   | No file              | `baa131892627`  |
| 1649   | No file              | `baa131892627`  |
| 1642   | No file              | `baa131892627`  |
| 1636   | No file              | `baa131892627`  |
| 1628   | No file              | `baa131892627`  |
| 1622   | No file              | `baa131892627`  |
| 1614   | No file              | `baa131892627`  |
| 1608   | No file              | `baa131892627`  |
| 1602   | No file              | `baa131892627`  |
| 1598   | No file              | `baa131892627`  |
| 1594   | No file              | `baa131892627`  |
| 1590   | No file              | `baa131892627`  |
| 1587   | No file              | `baa131892627`  |
| 1584   | No file              | `baa131892627`  |
| 1579   | No file              | `baa131892627`  |
| 1572   | No file              | `baa131892627`  |
| 1565   | No file              | `baa131892627`  |
| 1559   | No file              | `baa131892627`  |
| 1554   | No file              | `baa131892627`  |
| 1547   | No file              | `baa131892627`  |
| 1537   | No file              | `baa131892627`  |
| 1529   | No file              | `baa131892627`  |
| 1524   | No file              | `baa131892627`  |
| 1519   | No file              | `baa131892627`  |
| 1509   | No file              | `baa131892627`  |
| 1506   | No file              | `baa131892627`  |
| 1504   | No file              | `baa131892627`  |
| 1500   | No file              | `baa131892627`  |
| 1493   | No file              | `baa131892627`  |
| 1489   | No file              | `baa131892627`  |
| 1485   | No file              | `baa131892627`  |
| 1481   | No file              | `baa131892627`  |
| 1474   | No file              | `baa131892627`  |
| 1466   | No file              | `baa131892627`  |
| 1462   | No file              | `baa131892627`  |
| 1459   | No file              | `baa131892627`  |
| 1453   | No file              | `baa131892627`  |
| 1450   | No file              | `baa131892627`  |
| 1445   | No file              | `baa131892627`  |
| 1439   | No file              | `baa131892627`  |
| 1433   | No file              | `baa131892627`  |
| 1430   | No file              | `baa131892627`  |
| 1426   | No file              | `baa131892627`  |
| 1421   | No file              | `baa131892627`  |
| 1417   | No file              | `baa131892627`  |
| 1416   | No file              | `baa131892627`  |
| 1409   | No file              | `baa131892627`  |
| 1405   | No file              | `baa131892627`  |
| 1401   | No file              | `baa131892627`  |
| 1396   | No file              | `baa131892627`  |
| 1391   | No file              | `baa131892627`  |
| 1390   | No file              | `baa131892627`  |
| 1386   | No file              | `baa131892627`  |
| 1381   | No file              | `baa131892627`  |
| 1379   | No file              | `baa131892627`  |
| 1372   | No file              | `baa131892627`  |
| 1366   | No file              | `baa131892627`  |
| 1364   | No file              | `baa131892627`  |
| 1363   | No file              | `baa131892627`  |
| 1360   | No file              | `baa131892627`  |
| 1358   | No file              | `baa131892627`  |
| 1355   | No file              | `baa131892627`  |
| 1351   | No file              | `baa131892627`  |
| 1348   | No file              | `baa131892627`  |
| 1346   | No file              | `baa131892627`  |
| 1341   | No file              | `baa131892627`  |
| 1340   | No file              | `baa131892627`  |
| 1338   | No file              | `baa131892627`  |
| 1335   | No file              | `baa131892627`  |
| 1333   | No file              | `baa131892627`  |
| 1329   | No file              | `baa131892627`  |
| 1327   | No file              | `baa131892627`  |
| 1324   | No file              | `baa131892627`  |
| 1321   | No file              | `baa131892627`  |
| 1319   | No file              | `baa131892627`  |
| 1318   | No file              | `baa131892627`  |
| 1316   | No file              | `baa131892627`  |
| 1313   | No file              | `baa131892627`  |
| 1311   | No file              | `baa131892627`  |
| 1309   | No file              | `baa131892627`  |
| 1304   | No file              | `baa131892627`  |
| 1292   | No file              | `baa131892627`  |
| 1286   | No file              | `baa131892627`  |
| 1280   | No file              | `baa131892627`  |
| 1276   | No file              | `baa131892627`  |
| 1267   | No file              | `baa131892627`  |
| 1261   | No file              | `baa131892627`  |
| 1256   | No file              | `baa131892627`  |
| 1250   | No file              | `baa131892627`  |
| 1246   | No file              | `baa131892627`  |
| 1239   | No file              | `baa131892627`  |
| 1230   | No file              | `baa131892627`  |
| 1226   | No file              | `baa131892627`  |
| 1220   | No file              | `baa131892627`  |
| 1217   | No file              | `baa131892627`  |
| 1211   | No file              | `baa131892627`  |
| 1210   | No file              | `baa131892627`  |
| 1208   | No file              | `baa131892627`  |
| 1203   | No file              | `baa131892627`  |
| 1197   | No file              | `baa131892627`  |
| 1194   | No file              | `baa131892627`  |
| 1192   | No file              | `baa131892627`  |
| 1187   | No file              | `baa131892627`  |
| 1183   | No file              | `baa131892627`  |
| 1177   | No file              | `baa131892627`  |
| 1173   | No file              | `baa131892627`  |
| 1167   | No file              | `baa131892627`  |
| 1164   | No file              | `baa131892627`  |
| 1156   | No file              | `baa131892627`  |
| 1149   | No file              | `baa131892627`  |
| 1144   | No file              | `baa131892627`  |
| 1137   | No file              | `baa131892627`  |
| 1132   | No file              | `baa131892627`  |
| 1127   | No file              | `baa131892627`  |
| 1122   | No file              | `baa131892627`  |
| 1118   | No file              | `baa131892627`  |
| 1114   | No file              | `baa131892627`  |
| 1109   | No file              | `baa131892627`  |
| 1102   | No file              | `baa131892627`  |
| 1096   | No file              | `baa131892627`  |
| 1088   | No file              | `baa131892627`  |
| 1081   | No file              | `baa131892627`  |
| 1076   | No file              | `baa131892627`  |
| 1069   | No file              | `baa131892627`  |
| 1064   | No file              | `baa131892627`  |
| 1058   | No file              | `baa131892627`  |
| 1051   | No file              | `baa131892627`  |
| 1044   | No file              | `baa131892627`  |
| 1036   | No file              | `baa131892627`  |
| 1026   | No file              | `baa131892627`  |
| 1016   | No file              | `baa131892627`  |
| 1009   | No file              | `baa131892627`  |
| 1005   | No file              | `baa131892627`  |
| 1000   | No file              | `baa131892627`  |
| 998    | No file              | `baa131892627`  |
| 990    | No file              | `baa131892627`  |
| 979    | No file              | `baa131892627`  |
| 972    | No file              | `baa131892627`  |
| 963    | No file              | `baa131892627`  |
| 955    | No file              | `baa131892627`  |
| 946    | No file              | `baa131892627`  |
| 938    | No file              | `baa131892627`  |
| 927    | No file              | `baa131892627`  |
| 911    | No file              | `baa131892627`  |
| 904    | No file              | `baa131892627`  |
| 899    | No file              | `baa131892627`  |
| 894    | No file              | `baa131892627`  |
| 885    | No file              | `baa131892627`  |
| 879    | No file              | `baa131892627`  |
| 872    | No file              | `baa131892627`  |
| 864    | No file              | `baa131892627`  |
| 855    | No file              | `baa131892627`  |
| 853    | No file              | `baa131892627`  |
| 845    | No file              | `baa131892627`  |
| 837    | No file              | `baa131892627`  |
| 829    | No file              | `baa131892627`  |
| 822    | No file              | `baa131892627`  |
| 814    | No file              | `baa131892627`  |
| 805    | No file              | `baa131892627`  |
| 794    | No file              | `baa131892627`  |
| 787    | No file              | `baa131892627`  |
| 780    | No file              | `baa131892627`  |
| 771    | No file              | `baa131892627`  |
| 760    | No file              | `baa131892627`  |
| 748    | No file              | `baa131892627`  |
| 741    | No file              | `baa131892627`  |
| 736    | No file              | `baa131892627`  |
| 731    | No file              | `baa131892627`  |
| 723    | No file              | `baa131892627`  |
| 711    | No file              | `baa131892627`  |
| 707    | No file              | `baa131892627`  |
| 697    | No file              | `baa131892627`  |
| 689    | No file              | `baa131892627`  |
| 683    | No file              | `baa131892627`  |
| 678    | No file              | `baa131892627`  |
| 670    | No file              | `baa131892627`  |
| 661    | No file              | `baa131892627`  |
| 656    | No file              | `baa131892627`  |
| 652    | No file              | `baa131892627`  |
| 643    | No file              | `baa131892627`  |
| 637    | No file              | `baa131892627`  |
| 630    | No file              | `baa131892627`  |
| 627    | No file              | `baa131892627`  |
| 621    | No file              | `baa131892627`  |
| 617    | No file              | `baa131892627`  |
| 615    | No file              | `baa131892627`  |
| 606    | No file              | `baa131892627`  |
| 599    | No file              | `baa131892627`  |
| 592    | No file              | `baa131892627`  |
| 586    | No file              | `baa131892627`  |
| 577    | No file              | `baa131892627`  |
| 569    | No file              | `baa131892627`  |
| 561    | No file              | `baa131892627`  |
| 554    | No file              | `baa131892627`  |
| 542    | No file              | `baa131892627`  |
| 532    | No file              | `baa131892627`  |
| 531    | No file              | `baa131892627`  |
| 526    | No file              | `baa131892627`  |
| 521    | No file              | `baa131892627`  |
| 517    | No file              | `baa131892627`  |
| 510    | No file              | `baa131892627`  |
| 508    | No file              | `baa131892627`  |
| 504    | No file              | `baa131892627`  |
| 497    | No file              | `baa131892627`  |
| 491    | No file              | `baa131892627`  |
| 485    | No file              | `baa131892627`  |
| 478    | No file              | `baa131892627`  |
| 472    | No file              | `baa131892627`  |
| 466    | No file              | `baa131892627`  |
| 457    | No file              | `baa131892627`  |
| 452    | No file              | `baa131892627`  |
| 449    | No file              | `baa131892627`  |
| 435    | No file              | `baa131892627`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                             |
| ------------------------------- | -------- | ---------------------------------------------------------------- |
| `growthpasscategoryoffset.dbss` | Required | `category_key -> (offset, size)` of each record body             |
| `texturestring_combine.xml`     | Optional | Sprite sheet and rectangle of `icon_texture`                     |
| `languagedata_en.loc`           | Optional | Category name, LOC type 107 `str_id1 = category_key`             |

The grid of each category is in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), keyed by the same `category_key`.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type                 | Field        | Notes              |
| ------- | -------------------- | ------------ | ------------------ |
| `+0x00` | u32                  | record_count | `2` on client 3464 |
| `+0x04` | Record[record_count] | records      | See Record         |

### Record (variable: 4 bytes + body)

| Offset  | Type        | Field | Notes                               |
| ------- | ----------- | ----- | ----------------------------------- |
| `+0x00` | u32         | key   | Copy of the record's key            |
| `+0x04` | Record Body | body  | The offset row points at this field |

### Record Body (variable: 42 bytes + name and icon text)

The offset table points at the body, past the key copy.

| Offset              | Type      | Field           | Notes                                                                |
| ------------------- | --------- | --------------- | -------------------------------------------------------------------- |
| `+0x00`             | u32       | category_key    | Same as the key copy before it and the offset row key                |
| `+0x04`             | str16     | name_kr         | Length in characters, then the text; keeps `<PAColor>` tags          |
| `name_kr+0x00`      | str8      | icon_texture    | Length in bytes, then a `texturestring_combine.xml` texture ID       |
| `icon_texture+0x00` | u16       | quest_chain_id  | The quest chain of this category's grid                              |
| `icon_texture+0x02` | bytes[20] | unknown_tail_02 | Zero on both records                                                 |

Both strings carry a u64 length prefix, read with `RecordReader.text`.

### `growthpasscategoryoffset.dbss`

No `PABR` magic and no trailer: a u32 row count, then rows of u32 `category_key`, u32 `offset`, u32 `size`, read by `parse_bare_u32_offset_rows`. On client 3464: key 7 at `8`, 87 bytes; key 9 at `99`, 152 bytes. Sorted by offset, the key copies and bodies fill the file after the count.

| Offset  | Type                  | Field     | Notes                 |
| ------- | --------------------- | --------- | --------------------- |
| `+0x00` | u32                   | row_count | Number of offset rows |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                              |
| ------- | ---- | ------------ | ---------------------------------- |
| `+0x00` | u32  | category_key | Record key                         |
| `+0x04` | u32  | offset       | Absolute offset of the record body |
| `+0x08` | u32  | size         | Size of the record body            |

## Layout 1

Client 1784 record bodies end in 980 bytes after `quest_chain_id`, where
client 3473 has 20. Only the Record Body differs from Layout 2.

### Record Body (variable: 1002 bytes + name and icon text)

| Offset              | Type       | Field           | Notes                                                                 |
| ------------------- | ---------- | --------------- | --------------------------------------------------------------------- |
| `+0x00`             | u32        | category_key    |                                                                       |
| `+0x04`             | str16      | name_kr         |                                                                       |
| `name_kr+0x00`      | str8       | icon_texture    |                                                                       |
| `icon_texture+0x00` | u16        | quest_chain_id  | 4464 to 4471 on the eight records of client 1784                      |
| `icon_texture+0x02` | bytes[980] | unknown_tail_02 | Starts with u32 `5` on every record of client 1784; mostly zero after |

## Category Keys

`panel_window_growthpass.luac` sets `_hyperBoostCategoryKeyList = {9}`: the window sorts Hyper Boost categories first, then the rest in file order. It reads the name through `categoryWrapper:getCategoryName()` and the icon through `getIconTextureId()`.

LOC type 107 names keys 1 to 9 (`Quest/`, `PvE`, `Gathering`, `Farming/`, `Hunting/`, `Training`, `Game Tips`, `Guaranteed`, `HYPERBOOST`), but only 7 and 9 have a record on client 3464. `growthpassquestlist.bss` holds nine quest chains, 4464 to 4472; on client 3464 only 4470 and 4472 belong to a category.

## Notes

- Decompressed sizes on client 3464: `251` bytes, offset companion `28` bytes.
- calpheonlabs has no page for this table.
- `test_handler.py` checks that the records fill the file and that every icon key resolves; the layout tests check that each grid's quests are the chain its category names.

## Open Questions

### Unknown Tail

The 20 bytes after `quest_chain_id` are zero on both records. `ToClient_requestCategoryRewardItem(categoryKey, rewardIndex)` in `panel_window_growthpass_2.luac` claims a category reward, so a reward list could live here when a category has one; no record shows it.
