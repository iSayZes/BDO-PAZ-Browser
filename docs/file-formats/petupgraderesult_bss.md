# `petupgraderesult.bss` Format

## Purpose

The outcome of Tier 5 Pet Training per pet: which Tier 5 pet a Tier 4 pet
trains into, and the talent (base skill) the pet shows while it is the
alpha. The file holds two maps with no PABR magic and no trailer: Tier 4
pet to result, then Tier 5 pet to alpha talent. Pet keys are `pet_id`s of
[`pet.dbss`](pet_dbss.md); talents are Section 2 `equip_skill_id`s of
[`petequipskill.bss`](petequipskill_bss.md), the keys `pet.dbss` stores as
`base_skill_id`. The training cost is in [`petupgrade.bss`](petupgrade_bss.md)
and the alpha's loot cooldown bonus in
[`petleaderbuff.bss`](petleaderbuff_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ---------------------------- | --------- |
| 1      | 1927 and later | 3483    | `petupgraderesult.bss` | 7,112 | 444 Result, 444 Leader Skill | 10        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `petupgraderesult.bss` | 7,112 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `eb85c771b439`  |
| 3482   | Layout 1 | `eb85c771b439`  |
| 3474   | Layout 1 | `eb85c771b439`  |
| 3473   | Layout 1 | `eb85c771b439`  |
| 3464   | Layout 1 | `eb85c771b439`  |
| 3458   | Layout 1 | `eb85c771b439`  |
| 3454   | Layout 1 | `eb85c771b439`  |
| 3444   | Layout 1 | `eb85c771b439`  |
| 3435   | Layout 1 | `eb85c771b439`  |
| 3426   | Layout 1 | `eb85c771b439`  |
| 3418   | Layout 1 | `eb85c771b439`  |
| 3412   | Layout 1 | `eb85c771b439`  |
| 3402   | Layout 1 | `eb85c771b439`  |
| 3396   | Layout 1 | `eb85c771b439`  |
| 3387   | Layout 1 | `eb85c771b439`  |
| 3381   | Layout 1 | `eb85c771b439`  |
| 3373   | Layout 1 | `eb85c771b439`  |
| 3364   | Layout 1 | `eb85c771b439`  |
| 3356   | Layout 1 | `eb85c771b439`  |
| 3349   | Layout 1 | `eb85c771b439`  |
| 3342   | Layout 1 | `eb85c771b439`  |
| 3335   | Layout 1 | `eb85c771b439`  |
| 3326   | Layout 1 | `eb85c771b439`  |
| 3321   | Layout 1 | `eb85c771b439`  |
| 3314   | Layout 1 | `eb85c771b439`  |
| 3303   | Layout 1 | `eb85c771b439`  |
| 3302   | Layout 1 | `eb85c771b439`  |
| 3293   | Layout 1 | `eb85c771b439`  |
| 3283   | Layout 1 | `eb85c771b439`  |
| 3275   | Layout 1 | `eb85c771b439`  |
| 3267   | Layout 1 | `eb85c771b439`  |
| 3258   | Layout 1 | `eb85c771b439`  |
| 3251   | Layout 1 | `eb85c771b439`  |
| 3242   | Layout 1 | `eb85c771b439`  |
| 3235   | Layout 1 | `eb85c771b439`  |
| 3229   | Layout 1 | `eb85c771b439`  |
| 3212   | Layout 1 | `eb85c771b439`  |
| 3203   | Layout 1 | `eb85c771b439`  |
| 3193   | Layout 1 | `eb85c771b439`  |
| 3186   | Layout 1 | `eb85c771b439`  |
| 3177   | Layout 1 | `eb85c771b439`  |
| 3169   | Layout 1 | `eb85c771b439`  |
| 3158   | Layout 1 | `eb85c771b439`  |
| 3151   | Layout 1 | `eb85c771b439`  |
| 3144   | Layout 1 | `eb85c771b439`  |
| 3133   | Layout 1 | `eb85c771b439`  |
| 3125   | Layout 1 | `eb85c771b439`  |
| 3118   | Layout 1 | `eb85c771b439`  |
| 3111   | Layout 1 | `eb85c771b439`  |
| 3103   | Layout 1 | `eb85c771b439`  |
| 3095   | Layout 1 | `eb85c771b439`  |
| 3086   | Layout 1 | `eb85c771b439`  |
| 3072   | Layout 1 | `eb85c771b439`  |
| 3062   | Layout 1 | `eb85c771b439`  |
| 3052   | Layout 1 | `eb85c771b439`  |
| 3045   | Layout 1 | `eb85c771b439`  |
| 3037   | Layout 1 | `eb85c771b439`  |
| 3030   | Layout 1 | `eb85c771b439`  |
| 3021   | Layout 1 | `eb85c771b439`  |
| 3012   | Layout 1 | `eb85c771b439`  |
| 3002   | Layout 1 | `eb85c771b439`  |
| 2995   | Layout 1 | `eb85c771b439`  |
| 2987   | Layout 1 | `eb85c771b439`  |
| 2978   | Layout 1 | `eb85c771b439`  |
| 2970   | Layout 1 | `eb85c771b439`  |
| 2959   | Layout 1 | `eb85c771b439`  |
| 2951   | Layout 1 | `eb85c771b439`  |
| 2942   | Layout 1 | `eb85c771b439`  |
| 2935   | Layout 1 | `eb85c771b439`  |
| 2932   | Layout 1 | `eb85c771b439`  |
| 2923   | Layout 1 | `eb85c771b439`  |
| 2919   | Layout 1 | `eb85c771b439`  |
| 2907   | Layout 1 | `eb85c771b439`  |
| 2900   | Layout 1 | `eb85c771b439`  |
| 2891   | Layout 1 | `eb85c771b439`  |
| 2882   | Layout 1 | `eb85c771b439`  |
| 2872   | Layout 1 | `eb85c771b439`  |
| 2863   | Layout 1 | `eb85c771b439`  |
| 2855   | Layout 1 | `eb85c771b439`  |
| 2849   | Layout 1 | `eb85c771b439`  |
| 2844   | Layout 1 | `eb85c771b439`  |
| 2834   | Layout 1 | `eb85c771b439`  |
| 2825   | Layout 1 | `eb85c771b439`  |
| 2819   | Layout 1 | `eb85c771b439`  |
| 2811   | Layout 1 | `eb85c771b439`  |
| 2803   | Layout 1 | `eb85c771b439`  |
| 2794   | Layout 1 | `eb85c771b439`  |
| 2783   | Layout 1 | `eb85c771b439`  |
| 2774   | Layout 1 | `eb85c771b439`  |
| 2765   | Layout 1 | `eb85c771b439`  |
| 2756   | Layout 1 | `eb85c771b439`  |
| 2750   | Layout 1 | `eb85c771b439`  |
| 2743   | Layout 1 | `eb85c771b439`  |
| 2736   | Layout 1 | `eb85c771b439`  |
| 2726   | Layout 1 | `eb85c771b439`  |
| 2717   | Layout 1 | `eb85c771b439`  |
| 2709   | Layout 1 | `eb85c771b439`  |
| 2703   | Layout 1 | `eb85c771b439`  |
| 2695   | Layout 1 | `eb85c771b439`  |
| 2684   | Layout 1 | `eb85c771b439`  |
| 2672   | Layout 1 | `eb85c771b439`  |
| 2665   | Layout 1 | `eb85c771b439`  |
| 2657   | Layout 1 | `eb85c771b439`  |
| 2649   | Layout 1 | `eb85c771b439`  |
| 2644   | Layout 1 | `eb85c771b439`  |
| 2637   | Layout 1 | `eb85c771b439`  |
| 2629   | Layout 1 | `eb85c771b439`  |
| 2619   | Layout 1 | `eb85c771b439`  |
| 2612   | Layout 1 | `eb85c771b439`  |
| 2606   | Layout 1 | `eb85c771b439`  |
| 2602   | Layout 1 | `eb85c771b439`  |
| 2601   | Layout 1 | `eb85c771b439`  |
| 2592   | Layout 1 | `eb85c771b439`  |
| 2583   | Layout 1 | `eb85c771b439`  |
| 2575   | Layout 1 | `eb85c771b439`  |
| 2567   | Layout 1 | `eb85c771b439`  |
| 2560   | Layout 1 | `eb85c771b439`  |
| 2553   | Layout 1 | `eb85c771b439`  |
| 2545   | Layout 1 | `eb85c771b439`  |
| 2538   | Layout 1 | `eb85c771b439`  |
| 2529   | Layout 1 | `eb85c771b439`  |
| 2519   | Layout 1 | `eb85c771b439`  |
| 2513   | Layout 1 | `eb85c771b439`  |
| 2510   | Layout 1 | `eb85c771b439`  |
| 2507   | Layout 1 | `eb85c771b439`  |
| 2503   | Layout 1 | `eb85c771b439`  |
| 2498   | Layout 1 | `eb85c771b439`  |
| 2492   | Layout 1 | `eb85c771b439`  |
| 2487   | Layout 1 | `eb85c771b439`  |
| 2480   | Layout 1 | `eb85c771b439`  |
| 2474   | Layout 1 | `eb85c771b439`  |
| 2468   | Layout 1 | `eb85c771b439`  |
| 2460   | Layout 1 | `eb85c771b439`  |
| 2453   | Layout 1 | `eb85c771b439`  |
| 2444   | Layout 1 | `eb85c771b439`  |
| 2438   | Layout 1 | `eb85c771b439`  |
| 2434   | Layout 1 | `eb85c771b439`  |
| 2429   | Layout 1 | `eb85c771b439`  |
| 2421   | Layout 1 | `eb85c771b439`  |
| 2414   | Layout 1 | `eb85c771b439`  |
| 2407   | Layout 1 | `eb85c771b439`  |
| 2401   | Layout 1 | `eb85c771b439`  |
| 2397   | Layout 1 | `eb85c771b439`  |
| 2393   | Layout 1 | `eb85c771b439`  |
| 2384   | Layout 1 | `eb85c771b439`  |
| 2378   | Layout 1 | `eb85c771b439`  |
| 2372   | Layout 1 | `eb85c771b439`  |
| 2358   | Layout 1 | `eb85c771b439`  |
| 2352   | Layout 1 | `eb85c771b439`  |
| 2347   | Layout 1 | `eb85c771b439`  |
| 2343   | Layout 1 | `eb85c771b439`  |
| 2335   | Layout 1 | `eb85c771b439`  |
| 2327   | Layout 1 | `eb85c771b439`  |
| 2324   | Layout 1 | `eb85c771b439`  |
| 2319   | Layout 1 | `eb85c771b439`  |
| 2313   | Layout 1 | `eb85c771b439`  |
| 2308   | Layout 1 | `eb85c771b439`  |
| 2302   | Layout 1 | `eb85c771b439`  |
| 2295   | Layout 1 | `eb85c771b439`  |
| 2290   | Layout 1 | `eb85c771b439`  |
| 2284   | Layout 1 | `eb85c771b439`  |
| 2276   | Layout 1 | `eb85c771b439`  |
| 2269   | Layout 1 | `eb85c771b439`  |
| 2259   | Layout 1 | `eb85c771b439`  |
| 2250   | Layout 1 | `eb85c771b439`  |
| 2243   | Layout 1 | `eb85c771b439`  |
| 2235   | Layout 1 | `eb85c771b439`  |
| 2229   | Layout 1 | `eb85c771b439`  |
| 2224   | Layout 1 | `eb85c771b439`  |
| 2218   | Layout 1 | `eb85c771b439`  |
| 2215   | Layout 1 | `eb85c771b439`  |
| 2207   | Layout 1 | `eb85c771b439`  |
| 2203   | Layout 1 | `eb85c771b439`  |
| 2196   | Layout 1 | `eb85c771b439`  |
| 2192   | Layout 1 | `eb85c771b439`  |
| 2189   | Layout 1 | `eb85c771b439`  |
| 2183   | Layout 1 | `eb85c771b439`  |
| 2179   | Layout 1 | `eb85c771b439`  |
| 2171   | Layout 1 | `eb85c771b439`  |
| 2163   | Layout 1 | `eb85c771b439`  |
| 2156   | Layout 1 | `eb85c771b439`  |
| 2151   | Layout 1 | `eb85c771b439`  |
| 2147   | Layout 1 | `eb85c771b439`  |
| 2142   | Layout 1 | `eb85c771b439`  |
| 2138   | Layout 1 | `eb85c771b439`  |
| 2134   | Layout 1 | `eb85c771b439`  |
| 2130   | Layout 1 | `eb85c771b439`  |
| 2122   | Layout 1 | `eb85c771b439`  |
| 2107   | Layout 1 | `eb85c771b439`  |
| 2098   | Layout 1 | `eb85c771b439`  |
| 2089   | Layout 1 | `eb85c771b439`  |
| 2081   | Layout 1 | `eb85c771b439`  |
| 2073   | Layout 1 | `eb85c771b439`  |
| 2067   | Layout 1 | `eb85c771b439`  |
| 2063   | Layout 1 | `eb85c771b439`  |
| 2059   | Layout 1 | `eb85c771b439`  |
| 2052   | Layout 1 | `eb85c771b439`  |
| 2044   | Layout 1 | `eb85c771b439`  |
| 2039   | Layout 1 | `eb85c771b439`  |
| 2032   | Layout 1 | `eb85c771b439`  |
| 2025   | Layout 1 | `eb85c771b439`  |
| 2011   | Layout 1 | `eb85c771b439`  |
| 2005   | Layout 1 | `eb85c771b439`  |
| 2000   | Layout 1 | `eb85c771b439`  |
| 1996   | Layout 1 | `eb85c771b439`  |
| 1991   | Layout 1 | `eb85c771b439`  |
| 1985   | Layout 1 | `eb85c771b439`  |
| 1980   | Layout 1 | `eb85c771b439`  |
| 1969   | Layout 1 | `eb85c771b439`  |
| 1964   | Layout 1 | `eb85c771b439`  |
| 1958   | Layout 1 | `eb85c771b439`  |
| 1950   | Layout 1 | `eb85c771b439`  |
| 1945   | Layout 1 | `eb85c771b439`  |
| 1937   | Layout 1 | `eb85c771b439`  |
| 1933   | Layout 1 | `eb85c771b439`  |
| 1927   | Layout 1 | `eb85c771b439`  |
| 1921   | No file  | `eb85c771b439`  |
| 1914   | No file  | `eb85c771b439`  |
| 1908   | No file  | `eb85c771b439`  |
| 1897   | No file  | `eb85c771b439`  |
| 1892   | No file  | `eb85c771b439`  |
| 1886   | No file  | `eb85c771b439`  |
| 1881   | No file  | `eb85c771b439`  |
| 1871   | No file  | `eb85c771b439`  |
| 1866   | No file  | `eb85c771b439`  |
| 1862   | No file  | `eb85c771b439`  |
| 1854   | No file  | `eb85c771b439`  |
| 1846   | No file  | `eb85c771b439`  |
| 1838   | No file  | `eb85c771b439`  |
| 1832   | No file  | `eb85c771b439`  |
| 1826   | No file  | `eb85c771b439`  |
| 1822   | No file  | `eb85c771b439`  |
| 1818   | No file  | `eb85c771b439`  |
| 1804   | No file  | `eb85c771b439`  |
| 1794   | No file  | `eb85c771b439`  |
| 1790   | No file  | `eb85c771b439`  |
| 1784   | No file  | `eb85c771b439`  |
| 1774   | No file  | `eb85c771b439`  |
| 1771   | No file  | `eb85c771b439`  |
| 1762   | No file  | `eb85c771b439`  |
| 1759   | No file  | `eb85c771b439`  |
| 1754   | No file  | `eb85c771b439`  |
| 1749   | No file  | `eb85c771b439`  |
| 1743   | No file  | `eb85c771b439`  |
| 1737   | No file  | `eb85c771b439`  |
| 1731   | No file  | `eb85c771b439`  |
| 1725   | No file  | `eb85c771b439`  |
| 1717   | No file  | `eb85c771b439`  |
| 1710   | No file  | `eb85c771b439`  |
| 1704   | No file  | `eb85c771b439`  |
| 1698   | No file  | `eb85c771b439`  |
| 1690   | No file  | `eb85c771b439`  |
| 1685   | No file  | `eb85c771b439`  |
| 1680   | No file  | `eb85c771b439`  |
| 1674   | No file  | `eb85c771b439`  |
| 1668   | No file  | `eb85c771b439`  |
| 1659   | No file  | `eb85c771b439`  |
| 1649   | No file  | `eb85c771b439`  |
| 1642   | No file  | `eb85c771b439`  |
| 1636   | No file  | `eb85c771b439`  |
| 1628   | No file  | `eb85c771b439`  |
| 1622   | No file  | `eb85c771b439`  |
| 1614   | No file  | `eb85c771b439`  |
| 1608   | No file  | `eb85c771b439`  |
| 1602   | No file  | `eb85c771b439`  |
| 1598   | No file  | `eb85c771b439`  |
| 1594   | No file  | `eb85c771b439`  |
| 1590   | No file  | `eb85c771b439`  |
| 1587   | No file  | `eb85c771b439`  |
| 1584   | No file  | `eb85c771b439`  |
| 1579   | No file  | `eb85c771b439`  |
| 1572   | No file  | `eb85c771b439`  |
| 1565   | No file  | `eb85c771b439`  |
| 1559   | No file  | `eb85c771b439`  |
| 1554   | No file  | `eb85c771b439`  |
| 1547   | No file  | `eb85c771b439`  |
| 1537   | No file  | `eb85c771b439`  |
| 1529   | No file  | `eb85c771b439`  |
| 1524   | No file  | `eb85c771b439`  |
| 1519   | No file  | `eb85c771b439`  |
| 1509   | No file  | `eb85c771b439`  |
| 1506   | No file  | `eb85c771b439`  |
| 1504   | No file  | `eb85c771b439`  |
| 1500   | No file  | `eb85c771b439`  |
| 1493   | No file  | `eb85c771b439`  |
| 1489   | No file  | `eb85c771b439`  |
| 1485   | No file  | `eb85c771b439`  |
| 1481   | No file  | `eb85c771b439`  |
| 1474   | No file  | `eb85c771b439`  |
| 1466   | No file  | `eb85c771b439`  |
| 1462   | No file  | `eb85c771b439`  |
| 1459   | No file  | `eb85c771b439`  |
| 1453   | No file  | `eb85c771b439`  |
| 1450   | No file  | `eb85c771b439`  |
| 1445   | No file  | `eb85c771b439`  |
| 1439   | No file  | `eb85c771b439`  |
| 1433   | No file  | `eb85c771b439`  |
| 1430   | No file  | `eb85c771b439`  |
| 1426   | No file  | `eb85c771b439`  |
| 1421   | No file  | `eb85c771b439`  |
| 1417   | No file  | `eb85c771b439`  |
| 1416   | No file  | `eb85c771b439`  |
| 1409   | No file  | `eb85c771b439`  |
| 1405   | No file  | `eb85c771b439`  |
| 1401   | No file  | `eb85c771b439`  |
| 1396   | No file  | `eb85c771b439`  |
| 1391   | No file  | `eb85c771b439`  |
| 1390   | No file  | `eb85c771b439`  |
| 1386   | No file  | `eb85c771b439`  |
| 1381   | No file  | `eb85c771b439`  |
| 1379   | No file  | `eb85c771b439`  |
| 1372   | No file  | `eb85c771b439`  |
| 1366   | No file  | `eb85c771b439`  |
| 1364   | No file  | `eb85c771b439`  |
| 1363   | No file  | `eb85c771b439`  |
| 1360   | No file  | `eb85c771b439`  |
| 1358   | No file  | `eb85c771b439`  |
| 1355   | No file  | `eb85c771b439`  |
| 1351   | No file  | `eb85c771b439`  |
| 1348   | No file  | `eb85c771b439`  |
| 1346   | No file  | `eb85c771b439`  |
| 1341   | No file  | `eb85c771b439`  |
| 1340   | No file  | `eb85c771b439`  |
| 1338   | No file  | `eb85c771b439`  |
| 1335   | No file  | `eb85c771b439`  |
| 1333   | No file  | `eb85c771b439`  |
| 1329   | No file  | `eb85c771b439`  |
| 1327   | No file  | `eb85c771b439`  |
| 1324   | No file  | `eb85c771b439`  |
| 1321   | No file  | `eb85c771b439`  |
| 1319   | No file  | `eb85c771b439`  |
| 1318   | No file  | `eb85c771b439`  |
| 1316   | No file  | `eb85c771b439`  |
| 1313   | No file  | `eb85c771b439`  |
| 1311   | No file  | `eb85c771b439`  |
| 1309   | No file  | `eb85c771b439`  |
| 1304   | No file  | `eb85c771b439`  |
| 1292   | No file  | `eb85c771b439`  |
| 1286   | No file  | `eb85c771b439`  |
| 1280   | No file  | `eb85c771b439`  |
| 1276   | No file  | `eb85c771b439`  |
| 1267   | No file  | `eb85c771b439`  |
| 1261   | No file  | `eb85c771b439`  |
| 1256   | No file  | `eb85c771b439`  |
| 1250   | No file  | `eb85c771b439`  |
| 1246   | No file  | `eb85c771b439`  |
| 1239   | No file  | `eb85c771b439`  |
| 1230   | No file  | `eb85c771b439`  |
| 1226   | No file  | `eb85c771b439`  |
| 1220   | No file  | `eb85c771b439`  |
| 1217   | No file  | `eb85c771b439`  |
| 1211   | No file  | `eb85c771b439`  |
| 1210   | No file  | `eb85c771b439`  |
| 1208   | No file  | `eb85c771b439`  |
| 1203   | No file  | `eb85c771b439`  |
| 1197   | No file  | `eb85c771b439`  |
| 1194   | No file  | `eb85c771b439`  |
| 1192   | No file  | `eb85c771b439`  |
| 1187   | No file  | `eb85c771b439`  |
| 1183   | No file  | `eb85c771b439`  |
| 1177   | No file  | `eb85c771b439`  |
| 1173   | No file  | `eb85c771b439`  |
| 1167   | No file  | `eb85c771b439`  |
| 1164   | No file  | `eb85c771b439`  |
| 1156   | No file  | `eb85c771b439`  |
| 1149   | No file  | `eb85c771b439`  |
| 1144   | No file  | `eb85c771b439`  |
| 1137   | No file  | `eb85c771b439`  |
| 1132   | No file  | `eb85c771b439`  |
| 1127   | No file  | `eb85c771b439`  |
| 1122   | No file  | `eb85c771b439`  |
| 1118   | No file  | `eb85c771b439`  |
| 1114   | No file  | `eb85c771b439`  |
| 1109   | No file  | `eb85c771b439`  |
| 1102   | No file  | `eb85c771b439`  |
| 1096   | No file  | `eb85c771b439`  |
| 1088   | No file  | `eb85c771b439`  |
| 1081   | No file  | `eb85c771b439`  |
| 1076   | No file  | `eb85c771b439`  |
| 1069   | No file  | `eb85c771b439`  |
| 1064   | No file  | `eb85c771b439`  |
| 1058   | No file  | `eb85c771b439`  |
| 1051   | No file  | `eb85c771b439`  |
| 1044   | No file  | `eb85c771b439`  |
| 1036   | No file  | `eb85c771b439`  |
| 1026   | No file  | `eb85c771b439`  |
| 1016   | No file  | `eb85c771b439`  |
| 1009   | No file  | `eb85c771b439`  |
| 1005   | No file  | `eb85c771b439`  |
| 1000   | No file  | `eb85c771b439`  |
| 998    | No file  | `eb85c771b439`  |
| 990    | No file  | `eb85c771b439`  |
| 979    | No file  | `eb85c771b439`  |
| 972    | No file  | `eb85c771b439`  |
| 963    | No file  | `eb85c771b439`  |
| 955    | No file  | `eb85c771b439`  |
| 946    | No file  | `eb85c771b439`  |
| 938    | No file  | `eb85c771b439`  |
| 927    | No file  | `eb85c771b439`  |
| 911    | No file  | `eb85c771b439`  |
| 904    | No file  | `eb85c771b439`  |
| 899    | No file  | `eb85c771b439`  |
| 894    | No file  | `eb85c771b439`  |
| 885    | No file  | `eb85c771b439`  |
| 879    | No file  | `eb85c771b439`  |
| 872    | No file  | `eb85c771b439`  |
| 864    | No file  | `eb85c771b439`  |
| 855    | No file  | `eb85c771b439`  |
| 853    | No file  | `eb85c771b439`  |
| 845    | No file  | `eb85c771b439`  |
| 837    | No file  | `eb85c771b439`  |
| 829    | No file  | `eb85c771b439`  |
| 822    | No file  | `eb85c771b439`  |
| 814    | No file  | `eb85c771b439`  |
| 805    | No file  | `eb85c771b439`  |
| 794    | No file  | `eb85c771b439`  |
| 787    | No file  | `eb85c771b439`  |
| 780    | No file  | `eb85c771b439`  |
| 771    | No file  | `eb85c771b439`  |
| 760    | No file  | `eb85c771b439`  |
| 748    | No file  | `eb85c771b439`  |
| 741    | No file  | `eb85c771b439`  |
| 736    | No file  | `eb85c771b439`  |
| 731    | No file  | `eb85c771b439`  |
| 723    | No file  | `eb85c771b439`  |
| 711    | No file  | `eb85c771b439`  |
| 707    | No file  | `eb85c771b439`  |
| 697    | No file  | `eb85c771b439`  |
| 689    | No file  | `eb85c771b439`  |
| 683    | No file  | `eb85c771b439`  |
| 678    | No file  | `eb85c771b439`  |
| 670    | No file  | `eb85c771b439`  |
| 661    | No file  | `eb85c771b439`  |
| 656    | No file  | `eb85c771b439`  |
| 652    | No file  | `eb85c771b439`  |
| 643    | No file  | `eb85c771b439`  |
| 637    | No file  | `eb85c771b439`  |
| 630    | No file  | `eb85c771b439`  |
| 627    | No file  | `eb85c771b439`  |
| 621    | No file  | `eb85c771b439`  |
| 617    | No file  | `eb85c771b439`  |
| 615    | No file  | `eb85c771b439`  |
| 606    | No file  | `eb85c771b439`  |
| 599    | No file  | `eb85c771b439`  |
| 592    | No file  | `eb85c771b439`  |
| 586    | No file  | `eb85c771b439`  |
| 577    | No file  | `eb85c771b439`  |
| 569    | No file  | `eb85c771b439`  |
| 561    | No file  | `eb85c771b439`  |
| 554    | No file  | `eb85c771b439`  |
| 542    | No file  | `eb85c771b439`  |
| 532    | No file  | `eb85c771b439`  |
| 531    | No file  | `eb85c771b439`  |
| 526    | No file  | `eb85c771b439`  |
| 521    | No file  | `eb85c771b439`  |
| 517    | No file  | `eb85c771b439`  |
| 510    | No file  | `eb85c771b439`  |
| 508    | No file  | `eb85c771b439`  |
| 504    | No file  | `eb85c771b439`  |
| 497    | No file  | `eb85c771b439`  |
| 491    | No file  | `eb85c771b439`  |
| 485    | No file  | `eb85c771b439`  |
| 478    | No file  | `eb85c771b439`  |
| 472    | No file  | `eb85c771b439`  |
| 466    | No file  | `eb85c771b439`  |
| 457    | No file  | `eb85c771b439`  |
| 452    | No file  | `eb85c771b439`  |
| 449    | No file  | `eb85c771b439`  |
| 435    | No file  | `eb85c771b439`  |

<!-- versions:end -->

## Companion Files

None. The handler names the pets and the talents from
[`pet.dbss`](pet_dbss.md) (with `petoffset.dbss`) and
[`petequipskill.bss`](petequipskill_bss.md) when they are present.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset          | Type                          | Field              | Notes                                         |
| --------------- | ----------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`         | u32                           | result_count       | Number of Result rows                         |
| `+0x04`         | Result[result_count]          | results            | See Result                                    |
| `results+0x00`  | u32                           | leader_skill_count | Number of Leader Skill rows; equals `result_count` on client 3474 |
| `results+0x04`  | Leader Skill[leader_skill_count] | leader_skills   | See Leader Skill                              |

On client 3474 the file is 4 + 444 x 10 + 4 + 444 x 6 = 7,112 bytes.

### Result (10 bytes)

| Offset  | Type | Field                | Notes                                                                                     |
| ------- | ---- | -------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: the Tier 4 pet (`tier` `3` in [`pet.dbss`](pet_dbss.md))                         |
| `+0x02` | u16  | pet_id_dup           | Equals `pet_id` on every row                                                              |
| `+0x04` | u16  | result_pet_id        | The Tier 5 pet the training gives (`tier` `4` in `pet.dbss`)                              |
| `+0x06` | u32  | leader_base_skill_id | Talent of the trained pet as the alpha: a Section 2 `equip_skill_id` of [`petequipskill.bss`](petequipskill_bss.md) |

### Leader Skill (6 bytes)

| Offset  | Type | Field                | Notes                                                           |
| ------- | ---- | -------------------- | --------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: a Tier 5 pet, the `result_pet_id` of one Result row     |
| `+0x02` | u32  | leader_base_skill_id | Equals `leader_base_skill_id` of that Result row                 |

## Training Results

On client 3474 every Tier 4 pet of `pet.dbss` has a Result row except the
five fairy records (`pet_type` 1), and every Tier 5 pet is the
`result_pet_id` of exactly one row. 431 of the 444 rows give a pet with the
same LOC name; the other 13 give the Tier 5 record of the same pet where
the Tier 4 record has no LOC name (`아토락시온 타르케스_T4` to Tarkhes,
`반려동물 쪼쪼_교역_T4` to Jojo).

`leader_base_skill_id` is the talent one level above the Tier 4 pet's own
`base_skill_id`, keyed by that base skill on all 444 rows:

| Tier 4 `base_skill_id` | `leader_base_skill_id` | Talent as the alpha (LOC type 10) | Rows (client 3474) |
| ---------------------- | ---------------------- | --------------------------------- | ------------------ |
| 18                     | 99                     | Skill EXP +5%                     | 118                |
| 38                     | 101                    | Durability Reduction Resistance +5% | 100              |
| 23                     | 100                    | Life EXP +5%                      | 99                 |
| 58                     | 103                    | Weight Limit +60 LT               | 31                 |
| 43                     | 102                    | Normal and Higher Grade Gain Chance Lv. 5 | 30         |
| 78                     | 106                    | Death Penalty Resistance +5%      | 28                 |
| 73                     | 105                    | Combat EXP +5%                    | 24                 |
| 82                     | 107                    | Item Drop Rate +5%                | 5                  |
| 68                     | 104                    | Max HP +125                       | 5                  |
| 86                     | 108                    | Mount EXP +5%                     | 2                  |
| 98                     | 111                    | Big Ship Inventory Weight +250 LT | 1                  |
| 94                     | 110                    | Barter EXP +5%                    | 1                  |

The Tier 5 pet's own record in `pet.dbss` keeps the Tier 4 `base_skill_id`
on every row.

## Field Names

No reference source has the table: the file is not in the client 1784
archive, a private server's `DataSheets.bexcel` on client 1784 has no sheet
with `Upgrade` and `Pet` in its name, and the 2016 client's debug symbols
have no pet upgrade type. The names come from the client Lua of client
3474 and the official Black Desert wiki:

- `pet_id` and `result_pet_id`: the Tier 5 Pet Training window
  (`panel_dialog_petleader_all_1.luac`) calls
  `ToClient_getPetUpgradeSimulationResult(characterKey)` with the character
  key of the Tier 4 pet in the slot and reads the tier of the pet it
  returns (`newPetStaticStatus:getPetTier()`) for the alpha bonus. Every
  key of Result is a Tier 4 pet and every `result_pet_id` a Tier 5 one.
- `leader_base_skill_id`: the same window, the pet list
  (`panel_window_petlist_all_2.luac`) and the pet info window
  (`panel_window_petinfo_all_1.luac`) show the talent of an alpha pet with
  `ToClient_getPetBaseSkillStaticStatus(ToClient_getLeaderBaseSkill(petNo))`,
  and of any other pet with `getPetBaseSkillIndex()`. The official Black
  Desert wiki page "Tier 5 Pet Training/Alpha Appointment" says "The Alpha
  Pet's Talent gains one additional level", with the examples "Combat EXP
  +4% -> +5%" and "HP +100 -> +125", and that other Tier 5 pets "share the
  same stats as a Tier 4 pet". That is the step from `base_skill_id` to
  `leader_base_skill_id` in Training Results (`73` Combat EXP +5% and `104`
  Max HP +125).
- `pet_id_dup`: equal to the key on all 444 rows, as `plantupgradeparam.bss`
  stores its map key again as the first member of the value.

## Notes

- Clients 2107, 2519, 3002 and 3251 ship the file too; client 1784 does
  not.
- The rows of neither map are sorted by key, and the two maps
  list the pets in different orders.
- `ToClient_getLeaderBaseSkill` takes a pet number, not a key, so the Lua
  does not show which of the two maps it reads. The training window calls
  it for a Tier 4 pet (a Result key), the pet list for an alpha, which is a
  Tier 5 pet (a Leader Skill key).

## Open Questions

### Why the Second Map

Leader Skill repeats the talent of every Result row under the Tier 5 pet's
key. The client could look the talent up through either key; which call
reads which map is not in the client Lua, and the client 3474 executable
does not name the table's loader.
