# `specialenchantitem.bss` Format

## Purpose

The items whose name or icon changes with their enhancement level, one fixed
19-byte row per item key (`enchant_level << 24 | item_id`) with the level the
client shows, the icon path and the Korean name of that level. It is a compact
copy of the per-level blocks of [`itemenchant.dbss`](../dbss/itemenchant_dbss.md) for
these 551 items, so the per-level icon of a Sovereign weapon or a Fallen God
armor is reachable without walking the 194 MB file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes   | Records              | Row bytes |
| ------ | -------------- | ------------------------ | ------- | -------------------- | --------- |
| 1      | 1731 and later | `specialenchantitem.bss` | 174,941 | 3,081 Item Level Row | 19        |

| Layout | File                     | Known             | Unknown         |
| ------ | ------------------------ | ----------------- | --------------- |
| 1      | `specialenchantitem.bss` | 159,536 B (91.2%) | 15,405 B (8.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `37318e296ec3`  |
| 3482   | Layout 1             | `37318e296ec3`  |
| 3474   | Layout 1             | `37318e296ec3`  |
| 3473   | Layout 1             | `37318e296ec3`  |
| 3464   | Layout 1             | `37318e296ec3`  |
| 3458   | Layout 1             | `37318e296ec3`  |
| 3454   | Layout 1             | `37318e296ec3`  |
| 3444   | Layout 1             | `37318e296ec3`  |
| 3435   | Layout 1             | `37318e296ec3`  |
| 3426   | Layout 1             | `37318e296ec3`  |
| 3418   | Layout 1             | `37318e296ec3`  |
| 3412   | Layout 1             | `37318e296ec3`  |
| 3402   | Layout 1             | `37318e296ec3`  |
| 3396   | Layout 1             | `37318e296ec3`  |
| 3387   | Layout 1             | `37318e296ec3`  |
| 3381   | Layout 1             | `37318e296ec3`  |
| 3373   | Layout 1             | `37318e296ec3`  |
| 3364   | Layout 1             | `37318e296ec3`  |
| 3356   | Layout 1             | `37318e296ec3`  |
| 3349   | Layout 1             | `37318e296ec3`  |
| 3342   | Layout 1             | `37318e296ec3`  |
| 3335   | Layout 1             | `37318e296ec3`  |
| 3326   | Layout 1             | `37318e296ec3`  |
| 3321   | Layout 1             | `37318e296ec3`  |
| 3314   | Layout 1             | `37318e296ec3`  |
| 3303   | Layout 1             | `37318e296ec3`  |
| 3302   | Layout 1             | `37318e296ec3`  |
| 3293   | Layout 1             | `37318e296ec3`  |
| 3283   | Layout 1             | `37318e296ec3`  |
| 3275   | Layout 1             | `37318e296ec3`  |
| 3267   | Layout 1             | `37318e296ec3`  |
| 3258   | Layout 1             | `37318e296ec3`  |
| 3251   | Layout 1             | `37318e296ec3`  |
| 3242   | Layout 1             | `37318e296ec3`  |
| 3235   | Layout 1             | `37318e296ec3`  |
| 3229   | Layout 1             | `37318e296ec3`  |
| 3212   | Layout 1             | `37318e296ec3`  |
| 3203   | Layout 1             | `37318e296ec3`  |
| 3193   | Layout 1             | `37318e296ec3`  |
| 3186   | Layout 1             | `37318e296ec3`  |
| 3177   | Layout 1             | `37318e296ec3`  |
| 3169   | Layout 1             | `37318e296ec3`  |
| 3158   | Layout 1             | `37318e296ec3`  |
| 3151   | Layout 1             | `37318e296ec3`  |
| 3144   | Layout 1             | `37318e296ec3`  |
| 3133   | Layout 1             | `37318e296ec3`  |
| 3125   | Layout 1             | `37318e296ec3`  |
| 3118   | Layout 1             | `37318e296ec3`  |
| 3111   | Layout 1             | `37318e296ec3`  |
| 3103   | Layout 1             | `37318e296ec3`  |
| 3095   | Layout 1             | `37318e296ec3`  |
| 3086   | Layout 1             | `37318e296ec3`  |
| 3072   | Layout 1             | `37318e296ec3`  |
| 3062   | Layout 1             | `37318e296ec3`  |
| 3052   | Layout 1             | `37318e296ec3`  |
| 3045   | Layout 1             | `37318e296ec3`  |
| 3037   | Layout 1             | `37318e296ec3`  |
| 3030   | Layout 1             | `37318e296ec3`  |
| 3021   | Layout 1             | `37318e296ec3`  |
| 3012   | Layout 1             | `37318e296ec3`  |
| 3002   | Layout 1             | `37318e296ec3`  |
| 2995   | Layout 1             | `37318e296ec3`  |
| 2987   | Layout 1             | `37318e296ec3`  |
| 2978   | Layout 1             | `37318e296ec3`  |
| 2970   | Layout 1             | `37318e296ec3`  |
| 2959   | Layout 1             | `37318e296ec3`  |
| 2951   | Layout 1             | `37318e296ec3`  |
| 2942   | Layout 1             | `37318e296ec3`  |
| 2935   | Layout 1             | `37318e296ec3`  |
| 2932   | Layout 1             | `37318e296ec3`  |
| 2923   | Layout 1             | `37318e296ec3`  |
| 2919   | Layout 1             | `37318e296ec3`  |
| 2907   | Layout 1             | `37318e296ec3`  |
| 2900   | Layout 1             | `37318e296ec3`  |
| 2891   | Layout 1             | `37318e296ec3`  |
| 2882   | Layout 1             | `37318e296ec3`  |
| 2872   | Layout 1             | `37318e296ec3`  |
| 2863   | Layout 1             | `37318e296ec3`  |
| 2855   | Layout 1             | `37318e296ec3`  |
| 2849   | Layout 1             | `37318e296ec3`  |
| 2844   | Layout 1             | `37318e296ec3`  |
| 2834   | Layout 1             | `37318e296ec3`  |
| 2825   | Layout 1             | `37318e296ec3`  |
| 2819   | Layout 1             | `37318e296ec3`  |
| 2811   | Layout 1             | `37318e296ec3`  |
| 2803   | Layout 1             | `37318e296ec3`  |
| 2794   | Layout 1             | `37318e296ec3`  |
| 2783   | Layout 1             | `37318e296ec3`  |
| 2774   | Layout 1             | `37318e296ec3`  |
| 2765   | Layout 1             | `37318e296ec3`  |
| 2756   | Layout 1             | `37318e296ec3`  |
| 2750   | Layout 1             | `37318e296ec3`  |
| 2743   | Layout 1             | `37318e296ec3`  |
| 2736   | Layout 1             | `37318e296ec3`  |
| 2726   | Layout 1             | `37318e296ec3`  |
| 2717   | Layout 1             | `37318e296ec3`  |
| 2709   | Layout 1             | `37318e296ec3`  |
| 2703   | Layout 1             | `37318e296ec3`  |
| 2695   | Layout 1             | `37318e296ec3`  |
| 2684   | Layout 1             | `37318e296ec3`  |
| 2672   | Layout 1             | `37318e296ec3`  |
| 2665   | Layout 1             | `37318e296ec3`  |
| 2657   | Layout 1             | `37318e296ec3`  |
| 2649   | Layout 1             | `37318e296ec3`  |
| 2644   | Layout 1             | `37318e296ec3`  |
| 2637   | Layout 1             | `37318e296ec3`  |
| 2629   | Layout 1             | `37318e296ec3`  |
| 2619   | Layout 1             | `37318e296ec3`  |
| 2612   | Layout 1             | `37318e296ec3`  |
| 2606   | Layout 1             | `37318e296ec3`  |
| 2602   | Layout 1             | `37318e296ec3`  |
| 2601   | Layout 1             | `37318e296ec3`  |
| 2592   | Layout 1             | `37318e296ec3`  |
| 2583   | Layout 1             | `37318e296ec3`  |
| 2575   | Layout 1             | `37318e296ec3`  |
| 2567   | Layout 1             | `37318e296ec3`  |
| 2560   | Layout 1             | `37318e296ec3`  |
| 2553   | Layout 1             | `37318e296ec3`  |
| 2545   | Layout 1             | `37318e296ec3`  |
| 2538   | Layout 1             | `37318e296ec3`  |
| 2529   | Layout 1             | `37318e296ec3`  |
| 2519   | Layout 1             | `37318e296ec3`  |
| 2513   | Layout 1             | `37318e296ec3`  |
| 2510   | Layout 1             | `37318e296ec3`  |
| 2507   | Layout 1             | `37318e296ec3`  |
| 2503   | Layout 1             | `37318e296ec3`  |
| 2498   | Layout 1             | `37318e296ec3`  |
| 2492   | Layout 1             | `37318e296ec3`  |
| 2487   | Layout 1             | `37318e296ec3`  |
| 2480   | Layout 1             | `37318e296ec3`  |
| 2474   | Layout 1             | `37318e296ec3`  |
| 2468   | Layout 1             | `37318e296ec3`  |
| 2460   | Layout 1             | `37318e296ec3`  |
| 2453   | Layout 1             | `37318e296ec3`  |
| 2444   | Layout 1             | `37318e296ec3`  |
| 2438   | Layout 1             | `37318e296ec3`  |
| 2434   | Layout 1             | `37318e296ec3`  |
| 2429   | Layout 1             | `37318e296ec3`  |
| 2421   | Layout 1             | `37318e296ec3`  |
| 2414   | Layout 1             | `37318e296ec3`  |
| 2407   | Layout 1             | `37318e296ec3`  |
| 2401   | Layout 1             | `37318e296ec3`  |
| 2397   | Layout 1             | `37318e296ec3`  |
| 2393   | Layout 1             | `37318e296ec3`  |
| 2384   | Layout 1             | `37318e296ec3`  |
| 2378   | Layout 1             | `37318e296ec3`  |
| 2372   | Layout 1             | `37318e296ec3`  |
| 2358   | Layout 1             | `37318e296ec3`  |
| 2352   | Layout 1             | `37318e296ec3`  |
| 2347   | Layout 1             | `37318e296ec3`  |
| 2343   | Layout 1             | `37318e296ec3`  |
| 2335   | Layout 1             | `37318e296ec3`  |
| 2327   | Layout 1             | `37318e296ec3`  |
| 2324   | Layout 1             | `37318e296ec3`  |
| 2319   | Layout 1             | `37318e296ec3`  |
| 2313   | Layout 1             | `37318e296ec3`  |
| 2308   | Layout 1             | `37318e296ec3`  |
| 2302   | Layout 1             | `37318e296ec3`  |
| 2295   | Layout 1             | `37318e296ec3`  |
| 2290   | Layout 1             | `37318e296ec3`  |
| 2284   | Layout 1             | `37318e296ec3`  |
| 2276   | Layout 1             | `37318e296ec3`  |
| 2269   | Layout 1             | `37318e296ec3`  |
| 2259   | Layout 1             | `37318e296ec3`  |
| 2250   | Layout 1             | `37318e296ec3`  |
| 2243   | Layout 1             | `37318e296ec3`  |
| 2235   | Layout 1             | `37318e296ec3`  |
| 2229   | Layout 1             | `37318e296ec3`  |
| 2224   | Layout 1             | `37318e296ec3`  |
| 2218   | Layout 1             | `37318e296ec3`  |
| 2215   | Layout 1             | `37318e296ec3`  |
| 2207   | Layout 1             | `37318e296ec3`  |
| 2203   | Layout 1             | `37318e296ec3`  |
| 2196   | Layout 1             | `37318e296ec3`  |
| 2192   | Layout 1             | `37318e296ec3`  |
| 2189   | Layout 1             | `37318e296ec3`  |
| 2183   | Layout 1             | `37318e296ec3`  |
| 2179   | Layout 1             | `37318e296ec3`  |
| 2171   | Layout 1             | `37318e296ec3`  |
| 2163   | Layout 1             | `37318e296ec3`  |
| 2156   | Layout 1             | `37318e296ec3`  |
| 2151   | Layout 1             | `37318e296ec3`  |
| 2147   | Layout 1             | `37318e296ec3`  |
| 2142   | Layout 1             | `37318e296ec3`  |
| 2138   | Layout 1             | `37318e296ec3`  |
| 2134   | Layout 1             | `37318e296ec3`  |
| 2130   | Layout 1             | `37318e296ec3`  |
| 2122   | Layout 1             | `37318e296ec3`  |
| 2107   | Layout 1             | `37318e296ec3`  |
| 2098   | Layout 1             | `37318e296ec3`  |
| 2089   | Layout 1             | `37318e296ec3`  |
| 2081   | Layout 1             | `37318e296ec3`  |
| 2073   | Layout 1             | `37318e296ec3`  |
| 2067   | Layout 1             | `37318e296ec3`  |
| 2063   | Layout 1             | `37318e296ec3`  |
| 2059   | Layout 1             | `37318e296ec3`  |
| 2052   | Layout 1             | `37318e296ec3`  |
| 2044   | Layout 1             | `37318e296ec3`  |
| 2039   | Layout 1             | `37318e296ec3`  |
| 2032   | Layout 1             | `37318e296ec3`  |
| 2025   | Layout 1             | `37318e296ec3`  |
| 2011   | Layout 1             | `37318e296ec3`  |
| 2005   | Layout 1             | `37318e296ec3`  |
| 2000   | Layout 1             | `37318e296ec3`  |
| 1996   | Layout 1             | `37318e296ec3`  |
| 1991   | Layout 1             | `37318e296ec3`  |
| 1985   | Layout 1             | `37318e296ec3`  |
| 1980   | Layout 1             | `37318e296ec3`  |
| 1969   | Layout 1             | `37318e296ec3`  |
| 1964   | Layout 1             | `37318e296ec3`  |
| 1958   | Layout 1             | `37318e296ec3`  |
| 1950   | Layout 1             | `37318e296ec3`  |
| 1945   | Layout 1             | `37318e296ec3`  |
| 1937   | Layout 1             | `37318e296ec3`  |
| 1933   | Layout 1             | `37318e296ec3`  |
| 1927   | Layout 1             | `37318e296ec3`  |
| 1921   | No documented layout | `37318e296ec3`  |
| 1914   | No documented layout | `37318e296ec3`  |
| 1908   | Layout 1             | `37318e296ec3`  |
| 1897   | Layout 1             | `37318e296ec3`  |
| 1892   | Layout 1             | `37318e296ec3`  |
| 1886   | Layout 1             | `37318e296ec3`  |
| 1881   | Layout 1             | `37318e296ec3`  |
| 1871   | Layout 1             | `37318e296ec3`  |
| 1866   | Layout 1             | `37318e296ec3`  |
| 1862   | Layout 1             | `37318e296ec3`  |
| 1854   | Layout 1             | `37318e296ec3`  |
| 1846   | Layout 1             | `37318e296ec3`  |
| 1838   | Layout 1             | `37318e296ec3`  |
| 1832   | Layout 1             | `37318e296ec3`  |
| 1826   | Layout 1             | `37318e296ec3`  |
| 1822   | Layout 1             | `37318e296ec3`  |
| 1818   | Layout 1             | `37318e296ec3`  |
| 1804   | Layout 1             | `37318e296ec3`  |
| 1794   | Layout 1             | `37318e296ec3`  |
| 1790   | Layout 1             | `37318e296ec3`  |
| 1784   | Layout 1             | `37318e296ec3`  |
| 1774   | Layout 1             | `37318e296ec3`  |
| 1771   | Layout 1             | `37318e296ec3`  |
| 1762   | Layout 1             | `37318e296ec3`  |
| 1759   | Layout 1             | `37318e296ec3`  |
| 1754   | Layout 1             | `37318e296ec3`  |
| 1749   | Layout 1             | `37318e296ec3`  |
| 1743   | Layout 1             | `37318e296ec3`  |
| 1737   | Layout 1             | `37318e296ec3`  |
| 1731   | Layout 1             | `37318e296ec3`  |
| 1725   | No documented layout | `37318e296ec3`  |
| 1717   | No documented layout | `37318e296ec3`  |
| 1710   | No documented layout | `37318e296ec3`  |
| 1704   | No documented layout | `37318e296ec3`  |
| 1698   | No documented layout | `37318e296ec3`  |
| 1690   | No documented layout | `37318e296ec3`  |
| 1685   | No documented layout | `37318e296ec3`  |
| 1680   | No documented layout | `37318e296ec3`  |
| 1674   | No documented layout | `37318e296ec3`  |
| 1668   | No documented layout | `37318e296ec3`  |
| 1659   | No documented layout | `37318e296ec3`  |
| 1649   | No documented layout | `37318e296ec3`  |
| 1642   | No documented layout | `37318e296ec3`  |
| 1636   | No documented layout | `37318e296ec3`  |
| 1628   | No documented layout | `37318e296ec3`  |
| 1622   | No documented layout | `37318e296ec3`  |
| 1614   | No documented layout | `37318e296ec3`  |
| 1608   | No documented layout | `37318e296ec3`  |
| 1602   | No documented layout | `37318e296ec3`  |
| 1598   | No documented layout | `37318e296ec3`  |
| 1594   | No documented layout | `37318e296ec3`  |
| 1590   | No documented layout | `37318e296ec3`  |
| 1587   | No documented layout | `37318e296ec3`  |
| 1584   | No documented layout | `37318e296ec3`  |
| 1579   | No documented layout | `37318e296ec3`  |
| 1572   | No documented layout | `37318e296ec3`  |
| 1565   | No documented layout | `37318e296ec3`  |
| 1559   | No documented layout | `37318e296ec3`  |
| 1554   | No documented layout | `37318e296ec3`  |
| 1547   | No documented layout | `37318e296ec3`  |
| 1537   | No documented layout | `37318e296ec3`  |
| 1529   | No documented layout | `37318e296ec3`  |
| 1524   | No documented layout | `37318e296ec3`  |
| 1519   | No documented layout | `37318e296ec3`  |
| 1509   | No documented layout | `37318e296ec3`  |
| 1506   | No documented layout | `37318e296ec3`  |
| 1504   | No documented layout | `37318e296ec3`  |
| 1500   | No documented layout | `37318e296ec3`  |
| 1493   | No documented layout | `37318e296ec3`  |
| 1489   | No documented layout | `37318e296ec3`  |
| 1485   | No documented layout | `37318e296ec3`  |
| 1481   | No documented layout | `37318e296ec3`  |
| 1474   | No documented layout | `37318e296ec3`  |
| 1466   | No documented layout | `37318e296ec3`  |
| 1462   | No documented layout | `37318e296ec3`  |
| 1459   | No documented layout | `37318e296ec3`  |
| 1453   | No documented layout | `37318e296ec3`  |
| 1450   | No documented layout | `37318e296ec3`  |
| 1445   | No documented layout | `37318e296ec3`  |
| 1439   | No documented layout | `37318e296ec3`  |
| 1433   | No documented layout | `37318e296ec3`  |
| 1430   | No documented layout | `37318e296ec3`  |
| 1426   | No documented layout | `37318e296ec3`  |
| 1421   | No documented layout | `37318e296ec3`  |
| 1417   | No documented layout | `37318e296ec3`  |
| 1416   | No documented layout | `37318e296ec3`  |
| 1409   | No documented layout | `37318e296ec3`  |
| 1405   | No documented layout | `37318e296ec3`  |
| 1401   | No documented layout | `37318e296ec3`  |
| 1396   | No documented layout | `37318e296ec3`  |
| 1391   | No documented layout | `37318e296ec3`  |
| 1390   | No documented layout | `37318e296ec3`  |
| 1386   | No documented layout | `37318e296ec3`  |
| 1381   | No documented layout | `37318e296ec3`  |
| 1379   | No documented layout | `37318e296ec3`  |
| 1372   | No documented layout | `37318e296ec3`  |
| 1366   | No documented layout | `37318e296ec3`  |
| 1364   | No documented layout | `37318e296ec3`  |
| 1363   | No documented layout | `37318e296ec3`  |
| 1360   | No documented layout | `37318e296ec3`  |
| 1358   | No documented layout | `37318e296ec3`  |
| 1355   | No documented layout | `37318e296ec3`  |
| 1351   | No documented layout | `37318e296ec3`  |
| 1348   | No documented layout | `37318e296ec3`  |
| 1346   | No file              | `37318e296ec3`  |
| 1341   | No file              | `37318e296ec3`  |
| 1340   | No file              | `37318e296ec3`  |
| 1338   | No file              | `37318e296ec3`  |
| 1335   | No file              | `37318e296ec3`  |
| 1333   | No file              | `37318e296ec3`  |
| 1329   | No file              | `37318e296ec3`  |
| 1327   | No file              | `37318e296ec3`  |
| 1324   | No file              | `37318e296ec3`  |
| 1321   | No file              | `37318e296ec3`  |
| 1319   | No file              | `37318e296ec3`  |
| 1318   | No file              | `37318e296ec3`  |
| 1316   | No file              | `37318e296ec3`  |
| 1313   | No file              | `37318e296ec3`  |
| 1311   | No file              | `37318e296ec3`  |
| 1309   | No file              | `37318e296ec3`  |
| 1304   | No file              | `37318e296ec3`  |
| 1292   | No file              | `37318e296ec3`  |
| 1286   | No file              | `37318e296ec3`  |
| 1280   | No file              | `37318e296ec3`  |
| 1276   | No file              | `37318e296ec3`  |
| 1267   | No file              | `37318e296ec3`  |
| 1261   | No file              | `37318e296ec3`  |
| 1256   | No file              | `37318e296ec3`  |
| 1250   | No file              | `37318e296ec3`  |
| 1246   | No file              | `37318e296ec3`  |
| 1239   | No file              | `37318e296ec3`  |
| 1230   | No file              | `37318e296ec3`  |
| 1226   | No file              | `37318e296ec3`  |
| 1220   | No file              | `37318e296ec3`  |
| 1217   | No file              | `37318e296ec3`  |
| 1211   | No file              | `37318e296ec3`  |
| 1210   | No file              | `37318e296ec3`  |
| 1208   | No file              | `37318e296ec3`  |
| 1203   | No file              | `37318e296ec3`  |
| 1197   | No file              | `37318e296ec3`  |
| 1194   | No file              | `37318e296ec3`  |
| 1192   | No file              | `37318e296ec3`  |
| 1187   | No file              | `37318e296ec3`  |
| 1183   | No file              | `37318e296ec3`  |
| 1177   | No file              | `37318e296ec3`  |
| 1173   | No file              | `37318e296ec3`  |
| 1167   | No file              | `37318e296ec3`  |
| 1164   | No file              | `37318e296ec3`  |
| 1156   | No file              | `37318e296ec3`  |
| 1149   | No file              | `37318e296ec3`  |
| 1144   | No file              | `37318e296ec3`  |
| 1137   | No file              | `37318e296ec3`  |
| 1132   | No file              | `37318e296ec3`  |
| 1127   | No file              | `37318e296ec3`  |
| 1122   | No file              | `37318e296ec3`  |
| 1118   | No file              | `37318e296ec3`  |
| 1114   | No file              | `37318e296ec3`  |
| 1109   | No file              | `37318e296ec3`  |
| 1102   | No file              | `37318e296ec3`  |
| 1096   | No file              | `37318e296ec3`  |
| 1088   | No file              | `37318e296ec3`  |
| 1081   | No file              | `37318e296ec3`  |
| 1076   | No file              | `37318e296ec3`  |
| 1069   | No file              | `37318e296ec3`  |
| 1064   | No file              | `37318e296ec3`  |
| 1058   | No file              | `37318e296ec3`  |
| 1051   | No file              | `37318e296ec3`  |
| 1044   | No file              | `37318e296ec3`  |
| 1036   | No file              | `37318e296ec3`  |
| 1026   | No file              | `37318e296ec3`  |
| 1016   | No file              | `37318e296ec3`  |
| 1009   | No file              | `37318e296ec3`  |
| 1005   | No file              | `37318e296ec3`  |
| 1000   | No file              | `37318e296ec3`  |
| 998    | No file              | `37318e296ec3`  |
| 990    | No file              | `37318e296ec3`  |
| 979    | No file              | `37318e296ec3`  |
| 972    | No file              | `37318e296ec3`  |
| 963    | No file              | `37318e296ec3`  |
| 955    | No file              | `37318e296ec3`  |
| 946    | No file              | `37318e296ec3`  |
| 938    | No file              | `37318e296ec3`  |
| 927    | No file              | `37318e296ec3`  |
| 911    | No file              | `37318e296ec3`  |
| 904    | No file              | `37318e296ec3`  |
| 899    | No file              | `37318e296ec3`  |
| 894    | No file              | `37318e296ec3`  |
| 885    | No file              | `37318e296ec3`  |
| 879    | No file              | `37318e296ec3`  |
| 872    | No file              | `37318e296ec3`  |
| 864    | No file              | `37318e296ec3`  |
| 855    | No file              | `37318e296ec3`  |
| 853    | No file              | `37318e296ec3`  |
| 845    | No file              | `37318e296ec3`  |
| 837    | No file              | `37318e296ec3`  |
| 829    | No file              | `37318e296ec3`  |
| 822    | No file              | `37318e296ec3`  |
| 814    | No file              | `37318e296ec3`  |
| 805    | No file              | `37318e296ec3`  |
| 794    | No file              | `37318e296ec3`  |
| 787    | No file              | `37318e296ec3`  |
| 780    | No file              | `37318e296ec3`  |
| 771    | No file              | `37318e296ec3`  |
| 760    | No file              | `37318e296ec3`  |
| 748    | No file              | `37318e296ec3`  |
| 741    | No file              | `37318e296ec3`  |
| 736    | No file              | `37318e296ec3`  |
| 731    | No file              | `37318e296ec3`  |
| 723    | No file              | `37318e296ec3`  |
| 711    | No file              | `37318e296ec3`  |
| 707    | No file              | `37318e296ec3`  |
| 697    | No file              | `37318e296ec3`  |
| 689    | No file              | `37318e296ec3`  |
| 683    | No file              | `37318e296ec3`  |
| 678    | No file              | `37318e296ec3`  |
| 670    | No file              | `37318e296ec3`  |
| 661    | No file              | `37318e296ec3`  |
| 656    | No file              | `37318e296ec3`  |
| 652    | No file              | `37318e296ec3`  |
| 643    | No file              | `37318e296ec3`  |
| 637    | No file              | `37318e296ec3`  |
| 630    | No file              | `37318e296ec3`  |
| 627    | No file              | `37318e296ec3`  |
| 621    | No file              | `37318e296ec3`  |
| 617    | No file              | `37318e296ec3`  |
| 615    | No file              | `37318e296ec3`  |
| 606    | No file              | `37318e296ec3`  |
| 599    | No file              | `37318e296ec3`  |
| 592    | No file              | `37318e296ec3`  |
| 586    | No file              | `37318e296ec3`  |
| 577    | No file              | `37318e296ec3`  |
| 569    | No file              | `37318e296ec3`  |
| 561    | No file              | `37318e296ec3`  |
| 554    | No file              | `37318e296ec3`  |
| 542    | No file              | `37318e296ec3`  |
| 532    | No file              | `37318e296ec3`  |
| 531    | No file              | `37318e296ec3`  |
| 526    | No file              | `37318e296ec3`  |
| 521    | No file              | `37318e296ec3`  |
| 517    | No file              | `37318e296ec3`  |
| 510    | No file              | `37318e296ec3`  |
| 508    | No file              | `37318e296ec3`  |
| 504    | No file              | `37318e296ec3`  |
| 497    | No file              | `37318e296ec3`  |
| 491    | No file              | `37318e296ec3`  |
| 485    | No file              | `37318e296ec3`  |
| 478    | No file              | `37318e296ec3`  |
| 472    | No file              | `37318e296ec3`  |
| 466    | No file              | `37318e296ec3`  |
| 457    | No file              | `37318e296ec3`  |
| 452    | No file              | `37318e296ec3`  |
| 449    | No file              | `37318e296ec3`  |
| 435    | No file              | `37318e296ec3`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `itemenchant.dbss`    | Optional | Full item records; every row here has a level block there             |
| `languagedata_en.loc` | Optional | English names, LOC type 79, `str_id1` = item ID, `str_id2` = level    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss`, `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset              | Type                  | Field        | Notes                                          |
| ------------------- | --------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]               | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                   | count        | Number of rows; 3,081 on client 3458           |
| `+0x08`             | Item Level Row[count] | rows         | See Item Level Row                             |
| `rows+0x00`         | String Table          | string_table | See String Table                               |
| `string_table+0x00` | u32                   | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                   | zero         | Always 0                                       |

The rows follow `itemenchantoffset.dbss` key order exactly, which is neither
ascending nor descending (the first row is item 736815 at level 20).

### Item Level Row (19 bytes)

Fields are unaligned.

| Offset  | Type     | Field         | Notes                                                                    |
| ------- | -------- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | item_key      | `enchant_level << 24 \| item_id` (`_common/item_key.py`); unique          |
| `+0x04` | u8       | display_level | The level the client shows, on the weapon scale; see Display Level below |
| `+0x05` | u32      | icon_ref      | String table index of the icon path; never empty                         |
| `+0x09` | u32      | name_ref      | String table index of the Korean name; never empty                       |
| `+0x0D` | u32      | unknown_0d    | Always `0`; see Field Names                                              |
| `+0x11` | u8       | unknown_11    | `1` in 2,481 rows; the same in every row of one item, see Open Questions |
| `+0x12` | u8       | family_name_exception | `1` in 2,409 rows; the same in every row of one item, see Field Names |

### String Table (variable: 4 bytes + strings)

3,253 strings on client 3458, all referenced. `icon_ref` and `name_ref` index
the same table but never share an entry: 500 are icon paths, the other 2,753
names. Unlike `buffsimply.bss` there is no `"0"` or empty entry. Repeated
values are stored once, so levels that keep an icon point at the same entry.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 3,253 on client 3458 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Field Names

The rows are the `Enchant_Special` sheet of a private server on client
1784 (`datasheet_enchantdatatable_new.xlsm`: `ItemKey`, `Enchant`,
`EnchantImage`, `ItemName`, `ItemIcon`, `FamilyNameException`). That
server's dump (`Instance_dumpFull.exe`) loads the sheet (loader at VA
`0x140a397e0`) into a struct holding the packed `Enchant << 24 | ItemKey`, a
u32 with no column set to `0`, `EnchantImage` as a u8, `FamilyNameException`
as a u8 and a u8 with no column set to `0`. The server has no reader for the
client file, and the row does not keep that member order (`display_level` is
`EnchantImage` at `+0x04`), so the names below rest on the data.

`+0x12` is `family_name_exception`. Between client 1485 and 1784 the row
grew by exactly that byte, together with the new sheet column: the 1485
server loads no `FamilyNameException` and its rows are 18 bytes. On client
1784 the byte equals the column on all 1,020 rows (852 `1`, 168 `0`). The
column's Korean comment says that enhancing gear to V (PEN) engraves the
crafter's family name when the item is not bound (`VestedType` `0`), and
that `1` turns the engraving off even on success; it was added so Fallen
God's Armor, which reaches V at +5 like an accessory, does not take the
buyer's name after a sale. The 1784 server reads it after looking up the
item (VA `0x1414e7e54`) and skips the following block when it is set.

`unknown_0d` and `unknown_11` match the struct's two members with no column
by width. Both loaders (1485 and 1784) set them to `0` and no read of either
was found, so nothing names them.

## Display Level

The client reads this byte through `ToClient_getSpecialEnchantDisplayLevel`
(`include/global_util_ui_slot.luac`, the item tooltips, the enhancement window) and
passes it to `HighRomaEnchantLevel_ReplaceString`, so it is the level drawn on
the item slot, which can differ from the stored `enchant_level`. It uses the
weapon scale: `1` to `15` are `+1` to `+15`, `16` to `25` are the grades
below. The grade names are confirmed by LOC type 79, whose name of every row
at display level 16 to 25 starts with that grade (`PRI: Fiery Sovereign
Mareca`), 219 rows each on client 3458.

| Value | Grade |
| ----- | ----- |
| 16    | PRI   |
| 17    | DUO   |
| 18    | TRI   |
| 19    | TET   |
| 20    | PEN   |
| 21    | HEX   |
| 22    | SEP   |
| 23    | OCT   |
| 24    | NOV   |
| 25    | DEC   |

## Notes

- Checked against `itemenchant.dbss` on client 3458: every row's key has a
  block there, and the first string of that block is the same icon path in all
  3,081 rows. 1,356 rows store an icon that differs from the item's level-0
  icon, over 189 paths that no base item uses (`00747201_02.dds`). The
  `ITEM_ICON` index, read from level-0 blocks only, cannot reach them.
- The app builds its per-level item icon lookup index
  (`IndexKind.ITEM_KEY_ICON`, read through `IconKind.ITEM_KEY` and
  `item_key_icon_path()`) from this file.
- LOC type 79 names all 3,081 rows. In 2,250 the name differs from the item's
  LOC type 0 name: a grade prefix (`DEC: Fiery Sovereign Mareca`) or a new
  word for the stage (`Desperate Dahn's Gloves` at level 1, `Wailing Dahn's
  Gloves` at level 4).
- LOC type 79 reaches past this file: 5,298 rows over 925 items on client
  3458, among them accessories such as `Preonne Belt` whose every level
  repeats the item name. Level 0 always matches the LOC type 0 name, and a
  name that differs never repeats across the levels of one item, so
  `item_key_text()` (`_common/item_key.py`) shows it without the level
  suffix in every item list. Five more rows key Fallen God's Armor (719898)
  by its packed item key with `str_id2` 0; they repeat the item ID rows.
- All 500 icon paths exist on client 3458 once resolved under
  `ui_texture/icon/` and lowercased, as for `itemenchant.dbss`.
- The 551 items fall into four shapes on client 3458:

  | Rows per item | Items | `enchant_level` | `display_level`             | `unknown_11`, `family_name_exception` | Example             |
  | ------------- | ----- | --------------- | --------------------------- | -------------------------- | ------------------------------ |
  | 1             | 292   | 20              | 20                          | 0, 0                       | Earthshaking Nouver Shuriken   |
  | 6             | 12    | 0 to 5          | 20 at every level           | 1, 0                       | Dahn's Gloves (930905)         |
  | 11            | 28    | 0 to 10         | same as the level           | 0, 0                       | Preonne Ring                   |
  | 11            | 219   | 0 to 10         | 0, then 16 to 25 (PRI to DEC) | 1, 1                     | Fiery Sovereign Mareca         |

  An item with rows here has a row for every level from 0 to its
  `itemenchant.dbss` maximum, except the 292 single-row items, which list only
  level 20.

## Open Questions

### What does `unknown_11` mark, and why do Fallen God's Armor rows differ?

Both bytes are per-item flags. On client 3458 `unknown_11` is `1` on exactly
the items whose name changes between their levels (231 items; the 28
Preonne-style items keep one name and store `0`, and the 292 single-row
items cannot vary), and `family_name_exception` is `1` on exactly the items
whose display level jumps to the grade scale (0, then 16 to 25). On client
1784 `unknown_11` is `0` on every row, and the four Fallen God's Armor items
(719897, 719898, 719899, 719955) store `family_name_exception` `1`; on
client 3474 they store `unknown_11` `1` and `family_name_exception` `0`. The
1784 sheet comment names Fallen God's Armor as the reason for the column, so
either the rule for those items changed or `unknown_11` took over part of
it. The client Lua names `isSpecialEnchantItem` and `isSpecialAccessory`
next to the display level call, but neither is shown to read this file.
