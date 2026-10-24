# `vehicleskillowner.dbss` Format

## Purpose

Which [vehicleskill.dbss](vehicleskill_dbss.md) skills each servant can
learn: one record per servant character with a list of skill keys, each
with a learn value, an EXP value and a learn flag. On client 3474 the file
has 366 records, every one a `servant.bss` character, with 0 to 37 skills
each (5,620 in all).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ----------------------- | --------- |
| 2      | 2474 and later | 3483    | `vehicleskillowner.dbss`       | 94,316 | 5,620 Skill, 366 Record | 16        |
| 2      | 2474 and later | 3483    | `vehicleskillowneroffset.dbss` | 3,680  | 366 Offset Row          | 10        |
| 1      | 1346 to 2468   | 2468    | `vehicleskillowner.dbss`       | 62,907 | 4,643 Skill, 318 Record | 13        |
| 1      | 1346 to 2468   | 2468    | `vehicleskillowneroffset.dbss` | 3,200  | 318 Offset Row          | 10        |

| Layout | File                           | Known            | Unknown          |
| ------ | ------------------------------ | ---------------- | ---------------- |
| 2      | `vehicleskillowner.dbss`       | 77,456 B (82.1%) | 16,860 B (17.9%) |
| 2      | `vehicleskillowneroffset.dbss` | 3,680 B (100.0%) | 0 B (0.0%)       |
| 1      | `vehicleskillowner.dbss`       | 48,978 B (77.9%) | 13,929 B (22.1%) |
| 1      | `vehicleskillowneroffset.dbss` | 3,200 B (100.0%) | 0 B (0.0%)       |

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

| File                           | Required | Role                                                    |
| ------------------------------ | -------- | ------------------------------------------------------- |
| `vehicleskillowneroffset.dbss` | Optional | PABR index: character ID to the record's offset and size |
| `vehicleskill.dbss`            | Optional | The skills `skill_key` points at; their Korean names when LOC has none |
| `characterstaticoffset.dbss`   | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`          | Optional | Servant names (LOC type 6) and skill names (LOC type 8) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 366 on client 3474                     |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 12 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | Servant character, as in `servant.bss` |
| `+0x02` | u16                 | character_id_dup | Equals `character_id` on every record |
| `+0x04` | u32                 | cant_learnable_rate | Weight of "Does not learn" ([Learn Chance](#learn-chance)); 0 on 218 records, up to 1,000,000 on 148 (client 3474) |
| `+0x08` | u32                 | skill_count      | 0 to 37 on client 3474 |
| `+0x0C` | Skill[skill_count]  | skills           | In `skill_key` order |

### Skill (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | skill_key  | `vehicleskill.dbss` key, 1 to 106 on client 3474 |
| `+0x04` | u32  | able       | 1,000,000 on 996 of 5,620 entries (client 3474) |
| `+0x08` | u32  | add_exp    | |
| `+0x0C` | u8   | is_learn   | 0 on 153 entries (client 3474) |
| `+0x0D` | u8   | unknown_0d | 2 on every entry (client 3474) |
| `+0x0E` | u16  | unknown_0e | `0` on every entry (clients 1784 and 3474) |

### `vehicleskillowneroffset.dbss`

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | count              | Equals the main file's `count`     |
| `+0x08`             | Offset Row[count] | entries            | Not in file order                  |
| `entries+0x00`      | String Table      | string_table       | Present but empty                  |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                                 |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1784 has no `cant_learnable_rate` and stores `skill_key` as a u8; it has 288
records and 4,134 skills, keys 1 to 76.

### Record (variable: 8 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | |
| `+0x02` | u16                 | character_id_dup | |
| `+0x04` | u32                 | skill_count      | 0 to 27 |
| `+0x08` | Skill[skill_count]  | skills           | In `skill_key` order on 286 of 288 records |

### Skill (13 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u8   | skill_key  | |
| `+0x01` | u32  | able       | |
| `+0x05` | u32  | add_exp    | |
| `+0x09` | u8   | is_learn   | |
| `+0x0A` | u8   | unknown_0d | `0` on every entry |
| `+0x0B` | u16  | unknown_0e | `0` on every entry |

## Learn Chance

The horse growth window (Horse Growth Info, My Horse Info tab) lists a
chance per skill and a "Does not learn" row. The client Lua
(`panel_dialog_servantsimulator_5`) fills that row from
`ToClient_GetHorseSimulateDetailInformationCantLearnableRate()`. With the
window's Total Gain Chance `g`:

```text
chance(skill)   = able × (1 + g) / (cant_learnable_rate + sum of able of the skills not learned yet)
chance(nothing) = 100% - sum of chance(skill)
```

Learned and inherent skills drop out of the sum. On 103 of the 148 records
with a non-zero `cant_learnable_rate` (client 3474), it plus the `able` of
every entry below 1,000,000 is exactly 1,000,000; the formula does not need
that, and holds on a record where the total is 1,061,581 too (9890 below).

Checked on 2026-10-20 (client 3474) with Training Artisan 7, on two tier 6
stallions of the 9915 group (9915, 9952, 9953, 9973, 9978:
`cant_learnable_rate` 536,040, Hind Kick 75,000) at Total Gain Chance
21.7%, and on the tier 8 mare 9890 (`cant_learnable_rate` 379,906, Caution
37,000, Two-seater 9,000) at 31.7%:

| Horse | Learned | Sum | Chance | Does not learn |
| ----- | ------- | --- | ------ | -------------- |
| 9953 (Breed 11), level 8 | Fore Chop, Sprint (inherent) | 924,405 | Hind Kick 9.8739% (shown 9.8739%) | 48.8715% (shown 48.8715%) |
| 9915 (Breed 2), level 4 | Sprint (inherent), Start Accel, Streak Leap | 906,912 | Hind Kick 10.0644% (shown 10.0644%) | 50.2327% (shown 50.2327%) |
| 9890 (Breed 13), level 30 | 18 of 20, S: Instant Accel and Sprint inherent | 425,906 | Caution 11.4413%, Two-seater 2.7830% (shown 11.4413%, 2.783%) | 85.7757% (shown 85.7757%) |

The window's Base Coat line (`bdoservanttitless.bss`) names the breed,
which picks one character of the group. The level 4 horse's window lists
three learned skills; only Streak Leap
(38,064) as the third one gives its shown chances, and Drift, Fore Chop,
High Jump, Quick Stop and Instant Accel then match to the last digit too.

## Field Names

The names follow the `VehicleSkillOwner_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784: one row per `CharacterKey` with
`Able_N`, `AddExp_N` and `IsLearn_N` for skill keys 1 to 76. On client 1784
(288 records, every one in the sheet) the entries match by value:

| Column | Field | Equal (client 1784, 4,134 entries) | Equal (client 3474, 3,899 entries of 279 shared records) |
| ------ | ----- | ---------------------------------- | -------------------------------------------------------- |
| `Able_N` | `able` of the entry with `skill_key` N | 4,112 | 2,529 |
| `AddExp_N` | `add_exp` | 4,134 | 3,197 |
| `IsLearn_N` | `is_learn` | 4,134 | 3,899 |

The 22 client 1784 `able` misses are sheet values with a fraction stored
truncated (`4666.666667` as 4,666). Every record lists each skill whose
`Able_N` is not 0; 23 records also list skills whose `Able_N` is 0. The
client 3474 misses come from changed values: `able` 1,000,000 and `add_exp`
0 where client 1784 has 200,000 and 2,500 (camel 9081, Fore Chop 20 and
Hind Kick 21), and the client Lua gates the
skill-rate display of the breeding simulator behind
`_ContentsGroup_VehicleLearnSkill_Renewal`.

## Open Questions

### Records With No Does-Not-Learn Weight

`cant_learnable_rate` is new on client 3474: 0 on all tier 1 to 5 horses
and on 218 records in all, non-zero on 148, mostly tier 6 to 9 horses. 51
of the 218 start with every skill they list (31619, checked in game, shows
Skill List (27) with all 27 at 100%), but the other 167, among them every
tier 1 to 5 horse, still have skills to learn. With a weight of 0 the
formula gives "Does not learn" 0% and the skills more than 100% in sum, so
the window either shows those horses another way or uses another formula
for them.

### The Constant Byte

`unknown_0d` is 2 on every client 3474 entry and 0 on client 1784.
