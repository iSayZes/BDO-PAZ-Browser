# `eventmanagement.bss` Format

## Purpose

The scheduled world events and what each one switches on. The file holds two
tables. An event row has a name, a condition script that says when and on
which servers it runs (`checkPeriodbyGMT(0, 2026/09/17-09:00,
2026/10/08-09:00);`, `CheckWeekDayAndDuration(3,20,45,15);`,
`!CheckWorldNo(400);`) and the keys of the event contents it sets. An event
contents row is one action with up to four parameters: an event map or
sound (`c_seteventmap`, `c_setsoundevent`), a character or field boss spawn
(`s_spawncharacter`, `s_spawnrandomfieldboss`) or an EXP or drop rate bonus
(`s_addexp`, `s_addlifeexp`, `s_adddroprate`). On client 3483 the file
holds 1,386 events and 517 event contents.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                  | Bytes   | Records                           | Row bytes |
| ------ | ------------- | ------- | --------------------- | ------- | --------------------------------- | --------- |
| 1      | 805 and later | 3483    | `eventmanagement.bss` | 498,255 | 1,386 Event Row, 517 Contents Row | 15        |

| Layout | File                  | Known             | Unknown        |
| ------ | --------------------- | ----------------- | -------------- |
| 1      | `eventmanagement.bss` | 496,869 B (99.7%) | 1,386 B (0.3%) |

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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | Layout 1             |
| 1261   | Layout 1             |
| 1256   | Layout 1             |
| 1250   | Layout 1             |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | Layout 1             |
| 805    | Layout 1             |
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

None. Character names come from LOC type 6, else the Korean
`characterstatic.dbss` name (`CHARACTER_NAME_KR` lookup index).

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with two counted tables back to back, then the counted string table
and 8-byte trailer of
[`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). Every text of both tables is a string table
index.

| Offset                | Type                         | Field              | Notes                                          |
| --------------------- | ---------------------------- | ------------------ | ---------------------------------------------- |
| `+0x00`               | char[4]                      | magic              | ASCII `PABR`                                   |
| `+0x04`               | u32                          | event_count        | Number of events; 1,386 on client 3483         |
| `+0x08`               | Event Row[event_count]       | event_rows         | See Event Row                                  |
| `event_rows+0x00`     | u32                          | contents_count     | Number of event contents; 517 on client 3483   |
| `event_rows+0x04`     | Contents Row[contents_count] | contents_rows      | See Contents Row                               |
| `contents_rows+0x00`  | String Table                 | string_table       | See String Table                               |
| `string_table+0x00`   | u32                          | string_table_start | Offset of the string table, where the rows end |
| `string_table+0x04`   | u32                          | zero               | Always `0`                                     |

On client 3483 the file is 8 + 1,386 x 15 + 4 + 517 x 22 + 466,071 + 8 =
498,255 bytes.

### Event Row (15 bytes)

| Offset  | Type | Field            | Notes                                                                                     |
| ------- | ---- | ---------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | event_no         | Row key, unique; `2` to `9702` on client 3483                                             |
| `+0x02` | u32  | event_name_ref   | String table index of the event name (`DonghwaV2`, `GuildHouseAuction_NA`); 635 distinct names on 1,386 rows (client 3483) |
| `+0x06` | u32  | condition_ref    | String table index of the condition script; see Conditions                                |
| `+0x0A` | u32  | setted_event_ref | String table index of the event contents list: `event_contents_no` values joined by `,` (`3222`, `9075, 9072, 9013`) |
| `+0x0E` | u8   | unknown_0e       | `0` on every row of clients 1784 and 3483; see Open Questions                             |

### Contents Row (22 bytes)

| Offset  | Type | Field             | Notes                                                                    |
| ------- | ---- | ----------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | event_contents_no | Row key, unique; `1001` to `24598` on client 3483                        |
| `+0x02` | u32  | function_ref      | String table index of the action name, lower case (`s_spawncharacter`); see Functions |
| `+0x06` | u32  | param_1_ref       | String table index of the first parameter                                |
| `+0x0A` | u32  | param_2_ref       | String table index of the second parameter; `0` as text on 356 of 517 rows (client 3483) |
| `+0x0E` | u32  | param_3_ref       | String table index of the third parameter                                |
| `+0x12` | u32  | param_4_ref       | String table index of the fourth parameter                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `2405` on client 3483                     |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; all UTF-16 on client 3483 |

Each text is stored once: rows with the same name, condition or parameter
share one index. On client 3483 the `0` of 1,380 parameter slots is the one
entry at index `2003`.

## Conditions

The text of `condition_ref` is a list of calls separated by `;`, each one
optionally negated with `!`. Counted over the 1,386 events of client 3483
(an event with a call more than once counts once):

| Call                                                  | Events | Arguments                                                    |
| ----------------------------------------------------- | ------ | ------------------------------------------------------------ |
| `checkPeriod(start, end)`                             | 903    | Two times as `2025/07/10-09:00`                              |
| `checkPeriodbyGMT(n, start, end)`                     | 470    | `0` on every call, then two times                            |
| `CheckWeekDayAndDuration(day, hour, minute, minutes)` | 1,285  | Weekday `0` to `6`, start hour and minute, length in minutes |
| `CheckWorldNo(n)`                                     | 1,287  | Negated on every call (`!CheckWorldNo(400);`)                |
| `CheckServerType(type)`                               | 753    | Negated on 2,237 of 2,240 calls                              |
| `CheckMainChannel()`                                  | 740    | None                                                         |
| `BiWeeklyCheck(n)`                                    | 2      | `1` on both (`GuildHouseAuction_EU` and `_NA`)               |

No event has more than one period call, and 13 have none. The same calls
appear in the `visible_conditions` of [`newquest.bss`](newquest_bss.md) (as
`checkperiodbyGmt`).

## Functions

`function` names what an event contents row does. The `c_` functions act on
the client, the `s_` functions on the server. On client 3483:

| Function                 | Rows | Parameters                                                                     |
| ------------------------ | ---- | ------------------------------------------------------------------------------ |
| `s_spawncharacter`       | 230  | `param_1` character keys joined by `,` (`59128,59129,27199`), the rest `0`     |
| `s_addlifeexp`           | 120  | `param_1` an amount (`1000000`), `param_2` one of `0` to `6`, `8`, `9` or `11` (12 rows each) |
| `c_seteventmap`          | 41   | `param_1` an event map name (`xmas`, `halloween`)                              |
| `s_spawnrandomfieldboss` | 40   | `param_1` a field boss character key (`28922` Dastard Bheg), `param_2` and `param_3` `0` or `1` |
| `s_addexp`               | 17   | `param_1` an amount (`500000`)                                                 |
| `c_setsoundevent`        | 13   | `param_1` a time and region list (`DayTime-5, 30, 32, 77`), `param_2` a sound event (`Event_Xmas_Day`) |
| `s_addvehicleexp`        | 12   | `param_1` an amount                                                            |
| `s_adddroprate`          | 12   | `param_1` an amount (`100000`)                                                 |
| `s_addskillexp`          | 11   | `param_1` an amount                                                            |
| `c_seteventui`           | 5    | `param_1` an event name (`x-mas`, `ThanksGivingDay`)                           |
| `c_seteffectevent`       | 4    | `param_1` an effect name (`Aurora`, `firework`)                                |
| `s_changeselectrate`     | 3    | `param_1` a character key (`55944` Dog), then three numbers (`16001`, `0`, `3000`); see Open Questions |
| `s_copyequipitemevent`   | 2    | All `0`                                                                        |
| `c_navigationposition`   | 1    | `param_2` a list of positions, `param_3` the GAME sheet key `LUA_NAVIGATION_FISHING_EVENT` |

`s_varytemperature`, `s_showdroprateicon`, `s_showexpicon`,
`s_triggerexcution`, `s_feverpointmore` and `s_thanksgivingevent` have one
row each.

## Field Names

The event rows are the `EventManage` sheet and the event contents rows the
`EventContents` sheet of a private server's `DataSheets.bexcel` on client
1784. The private server's own compiled `eventmanagement.bss` matches its
sheets on 387 of 387 event keys and 229 of 229 contents keys in every
column (`function` ignoring case). The official client 1784 file matches by
key:

| Field                                    | Column            | Same value (client 1784) |
| ---------------------------------------- | ----------------- | ------------------------ |
| `event_no`                               | `EventNo`         | 387 of 387 keys          |
| `event_name_ref`                         | `EventName`       | 262 of 387               |
| `condition_ref`                          | `Condition`       | 255 of 387               |
| `setted_event_ref`                       | `SettedEvent`     | 387 of 387               |
| `event_contents_no`                      | `EventContentsNo` | 229 of 229 keys          |
| `function_ref`                           | `Function`        | 229 of 229, ignoring case |
| `param_1_ref` to `param_4_ref`           | `Param1` to `Param4` | 229 of 229            |

The name and condition misses are the private server's edits: boss spawn
names and times one hour apart (`BossSpawn_Sun_1400_NA` in the sheet,
`BossSpawn_Sun_1500_NA` in the file) and periods moved to other dates. The
official file has 402 event rows, 15 more than the sheet. Neither sheet has
a column for `unknown_0e`.

The 29-row `EventManage` table of a private server on client 519 has the
same four columns but holds 2017 events (`Flond_or_Goose` is key `2` there,
`4` on client 1784), so it names no field. Its `EventContents` table has the
six `EventContents` columns.

## Notes

- Neither table is stored in key order: the file starts with event `3050`
  and contents row `3049` (client 3483).
- On client 3483 every `setted_event` key (1,420 in all) is an
  `event_contents_no` of the file. 1,360 events set one contents row, 25 set
  two and one sets ten. 379 of the 517 contents rows are set by no event.
- 641 of the 673 distinct character keys in the `param_1` of
  `s_spawncharacter`, `s_spawnrandomfieldboss` and `s_changeselectrate` have
  a LOC type 6 name on client 3483.
- The sheet writes `function` in mixed case (`C_SetEventMap`,
  `S_SpawnCharacter`); the compiled file holds it in lower case. The
  parameters keep their case (`CherrBlossom_Festival`).
- The client Lua of client 3482 calls no getter on this table, and the
  2016 PDB has no struct for it.
- The `No file` clients 837 to 1246 name the file
  `#na#eventmanagement.bss` (clients 1000 and 1230 checked).
- Clients 435 to 794 store the file without PABR magic: the texts are
  inline `str16` and an event row starts with its u16 key twice (client
  435). No layout here reads them yet.

## Open Questions

### What `unknown_0e` Holds

The byte after `setted_event_ref` is `0` on every row of the official
clients 1784 and 3483. In the private server's own client 1784 build it is
`1` on 6 of 390 rows (`SteamPunk_Halloween_2021`, `Cherry Blossom Event`
and four hot time and drop events), and no sheet column holds it. In the
client 1784 server's `Load_EventManage` the row keeps a u16 (set to `0x100`)
and a u8 (set to `0`) after the parsed `SettedEvent` list that no column
fills; one of them may be this byte.

### What the `s_changeselectrate` Parameters Name

The three `s_changeselectrate` rows hold `55944`, `55945` and `55946` in
`param_1` (LOC type 6 names all three Dog), then `16001`, `4998` or
`40218`, then `0`, then `3000`, `1500` or `13000` (client 3483). Which
table the second number keys and what the fourth one scales is not known.

### What `checkPeriodbyGMT` Reads From Its First Argument

`checkPeriodbyGMT` takes a number before its two times: `0` on every call
of the official clients 1784 (178 calls) and 3483 (470 calls). Only the
private server's client 1784 sheet writes `3` on some rows. It may be a
time zone offset or a mode; the data does not show which.
