# `extractblackstone.bss` Format

## Purpose

What Black Stone extraction gives back for enhanced gear: per enhancement
difficulty (Easy, Normal, Hard), one entry per enhancement level for weapons
and one for armor, each with the item handed out and two counts. The
extraction window (`panel_window_extraction_blackstone_all_*.luac`) reads
it through `ToClient_GetExtractBlackStoneResultItemKey(isWeapon,
enchantDifficulty, enchantLevel)` and `ToClient_GetExtractBlackStoneResultCount`
with the same arguments.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------------------ | --------- |
| 1      | 3229 and later | 3483    | `extractblackstone.bss` | 2,308 | 108 Entry, 3 Group | 21        |

| Layout | File                    | Known         | Unknown         |
| ------ | ----------------------- | ------------- | --------------- |
| 1      | `extractblackstone.bss` | 580 B (25.1%) | 1,728 B (74.9%) |

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
| 3212   | No file  |
| 3203   | No file  |
| 3193   | No file  |
| 3186   | No file  |
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
| 3144   | No file  |
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
| 2995   | No file  |
| 2987   | No file  |
| 2978   | No file  |
| 2970   | No file  |
| 2959   | No file  |
| 2951   | No file  |
| 2942   | No file  |
| 2935   | No file  |
| 2932   | No file  |
| 2923   | No file  |
| 2919   | No file  |
| 2907   | No file  |
| 2900   | No file  |
| 2891   | No file  |
| 2882   | No file  |
| 2872   | No file  |
| 2863   | No file  |
| 2855   | No file  |
| 2849   | No file  |
| 2844   | No file  |
| 2834   | No file  |
| 2825   | No file  |
| 2819   | No file  |
| 2811   | No file  |
| 2803   | No file  |
| 2794   | No file  |
| 2783   | No file  |
| 2774   | No file  |
| 2765   | No file  |
| 2756   | No file  |
| 2750   | No file  |
| 2743   | No file  |
| 2736   | No file  |
| 2726   | No file  |
| 2717   | No file  |
| 2709   | No file  |
| 2703   | No file  |
| 2695   | No file  |
| 2684   | No file  |
| 2672   | No file  |
| 2665   | No file  |
| 2657   | No file  |
| 2649   | No file  |
| 2644   | No file  |
| 2637   | No file  |
| 2629   | No file  |
| 2619   | No file  |
| 2612   | No file  |
| 2606   | No file  |
| 2602   | No file  |
| 2601   | No file  |
| 2592   | No file  |
| 2583   | No file  |
| 2575   | No file  |
| 2567   | No file  |
| 2560   | No file  |
| 2553   | No file  |
| 2545   | No file  |
| 2538   | No file  |
| 2529   | No file  |
| 2519   | No file  |
| 2513   | No file  |
| 2510   | No file  |
| 2507   | No file  |
| 2503   | No file  |
| 2498   | No file  |
| 2492   | No file  |
| 2487   | No file  |
| 2480   | No file  |
| 2474   | No file  |
| 2468   | No file  |
| 2460   | No file  |
| 2453   | No file  |
| 2444   | No file  |
| 2438   | No file  |
| 2434   | No file  |
| 2429   | No file  |
| 2421   | No file  |
| 2414   | No file  |
| 2407   | No file  |
| 2401   | No file  |
| 2397   | No file  |
| 2393   | No file  |
| 2384   | No file  |
| 2378   | No file  |
| 2372   | No file  |
| 2358   | No file  |
| 2352   | No file  |
| 2347   | No file  |
| 2343   | No file  |
| 2335   | No file  |
| 2327   | No file  |
| 2324   | No file  |
| 2319   | No file  |
| 2313   | No file  |
| 2308   | No file  |
| 2302   | No file  |
| 2295   | No file  |
| 2290   | No file  |
| 2284   | No file  |
| 2276   | No file  |
| 2269   | No file  |
| 2259   | No file  |
| 2250   | No file  |
| 2243   | No file  |
| 2235   | No file  |
| 2229   | No file  |
| 2224   | No file  |
| 2218   | No file  |
| 2215   | No file  |
| 2207   | No file  |
| 2203   | No file  |
| 2196   | No file  |
| 2192   | No file  |
| 2189   | No file  |
| 2183   | No file  |
| 2179   | No file  |
| 2171   | No file  |
| 2163   | No file  |
| 2156   | No file  |
| 2151   | No file  |
| 2147   | No file  |
| 2142   | No file  |
| 2138   | No file  |
| 2134   | No file  |
| 2130   | No file  |
| 2122   | No file  |
| 2107   | No file  |
| 2098   | No file  |
| 2089   | No file  |
| 2081   | No file  |
| 2073   | No file  |
| 2067   | No file  |
| 2063   | No file  |
| 2059   | No file  |
| 2052   | No file  |
| 2044   | No file  |
| 2039   | No file  |
| 2032   | No file  |
| 2025   | No file  |
| 2011   | No file  |
| 2005   | No file  |
| 2000   | No file  |
| 1996   | No file  |
| 1991   | No file  |
| 1985   | No file  |
| 1980   | No file  |
| 1969   | No file  |
| 1964   | No file  |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
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

None. The handler names the result items through LOC type 0 and the item
icon index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                |
| ------- | ------------ | ------ | ------------------------------------ |
| `+0x00` | u32          | count  | Number of groups, one per difficulty |
| `+0x04` | Group[count] | groups | See Group                            |

The groups are not sorted: client 3474 stores difficulties 1, 2, 3 and
client 3251 3, 2, 1, with the same groups. On client 3474 the file is 4 +
3 x (12 + 36 x 21) = 2,308 bytes.

### Group (variable: 12 bytes + entries)

| Offset                | Type                 | Field          | Notes                                                        |
| --------------------- | -------------------- | -------------- | ------------------------------------------------------------ |
| `+0x00`               | u32                  | difficulty     | Enhancement difficulty, see Difficulties; unique             |
| `+0x04`               | u32                  | weapon_count   | Number of `weapon_entries`; `18` in every group of client 3474 |
| `+0x08`               | u32                  | armor_count    | Number of `armor_entries`; `18` in every group of client 3474 |
| `+0x0C`               | Entry[weapon_count]  | weapon_entries | What weapons give, see Entry                                 |
| `weapon_entries+0x00` | Entry[armor_count]   | armor_entries  | What armor gives, see Entry                                  |

### Entry (21 bytes)

| Offset  | Type | Field           | Notes                                                                       |
| ------- | ---- | --------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | enchant_level   | Enhancement level of the extracted gear; `1` to `18` in file order on client 3474 |
| `+0x01` | u32  | result_item_key | Item handed out, an item enchant key (`enchant_level << 24 \| item_id`), level `0` on every entry |
| `+0x05` | u64  | unknown_05      | A count; at least `unknown_0d` on every entry                               |
| `+0x0D` | u64  | unknown_0d      | A count                                                                     |

On client 3474 `result_item_key` is `16001` Black Stone for levels 1 to 15
and `16004` Concentrated Magical Black Stone for 16 to 18 (PRI to TRI).

## Difficulties

The developer comment on the `Difficulty` column of the `ExtractBlackStone`
sheet (a private server's `datasheet_contentsoptions.xlsm`, client 1784)
names `1` Easy, `2` Normal and `3` Hard. The item tooltip Lua
(`panel_tooltip_item.luac`) knows `__eEnchantDifficulty_None`, `_Easy`,
`_Normal`, `_Hard` and `_NotExtractHard`, and the extraction window turns
away gear of difficulty None or NotExtractHard, so those two have no group.

Entries of client 3474 for levels 8 and up:

| Level | Easy weapon | Easy armor | Normal weapon | Normal armor | Hard weapon | Hard armor |
| ----- | ----------- | ---------- | ------------- | ------------ | ----------- | ---------- |
| +8    | 8, 8        | 8, 8       | 9, 8          | 10, 8        | 9, 8        | 10, 8      |
| +9    | 9, 9        | 9, 9       | 10, 9         | 11, 9        | 11, 9       | 13, 10     |
| +10   | 10, 10      | 10, 10     | 12, 10        | 13, 10       | 12, 10      | 16, 13     |
| +11   | 11, 11      | 11, 11     | 14, 11        | 16, 12       | 16, 14      | 20, 15     |
| +12   | 12, 12      | 12, 12     | 16, 12        | 18, 14       | 20, 16      | 23, 18     |
| +13   | 13, 13      | 13, 13     | 17, 16        | 28, 21       | 22, 21      | 35, 27     |
| +14   | 14, 14      | 14, 14     | 28, 21        | 31, 25       | 35, 27      | 39, 32     |
| +15   | 15, 15      | 15, 15     | 34, 28        | 36, 31       | 43, 36      | 46, 39     |
| PRI   | 1, 1        | 1, 1       | 3, 2          | 3, 2         | 4, 2        | 4, 2       |
| DUO   | 2, 2        | 2, 2       | 5, 4          | 5, 4         | 6, 4        | 6, 4       |
| TRI   | 3, 3        | 3, 3       | 8, 7          | 8, 7         | 9, 7        | 9, 7       |

Each cell is `unknown_05, unknown_0d`. Below +8 both counts equal the level
in every group.

## Field Names

`difficulty` and the weapon and armor split follow the getters' arguments
(`isWeapon`, `enchantDifficulty`, `enchantLevel`), `result_item_key` the
getter `ToClient_GetExtractBlackStoneResultItemKey`. Neither the 2016 PDB nor
the client 1784 PAZ has the file (clients 3251 and 3474 have it).

The `ExtractBlackStone` sheet of a private server's `DataSheets.bexcel` on
client 1784 is the server-side table of the older extraction: per difficulty
several rows with a `Rate` weight and one count per column (`Weapon8` to
`Weapon15`, `Armor6` to `Armor15`, all `%` server-only). Read with the first
entry list as weapons, `unknown_0d` equals the smallest count of that
column on 52 of the 54 entries for levels the sheet has (34 of 36 outside
Easy, where every row holds the level), and `unknown_05` is at most its
largest count on all 54. Read with the lists swapped, 30 of 54 match. The
first list is the weapon list.

## Notes

- `weapon_count` and `armor_count` both sit before the two lists; the
  armor list starts right after the last weapon entry.
- The extraction window shows `?` when `ToClient_GetExtractBlackStoneResultCount`
  returns `0`, and needs gear whose `ToClient_GetExtractBlackStoneResultItemKey`
  is not `__eItemKeyUndefined`.

## In-Game Checks

### Which Count the Extraction Window Shows

Needs item: any weapon at +15 whose tooltip reads Enhancement Difficulty:
Hard

Open the Black Spirit's Extraction window, pick Black Stone extraction and
place the weapon (do not confirm). The window shows the Black Stone count
it gives. `43` means it shows `unknown_05` (the larger count); `36` means
it shows `unknown_0d`; a number in between means neither is the shown
count and the two are the limits of a random range.
