# `detail_dialog.dbss` Format

## Purpose

Stores the NPC dialog trees: for each character and dialog index, the greeting text and the list of dialog options the player can pick (quest turn-ins, knowledge, exchanges, cutscenes, leases and more). Each option carries a condition script, a Korean title, the NPC's answer text and an action script that the client runs when the option is chosen.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes      | Records                                                                                            | Row bytes                     |
| ------ | -------------- | ------- | -------------------------- | ---------- | -------------------------------------------------------------------------------------------------- | ----------------------------- |
| 1      | 1784 and later | 3483    | `detail_dialog.dbss`       | 28,283,830 | 35,768 Option, 59,783 Dialog Record, 59,783 Record, 12,774 Conditional Greeting, 197 Greeting Line | 56 to 603,491, 469 on average |
| 1      | 1784 and later | 3483    | `detail_dialogoffset.dbss` | 717,416    | 59,783 Index Row                                                                                   | 12                            |

| Layout | File                       | Known                | Unknown            |
| ------ | -------------------------- | -------------------- | ------------------ |
| 1      | `detail_dialog.dbss`       | 26,853,601 B (94.9%) | 1,430,229 B (5.1%) |
| 1      | `detail_dialogoffset.dbss` | 717,416 B (100.0%)   | 0 B (0.0%)         |

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
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
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
| 1774   | No documented layout |
| 1771   | No documented layout |
| 1762   | No documented layout |
| 1759   | No documented layout |
| 1754   | No documented layout |
| 1749   | No documented layout |
| 1743   | No documented layout |
| 1737   | No documented layout |
| 1731   | No documented layout |
| 1725   | No documented layout |
| 1717   | No documented layout |
| 1710   | No documented layout |
| 1704   | No documented layout |
| 1698   | No documented layout |
| 1690   | No documented layout |
| 1685   | No documented layout |
| 1680   | No documented layout |
| 1674   | No documented layout |
| 1668   | No documented layout |
| 1659   | No documented layout |
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
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
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
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

| File                       | Required | Role                                                  |
| -------------------------- | -------- | ----------------------------------------------------- |
| `detail_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size    |
| `languagedata_*.loc`       | Optional | The dialog text in the user's language (type `39`, see Localization) and character names (type `6`) |

All multi-byte values are little-endian. [base_dialog.dbss](base_dialog_dbss.md) holds the same 59,776 keys in the same order with a short base record each (display name and short lines).

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file                   |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its `u32` key; see Record |

The records tile the file: every record starts 4 bytes after the previous one ends (the repeated key), the first at `8`, and the last ends at end of file.

Strings are a `u64` count followed by that many units: UTF-16LE for text and scripts, single-byte ASCII for the two internal names. There is no terminator.

### Record (variable: 4 bytes + dialog record)

| Offset  | Type          | Field      | Notes                                                       |
| ------- | ------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32           | key_prefix | Repeated copy of the record's `key`                         |
| `+0x04` | Dialog Record | dialog     | `size` bytes; the index row's `offset` points at this field |

### Dialog Record (variable: 54 bytes + text and lists)

| Offset                | Type                                    | Field              | Notes |
| --------------------- | --------------------------------------- | ------------------ | ----- |
| `+0x00`               | u32                                     | key                | Same as the index key |
| `+0x04`               | u16                                     | text_id            | LOC text ID of the greeting and its lines, see Localization; `1` on 3,193 records. Increases with the dialog index inside a character (`1233`, `1235`, `1238`, ...) |
| `+0x06`               | str8                                    | internal_name      | E.g. `Martina`, `IgorBartali1`, `Social_Low_Front_01`; empty on 7,071 records |
| `internal_name+0x00`  | str8                                    | unknown_name_2     | Empty on all but 325 records (`2,0` on 101, `Social_*` names on the rest) |
| `unknown_name_2+0x00` | str16                                   | greeting           | The NPC's opening line, Korean |
| `greeting+0x00`       | u32                                     | line_count         | Extra greeting lines that follow; `0` on all but 136 records |
| `greeting+0x04`       | Greeting Line[line_count]               | lines              | See Greeting Line |
| `lines+0x00`          | u32                                     | option_count       | `0` on 49,710 records; up to 1,522 (`0x0001AE99`, Dorin Morgrim) |
| `lines+0x04`          | Option[option_count]                    | options            | 36,276 options in all |
| `options+0x00`        | u32                                     | conditional_count  | Conditional greetings that follow; `0` on 55,202 records |
| `options+0x04`        | Conditional Greeting[conditional_count] | conditionals       | See Conditional Greeting |
| `conditionals+0x00`   | u64                                     | unknown_list_count | `2` on 57,387 records, `0` on 2,389 |
| `conditionals+0x08`   | u16[unknown_list_count]                 | unknown_list       | `[2, 0]` on 57,383 records |
| `unknown_list+0x00`   | u32                                     | unknown_end        | Always `0`; the record ends exactly here |

Every one of the 59,776 records in client 3458 walks with this layout and ends exactly at its index size.

### Greeting Line (variable: 9 bytes + text)

| Offset  | Type  | Field         | Notes |
| ------- | ----- | ------------- | ----- |
| `+0x00` | u8    | contents_type | The NPC function the line belongs to, a client `CppEnums.ContentsType` value (see Notes); `2` (`Contents_Shop`) on 120 of 197 lines (client 3458), otherwise `3` to `39` |
| `+0x01` | str16 | text          | Korean |

### Option (variable: 38 bytes + text)

| Offset           | Type  | Field              | Notes |
| ---------------- | ----- | ------------------ | ----- |
| `+0x00`          | str16 | condition          | Client script that must hold for the option to show, e.g. `!getitemcount(3001,0)>0;`; may be empty |
| `condition+0x00` | str16 | title              | Korean option label; many start with a bracketed category such as `[교환]` (exchange) or `[대여]` (lease) |
| `title+0x00`     | u32   | dialog_button_type | A client `CppEnums.DialogButtonType` value, `0` to `7`, or `99`; see Notes |
| `title+0x04`     | str16 | text               | The NPC's answer, Korean |
| `text+0x00`      | str16 | action             | Client script run when the option is picked, e.g. `buyItemByPoint(58010,0,1,5,3)`; may be empty |
| `action+0x00`    | u16   | text_id            | LOC text ID of the title and text, see Localization |

### Conditional Greeting (variable: 18 bytes + text)

| Offset           | Type  | Field     | Notes |
| ---------------- | ----- | --------- | ----- |
| `+0x00`          | str16 | condition | E.g. `clearquest(8541,3);` or `checkclass(20);` |
| `condition+0x00` | str16 | text      | Korean |
| `text+0x00`      | u16   | text_id   | LOC text ID of the text, see Localization |

### `detail_dialogoffset.dbss`

| Offset              | Type             | Field        | Notes                                        |
| ------------------- | ---------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                       |
| `+0x04`             | u32              | count        | Number of index rows; `59776` in client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                |
| `rows+0x00`         | String Table     | string_table | See String Table                             |
| `string_table+0x00` | u32              | rows_end     | End offset of the rows (`8 + 12 * count`)    |
| `string_table+0x04` | u32              | zero         | Always `0`                                   |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                             |
| ------- | ---- | ------ | ------------------------------------------------- |
| `+0x00` | u32  | key    | `dialog_index << 16 \| character_id`              |
| `+0x04` | u32  | offset | Byte offset of the record in `detail_dialog.dbss` |
| `+0x08` | u32  | size   | Record size in bytes                              |

### String Table (variable: 4 bytes + strings)

The 12-byte trailer of the offset file is an empty PABR string table, the end offset of the rows and `zero`.

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Localization

The Korean strings are localized in LOC type `39`, keyed by the record's `key`, a `text_id` and a field (`str_id1 = key`, `str_id2 = text_id`, `str_id3 = 0`, `str_id4 = field`):

| Field | String | Coverage in client 3458 |
| ----: | ------ | ----------------------- |
| `0` | `greeting`, with the record's `text_id` | 59,680 of 59,770 non-empty greetings |
| `1` | The greeting lines, with the record's `text_id`, packed in one string as `function>text;` per line, e.g. `shop>Excellent choice!;` | Records with lines |
| `2` | Option `title`, with the option's `text_id` | 36,117 of 36,276 options |
| `3` | Option `text`, with the option's `text_id` | 36,112 of 36,276 options |
| `4` | Conditional greeting `text`, with its `text_id` | 12,796 of 12,796 |

For Martina Finto (`0x00019C58`), field `0` of text ID `689` reads "It's so lonely here, all by myself... David doesn't...", and option text ID `42` field `2` reads `[Rent] Small Fence`. The function names of field `1` (`shop`, `repair`, `extract`, `weakenItem`, `talk`, `exchange`) name what `contents_type` picks: `2` `shop`, `4` `repair`, `19` `extract`, `33` `weakenItem`, `38` `talk`, `39` `exchange` and the others in Notes.

## Lease Options

A lease is an option whose `action` is `buyItemByPoint(item, 0, 1, 5, cost)`: the item key, `0`, `1`, `5` and the contribution point cost. Client 3458 has 184 lease options on 63 characters, all with `dialog_button_type` `0` (Normal) and titled `[대여] <item>` ("[Lease]"). `npcsimply.bss` repeats the first lease option of 58 of these characters (`lease_item_id`, `lease_cost`, `has_lease_condition`); the file lists all of them, such as the 84 Nesser gear leases of Sahazad Nesser (`45006`), the 25 Kaia weapons of Kanobas (`42152`) and the Small Fence of Wale (`40605`), who has no lease in `npcsimply.bss`. See `npcsimply_bss.md` for the cost check in game.

## Notes

- The key's low 16 bits are a character ID: 49,252 of the 59,776 records resolve to a LOC type `6` name, and 10,153 of the other 10,524 are shared social dialogs (`Social_Low_Front_01` and similar), many on low IDs such as `817` to `864`. The high 16 bits number the dialogs of one character from `0` up; the main NPC dialog is usually index `1` (`0x00019C58` Martina Finto, `0x00019C51` Igor Bartali). 3,788 of 4,569 characters have one record.
- In option and greeting conditions, the first argument of `checkequipitemgroup(group,min,max)` and `checkinventoryitemgroup(group,min,max)` is a group key in [itemequipgroup.bss](itemequipgroup_bss.md).
- The main dialog's `internal_name` is often the NPC's name plus a digit (`IgorBartali1`, `OttavioFerre1`).
- A greeting can be the tag `{GetRandomText(<name>)}`, which picks a line from the pool of that name in [dialogtext.dbss](dialogtext_dbss.md), e.g. `{GetRandomText(PEDU_47759_1)}`.
- `dialog_button_type` is the client's `CppEnums.DialogButtonType` (`global_define_cpp_enum.luac`), listed in order from `0`: `eDialogButton_Normal`, `_Knowledge`, `_Function`, `_CutScene`, `_Exchange`, `_ExceptExchange`, `_TimeAttack`, `_Sequence`, `_Count`. The data fits that order by the title prefixes and actions: `1` knowledge (지식, `pushknowledge`), `3` cutscenes and videos (회상, 이야기, `showCutScene`, `showVideo`), `4` and `5` exchanges (교환, `ExchangeItem...`), `6` time-limited quests (시간 제한, `resettimeattackquest`) and `7` sequences (`playsequence`). `0` (Normal, 21,252 options on client 3458) and `2` (Function, 4,185) mix quest turn-ins, returns and leases; `99` (options with an empty action) is not in the enum. The dialog list Lua (`panel_dialog_list_all_1.luac`) reads it as `_dialogButtonType`: it starts the cutscene for `eDialogButton_CutScene` and the sequence state for `eDialogButton_Sequence`, and `panel_dialog_exchangelist_all_2.luac` checks `eDialogButton_Exchange` and `eDialogButton_ExceptExchange` for the exchange list.
- `contents_type` is the client's `CppEnums.ContentsType`, listed in order from `0` (`Contents_Quest`, `Contents_NewQuest`, `Contents_Shop`, `Contents_Skill`, `Contents_Repair`, `Contents_Auction`, `Contents_Inn`, `Contents_Warehouse`, `Contents_IntimacyGame`, `Contents_Stable`, `Contents_Transfer`, ...). The values match the function names in LOC type `39` field `1` on 135 of the 136 records with lines (client 3458): `2` `shop`, `3` `skill`, `4` `repair`, `5` `auction`, `6` `inn`, `7` `warehouse`, `9` `stable`, `10` `transfer`, `19` `extract` (`Contents_Extract`), `33` `weakenItem` (`Contents_WeakenEnchant`), `38` `talk` and `39` `exchange`. The exception is Ambrosia (`0x0001A075`, character `41077`, the `<Stable Keeper>` in Glish), which stores `9` where LOC says `shop`. The stored value is right: in game she has Repair, Stable and Conversation buttons and no Shop, and her line's camera tag is `Ambrosia_Stable_Camera_01`, so the LOC function word is the error. The LOC string does not keep the record's line order: `0x0001B7B1` stores `39, 38, 33, 4, 2, 19` and LOC lists `shop`, `repair`, `extract`, `weakenItem`, `talk`, `exchange`.
- The whole file walks in about 0.5 s after decompression. The `CHARACTER_LEASES` lookup index (see `docs/handler.md`) collects every lease option per character from it for the `npcsimply.bss` Leases column.

## Open Questions

### What are `unknown_name_2` and `unknown_list`?

`unknown_name_2` is empty on all but 325 records; `unknown_list` is `[2, 0]` on almost every record. Neither has a visible counterpart yet.
