# `*.pam` Static Mesh Format

## Purpose

Static meshes: world objects, houses, furniture, decals and the sector LOD meshes of `mapdata_real/`. A file holds one triangle list split into materials, each with the file name of its texture (`wood_66.dds`), which sits in the mesh's own folder or in `object/texture/`. The Model tab of the browser draws them (`PAZ-Parser/par_mesh.py`). It is one of the `PAR ` files, with [`*.pcm`](mesh_pcm.md) and [`*.pac`](mesh_pac.md); byte `0x04` names the kind (`0x06` here). On client 3483 there are 61,175 files: 2,739 of version 4, 49,515 of version 5 and 8,921 of version 6.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes     | Records                        | Row bytes |
| ------ | -------------- | --------------------------------- | --------- | ------------------------------ | --------- |
| 1      | 3483 and later | `52_10_0_lod.pam`                 | 3,267,132 | 90,802 Vertex                  | 28        |
| 1      | 3483 and later | `barricade_metal_01_hh_nr.pam`    | 2,056     | 24 Vertex                      | 28        |
| 1      | 3483 and later | `devildom_lava_08a.pam`           | 2,008     | 18 Vertex V6                   | 32        |
| 1      | 3483 and later | `inhouse_camping_ori_camp_01.pam` | 5,927,188 | 26 Material, 145,769 Vertex V6 | 32        |
| 1      | 3483 and later | `ori_obj_bamboo_basket_01.pam`    | 1,040     | -                              | -         |
| 1      | 3483 and later | `sectorhlod_-19_-1_-6_2_9.pam`    | 2,004     | 22 Vertex                      | 28        |

| Layout | File                              | Known               | Unknown             |
| ------ | --------------------------------- | ------------------- | ------------------- |
| 1      | `52_10_0_lod.pam`                 | 2,176,499 B (66.6%) | 1,090,633 B (33.4%) |
| 1      | `barricade_metal_01_hh_nr.pam`    | 763 B (37.1%)       | 1,293 B (62.9%)     |
| 1      | `devildom_lava_08a.pam`           | 715 B (35.6%)       | 1,293 B (64.4%)     |
| 1      | `inhouse_camping_ori_camp_01.pam` | 3,593,879 B (60.6%) | 2,333,309 B (39.4%) |
| 1      | `ori_obj_bamboo_basket_01.pam`    | 35 B (3.4%)         | 1,005 B (96.6%)     |
| 1      | `sectorhlod_-19_-1_-6_2_9.pam`    | 731 B (36.5%)       | 1,273 B (63.5%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `dec78e49bfee`  |
| 3482   | No file  | `dec78e49bfee`  |
| 3474   | No file  | `dec78e49bfee`  |
| 3473   | No file  | `dec78e49bfee`  |
| 3464   | No file  | `dec78e49bfee`  |
| 3458   | No file  | `dec78e49bfee`  |
| 3454   | No file  | `dec78e49bfee`  |
| 3444   | No file  | `dec78e49bfee`  |
| 3435   | No file  | `dec78e49bfee`  |
| 3426   | No file  | `dec78e49bfee`  |
| 3418   | No file  | `dec78e49bfee`  |
| 3412   | No file  | `dec78e49bfee`  |
| 3402   | No file  | `dec78e49bfee`  |
| 3396   | No file  | `dec78e49bfee`  |
| 3387   | No file  | `dec78e49bfee`  |
| 3381   | No file  | `dec78e49bfee`  |
| 3373   | No file  | `dec78e49bfee`  |
| 3364   | No file  | `dec78e49bfee`  |
| 3356   | No file  | `dec78e49bfee`  |
| 3349   | No file  | `dec78e49bfee`  |
| 3342   | No file  | `dec78e49bfee`  |
| 3335   | No file  | `dec78e49bfee`  |
| 3326   | No file  | `dec78e49bfee`  |
| 3321   | No file  | `dec78e49bfee`  |
| 3314   | No file  | `dec78e49bfee`  |
| 3303   | No file  | `dec78e49bfee`  |
| 3302   | No file  | `dec78e49bfee`  |
| 3293   | No file  | `dec78e49bfee`  |
| 3283   | No file  | `dec78e49bfee`  |
| 3275   | No file  | `dec78e49bfee`  |
| 3267   | No file  | `dec78e49bfee`  |
| 3258   | No file  | `dec78e49bfee`  |
| 3251   | No file  | `dec78e49bfee`  |
| 3242   | No file  | `dec78e49bfee`  |
| 3235   | No file  | `dec78e49bfee`  |
| 3229   | No file  | `dec78e49bfee`  |
| 3212   | No file  | `dec78e49bfee`  |
| 3203   | No file  | `dec78e49bfee`  |
| 3193   | No file  | `dec78e49bfee`  |
| 3186   | No file  | `dec78e49bfee`  |
| 3177   | No file  | `dec78e49bfee`  |
| 3169   | No file  | `dec78e49bfee`  |
| 3158   | No file  | `dec78e49bfee`  |
| 3151   | No file  | `dec78e49bfee`  |
| 3144   | No file  | `dec78e49bfee`  |
| 3133   | No file  | `dec78e49bfee`  |
| 3125   | No file  | `dec78e49bfee`  |
| 3118   | No file  | `dec78e49bfee`  |
| 3111   | No file  | `dec78e49bfee`  |
| 3103   | No file  | `dec78e49bfee`  |
| 3095   | No file  | `dec78e49bfee`  |
| 3086   | No file  | `dec78e49bfee`  |
| 3072   | No file  | `dec78e49bfee`  |
| 3062   | No file  | `dec78e49bfee`  |
| 3052   | No file  | `dec78e49bfee`  |
| 3045   | No file  | `dec78e49bfee`  |
| 3037   | No file  | `dec78e49bfee`  |
| 3030   | No file  | `dec78e49bfee`  |
| 3021   | No file  | `dec78e49bfee`  |
| 3012   | No file  | `dec78e49bfee`  |
| 3002   | No file  | `dec78e49bfee`  |
| 2995   | No file  | `dec78e49bfee`  |
| 2987   | No file  | `dec78e49bfee`  |
| 2978   | No file  | `dec78e49bfee`  |
| 2970   | No file  | `dec78e49bfee`  |
| 2959   | No file  | `dec78e49bfee`  |
| 2951   | No file  | `dec78e49bfee`  |
| 2942   | No file  | `dec78e49bfee`  |
| 2935   | No file  | `dec78e49bfee`  |
| 2932   | No file  | `dec78e49bfee`  |
| 2923   | No file  | `dec78e49bfee`  |
| 2919   | No file  | `dec78e49bfee`  |
| 2907   | No file  | `dec78e49bfee`  |
| 2900   | No file  | `dec78e49bfee`  |
| 2891   | No file  | `dec78e49bfee`  |
| 2882   | No file  | `dec78e49bfee`  |
| 2872   | No file  | `dec78e49bfee`  |
| 2863   | No file  | `dec78e49bfee`  |
| 2855   | No file  | `dec78e49bfee`  |
| 2849   | No file  | `dec78e49bfee`  |
| 2844   | No file  | `dec78e49bfee`  |
| 2834   | No file  | `dec78e49bfee`  |
| 2825   | No file  | `dec78e49bfee`  |
| 2819   | No file  | `dec78e49bfee`  |
| 2811   | No file  | `dec78e49bfee`  |
| 2803   | No file  | `dec78e49bfee`  |
| 2794   | No file  | `dec78e49bfee`  |
| 2783   | No file  | `dec78e49bfee`  |
| 2774   | No file  | `dec78e49bfee`  |
| 2765   | No file  | `dec78e49bfee`  |
| 2756   | No file  | `dec78e49bfee`  |
| 2750   | No file  | `dec78e49bfee`  |
| 2743   | No file  | `dec78e49bfee`  |
| 2736   | No file  | `dec78e49bfee`  |
| 2726   | No file  | `dec78e49bfee`  |
| 2717   | No file  | `dec78e49bfee`  |
| 2709   | No file  | `dec78e49bfee`  |
| 2703   | No file  | `dec78e49bfee`  |
| 2695   | No file  | `dec78e49bfee`  |
| 2684   | No file  | `dec78e49bfee`  |
| 2672   | No file  | `dec78e49bfee`  |
| 2665   | No file  | `dec78e49bfee`  |
| 2657   | No file  | `dec78e49bfee`  |
| 2649   | No file  | `dec78e49bfee`  |
| 2644   | No file  | `dec78e49bfee`  |
| 2637   | No file  | `dec78e49bfee`  |
| 2629   | No file  | `dec78e49bfee`  |
| 2619   | No file  | `dec78e49bfee`  |
| 2612   | No file  | `dec78e49bfee`  |
| 2606   | No file  | `dec78e49bfee`  |
| 2602   | No file  | `dec78e49bfee`  |
| 2601   | No file  | `dec78e49bfee`  |
| 2592   | No file  | `dec78e49bfee`  |
| 2583   | No file  | `dec78e49bfee`  |
| 2575   | No file  | `dec78e49bfee`  |
| 2567   | No file  | `dec78e49bfee`  |
| 2560   | No file  | `dec78e49bfee`  |
| 2553   | No file  | `dec78e49bfee`  |
| 2545   | No file  | `dec78e49bfee`  |
| 2538   | No file  | `dec78e49bfee`  |
| 2529   | No file  | `dec78e49bfee`  |
| 2519   | No file  | `dec78e49bfee`  |
| 2513   | No file  | `dec78e49bfee`  |
| 2510   | No file  | `dec78e49bfee`  |
| 2507   | No file  | `dec78e49bfee`  |
| 2503   | No file  | `dec78e49bfee`  |
| 2498   | No file  | `dec78e49bfee`  |
| 2492   | No file  | `dec78e49bfee`  |
| 2487   | No file  | `dec78e49bfee`  |
| 2480   | No file  | `dec78e49bfee`  |
| 2474   | No file  | `dec78e49bfee`  |
| 2468   | No file  | `dec78e49bfee`  |
| 2460   | No file  | `dec78e49bfee`  |
| 2453   | No file  | `dec78e49bfee`  |
| 2444   | No file  | `dec78e49bfee`  |
| 2438   | No file  | `dec78e49bfee`  |
| 2434   | No file  | `dec78e49bfee`  |
| 2429   | No file  | `dec78e49bfee`  |
| 2421   | No file  | `dec78e49bfee`  |
| 2414   | No file  | `dec78e49bfee`  |
| 2407   | No file  | `dec78e49bfee`  |
| 2401   | No file  | `dec78e49bfee`  |
| 2397   | No file  | `dec78e49bfee`  |
| 2393   | No file  | `dec78e49bfee`  |
| 2384   | No file  | `dec78e49bfee`  |
| 2378   | No file  | `dec78e49bfee`  |
| 2372   | No file  | `dec78e49bfee`  |
| 2358   | No file  | `dec78e49bfee`  |
| 2352   | No file  | `dec78e49bfee`  |
| 2347   | No file  | `dec78e49bfee`  |
| 2343   | No file  | `dec78e49bfee`  |
| 2335   | No file  | `dec78e49bfee`  |
| 2327   | No file  | `dec78e49bfee`  |
| 2324   | No file  | `dec78e49bfee`  |
| 2319   | No file  | `dec78e49bfee`  |
| 2313   | No file  | `dec78e49bfee`  |
| 2308   | No file  | `dec78e49bfee`  |
| 2302   | No file  | `dec78e49bfee`  |
| 2295   | No file  | `dec78e49bfee`  |
| 2290   | No file  | `dec78e49bfee`  |
| 2284   | No file  | `dec78e49bfee`  |
| 2276   | No file  | `dec78e49bfee`  |
| 2269   | No file  | `dec78e49bfee`  |
| 2259   | No file  | `dec78e49bfee`  |
| 2250   | No file  | `dec78e49bfee`  |
| 2243   | No file  | `dec78e49bfee`  |
| 2235   | No file  | `dec78e49bfee`  |
| 2229   | No file  | `dec78e49bfee`  |
| 2224   | No file  | `dec78e49bfee`  |
| 2218   | No file  | `dec78e49bfee`  |
| 2215   | No file  | `dec78e49bfee`  |
| 2207   | No file  | `dec78e49bfee`  |
| 2203   | No file  | `dec78e49bfee`  |
| 2196   | No file  | `dec78e49bfee`  |
| 2192   | No file  | `dec78e49bfee`  |
| 2189   | No file  | `dec78e49bfee`  |
| 2183   | No file  | `dec78e49bfee`  |
| 2179   | No file  | `dec78e49bfee`  |
| 2171   | No file  | `dec78e49bfee`  |
| 2163   | No file  | `dec78e49bfee`  |
| 2156   | No file  | `dec78e49bfee`  |
| 2151   | No file  | `dec78e49bfee`  |
| 2147   | No file  | `dec78e49bfee`  |
| 2142   | No file  | `dec78e49bfee`  |
| 2138   | No file  | `dec78e49bfee`  |
| 2134   | No file  | `dec78e49bfee`  |
| 2130   | No file  | `dec78e49bfee`  |
| 2122   | No file  | `dec78e49bfee`  |
| 2107   | No file  | `dec78e49bfee`  |
| 2098   | No file  | `dec78e49bfee`  |
| 2089   | No file  | `dec78e49bfee`  |
| 2081   | No file  | `dec78e49bfee`  |
| 2073   | No file  | `dec78e49bfee`  |
| 2067   | No file  | `dec78e49bfee`  |
| 2063   | No file  | `dec78e49bfee`  |
| 2059   | No file  | `dec78e49bfee`  |
| 2052   | No file  | `dec78e49bfee`  |
| 2044   | No file  | `dec78e49bfee`  |
| 2039   | No file  | `dec78e49bfee`  |
| 2032   | No file  | `dec78e49bfee`  |
| 2025   | No file  | `dec78e49bfee`  |
| 2011   | No file  | `dec78e49bfee`  |
| 2005   | No file  | `dec78e49bfee`  |
| 2000   | No file  | `dec78e49bfee`  |
| 1996   | No file  | `dec78e49bfee`  |
| 1991   | No file  | `dec78e49bfee`  |
| 1985   | No file  | `dec78e49bfee`  |
| 1980   | No file  | `dec78e49bfee`  |
| 1969   | No file  | `dec78e49bfee`  |
| 1964   | No file  | `dec78e49bfee`  |
| 1958   | No file  | `dec78e49bfee`  |
| 1950   | No file  | `dec78e49bfee`  |
| 1945   | No file  | `dec78e49bfee`  |
| 1937   | No file  | `dec78e49bfee`  |
| 1933   | No file  | `dec78e49bfee`  |
| 1927   | No file  | `dec78e49bfee`  |
| 1921   | No file  | `dec78e49bfee`  |
| 1914   | No file  | `dec78e49bfee`  |
| 1908   | No file  | `dec78e49bfee`  |
| 1897   | No file  | `dec78e49bfee`  |
| 1892   | No file  | `dec78e49bfee`  |
| 1886   | No file  | `dec78e49bfee`  |
| 1881   | No file  | `dec78e49bfee`  |
| 1871   | No file  | `dec78e49bfee`  |
| 1866   | No file  | `dec78e49bfee`  |
| 1862   | No file  | `dec78e49bfee`  |
| 1854   | No file  | `dec78e49bfee`  |
| 1846   | No file  | `dec78e49bfee`  |
| 1838   | No file  | `dec78e49bfee`  |
| 1832   | No file  | `dec78e49bfee`  |
| 1826   | No file  | `dec78e49bfee`  |
| 1822   | No file  | `dec78e49bfee`  |
| 1818   | No file  | `dec78e49bfee`  |
| 1804   | No file  | `dec78e49bfee`  |
| 1794   | No file  | `dec78e49bfee`  |
| 1790   | No file  | `dec78e49bfee`  |
| 1784   | No file  | `dec78e49bfee`  |
| 1774   | No file  | `dec78e49bfee`  |
| 1771   | No file  | `dec78e49bfee`  |
| 1762   | No file  | `dec78e49bfee`  |
| 1759   | No file  | `dec78e49bfee`  |
| 1754   | No file  | `dec78e49bfee`  |
| 1749   | No file  | `dec78e49bfee`  |
| 1743   | No file  | `dec78e49bfee`  |
| 1737   | No file  | `dec78e49bfee`  |
| 1731   | No file  | `dec78e49bfee`  |
| 1725   | No file  | `dec78e49bfee`  |
| 1717   | No file  | `dec78e49bfee`  |
| 1710   | No file  | `dec78e49bfee`  |
| 1704   | No file  | `dec78e49bfee`  |
| 1698   | No file  | `dec78e49bfee`  |
| 1690   | No file  | `dec78e49bfee`  |
| 1685   | No file  | `dec78e49bfee`  |
| 1680   | No file  | `dec78e49bfee`  |
| 1674   | No file  | `dec78e49bfee`  |
| 1668   | No file  | `dec78e49bfee`  |
| 1659   | No file  | `dec78e49bfee`  |
| 1649   | No file  | `dec78e49bfee`  |
| 1642   | No file  | `dec78e49bfee`  |
| 1636   | No file  | `dec78e49bfee`  |
| 1628   | No file  | `dec78e49bfee`  |
| 1622   | No file  | `dec78e49bfee`  |
| 1614   | No file  | `dec78e49bfee`  |
| 1608   | No file  | `dec78e49bfee`  |
| 1602   | No file  | `dec78e49bfee`  |
| 1598   | No file  | `dec78e49bfee`  |
| 1594   | No file  | `dec78e49bfee`  |
| 1590   | No file  | `dec78e49bfee`  |
| 1587   | No file  | `dec78e49bfee`  |
| 1584   | No file  | `dec78e49bfee`  |
| 1579   | No file  | `dec78e49bfee`  |
| 1572   | No file  | `dec78e49bfee`  |
| 1565   | No file  | `dec78e49bfee`  |
| 1559   | No file  | `dec78e49bfee`  |
| 1554   | No file  | `dec78e49bfee`  |
| 1547   | No file  | `dec78e49bfee`  |
| 1537   | No file  | `dec78e49bfee`  |
| 1529   | No file  | `dec78e49bfee`  |
| 1524   | No file  | `dec78e49bfee`  |
| 1519   | No file  | `dec78e49bfee`  |
| 1509   | No file  | `dec78e49bfee`  |
| 1506   | No file  | `dec78e49bfee`  |
| 1504   | No file  | `dec78e49bfee`  |
| 1500   | No file  | `dec78e49bfee`  |
| 1493   | No file  | `dec78e49bfee`  |
| 1489   | No file  | `dec78e49bfee`  |
| 1485   | No file  | `dec78e49bfee`  |
| 1481   | No file  | `dec78e49bfee`  |
| 1474   | No file  | `dec78e49bfee`  |
| 1466   | No file  | `dec78e49bfee`  |
| 1462   | No file  | `dec78e49bfee`  |
| 1459   | No file  | `dec78e49bfee`  |
| 1453   | No file  | `dec78e49bfee`  |
| 1450   | No file  | `dec78e49bfee`  |
| 1445   | No file  | `dec78e49bfee`  |
| 1439   | No file  | `dec78e49bfee`  |
| 1433   | No file  | `dec78e49bfee`  |
| 1430   | No file  | `dec78e49bfee`  |
| 1426   | No file  | `dec78e49bfee`  |
| 1421   | No file  | `dec78e49bfee`  |
| 1417   | No file  | `dec78e49bfee`  |
| 1416   | No file  | `dec78e49bfee`  |
| 1409   | No file  | `dec78e49bfee`  |
| 1405   | No file  | `dec78e49bfee`  |
| 1401   | No file  | `dec78e49bfee`  |
| 1396   | No file  | `dec78e49bfee`  |
| 1391   | No file  | `dec78e49bfee`  |
| 1390   | No file  | `dec78e49bfee`  |
| 1386   | No file  | `dec78e49bfee`  |
| 1381   | No file  | `dec78e49bfee`  |
| 1379   | No file  | `dec78e49bfee`  |
| 1372   | No file  | `dec78e49bfee`  |
| 1366   | No file  | `dec78e49bfee`  |
| 1364   | No file  | `dec78e49bfee`  |
| 1363   | No file  | `dec78e49bfee`  |
| 1360   | No file  | `dec78e49bfee`  |
| 1358   | No file  | `dec78e49bfee`  |
| 1355   | No file  | `dec78e49bfee`  |
| 1351   | No file  | `dec78e49bfee`  |
| 1348   | No file  | `dec78e49bfee`  |
| 1346   | No file  | `dec78e49bfee`  |
| 1341   | No file  | `dec78e49bfee`  |
| 1340   | No file  | `dec78e49bfee`  |
| 1338   | No file  | `dec78e49bfee`  |
| 1335   | No file  | `dec78e49bfee`  |
| 1333   | No file  | `dec78e49bfee`  |
| 1329   | No file  | `dec78e49bfee`  |
| 1327   | No file  | `dec78e49bfee`  |
| 1324   | No file  | `dec78e49bfee`  |
| 1321   | No file  | `dec78e49bfee`  |
| 1319   | No file  | `dec78e49bfee`  |
| 1318   | No file  | `dec78e49bfee`  |
| 1316   | No file  | `dec78e49bfee`  |
| 1313   | No file  | `dec78e49bfee`  |
| 1311   | No file  | `dec78e49bfee`  |
| 1309   | No file  | `dec78e49bfee`  |
| 1304   | No file  | `dec78e49bfee`  |
| 1292   | No file  | `dec78e49bfee`  |
| 1286   | No file  | `dec78e49bfee`  |
| 1280   | No file  | `dec78e49bfee`  |
| 1276   | No file  | `dec78e49bfee`  |
| 1267   | No file  | `dec78e49bfee`  |
| 1261   | No file  | `dec78e49bfee`  |
| 1256   | No file  | `dec78e49bfee`  |
| 1250   | No file  | `dec78e49bfee`  |
| 1246   | No file  | `dec78e49bfee`  |
| 1239   | No file  | `dec78e49bfee`  |
| 1230   | No file  | `dec78e49bfee`  |
| 1226   | No file  | `dec78e49bfee`  |
| 1220   | No file  | `dec78e49bfee`  |
| 1217   | No file  | `dec78e49bfee`  |
| 1211   | No file  | `dec78e49bfee`  |
| 1210   | No file  | `dec78e49bfee`  |
| 1208   | No file  | `dec78e49bfee`  |
| 1203   | No file  | `dec78e49bfee`  |
| 1197   | No file  | `dec78e49bfee`  |
| 1194   | No file  | `dec78e49bfee`  |
| 1192   | No file  | `dec78e49bfee`  |
| 1187   | No file  | `dec78e49bfee`  |
| 1183   | No file  | `dec78e49bfee`  |
| 1177   | No file  | `dec78e49bfee`  |
| 1173   | No file  | `dec78e49bfee`  |
| 1167   | No file  | `dec78e49bfee`  |
| 1164   | No file  | `dec78e49bfee`  |
| 1156   | No file  | `dec78e49bfee`  |
| 1149   | No file  | `dec78e49bfee`  |
| 1144   | No file  | `dec78e49bfee`  |
| 1137   | No file  | `dec78e49bfee`  |
| 1132   | No file  | `dec78e49bfee`  |
| 1127   | No file  | `dec78e49bfee`  |
| 1122   | No file  | `dec78e49bfee`  |
| 1118   | No file  | `dec78e49bfee`  |
| 1114   | No file  | `dec78e49bfee`  |
| 1109   | No file  | `dec78e49bfee`  |
| 1102   | No file  | `dec78e49bfee`  |
| 1096   | No file  | `dec78e49bfee`  |
| 1088   | No file  | `dec78e49bfee`  |
| 1081   | No file  | `dec78e49bfee`  |
| 1076   | No file  | `dec78e49bfee`  |
| 1069   | No file  | `dec78e49bfee`  |
| 1064   | No file  | `dec78e49bfee`  |
| 1058   | No file  | `dec78e49bfee`  |
| 1051   | No file  | `dec78e49bfee`  |
| 1044   | No file  | `dec78e49bfee`  |
| 1036   | No file  | `dec78e49bfee`  |
| 1026   | No file  | `dec78e49bfee`  |
| 1016   | No file  | `dec78e49bfee`  |
| 1009   | No file  | `dec78e49bfee`  |
| 1005   | No file  | `dec78e49bfee`  |
| 1000   | No file  | `dec78e49bfee`  |
| 998    | No file  | `dec78e49bfee`  |
| 990    | No file  | `dec78e49bfee`  |
| 979    | No file  | `dec78e49bfee`  |
| 972    | No file  | `dec78e49bfee`  |
| 963    | No file  | `dec78e49bfee`  |
| 955    | No file  | `dec78e49bfee`  |
| 946    | No file  | `dec78e49bfee`  |
| 938    | No file  | `dec78e49bfee`  |
| 927    | No file  | `dec78e49bfee`  |
| 911    | No file  | `dec78e49bfee`  |
| 904    | No file  | `dec78e49bfee`  |
| 899    | No file  | `dec78e49bfee`  |
| 894    | No file  | `dec78e49bfee`  |
| 885    | No file  | `dec78e49bfee`  |
| 879    | No file  | `dec78e49bfee`  |
| 872    | No file  | `dec78e49bfee`  |
| 864    | No file  | `dec78e49bfee`  |
| 855    | No file  | `dec78e49bfee`  |
| 853    | No file  | `dec78e49bfee`  |
| 845    | No file  | `dec78e49bfee`  |
| 837    | No file  | `dec78e49bfee`  |
| 829    | No file  | `dec78e49bfee`  |
| 822    | No file  | `dec78e49bfee`  |
| 814    | No file  | `dec78e49bfee`  |
| 805    | No file  | `dec78e49bfee`  |
| 794    | No file  | `dec78e49bfee`  |
| 787    | No file  | `dec78e49bfee`  |
| 780    | No file  | `dec78e49bfee`  |
| 771    | No file  | `dec78e49bfee`  |
| 760    | No file  | `dec78e49bfee`  |
| 748    | No file  | `dec78e49bfee`  |
| 741    | No file  | `dec78e49bfee`  |
| 736    | No file  | `dec78e49bfee`  |
| 731    | No file  | `dec78e49bfee`  |
| 723    | No file  | `dec78e49bfee`  |
| 711    | No file  | `dec78e49bfee`  |
| 707    | No file  | `dec78e49bfee`  |
| 697    | No file  | `dec78e49bfee`  |
| 689    | No file  | `dec78e49bfee`  |
| 683    | No file  | `dec78e49bfee`  |
| 678    | No file  | `dec78e49bfee`  |
| 670    | No file  | `dec78e49bfee`  |
| 661    | No file  | `dec78e49bfee`  |
| 656    | No file  | `dec78e49bfee`  |
| 652    | No file  | `dec78e49bfee`  |
| 643    | No file  | `dec78e49bfee`  |
| 637    | No file  | `dec78e49bfee`  |
| 630    | No file  | `dec78e49bfee`  |
| 627    | No file  | `dec78e49bfee`  |
| 621    | No file  | `dec78e49bfee`  |
| 617    | No file  | `dec78e49bfee`  |
| 615    | No file  | `dec78e49bfee`  |
| 606    | No file  | `dec78e49bfee`  |
| 599    | No file  | `dec78e49bfee`  |
| 592    | No file  | `dec78e49bfee`  |
| 586    | No file  | `dec78e49bfee`  |
| 577    | No file  | `dec78e49bfee`  |
| 569    | No file  | `dec78e49bfee`  |
| 561    | No file  | `dec78e49bfee`  |
| 554    | No file  | `dec78e49bfee`  |
| 542    | No file  | `dec78e49bfee`  |
| 532    | No file  | `dec78e49bfee`  |
| 531    | No file  | `dec78e49bfee`  |
| 526    | No file  | `dec78e49bfee`  |
| 521    | No file  | `dec78e49bfee`  |
| 517    | No file  | `dec78e49bfee`  |
| 510    | No file  | `dec78e49bfee`  |
| 508    | No file  | `dec78e49bfee`  |
| 504    | No file  | `dec78e49bfee`  |
| 497    | No file  | `dec78e49bfee`  |
| 491    | No file  | `dec78e49bfee`  |
| 485    | No file  | `dec78e49bfee`  |
| 478    | No file  | `dec78e49bfee`  |
| 472    | No file  | `dec78e49bfee`  |
| 466    | No file  | `dec78e49bfee`  |
| 457    | No file  | `dec78e49bfee`  |
| 452    | No file  | `dec78e49bfee`  |
| 449    | No file  | `dec78e49bfee`  |
| 435    | No file  | `dec78e49bfee`  |

<!-- versions:end -->

## Companion Files

None. The textures the materials name are separate `.dds` files the Model tab loads; a sector LOD mesh names a texture the client does not ship (`52_0_10_LOD.dds` in `52_10_0_lod.pam`) and has a `.dds` of its own name next to it (`52_10_0_lod.dds`).

## Layout 1

### File Layout

Materials come first, then the vertices of every material, then the indices of every material. A material's indices count from its own first vertex (`base_vertex`).

| Offset              | Type                                              | Field           | Notes |
| ------------------- | ------------------------------------------------- | --------------- | ----- |
| `+0x00`             | char[4]                                           | magic           | ASCII `PAR ` |
| `+0x04`             | u8                                                | kind            | `0x06` on every `.pam` |
| `+0x05`             | u8                                                | version         | `4`, `5` or `6`; picks the material and vertex records |
| `+0x06`             | bytes[10]                                         | unknown_06      | `00 01 02 03 04 05 06 07 08 09` on 2,457 of 2,500 sampled files (client 3483); `00 01 02 03 04 05 06 07 08 FF` on 40, `00 00 01 02 03 04 05 06 07 08` on 3 |
| `+0x10`             | u32                                               | material_count  | `0` on 1 file (`ori_obj_bamboo_basket_01.pam`) |
| `+0x14`             | f32[3]                                            | bounds_min      | Equals the smallest vertex x, y, z on 2,497 of 2,500 sampled files |
| `+0x20`             | f32[3]                                            | bounds_max      | Equals the largest vertex x, y, z on the same files |
| `+0x2C`             | u32                                               | unknown_2c      | `0` on 1,966 of 2,500 sampled files, `1` on 517, up to `6` |
| `+0x30`             | f32                                               | unknown_30      | `0.0` on 2,449 of 2,500 sampled files, else `1.0` or `1.5` |
| `+0x34`             | u8                                                | unknown_34      | `0` or `1` |
| `+0x35`             | u8                                                | unknown_35      | `1` on every sampled file |
| `+0x36`             | u8                                                | has_u32_indices | `1` on 5 of 61,175 files (client 3483), each with a material of more than 65,535 vertices; `0` on the rest |
| `+0x37`             | bytes[985]                                        | unknown_37      | All `0` on every sampled file |
| `+0x410`            | Material[material_count] if version != 5          | materials       |  |
| `materials+0x00`    | Material V5[material_count] if version = 5        | materials_v5    |  |
| `materials_v5+0x00` | Vertex[sum vertex_count] if version != 6          | vertices        |  |
| `vertices+0x00`     | Vertex V6[sum vertex_count] if version = 6        | vertices_v6     |  |
| `vertices_v6+0x00`  | u16[sum index_count] if has_u32_indices = 0       | indices         | Three per triangle |
| `indices+0x00`      | u32[sum index_count] if has_u32_indices = 1       | indices_u32     | Three per triangle |

### Material (272 bytes)

Versions 4 and 6.

| Offset  | Type      | Field        | Notes |
| ------- | --------- | ------------ | ----- |
| `+0x00` | u32       | vertex_count | Vertices of this material |
| `+0x04` | u32       | index_count  | Indices of this material, a multiple of 3 |
| `+0x08` | u32       | base_vertex  | The `vertex_count` of the materials before it, added up, on all 2,500 sampled files |
| `+0x0C` | u32       | base_index   | The `index_count` of the materials before it, added up, on the same files |
| `+0x10` | char[256] | texture_name | File name of the texture, `0`-padded (`Wood_66.dds`) |

### Material V5 (276 bytes)

Version 5: a u32 before the texture name.

| Offset  | Type      | Field        | Notes |
| ------- | --------- | ------------ | ----- |
| `+0x00` | u32       | vertex_count | As in Material |
| `+0x04` | u32       | index_count  | As in Material |
| `+0x08` | u32       | base_vertex  | As in Material |
| `+0x0C` | u32       | base_index   | As in Material |
| `+0x10` | u32       | unknown_10   | `0` on 6,100 sampled materials; `00 46 78 00` on 34, `00 50 82 00` on 30, `FF 00 00 00` on 28 |
| `+0x14` | char[256] | texture_name | As in Material |

### Vertex (28 bytes)

Versions 4 and 5.

| Offset  | Type      | Field      | Notes |
| ------- | --------- | ---------- | ----- |
| `+0x00` | f32[3]    | position   | x, y, z in centimetres, y up |
| `+0x0C` | f32       | unknown_0c | `1.0` on the first vertex of 2,125 of 2,147 sampled version 4 and 5 files |
| `+0x10` | f16[2]    | uv         | Texture u, v; the Model tab maps the texture with them |
| `+0x14` | bytes[4]  | unknown_14 | Not a normal as four u8 scaled to -1 to 1: no byte order matches the face normals |
| `+0x18` | bytes[4]  | unknown_18 | `FF FF FF FF` on every vertex of 1,991 of 2,500 sampled files |

### Vertex V6 (32 bytes)

Version 6: four more bytes.

| Offset  | Type      | Field      | Notes |
| ------- | --------- | ---------- | ----- |
| `+0x00` | f32[3]    | position   | As in Vertex |
| `+0x0C` | f32       | unknown_0c | `1.0` on the first vertex of 350 of 353 sampled version 6 files |
| `+0x10` | f16[2]    | uv         | As in Vertex |
| `+0x14` | bytes[4]  | unknown_14 | As in Vertex |
| `+0x18` | bytes[4]  | unknown_18 | As in Vertex |
| `+0x1C` | bytes[4]  | unknown_1c | All `0` on every vertex of 283 of 353 sampled version 6 files |

## Notes

- Every `.pam` on client 3483 walks to its last byte by this layout (61,175 files, checked with `par_mesh.py`). The sampled counts in the tables come from 2,500 random files of the same client.
- sibercat/PAZ-Unpacker (MIT) gave the first reading of the header, the material records and the vertex position and UV. It reads `unknown_14` as a packed normal and tangent and `unknown_18` as a vertex colour; neither is confirmed here.
- `has_u32_indices` is the only header byte that differs between the files with u32 and u16 indices. 255 files hold more than 65,535 vertices in all and still use u16 indices, because each of their materials stays under 65,536.
- The texture of a material is found by its file name: in the mesh's folder (the `mapdata_real/hloddata/` and `sectormapinfo_combine/` LOD meshes), then `object/texture/`, then `character/texture/`. `object/texture_thumbnail/` holds smaller copies of the same names.

## Open Questions

### Header Bytes `0x2C` to `0x35`

`unknown_2c` counts something from 0 to 6, `unknown_30` is a float of `0.0`, `1.0` or `1.5`, and `unknown_34` and `unknown_35` are `0` or `1`. None of them changes the layout. Comparing them against the folders the meshes come from (houses, decals, LOD meshes) is the next step.

### Vertex Bytes `0x0C`, `0x14` and `0x18`

`unknown_0c` is `1.0` on nearly every vertex, `unknown_14` holds four bytes that change per vertex but do not decode as a plain normal, and `unknown_18` is `FF FF FF FF` on most files. A decode of `unknown_14` that matches the face normals (another scale, octahedral, or a tangent frame) would settle it.

### `unknown_06`

Three byte patterns at `0x06` (`00 .. 09`, `00 .. 08 FF`, `00 00 01 .. 08`). The same bytes sit at `0x06` in [`*.pcm`](mesh_pcm.md) and [`*.pac`](mesh_pac.md).
