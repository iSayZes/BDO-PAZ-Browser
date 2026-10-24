# `lifeactionexperience.dbss` Format

## Purpose

Life skill EXP per item: each row names an item and up to two life skills
with an EXP amount each. On clients 1784 and 3474 every EXP amount is `0`
and every first life skill is `0` (Gathering), so the file holds a list of
items and no working EXP. `lifeactionexperienceoffset.dbss` is the
item-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ------ | ---------------- | --------- |
| 1      | 1346 and later | 3483    | `lifeactionexperience.dbss`       | 79,356 | 3,052 Row        | 26        |
| 1      | 1346 and later | 3483    | `lifeactionexperienceoffset.dbss` | 36,628 | 3,052 Offset Row | 12        |

| Layout | File                              | Known             | Unknown    |
| ------ | --------------------------------- | ----------------- | ---------- |
| 1      | `lifeactionexperience.dbss`       | 79,356 B (100.0%) | 0 B (0.0%) |
| 1      | `lifeactionexperienceoffset.dbss` | 36,628 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `95658854907b`  |
| 3482   | Layout 1             | `95658854907b`  |
| 3474   | Layout 1             | `95658854907b`  |
| 3473   | Layout 1             | `95658854907b`  |
| 3464   | Layout 1             | `95658854907b`  |
| 3458   | Layout 1             | `95658854907b`  |
| 3454   | Layout 1             | `95658854907b`  |
| 3444   | Layout 1             | `95658854907b`  |
| 3435   | Layout 1             | `95658854907b`  |
| 3426   | Layout 1             | `95658854907b`  |
| 3418   | Layout 1             | `95658854907b`  |
| 3412   | Layout 1             | `95658854907b`  |
| 3402   | Layout 1             | `95658854907b`  |
| 3396   | Layout 1             | `95658854907b`  |
| 3387   | Layout 1             | `95658854907b`  |
| 3381   | Layout 1             | `95658854907b`  |
| 3373   | Layout 1             | `95658854907b`  |
| 3364   | Layout 1             | `95658854907b`  |
| 3356   | Layout 1             | `95658854907b`  |
| 3349   | Layout 1             | `95658854907b`  |
| 3342   | Layout 1             | `95658854907b`  |
| 3335   | Layout 1             | `95658854907b`  |
| 3326   | Layout 1             | `95658854907b`  |
| 3321   | Layout 1             | `95658854907b`  |
| 3314   | Layout 1             | `95658854907b`  |
| 3303   | Layout 1             | `95658854907b`  |
| 3302   | Layout 1             | `95658854907b`  |
| 3293   | Layout 1             | `95658854907b`  |
| 3283   | Layout 1             | `95658854907b`  |
| 3275   | Layout 1             | `95658854907b`  |
| 3267   | Layout 1             | `95658854907b`  |
| 3258   | Layout 1             | `95658854907b`  |
| 3251   | Layout 1             | `95658854907b`  |
| 3242   | Layout 1             | `95658854907b`  |
| 3235   | Layout 1             | `95658854907b`  |
| 3229   | Layout 1             | `95658854907b`  |
| 3212   | Layout 1             | `95658854907b`  |
| 3203   | Layout 1             | `95658854907b`  |
| 3193   | Layout 1             | `95658854907b`  |
| 3186   | Layout 1             | `95658854907b`  |
| 3177   | Layout 1             | `95658854907b`  |
| 3169   | Layout 1             | `95658854907b`  |
| 3158   | Layout 1             | `95658854907b`  |
| 3151   | Layout 1             | `95658854907b`  |
| 3144   | Layout 1             | `95658854907b`  |
| 3133   | Layout 1             | `95658854907b`  |
| 3125   | Layout 1             | `95658854907b`  |
| 3118   | Layout 1             | `95658854907b`  |
| 3111   | Layout 1             | `95658854907b`  |
| 3103   | Layout 1             | `95658854907b`  |
| 3095   | Layout 1             | `95658854907b`  |
| 3086   | Layout 1             | `95658854907b`  |
| 3072   | Layout 1             | `95658854907b`  |
| 3062   | Layout 1             | `95658854907b`  |
| 3052   | Layout 1             | `95658854907b`  |
| 3045   | Layout 1             | `95658854907b`  |
| 3037   | Layout 1             | `95658854907b`  |
| 3030   | Layout 1             | `95658854907b`  |
| 3021   | Layout 1             | `95658854907b`  |
| 3012   | Layout 1             | `95658854907b`  |
| 3002   | Layout 1             | `95658854907b`  |
| 2995   | Layout 1             | `95658854907b`  |
| 2987   | Layout 1             | `95658854907b`  |
| 2978   | Layout 1             | `95658854907b`  |
| 2970   | Layout 1             | `95658854907b`  |
| 2959   | Layout 1             | `95658854907b`  |
| 2951   | Layout 1             | `95658854907b`  |
| 2942   | Layout 1             | `95658854907b`  |
| 2935   | Layout 1             | `95658854907b`  |
| 2932   | Layout 1             | `95658854907b`  |
| 2923   | Layout 1             | `95658854907b`  |
| 2919   | Layout 1             | `95658854907b`  |
| 2907   | Layout 1             | `95658854907b`  |
| 2900   | Layout 1             | `95658854907b`  |
| 2891   | Layout 1             | `95658854907b`  |
| 2882   | Layout 1             | `95658854907b`  |
| 2872   | Layout 1             | `95658854907b`  |
| 2863   | Layout 1             | `95658854907b`  |
| 2855   | Layout 1             | `95658854907b`  |
| 2849   | Layout 1             | `95658854907b`  |
| 2844   | Layout 1             | `95658854907b`  |
| 2834   | Layout 1             | `95658854907b`  |
| 2825   | Layout 1             | `95658854907b`  |
| 2819   | Layout 1             | `95658854907b`  |
| 2811   | Layout 1             | `95658854907b`  |
| 2803   | Layout 1             | `95658854907b`  |
| 2794   | Layout 1             | `95658854907b`  |
| 2783   | Layout 1             | `95658854907b`  |
| 2774   | Layout 1             | `95658854907b`  |
| 2765   | Layout 1             | `95658854907b`  |
| 2756   | Layout 1             | `95658854907b`  |
| 2750   | Layout 1             | `95658854907b`  |
| 2743   | Layout 1             | `95658854907b`  |
| 2736   | Layout 1             | `95658854907b`  |
| 2726   | Layout 1             | `95658854907b`  |
| 2717   | Layout 1             | `95658854907b`  |
| 2709   | Layout 1             | `95658854907b`  |
| 2703   | Layout 1             | `95658854907b`  |
| 2695   | Layout 1             | `95658854907b`  |
| 2684   | Layout 1             | `95658854907b`  |
| 2672   | Layout 1             | `95658854907b`  |
| 2665   | Layout 1             | `95658854907b`  |
| 2657   | Layout 1             | `95658854907b`  |
| 2649   | Layout 1             | `95658854907b`  |
| 2644   | Layout 1             | `95658854907b`  |
| 2637   | Layout 1             | `95658854907b`  |
| 2629   | Layout 1             | `95658854907b`  |
| 2619   | Layout 1             | `95658854907b`  |
| 2612   | Layout 1             | `95658854907b`  |
| 2606   | Layout 1             | `95658854907b`  |
| 2602   | Layout 1             | `95658854907b`  |
| 2601   | Layout 1             | `95658854907b`  |
| 2592   | Layout 1             | `95658854907b`  |
| 2583   | Layout 1             | `95658854907b`  |
| 2575   | Layout 1             | `95658854907b`  |
| 2567   | Layout 1             | `95658854907b`  |
| 2560   | Layout 1             | `95658854907b`  |
| 2553   | Layout 1             | `95658854907b`  |
| 2545   | Layout 1             | `95658854907b`  |
| 2538   | Layout 1             | `95658854907b`  |
| 2529   | Layout 1             | `95658854907b`  |
| 2519   | Layout 1             | `95658854907b`  |
| 2513   | Layout 1             | `95658854907b`  |
| 2510   | Layout 1             | `95658854907b`  |
| 2507   | Layout 1             | `95658854907b`  |
| 2503   | Layout 1             | `95658854907b`  |
| 2498   | Layout 1             | `95658854907b`  |
| 2492   | Layout 1             | `95658854907b`  |
| 2487   | Layout 1             | `95658854907b`  |
| 2480   | Layout 1             | `95658854907b`  |
| 2474   | Layout 1             | `95658854907b`  |
| 2468   | Layout 1             | `95658854907b`  |
| 2460   | Layout 1             | `95658854907b`  |
| 2453   | Layout 1             | `95658854907b`  |
| 2444   | Layout 1             | `95658854907b`  |
| 2438   | Layout 1             | `95658854907b`  |
| 2434   | Layout 1             | `95658854907b`  |
| 2429   | Layout 1             | `95658854907b`  |
| 2421   | Layout 1             | `95658854907b`  |
| 2414   | Layout 1             | `95658854907b`  |
| 2407   | Layout 1             | `95658854907b`  |
| 2401   | Layout 1             | `95658854907b`  |
| 2397   | Layout 1             | `95658854907b`  |
| 2393   | Layout 1             | `95658854907b`  |
| 2384   | Layout 1             | `95658854907b`  |
| 2378   | Layout 1             | `95658854907b`  |
| 2372   | Layout 1             | `95658854907b`  |
| 2358   | Layout 1             | `95658854907b`  |
| 2352   | Layout 1             | `95658854907b`  |
| 2347   | Layout 1             | `95658854907b`  |
| 2343   | Layout 1             | `95658854907b`  |
| 2335   | Layout 1             | `95658854907b`  |
| 2327   | Layout 1             | `95658854907b`  |
| 2324   | Layout 1             | `95658854907b`  |
| 2319   | Layout 1             | `95658854907b`  |
| 2313   | Layout 1             | `95658854907b`  |
| 2308   | Layout 1             | `95658854907b`  |
| 2302   | Layout 1             | `95658854907b`  |
| 2295   | Layout 1             | `95658854907b`  |
| 2290   | Layout 1             | `95658854907b`  |
| 2284   | Layout 1             | `95658854907b`  |
| 2276   | Layout 1             | `95658854907b`  |
| 2269   | Layout 1             | `95658854907b`  |
| 2259   | Layout 1             | `95658854907b`  |
| 2250   | Layout 1             | `95658854907b`  |
| 2243   | Layout 1             | `95658854907b`  |
| 2235   | Layout 1             | `95658854907b`  |
| 2229   | Layout 1             | `95658854907b`  |
| 2224   | Layout 1             | `95658854907b`  |
| 2218   | Layout 1             | `95658854907b`  |
| 2215   | Layout 1             | `95658854907b`  |
| 2207   | Layout 1             | `95658854907b`  |
| 2203   | Layout 1             | `95658854907b`  |
| 2196   | Layout 1             | `95658854907b`  |
| 2192   | Layout 1             | `95658854907b`  |
| 2189   | Layout 1             | `95658854907b`  |
| 2183   | Layout 1             | `95658854907b`  |
| 2179   | Layout 1             | `95658854907b`  |
| 2171   | Layout 1             | `95658854907b`  |
| 2163   | Layout 1             | `95658854907b`  |
| 2156   | Layout 1             | `95658854907b`  |
| 2151   | Layout 1             | `95658854907b`  |
| 2147   | Layout 1             | `95658854907b`  |
| 2142   | Layout 1             | `95658854907b`  |
| 2138   | Layout 1             | `95658854907b`  |
| 2134   | Layout 1             | `95658854907b`  |
| 2130   | Layout 1             | `95658854907b`  |
| 2122   | Layout 1             | `95658854907b`  |
| 2107   | Layout 1             | `95658854907b`  |
| 2098   | Layout 1             | `95658854907b`  |
| 2089   | Layout 1             | `95658854907b`  |
| 2081   | Layout 1             | `95658854907b`  |
| 2073   | Layout 1             | `95658854907b`  |
| 2067   | Layout 1             | `95658854907b`  |
| 2063   | Layout 1             | `95658854907b`  |
| 2059   | Layout 1             | `95658854907b`  |
| 2052   | Layout 1             | `95658854907b`  |
| 2044   | Layout 1             | `95658854907b`  |
| 2039   | Layout 1             | `95658854907b`  |
| 2032   | Layout 1             | `95658854907b`  |
| 2025   | Layout 1             | `95658854907b`  |
| 2011   | Layout 1             | `95658854907b`  |
| 2005   | Layout 1             | `95658854907b`  |
| 2000   | Layout 1             | `95658854907b`  |
| 1996   | Layout 1             | `95658854907b`  |
| 1991   | Layout 1             | `95658854907b`  |
| 1985   | Layout 1             | `95658854907b`  |
| 1980   | Layout 1             | `95658854907b`  |
| 1969   | Layout 1             | `95658854907b`  |
| 1964   | Layout 1             | `95658854907b`  |
| 1958   | Layout 1             | `95658854907b`  |
| 1950   | Layout 1             | `95658854907b`  |
| 1945   | Layout 1             | `95658854907b`  |
| 1937   | Layout 1             | `95658854907b`  |
| 1933   | Layout 1             | `95658854907b`  |
| 1927   | Layout 1             | `95658854907b`  |
| 1921   | Layout 1             | `95658854907b`  |
| 1914   | Layout 1             | `95658854907b`  |
| 1908   | Layout 1             | `95658854907b`  |
| 1897   | Layout 1             | `95658854907b`  |
| 1892   | Layout 1             | `95658854907b`  |
| 1886   | Layout 1             | `95658854907b`  |
| 1881   | Layout 1             | `95658854907b`  |
| 1871   | Layout 1             | `95658854907b`  |
| 1866   | Layout 1             | `95658854907b`  |
| 1862   | Layout 1             | `95658854907b`  |
| 1854   | Layout 1             | `95658854907b`  |
| 1846   | Layout 1             | `95658854907b`  |
| 1838   | Layout 1             | `95658854907b`  |
| 1832   | Layout 1             | `95658854907b`  |
| 1826   | Layout 1             | `95658854907b`  |
| 1822   | Layout 1             | `95658854907b`  |
| 1818   | Layout 1             | `95658854907b`  |
| 1804   | Layout 1             | `95658854907b`  |
| 1794   | Layout 1             | `95658854907b`  |
| 1790   | Layout 1             | `95658854907b`  |
| 1784   | Layout 1             | `95658854907b`  |
| 1774   | Layout 1             | `95658854907b`  |
| 1771   | Layout 1             | `95658854907b`  |
| 1762   | Layout 1             | `95658854907b`  |
| 1759   | Layout 1             | `95658854907b`  |
| 1754   | Layout 1             | `95658854907b`  |
| 1749   | Layout 1             | `95658854907b`  |
| 1743   | Layout 1             | `95658854907b`  |
| 1737   | Layout 1             | `95658854907b`  |
| 1731   | Layout 1             | `95658854907b`  |
| 1725   | Layout 1             | `95658854907b`  |
| 1717   | Layout 1             | `95658854907b`  |
| 1710   | Layout 1             | `95658854907b`  |
| 1704   | Layout 1             | `95658854907b`  |
| 1698   | Layout 1             | `95658854907b`  |
| 1690   | Layout 1             | `95658854907b`  |
| 1685   | Layout 1             | `95658854907b`  |
| 1680   | Layout 1             | `95658854907b`  |
| 1674   | Layout 1             | `95658854907b`  |
| 1668   | Layout 1             | `95658854907b`  |
| 1659   | Layout 1             | `95658854907b`  |
| 1649   | Layout 1             | `95658854907b`  |
| 1642   | Layout 1             | `95658854907b`  |
| 1636   | Layout 1             | `95658854907b`  |
| 1628   | Layout 1             | `95658854907b`  |
| 1622   | Layout 1             | `95658854907b`  |
| 1614   | Layout 1             | `95658854907b`  |
| 1608   | Layout 1             | `95658854907b`  |
| 1602   | Layout 1             | `95658854907b`  |
| 1598   | Layout 1             | `95658854907b`  |
| 1594   | Layout 1             | `95658854907b`  |
| 1590   | Layout 1             | `95658854907b`  |
| 1587   | Layout 1             | `95658854907b`  |
| 1584   | Layout 1             | `95658854907b`  |
| 1579   | Layout 1             | `95658854907b`  |
| 1572   | Layout 1             | `95658854907b`  |
| 1565   | Layout 1             | `95658854907b`  |
| 1559   | Layout 1             | `95658854907b`  |
| 1554   | Layout 1             | `95658854907b`  |
| 1547   | Layout 1             | `95658854907b`  |
| 1537   | Layout 1             | `95658854907b`  |
| 1529   | Layout 1             | `95658854907b`  |
| 1524   | Layout 1             | `95658854907b`  |
| 1519   | Layout 1             | `95658854907b`  |
| 1509   | Layout 1             | `95658854907b`  |
| 1506   | Layout 1             | `95658854907b`  |
| 1504   | Layout 1             | `95658854907b`  |
| 1500   | Layout 1             | `95658854907b`  |
| 1493   | Layout 1             | `95658854907b`  |
| 1489   | Layout 1             | `95658854907b`  |
| 1485   | Layout 1             | `95658854907b`  |
| 1481   | Layout 1             | `95658854907b`  |
| 1474   | Layout 1             | `95658854907b`  |
| 1466   | Layout 1             | `95658854907b`  |
| 1462   | Layout 1             | `95658854907b`  |
| 1459   | Layout 1             | `95658854907b`  |
| 1453   | Layout 1             | `95658854907b`  |
| 1450   | Layout 1             | `95658854907b`  |
| 1445   | Layout 1             | `95658854907b`  |
| 1439   | Layout 1             | `95658854907b`  |
| 1433   | Layout 1             | `95658854907b`  |
| 1430   | Layout 1             | `95658854907b`  |
| 1426   | Layout 1             | `95658854907b`  |
| 1421   | Layout 1             | `95658854907b`  |
| 1417   | Layout 1             | `95658854907b`  |
| 1416   | Layout 1             | `95658854907b`  |
| 1409   | Layout 1             | `95658854907b`  |
| 1405   | Layout 1             | `95658854907b`  |
| 1401   | Layout 1             | `95658854907b`  |
| 1396   | Layout 1             | `95658854907b`  |
| 1391   | Layout 1             | `95658854907b`  |
| 1390   | Layout 1             | `95658854907b`  |
| 1386   | Layout 1             | `95658854907b`  |
| 1381   | Layout 1             | `95658854907b`  |
| 1379   | Layout 1             | `95658854907b`  |
| 1372   | Layout 1             | `95658854907b`  |
| 1366   | Layout 1             | `95658854907b`  |
| 1364   | Layout 1             | `95658854907b`  |
| 1363   | Layout 1             | `95658854907b`  |
| 1360   | Layout 1             | `95658854907b`  |
| 1358   | Layout 1             | `95658854907b`  |
| 1355   | Layout 1             | `95658854907b`  |
| 1351   | Layout 1             | `95658854907b`  |
| 1348   | Layout 1             | `95658854907b`  |
| 1346   | Layout 1             | `95658854907b`  |
| 1341   | No documented layout | `95658854907b`  |
| 1340   | No documented layout | `95658854907b`  |
| 1338   | No documented layout | `95658854907b`  |
| 1335   | No documented layout | `95658854907b`  |
| 1333   | No documented layout | `95658854907b`  |
| 1329   | No documented layout | `95658854907b`  |
| 1327   | No documented layout | `95658854907b`  |
| 1324   | No documented layout | `95658854907b`  |
| 1321   | No documented layout | `95658854907b`  |
| 1319   | No documented layout | `95658854907b`  |
| 1318   | No documented layout | `95658854907b`  |
| 1316   | No documented layout | `95658854907b`  |
| 1313   | No documented layout | `95658854907b`  |
| 1311   | No documented layout | `95658854907b`  |
| 1309   | No documented layout | `95658854907b`  |
| 1304   | No documented layout | `95658854907b`  |
| 1292   | No documented layout | `95658854907b`  |
| 1286   | No documented layout | `95658854907b`  |
| 1280   | No documented layout | `95658854907b`  |
| 1276   | No file              | `95658854907b`  |
| 1267   | No file              | `95658854907b`  |
| 1261   | No file              | `95658854907b`  |
| 1256   | No file              | `95658854907b`  |
| 1250   | No file              | `95658854907b`  |
| 1246   | No file              | `95658854907b`  |
| 1239   | No file              | `95658854907b`  |
| 1230   | No file              | `95658854907b`  |
| 1226   | No file              | `95658854907b`  |
| 1220   | No file              | `95658854907b`  |
| 1217   | No file              | `95658854907b`  |
| 1211   | No file              | `95658854907b`  |
| 1210   | No file              | `95658854907b`  |
| 1208   | No file              | `95658854907b`  |
| 1203   | No file              | `95658854907b`  |
| 1197   | No file              | `95658854907b`  |
| 1194   | No file              | `95658854907b`  |
| 1192   | No file              | `95658854907b`  |
| 1187   | No file              | `95658854907b`  |
| 1183   | No file              | `95658854907b`  |
| 1177   | No file              | `95658854907b`  |
| 1173   | No file              | `95658854907b`  |
| 1167   | No file              | `95658854907b`  |
| 1164   | No file              | `95658854907b`  |
| 1156   | No file              | `95658854907b`  |
| 1149   | No file              | `95658854907b`  |
| 1144   | No file              | `95658854907b`  |
| 1137   | No file              | `95658854907b`  |
| 1132   | No file              | `95658854907b`  |
| 1127   | No file              | `95658854907b`  |
| 1122   | No file              | `95658854907b`  |
| 1118   | No file              | `95658854907b`  |
| 1114   | No file              | `95658854907b`  |
| 1109   | No file              | `95658854907b`  |
| 1102   | No file              | `95658854907b`  |
| 1096   | No file              | `95658854907b`  |
| 1088   | No file              | `95658854907b`  |
| 1081   | No file              | `95658854907b`  |
| 1076   | No file              | `95658854907b`  |
| 1069   | No file              | `95658854907b`  |
| 1064   | No file              | `95658854907b`  |
| 1058   | No file              | `95658854907b`  |
| 1051   | No file              | `95658854907b`  |
| 1044   | No file              | `95658854907b`  |
| 1036   | No file              | `95658854907b`  |
| 1026   | No file              | `95658854907b`  |
| 1016   | No file              | `95658854907b`  |
| 1009   | No file              | `95658854907b`  |
| 1005   | No file              | `95658854907b`  |
| 1000   | No file              | `95658854907b`  |
| 998    | No file              | `95658854907b`  |
| 990    | No file              | `95658854907b`  |
| 979    | No file              | `95658854907b`  |
| 972    | No file              | `95658854907b`  |
| 963    | No file              | `95658854907b`  |
| 955    | No file              | `95658854907b`  |
| 946    | No file              | `95658854907b`  |
| 938    | No file              | `95658854907b`  |
| 927    | No file              | `95658854907b`  |
| 911    | No file              | `95658854907b`  |
| 904    | No file              | `95658854907b`  |
| 899    | No file              | `95658854907b`  |
| 894    | No file              | `95658854907b`  |
| 885    | No file              | `95658854907b`  |
| 879    | No file              | `95658854907b`  |
| 872    | No file              | `95658854907b`  |
| 864    | No file              | `95658854907b`  |
| 855    | No file              | `95658854907b`  |
| 853    | No file              | `95658854907b`  |
| 845    | No file              | `95658854907b`  |
| 837    | No file              | `95658854907b`  |
| 829    | No file              | `95658854907b`  |
| 822    | No file              | `95658854907b`  |
| 814    | No file              | `95658854907b`  |
| 805    | No file              | `95658854907b`  |
| 794    | No file              | `95658854907b`  |
| 787    | No file              | `95658854907b`  |
| 780    | No file              | `95658854907b`  |
| 771    | No file              | `95658854907b`  |
| 760    | No file              | `95658854907b`  |
| 748    | No file              | `95658854907b`  |
| 741    | No file              | `95658854907b`  |
| 736    | No file              | `95658854907b`  |
| 731    | No file              | `95658854907b`  |
| 723    | No file              | `95658854907b`  |
| 711    | No file              | `95658854907b`  |
| 707    | No file              | `95658854907b`  |
| 697    | No file              | `95658854907b`  |
| 689    | No file              | `95658854907b`  |
| 683    | No file              | `95658854907b`  |
| 678    | No file              | `95658854907b`  |
| 670    | No file              | `95658854907b`  |
| 661    | No file              | `95658854907b`  |
| 656    | No file              | `95658854907b`  |
| 652    | No file              | `95658854907b`  |
| 643    | No file              | `95658854907b`  |
| 637    | No file              | `95658854907b`  |
| 630    | No file              | `95658854907b`  |
| 627    | No file              | `95658854907b`  |
| 621    | No file              | `95658854907b`  |
| 617    | No file              | `95658854907b`  |
| 615    | No file              | `95658854907b`  |
| 606    | No file              | `95658854907b`  |
| 599    | No file              | `95658854907b`  |
| 592    | No file              | `95658854907b`  |
| 586    | No file              | `95658854907b`  |
| 577    | No file              | `95658854907b`  |
| 569    | No file              | `95658854907b`  |
| 561    | No file              | `95658854907b`  |
| 554    | No file              | `95658854907b`  |
| 542    | No file              | `95658854907b`  |
| 532    | No file              | `95658854907b`  |
| 531    | No file              | `95658854907b`  |
| 526    | No file              | `95658854907b`  |
| 521    | No file              | `95658854907b`  |
| 517    | No file              | `95658854907b`  |
| 510    | No file              | `95658854907b`  |
| 508    | No file              | `95658854907b`  |
| 504    | No file              | `95658854907b`  |
| 497    | No file              | `95658854907b`  |
| 491    | No file              | `95658854907b`  |
| 485    | No file              | `95658854907b`  |
| 478    | No file              | `95658854907b`  |
| 472    | No file              | `95658854907b`  |
| 466    | No file              | `95658854907b`  |
| 457    | No file              | `95658854907b`  |
| 452    | No file              | `95658854907b`  |
| 449    | No file              | `95658854907b`  |
| 435    | No file              | `95658854907b`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                     |
| --------------------------------- | -------- | -------------------------------------------------------- |
| `lifeactionexperienceoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| `languagedata_en.loc`             | Optional | Item name for `item_key` (`str_type=0`, `str_id1=item_key`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                      |
| ------- | ---------- | ----- | ------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `3,052` on client 3474     |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (26 bytes)

| Offset  | Type   | Field             | Notes                                                              |
| ------- | ------ | ----------------- | ------------------------------------------------------------------ |
| `+0x00` | u32    | item_key          | Item, packed as `enchant_level << 24 \| item_id`; unique per row, the index key |
| `+0x04` | u32    | item_key_dup      | Equal to `item_key` in every row; the index's `data_offset` points here |
| `+0x08` | u8[2]  | life_action_types | Life skill per slot, see [Life Skills](lifeexp_dbss.md#life-skills); `15` (`Type_Count`) is an empty slot |
| `+0x0A` | i64[2] | experiences       | EXP per slot; `0` in every slot (clients 1784 and 3474)            |

Every `item_key` has a zero top byte (enhancement level 0) on both clients.
The rows are not sorted by key.

### `lifeactionexperienceoffset.dbss`

| Offset  | Type              | Field | Notes                                          |
| ------- | ----------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32               | count | Equals the `lifeactionexperience.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row           |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                     |
| ------- | ---- | ----------- | ----------------------------------------- |
| `+0x00` | u32  | item_key    | Row key                                   |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_key_dup`          |
| `+0x08` | u32  | data_size   | Row size - 4: `22`                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The row is the 2016 `gc::LifeActionExperienceStaticStatus` after the index
key: `_itemKey` (a `gc::ItemEnchantKey`), `_type`
(`pa::Array<gc::LifeExperienceType,2>`) and `_experience`
(`pa::Array<__int64,2>`). The 2016 `gc::LifeExperienceType` ends at
`Type_Count = 9`; the client 3474 Lua's `CppEnums.LifeExperienceType` ends at
`Type_Count = 15`, the empty slot value on both clients.

The values match the `LifeActionEXP_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `ItemKey`. An empty sheet cell in the
second slot is type `15` with EXP `0`.

| Field             | Column                                 | Same value (client 1784) | Same value (client 3474) |
| ----------------- | -------------------------------------- | ------------------------ | ------------------------ |
| item_key          | `ItemKey`                              | 1,817 of 1,817 rows      | 1,836 of 3,052 rows      |
| life_action_types | `LifeActionType0`, `LifeActionType1`   | 1,817 of 1,817           | 1,835 of 1,836           |
| experiences       | `Exp0`, `Exp1`                         | 1,817 of 1,817           | 1,836 of 1,836           |

The sheet has 1,858 rows. Client 1784 lacks 41 of them (`9069`, `9339` to
`9379` with gaps, `9640` and `9641`); client 3474 lacks 22 (`5201` Fruit of
Crimson Flame to `5217` with gaps, and seven keys from `9347` to `9377`). The one row that differs on client 3474 is `4999` Black Gem
Fragment, which gained a second Gathering slot after client 1784. The client
3474 file adds 1,216 keys the sheet lacks, up to `890074` Endless Ocean
Draught.

## Notes

- On client 3474, 141 rows fill both slots with Gathering (`0`, `0`) and
  2,911 fill the first slot only. The two-slot rows include processed
  materials (`4078` Melted Vanadium Shard, `4098` Melted Magnetite Shard),
  `4476` Red Coral, `5006` Spirit's Leaf and `5401` Sunrise Herb. The
  one-slot rows include items no life skill gives, such as `292` Flare of
  the Ancients and `518` HP Potion (Medium).
- No client Lua file names the table or reads it, and the client 1784 sheet
  holds `0` in every `Exp` cell too.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `actionexp.dbss` as "offset-indexed action award
  tables" whose record payloads "do not follow the ordinary decoded
  DBSS/PABR forms". The row is a plain fixed-size struct with a u32 count before it.

## Open Questions

### What The Life Skill Slots Select

Every row holds `0` EXP, so the file awards nothing on clients 1784 and
3474. Why 141 items carry a second Gathering slot, and what the item list
selects when the EXP is zero, has no reader in the client Lua to show.
