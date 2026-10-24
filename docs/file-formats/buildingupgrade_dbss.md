# `buildingupgrade.dbss` Format

## Purpose

The siege buildings a guild can upgrade after placing them: a Barricade
into an Iron Barricade, a Hwacha into a Big Hwacha, a Flame Tower into an
Enhanced Flame Tower. Each row names the placed building by its character
key, the character it becomes, the upgrade time and the items the upgrade
takes. Companion `buildingupgradeoffset.dbss` lists where every row sits.
The build and repair data of the guild building kits (forts, command
posts, Indomitable Flags) is in [`buildingsource.bss`](buildingsource_bss.md).

The interaction window reads a row when the server sends
`FromClient_InteractionBuildingUpgrade` for a placed building
(`panel_interaction_renew.luac`): it takes the building's
`getCharacterStaticStatusWrapper():getBuildingUpgradeStaticStatus()`, names
the target with `getTargetCharacter():getName()` in the
`LUA_INTERACTION_UPGRADE_BARRICADE` line, lists each source item with
`getSourceItemEnchantStaticStatus(index)` and `getSourceItemNeedCount(index)`,
and on Yes calls `toClient_RequestBuildingUpgrade(actorKeyRaw)`. The upgrade
then runs under progress bar type 12, `LUA_PROGRESSBAR_UPGRADING`, while
the player's action is `BUILDING_UPGRADE`
(`panel_widget_progressbar_renew.luac`).

On client 3474 the 32 rows are these upgrades; names are LOC type 6:

| Building                                   | Upgrades to                                     | Character keys                                                       |
| ------------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------- |
| Barricade                                  | Iron Barricade                                  | `12605` to `12609`, `12742`, `12805`, `12828`                        |
| Balenos/Serendia, Calpheon/Ulukita, Valencia/Edania Barricade | the same region's Iron Barricade | `12791` to `12793`                                                  |
| Barricade                                  | Sturdy Iron Barricade                           | `2022`                                                               |
| Savage Barricade                           | Savage Iron Barricade                           | `2056`                                                               |
| Hwacha                                     | Big Hwacha                                      | `12637` to `12639`, `12811`, `12834`, `2036`                         |
| Calpheon/Ulukita, Valencia/Edania Hwacha   | the same region's Big Hwacha                    | `12763`, `12764`                                                     |
| Flame Tower                                | Enhanced Flame Tower                            | `12632` to `12634`, `12810`, `12833`, `2035`                         |
| Calpheon/Ulukita, Valencia/Edania Flame Tower | the same region's Enhanced Flame Tower       | `12760`, `12761`                                                     |
| `[장미 전쟁]` (War of the Roses) buildings | their upgrades                                  | `12688`, `12690`, `12698`                                            |

The three War of the Roses rows have no LOC type 6 name; their
`characterstatic.dbss` Korean labels are the Flame Tower (`12688` to
`12691`), the Hwacha (`12690` to `12692`) and the Barricade (`12698` to
`12699`). The Name and Target Name columns show that Korean label
(`[장미 전쟁] 화염탑`) through `character_name()`. Every row on client 3474 takes Iron Ingot x10 and Melted Copper
Shard x10, except the Savage Barricade, which takes [Savage] Iron Ingot
x10. Client 1784 has 16 rows: the `12605` to `12609` and `12632` to `12639`
rows, `2022`, `2035`, `2036`, `2056`, and `2013` (Sturdy Barricade to
`2027`), which client 3474 no longer lists. Its Barricades take Iron Ingot
x30 and Melted Copper Shard x15 (`2013`: x10 and x5), its Hwachas and Flame
Towers Steel x100 and Melted Platinum Shard x50.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records                | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ---------------------- | --------- |
| 1      | 1276 and later | 3483    | `buildingupgrade.dbss`       | 1,288 | 63 Source Item, 32 Row | 12        |
| 1      | 1276 and later | 3483    | `buildingupgradeoffset.dbss` | 324   | 32 Index Row           | 10        |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `buildingupgrade.dbss`       | 1,288 B (100.0%) | 0 B (0.0%) |
| 1      | `buildingupgradeoffset.dbss` | 324 B (100.0%)   | 0 B (0.0%) |

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
| 1280   | Layout 1 |
| 1276   | Layout 1 |
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

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `buildingupgradeoffset.dbss` | Optional | `character_key -> (offset, size)` of every row; the rows are walked without it |
| `characterstaticoffset.dbss` | Optional | Which character keys have a `characterstatic.dbss` row to link to        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of variable rows with an empty string table.

| Offset      | Type       | Field        | Notes                                       |
| ----------- | ---------- | ------------ | ------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                      |
| `+0x04`     | u32        | count        | Number of rows                              |
| `+0x08`     | Row[count] | rows         | See Row                                     |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table            |
| `rows+0x04` | u32        | table_start  | End of the rows                             |
| `rows+0x08` | u32        | zero         | Always `0`                                  |

### Row (variable: 16 bytes + items)

| Offset  | Type                     | Field                | Notes                                                              |
| ------- | ------------------------ | -------------------- | ------------------------------------------------------------------ |
| `+0x00` | u16                      | character_key        | The placed building; unique; LOC type 6 names it                   |
| `+0x02` | u32                      | upgrade_time         | `90000`, `5000` on the Savage Barricade (clients 1784 and 3474); see In-Game Checks |
| `+0x06` | i32                      | upgrade_level        | `1` on every row of clients 1784 and 3474; see Open Questions       |
| `+0x0A` | u16                      | target_character_key | The character the building becomes                                 |
| `+0x0C` | u32                      | item_count           | Number of source items, at most 5                                  |
| `+0x10` | Source Item[item_count]  | items                | See Source Item                                                    |

### Source Item (12 bytes)

| Offset  | Type | Field    | Notes                                                                 |
| ------- | ---- | -------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item enchant key (`enchant_level << 24 \| item_id`); level `0` on every item of clients 1784 and 3474 |
| `+0x04` | i64  | count    | Number of that item                                                   |

### `buildingupgradeoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                          |
| ------- | ---------------- | ----- | ------------------------------ |
| `+0x00` | u32              | count | Equals the main file's `count` |
| `+0x04` | Index Row[count] | rows  | See Index Row                  |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                          |
| ------- | ---- | ------------- | -------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The main row's `character_key`                                 |
| `+0x02` | u32  | offset        | Start of the row in `buildingupgrade.dbss`, at its `character_key` |
| `+0x06` | u32  | size          | Full row length, `16 + 12 x item_count`                        |

On clients 1784 and 3474 the index rows run in the main file's order and
tile it from `0x08` to `table_start` with no gap.

## Field Names

The names are the columns of the `BuildingUpgrade_Table` sheet: `Index`,
`UpgradeTime`, `SourceItemKey00` to `SourceItemKey04` with `ItemCount00` to
`ItemCount04`, `TargetCharacterKey` and `UpgradeLevel`. `Index` holds the
building's character key, so the field is `character_key`.

| Source                                   | Rows | Matches                                                                            |
| ---------------------------------------- | ---- | ---------------------------------------------------------------------------------- |
| Private server `DataSheets.bexcel`, client 1784 | 17 | 16 of 16 client 1784 rows in every column; client 3474 shares 15 keys, with the same time, level and target on all 15 and the same items on 1 (`2056`) |
| Private server `BuildingUpgrade_Table`, client 519 | 5 | `2022`, `2013`, `2056`, `2035`, `2036`, every column as in the client 1784 file |

The 17th sheet row, `2085` with item `720767`, is not in any client file.
The 14 client 3474 rows whose items differ from the sheet take Iron Ingot
x10 and Melted Copper Shard x10 instead.

The server dump of the same private server on client 1784 loads the sheet in
`Load_BuildingUpgrade_Table` (VA `0x140934ae0`). It reads `Index` as an int,
keeps the low u16 and rejects a key the character table does not hold, does
the same for `TargetCharacterKey`, then reads `SourceItemKey%02d` and
`ItemCount%02d` for 0 to 4 as ints, stopping at the first empty
`SourceItemKey`, and rejects an item key of `0` or one the item table does
not hold. Each item goes into a vector of 16-byte (item key, int64 count)
pairs. `UpgradeTime` and `UpgradeLevel` are read as ints into one 8-byte
block, time first. The 2016 `gc::BuildingUpgradeStaticStatus` has `_key`
(u16), `_isBlockedUpgrade` (bool), `_sourceItemKey`
(`pa_vector<std::pair<gc::ItemEnchantKey,__int64>>`), `_upgradeTime`
(unsigned int) and `_targetCharacterKey` (u16); it has no upgrade level, and
the file stores no `_isBlockedUpgrade`.

## Notes

- The item descriptions (LOC type 0, `str_id4` `1`) of the placeable guild
  buildings still list the client 1784 materials on client 3474: "Iron
  Ingot x30, Melted Copper Shard x15" for `[Guild] Barricade (Tier 1)`
  (`44702`) and `[Guild] [Tier 2] Barricade (Conquest War)` (`767193`),
  "Steel x100, Melted Platinum Shard x50" for `[Guild] Hwacha (Tier 3)`
  (`56743`). The LOC type 108 Hwacha text keyed `59791` / `12834` lists
  "Iron Ingot x10, Melted Copper Shard x10", as the file does. The message
  box before an upgrade reads the items from this file.

## Open Questions

### What `upgrade_level` Counts

Every row of clients 1784 and 3474 and of the client 519 table has
`UpgradeLevel` `1`. The 2016 struct has no such member, and the Lua reads
only the target, the source items and their counts. It may be the step of a
building that upgrades more than once, but no row upgrades a building that
is itself an upgrade target.

## In-Game Checks

### Upgrade Time in Milliseconds

Needs item (all):

- [Iron Ingot](https://bdocodex.com/us/item/4052/) x10
- [Melted Copper Shard](https://bdocodex.com/us/item/4057/) x10

Needs zone: a Node War or Conquest War fort where your guild has placed a
Barricade, Hwacha or Flame Tower

This checks whether `upgrade_time` is in milliseconds.

1. Interact with the placed building and pick the upgrade action.
2. Confirm the message box that lists the materials.
3. Time the Upgrading progress bar from start to end.

Expected result: the bar takes about 90 seconds, so `upgrade_time` `90000`
is milliseconds. A bar of 90,000 seconds or one that ends at once means
another unit.
