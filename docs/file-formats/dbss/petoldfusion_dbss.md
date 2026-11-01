# `petoldfusion.dbss` Format

## Purpose

The result tiers of the old pet exchange, one row per fusion key (variant,
species and tier of the main pet, the four bytes `pet.dbss` stores at
payload `+0x02`): up to four result tiers, each with a chance. It is the
per-species table that [`petfusionnew.dbss`](petfusionnew_dbss.md) (one
row per tier) stands next to. Companion `petoldfusionoffset.dbss` lists
where every row sits. Tiers are stored from 0, as `tier` of
[`pet.dbss`](pet_dbss.md) stores them: `0` is Tier 1. Rates are on the
1,000,000 = 100% scale.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------------------------- | ------ | -------------- | --------- |
| 1      | 1346 and later | `petoldfusion.dbss`       | 15,364 | 384 Row        | 40        |
| 1      | 1346 and later | `petoldfusionoffset.dbss` | 4,612  | 384 Offset Row | 12        |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 1      | `petoldfusion.dbss`       | 14,980 B (97.5%) | 384 B (2.5%) |
| 1      | `petoldfusionoffset.dbss` | 4,612 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `fac393df5992`  |
| 3482   | Layout 1             | `fac393df5992`  |
| 3474   | Layout 1             | `fac393df5992`  |
| 3473   | Layout 1             | `fac393df5992`  |
| 3464   | Layout 1             | `fac393df5992`  |
| 3458   | Layout 1             | `fac393df5992`  |
| 3454   | Layout 1             | `fac393df5992`  |
| 3444   | Layout 1             | `fac393df5992`  |
| 3435   | Layout 1             | `fac393df5992`  |
| 3426   | Layout 1             | `fac393df5992`  |
| 3418   | Layout 1             | `fac393df5992`  |
| 3412   | Layout 1             | `fac393df5992`  |
| 3402   | Layout 1             | `fac393df5992`  |
| 3396   | Layout 1             | `fac393df5992`  |
| 3387   | Layout 1             | `fac393df5992`  |
| 3381   | Layout 1             | `fac393df5992`  |
| 3373   | Layout 1             | `fac393df5992`  |
| 3364   | Layout 1             | `fac393df5992`  |
| 3356   | Layout 1             | `fac393df5992`  |
| 3349   | Layout 1             | `fac393df5992`  |
| 3342   | Layout 1             | `fac393df5992`  |
| 3335   | Layout 1             | `fac393df5992`  |
| 3326   | Layout 1             | `fac393df5992`  |
| 3321   | Layout 1             | `fac393df5992`  |
| 3314   | Layout 1             | `fac393df5992`  |
| 3303   | Layout 1             | `fac393df5992`  |
| 3302   | Layout 1             | `fac393df5992`  |
| 3293   | Layout 1             | `fac393df5992`  |
| 3283   | Layout 1             | `fac393df5992`  |
| 3275   | Layout 1             | `fac393df5992`  |
| 3267   | Layout 1             | `fac393df5992`  |
| 3258   | Layout 1             | `fac393df5992`  |
| 3251   | Layout 1             | `fac393df5992`  |
| 3242   | Layout 1             | `fac393df5992`  |
| 3235   | Layout 1             | `fac393df5992`  |
| 3229   | Layout 1             | `fac393df5992`  |
| 3212   | Layout 1             | `fac393df5992`  |
| 3203   | Layout 1             | `fac393df5992`  |
| 3193   | Layout 1             | `fac393df5992`  |
| 3186   | Layout 1             | `fac393df5992`  |
| 3177   | Layout 1             | `fac393df5992`  |
| 3169   | Layout 1             | `fac393df5992`  |
| 3158   | Layout 1             | `fac393df5992`  |
| 3151   | Layout 1             | `fac393df5992`  |
| 3144   | Layout 1             | `fac393df5992`  |
| 3133   | Layout 1             | `fac393df5992`  |
| 3125   | Layout 1             | `fac393df5992`  |
| 3118   | Layout 1             | `fac393df5992`  |
| 3111   | Layout 1             | `fac393df5992`  |
| 3103   | Layout 1             | `fac393df5992`  |
| 3095   | Layout 1             | `fac393df5992`  |
| 3086   | Layout 1             | `fac393df5992`  |
| 3072   | Layout 1             | `fac393df5992`  |
| 3062   | Layout 1             | `fac393df5992`  |
| 3052   | Layout 1             | `fac393df5992`  |
| 3045   | Layout 1             | `fac393df5992`  |
| 3037   | Layout 1             | `fac393df5992`  |
| 3030   | Layout 1             | `fac393df5992`  |
| 3021   | Layout 1             | `fac393df5992`  |
| 3012   | Layout 1             | `fac393df5992`  |
| 3002   | Layout 1             | `fac393df5992`  |
| 2995   | Layout 1             | `fac393df5992`  |
| 2987   | Layout 1             | `fac393df5992`  |
| 2978   | Layout 1             | `fac393df5992`  |
| 2970   | Layout 1             | `fac393df5992`  |
| 2959   | Layout 1             | `fac393df5992`  |
| 2951   | Layout 1             | `fac393df5992`  |
| 2942   | Layout 1             | `fac393df5992`  |
| 2935   | Layout 1             | `fac393df5992`  |
| 2932   | Layout 1             | `fac393df5992`  |
| 2923   | Layout 1             | `fac393df5992`  |
| 2919   | Layout 1             | `fac393df5992`  |
| 2907   | Layout 1             | `fac393df5992`  |
| 2900   | Layout 1             | `fac393df5992`  |
| 2891   | Layout 1             | `fac393df5992`  |
| 2882   | Layout 1             | `fac393df5992`  |
| 2872   | Layout 1             | `fac393df5992`  |
| 2863   | Layout 1             | `fac393df5992`  |
| 2855   | Layout 1             | `fac393df5992`  |
| 2849   | Layout 1             | `fac393df5992`  |
| 2844   | Layout 1             | `fac393df5992`  |
| 2834   | Layout 1             | `fac393df5992`  |
| 2825   | Layout 1             | `fac393df5992`  |
| 2819   | Layout 1             | `fac393df5992`  |
| 2811   | Layout 1             | `fac393df5992`  |
| 2803   | Layout 1             | `fac393df5992`  |
| 2794   | Layout 1             | `fac393df5992`  |
| 2783   | Layout 1             | `fac393df5992`  |
| 2774   | Layout 1             | `fac393df5992`  |
| 2765   | Layout 1             | `fac393df5992`  |
| 2756   | Layout 1             | `fac393df5992`  |
| 2750   | Layout 1             | `fac393df5992`  |
| 2743   | Layout 1             | `fac393df5992`  |
| 2736   | Layout 1             | `fac393df5992`  |
| 2726   | Layout 1             | `fac393df5992`  |
| 2717   | Layout 1             | `fac393df5992`  |
| 2709   | Layout 1             | `fac393df5992`  |
| 2703   | Layout 1             | `fac393df5992`  |
| 2695   | Layout 1             | `fac393df5992`  |
| 2684   | Layout 1             | `fac393df5992`  |
| 2672   | Layout 1             | `fac393df5992`  |
| 2665   | Layout 1             | `fac393df5992`  |
| 2657   | Layout 1             | `fac393df5992`  |
| 2649   | Layout 1             | `fac393df5992`  |
| 2644   | Layout 1             | `fac393df5992`  |
| 2637   | Layout 1             | `fac393df5992`  |
| 2629   | Layout 1             | `fac393df5992`  |
| 2619   | Layout 1             | `fac393df5992`  |
| 2612   | Layout 1             | `fac393df5992`  |
| 2606   | Layout 1             | `fac393df5992`  |
| 2602   | Layout 1             | `fac393df5992`  |
| 2601   | Layout 1             | `fac393df5992`  |
| 2592   | Layout 1             | `fac393df5992`  |
| 2583   | Layout 1             | `fac393df5992`  |
| 2575   | Layout 1             | `fac393df5992`  |
| 2567   | Layout 1             | `fac393df5992`  |
| 2560   | Layout 1             | `fac393df5992`  |
| 2553   | Layout 1             | `fac393df5992`  |
| 2545   | Layout 1             | `fac393df5992`  |
| 2538   | Layout 1             | `fac393df5992`  |
| 2529   | Layout 1             | `fac393df5992`  |
| 2519   | Layout 1             | `fac393df5992`  |
| 2513   | Layout 1             | `fac393df5992`  |
| 2510   | Layout 1             | `fac393df5992`  |
| 2507   | Layout 1             | `fac393df5992`  |
| 2503   | Layout 1             | `fac393df5992`  |
| 2498   | Layout 1             | `fac393df5992`  |
| 2492   | Layout 1             | `fac393df5992`  |
| 2487   | Layout 1             | `fac393df5992`  |
| 2480   | Layout 1             | `fac393df5992`  |
| 2474   | Layout 1             | `fac393df5992`  |
| 2468   | Layout 1             | `fac393df5992`  |
| 2460   | Layout 1             | `fac393df5992`  |
| 2453   | Layout 1             | `fac393df5992`  |
| 2444   | Layout 1             | `fac393df5992`  |
| 2438   | Layout 1             | `fac393df5992`  |
| 2434   | Layout 1             | `fac393df5992`  |
| 2429   | Layout 1             | `fac393df5992`  |
| 2421   | Layout 1             | `fac393df5992`  |
| 2414   | Layout 1             | `fac393df5992`  |
| 2407   | Layout 1             | `fac393df5992`  |
| 2401   | Layout 1             | `fac393df5992`  |
| 2397   | Layout 1             | `fac393df5992`  |
| 2393   | Layout 1             | `fac393df5992`  |
| 2384   | Layout 1             | `fac393df5992`  |
| 2378   | Layout 1             | `fac393df5992`  |
| 2372   | Layout 1             | `fac393df5992`  |
| 2358   | Layout 1             | `fac393df5992`  |
| 2352   | Layout 1             | `fac393df5992`  |
| 2347   | Layout 1             | `fac393df5992`  |
| 2343   | Layout 1             | `fac393df5992`  |
| 2335   | Layout 1             | `fac393df5992`  |
| 2327   | Layout 1             | `fac393df5992`  |
| 2324   | Layout 1             | `fac393df5992`  |
| 2319   | Layout 1             | `fac393df5992`  |
| 2313   | Layout 1             | `fac393df5992`  |
| 2308   | Layout 1             | `fac393df5992`  |
| 2302   | Layout 1             | `fac393df5992`  |
| 2295   | Layout 1             | `fac393df5992`  |
| 2290   | Layout 1             | `fac393df5992`  |
| 2284   | Layout 1             | `fac393df5992`  |
| 2276   | Layout 1             | `fac393df5992`  |
| 2269   | Layout 1             | `fac393df5992`  |
| 2259   | Layout 1             | `fac393df5992`  |
| 2250   | Layout 1             | `fac393df5992`  |
| 2243   | Layout 1             | `fac393df5992`  |
| 2235   | Layout 1             | `fac393df5992`  |
| 2229   | Layout 1             | `fac393df5992`  |
| 2224   | Layout 1             | `fac393df5992`  |
| 2218   | Layout 1             | `fac393df5992`  |
| 2215   | Layout 1             | `fac393df5992`  |
| 2207   | Layout 1             | `fac393df5992`  |
| 2203   | Layout 1             | `fac393df5992`  |
| 2196   | Layout 1             | `fac393df5992`  |
| 2192   | Layout 1             | `fac393df5992`  |
| 2189   | Layout 1             | `fac393df5992`  |
| 2183   | Layout 1             | `fac393df5992`  |
| 2179   | Layout 1             | `fac393df5992`  |
| 2171   | Layout 1             | `fac393df5992`  |
| 2163   | Layout 1             | `fac393df5992`  |
| 2156   | Layout 1             | `fac393df5992`  |
| 2151   | Layout 1             | `fac393df5992`  |
| 2147   | Layout 1             | `fac393df5992`  |
| 2142   | Layout 1             | `fac393df5992`  |
| 2138   | Layout 1             | `fac393df5992`  |
| 2134   | Layout 1             | `fac393df5992`  |
| 2130   | Layout 1             | `fac393df5992`  |
| 2122   | Layout 1             | `fac393df5992`  |
| 2107   | Layout 1             | `fac393df5992`  |
| 2098   | Layout 1             | `fac393df5992`  |
| 2089   | Layout 1             | `fac393df5992`  |
| 2081   | Layout 1             | `fac393df5992`  |
| 2073   | Layout 1             | `fac393df5992`  |
| 2067   | Layout 1             | `fac393df5992`  |
| 2063   | Layout 1             | `fac393df5992`  |
| 2059   | Layout 1             | `fac393df5992`  |
| 2052   | Layout 1             | `fac393df5992`  |
| 2044   | Layout 1             | `fac393df5992`  |
| 2039   | Layout 1             | `fac393df5992`  |
| 2032   | Layout 1             | `fac393df5992`  |
| 2025   | Layout 1             | `fac393df5992`  |
| 2011   | Layout 1             | `fac393df5992`  |
| 2005   | Layout 1             | `fac393df5992`  |
| 2000   | Layout 1             | `fac393df5992`  |
| 1996   | Layout 1             | `fac393df5992`  |
| 1991   | Layout 1             | `fac393df5992`  |
| 1985   | Layout 1             | `fac393df5992`  |
| 1980   | Layout 1             | `fac393df5992`  |
| 1969   | Layout 1             | `fac393df5992`  |
| 1964   | Layout 1             | `fac393df5992`  |
| 1958   | Layout 1             | `fac393df5992`  |
| 1950   | Layout 1             | `fac393df5992`  |
| 1945   | Layout 1             | `fac393df5992`  |
| 1937   | Layout 1             | `fac393df5992`  |
| 1933   | Layout 1             | `fac393df5992`  |
| 1927   | Layout 1             | `fac393df5992`  |
| 1921   | Layout 1             | `fac393df5992`  |
| 1914   | Layout 1             | `fac393df5992`  |
| 1908   | Layout 1             | `fac393df5992`  |
| 1897   | Layout 1             | `fac393df5992`  |
| 1892   | Layout 1             | `fac393df5992`  |
| 1886   | Layout 1             | `fac393df5992`  |
| 1881   | Layout 1             | `fac393df5992`  |
| 1871   | Layout 1             | `fac393df5992`  |
| 1866   | Layout 1             | `fac393df5992`  |
| 1862   | Layout 1             | `fac393df5992`  |
| 1854   | Layout 1             | `fac393df5992`  |
| 1846   | Layout 1             | `fac393df5992`  |
| 1838   | Layout 1             | `fac393df5992`  |
| 1832   | Layout 1             | `fac393df5992`  |
| 1826   | Layout 1             | `fac393df5992`  |
| 1822   | Layout 1             | `fac393df5992`  |
| 1818   | Layout 1             | `fac393df5992`  |
| 1804   | Layout 1             | `fac393df5992`  |
| 1794   | Layout 1             | `fac393df5992`  |
| 1790   | Layout 1             | `fac393df5992`  |
| 1784   | Layout 1             | `fac393df5992`  |
| 1774   | Layout 1             | `fac393df5992`  |
| 1771   | Layout 1             | `fac393df5992`  |
| 1762   | Layout 1             | `fac393df5992`  |
| 1759   | Layout 1             | `fac393df5992`  |
| 1754   | Layout 1             | `fac393df5992`  |
| 1749   | Layout 1             | `fac393df5992`  |
| 1743   | Layout 1             | `fac393df5992`  |
| 1737   | Layout 1             | `fac393df5992`  |
| 1731   | Layout 1             | `fac393df5992`  |
| 1725   | Layout 1             | `fac393df5992`  |
| 1717   | Layout 1             | `fac393df5992`  |
| 1710   | Layout 1             | `fac393df5992`  |
| 1704   | Layout 1             | `fac393df5992`  |
| 1698   | Layout 1             | `fac393df5992`  |
| 1690   | Layout 1             | `fac393df5992`  |
| 1685   | Layout 1             | `fac393df5992`  |
| 1680   | Layout 1             | `fac393df5992`  |
| 1674   | Layout 1             | `fac393df5992`  |
| 1668   | Layout 1             | `fac393df5992`  |
| 1659   | Layout 1             | `fac393df5992`  |
| 1649   | Layout 1             | `fac393df5992`  |
| 1642   | Layout 1             | `fac393df5992`  |
| 1636   | Layout 1             | `fac393df5992`  |
| 1628   | Layout 1             | `fac393df5992`  |
| 1622   | Layout 1             | `fac393df5992`  |
| 1614   | Layout 1             | `fac393df5992`  |
| 1608   | Layout 1             | `fac393df5992`  |
| 1602   | Layout 1             | `fac393df5992`  |
| 1598   | Layout 1             | `fac393df5992`  |
| 1594   | Layout 1             | `fac393df5992`  |
| 1590   | Layout 1             | `fac393df5992`  |
| 1587   | Layout 1             | `fac393df5992`  |
| 1584   | Layout 1             | `fac393df5992`  |
| 1579   | Layout 1             | `fac393df5992`  |
| 1572   | Layout 1             | `fac393df5992`  |
| 1565   | Layout 1             | `fac393df5992`  |
| 1559   | Layout 1             | `fac393df5992`  |
| 1554   | Layout 1             | `fac393df5992`  |
| 1547   | Layout 1             | `fac393df5992`  |
| 1537   | Layout 1             | `fac393df5992`  |
| 1529   | Layout 1             | `fac393df5992`  |
| 1524   | Layout 1             | `fac393df5992`  |
| 1519   | Layout 1             | `fac393df5992`  |
| 1509   | Layout 1             | `fac393df5992`  |
| 1506   | Layout 1             | `fac393df5992`  |
| 1504   | Layout 1             | `fac393df5992`  |
| 1500   | Layout 1             | `fac393df5992`  |
| 1493   | Layout 1             | `fac393df5992`  |
| 1489   | Layout 1             | `fac393df5992`  |
| 1485   | Layout 1             | `fac393df5992`  |
| 1481   | Layout 1             | `fac393df5992`  |
| 1474   | Layout 1             | `fac393df5992`  |
| 1466   | Layout 1             | `fac393df5992`  |
| 1462   | Layout 1             | `fac393df5992`  |
| 1459   | Layout 1             | `fac393df5992`  |
| 1453   | Layout 1             | `fac393df5992`  |
| 1450   | Layout 1             | `fac393df5992`  |
| 1445   | Layout 1             | `fac393df5992`  |
| 1439   | Layout 1             | `fac393df5992`  |
| 1433   | Layout 1             | `fac393df5992`  |
| 1430   | Layout 1             | `fac393df5992`  |
| 1426   | Layout 1             | `fac393df5992`  |
| 1421   | Layout 1             | `fac393df5992`  |
| 1417   | Layout 1             | `fac393df5992`  |
| 1416   | Layout 1             | `fac393df5992`  |
| 1409   | Layout 1             | `fac393df5992`  |
| 1405   | Layout 1             | `fac393df5992`  |
| 1401   | Layout 1             | `fac393df5992`  |
| 1396   | Layout 1             | `fac393df5992`  |
| 1391   | Layout 1             | `fac393df5992`  |
| 1390   | Layout 1             | `fac393df5992`  |
| 1386   | Layout 1             | `fac393df5992`  |
| 1381   | Layout 1             | `fac393df5992`  |
| 1379   | Layout 1             | `fac393df5992`  |
| 1372   | Layout 1             | `fac393df5992`  |
| 1366   | Layout 1             | `fac393df5992`  |
| 1364   | Layout 1             | `fac393df5992`  |
| 1363   | Layout 1             | `fac393df5992`  |
| 1360   | Layout 1             | `fac393df5992`  |
| 1358   | Layout 1             | `fac393df5992`  |
| 1355   | Layout 1             | `fac393df5992`  |
| 1351   | Layout 1             | `fac393df5992`  |
| 1348   | Layout 1             | `fac393df5992`  |
| 1346   | Layout 1             | `fac393df5992`  |
| 1341   | No documented layout | `fac393df5992`  |
| 1340   | No documented layout | `fac393df5992`  |
| 1338   | No documented layout | `fac393df5992`  |
| 1335   | No documented layout | `fac393df5992`  |
| 1333   | No documented layout | `fac393df5992`  |
| 1329   | No documented layout | `fac393df5992`  |
| 1327   | No documented layout | `fac393df5992`  |
| 1324   | No documented layout | `fac393df5992`  |
| 1321   | No documented layout | `fac393df5992`  |
| 1319   | No documented layout | `fac393df5992`  |
| 1318   | No documented layout | `fac393df5992`  |
| 1316   | No documented layout | `fac393df5992`  |
| 1313   | No documented layout | `fac393df5992`  |
| 1311   | No documented layout | `fac393df5992`  |
| 1309   | No documented layout | `fac393df5992`  |
| 1304   | No documented layout | `fac393df5992`  |
| 1292   | No documented layout | `fac393df5992`  |
| 1286   | No documented layout | `fac393df5992`  |
| 1280   | No file              | `fac393df5992`  |
| 1276   | No file              | `fac393df5992`  |
| 1267   | No documented layout | `fac393df5992`  |
| 1261   | No documented layout | `fac393df5992`  |
| 1256   | No file              | `fac393df5992`  |
| 1250   | No file              | `fac393df5992`  |
| 1246   | No file              | `fac393df5992`  |
| 1239   | No file              | `fac393df5992`  |
| 1230   | No file              | `fac393df5992`  |
| 1226   | No file              | `fac393df5992`  |
| 1220   | No file              | `fac393df5992`  |
| 1217   | No file              | `fac393df5992`  |
| 1211   | No file              | `fac393df5992`  |
| 1210   | No file              | `fac393df5992`  |
| 1208   | No file              | `fac393df5992`  |
| 1203   | No file              | `fac393df5992`  |
| 1197   | No file              | `fac393df5992`  |
| 1194   | No file              | `fac393df5992`  |
| 1192   | No file              | `fac393df5992`  |
| 1187   | No file              | `fac393df5992`  |
| 1183   | No file              | `fac393df5992`  |
| 1177   | No file              | `fac393df5992`  |
| 1173   | No file              | `fac393df5992`  |
| 1167   | No file              | `fac393df5992`  |
| 1164   | No file              | `fac393df5992`  |
| 1156   | No file              | `fac393df5992`  |
| 1149   | No file              | `fac393df5992`  |
| 1144   | No file              | `fac393df5992`  |
| 1137   | No file              | `fac393df5992`  |
| 1132   | No file              | `fac393df5992`  |
| 1127   | No file              | `fac393df5992`  |
| 1122   | No file              | `fac393df5992`  |
| 1118   | No file              | `fac393df5992`  |
| 1114   | No file              | `fac393df5992`  |
| 1109   | No file              | `fac393df5992`  |
| 1102   | No file              | `fac393df5992`  |
| 1096   | No file              | `fac393df5992`  |
| 1088   | No file              | `fac393df5992`  |
| 1081   | No file              | `fac393df5992`  |
| 1076   | No file              | `fac393df5992`  |
| 1069   | No file              | `fac393df5992`  |
| 1064   | No file              | `fac393df5992`  |
| 1058   | No file              | `fac393df5992`  |
| 1051   | No file              | `fac393df5992`  |
| 1044   | No file              | `fac393df5992`  |
| 1036   | No file              | `fac393df5992`  |
| 1026   | No file              | `fac393df5992`  |
| 1016   | No file              | `fac393df5992`  |
| 1009   | No file              | `fac393df5992`  |
| 1005   | No file              | `fac393df5992`  |
| 1000   | No file              | `fac393df5992`  |
| 998    | No file              | `fac393df5992`  |
| 990    | No file              | `fac393df5992`  |
| 979    | No file              | `fac393df5992`  |
| 972    | No file              | `fac393df5992`  |
| 963    | No file              | `fac393df5992`  |
| 955    | No file              | `fac393df5992`  |
| 946    | No file              | `fac393df5992`  |
| 938    | No file              | `fac393df5992`  |
| 927    | No file              | `fac393df5992`  |
| 911    | No file              | `fac393df5992`  |
| 904    | No file              | `fac393df5992`  |
| 899    | No file              | `fac393df5992`  |
| 894    | No file              | `fac393df5992`  |
| 885    | No file              | `fac393df5992`  |
| 879    | No file              | `fac393df5992`  |
| 872    | No file              | `fac393df5992`  |
| 864    | No file              | `fac393df5992`  |
| 855    | No file              | `fac393df5992`  |
| 853    | No file              | `fac393df5992`  |
| 845    | No file              | `fac393df5992`  |
| 837    | No file              | `fac393df5992`  |
| 829    | No file              | `fac393df5992`  |
| 822    | No file              | `fac393df5992`  |
| 814    | No file              | `fac393df5992`  |
| 805    | No file              | `fac393df5992`  |
| 794    | No file              | `fac393df5992`  |
| 787    | No file              | `fac393df5992`  |
| 780    | No file              | `fac393df5992`  |
| 771    | No file              | `fac393df5992`  |
| 760    | No file              | `fac393df5992`  |
| 748    | No file              | `fac393df5992`  |
| 741    | No file              | `fac393df5992`  |
| 736    | No file              | `fac393df5992`  |
| 731    | No file              | `fac393df5992`  |
| 723    | No file              | `fac393df5992`  |
| 711    | No file              | `fac393df5992`  |
| 707    | No file              | `fac393df5992`  |
| 697    | No file              | `fac393df5992`  |
| 689    | No file              | `fac393df5992`  |
| 683    | No file              | `fac393df5992`  |
| 678    | No file              | `fac393df5992`  |
| 670    | No file              | `fac393df5992`  |
| 661    | No file              | `fac393df5992`  |
| 656    | No file              | `fac393df5992`  |
| 652    | No file              | `fac393df5992`  |
| 643    | No file              | `fac393df5992`  |
| 637    | No file              | `fac393df5992`  |
| 630    | No file              | `fac393df5992`  |
| 627    | No file              | `fac393df5992`  |
| 621    | No file              | `fac393df5992`  |
| 617    | No file              | `fac393df5992`  |
| 615    | No file              | `fac393df5992`  |
| 606    | No file              | `fac393df5992`  |
| 599    | No file              | `fac393df5992`  |
| 592    | No file              | `fac393df5992`  |
| 586    | No file              | `fac393df5992`  |
| 577    | No file              | `fac393df5992`  |
| 569    | No file              | `fac393df5992`  |
| 561    | No file              | `fac393df5992`  |
| 554    | No file              | `fac393df5992`  |
| 542    | No file              | `fac393df5992`  |
| 532    | No file              | `fac393df5992`  |
| 531    | No file              | `fac393df5992`  |
| 526    | No file              | `fac393df5992`  |
| 521    | No file              | `fac393df5992`  |
| 517    | No file              | `fac393df5992`  |
| 510    | No file              | `fac393df5992`  |
| 508    | No file              | `fac393df5992`  |
| 504    | No file              | `fac393df5992`  |
| 497    | No file              | `fac393df5992`  |
| 491    | No file              | `fac393df5992`  |
| 485    | No file              | `fac393df5992`  |
| 478    | No file              | `fac393df5992`  |
| 472    | No file              | `fac393df5992`  |
| 466    | No file              | `fac393df5992`  |
| 457    | No file              | `fac393df5992`  |
| 452    | No file              | `fac393df5992`  |
| 449    | No file              | `fac393df5992`  |
| 435    | No file              | `fac393df5992`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                       |
| ------------------------- | -------- | -------------------------------------------------------------------------- |
| `petoldfusionoffset.dbss` | Optional | `fusion key -> (offset, size)` of every row; the parser walks the main file without it |
| `pet.dbss` + `petoffset.dbss` | Optional | The LOC names of the pets with the row's fusion key                    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 384 x 40 = 15,364 bytes.

### Row (40 bytes)

A 4-byte copy of the fusion key, then the 36 bytes the offset row
addresses.

| Offset  | Type     | Field         | Notes                                                                     |
| ------- | -------- | ------------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | key_prefix    | The fusion key `variant`, `species`, `unknown_06`, `tier` read as one u32 |
| `+0x04` | u8       | variant       | Fusion key byte 0: `variant` of the main pet in `pet.dbss` (sheet `Kind`) |
| `+0x05` | u8       | species       | Fusion key byte 1: `species` (sheet `Race`)                               |
| `+0x06` | u8       | unknown_06    | Fusion key byte 2: `0` on every row, as `unknown_04` of `pet.dbss`         |
| `+0x07` | u8       | tier          | Fusion key byte 3: the main pet's tier, from 0                            |
| `+0x08` | u8       | select_tier_0 | First result tier, from 0                                                 |
| `+0x09` | bytes[3] | padding_09    | Alignment bytes of the `select_tier_0` entry, see Notes                   |
| `+0x0C` | u32      | select_rate_0 | Chance of `select_tier_0`                                                 |
| `+0x10` | u8       | select_tier_1 | Second result tier, from 0; `0` with `select_rate_1` `0` when unused       |
| `+0x11` | bytes[3] | padding_11    | Alignment bytes of the `select_tier_1` entry                              |
| `+0x14` | u32      | select_rate_1 | `1000000` when used, else `0`                                             |
| `+0x18` | u8       | select_tier_2 | `0` on every row (client 3474)                                            |
| `+0x19` | bytes[3] | padding_19    | Alignment bytes of the `select_tier_2` entry                              |
| `+0x1C` | u32      | select_rate_2 | `0` on every row (client 3474)                                            |
| `+0x20` | u8       | select_tier_3 | `0` on every row (client 3474)                                            |
| `+0x21` | bytes[3] | padding_21    | Alignment bytes of the `select_tier_3` entry                              |
| `+0x24` | u32      | select_rate_3 | `0` on every row (client 3474)                                            |

### `petoldfusionoffset.dbss`

Bare offset table into `petoldfusion.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `petoldfusion.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (12 bytes)

| Offset  | Type | Field      | Notes                                                                       |
| ------- | ---- | ---------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | fusion_key | Key of the row it points at, equal to its `key_prefix`                      |
| `+0x04` | u32  | offset     | Absolute byte offset in `petoldfusion.dbss` of the row's `variant`, past the key prefix |
| `+0x08` | u32  | size       | `36` on every row: the row without its key prefix                          |

Both files list the keys in the same order, which is not sorted.

## Exchange Results

On client 3474 the 384 rows cover 96 variant and species pairs of 42
species, four tiers each. With tiers as the game numbers them:

| Main pet | First result | Chance | Second result | Rows (client 3474) |
| -------- | ------------ | ------ | ------------- | ------------------ |
| Tier 1   | Tier 3       | 50%    | Tier 2        | 95                 |
| Tier 2   | Tier 3       | 70%    | Tier 2        | 94                 |
| Tier 3   | Tier 4       | 30%    | Tier 3        | 94                 |
| Tier 4   | Tier 4       | 100%   | none          | 96                 |

Five rows differ: one Tier 1 row with Tier 2 at 100%, one Tier 2 row with
Tier 3 at 100%, one Tier 2 row with Tier 3 at 40%, one Tier 3 row with
Tier 4 at 100% and one Tier 3 row with Tier 4 at 10%.

## Field Names

The `Pet_OldFusion_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Race`, `Kind`, `Tier`, `SelectRate_0` to
`SelectRate_3` and `SelectTier_0` to `SelectTier_3`, and its 380 rows match
the file on all 380 keys (`Race` = `species`, `Kind` = `variant`) and all
eight value columns, on client 1784 (380 rows) and on client 3474 (384
rows; the four more are species `84`, variant `1`). The file stores each
tier before its rate; the sheet lists the rate first, and its empty cells
(`<null>`) are the zeros of the file. The developer workbook
(`datasheet_petdatatable.xlsm`) adds the note columns
`#SelectCharacterName_0` to `#SelectCharacterName_3`, which name each select
tier as a generation (`3세대` for `2`), and `#참조 : 합성 세대 정보`
("reference: fusion generation info") with the tier pairs a row stands for
(`1+1` on tier `0`, `1+2, 2+2` on tier `1`).

The client 1784 server dump names the type `gc::PetOldFusionStaticStatus`,
held in a `BinaryUnorderedMap` keyed by `gc::PetFusionKey`, with the manager
`PetOldFusionStaticStatusManager`. The 2016 client's debug symbols have
`gc::PetFusionKey` as one u32 `_value`, and `gc::PetStaticStatus` stores the
same four bytes as `_fusionKey`; `pet.dbss` names them `variant`, `species`,
a zero byte and `tier`, and this doc takes those names.

## Notes

- `padding_09`, `padding_11`, `padding_19` and `padding_21` are the 3 bytes
  between a u8 tier and its 4-byte aligned rate, as in `petfusionnew.dbss`:
  each select is an 8-byte entry copied whole. On client 3474 they read
  `7F 00 00` in the first three entries and `00 00 00` in the fourth, in
  every row; on client 1784 `00 00 00`, `01 00 00`, `00 00 00` and
  `00 00 00`, while the sheet values are the same.
- Clients 1485, 1784, 2107, 2519, 3002 and 3251 ship both files.
- 20 rows on client 3474, all four tiers of five species and variant pairs
  (species `36` variant `1`, `39` and `6`, `84` and `1`, `99` and `99`,
  `100` and `100`), have no pet with their fusion key in `pet.dbss`; the
  handler's Pets column is empty for them.
- No client Lua reads the file: the exchange window
  (`panel_window_petfusion_all_1.luac`) shows the chances of
  [`petfusionnew.dbss`](petfusionnew_dbss.md) and
  [`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md)
  (`ToClient_getMainFusionRate`, `ToClient_getAddFusionRate`).

## Open Questions

### Whether the Server Still Reads the Table

The live exchange window shows the per-tier chances of `petfusionnew.dbss`,
and Garmoth's pets guide gives chances that match those. Whether the
server still uses the per-species rows here (the name says "old"), and
whether `select_rate_1` `1000000` is a cumulative bound or a chance of its
own, is not in the client data.
