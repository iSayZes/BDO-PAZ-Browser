# `employeestaticstatus.bss` Format

## Purpose

Static stats of every hireable ship crew member: one row per sailor per level, then one row per First Mate. Each row names the character whose name, title and portrait the sailor uses, and carries up to 19 ability values such as the ship stat bonuses shown in the Manage Sailors window.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes  | Records                         | Row bytes |
| ------ | -------------- | -------------------------- | ------ | ------------------------------- | --------- |
| 2      | 2882 and later | `employeestaticstatus.bss` | 33,465 | 4,484 Ability, 236 Employee Row | 5         |
| 1      | 1340 to 2736   | `employeestaticstatus.bss` | 29,799 | 3,910 Ability, 230 Employee Row | 5         |

| Layout | File                       | Known            | Unknown        |
| ------ | -------------------------- | ---------------- | -------------- |
| 2      | `employeestaticstatus.bss` | 31,985 B (95.6%) | 1,480 B (4.4%) |
| 1      | `employeestaticstatus.bss` | 28,379 B (95.2%) | 1,420 B (4.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `075a294681fe`  |
| 3482   | Layout 2             | `075a294681fe`  |
| 3474   | Layout 2             | `075a294681fe`  |
| 3473   | Layout 2             | `075a294681fe`  |
| 3464   | Layout 2             | `075a294681fe`  |
| 3458   | Layout 2             | `075a294681fe`  |
| 3454   | Layout 2             | `075a294681fe`  |
| 3444   | Layout 2             | `075a294681fe`  |
| 3435   | Layout 2             | `075a294681fe`  |
| 3426   | Layout 2             | `075a294681fe`  |
| 3418   | Layout 2             | `075a294681fe`  |
| 3412   | Layout 2             | `075a294681fe`  |
| 3402   | Layout 2             | `075a294681fe`  |
| 3396   | Layout 2             | `075a294681fe`  |
| 3387   | Layout 2             | `075a294681fe`  |
| 3381   | Layout 2             | `075a294681fe`  |
| 3373   | Layout 2             | `075a294681fe`  |
| 3364   | Layout 2             | `075a294681fe`  |
| 3356   | Layout 2             | `075a294681fe`  |
| 3349   | Layout 2             | `075a294681fe`  |
| 3342   | Layout 2             | `075a294681fe`  |
| 3335   | Layout 2             | `075a294681fe`  |
| 3326   | Layout 2             | `075a294681fe`  |
| 3321   | Layout 2             | `075a294681fe`  |
| 3314   | Layout 2             | `075a294681fe`  |
| 3303   | Layout 2             | `075a294681fe`  |
| 3302   | Layout 2             | `075a294681fe`  |
| 3293   | Layout 2             | `075a294681fe`  |
| 3283   | Layout 2             | `075a294681fe`  |
| 3275   | Layout 2             | `075a294681fe`  |
| 3267   | Layout 2             | `075a294681fe`  |
| 3258   | Layout 2             | `075a294681fe`  |
| 3251   | Layout 2             | `075a294681fe`  |
| 3242   | Layout 2             | `075a294681fe`  |
| 3235   | Layout 2             | `075a294681fe`  |
| 3229   | Layout 2             | `075a294681fe`  |
| 3212   | Layout 2             | `075a294681fe`  |
| 3203   | Layout 2             | `075a294681fe`  |
| 3193   | Layout 2             | `075a294681fe`  |
| 3186   | Layout 2             | `075a294681fe`  |
| 3177   | Layout 2             | `075a294681fe`  |
| 3169   | Layout 2             | `075a294681fe`  |
| 3158   | Layout 2             | `075a294681fe`  |
| 3151   | Layout 2             | `075a294681fe`  |
| 3144   | Layout 2             | `075a294681fe`  |
| 3133   | Layout 2             | `075a294681fe`  |
| 3125   | Layout 2             | `075a294681fe`  |
| 3118   | Layout 2             | `075a294681fe`  |
| 3111   | Layout 2             | `075a294681fe`  |
| 3103   | Layout 2             | `075a294681fe`  |
| 3095   | Layout 2             | `075a294681fe`  |
| 3086   | Layout 2             | `075a294681fe`  |
| 3072   | Layout 2             | `075a294681fe`  |
| 3062   | Layout 2             | `075a294681fe`  |
| 3052   | Layout 2             | `075a294681fe`  |
| 3045   | Layout 2             | `075a294681fe`  |
| 3037   | Layout 2             | `075a294681fe`  |
| 3030   | Layout 2             | `075a294681fe`  |
| 3021   | Layout 2             | `075a294681fe`  |
| 3012   | Layout 2             | `075a294681fe`  |
| 3002   | Layout 2             | `075a294681fe`  |
| 2995   | Layout 2             | `075a294681fe`  |
| 2987   | Layout 2             | `075a294681fe`  |
| 2978   | Layout 2             | `075a294681fe`  |
| 2970   | Layout 2             | `075a294681fe`  |
| 2959   | Layout 2             | `075a294681fe`  |
| 2951   | Layout 2             | `075a294681fe`  |
| 2942   | Layout 2             | `075a294681fe`  |
| 2935   | Layout 2             | `075a294681fe`  |
| 2932   | Layout 2             | `075a294681fe`  |
| 2923   | Layout 2             | `075a294681fe`  |
| 2919   | Layout 2             | `075a294681fe`  |
| 2907   | Layout 2             | `075a294681fe`  |
| 2900   | Layout 2             | `075a294681fe`  |
| 2891   | Layout 2             | `075a294681fe`  |
| 2882   | Layout 2             | `075a294681fe`  |
| 2872   | No documented layout | `075a294681fe`  |
| 2863   | No documented layout | `075a294681fe`  |
| 2855   | No documented layout | `075a294681fe`  |
| 2849   | No documented layout | `075a294681fe`  |
| 2844   | No documented layout | `075a294681fe`  |
| 2834   | No documented layout | `075a294681fe`  |
| 2825   | No documented layout | `075a294681fe`  |
| 2819   | No documented layout | `075a294681fe`  |
| 2811   | No documented layout | `075a294681fe`  |
| 2803   | No documented layout | `075a294681fe`  |
| 2794   | No documented layout | `075a294681fe`  |
| 2783   | No documented layout | `075a294681fe`  |
| 2774   | No documented layout | `075a294681fe`  |
| 2765   | No documented layout | `075a294681fe`  |
| 2756   | No documented layout | `075a294681fe`  |
| 2750   | No documented layout | `075a294681fe`  |
| 2743   | No documented layout | `075a294681fe`  |
| 2736   | Layout 1             | `075a294681fe`  |
| 2726   | Layout 1             | `075a294681fe`  |
| 2717   | Layout 1             | `075a294681fe`  |
| 2709   | Layout 1             | `075a294681fe`  |
| 2703   | Layout 1             | `075a294681fe`  |
| 2695   | Layout 1             | `075a294681fe`  |
| 2684   | Layout 1             | `075a294681fe`  |
| 2672   | Layout 1             | `075a294681fe`  |
| 2665   | Layout 1             | `075a294681fe`  |
| 2657   | Layout 1             | `075a294681fe`  |
| 2649   | Layout 1             | `075a294681fe`  |
| 2644   | Layout 1             | `075a294681fe`  |
| 2637   | Layout 1             | `075a294681fe`  |
| 2629   | Layout 1             | `075a294681fe`  |
| 2619   | Layout 1             | `075a294681fe`  |
| 2612   | Layout 1             | `075a294681fe`  |
| 2606   | Layout 1             | `075a294681fe`  |
| 2602   | Layout 1             | `075a294681fe`  |
| 2601   | Layout 1             | `075a294681fe`  |
| 2592   | Layout 1             | `075a294681fe`  |
| 2583   | Layout 1             | `075a294681fe`  |
| 2575   | Layout 1             | `075a294681fe`  |
| 2567   | Layout 1             | `075a294681fe`  |
| 2560   | Layout 1             | `075a294681fe`  |
| 2553   | Layout 1             | `075a294681fe`  |
| 2545   | Layout 1             | `075a294681fe`  |
| 2538   | Layout 1             | `075a294681fe`  |
| 2529   | Layout 1             | `075a294681fe`  |
| 2519   | Layout 1             | `075a294681fe`  |
| 2513   | Layout 1             | `075a294681fe`  |
| 2510   | Layout 1             | `075a294681fe`  |
| 2507   | Layout 1             | `075a294681fe`  |
| 2503   | Layout 1             | `075a294681fe`  |
| 2498   | Layout 1             | `075a294681fe`  |
| 2492   | Layout 1             | `075a294681fe`  |
| 2487   | Layout 1             | `075a294681fe`  |
| 2480   | Layout 1             | `075a294681fe`  |
| 2474   | Layout 1             | `075a294681fe`  |
| 2468   | Layout 1             | `075a294681fe`  |
| 2460   | Layout 1             | `075a294681fe`  |
| 2453   | Layout 1             | `075a294681fe`  |
| 2444   | Layout 1             | `075a294681fe`  |
| 2438   | Layout 1             | `075a294681fe`  |
| 2434   | Layout 1             | `075a294681fe`  |
| 2429   | Layout 1             | `075a294681fe`  |
| 2421   | Layout 1             | `075a294681fe`  |
| 2414   | Layout 1             | `075a294681fe`  |
| 2407   | Layout 1             | `075a294681fe`  |
| 2401   | Layout 1             | `075a294681fe`  |
| 2397   | Layout 1             | `075a294681fe`  |
| 2393   | Layout 1             | `075a294681fe`  |
| 2384   | Layout 1             | `075a294681fe`  |
| 2378   | Layout 1             | `075a294681fe`  |
| 2372   | Layout 1             | `075a294681fe`  |
| 2358   | Layout 1             | `075a294681fe`  |
| 2352   | Layout 1             | `075a294681fe`  |
| 2347   | Layout 1             | `075a294681fe`  |
| 2343   | Layout 1             | `075a294681fe`  |
| 2335   | Layout 1             | `075a294681fe`  |
| 2327   | Layout 1             | `075a294681fe`  |
| 2324   | Layout 1             | `075a294681fe`  |
| 2319   | Layout 1             | `075a294681fe`  |
| 2313   | Layout 1             | `075a294681fe`  |
| 2308   | Layout 1             | `075a294681fe`  |
| 2302   | Layout 1             | `075a294681fe`  |
| 2295   | Layout 1             | `075a294681fe`  |
| 2290   | Layout 1             | `075a294681fe`  |
| 2284   | Layout 1             | `075a294681fe`  |
| 2276   | Layout 1             | `075a294681fe`  |
| 2269   | Layout 1             | `075a294681fe`  |
| 2259   | Layout 1             | `075a294681fe`  |
| 2250   | Layout 1             | `075a294681fe`  |
| 2243   | Layout 1             | `075a294681fe`  |
| 2235   | Layout 1             | `075a294681fe`  |
| 2229   | Layout 1             | `075a294681fe`  |
| 2224   | Layout 1             | `075a294681fe`  |
| 2218   | Layout 1             | `075a294681fe`  |
| 2215   | Layout 1             | `075a294681fe`  |
| 2207   | Layout 1             | `075a294681fe`  |
| 2203   | Layout 1             | `075a294681fe`  |
| 2196   | Layout 1             | `075a294681fe`  |
| 2192   | Layout 1             | `075a294681fe`  |
| 2189   | Layout 1             | `075a294681fe`  |
| 2183   | Layout 1             | `075a294681fe`  |
| 2179   | Layout 1             | `075a294681fe`  |
| 2171   | Layout 1             | `075a294681fe`  |
| 2163   | Layout 1             | `075a294681fe`  |
| 2156   | Layout 1             | `075a294681fe`  |
| 2151   | Layout 1             | `075a294681fe`  |
| 2147   | Layout 1             | `075a294681fe`  |
| 2142   | Layout 1             | `075a294681fe`  |
| 2138   | Layout 1             | `075a294681fe`  |
| 2134   | Layout 1             | `075a294681fe`  |
| 2130   | Layout 1             | `075a294681fe`  |
| 2122   | Layout 1             | `075a294681fe`  |
| 2107   | Layout 1             | `075a294681fe`  |
| 2098   | Layout 1             | `075a294681fe`  |
| 2089   | Layout 1             | `075a294681fe`  |
| 2081   | Layout 1             | `075a294681fe`  |
| 2073   | Layout 1             | `075a294681fe`  |
| 2067   | Layout 1             | `075a294681fe`  |
| 2063   | Layout 1             | `075a294681fe`  |
| 2059   | Layout 1             | `075a294681fe`  |
| 2052   | Layout 1             | `075a294681fe`  |
| 2044   | Layout 1             | `075a294681fe`  |
| 2039   | Layout 1             | `075a294681fe`  |
| 2032   | Layout 1             | `075a294681fe`  |
| 2025   | Layout 1             | `075a294681fe`  |
| 2011   | Layout 1             | `075a294681fe`  |
| 2005   | Layout 1             | `075a294681fe`  |
| 2000   | Layout 1             | `075a294681fe`  |
| 1996   | Layout 1             | `075a294681fe`  |
| 1991   | Layout 1             | `075a294681fe`  |
| 1985   | Layout 1             | `075a294681fe`  |
| 1980   | Layout 1             | `075a294681fe`  |
| 1969   | Layout 1             | `075a294681fe`  |
| 1964   | Layout 1             | `075a294681fe`  |
| 1958   | Layout 1             | `075a294681fe`  |
| 1950   | Layout 1             | `075a294681fe`  |
| 1945   | Layout 1             | `075a294681fe`  |
| 1937   | Layout 1             | `075a294681fe`  |
| 1933   | Layout 1             | `075a294681fe`  |
| 1927   | Layout 1             | `075a294681fe`  |
| 1921   | Layout 1             | `075a294681fe`  |
| 1914   | Layout 1             | `075a294681fe`  |
| 1908   | Layout 1             | `075a294681fe`  |
| 1897   | Layout 1             | `075a294681fe`  |
| 1892   | Layout 1             | `075a294681fe`  |
| 1886   | Layout 1             | `075a294681fe`  |
| 1881   | Layout 1             | `075a294681fe`  |
| 1871   | Layout 1             | `075a294681fe`  |
| 1866   | Layout 1             | `075a294681fe`  |
| 1862   | Layout 1             | `075a294681fe`  |
| 1854   | Layout 1             | `075a294681fe`  |
| 1846   | Layout 1             | `075a294681fe`  |
| 1838   | Layout 1             | `075a294681fe`  |
| 1832   | Layout 1             | `075a294681fe`  |
| 1826   | Layout 1             | `075a294681fe`  |
| 1822   | Layout 1             | `075a294681fe`  |
| 1818   | Layout 1             | `075a294681fe`  |
| 1804   | Layout 1             | `075a294681fe`  |
| 1794   | Layout 1             | `075a294681fe`  |
| 1790   | Layout 1             | `075a294681fe`  |
| 1784   | Layout 1             | `075a294681fe`  |
| 1774   | Layout 1             | `075a294681fe`  |
| 1771   | Layout 1             | `075a294681fe`  |
| 1762   | Layout 1             | `075a294681fe`  |
| 1759   | Layout 1             | `075a294681fe`  |
| 1754   | Layout 1             | `075a294681fe`  |
| 1749   | Layout 1             | `075a294681fe`  |
| 1743   | Layout 1             | `075a294681fe`  |
| 1737   | Layout 1             | `075a294681fe`  |
| 1731   | Layout 1             | `075a294681fe`  |
| 1725   | Layout 1             | `075a294681fe`  |
| 1717   | Layout 1             | `075a294681fe`  |
| 1710   | Layout 1             | `075a294681fe`  |
| 1704   | Layout 1             | `075a294681fe`  |
| 1698   | Layout 1             | `075a294681fe`  |
| 1690   | Layout 1             | `075a294681fe`  |
| 1685   | Layout 1             | `075a294681fe`  |
| 1680   | Layout 1             | `075a294681fe`  |
| 1674   | Layout 1             | `075a294681fe`  |
| 1668   | Layout 1             | `075a294681fe`  |
| 1659   | Layout 1             | `075a294681fe`  |
| 1649   | Layout 1             | `075a294681fe`  |
| 1642   | Layout 1             | `075a294681fe`  |
| 1636   | Layout 1             | `075a294681fe`  |
| 1628   | Layout 1             | `075a294681fe`  |
| 1622   | Layout 1             | `075a294681fe`  |
| 1614   | Layout 1             | `075a294681fe`  |
| 1608   | Layout 1             | `075a294681fe`  |
| 1602   | Layout 1             | `075a294681fe`  |
| 1598   | Layout 1             | `075a294681fe`  |
| 1594   | Layout 1             | `075a294681fe`  |
| 1590   | Layout 1             | `075a294681fe`  |
| 1587   | Layout 1             | `075a294681fe`  |
| 1584   | Layout 1             | `075a294681fe`  |
| 1579   | Layout 1             | `075a294681fe`  |
| 1572   | Layout 1             | `075a294681fe`  |
| 1565   | Layout 1             | `075a294681fe`  |
| 1559   | Layout 1             | `075a294681fe`  |
| 1554   | Layout 1             | `075a294681fe`  |
| 1547   | Layout 1             | `075a294681fe`  |
| 1537   | Layout 1             | `075a294681fe`  |
| 1529   | Layout 1             | `075a294681fe`  |
| 1524   | Layout 1             | `075a294681fe`  |
| 1519   | Layout 1             | `075a294681fe`  |
| 1509   | Layout 1             | `075a294681fe`  |
| 1506   | Layout 1             | `075a294681fe`  |
| 1504   | Layout 1             | `075a294681fe`  |
| 1500   | Layout 1             | `075a294681fe`  |
| 1493   | Layout 1             | `075a294681fe`  |
| 1489   | Layout 1             | `075a294681fe`  |
| 1485   | Layout 1             | `075a294681fe`  |
| 1481   | Layout 1             | `075a294681fe`  |
| 1474   | Layout 1             | `075a294681fe`  |
| 1466   | Layout 1             | `075a294681fe`  |
| 1462   | Layout 1             | `075a294681fe`  |
| 1459   | Layout 1             | `075a294681fe`  |
| 1453   | Layout 1             | `075a294681fe`  |
| 1450   | Layout 1             | `075a294681fe`  |
| 1445   | Layout 1             | `075a294681fe`  |
| 1439   | Layout 1             | `075a294681fe`  |
| 1433   | Layout 1             | `075a294681fe`  |
| 1430   | Layout 1             | `075a294681fe`  |
| 1426   | Layout 1             | `075a294681fe`  |
| 1421   | Layout 1             | `075a294681fe`  |
| 1417   | Layout 1             | `075a294681fe`  |
| 1416   | Layout 1             | `075a294681fe`  |
| 1409   | Layout 1             | `075a294681fe`  |
| 1405   | Layout 1             | `075a294681fe`  |
| 1401   | Layout 1             | `075a294681fe`  |
| 1396   | Layout 1             | `075a294681fe`  |
| 1391   | Layout 1             | `075a294681fe`  |
| 1390   | Layout 1             | `075a294681fe`  |
| 1386   | Layout 1             | `075a294681fe`  |
| 1381   | Layout 1             | `075a294681fe`  |
| 1379   | Layout 1             | `075a294681fe`  |
| 1372   | Layout 1             | `075a294681fe`  |
| 1366   | Layout 1             | `075a294681fe`  |
| 1364   | Layout 1             | `075a294681fe`  |
| 1363   | Layout 1             | `075a294681fe`  |
| 1360   | Layout 1             | `075a294681fe`  |
| 1358   | Layout 1             | `075a294681fe`  |
| 1355   | Layout 1             | `075a294681fe`  |
| 1351   | Layout 1             | `075a294681fe`  |
| 1348   | Layout 1             | `075a294681fe`  |
| 1346   | Layout 1             | `075a294681fe`  |
| 1341   | Layout 1             | `075a294681fe`  |
| 1340   | Layout 1             | `075a294681fe`  |
| 1338   | No documented layout | `075a294681fe`  |
| 1335   | No documented layout | `075a294681fe`  |
| 1333   | No documented layout | `075a294681fe`  |
| 1329   | No documented layout | `075a294681fe`  |
| 1327   | No documented layout | `075a294681fe`  |
| 1324   | No documented layout | `075a294681fe`  |
| 1321   | No documented layout | `075a294681fe`  |
| 1319   | No documented layout | `075a294681fe`  |
| 1318   | No documented layout | `075a294681fe`  |
| 1316   | No documented layout | `075a294681fe`  |
| 1313   | No documented layout | `075a294681fe`  |
| 1311   | No documented layout | `075a294681fe`  |
| 1309   | No documented layout | `075a294681fe`  |
| 1304   | No documented layout | `075a294681fe`  |
| 1292   | No documented layout | `075a294681fe`  |
| 1286   | No documented layout | `075a294681fe`  |
| 1280   | No documented layout | `075a294681fe`  |
| 1276   | No documented layout | `075a294681fe`  |
| 1267   | No documented layout | `075a294681fe`  |
| 1261   | No documented layout | `075a294681fe`  |
| 1256   | No documented layout | `075a294681fe`  |
| 1250   | No documented layout | `075a294681fe`  |
| 1246   | No documented layout | `075a294681fe`  |
| 1239   | No documented layout | `075a294681fe`  |
| 1230   | No file              | `075a294681fe`  |
| 1226   | No file              | `075a294681fe`  |
| 1220   | No file              | `075a294681fe`  |
| 1217   | No file              | `075a294681fe`  |
| 1211   | No file              | `075a294681fe`  |
| 1210   | No file              | `075a294681fe`  |
| 1208   | No file              | `075a294681fe`  |
| 1203   | No file              | `075a294681fe`  |
| 1197   | No file              | `075a294681fe`  |
| 1194   | No file              | `075a294681fe`  |
| 1192   | No file              | `075a294681fe`  |
| 1187   | No file              | `075a294681fe`  |
| 1183   | No file              | `075a294681fe`  |
| 1177   | No file              | `075a294681fe`  |
| 1173   | No file              | `075a294681fe`  |
| 1167   | No file              | `075a294681fe`  |
| 1164   | No file              | `075a294681fe`  |
| 1156   | No file              | `075a294681fe`  |
| 1149   | No file              | `075a294681fe`  |
| 1144   | No file              | `075a294681fe`  |
| 1137   | No file              | `075a294681fe`  |
| 1132   | No file              | `075a294681fe`  |
| 1127   | No file              | `075a294681fe`  |
| 1122   | No file              | `075a294681fe`  |
| 1118   | No file              | `075a294681fe`  |
| 1114   | No file              | `075a294681fe`  |
| 1109   | No file              | `075a294681fe`  |
| 1102   | No file              | `075a294681fe`  |
| 1096   | No file              | `075a294681fe`  |
| 1088   | No file              | `075a294681fe`  |
| 1081   | No file              | `075a294681fe`  |
| 1076   | No file              | `075a294681fe`  |
| 1069   | No file              | `075a294681fe`  |
| 1064   | No file              | `075a294681fe`  |
| 1058   | No file              | `075a294681fe`  |
| 1051   | No file              | `075a294681fe`  |
| 1044   | No file              | `075a294681fe`  |
| 1036   | No file              | `075a294681fe`  |
| 1026   | No file              | `075a294681fe`  |
| 1016   | No file              | `075a294681fe`  |
| 1009   | No file              | `075a294681fe`  |
| 1005   | No file              | `075a294681fe`  |
| 1000   | No file              | `075a294681fe`  |
| 998    | No file              | `075a294681fe`  |
| 990    | No file              | `075a294681fe`  |
| 979    | No file              | `075a294681fe`  |
| 972    | No file              | `075a294681fe`  |
| 963    | No file              | `075a294681fe`  |
| 955    | No file              | `075a294681fe`  |
| 946    | No file              | `075a294681fe`  |
| 938    | No file              | `075a294681fe`  |
| 927    | No file              | `075a294681fe`  |
| 911    | No file              | `075a294681fe`  |
| 904    | No file              | `075a294681fe`  |
| 899    | No file              | `075a294681fe`  |
| 894    | No file              | `075a294681fe`  |
| 885    | No file              | `075a294681fe`  |
| 879    | No file              | `075a294681fe`  |
| 872    | No file              | `075a294681fe`  |
| 864    | No file              | `075a294681fe`  |
| 855    | No file              | `075a294681fe`  |
| 853    | No file              | `075a294681fe`  |
| 845    | No file              | `075a294681fe`  |
| 837    | No file              | `075a294681fe`  |
| 829    | No file              | `075a294681fe`  |
| 822    | No file              | `075a294681fe`  |
| 814    | No file              | `075a294681fe`  |
| 805    | No file              | `075a294681fe`  |
| 794    | No file              | `075a294681fe`  |
| 787    | No file              | `075a294681fe`  |
| 780    | No file              | `075a294681fe`  |
| 771    | No file              | `075a294681fe`  |
| 760    | No file              | `075a294681fe`  |
| 748    | No file              | `075a294681fe`  |
| 741    | No file              | `075a294681fe`  |
| 736    | No file              | `075a294681fe`  |
| 731    | No file              | `075a294681fe`  |
| 723    | No file              | `075a294681fe`  |
| 711    | No file              | `075a294681fe`  |
| 707    | No file              | `075a294681fe`  |
| 697    | No file              | `075a294681fe`  |
| 689    | No file              | `075a294681fe`  |
| 683    | No file              | `075a294681fe`  |
| 678    | No file              | `075a294681fe`  |
| 670    | No file              | `075a294681fe`  |
| 661    | No file              | `075a294681fe`  |
| 656    | No file              | `075a294681fe`  |
| 652    | No file              | `075a294681fe`  |
| 643    | No file              | `075a294681fe`  |
| 637    | No file              | `075a294681fe`  |
| 630    | No file              | `075a294681fe`  |
| 627    | No file              | `075a294681fe`  |
| 621    | No file              | `075a294681fe`  |
| 617    | No file              | `075a294681fe`  |
| 615    | No file              | `075a294681fe`  |
| 606    | No file              | `075a294681fe`  |
| 599    | No file              | `075a294681fe`  |
| 592    | No file              | `075a294681fe`  |
| 586    | No file              | `075a294681fe`  |
| 577    | No file              | `075a294681fe`  |
| 569    | No file              | `075a294681fe`  |
| 561    | No file              | `075a294681fe`  |
| 554    | No file              | `075a294681fe`  |
| 542    | No file              | `075a294681fe`  |
| 532    | No file              | `075a294681fe`  |
| 531    | No file              | `075a294681fe`  |
| 526    | No file              | `075a294681fe`  |
| 521    | No file              | `075a294681fe`  |
| 517    | No file              | `075a294681fe`  |
| 510    | No file              | `075a294681fe`  |
| 508    | No file              | `075a294681fe`  |
| 504    | No file              | `075a294681fe`  |
| 497    | No file              | `075a294681fe`  |
| 491    | No file              | `075a294681fe`  |
| 485    | No file              | `075a294681fe`  |
| 478    | No file              | `075a294681fe`  |
| 472    | No file              | `075a294681fe`  |
| 466    | No file              | `075a294681fe`  |
| 457    | No file              | `075a294681fe`  |
| 452    | No file              | `075a294681fe`  |
| 449    | No file              | `075a294681fe`  |
| 435    | No file              | `075a294681fe`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Name (LOC type `6`, `str_id4=0`) and title (`str_id4=1`) per character; without one the Korean `characterstatic.dbss` name and title show |
| `stringtable.bss`     | Optional | Key hashes of the First Mate skill texts (`LUA_CAPTAIN_SAILOR_PRESET_SKILL_DESC_*`, LOC type `37`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                 | Type                             | Field                         | Notes                                                            |
| ---------------------- | -------------------------------- | ----------------------------- | ---------------------------------------------------------------- |
| `+0x00`                | char[4]                          | magic                         | `PABR`                                                           |
| `+0x04`                | u32                              | sailor_count                  | Rows in the sailor list; observed `230` (23 sailors x 10 levels) |
| `+0x08`                | Employee Row[sailor_count]       | sailor_rows                   | Employee Row, `job` `0`                                          |
| `sailor_rows+0x00`     | u32                              | first_mate_count              | Rows in the First Mate list; observed `6`                        |
| `sailor_rows+0x04`     | Employee Row[first_mate_count]   | first_mate_rows               | Employee Row, `job` `1`, level `1` only                          |
| `first_mate_rows+0x00` | u32[16]                          | unknown_after_first_mate_rows | Sixteen u32 values, see Open Questions                           |
| `first_mate_rows+0x40` | String Table                     | string_table                  | Counted icon paths, the shared PABR tail                         |
| `string_table+0x00`    | u32                              | table_start                   | String table offset                                              |
| `string_table+0x04`    | u32                              | zero                          | `0`                                                              |

The string table is the same tail as in `npcsimply.bss` and `exploration.bss`: `u32 count`, then per entry `u8 is_wide`, `u32 byte_length` and the text (UTF-16LE when wide). All 29 observed entries are wide icon paths such as `Icon/New_Icon/11_Employee/Employee_59228.dds`. The parser checks that the two lists plus the 64-byte block end exactly where the trailer says the string table starts.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of entries   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

### Employee Row (130 bytes)

| Offset  | Type          | Field          | Notes                                                                 |
| ------- | ------------- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u8            | job            | `0` Sailor, `1` First Mate, see Job                                   |
| `+0x01` | u16           | level          | `1` to `10` for sailors, `1` for First Mates                          |
| `+0x03` | u16           | employee_key   | Sailor type, `1` to `29`; with `level` the row key                    |
| `+0x05` | Ability[19]   | abilities      | Ability slots: type, value. See Abilities                             |
| `+0x64` | u32           | weight         | Weight in 1/10,000 LT (`2,000,000` = 200 LT), same at every level     |
| `+0x68` | u32           | cabin_cost     | Cabin Cost, `3` to `13` for sailors, `0` for First Mates              |
| `+0x6C` | u32           | appetite       | Appetite, `80`, `100`, `120` or `150`, same at every level            |
| `+0x70` | u32           | max_condition  | Condition (max), grows with level (sailor 23: `46` at level 1 to `100` at level 10) |
| `+0x74` | u32           | unknown_74     | Always `5`                                                            |
| `+0x78` | u32           | icon_index     | Zero-based index into the string table                                |
| `+0x7C` | u16           | character_id   | Character key: LOC type 6 name/title, and the portrait file name      |
| `+0x7E` | u16           | employee_key_dup | Repeats `+0x03`; the parser rejects a row where it differs          |
| `+0x80` | u16           | unknown_80     | Always `0`                                                            |

The client Lua reads a sailor's key through `getEmployeeKey()`, and that key object answers `getLevel()`, so `employee_key` and `level` together are the client's employee key.

### Ability (5 bytes)

Each of the 19 slots is `u8 type` followed by `u32 value`.

| Offset  | Type | Field | Notes                    |
| ------- | ---- | ----- | ------------------------ |
| `+0x00` | u8   | type  | Ability type, see Abilities |
| `+0x01` | u32  | value | The type's value         |

## Layout 1

On client 1784 a row holds 17 ability slots, so it is 120 bytes and every
field after `abilities` sits 10 bytes earlier. The file has no First Mate
list, and the block before the string table holds 10 u32 values in place of
16. The File Layout and the Employee Row differ from Layout 2.

### File Layout

| Offset                 | Type                       | Field                         | Notes                                                       |
| ---------------------- | -------------------------- | ----------------------------- | ----------------------------------------------------------- |
| `+0x00`                | char[4]                    | magic                         | `PABR`                                                      |
| `+0x04`                | u32                        | sailor_count                  | `230` on client 1784                                        |
| `+0x08`                | Employee Row[sailor_count] | sailor_rows                   |                                                             |
| `sailor_rows+0x00`     | u32[10]                    | unknown_after_first_mate_rows | `5, 0, 5, 0, 300000, 1, 0, 50, 0, 1000` on client 1784: the first 10 values of the Layout 2 block, with `50` in place of `59`; client 1784 has no `first_mate_rows`, the name follows Layout 2 |
| `sailor_rows+0x28`     | String Table               | string_table                  |                                                             |
| `string_table+0x00`    | u32                        | table_start                   |                                                             |
| `string_table+0x04`    | u32                        | zero                          |                                                             |

### Employee Row (120 bytes)

| Offset  | Type        | Field            | Notes |
| ------- | ----------- | ---------------- | ----- |
| `+0x00` | u8          | job              |       |
| `+0x01` | u16         | level            |       |
| `+0x03` | u16         | employee_key     |       |
| `+0x05` | Ability[17] | abilities        |       |
| `+0x5A` | u32         | weight           |       |
| `+0x5E` | u32         | cabin_cost       |       |
| `+0x62` | u32         | appetite         |       |
| `+0x66` | u32         | max_condition    |       |
| `+0x6A` | u32         | unknown_74       |       |
| `+0x6E` | u32         | icon_index       |       |
| `+0x72` | u16         | character_id     |       |
| `+0x74` | u16         | employee_key_dup |       |
| `+0x76` | u16         | unknown_80       |       |

## Abilities

Every observed row has the same types in the same slots:

```text
slot: 0 1 2 3 4  5 6 7 8 9 10 11 12 13 14 15 16 17 18
type: 0 1 2 3 19 4 6 7 8 9 5  19 19 13 14 15 16 17 18
```

Type `19` fills three slots and is always `0`; it is one past the highest type in use and reads as unused. Types `10` to `12` never appear. The table shows only non-zero slots, as `type: value`.

Observed use of each type:

| Type     | Rows with a value                                  | Meaning                                                                 |
| -------- | -------------------------------------------------- | ----------------------------------------------------------------------- |
| `0`-`5`  | none                                               | Unknown; the four resists are candidates                                |
| `6`      | every sailor, `2,000` to `20,000`                  | Endurance (ship Speed); never set on First Mates                        |
| `7`      | every sailor, `2,000` to `16,000`                  | Wits (Acceleration)                                                     |
| `8`      | every sailor, `2,000` to `40,000`                  | Awareness (Turn)                                                        |
| `9`      | every sailor, `2,000` to `40,000`                  | Strength (Brake)                                                        |
| `13`     | none                                               | Patience (cannon reload time); no sailor has it                         |
| `14`     | sailors 5, 8, 15 and 20                            | Focus (cannon accuracy)                                                 |
| `15`     | sailors 5, 8, 15 and 20                            | Force (cannon range)                                                    |
| `16`     | sailors 5, 8, 15 and 20                            | Vision (cannon angle)                                                   |
| `17`     | First Mate Cleia (`62167`), `100,000`              | Parley reduction for bartering, per million: 10%                        |
| `18`     | First Mate Tranan Underfoe (`62168`), `1`          | Ship auto-repair, a flag                                                |

The labels are the Manage Sailors window's (English client), in its order: Endurance, Wits, Awareness, Strength, then the cannon stats Patience, Focus, Force and Vision. Types `6` to `9` and `13` to `16` follow that order. The window Lua fills them from `_speed`, `_accel`, `_turning`, `_break`, `_cannonCoolTime`, `_cannonAccuracy`, `_cannonMaxLength` and `_cannonMaxAngle`, in that order, which gives the cannon stats their meaning. The client keys confirm the order: `PANEL_SAILORMANAGER_SPEED` reads Endurance, `_ACCELATION` Wits, `_CORNERING` Awareness and `_BRAKING` Strength. Type `13` is read as Patience from its place in that order only, since no row sets it. Condition is `PANEL_SAILORMANAGER_LOYALTY` (the Lua reads it through `getMaxLoyalty()`); the window shows it as a bar, `80 / 80`.

The sailor Lua (`panel_window_sailorpresetmanager_all`) picks the First Mate skill text by character key: `62167` shows `LUA_CAPTAIN_SAILOR_PRESET_SKILL_DESC_02` "-10% Parley required for Bartering", `62168` shows `_03` "Auto-repairs ship (requires materials in ship's inventory)" and `62169` (Proix) shows `_01` "Use a slightly improved BreezySail". Cleia's `17: 100000` is that 10%, and Tranan's `18: 1` the switch; Proix has no ability value, so the improved skill lives elsewhere.

The same Lua shows each ship stat as `value x 0.0001` with one decimal and a `%` sign (`string.format("%.1f", _speed * 0.0001) .. "%"`), so a `16000` speed value reads `1.6%`.

## Job

`job` is `0` on all 230 rows of the first list and `1` on all 6 rows of the second. The second list holds exactly the characters whose LOC title is `<First Mate>` (`62167` to `62169`; `62170` to `62172` have no LOC name yet), and the Lua compares `getJob()` with `__eEmployeeJob_ViceCaptain` to mark First Mates. The labels follow the client's `PANEL_SAILORMANAGER_VICECAPTAIN` ("First Mate").

## Reference Rows

| Sailor ID | Level | Character ID | Name            | Title            | Role       | Icon                  |
| --------- | ----- | ------------ | --------------- | ---------------- | ---------- | --------------------- |
| `1`       | 1     | `59053`      | Sailor          | `<Ambitious>`    | Sailor     | `Employee_59053.dds`  |
| `21`      | 1     | `59101`      | Arkahn          | `<Prepared>`     | Sailor     | `Employee_59101.dds`  |
| `23`      | 1     | `59228`      | Pacuna          | `<Always Happy>` | Sailor     | `Employee_59228.dds`  |
| `24`      | 1     | `62167`      | Cleia           | `<First Mate>`   | First Mate | `Employee_62167.dds`  |
| `25`      | 1     | `62168`      | Tranan Underfoe | `<First Mate>`   | First Mate | `Employee_62168.dds`  |

Sailors `1` to `20` share the LOC name "Sailor"; their title is the sailor type the Sailor Preset filter lists (`LUA_SAILOR_PRESET_CATEGORY_FILTER_01` "Ambitious" and on).

## Notes

- Observed decompressed size is `33,465` bytes (client 3458).
- The sailor list runs level by level: all 23 sailors at level 1, then all at level 2, up to level 10. Inside a level the order is keys `23` down to `8`, then `1` to `7`; from level 5 on, key `7` comes right after `8`.
- `icon_index` runs `0` to `28` in the order of the string table, and every icon file is named after the row's character: `Employee_<character_id>.dds` under `ui_texture/icon/new_icon/11_employee/`.
- Ability values do not change with level on any row; only `max_condition` does.
- `employee_key` is not an `employeename.dbss` ID: those 60 names are given names, and nothing ties name `1` (Philav) to sailor `1`.
- The Manage Sailors window reads, besides the ship stats, `getCost()` (Cabin Cost), `getFoodConsume()` (Appetite), `getBodyWeight()` (Weight, formatted by `makeWeightString`), `getMaxLoyalty()` (Condition) and the four resist values (`Resist_Food`, `Resist_Loyalty`, `Resist_OceanCurrent`, `Resist_WindDirection`). The resists are the candidates for the zero ability types.
- Checked in game (2026-10-06):
  - Pacuna (`23`) at level 1: Condition 46, Appetite 80, Cabin Cost 5, Weight 100 LT, Endurance 0.5%, Wits 0.5%, Awareness 0.2%, Strength 0.2%, every cannon stat 0.0%. Her row: `max_condition 46`, `appetite 80`, `cabin_cost 5`, `weight 1,000,000`, `6: 5000, 7: 5000, 8: 2000, 9: 2000`.
  - Level 6 Confident (`9`) and Treasure-Seeking (`7`) sailors: Condition 110, Appetite 100, Cabin Cost 5, Weight 300 LT, as their level 6 rows read. Their ship stats are the level 1 base plus the `employeeexp.bss` growth rolls (see that doc), so the ability values here are base values.
  - Quick Sailor (`5`) at level 1: Condition 80, Appetite 100, Cabin Cost 10, Weight 250 LT, Endurance 0.2%, Wits 1.5%, Awareness 0.2%, Strength 0.2%, Patience 0.0%, Focus 0.2%, Force 2.0%, Vision 6.0%. Its row: `6: 2000, 7: 15000, 8: 2000, 9: 2000, 14: 2000, 15: 20000, 16: 60000`, which names `14` to `16`.
- The ship stats, Weight, Cabin Cost and Appetite also match the sailor table in GrumpyG's [BDO Sailors Guide](https://grumpygreen.cricket/bdo-sailors-guide/), which lists each plain sailor by title. All 20 match on Speed, Acceleration, Turn, Brake, Weight and Cabin Cost; Appetite matches on 19; the guide gives Treasure-Seeking (`7`) 110, but the game shows 100, as this file does. The guide's titles map to keys as: Ambitious `1`, Diligent `2`, Innocent `3`, Enamored `4`, Quick `5`, Calculating `6`, Treasure-Seeking `7`, Realistic `8`, Confident `9`, Tenacious `10`, Honest `11`, Tough `12`, Strong `13`, Experienced `14`, Curious `15`, Dreaming of a Full Haul `16`, Powerful `17`, Born-in-the-Sea `18`, Smart `19`, Quick-Witted `20`.

## Open Questions

### Field `unknown_74`

`5` on every row; nothing in the window matches it yet.

### The 64-Byte Block

Between the First Mate list and the string table sit sixteen u32 values: `5, 0, 5, 0, 300000, 1, 0, 59, 0, 1000, 5000, 2, 10000, 3, 10, 180`. They may be crew-wide constants such as recovery amounts or fishing timers; no reader in the sailor Lua points at them.
