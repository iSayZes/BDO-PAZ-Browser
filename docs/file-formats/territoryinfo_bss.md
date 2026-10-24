# `territoryinfo.bss` Format

## Purpose

The world's territories (Balenos, Serendia, Calpheon, ...) in game order: one
row per territory with its Korean territory and nation names, world map mark
icons, the booty items its lord receives (a conquest crown and armor), its
siege positions and its territory supply keys. The row key is the LOC type 12
ID, so the English territory and nation names come from that type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ----- | ---------------- | -------------------------- |
| 2      | 2726 and later | 3483    | `territoryinfo.bss` | 4,730 | 14 Territory Row | 88 to 92, 89 on average    |
| 1      | 1276 to 2468   | 2468    | `territoryinfo.bss` | 4,491 | 12 Territory Row | 120 to 132, 124 on average |

| Layout | File                | Known           | Unknown     |
| ------ | ------------------- | --------------- | ----------- |
| 2      | `territoryinfo.bss` | 4,674 B (98.8%) | 56 B (1.2%) |
| 1      | `territoryinfo.bss` | 4,443 B (98.9%) | 48 B (1.1%) |

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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
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
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
| 652    | No documented layout |
| 643    | No documented layout |
| 637    | No documented layout |
| 630    | No documented layout |
| 627    | No documented layout |
| 621    | No documented layout |
| 617    | No documented layout |
| 615    | No documented layout |
| 606    | No documented layout |
| 599    | No documented layout |
| 592    | No documented layout |
| 586    | No documented layout |
| 577    | No documented layout |
| 569    | No documented layout |
| 561    | No documented layout |
| 554    | No documented layout |
| 542    | No documented layout |
| 532    | No documented layout |
| 531    | No documented layout |
| 526    | No documented layout |
| 521    | No documented layout |
| 517    | No documented layout |
| 510    | No documented layout |
| 508    | No documented layout |
| 504    | No documented layout |
| 497    | No documented layout |
| 491    | No documented layout |
| 485    | No documented layout |
| 478    | No documented layout |
| 472    | No documented layout |
| 466    | No documented layout |
| 457    | No documented layout |
| 452    | No documented layout |
| 449    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 12, `str_id1` = `territory_key`, `str_id4` 0 / 1 = nation or realm / territory name |
| `languagedata_en.loc` | Optional | LOC type 0 names of the booty items                                                      |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout (`_common/pabr_strings.py`).

| Offset              | Type                 | Field        | Notes                                          |
| ------------------- | -------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                  | count        | Number of rows; 14 on client 3458              |
| `+0x08`             | Territory Row[count] | rows         | Byte-packed; see Territory Row                 |
| `rows+0x00`         | String Table         | string_table | See String Table                               |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                  | zero         | Always 0                                       |

A row is `80 + 4 * (booty_item_count + territory_supply_key_count)` bytes.
The rows tile `[0x08, table_start)` exactly (12 rows of 88 bytes and 2 of 92
on client 3458), so a parser walks them in order and fails when they do not
end at `table_start`.

### Territory Row (variable: 80 bytes + lists)

| Offset                       | Type                              | Field                      | Notes                                                                                  |
| ---------------------------- | --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------- |
| `+0x00`                      | u16                               | territory_key              | 0 to 13, equal to the row index; LOC type 12 `str_id1`                                 |
| `+0x02`                      | u8                                | is_king_territory_only     | `1` on Calpheon to Outer Edania, `0` on Balenos, Serendia and Inner Edania             |
| `+0x03`                      | u8                                | is_lord_territory_only     | `1` on Balenos and Serendia only, the two names ending in 자치령 (autonomous territory) |
| `+0x04`                      | f32[3]                            | occupying_tent_position    | World `x, y, z` of the occupying tent; all zero when unused |
| `+0x10`                      | f32[3]                            | volunteer_attack_position  | World `x, y, z` of the militia attack respawn point; all zero when unused |
| `+0x1C`                      | f32[3]                            | volunteer_defense_position | World `x, y, z` of the militia defense respawn point; all zero when unused |
| `+0x28`                      | u32                               | national_key               | Same value on every territory of one nation, different between nations |
| `+0x2C`                      | u32                               | nation_ref                 | String table index of the Korean nation or realm name                                  |
| `+0x30`                      | u32                               | name_ref                   | String table index of the Korean territory name                                        |
| `+0x34`                      | u32                               | icon_large_ref             | String table index of the large world map mark, relative to `ui_texture/`              |
| `+0x38`                      | u32                               | icon_small_ref             | String table index of the small world map mark, relative to `ui_texture/`              |
| `+0x3C`                      | u64                               | booty_item_count           | Entries in `booty_item_ids`; `2` on every row on client 3473                           |
| `+0x44`                      | u32[booty_item_count]             | booty_item_ids             | Items the territory's lord receives (LOC type 0): the conquest crown, then its armor   |
| `booty_item_ids+0x00`        | u64                               | territory_supply_key_count | Entries in `territory_supply_keys`; `1` on Serendia and Mediah, `0` elsewhere on client 3473 |
| `booty_item_ids+0x08`        | u32[territory_supply_key_count]   | territory_supply_keys      | Territory supply group keys: `114` on Serendia, `312` on Mediah on client 3473         |
| `territory_supply_keys+0x00` | u32                               | unknown_tail               | `0` on every row                                                                       |

Positions on client 3458: Calpheon, Mediah and Valencia fill all three,
Kamasylvia and O'dyllita only the first, the rest none. The occupying tent
and the militia defense position lie within about 20,000 units of a castle
node in `mapdata_realexplore2.bwp`: `calpheon_castle` (702), `mediacastle`
(1152), `valencia_castle` (1342) and `othilita_castle` (1692). Valencia's
militia attack position sits next to `ruins of castle valencia` (1374).

Booty items: Balenos to Mediah each have their own crown and armor (Silver
Mane, Blue Lion, Golden Eagle, Asula); Valencia and every later territory
store the Crown of Aal (23385) and Armor of Aal (23390).

### String Table (variable: 4 bytes + strings)

46 strings on client 3458, all referenced. The territories of one nation
share its nation entry (Republic of Calpheon, Alyaelli), and where nation and
territory names match (The Great Ocean, Kamasylvia and the other single
territory realms) both refs point at one entry. The Great Ocean (territory 5) stores Valencia's marks under
`New_UI_Common_forLua/Widget/WorldMap/territory/`; every other icon is under
`Renewal/ETC/WordMap/`. Paths keep mixed case, so the handler lowercases them.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 46 on client 3458   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

On client 1784 a Territory Row held five positions instead of three, which
moved `national_key` to `+0x40`, and a u16 list of territory trade keys before
the territory supply keys, which were u16 values too. Only the
Territory Row differs from Layout 2. On client 1784 the file holds 10 rows;
Balenos to Mediah have 5 trade keys and the rest none, and every territory
has 0 to 5 supply keys.

### Territory Row (variable: 112 bytes + lists)

| Offset                       | Type                            | Field                      | Notes                                                          |
| ---------------------------- | ------------------------------- | -------------------------- | -------------------------------------------------------------- |
| `+0x00`                      | u16                             | territory_key              |                                                                |
| `+0x02`                      | u8                              | is_king_territory_only     |                                                                |
| `+0x03`                      | u8                              | is_lord_territory_only     |  |
| `+0x04`                      | f32[3]                          | occupying_tent_position    |  |
| `+0x10`                      | f32[3]                          | volunteer_attack_position  |  |
| `+0x1C`                      | f32[3]                          | volunteer_defense_position |  |
| `+0x28`                      | f32[3]                          | plunder_attack_position    | World `x, y, z` of the plunder war attack respawn point |
| `+0x34`                      | f32[3]                          | plunder_defense_position   | World `x, y, z` of the plunder war defense respawn point |
| `+0x40`                      | u32                             | national_key               |  |
| `+0x44`                      | u32                             | nation_ref                 |                                                                |
| `+0x48`                      | u32                             | name_ref                   |                                                                |
| `+0x4C`                      | u32                             | icon_large_ref             |                                                                |
| `+0x50`                      | u32                             | icon_small_ref             |                                                                |
| `+0x54`                      | u64                             | booty_item_count           |                                                                |
| `+0x5C`                      | u32[booty_item_count]           | booty_item_ids             |                                                                |
| `booty_item_ids+0x00`        | u64                             | territory_trade_key_count  | Entries in `territory_trade_keys`                              |
| `booty_item_ids+0x08`        | u16[territory_trade_key_count]  | territory_trade_keys       | Territory trade group keys: Balenos holds `5` to `1`, Serendia `105` to `101` |
| `territory_trade_keys+0x00`  | u64                             | territory_supply_key_count |                                                                |
| `territory_trade_keys+0x08`  | u16[territory_supply_key_count] | territory_supply_keys      | Balenos holds `11` to `15`, Serendia `113`, `112`, `111`, `114`, `115` |
| `territory_supply_keys+0x00` | u32                             | unknown_tail               | `0` on every row on client 1784                                |

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::TerritoryInfo` holds `_territoryKey` (i16), `_isKingTerritoryOnly`,
`_isLordTerritoryOnly`, `_occupyingTentPosition`, three members filled at
load time (`_mainTownRegion`, `_capitalTownRegion`, `_affliatedRegionGroups`),
`_nationalKey` (u32), `_nationalName`, `_territoryName`, `_territoryImage`,
`_territorySmallImage`, `_bootyItemKeyList` (a vector of i32),
`_bootyItemList` (a vector of `gc::Item`), and four vectors of u16 keys:
`_territoryTradeList`, `_territorySupplyList`, `_territoryTradeKeyList` and
`_territorySupplyKeyList`. Layout 1 stores `_territoryKey` to
`_occupyingTentPosition`, `_nationalKey` to `_territorySmallImage`,
`_bootyItemKeyList`, `_territoryTradeKeyList` and `_territorySupplyKeyList`
in this order, with five positions where the 2016 struct has one.

`Territory_Table` in a private server's `DataSheets.bexcel` on client 1784
(and the same sheet in its `.xlsm`, and in a second private server's database
on client 519) has the columns `TerritoryKey`, `NationalName`,
`TerritoryName`, `TerritoryImage`, `TerritorySmallImage`,
`OccupyingTentPositionX` to `Z`, `BootyItem`, `WorldMapColor`,
`VolunteerAttackX` to `Z`, `VolunteerDefenseX` to `Z`, `PlunderAttackX` to
`Z` and `PlunderDefenseX` to `Z`. The sheet shares territory keys 0 to 9 with
both clients:

| Column | Field | Equal (client 1784, 10 keys) | Equal (client 3473, 10 keys) |
| ------ | ----- | ---------------------------- | ---------------------------- |
| `OccupyingTentPositionX` to `Z` | `occupying_tent_position` | 10 | 8 |
| `VolunteerAttackX` to `Z` | `volunteer_attack_position` | 10 | 10 |
| `VolunteerDefenseX` to `Z` | `volunteer_defense_position` | 10 | 10 |
| `PlunderAttackX` to `Z` | `plunder_attack_position` | 10 | |
| `PlunderDefenseX` to `Z` | `plunder_defense_position` | 10 | |
| `BootyItem` | `booty_item_ids` | 10 | 10 |

Calpheon, Mediah and Valencia fill every position column; the other rows
are zero in both. The two client 3473 tent mismatches are Kamasylvia and
O'dyllita, which the sheet leaves at zero. The
sheet comments call the volunteer columns the militia (민병대) siege attack
and defense respawn points, the plunder columns the plunder war (약탈전)
respawn points, and `BootyItem` the items given to the occupying lord, at
enchant level 0 and count 1. `WorldMapColor` has no bytes in either layout.

The two lists come from `TerritoryTradeItemList_Table` (columns
`TerritoryKey`, `ItemGroupKeyType`, `ItemMainGruopKey`, `TerritoryGroupKey`).
Its comment gives `ItemGroupKeyType` `0` as territory trade (영지 무역) and
`1` as territory supply (영지 납품). On client 1784 each list holds the
`TerritoryGroupKey` values of the territory's rows of one type, in sheet
order: the first list type `0` on 4 of the 4 territories that have such
rows, the second type `1` on 6 of the 9. Valencia and The Great Ocean keep
their first 4 of 5 and 6 rows, and O'dyllita stores none of its one row
(`415`, `515`, `516` and `811` are missing). Neither list holds `ItemMainGruopKey` values, so the names follow the 2016
`_territoryTradeKeyList` and `_territorySupplyKeyList`. Client 3473 has one
list, and its keys `114` (Serendia) and `312` (Mediah) are type `1` rows of
those territories. `TerritorySupply` is the NPC role the client labels
Imperial Delivery (see [characterspawntype](characterspawntype_dbss.md)).

`is_king_territory_only` has no sheet column and is named from its place in
the 2016 member order, between the matched `territory_key` and the occupying
tent position. The client Lua calls `siegeWrapper:isKingTerritoryOnly()` in
`panel_window_lordmenu_all_1.luac`, where `isKing()` and
`isKingTerritoryOnly()` together decide whether the lord menu shows its
first two local tax sliders. The next 2016 bool, `_isLordTerritoryOnly`, is
`is_lord_territory_only`, set on the two autonomous territories. `national_key` is the 2016
`_nationalKey`; the sheet has no column for it. The position fields take the
sheet's column names; the 2016 struct has only `_occupyingTentPosition`.

## Notes

- iDevelopThings' [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  documents the same layout (FORMATS.md, section 10), with
  `is_king_territory_only` as a primary-territory flag and the positions as
  world map marks.
- bdo-data-extractor reads a territory index in each `regioninfo.bss` region
  that joins this file and LOC type 12.
- The `territory_key` of `dropuimaincategoryinfo.bss` (see
  [dropuihuntinggroundinfo](dropuihuntinggroundinfo_bss.md)) is the same LOC
  type 12 key.
- A territory supply key is the territory key times 100 plus 11 to 16 in the
  sheet; the trade keys are the territory key times 100 plus 1 to 5.
- The handler's Lord Territory and King Territory column labels are my own
  translations of the 2016 `_isLordTerritoryOnly` and `_isKingTerritoryOnly`,
  in every language. The client LOC has no term for either flag: the English
  territory names are plain ("Balenos", "Serendia"), and the only English LOC
  string with "autonomous" is "Drieghan Autonomous Region". The Korean names
  of the two lord territories end in 자치령 (autonomous territory), which the
  English client does not show, so the column does not use that word.

## Open Questions

### What `unknown_tail` Holds

Both layouts end a row with a u32 that is `0` on every row of clients 1784
and 3473. The 2016
`gc::TerritoryInfo` ends with `_territorySupplyKeyList`, and no
`Territory_Table` column is left over except `WorldMapColor`, whose RGBA
values are not zero.
