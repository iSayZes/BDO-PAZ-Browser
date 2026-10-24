# `itembuildkit.bss` Format

## Purpose

The siege build kits: per kit item the structures it can place in a Node
or Conquest War (fences, barricades, the fort and command post annexes),
each with the condition script that allows it, a contents event, its icon
and its Korean description. Clients 1784 and 3482 have one kit, item 59791
`[Guild] Node/Conquest War Annex Assembly Tool`. The siege installation
window (`panel_house_installationmode_siege_all_1.luac`) lists the
structures with `ToClient_getSiegeInstallableListSize()` and
`ToClient_getSiegeInstallableListByIndex(index)` and places one with
`ToClient_requestSiegeInstallationStart(itemEnchantKey, characterKey)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records   | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | --------- | --------- |
| 3      | 2507 and later | 3483    | `itembuildkit.bss` | 41,439 | 103 Entry | 35        |
| 2      | 1704 to 2503   | 2503    | `itembuildkit.bss` | 56,950 | 56 Entry  | 26        |
| 1      | 1680 to 1698   | 1698    | `itembuildkit.bss` | 2,770  | 56 Entry  | 22        |

| Layout | File               | Known             | Unknown      |
| ------ | ------------------ | ----------------- | ------------ |
| 3      | `itembuildkit.bss` | 40,512 B (97.8%)  | 927 B (2.2%) |
| 2      | `itembuildkit.bss` | 56,950 B (100.0%) | 0 B (0.0%)   |
| 1      | `itembuildkit.bss` | 2,770 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 3 |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3473   | Layout 3 |
| 3464   | Layout 3 |
| 3458   | Layout 3 |
| 3454   | Layout 3 |
| 3444   | Layout 3 |
| 3435   | Layout 3 |
| 3426   | Layout 3 |
| 3418   | Layout 3 |
| 3412   | Layout 3 |
| 3402   | Layout 3 |
| 3396   | Layout 3 |
| 3387   | Layout 3 |
| 3381   | Layout 3 |
| 3373   | Layout 3 |
| 3364   | Layout 3 |
| 3356   | Layout 3 |
| 3349   | Layout 3 |
| 3342   | Layout 3 |
| 3335   | Layout 3 |
| 3326   | Layout 3 |
| 3321   | Layout 3 |
| 3314   | Layout 3 |
| 3303   | Layout 3 |
| 3302   | Layout 3 |
| 3293   | Layout 3 |
| 3283   | Layout 3 |
| 3275   | Layout 3 |
| 3267   | Layout 3 |
| 3258   | Layout 3 |
| 3251   | Layout 3 |
| 3242   | Layout 3 |
| 3235   | Layout 3 |
| 3229   | Layout 3 |
| 3212   | Layout 3 |
| 3203   | Layout 3 |
| 3193   | Layout 3 |
| 3186   | Layout 3 |
| 3177   | Layout 3 |
| 3169   | Layout 3 |
| 3158   | Layout 3 |
| 3151   | Layout 3 |
| 3144   | Layout 3 |
| 3133   | Layout 3 |
| 3125   | Layout 3 |
| 3118   | Layout 3 |
| 3111   | Layout 3 |
| 3103   | Layout 3 |
| 3095   | Layout 3 |
| 3086   | Layout 3 |
| 3072   | Layout 3 |
| 3062   | Layout 3 |
| 3052   | Layout 3 |
| 3045   | Layout 3 |
| 3037   | Layout 3 |
| 3030   | Layout 3 |
| 3021   | Layout 3 |
| 3012   | Layout 3 |
| 3002   | Layout 3 |
| 2995   | Layout 3 |
| 2987   | Layout 3 |
| 2978   | Layout 3 |
| 2970   | Layout 3 |
| 2959   | Layout 3 |
| 2951   | Layout 3 |
| 2942   | Layout 3 |
| 2935   | Layout 3 |
| 2932   | Layout 3 |
| 2923   | Layout 3 |
| 2919   | Layout 3 |
| 2907   | Layout 3 |
| 2900   | Layout 3 |
| 2891   | Layout 3 |
| 2882   | Layout 3 |
| 2872   | Layout 3 |
| 2863   | Layout 3 |
| 2855   | Layout 3 |
| 2849   | Layout 3 |
| 2844   | Layout 3 |
| 2834   | Layout 3 |
| 2825   | Layout 3 |
| 2819   | Layout 3 |
| 2811   | Layout 3 |
| 2803   | Layout 3 |
| 2794   | Layout 3 |
| 2783   | Layout 3 |
| 2774   | Layout 3 |
| 2765   | Layout 3 |
| 2756   | Layout 3 |
| 2750   | Layout 3 |
| 2743   | Layout 3 |
| 2736   | Layout 3 |
| 2726   | Layout 3 |
| 2717   | Layout 3 |
| 2709   | Layout 3 |
| 2703   | Layout 3 |
| 2695   | Layout 3 |
| 2684   | Layout 3 |
| 2672   | Layout 3 |
| 2665   | Layout 3 |
| 2657   | Layout 3 |
| 2649   | Layout 3 |
| 2644   | Layout 3 |
| 2637   | Layout 3 |
| 2629   | Layout 3 |
| 2619   | Layout 3 |
| 2612   | Layout 3 |
| 2606   | Layout 3 |
| 2602   | Layout 3 |
| 2601   | Layout 3 |
| 2592   | Layout 3 |
| 2583   | Layout 3 |
| 2575   | Layout 3 |
| 2567   | Layout 3 |
| 2560   | Layout 3 |
| 2553   | Layout 3 |
| 2545   | Layout 3 |
| 2538   | Layout 3 |
| 2529   | Layout 3 |
| 2519   | Layout 3 |
| 2513   | Layout 3 |
| 2510   | Layout 3 |
| 2507   | Layout 3 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
| 2089   | Layout 2 |
| 2081   | Layout 2 |
| 2073   | Layout 2 |
| 2067   | Layout 2 |
| 2063   | Layout 2 |
| 2059   | Layout 2 |
| 2052   | Layout 2 |
| 2044   | Layout 2 |
| 2039   | Layout 2 |
| 2032   | Layout 2 |
| 2025   | Layout 2 |
| 2011   | Layout 2 |
| 2005   | Layout 2 |
| 2000   | Layout 2 |
| 1996   | Layout 2 |
| 1991   | Layout 2 |
| 1985   | Layout 2 |
| 1980   | Layout 2 |
| 1969   | Layout 2 |
| 1964   | Layout 2 |
| 1958   | Layout 2 |
| 1950   | Layout 2 |
| 1945   | Layout 2 |
| 1937   | Layout 2 |
| 1933   | Layout 2 |
| 1927   | Layout 2 |
| 1921   | Layout 2 |
| 1914   | Layout 2 |
| 1908   | Layout 2 |
| 1897   | Layout 2 |
| 1892   | Layout 2 |
| 1886   | Layout 2 |
| 1881   | Layout 2 |
| 1871   | Layout 2 |
| 1866   | Layout 2 |
| 1862   | Layout 2 |
| 1854   | Layout 2 |
| 1846   | Layout 2 |
| 1838   | Layout 2 |
| 1832   | Layout 2 |
| 1826   | Layout 2 |
| 1822   | Layout 2 |
| 1818   | Layout 2 |
| 1804   | Layout 2 |
| 1794   | Layout 2 |
| 1790   | Layout 2 |
| 1784   | Layout 2 |
| 1774   | Layout 2 |
| 1771   | Layout 2 |
| 1762   | Layout 2 |
| 1759   | Layout 2 |
| 1754   | Layout 2 |
| 1749   | Layout 2 |
| 1743   | Layout 2 |
| 1737   | Layout 2 |
| 1731   | Layout 2 |
| 1725   | Layout 2 |
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
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

| File                         | Required | Role                                                                      |
| ---------------------------- | -------- | ------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a structure without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Item names (LOC type 0) and structure names (LOC type 6)                  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                        |
| ------------------- | -------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                 |
| `+0x04`             | u32            | kit_count    | Number of kits; `1` on clients 1784 and 3482 |
| `+0x08`             | Kit[kit_count] | kits         | See Kit                                      |
| `kits+0x00`         | String Table   | string_table | See String Table                             |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `kits` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                   |

### Kit (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                       |
| ------- | ------------------ | ----------- | ------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; 103 on client 3482     |
| `+0x04` | Entry[entry_count] | entries     | See Entry; one per structure the kit places |

### Entry (35 bytes)

| Offset  | Type | Field                 | Notes                                                                                     |
| ------- | ---- | --------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key              | The kit, a packed item key; the same in every entry of a kit                               |
| `+0x04` | u16  | character_key         | The structure placed (`2046` Wooden Fence, `12606` Barricade); unique within a kit          |
| `+0x06` | u32  | use_condition         | Index into `strings`: the condition script (`checksiegetower(0);checkInstallTentLevel(5);`) |
| `+0x0A` | u32  | contents_event_type   | `1` on every entry of clients 1784 and 3482                                                |
| `+0x0E` | u32  | contents_event_param1 | `15000` on every entry of client 1784, `5000` on client 3482                               |
| `+0x12` | u32  | icon_image_file       | Index into `strings`: the icon path (`New_Icon/03_ETC/06_Housing/00056071.dds`)            |
| `+0x16` | u32  | description           | Index into `strings`: the Korean description, with `<PAColor>` tags and `\n` escapes        |
| `+0x1A` | u32  | unknown_1a            | `0`, `30000000` or `50000000` on client 3482; see Open Questions                           |
| `+0x1E` | u32  | unknown_1e            | `0` on every entry of client 3482                                                          |
| `+0x22` | u8   | unknown_22            | `0`, `1` or `2` on client 3482; see Open Questions                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 73 on client 3482                                        |
| `+0x04` | pstr[string_count] | strings      | Condition scripts and descriptions UTF-16LE (`is_wide` 1), icon paths UTF-8; each text stored once |

## Layout 2

The entry ends after `description`. Only the Entry differs from Layout 3.

### Entry (26 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |
| `+0x16` | u32  | description           |       |

## Layout 1

The entry ends after `icon_image_file`: no description. Only the Entry
differs from Layout 2.

### Entry (22 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |

## Field Names

The `SiegeItemInstallation` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ItemKey`, `CharacterKey`, `UseCondition`,
`ContentsEventType`, `ContentsEventParam1`, `IconImageFile` and
`Description`, one sheet row per entry, in another order than the file.
Matched on (`ItemKey`, `CharacterKey`):

| Field                 | Column                | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------- | ------------------------ | ------------------------ |
| item_key              | `ItemKey`             | 56 of 56                 | 52 of 103                |
| character_key         | `CharacterKey`        | 56 of 56                 | 52 of 52                 |
| use_condition         | `UseCondition`        | 56 of 56                 | 28 of 52                 |
| contents_event_type   | `ContentsEventType`   | 56 of 56                 | 52 of 52                 |
| contents_event_param1 | `ContentsEventParam1` | 56 of 56                 | 0 of 52                  |
| icon_image_file       | `IconImageFile`       | 56 of 56                 | 52 of 52                 |
| description           | `Description`         | 56 of 56                 | 5 of 52                  |

The client 3482 misses are changed conditions and descriptions and the
parameter `5000` in place of `15000`. The sheet has no column for the three
fields Layout 3 adds.

## Notes

- `use_condition` calls `checksiegetower`, `checksiegetowercharacter`,
  `checkInstallTentLevel`, `checkiskingguild` and, on client 3482,
  `checksiege2024groupno`.
- On client 3482, `unknown_1a` is `30000000` on 6 entries and `50000000` on
  9, all of them with `unknown_22` `1`; these 15 entries (characters `12759`
  to `12790`) are the ones whose condition calls `checksiege2024groupno`.
- The handler (`_bss/itembuildkit/`) shows one row per entry: the kit, the
  structure with its name, the condition, the contents event, the icon and
  the description.

## Open Questions

### What the Three Fields Layout 3 Adds Hold

`unknown_1a` (`0`, `30000000`, `50000000`), `unknown_1e` (`0`) and
`unknown_22` (`0`, `1`, `2`) are new on client 2519 and match no sheet
column. `unknown_1a` may be a Silver cost of the 15 newer structures; the
client 3482 Lua reads no cost from the installable list.
