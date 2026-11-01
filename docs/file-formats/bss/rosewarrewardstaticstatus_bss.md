# `rosewarrewardstaticstatus.bss` Format

## Purpose

The Rose War rewards: one row without and one with a guild, each with the
items for a victory, a defeat and a liberation and a fourth item list. On
client 3474 the row with `is_guild` `0` hands out the Blossoming reward
boxes ("Third Legion" in their LOC text) and the row with `is_guild` `1`
the Flourishing ones ("Leading Guild"), each with Combat Secret Books, and
the guild row's fourth list holds 25 [Guild] Trace of Doom.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes | Records          | Row bytes |
| ------ | -------------- | ------------------------------- | ----- | ---------------- | --------- |
| 2      | 3473 and later | `rosewarrewardstaticstatus.bss` | 294   | 13 Reward, 2 Row | 16        |
| 1      | 2935 to 3464   | `rosewarrewardstaticstatus.bss` | 118   | 2 Row            | 49        |

| Layout | File                            | Known         | Unknown      |
| ------ | ------------------------------- | ------------- | ------------ |
| 2      | `rosewarrewardstaticstatus.bss` | 226 B (76.9%) | 68 B (23.1%) |
| 1      | `rosewarrewardstaticstatus.bss` | 94 B (79.7%)  | 24 B (20.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ac3f08824123`  |
| 3482   | Layout 2             | `ac3f08824123`  |
| 3474   | Layout 2             | `ac3f08824123`  |
| 3473   | Layout 2             | `ac3f08824123`  |
| 3464   | Layout 1             | `ac3f08824123`  |
| 3458   | Layout 1             | `ac3f08824123`  |
| 3454   | Layout 1             | `ac3f08824123`  |
| 3444   | Layout 1             | `ac3f08824123`  |
| 3435   | Layout 1             | `ac3f08824123`  |
| 3426   | Layout 1             | `ac3f08824123`  |
| 3418   | Layout 1             | `ac3f08824123`  |
| 3412   | Layout 1             | `ac3f08824123`  |
| 3402   | Layout 1             | `ac3f08824123`  |
| 3396   | Layout 1             | `ac3f08824123`  |
| 3387   | Layout 1             | `ac3f08824123`  |
| 3381   | Layout 1             | `ac3f08824123`  |
| 3373   | Layout 1             | `ac3f08824123`  |
| 3364   | Layout 1             | `ac3f08824123`  |
| 3356   | Layout 1             | `ac3f08824123`  |
| 3349   | Layout 1             | `ac3f08824123`  |
| 3342   | Layout 1             | `ac3f08824123`  |
| 3335   | Layout 1             | `ac3f08824123`  |
| 3326   | Layout 1             | `ac3f08824123`  |
| 3321   | Layout 1             | `ac3f08824123`  |
| 3314   | Layout 1             | `ac3f08824123`  |
| 3303   | Layout 1             | `ac3f08824123`  |
| 3302   | Layout 1             | `ac3f08824123`  |
| 3293   | Layout 1             | `ac3f08824123`  |
| 3283   | Layout 1             | `ac3f08824123`  |
| 3275   | Layout 1             | `ac3f08824123`  |
| 3267   | Layout 1             | `ac3f08824123`  |
| 3258   | Layout 1             | `ac3f08824123`  |
| 3251   | Layout 1             | `ac3f08824123`  |
| 3242   | Layout 1             | `ac3f08824123`  |
| 3235   | Layout 1             | `ac3f08824123`  |
| 3229   | Layout 1             | `ac3f08824123`  |
| 3212   | Layout 1             | `ac3f08824123`  |
| 3203   | Layout 1             | `ac3f08824123`  |
| 3193   | Layout 1             | `ac3f08824123`  |
| 3186   | Layout 1             | `ac3f08824123`  |
| 3177   | Layout 1             | `ac3f08824123`  |
| 3169   | Layout 1             | `ac3f08824123`  |
| 3158   | Layout 1             | `ac3f08824123`  |
| 3151   | Layout 1             | `ac3f08824123`  |
| 3144   | Layout 1             | `ac3f08824123`  |
| 3133   | Layout 1             | `ac3f08824123`  |
| 3125   | Layout 1             | `ac3f08824123`  |
| 3118   | Layout 1             | `ac3f08824123`  |
| 3111   | Layout 1             | `ac3f08824123`  |
| 3103   | Layout 1             | `ac3f08824123`  |
| 3095   | Layout 1             | `ac3f08824123`  |
| 3086   | Layout 1             | `ac3f08824123`  |
| 3072   | Layout 1             | `ac3f08824123`  |
| 3062   | Layout 1             | `ac3f08824123`  |
| 3052   | Layout 1             | `ac3f08824123`  |
| 3045   | Layout 1             | `ac3f08824123`  |
| 3037   | Layout 1             | `ac3f08824123`  |
| 3030   | Layout 1             | `ac3f08824123`  |
| 3021   | Layout 1             | `ac3f08824123`  |
| 3012   | Layout 1             | `ac3f08824123`  |
| 3002   | Layout 1             | `ac3f08824123`  |
| 2995   | Layout 1             | `ac3f08824123`  |
| 2987   | Layout 1             | `ac3f08824123`  |
| 2978   | Layout 1             | `ac3f08824123`  |
| 2970   | Layout 1             | `ac3f08824123`  |
| 2959   | Layout 1             | `ac3f08824123`  |
| 2951   | Layout 1             | `ac3f08824123`  |
| 2942   | Layout 1             | `ac3f08824123`  |
| 2935   | Layout 1             | `ac3f08824123`  |
| 2932   | No documented layout | `ac3f08824123`  |
| 2923   | No documented layout | `ac3f08824123`  |
| 2919   | No documented layout | `ac3f08824123`  |
| 2907   | No documented layout | `ac3f08824123`  |
| 2900   | No documented layout | `ac3f08824123`  |
| 2891   | No documented layout | `ac3f08824123`  |
| 2882   | No documented layout | `ac3f08824123`  |
| 2872   | No documented layout | `ac3f08824123`  |
| 2863   | No documented layout | `ac3f08824123`  |
| 2855   | No documented layout | `ac3f08824123`  |
| 2849   | No documented layout | `ac3f08824123`  |
| 2844   | No documented layout | `ac3f08824123`  |
| 2834   | No documented layout | `ac3f08824123`  |
| 2825   | No documented layout | `ac3f08824123`  |
| 2819   | No documented layout | `ac3f08824123`  |
| 2811   | No documented layout | `ac3f08824123`  |
| 2803   | No documented layout | `ac3f08824123`  |
| 2794   | No documented layout | `ac3f08824123`  |
| 2783   | No documented layout | `ac3f08824123`  |
| 2774   | No documented layout | `ac3f08824123`  |
| 2765   | No documented layout | `ac3f08824123`  |
| 2756   | No documented layout | `ac3f08824123`  |
| 2750   | No documented layout | `ac3f08824123`  |
| 2743   | No documented layout | `ac3f08824123`  |
| 2736   | No documented layout | `ac3f08824123`  |
| 2726   | No documented layout | `ac3f08824123`  |
| 2717   | No documented layout | `ac3f08824123`  |
| 2709   | No documented layout | `ac3f08824123`  |
| 2703   | No documented layout | `ac3f08824123`  |
| 2695   | No documented layout | `ac3f08824123`  |
| 2684   | No documented layout | `ac3f08824123`  |
| 2672   | No documented layout | `ac3f08824123`  |
| 2665   | No documented layout | `ac3f08824123`  |
| 2657   | No documented layout | `ac3f08824123`  |
| 2649   | No documented layout | `ac3f08824123`  |
| 2644   | No documented layout | `ac3f08824123`  |
| 2637   | No documented layout | `ac3f08824123`  |
| 2629   | No documented layout | `ac3f08824123`  |
| 2619   | No documented layout | `ac3f08824123`  |
| 2612   | No documented layout | `ac3f08824123`  |
| 2606   | No documented layout | `ac3f08824123`  |
| 2602   | No documented layout | `ac3f08824123`  |
| 2601   | No documented layout | `ac3f08824123`  |
| 2592   | No documented layout | `ac3f08824123`  |
| 2583   | No documented layout | `ac3f08824123`  |
| 2575   | No documented layout | `ac3f08824123`  |
| 2567   | No documented layout | `ac3f08824123`  |
| 2560   | No documented layout | `ac3f08824123`  |
| 2553   | No documented layout | `ac3f08824123`  |
| 2545   | No documented layout | `ac3f08824123`  |
| 2538   | No file              | `ac3f08824123`  |
| 2529   | No file              | `ac3f08824123`  |
| 2519   | No file              | `ac3f08824123`  |
| 2513   | No file              | `ac3f08824123`  |
| 2510   | No file              | `ac3f08824123`  |
| 2507   | No file              | `ac3f08824123`  |
| 2503   | No file              | `ac3f08824123`  |
| 2498   | No file              | `ac3f08824123`  |
| 2492   | No file              | `ac3f08824123`  |
| 2487   | No file              | `ac3f08824123`  |
| 2480   | No file              | `ac3f08824123`  |
| 2474   | No file              | `ac3f08824123`  |
| 2468   | No file              | `ac3f08824123`  |
| 2460   | No file              | `ac3f08824123`  |
| 2453   | No file              | `ac3f08824123`  |
| 2444   | No file              | `ac3f08824123`  |
| 2438   | No file              | `ac3f08824123`  |
| 2434   | No file              | `ac3f08824123`  |
| 2429   | No file              | `ac3f08824123`  |
| 2421   | No file              | `ac3f08824123`  |
| 2414   | No file              | `ac3f08824123`  |
| 2407   | No file              | `ac3f08824123`  |
| 2401   | No file              | `ac3f08824123`  |
| 2397   | No file              | `ac3f08824123`  |
| 2393   | No file              | `ac3f08824123`  |
| 2384   | No file              | `ac3f08824123`  |
| 2378   | No file              | `ac3f08824123`  |
| 2372   | No file              | `ac3f08824123`  |
| 2358   | No file              | `ac3f08824123`  |
| 2352   | No file              | `ac3f08824123`  |
| 2347   | No file              | `ac3f08824123`  |
| 2343   | No file              | `ac3f08824123`  |
| 2335   | No file              | `ac3f08824123`  |
| 2327   | No file              | `ac3f08824123`  |
| 2324   | No file              | `ac3f08824123`  |
| 2319   | No file              | `ac3f08824123`  |
| 2313   | No file              | `ac3f08824123`  |
| 2308   | No file              | `ac3f08824123`  |
| 2302   | No file              | `ac3f08824123`  |
| 2295   | No file              | `ac3f08824123`  |
| 2290   | No file              | `ac3f08824123`  |
| 2284   | No file              | `ac3f08824123`  |
| 2276   | No file              | `ac3f08824123`  |
| 2269   | No file              | `ac3f08824123`  |
| 2259   | No file              | `ac3f08824123`  |
| 2250   | No file              | `ac3f08824123`  |
| 2243   | No file              | `ac3f08824123`  |
| 2235   | No file              | `ac3f08824123`  |
| 2229   | No file              | `ac3f08824123`  |
| 2224   | No file              | `ac3f08824123`  |
| 2218   | No file              | `ac3f08824123`  |
| 2215   | No file              | `ac3f08824123`  |
| 2207   | No file              | `ac3f08824123`  |
| 2203   | No file              | `ac3f08824123`  |
| 2196   | No file              | `ac3f08824123`  |
| 2192   | No file              | `ac3f08824123`  |
| 2189   | No file              | `ac3f08824123`  |
| 2183   | No file              | `ac3f08824123`  |
| 2179   | No file              | `ac3f08824123`  |
| 2171   | No file              | `ac3f08824123`  |
| 2163   | No file              | `ac3f08824123`  |
| 2156   | No file              | `ac3f08824123`  |
| 2151   | No file              | `ac3f08824123`  |
| 2147   | No file              | `ac3f08824123`  |
| 2142   | No file              | `ac3f08824123`  |
| 2138   | No file              | `ac3f08824123`  |
| 2134   | No file              | `ac3f08824123`  |
| 2130   | No file              | `ac3f08824123`  |
| 2122   | No file              | `ac3f08824123`  |
| 2107   | No file              | `ac3f08824123`  |
| 2098   | No file              | `ac3f08824123`  |
| 2089   | No file              | `ac3f08824123`  |
| 2081   | No file              | `ac3f08824123`  |
| 2073   | No file              | `ac3f08824123`  |
| 2067   | No file              | `ac3f08824123`  |
| 2063   | No file              | `ac3f08824123`  |
| 2059   | No file              | `ac3f08824123`  |
| 2052   | No file              | `ac3f08824123`  |
| 2044   | No file              | `ac3f08824123`  |
| 2039   | No file              | `ac3f08824123`  |
| 2032   | No file              | `ac3f08824123`  |
| 2025   | No file              | `ac3f08824123`  |
| 2011   | No file              | `ac3f08824123`  |
| 2005   | No file              | `ac3f08824123`  |
| 2000   | No file              | `ac3f08824123`  |
| 1996   | No file              | `ac3f08824123`  |
| 1991   | No file              | `ac3f08824123`  |
| 1985   | No file              | `ac3f08824123`  |
| 1980   | No file              | `ac3f08824123`  |
| 1969   | No file              | `ac3f08824123`  |
| 1964   | No file              | `ac3f08824123`  |
| 1958   | No file              | `ac3f08824123`  |
| 1950   | No file              | `ac3f08824123`  |
| 1945   | No file              | `ac3f08824123`  |
| 1937   | No file              | `ac3f08824123`  |
| 1933   | No file              | `ac3f08824123`  |
| 1927   | No file              | `ac3f08824123`  |
| 1921   | No file              | `ac3f08824123`  |
| 1914   | No file              | `ac3f08824123`  |
| 1908   | No file              | `ac3f08824123`  |
| 1897   | No file              | `ac3f08824123`  |
| 1892   | No file              | `ac3f08824123`  |
| 1886   | No file              | `ac3f08824123`  |
| 1881   | No file              | `ac3f08824123`  |
| 1871   | No file              | `ac3f08824123`  |
| 1866   | No file              | `ac3f08824123`  |
| 1862   | No file              | `ac3f08824123`  |
| 1854   | No file              | `ac3f08824123`  |
| 1846   | No file              | `ac3f08824123`  |
| 1838   | No file              | `ac3f08824123`  |
| 1832   | No file              | `ac3f08824123`  |
| 1826   | No file              | `ac3f08824123`  |
| 1822   | No file              | `ac3f08824123`  |
| 1818   | No file              | `ac3f08824123`  |
| 1804   | No file              | `ac3f08824123`  |
| 1794   | No file              | `ac3f08824123`  |
| 1790   | No file              | `ac3f08824123`  |
| 1784   | No file              | `ac3f08824123`  |
| 1774   | No file              | `ac3f08824123`  |
| 1771   | No file              | `ac3f08824123`  |
| 1762   | No file              | `ac3f08824123`  |
| 1759   | No file              | `ac3f08824123`  |
| 1754   | No file              | `ac3f08824123`  |
| 1749   | No file              | `ac3f08824123`  |
| 1743   | No file              | `ac3f08824123`  |
| 1737   | No file              | `ac3f08824123`  |
| 1731   | No file              | `ac3f08824123`  |
| 1725   | No file              | `ac3f08824123`  |
| 1717   | No file              | `ac3f08824123`  |
| 1710   | No file              | `ac3f08824123`  |
| 1704   | No file              | `ac3f08824123`  |
| 1698   | No file              | `ac3f08824123`  |
| 1690   | No file              | `ac3f08824123`  |
| 1685   | No file              | `ac3f08824123`  |
| 1680   | No file              | `ac3f08824123`  |
| 1674   | No file              | `ac3f08824123`  |
| 1668   | No file              | `ac3f08824123`  |
| 1659   | No file              | `ac3f08824123`  |
| 1649   | No file              | `ac3f08824123`  |
| 1642   | No file              | `ac3f08824123`  |
| 1636   | No file              | `ac3f08824123`  |
| 1628   | No file              | `ac3f08824123`  |
| 1622   | No file              | `ac3f08824123`  |
| 1614   | No file              | `ac3f08824123`  |
| 1608   | No file              | `ac3f08824123`  |
| 1602   | No file              | `ac3f08824123`  |
| 1598   | No file              | `ac3f08824123`  |
| 1594   | No file              | `ac3f08824123`  |
| 1590   | No file              | `ac3f08824123`  |
| 1587   | No file              | `ac3f08824123`  |
| 1584   | No file              | `ac3f08824123`  |
| 1579   | No file              | `ac3f08824123`  |
| 1572   | No file              | `ac3f08824123`  |
| 1565   | No file              | `ac3f08824123`  |
| 1559   | No file              | `ac3f08824123`  |
| 1554   | No file              | `ac3f08824123`  |
| 1547   | No file              | `ac3f08824123`  |
| 1537   | No file              | `ac3f08824123`  |
| 1529   | No file              | `ac3f08824123`  |
| 1524   | No file              | `ac3f08824123`  |
| 1519   | No file              | `ac3f08824123`  |
| 1509   | No file              | `ac3f08824123`  |
| 1506   | No file              | `ac3f08824123`  |
| 1504   | No file              | `ac3f08824123`  |
| 1500   | No file              | `ac3f08824123`  |
| 1493   | No file              | `ac3f08824123`  |
| 1489   | No file              | `ac3f08824123`  |
| 1485   | No file              | `ac3f08824123`  |
| 1481   | No file              | `ac3f08824123`  |
| 1474   | No file              | `ac3f08824123`  |
| 1466   | No file              | `ac3f08824123`  |
| 1462   | No file              | `ac3f08824123`  |
| 1459   | No file              | `ac3f08824123`  |
| 1453   | No file              | `ac3f08824123`  |
| 1450   | No file              | `ac3f08824123`  |
| 1445   | No file              | `ac3f08824123`  |
| 1439   | No file              | `ac3f08824123`  |
| 1433   | No file              | `ac3f08824123`  |
| 1430   | No file              | `ac3f08824123`  |
| 1426   | No file              | `ac3f08824123`  |
| 1421   | No file              | `ac3f08824123`  |
| 1417   | No file              | `ac3f08824123`  |
| 1416   | No file              | `ac3f08824123`  |
| 1409   | No file              | `ac3f08824123`  |
| 1405   | No file              | `ac3f08824123`  |
| 1401   | No file              | `ac3f08824123`  |
| 1396   | No file              | `ac3f08824123`  |
| 1391   | No file              | `ac3f08824123`  |
| 1390   | No file              | `ac3f08824123`  |
| 1386   | No file              | `ac3f08824123`  |
| 1381   | No file              | `ac3f08824123`  |
| 1379   | No file              | `ac3f08824123`  |
| 1372   | No file              | `ac3f08824123`  |
| 1366   | No file              | `ac3f08824123`  |
| 1364   | No file              | `ac3f08824123`  |
| 1363   | No file              | `ac3f08824123`  |
| 1360   | No file              | `ac3f08824123`  |
| 1358   | No file              | `ac3f08824123`  |
| 1355   | No file              | `ac3f08824123`  |
| 1351   | No file              | `ac3f08824123`  |
| 1348   | No file              | `ac3f08824123`  |
| 1346   | No file              | `ac3f08824123`  |
| 1341   | No file              | `ac3f08824123`  |
| 1340   | No file              | `ac3f08824123`  |
| 1338   | No file              | `ac3f08824123`  |
| 1335   | No file              | `ac3f08824123`  |
| 1333   | No file              | `ac3f08824123`  |
| 1329   | No file              | `ac3f08824123`  |
| 1327   | No file              | `ac3f08824123`  |
| 1324   | No file              | `ac3f08824123`  |
| 1321   | No file              | `ac3f08824123`  |
| 1319   | No file              | `ac3f08824123`  |
| 1318   | No file              | `ac3f08824123`  |
| 1316   | No file              | `ac3f08824123`  |
| 1313   | No file              | `ac3f08824123`  |
| 1311   | No file              | `ac3f08824123`  |
| 1309   | No file              | `ac3f08824123`  |
| 1304   | No file              | `ac3f08824123`  |
| 1292   | No file              | `ac3f08824123`  |
| 1286   | No file              | `ac3f08824123`  |
| 1280   | No file              | `ac3f08824123`  |
| 1276   | No file              | `ac3f08824123`  |
| 1267   | No file              | `ac3f08824123`  |
| 1261   | No file              | `ac3f08824123`  |
| 1256   | No file              | `ac3f08824123`  |
| 1250   | No file              | `ac3f08824123`  |
| 1246   | No file              | `ac3f08824123`  |
| 1239   | No file              | `ac3f08824123`  |
| 1230   | No file              | `ac3f08824123`  |
| 1226   | No file              | `ac3f08824123`  |
| 1220   | No file              | `ac3f08824123`  |
| 1217   | No file              | `ac3f08824123`  |
| 1211   | No file              | `ac3f08824123`  |
| 1210   | No file              | `ac3f08824123`  |
| 1208   | No file              | `ac3f08824123`  |
| 1203   | No file              | `ac3f08824123`  |
| 1197   | No file              | `ac3f08824123`  |
| 1194   | No file              | `ac3f08824123`  |
| 1192   | No file              | `ac3f08824123`  |
| 1187   | No file              | `ac3f08824123`  |
| 1183   | No file              | `ac3f08824123`  |
| 1177   | No file              | `ac3f08824123`  |
| 1173   | No file              | `ac3f08824123`  |
| 1167   | No file              | `ac3f08824123`  |
| 1164   | No file              | `ac3f08824123`  |
| 1156   | No file              | `ac3f08824123`  |
| 1149   | No file              | `ac3f08824123`  |
| 1144   | No file              | `ac3f08824123`  |
| 1137   | No file              | `ac3f08824123`  |
| 1132   | No file              | `ac3f08824123`  |
| 1127   | No file              | `ac3f08824123`  |
| 1122   | No file              | `ac3f08824123`  |
| 1118   | No file              | `ac3f08824123`  |
| 1114   | No file              | `ac3f08824123`  |
| 1109   | No file              | `ac3f08824123`  |
| 1102   | No file              | `ac3f08824123`  |
| 1096   | No file              | `ac3f08824123`  |
| 1088   | No file              | `ac3f08824123`  |
| 1081   | No file              | `ac3f08824123`  |
| 1076   | No file              | `ac3f08824123`  |
| 1069   | No file              | `ac3f08824123`  |
| 1064   | No file              | `ac3f08824123`  |
| 1058   | No file              | `ac3f08824123`  |
| 1051   | No file              | `ac3f08824123`  |
| 1044   | No file              | `ac3f08824123`  |
| 1036   | No file              | `ac3f08824123`  |
| 1026   | No file              | `ac3f08824123`  |
| 1016   | No file              | `ac3f08824123`  |
| 1009   | No file              | `ac3f08824123`  |
| 1005   | No file              | `ac3f08824123`  |
| 1000   | No file              | `ac3f08824123`  |
| 998    | No file              | `ac3f08824123`  |
| 990    | No file              | `ac3f08824123`  |
| 979    | No file              | `ac3f08824123`  |
| 972    | No file              | `ac3f08824123`  |
| 963    | No file              | `ac3f08824123`  |
| 955    | No file              | `ac3f08824123`  |
| 946    | No file              | `ac3f08824123`  |
| 938    | No file              | `ac3f08824123`  |
| 927    | No file              | `ac3f08824123`  |
| 911    | No file              | `ac3f08824123`  |
| 904    | No file              | `ac3f08824123`  |
| 899    | No file              | `ac3f08824123`  |
| 894    | No file              | `ac3f08824123`  |
| 885    | No file              | `ac3f08824123`  |
| 879    | No file              | `ac3f08824123`  |
| 872    | No file              | `ac3f08824123`  |
| 864    | No file              | `ac3f08824123`  |
| 855    | No file              | `ac3f08824123`  |
| 853    | No file              | `ac3f08824123`  |
| 845    | No file              | `ac3f08824123`  |
| 837    | No file              | `ac3f08824123`  |
| 829    | No file              | `ac3f08824123`  |
| 822    | No file              | `ac3f08824123`  |
| 814    | No file              | `ac3f08824123`  |
| 805    | No file              | `ac3f08824123`  |
| 794    | No file              | `ac3f08824123`  |
| 787    | No file              | `ac3f08824123`  |
| 780    | No file              | `ac3f08824123`  |
| 771    | No file              | `ac3f08824123`  |
| 760    | No file              | `ac3f08824123`  |
| 748    | No file              | `ac3f08824123`  |
| 741    | No file              | `ac3f08824123`  |
| 736    | No file              | `ac3f08824123`  |
| 731    | No file              | `ac3f08824123`  |
| 723    | No file              | `ac3f08824123`  |
| 711    | No file              | `ac3f08824123`  |
| 707    | No file              | `ac3f08824123`  |
| 697    | No file              | `ac3f08824123`  |
| 689    | No file              | `ac3f08824123`  |
| 683    | No file              | `ac3f08824123`  |
| 678    | No file              | `ac3f08824123`  |
| 670    | No file              | `ac3f08824123`  |
| 661    | No file              | `ac3f08824123`  |
| 656    | No file              | `ac3f08824123`  |
| 652    | No file              | `ac3f08824123`  |
| 643    | No file              | `ac3f08824123`  |
| 637    | No file              | `ac3f08824123`  |
| 630    | No file              | `ac3f08824123`  |
| 627    | No file              | `ac3f08824123`  |
| 621    | No file              | `ac3f08824123`  |
| 617    | No file              | `ac3f08824123`  |
| 615    | No file              | `ac3f08824123`  |
| 606    | No file              | `ac3f08824123`  |
| 599    | No file              | `ac3f08824123`  |
| 592    | No file              | `ac3f08824123`  |
| 586    | No file              | `ac3f08824123`  |
| 577    | No file              | `ac3f08824123`  |
| 569    | No file              | `ac3f08824123`  |
| 561    | No file              | `ac3f08824123`  |
| 554    | No file              | `ac3f08824123`  |
| 542    | No file              | `ac3f08824123`  |
| 532    | No file              | `ac3f08824123`  |
| 531    | No file              | `ac3f08824123`  |
| 526    | No file              | `ac3f08824123`  |
| 521    | No file              | `ac3f08824123`  |
| 517    | No file              | `ac3f08824123`  |
| 510    | No file              | `ac3f08824123`  |
| 508    | No file              | `ac3f08824123`  |
| 504    | No file              | `ac3f08824123`  |
| 497    | No file              | `ac3f08824123`  |
| 491    | No file              | `ac3f08824123`  |
| 485    | No file              | `ac3f08824123`  |
| 478    | No file              | `ac3f08824123`  |
| 472    | No file              | `ac3f08824123`  |
| 466    | No file              | `ac3f08824123`  |
| 457    | No file              | `ac3f08824123`  |
| 452    | No file              | `ac3f08824123`  |
| 449    | No file              | `ac3f08824123`  |
| 435    | No file              | `ac3f08824123`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                      |
| --------------------- | -------- | ------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `2` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 33 bytes + rewards)

| Offset                 | Type                         | Field                | Notes                                                     |
| ---------------------- | ---------------------------- | -------------------- | --------------------------------------------------------- |
| `+0x00`                | u64                          | win_reward_count     | Number of `win_rewards`                                   |
| `+0x08`                | Reward[win_reward_count]     | win_rewards          | Victory rewards; see Reward                               |
| `win_rewards+0x00`     | u64                          | lose_reward_count    | Number of `lose_rewards`                                  |
| `win_rewards+0x08`     | Reward[lose_reward_count]    | lose_rewards         | Defeat rewards                                            |
| `lose_rewards+0x00`    | u64                          | draw_reward_count    | Number of `draw_rewards`                                  |
| `lose_rewards+0x08`    | Reward[draw_reward_count]    | draw_rewards         | Liberation rewards                                        |
| `draw_rewards+0x00`    | u64                          | unknown_reward_count | Number of `unknown_rewards`                               |
| `draw_rewards+0x08`    | Reward[unknown_reward_count] | unknown_rewards      | Empty on the `is_guild` `0` row; see Open Questions       |
| `unknown_rewards+0x00` | u8                           | is_guild             | `0` or `1`                                                |

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                                 |
| ------- | -------- | ---------- | --------------------------------------------------------------------- |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name     |
| `+0x04` | bytes[4] | unknown_04 | `FC 7F 00 00` on every reward; see Notes                              |
| `+0x08` | u64      | count      | How many of the item                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (49 bytes)

| Offset  | Type | Field              | Notes                                                    |
| ------- | ---- | ------------------ | -------------------------------------------------------- |
| `+0x00` | u32  | win_item_id        | Victory reward box                                       |
| `+0x04` | u32  | lose_item_id       | Defeat reward box                                        |
| `+0x08` | u32  | draw_item_id       | Liberation reward box                                    |
| `+0x0C` | u32  | unknown_item_id    | `0` on the `is_guild` `0` row, `761680` on the other     |
| `+0x10` | u64  | win_item_count     | `1`                                                      |
| `+0x18` | u64  | lose_item_count    | `1`                                                      |
| `+0x20` | u64  | draw_item_count    | `1`                                                      |
| `+0x28` | u64  | unknown_item_count | `0`, or `25` with item `761680`                          |
| `+0x30` | u8   | is_guild           | `0` or `1`                                               |

## Rewards

Client 3474; the names are LOC type 0, the result in each box's "How to
Obtain" line.

| `is_guild` | List              | Items                                                             |
| ---------- | ----------------- | ----------------------------------------------------------------- |
| `0`        | `win_rewards`     | Blossoming Victory Reward x1, Combat Secret Book (XL) x1          |
| `0`        | `lose_rewards`    | Blossoming Resolve Reward x1, Combat Secret Book (M) x4           |
| `0`        | `draw_rewards`    | Blossoming Battle Reward x1, Combat Secret Book (M) x4            |
| `1`        | `win_rewards`     | Flourishing Victory Reward x1, Combat Secret Book (XL) x1         |
| `1`        | `lose_rewards`    | Flourishing Resolve Reward x1, Combat Secret Book (M) x4          |
| `1`        | `draw_rewards`    | Flourishing Battle Reward x1, Combat Secret Book (M) x4           |
| `1`        | `unknown_rewards` | [Guild] Trace of Doom x25                                         |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The menu Lua
(`panel_rosewar_menu_1.luac`, client 3474) reads the rewards with
`ToClient_GetRoseWarWinReward(isGuild, index)`,
`ToClient_GetRoseWarDrawReward` and `ToClient_GetRoseWarLoseReward`, each
with a `...RewardSize(isGuild)`, and shows them as Win, Liberation and
Lose. Each box's LOC text names its result: Victory boxes say "victory",
Resolve boxes "defeat" and Battle boxes "liberation", which fixes the list
order win, lose, draw. The Flourishing boxes say "Leading Guild" and the
Blossoming ones "Third Legion", so the row whose last byte is `1` is the
guild row.

## Notes

- Clients 3002 and 3251 use Layout 1, one item per result: the same boxes
  (3251) or items `761587` to `761589` and `761584` to `761586` (3002), one
  each, and 25 of `761680` on the guild row (118 bytes). Client 3474 turns
  each result into a list and adds the Combat Secret Books (294 bytes). The
  file is not in the archives of client 1784.
- `unknown_04` is `FC 7F 00 00` on all 13 rewards of client 3474, the upper
  half of a 64-bit pointer, as in the `0x00007FFC` groups of
  [`instancefieldmapinfo.bss`](instancefieldmapinfo_bss.md): the item ID
  sits in an 8-byte slot whose upper half the tool that wrote the file did
  not clear.
- The handler (`_bss/rosewarrewardstaticstatus/`) reads Layout 2 and shows
  one row per reward item, with the item name, the count, the result of its
  list and the guild flag.

## Open Questions

### The Fourth List

The menu Lua reads three reward lists, and the fourth list holds [Guild]
Trace of Doom on the guild row only. A reward for the guild leading the
war or for the castle owner fits, but nothing names the list.
