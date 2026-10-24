# `yachtgameboardinfo.bss` Format

## Purpose

The game boards (modes) of a Yar! match between two players, picked in the
invite window (`panel_window_minigame_yachtdice_invite_1.luac`). Each row is
one board: the [`yachthandrank.bss`](yachthandrank_bss.md) hand ranks it
plays, how many rolls a turn allows, its difficulty level (stars), its
Korean description, its icon textures and whether it uses matchmaking. The
plain PABR file holds the rows, then the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | ----------------------- |
| 2      | 2855 and later | 3483    | `yachtgameboardinfo.bss` | 2,523 | 9 Row   | 54 to 90, 68 on average |
| 1      | 1762 to 2849   | 2849    | `yachtgameboardinfo.bss` | 2,220 | 8 Row   | 53 to 89, 64 on average |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 2      | `yachtgameboardinfo.bss` | 2,523 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtgameboardinfo.bss` | 2,220 B (100.0%) | 0 B (0.0%) |

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
| 1759   | No documented layout |
| 1754   | No documented layout |
| 1749   | No documented layout |
| 1743   | No documented layout |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No file              |
| 1276   | No file              |
| 1267   | No file              |
| 1261   | No file              |
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

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachthandrank.bss`   | Optional | Korean hand rank names, where LOC has none                                               |
| `languagedata_en.loc` | Optional | Board descriptions (LOC type 109, `str_id1=game_board_key`), hand rank names (LOC type 105) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row    |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). Walking `count` rows ends exactly at
`string_table_start`.

### Row (variable: 30 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                                              |
| --------------------- | -------------------- | ------------------ | ------------------------------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key, LOC type 109 `str_id1`                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                                               |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`, in sheet order (not always ascending) |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn; `3` or `4` (client 3474)                           |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description                       |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Card01`) |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Big_Card01`) |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars; `1` to `5`                   |
| `hand_rank_keys+0x11` | u8                   | is_use_matching    | `1` when the board offers matchmaking against a stranger           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (27 on client 3474)        |
| `+0x04` | pstr[string_count] | strings      | Per row its description (UTF-16) and two texture IDs (UTF-8) |

## Layout 1

Client 1784 rows have no `is_use_matching`.

### Row (variable: 29 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                      |
| --------------------- | -------------------- | ------------------ | ------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                       |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`                |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn                             |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars       |

## Game Boards

On client 3474 the file holds 9 rows. The descriptions are the first
sentence of the LOC type 109 English text.

| Key | Level | Hand ranks               | Rolls | Matchmaking | Description                                     |
| --- | ----- | ------------------------ | ----- | ----------- | ----------------------------------------------- |
| 1   | 1     | 1 to 6, 15               | 3     | No          | The most basic mode.                            |
| 2   | 2     | 1, 3, 5, 8, 14, 15       | 3     | No          | A mode with only odd-numbered hands.            |
| 3   | 2     | 2, 4, 6, 7, 9, 13, 15    | 3     | No          | A mode with only even-numbered hands.           |
| 4   | 3     | 1 to 6, 10, 11, 15       | 3     | No          | A mode with numbered hands, Double Trouble, and Den of Wolves. |
| 5   | 3     | 1 to 3, 10, 11, 13 to 15 | 3     | No          | A mode that values low-numbered hands.          |
| 6   | 4     | 1 to 6, 13 to 15         | 4     | No          | A mode with numbered hands, Broken Arrow, and Straight Shot. |
| 7   | 4     | 7 to 11, 13 to 15, 12    | 4     | No          | A mode without single-numbered hands.           |
| 8   | 5     | 1 to 11, 13 to 15, 12    | 4     | No          | A mode with all Yar! hands available.           |
| 9   | 5     | 1 to 11, 13 to 15, 12    | 4     | Yes         | A mode with all Yar! hands available.           |

Rows 7 to 9 list hand rank `12` last. Row 9 differs from row 8 only in
`is_use_matching` and its second description line, "Select this when you
want to battle a stranger."

## Field Names

The `PVP_GameBoard` sheet of a private server's `datasheet_minigame.xlsm`
on client 1784 has the columns `GameBoardKey` (`game_board_key`),
`HandRankKeyList` (`hand_rank_keys`, one comma-separated list),
`RollCountMax` (`roll_count_max`), `~Name`, `Level` (`level`), `~Desc`,
`IconTexture` and `BigTexture`. Its 8 rows match rows 1 to 8 of clients
1784 and 3474 in every named column and in the description and texture
strings, hand rank order included. `~Name` holds the level as star text
(`★★<PAColor0xff6c6c6c>☆☆☆<PAOldColor>`) and is not in the file. The file
writes `~Desc` before the textures and `Level` after them.

The client Lua (`panel_window_minigame_yachtdice_invite_1.luac`) reads a
board through `ToClient_getYachtGameBoardStaticStatusWrapperByIndex()` and
`...ByKey()`: `getKey()`, `getLevel()` (the star count), `getDesc()`,
`getHandRankCount()`, `isHaveHandRankKey()`, `getBigTextureId()`,
`getIconNormalTextureId()`, `getIconOverTextureId()` and
`getIconClickTextureId()` (three states of the board button, from the one
`icon_texture_index` string), and `isUseMatching()`, which shows the
matchmaking button.

## Notes

- Client 1784 has rows 1 to 8 and no `is_use_matching`. Client 3474 adds
  row 9 and the byte; row 9 is the only row with `1`.
