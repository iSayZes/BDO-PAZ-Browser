# `siege2024rewardstaticstatus.bss` Format

## Purpose

The Node War (2024 land siege) rewards: per row a u16, five reward sets
of four item lists each, one more item list and two skill keys. On
client 3482 the three rows (`unknown_00` `0`, `1` and `2`) hand out the
Determined, Kindling and Blazing reward boxes: each set a Triumph Reward
of its tier (Tier 1 to Tier 5), Battlefield Honor or Glory, five Gold
Bars 1G or Medals of Glory and a Triumph Reward of Resilience; the last
list a Resolve Reward with two Combat Secret Books (S).

Same layout as [`oceansiegereward.bss`](oceansiegereward_bss.md), read by
the same handler: a u32 row count, then per row the u16 `unknown_00`,
five Reward Sets of four u64-counted lists of 16-byte rewards
(`item_id`, `unknown_04`, `count`), the list `unknown_rewards` and the
u32 `skill_key_1` and `skill_key_2`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records                         | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------------------------- | --------- |
| 2      | 3473 and later | 3483    | `siege2024rewardstaticstatus.bss` | 1,658 | 69 Reward, 15 Reward Set, 3 Row | 16        |
| 1      | 2538 to 3464   | 3464    | `siege2024rewardstaticstatus.bss` | 806   | 63 Reward, 15 Reward Set, 3 Row | 12        |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 2      | `siege2024rewardstaticstatus.bss` | 872 B (52.6%) | 786 B (47.4%) |
| 1      | `siege2024rewardstaticstatus.bss` | 800 B (99.3%) | 6 B (0.7%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `616cd1aeeff9`  |
| 3482   | Layout 2             | `616cd1aeeff9`  |
| 3474   | Layout 2             | `616cd1aeeff9`  |
| 3473   | Layout 2             | `616cd1aeeff9`  |
| 3464   | Layout 1             | `616cd1aeeff9`  |
| 3458   | Layout 1             | `616cd1aeeff9`  |
| 3454   | Layout 1             | `616cd1aeeff9`  |
| 3444   | Layout 1             | `616cd1aeeff9`  |
| 3435   | Layout 1             | `616cd1aeeff9`  |
| 3426   | Layout 1             | `616cd1aeeff9`  |
| 3418   | Layout 1             | `616cd1aeeff9`  |
| 3412   | Layout 1             | `616cd1aeeff9`  |
| 3402   | Layout 1             | `616cd1aeeff9`  |
| 3396   | Layout 1             | `616cd1aeeff9`  |
| 3387   | Layout 1             | `616cd1aeeff9`  |
| 3381   | Layout 1             | `616cd1aeeff9`  |
| 3373   | Layout 1             | `616cd1aeeff9`  |
| 3364   | Layout 1             | `616cd1aeeff9`  |
| 3356   | Layout 1             | `616cd1aeeff9`  |
| 3349   | Layout 1             | `616cd1aeeff9`  |
| 3342   | Layout 1             | `616cd1aeeff9`  |
| 3335   | Layout 1             | `616cd1aeeff9`  |
| 3326   | Layout 1             | `616cd1aeeff9`  |
| 3321   | Layout 1             | `616cd1aeeff9`  |
| 3314   | Layout 1             | `616cd1aeeff9`  |
| 3303   | Layout 1             | `616cd1aeeff9`  |
| 3302   | Layout 1             | `616cd1aeeff9`  |
| 3293   | Layout 1             | `616cd1aeeff9`  |
| 3283   | Layout 1             | `616cd1aeeff9`  |
| 3275   | Layout 1             | `616cd1aeeff9`  |
| 3267   | Layout 1             | `616cd1aeeff9`  |
| 3258   | Layout 1             | `616cd1aeeff9`  |
| 3251   | Layout 1             | `616cd1aeeff9`  |
| 3242   | Layout 1             | `616cd1aeeff9`  |
| 3235   | Layout 1             | `616cd1aeeff9`  |
| 3229   | Layout 1             | `616cd1aeeff9`  |
| 3212   | Layout 1             | `616cd1aeeff9`  |
| 3203   | Layout 1             | `616cd1aeeff9`  |
| 3193   | Layout 1             | `616cd1aeeff9`  |
| 3186   | Layout 1             | `616cd1aeeff9`  |
| 3177   | Layout 1             | `616cd1aeeff9`  |
| 3169   | Layout 1             | `616cd1aeeff9`  |
| 3158   | Layout 1             | `616cd1aeeff9`  |
| 3151   | Layout 1             | `616cd1aeeff9`  |
| 3144   | Layout 1             | `616cd1aeeff9`  |
| 3133   | Layout 1             | `616cd1aeeff9`  |
| 3125   | Layout 1             | `616cd1aeeff9`  |
| 3118   | Layout 1             | `616cd1aeeff9`  |
| 3111   | Layout 1             | `616cd1aeeff9`  |
| 3103   | Layout 1             | `616cd1aeeff9`  |
| 3095   | Layout 1             | `616cd1aeeff9`  |
| 3086   | Layout 1             | `616cd1aeeff9`  |
| 3072   | Layout 1             | `616cd1aeeff9`  |
| 3062   | Layout 1             | `616cd1aeeff9`  |
| 3052   | Layout 1             | `616cd1aeeff9`  |
| 3045   | Layout 1             | `616cd1aeeff9`  |
| 3037   | Layout 1             | `616cd1aeeff9`  |
| 3030   | Layout 1             | `616cd1aeeff9`  |
| 3021   | Layout 1             | `616cd1aeeff9`  |
| 3012   | Layout 1             | `616cd1aeeff9`  |
| 3002   | Layout 1             | `616cd1aeeff9`  |
| 2995   | Layout 1             | `616cd1aeeff9`  |
| 2987   | Layout 1             | `616cd1aeeff9`  |
| 2978   | Layout 1             | `616cd1aeeff9`  |
| 2970   | Layout 1             | `616cd1aeeff9`  |
| 2959   | Layout 1             | `616cd1aeeff9`  |
| 2951   | Layout 1             | `616cd1aeeff9`  |
| 2942   | Layout 1             | `616cd1aeeff9`  |
| 2935   | Layout 1             | `616cd1aeeff9`  |
| 2932   | Layout 1             | `616cd1aeeff9`  |
| 2923   | Layout 1             | `616cd1aeeff9`  |
| 2919   | Layout 1             | `616cd1aeeff9`  |
| 2907   | Layout 1             | `616cd1aeeff9`  |
| 2900   | Layout 1             | `616cd1aeeff9`  |
| 2891   | Layout 1             | `616cd1aeeff9`  |
| 2882   | Layout 1             | `616cd1aeeff9`  |
| 2872   | No file              | `616cd1aeeff9`  |
| 2863   | No file              | `616cd1aeeff9`  |
| 2855   | No file              | `616cd1aeeff9`  |
| 2849   | No file              | `616cd1aeeff9`  |
| 2844   | No file              | `616cd1aeeff9`  |
| 2834   | No file              | `616cd1aeeff9`  |
| 2825   | No file              | `616cd1aeeff9`  |
| 2819   | No file              | `616cd1aeeff9`  |
| 2811   | No file              | `616cd1aeeff9`  |
| 2803   | No file              | `616cd1aeeff9`  |
| 2794   | No file              | `616cd1aeeff9`  |
| 2783   | No file              | `616cd1aeeff9`  |
| 2774   | No file              | `616cd1aeeff9`  |
| 2765   | No file              | `616cd1aeeff9`  |
| 2756   | No file              | `616cd1aeeff9`  |
| 2750   | No file              | `616cd1aeeff9`  |
| 2743   | No file              | `616cd1aeeff9`  |
| 2736   | No file              | `616cd1aeeff9`  |
| 2726   | No file              | `616cd1aeeff9`  |
| 2717   | No file              | `616cd1aeeff9`  |
| 2709   | No file              | `616cd1aeeff9`  |
| 2703   | No file              | `616cd1aeeff9`  |
| 2695   | No file              | `616cd1aeeff9`  |
| 2684   | No file              | `616cd1aeeff9`  |
| 2672   | No file              | `616cd1aeeff9`  |
| 2665   | No file              | `616cd1aeeff9`  |
| 2657   | No file              | `616cd1aeeff9`  |
| 2649   | No file              | `616cd1aeeff9`  |
| 2644   | No file              | `616cd1aeeff9`  |
| 2637   | No file              | `616cd1aeeff9`  |
| 2629   | No file              | `616cd1aeeff9`  |
| 2619   | No file              | `616cd1aeeff9`  |
| 2612   | No file              | `616cd1aeeff9`  |
| 2606   | No file              | `616cd1aeeff9`  |
| 2602   | No file              | `616cd1aeeff9`  |
| 2601   | No file              | `616cd1aeeff9`  |
| 2592   | No file              | `616cd1aeeff9`  |
| 2583   | No file              | `616cd1aeeff9`  |
| 2575   | No file              | `616cd1aeeff9`  |
| 2567   | No file              | `616cd1aeeff9`  |
| 2560   | No file              | `616cd1aeeff9`  |
| 2553   | Layout 1             | `616cd1aeeff9`  |
| 2545   | Layout 1             | `616cd1aeeff9`  |
| 2538   | Layout 1             | `616cd1aeeff9`  |
| 2529   | No documented layout | `616cd1aeeff9`  |
| 2519   | No documented layout | `616cd1aeeff9`  |
| 2513   | No file              | `616cd1aeeff9`  |
| 2510   | No file              | `616cd1aeeff9`  |
| 2507   | No file              | `616cd1aeeff9`  |
| 2503   | No file              | `616cd1aeeff9`  |
| 2498   | No file              | `616cd1aeeff9`  |
| 2492   | No file              | `616cd1aeeff9`  |
| 2487   | No file              | `616cd1aeeff9`  |
| 2480   | No file              | `616cd1aeeff9`  |
| 2474   | No file              | `616cd1aeeff9`  |
| 2468   | No file              | `616cd1aeeff9`  |
| 2460   | No file              | `616cd1aeeff9`  |
| 2453   | No file              | `616cd1aeeff9`  |
| 2444   | No file              | `616cd1aeeff9`  |
| 2438   | No file              | `616cd1aeeff9`  |
| 2434   | No file              | `616cd1aeeff9`  |
| 2429   | No file              | `616cd1aeeff9`  |
| 2421   | No file              | `616cd1aeeff9`  |
| 2414   | No file              | `616cd1aeeff9`  |
| 2407   | No file              | `616cd1aeeff9`  |
| 2401   | No file              | `616cd1aeeff9`  |
| 2397   | No file              | `616cd1aeeff9`  |
| 2393   | No file              | `616cd1aeeff9`  |
| 2384   | No file              | `616cd1aeeff9`  |
| 2378   | No file              | `616cd1aeeff9`  |
| 2372   | No file              | `616cd1aeeff9`  |
| 2358   | No file              | `616cd1aeeff9`  |
| 2352   | No file              | `616cd1aeeff9`  |
| 2347   | No file              | `616cd1aeeff9`  |
| 2343   | No file              | `616cd1aeeff9`  |
| 2335   | No file              | `616cd1aeeff9`  |
| 2327   | No file              | `616cd1aeeff9`  |
| 2324   | No file              | `616cd1aeeff9`  |
| 2319   | No file              | `616cd1aeeff9`  |
| 2313   | No file              | `616cd1aeeff9`  |
| 2308   | No file              | `616cd1aeeff9`  |
| 2302   | No file              | `616cd1aeeff9`  |
| 2295   | No file              | `616cd1aeeff9`  |
| 2290   | No file              | `616cd1aeeff9`  |
| 2284   | No file              | `616cd1aeeff9`  |
| 2276   | No file              | `616cd1aeeff9`  |
| 2269   | No file              | `616cd1aeeff9`  |
| 2259   | No file              | `616cd1aeeff9`  |
| 2250   | No file              | `616cd1aeeff9`  |
| 2243   | No file              | `616cd1aeeff9`  |
| 2235   | No file              | `616cd1aeeff9`  |
| 2229   | No file              | `616cd1aeeff9`  |
| 2224   | No file              | `616cd1aeeff9`  |
| 2218   | No file              | `616cd1aeeff9`  |
| 2215   | No file              | `616cd1aeeff9`  |
| 2207   | No file              | `616cd1aeeff9`  |
| 2203   | No file              | `616cd1aeeff9`  |
| 2196   | No file              | `616cd1aeeff9`  |
| 2192   | No file              | `616cd1aeeff9`  |
| 2189   | No file              | `616cd1aeeff9`  |
| 2183   | No file              | `616cd1aeeff9`  |
| 2179   | No file              | `616cd1aeeff9`  |
| 2171   | No file              | `616cd1aeeff9`  |
| 2163   | No file              | `616cd1aeeff9`  |
| 2156   | No file              | `616cd1aeeff9`  |
| 2151   | No file              | `616cd1aeeff9`  |
| 2147   | No file              | `616cd1aeeff9`  |
| 2142   | No file              | `616cd1aeeff9`  |
| 2138   | No file              | `616cd1aeeff9`  |
| 2134   | No file              | `616cd1aeeff9`  |
| 2130   | No file              | `616cd1aeeff9`  |
| 2122   | No file              | `616cd1aeeff9`  |
| 2107   | No file              | `616cd1aeeff9`  |
| 2098   | No file              | `616cd1aeeff9`  |
| 2089   | No file              | `616cd1aeeff9`  |
| 2081   | No file              | `616cd1aeeff9`  |
| 2073   | No file              | `616cd1aeeff9`  |
| 2067   | No file              | `616cd1aeeff9`  |
| 2063   | No file              | `616cd1aeeff9`  |
| 2059   | No file              | `616cd1aeeff9`  |
| 2052   | No file              | `616cd1aeeff9`  |
| 2044   | No file              | `616cd1aeeff9`  |
| 2039   | No file              | `616cd1aeeff9`  |
| 2032   | No file              | `616cd1aeeff9`  |
| 2025   | No file              | `616cd1aeeff9`  |
| 2011   | No file              | `616cd1aeeff9`  |
| 2005   | No file              | `616cd1aeeff9`  |
| 2000   | No file              | `616cd1aeeff9`  |
| 1996   | No file              | `616cd1aeeff9`  |
| 1991   | No file              | `616cd1aeeff9`  |
| 1985   | No file              | `616cd1aeeff9`  |
| 1980   | No file              | `616cd1aeeff9`  |
| 1969   | No file              | `616cd1aeeff9`  |
| 1964   | No file              | `616cd1aeeff9`  |
| 1958   | No file              | `616cd1aeeff9`  |
| 1950   | No file              | `616cd1aeeff9`  |
| 1945   | No file              | `616cd1aeeff9`  |
| 1937   | No file              | `616cd1aeeff9`  |
| 1933   | No file              | `616cd1aeeff9`  |
| 1927   | No file              | `616cd1aeeff9`  |
| 1921   | No file              | `616cd1aeeff9`  |
| 1914   | No file              | `616cd1aeeff9`  |
| 1908   | No file              | `616cd1aeeff9`  |
| 1897   | No file              | `616cd1aeeff9`  |
| 1892   | No file              | `616cd1aeeff9`  |
| 1886   | No file              | `616cd1aeeff9`  |
| 1881   | No file              | `616cd1aeeff9`  |
| 1871   | No file              | `616cd1aeeff9`  |
| 1866   | No file              | `616cd1aeeff9`  |
| 1862   | No file              | `616cd1aeeff9`  |
| 1854   | No file              | `616cd1aeeff9`  |
| 1846   | No file              | `616cd1aeeff9`  |
| 1838   | No file              | `616cd1aeeff9`  |
| 1832   | No file              | `616cd1aeeff9`  |
| 1826   | No file              | `616cd1aeeff9`  |
| 1822   | No file              | `616cd1aeeff9`  |
| 1818   | No file              | `616cd1aeeff9`  |
| 1804   | No file              | `616cd1aeeff9`  |
| 1794   | No file              | `616cd1aeeff9`  |
| 1790   | No file              | `616cd1aeeff9`  |
| 1784   | No file              | `616cd1aeeff9`  |
| 1774   | No file              | `616cd1aeeff9`  |
| 1771   | No file              | `616cd1aeeff9`  |
| 1762   | No file              | `616cd1aeeff9`  |
| 1759   | No file              | `616cd1aeeff9`  |
| 1754   | No file              | `616cd1aeeff9`  |
| 1749   | No file              | `616cd1aeeff9`  |
| 1743   | No file              | `616cd1aeeff9`  |
| 1737   | No file              | `616cd1aeeff9`  |
| 1731   | No file              | `616cd1aeeff9`  |
| 1725   | No file              | `616cd1aeeff9`  |
| 1717   | No file              | `616cd1aeeff9`  |
| 1710   | No file              | `616cd1aeeff9`  |
| 1704   | No file              | `616cd1aeeff9`  |
| 1698   | No file              | `616cd1aeeff9`  |
| 1690   | No file              | `616cd1aeeff9`  |
| 1685   | No file              | `616cd1aeeff9`  |
| 1680   | No file              | `616cd1aeeff9`  |
| 1674   | No file              | `616cd1aeeff9`  |
| 1668   | No file              | `616cd1aeeff9`  |
| 1659   | No file              | `616cd1aeeff9`  |
| 1649   | No file              | `616cd1aeeff9`  |
| 1642   | No file              | `616cd1aeeff9`  |
| 1636   | No file              | `616cd1aeeff9`  |
| 1628   | No file              | `616cd1aeeff9`  |
| 1622   | No file              | `616cd1aeeff9`  |
| 1614   | No file              | `616cd1aeeff9`  |
| 1608   | No file              | `616cd1aeeff9`  |
| 1602   | No file              | `616cd1aeeff9`  |
| 1598   | No file              | `616cd1aeeff9`  |
| 1594   | No file              | `616cd1aeeff9`  |
| 1590   | No file              | `616cd1aeeff9`  |
| 1587   | No file              | `616cd1aeeff9`  |
| 1584   | No file              | `616cd1aeeff9`  |
| 1579   | No file              | `616cd1aeeff9`  |
| 1572   | No file              | `616cd1aeeff9`  |
| 1565   | No file              | `616cd1aeeff9`  |
| 1559   | No file              | `616cd1aeeff9`  |
| 1554   | No file              | `616cd1aeeff9`  |
| 1547   | No file              | `616cd1aeeff9`  |
| 1537   | No file              | `616cd1aeeff9`  |
| 1529   | No file              | `616cd1aeeff9`  |
| 1524   | No file              | `616cd1aeeff9`  |
| 1519   | No file              | `616cd1aeeff9`  |
| 1509   | No file              | `616cd1aeeff9`  |
| 1506   | No file              | `616cd1aeeff9`  |
| 1504   | No file              | `616cd1aeeff9`  |
| 1500   | No file              | `616cd1aeeff9`  |
| 1493   | No file              | `616cd1aeeff9`  |
| 1489   | No file              | `616cd1aeeff9`  |
| 1485   | No file              | `616cd1aeeff9`  |
| 1481   | No file              | `616cd1aeeff9`  |
| 1474   | No file              | `616cd1aeeff9`  |
| 1466   | No file              | `616cd1aeeff9`  |
| 1462   | No file              | `616cd1aeeff9`  |
| 1459   | No file              | `616cd1aeeff9`  |
| 1453   | No file              | `616cd1aeeff9`  |
| 1450   | No file              | `616cd1aeeff9`  |
| 1445   | No file              | `616cd1aeeff9`  |
| 1439   | No file              | `616cd1aeeff9`  |
| 1433   | No file              | `616cd1aeeff9`  |
| 1430   | No file              | `616cd1aeeff9`  |
| 1426   | No file              | `616cd1aeeff9`  |
| 1421   | No file              | `616cd1aeeff9`  |
| 1417   | No file              | `616cd1aeeff9`  |
| 1416   | No file              | `616cd1aeeff9`  |
| 1409   | No file              | `616cd1aeeff9`  |
| 1405   | No file              | `616cd1aeeff9`  |
| 1401   | No file              | `616cd1aeeff9`  |
| 1396   | No file              | `616cd1aeeff9`  |
| 1391   | No file              | `616cd1aeeff9`  |
| 1390   | No file              | `616cd1aeeff9`  |
| 1386   | No file              | `616cd1aeeff9`  |
| 1381   | No file              | `616cd1aeeff9`  |
| 1379   | No file              | `616cd1aeeff9`  |
| 1372   | No file              | `616cd1aeeff9`  |
| 1366   | No file              | `616cd1aeeff9`  |
| 1364   | No file              | `616cd1aeeff9`  |
| 1363   | No file              | `616cd1aeeff9`  |
| 1360   | No file              | `616cd1aeeff9`  |
| 1358   | No file              | `616cd1aeeff9`  |
| 1355   | No file              | `616cd1aeeff9`  |
| 1351   | No file              | `616cd1aeeff9`  |
| 1348   | No file              | `616cd1aeeff9`  |
| 1346   | No file              | `616cd1aeeff9`  |
| 1341   | No file              | `616cd1aeeff9`  |
| 1340   | No file              | `616cd1aeeff9`  |
| 1338   | No file              | `616cd1aeeff9`  |
| 1335   | No file              | `616cd1aeeff9`  |
| 1333   | No file              | `616cd1aeeff9`  |
| 1329   | No file              | `616cd1aeeff9`  |
| 1327   | No file              | `616cd1aeeff9`  |
| 1324   | No file              | `616cd1aeeff9`  |
| 1321   | No file              | `616cd1aeeff9`  |
| 1319   | No file              | `616cd1aeeff9`  |
| 1318   | No file              | `616cd1aeeff9`  |
| 1316   | No file              | `616cd1aeeff9`  |
| 1313   | No file              | `616cd1aeeff9`  |
| 1311   | No file              | `616cd1aeeff9`  |
| 1309   | No file              | `616cd1aeeff9`  |
| 1304   | No file              | `616cd1aeeff9`  |
| 1292   | No file              | `616cd1aeeff9`  |
| 1286   | No file              | `616cd1aeeff9`  |
| 1280   | No file              | `616cd1aeeff9`  |
| 1276   | No file              | `616cd1aeeff9`  |
| 1267   | No file              | `616cd1aeeff9`  |
| 1261   | No file              | `616cd1aeeff9`  |
| 1256   | No file              | `616cd1aeeff9`  |
| 1250   | No file              | `616cd1aeeff9`  |
| 1246   | No file              | `616cd1aeeff9`  |
| 1239   | No file              | `616cd1aeeff9`  |
| 1230   | No file              | `616cd1aeeff9`  |
| 1226   | No file              | `616cd1aeeff9`  |
| 1220   | No file              | `616cd1aeeff9`  |
| 1217   | No file              | `616cd1aeeff9`  |
| 1211   | No file              | `616cd1aeeff9`  |
| 1210   | No file              | `616cd1aeeff9`  |
| 1208   | No file              | `616cd1aeeff9`  |
| 1203   | No file              | `616cd1aeeff9`  |
| 1197   | No file              | `616cd1aeeff9`  |
| 1194   | No file              | `616cd1aeeff9`  |
| 1192   | No file              | `616cd1aeeff9`  |
| 1187   | No file              | `616cd1aeeff9`  |
| 1183   | No file              | `616cd1aeeff9`  |
| 1177   | No file              | `616cd1aeeff9`  |
| 1173   | No file              | `616cd1aeeff9`  |
| 1167   | No file              | `616cd1aeeff9`  |
| 1164   | No file              | `616cd1aeeff9`  |
| 1156   | No file              | `616cd1aeeff9`  |
| 1149   | No file              | `616cd1aeeff9`  |
| 1144   | No file              | `616cd1aeeff9`  |
| 1137   | No file              | `616cd1aeeff9`  |
| 1132   | No file              | `616cd1aeeff9`  |
| 1127   | No file              | `616cd1aeeff9`  |
| 1122   | No file              | `616cd1aeeff9`  |
| 1118   | No file              | `616cd1aeeff9`  |
| 1114   | No file              | `616cd1aeeff9`  |
| 1109   | No file              | `616cd1aeeff9`  |
| 1102   | No file              | `616cd1aeeff9`  |
| 1096   | No file              | `616cd1aeeff9`  |
| 1088   | No file              | `616cd1aeeff9`  |
| 1081   | No file              | `616cd1aeeff9`  |
| 1076   | No file              | `616cd1aeeff9`  |
| 1069   | No file              | `616cd1aeeff9`  |
| 1064   | No file              | `616cd1aeeff9`  |
| 1058   | No file              | `616cd1aeeff9`  |
| 1051   | No file              | `616cd1aeeff9`  |
| 1044   | No file              | `616cd1aeeff9`  |
| 1036   | No file              | `616cd1aeeff9`  |
| 1026   | No file              | `616cd1aeeff9`  |
| 1016   | No file              | `616cd1aeeff9`  |
| 1009   | No file              | `616cd1aeeff9`  |
| 1005   | No file              | `616cd1aeeff9`  |
| 1000   | No file              | `616cd1aeeff9`  |
| 998    | No file              | `616cd1aeeff9`  |
| 990    | No file              | `616cd1aeeff9`  |
| 979    | No file              | `616cd1aeeff9`  |
| 972    | No file              | `616cd1aeeff9`  |
| 963    | No file              | `616cd1aeeff9`  |
| 955    | No file              | `616cd1aeeff9`  |
| 946    | No file              | `616cd1aeeff9`  |
| 938    | No file              | `616cd1aeeff9`  |
| 927    | No file              | `616cd1aeeff9`  |
| 911    | No file              | `616cd1aeeff9`  |
| 904    | No file              | `616cd1aeeff9`  |
| 899    | No file              | `616cd1aeeff9`  |
| 894    | No file              | `616cd1aeeff9`  |
| 885    | No file              | `616cd1aeeff9`  |
| 879    | No file              | `616cd1aeeff9`  |
| 872    | No file              | `616cd1aeeff9`  |
| 864    | No file              | `616cd1aeeff9`  |
| 855    | No file              | `616cd1aeeff9`  |
| 853    | No file              | `616cd1aeeff9`  |
| 845    | No file              | `616cd1aeeff9`  |
| 837    | No file              | `616cd1aeeff9`  |
| 829    | No file              | `616cd1aeeff9`  |
| 822    | No file              | `616cd1aeeff9`  |
| 814    | No file              | `616cd1aeeff9`  |
| 805    | No file              | `616cd1aeeff9`  |
| 794    | No file              | `616cd1aeeff9`  |
| 787    | No file              | `616cd1aeeff9`  |
| 780    | No file              | `616cd1aeeff9`  |
| 771    | No file              | `616cd1aeeff9`  |
| 760    | No file              | `616cd1aeeff9`  |
| 748    | No file              | `616cd1aeeff9`  |
| 741    | No file              | `616cd1aeeff9`  |
| 736    | No file              | `616cd1aeeff9`  |
| 731    | No file              | `616cd1aeeff9`  |
| 723    | No file              | `616cd1aeeff9`  |
| 711    | No file              | `616cd1aeeff9`  |
| 707    | No file              | `616cd1aeeff9`  |
| 697    | No file              | `616cd1aeeff9`  |
| 689    | No file              | `616cd1aeeff9`  |
| 683    | No file              | `616cd1aeeff9`  |
| 678    | No file              | `616cd1aeeff9`  |
| 670    | No file              | `616cd1aeeff9`  |
| 661    | No file              | `616cd1aeeff9`  |
| 656    | No file              | `616cd1aeeff9`  |
| 652    | No file              | `616cd1aeeff9`  |
| 643    | No file              | `616cd1aeeff9`  |
| 637    | No file              | `616cd1aeeff9`  |
| 630    | No file              | `616cd1aeeff9`  |
| 627    | No file              | `616cd1aeeff9`  |
| 621    | No file              | `616cd1aeeff9`  |
| 617    | No file              | `616cd1aeeff9`  |
| 615    | No file              | `616cd1aeeff9`  |
| 606    | No file              | `616cd1aeeff9`  |
| 599    | No file              | `616cd1aeeff9`  |
| 592    | No file              | `616cd1aeeff9`  |
| 586    | No file              | `616cd1aeeff9`  |
| 577    | No file              | `616cd1aeeff9`  |
| 569    | No file              | `616cd1aeeff9`  |
| 561    | No file              | `616cd1aeeff9`  |
| 554    | No file              | `616cd1aeeff9`  |
| 542    | No file              | `616cd1aeeff9`  |
| 532    | No file              | `616cd1aeeff9`  |
| 531    | No file              | `616cd1aeeff9`  |
| 526    | No file              | `616cd1aeeff9`  |
| 521    | No file              | `616cd1aeeff9`  |
| 517    | No file              | `616cd1aeeff9`  |
| 510    | No file              | `616cd1aeeff9`  |
| 508    | No file              | `616cd1aeeff9`  |
| 504    | No file              | `616cd1aeeff9`  |
| 497    | No file              | `616cd1aeeff9`  |
| 491    | No file              | `616cd1aeeff9`  |
| 485    | No file              | `616cd1aeeff9`  |
| 478    | No file              | `616cd1aeeff9`  |
| 472    | No file              | `616cd1aeeff9`  |
| 466    | No file              | `616cd1aeeff9`  |
| 457    | No file              | `616cd1aeeff9`  |
| 452    | No file              | `616cd1aeeff9`  |
| 449    | No file              | `616cd1aeeff9`  |
| 435    | No file              | `616cd1aeeff9`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                               |
| --------------------- | -------- | -------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), skill names (LOC type 10) |

All multi-byte values are little-endian.

## Reward Sets

Client 3482; the names are LOC type 0. Row `0` gives the Determined
boxes, row `1` the Kindling and row `2` the Blazing ones, so "Determined"
below stands for the row's box name:

| List                | Sets 1 and 2                                | Sets 3 to 5                                  |
| ------------------- | ------------------------------------------- | -------------------------------------------- |
| `unknown_rewards_1` | Determined Triumph Reward (Tier 1, Tier 2)  | Determined Triumph Reward (Tier 3 to Tier 5); set 5 adds Combat Secret Book (M) x2 |
| `unknown_rewards_2` | Battlefield Honor (Battlefield Glory on row `2`) | The same                                |
| `unknown_rewards_3` | Gold Bar 1G x5                              | Medal of Glory x5                            |
| `unknown_rewards_4` | Determined Triumph Reward of Resilience     | Another item of the same name                |

`unknown_rewards` holds the Determined Resolve Reward and Combat Secret
Book (S) x2. The skill pairs are Glorious Combat, Life (Standard) and
(Basic) on row `0`, (Advanced) and (Standard) on row `1` and (Ultimate)
and (Superior) on row `2`: skills `58478, 58479`, `58477, 58478` and
`58475, 58476`.

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. The rows have the shape of
[`oceansiegereward.bss`](oceansiegereward_bss.md), whose names they
take: `item_id` names an item with a LOC type 0
name on all 69 rewards of client 3482, and `skill_key_1` and
`skill_key_2` name skills with a LOC type 10 name.

## Notes

- Clients 3002 and 3251 use Layout 1 of `oceansiegereward.bss`, one
  item per list with no counts (806 bytes, three rows); client 3474
  turns each list into a counted list. Client 2519 has 254-byte rows
  (782 bytes): the Layout 1 row without the two skill keys, a layout
  neither doc lists, so the doc check finds no layout for it. The file
  is not in the archives of clients 2637 and 2765.
- `unknown_04` is `A4 00 00 00` on every reward of client 3482, as in
  `oceansiegereward.bss`.
- The handler of `oceansiegereward.bss` (`_bss/oceansiegereward/`)
  previews this file: one row per reward item with its set, list and
  the row's two skills.

## Open Questions

### What the Lists Stand For

[`siegerewarddata.bss`](siegerewarddata_bss.md) names the reward slots
of a Node War tier after the `SiegeReward` sheet of client 1784: a
victory item, a defeat item, a liberation item, a count of medals and a
plus item. The lists of each set line up with them: the Triumph Reward
of `unknown_rewards_1` is the victory item, Battlefield Honor and Glory
of `unknown_rewards_2` are the plus items `siegerewarddata.bss` names
(`44392`, `44391`), five of the medal item (`2`, Gold Bar 1G) are in
`unknown_rewards_3`, and the Resolve Reward of `unknown_rewards` matches
its defeat items. The Triumph Reward of Resilience has no slot there,
and the item IDs of `siegerewarddata.bss` are other boxes, so the names
stay open.

### The u16 and the Two Skills

`unknown_00` is `0`, `1` and `2`, one per box name (Determined, Kindling,
Blazing), which fits the three land groups of `_eTerritoryGroupType` in
`panel_window_villagesiegemenu_all.luac` (client 3482). Which of the two
skills goes to whom is open.
