# `mentalcard.dbss` Format

## Purpose

Defines every knowledge entry (card). Each record holds the card ID, its owning knowledge category (theme), the amity conversation parameters and combo effect, the Korean source name, description and acquisition text, the icon path, and a world position. Used to build knowledge trees and place entries within the knowledge UI.

Field names `cardKey`, `themeKey`, `minFavor`, `maxFavor` and `interest` follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor); the layout below was re-checked against our files. The combo field names follow the client Lua getters (`getBuffType`, `getVariedValue`, `getValidTurn`, `getApplyTurn`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes     | Records          | Row bytes                    |
| ------ | -------------- | ------- | ----------------------- | --------- | ---------------- | ---------------------------- |
| 2      | 2098 and later | 3483    | `mentalcard.dbss`       | 6,461,923 | 12,604 Card      | 162 to 2,273, 513 on average |
| 2      | 2098 and later | 3483    | `mentalcardoffset.dbss` | 151,268   | 12,604 Index Row | 12                           |
| 1      | 1250 to 2089   | 2089    | `mentalcard.dbss`       | 4,291,476 | 8,576 Card       | 161 to 2,248, 500 on average |
| 1      | 1250 to 2089   | 2089    | `mentalcardoffset.dbss` | 102,932   | 8,576 Index Row  | 12                           |

| Layout | File                    | Known               | Unknown          |
| ------ | ----------------------- | ------------------- | ---------------- |
| 2      | `mentalcard.dbss`       | 6,178,315 B (95.6%) | 283,608 B (4.4%) |
| 2      | `mentalcardoffset.dbss` | 151,268 B (100.0%)  | 0 B (0.0%)       |
| 1      | `mentalcard.dbss`       | 4,105,848 B (95.7%) | 185,628 B (4.3%) |
| 1      | `mentalcardoffset.dbss` | 102,932 B (100.0%)  | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
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
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
| 1267   | Layout 1 |
| 1261   | Layout 1 |
| 1256   | Layout 1 |
| 1250   | Layout 1 |
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

| File                    | Required | Role                                                 |
| ----------------------- | -------- | ---------------------------------------------------- |
| `mentalcardoffset.dbss` | Required | Provides card ID, byte offset and size for each card |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type        | Field   | Notes                                           |
| ------- | ----------- | ------- | ----------------------------------------------- |
| `+0x00` | u32         | count   | Number of records; matches `mentalcardoffset`   |
| `+0x04` | Card[count] | records | Variable-size card records, back to back; see Card |

Strings are `i64` UTF-16 code-unit counts followed by that many UTF-16LE units, except the icon path, which is an `i64` byte count followed by ASCII.

### Card (variable: 97 bytes + strings and hashes)

A 33-byte header (`+0x00` to `+0x20`), then the body.

| Offset                | Type            | Field                     | Notes                                                                                   |
| --------------------- | --------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`               | u32             | card_id                   | Knowledge entry ID; equals the index key; LOC `str_type=34`, `str_id1`                  |
| `+0x04`               | u16             | theme_id                  | Owning category in `mentaltheme.dbss`; LOC `str_type=9`                                 |
| `+0x06`               | u8              | unknown_06                | Observed `0` or `1`; `1` on 172 cards, mostly story and adventure-log entries           |
| `+0x07`               | u8              | unknown_07                | Observed `0` or `1`; `1` on 373 cards, almost all under theme `10399` (None)            |
| `+0x08`               | f32             | min_favor                 | Amity conversation favor, lower bound; whole numbers `0` to `72`                        |
| `+0x0C`               | f32             | max_favor                 | Amity conversation favor, upper bound; whole numbers `0` to `100`                       |
| `+0x10`               | f32             | interest                  | Amity conversation interest; whole numbers `0` to `100`                                 |
| `+0x14`               | u8              | buff_type                 | Combo effect stat: `0` Favor, `1` Interest Level, `4` no combo (9,962 cards)            |
| `+0x15`               | f32             | varied_value              | Combo amount, unaligned; whole numbers `1` to `10` (one card `19`); `0` without a combo |
| `+0x19`               | u32             | valid_turn                | Combo duration in turns, `1` to `4`; `0` without a combo                                |
| `+0x1D`               | u32             | apply_turn                | Combo delay, `1` to `4`; the tooltip shows it plus one; `0` without a combo             |
| `+0x21`               | str16           | name_kr                   | Korean card name; English form is LOC `str_type=34`, `str_id4=0`                        |
| `name_kr+0x00`        | str16           | description_kr            | Korean description; English form is LOC `str_type=34`, `str_id4=1`                      |
| `description_kr+0x00` | u8              | unknown_description_kr_00 | `0` or `1`; `1` on 474 cards, mostly adventure-log themes                               |
| `description_kr+0x01` | u8              | unknown_description_kr_01 | Always `0`                                                                              |
| `description_kr+0x02` | u32             | unknown_description_kr_02 | `5` on 10,455 cards, `0` on 1,893, `1` to `4` on the rest                               |
| `description_kr+0x06` | str8            | icon_path                 | Always under `UI_Artwork/`, e.g. `UI_Artwork/IC_015879.dds`                             |
| `icon_path+0x00`      | str16           | acquisition_kr            | Korean "how to obtain" text; English form is LOC `str_type=34`, `str_id4=2`             |
| `acquisition_kr+0x00` | f32[3]          | position                  | World `x`, `y` (height), `z`; all zero on 9,356 cards                                   |
| `acquisition_kr+0x0C` | u8              | unknown_acquisition_kr_0c | `17` on 10,388 cards, otherwise `0` to `16`                                             |
| `acquisition_kr+0x0D` | u32             | unknown_acquisition_kr_0d | `0`, `1` or `3`                                                                         |
| `acquisition_kr+0x11` | u32             | hash_count                | `1` to `7`                                                                              |
| `acquisition_kr+0x15` | u32[hash_count] | unknown_hashes            | Hash-like values; 271 distinct, lists share prefixes between cards                      |
| `unknown_hashes+0x00` | bytes[5]        | unknown_end               | Always zero                                                                             |

Earlier versions of this doc called `unknown_06` `theme_flag_a`, `unknown_07` `theme_flag_b`, `unknown_description_kr_00` `body_flag`, `unknown_description_kr_01` `unknown_after_body_flag`, `unknown_description_kr_02` `body_value`, `unknown_acquisition_kr_0c` `tail_kind`, `unknown_acquisition_kr_0d` `tail_value` and `unknown_hashes` `hashes`.

The combo fields build the tooltip's "Next combo effect" line: "After `{apply_turn + 1}` turns, `{Favor | Interest Level}` will increase by `{varied_value}` for `{valid_turn}` turns", or "None" when `buff_type` is `4`. Confirmed in game on 2026-09-27 and 2026-09-28 against 19 cards, 10 with a combo and 9 without; see Confirmed Examples. No card stores a decrease or a `buff_type` other than `0`, `1` and `4`.

Every one of the 12,502 records parses with this layout and ends exactly at its index `size`. The same layout holds for the older test fixture (12,087 records) and for the 12,604 records after the 2026-09-27 update, which still tile the file from byte `4` to its end.

### `mentalcardoffset.dbss`

`PABR` index with 12-byte rows, the same shape as other `PABR` offset companions but with a u32 key.

| Offset              | Type             | Field        | Notes                                           |
| ------------------- | ---------------- | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32              | count        | Number of rows; `12,604` after the 2026-09-27 client update, `12,502` before it, `12,087` in the test fixture |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                   |
| `rows+0x00`         | String Table     | string_table | See String Table                                |
| `string_table+0x00` | u32              | rows_end     | End offset of the index rows (`150032`)         |
| `string_table+0x04` | u32              | zero         | Always `0`                                      |

Rows tile `mentalcard.dbss` exactly: the first record starts at `4`, each next record starts where the previous one ends, and the last ends at the file size.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | card_id     | Equals the `card_id` at the start of the record          |
| `+0x04` | u32  | data_offset | Absolute offset of the record in `mentalcard.dbss`       |
| `+0x08` | u32  | size        | Record size in bytes                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

On client 1784 `unknown_end` is 4 zero bytes, so each card is one byte
shorter; every other field is as in Layout 2.

### Card (variable: 96 bytes + strings and hashes)

| Offset                | Type            | Field                     | Notes                    |
| --------------------- | --------------- | ------------------------- | ------------------------ |
| `+0x00`               | u32             | card_id                   |                          |
| `+0x04`               | u16             | theme_id                  |                          |
| `+0x06`               | u8              | unknown_06                |                          |
| `+0x07`               | u8              | unknown_07                |                          |
| `+0x08`               | f32             | min_favor                 |                          |
| `+0x0C`               | f32             | max_favor                 |                          |
| `+0x10`               | f32             | interest                  |                          |
| `+0x14`               | u8              | buff_type                 |                          |
| `+0x15`               | f32             | varied_value              |                          |
| `+0x19`               | u32             | valid_turn                |                          |
| `+0x1D`               | u32             | apply_turn                |                          |
| `+0x21`               | str16           | name_kr                   |                          |
| `name_kr+0x00`        | str16           | description_kr            |                          |
| `description_kr+0x00` | u8              | unknown_description_kr_00 |                          |
| `description_kr+0x01` | u8              | unknown_description_kr_01 |                          |
| `description_kr+0x02` | u32             | unknown_description_kr_02 |                          |
| `description_kr+0x06` | str8            | icon_path                 |                          |
| `icon_path+0x00`      | str16           | acquisition_kr            |                          |
| `acquisition_kr+0x00` | f32[3]          | position                  |                          |
| `acquisition_kr+0x0C` | u8              | unknown_acquisition_kr_0c |                          |
| `acquisition_kr+0x0D` | u32             | unknown_acquisition_kr_0d |                          |
| `acquisition_kr+0x11` | u32             | hash_count                |                          |
| `acquisition_kr+0x15` | u32[hash_count] | unknown_hashes            |                          |
| `unknown_hashes+0x00` | bytes[4]        | unknown_end               | Always zero              |

## Confirmed Examples

Client 3458:

| card_id | LOC Name                | theme_id | min/max favor | interest | combo (type, value, valid, apply) | position                     |
| ------- | ----------------------- | -------- | ------------- | -------- | --------------------------------- | ---------------------------- |
| `15879` | Despair-Consumed Blader | `10087`  | `1` / `8`     | `45`     | Favor, `6`, `1`, `3`              | `0, 0, 0`                    |
| `3001`  | Velia                   | `5101`   | `45` / `49`   | `20`     | none                              | `152611, -7849, 290383`      |
| `15949` | Ynix Remnant            | `355`    | `35` / `37`   | `22`     | none                              | `1115590, 6865, 651513`      |

Combo text checked in game (Ornella on 2026-09-27, the rest through Oliviero on 2026-09-28). Every card's Attributes (Interest Level, Favor range) also equal the stored values exactly:

| card_id | Name | Stored combo (type, value, valid, apply) | Tooltip "Next combo effect" |
| ---: | --- | --- | --- |
| 102 | Ornella | Favor, 4, 3, 1 | After 2 turns, Favor will increase by 4 for 3 turns |
| 6059 | Al Rhundi's Journal | Favor, 1, 3, 2 | After 3 turns, Favor will increase by 1 for 3 turns |
| 6062 | Lazy Soldiers | Favor, 5, 1, 1 | After 2 turns, Favor will increase by 5 for 1 turns |
| 6063 | Cruhorn's Errand | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6075 | Kite Flying | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6080 | Laborers of the Quarry | Favor, 4, 1, 3 | After 4 turns, Favor will increase by 4 for 1 turns |
| 6090 | Melissa's Heart | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6092 | Secret Mission at the Abandoned Fort Site | Interest, 3, 1, 2 | After 3 turns, Interest Level will increase by 3 for 1 turns |
| 6106 | Broken Wagon | Favor, 8, 2, 1 | After 2 turns, Favor will increase by 8 for 2 turns |
| 6122 | Demibeast and Shai | Favor, 8, 1, 4 | After 5 turns, Favor will increase by 8 for 1 turns |

Stored as no combo and shown as "None": `4024` Lost Lamb, `6066` Heidel Church Belfry, `6079` Cannonball Master, `6086` Mine Imps Gone Berserk, `6087` Bloodstained Letter, `6093` Risk Factors Everywhere, `6095` Broken Cannon, `6096` Ornella's taste, `6105` Orcs and Spirits.

## Notes

- `card_id` → LOC `str_type=34`, `str_id1=card_id`; `str_id4` selects name (0), description (1) and acquisition text (2). 12,485 of 12,502 cards have an English name.
- `theme_id` → LOC `str_type=9`, `str_id1=theme_id` → knowledge category name. Read it as a u16: 524 cards have a non-zero byte at `+0x06` or `+0x07`, and reading `+0x04` as a u32 gives values such as `86040` (`0x15018`) that match no theme. With the u16 read, every card's theme lists that card in its `mentaltheme.dbss` entries.
- The three floats are whole numbers. `min_favor <= max_favor` on 12,484 of 12,604 cards in client 3458. In client 3458 the median favor range is 34 to 39 with interest 22 on cards without a combo, and 20 to 26 with interest 30 on the 2,642 cards with one.
- `acquisition_kr` is empty on 651 cards. Whenever LOC has `str_id4=2` for a card, the card also has a non-empty `acquisition_kr` (11,766 cards).
- `characterstatic.dbss` `getknowledge(<id>)` scripts grant 3,556 of the 12,604 cards on client 3458 (`npcsimply.bss` adds none). Most are granted by one NPC or by copies of one NPC with the same name; card `19` "NPC Pathfind Preventive Knowledge" is granted by 352 characters.
- The monsters, NPCs and gathering nodes in [knowledgelearning.dbss](knowledgelearning_dbss.md) table 0 add 506 character links on client 3458, 177 of them for cards no script grants (card `1643` "Rhyolite" from the Rhyolite node `11982`). Learned From merges both indexes, so card `4678` "Helm Tribe Chief Steel Nux" reads `Helm Tribe Chief, Steel Nux`. Its table 1 items fill Learned From Items (card `8579` "Gurnard" from the Gurnard fish `8279`).
- Non-zero positions are on 3,147 cards in client 3458, mostly NPC, barterer and node-manager entries. They use the same world frame as the `exploration.bss` node positions: town cards sit exactly on their node (Olvia `3032`, Calpheon `3177`, Keplan `3176`), and NPC cards sit where the NPC stands (Igor Bartali `18`, Islin Bartali `1` and Marsella `6` are all within about 35 m of the Velia node at `18588, 76647`).
- The index key is not a separate row identifier: it equals `card_id` on every row.
- How the conversation uses the values, per the [Black Desert Foundry, Story Exchange guide](https://www.blackdesertfoundry.com/story-exchange-guide/): a topic (card) has a fixed Interest Level and a Favor range. The NPC rolls its own Interest Level and Favor each conversation (from its `npcpersonality.dbss` ranges). The window then shows values relative to that NPC: Sparking Interest = topic interest / NPC interest (the chance of a positive reaction, always positive when the topic's is higher), and Interest gained = topic favor minus NPC favor. So the same card shows different numbers with different NPCs (that is how I see it in game, 2026-09-27), and a reading converts back to base values: `interest ≈ sparking × NPC interest`, `favor = interest gained + NPC favor`.
- The guide's example is close to, but not equal to, the stored values: topic Shiel shows Interest Level `11` and Favor `31`-`39`; card `11` stored `10` and `33`-`38` before the 2026-09-27 update. Its NPC, Lorenzo Murray (`40015`), shows Interest `32` and Favor `15`, both inside his stored ranges (`31`-`34`, `15`-`19`).
- The topic tooltip has two parts: **Attributes**, the card's own Interest Level and Favor range, and **Interaction Effect**, the values relative to the current NPC. For Lost Lamb with Oliviero it shows Attributes `23` / `33` ~ `37` and Interaction Effect Sparking Interest `23 (77%)`, Favor `2-6`, which fits the formulas above exactly with Oliviero at Interest Level `30` (23 / 30 = 77%) and Favor `31` (33 - 31 = 2, 37 - 31 = 6).
- The stored Attributes equal what the game shows. On 2026-09-27 I compared readings through Oliviero (`41091`) with the pre-update fixture and found gaps of up to 2 interest and a few favor, but those readings equal client 3458 exactly (for example Lost Lamb `23` / `33`-`37`, stored `21` / `34`-`36` before the update), and so do all 19 cards read on 2026-09-28. The update rerolls many cards: Shiel (`11`) is `14` / `34`-`38` in client 3458, `10` / `33`-`38` before it and `11` / `31`-`39` in the 2024 guide above, so older readings (the guide, the tracker dataset below) differ because they come from older patches. Oliviero's own Interest Level stayed at 30 to 31 over several conversations (stored `30`-`34`), and his Favor stayed at `31` (stored `31`-`35`).
- The tooltip is built by `PaGlobal_MentalGame_All:updateTooltipContext` in `luacscript/x64/widget/dialogue/panel_mentalgame_all_1.luac` (Lua 5.1 bytecode, decompiled with unluac). Attributes come from the live conversation card, not from this record: Interest Level is `card:getHit()`, Favor is `card:getMinDD()` ~ `card:getMaxDD()`. The Interaction Effect is `getHit() / npc:getCurrentDV() * 100` (clamped to 0-100) and `getMinDD() - npc:getCurrentPV()` / `getMaxDD() - npc:getCurrentPV()` (clamped at 0), so the NPC's interest is `CurrentDV` and its favor `CurrentPV`. The static record (`card:getStaticStatus()`, this file) is only used for the card key and the combo text: `getBuffType()`, `getApplyTurn()` (shown plus one, "after N turns"), `getValidTurn()` and `getVariedValue()`. The live values equal the stored `interest`, `min_favor` and `max_favor` on every card checked (see the previous note).
- Stored favor and interest in the pre-update fixture are close to, but mostly not equal to, the readings in an amity tracker dataset from an older patch. Against 62 cards, 2 match exactly, 55 are within 5 on every value, and seven differ by 6 to 44, for example `6161` Slum in the City (interest `59` stored, `15` seen) and `4333` Calpheon Giant Bee (`28` / `24`-`30` stored, `2` / `40`-`47` seen). The dataset does not say which NPC each reading came from. No NPC in the current `npcpersonality.dbss` has card `4333`'s theme (`10321`, Creatures of Northern Calpheon) as an interest group.

## Open Questions

### Unknown Body And Tail Fields

`unknown_06`, `unknown_07`, `unknown_description_kr_00`, `unknown_description_kr_02`, `unknown_acquisition_kr_0c`, `unknown_acquisition_kr_0d` and `unknown_hashes` are not decoded. `unknown_description_kr_02` 1 to 4 appears on single NPC cards such as the Sausan Scout, Sniper and Assassin, which suggests a small enum.

### Position Meaning

The position is a world point, but which one is not settled. Town and NPC cards sit on their node or NPC (see Notes). The Iliya Island card (`3030`, `159209, -7831, 292072`) sits about 22 m from the Iliya Island node (`1002`, `157320, 290939`), so it marks the island, the exploration source in its acquisition text, and not Igor Bartali in Velia, its amity source. The Velia card (`3001`, `152611, -7849, 290383`) is the odd one: it also sits on Iliya Island, about 47 m from that node, instead of on the Velia node. Among its sources, only Diega (Amity) is on Iliya Island, but Diega's own card (`387`) sits about 72 m from it.
