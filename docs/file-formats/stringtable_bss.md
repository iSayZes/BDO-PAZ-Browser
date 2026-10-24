# `stringtable.bss` Format

## Purpose

The Korean source of the client's keyed UI strings. Each row pairs a string key
(`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_6`) with its Korean text and a 32-bit key
hash. The hash is the LOC type `37` `str_id1`, so this file is how a key the
client scripts use turns into the translated text in `languagedata_*.loc`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes     | Records                    | Row bytes |
| ------ | -------------- | ------- | ----------------- | --------- | -------------------------- | --------- |
| 1      | 1286 and later | 3483    | `stringtable.bss` | 7,334,867 | 51,099 String Row, 8 Sheet | 16        |

| Layout | File              | Known               | Unknown          |
| ------ | ----------------- | ------------------- | ---------------- |
| 1      | `stringtable.bss` | 7,130,471 B (97.2%) | 204,396 B (2.8%) |

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
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
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

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Translated text, type `37` keyed by the row hash and sheet |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

A PABR file of eight sheets, followed by the same counted string table and
8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings). Every
string in the table is UTF-16LE (`is_wide=1`).

| Offset              | Type               | Field              | Notes                                                |
| ------------------- | ------------------ | ------------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]            | magic              | ASCII `PABR`                                         |
| `+0x04`             | u32                | sheet_count        | `8` on client 3458                                   |
| `+0x08`             | Sheet[sheet_count] | sheets             | Sheets back to back, see Sheet                       |
| `sheets+0x00`       | String Table       | string_table       | See String Table                                     |
| `string_table+0x00` | u32                | string_table_start | Where the last sheet ends (`0xC6DD8` on client 3458) |
| `string_table+0x04` | u32                | zero               | Always `0`                                           |

### Sheet (variable: 12 bytes + rows)

A 12-byte sheet header, then the sheet's rows.

| Offset  | Type                  | Field      | Notes                                                          |
| ------- | --------------------- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u32                   | sheet_hash | Key hash of the sheet name (see Key Hash)                      |
| `+0x04` | u32                   | name_ref   | String table index of the sheet name (`GAME`, `RESOURCE`, ...) |
| `+0x08` | u32                   | row_count  | Number of 16-byte rows that follow                             |
| `+0x0C` | String Row[row_count] | rows       | See String Row                                                 |

### String Row (16 bytes)

| Offset  | Type | Field      | Notes                                                                  |
| ------- | ---- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | key_hash   | Key hash of the key string (see Key Hash); the LOC type `37` `str_id1` |
| `+0x04` | u32  | key_ref    | String table index of the key, e.g. `NPCSHOP_BUY`                      |
| `+0x08` | u32  | value_ref  | String table index of the Korean text; never empty, 7 are one space    |
| `+0x0C` | u32  | unknown_0c | Always `0`                                                             |

Rows are not sorted by hash or key. The string table is interned: each string
is stored once, in the order the sheets first use it (sheet name, then key
and value of each row), and later uses point back. No key repeats within a
sheet; 6,553 values reuse an earlier text such as `"확인"`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `95,195` strings on client 3458       |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, all UTF-16LE     |

## Key Hash

`key_hash` and `sheet_hash` are Bob Jenkins' lookup3 `hashlittle()` over the
UTF-16LE string without a terminator, seed `0xC5EDE`:
`LUA_GROWTHPASS_WIDGET_ICON_NOTICE_NEW_DESC` -> `1517777731`, `GAME` ->
`3183609639`. It matches all 50,992 key hashes and all 8 sheet hashes on
client 3464 (`test_every_key_hash_is_the_key_hash_of_its_key` and
`test_every_sheet_hash_is_the_key_hash_of_its_name`). The same function keys
the LOC type 59 TextBind texts (see `languagedata_loc.md`, Type 59). The
browser computes it with `key_hash()` in `_common/string_hash.py`.

## Sheets

The sheet order is fixed on client 3458. `loc str_id2` is the LOC type `37`
`str_id2` that every LOC row of that sheet's keys carries.

| # | Name          | Hash         | Rows   | `loc str_id2` | Holds                                                      |
| - | ------------- | ------------ | ------ | ------------- | ---------------------------------------------------------- |
| 0 | `GAME`        | `0xBDC20727` | 22,936 | `1`           | Lua UI strings (`LUA_*`, `WEBHELPER_*`), labels and tooltips |
| 1 | `SymbolNo`    | `0xA9B8EA3C` | 4,529  | `6`           | Server error and result messages (`eErrNo*`)               |
| 2 | `IMAGESLIDE`  | `0x8AD0A01B` | 204    | `7`           | Image slide subtitles (`SEQUENCE_SUBTITLE_IMAGE_SLIDE_*`)  |
| 3 | `ACTIONCHART` | `0x138A8C63` | 2,000  | `3`           | Speech bubbles and action lines (`Bubble_*`, `Trade_*`)     |
| 4 | `RESOURCE`    | `0x9C44332D` | 9,525  | `2`           | UI panel resources (`PANEL_*`)                             |
| 5 | `CUTSCENE`    | `0x08342431` | 8,564  | `0`           | Cutscene subtitles (`CS_*`)                                |
| 6 | `TOOL`        | `0xE09F9402` | 785    | `4`           | Enum labels (`eSymNo*`), e.g. chat types, log reasons      |
| 7 | `WEB`         | `0xA5AA1B9E` | 2,360  | `5`           | In-game web page strings (`WEB_*`)                         |

This settles which LOC type `37` `str_id2` is which sheet (the old
"Type 37 sheet names" question in
[`languagedata_loc.md`](languagedata_loc.md)).

## LOC Join

Look up a key's translated text as LOC type `37`, `str_id1 = key_hash`,
`str_id2 = ` the sheet's `loc str_id2`, `str_id3 = 0`, `str_id4 = 0`.

- 50,779 of the 50,903 rows have a LOC row on client 3458. The other 124
  (62 `GAME`, 33 `CUTSCENE`, 17 `RESOURCE`, 12 `SymbolNo`) have Korean text
  only; they read like newer content not yet translated, so fall back to
  the Korean `value_ref` text.
- 44 keys sit in two sheets (`NPCSHOP_BUY` in `GAME` and `RESOURCE`). Both
  rows carry the same hash and share the key string, and LOC keeps them
  apart by `str_id2`, which can hold different text (`ALCHEMY_MANUFACTURE_BTN_MANUFACTURE`:
  `GAME` "Start", `RESOURCE` "Start Crafting"). So the hash depends on the
  key alone, not on the sheet.
- 3,027 LOC type `37` `str_id1` values have no row here; keys dropped from
  the client whose translations LOC still carries.
- 352 LOC rows use `str_id3 = 1` as a second variant of a key, mostly
  regional URLs (`WEBHELPER_*_EN`) and date lines (`*_GMT`, `*_UTC`). 164 keys
  have only the `str_id3 = 1` row, so a lookup should try `str_id3 = 0` first
  and then `1`. `str_id4` is always `0`.

### Town NPC Navigation Types

The `GAME` sheet holds the town NPC navigation labels as
`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_1` to `_39`, one per number with no gaps.
The client picks them by `SpawnType`, and the suffix is not always the
`SpawnType` value; the full mapping is the Navi label column of
[`characterspawntype.dbss` SpawnType](characterspawntype_dbss.md#spawntype).
A few, as the English LOC text:

| Key suffix | Korean        | English (LOC)              | SpawnType          |
| ---------- | ------------- | -------------------------- | ------------------ |
| `_1`       | 기술 교관     | Skill Instructor           | `SkillTrainer` (1) |
| `_6`       | 창고          | Storage                    | `WareHouse` (6)    |
| `_25`      | 아이템 거래소 | Central Market             | `ItemMarket` (25)  |
| `_35`      | 악기 상인     | Instruments                | `Instrument` (40)  |
| `_39`      | 황실제작 납품 | Imperial Crafting Delivery | `SupplyShop` (33)  |

The client reads these through `PAGetString(Defines.StringSheet_GAME, key)`,
so a script's `StringSheet_<name>` picks the sheet and with it the LOC
`str_id2`.

## Notes

- Seven `GAME` values are a single space (`LUA_JOIN_LOCALWAR_RULE7`,
  `LUA_LOCALWARINFO_DESC_RULETEXT_9` and others on client 3458), unused rule
  and condition lines; the table shows them as a dash when LOC has no text.
- Some values forward to another text rather than holding it, e.g.
  `ALCHEMY_COOK_TEXT_DESCRPITION` = `{TextBind:TEXTBIND_ALCHEMY_COOK_TEXT_DESCRPITION}`,
  and the LOC text keeps the same placeholder. The text it names is LOC type
  59, keyed by the key hash of the name (`languagedata_loc.md`, Type 59), or
  the Korean `textbind.dbss` record of that key. The Text column shows it
  filled; the Korean column keeps the value as stored. 460 values hold a
  placeholder on client 3464. Values also carry `<PAColor...>` tags and
  `{name}` placeholders.
- bdo-data-extractor names the sheets `GAME`, `RESOURCE`, `ACTIONCHART` and
  others; the names are stored in this file, so that part is now confirmed.

## Open Questions

### `str_id3 = 1` Variants

352 LOC type `37` rows use `str_id3 = 1`. Most look like a second,
region-specific text of the key (a newer URL, a UTC instead of GMT date line),
but some keys have only the `str_id3 = 1` row. Which condition makes the client
pick variant `1` is not known.
