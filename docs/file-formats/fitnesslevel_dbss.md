# `fitnesslevel.dbss` Format

## Purpose

Level tables of the three fitness stats in the character window: Breath, Strength and Health. Each row gives the EXP to the next level and the total bonus the fitness stat grants at that level (max Stamina for Breath, weight limit for Strength, max HP and max MP/WP/SP for Health). Companion `fitnessleveloffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------------------ | --------- |
| 1      | 1276 and later | 3483    | `fitnesslevel.dbss`       | 4,453 | 153 Level Row, 3 Block         | 29        |
| 1      | 1276 and later | 3483    | `fitnessleveloffset.dbss` | 1,848 | 153 Offset Row, 3 Offset Block | 12        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `fitnesslevel.dbss`       | 4,453 B (100.0%) | 0 B (0.0%) |
| 1      | `fitnessleveloffset.dbss` | 1,848 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                   |
| ------------------------- | -------- | ------------------------------------------------------ |
| `fitnessleveloffset.dbss` | Required | `(fitness type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type              | Field      | Notes                                       |
| ------- | ----------------- | ---------- | ------------------------------------------- |
| `+0x00` | u32               | type_count | Number of fitness blocks (observed: 3)      |
| `+0x04` | Block[type_count] | blocks     | One block per fitness type                  |

The blocks fill the file exactly: 4 + 3 x (4 + 51 x 29) = 4,453 bytes on client 3458.

### Block (variable: 4 bytes + rows)

| Offset  | Type                   | Field       | Notes                                |
| ------- | ---------------------- | ----------- | ------------------------------------ |
| `+0x00` | u32                    | level_count | Rows in this block (observed: 51)    |
| `+0x04` | Level Row[level_count] | rows        | See Level Row                        |

### Level Row (29 bytes)

| Offset  | Type | Field        | Notes                                                                                          |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| `+0x00` | u8   | fitness_type | `0` Breath, `1` Strength, `2` Health; equals the block index                                   |
| `+0x01` | u32  | level        | `0` to `50`, ascending inside a block                                                          |
| `+0x05` | u64  | exp          | EXP needed to go from this level to the next, read like `lifeexp.dbss` (Notes); `0` on level 0, rising to 5,500,000 (Breath, Strength) and 2,750,000 (Health) on level 50 |
| `+0x0D` | f32  | max_stamina  | Breath total: max Stamina bonus; `0` in Strength and Health rows                               |
| `+0x11` | f32  | weight_limit | Strength total: weight limit bonus in 1/10,000 LT (`400000` is 40 LT); `0` elsewhere          |
| `+0x15` | f32  | max_hp       | Health total: max HP bonus; `0` elsewhere                                                      |
| `+0x19` | f32  | max_mp       | Health total: max MP/WP/SP bonus (the class's combat resource); `0` elsewhere                  |

Every row carries all four stat floats; only the ones of its own fitness type are non-zero. All stored floats are whole numbers except `weight_limit`, whose LT value can end in `.5` (Strength level 29 is 385,000, 38.5 LT). Levels 0 and 1 hold no bonus; level 2 is the first that grants one.

A row's totals are the bonus at that row's own level, confirmed in game on 2026-10-06: the tooltips at Breath Lv.37, Strength Lv.31 and Health Lv.33 read `Max Stamina +570`, `Weight Limit +42 LT` and `Max HP +320`, the values of rows 37, 31 and 33.

### `fitnessleveloffset.dbss`

Index into `fitnesslevel.dbss`, with the same block shape as the main file but no leading type count.

| Offset  | Type                | Field  | Notes                                     |
| ------- | ------------------- | ------ | ----------------------------------------- |
| `+0x00` | Offset Block[..end] | blocks | Blocks repeated until the end of the file |

The block index is the fitness type; the file stores no type field. 3 x (4 + 51 x 12) = 1,848 bytes on client 3458.

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                 |
| ------- | ----------------------- | ----------- | ------------------------------------- |
| `+0x00` | u32                     | level_count | Rows in this block (observed: 51)     |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                            |
| `+0x04` | u32  | data_offset | Absolute byte offset of the 29-byte row in `fitnesslevel.dbss`           |
| `+0x08` | u32  | data_size   | Always 29                                                                |

The first Breath row sits at `0x08`, after the type count and Breath's level count; each later block starts 4 bytes past the previous block's last row, skipping that block's level count. The parser reads the main file through these rows and checks that each row's `fitness_type` and `level` match the offset row's block and key.

## Enum Values

### Fitness Type

| ID  | Name     | Stat in the row                     |
| --- | -------- | ----------------------------------- |
| 0   | Breath   | `max_stamina`                       |
| 1   | Strength | `weight_limit`                      |
| 2   | Health   | `max_hp`, `max_mp`                  |

The order matches the client's `_ENUM_FITNESS` in `panel_characterinfo_basic_all.luac` (`BREATH`, `POWER`, then Health), whose hover handlers pass `0`, `1` and `2` for the Breath, Strength and Health texts. The stat per type matches the client's tooltip strings `Breath: Max Stamina +`, `Strength: Weight Limit +` and `Health: Max HP +{hpIncrease}, Max {mpTypeName} +{mpIncrease}`.

## Notes

- `fitnessmaxlevel.bss` stores the max level of each fitness type, `50` for all three on client 3464, the top row of every block here; see [fitnessmaxlevel](fitnessmaxlevel_bss.md).
- Level 30 is the soft cap. No file stores it, but on client 3464 the EXP to the next level jumps between rows 30 and 31 in every block: Breath 20,000 to 50,000, Strength 10,000 to 30,000, Health 5,000 to 20,000. Up to row 30 the step between rows is at most 3,500.
- The client reads a fitness level and its EXP through `getFitnessLevel`, `getCurrFitnessExperiencePoint` and `getDemandFItnessExperiencePoint` (`panel_characterinfo_basic_all_3.luac`); the bonus shown in the tooltip comes from `ToClient_GetFitnessLevelStatus(type)`.
- The four stat floats are cumulative totals, not per-level increments: every column only rises with the level (Breath 25, 50, 75 up to 800; Strength 2 LT up to 80 LT; Health HP 10 up to 490 and MP/WP/SP 10 up to 300).
- Breath and Strength have the same EXP from level 41 up and Strength needs less than Breath on levels 1 to 40.
- Row direction: read like [lifeexp](lifeexp_dbss.md), where a packet capture confirmed that the row of level N is the EXP to go from N to N + 1. Both tables use the same block shape and the client draws both bars as current / demand (`getCurrFitnessExperiencePoint` / `getDemandFItnessExperiencePoint` here, the life skill pair there). Row 0 (`0` EXP, no bonus) is then an unused placeholder, as characters start every fitness stat at Lv.1. No fitness capture yet; a fitness EXP message whose bar matches row N + 1, or a fresh character at Breath Lv.0, would flip it.
