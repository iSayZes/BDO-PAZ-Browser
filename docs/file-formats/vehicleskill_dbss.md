# `vehicleskill.dbss` Format

## Purpose

Mount and ship skills: one record per skill with its Korean name, skill EXP
cap, price, icon, key-command and description texts, contents groups,
condition, lock flag, the ship skills' display order and the Training level
that unlocks auto-sprint. On client 3474 the file has 106 records, keys 1 to
106, from Hind Kick (1) and Drift (3) to the ship skills such as
`충각 (항해 초급Lv.1이상)` (Ram, 36).
[servant.bss](servant_bss.md) lists the skills each servant starts with by
these keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes                    |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | ---------------------------- |
| 1      | 1572 and later | 3483    | `vehicleskill.dbss`       | 70,285 | 106 Record     | 268 to 1,646, 663 on average |
| 1      | 1572 and later | 3483    | `vehicleskilloffset.dbss` | 974    | 106 Offset Row | 9                            |

| Layout | File                      | Known            | Unknown        |
| ------ | ------------------------- | ---------------- | -------------- |
| 1      | `vehicleskill.dbss`       | 69,012 B (98.2%) | 1,273 B (1.8%) |
| 1      | `vehicleskilloffset.dbss` | 974 B (100.0%)   | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
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
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
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
| 1280   | No file              |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
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

| File                      | Required | Role                                                               |
| ------------------------- | -------- | ------------------------------------------------------------------ |
| `vehicleskilloffset.dbss` | Optional | PABR index: key to the record's offset and size                    |
| `languagedata_en.loc`     | Optional | LOC type 8, `str_id1` = `key`: `str_id4` 0 name, 1 key command, 3 description, 4 console key command |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field      | Notes                                         |
| ------- | ------------- | ---------- | --------------------------------------------- |
| `+0x00` | u8            | unknown_00 | `count` + 1 on clients 1784 (77) and 3474 (107) |
| `+0x01` | u32           | count      | 106 on client 3474                            |
| `+0x05` | Record[count] | records    | Back to back in key order, up to EOF          |

### Record (variable: 104 bytes + texts and contents groups)

| Offset                                | Type                         | Field                                | Notes |
| ------------------------------------- | ---------------------------- | ------------------------------------ | ----- |
| `+0x00`                               | u8                           | key                                  | 1 to 106 on client 3474 |
| `+0x01`                               | str16                        | name_kr                              | `뒷발차기` (Hind Kick) |
| `name_kr+0x00`                        | u32                          | max_exp                              | 30,000 on every record (client 3474) |
| `name_kr+0x04`                        | u32                          | add_exp_for_check                    | |
| `name_kr+0x08`                        | u64                          | base_price                           | |
| `name_kr+0x10`                        | u32                          | add_mating_rate                      | 0, or 20,000 to 40,000 on 5 records (client 3474) |
| `name_kr+0x14`                        | u8                           | is_learn_from_item                   | 1 on 16 records (client 3474) |
| `name_kr+0x15`                        | str16                        | icon_path                            | `New_Icon\04_PC_Skill/06_Riding_Skill/Riding_Skill_0004.dds` |
| `icon_path+0x00`                      | str16                        | desc_kr                              | Key command, `뒷발 공격 ↓+ F`; LOC `str_id4` 1 |
| `desc_kr+0x00`                        | str16                        | desc2_kr                             | Description with `<PAColor>` tags and `\n`; LOC `str_id4` 3 |
| `desc2_kr+0x00`                       | str16                        | console_desc_kr                      | Key command with `{KeyBind:...}`; LOC `str_id4` 4 |
| `console_desc_kr+0x00`                | str16                        | training_skill_characters            | Empty, or servant character IDs as text (`9989, 9889`) on keys 49 to 51 |
| `training_skill_characters+0x00`      | u8                           | is_market_filter                     | |
| `training_skill_characters+0x01`      | u32                          | contents_group_count                 | 1, or 2 on 4 records (client 3474) |
| `training_skill_characters+0x05`      | u32[contents_group_count]    | contents_group_key_hashes            | `key_hash` of each contents group key; `"0"` hashes to `1612107767` |
| `contents_group_key_hashes+0x00`      | bytes[8]                     | unknown_contents_group_key_hashes_00 | `0` on every record (clients 1784 and 3474) |
| `contents_group_key_hashes+0x08`      | str16                        | condition_desc                       | Empty, or a script call such as `VEHICLESKILL_CONDITION_4();` on 19 records (client 3474) |
| `condition_desc+0x00`                 | u8                           | vehicle_skill_lock                   | 0 on 9 records (client 3474) |
| `condition_desc+0x01`                 | u32                          | unknown_condition_desc_01            | `0` on every record (clients 1784 and 3474) |
| `condition_desc+0x05`                 | u32                          | skill_order                          | 0, or 101 to 115 on the 15 ship skills (client 3474) |
| `condition_desc+0x09`                 | u32                          | need_life_level_for_auto_skill       | 0, or 31 on the 5 sprint skills (client 3474) |

### `vehicleskilloffset.dbss`

| Offset              | Type              | Field              | Notes                                        |
| ------------------- | ----------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                                       |
| `+0x04`             | u32               | count              | Equals the main file's `count`               |
| `+0x08`             | Offset Row[count] | entries            | Key order                                    |
| `entries+0x00`      | String Table      | string_table       | Present but empty                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`            |
| `string_table+0x04` | u32               | zero               | `0`                                          |

### Offset Row (9 bytes)

| Offset  | Type | Field  | Notes                                         |
| ------- | ---- | ------ | --------------------------------------------- |
| `+0x00` | u8   | key    | The record's `key`                            |
| `+0x01` | u32  | offset | Start of the record; the first is `5`         |
| `+0x05` | u32  | size   | Record size; each record ends where the next starts |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Field Names

The names follow the `VehicleSkill_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against client
1784 (76 records, every one in the sheet) and the 76 client 3474 records in
the sheet:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index`, `Name`, `Icon` | `key`, `name_kr`, `icon_path` | 76 | 76 |
| `MaxExp`, `AddMatingRate`, `IsLearnFromItem` | `max_exp`, `add_mating_rate`, `is_learn_from_item` | 76 | 76 |
| `AddExpForCheck` | `add_exp_for_check` | 76 | 72 |
| `basePrice` | `base_price` | 76 | 12 |
| `Desc`, `Desc2`, `ConsoleDesc` | `desc_kr`, `desc2_kr`, `console_desc_kr` | 76 | 65, 61, 63 |
| `IsTrainingSkill` | `training_skill_characters` | 76 | 76 |
| `isMarketFilter` | `is_market_filter` | 76 | 76 |
| `ContentsGroupKey` (comma list) | `contents_group_key_hashes`, by `key_hash` | 76 | 76 |
| `ConditionDesc`, `VehicleSkillLock` | `condition_desc`, `vehicle_skill_lock` | 76 | 76 |
| `isSkillOrder` | `skill_order` | 76 | 68 |
| `LifeExperienceLevForAutoSkill` | `need_life_level_for_auto_skill` | 71 | 71 |

`key_hash` is the client's contents group key hash
([contentsgroupoptionstaticstatusmanager.bss](contentsgroupoptionstaticstatusmanager_bss.md#key-hash)):
`ContentsGroupKey` `284,80` is stored as the two hashes of `"284"` and
`"80"`, and an empty cell as the hash of `"0"`.

`need_life_level_for_auto_skill` is 41 on client 1784 and 31 on client 3474
for Sprint (4), `빠른발걸음` (22), `빠른 뛰기` (28), `숲의 질주` (55) and
`달려달려` (62); the sheet and the private server's own compiled file hold 0
there. The client Lua confirms the field: the horse stamina widget
(`horsemp`, `panel_widget_horsemp_renew`) blocks auto-sprint while the
player's life level is below `vehicleProxy:getNeedLifeLevelForAutoSkill(skillKey)`
(`LUA_AUTOSPRINT_CANNOTUSE`).

`skill_order` holds the column `isSkillOrder`, which is a number, not a flag:
the 15 ship skills on client 3474 run 101 to 115, the 10 on client 1784
101 to 110, and the new skills moved the old ones (Ram 101 on both,
`급발진` 105 on client 1784 and 108 on client 3474). `training_skill_characters` holds the column
`IsTrainingSkill`, a text list of servant character IDs (9989 and 9889 are
the male and female Arduanatt); the servant windows hide skills whose
wrapper says `isTrainingSkill()`. The client 3474 text misses are rewrites
of the descriptions and key hints; the price and EXP misses are rebalances.

The sheet's `PriceRate_0` to `PriceRate_2` (1,000,000 on every row) have no
field.

## Notes

- Client 1784 has the same layout with 76 records; 30 skills were added by
  client 3474.
- The highest key plus one is in its own one-byte file,
  [vehicleskillcount.dbss](vehicleskillcount_dbss.md). The skills each
  servant can learn are in
  [vehicleskillowner.dbss](vehicleskillowner_dbss.md).

## Open Questions

### The Header Byte and Zero Fields

`unknown_00` holds the same value as
[vehicleskillcount.dbss](vehicleskillcount_dbss.md) on clients 1485 to
3474: the highest key plus one, the 2016
`gc::VehicleSkillStaticStatusManager::_count`. The keys have no gap on any
of these clients, so the byte cannot be told apart from the record count
plus one, and nothing shows which of the two files the client takes
`_count` from. `unknown_contents_group_key_hashes_00`
(8 bytes) and `unknown_condition_desc_01` (u32) are `0` on every record of
both clients and match no sheet column.
