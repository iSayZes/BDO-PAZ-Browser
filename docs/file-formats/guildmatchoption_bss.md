# `guildmatchoption.bss` Format

## Purpose

The Guild League settings: 30 bytes of unnamed values, the reward items of
a victory and of a defeat, and a list of 93 item IDs (client 3474). The
victory reward is [Season] Guild League Victory Reward (890096) and item
890117, the defeat reward [Season] Guild League Resolve Reward (890097).
The item list holds cannon assembly kits, transformation scrolls, fences
and medical kits. The ranks are in [guildmatchrank](guildmatchrank_bss.md),
the EXP by level in [guildmatchexp](guildmatchexp_bss.md), and the guild
right to sign up for the league (right 29) in
[guildrightnewstaticstatus](guildrightnewstaticstatus_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 2434 and later | `guildmatchoption.bss` | 466   | 3 Reward Item | 12        |

| Layout | File                   | Known        | Unknown       |
| ------ | ---------------------- | ------------ | ------------- |
| 1      | `guildmatchoption.bss` | 60 B (12.9%) | 406 B (87.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `2eac91eeb378`  |
| 3482   | Layout 1             | `2eac91eeb378`  |
| 3474   | Layout 1             | `2eac91eeb378`  |
| 3473   | Layout 1             | `2eac91eeb378`  |
| 3464   | Layout 1             | `2eac91eeb378`  |
| 3458   | Layout 1             | `2eac91eeb378`  |
| 3454   | Layout 1             | `2eac91eeb378`  |
| 3444   | Layout 1             | `2eac91eeb378`  |
| 3435   | Layout 1             | `2eac91eeb378`  |
| 3426   | Layout 1             | `2eac91eeb378`  |
| 3418   | Layout 1             | `2eac91eeb378`  |
| 3412   | Layout 1             | `2eac91eeb378`  |
| 3402   | Layout 1             | `2eac91eeb378`  |
| 3396   | Layout 1             | `2eac91eeb378`  |
| 3387   | Layout 1             | `2eac91eeb378`  |
| 3381   | Layout 1             | `2eac91eeb378`  |
| 3373   | Layout 1             | `2eac91eeb378`  |
| 3364   | Layout 1             | `2eac91eeb378`  |
| 3356   | Layout 1             | `2eac91eeb378`  |
| 3349   | Layout 1             | `2eac91eeb378`  |
| 3342   | Layout 1             | `2eac91eeb378`  |
| 3335   | Layout 1             | `2eac91eeb378`  |
| 3326   | Layout 1             | `2eac91eeb378`  |
| 3321   | Layout 1             | `2eac91eeb378`  |
| 3314   | Layout 1             | `2eac91eeb378`  |
| 3303   | Layout 1             | `2eac91eeb378`  |
| 3302   | Layout 1             | `2eac91eeb378`  |
| 3293   | Layout 1             | `2eac91eeb378`  |
| 3283   | Layout 1             | `2eac91eeb378`  |
| 3275   | Layout 1             | `2eac91eeb378`  |
| 3267   | Layout 1             | `2eac91eeb378`  |
| 3258   | Layout 1             | `2eac91eeb378`  |
| 3251   | Layout 1             | `2eac91eeb378`  |
| 3242   | Layout 1             | `2eac91eeb378`  |
| 3235   | Layout 1             | `2eac91eeb378`  |
| 3229   | Layout 1             | `2eac91eeb378`  |
| 3212   | Layout 1             | `2eac91eeb378`  |
| 3203   | Layout 1             | `2eac91eeb378`  |
| 3193   | Layout 1             | `2eac91eeb378`  |
| 3186   | Layout 1             | `2eac91eeb378`  |
| 3177   | Layout 1             | `2eac91eeb378`  |
| 3169   | Layout 1             | `2eac91eeb378`  |
| 3158   | Layout 1             | `2eac91eeb378`  |
| 3151   | Layout 1             | `2eac91eeb378`  |
| 3144   | Layout 1             | `2eac91eeb378`  |
| 3133   | Layout 1             | `2eac91eeb378`  |
| 3125   | Layout 1             | `2eac91eeb378`  |
| 3118   | Layout 1             | `2eac91eeb378`  |
| 3111   | Layout 1             | `2eac91eeb378`  |
| 3103   | Layout 1             | `2eac91eeb378`  |
| 3095   | Layout 1             | `2eac91eeb378`  |
| 3086   | Layout 1             | `2eac91eeb378`  |
| 3072   | Layout 1             | `2eac91eeb378`  |
| 3062   | Layout 1             | `2eac91eeb378`  |
| 3052   | Layout 1             | `2eac91eeb378`  |
| 3045   | Layout 1             | `2eac91eeb378`  |
| 3037   | Layout 1             | `2eac91eeb378`  |
| 3030   | Layout 1             | `2eac91eeb378`  |
| 3021   | Layout 1             | `2eac91eeb378`  |
| 3012   | Layout 1             | `2eac91eeb378`  |
| 3002   | Layout 1             | `2eac91eeb378`  |
| 2995   | Layout 1             | `2eac91eeb378`  |
| 2987   | Layout 1             | `2eac91eeb378`  |
| 2978   | Layout 1             | `2eac91eeb378`  |
| 2970   | Layout 1             | `2eac91eeb378`  |
| 2959   | Layout 1             | `2eac91eeb378`  |
| 2951   | Layout 1             | `2eac91eeb378`  |
| 2942   | Layout 1             | `2eac91eeb378`  |
| 2935   | Layout 1             | `2eac91eeb378`  |
| 2932   | Layout 1             | `2eac91eeb378`  |
| 2923   | Layout 1             | `2eac91eeb378`  |
| 2919   | Layout 1             | `2eac91eeb378`  |
| 2907   | Layout 1             | `2eac91eeb378`  |
| 2900   | Layout 1             | `2eac91eeb378`  |
| 2891   | Layout 1             | `2eac91eeb378`  |
| 2882   | Layout 1             | `2eac91eeb378`  |
| 2872   | Layout 1             | `2eac91eeb378`  |
| 2863   | Layout 1             | `2eac91eeb378`  |
| 2855   | Layout 1             | `2eac91eeb378`  |
| 2849   | Layout 1             | `2eac91eeb378`  |
| 2844   | Layout 1             | `2eac91eeb378`  |
| 2834   | Layout 1             | `2eac91eeb378`  |
| 2825   | Layout 1             | `2eac91eeb378`  |
| 2819   | Layout 1             | `2eac91eeb378`  |
| 2811   | Layout 1             | `2eac91eeb378`  |
| 2803   | Layout 1             | `2eac91eeb378`  |
| 2794   | Layout 1             | `2eac91eeb378`  |
| 2783   | Layout 1             | `2eac91eeb378`  |
| 2774   | Layout 1             | `2eac91eeb378`  |
| 2765   | Layout 1             | `2eac91eeb378`  |
| 2756   | Layout 1             | `2eac91eeb378`  |
| 2750   | Layout 1             | `2eac91eeb378`  |
| 2743   | Layout 1             | `2eac91eeb378`  |
| 2736   | Layout 1             | `2eac91eeb378`  |
| 2726   | Layout 1             | `2eac91eeb378`  |
| 2717   | Layout 1             | `2eac91eeb378`  |
| 2709   | Layout 1             | `2eac91eeb378`  |
| 2703   | Layout 1             | `2eac91eeb378`  |
| 2695   | Layout 1             | `2eac91eeb378`  |
| 2684   | Layout 1             | `2eac91eeb378`  |
| 2672   | Layout 1             | `2eac91eeb378`  |
| 2665   | Layout 1             | `2eac91eeb378`  |
| 2657   | Layout 1             | `2eac91eeb378`  |
| 2649   | Layout 1             | `2eac91eeb378`  |
| 2644   | Layout 1             | `2eac91eeb378`  |
| 2637   | Layout 1             | `2eac91eeb378`  |
| 2629   | Layout 1             | `2eac91eeb378`  |
| 2619   | Layout 1             | `2eac91eeb378`  |
| 2612   | Layout 1             | `2eac91eeb378`  |
| 2606   | Layout 1             | `2eac91eeb378`  |
| 2602   | Layout 1             | `2eac91eeb378`  |
| 2601   | Layout 1             | `2eac91eeb378`  |
| 2592   | Layout 1             | `2eac91eeb378`  |
| 2583   | Layout 1             | `2eac91eeb378`  |
| 2575   | Layout 1             | `2eac91eeb378`  |
| 2567   | Layout 1             | `2eac91eeb378`  |
| 2560   | Layout 1             | `2eac91eeb378`  |
| 2553   | Layout 1             | `2eac91eeb378`  |
| 2545   | Layout 1             | `2eac91eeb378`  |
| 2538   | Layout 1             | `2eac91eeb378`  |
| 2529   | Layout 1             | `2eac91eeb378`  |
| 2519   | Layout 1             | `2eac91eeb378`  |
| 2513   | Layout 1             | `2eac91eeb378`  |
| 2510   | Layout 1             | `2eac91eeb378`  |
| 2507   | Layout 1             | `2eac91eeb378`  |
| 2503   | Layout 1             | `2eac91eeb378`  |
| 2498   | Layout 1             | `2eac91eeb378`  |
| 2492   | Layout 1             | `2eac91eeb378`  |
| 2487   | Layout 1             | `2eac91eeb378`  |
| 2480   | Layout 1             | `2eac91eeb378`  |
| 2474   | Layout 1             | `2eac91eeb378`  |
| 2468   | Layout 1             | `2eac91eeb378`  |
| 2460   | Layout 1             | `2eac91eeb378`  |
| 2453   | Layout 1             | `2eac91eeb378`  |
| 2444   | Layout 1             | `2eac91eeb378`  |
| 2438   | Layout 1             | `2eac91eeb378`  |
| 2434   | Layout 1             | `2eac91eeb378`  |
| 2429   | No documented layout | `2eac91eeb378`  |
| 2421   | No documented layout | `2eac91eeb378`  |
| 2414   | No documented layout | `2eac91eeb378`  |
| 2407   | No documented layout | `2eac91eeb378`  |
| 2401   | No documented layout | `2eac91eeb378`  |
| 2397   | No documented layout | `2eac91eeb378`  |
| 2393   | No file              | `2eac91eeb378`  |
| 2384   | No file              | `2eac91eeb378`  |
| 2378   | No file              | `2eac91eeb378`  |
| 2372   | No file              | `2eac91eeb378`  |
| 2358   | No file              | `2eac91eeb378`  |
| 2352   | No file              | `2eac91eeb378`  |
| 2347   | No file              | `2eac91eeb378`  |
| 2343   | No file              | `2eac91eeb378`  |
| 2335   | No file              | `2eac91eeb378`  |
| 2327   | No file              | `2eac91eeb378`  |
| 2324   | No file              | `2eac91eeb378`  |
| 2319   | No file              | `2eac91eeb378`  |
| 2313   | No file              | `2eac91eeb378`  |
| 2308   | No file              | `2eac91eeb378`  |
| 2302   | No file              | `2eac91eeb378`  |
| 2295   | No file              | `2eac91eeb378`  |
| 2290   | No file              | `2eac91eeb378`  |
| 2284   | No file              | `2eac91eeb378`  |
| 2276   | No file              | `2eac91eeb378`  |
| 2269   | No file              | `2eac91eeb378`  |
| 2259   | No file              | `2eac91eeb378`  |
| 2250   | No file              | `2eac91eeb378`  |
| 2243   | No file              | `2eac91eeb378`  |
| 2235   | No file              | `2eac91eeb378`  |
| 2229   | No file              | `2eac91eeb378`  |
| 2224   | No file              | `2eac91eeb378`  |
| 2218   | No file              | `2eac91eeb378`  |
| 2215   | No file              | `2eac91eeb378`  |
| 2207   | No file              | `2eac91eeb378`  |
| 2203   | No file              | `2eac91eeb378`  |
| 2196   | No file              | `2eac91eeb378`  |
| 2192   | No file              | `2eac91eeb378`  |
| 2189   | No file              | `2eac91eeb378`  |
| 2183   | No file              | `2eac91eeb378`  |
| 2179   | No file              | `2eac91eeb378`  |
| 2171   | No file              | `2eac91eeb378`  |
| 2163   | No file              | `2eac91eeb378`  |
| 2156   | No file              | `2eac91eeb378`  |
| 2151   | No file              | `2eac91eeb378`  |
| 2147   | No file              | `2eac91eeb378`  |
| 2142   | No file              | `2eac91eeb378`  |
| 2138   | No file              | `2eac91eeb378`  |
| 2134   | No file              | `2eac91eeb378`  |
| 2130   | No file              | `2eac91eeb378`  |
| 2122   | No file              | `2eac91eeb378`  |
| 2107   | No file              | `2eac91eeb378`  |
| 2098   | No file              | `2eac91eeb378`  |
| 2089   | No file              | `2eac91eeb378`  |
| 2081   | No file              | `2eac91eeb378`  |
| 2073   | No file              | `2eac91eeb378`  |
| 2067   | No file              | `2eac91eeb378`  |
| 2063   | No file              | `2eac91eeb378`  |
| 2059   | No file              | `2eac91eeb378`  |
| 2052   | No file              | `2eac91eeb378`  |
| 2044   | No file              | `2eac91eeb378`  |
| 2039   | No file              | `2eac91eeb378`  |
| 2032   | No file              | `2eac91eeb378`  |
| 2025   | No file              | `2eac91eeb378`  |
| 2011   | No file              | `2eac91eeb378`  |
| 2005   | No file              | `2eac91eeb378`  |
| 2000   | No file              | `2eac91eeb378`  |
| 1996   | No file              | `2eac91eeb378`  |
| 1991   | No file              | `2eac91eeb378`  |
| 1985   | No file              | `2eac91eeb378`  |
| 1980   | No file              | `2eac91eeb378`  |
| 1969   | No file              | `2eac91eeb378`  |
| 1964   | No file              | `2eac91eeb378`  |
| 1958   | No file              | `2eac91eeb378`  |
| 1950   | No file              | `2eac91eeb378`  |
| 1945   | No file              | `2eac91eeb378`  |
| 1937   | No file              | `2eac91eeb378`  |
| 1933   | No file              | `2eac91eeb378`  |
| 1927   | No file              | `2eac91eeb378`  |
| 1921   | No file              | `2eac91eeb378`  |
| 1914   | No file              | `2eac91eeb378`  |
| 1908   | No file              | `2eac91eeb378`  |
| 1897   | No file              | `2eac91eeb378`  |
| 1892   | No file              | `2eac91eeb378`  |
| 1886   | No file              | `2eac91eeb378`  |
| 1881   | No file              | `2eac91eeb378`  |
| 1871   | No file              | `2eac91eeb378`  |
| 1866   | No file              | `2eac91eeb378`  |
| 1862   | No file              | `2eac91eeb378`  |
| 1854   | No file              | `2eac91eeb378`  |
| 1846   | No file              | `2eac91eeb378`  |
| 1838   | No file              | `2eac91eeb378`  |
| 1832   | No file              | `2eac91eeb378`  |
| 1826   | No file              | `2eac91eeb378`  |
| 1822   | No file              | `2eac91eeb378`  |
| 1818   | No file              | `2eac91eeb378`  |
| 1804   | No file              | `2eac91eeb378`  |
| 1794   | No file              | `2eac91eeb378`  |
| 1790   | No file              | `2eac91eeb378`  |
| 1784   | No file              | `2eac91eeb378`  |
| 1774   | No file              | `2eac91eeb378`  |
| 1771   | No file              | `2eac91eeb378`  |
| 1762   | No file              | `2eac91eeb378`  |
| 1759   | No file              | `2eac91eeb378`  |
| 1754   | No file              | `2eac91eeb378`  |
| 1749   | No file              | `2eac91eeb378`  |
| 1743   | No file              | `2eac91eeb378`  |
| 1737   | No file              | `2eac91eeb378`  |
| 1731   | No file              | `2eac91eeb378`  |
| 1725   | No file              | `2eac91eeb378`  |
| 1717   | No file              | `2eac91eeb378`  |
| 1710   | No file              | `2eac91eeb378`  |
| 1704   | No file              | `2eac91eeb378`  |
| 1698   | No file              | `2eac91eeb378`  |
| 1690   | No file              | `2eac91eeb378`  |
| 1685   | No file              | `2eac91eeb378`  |
| 1680   | No file              | `2eac91eeb378`  |
| 1674   | No file              | `2eac91eeb378`  |
| 1668   | No file              | `2eac91eeb378`  |
| 1659   | No file              | `2eac91eeb378`  |
| 1649   | No file              | `2eac91eeb378`  |
| 1642   | No file              | `2eac91eeb378`  |
| 1636   | No file              | `2eac91eeb378`  |
| 1628   | No file              | `2eac91eeb378`  |
| 1622   | No file              | `2eac91eeb378`  |
| 1614   | No file              | `2eac91eeb378`  |
| 1608   | No file              | `2eac91eeb378`  |
| 1602   | No file              | `2eac91eeb378`  |
| 1598   | No file              | `2eac91eeb378`  |
| 1594   | No file              | `2eac91eeb378`  |
| 1590   | No file              | `2eac91eeb378`  |
| 1587   | No file              | `2eac91eeb378`  |
| 1584   | No file              | `2eac91eeb378`  |
| 1579   | No file              | `2eac91eeb378`  |
| 1572   | No file              | `2eac91eeb378`  |
| 1565   | No file              | `2eac91eeb378`  |
| 1559   | No file              | `2eac91eeb378`  |
| 1554   | No file              | `2eac91eeb378`  |
| 1547   | No file              | `2eac91eeb378`  |
| 1537   | No file              | `2eac91eeb378`  |
| 1529   | No file              | `2eac91eeb378`  |
| 1524   | No file              | `2eac91eeb378`  |
| 1519   | No file              | `2eac91eeb378`  |
| 1509   | No file              | `2eac91eeb378`  |
| 1506   | No file              | `2eac91eeb378`  |
| 1504   | No file              | `2eac91eeb378`  |
| 1500   | No file              | `2eac91eeb378`  |
| 1493   | No file              | `2eac91eeb378`  |
| 1489   | No file              | `2eac91eeb378`  |
| 1485   | No file              | `2eac91eeb378`  |
| 1481   | No file              | `2eac91eeb378`  |
| 1474   | No file              | `2eac91eeb378`  |
| 1466   | No file              | `2eac91eeb378`  |
| 1462   | No file              | `2eac91eeb378`  |
| 1459   | No file              | `2eac91eeb378`  |
| 1453   | No file              | `2eac91eeb378`  |
| 1450   | No file              | `2eac91eeb378`  |
| 1445   | No file              | `2eac91eeb378`  |
| 1439   | No file              | `2eac91eeb378`  |
| 1433   | No file              | `2eac91eeb378`  |
| 1430   | No file              | `2eac91eeb378`  |
| 1426   | No file              | `2eac91eeb378`  |
| 1421   | No file              | `2eac91eeb378`  |
| 1417   | No file              | `2eac91eeb378`  |
| 1416   | No file              | `2eac91eeb378`  |
| 1409   | No file              | `2eac91eeb378`  |
| 1405   | No file              | `2eac91eeb378`  |
| 1401   | No file              | `2eac91eeb378`  |
| 1396   | No file              | `2eac91eeb378`  |
| 1391   | No file              | `2eac91eeb378`  |
| 1390   | No file              | `2eac91eeb378`  |
| 1386   | No file              | `2eac91eeb378`  |
| 1381   | No file              | `2eac91eeb378`  |
| 1379   | No file              | `2eac91eeb378`  |
| 1372   | No file              | `2eac91eeb378`  |
| 1366   | No file              | `2eac91eeb378`  |
| 1364   | No file              | `2eac91eeb378`  |
| 1363   | No file              | `2eac91eeb378`  |
| 1360   | No file              | `2eac91eeb378`  |
| 1358   | No file              | `2eac91eeb378`  |
| 1355   | No file              | `2eac91eeb378`  |
| 1351   | No file              | `2eac91eeb378`  |
| 1348   | No file              | `2eac91eeb378`  |
| 1346   | No file              | `2eac91eeb378`  |
| 1341   | No file              | `2eac91eeb378`  |
| 1340   | No file              | `2eac91eeb378`  |
| 1338   | No file              | `2eac91eeb378`  |
| 1335   | No file              | `2eac91eeb378`  |
| 1333   | No file              | `2eac91eeb378`  |
| 1329   | No file              | `2eac91eeb378`  |
| 1327   | No file              | `2eac91eeb378`  |
| 1324   | No file              | `2eac91eeb378`  |
| 1321   | No file              | `2eac91eeb378`  |
| 1319   | No file              | `2eac91eeb378`  |
| 1318   | No file              | `2eac91eeb378`  |
| 1316   | No file              | `2eac91eeb378`  |
| 1313   | No file              | `2eac91eeb378`  |
| 1311   | No file              | `2eac91eeb378`  |
| 1309   | No file              | `2eac91eeb378`  |
| 1304   | No file              | `2eac91eeb378`  |
| 1292   | No file              | `2eac91eeb378`  |
| 1286   | No file              | `2eac91eeb378`  |
| 1280   | No file              | `2eac91eeb378`  |
| 1276   | No file              | `2eac91eeb378`  |
| 1267   | No file              | `2eac91eeb378`  |
| 1261   | No file              | `2eac91eeb378`  |
| 1256   | No file              | `2eac91eeb378`  |
| 1250   | No file              | `2eac91eeb378`  |
| 1246   | No file              | `2eac91eeb378`  |
| 1239   | No file              | `2eac91eeb378`  |
| 1230   | No file              | `2eac91eeb378`  |
| 1226   | No file              | `2eac91eeb378`  |
| 1220   | No file              | `2eac91eeb378`  |
| 1217   | No file              | `2eac91eeb378`  |
| 1211   | No file              | `2eac91eeb378`  |
| 1210   | No file              | `2eac91eeb378`  |
| 1208   | No file              | `2eac91eeb378`  |
| 1203   | No file              | `2eac91eeb378`  |
| 1197   | No file              | `2eac91eeb378`  |
| 1194   | No file              | `2eac91eeb378`  |
| 1192   | No file              | `2eac91eeb378`  |
| 1187   | No file              | `2eac91eeb378`  |
| 1183   | No file              | `2eac91eeb378`  |
| 1177   | No file              | `2eac91eeb378`  |
| 1173   | No file              | `2eac91eeb378`  |
| 1167   | No file              | `2eac91eeb378`  |
| 1164   | No file              | `2eac91eeb378`  |
| 1156   | No file              | `2eac91eeb378`  |
| 1149   | No file              | `2eac91eeb378`  |
| 1144   | No file              | `2eac91eeb378`  |
| 1137   | No file              | `2eac91eeb378`  |
| 1132   | No file              | `2eac91eeb378`  |
| 1127   | No file              | `2eac91eeb378`  |
| 1122   | No file              | `2eac91eeb378`  |
| 1118   | No file              | `2eac91eeb378`  |
| 1114   | No file              | `2eac91eeb378`  |
| 1109   | No file              | `2eac91eeb378`  |
| 1102   | No file              | `2eac91eeb378`  |
| 1096   | No file              | `2eac91eeb378`  |
| 1088   | No file              | `2eac91eeb378`  |
| 1081   | No file              | `2eac91eeb378`  |
| 1076   | No file              | `2eac91eeb378`  |
| 1069   | No file              | `2eac91eeb378`  |
| 1064   | No file              | `2eac91eeb378`  |
| 1058   | No file              | `2eac91eeb378`  |
| 1051   | No file              | `2eac91eeb378`  |
| 1044   | No file              | `2eac91eeb378`  |
| 1036   | No file              | `2eac91eeb378`  |
| 1026   | No file              | `2eac91eeb378`  |
| 1016   | No file              | `2eac91eeb378`  |
| 1009   | No file              | `2eac91eeb378`  |
| 1005   | No file              | `2eac91eeb378`  |
| 1000   | No file              | `2eac91eeb378`  |
| 998    | No file              | `2eac91eeb378`  |
| 990    | No file              | `2eac91eeb378`  |
| 979    | No file              | `2eac91eeb378`  |
| 972    | No file              | `2eac91eeb378`  |
| 963    | No file              | `2eac91eeb378`  |
| 955    | No file              | `2eac91eeb378`  |
| 946    | No file              | `2eac91eeb378`  |
| 938    | No file              | `2eac91eeb378`  |
| 927    | No file              | `2eac91eeb378`  |
| 911    | No file              | `2eac91eeb378`  |
| 904    | No file              | `2eac91eeb378`  |
| 899    | No file              | `2eac91eeb378`  |
| 894    | No file              | `2eac91eeb378`  |
| 885    | No file              | `2eac91eeb378`  |
| 879    | No file              | `2eac91eeb378`  |
| 872    | No file              | `2eac91eeb378`  |
| 864    | No file              | `2eac91eeb378`  |
| 855    | No file              | `2eac91eeb378`  |
| 853    | No file              | `2eac91eeb378`  |
| 845    | No file              | `2eac91eeb378`  |
| 837    | No file              | `2eac91eeb378`  |
| 829    | No file              | `2eac91eeb378`  |
| 822    | No file              | `2eac91eeb378`  |
| 814    | No file              | `2eac91eeb378`  |
| 805    | No file              | `2eac91eeb378`  |
| 794    | No file              | `2eac91eeb378`  |
| 787    | No file              | `2eac91eeb378`  |
| 780    | No file              | `2eac91eeb378`  |
| 771    | No file              | `2eac91eeb378`  |
| 760    | No file              | `2eac91eeb378`  |
| 748    | No file              | `2eac91eeb378`  |
| 741    | No file              | `2eac91eeb378`  |
| 736    | No file              | `2eac91eeb378`  |
| 731    | No file              | `2eac91eeb378`  |
| 723    | No file              | `2eac91eeb378`  |
| 711    | No file              | `2eac91eeb378`  |
| 707    | No file              | `2eac91eeb378`  |
| 697    | No file              | `2eac91eeb378`  |
| 689    | No file              | `2eac91eeb378`  |
| 683    | No file              | `2eac91eeb378`  |
| 678    | No file              | `2eac91eeb378`  |
| 670    | No file              | `2eac91eeb378`  |
| 661    | No file              | `2eac91eeb378`  |
| 656    | No file              | `2eac91eeb378`  |
| 652    | No file              | `2eac91eeb378`  |
| 643    | No file              | `2eac91eeb378`  |
| 637    | No file              | `2eac91eeb378`  |
| 630    | No file              | `2eac91eeb378`  |
| 627    | No file              | `2eac91eeb378`  |
| 621    | No file              | `2eac91eeb378`  |
| 617    | No file              | `2eac91eeb378`  |
| 615    | No file              | `2eac91eeb378`  |
| 606    | No file              | `2eac91eeb378`  |
| 599    | No file              | `2eac91eeb378`  |
| 592    | No file              | `2eac91eeb378`  |
| 586    | No file              | `2eac91eeb378`  |
| 577    | No file              | `2eac91eeb378`  |
| 569    | No file              | `2eac91eeb378`  |
| 561    | No file              | `2eac91eeb378`  |
| 554    | No file              | `2eac91eeb378`  |
| 542    | No file              | `2eac91eeb378`  |
| 532    | No file              | `2eac91eeb378`  |
| 531    | No file              | `2eac91eeb378`  |
| 526    | No file              | `2eac91eeb378`  |
| 521    | No file              | `2eac91eeb378`  |
| 517    | No file              | `2eac91eeb378`  |
| 510    | No file              | `2eac91eeb378`  |
| 508    | No file              | `2eac91eeb378`  |
| 504    | No file              | `2eac91eeb378`  |
| 497    | No file              | `2eac91eeb378`  |
| 491    | No file              | `2eac91eeb378`  |
| 485    | No file              | `2eac91eeb378`  |
| 478    | No file              | `2eac91eeb378`  |
| 472    | No file              | `2eac91eeb378`  |
| 466    | No file              | `2eac91eeb378`  |
| 457    | No file              | `2eac91eeb378`  |
| 452    | No file              | `2eac91eeb378`  |
| 449    | No file              | `2eac91eeb378`  |
| 435    | No file              | `2eac91eeb378`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                     | Type                          | Field                | Notes                                                                 |
| -------------------------- | ----------------------------- | -------------------- | --------------------------------------------------------------------- |
| `+0x00`                    | char[4]                       | magic                | ASCII `PABR`                                                          |
| `+0x04`                    | u16                           | unknown_04           | `1200` on client 3474, `1800` on 2519 to 3251                          |
| `+0x06`                    | u16                           | unknown_06           | `240` on client 3474, `120` on 2519 to 3251                            |
| `+0x08`                    | u16                           | unknown_08           | `10` on every client checked                                           |
| `+0x0A`                    | u16                           | unknown_0a           | `600` on client 3474, `1000` on 2519 to 3251                           |
| `+0x0C`                    | u16                           | unknown_0c           | `720` on client 3474, `1200` on 2519 to 3251                           |
| `+0x0E`                    | u8                            | unknown_0e           | `30` on client 3474, `50` on 2519 to 3251                              |
| `+0x0F`                    | u8                            | unknown_0f           | `3` on every client checked                                            |
| `+0x10`                    | bytes[8]                      | unknown_10           | `3c eb f4 bc e5 07 0a 03` on every client checked; see Notes           |
| `+0x18`                    | u32                           | unknown_18           | `604800` (7 days in seconds) on every client checked                   |
| `+0x1C`                    | u8                            | unknown_1c           | `4` on every client checked                                            |
| `+0x1D`                    | u8                            | unknown_1d           | `15` on every client checked                                           |
| `+0x1E`                    | u16                           | unknown_1e           | `400` on every client checked                                          |
| `+0x20`                    | u8                            | unknown_20           | `30` on every client checked                                           |
| `+0x21`                    | u8                            | unknown_21           | `15` on every client checked                                           |
| `+0x22`                    | u32                           | victory_reward_count | Number of victory reward items                                        |
| `+0x26`                    | Reward Item[victory_reward_count] | victory_reward_items | See Reward Item                                                  |
| `victory_reward_items+0x00` | u32                          | defeat_reward_count  | Number of defeat reward items                                         |
| `victory_reward_items+0x04` | Reward Item[defeat_reward_count] | defeat_reward_items | See Reward Item                                                   |
| `defeat_reward_items+0x00` | u32                           | unknown_item_count   | Number of `unknown_item_ids`                                          |
| `defeat_reward_items+0x04` | u32[unknown_item_count]       | unknown_item_ids     | Item IDs; 93 of 93 have a LOC type 0 name (client 3474); see Notes    |
| `unknown_item_ids+0x00`    | String Table                  | string_table         | See String Table                                                      |
| `string_table+0x00`        | u32                           | table_start          | Offset of the string table, where `unknown_item_ids` ends             |
| `string_table+0x04`        | u32                           | zero                 | Always `0`                                                            |

### Reward Item (12 bytes)

| Offset  | Type | Field      | Notes                                                                       |
| ------- | ---- | ---------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` |
| `+0x04` | u64  | item_count | Number of items; `1` on every entry checked                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Reward Items

| Client | Victory                                                                  | Defeat                                                                   |
| ------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| 2519   | [Event] Guild League Victory Reward (56267), Victory Combat EXP (56276)  | [Event] Guild League Resolve Reward (56268), Defeat Combat EXP (56277)   |
| 3002   | [Season] Guild League Victory Reward (767690), Victory Combat EXP (56276) | [Season] Guild League Resolve Reward (767691), Defeat Combat EXP (56277) |
| 3251   | [Season] Guild League Victory Reward (761953), Victory Combat EXP (56276) | [Season] Guild League Resolve Reward (761954), Defeat Combat EXP (56277) |
| 3474   | [Season] Guild League Victory Reward (890096), item 890117 (no LOC name)  | [Season] Guild League Resolve Reward (890097)                            |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it. The
reward lists follow the client Lua of client 3474
(`panel_guildmatch_all_1.luac`): the reward tooltip reads
`ToClient_GetGuildMatchVictoryRewardCount()`, then per entry
`ToClient_GetGuildMatchVictoryRewardItemKey(index)` and
`ToClient_GetGuildMatchVictoryRewardItemCount(index)` (a 64-bit count), and
the same three `...DepeatReward...` calls for the defeat side. Every first
entry is a Guild League Victory Reward or Resolve Reward item, in that
order. The Lua also reads `ToClient_GetGuildMatchParticipatedMaxCount()`,
`...WaitRemainTime()`, `...PlayingRemainTime()` and `...ExitRemainTime()`;
which of the unnamed values they come from is not known.

## Notes

- The file is 482 bytes on clients 2519 to 3251 (94 item IDs) and 466 on
  3474, where item 757111 left the list. Clients 1784 and 2107 do not ship
  it.
- `unknown_item_ids` holds Cannon Assembly Kits (Lynch, Trina, Vype Stoner,
  Monsterbane), transformation scrolls (MOD Oog, Crasher, the 1-day and
  7-day ones), fences ([CP] Strong Fence, Old Moon Fence) and Medical Kits.
- `unknown_10` reads `e5 07 0a 03` at `+0x14`, which as u16 `2021`, u8
  `10`, u8 `3` would be a date; the first 4 bytes fit no plain number.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the two reward lists with item names
  and counts.

## Open Questions

### Unnamed Settings

Which of `unknown_04` to `unknown_21` is the match time, the waiting time,
the exit countdown and the weekly participation cap. `unknown_04` (1800 to
1200), `unknown_0a` (1000 to 600) and `unknown_0c` (1200 to 720) all fell
on client 3474, and `unknown_18` is 7 days in seconds.

### Item ID List

What the client does with `unknown_item_ids`. The entries are cannons,
transformation scrolls, fences and medical kits, which fits
items that cannot be used in a Guild League match, but no Lua reads the
list by a name.
