# `tutorial_startevent.bss` Format

## Purpose

What a Black Spirit guide step shows when it starts: an item to look up in
the inventory, a black frame and a white frame around a UI panel or one of
its controls, the controls the player can still click while the rest of
the UI is greyed out, the snapping effect and one Lua call. The steps of
[`tutorial.bss`](tutorial_bss.md) name these rows in `start_event_keys`.
It is a PABR table of 101-byte rows; panel and control names are stored as
hashes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                                   | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ----------------------------------------- | --------- |
| 2      | 1725 and later | 3482    | `tutorial_startevent.bss` | 1,770 | 34 Highlight, 85 Selected Control, 17 Row | 8         |
| 1      | 1717           | 1717    | `tutorial_startevent.bss` | 851   | 28 Highlight, 14 Row                      | 21        |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 2      | `tutorial_startevent.bss` | 1,770 B (100.0%) | 0 B (0.0%) |
| 1      | `tutorial_startevent.bss` | 851 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
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
| 1717   | Layout 1 |
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

| File           | Required | Role                                                                                   |
| -------------- | -------- | -------------------------------------------------------------------------------------- |
| `tutorial.bss` | Optional | The steps that start each event, and the panel and control names its step scripts use  |

The handler links each row to the `tutorial.bss` steps that list its key,
and the `tutorial.bss` view links each start event key back here. The
item name is LOC type 0 when `languagedata_*.loc` is loaded.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of start events                        |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (101 bytes)

| Offset  | Type                | Field               | Notes                                                                                                         |
| ------- | ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32                 | key                 | Start event key, `1` to `17` on client 3482; `ToClient_getTutorialStartEventStaticStatusWrapper(key)`                        |
| `+0x04` | u8                  | item_where_type     | Where to look for `item_key`: `1` on key `1`; `32` on the rows without an item; see Open Questions            |
| `+0x05` | u32                 | item_key            | `getItemEnchantKey()`: the item the inventory search looks up (`331059` on key `1`); `0` for none             |
| `+0x09` | Highlight           | black_bg            | The black frame: `getUseBlackBG()`, `getBlackPanel()`, `getBlackChildControl()`, `getBlackChildControlIndex()`, `getBlackOffset()` |
| `+0x1E` | Highlight           | white_bg            | The white frame: `getUseWhiteBG()`, `getWhitePanel()`, `getWhiteChildControl()`, `getWhiteChildControlIndex()`, `getWhiteOffset()` |
| `+0x33` | u8                  | white_ignore        | `getWhiteIgnore()`: `1` places the white frame but does not show it; `1` on 16 of 17 rows (client 3482)      |
| `+0x34` | u32                 | selected_panel_hash | `getSelectedPanel()`: `ascii_key_hash()` of the panel whose controls stay clickable; `0` for none             |
| `+0x38` | Selected Control[5] | selected_controls   | `getSelectedChildControl(i)` and `getSelectedChildControlIndex(i)`; unused entries are zero                   |
| `+0x60` | u8                  | snapping_effect_on  | `getSnappingEffectOn()`: `1` points the guide effect at the highlighted control                               |
| `+0x61` | u32                 | do_lua              | Index into `strings`: the Lua call `ToClient_tutorialStartEventDoLua()` runs (`InventoryWindow_Close()`); empty on 16 of 17 rows (client 3482) |

### Highlight (21 bytes)

| Offset  | Type   | Field               | Notes                                                                                           |
| ------- | ------ | ------------------- | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u8     | use_bg              | `1` shows the frame                                                                             |
| `+0x01` | u32    | panel_hash          | `ascii_key_hash()` of the panel (`Panel_Window_PetList_All`); `0` for none                      |
| `+0x05` | u32    | child_control_hash  | `ascii_key_hash()` of the control inside the panel (`Button_AllUnSeal`); `0` frames the panel   |
| `+0x09` | u32    | child_control_index | Which copy of a repeated control (`2` for the third `Template_Button_Unseal`); `FindControlByIndex(child, index)` |
| `+0x0D` | f32[2] | offset              | x and y the frame grows by around the control (`55, 55`, `20, 20`)                              |

### Selected Control (8 bytes)

| Offset  | Type | Field               | Notes                                                    |
| ------- | ---- | ------------------- | -------------------------------------------------------- |
| `+0x00` | u32  | child_control_hash  | `ascii_key_hash()` of a control of `selected_panel_hash` |
| `+0x04` | u32  | child_control_index | As in Highlight                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                      |
| ------- | ------------------ | ------------ | ------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings                          |
| `+0x04` | pstr[string_count] | strings      | String `0` is empty; the `do_lua` calls    |

## Layout 1

The row has no `selected_panel_hash` and no `selected_controls`.

### Row (57 bytes)

| Offset  | Type      | Field              | Notes          |
| ------- | --------- | ------------------ | -------------- |
| `+0x00` | u32       | key                | As in Layout 2 |
| `+0x04` | u8        | item_where_type    | As in Layout 2 |
| `+0x05` | u32       | item_key           | As in Layout 2 |
| `+0x09` | Highlight | black_bg           | As in Layout 2 |
| `+0x1E` | Highlight | white_bg           | As in Layout 2 |
| `+0x33` | u8        | white_ignore       | As in Layout 2 |
| `+0x34` | u8        | snapping_effect_on | As in Layout 2 |
| `+0x35` | u32       | do_lua             | As in Layout 2 |

## UI Names

Every hash in the file is the `ascii_key_hash()` (lookup3, seed
`0xC5EDE`) of a client UI name. On client 3482 the file holds 21
different hashes. 17 of them are names the `tutorial.bss` step scripts
use (`uiinputevent(Panel_Window_PetList_All, Button_AllUnSeal,
Mouse_LUp)`); the other four are `Panel_Widget_ServantIcon`,
`Button_Icon_10`, `Static_FeedingBg` and `Static_IconBg0`, the names the
source sheet stores (Field Names). The handler resolves all 21.

| Panel                          | Controls the rows name                                                                                    |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `Panel_Window_Inventory_All`   | (the item slot the inventory search finds)                                                                |
| `Panel_Window_PetRegister_All` | `Edit_Naming`, `Button_Yes`                                                                               |
| `Panel_Window_MessageBox_All`  | `Button_Yes`                                                                                              |
| `Panel_Widget_ServantIcon`     | `Button_Icon_10`                                                                                          |
| `Panel_Window_PetList_All`     | `Template_Button_Unseal`, `Template_Button_Seal`, `Button_AllUnSeal`, `Template_Button_GroupIndex1`, `Button_AllSeal_Group1`, `Button_FeedingAll`, `Static_FeedingBg`, `Static_IconBg0`, `Button_FeedOne` |
| `Panel_Widget_Function`        | `Button_FindNavi`                                                                                         |
| `Panel_NpcNavi_All`            | `Button_001`                                                                                              |

## Field Names

Every field is a column of the `Tutorial_Start_Event_Table` sheet of a
private server's `DataSheets.bexcel` on client 1784: `Key`,
`ItemWhereType`, `ItemKey`, `UseBlackBG`, `BlackPanel`,
`BlackChildControl`, `BlackChildControlIndex`, `BlackOffset`, the same
five `White` columns, `WhiteIgnore`, `SnappingEffectOn`, `DoLua`,
`SelectedPanel` and `SelectedChildControl_0` to `_4` with their
`SelectedChildControlIndex_0` to `_4`. All of them match on the sheet's
17 rows, against client 1784's file and client 3482's file; panel and
control names match as their hashes. The sheet also has five `Focus`
columns (`UseFocusBG`, `FocusPanel`, `FocusChildControl`,
`FocusChildControlIndex`, `FocusOffset`); the file does not store them,
and they match the `white_bg` bytes on only 10 of the 17 rows. The Lua
getters in `panel_widget_tutorial_guideui_1.luac` (`startEvent__XXX()`)
read the same fields and no focus frame.

## Notes

- The rows are not in key order: the file runs from key `15` down to `1`,
  then `17` and `16`.
- `startEvent__XXX()` searches the inventory for the item's name first;
  when it finds the slot, the white frame and the snapping effect go
  around that slot in place of `white_bg`'s panel. Key `1` uses it for the
  pet item `331059`, with no white panel and an offset of `100, 100`.
- `getSelectedControlListSize()` reads the five-entry list; the Lua skips
  an entry whose control is `0`.
- Client 1784 and client 3482 store the same rows; the only change is
  `item_where_type` on the rows without an item, `28` on client 1784 and
  `32` on client 3482.
- Start event `11` is listed by no `tutorial.bss` step on client 3482.

## Open Questions

### What `item_where_type` `32` Is

The sheet leaves `ItemWhereType` empty on the 16 rows without an item,
and the file stores `28` there on client 1784 and `32` on client 3482.
A value that moves with the client looks like the item location enum's
count (`CppEnums.ItemWhereType.eCount` is `__eItemWhereTypeCount`), but
the Lua holds only the names and the Lua of the guide never reads the
field, so the enum values are not known.
