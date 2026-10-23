# `nakmessagerenewelss.bss` Format

## Purpose

The look of every screen-wide message (NAK) that `Panel_NakMessage_Renewel`
shows, one row per message type (306 on client 3482): entering a Safe Zone,
a guild war start, a world boss spawn, a learned skill. Per type the file
holds the display time, the main and the optional sub background texture
with their grid and offsets, up to four text lines with font, colour and
chat flag, the UI effects, the system sounds and the item icon offsets. The
Lua `FromClient_NakMessageRenewelRequest` passes the type to
`ToClient_GetNakMessageRenewelData()` and reads the named fields through
the getters listed in [Field Names](#field-names); the strings it shows come
with the event (`mainStr`, `subStr`), and no getter reads the row's text.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records                                                   | Row bytes                 |
| ------ | -------------- | ------- | ------------------------- | ------- | --------------------------------------------------------- | ------------------------- |
| 4      | 2923 and later | 3482    | `nakmessagerenewelss.bss` | 170,779 | 612 Background, 1,224 Text, 306 Row, 99 Effect, 152 Sound | 33 to 354, 69 on average  |
| 3      | 3381 to 3396   | 3396    | `nakmessagerenewelss.bss` | 144,940 | 602 Background, 602 Text, 301 Row, 97 Effect, 150 Sound   | 85 to 138, 102 on average |
| 2      | 2987 to 3373   | 3373    | `nakmessagerenewelss.bss` | 140,183 | 590 Background, 590 Text, 295 Row, 87 Effect, 144 Sound   | 85 to 138, 102 on average |
| 1      | 2970 to 2978   | 2978    | `nakmessagerenewelss.bss` | 93,443  | 582 Background, 582 Text, 291 Row, 83 Effect, 141 Sound   | 20 to 73, 37 on average   |

| Layout | File                      | Known             | Unknown         |
| ------ | ------------------------- | ----------------- | --------------- |
| 4      | `nakmessagerenewelss.bss` | 160,069 B (93.7%) | 10,710 B (6.3%) |
| 3      | `nakmessagerenewelss.bss` | 134,405 B (92.7%) | 10,535 B (7.3%) |
| 2      | `nakmessagerenewelss.bss` | 130,153 B (92.8%) | 10,030 B (7.2%) |
| 1      | `nakmessagerenewelss.bss` | 90,533 B (96.9%)  | 2,910 B (3.1%)  |

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
| 3396   | Layout 3 |
| 3387   | Layout 3 |
| 3381   | Layout 3 |
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
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 4 |
| 2951   | Layout 4 |
| 2942   | Layout 4 |
| 2935   | Layout 4 |
| 2932   | Layout 4 |
| 2923   | Layout 4 |
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

| File                  | Required | Role                                                                      |
| --------------------- | -------- | ------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | The text lines: LOC type 132, `str_id1` = `nak_message_type`, `str_id4` = line (`0` main, `1` sub, `2` and `3` the extra lines) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

No `PABR` magic and no string table.

| Offset  | Type       | Field | Notes                                                        |
| ------- | ---------- | ----- | ------------------------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `306` on client 3482                         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row                 |

### Row (variable: 66 bytes + backgrounds, texts, effects and sounds)

On client 3482 the rows are in key order and `nak_message_type` equals the
row index on all 306 rows. Each `is_exist_*` flag is `1` exactly on the rows
whose part holds data, on all 306 rows of client 3482.

| Offset                 | Type                | Field               | Notes                                                                    |
| ---------------------- | ------------------- | ------------------- | ------------------------------------------------------------------------ |
| `+0x00`                | u8                  | is_exist_sub_bg     | `1` when `sub_bg` has a texture; 32 rows                                 |
| `+0x01`                | u8                  | is_exist_sub_text   | `1` when `sub_text` has text; 188 rows                                   |
| `+0x02`                | u8                  | is_exist_sub_text2  | `1` when `sub_text2` has text; 1 row                                     |
| `+0x03`                | u8                  | is_exist_sub_text3  | `1` when `sub_text3` has text; 1 row                                     |
| `+0x04`                | u8                  | is_exist_effect_bg  | `1` when `effects` is not empty; 72 rows                                 |
| `+0x05`                | u8                  | is_exist_sound_list | `1` when `sounds` is not empty; 146 rows                                 |
| `+0x06`                | u8                  | is_exist_icon       | `1` on the 55 rows whose icon fields differ from `0` and `42.0`          |
| `+0x07`                | u32                 | nak_message_type    | Row key, the `__eNakMessage_*` value the Lua passes                      |
| `+0x0B`                | u16                 | unknown_0b          | `1` on 69 rows, `65535` on 66, `100` on 46, `3` on 44, `200` on 38, `300` on 22, also `2`, `4`, `5`, `10`, `400` |
| `+0x0D`                | f32                 | ani_time            | Seconds the message stays, `_AniTime`; `5.0` on 152 rows, `1.8` to `33.0` |
| `+0x11`                | u8                  | unknown_11          | `1` on 3 rows (`44`, `149`, `154`), else `0` |
| `+0x12`                | u8                  | unknown_12          | `7` on the 7 rows `9` to `15` (territory war tents), else `0`            |
| `+0x13`                | u8                  | unknown_13          | `0` on every row                                                         |
| `+0x14`                | u8                  | unknown_14          | `1` on 12 rows, else `0`                                                 |
| `+0x15`                | u8                  | unknown_15          | `1` on 22 rows (`0`, `1`, `92`, `93`, `189` to `205`, `270`), else `0`   |
| `+0x16`                | u32                 | unknown_16          | `1` on every row                                                         |
| `+0x1A`                | u32                 | contents_group_hash | Contents group key as the client's string hash; see [Contents Groups](#contents-groups) |
| `+0x1E`                | Background          | main_bg             | See Background                                                           |
| `main_bg+0x00`         | Background          | sub_bg              | Empty texture on the rows without `is_exist_sub_bg`                      |
| `sub_bg+0x00`          | Text                | main_text           | See Text; text on every row                                              |
| `main_text+0x00`       | Text                | sub_text            | Empty strings on the rows without `is_exist_sub_text`                    |
| `sub_text+0x00`        | Text                | sub_text2           | Text on row `297` only                                                   |
| `sub_text2+0x00`       | Text                | sub_text3           | Text on row `297` only                                                   |
| `sub_text3+0x00`       | u32                 | effect_count        | `getEffectFileCount()`; `0` to `4`                                       |
| `sub_text3+0x04`       | Effect[effect_count]| effects             | See Effect                                                               |
| `effects+0x00`         | u32                 | sound_count         | `getSoundListCount()`; `0` to `2`                                        |
| `effects+0x04`         | Sound[sound_count]  | sounds              | See Sound                                                                |
| `sounds+0x00`          | f32                 | icon_span_y         | `getIconSpanY()`: vertical offset of the item icon; `0.0` on 251 rows, `-30.0` to `118.0` |
| `sounds+0x04`          | bytes[8]            | unknown_sounds_04   | All zero on every row                                                    |
| `sounds+0x0C`          | f32[2]              | unknown_sounds_0c   | `42.0, 42.0` on 303 rows; `144.0, 144.0` (`82`), `308.0, 280.0` (`83`), `360.0, 360.0` (`264`) |
| `sounds+0x14`          | f32[2]              | unknown_sounds_14   | `42.0, 42.0` on 297 rows; `44.0` to `100.0` (both the same) on 9         |

### Background (variable: 85 bytes + texture ID)

| Offset            | Type   | Field      | Notes                                                                              |
| ----------------- | ------ | ---------- | ---------------------------------------------------------------------------------- |
| `+0x00`           | str8   | texture_id | UI texture ID, `getMainBgTID()` / `getSubBgTID()` (`NakMessage_NakBG_Safety_01`, `Combine_Etc_JinWorldBoss_Nak_BG`) |
| `texture_id+0x00` | u8     | use_grid   | `getMainBgUseGrid()`: `1` draws the texture as a nine-slice grid; 11 main backgrounds, no sub background |
| `texture_id+0x01` | f32[4] | grid_pos_x | `getMainBgGridPosX()`: the four x positions of the grid lines; `0.0` where `use_grid` is `0` |
| `texture_id+0x11` | f32[4] | grid_pos_y | `getMainBgGridPosY()`: the four y positions                                        |
| `texture_id+0x21` | f32[4] | grid_uv_x  | `getMainBgGridUVX()`: the four x texture coordinates                               |
| `texture_id+0x31` | f32[4] | grid_uv_y  | `getMainBgGridUVY()`: the four y texture coordinates                               |
| `texture_id+0x41` | f32    | span_y     | `getMainBgSpanY()`: vertical offset in pixels; `0.0` on 256 main backgrounds, `-110.0` to `70.0` |
| `texture_id+0x45` | f32[2] | size       | `getMainBgSize()`: width and height; `0.0, 0.0` on 288 main backgrounds and 294 sub backgrounds |

The Lua sets the control to `size` when `getMainBgUseFixedSize()` is true,
else to the texture's size. The file has no byte left for that flag; on
client 3482 the last `grid_pos_x` and `grid_pos_y` value equals `size` on
every grid background.

### Text (variable: 33 bytes + text, font and color)

| Offset         | Type  | Field     | Notes                                                                                |
| -------------- | ----- | --------- | ------------------------------------------------------------------------------------ |
| `+0x00`        | str16 | text_kr   | Korean text with `<PAColor>` tags and `{name}` placeholders; LOC type 132 holds the other languages |
| `text_kr+0x00` | str8  | font      | Font name, `getMainTextFont()` (`RealFont_25_Shadhow` on 266 main texts); empty on the lines without text |
| `font+0x00`    | str8  | color     | ARGB colour as hex text, `getMainTextColor()` (`ffdeff6d`, `FFFFEF82`)              |
| `color+0x00`   | u8    | send_chat | `getMainTextSendChat()` / `getSubTextSendChat()`: `1` also posts the line to the system chat; 281 main and 177 sub texts |
| `color+0x01`   | f32   | span_x    | `getMainTextSpanX()`: horizontal offset; `0.0` on every main and sub text, `-55.0` and `55.0` on the extra lines of row `297` |
| `color+0x05`   | f32   | span_y    | `getMainTextSpanY()`: vertical offset                                                |

### Effect (variable: 13 bytes + effect name)

| Offset             | Type  | Field       | Notes                                                                   |
| ------------------ | ----- | ----------- | ----------------------------------------------------------------------- |
| `+0x00`            | str8  | effect_name | `getEffectBgFilePath(index)`: UI effect name (`fui_skillawakenboom_red`, `UI_SiegeWarfare_Win_Red`) |
| `effect_name+0x00` | u8    | loop        | `_loop` of `getEffectBg(index)`; `0` on all 99 effects                  |
| `effect_name+0x01` | i16   | pos_x       | `_posX`: horizontal offset                                              |
| `effect_name+0x03` | i16   | pos_y       | `_posY`: vertical offset                                                |

### Sound (5 bytes)

| Offset  | Type | Field         | Notes                                                                          |
| ------- | ---- | ------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | audio_index   | First argument of `audioPostEvent_SystemUi()`, `_audioIndex`                   |
| `+0x02` | u16  | audio_index_b | Second argument, `_audioIndexB`                                                |
| `+0x04` | u8   | console_play  | `_consolePlay`: `1` also plays it on Xbox; `1` on all 152 sounds               |

## Layout 3

The two extra text lines and their flags are not there yet, and a text line
has no `span_x`.

### Row (variable: 64 bytes + backgrounds, texts, effects and sounds)

| Offset           | Type                 | Field               | Notes                         |
| ---------------- | -------------------- | ------------------- | ----------------------------- |
| `+0x00`          | u8                   | is_exist_sub_bg     |                               |
| `+0x01`          | u8                   | is_exist_sub_text   |                               |
| `+0x02`          | u8                   | is_exist_effect_bg  |                               |
| `+0x03`          | u8                   | is_exist_sound_list |                               |
| `+0x04`          | u8                   | is_exist_icon       |                               |
| `+0x05`          | u32                  | nak_message_type    |                               |
| `+0x09`          | u16                  | unknown_0b          |                               |
| `+0x0B`          | f32                  | ani_time            |                               |
| `+0x0F`          | u8                   | unknown_11          |                               |
| `+0x10`          | u8                   | unknown_12          |                               |
| `+0x11`          | u8                   | unknown_13          |                               |
| `+0x12`          | u8                   | unknown_14          |                               |
| `+0x13`          | u8                   | unknown_15          |                               |
| `+0x14`          | u32                  | unknown_16          |                               |
| `+0x18`          | u32                  | contents_group_hash |                               |
| `+0x1C`          | Background           | main_bg             |                               |
| `main_bg+0x00`   | Background           | sub_bg              |                               |
| `sub_bg+0x00`    | Text                 | main_text           |                               |
| `main_text+0x00` | Text                 | sub_text            |                               |
| `sub_text+0x00`  | u32                  | effect_count        |                               |
| `sub_text+0x04`  | Effect[effect_count] | effects             |                               |
| `effects+0x00`   | u32                  | sound_count         |                               |
| `effects+0x04`   | Sound[sound_count]   | sounds              |                               |
| `sounds+0x00`    | f32                  | icon_span_y         |                               |
| `sounds+0x04`    | bytes[8]             | unknown_sounds_04   |                               |
| `sounds+0x0C`    | f32[2]               | unknown_sounds_0c   |                               |
| `sounds+0x14`    | f32[2]               | unknown_sounds_14   |                               |

On client 3396 the five flags match their parts on all 301 rows.

### Text (variable: 29 bytes + text, font and color)

| Offset         | Type  | Field     | Notes |
| -------------- | ----- | --------- | ----- |
| `+0x00`        | str16 | text_kr   |       |
| `text_kr+0x00` | str8  | font      |       |
| `font+0x00`    | str8  | color     |       |
| `color+0x00`   | u8    | send_chat |       |
| `color+0x01`   | f32   | span_y    |       |

## Layout 2

The row has one u8 fewer between `unknown_11` and `unknown_14`. On client
3482 `unknown_13` is `0` on every row and `unknown_12` is `7` on 7 rows;
the byte here is `0` on every row of client 3373, so which of the two came
later is not known. The tables of Layouts 1 and 2 name it `unknown_12`.

### Row (variable: 63 bytes + backgrounds, texts, effects and sounds)

| Offset           | Type                 | Field               | Notes                         |
| ---------------- | -------------------- | ------------------- | ----------------------------- |
| `+0x00`          | u8                   | is_exist_sub_bg     |                               |
| `+0x01`          | u8                   | is_exist_sub_text   |                               |
| `+0x02`          | u8                   | is_exist_effect_bg  |                               |
| `+0x03`          | u8                   | is_exist_sound_list |                               |
| `+0x04`          | u8                   | is_exist_icon       |                               |
| `+0x05`          | u32                  | nak_message_type    |                               |
| `+0x09`          | u16                  | unknown_0b          |                               |
| `+0x0B`          | f32                  | ani_time            |                               |
| `+0x0F`          | u8                   | unknown_11          |                               |
| `+0x10`          | u8                   | unknown_12          | See the text above            |
| `+0x11`          | u8                   | unknown_14          |                               |
| `+0x12`          | u8                   | unknown_15          |                               |
| `+0x13`          | u32                  | unknown_16          |                               |
| `+0x17`          | u32                  | contents_group_hash |                               |
| `+0x1B`          | Background           | main_bg             |                               |
| `main_bg+0x00`   | Background           | sub_bg              |                               |
| `sub_bg+0x00`    | Text                 | main_text           |                               |
| `main_text+0x00` | Text                 | sub_text            |                               |
| `sub_text+0x00`  | u32                  | effect_count        |                               |
| `sub_text+0x04`  | Effect[effect_count] | effects             |                               |
| `effects+0x00`   | u32                  | sound_count         |                               |
| `effects+0x04`   | Sound[sound_count]   | sounds              |                               |
| `sounds+0x00`    | f32                  | icon_span_y         |                               |
| `sounds+0x04`    | bytes[8]             | unknown_sounds_04   |                               |
| `sounds+0x0C`    | f32[2]               | unknown_sounds_0c   |                               |
| `sounds+0x14`    | f32[2]               | unknown_sounds_14   |                               |

On client 3373 the five flags match their parts on all 295 rows.

## Layout 1

A background has no grid yet, and the icon has its offset only.

### Row (variable: 39 bytes + backgrounds, texts, effects and sounds)

| Offset           | Type                 | Field               | Notes                         |
| ---------------- | -------------------- | ------------------- | ----------------------------- |
| `+0x00`          | u8                   | is_exist_sub_bg     |                               |
| `+0x01`          | u8                   | is_exist_sub_text   |                               |
| `+0x02`          | u8                   | is_exist_effect_bg  |                               |
| `+0x03`          | u8                   | is_exist_sound_list |                               |
| `+0x04`          | u8                   | is_exist_icon       |                               |
| `+0x05`          | u32                  | nak_message_type    |                               |
| `+0x09`          | u16                  | unknown_0b          |                               |
| `+0x0B`          | f32                  | ani_time            |                               |
| `+0x0F`          | u8                   | unknown_11          |                               |
| `+0x10`          | u8                   | unknown_12          | See the text above            |
| `+0x11`          | u8                   | unknown_14          |                               |
| `+0x12`          | u8                   | unknown_15          |                               |
| `+0x13`          | u32                  | unknown_16          |                               |
| `+0x17`          | u32                  | contents_group_hash |                               |
| `+0x1B`          | Background           | main_bg             |                               |
| `main_bg+0x00`   | Background           | sub_bg              |                               |
| `sub_bg+0x00`    | Text                 | main_text           |                               |
| `main_text+0x00` | Text                 | sub_text            |                               |
| `sub_text+0x00`  | u32                  | effect_count        |                               |
| `sub_text+0x04`  | Effect[effect_count] | effects             |                               |
| `effects+0x00`   | u32                  | sound_count         |                               |
| `effects+0x04`   | Sound[sound_count]   | sounds              |                               |
| `sounds+0x00`    | f32                  | icon_span_y         |                               |

On client 2970 the five flags match their parts on all 291 rows.

### Background (variable: 20 bytes + texture ID)

| Offset            | Type   | Field      | Notes |
| ----------------- | ------ | ---------- | ----- |
| `+0x00`           | str8   | texture_id |       |
| `texture_id+0x00` | f32    | span_y     |       |
| `texture_id+0x04` | f32[2] | size       |       |

## Field Names

Every named field is a getter or member that `nakmessage_renewel.luac`
(client 3482) reads from the row `ToClient_GetNakMessageRenewelData()`
returns. The `is_exist_*` names are the
Lua members `_isExistSubBg` to `_isExistIcon`; the file stores the icon
flag after the sound flag, and each flag matches its part on all 306 rows.
The Background getters are named for the main background; the sub
background has the same getters with `SubBg`, and the Text getters exist
as `getMainText*`, `getSubText*`, `getSubText*2` and `getSubText*3`. In the
Text block the strings are the font and colour (`ToClient_getFontWrapper`,
`tonumber(color, 16)`) and the two floats the spans, so the one byte left is
the chat flag, the only other text getter. No reference sheet or server
table has this table.

## Contents Groups

`contents_group_hash` is the client's string hash (`_common/string_hash.py`
`key_hash`) of a contents group key written in decimal, as in
[`characterstatic.dbss`](characterstatic_dbss.md#contents-groups). On
client 3482, 274 rows hold the hash of `0`, and the others are `1880` (11
Rose War rows, `107` to `117`), `1177` (the guild war rows `295` to `301`),
`2137`, `2180`, `1921`, `4034` and `898`.

## Notes

- On client 3482 LOC type 132 has a text for every main and sub line whose
  `text_kr` is not blank, and for the two extra lines of row `297`.
- The Lua handles two types on top of the row: `__eNakMessage_RichMerchantRing`
  and `__eNakMessage_PanOkSeonPersonal` add NPC lines from the `GAME` sheet
  (`LUA_NAKMESSAGE_SHAKATU_MSG_1` and on) and set their own display time.
  The two rows with `ani_time` `33.0`, `149` and `154`, have the
  `Combine_ETC_Nak_MerchantRing_BG` and `Combine_ETC_Nak_Panokseon_BG`
  backgrounds.
- `__eNakMessage_LearnMentalCard` shows the knowledge level icon next to the
  sub text; the level comes from the event, not from the row.
- On client 3482, 70 rows store the text `{empty}` as their main text, in
  `text_kr` and in LOC alike, and rows `285` to `288` store one space as
  their sub text.
- Clients 2923 to 2959 hold the file with a count of `0`, which every layout
  reads; that is why the newest layout's client range starts there.
- [`itemnakmessage.dbss`](itemnakmessage_dbss.md) is a different table: the
  rare item lines as `stringtable.bss` keys. It shares no field with this
  one.

## Open Questions

### Display Position, Chat Type and Only Chat

The Lua also calls `getNakMessagePosition()` (`__eNakPosition_Top`,
`__eNakPosition_Center`, else the top edge), `getChatSystemType()` and
reads `_onlyChat`. The fields left are `unknown_0b` (u16, `1` to `400` and
`65535`), the u8 fields `unknown_11`, `unknown_12` (`7` on the
territory war tent rows), `unknown_13`, `unknown_14` and `unknown_15`,
and the u32 `unknown_16` (`1` on every row). Which of them is which needs the client's enum values
for `__eNakPosition_*` and the chat system types.

### Icon Size

`getIconSize()` is the only icon getter besides `getIconSpanY()`, and both
`unknown_sounds_0c` and `unknown_sounds_14` hold `42.0, 42.0` (the
`Static_ItemIcon` size in `nakmessage_renewel.xml`) on most rows. Rows `82`
and `83` (main texts `{servantTier} {price}` and `{workerName} {price}`) set the first pair to
`144.0, 144.0` and `308.0, 280.0`; the rows `285` to `288` set the second to `55.0` to `78.0`. Which pair
is the icon size, and what the other one sizes, is open. The 8 zero bytes
before them are not named either.
