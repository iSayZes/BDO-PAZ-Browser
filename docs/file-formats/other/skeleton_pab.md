# `*.pab` Skeleton Format

## Purpose

Bone hierarchies of the skinned meshes under `character/model/`: per bone its name, parent, bind pose matrices and local scale, rotation and translation, then optional collision shapes and constraint axes, and after the bones a list of bone volumes. A `.pac` mesh names bones by `bone_id` in its `bone_palette` (see [`mesh_pac.md`](mesh_pac.md)); the skeleton holding those ids is a `.pab` file in the mesh's folder or a folder above it (see Finding a Mesh's Skeleton). The Model tab of the browser draws the bones and poses `.pac` meshes on them (`PAZ-Parser/par_skeleton.py`). Byte `0x04` of the `PAR ` header is `0x01`. On client 3483 there are 2,007 `.pab` files: 1 of version 2, 970 of version 3 and 1,036 of version 4, with 1 to 256 bones each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                               | Bytes   | Records                                                           | Row bytes                    |
| ------ | -------------- | -------------------------------------------------- | ------- | ----------------------------------------------------------------- | ---------------------------- |
| 1      | 3483 and later | `c0008_01.pab`                                     | 334     | 1 Bone                                                            | 314                          |
| 1      | 3483 and later | `character/model/4_riding/r0009_wagons/prw_01.pab` | 20,930  | 58 Bone, 3 Dynamic Shape, 5 Constraint Axis                       | 312 to 535, 329 on average   |
| 1      | 3483 and later | `character/model/4_riding/r0010_wagonm/prw_01.pab` | 116,186 | 221 Bone V4, 19 Dynamic Shape, 22 Typed Shape, 23 Constraint Axis | 312 to 4,827, 517 on average |
| 1      | 3483 and later | `m0065_01.pab`                                     | 9,219   | 26 Bone V4, 14 Typed Shape, 14 Constraint Axis                    | 313 to 385, 354 on average   |
| 1      | 3483 and later | `m0099_01.pab`                                     | 38,106  | 121 Bone                                                          | 314 to 333, 315 on average   |
| 1      | 3483 and later | `m0428_01.pab`                                     | 58,919  | 186 Bone V4                                                       | 312 to 323, 316 on average   |
| 1      | 3483 and later | `pdw_01.pab`                                       | 74,474  | 230 Bone V4, 4 Typed Shape, 4 Constraint Axis                     | 312 to 373, 324 on average   |
| 1      | 3483 and later | `t0002_05.pab`                                     | 414     | 1 Bone, 1 Bone Volume                                             | 312                          |
| 1      | 3483 and later | `t0303_event_xmas_bigsnowman_0001.pab`             | 1,247   | 1 Bone V4, 1 Dynamic Shape, 1 Bone Volume                         | 313                          |
| 1      | 3483 and later | `t0311_01.pab`                                     | 526     | 1 Bone V4, 1 Dynamic Shape, 1 Bone Volume                         | 312                          |

| Layout | File                                               | Known              | Unknown     |
| ------ | -------------------------------------------------- | ------------------ | ----------- |
| 1      | `c0008_01.pab`                                     | 324 B (97.0%)      | 10 B (3.0%) |
| 1      | `character/model/4_riding/r0009_wagons/prw_01.pab` | 20,920 B (100.0%)  | 10 B (0.0%) |
| 1      | `character/model/4_riding/r0010_wagonm/prw_01.pab` | 116,140 B (100.0%) | 46 B (0.0%) |
| 1      | `m0065_01.pab`                                     | 9,209 B (99.9%)    | 10 B (0.1%) |
| 1      | `m0099_01.pab`                                     | 38,096 B (100.0%)  | 10 B (0.0%) |
| 1      | `m0428_01.pab`                                     | 58,909 B (100.0%)  | 10 B (0.0%) |
| 1      | `pdw_01.pab`                                       | 74,448 B (100.0%)  | 26 B (0.0%) |
| 1      | `t0002_05.pab`                                     | 404 B (97.6%)      | 10 B (2.4%) |
| 1      | `t0303_event_xmas_bigsnowman_0001.pab`             | 1,237 B (99.2%)    | 10 B (0.8%) |
| 1      | `t0311_01.pab`                                     | 516 B (98.1%)      | 10 B (1.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `4b97b1b4989a`  |
| 3482   | No file  | `4b97b1b4989a`  |
| 3474   | No file  | `4b97b1b4989a`  |
| 3473   | No file  | `4b97b1b4989a`  |
| 3464   | No file  | `4b97b1b4989a`  |
| 3458   | No file  | `4b97b1b4989a`  |
| 3454   | No file  | `4b97b1b4989a`  |
| 3444   | No file  | `4b97b1b4989a`  |
| 3435   | No file  | `4b97b1b4989a`  |
| 3426   | No file  | `4b97b1b4989a`  |
| 3418   | No file  | `4b97b1b4989a`  |
| 3412   | No file  | `4b97b1b4989a`  |
| 3402   | No file  | `4b97b1b4989a`  |
| 3396   | No file  | `4b97b1b4989a`  |
| 3387   | No file  | `4b97b1b4989a`  |
| 3381   | No file  | `4b97b1b4989a`  |
| 3373   | No file  | `4b97b1b4989a`  |
| 3364   | No file  | `4b97b1b4989a`  |
| 3356   | No file  | `4b97b1b4989a`  |
| 3349   | No file  | `4b97b1b4989a`  |
| 3342   | No file  | `4b97b1b4989a`  |
| 3335   | No file  | `4b97b1b4989a`  |
| 3326   | No file  | `4b97b1b4989a`  |
| 3321   | No file  | `4b97b1b4989a`  |
| 3314   | No file  | `4b97b1b4989a`  |
| 3303   | No file  | `4b97b1b4989a`  |
| 3302   | No file  | `4b97b1b4989a`  |
| 3293   | No file  | `4b97b1b4989a`  |
| 3283   | No file  | `4b97b1b4989a`  |
| 3275   | No file  | `4b97b1b4989a`  |
| 3267   | No file  | `4b97b1b4989a`  |
| 3258   | No file  | `4b97b1b4989a`  |
| 3251   | No file  | `4b97b1b4989a`  |
| 3242   | No file  | `4b97b1b4989a`  |
| 3235   | No file  | `4b97b1b4989a`  |
| 3229   | No file  | `4b97b1b4989a`  |
| 3212   | No file  | `4b97b1b4989a`  |
| 3203   | No file  | `4b97b1b4989a`  |
| 3193   | No file  | `4b97b1b4989a`  |
| 3186   | No file  | `4b97b1b4989a`  |
| 3177   | No file  | `4b97b1b4989a`  |
| 3169   | No file  | `4b97b1b4989a`  |
| 3158   | No file  | `4b97b1b4989a`  |
| 3151   | No file  | `4b97b1b4989a`  |
| 3144   | No file  | `4b97b1b4989a`  |
| 3133   | No file  | `4b97b1b4989a`  |
| 3125   | No file  | `4b97b1b4989a`  |
| 3118   | No file  | `4b97b1b4989a`  |
| 3111   | No file  | `4b97b1b4989a`  |
| 3103   | No file  | `4b97b1b4989a`  |
| 3095   | No file  | `4b97b1b4989a`  |
| 3086   | No file  | `4b97b1b4989a`  |
| 3072   | No file  | `4b97b1b4989a`  |
| 3062   | No file  | `4b97b1b4989a`  |
| 3052   | No file  | `4b97b1b4989a`  |
| 3045   | No file  | `4b97b1b4989a`  |
| 3037   | No file  | `4b97b1b4989a`  |
| 3030   | No file  | `4b97b1b4989a`  |
| 3021   | No file  | `4b97b1b4989a`  |
| 3012   | No file  | `4b97b1b4989a`  |
| 3002   | No file  | `4b97b1b4989a`  |
| 2995   | No file  | `4b97b1b4989a`  |
| 2987   | No file  | `4b97b1b4989a`  |
| 2978   | No file  | `4b97b1b4989a`  |
| 2970   | No file  | `4b97b1b4989a`  |
| 2959   | No file  | `4b97b1b4989a`  |
| 2951   | No file  | `4b97b1b4989a`  |
| 2942   | No file  | `4b97b1b4989a`  |
| 2935   | No file  | `4b97b1b4989a`  |
| 2932   | No file  | `4b97b1b4989a`  |
| 2923   | No file  | `4b97b1b4989a`  |
| 2919   | No file  | `4b97b1b4989a`  |
| 2907   | No file  | `4b97b1b4989a`  |
| 2900   | No file  | `4b97b1b4989a`  |
| 2891   | No file  | `4b97b1b4989a`  |
| 2882   | No file  | `4b97b1b4989a`  |
| 2872   | No file  | `4b97b1b4989a`  |
| 2863   | No file  | `4b97b1b4989a`  |
| 2855   | No file  | `4b97b1b4989a`  |
| 2849   | No file  | `4b97b1b4989a`  |
| 2844   | No file  | `4b97b1b4989a`  |
| 2834   | No file  | `4b97b1b4989a`  |
| 2825   | No file  | `4b97b1b4989a`  |
| 2819   | No file  | `4b97b1b4989a`  |
| 2811   | No file  | `4b97b1b4989a`  |
| 2803   | No file  | `4b97b1b4989a`  |
| 2794   | No file  | `4b97b1b4989a`  |
| 2783   | No file  | `4b97b1b4989a`  |
| 2774   | No file  | `4b97b1b4989a`  |
| 2765   | No file  | `4b97b1b4989a`  |
| 2756   | No file  | `4b97b1b4989a`  |
| 2750   | No file  | `4b97b1b4989a`  |
| 2743   | No file  | `4b97b1b4989a`  |
| 2736   | No file  | `4b97b1b4989a`  |
| 2726   | No file  | `4b97b1b4989a`  |
| 2717   | No file  | `4b97b1b4989a`  |
| 2709   | No file  | `4b97b1b4989a`  |
| 2703   | No file  | `4b97b1b4989a`  |
| 2695   | No file  | `4b97b1b4989a`  |
| 2684   | No file  | `4b97b1b4989a`  |
| 2672   | No file  | `4b97b1b4989a`  |
| 2665   | No file  | `4b97b1b4989a`  |
| 2657   | No file  | `4b97b1b4989a`  |
| 2649   | No file  | `4b97b1b4989a`  |
| 2644   | No file  | `4b97b1b4989a`  |
| 2637   | No file  | `4b97b1b4989a`  |
| 2629   | No file  | `4b97b1b4989a`  |
| 2619   | No file  | `4b97b1b4989a`  |
| 2612   | No file  | `4b97b1b4989a`  |
| 2606   | No file  | `4b97b1b4989a`  |
| 2602   | No file  | `4b97b1b4989a`  |
| 2601   | No file  | `4b97b1b4989a`  |
| 2592   | No file  | `4b97b1b4989a`  |
| 2583   | No file  | `4b97b1b4989a`  |
| 2575   | No file  | `4b97b1b4989a`  |
| 2567   | No file  | `4b97b1b4989a`  |
| 2560   | No file  | `4b97b1b4989a`  |
| 2553   | No file  | `4b97b1b4989a`  |
| 2545   | No file  | `4b97b1b4989a`  |
| 2538   | No file  | `4b97b1b4989a`  |
| 2529   | No file  | `4b97b1b4989a`  |
| 2519   | No file  | `4b97b1b4989a`  |
| 2513   | No file  | `4b97b1b4989a`  |
| 2510   | No file  | `4b97b1b4989a`  |
| 2507   | No file  | `4b97b1b4989a`  |
| 2503   | No file  | `4b97b1b4989a`  |
| 2498   | No file  | `4b97b1b4989a`  |
| 2492   | No file  | `4b97b1b4989a`  |
| 2487   | No file  | `4b97b1b4989a`  |
| 2480   | No file  | `4b97b1b4989a`  |
| 2474   | No file  | `4b97b1b4989a`  |
| 2468   | No file  | `4b97b1b4989a`  |
| 2460   | No file  | `4b97b1b4989a`  |
| 2453   | No file  | `4b97b1b4989a`  |
| 2444   | No file  | `4b97b1b4989a`  |
| 2438   | No file  | `4b97b1b4989a`  |
| 2434   | No file  | `4b97b1b4989a`  |
| 2429   | No file  | `4b97b1b4989a`  |
| 2421   | No file  | `4b97b1b4989a`  |
| 2414   | No file  | `4b97b1b4989a`  |
| 2407   | No file  | `4b97b1b4989a`  |
| 2401   | No file  | `4b97b1b4989a`  |
| 2397   | No file  | `4b97b1b4989a`  |
| 2393   | No file  | `4b97b1b4989a`  |
| 2384   | No file  | `4b97b1b4989a`  |
| 2378   | No file  | `4b97b1b4989a`  |
| 2372   | No file  | `4b97b1b4989a`  |
| 2358   | No file  | `4b97b1b4989a`  |
| 2352   | No file  | `4b97b1b4989a`  |
| 2347   | No file  | `4b97b1b4989a`  |
| 2343   | No file  | `4b97b1b4989a`  |
| 2335   | No file  | `4b97b1b4989a`  |
| 2327   | No file  | `4b97b1b4989a`  |
| 2324   | No file  | `4b97b1b4989a`  |
| 2319   | No file  | `4b97b1b4989a`  |
| 2313   | No file  | `4b97b1b4989a`  |
| 2308   | No file  | `4b97b1b4989a`  |
| 2302   | No file  | `4b97b1b4989a`  |
| 2295   | No file  | `4b97b1b4989a`  |
| 2290   | No file  | `4b97b1b4989a`  |
| 2284   | No file  | `4b97b1b4989a`  |
| 2276   | No file  | `4b97b1b4989a`  |
| 2269   | No file  | `4b97b1b4989a`  |
| 2259   | No file  | `4b97b1b4989a`  |
| 2250   | No file  | `4b97b1b4989a`  |
| 2243   | No file  | `4b97b1b4989a`  |
| 2235   | No file  | `4b97b1b4989a`  |
| 2229   | No file  | `4b97b1b4989a`  |
| 2224   | No file  | `4b97b1b4989a`  |
| 2218   | No file  | `4b97b1b4989a`  |
| 2215   | No file  | `4b97b1b4989a`  |
| 2207   | No file  | `4b97b1b4989a`  |
| 2203   | No file  | `4b97b1b4989a`  |
| 2196   | No file  | `4b97b1b4989a`  |
| 2192   | No file  | `4b97b1b4989a`  |
| 2189   | No file  | `4b97b1b4989a`  |
| 2183   | No file  | `4b97b1b4989a`  |
| 2179   | No file  | `4b97b1b4989a`  |
| 2171   | No file  | `4b97b1b4989a`  |
| 2163   | No file  | `4b97b1b4989a`  |
| 2156   | No file  | `4b97b1b4989a`  |
| 2151   | No file  | `4b97b1b4989a`  |
| 2147   | No file  | `4b97b1b4989a`  |
| 2142   | No file  | `4b97b1b4989a`  |
| 2138   | No file  | `4b97b1b4989a`  |
| 2134   | No file  | `4b97b1b4989a`  |
| 2130   | No file  | `4b97b1b4989a`  |
| 2122   | No file  | `4b97b1b4989a`  |
| 2107   | No file  | `4b97b1b4989a`  |
| 2098   | No file  | `4b97b1b4989a`  |
| 2089   | No file  | `4b97b1b4989a`  |
| 2081   | No file  | `4b97b1b4989a`  |
| 2073   | No file  | `4b97b1b4989a`  |
| 2067   | No file  | `4b97b1b4989a`  |
| 2063   | No file  | `4b97b1b4989a`  |
| 2059   | No file  | `4b97b1b4989a`  |
| 2052   | No file  | `4b97b1b4989a`  |
| 2044   | No file  | `4b97b1b4989a`  |
| 2039   | No file  | `4b97b1b4989a`  |
| 2032   | No file  | `4b97b1b4989a`  |
| 2025   | No file  | `4b97b1b4989a`  |
| 2011   | No file  | `4b97b1b4989a`  |
| 2005   | No file  | `4b97b1b4989a`  |
| 2000   | No file  | `4b97b1b4989a`  |
| 1996   | No file  | `4b97b1b4989a`  |
| 1991   | No file  | `4b97b1b4989a`  |
| 1985   | No file  | `4b97b1b4989a`  |
| 1980   | No file  | `4b97b1b4989a`  |
| 1969   | No file  | `4b97b1b4989a`  |
| 1964   | No file  | `4b97b1b4989a`  |
| 1958   | No file  | `4b97b1b4989a`  |
| 1950   | No file  | `4b97b1b4989a`  |
| 1945   | No file  | `4b97b1b4989a`  |
| 1937   | No file  | `4b97b1b4989a`  |
| 1933   | No file  | `4b97b1b4989a`  |
| 1927   | No file  | `4b97b1b4989a`  |
| 1921   | No file  | `4b97b1b4989a`  |
| 1914   | No file  | `4b97b1b4989a`  |
| 1908   | No file  | `4b97b1b4989a`  |
| 1897   | No file  | `4b97b1b4989a`  |
| 1892   | No file  | `4b97b1b4989a`  |
| 1886   | No file  | `4b97b1b4989a`  |
| 1881   | No file  | `4b97b1b4989a`  |
| 1871   | No file  | `4b97b1b4989a`  |
| 1866   | No file  | `4b97b1b4989a`  |
| 1862   | No file  | `4b97b1b4989a`  |
| 1854   | No file  | `4b97b1b4989a`  |
| 1846   | No file  | `4b97b1b4989a`  |
| 1838   | No file  | `4b97b1b4989a`  |
| 1832   | No file  | `4b97b1b4989a`  |
| 1826   | No file  | `4b97b1b4989a`  |
| 1822   | No file  | `4b97b1b4989a`  |
| 1818   | No file  | `4b97b1b4989a`  |
| 1804   | No file  | `4b97b1b4989a`  |
| 1794   | No file  | `4b97b1b4989a`  |
| 1790   | No file  | `4b97b1b4989a`  |
| 1784   | No file  | `4b97b1b4989a`  |
| 1774   | No file  | `4b97b1b4989a`  |
| 1771   | No file  | `4b97b1b4989a`  |
| 1762   | No file  | `4b97b1b4989a`  |
| 1759   | No file  | `4b97b1b4989a`  |
| 1754   | No file  | `4b97b1b4989a`  |
| 1749   | No file  | `4b97b1b4989a`  |
| 1743   | No file  | `4b97b1b4989a`  |
| 1737   | No file  | `4b97b1b4989a`  |
| 1731   | No file  | `4b97b1b4989a`  |
| 1725   | No file  | `4b97b1b4989a`  |
| 1717   | No file  | `4b97b1b4989a`  |
| 1710   | No file  | `4b97b1b4989a`  |
| 1704   | No file  | `4b97b1b4989a`  |
| 1698   | No file  | `4b97b1b4989a`  |
| 1690   | No file  | `4b97b1b4989a`  |
| 1685   | No file  | `4b97b1b4989a`  |
| 1680   | No file  | `4b97b1b4989a`  |
| 1674   | No file  | `4b97b1b4989a`  |
| 1668   | No file  | `4b97b1b4989a`  |
| 1659   | No file  | `4b97b1b4989a`  |
| 1649   | No file  | `4b97b1b4989a`  |
| 1642   | No file  | `4b97b1b4989a`  |
| 1636   | No file  | `4b97b1b4989a`  |
| 1628   | No file  | `4b97b1b4989a`  |
| 1622   | No file  | `4b97b1b4989a`  |
| 1614   | No file  | `4b97b1b4989a`  |
| 1608   | No file  | `4b97b1b4989a`  |
| 1602   | No file  | `4b97b1b4989a`  |
| 1598   | No file  | `4b97b1b4989a`  |
| 1594   | No file  | `4b97b1b4989a`  |
| 1590   | No file  | `4b97b1b4989a`  |
| 1587   | No file  | `4b97b1b4989a`  |
| 1584   | No file  | `4b97b1b4989a`  |
| 1579   | No file  | `4b97b1b4989a`  |
| 1572   | No file  | `4b97b1b4989a`  |
| 1565   | No file  | `4b97b1b4989a`  |
| 1559   | No file  | `4b97b1b4989a`  |
| 1554   | No file  | `4b97b1b4989a`  |
| 1547   | No file  | `4b97b1b4989a`  |
| 1537   | No file  | `4b97b1b4989a`  |
| 1529   | No file  | `4b97b1b4989a`  |
| 1524   | No file  | `4b97b1b4989a`  |
| 1519   | No file  | `4b97b1b4989a`  |
| 1509   | No file  | `4b97b1b4989a`  |
| 1506   | No file  | `4b97b1b4989a`  |
| 1504   | No file  | `4b97b1b4989a`  |
| 1500   | No file  | `4b97b1b4989a`  |
| 1493   | No file  | `4b97b1b4989a`  |
| 1489   | No file  | `4b97b1b4989a`  |
| 1485   | No file  | `4b97b1b4989a`  |
| 1481   | No file  | `4b97b1b4989a`  |
| 1474   | No file  | `4b97b1b4989a`  |
| 1466   | No file  | `4b97b1b4989a`  |
| 1462   | No file  | `4b97b1b4989a`  |
| 1459   | No file  | `4b97b1b4989a`  |
| 1453   | No file  | `4b97b1b4989a`  |
| 1450   | No file  | `4b97b1b4989a`  |
| 1445   | No file  | `4b97b1b4989a`  |
| 1439   | No file  | `4b97b1b4989a`  |
| 1433   | No file  | `4b97b1b4989a`  |
| 1430   | No file  | `4b97b1b4989a`  |
| 1426   | No file  | `4b97b1b4989a`  |
| 1421   | No file  | `4b97b1b4989a`  |
| 1417   | No file  | `4b97b1b4989a`  |
| 1416   | No file  | `4b97b1b4989a`  |
| 1409   | No file  | `4b97b1b4989a`  |
| 1405   | No file  | `4b97b1b4989a`  |
| 1401   | No file  | `4b97b1b4989a`  |
| 1396   | No file  | `4b97b1b4989a`  |
| 1391   | No file  | `4b97b1b4989a`  |
| 1390   | No file  | `4b97b1b4989a`  |
| 1386   | No file  | `4b97b1b4989a`  |
| 1381   | No file  | `4b97b1b4989a`  |
| 1379   | No file  | `4b97b1b4989a`  |
| 1372   | No file  | `4b97b1b4989a`  |
| 1366   | No file  | `4b97b1b4989a`  |
| 1364   | No file  | `4b97b1b4989a`  |
| 1363   | No file  | `4b97b1b4989a`  |
| 1360   | No file  | `4b97b1b4989a`  |
| 1358   | No file  | `4b97b1b4989a`  |
| 1355   | No file  | `4b97b1b4989a`  |
| 1351   | No file  | `4b97b1b4989a`  |
| 1348   | No file  | `4b97b1b4989a`  |
| 1346   | No file  | `4b97b1b4989a`  |
| 1341   | No file  | `4b97b1b4989a`  |
| 1340   | No file  | `4b97b1b4989a`  |
| 1338   | No file  | `4b97b1b4989a`  |
| 1335   | No file  | `4b97b1b4989a`  |
| 1333   | No file  | `4b97b1b4989a`  |
| 1329   | No file  | `4b97b1b4989a`  |
| 1327   | No file  | `4b97b1b4989a`  |
| 1324   | No file  | `4b97b1b4989a`  |
| 1321   | No file  | `4b97b1b4989a`  |
| 1319   | No file  | `4b97b1b4989a`  |
| 1318   | No file  | `4b97b1b4989a`  |
| 1316   | No file  | `4b97b1b4989a`  |
| 1313   | No file  | `4b97b1b4989a`  |
| 1311   | No file  | `4b97b1b4989a`  |
| 1309   | No file  | `4b97b1b4989a`  |
| 1304   | No file  | `4b97b1b4989a`  |
| 1292   | No file  | `4b97b1b4989a`  |
| 1286   | No file  | `4b97b1b4989a`  |
| 1280   | No file  | `4b97b1b4989a`  |
| 1276   | No file  | `4b97b1b4989a`  |
| 1267   | No file  | `4b97b1b4989a`  |
| 1261   | No file  | `4b97b1b4989a`  |
| 1256   | No file  | `4b97b1b4989a`  |
| 1250   | No file  | `4b97b1b4989a`  |
| 1246   | No file  | `4b97b1b4989a`  |
| 1239   | No file  | `4b97b1b4989a`  |
| 1230   | No file  | `4b97b1b4989a`  |
| 1226   | No file  | `4b97b1b4989a`  |
| 1220   | No file  | `4b97b1b4989a`  |
| 1217   | No file  | `4b97b1b4989a`  |
| 1211   | No file  | `4b97b1b4989a`  |
| 1210   | No file  | `4b97b1b4989a`  |
| 1208   | No file  | `4b97b1b4989a`  |
| 1203   | No file  | `4b97b1b4989a`  |
| 1197   | No file  | `4b97b1b4989a`  |
| 1194   | No file  | `4b97b1b4989a`  |
| 1192   | No file  | `4b97b1b4989a`  |
| 1187   | No file  | `4b97b1b4989a`  |
| 1183   | No file  | `4b97b1b4989a`  |
| 1177   | No file  | `4b97b1b4989a`  |
| 1173   | No file  | `4b97b1b4989a`  |
| 1167   | No file  | `4b97b1b4989a`  |
| 1164   | No file  | `4b97b1b4989a`  |
| 1156   | No file  | `4b97b1b4989a`  |
| 1149   | No file  | `4b97b1b4989a`  |
| 1144   | No file  | `4b97b1b4989a`  |
| 1137   | No file  | `4b97b1b4989a`  |
| 1132   | No file  | `4b97b1b4989a`  |
| 1127   | No file  | `4b97b1b4989a`  |
| 1122   | No file  | `4b97b1b4989a`  |
| 1118   | No file  | `4b97b1b4989a`  |
| 1114   | No file  | `4b97b1b4989a`  |
| 1109   | No file  | `4b97b1b4989a`  |
| 1102   | No file  | `4b97b1b4989a`  |
| 1096   | No file  | `4b97b1b4989a`  |
| 1088   | No file  | `4b97b1b4989a`  |
| 1081   | No file  | `4b97b1b4989a`  |
| 1076   | No file  | `4b97b1b4989a`  |
| 1069   | No file  | `4b97b1b4989a`  |
| 1064   | No file  | `4b97b1b4989a`  |
| 1058   | No file  | `4b97b1b4989a`  |
| 1051   | No file  | `4b97b1b4989a`  |
| 1044   | No file  | `4b97b1b4989a`  |
| 1036   | No file  | `4b97b1b4989a`  |
| 1026   | No file  | `4b97b1b4989a`  |
| 1016   | No file  | `4b97b1b4989a`  |
| 1009   | No file  | `4b97b1b4989a`  |
| 1005   | No file  | `4b97b1b4989a`  |
| 1000   | No file  | `4b97b1b4989a`  |
| 998    | No file  | `4b97b1b4989a`  |
| 990    | No file  | `4b97b1b4989a`  |
| 979    | No file  | `4b97b1b4989a`  |
| 972    | No file  | `4b97b1b4989a`  |
| 963    | No file  | `4b97b1b4989a`  |
| 955    | No file  | `4b97b1b4989a`  |
| 946    | No file  | `4b97b1b4989a`  |
| 938    | No file  | `4b97b1b4989a`  |
| 927    | No file  | `4b97b1b4989a`  |
| 911    | No file  | `4b97b1b4989a`  |
| 904    | No file  | `4b97b1b4989a`  |
| 899    | No file  | `4b97b1b4989a`  |
| 894    | No file  | `4b97b1b4989a`  |
| 885    | No file  | `4b97b1b4989a`  |
| 879    | No file  | `4b97b1b4989a`  |
| 872    | No file  | `4b97b1b4989a`  |
| 864    | No file  | `4b97b1b4989a`  |
| 855    | No file  | `4b97b1b4989a`  |
| 853    | No file  | `4b97b1b4989a`  |
| 845    | No file  | `4b97b1b4989a`  |
| 837    | No file  | `4b97b1b4989a`  |
| 829    | No file  | `4b97b1b4989a`  |
| 822    | No file  | `4b97b1b4989a`  |
| 814    | No file  | `4b97b1b4989a`  |
| 805    | No file  | `4b97b1b4989a`  |
| 794    | No file  | `4b97b1b4989a`  |
| 787    | No file  | `4b97b1b4989a`  |
| 780    | No file  | `4b97b1b4989a`  |
| 771    | No file  | `4b97b1b4989a`  |
| 760    | No file  | `4b97b1b4989a`  |
| 748    | No file  | `4b97b1b4989a`  |
| 741    | No file  | `4b97b1b4989a`  |
| 736    | No file  | `4b97b1b4989a`  |
| 731    | No file  | `4b97b1b4989a`  |
| 723    | No file  | `4b97b1b4989a`  |
| 711    | No file  | `4b97b1b4989a`  |
| 707    | No file  | `4b97b1b4989a`  |
| 697    | No file  | `4b97b1b4989a`  |
| 689    | No file  | `4b97b1b4989a`  |
| 683    | No file  | `4b97b1b4989a`  |
| 678    | No file  | `4b97b1b4989a`  |
| 670    | No file  | `4b97b1b4989a`  |
| 661    | No file  | `4b97b1b4989a`  |
| 656    | No file  | `4b97b1b4989a`  |
| 652    | No file  | `4b97b1b4989a`  |
| 643    | No file  | `4b97b1b4989a`  |
| 637    | No file  | `4b97b1b4989a`  |
| 630    | No file  | `4b97b1b4989a`  |
| 627    | No file  | `4b97b1b4989a`  |
| 621    | No file  | `4b97b1b4989a`  |
| 617    | No file  | `4b97b1b4989a`  |
| 615    | No file  | `4b97b1b4989a`  |
| 606    | No file  | `4b97b1b4989a`  |
| 599    | No file  | `4b97b1b4989a`  |
| 592    | No file  | `4b97b1b4989a`  |
| 586    | No file  | `4b97b1b4989a`  |
| 577    | No file  | `4b97b1b4989a`  |
| 569    | No file  | `4b97b1b4989a`  |
| 561    | No file  | `4b97b1b4989a`  |
| 554    | No file  | `4b97b1b4989a`  |
| 542    | No file  | `4b97b1b4989a`  |
| 532    | No file  | `4b97b1b4989a`  |
| 531    | No file  | `4b97b1b4989a`  |
| 526    | No file  | `4b97b1b4989a`  |
| 521    | No file  | `4b97b1b4989a`  |
| 517    | No file  | `4b97b1b4989a`  |
| 510    | No file  | `4b97b1b4989a`  |
| 508    | No file  | `4b97b1b4989a`  |
| 504    | No file  | `4b97b1b4989a`  |
| 497    | No file  | `4b97b1b4989a`  |
| 491    | No file  | `4b97b1b4989a`  |
| 485    | No file  | `4b97b1b4989a`  |
| 478    | No file  | `4b97b1b4989a`  |
| 472    | No file  | `4b97b1b4989a`  |
| 466    | No file  | `4b97b1b4989a`  |
| 457    | No file  | `4b97b1b4989a`  |
| 452    | No file  | `4b97b1b4989a`  |
| 449    | No file  | `4b97b1b4989a`  |
| 435    | No file  | `4b97b1b4989a`  |

<!-- versions:end -->

## Companion Files

None read. The `.pac` meshes that use the skeleton do not name it, and it does not name them.

## Layout 1

### File Layout

| Offset            | Type                              | Field         | Notes |
| ----------------- | --------------------------------- | ------------- | ----- |
| `+0x00`           | char[4]                           | magic         | ASCII `PAR ` |
| `+0x04`           | u8                                | kind          | `0x01` on every `.pab` |
| `+0x05`           | u8                                | version       | `2`, `3` or `4`; version 4 picks Bone V4 |
| `+0x06`           | bytes[10]                         | unknown_06    | `00 01 02 03 04 05 06 07 08 09` on 2,001 of 2,007 files (client 3483); `FF 00 01 02 03 04 05 06 07 08` on 6 |
| `+0x10`           | u16                               | bone_count    | `1` to `256` on client 3483 |
| `+0x12`           | Bone[bone_count] if version != 4  | bones         |  |
| `bones+0x00`      | Bone V4[bone_count] if version = 4 | bones_v4     |  |
| `bones_v4+0x00`   | u16                               | volume_count  | `0` on 1,619 of 2,007 files (client 3483), up to `17` |
| `bones_v4+0x02`   | Bone Volume[volume_count]         | volumes       |  |

### Bone (variable: 307 bytes + name, shapes and constraint axes)

Versions 2 and 3. The 2016 `PACharacterBoneNode` names the fields (see Field Names).

| Offset                    | Type                                     | Field                 | Notes |
| ------------------------- | ---------------------------------------- | --------------------- | ----- |
| `+0x00`                   | u32                                      | bone_id               | lookup3 `hashlittle` of the name bytes with seed `0xC5EDE` on all 97,038 bones (client 3483); the id a `.pac` `bone_palette` lists |
| `+0x04`                   | u8                                       | name_length           |  |
| `+0x05`                   | char[name_length]                        | name                  | ASCII, except 11 CP949 names in 9 files (`소매`) |
| `name+0x00`               | i32                                      | parent_index          | `-1` on the first bone and only there; below the bone's own index on every other |
| `name+0x04`               | f32[16]                                  | world_matrix          | Bind pose in model space, row-major with the translation in the last row: `local_matrix` times the parent's `world_matrix` on all 97,038 bones; `local_matrix` on the root |
| `name+0x44`               | f32[16]                                  | inverse_world_matrix  | The inverse of `world_matrix` on 96,987 of 97,038 bones |
| `name+0x84`               | f32[16]                                  | local_matrix          | Relative to the parent; built from `scale`, `rotation` and `translation` on 96,882 of 97,038 bones |
| `name+0xC4`               | f32[16]                                  | inverse_local_matrix  | The inverse of `local_matrix` on 97,021 of 97,038 bones |
| `name+0x104`              | f32[3]                                   | scale                 | `1, 1, 1` on 95,504 of 97,038 bones |
| `name+0x110`              | f32[4]                                   | rotation              | Unit quaternion x, y, z, w |
| `name+0x120`              | f32[3]                                   | translation           | Centimetres; the last row of `local_matrix` |
| `name+0x12C`              | u8                                       | dynamic_shape_count   | `0` or `1`; `1` on 126 bones in 15 version 3 wagon skeletons (client 3483) |
| `name+0x12D`              | Dynamic Shape[dynamic_shape_count]       | dynamic_shapes        |  |
| `dynamic_shapes+0x00`     | u8                                       | constraint_axis_count | `0` or `1` |
| `dynamic_shapes+0x01`     | Constraint Axis[constraint_axis_count]   | constraint_axes       |  |

### Bone V4 (variable: 307 bytes + name, shapes and constraint axes)

Version 4: each dynamic shape starts with a shape type.

| Offset                    | Type                                     | Field                 | Notes |
| ------------------------- | ---------------------------------------- | --------------------- | ----- |
| `+0x00`                   | u32                                      | bone_id               | As in Bone |
| `+0x04`                   | u8                                       | name_length           |  |
| `+0x05`                   | char[name_length]                        | name                  | As in Bone |
| `name+0x00`               | i32                                      | parent_index          | As in Bone |
| `name+0x04`               | f32[16]                                  | world_matrix          | As in Bone |
| `name+0x44`               | f32[16]                                  | inverse_world_matrix  | As in Bone |
| `name+0x84`               | f32[16]                                  | local_matrix          | As in Bone |
| `name+0xC4`               | f32[16]                                  | inverse_local_matrix  | As in Bone |
| `name+0x104`              | f32[3]                                   | scale                 | As in Bone |
| `name+0x110`              | f32[4]                                   | rotation              | As in Bone |
| `name+0x120`              | f32[3]                                   | translation           | As in Bone |
| `name+0x12C`              | u8                                       | dynamic_shape_count   | `0` or `1`; `1` on 2,009 bones (client 3483) |
| `name+0x12D`              | Typed Shape[dynamic_shape_count]         | dynamic_shapes        |  |
| `dynamic_shapes+0x00`     | u8                                       | constraint_axis_count | `0` or `1` |
| `dynamic_shapes+0x01`     | Constraint Axis[constraint_axis_count]   | constraint_axes       |  |

### Typed Shape (variable: 16 bytes + shape body)

Version 4 is newer than the 2016 loader, so the fields here are read from the client 3483 files against the `.pac` meshes of the same skeleton (see Typed Shapes Against the Mesh).

| Offset                 | Type                       | Field             | Notes |
| ---------------------- | -------------------------- | ----------------- | ----- |
| `+0x00`                | u32                        | shape             | See Shape Values; `1` on 1,930 of 2,009 shapes (client 3483), `2` on 58, `4` on 12, `0` on 9 |
| `+0x04`                | f32[3]                     | position_in_world | Where the shape sits, in model space and metres as in Constraint Axis; on the bone's local x axis within 1 mm on 1,606 of 2,009 shapes (client 3483) |
| `+0x10`                | f32[3] if shape = 0        | unknown_box       | `-0.04, 0.332, 0.356` on all 9 (client 3483) |
| `unknown_box+0x00`     | f32 if shape = 1           | cylinder_length   | Along the bone's local x axis |
| `cylinder_length+0x00` | f32 if shape = 1           | cylinder_radius   |  |
| `cylinder_radius+0x00` | Dynamic Shape if shape = 2 | mesh              | Points in the bone's local space, in metres |
| `mesh+0x00`            | f32 if shape = 4           | unknown_shape_4   | `0.04` to `0.081` on client 3483 |

### Dynamic Shape (variable: 4 bytes + vertices and indices)

The 2016 `PADynamicShape`: `_vertexArr` and `_indexArr`.

| Offset          | Type                     | Field        | Notes |
| --------------- | ------------------------ | ------------ | ----- |
| `+0x00`         | u16                      | vertex_count |  |
| `+0x02`         | f32[vertex_count][3]     | vertices     | x, y, z |
| `vertices+0x00` | u16                      | index_count  | A multiple of 3 |
| `vertices+0x02` | u16[index_count]         | indices      | Three per triangle, each below `vertex_count` on every shape and volume of client 3483 |

### Constraint Axis (36 bytes)

The 2016 `PAConstraintAxisInfo`.

| Offset  | Type   | Field               | Notes |
| ------- | ------ | ------------------- | ----- |
| `+0x00` | f32[3] | position_in_world   | Metres: times 100 it is within 0.1 cm of the bone's `world_matrix` translation on 1,987 of 2,181 axes (client 3483) |
| `+0x0C` | f32[3] | twist_axis_in_world | A unit vector on all 2,181 |
| `+0x18` | f32[3] | plane_axis_in_world | A unit vector at right angles to `twist_axis_in_world` on all 2,181 |

### Bone Volume (variable: 70 bytes + shape body)

The 2016 `PABoneVolumeInfo`, in another member order; the Notes cells name the member the 2016 loader writes each field to.

| Offset                  | Type                       | Field             | Notes |
| ----------------------- | -------------------------- | ----------------- | ----- |
| `+0x00`                 | u32                        | parent_bone_index | Index into `bones`; below `bone_count` on all 497 volumes (client 3483) |
| `+0x04`                 | f32[16]                    | local_matrix      | `_localTM` |
| `+0x44`                 | u8                         | volume_type       | See Volume Type Values; `0` on 460 of 497 volumes (client 3483), `2` on 37 |
| `+0x45`                 | u8                         | shape             | See Shape Values; `2` on 480, `0` on 15, `1` on 2 |
| `+0x46`                 | f32 if shape = 0           | box_length        | `_length` |
| `box_length+0x00`       | f32 if shape = 0           | box_width         | `_width` |
| `box_width+0x00`        | f32 if shape = 0           | box_height        | `_height` |
| `box_height+0x00`       | f32 if shape = 1           | cylinder_radius   | `_radius` |
| `cylinder_radius+0x00`  | f32 if shape = 1           | cylinder_height   | `_height` |
| `cylinder_height+0x00`  | Dynamic Shape if shape = 2 | mesh              | `_mesh` |

## Shape Values

The 2016 `EBvShape` names `0` to `3`; `4` came later and holds one float.

| Value | Name                 | Body |
| ----- | -------------------- | ---- |
| 0     | `eBvS_Box`           | Length, width, height |
| 1     | `eBvS_Cylinder`      | Radius, height |
| 2     | `eBvS_Mesh`          | Dynamic Shape |
| 3     | `eBvS_None`          | Not seen; the 2016 loader fails the file at a volume of this shape, as at a wrong header |
| 4     | Not in the 2016 enum | `f32` |

## Volume Type Values

The 2016 `EBvType`.

| Value | Name             |
| ----- | ---------------- |
| 0     | `eBvT_Carrier`   |
| 1     | `eBvT_Reserve1`  |
| 2     | `eBvT_Collision` |
| 3     | `eBvT_None`      |

## Field Names

The 2016 `PACharacterBoneNode` holds `_worldNodeTM`, `_invWorldNodeTM`, `_localNodeTM`, `_invLocalNodeTM`, `_s_local`, `_r_local` (x, y, z, w), `_t_local`, `_nameHash`, `_parentBoneIdx`, `_name`, `_dynamicShapeArr` and `_constraintAxisInfoArr`. The 2016 loader, `PACharacterBone::loadSkeletonResource`, reads each Bone field into its member in file order: the first matrix into `_worldNodeTM`, the second into `_invWorldNodeTM` (the struct lists the inverse first), `dynamic_shape_count` as the size of `_dynamicShapeArr` and `constraint_axis_count` as the size of `_constraintAxisInfoArr`. The client 3483 files agree: the matrix chain and the inverses in the Bone notes, the name hash over all 97,038 bones. `PACharacterBone` keeps the skeleton file name (`_skeletonFilename`) and a list of `PABoneVolumeInfo` (`_boneVolumeInfoArr`), the Bone Volume records.

## Typed Shapes Against the Mesh

For each Typed Shape, the vertices of the `.pac` meshes in the skeleton's folder whose largest weight is on the shape's bone were taken in model space (client 3483; 1,695 cylinders found such vertices, the other shapes none in the same folder).

| Reading | Result |
| ------- | ------ |
| `position_in_world` of a cylinder is its centre | Moved into the bone's space, it lies on the local x axis on 1,549 of 1,930 cylinders, at x = half the first float on 521 |
| First float is the length, second the radius | A median 66% of the bone's vertices fall inside the cylinder (with 25% slack); read the other way round, 36% |
| `position_in_world` of a mesh shape is the bone | Within 1 mm of the bone's position on 48 of 58 |
| Mesh points are in the bone's local space, in metres | Moved by `world_matrix`, their box overlaps the bone's vertex box best on 38 of 45 mesh shapes (version 3 and 4) with vertices, ahead of centimetres or model space |

The version 3 Dynamic Shape points read the same way.

## Finding a Mesh's Skeleton

For a `.pac` with a non-empty `bone_palette`, walk from the mesh's folder up the tree and take the nearest folder with a `.pab` that holds every palette id that is not one of the mesh's own bones. On client 3483 that finds a skeleton for 96,352 of the 97,151 meshes with a palette; for 98 of them the nearest such folder holds more than one fitting `.pab`. Of the other 799, 527 miss 1 to more than 5 ids against the nearest `.pab` and 272 have no `.pab` above them (109 under `character/model/2_mon/m0127_sd_head`). The ids are name hashes, so a palette id also matches a bone of that name in an unrelated skeleton.

## Notes

- Every `.pab` on client 3483 walks to its last byte by this layout (2,007 files).
- The 2016 loader accepts `kind` `1` with `version` `3` only and reads every version 3 structure as this layout does. It also sets bit `volume_type` of `_boneVolumeTypeBitFlag` for each volume.
- The `.pac` Bone record is this Bone with no name: the same matrices, scale, rotation and translation, then the two counts; the `dynamic_shape_count` of all 9,027 `.pac` bones is `0`.
- sibercat/PAZ-Unpacker (MIT) gave the first reading of the header, the bone name, parent and matrices. It reads the matrices as local, inverse local, bind and inverse bind; the chain check puts the world (bind) matrices first. It guesses the block after `translation` from the record after it (0, 24, 36, 56 or 60 bytes); the two counts and the shape type give its size.

## Open Questions

### Box and Shape 4 Bodies of a Typed Shape

The 9 box bodies on client 3483 are one value, `-0.04, 0.332, 0.356`, on the flag bones of three train and wagon skeletons; a negative first float does not fit a length, and one value gives nothing to compare. The 12 shape `4` bodies are four values on the `B_Add_b_00` to `B_Add_b_03` bones of `pdw_01.pab` and two monster skeletons. Each `position_in_world` sits about that float out along the bone's local x axis (`0.0436` for `0.0399`), and the `pdw` mesh vertices of those bones lie a median `0.043` to `0.068` from it, so a sphere radius is the lead; four shapes are too few to name it.

### `unknown_06`

The same ten bytes as `unknown_06` of [`mesh_pac.md`](mesh_pac.md). Six skeletons start them with `FF`. The 2016 loader fills its header buffer with `0` to `9` before it reads the file and never checks these bytes, so they are likely a header default the exporter writes.
