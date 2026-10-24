# `fairypotion.dbss` Format

## Purpose

The potions a fairy can be set to use. The file holds one item list per
potion type: list `0` is the HP potions for the fairy's HP slot, lists `1`,
`2` and `3` the potions for the MP slot of classes that use MP, WP and SP.
`fairypotionoffset.dbss` is the type-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------- | -------------------------- |
| 1      | 1261 and later | 3483    | `fairypotion.dbss`       | 1,200 | 4 Potion List | 257 to 313, 299 on average |
| 1      | 1261 and later | 3483    | `fairypotionoffset.dbss` | 44    | 4 Offset Row  | 10                         |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `fairypotion.dbss`       | 1,200 B (100.0%) | 0 B (0.0%) |
| 1      | `fairypotionoffset.dbss` | 44 B (100.0%)    | 0 B (0.0%) |

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
| 1280   | No file  |
| 1276   | No file  |
| 1267   | Layout 1 |
| 1261   | Layout 1 |
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

| File                     | Required | Role                                                      |
| ------------------------ | -------- | --------------------------------------------------------- |
| `fairypotionoffset.dbss` | Optional | `potion_type -> (data_offset, data_size)` index           |
| `languagedata_en.loc`    | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`) |

Each list stores its own item count, so the handler walks the main file
without the offset companion.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field | Notes                |
| ------- | ------------------ | ----- | -------------------- |
| `+0x00` | u32                | count | Number of lists      |
| `+0x04` | Potion List[count] | lists | See Potion List      |

### Potion List (variable: 5 bytes + items)

| Offset          | Type             | Field       | Notes                                   |
| --------------- | ---------------- | ----------- | --------------------------------------- |
| `+0x00`         | u32              | item_count  | Number of item IDs that follow          |
| `+0x04`         | u32[item_count]  | item_ids    | Items the fairy may use for this type   |
| `item_ids+0x00` | u8               | potion_type | List key, see Potion Types              |

A list is `4 + 4 * item_count + 1` bytes. The key is the last byte of the
list, not the first, and the last list ends at the end of the file.

On client 3464 the file is 1,200 bytes: 4 lists stored in key order `3`, `2`,
`1`, `0` with 77, 77, 77 and 63 items (294 rows in the handler).

Every `item_id` has a zero top byte, so it reads the same as an item key with
enhancement level 0 (`_common/item_key.py`).

### `fairypotionoffset.dbss`

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `fairypotion.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u16  | potion_type | List key                                           |
| `+0x02` | u32  | data_offset | Absolute offset of the list's `item_count`         |
| `+0x06` | u32  | data_size   | Whole list, trailing `potion_type` byte included   |

There is no `PABR` magic and no trailer (`parse_bare_offset_rows`). Rows are
in the same order as the lists. Unlike most offset tables, `data_offset`
points at the start of the list, since the key sits at its end.

## Potion Types

| Type | Resource | Items on client 3464                                                       |
| ---- | -------- | -------------------------------------------------------------------------- |
| 0    | HP       | HP potions, Grain Juice, HP Spirit Essence items, Odore's Spirits         |
| 1    | MP       | MP, WP and SP potions, Herbal Juice, MP Spirit Essence items, Ornette's Spirits |
| 2    | WP       | The type `1` items with Odore's Spirits in place of Ornette's Spirits      |
| 3    | SP       | The type `2` items in the same order                                       |

Type `0` is HP: on client 3464 every named item in it is an HP item by its
English LOC name or description. The names of types `1` to `3` come from the
client Lua (see Notes); the lists themselves no longer tell them apart.

## Notes

- The Fairy Settings window (`panel_window_fairy_all_4.luac`,
  `PaGlobal_FairySetting_All`) has one HP slot and one MP slot. Its inventory
  list shows the items for which `ToClient_checkUsableFairyPotion(itemKey,
  classType)` is true. On a click, `ToClient_getFairyPotionType(itemKey,
  classType)` returns `-1` (message `LUA_FAIRYSETTING_NOT_ITEM`), `0` (HP
  slot) or another value (MP slot). Both calls take the player's class type,
  which fits one list per class resource.
- The same Lua file still holds hard-coded lists: `fairyMainPotionData[0]`
  (HP potions) and `fairySubPotionData[1]`, `[2]` and `[3]`. Index `1` holds
  MP potions and is the default; index `2` holds WP potions and is picked for
  the class types in its `spiritClass` table (0 Warrior, 11 Lahn, 12
  Berserker, 19 Striker, 20 Musa, 21 Maehwa, 23 Mystic, 25 Kunoichi, 26
  Ninja, 30 Woosa); index `3` holds SP potions and is picked for class type
  24 (Valkyrie). Indexes `2` and `3` also hold the Herbal Juice items. Only
  `isMP()` and `isHP()` read these tables, and they are passed `mpKeyStr`
  and `hpKeyStr`, which no fairy Lua file sets. The Resource names in this
  doc follow these indexes.
- On client 3464 every item of the Lua lists is in the matching list of this
  file except `[Savage] HP Potion (Extra Large)` (56093), which the Lua HP
  list has and list `0` lacks. Its MP counterpart (56094) is in lists `1` to
  `3`. The file lists add the Spirit Essence items, the Gourd Bottles (1041,
  1042) and others the Lua lists lack.
- Lists `1` to `3` each hold the MP, WP and SP potions together on client
  3464, while the Lua lists keep them apart (index `1` MP only, `2` WP only,
  `3` SP only).
- The two "Spirits" items are named the other way round from the two
  "Spirit Essence" items: Odore's Spirits (40734) and Ornette's Spirit
  Essence (40747) restore 550 HP, Ornette's Spirits (40733) and Odore's Spirit
  Essence (40713) restore 375 MP/WP/SP (English LOC item descriptions).
  List `0` and list `1` follow the descriptions; lists `2` and `3` hold
  Odore's Spirits (HP) and lack Ornette's Spirits.
- On client 3464, 26 rows have no English LOC item name: items 46901 and
  46907 in list `0`, and 46902 to 46904, 46908 to 46910, 720752 and 720753
  in each of lists `1` to `3`. The handler shows their item ID.

## Open Questions

### Potion Types 1 to 3

Type `0` is HP by its content. The MP, WP and SP names of types `1`, `2` and
`3` rest on the indexes of the Lua's `fairySubPotionData` table; the file
lists are near copies of each other, and the class-to-list choice happens in
`ToClient_getFairyPotionType`, which the Lua cannot show.

## In-Game Checks

### Ornette's Spirits for a WP Class

Needs item: [Ornette's Spirits](https://bdocodex.com/us/item/40733/)

Needs class: Warrior, or another class in the Lua's `spiritClass` list

Lists `2` and `3` lack Ornette's Spirits (MP/WP/SP) and hold Odore's Spirits
(HP) instead. Open the fairy's potion settings with Ornette's Spirits in the
inventory. If it is missing from the list on a Warrior but shows on an MP
class such as Sorceress, the client reads list `2` for WP classes, which
confirms type `2` as WP. If it shows on both, the client does not pick the
list by these types the way the Lua does.
