# `growthpasscategory.dbss` Format

## Purpose

The tabs of the Growth Pass window (`panel_window_growthpass*.luac`): per category a key, a Korean name, an icon texture key and the quest chain its grid holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records                 | Row bytes                        |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------------- | -------------------------------- |
| 2      | 1680 and later | 3483    | `growthpasscategory.dbss`       | 251   | 2 Record Body, 2 Record | 87 to 152, 120 on average        |
| 2      | 1680 and later | 3483    | `growthpasscategoryoffset.dbss` | 28    | 2 Offset Row            | 12                               |
| 1      | 1717 to 2545   | 2545    | `growthpasscategory.dbss`       | 8,409 | 8 Record Body, 8 Record | 1,042 to 1,052, 1,047 on average |
| 1      | 1717 to 2545   | 2545    | `growthpasscategoryoffset.dbss` | 100   | 8 Offset Row            | 12                               |

| Layout | File                            | Known          | Unknown         |
| ------ | ------------------------------- | -------------- | --------------- |
| 2      | `growthpasscategory.dbss`       | 211 B (84.1%)  | 40 B (15.9%)    |
| 2      | `growthpasscategoryoffset.dbss` | 28 B (100.0%)  | 0 B (0.0%)      |
| 1      | `growthpasscategory.dbss`       | 569 B (6.8%)   | 7,840 B (93.2%) |
| 1      | `growthpasscategoryoffset.dbss` | 100 B (100.0%) | 0 B (0.0%)      |

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
| 3412   | No documented layout |
| 3402   | No documented layout |
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
| 1710   | No file              |
| 1704   | No file              |
| 1698   | Layout 2             |
| 1690   | Layout 2             |
| 1685   | Layout 2             |
| 1680   | Layout 2             |
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

| File                            | Required | Role                                                             |
| ------------------------------- | -------- | ---------------------------------------------------------------- |
| `growthpasscategoryoffset.dbss` | Required | `category_key -> (offset, size)` of each record body             |
| `texturestring_combine.xml`     | Optional | Sprite sheet and rectangle of `icon_texture`                     |
| `languagedata_en.loc`           | Optional | Category name, LOC type 107 `str_id1 = category_key`             |

The grid of each category is in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), keyed by the same `category_key`.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type                 | Field        | Notes              |
| ------- | -------------------- | ------------ | ------------------ |
| `+0x00` | u32                  | record_count | `2` on client 3464 |
| `+0x04` | Record[record_count] | records      | See Record         |

### Record (variable: 4 bytes + body)

| Offset  | Type        | Field | Notes                               |
| ------- | ----------- | ----- | ----------------------------------- |
| `+0x00` | u32         | key   | Copy of the record's key            |
| `+0x04` | Record Body | body  | The offset row points at this field |

### Record Body (variable: 42 bytes + name and icon text)

The offset table points at the body, past the key copy.

| Offset              | Type      | Field           | Notes                                                                |
| ------------------- | --------- | --------------- | -------------------------------------------------------------------- |
| `+0x00`             | u32       | category_key    | Same as the key copy before it and the offset row key                |
| `+0x04`             | str16     | name_kr         | Length in characters, then the text; keeps `<PAColor>` tags          |
| `name_kr+0x00`      | str8      | icon_texture    | Length in bytes, then a `texturestring_combine.xml` texture ID       |
| `icon_texture+0x00` | u16       | quest_chain_id  | The quest chain of this category's grid                              |
| `icon_texture+0x02` | bytes[20] | unknown_tail_02 | Zero on both records                                                 |

Both strings carry a u64 length prefix, read with `RecordReader.text`.

### `growthpasscategoryoffset.dbss`

No `PABR` magic and no trailer: a u32 row count, then rows of u32 `category_key`, u32 `offset`, u32 `size`, read by `parse_bare_u32_offset_rows`. On client 3464: key 7 at `8`, 87 bytes; key 9 at `99`, 152 bytes. Sorted by offset, the key copies and bodies fill the file after the count.

| Offset  | Type                  | Field     | Notes                 |
| ------- | --------------------- | --------- | --------------------- |
| `+0x00` | u32                   | row_count | Number of offset rows |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                              |
| ------- | ---- | ------------ | ---------------------------------- |
| `+0x00` | u32  | category_key | Record key                         |
| `+0x04` | u32  | offset       | Absolute offset of the record body |
| `+0x08` | u32  | size         | Size of the record body            |

## Layout 1

Client 1784 record bodies end in 980 bytes after `quest_chain_id`, where
client 3473 has 20. Only the Record Body differs from Layout 2.

### Record Body (variable: 1002 bytes + name and icon text)

| Offset              | Type       | Field           | Notes                                                                 |
| ------------------- | ---------- | --------------- | --------------------------------------------------------------------- |
| `+0x00`             | u32        | category_key    |                                                                       |
| `+0x04`             | str16      | name_kr         |                                                                       |
| `name_kr+0x00`      | str8       | icon_texture    |                                                                       |
| `icon_texture+0x00` | u16        | quest_chain_id  | 4464 to 4471 on the eight records of client 1784                      |
| `icon_texture+0x02` | bytes[980] | unknown_tail_02 | Starts with u32 `5` on every record of client 1784; mostly zero after |

## Category Keys

`panel_window_growthpass.luac` sets `_hyperBoostCategoryKeyList = {9}`: the window sorts Hyper Boost categories first, then the rest in file order. It reads the name through `categoryWrapper:getCategoryName()` and the icon through `getIconTextureId()`.

LOC type 107 names keys 1 to 9 (`Quest/`, `PvE`, `Gathering`, `Farming/`, `Hunting/`, `Training`, `Game Tips`, `Guaranteed`, `HYPERBOOST`), but only 7 and 9 have a record on client 3464. `growthpassquestlist.bss` holds nine quest chains, 4464 to 4472; on client 3464 only 4470 and 4472 belong to a category.

## Notes

- Decompressed sizes on client 3464: `251` bytes, offset companion `28` bytes.
- calpheonlabs has no page for this table.
- `test_handler.py` checks that the records fill the file and that every icon key resolves; the layout tests check that each grid's quests are the chain its category names.

## Open Questions

### Unknown Tail

The 20 bytes after `quest_chain_id` are zero on both records. `ToClient_requestCategoryRewardItem(categoryKey, rewardIndex)` in `panel_window_growthpass_2.luac` claims a category reward, so a reward list could live here when a category has one; no record shows it.
