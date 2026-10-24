# `groupcameradata.bss` Format

## Purpose

The summaries shown when a story cutscene is skipped: one fixed 28-byte row per
cutscene with its title, a short recap, a quoted line and a region symbol icon,
all as indices into a shared string table. The Korean text is the source; LOC
type 97 holds the translations.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records                                 | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | --------------------------------------- | --------- |
| 2      | 2142 and later | 3483    | `groupcameradata.bss` | 25,147 | 92 Cutscene Row                         | 28        |
| 1      | 1579 to 1784   | 1784    | `groupcameradata.bss` | 12,760 | 6 Cutscene Row, 170 Line, 12 Line Group | 16        |

| Layout | File                  | Known            | Unknown         |
| ------ | --------------------- | ---------------- | --------------- |
| 2      | `groupcameradata.bss` | 24,411 B (97.1%) | 736 B (2.9%)    |
| 1      | `groupcameradata.bss` | 11,400 B (89.3%) | 1,360 B (10.7%) |

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
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | No documented layout |
| 1897   | No documented layout |
| 1892   | No documented layout |
| 1886   | No documented layout |
| 1881   | No documented layout |
| 1871   | No documented layout |
| 1866   | No documented layout |
| 1862   | No documented layout |
| 1854   | No documented layout |
| 1846   | No documented layout |
| 1838   | No documented layout |
| 1832   | No documented layout |
| 1826   | No documented layout |
| 1822   | No documented layout |
| 1818   | No documented layout |
| 1804   | No documented layout |
| 1794   | No documented layout |
| 1790   | No documented layout |
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

| File                  | Required | Role                                                                   |
| --------------------- | -------- | ---------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 97, `str_id1` = `scene_id`, `str_id4` 0 / 1 / 2 = title / description / quote |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                | Field        | Notes                                          |
| ------------------- | ------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                 | count        | Number of rows; 92 on client 3458              |
| `+0x08`             | Cutscene Row[count] | rows         | See Cutscene Row                               |
| `rows+0x00`         | String Table        | string_table | See String Table                               |
| `string_table+0x00` | u32                 | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                 | zero         | Always 0                                       |

Rows are not sorted by ID (the first three are 65, 66 and 2).

### Cutscene Row (28 bytes)

| Offset  | Type     | Field           | Notes                                                             |
| ------- | -------- | --------------- | ----------------------------------------------------------------- |
| `+0x00` | u32      | scene_id        | Unique; 2 to 260 on client 3458, with gaps                        |
| `+0x04` | u32      | title_ref       | String table index of the Korean title                            |
| `+0x08` | u32      | description_ref | String table index of the Korean recap, with stored line breaks   |
| `+0x0C` | u32      | quote_ref       | String table index of the Korean quoted line                      |
| `+0x10` | u32      | icon_ref        | String table index of the region symbol, relative to `ui_texture/` |
| `+0x14` | bytes[8] | unknown_14      | Always `0`                                                        |

### String Table (variable: 4 bytes + strings)

251 strings on client 3458, all referenced. Scenes that repeat a summary
share its entries: 43 to 47, 197 and 198, and 253 to 256 share their title,
recap and quote, 248 and 249 their title and quote, and 257 to 260 their
title. The four icons are stored once each.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 251 on client 3458  |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

Client 1784 rows are 20 bytes, without `unknown_14`, and a second table of
timed voice lines follows the rows, before the string table. Only the File
Layout and the Cutscene Row differ from Layout 2; Line Group and Line exist
only here. The parser reads only Layout 2.

### File Layout

| Offset             | Type                         | Field            | Notes                                                 |
| ------------------ | ---------------------------- | ---------------- | ----------------------------------------------------- |
| `+0x00`            | char[4]                      | magic            | ASCII `PABR`                                          |
| `+0x04`            | u32                          | count            | Number of rows; 6 on client 1784                      |
| `+0x08`            | Cutscene Row[count]          | rows             | See Cutscene Row                                      |
| `rows+0x00`        | u32                          | line_group_count | 12 on client 1784                                     |
| `rows+0x04`        | Line Group[line_group_count] | line_groups      | See Line Group                                        |
| `line_groups+0x00` | String Table                 | string_table     | See String Table                                      |
| `EOF-0x08`         | u32                          | table_start      | Offset of the string table, where the line groups end |
| `EOF-0x04`         | u32                          | zero             | Always 0                                              |

### Line Group (variable: 4 bytes + lines)

2 to 36 lines per group on client 1784.

| Offset  | Type             | Field      | Notes            |
| ------- | ---------------- | ---------- | ---------------- |
| `+0x00` | u32              | line_count | Number of lines  |
| `+0x04` | Line[line_count] | lines      | See Line         |

### Line (16 bytes)

| Offset  | Type | Field      | Notes                                                                                           |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00 | 1 to 15 on client 1784, the same value in every line of a group and unique per group; 1 to 5 and 14 are also `scene_id` values of the rows |
| `+0x04` | u32  | unknown_04 | Rises within a group in steps of thousands (0 to 165000), a time in milliseconds by its values  |
| `+0x08` | u32  | voice_ref  | String table index of a voice key (`QUEST_VCE_NEW_9027_43_1_Illezra`, `NPC_VCE_NEW_0_0_Mute_1`) |
| `+0x0C` | u32  | line_ref   | String table index of the Korean line spoken                                                    |

### Cutscene Row (20 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | scene_id        |       |
| `+0x04` | u32  | title_ref       |       |
| `+0x08` | u32  | description_ref |       |
| `+0x0C` | u32  | quote_ref       |       |
| `+0x10` | u32  | icon_ref        | String table index of the icon path; on client 1784 also quest icons (`Icon/Quest/405_1.dds`) |

## Notes

- The cutscene skip panel (`window/cutscene/panel_window_cutsceneskip_1`)
  opens in `eRenderMode_GroupCamera` and fills its title, main text, sub text
  and territory icon from `getTitle`, `getMainDescription`,
  `getSubDescription` and `getIconPath`, the four strings of a row.
- The icons mark the story region. On client 3458:
  `SymbolIcon_SnowMountain.dds` (Drieghan, 40 scenes),
  `SymbolIcon_AbyssOne.dds` (The Magnus, 19), `SymbolIcon_Valenos.dds`
  (Balenos, 18) and `SymbolIcon_Feather.dds` (Atoraxxion, 15). All four
  exist under `ui_texture/combine/icon/symbolicon/`.
- The app indexes the region icons by scene ID (`IndexKind.CUTSCENE_ICON`,
  read through `IconKind.CUTSCENE`).
