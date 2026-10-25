# `monsterbuffzone.bss` Format

## Purpose

A table of the monster buff zone, the zone a Dehkia's Lantern opens: the
zone window (`panel_window_monsterbuffzone`) shows the lantern's
durability (`ToClient_GetMonsterBuffZoneCurrentEndurance()`,
`ToClient_GetMonsterBuffZoneMaxEndurance()`), the player's distance to the
zone (`ToClient_GetDistanceMonsterBuffZoneToSelfPlayer()`) and plays the
`fUI_DekiaLanterns_Alarm_01A` effect past 80% of the largest distance; its
off button asks with the `LUA_DEKIA_SUMMONOFF_MSGTITLE` text. The repair
window (`panel_window_monsterbuffzoneitemrepair`) charges the lantern with
`ToClient_GetMonsterBuffZoneMaterialItemSSW()`. None of these calls takes
a key of this file. On client 3474 the file has 10 rows, keys `0x000` to
`0x004` and `0x100` to `0x104`. The file is a u32 count and fixed rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | --------------------- | ----- | ------- | --------- |
| 1      | 2269 and later | `monsterbuffzone.bss` | 224   | 10 Row  | 22        |

| Layout | File                  | Known        | Unknown       |
| ------ | --------------------- | ------------ | ------------- |
| 1      | `monsterbuffzone.bss` | 44 B (19.6%) | 180 B (80.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c6469652aee5`  |
| 3482   | Layout 1             | `c6469652aee5`  |
| 3474   | Layout 1             | `c6469652aee5`  |
| 3473   | Layout 1             | `c6469652aee5`  |
| 3464   | Layout 1             | `c6469652aee5`  |
| 3458   | Layout 1             | `c6469652aee5`  |
| 3454   | Layout 1             | `c6469652aee5`  |
| 3444   | Layout 1             | `c6469652aee5`  |
| 3435   | Layout 1             | `c6469652aee5`  |
| 3426   | Layout 1             | `c6469652aee5`  |
| 3418   | Layout 1             | `c6469652aee5`  |
| 3412   | Layout 1             | `c6469652aee5`  |
| 3402   | Layout 1             | `c6469652aee5`  |
| 3396   | Layout 1             | `c6469652aee5`  |
| 3387   | Layout 1             | `c6469652aee5`  |
| 3381   | Layout 1             | `c6469652aee5`  |
| 3373   | Layout 1             | `c6469652aee5`  |
| 3364   | Layout 1             | `c6469652aee5`  |
| 3356   | Layout 1             | `c6469652aee5`  |
| 3349   | Layout 1             | `c6469652aee5`  |
| 3342   | Layout 1             | `c6469652aee5`  |
| 3335   | Layout 1             | `c6469652aee5`  |
| 3326   | Layout 1             | `c6469652aee5`  |
| 3321   | Layout 1             | `c6469652aee5`  |
| 3314   | Layout 1             | `c6469652aee5`  |
| 3303   | Layout 1             | `c6469652aee5`  |
| 3302   | Layout 1             | `c6469652aee5`  |
| 3293   | Layout 1             | `c6469652aee5`  |
| 3283   | Layout 1             | `c6469652aee5`  |
| 3275   | Layout 1             | `c6469652aee5`  |
| 3267   | Layout 1             | `c6469652aee5`  |
| 3258   | Layout 1             | `c6469652aee5`  |
| 3251   | Layout 1             | `c6469652aee5`  |
| 3242   | Layout 1             | `c6469652aee5`  |
| 3235   | Layout 1             | `c6469652aee5`  |
| 3229   | Layout 1             | `c6469652aee5`  |
| 3212   | Layout 1             | `c6469652aee5`  |
| 3203   | Layout 1             | `c6469652aee5`  |
| 3193   | Layout 1             | `c6469652aee5`  |
| 3186   | Layout 1             | `c6469652aee5`  |
| 3177   | Layout 1             | `c6469652aee5`  |
| 3169   | Layout 1             | `c6469652aee5`  |
| 3158   | Layout 1             | `c6469652aee5`  |
| 3151   | Layout 1             | `c6469652aee5`  |
| 3144   | Layout 1             | `c6469652aee5`  |
| 3133   | Layout 1             | `c6469652aee5`  |
| 3125   | Layout 1             | `c6469652aee5`  |
| 3118   | Layout 1             | `c6469652aee5`  |
| 3111   | Layout 1             | `c6469652aee5`  |
| 3103   | Layout 1             | `c6469652aee5`  |
| 3095   | Layout 1             | `c6469652aee5`  |
| 3086   | Layout 1             | `c6469652aee5`  |
| 3072   | Layout 1             | `c6469652aee5`  |
| 3062   | Layout 1             | `c6469652aee5`  |
| 3052   | Layout 1             | `c6469652aee5`  |
| 3045   | Layout 1             | `c6469652aee5`  |
| 3037   | Layout 1             | `c6469652aee5`  |
| 3030   | Layout 1             | `c6469652aee5`  |
| 3021   | Layout 1             | `c6469652aee5`  |
| 3012   | Layout 1             | `c6469652aee5`  |
| 3002   | Layout 1             | `c6469652aee5`  |
| 2995   | Layout 1             | `c6469652aee5`  |
| 2987   | Layout 1             | `c6469652aee5`  |
| 2978   | Layout 1             | `c6469652aee5`  |
| 2970   | Layout 1             | `c6469652aee5`  |
| 2959   | Layout 1             | `c6469652aee5`  |
| 2951   | Layout 1             | `c6469652aee5`  |
| 2942   | Layout 1             | `c6469652aee5`  |
| 2935   | Layout 1             | `c6469652aee5`  |
| 2932   | Layout 1             | `c6469652aee5`  |
| 2923   | Layout 1             | `c6469652aee5`  |
| 2919   | Layout 1             | `c6469652aee5`  |
| 2907   | Layout 1             | `c6469652aee5`  |
| 2900   | Layout 1             | `c6469652aee5`  |
| 2891   | Layout 1             | `c6469652aee5`  |
| 2882   | Layout 1             | `c6469652aee5`  |
| 2872   | Layout 1             | `c6469652aee5`  |
| 2863   | Layout 1             | `c6469652aee5`  |
| 2855   | Layout 1             | `c6469652aee5`  |
| 2849   | Layout 1             | `c6469652aee5`  |
| 2844   | Layout 1             | `c6469652aee5`  |
| 2834   | Layout 1             | `c6469652aee5`  |
| 2825   | Layout 1             | `c6469652aee5`  |
| 2819   | Layout 1             | `c6469652aee5`  |
| 2811   | Layout 1             | `c6469652aee5`  |
| 2803   | Layout 1             | `c6469652aee5`  |
| 2794   | Layout 1             | `c6469652aee5`  |
| 2783   | Layout 1             | `c6469652aee5`  |
| 2774   | Layout 1             | `c6469652aee5`  |
| 2765   | Layout 1             | `c6469652aee5`  |
| 2756   | Layout 1             | `c6469652aee5`  |
| 2750   | Layout 1             | `c6469652aee5`  |
| 2743   | Layout 1             | `c6469652aee5`  |
| 2736   | Layout 1             | `c6469652aee5`  |
| 2726   | Layout 1             | `c6469652aee5`  |
| 2717   | Layout 1             | `c6469652aee5`  |
| 2709   | Layout 1             | `c6469652aee5`  |
| 2703   | Layout 1             | `c6469652aee5`  |
| 2695   | Layout 1             | `c6469652aee5`  |
| 2684   | Layout 1             | `c6469652aee5`  |
| 2672   | Layout 1             | `c6469652aee5`  |
| 2665   | Layout 1             | `c6469652aee5`  |
| 2657   | Layout 1             | `c6469652aee5`  |
| 2649   | Layout 1             | `c6469652aee5`  |
| 2644   | Layout 1             | `c6469652aee5`  |
| 2637   | Layout 1             | `c6469652aee5`  |
| 2629   | Layout 1             | `c6469652aee5`  |
| 2619   | Layout 1             | `c6469652aee5`  |
| 2612   | Layout 1             | `c6469652aee5`  |
| 2606   | Layout 1             | `c6469652aee5`  |
| 2602   | Layout 1             | `c6469652aee5`  |
| 2601   | Layout 1             | `c6469652aee5`  |
| 2592   | Layout 1             | `c6469652aee5`  |
| 2583   | Layout 1             | `c6469652aee5`  |
| 2575   | Layout 1             | `c6469652aee5`  |
| 2567   | Layout 1             | `c6469652aee5`  |
| 2560   | Layout 1             | `c6469652aee5`  |
| 2553   | Layout 1             | `c6469652aee5`  |
| 2545   | Layout 1             | `c6469652aee5`  |
| 2538   | Layout 1             | `c6469652aee5`  |
| 2529   | Layout 1             | `c6469652aee5`  |
| 2519   | Layout 1             | `c6469652aee5`  |
| 2513   | Layout 1             | `c6469652aee5`  |
| 2510   | Layout 1             | `c6469652aee5`  |
| 2507   | Layout 1             | `c6469652aee5`  |
| 2503   | Layout 1             | `c6469652aee5`  |
| 2498   | Layout 1             | `c6469652aee5`  |
| 2492   | Layout 1             | `c6469652aee5`  |
| 2487   | Layout 1             | `c6469652aee5`  |
| 2480   | Layout 1             | `c6469652aee5`  |
| 2474   | Layout 1             | `c6469652aee5`  |
| 2468   | Layout 1             | `c6469652aee5`  |
| 2460   | Layout 1             | `c6469652aee5`  |
| 2453   | Layout 1             | `c6469652aee5`  |
| 2444   | Layout 1             | `c6469652aee5`  |
| 2438   | Layout 1             | `c6469652aee5`  |
| 2434   | Layout 1             | `c6469652aee5`  |
| 2429   | Layout 1             | `c6469652aee5`  |
| 2421   | Layout 1             | `c6469652aee5`  |
| 2414   | Layout 1             | `c6469652aee5`  |
| 2407   | Layout 1             | `c6469652aee5`  |
| 2401   | Layout 1             | `c6469652aee5`  |
| 2397   | Layout 1             | `c6469652aee5`  |
| 2393   | Layout 1             | `c6469652aee5`  |
| 2384   | Layout 1             | `c6469652aee5`  |
| 2378   | Layout 1             | `c6469652aee5`  |
| 2372   | Layout 1             | `c6469652aee5`  |
| 2358   | Layout 1             | `c6469652aee5`  |
| 2352   | Layout 1             | `c6469652aee5`  |
| 2347   | Layout 1             | `c6469652aee5`  |
| 2343   | Layout 1             | `c6469652aee5`  |
| 2335   | Layout 1             | `c6469652aee5`  |
| 2327   | Layout 1             | `c6469652aee5`  |
| 2324   | Layout 1             | `c6469652aee5`  |
| 2319   | Layout 1             | `c6469652aee5`  |
| 2313   | Layout 1             | `c6469652aee5`  |
| 2308   | Layout 1             | `c6469652aee5`  |
| 2302   | Layout 1             | `c6469652aee5`  |
| 2295   | Layout 1             | `c6469652aee5`  |
| 2290   | Layout 1             | `c6469652aee5`  |
| 2284   | Layout 1             | `c6469652aee5`  |
| 2276   | Layout 1             | `c6469652aee5`  |
| 2269   | Layout 1             | `c6469652aee5`  |
| 2259   | No documented layout | `c6469652aee5`  |
| 2250   | No documented layout | `c6469652aee5`  |
| 2243   | No documented layout | `c6469652aee5`  |
| 2235   | No file              | `c6469652aee5`  |
| 2229   | No file              | `c6469652aee5`  |
| 2224   | No file              | `c6469652aee5`  |
| 2218   | No file              | `c6469652aee5`  |
| 2215   | No file              | `c6469652aee5`  |
| 2207   | No file              | `c6469652aee5`  |
| 2203   | No file              | `c6469652aee5`  |
| 2196   | No file              | `c6469652aee5`  |
| 2192   | No file              | `c6469652aee5`  |
| 2189   | No file              | `c6469652aee5`  |
| 2183   | No file              | `c6469652aee5`  |
| 2179   | No file              | `c6469652aee5`  |
| 2171   | No file              | `c6469652aee5`  |
| 2163   | No file              | `c6469652aee5`  |
| 2156   | No file              | `c6469652aee5`  |
| 2151   | No file              | `c6469652aee5`  |
| 2147   | No file              | `c6469652aee5`  |
| 2142   | No file              | `c6469652aee5`  |
| 2138   | No file              | `c6469652aee5`  |
| 2134   | No file              | `c6469652aee5`  |
| 2130   | No file              | `c6469652aee5`  |
| 2122   | No file              | `c6469652aee5`  |
| 2107   | No file              | `c6469652aee5`  |
| 2098   | No file              | `c6469652aee5`  |
| 2089   | No file              | `c6469652aee5`  |
| 2081   | No file              | `c6469652aee5`  |
| 2073   | No file              | `c6469652aee5`  |
| 2067   | No file              | `c6469652aee5`  |
| 2063   | No file              | `c6469652aee5`  |
| 2059   | No file              | `c6469652aee5`  |
| 2052   | No file              | `c6469652aee5`  |
| 2044   | No file              | `c6469652aee5`  |
| 2039   | No file              | `c6469652aee5`  |
| 2032   | No file              | `c6469652aee5`  |
| 2025   | No file              | `c6469652aee5`  |
| 2011   | No file              | `c6469652aee5`  |
| 2005   | No file              | `c6469652aee5`  |
| 2000   | No file              | `c6469652aee5`  |
| 1996   | No file              | `c6469652aee5`  |
| 1991   | No file              | `c6469652aee5`  |
| 1985   | No file              | `c6469652aee5`  |
| 1980   | No file              | `c6469652aee5`  |
| 1969   | No file              | `c6469652aee5`  |
| 1964   | No file              | `c6469652aee5`  |
| 1958   | No file              | `c6469652aee5`  |
| 1950   | No file              | `c6469652aee5`  |
| 1945   | No file              | `c6469652aee5`  |
| 1937   | No file              | `c6469652aee5`  |
| 1933   | No file              | `c6469652aee5`  |
| 1927   | No file              | `c6469652aee5`  |
| 1921   | No file              | `c6469652aee5`  |
| 1914   | No file              | `c6469652aee5`  |
| 1908   | No file              | `c6469652aee5`  |
| 1897   | No file              | `c6469652aee5`  |
| 1892   | No file              | `c6469652aee5`  |
| 1886   | No file              | `c6469652aee5`  |
| 1881   | No file              | `c6469652aee5`  |
| 1871   | No file              | `c6469652aee5`  |
| 1866   | No file              | `c6469652aee5`  |
| 1862   | No file              | `c6469652aee5`  |
| 1854   | No file              | `c6469652aee5`  |
| 1846   | No file              | `c6469652aee5`  |
| 1838   | No file              | `c6469652aee5`  |
| 1832   | No file              | `c6469652aee5`  |
| 1826   | No file              | `c6469652aee5`  |
| 1822   | No file              | `c6469652aee5`  |
| 1818   | No file              | `c6469652aee5`  |
| 1804   | No file              | `c6469652aee5`  |
| 1794   | No file              | `c6469652aee5`  |
| 1790   | No file              | `c6469652aee5`  |
| 1784   | No file              | `c6469652aee5`  |
| 1774   | No file              | `c6469652aee5`  |
| 1771   | No file              | `c6469652aee5`  |
| 1762   | No file              | `c6469652aee5`  |
| 1759   | No file              | `c6469652aee5`  |
| 1754   | No file              | `c6469652aee5`  |
| 1749   | No file              | `c6469652aee5`  |
| 1743   | No file              | `c6469652aee5`  |
| 1737   | No file              | `c6469652aee5`  |
| 1731   | No file              | `c6469652aee5`  |
| 1725   | No file              | `c6469652aee5`  |
| 1717   | No file              | `c6469652aee5`  |
| 1710   | No file              | `c6469652aee5`  |
| 1704   | No file              | `c6469652aee5`  |
| 1698   | No file              | `c6469652aee5`  |
| 1690   | No file              | `c6469652aee5`  |
| 1685   | No file              | `c6469652aee5`  |
| 1680   | No file              | `c6469652aee5`  |
| 1674   | No file              | `c6469652aee5`  |
| 1668   | No file              | `c6469652aee5`  |
| 1659   | No file              | `c6469652aee5`  |
| 1649   | No file              | `c6469652aee5`  |
| 1642   | No file              | `c6469652aee5`  |
| 1636   | No file              | `c6469652aee5`  |
| 1628   | No file              | `c6469652aee5`  |
| 1622   | No file              | `c6469652aee5`  |
| 1614   | No file              | `c6469652aee5`  |
| 1608   | No file              | `c6469652aee5`  |
| 1602   | No file              | `c6469652aee5`  |
| 1598   | No file              | `c6469652aee5`  |
| 1594   | No file              | `c6469652aee5`  |
| 1590   | No file              | `c6469652aee5`  |
| 1587   | No file              | `c6469652aee5`  |
| 1584   | No file              | `c6469652aee5`  |
| 1579   | No file              | `c6469652aee5`  |
| 1572   | No file              | `c6469652aee5`  |
| 1565   | No file              | `c6469652aee5`  |
| 1559   | No file              | `c6469652aee5`  |
| 1554   | No file              | `c6469652aee5`  |
| 1547   | No file              | `c6469652aee5`  |
| 1537   | No file              | `c6469652aee5`  |
| 1529   | No file              | `c6469652aee5`  |
| 1524   | No file              | `c6469652aee5`  |
| 1519   | No file              | `c6469652aee5`  |
| 1509   | No file              | `c6469652aee5`  |
| 1506   | No file              | `c6469652aee5`  |
| 1504   | No file              | `c6469652aee5`  |
| 1500   | No file              | `c6469652aee5`  |
| 1493   | No file              | `c6469652aee5`  |
| 1489   | No file              | `c6469652aee5`  |
| 1485   | No file              | `c6469652aee5`  |
| 1481   | No file              | `c6469652aee5`  |
| 1474   | No file              | `c6469652aee5`  |
| 1466   | No file              | `c6469652aee5`  |
| 1462   | No file              | `c6469652aee5`  |
| 1459   | No file              | `c6469652aee5`  |
| 1453   | No file              | `c6469652aee5`  |
| 1450   | No file              | `c6469652aee5`  |
| 1445   | No file              | `c6469652aee5`  |
| 1439   | No file              | `c6469652aee5`  |
| 1433   | No file              | `c6469652aee5`  |
| 1430   | No file              | `c6469652aee5`  |
| 1426   | No file              | `c6469652aee5`  |
| 1421   | No file              | `c6469652aee5`  |
| 1417   | No file              | `c6469652aee5`  |
| 1416   | No file              | `c6469652aee5`  |
| 1409   | No file              | `c6469652aee5`  |
| 1405   | No file              | `c6469652aee5`  |
| 1401   | No file              | `c6469652aee5`  |
| 1396   | No file              | `c6469652aee5`  |
| 1391   | No file              | `c6469652aee5`  |
| 1390   | No file              | `c6469652aee5`  |
| 1386   | No file              | `c6469652aee5`  |
| 1381   | No file              | `c6469652aee5`  |
| 1379   | No file              | `c6469652aee5`  |
| 1372   | No file              | `c6469652aee5`  |
| 1366   | No file              | `c6469652aee5`  |
| 1364   | No file              | `c6469652aee5`  |
| 1363   | No file              | `c6469652aee5`  |
| 1360   | No file              | `c6469652aee5`  |
| 1358   | No file              | `c6469652aee5`  |
| 1355   | No file              | `c6469652aee5`  |
| 1351   | No file              | `c6469652aee5`  |
| 1348   | No file              | `c6469652aee5`  |
| 1346   | No file              | `c6469652aee5`  |
| 1341   | No file              | `c6469652aee5`  |
| 1340   | No file              | `c6469652aee5`  |
| 1338   | No file              | `c6469652aee5`  |
| 1335   | No file              | `c6469652aee5`  |
| 1333   | No file              | `c6469652aee5`  |
| 1329   | No file              | `c6469652aee5`  |
| 1327   | No file              | `c6469652aee5`  |
| 1324   | No file              | `c6469652aee5`  |
| 1321   | No file              | `c6469652aee5`  |
| 1319   | No file              | `c6469652aee5`  |
| 1318   | No file              | `c6469652aee5`  |
| 1316   | No file              | `c6469652aee5`  |
| 1313   | No file              | `c6469652aee5`  |
| 1311   | No file              | `c6469652aee5`  |
| 1309   | No file              | `c6469652aee5`  |
| 1304   | No file              | `c6469652aee5`  |
| 1292   | No file              | `c6469652aee5`  |
| 1286   | No file              | `c6469652aee5`  |
| 1280   | No file              | `c6469652aee5`  |
| 1276   | No file              | `c6469652aee5`  |
| 1267   | No file              | `c6469652aee5`  |
| 1261   | No file              | `c6469652aee5`  |
| 1256   | No file              | `c6469652aee5`  |
| 1250   | No file              | `c6469652aee5`  |
| 1246   | No file              | `c6469652aee5`  |
| 1239   | No file              | `c6469652aee5`  |
| 1230   | No file              | `c6469652aee5`  |
| 1226   | No file              | `c6469652aee5`  |
| 1220   | No file              | `c6469652aee5`  |
| 1217   | No file              | `c6469652aee5`  |
| 1211   | No file              | `c6469652aee5`  |
| 1210   | No file              | `c6469652aee5`  |
| 1208   | No file              | `c6469652aee5`  |
| 1203   | No file              | `c6469652aee5`  |
| 1197   | No file              | `c6469652aee5`  |
| 1194   | No file              | `c6469652aee5`  |
| 1192   | No file              | `c6469652aee5`  |
| 1187   | No file              | `c6469652aee5`  |
| 1183   | No file              | `c6469652aee5`  |
| 1177   | No file              | `c6469652aee5`  |
| 1173   | No file              | `c6469652aee5`  |
| 1167   | No file              | `c6469652aee5`  |
| 1164   | No file              | `c6469652aee5`  |
| 1156   | No file              | `c6469652aee5`  |
| 1149   | No file              | `c6469652aee5`  |
| 1144   | No file              | `c6469652aee5`  |
| 1137   | No file              | `c6469652aee5`  |
| 1132   | No file              | `c6469652aee5`  |
| 1127   | No file              | `c6469652aee5`  |
| 1122   | No file              | `c6469652aee5`  |
| 1118   | No file              | `c6469652aee5`  |
| 1114   | No file              | `c6469652aee5`  |
| 1109   | No file              | `c6469652aee5`  |
| 1102   | No file              | `c6469652aee5`  |
| 1096   | No file              | `c6469652aee5`  |
| 1088   | No file              | `c6469652aee5`  |
| 1081   | No file              | `c6469652aee5`  |
| 1076   | No file              | `c6469652aee5`  |
| 1069   | No file              | `c6469652aee5`  |
| 1064   | No file              | `c6469652aee5`  |
| 1058   | No file              | `c6469652aee5`  |
| 1051   | No file              | `c6469652aee5`  |
| 1044   | No file              | `c6469652aee5`  |
| 1036   | No file              | `c6469652aee5`  |
| 1026   | No file              | `c6469652aee5`  |
| 1016   | No file              | `c6469652aee5`  |
| 1009   | No file              | `c6469652aee5`  |
| 1005   | No file              | `c6469652aee5`  |
| 1000   | No file              | `c6469652aee5`  |
| 998    | No file              | `c6469652aee5`  |
| 990    | No file              | `c6469652aee5`  |
| 979    | No file              | `c6469652aee5`  |
| 972    | No file              | `c6469652aee5`  |
| 963    | No file              | `c6469652aee5`  |
| 955    | No file              | `c6469652aee5`  |
| 946    | No file              | `c6469652aee5`  |
| 938    | No file              | `c6469652aee5`  |
| 927    | No file              | `c6469652aee5`  |
| 911    | No file              | `c6469652aee5`  |
| 904    | No file              | `c6469652aee5`  |
| 899    | No file              | `c6469652aee5`  |
| 894    | No file              | `c6469652aee5`  |
| 885    | No file              | `c6469652aee5`  |
| 879    | No file              | `c6469652aee5`  |
| 872    | No file              | `c6469652aee5`  |
| 864    | No file              | `c6469652aee5`  |
| 855    | No file              | `c6469652aee5`  |
| 853    | No file              | `c6469652aee5`  |
| 845    | No file              | `c6469652aee5`  |
| 837    | No file              | `c6469652aee5`  |
| 829    | No file              | `c6469652aee5`  |
| 822    | No file              | `c6469652aee5`  |
| 814    | No file              | `c6469652aee5`  |
| 805    | No file              | `c6469652aee5`  |
| 794    | No file              | `c6469652aee5`  |
| 787    | No file              | `c6469652aee5`  |
| 780    | No file              | `c6469652aee5`  |
| 771    | No file              | `c6469652aee5`  |
| 760    | No file              | `c6469652aee5`  |
| 748    | No file              | `c6469652aee5`  |
| 741    | No file              | `c6469652aee5`  |
| 736    | No file              | `c6469652aee5`  |
| 731    | No file              | `c6469652aee5`  |
| 723    | No file              | `c6469652aee5`  |
| 711    | No file              | `c6469652aee5`  |
| 707    | No file              | `c6469652aee5`  |
| 697    | No file              | `c6469652aee5`  |
| 689    | No file              | `c6469652aee5`  |
| 683    | No file              | `c6469652aee5`  |
| 678    | No file              | `c6469652aee5`  |
| 670    | No file              | `c6469652aee5`  |
| 661    | No file              | `c6469652aee5`  |
| 656    | No file              | `c6469652aee5`  |
| 652    | No file              | `c6469652aee5`  |
| 643    | No file              | `c6469652aee5`  |
| 637    | No file              | `c6469652aee5`  |
| 630    | No file              | `c6469652aee5`  |
| 627    | No file              | `c6469652aee5`  |
| 621    | No file              | `c6469652aee5`  |
| 617    | No file              | `c6469652aee5`  |
| 615    | No file              | `c6469652aee5`  |
| 606    | No file              | `c6469652aee5`  |
| 599    | No file              | `c6469652aee5`  |
| 592    | No file              | `c6469652aee5`  |
| 586    | No file              | `c6469652aee5`  |
| 577    | No file              | `c6469652aee5`  |
| 569    | No file              | `c6469652aee5`  |
| 561    | No file              | `c6469652aee5`  |
| 554    | No file              | `c6469652aee5`  |
| 542    | No file              | `c6469652aee5`  |
| 532    | No file              | `c6469652aee5`  |
| 531    | No file              | `c6469652aee5`  |
| 526    | No file              | `c6469652aee5`  |
| 521    | No file              | `c6469652aee5`  |
| 517    | No file              | `c6469652aee5`  |
| 510    | No file              | `c6469652aee5`  |
| 508    | No file              | `c6469652aee5`  |
| 504    | No file              | `c6469652aee5`  |
| 497    | No file              | `c6469652aee5`  |
| 491    | No file              | `c6469652aee5`  |
| 485    | No file              | `c6469652aee5`  |
| 478    | No file              | `c6469652aee5`  |
| 472    | No file              | `c6469652aee5`  |
| 466    | No file              | `c6469652aee5`  |
| 457    | No file              | `c6469652aee5`  |
| 452    | No file              | `c6469652aee5`  |
| 449    | No file              | `c6469652aee5`  |
| 435    | No file              | `c6469652aee5`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (22 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u32  | key        | Row key: second byte `0` or `1`, first byte `0` to `4` (client 3474) |
| `+0x04` | u32  | unknown_04 | `2000` on every row of client 3474                           |
| `+0x08` | u32  | unknown_08 | `1` on every row                                             |
| `+0x0C` | u32  | unknown_0c | `1` on every row                                             |
| `+0x10` | u32  | unknown_10 | `1` on every row                                             |
| `+0x14` | u8   | unknown_14 | The key's second byte                                        |
| `+0x15` | u8   | unknown_15 | The key's first byte                                         |

The rows run `0x004` down to `0x000`, then `0x104` down to `0x100`.

## Notes

- The file is not in client 1784, and no sheet of a private server's
  `DataSheets.bexcel` on client 1784 or member of the 2016 client's debug
  symbols holds it. The client 1784 server dump has no monster buff zone
  text either.
- The two key bytes repeat as the last two bytes of the row, in the order
  second byte, first byte.

## Open Questions

### What the Key Bytes Select

The rows form two sets of five (`unknown_14` `0` and `1`, `unknown_15` `0`
to `4`). LOC type 0 names five Dehkia's Lantern items (`790584` Tier 1,
`790585` Tier 2, and three more named `Dehkia's Lantern`, `790586` to
`790588`). Whether `unknown_15` is the lantern tier, and what the second
byte splits, is open; every other value is the same on all 10 rows.

### unknown_04 to unknown_10

`2000`, `1`, `1` and `1` on all 10 rows. The Lua shows a maximum distance
and a maximum durability per zone, but reads both from the client, so
neither can be matched to a value here.
