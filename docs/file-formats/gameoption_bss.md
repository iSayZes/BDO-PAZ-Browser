# `gameoption.bss` Format

## Purpose

The client's copy of the game option values in one PABR record: battle,
inn, password, revival, mail and awakening settings at the start, then
trade, fishing, alchemy and PvP arena values and long runs of f32 values. The values are the client side of the one-row option sheets,
`BattleOption` and `EtcOption` among them (see Field Names). Only the head,
the first `0xC5` bytes, is decoded; the rest of the record is one byte run
up to the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes   | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------- | ------- | -------------- | --------- |
| 2      | 3464 and later | 3482    | `gameoption.bss` | 123,989 | 1 String Table | 1,546     |
| 1      | 1784           | 1784    | `gameoption.bss` | 329,469 | 1 String Table | 19,847    |

| Layout | File             | Known           | Unknown           |
| ------ | ---------------- | --------------- | ----------------- |
| 2      | `gameoption.bss` | 1,640 B (1.3%)  | 122,349 B (98.7%) |
| 1      | `gameoption.bss` | 19,953 B (6.1%) | 309,516 B (93.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | No documented layout |
| 3454   | No documented layout |
| 3444   | No documented layout |
| 3435   | No documented layout |
| 3426   | No documented layout |
| 3418   | No documented layout |
| 3412   | No documented layout |
| 3402   | No documented layout |
| 3396   | No documented layout |
| 3387   | No documented layout |
| 3381   | No documented layout |
| 3373   | No documented layout |
| 3364   | No documented layout |
| 3356   | No documented layout |
| 3349   | No documented layout |
| 3342   | No documented layout |
| 3335   | No documented layout |
| 3326   | No documented layout |
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No documented layout |
| 3267   | No documented layout |
| 3258   | No documented layout |
| 3251   | No documented layout |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
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
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | No documented layout |
| 1897   | No documented layout |
| 1892   | No documented layout |
| 1886   | No documented layout |
| 1881   | No documented layout |
| 1871   | No documented layout |
| 1866   | No documented layout |
| 1862   | No documented layout |
| 1854   | No documented layout |
| 1846   | No documented layout |
| 1838   | No documented layout |
| 1832   | No documented layout |
| 1826   | No documented layout |
| 1822   | No documented layout |
| 1818   | No documented layout |
| 1804   | No documented layout |
| 1794   | No documented layout |
| 1790   | No documented layout |
| 1784   | Layout 1             |
| 1774   | No documented layout |
| 1771   | No documented layout |
| 1762   | No documented layout |
| 1759   | No documented layout |
| 1754   | No documented layout |
| 1749   | No documented layout |
| 1743   | No documented layout |
| 1737   | No documented layout |
| 1731   | No documented layout |
| 1725   | No documented layout |
| 1717   | No documented layout |
| 1710   | No documented layout |
| 1704   | No documented layout |
| 1698   | No documented layout |
| 1690   | No documented layout |
| 1685   | No documented layout |
| 1680   | No documented layout |
| 1674   | No documented layout |
| 1668   | No documented layout |
| 1659   | No documented layout |
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
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
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
| 652    | No documented layout |
| 643    | No documented layout |
| 637    | No documented layout |
| 630    | No documented layout |
| 627    | No documented layout |
| 621    | No documented layout |
| 617    | No documented layout |
| 615    | No documented layout |
| 606    | No documented layout |
| 599    | No documented layout |
| 592    | No documented layout |
| 586    | No documented layout |
| 577    | No documented layout |
| 569    | No documented layout |
| 561    | No documented layout |
| 554    | No documented layout |
| 542    | No documented layout |
| 532    | No documented layout |
| 531    | No documented layout |
| 526    | No documented layout |
| 521    | No documented layout |
| 517    | No documented layout |
| 510    | No documented layout |
| 508    | No documented layout |
| 504    | No documented layout |
| 497    | No documented layout |
| 491    | No documented layout |
| 485    | No documented layout |
| 478    | No documented layout |
| 472    | No documented layout |
| 466    | No documented layout |
| 457    | No documented layout |
| 452    | No documented layout |
| 449    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset             | Type                 | Field                                    | Notes                                                                       |
| ------------------ | -------------------- | ---------------------------------------- | --------------------------------------------------------------------------- |
| `+0x00`            | char[4]              | magic                                    | ASCII `PABR`                                                                |
| `+0x04`            | bytes[36]            | unknown_04                               | All `0` on client 3482; see Open Questions                                  |
| `+0x28`            | i64                  | inn_rental_time                          | `216000` on client 3482: the sheet's `3600` times 60                        |
| `+0x30`            | i16                  | inn_room_service_time                    | `1` on client 3482                                                          |
| `+0x32`            | bytes[10]            | unknown_32                               | All `0` on client 3482; see Open Questions                                  |
| `+0x3C`            | u32                  | summon_monster_count_limit               | `10` on client 3482                                                         |
| `+0x40`            | f32                  | max_decreasable_hp_by_damage_rate_module | `2000` on client 3482                                                       |
| `+0x44`            | i32                  | max_decreasable_mp_by_damage_rate_module | `1500` on client 3482                                                       |
| `+0x48`            | bytes[13]            | unknown_48                               | A u32 `0`, a u32 `1500000`, a u32 `100000` and a u8 `0` on client 3482 if read in that order |
| `+0x55`            | u64                  | saving_buff_time                         | `10000` on client 3482                                                      |
| `+0x5D`            | u64                  | saving_cool_time                         | `60000` on client 3482                                                      |
| `+0x65`            | bytes[24]            | unknown_65                               | All `0` on client 3482                                                      |
| `+0x7D`            | u8                   | authentic_password_limit                 | `3` on client 3482                                                          |
| `+0x7E`            | u8                   | password_length_min                      | `6` on client 3482                                                          |
| `+0x7F`            | u8                   | password_length_max                      | `12` on client 3482                                                         |
| `+0x80`            | u32                  | revival_product_no                       | `5017` on client 3482                                                       |
| `+0x84`            | u64                  | rescue_cool_time                         | `1800000` on client 3482                                                    |
| `+0x8C`            | u32                  | final_level_up_condition_ref             | Index into `strings`; string `0` (`"0"`) on client 3482                     |
| `+0x90`            | u64                  | mail_remain_time                         | `864000` on client 3482                                                     |
| `+0x98`            | u64                  | unknown_98                               | `259200` on client 3482; see Open Questions                                 |
| `+0xA0`            | i64                  | reset_awakening_need_exp                 | `31000000` on client 3482                                                   |
| `+0xA8`            | u8                   | expired_tent_check_day                   | `28` on client 3482, `14` on client 3283                                    |
| `+0xA9`            | bytes[20]            | unknown_a9                               | All `0` on client 3482                                                      |
| `+0xBD`            | i32                  | attack_to_servant_rate                   | `100000` on client 3482                                                     |
| `+0xC1`            | u32                  | re_awakening_item_key                    | Item key; `44195` (Memory Fragment) on client 3482                          |
| `+0xC5`            | bytes[122238]        | unknown_c5                               | The rest of the record, up to `table_start`; see Values Past the Head and Notes |
| `+0x1DE43`         | String Table         | string_table                             | See String Table                                                            |
| `EOF-0x08`         | u32                  | table_start                              | Offset of the string table, where `unknown_c5` ends                         |
| `EOF-0x04`         | u32                  | zero                                     | Always `0`                                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `21` on client 3482, `1579` on client 1784 |
| `+0x04` | pstr[string_count] | strings      | Every `*_ref` field is an index into `strings`              |

## Layout 1

The head of client 1784: `unknown_04` is 28 bytes, `unknown_32` 12 bytes,
`percent_damage_pv_rate`, `max_local_war_player` and
`siege_bonus_damage_rate` are still in it, `unknown_98` is not, and 4 bytes
sit between `reset_awakening_need_exp` and `expired_tent_check_day`.

### File Layout

| Offset             | Type                 | Field                                    | Notes                                                          |
| ------------------ | -------------------- | ---------------------------------------- | -------------------------------------------------------------- |
| `+0x00`            | char[4]              | magic                                    | ASCII `PABR`                                                   |
| `+0x04`            | bytes[28]            | unknown_04                               | All `0` on client 1784                                         |
| `+0x20`            | i64                  | inn_rental_time                          | `216000` on client 1784                                        |
| `+0x28`            | i16                  | inn_room_service_time                    | `1` on client 1784                                             |
| `+0x2A`            | bytes[12]            | unknown_32                               | A u64 `1` and a u32 `0` on client 1784; see Open Questions     |
| `+0x36`            | u32                  | summon_monster_count_limit               | `10` on client 1784                                            |
| `+0x3A`            | i32                  | percent_damage_pv_rate                   | `3200` on client 1784                                          |
| `+0x3E`            | f32                  | max_decreasable_hp_by_damage_rate_module | `2000` on client 1784                                          |
| `+0x42`            | i32                  | max_decreasable_mp_by_damage_rate_module | `1500` on client 1784                                          |
| `+0x46`            | i32                  | max_local_war_player                     | `30` on client 1784                                            |
| `+0x4A`            | bytes[13]            | unknown_48                               | All `0` on client 1784                                         |
| `+0x57`            | u64                  | saving_buff_time                         | `10000` on client 1784                                         |
| `+0x5F`            | u64                  | saving_cool_time                         | `60000` on client 1784                                         |
| `+0x67`            | bytes[24]            | unknown_65                               | All `0` on client 1784                                         |
| `+0x7F`            | u8                   | authentic_password_limit                 | `3` on client 1784                                             |
| `+0x80`            | u8                   | password_length_min                      | `6` on client 1784                                             |
| `+0x81`            | u8                   | password_length_max                      | `12` on client 1784                                            |
| `+0x82`            | u32                  | revival_product_no                       | `5017` on client 1784                                          |
| `+0x86`            | u64                  | rescue_cool_time                         | `1800000` on client 1784                                       |
| `+0x8E`            | u32                  | final_level_up_condition_ref             | String `0` (`"0"`) on client 1784                              |
| `+0x92`            | u64                  | mail_remain_time                         | `864000` on client 1784                                        |
| `+0x9A`            | i64                  | reset_awakening_need_exp                 | `31000000` on client 1784                                      |
| `+0xA2`            | bytes[4]             | unknown_after_reset_awakening_need_exp   | All `0` on client 1784                                         |
| `+0xA6`            | u8                   | expired_tent_check_day                   | `7` on client 1784                                             |
| `+0xA7`            | bytes[12]            | unknown_a9                               | All `0` on client 1784                                         |
| `+0xB3`            | i32                  | siege_bonus_damage_rate                  | `500000` on client 1784                                        |
| `+0xB7`            | bytes[8]             | unknown_after_siege_bonus_damage_rate    | All `0` on client 1784                                         |
| `+0xBF`            | i32                  | attack_to_servant_rate                   | `100000` on client 1784                                        |
| `+0xC3`            | u32                  | re_awakening_item_key                    | `44195` on client 1784                                         |
| `+0xC7`            | bytes[309415]        | unknown_c5                               | The rest of the record, up to `table_start`                    |
| `+0x4B96E`         | String Table         | string_table                             | See String Table                                               |
| `EOF-0x08`         | u32                  | table_start                              | Offset of the string table, where `unknown_c5` ends            |
| `EOF-0x04`         | u32                  | zero                                     | Always `0`                                                     |

## Values Past the Head

`unknown_c5` holds more sheet values. These two runs match the `EtcOption`
and `BattleOption` sheets value by value on client 1784 and sit in the
same order on client 3482, where most values are unchanged. They are not
in the layout because the bytes before each run change size between
clients. Offsets are file offsets; a dash
means the field is not there.

| Field                                          | Type       | Client 3482 | Client 1784 | Value on client 3482                     | Sheet column                              |
| ---------------------------------------------- | ---------- | ----------- | ----------- | ---------------------------------------- | ----------------------------------------- |
| world_chat_condition                           | i32        | `0xBF8F`    | `0xDE57`    | `99`                                     | `EtcOption.WorldChatCondition`            |
| max_endurance_increase_rate                    | i32        | `0xBF93`    | `0xDE5B`    | `100000` (`0` on client 1784)            | `EtcOption.MaxEnduranceIncreaseRate`      |
| trade_bonus_exp_percent                        | i32        | `0xBF97`    | `0xDE5F`    | `200`                                    | `EtcOption.TradeBonusExpPercent`          |
| trade_bonus_gold_percent                       | i32        | `0xBF9B`    | `0xDE63`    | `68`                                     | `EtcOption.TradeBonusGoldPercent`         |
| max_distance_bonus                             | i32        | `0xBF9F`    | `0xDE67`    | `1500000`                                | `EtcOption.MaxDistanceBonus`              |
| catch_resistance_time                          | u64        | `0xBFA3`    | `0xDE6B`    | `12000`                                  | `EtcOption.CatchResistanceTime`           |
| catch_resistance_rate                          | i32        | `0xBFAB`    | `0xDE73`    | `30000`                                  | `EtcOption.CatchResistanceRate`           |
| catch_resistance_extra_rate                    | i32        | `0xBFAF`    | `0xDE77`    | `5000000`                                | `EtcOption.CatchResistanceExtraRate`      |
| reduce_repair_price_for_seal                   | i32        | `0xBFB3`    | `0xDE7B`    | `670000`                                 | `EtcOption.ReduceRepairPriceForSeal`      |
| endurance_decrease_percent_equip_item_for_seal | i32        | `0xBFB7`    | `0xDE7F`    | `500000`                                 | `EtcOption.EnduranceDecreasePercentEquipItemForSeal` |
| worker_shop_consume_wp                         | u16        | `0xBFBB`    | `0xDE83`    | `5`                                      | `EtcOption.WorkerShopConsumeWp`           |
| world_item_market_consume_wp                   | u16        | `0xBFBD`    | `0xDE85`    | `1`                                      | `EtcOption.WorldItemMarketConsumeWp`      |
| trade_game_bonus_percent                       | i32        | `0xBFBF`    | `0xDE87`    | `50000`                                  | `EtcOption.TradeGameBonusPercent`         |
| trade_game_consume_wp                          | u16        | `0xBFC3`    | `0xDE8B`    | `5`                                      | `EtcOption.TradeGameConsumeWp`            |
| trade_game_try_count                           | i32        | `0xBFC5`    | `0xDE8D`    | `3`                                      | `EtcOption.TradeGameTryCount`             |
| trade_game_goal_interval                       | i32        | `0xBFC9`    | `0xDE91`    | `3`                                      | `EtcOption.TradeGameGoalInterval`         |
| other_region_trade_graph_show_wp               | u16        | `0xBFCD`    | `0xDE95`    | `1`                                      | `EtcOption.OtherRegionTradeGraphShowWp`   |
| territory_supply_max_sell_rate                 | i32        | `0xBFCF`    | `0xDE97`    | `2500000`                                | `EtcOption.TerritorySupplyMaxSellRate`    |
| trade_supply_max_sell_rate                     | i32        | `0xBFD3`    | `0xDE9B`    | `2500000`                                | `EtcOption.TradeSupplyMaxSellRate`        |
| dyeing_combine_item                            | u32        | `0xBFD7`    | `0xDE9F`    | `17030` (Unknown Dye Box)                | `EtcOption.DyeingCombineItem`             |
| day_random_shop_consume_wp                     | u16        | `0xBFEB`    | `0xDEAF`    | `10`                                     | `EtcOption.DayRandomShopConsumeWp`        |
| free_revival_level                             | i32        | `0xBFED`    | `0xDEB1`    | `20`                                     | `EtcOption.FreeRevivalLevel`              |
| fishing_add_rate                               | f32        | `0xBFF1`    | `0xDEB5`    | `2.5`                                    | `EtcOption.FishingAddRate`                |
| fishing_decrease_endurance_rate                | i32        | `0xBFF5`    | `0xDEB9`    | `900000`                                 | `EtcOption.FishingDecreaseEnduranceRate`  |
| fishing_decrease_endurance_rate_add_per_level  | i32        | `0xBFF9`    | `0xDEBD`    | `5000`                                   | `EtcOption.FishingDecreaseEnduranceRateAddPerLevel` |
| fishing_minimum_decrease_endurance_rate        | i32        | `0xBFFD`    | `0xDEC1`    | `400000`                                 | `EtcOption.FishingMinimumDecreaseEnduranceRate` |
| alchemy_residue_item_key                       | u32        | `0xC001`    | `0xDEC5`    | `9725` (Burnt Reagent)                   | `EtcOption.AlchemyResidueItemKey`         |
| alchemy_residue_error_count                    | i32        | `0xC005`    | `0xDEC9`    | `3`                                      | `EtcOption.AlchemyResidueErrorCount`      |
| cook_residue_item_key                          | u32        | `0xC009`    | `0xDECD`    | `9724` (Failed Dish)                     | `EtcOption.CookResidueItemKey`            |
| cook_residue_error_count                       | i32        | `0xC00D`    | `0xDED1`    | `3`                                      | `EtcOption.CookResidueErrorCount`         |
| node_increase_item_drop_percent                | i32        | `0xC011`    | `0xDED5`    | `50000`                                  | `EtcOption.NodeIncreaseItemDropPercent`   |
| supply_shop_interval                           | i16        | `0xC01D`    | `0xDED9`    | `3`                                      | `EtcOption.SupplyShopInterval`            |
| supply_shop_refresh_percent                    | i32        | `0xC01F`    | `0xDEDB`    | `100`                                    | `EtcOption.SupplyShopRefreshPercent`      |
| territory_supply_shop_interval                 | i16        | `0xC023`    | `0xDEDF`    | `4`                                      | `EtcOption.TerritorySupplyShopInterval`   |
| alchemy_stone_up_grade_rate                    | i32[8]     | `0xC025`    | `0xDEE1`    | `3000, 1000, 750, 2000, 800, 700, 500, 0` (`3000, 1000, 750, 250, 65, 13, 2, 0` on client 1784) | `EtcOption.AlchemyStoneUpGradeRate_1` |
| pruning                                        | u32 (u16 on client 1784) | `0xC045` | `0xDF01` | `57965`                               | `EtcOption.Pruning`                       |
| catchbug                                       | u32 (u16 on client 1784) | `0xC049` | `0xDF03` | `57966`                               | `EtcOption.Catchbug`                      |
| localwar_item_rate                             | i32        | -           | `0xDF05`    | -                                        | `EtcOption.LocalwarItemRate` (`750000`)   |
| localwar_item_key                              | u32        | -           | `0xDF09`    | -                                        | `EtcOption.LocalwarItemKey` (`450`)       |
| horserace_item_key                             | u32        | -           | `0xDF0D`    | -                                        | `EtcOption.HorseraceItemKey` (`1001`)     |
| prevent_downgrade_item_key                     | u32        | `0xC04D`    | `0xDF11`    | `16080` (Cron Stone)                     | `EtcOption.PreventDowngradeItemKey`       |
| promotion_enchant_item_key                     | u32        | `0xC051`    | `0xDF15`    | `721003` (Caphras Stone)                 | `EtcOption.PromotionEnchantItemKey`       |
| accessory_broken_rate                          | i32        | `0xC055`    | `0xDF19`    | `400000`                                 | `EtcOption.AccessoryBrokenRate`           |
| min_random_price                               | i32        | `0xC059`    | `0xDF1D`    | `1000000`                                | `EtcOption.MinRandomPrice`                |
| added_pet_collect_drop_rate                    | i32        | `0xC05D`    | `0xDF21`    | `-700000`                                | `EtcOption.AddedPetCollectDropRate`       |
| commerce_type_for_trade_game                   | u8         | `0xC061`    | `0xDF25`    | `7`                                      | `EtcOption.CommerceTypeForTradeGame`      |
| commerce_type_for_trade_game_percent           | i32        | `0xC062`    | `0xDF26`    | `2000000`                                | `EtcOption.CommerceTypeForTradeGamePercent` |
| world_chat_item_keys                           | u64 count, u32 each | `0xC066` | `0xDF2A` | `17645` ([Event] Megaphone), `18851` (Megaphone) | `EtcOption.WorldChatItemKey`  |
| user_chat_block_with_item                      | u32        | -           | `0xDF3A`    | -                                        | `EtcOption.UserChatBlockWithItem` (`65208`) |
| desert_storm_shielder_character_keys           | u64 count, u16 each | `0xC076` | `0xDF3E` | `910`                                | `EtcOption.DesertStormShielderCharacterKey` |
| resist_desert                                  | u32 count, u32 each | `0xC080` | `0xDF48` | `16012, 16016, 18858, 608814, 750567, 751503` (five on client 1784, no `608814`) | `EtcOption.ResistDesert` |
| add_resist_value                               | u64 count, i32 each | `0xC09C` | `0xDF60` | `1, 1, 1, 1, 1, 1`                   | `EtcOption.AddResistValue`                |
| pvp_arena_return_position                      | f32[3]     | `0x1CD73`   | `0x4AE04`   | `140974, -763, 347416`                   | `BattleOption.PvpArenaReturnPosition`     |
| pvp_arena_battle_time                          | u64        | `0x1CD7F`   | `0x4AE10`   | `180000`                                 | `BattleOption.PvpArenaBattleTime`         |
| play_ground_enter_position                     | f32[3]     | `0x1CD87`   | `0x4AE18`   | `138476, 357, 337361`                    | `BattleOption.PlayGroundEnterPosition`    |
| pvp_arena_champion_position                    | f32[3]     | `0x1CD93`   | `0x4AE24`   | `137989, -1003, 345971`                  | `BattleOption.PvpArenaChampionPosition`   |
| pvp_arena_challenger_position                  | f32[3]     | `0x1CD9F`   | `0x4AE30`   | `137800, -1000, 347949`                  | `BattleOption.PvpArenaChallengerPosition` |

The gaps in the `EtcOption` run hold values no column matches: three f32
after `dyeing_combine_item` (`-0.4`, `120`, `1.8` on both clients) and a
fourth (`100`) on client 3482 only, and an i32 `5000` and an i32 `2000000`
after `node_increase_item_drop_percent` on client 3482 only. The sheet's
`AlchemyStoneUpGradeRate_1` holds seven numbers; the file stores eight, the
last `0`. `resist_desert` is stored in ascending order, the sheet lists the
keys in another order. The item names come from LOC type `0`.

## Field Names

The names come from the `BattleOption` and `EtcOption` sheets of a private
server's `DataSheets.bexcel` on client 1784 (one row each), matched by
value against the client 1784 file, and from the loaders of that private
server's game server build on client 1784, which read the columns in the
order the head stores them. The private server's values are edited, so
only the column names carry over.

The named head fields follow the `BattleOption` loader's read order:
`InnRentalTime`, `InnRoomServiceTime`, `DecreaseDropRate`,
`SummonMonsterCountLimit`, `PersentDamegePvRate`,
`MaxDecreasableHpByDamageRateModule`, `MaxDecreasableMpByDamageRateModule`,
`MaxLocalWarPlayer`, then (after `GuildWareHouseSlotDefault`,
`MonsterPowerInNight`, `MonsterExperienceInNight` and `UseChannelInstance`)
`SavingBuffTime`, `SavingCoolTime`, `TradeSummaryInterval`,
`CollectSpawnPercentInServerBeginning`, `CollectAwakeDelay`,
`CollectSpawnPercentForDelay`, `AuthenticPasswordLimit`,
`PasswordLengthMin`, `PasswordLengthMax`, `RevivalProductNo`,
`RescueCoolTime`, `FinalLevelUpCondition`, `MailRemainTime`,
`ResetAwakeningNeedExp`, `SuperSkillBaseRate`, `ExpiredTentCheckDay`, six
rate columns with `SiegeBonusDamageRate` fourth, `AttackToServantRate` and
`ReAwakeningItemKey`. The loader multiplies `InnRentalTime` by 60 and
stores it as an i64, which is why the file holds `216000` for the sheet's
`3600`. The client 1784 file matches the sheet for every named field:
`3600` (times 60), `1`, `10`, `3200`, `2000`, `1500`, `30`, `10000`,
`60000`, `3`, `6`, `12`, `5017`, `1800000`, `"0"`, `864000`, `31000000`,
`7`, `500000`, `100000` and `44195`. The 28 bytes of `unknown_04` on
client 1784 are as long as the five i32 and the u64 the loader reads before
`InnRentalTime` (`BackAttackDamageRate` to `SpeedAttackDamageRate`, then
`ActionRestrictionRemainTick`), all `0` in the sheet; zero bytes stay
unknown here. `percent_damage_pv_rate` is the column
`PersentDamegePvRate`.

The fields keep their name on client 3482 where the bytes around them
line up with the client 1784 file: the values are the same there except
`expired_tent_check_day` (`28`).

## Notes

- `unknown_c5` changes length with most patches: 122,521 bytes on client
  3412, 122,238 on clients 3474 and 3482. The layouts give its length
  on the clients they were written from, so each layout fits only the
  clients whose head it describes; a run up to `table_start` would let
  Layout 2 walk every client back to 805. The Layout 2 head also holds on
  clients 3037, 3062, 3283 and 3412, and the Layout 1 head on clients 1485
  and 2052 (checked by hand); their `unknown_c5` has another length.
- The handler (`_bss/gameoption/`) shows one row per named head field,
  with the item name of `re_awakening_item_key` and the string of
  `final_level_up_condition_ref`, then one row per string. `unknown_c5` is
  only counted.
- On client 3482, string `1` is `getLevel()<5`, the text of
  `EtcOption.TutorialCondition`, and strings `18` and `19` are
  `checkPeriod(...)` conditions; the fields that point at them are in
  `unknown_c5`.

## Open Questions

### The Record Past the Head

`unknown_c5` is 122,238 bytes on client 3482. It is not the 2016
`gc::GameOptionManager` members in declaration order: the head starts with
`InnRentalTime` where that struct starts with `_isBranchCheck` and
`_summonMonsterLimitCount`, and `MaxLocalWarPlayer` follows
`MaxDecreasableMpByDamageRateModule` although the struct stores it much
later. It follows the server loaders in runs, with jumps between them: the
`BattleOption` PvP arena values sit near the end, and the
`EtcOption` run (see Values Past the Head) stores its values in a
different order from the loader in places. Ahead of the `EtcOption` run,
client 1784 holds `43200000` at `0xDB8F`, the value of
`ServantOption.MatingRegistTime`. From `0x255` on client 3482, long runs
of ascending f32 values start (`5`, `10`, `15`, `20` and up). Mapping the
other loaders that fill the option manager (`ServantOption`,
`GuildOption`, `MovementVerifyOption`, `ItemMarket`, `LocalizingOption`)
the same way would split `unknown_c5` into structures.

### The Zero Blocks of the Head

`unknown_04`, `unknown_48`, `unknown_65` and `unknown_a9` sit where the
`BattleOption` loader reads columns that are `0` in the sheet, so no value
confirms them. `unknown_04` grows from 28 bytes (client 1784) to 36 (client
3482), so 8 bytes were inserted in it. `unknown_32` sits where the loader
reads `DecreaseDropRate`: on client 1784 a u64 `1` and a u32 `0`, which
reads as a counted list holding the sheet's one value `0`; on client 3482
it is 10 zero bytes, which a u64 count of `0` and two more bytes would
explain. On client 3482 `unknown_48` holds `1500000` and `100000`, where
client 1784 has zero bytes.

### `unknown_98`

A u64 `259200` between `mail_remain_time` and `reset_awakening_need_exp`,
from client 2414 on (client 2052 does not have it). No `BattleOption` or
`EtcOption` column holds that value.

### The Heads of Clients 2414 to 3002

Clients 2414 to 2736 hold the client 1784 head with `unknown_98` added,
and client 2736 has 4 bytes fewer between `expired_tent_check_day` and
`attack_to_servant_rate`. Client 3002 holds the client 3482 head with
`percent_damage_pv_rate` still after `summon_monster_count_limit`. No
layout covers them yet.
