# `alchemystonechange.dbss` Format

## Purpose

The Growth recipes for items that grow into a higher tier: alchemy stones,
Vell's and Khan's Hearts and Behelit's Hearts with Brimming Essence of Aether
at Alchemy Apprentice 1, and Totems of the Sea with a Black Stone at a
Fishing level. A row is the item, its Growth material and count, the life
skill condition as an inline script, and the item it grows into.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | ------------- | --------- |
| 2      | 3045 and later | 3483    | `alchemystonechange.dbss`       | 12,506 | 133 Row       | 94        |
| 2      | 3045 and later | 3483    | `alchemystonechangeoffset.dbss` | 1,600  | 133 Index Row | 12        |
| 1      | 1346 to 2717   | 2717    | `alchemystonechange.dbss`       | 13,732 | 176 Row       | 78        |
| 1      | 1346 to 2717   | 2717    | `alchemystonechangeoffset.dbss` | 2,116  | 176 Index Row | 12        |

| Layout | File                            | Known            | Unknown         |
| ------ | ------------------------------- | ---------------- | --------------- |
| 2      | `alchemystonechange.dbss`       | 8,782 B (70.2%)  | 3,724 B (29.8%) |
| 2      | `alchemystonechangeoffset.dbss` | 1,600 B (100.0%) | 0 B (0.0%)      |
| 1      | `alchemystonechange.dbss`       | 10,916 B (79.5%) | 2,816 B (20.5%) |
| 1      | `alchemystonechangeoffset.dbss` | 2,116 B (100.0%) | 0 B (0.0%)      |

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

None. The handler reads the rows in file order and does not need
`alchemystonechangeoffset.dbss` (see below). Item names come from LOC type 0
and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `133` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (variable: 56 bytes + condition text)

A fixed head, an inline condition script and a 12-byte tail. Every
condition on client 3464 is 19 characters long, so every row is 94 bytes
there; a reader takes the length from the count of `condition`.

| Offset           | Type      | Field            | Notes                                                    |
| ---------------- | --------- | ---------------- | -------------------------------------------------------- |
| `+0x00`          | u32       | key              | Row key; equals `item_id` on every row                   |
| `+0x04`          | u32       | item_id          | The item that grows; unique per row                      |
| `+0x08`          | u32       | unknown_08       | `0` on every row (client 3464)                           |
| `+0x0C`          | u32       | material_item_id | Growth material                                          |
| `+0x10`          | u32       | material_count   | Material units one Growth attempt takes                  |
| `+0x14`          | bytes[16] | unknown_14       | All zero on every row (client 3464)                      |
| `+0x24`          | str16     | condition        | Client condition script, see Conditions                  |
| `condition+0x00` | u32       | result_item_id   | The item a successful Growth gives; `0` on Totem rows    |
| `condition+0x04` | u32       | unknown_tail_04  | Falls with the stone tier; see Open Questions            |
| `condition+0x08` | u32       | unknown_tail_08  | `0` on every row (client 3464)                           |

On client 3464 the rows fall into two families:

| Rows | Items                                                                 | Material                          | material_count   | condition              |
| ---- | --------------------------------------------------------------------- | --------------------------------- | ---------------- | ---------------------- |
| 53   | Alchemy stones (45201 Imperfect to 45292 Splendid), Blessed and Exalted alchemy stones (768181 to 768512), Vell's, Khan's and Behelit's Hearts (761839 to 761876) | 821322 Brimming Essence of Aether | `2` to `30`      | `getLifeLevel(4)>10;`  |
| 80   | Totems of the Sea (54201 to 54292)                                    | 16001 Black Stone                 | `1`              | `getLifeLevel(1)>30;`, `>40;` or `>50;` |

`material_count` and `unknown_tail_04` follow the tier the stone grows into
(client 3464):

| Growth                | material_count | unknown_tail_04 |
| --------------------- | -------------- | --------------- |
| Imperfect to Sturdy   | `2`            | `455000`        |
| Sturdy to Sharp       | `3`            | `176000`        |
| Sharp to Resplendent  | `10`           | `31400`         |
| Resplendent to Splendid | `20`         | `12000`         |
| Splendid to Shining   | `30`           | `3870`          |

The Blessed, Exalted and Heart chains use the same pairs for the same tier
step. Imperfect stones grow straight to Sturdy (45201 to 45216, 45233 to
45248, 45265 to 45280); no row starts at a Rough stone.

### `alchemystonechangeoffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first three keys are 768512, 54205,
768189 where the main file has 768512, 768189, 768188).

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                    |
| ------- | ---- | ------- | -------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key, the main row's `key`                            |
| `+0x04` | u32  | offset  | Start of the row in `alchemystonechange.dbss` plus 4, at its `item_id` |
| `+0x08` | u32  | size    | Row length minus the 4-byte `key`; `90` on every row (client 3464) |

## Layout 1

On client 1784 the row has a u16 at `+0x08` where Layout 2 has a u32, 14
bytes of unknown fields before `condition` where Layout 2 has 16, and no
12-byte tail after `condition`. Only the Row differs from Layout 2.

### Row (variable: 40 bytes + condition text)

The index row `size` is `36` for a row with an empty `condition` and `74`
for one with a 19-character condition (client 1784).

| Offset  | Type     | Field            | Notes                                                            |
| ------- | -------- | ---------------- | ---------------------------------------------------------------- |
| `+0x00` | u32      | key              |                                                                  |
| `+0x04` | u32      | item_id          |                                                                  |
| `+0x08` | u16      | unknown_old_08   | `0` on Totem rows, an id near `item_id + 800` on alchemy stone rows |
| `+0x0A` | u32      | material_item_id | `16001` Black Stone on every row (client 1784)                   |
| `+0x0E` | u32      | material_count   | `1` or `50` (client 1784)                                        |
| `+0x12` | bytes[8] | unknown_12       | All zero on every row (client 1784)                              |
| `+0x1A` | u32      | unknown_1a       | `0`, `700000` or `850000` (client 1784)                          |
| `+0x1E` | u16      | unknown_1e       | `0`, or an id near `item_id + 870` on 24 alchemy stone rows (client 1784) |
| `+0x20` | str16    | condition        | Empty on every alchemy stone row (client 1784)                   |

## Conditions

The condition is a client condition script, as in the quest tables
(`getLifeLevel(6)>80;` in `newquest.bss`). `getLifeLevel(n)` reads a life
skill level, and the item tooltips name the skill and the rank each
condition stands for:

| condition             | Tooltip text                                                      |
| --------------------- | ----------------------------------------------------------------- |
| `getLifeLevel(4)>10;` | Alchemy stones: "Growth Attempt: At least Alchemy Apprentice 1"   |
| `getLifeLevel(1)>30;` | 54201 Old Totem of the Sea: "Growth available for Fishing Professional 1 and higher." |
| `getLifeLevel(1)>40;` | 54280 Plain Totem of the Sea [Amberjack]: "Fishing Artisan 1"     |
| `getLifeLevel(1)>50;` | 54287 Refined Totem of the Sea [Amberjack]: "Fishing Master 1"    |

So life skill `4` is Alchemy, `1` is Fishing, and level `10` is Beginner 10
(the condition asks for level 11, Apprentice 1).

## Notes

- The Growth window reads its material from the stone's item key
  (`ToClient_GetAlchemyEvolveNeedItemKey`, `ToClient_GetAlchemyEvolveNeedItemCount`)
  and its result from `getAlchemyEvolveItemStaticStatusWrapper(itemKey, 0)`
  (`panel_window_alchemystoneevolve_all`). The rows agree: 821322 Brimming
  Essence of Aether lists "Usage #1: Alchemy Stone Growth", and every
  `result_item_id` is the next tier of `item_id` (45228 Splendid to 45232
  Shining Alchemy Stone of Destruction).
- The Totem tooltips read "Depending on the amount of EXP, it can be grown
  with Black Stone", which matches the 16001 Black Stone x1 rows.
- The Growth tab lists up to three results per stone
  (`getAlchemyEvolveItemSize`, slots `0` to `2` in `panel_window_alchemystone_all`);
  this file holds one `result_item_id` per row.
- The window shows the Growth chance from `ToClient_requestAlchemyEvolveRate`
  as `rate * 1e-4` with a `%` (`LUA_ALCHEMY_ENCHANT_RATE`), the
  1,000,000 = 100% scale of the Polishing EXP in `alchemyupgrade.dbss`. The
  Lua asks for the rate per stone slot, so it is not read from this file
  directly.

## Open Questions

### Totem Results

The 80 Totem rows hold `result_item_id` `0`, yet each Totem tooltip says it
can be grown. The tier the Totem grows into is not in this file; the
item IDs run in tier blocks per fish (54273 Old, 54280 Plain, 54287 Refined,
54292 Resplendent Totem of the Sea [Amberjack]), but that order is not a
link the client data states.

### unknown_08, unknown_14 and unknown_tail_08

All zero on client 3464. The 16 bytes of `unknown_14` fit two more
(item, count) pairs after `material_item_id` and `material_count`, but no
row fills them.

## In-Game Checks

### unknown_tail_04 as the Growth Chance

Needs item (all):

- [Splendid Alchemy Stone of Destruction](https://bdocodex.com/us/item/45228/)
- [Brimming Essence of Aether](https://bdocodex.com/us/item/821322/)

`unknown_tail_04` falls with the tier, from `455000` (Imperfect to Sturdy)
to `3870` (Splendid to Shining), and reads as a chance on the 1,000,000 =
100% scale the Growth window uses. Polish the stone to 100% and open Growth.
A chance of 0.387% means `unknown_tail_04` is the Growth chance at 100%
Polishing. Read it again at 80% and 150%: a chance that scales from 0.387%
with Polishing confirms it as the base the client scales.
