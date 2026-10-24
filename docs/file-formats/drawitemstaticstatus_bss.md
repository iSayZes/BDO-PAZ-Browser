# `drawitemstaticstatus.bss` Format

## Purpose

The prizes of the event ticket shop (`panel_event_ticketshop_all`, shown
while `_ContentsGroup_drawEvent` is on): one 26-byte row per prize with
the prize item and count, the coin item a draw costs and the item a lost
draw gives. Each event rewrites the file. On client 3483 the 8 rows are
the `[Event] Agent's Adventures` logs (Subjugation, Gathering, Fishing,
Barter, Training, Hunting, Cooking, Alchemy), drawn with `[Event] Agent's
Adventures` and with `[Event] Agent's Seal` as the lose item; the draw
prompt `LUA_EVENT_TICKETSHOP_POPUP_DESC` reads "There is a chance to
instantly obtain [Event] Agent's Seal".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | --------- |
| 1      | 1818 and later | 3483    | `drawitemstaticstatus.bss` | 228   | 8 Row   | 26        |

| Layout | File                       | Known         | Unknown      |
| ------ | -------------------------- | ------------- | ------------ |
| 1      | `drawitemstaticstatus.bss` | 148 B (64.9%) | 80 B (35.1%) |

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

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of prizes; `0` between events          |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (26 bytes)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | item_key      | The prize: `enchant_level << 24 \| item_id`                            |
| `+0x04` | u32  | coin_item_key | The item a draw costs; the same on every row                           |
| `+0x08` | u32  | lose_item_key | The item a lost draw gives; the same on every row                      |
| `+0x0C` | u32  | unknown_0c    | `0` on every row of every client checked                               |
| `+0x10` | u16  | index         | `1` to `row_count`, unique; the draw number `ToClient_RequestDrawItem` takes |
| `+0x12` | u16  | item_count    | Count of the prize                                                     |
| `+0x14` | u16  | unknown_14    | See Open Questions                                                     |
| `+0x16` | u16  | unknown_16    | See Open Questions                                                     |
| `+0x18` | u8   | unknown_18    | `0` or `1`; see Open Questions                                         |
| `+0x19` | u8   | unknown_19    | `0` or `1`; see Open Questions                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Events

The coin and lose items of four clients, with the prize count and the
values of `unknown_14` and `unknown_16`.

| Client | Prizes | `coin_item_key`                                  | `lose_item_key`                              | `unknown_14`       | `unknown_16`       |
| ------ | ------ | ------------------------------------------------ | -------------------------------------------- | ------------------ | ------------------ |
| 2276   | 16     | 752218 [Event] Box Full O' Love                  | 752219 [Event] Sweet Chocolate               | 10 to 50           | equal to `unknown_14` |
| 2583   | 12     | 752669 [Event] Old Moon ADV Lesson Ticket        | 752649 [Event] Jetina's Certificate Seal     | 10, 12 on one row  | 1                  |
| 3242   | 10     | 1000572 [Event] Exciting 10th Anniversary ADV Ticket | 1000571 [Event] Decade-Infused Pearl     | 3500               | 1                  |
| 3483   | 8      | 1000807 [Event] Agent's Adventures               | 1000808 [Event] Agent's Seal                 | 300                | 1                  |

The rows are not in `index` order. Clients 3103, 3169, 3303 and 3364 hold
an empty file (`row_count` `0`). One prize of client 2276 is Caphras Stone
with `item_count` `5000`; every other prize of the four clients has
`item_count` `1`.

## Field Names

The file is not in the archives of client 1784, and no sheet of a private
server's `DataSheets.bexcel` on that client has `Draw` in its name. The
names follow the draw wrapper getters of the client Lua (client 3482,
`panel_event_ticketshop_all_1` and `_2`):

- `getItemkey()` and `getItemCount()` fill the prize slot; the prize varies
  per row, which leaves `item_key` at `+0x00`, and `item_count` is `5000`
  on the Caphras Stone prize of client 2276.
- `getCoinItemKey()` and `getLoseItemKey()` name the two currency tooltips.
  `lose_item_key` is the item the draw prompt says a draw may give
  (`[Event] Agent's Seal`, `1000808`); `coin_item_key` is the event ticket
  the event's challenges hand out (`1000807`, "Use it to choose from
  various adventures").
- `getIndex()` is the number `ToClient_RequestDrawItem` and
  `ToClient_CheckCanDrawItem` take; `index` is the only field that runs
  from `1` to `row_count`.

The Lua reads five more values per prize: `getCoinCount()` (the `{ticket}`
count of the draw prompt), `getLoseCoinCount()`, `getDrawMaxCount()` and
`getDrawMinCount()` (a prize shows sold out when max minus min is `0` or
less), and `getIsSpecialItem()`. They are the leads for the five unnamed
fields.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the index, the prize with its icon and LOC name, the coin and lose items
  and the prize count.

## Open Questions

### Which of `unknown_14` and `unknown_16` Is the Coin Count

One of the two is likely `getCoinCount()` and the other
`getLoseCoinCount()`. `unknown_16` is `1` on every event since client 2583,
and the client 3483 coin item is a single log a player uses to start one
adventure, which fits a cost of one coin per draw. `unknown_14` (`300` on
client 3483) equals the `[Event] Agent's Seal x300` each Agent's
Adventures quest rewards, which fits the lose count. On client 2276 both
fields hold the same value on every row, so that client cannot split them.

### What `unknown_18` and `unknown_19` Flag

On client 2276 `unknown_18` is `1` on 5 of 16 prizes: the TET (IV) Black
Distortion Earring (`67120717`, Black Distortion Earring at level 4), the
Choose Your Ship License: Epheria Carrack Box, Choose Your TET (IV)
Blackstar Weapon Box, Choose Your TET (IV) Manos Accessory Box and Choose
Your Horse Emblem: Dream Horse Box. These are the highest prizes, a lead
for `getIsSpecialItem()`. `unknown_19` is `1` on 14 of 16 prizes and `0`
on the Combat/Skill EXP Exchange Coupon and the Weapon Exchange Coupon
Box. Both bytes are `0` on every later event checked.

### What `unknown_0c` Holds

`unknown_0c` is `0` on every row of clients 2276, 2583, 2765, 3030, 3242
and 3483. With `getDrawMaxCount()` and `getDrawMinCount()` both unplaced,
it may be one of them.
