# `itemexchangetoclass.dbss` Format

## Purpose

The weapon exchange groups behind the Weapon Exchange window
(`Panel_Window_ChangeItem_All`): each row is one group of equivalent
weapons, such as the Rusty weapons (key `1`) or the Tuvala main weapons
(key `165`), with one item key per class type. Exchanging an item for
another class gives the item in that class's slot of the item's group.
`itemexchangetoclassoffset.dbss` is the index into it, and
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) maps
each item back to its group.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ------ | -------------- | --------- |
| 2      | 3381 and later | 3483    | `itemexchangetoclass.dbss`       | 39,404 | 200 Row        | 197       |
| 2      | 3381 and later | 3483    | `itemexchangetoclassoffset.dbss` | 2,404  | 200 Offset Row | 12        |
| 1      | 1622 to 2243   | 2243    | `itemexchangetoclass.dbss`       | 26,171 | 191 Row        | 137       |
| 1      | 1622 to 2243   | 2243    | `itemexchangetoclassoffset.dbss` | 2,296  | 191 Offset Row | 12        |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 2      | `itemexchangetoclass.dbss`       | 39,404 B (100.0%) | 0 B (0.0%) |
| 2      | `itemexchangetoclassoffset.dbss` | 2,404 B (100.0%)  | 0 B (0.0%) |
| 1      | `itemexchangetoclass.dbss`       | 26,171 B (100.0%) | 0 B (0.0%) |
| 1      | `itemexchangetoclassoffset.dbss` | 2,296 B (100.0%)  | 0 B (0.0%) |

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
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No documented layout |
| 3267   | No documented layout |
| 3258   | No documented layout |
| 3251   | No documented layout |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
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
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
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

| File                             | Required | Role                                                                |
| -------------------------------- | -------- | ------------------------------------------------------------------- |
| `itemexchangetoclassoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |
| `languagedata_en.loc`            | Optional | Class name (type `21`, `str_id1` = class type) and item name (type `0`, `str_id1` = item ID) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `200` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (197 bytes)

| Offset  | Type    | Field         | Notes                                                            |
| ------- | ------- | ------------- | ---------------------------------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                                        |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row; the offset file points here         |
| `+0x08` | u32[47] | item_keys     | Item key (`enchant_level << 24 \| item_id`) per class type, index = class type; `0` for a class without an item |
| `+0xC4` | u8      | exchange_type | See Exchange Types                                               |

The rows are not sorted by key: on client 3474 they start `203`, `202`,
`201` and run down in runs that restart higher (`192` is followed by
`219`).

### `itemexchangetoclassoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemexchangetoclass.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                      |
| ------- | ---- | ----------- | ---------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                                |
| `+0x04` | u32  | data_offset | Row start + 4, at `key_dup`                                |
| `+0x08` | u32  | data_size   | The row without its leading `key`: `193` on client 3474    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are not in file order (`139`, `203`, `138`, `202` on client
3474); on clients 1784 and 3474 every index row points at the row with its
key.

## Layout 1

On client 1784 the row holds 32 class slots where Layout 2 has 47, and
`data_size` is `133`. The file has 171 rows.

### Row (137 bytes)

| Offset  | Type    | Field         | Notes                                    |
| ------- | ------- | ------------- | ---------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row              |
| `+0x08` | u32[32] | item_keys     | Item key per class type, index = class type |
| `+0x88` | u8      | exchange_type | See Exchange Types                       |

## Class Slots

The slot index is the class type `getClassType()` returns, so slot `0` is
Warrior, `4` Ranger, `8` Sorceress and `32` Seraph: in every row the class
whose LOC type 21 name matches the item's weapon (Hashashin a Shamshir,
Sage a Kyve, Lahn a Crescent Pendulum). On client 3474 the rows fill class
types 0 to 35 without 13, 14, 18 and 22, the same set as
`PLAYABLE_CLASSES_MASK` in `_common/class_type.py`; slots 36 to 46 are `0`
in every row. Classes that share a weapon share the item: Musa (`20`) and
Maehwa (`21`) both get `13301` Rusty Blade in row `1`.

An item key carries no enhancement level in any row on clients 1784 and
3474 (every `item_keys` value is below `1 << 24`).

## Exchange Types

| Value | Meaning      | Rows on client 3474                             |
| ----- | ------------ | ----------------------------------------------- |
| `0`   | Normal item  | 191                                             |
| `1`   | Season item  | 9: `105` to `107`, `165` to `167`, `170` to `172` |

The names come from the developer note on the `ExchangeType` column of the
`Item_Exchange` sheet in a private server's `.xlsm` on client 1784: the
column tells whether a group is exchanged with a normal weapon exchange
coupon or a season one. Both coupons use `ContentsEventType` `38`
(`ContentsType_ItemExchangeToClass` in the client 3474 Lua enum) and
`ContentsEventParam1` `-1`; `ContentsEventParam2` `0`, `1` and `2` (main,
awakening, sub-weapon) are the normal coupons, `3`, `4` and `5` the season
ones. The client data agrees: rows `165` to `167` hold the Tuvala main,
sub-weapon and awakening weapons and rows `170` to `172` Combatant's
Tuvala weapons, both season server gear.

## Field Names

The row is the 2016 `gc::ItemExchangeToClassStaticStatus`: `_key`
(`gc::KeyType<int,0>`, an i32) and `_itemKey`, a `pa::Array` of 32
`gc::ItemEnchantKey`. The file writes the key before the struct as the
index key and again as `_key`. The 2016 struct has no exchange type; the
`ItemExchangeToClassStaticStatusManager` around it also holds
`_mapKeyFromItemKey`, the item to group map that
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) stores.

The values match the `Item_Exchange` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`. Its item columns are named
`ClassType0` to `ClassType32` after the class type, each followed by a note
column with the Korean class name; slot `n` matches the column
`ClassTypeN`. The sheet lists `ClassType26` and `ClassType27` twice, an
empty pair first, and the second pair matches.

| Field         | Column                           | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------------- | ------------------------ | ------------------------ |
| key           | `Index`                          | 171 of 171 rows          | 167 of 171 sheet rows    |
| item_keys     | `ClassType0` to `ClassType32`    | 170 of 171               | 161 of 167 shared rows   |
| exchange_type | `ExchangeType`                   | 171 of 171               | 164 of 167               |

- Client 1784 row `171` holds no item, while the sheet lists the Godr-Ayed
  sub-weapons (`738301` up).
- On client 3474 the sheet rows `173` to `176` have no row, and the 33
  rows `177` to `219` have none in the sheet. The 161 matching rows also
  fill class types the sheet leaves empty (3 Wukong, 6 Scholar, 7
  Drakania, 15 Maegu, 30 Woosa, 32 to 35); the comparison skips those. The
  six other rows are `105` to `107`, which the sheet fills with the Tuvala
  weapons `694113` up and client 3474 empties, and `170` to `172`, which
  hold Godr-Ayed sub-weapons and type `0` in the sheet and Combatant's
  Tuvala weapons and type `1` on client 3474.

## Notes

- The Weapon Exchange window Lua (`panel_window_changeitem_all_1.luac` and
  `_2.luac`) opens on `FromClient_UseItemExchangeToClass`, asks
  `getExchangeItem()` for the result of each inventory item and exchanges
  with `exchangeItemToClass()`; it reads no table field itself. The coupon's
  `getContentsEventParam1()` picks the target class, `-1` meaning the
  player's own class.
- On client 3474 rows `105` and `106` hold no item, and row `107` only
  `695193` Tuvala Pendant at class type 35 (Agent), which row `167` holds
  in the same slot. `931802` Ultimate Krea Clavis sits in rows `68` and
  `71` at class type 32. These two are the only items in two rows.
