# `itemenchantbackendtest.dbss` Format

## Purpose

The front part of every [`itemenchant.dbss`](itemenchant_dbss.md) block:
for each (item, enchant level) the block from its packed key to
`life_restrict_type`, `0x2A` bytes into the Message Tail. Everything after
that, from Message Tail `+0x2B` to the crystal group at the block end, is in
[`itemenchantbackend.dbss`](itemenchantbackend_dbss.md). On client 3483
each of the 169,345 `itemenchant.dbss` blocks is, byte for byte, the block
of this file followed by the `itemenchantbackend.dbss` block of the same
key, and the file sizes add up: 76,122,866 + 126,919,140 bytes is the
203,042,002 of `itemenchant.dbss` plus one 4-byte count.

Unlike its two siblings, this file has no offset index: the blocks follow
each other in the order of `itemenchantoffset.dbss`, and a reader finds the
end of a block by walking its lists and strings.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes      | Records                                                                     | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ---------- | --------------------------------------------------------------------------- | --------- |
| 1      | 3435 and later | 3483    | `itemenchantbackendtest.dbss` | 76,122,866 | 276,167 Class Entry, 169,345 Icon Tail, 169,345 Message Tail, 169,345 Block | 5         |

| Layout | File                          | Known                | Unknown              |
| ------ | ----------------------------- | -------------------- | -------------------- |
| 1      | `itemenchantbackendtest.dbss` | 58,866,318 B (77.3%) | 17,256,548 B (22.7%) |

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
| 3426   | No documented layout |
| 3418   | No documented layout |
| 3412   | No documented layout |
| 3402   | No documented layout |
| 3396   | No documented layout |
| 3387   | No documented layout |
| 3381   | No documented layout |
| 3373   | No documented layout |
| 3364   | No documented layout |
| 3356   | No documented layout |
| 3349   | No documented layout |
| 3342   | No documented layout |
| 3335   | No documented layout |
| 3326   | No documented layout |
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No documented layout |
| 3267   | No documented layout |
| 3258   | No documented layout |
| 3251   | No documented layout |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
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
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
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

The blocks need no companion: the walk gives each block's size. The handler
reads the same optional data as the `itemenchant.dbss` one, minus the
crystal groups, which this file does not store.

| File                  | Required | Role                                                                                 |
| --------------------- | -------- | ------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Item name and description for the item ID (`str_type=0`, `str_id4` 0 and 1)         |
| `skill.dbss`          | Optional | The buffs of `skill_key_1` and `skill_key_2`, through the `SKILL_BUFFS` lookup index  |
| `lightstoneset.bss`   | Optional | The Lightstone sets an item counts toward, through the `LIGHTSTONE_SETS` lookup index |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes |
| ------- | ------------ | ------ | ----- |
| `+0x00` | u32          | count  | Block count, the row count of `itemenchantoffset.dbss` |
| `+0x04` | Block[count] | blocks | Contiguous, in the order of `itemenchantoffset.dbss`; the last block ends at the end of the file |

### Block (variable: 309 bytes + lists and strings)

Every field has the offset, type and name it has in the Block of
[`itemenchant.dbss`](itemenchant_dbss.md), and the meanings, value counts
and evidence are there. As there, the header fields after `unknown_61` move
by its count `unknown_5d`, and the hex in their `unknown_<hex>` names is the
offset in a block whose count is `0`.

| Offset               | Type                           | Field                       | Notes |
| -------------------- | ------------------------------ | --------------------------- | ----- |
| `+0x00`              | u32                            | key                         | Packed item ID and enchant level, `enchant_level << 24 \| item_id` |
| `+0x04`              | u8                             | item_type                   |       |
| `+0x05`              | u8                             | category                    |       |
| `+0x06`              | u8                             | grade                       |       |
| `+0x07`              | u8                             | equip_type                  |       |
| `+0x08`              | bytes[6]                       | unknown_08                  |       |
| `+0x0E`              | u8                             | equip_slot                  |       |
| `+0x0F`              | u8                             | unknown_0f                  |       |
| `+0x10`              | u8[46]                         | extended_slots              |       |
| `+0x3E`              | u8                             | item_material               |       |
| `+0x3F`              | i32                            | weight                      |       |
| `+0x43`              | u8                             | stackable                   |       |
| `+0x44`              | u8                             | do_apply_directly           |       |
| `+0x45`              | u32                            | expiration_minutes          |       |
| `+0x49`              | u8                             | vested_type                 |       |
| `+0x4A`              | u8                             | family_bound                |       |
| `+0x4B`              | u8                             | for_trade                   |       |
| `+0x4C`              | u8                             | trade_type                  |       |
| `+0x4D`              | u64                            | class_mask                  |       |
| `+0x55`              | u32                            | servant_kinds               |       |
| `+0x59`              | bytes[4]                       | unknown_59                  |       |
| `+0x5D`              | u32                            | unknown_5d                  | Count of `unknown_61`; `0` except on mount and ship gear |
| `+0x61`              | bytes[unknown_5d]              | unknown_61                  |       |
| `unknown_61+0x00`    | i32                            | required_level              |       |
| `unknown_61+0x04`    | i32                            | max_level                   |       |
| `unknown_61+0x08`    | u8                             | life_exp_type               |       |
| `unknown_61+0x09`    | i32                            | life_min_level              |       |
| `unknown_61+0x0D`    | i64                            | buy_price                   |       |
| `unknown_61+0x15`    | i64                            | sell_price                  |       |
| `unknown_61+0x1D`    | i64                            | repair_price                |       |
| `unknown_61+0x25`    | u16                            | contents_event_type         |       |
| `unknown_61+0x27`    | i64                            | contents_event_param1       |       |
| `unknown_61+0x2F`    | i64                            | contents_event_param2       |       |
| `unknown_61+0x37`    | bytes[8]                       | unknown_98                  |       |
| `unknown_61+0x3F`    | u8                             | commerce_type               |       |
| `unknown_61+0x40`    | u16                            | item_action_number          |       |
| `unknown_61+0x42`    | u8                             | hide_from_note              |       |
| `unknown_61+0x43`    | u8                             | is_cash                     |       |
| `unknown_61+0x44`    | u8                             | unknown_a5                  |       |
| `unknown_61+0x45`    | u8                             | is_term                     |       |
| `unknown_61+0x46`    | u8                             | guild_stock_level           |       |
| `unknown_61+0x47`    | u8                             | dyeable                     |       |
| `unknown_61+0x48`    | u8                             | is_target_alive             |       |
| `unknown_61+0x49`    | u16                            | character_id                |       |
| `unknown_61+0x4B`    | u8                             | repair_endurance_count      |       |
| `unknown_61+0x4C`    | u8                             | unknown_ad                  |       |
| `unknown_61+0x4D`    | bytes[22]                      | unknown_ae                  |       |
| `unknown_61+0x63`    | u8                             | personal_trade              |       |
| `unknown_61+0x64`    | u16                            | max_durability              |       |
| `unknown_61+0x66`    | u8                             | is_client_use               |       |
| `unknown_61+0x67`    | u8                             | market_category             |       |
| `unknown_61+0x68`    | u8                             | market_sub_category         |       |
| `unknown_61+0x69`    | u8                             | node_free_trade             |       |
| `unknown_61+0x6A`    | u8                             | unknown_cb                  |       |
| `unknown_61+0x6B`    | u32                            | skill_key_1                 |       |
| `unknown_61+0x6F`    | u32                            | skill_key_2                 |       |
| `unknown_61+0x73`    | u32                            | class_entry_count           |       |
| `unknown_61+0x77`    | Class Entry[class_entry_count] | class_entries               |       |
| `class_entries+0x00` | u32                            | unknown_list2_count         |       |
| `class_entries+0x04` | u8[unknown_list2_count][5]     | unknown_list2               |       |
| `unknown_list2+0x00` | bytes[4]                       | unknown_after_unknown_list2 |       |
| `unknown_list2+0x04` | u32                            | unknown_list3_count         |       |
| `unknown_list2+0x08` | u32[unknown_list3_count]       | unknown_list3               |       |
| `unknown_list3+0x00` | u32                            | enchant_key                 |       |
| `unknown_list3+0x04` | str16                          | name_kr                     | Korean item name |
| `name_kr+0x00`       | str8                           | icon                        | Icon path, relative to `ui_texture/icon/` |
| `icon+0x00`          | Icon Tail                      | icon_tail                   | See Icon Tail |
| `icon+0x12`          | str16[3]                       | messages_kr                 |       |
| `messages_kr+0x00`   | Message Tail                   | message_tail                | See Message Tail; the block ends with it |

### Class Entry (5 bytes)

| Offset  | Type | Field         | Notes |
| ------- | ---- | ------------- | ----- |
| `+0x00` | u8   | class_type    |       |
| `+0x01` | u32  | item_mesh_key | The key of [`itemeffectchange.dbss`](itemeffectchange_dbss.md) |

### Icon Tail (18 bytes)

| Offset  | Type      | Field            | Notes |
| ------- | --------- | ---------------- | ----- |
| `+0x00` | u8        | marketable       |       |
| `+0x01` | u8        | karma_type       |       |
| `+0x02` | bytes[11] | unknown_02       |       |
| `+0x0D` | u8        | family_inventory |       |
| `+0x0E` | u8        | unknown_0e       |       |
| `+0x0F` | u8        | season_item_type |       |
| `+0x10` | bytes[2]  | unknown_10       |       |

### Message Tail (43 bytes)

The first `0x2B` bytes of the `itemenchant.dbss` Message Tail, with the same
offsets and names; its `unknown_2b` and `item_access_level` are the first
fields of an `itemenchantbackend.dbss` block.

| Offset  | Type     | Field                  | Notes |
| ------- | -------- | ---------------------- | ----- |
| `+0x00` | i64      | unknown_limit          |       |
| `+0x08` | u8       | unknown_08             |       |
| `+0x09` | u32      | enhancement_group      |       |
| `+0x0D` | u32      | enhancement_type       |       |
| `+0x11` | u8       | is_removable           |       |
| `+0x12` | bytes[4] | unknown_12             |       |
| `+0x16` | u8       | cron_enchant_control   |       |
| `+0x17` | u8       | unknown_17             |       |
| `+0x18` | u8       | is_notice_world_market |       |
| `+0x19` | bytes[2] | unknown_19             |       |
| `+0x1B` | u8       | barter_type            |       |
| `+0x1C` | bytes[6] | unknown_1c             |       |
| `+0x22` | u8       | is_dropable            |       |
| `+0x23` | u8       | is_exchange_item       |       |
| `+0x24` | u8       | is_navigation          |       |
| `+0x25` | bytes[4] | unknown_25             |       |
| `+0x29` | u8       | life_equip_type        |       |
| `+0x2A` | u8       | life_restrict_type     |       |

## Notes

- I checked the split on client 3483 by walking all three files: for all
  169,345 keys the first bytes of the `itemenchant.dbss` block equal the
  block of this file, the rest equals the `itemenchantbackend.dbss` block,
  and the blocks of this file tile it from byte `4` to the end. The parsed
  fields of the 70,826 base items match the `itemenchant.dbss` parse.
- The fields this file leaves out are the ones the `itemenchant.dbss` doc
  places after Message Tail `+0x2A`: `item_access_level`, `second_string`,
  `key_dup` and `crystal_group`, and the undecoded remainder between them.
- The file first appears on client 1980, two test clients after
  `itemenchantbackend.dbss` (1964). Clients 1980 to 3251 ship it in an older
  block layout that is not documented here, as for `itemenchant.dbss`
  before client 3473.

## Open Questions

### Which File the Client Reads

The client data holds the whole blocks in `itemenchant.dbss` and the same
bytes again, split, in this file and `itemenchantbackend.dbss`. Whether the
client loads the split pair, the whole file or both, and what the `test` in
this file's name stands for, is open.
