# `interiorrelationpoint.dbss` Format

## Purpose

Placement points of the house furniture: one 66-byte row per furniture
character with the chair that matches it and a point value for each piece
of furniture it can stand on (dresser, bedside cabinet, table, shelf and
more) and for each free side (front, back, left, right). The matching
character pairs a table with its chair: Melissande Table (`6252`) and
Melissande Dining Table (`6251`) both match Melissande Chair (`6751`).
On client 3482 the file holds 1,140 rows, 966 on client 1784. Companion
`interiorrelationpointoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ------ | ---------------- | --------- |
| 1      | 1346 and later | 3483    | `interiorrelationpoint.dbss`       | 75,260 | 1,140 Row        | 66        |
| 1      | 1346 and later | 3483    | `interiorrelationpointoffset.dbss` | 11,420 | 1,140 Offset Row | 10        |

| Layout | File                               | Known             | Unknown    |
| ------ | ---------------------------------- | ----------------- | ---------- |
| 1      | `interiorrelationpoint.dbss`       | 75,260 B (100.0%) | 0 B (0.0%) |
| 1      | `interiorrelationpointoffset.dbss` | 11,420 B (100.0%) | 0 B (0.0%) |

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

| File                               | Required | Role                                                                                    |
| ---------------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `interiorrelationpointoffset.dbss` | Optional | `character_key -> data_offset` of every row; the parser walks the main file without it   |
| `characterstaticoffset.dbss`       | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text              |
| `languagedata_en.loc`              | Optional | Furniture names, LOC type 6                                                              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                    |
| ----------- | ---------- | ------------ | ---------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                   |
| `+0x04`     | u32        | count        | Number of rows; 1,140 on client 3482     |
| `+0x08`     | Row[count] | rows         | See Row                                  |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table         |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 66 * count`)       |
| `rows+0x08` | u32        | zero         | Always `0`                               |

### Row (66 bytes)

Values on client 3482; a point is `0`, `1`, `2`, `3` or `5`.

| Offset  | Type | Field                    | Notes                                                                    |
| ------- | ---- | ------------------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | character_key            | Row key: the furniture installation, a `characterstatic.dbss` character  |
| `+0x02` | u16  | character_key_dup        | Equal to `character_key` on every row; the offset index points here      |
| `+0x04` | u16  | matching_character_key   | The matching chair, a `characterstatic.dbss` key; `0` on 1,016 rows      |
| `+0x06` | i32  | matching_character_point | `0` on every row (clients 1784 and 3482)                                 |
| `+0x0A` | i32  | on_dresser               | Non-zero on 262 rows                                                      |
| `+0x0E` | i32  | on_bed_side_cabinet      | Equal to `on_dresser` on every row                                       |
| `+0x12` | i32  | on_wardrobe              | `0` on every row                                                          |
| `+0x16` | i32  | on_dining_table          | Non-zero on 261 rows                                                      |
| `+0x1A` | i32  | on_table                 | Non-zero on 262 rows                                                      |
| `+0x1E` | i32  | on_chair                 | `0` on every row                                                          |
| `+0x22` | i32  | on_sofa                  | `0` on every row                                                          |
| `+0x26` | i32  | on_bed                   | `0` on every row                                                          |
| `+0x2A` | i32  | on_book_case             | `3` on 17 rows, else `0`                                                 |
| `+0x2E` | i32  | on_shelf                 | Non-zero on 261 rows                                                      |
| `+0x32` | i32  | is_empty_in_front        | Non-zero on 531 rows                                                      |
| `+0x36` | i32  | is_empty_in_back         | `2` on 61 rows, else `0`                                                 |
| `+0x3A` | i32  | is_empty_in_left         | Equal to `is_empty_in_back` on every row                                 |
| `+0x3E` | i32  | is_empty_in_right        | Equal to `is_empty_in_back` on every row                                 |

The rows are in no key order; client 3482 opens with 16111, 16110, 16109.

### `interiorrelationpointoffset.dbss`

The `PABR` index layout of `characterstaticoffset.dbss`, read by
`parse_pabr_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                         |
| ----------- | ----------------- | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                        |
| `+0x04`     | u32               | count        | Equals the `interiorrelationpoint.dbss` count |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                                |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table              |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 10 * count`)            |
| `rows+0x08` | u32               | zero         | Always `0`                                    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                     |
| ------- | ---- | ------------- | ----------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at               |
| `+0x02` | u32  | data_offset   | Row start + 2, at `character_key_dup`     |
| `+0x06` | u32  | data_size     | `0` on every row                          |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Field Names

The `InteriorRelationPoint_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 17 columns: `CharacterKey`, the ten
`On*` columns (`OnDresser` to `OnShelf`), the four `IsEmptyIn*` columns,
`MatchingCharacterKey` and `MatchingCharacterPoint`. The 2016
`gc::InteriorRelationPointStaticStatus` holds `_installationCharacterKey`,
`_relationPoint` (13 i32 then, 14 now) and `_matchingCharacterKey` and
`_matchingCharacterPoint` as a pair.

All 966 keys of the sheet have a row on client 1784. The ten relation
columns with non-zero values match a field on 966 of 966 keys each, in
sheet order: `OnDresser` and `OnBedSideCabinet` (equal columns, `+0x0A`
and `+0x0E`), `OnDiningTable`, `OnTable`, `OnBookCase`, `OnShelf`,
`IsEmptyInFront`, and the equal `IsEmptyInBack`, `IsEmptyInLeft` and
`IsEmptyInRight` (`+0x36` to `+0x3E`). The four columns that are `0` on
every sheet row (`OnWardrobe`, `OnChair`, `OnSofa`, `OnBed`) take the four
all-zero fields between them in the same order. `MatchingCharacterKey`
matches `matching_character_key` on 966 of 966 keys (`<null>` as `0`), and
`MatchingCharacterPoint` (`0` on every sheet row) is the one field left,
next to the key as in the 2016 struct.

## Notes

- 124 of the 1,140 rows name a matching character on client 3482: tables
  and dining tables name the chair of their set. All 45 chairs named that
  way have a row of their own.
- No Lua file of client 3482 reads this table. The house window shows the
  interior points of the visited house through
  `toClient_GetVisitingTotalInteriorPoint()`, `...BaseInteriorPoint()`,
  `...SetOptionInteriorPoint()` and `...BonusInteriorPoint()`
  (`panel_window_installationmode_housepoint_renew.luac`).

## Open Questions

### How the Relation Points Count

The points read as a bonus for placing the furniture on another piece or
with a free side, but what the game adds them to (the interior points of
the house window, or a placement check) and what the values `1` to `5`
weigh is open.
