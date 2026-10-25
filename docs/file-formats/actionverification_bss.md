# `actionverification.bss` Format

## Purpose

A list of actions per character: each character key holds action name
hashes, each with an `AbleCallTime` value. On client 3474 the file holds 14
characters and 150 actions. Five are the player classes Warrior (`1`),
Ranger (`2`), Sorcerer (`3`), Tamer (`5`) and Musa (`21`), with one action
each (`BT_WAIT`, `BT_skill_SkyFall`, `BT_skill_ThrustAndSmash_AttQ1`). The
other nine are the hero characters `65002` to `65037` (Jordine, Peony,
Ahon Kirus, Povios, Syaki, Nelydormin, Orwen, Striker, Tamer in LOC type 6),
with 12 to 23 `SHADOW_*` and `BT_ROLL_*` actions each. Each hero key is
`64950` plus one of the class types in
[`actionverificationindex.dbss`](actionverificationindex_dbss.md) (see
Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------------------------ | --------- |
| 2      | 1280 and later | `actionverification.bss` | 1,304 | 150 Action, 14 Character | 8         |
| 1      | 1220 to 1230   | `actionverification.bss` | 100   | 5 Row                    | 16        |

| Layout | File                     | Known            | Unknown      |
| ------ | ------------------------ | ---------------- | ------------ |
| 2      | `actionverification.bss` | 1,304 B (100.0%) | 0 B (0.0%)   |
| 1      | `actionverification.bss` | 60 B (60.0%)     | 40 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `7a6526c48435`  |
| 3482   | Layout 2             | `7a6526c48435`  |
| 3474   | Layout 2             | `7a6526c48435`  |
| 3473   | Layout 2             | `7a6526c48435`  |
| 3464   | Layout 2             | `7a6526c48435`  |
| 3458   | Layout 2             | `7a6526c48435`  |
| 3454   | Layout 2             | `7a6526c48435`  |
| 3444   | Layout 2             | `7a6526c48435`  |
| 3435   | Layout 2             | `7a6526c48435`  |
| 3426   | Layout 2             | `7a6526c48435`  |
| 3418   | Layout 2             | `7a6526c48435`  |
| 3412   | Layout 2             | `7a6526c48435`  |
| 3402   | Layout 2             | `7a6526c48435`  |
| 3396   | Layout 2             | `7a6526c48435`  |
| 3387   | Layout 2             | `7a6526c48435`  |
| 3381   | Layout 2             | `7a6526c48435`  |
| 3373   | Layout 2             | `7a6526c48435`  |
| 3364   | Layout 2             | `7a6526c48435`  |
| 3356   | Layout 2             | `7a6526c48435`  |
| 3349   | Layout 2             | `7a6526c48435`  |
| 3342   | Layout 2             | `7a6526c48435`  |
| 3335   | Layout 2             | `7a6526c48435`  |
| 3326   | Layout 2             | `7a6526c48435`  |
| 3321   | Layout 2             | `7a6526c48435`  |
| 3314   | Layout 2             | `7a6526c48435`  |
| 3303   | Layout 2             | `7a6526c48435`  |
| 3302   | Layout 2             | `7a6526c48435`  |
| 3293   | Layout 2             | `7a6526c48435`  |
| 3283   | Layout 2             | `7a6526c48435`  |
| 3275   | Layout 2             | `7a6526c48435`  |
| 3267   | Layout 2             | `7a6526c48435`  |
| 3258   | Layout 2             | `7a6526c48435`  |
| 3251   | Layout 2             | `7a6526c48435`  |
| 3242   | Layout 2             | `7a6526c48435`  |
| 3235   | Layout 2             | `7a6526c48435`  |
| 3229   | Layout 2             | `7a6526c48435`  |
| 3212   | Layout 2             | `7a6526c48435`  |
| 3203   | Layout 2             | `7a6526c48435`  |
| 3193   | Layout 2             | `7a6526c48435`  |
| 3186   | Layout 2             | `7a6526c48435`  |
| 3177   | Layout 2             | `7a6526c48435`  |
| 3169   | Layout 2             | `7a6526c48435`  |
| 3158   | Layout 2             | `7a6526c48435`  |
| 3151   | Layout 2             | `7a6526c48435`  |
| 3144   | Layout 2             | `7a6526c48435`  |
| 3133   | Layout 2             | `7a6526c48435`  |
| 3125   | Layout 2             | `7a6526c48435`  |
| 3118   | Layout 2             | `7a6526c48435`  |
| 3111   | Layout 2             | `7a6526c48435`  |
| 3103   | Layout 2             | `7a6526c48435`  |
| 3095   | Layout 2             | `7a6526c48435`  |
| 3086   | Layout 2             | `7a6526c48435`  |
| 3072   | Layout 2             | `7a6526c48435`  |
| 3062   | Layout 2             | `7a6526c48435`  |
| 3052   | Layout 2             | `7a6526c48435`  |
| 3045   | Layout 2             | `7a6526c48435`  |
| 3037   | Layout 2             | `7a6526c48435`  |
| 3030   | Layout 2             | `7a6526c48435`  |
| 3021   | Layout 2             | `7a6526c48435`  |
| 3012   | Layout 2             | `7a6526c48435`  |
| 3002   | Layout 2             | `7a6526c48435`  |
| 2995   | Layout 2             | `7a6526c48435`  |
| 2987   | Layout 2             | `7a6526c48435`  |
| 2978   | Layout 2             | `7a6526c48435`  |
| 2970   | Layout 2             | `7a6526c48435`  |
| 2959   | Layout 2             | `7a6526c48435`  |
| 2951   | Layout 2             | `7a6526c48435`  |
| 2942   | Layout 2             | `7a6526c48435`  |
| 2935   | Layout 2             | `7a6526c48435`  |
| 2932   | Layout 2             | `7a6526c48435`  |
| 2923   | Layout 2             | `7a6526c48435`  |
| 2919   | Layout 2             | `7a6526c48435`  |
| 2907   | Layout 2             | `7a6526c48435`  |
| 2900   | Layout 2             | `7a6526c48435`  |
| 2891   | Layout 2             | `7a6526c48435`  |
| 2882   | Layout 2             | `7a6526c48435`  |
| 2872   | Layout 2             | `7a6526c48435`  |
| 2863   | Layout 2             | `7a6526c48435`  |
| 2855   | Layout 2             | `7a6526c48435`  |
| 2849   | Layout 2             | `7a6526c48435`  |
| 2844   | Layout 2             | `7a6526c48435`  |
| 2834   | Layout 2             | `7a6526c48435`  |
| 2825   | Layout 2             | `7a6526c48435`  |
| 2819   | Layout 2             | `7a6526c48435`  |
| 2811   | Layout 2             | `7a6526c48435`  |
| 2803   | Layout 2             | `7a6526c48435`  |
| 2794   | Layout 2             | `7a6526c48435`  |
| 2783   | Layout 2             | `7a6526c48435`  |
| 2774   | Layout 2             | `7a6526c48435`  |
| 2765   | Layout 2             | `7a6526c48435`  |
| 2756   | Layout 2             | `7a6526c48435`  |
| 2750   | Layout 2             | `7a6526c48435`  |
| 2743   | Layout 2             | `7a6526c48435`  |
| 2736   | Layout 2             | `7a6526c48435`  |
| 2726   | Layout 2             | `7a6526c48435`  |
| 2717   | Layout 2             | `7a6526c48435`  |
| 2709   | Layout 2             | `7a6526c48435`  |
| 2703   | Layout 2             | `7a6526c48435`  |
| 2695   | Layout 2             | `7a6526c48435`  |
| 2684   | Layout 2             | `7a6526c48435`  |
| 2672   | Layout 2             | `7a6526c48435`  |
| 2665   | Layout 2             | `7a6526c48435`  |
| 2657   | Layout 2             | `7a6526c48435`  |
| 2649   | Layout 2             | `7a6526c48435`  |
| 2644   | Layout 2             | `7a6526c48435`  |
| 2637   | Layout 2             | `7a6526c48435`  |
| 2629   | Layout 2             | `7a6526c48435`  |
| 2619   | Layout 2             | `7a6526c48435`  |
| 2612   | Layout 2             | `7a6526c48435`  |
| 2606   | Layout 2             | `7a6526c48435`  |
| 2602   | Layout 2             | `7a6526c48435`  |
| 2601   | Layout 2             | `7a6526c48435`  |
| 2592   | Layout 2             | `7a6526c48435`  |
| 2583   | Layout 2             | `7a6526c48435`  |
| 2575   | Layout 2             | `7a6526c48435`  |
| 2567   | Layout 2             | `7a6526c48435`  |
| 2560   | Layout 2             | `7a6526c48435`  |
| 2553   | Layout 2             | `7a6526c48435`  |
| 2545   | Layout 2             | `7a6526c48435`  |
| 2538   | Layout 2             | `7a6526c48435`  |
| 2529   | Layout 2             | `7a6526c48435`  |
| 2519   | Layout 2             | `7a6526c48435`  |
| 2513   | Layout 2             | `7a6526c48435`  |
| 2510   | Layout 2             | `7a6526c48435`  |
| 2507   | Layout 2             | `7a6526c48435`  |
| 2503   | Layout 2             | `7a6526c48435`  |
| 2498   | Layout 2             | `7a6526c48435`  |
| 2492   | Layout 2             | `7a6526c48435`  |
| 2487   | Layout 2             | `7a6526c48435`  |
| 2480   | Layout 2             | `7a6526c48435`  |
| 2474   | Layout 2             | `7a6526c48435`  |
| 2468   | Layout 2             | `7a6526c48435`  |
| 2460   | Layout 2             | `7a6526c48435`  |
| 2453   | Layout 2             | `7a6526c48435`  |
| 2444   | Layout 2             | `7a6526c48435`  |
| 2438   | Layout 2             | `7a6526c48435`  |
| 2434   | Layout 2             | `7a6526c48435`  |
| 2429   | Layout 2             | `7a6526c48435`  |
| 2421   | Layout 2             | `7a6526c48435`  |
| 2414   | Layout 2             | `7a6526c48435`  |
| 2407   | Layout 2             | `7a6526c48435`  |
| 2401   | Layout 2             | `7a6526c48435`  |
| 2397   | Layout 2             | `7a6526c48435`  |
| 2393   | Layout 2             | `7a6526c48435`  |
| 2384   | Layout 2             | `7a6526c48435`  |
| 2378   | Layout 2             | `7a6526c48435`  |
| 2372   | Layout 2             | `7a6526c48435`  |
| 2358   | Layout 2             | `7a6526c48435`  |
| 2352   | Layout 2             | `7a6526c48435`  |
| 2347   | Layout 2             | `7a6526c48435`  |
| 2343   | Layout 2             | `7a6526c48435`  |
| 2335   | Layout 2             | `7a6526c48435`  |
| 2327   | Layout 2             | `7a6526c48435`  |
| 2324   | Layout 2             | `7a6526c48435`  |
| 2319   | Layout 2             | `7a6526c48435`  |
| 2313   | Layout 2             | `7a6526c48435`  |
| 2308   | Layout 2             | `7a6526c48435`  |
| 2302   | Layout 2             | `7a6526c48435`  |
| 2295   | Layout 2             | `7a6526c48435`  |
| 2290   | Layout 2             | `7a6526c48435`  |
| 2284   | Layout 2             | `7a6526c48435`  |
| 2276   | Layout 2             | `7a6526c48435`  |
| 2269   | Layout 2             | `7a6526c48435`  |
| 2259   | Layout 2             | `7a6526c48435`  |
| 2250   | Layout 2             | `7a6526c48435`  |
| 2243   | Layout 2             | `7a6526c48435`  |
| 2235   | Layout 2             | `7a6526c48435`  |
| 2229   | Layout 2             | `7a6526c48435`  |
| 2224   | Layout 2             | `7a6526c48435`  |
| 2218   | Layout 2             | `7a6526c48435`  |
| 2215   | Layout 2             | `7a6526c48435`  |
| 2207   | Layout 2             | `7a6526c48435`  |
| 2203   | Layout 2             | `7a6526c48435`  |
| 2196   | Layout 2             | `7a6526c48435`  |
| 2192   | Layout 2             | `7a6526c48435`  |
| 2189   | Layout 2             | `7a6526c48435`  |
| 2183   | Layout 2             | `7a6526c48435`  |
| 2179   | Layout 2             | `7a6526c48435`  |
| 2171   | Layout 2             | `7a6526c48435`  |
| 2163   | Layout 2             | `7a6526c48435`  |
| 2156   | Layout 2             | `7a6526c48435`  |
| 2151   | Layout 2             | `7a6526c48435`  |
| 2147   | Layout 2             | `7a6526c48435`  |
| 2142   | Layout 2             | `7a6526c48435`  |
| 2138   | Layout 2             | `7a6526c48435`  |
| 2134   | Layout 2             | `7a6526c48435`  |
| 2130   | Layout 2             | `7a6526c48435`  |
| 2122   | Layout 2             | `7a6526c48435`  |
| 2107   | Layout 2             | `7a6526c48435`  |
| 2098   | Layout 2             | `7a6526c48435`  |
| 2089   | Layout 2             | `7a6526c48435`  |
| 2081   | Layout 2             | `7a6526c48435`  |
| 2073   | Layout 2             | `7a6526c48435`  |
| 2067   | Layout 2             | `7a6526c48435`  |
| 2063   | Layout 2             | `7a6526c48435`  |
| 2059   | Layout 2             | `7a6526c48435`  |
| 2052   | Layout 2             | `7a6526c48435`  |
| 2044   | Layout 2             | `7a6526c48435`  |
| 2039   | Layout 2             | `7a6526c48435`  |
| 2032   | Layout 2             | `7a6526c48435`  |
| 2025   | Layout 2             | `7a6526c48435`  |
| 2011   | Layout 2             | `7a6526c48435`  |
| 2005   | Layout 2             | `7a6526c48435`  |
| 2000   | Layout 2             | `7a6526c48435`  |
| 1996   | Layout 2             | `7a6526c48435`  |
| 1991   | Layout 2             | `7a6526c48435`  |
| 1985   | Layout 2             | `7a6526c48435`  |
| 1980   | Layout 2             | `7a6526c48435`  |
| 1969   | Layout 2             | `7a6526c48435`  |
| 1964   | Layout 2             | `7a6526c48435`  |
| 1958   | Layout 2             | `7a6526c48435`  |
| 1950   | Layout 2             | `7a6526c48435`  |
| 1945   | Layout 2             | `7a6526c48435`  |
| 1937   | Layout 2             | `7a6526c48435`  |
| 1933   | Layout 2             | `7a6526c48435`  |
| 1927   | Layout 2             | `7a6526c48435`  |
| 1921   | Layout 2             | `7a6526c48435`  |
| 1914   | Layout 2             | `7a6526c48435`  |
| 1908   | Layout 2             | `7a6526c48435`  |
| 1897   | Layout 2             | `7a6526c48435`  |
| 1892   | Layout 2             | `7a6526c48435`  |
| 1886   | Layout 2             | `7a6526c48435`  |
| 1881   | Layout 2             | `7a6526c48435`  |
| 1871   | Layout 2             | `7a6526c48435`  |
| 1866   | Layout 2             | `7a6526c48435`  |
| 1862   | Layout 2             | `7a6526c48435`  |
| 1854   | Layout 2             | `7a6526c48435`  |
| 1846   | Layout 2             | `7a6526c48435`  |
| 1838   | Layout 2             | `7a6526c48435`  |
| 1832   | Layout 2             | `7a6526c48435`  |
| 1826   | Layout 2             | `7a6526c48435`  |
| 1822   | Layout 2             | `7a6526c48435`  |
| 1818   | Layout 2             | `7a6526c48435`  |
| 1804   | Layout 2             | `7a6526c48435`  |
| 1794   | Layout 2             | `7a6526c48435`  |
| 1790   | Layout 2             | `7a6526c48435`  |
| 1784   | Layout 2             | `7a6526c48435`  |
| 1774   | Layout 2             | `7a6526c48435`  |
| 1771   | Layout 2             | `7a6526c48435`  |
| 1762   | Layout 2             | `7a6526c48435`  |
| 1759   | Layout 2             | `7a6526c48435`  |
| 1754   | Layout 2             | `7a6526c48435`  |
| 1749   | Layout 2             | `7a6526c48435`  |
| 1743   | Layout 2             | `7a6526c48435`  |
| 1737   | Layout 2             | `7a6526c48435`  |
| 1731   | Layout 2             | `7a6526c48435`  |
| 1725   | Layout 2             | `7a6526c48435`  |
| 1717   | Layout 2             | `7a6526c48435`  |
| 1710   | Layout 2             | `7a6526c48435`  |
| 1704   | Layout 2             | `7a6526c48435`  |
| 1698   | Layout 2             | `7a6526c48435`  |
| 1690   | Layout 2             | `7a6526c48435`  |
| 1685   | Layout 2             | `7a6526c48435`  |
| 1680   | Layout 2             | `7a6526c48435`  |
| 1674   | Layout 2             | `7a6526c48435`  |
| 1668   | Layout 2             | `7a6526c48435`  |
| 1659   | Layout 2             | `7a6526c48435`  |
| 1649   | Layout 2             | `7a6526c48435`  |
| 1642   | Layout 2             | `7a6526c48435`  |
| 1636   | Layout 2             | `7a6526c48435`  |
| 1628   | Layout 2             | `7a6526c48435`  |
| 1622   | Layout 2             | `7a6526c48435`  |
| 1614   | Layout 2             | `7a6526c48435`  |
| 1608   | Layout 2             | `7a6526c48435`  |
| 1602   | Layout 2             | `7a6526c48435`  |
| 1598   | Layout 2             | `7a6526c48435`  |
| 1594   | Layout 2             | `7a6526c48435`  |
| 1590   | Layout 2             | `7a6526c48435`  |
| 1587   | Layout 2             | `7a6526c48435`  |
| 1584   | Layout 2             | `7a6526c48435`  |
| 1579   | Layout 2             | `7a6526c48435`  |
| 1572   | Layout 2             | `7a6526c48435`  |
| 1565   | Layout 2             | `7a6526c48435`  |
| 1559   | Layout 2             | `7a6526c48435`  |
| 1554   | Layout 2             | `7a6526c48435`  |
| 1547   | Layout 2             | `7a6526c48435`  |
| 1537   | Layout 2             | `7a6526c48435`  |
| 1529   | Layout 2             | `7a6526c48435`  |
| 1524   | Layout 2             | `7a6526c48435`  |
| 1519   | Layout 2             | `7a6526c48435`  |
| 1509   | Layout 2             | `7a6526c48435`  |
| 1506   | Layout 2             | `7a6526c48435`  |
| 1504   | Layout 2             | `7a6526c48435`  |
| 1500   | Layout 2             | `7a6526c48435`  |
| 1493   | Layout 2             | `7a6526c48435`  |
| 1489   | Layout 2             | `7a6526c48435`  |
| 1485   | Layout 2             | `7a6526c48435`  |
| 1481   | Layout 2             | `7a6526c48435`  |
| 1474   | Layout 2             | `7a6526c48435`  |
| 1466   | Layout 2             | `7a6526c48435`  |
| 1462   | Layout 2             | `7a6526c48435`  |
| 1459   | Layout 2             | `7a6526c48435`  |
| 1453   | Layout 2             | `7a6526c48435`  |
| 1450   | Layout 2             | `7a6526c48435`  |
| 1445   | Layout 2             | `7a6526c48435`  |
| 1439   | Layout 2             | `7a6526c48435`  |
| 1433   | Layout 2             | `7a6526c48435`  |
| 1430   | Layout 2             | `7a6526c48435`  |
| 1426   | Layout 2             | `7a6526c48435`  |
| 1421   | Layout 2             | `7a6526c48435`  |
| 1417   | Layout 2             | `7a6526c48435`  |
| 1416   | Layout 2             | `7a6526c48435`  |
| 1409   | Layout 2             | `7a6526c48435`  |
| 1405   | Layout 2             | `7a6526c48435`  |
| 1401   | Layout 2             | `7a6526c48435`  |
| 1396   | Layout 2             | `7a6526c48435`  |
| 1391   | Layout 2             | `7a6526c48435`  |
| 1390   | Layout 2             | `7a6526c48435`  |
| 1386   | Layout 2             | `7a6526c48435`  |
| 1381   | Layout 2             | `7a6526c48435`  |
| 1379   | Layout 2             | `7a6526c48435`  |
| 1372   | Layout 2             | `7a6526c48435`  |
| 1366   | Layout 2             | `7a6526c48435`  |
| 1364   | Layout 2             | `7a6526c48435`  |
| 1363   | Layout 2             | `7a6526c48435`  |
| 1360   | Layout 2             | `7a6526c48435`  |
| 1358   | Layout 2             | `7a6526c48435`  |
| 1355   | Layout 2             | `7a6526c48435`  |
| 1351   | Layout 2             | `7a6526c48435`  |
| 1348   | Layout 2             | `7a6526c48435`  |
| 1346   | Layout 2             | `7a6526c48435`  |
| 1341   | Layout 2             | `7a6526c48435`  |
| 1340   | Layout 2             | `7a6526c48435`  |
| 1338   | Layout 2             | `7a6526c48435`  |
| 1335   | Layout 2             | `7a6526c48435`  |
| 1333   | Layout 2             | `7a6526c48435`  |
| 1329   | Layout 2             | `7a6526c48435`  |
| 1327   | Layout 2             | `7a6526c48435`  |
| 1324   | Layout 2             | `7a6526c48435`  |
| 1321   | Layout 2             | `7a6526c48435`  |
| 1319   | Layout 2             | `7a6526c48435`  |
| 1318   | Layout 2             | `7a6526c48435`  |
| 1316   | Layout 2             | `7a6526c48435`  |
| 1313   | Layout 2             | `7a6526c48435`  |
| 1311   | Layout 2             | `7a6526c48435`  |
| 1309   | Layout 2             | `7a6526c48435`  |
| 1304   | Layout 2             | `7a6526c48435`  |
| 1292   | Layout 2             | `7a6526c48435`  |
| 1286   | Layout 2             | `7a6526c48435`  |
| 1280   | Layout 2             | `7a6526c48435`  |
| 1276   | No documented layout | `7a6526c48435`  |
| 1267   | No documented layout | `7a6526c48435`  |
| 1261   | No documented layout | `7a6526c48435`  |
| 1256   | No documented layout | `7a6526c48435`  |
| 1250   | No documented layout | `7a6526c48435`  |
| 1246   | No documented layout | `7a6526c48435`  |
| 1239   | No documented layout | `7a6526c48435`  |
| 1230   | Layout 1             | `7a6526c48435`  |
| 1226   | Layout 1             | `7a6526c48435`  |
| 1220   | Layout 1             | `7a6526c48435`  |
| 1217   | No file              | `7a6526c48435`  |
| 1211   | No file              | `7a6526c48435`  |
| 1210   | No file              | `7a6526c48435`  |
| 1208   | No file              | `7a6526c48435`  |
| 1203   | No file              | `7a6526c48435`  |
| 1197   | No file              | `7a6526c48435`  |
| 1194   | No file              | `7a6526c48435`  |
| 1192   | No file              | `7a6526c48435`  |
| 1187   | No file              | `7a6526c48435`  |
| 1183   | No file              | `7a6526c48435`  |
| 1177   | No file              | `7a6526c48435`  |
| 1173   | No file              | `7a6526c48435`  |
| 1167   | No file              | `7a6526c48435`  |
| 1164   | No file              | `7a6526c48435`  |
| 1156   | No file              | `7a6526c48435`  |
| 1149   | No file              | `7a6526c48435`  |
| 1144   | No file              | `7a6526c48435`  |
| 1137   | No file              | `7a6526c48435`  |
| 1132   | No file              | `7a6526c48435`  |
| 1127   | No file              | `7a6526c48435`  |
| 1122   | No file              | `7a6526c48435`  |
| 1118   | No file              | `7a6526c48435`  |
| 1114   | No file              | `7a6526c48435`  |
| 1109   | No file              | `7a6526c48435`  |
| 1102   | No file              | `7a6526c48435`  |
| 1096   | No file              | `7a6526c48435`  |
| 1088   | No file              | `7a6526c48435`  |
| 1081   | No file              | `7a6526c48435`  |
| 1076   | No file              | `7a6526c48435`  |
| 1069   | No file              | `7a6526c48435`  |
| 1064   | No file              | `7a6526c48435`  |
| 1058   | No file              | `7a6526c48435`  |
| 1051   | No file              | `7a6526c48435`  |
| 1044   | No file              | `7a6526c48435`  |
| 1036   | No file              | `7a6526c48435`  |
| 1026   | No file              | `7a6526c48435`  |
| 1016   | No file              | `7a6526c48435`  |
| 1009   | No file              | `7a6526c48435`  |
| 1005   | No file              | `7a6526c48435`  |
| 1000   | No file              | `7a6526c48435`  |
| 998    | No file              | `7a6526c48435`  |
| 990    | No file              | `7a6526c48435`  |
| 979    | No file              | `7a6526c48435`  |
| 972    | No file              | `7a6526c48435`  |
| 963    | No file              | `7a6526c48435`  |
| 955    | No file              | `7a6526c48435`  |
| 946    | No file              | `7a6526c48435`  |
| 938    | No file              | `7a6526c48435`  |
| 927    | No file              | `7a6526c48435`  |
| 911    | No file              | `7a6526c48435`  |
| 904    | No file              | `7a6526c48435`  |
| 899    | No file              | `7a6526c48435`  |
| 894    | No file              | `7a6526c48435`  |
| 885    | No file              | `7a6526c48435`  |
| 879    | No file              | `7a6526c48435`  |
| 872    | No file              | `7a6526c48435`  |
| 864    | No file              | `7a6526c48435`  |
| 855    | No file              | `7a6526c48435`  |
| 853    | No file              | `7a6526c48435`  |
| 845    | No file              | `7a6526c48435`  |
| 837    | No file              | `7a6526c48435`  |
| 829    | No file              | `7a6526c48435`  |
| 822    | No file              | `7a6526c48435`  |
| 814    | No file              | `7a6526c48435`  |
| 805    | No file              | `7a6526c48435`  |
| 794    | No file              | `7a6526c48435`  |
| 787    | No file              | `7a6526c48435`  |
| 780    | No file              | `7a6526c48435`  |
| 771    | No file              | `7a6526c48435`  |
| 760    | No file              | `7a6526c48435`  |
| 748    | No file              | `7a6526c48435`  |
| 741    | No file              | `7a6526c48435`  |
| 736    | No file              | `7a6526c48435`  |
| 731    | No file              | `7a6526c48435`  |
| 723    | No file              | `7a6526c48435`  |
| 711    | No file              | `7a6526c48435`  |
| 707    | No file              | `7a6526c48435`  |
| 697    | No file              | `7a6526c48435`  |
| 689    | No file              | `7a6526c48435`  |
| 683    | No file              | `7a6526c48435`  |
| 678    | No file              | `7a6526c48435`  |
| 670    | No file              | `7a6526c48435`  |
| 661    | No file              | `7a6526c48435`  |
| 656    | No file              | `7a6526c48435`  |
| 652    | No file              | `7a6526c48435`  |
| 643    | No file              | `7a6526c48435`  |
| 637    | No file              | `7a6526c48435`  |
| 630    | No file              | `7a6526c48435`  |
| 627    | No file              | `7a6526c48435`  |
| 621    | No file              | `7a6526c48435`  |
| 617    | No file              | `7a6526c48435`  |
| 615    | No file              | `7a6526c48435`  |
| 606    | No file              | `7a6526c48435`  |
| 599    | No file              | `7a6526c48435`  |
| 592    | No file              | `7a6526c48435`  |
| 586    | No file              | `7a6526c48435`  |
| 577    | No file              | `7a6526c48435`  |
| 569    | No file              | `7a6526c48435`  |
| 561    | No file              | `7a6526c48435`  |
| 554    | No file              | `7a6526c48435`  |
| 542    | No file              | `7a6526c48435`  |
| 532    | No file              | `7a6526c48435`  |
| 531    | No file              | `7a6526c48435`  |
| 526    | No file              | `7a6526c48435`  |
| 521    | No file              | `7a6526c48435`  |
| 517    | No file              | `7a6526c48435`  |
| 510    | No file              | `7a6526c48435`  |
| 508    | No file              | `7a6526c48435`  |
| 504    | No file              | `7a6526c48435`  |
| 497    | No file              | `7a6526c48435`  |
| 491    | No file              | `7a6526c48435`  |
| 485    | No file              | `7a6526c48435`  |
| 478    | No file              | `7a6526c48435`  |
| 472    | No file              | `7a6526c48435`  |
| 466    | No file              | `7a6526c48435`  |
| 457    | No file              | `7a6526c48435`  |
| 452    | No file              | `7a6526c48435`  |
| 449    | No file              | `7a6526c48435`  |
| 435    | No file              | `7a6526c48435`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Character keys with a `characterstatic.dbss` row, for the link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6, `str_id1` = character key)       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A `PABR` table of variable-size character entries with an empty string
table.

| Offset                | Type             | Field              | Notes                                         |
| --------------------- | ---------------- | ------------------ | --------------------------------------------- |
| `+0x00`               | char[4]          | magic              | ASCII `PABR`                                  |
| `+0x04`               | u32              | count              | Number of characters; `14` on client 3474     |
| `+0x08`               | Character[count] | characters         | See Character                                 |
| `characters+0x00`     | String Table     | string_table       | Empty string table                            |
| `string_table+0x00`   | u32              | string_table_start | End of the characters, `1292` on client 3474  |
| `string_table+0x04`   | u32              | zero               | `0`                                           |

The characters are in neither key order nor sheet order (`1`, `65002`,
`2`, `65003`, `3`, `65005`, `21`, `5`, `65008` and up on client 3474).

### Character (variable: 6 bytes + actions)

| Offset  | Type                 | Field        | Notes                                              |
| ------- | -------------------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16                  | character_key | Character key (LOC type 6 name); unique in the file; see Notes |
| `+0x02` | u32                  | action_count | Number of actions                                  |
| `+0x06` | Action[action_count] | actions      | See Action                                         |

### Action (8 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | action_hash    | `ascii_key_hash` of the action name (`_common/string_hash.py`); unique within a character |
| `+0x04` | u32  | able_call_time | `AbleCallTime`, the sheet value cut to a whole number (`598.290598` is stored as `598`) |

The actions of a character are not in sheet order either.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1230 has one action per character and no action hash: 5 rows for
the five player classes of Layout 2, in the same order, each with the same
`able_call_time` as its one Layout 2 action.

### File Layout

| Offset              | Type         | Field              | Notes                                   |
| ------------------- | ------------ | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                            |
| `+0x04`             | u32          | count              | Number of rows; `5` on client 1230      |
| `+0x08`             | Row[count]   | rows               | See Row                                 |
| `rows+0x00`         | String Table | string_table       | Empty string table                      |
| `string_table+0x00` | u32          | string_table_start | End of the rows, `88` on client 1230    |
| `string_table+0x04` | u32          | zero               | `0`                                     |

### Row (16 bytes)

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u32  | unknown_00     | `8` in every row; see Open Questions     |
| `+0x04` | u32  | unknown_04     | `0` in every row                         |
| `+0x08` | u32  | character_key  | Player class character key               |
| `+0x0C` | u32  | able_call_time | As in Layout 2                           |

## Action Names

The client stores the names only as `action_hash`. The handler names an
action from the 29 action names of the client 1784 sheet (see Field
Names), each hashed with `ascii_key_hash`; an action whose hash is not one
of them shows as hex. On client 3474 all 150 action hashes are one of the
29.

| Character keys  | Action names                                                                 |
| --------------- | ---------------------------------------------------------------------------- |
| `1`, `2`, `5`   | `BT_WAIT`                                                                    |
| `3`             | `BT_skill_SkyFall`                                                           |
| `21`            | `BT_skill_ThrustAndSmash_AttQ1`                                              |
| `65002` to `65037` | `SHADOW_ATTACK_1` to `SHADOW_ATTACK_6`, `SHADOW_ATTACK_1_2`, `SHADOW_ATTACK_F_1` to `SHADOW_ATTACK_F_5`, `SHADOW_ATTACK_L_1` to `SHADOW_ATTACK_L_3`, `SHADOW_ATTACK_L_1_C`, `SHADOW_ATTACK_R_1` to `SHADOW_ATTACK_R_3`, `SHADOW_ATTACK_R_1_C`, `SHADOW_DASHATTACK_1`, `SHADOW_JUMP_ATTACK`, `SHADOW_DASHJUMP_ATTACK`, `BT_ROLL_L`, `BT_ROLL_R`, `BT_ROLL_B` |

## Field Names

The names follow the `ActionVerification_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784, columns `CharacterKey`,
`ActionName` and `AbleCallTime`. All 150 sheet rows are in the client 1784
and 3474 files: the `ascii_key_hash` of each `ActionName` is an
`action_hash` of the row's `CharacterKey`, and its `AbleCallTime`, cut to a
whole number, is the stored `able_call_time` (150 of 150 rows, client
3474). The server dump of the same private server reads the sheet in the
function at `0x1408f0b10`.

The 2016 PDB has no action verification type and the client 519 tables
have no such table.

## Notes

- The client 1784, 1485, 2107, 2519, 3002, 3251 and 3474 files are byte for
  byte the same. Client 794 has no `actionverification.bss`.
- Each hero character key is `64950` plus a class type of
  [`actionverificationindex.dbss`](actionverificationindex_dbss.md):
  `65002` Jordine is class type `52` Jordine, and the LOC names of the two
  agree for Peony, Ahon Kirus, Povios, Syaki, Nelydormin and Orwen as well.
  `65031` (Striker) and `65037` (Tamer) give `81` and `87`, which LOC type
  21 names `[PH] 22` and `[PH] 28`. Class types `61`, `65` and `71` have no
  character in this file.
- On client 3474 the five player class keys have a `characterstatic.dbss`
  row and the nine hero keys have none; every key has a LOC type 6 name.
- `BT_ROLL_L`, `BT_ROLL_R` and `BT_ROLL_B` hold `230` for every hero on
  client 3474 (`230.769231` in the sheet).

## Open Questions

### Unit of `able_call_time`

The sheet values are fractions such as `230.769231` (`3000 / 13`) and
`598.290598`; the stored values are whole numbers from `230` to `6300` on
client 3474. No client Lua file names `ActionVerification` or
`AbleCallTime`, so the unit (milliseconds or another time base) is not
confirmed.

### What the Layout 1 `unknown_00` Holds

Each client 1230 row starts with a u32 `8` and a u32 `0`. The `8` could
be the size of the `character_key` and `able_call_time` pair that follows,
or an action count of another meaning; with five identical rows the
reading cannot be told apart.
