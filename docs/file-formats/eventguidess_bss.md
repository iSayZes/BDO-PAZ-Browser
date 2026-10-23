# `eventguidess.bss` Format

## Purpose

The events of the Event Guide window `Panel_EventGuide_Total`: on client
3482 162 events, from the current Halloween world boss back to the
Blackstar gift of 2023. Each event has a Korean title, page text and
period text, a list icon and a page background texture, its UTC start and
end, the keyword of its web page, an optional button that opens a UI
window, a Hot or New tag, its event key and the reward items it shows. The
Lua lists the events whose end is still ahead
(`eventGuideSS:isEnd(getServerUtc64())`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records | Row bytes                  |
| ------ | -------------- | ------- | ------------------ | ------ | ------- | -------------------------- |
| 2      | 3012 and later | 3482    | `eventguidess.bss` | 77,912 | 162 Row | 375 to 623, 481 on average |
| 1      | 3002           | 3002    | `eventguidess.bss` | 6,579  | 15 Row  | 388 to 504, 438 on average |

| Layout | File               | Known             | Unknown    |
| ------ | ------------------ | ----------------- | ---------- |
| 2      | `eventguidess.bss` | 77,912 B (100.0%) | 0 B (0.0%) |
| 1      | `eventguidess.bss` | 6,579 B (100.0%)  | 0 B (0.0%) |

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

None. The handler reads this file alone; it shows the icon from
`texturestring_combine.xml` when that file is there.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                  |
| ------- | ---------- | ----- | -------------------------------------- |
| `+0x00` | u32        | count | Number of events; `162` on client 3482 |
| `+0x04` | Row[count] | rows  | See Row                                |

### Row (variable: 105 bytes + texts and rewards)

| Offset                  | Type                 | Field            | Notes |
| ----------------------- | -------------------- | ---------------- | ----- |
| `+0x00`                 | str16                | main_title_kr    | `getMainTitle()`: Korean event name in the list |
| `main_title_kr+0x00`    | str16                | main_desc_kr     | `getMainDesc()`: Korean headline of the page; the same text as `main_title_kr` on all 162 rows. See Open Questions |
| `main_desc_kr+0x00`     | str16                | sub_desc_kr      | `getSubDesc()`: Korean page text |
| `sub_desc_kr+0x00`      | str16                | period_desc_kr   | `getPeriodDesc()`: Korean period text (`2026년 10월 22일(목) 정기점검 후 ~ ...`) |
| `period_desc_kr+0x00`   | str8                 | icon             | `getIcon()`: UI texture ID of the list icon (`Combine_Tab_Icon_Daily_Select`) |
| `icon+0x00`             | str8                 | texture_bg       | `getTextureBg()`: UI texture ID of the page background (`Combine_Etc_Event_Halloween12`) |
| `texture_bg+0x00`       | u64                  | start_time       | Event start, UTC Unix seconds |
| `texture_bg+0x08`       | u64                  | end_time         | Event end, UTC Unix seconds; `isEnd()` compares it with the server time. 2099-12-31 23:59 on 5 rows |
| `texture_bg+0x10`       | str8                 | web_keyword      | `getWebKeyword()`: web page keyword, the event's date and number (`2610210002`) |
| `web_keyword+0x00`      | str8                 | web_hash_id      | `getWebHashID()`; empty on all 162 rows |
| `web_hash_id+0x00`      | str8                 | function         | Script of the page button, `ToClient_RequestEventGuideFunctionAt()` (`openui(newquest)`, `openui(cashshop)`); empty on 58 rows, `isFunctionEmpty()` |
| `function+0x00`         | str16                | function_desc_kr | `getFunctionDesc()`: Korean button text (`신규 의뢰 바로가기`) |
| `function_desc_kr+0x00` | u8                   | tag              | `getTag()`: `__eEventGuideTag_Hot`, `__eEventGuideTag_New` or none; `0` on 154 rows, `1` on 1, `2` on 7 |
| `function_desc_kr+0x01` | u32                  | event_key        | Event key, unique; `1` to `230` on client 3482 |
| `function_desc_kr+0x05` | u32                  | reward_count     | `getRewardCount()`; `0` to `7` |
| `function_desc_kr+0x09` | u32[reward_count]    | rewards          | `getRewardAt(i)`: item keys |

## Layout 1

Layout 2 without `function_desc_kr`.

### Row (variable: 97 bytes + texts and rewards)

| Offset                | Type              | Field          | Notes |
| --------------------- | ----------------- | -------------- | ----- |
| `+0x00`               | str16             | main_title_kr  |       |
| `main_title_kr+0x00`  | str16             | main_desc_kr   |       |
| `main_desc_kr+0x00`   | str16             | sub_desc_kr    |       |
| `sub_desc_kr+0x00`    | str16             | period_desc_kr |       |
| `period_desc_kr+0x00` | str8              | icon           |       |
| `icon+0x00`           | str8              | texture_bg     |       |
| `texture_bg+0x00`     | u64               | start_time     |       |
| `texture_bg+0x08`     | u64               | end_time       |       |
| `texture_bg+0x10`     | str8              | web_keyword    |       |
| `web_keyword+0x00`    | str8              | web_hash_id    |       |
| `web_hash_id+0x00`    | str8              | function       |       |
| `function+0x00`       | u8                | tag            |       |
| `function+0x01`       | u32               | event_key      |       |
| `function+0x05`       | u32               | reward_count   |       |
| `function+0x09`       | u32[reward_count] | rewards        |       |

## Field Names

The names follow the getters `panel_eventguide_total_1.luac` and
`panel_eventguide_total_2.luac` (client 3482) call on
`ToClient_RequestEventGuideAt(index)`: `getMainTitle()`, `getMainDesc()`,
`getSubDesc()`, `getPeriodDesc()`, `getIcon()`, `getTextureBg()`,
`isEnd(time)`, `getWebKeyword()`, `getWebHashID()`, `isFunctionEmpty()`,
`getFunctionDesc()`, `getTag()`, `getRewardCount()` and `getRewardAt(i)`.
`start_time` and `end_time` are told apart by their order and by the
period text: the first row's `2026-10-22 09:00` to `2026-11-05 09:00`
UTC are the maintenance times its `period_desc_kr` names. Client 1784 has
no file and no matching sheet.

## Notes

- On client 3482 the first row holds event key `230` and the last key
  `1`; past events stay in the file and the Lua hides them.
- Some rows have a `function_desc_kr` and an empty `function`;
  `isFunctionEmpty()` hides their button.

## Open Questions

### Title and Main Description Order

`main_title_kr` and `main_desc_kr` hold the same text on every row of
clients 3251 and 3482, so the data does not show which of the two
`getMainTitle()` reads.

### Tag Values

`tag` is `1` on one row and `2` on seven. The Lua compares it with
`__eEventGuideTag_Hot` and `__eEventGuideTag_New`, whose values are set
by the client exe.
