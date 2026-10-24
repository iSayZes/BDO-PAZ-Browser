# `audioinfo.bss` Format

## Purpose

The world's background music and ambience by area: per area colour of
the audio map image (`AudioMap.bmp`, the `audio_map_index` `7` of
[`fieldinfo.bss`](fieldinfo_bss.md)) the four Wwise `BGM` states
the area plays and its ambience index. Since the Wwise sound system
(client 1866) the file also lists the `BGM` states of a few special
situations and the radio channels of the radio player. Client 1784 holds
the older layout with sound bank and music numbers per situation.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ----------------------------------------- | --------- |
| 6      | 2665 and later | 3483    | `audioinfo.bss` | 40,977  | 1,256 Row, 10 State Entry, 10 Radio Entry | 28        |
| 5      | 2000 to 2657   | 2657    | `audioinfo.bss` | 36,534  | 1,113 Row, 10 State Entry, 10 Radio Entry | 28        |
| 4      | 1958 to 1996   | 1996    | `audioinfo.bss` | 28,374  | 831 Row, 9 State Entry, 10 Radio Entry    | 28        |
| 3      | 1914 to 3482   | 3482    | `audioinfo.bss` | 40,977  | 1,256 Row, 10 State Entry, 10 Radio Entry | 28        |
| 2      | 1866 to 1937   | 1937    | `audioinfo.bss` | 27,671  | 831 Row, 8 State Entry                    | 28        |
| 1      | 1109 to 1862   | 1862    | `audioinfo.bss` | 132,980 | 831 Row                                   | 160       |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 6      | `audioinfo.bss` | 40,846 B (99.7%)  | 131 B (0.3%)   |
| 5      | `audioinfo.bss` | 36,443 B (99.8%)  | 91 B (0.2%)    |
| 4      | `audioinfo.bss` | 28,285 B (99.7%)  | 89 B (0.3%)    |
| 3      | `audioinfo.bss` | 40,846 B (99.7%)  | 131 B (0.3%)   |
| 2      | `audioinfo.bss` | 27,655 B (99.9%)  | 16 B (0.1%)    |
| 1      | `audioinfo.bss` | 129,656 B (97.5%) | 3,324 B (2.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 6             |
| 3482   | Layout 6             |
| 3474   | Layout 6             |
| 3473   | Layout 6             |
| 3464   | Layout 6             |
| 3458   | Layout 6             |
| 3454   | Layout 6             |
| 3444   | Layout 6             |
| 3435   | Layout 6             |
| 3426   | Layout 6             |
| 3418   | Layout 6             |
| 3412   | Layout 6             |
| 3402   | Layout 6             |
| 3396   | Layout 6             |
| 3387   | Layout 6             |
| 3381   | Layout 6             |
| 3373   | Layout 6             |
| 3364   | Layout 6             |
| 3356   | Layout 6             |
| 3349   | Layout 6             |
| 3342   | Layout 6             |
| 3335   | Layout 6             |
| 3326   | Layout 6             |
| 3321   | Layout 6             |
| 3314   | Layout 6             |
| 3303   | Layout 6             |
| 3302   | Layout 6             |
| 3293   | Layout 6             |
| 3283   | Layout 6             |
| 3275   | Layout 6             |
| 3267   | Layout 6             |
| 3258   | Layout 6             |
| 3251   | Layout 6             |
| 3242   | Layout 6             |
| 3235   | Layout 6             |
| 3229   | Layout 6             |
| 3212   | Layout 6             |
| 3203   | Layout 6             |
| 3193   | Layout 6             |
| 3186   | Layout 6             |
| 3177   | Layout 6             |
| 3169   | Layout 6             |
| 3158   | Layout 6             |
| 3151   | Layout 6             |
| 3144   | Layout 6             |
| 3133   | Layout 6             |
| 3125   | Layout 6             |
| 3118   | Layout 6             |
| 3111   | Layout 6             |
| 3103   | Layout 6             |
| 3095   | Layout 6             |
| 3086   | Layout 6             |
| 3072   | Layout 6             |
| 3062   | Layout 6             |
| 3052   | Layout 6             |
| 3045   | Layout 6             |
| 3037   | Layout 6             |
| 3030   | Layout 6             |
| 3021   | Layout 6             |
| 3012   | Layout 6             |
| 3002   | Layout 6             |
| 2995   | Layout 6             |
| 2987   | Layout 6             |
| 2978   | Layout 6             |
| 2970   | Layout 6             |
| 2959   | Layout 6             |
| 2951   | Layout 6             |
| 2942   | Layout 6             |
| 2935   | Layout 6             |
| 2932   | Layout 6             |
| 2923   | Layout 6             |
| 2919   | Layout 6             |
| 2907   | Layout 6             |
| 2900   | Layout 6             |
| 2891   | Layout 6             |
| 2882   | Layout 6             |
| 2872   | Layout 6             |
| 2863   | Layout 6             |
| 2855   | Layout 6             |
| 2849   | Layout 6             |
| 2844   | Layout 6             |
| 2834   | Layout 6             |
| 2825   | Layout 6             |
| 2819   | Layout 6             |
| 2811   | Layout 6             |
| 2803   | Layout 6             |
| 2794   | Layout 6             |
| 2783   | Layout 6             |
| 2774   | Layout 6             |
| 2765   | Layout 6             |
| 2756   | Layout 6             |
| 2750   | Layout 6             |
| 2743   | Layout 6             |
| 2736   | Layout 6             |
| 2726   | Layout 6             |
| 2717   | Layout 6             |
| 2709   | Layout 6             |
| 2703   | Layout 6             |
| 2695   | Layout 6             |
| 2684   | Layout 6             |
| 2672   | Layout 6             |
| 2665   | Layout 6             |
| 2657   | Layout 5             |
| 2649   | Layout 5             |
| 2644   | Layout 5             |
| 2637   | Layout 5             |
| 2629   | Layout 5             |
| 2619   | Layout 5             |
| 2612   | Layout 5             |
| 2606   | Layout 5             |
| 2602   | Layout 5             |
| 2601   | Layout 5             |
| 2592   | Layout 5             |
| 2583   | Layout 5             |
| 2575   | Layout 5             |
| 2567   | Layout 5             |
| 2560   | Layout 5             |
| 2553   | Layout 5             |
| 2545   | Layout 5             |
| 2538   | Layout 5             |
| 2529   | Layout 5             |
| 2519   | Layout 5             |
| 2513   | Layout 5             |
| 2510   | Layout 5             |
| 2507   | Layout 5             |
| 2503   | Layout 5             |
| 2498   | Layout 5             |
| 2492   | Layout 5             |
| 2487   | Layout 5             |
| 2480   | Layout 5             |
| 2474   | Layout 5             |
| 2468   | Layout 5             |
| 2460   | Layout 5             |
| 2453   | Layout 5             |
| 2444   | Layout 5             |
| 2438   | Layout 5             |
| 2434   | Layout 5             |
| 2429   | Layout 5             |
| 2421   | Layout 5             |
| 2414   | Layout 5             |
| 2407   | Layout 5             |
| 2401   | Layout 5             |
| 2397   | Layout 5             |
| 2393   | Layout 5             |
| 2384   | Layout 5             |
| 2378   | Layout 5             |
| 2372   | Layout 5             |
| 2358   | Layout 5             |
| 2352   | Layout 5             |
| 2347   | Layout 5             |
| 2343   | Layout 5             |
| 2335   | Layout 5             |
| 2327   | Layout 5             |
| 2324   | Layout 5             |
| 2319   | Layout 5             |
| 2313   | Layout 5             |
| 2308   | Layout 5             |
| 2302   | Layout 5             |
| 2295   | Layout 5             |
| 2290   | Layout 5             |
| 2284   | Layout 5             |
| 2276   | Layout 5             |
| 2269   | Layout 5             |
| 2259   | Layout 5             |
| 2250   | Layout 5             |
| 2243   | Layout 5             |
| 2235   | Layout 5             |
| 2229   | Layout 5             |
| 2224   | Layout 5             |
| 2218   | Layout 5             |
| 2215   | Layout 5             |
| 2207   | Layout 5             |
| 2203   | Layout 5             |
| 2196   | Layout 5             |
| 2192   | Layout 5             |
| 2189   | Layout 5             |
| 2183   | Layout 5             |
| 2179   | Layout 5             |
| 2171   | Layout 5             |
| 2163   | Layout 5             |
| 2156   | Layout 5             |
| 2151   | Layout 5             |
| 2147   | Layout 5             |
| 2142   | Layout 5             |
| 2138   | Layout 5             |
| 2134   | Layout 5             |
| 2130   | Layout 5             |
| 2122   | Layout 5             |
| 2107   | Layout 5             |
| 2098   | Layout 5             |
| 2089   | Layout 5             |
| 2081   | Layout 5             |
| 2073   | Layout 5             |
| 2067   | Layout 5             |
| 2063   | Layout 5             |
| 2059   | Layout 5             |
| 2052   | Layout 5             |
| 2044   | Layout 5             |
| 2039   | Layout 5             |
| 2032   | Layout 5             |
| 2025   | Layout 5             |
| 2011   | Layout 5             |
| 2005   | Layout 5             |
| 2000   | Layout 5             |
| 1996   | Layout 4             |
| 1991   | Layout 4             |
| 1985   | Layout 4             |
| 1980   | Layout 4             |
| 1969   | Layout 4             |
| 1964   | Layout 4             |
| 1958   | Layout 4             |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | Layout 3             |
| 1933   | Layout 3             |
| 1927   | Layout 3             |
| 1921   | Layout 3             |
| 1914   | Layout 3             |
| 1908   | Layout 2             |
| 1897   | Layout 2             |
| 1892   | Layout 2             |
| 1886   | Layout 2             |
| 1881   | Layout 2             |
| 1871   | Layout 2             |
| 1866   | Layout 2             |
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
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | Layout 1             |
| 1137   | Layout 1             |
| 1132   | Layout 1             |
| 1127   | Layout 1             |
| 1122   | Layout 1             |
| 1118   | Layout 1             |
| 1114   | Layout 1             |
| 1109   | Layout 1             |
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
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
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

None.

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[10]          | state_entries      | No count in the file; see State Entry Count             |
| `rows+0x64`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x68`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | 17 values from `0` to `60` in rising order on client 3482 |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table, where `unknown_tail` ends    |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

### Row (28 bytes)

| Offset  | Type   | Field               | Notes                                                                                     |
| ------- | ------ | ------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32    | color               | Area colour as `0x00RRGGBB`; each colour once                                             |
| `+0x04` | u32    | color_dup           | Equals `color` on every row                                                               |
| `+0x08` | u32[4] | bgm_states          | Indexes into `strings`: four states of the Wwise `BGM` state group (`W01_Balenos_Exploration_Motivated`); see BGM State Slots |
| `+0x18` | u32    | bank_no_environment | Ambience: the Wwise `ENV_INDEX_<n>` state; `0` on 226 of 1,256 rows (client 3482)         |

The rows are in no colour order.

### State Entry (10 bytes)

| Offset  | Type | Field       | Notes                                                                             |
| ------- | ---- | ----------- | --------------------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00  | `0` to `9`, each once, in no order (client 3482)                                  |
| `+0x01` | u8   | unknown_01  | `51` to `55`, or `255` on four entries                                             |
| `+0x02` | u32  | state_group | Index into `strings`: the Wwise state group, `BGM` on every entry                 |
| `+0x06` | u32  | state_name  | Index into `strings`: the state (`W00_ArenaOfSolare_Round_Start`)                 |

### Radio Entry (17 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00   | `1` to `10` in file order on client 3482                                                |
| `+0x04` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or an empty string                      |
| `+0x08` | u32  | channel_name | Index into `strings`: the channel title (`City Jazz Vibes (feat. Jazz in Black Desert)`), UTF-16LE; empty for entries 1 and 2 |
| `+0x0C` | u32  | event_name   | Index into `strings`: the Wwise event (`BGM_Radio_Chanel_01`, `BGM_Radio_off`)           |
| `+0x10` | u8   | unknown_10   | `1` on the eight channels, `0` on entries 1 and 2                                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | State and event names, UTF-8; the channel titles and one empty string UTF-16LE; a string several rows use is stored once |

## Layout 5

The radio entries have no leading `unknown_00`. Only the Radio Entry
differs from Layout 6.

### Radio Entry (13 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | unknown_04   | Index into `strings`: `Game_Start`, `Radio_Off` or empty |
| `+0x04` | u32  | channel_name | Index into `strings`: the channel title                  |
| `+0x08` | u32  | event_name   | Index into `strings`: the Wwise event                    |
| `+0x0C` | u8   | unknown_10   | `1` on the eight channels                                |

## Layout 4

Nine state entries. Only the File Layout differs from Layout 5.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[9]           | state_entries      | No count in the file; keys `0` to `8`                    |
| `rows+0x5A`               | u32                      | radio_count        | Number of `radio_entries`                                |
| `rows+0x5E`               | Radio Entry[radio_count] | radio_entries      | See Radio Entry                                          |
| `radio_entries+0x00`      | u32                      | unknown_tail_count | Number of `unknown_tail` bytes                           |
| `radio_entries+0x04`      | u8[unknown_tail_count]   | unknown_tail       | The same 17 values as on client 3482                     |
| `unknown_tail+0x00`       | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 3

Eight state entries and no radio entries or tail. Only the File Layout
differs from Layout 4.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[8]           | state_entries      | No count in the file; keys `0` to `7`                    |
| `rows+0x50`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 2

Five state entries and no radio entries or tail. Only the File Layout
differs from Layout 3.

### File Layout

| Offset                    | Type                     | Field              | Notes                                                    |
| ------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                   | char[4]                  | magic              | ASCII `PABR`                                             |
| `+0x04`                   | u32                      | row_count          | Number of area colours                                   |
| `+0x08`                   | Row[row_count]           | rows               | See Row                                                  |
| `rows+0x00`               | State Entry[5]           | state_entries      | No count in the file; keys `0` to `4`                    |
| `rows+0x32`               | String Table             | string_table       | See String Table                                         |
| `string_table+0x00`       | u32                      | string_table_start | Offset of the string table                               |
| `string_table+0x04`       | u32                      | zero               | `0`                                                      |

## Layout 1

The sound bank system before Wwise: per area colour a sound bank and a
music number for each of 18 situations, and no state entries. The string
table is empty. The File Layout and the Row differ from Layout 2.

### File Layout

| Offset              | Type           | Field              | Notes                                   |
| ------------------- | -------------- | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                            |
| `+0x04`             | u32            | row_count          | Number of area colours                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                 |
| `rows+0x00`         | String Table   | string_table       | `string_count` `0` on client 1784       |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table              |
| `string_table+0x04` | u32            | zero               | `0`                                     |

### Row (160 bytes)

| Offset  | Type    | Field               | Notes                                                           |
| ------- | ------- | ------------------- | --------------------------------------------------------------- |
| `+0x00` | u32     | color               | Area colour as `0x00RRGGBB`; each colour once                   |
| `+0x04` | u32     | color_dup           | Equals `color` on every row                                     |
| `+0x08` | u32[18] | bank_nos            | Sound bank per situation, in the order of Situations            |
| `+0x50` | u32[18] | music_indexes       | Music number in that bank per situation, same order             |
| `+0x98` | u32     | unknown_98          | `1` on every row of client 1784                                 |
| `+0x9C` | u32     | bank_no_environment | Ambience bank                                                   |

## Situations

The order of `bank_nos` and `music_indexes` in Layout 1, with the column
pair of the client 1784 sheet each slot matches:

| Slot | Columns                                              |
| ---- | ---------------------------------------------------- |
| 0    | `BankNo_NormaiDay`, `MusicIdx_NormaiDay`             |
| 1    | `BankNo_NormaiNight`, `MusicIdx_NormaiNight`         |
| 2    | `BankNo_CombatLv1`, `MusicIdx_CombatLv1`             |
| 3    | `BankNo_CombatLv2`, `MusicIdx_CombatLv2`             |
| 4    | `BankNo_CombatNightLv1`, `MusicIdx_CombatNightLv1`   |
| 5    | `BankNo_CombatNightLv2`, `MusicIdx_CombatNightLv2`   |
| 6    | `BankNo_CombatBoss`, `MusicIdx_CombatBoss`           |
| 7    | `BankNo_CombatHpLow`, `MusicIdx_CombatHpLow`         |
| 8    | `BankNo_Riding`, `MusicIdx_Riding`                   |
| 9    | `BankNo_Racing`, `MusicIdx_Racing`                   |
| 10   | `BankNo_VillageSiege`, `MusicIdx_VillageSiege`       |
| 11   | `BankNo_Siegewarfare`, `MusicIdx_Siegewarfare`       |
| 12   | `BankNo_GuildTeamBattle`, `MusicIdx_GuildTeamBattle` |
| 13   | `BankNo_BattleRoyale`, `MusicIdx_BattleRoyale`       |
| 14   | `BankNo_BattleRoyaleLobby`, `MusicIdx_BattleRoyaleLobby` |
| 15   | `BankNo_BattleRoyaleLostRegion`, `MusicIdx_BattleRoyaleLostRegion` |
| 16   | `BankNo_NationSiegeStart`, `MusicIdx_NationSiegeStart` |
| 17   | `BankNo_Undersea`, `MusicIdx_Undersea`               |

## State Entry Count

No field holds the number of state entries; it grew from 5 (clients 1866
and 1886) to 8, 9 and 10 (client 2107 and later), one entry per new key,
so each count is its own layout. A reader can only check a count by
walking the rest of the file to the string table.

## BGM State Slots

The names the four `bgm_states` slots hold most often on client 3482
(the part after the area prefix, `W01_Balenos_`):

| Slot | Most frequent names                                                        |
| ---- | -------------------------------------------------------------------------- |
| 0    | `Exploration_Motivated` (294 rows), `Exploration_Peaceful` (105)           |
| 1    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Battle_General` (84) |
| 2    | `Battle_Boss` (866)                                                        |
| 3    | `Exploration_Motivated` (293), `Exploration_Peaceful` (105), `Diving` (83) |

Areas with combat or underwater music fill slot 1 with a `Battle_General`
and slot 3 with a `Diving` state; elsewhere slots 0, 1 and 3 hold the same
state.

## Field Names

The `AudioMap_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `RegionGroupKey`, `R`, `G`, `B`,
`AreaName`, `BankNo_Environment` and a `BankNo_` and `MusicIdx_` pair per
situation. Joined on `R`, `G`, `B` = `color`, 811 of 811 sheet rows have a
Layout 1 row (client 1784). `bank_no_environment` matches on 811 of 811,
the 18 `music_indexes` on 811 of 811 each. `bank_nos` slot 7 matches on
811 of 811 and the other 17 slots on 810: the sheet row `1087` holds bank
`109` in them where the file holds `110`.
`Index`, `RegionGroupKey` and the `AreaName` note are not in the file.

In Layout 3, `bank_no_environment` equals the client 1784 value on 810 of
the 811 colours both clients have (client 3482), and every value is an
`ENV_INDEX_<n>` state of `sound2022/wwise_ids.h`. That header lists the
`bgm_states` and `state_name` strings under the `BGM` state group, and
the radio `event_name` strings under its events. The `AudioRenewal_Table`
sheet of client 1784 has the columns `Index`, `AudioStateGroupName`,
`AudioStateName` and `ContentsGroupKey` and no rows; it fits the State
Entry, but with no rows no value can confirm it.

## Open Questions

### BGM State Slot Meaning

Which situation each `bgm_states` slot plays is not confirmed. The names
point at normal play (slot 0), combat (slot 1), boss fights (slot 2) and
underwater (slot 3), the Layout 1 situations `NormaiDay`, `CombatLv1`,
`CombatBoss` and `Undersea`.

### State Entry Keys

`unknown_00` of the state entries runs `0` to `9` and `unknown_01` holds
`51` to `55` or `255`. The states (`W00_ArenaOfSolare_Round_Start`,
`W00_Ocean_Battle_PVP`, `W01_PapuCrioWar_Default`) suggest a key per
special situation (an arena round, a sea battle); `unknown_01` may be a
contents group or a priority.

### Radio Tail

`unknown_tail` (17 rising values up to `60`) follows the radio entries and
matches no key in the file.

### Layout Before Client 1109

Clients 435 to 822 hold a file no layout reads (85,652 bytes on client
822); clients 855 to 1076 have none. Its rows are larger than the Layout 1
row.
