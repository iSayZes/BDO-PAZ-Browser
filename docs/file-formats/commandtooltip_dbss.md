# `commandtooltip.dbss` Format

## Purpose

The key combination line of a skill tooltip, once for keyboard and mouse
(`pc_command_kr`) and once for the console pad (`console_command_kr`):
`<PAColor0xffd8ff00>{KeyBind:Dash} + {KeyBind:Attack2}<PAOldColor>`, or a
note such as `기술 슬롯에 등록해서 사용 가능` ("Can be added to a Quick
Slot"). Each row is keyed by the hash of a string key such as `WARRIOR_01`;
the key itself is not stored. Both texts are Korean; LOC type 55 holds the
user-language text under the same hash. Companion
`commandtooltipoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes     | Records          | Row bytes                   |
| ------ | -------------- | ------- | --------------------------- | --------- | ---------------- | --------------------------- |
| 2      | 1529 and later | 3483    | `commandtooltip.dbss`       | 3,865,388 | 7,663 Row        | 36 to 2,614, 504 on average |
| 2      | 1529 and later | 3483    | `commandtooltipoffset.dbss` | 91,976    | 7,663 Offset Row | 12                          |
| 1      | 1239 to 1524   | 1524    | `commandtooltip.dbss`       | 1,001,964 | 5,289 Row        | 22 to 1,036, 189 on average |
| 1      | 1239 to 1524   | 1524    | `commandtooltipoffset.dbss` | 63,488    | 5,289 Offset Row | 12                          |

| Layout | File                        | Known               | Unknown         |
| ------ | --------------------------- | ------------------- | --------------- |
| 2      | `commandtooltip.dbss`       | 3,834,736 B (99.2%) | 30,652 B (0.8%) |
| 2      | `commandtooltipoffset.dbss` | 91,976 B (100.0%)   | 0 B (0.0%)      |
| 1      | `commandtooltip.dbss`       | 980,808 B (97.9%)   | 21,156 B (2.1%) |
| 1      | `commandtooltipoffset.dbss` | 63,488 B (100.0%)   | 0 B (0.0%)      |

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
| 1871   | Layout 2             |
| 1866   | Layout 2             |
| 1862   | Layout 2             |
| 1854   | Layout 2             |
| 1846   | Layout 2             |
| 1838   | Layout 2             |
| 1832   | Layout 2             |
| 1826   | Layout 2             |
| 1822   | Layout 2             |
| 1818   | Layout 2             |
| 1804   | Layout 2             |
| 1794   | Layout 2             |
| 1790   | Layout 2             |
| 1784   | Layout 2             |
| 1774   | Layout 2             |
| 1771   | Layout 2             |
| 1762   | Layout 2             |
| 1759   | Layout 2             |
| 1754   | Layout 2             |
| 1749   | Layout 2             |
| 1743   | Layout 2             |
| 1737   | Layout 2             |
| 1731   | Layout 2             |
| 1725   | Layout 2             |
| 1717   | Layout 2             |
| 1710   | Layout 2             |
| 1704   | Layout 2             |
| 1698   | Layout 2             |
| 1690   | Layout 2             |
| 1685   | Layout 2             |
| 1680   | Layout 2             |
| 1674   | Layout 2             |
| 1668   | Layout 2             |
| 1659   | Layout 2             |
| 1649   | Layout 2             |
| 1642   | Layout 2             |
| 1636   | Layout 2             |
| 1628   | Layout 2             |
| 1622   | Layout 2             |
| 1614   | Layout 2             |
| 1608   | Layout 2             |
| 1602   | Layout 2             |
| 1598   | Layout 2             |
| 1594   | Layout 2             |
| 1590   | Layout 2             |
| 1587   | Layout 2             |
| 1584   | Layout 2             |
| 1579   | Layout 2             |
| 1572   | Layout 2             |
| 1565   | Layout 2             |
| 1559   | Layout 2             |
| 1554   | Layout 2             |
| 1547   | Layout 2             |
| 1537   | Layout 2             |
| 1529   | Layout 2             |
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
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | No documented layout |
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

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `commandtooltipoffset.dbss` | Optional | `key_hash -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`       | Optional | Both texts in the user's language (type `55`)                                  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `7663` on client 3483 |
| `+0x04` | Row[count] | rows  | See Row                               |

### Row (variable: 24 bytes + texts)

| Offset                    | Type  | Field                         | Notes |
| ------------------------- | ----- | ----------------------------- | ----- |
| `+0x00`                   | u32   | key_hash                      | `key_hash()` of the row's string key (lookup3 over its UTF-16LE text, seed `0xC5EDE`, `_common/string_hash.py`); unique per row |
| `+0x04`                   | str16 | pc_command_kr                 | Korean text for keyboard and mouse; LOC type 55 `(key_hash, 0)`. Line breaks are the two characters `\n` |
| `pc_command_kr+0x00`      | str16 | console_command_kr            | Korean text for the console pad; LOC type 55 `(key_hash, 1)`. Equals `pc_command_kr` on 6,817 of 7,663 rows (client 3483) |
| `console_command_kr+0x00` | u32   | unknown_console_command_kr_00 | `0` on every row of clients 1784 and 3483 |

The rows are not sorted by key. The LOC type 55 key is
`(key_hash, 0, 0, variant)`: variant `0` is `pc_command_kr`, `1` is
`console_command_kr`. On client 3483 every row has both LOC rows.

### `commandtooltipoffset.dbss`

`PABR` index with 12-byte rows and a u32 key.

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32               | count              | Equals the `commandtooltip.dbss` count        |
| `+0x08`             | Offset Row[count] | rows               | See Offset Row                                |
| `rows+0x00`         | String Table      | string_table       | The PABR string table, present but empty      |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 12 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                       |
| ------- | ---- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key_hash    | Key of the row it points at                                 |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `commandtooltip.dbss`, at its `key_hash` |
| `+0x08` | u32  | data_size   | The whole row                                               |

Read by `parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; read in offset order they
cover the main file from `+0x04` to its end, and every index row points at
the row with its key (clients 1784 and 3483).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

### Row (variable: 16 bytes + text)

One text per row: `console_command_kr` is not there yet.

| Offset               | Type  | Field                         | Notes |
| -------------------- | ----- | ----------------------------- | ----- |
| `+0x00`              | u32   | key_hash                      |       |
| `+0x04`              | str16 | pc_command_kr                 |       |
| `pc_command_kr+0x00` | u32   | unknown_console_command_kr_00 |       |

## Field Names

The `Command_Tooltip_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Key`, `PC`, `Console`, `Sura` and `Nachal`,
5,822 rows. `key_hash()` of every `Key` is a `key_hash` of client 1784,
whose file also has 5,822 rows. Matched by that hash:

| Field              | Column    | Same value (client 1784) | Same value (client 3483) |
| ------------------ | --------- | ------------------------ | ------------------------ |
| key_hash           | `Key`     | 5,822 of 5,822 (hashed)  | 5,822 of 5,822 (hashed)  |
| pc_command_kr      | `PC`      | 5,822 of 5,822           | 1,394 of 5,822           |
| console_command_kr | `Console` | 5,822 of 5,822           | 3,813 of 5,822           |

`Sura` and `Nachal` equal `PC` on 5,814 of 5,822 rows and are not
compiled. The client 3483 misses are rewritten texts: on client 1784 no
`PC` text and 4,259 `Console` texts hold a `{KeyBind:...}` placeholder,
on client 3483 most texts of both fields do (see Notes). The field names add
`_command`, after the client Lua: `panel_tooltip_skill.luac` reads a skill's
`getCommand()`, and `getConsoleCommand()` when `_ContentsGroup_isConsole` is
set.

## Notes

- The sheet keys are `<CLASS>_<number>` (`WARRIOR_01`, `BLADER_102`) plus
  `COMMON_*`, `GUILD_*` and a few others. The `PatternControl` column of the
  `SkillType_Table_New` sheet of the same workbook names the key of each
  skill, and `skilltype.dbss` holds these keys as `str16` text in its
  `config` block: 7,535 of the 7,663 hashes of client 3483 are the hash of
  such a text there.
- On client 3483, 5,726 `pc_command_kr` and 5,623 `console_command_kr`
  texts hold a `{KeyBind:...}` placeholder.
- Client 1784 also has `simplecommandtooltip.dbss` and its offset file
  (sheet `SimpleCommandTooltip_Table`, columns `skillKey` and `Tooltip`);
  client 3483 has neither.
- Client 1230, the first test client with the file, fits neither layout:
  its first row breaks at `pc_command_kr` (`+0x10` in the file).

## Open Questions

### What the Last u32 Holds

`unknown_console_command_kr_00` is `0` on every row of clients 1784 and
3483. The sheet has no fifth compiled column (`Sura` and `Nachal` do not
reach the file), and the 2016 PDB has no command tooltip struct to give
the member its name.
