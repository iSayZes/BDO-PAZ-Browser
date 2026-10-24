# `siegeinfo.bss` Format

## Purpose

The areas of the Conquest War (siege) region map, one row per colour of
`ui_texture/minimap/area/siegemap.bmp`: the colour, a copy of it, whether
the area is a siege area and the territory it belongs to. Client 3482 has
six rows: one per territory from Balenos to Valencia and the `c8c8c8`
row with no territory. The rows open like the 9-byte rows of
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md) and its siblings,
with a u8 and a u16 territory key in place of their last u8.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ------- | --------- |
| 1      | 1749 and later | 3483    | `siegeinfo.bss` | 86    | 6 Row   | 11        |

| Layout | File            | Known        | Unknown      |
| ------ | --------------- | ------------ | ------------ |
| 1      | `siegeinfo.bss` | 74 B (86.0%) | 12 B (14.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `236aa431b337`  |
| 3482   | Layout 1             | `236aa431b337`  |
| 3474   | Layout 1             | `236aa431b337`  |
| 3473   | Layout 1             | `236aa431b337`  |
| 3464   | Layout 1             | `236aa431b337`  |
| 3458   | Layout 1             | `236aa431b337`  |
| 3454   | Layout 1             | `236aa431b337`  |
| 3444   | Layout 1             | `236aa431b337`  |
| 3435   | Layout 1             | `236aa431b337`  |
| 3426   | Layout 1             | `236aa431b337`  |
| 3418   | Layout 1             | `236aa431b337`  |
| 3412   | Layout 1             | `236aa431b337`  |
| 3402   | Layout 1             | `236aa431b337`  |
| 3396   | Layout 1             | `236aa431b337`  |
| 3387   | Layout 1             | `236aa431b337`  |
| 3381   | Layout 1             | `236aa431b337`  |
| 3373   | Layout 1             | `236aa431b337`  |
| 3364   | Layout 1             | `236aa431b337`  |
| 3356   | Layout 1             | `236aa431b337`  |
| 3349   | Layout 1             | `236aa431b337`  |
| 3342   | Layout 1             | `236aa431b337`  |
| 3335   | Layout 1             | `236aa431b337`  |
| 3326   | Layout 1             | `236aa431b337`  |
| 3321   | Layout 1             | `236aa431b337`  |
| 3314   | Layout 1             | `236aa431b337`  |
| 3303   | Layout 1             | `236aa431b337`  |
| 3302   | Layout 1             | `236aa431b337`  |
| 3293   | Layout 1             | `236aa431b337`  |
| 3283   | Layout 1             | `236aa431b337`  |
| 3275   | Layout 1             | `236aa431b337`  |
| 3267   | Layout 1             | `236aa431b337`  |
| 3258   | Layout 1             | `236aa431b337`  |
| 3251   | Layout 1             | `236aa431b337`  |
| 3242   | Layout 1             | `236aa431b337`  |
| 3235   | Layout 1             | `236aa431b337`  |
| 3229   | Layout 1             | `236aa431b337`  |
| 3212   | Layout 1             | `236aa431b337`  |
| 3203   | Layout 1             | `236aa431b337`  |
| 3193   | Layout 1             | `236aa431b337`  |
| 3186   | Layout 1             | `236aa431b337`  |
| 3177   | Layout 1             | `236aa431b337`  |
| 3169   | Layout 1             | `236aa431b337`  |
| 3158   | Layout 1             | `236aa431b337`  |
| 3151   | Layout 1             | `236aa431b337`  |
| 3144   | Layout 1             | `236aa431b337`  |
| 3133   | Layout 1             | `236aa431b337`  |
| 3125   | Layout 1             | `236aa431b337`  |
| 3118   | Layout 1             | `236aa431b337`  |
| 3111   | Layout 1             | `236aa431b337`  |
| 3103   | Layout 1             | `236aa431b337`  |
| 3095   | Layout 1             | `236aa431b337`  |
| 3086   | Layout 1             | `236aa431b337`  |
| 3072   | Layout 1             | `236aa431b337`  |
| 3062   | Layout 1             | `236aa431b337`  |
| 3052   | Layout 1             | `236aa431b337`  |
| 3045   | Layout 1             | `236aa431b337`  |
| 3037   | Layout 1             | `236aa431b337`  |
| 3030   | Layout 1             | `236aa431b337`  |
| 3021   | Layout 1             | `236aa431b337`  |
| 3012   | Layout 1             | `236aa431b337`  |
| 3002   | Layout 1             | `236aa431b337`  |
| 2995   | Layout 1             | `236aa431b337`  |
| 2987   | Layout 1             | `236aa431b337`  |
| 2978   | Layout 1             | `236aa431b337`  |
| 2970   | Layout 1             | `236aa431b337`  |
| 2959   | Layout 1             | `236aa431b337`  |
| 2951   | Layout 1             | `236aa431b337`  |
| 2942   | Layout 1             | `236aa431b337`  |
| 2935   | Layout 1             | `236aa431b337`  |
| 2932   | Layout 1             | `236aa431b337`  |
| 2923   | Layout 1             | `236aa431b337`  |
| 2919   | Layout 1             | `236aa431b337`  |
| 2907   | Layout 1             | `236aa431b337`  |
| 2900   | Layout 1             | `236aa431b337`  |
| 2891   | Layout 1             | `236aa431b337`  |
| 2882   | Layout 1             | `236aa431b337`  |
| 2872   | Layout 1             | `236aa431b337`  |
| 2863   | Layout 1             | `236aa431b337`  |
| 2855   | Layout 1             | `236aa431b337`  |
| 2849   | Layout 1             | `236aa431b337`  |
| 2844   | Layout 1             | `236aa431b337`  |
| 2834   | Layout 1             | `236aa431b337`  |
| 2825   | Layout 1             | `236aa431b337`  |
| 2819   | Layout 1             | `236aa431b337`  |
| 2811   | Layout 1             | `236aa431b337`  |
| 2803   | Layout 1             | `236aa431b337`  |
| 2794   | Layout 1             | `236aa431b337`  |
| 2783   | Layout 1             | `236aa431b337`  |
| 2774   | Layout 1             | `236aa431b337`  |
| 2765   | Layout 1             | `236aa431b337`  |
| 2756   | Layout 1             | `236aa431b337`  |
| 2750   | Layout 1             | `236aa431b337`  |
| 2743   | Layout 1             | `236aa431b337`  |
| 2736   | Layout 1             | `236aa431b337`  |
| 2726   | Layout 1             | `236aa431b337`  |
| 2717   | Layout 1             | `236aa431b337`  |
| 2709   | Layout 1             | `236aa431b337`  |
| 2703   | Layout 1             | `236aa431b337`  |
| 2695   | Layout 1             | `236aa431b337`  |
| 2684   | Layout 1             | `236aa431b337`  |
| 2672   | Layout 1             | `236aa431b337`  |
| 2665   | Layout 1             | `236aa431b337`  |
| 2657   | Layout 1             | `236aa431b337`  |
| 2649   | Layout 1             | `236aa431b337`  |
| 2644   | Layout 1             | `236aa431b337`  |
| 2637   | Layout 1             | `236aa431b337`  |
| 2629   | Layout 1             | `236aa431b337`  |
| 2619   | Layout 1             | `236aa431b337`  |
| 2612   | Layout 1             | `236aa431b337`  |
| 2606   | Layout 1             | `236aa431b337`  |
| 2602   | Layout 1             | `236aa431b337`  |
| 2601   | Layout 1             | `236aa431b337`  |
| 2592   | Layout 1             | `236aa431b337`  |
| 2583   | Layout 1             | `236aa431b337`  |
| 2575   | Layout 1             | `236aa431b337`  |
| 2567   | Layout 1             | `236aa431b337`  |
| 2560   | Layout 1             | `236aa431b337`  |
| 2553   | Layout 1             | `236aa431b337`  |
| 2545   | Layout 1             | `236aa431b337`  |
| 2538   | Layout 1             | `236aa431b337`  |
| 2529   | Layout 1             | `236aa431b337`  |
| 2519   | Layout 1             | `236aa431b337`  |
| 2513   | Layout 1             | `236aa431b337`  |
| 2510   | Layout 1             | `236aa431b337`  |
| 2507   | Layout 1             | `236aa431b337`  |
| 2503   | Layout 1             | `236aa431b337`  |
| 2498   | Layout 1             | `236aa431b337`  |
| 2492   | Layout 1             | `236aa431b337`  |
| 2487   | Layout 1             | `236aa431b337`  |
| 2480   | Layout 1             | `236aa431b337`  |
| 2474   | Layout 1             | `236aa431b337`  |
| 2468   | Layout 1             | `236aa431b337`  |
| 2460   | Layout 1             | `236aa431b337`  |
| 2453   | Layout 1             | `236aa431b337`  |
| 2444   | Layout 1             | `236aa431b337`  |
| 2438   | Layout 1             | `236aa431b337`  |
| 2434   | Layout 1             | `236aa431b337`  |
| 2429   | Layout 1             | `236aa431b337`  |
| 2421   | Layout 1             | `236aa431b337`  |
| 2414   | Layout 1             | `236aa431b337`  |
| 2407   | Layout 1             | `236aa431b337`  |
| 2401   | Layout 1             | `236aa431b337`  |
| 2397   | Layout 1             | `236aa431b337`  |
| 2393   | Layout 1             | `236aa431b337`  |
| 2384   | Layout 1             | `236aa431b337`  |
| 2378   | Layout 1             | `236aa431b337`  |
| 2372   | Layout 1             | `236aa431b337`  |
| 2358   | Layout 1             | `236aa431b337`  |
| 2352   | Layout 1             | `236aa431b337`  |
| 2347   | Layout 1             | `236aa431b337`  |
| 2343   | Layout 1             | `236aa431b337`  |
| 2335   | Layout 1             | `236aa431b337`  |
| 2327   | Layout 1             | `236aa431b337`  |
| 2324   | Layout 1             | `236aa431b337`  |
| 2319   | Layout 1             | `236aa431b337`  |
| 2313   | Layout 1             | `236aa431b337`  |
| 2308   | Layout 1             | `236aa431b337`  |
| 2302   | Layout 1             | `236aa431b337`  |
| 2295   | Layout 1             | `236aa431b337`  |
| 2290   | Layout 1             | `236aa431b337`  |
| 2284   | Layout 1             | `236aa431b337`  |
| 2276   | Layout 1             | `236aa431b337`  |
| 2269   | Layout 1             | `236aa431b337`  |
| 2259   | Layout 1             | `236aa431b337`  |
| 2250   | Layout 1             | `236aa431b337`  |
| 2243   | Layout 1             | `236aa431b337`  |
| 2235   | Layout 1             | `236aa431b337`  |
| 2229   | Layout 1             | `236aa431b337`  |
| 2224   | Layout 1             | `236aa431b337`  |
| 2218   | Layout 1             | `236aa431b337`  |
| 2215   | Layout 1             | `236aa431b337`  |
| 2207   | Layout 1             | `236aa431b337`  |
| 2203   | Layout 1             | `236aa431b337`  |
| 2196   | Layout 1             | `236aa431b337`  |
| 2192   | Layout 1             | `236aa431b337`  |
| 2189   | Layout 1             | `236aa431b337`  |
| 2183   | Layout 1             | `236aa431b337`  |
| 2179   | Layout 1             | `236aa431b337`  |
| 2171   | Layout 1             | `236aa431b337`  |
| 2163   | Layout 1             | `236aa431b337`  |
| 2156   | Layout 1             | `236aa431b337`  |
| 2151   | Layout 1             | `236aa431b337`  |
| 2147   | Layout 1             | `236aa431b337`  |
| 2142   | Layout 1             | `236aa431b337`  |
| 2138   | Layout 1             | `236aa431b337`  |
| 2134   | Layout 1             | `236aa431b337`  |
| 2130   | Layout 1             | `236aa431b337`  |
| 2122   | Layout 1             | `236aa431b337`  |
| 2107   | Layout 1             | `236aa431b337`  |
| 2098   | Layout 1             | `236aa431b337`  |
| 2089   | Layout 1             | `236aa431b337`  |
| 2081   | Layout 1             | `236aa431b337`  |
| 2073   | Layout 1             | `236aa431b337`  |
| 2067   | Layout 1             | `236aa431b337`  |
| 2063   | Layout 1             | `236aa431b337`  |
| 2059   | Layout 1             | `236aa431b337`  |
| 2052   | Layout 1             | `236aa431b337`  |
| 2044   | Layout 1             | `236aa431b337`  |
| 2039   | Layout 1             | `236aa431b337`  |
| 2032   | Layout 1             | `236aa431b337`  |
| 2025   | Layout 1             | `236aa431b337`  |
| 2011   | Layout 1             | `236aa431b337`  |
| 2005   | Layout 1             | `236aa431b337`  |
| 2000   | Layout 1             | `236aa431b337`  |
| 1996   | Layout 1             | `236aa431b337`  |
| 1991   | Layout 1             | `236aa431b337`  |
| 1985   | Layout 1             | `236aa431b337`  |
| 1980   | Layout 1             | `236aa431b337`  |
| 1969   | Layout 1             | `236aa431b337`  |
| 1964   | Layout 1             | `236aa431b337`  |
| 1958   | Layout 1             | `236aa431b337`  |
| 1950   | Layout 1             | `236aa431b337`  |
| 1945   | Layout 1             | `236aa431b337`  |
| 1937   | Layout 1             | `236aa431b337`  |
| 1933   | Layout 1             | `236aa431b337`  |
| 1927   | Layout 1             | `236aa431b337`  |
| 1921   | Layout 1             | `236aa431b337`  |
| 1914   | Layout 1             | `236aa431b337`  |
| 1908   | Layout 1             | `236aa431b337`  |
| 1897   | Layout 1             | `236aa431b337`  |
| 1892   | Layout 1             | `236aa431b337`  |
| 1886   | Layout 1             | `236aa431b337`  |
| 1881   | Layout 1             | `236aa431b337`  |
| 1871   | Layout 1             | `236aa431b337`  |
| 1866   | Layout 1             | `236aa431b337`  |
| 1862   | Layout 1             | `236aa431b337`  |
| 1854   | Layout 1             | `236aa431b337`  |
| 1846   | Layout 1             | `236aa431b337`  |
| 1838   | Layout 1             | `236aa431b337`  |
| 1832   | Layout 1             | `236aa431b337`  |
| 1826   | Layout 1             | `236aa431b337`  |
| 1822   | Layout 1             | `236aa431b337`  |
| 1818   | Layout 1             | `236aa431b337`  |
| 1804   | Layout 1             | `236aa431b337`  |
| 1794   | Layout 1             | `236aa431b337`  |
| 1790   | Layout 1             | `236aa431b337`  |
| 1784   | Layout 1             | `236aa431b337`  |
| 1774   | Layout 1             | `236aa431b337`  |
| 1771   | Layout 1             | `236aa431b337`  |
| 1762   | Layout 1             | `236aa431b337`  |
| 1759   | Layout 1             | `236aa431b337`  |
| 1754   | Layout 1             | `236aa431b337`  |
| 1749   | Layout 1             | `236aa431b337`  |
| 1743   | No documented layout | `236aa431b337`  |
| 1737   | No documented layout | `236aa431b337`  |
| 1731   | No documented layout | `236aa431b337`  |
| 1725   | No documented layout | `236aa431b337`  |
| 1717   | No documented layout | `236aa431b337`  |
| 1710   | No documented layout | `236aa431b337`  |
| 1704   | No documented layout | `236aa431b337`  |
| 1698   | No documented layout | `236aa431b337`  |
| 1690   | No documented layout | `236aa431b337`  |
| 1685   | No documented layout | `236aa431b337`  |
| 1680   | No documented layout | `236aa431b337`  |
| 1674   | No documented layout | `236aa431b337`  |
| 1668   | No documented layout | `236aa431b337`  |
| 1659   | No documented layout | `236aa431b337`  |
| 1649   | No documented layout | `236aa431b337`  |
| 1642   | No documented layout | `236aa431b337`  |
| 1636   | No documented layout | `236aa431b337`  |
| 1628   | No documented layout | `236aa431b337`  |
| 1622   | No documented layout | `236aa431b337`  |
| 1614   | No documented layout | `236aa431b337`  |
| 1608   | No documented layout | `236aa431b337`  |
| 1602   | No documented layout | `236aa431b337`  |
| 1598   | No documented layout | `236aa431b337`  |
| 1594   | No documented layout | `236aa431b337`  |
| 1590   | No documented layout | `236aa431b337`  |
| 1587   | No documented layout | `236aa431b337`  |
| 1584   | No documented layout | `236aa431b337`  |
| 1579   | No documented layout | `236aa431b337`  |
| 1572   | No documented layout | `236aa431b337`  |
| 1565   | No documented layout | `236aa431b337`  |
| 1559   | No documented layout | `236aa431b337`  |
| 1554   | No documented layout | `236aa431b337`  |
| 1547   | No documented layout | `236aa431b337`  |
| 1537   | No documented layout | `236aa431b337`  |
| 1529   | No documented layout | `236aa431b337`  |
| 1524   | No documented layout | `236aa431b337`  |
| 1519   | No documented layout | `236aa431b337`  |
| 1509   | No documented layout | `236aa431b337`  |
| 1506   | No documented layout | `236aa431b337`  |
| 1504   | No documented layout | `236aa431b337`  |
| 1500   | No documented layout | `236aa431b337`  |
| 1493   | No documented layout | `236aa431b337`  |
| 1489   | No documented layout | `236aa431b337`  |
| 1485   | No documented layout | `236aa431b337`  |
| 1481   | No documented layout | `236aa431b337`  |
| 1474   | No documented layout | `236aa431b337`  |
| 1466   | No documented layout | `236aa431b337`  |
| 1462   | No documented layout | `236aa431b337`  |
| 1459   | No documented layout | `236aa431b337`  |
| 1453   | No documented layout | `236aa431b337`  |
| 1450   | No documented layout | `236aa431b337`  |
| 1445   | No documented layout | `236aa431b337`  |
| 1439   | No documented layout | `236aa431b337`  |
| 1433   | No documented layout | `236aa431b337`  |
| 1430   | No documented layout | `236aa431b337`  |
| 1426   | No documented layout | `236aa431b337`  |
| 1421   | No documented layout | `236aa431b337`  |
| 1417   | No documented layout | `236aa431b337`  |
| 1416   | No documented layout | `236aa431b337`  |
| 1409   | No documented layout | `236aa431b337`  |
| 1405   | No documented layout | `236aa431b337`  |
| 1401   | No documented layout | `236aa431b337`  |
| 1396   | No documented layout | `236aa431b337`  |
| 1391   | No documented layout | `236aa431b337`  |
| 1390   | No documented layout | `236aa431b337`  |
| 1386   | No documented layout | `236aa431b337`  |
| 1381   | No documented layout | `236aa431b337`  |
| 1379   | No documented layout | `236aa431b337`  |
| 1372   | No documented layout | `236aa431b337`  |
| 1366   | No documented layout | `236aa431b337`  |
| 1364   | No documented layout | `236aa431b337`  |
| 1363   | No documented layout | `236aa431b337`  |
| 1360   | No documented layout | `236aa431b337`  |
| 1358   | No documented layout | `236aa431b337`  |
| 1355   | No documented layout | `236aa431b337`  |
| 1351   | No documented layout | `236aa431b337`  |
| 1348   | No documented layout | `236aa431b337`  |
| 1346   | No documented layout | `236aa431b337`  |
| 1341   | No documented layout | `236aa431b337`  |
| 1340   | No documented layout | `236aa431b337`  |
| 1338   | No documented layout | `236aa431b337`  |
| 1335   | No documented layout | `236aa431b337`  |
| 1333   | No documented layout | `236aa431b337`  |
| 1329   | No documented layout | `236aa431b337`  |
| 1327   | No documented layout | `236aa431b337`  |
| 1324   | No documented layout | `236aa431b337`  |
| 1321   | No documented layout | `236aa431b337`  |
| 1319   | No documented layout | `236aa431b337`  |
| 1318   | No documented layout | `236aa431b337`  |
| 1316   | No documented layout | `236aa431b337`  |
| 1313   | No documented layout | `236aa431b337`  |
| 1311   | No documented layout | `236aa431b337`  |
| 1309   | No documented layout | `236aa431b337`  |
| 1304   | No documented layout | `236aa431b337`  |
| 1292   | No documented layout | `236aa431b337`  |
| 1286   | No documented layout | `236aa431b337`  |
| 1280   | No documented layout | `236aa431b337`  |
| 1276   | No documented layout | `236aa431b337`  |
| 1267   | No documented layout | `236aa431b337`  |
| 1261   | No documented layout | `236aa431b337`  |
| 1256   | No documented layout | `236aa431b337`  |
| 1250   | No documented layout | `236aa431b337`  |
| 1246   | No documented layout | `236aa431b337`  |
| 1239   | No documented layout | `236aa431b337`  |
| 1230   | No documented layout | `236aa431b337`  |
| 1226   | No documented layout | `236aa431b337`  |
| 1220   | No documented layout | `236aa431b337`  |
| 1217   | No documented layout | `236aa431b337`  |
| 1211   | No documented layout | `236aa431b337`  |
| 1210   | No documented layout | `236aa431b337`  |
| 1208   | No documented layout | `236aa431b337`  |
| 1203   | No documented layout | `236aa431b337`  |
| 1197   | No documented layout | `236aa431b337`  |
| 1194   | No documented layout | `236aa431b337`  |
| 1192   | No documented layout | `236aa431b337`  |
| 1187   | No documented layout | `236aa431b337`  |
| 1183   | No documented layout | `236aa431b337`  |
| 1177   | No documented layout | `236aa431b337`  |
| 1173   | No documented layout | `236aa431b337`  |
| 1167   | No documented layout | `236aa431b337`  |
| 1164   | No documented layout | `236aa431b337`  |
| 1156   | No documented layout | `236aa431b337`  |
| 1149   | No documented layout | `236aa431b337`  |
| 1144   | No documented layout | `236aa431b337`  |
| 1137   | No documented layout | `236aa431b337`  |
| 1132   | No documented layout | `236aa431b337`  |
| 1127   | No documented layout | `236aa431b337`  |
| 1122   | No documented layout | `236aa431b337`  |
| 1118   | No documented layout | `236aa431b337`  |
| 1114   | No documented layout | `236aa431b337`  |
| 1109   | No documented layout | `236aa431b337`  |
| 1102   | No file              | `236aa431b337`  |
| 1096   | No file              | `236aa431b337`  |
| 1088   | No file              | `236aa431b337`  |
| 1081   | No file              | `236aa431b337`  |
| 1076   | No file              | `236aa431b337`  |
| 1069   | No file              | `236aa431b337`  |
| 1064   | No file              | `236aa431b337`  |
| 1058   | No file              | `236aa431b337`  |
| 1051   | No file              | `236aa431b337`  |
| 1044   | No file              | `236aa431b337`  |
| 1036   | No file              | `236aa431b337`  |
| 1026   | No file              | `236aa431b337`  |
| 1016   | No file              | `236aa431b337`  |
| 1009   | No file              | `236aa431b337`  |
| 1005   | No file              | `236aa431b337`  |
| 1000   | No file              | `236aa431b337`  |
| 998    | No file              | `236aa431b337`  |
| 990    | No file              | `236aa431b337`  |
| 979    | No file              | `236aa431b337`  |
| 972    | No file              | `236aa431b337`  |
| 963    | No file              | `236aa431b337`  |
| 955    | No file              | `236aa431b337`  |
| 946    | No file              | `236aa431b337`  |
| 938    | No file              | `236aa431b337`  |
| 927    | No file              | `236aa431b337`  |
| 911    | No file              | `236aa431b337`  |
| 904    | No file              | `236aa431b337`  |
| 899    | No file              | `236aa431b337`  |
| 894    | No file              | `236aa431b337`  |
| 885    | No file              | `236aa431b337`  |
| 879    | No file              | `236aa431b337`  |
| 872    | No file              | `236aa431b337`  |
| 864    | No file              | `236aa431b337`  |
| 855    | No file              | `236aa431b337`  |
| 853    | No file              | `236aa431b337`  |
| 845    | No file              | `236aa431b337`  |
| 837    | No file              | `236aa431b337`  |
| 829    | No documented layout | `236aa431b337`  |
| 822    | No documented layout | `236aa431b337`  |
| 814    | No documented layout | `236aa431b337`  |
| 805    | No documented layout | `236aa431b337`  |
| 794    | No documented layout | `236aa431b337`  |
| 787    | No documented layout | `236aa431b337`  |
| 780    | No documented layout | `236aa431b337`  |
| 771    | No documented layout | `236aa431b337`  |
| 760    | No documented layout | `236aa431b337`  |
| 748    | No documented layout | `236aa431b337`  |
| 741    | No documented layout | `236aa431b337`  |
| 736    | No documented layout | `236aa431b337`  |
| 731    | No documented layout | `236aa431b337`  |
| 723    | No documented layout | `236aa431b337`  |
| 711    | No documented layout | `236aa431b337`  |
| 707    | No documented layout | `236aa431b337`  |
| 697    | No documented layout | `236aa431b337`  |
| 689    | No documented layout | `236aa431b337`  |
| 683    | No documented layout | `236aa431b337`  |
| 678    | No documented layout | `236aa431b337`  |
| 670    | No documented layout | `236aa431b337`  |
| 661    | No documented layout | `236aa431b337`  |
| 656    | No documented layout | `236aa431b337`  |
| 652    | No documented layout | `236aa431b337`  |
| 643    | No documented layout | `236aa431b337`  |
| 637    | No documented layout | `236aa431b337`  |
| 630    | No documented layout | `236aa431b337`  |
| 627    | No documented layout | `236aa431b337`  |
| 621    | No documented layout | `236aa431b337`  |
| 617    | No documented layout | `236aa431b337`  |
| 615    | No documented layout | `236aa431b337`  |
| 606    | No documented layout | `236aa431b337`  |
| 599    | No documented layout | `236aa431b337`  |
| 592    | No documented layout | `236aa431b337`  |
| 586    | No documented layout | `236aa431b337`  |
| 577    | No documented layout | `236aa431b337`  |
| 569    | No documented layout | `236aa431b337`  |
| 561    | No documented layout | `236aa431b337`  |
| 554    | No documented layout | `236aa431b337`  |
| 542    | No documented layout | `236aa431b337`  |
| 532    | No documented layout | `236aa431b337`  |
| 531    | No documented layout | `236aa431b337`  |
| 526    | No documented layout | `236aa431b337`  |
| 521    | No documented layout | `236aa431b337`  |
| 517    | No documented layout | `236aa431b337`  |
| 510    | No documented layout | `236aa431b337`  |
| 508    | No documented layout | `236aa431b337`  |
| 504    | No documented layout | `236aa431b337`  |
| 497    | No documented layout | `236aa431b337`  |
| 491    | No documented layout | `236aa431b337`  |
| 485    | No documented layout | `236aa431b337`  |
| 478    | No documented layout | `236aa431b337`  |
| 472    | No documented layout | `236aa431b337`  |
| 466    | No documented layout | `236aa431b337`  |
| 457    | No documented layout | `236aa431b337`  |
| 452    | No documented layout | `236aa431b337`  |
| 449    | No documented layout | `236aa431b337`  |
| 435    | No documented layout | `236aa431b337`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (11 bytes)

| Offset  | Type     | Field         | Notes                                                                      |
| ------- | -------- | ------------- | -------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color     | Region map colour, stored blue, green, red; unique per row. See Map Colours |
| `+0x03` | u8       | unknown_03    | Always `0`                                                                 |
| `+0x04` | bytes[3] | map_color_dup | Equals `map_color` on every row; see Field Names                           |
| `+0x07` | u8       | unknown_07    | Always `0`                                                                 |
| `+0x08` | u8       | is_siege      | `1` on the five territory rows, `0` on the `c8c8c8` row                    |
| `+0x09` | i16      | territory_key | `territoryinfo.bss` key, LOC type 12 name; `-1` on the `c8c8c8` row        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`. The `.rid`
position is the colour's place in `siegemap.bmp.rid`, which lists the six
colours in the same order as this file.

| `map_color` | `is_siege` | `territory_key` | Position in `.rid` |
| ----------- | ---------- | --------------- | ------------------ |
| `c8c8c8`    | 0          | -1              | 1                  |
| `323264`    | 1          | 4 Valencia      | 2                  |
| `643232`    | 1          | 3 Mediah        | 3                  |
| `0a0a64`    | 1          | 2 Calpheon      | 4                  |
| `0a640a`    | 1          | 1 Serendia      | 5                  |
| `640a0a`    | 1          | 0 Balenos       | 6                  |

## Field Names

The `Siege_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B`, `IsSiege` and `TerritoryKey`
and six rows. The file is byte-identical on clients 1784 and 3482, and
every sheet row matches one file row by its colour (6 of 6): `B`, `G`, `R`
are the three `map_color` bytes in file order, and `IsSiege` and
`TerritoryKey` (`<null>` on the `200, 200, 200` row) are the last two
fields. The sheet lists the rows in another order (territory 0 first).

The 2016 `gc::SiegeInfo` starts with `pa::Color _colorKey` (members `b`,
`g`, `r`, `a`) and holds `bool _canSiegeInstall`; it has no territory key
yet. So the row is the colour the table is keyed by, then the struct's own
`_colorKey` (`map_color_dup`, with `unknown_07` its `a` byte) and its
members packed. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `siegemap.bmp.rid` lists exactly the six `map_color` values.

## Notes

- The file is byte-identical on clients 1784 and 3482. Clients 1230 to
  1636 hold a row that no layout here reads yet.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `map_color` as `rrggbb`, `is_siege`
  and the territory with its name.
