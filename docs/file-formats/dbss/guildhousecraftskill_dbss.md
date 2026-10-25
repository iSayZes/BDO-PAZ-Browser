# `guildhousecraftskill.dbss` Format

## Purpose

The guild skills a guild house use grants: one row per house use (a
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key) with up to
five skill numbers. The Guild Shipyard grants Building Boat Lv. 1 and 2, the
specialty packing workshops Local Economy Revitalization, and Storage and
Guild Storage level 2 to 9 grant Ample Storage Lv. 1 to 37 between them.
Companion `guildhousecraftskilloffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes | Records       | Row bytes |
| ------ | -------------- | --------------------------------- | ----- | ------------- | --------- |
| 1      | 1346 and later | `guildhousecraftskill.dbss`       | 384   | 19 Row        | 20        |
| 1      | 1346 and later | `guildhousecraftskilloffset.dbss` | 232   | 19 Offset Row | 12        |

| Layout | File                              | Known          | Unknown     |
| ------ | --------------------------------- | -------------- | ----------- |
| 1      | `guildhousecraftskill.dbss`       | 346 B (90.1%)  | 38 B (9.9%) |
| 1      | `guildhousecraftskilloffset.dbss` | 232 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ef002c91ec73`  |
| 3482   | Layout 1             | `ef002c91ec73`  |
| 3474   | Layout 1             | `ef002c91ec73`  |
| 3473   | Layout 1             | `ef002c91ec73`  |
| 3464   | Layout 1             | `ef002c91ec73`  |
| 3458   | Layout 1             | `ef002c91ec73`  |
| 3454   | Layout 1             | `ef002c91ec73`  |
| 3444   | Layout 1             | `ef002c91ec73`  |
| 3435   | Layout 1             | `ef002c91ec73`  |
| 3426   | Layout 1             | `ef002c91ec73`  |
| 3418   | Layout 1             | `ef002c91ec73`  |
| 3412   | Layout 1             | `ef002c91ec73`  |
| 3402   | Layout 1             | `ef002c91ec73`  |
| 3396   | Layout 1             | `ef002c91ec73`  |
| 3387   | Layout 1             | `ef002c91ec73`  |
| 3381   | Layout 1             | `ef002c91ec73`  |
| 3373   | Layout 1             | `ef002c91ec73`  |
| 3364   | Layout 1             | `ef002c91ec73`  |
| 3356   | Layout 1             | `ef002c91ec73`  |
| 3349   | Layout 1             | `ef002c91ec73`  |
| 3342   | Layout 1             | `ef002c91ec73`  |
| 3335   | Layout 1             | `ef002c91ec73`  |
| 3326   | Layout 1             | `ef002c91ec73`  |
| 3321   | Layout 1             | `ef002c91ec73`  |
| 3314   | Layout 1             | `ef002c91ec73`  |
| 3303   | Layout 1             | `ef002c91ec73`  |
| 3302   | Layout 1             | `ef002c91ec73`  |
| 3293   | Layout 1             | `ef002c91ec73`  |
| 3283   | Layout 1             | `ef002c91ec73`  |
| 3275   | Layout 1             | `ef002c91ec73`  |
| 3267   | Layout 1             | `ef002c91ec73`  |
| 3258   | Layout 1             | `ef002c91ec73`  |
| 3251   | Layout 1             | `ef002c91ec73`  |
| 3242   | Layout 1             | `ef002c91ec73`  |
| 3235   | Layout 1             | `ef002c91ec73`  |
| 3229   | Layout 1             | `ef002c91ec73`  |
| 3212   | Layout 1             | `ef002c91ec73`  |
| 3203   | Layout 1             | `ef002c91ec73`  |
| 3193   | Layout 1             | `ef002c91ec73`  |
| 3186   | Layout 1             | `ef002c91ec73`  |
| 3177   | Layout 1             | `ef002c91ec73`  |
| 3169   | Layout 1             | `ef002c91ec73`  |
| 3158   | Layout 1             | `ef002c91ec73`  |
| 3151   | Layout 1             | `ef002c91ec73`  |
| 3144   | Layout 1             | `ef002c91ec73`  |
| 3133   | Layout 1             | `ef002c91ec73`  |
| 3125   | Layout 1             | `ef002c91ec73`  |
| 3118   | Layout 1             | `ef002c91ec73`  |
| 3111   | Layout 1             | `ef002c91ec73`  |
| 3103   | Layout 1             | `ef002c91ec73`  |
| 3095   | Layout 1             | `ef002c91ec73`  |
| 3086   | Layout 1             | `ef002c91ec73`  |
| 3072   | Layout 1             | `ef002c91ec73`  |
| 3062   | Layout 1             | `ef002c91ec73`  |
| 3052   | Layout 1             | `ef002c91ec73`  |
| 3045   | Layout 1             | `ef002c91ec73`  |
| 3037   | Layout 1             | `ef002c91ec73`  |
| 3030   | Layout 1             | `ef002c91ec73`  |
| 3021   | Layout 1             | `ef002c91ec73`  |
| 3012   | Layout 1             | `ef002c91ec73`  |
| 3002   | Layout 1             | `ef002c91ec73`  |
| 2995   | Layout 1             | `ef002c91ec73`  |
| 2987   | Layout 1             | `ef002c91ec73`  |
| 2978   | Layout 1             | `ef002c91ec73`  |
| 2970   | Layout 1             | `ef002c91ec73`  |
| 2959   | Layout 1             | `ef002c91ec73`  |
| 2951   | Layout 1             | `ef002c91ec73`  |
| 2942   | Layout 1             | `ef002c91ec73`  |
| 2935   | Layout 1             | `ef002c91ec73`  |
| 2932   | Layout 1             | `ef002c91ec73`  |
| 2923   | Layout 1             | `ef002c91ec73`  |
| 2919   | Layout 1             | `ef002c91ec73`  |
| 2907   | Layout 1             | `ef002c91ec73`  |
| 2900   | Layout 1             | `ef002c91ec73`  |
| 2891   | Layout 1             | `ef002c91ec73`  |
| 2882   | Layout 1             | `ef002c91ec73`  |
| 2872   | Layout 1             | `ef002c91ec73`  |
| 2863   | Layout 1             | `ef002c91ec73`  |
| 2855   | Layout 1             | `ef002c91ec73`  |
| 2849   | Layout 1             | `ef002c91ec73`  |
| 2844   | Layout 1             | `ef002c91ec73`  |
| 2834   | Layout 1             | `ef002c91ec73`  |
| 2825   | Layout 1             | `ef002c91ec73`  |
| 2819   | Layout 1             | `ef002c91ec73`  |
| 2811   | Layout 1             | `ef002c91ec73`  |
| 2803   | Layout 1             | `ef002c91ec73`  |
| 2794   | Layout 1             | `ef002c91ec73`  |
| 2783   | Layout 1             | `ef002c91ec73`  |
| 2774   | Layout 1             | `ef002c91ec73`  |
| 2765   | Layout 1             | `ef002c91ec73`  |
| 2756   | Layout 1             | `ef002c91ec73`  |
| 2750   | Layout 1             | `ef002c91ec73`  |
| 2743   | Layout 1             | `ef002c91ec73`  |
| 2736   | Layout 1             | `ef002c91ec73`  |
| 2726   | Layout 1             | `ef002c91ec73`  |
| 2717   | Layout 1             | `ef002c91ec73`  |
| 2709   | Layout 1             | `ef002c91ec73`  |
| 2703   | Layout 1             | `ef002c91ec73`  |
| 2695   | Layout 1             | `ef002c91ec73`  |
| 2684   | Layout 1             | `ef002c91ec73`  |
| 2672   | Layout 1             | `ef002c91ec73`  |
| 2665   | Layout 1             | `ef002c91ec73`  |
| 2657   | Layout 1             | `ef002c91ec73`  |
| 2649   | Layout 1             | `ef002c91ec73`  |
| 2644   | Layout 1             | `ef002c91ec73`  |
| 2637   | Layout 1             | `ef002c91ec73`  |
| 2629   | Layout 1             | `ef002c91ec73`  |
| 2619   | Layout 1             | `ef002c91ec73`  |
| 2612   | Layout 1             | `ef002c91ec73`  |
| 2606   | Layout 1             | `ef002c91ec73`  |
| 2602   | Layout 1             | `ef002c91ec73`  |
| 2601   | Layout 1             | `ef002c91ec73`  |
| 2592   | Layout 1             | `ef002c91ec73`  |
| 2583   | Layout 1             | `ef002c91ec73`  |
| 2575   | Layout 1             | `ef002c91ec73`  |
| 2567   | Layout 1             | `ef002c91ec73`  |
| 2560   | Layout 1             | `ef002c91ec73`  |
| 2553   | Layout 1             | `ef002c91ec73`  |
| 2545   | Layout 1             | `ef002c91ec73`  |
| 2538   | Layout 1             | `ef002c91ec73`  |
| 2529   | Layout 1             | `ef002c91ec73`  |
| 2519   | Layout 1             | `ef002c91ec73`  |
| 2513   | Layout 1             | `ef002c91ec73`  |
| 2510   | Layout 1             | `ef002c91ec73`  |
| 2507   | Layout 1             | `ef002c91ec73`  |
| 2503   | Layout 1             | `ef002c91ec73`  |
| 2498   | Layout 1             | `ef002c91ec73`  |
| 2492   | Layout 1             | `ef002c91ec73`  |
| 2487   | Layout 1             | `ef002c91ec73`  |
| 2480   | Layout 1             | `ef002c91ec73`  |
| 2474   | Layout 1             | `ef002c91ec73`  |
| 2468   | Layout 1             | `ef002c91ec73`  |
| 2460   | Layout 1             | `ef002c91ec73`  |
| 2453   | Layout 1             | `ef002c91ec73`  |
| 2444   | Layout 1             | `ef002c91ec73`  |
| 2438   | Layout 1             | `ef002c91ec73`  |
| 2434   | Layout 1             | `ef002c91ec73`  |
| 2429   | Layout 1             | `ef002c91ec73`  |
| 2421   | Layout 1             | `ef002c91ec73`  |
| 2414   | Layout 1             | `ef002c91ec73`  |
| 2407   | Layout 1             | `ef002c91ec73`  |
| 2401   | Layout 1             | `ef002c91ec73`  |
| 2397   | Layout 1             | `ef002c91ec73`  |
| 2393   | Layout 1             | `ef002c91ec73`  |
| 2384   | Layout 1             | `ef002c91ec73`  |
| 2378   | Layout 1             | `ef002c91ec73`  |
| 2372   | Layout 1             | `ef002c91ec73`  |
| 2358   | Layout 1             | `ef002c91ec73`  |
| 2352   | Layout 1             | `ef002c91ec73`  |
| 2347   | Layout 1             | `ef002c91ec73`  |
| 2343   | Layout 1             | `ef002c91ec73`  |
| 2335   | Layout 1             | `ef002c91ec73`  |
| 2327   | Layout 1             | `ef002c91ec73`  |
| 2324   | Layout 1             | `ef002c91ec73`  |
| 2319   | Layout 1             | `ef002c91ec73`  |
| 2313   | Layout 1             | `ef002c91ec73`  |
| 2308   | Layout 1             | `ef002c91ec73`  |
| 2302   | Layout 1             | `ef002c91ec73`  |
| 2295   | Layout 1             | `ef002c91ec73`  |
| 2290   | Layout 1             | `ef002c91ec73`  |
| 2284   | Layout 1             | `ef002c91ec73`  |
| 2276   | Layout 1             | `ef002c91ec73`  |
| 2269   | Layout 1             | `ef002c91ec73`  |
| 2259   | Layout 1             | `ef002c91ec73`  |
| 2250   | Layout 1             | `ef002c91ec73`  |
| 2243   | Layout 1             | `ef002c91ec73`  |
| 2235   | Layout 1             | `ef002c91ec73`  |
| 2229   | Layout 1             | `ef002c91ec73`  |
| 2224   | Layout 1             | `ef002c91ec73`  |
| 2218   | Layout 1             | `ef002c91ec73`  |
| 2215   | Layout 1             | `ef002c91ec73`  |
| 2207   | Layout 1             | `ef002c91ec73`  |
| 2203   | Layout 1             | `ef002c91ec73`  |
| 2196   | Layout 1             | `ef002c91ec73`  |
| 2192   | Layout 1             | `ef002c91ec73`  |
| 2189   | Layout 1             | `ef002c91ec73`  |
| 2183   | Layout 1             | `ef002c91ec73`  |
| 2179   | Layout 1             | `ef002c91ec73`  |
| 2171   | Layout 1             | `ef002c91ec73`  |
| 2163   | Layout 1             | `ef002c91ec73`  |
| 2156   | Layout 1             | `ef002c91ec73`  |
| 2151   | Layout 1             | `ef002c91ec73`  |
| 2147   | Layout 1             | `ef002c91ec73`  |
| 2142   | Layout 1             | `ef002c91ec73`  |
| 2138   | Layout 1             | `ef002c91ec73`  |
| 2134   | Layout 1             | `ef002c91ec73`  |
| 2130   | Layout 1             | `ef002c91ec73`  |
| 2122   | Layout 1             | `ef002c91ec73`  |
| 2107   | Layout 1             | `ef002c91ec73`  |
| 2098   | Layout 1             | `ef002c91ec73`  |
| 2089   | Layout 1             | `ef002c91ec73`  |
| 2081   | Layout 1             | `ef002c91ec73`  |
| 2073   | Layout 1             | `ef002c91ec73`  |
| 2067   | Layout 1             | `ef002c91ec73`  |
| 2063   | Layout 1             | `ef002c91ec73`  |
| 2059   | Layout 1             | `ef002c91ec73`  |
| 2052   | Layout 1             | `ef002c91ec73`  |
| 2044   | Layout 1             | `ef002c91ec73`  |
| 2039   | Layout 1             | `ef002c91ec73`  |
| 2032   | Layout 1             | `ef002c91ec73`  |
| 2025   | Layout 1             | `ef002c91ec73`  |
| 2011   | Layout 1             | `ef002c91ec73`  |
| 2005   | Layout 1             | `ef002c91ec73`  |
| 2000   | Layout 1             | `ef002c91ec73`  |
| 1996   | Layout 1             | `ef002c91ec73`  |
| 1991   | Layout 1             | `ef002c91ec73`  |
| 1985   | Layout 1             | `ef002c91ec73`  |
| 1980   | Layout 1             | `ef002c91ec73`  |
| 1969   | Layout 1             | `ef002c91ec73`  |
| 1964   | Layout 1             | `ef002c91ec73`  |
| 1958   | Layout 1             | `ef002c91ec73`  |
| 1950   | Layout 1             | `ef002c91ec73`  |
| 1945   | Layout 1             | `ef002c91ec73`  |
| 1937   | Layout 1             | `ef002c91ec73`  |
| 1933   | Layout 1             | `ef002c91ec73`  |
| 1927   | Layout 1             | `ef002c91ec73`  |
| 1921   | Layout 1             | `ef002c91ec73`  |
| 1914   | Layout 1             | `ef002c91ec73`  |
| 1908   | Layout 1             | `ef002c91ec73`  |
| 1897   | Layout 1             | `ef002c91ec73`  |
| 1892   | Layout 1             | `ef002c91ec73`  |
| 1886   | Layout 1             | `ef002c91ec73`  |
| 1881   | Layout 1             | `ef002c91ec73`  |
| 1871   | Layout 1             | `ef002c91ec73`  |
| 1866   | Layout 1             | `ef002c91ec73`  |
| 1862   | Layout 1             | `ef002c91ec73`  |
| 1854   | Layout 1             | `ef002c91ec73`  |
| 1846   | Layout 1             | `ef002c91ec73`  |
| 1838   | Layout 1             | `ef002c91ec73`  |
| 1832   | Layout 1             | `ef002c91ec73`  |
| 1826   | Layout 1             | `ef002c91ec73`  |
| 1822   | Layout 1             | `ef002c91ec73`  |
| 1818   | Layout 1             | `ef002c91ec73`  |
| 1804   | Layout 1             | `ef002c91ec73`  |
| 1794   | Layout 1             | `ef002c91ec73`  |
| 1790   | Layout 1             | `ef002c91ec73`  |
| 1784   | Layout 1             | `ef002c91ec73`  |
| 1774   | Layout 1             | `ef002c91ec73`  |
| 1771   | Layout 1             | `ef002c91ec73`  |
| 1762   | Layout 1             | `ef002c91ec73`  |
| 1759   | Layout 1             | `ef002c91ec73`  |
| 1754   | Layout 1             | `ef002c91ec73`  |
| 1749   | Layout 1             | `ef002c91ec73`  |
| 1743   | Layout 1             | `ef002c91ec73`  |
| 1737   | Layout 1             | `ef002c91ec73`  |
| 1731   | Layout 1             | `ef002c91ec73`  |
| 1725   | Layout 1             | `ef002c91ec73`  |
| 1717   | Layout 1             | `ef002c91ec73`  |
| 1710   | Layout 1             | `ef002c91ec73`  |
| 1704   | Layout 1             | `ef002c91ec73`  |
| 1698   | Layout 1             | `ef002c91ec73`  |
| 1690   | Layout 1             | `ef002c91ec73`  |
| 1685   | Layout 1             | `ef002c91ec73`  |
| 1680   | Layout 1             | `ef002c91ec73`  |
| 1674   | Layout 1             | `ef002c91ec73`  |
| 1668   | Layout 1             | `ef002c91ec73`  |
| 1659   | Layout 1             | `ef002c91ec73`  |
| 1649   | Layout 1             | `ef002c91ec73`  |
| 1642   | Layout 1             | `ef002c91ec73`  |
| 1636   | Layout 1             | `ef002c91ec73`  |
| 1628   | Layout 1             | `ef002c91ec73`  |
| 1622   | Layout 1             | `ef002c91ec73`  |
| 1614   | Layout 1             | `ef002c91ec73`  |
| 1608   | Layout 1             | `ef002c91ec73`  |
| 1602   | Layout 1             | `ef002c91ec73`  |
| 1598   | Layout 1             | `ef002c91ec73`  |
| 1594   | Layout 1             | `ef002c91ec73`  |
| 1590   | Layout 1             | `ef002c91ec73`  |
| 1587   | Layout 1             | `ef002c91ec73`  |
| 1584   | Layout 1             | `ef002c91ec73`  |
| 1579   | Layout 1             | `ef002c91ec73`  |
| 1572   | Layout 1             | `ef002c91ec73`  |
| 1565   | Layout 1             | `ef002c91ec73`  |
| 1559   | Layout 1             | `ef002c91ec73`  |
| 1554   | Layout 1             | `ef002c91ec73`  |
| 1547   | Layout 1             | `ef002c91ec73`  |
| 1537   | Layout 1             | `ef002c91ec73`  |
| 1529   | Layout 1             | `ef002c91ec73`  |
| 1524   | Layout 1             | `ef002c91ec73`  |
| 1519   | Layout 1             | `ef002c91ec73`  |
| 1509   | Layout 1             | `ef002c91ec73`  |
| 1506   | Layout 1             | `ef002c91ec73`  |
| 1504   | Layout 1             | `ef002c91ec73`  |
| 1500   | Layout 1             | `ef002c91ec73`  |
| 1493   | Layout 1             | `ef002c91ec73`  |
| 1489   | Layout 1             | `ef002c91ec73`  |
| 1485   | Layout 1             | `ef002c91ec73`  |
| 1481   | Layout 1             | `ef002c91ec73`  |
| 1474   | Layout 1             | `ef002c91ec73`  |
| 1466   | Layout 1             | `ef002c91ec73`  |
| 1462   | Layout 1             | `ef002c91ec73`  |
| 1459   | Layout 1             | `ef002c91ec73`  |
| 1453   | Layout 1             | `ef002c91ec73`  |
| 1450   | Layout 1             | `ef002c91ec73`  |
| 1445   | Layout 1             | `ef002c91ec73`  |
| 1439   | Layout 1             | `ef002c91ec73`  |
| 1433   | Layout 1             | `ef002c91ec73`  |
| 1430   | Layout 1             | `ef002c91ec73`  |
| 1426   | Layout 1             | `ef002c91ec73`  |
| 1421   | Layout 1             | `ef002c91ec73`  |
| 1417   | Layout 1             | `ef002c91ec73`  |
| 1416   | Layout 1             | `ef002c91ec73`  |
| 1409   | Layout 1             | `ef002c91ec73`  |
| 1405   | Layout 1             | `ef002c91ec73`  |
| 1401   | Layout 1             | `ef002c91ec73`  |
| 1396   | Layout 1             | `ef002c91ec73`  |
| 1391   | Layout 1             | `ef002c91ec73`  |
| 1390   | Layout 1             | `ef002c91ec73`  |
| 1386   | Layout 1             | `ef002c91ec73`  |
| 1381   | Layout 1             | `ef002c91ec73`  |
| 1379   | Layout 1             | `ef002c91ec73`  |
| 1372   | Layout 1             | `ef002c91ec73`  |
| 1366   | Layout 1             | `ef002c91ec73`  |
| 1364   | Layout 1             | `ef002c91ec73`  |
| 1363   | Layout 1             | `ef002c91ec73`  |
| 1360   | Layout 1             | `ef002c91ec73`  |
| 1358   | Layout 1             | `ef002c91ec73`  |
| 1355   | Layout 1             | `ef002c91ec73`  |
| 1351   | Layout 1             | `ef002c91ec73`  |
| 1348   | Layout 1             | `ef002c91ec73`  |
| 1346   | Layout 1             | `ef002c91ec73`  |
| 1341   | No documented layout | `ef002c91ec73`  |
| 1340   | No documented layout | `ef002c91ec73`  |
| 1338   | No documented layout | `ef002c91ec73`  |
| 1335   | No documented layout | `ef002c91ec73`  |
| 1333   | No documented layout | `ef002c91ec73`  |
| 1329   | No documented layout | `ef002c91ec73`  |
| 1327   | No documented layout | `ef002c91ec73`  |
| 1324   | No documented layout | `ef002c91ec73`  |
| 1321   | No documented layout | `ef002c91ec73`  |
| 1319   | No documented layout | `ef002c91ec73`  |
| 1318   | No documented layout | `ef002c91ec73`  |
| 1316   | No documented layout | `ef002c91ec73`  |
| 1313   | No documented layout | `ef002c91ec73`  |
| 1311   | No documented layout | `ef002c91ec73`  |
| 1309   | No documented layout | `ef002c91ec73`  |
| 1304   | No documented layout | `ef002c91ec73`  |
| 1292   | No documented layout | `ef002c91ec73`  |
| 1286   | No file              | `ef002c91ec73`  |
| 1280   | No file              | `ef002c91ec73`  |
| 1276   | No file              | `ef002c91ec73`  |
| 1267   | No file              | `ef002c91ec73`  |
| 1261   | No file              | `ef002c91ec73`  |
| 1256   | No file              | `ef002c91ec73`  |
| 1250   | No file              | `ef002c91ec73`  |
| 1246   | No file              | `ef002c91ec73`  |
| 1239   | No file              | `ef002c91ec73`  |
| 1230   | No file              | `ef002c91ec73`  |
| 1226   | No file              | `ef002c91ec73`  |
| 1220   | No file              | `ef002c91ec73`  |
| 1217   | No file              | `ef002c91ec73`  |
| 1211   | No file              | `ef002c91ec73`  |
| 1210   | No file              | `ef002c91ec73`  |
| 1208   | No file              | `ef002c91ec73`  |
| 1203   | No file              | `ef002c91ec73`  |
| 1197   | No file              | `ef002c91ec73`  |
| 1194   | No file              | `ef002c91ec73`  |
| 1192   | No file              | `ef002c91ec73`  |
| 1187   | No file              | `ef002c91ec73`  |
| 1183   | No file              | `ef002c91ec73`  |
| 1177   | No file              | `ef002c91ec73`  |
| 1173   | No file              | `ef002c91ec73`  |
| 1167   | No file              | `ef002c91ec73`  |
| 1164   | No file              | `ef002c91ec73`  |
| 1156   | No file              | `ef002c91ec73`  |
| 1149   | No file              | `ef002c91ec73`  |
| 1144   | No file              | `ef002c91ec73`  |
| 1137   | No file              | `ef002c91ec73`  |
| 1132   | No file              | `ef002c91ec73`  |
| 1127   | No file              | `ef002c91ec73`  |
| 1122   | No file              | `ef002c91ec73`  |
| 1118   | No file              | `ef002c91ec73`  |
| 1114   | No file              | `ef002c91ec73`  |
| 1109   | No file              | `ef002c91ec73`  |
| 1102   | No file              | `ef002c91ec73`  |
| 1096   | No file              | `ef002c91ec73`  |
| 1088   | No file              | `ef002c91ec73`  |
| 1081   | No file              | `ef002c91ec73`  |
| 1076   | No file              | `ef002c91ec73`  |
| 1069   | No file              | `ef002c91ec73`  |
| 1064   | No file              | `ef002c91ec73`  |
| 1058   | No file              | `ef002c91ec73`  |
| 1051   | No file              | `ef002c91ec73`  |
| 1044   | No file              | `ef002c91ec73`  |
| 1036   | No file              | `ef002c91ec73`  |
| 1026   | No file              | `ef002c91ec73`  |
| 1016   | No file              | `ef002c91ec73`  |
| 1009   | No file              | `ef002c91ec73`  |
| 1005   | No file              | `ef002c91ec73`  |
| 1000   | No file              | `ef002c91ec73`  |
| 998    | No file              | `ef002c91ec73`  |
| 990    | No file              | `ef002c91ec73`  |
| 979    | No file              | `ef002c91ec73`  |
| 972    | No file              | `ef002c91ec73`  |
| 963    | No file              | `ef002c91ec73`  |
| 955    | No file              | `ef002c91ec73`  |
| 946    | No file              | `ef002c91ec73`  |
| 938    | No file              | `ef002c91ec73`  |
| 927    | No file              | `ef002c91ec73`  |
| 911    | No file              | `ef002c91ec73`  |
| 904    | No file              | `ef002c91ec73`  |
| 899    | No file              | `ef002c91ec73`  |
| 894    | No file              | `ef002c91ec73`  |
| 885    | No file              | `ef002c91ec73`  |
| 879    | No file              | `ef002c91ec73`  |
| 872    | No file              | `ef002c91ec73`  |
| 864    | No file              | `ef002c91ec73`  |
| 855    | No file              | `ef002c91ec73`  |
| 853    | No file              | `ef002c91ec73`  |
| 845    | No file              | `ef002c91ec73`  |
| 837    | No file              | `ef002c91ec73`  |
| 829    | No file              | `ef002c91ec73`  |
| 822    | No file              | `ef002c91ec73`  |
| 814    | No file              | `ef002c91ec73`  |
| 805    | No file              | `ef002c91ec73`  |
| 794    | No file              | `ef002c91ec73`  |
| 787    | No file              | `ef002c91ec73`  |
| 780    | No file              | `ef002c91ec73`  |
| 771    | No file              | `ef002c91ec73`  |
| 760    | No file              | `ef002c91ec73`  |
| 748    | No file              | `ef002c91ec73`  |
| 741    | No file              | `ef002c91ec73`  |
| 736    | No file              | `ef002c91ec73`  |
| 731    | No file              | `ef002c91ec73`  |
| 723    | No file              | `ef002c91ec73`  |
| 711    | No file              | `ef002c91ec73`  |
| 707    | No file              | `ef002c91ec73`  |
| 697    | No file              | `ef002c91ec73`  |
| 689    | No file              | `ef002c91ec73`  |
| 683    | No file              | `ef002c91ec73`  |
| 678    | No file              | `ef002c91ec73`  |
| 670    | No file              | `ef002c91ec73`  |
| 661    | No file              | `ef002c91ec73`  |
| 656    | No file              | `ef002c91ec73`  |
| 652    | No file              | `ef002c91ec73`  |
| 643    | No file              | `ef002c91ec73`  |
| 637    | No file              | `ef002c91ec73`  |
| 630    | No file              | `ef002c91ec73`  |
| 627    | No file              | `ef002c91ec73`  |
| 621    | No file              | `ef002c91ec73`  |
| 617    | No file              | `ef002c91ec73`  |
| 615    | No file              | `ef002c91ec73`  |
| 606    | No file              | `ef002c91ec73`  |
| 599    | No file              | `ef002c91ec73`  |
| 592    | No file              | `ef002c91ec73`  |
| 586    | No file              | `ef002c91ec73`  |
| 577    | No file              | `ef002c91ec73`  |
| 569    | No file              | `ef002c91ec73`  |
| 561    | No file              | `ef002c91ec73`  |
| 554    | No file              | `ef002c91ec73`  |
| 542    | No file              | `ef002c91ec73`  |
| 532    | No file              | `ef002c91ec73`  |
| 531    | No file              | `ef002c91ec73`  |
| 526    | No file              | `ef002c91ec73`  |
| 521    | No file              | `ef002c91ec73`  |
| 517    | No file              | `ef002c91ec73`  |
| 510    | No file              | `ef002c91ec73`  |
| 508    | No file              | `ef002c91ec73`  |
| 504    | No file              | `ef002c91ec73`  |
| 497    | No file              | `ef002c91ec73`  |
| 491    | No file              | `ef002c91ec73`  |
| 485    | No file              | `ef002c91ec73`  |
| 478    | No file              | `ef002c91ec73`  |
| 472    | No file              | `ef002c91ec73`  |
| 466    | No file              | `ef002c91ec73`  |
| 457    | No file              | `ef002c91ec73`  |
| 452    | No file              | `ef002c91ec73`  |
| 449    | No file              | `ef002c91ec73`  |
| 435    | No file              | `ef002c91ec73`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `guildhousecraftskilloffset.dbss` | Optional | `receipe_key -> (data_offset, data_size)` of every row; the rows are 20 bytes each and can be walked without it |
| `languagedata_en.loc`             | Optional | House use name (type `16`, `str_id1` = `receipe_key`) and skill name (type `10`, `str_id1` = skill number) |

The handler links each `receipe_key` to its `houseinforeceipe.dbss` row and
each skill number to its first `skill.dbss` row. It loads neither file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `19` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (20 bytes)

| Offset  | Type   | Field           | Notes                                                              |
| ------- | ------ | --------------- | ------------------------------------------------------------------ |
| `+0x00` | i32    | receipe_key     | House use, a `houseinforeceipe.dbss` key; unique per row           |
| `+0x04` | i32    | receipe_key_dup | Equal to `receipe_key` in every row; the offset file points here   |
| `+0x08` | u16    | unknown_08      | `0` on every row (clients 1784 and 3474); see Open Questions       |
| `+0x0A` | u16[5] | skill_nos       | Skill numbers in slot order, `0` in an unused slot; see Skill Slots |

The rows are sorted neither by key nor in index order: on client 3474 the
file runs 50009 down to 50001, 1610 down to 1604, 1602, 1601 and ends with
`2`.

### `guildhousecraftskilloffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildhousecraftskill.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u32  | receipe_key | Key of the row it points at                        |
| `+0x04` | u32  | data_offset | Row start + 4, at `receipe_key_dup`                |
| `+0x08` | u32  | data_size   | `16`: the row without its leading `receipe_key`    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
lists the rows in file order except key `2`, which sits between 1604 and
1602 (client 3474). On clients 1784 and 3474 every index row points at the
row with its key.

## Skill Slots

Each filled slot is a `skill.dbss` skill number, named by LOC type 10. The
slots fill from the first with no gap. On client 3474 the 19 rows fill 48
slots with 44 distinct skills:

| Receipe keys       | House use                                  | Skills (client 3474)                               |
| ------------------ | ------------------------------------------ | -------------------------------------------------- |
| `1601`             | Guild Shipyard                             | `65042`, `65043` Building Boat Lv. 1 and 2          |
| `1602`             | Elephant Nursery                           | `65052`, `65053` Monstrous Force Lv. 1 and 2        |
| `1604`             | Imperial Trade Packing                     | `65057` Imperial Calling                            |
| `1605` to `1609`   | Balenos to Valencia Specialties Packing    | `65058` Local Economy Revitalization, all five rows |
| `1610`             | Mount Part Workshop                        | `65059` Fully Prepared                              |
| `2`                | Storage                                    | Ample Storage Lv. 1 to 5                            |
| `50001` to `50009` | Guild Storage level 2 to 9                 | Ample Storage Lv. 6 to 37, 1 to 5 levels per row    |

## Field Names

The 2016 PDB has no guild house craft skill struct. The server dump of a
private server on client 1784 names the class
`gc::GuildHouseCraftSkillStaticStatus`, keyed by `gc::KeyType<int,-1>` (an
i32), loaded by `loadHouseForGuildHouseCraftSkillInfo`.

The values match the `GuildHouseCraftSkillInfo` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `HouseInfoReceipeKey`:

| Field          | Column                 | Same value (client 1784) | Same value (client 3474) |
| -------------- | ---------------------- | ------------------------ | ------------------------ |
| receipe_key    | `HouseInfoReceipeKey`  | 16 of 16 rows            | 16 of 16 shared rows     |
| skill_nos[0]   | `SkillNo_1`            | 16 of 16                 | 16 of 16                 |
| skill_nos[1]   | `SkillNo_2`            | 16 of 16                 | 16 of 16                 |
| skill_nos[2]   | `SkillNo_3`            | 16 of 16                 | 15 of 16                 |
| skill_nos[3]   | `SkillNo_4`            | 16 of 16                 | 15 of 16                 |
| skill_nos[4]   | `SkillNo_5`            | 16 of 16                 | 15 of 16                 |

The one miss on client 3474 is Guild Storage key `50006`, which adds
`65228`, `65229` and `65230` (Ample Storage Lv. 25 to 27) in slots 3 to 5
where the sheet and client 1784 have none. Client 3474 also adds the rows
`50007`, `50008` and `50009`, which neither has. The sheet has no column for
`unknown_08`.

## Notes

- [`guildhousecraftskillreverselinklist.bss`](../bss/guildhousecraftskillreverselinklist_bss.md)
  holds the reverse of this table: per skill number, the rows that list it as
  (`receipe_key`, slot) pairs, the slot counted from `1` for `skill_nos[0]`.
  Skill `65058` lists `1605` to `1609`, each at slot `1`.
- [`guildhousecraftstorage.dbss`](guildhousecraftstorage_dbss.md) is keyed
  by the same receipe keys, Storage and Guild Storage only, and holds one
  storage count per row.
- The guild house Lua (`worldmap_grand_guildhousecontrol.luac`,
  `panel_worldmap_guildhousemanagement_renew.luac`) reads the house uses
  through `getGuildHouseCraftInfoManager()` and `getHouseCraftWrapperByIndex()`
  and reads no skill from this table.

## Open Questions

### What `unknown_08` Holds

The u16 between `receipe_key_dup` and `skill_nos` is `0` in all 19 rows on
client 3474 and all 16 on client 1784, and the source sheet has no column
for it. The reverse link list counts slots from `1`, so one reading is a
six-entry u16 array whose slot `0` is never used; nothing in the client
confirms it.
