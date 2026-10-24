# `guaranteeenchantss.dbss` Format

## Purpose

The Ancient Anvil table: for each enhancement type and current enhancement
level, how many Agris Essences a failed attempt has to stack before the next
attempt at that level is guaranteed. The enhancement window shows this count
as the hammer gauge (`getSSEnchantCount()` in the client Lua). The enhancement
type is the item's `enhancement_type` in `itemenchant.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2444 and later | 3483    | `guaranteeenchantss.dbss` | 2,307 | 329 Row | 7         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `guaranteeenchantss.dbss` | 2,307 B (100.0%) | 0 B (0.0%) |

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

| File               | Required | Role                                                                 |
| ------------------ | -------- | -------------------------------------------------------------------- |
| `itemenchant.dbss` | Optional | The items of each enhancement type; the handler reads them from the `ENHANCEMENT_TYPE_ITEMS` lookup index, not as a companion |

There is no `guaranteeenchantssoffset.dbss`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                              |
| ------- | ---------- | ----- | ---------------------------------- |
| `+0x00` | u32        | count | Number of rows; 329 on client 3464 |
| `+0x04` | Row[count] | rows  | See Row                            |

There is no `PABR` magic and no trailer: the file is `4 + count × 7` bytes
(2,307 on client 3464).

### Row (7 bytes)

| Offset  | Type | Field            | Notes                                                       |
| ------- | ---- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | enhancement_type | `enhancement_type` of the item in `itemenchant.dbss`        |
| `+0x04` | u8   | enchant_level    | The item's current level; the attempt goes to the next level |
| `+0x05` | u16  | agris_count      | Agris Essences needed for a guaranteed success; `0` means no gauge at that level |

The row is unaligned: `agris_count` starts at an odd offset. `(enhancement_type,
enchant_level)` is unique. Rows are not sorted by either field (the first rows
are `24/7`, `3/10`, `2/17`, `1/0`).

`enchant_level` is the current level and not the target: types of items that
go to PEN at level 20 run 0 to 19 and types of five-level accessories run 0
to 4, so no row exists for the highest level. Levels 0 to 6 of types 1, 2
and 7 store `0`.

## Enhancement Types

The items of each enhancement type on client 3464, from `enhancement_type` in
`itemenchant.dbss`; base items only, with each item's highest level.

| Type  | Levels | Items (client 3464) | Example items                                                    |
| ----: | ------ | ------------------: | ---------------------------------------------------------------- |
| 1     | 0-19   | 3,678 | Kzarka Longsword, Kutum Shotgun, Offin Tett's Radiant Kyve, Rebar Helmet |
| 2     | 0-19   | 382   | Blackstar Longsword, Blackstar Kunai, Fiery Blackstar Hexround      |
| 3     | 0-19   | 0     | None; Naru gear until 2025-12-18 (see Notes)                      |
| 4     | 0-19   | 0     |                                                                   |
| 5     | 0-4    | 0     | None; Godr-Ayed weapons until 2026-03-26 (see Notes)              |
| 6     | 0-4    | 12    | Fallen God's Armor, Labreska's Helmet, Ator's Shoes, Dahn's Gloves |
| 7     | 0-19   | 24    | Manos Cook's Clothes, Loggia Hunter's Clothes, Crio Fisher's Clothes |
| 8     | 0-9    | 184   | [Donkey] Steel Combat Barding, Trade Wagon Wheel, [Hunting] Master Matchlock |
| 9     | 0-9    | 11    | Epheria Galleass: Enhanced Plating, Epheria Caravel: Verisha Cannon |
| 10    | 0-9    | 11    | Epheria Galleass: Mayna Cannon, Epheria Caravel: Black Dragon Figurehead |
| 11    | 0-9    | 8     | Panokseon: Haemo's Sail, Epheria Carrack: Toro Cannon               |
| 12    | 0-9    | 24    | Epheria Carrack: Valor (Chiro's Cannon), Panokseon: Byukgye's Enhanced Sail |
| 13    | 0-4    | 176   | Deboreka Necklace, Talis Earring, Yuria Necklace, Red Coral Ring     |
| 14    | 0-4    | 10    | Capotia Earring, Tidal Capotia Belt                                 |
| 15    | 0-4    | 12    | Manos Ring, Loggia Necklace, Geranoa Belt                           |
| 16    | 0-9    | 4     | Tuvala Belt, Ring, Earring and Necklace                             |
| 17    | 0-4    | 15    | Asula's Crimson Eye Earring, Ring of Sealed Magical Power, [Event] Terrmina Necklace |
| 18    | 0-2    | 4     | Forest's Eye Earring, Rock Heart Belt, Red Sand Crystal Ring, Tears of the Wind Necklace |
| 19    | 0-9    | 212   | Sovereign Longsword, Sovereign Dual Glaives                          |
| 20    | 0-19   | 1     | [Event] Tarnished Sword                                             |
| 21    | 0-9    | 8     | Kharazad Necklace, Moonhushed Kharazad Earring                      |
| 22    | 0-9    | 4     | Preonne Belt, Ring, Earring and Necklace                            |
| 23    | 0-24   | 168   | Tuvala Helmet, Tuvala Shotgun, Combatant's Tuvala Longsword         |
| 24    | 0-9    | 4     | Edana - Furystride, Edana - Oathgrip, Edana - Abyssveil, Edana - Heavensmite |
| 25    | 0      | 3     | Imperfect Alchemy Stone of Life, Protection and Destruction          |
| 26    | 0      | 3     | Sturdy Alchemy Stone of Life, Protection and Destruction             |
| 27    | 0      | 9     | Sharp Alchemy Stone of Destruction, Resolute Alchemy Stone - Protection |
| 28    | 0      | 20    | Resplendent Alchemy Stone of Life, Resplendent Khan's Heart: Protection |
| 29    | 0      | 20    | Splendid Alchemy Stone of Life, Blessed Splendid Vell's Heart        |
| 30    | 0-9    | 8     | Ekleta Necklace, Duskborne Ekleta Belt                              |
| 31    | 0-9    | 8     | Apeiron Necklace, Sunstarved Apeiron Ring                           |
| 32    | 0-9    | 16    | Epheria Carrack: Valor (Falasi's Sail), Epheria Carrack: Balance (Falasi's Plating) |
| 33    | 0-15   | 0     |                                                                   |

Type 0 (65,174 base items) has no rows. Types 25 to 29 are alchemy stones
with one level; the LOC note on alchemy stone growth (type 37, id1
1288266772) reads "A full Ancient Anvil and 80%+ EXP guarantees a higher
grade".

## Notes

- How the client uses the count (`panel_widget_enchant_main_all`,
  `updateAgrisStack`): the gauge is shown when `getSSEnchantCount()` is not
  `0` and the target cannot be changed to Tuvala. It reads
  `getCurrentEnchantCount() / getSSEnchantCount()`, and at a full gauge the
  hammer effect `fUI_SpiritEnchant_New_Hammer_01A` plays.
  `ToClient_IsGuaranteeEnchant()` then sets the shown success rate to
  `1000000`, which is `CppDefine.e100Percent` (100%).
- The gauge tooltip (`LUA_ANVILOFANCIENT_TOOLTIP_DESC`) reads "Upon failed
  enhancement, Agris Essence is accumulated for the gear and its enhancement
  level. Once enough Agris Essence has accumulated, enhancement success is
  guaranteed." The count is per item and per level, as the table is.
- `enhancement_type` is the u32 of the same name in the After the Icon
  section of [itemenchant.dbss](itemenchant_dbss.md). On client 3464 every
  type an item carries has rows here, and only types 3, 4, 5 and 33 have
  rows but no items.
- Garmoth's Ancient Anvil guide lists the same counts, e.g. 35 for a yellow
  TET weapon to PEN (type 1, level 19) and 15 for a TET Blackstar to PEN
  (type 2, level 19).
- `agris_count` is not the `enchantstaticstatus.dbss` count: Blackstar
  Longsword stores 3,670 there at PEN, against 15 here.
- On client 3464, `agris_count` runs 0 to 1,000; 1,000 is type 6, level 4
  (Fallen God gear at TET).
- Type 4 stores the same counts as the first 20 levels of type 23
  (Tuvala), including `0` at levels 15 to 17.
- Type 5 is left over from the Godr-Ayed weapons. Pearl Abyss's
  [notice for the 2026-03-26 update](https://blackdesert.pearlabyss.com/Asia/en-us/News/Notice/Detail?_boardNo=13023)
  removed them and turned each into a Blackstar weapon (PRI to TET into TET
  Blackstar plus Silver, PEN into PEN Blackstar), and Garmoth's Ancient Anvil
  guide lists type 5's counts (7, 9, 11, 15, 18) under Godr-Ayed ("After").
  Its five levels fit the PRI to PEN range of those weapons. Godr-Ayed
  Celestial Bo Staff (954005), the one item still named Godr-Ayed on client
  3464, stores type `0`.
- Type 3 is left over from the Naru gear. The Season Changes FAQ for the
  [2025-12-18 maintenance](https://www.naeu.playblackdesert.com/en-us/News/Detail?groupContentNo=9477&countryType=de-DE)
  says Naru Gear "has been replaced by Tuvala Gear", which now enhances from
  +0 to PEN on every character, and Garmoth's Ancient Anvil guide lists type
  3's counts under Naru. Its levels 0 to 19 fit gear that goes from +0 to
  PEN. No English item name on client 3464 starts with "Naru ".

## Open Questions

### Enhancement Types Without Items

No item on client 3464 carries `enhancement_type` 4 or 33, so those rows
have no items to name them by (types 3 and 5 are removed Naru and Godr-Ayed
gear, see Notes). Removed gear would explain them too. Type 4 stores the same
counts as the first 20 levels of type 23 (Tuvala); type 33 stores one count,
10 at level 15. A patch notice that removes gear with those levels, or a
patch that adds items with these values, would settle it.
