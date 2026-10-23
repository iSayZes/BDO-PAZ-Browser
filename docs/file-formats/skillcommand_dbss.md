# `skillcommand.dbss` Format

## Purpose

The key commands of the Skill Guide widget: one row per skill number with
the skill's Korean name, icon, keyboard command, controller command and
four small flags. The Lua of the widget (`ui_widget_skillcommand.luac`)
reads a row with `getSkillCommandStatus(skillNo)` and its getters
`getName()`, `getIconPath()`, `getCommand()`, `getConsoleCommand()` and
`getExtraParam()`. Every skill number of
[`classskilllist.bss`](classskilllist_bss.md), the Skill Guide list of
each class, is a key here. Companion `skillcommandoffset.dbss` lists where
each row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records        | Row bytes                  |
| ------ | -------------- | ------- | ------------------------- | ------- | -------------- | -------------------------- |
| 4      | 1950 and later | 3482    | `skillcommand.dbss`       | 211,258 | 626 Row        | 187 to 705, 337 on average |
| 4      | 1950 and later | 3482    | `skillcommandoffset.dbss` | 6,264   | 626 Offset Row | 10                         |
| 3      | 1559 to 1945   | 1945    | `skillcommand.dbss`       | 118,968 | 421 Row        | 186 to 546, 283 on average |
| 3      | 1559 to 1945   | 1945    | `skillcommandoffset.dbss` | 4,214   | 421 Offset Row | 10                         |
| 2      | 1346 to 1554   | 1554    | `skillcommand.dbss`       | 70,914  | 349 Row        | 176 to 280, 203 on average |
| 2      | 1346 to 1554   | 1554    | `skillcommandoffset.dbss` | 3,494   | 349 Offset Row | 10                         |
| 1      | 1256 to 1341   | 1341    | `skillcommand.dbss`       | 63,530  | 316 Row        | 174 to 278, 201 on average |
| 1      | 1256 to 1341   | 1341    | `skillcommandoffset.dbss` | 3,164   | 316 Offset Row | 10                         |

| Layout | File                      | Known             | Unknown        |
| ------ | ------------------------- | ----------------- | -------------- |
| 4      | `skillcommand.dbss`       | 208,754 B (98.8%) | 2,504 B (1.2%) |
| 4      | `skillcommandoffset.dbss` | 6,264 B (100.0%)  | 0 B (0.0%)     |
| 3      | `skillcommand.dbss`       | 117,284 B (98.6%) | 1,684 B (1.4%) |
| 3      | `skillcommandoffset.dbss` | 4,214 B (100.0%)  | 0 B (0.0%)     |
| 2      | `skillcommand.dbss`       | 69,518 B (98.0%)  | 1,396 B (2.0%) |
| 2      | `skillcommandoffset.dbss` | 3,494 B (100.0%)  | 0 B (0.0%)     |
| 1      | `skillcommand.dbss`       | 62,266 B (98.0%)  | 1,264 B (2.0%) |
| 1      | `skillcommandoffset.dbss` | 3,164 B (100.0%)  | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 4 |
| 3474   | Layout 4 |
| 3464   | Layout 4 |
| 3458   | Layout 4 |
| 3454   | Layout 4 |
| 3444   | Layout 4 |
| 3435   | Layout 4 |
| 3426   | Layout 4 |
| 3418   | Layout 4 |
| 3412   | Layout 4 |
| 3402   | Layout 4 |
| 3396   | Layout 4 |
| 3387   | Layout 4 |
| 3381   | Layout 4 |
| 3373   | Layout 4 |
| 3364   | Layout 4 |
| 3356   | Layout 4 |
| 3349   | Layout 4 |
| 3342   | Layout 4 |
| 3335   | Layout 4 |
| 3326   | Layout 4 |
| 3321   | Layout 4 |
| 3314   | Layout 4 |
| 3303   | Layout 4 |
| 3302   | Layout 4 |
| 3293   | Layout 4 |
| 3283   | Layout 4 |
| 3275   | Layout 4 |
| 3267   | Layout 4 |
| 3258   | Layout 4 |
| 3251   | Layout 4 |
| 3242   | Layout 4 |
| 3235   | Layout 4 |
| 3229   | Layout 4 |
| 3212   | Layout 4 |
| 3203   | Layout 4 |
| 3193   | Layout 4 |
| 3186   | Layout 4 |
| 3177   | Layout 4 |
| 3169   | Layout 4 |
| 3158   | Layout 4 |
| 3151   | Layout 4 |
| 3144   | Layout 4 |
| 3133   | Layout 4 |
| 3125   | Layout 4 |
| 3118   | Layout 4 |
| 3111   | Layout 4 |
| 3103   | Layout 4 |
| 3095   | Layout 4 |
| 3086   | Layout 4 |
| 3072   | Layout 4 |
| 3062   | Layout 4 |
| 3052   | Layout 4 |
| 3045   | Layout 4 |
| 3037   | Layout 4 |
| 3030   | Layout 4 |
| 3021   | Layout 4 |
| 3012   | Layout 4 |
| 3002   | Layout 4 |
| 2995   | Layout 4 |
| 2987   | Layout 4 |
| 2978   | Layout 4 |
| 2970   | Layout 4 |
| 2959   | Layout 4 |
| 2951   | Layout 4 |
| 2942   | Layout 4 |
| 2935   | Layout 4 |
| 2932   | Layout 4 |
| 2923   | Layout 4 |
| 2919   | Layout 4 |
| 2907   | Layout 4 |
| 2900   | Layout 4 |
| 2891   | Layout 4 |
| 2882   | Layout 4 |
| 2872   | Layout 4 |
| 2863   | Layout 4 |
| 2855   | Layout 4 |
| 2849   | Layout 4 |
| 2844   | Layout 4 |
| 2834   | Layout 4 |
| 2825   | Layout 4 |
| 2819   | Layout 4 |
| 2811   | Layout 4 |
| 2803   | Layout 4 |
| 2794   | Layout 4 |
| 2783   | Layout 4 |
| 2774   | Layout 4 |
| 2765   | Layout 4 |
| 2756   | Layout 4 |
| 2750   | Layout 4 |
| 2743   | Layout 4 |
| 2736   | Layout 4 |
| 2726   | Layout 4 |
| 2717   | Layout 4 |
| 2709   | Layout 4 |
| 2703   | Layout 4 |
| 2695   | Layout 4 |
| 2684   | Layout 4 |
| 2672   | Layout 4 |
| 2665   | Layout 4 |
| 2657   | Layout 4 |
| 2649   | Layout 4 |
| 2644   | Layout 4 |
| 2637   | Layout 4 |
| 2629   | Layout 4 |
| 2619   | Layout 4 |
| 2612   | Layout 4 |
| 2606   | Layout 4 |
| 2602   | Layout 4 |
| 2601   | Layout 4 |
| 2592   | Layout 4 |
| 2583   | Layout 4 |
| 2575   | Layout 4 |
| 2567   | Layout 4 |
| 2560   | Layout 4 |
| 2553   | Layout 4 |
| 2545   | Layout 4 |
| 2538   | Layout 4 |
| 2529   | Layout 4 |
| 2519   | Layout 4 |
| 2513   | Layout 4 |
| 2510   | Layout 4 |
| 2507   | Layout 4 |
| 2503   | Layout 4 |
| 2498   | Layout 4 |
| 2492   | Layout 4 |
| 2487   | Layout 4 |
| 2480   | Layout 4 |
| 2474   | Layout 4 |
| 2468   | Layout 4 |
| 2460   | Layout 4 |
| 2453   | Layout 4 |
| 2444   | Layout 4 |
| 2438   | Layout 4 |
| 2434   | Layout 4 |
| 2429   | Layout 4 |
| 2421   | Layout 4 |
| 2414   | Layout 4 |
| 2407   | Layout 4 |
| 2401   | Layout 4 |
| 2397   | Layout 4 |
| 2393   | Layout 4 |
| 2384   | Layout 4 |
| 2378   | Layout 4 |
| 2372   | Layout 4 |
| 2358   | Layout 4 |
| 2352   | Layout 4 |
| 2347   | Layout 4 |
| 2343   | Layout 4 |
| 2335   | Layout 4 |
| 2327   | Layout 4 |
| 2324   | Layout 4 |
| 2319   | Layout 4 |
| 2313   | Layout 4 |
| 2308   | Layout 4 |
| 2302   | Layout 4 |
| 2295   | Layout 4 |
| 2290   | Layout 4 |
| 2284   | Layout 4 |
| 2276   | Layout 4 |
| 2269   | Layout 4 |
| 2259   | Layout 4 |
| 2250   | Layout 4 |
| 2243   | Layout 4 |
| 2235   | Layout 4 |
| 2229   | Layout 4 |
| 2224   | Layout 4 |
| 2218   | Layout 4 |
| 2215   | Layout 4 |
| 2207   | Layout 4 |
| 2203   | Layout 4 |
| 2196   | Layout 4 |
| 2192   | Layout 4 |
| 2189   | Layout 4 |
| 2183   | Layout 4 |
| 2179   | Layout 4 |
| 2171   | Layout 4 |
| 2163   | Layout 4 |
| 2156   | Layout 4 |
| 2151   | Layout 4 |
| 2147   | Layout 4 |
| 2142   | Layout 4 |
| 2138   | Layout 4 |
| 2134   | Layout 4 |
| 2130   | Layout 4 |
| 2122   | Layout 4 |
| 2107   | Layout 4 |
| 2098   | Layout 4 |
| 2089   | Layout 4 |
| 2081   | Layout 4 |
| 2073   | Layout 4 |
| 2067   | Layout 4 |
| 2063   | Layout 4 |
| 2059   | Layout 4 |
| 2052   | Layout 4 |
| 2044   | Layout 4 |
| 2039   | Layout 4 |
| 2032   | Layout 4 |
| 2025   | Layout 4 |
| 2011   | Layout 4 |
| 2005   | Layout 4 |
| 2000   | Layout 4 |
| 1996   | Layout 4 |
| 1991   | Layout 4 |
| 1985   | Layout 4 |
| 1980   | Layout 4 |
| 1969   | Layout 4 |
| 1964   | Layout 4 |
| 1958   | Layout 4 |
| 1950   | Layout 4 |
| 1945   | Layout 3 |
| 1937   | Layout 3 |
| 1933   | Layout 3 |
| 1927   | Layout 3 |
| 1921   | Layout 3 |
| 1914   | Layout 3 |
| 1908   | Layout 3 |
| 1897   | Layout 3 |
| 1892   | Layout 3 |
| 1886   | Layout 3 |
| 1881   | Layout 3 |
| 1871   | Layout 3 |
| 1866   | Layout 3 |
| 1862   | Layout 3 |
| 1854   | Layout 3 |
| 1846   | Layout 3 |
| 1838   | Layout 3 |
| 1832   | Layout 3 |
| 1826   | Layout 3 |
| 1822   | Layout 3 |
| 1818   | Layout 3 |
| 1804   | Layout 3 |
| 1794   | Layout 3 |
| 1790   | Layout 3 |
| 1784   | Layout 3 |
| 1774   | Layout 3 |
| 1771   | Layout 3 |
| 1762   | Layout 3 |
| 1759   | Layout 3 |
| 1754   | Layout 3 |
| 1749   | Layout 3 |
| 1743   | Layout 3 |
| 1737   | Layout 3 |
| 1731   | Layout 3 |
| 1725   | Layout 3 |
| 1717   | Layout 3 |
| 1710   | Layout 3 |
| 1704   | Layout 3 |
| 1698   | Layout 3 |
| 1690   | Layout 3 |
| 1685   | Layout 3 |
| 1680   | Layout 3 |
| 1674   | Layout 3 |
| 1668   | Layout 3 |
| 1659   | Layout 3 |
| 1649   | Layout 3 |
| 1642   | Layout 3 |
| 1636   | Layout 3 |
| 1628   | Layout 3 |
| 1622   | Layout 3 |
| 1614   | Layout 3 |
| 1608   | Layout 3 |
| 1602   | Layout 3 |
| 1598   | Layout 3 |
| 1594   | Layout 3 |
| 1590   | Layout 3 |
| 1587   | Layout 3 |
| 1584   | Layout 3 |
| 1579   | Layout 3 |
| 1572   | Layout 3 |
| 1565   | Layout 3 |
| 1559   | Layout 3 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
| 1267   | Layout 1 |
| 1261   | Layout 1 |
| 1256   | Layout 1 |
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

| File                      | Required | Role                                                                                          |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------- |
| `skillcommandoffset.dbss` | Optional | `skill_no -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `classskilllist.bss`      | Optional | The class types whose Skill Guide lists each skill number, for the Class column               |
| `languagedata_en.loc`     | Optional | LOC type `2`, `str_id1 = skill_no`: `str_id4` `0` the name, `1` the command, `2` the controller command; LOC type `21` class names |

The skill numbers are skill numbers of [`skill.dbss`](skill_dbss.md); the
handler links each one to it, except the Shadow Arena rows `17051` to
`17174` (Notes).

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file holds 626 rows in 211,258 bytes. The rows are in no
key order and every key is unique.

### Row (variable: 47 bytes + command, name, icon and controller command text)

| Offset                       | Type  | Field                 | Notes                                                                                          |
| ---------------------------- | ----- | --------------------- | ---------------------------------------------------------------------------------------------- |
| `+0x00`                      | u16   | skill_no              | Row key, a `skill.dbss` skill number                                                            |
| `+0x02`                      | u16   | skill_no_dup          | Equal to `skill_no` on every row; the offset index points here                                  |
| `+0x04`                      | str16 | command_kr            | Keyboard command, `getCommand()`: key bindings in angle brackets, `<{KeyBind:Dash}> + <{KeyBind:Attack2}>`, and Korean conditions |
| `command_kr+0x00`            | str16 | name_kr               | Korean skill name, `getName()`                                                                  |
| `name_kr+0x00`               | str16 | icon_path             | Icon path under `ui_texture/icon/`, `getIconPath()`, `New_Icon/04_PC_Skill/...`                |
| `icon_path+0x00`             | u32   | pc_level_for_learning | Character level, `0` to `60` and one `99` on client 3482                                        |
| `icon_path+0x04`             | u8    | show_check            | `0` or `1`                                                                                      |
| `icon_path+0x05`             | u8    | awaken_command        | `1` for a command of the awakening weapon, see Notes                                           |
| `icon_path+0x06`             | u8    | extra_param           | `getExtraParam()`: Drakania form, see Extra Param                                               |
| `icon_path+0x07`             | u32   | unknown_icon_path_07  | `0` on every row of clients 1784 and 3482                                                       |
| `icon_path+0x0B`             | str16 | console_command_kr    | Controller command, `getConsoleCommand()`, read while `_ContentsGroup_UsePadSnapping` is on; empty on 41 rows |

### `skillcommandoffset.dbss`

Bare offset table into `skillcommand.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `skillcommand.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                  |
| ------- | ---- | ----------- | -------------------------------------- |
| `+0x00` | u16  | skill_no    | Key of the row it points at            |
| `+0x02` | u32  | data_offset | Row start + 2, at `skill_no_dup`       |
| `+0x06` | u32  | data_size   | The row less its 2-byte key            |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3482 every
index row points at the row with its key and the rows tile the file.

## Layout 3

### Row (variable: 46 bytes + command, name, icon and controller command text)

The row has no `extra_param`.

| Offset                       | Type  | Field                 | Notes                                                                 |
| ---------------------------- | ----- | --------------------- | --------------------------------------------------------------------- |
| `+0x00`                      | u16   | skill_no              | Row key                                                               |
| `+0x02`                      | u16   | skill_no_dup          | Equal to `skill_no`                                                   |
| `+0x04`                      | str16 | command_kr            | Keyboard command as keys, `<Shift> + <RB>`                            |
| `command_kr+0x00`            | str16 | name_kr               | Korean skill name                                                     |
| `name_kr+0x00`               | str16 | icon_path             | Icon path under `ui_texture/icon/`                                    |
| `icon_path+0x00`             | u32   | pc_level_for_learning | Character level                                                       |
| `icon_path+0x04`             | u8    | show_check            | `0` or `1`                                                            |
| `icon_path+0x05`             | u8    | awaken_command        | `1` for a command of the awakening weapon                             |
| `icon_path+0x06`             | u32   | unknown_icon_path_07  | `0` on every row of client 1784                                       |
| `icon_path+0x0A`             | str16 | console_command_kr    | Controller command with key bindings, `<{KeyBind:Dash}> + <{KeyBind:Attack2}>` |

On client 1784 the file holds 372 rows.

## Layout 2

### Row (variable: 38 bytes + command, name and icon text)

The row has no `console_command_kr`.

| Offset            | Type  | Field                 | Notes                                      |
| ----------------- | ----- | --------------------- | ------------------------------------------ |
| `+0x00`           | u16   | skill_no              | Row key                                    |
| `+0x02`           | u16   | skill_no_dup          | Equal to `skill_no`                        |
| `+0x04`           | str16 | command_kr            | Keyboard command as keys, `<Shift> + <RB>` |
| `command_kr+0x00` | str16 | name_kr               | Korean skill name                          |
| `name_kr+0x00`    | str16 | icon_path             | Icon path under `ui_texture/icon/`         |
| `icon_path+0x00`  | u32   | pc_level_for_learning | Character level                            |
| `icon_path+0x04`  | u8    | show_check            | `0` or `1`                                 |
| `icon_path+0x05`  | u8    | awaken_command        | `0` or `1`                                 |
| `icon_path+0x06`  | u32   | unknown_icon_path_07  | `0`                                        |

On client 1554 the file holds 349 rows.

## Layout 1

### Row (variable: 36 bytes + command, name and icon text)

The row has no `skill_no_dup`, and each `skillcommandoffset.dbss` row
points at the row start with the whole row as its size.

| Offset            | Type  | Field                 | Notes                                    |
| ----------------- | ----- | --------------------- | ---------------------------------------- |
| `+0x00`           | u16   | skill_no              | Row key                                  |
| `+0x02`           | str16 | command_kr            | Keyboard command as keys, `<E>`          |
| `command_kr+0x00` | str16 | name_kr               | Korean skill name                        |
| `name_kr+0x00`    | str16 | icon_path             | Icon path under `ui_texture/icon/`       |
| `icon_path+0x00`  | u32   | pc_level_for_learning | Character level                          |
| `icon_path+0x04`  | u8    | show_check            | `0` or `1`                               |
| `icon_path+0x05`  | u8    | awaken_command        | `0` or `1`                               |
| `icon_path+0x06`  | u32   | unknown_icon_path_07  | `0`                                      |

On client 1341 the file holds 316 rows.

## Extra Param

The widget Lua defines `_eDrakaniaFormType = {FORM_NORMAL = 1, FORM_DRAGON
= 2}`. In `FromClient_SkillCommandList(skillNo, isAwaken)` it drops an
awakening command of a Drakania whose `getExtraParam()` names the other
form: `1` while `ToClient_isDrakaniaDragonForm()` holds, `2` while it does
not.

| Value | Meaning                      | Rows (client 3482) |
| ----- | ---------------------------- | ------------------ |
| 0     | Shown in both forms          | 614                |
| 1     | Drakania normal form only    | 5                  |
| 2     | Drakania dragon form only    | 7                  |

The five `1` rows (`6993`, `7000`, `7010`, `7015`, `7017`) and five of the
`2` rows (`7020`, `7025`, `7029`, `7036`, `7037`) are awakening rows of the
Drakania list in `classskilllist.bss`, in pairs such as `7000` Tectonic
Slam I and `7036` Tectonic Slam. The other two `2` rows, `6820` Brimbolt
Strike I and `6826` Flow: Brimbolt Wave I, have `awaken_command` `0` and
no `classskilllist.bss` row, so the filter never reads them.

## Field Names

The `SkillCommand` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `ClassType`, `SkillNo`, `PcLevel_ForLearning`,
`SkillName`, `Control`, `Console`, `IconImageFile`, `ShowCheck` and
`AwakenCommand`. The file stores them in another order and has no
`ClassType`; `classskilllist.bss` gives the class instead. The 2016
client's debug symbols have no struct for the table. `extra_param` is
named after its Lua getter.

| Field                 | Column                | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------- | ------------------------ | ------------------------ |
| skill_no              | `SkillNo`             | 371 of 372 keys          | 363 of 626 keys          |
| command_kr            | `Control`             | 363 of 371               | 41 of 363                |
| name_kr               | `SkillName`           | 367 of 371               | 344 of 363               |
| icon_path             | `IconImageFile`       | 368 of 371               | 344 of 363               |
| pc_level_for_learning | `PcLevel_ForLearning` | 370 of 371               | 161 of 363               |
| show_check            | `ShowCheck`           | 371 of 371               | 317 of 363               |
| awaken_command        | `AwakenCommand`       | 371 of 371               | 363 of 363               |
| console_command_kr    | `Console`             | 363 of 371               | 349 of 363               |

By client 3482 the keyboard command is written as key bindings: 307 of the 363
shared `command_kr` values equal the sheet's `Console` text, and the
command and the controller command differ on 13 rows with both set. Of the
202 changed levels, 72 go from `0` to `1` and 64 to `56`.

## Notes

- Every number of `classskilllist.bss` has a row (517 of 626 rows on client
  3482). Every skill number is a `skill.dbss` skill number; 567 rows have
  the LOC type 10 name of that skill, 13 differ in the rank numeral only
  (`819` Fireball against Fireball II) and 5 (`1412`, `2173`, `2175`,
  `2176`, `7015`) name another skill.
- `awaken_command` splits the Skill Guide list by weapon: the Wizard row of
  `classskilllist.bss` holds eight numbers with `0` and five (`2212` to
  `2236`) with `1`, the eight main weapon and the five awakening lines the
  in-game check of that doc found on client 3474. The widget Lua gets the
  flag as `isAwaken` in `FromClient_SkillCommandList(skillNo, isAwaken)`
  and drops awakening commands unless the awakening weapon is out.
- The 41 rows `17051` to `17174` have no controller command and name
  skills such as War Cry (`17062`) and Night Crow (`17105`), while
  `skill.dbss` names these numbers Tamer and Valkyrie skills. Their
  commands describe effects (`[Charge] + <Bound>`) instead of keys. A
  private server's `datasheet_skillcommand_shadow.xlsm` on client 1784
  holds these rows under class type `3`, with `17051` to `17058` in its
  `SkillCheck` sheet. On client 3482 the `classskilllist.bss` row of class
  type `3`, Wukong, lists `17051` to `17058` after nine Wukong skills. The
  handler shows these skill numbers without a `skill.dbss` link.
- 95 rows on client 3482 have an icon whose number is not the row's skill
  number (`5127` uses `PGW_Skill_5130.dds`). For a skill the player has
  learned, the widget shows the name and icon of the highest learned rank
  (`ToClient_GetTopLevelLearnActiveSkillNo()`, `getSkillTypeStaticStatus()`)
  and falls back to this row's.
- The LOC type 2 command texts keep the key bindings and translate the
  conditions: `9565` is `<{KeyBind:Jump}> [after other skills]`.

## Open Questions

### What Show Check Does

`ShowCheck` is `1` on 424 of 626 rows (client 3482). The widget Lua reads
no getter for it; `SkillCommand_SetSkillShow(skillNo, isShow)` takes its
flag from the client. Whether `show_check` picks the commands the Skill
Guide shows first, or something else, is open.

### When the Level Applies

`pc_level_for_learning` is `56` on 130 rows (client 3482), 125 of them
with `awaken_command` `1`, and `1` on 182. The Lua has a separate
`FromClient_SkillCommandListonLevelUp(skillNo, isAwaken)` callback.
Whether reaching the level adds the row's command to the widget is a lead
from the callback name only.
