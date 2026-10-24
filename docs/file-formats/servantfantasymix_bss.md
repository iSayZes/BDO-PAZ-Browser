# `servantfantasymix.bss` Format

## Purpose

The horse pairs of the Mythical horse exchange: per pair a male and a
female horse character, how many horses the exchange makes, the Mythical
horse character it makes and the rate for that character. The exchange
window (`panel_dialog_servantexchange_fantasy_all_1.luac`, client 3482)
takes the two horses and calls `ToClient_fantasyMix(leftServantNo,
rightServantNo, ...)`; it is behind `_ContentsGroup_ServantFantasyMix`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 1433 and later | 3483    | `servantfantasymix.bss` | 258   | 17 Row  | 14        |

| Layout | File                    | Known          | Unknown    |
| ------ | ----------------------- | -------------- | ---------- |
| 1      | `servantfantasymix.bss` | 258 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e6ffbdd255dc`  |
| 3482   | Layout 1 | `e6ffbdd255dc`  |
| 3474   | Layout 1 | `e6ffbdd255dc`  |
| 3473   | Layout 1 | `e6ffbdd255dc`  |
| 3464   | Layout 1 | `e6ffbdd255dc`  |
| 3458   | Layout 1 | `e6ffbdd255dc`  |
| 3454   | Layout 1 | `e6ffbdd255dc`  |
| 3444   | Layout 1 | `e6ffbdd255dc`  |
| 3435   | Layout 1 | `e6ffbdd255dc`  |
| 3426   | Layout 1 | `e6ffbdd255dc`  |
| 3418   | Layout 1 | `e6ffbdd255dc`  |
| 3412   | Layout 1 | `e6ffbdd255dc`  |
| 3402   | Layout 1 | `e6ffbdd255dc`  |
| 3396   | Layout 1 | `e6ffbdd255dc`  |
| 3387   | Layout 1 | `e6ffbdd255dc`  |
| 3381   | Layout 1 | `e6ffbdd255dc`  |
| 3373   | Layout 1 | `e6ffbdd255dc`  |
| 3364   | Layout 1 | `e6ffbdd255dc`  |
| 3356   | Layout 1 | `e6ffbdd255dc`  |
| 3349   | Layout 1 | `e6ffbdd255dc`  |
| 3342   | Layout 1 | `e6ffbdd255dc`  |
| 3335   | Layout 1 | `e6ffbdd255dc`  |
| 3326   | Layout 1 | `e6ffbdd255dc`  |
| 3321   | Layout 1 | `e6ffbdd255dc`  |
| 3314   | Layout 1 | `e6ffbdd255dc`  |
| 3303   | Layout 1 | `e6ffbdd255dc`  |
| 3302   | Layout 1 | `e6ffbdd255dc`  |
| 3293   | Layout 1 | `e6ffbdd255dc`  |
| 3283   | Layout 1 | `e6ffbdd255dc`  |
| 3275   | Layout 1 | `e6ffbdd255dc`  |
| 3267   | Layout 1 | `e6ffbdd255dc`  |
| 3258   | Layout 1 | `e6ffbdd255dc`  |
| 3251   | Layout 1 | `e6ffbdd255dc`  |
| 3242   | Layout 1 | `e6ffbdd255dc`  |
| 3235   | Layout 1 | `e6ffbdd255dc`  |
| 3229   | Layout 1 | `e6ffbdd255dc`  |
| 3212   | Layout 1 | `e6ffbdd255dc`  |
| 3203   | Layout 1 | `e6ffbdd255dc`  |
| 3193   | Layout 1 | `e6ffbdd255dc`  |
| 3186   | Layout 1 | `e6ffbdd255dc`  |
| 3177   | Layout 1 | `e6ffbdd255dc`  |
| 3169   | Layout 1 | `e6ffbdd255dc`  |
| 3158   | Layout 1 | `e6ffbdd255dc`  |
| 3151   | Layout 1 | `e6ffbdd255dc`  |
| 3144   | Layout 1 | `e6ffbdd255dc`  |
| 3133   | Layout 1 | `e6ffbdd255dc`  |
| 3125   | Layout 1 | `e6ffbdd255dc`  |
| 3118   | Layout 1 | `e6ffbdd255dc`  |
| 3111   | Layout 1 | `e6ffbdd255dc`  |
| 3103   | Layout 1 | `e6ffbdd255dc`  |
| 3095   | Layout 1 | `e6ffbdd255dc`  |
| 3086   | Layout 1 | `e6ffbdd255dc`  |
| 3072   | Layout 1 | `e6ffbdd255dc`  |
| 3062   | Layout 1 | `e6ffbdd255dc`  |
| 3052   | Layout 1 | `e6ffbdd255dc`  |
| 3045   | Layout 1 | `e6ffbdd255dc`  |
| 3037   | Layout 1 | `e6ffbdd255dc`  |
| 3030   | Layout 1 | `e6ffbdd255dc`  |
| 3021   | Layout 1 | `e6ffbdd255dc`  |
| 3012   | Layout 1 | `e6ffbdd255dc`  |
| 3002   | Layout 1 | `e6ffbdd255dc`  |
| 2995   | Layout 1 | `e6ffbdd255dc`  |
| 2987   | Layout 1 | `e6ffbdd255dc`  |
| 2978   | Layout 1 | `e6ffbdd255dc`  |
| 2970   | Layout 1 | `e6ffbdd255dc`  |
| 2959   | Layout 1 | `e6ffbdd255dc`  |
| 2951   | Layout 1 | `e6ffbdd255dc`  |
| 2942   | Layout 1 | `e6ffbdd255dc`  |
| 2935   | Layout 1 | `e6ffbdd255dc`  |
| 2932   | Layout 1 | `e6ffbdd255dc`  |
| 2923   | Layout 1 | `e6ffbdd255dc`  |
| 2919   | Layout 1 | `e6ffbdd255dc`  |
| 2907   | Layout 1 | `e6ffbdd255dc`  |
| 2900   | Layout 1 | `e6ffbdd255dc`  |
| 2891   | Layout 1 | `e6ffbdd255dc`  |
| 2882   | Layout 1 | `e6ffbdd255dc`  |
| 2872   | Layout 1 | `e6ffbdd255dc`  |
| 2863   | Layout 1 | `e6ffbdd255dc`  |
| 2855   | Layout 1 | `e6ffbdd255dc`  |
| 2849   | Layout 1 | `e6ffbdd255dc`  |
| 2844   | Layout 1 | `e6ffbdd255dc`  |
| 2834   | Layout 1 | `e6ffbdd255dc`  |
| 2825   | Layout 1 | `e6ffbdd255dc`  |
| 2819   | Layout 1 | `e6ffbdd255dc`  |
| 2811   | Layout 1 | `e6ffbdd255dc`  |
| 2803   | Layout 1 | `e6ffbdd255dc`  |
| 2794   | Layout 1 | `e6ffbdd255dc`  |
| 2783   | Layout 1 | `e6ffbdd255dc`  |
| 2774   | Layout 1 | `e6ffbdd255dc`  |
| 2765   | Layout 1 | `e6ffbdd255dc`  |
| 2756   | Layout 1 | `e6ffbdd255dc`  |
| 2750   | Layout 1 | `e6ffbdd255dc`  |
| 2743   | Layout 1 | `e6ffbdd255dc`  |
| 2736   | Layout 1 | `e6ffbdd255dc`  |
| 2726   | Layout 1 | `e6ffbdd255dc`  |
| 2717   | Layout 1 | `e6ffbdd255dc`  |
| 2709   | Layout 1 | `e6ffbdd255dc`  |
| 2703   | Layout 1 | `e6ffbdd255dc`  |
| 2695   | Layout 1 | `e6ffbdd255dc`  |
| 2684   | Layout 1 | `e6ffbdd255dc`  |
| 2672   | Layout 1 | `e6ffbdd255dc`  |
| 2665   | Layout 1 | `e6ffbdd255dc`  |
| 2657   | Layout 1 | `e6ffbdd255dc`  |
| 2649   | Layout 1 | `e6ffbdd255dc`  |
| 2644   | Layout 1 | `e6ffbdd255dc`  |
| 2637   | Layout 1 | `e6ffbdd255dc`  |
| 2629   | Layout 1 | `e6ffbdd255dc`  |
| 2619   | Layout 1 | `e6ffbdd255dc`  |
| 2612   | Layout 1 | `e6ffbdd255dc`  |
| 2606   | Layout 1 | `e6ffbdd255dc`  |
| 2602   | Layout 1 | `e6ffbdd255dc`  |
| 2601   | Layout 1 | `e6ffbdd255dc`  |
| 2592   | Layout 1 | `e6ffbdd255dc`  |
| 2583   | Layout 1 | `e6ffbdd255dc`  |
| 2575   | Layout 1 | `e6ffbdd255dc`  |
| 2567   | Layout 1 | `e6ffbdd255dc`  |
| 2560   | Layout 1 | `e6ffbdd255dc`  |
| 2553   | Layout 1 | `e6ffbdd255dc`  |
| 2545   | Layout 1 | `e6ffbdd255dc`  |
| 2538   | Layout 1 | `e6ffbdd255dc`  |
| 2529   | Layout 1 | `e6ffbdd255dc`  |
| 2519   | Layout 1 | `e6ffbdd255dc`  |
| 2513   | Layout 1 | `e6ffbdd255dc`  |
| 2510   | Layout 1 | `e6ffbdd255dc`  |
| 2507   | Layout 1 | `e6ffbdd255dc`  |
| 2503   | Layout 1 | `e6ffbdd255dc`  |
| 2498   | Layout 1 | `e6ffbdd255dc`  |
| 2492   | Layout 1 | `e6ffbdd255dc`  |
| 2487   | Layout 1 | `e6ffbdd255dc`  |
| 2480   | Layout 1 | `e6ffbdd255dc`  |
| 2474   | Layout 1 | `e6ffbdd255dc`  |
| 2468   | Layout 1 | `e6ffbdd255dc`  |
| 2460   | Layout 1 | `e6ffbdd255dc`  |
| 2453   | Layout 1 | `e6ffbdd255dc`  |
| 2444   | Layout 1 | `e6ffbdd255dc`  |
| 2438   | Layout 1 | `e6ffbdd255dc`  |
| 2434   | Layout 1 | `e6ffbdd255dc`  |
| 2429   | Layout 1 | `e6ffbdd255dc`  |
| 2421   | Layout 1 | `e6ffbdd255dc`  |
| 2414   | Layout 1 | `e6ffbdd255dc`  |
| 2407   | Layout 1 | `e6ffbdd255dc`  |
| 2401   | Layout 1 | `e6ffbdd255dc`  |
| 2397   | Layout 1 | `e6ffbdd255dc`  |
| 2393   | Layout 1 | `e6ffbdd255dc`  |
| 2384   | Layout 1 | `e6ffbdd255dc`  |
| 2378   | Layout 1 | `e6ffbdd255dc`  |
| 2372   | Layout 1 | `e6ffbdd255dc`  |
| 2358   | Layout 1 | `e6ffbdd255dc`  |
| 2352   | Layout 1 | `e6ffbdd255dc`  |
| 2347   | Layout 1 | `e6ffbdd255dc`  |
| 2343   | Layout 1 | `e6ffbdd255dc`  |
| 2335   | Layout 1 | `e6ffbdd255dc`  |
| 2327   | Layout 1 | `e6ffbdd255dc`  |
| 2324   | Layout 1 | `e6ffbdd255dc`  |
| 2319   | Layout 1 | `e6ffbdd255dc`  |
| 2313   | Layout 1 | `e6ffbdd255dc`  |
| 2308   | Layout 1 | `e6ffbdd255dc`  |
| 2302   | Layout 1 | `e6ffbdd255dc`  |
| 2295   | Layout 1 | `e6ffbdd255dc`  |
| 2290   | Layout 1 | `e6ffbdd255dc`  |
| 2284   | Layout 1 | `e6ffbdd255dc`  |
| 2276   | Layout 1 | `e6ffbdd255dc`  |
| 2269   | Layout 1 | `e6ffbdd255dc`  |
| 2259   | Layout 1 | `e6ffbdd255dc`  |
| 2250   | Layout 1 | `e6ffbdd255dc`  |
| 2243   | Layout 1 | `e6ffbdd255dc`  |
| 2235   | Layout 1 | `e6ffbdd255dc`  |
| 2229   | Layout 1 | `e6ffbdd255dc`  |
| 2224   | Layout 1 | `e6ffbdd255dc`  |
| 2218   | Layout 1 | `e6ffbdd255dc`  |
| 2215   | Layout 1 | `e6ffbdd255dc`  |
| 2207   | Layout 1 | `e6ffbdd255dc`  |
| 2203   | Layout 1 | `e6ffbdd255dc`  |
| 2196   | Layout 1 | `e6ffbdd255dc`  |
| 2192   | Layout 1 | `e6ffbdd255dc`  |
| 2189   | Layout 1 | `e6ffbdd255dc`  |
| 2183   | Layout 1 | `e6ffbdd255dc`  |
| 2179   | Layout 1 | `e6ffbdd255dc`  |
| 2171   | Layout 1 | `e6ffbdd255dc`  |
| 2163   | Layout 1 | `e6ffbdd255dc`  |
| 2156   | Layout 1 | `e6ffbdd255dc`  |
| 2151   | Layout 1 | `e6ffbdd255dc`  |
| 2147   | Layout 1 | `e6ffbdd255dc`  |
| 2142   | Layout 1 | `e6ffbdd255dc`  |
| 2138   | Layout 1 | `e6ffbdd255dc`  |
| 2134   | Layout 1 | `e6ffbdd255dc`  |
| 2130   | Layout 1 | `e6ffbdd255dc`  |
| 2122   | Layout 1 | `e6ffbdd255dc`  |
| 2107   | Layout 1 | `e6ffbdd255dc`  |
| 2098   | Layout 1 | `e6ffbdd255dc`  |
| 2089   | Layout 1 | `e6ffbdd255dc`  |
| 2081   | Layout 1 | `e6ffbdd255dc`  |
| 2073   | Layout 1 | `e6ffbdd255dc`  |
| 2067   | Layout 1 | `e6ffbdd255dc`  |
| 2063   | Layout 1 | `e6ffbdd255dc`  |
| 2059   | Layout 1 | `e6ffbdd255dc`  |
| 2052   | Layout 1 | `e6ffbdd255dc`  |
| 2044   | Layout 1 | `e6ffbdd255dc`  |
| 2039   | Layout 1 | `e6ffbdd255dc`  |
| 2032   | Layout 1 | `e6ffbdd255dc`  |
| 2025   | Layout 1 | `e6ffbdd255dc`  |
| 2011   | Layout 1 | `e6ffbdd255dc`  |
| 2005   | Layout 1 | `e6ffbdd255dc`  |
| 2000   | Layout 1 | `e6ffbdd255dc`  |
| 1996   | Layout 1 | `e6ffbdd255dc`  |
| 1991   | Layout 1 | `e6ffbdd255dc`  |
| 1985   | Layout 1 | `e6ffbdd255dc`  |
| 1980   | Layout 1 | `e6ffbdd255dc`  |
| 1969   | Layout 1 | `e6ffbdd255dc`  |
| 1964   | Layout 1 | `e6ffbdd255dc`  |
| 1958   | Layout 1 | `e6ffbdd255dc`  |
| 1950   | Layout 1 | `e6ffbdd255dc`  |
| 1945   | Layout 1 | `e6ffbdd255dc`  |
| 1937   | Layout 1 | `e6ffbdd255dc`  |
| 1933   | Layout 1 | `e6ffbdd255dc`  |
| 1927   | Layout 1 | `e6ffbdd255dc`  |
| 1921   | Layout 1 | `e6ffbdd255dc`  |
| 1914   | Layout 1 | `e6ffbdd255dc`  |
| 1908   | Layout 1 | `e6ffbdd255dc`  |
| 1897   | Layout 1 | `e6ffbdd255dc`  |
| 1892   | Layout 1 | `e6ffbdd255dc`  |
| 1886   | Layout 1 | `e6ffbdd255dc`  |
| 1881   | Layout 1 | `e6ffbdd255dc`  |
| 1871   | Layout 1 | `e6ffbdd255dc`  |
| 1866   | Layout 1 | `e6ffbdd255dc`  |
| 1862   | Layout 1 | `e6ffbdd255dc`  |
| 1854   | Layout 1 | `e6ffbdd255dc`  |
| 1846   | Layout 1 | `e6ffbdd255dc`  |
| 1838   | Layout 1 | `e6ffbdd255dc`  |
| 1832   | Layout 1 | `e6ffbdd255dc`  |
| 1826   | Layout 1 | `e6ffbdd255dc`  |
| 1822   | Layout 1 | `e6ffbdd255dc`  |
| 1818   | Layout 1 | `e6ffbdd255dc`  |
| 1804   | Layout 1 | `e6ffbdd255dc`  |
| 1794   | Layout 1 | `e6ffbdd255dc`  |
| 1790   | Layout 1 | `e6ffbdd255dc`  |
| 1784   | Layout 1 | `e6ffbdd255dc`  |
| 1774   | Layout 1 | `e6ffbdd255dc`  |
| 1771   | Layout 1 | `e6ffbdd255dc`  |
| 1762   | Layout 1 | `e6ffbdd255dc`  |
| 1759   | Layout 1 | `e6ffbdd255dc`  |
| 1754   | Layout 1 | `e6ffbdd255dc`  |
| 1749   | Layout 1 | `e6ffbdd255dc`  |
| 1743   | Layout 1 | `e6ffbdd255dc`  |
| 1737   | Layout 1 | `e6ffbdd255dc`  |
| 1731   | Layout 1 | `e6ffbdd255dc`  |
| 1725   | Layout 1 | `e6ffbdd255dc`  |
| 1717   | Layout 1 | `e6ffbdd255dc`  |
| 1710   | Layout 1 | `e6ffbdd255dc`  |
| 1704   | Layout 1 | `e6ffbdd255dc`  |
| 1698   | Layout 1 | `e6ffbdd255dc`  |
| 1690   | Layout 1 | `e6ffbdd255dc`  |
| 1685   | Layout 1 | `e6ffbdd255dc`  |
| 1680   | Layout 1 | `e6ffbdd255dc`  |
| 1674   | Layout 1 | `e6ffbdd255dc`  |
| 1668   | Layout 1 | `e6ffbdd255dc`  |
| 1659   | Layout 1 | `e6ffbdd255dc`  |
| 1649   | Layout 1 | `e6ffbdd255dc`  |
| 1642   | Layout 1 | `e6ffbdd255dc`  |
| 1636   | Layout 1 | `e6ffbdd255dc`  |
| 1628   | Layout 1 | `e6ffbdd255dc`  |
| 1622   | Layout 1 | `e6ffbdd255dc`  |
| 1614   | Layout 1 | `e6ffbdd255dc`  |
| 1608   | Layout 1 | `e6ffbdd255dc`  |
| 1602   | Layout 1 | `e6ffbdd255dc`  |
| 1598   | Layout 1 | `e6ffbdd255dc`  |
| 1594   | Layout 1 | `e6ffbdd255dc`  |
| 1590   | Layout 1 | `e6ffbdd255dc`  |
| 1587   | Layout 1 | `e6ffbdd255dc`  |
| 1584   | Layout 1 | `e6ffbdd255dc`  |
| 1579   | Layout 1 | `e6ffbdd255dc`  |
| 1572   | Layout 1 | `e6ffbdd255dc`  |
| 1565   | Layout 1 | `e6ffbdd255dc`  |
| 1559   | Layout 1 | `e6ffbdd255dc`  |
| 1554   | Layout 1 | `e6ffbdd255dc`  |
| 1547   | Layout 1 | `e6ffbdd255dc`  |
| 1537   | Layout 1 | `e6ffbdd255dc`  |
| 1529   | Layout 1 | `e6ffbdd255dc`  |
| 1524   | Layout 1 | `e6ffbdd255dc`  |
| 1519   | Layout 1 | `e6ffbdd255dc`  |
| 1509   | Layout 1 | `e6ffbdd255dc`  |
| 1506   | Layout 1 | `e6ffbdd255dc`  |
| 1504   | Layout 1 | `e6ffbdd255dc`  |
| 1500   | Layout 1 | `e6ffbdd255dc`  |
| 1493   | Layout 1 | `e6ffbdd255dc`  |
| 1489   | Layout 1 | `e6ffbdd255dc`  |
| 1485   | Layout 1 | `e6ffbdd255dc`  |
| 1481   | Layout 1 | `e6ffbdd255dc`  |
| 1474   | Layout 1 | `e6ffbdd255dc`  |
| 1466   | Layout 1 | `e6ffbdd255dc`  |
| 1462   | Layout 1 | `e6ffbdd255dc`  |
| 1459   | Layout 1 | `e6ffbdd255dc`  |
| 1453   | Layout 1 | `e6ffbdd255dc`  |
| 1450   | Layout 1 | `e6ffbdd255dc`  |
| 1445   | Layout 1 | `e6ffbdd255dc`  |
| 1439   | Layout 1 | `e6ffbdd255dc`  |
| 1433   | Layout 1 | `e6ffbdd255dc`  |
| 1430   | No file  | `e6ffbdd255dc`  |
| 1426   | No file  | `e6ffbdd255dc`  |
| 1421   | No file  | `e6ffbdd255dc`  |
| 1417   | No file  | `e6ffbdd255dc`  |
| 1416   | No file  | `e6ffbdd255dc`  |
| 1409   | No file  | `e6ffbdd255dc`  |
| 1405   | No file  | `e6ffbdd255dc`  |
| 1401   | No file  | `e6ffbdd255dc`  |
| 1396   | No file  | `e6ffbdd255dc`  |
| 1391   | No file  | `e6ffbdd255dc`  |
| 1390   | No file  | `e6ffbdd255dc`  |
| 1386   | No file  | `e6ffbdd255dc`  |
| 1381   | No file  | `e6ffbdd255dc`  |
| 1379   | No file  | `e6ffbdd255dc`  |
| 1372   | No file  | `e6ffbdd255dc`  |
| 1366   | No file  | `e6ffbdd255dc`  |
| 1364   | No file  | `e6ffbdd255dc`  |
| 1363   | No file  | `e6ffbdd255dc`  |
| 1360   | No file  | `e6ffbdd255dc`  |
| 1358   | No file  | `e6ffbdd255dc`  |
| 1355   | No file  | `e6ffbdd255dc`  |
| 1351   | No file  | `e6ffbdd255dc`  |
| 1348   | No file  | `e6ffbdd255dc`  |
| 1346   | No file  | `e6ffbdd255dc`  |
| 1341   | No file  | `e6ffbdd255dc`  |
| 1340   | No file  | `e6ffbdd255dc`  |
| 1338   | No file  | `e6ffbdd255dc`  |
| 1335   | No file  | `e6ffbdd255dc`  |
| 1333   | No file  | `e6ffbdd255dc`  |
| 1329   | No file  | `e6ffbdd255dc`  |
| 1327   | No file  | `e6ffbdd255dc`  |
| 1324   | No file  | `e6ffbdd255dc`  |
| 1321   | No file  | `e6ffbdd255dc`  |
| 1319   | No file  | `e6ffbdd255dc`  |
| 1318   | No file  | `e6ffbdd255dc`  |
| 1316   | No file  | `e6ffbdd255dc`  |
| 1313   | No file  | `e6ffbdd255dc`  |
| 1311   | No file  | `e6ffbdd255dc`  |
| 1309   | No file  | `e6ffbdd255dc`  |
| 1304   | No file  | `e6ffbdd255dc`  |
| 1292   | No file  | `e6ffbdd255dc`  |
| 1286   | No file  | `e6ffbdd255dc`  |
| 1280   | No file  | `e6ffbdd255dc`  |
| 1276   | No file  | `e6ffbdd255dc`  |
| 1267   | No file  | `e6ffbdd255dc`  |
| 1261   | No file  | `e6ffbdd255dc`  |
| 1256   | No file  | `e6ffbdd255dc`  |
| 1250   | No file  | `e6ffbdd255dc`  |
| 1246   | No file  | `e6ffbdd255dc`  |
| 1239   | No file  | `e6ffbdd255dc`  |
| 1230   | No file  | `e6ffbdd255dc`  |
| 1226   | No file  | `e6ffbdd255dc`  |
| 1220   | No file  | `e6ffbdd255dc`  |
| 1217   | No file  | `e6ffbdd255dc`  |
| 1211   | No file  | `e6ffbdd255dc`  |
| 1210   | No file  | `e6ffbdd255dc`  |
| 1208   | No file  | `e6ffbdd255dc`  |
| 1203   | No file  | `e6ffbdd255dc`  |
| 1197   | No file  | `e6ffbdd255dc`  |
| 1194   | No file  | `e6ffbdd255dc`  |
| 1192   | No file  | `e6ffbdd255dc`  |
| 1187   | No file  | `e6ffbdd255dc`  |
| 1183   | No file  | `e6ffbdd255dc`  |
| 1177   | No file  | `e6ffbdd255dc`  |
| 1173   | No file  | `e6ffbdd255dc`  |
| 1167   | No file  | `e6ffbdd255dc`  |
| 1164   | No file  | `e6ffbdd255dc`  |
| 1156   | No file  | `e6ffbdd255dc`  |
| 1149   | No file  | `e6ffbdd255dc`  |
| 1144   | No file  | `e6ffbdd255dc`  |
| 1137   | No file  | `e6ffbdd255dc`  |
| 1132   | No file  | `e6ffbdd255dc`  |
| 1127   | No file  | `e6ffbdd255dc`  |
| 1122   | No file  | `e6ffbdd255dc`  |
| 1118   | No file  | `e6ffbdd255dc`  |
| 1114   | No file  | `e6ffbdd255dc`  |
| 1109   | No file  | `e6ffbdd255dc`  |
| 1102   | No file  | `e6ffbdd255dc`  |
| 1096   | No file  | `e6ffbdd255dc`  |
| 1088   | No file  | `e6ffbdd255dc`  |
| 1081   | No file  | `e6ffbdd255dc`  |
| 1076   | No file  | `e6ffbdd255dc`  |
| 1069   | No file  | `e6ffbdd255dc`  |
| 1064   | No file  | `e6ffbdd255dc`  |
| 1058   | No file  | `e6ffbdd255dc`  |
| 1051   | No file  | `e6ffbdd255dc`  |
| 1044   | No file  | `e6ffbdd255dc`  |
| 1036   | No file  | `e6ffbdd255dc`  |
| 1026   | No file  | `e6ffbdd255dc`  |
| 1016   | No file  | `e6ffbdd255dc`  |
| 1009   | No file  | `e6ffbdd255dc`  |
| 1005   | No file  | `e6ffbdd255dc`  |
| 1000   | No file  | `e6ffbdd255dc`  |
| 998    | No file  | `e6ffbdd255dc`  |
| 990    | No file  | `e6ffbdd255dc`  |
| 979    | No file  | `e6ffbdd255dc`  |
| 972    | No file  | `e6ffbdd255dc`  |
| 963    | No file  | `e6ffbdd255dc`  |
| 955    | No file  | `e6ffbdd255dc`  |
| 946    | No file  | `e6ffbdd255dc`  |
| 938    | No file  | `e6ffbdd255dc`  |
| 927    | No file  | `e6ffbdd255dc`  |
| 911    | No file  | `e6ffbdd255dc`  |
| 904    | No file  | `e6ffbdd255dc`  |
| 899    | No file  | `e6ffbdd255dc`  |
| 894    | No file  | `e6ffbdd255dc`  |
| 885    | No file  | `e6ffbdd255dc`  |
| 879    | No file  | `e6ffbdd255dc`  |
| 872    | No file  | `e6ffbdd255dc`  |
| 864    | No file  | `e6ffbdd255dc`  |
| 855    | No file  | `e6ffbdd255dc`  |
| 853    | No file  | `e6ffbdd255dc`  |
| 845    | No file  | `e6ffbdd255dc`  |
| 837    | No file  | `e6ffbdd255dc`  |
| 829    | No file  | `e6ffbdd255dc`  |
| 822    | No file  | `e6ffbdd255dc`  |
| 814    | No file  | `e6ffbdd255dc`  |
| 805    | No file  | `e6ffbdd255dc`  |
| 794    | No file  | `e6ffbdd255dc`  |
| 787    | No file  | `e6ffbdd255dc`  |
| 780    | No file  | `e6ffbdd255dc`  |
| 771    | No file  | `e6ffbdd255dc`  |
| 760    | No file  | `e6ffbdd255dc`  |
| 748    | No file  | `e6ffbdd255dc`  |
| 741    | No file  | `e6ffbdd255dc`  |
| 736    | No file  | `e6ffbdd255dc`  |
| 731    | No file  | `e6ffbdd255dc`  |
| 723    | No file  | `e6ffbdd255dc`  |
| 711    | No file  | `e6ffbdd255dc`  |
| 707    | No file  | `e6ffbdd255dc`  |
| 697    | No file  | `e6ffbdd255dc`  |
| 689    | No file  | `e6ffbdd255dc`  |
| 683    | No file  | `e6ffbdd255dc`  |
| 678    | No file  | `e6ffbdd255dc`  |
| 670    | No file  | `e6ffbdd255dc`  |
| 661    | No file  | `e6ffbdd255dc`  |
| 656    | No file  | `e6ffbdd255dc`  |
| 652    | No file  | `e6ffbdd255dc`  |
| 643    | No file  | `e6ffbdd255dc`  |
| 637    | No file  | `e6ffbdd255dc`  |
| 630    | No file  | `e6ffbdd255dc`  |
| 627    | No file  | `e6ffbdd255dc`  |
| 621    | No file  | `e6ffbdd255dc`  |
| 617    | No file  | `e6ffbdd255dc`  |
| 615    | No file  | `e6ffbdd255dc`  |
| 606    | No file  | `e6ffbdd255dc`  |
| 599    | No file  | `e6ffbdd255dc`  |
| 592    | No file  | `e6ffbdd255dc`  |
| 586    | No file  | `e6ffbdd255dc`  |
| 577    | No file  | `e6ffbdd255dc`  |
| 569    | No file  | `e6ffbdd255dc`  |
| 561    | No file  | `e6ffbdd255dc`  |
| 554    | No file  | `e6ffbdd255dc`  |
| 542    | No file  | `e6ffbdd255dc`  |
| 532    | No file  | `e6ffbdd255dc`  |
| 531    | No file  | `e6ffbdd255dc`  |
| 526    | No file  | `e6ffbdd255dc`  |
| 521    | No file  | `e6ffbdd255dc`  |
| 517    | No file  | `e6ffbdd255dc`  |
| 510    | No file  | `e6ffbdd255dc`  |
| 508    | No file  | `e6ffbdd255dc`  |
| 504    | No file  | `e6ffbdd255dc`  |
| 497    | No file  | `e6ffbdd255dc`  |
| 491    | No file  | `e6ffbdd255dc`  |
| 485    | No file  | `e6ffbdd255dc`  |
| 478    | No file  | `e6ffbdd255dc`  |
| 472    | No file  | `e6ffbdd255dc`  |
| 466    | No file  | `e6ffbdd255dc`  |
| 457    | No file  | `e6ffbdd255dc`  |
| 452    | No file  | `e6ffbdd255dc`  |
| 449    | No file  | `e6ffbdd255dc`  |
| 435    | No file  | `e6ffbdd255dc`  |

<!-- versions:end -->

## Companion Files

None. The handler names each character with LOC type 6 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of pairs                               |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (14 bytes)

| Offset  | Type | Field                  | Notes                                                       |
| ------- | ---- | ---------------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | male_character_key     | Male horse character; LOC type 6 names it                   |
| `+0x02` | u16  | female_character_key   | Female horse character                                      |
| `+0x04` | u32  | result_character_count | Number of Mythical horses the exchange makes; `1` on every row (clients 1784 and 3482) |
| `+0x08` | u16  | upgrade_character_key  | Mythical horse character the exchange makes                 |
| `+0x0A` | u32  | upgrade_rate           | Rate of `upgrade_character_key`, per million; `1000000` on every row (clients 1784 and 3482) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Pairs

Client 1784 has one row, `9989` Arduanatt with `9889` Arduanatt to
`31539` Mythical Arduanatt. On client 3482 the 17 rows pair every male
with every female character of one breed:

| Breed     | Male characters         | Female characters       | `upgrade_character_key`   |
| --------- | ----------------------- | ----------------------- | ------------------------- |
| Arduanatt | `9989`, `31583`, `31632` | `9889`, `31580`, `31631` | `31539` Mythical Arduanatt |
| Diné      | `9988`, `31582`          | `9888`, `31579`          | `31557` Mythical Diné      |
| Doom      | `9987`, `31581`          | `9887`, `31578`          | `31575` Mythical Doom      |

That is 9 Arduanatt rows and 4 rows each for Diné and Doom. The exchange
window draws the left horse's portrait for the same male keys (`9989`,
`31583` and `31632` the Arduanatt image).

## Field Names

The names follow the `ServantFantasy_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_servantdatatable.xlsm`: columns `MaleCharacterKey`,
`FemaleCharacterKey`, `ResultCharacterCount`, `UpgradeCharacterKey` and
`UpgradeRate`, one row (`9989`, `9889`, `1`, `31539`, `1000000`). It
matches the client 1784 file's row value for value (1 of 1). The xlsm
notes `ResultCharacterCount` as "환상마 업그레이드 성공 시 나올 환상마
캐릭터키 개수 설정" (how many Mythical horse character keys a successful
upgrade gives), `UpgradeCharacterKey` as "업그레이드 시 캐릭터키 종류" (the
character key of the upgrade) and `UpgradeRate` as "업그레이드 시 나올
캐릭터키 확률" (the chance of that character key). Its two `#` columns hold
the Korean names (`아두아나트`) and are not compiled.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/servant_tables.py`: each
  character key next to its LOC name, the rate as a percentage.
- The exchange's success rate is not in this file: the window reads
  `ToClient_getFantasyMixMaxRate()`, `ToClient_getFantasyMixStackCount()`
  and `ToClient_getFantasyMixNeedItem()`.
