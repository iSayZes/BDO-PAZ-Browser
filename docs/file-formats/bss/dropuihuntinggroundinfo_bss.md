# `dropuihuntinggroundinfo.bss` Format

## Purpose

The hunting grounds of the drop item window (Monster Zone Info): one
variable-length row per zone with its region tab, filter categories, Korean
name, monsters, repeat and sudden quests, drop items, tags, regions, titles,
navigation position, recommended and Total Stat AP / DP, node and the Max AP
Limit. LOC type 116 names the zones by key.

`worldmapmonster.dbss` points at these keys from its hunting zone markers (see
[`worldmapmonster_dbss.md`](../dbss/worldmapmonster_dbss.md) Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes  | Records                | Row bytes                  |
| ------ | -------------- | ----------------------------- | ------ | ---------------------- | -------------------------- |
| 1      | 3321 and later | `dropuihuntinggroundinfo.bss` | 28,350 | 112 Hunting Ground Row | 103 to 325, 218 on average |

| Layout | File                          | Known             | Unknown    |
| ------ | ----------------------------- | ----------------- | ---------- |
| 1      | `dropuihuntinggroundinfo.bss` | 28,350 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `0e670167704f`  |
| 3482   | Layout 1             | `0e670167704f`  |
| 3474   | Layout 1             | `0e670167704f`  |
| 3473   | Layout 1             | `0e670167704f`  |
| 3464   | Layout 1             | `0e670167704f`  |
| 3458   | Layout 1             | `0e670167704f`  |
| 3454   | Layout 1             | `0e670167704f`  |
| 3444   | Layout 1             | `0e670167704f`  |
| 3435   | Layout 1             | `0e670167704f`  |
| 3426   | Layout 1             | `0e670167704f`  |
| 3418   | Layout 1             | `0e670167704f`  |
| 3412   | Layout 1             | `0e670167704f`  |
| 3402   | Layout 1             | `0e670167704f`  |
| 3396   | Layout 1             | `0e670167704f`  |
| 3387   | Layout 1             | `0e670167704f`  |
| 3381   | Layout 1             | `0e670167704f`  |
| 3373   | Layout 1             | `0e670167704f`  |
| 3364   | Layout 1             | `0e670167704f`  |
| 3356   | Layout 1             | `0e670167704f`  |
| 3349   | Layout 1             | `0e670167704f`  |
| 3342   | Layout 1             | `0e670167704f`  |
| 3335   | Layout 1             | `0e670167704f`  |
| 3326   | Layout 1             | `0e670167704f`  |
| 3321   | Layout 1             | `0e670167704f`  |
| 3314   | No documented layout | `0e670167704f`  |
| 3303   | No documented layout | `0e670167704f`  |
| 3302   | No documented layout | `0e670167704f`  |
| 3293   | No documented layout | `0e670167704f`  |
| 3283   | No documented layout | `0e670167704f`  |
| 3275   | No documented layout | `0e670167704f`  |
| 3267   | No documented layout | `0e670167704f`  |
| 3258   | No documented layout | `0e670167704f`  |
| 3251   | No documented layout | `0e670167704f`  |
| 3242   | No documented layout | `0e670167704f`  |
| 3235   | No documented layout | `0e670167704f`  |
| 3229   | No documented layout | `0e670167704f`  |
| 3212   | No documented layout | `0e670167704f`  |
| 3203   | No documented layout | `0e670167704f`  |
| 3193   | No documented layout | `0e670167704f`  |
| 3186   | No documented layout | `0e670167704f`  |
| 3177   | No documented layout | `0e670167704f`  |
| 3169   | No documented layout | `0e670167704f`  |
| 3158   | No documented layout | `0e670167704f`  |
| 3151   | No documented layout | `0e670167704f`  |
| 3144   | No documented layout | `0e670167704f`  |
| 3133   | No documented layout | `0e670167704f`  |
| 3125   | No documented layout | `0e670167704f`  |
| 3118   | No documented layout | `0e670167704f`  |
| 3111   | No documented layout | `0e670167704f`  |
| 3103   | No documented layout | `0e670167704f`  |
| 3095   | No documented layout | `0e670167704f`  |
| 3086   | No documented layout | `0e670167704f`  |
| 3072   | No documented layout | `0e670167704f`  |
| 3062   | No documented layout | `0e670167704f`  |
| 3052   | No documented layout | `0e670167704f`  |
| 3045   | No documented layout | `0e670167704f`  |
| 3037   | No documented layout | `0e670167704f`  |
| 3030   | No documented layout | `0e670167704f`  |
| 3021   | No documented layout | `0e670167704f`  |
| 3012   | No documented layout | `0e670167704f`  |
| 3002   | No documented layout | `0e670167704f`  |
| 2995   | No documented layout | `0e670167704f`  |
| 2987   | No documented layout | `0e670167704f`  |
| 2978   | No documented layout | `0e670167704f`  |
| 2970   | No documented layout | `0e670167704f`  |
| 2959   | No documented layout | `0e670167704f`  |
| 2951   | No documented layout | `0e670167704f`  |
| 2942   | No documented layout | `0e670167704f`  |
| 2935   | No documented layout | `0e670167704f`  |
| 2932   | No documented layout | `0e670167704f`  |
| 2923   | No documented layout | `0e670167704f`  |
| 2919   | No documented layout | `0e670167704f`  |
| 2907   | No documented layout | `0e670167704f`  |
| 2900   | No documented layout | `0e670167704f`  |
| 2891   | No documented layout | `0e670167704f`  |
| 2882   | No documented layout | `0e670167704f`  |
| 2872   | No documented layout | `0e670167704f`  |
| 2863   | No documented layout | `0e670167704f`  |
| 2855   | No documented layout | `0e670167704f`  |
| 2849   | No documented layout | `0e670167704f`  |
| 2844   | No documented layout | `0e670167704f`  |
| 2834   | No documented layout | `0e670167704f`  |
| 2825   | No documented layout | `0e670167704f`  |
| 2819   | No documented layout | `0e670167704f`  |
| 2811   | No documented layout | `0e670167704f`  |
| 2803   | No documented layout | `0e670167704f`  |
| 2794   | No documented layout | `0e670167704f`  |
| 2783   | No documented layout | `0e670167704f`  |
| 2774   | No documented layout | `0e670167704f`  |
| 2765   | No documented layout | `0e670167704f`  |
| 2756   | No documented layout | `0e670167704f`  |
| 2750   | No documented layout | `0e670167704f`  |
| 2743   | No documented layout | `0e670167704f`  |
| 2736   | No documented layout | `0e670167704f`  |
| 2726   | No documented layout | `0e670167704f`  |
| 2717   | No documented layout | `0e670167704f`  |
| 2709   | No documented layout | `0e670167704f`  |
| 2703   | No documented layout | `0e670167704f`  |
| 2695   | No documented layout | `0e670167704f`  |
| 2684   | No documented layout | `0e670167704f`  |
| 2672   | No documented layout | `0e670167704f`  |
| 2665   | No documented layout | `0e670167704f`  |
| 2657   | No documented layout | `0e670167704f`  |
| 2649   | No documented layout | `0e670167704f`  |
| 2644   | No documented layout | `0e670167704f`  |
| 2637   | No documented layout | `0e670167704f`  |
| 2629   | No documented layout | `0e670167704f`  |
| 2619   | No documented layout | `0e670167704f`  |
| 2612   | No documented layout | `0e670167704f`  |
| 2606   | No documented layout | `0e670167704f`  |
| 2602   | No documented layout | `0e670167704f`  |
| 2601   | No documented layout | `0e670167704f`  |
| 2592   | No documented layout | `0e670167704f`  |
| 2583   | No documented layout | `0e670167704f`  |
| 2575   | No documented layout | `0e670167704f`  |
| 2567   | No documented layout | `0e670167704f`  |
| 2560   | No documented layout | `0e670167704f`  |
| 2553   | No documented layout | `0e670167704f`  |
| 2545   | No documented layout | `0e670167704f`  |
| 2538   | No documented layout | `0e670167704f`  |
| 2529   | No documented layout | `0e670167704f`  |
| 2519   | No documented layout | `0e670167704f`  |
| 2513   | No documented layout | `0e670167704f`  |
| 2510   | No documented layout | `0e670167704f`  |
| 2507   | No documented layout | `0e670167704f`  |
| 2503   | No documented layout | `0e670167704f`  |
| 2498   | No documented layout | `0e670167704f`  |
| 2492   | No documented layout | `0e670167704f`  |
| 2487   | No documented layout | `0e670167704f`  |
| 2480   | No documented layout | `0e670167704f`  |
| 2474   | No documented layout | `0e670167704f`  |
| 2468   | No documented layout | `0e670167704f`  |
| 2460   | No documented layout | `0e670167704f`  |
| 2453   | No documented layout | `0e670167704f`  |
| 2444   | No documented layout | `0e670167704f`  |
| 2438   | No documented layout | `0e670167704f`  |
| 2434   | No documented layout | `0e670167704f`  |
| 2429   | No documented layout | `0e670167704f`  |
| 2421   | No documented layout | `0e670167704f`  |
| 2414   | No documented layout | `0e670167704f`  |
| 2407   | No documented layout | `0e670167704f`  |
| 2401   | No documented layout | `0e670167704f`  |
| 2397   | No documented layout | `0e670167704f`  |
| 2393   | No documented layout | `0e670167704f`  |
| 2384   | No documented layout | `0e670167704f`  |
| 2378   | No documented layout | `0e670167704f`  |
| 2372   | No documented layout | `0e670167704f`  |
| 2358   | No documented layout | `0e670167704f`  |
| 2352   | No documented layout | `0e670167704f`  |
| 2347   | No documented layout | `0e670167704f`  |
| 2343   | No documented layout | `0e670167704f`  |
| 2335   | No documented layout | `0e670167704f`  |
| 2327   | No documented layout | `0e670167704f`  |
| 2324   | No documented layout | `0e670167704f`  |
| 2319   | No documented layout | `0e670167704f`  |
| 2313   | No documented layout | `0e670167704f`  |
| 2308   | No documented layout | `0e670167704f`  |
| 2302   | No documented layout | `0e670167704f`  |
| 2295   | No documented layout | `0e670167704f`  |
| 2290   | No documented layout | `0e670167704f`  |
| 2284   | No documented layout | `0e670167704f`  |
| 2276   | No documented layout | `0e670167704f`  |
| 2269   | No documented layout | `0e670167704f`  |
| 2259   | No documented layout | `0e670167704f`  |
| 2250   | No documented layout | `0e670167704f`  |
| 2243   | No documented layout | `0e670167704f`  |
| 2235   | No documented layout | `0e670167704f`  |
| 2229   | No documented layout | `0e670167704f`  |
| 2224   | No documented layout | `0e670167704f`  |
| 2218   | No documented layout | `0e670167704f`  |
| 2215   | No documented layout | `0e670167704f`  |
| 2207   | No documented layout | `0e670167704f`  |
| 2203   | No documented layout | `0e670167704f`  |
| 2196   | No documented layout | `0e670167704f`  |
| 2192   | No documented layout | `0e670167704f`  |
| 2189   | No documented layout | `0e670167704f`  |
| 2183   | No documented layout | `0e670167704f`  |
| 2179   | No documented layout | `0e670167704f`  |
| 2171   | No documented layout | `0e670167704f`  |
| 2163   | No documented layout | `0e670167704f`  |
| 2156   | No documented layout | `0e670167704f`  |
| 2151   | No documented layout | `0e670167704f`  |
| 2147   | No documented layout | `0e670167704f`  |
| 2142   | No documented layout | `0e670167704f`  |
| 2138   | No documented layout | `0e670167704f`  |
| 2134   | No documented layout | `0e670167704f`  |
| 2130   | No documented layout | `0e670167704f`  |
| 2122   | No documented layout | `0e670167704f`  |
| 2107   | No documented layout | `0e670167704f`  |
| 2098   | No documented layout | `0e670167704f`  |
| 2089   | No documented layout | `0e670167704f`  |
| 2081   | No documented layout | `0e670167704f`  |
| 2073   | No documented layout | `0e670167704f`  |
| 2067   | No documented layout | `0e670167704f`  |
| 2063   | No documented layout | `0e670167704f`  |
| 2059   | No documented layout | `0e670167704f`  |
| 2052   | No documented layout | `0e670167704f`  |
| 2044   | No documented layout | `0e670167704f`  |
| 2039   | No documented layout | `0e670167704f`  |
| 2032   | No documented layout | `0e670167704f`  |
| 2025   | No documented layout | `0e670167704f`  |
| 2011   | No documented layout | `0e670167704f`  |
| 2005   | No documented layout | `0e670167704f`  |
| 2000   | No documented layout | `0e670167704f`  |
| 1996   | No documented layout | `0e670167704f`  |
| 1991   | No documented layout | `0e670167704f`  |
| 1985   | No documented layout | `0e670167704f`  |
| 1980   | No documented layout | `0e670167704f`  |
| 1969   | No documented layout | `0e670167704f`  |
| 1964   | No documented layout | `0e670167704f`  |
| 1958   | No documented layout | `0e670167704f`  |
| 1950   | No documented layout | `0e670167704f`  |
| 1945   | No documented layout | `0e670167704f`  |
| 1937   | No documented layout | `0e670167704f`  |
| 1933   | No documented layout | `0e670167704f`  |
| 1927   | No documented layout | `0e670167704f`  |
| 1921   | No documented layout | `0e670167704f`  |
| 1914   | No documented layout | `0e670167704f`  |
| 1908   | No file              | `0e670167704f`  |
| 1897   | No file              | `0e670167704f`  |
| 1892   | No file              | `0e670167704f`  |
| 1886   | No file              | `0e670167704f`  |
| 1881   | No file              | `0e670167704f`  |
| 1871   | No file              | `0e670167704f`  |
| 1866   | No file              | `0e670167704f`  |
| 1862   | No file              | `0e670167704f`  |
| 1854   | No file              | `0e670167704f`  |
| 1846   | No file              | `0e670167704f`  |
| 1838   | No file              | `0e670167704f`  |
| 1832   | No file              | `0e670167704f`  |
| 1826   | No file              | `0e670167704f`  |
| 1822   | No file              | `0e670167704f`  |
| 1818   | No file              | `0e670167704f`  |
| 1804   | No file              | `0e670167704f`  |
| 1794   | No file              | `0e670167704f`  |
| 1790   | No file              | `0e670167704f`  |
| 1784   | No file              | `0e670167704f`  |
| 1774   | No file              | `0e670167704f`  |
| 1771   | No file              | `0e670167704f`  |
| 1762   | No file              | `0e670167704f`  |
| 1759   | No file              | `0e670167704f`  |
| 1754   | No file              | `0e670167704f`  |
| 1749   | No file              | `0e670167704f`  |
| 1743   | No file              | `0e670167704f`  |
| 1737   | No file              | `0e670167704f`  |
| 1731   | No file              | `0e670167704f`  |
| 1725   | No file              | `0e670167704f`  |
| 1717   | No file              | `0e670167704f`  |
| 1710   | No file              | `0e670167704f`  |
| 1704   | No file              | `0e670167704f`  |
| 1698   | No file              | `0e670167704f`  |
| 1690   | No file              | `0e670167704f`  |
| 1685   | No file              | `0e670167704f`  |
| 1680   | No file              | `0e670167704f`  |
| 1674   | No file              | `0e670167704f`  |
| 1668   | No file              | `0e670167704f`  |
| 1659   | No file              | `0e670167704f`  |
| 1649   | No file              | `0e670167704f`  |
| 1642   | No file              | `0e670167704f`  |
| 1636   | No file              | `0e670167704f`  |
| 1628   | No file              | `0e670167704f`  |
| 1622   | No file              | `0e670167704f`  |
| 1614   | No file              | `0e670167704f`  |
| 1608   | No file              | `0e670167704f`  |
| 1602   | No file              | `0e670167704f`  |
| 1598   | No file              | `0e670167704f`  |
| 1594   | No file              | `0e670167704f`  |
| 1590   | No file              | `0e670167704f`  |
| 1587   | No file              | `0e670167704f`  |
| 1584   | No file              | `0e670167704f`  |
| 1579   | No file              | `0e670167704f`  |
| 1572   | No file              | `0e670167704f`  |
| 1565   | No file              | `0e670167704f`  |
| 1559   | No file              | `0e670167704f`  |
| 1554   | No file              | `0e670167704f`  |
| 1547   | No file              | `0e670167704f`  |
| 1537   | No file              | `0e670167704f`  |
| 1529   | No file              | `0e670167704f`  |
| 1524   | No file              | `0e670167704f`  |
| 1519   | No file              | `0e670167704f`  |
| 1509   | No file              | `0e670167704f`  |
| 1506   | No file              | `0e670167704f`  |
| 1504   | No file              | `0e670167704f`  |
| 1500   | No file              | `0e670167704f`  |
| 1493   | No file              | `0e670167704f`  |
| 1489   | No file              | `0e670167704f`  |
| 1485   | No file              | `0e670167704f`  |
| 1481   | No file              | `0e670167704f`  |
| 1474   | No file              | `0e670167704f`  |
| 1466   | No file              | `0e670167704f`  |
| 1462   | No file              | `0e670167704f`  |
| 1459   | No file              | `0e670167704f`  |
| 1453   | No file              | `0e670167704f`  |
| 1450   | No file              | `0e670167704f`  |
| 1445   | No file              | `0e670167704f`  |
| 1439   | No file              | `0e670167704f`  |
| 1433   | No file              | `0e670167704f`  |
| 1430   | No file              | `0e670167704f`  |
| 1426   | No file              | `0e670167704f`  |
| 1421   | No file              | `0e670167704f`  |
| 1417   | No file              | `0e670167704f`  |
| 1416   | No file              | `0e670167704f`  |
| 1409   | No file              | `0e670167704f`  |
| 1405   | No file              | `0e670167704f`  |
| 1401   | No file              | `0e670167704f`  |
| 1396   | No file              | `0e670167704f`  |
| 1391   | No file              | `0e670167704f`  |
| 1390   | No file              | `0e670167704f`  |
| 1386   | No file              | `0e670167704f`  |
| 1381   | No file              | `0e670167704f`  |
| 1379   | No file              | `0e670167704f`  |
| 1372   | No file              | `0e670167704f`  |
| 1366   | No file              | `0e670167704f`  |
| 1364   | No file              | `0e670167704f`  |
| 1363   | No file              | `0e670167704f`  |
| 1360   | No file              | `0e670167704f`  |
| 1358   | No file              | `0e670167704f`  |
| 1355   | No file              | `0e670167704f`  |
| 1351   | No file              | `0e670167704f`  |
| 1348   | No file              | `0e670167704f`  |
| 1346   | No file              | `0e670167704f`  |
| 1341   | No file              | `0e670167704f`  |
| 1340   | No file              | `0e670167704f`  |
| 1338   | No file              | `0e670167704f`  |
| 1335   | No file              | `0e670167704f`  |
| 1333   | No file              | `0e670167704f`  |
| 1329   | No file              | `0e670167704f`  |
| 1327   | No file              | `0e670167704f`  |
| 1324   | No file              | `0e670167704f`  |
| 1321   | No file              | `0e670167704f`  |
| 1319   | No file              | `0e670167704f`  |
| 1318   | No file              | `0e670167704f`  |
| 1316   | No file              | `0e670167704f`  |
| 1313   | No file              | `0e670167704f`  |
| 1311   | No file              | `0e670167704f`  |
| 1309   | No file              | `0e670167704f`  |
| 1304   | No file              | `0e670167704f`  |
| 1292   | No file              | `0e670167704f`  |
| 1286   | No file              | `0e670167704f`  |
| 1280   | No file              | `0e670167704f`  |
| 1276   | No file              | `0e670167704f`  |
| 1267   | No file              | `0e670167704f`  |
| 1261   | No file              | `0e670167704f`  |
| 1256   | No file              | `0e670167704f`  |
| 1250   | No file              | `0e670167704f`  |
| 1246   | No file              | `0e670167704f`  |
| 1239   | No file              | `0e670167704f`  |
| 1230   | No file              | `0e670167704f`  |
| 1226   | No file              | `0e670167704f`  |
| 1220   | No file              | `0e670167704f`  |
| 1217   | No file              | `0e670167704f`  |
| 1211   | No file              | `0e670167704f`  |
| 1210   | No file              | `0e670167704f`  |
| 1208   | No file              | `0e670167704f`  |
| 1203   | No file              | `0e670167704f`  |
| 1197   | No file              | `0e670167704f`  |
| 1194   | No file              | `0e670167704f`  |
| 1192   | No file              | `0e670167704f`  |
| 1187   | No file              | `0e670167704f`  |
| 1183   | No file              | `0e670167704f`  |
| 1177   | No file              | `0e670167704f`  |
| 1173   | No file              | `0e670167704f`  |
| 1167   | No file              | `0e670167704f`  |
| 1164   | No file              | `0e670167704f`  |
| 1156   | No file              | `0e670167704f`  |
| 1149   | No file              | `0e670167704f`  |
| 1144   | No file              | `0e670167704f`  |
| 1137   | No file              | `0e670167704f`  |
| 1132   | No file              | `0e670167704f`  |
| 1127   | No file              | `0e670167704f`  |
| 1122   | No file              | `0e670167704f`  |
| 1118   | No file              | `0e670167704f`  |
| 1114   | No file              | `0e670167704f`  |
| 1109   | No file              | `0e670167704f`  |
| 1102   | No file              | `0e670167704f`  |
| 1096   | No file              | `0e670167704f`  |
| 1088   | No file              | `0e670167704f`  |
| 1081   | No file              | `0e670167704f`  |
| 1076   | No file              | `0e670167704f`  |
| 1069   | No file              | `0e670167704f`  |
| 1064   | No file              | `0e670167704f`  |
| 1058   | No file              | `0e670167704f`  |
| 1051   | No file              | `0e670167704f`  |
| 1044   | No file              | `0e670167704f`  |
| 1036   | No file              | `0e670167704f`  |
| 1026   | No file              | `0e670167704f`  |
| 1016   | No file              | `0e670167704f`  |
| 1009   | No file              | `0e670167704f`  |
| 1005   | No file              | `0e670167704f`  |
| 1000   | No file              | `0e670167704f`  |
| 998    | No file              | `0e670167704f`  |
| 990    | No file              | `0e670167704f`  |
| 979    | No file              | `0e670167704f`  |
| 972    | No file              | `0e670167704f`  |
| 963    | No file              | `0e670167704f`  |
| 955    | No file              | `0e670167704f`  |
| 946    | No file              | `0e670167704f`  |
| 938    | No file              | `0e670167704f`  |
| 927    | No file              | `0e670167704f`  |
| 911    | No file              | `0e670167704f`  |
| 904    | No file              | `0e670167704f`  |
| 899    | No file              | `0e670167704f`  |
| 894    | No file              | `0e670167704f`  |
| 885    | No file              | `0e670167704f`  |
| 879    | No file              | `0e670167704f`  |
| 872    | No file              | `0e670167704f`  |
| 864    | No file              | `0e670167704f`  |
| 855    | No file              | `0e670167704f`  |
| 853    | No file              | `0e670167704f`  |
| 845    | No file              | `0e670167704f`  |
| 837    | No file              | `0e670167704f`  |
| 829    | No file              | `0e670167704f`  |
| 822    | No file              | `0e670167704f`  |
| 814    | No file              | `0e670167704f`  |
| 805    | No file              | `0e670167704f`  |
| 794    | No file              | `0e670167704f`  |
| 787    | No file              | `0e670167704f`  |
| 780    | No file              | `0e670167704f`  |
| 771    | No file              | `0e670167704f`  |
| 760    | No file              | `0e670167704f`  |
| 748    | No file              | `0e670167704f`  |
| 741    | No file              | `0e670167704f`  |
| 736    | No file              | `0e670167704f`  |
| 731    | No file              | `0e670167704f`  |
| 723    | No file              | `0e670167704f`  |
| 711    | No file              | `0e670167704f`  |
| 707    | No file              | `0e670167704f`  |
| 697    | No file              | `0e670167704f`  |
| 689    | No file              | `0e670167704f`  |
| 683    | No file              | `0e670167704f`  |
| 678    | No file              | `0e670167704f`  |
| 670    | No file              | `0e670167704f`  |
| 661    | No file              | `0e670167704f`  |
| 656    | No file              | `0e670167704f`  |
| 652    | No file              | `0e670167704f`  |
| 643    | No file              | `0e670167704f`  |
| 637    | No file              | `0e670167704f`  |
| 630    | No file              | `0e670167704f`  |
| 627    | No file              | `0e670167704f`  |
| 621    | No file              | `0e670167704f`  |
| 617    | No file              | `0e670167704f`  |
| 615    | No file              | `0e670167704f`  |
| 606    | No file              | `0e670167704f`  |
| 599    | No file              | `0e670167704f`  |
| 592    | No file              | `0e670167704f`  |
| 586    | No file              | `0e670167704f`  |
| 577    | No file              | `0e670167704f`  |
| 569    | No file              | `0e670167704f`  |
| 561    | No file              | `0e670167704f`  |
| 554    | No file              | `0e670167704f`  |
| 542    | No file              | `0e670167704f`  |
| 532    | No file              | `0e670167704f`  |
| 531    | No file              | `0e670167704f`  |
| 526    | No file              | `0e670167704f`  |
| 521    | No file              | `0e670167704f`  |
| 517    | No file              | `0e670167704f`  |
| 510    | No file              | `0e670167704f`  |
| 508    | No file              | `0e670167704f`  |
| 504    | No file              | `0e670167704f`  |
| 497    | No file              | `0e670167704f`  |
| 491    | No file              | `0e670167704f`  |
| 485    | No file              | `0e670167704f`  |
| 478    | No file              | `0e670167704f`  |
| 472    | No file              | `0e670167704f`  |
| 466    | No file              | `0e670167704f`  |
| 457    | No file              | `0e670167704f`  |
| 452    | No file              | `0e670167704f`  |
| 449    | No file              | `0e670167704f`  |
| 435    | No file              | `0e670167704f`  |

<!-- versions:end -->

## Companion Files

| File                                                          | Required | Role                                                      |
| ------------------------------------------------------------- | -------- | --------------------------------------------------------- |
| [`dropuimaincategoryinfo.bss`](dropuimaincategoryinfo_bss.md) | Optional | Region tabs: tab key -> territory, for the Region column  |
| [`dropuitaginfo.bss`](dropuitaginfo_bss.md)                   | Optional | Tag pill colours for the Tags column                      |
| `languagedata_en.loc`                                         | Optional | Zone names (116), categories (115), tags (117), territories (12), monsters (6), items (0), quests (18), regions (17), titles (1), nodes (29) |

[`dropuisubcategoryinfo.bss`](dropuisubcategoryinfo_bss.md) holds the filter
categories of `sub_category_keys`; the handler names them from LOC type 115
alone.

`dropuiurlinfo.bss` (20 bytes) is an empty PABR table on client 3458 (count
0); see [empty](empty_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block with variable-length rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`).

| Offset              | Type                      | Field              | Notes                                        |
| ------------------- | ------------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                       | count              | Number of rows; 112 on client 3458           |
| `+0x08`             | Hunting Ground Row[count] | rows               | Variable-length rows, read in order          |
| `rows+0x00`         | String Table              | string_table       | 112 wide strings, one Korean name per row    |
| `string_table+0x00` | u32                       | string_table_start | Where the rows end (`0x5FD8` on client 3458) |
| `string_table+0x04` | u32                       | zero               | Always `0`                                   |

Rows are sorted by key, which runs from 0 to 119 with gaps (2, 4, 7, 8, 14,
15, 16 and 49 are missing).

### Hunting Ground Row (variable: 85 bytes + lists)

A list is a u32 count followed by that many values.

| Offset                   | Type                        | Field                    | Notes                                                                 |
| ------------------------ | --------------------------- | ------------------------ | --------------------------------------------------------------------- |
| `+0x00`                  | u32                         | key                      | Hunting ground key; LOC type 116 `str_id1`                            |
| `+0x04`                  | u32                         | main_category_key        | Region tab, 1 to 13, a `dropuimaincategoryinfo.bss` key               |
| `+0x08`                  | u32                         | sub_category_key_count   | Number of `sub_category_keys`                                         |
| `+0x0C`                  | u32[sub_category_key_count] | sub_category_keys        | Filter categories (`dropuisubcategoryinfo.bss` keys, LOC type 115); empty on 13 rows |
| `sub_category_keys+0x00` | u32                         | name_ref                 | String table index of the Korean name; unique per row                 |
| `sub_category_keys+0x04` | u32                         | monster_id_count         | Number of `monster_ids`                                               |
| `sub_category_keys+0x08` | u16[monster_id_count]       | monster_ids              | Character IDs (LOC type 6), 1 to 17 per row                           |
| `monster_ids+0x00`       | u32                         | repeat_quest_key_count   | Number of `repeat_quest_keys`                                         |
| `monster_ids+0x04`       | u32[repeat_quest_key_count] | repeat_quest_keys        | Packed quest keys: low u16 quest chain, high u16 quest (LOC type 18 `str_id1` / `str_id2`), as in `allquestlist.bss`; repeat, daily and weekly quests |
| `repeat_quest_keys+0x00` | u32                         | sudden_quest_key_count   | Number of `sudden_quest_keys`                                         |
| `repeat_quest_keys+0x04` | u32[sudden_quest_key_count] | sudden_quest_keys        | Packed like `repeat_quest_keys`; subjugation and season quests, on 27 rows (13 of them in Valencia) |
| `sudden_quest_keys+0x00` | u32                         | drop_item_count          | Number of `drop_item_ids`                                             |
| `sudden_quest_keys+0x04` | u32[drop_item_count]        | drop_item_ids            | Item IDs (LOC type 0), plain IDs with no enchant level, in the window's display order |
| `drop_item_ids+0x00`     | u32                         | tag_key_count            | Number of `tag_keys`                                                  |
| `drop_item_ids+0x04`     | u32[tag_key_count]          | tag_keys                 | Tag keys, LOC type 117 (`#LotsOfMobs`, `#CombatEXP`)                  |
| `tag_keys+0x00`          | u32                         | region_key_count         | Number of `region_keys`                                               |
| `tag_keys+0x04`          | u16[region_key_count]       | region_keys              | Region keys, LOC type 17; a zone can span several regions (Mansha Forest: 289 and 523) |
| `region_keys+0x00`       | u32                         | title_key_count          | Number of `title_keys`                                                |
| `region_keys+0x04`       | u32[title_key_count]        | title_keys               | Titles earned in the zone, LOC type 1 (`Mansha Slayer`)               |
| `title_keys+0x00`        | f32[3]                      | position                 | World position for the navigation guide; `0, 0, 0` on 21 rows         |
| `title_keys+0x0C`        | f32                         | recommended_ap           | The "Recommended AP" of the worldmap marker label                     |
| `title_keys+0x10`        | f32                         | recommended_dp           | Recommended DP                                                        |
| `title_keys+0x14`        | u32                         | node_key                 | `exploration.bss` node key (LOC type 29); `0` on 6 rows               |
| `title_keys+0x18`        | f32                         | total_ap                 | The "AP (Total Stat)" of the worldmap marker label                    |
| `title_keys+0x1C`        | f32                         | total_dp                 | Recommended DP (Total Stat)                                           |
| `title_keys+0x20`        | u32                         | limited_ap               | Max AP Limit                                                          |
| `title_keys+0x24`        | u32                         | limited_ap_apply_percent | Percent of the AP above `limited_ap` that still applies; `0` on 13 rows |
| `title_keys+0x28`        | u8                          | tribe_type               | Monster species, 0 to 4; see `tribe_type` Values                      |

All 112 rows walk to exactly `string_table_start` with this layout on client
3458.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                      |
| ------- | ------------------ | ------------ | ------------------------------------------ |
| `+0x00` | u32                | string_count | 112 on client 3458                         |
| `+0x04` | pstr[string_count] | strings      | Korean zone names; `name_ref` indexes them |

## `tribe_type` Values

The client enum `__eNewTribeType_*`; the drop window labels each value with a
`GAME` sheet string (LOC type 37) and says which Extra AP applies
(`LUA_DROPITEM_<X>_TOOLTIP_DESC`).

| Value | Enum         | Label key                              | Label                 | Rows | Extra AP that applies             |
| ----- | ------------ | -------------------------------------- | --------------------- | ---- | --------------------------------- |
| 0     | `Human`      | `LUA_DROPITEM_HUMAN_TOOLTIP_NAME`      | Humans                | 21   | Extra AP Against Humans           |
| 1     | `NonHuman`   | `LUA_DROPITEM_AIN_TOOLTIP_NAME`        | Demihumans            | 34   | Extra AP Against Demihumans       |
| 2     | `Others`     | `LUA_DROPITEM_NORMAL_TOOLTIP_NAME`     | Normal                | 22   | Extra AP Against Monsters         |
| 3     | `Kamasilvia` | `LUA_DROPITEM_KAMASILVIA_TOOLTIP_NAME` | Kamasylvian Monsters  | 21   | Extra AP Against Kamasylvian Monsters |
| 4     | `Edania`     | `LUA_DROPITEM_EDANIA_TOOLTIP_NAME`     | Edanian Monsters      | 14   | Extra AP Against Edanian Monsters |

The Lua lists the five enum names with their label keys in this order, and the
zones match: `0` bandits, pirates, Abandoned Monastery and the Elvia human
zones; `1` Mansha Forest, Catfishman Camp, Rhutum Outstation; `2` Hexe
Sanctuary, Soldier's Grave, Cyclops Land; `3` Polly's Forest, Navarn Steppe,
Ash Forest, Olun's Valley; `4` Aetherion Castle to Scales of Judgment.

## Notes

- Since client 3464 every one of the 112 names opens with a level, in the
  Korean string table (`Lv.74 아레시온 신전`) and in LOC type 116
  (`Lv. 74 Aresion Temple`). The node names (LOC type 29) carry none. The
  handler shows the names as stored.
- The drop item window Lua (`window/dropitem/panel_window_renewdropitem_all_1`)
  reads the row through `ToClient_getDropUIHuntingGroundStaticStatusWrapper`;
  its getters match the fields: `getMainCategoryKey`,
  `getSubCategoryKeyByIndex`, `getName`, `getRepeatQuestNoByIndex`,
  `getSuddenQuestNoByIndex`, `getDropItemStaticStatusWrapper`,
  `getTagKeyByIndex`, `getRegionKeyRawByIndex`,
  `getDropTitleStaticStatusWrapper`, `getWayPointKey`, `getLimitedAP`,
  `getLAPApplyPercent` and `getTribeType`.
- The Max AP Limit text is `LUA_DROPINFO_MAXAP` (`{appoint}({appercent}%)`)
  or, when the percent is 0, `LUA_DROPINFO_MAXAP_NONE_PERCENT` (`{appoint}
  effective limit`); `LUA_DROPINFO_MAXAP_DESC` explains that only that share of
  the AP above the limit applies.
- The AP values equal the worldmap marker labels of the same zone: Aresion
  Temple stores 415 and 2455, and its marker reads "Recommended AP: 415" and
  "AP (Total Stat): 2455". `limited_ap` sits 30 above `total_ap` on 67 rows
  (2455 -> 2485, 2570 -> 2600).
- LOC type 116 names all 112 rows and has one more key, 49, with no row.
  Every monster, item, tag, region, title, node and quest ID in the file has
  LOC text on client 3458.
- The `CHARACTER_HUNTING_GROUNDS` lookup index inverts `monster_ids`
  (character key -> the keys of the rows that list it), and
  `HUNTING_GROUND_NAME_KR` holds `name_kr` by key, the fallback when LOC type
  116 has no name. The [`monstergroup.dbss`](../dbss/monstergroup_dbss.md) Hunting
  Grounds column reads both and links each zone to its row here.
- `drop_item_ids` holds plain item IDs (`28` Prognyl Silver Bar, `721002`
  Ancient Spirit Dust), not the packed `itemenchant.dbss` key.
- bdo-viewer (built on bdo-data-extractor) counts 105 zones; the file holds
  112 rows.
