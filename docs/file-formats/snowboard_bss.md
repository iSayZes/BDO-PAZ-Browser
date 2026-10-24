# `snowboard.bss` Format

## Purpose

The snowboard courses of Snowfall Crasher: Alpine Glide. After a head
of settings for the whole field, each course gives its key, Korean name,
mode and chain of checkpoints; two lists of effect settings follow. The
snowboard menu (`panel_window_snowboard_menu_all_1.luac`, client 3482)
makes one tab per course from `ToClient_SnowBoardCourseCount()` and
`ToClient_GetSnowBoardStaticStatusByIndex(ii)`, reading `getKeyRaw()`,
`getMode()` and `getName()`; the race HUD reads `getCheckPointCount()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ----------------------------------------- | --------- |
| 1      | 3151 and later | 3483    | `snowboard.bss` | 3,293 | 45 Checkpoint, 3 Course, 2 Item, 7 Effect | 50        |

| Layout | File            | Known         | Unknown         |
| ------ | --------------- | ------------- | --------------- |
| 1      | `snowboard.bss` | 961 B (29.2%) | 2,332 B (70.8%) |

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
| 3186   | No file  |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | No file  |
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
| 2995   | No file  |
| 2987   | No file  |
| 2978   | No file  |
| 2970   | No file  |
| 2959   | No file  |
| 2951   | No file  |
| 2942   | No file  |
| 2935   | No file  |
| 2932   | No file  |
| 2923   | No file  |
| 2919   | No file  |
| 2907   | No file  |
| 2900   | No file  |
| 2891   | No file  |
| 2882   | No file  |
| 2872   | No file  |
| 2863   | No file  |
| 2855   | No file  |
| 2849   | No file  |
| 2844   | No file  |
| 2834   | No file  |
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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field            | Notes                                                       |
| ------------------- | -------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]              | magic            | ASCII `PABR`                                                |
| `+0x04`             | u16                  | unknown_04       | `1` (client 3482)                                           |
| `+0x06`             | u32                  | unknown_06       | `200` (client 3482)                                         |
| `+0x0A`             | u32                  | unknown_0a       | `10` (client 3482)                                          |
| `+0x0E`             | u32                  | unknown_item_key | Item ID: `1000383` [Event] Snowfall Crasher Seal (client 3482) |
| `+0x12`             | f32[3]               | unknown_12       | `180.0` three times (client 3482)                           |
| `+0x1E`             | u32                  | effect_ref       | String table index of an effect name; see Field Names       |
| `+0x22`             | u16                  | region_key       | `regioninfo.bss` region: `1176` Snowfall Crasher: Alpine Glide |
| `+0x24`             | f32[3]               | unknown_24       | A world position x, y, z in that region                     |
| `+0x30`             | bytes[8]             | unknown_30       | `D2 C4 AA 94 64 25 00 00` (client 3482)                     |
| `+0x38`             | u32                  | unknown_38       | `60` (client 3482)                                          |
| `+0x3C`             | u32                  | course_count     | Number of courses, `ToClient_SnowBoardCourseCount()`        |
| `+0x40`             | Course[course_count] | courses          | See Course; menu tab `ii` is course `ii`                    |
| `courses+0x00`      | u32                  | item_count       | Number of item effect entries                               |
| `courses+0x04`      | Item[item_count]     | items            | See Item                                                    |
| `items+0x00`        | u32                  | effect_count     | Number of checkpoint effect entries                         |
| `items+0x04`        | Effect[effect_count] | effects          | See Effect                                                  |
| `effects+0x00`      | String Table         | string_table     | See String Table                                            |
| `string_table+0x00` | u32                  | table_start      | Offset of the string table, where `effects` ends            |
| `string_table+0x04` | u32                  | zero             | Always `0`                                                  |

### Course (variable: 41 bytes + checkpoints)

| Offset  | Type                         | Field            | Notes                                                       |
| ------- | ---------------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u32                          | course_key       | `getKeyRaw()`; `1` up in course order                       |
| `+0x04` | u32                          | name_ref         | String table index of the Korean course name, `getName()`   |
| `+0x08` | u8                           | mode             | `getMode()`: `0` Item, `1` Speed; see Course Modes          |
| `+0x09` | f32[3]                       | unknown_09       | A world position x, y, z; the same on every course (client 3482) |
| `+0x15` | f32                          | unknown_15       | `0.36` on every course (client 3482)                        |
| `+0x19` | f32                          | unknown_19       | `100.0` on every course (client 3482)                       |
| `+0x1D` | u32                          | unknown_1d       | `60` on the Item course, `0` on the others (client 3482)    |
| `+0x21` | u32                          | unknown_21       | `0`, `15000` and `5000` on courses `1` to `3` (client 3482) |
| `+0x25` | u32                          | checkpoint_count | Number of checkpoints, `getCheckPointCount()`               |
| `+0x29` | Checkpoint[checkpoint_count] | checkpoints      | See Checkpoint                                              |

### Checkpoint (50 bytes)

| Offset  | Type   | Field                 | Notes                                                                |
| ------- | ------ | --------------------- | -------------------------------------------------------------------- |
| `+0x00` | u32    | checkpoint_index      | `1` up in list order                                                 |
| `+0x04` | u32    | next_checkpoint_index | The checkpoint after this one; the last points back to `1`           |
| `+0x08` | f32[3] | unknown_08            | A world position x, y, z                                             |
| `+0x14` | f32    | unknown_14            | `-2.19` to `2.88` on client 3482, inside plus or minus pi            |
| `+0x18` | f32[6] | unknown_18            | Two sets of three; see Checkpoints                                   |
| `+0x30` | u8     | unknown_30            | `0` to `6`, below `effect_count`; see Checkpoints                    |
| `+0x31` | u8     | unknown_31            | `0` on the first checkpoint, `2` on the last, `1` between (client 3482) |

### Item (36 bytes)

| Offset  | Type   | Field             | Notes                                                    |
| ------- | ------ | ----------------- | -------------------------------------------------------- |
| `+0x00` | u32    | unknown_00        | `1` and `2` (client 3482)                                |
| `+0x04` | u32    | first_effect_ref  | String table index of an effect name                     |
| `+0x08` | u32    | second_effect_ref | String table index of an effect name                     |
| `+0x0C` | f32[3] | unknown_0c        | `0.0, 100.0, 0.0` on both entries (client 3482)          |
| `+0x18` | f32[3] | unknown_18        | `1.0` three times on both entries (client 3482)          |

### Effect (44 bytes)

| Offset  | Type   | Field             | Notes                                                        |
| ------- | ------ | ----------------- | ------------------------------------------------------------ |
| `+0x00` | u32    | first_effect_ref  | String table index of an effect name                         |
| `+0x04` | u32    | second_effect_ref | String table index of an effect name, or of the empty string |
| `+0x08` | f32[3] | unknown_08        | `0.0, -100.0, 0.0` on entries `1` to `5`, zeros on `0` and `6` (client 3482) |
| `+0x14` | f32[3] | unknown_14        | Zeros on every entry (client 3482)                           |
| `+0x20` | f32[3] | unknown_20        | `1.0` three times on every entry (client 3482)               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                     |
| `+0x04` | pstr[string_count] | strings      | UTF-8 effect names and UTF-16LE course names, in the order the fields first point to them |

## Course Modes

The client compares `getMode()` with `__eSnowBoardCourseMode_Item` and
`__eSnowBoardCourseMode_Speed`, which the Lua does not set. The menu shows
the item ranking for an Item course and the speed ranking for a Speed
course. On client 3482 course `1` (`스코어`, score) stores `0` and courses
`2` (`점프`, jump) and `3` (`스피드`, speed) store `1`, so `0` is Item and
`1` is Speed. The menu also picks a third title image for the Speed course
with key `3`.

## Checkpoints

The courses on client 3482:

| `course_key` | Name     | `mode` | `checkpoint_count` |
| ------------ | -------- | ------ | ------------------ |
| 1            | `스코어` | 0      | 2                  |
| 2            | `점프`   | 1      | 8                  |
| 3            | `스피드` | 1      | 35                 |

The last checkpoint of every course has the same position and
`unknown_18`, and `unknown_30` `6` and `unknown_31` `2`. Course `3`'s
checkpoints between the first and the last store `unknown_18` `650, 1000,
50, 4600, 1600, 50` and `unknown_30` `1`; course `2`'s store
`3700, 2500, 100` or `4300, 2500, 100` with zeros, and `unknown_30` `4`
or `5` to match.

`unknown_30` is one of the values `0` to `6`, and the Effect list has 7
entries: entry `0` and entry `6` name `fN_Event_Object_Start_Track_Aura_01A`,
entries `1` to `5` `fN_Event_Object_Check_Point_01A` (with `_01B` as its
second effect) to `_01F`. The first checkpoints store `0`, the last ones
`6`.

## Field Names

The file is not in client 1784, and no sheet of a private server's
`DataSheets.bexcel` on that client has `Snowboard` in its name.
`course_key`, `name_ref`, `mode` and `checkpoint_count` follow the Lua
getters (`getKeyRaw`, `getName`, `getMode`, `getCheckPointCount`): the
menu's tab count is the course count, and the three tabs carry the three
names. `next_checkpoint_index` holds the next checkpoint's index on every
checkpoint, and the last one's points back to `1`. `region_key` is the
`regioninfo.bss` key whose LOC type 17 name is Snowfall Crasher: Alpine
Glide.

Every string an `*_effect_ref` points to is the name of an
`effectbin/<name>.pae` file (`effectbin/fco_new_snowboard_item_01a.pae`,
`fn_event_object_check_point_01a.pae`). The strings sit in the order of
the first field that points to each, so string `0`,
`fN_Event_Object_Ghost_Location_01A`, belongs to the head's only string
index before the course names, `effect_ref` at `+0x1E` (value `0`). The
item effects are `fCO_New_SnowBoard_Item_01A` with `fCO_NEW_SnowBoard_Item_02A`
and `_01B` with `_02B`.

## Notes

- `snowboard.bss` has its own handler (`_bss/snowboard/`): one row per
  checkpoint with its course key, the Korean course name, the mode name
  and the checkpoint and next checkpoint index.
- [`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md) holds the
  colours of the snowboard course region map.

## Open Questions

### What the Checkpoint Values Are

`unknown_18` reads as two box sizes and `unknown_14` as an angle, and
`unknown_30` fits an index into the Effect list (the start and finish
effect on the first and last checkpoint), with `unknown_31` the kind of
checkpoint (start, between, finish). No Lua getter returns these values,
so the names stay open.

### What the Head Values Are

The head holds the region, an item (`1000383` [Event] Snowfall Crasher
Seal, maybe the course coin or reward), three `180.0` values, a world
position and the values `1`, `200`, `10` and `60`. The HUD and menu call
`ToClient_SnowBoardCoinCount()`, `ToClient_GetSnowBoardRankMax()` and
`ToClient_GetPossibleSnowBoardRecord()`, which may read some of them;
nothing in the Lua ties a call to a field.
