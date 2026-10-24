# `buffsimply.bss` Format

## Purpose

A compact copy of [`buff.dbss`](buff_dbss.md): one fixed 32-byte row per buff
with the buff ID, the icon path and `effect_name` as indices into a shared
string table, `is_shown`, `is_debuff`, `remove_on_dead` and the equipment the
buff needs. It holds no name, parameters,
duration or description, so it covers what the buff bar needs to draw a buff
and nothing about its effect.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes     | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------- | --------- | --------------- | --------- |
| 2      | 3464 and later | 3483    | `buffsimply.bss` | 1,490,698 | 44,724 Buff Row | 32        |
| 1      | 1311 to 3458   | 3458    | `buffsimply.bss` | 1,398,407 | 44,645 Buff Row | 30        |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 2      | `buffsimply.bss` | 819,838 B (55.0%) | 670,860 B (45.0%) |
| 1      | `buffsimply.bss` | 728,732 B (52.1%) | 669,675 B (47.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
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
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
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

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `buff.dbss`           | Optional | Full buff records; every row here has a record there        |
| `languagedata_en.loc` | Optional | English descriptions, LOC type 5 keyed by `buff_id`         |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset              | Type            | Field        | Notes                                                  |
| ------------------- | --------------- | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                           |
| `+0x04`             | u32             | count        | Number of rows; 44,683 on client 3464, equal to the `buff.dbss` count |
| `+0x08`             | Buff Row[count] | rows         | See Buff Row                                           |
| `rows+0x00`         | String Table    | string_table | See String Table                                       |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where the rows end         |
| `string_table+0x04` | u32             | zero         | Always 0                                               |

The rows follow `buffoffset.dbss` order exactly, which is neither ascending nor
descending by ID (the first row is buff 4100000000 on client 3464, 48879 on
3458).

### Buff Row (32 bytes)

Fields are unaligned. The Source column names the `buff.dbss` field that holds
the same value in every row, when one does.

| Offset  | Type     | Field           | Source (`buff.dbss`)    | Notes                                                                          |
| ------- | -------- | --------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u32      | buff_id         | `buff_id`               | Unique; 43 to 65,528 and five IDs from 700,000 to 4,100,000,000                |
| `+0x04` | u8       | need_equip_type | stats `need_equip_type` | `0` in every row but buff 2078 (`13`)                                          |
| `+0x05` | bytes[2] | unknown_05      |                         | Always `0`                                                                     |
| `+0x07` | u8       | unknown_07      | stats `+0x7D`           | `0` in every row but buff 2078 (`1`)                                           |
| `+0x08` | u8       | unknown_08      | stats `+0x7D`           | Same values as `unknown_07`; not stats `+0x7E`, see Notes                      |
| `+0x09` | u8       | unknown_09      | stats `unknown_7f`      | Always `2`                                                                     |
| `+0x0A` | u8       | unknown_0a      |                         | Always `0`                                                                     |
| `+0x0B` | u8       | need_equip_slot | stats `need_equip_slot` | `46` (no slot) in every row but buff 2078 (`6`)                                |
| `+0x0C` | u8       | unknown_0c      | stats `unknown_82`      | `2` in every row but buff 2078 (`1`)                                           |
| `+0x0D` | u32      | effect_name_ref | `effect_name`           | String table index; 187 distinct, `0` (`"0"`) in 39,527 rows, `1` (`""`) in 52 |
| `+0x11` | u8       | is_debuff       | stats `is_debuff`       | `1` in 14,432 rows                                                             |
| `+0x12` | u8       | unknown_12      |                         | Always `1`; no `buff.dbss` byte matches, see Open Questions                    |
| `+0x13` | bytes[3] | unknown_13      |                         | Always `0`                                                                     |
| `+0x16` | u8       | remove_on_dead  | stats `remove_on_dead`  | `1` in 33,944 rows                                                             |
| `+0x17` | u8       | is_shown        | `is_shown`              | `1` in 12,766 rows                                                             |
| `+0x18` | u32      | unknown_18      | tail `unknown_02`       | `0` in 25,701 rows, `1` in 14,420, `2` in 4,562                                |
| `+0x1C` | u32      | icon_ref        | `icon_path`             | String table index; `1` (the empty string) in 29,357 rows                      |

### String Table (variable: 4 bytes + strings)

1,235 strings on client 3464, all distinct and all referenced. `effect_name_ref`
and `icon_ref` index the same table and share only the empty string: index 0
is `"0"`, index 1 is `""`, and every other entry is either an `effect_name`
value or an icon path.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 1,235 on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Layout 1

Before client 3464 `buff_id` was a u16 and every later field sat 2 bytes
earlier. Only the Buff Row differs from Layout 2. Field names keep Layout
2's offsets, so `unknown_05` sits at `+0x03` here. The parser reads only
Layout 2.

### Buff Row (30 bytes)

| Offset  | Type     | Field           | Notes |
| ------- | -------- | --------------- | ----- |
| `+0x00` | u16      | buff_id         |       |
| `+0x02` | u8       | need_equip_type |       |
| `+0x03` | bytes[2] | unknown_05      |       |
| `+0x05` | u8       | unknown_07      |       |
| `+0x06` | u8       | unknown_08      |       |
| `+0x07` | u8       | unknown_09      |       |
| `+0x08` | u8       | unknown_0a      |       |
| `+0x09` | u8       | need_equip_slot |       |
| `+0x0A` | u8       | unknown_0c      |       |
| `+0x0B` | u32      | effect_name_ref |       |
| `+0x0F` | u8       | is_debuff       |       |
| `+0x10` | u8       | unknown_12      |       |
| `+0x11` | bytes[3] | unknown_13      |       |
| `+0x14` | u8       | remove_on_dead  |       |
| `+0x15` | u8       | is_shown        |       |
| `+0x16` | u32      | unknown_18      |       |
| `+0x1A` | u32      | icon_ref        |       |

## Notes

- Checked against `buff.dbss` on client 3464: all 44,683 IDs have a record
  there, and `effect_name_ref`, `icon_ref`, `is_shown` and every field with a
  Source match the record in all 44,683 rows.
- The app builds its buff icon lookup index (`IndexKind.BUFF_ICON`, read
  through `IconKind.BUFF`) from this file: it gives the same paths as
  `buff.dbss` from a 1.4 MB fixed-row file, without walking the 12 MB of
  variable-length records.
- Icon paths follow the `buff.dbss` conventions: 15,282 rows set one, over
  1,043 stored strings that become 1,017 paths once lowercased with `\`
  turned into `/` (35 stored strings use backslashes). 206 rows store the
  placeholder `UNKNOWN`, and three double a separator
  (`04_PC_Skill//04_Debuff`); collapsing it finds their file. Resolve under
  `ui_texture/icon/`, as for `buff.dbss`. On client 3458, 14,884 of the
  15,076 real icons exist; the other 192 rows point at 22 paths the client
  does not ship.
- The icon is not unique to a headline buff: the hidden effects that follow
  one often store the same path (all of 48717 to 48734, the three Adventure's
  Boon runs, store `SilverBless.dds`), while only the headline has `is_shown`.
- Buff 2078 (`[장착용] 두건 효과 : 정체 감추기`, "equip: hood effect, hide
  identity") is the only row where `+0x04` to `+0x0C` differ from the
  constants, and its stats bytes `+0x7A` to `+0x82` read
  `0d 00 00 01 01 02 00 06 01`, the same nine bytes as this row: the
  `_needEquipType` copy of an `itemenchant.dbss` equip type (see the
  `buff.dbss` Field Names). On every other buff stats `+0x7E` (`unknown_7e`) is
  `1` in 44,588 rows while `+0x08` here stays `0`, so `+0x08` is not that
  byte. Only per-byte matches are claimed above.
- `buff.dbss` fields with no copy here: `name`, `buff_level`, `group`,
  `condition_type`, `effect_type`, the parameters, `duration_ms`,
  `apply_rate`, `description` and `stacking_category`.
- [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  mentions the file only as a 30-byte PABR projection over the buff keys (the
  pre-3464 row size) with
  an icon string-table reference; it gives no row layout.

## Field Names

The named fields take the names of the `buff.dbss` fields they copy, which come from the 2016 `gc::BuffStaticStatus` and the `Buff_Table` of a private server on client 519 ([buff.dbss Field Names](buff_dbss.md#field-names)). `unknown_07`, `unknown_08`, `unknown_09` and `unknown_0c` sit in the `_isExtractable`, `_isUseAvatarMesh`, `_rangeType` and `_enchantFailType` places of the `_needEquipType` copy; no server column holds them and the matching `itemenchant.dbss` header bytes have no name either. `unknown_18` copies `buff.dbss` tail `unknown_02`, which matches no server column.

## Open Questions

### What does `unknown_12` hold?

It is `1` in every row and matches no `buff.dbss` byte in all rows. The
closest are stats `param_1_set` (`1` in 44,525 rows) and `unknown_7e` (`1` in 44,550),
so it may be one of those with the exceptions dropped, or a constant of the
compact format.
