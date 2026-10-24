# `siegeterritoryoptionstaticstatus.bss` Format

## Purpose

The Node War options of each territory group: the two territories a
group fights in and the one console shows, the stat limits of its node
wars, the most participants per day, the battle days, the map icon
positions of the two territories and a list of skills. Client 3482 has
three rows, one per `_eTerritoryGroupType` (`BEGINNER = 0`, `ADVANCED =
1`, `INTERMEDIATE = 2` in `panel_window_villagesiegemenu_all.luac`):
Balenos and Serendia, Calpheon and Ulukita, Valencia and Outer Edania.
The Lua reads a row with
`ToClient_GetSiegeTerritoryOptionStaticStatusWrapper(groupType)`. The
Blue Battlefield table
[`oceansiegeterritoryoption.bss`](oceansiegeterritoryoption_bss.md) opens
its rows with the same keys and limit block.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                   | Bytes | Records | Row bytes                  |
| ------ | -------------- | ------- | -------------------------------------- | ----- | ------- | -------------------------- |
| 2      | 3402 and later | 3483    | `siegeterritoryoptionstaticstatus.bss` | 797   | 3 Row   | 247 to 283, 259 on average |
| 1      | 2709 to 3293   | 3293    | `siegeterritoryoptionstaticstatus.bss` | 485   | 3 Row   | 155                        |

| Layout | File                                   | Known         | Unknown       |
| ------ | -------------------------------------- | ------------- | ------------- |
| 2      | `siegeterritoryoptionstaticstatus.bss` | 302 B (37.9%) | 495 B (62.1%) |
| 1      | `siegeterritoryoptionstaticstatus.bss` | 230 B (47.4%) | 255 B (52.6%) |

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
| 3396   | No documented layout |
| 3387   | No documented layout |
| 3381   | No documented layout |
| 3373   | No documented layout |
| 3364   | No documented layout |
| 3356   | No documented layout |
| 3349   | No documented layout |
| 3342   | No documented layout |
| 3335   | No documented layout |
| 3326   | No documented layout |
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
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
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
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
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
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

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                                |
| ------------------- | -------------- | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                         |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory group              |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                                 |
| `rows+0x00`         | String Table   | string_table | See String Table                                     |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends        |
| `string_table+0x04` | u32            | zero         | Always `0`                                           |

### Row (variable: 223 bytes + start days and skills)

Values in the Notes are those of the three rows of client 3482, in
order.

| Offset                | Type                          | Field                        | Notes                                                                       |
| --------------------- | ----------------------------- | ---------------------------- | --------------------------------------------------------------------------- |
| `+0x00`               | u16                           | territory_key_1              | `territoryinfo.bss` key, LOC type 12 name: `0`, `2`, `4`                     |
| `+0x02`               | u16                           | territory_key_2              | `1`, `11`, `12`                                                              |
| `+0x04`               | u16                           | console_territory_key        | The territory console shows: `1`, `11`, `12`                                |
| `+0x06`               | u16                           | unknown_06                   | `14`, `3`, `3`                                                               |
| `+0x08`               | f32                           | hp_limit                     | `6500`, `11000`, `100000000`. See Stat Limits                                |
| `+0x0C`               | f32                           | ap_limit                     | `395`, `680`, `9999`                                                         |
| `+0x10`               | f32                           | dr_limit                     | Damage reduction: `335`, `530`, `9999`                                       |
| `+0x14`               | f32                           | unknown_14                   | `270`, `309`, FLT_MAX; with `unknown_18` the AP+DP limit, see Stat Limits     |
| `+0x18`               | f32                           | unknown_18                   | `346`, `411`, FLT_MAX                                                        |
| `+0x1C`               | f32                           | accuracy_limit               | `650`, `820`, `9999`                                                         |
| `+0x20`               | f32                           | evasion_limit                | `738`, `908`, `9999`                                                         |
| `+0x24`               | u32                           | dr_rate_limit                | Damage reduction rate, `1000000` = 100%: `200000`, `300000`, `1000000`       |
| `+0x28`               | u32                           | unknown_28                   | `0`, `0`, `1000000`                                                          |
| `+0x2C`               | u32                           | unknown_2c                   | `0`, `0`, `1000000`                                                          |
| `+0x30`               | u32                           | unknown_30                   | `0` on every row                                                             |
| `+0x34`               | f32                           | unknown_34                   | Equals `ap_limit` on every row                                               |
| `+0x38`               | f32                           | unknown_38                   | Equals `ap_limit` on every row                                               |
| `+0x3C`               | f32                           | unknown_3c                   | `100000000` on every row                                                     |
| `+0x40`               | u32                           | unknown_40                   | `300000`, `1000000`, `1000000`; the next three equal it on every row         |
| `+0x44`               | u32                           | unknown_44                   |                                                                              |
| `+0x48`               | u32                           | unknown_48                   |                                                                              |
| `+0x4C`               | u32                           | unknown_4c                   |                                                                              |
| `+0x50`               | u16                           | unknown_50                   | `0`, `1`, `2`: the row's `_eTerritoryGroupType`                              |
| `+0x52`               | u16                           | unknown_52                   | `3` on every row                                                             |
| `+0x54`               | u16                           | unknown_54                   | `2` on every row                                                             |
| `+0x56`               | u16                           | unknown_56                   | `1` on every row                                                             |
| `+0x58`               | u16                           | unknown_58                   | `2` on every row                                                             |
| `+0x5A`               | u16                           | unknown_5a                   | `1` on every row                                                             |
| `+0x5C`               | u16                           | unknown_5c                   | `1` on every row                                                             |
| `+0x5E`               | u16                           | unknown_5e                   | `10` on every row                                                            |
| `+0x60`               | u16                           | unknown_60                   | `1` on every row                                                             |
| `+0x62`               | u32                           | unknown_62                   | `10000` on every row                                                         |
| `+0x66`               | u32                           | unknown_66                   | `0` on every row                                                             |
| `+0x6A`               | u32                           | unknown_6a                   | `30000` on every row                                                         |
| `+0x6E`               | u32                           | unknown_6e                   | `0` on every row                                                             |
| `+0x72`               | u16                           | limit_member_count_sunday    | Most participants on a Sunday node war: `30`, `50`, `75`                     |
| `+0x74`               | u16                           | limit_member_count_monday    | `25`, `40`, `55`                                                             |
| `+0x76`               | u16                           | limit_member_count_tuesday   | `30`, `40`, `55`                                                             |
| `+0x78`               | u16                           | limit_member_count_wednesday | `25`, `40`, `75`                                                             |
| `+0x7A`               | u16                           | limit_member_count_thursday  | `30`, `40`, `55`                                                             |
| `+0x7C`               | u16                           | limit_member_count_friday    | `25`, `50`, `75`                                                             |
| `+0x7E`               | u32                           | start_day_count              | Number of `start_days`                                                       |
| `+0x82`               | u32[start_day_count]          | start_days                   | `CppEnums.VillageSiegeType` days; `0` to `5` (Sunday to Friday) on every row |
| `start_days+0x00`     | u8                            | unknown_start_days_00        | `2`, `3`, `4`                                                                |
| `start_days+0x01`     | f32                           | territory_1_icon_x           | Map icon of `territory_key_1`: `630`, `430`, `1110`                          |
| `start_days+0x05`     | f32                           | territory_1_icon_y           | `270`, `410`, `220`                                                          |
| `start_days+0x09`     | f32                           | territory_2_icon_x           | Map icon of `territory_key_2`: `660`, `840`, `950`                           |
| `start_days+0x0D`     | f32                           | territory_2_icon_y           | `390`, `420`, `80`                                                           |
| `start_days+0x11`     | u32                           | unknown_start_days_11        | `200000` on the first row, `0x7FFFFFFF` on the others                        |
| `start_days+0x15`     | u32                           | unknown_start_days_15        | `0x7FFFFFFF` on every row                                                    |
| `start_days+0x19`     | u32                           | unknown_start_days_19        | As `unknown_start_days_11`                                                   |
| `start_days+0x1D`     | u32                           | unknown_start_days_1d        | As `unknown_start_days_15`                                                   |
| `start_days+0x21`     | u32                           | unknown_start_days_21        | As `unknown_start_days_11`                                                   |
| `start_days+0x25`     | u32                           | unknown_start_days_25        | As `unknown_start_days_15`                                                   |
| `start_days+0x29`     | u32                           | unknown_start_days_29        | As `unknown_start_days_11`                                                   |
| `start_days+0x2D`     | u32                           | unknown_start_days_2d        | As `unknown_start_days_15`                                                   |
| `start_days+0x31`     | u32                           | unknown_start_days_31        | As `unknown_start_days_11`                                                   |
| `start_days+0x35`     | u32                           | unknown_start_days_35        | As `unknown_start_days_15`                                                   |
| `start_days+0x39`     | u32                           | unknown_start_days_39        | As `unknown_start_days_11`                                                   |
| `start_days+0x3D`     | u32                           | unknown_start_days_3d        | As `unknown_start_days_15`                                                   |
| `start_days+0x41`     | u32                           | unknown_start_days_41        | `200000`, `1000000`, `1000000`                                               |
| `start_days+0x45`     | u32                           | unknown_start_days_45        | `200000`, `0x7FFFFFFF`, `0x7FFFFFFF`                                         |
| `start_days+0x49`     | f32                           | hp_recovery_limit            | `5`, `0`, `0`                                                                |
| `start_days+0x4D`     | u32                           | unknown_start_days_4d        | `10000`, `0`, `0`                                                            |
| `start_days+0x51`     | u32                           | unknown_start_days_51        | `15`, `0`, `0`                                                               |
| `start_days+0x55`     | u32                           | stamina_limit                | `2100`, `0`, `0`                                                             |
| `start_days+0x59`     | u32                           | unknown_skill_no_count       | Number of `unknown_skill_nos`: `18`, `0`, `0`                                |
| `start_days+0x5D`     | u16[unknown_skill_no_count]   | unknown_skill_nos            | Skill numbers, LOC type 10 names. See Notes                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (variable: 131 bytes + start days)

| Offset            | Type                 | Field                        | Notes |
| ----------------- | -------------------- | ---------------------------- | ----- |
| `+0x00`           | u16                  | territory_key_1              |       |
| `+0x02`           | u16                  | territory_key_2              |       |
| `+0x04`           | u16                  | console_territory_key        |       |
| `+0x06`           | u16                  | unknown_06                   |       |
| `+0x08`           | f32                  | hp_limit                     |       |
| `+0x0C`           | f32                  | ap_limit                     |       |
| `+0x10`           | f32                  | dr_limit                     |       |
| `+0x14`           | f32                  | unknown_14                   |       |
| `+0x18`           | f32                  | unknown_18                   |       |
| `+0x1C`           | f32                  | accuracy_limit               |       |
| `+0x20`           | f32                  | evasion_limit                |       |
| `+0x24`           | u32                  | dr_rate_limit                |       |
| `+0x28`           | u32                  | unknown_28                   |       |
| `+0x2C`           | u32                  | unknown_2c                   |       |
| `+0x30`           | u32                  | unknown_30                   |       |
| `+0x34`           | f32                  | unknown_34                   |       |
| `+0x38`           | f32                  | unknown_38                   |       |
| `+0x3C`           | f32                  | unknown_3c                   |       |
| `+0x40`           | u32                  | unknown_40                   |       |
| `+0x44`           | u32                  | unknown_44                   |       |
| `+0x48`           | u32                  | unknown_48                   |       |
| `+0x4C`           | u32                  | unknown_4c                   |       |
| `+0x50`           | u16                  | unknown_50                   |       |
| `+0x52`           | u16                  | unknown_52                   |       |
| `+0x54`           | u16                  | unknown_54                   |       |
| `+0x56`           | u16                  | unknown_56                   |       |
| `+0x58`           | u16                  | unknown_58                   |       |
| `+0x5A`           | u16                  | unknown_5a                   |       |
| `+0x5C`           | u16                  | unknown_5c                   |       |
| `+0x5E`           | u16                  | unknown_5e                   |       |
| `+0x60`           | u16                  | unknown_60                   |       |
| `+0x62`           | u32                  | unknown_62                   |       |
| `+0x66`           | u32                  | unknown_66                   |       |
| `+0x6A`           | u32                  | unknown_6a                   |       |
| `+0x6E`           | u32                  | unknown_6e                   |       |
| `+0x72`           | u16                  | limit_member_count_sunday    |       |
| `+0x74`           | u16                  | limit_member_count_monday    |       |
| `+0x76`           | u16                  | limit_member_count_tuesday   |       |
| `+0x78`           | u16                  | limit_member_count_wednesday |       |
| `+0x7A`           | u16                  | limit_member_count_thursday  |       |
| `+0x7C`           | u16                  | limit_member_count_friday    |       |
| `+0x7E`           | u32                  | start_day_count              |       |
| `+0x82`           | u32[start_day_count] | start_days                   |       |
| `start_days+0x00` | u8                   | unknown_start_days_00        |       |

## Stat Limits

The limit block, matched against the node tooltips the
[`regioninfo.bss`](regioninfo_bss.md) Notes record from my game:

| Field            | Balenos, Serendia | Calpheon, Ulukita | Valencia, Outer Edania | Tooltip                                                         |
| ---------------- | ----------------- | ----------------- | ---------------------- | --------------------------------------------------------------- |
| `hp_limit`       | 6500              | 11000             | 100000000              | HP 6,500 on occupation nodes, 11,000 on Calpheon and Ulukita    |
| `ap_limit`       | 395               | 680               | 9999                   | AP 395 on occupation nodes, 680 at Trina Fort and City of the Dead |
| `dr_limit`       | 335               | 530               | 9999                   | Damage reduction 335 and 530                                    |
| `accuracy_limit` | 650               | 820               | 9999                   | Accuracy 650 and 820                                            |
| `evasion_limit`  | 738               | 908               | 9999                   | Evasion 738 and 908                                             |
| `dr_rate_limit`  | 200000            | 300000            | 1000000                | Damage reduction rate 20% and 30%                               |
| `hp_recovery_limit` | 5              | 0                 | 0                      | HP recovery 5 on occupation nodes                               |
| `stamina_limit`  | 2100              | 0                 | 0                      | Stamina 2,100 on occupation nodes                               |

`unknown_14` and `unknown_18` sum to the "Stats (AP+DP) Limit: {sum}"
line (`LUA_VILLAGESIEGE_LIMITVALUE`) the node war menu prints from
`_siegeMaxDDForUI + _siegeMaxPVForUI`: `616` for Balenos and Serendia,
`720` for Calpheon and Ulukita (the gear limit the `regioninfo.bss` Notes
give for those nodes), and FLT_MAX for Valencia and Outer Edania, where
`isUnlimitedDDPV()` prints "No Stat Limit".

## Field Names

The table is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`TerritoryOption` in its name. The names come from the Lua of client 3482
and the node tooltips:

| Field                                   | Source                                                          |
| --------------------------------------- | --------------------------------------------------------------- |
| `territory_key_1`, `territory_key_2`, `console_territory_key` | `getTerritoryKey1Raw()`, `getTerritoryKey2Raw()`, `getConsoleTerritoryKeyRaw()`; each pair is one row of `_eTerritoryKeyRaw` pairs the Lua draws as flags, and the console key always equals one of the two |
| `limit_member_count_*`, `start_days`    | `getLimitMemberCount(day)`, `getStartDayListCount()`, `getStartDay(index)`, as in `oceansiegeterritoryoption.bss` |
| `hp_limit` to `stamina_limit`           | See Stat Limits; each value matches its tooltip line on both capped rows, or on the occupation row for HP recovery and stamina |
| `territory_1_icon_x` to `territory_2_icon_y` | `_territory1IconPos.x`, `.y` and `_territory2IconPos.x`, `.y`, which `panel_window_villagesiegemenu_all_1.luac` passes to `SetPosXY` for the two territory icons under `_ContentsGroup_SiegeRenewal2026`; the four f32 are the only x, y pairs in the row and are whole tens inside the map panel |

## Notes

- Client 3474 has the same file as client 3482. Clients 2765 to 3251
  use Layout 1 (485 bytes): the rows stop after `unknown_start_days_00`,
  with no icon positions, tail values or skills. Client 2519 has a
  shorter row (428 bytes) that no layout here reads yet.
- `unknown_skill_nos` on the Balenos and Serendia row are the skills
  `10189` to `10194` (Blessing of Taebaek and its PRI to PEN levels) and
  `10206` to `10217` (Blessing of Asadal and Fury of Asadal with theirs).
- The tooltip of an occupation node lists 20% for critical hit rate and
  damage and for back, down and air attack damage, Black Spirit's Rage
  100% and its recovery 0.15%. The first row's twelve
  `unknown_start_days_11` to `_3d` hold six `200000` (20%) values, and
  `unknown_start_days_4d` (`10000`) and `_51` (`15`) read as 100% and
  0.15% on a 10,000 = 100% scale; which value is which line is open.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: the three territory keys with their
  names, the named limits, the six day limits, the battle days by name
  and the icon positions.

## Open Questions

### Which of the AP+DP Pair Is AP

`unknown_14` and `unknown_18` are `_siegeMaxDDForUI` and
`_siegeMaxPVForUI`, but the Lua only prints their sum. The smaller value
comes first on both capped rows (`270, 346` and `309, 411`), as AP comes
before damage reduction in `ap_limit` and `dr_limit`; no source shows
the two apart.

### The Tail Values

What `unknown_start_days_11` to `unknown_start_days_51` limit: the six
pairs of `200000` and `0x7FFFFFFF`, the two values after them and the
`10000` and `15` before the stamina (see Notes), and why the other two
rows leave them unlimited.

### The Skill List

What the game does with `unknown_skill_nos` in Balenos and Serendia node
wars, which list the Taebaek and Asadal skills, and whether it turns them
off there.

### The u16 Block

`unknown_06` (`14`, `3`, `3`; `13` on client 3251), `unknown_50` to
`unknown_60` and `unknown_start_days_00` (`2`, `3`, `4`). `unknown_52`
(`3`) may be the 3 war heroes the occupation tooltip shows, which
[`siegemercenarylimitcount.bss`](siegemercenarylimitcount_bss.md) also
lists.
