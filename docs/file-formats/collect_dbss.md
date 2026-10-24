# `collect.dbss` Format

## Purpose

Gathering rules per gathering character: one row per Collect character (a
tree, ore vein, plant or animal corpse) with its gathering kind, gathering
time, the tools that work on it and the drop group each tool gives. The row
key is the character key that `collectresourcename.dbss` maps the world
models to. `collectoffset.dbss` is the key-ordered index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ------ | -------------- | --------- |
| 2      | 2726 and later | 3483    | `collect.dbss`       | 48,556 | 714 Row        | 68        |
| 2      | 2726 and later | 3483    | `collectoffset.dbss` | 7,144  | 714 Offset Row | 10        |
| 1      | 1346 to 2039   | 2039    | `collect.dbss`       | 29,716 | 619 Row        | 48        |
| 1      | 1346 to 2039   | 2039    | `collectoffset.dbss` | 6,194  | 619 Offset Row | 10        |

| Layout | File                 | Known             | Unknown         |
| ------ | -------------------- | ----------------- | --------------- |
| 2      | `collect.dbss`       | 39,988 B (82.4%)  | 8,568 B (17.6%) |
| 2      | `collectoffset.dbss` | 7,144 B (100.0%)  | 0 B (0.0%)      |
| 1      | `collect.dbss`       | 29,716 B (100.0%) | 0 B (0.0%)      |
| 1      | `collectoffset.dbss` | 6,194 B (100.0%)  | 0 B (0.0%)      |

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
| 2717   | No documented layout |
| 2709   | No documented layout |
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
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
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

| File                                              | Required | Role                                                        |
| ------------------------------------------------- | -------- | ----------------------------------------------------------- |
| `collectoffset.dbss`                              | Optional | `character_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Character names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                      |
| ------- | ---------- | ----- | ------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `713` on client 3474       |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 68 bytes + name text)

| Offset        | Type    | Field                  | Notes                                                              |
| ------------- | ------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`       | u16     | character_key          | Gathering character, a `characterstatic.dbss` `character_id`; unique per row, the index key |
| `+0x02`       | str16   | name                   | Empty on every row; the index's `data_offset` points here          |
| `name+0x00`   | u16     | character_key_dup      | Equal to `character_key` in every row                              |
| `name+0x02`   | u8      | product_data_type      | Gathering kind, see Product Data Types                             |
| `name+0x03`   | u32     | product_time           | `60000` on every row (client 3474)                                 |
| `name+0x07`   | f32     | product_hp             | `1.0` on every row (client 3474)                                   |
| `name+0x0B`   | f32     | product_decrease_hp    | `1.0` on every row (client 3474)                                   |
| `name+0x0F`   | u32     | product_item_drop_key  | `10002` on every row (client 3474); an item main group key, see Notes |
| `name+0x13`   | u8[3]   | collect_tool_types     | Tool per slot, see Collect Tool Types; `19` is an empty slot       |
| `name+0x16`   | u32[3]  | collect_item_drop_keys | Item main group key per slot; `0` exactly where the slot's tool is `19` |
| `name+0x22`   | bytes[12] | unknown_name_22      | `0` on every row (client 3474); not in Layout 1                    |
| `name+0x2E`   | u32     | action_point           | `1` on every row (client 3474)                                     |
| `name+0x32`   | u32     | spawn_delay_time       | `0` on every row (client 3474)                                     |
| `name+0x36`   | u32     | spawn_variable_time    | `0` on every row (client 3474)                                     |

With the empty `name`, every row is 68 bytes. The rows are not sorted by key.

### `collectoffset.dbss`

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `collect.dbss` count        |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row   |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                  |
| ------- | ---- | ------------- | -------------------------------------- |
| `+0x00` | u16  | character_key | Row key                                |
| `+0x02` | u32  | data_offset   | Row start + 2, at `name`               |
| `+0x06` | u32  | data_size     | Row size - 2: `66` on client 3474      |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Layout 1

### Row (variable: 48 bytes + name text)

| Offset      | Type   | Field                  | Notes                                                   |
| ----------- | ------ | ---------------------- | ------------------------------------------------------- |
| `+0x00`     | u16    | character_key          | Gathering character                                     |
| `+0x02`     | str16  | name                   | Empty on every row                                      |
| `name+0x00` | u16    | character_key_dup      | Equal to `character_key` in every row                   |
| `name+0x02` | u8     | product_data_type      | Gathering kind, see Product Data Types                  |
| `name+0x03` | u32    | product_time           | `60000` on every row (client 1784)                      |
| `name+0x07` | f32    | product_hp             | `1.0` on every row (client 1784)                        |
| `name+0x0B` | f32    | product_decrease_hp    | `1.0` on every row (client 1784)                        |
| `name+0x0F` | u16    | product_item_drop_key  | `10002` on every row (client 1784)                      |
| `name+0x11` | u8[3]  | collect_tool_types     | Tool per slot; `15` is an empty slot                    |
| `name+0x14` | u16[3] | collect_item_drop_keys | `0` exactly where the slot's tool is `15`               |
| `name+0x1A` | u32    | action_point           | `1` on every row (client 1784)                          |
| `name+0x1E` | u32    | spawn_delay_time       | `0` on every row (client 1784)                          |
| `name+0x22` | u32    | spawn_variable_time    | `0` on every row (client 1784)                          |

The drop keys are u16 here and u32 in Layout 2, and `unknown_name_22` does
not exist yet. Every row is 48 bytes; the index's `data_size` is `46`.

## Field Names

The row is the 2016 `gc::CollectStaticStatus` in member order: `_name`,
`_key`, `_productDataType`, `_productTime`, `_productHp`,
`_productDecreaseHp`, `_productItemDropKey`, `_collectToolType[3]`,
`_collectItemDropKey[3]`, `_actionPoint`, `_spawnDelayTime`,
`_spawnVariableTime`. The 2016 drop keys are u16, as in Layout 1.

The values match the `Collect_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`, the `character_key`: all 606
sheet keys are rows on both clients. An empty sheet cell in a tool slot is
tool `15` with drop key `0` on client 1784, and tool `19` with drop key `0`
on client 3474.

| Field                  | Column                           | Same value (client 1784) | Same value (client 3474) |
| ---------------------- | -------------------------------- | ------------------------ | ------------------------ |
| product_data_type      | `ProductDataType`                | 606 of 606               | 606 of 606               |
| product_time           | `ProductTime`                    | 606 of 606               | 606 of 606               |
| product_hp             | `ProductAllHP`                   | 606 of 606               | 606 of 606               |
| product_decrease_hp    | `ProductDeceraseHP`              | 606 of 606               | 606 of 606               |
| product_item_drop_key  | `ItemDropID`                     | 606 of 606               | 606 of 606               |
| collect_tool_types     | `ToolType_0` to `ToolType_2`     | 606 of 606               | 598 of 606               |
| collect_item_drop_keys | `ItemDropID_0` to `ItemDropID_2` | 606 of 606               | 598 of 606               |
| action_point           | `ActionPoint`                    | 606 of 606               | 606 of 606               |
| spawn_delay_time       | `SpawnDelayTime`                 | 606 of 606               | 606 of 606               |
| spawn_variable_time    | `SpawnVariableTime`              | 606 of 606               | 606 of 606               |

`product_time`, `product_hp`, `product_decrease_hp`, `product_item_drop_key`,
`action_point` and both spawn times hold one value on every row and in the
sheet, so their names rest on the 2016 member order and the Layout 1
positions, not on the values. The eight rows that differ on client 3474 are
`11985` to `11992` (Chanterelle, Red-spotted Amanita, Mesima, Dictyophora,
three Citron Trees, Jadeite): their tool slots or drop groups changed after
client 1784. The client 3474 file adds 107 keys the sheet lacks.

The sheet columns `NeedObjectSkillNo`, `ProductSkillLevel`, `Exp`,
`ProductSkillPointExp` and `IsNotReduce` have no place in the row. `Exp`
and `IsNotReduce` vary in the sheet, and no row byte follows them.

## Product Data Types

The names are the 2016 `gc::ProductDataType::Type` values.

| Value | Name                           | Rows (client 3474) | Tools in the rows                    |
| ----- | ------------------------------ | ------------------ | ------------------------------------ |
| 0     | `eProductData_Default`         | 0                  |                                      |
| 1     | `eProductData_Collect_Base`    | 0                  |                                      |
| 2     | `eProductData_Collect_Collect` | 229                | BareHands, Hoe, Syringe, Pray        |
| 3     | `eProductData_Collect_Farm`    | 0                  |                                      |
| 4     | `eProductData_Collect_Mining`  | 97                 | Pickax, BareHands, ButcheryKnife     |
| 5     | `eProductData_Collect_Purify`  | 0                  |                                      |
| 6     | `eProductData_Collect_Logging` | 246                | Axe, Syringe, Hoe, BareHands, Pickax |
| 7     | `eProductData_Collect_Tanning` | 141                | ButcheryKnife, SkinKnife, Syringe, Hoe, Axe |

## Collect Tool Types

Values `0` to `10` are the 2016 `gc::CollectToolType::Type` values, which end
at `TypeCount = 11`. The client Lua's `CppEnums.CollectToolTypeName`
(`global_define_cpp_enum.luac`) lists the same names in the same order and
adds MassStone, FishingChair, Whip, Oar and, on client 3474, Reserve; it
keys them by engine globals, so their numbers do not show in the Lua.

| Value | Name           | Slots (client 3474) |
| ----- | -------------- | ------------------- |
| 0     | BareHands      | 281                 |
| 2     | Axe            | 151                 |
| 3     | Syringe        | 175                 |
| 4     | Hoe            | 217                 |
| 5     | ButcheryKnife  | 122                 |
| 6     | SkinKnife      | 38                  |
| 7     | Pickax         | 110                 |
| 9     | Pray           | 2                   |
| 19    | Empty slot     | 1,043               |

The empty slot is `15` on client 1784, where the Lua lists 15 names (`0`
BareHands to `14` Oar) followed by `__eCollectToolType_Count`, which puts
`__eCollectToolType_Count` if the values run on from `0`. On client 3474 it
is `19` while the Lua lists 16 names.

## Notes

- On client 3474, 564 of the 713 keys are `characterstatic.dbss`
  characters: 563 with `npc_kind` Collect and `18561` Pine Mushroom with
  `npc_kind` 2. The one Collect character without a row is `501` Test
  Object. The other 149 keys (`10003`, `10146`, `10701` and more) have no
  `characterstatic.dbss` row and no LOC type 6 name.
- 561 keys are the `character_key` of a `collectresourcename.dbss` model;
  152 keys have no model there.
- None of the 564 distinct drop keys on client 3474 is a group of
  `itemmaingroup.bss` or a subgroup of `itemsubgroup.dbss`, so the drops
  cannot be resolved from the client. 481 of them are keys of the
  `ItemMainGroup_Table` sheet of a private server on client 1784, where
  main group `10002` holds subgroup `10002` and three subgroups many
  gathering groups share.
- The tool slot fill follows the gathering kind: logging rows hold Axe and
  Syringe (`11983` Snowfield Cedar Tree), mining rows Pickax, tanning rows
  ButcheryKnife and SkinKnife.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `collectresourcename.dbss` as "gatherable identity
  and internal mesh names; no yields or rates". The row has no rate, but it
  holds the drop group per tool.

## Open Questions

### The 12 Bytes After The Drop Keys

`unknown_name_22` is 12 bytes that Layout 1 does not have, `0` on every row
of client 3474. The 2016 struct has nothing between `_collectItemDropKey`
and `_actionPoint`, and the client 1784 sheet has no column for it.
