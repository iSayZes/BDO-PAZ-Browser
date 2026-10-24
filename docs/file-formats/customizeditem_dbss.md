# `customizeditem.dbss` Format

## Purpose

Item lists for boxes that give a different item to each character: an item
whose contents event is `31 CustomizedItemBox` (`itemenchant.dbss`
`contents_event_type`) names one record here by its
`contents_event_param1`, and the record lists condition scripts with the item
each one gives. Most conditions are `checkClass(N);`, so an outfit or weapon
box hands out the version for the opening character's class. The pearl shop
Lua (`panel_ingamecashshop_setequip.luac`,
`panel_pearlshop_displaycontroller.luac`) reads a record through
`ToClient_getCustomizedItemStaticStatusWrapper(CustomizedItemKey(itemSSW:getContentsEventParam1()))`
and takes `getMatchedItem()`, the item for the current character, to preview
the box contents.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes   | Records                 | Row bytes               |
| ------ | -------------- | ------- | --------------------------- | ------- | ----------------------- | ----------------------- |
| 1      | 1346 and later | 3483    | `customizeditem.dbss`       | 763,556 | 18,295 Item, 879 Record | 40 to 54, 41 on average |
| 1      | 1346 and later | 3483    | `customizeditemoffset.dbss` | 8,794   | 879 Index Row           | 10                      |

| Layout | File                        | Known              | Unknown    |
| ------ | --------------------------- | ------------------ | ---------- |
| 1      | `customizeditem.dbss`       | 763,556 B (100.0%) | 0 B (0.0%) |
| 1      | `customizeditemoffset.dbss` | 8,794 B (100.0%)   | 0 B (0.0%) |

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

| File                        | Required | Role                                                                                      |
| --------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `customizeditemoffset.dbss` | Optional | `customized_item_key -> (data_offset, data_size)` index, see below; the records can be walked without it |
| `languagedata_en.loc`       | Optional | Item names (LOC type 0), class names (LOC type 21) and quest titles (LOC type 18) for the view |
| `itemenchant.dbss`          | Optional | The box items that open each record, for the Boxes column; the handler reads them from the `CUSTOMIZED_ITEM_BOXES` lookup index, not as a companion |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `879` on client 3482         |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record |

### Record (variable: 8 bytes + items)

| Offset         | Type              | Field                   | Notes                                                                          |
| -------------- | ----------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00`        | u16               | customized_item_key     | The record key, the `contents_event_param1` of the box items that open it      |
| `+0x02`        | u32               | item_count              | Number of `items`; the index's `data_offset` points here                       |
| `+0x06`        | Item[item_count]  | items                   | Condition and item pairs in sheet column order; see Item                       |
| `items+0x00`   | u16               | customized_item_key_dup | Equal to `customized_item_key` in every record (clients 1784 and 3482)         |

### Item (variable: 12 bytes + condition text)

| Offset           | Type  | Field     | Notes                                                                                  |
| ---------------- | ----- | --------- | -------------------------------------------------------------------------------------- |
| `+0x00`          | str16 | condition | Condition script, see Conditions                                                       |
| `condition+0x00` | u32   | item_key  | Packed item key, `enchant_level << 24 \| item_id`: the item and enhancement level given |

### `customizeditemoffset.dbss`

| Offset  | Type             | Field | Notes                                   |
| ------- | ---------------- | ----- | --------------------------------------- |
| `+0x00` | u32              | count | Equals the `customizeditem.dbss` count  |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row     |

### Index Row (10 bytes)

| Offset  | Type | Field               | Notes                                               |
| ------- | ---- | ------------------- | --------------------------------------------------- |
| `+0x00` | u16  | customized_item_key | Record key                                          |
| `+0x02` | u32  | data_offset         | Record start + 2, at `item_count`                   |
| `+0x06` | u32  | data_size           | Record size - 2, through `customized_item_key_dup`  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The rows are
not in file order; on clients 1784 and 3482 every row matches the record
walked from the start of the file.

## Field Names

The record is the `CustomizedItemList` sheet of a private server's
`DataSheets.bexcel` on client 1784: `CustomizedItemKey`, then up to 25
column triples `ConditionN`, `ItemN` and `EnchantN`. The file stores one
item per filled `ConditionN` and packs `EnchantN` into the top byte of
`ItemN`. The 2016 `gc::CustomizedItemStaticStatus` has the same shape:
`_itemList` (a vector of `gc::CustomizedItem` with `_conditionString` and the
`gc::ItemEnchantKey` `_itemKey`), then the u16 `_key`, which is
`customized_item_key_dup`; the leading `customized_item_key` is the map key.

| Field               | Column                    | Match                                                                                   |
| ------------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| customized_item_key | `CustomizedItemKey`       | 410 of 410 keys are sheet keys (client 1784), 483 of 879 (client 3482)                 |
| condition           | `ConditionN`              | Same pairs in the same order on 384 of 410 shared keys (client 1784), 38 of 483 (client 3482) |
| item_key            | `ItemN \| EnchantN << 24` | Compared with `condition` as pairs                                                      |

On client 3482, 279 of the 445 shared records that differ keep the sheet's
pairs as their first entries and add pairs behind them for class types the
sheet has none for (`3`, `6`, `7`, `15`, `30`, `32` to `35`). The other 166
differ from the private server's sheet in their items or conditions.

## Conditions

Two script forms occur, counted on client 3482 (18,295 entries):

| Script                      | Entries | Meaning in the view                                                       |
| --------------------------- | ------- | ------------------------------------------------------------------------- |
| `checkClass(N);`            | 18,292  | Class type `N` (`getClassType()`, LOC type 21 name)                       |
| `clearquest(chain,quest);`  | 3       | Quest done, LOC type 18 title; record `497`, three `[Crossroad]` quests  |

Record `497` is the Mysterious Secret Note (item `66297`): it gives the
Secret Dispatch: The Giving Tree item `66298`, `66299` or `66300` after
quest `22226` part `20`, `21` or `22` ([Crossroad] For Calpheon, For
O'dyllita, For Power).

## Notes

- `item_count` runs from 1 to 32 on client 3482; 304 of the 879 records
  hold 32 entries, one per playable class type (0 to 35 without 13, 14, 18
  and 22).
- 84 records on client 3482 give the same item to every condition.
- Five records (`31`, `32`, `34`, `35`, `42`) list `checkClass(15);` twice
  with the same item on client 3482.
- 4,660 of the 18,295 items on client 3482 carry an enhancement level above
  0 in the top byte, 3,033 of them PRI to PEN (16 to 20).
- On client 3482, 754 `itemenchant.dbss` items have contents event `31`;
  731 of their 740 distinct `contents_event_param1` values are keys here.
  The nine others (`536`, `60013`, `60016`, `60025`, `60113`, `60116`,
  `60119`, `60122`, `60125`) have no record, and 148 records have no box item.
  The `CUSTOMIZED_ITEM_BOXES` lookup index turns `contents_event_param1`
  around: the Boxes column lists the items that open each record, and the
  `itemenchant.dbss` Event Param 1 of a box item links to its record here.
- Client 1784 has 410 records with keys 1 to 485 and the same layout.

## Open Questions

### Boxes Without a Record

Nine `contents_event_param1` values of `CustomizedItemBox` items have no
record on client 3482 (listed in Notes). The items are Awakening Secret Book
Box (65297, `536`), three Enduring Crow Main Weapon Boxes (950323, 950326,
950335: `60013`, `60016`, `60025`) and five Enduring Crow Awakening Weapon
Boxes (950423 to 950435: `60113` to `60125`). No client Lua shows what opening
such a box does: only `panel_ingamecashshop_setequip.luac` and
`panel_pearlshop_displaycontroller.luac` read a record, and
`getMatchedItem()` is only read after a `nil` check of the wrapper.
