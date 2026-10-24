# `journalinfostaticstatus.bss` Format

## Purpose

The main quest boards of `Panel_Window_Journal_All`: on client 3482 two
journal lists, Morning Land (27 journals) and Edania (14). Each journal is
one boss or castle card of a board page: its chapter tab, its UI type and
place on the page, the quest chain it tracks, the `GAME` sheet keys of its
chapter, title and story text, its card and button textures, the
bookshelf quest it opens once cleared (chosen by condition), and the
textures it switches to as its quests are cleared. After the lists come 21
texture IDs and string keys per list for the board frame, the page and the
book view. The Lua reads a journal with
`ToClient_getJournalInfo(list, chapter, uiTypeIndex, journal)` and the list
textures with `ToClient_getJournalTextureInfo(list, slot)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records                                                                                    | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ------ | ------------------------------------------------------------------------------------------ | --------- |
| 3      | 3473 and later | 3483    | `journalinfostaticstatus.bss` | 22,717 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 2      | 3052 to 3464   | 3464    | `journalinfostaticstatus.bss` | 22,635 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 1      | 3002 to 3045   | 3045    | `journalinfostaticstatus.bss` | 17,673 | 42 Book Quest, 50 Ed Texture, 34 Journal, 2 Journal List, 2 Select Texture, 2 Texture Info | 10        |

| Layout | File                          | Known            | Unknown      |
| ------ | ----------------------------- | ---------------- | ------------ |
| 3      | `journalinfostaticstatus.bss` | 22,095 B (97.3%) | 622 B (2.7%) |
| 2      | `journalinfostaticstatus.bss` | 22,095 B (97.6%) | 540 B (2.4%) |
| 1      | `journalinfostaticstatus.bss` | 17,217 B (97.4%) | 456 B (2.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 3             |
| 3482   | Layout 3             |
| 3474   | Layout 3             |
| 3473   | Layout 3             |
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
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | No documented layout |
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

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Key hashes of the `GAME` sheet keys, for their LOC type 37 text |
| `languagedata_en.loc` | Optional | LOC type 37 text of the chapter, title and story keys |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                | Type                                  | Field              | Notes                                         |
| --------------------- | ------------------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`               | char[4]                               | magic              | ASCII `PABR`                                  |
| `+0x04`               | u32                                   | journal_list_count | Number of journal lists; `2` on client 3482   |
| `+0x08`               | Journal List[journal_list_count]      | journal_lists      | See Journal List; list `0` is Morning Land, `1` Edania |
| `journal_lists+0x00`  | u32                                   | texture_info_count | Equals `journal_list_count`                   |
| `journal_lists+0x04`  | Texture Info[texture_info_count]      | texture_infos      | One per journal list, in list order           |
| `texture_infos+0x00`  | String Table                          | string_table       | See String Table                              |
| `string_table+0x00`   | u32                                   | table_start        | Offset of the string table, where `texture_infos` ends |
| `string_table+0x04`   | u32                                   | zero               | Always `0`                                    |

### Journal List (variable: 4 bytes + journals)

| Offset  | Type                    | Field         | Notes                       |
| ------- | ----------------------- | ------------- | --------------------------- |
| `+0x00` | u32                     | journal_count | `27` and `14` on client 3482 |
| `+0x04` | Journal[journal_count]  | journals      | See Journal                 |

### Journal (variable: 64 bytes + book quests and ed textures)

Every `*_ref` field and `unknown_22` is an index into `strings`.

| Offset              | Type                          | Field                      | Notes |
| ------------------- | ----------------------------- | -------------------------- | ----- |
| `+0x00`             | u16                           | chapter_index              | `_chapterIndex`: chapter tab, from `1` (`1` and `2` in both lists) |
| `+0x02`             | u16                           | ui_type                    | `ToClient_getJournalUIType()`: `0` a boss card with normal and over textures, `1` a visual card (`Static_QuestVisual`) |
| `+0x04`             | u16                           | ui_type_index              | `_uiTypeIndex`: page of the chapter, from `1`; `1` holds the type `0` cards, `2` the type `1` cards |
| `+0x06`             | u16                           | journal_index              | `_journalIndex`: card on the page, from `1` |
| `+0x08`             | u16                           | quest_group_no             | `_questGroupNo`: the quest chain the card tracks; a `quest.dbss` chain on all 41 journals of client 3482 |
| `+0x0A`             | u16                           | unknown_0a                 | `2` to `39`; at most the highest quest ID of the chain on all 41 journals. See Open Questions |
| `+0x0C`             | u32                           | chapter_string_ref         | `getChapterString()`: `GAME` key of the chapter tab (`LUA_MORNINGLAND_QUESTBOARD_TAB1`) |
| `+0x10`             | u32                           | scenario_desc_ref          | `getScenarioDesc()`: `GAME` key of the story text (`LUA_MORNING_QUESTBOARD_DESC_1`) |
| `+0x14`             | u32                           | title_string_ref           | `getTitleString()`: `GAME` key of the boss or chapter title (`LUA_MORNINGMAINPROGRESS_TITLE_01`) |
| `+0x18`             | u16                           | unknown_18                 | `0` on every journal |
| `+0x1A`             | u32                           | texture_normal_ref         | `ToClient_getJournalInfoTextureID(info, 0)`: card texture ID (`Combine_Etc_MorningLand_MainQuest_Boss_05_Normal`) |
| `+0x1E`             | u32                           | texture_over_ref           | `ToClient_getJournalInfoTextureID(info, 1)`: mouse-over texture ID; the same as `texture_normal_ref` on the type `1` cards |
| `+0x22`             | u32                           | unknown_22                 | Condition script: empty on Morning Land, a `clearquest(...)` of the chain before on every Edania journal (`clearquest(9100,5)`) |
| `+0x26`             | u32[3]                        | detail_btn_texture_id_refs | `getDetailBtnTextureId(0)` to `(2)`: texture IDs of the detail button |
| `+0x32`             | u32                           | detail_btn_string_ref      | `getDetailBtnString()`: `GAME` key shown as the boss name on Edania (`LUA_EDANIA_JOURNAL_1`); empty on Morning Land |
| `+0x36`             | u16                           | unknown_36                 | `0` on 37 journals; `305`, `131`, `123`, `104` on chains `9303` to `9306`, the highest quest ID of each chain on client 3482 |
| `+0x38`             | u32                           | book_quest_count           | `1` or `2`                    |
| `+0x3C`             | Book Quest[book_quest_count]  | book_quests                | See Book Quest                |
| `book_quests+0x00`  | u32                           | ed_texture_count           | `1` or `2`                    |
| `book_quests+0x04`  | Ed Texture[ed_texture_count]  | ed_textures                | See Ed Texture                |

### Book Quest (10 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | condition_ref    | Condition script: empty on 33 entries, else `clearquest(8504,21);` or a class check (`checkClass(15);<or>checkClass(30);`) |
| `+0x04` | u16  | book_quest_group | `getBookQuestNo()._group`: chain of the bookshelf quest the cleared card opens (`8542` to `8554`, `8700` to `8714`, `9131` to `9137`, `9331` to `9337`) |
| `+0x06` | u16  | book_quest_id    | `getBookQuestNo()._quest`; `book_quest_group`, `book_quest_id` is a `quest.dbss` quest on 49 of 49 entries |
| `+0x08` | u16  | unknown_08       | `2` to `41`; see Open Questions |

### Ed Texture (10 bytes)

| Offset  | Type | Field              | Notes |
| ------- | ---- | ------------------ | ----- |
| `+0x00` | u32  | texture_normal_ref | Texture ID ending in `_ed`, `_ed_S_Normal` or `_ed_H_Normal` |
| `+0x04` | u32  | texture_over_ref   | The matching over texture ID |
| `+0x08` | u16  | unknown_08         | A quest ID of `quest_group_no`; on chains `8504` to `8507` and `8512`, `8513` the two values are the quest IDs of the two `clearquest` conditions |

### Texture Info (84 bytes)

| Offset  | Type    | Field             | Notes |
| ------- | ------- | ----------------- | ----- |
| `+0x00` | u32[21] | texture_info_refs | Slot `n` is `ToClient_getJournalTextureInfo(list, n)`; see [Texture Info Slots](#texture-info-slots) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `342` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Each text is stored once               |

## Layout 2

Layout 3 without `unknown_36`.

### Journal (variable: 62 bytes + book quests and ed textures)

| Offset              | Type                          | Field                      | Notes |
| ------------------- | ----------------------------- | -------------------------- | ----- |
| `+0x00`             | u16                           | chapter_index              |       |
| `+0x02`             | u16                           | ui_type                    |       |
| `+0x04`             | u16                           | ui_type_index              |       |
| `+0x06`             | u16                           | journal_index              |       |
| `+0x08`             | u16                           | quest_group_no             |       |
| `+0x0A`             | u16                           | unknown_0a                 |       |
| `+0x0C`             | u32                           | chapter_string_ref         |       |
| `+0x10`             | u32                           | scenario_desc_ref          |       |
| `+0x14`             | u32                           | title_string_ref           |       |
| `+0x18`             | u16                           | unknown_18                 |       |
| `+0x1A`             | u32                           | texture_normal_ref         |       |
| `+0x1E`             | u32                           | texture_over_ref           |       |
| `+0x22`             | u32                           | unknown_22                 |       |
| `+0x26`             | u32[3]                        | detail_btn_texture_id_refs |       |
| `+0x32`             | u32                           | detail_btn_string_ref      |       |
| `+0x36`             | u32                           | book_quest_count           |       |
| `+0x3A`             | Book Quest[book_quest_count]  | book_quests                |       |
| `book_quests+0x00`  | u32                           | ed_texture_count           |       |
| `book_quests+0x04`  | Ed Texture[ed_texture_count]  | ed_textures                |       |

## Layout 1

The list textures are two lists: the three select button textures (slots
`0` to `2` of Layout 3), then four slots (`3` to `6`) per journal list.

### File Layout

| Offset                   | Type                                  | Field                 | Notes                                         |
| ------------------------ | ------------------------------------- | --------------------- | --------------------------------------------- |
| `+0x00`                  | char[4]                               | magic                 | ASCII `PABR`                                  |
| `+0x04`                  | u32                                   | journal_list_count    | Number of journal lists                       |
| `+0x08`                  | Journal List[journal_list_count]      | journal_lists         | See Journal List                              |
| `journal_lists+0x00`     | u32                                   | select_texture_count  | Equals `journal_list_count`                   |
| `journal_lists+0x04`     | Select Texture[select_texture_count]  | select_textures       | See Select Texture                            |
| `select_textures+0x00`   | u32                                   | texture_info_count    | Equals `journal_list_count`                   |
| `select_textures+0x04`   | Texture Info[texture_info_count]      | texture_infos         | See Texture Info                              |
| `texture_infos+0x00`     | String Table                          | string_table          | See String Table                              |
| `string_table+0x00`      | u32                                   | table_start           | Offset of the string table                    |
| `string_table+0x04`      | u32                                   | zero                  | Always `0`                                    |

### Select Texture (12 bytes)

| Offset  | Type   | Field               | Notes                                                        |
| ------- | ------ | ------------------- | ------------------------------------------------------------ |
| `+0x00` | u32[3] | select_texture_refs | Base, over and click texture of the board select button      |

### Texture Info (16 bytes)

| Offset  | Type   | Field             | Notes                                                 |
| ------- | ------ | ----------------- | ----------------------------------------------------- |
| `+0x00` | u32[4] | texture_info_refs | Slots `3` to `6` of Layout 3: frame, bar, title key, text key |

## Texture Info Slots

The Lua reads the slots with `ToClient_getJournalTextureInfo(list, n)`; the
values are those of list `0` on client 3482.

| Slot | Lua use                                                    | List `0` value |
| ---- | ---------------------------------------------------------- | -------------- |
| 0    | Board select button, base (`panel_window_journal_select_all`) | `Combine_Etc_StartMap_01_Btn_03_Normal_2` |
| 1    | Board select button, over                                  | `Combine_Etc_StartMap_01_Btn_03_Over_2` |
| 2    | Board select button, click                                 | `Combine_Etc_StartMap_01_Btn_03_Click_2` |
| 3    | Board frame texture                                        | `Combine_Etc_MorningLand_MainQuest_Frame` |
| 4    | Line on the type `0` pages                                 | `Etc_MorningLand_MainQuest_Center_Bar` |
| 5    | `GAME` key of the board title                              | `LUA_EDANIA_JOURNAL_TITLE_NAME1` |
| 6    | `GAME` key of the board text                               | `LUA_EDANIA_JOURNAL_TITLE_DESC1` |
| 7    | Story page background                                      | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_BG` |
| 8    | Story page button, base                                    | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Normal` |
| 9    | Story page button, over                                    | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Over` |
| 10   | Story page button, click                                   | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Click` |
| 11   | Book background                                            | `Combine_Etc_Morning_Book_BG` |
| 12   | Book left button, base                                     | `Combine_Etc_Morning_Book_01_Btn_L_Normal` |
| 13   | Book left button, over                                     | `Combine_Etc_Morning_Book_01_Btn_L_Over` |
| 14   | Book left button, click                                    | `Combine_Etc_Morning_Book_01_Btn_L_Click` |
| 15   | Book right button, base                                    | `Combine_Etc_Morning_Book_01_Btn_R_Normal` |
| 16   | Book right button, over                                    | `Combine_Etc_Morning_Book_01_Btn_R_Over` |
| 17   | Book right button, click                                   | `Combine_Etc_Morning_Book_01_Btn_R_Click` |
| 18   | Hidden book page                                           | `Combine_Etc_Morning_Book_Image_Secret_02` |
| 19   | Left page effect                                           | `UI_Book_02B` |
| 20   | Right page effect                                          | `UI_Book_02A` |

## Field Names

The names follow `panel_window_journal_all_1.luac`,
`panel_window_journal_page_all.luac`, `panel_window_journal_book_all.luac`
and `panel_window_journal_select_all.luac` (client 3482): the members
`_chapterIndex`, `_uiTypeIndex`, `_journalIndex` and `_questGroupNo` of the
journal info, its getters `getChapterString()`, `getScenarioDesc()`,
`getTitleString()`, `getDetailBtnTextureId(i)`, `getDetailBtnString()` and
`getBookQuestNo()`, and `ToClient_getJournalUIType()`,
`ToClient_getJournalInfoTextureID(info, i)` and
`ToClient_getJournalTextureInfo(list, n)`. The chapter and page fields are
told apart by their ranges: `ui_type` is `0` or `1` and `ui_type_index`
`1` or `2`, and every type `1` card sits on page `2`. Client 1784 has no
file and no matching sheet.

## Notes

- The strings are not in walk order: the texture info strings come last
  (`300` to `341` on client 3482).
- The `GAME` keys resolve through `stringtable.bss` and LOC type 37; the
  Lua passes them to `PAGetString(Defines.StringSheet_GAME, ...)`.

## Open Questions

### Quest Counts of a Journal

`unknown_0a` and the `unknown_08` of a book quest look like quest counts of
the chain. On client 3482 `unknown_08` equals the highest quest ID of
`quest_group_no` on 17 of the 33 single book quests (`8503`: 30, `8524`:
22), and `unknown_0a` is at most that ID on all 41 journals. The Lua
divides `ToClient_getJournalInfoClearQuestCount(info)` by
`_totalQuestCount`, but no getter shows which field that is.

### Highest Quest ID on Four Edania Journals

`unknown_36` is `0` except on chains `9303` to `9306`, where it equals the
highest quest ID of the chain in `quest.dbss`. Layouts 1 and 2 have no `unknown_36`.
