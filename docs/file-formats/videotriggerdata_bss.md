# `videotriggerdata.bss` Format

## Purpose

Where a video plays when the player walks into an area, and the scripts
it runs. Each row names one video (`Intro`, `PEDU2_C6A`), a world
position and radius, a start condition (quest state checks, `getlevel`,
`checkwoman`), the scripts the client runs when the video starts and ends
(`acceptquest`, `completequest`, `setPosition`, `PushItem`) and the
contents group that must be open. It is a PABR table of 45-byte rows
whose text sits in the string table. The rows have the shape of the
[`sequencetriggerdata.bss`](sequencetriggerdata_bss.md) rows, with a
video in place of the sequence.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 2      | 3458 and later | 3482    | `videotriggerdata.bss` | 1,676 | 6 Row   | 45        |
| 1      | 3454           | 3454    | `videotriggerdata.bss` | 1,507 | 5 Row   | 44        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 2      | `videotriggerdata.bss` | 1,670 B (99.6%)  | 6 B (0.4%) |
| 1      | `videotriggerdata.bss` | 1,507 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 1 |
| 3444   | No file  |
| 3435   | No file  |
| 3426   | No file  |
| 3418   | No file  |
| 3412   | No file  |
| 3402   | No file  |
| 3396   | No file  |
| 3387   | No file  |
| 3381   | No file  |
| 3373   | No file  |
| 3364   | No file  |
| 3356   | No file  |
| 3349   | No file  |
| 3342   | No file  |
| 3335   | No file  |
| 3326   | No file  |
| 3321   | No file  |
| 3314   | No file  |
| 3303   | No file  |
| 3302   | No file  |
| 3293   | No file  |
| 3283   | No file  |
| 3275   | No file  |
| 3267   | No file  |
| 3258   | No file  |
| 3251   | No file  |
| 3242   | No file  |
| 3235   | No file  |
| 3229   | No file  |
| 3212   | No file  |
| 3203   | No file  |
| 3193   | No file  |
| 3186   | No file  |
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
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

None. The video stays a name: the `.bk2` videos under `ui_movie/` have no
handler.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (45 bytes)

| Offset  | Type   | Field               | Notes                                                                                                     |
| ------- | ------ | ------------------- | --------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32    | video_name_hash     | ASCII key hash (lookup3, seed `0xC5EDE`) of `video_name`; matches on every row                            |
| `+0x04` | u32    | video_name          | Index into `strings`: the video, `Intro` for `ui_movie/pc/intro/intro.bk2`, `PEDU2_C6A` for `ui_movie/pc/edania2/pedu2_c6a.bk2` |
| `+0x08` | u32    | start_condition     | Index into `strings`: the script that must hold for the video to start                                    |
| `+0x0C` | u32    | start_execute       | Index into `strings`: the script run when the video starts; empty when none                               |
| `+0x10` | u32    | end_execute         | Index into `strings`: the script run when the video ends                                                  |
| `+0x14` | f32[3] | position            | World x, y, z of the trigger area                                                                         |
| `+0x20` | u32    | video_name_hash_dup | Same value as `video_name_hash` on every row                                                              |
| `+0x24` | f32    | radius              | Radius of the trigger area around `position`, in world units (`1100` to `3020` on client 3482)                           |
| `+0x28` | u32    | contents_group_open | Index into `strings`: the contents group key as decimal text (`9`, `2186`)                                |
| `+0x2C` | u8     | unknown_2c          | `0` or `1`; see Open Questions                                                                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                     |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                         |
| `+0x04` | pstr[string_count] | strings      | UTF-8 names, scripts and keys; one empty string serves every empty field  |

## Layout 1

The row has no `unknown_2c`.

### Row (44 bytes)

| Offset  | Type   | Field               | Notes                                                        |
| ------- | ------ | ------------------- | ------------------------------------------------------------ |
| `+0x00` | u32    | video_name_hash     | As in Layout 2                                               |
| `+0x04` | u32    | video_name          | As in Layout 2, with the folder in front (`Intro/Intro`)     |
| `+0x08` | u32    | start_condition     | As in Layout 2                                               |
| `+0x0C` | u32    | start_execute       | As in Layout 2                                               |
| `+0x10` | u32    | end_execute         | As in Layout 2                                               |
| `+0x14` | f32[3] | position            | As in Layout 2                                               |
| `+0x20` | u32    | video_name_hash_dup | As in Layout 2                                               |
| `+0x24` | f32    | radius              | As in Layout 2                                               |
| `+0x28` | u32    | contents_group_open | As in Layout 2                                               |

## Rows

On client 3482 the file has 6 rows: `Intro` (contents group `9`,
`unknown_2c` `0`) and the five Edania videos `PEDU2_C6A`, `PEDU2_C6B`,
`PEDU2_C6C`, `PEDU2_C6C_F` and `PEDU2_C6D` (contents group `2186`,
`unknown_2c` `1`). `PEDU2_C6C` and `PEDU2_C6C_F` share quest step
`9306,30` and split on `!checkwoman()` and `checkwoman()`, a male and a
female cut of one video.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
the table, and client 1784 has no `videotriggerdata.bss`. The script
fields and the trigger area take their names from the
[`sequencetriggerdata.bss`](sequencetriggerdata_bss.md) row, whose source
XML names them: `StartCondition`, `StartExecute`, `EndExecute`,
`Position`, `Radius` and `ContentsGroupOpen`, and that row also stores a
copy of its name hash before the radius. The values agree: the 157 `PEDU2`
sequences of `sequencetriggerdata.bss` all have contents group `2186`, as
the five `PEDU2` videos do, and 149 sequences have `9`, as `Intro` does
(client 3482).

## Notes

- `FromClient_PlayDialogVideo()` in `panel_dialogmovie.luac` plays a video
  path with `.bk2` added (`.webm` on console) and its `.srt` subtitles;
  `CloseDialogMovie()` calls `ToClient_onEndVideoTriggerEvent()`, the end
  of a video trigger.
- `9` and `2186` are contents group keys, not region keys: region `9` is
  Western Guard Camp, and `regioninfo.bss` has no region `2186`.

## Open Questions

### What `unknown_2c` Marks

`1` on the five `PEDU2` rows and `0` on `Intro` (client 3482). The six
rows show no pattern beyond that split, and no Lua getter reads the
table, so the byte cannot be tied to one of the six flags that end a
[`sequencetriggerdata.bss`](sequencetriggerdata_bss.md) row.
