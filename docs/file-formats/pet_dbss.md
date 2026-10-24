# `pet.dbss` Format

## Purpose

Defines one record per pet: species, tier, level cap, EXP table, look, icon path, market price fields, the loot, race and base skills, the equip-skill roll pool and the ten action rates. Each record is a specific pet at a specific tier (e.g. "Dog variant #40 at Tier 4"); fairies are pet records too (`pet_type` 1). Companion `petoffset.dbss` enables O(1) lookup by pet ID.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes   | Records                     | Row bytes                  |
| ------ | -------------- | ------- | ---------------- | ------- | --------------------------- | -------------------------- |
| 1      | 1685 and later | 3483    | `pet.dbss`       | 376,078 | 2,009 Payload, 2,009 Record | 180 to 194, 185 on average |
| 1      | 1685 and later | 3483    | `petoffset.dbss` | 20,094  | 2,009 Offset Row            | 10                         |

| Layout | File             | Known             | Unknown         |
| ------ | ---------------- | ----------------- | --------------- |
| 1      | `pet.dbss`       | 357,997 B (95.2%) | 18,081 B (4.8%) |
| 1      | `petoffset.dbss` | 16,076 B (80.0%)  | 4,018 B (20.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `72dd805ffcdc`  |
| 3482   | Layout 1             | `72dd805ffcdc`  |
| 3474   | Layout 1             | `72dd805ffcdc`  |
| 3473   | Layout 1             | `72dd805ffcdc`  |
| 3464   | Layout 1             | `72dd805ffcdc`  |
| 3458   | Layout 1             | `72dd805ffcdc`  |
| 3454   | Layout 1             | `72dd805ffcdc`  |
| 3444   | Layout 1             | `72dd805ffcdc`  |
| 3435   | Layout 1             | `72dd805ffcdc`  |
| 3426   | Layout 1             | `72dd805ffcdc`  |
| 3418   | Layout 1             | `72dd805ffcdc`  |
| 3412   | Layout 1             | `72dd805ffcdc`  |
| 3402   | Layout 1             | `72dd805ffcdc`  |
| 3396   | Layout 1             | `72dd805ffcdc`  |
| 3387   | Layout 1             | `72dd805ffcdc`  |
| 3381   | Layout 1             | `72dd805ffcdc`  |
| 3373   | Layout 1             | `72dd805ffcdc`  |
| 3364   | Layout 1             | `72dd805ffcdc`  |
| 3356   | Layout 1             | `72dd805ffcdc`  |
| 3349   | Layout 1             | `72dd805ffcdc`  |
| 3342   | Layout 1             | `72dd805ffcdc`  |
| 3335   | Layout 1             | `72dd805ffcdc`  |
| 3326   | Layout 1             | `72dd805ffcdc`  |
| 3321   | Layout 1             | `72dd805ffcdc`  |
| 3314   | Layout 1             | `72dd805ffcdc`  |
| 3303   | Layout 1             | `72dd805ffcdc`  |
| 3302   | Layout 1             | `72dd805ffcdc`  |
| 3293   | Layout 1             | `72dd805ffcdc`  |
| 3283   | Layout 1             | `72dd805ffcdc`  |
| 3275   | Layout 1             | `72dd805ffcdc`  |
| 3267   | Layout 1             | `72dd805ffcdc`  |
| 3258   | Layout 1             | `72dd805ffcdc`  |
| 3251   | Layout 1             | `72dd805ffcdc`  |
| 3242   | Layout 1             | `72dd805ffcdc`  |
| 3235   | Layout 1             | `72dd805ffcdc`  |
| 3229   | Layout 1             | `72dd805ffcdc`  |
| 3212   | Layout 1             | `72dd805ffcdc`  |
| 3203   | Layout 1             | `72dd805ffcdc`  |
| 3193   | Layout 1             | `72dd805ffcdc`  |
| 3186   | Layout 1             | `72dd805ffcdc`  |
| 3177   | Layout 1             | `72dd805ffcdc`  |
| 3169   | Layout 1             | `72dd805ffcdc`  |
| 3158   | Layout 1             | `72dd805ffcdc`  |
| 3151   | Layout 1             | `72dd805ffcdc`  |
| 3144   | Layout 1             | `72dd805ffcdc`  |
| 3133   | Layout 1             | `72dd805ffcdc`  |
| 3125   | Layout 1             | `72dd805ffcdc`  |
| 3118   | Layout 1             | `72dd805ffcdc`  |
| 3111   | Layout 1             | `72dd805ffcdc`  |
| 3103   | Layout 1             | `72dd805ffcdc`  |
| 3095   | Layout 1             | `72dd805ffcdc`  |
| 3086   | Layout 1             | `72dd805ffcdc`  |
| 3072   | Layout 1             | `72dd805ffcdc`  |
| 3062   | Layout 1             | `72dd805ffcdc`  |
| 3052   | Layout 1             | `72dd805ffcdc`  |
| 3045   | Layout 1             | `72dd805ffcdc`  |
| 3037   | Layout 1             | `72dd805ffcdc`  |
| 3030   | Layout 1             | `72dd805ffcdc`  |
| 3021   | Layout 1             | `72dd805ffcdc`  |
| 3012   | Layout 1             | `72dd805ffcdc`  |
| 3002   | Layout 1             | `72dd805ffcdc`  |
| 2995   | Layout 1             | `72dd805ffcdc`  |
| 2987   | Layout 1             | `72dd805ffcdc`  |
| 2978   | Layout 1             | `72dd805ffcdc`  |
| 2970   | Layout 1             | `72dd805ffcdc`  |
| 2959   | Layout 1             | `72dd805ffcdc`  |
| 2951   | Layout 1             | `72dd805ffcdc`  |
| 2942   | Layout 1             | `72dd805ffcdc`  |
| 2935   | Layout 1             | `72dd805ffcdc`  |
| 2932   | Layout 1             | `72dd805ffcdc`  |
| 2923   | Layout 1             | `72dd805ffcdc`  |
| 2919   | Layout 1             | `72dd805ffcdc`  |
| 2907   | Layout 1             | `72dd805ffcdc`  |
| 2900   | Layout 1             | `72dd805ffcdc`  |
| 2891   | Layout 1             | `72dd805ffcdc`  |
| 2882   | Layout 1             | `72dd805ffcdc`  |
| 2872   | Layout 1             | `72dd805ffcdc`  |
| 2863   | Layout 1             | `72dd805ffcdc`  |
| 2855   | Layout 1             | `72dd805ffcdc`  |
| 2849   | Layout 1             | `72dd805ffcdc`  |
| 2844   | Layout 1             | `72dd805ffcdc`  |
| 2834   | Layout 1             | `72dd805ffcdc`  |
| 2825   | Layout 1             | `72dd805ffcdc`  |
| 2819   | Layout 1             | `72dd805ffcdc`  |
| 2811   | Layout 1             | `72dd805ffcdc`  |
| 2803   | Layout 1             | `72dd805ffcdc`  |
| 2794   | Layout 1             | `72dd805ffcdc`  |
| 2783   | Layout 1             | `72dd805ffcdc`  |
| 2774   | Layout 1             | `72dd805ffcdc`  |
| 2765   | Layout 1             | `72dd805ffcdc`  |
| 2756   | Layout 1             | `72dd805ffcdc`  |
| 2750   | Layout 1             | `72dd805ffcdc`  |
| 2743   | Layout 1             | `72dd805ffcdc`  |
| 2736   | Layout 1             | `72dd805ffcdc`  |
| 2726   | Layout 1             | `72dd805ffcdc`  |
| 2717   | Layout 1             | `72dd805ffcdc`  |
| 2709   | Layout 1             | `72dd805ffcdc`  |
| 2703   | Layout 1             | `72dd805ffcdc`  |
| 2695   | Layout 1             | `72dd805ffcdc`  |
| 2684   | Layout 1             | `72dd805ffcdc`  |
| 2672   | Layout 1             | `72dd805ffcdc`  |
| 2665   | Layout 1             | `72dd805ffcdc`  |
| 2657   | Layout 1             | `72dd805ffcdc`  |
| 2649   | Layout 1             | `72dd805ffcdc`  |
| 2644   | Layout 1             | `72dd805ffcdc`  |
| 2637   | Layout 1             | `72dd805ffcdc`  |
| 2629   | Layout 1             | `72dd805ffcdc`  |
| 2619   | Layout 1             | `72dd805ffcdc`  |
| 2612   | Layout 1             | `72dd805ffcdc`  |
| 2606   | Layout 1             | `72dd805ffcdc`  |
| 2602   | Layout 1             | `72dd805ffcdc`  |
| 2601   | Layout 1             | `72dd805ffcdc`  |
| 2592   | Layout 1             | `72dd805ffcdc`  |
| 2583   | Layout 1             | `72dd805ffcdc`  |
| 2575   | Layout 1             | `72dd805ffcdc`  |
| 2567   | Layout 1             | `72dd805ffcdc`  |
| 2560   | Layout 1             | `72dd805ffcdc`  |
| 2553   | Layout 1             | `72dd805ffcdc`  |
| 2545   | Layout 1             | `72dd805ffcdc`  |
| 2538   | Layout 1             | `72dd805ffcdc`  |
| 2529   | Layout 1             | `72dd805ffcdc`  |
| 2519   | Layout 1             | `72dd805ffcdc`  |
| 2513   | Layout 1             | `72dd805ffcdc`  |
| 2510   | Layout 1             | `72dd805ffcdc`  |
| 2507   | Layout 1             | `72dd805ffcdc`  |
| 2503   | Layout 1             | `72dd805ffcdc`  |
| 2498   | Layout 1             | `72dd805ffcdc`  |
| 2492   | Layout 1             | `72dd805ffcdc`  |
| 2487   | Layout 1             | `72dd805ffcdc`  |
| 2480   | Layout 1             | `72dd805ffcdc`  |
| 2474   | Layout 1             | `72dd805ffcdc`  |
| 2468   | Layout 1             | `72dd805ffcdc`  |
| 2460   | Layout 1             | `72dd805ffcdc`  |
| 2453   | Layout 1             | `72dd805ffcdc`  |
| 2444   | Layout 1             | `72dd805ffcdc`  |
| 2438   | Layout 1             | `72dd805ffcdc`  |
| 2434   | Layout 1             | `72dd805ffcdc`  |
| 2429   | Layout 1             | `72dd805ffcdc`  |
| 2421   | Layout 1             | `72dd805ffcdc`  |
| 2414   | Layout 1             | `72dd805ffcdc`  |
| 2407   | Layout 1             | `72dd805ffcdc`  |
| 2401   | Layout 1             | `72dd805ffcdc`  |
| 2397   | Layout 1             | `72dd805ffcdc`  |
| 2393   | Layout 1             | `72dd805ffcdc`  |
| 2384   | Layout 1             | `72dd805ffcdc`  |
| 2378   | Layout 1             | `72dd805ffcdc`  |
| 2372   | Layout 1             | `72dd805ffcdc`  |
| 2358   | Layout 1             | `72dd805ffcdc`  |
| 2352   | Layout 1             | `72dd805ffcdc`  |
| 2347   | Layout 1             | `72dd805ffcdc`  |
| 2343   | Layout 1             | `72dd805ffcdc`  |
| 2335   | Layout 1             | `72dd805ffcdc`  |
| 2327   | Layout 1             | `72dd805ffcdc`  |
| 2324   | Layout 1             | `72dd805ffcdc`  |
| 2319   | Layout 1             | `72dd805ffcdc`  |
| 2313   | Layout 1             | `72dd805ffcdc`  |
| 2308   | Layout 1             | `72dd805ffcdc`  |
| 2302   | Layout 1             | `72dd805ffcdc`  |
| 2295   | Layout 1             | `72dd805ffcdc`  |
| 2290   | Layout 1             | `72dd805ffcdc`  |
| 2284   | Layout 1             | `72dd805ffcdc`  |
| 2276   | Layout 1             | `72dd805ffcdc`  |
| 2269   | Layout 1             | `72dd805ffcdc`  |
| 2259   | Layout 1             | `72dd805ffcdc`  |
| 2250   | Layout 1             | `72dd805ffcdc`  |
| 2243   | Layout 1             | `72dd805ffcdc`  |
| 2235   | Layout 1             | `72dd805ffcdc`  |
| 2229   | Layout 1             | `72dd805ffcdc`  |
| 2224   | Layout 1             | `72dd805ffcdc`  |
| 2218   | Layout 1             | `72dd805ffcdc`  |
| 2215   | Layout 1             | `72dd805ffcdc`  |
| 2207   | Layout 1             | `72dd805ffcdc`  |
| 2203   | Layout 1             | `72dd805ffcdc`  |
| 2196   | Layout 1             | `72dd805ffcdc`  |
| 2192   | Layout 1             | `72dd805ffcdc`  |
| 2189   | Layout 1             | `72dd805ffcdc`  |
| 2183   | Layout 1             | `72dd805ffcdc`  |
| 2179   | Layout 1             | `72dd805ffcdc`  |
| 2171   | Layout 1             | `72dd805ffcdc`  |
| 2163   | Layout 1             | `72dd805ffcdc`  |
| 2156   | Layout 1             | `72dd805ffcdc`  |
| 2151   | Layout 1             | `72dd805ffcdc`  |
| 2147   | Layout 1             | `72dd805ffcdc`  |
| 2142   | Layout 1             | `72dd805ffcdc`  |
| 2138   | Layout 1             | `72dd805ffcdc`  |
| 2134   | Layout 1             | `72dd805ffcdc`  |
| 2130   | Layout 1             | `72dd805ffcdc`  |
| 2122   | Layout 1             | `72dd805ffcdc`  |
| 2107   | Layout 1             | `72dd805ffcdc`  |
| 2098   | Layout 1             | `72dd805ffcdc`  |
| 2089   | Layout 1             | `72dd805ffcdc`  |
| 2081   | Layout 1             | `72dd805ffcdc`  |
| 2073   | Layout 1             | `72dd805ffcdc`  |
| 2067   | Layout 1             | `72dd805ffcdc`  |
| 2063   | Layout 1             | `72dd805ffcdc`  |
| 2059   | Layout 1             | `72dd805ffcdc`  |
| 2052   | Layout 1             | `72dd805ffcdc`  |
| 2044   | Layout 1             | `72dd805ffcdc`  |
| 2039   | Layout 1             | `72dd805ffcdc`  |
| 2032   | Layout 1             | `72dd805ffcdc`  |
| 2025   | Layout 1             | `72dd805ffcdc`  |
| 2011   | Layout 1             | `72dd805ffcdc`  |
| 2005   | Layout 1             | `72dd805ffcdc`  |
| 2000   | Layout 1             | `72dd805ffcdc`  |
| 1996   | Layout 1             | `72dd805ffcdc`  |
| 1991   | Layout 1             | `72dd805ffcdc`  |
| 1985   | Layout 1             | `72dd805ffcdc`  |
| 1980   | Layout 1             | `72dd805ffcdc`  |
| 1969   | Layout 1             | `72dd805ffcdc`  |
| 1964   | Layout 1             | `72dd805ffcdc`  |
| 1958   | Layout 1             | `72dd805ffcdc`  |
| 1950   | Layout 1             | `72dd805ffcdc`  |
| 1945   | Layout 1             | `72dd805ffcdc`  |
| 1937   | Layout 1             | `72dd805ffcdc`  |
| 1933   | Layout 1             | `72dd805ffcdc`  |
| 1927   | Layout 1             | `72dd805ffcdc`  |
| 1921   | Layout 1             | `72dd805ffcdc`  |
| 1914   | Layout 1             | `72dd805ffcdc`  |
| 1908   | Layout 1             | `72dd805ffcdc`  |
| 1897   | Layout 1             | `72dd805ffcdc`  |
| 1892   | Layout 1             | `72dd805ffcdc`  |
| 1886   | Layout 1             | `72dd805ffcdc`  |
| 1881   | Layout 1             | `72dd805ffcdc`  |
| 1871   | Layout 1             | `72dd805ffcdc`  |
| 1866   | Layout 1             | `72dd805ffcdc`  |
| 1862   | Layout 1             | `72dd805ffcdc`  |
| 1854   | Layout 1             | `72dd805ffcdc`  |
| 1846   | Layout 1             | `72dd805ffcdc`  |
| 1838   | Layout 1             | `72dd805ffcdc`  |
| 1832   | Layout 1             | `72dd805ffcdc`  |
| 1826   | Layout 1             | `72dd805ffcdc`  |
| 1822   | Layout 1             | `72dd805ffcdc`  |
| 1818   | Layout 1             | `72dd805ffcdc`  |
| 1804   | Layout 1             | `72dd805ffcdc`  |
| 1794   | Layout 1             | `72dd805ffcdc`  |
| 1790   | Layout 1             | `72dd805ffcdc`  |
| 1784   | Layout 1             | `72dd805ffcdc`  |
| 1774   | Layout 1             | `72dd805ffcdc`  |
| 1771   | Layout 1             | `72dd805ffcdc`  |
| 1762   | Layout 1             | `72dd805ffcdc`  |
| 1759   | Layout 1             | `72dd805ffcdc`  |
| 1754   | Layout 1             | `72dd805ffcdc`  |
| 1749   | Layout 1             | `72dd805ffcdc`  |
| 1743   | Layout 1             | `72dd805ffcdc`  |
| 1737   | Layout 1             | `72dd805ffcdc`  |
| 1731   | Layout 1             | `72dd805ffcdc`  |
| 1725   | Layout 1             | `72dd805ffcdc`  |
| 1717   | Layout 1             | `72dd805ffcdc`  |
| 1710   | Layout 1             | `72dd805ffcdc`  |
| 1704   | Layout 1             | `72dd805ffcdc`  |
| 1698   | Layout 1             | `72dd805ffcdc`  |
| 1690   | Layout 1             | `72dd805ffcdc`  |
| 1685   | Layout 1             | `72dd805ffcdc`  |
| 1680   | No documented layout | `72dd805ffcdc`  |
| 1674   | No documented layout | `72dd805ffcdc`  |
| 1668   | No documented layout | `72dd805ffcdc`  |
| 1659   | No documented layout | `72dd805ffcdc`  |
| 1649   | No documented layout | `72dd805ffcdc`  |
| 1642   | No documented layout | `72dd805ffcdc`  |
| 1636   | No documented layout | `72dd805ffcdc`  |
| 1628   | No documented layout | `72dd805ffcdc`  |
| 1622   | No documented layout | `72dd805ffcdc`  |
| 1614   | No documented layout | `72dd805ffcdc`  |
| 1608   | No documented layout | `72dd805ffcdc`  |
| 1602   | No documented layout | `72dd805ffcdc`  |
| 1598   | No documented layout | `72dd805ffcdc`  |
| 1594   | No documented layout | `72dd805ffcdc`  |
| 1590   | No documented layout | `72dd805ffcdc`  |
| 1587   | No documented layout | `72dd805ffcdc`  |
| 1584   | No documented layout | `72dd805ffcdc`  |
| 1579   | No documented layout | `72dd805ffcdc`  |
| 1572   | No documented layout | `72dd805ffcdc`  |
| 1565   | No documented layout | `72dd805ffcdc`  |
| 1559   | No documented layout | `72dd805ffcdc`  |
| 1554   | No documented layout | `72dd805ffcdc`  |
| 1547   | No documented layout | `72dd805ffcdc`  |
| 1537   | No documented layout | `72dd805ffcdc`  |
| 1529   | No documented layout | `72dd805ffcdc`  |
| 1524   | No documented layout | `72dd805ffcdc`  |
| 1519   | No documented layout | `72dd805ffcdc`  |
| 1509   | No documented layout | `72dd805ffcdc`  |
| 1506   | No documented layout | `72dd805ffcdc`  |
| 1504   | No documented layout | `72dd805ffcdc`  |
| 1500   | No documented layout | `72dd805ffcdc`  |
| 1493   | No documented layout | `72dd805ffcdc`  |
| 1489   | No documented layout | `72dd805ffcdc`  |
| 1485   | No documented layout | `72dd805ffcdc`  |
| 1481   | No documented layout | `72dd805ffcdc`  |
| 1474   | No documented layout | `72dd805ffcdc`  |
| 1466   | No documented layout | `72dd805ffcdc`  |
| 1462   | No documented layout | `72dd805ffcdc`  |
| 1459   | No documented layout | `72dd805ffcdc`  |
| 1453   | No documented layout | `72dd805ffcdc`  |
| 1450   | No documented layout | `72dd805ffcdc`  |
| 1445   | No documented layout | `72dd805ffcdc`  |
| 1439   | No documented layout | `72dd805ffcdc`  |
| 1433   | No documented layout | `72dd805ffcdc`  |
| 1430   | No documented layout | `72dd805ffcdc`  |
| 1426   | No documented layout | `72dd805ffcdc`  |
| 1421   | No documented layout | `72dd805ffcdc`  |
| 1417   | No documented layout | `72dd805ffcdc`  |
| 1416   | No documented layout | `72dd805ffcdc`  |
| 1409   | No documented layout | `72dd805ffcdc`  |
| 1405   | No documented layout | `72dd805ffcdc`  |
| 1401   | No documented layout | `72dd805ffcdc`  |
| 1396   | No documented layout | `72dd805ffcdc`  |
| 1391   | No documented layout | `72dd805ffcdc`  |
| 1390   | No documented layout | `72dd805ffcdc`  |
| 1386   | No documented layout | `72dd805ffcdc`  |
| 1381   | No documented layout | `72dd805ffcdc`  |
| 1379   | No documented layout | `72dd805ffcdc`  |
| 1372   | No documented layout | `72dd805ffcdc`  |
| 1366   | No documented layout | `72dd805ffcdc`  |
| 1364   | No documented layout | `72dd805ffcdc`  |
| 1363   | No documented layout | `72dd805ffcdc`  |
| 1360   | No documented layout | `72dd805ffcdc`  |
| 1358   | No documented layout | `72dd805ffcdc`  |
| 1355   | No documented layout | `72dd805ffcdc`  |
| 1351   | No documented layout | `72dd805ffcdc`  |
| 1348   | No documented layout | `72dd805ffcdc`  |
| 1346   | No documented layout | `72dd805ffcdc`  |
| 1341   | No documented layout | `72dd805ffcdc`  |
| 1340   | No documented layout | `72dd805ffcdc`  |
| 1338   | No documented layout | `72dd805ffcdc`  |
| 1335   | No documented layout | `72dd805ffcdc`  |
| 1333   | No documented layout | `72dd805ffcdc`  |
| 1329   | No documented layout | `72dd805ffcdc`  |
| 1327   | No documented layout | `72dd805ffcdc`  |
| 1324   | No documented layout | `72dd805ffcdc`  |
| 1321   | No documented layout | `72dd805ffcdc`  |
| 1319   | No documented layout | `72dd805ffcdc`  |
| 1318   | No documented layout | `72dd805ffcdc`  |
| 1316   | No documented layout | `72dd805ffcdc`  |
| 1313   | No documented layout | `72dd805ffcdc`  |
| 1311   | No documented layout | `72dd805ffcdc`  |
| 1309   | No documented layout | `72dd805ffcdc`  |
| 1304   | No documented layout | `72dd805ffcdc`  |
| 1292   | No documented layout | `72dd805ffcdc`  |
| 1286   | No documented layout | `72dd805ffcdc`  |
| 1280   | No file              | `72dd805ffcdc`  |
| 1276   | No file              | `72dd805ffcdc`  |
| 1267   | No documented layout | `72dd805ffcdc`  |
| 1261   | No documented layout | `72dd805ffcdc`  |
| 1256   | No file              | `72dd805ffcdc`  |
| 1250   | No file              | `72dd805ffcdc`  |
| 1246   | No file              | `72dd805ffcdc`  |
| 1239   | No file              | `72dd805ffcdc`  |
| 1230   | No file              | `72dd805ffcdc`  |
| 1226   | No file              | `72dd805ffcdc`  |
| 1220   | No file              | `72dd805ffcdc`  |
| 1217   | No file              | `72dd805ffcdc`  |
| 1211   | No file              | `72dd805ffcdc`  |
| 1210   | No file              | `72dd805ffcdc`  |
| 1208   | No file              | `72dd805ffcdc`  |
| 1203   | No file              | `72dd805ffcdc`  |
| 1197   | No file              | `72dd805ffcdc`  |
| 1194   | No file              | `72dd805ffcdc`  |
| 1192   | No file              | `72dd805ffcdc`  |
| 1187   | No file              | `72dd805ffcdc`  |
| 1183   | No file              | `72dd805ffcdc`  |
| 1177   | No file              | `72dd805ffcdc`  |
| 1173   | No file              | `72dd805ffcdc`  |
| 1167   | No file              | `72dd805ffcdc`  |
| 1164   | No file              | `72dd805ffcdc`  |
| 1156   | No file              | `72dd805ffcdc`  |
| 1149   | No file              | `72dd805ffcdc`  |
| 1144   | No file              | `72dd805ffcdc`  |
| 1137   | No file              | `72dd805ffcdc`  |
| 1132   | No file              | `72dd805ffcdc`  |
| 1127   | No file              | `72dd805ffcdc`  |
| 1122   | No file              | `72dd805ffcdc`  |
| 1118   | No file              | `72dd805ffcdc`  |
| 1114   | No file              | `72dd805ffcdc`  |
| 1109   | No file              | `72dd805ffcdc`  |
| 1102   | No file              | `72dd805ffcdc`  |
| 1096   | No file              | `72dd805ffcdc`  |
| 1088   | No file              | `72dd805ffcdc`  |
| 1081   | No file              | `72dd805ffcdc`  |
| 1076   | No file              | `72dd805ffcdc`  |
| 1069   | No file              | `72dd805ffcdc`  |
| 1064   | No file              | `72dd805ffcdc`  |
| 1058   | No file              | `72dd805ffcdc`  |
| 1051   | No file              | `72dd805ffcdc`  |
| 1044   | No file              | `72dd805ffcdc`  |
| 1036   | No file              | `72dd805ffcdc`  |
| 1026   | No file              | `72dd805ffcdc`  |
| 1016   | No file              | `72dd805ffcdc`  |
| 1009   | No file              | `72dd805ffcdc`  |
| 1005   | No file              | `72dd805ffcdc`  |
| 1000   | No file              | `72dd805ffcdc`  |
| 998    | No file              | `72dd805ffcdc`  |
| 990    | No file              | `72dd805ffcdc`  |
| 979    | No file              | `72dd805ffcdc`  |
| 972    | No file              | `72dd805ffcdc`  |
| 963    | No file              | `72dd805ffcdc`  |
| 955    | No file              | `72dd805ffcdc`  |
| 946    | No file              | `72dd805ffcdc`  |
| 938    | No file              | `72dd805ffcdc`  |
| 927    | No file              | `72dd805ffcdc`  |
| 911    | No file              | `72dd805ffcdc`  |
| 904    | No file              | `72dd805ffcdc`  |
| 899    | No file              | `72dd805ffcdc`  |
| 894    | No file              | `72dd805ffcdc`  |
| 885    | No file              | `72dd805ffcdc`  |
| 879    | No file              | `72dd805ffcdc`  |
| 872    | No file              | `72dd805ffcdc`  |
| 864    | No file              | `72dd805ffcdc`  |
| 855    | No file              | `72dd805ffcdc`  |
| 853    | No file              | `72dd805ffcdc`  |
| 845    | No file              | `72dd805ffcdc`  |
| 837    | No file              | `72dd805ffcdc`  |
| 829    | No file              | `72dd805ffcdc`  |
| 822    | No file              | `72dd805ffcdc`  |
| 814    | No file              | `72dd805ffcdc`  |
| 805    | No file              | `72dd805ffcdc`  |
| 794    | No file              | `72dd805ffcdc`  |
| 787    | No file              | `72dd805ffcdc`  |
| 780    | No file              | `72dd805ffcdc`  |
| 771    | No file              | `72dd805ffcdc`  |
| 760    | No file              | `72dd805ffcdc`  |
| 748    | No file              | `72dd805ffcdc`  |
| 741    | No file              | `72dd805ffcdc`  |
| 736    | No file              | `72dd805ffcdc`  |
| 731    | No file              | `72dd805ffcdc`  |
| 723    | No file              | `72dd805ffcdc`  |
| 711    | No file              | `72dd805ffcdc`  |
| 707    | No file              | `72dd805ffcdc`  |
| 697    | No file              | `72dd805ffcdc`  |
| 689    | No file              | `72dd805ffcdc`  |
| 683    | No file              | `72dd805ffcdc`  |
| 678    | No file              | `72dd805ffcdc`  |
| 670    | No file              | `72dd805ffcdc`  |
| 661    | No file              | `72dd805ffcdc`  |
| 656    | No file              | `72dd805ffcdc`  |
| 652    | No file              | `72dd805ffcdc`  |
| 643    | No file              | `72dd805ffcdc`  |
| 637    | No file              | `72dd805ffcdc`  |
| 630    | No file              | `72dd805ffcdc`  |
| 627    | No file              | `72dd805ffcdc`  |
| 621    | No file              | `72dd805ffcdc`  |
| 617    | No file              | `72dd805ffcdc`  |
| 615    | No file              | `72dd805ffcdc`  |
| 606    | No file              | `72dd805ffcdc`  |
| 599    | No file              | `72dd805ffcdc`  |
| 592    | No file              | `72dd805ffcdc`  |
| 586    | No file              | `72dd805ffcdc`  |
| 577    | No file              | `72dd805ffcdc`  |
| 569    | No file              | `72dd805ffcdc`  |
| 561    | No file              | `72dd805ffcdc`  |
| 554    | No file              | `72dd805ffcdc`  |
| 542    | No file              | `72dd805ffcdc`  |
| 532    | No file              | `72dd805ffcdc`  |
| 531    | No file              | `72dd805ffcdc`  |
| 526    | No file              | `72dd805ffcdc`  |
| 521    | No file              | `72dd805ffcdc`  |
| 517    | No file              | `72dd805ffcdc`  |
| 510    | No file              | `72dd805ffcdc`  |
| 508    | No file              | `72dd805ffcdc`  |
| 504    | No file              | `72dd805ffcdc`  |
| 497    | No file              | `72dd805ffcdc`  |
| 491    | No file              | `72dd805ffcdc`  |
| 485    | No file              | `72dd805ffcdc`  |
| 478    | No file              | `72dd805ffcdc`  |
| 472    | No file              | `72dd805ffcdc`  |
| 466    | No file              | `72dd805ffcdc`  |
| 457    | No file              | `72dd805ffcdc`  |
| 452    | No file              | `72dd805ffcdc`  |
| 449    | No file              | `72dd805ffcdc`  |
| 435    | No file              | `72dd805ffcdc`  |

<!-- versions:end -->

## Companion Files

| File             | Required | Role                                                     |
| ---------------- | -------- | -------------------------------------------------------- |
| `petoffset.dbss` | Required | `pet_id → (data_offset, data_size)` for variable records |
| `petgrade.dbss`  | Optional | `(species, variant) → grade` per pet type                |
| `petequipskill.bss` | Optional | `base_skill_id` → base skill name (Section 2, LOC type 10) |
| `petskill.dbss`, `petskilloffset.dbss` | Optional | `loot_skill_id` and `race_skill_id` → skill type |
| `stringtable.bss` | Optional | Key hashes of the skill type names, see [petskill.dbss](petskill_dbss.md#skill-types) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petoffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                                                                  |
| ------- | ------------- | ------- | ---------------------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of pet records (observed: 1,782 before 2026-09-27, 2,009 after) |
| `+0x04` | Record[count] | records | See Record                                                             |

`+0x04` is the key prefix of the first record (`first_record_key` in earlier
versions of this doc), not a standalone header field. Records begin
immediately at `+0x04`.

### Record (variable: 2 bytes + payload)

Typically 181 to 194 bytes. Each record is stored as
`[u16 key_prefix][data_bytes]`. The `key_prefix` (2 bytes) equals `pet_id`
and is also the first 2 bytes of `data_bytes`.

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_id`                                        |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 126 bytes + icon path text)

The 32-byte fixed header, the icon path, then the 94-byte fixed footer.
Counts are records on client 3473.

| Offset           | Type     | Field                         | Notes                                                                                   |
| ---------------- | -------- | ----------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`          | u16      | pet_id                        | Unique record key; equal to the preceding 2-byte file prefix                            |
| `+0x02`          | u8       | variant                       | Sub-variant within the species (1–57 observed)                                          |
| `+0x03`          | u8       | species                       | Pet family/model code                                                                   |
| `+0x04`          | u8       | unknown_04                    | `0` in every record                                                                     |
| `+0x05`          | u8       | tier                          | Tier (0 = lowest, 4 = highest for regular pets)                                         |
| `+0x06`          | u8       | unknown_06                    | `1` in every record                                                                     |
| `+0x07`          | i32      | max_level                     | 10 on 1,994 records; Laila has 10, 20, 30 or 50 by `exp_key`                            |
| `+0x0B`          | i32      | max_hunger                    | `400` in every record                                                                   |
| `+0x0F`          | u16      | exp_key                       | Key into [petexp.dbss](petexp_dbss.md): 1 to 4 for pets, 6 to 9 for the Laila grades    |
| `+0x11`          | u8       | is_indexed                    | `1` on 355 records                                                                      |
| `+0x12`          | u32      | default_action_index          | Default look within the `change_look_key` group                                         |
| `+0x16`          | u16      | change_look_key               | Key into [`petchangelook.dbss`](petchangelook_dbss.md); `0` on 614 records              |
| `+0x18`          | str8     | icon_path                     | u64 byte length (`icon_path_len`), then the ASCII path with no null terminator          |
| `icon_path+0x00` | i64      | base_price_for_pet_market     | `30000` in every record                                                                 |
| `icon_path+0x08` | i64      | min_price_for_pet_market      | `base_price_for_pet_market × minest_percent_for_pet_market / 1,000,000`                  |
| `icon_path+0x10` | i64      | max_price_for_pet_market      | `base_price_for_pet_market × maxest_percent_for_pet_market / 1,000,000`                  |
| `icon_path+0x18` | i32      | minest_percent_for_pet_market | Millionths; `500000` in every record                                                    |
| `icon_path+0x1C` | i32      | maxest_percent_for_pet_market | Millionths; `1000000` in every record                                                   |
| `icon_path+0x20` | u32      | skill_max_count               | `2` in every record: `loot_skill_id` and `race_skill_id`                                 |
| `icon_path+0x24` | u16      | acquire_type_id               | Equip-skill roll pool; 0 = none. Pets key into [petequipskillaquire.dbss](petequipskillaquire_dbss.md), fairies (501 to 504) into [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md) |
| `icon_path+0x26` | u16      | base_skill_id                 | The pet's base skill, a Section 2 `equip_skill_id` of [petequipskill.bss](petequipskill_bss.md) on all 2,009 records |
| `icon_path+0x28` | u16      | unknown_tail_28               | `0` in every record                                                                     |
| `icon_path+0x2A` | i32[10]  | action_rates                  | One millionths rate per pet action, see below                                           |
| `icon_path+0x52` | u8       | pet_type                      | `1` on the 21 fairy records, else `0`                                                   |
| `icon_path+0x53` | u16      | loot_skill_id                 | Key into [petskill.dbss](petskill_dbss.md): 11, 16 or 17 on 1,908 records; the pet window's "Basic" skill |
| `icon_path+0x55` | u16      | race_skill_id                 | Key into [petskill.dbss](petskill_dbss.md); the pet window's "Special" skill            |
| `icon_path+0x57` | u8       | unknown_57                    | `0` on 85 records, see Open Questions                                                   |
| `icon_path+0x58` | u8       | is_joker_pet_use              | `1` on 1,974 records                                                                    |
| `icon_path+0x59` | u8       | pc_room_type                  | `1` on 20 records, two each of ten species                                              |
| `icon_path+0x5A` | bytes[4] | unknown_tail_5a               | `0` in every record                                                                     |

The icon path is stored immediately after the fixed header, in ASCII.
**Not** null-terminated. Footer offsets are relative to the byte immediately
following the icon path. `unknown_57` keeps the name of its footer offset.

```text
New_UI_Common_forLua\Window\Stable\Pet\GoldStar_Pet_0004.dds
```

`exp_key` follows the tier on most pets (tier 0 has key 1, tier 1 key 2, tier 2 key 3, tiers 3 and 4 key 4). 138 records do not: key 4 on 55 tier-2 and 18 tier-1 records, key 2 on 54 tier-0 and 4 tier-2 records, key 3 on 7 tier-1 records.

Earlier versions of this doc read `exp_key` as `equip_skill_slots`, `is_indexed` as `unknown_10` (a u16 at `+0x10` that was `256` when set), `default_action_index` as `unknown_12` and `change_look_key` as `unknown_14` (a u32 at `+0x14`, `change_look_key << 16`). `max_level` was a u8, and the bytes of `max_hunger` read as `0x90000000` at `+0x08` and a constant `1` at `+0x0C`.

The ten `action_rates` follow the sheet's `Action_0` to `Action_9`, whose Korean comments name the actions: joy, feed, angry, sleepy, run, sit, play, crouch, cry and sulk. 1,642 of the 1,782 records before the 2026-09-27 update store ten times 1,000,000 and 96 store ten zeros; the rest mix 0 and 1,000,000 or carry smaller values such as 220,000, 100,000 and 40,000.

Earlier versions of this doc called the market fields and `skill_max_count` `unknown_00` (six `const_*` fields before that), `action_rates` `unknown_2a` (`upgrade_table` before that), `loot_skill_id` `unknown_53` (`tier_score`) and `base_skill_id` `equip_skill_id`. `pet_type`, `race_skill_id` and the two flags after `unknown_57` were listed as constant bytes.

### `petoffset.dbss`

Provides O(1) lookup of any pet record by `pet_id`. Records are **not** stored in file order; use the offset to locate any record.

| Offset  | Type              | Field | Notes                       |
| ------- | ----------------- | ----- | --------------------------- |
| `+0x00` | u32               | count | Must equal `pet.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row              |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                           |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id      | Matches `pet_id` in the main record                                             |
| `+0x02` | u32  | data_offset | Absolute byte offset in `pet.dbss` to the **data** (past the 2-byte key prefix) |
| `+0x06` | u16  | data_size   | Size of data in bytes (excluding the 2-byte key prefix)                         |
| `+0x08` | u16  | unknown_08  | Always 0                                                                        |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix in the file.  
`total_record_size = data_size + 2`.  
The parser reads `data_size` and `unknown_08` as one u32 (`parse_bare_offset_rows()`).

## Notes

- Total file size = 4 + Σ(2 + `data_size`) over all records: 332,420 bytes for the 1,782 records before the 2026-09-27 client update, 376,078 bytes for 2,009 records after it.
- Record size varies because `icon_path_len` differs per pet (observed: 55–68 bytes). The 32-byte header and 94-byte footer are fixed; only the path varies.
- `pet_id` appears three times per record: as the 2-byte key prefix in the file, as field `+0x00` in the data header, and as the `pet_id` field in the `petoffset.dbss` index.
- English pet display names resolve from `languagedata_en.loc` with `str_type = 6` and `str_id1 = pet_id`.
- The fairy records are species 25 (Laila, 20 records, `exp_key` 6 to 9 by grade) and one "Fairy's Energy" record of species 100. They are the 21 records with `pet_type` 1 and the 21 with `acquire_type_id` 501 to 504, which have no row in `petequipskillaquire.dbss`.
- `acquire_type_id` values 301–304 appear for regular pets and correspond to tiers 0–4 (tier 0 → 301, tier 4 → 304); lower values (1, 2, 3, 4) and mid-range values (101–104, 201–204, 401–404) appear for specific sub-groups.
- 21 records have no `petgrade.dbss` row for their `(species, variant)` and show no grade.
- [`petleaderbuff.bss`](petleaderbuff_bss.md) is keyed by `tier`: tier `4` (Tier 5 in the game) holds the alpha pet's loot cooldown cut.
- [`petupgrade.bss`](petupgrade_bss.md) is keyed by `tier` too: tier `3` (Tier 4) holds the Tier 5 Pet Training item.

## Field Names

The names follow the `Pet_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (keyed by `CharacterKey`), which shares 1,264 records with client 3473, and the 2016 `gc::PetStaticStatus` member order: `_maxLevel`, `_maxHungry`, `_petExpKey`, `_isIndexed`, `_defaultActionIndex`, `_changeLookKey`, `_iconPath`, `_basePriceForPetMarket`, `_minPriceForPetMarket`, `_maxPriceForPetMarket`, `_minestPricePercent`, `_maxestPricePercent`, `_skillMaxCount`, `_skillList[2]`, `_learnAttractList[10]`, `_petEquipSkillAquireKey`. In the 2016 struct the four bytes at `+0x02` are one u32 `_fusionKey`: `variant`, `species`, a zero byte and `tier`.

| Column | Field | Equal (non-zero rows) |
| ------ | ----- | --------------------- |
| `Kind` (Korean comment "body type") | `variant` | 1,264 of 1,264 |
| `Race` ("race") | `species` | 1,262 of 1,264 |
| `Tier` ("grade") | `tier` | 1,023 of 1,023 |
| `Level` | `max_level` | 1,259 of 1,264 |
| `Hunger` | `max_hunger` | `400` on every sheet row and record |
| `RequireEXPType` | `exp_key` | 1,264 of 1,264 |
| `IsIndexed` | `is_indexed` | 285 of 285 |
| `DefaultActionIndex` ("appearance") | `default_action_index` | 1,249 of 1,249 |
| `PetChangeLookKey` | `change_look_key` | 956 of 956 |
| `basePriceForPetMarket`, `minestPercentForPetMarket`, `maxestPercentForPetMarket` | the market fields | `30000`, `500000` and `1000000` on every sheet row and record |
| `EquipSkillAquireKey` ("skill group") | `acquire_type_id` | 986 of 986 |
| `BaseSkill` ("base skill") | `base_skill_id` | 1,264 of 1,264 |
| `Action_0` to `Action_9` | `action_rates` | 1,168 of 1,168 to 1,187 of 1,187 per column |
| `PetType` | `pet_type` | 21 of 21 |
| `Skill_0` ("looting") | `loot_skill_id` | 1,221 of 1,264 |
| `Skill_1` ("race skill") | `race_skill_id` | 1,264 of 1,264 |
| `IsJokerPetUse` | `is_joker_pet_use` | 1,236 of 1,236 |
| `PcRoomType` | `pc_room_type` | 10 of 10 |

`BaseSkill` keys the `Pet_BaseSkill_Table` sheet, whose 60 rows match Section 2 of `petequipskill.bss` by skill number (60 of 60); `Pet_EquipSkill_Table` matches Section 1 (43 of 43). The sheet's `EquipSkill_0` to `EquipSkill_14` and `BoneScale` columns have no field in the record. The derived min and max prices are not sheet columns; the 2016 member order places them.

## Open Questions

### `unknown_57` Meaning

The u8 at footer `+0x57` is `0` on every record of species 4 (Penguin), 21 (Kuku), 39 (Young Crimson Dragon), 40 (Young Fogan), 46 (Arctic Fox, Black Leopard, Prankkebi, Tarkhes) and 49 (Jojo, Putrakium), 85 records on client 3473, and `1` on the rest. It sits between `race_skill_id` and `is_joker_pet_use`, where the sheet has no column. The private server's own `pet.dbss` (client 1784) stores the same byte with the same split by species, so it is filled from a source outside `Pet_Table`.
