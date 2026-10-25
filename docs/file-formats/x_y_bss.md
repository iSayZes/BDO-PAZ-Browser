# `x_y.bss` Format

## Purpose

The spawn grid cells: the client copy of the NPC and monster spawn
placements of one field, cut into files by grid square. Each file sits at
`mapdata_<resource>/spawnplacementfieldgrid/<field_no>/7/<x>_<z>.bss` and is
named after its first grid square; the browser lists the family as
`x_y.bss`. `<field_no>` is the [fieldinfo.bss](fieldinfo_bss.md) field
number (its `resource_name` `_real` or `_instancedungeon/4001` gives the
`mapdata_` folder). A spawn holds its placement key, a world position and
direction, the character key, the spawn delays, the NPC's action and dialog
index, waypoint keys, a home position and optional spawn hours.

On client 3482 field `1` (the open world) has 1,430 cell files with 95,787
spawns, field `700` (`칼페온 크자카 인던`, the Calpheon Kzarka instance) one
file with 20 and field `701` (`아쳐 튜토리얼 인던`) two files with 16. The 66
`A1_` fields `4001` to `4066` have the folder with its two list files and
no cells.

The two list files of each folder have their own docs:
[fieldgridinfo.bss](fieldgridinfo_bss.md) lists the grid squares that hold
spawns, [fileinfo.bss](fileinfo_bss.md) the cell files.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                                                   | Bytes  | Records                                               | Row bytes |
| ------ | ------------- | ------------------------------------------------------ | ------ | ----------------------------------------------------- | --------- |
| 1      | 805 and later | `mapdata_real/spawnplacementfieldgrid/1/7/651_259.bss` | 28,752 | 780 Waypoint, 176 Spawn, 14 Square, 34 Index Position | 5         |

| Layout | File                                                   | Known            | Unknown         |
| ------ | ------------------------------------------------------ | ---------------- | --------------- |
| 1      | `mapdata_real/spawnplacementfieldgrid/1/7/651_259.bss` | 22,700 B (79.0%) | 6,052 B (21.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `67a309ba69c4`  |
| 3482   | No file              | `67a309ba69c4`  |
| 3474   | Layout 1             | `67a309ba69c4`  |
| 3473   | Layout 1             | `67a309ba69c4`  |
| 3464   | Layout 1             | `67a309ba69c4`  |
| 3458   | Layout 1             | `67a309ba69c4`  |
| 3454   | Layout 1             | `67a309ba69c4`  |
| 3444   | Layout 1             | `67a309ba69c4`  |
| 3435   | Layout 1             | `67a309ba69c4`  |
| 3426   | Layout 1             | `67a309ba69c4`  |
| 3418   | Layout 1             | `67a309ba69c4`  |
| 3412   | Layout 1             | `67a309ba69c4`  |
| 3402   | Layout 1             | `67a309ba69c4`  |
| 3396   | Layout 1             | `67a309ba69c4`  |
| 3387   | Layout 1             | `67a309ba69c4`  |
| 3381   | Layout 1             | `67a309ba69c4`  |
| 3373   | Layout 1             | `67a309ba69c4`  |
| 3364   | Layout 1             | `67a309ba69c4`  |
| 3356   | Layout 1             | `67a309ba69c4`  |
| 3349   | Layout 1             | `67a309ba69c4`  |
| 3342   | Layout 1             | `67a309ba69c4`  |
| 3335   | Layout 1             | `67a309ba69c4`  |
| 3326   | Layout 1             | `67a309ba69c4`  |
| 3321   | Layout 1             | `67a309ba69c4`  |
| 3314   | Layout 1             | `67a309ba69c4`  |
| 3303   | Layout 1             | `67a309ba69c4`  |
| 3302   | Layout 1             | `67a309ba69c4`  |
| 3293   | Layout 1             | `67a309ba69c4`  |
| 3283   | Layout 1             | `67a309ba69c4`  |
| 3275   | Layout 1             | `67a309ba69c4`  |
| 3267   | Layout 1             | `67a309ba69c4`  |
| 3258   | Layout 1             | `67a309ba69c4`  |
| 3251   | Layout 1             | `67a309ba69c4`  |
| 3242   | Layout 1             | `67a309ba69c4`  |
| 3235   | Layout 1             | `67a309ba69c4`  |
| 3229   | Layout 1             | `67a309ba69c4`  |
| 3212   | Layout 1             | `67a309ba69c4`  |
| 3203   | Layout 1             | `67a309ba69c4`  |
| 3193   | Layout 1             | `67a309ba69c4`  |
| 3186   | Layout 1             | `67a309ba69c4`  |
| 3177   | Layout 1             | `67a309ba69c4`  |
| 3169   | Layout 1             | `67a309ba69c4`  |
| 3158   | Layout 1             | `67a309ba69c4`  |
| 3151   | Layout 1             | `67a309ba69c4`  |
| 3144   | Layout 1             | `67a309ba69c4`  |
| 3133   | Layout 1             | `67a309ba69c4`  |
| 3125   | Layout 1             | `67a309ba69c4`  |
| 3118   | Layout 1             | `67a309ba69c4`  |
| 3111   | Layout 1             | `67a309ba69c4`  |
| 3103   | Layout 1             | `67a309ba69c4`  |
| 3095   | Layout 1             | `67a309ba69c4`  |
| 3086   | Layout 1             | `67a309ba69c4`  |
| 3072   | Layout 1             | `67a309ba69c4`  |
| 3062   | Layout 1             | `67a309ba69c4`  |
| 3052   | Layout 1             | `67a309ba69c4`  |
| 3045   | Layout 1             | `67a309ba69c4`  |
| 3037   | Layout 1             | `67a309ba69c4`  |
| 3030   | Layout 1             | `67a309ba69c4`  |
| 3021   | Layout 1             | `67a309ba69c4`  |
| 3012   | Layout 1             | `67a309ba69c4`  |
| 3002   | Layout 1             | `67a309ba69c4`  |
| 2995   | Layout 1             | `67a309ba69c4`  |
| 2987   | Layout 1             | `67a309ba69c4`  |
| 2978   | Layout 1             | `67a309ba69c4`  |
| 2970   | Layout 1             | `67a309ba69c4`  |
| 2959   | Layout 1             | `67a309ba69c4`  |
| 2951   | Layout 1             | `67a309ba69c4`  |
| 2942   | Layout 1             | `67a309ba69c4`  |
| 2935   | Layout 1             | `67a309ba69c4`  |
| 2932   | Layout 1             | `67a309ba69c4`  |
| 2923   | Layout 1             | `67a309ba69c4`  |
| 2919   | Layout 1             | `67a309ba69c4`  |
| 2907   | Layout 1             | `67a309ba69c4`  |
| 2900   | Layout 1             | `67a309ba69c4`  |
| 2891   | Layout 1             | `67a309ba69c4`  |
| 2882   | Layout 1             | `67a309ba69c4`  |
| 2872   | Layout 1             | `67a309ba69c4`  |
| 2863   | Layout 1             | `67a309ba69c4`  |
| 2855   | Layout 1             | `67a309ba69c4`  |
| 2849   | Layout 1             | `67a309ba69c4`  |
| 2844   | Layout 1             | `67a309ba69c4`  |
| 2834   | Layout 1             | `67a309ba69c4`  |
| 2825   | Layout 1             | `67a309ba69c4`  |
| 2819   | Layout 1             | `67a309ba69c4`  |
| 2811   | Layout 1             | `67a309ba69c4`  |
| 2803   | Layout 1             | `67a309ba69c4`  |
| 2794   | Layout 1             | `67a309ba69c4`  |
| 2783   | Layout 1             | `67a309ba69c4`  |
| 2774   | Layout 1             | `67a309ba69c4`  |
| 2765   | Layout 1             | `67a309ba69c4`  |
| 2756   | Layout 1             | `67a309ba69c4`  |
| 2750   | Layout 1             | `67a309ba69c4`  |
| 2743   | Layout 1             | `67a309ba69c4`  |
| 2736   | Layout 1             | `67a309ba69c4`  |
| 2726   | Layout 1             | `67a309ba69c4`  |
| 2717   | Layout 1             | `67a309ba69c4`  |
| 2709   | Layout 1             | `67a309ba69c4`  |
| 2703   | Layout 1             | `67a309ba69c4`  |
| 2695   | Layout 1             | `67a309ba69c4`  |
| 2684   | Layout 1             | `67a309ba69c4`  |
| 2672   | Layout 1             | `67a309ba69c4`  |
| 2665   | Layout 1             | `67a309ba69c4`  |
| 2657   | Layout 1             | `67a309ba69c4`  |
| 2649   | Layout 1             | `67a309ba69c4`  |
| 2644   | Layout 1             | `67a309ba69c4`  |
| 2637   | Layout 1             | `67a309ba69c4`  |
| 2629   | Layout 1             | `67a309ba69c4`  |
| 2619   | Layout 1             | `67a309ba69c4`  |
| 2612   | Layout 1             | `67a309ba69c4`  |
| 2606   | Layout 1             | `67a309ba69c4`  |
| 2602   | Layout 1             | `67a309ba69c4`  |
| 2601   | Layout 1             | `67a309ba69c4`  |
| 2592   | Layout 1             | `67a309ba69c4`  |
| 2583   | Layout 1             | `67a309ba69c4`  |
| 2575   | Layout 1             | `67a309ba69c4`  |
| 2567   | Layout 1             | `67a309ba69c4`  |
| 2560   | Layout 1             | `67a309ba69c4`  |
| 2553   | Layout 1             | `67a309ba69c4`  |
| 2545   | Layout 1             | `67a309ba69c4`  |
| 2538   | Layout 1             | `67a309ba69c4`  |
| 2529   | Layout 1             | `67a309ba69c4`  |
| 2519   | Layout 1             | `67a309ba69c4`  |
| 2513   | Layout 1             | `67a309ba69c4`  |
| 2510   | Layout 1             | `67a309ba69c4`  |
| 2507   | Layout 1             | `67a309ba69c4`  |
| 2503   | Layout 1             | `67a309ba69c4`  |
| 2498   | Layout 1             | `67a309ba69c4`  |
| 2492   | Layout 1             | `67a309ba69c4`  |
| 2487   | Layout 1             | `67a309ba69c4`  |
| 2480   | Layout 1             | `67a309ba69c4`  |
| 2474   | Layout 1             | `67a309ba69c4`  |
| 2468   | Layout 1             | `67a309ba69c4`  |
| 2460   | Layout 1             | `67a309ba69c4`  |
| 2453   | Layout 1             | `67a309ba69c4`  |
| 2444   | Layout 1             | `67a309ba69c4`  |
| 2438   | Layout 1             | `67a309ba69c4`  |
| 2434   | Layout 1             | `67a309ba69c4`  |
| 2429   | Layout 1             | `67a309ba69c4`  |
| 2421   | Layout 1             | `67a309ba69c4`  |
| 2414   | Layout 1             | `67a309ba69c4`  |
| 2407   | Layout 1             | `67a309ba69c4`  |
| 2401   | Layout 1             | `67a309ba69c4`  |
| 2397   | Layout 1             | `67a309ba69c4`  |
| 2393   | Layout 1             | `67a309ba69c4`  |
| 2384   | Layout 1             | `67a309ba69c4`  |
| 2378   | Layout 1             | `67a309ba69c4`  |
| 2372   | Layout 1             | `67a309ba69c4`  |
| 2358   | Layout 1             | `67a309ba69c4`  |
| 2352   | Layout 1             | `67a309ba69c4`  |
| 2347   | Layout 1             | `67a309ba69c4`  |
| 2343   | Layout 1             | `67a309ba69c4`  |
| 2335   | Layout 1             | `67a309ba69c4`  |
| 2327   | Layout 1             | `67a309ba69c4`  |
| 2324   | Layout 1             | `67a309ba69c4`  |
| 2319   | Layout 1             | `67a309ba69c4`  |
| 2313   | Layout 1             | `67a309ba69c4`  |
| 2308   | Layout 1             | `67a309ba69c4`  |
| 2302   | Layout 1             | `67a309ba69c4`  |
| 2295   | Layout 1             | `67a309ba69c4`  |
| 2290   | Layout 1             | `67a309ba69c4`  |
| 2284   | Layout 1             | `67a309ba69c4`  |
| 2276   | Layout 1             | `67a309ba69c4`  |
| 2269   | Layout 1             | `67a309ba69c4`  |
| 2259   | Layout 1             | `67a309ba69c4`  |
| 2250   | Layout 1             | `67a309ba69c4`  |
| 2243   | Layout 1             | `67a309ba69c4`  |
| 2235   | Layout 1             | `67a309ba69c4`  |
| 2229   | Layout 1             | `67a309ba69c4`  |
| 2224   | Layout 1             | `67a309ba69c4`  |
| 2218   | Layout 1             | `67a309ba69c4`  |
| 2215   | Layout 1             | `67a309ba69c4`  |
| 2207   | Layout 1             | `67a309ba69c4`  |
| 2203   | Layout 1             | `67a309ba69c4`  |
| 2196   | Layout 1             | `67a309ba69c4`  |
| 2192   | Layout 1             | `67a309ba69c4`  |
| 2189   | Layout 1             | `67a309ba69c4`  |
| 2183   | Layout 1             | `67a309ba69c4`  |
| 2179   | Layout 1             | `67a309ba69c4`  |
| 2171   | Layout 1             | `67a309ba69c4`  |
| 2163   | Layout 1             | `67a309ba69c4`  |
| 2156   | Layout 1             | `67a309ba69c4`  |
| 2151   | Layout 1             | `67a309ba69c4`  |
| 2147   | Layout 1             | `67a309ba69c4`  |
| 2142   | Layout 1             | `67a309ba69c4`  |
| 2138   | Layout 1             | `67a309ba69c4`  |
| 2134   | Layout 1             | `67a309ba69c4`  |
| 2130   | Layout 1             | `67a309ba69c4`  |
| 2122   | Layout 1             | `67a309ba69c4`  |
| 2107   | Layout 1             | `67a309ba69c4`  |
| 2098   | Layout 1             | `67a309ba69c4`  |
| 2089   | Layout 1             | `67a309ba69c4`  |
| 2081   | Layout 1             | `67a309ba69c4`  |
| 2073   | Layout 1             | `67a309ba69c4`  |
| 2067   | Layout 1             | `67a309ba69c4`  |
| 2063   | Layout 1             | `67a309ba69c4`  |
| 2059   | Layout 1             | `67a309ba69c4`  |
| 2052   | Layout 1             | `67a309ba69c4`  |
| 2044   | Layout 1             | `67a309ba69c4`  |
| 2039   | Layout 1             | `67a309ba69c4`  |
| 2032   | Layout 1             | `67a309ba69c4`  |
| 2025   | Layout 1             | `67a309ba69c4`  |
| 2011   | Layout 1             | `67a309ba69c4`  |
| 2005   | Layout 1             | `67a309ba69c4`  |
| 2000   | Layout 1             | `67a309ba69c4`  |
| 1996   | Layout 1             | `67a309ba69c4`  |
| 1991   | Layout 1             | `67a309ba69c4`  |
| 1985   | Layout 1             | `67a309ba69c4`  |
| 1980   | Layout 1             | `67a309ba69c4`  |
| 1969   | Layout 1             | `67a309ba69c4`  |
| 1964   | Layout 1             | `67a309ba69c4`  |
| 1958   | Layout 1             | `67a309ba69c4`  |
| 1950   | Layout 1             | `67a309ba69c4`  |
| 1945   | Layout 1             | `67a309ba69c4`  |
| 1937   | Layout 1             | `67a309ba69c4`  |
| 1933   | Layout 1             | `67a309ba69c4`  |
| 1927   | Layout 1             | `67a309ba69c4`  |
| 1921   | Layout 1             | `67a309ba69c4`  |
| 1914   | Layout 1             | `67a309ba69c4`  |
| 1908   | Layout 1             | `67a309ba69c4`  |
| 1897   | Layout 1             | `67a309ba69c4`  |
| 1892   | Layout 1             | `67a309ba69c4`  |
| 1886   | Layout 1             | `67a309ba69c4`  |
| 1881   | Layout 1             | `67a309ba69c4`  |
| 1871   | Layout 1             | `67a309ba69c4`  |
| 1866   | Layout 1             | `67a309ba69c4`  |
| 1862   | Layout 1             | `67a309ba69c4`  |
| 1854   | Layout 1             | `67a309ba69c4`  |
| 1846   | Layout 1             | `67a309ba69c4`  |
| 1838   | Layout 1             | `67a309ba69c4`  |
| 1832   | Layout 1             | `67a309ba69c4`  |
| 1826   | Layout 1             | `67a309ba69c4`  |
| 1822   | Layout 1             | `67a309ba69c4`  |
| 1818   | Layout 1             | `67a309ba69c4`  |
| 1804   | Layout 1             | `67a309ba69c4`  |
| 1794   | Layout 1             | `67a309ba69c4`  |
| 1790   | Layout 1             | `67a309ba69c4`  |
| 1784   | Layout 1             | `67a309ba69c4`  |
| 1774   | Layout 1             | `67a309ba69c4`  |
| 1771   | Layout 1             | `67a309ba69c4`  |
| 1762   | Layout 1             | `67a309ba69c4`  |
| 1759   | Layout 1             | `67a309ba69c4`  |
| 1754   | Layout 1             | `67a309ba69c4`  |
| 1749   | Layout 1             | `67a309ba69c4`  |
| 1743   | Layout 1             | `67a309ba69c4`  |
| 1737   | Layout 1             | `67a309ba69c4`  |
| 1731   | Layout 1             | `67a309ba69c4`  |
| 1725   | Layout 1             | `67a309ba69c4`  |
| 1717   | Layout 1             | `67a309ba69c4`  |
| 1710   | Layout 1             | `67a309ba69c4`  |
| 1704   | Layout 1             | `67a309ba69c4`  |
| 1698   | Layout 1             | `67a309ba69c4`  |
| 1690   | Layout 1             | `67a309ba69c4`  |
| 1685   | Layout 1             | `67a309ba69c4`  |
| 1680   | Layout 1             | `67a309ba69c4`  |
| 1674   | Layout 1             | `67a309ba69c4`  |
| 1668   | Layout 1             | `67a309ba69c4`  |
| 1659   | Layout 1             | `67a309ba69c4`  |
| 1649   | Layout 1             | `67a309ba69c4`  |
| 1642   | Layout 1             | `67a309ba69c4`  |
| 1636   | Layout 1             | `67a309ba69c4`  |
| 1628   | Layout 1             | `67a309ba69c4`  |
| 1622   | Layout 1             | `67a309ba69c4`  |
| 1614   | Layout 1             | `67a309ba69c4`  |
| 1608   | Layout 1             | `67a309ba69c4`  |
| 1602   | Layout 1             | `67a309ba69c4`  |
| 1598   | Layout 1             | `67a309ba69c4`  |
| 1594   | Layout 1             | `67a309ba69c4`  |
| 1590   | Layout 1             | `67a309ba69c4`  |
| 1587   | Layout 1             | `67a309ba69c4`  |
| 1584   | Layout 1             | `67a309ba69c4`  |
| 1579   | Layout 1             | `67a309ba69c4`  |
| 1572   | Layout 1             | `67a309ba69c4`  |
| 1565   | Layout 1             | `67a309ba69c4`  |
| 1559   | Layout 1             | `67a309ba69c4`  |
| 1554   | Layout 1             | `67a309ba69c4`  |
| 1547   | Layout 1             | `67a309ba69c4`  |
| 1537   | Layout 1             | `67a309ba69c4`  |
| 1529   | Layout 1             | `67a309ba69c4`  |
| 1524   | Layout 1             | `67a309ba69c4`  |
| 1519   | Layout 1             | `67a309ba69c4`  |
| 1509   | Layout 1             | `67a309ba69c4`  |
| 1506   | Layout 1             | `67a309ba69c4`  |
| 1504   | Layout 1             | `67a309ba69c4`  |
| 1500   | Layout 1             | `67a309ba69c4`  |
| 1493   | Layout 1             | `67a309ba69c4`  |
| 1489   | Layout 1             | `67a309ba69c4`  |
| 1485   | Layout 1             | `67a309ba69c4`  |
| 1481   | Layout 1             | `67a309ba69c4`  |
| 1474   | Layout 1             | `67a309ba69c4`  |
| 1466   | Layout 1             | `67a309ba69c4`  |
| 1462   | Layout 1             | `67a309ba69c4`  |
| 1459   | Layout 1             | `67a309ba69c4`  |
| 1453   | Layout 1             | `67a309ba69c4`  |
| 1450   | Layout 1             | `67a309ba69c4`  |
| 1445   | Layout 1             | `67a309ba69c4`  |
| 1439   | Layout 1             | `67a309ba69c4`  |
| 1433   | Layout 1             | `67a309ba69c4`  |
| 1430   | Layout 1             | `67a309ba69c4`  |
| 1426   | Layout 1             | `67a309ba69c4`  |
| 1421   | Layout 1             | `67a309ba69c4`  |
| 1417   | Layout 1             | `67a309ba69c4`  |
| 1416   | Layout 1             | `67a309ba69c4`  |
| 1409   | Layout 1             | `67a309ba69c4`  |
| 1405   | Layout 1             | `67a309ba69c4`  |
| 1401   | Layout 1             | `67a309ba69c4`  |
| 1396   | Layout 1             | `67a309ba69c4`  |
| 1391   | Layout 1             | `67a309ba69c4`  |
| 1390   | Layout 1             | `67a309ba69c4`  |
| 1386   | Layout 1             | `67a309ba69c4`  |
| 1381   | Layout 1             | `67a309ba69c4`  |
| 1379   | Layout 1             | `67a309ba69c4`  |
| 1372   | Layout 1             | `67a309ba69c4`  |
| 1366   | Layout 1             | `67a309ba69c4`  |
| 1364   | Layout 1             | `67a309ba69c4`  |
| 1363   | Layout 1             | `67a309ba69c4`  |
| 1360   | Layout 1             | `67a309ba69c4`  |
| 1358   | Layout 1             | `67a309ba69c4`  |
| 1355   | Layout 1             | `67a309ba69c4`  |
| 1351   | Layout 1             | `67a309ba69c4`  |
| 1348   | Layout 1             | `67a309ba69c4`  |
| 1346   | Layout 1             | `67a309ba69c4`  |
| 1341   | Layout 1             | `67a309ba69c4`  |
| 1340   | Layout 1             | `67a309ba69c4`  |
| 1338   | Layout 1             | `67a309ba69c4`  |
| 1335   | Layout 1             | `67a309ba69c4`  |
| 1333   | Layout 1             | `67a309ba69c4`  |
| 1329   | Layout 1             | `67a309ba69c4`  |
| 1327   | Layout 1             | `67a309ba69c4`  |
| 1324   | Layout 1             | `67a309ba69c4`  |
| 1321   | Layout 1             | `67a309ba69c4`  |
| 1319   | Layout 1             | `67a309ba69c4`  |
| 1318   | Layout 1             | `67a309ba69c4`  |
| 1316   | Layout 1             | `67a309ba69c4`  |
| 1313   | Layout 1             | `67a309ba69c4`  |
| 1311   | Layout 1             | `67a309ba69c4`  |
| 1309   | Layout 1             | `67a309ba69c4`  |
| 1304   | Layout 1             | `67a309ba69c4`  |
| 1292   | Layout 1             | `67a309ba69c4`  |
| 1286   | Layout 1             | `67a309ba69c4`  |
| 1280   | Layout 1             | `67a309ba69c4`  |
| 1276   | Layout 1             | `67a309ba69c4`  |
| 1267   | Layout 1             | `67a309ba69c4`  |
| 1261   | Layout 1             | `67a309ba69c4`  |
| 1256   | Layout 1             | `67a309ba69c4`  |
| 1250   | Layout 1             | `67a309ba69c4`  |
| 1246   | Layout 1             | `67a309ba69c4`  |
| 1239   | Layout 1             | `67a309ba69c4`  |
| 1230   | Layout 1             | `67a309ba69c4`  |
| 1226   | Layout 1             | `67a309ba69c4`  |
| 1220   | Layout 1             | `67a309ba69c4`  |
| 1217   | Layout 1             | `67a309ba69c4`  |
| 1211   | Layout 1             | `67a309ba69c4`  |
| 1210   | Layout 1             | `67a309ba69c4`  |
| 1208   | Layout 1             | `67a309ba69c4`  |
| 1203   | Layout 1             | `67a309ba69c4`  |
| 1197   | Layout 1             | `67a309ba69c4`  |
| 1194   | Layout 1             | `67a309ba69c4`  |
| 1192   | Layout 1             | `67a309ba69c4`  |
| 1187   | Layout 1             | `67a309ba69c4`  |
| 1183   | Layout 1             | `67a309ba69c4`  |
| 1177   | Layout 1             | `67a309ba69c4`  |
| 1173   | Layout 1             | `67a309ba69c4`  |
| 1167   | Layout 1             | `67a309ba69c4`  |
| 1164   | Layout 1             | `67a309ba69c4`  |
| 1156   | Layout 1             | `67a309ba69c4`  |
| 1149   | Layout 1             | `67a309ba69c4`  |
| 1144   | Layout 1             | `67a309ba69c4`  |
| 1137   | Layout 1             | `67a309ba69c4`  |
| 1132   | Layout 1             | `67a309ba69c4`  |
| 1127   | Layout 1             | `67a309ba69c4`  |
| 1122   | Layout 1             | `67a309ba69c4`  |
| 1118   | Layout 1             | `67a309ba69c4`  |
| 1114   | Layout 1             | `67a309ba69c4`  |
| 1109   | Layout 1             | `67a309ba69c4`  |
| 1102   | Layout 1             | `67a309ba69c4`  |
| 1096   | Layout 1             | `67a309ba69c4`  |
| 1088   | Layout 1             | `67a309ba69c4`  |
| 1081   | Layout 1             | `67a309ba69c4`  |
| 1076   | Layout 1             | `67a309ba69c4`  |
| 1069   | Layout 1             | `67a309ba69c4`  |
| 1064   | Layout 1             | `67a309ba69c4`  |
| 1058   | Layout 1             | `67a309ba69c4`  |
| 1051   | Layout 1             | `67a309ba69c4`  |
| 1044   | Layout 1             | `67a309ba69c4`  |
| 1036   | Layout 1             | `67a309ba69c4`  |
| 1026   | Layout 1             | `67a309ba69c4`  |
| 1016   | Layout 1             | `67a309ba69c4`  |
| 1009   | Layout 1             | `67a309ba69c4`  |
| 1005   | Layout 1             | `67a309ba69c4`  |
| 1000   | Layout 1             | `67a309ba69c4`  |
| 998    | Layout 1             | `67a309ba69c4`  |
| 990    | Layout 1             | `67a309ba69c4`  |
| 979    | Layout 1             | `67a309ba69c4`  |
| 972    | Layout 1             | `67a309ba69c4`  |
| 963    | Layout 1             | `67a309ba69c4`  |
| 955    | Layout 1             | `67a309ba69c4`  |
| 946    | Layout 1             | `67a309ba69c4`  |
| 938    | Layout 1             | `67a309ba69c4`  |
| 927    | Layout 1             | `67a309ba69c4`  |
| 911    | Layout 1             | `67a309ba69c4`  |
| 904    | Layout 1             | `67a309ba69c4`  |
| 899    | Layout 1             | `67a309ba69c4`  |
| 894    | Layout 1             | `67a309ba69c4`  |
| 885    | Layout 1             | `67a309ba69c4`  |
| 879    | Layout 1             | `67a309ba69c4`  |
| 872    | Layout 1             | `67a309ba69c4`  |
| 864    | Layout 1             | `67a309ba69c4`  |
| 855    | Layout 1             | `67a309ba69c4`  |
| 853    | Layout 1             | `67a309ba69c4`  |
| 845    | Layout 1             | `67a309ba69c4`  |
| 837    | Layout 1             | `67a309ba69c4`  |
| 829    | Layout 1             | `67a309ba69c4`  |
| 822    | Layout 1             | `67a309ba69c4`  |
| 814    | Layout 1             | `67a309ba69c4`  |
| 805    | Layout 1             | `67a309ba69c4`  |
| 794    | No documented layout | `67a309ba69c4`  |
| 787    | No documented layout | `67a309ba69c4`  |
| 780    | No documented layout | `67a309ba69c4`  |
| 771    | No documented layout | `67a309ba69c4`  |
| 760    | No file              | `67a309ba69c4`  |
| 748    | No file              | `67a309ba69c4`  |
| 741    | No file              | `67a309ba69c4`  |
| 736    | No file              | `67a309ba69c4`  |
| 731    | No file              | `67a309ba69c4`  |
| 723    | No file              | `67a309ba69c4`  |
| 711    | No file              | `67a309ba69c4`  |
| 707    | No file              | `67a309ba69c4`  |
| 697    | No file              | `67a309ba69c4`  |
| 689    | No file              | `67a309ba69c4`  |
| 683    | No file              | `67a309ba69c4`  |
| 678    | No file              | `67a309ba69c4`  |
| 670    | No file              | `67a309ba69c4`  |
| 661    | No file              | `67a309ba69c4`  |
| 656    | No file              | `67a309ba69c4`  |
| 652    | No file              | `67a309ba69c4`  |
| 643    | No file              | `67a309ba69c4`  |
| 637    | No file              | `67a309ba69c4`  |
| 630    | No file              | `67a309ba69c4`  |
| 627    | No file              | `67a309ba69c4`  |
| 621    | No file              | `67a309ba69c4`  |
| 617    | No file              | `67a309ba69c4`  |
| 615    | No file              | `67a309ba69c4`  |
| 606    | No file              | `67a309ba69c4`  |
| 599    | No file              | `67a309ba69c4`  |
| 592    | No file              | `67a309ba69c4`  |
| 586    | No file              | `67a309ba69c4`  |
| 577    | No file              | `67a309ba69c4`  |
| 569    | No file              | `67a309ba69c4`  |
| 561    | No file              | `67a309ba69c4`  |
| 554    | No file              | `67a309ba69c4`  |
| 542    | No file              | `67a309ba69c4`  |
| 532    | No file              | `67a309ba69c4`  |
| 531    | No file              | `67a309ba69c4`  |
| 526    | No file              | `67a309ba69c4`  |
| 521    | No file              | `67a309ba69c4`  |
| 517    | No file              | `67a309ba69c4`  |
| 510    | No file              | `67a309ba69c4`  |
| 508    | No file              | `67a309ba69c4`  |
| 504    | No file              | `67a309ba69c4`  |
| 497    | No file              | `67a309ba69c4`  |
| 491    | No file              | `67a309ba69c4`  |
| 485    | No file              | `67a309ba69c4`  |
| 478    | No file              | `67a309ba69c4`  |
| 472    | No file              | `67a309ba69c4`  |
| 466    | No file              | `67a309ba69c4`  |
| 457    | No file              | `67a309ba69c4`  |
| 452    | No file              | `67a309ba69c4`  |
| 449    | No file              | `67a309ba69c4`  |
| 435    | No file              | `67a309ba69c4`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                    |
| ---------------------------- | -------- | ----------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a character key without a row shows as plain text |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with no row count: the squares run up to the string table, whose
offset the trailer holds.

| Offset         | Type                  | Field        | Notes                                              |
| -------------- | --------------------- | ------------ | -------------------------------------------------- |
| `+0x00`        | char[4]               | magic        | ASCII `PABR`                                       |
| `+0x04`        | Square[..table_start] | squares      | Squares back to back until `table_start`; see Square |
| `squares+0x00` | String Table          | string_table | See String Table                                   |
| `EOF-0x08`     | u32                   | table_start  | Offset of the string table, where `squares` ends   |
| `EOF-0x04`     | u32                   | zero         | Always `0`                                         |

### Square (variable: 8 bytes + spawns)

| Offset  | Type               | Field       | Notes                                                                 |
| ------- | ------------------ | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16                | grid_x      | Field grid square column; see [Grid Squares](#grid-squares)           |
| `+0x02` | u16                | grid_z      | Field grid square row                                                 |
| `+0x04` | u32                | spawn_count | Number of `spawns`, at least `1`                                      |
| `+0x08` | Spawn[spawn_count] | spawns      | See Spawn                                                             |

### Spawn (variable: 135 bytes + character key and lists)

| Offset                  | Type                                        | Field                     | Notes                                                                                 |
| ----------------------- | ------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`                 | u8                                          | is_spawnable              | `1` or `0`                                                                            |
| `+0x01`                 | u16                                         | key_index                 | Spawn number within its sector and type; with the next four fields the XML `Key`      |
| `+0x03`                 | i16                                         | key_sector_z              | Sector (12,800 units) row of the spawn's source file                                  |
| `+0x05`                 | i16                                         | key_sector_x              | Sector column of the spawn's source file                                              |
| `+0x07`                 | u8                                          | key_type                  | Source file kind: `2` `_Monster.xml`, `3` `_Npc.xml`; `11` on 9 field 700 and 701 spawns |
| `+0x08`                 | u8                                          | unknown_08                | `0` on every spawn                                                                    |
| `+0x09`                 | f32                                         | position_x                | World position                                                                        |
| `+0x0D`                 | f32                                         | position_y                | Height                                                                                |
| `+0x11`                 | f32                                         | position_z                |                                                                                       |
| `+0x15`                 | u16                                         | spawn_range               | `0` on 95,587 spawns                                                                  |
| `+0x17`                 | f32                                         | direction                 | Facing in radians                                                                     |
| `+0x1B`                 | u16                                         | unknown_1b                | `0` on every spawn                                                                    |
| `+0x1D`                 | u8                                          | has_character             | `1` when `character_key` follows; see Notes                                           |
| `+0x1E`                 | u16 if has_character = 1                    | character_key             | `characterstatic.dbss` key                                                            |
| `character_key+0x00`    | i32                                         | scene_sector_x            | Sector of a linked scene object; `0` with `scene_type` `0`                            |
| `character_key+0x04`    | i32                                         | scene_sector_y            |                                                                                       |
| `character_key+0x08`    | i32                                         | scene_sector_z            |                                                                                       |
| `character_key+0x0C`    | u16                                         | scene_type                | `2` on 720 spawns, else `0`                                                           |
| `character_key+0x0E`    | u16                                         | scene_index               | Object number in that sector                                                          |
| `character_key+0x10`    | u32                                         | unknown_character_key_10  | `1` on every spawn; see Field Names                                                   |
| `character_key+0x14`    | u32                                         | unknown_character_key_14  | `0` on every spawn                                                                    |
| `character_key+0x18`    | u32                                         | unknown_character_key_18  | `0` on every spawn                                                                    |
| `character_key+0x1C`    | u8                                          | unknown_character_key_1c  | `0` on every spawn                                                                    |
| `character_key+0x1D`    | u32                                         | spawn_delay_time          | Milliseconds; `120000` or `60000`                                                     |
| `character_key+0x21`    | u32                                         | spawn_delay_variable_time | Milliseconds; a quarter of `spawn_delay_time` on every spawn                     |
| `character_key+0x25`    | u8                                          | unknown_character_key_25  | `1` on every spawn                                                                    |
| `character_key+0x26`    | bytes[3]                                    | unknown_character_key_26  | `0` on every spawn                                                                    |
| `character_key+0x29`    | u32                                         | respawn_number            | `0` on all but 4 spawns                                                               |
| `character_key+0x2D`    | u8                                          | unknown_character_key_2d  | `0` on every spawn                                                                    |
| `character_key+0x2E`    | u32                                         | event_object_key          | `157` on one spawn, else `0`                                                          |
| `character_key+0x32`    | u32                                         | unknown_character_key_32  | `0` on every spawn                                                                    |
| `character_key+0x36`    | u32                                         | live_world_event_key      | `4`, `7`, `98` and `207` on one spawn each, else `0`                                  |
| `character_key+0x3A`    | i16                                         | territory                 | `-1` for none; `0`, `1` or `2` on 758 spawns                                          |
| `character_key+0x3C`    | u32                                         | action_index              | NPC action                                                                            |
| `character_key+0x40`    | u16                                         | dialog_index              | NPC dialog                                                                            |
| `character_key+0x42`    | u32                                         | dialog_update_time        | Milliseconds; `0` on 94,727 spawns                                                    |
| `character_key+0x46`    | bytes[4]                                    | unknown_character_key_46  | `0` on every spawn                                                                    |
| `character_key+0x4A`    | i32                                         | team_no                   | `-1` on 3,135 spawns, `0` on most                                                     |
| `character_key+0x4E`    | i32                                         | unknown_character_key_4e  | `-1` where `team_no` is `-1` or `-660`, else `0`                                      |
| `character_key+0x52`    | f32                                         | house_x                   | NPC home position; `0, 0, 0` on all but 1,035 spawns                                                   |
| `character_key+0x56`    | f32                                         | house_y                   |                                                                                       |
| `character_key+0x5A`    | f32                                         | house_z                   |                                                                                       |
| `character_key+0x5E`    | u32                                         | waypoint_count            | Number of `waypoints`: `5` or `0`                                                     |
| `character_key+0x62`    | Waypoint[waypoint_count]                    | waypoints                 | See Waypoint                                                                          |
| `waypoints+0x00`        | u8                                          | go_home_type              | `0`, `1` or `2`                                                                       |
| `waypoints+0x01`        | u8                                          | unknown_waypoints_01      | `0` on every spawn                                                                    |
| `waypoints+0x02`        | u32                                         | index_position_count      | Number of `index_positions`, `0` or `1`                                               |
| `waypoints+0x06`        | Index Position[index_position_count]        | index_positions           | See Index Position                                                                    |
| `index_positions+0x00`  | u8                                          | condition_count           | Number of `conditions`, `0` or `1`                                                    |
| `index_positions+0x01`  | Spawn Condition[condition_count]            | conditions                | See Spawn Condition                                                                   |

### Waypoint (5 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | using_type   | `gc::SpawnWaypointUsingType`: `1` go home, `2` go back, `3` to `5` roaming 1 to 3; every list holds `1` to `5` in order |
| `+0x01` | i32  | waypoint_key | `0` for none; the go back key is the negated go home key on every spawn with both       |

### Index Position (18 bytes)

| Offset  | Type | Field      | Notes                          |
| ------- | ---- | ---------- | ------------------------------ |
| `+0x00` | u16  | unknown_00 | `0` on all 34 entries          |
| `+0x02` | f32  | x          | World position                 |
| `+0x06` | f32  | y          |                                |
| `+0x0A` | f32  | z          |                                |
| `+0x0E` | f32  | direction  | Radians                        |

### Spawn Condition (5 bytes)

| Offset  | Type | Field            | Notes                                   |
| ------- | ---- | ---------------- | --------------------------------------- |
| `+0x00` | u8   | unknown_00       | `0` on all 64 entries                   |
| `+0x01` | i16  | spawn_start_hour | `2` on 50 entries, `-1` on 13, `20` on 1 |
| `+0x03` | i16  | spawn_end_hour   | `22` on 50 entries, `-1` on 13, `2` on 1 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | `0` in every file                    |
| `+0x04` | pstr[string_count] | strings      | No field reads a string              |

Counts and values in the Notes cells are from the 1,433 cell files of
client 3482 (95,823 spawns).

## Grid Squares

A field grid square is 3,700 world units on a side, counted from the
field's `world_start_x` and `world_start_z` in
[fieldinfo.bss](fieldinfo_bss.md): square (`grid_x`, `grid_z`) covers
`world_start_x + grid_x * 3700` up to the next square in x, and the same in
z. Field `1` starts at (-2,035,200, -1,113,600), the corner of sector
(-159, -87). On client 3482 every one of the 95,787 field `1` spawns lies
inside the square it is listed under, and 3,700 is the only square size
from 3,600.0 to 3,800.0 (in steps of 0.1) that places them all. The
[instancefield.dbss](instancefield_dbss.md) loader of a private server on
client 1784 multiplies `field_grid_sector_count` by the same 3,700.

A cell file covers 7 x 7 squares, 25,900 units on a side: its name is its
first square, a multiple of 7 on both axes (the folder `7`), and every
square in `553_364.bss` has a `grid_x` of 553 to 559 and a `grid_z` of 364
to 370. This holds for all 1,433 files of client 3482.

The key's sector is the 12,800-unit sector of the spawn's source file
(`<sector_x>_0_<sector_z>_Npc.xml`); `position_x` and `position_z` fall
inside it on 95,785 of the 95,787 field `1` spawns.

## Field Names

The names follow the `SpawnPlacement` XML a private server on client 1784
compiles these files from (`Spawnplacement/MapData_real/1/<x>_0_<z>_<Kind>.xml`,
925,171 entries, most of them gathering points that the grid leaves out).
Its `Key` attribute is the spawn's eight key bytes read as a u64; 57,557 of
the 95,787 field `1` spawns of client 3482 have their key there. Matches
over those keys, by value:

| Field                                   | XML                                         | Match (client 3482)        |
| --------------------------------------- | ------------------------------------------- | -------------------------- |
| `is_spawnable`                          | `IsSpawnable`                               | 57,301 of 57,557           |
| `position_x`, `position_y`, `position_z` | `Position` `X`, `Y`, `Z`                    | 57,346, 57,345 and 57,331 of 57,557 |
| `spawn_range`                           | `Position` `SpawnRange`                     | 57,554 of 57,557           |
| `direction`                             | `Direction`                                 | 57,417 of 57,557           |
| `character_key`                         | `UseSpawnGroup` `SpawnCharacterKey`         | 57,434 of 57,557           |
| `scene_sector_x` to `scene_index`       | `UseSpawnGroup` `SceneUID_X`, `_Y`, `_Z`, `_Type`, `_Index` | 214 of 217 each |
| `spawn_delay_time`                      | `SpawnDelay` `Time`                         | 57,552 of 57,557           |
| `spawn_delay_variable_time`             | `SpawnDelay` `VariableTime`                 | 57,552 of 57,557           |
| `respawn_number`                        | `ReSpawnNumber`                             | 57,557 of 57,557, 3 of them not `0` |
| `event_object_key`                      | `EventObjectKey`                            | 1 of 1                     |
| `live_world_event_key`                  | `LiveWorldEventKey`                         | 1 of 1                     |
| `territory`                             | `Territory`                                 | 745 of 745                 |
| `action_index`                          | `ActionIndex`                               | 52,465 of 52,544           |
| `dialog_index`                          | `DialogIndex`                               | 30,303 of 30,309           |
| `dialog_update_time`                    | `DialogUpdateTime`                          | 1,041 of 1,041             |
| `team_no`                               | `TeamNo`                                    | 2,575 of 2,578             |
| `house_x`, `house_y`, `house_z`         | `House` `X`, `Y`, `Z`                       | 1,034 of 1,035             |
| `waypoint_key` of `using_type` 1 and 2  | `gohome`, `goback`                          | 764 of 766 each            |
| `go_home_type`                          | `GoHomeType`                                | 57,555 of 57,557           |
| Index Position `x` to `direction`       | `SpawnIndexPosition` `X`, `Y`, `Z`, `Direction` | 34 of 34               |
| `spawn_start_hour`, `spawn_end_hour`    | `CustomSpawnCondition` `SpawnStartHour`, `SpawnEndHour` | 64 of 64       |

The misses are keys whose values differ between clients 1784 and 3482. `key_type`
follows the source file name: on the shared keys every `2` comes from a
`_Monster.xml` (715) and every `3` from a `_Npc.xml` (56,842).
`using_type` takes its names from the 2016 `gc::SpawnWaypointUsingType`
(`SWUT_GOHOME` 1, `SWUT_GOBACK` 2, `SWUT_ROAMING1` to `SWUT_ROAMING3` 3 to
5); slots 1 and 2 hold the XML `gohome` and `goback` keys. The grid
squares are the 2016 `gc::FieldGridSectorIndex` (u16 `_x`, u16 `_z`), and
the scene fields the 2016 `PASceneUID` (three i32 sector indexes and two
u16), whose u16 order (`m_nSceneIndex` then `m_nSceneType`) is the reverse
of what the XML values show.

Several fields sit where an XML attribute would go but hold one value on
every spawn and in the XML, so the value cannot place them; they stay
`unknown_*` with their lead:

| Field                      | Lead                                                                 |
| -------------------------- | -------------------------------------------------------------------- |
| `unknown_character_key_10` | `UseSpawnGroup` `SpawnQuantity`, `1` on every entry                  |
| `unknown_character_key_14` | `SpawnDelay` `BootTime`, `0` on every entry                          |
| `unknown_character_key_18` | `SpawnDelay` `BootVariableTime`, `0` on every entry                  |
| `unknown_character_key_25` | `SpawnDelay` `IsSpawnOnBoot`, `1` on every entry                     |
| `unknown_character_key_26` | `SpawnDelay` `IsSpawnOnRealTime` and `IsMainChannelSync`, `0` on every entry |
| Index Position `unknown_00` | `SpawnIndexPosition` `PageIndex`, `0` on every entry                |
| Spawn Condition `unknown_00` | `CustomSpawnCondition` `SpawnConditionType`, `0` on every entry    |

## Notes

- `has_character` is `0` on 47 spawns of client 3482 (38 in field `1`, the
  9 `key_type` `11` spawns of fields 700 and 701), and those spawns have no
  `character_key` bytes. In field `1` their XML entries name characters
  `986` (32 spawns), `759` (4) and `59622` (2), none of which has a
  `characterstatic.dbss` row on client 3482. The private server's copy on
  client 1784 also leaves out `23411` (296 spawns), which client 3482
  writes and has a row for. The key seems to be written only when the
  character exists when the file is built.
- The grid holds key types `2` and `3` only; the XML's gathering
  (`_Collect.xml`), vehicle and stable files have no spawns in it.
- A private server's copy of `spawnplacementfieldgrid/1/7/` on client 1784
  (1,015 cell files, 58,988 spawns) walks by this layout; the client 1784
  test client holds no `mapdata_*` files.
- [fieldgridinfo.bss](fieldgridinfo_bss.md) lists exactly the squares the
  cell files of its folder hold, and [fileinfo.bss](fileinfo_bss.md)
  exactly the cell files.

## Open Questions

### What `key_type` 11 Is

Fields 700 and 701 hold 9 spawns with `key_type` `11` and no character
(`3377553690460161` and up in `700/7/427_238.bss`). The 1784 XML of those
fields is not in the private server's files, so the source file kind of
type `11` is open.

### What `territory` Keys

`territory` matches the XML `Territory` on all 745 shared keys and is `0`,
`1` or `2` where set. Whether these are `territoryinfo.bss` keys (Balenos,
Serendia, Calpheon) is not checked against the positions yet.
