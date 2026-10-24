# `extractitem.dbss` Format

## Purpose

Reform stone extraction (`PANEL_EXTRACTIONSYSTEM_TITLE` "Extract Reform
Stone"): the blacksmith window that splits reformed gear back into the gear
it was made from and the reform stone. A row names the reformed item, the
item the extraction uses up, and the two items it returns.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes   | Records         | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------- | --------------- | --------- |
| 1      | 1280 and later | 3483    | `extractitem.dbss`       | 112,132 | 2,336 Row       | 48        |
| 1      | 1280 and later | 3483    | `extractitemoffset.dbss` | 28,036  | 2,336 Index Row | 12        |

| Layout | File                     | Known              | Unknown    |
| ------ | ------------------------ | ------------------ | ---------- |
| 1      | `extractitem.dbss`       | 112,132 B (100.0%) | 0 B (0.0%) |
| 1      | `extractitemoffset.dbss` | 28,036 B (100.0%)  | 0 B (0.0%) |

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

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `extractitemoffset.dbss`  | Optional | `item_id -> (data_offset, data_size)` index, see below; the rows can be walked without it |
| [`itemimprovement.dbss`](itemimprovement_dbss.md) | Optional | Reform records; the handler's Reform Group column, see Notes |
| [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) | Optional | Reform stone groups; picks one group when a reform pair has several |

Item names come from LOC type 0.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                                     |
| ------- | ---------- | ----- | --------------------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2,336` on client 3464                    |
| `+0x04` | Row[count] | rows  | `count` 48-byte rows, back to back to the end of the file |

### Row (48 bytes)

The row is four 12-byte slots of a u32 item ID and its u64 count. Every
count is `1` on all 2,336 rows (client 3473).

| Offset  | Type | Field                 | Notes                                                         |
| ------- | ---- | --------------------- | ------------------------------------------------------------- |
| `+0x00` | u32  | item_id               | Reformed gear the window takes; unique per row, the index key |
| `+0x04` | u64  | item_count            | Fixed `1`, see Field Names                                    |
| `+0x0C` | u32  | need_item_id          | Item the extraction uses up, see below                        |
| `+0x10` | u64  | need_item_count       | How many `need_item_id` the extraction uses up                |
| `+0x18` | u32  | result_item_id        | Gear returned; never equal to `item_id`                       |
| `+0x1C` | u64  | result_item_count     | Fixed `1`, see Field Names                                    |
| `+0x24` | u32  | result_material_id    | Reform stone (or other material) returned                     |
| `+0x28` | u64  | result_material_count | Fixed `1`, see Field Names                                    |

Byte `+0x03` of each item ID is `0` on every row, so no ID carries an
enchant level in its top byte. The rows are not sorted by `item_id`.

Each `result_material_id` goes with one `need_item_id` (client 3464):

| need_item_id                         | result_material_id                                   | Rows |
| ------------------------------------ | ---------------------------------------------------- | ---- |
| `320060` Mirror of Equilibrium       | `9771` Inverted Heart of Garmoth                     | 844  |
| `320060` Mirror of Equilibrium       | `9793` Heart of Kutum                                | 455  |
| `320060` Mirror of Equilibrium       | `9787` Heart of Karanda                              | 363  |
| `320060` Mirror of Equilibrium       | `8421` Blessed Soul Fragment, `8432` Exalted Soul Fragment | 26 each |
| `320060` Mirror of Equilibrium       | Six Cups (`8141`, `8148`, `8149`, `8181`, `8182`, `8417`) | 10 each |
| `320060` Mirror of Equilibrium       | `9788` Obsidian Specter's Energy                     | 4    |
| `320060` Mirror of Equilibrium       | `820974` to `820977` Cups, `821251` Flawless Herald's Crystal | 3 each |
| `320060` Mirror of Equilibrium       | `820018` Gauche Rawr-Rawr's Heart                    | 2    |
| `320060` Mirror of Equilibrium       | `820969` Crimson Behelit Alchemy Stone Appearance    | 1    |
| `4929` Restoration Stone             | `4912` Ultimate Weapon Reform Stone                  | 407  |
| `4929` Restoration Stone             | `4913` Ultimate Armor Reform Stone                   | 44   |
| `4929` Restoration Stone             | `8179` Sunset Glow Crystal                           | 6    |
| `8172` Combatant's Restoration Stone | `8170` Combatant's Stone (Weapon)                    | 79   |
| `8172` Combatant's Restoration Stone | `8171` Combatant's Stone (Armor)                     | 4    |

The three need items' own texts list these pairs: the Mirror of Equilibrium
(TextBind `MIRROR_OF_EQUILIBRIUM`) reads "Extract Heart of Karanda from
Storm Devoured gear", "Extract Inverted Heart of Garmoth from Fiery gear"
and so on; Restoration Stone (`4929`) names the two Ultimate Reform Stones
and Sunset Glow Crystal; Combatant's Restoration Stone (`8172`) names the
two Combatant's Stones.

### `extractitemoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `extractitem.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 12-byte rows; no magic, no trailer |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                         |
| ------- | ---- | ----------- | --------------------------------------------- |
| `+0x00` | u32  | item_id     | Row key, the `item_id` at `data_offset`       |
| `+0x04` | u32  | data_offset | Row start, the `item_id` itself (not past it) |
| `+0x08` | u32  | data_size   | `48`, the whole row                           |

Unlike the `itemimprovementoffset.dbss` index, `data_offset` points at the
key and `data_size` covers it. The index rows are not in file order; on
client 3464 the 2,336 offsets are exactly the 2,336 row starts, and the key
at each offset equals the index `item_id`.

## Field Names

The row is the `Item_ImprovementExtract_Table` sheet that a private server
on client 1784 ships in its `DataSheets.bexcel`. Its columns are
`ExtractionItem`, `NeedExtractMaterialKey`, `NeedExtractMaterialCount`,
`ExtractDropItem1`, `ExtractDropItem2` and `ContentsGroupKey`; the last one
is not in the row.

| Field                 | Column                     |
| --------------------- | -------------------------- |
| `item_id`             | `ExtractionItem`           |
| `need_item_id`        | `NeedExtractMaterialKey`   |
| `need_item_count`     | `NeedExtractMaterialCount` |
| `result_item_id`      | `ExtractDropItem1`         |
| `result_material_id`  | `ExtractDropItem2`         |

Matched by `ExtractionItem` against client 3473, the sheet and the client
file share 1,127 keys. `need_item_id` and `result_item_id` match on all
1,127 and `result_material_id` on 1,086; the other 41 are Cups whose key
changed (sheet `8135`, `8146` and `8147`, client `8141`, `8148`, `8149`,
`8181` and `8182`). That private server's own `extractitem.dbss`, built from
the sheet, holds 1,196 rows; all three item columns match on every one.

`NeedExtractMaterialCount` is `1` on every sheet row, so the values do not
place it. The server dump of that private server does. Its
`Item_ImprovementExtract_Table` loader builds four (item key, 8-byte count)
pairs per row, in row order: `ExtractionItem` with a literal count of `1`,
`NeedExtractMaterialKey` with `NeedExtractMaterialCount`, then
`ExtractDropItem1` and `ExtractDropItem2` (one `ExtractDropItem%#` string,
read for 1 and 2), each with a literal `1`. It rejects a row when any key is
`0` or any count is not above `0`. So `need_item_count` is the only count
the sheet sets, and the other three are `1` by the loader.

Neither the 2016 client with debug symbols nor the tables of a private server on
client 519 have an extraction type or table.

## Notes

- The window is `panel_window_extraction_system_all`
  (`PaGlobal_Extraction_System_All`, decompiled with unluac). For the item in
  the window it calls `ToClient_ExtractNeedItemEnchantKey(itemKey)` for the
  item to use up (shown with `PANEL_EXTRACTIONSYSTEM_NEEDCATALYST` "※ You
  need a [{itemName}]." when the inventory has none),
  `ToClient_ExtractToItemEnchantKey(itemKey, 0)` for the result item and
  `ToClient_ExtractToItemEnchantKey(itemKey, 1)` for the result material, the
  three IDs at `+0x0C`, `+0x18` and `+0x24`. The inventory list takes items
  for which `ToClient_isExtractFromItem(key)` is true, and the request is
  `ToClient_requestExtractItem(extractableSlotNo, materialSlotNo)`. The
  result line is `LUA_EXTRACTIONSYSTEM_RESULTMSG` "{item1} and {itme2} were
  separated.", and the two result icons hide their count. The need item is
  drawn with a literal `1` (or `0` when the inventory has none), not with
  `need_item_count`.
- The window refuses gear with Caphras EXP (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_1`)
  or transfused crystals (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_2`); the table has no
  field for either.
- A row is a [`itemimprovement.dbss`](itemimprovement_dbss.md) reform run
  backwards. On client 3464, 2,323 of the 2,336 rows have a 5-item reform
  record whose result is `item_id` and whose input is `result_item_id`, and
  `result_material_id` is a stone of that record's group in
  [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md). This holds
  for all three need items, the Ultimate and Combatant's gear included.
  20 (result, input) pairs have reform records in two groups; on the 10
  rows that hit one (client 3464), Dandelion Purgatum gear from `742928` to
  `743330`, only one of the two groups holds `result_material_id` as a
  stone. The handler's Reform Group is that one group, and `-` on the other
  13 rows.
- The other 13 rows (client 3464) return a different gear key than the
  reform input: ten Dandelion Purgatum rows (`742932`, `742933`, `743032`,
  `743033`, `743132`, `743133`, `743232`, `743233`, `743332`, `743333`) and
  three Hexround rows (`736624`, `736724`, `736824`). For example `743332`
  (Fiery Dandelion Purgatum) is reformed from `743232` but extracts to
  `743231` (Dandelion Purgatum).
- 41 `result_item_id` values (client 3464) are themselves an `item_id` of
  another row, so reformed gear can be extracted down more than one step.
- One `item_id` has no LOC type 0 name on client 3464: `748603`, which
  extracts to `748601` Dandelion Enlightened Blade and Heart of Karanda. The
  handler shows the Korean name `itemenchant.dbss` stores for it
  (폭풍을 삼킨 단델리온 선검).
- calpheonlabs' page gives the example `731222` and `320060` to `694273` and
  `9771` (Inverted Heart of Garmoth). On client 3464 the `731222` row returns
  `9787` (Heart of Karanda), which is what the Mirror of Equilibrium text
  says for Storm Devoured gear; its capture has 2,328 rows.

## Open Questions

### Enchant Level on the Key

The Lua passes the item's `getKey()`, an item enchant key, to
`ToClient_isExtractFromItem` and the two lookup functions, while the table
stores plain item IDs. Whether the client drops the enchant level before
the lookup, and whether the returned gear keeps the enchant level of the
extracted gear, is not in the table.
