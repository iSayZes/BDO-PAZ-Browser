# `sequencetriggerdata.bss` Format

## Purpose

Where each sequence starts on its own, and what it runs. A row names one
sequence by folder and file (`Sadang` and
`CS_SadangSeoul_06_02_Pyeseja`, the file
`sequence/sadang/cs_sadangseoul_06_02_pyeseja.paseqfe`), the regions and
the world position and radius that trigger it, the position the player
revives at, a start condition (quest state checks, `getlevel`,
`checkclass`, `checkelementalmonsterkey`), the scripts run when it starts
and ends and when it is skipped, the contents group that must be open and
six flags. The file is compiled from `sequence/sequencetriggerdata.xml`,
which the client ships next to it. It is a PABR table of variable rows
whose text sits in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records   | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ------- | --------- | ----------------------- |
| 4      | 2156 and later | 3483    | `sequencetriggerdata.bss` | 390,727 | 1,101 Row | 84 to 86, 84 on average |
| 3      | 3242           | 3242    | `sequencetriggerdata.bss` | 264,735 | 731 Row   | 85                      |
| 2      | 3111 to 3212   | 3212    | `sequencetriggerdata.bss` | 261,790 | 727 Row   | 83                      |
| 1      | 2703 to 3103   | 3103    | `sequencetriggerdata.bss` | 249,445 | 705 Row   | 75                      |

| Layout | File                      | Known              | Unknown      |
| ------ | ------------------------- | ------------------ | ------------ |
| 4      | `sequencetriggerdata.bss` | 390,727 B (100.0%) | 0 B (0.0%)   |
| 3      | `sequencetriggerdata.bss` | 264,004 B (99.7%)  | 731 B (0.3%) |
| 2      | `sequencetriggerdata.bss` | 261,790 B (100.0%) | 0 B (0.0%)   |
| 1      | `sequencetriggerdata.bss` | 249,445 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 4             |
| 3482   | Layout 4             |
| 3474   | Layout 4             |
| 3473   | Layout 4             |
| 3464   | Layout 4             |
| 3458   | Layout 4             |
| 3454   | Layout 4             |
| 3444   | Layout 4             |
| 3435   | Layout 4             |
| 3426   | Layout 4             |
| 3418   | Layout 4             |
| 3412   | Layout 4             |
| 3402   | Layout 4             |
| 3396   | Layout 4             |
| 3387   | Layout 4             |
| 3381   | Layout 4             |
| 3373   | Layout 4             |
| 3364   | Layout 4             |
| 3356   | Layout 4             |
| 3349   | Layout 4             |
| 3342   | Layout 4             |
| 3335   | Layout 4             |
| 3326   | Layout 4             |
| 3321   | Layout 4             |
| 3314   | Layout 4             |
| 3303   | Layout 4             |
| 3302   | Layout 4             |
| 3293   | Layout 4             |
| 3283   | Layout 4             |
| 3275   | Layout 4             |
| 3267   | Layout 4             |
| 3258   | Layout 4             |
| 3251   | Layout 4             |
| 3242   | Layout 3             |
| 3235   | Layout 4             |
| 3229   | Layout 4             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | Layout 4             |
| 2196   | Layout 4             |
| 2192   | Layout 4             |
| 2189   | Layout 4             |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | Layout 4             |
| 2156   | Layout 4             |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No file              |
| 1276   | No file              |
| 1267   | No file              |
| 1261   | No file              |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None. The handler names the regions with their LOC type 17 names from
`languagedata_*.loc` when it is loaded. The sequence stays a path: the
`.paseqfe` sequences under `sequence/` have no handler.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 82 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                                                                   |
| ------------------ | ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | ASCII key hash (lookup3, seed `0xC5EDE`) of `file_name`; matches on every row                           |
| `+0x04`            | u32               | file_name               | Index into `strings`: the sequence file without folder or extension (`CS_SadangSeoul_06_02_Pyeseja`); unique |
| `+0x08`            | u32               | folder                  | Index into `strings`: the folder under `sequence/` (`Sadang`, `PEDU/EdaniaBoss`); empty on 6 rows of client 3482       |
| `+0x0C`            | u32               | start_condition         | Index into `strings`: the script that must hold for the sequence to start; empty when none              |
| `+0x10`            | u32               | start_execute           | Index into `strings`: the script run when the sequence starts                                           |
| `+0x14`            | u32               | end_execute             | Index into `strings`: the script run when the sequence ends                                             |
| `+0x18`            | u32               | force_skip_end_execute  | Index into `strings`: the script run in place of `end_execute` when the sequence is force skipped       |
| `+0x1C`            | u32               | skip_condition          | Index into `strings`: the condition for skipping; empty on every row of client 3482                     |
| `+0x20`            | u32               | contents_group_open     | Index into `strings`: the contents group key as decimal text (`863`, `2186`)                            |
| `+0x24`            | f32[3]            | position                | World x, y, z of the trigger area                                                                       |
| `+0x30`            | f32[3]            | resurrect_position      | World x, y, z the player revives at during the sequence                                                 |
| `+0x3C`            | u64               | region_count            | Number of region keys; `1` on all but one row of client 3482                                                           |
| `+0x44`            | u16[region_count] | region_keys             | `regioninfo.bss` regions of the trigger (`1496` Geunjeongjeon Hall), LOC type 17                        |
| `region_keys+0x00` | u32               | file_name_hash_dup      | Same value as `file_name_hash` on every row                                                             |
| `region_keys+0x04` | f32               | radius                  | Radius of the trigger area around `position`, in world units; `0` on 149 rows of client 3482                           |
| `region_keys+0x08` | u8                | use_client_spawn        | XML `UseClientSpawn`                                                                                    |
| `region_keys+0x09` | u8                | exit_character_select   | XML `ExitCharacterSelect`                                                                               |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | XML `PreUpdateFadeOut`                                                                                  |
| `region_keys+0x0B` | u8                | party_sequence          | XML `PartySequence`                                                                                     |
| `region_keys+0x0C` | u8                | character_swap_sequence | XML `CharacterSwapSequence`; `0` on every row of client 3482                                            |
| `region_keys+0x0D` | u8                | force_skip_sequence     | XML `ForceSkipSequence`                                                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                         |
| ------- | ------------------ | ------------ | ----------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                             |
| `+0x04` | pstr[string_count] | strings      | UTF-8 names, folders, scripts and keys; one empty string serves every empty field |

## Layout 3

The row has one more flag byte, `unknown_region_keys_0d`, between
`character_swap_sequence` and `force_skip_sequence`.

### Row (variable: 83 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 4                                           |
| `+0x04`            | u32               | file_name               | As in Layout 4                                           |
| `+0x08`            | u32               | folder                  | As in Layout 4                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 4                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 4                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 4                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 4                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 4                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 4                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 4                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 4                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 4                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 4                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 4                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 4                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 4                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 4                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 4                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 4                                           |
| `region_keys+0x0C` | u8                | character_swap_sequence | As in Layout 4                                           |
| `region_keys+0x0D` | u8                | unknown_region_keys_0d  | `0` on every row of client 3242; see Notes               |
| `region_keys+0x0E` | u8                | force_skip_sequence     | As in Layout 4                                           |

## Layout 2

The row has five flag bytes: no `character_swap_sequence`.

### Row (variable: 81 bytes + region keys)

| Offset             | Type              | Field                   | Notes                                                    |
| ------------------ | ----------------- | ----------------------- | -------------------------------------------------------- |
| `+0x00`            | u32               | file_name_hash          | As in Layout 4                                           |
| `+0x04`            | u32               | file_name               | As in Layout 4                                           |
| `+0x08`            | u32               | folder                  | As in Layout 4                                           |
| `+0x0C`            | u32               | start_condition         | As in Layout 4                                           |
| `+0x10`            | u32               | start_execute           | As in Layout 4                                           |
| `+0x14`            | u32               | end_execute             | As in Layout 4                                           |
| `+0x18`            | u32               | force_skip_end_execute  | As in Layout 4                                           |
| `+0x1C`            | u32               | skip_condition          | As in Layout 4                                           |
| `+0x20`            | u32               | contents_group_open     | As in Layout 4                                           |
| `+0x24`            | f32[3]            | position                | As in Layout 4                                           |
| `+0x30`            | f32[3]            | resurrect_position      | As in Layout 4                                           |
| `+0x3C`            | u64               | region_count            | As in Layout 4                                           |
| `+0x44`            | u16[region_count] | region_keys             | As in Layout 4                                           |
| `region_keys+0x00` | u32               | file_name_hash_dup      | As in Layout 4                                           |
| `region_keys+0x04` | f32               | radius                  | As in Layout 4                                           |
| `region_keys+0x08` | u8                | use_client_spawn        | As in Layout 4                                           |
| `region_keys+0x09` | u8                | exit_character_select   | As in Layout 4                                           |
| `region_keys+0x0A` | u8                | pre_update_fade_out     | As in Layout 4                                           |
| `region_keys+0x0B` | u8                | party_sequence          | As in Layout 4                                           |
| `region_keys+0x0C` | u8                | force_skip_sequence     | As in Layout 4                                           |

## Layout 1

The row has one region key and no `region_count`, and the five flag
bytes of Layout 2.

### Row (75 bytes)

| Offset            | Type   | Field                  | Notes                                                    |
| ----------------- | ------ | ---------------------- | -------------------------------------------------------- |
| `+0x00`           | u32    | file_name_hash         | As in Layout 4                                           |
| `+0x04`           | u32    | file_name              | As in Layout 4                                           |
| `+0x08`           | u32    | folder                 | As in Layout 4                                           |
| `+0x0C`           | u32    | start_condition        | As in Layout 4                                           |
| `+0x10`           | u32    | start_execute          | As in Layout 4                                           |
| `+0x14`           | u32    | end_execute            | As in Layout 4                                           |
| `+0x18`           | u32    | force_skip_end_execute | As in Layout 4                                           |
| `+0x1C`           | u32    | skip_condition         | As in Layout 4                                           |
| `+0x20`           | u32    | contents_group_open    | As in Layout 4                                           |
| `+0x24`           | f32[3] | position               | As in Layout 4                                           |
| `+0x30`           | f32[3] | resurrect_position     | As in Layout 4                                           |
| `+0x3C`           | u16    | region_keys            | The one region of the trigger; no count before it        |
| `+0x3E`           | u32    | file_name_hash_dup     | As in Layout 4                                           |
| `+0x42`           | f32    | radius                 | As in Layout 4                                           |
| `+0x46`           | u8     | use_client_spawn       | As in Layout 4                                           |
| `+0x47`           | u8     | exit_character_select  | As in Layout 4                                           |
| `+0x48`           | u8     | pre_update_fade_out    | As in Layout 4                                           |
| `+0x49`           | u8     | party_sequence         | As in Layout 4                                           |
| `+0x4A`           | u8     | force_skip_sequence    | As in Layout 4                                           |

## Scripts

The script fields hold calls joined by `;`. A `!` in front of a call
negates it, and `<or>` splits a condition into alternatives. Counts are
rows using each call, client 3482 (1,101 rows, 3,346 strings).

| Field                    | Calls (rows)                                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `start_condition`        | `checkquestcondition` (715), `progressquest` (631), `clearquest` (457), `getlevel` (144), `checkclass` (118), `checkwoman` (50), `checkelementalmonsterkey` (21) and 8 more; empty on 63 rows |
| `start_execute`          | `acceptquest` (370); empty on 731 rows                                                                                                    |
| `end_execute`            | `completequestcondition` (855), `setposition` (250), `completequest` (84), `acceptquest` (57), `pushitem` (33), `pushknowledge` (10) and 4 more; empty on 117 rows |
| `force_skip_end_execute` | `pushitem`, `completequest` and `tutorialendteleportroute`, on 2 rows                                                                     |

## Flags

Rows with each flag set, client 3482:

| Flag                      | Rows |
| ------------------------- | ---- |
| `use_client_spawn`        | 26   |
| `exit_character_select`   | 67   |
| `pre_update_fade_out`     | 9    |
| `party_sequence`          | 11   |
| `character_swap_sequence` | 0    |
| `force_skip_sequence`     | 2    |

## Field Names

Every field but `file_name_hash` and its copy is a `<TriggerData>`
element of `sequence/sequencetriggerdata.xml` in the same client. The
XML's `FileName` attribute is `folder` and `file_name` joined by `/`
(`Sadang/CS_SadangSeoul_06_02_PyesejaHard`); `RegionKey` (`1109,1110`
on the row with two regions), `Position`, `Radius`, `ResurrectPosition`,
`StartCondition`, `StartExecute`, `EndExecute`, `ForceSkipEndExecute`,
`SkipCondition`, `ContentsGroupOpen` and the six flags follow. On client
3482 all 1,101 rows match their XML element in every field and in file
order; the XML has 21 more elements the file leaves out, test and console
sequences among them (`CS_TEST_VelliaTest`,
`Seoul/CS_Seoul_01_00_BalanhosuToNampo_Console`). The XML writes the flags
as `True` and `False` in the order the file stores them;
`CharacterSwapSequence` is `False` on every element, so its byte is
placed by that order alone.

## Notes

- Clients 2171 to 2183 and 2207 to 2695 store rows of another shape,
  which no layout of this doc reads yet: client 2207 has 2 rows of 63
  bytes with six string indexes (no `folder`), one region key and one flag
  byte. The other clients from 2156 to 2203 ship the table empty (row
  count `0`), which every layout reads.
- Client 3242 stores 7 flag bytes (Layout 3). Matched by file name to
  client 3482, its rows hold the same values in the first four flags and
  in `force_skip_sequence`. The two bytes between them are `0` on all 731
  rows, so which of the two is the dropped field, and what it held, is
  not known; the doc takes the second.
- `file_name_hash` is the hash the cutscene tables compute from a file
  name without `.pas` (`cutscene_file_hash()` in
  `_bss/sequence_scripts/reader.py`). On client 3482 the 2 rows of
  [`sequence_skill.bss`](sequence_skill_bss.md) and the 4 of
  [`sequencetutorial_equipment.bss`](tutorial_equipment_bss.md) all key a
  sequence of this file, and their handlers show the sequence path from
  here (`_bss/sequencetriggerdata/lookup.py`); none of the 1,101 file names
  is a `sequencedatatable.bss` cutscene.
- `folder` writes both separators: `PEDU/EdaniaSub` (3 rows) and
  `PEDU\EdaniaSub` (4 rows) are one folder.
- On client 3482 the rows cover 268 regions and 75 contents groups; the
  157 `PEDU2` rows all have contents group `2186`, the group the `PEDU2`
  videos of [`videotriggerdata.bss`](videotriggerdata_bss.md) have.
- The QA scripts `abyssonehelp.luac` and `qasupportmain.luac` start a
  sequence by name with `ToClient_SequenceTriggerForQA()`.
