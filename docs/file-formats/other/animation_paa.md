# `*.paa` Animation Format

## Purpose

Animation clips under `character/motion/`: per bone a list of scale, rotation and translation keys with millisecond times. A clip names its bones by the `bone_id` name hashes of a [`.pab` skeleton](skeleton_pab.md); the keys are local transforms in that skeleton's frame. The Model tab of the browser plays a clip on its skeleton (`PAZ-Parser/par_animation.py`). Byte `0x04` of the `PAR ` header is `0x02`. On client 3483 there are 71,286 `.paa` files: 71,285 of version 2 and one of version 1, with 0 to 254 bones and 0.033 to 65.33 seconds each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                                                                     | Bytes     | Records                                                               | Row bytes |
| ------ | -------------- | ---------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------- | --------- |
| 1      | 3483 and later | `character/motion/6_object/t0093_the_outside_sink_0001/t0093_00_00_00_stand_idle_00.paa` | 88        | 2 Scale Key V1, 2 Rotation Key V1, 2 Translation Key V1               | 8         |
| 1      | 3483 and later | `character/motion/7_montower/m0130_redgoblinbuff_0003/m0130_00_00_00_stand_idle_00.paa`  | 26        | -                                                                     | -         |
| 1      | 3483 and later | `cs_calpheon_01_cob0003_effect_0138_004.paa`                                             | 662       | 76 Translation Key                                                    | 8         |
| 1      | 3483 and later | `cs_pedu2_4f_01_pdkl_00.paa`                                                             | 2,362,322 | 271 Scale Key, 189,998 Rotation Key, 57,301 Translation Key, 174 Node | 10        |
| 1      | 3483 and later | `pmyf_00_00_rh_riding_run_l_drift_dash_00.paa`                                           | 77,510    | 305 Scale Key, 6,067 Rotation Key, 1,543 Translation Key, 203 Node    | 10        |

| Layout | File                                                                                     | Known                | Unknown      |
| ------ | ---------------------------------------------------------------------------------------- | -------------------- | ------------ |
| 1      | `character/motion/6_object/t0093_the_outside_sink_0001/t0093_00_00_00_stand_idle_00.paa` | 78 B (88.6%)         | 10 B (11.4%) |
| 1      | `character/motion/7_montower/m0130_redgoblinbuff_0003/m0130_00_00_00_stand_idle_00.paa`  | 16 B (61.5%)         | 10 B (38.5%) |
| 1      | `cs_calpheon_01_cob0003_effect_0138_004.paa`                                             | 652 B (98.5%)        | 10 B (1.5%)  |
| 1      | `cs_pedu2_4f_01_pdkl_00.paa`                                                             | 2,362,312 B (100.0%) | 10 B (0.0%)  |
| 1      | `pmyf_00_00_rh_riding_run_l_drift_dash_00.paa`                                           | 77,500 B (100.0%)    | 10 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `bfa09d643c7d`  |
| 3482   | No file  | `bfa09d643c7d`  |
| 3474   | No file  | `bfa09d643c7d`  |
| 3473   | No file  | `bfa09d643c7d`  |
| 3464   | No file  | `bfa09d643c7d`  |
| 3458   | No file  | `bfa09d643c7d`  |
| 3454   | No file  | `bfa09d643c7d`  |
| 3444   | No file  | `bfa09d643c7d`  |
| 3435   | No file  | `bfa09d643c7d`  |
| 3426   | No file  | `bfa09d643c7d`  |
| 3418   | No file  | `bfa09d643c7d`  |
| 3412   | No file  | `bfa09d643c7d`  |
| 3402   | No file  | `bfa09d643c7d`  |
| 3396   | No file  | `bfa09d643c7d`  |
| 3387   | No file  | `bfa09d643c7d`  |
| 3381   | No file  | `bfa09d643c7d`  |
| 3373   | No file  | `bfa09d643c7d`  |
| 3364   | No file  | `bfa09d643c7d`  |
| 3356   | No file  | `bfa09d643c7d`  |
| 3349   | No file  | `bfa09d643c7d`  |
| 3342   | No file  | `bfa09d643c7d`  |
| 3335   | No file  | `bfa09d643c7d`  |
| 3326   | No file  | `bfa09d643c7d`  |
| 3321   | No file  | `bfa09d643c7d`  |
| 3314   | No file  | `bfa09d643c7d`  |
| 3303   | No file  | `bfa09d643c7d`  |
| 3302   | No file  | `bfa09d643c7d`  |
| 3293   | No file  | `bfa09d643c7d`  |
| 3283   | No file  | `bfa09d643c7d`  |
| 3275   | No file  | `bfa09d643c7d`  |
| 3267   | No file  | `bfa09d643c7d`  |
| 3258   | No file  | `bfa09d643c7d`  |
| 3251   | No file  | `bfa09d643c7d`  |
| 3242   | No file  | `bfa09d643c7d`  |
| 3235   | No file  | `bfa09d643c7d`  |
| 3229   | No file  | `bfa09d643c7d`  |
| 3212   | No file  | `bfa09d643c7d`  |
| 3203   | No file  | `bfa09d643c7d`  |
| 3193   | No file  | `bfa09d643c7d`  |
| 3186   | No file  | `bfa09d643c7d`  |
| 3177   | No file  | `bfa09d643c7d`  |
| 3169   | No file  | `bfa09d643c7d`  |
| 3158   | No file  | `bfa09d643c7d`  |
| 3151   | No file  | `bfa09d643c7d`  |
| 3144   | No file  | `bfa09d643c7d`  |
| 3133   | No file  | `bfa09d643c7d`  |
| 3125   | No file  | `bfa09d643c7d`  |
| 3118   | No file  | `bfa09d643c7d`  |
| 3111   | No file  | `bfa09d643c7d`  |
| 3103   | No file  | `bfa09d643c7d`  |
| 3095   | No file  | `bfa09d643c7d`  |
| 3086   | No file  | `bfa09d643c7d`  |
| 3072   | No file  | `bfa09d643c7d`  |
| 3062   | No file  | `bfa09d643c7d`  |
| 3052   | No file  | `bfa09d643c7d`  |
| 3045   | No file  | `bfa09d643c7d`  |
| 3037   | No file  | `bfa09d643c7d`  |
| 3030   | No file  | `bfa09d643c7d`  |
| 3021   | No file  | `bfa09d643c7d`  |
| 3012   | No file  | `bfa09d643c7d`  |
| 3002   | No file  | `bfa09d643c7d`  |
| 2995   | No file  | `bfa09d643c7d`  |
| 2987   | No file  | `bfa09d643c7d`  |
| 2978   | No file  | `bfa09d643c7d`  |
| 2970   | No file  | `bfa09d643c7d`  |
| 2959   | No file  | `bfa09d643c7d`  |
| 2951   | No file  | `bfa09d643c7d`  |
| 2942   | No file  | `bfa09d643c7d`  |
| 2935   | No file  | `bfa09d643c7d`  |
| 2932   | No file  | `bfa09d643c7d`  |
| 2923   | No file  | `bfa09d643c7d`  |
| 2919   | No file  | `bfa09d643c7d`  |
| 2907   | No file  | `bfa09d643c7d`  |
| 2900   | No file  | `bfa09d643c7d`  |
| 2891   | No file  | `bfa09d643c7d`  |
| 2882   | No file  | `bfa09d643c7d`  |
| 2872   | No file  | `bfa09d643c7d`  |
| 2863   | No file  | `bfa09d643c7d`  |
| 2855   | No file  | `bfa09d643c7d`  |
| 2849   | No file  | `bfa09d643c7d`  |
| 2844   | No file  | `bfa09d643c7d`  |
| 2834   | No file  | `bfa09d643c7d`  |
| 2825   | No file  | `bfa09d643c7d`  |
| 2819   | No file  | `bfa09d643c7d`  |
| 2811   | No file  | `bfa09d643c7d`  |
| 2803   | No file  | `bfa09d643c7d`  |
| 2794   | No file  | `bfa09d643c7d`  |
| 2783   | No file  | `bfa09d643c7d`  |
| 2774   | No file  | `bfa09d643c7d`  |
| 2765   | No file  | `bfa09d643c7d`  |
| 2756   | No file  | `bfa09d643c7d`  |
| 2750   | No file  | `bfa09d643c7d`  |
| 2743   | No file  | `bfa09d643c7d`  |
| 2736   | No file  | `bfa09d643c7d`  |
| 2726   | No file  | `bfa09d643c7d`  |
| 2717   | No file  | `bfa09d643c7d`  |
| 2709   | No file  | `bfa09d643c7d`  |
| 2703   | No file  | `bfa09d643c7d`  |
| 2695   | No file  | `bfa09d643c7d`  |
| 2684   | No file  | `bfa09d643c7d`  |
| 2672   | No file  | `bfa09d643c7d`  |
| 2665   | No file  | `bfa09d643c7d`  |
| 2657   | No file  | `bfa09d643c7d`  |
| 2649   | No file  | `bfa09d643c7d`  |
| 2644   | No file  | `bfa09d643c7d`  |
| 2637   | No file  | `bfa09d643c7d`  |
| 2629   | No file  | `bfa09d643c7d`  |
| 2619   | No file  | `bfa09d643c7d`  |
| 2612   | No file  | `bfa09d643c7d`  |
| 2606   | No file  | `bfa09d643c7d`  |
| 2602   | No file  | `bfa09d643c7d`  |
| 2601   | No file  | `bfa09d643c7d`  |
| 2592   | No file  | `bfa09d643c7d`  |
| 2583   | No file  | `bfa09d643c7d`  |
| 2575   | No file  | `bfa09d643c7d`  |
| 2567   | No file  | `bfa09d643c7d`  |
| 2560   | No file  | `bfa09d643c7d`  |
| 2553   | No file  | `bfa09d643c7d`  |
| 2545   | No file  | `bfa09d643c7d`  |
| 2538   | No file  | `bfa09d643c7d`  |
| 2529   | No file  | `bfa09d643c7d`  |
| 2519   | No file  | `bfa09d643c7d`  |
| 2513   | No file  | `bfa09d643c7d`  |
| 2510   | No file  | `bfa09d643c7d`  |
| 2507   | No file  | `bfa09d643c7d`  |
| 2503   | No file  | `bfa09d643c7d`  |
| 2498   | No file  | `bfa09d643c7d`  |
| 2492   | No file  | `bfa09d643c7d`  |
| 2487   | No file  | `bfa09d643c7d`  |
| 2480   | No file  | `bfa09d643c7d`  |
| 2474   | No file  | `bfa09d643c7d`  |
| 2468   | No file  | `bfa09d643c7d`  |
| 2460   | No file  | `bfa09d643c7d`  |
| 2453   | No file  | `bfa09d643c7d`  |
| 2444   | No file  | `bfa09d643c7d`  |
| 2438   | No file  | `bfa09d643c7d`  |
| 2434   | No file  | `bfa09d643c7d`  |
| 2429   | No file  | `bfa09d643c7d`  |
| 2421   | No file  | `bfa09d643c7d`  |
| 2414   | No file  | `bfa09d643c7d`  |
| 2407   | No file  | `bfa09d643c7d`  |
| 2401   | No file  | `bfa09d643c7d`  |
| 2397   | No file  | `bfa09d643c7d`  |
| 2393   | No file  | `bfa09d643c7d`  |
| 2384   | No file  | `bfa09d643c7d`  |
| 2378   | No file  | `bfa09d643c7d`  |
| 2372   | No file  | `bfa09d643c7d`  |
| 2358   | No file  | `bfa09d643c7d`  |
| 2352   | No file  | `bfa09d643c7d`  |
| 2347   | No file  | `bfa09d643c7d`  |
| 2343   | No file  | `bfa09d643c7d`  |
| 2335   | No file  | `bfa09d643c7d`  |
| 2327   | No file  | `bfa09d643c7d`  |
| 2324   | No file  | `bfa09d643c7d`  |
| 2319   | No file  | `bfa09d643c7d`  |
| 2313   | No file  | `bfa09d643c7d`  |
| 2308   | No file  | `bfa09d643c7d`  |
| 2302   | No file  | `bfa09d643c7d`  |
| 2295   | No file  | `bfa09d643c7d`  |
| 2290   | No file  | `bfa09d643c7d`  |
| 2284   | No file  | `bfa09d643c7d`  |
| 2276   | No file  | `bfa09d643c7d`  |
| 2269   | No file  | `bfa09d643c7d`  |
| 2259   | No file  | `bfa09d643c7d`  |
| 2250   | No file  | `bfa09d643c7d`  |
| 2243   | No file  | `bfa09d643c7d`  |
| 2235   | No file  | `bfa09d643c7d`  |
| 2229   | No file  | `bfa09d643c7d`  |
| 2224   | No file  | `bfa09d643c7d`  |
| 2218   | No file  | `bfa09d643c7d`  |
| 2215   | No file  | `bfa09d643c7d`  |
| 2207   | No file  | `bfa09d643c7d`  |
| 2203   | No file  | `bfa09d643c7d`  |
| 2196   | No file  | `bfa09d643c7d`  |
| 2192   | No file  | `bfa09d643c7d`  |
| 2189   | No file  | `bfa09d643c7d`  |
| 2183   | No file  | `bfa09d643c7d`  |
| 2179   | No file  | `bfa09d643c7d`  |
| 2171   | No file  | `bfa09d643c7d`  |
| 2163   | No file  | `bfa09d643c7d`  |
| 2156   | No file  | `bfa09d643c7d`  |
| 2151   | No file  | `bfa09d643c7d`  |
| 2147   | No file  | `bfa09d643c7d`  |
| 2142   | No file  | `bfa09d643c7d`  |
| 2138   | No file  | `bfa09d643c7d`  |
| 2134   | No file  | `bfa09d643c7d`  |
| 2130   | No file  | `bfa09d643c7d`  |
| 2122   | No file  | `bfa09d643c7d`  |
| 2107   | No file  | `bfa09d643c7d`  |
| 2098   | No file  | `bfa09d643c7d`  |
| 2089   | No file  | `bfa09d643c7d`  |
| 2081   | No file  | `bfa09d643c7d`  |
| 2073   | No file  | `bfa09d643c7d`  |
| 2067   | No file  | `bfa09d643c7d`  |
| 2063   | No file  | `bfa09d643c7d`  |
| 2059   | No file  | `bfa09d643c7d`  |
| 2052   | No file  | `bfa09d643c7d`  |
| 2044   | No file  | `bfa09d643c7d`  |
| 2039   | No file  | `bfa09d643c7d`  |
| 2032   | No file  | `bfa09d643c7d`  |
| 2025   | No file  | `bfa09d643c7d`  |
| 2011   | No file  | `bfa09d643c7d`  |
| 2005   | No file  | `bfa09d643c7d`  |
| 2000   | No file  | `bfa09d643c7d`  |
| 1996   | No file  | `bfa09d643c7d`  |
| 1991   | No file  | `bfa09d643c7d`  |
| 1985   | No file  | `bfa09d643c7d`  |
| 1980   | No file  | `bfa09d643c7d`  |
| 1969   | No file  | `bfa09d643c7d`  |
| 1964   | No file  | `bfa09d643c7d`  |
| 1958   | No file  | `bfa09d643c7d`  |
| 1950   | No file  | `bfa09d643c7d`  |
| 1945   | No file  | `bfa09d643c7d`  |
| 1937   | No file  | `bfa09d643c7d`  |
| 1933   | No file  | `bfa09d643c7d`  |
| 1927   | No file  | `bfa09d643c7d`  |
| 1921   | No file  | `bfa09d643c7d`  |
| 1914   | No file  | `bfa09d643c7d`  |
| 1908   | No file  | `bfa09d643c7d`  |
| 1897   | No file  | `bfa09d643c7d`  |
| 1892   | No file  | `bfa09d643c7d`  |
| 1886   | No file  | `bfa09d643c7d`  |
| 1881   | No file  | `bfa09d643c7d`  |
| 1871   | No file  | `bfa09d643c7d`  |
| 1866   | No file  | `bfa09d643c7d`  |
| 1862   | No file  | `bfa09d643c7d`  |
| 1854   | No file  | `bfa09d643c7d`  |
| 1846   | No file  | `bfa09d643c7d`  |
| 1838   | No file  | `bfa09d643c7d`  |
| 1832   | No file  | `bfa09d643c7d`  |
| 1826   | No file  | `bfa09d643c7d`  |
| 1822   | No file  | `bfa09d643c7d`  |
| 1818   | No file  | `bfa09d643c7d`  |
| 1804   | No file  | `bfa09d643c7d`  |
| 1794   | No file  | `bfa09d643c7d`  |
| 1790   | No file  | `bfa09d643c7d`  |
| 1784   | No file  | `bfa09d643c7d`  |
| 1774   | No file  | `bfa09d643c7d`  |
| 1771   | No file  | `bfa09d643c7d`  |
| 1762   | No file  | `bfa09d643c7d`  |
| 1759   | No file  | `bfa09d643c7d`  |
| 1754   | No file  | `bfa09d643c7d`  |
| 1749   | No file  | `bfa09d643c7d`  |
| 1743   | No file  | `bfa09d643c7d`  |
| 1737   | No file  | `bfa09d643c7d`  |
| 1731   | No file  | `bfa09d643c7d`  |
| 1725   | No file  | `bfa09d643c7d`  |
| 1717   | No file  | `bfa09d643c7d`  |
| 1710   | No file  | `bfa09d643c7d`  |
| 1704   | No file  | `bfa09d643c7d`  |
| 1698   | No file  | `bfa09d643c7d`  |
| 1690   | No file  | `bfa09d643c7d`  |
| 1685   | No file  | `bfa09d643c7d`  |
| 1680   | No file  | `bfa09d643c7d`  |
| 1674   | No file  | `bfa09d643c7d`  |
| 1668   | No file  | `bfa09d643c7d`  |
| 1659   | No file  | `bfa09d643c7d`  |
| 1649   | No file  | `bfa09d643c7d`  |
| 1642   | No file  | `bfa09d643c7d`  |
| 1636   | No file  | `bfa09d643c7d`  |
| 1628   | No file  | `bfa09d643c7d`  |
| 1622   | No file  | `bfa09d643c7d`  |
| 1614   | No file  | `bfa09d643c7d`  |
| 1608   | No file  | `bfa09d643c7d`  |
| 1602   | No file  | `bfa09d643c7d`  |
| 1598   | No file  | `bfa09d643c7d`  |
| 1594   | No file  | `bfa09d643c7d`  |
| 1590   | No file  | `bfa09d643c7d`  |
| 1587   | No file  | `bfa09d643c7d`  |
| 1584   | No file  | `bfa09d643c7d`  |
| 1579   | No file  | `bfa09d643c7d`  |
| 1572   | No file  | `bfa09d643c7d`  |
| 1565   | No file  | `bfa09d643c7d`  |
| 1559   | No file  | `bfa09d643c7d`  |
| 1554   | No file  | `bfa09d643c7d`  |
| 1547   | No file  | `bfa09d643c7d`  |
| 1537   | No file  | `bfa09d643c7d`  |
| 1529   | No file  | `bfa09d643c7d`  |
| 1524   | No file  | `bfa09d643c7d`  |
| 1519   | No file  | `bfa09d643c7d`  |
| 1509   | No file  | `bfa09d643c7d`  |
| 1506   | No file  | `bfa09d643c7d`  |
| 1504   | No file  | `bfa09d643c7d`  |
| 1500   | No file  | `bfa09d643c7d`  |
| 1493   | No file  | `bfa09d643c7d`  |
| 1489   | No file  | `bfa09d643c7d`  |
| 1485   | No file  | `bfa09d643c7d`  |
| 1481   | No file  | `bfa09d643c7d`  |
| 1474   | No file  | `bfa09d643c7d`  |
| 1466   | No file  | `bfa09d643c7d`  |
| 1462   | No file  | `bfa09d643c7d`  |
| 1459   | No file  | `bfa09d643c7d`  |
| 1453   | No file  | `bfa09d643c7d`  |
| 1450   | No file  | `bfa09d643c7d`  |
| 1445   | No file  | `bfa09d643c7d`  |
| 1439   | No file  | `bfa09d643c7d`  |
| 1433   | No file  | `bfa09d643c7d`  |
| 1430   | No file  | `bfa09d643c7d`  |
| 1426   | No file  | `bfa09d643c7d`  |
| 1421   | No file  | `bfa09d643c7d`  |
| 1417   | No file  | `bfa09d643c7d`  |
| 1416   | No file  | `bfa09d643c7d`  |
| 1409   | No file  | `bfa09d643c7d`  |
| 1405   | No file  | `bfa09d643c7d`  |
| 1401   | No file  | `bfa09d643c7d`  |
| 1396   | No file  | `bfa09d643c7d`  |
| 1391   | No file  | `bfa09d643c7d`  |
| 1390   | No file  | `bfa09d643c7d`  |
| 1386   | No file  | `bfa09d643c7d`  |
| 1381   | No file  | `bfa09d643c7d`  |
| 1379   | No file  | `bfa09d643c7d`  |
| 1372   | No file  | `bfa09d643c7d`  |
| 1366   | No file  | `bfa09d643c7d`  |
| 1364   | No file  | `bfa09d643c7d`  |
| 1363   | No file  | `bfa09d643c7d`  |
| 1360   | No file  | `bfa09d643c7d`  |
| 1358   | No file  | `bfa09d643c7d`  |
| 1355   | No file  | `bfa09d643c7d`  |
| 1351   | No file  | `bfa09d643c7d`  |
| 1348   | No file  | `bfa09d643c7d`  |
| 1346   | No file  | `bfa09d643c7d`  |
| 1341   | No file  | `bfa09d643c7d`  |
| 1340   | No file  | `bfa09d643c7d`  |
| 1338   | No file  | `bfa09d643c7d`  |
| 1335   | No file  | `bfa09d643c7d`  |
| 1333   | No file  | `bfa09d643c7d`  |
| 1329   | No file  | `bfa09d643c7d`  |
| 1327   | No file  | `bfa09d643c7d`  |
| 1324   | No file  | `bfa09d643c7d`  |
| 1321   | No file  | `bfa09d643c7d`  |
| 1319   | No file  | `bfa09d643c7d`  |
| 1318   | No file  | `bfa09d643c7d`  |
| 1316   | No file  | `bfa09d643c7d`  |
| 1313   | No file  | `bfa09d643c7d`  |
| 1311   | No file  | `bfa09d643c7d`  |
| 1309   | No file  | `bfa09d643c7d`  |
| 1304   | No file  | `bfa09d643c7d`  |
| 1292   | No file  | `bfa09d643c7d`  |
| 1286   | No file  | `bfa09d643c7d`  |
| 1280   | No file  | `bfa09d643c7d`  |
| 1276   | No file  | `bfa09d643c7d`  |
| 1267   | No file  | `bfa09d643c7d`  |
| 1261   | No file  | `bfa09d643c7d`  |
| 1256   | No file  | `bfa09d643c7d`  |
| 1250   | No file  | `bfa09d643c7d`  |
| 1246   | No file  | `bfa09d643c7d`  |
| 1239   | No file  | `bfa09d643c7d`  |
| 1230   | No file  | `bfa09d643c7d`  |
| 1226   | No file  | `bfa09d643c7d`  |
| 1220   | No file  | `bfa09d643c7d`  |
| 1217   | No file  | `bfa09d643c7d`  |
| 1211   | No file  | `bfa09d643c7d`  |
| 1210   | No file  | `bfa09d643c7d`  |
| 1208   | No file  | `bfa09d643c7d`  |
| 1203   | No file  | `bfa09d643c7d`  |
| 1197   | No file  | `bfa09d643c7d`  |
| 1194   | No file  | `bfa09d643c7d`  |
| 1192   | No file  | `bfa09d643c7d`  |
| 1187   | No file  | `bfa09d643c7d`  |
| 1183   | No file  | `bfa09d643c7d`  |
| 1177   | No file  | `bfa09d643c7d`  |
| 1173   | No file  | `bfa09d643c7d`  |
| 1167   | No file  | `bfa09d643c7d`  |
| 1164   | No file  | `bfa09d643c7d`  |
| 1156   | No file  | `bfa09d643c7d`  |
| 1149   | No file  | `bfa09d643c7d`  |
| 1144   | No file  | `bfa09d643c7d`  |
| 1137   | No file  | `bfa09d643c7d`  |
| 1132   | No file  | `bfa09d643c7d`  |
| 1127   | No file  | `bfa09d643c7d`  |
| 1122   | No file  | `bfa09d643c7d`  |
| 1118   | No file  | `bfa09d643c7d`  |
| 1114   | No file  | `bfa09d643c7d`  |
| 1109   | No file  | `bfa09d643c7d`  |
| 1102   | No file  | `bfa09d643c7d`  |
| 1096   | No file  | `bfa09d643c7d`  |
| 1088   | No file  | `bfa09d643c7d`  |
| 1081   | No file  | `bfa09d643c7d`  |
| 1076   | No file  | `bfa09d643c7d`  |
| 1069   | No file  | `bfa09d643c7d`  |
| 1064   | No file  | `bfa09d643c7d`  |
| 1058   | No file  | `bfa09d643c7d`  |
| 1051   | No file  | `bfa09d643c7d`  |
| 1044   | No file  | `bfa09d643c7d`  |
| 1036   | No file  | `bfa09d643c7d`  |
| 1026   | No file  | `bfa09d643c7d`  |
| 1016   | No file  | `bfa09d643c7d`  |
| 1009   | No file  | `bfa09d643c7d`  |
| 1005   | No file  | `bfa09d643c7d`  |
| 1000   | No file  | `bfa09d643c7d`  |
| 998    | No file  | `bfa09d643c7d`  |
| 990    | No file  | `bfa09d643c7d`  |
| 979    | No file  | `bfa09d643c7d`  |
| 972    | No file  | `bfa09d643c7d`  |
| 963    | No file  | `bfa09d643c7d`  |
| 955    | No file  | `bfa09d643c7d`  |
| 946    | No file  | `bfa09d643c7d`  |
| 938    | No file  | `bfa09d643c7d`  |
| 927    | No file  | `bfa09d643c7d`  |
| 911    | No file  | `bfa09d643c7d`  |
| 904    | No file  | `bfa09d643c7d`  |
| 899    | No file  | `bfa09d643c7d`  |
| 894    | No file  | `bfa09d643c7d`  |
| 885    | No file  | `bfa09d643c7d`  |
| 879    | No file  | `bfa09d643c7d`  |
| 872    | No file  | `bfa09d643c7d`  |
| 864    | No file  | `bfa09d643c7d`  |
| 855    | No file  | `bfa09d643c7d`  |
| 853    | No file  | `bfa09d643c7d`  |
| 845    | No file  | `bfa09d643c7d`  |
| 837    | No file  | `bfa09d643c7d`  |
| 829    | No file  | `bfa09d643c7d`  |
| 822    | No file  | `bfa09d643c7d`  |
| 814    | No file  | `bfa09d643c7d`  |
| 805    | No file  | `bfa09d643c7d`  |
| 794    | No file  | `bfa09d643c7d`  |
| 787    | No file  | `bfa09d643c7d`  |
| 780    | No file  | `bfa09d643c7d`  |
| 771    | No file  | `bfa09d643c7d`  |
| 760    | No file  | `bfa09d643c7d`  |
| 748    | No file  | `bfa09d643c7d`  |
| 741    | No file  | `bfa09d643c7d`  |
| 736    | No file  | `bfa09d643c7d`  |
| 731    | No file  | `bfa09d643c7d`  |
| 723    | No file  | `bfa09d643c7d`  |
| 711    | No file  | `bfa09d643c7d`  |
| 707    | No file  | `bfa09d643c7d`  |
| 697    | No file  | `bfa09d643c7d`  |
| 689    | No file  | `bfa09d643c7d`  |
| 683    | No file  | `bfa09d643c7d`  |
| 678    | No file  | `bfa09d643c7d`  |
| 670    | No file  | `bfa09d643c7d`  |
| 661    | No file  | `bfa09d643c7d`  |
| 656    | No file  | `bfa09d643c7d`  |
| 652    | No file  | `bfa09d643c7d`  |
| 643    | No file  | `bfa09d643c7d`  |
| 637    | No file  | `bfa09d643c7d`  |
| 630    | No file  | `bfa09d643c7d`  |
| 627    | No file  | `bfa09d643c7d`  |
| 621    | No file  | `bfa09d643c7d`  |
| 617    | No file  | `bfa09d643c7d`  |
| 615    | No file  | `bfa09d643c7d`  |
| 606    | No file  | `bfa09d643c7d`  |
| 599    | No file  | `bfa09d643c7d`  |
| 592    | No file  | `bfa09d643c7d`  |
| 586    | No file  | `bfa09d643c7d`  |
| 577    | No file  | `bfa09d643c7d`  |
| 569    | No file  | `bfa09d643c7d`  |
| 561    | No file  | `bfa09d643c7d`  |
| 554    | No file  | `bfa09d643c7d`  |
| 542    | No file  | `bfa09d643c7d`  |
| 532    | No file  | `bfa09d643c7d`  |
| 531    | No file  | `bfa09d643c7d`  |
| 526    | No file  | `bfa09d643c7d`  |
| 521    | No file  | `bfa09d643c7d`  |
| 517    | No file  | `bfa09d643c7d`  |
| 510    | No file  | `bfa09d643c7d`  |
| 508    | No file  | `bfa09d643c7d`  |
| 504    | No file  | `bfa09d643c7d`  |
| 497    | No file  | `bfa09d643c7d`  |
| 491    | No file  | `bfa09d643c7d`  |
| 485    | No file  | `bfa09d643c7d`  |
| 478    | No file  | `bfa09d643c7d`  |
| 472    | No file  | `bfa09d643c7d`  |
| 466    | No file  | `bfa09d643c7d`  |
| 457    | No file  | `bfa09d643c7d`  |
| 452    | No file  | `bfa09d643c7d`  |
| 449    | No file  | `bfa09d643c7d`  |
| 435    | No file  | `bfa09d643c7d`  |

<!-- versions:end -->

## Companion Files

None read. The skeleton the bone ids belong to is a `.pab` file that the clip does not name.

## Layout 1

### File Layout

| Offset          | Type                              | Field         | Notes |
| --------------- | --------------------------------- | ------------- | ----- |
| `+0x00`         | char[4]                           | magic         | ASCII `PAR ` |
| `+0x04`         | u8                                | kind          | `0x02` on every `.paa` |
| `+0x05`         | u8                                | version       | `2` on 71,285 of 71,286 files (client 3483), `1` on one; version 1 picks Node V1 |
| `+0x06`         | bytes[10]                         | unknown_06    | `00 01 02 03 04 05 06 07 08 09` on 71,078 files (client 3483); `00 00 01 02 03 04 05 06 07 08` on 208 |
| `+0x10`         | u16                               | node_count    | `0` on 913 files (client 3483), up to `254` |
| `+0x12`         | f32                               | duration      | `_animationTime`, seconds; the last key's `time` in seconds on 69,633 of the 70,373 clips with nodes (client 3483), later than it on the rest |
| `+0x16`         | u32                               | key_data_size | `_dataSizeInByte`: the bytes of every key in the file, ids and counts left out, on all 71,286 files |
| `+0x1A`         | Node[node_count] if version != 1  | nodes         |  |
| `nodes+0x00`    | Node V1[node_count] if version = 1 | nodes_v1     |  |

### Node (variable: 10 bytes + keys)

The 2016 `PACharacterAnimationNode`.

| Offset                | Type                                     | Field                 | Notes |
| --------------------- | ---------------------------------------- | --------------------- | ----- |
| `+0x00`               | u32                                      | bone_id               | `_hash`: a `.pab` `bone_id` on 262,385 of 263,395 nodes in 2,000 sampled clips (client 3483) |
| `+0x04`               | u16                                      | scale_key_count       | `_num_s_keys` |
| `+0x06`               | Scale Key[scale_key_count]               | scale_keys            |  |
| `scale_keys+0x00`     | u16                                      | rotation_key_count    | `_num_r_keys` |
| `scale_keys+0x02`     | Rotation Key[rotation_key_count]         | rotation_keys         |  |
| `rotation_keys+0x00`  | u16                                      | translation_key_count | `_num_t_keys` |
| `rotation_keys+0x02`  | Translation Key[translation_key_count]   | translation_keys      |  |

### Scale Key (8 bytes)

The 2016 `s_key`.

| Offset  | Type   | Field | Notes |
| ------- | ------ | ----- | ----- |
| `+0x00` | u16    | time  | `_t`, milliseconds; the first key of every list is `0` and the times rise in every list of the 2,000 sampled clips |
| `+0x02` | f16[3] | scale | `_v`; `1.0` on 97.6% of the sampled values |

### Rotation Key (10 bytes)

The 2016 `r_key`.

| Offset  | Type   | Field    | Notes |
| ------- | ------ | -------- | ----- |
| `+0x00` | u16    | time     | As in Scale Key |
| `+0x02` | f16[4] | rotation | `_v`, a unit quaternion x, y, z, w relative to the parent bone |

### Translation Key (8 bytes)

The 2016 `t_key`.

| Offset  | Type   | Field       | Notes |
| ------- | ------ | ----------- | ----- |
| `+0x00` | u16    | time        | As in Scale Key |
| `+0x02` | f16[3] | translation | `_v`, centimetres relative to the parent bone |

### Node V1 (variable: 10 bytes + keys)

Version 1: the same sizes with i16 values.

| Offset                | Type                                      | Field                 | Notes |
| --------------------- | ----------------------------------------- | --------------------- | ----- |
| `+0x00`               | u32                                       | bone_id               | As in Node |
| `+0x04`               | u16                                       | scale_key_count       | As in Node |
| `+0x06`               | Scale Key V1[scale_key_count]             | scale_keys            |  |
| `scale_keys+0x00`     | u16                                       | rotation_key_count    | As in Node |
| `scale_keys+0x02`     | Rotation Key V1[rotation_key_count]       | rotation_keys         |  |
| `rotation_keys+0x00`  | u16                                       | translation_key_count | As in Node |
| `rotation_keys+0x02`  | Translation Key V1[translation_key_count] | translation_keys      |  |

### Scale Key V1 (8 bytes)

| Offset  | Type   | Field | Notes |
| ------- | ------ | ----- | ----- |
| `+0x00` | u16    | time  | As in Scale Key |
| `+0x02` | i16[3] | scale | `1000` where version 2 holds `1.0` |

### Rotation Key V1 (10 bytes)

| Offset  | Type   | Field    | Notes |
| ------- | ------ | -------- | ----- |
| `+0x00` | u16    | time     | As in Scale Key |
| `+0x02` | i16[4] | rotation | `16384, -16384, 16384, -16384` in the one file: a unit quaternion over 32,768 |

### Translation Key V1 (8 bytes)

| Offset  | Type   | Field       | Notes |
| ------- | ------ | ----------- | ----- |
| `+0x00` | u16    | time        | As in Scale Key |
| `+0x02` | i16[3] | translation | `0` in the one file, so its scale does not show |

## Finding a Clip's Skeleton

A clip names no skeleton. The motion folders mirror the model folders by their first two levels: the clips under `character/motion/1_pc/17_psw/` belong with the skeletons under `character/model/1_pc/17_psw/`. In 2,000 sampled clips (client 3483), 1,845 have a `.pab` that holds every bone id they name, and for 1,650 of them such a skeleton sits under the mirrored model folder. A mirrored folder also holds clips of other skeletons (pets, mounts, gear), so the browser takes the `.pab` under it that holds the most of the clip's ids.

## Notes

- Every `.paa` on client 3483 walks to its last byte by this layout (71,286 files). The version 1 file is `character/motion/6_object/t0093_the_outside_sink_0001/t0093_00_00_00_stand_idle_00.paa`.
- The 2016 loader, `PACharacterAnimation::loadAnimationData`, accepts `kind` `2` with `version` `2` only. It reads `node_count`, `duration` into `_animationTime` (a negative value becomes `0`), `key_data_size` into `_dataSizeInByte` (the size of the key buffer it allocates), then per node `bone_id` and the three counted lists, each key copied as is.
- The keys are local transforms of the skeleton's bones: in 500 sampled clips, matched to the `.pab` holding most of their bone ids, the first rotation key equals the bone's `rotation` on 20,690 of 65,454 nodes (309 when read w first) and the first translation key its `translation` in centimetres on 39,501.
- sibercat/PAZ-Unpacker (MIT) gave the first reading of the node and key layout.

## Open Questions

### `unknown_06`

The same ten bytes as `unknown_06` of [`skeleton_pab.md`](skeleton_pab.md), where the 2016 loader fills its header buffer with `0` to `9` before it reads the file. 208 clips hold `00 00 01 02 03 04 05 06 07 08`.
