# `hardcorechanneletcoptionstaticstatus.bss` Format

## Purpose

The settings of the Hardcore channel: 83 bytes of unnamed numbers, a
counted list of two (u8, f32, u16) entries, an f32 and the class types that
can create a Hardcore character. On client 3474 that class list holds 29
class types, every playable class but Wukong, Seraph and Agent. The class
types are those of [`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md),
which holds a stat row per class type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------ | ----- | ------- | --------- |
| 1      | 2834 and later | 3483    | `hardcorechanneletcoptionstaticstatus.bss` | 154   | 2 Entry | 7         |

| Layout | File                                       | Known        | Unknown       |
| ------ | ------------------------------------------ | ------------ | ------------- |
| 1      | `hardcorechanneletcoptionstaticstatus.bss` | 49 B (31.8%) | 105 B (68.2%) |

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
| 2825   | No file  |
| 2819   | No file  |
| 2811   | No file  |
| 2803   | No file  |
| 2794   | No file  |
| 2783   | No file  |
| 2774   | No file  |
| 2765   | No file  |
| 2756   | No file  |
| 2750   | No file  |
| 2743   | No file  |
| 2736   | No file  |
| 2726   | No file  |
| 2717   | No file  |
| 2709   | No file  |
| 2703   | No file  |
| 2695   | No file  |
| 2684   | No file  |
| 2672   | No file  |
| 2665   | No file  |
| 2657   | No file  |
| 2649   | No file  |
| 2644   | No file  |
| 2637   | No file  |
| 2629   | No file  |
| 2619   | No file  |
| 2612   | No file  |
| 2606   | No file  |
| 2602   | No file  |
| 2601   | No file  |
| 2592   | No file  |
| 2583   | No file  |
| 2575   | No file  |
| 2567   | No file  |
| 2560   | No file  |
| 2553   | No file  |
| 2545   | No file  |
| 2538   | No file  |
| 2529   | No file  |
| 2519   | No file  |
| 2513   | No file  |
| 2510   | No file  |
| 2507   | No file  |
| 2503   | No file  |
| 2498   | No file  |
| 2492   | No file  |
| 2487   | No file  |
| 2480   | No file  |
| 2474   | No file  |
| 2468   | No file  |
| 2460   | No file  |
| 2453   | No file  |
| 2444   | No file  |
| 2438   | No file  |
| 2434   | No file  |
| 2429   | No file  |
| 2421   | No file  |
| 2414   | No file  |
| 2407   | No file  |
| 2401   | No file  |
| 2397   | No file  |
| 2393   | No file  |
| 2384   | No file  |
| 2378   | No file  |
| 2372   | No file  |
| 2358   | No file  |
| 2352   | No file  |
| 2347   | No file  |
| 2343   | No file  |
| 2335   | No file  |
| 2327   | No file  |
| 2324   | No file  |
| 2319   | No file  |
| 2313   | No file  |
| 2308   | No file  |
| 2302   | No file  |
| 2295   | No file  |
| 2290   | No file  |
| 2284   | No file  |
| 2276   | No file  |
| 2269   | No file  |
| 2259   | No file  |
| 2250   | No file  |
| 2243   | No file  |
| 2235   | No file  |
| 2229   | No file  |
| 2224   | No file  |
| 2218   | No file  |
| 2215   | No file  |
| 2207   | No file  |
| 2203   | No file  |
| 2196   | No file  |
| 2192   | No file  |
| 2189   | No file  |
| 2183   | No file  |
| 2179   | No file  |
| 2171   | No file  |
| 2163   | No file  |
| 2156   | No file  |
| 2151   | No file  |
| 2147   | No file  |
| 2142   | No file  |
| 2138   | No file  |
| 2134   | No file  |
| 2130   | No file  |
| 2122   | No file  |
| 2107   | No file  |
| 2098   | No file  |
| 2089   | No file  |
| 2081   | No file  |
| 2073   | No file  |
| 2067   | No file  |
| 2063   | No file  |
| 2059   | No file  |
| 2052   | No file  |
| 2044   | No file  |
| 2039   | No file  |
| 2032   | No file  |
| 2025   | No file  |
| 2011   | No file  |
| 2005   | No file  |
| 2000   | No file  |
| 1996   | No file  |
| 1991   | No file  |
| 1985   | No file  |
| 1980   | No file  |
| 1969   | No file  |
| 1964   | No file  |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
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

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Class names, LOC type 21    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                         | Field                | Notes                                                              |
| ---------------------------- | ---------------------------- | -------------------- | ------------------------------------------------------------------ |
| `+0x00`                      | char[4]                      | magic                | ASCII `PABR`                                                       |
| `+0x04`                      | u32                          | unknown_04           | `60` on client 3474                                                |
| `+0x08`                      | u32                          | unknown_08           | `2` on client 3474                                                 |
| `+0x0C`                      | u16                          | unknown_0c           | `60` on client 3474                                                |
| `+0x0E`                      | u8                           | unknown_0e           | `1` on client 3474                                                 |
| `+0x0F`                      | u32                          | unknown_0f           | `60` on client 3474                                                |
| `+0x13`                      | u32                          | unknown_13           | `50` on client 3474                                                |
| `+0x17`                      | u32                          | unknown_17           | `100000` on client 3474                                            |
| `+0x1B`                      | u32                          | unknown_1b           | `300000` on client 3474                                            |
| `+0x1F`                      | u32                          | unknown_1f           | `10000` on client 3474                                             |
| `+0x23`                      | u32                          | unknown_23           | `3000` on client 3474                                              |
| `+0x27`                      | u32                          | unknown_27           | `200000` on client 3474                                            |
| `+0x2B`                      | u32                          | unknown_2b           | `300000` on client 3474                                            |
| `+0x2F`                      | u32                          | unknown_2f           | `3` on client 3474                                                 |
| `+0x33`                      | u32                          | unknown_33           | `500` on client 3474                                               |
| `+0x37`                      | u32                          | unknown_37           | `300` on client 3474                                               |
| `+0x3B`                      | i32                          | unknown_3b           | `-40` on client 3474                                               |
| `+0x3F`                      | u64                          | unknown_3f           | `100` on client 3474                                               |
| `+0x47`                      | u64                          | unknown_47           | `50` on client 3474                                                |
| `+0x4F`                      | u64                          | unknown_4f           | `20` on client 3474                                                |
| `+0x57`                      | u32                          | unknown_entry_count  | Number of `unknown_entries`; `2` on client 3474                     |
| `+0x5B`                      | Entry[unknown_entry_count]   | unknown_entries      | See Entry                                                          |
| `unknown_entries+0x00`       | f32                          | unknown_entries_00   | `74.0` on client 3474, the f32 of entry `1`                        |
| `unknown_entries+0x04`       | u32                          | class_count          | Number of `possible_class_types`                                   |
| `unknown_entries+0x08`       | u8[class_count]              | possible_class_types | Class types that can create a Hardcore character; see Classes      |
| `possible_class_types+0x00`  | String Table                 | string_table         | See String Table                                                   |
| `string_table+0x00`          | u32                          | table_start          | Offset of the string table, where `possible_class_types` ends      |
| `string_table+0x04`          | u32                          | zero                 | Always `0`                                                         |

### Entry (7 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u8   | unknown_00 | `1` and `2` on client 3474                               |
| `+0x01` | f32  | unknown_01 | `74.0` with `1`, `37.0` with `2` on client 3474          |
| `+0x05` | u16  | unknown_05 | `1` on both entries                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Classes

`possible_class_types` on client 3474, by LOC type 21 name: Warrior (0),
Hashashin (1), Sage (2), Ranger (4), Guardian (5), Scholar (6), Drakania
(7), Sorceress (8), Nova (9), Corsair (10), Lahn (11), Berserker (12),
Maegu (15), Tamer (16), Shai (17), Striker (19), Musa (20), Maehwa (21),
Mystic (23), Valkyrie (24), Kunoichi (25), Ninja (26), Dark Knight (27),
Wizard (28), Archer (29), Woosa (30), Witch (31), Dosa (33) and Deadeye
(34). Wukong (3), Seraph (32) and Agent (35) are missing, besides the
unused class types 13, 14, 18 and 22.

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. `possible_class_types` follows the client
Lua of client 3474: the class select windows
(`panel_lobby_classselect_renew.luac` and `panel_lobby_main.luac`) read
the classes a Hardcore character can take with
`ToClient_getHardCorePossbieClassCount()` and
`ToClient_getHardCorePossbieClassFromIndex(index)`, a count and a class
type per index, and every value of the list has a LOC type 21 class name.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The LOC type 37 server text that opened Hardcore characters to Warrior,
  Ranger, Sorceress and Berserker
  ([`hardcorecharacterstatstaticstatus.bss`](hardcorecharacterstatstaticstatus_bss.md)
  Notes) names fewer classes than this list, which holds the same 29 on
  clients 3002 to 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  the class list by name.

## Open Questions

### Unnamed Settings

Which value each Hardcore getter of the client 3474 Lua returns. The Lua
reads `ToClient_isHardCoreChannelEnterPossibleLevel()` (the level in
"LUA_HARDCORECHANNEL_CANTPLAY_NOTIFY"), `ToClient_getHardCoreMaxBossCount()`,
`ToClient_getHardCoreHighRankerMaxCount()`,
`ToClient_getHardCoreRepeatQuestCountMax()`,
`ToClient_getHardCoreExchangeCoinMaxCount()` and
`ToClient_GetHardCoreCharacterRespawnTime()`, and none of them is a plain
match: `60` appears three times, `2` fits the two bosses of
[`hardcorerandomspawncharacterstaticstatusmanager.bss`](hardcorerandomspawncharacterstaticstatusmanager_bss.md),
`3` the three top ranks, `500` and `300` a coin cap and a respawn time.

### Alert Entries

What `unknown_entries` and `unknown_entries_00` hold. The enemy alert
widget (`panel_widget_enemyalert_hardcore_1.luac`) reads
`ToClient_GetHardCoreNearPlayerAlertLevel()` and shows one effect for level
`1` and another for `2`. The entries are numbered `1` and `2`, the f32 of
`2` is half that of `1` (`37.0` and `74.0`), and `unknown_entries_00`
repeats `74.0`, which fits a distance per alert level, but no Lua reads the
values.
