# `*.pac` Character Mesh Format

## Purpose

Skinned meshes of player classes, NPCs, monsters, mounts and their gear under `character/model/`. A file holds submeshes, each with three levels of detail; a vertex names up to four bones through the file's bone palette. A submesh's texture is its name plus `.dds` (546 of 548 sampled submeshes find one, in `character/texture/` or `object/texture/`). The Model tab of the browser draws LOD 0 of every submesh (`PAZ-Parser/par_mesh.py`). Byte `0x04` of the `PAR ` header is `0x03`. On client 3483 there are 97,645 `.pac` files: 18,117 of version 1, 12,077 of version 2, 67,450 of version 3, and one that is not a `PAR ` file (see Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                         | Bytes   | Records                        | Row bytes |
| ------ | -------------- | -------------------------------------------- | ------- | ------------------------------ | --------- |
| 1      | 3483 and later | `pem_00_gtb_0033_01.pac`                     | 51,931  | 8 Bone, 1,304 Vertex, 3 Lod    | 32        |
| 1      | 3483 and later | `pew_ew_hel_0031_haircut.pac`                | 125     | 4 Entry, 4 Group               | 16        |
| 1      | 3483 and later | `pfw_00_customizing_lip_left_down_pick.pac`  | 2,002   | 47 Vertex, 3 Lod               | 32        |
| 1      | 3483 and later | `psw_00_cts_0033.pac`                        | 586,120 | 128 Bone, 13,939 Vertex, 3 Lod | 32        |
| 1      | 3483 and later | `psw_00_customizing_eye_right_down_pick.pac` | 2,014   | 47 Vertex, 3 Lod               | 32        |
| 1      | 3483 and later | `psw_10_lb_0057.pac`                         | 73,812  | 1,784 Vertex, 3 Lod, 5 Entry   | 32        |
| 1      | 3483 and later | `pvw_00_customizing_body_rfinger4_pick.pac`  | 2,002   | 49 Vertex, 3 Lod               | 32        |

| Layout | File                                         | Known             | Unknown           |
| ------ | -------------------------------------------- | ----------------- | ----------------- |
| 1      | `pem_00_gtb_0033_01.pac`                     | 39,230 B (75.5%)  | 12,701 B (24.5%)  |
| 1      | `pew_ew_hel_0031_haircut.pac`                | 42 B (33.6%)      | 83 B (66.4%)      |
| 1      | `pfw_00_customizing_lip_left_down_pick.pac`  | 1,605 B (80.2%)   | 397 B (19.8%)     |
| 1      | `psw_00_cts_0033.pac`                        | 437,919 B (74.7%) | 148,201 B (25.3%) |
| 1      | `psw_00_customizing_eye_right_down_pick.pac` | 1,617 B (80.3%)   | 397 B (19.7%)     |
| 1      | `psw_10_lb_0057.pac`                         | 59,430 B (80.5%)  | 14,382 B (19.5%)  |
| 1      | `pvw_00_customizing_body_rfinger4_pick.pac`  | 1,589 B (79.4%)   | 413 B (20.6%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `199ef57f23d2`  |
| 3482   | No file  | `199ef57f23d2`  |
| 3474   | No file  | `199ef57f23d2`  |
| 3473   | No file  | `199ef57f23d2`  |
| 3464   | No file  | `199ef57f23d2`  |
| 3458   | No file  | `199ef57f23d2`  |
| 3454   | No file  | `199ef57f23d2`  |
| 3444   | No file  | `199ef57f23d2`  |
| 3435   | No file  | `199ef57f23d2`  |
| 3426   | No file  | `199ef57f23d2`  |
| 3418   | No file  | `199ef57f23d2`  |
| 3412   | No file  | `199ef57f23d2`  |
| 3402   | No file  | `199ef57f23d2`  |
| 3396   | No file  | `199ef57f23d2`  |
| 3387   | No file  | `199ef57f23d2`  |
| 3381   | No file  | `199ef57f23d2`  |
| 3373   | No file  | `199ef57f23d2`  |
| 3364   | No file  | `199ef57f23d2`  |
| 3356   | No file  | `199ef57f23d2`  |
| 3349   | No file  | `199ef57f23d2`  |
| 3342   | No file  | `199ef57f23d2`  |
| 3335   | No file  | `199ef57f23d2`  |
| 3326   | No file  | `199ef57f23d2`  |
| 3321   | No file  | `199ef57f23d2`  |
| 3314   | No file  | `199ef57f23d2`  |
| 3303   | No file  | `199ef57f23d2`  |
| 3302   | No file  | `199ef57f23d2`  |
| 3293   | No file  | `199ef57f23d2`  |
| 3283   | No file  | `199ef57f23d2`  |
| 3275   | No file  | `199ef57f23d2`  |
| 3267   | No file  | `199ef57f23d2`  |
| 3258   | No file  | `199ef57f23d2`  |
| 3251   | No file  | `199ef57f23d2`  |
| 3242   | No file  | `199ef57f23d2`  |
| 3235   | No file  | `199ef57f23d2`  |
| 3229   | No file  | `199ef57f23d2`  |
| 3212   | No file  | `199ef57f23d2`  |
| 3203   | No file  | `199ef57f23d2`  |
| 3193   | No file  | `199ef57f23d2`  |
| 3186   | No file  | `199ef57f23d2`  |
| 3177   | No file  | `199ef57f23d2`  |
| 3169   | No file  | `199ef57f23d2`  |
| 3158   | No file  | `199ef57f23d2`  |
| 3151   | No file  | `199ef57f23d2`  |
| 3144   | No file  | `199ef57f23d2`  |
| 3133   | No file  | `199ef57f23d2`  |
| 3125   | No file  | `199ef57f23d2`  |
| 3118   | No file  | `199ef57f23d2`  |
| 3111   | No file  | `199ef57f23d2`  |
| 3103   | No file  | `199ef57f23d2`  |
| 3095   | No file  | `199ef57f23d2`  |
| 3086   | No file  | `199ef57f23d2`  |
| 3072   | No file  | `199ef57f23d2`  |
| 3062   | No file  | `199ef57f23d2`  |
| 3052   | No file  | `199ef57f23d2`  |
| 3045   | No file  | `199ef57f23d2`  |
| 3037   | No file  | `199ef57f23d2`  |
| 3030   | No file  | `199ef57f23d2`  |
| 3021   | No file  | `199ef57f23d2`  |
| 3012   | No file  | `199ef57f23d2`  |
| 3002   | No file  | `199ef57f23d2`  |
| 2995   | No file  | `199ef57f23d2`  |
| 2987   | No file  | `199ef57f23d2`  |
| 2978   | No file  | `199ef57f23d2`  |
| 2970   | No file  | `199ef57f23d2`  |
| 2959   | No file  | `199ef57f23d2`  |
| 2951   | No file  | `199ef57f23d2`  |
| 2942   | No file  | `199ef57f23d2`  |
| 2935   | No file  | `199ef57f23d2`  |
| 2932   | No file  | `199ef57f23d2`  |
| 2923   | No file  | `199ef57f23d2`  |
| 2919   | No file  | `199ef57f23d2`  |
| 2907   | No file  | `199ef57f23d2`  |
| 2900   | No file  | `199ef57f23d2`  |
| 2891   | No file  | `199ef57f23d2`  |
| 2882   | No file  | `199ef57f23d2`  |
| 2872   | No file  | `199ef57f23d2`  |
| 2863   | No file  | `199ef57f23d2`  |
| 2855   | No file  | `199ef57f23d2`  |
| 2849   | No file  | `199ef57f23d2`  |
| 2844   | No file  | `199ef57f23d2`  |
| 2834   | No file  | `199ef57f23d2`  |
| 2825   | No file  | `199ef57f23d2`  |
| 2819   | No file  | `199ef57f23d2`  |
| 2811   | No file  | `199ef57f23d2`  |
| 2803   | No file  | `199ef57f23d2`  |
| 2794   | No file  | `199ef57f23d2`  |
| 2783   | No file  | `199ef57f23d2`  |
| 2774   | No file  | `199ef57f23d2`  |
| 2765   | No file  | `199ef57f23d2`  |
| 2756   | No file  | `199ef57f23d2`  |
| 2750   | No file  | `199ef57f23d2`  |
| 2743   | No file  | `199ef57f23d2`  |
| 2736   | No file  | `199ef57f23d2`  |
| 2726   | No file  | `199ef57f23d2`  |
| 2717   | No file  | `199ef57f23d2`  |
| 2709   | No file  | `199ef57f23d2`  |
| 2703   | No file  | `199ef57f23d2`  |
| 2695   | No file  | `199ef57f23d2`  |
| 2684   | No file  | `199ef57f23d2`  |
| 2672   | No file  | `199ef57f23d2`  |
| 2665   | No file  | `199ef57f23d2`  |
| 2657   | No file  | `199ef57f23d2`  |
| 2649   | No file  | `199ef57f23d2`  |
| 2644   | No file  | `199ef57f23d2`  |
| 2637   | No file  | `199ef57f23d2`  |
| 2629   | No file  | `199ef57f23d2`  |
| 2619   | No file  | `199ef57f23d2`  |
| 2612   | No file  | `199ef57f23d2`  |
| 2606   | No file  | `199ef57f23d2`  |
| 2602   | No file  | `199ef57f23d2`  |
| 2601   | No file  | `199ef57f23d2`  |
| 2592   | No file  | `199ef57f23d2`  |
| 2583   | No file  | `199ef57f23d2`  |
| 2575   | No file  | `199ef57f23d2`  |
| 2567   | No file  | `199ef57f23d2`  |
| 2560   | No file  | `199ef57f23d2`  |
| 2553   | No file  | `199ef57f23d2`  |
| 2545   | No file  | `199ef57f23d2`  |
| 2538   | No file  | `199ef57f23d2`  |
| 2529   | No file  | `199ef57f23d2`  |
| 2519   | No file  | `199ef57f23d2`  |
| 2513   | No file  | `199ef57f23d2`  |
| 2510   | No file  | `199ef57f23d2`  |
| 2507   | No file  | `199ef57f23d2`  |
| 2503   | No file  | `199ef57f23d2`  |
| 2498   | No file  | `199ef57f23d2`  |
| 2492   | No file  | `199ef57f23d2`  |
| 2487   | No file  | `199ef57f23d2`  |
| 2480   | No file  | `199ef57f23d2`  |
| 2474   | No file  | `199ef57f23d2`  |
| 2468   | No file  | `199ef57f23d2`  |
| 2460   | No file  | `199ef57f23d2`  |
| 2453   | No file  | `199ef57f23d2`  |
| 2444   | No file  | `199ef57f23d2`  |
| 2438   | No file  | `199ef57f23d2`  |
| 2434   | No file  | `199ef57f23d2`  |
| 2429   | No file  | `199ef57f23d2`  |
| 2421   | No file  | `199ef57f23d2`  |
| 2414   | No file  | `199ef57f23d2`  |
| 2407   | No file  | `199ef57f23d2`  |
| 2401   | No file  | `199ef57f23d2`  |
| 2397   | No file  | `199ef57f23d2`  |
| 2393   | No file  | `199ef57f23d2`  |
| 2384   | No file  | `199ef57f23d2`  |
| 2378   | No file  | `199ef57f23d2`  |
| 2372   | No file  | `199ef57f23d2`  |
| 2358   | No file  | `199ef57f23d2`  |
| 2352   | No file  | `199ef57f23d2`  |
| 2347   | No file  | `199ef57f23d2`  |
| 2343   | No file  | `199ef57f23d2`  |
| 2335   | No file  | `199ef57f23d2`  |
| 2327   | No file  | `199ef57f23d2`  |
| 2324   | No file  | `199ef57f23d2`  |
| 2319   | No file  | `199ef57f23d2`  |
| 2313   | No file  | `199ef57f23d2`  |
| 2308   | No file  | `199ef57f23d2`  |
| 2302   | No file  | `199ef57f23d2`  |
| 2295   | No file  | `199ef57f23d2`  |
| 2290   | No file  | `199ef57f23d2`  |
| 2284   | No file  | `199ef57f23d2`  |
| 2276   | No file  | `199ef57f23d2`  |
| 2269   | No file  | `199ef57f23d2`  |
| 2259   | No file  | `199ef57f23d2`  |
| 2250   | No file  | `199ef57f23d2`  |
| 2243   | No file  | `199ef57f23d2`  |
| 2235   | No file  | `199ef57f23d2`  |
| 2229   | No file  | `199ef57f23d2`  |
| 2224   | No file  | `199ef57f23d2`  |
| 2218   | No file  | `199ef57f23d2`  |
| 2215   | No file  | `199ef57f23d2`  |
| 2207   | No file  | `199ef57f23d2`  |
| 2203   | No file  | `199ef57f23d2`  |
| 2196   | No file  | `199ef57f23d2`  |
| 2192   | No file  | `199ef57f23d2`  |
| 2189   | No file  | `199ef57f23d2`  |
| 2183   | No file  | `199ef57f23d2`  |
| 2179   | No file  | `199ef57f23d2`  |
| 2171   | No file  | `199ef57f23d2`  |
| 2163   | No file  | `199ef57f23d2`  |
| 2156   | No file  | `199ef57f23d2`  |
| 2151   | No file  | `199ef57f23d2`  |
| 2147   | No file  | `199ef57f23d2`  |
| 2142   | No file  | `199ef57f23d2`  |
| 2138   | No file  | `199ef57f23d2`  |
| 2134   | No file  | `199ef57f23d2`  |
| 2130   | No file  | `199ef57f23d2`  |
| 2122   | No file  | `199ef57f23d2`  |
| 2107   | No file  | `199ef57f23d2`  |
| 2098   | No file  | `199ef57f23d2`  |
| 2089   | No file  | `199ef57f23d2`  |
| 2081   | No file  | `199ef57f23d2`  |
| 2073   | No file  | `199ef57f23d2`  |
| 2067   | No file  | `199ef57f23d2`  |
| 2063   | No file  | `199ef57f23d2`  |
| 2059   | No file  | `199ef57f23d2`  |
| 2052   | No file  | `199ef57f23d2`  |
| 2044   | No file  | `199ef57f23d2`  |
| 2039   | No file  | `199ef57f23d2`  |
| 2032   | No file  | `199ef57f23d2`  |
| 2025   | No file  | `199ef57f23d2`  |
| 2011   | No file  | `199ef57f23d2`  |
| 2005   | No file  | `199ef57f23d2`  |
| 2000   | No file  | `199ef57f23d2`  |
| 1996   | No file  | `199ef57f23d2`  |
| 1991   | No file  | `199ef57f23d2`  |
| 1985   | No file  | `199ef57f23d2`  |
| 1980   | No file  | `199ef57f23d2`  |
| 1969   | No file  | `199ef57f23d2`  |
| 1964   | No file  | `199ef57f23d2`  |
| 1958   | No file  | `199ef57f23d2`  |
| 1950   | No file  | `199ef57f23d2`  |
| 1945   | No file  | `199ef57f23d2`  |
| 1937   | No file  | `199ef57f23d2`  |
| 1933   | No file  | `199ef57f23d2`  |
| 1927   | No file  | `199ef57f23d2`  |
| 1921   | No file  | `199ef57f23d2`  |
| 1914   | No file  | `199ef57f23d2`  |
| 1908   | No file  | `199ef57f23d2`  |
| 1897   | No file  | `199ef57f23d2`  |
| 1892   | No file  | `199ef57f23d2`  |
| 1886   | No file  | `199ef57f23d2`  |
| 1881   | No file  | `199ef57f23d2`  |
| 1871   | No file  | `199ef57f23d2`  |
| 1866   | No file  | `199ef57f23d2`  |
| 1862   | No file  | `199ef57f23d2`  |
| 1854   | No file  | `199ef57f23d2`  |
| 1846   | No file  | `199ef57f23d2`  |
| 1838   | No file  | `199ef57f23d2`  |
| 1832   | No file  | `199ef57f23d2`  |
| 1826   | No file  | `199ef57f23d2`  |
| 1822   | No file  | `199ef57f23d2`  |
| 1818   | No file  | `199ef57f23d2`  |
| 1804   | No file  | `199ef57f23d2`  |
| 1794   | No file  | `199ef57f23d2`  |
| 1790   | No file  | `199ef57f23d2`  |
| 1784   | No file  | `199ef57f23d2`  |
| 1774   | No file  | `199ef57f23d2`  |
| 1771   | No file  | `199ef57f23d2`  |
| 1762   | No file  | `199ef57f23d2`  |
| 1759   | No file  | `199ef57f23d2`  |
| 1754   | No file  | `199ef57f23d2`  |
| 1749   | No file  | `199ef57f23d2`  |
| 1743   | No file  | `199ef57f23d2`  |
| 1737   | No file  | `199ef57f23d2`  |
| 1731   | No file  | `199ef57f23d2`  |
| 1725   | No file  | `199ef57f23d2`  |
| 1717   | No file  | `199ef57f23d2`  |
| 1710   | No file  | `199ef57f23d2`  |
| 1704   | No file  | `199ef57f23d2`  |
| 1698   | No file  | `199ef57f23d2`  |
| 1690   | No file  | `199ef57f23d2`  |
| 1685   | No file  | `199ef57f23d2`  |
| 1680   | No file  | `199ef57f23d2`  |
| 1674   | No file  | `199ef57f23d2`  |
| 1668   | No file  | `199ef57f23d2`  |
| 1659   | No file  | `199ef57f23d2`  |
| 1649   | No file  | `199ef57f23d2`  |
| 1642   | No file  | `199ef57f23d2`  |
| 1636   | No file  | `199ef57f23d2`  |
| 1628   | No file  | `199ef57f23d2`  |
| 1622   | No file  | `199ef57f23d2`  |
| 1614   | No file  | `199ef57f23d2`  |
| 1608   | No file  | `199ef57f23d2`  |
| 1602   | No file  | `199ef57f23d2`  |
| 1598   | No file  | `199ef57f23d2`  |
| 1594   | No file  | `199ef57f23d2`  |
| 1590   | No file  | `199ef57f23d2`  |
| 1587   | No file  | `199ef57f23d2`  |
| 1584   | No file  | `199ef57f23d2`  |
| 1579   | No file  | `199ef57f23d2`  |
| 1572   | No file  | `199ef57f23d2`  |
| 1565   | No file  | `199ef57f23d2`  |
| 1559   | No file  | `199ef57f23d2`  |
| 1554   | No file  | `199ef57f23d2`  |
| 1547   | No file  | `199ef57f23d2`  |
| 1537   | No file  | `199ef57f23d2`  |
| 1529   | No file  | `199ef57f23d2`  |
| 1524   | No file  | `199ef57f23d2`  |
| 1519   | No file  | `199ef57f23d2`  |
| 1509   | No file  | `199ef57f23d2`  |
| 1506   | No file  | `199ef57f23d2`  |
| 1504   | No file  | `199ef57f23d2`  |
| 1500   | No file  | `199ef57f23d2`  |
| 1493   | No file  | `199ef57f23d2`  |
| 1489   | No file  | `199ef57f23d2`  |
| 1485   | No file  | `199ef57f23d2`  |
| 1481   | No file  | `199ef57f23d2`  |
| 1474   | No file  | `199ef57f23d2`  |
| 1466   | No file  | `199ef57f23d2`  |
| 1462   | No file  | `199ef57f23d2`  |
| 1459   | No file  | `199ef57f23d2`  |
| 1453   | No file  | `199ef57f23d2`  |
| 1450   | No file  | `199ef57f23d2`  |
| 1445   | No file  | `199ef57f23d2`  |
| 1439   | No file  | `199ef57f23d2`  |
| 1433   | No file  | `199ef57f23d2`  |
| 1430   | No file  | `199ef57f23d2`  |
| 1426   | No file  | `199ef57f23d2`  |
| 1421   | No file  | `199ef57f23d2`  |
| 1417   | No file  | `199ef57f23d2`  |
| 1416   | No file  | `199ef57f23d2`  |
| 1409   | No file  | `199ef57f23d2`  |
| 1405   | No file  | `199ef57f23d2`  |
| 1401   | No file  | `199ef57f23d2`  |
| 1396   | No file  | `199ef57f23d2`  |
| 1391   | No file  | `199ef57f23d2`  |
| 1390   | No file  | `199ef57f23d2`  |
| 1386   | No file  | `199ef57f23d2`  |
| 1381   | No file  | `199ef57f23d2`  |
| 1379   | No file  | `199ef57f23d2`  |
| 1372   | No file  | `199ef57f23d2`  |
| 1366   | No file  | `199ef57f23d2`  |
| 1364   | No file  | `199ef57f23d2`  |
| 1363   | No file  | `199ef57f23d2`  |
| 1360   | No file  | `199ef57f23d2`  |
| 1358   | No file  | `199ef57f23d2`  |
| 1355   | No file  | `199ef57f23d2`  |
| 1351   | No file  | `199ef57f23d2`  |
| 1348   | No file  | `199ef57f23d2`  |
| 1346   | No file  | `199ef57f23d2`  |
| 1341   | No file  | `199ef57f23d2`  |
| 1340   | No file  | `199ef57f23d2`  |
| 1338   | No file  | `199ef57f23d2`  |
| 1335   | No file  | `199ef57f23d2`  |
| 1333   | No file  | `199ef57f23d2`  |
| 1329   | No file  | `199ef57f23d2`  |
| 1327   | No file  | `199ef57f23d2`  |
| 1324   | No file  | `199ef57f23d2`  |
| 1321   | No file  | `199ef57f23d2`  |
| 1319   | No file  | `199ef57f23d2`  |
| 1318   | No file  | `199ef57f23d2`  |
| 1316   | No file  | `199ef57f23d2`  |
| 1313   | No file  | `199ef57f23d2`  |
| 1311   | No file  | `199ef57f23d2`  |
| 1309   | No file  | `199ef57f23d2`  |
| 1304   | No file  | `199ef57f23d2`  |
| 1292   | No file  | `199ef57f23d2`  |
| 1286   | No file  | `199ef57f23d2`  |
| 1280   | No file  | `199ef57f23d2`  |
| 1276   | No file  | `199ef57f23d2`  |
| 1267   | No file  | `199ef57f23d2`  |
| 1261   | No file  | `199ef57f23d2`  |
| 1256   | No file  | `199ef57f23d2`  |
| 1250   | No file  | `199ef57f23d2`  |
| 1246   | No file  | `199ef57f23d2`  |
| 1239   | No file  | `199ef57f23d2`  |
| 1230   | No file  | `199ef57f23d2`  |
| 1226   | No file  | `199ef57f23d2`  |
| 1220   | No file  | `199ef57f23d2`  |
| 1217   | No file  | `199ef57f23d2`  |
| 1211   | No file  | `199ef57f23d2`  |
| 1210   | No file  | `199ef57f23d2`  |
| 1208   | No file  | `199ef57f23d2`  |
| 1203   | No file  | `199ef57f23d2`  |
| 1197   | No file  | `199ef57f23d2`  |
| 1194   | No file  | `199ef57f23d2`  |
| 1192   | No file  | `199ef57f23d2`  |
| 1187   | No file  | `199ef57f23d2`  |
| 1183   | No file  | `199ef57f23d2`  |
| 1177   | No file  | `199ef57f23d2`  |
| 1173   | No file  | `199ef57f23d2`  |
| 1167   | No file  | `199ef57f23d2`  |
| 1164   | No file  | `199ef57f23d2`  |
| 1156   | No file  | `199ef57f23d2`  |
| 1149   | No file  | `199ef57f23d2`  |
| 1144   | No file  | `199ef57f23d2`  |
| 1137   | No file  | `199ef57f23d2`  |
| 1132   | No file  | `199ef57f23d2`  |
| 1127   | No file  | `199ef57f23d2`  |
| 1122   | No file  | `199ef57f23d2`  |
| 1118   | No file  | `199ef57f23d2`  |
| 1114   | No file  | `199ef57f23d2`  |
| 1109   | No file  | `199ef57f23d2`  |
| 1102   | No file  | `199ef57f23d2`  |
| 1096   | No file  | `199ef57f23d2`  |
| 1088   | No file  | `199ef57f23d2`  |
| 1081   | No file  | `199ef57f23d2`  |
| 1076   | No file  | `199ef57f23d2`  |
| 1069   | No file  | `199ef57f23d2`  |
| 1064   | No file  | `199ef57f23d2`  |
| 1058   | No file  | `199ef57f23d2`  |
| 1051   | No file  | `199ef57f23d2`  |
| 1044   | No file  | `199ef57f23d2`  |
| 1036   | No file  | `199ef57f23d2`  |
| 1026   | No file  | `199ef57f23d2`  |
| 1016   | No file  | `199ef57f23d2`  |
| 1009   | No file  | `199ef57f23d2`  |
| 1005   | No file  | `199ef57f23d2`  |
| 1000   | No file  | `199ef57f23d2`  |
| 998    | No file  | `199ef57f23d2`  |
| 990    | No file  | `199ef57f23d2`  |
| 979    | No file  | `199ef57f23d2`  |
| 972    | No file  | `199ef57f23d2`  |
| 963    | No file  | `199ef57f23d2`  |
| 955    | No file  | `199ef57f23d2`  |
| 946    | No file  | `199ef57f23d2`  |
| 938    | No file  | `199ef57f23d2`  |
| 927    | No file  | `199ef57f23d2`  |
| 911    | No file  | `199ef57f23d2`  |
| 904    | No file  | `199ef57f23d2`  |
| 899    | No file  | `199ef57f23d2`  |
| 894    | No file  | `199ef57f23d2`  |
| 885    | No file  | `199ef57f23d2`  |
| 879    | No file  | `199ef57f23d2`  |
| 872    | No file  | `199ef57f23d2`  |
| 864    | No file  | `199ef57f23d2`  |
| 855    | No file  | `199ef57f23d2`  |
| 853    | No file  | `199ef57f23d2`  |
| 845    | No file  | `199ef57f23d2`  |
| 837    | No file  | `199ef57f23d2`  |
| 829    | No file  | `199ef57f23d2`  |
| 822    | No file  | `199ef57f23d2`  |
| 814    | No file  | `199ef57f23d2`  |
| 805    | No file  | `199ef57f23d2`  |
| 794    | No file  | `199ef57f23d2`  |
| 787    | No file  | `199ef57f23d2`  |
| 780    | No file  | `199ef57f23d2`  |
| 771    | No file  | `199ef57f23d2`  |
| 760    | No file  | `199ef57f23d2`  |
| 748    | No file  | `199ef57f23d2`  |
| 741    | No file  | `199ef57f23d2`  |
| 736    | No file  | `199ef57f23d2`  |
| 731    | No file  | `199ef57f23d2`  |
| 723    | No file  | `199ef57f23d2`  |
| 711    | No file  | `199ef57f23d2`  |
| 707    | No file  | `199ef57f23d2`  |
| 697    | No file  | `199ef57f23d2`  |
| 689    | No file  | `199ef57f23d2`  |
| 683    | No file  | `199ef57f23d2`  |
| 678    | No file  | `199ef57f23d2`  |
| 670    | No file  | `199ef57f23d2`  |
| 661    | No file  | `199ef57f23d2`  |
| 656    | No file  | `199ef57f23d2`  |
| 652    | No file  | `199ef57f23d2`  |
| 643    | No file  | `199ef57f23d2`  |
| 637    | No file  | `199ef57f23d2`  |
| 630    | No file  | `199ef57f23d2`  |
| 627    | No file  | `199ef57f23d2`  |
| 621    | No file  | `199ef57f23d2`  |
| 617    | No file  | `199ef57f23d2`  |
| 615    | No file  | `199ef57f23d2`  |
| 606    | No file  | `199ef57f23d2`  |
| 599    | No file  | `199ef57f23d2`  |
| 592    | No file  | `199ef57f23d2`  |
| 586    | No file  | `199ef57f23d2`  |
| 577    | No file  | `199ef57f23d2`  |
| 569    | No file  | `199ef57f23d2`  |
| 561    | No file  | `199ef57f23d2`  |
| 554    | No file  | `199ef57f23d2`  |
| 542    | No file  | `199ef57f23d2`  |
| 532    | No file  | `199ef57f23d2`  |
| 531    | No file  | `199ef57f23d2`  |
| 526    | No file  | `199ef57f23d2`  |
| 521    | No file  | `199ef57f23d2`  |
| 517    | No file  | `199ef57f23d2`  |
| 510    | No file  | `199ef57f23d2`  |
| 508    | No file  | `199ef57f23d2`  |
| 504    | No file  | `199ef57f23d2`  |
| 497    | No file  | `199ef57f23d2`  |
| 491    | No file  | `199ef57f23d2`  |
| 485    | No file  | `199ef57f23d2`  |
| 478    | No file  | `199ef57f23d2`  |
| 472    | No file  | `199ef57f23d2`  |
| 466    | No file  | `199ef57f23d2`  |
| 457    | No file  | `199ef57f23d2`  |
| 452    | No file  | `199ef57f23d2`  |
| 449    | No file  | `199ef57f23d2`  |
| 435    | No file  | `199ef57f23d2`  |

<!-- versions:end -->

## Companion Files

None read. The skeleton the bone ids belong to is a separate `.pab` file; a mesh does not name it.

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

### Bone (variable: 306 bytes + extra block)

The 9,027 bones of the 144 files on client 3483 back each reading below.

| Offset  | Type                       | Field         | Notes |
| ------- | -------------------------- | ------------- | ----- |
| `+0x00` | u32                        | bone_id       | Unique within the file; `bone_palette` holds only these ids in 141 of the 144 files |
| `+0x04` | i32                        | parent_index  | `-1` on the first bone; below the bone's own index on every other |
| `+0x08` | f32[4][16]                 | unknown_08    | Four 4 x 4 float matrices |
| `+0x108`| f32[3]                     | unknown_108   |  |
| `+0x114`| f32[4]                     | rotation      | Unit quaternion on all 9,027 bones |
| `+0x124`| f32[3]                     | unknown_124   |  |
| `+0x130`| u8                         | unknown_130   | `0` on all 9,027 bones |
| `+0x131`| u8                         | has_extra     | `1` on 38 bones (`psw_00_cts_0033.pac`), `0` on the rest |
| `+0x132`| bytes[36] if has_extra = 1 | unknown_132   |  |

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
- sibercat/PAZ-Unpacker (MIT) gave the first reading of the header versions, the bone records, the palette and the vertex position, UV, bone indices and weights. It reads the bone matrices as local, inverse local, bind and inverse bind transforms and `unknown_108` and `unknown_124` as scale and translation; none of these is confirmed here.

## Open Questions

### What the Trailer Bounds Cover

`bounds_min` and `bounds_max` equal the LOD 0 vertex box on 79,514 of 97,151 meshes. On the other 17,637 they differ; a box over all LODs, the bind pose or a fixed margin are the first things to compare.

### The Groups of 16-Byte Entries

Each entry is a float and a unit vector, so a plane is the likely reading. `character/partcutdesc.xml` names the parts a worn piece hides, and comparing its entries with the files that have groups may show whether these planes cut a mesh where another piece covers it.

### `unknown_list` and the Eight Bytes After It

A u8-counted list that counts up from 0 on most files, then 8 bytes that hold two equal u32 values in the most frequent sampled values. Their link to `palette_count` or `submesh_count` is not checked yet.

### Palette Ids Outside the Own Bones

On 3 of the 144 files with their own bones, `bone_palette` holds an id that none of the file's bones has. The `.pab` skeletons of the same class may hold it.

### Vertex Bytes `0x0C` and `0x14`

Four bytes each that change per vertex but are not a plain u8 normal. A decode that matches the face normals would name them.
