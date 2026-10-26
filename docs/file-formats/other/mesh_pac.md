# `*.pac` Character Mesh Format

## Purpose

Skinned meshes of player classes, NPCs, monsters, mounts and their gear under `character/model/`. A file holds submeshes, each with three levels of detail; a vertex names up to four bones through the file's bone palette. A submesh's texture is its name plus `.dds` (546 of 548 sampled submeshes find one, in `character/texture/` or `object/texture/`). The Model tab of the browser draws LOD 0 of every submesh (`PAZ-Parser/par_mesh.py`). Byte `0x04` of the `PAR ` header is `0x03`. On client 3483 there are 97,645 `.pac` files: 18,117 of version 1, 12,077 of version 2, 67,450 of version 3, and one that is not a `PAR ` file (see Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                         | Bytes   | Records                                            | Row bytes |
| ------ | -------------- | -------------------------------------------- | ------- | -------------------------------------------------- | --------- |
| 1      | 3483 and later | `pem_00_gtb_0033_01.pac`                     | 51,931  | 8 Bone, 1,304 Vertex, 3 Lod                        | 32        |
| 1      | 3483 and later | `pew_ew_hel_0031_haircut.pac`                | 125     | 4 Entry, 4 Group                                   | 16        |
| 1      | 3483 and later | `pfw_00_customizing_lip_left_down_pick.pac`  | 2,002   | 47 Vertex, 3 Lod                                   | 32        |
| 1      | 3483 and later | `psw_00_cts_0033.pac`                        | 586,120 | 128 Bone, 19 Constraint Axis, 13,939 Vertex, 3 Lod | 32        |
| 1      | 3483 and later | `psw_00_customizing_eye_right_down_pick.pac` | 2,014   | 47 Vertex, 3 Lod                                   | 32        |
| 1      | 3483 and later | `psw_10_lb_0057.pac`                         | 73,812  | 1,784 Vertex, 3 Lod, 5 Entry                       | 32        |
| 1      | 3483 and later | `pvw_00_customizing_body_rfinger4_pick.pac`  | 2,002   | 49 Vertex, 3 Lod                                   | 32        |

| Layout | File                                         | Known             | Unknown           |
| ------ | -------------------------------------------- | ----------------- | ----------------- |
| 1      | `pem_00_gtb_0033_01.pac`                     | 41,478 B (79.9%)  | 10,453 B (20.1%)  |
| 1      | `pew_ew_hel_0031_haircut.pac`                | 42 B (33.6%)      | 83 B (66.4%)      |
| 1      | `pfw_00_customizing_lip_left_down_pick.pac`  | 1,605 B (80.2%)   | 397 B (19.8%)     |
| 1      | `psw_00_cts_0033.pac`                        | 474,571 B (81.0%) | 111,549 B (19.0%) |
| 1      | `psw_00_customizing_eye_right_down_pick.pac` | 1,617 B (80.3%)   | 397 B (19.7%)     |
| 1      | `psw_10_lb_0057.pac`                         | 59,430 B (80.5%)  | 14,382 B (19.5%)  |
| 1      | `pvw_00_customizing_body_rfinger4_pick.pac`  | 1,589 B (79.4%)   | 413 B (20.6%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a46514ea19bf`  |
| 3482   | No file  | `a46514ea19bf`  |
| 3474   | No file  | `a46514ea19bf`  |
| 3473   | No file  | `a46514ea19bf`  |
| 3464   | No file  | `a46514ea19bf`  |
| 3458   | No file  | `a46514ea19bf`  |
| 3454   | No file  | `a46514ea19bf`  |
| 3444   | No file  | `a46514ea19bf`  |
| 3435   | No file  | `a46514ea19bf`  |
| 3426   | No file  | `a46514ea19bf`  |
| 3418   | No file  | `a46514ea19bf`  |
| 3412   | No file  | `a46514ea19bf`  |
| 3402   | No file  | `a46514ea19bf`  |
| 3396   | No file  | `a46514ea19bf`  |
| 3387   | No file  | `a46514ea19bf`  |
| 3381   | No file  | `a46514ea19bf`  |
| 3373   | No file  | `a46514ea19bf`  |
| 3364   | No file  | `a46514ea19bf`  |
| 3356   | No file  | `a46514ea19bf`  |
| 3349   | No file  | `a46514ea19bf`  |
| 3342   | No file  | `a46514ea19bf`  |
| 3335   | No file  | `a46514ea19bf`  |
| 3326   | No file  | `a46514ea19bf`  |
| 3321   | No file  | `a46514ea19bf`  |
| 3314   | No file  | `a46514ea19bf`  |
| 3303   | No file  | `a46514ea19bf`  |
| 3302   | No file  | `a46514ea19bf`  |
| 3293   | No file  | `a46514ea19bf`  |
| 3283   | No file  | `a46514ea19bf`  |
| 3275   | No file  | `a46514ea19bf`  |
| 3267   | No file  | `a46514ea19bf`  |
| 3258   | No file  | `a46514ea19bf`  |
| 3251   | No file  | `a46514ea19bf`  |
| 3242   | No file  | `a46514ea19bf`  |
| 3235   | No file  | `a46514ea19bf`  |
| 3229   | No file  | `a46514ea19bf`  |
| 3212   | No file  | `a46514ea19bf`  |
| 3203   | No file  | `a46514ea19bf`  |
| 3193   | No file  | `a46514ea19bf`  |
| 3186   | No file  | `a46514ea19bf`  |
| 3177   | No file  | `a46514ea19bf`  |
| 3169   | No file  | `a46514ea19bf`  |
| 3158   | No file  | `a46514ea19bf`  |
| 3151   | No file  | `a46514ea19bf`  |
| 3144   | No file  | `a46514ea19bf`  |
| 3133   | No file  | `a46514ea19bf`  |
| 3125   | No file  | `a46514ea19bf`  |
| 3118   | No file  | `a46514ea19bf`  |
| 3111   | No file  | `a46514ea19bf`  |
| 3103   | No file  | `a46514ea19bf`  |
| 3095   | No file  | `a46514ea19bf`  |
| 3086   | No file  | `a46514ea19bf`  |
| 3072   | No file  | `a46514ea19bf`  |
| 3062   | No file  | `a46514ea19bf`  |
| 3052   | No file  | `a46514ea19bf`  |
| 3045   | No file  | `a46514ea19bf`  |
| 3037   | No file  | `a46514ea19bf`  |
| 3030   | No file  | `a46514ea19bf`  |
| 3021   | No file  | `a46514ea19bf`  |
| 3012   | No file  | `a46514ea19bf`  |
| 3002   | No file  | `a46514ea19bf`  |
| 2995   | No file  | `a46514ea19bf`  |
| 2987   | No file  | `a46514ea19bf`  |
| 2978   | No file  | `a46514ea19bf`  |
| 2970   | No file  | `a46514ea19bf`  |
| 2959   | No file  | `a46514ea19bf`  |
| 2951   | No file  | `a46514ea19bf`  |
| 2942   | No file  | `a46514ea19bf`  |
| 2935   | No file  | `a46514ea19bf`  |
| 2932   | No file  | `a46514ea19bf`  |
| 2923   | No file  | `a46514ea19bf`  |
| 2919   | No file  | `a46514ea19bf`  |
| 2907   | No file  | `a46514ea19bf`  |
| 2900   | No file  | `a46514ea19bf`  |
| 2891   | No file  | `a46514ea19bf`  |
| 2882   | No file  | `a46514ea19bf`  |
| 2872   | No file  | `a46514ea19bf`  |
| 2863   | No file  | `a46514ea19bf`  |
| 2855   | No file  | `a46514ea19bf`  |
| 2849   | No file  | `a46514ea19bf`  |
| 2844   | No file  | `a46514ea19bf`  |
| 2834   | No file  | `a46514ea19bf`  |
| 2825   | No file  | `a46514ea19bf`  |
| 2819   | No file  | `a46514ea19bf`  |
| 2811   | No file  | `a46514ea19bf`  |
| 2803   | No file  | `a46514ea19bf`  |
| 2794   | No file  | `a46514ea19bf`  |
| 2783   | No file  | `a46514ea19bf`  |
| 2774   | No file  | `a46514ea19bf`  |
| 2765   | No file  | `a46514ea19bf`  |
| 2756   | No file  | `a46514ea19bf`  |
| 2750   | No file  | `a46514ea19bf`  |
| 2743   | No file  | `a46514ea19bf`  |
| 2736   | No file  | `a46514ea19bf`  |
| 2726   | No file  | `a46514ea19bf`  |
| 2717   | No file  | `a46514ea19bf`  |
| 2709   | No file  | `a46514ea19bf`  |
| 2703   | No file  | `a46514ea19bf`  |
| 2695   | No file  | `a46514ea19bf`  |
| 2684   | No file  | `a46514ea19bf`  |
| 2672   | No file  | `a46514ea19bf`  |
| 2665   | No file  | `a46514ea19bf`  |
| 2657   | No file  | `a46514ea19bf`  |
| 2649   | No file  | `a46514ea19bf`  |
| 2644   | No file  | `a46514ea19bf`  |
| 2637   | No file  | `a46514ea19bf`  |
| 2629   | No file  | `a46514ea19bf`  |
| 2619   | No file  | `a46514ea19bf`  |
| 2612   | No file  | `a46514ea19bf`  |
| 2606   | No file  | `a46514ea19bf`  |
| 2602   | No file  | `a46514ea19bf`  |
| 2601   | No file  | `a46514ea19bf`  |
| 2592   | No file  | `a46514ea19bf`  |
| 2583   | No file  | `a46514ea19bf`  |
| 2575   | No file  | `a46514ea19bf`  |
| 2567   | No file  | `a46514ea19bf`  |
| 2560   | No file  | `a46514ea19bf`  |
| 2553   | No file  | `a46514ea19bf`  |
| 2545   | No file  | `a46514ea19bf`  |
| 2538   | No file  | `a46514ea19bf`  |
| 2529   | No file  | `a46514ea19bf`  |
| 2519   | No file  | `a46514ea19bf`  |
| 2513   | No file  | `a46514ea19bf`  |
| 2510   | No file  | `a46514ea19bf`  |
| 2507   | No file  | `a46514ea19bf`  |
| 2503   | No file  | `a46514ea19bf`  |
| 2498   | No file  | `a46514ea19bf`  |
| 2492   | No file  | `a46514ea19bf`  |
| 2487   | No file  | `a46514ea19bf`  |
| 2480   | No file  | `a46514ea19bf`  |
| 2474   | No file  | `a46514ea19bf`  |
| 2468   | No file  | `a46514ea19bf`  |
| 2460   | No file  | `a46514ea19bf`  |
| 2453   | No file  | `a46514ea19bf`  |
| 2444   | No file  | `a46514ea19bf`  |
| 2438   | No file  | `a46514ea19bf`  |
| 2434   | No file  | `a46514ea19bf`  |
| 2429   | No file  | `a46514ea19bf`  |
| 2421   | No file  | `a46514ea19bf`  |
| 2414   | No file  | `a46514ea19bf`  |
| 2407   | No file  | `a46514ea19bf`  |
| 2401   | No file  | `a46514ea19bf`  |
| 2397   | No file  | `a46514ea19bf`  |
| 2393   | No file  | `a46514ea19bf`  |
| 2384   | No file  | `a46514ea19bf`  |
| 2378   | No file  | `a46514ea19bf`  |
| 2372   | No file  | `a46514ea19bf`  |
| 2358   | No file  | `a46514ea19bf`  |
| 2352   | No file  | `a46514ea19bf`  |
| 2347   | No file  | `a46514ea19bf`  |
| 2343   | No file  | `a46514ea19bf`  |
| 2335   | No file  | `a46514ea19bf`  |
| 2327   | No file  | `a46514ea19bf`  |
| 2324   | No file  | `a46514ea19bf`  |
| 2319   | No file  | `a46514ea19bf`  |
| 2313   | No file  | `a46514ea19bf`  |
| 2308   | No file  | `a46514ea19bf`  |
| 2302   | No file  | `a46514ea19bf`  |
| 2295   | No file  | `a46514ea19bf`  |
| 2290   | No file  | `a46514ea19bf`  |
| 2284   | No file  | `a46514ea19bf`  |
| 2276   | No file  | `a46514ea19bf`  |
| 2269   | No file  | `a46514ea19bf`  |
| 2259   | No file  | `a46514ea19bf`  |
| 2250   | No file  | `a46514ea19bf`  |
| 2243   | No file  | `a46514ea19bf`  |
| 2235   | No file  | `a46514ea19bf`  |
| 2229   | No file  | `a46514ea19bf`  |
| 2224   | No file  | `a46514ea19bf`  |
| 2218   | No file  | `a46514ea19bf`  |
| 2215   | No file  | `a46514ea19bf`  |
| 2207   | No file  | `a46514ea19bf`  |
| 2203   | No file  | `a46514ea19bf`  |
| 2196   | No file  | `a46514ea19bf`  |
| 2192   | No file  | `a46514ea19bf`  |
| 2189   | No file  | `a46514ea19bf`  |
| 2183   | No file  | `a46514ea19bf`  |
| 2179   | No file  | `a46514ea19bf`  |
| 2171   | No file  | `a46514ea19bf`  |
| 2163   | No file  | `a46514ea19bf`  |
| 2156   | No file  | `a46514ea19bf`  |
| 2151   | No file  | `a46514ea19bf`  |
| 2147   | No file  | `a46514ea19bf`  |
| 2142   | No file  | `a46514ea19bf`  |
| 2138   | No file  | `a46514ea19bf`  |
| 2134   | No file  | `a46514ea19bf`  |
| 2130   | No file  | `a46514ea19bf`  |
| 2122   | No file  | `a46514ea19bf`  |
| 2107   | No file  | `a46514ea19bf`  |
| 2098   | No file  | `a46514ea19bf`  |
| 2089   | No file  | `a46514ea19bf`  |
| 2081   | No file  | `a46514ea19bf`  |
| 2073   | No file  | `a46514ea19bf`  |
| 2067   | No file  | `a46514ea19bf`  |
| 2063   | No file  | `a46514ea19bf`  |
| 2059   | No file  | `a46514ea19bf`  |
| 2052   | No file  | `a46514ea19bf`  |
| 2044   | No file  | `a46514ea19bf`  |
| 2039   | No file  | `a46514ea19bf`  |
| 2032   | No file  | `a46514ea19bf`  |
| 2025   | No file  | `a46514ea19bf`  |
| 2011   | No file  | `a46514ea19bf`  |
| 2005   | No file  | `a46514ea19bf`  |
| 2000   | No file  | `a46514ea19bf`  |
| 1996   | No file  | `a46514ea19bf`  |
| 1991   | No file  | `a46514ea19bf`  |
| 1985   | No file  | `a46514ea19bf`  |
| 1980   | No file  | `a46514ea19bf`  |
| 1969   | No file  | `a46514ea19bf`  |
| 1964   | No file  | `a46514ea19bf`  |
| 1958   | No file  | `a46514ea19bf`  |
| 1950   | No file  | `a46514ea19bf`  |
| 1945   | No file  | `a46514ea19bf`  |
| 1937   | No file  | `a46514ea19bf`  |
| 1933   | No file  | `a46514ea19bf`  |
| 1927   | No file  | `a46514ea19bf`  |
| 1921   | No file  | `a46514ea19bf`  |
| 1914   | No file  | `a46514ea19bf`  |
| 1908   | No file  | `a46514ea19bf`  |
| 1897   | No file  | `a46514ea19bf`  |
| 1892   | No file  | `a46514ea19bf`  |
| 1886   | No file  | `a46514ea19bf`  |
| 1881   | No file  | `a46514ea19bf`  |
| 1871   | No file  | `a46514ea19bf`  |
| 1866   | No file  | `a46514ea19bf`  |
| 1862   | No file  | `a46514ea19bf`  |
| 1854   | No file  | `a46514ea19bf`  |
| 1846   | No file  | `a46514ea19bf`  |
| 1838   | No file  | `a46514ea19bf`  |
| 1832   | No file  | `a46514ea19bf`  |
| 1826   | No file  | `a46514ea19bf`  |
| 1822   | No file  | `a46514ea19bf`  |
| 1818   | No file  | `a46514ea19bf`  |
| 1804   | No file  | `a46514ea19bf`  |
| 1794   | No file  | `a46514ea19bf`  |
| 1790   | No file  | `a46514ea19bf`  |
| 1784   | No file  | `a46514ea19bf`  |
| 1774   | No file  | `a46514ea19bf`  |
| 1771   | No file  | `a46514ea19bf`  |
| 1762   | No file  | `a46514ea19bf`  |
| 1759   | No file  | `a46514ea19bf`  |
| 1754   | No file  | `a46514ea19bf`  |
| 1749   | No file  | `a46514ea19bf`  |
| 1743   | No file  | `a46514ea19bf`  |
| 1737   | No file  | `a46514ea19bf`  |
| 1731   | No file  | `a46514ea19bf`  |
| 1725   | No file  | `a46514ea19bf`  |
| 1717   | No file  | `a46514ea19bf`  |
| 1710   | No file  | `a46514ea19bf`  |
| 1704   | No file  | `a46514ea19bf`  |
| 1698   | No file  | `a46514ea19bf`  |
| 1690   | No file  | `a46514ea19bf`  |
| 1685   | No file  | `a46514ea19bf`  |
| 1680   | No file  | `a46514ea19bf`  |
| 1674   | No file  | `a46514ea19bf`  |
| 1668   | No file  | `a46514ea19bf`  |
| 1659   | No file  | `a46514ea19bf`  |
| 1649   | No file  | `a46514ea19bf`  |
| 1642   | No file  | `a46514ea19bf`  |
| 1636   | No file  | `a46514ea19bf`  |
| 1628   | No file  | `a46514ea19bf`  |
| 1622   | No file  | `a46514ea19bf`  |
| 1614   | No file  | `a46514ea19bf`  |
| 1608   | No file  | `a46514ea19bf`  |
| 1602   | No file  | `a46514ea19bf`  |
| 1598   | No file  | `a46514ea19bf`  |
| 1594   | No file  | `a46514ea19bf`  |
| 1590   | No file  | `a46514ea19bf`  |
| 1587   | No file  | `a46514ea19bf`  |
| 1584   | No file  | `a46514ea19bf`  |
| 1579   | No file  | `a46514ea19bf`  |
| 1572   | No file  | `a46514ea19bf`  |
| 1565   | No file  | `a46514ea19bf`  |
| 1559   | No file  | `a46514ea19bf`  |
| 1554   | No file  | `a46514ea19bf`  |
| 1547   | No file  | `a46514ea19bf`  |
| 1537   | No file  | `a46514ea19bf`  |
| 1529   | No file  | `a46514ea19bf`  |
| 1524   | No file  | `a46514ea19bf`  |
| 1519   | No file  | `a46514ea19bf`  |
| 1509   | No file  | `a46514ea19bf`  |
| 1506   | No file  | `a46514ea19bf`  |
| 1504   | No file  | `a46514ea19bf`  |
| 1500   | No file  | `a46514ea19bf`  |
| 1493   | No file  | `a46514ea19bf`  |
| 1489   | No file  | `a46514ea19bf`  |
| 1485   | No file  | `a46514ea19bf`  |
| 1481   | No file  | `a46514ea19bf`  |
| 1474   | No file  | `a46514ea19bf`  |
| 1466   | No file  | `a46514ea19bf`  |
| 1462   | No file  | `a46514ea19bf`  |
| 1459   | No file  | `a46514ea19bf`  |
| 1453   | No file  | `a46514ea19bf`  |
| 1450   | No file  | `a46514ea19bf`  |
| 1445   | No file  | `a46514ea19bf`  |
| 1439   | No file  | `a46514ea19bf`  |
| 1433   | No file  | `a46514ea19bf`  |
| 1430   | No file  | `a46514ea19bf`  |
| 1426   | No file  | `a46514ea19bf`  |
| 1421   | No file  | `a46514ea19bf`  |
| 1417   | No file  | `a46514ea19bf`  |
| 1416   | No file  | `a46514ea19bf`  |
| 1409   | No file  | `a46514ea19bf`  |
| 1405   | No file  | `a46514ea19bf`  |
| 1401   | No file  | `a46514ea19bf`  |
| 1396   | No file  | `a46514ea19bf`  |
| 1391   | No file  | `a46514ea19bf`  |
| 1390   | No file  | `a46514ea19bf`  |
| 1386   | No file  | `a46514ea19bf`  |
| 1381   | No file  | `a46514ea19bf`  |
| 1379   | No file  | `a46514ea19bf`  |
| 1372   | No file  | `a46514ea19bf`  |
| 1366   | No file  | `a46514ea19bf`  |
| 1364   | No file  | `a46514ea19bf`  |
| 1363   | No file  | `a46514ea19bf`  |
| 1360   | No file  | `a46514ea19bf`  |
| 1358   | No file  | `a46514ea19bf`  |
| 1355   | No file  | `a46514ea19bf`  |
| 1351   | No file  | `a46514ea19bf`  |
| 1348   | No file  | `a46514ea19bf`  |
| 1346   | No file  | `a46514ea19bf`  |
| 1341   | No file  | `a46514ea19bf`  |
| 1340   | No file  | `a46514ea19bf`  |
| 1338   | No file  | `a46514ea19bf`  |
| 1335   | No file  | `a46514ea19bf`  |
| 1333   | No file  | `a46514ea19bf`  |
| 1329   | No file  | `a46514ea19bf`  |
| 1327   | No file  | `a46514ea19bf`  |
| 1324   | No file  | `a46514ea19bf`  |
| 1321   | No file  | `a46514ea19bf`  |
| 1319   | No file  | `a46514ea19bf`  |
| 1318   | No file  | `a46514ea19bf`  |
| 1316   | No file  | `a46514ea19bf`  |
| 1313   | No file  | `a46514ea19bf`  |
| 1311   | No file  | `a46514ea19bf`  |
| 1309   | No file  | `a46514ea19bf`  |
| 1304   | No file  | `a46514ea19bf`  |
| 1292   | No file  | `a46514ea19bf`  |
| 1286   | No file  | `a46514ea19bf`  |
| 1280   | No file  | `a46514ea19bf`  |
| 1276   | No file  | `a46514ea19bf`  |
| 1267   | No file  | `a46514ea19bf`  |
| 1261   | No file  | `a46514ea19bf`  |
| 1256   | No file  | `a46514ea19bf`  |
| 1250   | No file  | `a46514ea19bf`  |
| 1246   | No file  | `a46514ea19bf`  |
| 1239   | No file  | `a46514ea19bf`  |
| 1230   | No file  | `a46514ea19bf`  |
| 1226   | No file  | `a46514ea19bf`  |
| 1220   | No file  | `a46514ea19bf`  |
| 1217   | No file  | `a46514ea19bf`  |
| 1211   | No file  | `a46514ea19bf`  |
| 1210   | No file  | `a46514ea19bf`  |
| 1208   | No file  | `a46514ea19bf`  |
| 1203   | No file  | `a46514ea19bf`  |
| 1197   | No file  | `a46514ea19bf`  |
| 1194   | No file  | `a46514ea19bf`  |
| 1192   | No file  | `a46514ea19bf`  |
| 1187   | No file  | `a46514ea19bf`  |
| 1183   | No file  | `a46514ea19bf`  |
| 1177   | No file  | `a46514ea19bf`  |
| 1173   | No file  | `a46514ea19bf`  |
| 1167   | No file  | `a46514ea19bf`  |
| 1164   | No file  | `a46514ea19bf`  |
| 1156   | No file  | `a46514ea19bf`  |
| 1149   | No file  | `a46514ea19bf`  |
| 1144   | No file  | `a46514ea19bf`  |
| 1137   | No file  | `a46514ea19bf`  |
| 1132   | No file  | `a46514ea19bf`  |
| 1127   | No file  | `a46514ea19bf`  |
| 1122   | No file  | `a46514ea19bf`  |
| 1118   | No file  | `a46514ea19bf`  |
| 1114   | No file  | `a46514ea19bf`  |
| 1109   | No file  | `a46514ea19bf`  |
| 1102   | No file  | `a46514ea19bf`  |
| 1096   | No file  | `a46514ea19bf`  |
| 1088   | No file  | `a46514ea19bf`  |
| 1081   | No file  | `a46514ea19bf`  |
| 1076   | No file  | `a46514ea19bf`  |
| 1069   | No file  | `a46514ea19bf`  |
| 1064   | No file  | `a46514ea19bf`  |
| 1058   | No file  | `a46514ea19bf`  |
| 1051   | No file  | `a46514ea19bf`  |
| 1044   | No file  | `a46514ea19bf`  |
| 1036   | No file  | `a46514ea19bf`  |
| 1026   | No file  | `a46514ea19bf`  |
| 1016   | No file  | `a46514ea19bf`  |
| 1009   | No file  | `a46514ea19bf`  |
| 1005   | No file  | `a46514ea19bf`  |
| 1000   | No file  | `a46514ea19bf`  |
| 998    | No file  | `a46514ea19bf`  |
| 990    | No file  | `a46514ea19bf`  |
| 979    | No file  | `a46514ea19bf`  |
| 972    | No file  | `a46514ea19bf`  |
| 963    | No file  | `a46514ea19bf`  |
| 955    | No file  | `a46514ea19bf`  |
| 946    | No file  | `a46514ea19bf`  |
| 938    | No file  | `a46514ea19bf`  |
| 927    | No file  | `a46514ea19bf`  |
| 911    | No file  | `a46514ea19bf`  |
| 904    | No file  | `a46514ea19bf`  |
| 899    | No file  | `a46514ea19bf`  |
| 894    | No file  | `a46514ea19bf`  |
| 885    | No file  | `a46514ea19bf`  |
| 879    | No file  | `a46514ea19bf`  |
| 872    | No file  | `a46514ea19bf`  |
| 864    | No file  | `a46514ea19bf`  |
| 855    | No file  | `a46514ea19bf`  |
| 853    | No file  | `a46514ea19bf`  |
| 845    | No file  | `a46514ea19bf`  |
| 837    | No file  | `a46514ea19bf`  |
| 829    | No file  | `a46514ea19bf`  |
| 822    | No file  | `a46514ea19bf`  |
| 814    | No file  | `a46514ea19bf`  |
| 805    | No file  | `a46514ea19bf`  |
| 794    | No file  | `a46514ea19bf`  |
| 787    | No file  | `a46514ea19bf`  |
| 780    | No file  | `a46514ea19bf`  |
| 771    | No file  | `a46514ea19bf`  |
| 760    | No file  | `a46514ea19bf`  |
| 748    | No file  | `a46514ea19bf`  |
| 741    | No file  | `a46514ea19bf`  |
| 736    | No file  | `a46514ea19bf`  |
| 731    | No file  | `a46514ea19bf`  |
| 723    | No file  | `a46514ea19bf`  |
| 711    | No file  | `a46514ea19bf`  |
| 707    | No file  | `a46514ea19bf`  |
| 697    | No file  | `a46514ea19bf`  |
| 689    | No file  | `a46514ea19bf`  |
| 683    | No file  | `a46514ea19bf`  |
| 678    | No file  | `a46514ea19bf`  |
| 670    | No file  | `a46514ea19bf`  |
| 661    | No file  | `a46514ea19bf`  |
| 656    | No file  | `a46514ea19bf`  |
| 652    | No file  | `a46514ea19bf`  |
| 643    | No file  | `a46514ea19bf`  |
| 637    | No file  | `a46514ea19bf`  |
| 630    | No file  | `a46514ea19bf`  |
| 627    | No file  | `a46514ea19bf`  |
| 621    | No file  | `a46514ea19bf`  |
| 617    | No file  | `a46514ea19bf`  |
| 615    | No file  | `a46514ea19bf`  |
| 606    | No file  | `a46514ea19bf`  |
| 599    | No file  | `a46514ea19bf`  |
| 592    | No file  | `a46514ea19bf`  |
| 586    | No file  | `a46514ea19bf`  |
| 577    | No file  | `a46514ea19bf`  |
| 569    | No file  | `a46514ea19bf`  |
| 561    | No file  | `a46514ea19bf`  |
| 554    | No file  | `a46514ea19bf`  |
| 542    | No file  | `a46514ea19bf`  |
| 532    | No file  | `a46514ea19bf`  |
| 531    | No file  | `a46514ea19bf`  |
| 526    | No file  | `a46514ea19bf`  |
| 521    | No file  | `a46514ea19bf`  |
| 517    | No file  | `a46514ea19bf`  |
| 510    | No file  | `a46514ea19bf`  |
| 508    | No file  | `a46514ea19bf`  |
| 504    | No file  | `a46514ea19bf`  |
| 497    | No file  | `a46514ea19bf`  |
| 491    | No file  | `a46514ea19bf`  |
| 485    | No file  | `a46514ea19bf`  |
| 478    | No file  | `a46514ea19bf`  |
| 472    | No file  | `a46514ea19bf`  |
| 466    | No file  | `a46514ea19bf`  |
| 457    | No file  | `a46514ea19bf`  |
| 452    | No file  | `a46514ea19bf`  |
| 449    | No file  | `a46514ea19bf`  |
| 435    | No file  | `a46514ea19bf`  |

<!-- versions:end -->

## Companion Files

None read. The skeleton the bone ids belong to is a separate [`.pab`](skeleton_pab.md) file; a mesh does not name it, and its Finding a Mesh's Skeleton section has the folder rule that finds it.

## Layout 1

### File Layout

| Offset                       | Type                          | Field                      | Notes |
| ---------------------------- | ----------------------------- | -------------------------- | ----- |
| `+0x00`                      | char[4]                       | magic                      | ASCII `PAR ` |
| `+0x04`                      | u8                            | kind                       | `0x03` on every `PAR` `.pac` |
| `+0x05`                      | u8                            | version                    | `1`, `2` or `3`; version 1 has no Own Bones |
| `+0x06`                      | bytes[10]                     | unknown_06                 | `00 01 02 03 04 05 06 07 08 09` on 2,497 of 2,500 sampled files (client 3483); `00 00 01 02 03 04 05 06 07 08` on 3 |
| `+0x10`                      | Own Bones if version != 1     | own_bones                  |  |
| `own_bones+0x00`             | u8                            | palette_count              |  |
| `own_bones+0x01`             | u32[palette_count]            | bone_palette               | Bone ids; a vertex's `bone_indices` index this list |
| `bone_palette+0x00`          | u8                            | unknown_list_count         | `0` on 1,508 of 2,500 sampled files |
| `bone_palette+0x01`          | u8[unknown_list_count]        | unknown_list               | `0, 1, 2, ...` counting up from 0 in the most frequent sampled values |
| `unknown_list+0x00`          | bytes[8]                      | unknown_after_unknown_list | Two equal u32 values in the most frequent sampled values (`06 00 00 00 06 00 00 00`) |
| `unknown_list+0x08`          | u16                           | submesh_count              | `0` on the 493 placeholder files |
| `unknown_list+0x0A`          | Submesh[submesh_count]        | submeshes                  |  |
| `submeshes+0x00`             | f32[3]                        | bounds_min                 | Equals the smallest LOD 0 vertex x, y, z on 79,514 of 97,151 meshes with vertices |
| `submeshes+0x0C`             | f32[3]                        | bounds_max                 | Equals the largest LOD 0 vertex x, y, z on the same meshes |
| `submeshes+0x18`             | u8                            | group_count                | `0` on 72,540 of 97,644 files (client 3483) |
| `submeshes+0x19`             | Group[group_count]            | groups                     |  |

### Own Bones (variable: 4 bytes + bones)

Versions 2 and 3.

| Offset             | Type                               | Field         | Notes |
| ------------------ | ---------------------------------- | ------------- | ----- |
| `+0x00`            | u32                                | has_own_bones | `1` on 144 files (client 3483), among them `_0033` weapons (`pem_00_gtb_0033_01.pac`); `0` on the rest |
| `+0x04`            | u32 if has_own_bones = 1           | bone_count    |  |
| `bone_count+0x00`  | Bone[bone_count] if has_own_bones = 1 | bones      |  |

### Bone (variable: 306 bytes + constraint axes)

The Bone of a [`.pab` skeleton](skeleton_pab.md) without the name. The 9,027 bones of the 144 files on client 3483 back each reading below.

| Offset   | Type                                   | Field                 | Notes |
| -------- | -------------------------------------- | --------------------- | ----- |
| `+0x00`  | u32                                    | bone_id               | Unique within the file; `bone_palette` holds only these ids in 141 of the 144 files |
| `+0x04`  | i32                                    | parent_index          | `-1` on the first bone; below the bone's own index on every other |
| `+0x08`  | f32[16]                                | world_matrix          | `local_matrix` times the parent's `world_matrix` on all 9,027 bones |
| `+0x48`  | f32[16]                                | inverse_world_matrix  | The inverse of `world_matrix` on all 9,027 bones |
| `+0x88`  | f32[16]                                | local_matrix          | Built from `scale`, `rotation` and `translation` on all 9,027 bones |
| `+0xC8`  | f32[16]                                | inverse_local_matrix  | The inverse of `local_matrix` on all 9,027 bones |
| `+0x108` | f32[3]                                 | scale                 |  |
| `+0x114` | f32[4]                                 | rotation              | Unit quaternion x, y, z, w on all 9,027 bones |
| `+0x124` | f32[3]                                 | translation           | The last row of `local_matrix` |
| `+0x130` | u8                                     | dynamic_shape_count   | `0` on all 9,027 bones; in a `.pab` the shapes follow it |
| `+0x131` | u8                                     | constraint_axis_count | `1` on 38 bones (`psw_00_cts_0033.pac`), `0` on the rest |
| `+0x132` | Constraint Axis[constraint_axis_count] | constraint_axes       |  |

### Constraint Axis (36 bytes)

As in [`skeleton_pab.md`](skeleton_pab.md).

| Offset  | Type   | Field               | Notes |
| ------- | ------ | ------------------- | ----- |
| `+0x00` | f32[3] | position_in_world   | Metres |
| `+0x0C` | f32[3] | twist_axis_in_world | A unit vector |
| `+0x18` | f32[3] | plane_axis_in_world | A unit vector at right angles to `twist_axis_in_world` |

### Submesh (variable: 3 bytes + name and LODs)

| Offset       | Type              | Field          | Notes |
| ------------ | ----------------- | -------------- | ----- |
| `+0x00`      | u8                | name_length    | `0` allowed: the submesh then has no texture |
| `+0x01`      | char[name_length] | name           | Also the texture name without `.dds` (`PHM_00_UW_LB_0017`) |
| `name+0x00`  | u16               | unknown_name_00 | `1` on all 4,690 sampled submeshes |
| `name+0x02`  | Lod[3]            | lods           | Most detailed first; LOD 1 is empty on 34 and LOD 2 on 450 of 4,690 sampled submeshes |

### Lod (variable: 6 bytes + vertices and indices)

| Offset          | Type                 | Field        | Notes |
| --------------- | -------------------- | ------------ | ----- |
| `+0x00`         | u16                  | vertex_count |  |
| `+0x02`         | Vertex[vertex_count] | vertices     |  |
| `vertices+0x00` | u32                  | index_count  | A multiple of 3 |
| `vertices+0x04` | u16[index_count]     | indices      | Three per triangle, each below `vertex_count` |

### Vertex (32 bytes)

| Offset  | Type     | Field        | Notes |
| ------- | -------- | ------------ | ----- |
| `+0x00` | f32[3]   | position     | x, y, z in centimetres, y up |
| `+0x0C` | bytes[4] | unknown_0c   | Not a normal as four u8 scaled to -1 to 1: no byte order matches the face normals |
| `+0x10` | f16[2]   | uv           | Texture u, v; the Model tab maps the texture with them |
| `+0x14` | bytes[4] | unknown_14   | Not a normal by the same test |
| `+0x18` | u8[4]    | bone_indices | Index into `bone_palette`; below `palette_count` wherever the weight is not `0`, on all 4,690 sampled LOD 0 lists |
| `+0x1C` | u8[4]    | bone_weights | Add up to 254 to 257; sorted largest first on 4,685 of 4,690 sampled lists |

### Group (variable: 1 byte + entries)

| Offset  | Type               | Field       | Notes |
| ------- | ------------------ | ----------- | ----- |
| `+0x00` | u8                 | entry_count | 1 to 6 on client 3483 |
| `+0x01` | Entry[entry_count] | entries     |  |

### Entry (16 bytes)

| Offset  | Type   | Field      | Notes |
| ------- | ------ | ---------- | ----- |
| `+0x00` | f32    | unknown_00 |  |
| `+0x04` | f32[3] | unknown_04 | A unit vector on 226,683 of 226,908 entries (client 3483) |

## Notes

- Every `PAR` `.pac` on client 3483 walks to its last byte by this layout (97,644 files, checked with a walk of the groups after the submeshes). `character/model/1_pc/5_pbw/armor/38_underwear/pbw_99_uw_0000.pac` is a 178-byte file with no `PAR ` magic that starts with a `Combination` name and holds a 3-vertex stub.
- 493 files have `submesh_count` `0`: the bounds and groups follow the palette directly (`pew_ew_hel_0031_haircut.pac`).
- The sampled counts come from 2,500 random `.pac` files of client 3483.
- sibercat/PAZ-Unpacker (MIT) gave the first reading of the header versions, the bone records, the palette and the vertex position, UV, bone indices and weights. It reads the bone matrices as local, inverse local, bind and inverse bind transforms; the matrix chain puts the world (bind) matrices first (see Bone).

## Open Questions

### What the Trailer Bounds Cover

`bounds_min` and `bounds_max` equal the LOD 0 vertex box on 79,514 of 97,151 meshes. On the other 17,637 they differ; a box over all LODs, the bind pose or a fixed margin are the first things to compare.

### The Groups of 16-Byte Entries

Each entry is a float and a unit vector, so a plane is the likely reading. `character/partcutdesc.xml` names the parts a worn piece hides, and comparing its entries with the files that have groups may show whether these planes cut a mesh where another piece covers it.

### `unknown_list` and the Eight Bytes After It

A u8-counted list that counts up from 0 on most files, then 8 bytes that hold two equal u32 values in the most frequent sampled values. Their link to `palette_count` or `submesh_count` is not checked yet.

### Palette Ids Outside the Own Bones

On 3 of the 144 files with their own bones, `bone_palette` holds an id that none of the file's bones has (`pcw_00_mgt_0033.pac`, `pcw_00_mgt_0033_in.pac` and `pkow_tail_01.pac`, 2 to 4 ids each). No `.pab` on client 3483 holds them either.

### Vertex Bytes `0x0C` and `0x14`

Four bytes each that change per vertex but are not a plain u8 normal. A decode that matches the face normals would name them.
