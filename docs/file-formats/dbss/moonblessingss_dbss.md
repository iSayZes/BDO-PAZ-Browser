# `moonblessingss.dbss` Format

## Purpose

The Moon's Blessing events of the Pearl Shop: per event its period, the
Pearl total of its top level, a Korean description and its levels. Each
level has a Korean title (`800펄 사용`, "use 800 Pearls"), its item rewards
as quest reward entries and the Pearls spent that unlock it.
`panel_ingamecashshop_moonblessing_renew_all_1.luac` shows the levels
through `ToClient_GetMoonBlessingRewardAt()` (`getTitle()`,
`getBaseRewardCount()`, `getBaseRewardAt(i)`, `getTargetUsedPearl()`) and
the event text through `ToClient_GetMoonBlessingDesc()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records                            | Row bytes |
| ------ | -------------- | --------------------- | ------ | ---------------------------------- | --------- |
| 1      | 2923 and later | `moonblessingss.dbss` | 46,627 | 221 Reward Entry, 92 Level, 11 Row | 178       |

| Layout | File                  | Known            | Unknown          |
| ------ | --------------------- | ---------------- | ---------------- |
| 1      | `moonblessingss.dbss` | 33,334 B (71.5%) | 13,293 B (28.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `6d99a469eb86`  |
| 3482   | Layout 1             | `6d99a469eb86`  |
| 3474   | Layout 1             | `6d99a469eb86`  |
| 3473   | Layout 1             | `6d99a469eb86`  |
| 3464   | Layout 1             | `6d99a469eb86`  |
| 3458   | Layout 1             | `6d99a469eb86`  |
| 3454   | Layout 1             | `6d99a469eb86`  |
| 3444   | Layout 1             | `6d99a469eb86`  |
| 3435   | Layout 1             | `6d99a469eb86`  |
| 3426   | Layout 1             | `6d99a469eb86`  |
| 3418   | Layout 1             | `6d99a469eb86`  |
| 3412   | Layout 1             | `6d99a469eb86`  |
| 3402   | Layout 1             | `6d99a469eb86`  |
| 3396   | Layout 1             | `6d99a469eb86`  |
| 3387   | Layout 1             | `6d99a469eb86`  |
| 3381   | Layout 1             | `6d99a469eb86`  |
| 3373   | Layout 1             | `6d99a469eb86`  |
| 3364   | Layout 1             | `6d99a469eb86`  |
| 3356   | Layout 1             | `6d99a469eb86`  |
| 3349   | Layout 1             | `6d99a469eb86`  |
| 3342   | Layout 1             | `6d99a469eb86`  |
| 3335   | Layout 1             | `6d99a469eb86`  |
| 3326   | Layout 1             | `6d99a469eb86`  |
| 3321   | Layout 1             | `6d99a469eb86`  |
| 3314   | Layout 1             | `6d99a469eb86`  |
| 3303   | Layout 1             | `6d99a469eb86`  |
| 3302   | Layout 1             | `6d99a469eb86`  |
| 3293   | Layout 1             | `6d99a469eb86`  |
| 3283   | Layout 1             | `6d99a469eb86`  |
| 3275   | Layout 1             | `6d99a469eb86`  |
| 3267   | Layout 1             | `6d99a469eb86`  |
| 3258   | Layout 1             | `6d99a469eb86`  |
| 3251   | Layout 1             | `6d99a469eb86`  |
| 3242   | Layout 1             | `6d99a469eb86`  |
| 3235   | Layout 1             | `6d99a469eb86`  |
| 3229   | Layout 1             | `6d99a469eb86`  |
| 3212   | Layout 1             | `6d99a469eb86`  |
| 3203   | Layout 1             | `6d99a469eb86`  |
| 3193   | Layout 1             | `6d99a469eb86`  |
| 3186   | Layout 1             | `6d99a469eb86`  |
| 3177   | Layout 1             | `6d99a469eb86`  |
| 3169   | Layout 1             | `6d99a469eb86`  |
| 3158   | Layout 1             | `6d99a469eb86`  |
| 3151   | Layout 1             | `6d99a469eb86`  |
| 3144   | Layout 1             | `6d99a469eb86`  |
| 3133   | Layout 1             | `6d99a469eb86`  |
| 3125   | Layout 1             | `6d99a469eb86`  |
| 3118   | Layout 1             | `6d99a469eb86`  |
| 3111   | Layout 1             | `6d99a469eb86`  |
| 3103   | Layout 1             | `6d99a469eb86`  |
| 3095   | Layout 1             | `6d99a469eb86`  |
| 3086   | Layout 1             | `6d99a469eb86`  |
| 3072   | Layout 1             | `6d99a469eb86`  |
| 3062   | Layout 1             | `6d99a469eb86`  |
| 3052   | Layout 1             | `6d99a469eb86`  |
| 3045   | Layout 1             | `6d99a469eb86`  |
| 3037   | Layout 1             | `6d99a469eb86`  |
| 3030   | Layout 1             | `6d99a469eb86`  |
| 3021   | Layout 1             | `6d99a469eb86`  |
| 3012   | Layout 1             | `6d99a469eb86`  |
| 3002   | Layout 1             | `6d99a469eb86`  |
| 2995   | Layout 1             | `6d99a469eb86`  |
| 2987   | Layout 1             | `6d99a469eb86`  |
| 2978   | Layout 1             | `6d99a469eb86`  |
| 2970   | Layout 1             | `6d99a469eb86`  |
| 2959   | Layout 1             | `6d99a469eb86`  |
| 2951   | Layout 1             | `6d99a469eb86`  |
| 2942   | Layout 1             | `6d99a469eb86`  |
| 2935   | Layout 1             | `6d99a469eb86`  |
| 2932   | Layout 1             | `6d99a469eb86`  |
| 2923   | Layout 1             | `6d99a469eb86`  |
| 2919   | No documented layout | `6d99a469eb86`  |
| 2907   | No documented layout | `6d99a469eb86`  |
| 2900   | No documented layout | `6d99a469eb86`  |
| 2891   | No documented layout | `6d99a469eb86`  |
| 2882   | No documented layout | `6d99a469eb86`  |
| 2872   | No documented layout | `6d99a469eb86`  |
| 2863   | No documented layout | `6d99a469eb86`  |
| 2855   | No documented layout | `6d99a469eb86`  |
| 2849   | No documented layout | `6d99a469eb86`  |
| 2844   | No documented layout | `6d99a469eb86`  |
| 2834   | No documented layout | `6d99a469eb86`  |
| 2825   | No documented layout | `6d99a469eb86`  |
| 2819   | No documented layout | `6d99a469eb86`  |
| 2811   | No file              | `6d99a469eb86`  |
| 2803   | No file              | `6d99a469eb86`  |
| 2794   | No file              | `6d99a469eb86`  |
| 2783   | No file              | `6d99a469eb86`  |
| 2774   | No file              | `6d99a469eb86`  |
| 2765   | No file              | `6d99a469eb86`  |
| 2756   | No file              | `6d99a469eb86`  |
| 2750   | No file              | `6d99a469eb86`  |
| 2743   | No file              | `6d99a469eb86`  |
| 2736   | No file              | `6d99a469eb86`  |
| 2726   | No file              | `6d99a469eb86`  |
| 2717   | No file              | `6d99a469eb86`  |
| 2709   | No file              | `6d99a469eb86`  |
| 2703   | No file              | `6d99a469eb86`  |
| 2695   | No file              | `6d99a469eb86`  |
| 2684   | No file              | `6d99a469eb86`  |
| 2672   | No file              | `6d99a469eb86`  |
| 2665   | No file              | `6d99a469eb86`  |
| 2657   | No file              | `6d99a469eb86`  |
| 2649   | No file              | `6d99a469eb86`  |
| 2644   | No file              | `6d99a469eb86`  |
| 2637   | No file              | `6d99a469eb86`  |
| 2629   | No file              | `6d99a469eb86`  |
| 2619   | No file              | `6d99a469eb86`  |
| 2612   | No file              | `6d99a469eb86`  |
| 2606   | No file              | `6d99a469eb86`  |
| 2602   | No file              | `6d99a469eb86`  |
| 2601   | No file              | `6d99a469eb86`  |
| 2592   | No file              | `6d99a469eb86`  |
| 2583   | No file              | `6d99a469eb86`  |
| 2575   | No file              | `6d99a469eb86`  |
| 2567   | No file              | `6d99a469eb86`  |
| 2560   | No file              | `6d99a469eb86`  |
| 2553   | No file              | `6d99a469eb86`  |
| 2545   | No file              | `6d99a469eb86`  |
| 2538   | No file              | `6d99a469eb86`  |
| 2529   | No file              | `6d99a469eb86`  |
| 2519   | No file              | `6d99a469eb86`  |
| 2513   | No file              | `6d99a469eb86`  |
| 2510   | No file              | `6d99a469eb86`  |
| 2507   | No file              | `6d99a469eb86`  |
| 2503   | No file              | `6d99a469eb86`  |
| 2498   | No file              | `6d99a469eb86`  |
| 2492   | No file              | `6d99a469eb86`  |
| 2487   | No file              | `6d99a469eb86`  |
| 2480   | No file              | `6d99a469eb86`  |
| 2474   | No file              | `6d99a469eb86`  |
| 2468   | No file              | `6d99a469eb86`  |
| 2460   | No file              | `6d99a469eb86`  |
| 2453   | No file              | `6d99a469eb86`  |
| 2444   | No file              | `6d99a469eb86`  |
| 2438   | No file              | `6d99a469eb86`  |
| 2434   | No file              | `6d99a469eb86`  |
| 2429   | No file              | `6d99a469eb86`  |
| 2421   | No file              | `6d99a469eb86`  |
| 2414   | No file              | `6d99a469eb86`  |
| 2407   | No file              | `6d99a469eb86`  |
| 2401   | No file              | `6d99a469eb86`  |
| 2397   | No file              | `6d99a469eb86`  |
| 2393   | No file              | `6d99a469eb86`  |
| 2384   | No file              | `6d99a469eb86`  |
| 2378   | No file              | `6d99a469eb86`  |
| 2372   | No file              | `6d99a469eb86`  |
| 2358   | No file              | `6d99a469eb86`  |
| 2352   | No file              | `6d99a469eb86`  |
| 2347   | No file              | `6d99a469eb86`  |
| 2343   | No file              | `6d99a469eb86`  |
| 2335   | No file              | `6d99a469eb86`  |
| 2327   | No file              | `6d99a469eb86`  |
| 2324   | No file              | `6d99a469eb86`  |
| 2319   | No file              | `6d99a469eb86`  |
| 2313   | No file              | `6d99a469eb86`  |
| 2308   | No file              | `6d99a469eb86`  |
| 2302   | No file              | `6d99a469eb86`  |
| 2295   | No file              | `6d99a469eb86`  |
| 2290   | No file              | `6d99a469eb86`  |
| 2284   | No file              | `6d99a469eb86`  |
| 2276   | No file              | `6d99a469eb86`  |
| 2269   | No file              | `6d99a469eb86`  |
| 2259   | No file              | `6d99a469eb86`  |
| 2250   | No file              | `6d99a469eb86`  |
| 2243   | No file              | `6d99a469eb86`  |
| 2235   | No file              | `6d99a469eb86`  |
| 2229   | No file              | `6d99a469eb86`  |
| 2224   | No file              | `6d99a469eb86`  |
| 2218   | No file              | `6d99a469eb86`  |
| 2215   | No file              | `6d99a469eb86`  |
| 2207   | No file              | `6d99a469eb86`  |
| 2203   | No file              | `6d99a469eb86`  |
| 2196   | No file              | `6d99a469eb86`  |
| 2192   | No file              | `6d99a469eb86`  |
| 2189   | No file              | `6d99a469eb86`  |
| 2183   | No file              | `6d99a469eb86`  |
| 2179   | No file              | `6d99a469eb86`  |
| 2171   | No file              | `6d99a469eb86`  |
| 2163   | No file              | `6d99a469eb86`  |
| 2156   | No file              | `6d99a469eb86`  |
| 2151   | No file              | `6d99a469eb86`  |
| 2147   | No file              | `6d99a469eb86`  |
| 2142   | No file              | `6d99a469eb86`  |
| 2138   | No file              | `6d99a469eb86`  |
| 2134   | No file              | `6d99a469eb86`  |
| 2130   | No file              | `6d99a469eb86`  |
| 2122   | No file              | `6d99a469eb86`  |
| 2107   | No file              | `6d99a469eb86`  |
| 2098   | No file              | `6d99a469eb86`  |
| 2089   | No file              | `6d99a469eb86`  |
| 2081   | No file              | `6d99a469eb86`  |
| 2073   | No file              | `6d99a469eb86`  |
| 2067   | No file              | `6d99a469eb86`  |
| 2063   | No file              | `6d99a469eb86`  |
| 2059   | No file              | `6d99a469eb86`  |
| 2052   | No file              | `6d99a469eb86`  |
| 2044   | No file              | `6d99a469eb86`  |
| 2039   | No file              | `6d99a469eb86`  |
| 2032   | No file              | `6d99a469eb86`  |
| 2025   | No file              | `6d99a469eb86`  |
| 2011   | No file              | `6d99a469eb86`  |
| 2005   | No file              | `6d99a469eb86`  |
| 2000   | No file              | `6d99a469eb86`  |
| 1996   | No file              | `6d99a469eb86`  |
| 1991   | No file              | `6d99a469eb86`  |
| 1985   | No file              | `6d99a469eb86`  |
| 1980   | No file              | `6d99a469eb86`  |
| 1969   | No file              | `6d99a469eb86`  |
| 1964   | No file              | `6d99a469eb86`  |
| 1958   | No file              | `6d99a469eb86`  |
| 1950   | No file              | `6d99a469eb86`  |
| 1945   | No file              | `6d99a469eb86`  |
| 1937   | No file              | `6d99a469eb86`  |
| 1933   | No file              | `6d99a469eb86`  |
| 1927   | No file              | `6d99a469eb86`  |
| 1921   | No file              | `6d99a469eb86`  |
| 1914   | No file              | `6d99a469eb86`  |
| 1908   | No file              | `6d99a469eb86`  |
| 1897   | No file              | `6d99a469eb86`  |
| 1892   | No file              | `6d99a469eb86`  |
| 1886   | No file              | `6d99a469eb86`  |
| 1881   | No file              | `6d99a469eb86`  |
| 1871   | No file              | `6d99a469eb86`  |
| 1866   | No file              | `6d99a469eb86`  |
| 1862   | No file              | `6d99a469eb86`  |
| 1854   | No file              | `6d99a469eb86`  |
| 1846   | No file              | `6d99a469eb86`  |
| 1838   | No file              | `6d99a469eb86`  |
| 1832   | No file              | `6d99a469eb86`  |
| 1826   | No file              | `6d99a469eb86`  |
| 1822   | No file              | `6d99a469eb86`  |
| 1818   | No file              | `6d99a469eb86`  |
| 1804   | No file              | `6d99a469eb86`  |
| 1794   | No file              | `6d99a469eb86`  |
| 1790   | No file              | `6d99a469eb86`  |
| 1784   | No file              | `6d99a469eb86`  |
| 1774   | No file              | `6d99a469eb86`  |
| 1771   | No file              | `6d99a469eb86`  |
| 1762   | No file              | `6d99a469eb86`  |
| 1759   | No file              | `6d99a469eb86`  |
| 1754   | No file              | `6d99a469eb86`  |
| 1749   | No file              | `6d99a469eb86`  |
| 1743   | No file              | `6d99a469eb86`  |
| 1737   | No file              | `6d99a469eb86`  |
| 1731   | No file              | `6d99a469eb86`  |
| 1725   | No file              | `6d99a469eb86`  |
| 1717   | No file              | `6d99a469eb86`  |
| 1710   | No file              | `6d99a469eb86`  |
| 1704   | No file              | `6d99a469eb86`  |
| 1698   | No file              | `6d99a469eb86`  |
| 1690   | No file              | `6d99a469eb86`  |
| 1685   | No file              | `6d99a469eb86`  |
| 1680   | No file              | `6d99a469eb86`  |
| 1674   | No file              | `6d99a469eb86`  |
| 1668   | No file              | `6d99a469eb86`  |
| 1659   | No file              | `6d99a469eb86`  |
| 1649   | No file              | `6d99a469eb86`  |
| 1642   | No file              | `6d99a469eb86`  |
| 1636   | No file              | `6d99a469eb86`  |
| 1628   | No file              | `6d99a469eb86`  |
| 1622   | No file              | `6d99a469eb86`  |
| 1614   | No file              | `6d99a469eb86`  |
| 1608   | No file              | `6d99a469eb86`  |
| 1602   | No file              | `6d99a469eb86`  |
| 1598   | No file              | `6d99a469eb86`  |
| 1594   | No file              | `6d99a469eb86`  |
| 1590   | No file              | `6d99a469eb86`  |
| 1587   | No file              | `6d99a469eb86`  |
| 1584   | No file              | `6d99a469eb86`  |
| 1579   | No file              | `6d99a469eb86`  |
| 1572   | No file              | `6d99a469eb86`  |
| 1565   | No file              | `6d99a469eb86`  |
| 1559   | No file              | `6d99a469eb86`  |
| 1554   | No file              | `6d99a469eb86`  |
| 1547   | No file              | `6d99a469eb86`  |
| 1537   | No file              | `6d99a469eb86`  |
| 1529   | No file              | `6d99a469eb86`  |
| 1524   | No file              | `6d99a469eb86`  |
| 1519   | No file              | `6d99a469eb86`  |
| 1509   | No file              | `6d99a469eb86`  |
| 1506   | No file              | `6d99a469eb86`  |
| 1504   | No file              | `6d99a469eb86`  |
| 1500   | No file              | `6d99a469eb86`  |
| 1493   | No file              | `6d99a469eb86`  |
| 1489   | No file              | `6d99a469eb86`  |
| 1485   | No file              | `6d99a469eb86`  |
| 1481   | No file              | `6d99a469eb86`  |
| 1474   | No file              | `6d99a469eb86`  |
| 1466   | No file              | `6d99a469eb86`  |
| 1462   | No file              | `6d99a469eb86`  |
| 1459   | No file              | `6d99a469eb86`  |
| 1453   | No file              | `6d99a469eb86`  |
| 1450   | No file              | `6d99a469eb86`  |
| 1445   | No file              | `6d99a469eb86`  |
| 1439   | No file              | `6d99a469eb86`  |
| 1433   | No file              | `6d99a469eb86`  |
| 1430   | No file              | `6d99a469eb86`  |
| 1426   | No file              | `6d99a469eb86`  |
| 1421   | No file              | `6d99a469eb86`  |
| 1417   | No file              | `6d99a469eb86`  |
| 1416   | No file              | `6d99a469eb86`  |
| 1409   | No file              | `6d99a469eb86`  |
| 1405   | No file              | `6d99a469eb86`  |
| 1401   | No file              | `6d99a469eb86`  |
| 1396   | No file              | `6d99a469eb86`  |
| 1391   | No file              | `6d99a469eb86`  |
| 1390   | No file              | `6d99a469eb86`  |
| 1386   | No file              | `6d99a469eb86`  |
| 1381   | No file              | `6d99a469eb86`  |
| 1379   | No file              | `6d99a469eb86`  |
| 1372   | No file              | `6d99a469eb86`  |
| 1366   | No file              | `6d99a469eb86`  |
| 1364   | No file              | `6d99a469eb86`  |
| 1363   | No file              | `6d99a469eb86`  |
| 1360   | No file              | `6d99a469eb86`  |
| 1358   | No file              | `6d99a469eb86`  |
| 1355   | No file              | `6d99a469eb86`  |
| 1351   | No file              | `6d99a469eb86`  |
| 1348   | No file              | `6d99a469eb86`  |
| 1346   | No file              | `6d99a469eb86`  |
| 1341   | No file              | `6d99a469eb86`  |
| 1340   | No file              | `6d99a469eb86`  |
| 1338   | No file              | `6d99a469eb86`  |
| 1335   | No file              | `6d99a469eb86`  |
| 1333   | No file              | `6d99a469eb86`  |
| 1329   | No file              | `6d99a469eb86`  |
| 1327   | No file              | `6d99a469eb86`  |
| 1324   | No file              | `6d99a469eb86`  |
| 1321   | No file              | `6d99a469eb86`  |
| 1319   | No file              | `6d99a469eb86`  |
| 1318   | No file              | `6d99a469eb86`  |
| 1316   | No file              | `6d99a469eb86`  |
| 1313   | No file              | `6d99a469eb86`  |
| 1311   | No file              | `6d99a469eb86`  |
| 1309   | No file              | `6d99a469eb86`  |
| 1304   | No file              | `6d99a469eb86`  |
| 1292   | No file              | `6d99a469eb86`  |
| 1286   | No file              | `6d99a469eb86`  |
| 1280   | No file              | `6d99a469eb86`  |
| 1276   | No file              | `6d99a469eb86`  |
| 1267   | No file              | `6d99a469eb86`  |
| 1261   | No file              | `6d99a469eb86`  |
| 1256   | No file              | `6d99a469eb86`  |
| 1250   | No file              | `6d99a469eb86`  |
| 1246   | No file              | `6d99a469eb86`  |
| 1239   | No file              | `6d99a469eb86`  |
| 1230   | No file              | `6d99a469eb86`  |
| 1226   | No file              | `6d99a469eb86`  |
| 1220   | No file              | `6d99a469eb86`  |
| 1217   | No file              | `6d99a469eb86`  |
| 1211   | No file              | `6d99a469eb86`  |
| 1210   | No file              | `6d99a469eb86`  |
| 1208   | No file              | `6d99a469eb86`  |
| 1203   | No file              | `6d99a469eb86`  |
| 1197   | No file              | `6d99a469eb86`  |
| 1194   | No file              | `6d99a469eb86`  |
| 1192   | No file              | `6d99a469eb86`  |
| 1187   | No file              | `6d99a469eb86`  |
| 1183   | No file              | `6d99a469eb86`  |
| 1177   | No file              | `6d99a469eb86`  |
| 1173   | No file              | `6d99a469eb86`  |
| 1167   | No file              | `6d99a469eb86`  |
| 1164   | No file              | `6d99a469eb86`  |
| 1156   | No file              | `6d99a469eb86`  |
| 1149   | No file              | `6d99a469eb86`  |
| 1144   | No file              | `6d99a469eb86`  |
| 1137   | No file              | `6d99a469eb86`  |
| 1132   | No file              | `6d99a469eb86`  |
| 1127   | No file              | `6d99a469eb86`  |
| 1122   | No file              | `6d99a469eb86`  |
| 1118   | No file              | `6d99a469eb86`  |
| 1114   | No file              | `6d99a469eb86`  |
| 1109   | No file              | `6d99a469eb86`  |
| 1102   | No file              | `6d99a469eb86`  |
| 1096   | No file              | `6d99a469eb86`  |
| 1088   | No file              | `6d99a469eb86`  |
| 1081   | No file              | `6d99a469eb86`  |
| 1076   | No file              | `6d99a469eb86`  |
| 1069   | No file              | `6d99a469eb86`  |
| 1064   | No file              | `6d99a469eb86`  |
| 1058   | No file              | `6d99a469eb86`  |
| 1051   | No file              | `6d99a469eb86`  |
| 1044   | No file              | `6d99a469eb86`  |
| 1036   | No file              | `6d99a469eb86`  |
| 1026   | No file              | `6d99a469eb86`  |
| 1016   | No file              | `6d99a469eb86`  |
| 1009   | No file              | `6d99a469eb86`  |
| 1005   | No file              | `6d99a469eb86`  |
| 1000   | No file              | `6d99a469eb86`  |
| 998    | No file              | `6d99a469eb86`  |
| 990    | No file              | `6d99a469eb86`  |
| 979    | No file              | `6d99a469eb86`  |
| 972    | No file              | `6d99a469eb86`  |
| 963    | No file              | `6d99a469eb86`  |
| 955    | No file              | `6d99a469eb86`  |
| 946    | No file              | `6d99a469eb86`  |
| 938    | No file              | `6d99a469eb86`  |
| 927    | No file              | `6d99a469eb86`  |
| 911    | No file              | `6d99a469eb86`  |
| 904    | No file              | `6d99a469eb86`  |
| 899    | No file              | `6d99a469eb86`  |
| 894    | No file              | `6d99a469eb86`  |
| 885    | No file              | `6d99a469eb86`  |
| 879    | No file              | `6d99a469eb86`  |
| 872    | No file              | `6d99a469eb86`  |
| 864    | No file              | `6d99a469eb86`  |
| 855    | No file              | `6d99a469eb86`  |
| 853    | No file              | `6d99a469eb86`  |
| 845    | No file              | `6d99a469eb86`  |
| 837    | No file              | `6d99a469eb86`  |
| 829    | No file              | `6d99a469eb86`  |
| 822    | No file              | `6d99a469eb86`  |
| 814    | No file              | `6d99a469eb86`  |
| 805    | No file              | `6d99a469eb86`  |
| 794    | No file              | `6d99a469eb86`  |
| 787    | No file              | `6d99a469eb86`  |
| 780    | No file              | `6d99a469eb86`  |
| 771    | No file              | `6d99a469eb86`  |
| 760    | No file              | `6d99a469eb86`  |
| 748    | No file              | `6d99a469eb86`  |
| 741    | No file              | `6d99a469eb86`  |
| 736    | No file              | `6d99a469eb86`  |
| 731    | No file              | `6d99a469eb86`  |
| 723    | No file              | `6d99a469eb86`  |
| 711    | No file              | `6d99a469eb86`  |
| 707    | No file              | `6d99a469eb86`  |
| 697    | No file              | `6d99a469eb86`  |
| 689    | No file              | `6d99a469eb86`  |
| 683    | No file              | `6d99a469eb86`  |
| 678    | No file              | `6d99a469eb86`  |
| 670    | No file              | `6d99a469eb86`  |
| 661    | No file              | `6d99a469eb86`  |
| 656    | No file              | `6d99a469eb86`  |
| 652    | No file              | `6d99a469eb86`  |
| 643    | No file              | `6d99a469eb86`  |
| 637    | No file              | `6d99a469eb86`  |
| 630    | No file              | `6d99a469eb86`  |
| 627    | No file              | `6d99a469eb86`  |
| 621    | No file              | `6d99a469eb86`  |
| 617    | No file              | `6d99a469eb86`  |
| 615    | No file              | `6d99a469eb86`  |
| 606    | No file              | `6d99a469eb86`  |
| 599    | No file              | `6d99a469eb86`  |
| 592    | No file              | `6d99a469eb86`  |
| 586    | No file              | `6d99a469eb86`  |
| 577    | No file              | `6d99a469eb86`  |
| 569    | No file              | `6d99a469eb86`  |
| 561    | No file              | `6d99a469eb86`  |
| 554    | No file              | `6d99a469eb86`  |
| 542    | No file              | `6d99a469eb86`  |
| 532    | No file              | `6d99a469eb86`  |
| 531    | No file              | `6d99a469eb86`  |
| 526    | No file              | `6d99a469eb86`  |
| 521    | No file              | `6d99a469eb86`  |
| 517    | No file              | `6d99a469eb86`  |
| 510    | No file              | `6d99a469eb86`  |
| 508    | No file              | `6d99a469eb86`  |
| 504    | No file              | `6d99a469eb86`  |
| 497    | No file              | `6d99a469eb86`  |
| 491    | No file              | `6d99a469eb86`  |
| 485    | No file              | `6d99a469eb86`  |
| 478    | No file              | `6d99a469eb86`  |
| 472    | No file              | `6d99a469eb86`  |
| 466    | No file              | `6d99a469eb86`  |
| 457    | No file              | `6d99a469eb86`  |
| 452    | No file              | `6d99a469eb86`  |
| 449    | No file              | `6d99a469eb86`  |
| 435    | No file              | `6d99a469eb86`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Item names (LOC type 0)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 41 bytes + description and levels)

| Offset                | Type               | Field                     | Notes                                                                                |
| --------------------- | ------------------ | ------------------------- | ------------------------------------------------------------------------------------ |
| `+0x00`               | u16                | key                       | Row key; `1` to `14` on client 3482, `7` to `9` missing                               |
| `+0x02`               | u64                | start_time                | Unix seconds (UTC); the start date the description names on 10 of 11 rows (client 3482) |
| `+0x0A`               | u64                | end_time                  | Unix seconds (UTC), after `start_time` on every row                                   |
| `+0x12`               | u64                | max_used_pearl            | Equals the last level's `target_used_pearl` on all 11 rows (client 3482); see Field Names |
| `+0x1A`               | u16                | unknown_1a                | `2` on the rows with 7 levels, `4` on those with 8 or 9 (client 3482); see Open Questions |
| `+0x1C`               | str16              | description_kr            | Korean period and rules text with `<PAColor>` tags; `ToClient_GetMoonBlessingDesc()`   |
| `description_kr+0x00` | u8                 | unknown_description_kr_00 | `1` on every row (clients 3002 to 3482)                                               |
| `description_kr+0x01` | u32                | level_count               | Number of `levels`; 7 to 9                                                            |
| `description_kr+0x05` | Level[level_count] | levels                    | See Level                                                                            |

### Level (variable: 22 bytes + title and rewards)

| Offset              | Type                       | Field             | Notes                                                                 |
| ------------------- | -------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`             | str16                      | title_kr          | Korean level title, `<n>펄 사용`; `getTitle()`                         |
| `title_kr+0x00`     | u32                        | reward_count      | Number of `base_rewards`; `getBaseRewardCount()`                       |
| `title_kr+0x04`     | Reward Entry[reward_count] | base_rewards      | See Reward Entry; `getBaseRewardAt(i)`                                 |
| `base_rewards+0x00` | u16                        | level_no          | The level's 1-based position in the row, on every level (client 3482) |
| `base_rewards+0x02` | u64                        | target_used_pearl | Pearls spent that unlock the level, rising level by level; `getTargetUsedPearl()` |

### Reward Entry (178 bytes)

The 178-byte entry of the [`quest.dbss` Reward Entry](quest_dbss.md#reward-entry-178-bytes),
read by `_common/quest/reward_entry.py`. On client 3482 all 221 entries
are items (type `3`) and hold the values of the guild mission entries of
[`guildquest.dbss`](guildquest_dbss.md#reward-entry-178-bytes) outside the
item fields.

| Offset  | Type      | Field                | Notes |
| ------- | --------- | -------------------- | ----- |
| `+0x00` | u32       | reward_type          | `gc::RewardType`; `3` (item) on every entry of client 3482 |
| `+0x04` | i64       | experience           | `0` on every entry |
| `+0x0C` | i32       | skill_experience     | `0` on every entry |
| `+0x10` | i32       | product_experience   | `0` on every entry |
| `+0x14` | u8        | life_experience_type | `15` on every entry |
| `+0x15` | i32       | life_experience      | `0` on every entry |
| `+0x19` | u32       | item_key             | Reward item, packed as `enchant_level << 24 \| item_id`; `getItemEnchantKey()` |
| `+0x1D` | i64       | item_count           | Amount of `item_key` |
| `+0x25` | u16       | intimacy_character   | NPC of an Amity reward; `getIntimacyCharacter()`; `0` on every entry |
| `+0x27` | i32       | intimacy_value       | `0` on every entry |
| `+0x2B` | i32       | mental_card_key      | `0` on every entry |
| `+0x2F` | bytes[2]  | unknown_2f           | Zero on every entry |
| `+0x31` | u8        | exp_grade            | `0` on every entry |
| `+0x32` | bytes[4]  | unknown_32           | Zero on every entry |
| `+0x36` | bytes[49] | unknown_36           | u32 `16`, then 45 zero bytes, on every entry |
| `+0x67` | bytes[53] | family_stat          | The `quest.dbss` [Family Stat Union](quest_dbss.md#family-stat-union-53-bytes); `family_stat_type` `16` (no stat) on every entry |
| `+0x9C` | bytes[4]  | unknown_9c           | Zero on every entry |
| `+0xA0` | u32       | max_fever_point      | `0` on every entry |
| `+0xA4` | u32       | add_fever_point      | `0` on every entry |
| `+0xA8` | u8        | unknown_a8           | `0` on every entry |
| `+0xA9` | u8        | season_no            | `0` on every entry |
| `+0xAA` | i64       | explore_exp          | `0` on every entry; ends the entry |

## Field Names

The Moon's Blessing is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it. The level and reward names are the getters of
`panel_ingamecashshop_moonblessing_renew_all_1.luac` (client 3482).
`max_used_pearl` follows `ToClient_GetCurrentMoonblessingMaxUsedPearl()`,
which the same Lua multiplies by the reset count for the progress bar; the
field equals the top level's target on all 11 rows. `start_time` and
`end_time` are named by their values: Unix seconds at 09:00 or 10:00 UTC
on maintenance days, and on 10 of 11 rows `start_time` is the start date of
the description (`기간 : 2025년 3월 13일 정기 점검 후 ~ ...`). Row 1 runs
from 2025-02-20 to 2025-02-23 while its text names 27 February to
20 March 2025.

## Notes

- Client 3002 has 4 rows, 3251 has 7, 3474 and 3482 have 11; clients 2765
  and older do not ship the file. The layout is the same on all of them.
- The handler (`_dbss/moonblessingss/`) shows one row per level, in file
  order, with its event's key, period, top target and description and the
  level's rewards as item icons with counts.

## Open Questions

### What `unknown_1a` and `unknown_description_kr_00` Hold

`unknown_1a` is `2` on the three 2025 rows with 7 levels and `4` on the
eight rows with 8 or 9; the Lua reads a reset count and its maximum
(`ToClient_GetCurrentMoonblessingResetCount()`,
`ToClient_GetCurrentMoonblessingMaxResetCount()`), and the maximum fits,
but the descriptions do not state a number to check it against.
`unknown_description_kr_00` is `1` on every row of every client checked.
