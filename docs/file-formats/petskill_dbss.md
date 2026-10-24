# `petskill.dbss` Format

## Purpose

Pet skill levels. Each record is keyed by `pet_skill_id`, has a skill type that names it in the pet window, and holds ten level entries with two effect parameters each. Companion `petskilloffset.dbss` provides keyed lookup into the variable-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------------------------------------- | --------- |
| 2      | 1881 and later | 3483    | `petskill.dbss`       | 9,380 | 490 Level Entry, 49 Payload, 49 Record | 17        |
| 2      | 1881 and later | 3483    | `petskilloffset.dbss` | 494   | 49 Offset Row                          | 10        |
| 1      | 1346 to 1871   | 1871    | `petskill.dbss`       | 8,606 | 460 Level Entry, 46 Payload, 46 Record | 17        |
| 1      | 1346 to 1871   | 1871    | `petskilloffset.dbss` | 464   | 46 Offset Row                          | 10        |

| Layout | File                  | Known           | Unknown      |
| ------ | --------------------- | --------------- | ------------ |
| 2      | `petskill.dbss`       | 8,775 B (93.6%) | 605 B (6.4%) |
| 2      | `petskilloffset.dbss` | 396 B (80.2%)   | 98 B (19.8%) |
| 1      | `petskill.dbss`       | 8,238 B (95.7%) | 368 B (4.3%) |
| 1      | `petskilloffset.dbss` | 372 B (80.2%)   | 92 B (19.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
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
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
| 2717   | Layout 2             |
| 2709   | Layout 2             |
| 2703   | Layout 2             |
| 2695   | Layout 2             |
| 2684   | Layout 2             |
| 2672   | Layout 2             |
| 2665   | Layout 2             |
| 2657   | Layout 2             |
| 2649   | Layout 2             |
| 2644   | Layout 2             |
| 2637   | Layout 2             |
| 2629   | Layout 2             |
| 2619   | Layout 2             |
| 2612   | Layout 2             |
| 2606   | Layout 2             |
| 2602   | Layout 2             |
| 2601   | Layout 2             |
| 2592   | Layout 2             |
| 2583   | Layout 2             |
| 2575   | Layout 2             |
| 2567   | Layout 2             |
| 2560   | Layout 2             |
| 2553   | Layout 2             |
| 2545   | Layout 2             |
| 2538   | Layout 2             |
| 2529   | Layout 2             |
| 2519   | Layout 2             |
| 2513   | Layout 2             |
| 2510   | Layout 2             |
| 2507   | Layout 2             |
| 2503   | Layout 2             |
| 2498   | Layout 2             |
| 2492   | Layout 2             |
| 2487   | Layout 2             |
| 2480   | Layout 2             |
| 2474   | Layout 2             |
| 2468   | Layout 2             |
| 2460   | Layout 2             |
| 2453   | Layout 2             |
| 2444   | Layout 2             |
| 2438   | Layout 2             |
| 2434   | Layout 2             |
| 2429   | Layout 2             |
| 2421   | Layout 2             |
| 2414   | Layout 2             |
| 2407   | Layout 2             |
| 2401   | Layout 2             |
| 2397   | Layout 2             |
| 2393   | Layout 2             |
| 2384   | Layout 2             |
| 2378   | Layout 2             |
| 2372   | Layout 2             |
| 2358   | Layout 2             |
| 2352   | Layout 2             |
| 2347   | Layout 2             |
| 2343   | Layout 2             |
| 2335   | Layout 2             |
| 2327   | Layout 2             |
| 2324   | Layout 2             |
| 2319   | Layout 2             |
| 2313   | Layout 2             |
| 2308   | Layout 2             |
| 2302   | Layout 2             |
| 2295   | Layout 2             |
| 2290   | Layout 2             |
| 2284   | Layout 2             |
| 2276   | Layout 2             |
| 2269   | Layout 2             |
| 2259   | Layout 2             |
| 2250   | Layout 2             |
| 2243   | Layout 2             |
| 2235   | Layout 2             |
| 2229   | Layout 2             |
| 2224   | Layout 2             |
| 2218   | Layout 2             |
| 2215   | Layout 2             |
| 2207   | Layout 2             |
| 2203   | Layout 2             |
| 2196   | Layout 2             |
| 2192   | Layout 2             |
| 2189   | Layout 2             |
| 2183   | Layout 2             |
| 2179   | Layout 2             |
| 2171   | Layout 2             |
| 2163   | Layout 2             |
| 2156   | Layout 2             |
| 2151   | Layout 2             |
| 2147   | Layout 2             |
| 2142   | Layout 2             |
| 2138   | Layout 2             |
| 2134   | Layout 2             |
| 2130   | Layout 2             |
| 2122   | Layout 2             |
| 2107   | Layout 2             |
| 2098   | Layout 2             |
| 2089   | Layout 2             |
| 2081   | Layout 2             |
| 2073   | Layout 2             |
| 2067   | Layout 2             |
| 2063   | Layout 2             |
| 2059   | Layout 2             |
| 2052   | Layout 2             |
| 2044   | Layout 2             |
| 2039   | Layout 2             |
| 2032   | Layout 2             |
| 2025   | Layout 2             |
| 2011   | Layout 2             |
| 2005   | Layout 2             |
| 2000   | Layout 2             |
| 1996   | Layout 2             |
| 1991   | Layout 2             |
| 1985   | Layout 2             |
| 1980   | Layout 2             |
| 1969   | Layout 2             |
| 1964   | Layout 2             |
| 1958   | Layout 2             |
| 1950   | Layout 2             |
| 1945   | Layout 2             |
| 1937   | Layout 2             |
| 1933   | Layout 2             |
| 1927   | Layout 2             |
| 1921   | Layout 2             |
| 1914   | Layout 2             |
| 1908   | Layout 2             |
| 1897   | Layout 2             |
| 1892   | Layout 2             |
| 1886   | Layout 2             |
| 1881   | Layout 2             |
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
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
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
| 1276   | No file              |
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

| File                   | Required | Role                                                |
| ---------------------- | -------- | --------------------------------------------------- |
| `petskilloffset.dbss`  | Required | `pet_skill_id -> (data_offset, data_size)` lookup   |
| `stringtable.bss`      | Optional | Key hashes of the skill type names, see Skill Types |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petskilloffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                                |
| ------- | ------------- | ------- | ------------------------------------ |
| `+0x00` | u32           | count   | Number of records; 49 on client 3473 |
| `+0x04` | Record[count] | records | See Record                           |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_skill_id`                                  |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 19 bytes + levels and list, size from `petskilloffset.dbss`)

| Offset        | Type                     | Field              | Notes                                                        |
| ------------- | ------------------------ | ------------------ | ------------------------------------------------------------ |
| `+0x00`       | u16                      | pet_skill_id       | Equals the key prefix and the offset-table key               |
| `+0x02`       | u8                       | skill_type         | 1 to 11 on client 3473, see Skill Types                      |
| `+0x03`       | i32                      | unknown_03         | Always `1`; the place of the 2016 `_petRequireLevel` (Notes) |
| `+0x07`       | u32                      | unknown_07         | Always `10`; the place of the 2016 `_skillMaxCount` (Notes)  |
| `+0x0B`       | u32                      | level_count        | `10` on every record                                         |
| `+0x0F`       | Level Entry[level_count] | levels             | Level 1 first                                                |
| `levels+0x00` | u32                      | unknown_list_count | `0` or `1`                                                   |
| `levels+0x04` | u8[unknown_list_count]   | unknown_list       | `9` or `10` when present                                     |

On client 3473, 32 payloads have an empty list (189 bytes) and 17 hold one
byte (190 bytes): `10` on the three type 9 skills (41 to 43), `9` on 14
skills of types 1, 2, 6, 10 and 11 (44 to 57).

### Level Entry (17 bytes)

One `gc::PetSkillParam` of the 2016 client (`_type`, `_level`, `_param[2]`),
after its map key.

| Offset  | Type | Field      | Notes                                                                          |
| ------- | ---- | ---------- | ------------------------------------------------------------------------------ |
| `+0x00` | i32  | level_dup  | Equals `level`; the key of the 2016 `_skillList` map                           |
| `+0x04` | u8   | skill_type | Equals the payload's `skill_type`                                              |
| `+0x05` | i32  | level      | 1 to 10                                                                        |
| `+0x09` | i32  | param_0    | The sheet's `Param0` (Notes); 2,000 to 500,000 on client 3473                  |
| `+0x0D` | i32  | param_1    | The sheet's `Param1`; 0 to 300,000 on client 3473, 0 on 200 of the 490 entries |

Earlier versions of this doc read the payload one byte off, as eleven 17-byte
rows of u8 `skill_type`, u8 `row_level`, u16 and three u32 (`raw_value_a`,
`raw_value_b`, `unknown_0c`) and a trailing u8 `unknown_bd`. The "baseline
row" was the payload head (`skill_type`, `1`, `10`, `10`) and the level 1
key; `raw_value_a` and `raw_value_b` were `param_0` and `param_1` times 256,
`unknown_0c` the next entry's `level_dup` and `unknown_bd` the list byte.

### `petskilloffset.dbss`

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Equals the `petskill.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                        |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_skill_id | Matches `pet_skill_id` in the main record                                    |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petskill.dbss` to the payload, after the key prefix |
| `+0x06` | u16  | data_size    | 189 or 190 bytes on client 3473                                              |
| `+0x08` | u16  | unknown_08   | Always 0                                                                     |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix.

## Layout 1

On client 1784 every payload is 185 bytes: it ends after the tenth level
entry, with no `unknown_list_count`. Only the Payload differs from Layout 2.

### Payload (variable: 15 bytes + levels, size from `petskilloffset.dbss`)

| Offset  | Type                     | Field        | Notes                                          |
| ------- | ------------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u16                      | pet_skill_id | Equals the key prefix and the offset-table key |
| `+0x02` | u8                       | skill_type   |                                                |
| `+0x03` | i32                      | unknown_03   | Always `1`                                     |
| `+0x07` | u32                      | unknown_07   | Always `10`                                    |
| `+0x0B` | u32                      | level_count  | `10` on every record                           |
| `+0x0F` | Level Entry[level_count] | levels       | Level 1 first                                  |

## Observed Values

Client 3473:

| Field          | Observed values / range                           |
| -------------- | ------------------------------------------------- |
| `pet_skill_id` | 1 to 6, 11 to 18, 21 to 23, 26 to 57 (49 records) |
| `skill_type`   | 1 to 11                                           |
| `param_0`      | 2,000 to 500,000                                  |
| `param_1`      | 0 to 300,000                                      |
| `unknown_list` | empty, `9` or `10`                                |

`skill_type` is not unique: multiple `pet_skill_id` records share one value while carrying different parameters.

## Skill Types

`skill_type` is the 2016 `gc::PetSkillParam::PetSkillType`, which Lua reads as `skillParam._type`. It equals the `PetSkillType` column of the `Pet_Skill_Table` sheet of a private server on client 1784 on all 46 shared skills. The pet info window (`setPetSkillType` in `panel_window_petinfo_all_1.luac`) shows one GAME sheet string per type, prefixed `LUA_PETINFO_PETSKILLTYPE_`. Types 11 to 14 are newer than the 2016 enum. English text from client 3473:

| Type | 2016 enum | Key suffix | English text |
| ---: | --------- | ---------- | ------------ |
| 1  | `ePetSkill_Looting` | `ITEMGETTIME` | Loot (every {itemGetTime} sec) |
| 2  | `ePetSkill_AlertCollect` | `FINDGATHER` | Finds Resources |
| 3  | `ePetSkill_AlertMurderer` | `FINDPK` | Hostility Detection |
| 4  | `ePetSkill_DetectPosition` | `FINDPLACE` | Location Find |
| 5  | `ePetSkill_Aggro` | `MOBAGGRO` | Taunt Monster |
| 6  | `ePetSkill_FindNamedMonster` | `FINDRAREMONSTER` | Finds Rare Monsters |
| 7  | `ePetSkill_ReduceAutoFishingTime` | `REDUCEAUTOFISHINGTIME` | Auto-fishing Time Reduction |
| 8  | `ePetSkill_RegistForRegionSkill` | `REGISTILL` | Resistance to Desert Illnesses |
| 9  | `ePetSkill_Collecting` | `AUTOGETHERING` | Auto Gathering |
| 10 | `ePetSkill_CollectingBoost` | `GETHERINGINCREASE` | Gathering Quantity Increase |
| 11 | - | `HPRECOVERY` | Restore HP |
| 12 | - | `MPRECOVERY` | Endurance/MP Recovery |
| 13 | - | `FINDLOSTNORMALITEM` | Find Normal Lost Item |
| 14 | - | `FINDLOSTSPECIALITEM` | Find Special Lost Item |

The client fills `{itemGetTime}` from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code the browser cannot reproduce, so the handler shows `?` there. The window prints the first pet skill as "Basic: ..." and the second as "Special: ...".

The parser yields one record per level entry, ten per pet skill.

## Notes

- File size is 9,380 bytes on client 3473: 4-byte count plus 49 wrapper records.
- `petskilloffset.dbss` size is 494 bytes on client 3473: 4-byte count plus 49 x 10-byte offset rows.
- `unknown_08` of the offset table is 0 in every record.
- Offset rows are sorted descending for high IDs first, not ascending by key.
- The 2016 client's `gc::PetSkillStaticStatus` holds `_petSkillKey` (u16), `_type` (u8), `_petRequireLevel` (i32), `_skillMaxCount` (u32) and `_skillList`, a map from int to `gc::PetSkillParam`. The payload follows that order. `unknown_03` and `unknown_07` stay unnamed: they are `1` and `10` on every record of both clients, and `Pet_Skill_Table` has no column for them.
- `skill_type`, `level`, `param_0` and `param_1` follow the `Pet_Skill_Table` sheet (`PetSkillNo`, `PetSkillType`, `Level`, `Param0`, `Param1`) of a private server's `DataSheets.bexcel` on client 1784. The private server's own file matches it on all 460 level entries. Client 3473 matches `PetSkillType` on all 460 shared entries, `Param0` on 190 and `Param1` on 274; the other values changed since.
- This file is distinct from `petequipskill.bss`, which stores localized equip-skill catalog entries.
- [pet.dbss](pet_dbss.md) keys this file twice per pet: `loot_skill_id` and `race_skill_id`. Every value of both is a `pet_skill_id` here.

## Open Questions

### Parameter Units

`param_0` and `param_1` mean something different per skill type. Loot (type 1) holds 2,000 to 8,000 in `param_0`, and Restore HP (type 11) falls from 14,000 at level 1 to 5,000 at level 10, which reads as an interval in milliseconds. The loot text gets its time from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code that does not show which field `param` is.

### The Trailing List

On client 3473, 17 payloads end with a one-byte list (`9` or `10`), the others with an empty one; client 1784 has no list. The value does not follow `skill_type` alone (type 1 skills hold both an empty list and `9`), so what it selects is open.
