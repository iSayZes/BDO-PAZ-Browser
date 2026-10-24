# `characterlobby.bss` Format

## Purpose

The camera zoom limits of the character select and creation lobby, per
class character. A PABR list of rows; each row names a player character
key and two zoom limits of the lobby camera on it. On
client 3482 it holds 32 class characters, from key `1` (Warrior) up to
key `36`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1109 and later | 3483    | `characterlobby.bss` | 340   | 32 Row  | 10        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `characterlobby.bss` | 340 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `7e99bef69616`  |
| 3482   | Layout 1 | `7e99bef69616`  |
| 3474   | Layout 1 | `7e99bef69616`  |
| 3473   | Layout 1 | `7e99bef69616`  |
| 3464   | Layout 1 | `7e99bef69616`  |
| 3458   | Layout 1 | `7e99bef69616`  |
| 3454   | Layout 1 | `7e99bef69616`  |
| 3444   | Layout 1 | `7e99bef69616`  |
| 3435   | Layout 1 | `7e99bef69616`  |
| 3426   | Layout 1 | `7e99bef69616`  |
| 3418   | Layout 1 | `7e99bef69616`  |
| 3412   | Layout 1 | `7e99bef69616`  |
| 3402   | Layout 1 | `7e99bef69616`  |
| 3396   | Layout 1 | `7e99bef69616`  |
| 3387   | Layout 1 | `7e99bef69616`  |
| 3381   | Layout 1 | `7e99bef69616`  |
| 3373   | Layout 1 | `7e99bef69616`  |
| 3364   | Layout 1 | `7e99bef69616`  |
| 3356   | Layout 1 | `7e99bef69616`  |
| 3349   | Layout 1 | `7e99bef69616`  |
| 3342   | Layout 1 | `7e99bef69616`  |
| 3335   | Layout 1 | `7e99bef69616`  |
| 3326   | Layout 1 | `7e99bef69616`  |
| 3321   | Layout 1 | `7e99bef69616`  |
| 3314   | Layout 1 | `7e99bef69616`  |
| 3303   | Layout 1 | `7e99bef69616`  |
| 3302   | Layout 1 | `7e99bef69616`  |
| 3293   | Layout 1 | `7e99bef69616`  |
| 3283   | Layout 1 | `7e99bef69616`  |
| 3275   | Layout 1 | `7e99bef69616`  |
| 3267   | Layout 1 | `7e99bef69616`  |
| 3258   | Layout 1 | `7e99bef69616`  |
| 3251   | Layout 1 | `7e99bef69616`  |
| 3242   | Layout 1 | `7e99bef69616`  |
| 3235   | Layout 1 | `7e99bef69616`  |
| 3229   | Layout 1 | `7e99bef69616`  |
| 3212   | Layout 1 | `7e99bef69616`  |
| 3203   | Layout 1 | `7e99bef69616`  |
| 3193   | Layout 1 | `7e99bef69616`  |
| 3186   | Layout 1 | `7e99bef69616`  |
| 3177   | Layout 1 | `7e99bef69616`  |
| 3169   | Layout 1 | `7e99bef69616`  |
| 3158   | Layout 1 | `7e99bef69616`  |
| 3151   | Layout 1 | `7e99bef69616`  |
| 3144   | Layout 1 | `7e99bef69616`  |
| 3133   | Layout 1 | `7e99bef69616`  |
| 3125   | Layout 1 | `7e99bef69616`  |
| 3118   | Layout 1 | `7e99bef69616`  |
| 3111   | Layout 1 | `7e99bef69616`  |
| 3103   | Layout 1 | `7e99bef69616`  |
| 3095   | Layout 1 | `7e99bef69616`  |
| 3086   | Layout 1 | `7e99bef69616`  |
| 3072   | Layout 1 | `7e99bef69616`  |
| 3062   | Layout 1 | `7e99bef69616`  |
| 3052   | Layout 1 | `7e99bef69616`  |
| 3045   | Layout 1 | `7e99bef69616`  |
| 3037   | Layout 1 | `7e99bef69616`  |
| 3030   | Layout 1 | `7e99bef69616`  |
| 3021   | Layout 1 | `7e99bef69616`  |
| 3012   | Layout 1 | `7e99bef69616`  |
| 3002   | Layout 1 | `7e99bef69616`  |
| 2995   | Layout 1 | `7e99bef69616`  |
| 2987   | Layout 1 | `7e99bef69616`  |
| 2978   | Layout 1 | `7e99bef69616`  |
| 2970   | Layout 1 | `7e99bef69616`  |
| 2959   | Layout 1 | `7e99bef69616`  |
| 2951   | Layout 1 | `7e99bef69616`  |
| 2942   | Layout 1 | `7e99bef69616`  |
| 2935   | Layout 1 | `7e99bef69616`  |
| 2932   | Layout 1 | `7e99bef69616`  |
| 2923   | Layout 1 | `7e99bef69616`  |
| 2919   | Layout 1 | `7e99bef69616`  |
| 2907   | Layout 1 | `7e99bef69616`  |
| 2900   | Layout 1 | `7e99bef69616`  |
| 2891   | Layout 1 | `7e99bef69616`  |
| 2882   | Layout 1 | `7e99bef69616`  |
| 2872   | Layout 1 | `7e99bef69616`  |
| 2863   | Layout 1 | `7e99bef69616`  |
| 2855   | Layout 1 | `7e99bef69616`  |
| 2849   | Layout 1 | `7e99bef69616`  |
| 2844   | Layout 1 | `7e99bef69616`  |
| 2834   | Layout 1 | `7e99bef69616`  |
| 2825   | Layout 1 | `7e99bef69616`  |
| 2819   | Layout 1 | `7e99bef69616`  |
| 2811   | Layout 1 | `7e99bef69616`  |
| 2803   | Layout 1 | `7e99bef69616`  |
| 2794   | Layout 1 | `7e99bef69616`  |
| 2783   | Layout 1 | `7e99bef69616`  |
| 2774   | Layout 1 | `7e99bef69616`  |
| 2765   | Layout 1 | `7e99bef69616`  |
| 2756   | Layout 1 | `7e99bef69616`  |
| 2750   | Layout 1 | `7e99bef69616`  |
| 2743   | Layout 1 | `7e99bef69616`  |
| 2736   | Layout 1 | `7e99bef69616`  |
| 2726   | Layout 1 | `7e99bef69616`  |
| 2717   | Layout 1 | `7e99bef69616`  |
| 2709   | Layout 1 | `7e99bef69616`  |
| 2703   | Layout 1 | `7e99bef69616`  |
| 2695   | Layout 1 | `7e99bef69616`  |
| 2684   | Layout 1 | `7e99bef69616`  |
| 2672   | Layout 1 | `7e99bef69616`  |
| 2665   | Layout 1 | `7e99bef69616`  |
| 2657   | Layout 1 | `7e99bef69616`  |
| 2649   | Layout 1 | `7e99bef69616`  |
| 2644   | Layout 1 | `7e99bef69616`  |
| 2637   | Layout 1 | `7e99bef69616`  |
| 2629   | Layout 1 | `7e99bef69616`  |
| 2619   | Layout 1 | `7e99bef69616`  |
| 2612   | Layout 1 | `7e99bef69616`  |
| 2606   | Layout 1 | `7e99bef69616`  |
| 2602   | Layout 1 | `7e99bef69616`  |
| 2601   | Layout 1 | `7e99bef69616`  |
| 2592   | Layout 1 | `7e99bef69616`  |
| 2583   | Layout 1 | `7e99bef69616`  |
| 2575   | Layout 1 | `7e99bef69616`  |
| 2567   | Layout 1 | `7e99bef69616`  |
| 2560   | Layout 1 | `7e99bef69616`  |
| 2553   | Layout 1 | `7e99bef69616`  |
| 2545   | Layout 1 | `7e99bef69616`  |
| 2538   | Layout 1 | `7e99bef69616`  |
| 2529   | Layout 1 | `7e99bef69616`  |
| 2519   | Layout 1 | `7e99bef69616`  |
| 2513   | Layout 1 | `7e99bef69616`  |
| 2510   | Layout 1 | `7e99bef69616`  |
| 2507   | Layout 1 | `7e99bef69616`  |
| 2503   | Layout 1 | `7e99bef69616`  |
| 2498   | Layout 1 | `7e99bef69616`  |
| 2492   | Layout 1 | `7e99bef69616`  |
| 2487   | Layout 1 | `7e99bef69616`  |
| 2480   | Layout 1 | `7e99bef69616`  |
| 2474   | Layout 1 | `7e99bef69616`  |
| 2468   | Layout 1 | `7e99bef69616`  |
| 2460   | Layout 1 | `7e99bef69616`  |
| 2453   | Layout 1 | `7e99bef69616`  |
| 2444   | Layout 1 | `7e99bef69616`  |
| 2438   | Layout 1 | `7e99bef69616`  |
| 2434   | Layout 1 | `7e99bef69616`  |
| 2429   | Layout 1 | `7e99bef69616`  |
| 2421   | Layout 1 | `7e99bef69616`  |
| 2414   | Layout 1 | `7e99bef69616`  |
| 2407   | Layout 1 | `7e99bef69616`  |
| 2401   | Layout 1 | `7e99bef69616`  |
| 2397   | Layout 1 | `7e99bef69616`  |
| 2393   | Layout 1 | `7e99bef69616`  |
| 2384   | Layout 1 | `7e99bef69616`  |
| 2378   | Layout 1 | `7e99bef69616`  |
| 2372   | Layout 1 | `7e99bef69616`  |
| 2358   | Layout 1 | `7e99bef69616`  |
| 2352   | Layout 1 | `7e99bef69616`  |
| 2347   | Layout 1 | `7e99bef69616`  |
| 2343   | Layout 1 | `7e99bef69616`  |
| 2335   | Layout 1 | `7e99bef69616`  |
| 2327   | Layout 1 | `7e99bef69616`  |
| 2324   | Layout 1 | `7e99bef69616`  |
| 2319   | Layout 1 | `7e99bef69616`  |
| 2313   | Layout 1 | `7e99bef69616`  |
| 2308   | Layout 1 | `7e99bef69616`  |
| 2302   | Layout 1 | `7e99bef69616`  |
| 2295   | Layout 1 | `7e99bef69616`  |
| 2290   | Layout 1 | `7e99bef69616`  |
| 2284   | Layout 1 | `7e99bef69616`  |
| 2276   | Layout 1 | `7e99bef69616`  |
| 2269   | Layout 1 | `7e99bef69616`  |
| 2259   | Layout 1 | `7e99bef69616`  |
| 2250   | Layout 1 | `7e99bef69616`  |
| 2243   | Layout 1 | `7e99bef69616`  |
| 2235   | Layout 1 | `7e99bef69616`  |
| 2229   | Layout 1 | `7e99bef69616`  |
| 2224   | Layout 1 | `7e99bef69616`  |
| 2218   | Layout 1 | `7e99bef69616`  |
| 2215   | Layout 1 | `7e99bef69616`  |
| 2207   | Layout 1 | `7e99bef69616`  |
| 2203   | Layout 1 | `7e99bef69616`  |
| 2196   | Layout 1 | `7e99bef69616`  |
| 2192   | Layout 1 | `7e99bef69616`  |
| 2189   | Layout 1 | `7e99bef69616`  |
| 2183   | Layout 1 | `7e99bef69616`  |
| 2179   | Layout 1 | `7e99bef69616`  |
| 2171   | Layout 1 | `7e99bef69616`  |
| 2163   | Layout 1 | `7e99bef69616`  |
| 2156   | Layout 1 | `7e99bef69616`  |
| 2151   | Layout 1 | `7e99bef69616`  |
| 2147   | Layout 1 | `7e99bef69616`  |
| 2142   | Layout 1 | `7e99bef69616`  |
| 2138   | Layout 1 | `7e99bef69616`  |
| 2134   | Layout 1 | `7e99bef69616`  |
| 2130   | Layout 1 | `7e99bef69616`  |
| 2122   | Layout 1 | `7e99bef69616`  |
| 2107   | Layout 1 | `7e99bef69616`  |
| 2098   | Layout 1 | `7e99bef69616`  |
| 2089   | Layout 1 | `7e99bef69616`  |
| 2081   | Layout 1 | `7e99bef69616`  |
| 2073   | Layout 1 | `7e99bef69616`  |
| 2067   | Layout 1 | `7e99bef69616`  |
| 2063   | Layout 1 | `7e99bef69616`  |
| 2059   | Layout 1 | `7e99bef69616`  |
| 2052   | Layout 1 | `7e99bef69616`  |
| 2044   | Layout 1 | `7e99bef69616`  |
| 2039   | Layout 1 | `7e99bef69616`  |
| 2032   | Layout 1 | `7e99bef69616`  |
| 2025   | Layout 1 | `7e99bef69616`  |
| 2011   | Layout 1 | `7e99bef69616`  |
| 2005   | Layout 1 | `7e99bef69616`  |
| 2000   | Layout 1 | `7e99bef69616`  |
| 1996   | Layout 1 | `7e99bef69616`  |
| 1991   | Layout 1 | `7e99bef69616`  |
| 1985   | Layout 1 | `7e99bef69616`  |
| 1980   | Layout 1 | `7e99bef69616`  |
| 1969   | Layout 1 | `7e99bef69616`  |
| 1964   | Layout 1 | `7e99bef69616`  |
| 1958   | Layout 1 | `7e99bef69616`  |
| 1950   | Layout 1 | `7e99bef69616`  |
| 1945   | Layout 1 | `7e99bef69616`  |
| 1937   | Layout 1 | `7e99bef69616`  |
| 1933   | Layout 1 | `7e99bef69616`  |
| 1927   | Layout 1 | `7e99bef69616`  |
| 1921   | Layout 1 | `7e99bef69616`  |
| 1914   | Layout 1 | `7e99bef69616`  |
| 1908   | Layout 1 | `7e99bef69616`  |
| 1897   | Layout 1 | `7e99bef69616`  |
| 1892   | Layout 1 | `7e99bef69616`  |
| 1886   | Layout 1 | `7e99bef69616`  |
| 1881   | Layout 1 | `7e99bef69616`  |
| 1871   | Layout 1 | `7e99bef69616`  |
| 1866   | Layout 1 | `7e99bef69616`  |
| 1862   | Layout 1 | `7e99bef69616`  |
| 1854   | Layout 1 | `7e99bef69616`  |
| 1846   | Layout 1 | `7e99bef69616`  |
| 1838   | Layout 1 | `7e99bef69616`  |
| 1832   | Layout 1 | `7e99bef69616`  |
| 1826   | Layout 1 | `7e99bef69616`  |
| 1822   | Layout 1 | `7e99bef69616`  |
| 1818   | Layout 1 | `7e99bef69616`  |
| 1804   | Layout 1 | `7e99bef69616`  |
| 1794   | Layout 1 | `7e99bef69616`  |
| 1790   | Layout 1 | `7e99bef69616`  |
| 1784   | Layout 1 | `7e99bef69616`  |
| 1774   | Layout 1 | `7e99bef69616`  |
| 1771   | Layout 1 | `7e99bef69616`  |
| 1762   | Layout 1 | `7e99bef69616`  |
| 1759   | Layout 1 | `7e99bef69616`  |
| 1754   | Layout 1 | `7e99bef69616`  |
| 1749   | Layout 1 | `7e99bef69616`  |
| 1743   | Layout 1 | `7e99bef69616`  |
| 1737   | Layout 1 | `7e99bef69616`  |
| 1731   | Layout 1 | `7e99bef69616`  |
| 1725   | Layout 1 | `7e99bef69616`  |
| 1717   | Layout 1 | `7e99bef69616`  |
| 1710   | Layout 1 | `7e99bef69616`  |
| 1704   | Layout 1 | `7e99bef69616`  |
| 1698   | Layout 1 | `7e99bef69616`  |
| 1690   | Layout 1 | `7e99bef69616`  |
| 1685   | Layout 1 | `7e99bef69616`  |
| 1680   | Layout 1 | `7e99bef69616`  |
| 1674   | Layout 1 | `7e99bef69616`  |
| 1668   | Layout 1 | `7e99bef69616`  |
| 1659   | Layout 1 | `7e99bef69616`  |
| 1649   | Layout 1 | `7e99bef69616`  |
| 1642   | Layout 1 | `7e99bef69616`  |
| 1636   | Layout 1 | `7e99bef69616`  |
| 1628   | Layout 1 | `7e99bef69616`  |
| 1622   | Layout 1 | `7e99bef69616`  |
| 1614   | Layout 1 | `7e99bef69616`  |
| 1608   | Layout 1 | `7e99bef69616`  |
| 1602   | Layout 1 | `7e99bef69616`  |
| 1598   | Layout 1 | `7e99bef69616`  |
| 1594   | Layout 1 | `7e99bef69616`  |
| 1590   | Layout 1 | `7e99bef69616`  |
| 1587   | Layout 1 | `7e99bef69616`  |
| 1584   | Layout 1 | `7e99bef69616`  |
| 1579   | Layout 1 | `7e99bef69616`  |
| 1572   | Layout 1 | `7e99bef69616`  |
| 1565   | Layout 1 | `7e99bef69616`  |
| 1559   | Layout 1 | `7e99bef69616`  |
| 1554   | Layout 1 | `7e99bef69616`  |
| 1547   | Layout 1 | `7e99bef69616`  |
| 1537   | Layout 1 | `7e99bef69616`  |
| 1529   | Layout 1 | `7e99bef69616`  |
| 1524   | Layout 1 | `7e99bef69616`  |
| 1519   | Layout 1 | `7e99bef69616`  |
| 1509   | Layout 1 | `7e99bef69616`  |
| 1506   | Layout 1 | `7e99bef69616`  |
| 1504   | Layout 1 | `7e99bef69616`  |
| 1500   | Layout 1 | `7e99bef69616`  |
| 1493   | Layout 1 | `7e99bef69616`  |
| 1489   | Layout 1 | `7e99bef69616`  |
| 1485   | Layout 1 | `7e99bef69616`  |
| 1481   | Layout 1 | `7e99bef69616`  |
| 1474   | Layout 1 | `7e99bef69616`  |
| 1466   | Layout 1 | `7e99bef69616`  |
| 1462   | Layout 1 | `7e99bef69616`  |
| 1459   | Layout 1 | `7e99bef69616`  |
| 1453   | Layout 1 | `7e99bef69616`  |
| 1450   | Layout 1 | `7e99bef69616`  |
| 1445   | Layout 1 | `7e99bef69616`  |
| 1439   | Layout 1 | `7e99bef69616`  |
| 1433   | Layout 1 | `7e99bef69616`  |
| 1430   | Layout 1 | `7e99bef69616`  |
| 1426   | Layout 1 | `7e99bef69616`  |
| 1421   | Layout 1 | `7e99bef69616`  |
| 1417   | Layout 1 | `7e99bef69616`  |
| 1416   | Layout 1 | `7e99bef69616`  |
| 1409   | Layout 1 | `7e99bef69616`  |
| 1405   | Layout 1 | `7e99bef69616`  |
| 1401   | Layout 1 | `7e99bef69616`  |
| 1396   | Layout 1 | `7e99bef69616`  |
| 1391   | Layout 1 | `7e99bef69616`  |
| 1390   | Layout 1 | `7e99bef69616`  |
| 1386   | Layout 1 | `7e99bef69616`  |
| 1381   | Layout 1 | `7e99bef69616`  |
| 1379   | Layout 1 | `7e99bef69616`  |
| 1372   | Layout 1 | `7e99bef69616`  |
| 1366   | Layout 1 | `7e99bef69616`  |
| 1364   | Layout 1 | `7e99bef69616`  |
| 1363   | Layout 1 | `7e99bef69616`  |
| 1360   | Layout 1 | `7e99bef69616`  |
| 1358   | Layout 1 | `7e99bef69616`  |
| 1355   | Layout 1 | `7e99bef69616`  |
| 1351   | Layout 1 | `7e99bef69616`  |
| 1348   | Layout 1 | `7e99bef69616`  |
| 1346   | Layout 1 | `7e99bef69616`  |
| 1341   | Layout 1 | `7e99bef69616`  |
| 1340   | Layout 1 | `7e99bef69616`  |
| 1338   | Layout 1 | `7e99bef69616`  |
| 1335   | Layout 1 | `7e99bef69616`  |
| 1333   | Layout 1 | `7e99bef69616`  |
| 1329   | Layout 1 | `7e99bef69616`  |
| 1327   | Layout 1 | `7e99bef69616`  |
| 1324   | Layout 1 | `7e99bef69616`  |
| 1321   | Layout 1 | `7e99bef69616`  |
| 1319   | Layout 1 | `7e99bef69616`  |
| 1318   | Layout 1 | `7e99bef69616`  |
| 1316   | Layout 1 | `7e99bef69616`  |
| 1313   | Layout 1 | `7e99bef69616`  |
| 1311   | Layout 1 | `7e99bef69616`  |
| 1309   | Layout 1 | `7e99bef69616`  |
| 1304   | Layout 1 | `7e99bef69616`  |
| 1292   | Layout 1 | `7e99bef69616`  |
| 1286   | Layout 1 | `7e99bef69616`  |
| 1280   | Layout 1 | `7e99bef69616`  |
| 1276   | Layout 1 | `7e99bef69616`  |
| 1267   | Layout 1 | `7e99bef69616`  |
| 1261   | Layout 1 | `7e99bef69616`  |
| 1256   | Layout 1 | `7e99bef69616`  |
| 1250   | Layout 1 | `7e99bef69616`  |
| 1246   | No file  | `7e99bef69616`  |
| 1239   | No file  | `7e99bef69616`  |
| 1230   | No file  | `7e99bef69616`  |
| 1226   | No file  | `7e99bef69616`  |
| 1220   | No file  | `7e99bef69616`  |
| 1217   | No file  | `7e99bef69616`  |
| 1211   | No file  | `7e99bef69616`  |
| 1210   | No file  | `7e99bef69616`  |
| 1208   | No file  | `7e99bef69616`  |
| 1203   | No file  | `7e99bef69616`  |
| 1197   | No file  | `7e99bef69616`  |
| 1194   | No file  | `7e99bef69616`  |
| 1192   | No file  | `7e99bef69616`  |
| 1187   | No file  | `7e99bef69616`  |
| 1183   | No file  | `7e99bef69616`  |
| 1177   | No file  | `7e99bef69616`  |
| 1173   | No file  | `7e99bef69616`  |
| 1167   | No file  | `7e99bef69616`  |
| 1164   | No file  | `7e99bef69616`  |
| 1156   | No file  | `7e99bef69616`  |
| 1149   | No file  | `7e99bef69616`  |
| 1144   | Layout 1 | `7e99bef69616`  |
| 1137   | Layout 1 | `7e99bef69616`  |
| 1132   | Layout 1 | `7e99bef69616`  |
| 1127   | Layout 1 | `7e99bef69616`  |
| 1122   | Layout 1 | `7e99bef69616`  |
| 1118   | Layout 1 | `7e99bef69616`  |
| 1114   | Layout 1 | `7e99bef69616`  |
| 1109   | Layout 1 | `7e99bef69616`  |
| 1102   | No file  | `7e99bef69616`  |
| 1096   | No file  | `7e99bef69616`  |
| 1088   | No file  | `7e99bef69616`  |
| 1081   | No file  | `7e99bef69616`  |
| 1076   | No file  | `7e99bef69616`  |
| 1069   | No file  | `7e99bef69616`  |
| 1064   | No file  | `7e99bef69616`  |
| 1058   | No file  | `7e99bef69616`  |
| 1051   | No file  | `7e99bef69616`  |
| 1044   | No file  | `7e99bef69616`  |
| 1036   | No file  | `7e99bef69616`  |
| 1026   | No file  | `7e99bef69616`  |
| 1016   | No file  | `7e99bef69616`  |
| 1009   | No file  | `7e99bef69616`  |
| 1005   | No file  | `7e99bef69616`  |
| 1000   | No file  | `7e99bef69616`  |
| 998    | No file  | `7e99bef69616`  |
| 990    | No file  | `7e99bef69616`  |
| 979    | No file  | `7e99bef69616`  |
| 972    | No file  | `7e99bef69616`  |
| 963    | No file  | `7e99bef69616`  |
| 955    | No file  | `7e99bef69616`  |
| 946    | No file  | `7e99bef69616`  |
| 938    | No file  | `7e99bef69616`  |
| 927    | No file  | `7e99bef69616`  |
| 911    | No file  | `7e99bef69616`  |
| 904    | No file  | `7e99bef69616`  |
| 899    | No file  | `7e99bef69616`  |
| 894    | No file  | `7e99bef69616`  |
| 885    | No file  | `7e99bef69616`  |
| 879    | No file  | `7e99bef69616`  |
| 872    | No file  | `7e99bef69616`  |
| 864    | No file  | `7e99bef69616`  |
| 855    | No file  | `7e99bef69616`  |
| 853    | No file  | `7e99bef69616`  |
| 845    | No file  | `7e99bef69616`  |
| 837    | No file  | `7e99bef69616`  |
| 829    | No file  | `7e99bef69616`  |
| 822    | No file  | `7e99bef69616`  |
| 814    | No file  | `7e99bef69616`  |
| 805    | No file  | `7e99bef69616`  |
| 794    | No file  | `7e99bef69616`  |
| 787    | No file  | `7e99bef69616`  |
| 780    | No file  | `7e99bef69616`  |
| 771    | No file  | `7e99bef69616`  |
| 760    | No file  | `7e99bef69616`  |
| 748    | No file  | `7e99bef69616`  |
| 741    | No file  | `7e99bef69616`  |
| 736    | No file  | `7e99bef69616`  |
| 731    | No file  | `7e99bef69616`  |
| 723    | No file  | `7e99bef69616`  |
| 711    | No file  | `7e99bef69616`  |
| 707    | No file  | `7e99bef69616`  |
| 697    | No file  | `7e99bef69616`  |
| 689    | No file  | `7e99bef69616`  |
| 683    | No file  | `7e99bef69616`  |
| 678    | No file  | `7e99bef69616`  |
| 670    | No file  | `7e99bef69616`  |
| 661    | No file  | `7e99bef69616`  |
| 656    | No file  | `7e99bef69616`  |
| 652    | No file  | `7e99bef69616`  |
| 643    | No file  | `7e99bef69616`  |
| 637    | No file  | `7e99bef69616`  |
| 630    | No file  | `7e99bef69616`  |
| 627    | No file  | `7e99bef69616`  |
| 621    | No file  | `7e99bef69616`  |
| 617    | No file  | `7e99bef69616`  |
| 615    | No file  | `7e99bef69616`  |
| 606    | No file  | `7e99bef69616`  |
| 599    | No file  | `7e99bef69616`  |
| 592    | No file  | `7e99bef69616`  |
| 586    | No file  | `7e99bef69616`  |
| 577    | No file  | `7e99bef69616`  |
| 569    | No file  | `7e99bef69616`  |
| 561    | No file  | `7e99bef69616`  |
| 554    | No file  | `7e99bef69616`  |
| 542    | No file  | `7e99bef69616`  |
| 532    | No file  | `7e99bef69616`  |
| 531    | No file  | `7e99bef69616`  |
| 526    | No file  | `7e99bef69616`  |
| 521    | No file  | `7e99bef69616`  |
| 517    | No file  | `7e99bef69616`  |
| 510    | No file  | `7e99bef69616`  |
| 508    | No file  | `7e99bef69616`  |
| 504    | No file  | `7e99bef69616`  |
| 497    | No file  | `7e99bef69616`  |
| 491    | No file  | `7e99bef69616`  |
| 485    | No file  | `7e99bef69616`  |
| 478    | No file  | `7e99bef69616`  |
| 472    | No file  | `7e99bef69616`  |
| 466    | No file  | `7e99bef69616`  |
| 457    | No file  | `7e99bef69616`  |
| 452    | No file  | `7e99bef69616`  |
| 449    | No file  | `7e99bef69616`  |
| 435    | No file  | `7e99bef69616`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | Character names of `character_key`, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of class characters                    |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (10 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | character_key | Player character key (`1` Warrior, `2` Ranger, ...)                 |
| `+0x02` | f32  | zoom_in_max   | `10` to `60` on client 3482, in steps of `10`                      |
| `+0x06` | f32  | zoom_out_max  | `10` to `100` on client 3482                                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names are the `CharacterKey`, `ZoomInMax` and `ZoomOutMax` columns of
the `CharacterLobby_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784, in that order; the sheet's `CharName` column (Korean
character names such as `PC-워리어`) is not compiled. The client 1784 file
holds 44 rows and all 44 match the sheet on both zoom values. The sheet
lists key `29` twice (the young and the old Wizard, both `50` and `100`);
the file holds it once.

On client 3482, 23 of the 24 keys the file shares with the sheet match;
key `29` holds `20` and `50` there. The keys `10`, `11`, `17`, `31` and
`33` to `36` are newer than the sheet, and the sheet's keys `65001` to
`65020` (NPC lobby characters such as `클리프`) are not in the file.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/client_tables.py`, with
  the character name next to the key.

## Open Questions

### Zoom Unit

`zoom_in_max` and `zoom_out_max` keep their sheet names. No client Lua
file reads the table, so whether the values are a camera distance or a
zoom step is open. Two rows of client 3482 hold a larger `zoom_in_max`
than `zoom_out_max` (key `11`: `30` and `10`, key `24`: `60` and `50`),
so the two may not be the near and far end of one range.
