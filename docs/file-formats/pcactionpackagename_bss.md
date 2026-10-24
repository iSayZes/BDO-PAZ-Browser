# `pcactionpackagename.bss` Format

## Purpose

The action chart package each player class loads for a held weapon, a
vehicle, a vehicle with a weapon and cutscenes. A package is a lower-case
path without extension, such as `pc/1_phm/fighteraction_onehandsword`
(Warrior, Longsword) or
`pc/vehicle/riding_ground/horse/fighteraction_ridinghorse` (Warrior on a
horse). On client 3483 the no-weapon packages of 33 classes are files
`character/binaryactionchart/<package>.paac`, such as
`character/binaryactionchart/pc/1_phm/fighteraction_noweapon.paac`; the
other packages have no file of their own. The file is a plain PABR table
with no row count: one block per class type, in class type order, then (from
client 2107) a short list keyed by class type, then the PABR string table
that holds every path and vehicle type name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records                                                                                                | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------ | --------- |
| 19     | 3381 and later | 3483    | `pcactionpackagename.bss` | 548,981 | 11,640 Package Cell, 5,444 Vehicle Row, 11,543 Equip Vehicle List, 97 Class Block, 3 Class Package Row | 8         |
| 18     | 3177 to 3373   | 3373    | `pcactionpackagename.bss` | 510,912 | 10,440 Package Cell, 4,579 Vehicle Row, 10,353 Equip Vehicle List, 87 Class Block, 3 Class Package Row | 8         |
| 17     | 3012 to 3169   | 3169    | `pcactionpackagename.bss` | 509,578 | 10,353 Package Cell, 4,645 Vehicle Row, 10,266 Equip Vehicle List, 87 Class Block, 3 Class Package Row | 8         |
| 16     | 2825 to 3002   | 3002    | `pcactionpackagename.bss` | 507,443 | 10,179 Package Cell, 4,645 Vehicle Row, 10,092 Equip Vehicle List, 87 Class Block, 2 Class Package Row | 8         |
| 15     | 2794 to 2819   | 2819    | `pcactionpackagename.bss` | 554,293 | 10,092 Package Cell, 5,474 Vehicle Row, 10,005 Equip Vehicle List, 87 Class Block, 2 Class Package Row | 8         |
| 14     | 2644 to 2783   | 2783    | `pcactionpackagename.bss` | 542,694 | 10,005 Package Cell, 5,474 Vehicle Row, 9,918 Equip Vehicle List, 87 Class Block, 2 Class Package Row  | 8         |
| 13     | 2601 to 2637   | 2637    | `pcactionpackagename.bss` | 522,022 | 9,831 Package Cell, 5,297 Vehicle Row, 9,744 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8         |
| 12     | 2429 to 2592   | 2592    | `pcactionpackagename.bss` | 520,978 | 9,744 Package Cell, 5,297 Vehicle Row, 9,657 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8         |
| 11     | 2393 to 2421   | 2421    | `pcactionpackagename.bss` | 507,606 | 9,570 Package Cell, 5,225 Vehicle Row, 9,483 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8         |
| 10     | 2302 to 2384   | 2384    | `pcactionpackagename.bss` | 506,562 | 9,483 Package Cell, 5,225 Vehicle Row, 9,396 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8         |
| 9      | 2250 to 2295   | 2295    | `pcactionpackagename.bss` | 497,777 | 8,961 Package Cell, 5,190 Vehicle Row, 8,874 Equip Vehicle List, 87 Class Block                        | 8         |
| 8      | 2207 to 2243   | 2243    | `pcactionpackagename.bss` | 506,186 | 8,364 Package Cell, 7,932 Vehicle Row, 8,282 Equip Vehicle List, 82 Class Block                        | 8         |
| 7      | 2107 to 2203   | 2203    | `pcactionpackagename.bss` | 502,161 | 8,282 Package Cell, 7,828 Vehicle Row, 8,200 Equip Vehicle List, 82 Class Block                        | 8         |
| 6      | 2059 to 2098   | 2098    | `pcactionpackagename.bss` | 492,651 | 8,282 Package Cell, 7,827 Vehicle Row, 8,200 Equip Vehicle List, 82 Class Block                        | 8         |
| 5      | 1991 to 2052   | 2052    | `pcactionpackagename.bss` | 490,625 | 8,118 Package Cell, 7,827 Vehicle Row, 8,036 Equip Vehicle List, 82 Class Block                        | 8         |
| 4      | 1794 to 1985   | 1985    | `pcactionpackagename.bss` | 450,061 | 7,872 Package Cell, 7,335 Vehicle Row, 7,790 Equip Vehicle List, 82 Class Block                        | 8         |
| 3      | 1790           | 1790    | `pcactionpackagename.bss` | 366,086 | 7,708 Package Cell, 5,887 Vehicle Row, 7,626 Equip Vehicle List, 82 Class Block                        | 8         |
| 2      | 1774 to 1784   | 1784    | `pcactionpackagename.bss` | 362,622 | 7,626 Package Cell, 5,839 Vehicle Row, 7,544 Equip Vehicle List, 82 Class Block                        | 8         |
| 1      | 1743 to 1771   | 1771    | `pcactionpackagename.bss` | 362,128 | 7,544 Package Cell, 5,884 Vehicle Row, 7,462 Equip Vehicle List, 82 Class Block                        | 8         |

| Layout | File                      | Known              | Unknown    |
| ------ | ------------------------- | ------------------ | ---------- |
| 19     | `pcactionpackagename.bss` | 548,977 B (100.0%) | 4 B (0.0%) |
| 18     | `pcactionpackagename.bss` | 510,908 B (100.0%) | 4 B (0.0%) |
| 17     | `pcactionpackagename.bss` | 509,574 B (100.0%) | 4 B (0.0%) |
| 16     | `pcactionpackagename.bss` | 507,439 B (100.0%) | 4 B (0.0%) |
| 15     | `pcactionpackagename.bss` | 554,289 B (100.0%) | 4 B (0.0%) |
| 14     | `pcactionpackagename.bss` | 542,690 B (100.0%) | 4 B (0.0%) |
| 13     | `pcactionpackagename.bss` | 522,018 B (100.0%) | 4 B (0.0%) |
| 12     | `pcactionpackagename.bss` | 520,974 B (100.0%) | 4 B (0.0%) |
| 11     | `pcactionpackagename.bss` | 507,602 B (100.0%) | 4 B (0.0%) |
| 10     | `pcactionpackagename.bss` | 506,558 B (100.0%) | 4 B (0.0%) |
| 9      | `pcactionpackagename.bss` | 497,773 B (100.0%) | 4 B (0.0%) |
| 8      | `pcactionpackagename.bss` | 506,182 B (100.0%) | 4 B (0.0%) |
| 7      | `pcactionpackagename.bss` | 502,157 B (100.0%) | 4 B (0.0%) |
| 6      | `pcactionpackagename.bss` | 492,651 B (100.0%) | 0 B (0.0%) |
| 5      | `pcactionpackagename.bss` | 490,625 B (100.0%) | 0 B (0.0%) |
| 4      | `pcactionpackagename.bss` | 450,061 B (100.0%) | 0 B (0.0%) |
| 3      | `pcactionpackagename.bss` | 366,086 B (100.0%) | 0 B (0.0%) |
| 2      | `pcactionpackagename.bss` | 362,622 B (100.0%) | 0 B (0.0%) |
| 1      | `pcactionpackagename.bss` | 362,128 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 19            | `2ae10897d3e2`  |
| 3482   | Layout 19            | `2ae10897d3e2`  |
| 3474   | Layout 19            | `2ae10897d3e2`  |
| 3473   | Layout 19            | `2ae10897d3e2`  |
| 3464   | Layout 19            | `2ae10897d3e2`  |
| 3458   | Layout 19            | `2ae10897d3e2`  |
| 3454   | Layout 19            | `2ae10897d3e2`  |
| 3444   | Layout 19            | `2ae10897d3e2`  |
| 3435   | Layout 19            | `2ae10897d3e2`  |
| 3426   | Layout 19            | `2ae10897d3e2`  |
| 3418   | Layout 19            | `2ae10897d3e2`  |
| 3412   | Layout 19            | `2ae10897d3e2`  |
| 3402   | Layout 19            | `2ae10897d3e2`  |
| 3396   | Layout 19            | `2ae10897d3e2`  |
| 3387   | Layout 19            | `2ae10897d3e2`  |
| 3381   | Layout 19            | `2ae10897d3e2`  |
| 3373   | Layout 18            | `2ae10897d3e2`  |
| 3364   | Layout 18            | `2ae10897d3e2`  |
| 3356   | Layout 18            | `2ae10897d3e2`  |
| 3349   | Layout 18            | `2ae10897d3e2`  |
| 3342   | Layout 18            | `2ae10897d3e2`  |
| 3335   | Layout 18            | `2ae10897d3e2`  |
| 3326   | Layout 18            | `2ae10897d3e2`  |
| 3321   | Layout 18            | `2ae10897d3e2`  |
| 3314   | Layout 18            | `2ae10897d3e2`  |
| 3303   | Layout 18            | `2ae10897d3e2`  |
| 3302   | Layout 18            | `2ae10897d3e2`  |
| 3293   | Layout 18            | `2ae10897d3e2`  |
| 3283   | Layout 18            | `2ae10897d3e2`  |
| 3275   | Layout 18            | `2ae10897d3e2`  |
| 3267   | Layout 18            | `2ae10897d3e2`  |
| 3258   | Layout 18            | `2ae10897d3e2`  |
| 3251   | Layout 18            | `2ae10897d3e2`  |
| 3242   | Layout 18            | `2ae10897d3e2`  |
| 3235   | Layout 18            | `2ae10897d3e2`  |
| 3229   | Layout 18            | `2ae10897d3e2`  |
| 3212   | Layout 18            | `2ae10897d3e2`  |
| 3203   | Layout 18            | `2ae10897d3e2`  |
| 3193   | Layout 18            | `2ae10897d3e2`  |
| 3186   | Layout 18            | `2ae10897d3e2`  |
| 3177   | Layout 18            | `2ae10897d3e2`  |
| 3169   | Layout 17            | `2ae10897d3e2`  |
| 3158   | Layout 17            | `2ae10897d3e2`  |
| 3151   | Layout 17            | `2ae10897d3e2`  |
| 3144   | Layout 17            | `2ae10897d3e2`  |
| 3133   | Layout 17            | `2ae10897d3e2`  |
| 3125   | Layout 17            | `2ae10897d3e2`  |
| 3118   | Layout 17            | `2ae10897d3e2`  |
| 3111   | Layout 17            | `2ae10897d3e2`  |
| 3103   | Layout 17            | `2ae10897d3e2`  |
| 3095   | Layout 17            | `2ae10897d3e2`  |
| 3086   | Layout 17            | `2ae10897d3e2`  |
| 3072   | Layout 17            | `2ae10897d3e2`  |
| 3062   | Layout 17            | `2ae10897d3e2`  |
| 3052   | Layout 17            | `2ae10897d3e2`  |
| 3045   | Layout 17            | `2ae10897d3e2`  |
| 3037   | Layout 17            | `2ae10897d3e2`  |
| 3030   | Layout 17            | `2ae10897d3e2`  |
| 3021   | Layout 17            | `2ae10897d3e2`  |
| 3012   | Layout 17            | `2ae10897d3e2`  |
| 3002   | Layout 16            | `2ae10897d3e2`  |
| 2995   | Layout 16            | `2ae10897d3e2`  |
| 2987   | Layout 16            | `2ae10897d3e2`  |
| 2978   | Layout 16            | `2ae10897d3e2`  |
| 2970   | Layout 16            | `2ae10897d3e2`  |
| 2959   | Layout 16            | `2ae10897d3e2`  |
| 2951   | Layout 16            | `2ae10897d3e2`  |
| 2942   | Layout 16            | `2ae10897d3e2`  |
| 2935   | Layout 16            | `2ae10897d3e2`  |
| 2932   | Layout 16            | `2ae10897d3e2`  |
| 2923   | Layout 16            | `2ae10897d3e2`  |
| 2919   | Layout 16            | `2ae10897d3e2`  |
| 2907   | Layout 16            | `2ae10897d3e2`  |
| 2900   | Layout 16            | `2ae10897d3e2`  |
| 2891   | Layout 16            | `2ae10897d3e2`  |
| 2882   | Layout 16            | `2ae10897d3e2`  |
| 2872   | Layout 16            | `2ae10897d3e2`  |
| 2863   | Layout 16            | `2ae10897d3e2`  |
| 2855   | Layout 16            | `2ae10897d3e2`  |
| 2849   | Layout 16            | `2ae10897d3e2`  |
| 2844   | Layout 16            | `2ae10897d3e2`  |
| 2834   | Layout 16            | `2ae10897d3e2`  |
| 2825   | Layout 16            | `2ae10897d3e2`  |
| 2819   | Layout 15            | `2ae10897d3e2`  |
| 2811   | Layout 15            | `2ae10897d3e2`  |
| 2803   | Layout 15            | `2ae10897d3e2`  |
| 2794   | Layout 15            | `2ae10897d3e2`  |
| 2783   | Layout 14            | `2ae10897d3e2`  |
| 2774   | Layout 14            | `2ae10897d3e2`  |
| 2765   | Layout 14            | `2ae10897d3e2`  |
| 2756   | Layout 14            | `2ae10897d3e2`  |
| 2750   | Layout 14            | `2ae10897d3e2`  |
| 2743   | Layout 14            | `2ae10897d3e2`  |
| 2736   | Layout 14            | `2ae10897d3e2`  |
| 2726   | Layout 14            | `2ae10897d3e2`  |
| 2717   | Layout 14            | `2ae10897d3e2`  |
| 2709   | Layout 14            | `2ae10897d3e2`  |
| 2703   | Layout 14            | `2ae10897d3e2`  |
| 2695   | Layout 14            | `2ae10897d3e2`  |
| 2684   | Layout 14            | `2ae10897d3e2`  |
| 2672   | Layout 14            | `2ae10897d3e2`  |
| 2665   | Layout 14            | `2ae10897d3e2`  |
| 2657   | Layout 14            | `2ae10897d3e2`  |
| 2649   | Layout 14            | `2ae10897d3e2`  |
| 2644   | Layout 14            | `2ae10897d3e2`  |
| 2637   | Layout 13            | `2ae10897d3e2`  |
| 2629   | Layout 13            | `2ae10897d3e2`  |
| 2619   | Layout 13            | `2ae10897d3e2`  |
| 2612   | Layout 13            | `2ae10897d3e2`  |
| 2606   | Layout 13            | `2ae10897d3e2`  |
| 2602   | Layout 13            | `2ae10897d3e2`  |
| 2601   | Layout 13            | `2ae10897d3e2`  |
| 2592   | Layout 12            | `2ae10897d3e2`  |
| 2583   | Layout 12            | `2ae10897d3e2`  |
| 2575   | Layout 12            | `2ae10897d3e2`  |
| 2567   | Layout 12            | `2ae10897d3e2`  |
| 2560   | Layout 12            | `2ae10897d3e2`  |
| 2553   | Layout 12            | `2ae10897d3e2`  |
| 2545   | Layout 12            | `2ae10897d3e2`  |
| 2538   | Layout 12            | `2ae10897d3e2`  |
| 2529   | Layout 12            | `2ae10897d3e2`  |
| 2519   | Layout 12            | `2ae10897d3e2`  |
| 2513   | Layout 12            | `2ae10897d3e2`  |
| 2510   | Layout 12            | `2ae10897d3e2`  |
| 2507   | Layout 12            | `2ae10897d3e2`  |
| 2503   | Layout 12            | `2ae10897d3e2`  |
| 2498   | Layout 12            | `2ae10897d3e2`  |
| 2492   | Layout 12            | `2ae10897d3e2`  |
| 2487   | Layout 12            | `2ae10897d3e2`  |
| 2480   | Layout 12            | `2ae10897d3e2`  |
| 2474   | Layout 12            | `2ae10897d3e2`  |
| 2468   | Layout 12            | `2ae10897d3e2`  |
| 2460   | Layout 12            | `2ae10897d3e2`  |
| 2453   | Layout 12            | `2ae10897d3e2`  |
| 2444   | Layout 12            | `2ae10897d3e2`  |
| 2438   | Layout 12            | `2ae10897d3e2`  |
| 2434   | Layout 12            | `2ae10897d3e2`  |
| 2429   | Layout 12            | `2ae10897d3e2`  |
| 2421   | Layout 11            | `2ae10897d3e2`  |
| 2414   | Layout 11            | `2ae10897d3e2`  |
| 2407   | Layout 11            | `2ae10897d3e2`  |
| 2401   | Layout 11            | `2ae10897d3e2`  |
| 2397   | Layout 11            | `2ae10897d3e2`  |
| 2393   | Layout 11            | `2ae10897d3e2`  |
| 2384   | Layout 10            | `2ae10897d3e2`  |
| 2378   | Layout 10            | `2ae10897d3e2`  |
| 2372   | Layout 10            | `2ae10897d3e2`  |
| 2358   | Layout 10            | `2ae10897d3e2`  |
| 2352   | Layout 10            | `2ae10897d3e2`  |
| 2347   | Layout 10            | `2ae10897d3e2`  |
| 2343   | Layout 10            | `2ae10897d3e2`  |
| 2335   | Layout 10            | `2ae10897d3e2`  |
| 2327   | Layout 10            | `2ae10897d3e2`  |
| 2324   | Layout 10            | `2ae10897d3e2`  |
| 2319   | Layout 10            | `2ae10897d3e2`  |
| 2313   | Layout 10            | `2ae10897d3e2`  |
| 2308   | Layout 10            | `2ae10897d3e2`  |
| 2302   | Layout 10            | `2ae10897d3e2`  |
| 2295   | Layout 9             | `2ae10897d3e2`  |
| 2290   | Layout 9             | `2ae10897d3e2`  |
| 2284   | Layout 9             | `2ae10897d3e2`  |
| 2276   | Layout 9             | `2ae10897d3e2`  |
| 2269   | Layout 9             | `2ae10897d3e2`  |
| 2259   | Layout 9             | `2ae10897d3e2`  |
| 2250   | Layout 9             | `2ae10897d3e2`  |
| 2243   | Layout 8             | `2ae10897d3e2`  |
| 2235   | Layout 8             | `2ae10897d3e2`  |
| 2229   | Layout 8             | `2ae10897d3e2`  |
| 2224   | Layout 8             | `2ae10897d3e2`  |
| 2218   | Layout 8             | `2ae10897d3e2`  |
| 2215   | Layout 8             | `2ae10897d3e2`  |
| 2207   | Layout 8             | `2ae10897d3e2`  |
| 2203   | Layout 7             | `2ae10897d3e2`  |
| 2196   | Layout 7             | `2ae10897d3e2`  |
| 2192   | Layout 7             | `2ae10897d3e2`  |
| 2189   | Layout 7             | `2ae10897d3e2`  |
| 2183   | Layout 7             | `2ae10897d3e2`  |
| 2179   | Layout 7             | `2ae10897d3e2`  |
| 2171   | Layout 7             | `2ae10897d3e2`  |
| 2163   | Layout 7             | `2ae10897d3e2`  |
| 2156   | Layout 7             | `2ae10897d3e2`  |
| 2151   | Layout 7             | `2ae10897d3e2`  |
| 2147   | Layout 7             | `2ae10897d3e2`  |
| 2142   | Layout 7             | `2ae10897d3e2`  |
| 2138   | Layout 7             | `2ae10897d3e2`  |
| 2134   | Layout 7             | `2ae10897d3e2`  |
| 2130   | Layout 7             | `2ae10897d3e2`  |
| 2122   | Layout 7             | `2ae10897d3e2`  |
| 2107   | Layout 7             | `2ae10897d3e2`  |
| 2098   | Layout 6             | `2ae10897d3e2`  |
| 2089   | Layout 6             | `2ae10897d3e2`  |
| 2081   | Layout 6             | `2ae10897d3e2`  |
| 2073   | Layout 6             | `2ae10897d3e2`  |
| 2067   | Layout 6             | `2ae10897d3e2`  |
| 2063   | Layout 6             | `2ae10897d3e2`  |
| 2059   | Layout 6             | `2ae10897d3e2`  |
| 2052   | Layout 5             | `2ae10897d3e2`  |
| 2044   | Layout 5             | `2ae10897d3e2`  |
| 2039   | Layout 5             | `2ae10897d3e2`  |
| 2032   | Layout 5             | `2ae10897d3e2`  |
| 2025   | Layout 5             | `2ae10897d3e2`  |
| 2011   | Layout 5             | `2ae10897d3e2`  |
| 2005   | Layout 5             | `2ae10897d3e2`  |
| 2000   | Layout 5             | `2ae10897d3e2`  |
| 1996   | Layout 5             | `2ae10897d3e2`  |
| 1991   | Layout 5             | `2ae10897d3e2`  |
| 1985   | Layout 4             | `2ae10897d3e2`  |
| 1980   | Layout 4             | `2ae10897d3e2`  |
| 1969   | Layout 4             | `2ae10897d3e2`  |
| 1964   | Layout 4             | `2ae10897d3e2`  |
| 1958   | Layout 4             | `2ae10897d3e2`  |
| 1950   | Layout 4             | `2ae10897d3e2`  |
| 1945   | Layout 4             | `2ae10897d3e2`  |
| 1937   | Layout 4             | `2ae10897d3e2`  |
| 1933   | Layout 4             | `2ae10897d3e2`  |
| 1927   | Layout 4             | `2ae10897d3e2`  |
| 1921   | Layout 4             | `2ae10897d3e2`  |
| 1914   | Layout 4             | `2ae10897d3e2`  |
| 1908   | Layout 4             | `2ae10897d3e2`  |
| 1897   | Layout 4             | `2ae10897d3e2`  |
| 1892   | Layout 4             | `2ae10897d3e2`  |
| 1886   | Layout 4             | `2ae10897d3e2`  |
| 1881   | Layout 4             | `2ae10897d3e2`  |
| 1871   | Layout 4             | `2ae10897d3e2`  |
| 1866   | Layout 4             | `2ae10897d3e2`  |
| 1862   | Layout 4             | `2ae10897d3e2`  |
| 1854   | Layout 4             | `2ae10897d3e2`  |
| 1846   | Layout 4             | `2ae10897d3e2`  |
| 1838   | Layout 4             | `2ae10897d3e2`  |
| 1832   | Layout 4             | `2ae10897d3e2`  |
| 1826   | Layout 4             | `2ae10897d3e2`  |
| 1822   | Layout 4             | `2ae10897d3e2`  |
| 1818   | Layout 4             | `2ae10897d3e2`  |
| 1804   | Layout 4             | `2ae10897d3e2`  |
| 1794   | Layout 4             | `2ae10897d3e2`  |
| 1790   | Layout 3             | `2ae10897d3e2`  |
| 1784   | Layout 2             | `2ae10897d3e2`  |
| 1774   | Layout 2             | `2ae10897d3e2`  |
| 1771   | Layout 1             | `2ae10897d3e2`  |
| 1762   | Layout 1             | `2ae10897d3e2`  |
| 1759   | Layout 1             | `2ae10897d3e2`  |
| 1754   | Layout 1             | `2ae10897d3e2`  |
| 1749   | Layout 1             | `2ae10897d3e2`  |
| 1743   | Layout 1             | `2ae10897d3e2`  |
| 1737   | No documented layout | `2ae10897d3e2`  |
| 1731   | No documented layout | `2ae10897d3e2`  |
| 1725   | No documented layout | `2ae10897d3e2`  |
| 1717   | No documented layout | `2ae10897d3e2`  |
| 1710   | No documented layout | `2ae10897d3e2`  |
| 1704   | No documented layout | `2ae10897d3e2`  |
| 1698   | No documented layout | `2ae10897d3e2`  |
| 1690   | No documented layout | `2ae10897d3e2`  |
| 1685   | No documented layout | `2ae10897d3e2`  |
| 1680   | No documented layout | `2ae10897d3e2`  |
| 1674   | No documented layout | `2ae10897d3e2`  |
| 1668   | No documented layout | `2ae10897d3e2`  |
| 1659   | No documented layout | `2ae10897d3e2`  |
| 1649   | No documented layout | `2ae10897d3e2`  |
| 1642   | No documented layout | `2ae10897d3e2`  |
| 1636   | No documented layout | `2ae10897d3e2`  |
| 1628   | No documented layout | `2ae10897d3e2`  |
| 1622   | No documented layout | `2ae10897d3e2`  |
| 1614   | No documented layout | `2ae10897d3e2`  |
| 1608   | No documented layout | `2ae10897d3e2`  |
| 1602   | No documented layout | `2ae10897d3e2`  |
| 1598   | No documented layout | `2ae10897d3e2`  |
| 1594   | No documented layout | `2ae10897d3e2`  |
| 1590   | No documented layout | `2ae10897d3e2`  |
| 1587   | No documented layout | `2ae10897d3e2`  |
| 1584   | No documented layout | `2ae10897d3e2`  |
| 1579   | No documented layout | `2ae10897d3e2`  |
| 1572   | No documented layout | `2ae10897d3e2`  |
| 1565   | No documented layout | `2ae10897d3e2`  |
| 1559   | No documented layout | `2ae10897d3e2`  |
| 1554   | No documented layout | `2ae10897d3e2`  |
| 1547   | No documented layout | `2ae10897d3e2`  |
| 1537   | No documented layout | `2ae10897d3e2`  |
| 1529   | No documented layout | `2ae10897d3e2`  |
| 1524   | No documented layout | `2ae10897d3e2`  |
| 1519   | No documented layout | `2ae10897d3e2`  |
| 1509   | No documented layout | `2ae10897d3e2`  |
| 1506   | No documented layout | `2ae10897d3e2`  |
| 1504   | No documented layout | `2ae10897d3e2`  |
| 1500   | No documented layout | `2ae10897d3e2`  |
| 1493   | No documented layout | `2ae10897d3e2`  |
| 1489   | No documented layout | `2ae10897d3e2`  |
| 1485   | No documented layout | `2ae10897d3e2`  |
| 1481   | No documented layout | `2ae10897d3e2`  |
| 1474   | No documented layout | `2ae10897d3e2`  |
| 1466   | No documented layout | `2ae10897d3e2`  |
| 1462   | No documented layout | `2ae10897d3e2`  |
| 1459   | No documented layout | `2ae10897d3e2`  |
| 1453   | No documented layout | `2ae10897d3e2`  |
| 1450   | No documented layout | `2ae10897d3e2`  |
| 1445   | No documented layout | `2ae10897d3e2`  |
| 1439   | No documented layout | `2ae10897d3e2`  |
| 1433   | No documented layout | `2ae10897d3e2`  |
| 1430   | No documented layout | `2ae10897d3e2`  |
| 1426   | No documented layout | `2ae10897d3e2`  |
| 1421   | No documented layout | `2ae10897d3e2`  |
| 1417   | No documented layout | `2ae10897d3e2`  |
| 1416   | No documented layout | `2ae10897d3e2`  |
| 1409   | No documented layout | `2ae10897d3e2`  |
| 1405   | No documented layout | `2ae10897d3e2`  |
| 1401   | No documented layout | `2ae10897d3e2`  |
| 1396   | No documented layout | `2ae10897d3e2`  |
| 1391   | No documented layout | `2ae10897d3e2`  |
| 1390   | No documented layout | `2ae10897d3e2`  |
| 1386   | No documented layout | `2ae10897d3e2`  |
| 1381   | No documented layout | `2ae10897d3e2`  |
| 1379   | No documented layout | `2ae10897d3e2`  |
| 1372   | No documented layout | `2ae10897d3e2`  |
| 1366   | No documented layout | `2ae10897d3e2`  |
| 1364   | No documented layout | `2ae10897d3e2`  |
| 1363   | No documented layout | `2ae10897d3e2`  |
| 1360   | No documented layout | `2ae10897d3e2`  |
| 1358   | No documented layout | `2ae10897d3e2`  |
| 1355   | No documented layout | `2ae10897d3e2`  |
| 1351   | No documented layout | `2ae10897d3e2`  |
| 1348   | No documented layout | `2ae10897d3e2`  |
| 1346   | No documented layout | `2ae10897d3e2`  |
| 1341   | No documented layout | `2ae10897d3e2`  |
| 1340   | No documented layout | `2ae10897d3e2`  |
| 1338   | No documented layout | `2ae10897d3e2`  |
| 1335   | No documented layout | `2ae10897d3e2`  |
| 1333   | No documented layout | `2ae10897d3e2`  |
| 1329   | No documented layout | `2ae10897d3e2`  |
| 1327   | No documented layout | `2ae10897d3e2`  |
| 1324   | No documented layout | `2ae10897d3e2`  |
| 1321   | No documented layout | `2ae10897d3e2`  |
| 1319   | No documented layout | `2ae10897d3e2`  |
| 1318   | No documented layout | `2ae10897d3e2`  |
| 1316   | No documented layout | `2ae10897d3e2`  |
| 1313   | No documented layout | `2ae10897d3e2`  |
| 1311   | No documented layout | `2ae10897d3e2`  |
| 1309   | No documented layout | `2ae10897d3e2`  |
| 1304   | No documented layout | `2ae10897d3e2`  |
| 1292   | No documented layout | `2ae10897d3e2`  |
| 1286   | No documented layout | `2ae10897d3e2`  |
| 1280   | No documented layout | `2ae10897d3e2`  |
| 1276   | No documented layout | `2ae10897d3e2`  |
| 1267   | No documented layout | `2ae10897d3e2`  |
| 1261   | No documented layout | `2ae10897d3e2`  |
| 1256   | No documented layout | `2ae10897d3e2`  |
| 1250   | No documented layout | `2ae10897d3e2`  |
| 1246   | No documented layout | `2ae10897d3e2`  |
| 1239   | No documented layout | `2ae10897d3e2`  |
| 1230   | No documented layout | `2ae10897d3e2`  |
| 1226   | No documented layout | `2ae10897d3e2`  |
| 1220   | No documented layout | `2ae10897d3e2`  |
| 1217   | No documented layout | `2ae10897d3e2`  |
| 1211   | No documented layout | `2ae10897d3e2`  |
| 1210   | No documented layout | `2ae10897d3e2`  |
| 1208   | No documented layout | `2ae10897d3e2`  |
| 1203   | No documented layout | `2ae10897d3e2`  |
| 1197   | No documented layout | `2ae10897d3e2`  |
| 1194   | No documented layout | `2ae10897d3e2`  |
| 1192   | No documented layout | `2ae10897d3e2`  |
| 1187   | No documented layout | `2ae10897d3e2`  |
| 1183   | No documented layout | `2ae10897d3e2`  |
| 1177   | No documented layout | `2ae10897d3e2`  |
| 1173   | No documented layout | `2ae10897d3e2`  |
| 1167   | No documented layout | `2ae10897d3e2`  |
| 1164   | No documented layout | `2ae10897d3e2`  |
| 1156   | No documented layout | `2ae10897d3e2`  |
| 1149   | No documented layout | `2ae10897d3e2`  |
| 1144   | No documented layout | `2ae10897d3e2`  |
| 1137   | No documented layout | `2ae10897d3e2`  |
| 1132   | No documented layout | `2ae10897d3e2`  |
| 1127   | No documented layout | `2ae10897d3e2`  |
| 1122   | No documented layout | `2ae10897d3e2`  |
| 1118   | No documented layout | `2ae10897d3e2`  |
| 1114   | No documented layout | `2ae10897d3e2`  |
| 1109   | No documented layout | `2ae10897d3e2`  |
| 1102   | No file              | `2ae10897d3e2`  |
| 1096   | No file              | `2ae10897d3e2`  |
| 1088   | No file              | `2ae10897d3e2`  |
| 1081   | No file              | `2ae10897d3e2`  |
| 1076   | No file              | `2ae10897d3e2`  |
| 1069   | No file              | `2ae10897d3e2`  |
| 1064   | No file              | `2ae10897d3e2`  |
| 1058   | No file              | `2ae10897d3e2`  |
| 1051   | No file              | `2ae10897d3e2`  |
| 1044   | No file              | `2ae10897d3e2`  |
| 1036   | No file              | `2ae10897d3e2`  |
| 1026   | No file              | `2ae10897d3e2`  |
| 1016   | No file              | `2ae10897d3e2`  |
| 1009   | No file              | `2ae10897d3e2`  |
| 1005   | No file              | `2ae10897d3e2`  |
| 1000   | No file              | `2ae10897d3e2`  |
| 998    | No file              | `2ae10897d3e2`  |
| 990    | No file              | `2ae10897d3e2`  |
| 979    | No file              | `2ae10897d3e2`  |
| 972    | No file              | `2ae10897d3e2`  |
| 963    | No file              | `2ae10897d3e2`  |
| 955    | No file              | `2ae10897d3e2`  |
| 946    | No file              | `2ae10897d3e2`  |
| 938    | No file              | `2ae10897d3e2`  |
| 927    | No file              | `2ae10897d3e2`  |
| 911    | No file              | `2ae10897d3e2`  |
| 904    | No file              | `2ae10897d3e2`  |
| 899    | No file              | `2ae10897d3e2`  |
| 894    | No file              | `2ae10897d3e2`  |
| 885    | No file              | `2ae10897d3e2`  |
| 879    | No file              | `2ae10897d3e2`  |
| 872    | No file              | `2ae10897d3e2`  |
| 864    | No file              | `2ae10897d3e2`  |
| 855    | No file              | `2ae10897d3e2`  |
| 853    | No file              | `2ae10897d3e2`  |
| 845    | No file              | `2ae10897d3e2`  |
| 837    | No file              | `2ae10897d3e2`  |
| 829    | No documented layout | `2ae10897d3e2`  |
| 822    | No documented layout | `2ae10897d3e2`  |
| 814    | No documented layout | `2ae10897d3e2`  |
| 805    | No documented layout | `2ae10897d3e2`  |
| 794    | No documented layout | `2ae10897d3e2`  |
| 787    | No documented layout | `2ae10897d3e2`  |
| 780    | No documented layout | `2ae10897d3e2`  |
| 771    | No documented layout | `2ae10897d3e2`  |
| 760    | No documented layout | `2ae10897d3e2`  |
| 748    | No documented layout | `2ae10897d3e2`  |
| 741    | No documented layout | `2ae10897d3e2`  |
| 736    | No documented layout | `2ae10897d3e2`  |
| 731    | No documented layout | `2ae10897d3e2`  |
| 723    | No documented layout | `2ae10897d3e2`  |
| 711    | No documented layout | `2ae10897d3e2`  |
| 707    | No documented layout | `2ae10897d3e2`  |
| 697    | No documented layout | `2ae10897d3e2`  |
| 689    | No documented layout | `2ae10897d3e2`  |
| 683    | No documented layout | `2ae10897d3e2`  |
| 678    | No documented layout | `2ae10897d3e2`  |
| 670    | No documented layout | `2ae10897d3e2`  |
| 661    | No documented layout | `2ae10897d3e2`  |
| 656    | No documented layout | `2ae10897d3e2`  |
| 652    | No documented layout | `2ae10897d3e2`  |
| 643    | No documented layout | `2ae10897d3e2`  |
| 637    | No documented layout | `2ae10897d3e2`  |
| 630    | No documented layout | `2ae10897d3e2`  |
| 627    | No documented layout | `2ae10897d3e2`  |
| 621    | No documented layout | `2ae10897d3e2`  |
| 617    | No documented layout | `2ae10897d3e2`  |
| 615    | No documented layout | `2ae10897d3e2`  |
| 606    | No documented layout | `2ae10897d3e2`  |
| 599    | No documented layout | `2ae10897d3e2`  |
| 592    | No documented layout | `2ae10897d3e2`  |
| 586    | No documented layout | `2ae10897d3e2`  |
| 577    | No documented layout | `2ae10897d3e2`  |
| 569    | No documented layout | `2ae10897d3e2`  |
| 561    | No documented layout | `2ae10897d3e2`  |
| 554    | No documented layout | `2ae10897d3e2`  |
| 542    | No documented layout | `2ae10897d3e2`  |
| 532    | No documented layout | `2ae10897d3e2`  |
| 531    | No documented layout | `2ae10897d3e2`  |
| 526    | No documented layout | `2ae10897d3e2`  |
| 521    | No documented layout | `2ae10897d3e2`  |
| 517    | No documented layout | `2ae10897d3e2`  |
| 510    | No documented layout | `2ae10897d3e2`  |
| 508    | No documented layout | `2ae10897d3e2`  |
| 504    | No documented layout | `2ae10897d3e2`  |
| 497    | No documented layout | `2ae10897d3e2`  |
| 491    | No documented layout | `2ae10897d3e2`  |
| 485    | No documented layout | `2ae10897d3e2`  |
| 478    | No documented layout | `2ae10897d3e2`  |
| 472    | No documented layout | `2ae10897d3e2`  |
| 466    | No documented layout | `2ae10897d3e2`  |
| 457    | No documented layout | `2ae10897d3e2`  |
| 452    | No documented layout | `2ae10897d3e2`  |
| 449    | No documented layout | `2ae10897d3e2`  |
| 435    | No documented layout | `2ae10897d3e2`  |

<!-- versions:end -->

## Companion Files

The handler reads no other file. Class names come from LOC type 21
(`languagedata_*.loc`) when LOC is loaded; equip type names are built into
the handler, see [Equip Types](#equip-types).

All multi-byte values are little-endian.

## Block Counts

Neither block count is stored. The class type count is the number of class
blocks before the class package list (or the string table, where there is
no list), the equip type count the number of Package Cells at the start of
each block. Both grow with the client, and the class package list arrived
later, so the layouts differ only in these three:

| Layout | Class types | Equip types | Class package list |
| ------ | ----------- | ----------- | ------------------ |
| 19     | 97          | 119         | yes                |
| 18     | 87          | 119         | yes                |
| 17     | 87          | 118         | yes                |
| 16     | 87          | 116         | yes                |
| 15     | 87          | 115         | yes                |
| 14     | 87          | 114         | yes                |
| 13     | 87          | 112         | yes                |
| 12     | 87          | 111         | yes                |
| 11     | 87          | 109         | yes                |
| 10     | 87          | 108         | yes                |
| 9      | 87          | 102         | yes                |
| 8      | 82          | 101         | yes                |
| 7      | 82          | 100         | yes                |
| 6      | 82          | 100         | no                 |
| 5      | 82          | 98          | no                 |
| 4      | 82          | 95          | no                 |
| 3      | 82          | 93          | no                 |
| 2      | 82          | 92          | no                 |
| 1      | 82          | 91          | no                 |

The handler reads every layout with one walk that finds the counts in the
file. The equip type count is the smallest one for which class block `0`
holds a valid [package hash](#package-hash) in every cell and row and the
blocks then reach `string_table_start`; the class blocks go on until the
rest is nothing or exactly one class package list (a u32 count and that
many 9-byte rows). The doc check walks literal counts only (`T[N]` or
`T[field]` in [format-docs.md](../format-docs.md#types)), so each count pair
is a layout of its own here. An older layout lists only the File Layout or
Class Block that differs from the next newer one.

## Layout 19

### File Layout

| Offset                        | Type                                            | Field                       | Notes                                                                      |
| ----------------------------- | ----------------------------------------------- | --------------------------- | -------------------------------------------------------------------------- |
| `+0x00`                       | char[4]                                         | magic                       | ASCII `PABR`; no row count follows                                         |
| `+0x04`                       | Class Block[97]                                 | classes                     | One block per class type, `0` to `96`; see Class Block                     |
| `classes+0x00`                | u32                                             | unknown_class_package_count | `3` on client 3483                                                         |
| `classes+0x04`                | Class Package Row[unknown_class_package_count]  | unknown_class_packages      | See Class Package Row and [Open Questions](#open-questions)                |
| `unknown_class_packages+0x00` | String Table                                    | string_table                | See String Table                                                           |
| `string_table+0x00`           | u32                                             | string_table_start          | Offset of `string_count`, where `unknown_class_packages` ends              |
| `string_table+0x04`           | u32                                             | zero                        | Always `0`                                                                 |

97 class types and 119 equip types (`0` to `118`, the `equip_type` range of
[`itemenchant.dbss`](itemenchant_dbss.md#equip_type)); see
[Block Counts](#block-counts). Walking 97 blocks and the list ends exactly
at `string_table_start`.

### Class Block (variable: 964 bytes + vehicle rows)

| Offset                         | Type                         | Field                   | Notes                                                                  |
| ------------------------------ | ---------------------------- | ----------------------- | ---------------------------------------------------------------------- |
| `+0x00`                        | Package Cell[119]            | weapon_packages         | One cell per equip type; see [Equip Types](#equip-types)               |
| `+0x3B8`                       | u32                          | vehicle_count           | `0`, `66`, `137`, `140` or `141` (client 3483)                         |
| `+0x3BC`                       | Vehicle Row[vehicle_count]   | vehicle_packages        | One row per vehicle type name                                          |
| `vehicle_packages+0x00`        | Equip Vehicle List[119]      | vehicle_weapon_packages | One list per equip type: the package on a vehicle with that weapon     |
| `vehicle_weapon_packages+0x00` | Package Cell                 | cutscene_package        | The class's cutscene package, such as `pc/cutscene/fighteraction_cutscene` |

### Package Cell (8 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | package_index | Index into the string table; an empty cell points at the empty string       |
| `+0x04` | u32  | package_hash  | Hash of the package path, see [Package Hash](#package-hash); `0` when empty |

### Vehicle Row (12 bytes)

| Offset  | Type | Field              | Notes                                                                   |
| ------- | ---- | ------------------ | ----------------------------------------------------------------------- |
| `+0x00` | u32  | vehicle_name_index | Index into the string table of a vehicle type name, such as `Horse`     |
| `+0x04` | u32  | package_index      | Index into the string table                                             |
| `+0x08` | u32  | package_hash       | Hash of the package path; never `0`                                     |

### Equip Vehicle List (variable: 4 bytes + vehicle rows)

| Offset  | Type                       | Field            | Notes                                                    |
| ------- | -------------------------- | ---------------- | -------------------------------------------------------- |
| `+0x00` | u32                        | vehicle_count    | `0` or `1` on client 3483                                |
| `+0x04` | Vehicle Row[vehicle_count] | vehicle_packages | Same row as the vehicle packages of the block            |

### Class Package Row (9 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u8   | class_type    | The class type of the block whose packages the path follows |
| `+0x01` | u32  | package_index | Index into the string table; unaligned                      |
| `+0x05` | u32  | package_hash  | Hash of the package path; unaligned                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `4,739` on client 3483      |
| `+0x04` | pstr[string_count] | strings      | `u8 is_wide`, `u32 byte_length`, then the text |

The string table has the shape `manufacture.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). Every string is narrow (`is_wide = 0`). The
package paths are lower case; the vehicle type names keep their case
(`FrigateShip`). Index `2` is the empty string on clients 1784 and 3483.

## Layout 18

87 class types and 119 equip types, with the class package list.

### File Layout

| Offset                        | Type                                           | Field                       | Notes                                 |
| ----------------------------- | ---------------------------------------------- | --------------------------- | ------------------------------------- |
| `+0x00`                       | char[4]                                        | magic                       | ASCII `PABR`                          |
| `+0x04`                       | Class Block[87]                                | classes                     | One block per class type, `0` to `86` |
| `classes+0x00`                | u32                                            | unknown_class_package_count |                                       |
| `classes+0x04`                | Class Package Row[unknown_class_package_count] | unknown_class_packages      |                                       |
| `unknown_class_packages+0x00` | String Table                                   | string_table                |                                       |
| `string_table+0x00`           | u32                                            | string_table_start          | Offset of `string_count`              |
| `string_table+0x04`           | u32                                            | zero                        | Always `0`                            |

## Layout 17

87 class types and 118 equip types, with the class package list.

### Class Block (variable: 956 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[118]          | weapon_packages         | One cell per equip type, `0` to `117` |
| `+0x3B0`                       | u32                        | vehicle_count           |                                       |
| `+0x3B4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[118]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 16

87 class types and 116 equip types, with the class package list.

### Class Block (variable: 940 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[116]          | weapon_packages         | One cell per equip type, `0` to `115` |
| `+0x3A0`                       | u32                        | vehicle_count           |                                       |
| `+0x3A4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[116]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 15

87 class types and 115 equip types, with the class package list.

### Class Block (variable: 932 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[115]          | weapon_packages         | One cell per equip type, `0` to `114` |
| `+0x398`                       | u32                        | vehicle_count           |                                       |
| `+0x39C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[115]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 14

87 class types and 114 equip types, with the class package list.

### Class Block (variable: 924 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[114]          | weapon_packages         | One cell per equip type, `0` to `113` |
| `+0x390`                       | u32                        | vehicle_count           |                                       |
| `+0x394`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[114]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 13

87 class types and 112 equip types, with the class package list.

### Class Block (variable: 908 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[112]          | weapon_packages         | One cell per equip type, `0` to `111` |
| `+0x380`                       | u32                        | vehicle_count           |                                       |
| `+0x384`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[112]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 12

87 class types and 111 equip types, with the class package list.

### Class Block (variable: 900 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[111]          | weapon_packages         | One cell per equip type, `0` to `110` |
| `+0x378`                       | u32                        | vehicle_count           |                                       |
| `+0x37C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[111]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 11

87 class types and 109 equip types, with the class package list.

### Class Block (variable: 884 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[109]          | weapon_packages         | One cell per equip type, `0` to `108` |
| `+0x368`                       | u32                        | vehicle_count           |                                       |
| `+0x36C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[109]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 10

87 class types and 108 equip types, with the class package list.

### Class Block (variable: 876 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[108]          | weapon_packages         | One cell per equip type, `0` to `107` |
| `+0x360`                       | u32                        | vehicle_count           |                                       |
| `+0x364`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[108]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 9

87 class types and 102 equip types, with the class package list.

### Class Block (variable: 828 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[102]          | weapon_packages         | One cell per equip type, `0` to `101` |
| `+0x330`                       | u32                        | vehicle_count           |                                       |
| `+0x334`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[102]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 8

82 class types and 101 equip types, with the class package list.

### File Layout

| Offset                        | Type                                           | Field                       | Notes                                 |
| ----------------------------- | ---------------------------------------------- | --------------------------- | ------------------------------------- |
| `+0x00`                       | char[4]                                        | magic                       | ASCII `PABR`                          |
| `+0x04`                       | Class Block[82]                                | classes                     | One block per class type, `0` to `81` |
| `classes+0x00`                | u32                                            | unknown_class_package_count |                                       |
| `classes+0x04`                | Class Package Row[unknown_class_package_count] | unknown_class_packages      |                                       |
| `unknown_class_packages+0x00` | String Table                                   | string_table                |                                       |
| `string_table+0x00`           | u32                                            | string_table_start          | Offset of `string_count`              |
| `string_table+0x04`           | u32                                            | zero                        | Always `0`                            |

### Class Block (variable: 820 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[101]          | weapon_packages         | One cell per equip type, `0` to `100` |
| `+0x328`                       | u32                        | vehicle_count           |                                       |
| `+0x32C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[101]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 7

82 class types and 100 equip types, with the class package list.

### Class Block (variable: 812 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[100]          | weapon_packages         | One cell per equip type, `0` to `99` |
| `+0x320`                       | u32                        | vehicle_count           |                                      |
| `+0x324`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[100]    | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 6

82 class types and 100 equip types, without the class package list.

### File Layout

| Offset              | Type            | Field              | Notes                                 |
| ------------------- | --------------- | ------------------ | ------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                          |
| `+0x04`             | Class Block[82] | classes            | One block per class type, `0` to `81` |
| `classes+0x00`      | String Table    | string_table       |                                       |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`              |
| `string_table+0x04` | u32             | zero               | Always `0`                            |

## Layout 5

82 class types and 98 equip types, without the class package list.

### Class Block (variable: 796 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[98]           | weapon_packages         | One cell per equip type, `0` to `97` |
| `+0x310`                       | u32                        | vehicle_count           |                                      |
| `+0x314`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[98]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 4

82 class types and 95 equip types, without the class package list.

### Class Block (variable: 772 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[95]           | weapon_packages         | One cell per equip type, `0` to `94` |
| `+0x2F8`                       | u32                        | vehicle_count           |                                      |
| `+0x2FC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[95]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 3

82 class types and 93 equip types, without the class package list.

### Class Block (variable: 756 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[93]           | weapon_packages         | One cell per equip type, `0` to `92` |
| `+0x2E8`                       | u32                        | vehicle_count           |                                      |
| `+0x2EC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[93]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 2

82 class types and 92 equip types, without the class package list.

### Class Block (variable: 748 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[92]           | weapon_packages         | One cell per equip type, `0` to `91` |
| `+0x2E0`                       | u32                        | vehicle_count           |                                      |
| `+0x2E4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[92]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 1

82 class types and 91 equip types, without the class package list.

### Class Block (variable: 740 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[91]           | weapon_packages         | One cell per equip type, `0` to `90` |
| `+0x2D8`                       | u32                        | vehicle_count           |                                      |
| `+0x2DC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[91]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Package Hash

`package_hash` is Bob Jenkins' lookup3 `hashlittle` of the path's ASCII
bytes with seed `0xC5EDE`, the hash `manufacture.bss` stores for its
action names (`ascii_key_hash` in `_common/string_hash.py`). It matches on
every non-empty cell and row of every client from 1743 to 3483. Empty cells
store `0`, not the hash of the empty string (`0xDEBA1DCD`). Vehicle type
names have no hash.

## Equip Types

The cell position in `weapon_packages` and the list position in
`vehicle_weapon_packages` is the item `equip_type` of
[`itemenchant.dbss`](itemenchant_dbss.md#equip_type): Longsword `1` holds
`pc/1_phm/fighteraction_onehandsword` for the Warrior, matchlock `53` the
`commonchart_huntrifle` packages. An older layout has the same types up to
its count. On client 3483, 45 of the 119 equip types hold a package for at
least one class.

The Enum column is `gc::ItemEquipType::Type` of the 2016 client's debug
symbols (`BlackDesert64.pdb`), which names `0` to `62` and ends with
`TypeCount = 63`. The sheet column is the `PcActionWeapon_Table` column of a
private server's `DataSheets.bexcel` on client 1784 whose cells match that
position in the client 1784 file, with the number of classes that match;
types `93` and up have no column there. Where both name a type they agree,
and the enum settles `Bow` (`4`) and `BowOneHanded` (`31`), which the sheet
cannot tell apart (see [Field Names](#field-names)). The browser's Equip
Type Name column shows the enum name, else the sheet column
(`equip_types.py`), else nothing.

| Equip type | Enum (2016)    | Sheet column (client 1784) | Classes (client 3483) | Example package (client 3483) |
| ---------- | -------------- | -------------------------- | --------------------- | ----------------------------- |
| 0   | `None`           | `None` (39)              | 47 | `pc/1_phm/fighteraction_noweapon` |
| 1   | `LongSword`      | `LongSword` (13)         | 2  | `pc/1_phm/fighteraction_onehandsword` |
| 2   | `ElBlade`        | `ElBlade` (3)            | 3  | `pc/5_pbw/tameraction_wavesword` |
| 3   | `Blade`          | `Blade` (3)              | 3  | `pc/6_pkm/blademasteraction_blade` |
| 4   | `Bow`            | `Bow`, `BowOneHanded` (1) | 1 | `pc/3_pew/elfaction_bow` |
| 6   | `Staff`          | `Staff` (3)              | 2  | `pc/8_pwmm/whitemageaction_weaponmain_m` |
| 28  | `EnchantArm`     | `EnchantArm` (1)         | 1  | `pc/2_phw/sorceressaction_enchantarm` |
| 29  | `DoubleAxe`      | `DoubleAxe` (1)          | 1  | `pc/4_pgm/giantaction_doubleaxe` |
| 31  | `BowOneHanded`   | `Bow`, `BowOneHanded` (1) | 1 | `pc/3_pew/elfaction_bow` |
| 43  | `Rifle`          | `Rifle` (25)             | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_rifle` |
| 44  | `FishingRod`     | `FishingRod` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingrod` |
| 45  | `Flute`          | `Flute` (25)             | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_flute` |
| 47  | `Cane`           | `Cane` (25)              | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_cane` |
| 48  | `FishingHarpoon` | `FishingHarpoon` (25)    | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingharpoon` |
| 49  | `FishingNet`     | `FishingNet` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_fishingnet` |
| 50  | `Drum`           | `Drum` (25)              | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_drum` |
| 53  | `HuntRifle`      | `HuntRifle` (25)         | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_huntrifle` |
| 60  | `Cymbals`        | `Cymbals` (25)           | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_cymbals` |
| 61  | `Guitar`         | `Guitar` (25)            | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_guitar` |
| 62  | `Trumpet`        | `Trumpet` (25)           | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_trumpet` |
| 63  |                  | `Kriegsmesser` (1)       | 1  | `pc/15_pdew/darkelfaction_blade` |
| 64  |                  | `SiegeRifle` (25)        | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_siegerifle` |
| 65  |                  | `Gauntlet` (2)           | 2  | `pc/16_pcm/combattantaction_gauntlet` |
| 67  |                  | `Sherry_Main` (1)        | 1  | `pc/17_psw/chineseaction_enchantarm` |
| 69  |                  | `SiegeAxe` (25)          | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_siegeaxe` |
| 71  |                  | `HandGrenade` (25)       | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_handgrenade` |
| 73  |                  | `CrossBow_Main` (1)      | 1  | `pc/9_pem/elfmanaction_crossbow` |
| 75  |                  | `WaterBomb` (25)         | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_waterbomb` |
| 77  |                  | `SniperRifle` (25)       | 44 | `pc/1_phm/common_weapon/fighteraction_commonchart_sniperrifle` |
| 78  |                  | `Boomerang` (1)          | 1  | `pc/14_plw/shytribeaction_weaponmain_w` |
| 80  |                  | `Scimitar` (1)           | 1  | `pc/18_pam/valenciafighteraction_weapon` |
| 82  |                  | `BroadSword` (1)         | 1  | `pc/19_prum/rutumaction_broadsword` |
| 83  |                  | `OneHandAxe` (1)         | 1  | `pc/11_pgw/giantwomenaction_onehandaxe` |
| 86  |                  | `Mace` (1)               | 1  | `pc/21_phwb/blackfighterwomenaction_mace` |
| 88  |                  | `PPM_Main` (1)           | 1  | `pc/23_ppm/ppmaction_weapon` |
| 89  |                  | `PFW_Main` (1)           | 1  | `pc/24_pfw/pfwaction_mainweapon` |
| 93  |                  |                          | 1  | `pc/25_pqw/pqwaction_weapon` |
| 95  |                  |                          | 1  | `pc/26_pbm/pbmaction_weapon` |
| 96  |                  |                          | 1  | `pc/27_pkow/pkowaction_weapon` |
| 97  |                  |                          | 6  | `pc/28_pmyf/pmyfaction_weapon` |
| 100 |                  |                          | 1  | `pc/29_pnyw/pnywaction_weapon` |
| 109 |                  |                          | 6  | `pc/31_prsa/prsaaction_weapon` |
| 112 |                  |                          | 2  | `pc/32_pwge/pwgeaction_weapon` |
| 114 |                  |                          | 1  | `pc/20_pjkd/pjkdaction_weapon` |
| 116 |                  |                          | 1  | `pc/30_pdkl/pdklaction_weapon` |

The only `vehicle_weapon_packages` entries on clients 1743 to 3483 are
`Horse` under equip type `53`, the `horsehuntrifle` package of each class
(34 classes on client 3483). The sheet's one `PcActionVehicleWithWeapon_Table`
row is `Horse` with `HuntRifle`.

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) declare
`gc::PcActionPackageNameManager` with the members
`_packageNameArray_Weapon[32][63]`, `_packageNameArray_Vehicle[32][37]` and
`_packageNameMap_VehicleWithWeapon[32]`, a map keyed by
`(gc::VehicleType, gc::ItemEquipType::Type)`, each next to a matching
`_packageHash*` member of `unsigned int`. The outer index is the class type,
the inner `63` of the weapon array is `gc::ItemEquipType::TypeCount`. The
live file stores each name and hash as one Package Cell; the vehicle array
became rows keyed by the vehicle type name, and the map one list per equip
type.

The `PcActionPackage_Table` workbook of a private server's
`DataSheets.bexcel` on client 1784 has the four sheets the dump of that
server (`Instance_dumpFull.exe`) loads with it: `PcActionWeapon_Table` (one
row per class type, one column per weapon), `PcActionVehicle_Table` (one
row per `VehicleTypeName`, one column per class type),
`PcActionVehicleWithWeapon_Table` (`VehicleTypeName`, `WeaponTypeName`, a
column per class type) and `CutScenePcAction_Table` (`classType`,
`cutSceneAction`). The private server's paths are edited, so the values
match in part only: on client 1784, 32 of the 32 `cutSceneAction` cells
and 3,208 of the 5,565 filled `PcActionVehicle_Table` cells match the file
by file name (26 of 32 and 2,137 of 5,809 on client 3483). Each weapon
column that matches lands on one equip type, listed under
[Equip Types](#equip-types), except `Bow` and `BowOneHanded`: class type
`4` holds the same `elfaction_bow` package at `4` and `31`, so both columns
match both.

`class_type` in Class Package Row is named by value: rows `6`, `15` and
`32` (client 3483) hold `pc/29_pnyw/`, `pc/27_pkow/` and `pc/30_pdkl/`
paths, the folders of class blocks `6`, `15` and `32`.

## Notes

- On client 3483, class blocks `47` to `96` are empty: every cell points at
  the empty string and every count is `0`. Blocks `36` to `46` hold 66
  vehicle rows each and repeat the packages of other classes
  (`pc/35_pyfm/` and `pc/36_pyfw/` alternate from block `37`). Block `14`
  also holds 66, block `16` 141, block `17` 137 and the other filled blocks
  140.
- Blocks `18` and `22` have no vehicle rows on client 3483; block `18`
  repeats the Tamer's `pc/5_pbw/` weapon packages.
- On client 1784 each of the 82 blocks holds at least one weapon package;
  33 of them have no vehicle rows.
- Clients 1109 to 1737 have no `cutscene_package` cell at the end of a class
  block; their blocks otherwise walk as Layout 1 with 84 to 91 equip types,
  and clients 1109 to 1164 hold 32 class blocks, the outer count of the 2016
  arrays. No layout here reads them yet.

## Open Questions

### What the Class Package List Is For

`unknown_class_packages` holds paths named `*action_weapon_copy`, one per
class, and no class block cell or row points at them. The list first
appears on client 2107 with no rows (clients 2059 to 2098 end their class
blocks at `string_table_start`). Each class got its row some patches after
its `*action_weapon` package first appeared in the string table:

| Class type | Package                              | `*action_weapon` from client | Row from client |
| ---------- | ------------------------------------ | ---------------------------- | --------------- |
| 15         | `pc/27_pkow/pkowaction_weapon_copy`  | 1996                         | 2122            |
| 6          | `pc/29_pnyw/pnywaction_weapon_copy`  | 2313                         | 2335            |
| 32         | `pc/30_pdkl/pdklaction_weapon_copy`  | 2872                         | 3118            |

No 1784 sheet holds the names, the client 3483 PAZ index has no file whose
name holds `weapon_copy`, and which weapon state loads the copy package is
not in the file.

### Where the Packages Without a File Live

Of the 4,594 `pc/` paths in the string table (client 3483), 33 are
`.paac` files under `character/binaryactionchart/`, all of them equip type
`0` packages. The other 34th file there,
`character/binaryactionchart/pc/pc_actionchartpackagepcraw.paac`
(131 MB), is not named here and may hold the weapon, vehicle and cutscene
packages; that needs a `.paac` doc first.
