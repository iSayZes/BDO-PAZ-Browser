# `itemimprovement.dbss` Format

## Purpose

Gear Reform (`LUA_IMPROVEMENT_TITLE` "Reform"): the Black Spirit window where
a piece of gear and a reform stone turn into the next grade of that gear. A
record names the result and the gear it is made from, and a reform group that
ties it to the stones of
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes   | Records         | Row bytes               |
| ------ | -------------- | ------- | ---------------------------- | ------- | --------------- | ----------------------- |
| 2      | 3258 and later | 3483    | `itemimprovement.dbss`       | 174,276 | 3,904 Record    | 29 to 45, 45 on average |
| 2      | 3258 and later | 3483    | `itemimprovementoffset.dbss` | 46,852  | 3,904 Index Row | 12                      |
| 1      | 1346 to 2498   | 2498    | `itemimprovement.dbss`       | 121,142 | 3,274 Record    | 37                      |
| 1      | 1346 to 2498   | 2498    | `itemimprovementoffset.dbss` | 39,292  | 3,274 Index Row | 12                      |

| Layout | File                         | Known             | Unknown          |
| ------ | ---------------------------- | ----------------- | ---------------- |
| 2      | `itemimprovement.dbss`       | 127,428 B (73.1%) | 46,848 B (26.9%) |
| 2      | `itemimprovementoffset.dbss` | 46,852 B (100.0%) | 0 B (0.0%)       |
| 1      | `itemimprovement.dbss`       | 108,046 B (89.2%) | 13,096 B (10.8%) |
| 1      | `itemimprovementoffset.dbss` | 39,292 B (100.0%) | 0 B (0.0%)       |

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

| File                              | Required | Role                                                     |
| --------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementoffset.dbss`      | Optional | `key -> (data_offset, data_size)` index, see below; the handler walks the records without it |
| `itemimprovementsource.dbss`      | Optional | The reform stones, see [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type           | Field   | Notes                                                       |
| ------- | -------------- | ------- | ----------------------------------------------------------- |
| `+0x00` | u32            | count   | Number of records; `3,904` on client 3464                   |
| `+0x04` | Record[count]  | records | Back to back to the end of the file; see Record             |

### Record (variable: 25 bytes + item IDs)

| Offset           | Type             | Field          | Notes                                                    |
| ---------------- | ---------------- | -------------- | -------------------------------------------------------- |
| `+0x00`          | u32              | key            | Record key, `1` to `4,949` with gaps; the index's `data_offset` points past it |
| `+0x04`          | u64              | item_count     | `5` or `1`                                               |
| `+0x0C`          | u32[item_count]  | item_ids       | `item_count` item IDs, see below                         |
| `item_ids+0x00`  | u8               | unknown_tail_0 | `0` in every record                                      |
| `item_ids+0x01`  | u8               | group          | Reform group, `1` to `37`; matches `group` of the stones |
| `item_ids+0x02`  | bytes[11]        | unknown_tail_2 | All `0` in every record                                  |

With 5 items, `item_ids[0]` is the result and `item_ids[1]` to `[4]` the input
gear, the same ID four times in all 3,816 such records (client 3464).
Kharazad Necklace (`11697`) to Dawnbound Kharazad Necklace (`11698`) is
stored as `[11698, 11697, 11697, 11697, 11697]`, and Kutum Clavis (`743327`)
to Earthshaking Kutum Clavis (`737423`) as `[737423, 743327 x4]`. The 88
records with 1 item hold 87 Tuvala items, mostly in groups 3, 4 and 5 (Tuvala
Clavis `695190` in groups 4 and 5); see Open Questions.

An item can be the input of several records with different groups and
results; 1,528 items are a result in one record and an input in another.

### `itemimprovementoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `itemimprovement.dbss` count    |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row        |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | key         | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `key`            |
| `+0x08` | u32  | data_size   | Record size - 4: `41` or `25`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3464 every row matches the record walked
from the start of the file.

## Layout 1

Client 1784 records end in 3 bytes after `group`, where client 3473 has 11.
Only the Record differs from Layout 2.

### Record (variable: 17 bytes + item IDs)

| Offset          | Type            | Field          | Notes                                       |
| --------------- | --------------- | -------------- | ------------------------------------------- |
| `+0x00`         | u32             | key            |                                             |
| `+0x04`         | u64             | item_count     | `5` in all 2,081 records on client 1784     |
| `+0x0C`         | u32[item_count] | item_ids       |                                             |
| `item_ids+0x00` | u8              | unknown_tail_0 |                                             |
| `item_ids+0x01` | u8              | group          |                                             |
| `item_ids+0x02` | bytes[3]        | unknown_tail_2 | All `0` in every record (client 1784)       |

## Notes

- The window is `panel_improvement_all` (`Panel_Window_Improvement_All`). It
  lists gear whose item static status says `isImprovable()`, and stones that
  `getImproveInformation():checkIsValidSubItem(slot)` accepts; both checks run
  in the client, so the Lua does not show how a stone is matched to gear.
- The window text: "You can use Reform Stones to level up gear to the next
  grade. The higher the grade of the Reform stone, the higher the chances of
  acquiring higher grade gear." (`LUA_IMPROVEMENT_DESC_RENEW`).
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  (`internal/tables/itemimprovement.go`) reads the record body as `u32 disc`,
  `u32 0`, result, four bases, a `flag` that is "always N x 256" and 9 zero
  bytes, and drops the 25-byte records. Its `disc` and `0` are the u64
  `item_count` (`5` or `1`, the number of IDs that follow), and its `flag` is
  `group` read as a u32 from one byte early: `0x2100` is group `33`.

## Open Questions

### Which Stone a Record Takes

Several stones share a `group`; they differ in `category` (see
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md)). Mapping the
input gear's `itemenchant.dbss` `category` byte (`+0x05`) to a stone category,
`1` and `2` (weapons) to `1`, `3` (armor) to `2`, `4` (accessories) to `3` and
`0` (alchemy stones) to `4`, every one of the 3,904 records (client 3464) has
a stone with its group and that category, and the names agree: Behelit's
Heart (`761877`, group 3) meets Crimson Behelit Alchemy Stone Appearance
(category 4, group 3). Whether the client matches by this pair, and what
stone category `5` (Flawless Herald's Crystal) takes, is open.

### Records With One Item

The 88 records with one item ID name Tuvala gear and no result. Groups 3, 4
and 5 are also the groups of the `[Season] Tuvala ... Conversion Stone`
items, so these may be conversions whose result is not one fixed item. What
the client does with them is open.

### The 13-Byte Tail

Only byte `+1` (`group`) is ever non-zero.
