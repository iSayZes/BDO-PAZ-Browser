# `edaniaetcoptionstaticstatus.bss` Format

## Purpose

The Edania (Throne of Edana) options: one row per castle, in
`__eEdaniaRegion` order, with its contents group, the minimum AP, DP and
item grade to enter its battles, its entry scroll tax rate and base
amount, the weekly throne quest, a world position near the castle, the
boss clear item and a list of 16 Dawn crystals; then seven settings stored
once, three of them Edana's drop buff. The Lua reads it with `ToClient_GetEdaniaEtcOption()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 3412 and later | 3483    | `edaniaetcoptionstaticstatus.bss` | 1,388 | 10 Row  | 135       |
| 1      | 3002 to 3356   | 3356    | `edaniaetcoptionstaticstatus.bss` | 373   | 5 Row   | 67        |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 2      | `edaniaetcoptionstaticstatus.bss` | 448 B (32.3%) | 940 B (67.7%) |
| 1      | `edaniaetcoptionstaticstatus.bss` | 238 B (63.8%) | 135 B (36.2%) |

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
| 3402   | No documented layout |
| 3396   | No documented layout |
| 3387   | No documented layout |
| 3381   | No documented layout |
| 3373   | No documented layout |
| 3364   | No documented layout |
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
| 2995   | No file              |
| 2987   | No file              |
| 2978   | No file              |
| 2970   | No file              |
| 2959   | No file              |
| 2951   | No file              |
| 2942   | No file              |
| 2935   | No file              |
| 2932   | No file              |
| 2923   | No file              |
| 2919   | No file              |
| 2907   | No file              |
| 2900   | No file              |
| 2891   | No file              |
| 2882   | No file              |
| 2872   | No file              |
| 2863   | No file              |
| 2855   | No file              |
| 2849   | No file              |
| 2844   | No file              |
| 2834   | No file              |
| 2825   | No file              |
| 2819   | No file              |
| 2811   | No file              |
| 2803   | No file              |
| 2794   | No file              |
| 2783   | No file              |
| 2774   | No file              |
| 2765   | No file              |
| 2756   | No file              |
| 2750   | No file              |
| 2743   | No file              |
| 2736   | No file              |
| 2726   | No file              |
| 2717   | No file              |
| 2709   | No file              |
| 2703   | No file              |
| 2695   | No file              |
| 2684   | No file              |
| 2672   | No file              |
| 2665   | No file              |
| 2657   | No file              |
| 2649   | No file              |
| 2644   | No file              |
| 2637   | No file              |
| 2629   | No file              |
| 2619   | No file              |
| 2612   | No file              |
| 2606   | No file              |
| 2602   | No file              |
| 2601   | No file              |
| 2592   | No file              |
| 2583   | No file              |
| 2575   | No file              |
| 2567   | No file              |
| 2560   | No file              |
| 2553   | No file              |
| 2545   | No file              |
| 2538   | No file              |
| 2529   | No file              |
| 2519   | No file              |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
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

| File                  | Required | Role                                                                                  |
| --------------------- | -------- | ------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Castle names (LOC type 37), quest titles (LOC type 18) and item names (LOC type 0)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset      | Type         | Field           | Notes                                                                  |
| ----------- | ------------ | --------------- | ---------------------------------------------------------------------- |
| `+0x00`     | char[4]      | magic           | ASCII `PABR`                                                           |
| `+0x04`     | Row[10]      | rows            | One per `__eEdaniaRegion` castle, Aetherion to Voidekaia; no row count |
| `rows+0x00` | u8           | unknown_rows_00 | `7`; see Open Questions                                                |
| `rows+0x01` | u8           | unknown_rows_01 | `3`                                                                    |
| `rows+0x02` | u32          | unknown_rows_02 | `5`                                                                    |
| `rows+0x06` | u32          | drop_buff_count | Edana's drop buff uses per term; `10`                                  |
| `rows+0x0A` | u32          | drop_buff_rate  | Its Item Drop Rate bonus, 1,000,000 = 100%; `1000000`                  |
| `rows+0x0E` | u32          | drop_buff_minutes | Its duration in minutes; `60`                                        |
| `rows+0x12` | u32          | unknown_rows_12 | `0`                                                                    |
| `rows+0x16` | String Table | string_table    | See String Table                                                       |
| `EOF-0x08`  | u32          | table_start     | Offset of the string table, where `unknown_rows_12` ends               |
| `EOF-0x04`  | u32          | zero            | Always `0`                                                             |

The parser reads rows up to 22 bytes before `table_start`, where the
settings start, and numbers them from `0` as their `__eEdaniaRegion`
value.

### Row (variable: 71 bytes + item IDs)

| Offset  | Type                     | Field               | Notes                                                                                     |
| ------- | ------------------------ | ------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32                      | contents_group_hash | Contents group key as the client's string hash; `2177` Aetherion to `2245` Voidekaia      |
| `+0x04` | f32                      | min_ap_1            | Minimum AP to enter; `350` (Aetherion) to `428` (Voidekaia); see Open Questions           |
| `+0x08` | f32                      | min_dp_1            | Minimum DP to enter; `427` to `520`                                                       |
| `+0x0C` | f32                      | min_ap_2            | Equals `min_ap_1` on every row                                                            |
| `+0x10` | f32                      | min_dp_2            | Equals `min_dp_1` on every row                                                            |
| `+0x14` | u8                       | min_item_grade_1    | Minimum item grade of the worn gear; `4` (orange, "Red grade") on every row               |
| `+0x15` | u32                      | unknown_15          | `13` on every row                                                                         |
| `+0x19` | u8                       | min_item_grade_2    | Equals `min_item_grade_1` on every row                                                    |
| `+0x1A` | u32                      | unknown_1a          | `13` on every row                                                                         |
| `+0x1E` | u32                      | tax_rate            | Share of the entry scroll price that accrues as tax, 1,000,000 = 100%; `2000` to `5000`  |
| `+0x22` | u8                       | unknown_22          | The castle's `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` number minus one; see Notes              |
| `+0x23` | bytes[3]                 | unknown_23          | `71 0B 00` on every row                                                                   |
| `+0x26` | u32                      | throne_quest        | Packed quest ID (`quest_id << 16 \| quest_chain_id`): `9108/1` to `9108/5`, `9308/1` to `9308/5` |
| `+0x2A` | f32                      | unknown_2a          | With the next two a world position near the castle; see Notes                             |
| `+0x2E` | f32                      | unknown_2e          |                                                                                           |
| `+0x32` | f32                      | unknown_32          |                                                                                           |
| `+0x36` | u64                      | tax_base_amount     | Silver the tax starts from; `3,000,000,000` to `25,000,000,000`, rising with the row      |
| `+0x3E` | u32                      | boss_clear_item_key | Item ID, an "Edania: ... Chest"; `890056` (Azureach Chest) on row `0`                     |
| `+0x42` | u8                       | unknown_42          | `0` on every row                                                                          |
| `+0x43` | u32                      | unknown_item_count  | Number of `unknown_item_ids`; `16` on every row                                           |
| `+0x47` | u32[unknown_item_count]  | unknown_item_ids    | Item IDs, the same 16 Dawn crystals on every row; see Open Questions                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### File Layout

| Offset     | Type         | Field           | Notes                                                    |
| ---------- | ------------ | --------------- | -------------------------------------------------------- |
| `+0x00`    | char[4]      | magic           | ASCII `PABR`                                             |
| `+0x04`    | Row[5]       | rows            | Aetherion to Zephyros, the first Edana group             |
| `+0x153`   | u8           | unknown_rows_00 |                                                          |
| `+0x154`   | u8           | unknown_rows_01 |                                                          |
| `+0x155`   | u32          | unknown_rows_02 |                                                          |
| `+0x159`   | u32          | drop_buff_count |                                                          |
| `+0x15D`   | u32          | drop_buff_rate  |                                                          |
| `+0x161`   | u32          | drop_buff_minutes |                                                          |
| `+0x165`   | u32          | unknown_rows_12 |                                                          |
| `+0x169`   | String Table | string_table    | See String Table                                         |
| `EOF-0x08` | u32          | table_start     | Offset of the string table, where `unknown_rows_12` ends |
| `EOF-0x04` | u32          | zero            | Always `0`                                               |

### Row (67 bytes)

| Offset  | Type     | Field               | Notes                                  |
| ------- | -------- | ------------------- | -------------------------------------- |
| `+0x00` | u32      | contents_group_hash |                                        |
| `+0x04` | f32      | min_ap_1            |                                        |
| `+0x08` | f32      | min_dp_1            |                                        |
| `+0x0C` | f32      | min_ap_2            |                                        |
| `+0x10` | f32      | min_dp_2            |                                        |
| `+0x14` | u8       | min_item_grade_1    |                                        |
| `+0x15` | u32      | unknown_15          |                                        |
| `+0x19` | u8       | min_item_grade_2    |                                        |
| `+0x1A` | u32      | unknown_1a          |                                        |
| `+0x1E` | u32      | tax_rate            |                                        |
| `+0x22` | u8       | unknown_22          |                                        |
| `+0x23` | bytes[3] | unknown_23          |                                        |
| `+0x26` | u32      | throne_quest        |                                        |
| `+0x2A` | f32      | unknown_2a          |                                        |
| `+0x2E` | f32      | unknown_2e          |                                        |
| `+0x32` | f32      | unknown_32          |                                        |
| `+0x36` | u64      | tax_base_amount     |                                        |
| `+0x3E` | u32      | boss_clear_item_key | A different item ID per row (`761697` on row `0`) |
| `+0x42` | u8       | unknown_42          |                                        |

## Castles

The rows on client 3482.

| Row | Contents group | `throne_quest` | Quest title                          | `boss_clear_item_key` | Item                        |
| --- | -------------- | -------------- | ------------------------------------ | --------------------- | --------------------------- |
| 0   | `2177`         | `9108/1`       | [Weekly] For the Throne: Aetherion   | `890056`              | Edania: Azureach Chest      |
| 1   | `2178`         | `9108/2`       | [Weekly] For the Throne: Nymphamaré  | `890057`              | Edania: Emeraltides Chest   |
| 2   | `2176`         | `9108/3`       | [Weekly] For the Throne: Orbita      | `890058`              | Edania: Amberwilds Chest    |
| 3   | `2179`         | `9108/4`       | [Weekly] For the Throne: Tenebraum   | `890059`              | Edania: Ebonshade Chest     |
| 4   | `2175`         | `9108/5`       | [Weekly] For the Throne: Zephyros    | `890060`              | Edania: Crimsonroot Chest   |
| 5   | `2216`         | `9308/1`       | [Weekly] For the Throne: Aphrodon    | `790866`              | Edania: Goldroot Chest      |
| 6   | `2218`         | `9308/2`       | [Weekly] For the Throne: Hermesia    | `890102`              | Edania: Ebonmere Chest      |
| 7   | `2219`         | `9308/3`       | [Weekly] For the Throne: Magaia      | `890103`              | Edania: Everlight Chest     |
| 8   | `2220`         | `9308/4`       | [Weekly] For the Throne: Aresion     | `890104`              | Edania: Crimsonflare Chest  |
| 9   | `2245`         | `9308/5`       | [Weekly] For the Throne: Voidekaia   | `890105`              | Edania: Voidreach Chest     |

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. The Edania window
(`panel_window_edania_contents_all_1.luac` and `_2.luac`, client 3482)
loops `regionIndex` from `0` to `__eEdaniaRegion_Count - 1` and reads, per
castle, `getLimitStat(regionIndex, isBossRoom, isOffence)`,
`checkContentsOption(regionIndex)`, `getEdanaBossClearItemKey(regionIndex)`
and `getEdanaPersonalFieldTaxPercent(regionIndex)`, and once
`getEdanaDropBuffTime()`, `getEdanaDropBuffPercent()` and
`getEdanaDropBuffCount()`. The file has one row per castle and one block
of settings, which fits that split.

| Field                 | Source                                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `contents_group_hash` | Each value is the client's string hash of a contents group key (`_common/contents_group.py`), `2175` to `2245`; a per-castle switch is what `checkContentsOption` tests |
| `throne_quest`        | Each value is a packed quest ID whose LOC type 18 title names the castle of its row                            |
| `boss_clear_item_key` | The only per-row item ID besides the shared crystal list; each is an "Edania: ... Chest", one per castle, which `getEdanaBossClearItemKey` returns for the boss clear slot |

The official Throne of Edana page of the NA/EU game wiki (wikiNo 457)
lists the entry conditions and the tax of Aetherion, Nymphamaré and
Orbita Castle, and Edana's drop buff. Its values match the file:

| Field | Official wiki page | File (client 3482) |
| ----- | ------------------ | ------------------ |
| `min_ap_1`, `min_dp_1` | "AP 350+ / DP 427+", "AP 375+ / DP 440+", "AP 385+ / DP 445+" | `350, 427`, `375, 440` and `385, 445` on rows `0` to `2` |
| `min_item_grade_1` | At least "Red grade" gear equipped, at every castle | `4` on every row, the grade the client draws orange-red (`_common/item_grade.py`) |
| `tax_rate` | Tax Rate 0.4%, 0.3% and 0.25% | `4000`, `3000` and `2500` on the 1,000,000 = 100% scale |
| `tax_base_amount` | Base amount 3, 5 and 8 billion Silver | `3000000000`, `5000000000` and `8000000000` |
| `drop_buff_rate`, `drop_buff_minutes`, `drop_buff_count` | Edana's Blessing: Item Drop Rate +100% for up to 1 hour, up to 10 times per week | `1000000` (100%), `60` and `10` |

The page gives one AP, DP and grade condition per castle for both the
10-challenger battle and the final challenger vs. Edana battle; the file
stores two copies, which fits `getLimitStat(regionIndex, isBossRoom,
isOffence)` and the two `ToClient_Check...RoomItemGradeType` calls. The
window compares the offence value with `ToClient_getAttackDisplayOffenceMax()`
(AP) and the defence value with `ToClient_getAttackDisplayDefence()` (DP).

## Notes

- Clients 3002 and 3251 use Layout 1: five rows (the first Edana group)
  of 67 bytes, with no crystal list. Client 3474 adds the second group and
  the list and matches client 3482 byte for byte. The settings block is
  the same on all four clients. The file is not in the archives of client
  1784.
- `unknown_22` runs `0, 1, 3, 2, 4, 5, ...`: the castle number of the
  `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` key of the row's castle minus one,
  where Orbita and Tenebraum swap numbers 3 and 4
  ([`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#enum-values)). The row
  order follows `__eEdaniaRegion`: the quest titles and the positions put
  Orbita on row `2` and Tenebraum on row `3`.
- `unknown_2a`, `unknown_2e` and `unknown_32` read as a world position
  (`y` the height). On client 3482 its X and Z lie within 400 units of the
  castle's map mark in
  [`edanacastleinfostaicstatusmanager.bss`](edanacastleinfostaicstatusmanager_bss.md)
  on 7 of 10 rows (`559137, 573784` against `559141, 573692` for
  Aetherion), 4,253 and 6,995 units away for Tenebraum and Zephyros and
  16,152 for Orbita. The Lua names a castle teleport
  (`HandleEventLUp_Edania_Contents_TeleportToMyCastle`,
  `__ePreCoolTimeType_EdanaCastleTeleport`) but no getter for it.
- `unknown_item_ids` lists the HAN, JIN, BON and WON grades of four Dawn
  crystals (`15264` to `15275` and `15282` to `15285`): "Black Spirit's
  Rage", "Accuracy", "Damage Reduction" and "Evasion" (LOC type 0, "JIN
  Dawn Crystal - Accuracy").
- The handler shows one row per castle: the castle name, the contents
  group key, the AP, DP and grade minimums, the tax rate and base amount,
  the quest title and the boss clear item, with the drop buff in the count
  line; the other fields stay on the record.

## Open Questions

### Which Copy Is Which Room

`min_ap_1`, `min_dp_1` and `min_item_grade_1` equal `min_ap_2`,
`min_dp_2` and `min_item_grade_2` on every row, so which copy is the boss
(Edana) room and which the challenger room of `getLimitStat(regionIndex,
isBossRoom, isOffence)` cannot be told from the values.

### The Other Settings

`unknown_rows_00` (`7`), `unknown_rows_01` (`3`), `unknown_rows_02` (`5`)
and `unknown_rows_12` (`0`) are stored once next to the drop buff. No
number on the official wiki page matches them.

### The Other Row Fields

What `unknown_15` and `unknown_1a` (`13` after each grade), `unknown_23`
(`71 0B 00`) and the crystal list are for. The entry scroll prices on the
official wiki page (50, 70 and 80 million Silver) are not in the row.
