# `edaniaregioninfo.bss` Format

## Purpose

Holds one row per Edania region, the ten castle domains that guilds hold in Edania (Aetherion to Voidekaia), plus a row for the "no region" value. Each row stores the client's `__eEdaniaRegion` value and its colour in the Edania region map (`ui_texture/minimap/area/edaniaregionmap.bmp`), twice; for the five castles with a region of their own the colour equals that region's `regioninfo.bss` `color`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3483    | `edaniaregioninfo.bss` | 119   | 11 Row  | 9         |

| Layout | File                   | Known        | Unknown      |
| ------ | ---------------------- | ------------ | ------------ |
| 1      | `edaniaregioninfo.bss` | 64 B (53.8%) | 55 B (46.2%) |

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

| File                  | Required | Role                                                                                                   |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Castle name text (LOC type 37, keyed by the hash of the GAME sheet key `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>`) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                   |
| ------------------- | ----------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                          |
| `+0x04`             | u32               | record_count       | Observed `11`                                           |
| `+0x08`             | Row[record_count] | records            | See Row; byte-packed                                    |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 9 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                              |

The file is `8 + 9 × 11 + 12 = 119` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (9 bytes)

| Offset  | Type     | Field         | Notes                                                                                                   |
| ------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color     | Region map colour, stored blue, green, red like the `regioninfo.bss` `color`; the parser returns `rrggbb`. See Notes |
| `+0x03` | u8       | unknown_03    | Always `0`                                                                                              |
| `+0x04` | bytes[3] | unknown_04    | Equals `map_color` on every row                                                                         |
| `+0x07` | u8       | unknown_07    | Always `0`                                                                                              |
| `+0x08` | u8       | edania_region | `__eEdaniaRegion` value, unique; `0` to `9` for the regions, `10` for `__eEdaniaRegion_Count`. Rows are not in key order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Enum Values

`edania_region` is the client's `__eEdaniaRegion` enum. The Lua lists the names in this order (`panel_characternametag.luac`, `panel_widget_chatmain_2.luac`, `panel_window_edania_contents_all.luac`) and loops `0` to `Zephyros` for the first Edana group and `Aphrodon` to `Count - 1` for the second (`panel_characterinfo_cashbuff_all_1.luac`). The castle name key is the one the Edania window gives each region.

| Value | Enum name   | Castle name key                   | English castle name |
| ----- | ----------- | --------------------------------- | ------------------- |
| `0`   | Aetherion   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_1`  | Aetherion Castle    |
| `1`   | Nymphamare  | `LUA_EDANIA_SYSTEM_CASTLE_NAME_2`  | Nymphamaré Castle   |
| `2`   | Orbita      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_4`  | Orbita Castle       |
| `3`   | Tenebraum   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_3`  | Tenebraum Castle    |
| `4`   | Zephyros    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_5`  | Zephyros Castle     |
| `5`   | Aphrodon    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_6`  | Aphrodon Temple     |
| `6`   | Hermesia    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_7`  | Hermesia Castle     |
| `7`   | Magaia      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_8`  | Magaia Temple       |
| `8`   | Aresion     | `LUA_EDANIA_SYSTEM_CASTLE_NAME_9`  | Aresion Temple      |
| `9`   | Voidekaia   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_10` | Event Horizon       |
| `10`  | _Count      |                                   | none                |

Orbita and Tenebraum swap key numbers 3 and 4. The file confirms the values of the first five: their `map_color` matches the `regioninfo.bss` `color` of exactly one region each, and that region is the castle of the same name (1581 Aetherion Castle, 1621 Nymphamaré Castle, 1571 Orbita Castle, 1611 Tenebraum Castle, 1596 Zephyros Castle).

## Notes

- The client reads a player's Edania region with `ToClient_GetEdaniaRegion(userNo)` and picks the faction icon on the name tag and in chat from it (`Combine_Etc_EdaniaIcon_Jordain_Normal` for Aetherion ... `Combine_Etc_EdaniaIcon_Hadum_Normal` for Voidekaia). `_Count` is the "no Edania region" answer.
- `regioninfo.bss` has regions named after the second-group castles too (Aphrodon Temple, Hermesia Outer and Inner Castle, Magaia Temple, Aresion Temple), but none of them has the colour stored here, so only the first five rows link to a region.
- `map_color` follows `ui_texture/minimap/area/edaniaregionmap.bmp.rid`, the palette of the Edania region map, which lists exactly these 11 colours on client 3474 (`100d10` first); the same holds for the region maps of three other tables of this row shape ([`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names) Field Names).
- `blizzardregioninfo.bss` is the other small region-variant table. It does not share this layout (26-byte rows keyed by a region key), so the two files have separate parsers.

## Open Questions

### Why the Value Is Stored Twice

`unknown_04` equals `map_color` on every row. Whether the two are fill and
border, or two map layers, is not known. `100d10`, the `_Count` row's
colour, is the first colour of every region map palette of this row shape.

Each colour plus its zero byte has the shape of `regioninfo.bss` `color`
(u8[3]) and `color_alpha`, which the 2016 client types as one 4-byte
`pa::Color _colorKey`, so `unknown_03` and `unknown_07` read as alpha
bytes; that is a reading, not a name. No source names `unknown_03`,
`unknown_04` and `unknown_07`: the file is not in the client 1784 private server's binaries,
sheets or server dump (no `edania` string), the 2016 client predates
Edania, the live client exe holds no readable strings, and none of the
client 3474 Lua Edania calls (`ToClient_GetEdaniaRegion`,
`ToClient_GetEdaniaApplyRegion`, `ToClient_IsEdaniaAreaOn`,
`ToClient_ToggleEdaniaArea`, `ToClient_GetEdaniaEtcOption`) returns a
colour.

## In-Game Checks

### Edania Overlay Colours

Needs zone: Edania

This checks whether the world map overlay draws each Edania domain in its `map_color`, the colour of the domain in the Edania region map.

For the five first-group castles `map_color` equals the `regioninfo.bss` `color` of the castle's region, and `regioninfo.bss` stores that colour blue, green, red (its `R`, `G` and `B` match the server-side `Region_Table` on 895 of 896 regions, client 3464). Read the same way, the rows here are Aetherion `0a1cf5` (blue), Orbita `905037` (brown-red) and Event Horizon (Voidekaia) `770868` (purple).

1. Open the world map over Edania.
2. Switch the Edania area overlay on (`ToClient_ToggleEdaniaArea`).
3. Note the colour of the Aetherion, Orbita and Event Horizon domains.

Expected result: the three domains show those colours. A domain colour that matches no row means the overlay takes its colour from somewhere else.
