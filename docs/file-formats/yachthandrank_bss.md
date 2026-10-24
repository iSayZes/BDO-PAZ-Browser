# `yachthandrank.bss` Format

## Purpose

The hand ranks (scoring combinations) of Yar!, the card and dice minigame
of [`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md). Each row is one hand
rank: which cards it checks (an eye value, a count of equal cards, a
straight length, two pair or full house), whether it scores a fixed number
of points or the sum of the matching cards, and its icon texture, Korean
name and Korean description. `yachtnpcdiceinfo.bss` and
[`yachtgameboardinfo.bss`](yachtgameboardinfo_bss.md) list hand ranks by
key, and [`yachtautobubbletextinfo.bss`](yachtautobubbletextinfo_bss.md)
keys some lines to one. The plain PABR file holds the rows, then the string
table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1754 and later | 3483    | `yachthandrank.bss` | 2,951 | 15 Row  | 49        |

| Layout | File                | Known           | Unknown      |
| ------ | ------------------- | --------------- | ------------ |
| 1      | `yachthandrank.bss` | 2,696 B (91.4%) | 255 B (8.6%) |

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

| File                  | Required | Role                                                                                               |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Hand rank names (LOC type 105, `str_id1=hand_rank_key`, `str_id4=0`) and descriptions (`str_id4=1`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Fixed-size rows, back to back; see Row       |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). `count` rows of 49 bytes end exactly at
`string_table_start`.

### Row (49 bytes)

| Offset  | Type     | Field              | Notes                                                                      |
| ------- | -------- | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32      | hand_rank_key      | Unique row key, LOC type 105 `str_id1`                                     |
| `+0x04` | bytes[9] | unknown_04         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x0D` | u32      | unknown_0d         | `1` on every row (clients 1784 and 3474)                                   |
| `+0x11` | bytes[4] | unknown_11         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x15` | u8       | target_eye         | Eye value the hand counts (`1` to `6`); `0` checks no eye                  |
| `+0x16` | u32      | target_count       | Number of equal cards the hand needs (`2` to `5`); `0` for none            |
| `+0x1A` | u32      | straight_count     | Length of the straight the hand needs (`4` or `5`); `0` for none           |
| `+0x1E` | u8       | is_full_house      | `1` on the full house hand (key 11)                                        |
| `+0x1F` | u8       | is_two_pair        | `1` on the two pair hand (key 10)                                          |
| `+0x20` | u32      | made_point         | Fixed points the hand scores; `0` when it scores the card sum              |
| `+0x24` | u8       | is_sum_point       | `1` when the hand scores the sum of its cards                              |
| `+0x25` | u32      | icon_texture_index | String table index of the icon's texture ID (`Combine_Etc_Minigame_Yatzee_Icon_Ones`) |
| `+0x29` | u32      | name_kr_index      | String table index of the Korean name                                      |
| `+0x2D` | u32      | desc_kr_index      | String table index of the Korean description                               |

No field is padded, so the u32 fields after `target_eye` are not 4-byte
aligned.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (45 on client 3474)     |
| `+0x04` | pstr[string_count] | strings      | Per row its icon texture ID (UTF-8), name and description (UTF-16) |

## Hand Ranks

On client 3474 the file holds 15 rows. Names are the LOC type 105 English text.

| Key | Name           | Checks                         | Points       |
| --- | -------------- | ------------------------------ | ------------ |
| 1   | Bit o' Ones    | Eye 1                          | Sum          |
| 2   | Bunch o' Twos  | Eye 2                          | Sum          |
| 3   | Lump o' Threes | Eye 3                          | Sum          |
| 4   | Nest o' Fours  | Eye 4                          | Sum          |
| 5   | Clump o' Fives | Eye 5                          | Sum          |
| 6   | Stack o' Sixes | Eye 6                          | Sum          |
| 7   | Mates          | 2 equal cards                  | Sum          |
| 8   | Peak           | 3 equal cards                  | Sum          |
| 9   | Dragon Claw    | 4 equal cards                  | Sum          |
| 10  | Double Trouble | Two pair                       | 15           |
| 11  | Den of Wolves  | Full house                     | 25           |
| 12  | Yar!           | 5 equal cards                  | 50           |
| 13  | Broken Arrow   | Straight of 4                  | 30           |
| 14  | Straight Shot  | Straight of 5                  | 40           |
| 15  | Chance         | None                           | Sum          |

On every row exactly one of `made_point` and `is_sum_point` is set.

## Field Names

The `HandRanking` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `HandRankKey` (`hand_rank_key`), `HandType`,
`TargetSymbol`, `TargetEye` (`target_eye`), `IsTwoPair` (`is_two_pair`),
`IsFullHouse` (`is_full_house`), `TargetCount` (`target_count`),
`StraightCount` (`straight_count`), `MadePoint` (`made_point`), `SumPoint`
(`is_sum_point`), `UI_Texture`, `~Name` and `~Desc`. Its 15 rows match the
15 rows of clients 1784 and 3474 in every named column and string, with
`<null>` stored as `0`; the file writes `IsFullHouse` before `IsTwoPair`.
The two files are byte for byte the same. The client Lua reads the strings
through `getIconTextureName()`, `getName()` and `getDesc()` on
`ToClient_getHandRankStaticStatusWrapper(key)`
(`panel_window_minigame_yachtdice_invite_1.luac`).

The `#참조` sheet of the same workbook notes the values: `HandType` `0`
checks the eye only, `1` the symbol only, `2` both; `TargetSymbol` is a
card symbol (`1` to `4`, see [`yachtbasecard.dbss`](yachtbasecard_dbss.md)).
Both are `0` or `<null>` on every sheet row, so the data cannot tell which
bytes of `unknown_04` to `unknown_11` hold them.

## Notes

- The LOC type 105 descriptions (`str_id4=1`) follow the Korean ones:
  "Gain the sum of all 1s in points.", "Two pairs. Gain 15 points."

## Open Questions

### Where `HandType` and `TargetSymbol` Sit

The sheet has two columns the named fields do not cover, `HandType` and
`TargetSymbol`, both `0` on every row, and the row has 17 bytes from `+0x04`
to `+0x14` that the named fields do not cover: 13 zero bytes and the u32
`unknown_0d`, `1` on every row. A hand rank with a symbol check would show
which bytes they are; no client has one. `unknown_0d` matches no sheet
column.
