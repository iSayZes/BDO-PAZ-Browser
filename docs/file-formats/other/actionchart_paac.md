# `*.paac` Format

## Purpose

An action chart under `character/binaryactionchart/` describes how one
character, mount, monster or object moves: its animations (`.paa` clips),
skeleton (`.pab`), mesh parts (`.pac`), effects, hit parts, condition
records, frame events and, last, its packages of actions. Client 3483 has
8,031 `.paac` files. The game server does not read them; it loads its own
per-weapon summaries.

Each class folder under `pc/` has one chart, `<class>action_noweapon.paac`
(`13_pnw` has two; 33 charts in 32 folders on client 3483), and that chart
holds every package of the class: weapon, vehicle and cutscene packages included. The packages
are the ones [`pcactionpackagename.bss`](../bss/pcactionpackagename_bss.md)
names: on client 3483, 4,449 of its 4,594 package hashes are package keys of
a class chart, and the 145 others belong to classes with no chart yet
(`pc/26_pbm/...`). On client 3483, 30 of the 33 class charts have 139 or 140
packages (`elfaction_noweapon.paac`: 139 packages, 23,211 actions);
`shytribeaction_noweaponmain_w.paac` has 135 and
`bladewomen2action_noweapon.paac` 4.

`pc/pc_actionchartpackagepcraw.paac` holds the condition records, frame
events and elements the class charts share (the class charts have
`uses_shared_tables` set and no records, events or elements of their own);
its table is in each layout. Layout 1 is client 1784, the build of the
client loader the field notes come from; Layout 2 is the current one.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                                              | Bytes       | Records                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Row bytes                |
| ------ | -------------- | ----------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| 2      | 3258 and later | `character/binaryactionchart/pc/3_pew/elfaction_noweapon.paac`    | 8,032,893   | 2,451 Animation, 60 U32 List, 60 U64 List, 167 Animation Event, 8 List Pair, 15 List Entry, 14 List Weight, 4 List Group, 263 Mesh Part, 1,549 Effect Attachment, 1,564 Effect Data, 1,564 Effect, 240 Unknown Row, 42 Slot Entry, 25,828 Branch Row, 2,137 Branch, 61,086 Action Row B, 23,211 Action, 139 Package, 574 Key Pair, 5,717 Action Row A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 22                       |
| 2      | 3258 and later | `character/binaryactionchart/pc/9_pem/elfmanaction_noweapon.paac` | 7,991,869   | 2,503 Animation, 61 U32 List, 61 U64 List, 128 Animation Event, 10 List Pair, 17 List Entry, 15 List Weight, 5 List Group, 271 Mesh Part, 1,549 Effect Attachment, 1,564 Effect Data, 1,564 Effect, 240 Unknown Row, 42 Slot Entry, 55,134 Action Row B, 22,251 Action, 139 Package, 824 Key Pair, 2,014 Branch, 25,609 Branch Row, 11,031 Action Row A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 22                       |
| 2      | 3258 and later | `pc_actionchartpackagepcraw.paac`                                 | 134,345,673 | 74,498 Wide List, 103,365 Condition Set, 101,452 Condition Record, 97,156 U16 List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 18 to 250, 50 on average |
| 1      | 1784           | `character/binaryactionchart/pc/3_pew/elfaction_noweapon.paac`    | 6,459,012   | 1,865 Animation, 54 U32 List, 54 U64 List, 90 Animation Event, 4 List Pair, 3 List Entry, 2 List Weight, 2 List Group, 120 Mesh Part, 870 Effect Attachment, 885 Effect Data, 885 Effect, 195 Unknown Row, 32 Slot Entry, 553 Key Pair, 18,659 Branch Row, 1,877 Branch, 52,306 Action Row B, 20,012 Action Data, 20,012 Element Link, 20,012 Action, 127 Package, 5,172 Action Row A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 22                       |
| 1      | 1784           | `character/binaryactionchart/pc/9_pem/elfmanaction_noweapon.paac` | 6,239,372   | 1,919 Animation, 55 U32 List, 55 U64 List, 64 Animation Event, 6 List Pair, 5 List Entry, 3 List Weight, 3 List Group, 129 Mesh Part, 870 Effect Attachment, 885 Effect Data, 885 Effect, 195 Unknown Row, 32 Slot Entry, 776 Key Pair, 18,794 Branch Row, 1,742 Branch, 45,362 Action Row B, 18,925 Action Data, 18,925 Element Link, 18,925 Action, 127 Package, 10,935 Action Row A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 22                       |
| 1      | 1784           | `pc_actionchartpackagepcraw.paac`                                 | 125,206,586 | 97,419 U16 List, 551,095 Condition Set, 87,411 Condition Record, 348,729 Wide List, 3,100 Switch Fields, 299,518 Frame Event, 498 Switch Chain Fields, 1,456 Mesh Fields, 1,725 Name Data Fields, 52,727 Data Fields, 763 Weapon Mesh Fields, 96,747 Effect Attachment, 93,857 Effect Data, 93,658 Effect Fields, 291 Lua Event Fields, 85 Battle FX Fields, 10,419 Two Value Fields, 762 Weapon Fields, 4,501 Camera Fields, 199 Effect Ground Fields, 2,022 Value Fields, 98,088 Attack Skill Fields, 533 Name Fields, 355 Jump Fields, 43 Bubble Fields, 1,082 Attack Fields, 55 Two Byte Fields, 20,606 Attack Arrow Skill Fields, 18 Switch Target Fields, 486 Light Fields, 2 Grenade Path Fields, 26 Camera Motion Fields, 1,146 Sword Trail Fields, 69 Byte Fields, 960 Decal Fields, 27 Glitter Fields, 48 Model Animation Fields, 976 Client Attack Fields, 9 Play Animation Fields, 1,808 Cannon Predict Fields, 11 Wave Fields, 686 Attack Arrow Fields, 88 Attack Catch Fields, 42 Attack Throw Fields, 76,993 Element Parameters, 76,993 Element, 307,067 Element Record, 585 Element Group | 8 to 256, 28 on average  |

| Layout | File                                                              | Known                | Unknown               |
| ------ | ----------------------------------------------------------------- | -------------------- | --------------------- |
| 2      | `character/binaryactionchart/pc/3_pew/elfaction_noweapon.paac`    | 2,057,735 B (25.6%)  | 5,975,158 B (74.4%)   |
| 2      | `character/binaryactionchart/pc/9_pem/elfmanaction_noweapon.paac` | 1,991,083 B (24.9%)  | 6,000,786 B (75.1%)   |
| 2      | `pc_actionchartpackagepcraw.paac`                                 | 9,493,101 B (7.1%)   | 124,852,572 B (92.9%) |
| 1      | `character/binaryactionchart/pc/3_pew/elfaction_noweapon.paac`    | 2,189,832 B (33.9%)  | 4,269,180 B (66.1%)   |
| 1      | `character/binaryactionchart/pc/9_pem/elfmanaction_noweapon.paac` | 2,088,413 B (33.5%)  | 4,150,959 B (66.5%)   |
| 1      | `pc_actionchartpackagepcraw.paac`                                 | 27,035,485 B (21.6%) | 98,171,101 B (78.4%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `67a9d3b7974b`  |
| 3482   | No file              | `67a9d3b7974b`  |
| 3474   | No file              | `67a9d3b7974b`  |
| 3473   | No file              | `67a9d3b7974b`  |
| 3464   | No file              | `67a9d3b7974b`  |
| 3458   | No file              | `67a9d3b7974b`  |
| 3454   | No file              | `67a9d3b7974b`  |
| 3444   | No file              | `67a9d3b7974b`  |
| 3435   | No file              | `67a9d3b7974b`  |
| 3426   | No file              | `67a9d3b7974b`  |
| 3418   | No file              | `67a9d3b7974b`  |
| 3412   | No file              | `67a9d3b7974b`  |
| 3402   | No file              | `67a9d3b7974b`  |
| 3396   | No file              | `67a9d3b7974b`  |
| 3387   | No file              | `67a9d3b7974b`  |
| 3381   | No file              | `67a9d3b7974b`  |
| 3373   | No file              | `67a9d3b7974b`  |
| 3364   | No file              | `67a9d3b7974b`  |
| 3356   | No file              | `67a9d3b7974b`  |
| 3349   | No file              | `67a9d3b7974b`  |
| 3342   | No file              | `67a9d3b7974b`  |
| 3335   | No file              | `67a9d3b7974b`  |
| 3326   | No file              | `67a9d3b7974b`  |
| 3321   | No file              | `67a9d3b7974b`  |
| 3314   | No file              | `67a9d3b7974b`  |
| 3303   | No file              | `67a9d3b7974b`  |
| 3302   | No file              | `67a9d3b7974b`  |
| 3293   | No file              | `67a9d3b7974b`  |
| 3283   | No file              | `67a9d3b7974b`  |
| 3275   | No file              | `67a9d3b7974b`  |
| 3267   | No file              | `67a9d3b7974b`  |
| 3258   | Layout 2             | `67a9d3b7974b`  |
| 3251   | No file              | `67a9d3b7974b`  |
| 3242   | No file              | `67a9d3b7974b`  |
| 3235   | No file              | `67a9d3b7974b`  |
| 3229   | No file              | `67a9d3b7974b`  |
| 3212   | No file              | `67a9d3b7974b`  |
| 3203   | No file              | `67a9d3b7974b`  |
| 3193   | No file              | `67a9d3b7974b`  |
| 3186   | No file              | `67a9d3b7974b`  |
| 3177   | No file              | `67a9d3b7974b`  |
| 3169   | No file              | `67a9d3b7974b`  |
| 3158   | No file              | `67a9d3b7974b`  |
| 3151   | No file              | `67a9d3b7974b`  |
| 3144   | No file              | `67a9d3b7974b`  |
| 3133   | No file              | `67a9d3b7974b`  |
| 3125   | No file              | `67a9d3b7974b`  |
| 3118   | No file              | `67a9d3b7974b`  |
| 3111   | No file              | `67a9d3b7974b`  |
| 3103   | No file              | `67a9d3b7974b`  |
| 3095   | No file              | `67a9d3b7974b`  |
| 3086   | No file              | `67a9d3b7974b`  |
| 3072   | No file              | `67a9d3b7974b`  |
| 3062   | No file              | `67a9d3b7974b`  |
| 3052   | No file              | `67a9d3b7974b`  |
| 3045   | No file              | `67a9d3b7974b`  |
| 3037   | No file              | `67a9d3b7974b`  |
| 3030   | No file              | `67a9d3b7974b`  |
| 3021   | No file              | `67a9d3b7974b`  |
| 3012   | No file              | `67a9d3b7974b`  |
| 3002   | No file              | `67a9d3b7974b`  |
| 2995   | No file              | `67a9d3b7974b`  |
| 2987   | No file              | `67a9d3b7974b`  |
| 2978   | No file              | `67a9d3b7974b`  |
| 2970   | No file              | `67a9d3b7974b`  |
| 2959   | No file              | `67a9d3b7974b`  |
| 2951   | No file              | `67a9d3b7974b`  |
| 2942   | No file              | `67a9d3b7974b`  |
| 2935   | No file              | `67a9d3b7974b`  |
| 2932   | No file              | `67a9d3b7974b`  |
| 2923   | No file              | `67a9d3b7974b`  |
| 2919   | No documented layout | `67a9d3b7974b`  |
| 2907   | No file              | `67a9d3b7974b`  |
| 2900   | No file              | `67a9d3b7974b`  |
| 2891   | No file              | `67a9d3b7974b`  |
| 2882   | No file              | `67a9d3b7974b`  |
| 2872   | No file              | `67a9d3b7974b`  |
| 2863   | No file              | `67a9d3b7974b`  |
| 2855   | No file              | `67a9d3b7974b`  |
| 2849   | No file              | `67a9d3b7974b`  |
| 2844   | No file              | `67a9d3b7974b`  |
| 2834   | No file              | `67a9d3b7974b`  |
| 2825   | No file              | `67a9d3b7974b`  |
| 2819   | No file              | `67a9d3b7974b`  |
| 2811   | No file              | `67a9d3b7974b`  |
| 2803   | No file              | `67a9d3b7974b`  |
| 2794   | No file              | `67a9d3b7974b`  |
| 2783   | No file              | `67a9d3b7974b`  |
| 2774   | No file              | `67a9d3b7974b`  |
| 2765   | No file              | `67a9d3b7974b`  |
| 2756   | No file              | `67a9d3b7974b`  |
| 2750   | No file              | `67a9d3b7974b`  |
| 2743   | No file              | `67a9d3b7974b`  |
| 2736   | No file              | `67a9d3b7974b`  |
| 2726   | No file              | `67a9d3b7974b`  |
| 2717   | No file              | `67a9d3b7974b`  |
| 2709   | No file              | `67a9d3b7974b`  |
| 2703   | No file              | `67a9d3b7974b`  |
| 2695   | No file              | `67a9d3b7974b`  |
| 2684   | No file              | `67a9d3b7974b`  |
| 2672   | No file              | `67a9d3b7974b`  |
| 2665   | No file              | `67a9d3b7974b`  |
| 2657   | No file              | `67a9d3b7974b`  |
| 2649   | No file              | `67a9d3b7974b`  |
| 2644   | No file              | `67a9d3b7974b`  |
| 2637   | No file              | `67a9d3b7974b`  |
| 2629   | No file              | `67a9d3b7974b`  |
| 2619   | No file              | `67a9d3b7974b`  |
| 2612   | No file              | `67a9d3b7974b`  |
| 2606   | No file              | `67a9d3b7974b`  |
| 2602   | No file              | `67a9d3b7974b`  |
| 2601   | No file              | `67a9d3b7974b`  |
| 2592   | No file              | `67a9d3b7974b`  |
| 2583   | No file              | `67a9d3b7974b`  |
| 2575   | No file              | `67a9d3b7974b`  |
| 2567   | No file              | `67a9d3b7974b`  |
| 2560   | No file              | `67a9d3b7974b`  |
| 2553   | No file              | `67a9d3b7974b`  |
| 2545   | No file              | `67a9d3b7974b`  |
| 2538   | No file              | `67a9d3b7974b`  |
| 2529   | No file              | `67a9d3b7974b`  |
| 2519   | No file              | `67a9d3b7974b`  |
| 2513   | No file              | `67a9d3b7974b`  |
| 2510   | No file              | `67a9d3b7974b`  |
| 2507   | No file              | `67a9d3b7974b`  |
| 2503   | No file              | `67a9d3b7974b`  |
| 2498   | No file              | `67a9d3b7974b`  |
| 2492   | No file              | `67a9d3b7974b`  |
| 2487   | No file              | `67a9d3b7974b`  |
| 2480   | No file              | `67a9d3b7974b`  |
| 2474   | No file              | `67a9d3b7974b`  |
| 2468   | No file              | `67a9d3b7974b`  |
| 2460   | No file              | `67a9d3b7974b`  |
| 2453   | No file              | `67a9d3b7974b`  |
| 2444   | No file              | `67a9d3b7974b`  |
| 2438   | No file              | `67a9d3b7974b`  |
| 2434   | No file              | `67a9d3b7974b`  |
| 2429   | No file              | `67a9d3b7974b`  |
| 2421   | No file              | `67a9d3b7974b`  |
| 2414   | No file              | `67a9d3b7974b`  |
| 2407   | No file              | `67a9d3b7974b`  |
| 2401   | No file              | `67a9d3b7974b`  |
| 2397   | No file              | `67a9d3b7974b`  |
| 2393   | No file              | `67a9d3b7974b`  |
| 2384   | No file              | `67a9d3b7974b`  |
| 2378   | No file              | `67a9d3b7974b`  |
| 2372   | No file              | `67a9d3b7974b`  |
| 2358   | No file              | `67a9d3b7974b`  |
| 2352   | No file              | `67a9d3b7974b`  |
| 2347   | No file              | `67a9d3b7974b`  |
| 2343   | No file              | `67a9d3b7974b`  |
| 2335   | No documented layout | `67a9d3b7974b`  |
| 2327   | No file              | `67a9d3b7974b`  |
| 2324   | No file              | `67a9d3b7974b`  |
| 2319   | No file              | `67a9d3b7974b`  |
| 2313   | No file              | `67a9d3b7974b`  |
| 2308   | No file              | `67a9d3b7974b`  |
| 2302   | No file              | `67a9d3b7974b`  |
| 2295   | No file              | `67a9d3b7974b`  |
| 2290   | No file              | `67a9d3b7974b`  |
| 2284   | No file              | `67a9d3b7974b`  |
| 2276   | No file              | `67a9d3b7974b`  |
| 2269   | No file              | `67a9d3b7974b`  |
| 2259   | No file              | `67a9d3b7974b`  |
| 2250   | No file              | `67a9d3b7974b`  |
| 2243   | No file              | `67a9d3b7974b`  |
| 2235   | No file              | `67a9d3b7974b`  |
| 2229   | No file              | `67a9d3b7974b`  |
| 2224   | No file              | `67a9d3b7974b`  |
| 2218   | No file              | `67a9d3b7974b`  |
| 2215   | No file              | `67a9d3b7974b`  |
| 2207   | No file              | `67a9d3b7974b`  |
| 2203   | No file              | `67a9d3b7974b`  |
| 2196   | No file              | `67a9d3b7974b`  |
| 2192   | No file              | `67a9d3b7974b`  |
| 2189   | No file              | `67a9d3b7974b`  |
| 2183   | No file              | `67a9d3b7974b`  |
| 2179   | No file              | `67a9d3b7974b`  |
| 2171   | No file              | `67a9d3b7974b`  |
| 2163   | No file              | `67a9d3b7974b`  |
| 2156   | No file              | `67a9d3b7974b`  |
| 2151   | No file              | `67a9d3b7974b`  |
| 2147   | No file              | `67a9d3b7974b`  |
| 2142   | No file              | `67a9d3b7974b`  |
| 2138   | No file              | `67a9d3b7974b`  |
| 2134   | No file              | `67a9d3b7974b`  |
| 2130   | No file              | `67a9d3b7974b`  |
| 2122   | No file              | `67a9d3b7974b`  |
| 2107   | No file              | `67a9d3b7974b`  |
| 2098   | No file              | `67a9d3b7974b`  |
| 2089   | No file              | `67a9d3b7974b`  |
| 2081   | No file              | `67a9d3b7974b`  |
| 2073   | No file              | `67a9d3b7974b`  |
| 2067   | No file              | `67a9d3b7974b`  |
| 2063   | No file              | `67a9d3b7974b`  |
| 2059   | No file              | `67a9d3b7974b`  |
| 2052   | No file              | `67a9d3b7974b`  |
| 2044   | No file              | `67a9d3b7974b`  |
| 2039   | No file              | `67a9d3b7974b`  |
| 2032   | No file              | `67a9d3b7974b`  |
| 2025   | No file              | `67a9d3b7974b`  |
| 2011   | No file              | `67a9d3b7974b`  |
| 2005   | No file              | `67a9d3b7974b`  |
| 2000   | No file              | `67a9d3b7974b`  |
| 1996   | No file              | `67a9d3b7974b`  |
| 1991   | No file              | `67a9d3b7974b`  |
| 1985   | No file              | `67a9d3b7974b`  |
| 1980   | No file              | `67a9d3b7974b`  |
| 1969   | No file              | `67a9d3b7974b`  |
| 1964   | No file              | `67a9d3b7974b`  |
| 1958   | No file              | `67a9d3b7974b`  |
| 1950   | No file              | `67a9d3b7974b`  |
| 1945   | No file              | `67a9d3b7974b`  |
| 1937   | No file              | `67a9d3b7974b`  |
| 1933   | No file              | `67a9d3b7974b`  |
| 1927   | No file              | `67a9d3b7974b`  |
| 1921   | No file              | `67a9d3b7974b`  |
| 1914   | No file              | `67a9d3b7974b`  |
| 1908   | No file              | `67a9d3b7974b`  |
| 1897   | No file              | `67a9d3b7974b`  |
| 1892   | No file              | `67a9d3b7974b`  |
| 1886   | No file              | `67a9d3b7974b`  |
| 1881   | No file              | `67a9d3b7974b`  |
| 1871   | No file              | `67a9d3b7974b`  |
| 1866   | No file              | `67a9d3b7974b`  |
| 1862   | No file              | `67a9d3b7974b`  |
| 1854   | No file              | `67a9d3b7974b`  |
| 1846   | No file              | `67a9d3b7974b`  |
| 1838   | No file              | `67a9d3b7974b`  |
| 1832   | No file              | `67a9d3b7974b`  |
| 1826   | No file              | `67a9d3b7974b`  |
| 1822   | No file              | `67a9d3b7974b`  |
| 1818   | No file              | `67a9d3b7974b`  |
| 1804   | No file              | `67a9d3b7974b`  |
| 1794   | No file              | `67a9d3b7974b`  |
| 1790   | No file              | `67a9d3b7974b`  |
| 1784   | Layout 1             | `67a9d3b7974b`  |
| 1774   | No file              | `67a9d3b7974b`  |
| 1771   | No file              | `67a9d3b7974b`  |
| 1762   | No file              | `67a9d3b7974b`  |
| 1759   | No file              | `67a9d3b7974b`  |
| 1754   | No file              | `67a9d3b7974b`  |
| 1749   | No file              | `67a9d3b7974b`  |
| 1743   | No file              | `67a9d3b7974b`  |
| 1737   | No file              | `67a9d3b7974b`  |
| 1731   | No file              | `67a9d3b7974b`  |
| 1725   | No file              | `67a9d3b7974b`  |
| 1717   | No file              | `67a9d3b7974b`  |
| 1710   | No file              | `67a9d3b7974b`  |
| 1704   | No file              | `67a9d3b7974b`  |
| 1698   | No file              | `67a9d3b7974b`  |
| 1690   | No file              | `67a9d3b7974b`  |
| 1685   | No file              | `67a9d3b7974b`  |
| 1680   | No file              | `67a9d3b7974b`  |
| 1674   | No file              | `67a9d3b7974b`  |
| 1668   | No file              | `67a9d3b7974b`  |
| 1659   | No file              | `67a9d3b7974b`  |
| 1649   | No file              | `67a9d3b7974b`  |
| 1642   | No file              | `67a9d3b7974b`  |
| 1636   | No file              | `67a9d3b7974b`  |
| 1628   | No file              | `67a9d3b7974b`  |
| 1622   | No file              | `67a9d3b7974b`  |
| 1614   | No file              | `67a9d3b7974b`  |
| 1608   | No file              | `67a9d3b7974b`  |
| 1602   | No file              | `67a9d3b7974b`  |
| 1598   | No file              | `67a9d3b7974b`  |
| 1594   | No file              | `67a9d3b7974b`  |
| 1590   | No file              | `67a9d3b7974b`  |
| 1587   | No file              | `67a9d3b7974b`  |
| 1584   | No file              | `67a9d3b7974b`  |
| 1579   | No file              | `67a9d3b7974b`  |
| 1572   | No file              | `67a9d3b7974b`  |
| 1565   | No file              | `67a9d3b7974b`  |
| 1559   | No file              | `67a9d3b7974b`  |
| 1554   | No file              | `67a9d3b7974b`  |
| 1547   | No file              | `67a9d3b7974b`  |
| 1537   | No file              | `67a9d3b7974b`  |
| 1529   | No file              | `67a9d3b7974b`  |
| 1524   | No file              | `67a9d3b7974b`  |
| 1519   | No file              | `67a9d3b7974b`  |
| 1509   | No file              | `67a9d3b7974b`  |
| 1506   | No file              | `67a9d3b7974b`  |
| 1504   | No file              | `67a9d3b7974b`  |
| 1500   | No file              | `67a9d3b7974b`  |
| 1493   | No file              | `67a9d3b7974b`  |
| 1489   | No file              | `67a9d3b7974b`  |
| 1485   | No file              | `67a9d3b7974b`  |
| 1481   | No file              | `67a9d3b7974b`  |
| 1474   | No file              | `67a9d3b7974b`  |
| 1466   | No file              | `67a9d3b7974b`  |
| 1462   | No file              | `67a9d3b7974b`  |
| 1459   | No file              | `67a9d3b7974b`  |
| 1453   | No file              | `67a9d3b7974b`  |
| 1450   | No file              | `67a9d3b7974b`  |
| 1445   | No file              | `67a9d3b7974b`  |
| 1439   | No file              | `67a9d3b7974b`  |
| 1433   | No file              | `67a9d3b7974b`  |
| 1430   | No file              | `67a9d3b7974b`  |
| 1426   | No file              | `67a9d3b7974b`  |
| 1421   | No file              | `67a9d3b7974b`  |
| 1417   | No file              | `67a9d3b7974b`  |
| 1416   | No file              | `67a9d3b7974b`  |
| 1409   | No file              | `67a9d3b7974b`  |
| 1405   | No file              | `67a9d3b7974b`  |
| 1401   | No file              | `67a9d3b7974b`  |
| 1396   | No file              | `67a9d3b7974b`  |
| 1391   | No file              | `67a9d3b7974b`  |
| 1390   | No file              | `67a9d3b7974b`  |
| 1386   | No file              | `67a9d3b7974b`  |
| 1381   | No file              | `67a9d3b7974b`  |
| 1379   | No file              | `67a9d3b7974b`  |
| 1372   | No file              | `67a9d3b7974b`  |
| 1366   | No file              | `67a9d3b7974b`  |
| 1364   | No file              | `67a9d3b7974b`  |
| 1363   | No file              | `67a9d3b7974b`  |
| 1360   | No file              | `67a9d3b7974b`  |
| 1358   | No file              | `67a9d3b7974b`  |
| 1355   | No file              | `67a9d3b7974b`  |
| 1351   | No file              | `67a9d3b7974b`  |
| 1348   | No file              | `67a9d3b7974b`  |
| 1346   | No file              | `67a9d3b7974b`  |
| 1341   | No file              | `67a9d3b7974b`  |
| 1340   | No file              | `67a9d3b7974b`  |
| 1338   | No file              | `67a9d3b7974b`  |
| 1335   | No file              | `67a9d3b7974b`  |
| 1333   | No file              | `67a9d3b7974b`  |
| 1329   | No file              | `67a9d3b7974b`  |
| 1327   | No file              | `67a9d3b7974b`  |
| 1324   | No file              | `67a9d3b7974b`  |
| 1321   | No file              | `67a9d3b7974b`  |
| 1319   | No file              | `67a9d3b7974b`  |
| 1318   | No file              | `67a9d3b7974b`  |
| 1316   | No file              | `67a9d3b7974b`  |
| 1313   | No file              | `67a9d3b7974b`  |
| 1311   | No file              | `67a9d3b7974b`  |
| 1309   | No file              | `67a9d3b7974b`  |
| 1304   | No file              | `67a9d3b7974b`  |
| 1292   | No file              | `67a9d3b7974b`  |
| 1286   | No file              | `67a9d3b7974b`  |
| 1280   | No file              | `67a9d3b7974b`  |
| 1276   | No file              | `67a9d3b7974b`  |
| 1267   | No file              | `67a9d3b7974b`  |
| 1261   | No file              | `67a9d3b7974b`  |
| 1256   | No file              | `67a9d3b7974b`  |
| 1250   | No file              | `67a9d3b7974b`  |
| 1246   | No file              | `67a9d3b7974b`  |
| 1239   | No file              | `67a9d3b7974b`  |
| 1230   | No file              | `67a9d3b7974b`  |
| 1226   | No file              | `67a9d3b7974b`  |
| 1220   | No file              | `67a9d3b7974b`  |
| 1217   | No file              | `67a9d3b7974b`  |
| 1211   | No file              | `67a9d3b7974b`  |
| 1210   | No file              | `67a9d3b7974b`  |
| 1208   | No file              | `67a9d3b7974b`  |
| 1203   | No file              | `67a9d3b7974b`  |
| 1197   | No file              | `67a9d3b7974b`  |
| 1194   | No file              | `67a9d3b7974b`  |
| 1192   | No file              | `67a9d3b7974b`  |
| 1187   | No file              | `67a9d3b7974b`  |
| 1183   | No file              | `67a9d3b7974b`  |
| 1177   | No file              | `67a9d3b7974b`  |
| 1173   | No file              | `67a9d3b7974b`  |
| 1167   | No file              | `67a9d3b7974b`  |
| 1164   | No file              | `67a9d3b7974b`  |
| 1156   | No file              | `67a9d3b7974b`  |
| 1149   | No file              | `67a9d3b7974b`  |
| 1144   | No file              | `67a9d3b7974b`  |
| 1137   | No file              | `67a9d3b7974b`  |
| 1132   | No file              | `67a9d3b7974b`  |
| 1127   | No file              | `67a9d3b7974b`  |
| 1122   | No file              | `67a9d3b7974b`  |
| 1118   | No file              | `67a9d3b7974b`  |
| 1114   | No file              | `67a9d3b7974b`  |
| 1109   | No file              | `67a9d3b7974b`  |
| 1102   | No file              | `67a9d3b7974b`  |
| 1096   | No file              | `67a9d3b7974b`  |
| 1088   | No file              | `67a9d3b7974b`  |
| 1081   | No file              | `67a9d3b7974b`  |
| 1076   | No file              | `67a9d3b7974b`  |
| 1069   | No file              | `67a9d3b7974b`  |
| 1064   | No file              | `67a9d3b7974b`  |
| 1058   | No file              | `67a9d3b7974b`  |
| 1051   | No file              | `67a9d3b7974b`  |
| 1044   | No file              | `67a9d3b7974b`  |
| 1036   | No file              | `67a9d3b7974b`  |
| 1026   | No file              | `67a9d3b7974b`  |
| 1016   | No file              | `67a9d3b7974b`  |
| 1009   | No file              | `67a9d3b7974b`  |
| 1005   | No file              | `67a9d3b7974b`  |
| 1000   | No file              | `67a9d3b7974b`  |
| 998    | No file              | `67a9d3b7974b`  |
| 990    | No file              | `67a9d3b7974b`  |
| 979    | No file              | `67a9d3b7974b`  |
| 972    | No file              | `67a9d3b7974b`  |
| 963    | No file              | `67a9d3b7974b`  |
| 955    | No file              | `67a9d3b7974b`  |
| 946    | No file              | `67a9d3b7974b`  |
| 938    | No file              | `67a9d3b7974b`  |
| 927    | No file              | `67a9d3b7974b`  |
| 911    | No file              | `67a9d3b7974b`  |
| 904    | No file              | `67a9d3b7974b`  |
| 899    | No file              | `67a9d3b7974b`  |
| 894    | No file              | `67a9d3b7974b`  |
| 885    | No file              | `67a9d3b7974b`  |
| 879    | No file              | `67a9d3b7974b`  |
| 872    | No file              | `67a9d3b7974b`  |
| 864    | No file              | `67a9d3b7974b`  |
| 855    | No file              | `67a9d3b7974b`  |
| 853    | No file              | `67a9d3b7974b`  |
| 845    | No file              | `67a9d3b7974b`  |
| 837    | No file              | `67a9d3b7974b`  |
| 829    | No file              | `67a9d3b7974b`  |
| 822    | No file              | `67a9d3b7974b`  |
| 814    | No file              | `67a9d3b7974b`  |
| 805    | No file              | `67a9d3b7974b`  |
| 794    | No file              | `67a9d3b7974b`  |
| 787    | No file              | `67a9d3b7974b`  |
| 780    | No file              | `67a9d3b7974b`  |
| 771    | No file              | `67a9d3b7974b`  |
| 760    | No file              | `67a9d3b7974b`  |
| 748    | No file              | `67a9d3b7974b`  |
| 741    | No file              | `67a9d3b7974b`  |
| 736    | No file              | `67a9d3b7974b`  |
| 731    | No file              | `67a9d3b7974b`  |
| 723    | No file              | `67a9d3b7974b`  |
| 711    | No file              | `67a9d3b7974b`  |
| 707    | No file              | `67a9d3b7974b`  |
| 697    | No file              | `67a9d3b7974b`  |
| 689    | No file              | `67a9d3b7974b`  |
| 683    | No file              | `67a9d3b7974b`  |
| 678    | No file              | `67a9d3b7974b`  |
| 670    | No file              | `67a9d3b7974b`  |
| 661    | No file              | `67a9d3b7974b`  |
| 656    | No file              | `67a9d3b7974b`  |
| 652    | No file              | `67a9d3b7974b`  |
| 643    | No file              | `67a9d3b7974b`  |
| 637    | No file              | `67a9d3b7974b`  |
| 630    | No file              | `67a9d3b7974b`  |
| 627    | No file              | `67a9d3b7974b`  |
| 621    | No file              | `67a9d3b7974b`  |
| 617    | No file              | `67a9d3b7974b`  |
| 615    | No file              | `67a9d3b7974b`  |
| 606    | No file              | `67a9d3b7974b`  |
| 599    | No file              | `67a9d3b7974b`  |
| 592    | No file              | `67a9d3b7974b`  |
| 586    | No file              | `67a9d3b7974b`  |
| 577    | No file              | `67a9d3b7974b`  |
| 569    | No file              | `67a9d3b7974b`  |
| 561    | No file              | `67a9d3b7974b`  |
| 554    | No file              | `67a9d3b7974b`  |
| 542    | No file              | `67a9d3b7974b`  |
| 532    | No file              | `67a9d3b7974b`  |
| 531    | No file              | `67a9d3b7974b`  |
| 526    | No file              | `67a9d3b7974b`  |
| 521    | No file              | `67a9d3b7974b`  |
| 517    | No file              | `67a9d3b7974b`  |
| 510    | No file              | `67a9d3b7974b`  |
| 508    | No file              | `67a9d3b7974b`  |
| 504    | No file              | `67a9d3b7974b`  |
| 497    | No file              | `67a9d3b7974b`  |
| 491    | No file              | `67a9d3b7974b`  |
| 485    | No file              | `67a9d3b7974b`  |
| 478    | No file              | `67a9d3b7974b`  |
| 472    | No file              | `67a9d3b7974b`  |
| 466    | No file              | `67a9d3b7974b`  |
| 457    | No file              | `67a9d3b7974b`  |
| 452    | No file              | `67a9d3b7974b`  |
| 449    | No file              | `67a9d3b7974b`  |
| 435    | No file              | `67a9d3b7974b`  |

<!-- versions:end -->

## Companion Files

| File | Required | Role |
| --- | --- | --- |
| [`actionchartheader.paach`](actionchartheader_paach.md) | Optional | Flag bytes per chart, keyed by the chart's path hash |
| `pc/pc_actionchartpackagepcraw.paac` | Optional | Shared condition records, frame events and elements of the `pc/` charts |
| [`pcactionpackagename.bss`](../bss/pcactionpackagename_bss.md) | Optional | Names the packages of the class charts by the same path hash |

All multi-byte values are little-endian. A `_ref` field is a u32 index into
the PABR string table at the end of the file. Every hash here is lookup3
`hashlittle` with seed `810718` (`0xC5EDE`) over the ASCII text.

## Layout 2

### File Layout

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | char[4] | magic | ASCII `PABR` |
| `+0x04` | u32 | version | `1`; the 1784 loader stops on any other value |
| `+0x08` | u8 | uses_shared_tables | `1` on every class chart. In the 1784 loader a chart whose path starts with `pc/` and has this set takes its condition records from `pc_actionchartpackagepcraw.paac` |
| `+0x09` | u64 | animation_count | |
| `+0x11` | Animation[animation_count] | animations | See Animation |
| `animations+0x00` | List Block | unknown_list_block | See List Block |
| `unknown_list_block+0x00` | u64 | skeleton_count | `1` on every chart checked |
| `unknown_list_block+0x08` | Skeleton[skeleton_count] | skeletons | See Skeleton |
| `skeletons+0x00` | u64 | unknown_pair_count | `0` on every chart checked |
| `skeletons+0x08` | String Pair[unknown_pair_count] | unknown_pairs | See String Pair |
| `unknown_pairs+0x00` | u64 | mesh_group_count | |
| `unknown_pairs+0x08` | Mesh Group[mesh_group_count] | mesh_groups | See Mesh Group |
| `mesh_groups+0x00` | u64 | effect_count | |
| `mesh_groups+0x08` | Effect[effect_count] | effects | See Effect |
| `effects+0x00` | u64 | unknown_entry_count | |
| `effects+0x08` | Keyed Entry[unknown_entry_count] | unknown_entries | See Keyed Entry |
| `unknown_entries+0x00` | u64 | unknown_row_count | |
| `unknown_entries+0x08` | Unknown Row[unknown_row_count] | unknown_rows | See Unknown Row |
| `unknown_rows+0x00` | u32 | unknown_str_ref | A name such as `PC_FX_2_Ranger` or `Object_Script_CashShop` |
| `unknown_rows+0x04` | u32 | unknown_rows_04 | |
| `unknown_rows+0x08` | u8 | str_ref_count | |
| `unknown_rows+0x09` | u32[str_ref_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u32 | unknown_str_refs_00 | |
| `unknown_str_refs+0x04` | Slot Entry[42] | slots | Always 42 entries; the 1784 loader reads 32. See Slot Entry |
| `slots+0x00` | u8 | has_hit_parts | |
| `slots+0x01` | Hit Parts if has_hit_parts = 1 | hit_parts | See Hit Parts |
| `hit_parts+0x00` | u64 | condition_count | `0` on the class charts, which use the shared records |
| `hit_parts+0x08` | Condition Record[condition_count] | conditions | See Condition Record |
| `conditions+0x00` | u32 | event_count | `0` on the class charts |
| `conditions+0x04` | Frame Event[event_count] | events | See Frame Event |
| `events+0x00` | u64 | package_count | 139 or 140 on a class chart, `1` on the other charts checked |
| `events+0x08` | Package[package_count] | packages | See Package |
| `packages+0x00` | u32 | version_end | `1`; the 1784 loader checks it like `version` |
| `packages+0x04` | String Table | string_table | See String Table |
| `EOF-0x08` | u32 | table_start | Offset of the string table |
| `EOF-0x04` | u32 | zero | Always `0` |

### `pc_actionchartpackagepcraw.paac`

`character/binaryactionchart/pc/pc_actionchartpackagepcraw.paac`, the shared
tables of the class charts; Layout 1 has the whole file. On client 3483 the
condition records read as on client 1784 (101,452 of them); the frame events
after them do not yet (see Open Questions), so the rest of the file is one
unknown block here.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | char[4] | magic | ASCII `PABR` |
| `+0x04` | u32 | version | `1` |
| `+0x08` | u64 | condition_count | |
| `+0x10` | Condition Record[condition_count] | conditions | |
| `conditions+0x00` | u8[..table_start] | unknown_events_and_elements | The u32 event count, the frame events, the element groups and the trailing version `1` |
| `unknown_events_and_elements+0x00` | String Table | string_table | |
| `EOF-0x08` | u32 | table_start | Offset of the string table |
| `EOF-0x04` | u32 | zero | Always `0` |

### Animation (variable: 24 bytes + lists and events)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | name_hash | Hash of the text at `name_ref` (`Ani_Start` is `0x137D2BFB`) |
| `+0x04` | u32 | unknown_str_ref_04 | `DEFAULT` on the entries checked |
| `+0x08` | u32 | name_ref | Animation name, such as `Ani_Att_Shoot` |
| `+0x0C` | u32 | clip_ref | `.paa` clip path, such as `1_PC/3_PEW/PEW_00_01_BS_Att_Shoot_00.paa` |
| `+0x10` | u16 | unknown_10 | |
| `+0x12` | bytes[24] if unknown_10 != 0 | unknown_12 | Starts with `name_hash` on the entries checked |
| `unknown_12+0x00` | u8 | has_u32_list | |
| `unknown_12+0x01` | U32 List if has_u32_list = 1 | unknown_u32_list | Starts with `name_hash` on the entries checked |
| `unknown_u32_list+0x00` | u8 | has_u64_list | |
| `unknown_u32_list+0x01` | U64 List if has_u64_list = 1 | unknown_u64_list | |
| `unknown_u64_list+0x00` | u32 | event_count | |
| `unknown_u64_list+0x04` | Animation Event[event_count] | events | See Animation Event |

### U32 List (variable: 8 bytes + values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | value_count | |
| `+0x08` | u32[value_count] | values | |

### U64 List (variable: 8 bytes + values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | value_count | |
| `+0x08` | u64[value_count] | values | `0` on the entries checked |

### Animation Event (36 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u16 | unknown_08 | |
| `+0x0A` | u16 | unknown_0a | |
| `+0x0C` | u16 | unknown_0c | |
| `+0x0E` | u32 | mesh_ref | A `.pac` path, such as `1_pc/3_pew/armor/9_upperbody/pew_10_ub_0009.pac` |
| `+0x12` | u16 | unknown_12 | |
| `+0x14` | u32 | unknown_14 | `0xFFFFFFFF` on the entries checked |
| `+0x18` | u32 | unknown_18 | `0xFFFFFFFF` on the entries checked |
| `+0x1C` | bytes[8] | unknown_1c | `0`; not in the 1784 loader |

### List Block (variable: 12 bytes + lists)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | first_count | |
| `+0x04` | List Pair[first_count] | first_pairs | |
| `first_pairs+0x00` | u32 | second_count | |
| `first_pairs+0x04` | List Pair[second_count] | second_pairs | |
| `second_pairs+0x00` | u32 | group_count | |
| `second_pairs+0x04` | List Group[group_count] | groups | |

### List Pair (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_04 | |

### List Group (variable: 12 bytes + entries and weights)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | entry_count | |
| `+0x08` | List Entry[entry_count] | entries | |
| `entries+0x00` | u32 | weight_count | |
| `entries+0x04` | List Weight[weight_count] | weights | |

### List Entry (12 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u16 | unknown_08 | |
| `+0x0A` | u16 | unknown_0a | |

### List Weight (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | f32 | unknown_04 | |

### Skeleton (variable: 32 bytes + rows and parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | `0` on the charts checked |
| `+0x04` | u32 | unknown_str_ref_04 | `DEFAULT` on the charts checked |
| `+0x08` | u32 | skeleton_ref | `.pab` skeleton path, such as `12_Cash/C0000_Pearl/C0000_01.pab` |
| `+0x0C` | u32 | unknown_str_ref_0c | Empty text on the charts checked |
| `+0x10` | u64 | row_count | |
| `+0x18` | Skeleton Row[row_count] | rows | |
| `rows+0x00` | u64 | parameter_size | `30` on the charts checked |
| `rows+0x08` | bytes[parameter_size] | unknown_parameters | Starts with f32 `0.3`, `1.0`, `1.0`, `-1.0`, `-1.0` on the cash chart |

### Skeleton Row (54 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[54] | unknown_00 | |

### String Pair (12 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |

### Mesh Group (variable: 24 bytes + parts and parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | `0` on the charts checked |
| `+0x04` | u32 | unknown_str_ref_04 | `DEFAULT` on the charts checked |
| `+0x08` | u64 | part_count | |
| `+0x10` | Mesh Part[part_count] | parts | |
| `parts+0x00` | u64 | parameter_size | |
| `parts+0x08` | bytes[parameter_size] | unknown_parameters | |

### Mesh Part (variable: 16 bytes + parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | part_name_ref | A part name, such as `base_body` |
| `+0x04` | u32 | mesh_ref | The part's `.pac` path |
| `+0x08` | u64 | parameter_size | `18` on the parts checked |
| `+0x10` | bytes[parameter_size] | unknown_parameters | Starts with three `FF FF FF 00` words on the parts checked |

### Effect (variable: 4 bytes + effect)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | Effect Data | data | |

### Effect Data (variable: 132 bytes + attachments)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | effect_name_ref | Such as `ChainLightning01_PPM` |
| `+0x04` | u32 | unknown_str_ref_04 | Such as `CO_Empty` or `M_Sea_Summon_WaterBall_01` |
| `+0x08` | u64 | parameter_size | `116` on every effect read (93,857 effect events of the 1784 PcRaw file included), except four leftover charts of client 1784 with `106` (see Notes); the loader copies the bytes over a fixed block of the effect object |
| `+0x10` | bytes[112] | unknown_10 | Starts with f32 `1.0`, `1.0`, `1.0` |
| `+0x80` | u8 | attachment_count | Byte `0x70` of the parameters; the loader reads this many attachments |
| `+0x81` | bytes[3] | unknown_81 | |
| `+0x84` | Effect Attachment[attachment_count] | attachments | |

### Effect Attachment (56 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[48] | unknown_00 | Four groups of 12 bytes in the 1784 loader; f32 values |
| `+0x30` | u32 | bone_ref | A bone name, such as `Bip01` or `Bip01 Spine1`, or empty |
| `+0x34` | u32 | unknown_34 | f32 `1.0` on the attachments checked |

### Keyed Entry (variable: 4 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | i32 | key | |
| `+0x04` | Keyed Data if key != -1 | data | |

### Keyed Data (22 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32[4] | unknown_04 | |
| `+0x14` | u8 | unknown_14 | |
| `+0x15` | u8 | unknown_15 | |

### Unknown Row (20 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[20] | unknown_00 | Two u32 hashes then zeros on many rows |

### Slot Entry (variable: 1 byte + slot)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | has_slot | |
| `+0x01` | Slot if has_slot = 1 | slot | |

### Slot (120 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32[8] | unknown_00 | Read as eight u32; f32 `20.0`, `10.0` and `2.0` in some |
| `+0x20` | u8[42] | unknown_20 | One byte per slot index; 32 bytes in the 1784 loader |
| `+0x4A` | u8[42] | unknown_4a | One byte per slot index; 32 bytes in the 1784 loader |
| `+0x74` | u8[4] | unknown_74 | |

### Hit Parts (variable: 16 bytes + groups and bones)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | group_count | |
| `+0x08` | Hit Part Group[group_count] | groups | |
| `groups+0x00` | u64 | bone_count | |
| `groups+0x08` | u32[bone_count] | bone_refs | Every bone the groups name, sorted by name |

### Hit Part Group (variable: 16 bytes + parts)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | `0xFF00FFFF`, `0xFFFFFFFF`, `0xFFFF0000` or `0xFF00FF00`, colour-like |
| `+0x04` | u32 | unknown_04 | f32 such as `0.4` or `0.05`, or `0` |
| `+0x08` | u64 | part_count | |
| `+0x10` | Hit Part[part_count] | parts | |

### Hit Part (33 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | bone_ref | Such as `Bip01 Spine1` or `B_Mouth_UL` |
| `+0x04` | f32 | unknown_04 | `400.0`, `100.0`, `10.0` |
| `+0x08` | bytes[12] | unknown_08 | |
| `+0x14` | u32 | unknown_14 | Index of `bone_ref` in `bone_refs` on the charts checked |
| `+0x18` | u8 | unknown_18 | `0` to `3` |
| `+0x19` | u32 | unknown_19 | `1000000`, `15000000`, `45000000`, `120000000`; not in the 1784 loader |
| `+0x1D` | u32 | unknown_1d | `0`, `10` or `30`; not in the 1784 loader |

### Condition Record (variable: 19 bytes + sets and data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | has_byte_sets | |
| `+0x01` | Byte Sets if has_byte_sets = 1 | byte_sets | |
| `byte_sets+0x00` | u8 | set_count | |
| `byte_sets+0x01` | Condition Set[set_count] | sets | |
| `sets+0x00` | u32 | unknown_str_ref_a | An action name, such as `WAIT` |
| `sets+0x04` | u32 | unknown_str_ref_b | An action name or empty text |
| `sets+0x08` | u8 | has_unknown_extra | |
| `sets+0x09` | bytes[12] if has_unknown_extra = 1 | unknown_extra | |
| `unknown_extra+0x00` | u64 | data_size | `23` on the records checked |
| `unknown_extra+0x08` | bytes[data_size] | unknown_data | |

### Byte Sets (variable: 8 bytes + lists)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | Byte List if unknown_00 != 0 | first_list | |
| `first_list+0x00` | u32 | unknown_first_list_00 | |
| `first_list+0x04` | Byte List if unknown_first_list_00 != 0 | second_list | |

### Byte List (variable: 8 bytes + values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | value_count | |
| `+0x08` | u8[value_count] | values | |

### Condition Set (variable: 8 bytes + lists)

The 1784 client's `ge::ActionConditionSet_Client`.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | U16 List if unknown_00 != 0 | condition_list | `RFBConArr` in the 1784 loader |
| `condition_list+0x00` | Wide List if unknown_04 != 0 | extra_condition_list | `RFBConExArr` in the 1784 loader |

### U16 List (variable: 8 bytes + values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | value_count | |
| `+0x08` | u16[value_count] | values | |

### Wide List (variable: 8 bytes + values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | value_count | |
| `+0x08` | u8[value_count][16] | values | 16 bytes each |

### Frame Event (variable: 20 bytes + sets and type fields)

The fields after the sets depend on `type`; see Frame Event Types. On client 3483 only the types with events in the last column of that table are checked; the others are read as on client 1784.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | type | See Frame Event Types |
| `+0x01` | u32 | unknown_str_ref_01 | |
| `+0x05` | u64 | base_size | `7` on every event read |
| `+0x0D` | f32 | unknown_0d | `1.0`, `12.0`, `20.0` |
| `+0x11` | u8 | unknown_11 | |
| `+0x12` | u8 | unknown_12 | |
| `+0x13` | u8 | set_count | |
| `+0x14` | Condition Set[set_count] | sets | |
| `sets+0x00` | Attack Fields if type = 0 or type = 155 | attack_fields | |
| `attack_fields+0x00` | Attack Skill Fields if type = 1 | attack_skill_fields | |
| `attack_skill_fields+0x00` | Attack Arrow Fields if type = 2 | attack_arrow_fields | |
| `attack_arrow_fields+0x00` | Attack Arrow Skill Fields if type = 3 | attack_arrow_skill_fields | |
| `attack_arrow_skill_fields+0x00` | Attack Catch Fields if type = 4 | attack_catch_fields | |
| `attack_catch_fields+0x00` | Attack Throw Fields if type = 5 | attack_throw_fields | |
| `attack_throw_fields+0x00` | Effect Fields if type = 6 | effect_fields | |
| `effect_fields+0x00` | Effect Ground Fields if type = 7 | effect_ground_fields | |
| `effect_ground_fields+0x00` | Switch Fields if type = 8 | switch_fields | |
| `switch_fields+0x00` | Switch Chain Fields if type = 9 | switch_chain_fields | |
| `switch_chain_fields+0x00` | Switch Target Fields if type = 10 | switch_target_fields | |
| `switch_target_fields+0x00` | Switch Change Fields if type = 12 | switch_change_fields | |
| `switch_change_fields+0x00` | Data Fields if type = 14 or type = 15 or type = 16 or type = 17 or type = 27 or type = 40 or type = 41 or type = 42 or type = 43 or type = 44 or type = 45 or type = 75 or type = 76 or type = 85 or type = 87 or type = 88 or type = 89 or type = 90 or type = 92 or type = 93 or type = 94 or type = 125 or type = 130 or type = 144 or type = 165 or type = 166 or type = 167 | data_fields | |
| `data_fields+0x00` | Camera Motion Fields if type = 18 | camera_motion_fields | |
| `camera_motion_fields+0x00` | Camera Pulse Fields if type = 19 | camera_pulse_fields | |
| `camera_pulse_fields+0x00` | Name Fields if type = 20 or type = 21 or type = 22 or type = 74 | name_fields | |
| `name_fields+0x00` | Bubble Fields if type = 23 | bubble_fields | |
| `bubble_fields+0x00` | Value Fields if type = 24 or type = 30 or type = 31 or type = 77 or type = 79 or type = 81 or type = 99 or type = 100 or type = 108 or type = 115 or type = 117 or type = 118 or type = 158 or type = 159 or type = 168 | value_fields | |
| `value_fields+0x00` | Two Value Fields if type = 25 or type = 26 or type = 68 or type = 69 or type = 119 or type = 138 or type = 139 | two_value_fields | |
| `two_value_fields+0x00` | Name Data Fields if type = 28 or type = 47 or type = 66 or type = 67 or type = 164 | name_data_fields | |
| `name_data_fields+0x00` | Sword Trail Fields if type = 29 | sword_trail_fields | |
| `sword_trail_fields+0x00` | Mesh Fields if type = 33 or type = 34 | mesh_fields | |
| `mesh_fields+0x00` | Jump Fields if type = 35 | jump_fields | |
| `jump_fields+0x00` | Weapon Fields if type = 36 or type = 37 | weapon_fields | |
| `weapon_fields+0x00` | Weapon Mesh Fields if type = 38 or type = 39 | weapon_mesh_fields | |
| `weapon_mesh_fields+0x00` | Glitter Fields if type = 46 | glitter_fields | |
| `glitter_fields+0x00` | Sound Kill Fields if type = 48 | sound_kill_fields | |
| `sound_kill_fields+0x00` | Sound Fields if type = 49 or type = 50 or type = 51 or type = 53 or type = 54 or type = 55 or type = 56 or type = 57 or type = 58 or type = 59 or type = 60 or type = 61 or type = 62 or type = 63 or type = 64 or type = 65 | sound_fields | |
| `sound_fields+0x00` | Sound External Fields if type = 52 | sound_external_fields | |
| `sound_external_fields+0x00` | Camera Fields if type = 78 or type = 80 | camera_fields | |
| `camera_fields+0x00` | Byte Fields if type = 82 or type = 84 or type = 116 or type = 124 or type = 128 or type = 157 | byte_fields | |
| `byte_fields+0x00` | Additive Fields if type = 83 | additive_fields | |
| `additive_fields+0x00` | Two Byte Fields if type = 101 or type = 162 | two_byte_fields | |
| `two_byte_fields+0x00` | Lua Event Fields if type = 111 | lua_event_fields | |
| `lua_event_fields+0x00` | Decal Fields if type = 112 | decal_fields | |
| `decal_fields+0x00` | Light Fields if type = 120 or type = 123 or type = 142 | light_fields | |
| `light_fields+0x00` | Weather Fields if type = 121 | weather_fields | |
| `weather_fields+0x00` | Pose Fields if type = 129 | pose_fields | |
| `pose_fields+0x00` | Attack Bounds Fields if type = 134 | attack_bounds_fields | |
| `attack_bounds_fields+0x00` | Cannon Predict Fields if type = 135 | cannon_predict_fields | |
| `cannon_predict_fields+0x00` | Wave Fields if type = 137 | wave_fields | |
| `wave_fields+0x00` | Model Animation Fields if type = 140 | model_animation_fields | |
| `model_animation_fields+0x00` | Attack Skill Simple Fields if type = 145 | attack_skill_simple_fields | |
| `attack_skill_simple_fields+0x00` | Attack Arrow Skill Simple Fields if type = 146 | attack_arrow_skill_simple_fields | |
| `attack_arrow_skill_simple_fields+0x00` | Client Attack Fields if type = 152 | client_attack_fields | |
| `client_attack_fields+0x00` | Grenade Fields if type = 154 | grenade_fields | |
| `grenade_fields+0x00` | Grenade Path Fields if type = 156 | grenade_path_fields | |
| `grenade_path_fields+0x00` | Battle FX Fields if type = 161 | battle_fx_fields | |
| `battle_fx_fields+0x00` | Cutscene Fields if type = 169 | cutscene_fields | |
| `cutscene_fields+0x00` | Play Animation Fields if type = 171 | play_animation_fields | |

### Client Attack Fields (38 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | unknown_00 | |
| `+0x01` | u32 | unknown_01 | |
| `+0x05` | bytes[24] | unknown_05 | |
| `+0x1D` | bytes[8] | unknown_1d | |
| `+0x25` | u8 | unknown_25 | |

### Attack Fields (variable: 24 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |

### Attack Arrow Fields (variable: 60 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u32 | unknown_unknown_first_data_00 | |
| `unknown_first_data+0x04` | u32 | unknown_unknown_first_data_04 | |
| `unknown_first_data+0x08` | u32 | unknown_unknown_first_data_08 | |
| `unknown_first_data+0x0C` | u32 | unknown_unknown_first_data_0c | |
| `unknown_first_data+0x10` | u32 | unknown_unknown_first_data_10 | |
| `unknown_first_data+0x14` | u32 | unknown_unknown_first_data_14 | |
| `unknown_first_data+0x18` | u32 | unknown_unknown_first_data_18 | |
| `unknown_first_data+0x1C` | u64 | second_data_size | |
| `unknown_first_data+0x24` | bytes[second_data_size] | unknown_second_data | |

### Attack Arrow Skill Fields (variable: 70 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u32 | unknown_unknown_first_data_00 | |
| `unknown_first_data+0x04` | u32 | unknown_unknown_first_data_04 | |
| `unknown_first_data+0x08` | u32 | unknown_unknown_first_data_08 | |
| `unknown_first_data+0x0C` | u32 | unknown_unknown_first_data_0c | |
| `unknown_first_data+0x10` | u32 | unknown_unknown_first_data_10 | |
| `unknown_first_data+0x14` | u32 | unknown_unknown_first_data_14 | |
| `unknown_first_data+0x18` | u32 | unknown_unknown_first_data_18 | |
| `unknown_first_data+0x1C` | u64 | second_data_size | |
| `unknown_first_data+0x24` | bytes[second_data_size] | unknown_second_data | |
| `unknown_second_data+0x00` | u64 | third_data_size | |
| `unknown_second_data+0x08` | bytes[third_data_size] | unknown_third_data | |
| `unknown_third_data+0x00` | u8 | unknown_unknown_third_data_00 | |
| `unknown_third_data+0x01` | u8 | unknown_unknown_third_data_01 | |

### Attack Arrow Skill Simple Fields (variable: 76 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u32 | unknown_unknown_first_data_00 | |
| `unknown_first_data+0x04` | u32 | unknown_unknown_first_data_04 | |
| `unknown_first_data+0x08` | u32 | unknown_unknown_first_data_08 | |
| `unknown_first_data+0x0C` | u32 | unknown_unknown_first_data_0c | |
| `unknown_first_data+0x10` | u32 | unknown_unknown_first_data_10 | |
| `unknown_first_data+0x14` | u32 | unknown_unknown_first_data_14 | |
| `unknown_first_data+0x18` | u32 | unknown_unknown_first_data_18 | |
| `unknown_first_data+0x1C` | u64 | second_data_size | |
| `unknown_first_data+0x24` | bytes[second_data_size] | unknown_second_data | |
| `unknown_second_data+0x00` | u64 | third_data_size | |
| `unknown_second_data+0x08` | bytes[third_data_size] | unknown_third_data | |
| `unknown_third_data+0x00` | u64 | list_count | |
| `unknown_third_data+0x08` | U32 List[list_count] | unknown_lists | |

### Attack Catch Fields (variable: 33 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u32 | unknown_unknown_first_data_00 | |
| `unknown_first_data+0x04` | u32 | unknown_unknown_first_data_04 | |
| `unknown_first_data+0x08` | u8 | unknown_unknown_first_data_08 | |

### Attack Skill Fields (variable: 33 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u64 | second_data_size | |
| `unknown_first_data+0x08` | bytes[second_data_size] | unknown_second_data | |
| `unknown_second_data+0x00` | u8 | unknown_unknown_second_data_00 | |

### Attack Skill Simple Fields (variable: 40 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u64 | first_data_size | |
| `+0x18` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u64 | second_data_size | |
| `unknown_first_data+0x08` | bytes[second_data_size] | unknown_second_data | |
| `unknown_second_data+0x00` | u64 | list_count | |
| `unknown_second_data+0x08` | U32 List[list_count] | unknown_lists | |

### Attack Throw Fields (10 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u16 | unknown_00 | |
| `+0x02` | u16 | unknown_02 | |
| `+0x04` | u16 | unknown_04 | |
| `+0x06` | u16 | unknown_06 | |
| `+0x08` | u16 | unknown_08 | |

### Battle FX Fields (16 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[12] | unknown_00 | |
| `+0x0C` | u32 | unknown_0c | |

### Data Fields (variable: 8 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | first_data_size | |
| `+0x08` | bytes[first_data_size] | unknown_first_data | |

### Camera Fields (variable: 9 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | first_data_size | |
| `+0x08` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u8 | unknown_unknown_first_data_00 | |

### Bubble Fields (5 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u8 | unknown_04 | |

### Cannon Predict Fields (variable: 41 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u8 | unknown_0c | |
| `+0x0D` | bytes[16] | unknown_0d | |
| `+0x1D` | u32 | unknown_1d | |
| `+0x21` | u64 | first_data_size | |
| `+0x29` | bytes[first_data_size] | unknown_first_data | |

### Cutscene Fields (9 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | unknown_00 | |
| `+0x01` | u32 | unknown_str_ref_01 | |
| `+0x05` | u32 | unknown_05 | |

### Decal Fields (variable: 13 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u64 | first_data_size | |
| `+0x0C` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u8 | unknown_unknown_first_data_00 | |

### Switch Fields (variable: 3 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | name_count | |
| `+0x01` | u32[name_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u8 | unknown_unknown_str_refs_00 | |
| `unknown_str_refs+0x01` | u8 | unknown_unknown_str_refs_01 | |

### Switch Chain Fields (variable: 24 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | name_count | |
| `+0x01` | u32[name_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u8 | unknown_unknown_str_refs_00 | |
| `unknown_str_refs+0x01` | u8 | unknown_unknown_str_refs_01 | |
| `unknown_str_refs+0x02` | u32 | unknown_unknown_str_refs_02 | |
| `unknown_str_refs+0x06` | u32 | unknown_unknown_str_refs_06 | |
| `unknown_str_refs+0x0A` | u32 | unknown_unknown_str_refs_0a | |
| `unknown_str_refs+0x0E` | u64 | first_data_size | |
| `unknown_str_refs+0x16` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u8 | unknown_unknown_first_data_00 | |

### Switch Change Fields (10 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u8 | unknown_08 | |
| `+0x09` | u8 | unknown_09 | |

### Switch Target Fields (variable: 4 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | name_count | |
| `+0x01` | u32[name_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u8 | unknown_unknown_str_refs_00 | |
| `unknown_str_refs+0x01` | u8 | unknown_unknown_str_refs_01 | |
| `unknown_str_refs+0x02` | u8 | unknown_unknown_str_refs_02 | |

### Glitter Fields (17 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[12] | unknown_00 | |
| `+0x0C` | u32 | unknown_str_ref_0c | |
| `+0x10` | u8 | unknown_10 | |

### Grenade Fields (48 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | bytes[12] | unknown_04 | |
| `+0x10` | u32 | unknown_10 | |
| `+0x14` | u32 | unknown_14 | |
| `+0x18` | u32 | unknown_18 | |
| `+0x1C` | bytes[12] | unknown_1c | |
| `+0x28` | u32 | unknown_28 | |
| `+0x2C` | u32 | unknown_2c | |

### Jump Fields (5 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u8 | unknown_04 | |

### Light Fields (21 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[12] | unknown_00 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u32 | unknown_str_ref_10 | |
| `+0x14` | u8 | unknown_14 | |

### Lua Event Fields (14 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u8 | unknown_0c | |
| `+0x0D` | u8 | unknown_0d | |

### Mesh Fields (variable: 6 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | name_count | |
| `+0x01` | u32[name_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u32 | unknown_unknown_str_refs_00 | |
| `unknown_str_refs+0x04` | u8 | unknown_unknown_str_refs_04 | |

### Model Animation Fields (28 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u32 | unknown_10 | |
| `+0x14` | u32 | unknown_14 | |
| `+0x18` | u32 | unknown_18 | |

### Play Animation Fields (20 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u32 | unknown_10 | |

### Pose Fields (25 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u32 | unknown_10 | |
| `+0x14` | u32 | unknown_14 | |
| `+0x18` | u8 | unknown_18 | |

### Grenade Path Fields (29 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | bytes[12] | unknown_10 | |
| `+0x1C` | u8 | unknown_1c | |

### Camera Motion Fields (12 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[12] | unknown_00 | |

### Camera Pulse Fields (84 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[84] | unknown_00 | |

### Sound External Fields (variable: 12 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | first_data_size | |
| `+0x08` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u32 | unknown_unknown_first_data_00 | |

### Name Fields (4 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |

### Name Data Fields (variable: 12 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u64 | first_data_size | |
| `+0x0C` | bytes[first_data_size] | unknown_first_data | |

### Additive Fields (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_04 | |

### Sword Trail Fields (variable: 24 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | u64 | first_data_size | |
| `+0x10` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u64 | second_data_size | |
| `unknown_first_data+0x08` | bytes[second_data_size] | unknown_second_data | |

### Value Fields (4 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |

### Two Value Fields (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |

### Byte Fields (1 byte)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | unknown_00 | |

### Two Byte Fields (2 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | unknown_00 | |
| `+0x01` | u8 | unknown_01 | |

### Wave Fields (24 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u32 | unknown_10 | |
| `+0x14` | u32 | unknown_14 | |

### Weapon Fields (variable: 1 byte + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | value_count | |
| `+0x01` | u8[value_count] | unknown_values | |

### Weapon Mesh Fields (variable: 2 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | value_count | |
| `+0x01` | u8[value_count] | unknown_values | |
| `unknown_values+0x00` | u8 | unknown_unknown_values_00 | |

### Weather Fields (20 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[16] | unknown_00 | |
| `+0x10` | u32 | unknown_10 | |

### Attack Bounds Fields (variable: 41 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | first_data_size | |
| `+0x08` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | bytes[33] | unknown_unknown_first_data_00 | |

### Effect Fields (variable: 3 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | Effect Data | effect | |
| `effect+0x00` | u8 | unknown_effect_00 | |
| `effect+0x01` | u8 | unknown_effect_01 | |
| `effect+0x02` | u8 | unknown_effect_02 | |

### Effect Ground Fields (variable: 12 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | Effect Data | effect | |
| `effect+0x00` | u8 | unknown_effect_00 | |
| `effect+0x01` | u8 | unknown_effect_01 | |
| `effect+0x02` | u8 | unknown_effect_02 | |
| `effect+0x03` | u32 | unknown_effect_03 | |
| `effect+0x07` | u32 | unknown_effect_07 | |
| `effect+0x0B` | u8 | unknown_effect_0b | |

### Sound Fields (variable: 12 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u64 | first_data_size | |
| `+0x0C` | bytes[first_data_size] | unknown_first_data | |

### Sound Kill Fields (1 byte)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | unknown_00 | |

### Package (variable: 150 bytes + groups, branches and actions)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | package_hash | Hash of the `package_path_ref` text; the `package_hash` of [`pcactionpackagename.bss`](../bss/pcactionpackagename_bss.md) |
| `+0x04` | u8 | unknown_04 | `1` on every class chart package |
| `+0x05` | u8 | unknown_05 | `1` on every class chart package. When this and `unknown_04` are not 0, the actions carry no element |
| `+0x06` | u32 | package_path_ref | The package path, such as `pc/vehicle/riding_ground/horse/elfaction_ridinghorse`; its hash is the key |
| `+0x0A` | u32[10] | unknown_str_refs_0a | Action names, such as `WAIT` |
| `+0x32` | u16 | unknown_32 | Up to about `0x0F00` |
| `+0x34` | u8 | unknown_34 | `0` or `5` |
| `+0x35` | u8 | unknown_35 | `0` |
| `+0x36` | u32 | unknown_36 | `0`, `1` or `2`. The 1784 loader reads u16, three u8 and u32 here, one byte more |
| `+0x3A` | u64 | key_group_count | |
| `+0x42` | Key Group[key_group_count] | key_groups | |
| `key_groups+0x00` | u64 | pair_count | |
| `key_groups+0x08` | Key Pair[pair_count] | pairs | |
| `pairs+0x00` | u64 | branch_count | |
| `pairs+0x08` | Branch[branch_count] | branches | |
| `branches+0x00` | u64 | action_count | |
| `branches+0x08` | Action[action_count] if unknown_04 != 0 and unknown_05 != 0 | actions | See Action |
| `actions+0x00` | Action With Element[action_count] if unknown_04 = 0 or unknown_05 = 0 | element_actions | See Action With Element |
| `element_actions+0x00` | bytes[60] | unknown_tail | `0` on 4,353 of the 4,452 class chart packages (client 3483) |

### Key Group (variable: 12 bytes + entries)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | key | |
| `+0x04` | u64 | entry_count | |
| `+0x0C` | Key Entry[entry_count] | entries | |

### Key Entry (16 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | key | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u32 | unknown_str_ref_08 | |
| `+0x0C` | u32 | unknown_0c | |

### Key Pair (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | key | |
| `+0x04` | u32 | unknown_04 | |

### Branch (variable: 20 bytes + indexes and rows)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u64 | condition_count | |
| `+0x08` | i32[condition_count] | condition_indexes | Index of a Condition Record; into `pc_actionchartpackagepcraw.paac` when `uses_shared_tables` applies (1784 loader) |
| `condition_indexes+0x00` | u64 | row_count | |
| `condition_indexes+0x08` | Branch Row[row_count] | rows | |
| `rows+0x00` | u32 | unknown_str_ref_rows_00 | |

### Branch Row (10 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u16 | unknown_04 | |
| `+0x06` | u16 | unknown_06 | `0xFFFF` on many rows |
| `+0x08` | u16 | unknown_08 | `0xFFFF` on many rows |

### Action (variable: 78 bytes + lists and data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | action_hash | Hash of the action name (`WAIT` is `0x95E46D94`); the cash chart's 10 keys are the hashes of its 10 `CASHSHOP_*` and `WAIT` names |
| `+0x04` | u64 | first_count | |
| `+0x0C` | i32[first_count] | unknown_first_values | |
| `unknown_first_values+0x00` | u64 | second_count | |
| `unknown_first_values+0x08` | u32[second_count] | unknown_second_values | |
| `unknown_second_values+0x00` | u64 | third_count | |
| `unknown_second_values+0x08` | u16[third_count] | unknown_third_values | |
| `unknown_third_values+0x00` | u64 | fourth_count | |
| `unknown_third_values+0x08` | Action Row A[fourth_count] | unknown_fourth_rows | |
| `unknown_fourth_rows+0x00` | u64 | fifth_count | |
| `unknown_fourth_rows+0x08` | u16[fifth_count][2] | unknown_fifth_rows | |
| `unknown_fifth_rows+0x00` | u64 | sixth_count | |
| `unknown_fifth_rows+0x08` | Action Row B[sixth_count] | unknown_sixth_rows | |
| `unknown_sixth_rows+0x00` | u32 | unknown_sixth_rows_00 | |
| `unknown_sixth_rows+0x04` | u32 | unknown_sixth_rows_04 | |
| `unknown_sixth_rows+0x08` | u64 | first_data_size | `16` on every class chart action |
| `unknown_sixth_rows+0x10` | bytes[first_data_size] | unknown_first_data | |
| `unknown_first_data+0x00` | u16 | unknown_first_data_00 | |
| `unknown_first_data+0x02` | u64 | second_data_size | `18` on every class chart action (client 3483); `19` in Layout 1 |
| `unknown_first_data+0x0A` | bytes[second_data_size] | unknown_second_data | Its first 16 bytes look like the Layout 1 Element Link (u32 `+0x04` is `0` on all 22,251 actions of `elfmanaction_noweapon.paac`, client 3483); not checked against the shared elements, which Layout 2 does not read yet |

### Action Row A (8 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u16 | unknown_00 | |
| `+0x02` | u16 | unknown_02 | |
| `+0x04` | u32 | unknown_04 | |

### Action Row B (22 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | i32 | unknown_00 | |
| `+0x04` | u16 | unknown_04 | |
| `+0x06` | u16 | unknown_06 | |
| `+0x08` | u32 | unknown_08 | |
| `+0x0C` | u32 | unknown_0c | |
| `+0x10` | u16 | unknown_10 | |
| `+0x12` | u16 | unknown_12 | |
| `+0x14` | u16 | unknown_14 | |

### Action With Element (variable: 0 bytes + action and element)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | Action | action | |
| `action+0x00` | Element | element | |

### Element (variable: 93 bytes + items and parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | action_name_ref | The action's name; its hash is the Action's `action_hash` |
| `+0x04` | u32 | animation_ref | The name of an Animation of the same chart |
| `+0x08` | u32[11] | unknown_str_refs_08 | |
| `+0x34` | u32 | unknown_str_ref_34 | |
| `+0x38` | bytes[12] | unknown_38 | |
| `+0x44` | u32 | item_count | |
| `+0x48` | Element Item[item_count] | unknown_items | |
| `unknown_items+0x00` | u32 | unknown_items_00 | |
| `unknown_items+0x04` | u64 | unknown_items_04 | |
| `unknown_items+0x0C` | u8 | unknown_items_0c | `0x5F` on the elements checked |
| `unknown_items+0x0D` | u64 | parameter_size | |
| `unknown_items+0x15` | bytes[parameter_size] | unknown_parameters | |

### Element Item (17 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[17] | unknown_00 | |

### String Table (variable: 4 bytes + strings)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | string_count | |
| `+0x04` | pstr[string_count] | strings | Narrow (`is_wide` `0`) on the charts checked |

## Layout 1

Client 1784, the layout the 1784 loader reads. The structures below differ
from Layout 2; every other structure is the same.

A class chart Action has no element of its own: its Element Link names the
element in `pc_actionchartpackagepcraw.paac`. The named fields of the Action
Data, Element Link and Element Parameters were matched against a private
server's per-weapon summaries for client 1784, joined by action name, on
`elfmanaction_noweapon.paac` (Archer, 4,126 actions with a summary entry) and
`elfaction_noweapon.paac` (Ranger, 5,046). The counts in their Notes are
"Archer / Ranger" and come from client 1784.

### File Layout

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | char[4] | magic | ASCII `PABR` |
| `+0x04` | u32 | version | `1`; the 1784 loader stops on any other value |
| `+0x08` | u8 | uses_shared_tables | See Layout 2 |
| `+0x09` | u64 | animation_count | |
| `+0x11` | Animation[animation_count] | animations | See Animation |
| `animations+0x00` | List Block | unknown_list_block | |
| `unknown_list_block+0x00` | u64 | skeleton_count | |
| `unknown_list_block+0x08` | Skeleton[skeleton_count] | skeletons | See Skeleton |
| `skeletons+0x00` | u64 | unknown_pair_count | |
| `skeletons+0x08` | String Pair[unknown_pair_count] | unknown_pairs | |
| `unknown_pairs+0x00` | u64 | mesh_group_count | |
| `unknown_pairs+0x08` | Mesh Group[mesh_group_count] | mesh_groups | See Mesh Group |
| `mesh_groups+0x00` | u64 | effect_count | |
| `mesh_groups+0x08` | Effect[effect_count] | effects | |
| `effects+0x00` | u64 | unknown_entry_count | |
| `effects+0x08` | Keyed Entry[unknown_entry_count] | unknown_entries | |
| `unknown_entries+0x00` | u64 | unknown_row_count | |
| `unknown_entries+0x08` | Unknown Row[unknown_row_count] | unknown_rows | |
| `unknown_rows+0x00` | u32 | unknown_str_ref | |
| `unknown_rows+0x04` | u32 | unknown_rows_04 | |
| `unknown_rows+0x08` | u8 | str_ref_count | |
| `unknown_rows+0x09` | u32[str_ref_count] | unknown_str_refs | |
| `unknown_str_refs+0x00` | u32 | unknown_str_refs_00 | |
| `unknown_str_refs+0x04` | Slot Entry[32] | slots | 32 entries on client 1784 |
| `slots+0x00` | u8 | has_hit_parts | |
| `slots+0x01` | Hit Parts if has_hit_parts = 1 | hit_parts | |
| `hit_parts+0x00` | u64 | condition_count | |
| `hit_parts+0x08` | Condition Record[condition_count] | conditions | |
| `conditions+0x00` | u32 | event_count | |
| `conditions+0x04` | Frame Event[event_count] | events | See Frame Event |
| `events+0x00` | u64 | package_count | |
| `events+0x08` | Package[package_count] | packages | See Package |
| `packages+0x00` | u32 | version_end | `1` |
| `packages+0x04` | String Table | string_table | |
| `EOF-0x08` | u32 | table_start | Offset of the string table |
| `EOF-0x04` | u32 | zero | Always `0` |

### `pc_actionchartpackagepcraw.paac`

`character/binaryactionchart/pc/pc_actionchartpackagepcraw.paac`, the shared
tables of the class charts (1784 loader `0x1417d3200`). On client 1784 it
holds 87,411 condition records, 299,518 frame events and 76,993 elements in
585 groups (125,206,586 bytes).

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | char[4] | magic | ASCII `PABR` |
| `+0x04` | u32 | version | `1` |
| `+0x08` | u64 | condition_count | The records a class chart's Branch `condition_indexes` point at |
| `+0x10` | Condition Record[condition_count] | conditions | |
| `conditions+0x00` | u32 | event_count | |
| `conditions+0x04` | Frame Event[event_count] | events | |
| `events+0x00` | u64 | element_group_count | |
| `events+0x08` | Element Group[element_group_count] | element_groups | |
| `element_groups+0x00` | u32 | version_end | `1` |
| `element_groups+0x04` | String Table | string_table | |
| `EOF-0x08` | u32 | table_start | Offset of the string table |
| `EOF-0x04` | u32 | zero | Always `0` |

### Element Group (variable: 12 bytes + elements)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | key | 64 of the 585 keys are `pcactionpackagename.bss` package hashes (client 1784); a class chart Action's `element_group_key` |
| `+0x04` | u64 | element_count | |
| `+0x0C` | Element[element_count] | elements | |

### Animation (variable: 20 bytes + lists and events)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | name_hash | |
| `+0x04` | u32 | name_ref | |
| `+0x08` | u32 | clip_ref | |
| `+0x0C` | u16 | unknown_10 | |
| `+0x0E` | bytes[24] if unknown_10 != 0 | unknown_12 | |
| `unknown_12+0x00` | u8 | has_u32_list | |
| `unknown_12+0x01` | U32 List if has_u32_list = 1 | unknown_u32_list | |
| `unknown_u32_list+0x00` | u8 | has_u64_list | |
| `unknown_u32_list+0x01` | U64 List if has_u64_list = 1 | unknown_u64_list | |
| `unknown_u64_list+0x00` | u32 | event_count | |
| `unknown_u64_list+0x04` | Animation Event[event_count] | events | |

### Animation Event (28 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | unknown_04 | |
| `+0x08` | u16 | unknown_08 | |
| `+0x0A` | u16 | unknown_0a | |
| `+0x0C` | u16 | unknown_0c | |
| `+0x0E` | u32 | mesh_ref | |
| `+0x12` | u16 | unknown_12 | |
| `+0x14` | u32 | unknown_14 | |
| `+0x18` | u32 | unknown_18 | |

### Skeleton (variable: 28 bytes + rows and parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u32 | skeleton_ref | |
| `+0x08` | u32 | unknown_str_ref_0c | |
| `+0x0C` | u64 | row_count | |
| `+0x14` | Skeleton Row[row_count] | rows | |
| `rows+0x00` | u64 | parameter_size | |
| `rows+0x08` | bytes[parameter_size] | unknown_parameters | |

### Mesh Group (variable: 20 bytes + parts and parameters)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_00 | |
| `+0x04` | u64 | part_count | |
| `+0x0C` | Mesh Part[part_count] | parts | |
| `parts+0x00` | u64 | parameter_size | |
| `parts+0x08` | bytes[parameter_size] | unknown_parameters | |

### Slot (100 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32[8] | unknown_00 | |
| `+0x20` | u8[32] | unknown_20 | |
| `+0x40` | u8[32] | unknown_4a | |
| `+0x60` | u8[4] | unknown_74 | |

### Hit Part (25 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | bone_ref | |
| `+0x04` | f32 | unknown_04 | |
| `+0x08` | bytes[12] | unknown_08 | |
| `+0x14` | u32 | unknown_14 | |
| `+0x18` | u8 | unknown_18 | |

### Package (variable: 151 bytes + groups, branches and actions)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | package_hash | |
| `+0x04` | u8 | unknown_04 | |
| `+0x05` | u8 | unknown_05 | |
| `+0x06` | u32 | package_path_ref | |
| `+0x0A` | u32[10] | unknown_str_refs_0a | |
| `+0x32` | u16 | unknown_32 | |
| `+0x34` | u8 | unknown_34 | |
| `+0x35` | u8 | unknown_35 | |
| `+0x36` | u8 | unknown_after_unknown_35 | One of the three u8 here is gone on client 3483; which one is not known |
| `+0x37` | u32 | unknown_36 | |
| `+0x3B` | u64 | key_group_count | |
| `+0x43` | Key Group[key_group_count] | key_groups | |
| `key_groups+0x00` | u64 | pair_count | |
| `key_groups+0x08` | Key Pair[pair_count] | pairs | |
| `pairs+0x00` | u64 | branch_count | |
| `pairs+0x08` | Branch[branch_count] | branches | |
| `branches+0x00` | u64 | action_count | |
| `branches+0x08` | Action[action_count] if unknown_04 != 0 and unknown_05 != 0 | actions | |
| `actions+0x00` | Action With Element[action_count] if unknown_04 = 0 or unknown_05 = 0 | element_actions | |
| `element_actions+0x00` | bytes[60] | unknown_tail | |

### Action (variable: 78 bytes + lists and data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | action_hash | |
| `+0x04` | u64 | first_count | |
| `+0x0C` | i32[first_count] | unknown_first_values | |
| `unknown_first_values+0x00` | u64 | second_count | |
| `unknown_first_values+0x08` | u32[second_count] | unknown_second_values | |
| `unknown_second_values+0x00` | u64 | third_count | |
| `unknown_second_values+0x08` | u16[third_count] | unknown_third_values | |
| `unknown_third_values+0x00` | u64 | fourth_count | |
| `unknown_third_values+0x08` | Action Row A[fourth_count] | unknown_fourth_rows | |
| `unknown_fourth_rows+0x00` | u64 | fifth_count | |
| `unknown_fourth_rows+0x08` | u16[fifth_count][2] | unknown_fifth_rows | |
| `unknown_fifth_rows+0x00` | u64 | sixth_count | |
| `unknown_fifth_rows+0x08` | Action Row B[sixth_count] | unknown_sixth_rows | |
| `unknown_sixth_rows+0x00` | u32 | unknown_sixth_rows_00 | |
| `unknown_sixth_rows+0x04` | u32 | unknown_sixth_rows_04 | |
| `unknown_sixth_rows+0x08` | u64 | first_data_size | `16` on all 38,937 actions of the two charts |
| `unknown_sixth_rows+0x10` | Action Data if first_data_size = 16 | action_data | |
| `action_data+0x00` | bytes[first_data_size] if first_data_size != 16 | unknown_first_data | |
| `unknown_first_data+0x00` | u16 | unknown_first_data_00 | |
| `unknown_first_data+0x02` | u64 | second_data_size | `19` on all 38,937 |
| `unknown_first_data+0x0A` | Element Link if second_data_size = 19 | element_link | |
| `element_link+0x00` | bytes[second_data_size] if second_data_size != 19 | unknown_second_data | |

### Action Data (16 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | f32 | move_speed | The summary's `MoveSpeed` on 439 of 492 / 458 of 509 |
| `+0x04` | f32 | move_speed_dup | Same value as `move_speed` on all 38,937 actions |
| `+0x08` | f32 | frame_count | The action's length in frames at 30 fps: `frame_count * 1000 / 30` is the summary's `TotalFrame` in ms, within 1, on 4,038 of 4,126 / 4,901 of 5,046 |
| `+0x0C` | u32 | unknown_0c | `0` on 20,476 of the 38,937 |

### Element Link (19 bytes)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | element_index | Index of the action's Element in its Element Group, counted in file order. The element's `action_name` is the action's name on every action of the five class charts checked (`1_phm`, `3_pew`, `8_pwm` both, `9_pem`: 18,925 to 20,012 each) |
| `+0x04` | u32 | unknown_04 | `0` on all 38,937 |
| `+0x08` | u32 | weapon_type | The summary's `WeaponType` on 1,333 of 1,333 / 2,224 of 2,224 |
| `+0x0C` | u32 | element_group_key | The `key` of the Element Group in `pc_actionchartpackagepcraw.paac` |
| `+0x10` | bytes[3] | unknown_10 | `0` on all 38,937 |

### Frame Event (variable: 20 bytes + sets and type fields)

The fields after the sets depend on `type`; see Frame Event Types.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u8 | type | See Frame Event Types |
| `+0x01` | u32 | unknown_str_ref_01 | |
| `+0x05` | u64 | base_size | `7` on every event read |
| `+0x0D` | f32 | unknown_0d | `1.0`, `12.0`, `20.0` |
| `+0x11` | u8 | unknown_11 | |
| `+0x12` | u8 | unknown_12 | |
| `+0x13` | u8 | set_count | |
| `+0x14` | Condition Set[set_count] | sets | |
| `sets+0x00` | Attack Fields if type = 0 or type = 155 | attack_fields | |
| `attack_fields+0x00` | Attack Skill Fields if type = 1 | attack_skill_fields | |
| `attack_skill_fields+0x00` | Attack Arrow Fields if type = 2 | attack_arrow_fields | |
| `attack_arrow_fields+0x00` | Attack Arrow Skill Fields if type = 3 | attack_arrow_skill_fields | |
| `attack_arrow_skill_fields+0x00` | Attack Catch Fields if type = 4 | attack_catch_fields | |
| `attack_catch_fields+0x00` | Attack Throw Fields if type = 5 | attack_throw_fields | |
| `attack_throw_fields+0x00` | Effect Fields if type = 6 | effect_fields | |
| `effect_fields+0x00` | Effect Ground Fields if type = 7 | effect_ground_fields | |
| `effect_ground_fields+0x00` | Switch Fields if type = 8 | switch_fields | |
| `switch_fields+0x00` | Switch Chain Fields if type = 9 | switch_chain_fields | |
| `switch_chain_fields+0x00` | Switch Target Fields if type = 10 | switch_target_fields | |
| `switch_target_fields+0x00` | Switch Change Fields if type = 12 | switch_change_fields | |
| `switch_change_fields+0x00` | Data Fields if type = 14 or type = 15 or type = 16 or type = 17 or type = 27 or type = 40 or type = 41 or type = 42 or type = 43 or type = 44 or type = 45 or type = 48 or type = 49 or type = 50 or type = 51 or type = 53 or type = 54 or type = 55 or type = 56 or type = 57 or type = 58 or type = 59 or type = 60 or type = 61 or type = 62 or type = 63 or type = 64 or type = 65 or type = 75 or type = 76 or type = 85 or type = 87 or type = 88 or type = 89 or type = 90 or type = 92 or type = 93 or type = 94 or type = 125 or type = 130 or type = 134 or type = 144 or type = 165 or type = 166 or type = 167 | data_fields | |
| `data_fields+0x00` | Camera Motion Fields if type = 18 | camera_motion_fields | |
| `camera_motion_fields+0x00` | Camera Pulse Fields if type = 19 | camera_pulse_fields | |
| `camera_pulse_fields+0x00` | Name Fields if type = 20 or type = 21 or type = 22 or type = 74 | name_fields | |
| `name_fields+0x00` | Bubble Fields if type = 23 | bubble_fields | |
| `bubble_fields+0x00` | Value Fields if type = 24 or type = 30 or type = 31 or type = 77 or type = 79 or type = 81 or type = 99 or type = 100 or type = 108 or type = 115 or type = 117 or type = 118 or type = 158 or type = 159 or type = 168 | value_fields | |
| `value_fields+0x00` | Two Value Fields if type = 25 or type = 26 or type = 68 or type = 69 or type = 119 or type = 138 or type = 139 | two_value_fields | |
| `two_value_fields+0x00` | Name Data Fields if type = 28 or type = 47 or type = 66 or type = 67 or type = 164 | name_data_fields | |
| `name_data_fields+0x00` | Sword Trail Fields if type = 29 | sword_trail_fields | |
| `sword_trail_fields+0x00` | Mesh Fields if type = 33 or type = 34 | mesh_fields | |
| `mesh_fields+0x00` | Jump Fields if type = 35 | jump_fields | |
| `jump_fields+0x00` | Weapon Fields if type = 36 or type = 37 | weapon_fields | |
| `weapon_fields+0x00` | Weapon Mesh Fields if type = 38 or type = 39 | weapon_mesh_fields | |
| `weapon_mesh_fields+0x00` | Glitter Fields if type = 46 | glitter_fields | |
| `glitter_fields+0x00` | Sound External Fields if type = 52 | sound_external_fields | |
| `sound_external_fields+0x00` | Camera Fields if type = 78 or type = 80 | camera_fields | |
| `camera_fields+0x00` | Byte Fields if type = 82 or type = 84 or type = 116 or type = 124 or type = 128 or type = 157 | byte_fields | |
| `byte_fields+0x00` | Additive Fields if type = 83 | additive_fields | |
| `additive_fields+0x00` | Two Byte Fields if type = 101 or type = 162 | two_byte_fields | |
| `two_byte_fields+0x00` | Lua Event Fields if type = 111 | lua_event_fields | |
| `lua_event_fields+0x00` | Decal Fields if type = 112 | decal_fields | |
| `decal_fields+0x00` | Light Fields if type = 120 or type = 123 or type = 142 | light_fields | |
| `light_fields+0x00` | Weather Fields if type = 121 | weather_fields | |
| `weather_fields+0x00` | Pose Fields if type = 129 | pose_fields | |
| `pose_fields+0x00` | Cannon Predict Fields if type = 135 | cannon_predict_fields | |
| `cannon_predict_fields+0x00` | Wave Fields if type = 137 | wave_fields | |
| `wave_fields+0x00` | Model Animation Fields if type = 140 | model_animation_fields | |
| `model_animation_fields+0x00` | Attack Skill Simple Fields if type = 145 | attack_skill_simple_fields | |
| `attack_skill_simple_fields+0x00` | Attack Arrow Skill Simple Fields if type = 146 | attack_arrow_skill_simple_fields | |
| `attack_arrow_skill_simple_fields+0x00` | Client Attack Fields if type = 152 | client_attack_fields | |
| `client_attack_fields+0x00` | Grenade Fields if type = 154 | grenade_fields | |
| `grenade_fields+0x00` | Grenade Path Fields if type = 156 | grenade_path_fields | |
| `grenade_path_fields+0x00` | Battle FX Fields if type = 161 | battle_fx_fields | |
| `battle_fx_fields+0x00` | Cutscene Fields if type = 169 | cutscene_fields | |
| `cutscene_fields+0x00` | Play Animation Fields if type = 171 | play_animation_fields | |

### Effect Fields (variable: 2 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | Effect Data | effect | |
| `effect+0x00` | u8 | unknown_effect_00 | |
| `effect+0x01` | u8 | unknown_effect_01 | |

### Effect Ground Fields (variable: 10 bytes + data)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | Effect Data | effect | |
| `effect+0x00` | u8 | unknown_effect_00 | |
| `effect+0x01` | u8 | unknown_effect_01 | |
| `effect+0x02` | u32 | unknown_effect_02 | |
| `effect+0x06` | u32 | unknown_effect_06 | |

### Element (variable: 80 bytes + records and parameters)

The 1784 loader `0x1417c7230`. On client 1784, 20,283 elements of the
class and object charts and the 76,993 of the PcRaw file read with it.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | action_name_ref | The action's name; its hash is the Action's `action_hash` on all 7,747 elements of 200 charts checked |
| `+0x04` | u32 | animation_ref | The name of an Animation of the same chart on all 7,747 of them |
| `+0x08` | u32[11] | unknown_str_refs_08 | The loader stores the eighth before the seventh |
| `+0x34` | u32 | unknown_34 | |
| `+0x38` | u32[2] | unknown_str_refs_38 | |
| `+0x40` | u64 | record_count | |
| `+0x48` | Element Record[record_count] | records | |
| `records+0x00` | u64 | parameter_size | At most `0x158` in the loader; `337` on all 76,993 elements of the PcRaw file |
| `records+0x08` | Element Parameters if parameter_size = 337 | parameters | |
| `parameters+0x00` | bytes[parameter_size] if parameter_size != 337 | unknown_parameters | |

### Element Record (variable: 13 bytes + set and values)

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | u32 | unknown_str_ref_00 | |
| `+0x04` | u32 | unknown_str_ref_04 | |
| `+0x08` | Condition Set | set | |
| `set+0x00` | u32 | unknown_set_00 | |
| `set+0x04` | u8 | value_count | |
| `set+0x05` | u8[value_count] | values | |

### Element Parameters (337 bytes)

The summary attribute each field matches is in its Notes; the enum values
are in the table after this one.

| Offset | Type | Field | Notes |
| --- | --- | --- | --- |
| `+0x00` | bytes[8] | unknown_00 | |
| `+0x08` | f32 | start_frame | `StartFrame` on 687 of 697 / 922 of 925 |
| `+0x0C` | f32 | end_frame | `EndFrame` on 1,163 of 1,196 / 1,252 of 1,265; `-1` on 2,925 of the 2,930 / 3,777 of the 3,781 without one |
| `+0x10` | f32 | animation_speed | `AnimationSpeed` on 1,746 of 1,796 / 2,392 of 2,432 |
| `+0x14` | bytes[8] | unknown_14 | |
| `+0x1C` | f32 | rotation | `Rotation` in minus radians (90 is `-pi/2`) on 574 of 575 / 640 of 640 |
| `+0x20` | bytes[36] | unknown_20 | |
| `+0x44` | i32 | unknown_44 | `-1` on 4,078 of the 4,082 / 4,769 of the 4,990 without a `StartAvoidTime`, but equal to it on only 18 of 44 / 45 of 56 |
| `+0x48` | i32 | unknown_48 | `-1` on 4,078 of the 4,082 / 4,769 of the 4,990 without an `EndAvoidTime`, but equal to it on only 18 of 44 / 37 of 56 |
| `+0x4C` | bytes[88] | unknown_4c | |
| `+0xA4` | f32 | animation_speed_dup | Same value as `animation_speed` on all 76,993 elements of the PcRaw file |
| `+0xA8` | bytes[64] | unknown_a8 | |
| `+0xE8` | i32 | skill_no | `SkillNo` on 313 of 314 / 477 of 477; `0` on 62,269 of the 76,993 elements |
| `+0xEC` | bytes[8] | unknown_ec | |
| `+0xF4` | i32 | apply_sp | `ApplySp` on 334 of 334 / 440 of 531; `0` on all 3,792 Archer actions without one |
| `+0xF8` | bytes[25] | unknown_f8 | |
| `+0x111` | u8 | unknown_111 | `0` on 76,981 of the 76,993 |
| `+0x112` | u8 | unknown_112 | `10` on all 76,993, as `RandomNumberRange` is in every summary entry; a constant, so not named |
| `+0x113` | u8 | unknown_113 | `0` on all 76,993 |
| `+0x114` | u8 | action_type | `ActionType` on 4,108 of 4,126 / 5,028 of 5,046; the misses are the 14 `Slope` actions and 4 others |
| `+0x115` | u8 | move_direction | `MoveDirection` on 4,089 of 4,095 / 5,030 of 5,032 named values |
| `+0x116` | u8 | sp_use_type | `SpUseType` on 872 of 879 / 1,224 of 1,320 |
| `+0x117` | bytes[6] | unknown_117 | |
| `+0x11D` | u8 | apply_speed_buff_type | `ApplySpeedBuffType` on 1,151 of 1,170 / 2,152 of 2,158 |
| `+0x11E` | bytes[23] | unknown_11e | |
| `+0x135` | u8 | navigation_type | Bit flags of `NavigationType` on 4,108 of 4,126 / 5,036 of 5,046 |
| `+0x136` | bytes[11] | unknown_136 | |
| `+0x141` | u8 | item_access_level | `ItemAccessLevel` on 587 of 587 / 702 of 702 |
| `+0x142` | bytes[15] | unknown_142 | |

The enum values below are the ones the matched actions use, unless the row
names another source.

| Field | Values |
| --- | --- |
| `action_type` | `Move` 0, `ForcedMove` 1, `Attack` 2, `ArrowAttack` 3, `Skill` 4, `ArrowSkill` 5, `CombineWave` 6, `Defence` 7, `Misc` 8, `Catch` 9, `Collect` 10, `Product_Prepare` 11, `Product_Failed` 12, `Product_Start` 13, `Product_Wait` 14, `Product_Progress` 15, `Product_Finish` 16, `RideOn_Prepare` 17, `RideOn_Failed` 19, `RideOff_Do` 21, `Arrest_Target` 30, `Die` 31, `Build_Tent` 34, `TakeDown_Tent` 35, `MiniGame17` 53, `UseItem` 58, `Manufacture` 59, `ClimbWall1` 60, `ClimbWall2` 61, `ClimbWall3` 62, `RepairItem` 64, `Taming_Start` 65, `Taming_Step1` 66, `Taming_Step2` 67, `Taming_End` 68, `ReadBook` 69, `Campfire` 70, `SwimmingStep` 71, `CanntSwimmingStep` 72, `UseInstallation_Prepare` 73, `UseInstallation_Do` 74, `UseInstallation_Failed` 75, `UsingInstallation` 76, `FinishUseInstallation` 77, `WaitIdle` 78, `Takedown_Cannon` 81, `SummonCharacter` 82, `Alchemy` 83, `Commond_Repair` 84, `ActiveSkill` 85, `Building_Upgrade` 86, `Banquet` 91, `DefencePose` 94, `Training` 95, `GrenadePrepare` 101, `GrenadeStart` 103, `Build_Tent_Kit` 105, `IceFishingMiniGame` 106 |
| `move_direction` | `Foward` 0, `Foward_Direction` 2, `Backward_Direction` 3, `Foward_Direction_Fix` 4, `Backward_Direction_Fix` 5, `Foward_Camera_Direction` 8 (the server's spelling) |
| `sp_use_type` | `Once` 0, `Continue` 1, `Recover` 2, `Stop` 3, `Reset` 4, `None` 5, the order of the server code's `ESpUseType`. The matched actions use 0, 1 and 3; `Recover` 2 is on 3,247 of 3,247 / 3,698 of 3,726 actions whose entry has no `SpUseType` |
| `apply_speed_buff_type` | `Move` 0, `Attack` 1, `Cast` 2, `None` 3, the order of the server code's `EApplySpeedBuffType`. The matched actions use 0 and 1; `None` 3 is on all 2,956 / 2,888 actions whose entry has none |
| `navigation_type` | `air` 0x01, `wall` 0x02, `reserved0` 0x04, `reserved1` 0x08, `ground` 0x10, `under_ground` 0x20, `water` 0x40, `under_water` 0x80 |

## Frame Event Types

The type picks the event's class and the fields after the condition sets.
The 1784 client names the classes (`ge::ActionChart_FrameEvent_*`, 172
types from `0x00` to `0xAB`). Client 3483 uses the same ids: on 312 charts
whose event lists have the same length on both clients, every event of
client 3483 starts with the type of the event at the same place on client
1784. Five readers changed between the two clients (Effect, Effect Ground,
the sound types, Sound Kill and Attack Bounds); the other types checked on
client 3483 have the 1784 fields. A type with no events in the last column
is not checked on client 3483.

The fields on client 1784 are the 1784 loader's, and the 1784 PcRaw file
and 724 of the 728 class and object charts of that client read with them
to their last byte (see Notes for the other four).

| Type | Class (1784 client) | Fields on client 1784 | Fields on client 3483 | Events in the 1784 PcRaw file | Events checked on client 3483 |
| --- | --- | --- | --- | --- | --- |
| `0x00` | `ge::ActionChart_FrameEvent_Attack` | Attack Fields | Attack Fields | 1,081 | 4 |
| `0x01` | `ge::ActionChart_FrameEvent_AttackSkill` | Attack Skill Fields | Attack Skill Fields | 98,088 | 424 |
| `0x02` | `ge::ActionChart_FrameEvent_AttackArrow` | Attack Arrow Fields | Attack Arrow Fields | 686 | 0 |
| `0x03` | `ge::ActionChart_FrameEvent_AttackArrowSkill` | Attack Arrow Skill Fields | Attack Arrow Skill Fields | 20,606 | 45 |
| `0x04` | `ge::ActionChart_FrameEvent_AttackCatch` | Attack Catch Fields | Attack Catch Fields | 88 | 0 |
| `0x05` | `ge::ActionChart_FrameEvent_AttackThrow` | Attack Throw Fields | Attack Throw Fields | 42 | 0 |
| `0x06` | `ge::ActionChart_FrameEvent_Effect` | Effect Fields | Effect Fields | 93,658 | 3,786 |
| `0x07` | `ge::ActionChart_FrameEvent_EffectGround` | Effect Ground Fields | Effect Ground Fields | 199 | 95 |
| `0x08` | `ge::ActionChart_FrameEvent_EffectSwitch` | Switch Fields | Switch Fields | 3,100 | 217 |
| `0x09` | `ge::ActionChart_FrameEvent_EffectSwitchChain` | Switch Chain Fields | Switch Chain Fields | 498 | 0 |
| `0x0A` | `ge::ActionChart_FrameEvent_EffectSwitchTarget` | Switch Target Fields | Switch Target Fields | 18 | 0 |
| `0x0B` | `ge::ActionChart_FrameEvent_EffectSwitchTargetAllOff` | none | none | 3 | 0 |
| `0x0C` | `ge::ActionChart_FrameEvent_EffectSwitchChange` | Switch Change Fields | Switch Change Fields | 0 | 0 |
| `0x0D` | `ge::ActionChart_FrameEvent_EffectSwitchAllOff` | none | none | 1 | 0 |
| `0x0E` | `ge::ActionChart_FrameEvent_CharacterEffect` | Data Fields | Data Fields | 6,418 | 482 |
| `0x0F` | `ge::ActionChart_FrameEvent_GrassShake` | Data Fields | Data Fields | 102 | 0 |
| `0x10` | `ge::ActionChart_FrameEvent_CameraShake` | Data Fields | Data Fields | 6,073 | 435 |
| `0x11` | `ge::ActionChart_FrameEvent_CameraDirShake` | Data Fields | Data Fields | 44 | 17 |
| `0x12` | `ge::ActionChart_FrameEvent_CameraMotion` | Camera Motion Fields | Camera Motion Fields | 26 | 0 |
| `0x13` | `ge::ActionChart_FrameEvent_CameraPulse` | Camera Pulse Fields | Camera Pulse Fields | 0 | 0 |
| `0x14` | `ge::ActionChart_FrameEvent_OrderToSummon` | Name Fields | Name Fields | 471 | 0 |
| `0x15` | `ge::ActionChart_FrameEvent_OrderToHorse` | Name Fields | Name Fields | 3 | 0 |
| `0x16` | `ge::ActionChart_FrameEvent_OrderToRideVehicle` | Name Fields | Name Fields | 40 | 0 |
| `0x17` | `ge::ActionChart_FrameEvent_ShowBubbleBox` | Bubble Fields | Bubble Fields | 43 | 4 |
| `0x18` | `ge::ActionChart_FrameEvent_Delay` | Value Fields | Value Fields | 19 | 0 |
| `0x19` | `ge::ActionChart_FrameEvent_AnimationSpeed` | Two Value Fields | Two Value Fields | 2,378 | 171 |
| `0x1A` | `ge::ActionChart_FrameEvent_Speed` | Two Value Fields | Two Value Fields | 6,762 | 1,082 |
| `0x1B` | `ge::ActionChart_FrameEvent_Rotate` | Data Fields | Data Fields | 179 | 134 |
| `0x1C` | `ge::ActionChart_FrameEvent_Variable` | Name Data Fields | Name Data Fields | 961 | 58 |
| `0x1D` | `ge::ActionChart_FrameEvent_SwordTrail` | Sword Trail Fields | Sword Trail Fields | 1,146 | 25 |
| `0x1E` | `ge::ActionChart_FrameEvent_BounceBack` | Value Fields | Value Fields | 2 | 0 |
| `0x1F` | `ge::ActionChart_FrameEvent_PushBack` | Value Fields | Value Fields | 0 | 0 |
| `0x20` | `ge::ActionChart_FrameEvent_PickItemDropList` | none | none | 3 | 0 |
| `0x21` | `ge::ActionChart_FrameEvent_MeshOn` | Mesh Fields | Mesh Fields | 654 | 291 |
| `0x22` | `ge::ActionChart_FrameEvent_MeshOff` | Mesh Fields | Mesh Fields | 802 | 370 |
| `0x23` | `ge::ActionChart_FrameEvent_Jump` | Jump Fields | Jump Fields | 355 | 6 |
| `0x24` | `ge::ActionChart_FrameEvent_WeaponIn` | Weapon Fields | Weapon Fields | 403 | 0 |
| `0x25` | `ge::ActionChart_FrameEvent_WeaponOut` | Weapon Fields | Weapon Fields | 359 | 0 |
| `0x26` | `ge::ActionChart_FrameEvent_WeaponMeshOn` | Weapon Mesh Fields | Weapon Mesh Fields | 392 | 0 |
| `0x27` | `ge::ActionChart_FrameEvent_WeaponMeshOff` | Weapon Mesh Fields | Weapon Mesh Fields | 371 | 0 |
| `0x28` | `ge::ActionChart_FrameEvent_PointBlur` | Data Fields | Data Fields | 3,431 | 57 |
| `0x29` | `ge::ActionChart_FrameEvent_ChromaticBlur` | Data Fields | Data Fields | 204 | 0 |
| `0x2A` | `ge::ActionChart_FrameEvent_Blur` | Data Fields | Data Fields | 475 | 0 |
| `0x2B` | `ge::ActionChart_FrameEvent_SlowMotion` | Data Fields | Data Fields | 688 | 0 |
| `0x2C` | `ge::ActionChart_FrameEvent_ColorByPass` | Data Fields | Data Fields | 44 | 0 |
| `0x2D` | `ge::ActionChart_FrameEvent_ColorBalance` | Data Fields | Data Fields | 18 | 0 |
| `0x2E` | `ge::ActionChart_FrameEvent_Glitter` | Glitter Fields | Glitter Fields | 27 | 0 |
| `0x2F` | `ge::ActionChart_FrameEvent_BoneScale` | Name Data Fields | Name Data Fields | 28 | 7 |
| `0x30` | `ge::ActionChart_FrameEvent_SoundKill` | Data Fields | Sound Kill Fields | 76 | 10 |
| `0x31` | `ge::ActionChart_FrameEvent_SoundBase` | Data Fields | Sound Fields | 0 | 0 |
| `0x32` | `ge::ActionChart_FrameEvent_Sound` | Data Fields | Sound Fields | 7,814 | 2,633 |
| `0x33` | `ge::ActionChart_FrameEvent_Voice` | Data Fields | Sound Fields | 4,080 | 365 |
| `0x34` | `ge::ActionChart_FrameEvent_SoundExternal` | Sound External Fields | Sound External Fields | 0 | 0 |
| `0x35` | `ge::ActionChart_FrameEvent_SoundWeaponSwing` | Data Fields | Sound Fields | 566 | 47 |
| `0x36` | `ge::ActionChart_FrameEvent_SoundFootstep` | Data Fields | Sound Fields | 6,001 | 246 |
| `0x37` | `ge::ActionChart_FrameEvent_SoundJumpUp` | Data Fields | Sound Fields | 0 | 0 |
| `0x38` | `ge::ActionChart_FrameEvent_SoundJumpLand` | Data Fields | Sound Fields | 111 | 19 |
| `0x39` | `ge::ActionChart_FrameEvent_SoundMovement` | Data Fields | Sound Fields | 5,829 | 0 |
| `0x3A` | `ge::ActionChart_FrameEvent_SoundWeaponIn` | Data Fields | Sound Fields | 12 | 2 |
| `0x3B` | `ge::ActionChart_FrameEvent_SoundWeaponOut` | Data Fields | Sound Fields | 19 | 2 |
| `0x3C` | `ge::ActionChart_FrameEvent_SoundImpact` | Data Fields | Sound Fields | 0 | 0 |
| `0x3D` | `ge::ActionChart_FrameEvent_SoundCommon` | Data Fields | Sound Fields | 1,084 | 26 |
| `0x3E` | `ge::ActionChart_FrameEvent_SoundBodyfall` | Data Fields | Sound Fields | 69 | 67 |
| `0x3F` | `ge::ActionChart_FrameEvent_SoundMovementStop` | Data Fields | Sound Fields | 11 | 0 |
| `0x40` | `ge::ActionChart_FrameEvent_SoundWeaponReady` | Data Fields | Sound Fields | 35 | 0 |
| `0x41` | `ge::ActionChart_FrameEvent_SoundPassingGrass` | Data Fields | Sound Fields | 0 | 0 |
| `0x42` | `ge::ActionChart_FrameEvent_SoundEvent` | Name Data Fields | Name Data Fields | 0 | 0 |
| `0x43` | `ge::ActionChart_FrameEvent_FacialAnimation` | Name Data Fields | Name Data Fields | 726 | 0 |
| `0x44` | `ge::ActionChart_FrameEvent_FacialAnimationWeight` | Two Value Fields | Two Value Fields | 535 | 0 |
| `0x45` | `ge::ActionChart_FrameEvent_FaceMorphWeight` | Two Value Fields | Two Value Fields | 635 | 0 |
| `0x46` | `ge::ActionChart_FrameEvent_KeepAimOn` | none | none | 40 | 0 |
| `0x47` | `ge::ActionChart_FrameEvent_KeepAimOff` | none | none | 13 | 0 |
| `0x48` | `ge::ActionChart_FrameEvent_Collect` | none | none | 3 | 0 |
| `0x49` | `ge::ActionChart_FrameEvent_Product` | none | none | 1 | 0 |
| `0x4A` | `ge::ActionChart_FrameEvent_ReTargetPosition` | Name Fields | Name Fields | 19 | 13 |
| `0x4B` | `ge::ActionChart_FrameEvent_ChangeSpeedToTarget` | Data Fields | Data Fields | 114 | 0 |
| `0x4C` | `ge::ActionChart_FrameEvent_FindTarget` | Data Fields | Data Fields | 188 | 0 |
| `0x4D` | `ge::ActionChart_FrameEvent_SetFindedTarget` | Value Fields | Value Fields | 90 | 0 |
| `0x4E` | `ge::ActionChart_FrameEvent_SetCameraFov` | Camera Fields | Camera Fields | 2,721 | 0 |
| `0x4F` | `ge::ActionChart_FrameEvent_ResetCameraFov` | Value Fields | Value Fields | 942 | 0 |
| `0x50` | `ge::ActionChart_FrameEvent_SetCameraPos` | Camera Fields | Camera Fields | 1,780 | 0 |
| `0x51` | `ge::ActionChart_FrameEvent_ResetCameraPos` | Value Fields | Value Fields | 536 | 0 |
| `0x52` | `ge::ActionChart_FrameEvent_RiderIK` | Byte Fields | Byte Fields | 34 | 0 |
| `0x53` | `ge::ActionChart_FrameEvent_AdditiveAnimation` | Additive Fields | Additive Fields | 1 | 20 |
| `0x54` | `ge::ActionChart_FrameEvent_LookAt` | Byte Fields | Byte Fields | 24 | 0 |
| `0x55` | `ge::ActionChart_FrameEvent_StartCameraWave` | Data Fields | Data Fields | 0 | 0 |
| `0x56` | `ge::ActionChart_FrameEvent_StopCameraWave` | none | none | 1 | 0 |
| `0x57` | `ge::ActionChart_FrameEvent_MovePos` | Data Fields | Data Fields | 43 | 0 |
| `0x58` | `ge::ActionChart_FrameEvent_VaryStat` | Data Fields | Data Fields | 8,572 | 0 |
| `0x59` | `ge::ActionChart_FrameEvent_VaryVehicleStat` | Data Fields | Data Fields | 143 | 0 |
| `0x5A` | `ge::ActionChart_FrameEvent_TowerAim` | Data Fields | Data Fields | 0 | 0 |
| `0x5B` | `ge::ActionChart_FrameEvent_Fishing` | none | none | 1 | 0 |
| `0x5C` | `ge::ActionChart_FrameEvent_SetHitPartHp` | Data Fields | Data Fields | 0 | 0 |
| `0x5D` | `ge::ActionChart_FrameEvent_VaryHitPartHp` | Data Fields | Data Fields | 0 | 0 |
| `0x5E` | `ge::ActionChart_FrameEvent_SetHitPartAvoid` | Data Fields | Data Fields | 0 | 0 |
| `0x5F` | `ge::ActionChart_FrameEvent_BuildTent` | none | none | 1 | 0 |
| `0x60` | `ge::ActionChart_FrameEvent_TakeDownTent` | none | none | 1 | 0 |
| `0x61` | `ge::ActionChart_FrameEvent_RollRateDice` | none | none | 0 | 0 |
| `0x62` | `ge::ActionChart_FrameEvent_Manufacture` | none | none | 1 | 0 |
| `0x63` | `ge::ActionChart_FrameEvent_HideCharacter` | Value Fields | Value Fields | 129 | 11 |
| `0x64` | `ge::ActionChart_FrameEvent_RevealCharacter` | Value Fields | Value Fields | 124 | 8 |
| `0x65` | `ge::ActionChart_FrameEvent_HeadLineMessage` | Two Byte Fields | Two Byte Fields | 55 | 0 |
| `0x66` | `ge::ActionChart_FrameEvent_RepairItem` | none | none | 1 | 0 |
| `0x67` | `ge::ActionChart_FrameEvent_Campfire` | none | none | 1 | 0 |
| `0x68` | `ge::ActionChart_FrameEvent_StartSitDownIk` | none | none | 2 | 0 |
| `0x69` | `ge::ActionChart_FrameEvent_EndSitDownIk` | none | none | 1 | 0 |
| `0x6A` | `ge::ActionChart_FrameEvent_Greet` | none | none | 1 | 0 |
| `0x6B` | `ge::ActionChart_FrameEvent_Steal` | none | none | 1 | 0 |
| `0x6C` | `ge::ActionChart_FrameEvent_StartCasting` | Value Fields | Value Fields | 10 | 0 |
| `0x6D` | `ge::ActionChart_FrameEvent_CancelCasting` | none | none | 0 | 0 |
| `0x6E` | `ge::ActionChart_FrameEvent_ReadBook` | none | none | 1 | 0 |
| `0x6F` | `ge::ActionChart_FrameEvent_CallLuaEvent` | Lua Event Fields | Lua Event Fields | 291 | 5 |
| `0x70` | `ge::ActionChart_FrameEvent_CreateDecal` | Decal Fields | Decal Fields | 960 | 3 |
| `0x71` | `ge::ActionChart_FrameEvent_RetryActionMoveReady` | none | none | 0 | 0 |
| `0x72` | `ge::ActionChart_FrameEvent_RetryActionMove` | none | none | 3 | 29 |
| `0x73` | `ge::ActionChart_FrameEvent_WeaponType` | Value Fields | Value Fields | 169 | 0 |
| `0x74` | `ge::ActionChart_FrameEvent_FishingFloatIK` | Byte Fields | Byte Fields | 3 | 0 |
| `0x75` | `ge::ActionChart_FrameEvent_AdditionalDamageType` | Value Fields | Value Fields | 0 | 0 |
| `0x76` | `ge::ActionChart_FrameEvent_UsePetSkill` | Value Fields | Value Fields | 0 | 0 |
| `0x77` | `ge::ActionChart_FrameEvent_FlashBang` | Two Value Fields | Two Value Fields | 3 | 0 |
| `0x78` | `ge::ActionChart_FrameEvent_Lighten` | Light Fields | Light Fields | 486 | 9 |
| `0x79` | `ge::ActionChart_FrameEvent_Weather` | Weather Fields | Weather Fields | 0 | 0 |
| `0x7A` | `ge::ActionChart_FrameEvent_Thunder` | none | none | 0 | 0 |
| `0x7B` | `ge::ActionChart_FrameEvent_CharacterParticle` | Light Fields | Light Fields | 0 | 0 |
| `0x7C` | `ge::ActionChart_FrameEvent_SetBerserk` | Byte Fields | Byte Fields | 2 | 4 |
| `0x7D` | `ge::ActionChart_FrameEvent_OperateCommonGauge` | Data Fields | Data Fields | 37 | 0 |
| `0x7E` | `ge::ActionChart_FrameEvent_TakeDownCannon` | none | none | 1 | 0 |
| `0x7F` | `ge::ActionChart_FrameEvent_SummonCharacter` | none | none | 6 | 0 |
| `0x80` | `ge::ActionChart_FrameEvent_CannonAngle` | Byte Fields | Byte Fields | 4 | 0 |
| `0x81` | `ge::ActionChart_FrameEvent_PoseFemale` | Pose Fields | Pose Fields | 0 | 0 |
| `0x82` | `ge::ActionChart_FrameEvent_CameraRotate` | Data Fields | Data Fields | 37 | 0 |
| `0x83` | `ge::ActionChart_FrameEvent_CommandRepair` | none | none | 1 | 0 |
| `0x84` | `ge::ActionChart_FrameEvent_ActiveSkill` | none | none | 2 | 0 |
| `0x85` | `ge::ActionChart_FrameEvent_BuildingUpgrade` | none | none | 1 | 0 |
| `0x86` | `ge::ActionChart_FrameEvent_AttackBounds` | Data Fields | Attack Bounds Fields | 3 | 11 |
| `0x87` | `ge::ActionChart_FrameEvent_PredictCannonAtkPos` | Cannon Predict Fields | Cannon Predict Fields | 1,808 | 0 |
| `0x88` | `ge::ActionChart_FrameEvent_Banquet` | none | none | 1 | 0 |
| `0x89` | `ge::ActionChart_FrameEvent_GenerateWave` | Wave Fields | Wave Fields | 11 | 0 |
| `0x8A` | `ge::ActionChart_FrameEvent_WeaponBoneFlag` | Two Value Fields | Two Value Fields | 98 | 0 |
| `0x8B` | `ge::ActionChart_FrameEvent_ActionTimer` | Two Value Fields | Two Value Fields | 8 | 0 |
| `0x8C` | `ge::ActionChart_FrameEvent_ModelAnimation` | Model Animation Fields | Model Animation Fields | 48 | 0 |
| `0x8D` | `ge::ActionChart_FrameEvent_Observer` | none | none | 25 | 0 |
| `0x8E` | `ge::ActionChart_FrameEvent_Texture` | Light Fields | Light Fields | 0 | 0 |
| `0x8F` | `ge::ActionChart_FrameEvent_ResetTargetList` | none | none | 23 | 0 |
| `0x90` | `ge::ActionChart_FrameEvent_SummonCharacters` | Data Fields | Data Fields | 172 | 0 |
| `0x91` | `ge::ActionChart_FrameEvent_AttackSkillSimple` | Attack Skill Simple Fields | Attack Skill Simple Fields | 0 | 0 |
| `0x92` | `ge::ActionChart_FrameEvent_AttackArrowSkillSimple` | Attack Arrow Skill Simple Fields | Attack Arrow Skill Simple Fields | 0 | 0 |
| `0x93` | `ge::ActionChart_FrameEvent_ResetGuard` | none | none | 1 | 0 |
| `0x94` | `ge::ActionChart_FrameEvent_BaseMeshOff` | none | none | 0 | 0 |
| `0x95` | `ge::ActionChart_FrameEvent_ControlApStack` | none | none | 0 | 0 |
| `0x96` | `ge::ActionChart_FrameEvent_Ragdollize` | none | none | 0 | 0 |
| `0x97` | `ge::ActionChart_FrameEvent_ReqGuildTeamBattle` | none | none | 3 | 0 |
| `0x98` | `ge::ActionChart_FrameEvent_AtackForClient` | Client Attack Fields | Client Attack Fields | 976 | 0 |
| `0x99` | `ge::ActionChart_FrameEvent_ResetUpper` | none | none | 0 | 0 |
| `0x9A` | `ge::ActionChart_FrameEvent_ThrowGrenade` | Grenade Fields | Grenade Fields | 1 | 0 |
| `0x9B` | `ge::ActionChart_FrameEvent_UnsafenGrenade` | Attack Fields | Attack Fields | 1 | 0 |
| `0x9C` | `ge::ActionChart_FrameEvent_PredGrenadePath` | Grenade Path Fields | Grenade Path Fields | 2 | 0 |
| `0x9D` | `ge::ActionChart_FrameEvent_MouseFocus` | Byte Fields | Byte Fields | 2 | 0 |
| `0x9E` | `ge::ActionChart_FrameEvent_SetIgnoreAggroFlag` | Value Fields | Value Fields | 0 | 0 |
| `0x9F` | `ge::ActionChart_FrameEvent_UVAnimationSpeed` | Value Fields | Value Fields | 0 | 0 |
| `0xA0` | `ge::ActionChart_FrameEvent_SpawnTotem` | none | none | 1 | 0 |
| `0xA1` | `ge::ActionChart_FrameEvent_SetBattleFX` | Battle FX Fields | Battle FX Fields | 85 | 0 |
| `0xA2` | `ge::ActionChart_FrameEvent_VehicleMeshOff` | Two Byte Fields | Two Byte Fields | 0 | 0 |
| `0xA3` | `ge::ActionChart_FrameEvent_ClearRestriction` | none | none | 0 | 0 |
| `0xA4` | `ge::ActionChart_FrameEvent_CannonAttackBounds` | Name Data Fields | Name Data Fields | 10 | 0 |
| `0xA5` | `ge::ActionChart_FrameEvent_ReturnToPos` | Data Fields | Data Fields | 11 | 0 |
| `0xA6` | `ge::ActionChart_FrameEvent_DecreaseSkillCoolTime` | Data Fields | Data Fields | 21 | 0 |
| `0xA7` | `ge::ActionChart_FrameEvent_DecreaseSubResourcePoint` | Data Fields | Data Fields | 3 | 0 |
| `0xA8` | `ge::ActionChart_FrameEvent_DecreaseAllSkillCoolTime` | Value Fields | Value Fields | 1 | 0 |
| `0xA9` | `ge::ActionChart_FrameEvent_PlayCutscene` | Cutscene Fields | Cutscene Fields | 0 | 0 |
| `0xAA` | `ge::ActionChart_FrameEvent_BuildTentKit` | none | none | 1 | 0 |
| `0xAB` | `ge::ActionChart_FrameEvent_PlayAnimation` | Play Animation Fields | Play Animation Fields | 9 | 0 |

## Notes

- On client 3483, 7,228 of the 8,030 charts (`pc_actionchartpackagepcraw.paac`
  aside) read with Layout 2 to their last byte, the 33 class charts among
  them. Six of the others still have Layout 1, among them
  `object/t0050_characterselect_pnym_normal.paac`,
  `summon/war_monster/m0002_ogre_war.paac` and
  `summon/war_monster/m0119_cyclops_war.paac`. Their string 0 is not
  `DEFAULT`, which every Layout 2 chart has; no version field tells the two
  layouts apart. The rest break in a frame event or an element (see Open
  Questions).
- On client 1784, 724 of the 728 charts in the archives of the doc's sample
  files read with Layout 1 to their last byte, together with the PcRaw file.
  The other four (`pc/10_pjw/kunoichiaction_noweapon.paac` and its
  `_simple` copy, `pc/14_plw/shytribeaction_noweaponmain_m.paac` and
  `infinitydefence/monster/24/m0150_valstoneorc_f_named.paac`) are not in
  that client's `actionchartheader.paach` and have 106-byte effect
  parameters. Their attachment count sits at byte `0x67` of those 106
  bytes; the 1784 loader reads byte `0x70`, past their end, so it cannot
  read these four either.
- Of the layouts in between, client 3258 has Layout 2; clients 2335 and
  2919 fit neither.
- A read past the end of the file leaves a field at its default in the
  client loader instead of failing, so a wrong layout reads on silently.

## Open Questions

### Frame Events on Client 3483

The 1784 ids still hold, and five readers changed (see Frame Event Types).
Types that no checked chart of client 3483 uses are read with their 1784
fields, which is not checked: the PcRaw file of client 3483 breaks at its
24th event, a `0xA1` Set Battle FX event that carries 4 bytes more
than on client 1784. Until every type is checked, Layout 2 leaves the PcRaw
events and elements as one block, and a non-class chart reads past `events`
only when its types are among the checked ones.

### Elements on Client 3483

The Layout 2 Element reads the elements of the 7,228 client 3483 charts that
read whole, but only its two names are tied to anything: what the 17-byte
items are, and how the 1784 fields (a u32, two strings and the Element
Records) map onto `unknown_str_ref_34`, `unknown_38` and the fields after
the items, is not known.

### Which Field Holds StaminaSpeed

The server's per-weapon summaries give each action a `StaminaSpeed`. The
other summary fields have their place in Layout 1 (Action Data and Element
Parameters), but on client 1784 every Archer and Ranger action with a
summary entry has `StaminaSpeed` `1`, so a match cannot place it. A client
whose summaries have other values, together with its own Layout 1 charts,
would answer it.
