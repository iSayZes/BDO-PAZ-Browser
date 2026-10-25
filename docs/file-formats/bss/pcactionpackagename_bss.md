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
other packages have no file of their own. From client 1109 the file is a
plain PABR table with no row count: one block per class type, in class type
order, then (from client 2107) a short list keyed by class type, then the
PABR string table that holds every path and vehicle type name. Clients 435
to 829 store one array per section instead, then the same arrays of hashes;
see [Block Counts](#block-counts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes   | Records                                                                                                | Row bytes              |
| ------ | -------------- | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------ | ---------------------- |
| 39     | 3381 and later | `pcactionpackagename.bss` | 548,981 | 11,640 Package Cell, 5,444 Vehicle Row, 11,543 Equip Vehicle List, 97 Class Block, 3 Class Package Row | 8                      |
| 38     | 3177 to 3373   | `pcactionpackagename.bss` | 510,912 | 10,440 Package Cell, 4,579 Vehicle Row, 10,353 Equip Vehicle List, 87 Class Block, 3 Class Package Row | 8                      |
| 37     | 3012 to 3169   | `pcactionpackagename.bss` | 509,578 | 10,353 Package Cell, 4,645 Vehicle Row, 10,266 Equip Vehicle List, 87 Class Block, 3 Class Package Row | 8                      |
| 36     | 2825 to 3002   | `pcactionpackagename.bss` | 507,443 | 10,179 Package Cell, 4,645 Vehicle Row, 10,092 Equip Vehicle List, 87 Class Block, 2 Class Package Row | 8                      |
| 35     | 2794 to 2819   | `pcactionpackagename.bss` | 554,293 | 10,092 Package Cell, 5,474 Vehicle Row, 10,005 Equip Vehicle List, 87 Class Block, 2 Class Package Row | 8                      |
| 34     | 2644 to 2783   | `pcactionpackagename.bss` | 542,694 | 10,005 Package Cell, 5,474 Vehicle Row, 9,918 Equip Vehicle List, 87 Class Block, 2 Class Package Row  | 8                      |
| 33     | 2601 to 2637   | `pcactionpackagename.bss` | 522,022 | 9,831 Package Cell, 5,297 Vehicle Row, 9,744 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8                      |
| 32     | 2429 to 2592   | `pcactionpackagename.bss` | 520,978 | 9,744 Package Cell, 5,297 Vehicle Row, 9,657 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8                      |
| 31     | 2393 to 2421   | `pcactionpackagename.bss` | 507,606 | 9,570 Package Cell, 5,225 Vehicle Row, 9,483 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8                      |
| 30     | 2302 to 2384   | `pcactionpackagename.bss` | 506,562 | 9,483 Package Cell, 5,225 Vehicle Row, 9,396 Equip Vehicle List, 87 Class Block, 2 Class Package Row   | 8                      |
| 29     | 2250 to 2295   | `pcactionpackagename.bss` | 497,777 | 8,961 Package Cell, 5,190 Vehicle Row, 8,874 Equip Vehicle List, 87 Class Block                        | 8                      |
| 28     | 2207 to 2243   | `pcactionpackagename.bss` | 506,186 | 8,364 Package Cell, 7,932 Vehicle Row, 8,282 Equip Vehicle List, 82 Class Block                        | 8                      |
| 27     | 2107 to 2203   | `pcactionpackagename.bss` | 502,161 | 8,282 Package Cell, 7,828 Vehicle Row, 8,200 Equip Vehicle List, 82 Class Block                        | 8                      |
| 26     | 2059 to 2098   | `pcactionpackagename.bss` | 492,651 | 8,282 Package Cell, 7,827 Vehicle Row, 8,200 Equip Vehicle List, 82 Class Block                        | 8                      |
| 25     | 1991 to 2052   | `pcactionpackagename.bss` | 490,625 | 8,118 Package Cell, 7,827 Vehicle Row, 8,036 Equip Vehicle List, 82 Class Block                        | 8                      |
| 24     | 1794 to 1985   | `pcactionpackagename.bss` | 450,061 | 7,872 Package Cell, 7,335 Vehicle Row, 7,790 Equip Vehicle List, 82 Class Block                        | 8                      |
| 23     | 1790           | `pcactionpackagename.bss` | 366,086 | 7,708 Package Cell, 5,887 Vehicle Row, 7,626 Equip Vehicle List, 82 Class Block                        | 8                      |
| 22     | 1774 to 1784   | `pcactionpackagename.bss` | 362,622 | 7,626 Package Cell, 5,839 Vehicle Row, 7,544 Equip Vehicle List, 82 Class Block                        | 8                      |
| 21     | 1743 to 1771   | `pcactionpackagename.bss` | 362,128 | 7,544 Package Cell, 5,884 Vehicle Row, 7,462 Equip Vehicle List, 82 Class Block                        | 8                      |
| 20     | 1608 to 1737   | `pcactionpackagename.bss` | 360,465 | 7,462 Package Cell, 5,884 Vehicle Row, 7,462 Equip Vehicle List, 82 Class Block                        | 8                      |
| 19     | 1565 to 1602   | `pcactionpackagename.bss` | 320,158 | 7,380 Package Cell, 5,143 Vehicle Row, 7,380 Equip Vehicle List, 82 Class Block                        | 8                      |
| 18     | 1500 to 1559   | `pcactionpackagename.bss` | 312,615 | 7,298 Package Cell, 5,042 Vehicle Row, 7,298 Equip Vehicle List, 82 Class Block                        | 8                      |
| 17     | 1358 to 1493   | `pcactionpackagename.bss` | 303,461 | 7,216 Package Cell, 4,931 Vehicle Row, 7,216 Equip Vehicle List, 82 Class Block                        | 8                      |
| 16     | 1167 to 1355   | `pcactionpackagename.bss` | 256,508 | 6,888 Package Cell, 4,152 Vehicle Row, 6,888 Equip Vehicle List, 82 Class Block                        | 8                      |
| 15     | 1109 to 1164   | `pcactionpackagename.bss` | 145,223 | 2,688 Package Cell, 2,201 Vehicle Row, 2,688 Equip Vehicle List, 32 Class Block                        | 8                      |
| 14     | 822 to 829     | `pcactionpackagename.bss` | 88,551  | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 10, 9 on average  |
| 13     | 814            | `pcactionpackagename.bss` | 87,335  | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 10, 9 on average  |
| 12     | 805            | `pcactionpackagename.bss` | 87,079  | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 10, 9 on average  |
| 11     | 771 to 794     | `pcactionpackagename.bss` | 140,683 | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 62 on average |
| 10     | 707 to 760     | `pcactionpackagename.bss` | 137,785 | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 62 on average |
| 9      | 643 to 697     | `pcactionpackagename.bss` | 135,939 | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 62 on average |
| 8      | 637            | `pcactionpackagename.bss` | 133,930 | 28 Vehicle Weapon Row, 32 Vehicle Weapon Map, 28 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 62 on average |
| 7      | 592 to 630     | `pcactionpackagename.bss` | 130,265 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 6      | 531 to 586     | `pcactionpackagename.bss` | 129,881 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 5      | 508 to 526     | `pcactionpackagename.bss` | 128,089 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 4      | 504            | `pcactionpackagename.bss` | 126,505 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 3      | 485 to 497     | `pcactionpackagename.bss` | 123,343 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 2      | 472 to 478     | `pcactionpackagename.bss` | 121,574 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |
| 1      | 435 to 466     | `pcactionpackagename.bss` | 116,021 | 27 Vehicle Weapon Row, 32 Vehicle Weapon Map, 27 Vehicle Weapon Hash Row, 32 Vehicle Weapon Hash Map   | 4 to 78, 60 on average |

| Layout | File                      | Known              | Unknown    |
| ------ | ------------------------- | ------------------ | ---------- |
| 39     | `pcactionpackagename.bss` | 548,977 B (100.0%) | 4 B (0.0%) |
| 38     | `pcactionpackagename.bss` | 510,908 B (100.0%) | 4 B (0.0%) |
| 37     | `pcactionpackagename.bss` | 509,574 B (100.0%) | 4 B (0.0%) |
| 36     | `pcactionpackagename.bss` | 507,439 B (100.0%) | 4 B (0.0%) |
| 35     | `pcactionpackagename.bss` | 554,289 B (100.0%) | 4 B (0.0%) |
| 34     | `pcactionpackagename.bss` | 542,690 B (100.0%) | 4 B (0.0%) |
| 33     | `pcactionpackagename.bss` | 522,018 B (100.0%) | 4 B (0.0%) |
| 32     | `pcactionpackagename.bss` | 520,974 B (100.0%) | 4 B (0.0%) |
| 31     | `pcactionpackagename.bss` | 507,602 B (100.0%) | 4 B (0.0%) |
| 30     | `pcactionpackagename.bss` | 506,558 B (100.0%) | 4 B (0.0%) |
| 29     | `pcactionpackagename.bss` | 497,773 B (100.0%) | 4 B (0.0%) |
| 28     | `pcactionpackagename.bss` | 506,182 B (100.0%) | 4 B (0.0%) |
| 27     | `pcactionpackagename.bss` | 502,157 B (100.0%) | 4 B (0.0%) |
| 26     | `pcactionpackagename.bss` | 492,651 B (100.0%) | 0 B (0.0%) |
| 25     | `pcactionpackagename.bss` | 490,625 B (100.0%) | 0 B (0.0%) |
| 24     | `pcactionpackagename.bss` | 450,061 B (100.0%) | 0 B (0.0%) |
| 23     | `pcactionpackagename.bss` | 366,086 B (100.0%) | 0 B (0.0%) |
| 22     | `pcactionpackagename.bss` | 362,622 B (100.0%) | 0 B (0.0%) |
| 21     | `pcactionpackagename.bss` | 362,128 B (100.0%) | 0 B (0.0%) |
| 20     | `pcactionpackagename.bss` | 360,465 B (100.0%) | 0 B (0.0%) |
| 19     | `pcactionpackagename.bss` | 320,158 B (100.0%) | 0 B (0.0%) |
| 18     | `pcactionpackagename.bss` | 312,615 B (100.0%) | 0 B (0.0%) |
| 17     | `pcactionpackagename.bss` | 303,461 B (100.0%) | 0 B (0.0%) |
| 16     | `pcactionpackagename.bss` | 256,508 B (100.0%) | 0 B (0.0%) |
| 15     | `pcactionpackagename.bss` | 145,223 B (100.0%) | 0 B (0.0%) |
| 14     | `pcactionpackagename.bss` | 88,551 B (100.0%)  | 0 B (0.0%) |
| 13     | `pcactionpackagename.bss` | 87,335 B (100.0%)  | 0 B (0.0%) |
| 12     | `pcactionpackagename.bss` | 87,079 B (100.0%)  | 0 B (0.0%) |
| 11     | `pcactionpackagename.bss` | 140,683 B (100.0%) | 0 B (0.0%) |
| 10     | `pcactionpackagename.bss` | 137,785 B (100.0%) | 0 B (0.0%) |
| 9      | `pcactionpackagename.bss` | 135,939 B (100.0%) | 0 B (0.0%) |
| 8      | `pcactionpackagename.bss` | 133,930 B (100.0%) | 0 B (0.0%) |
| 7      | `pcactionpackagename.bss` | 130,265 B (100.0%) | 0 B (0.0%) |
| 6      | `pcactionpackagename.bss` | 129,881 B (100.0%) | 0 B (0.0%) |
| 5      | `pcactionpackagename.bss` | 128,089 B (100.0%) | 0 B (0.0%) |
| 4      | `pcactionpackagename.bss` | 126,505 B (100.0%) | 0 B (0.0%) |
| 3      | `pcactionpackagename.bss` | 123,343 B (100.0%) | 0 B (0.0%) |
| 2      | `pcactionpackagename.bss` | 121,574 B (100.0%) | 0 B (0.0%) |
| 1      | `pcactionpackagename.bss` | 116,021 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result    | Checked against |
| ------ | --------- | --------------- |
| 3483   | Layout 39 | `9ad54715ef01`  |
| 3482   | Layout 39 | `9ad54715ef01`  |
| 3474   | Layout 39 | `9ad54715ef01`  |
| 3473   | Layout 39 | `9ad54715ef01`  |
| 3464   | Layout 39 | `9ad54715ef01`  |
| 3458   | Layout 39 | `9ad54715ef01`  |
| 3454   | Layout 39 | `9ad54715ef01`  |
| 3444   | Layout 39 | `9ad54715ef01`  |
| 3435   | Layout 39 | `9ad54715ef01`  |
| 3426   | Layout 39 | `9ad54715ef01`  |
| 3418   | Layout 39 | `9ad54715ef01`  |
| 3412   | Layout 39 | `9ad54715ef01`  |
| 3402   | Layout 39 | `9ad54715ef01`  |
| 3396   | Layout 39 | `9ad54715ef01`  |
| 3387   | Layout 39 | `9ad54715ef01`  |
| 3381   | Layout 39 | `9ad54715ef01`  |
| 3373   | Layout 38 | `9ad54715ef01`  |
| 3364   | Layout 38 | `9ad54715ef01`  |
| 3356   | Layout 38 | `9ad54715ef01`  |
| 3349   | Layout 38 | `9ad54715ef01`  |
| 3342   | Layout 38 | `9ad54715ef01`  |
| 3335   | Layout 38 | `9ad54715ef01`  |
| 3326   | Layout 38 | `9ad54715ef01`  |
| 3321   | Layout 38 | `9ad54715ef01`  |
| 3314   | Layout 38 | `9ad54715ef01`  |
| 3303   | Layout 38 | `9ad54715ef01`  |
| 3302   | Layout 38 | `9ad54715ef01`  |
| 3293   | Layout 38 | `9ad54715ef01`  |
| 3283   | Layout 38 | `9ad54715ef01`  |
| 3275   | Layout 38 | `9ad54715ef01`  |
| 3267   | Layout 38 | `9ad54715ef01`  |
| 3258   | Layout 38 | `9ad54715ef01`  |
| 3251   | Layout 38 | `9ad54715ef01`  |
| 3242   | Layout 38 | `9ad54715ef01`  |
| 3235   | Layout 38 | `9ad54715ef01`  |
| 3229   | Layout 38 | `9ad54715ef01`  |
| 3212   | Layout 38 | `9ad54715ef01`  |
| 3203   | Layout 38 | `9ad54715ef01`  |
| 3193   | Layout 38 | `9ad54715ef01`  |
| 3186   | Layout 38 | `9ad54715ef01`  |
| 3177   | Layout 38 | `9ad54715ef01`  |
| 3169   | Layout 37 | `9ad54715ef01`  |
| 3158   | Layout 37 | `9ad54715ef01`  |
| 3151   | Layout 37 | `9ad54715ef01`  |
| 3144   | Layout 37 | `9ad54715ef01`  |
| 3133   | Layout 37 | `9ad54715ef01`  |
| 3125   | Layout 37 | `9ad54715ef01`  |
| 3118   | Layout 37 | `9ad54715ef01`  |
| 3111   | Layout 37 | `9ad54715ef01`  |
| 3103   | Layout 37 | `9ad54715ef01`  |
| 3095   | Layout 37 | `9ad54715ef01`  |
| 3086   | Layout 37 | `9ad54715ef01`  |
| 3072   | Layout 37 | `9ad54715ef01`  |
| 3062   | Layout 37 | `9ad54715ef01`  |
| 3052   | Layout 37 | `9ad54715ef01`  |
| 3045   | Layout 37 | `9ad54715ef01`  |
| 3037   | Layout 37 | `9ad54715ef01`  |
| 3030   | Layout 37 | `9ad54715ef01`  |
| 3021   | Layout 37 | `9ad54715ef01`  |
| 3012   | Layout 37 | `9ad54715ef01`  |
| 3002   | Layout 36 | `9ad54715ef01`  |
| 2995   | Layout 36 | `9ad54715ef01`  |
| 2987   | Layout 36 | `9ad54715ef01`  |
| 2978   | Layout 36 | `9ad54715ef01`  |
| 2970   | Layout 36 | `9ad54715ef01`  |
| 2959   | Layout 36 | `9ad54715ef01`  |
| 2951   | Layout 36 | `9ad54715ef01`  |
| 2942   | Layout 36 | `9ad54715ef01`  |
| 2935   | Layout 36 | `9ad54715ef01`  |
| 2932   | Layout 36 | `9ad54715ef01`  |
| 2923   | Layout 36 | `9ad54715ef01`  |
| 2919   | Layout 36 | `9ad54715ef01`  |
| 2907   | Layout 36 | `9ad54715ef01`  |
| 2900   | Layout 36 | `9ad54715ef01`  |
| 2891   | Layout 36 | `9ad54715ef01`  |
| 2882   | Layout 36 | `9ad54715ef01`  |
| 2872   | Layout 36 | `9ad54715ef01`  |
| 2863   | Layout 36 | `9ad54715ef01`  |
| 2855   | Layout 36 | `9ad54715ef01`  |
| 2849   | Layout 36 | `9ad54715ef01`  |
| 2844   | Layout 36 | `9ad54715ef01`  |
| 2834   | Layout 36 | `9ad54715ef01`  |
| 2825   | Layout 36 | `9ad54715ef01`  |
| 2819   | Layout 35 | `9ad54715ef01`  |
| 2811   | Layout 35 | `9ad54715ef01`  |
| 2803   | Layout 35 | `9ad54715ef01`  |
| 2794   | Layout 35 | `9ad54715ef01`  |
| 2783   | Layout 34 | `9ad54715ef01`  |
| 2774   | Layout 34 | `9ad54715ef01`  |
| 2765   | Layout 34 | `9ad54715ef01`  |
| 2756   | Layout 34 | `9ad54715ef01`  |
| 2750   | Layout 34 | `9ad54715ef01`  |
| 2743   | Layout 34 | `9ad54715ef01`  |
| 2736   | Layout 34 | `9ad54715ef01`  |
| 2726   | Layout 34 | `9ad54715ef01`  |
| 2717   | Layout 34 | `9ad54715ef01`  |
| 2709   | Layout 34 | `9ad54715ef01`  |
| 2703   | Layout 34 | `9ad54715ef01`  |
| 2695   | Layout 34 | `9ad54715ef01`  |
| 2684   | Layout 34 | `9ad54715ef01`  |
| 2672   | Layout 34 | `9ad54715ef01`  |
| 2665   | Layout 34 | `9ad54715ef01`  |
| 2657   | Layout 34 | `9ad54715ef01`  |
| 2649   | Layout 34 | `9ad54715ef01`  |
| 2644   | Layout 34 | `9ad54715ef01`  |
| 2637   | Layout 33 | `9ad54715ef01`  |
| 2629   | Layout 33 | `9ad54715ef01`  |
| 2619   | Layout 33 | `9ad54715ef01`  |
| 2612   | Layout 33 | `9ad54715ef01`  |
| 2606   | Layout 33 | `9ad54715ef01`  |
| 2602   | Layout 33 | `9ad54715ef01`  |
| 2601   | Layout 33 | `9ad54715ef01`  |
| 2592   | Layout 32 | `9ad54715ef01`  |
| 2583   | Layout 32 | `9ad54715ef01`  |
| 2575   | Layout 32 | `9ad54715ef01`  |
| 2567   | Layout 32 | `9ad54715ef01`  |
| 2560   | Layout 32 | `9ad54715ef01`  |
| 2553   | Layout 32 | `9ad54715ef01`  |
| 2545   | Layout 32 | `9ad54715ef01`  |
| 2538   | Layout 32 | `9ad54715ef01`  |
| 2529   | Layout 32 | `9ad54715ef01`  |
| 2519   | Layout 32 | `9ad54715ef01`  |
| 2513   | Layout 32 | `9ad54715ef01`  |
| 2510   | Layout 32 | `9ad54715ef01`  |
| 2507   | Layout 32 | `9ad54715ef01`  |
| 2503   | Layout 32 | `9ad54715ef01`  |
| 2498   | Layout 32 | `9ad54715ef01`  |
| 2492   | Layout 32 | `9ad54715ef01`  |
| 2487   | Layout 32 | `9ad54715ef01`  |
| 2480   | Layout 32 | `9ad54715ef01`  |
| 2474   | Layout 32 | `9ad54715ef01`  |
| 2468   | Layout 32 | `9ad54715ef01`  |
| 2460   | Layout 32 | `9ad54715ef01`  |
| 2453   | Layout 32 | `9ad54715ef01`  |
| 2444   | Layout 32 | `9ad54715ef01`  |
| 2438   | Layout 32 | `9ad54715ef01`  |
| 2434   | Layout 32 | `9ad54715ef01`  |
| 2429   | Layout 32 | `9ad54715ef01`  |
| 2421   | Layout 31 | `9ad54715ef01`  |
| 2414   | Layout 31 | `9ad54715ef01`  |
| 2407   | Layout 31 | `9ad54715ef01`  |
| 2401   | Layout 31 | `9ad54715ef01`  |
| 2397   | Layout 31 | `9ad54715ef01`  |
| 2393   | Layout 31 | `9ad54715ef01`  |
| 2384   | Layout 30 | `9ad54715ef01`  |
| 2378   | Layout 30 | `9ad54715ef01`  |
| 2372   | Layout 30 | `9ad54715ef01`  |
| 2358   | Layout 30 | `9ad54715ef01`  |
| 2352   | Layout 30 | `9ad54715ef01`  |
| 2347   | Layout 30 | `9ad54715ef01`  |
| 2343   | Layout 30 | `9ad54715ef01`  |
| 2335   | Layout 30 | `9ad54715ef01`  |
| 2327   | Layout 30 | `9ad54715ef01`  |
| 2324   | Layout 30 | `9ad54715ef01`  |
| 2319   | Layout 30 | `9ad54715ef01`  |
| 2313   | Layout 30 | `9ad54715ef01`  |
| 2308   | Layout 30 | `9ad54715ef01`  |
| 2302   | Layout 30 | `9ad54715ef01`  |
| 2295   | Layout 29 | `9ad54715ef01`  |
| 2290   | Layout 29 | `9ad54715ef01`  |
| 2284   | Layout 29 | `9ad54715ef01`  |
| 2276   | Layout 29 | `9ad54715ef01`  |
| 2269   | Layout 29 | `9ad54715ef01`  |
| 2259   | Layout 29 | `9ad54715ef01`  |
| 2250   | Layout 29 | `9ad54715ef01`  |
| 2243   | Layout 28 | `9ad54715ef01`  |
| 2235   | Layout 28 | `9ad54715ef01`  |
| 2229   | Layout 28 | `9ad54715ef01`  |
| 2224   | Layout 28 | `9ad54715ef01`  |
| 2218   | Layout 28 | `9ad54715ef01`  |
| 2215   | Layout 28 | `9ad54715ef01`  |
| 2207   | Layout 28 | `9ad54715ef01`  |
| 2203   | Layout 27 | `9ad54715ef01`  |
| 2196   | Layout 27 | `9ad54715ef01`  |
| 2192   | Layout 27 | `9ad54715ef01`  |
| 2189   | Layout 27 | `9ad54715ef01`  |
| 2183   | Layout 27 | `9ad54715ef01`  |
| 2179   | Layout 27 | `9ad54715ef01`  |
| 2171   | Layout 27 | `9ad54715ef01`  |
| 2163   | Layout 27 | `9ad54715ef01`  |
| 2156   | Layout 27 | `9ad54715ef01`  |
| 2151   | Layout 27 | `9ad54715ef01`  |
| 2147   | Layout 27 | `9ad54715ef01`  |
| 2142   | Layout 27 | `9ad54715ef01`  |
| 2138   | Layout 27 | `9ad54715ef01`  |
| 2134   | Layout 27 | `9ad54715ef01`  |
| 2130   | Layout 27 | `9ad54715ef01`  |
| 2122   | Layout 27 | `9ad54715ef01`  |
| 2107   | Layout 27 | `9ad54715ef01`  |
| 2098   | Layout 26 | `9ad54715ef01`  |
| 2089   | Layout 26 | `9ad54715ef01`  |
| 2081   | Layout 26 | `9ad54715ef01`  |
| 2073   | Layout 26 | `9ad54715ef01`  |
| 2067   | Layout 26 | `9ad54715ef01`  |
| 2063   | Layout 26 | `9ad54715ef01`  |
| 2059   | Layout 26 | `9ad54715ef01`  |
| 2052   | Layout 25 | `9ad54715ef01`  |
| 2044   | Layout 25 | `9ad54715ef01`  |
| 2039   | Layout 25 | `9ad54715ef01`  |
| 2032   | Layout 25 | `9ad54715ef01`  |
| 2025   | Layout 25 | `9ad54715ef01`  |
| 2011   | Layout 25 | `9ad54715ef01`  |
| 2005   | Layout 25 | `9ad54715ef01`  |
| 2000   | Layout 25 | `9ad54715ef01`  |
| 1996   | Layout 25 | `9ad54715ef01`  |
| 1991   | Layout 25 | `9ad54715ef01`  |
| 1985   | Layout 24 | `9ad54715ef01`  |
| 1980   | Layout 24 | `9ad54715ef01`  |
| 1969   | Layout 24 | `9ad54715ef01`  |
| 1964   | Layout 24 | `9ad54715ef01`  |
| 1958   | Layout 24 | `9ad54715ef01`  |
| 1950   | Layout 24 | `9ad54715ef01`  |
| 1945   | Layout 24 | `9ad54715ef01`  |
| 1937   | Layout 24 | `9ad54715ef01`  |
| 1933   | Layout 24 | `9ad54715ef01`  |
| 1927   | Layout 24 | `9ad54715ef01`  |
| 1921   | Layout 24 | `9ad54715ef01`  |
| 1914   | Layout 24 | `9ad54715ef01`  |
| 1908   | Layout 24 | `9ad54715ef01`  |
| 1897   | Layout 24 | `9ad54715ef01`  |
| 1892   | Layout 24 | `9ad54715ef01`  |
| 1886   | Layout 24 | `9ad54715ef01`  |
| 1881   | Layout 24 | `9ad54715ef01`  |
| 1871   | Layout 24 | `9ad54715ef01`  |
| 1866   | Layout 24 | `9ad54715ef01`  |
| 1862   | Layout 24 | `9ad54715ef01`  |
| 1854   | Layout 24 | `9ad54715ef01`  |
| 1846   | Layout 24 | `9ad54715ef01`  |
| 1838   | Layout 24 | `9ad54715ef01`  |
| 1832   | Layout 24 | `9ad54715ef01`  |
| 1826   | Layout 24 | `9ad54715ef01`  |
| 1822   | Layout 24 | `9ad54715ef01`  |
| 1818   | Layout 24 | `9ad54715ef01`  |
| 1804   | Layout 24 | `9ad54715ef01`  |
| 1794   | Layout 24 | `9ad54715ef01`  |
| 1790   | Layout 23 | `9ad54715ef01`  |
| 1784   | Layout 22 | `9ad54715ef01`  |
| 1774   | Layout 22 | `9ad54715ef01`  |
| 1771   | Layout 21 | `9ad54715ef01`  |
| 1762   | Layout 21 | `9ad54715ef01`  |
| 1759   | Layout 21 | `9ad54715ef01`  |
| 1754   | Layout 21 | `9ad54715ef01`  |
| 1749   | Layout 21 | `9ad54715ef01`  |
| 1743   | Layout 21 | `9ad54715ef01`  |
| 1737   | Layout 20 | `9ad54715ef01`  |
| 1731   | Layout 20 | `9ad54715ef01`  |
| 1725   | Layout 20 | `9ad54715ef01`  |
| 1717   | Layout 20 | `9ad54715ef01`  |
| 1710   | Layout 20 | `9ad54715ef01`  |
| 1704   | Layout 20 | `9ad54715ef01`  |
| 1698   | Layout 20 | `9ad54715ef01`  |
| 1690   | Layout 20 | `9ad54715ef01`  |
| 1685   | Layout 20 | `9ad54715ef01`  |
| 1680   | Layout 20 | `9ad54715ef01`  |
| 1674   | Layout 20 | `9ad54715ef01`  |
| 1668   | Layout 20 | `9ad54715ef01`  |
| 1659   | Layout 20 | `9ad54715ef01`  |
| 1649   | Layout 20 | `9ad54715ef01`  |
| 1642   | Layout 20 | `9ad54715ef01`  |
| 1636   | Layout 20 | `9ad54715ef01`  |
| 1628   | Layout 20 | `9ad54715ef01`  |
| 1622   | Layout 20 | `9ad54715ef01`  |
| 1614   | Layout 20 | `9ad54715ef01`  |
| 1608   | Layout 20 | `9ad54715ef01`  |
| 1602   | Layout 19 | `9ad54715ef01`  |
| 1598   | Layout 19 | `9ad54715ef01`  |
| 1594   | Layout 19 | `9ad54715ef01`  |
| 1590   | Layout 19 | `9ad54715ef01`  |
| 1587   | Layout 19 | `9ad54715ef01`  |
| 1584   | Layout 19 | `9ad54715ef01`  |
| 1579   | Layout 19 | `9ad54715ef01`  |
| 1572   | Layout 19 | `9ad54715ef01`  |
| 1565   | Layout 19 | `9ad54715ef01`  |
| 1559   | Layout 18 | `9ad54715ef01`  |
| 1554   | Layout 18 | `9ad54715ef01`  |
| 1547   | Layout 18 | `9ad54715ef01`  |
| 1537   | Layout 18 | `9ad54715ef01`  |
| 1529   | Layout 18 | `9ad54715ef01`  |
| 1524   | Layout 18 | `9ad54715ef01`  |
| 1519   | Layout 18 | `9ad54715ef01`  |
| 1509   | Layout 18 | `9ad54715ef01`  |
| 1506   | Layout 18 | `9ad54715ef01`  |
| 1504   | Layout 18 | `9ad54715ef01`  |
| 1500   | Layout 18 | `9ad54715ef01`  |
| 1493   | Layout 17 | `9ad54715ef01`  |
| 1489   | Layout 17 | `9ad54715ef01`  |
| 1485   | Layout 17 | `9ad54715ef01`  |
| 1481   | Layout 17 | `9ad54715ef01`  |
| 1474   | Layout 17 | `9ad54715ef01`  |
| 1466   | Layout 17 | `9ad54715ef01`  |
| 1462   | Layout 17 | `9ad54715ef01`  |
| 1459   | Layout 17 | `9ad54715ef01`  |
| 1453   | Layout 17 | `9ad54715ef01`  |
| 1450   | Layout 17 | `9ad54715ef01`  |
| 1445   | Layout 17 | `9ad54715ef01`  |
| 1439   | Layout 17 | `9ad54715ef01`  |
| 1433   | Layout 17 | `9ad54715ef01`  |
| 1430   | Layout 17 | `9ad54715ef01`  |
| 1426   | Layout 17 | `9ad54715ef01`  |
| 1421   | Layout 17 | `9ad54715ef01`  |
| 1417   | Layout 17 | `9ad54715ef01`  |
| 1416   | Layout 17 | `9ad54715ef01`  |
| 1409   | Layout 17 | `9ad54715ef01`  |
| 1405   | Layout 17 | `9ad54715ef01`  |
| 1401   | Layout 17 | `9ad54715ef01`  |
| 1396   | Layout 17 | `9ad54715ef01`  |
| 1391   | Layout 17 | `9ad54715ef01`  |
| 1390   | Layout 17 | `9ad54715ef01`  |
| 1386   | Layout 17 | `9ad54715ef01`  |
| 1381   | Layout 17 | `9ad54715ef01`  |
| 1379   | Layout 17 | `9ad54715ef01`  |
| 1372   | Layout 17 | `9ad54715ef01`  |
| 1366   | Layout 17 | `9ad54715ef01`  |
| 1364   | Layout 17 | `9ad54715ef01`  |
| 1363   | Layout 17 | `9ad54715ef01`  |
| 1360   | Layout 17 | `9ad54715ef01`  |
| 1358   | Layout 17 | `9ad54715ef01`  |
| 1355   | Layout 16 | `9ad54715ef01`  |
| 1351   | Layout 16 | `9ad54715ef01`  |
| 1348   | Layout 16 | `9ad54715ef01`  |
| 1346   | Layout 16 | `9ad54715ef01`  |
| 1341   | Layout 16 | `9ad54715ef01`  |
| 1340   | Layout 16 | `9ad54715ef01`  |
| 1338   | Layout 16 | `9ad54715ef01`  |
| 1335   | Layout 16 | `9ad54715ef01`  |
| 1333   | Layout 16 | `9ad54715ef01`  |
| 1329   | Layout 16 | `9ad54715ef01`  |
| 1327   | Layout 16 | `9ad54715ef01`  |
| 1324   | Layout 16 | `9ad54715ef01`  |
| 1321   | Layout 16 | `9ad54715ef01`  |
| 1319   | Layout 16 | `9ad54715ef01`  |
| 1318   | Layout 16 | `9ad54715ef01`  |
| 1316   | Layout 16 | `9ad54715ef01`  |
| 1313   | Layout 16 | `9ad54715ef01`  |
| 1311   | Layout 16 | `9ad54715ef01`  |
| 1309   | Layout 16 | `9ad54715ef01`  |
| 1304   | Layout 16 | `9ad54715ef01`  |
| 1292   | Layout 16 | `9ad54715ef01`  |
| 1286   | Layout 16 | `9ad54715ef01`  |
| 1280   | Layout 16 | `9ad54715ef01`  |
| 1276   | Layout 16 | `9ad54715ef01`  |
| 1267   | Layout 16 | `9ad54715ef01`  |
| 1261   | Layout 16 | `9ad54715ef01`  |
| 1256   | Layout 16 | `9ad54715ef01`  |
| 1250   | Layout 16 | `9ad54715ef01`  |
| 1246   | Layout 16 | `9ad54715ef01`  |
| 1239   | Layout 16 | `9ad54715ef01`  |
| 1230   | Layout 16 | `9ad54715ef01`  |
| 1226   | Layout 16 | `9ad54715ef01`  |
| 1220   | Layout 16 | `9ad54715ef01`  |
| 1217   | Layout 16 | `9ad54715ef01`  |
| 1211   | Layout 16 | `9ad54715ef01`  |
| 1210   | Layout 16 | `9ad54715ef01`  |
| 1208   | Layout 16 | `9ad54715ef01`  |
| 1203   | Layout 16 | `9ad54715ef01`  |
| 1197   | Layout 16 | `9ad54715ef01`  |
| 1194   | Layout 16 | `9ad54715ef01`  |
| 1192   | Layout 16 | `9ad54715ef01`  |
| 1187   | Layout 16 | `9ad54715ef01`  |
| 1183   | Layout 16 | `9ad54715ef01`  |
| 1177   | Layout 16 | `9ad54715ef01`  |
| 1173   | Layout 16 | `9ad54715ef01`  |
| 1167   | Layout 16 | `9ad54715ef01`  |
| 1164   | Layout 15 | `9ad54715ef01`  |
| 1156   | Layout 15 | `9ad54715ef01`  |
| 1149   | Layout 15 | `9ad54715ef01`  |
| 1144   | Layout 15 | `9ad54715ef01`  |
| 1137   | Layout 15 | `9ad54715ef01`  |
| 1132   | Layout 15 | `9ad54715ef01`  |
| 1127   | Layout 15 | `9ad54715ef01`  |
| 1122   | Layout 15 | `9ad54715ef01`  |
| 1118   | Layout 15 | `9ad54715ef01`  |
| 1114   | Layout 15 | `9ad54715ef01`  |
| 1109   | Layout 15 | `9ad54715ef01`  |
| 1102   | No file   | `9ad54715ef01`  |
| 1096   | No file   | `9ad54715ef01`  |
| 1088   | No file   | `9ad54715ef01`  |
| 1081   | No file   | `9ad54715ef01`  |
| 1076   | No file   | `9ad54715ef01`  |
| 1069   | No file   | `9ad54715ef01`  |
| 1064   | No file   | `9ad54715ef01`  |
| 1058   | No file   | `9ad54715ef01`  |
| 1051   | No file   | `9ad54715ef01`  |
| 1044   | No file   | `9ad54715ef01`  |
| 1036   | No file   | `9ad54715ef01`  |
| 1026   | No file   | `9ad54715ef01`  |
| 1016   | No file   | `9ad54715ef01`  |
| 1009   | No file   | `9ad54715ef01`  |
| 1005   | No file   | `9ad54715ef01`  |
| 1000   | No file   | `9ad54715ef01`  |
| 998    | No file   | `9ad54715ef01`  |
| 990    | No file   | `9ad54715ef01`  |
| 979    | No file   | `9ad54715ef01`  |
| 972    | No file   | `9ad54715ef01`  |
| 963    | No file   | `9ad54715ef01`  |
| 955    | No file   | `9ad54715ef01`  |
| 946    | No file   | `9ad54715ef01`  |
| 938    | No file   | `9ad54715ef01`  |
| 927    | No file   | `9ad54715ef01`  |
| 911    | No file   | `9ad54715ef01`  |
| 904    | No file   | `9ad54715ef01`  |
| 899    | No file   | `9ad54715ef01`  |
| 894    | No file   | `9ad54715ef01`  |
| 885    | No file   | `9ad54715ef01`  |
| 879    | No file   | `9ad54715ef01`  |
| 872    | No file   | `9ad54715ef01`  |
| 864    | No file   | `9ad54715ef01`  |
| 855    | No file   | `9ad54715ef01`  |
| 853    | No file   | `9ad54715ef01`  |
| 845    | No file   | `9ad54715ef01`  |
| 837    | No file   | `9ad54715ef01`  |
| 829    | Layout 14 | `9ad54715ef01`  |
| 822    | Layout 14 | `9ad54715ef01`  |
| 814    | Layout 13 | `9ad54715ef01`  |
| 805    | Layout 12 | `9ad54715ef01`  |
| 794    | Layout 11 | `9ad54715ef01`  |
| 787    | Layout 11 | `9ad54715ef01`  |
| 780    | Layout 11 | `9ad54715ef01`  |
| 771    | Layout 11 | `9ad54715ef01`  |
| 760    | Layout 10 | `9ad54715ef01`  |
| 748    | Layout 10 | `9ad54715ef01`  |
| 741    | Layout 10 | `9ad54715ef01`  |
| 736    | Layout 10 | `9ad54715ef01`  |
| 731    | Layout 10 | `9ad54715ef01`  |
| 723    | Layout 10 | `9ad54715ef01`  |
| 711    | Layout 10 | `9ad54715ef01`  |
| 707    | Layout 10 | `9ad54715ef01`  |
| 697    | Layout 9  | `9ad54715ef01`  |
| 689    | Layout 9  | `9ad54715ef01`  |
| 683    | Layout 9  | `9ad54715ef01`  |
| 678    | Layout 9  | `9ad54715ef01`  |
| 670    | Layout 9  | `9ad54715ef01`  |
| 661    | Layout 9  | `9ad54715ef01`  |
| 656    | Layout 9  | `9ad54715ef01`  |
| 652    | Layout 9  | `9ad54715ef01`  |
| 643    | Layout 9  | `9ad54715ef01`  |
| 637    | Layout 8  | `9ad54715ef01`  |
| 630    | Layout 7  | `9ad54715ef01`  |
| 627    | Layout 7  | `9ad54715ef01`  |
| 621    | Layout 7  | `9ad54715ef01`  |
| 617    | Layout 7  | `9ad54715ef01`  |
| 615    | Layout 7  | `9ad54715ef01`  |
| 606    | Layout 7  | `9ad54715ef01`  |
| 599    | Layout 7  | `9ad54715ef01`  |
| 592    | Layout 7  | `9ad54715ef01`  |
| 586    | Layout 6  | `9ad54715ef01`  |
| 577    | Layout 6  | `9ad54715ef01`  |
| 569    | Layout 6  | `9ad54715ef01`  |
| 561    | Layout 6  | `9ad54715ef01`  |
| 554    | Layout 6  | `9ad54715ef01`  |
| 542    | Layout 6  | `9ad54715ef01`  |
| 532    | Layout 6  | `9ad54715ef01`  |
| 531    | Layout 6  | `9ad54715ef01`  |
| 526    | Layout 5  | `9ad54715ef01`  |
| 521    | Layout 5  | `9ad54715ef01`  |
| 517    | Layout 5  | `9ad54715ef01`  |
| 510    | Layout 5  | `9ad54715ef01`  |
| 508    | Layout 5  | `9ad54715ef01`  |
| 504    | Layout 4  | `9ad54715ef01`  |
| 497    | Layout 3  | `9ad54715ef01`  |
| 491    | Layout 3  | `9ad54715ef01`  |
| 485    | Layout 3  | `9ad54715ef01`  |
| 478    | Layout 2  | `9ad54715ef01`  |
| 472    | Layout 2  | `9ad54715ef01`  |
| 466    | Layout 1  | `9ad54715ef01`  |
| 457    | Layout 1  | `9ad54715ef01`  |
| 452    | Layout 1  | `9ad54715ef01`  |
| 449    | Layout 1  | `9ad54715ef01`  |
| 435    | Layout 1  | `9ad54715ef01`  |

<!-- versions:end -->

## Companion Files

The handler reads no other file. Class names come from LOC type 21
(`languagedata_*.loc`) when LOC is loaded; equip type names are built into
the handler, see [Equip Types](#equip-types), and so are the vehicle type
names of clients 435 to 829 (`_common/vehicle_type.py`).

All multi-byte values are little-endian.

## Block Counts

No count is stored. From client 1109 the class type count is the number of
class blocks before the class package list (or the string table, where
there is no list), the equip type count the number of Package Cells at the
start of each block. Clients 435 to 829 have no blocks: 32 class rows of
weapon packages, 32 rows of vehicle packages and one vehicle with weapon map
per class, then the same three as hashes. Their equip and vehicle type
counts are the row lengths, and their vehicle types are row positions, where
the blocks name each vehicle row. Clients 435 to 794 write each path in
place as `str8` and have no magic and no string table; clients 805 to 829
write a string table index. The counts grow with the client, the cutscene
cell arrived on client 1743 and the class package list on client 2107, so
the layouts differ only in these:

| Layout | Storage                   | Class types | Equip types | Vehicle types | Cutscene cell | Class package list |
| ------ | ------------------------- | ----------- | ----------- | ------------- | ------------- | ------------------ |
| 39     | Class blocks              | 97          | 119         | by name       | yes           | yes                |
| 38     | Class blocks              | 87          | 119         | by name       | yes           | yes                |
| 37     | Class blocks              | 87          | 118         | by name       | yes           | yes                |
| 36     | Class blocks              | 87          | 116         | by name       | yes           | yes                |
| 35     | Class blocks              | 87          | 115         | by name       | yes           | yes                |
| 34     | Class blocks              | 87          | 114         | by name       | yes           | yes                |
| 33     | Class blocks              | 87          | 112         | by name       | yes           | yes                |
| 32     | Class blocks              | 87          | 111         | by name       | yes           | yes                |
| 31     | Class blocks              | 87          | 109         | by name       | yes           | yes                |
| 30     | Class blocks              | 87          | 108         | by name       | yes           | yes                |
| 29     | Class blocks              | 87          | 102         | by name       | yes           | yes                |
| 28     | Class blocks              | 82          | 101         | by name       | yes           | yes                |
| 27     | Class blocks              | 82          | 100         | by name       | yes           | yes                |
| 26     | Class blocks              | 82          | 100         | by name       | yes           | no                 |
| 25     | Class blocks              | 82          | 98          | by name       | yes           | no                 |
| 24     | Class blocks              | 82          | 95          | by name       | yes           | no                 |
| 23     | Class blocks              | 82          | 93          | by name       | yes           | no                 |
| 22     | Class blocks              | 82          | 92          | by name       | yes           | no                 |
| 21     | Class blocks              | 82          | 91          | by name       | yes           | no                 |
| 20     | Class blocks              | 82          | 91          | by name       | no            | no                 |
| 19     | Class blocks              | 82          | 90          | by name       | no            | no                 |
| 18     | Class blocks              | 82          | 89          | by name       | no            | no                 |
| 17     | Class blocks              | 82          | 88          | by name       | no            | no                 |
| 16     | Class blocks              | 82          | 84          | by name       | no            | no                 |
| 15     | Class blocks              | 32          | 84          | by name       | no            | no                 |
| 14     | Arrays of string indices  | 32          | 77          | 56            | no            | no                 |
| 13     | Arrays of string indices  | 32          | 77          | 55            | no            | no                 |
| 12     | Arrays of string indices  | 32          | 76          | 55            | no            | no                 |
| 11     | Arrays of inline paths    | 32          | 76          | 55            | no            | no                 |
| 10     | Arrays of inline paths    | 32          | 76          | 54            | no            | no                 |
| 9      | Arrays of inline paths    | 32          | 75          | 54            | no            | no                 |
| 8      | Arrays of inline paths    | 32          | 75          | 53            | no            | no                 |
| 7      | Arrays of inline paths    | 32          | 73          | 53            | no            | no                 |
| 6      | Arrays of inline paths    | 32          | 72          | 53            | no            | no                 |
| 5      | Arrays of inline paths    | 32          | 72          | 52            | no            | no                 |
| 4      | Arrays of inline paths    | 32          | 72          | 51            | no            | no                 |
| 3      | Arrays of inline paths    | 32          | 72          | 49            | no            | no                 |
| 2      | Arrays of inline paths    | 32          | 72          | 48            | no            | no                 |
| 1      | Arrays of inline paths    | 32          | 68          | 48            | no            | no                 |

The handler finds the counts in the file. For class blocks, the equip type
count is the smallest one for which class block `0` holds a valid
[package hash](#package-hash) in every cell and row and the blocks then
reach `string_table_start`, tried with the cutscene cell first and then
without; the class blocks go on until the rest is nothing or exactly one
class package list (a u32 count and that many 9-byte rows). For arrays, the
row length (equip plus vehicle types) is the one whose hashes match every
path and whose last hash map ends the file or reaches `string_table_start`.
The weapon rows end at the first `pc/vehicle/` path, which on every client
from 435 to 829 is the first cell of a class row: the Warrior's (class type
`0`) `Horse` package. The doc check walks literal counts only (`T[N]` or
`T[field]` in [format-docs.md](../../format-docs.md#types)), so each count set
is a layout of its own here. An older layout lists only the structures that
differ from the next newer one.

## Layout 39

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
[`itemenchant.dbss`](../dbss/itemenchant_dbss.md#equip_type)); see
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

## Layout 38

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

## Layout 37

87 class types and 118 equip types, with the class package list.

### Class Block (variable: 956 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[118]          | weapon_packages         | One cell per equip type, `0` to `117` |
| `+0x3B0`                       | u32                        | vehicle_count           |                                       |
| `+0x3B4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[118]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 36

87 class types and 116 equip types, with the class package list.

### Class Block (variable: 940 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[116]          | weapon_packages         | One cell per equip type, `0` to `115` |
| `+0x3A0`                       | u32                        | vehicle_count           |                                       |
| `+0x3A4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[116]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 35

87 class types and 115 equip types, with the class package list.

### Class Block (variable: 932 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[115]          | weapon_packages         | One cell per equip type, `0` to `114` |
| `+0x398`                       | u32                        | vehicle_count           |                                       |
| `+0x39C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[115]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 34

87 class types and 114 equip types, with the class package list.

### Class Block (variable: 924 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[114]          | weapon_packages         | One cell per equip type, `0` to `113` |
| `+0x390`                       | u32                        | vehicle_count           |                                       |
| `+0x394`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[114]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 33

87 class types and 112 equip types, with the class package list.

### Class Block (variable: 908 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[112]          | weapon_packages         | One cell per equip type, `0` to `111` |
| `+0x380`                       | u32                        | vehicle_count           |                                       |
| `+0x384`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[112]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 32

87 class types and 111 equip types, with the class package list.

### Class Block (variable: 900 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[111]          | weapon_packages         | One cell per equip type, `0` to `110` |
| `+0x378`                       | u32                        | vehicle_count           |                                       |
| `+0x37C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[111]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 31

87 class types and 109 equip types, with the class package list.

### Class Block (variable: 884 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[109]          | weapon_packages         | One cell per equip type, `0` to `108` |
| `+0x368`                       | u32                        | vehicle_count           |                                       |
| `+0x36C`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[109]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 30

87 class types and 108 equip types, with the class package list.

### Class Block (variable: 876 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[108]          | weapon_packages         | One cell per equip type, `0` to `107` |
| `+0x360`                       | u32                        | vehicle_count           |                                       |
| `+0x364`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[108]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 29

87 class types and 102 equip types, with the class package list.

### Class Block (variable: 828 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                 |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------- |
| `+0x00`                        | Package Cell[102]          | weapon_packages         | One cell per equip type, `0` to `101` |
| `+0x330`                       | u32                        | vehicle_count           |                                       |
| `+0x334`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                       |
| `vehicle_packages+0x00`        | Equip Vehicle List[102]    | vehicle_weapon_packages |                                       |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                       |

## Layout 28

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

## Layout 27

82 class types and 100 equip types, with the class package list.

### Class Block (variable: 812 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[100]          | weapon_packages         | One cell per equip type, `0` to `99` |
| `+0x320`                       | u32                        | vehicle_count           |                                      |
| `+0x324`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[100]    | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 26

82 class types and 100 equip types, without the class package list.

### File Layout

| Offset              | Type            | Field              | Notes                                 |
| ------------------- | --------------- | ------------------ | ------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                          |
| `+0x04`             | Class Block[82] | classes            | One block per class type, `0` to `81` |
| `classes+0x00`      | String Table    | string_table       |                                       |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`              |
| `string_table+0x04` | u32             | zero               | Always `0`                            |

## Layout 25

82 class types and 98 equip types, without the class package list.

### Class Block (variable: 796 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[98]           | weapon_packages         | One cell per equip type, `0` to `97` |
| `+0x310`                       | u32                        | vehicle_count           |                                      |
| `+0x314`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[98]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 24

82 class types and 95 equip types, without the class package list.

### Class Block (variable: 772 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[95]           | weapon_packages         | One cell per equip type, `0` to `94` |
| `+0x2F8`                       | u32                        | vehicle_count           |                                      |
| `+0x2FC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[95]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 23

82 class types and 93 equip types, without the class package list.

### Class Block (variable: 756 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[93]           | weapon_packages         | One cell per equip type, `0` to `92` |
| `+0x2E8`                       | u32                        | vehicle_count           |                                      |
| `+0x2EC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[93]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 22

82 class types and 92 equip types, without the class package list.

### Class Block (variable: 748 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[92]           | weapon_packages         | One cell per equip type, `0` to `91` |
| `+0x2E0`                       | u32                        | vehicle_count           |                                      |
| `+0x2E4`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[92]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 21

82 class types and 91 equip types, without the class package list.

### Class Block (variable: 740 bytes + vehicle rows)

| Offset                         | Type                       | Field                   | Notes                                |
| ------------------------------ | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                        | Package Cell[91]           | weapon_packages         | One cell per equip type, `0` to `90` |
| `+0x2D8`                       | u32                        | vehicle_count           |                                      |
| `+0x2DC`                       | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00`        | Equip Vehicle List[91]     | vehicle_weapon_packages |                                      |
| `vehicle_weapon_packages+0x00` | Package Cell               | cutscene_package        |                                      |

## Layout 20

82 class types and 91 equip types, without the cutscene cell and the class package list.

### Class Block (variable: 732 bytes + vehicle rows)

| Offset                  | Type                       | Field                   | Notes                                |
| ----------------------- | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                 | Package Cell[91]           | weapon_packages         | One cell per equip type, `0` to `90` |
| `+0x2D8`                | u32                        | vehicle_count           |                                      |
| `+0x2DC`                | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00` | Equip Vehicle List[91]     | vehicle_weapon_packages | No `cutscene_package` follows        |

## Layout 19

82 class types and 90 equip types, without the cutscene cell and the class package list.

### Class Block (variable: 724 bytes + vehicle rows)

| Offset                  | Type                       | Field                   | Notes                                |
| ----------------------- | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                 | Package Cell[90]           | weapon_packages         | One cell per equip type, `0` to `89` |
| `+0x2D0`                | u32                        | vehicle_count           |                                      |
| `+0x2D4`                | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00` | Equip Vehicle List[90]     | vehicle_weapon_packages | No `cutscene_package` follows        |

## Layout 18

82 class types and 89 equip types, without the cutscene cell and the class package list.

### Class Block (variable: 716 bytes + vehicle rows)

| Offset                  | Type                       | Field                   | Notes                                |
| ----------------------- | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                 | Package Cell[89]           | weapon_packages         | One cell per equip type, `0` to `88` |
| `+0x2C8`                | u32                        | vehicle_count           |                                      |
| `+0x2CC`                | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00` | Equip Vehicle List[89]     | vehicle_weapon_packages | No `cutscene_package` follows        |

## Layout 17

82 class types and 88 equip types, without the cutscene cell and the class package list.

### Class Block (variable: 708 bytes + vehicle rows)

| Offset                  | Type                       | Field                   | Notes                                |
| ----------------------- | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                 | Package Cell[88]           | weapon_packages         | One cell per equip type, `0` to `87` |
| `+0x2C0`                | u32                        | vehicle_count           |                                      |
| `+0x2C4`                | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00` | Equip Vehicle List[88]     | vehicle_weapon_packages | No `cutscene_package` follows        |

## Layout 16

82 class types and 84 equip types, without the cutscene cell and the class package list.

### Class Block (variable: 676 bytes + vehicle rows)

| Offset                  | Type                       | Field                   | Notes                                |
| ----------------------- | -------------------------- | ----------------------- | ------------------------------------ |
| `+0x00`                 | Package Cell[84]           | weapon_packages         | One cell per equip type, `0` to `83` |
| `+0x2A0`                | u32                        | vehicle_count           |                                      |
| `+0x2A4`                | Vehicle Row[vehicle_count] | vehicle_packages        |                                      |
| `vehicle_packages+0x00` | Equip Vehicle List[84]     | vehicle_weapon_packages | No `cutscene_package` follows        |

## Layout 15

32 class types and 84 equip types, without the cutscene cell and the class package list.

### File Layout

| Offset              | Type            | Field              | Notes                                 |
| ------------------- | --------------- | ------------------ | ------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                          |
| `+0x04`             | Class Block[32] | classes            | One block per class type, `0` to `31` |
| `classes+0x00`      | String Table    | string_table       |                                       |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`              |
| `string_table+0x04` | u32             | zero               | Always `0`                            |

## Layout 14

32 class types, 77 equip types and 56 vehicle types, as arrays of string indices.

### File Layout

| Offset                               | Type                        | Field                         | Notes                                                           |
| ------------------------------------ | --------------------------- | ----------------------------- | --------------------------------------------------------------- |
| `+0x00`                              | char[4]                     | magic                         | ASCII `PABR`                                                    |
| `+0x04`                              | u32[32][77]                 | weapon_package_indices        | One row per class type, one string index per equip type         |
| `+0x2684`                            | u32[32][56]                 | vehicle_package_indices       | One row per class type, one string index per vehicle type       |
| `+0x4284`                            | Vehicle Weapon Map[32]      | vehicle_weapon_packages       | One map per class type                                          |
| `vehicle_weapon_packages+0x00`       | u32[32][77]                 | weapon_package_hashes         | Hash of each weapon package, same order; `0` when empty         |
| `vehicle_weapon_packages+0x2680`     | u32[32][56]                 | vehicle_package_hashes        | Hash of each vehicle package, same order                        |
| `vehicle_weapon_packages+0x4280`     | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes | One map per class type, the hashes of `vehicle_weapon_packages` |
| `vehicle_weapon_package_hashes+0x00` | String Table                | string_table                  |                                                                 |
| `string_table+0x00`                  | u32                         | string_table_start            | Offset of `string_count`                                        |
| `string_table+0x04`                  | u32                         | zero                          | Always `0`                                                      |

### Vehicle Weapon Map (variable: 4 bytes + rows)

| Offset  | Type                          | Field     | Notes                              |
| ------- | ----------------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                           | row_count | `0` or `1`; `2` on client 643 only |
| `+0x04` | Vehicle Weapon Row[row_count] | rows      |                                    |

### Vehicle Weapon Row (6 bytes)

| Offset  | Type | Field         | Notes                                     |
| ------- | ---- | ------------- | ----------------------------------------- |
| `+0x00` | u8   | vehicle_type  | `CppEnums.VehicleType`, such as `0` Horse |
| `+0x01` | u8   | equip_type    | Such as `53` HuntRifle                    |
| `+0x02` | u32  | package_index | Index into the string table; unaligned    |

### Vehicle Weapon Hash Map (variable: 4 bytes + rows)

| Offset  | Type                               | Field     | Notes                        |
| ------- | ---------------------------------- | --------- | ---------------------------- |
| `+0x00` | u32                                | row_count | Same as the map of the class |
| `+0x04` | Vehicle Weapon Hash Row[row_count] | rows      |                              |

### Vehicle Weapon Hash Row (6 bytes)

| Offset  | Type | Field        | Notes                                    |
| ------- | ---- | ------------ | ---------------------------------------- |
| `+0x00` | u8   | vehicle_type | Same as the map row                      |
| `+0x01` | u8   | equip_type   | Same as the map row                      |
| `+0x02` | u32  | package_hash | Hash of the map row's package; unaligned |

## Layout 13

32 class types, 77 equip types and 55 vehicle types, as arrays of string indices.

### File Layout

| Offset                               | Type                        | Field                         | Notes |
| ------------------------------------ | --------------------------- | ----------------------------- | ----- |
| `+0x00`                              | char[4]                     | magic                         |       |
| `+0x04`                              | u32[32][77]                 | weapon_package_indices        |       |
| `+0x2684`                            | u32[32][55]                 | vehicle_package_indices       |       |
| `+0x4204`                            | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |       |
| `vehicle_weapon_packages+0x00`       | u32[32][77]                 | weapon_package_hashes         |       |
| `vehicle_weapon_packages+0x2680`     | u32[32][55]                 | vehicle_package_hashes        |       |
| `vehicle_weapon_packages+0x4200`     | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |       |
| `vehicle_weapon_package_hashes+0x00` | String Table                | string_table                  |       |
| `string_table+0x00`                  | u32                         | string_table_start            |       |
| `string_table+0x04`                  | u32                         | zero                          |       |

## Layout 12

32 class types, 76 equip types and 55 vehicle types, as arrays of string indices.

### File Layout

| Offset                               | Type                        | Field                         | Notes |
| ------------------------------------ | --------------------------- | ----------------------------- | ----- |
| `+0x00`                              | char[4]                     | magic                         |       |
| `+0x04`                              | u32[32][76]                 | weapon_package_indices        |       |
| `+0x2604`                            | u32[32][55]                 | vehicle_package_indices       |       |
| `+0x4184`                            | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |       |
| `vehicle_weapon_packages+0x00`       | u32[32][76]                 | weapon_package_hashes         |       |
| `vehicle_weapon_packages+0x2600`     | u32[32][55]                 | vehicle_package_hashes        |       |
| `vehicle_weapon_packages+0x4180`     | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |       |
| `vehicle_weapon_package_hashes+0x00` | String Table                | string_table                  |       |
| `string_table+0x00`                  | u32                         | string_table_start            |       |
| `string_table+0x04`                  | u32                         | zero                          |       |

## Layout 11

32 class types, 76 equip types and 55 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                                                                    |
| -------------------------------- | --------------------------- | ----------------------------- | ------------------------------------------------------------------------ |
| `+0x00`                          | str8[2432]                  | weapon_packages               | No magic; 32 rows of 76: one row per class type, one path per equip type |
| `weapon_packages+0x00`           | str8[1760]                  | vehicle_packages              | 32 rows of 55: one row per class type, one path per vehicle type         |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       | One map per class type                                                   |
| `vehicle_weapon_packages+0x00`   | u32[32][76]                 | weapon_package_hashes         | Hash of each weapon package, same order; `0` when empty                  |
| `vehicle_weapon_packages+0x2600` | u32[32][55]                 | vehicle_package_hashes        | Hash of each vehicle package, same order                                 |
| `vehicle_weapon_packages+0x4180` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes | One map per class type, the hashes of `vehicle_weapon_packages`          |

### Vehicle Weapon Row (variable: 10 bytes + package text)

| Offset  | Type | Field        | Notes    |
| ------- | ---- | ------------ | -------- |
| `+0x00` | u8   | vehicle_type |          |
| `+0x01` | u8   | equip_type   |          |
| `+0x02` | str8 | package      | The path |

## Layout 10

32 class types, 76 equip types and 54 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2432]                  | weapon_packages               | No magic; 32 rows of 76 |
| `weapon_packages+0x00`           | str8[1728]                  | vehicle_packages              | 32 rows of 54           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][76]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2600` | u32[32][54]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x4100` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 9

32 class types, 75 equip types and 54 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2400]                  | weapon_packages               | No magic; 32 rows of 75 |
| `weapon_packages+0x00`           | str8[1728]                  | vehicle_packages              | 32 rows of 54           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][75]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2580` | u32[32][54]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x4080` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 8

32 class types, 75 equip types and 53 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2400]                  | weapon_packages               | No magic; 32 rows of 75 |
| `weapon_packages+0x00`           | str8[1696]                  | vehicle_packages              | 32 rows of 53           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][75]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2580` | u32[32][53]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x4000` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 7

32 class types, 73 equip types and 53 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2336]                  | weapon_packages               | No magic; 32 rows of 73 |
| `weapon_packages+0x00`           | str8[1696]                  | vehicle_packages              | 32 rows of 53           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][73]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2480` | u32[32][53]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3F00` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 6

32 class types, 72 equip types and 53 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2304]                  | weapon_packages               | No magic; 32 rows of 72 |
| `weapon_packages+0x00`           | str8[1696]                  | vehicle_packages              | 32 rows of 53           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][72]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2400` | u32[32][53]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3E80` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 5

32 class types, 72 equip types and 52 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2304]                  | weapon_packages               | No magic; 32 rows of 72 |
| `weapon_packages+0x00`           | str8[1664]                  | vehicle_packages              | 32 rows of 52           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][72]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2400` | u32[32][52]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3E00` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 4

32 class types, 72 equip types and 51 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2304]                  | weapon_packages               | No magic; 32 rows of 72 |
| `weapon_packages+0x00`           | str8[1632]                  | vehicle_packages              | 32 rows of 51           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][72]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2400` | u32[32][51]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3D80` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 3

32 class types, 72 equip types and 49 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2304]                  | weapon_packages               | No magic; 32 rows of 72 |
| `weapon_packages+0x00`           | str8[1568]                  | vehicle_packages              | 32 rows of 49           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][72]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2400` | u32[32][49]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3C80` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 2

32 class types, 72 equip types and 48 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2304]                  | weapon_packages               | No magic; 32 rows of 72 |
| `weapon_packages+0x00`           | str8[1536]                  | vehicle_packages              | 32 rows of 48           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][72]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2400` | u32[32][48]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3C00` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Layout 1

32 class types, 68 equip types and 48 vehicle types, as arrays of inline paths.

### File Layout

| Offset                           | Type                        | Field                         | Notes                   |
| -------------------------------- | --------------------------- | ----------------------------- | ----------------------- |
| `+0x00`                          | str8[2176]                  | weapon_packages               | No magic; 32 rows of 68 |
| `weapon_packages+0x00`           | str8[1536]                  | vehicle_packages              | 32 rows of 48           |
| `vehicle_packages+0x00`          | Vehicle Weapon Map[32]      | vehicle_weapon_packages       |                         |
| `vehicle_weapon_packages+0x00`   | u32[32][68]                 | weapon_package_hashes         |                         |
| `vehicle_weapon_packages+0x2200` | u32[32][48]                 | vehicle_package_hashes        |                         |
| `vehicle_weapon_packages+0x3A00` | Vehicle Weapon Hash Map[32] | vehicle_weapon_package_hashes |                         |

## Package Hash

`package_hash` is Bob Jenkins' lookup3 `hashlittle` of the path's ASCII
bytes with seed `0xC5EDE`, the hash `manufacture.bss` stores for its
action names (`ascii_key_hash` in `_common/string_hash.py`). It matches on
every non-empty cell and row of every client from 435 to 3483; clients 435
to 829 keep it in the hash arrays, at the position of the path in the name
arrays. Empty cells store `0`, not the hash of the empty string
(`0xDEBA1DCD`). Vehicle type names have no hash.

## Equip Types

The cell position in `weapon_packages` and the list position in
`vehicle_weapon_packages` is the item `equip_type` of
[`itemenchant.dbss`](../dbss/itemenchant_dbss.md#equip_type): Longsword `1` holds
`pc/1_phm/fighteraction_onehandsword` for the Warrior, matchlock `53` the
`commonchart_huntrifle` packages. An older layout has the same types up to
its count; in the array layouts the equip type is the position in a class
row of `weapon_packages` or `weapon_package_indices`, and the `equip_type`
of a Vehicle Weapon Row. On client 3483, 45 of the 119 equip types hold a
package for at least one class.

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

The only `vehicle_weapon_packages` entries on clients 435 to 3483 are
`Horse` under equip type `53`, the `horsehuntrifle` package of each class
(34 classes on client 3483), and on client 643 alone also vehicle type `53`
(`RaceHorse`) under `53`. The sheet's one `PcActionVehicleWithWeapon_Table`
row is `Horse` with `HuntRifle`.

## Vehicle Types

The class blocks name each vehicle row by a string, such as `Horse`. The
array layouts of clients 435 to 829 have no names: the position in a class
row of `vehicle_packages` or `vehicle_package_indices`, and the
`vehicle_type` of a Vehicle Weapon Row, is the `CppEnums.VehicleType` value
of `global_define_cpp_enum.luac` (`_common/vehicle_type.py`). Matching the
paths of client 829 against the named rows of client 1109 bears this out:
position `0` holds the packages client 1109 lists under `Horse`, `18` those
under `Boat`, `22` `Ballista`, `32` `MountainGoat`, `53` `RaceHorse` and
`55` `FastShip`, the enum's names for those values. The browser's Vehicle
Type column shows the enum name for these clients, or the bare number
where the enum has none.

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) declare
`gc::PcActionPackageNameManager` with the members
`_packageNameArray_Weapon[32][63]`, `_packageNameArray_Vehicle[32][37]` and
`_packageNameMap_VehicleWithWeapon[32]`, a map keyed by
`(gc::VehicleType, gc::ItemEquipType::Type)`, each next to a matching
`_packageHash*` member of `unsigned int`. The outer index is the class type,
the inner `63` of the weapon array is `gc::ItemEquipType::TypeCount`.
Clients 435 to 829 store these members in that shape: the name arrays and
the maps, then the hash arrays and maps, with 68 to 77 equip types and 48 to
56 vehicle types per row. From client 1109 the file stores each name and
hash as one Package Cell; the vehicle array became rows keyed by the vehicle
type name, and the map one list per equip type.

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
- Clients 1109 to 1164 hold 32 class blocks, the outer count of the 2016
  arrays and of the array layouts; client 1167 has 82.
- Clients 435 to 794 have no PABR trailer: their last 8 bytes are the end
  of the last hash map, so a PABR reader takes `0x35000000`
  (`0x3535FF60` on client 643) for `string_table_start`.
- Clients 837 to 1102 have no `pcactionpackagename.bss`.

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
