# `servant.bss` Format

## Purpose

Base data of the servants (horses, donkeys, camels, elephants, wagons,
boats, ships, the camping tent): one record per servant character with its
Korean dev name, servant kind, tier, grade, coat colors, breeding count,
lifespan, price, the vehicle skills it starts with or can keep, and the
mix and breeding flags. On client 3474 the file has 419 records. The level
stats live in [servantexperience.dbss](servantexperience_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records        | Row bytes                 |
| ------ | -------------- | ------- | -------------------- | ------ | -------------- | ------------------------- |
| 2      | 2794 and later | 3483    | `servant.bss`        | 45,128 | 419 Row        | 84 to 165, 108 on average |
| 1      | 1421 to 2783   | 2783    | `servant.dbss`       | 40,590 | 384 Row        | 84 to 165, 106 on average |
| 1      | 1421 to 2783   | 2783    | `servantoffset.dbss` | 3,844  | 384 Offset Row | 10                        |

| Layout | File                 | Known            | Unknown        |
| ------ | -------------------- | ---------------- | -------------- |
| 2      | `servant.bss`        | 42,195 B (93.5%) | 2,933 B (6.5%) |
| 1      | `servant.dbss`       | 37,902 B (93.4%) | 2,688 B (6.6%) |
| 1      | `servantoffset.dbss` | 3,844 B (100.0%) | 0 B (0.0%)     |

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

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `vehicleskill.dbss`          | Optional | Korean skill names for `basic_learn_skill_keys` and `stallion_skill_keys` when LOC has none |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) and skill names (LOC type 8, `str_id1` = skill key) |

Client 1784 ships the same records as `servant.dbss` with the index
`servantoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 419 on client 3474                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### Row (variable: 80 bytes + name text and skill lists)

| Offset                        | Type                           | Field                             | Notes |
| ----------------------------- | ------------------------------ | --------------------------------- | ----- |
| `+0x00`                       | u16                            | character_id                      | Servant character, as in `characterstatic.dbss`; records sort by it, highest first |
| `+0x02`                       | u16                            | character_id_dup                  | Equals `character_id` on every record |
| `+0x04`                       | str16                          | name_kr                           | Korean dev name (`탑승용 수말29`); the game name is LOC type 6 |
| `name_kr+0x00`                | u8                             | servant_kind                      | `ServantKind`: 0 horse on 332 records (client 3474); the groups are in [itemenchant.dbss](itemenchant_dbss.md#equip_slot) |
| `name_kr+0x01`                | u8                             | servant_kind_sub                  | 0 to 10; non-zero on the dream horses and other kinds' variants |
| `name_kr+0x02`                | u16                            | tier                              | 0 to 9 |
| `name_kr+0x04`                | u16                            | grade                             | |
| `name_kr+0x06`                | u16                            | color1                            | |
| `name_kr+0x08`                | u16                            | color2                            | |
| `name_kr+0x0A`                | u16                            | color3                            | |
| `name_kr+0x0C`                | u8                             | mating_count                      | Breeding count; 0 on everything that cannot breed |
| `name_kr+0x0D`                | u32                            | lifespan                          | Seconds; 0 except 9057, an event Horse (259,200, 3 days) and 31125 Doomcaller (1,209,600, 14 days) on client 3474 |
| `name_kr+0x11`                | i64                            | base_price                        | Silver |
| `name_kr+0x19`                | i64                            | price_per_level                   | Silver |
| `name_kr+0x21`                | u8                             | is_male                           | |
| `name_kr+0x22`                | u8                             | is_display_gender                 | 0 on 22 records (client 3474), among them the dream horses, the dragons and the Twins |
| `name_kr+0x23`                | u8                             | servant_main_model                | 1 on one servant per kind (Notes) |
| `name_kr+0x24`                | u8                             | is_mating_result                  | |
| `name_kr+0x25`                | u8                             | is_trade                          | |
| `name_kr+0x26`                | u8                             | link_count                        | 0, 1, 2 or 4 |
| `name_kr+0x27`                | i32                            | experience_per_one                | 0, or 250,000 to 1,050,000 on 11 records (client 3474) |
| `name_kr+0x2B`                | u16                            | form_index                        | |
| `name_kr+0x2D`                | u8                             | basic_learn_skill_max_count       | |
| `name_kr+0x2E`                | u32                            | basic_learn_skill_count           | |
| `name_kr+0x32`                | u8[basic_learn_skill_count]    | basic_learn_skill_keys            | `vehicleskill.dbss` keys |
| `basic_learn_skill_keys+0x00` | bytes[5]                       | unknown_basic_learn_skill_keys_00 | `0` on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x05` | u32                            | reward_money_percent              | 500,000 on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x09` | u8                             | is_only_pcroom                    | 1 on 8 records (client 3474) |
| `basic_learn_skill_keys+0x0A` | u32                            | stallion_skill_count              | |
| `basic_learn_skill_keys+0x0E` | u8[stallion_skill_count]       | stallion_skill_keys               | `vehicleskill.dbss` keys: 3, 4, 8, 9, 10, 18 and 19 on client 3474 |
| `stallion_skill_keys+0x00`    | u8                             | can_mix                           | |
| `stallion_skill_keys+0x01`    | u8                             | can_mating                        | 1 exactly where `mating_count` is above 0 (Field Names) |
| `stallion_skill_keys+0x02`    | bytes[2]                       | unknown_stallion_skill_keys_02    | `0` on every record (clients 1784 and 3474) |

## Layout 1

Client 1784 names the file `servant.dbss`, with the same records, and adds
the index `servantoffset.dbss`.

### `servant.dbss`

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 333 on client 1784                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### `servantoffset.dbss`

| Offset  | Type              | Field   | Notes                       |
| ------- | ----------------- | ------- | --------------------------- |
| `+0x00` | u32               | count   | Equals the `servant.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 10 bytes |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                              |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2, from `character_id_dup` to the record end |

## Field Names

The names follow the `ServantSet_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against the
official client 1784 `servant.dbss` (333 records, every one in the sheet)
and client 3474 (329 of 419 records in the sheet):

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `RaceType` | `servant_kind` | 333 | 329 |
| `RaceSubType` | `servant_kind_sub` | 333 | 314 |
| `Tier`, `Grade` | `tier`, `grade` | 333 | 328, 329 |
| `Color1` to `Color3` | `color1` to `color3` | 333 | 329 |
| `MatingCount` | `mating_count` | 333 | 329 |
| `Lifespan` (minutes) | `lifespan` (seconds, x 60) | 333 | 329 |
| `basePrice`, `PricePerLevel` | `base_price`, `price_per_level` | 178 | 99, 101 |
| `IsMale`, `isDisplayGender` | `is_male`, `is_display_gender` | 333 | 329 |
| `ServantMainModel` | `servant_main_model` | 333 | 328 |
| `IsMatingResult`, `IsTrade` | `is_mating_result`, `is_trade` | 333 | 329 |
| `LinkCount`, `ExperiencePerOn` | `link_count`, `experience_per_one` | 333 | 329 |
| `FormIndex` | `form_index` | 333 | 329 |
| `basicLearnSkillMaxCount` | `basic_learn_skill_max_count` | 333 | 295 |
| `basicLearnSkillKey` (comma list) | `basic_learn_skill_keys` | 333 | 127 |
| `rewardMoneyPercent`, `isOnlyPcroom` | `reward_money_percent`, `is_only_pcroom` | 333 | 329 |
| `stallionSkillKey` (comma list) | `stallion_skill_keys` | 333 | 329 |
| `CanMix` | `can_mix` | 333 | 329 |

The prices are the private server's own; every other column matches all of
client 1784. The client 3474 misses are later changes: 15 dream horses
(Arduanatt, Diné, Doom and their dream and GT versions) have a
`servant_kind_sub` of 1 to 7 where the sheet has 0, Epheria Carrack:
Advance (31054) is a main model and Panokseon (31025) tier 3, and 183 of
the 202 `basic_learn_skill_keys` misses are the sheet's list plus vehicle
skill 4 (Sprint).

The sheet has no column for `can_mating`. The 2016 `gc::ServantStaticStatus`
ends with `_canMix` and `_canMating`, and the byte after `can_mix` is 1
exactly where `mating_count` is above 0 (419 of 419 records, client 3474).
The same struct holds `_servantKind`, `_servantExpirationPeriod` (the
`lifespan` slot) and `_experiencePerOne`, in the file's order. The client Lua
calls `getServantKind`, `getServantKindSub`, `getTier`, `getGrade`,
`isMale`, `isDisplayGender`, `getMatingCount`, `getLinkCount` and
`isPcroomOnly`.

## Notes

- `servant_main_model` is 1 on 8 records (client 3474), one per kind: 9909
  (Horse), 9010 (Brown Camel), 9113 (Donkey), 9052 (Merchant Wagon), 9032
  (Rowboat), 9065 (Fishing Boat), 31001 (Epheria Sailboat) and 31054
  (Epheria Carrack: Advance).
- The skill lists index [vehicleskill.dbss](vehicleskill_dbss.md) by its
  u8 key (1 to 106 on client 3474): stallion skill 3 is `드리프트` (Drift), 4
  `전력질주` (Sprint), 8 `순간가속` (Instant Acceleration), 9 `돌진` (Charge).
- In game on client 3474, a Mythical horse with Base Coat "Breed 13" (only
  31619 fits, see [bdoservanttitless.bss](bdoservanttitless_bss.md)) shows
  Skill List (27), all locked at 100%: its 27 `basic_learn_skill_keys`.
- No field holds HP, stamina, weight or a movement stat, so the 500 HP and 1
  stamina that two horses start above their `servantexperience.dbss` level 1
  row (its Open Questions) do not come from this file.

## Open Questions

### The Zero Fields

`unknown_basic_learn_skill_keys_00` (5 bytes) and
`unknown_stallion_skill_keys_02` (2 bytes) are `0` on every record of
clients 1784 and 3474. In column order the first sits where the sheet has
`specialLearnSkillMaxCount` and `specialLearnSkillKey`, but the sheet holds
`1` in `specialLearnSkillMaxCount` on every row, so the bytes do not follow
it. A u8 plus a u32 count of an empty list would fit the 5 bytes as well.
