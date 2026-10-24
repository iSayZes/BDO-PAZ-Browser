# `bossinfostaicstatusmanager.bss` Format

## Purpose

The bosses of the Boss Info window (`panel_worldmap_bosslist_all`, opened
from the world map): one variable-length record per boss with its tab, its
character, an optional reinforced form, the window's two images, the main
rewards, a world position and, for world bosses, the weekly spawn times. The
window reads a record through `ToClient_getBossStaticStatus(index)`. On
client 3464 the 28 records are 14 World bosses, the 5 Field bosses, 6 Dark
Rift bosses and 3 Hunting/Sniper bosses. The file name spells "staic" for
"static".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records                                                    | Row bytes               |
| ------ | -------------- | ------- | -------------------------------- | ----- | ---------------------------------------------------------- | ----------------------- |
| 1      | 3326 and later | 3483    | `bossinfostaicstatusmanager.bss` | 7,640 | 56 Group, 58 Group List, 29 Boss Record, 8 Reinforced Form | 4 to 126, 36 on average |

| Layout | File                             | Known           | Unknown     |
| ------ | -------------------------------- | --------------- | ----------- |
| 1      | `bossinfostaicstatusmanager.bss` | 7,611 B (99.6%) | 29 B (0.4%) |

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
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No file              |
| 3267   | No file              |
| 3258   | No file              |
| 3251   | No file              |
| 3242   | No file              |
| 3235   | No file              |
| 3229   | No file              |
| 3212   | No file              |
| 3203   | No file              |
| 3193   | No file              |
| 3186   | No file              |
| 3177   | No file              |
| 3169   | No file              |
| 3158   | No file              |
| 3151   | No file              |
| 3144   | No file              |
| 3133   | No file              |
| 3125   | No file              |
| 3118   | No file              |
| 3111   | No file              |
| 3103   | No file              |
| 3095   | No file              |
| 3086   | No file              |
| 3072   | No file              |
| 3062   | No file              |
| 3052   | No file              |
| 3045   | No file              |
| 3037   | No file              |
| 3030   | No file              |
| 3021   | No file              |
| 3012   | No file              |
| 3002   | No file              |
| 2995   | No file              |
| 2987   | No file              |
| 2978   | No file              |
| 2970   | No file              |
| 2959   | No file              |
| 2951   | No file              |
| 2942   | No file              |
| 2935   | No file              |
| 2932   | No file              |
| 2923   | No file              |
| 2919   | No file              |
| 2907   | No file              |
| 2900   | No file              |
| 2891   | No file              |
| 2882   | No file              |
| 2872   | No file              |
| 2863   | No file              |
| 2855   | No file              |
| 2849   | No file              |
| 2844   | No file              |
| 2834   | No file              |
| 2825   | No file              |
| 2819   | No file              |
| 2811   | No file              |
| 2803   | No file              |
| 2794   | No file              |
| 2783   | No file              |
| 2774   | No file              |
| 2765   | No file              |
| 2756   | No file              |
| 2750   | No file              |
| 2743   | No file              |
| 2736   | No file              |
| 2726   | No file              |
| 2717   | No file              |
| 2709   | No file              |
| 2703   | No file              |
| 2695   | No file              |
| 2684   | No file              |
| 2672   | No file              |
| 2665   | No file              |
| 2657   | No file              |
| 2649   | No file              |
| 2644   | No file              |
| 2637   | No file              |
| 2629   | No file              |
| 2619   | No file              |
| 2612   | No file              |
| 2606   | No file              |
| 2602   | No file              |
| 2601   | No file              |
| 2592   | No file              |
| 2583   | No file              |
| 2575   | No file              |
| 2567   | No file              |
| 2560   | No file              |
| 2553   | No file              |
| 2545   | No file              |
| 2538   | No file              |
| 2529   | No file              |
| 2519   | No file              |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
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

| File                                                 | Required | Role                                                                 |
| ---------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| `stringtable.bss`                                    | Optional | Tab names, keys `LUA_WORLDMAP_BOSSLIST_TOOLTIP_<boss_info_type>`     |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Resolves the texture keys to a DDS file and a UV rectangle           |
| `languagedata_en.loc`                                | Optional | LOC type 6 boss names, LOC type 0 reward item names                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                      | Field        | Notes                                                          |
| ------------------- | ------------------------- | ------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]                   | magic        | `PABR`                                                         |
| `+0x04`             | u32                       | record_count | `28` on client 3464                                            |
| `+0x08`             | Boss Record[record_count] | records      | Variable size; the last one ends where the string table starts |
| `records+0x00`      | String Table              | string_table | Counted string table (`_common/pabr_strings.py`)               |
| `string_table+0x00` | u32                       | table_start  | Offset of the string table                                     |
| `string_table+0x04` | u32                       | zero         |                                                                |

### Boss Record (variable: 30 bytes + lists and reinforced form)

| Offset               | Type                               | Field             | Notes                                                                 |
| -------------------- | ---------------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`              | Group List                         | spawn_times       | See Group List; empty on every non-World record                       |
| `spawn_times+0x00`   | Group List                         | unknown_ids       | Same groups and lengths as `spawn_times`, one ID per time; see Open Questions |
| `unknown_ids+0x00`   | u32                                | reward_item_count | Number of `reward_items`                                              |
| `unknown_ids+0x04`   | u32[reward_item_count]             | reward_items      | Item IDs: the "Main Rewards" row of the window                        |
| `reward_items+0x00`  | u32                                | main_texture      | String index of the large boss image (`Img_` key)                     |
| `reward_items+0x04`  | u32                                | list_texture      | String index of the list entry image; always `main_texture + 1`       |
| `reward_items+0x08`  | u16                                | character_id      | `characterstatic.dbss` character ID, LOC type 6                       |
| `reward_items+0x0A`  | u8                                 | has_reinforced    | `0` or `1`; when `1`, the Reinforced Form follows                     |
| `reward_items+0x0B`  | Reinforced Form if has_reinforced = 1 | reinforced     | See Reinforced Form                                                   |
| `reinforced+0x00`    | f32[3]                             | position          | World position; the second value is the height                       |
| `reinforced+0x0C`    | u8                                 | boss_info_type    | Window tab, see [Boss Info Types](#boss-info-types)                   |
| `reinforced+0x0D`    | u8                                 | unknown_flag      | `1` on the 14 World records, `0` on the rest                          |
| `reinforced+0x0E`    | u8                                 | is_event_boss     | `1` only on 21878 Gift Box; see Notes                                 |

### Reinforced Form (variable: 14 bytes + rewards)

| Offset                          | Type                              | Field                        | Notes                                                           |
| ------------------------------- | --------------------------------- | ---------------------------- | --------------------------------------------------------------- |
| `+0x00`                         | u16                               | reinforced_character_id      | The reinforced form (23172 Nightmarish Kzarka for 23001 Kzarka) |
| `+0x02`                         | u32                               | reinforced_main_texture      | String index                                                    |
| `+0x06`                         | u32                               | reinforced_list_texture      | String index                                                    |
| `+0x0A`                         | u32                               | reinforced_reward_item_count | Number of `reinforced_reward_items`                             |
| `+0x0E`                         | u32[reinforced_reward_item_count] | reinforced_reward_items      | Item IDs                                                        |

The reinforced form stores its textures before its rewards, the reverse of
the Boss Record's `reward_items`, `main_texture` and `list_texture`.

### Group List (variable: 4 bytes + groups)

| Offset  | Type               | Field       | Notes                        |
| ------- | ------------------ | ----------- | ---------------------------- |
| `+0x00` | u32                | group_count | `0`, or `2` on World records |
| `+0x04` | Group[group_count] | groups      | See Group                    |

The group keys are `0` then `1` on every record that has groups.

### Group (variable: 5 bytes + values)

| Offset  | Type             | Field       | Notes                 |
| ------- | ---------------- | ----------- | --------------------- |
| `+0x00` | u8               | group_key   | `0` or `1`            |
| `+0x01` | u32              | value_count | Number of `values`    |
| `+0x05` | u32[value_count] | values      | The group's values    |

### String Table (variable: 4 bytes + strings)

The string table holds the texture keys, an `Img_` key followed by the list
key for each image set (`Combine_Etc_WorldMap_BossList_Img_Begg`,
`Combine_Etc_WorldMap_BossList_Begg`): 60 strings for 30 sets on client
3464.

| Offset  | Type               | Field        | Notes                                    |
| ------- | ------------------ | ------------ | ---------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                        |
| `+0x04` | pstr[string_count] | strings      | Texture keys; the texture fields index this list |

## Boss Info Types

The window tab, named by `stringtable.bss` key
`LUA_WORLDMAP_BOSSLIST_TOOLTIP_<n>`.

| Value | Tab            | Records (client 3464)                                                    |
| ----- | -------------- | ------------------------------------------------------------------------ |
| 0     | World          | 14: Gift Box, Kzarka, Nouver, Karanda, Kutum, Offin, Garmoth, Vell, Quint, Muraka, Bulgasal, Uturi, Sangoon, Golden Pig King |
| 1     | Field          | 5: Dastard Bheg, Red Nose, Dim Tree Spirit, Giant Mudster, Katzvariak    |
| 2     | Dark Rift      | 6: Red Nose, Dastard Bheg, Muskan, Dim Tree Spirit, Ferrid, Griffon (25501 to 25531) |
| 3     | Hunting/Sniper | 3: Rawr-Rawr, Blue Whale, Fugitive Khalk                                 |
| 4     | Event          | None in the file                                                         |

`TOOLTIP_5` is "Hunting", the console name of tab 3.

## Notes

- The Lua calls on a record are `getBossInfoType()`,
  `getCharacterKeyRaw(isReinforce)`, `getCharacterName(isReinforce)`,
  `getMainTextureID(isReinforce)`, `getSubTextureID(isReinforce)`,
  `getRewardItemKeyListSize(isReinforce)` / `getRewardItemKeyByIndex`,
  `getPosition()`, `getNextSpawnLeftTime(serverUtc)` and `isEventBoss()`.
  `ToClient_isReinforceBoss(index)` picks the form.
- A record without spawn times is the window's "Random Spawn"
  (`LUA_WORLDMAP_BOSSLIST_RANDOM_APPEAR`): the Lua shows it when
  `getNextSpawnLeftTime` returns `-1`, and all five Field bosses show it in
  game while their `spawn_times` are empty.
- Dastard Bheg's 12 `reward_items` (11015 Bheg's Gloves, 8904 Concentrated
  Boss Crystal, 42435 Latent Boss Aura, 44926 Awakening Weapon Box, 15992
  Liverto Weapon Bundle, 15606 Ancient Magic Crystal of Crimson Flame -
  Power, 757010 Mythical Feather, 721002 Ancient Spirit Dust, 17839 and
  17829 Advice of Valks (+40) and (+30), 752023 Mass of Pure Magic, 768495
  Ode to Heroes of Yore) are the window's Main Rewards row in order.
- `is_event_boss` drives the event tag on a list entry
  (`eventTag:SetShow(bossInfo:isEventBoss() == true)`); 21878 Gift Box, the
  one record with it set, is an event boss with its own `Gift` image set.
- Quint and Muraka have the same `spawn_times` and the same `unknown_ids`
  (`158, 139` and `556, 560`), the only IDs shared by two records. They
  spawn together in game.
- The 8 reinforced forms have their own reward lists; 23001 Kzarka's
  reinforced list adds 4 items and drops 4. All reward values are below
  `2^24`, so they are item IDs with no enhancement level.
- Both groups of a World record hold the same number of times, but only
  Garmoth (13 of 14 times) and Vell have group 1 at group 0 minus 420
  minutes; the other bosses' groups are two unrelated timetables.
- The four Land of the Morning Light bosses (Bulgasal, Uturi, Sangoon,
  Golden Pig King) each have their own reinforced character (28733 to
  28736), all named Dark Bonghwang with the same model and the
  `Blackphoenix` image set.
- Khalk's two texture keys are spelled differently
  (`Combine_Etc_WorldMap_BossList_Img_Kalk`, `..._Kark`); both resolve in
  `texturestring_combine.xml`, so the pairing is by string index, not name.
- `fieldboss.dbss` holds every Field record's character, but it is a
  different list (694 characters); see [fieldboss](fieldboss_dbss.md).

## Open Questions

### unknown_ids

One u32 per spawn time, `101` to `1102` on client 3464, unique except for
the Quint and Muraka pair. The boss alert Lua (`panel_bossalert_alarm`)
works from character keys and times only, so nothing in Lua names these.

### unknown_flag

`1` on exactly the World records. The Lua only enables the Boss
Notification button on the World tab, but it decides that by tab, not by a
record field, so the byte cannot be told apart from the tab.

## In-Game Checks

### spawn_times as Minutes of the Week

Needs zone: anywhere with the world map

Every value is below 10,080, the minutes in a week. Open the world map,
then Boss Info on the World tab, and note the clock time with the countdown
of Kzarka, Garmoth and Vell. If each countdown ends on a value of one group
read as day `value // 1440` and minute of day `value % 1440` from the same
week start, `spawn_times` are minutes of the week; the group that matches
is the one this client's region uses (the other may be the second service
region of the same client), and the offset gives the week start.
