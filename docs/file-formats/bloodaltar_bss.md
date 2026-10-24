# `bloodaltar.bss` Format

## Purpose

The stages of the Blood Altar, a party instance
(`__eInstanceContentsType_BloodAltar`). A PABR file: four option values,
then one row per stage with its Korean stage texts and boss banner
texture (string-table indices), the minimum and recommended AP and DP,
and two reward lists,
the first clear rewards and the weekly rewards. On client 3482 it holds
24 stages, `제1의 환상` ("the 1st Illusion") to `제 24의 환상`; the
first clear reward of stage N is Bloodstained Welcome - The Nth Illusion
(`980010 + N`) and the weekly rewards are Bloodstained Spoils - The Nth
Illusion (`980040 + N`) and Combat Secret Book (M) (`890118`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------------------------- | --------- |
| 2      | 3473 and later | 3483    | `bloodaltar.bss` | 3,363 | 72 Reward Entry, 24 Stage | 16        |
| 1      | 3283 to 3464   | 3464    | `bloodaltar.bss` | 2,211 | 24 Stage                  | 40        |

| Layout | File             | Known           | Unknown      |
| ------ | ---------------- | --------------- | ------------ |
| 2      | `bloodaltar.bss` | 3,157 B (93.9%) | 206 B (6.1%) |
| 1      | `bloodaltar.bss` | 2,005 B (90.7%) | 206 B (9.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
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
| 3275   | No file  |
| 3267   | No file  |
| 3258   | No file  |
| 3251   | No file  |
| 3242   | No file  |
| 3235   | No file  |
| 3229   | No file  |
| 3212   | No file  |
| 3203   | No file  |
| 3193   | No file  |
| 3186   | No file  |
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
| 3144   | No file  |
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
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

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type               | Field        | Notes                                           |
| ------------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`             | Options            | options      | See Options                                     |
| `+0x12`             | u32                | stage_count  | Number of stages                                |
| `+0x16`             | Stage[stage_count] | stages       | See Stage                                       |
| `stages+0x00`       | String Table       | string_table | See String Table                                |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `stages` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                      |

### Options (14 bytes)

| Offset  | Type | Field      | Notes                                            |
| ------- | ---- | ---------- | ------------------------------------------------ |
| `+0x00` | u32  | unknown_00 | `24` on client 3482, equal to `stage_count`      |
| `+0x04` | u32  | unknown_04 | `3` on client 3482                               |
| `+0x08` | u32  | unknown_08 | `56` on client 3482                              |
| `+0x0C` | u16  | unknown_0c | `10` on client 3482                              |

### Stage (variable: 40 bytes + reward entries)

| Offset               | Type                              | Field               | Notes                                                                         |
| -------------------- | --------------------------------- | ------------------- | ----------------------------------------------------------------------------- |
| `+0x00`              | u32                               | stage_key           | `1` to `stage_count` in file order; the stage key the Lua getters take        |
| `+0x04`              | u32                               | unknown_str_ref_04  | String-table index of a Korean stage text with a space after `제` (`제 1의 환상`) |
| `+0x08`              | u32                               | unknown_str_ref_08  | String-table index of a Korean stage text, `제1의 환상` on stages 1 to 21, the `unknown_str_ref_04` text on stages 22 to 24 |
| `+0x0C`              | u32                               | boss_texture_ref    | String-table index of the boss banner texture name; an empty string on the stages that keep the boss of the stage before |
| `+0x10`              | f32                               | match_min_offence   | Minimum AP to match: `300` to `415` on client 3482, `+5` per stage            |
| `+0x14`              | f32                               | match_min_defence   | Minimum DP to match: `390` to `475` on client 3482                            |
| `+0x18`              | f32                               | recommended_offence | Recommended AP: `1070` to `2290` on client 3482                               |
| `+0x1C`              | f32                               | recommended_defence | Recommended DP: `420` to `820` on client 3482                                 |
| `+0x20`              | u32                               | first_reward_count  | Number of `first_rewards`; `1` on every stage of client 3482                  |
| `+0x24`              | Reward Entry[first_reward_count]  | first_rewards       | The first clear rewards; see Reward Entry                                     |
| `first_rewards+0x00` | u32                               | weekly_reward_count | Number of `weekly_rewards`; `2` on every stage of client 3482                 |
| `first_rewards+0x04` | Reward Entry[weekly_reward_count] | weekly_rewards      | The weekly rewards; see Reward Entry                                          |

### Reward Entry (16 bytes)

| Offset  | Type     | Field            | Notes                                                                                   |
| ------- | -------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32      | item_enchant_key | `enchant_level << 24 \| item_id`; `ToClient_getBloodAltarRewardItemEnchantKey`          |
| `+0x04` | bytes[4] | padding_04       | Alignment of the u64 `item_count` to 8 bytes; `f6 7f 00 00` in every entry of client 3482 |
| `+0x08` | u64      | item_count       | `ToClient_getBloodAltarRewardItemCount`; `1` in every entry of client 3482              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                              |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; 54 on client 3482                               |
| `+0x04` | pstr[string_count] | strings      | UTF-16 stage texts and boss texture names, in stage order          |

## Layout 1

### Stage (40 bytes)

| Offset  | Type | Field                  | Notes                                                                  |
| ------- | ---- | ---------------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | stage_key              | `1` to `stage_count` in file order                                     |
| `+0x04` | u32  | unknown_str_ref_04     | String-table index of a Korean stage text                              |
| `+0x08` | u32  | unknown_str_ref_08     | String-table index of a Korean stage text                              |
| `+0x0C` | u32  | boss_texture_ref       | String-table index of the boss banner texture name                     |
| `+0x10` | f32  | match_min_offence      | Same as Layout 2                                                       |
| `+0x14` | f32  | match_min_defence      | Same as Layout 2                                                       |
| `+0x18` | f32  | recommended_offence    | Same as Layout 2                                                       |
| `+0x1C` | f32  | recommended_defence    | Same as Layout 2                                                       |
| `+0x20` | u32  | weekly_reward_item_key | One item key, Bloodstained Spoils - The Nth Illusion (`980040 + N`) on stage N |
| `+0x24` | u32  | first_reward_item_key  | One item key, Bloodstained Welcome - The Nth Illusion (`980010 + N`) on stage N |

## Boss Textures

Client 3482: the stages with a non-empty `boss_texture_ref` string; the
other stages, 1 and 2 among them, point at an empty string. Each texture
is a `Combine_Etc_BloodAltar_PopUpImg_Boss_<n>` UI texture ID.

| Stage | Boss texture                             |
| ----- | ---------------------------------------- |
| 3     | `Combine_Etc_BloodAltar_PopUpImg_Boss_2` |
| 6     | `Combine_Etc_BloodAltar_PopUpImg_Boss_3` |
| 9     | `Combine_Etc_BloodAltar_PopUpImg_Boss_4` |
| 12    | `Combine_Etc_BloodAltar_PopUpImg_Boss_8` |
| 15    | `Combine_Etc_BloodAltar_PopUpImg_Boss_9` |
| 18    | `Combine_Etc_BloodAltar_PopUpImg_Boss_6` |
| 21    | `Combine_Etc_BloodAltar_PopUpImg_Boss_1` |
| 24    | `Combine_Etc_BloodAltar_PopUpImg_Boss_10` |

## Field Names

Blood Altar is newer than client 1784: the file is not in its archives
and no sheet of a private server's `DataSheets.bexcel` on that client has
`Blood` or `Altar` in its name. The names come from the getters of the
stage menu Lua (`panel_window_bloodaltarmenu_all_1.luac`, client 3482):

- `stage_key`: the menu lists `ToClient_getBloodAltarStageSize()` stages
  and passes `index + 1` as the stage key to every getter, so the keys run
  from `1` in file order.
- `boss_texture_ref`: `ToClient_getBloodAltarBossTextureID(stageKey)`
  goes to `setRenderTexture` of the boss banner; the string is a UI
  texture ID.
- `first_rewards` and `weekly_rewards`: `ToClient_getBloodAltarRewardSize(stageKey, isFirst)`
  with `true` and `false`, then `ToClient_getBloodAltarRewardItemEnchantKey`
  and `ToClient_getBloodAltarRewardItemCount` per entry. The first list
  holds Bloodstained Welcome items, the second Bloodstained Spoils items,
  the item names of the first clear and the weekly reward.
- `match_min_offence` and `match_min_defence`:
  `ToClient_getBloodAltarMatchMinStatOffence` and `...Defence`;
  `recommended_offence` and `recommended_defence`:
  `ToClient_getBloodAltarRecommandStatOffence` and `...Defence`. In game
  the stage 1 window shows a minimum AP of 300 and DP of 390 and a
  recommended AP of 1070 and DP of 420, the values at `+0x10` to `+0x1C`
  in that order.

The Lua also calls `ToClient_getBloodAltarStageName(stageKey)`; which
stage text it reads is open (see Open Questions).

## Notes

- Layout 1 (clients 3283 to 3454) stores one weekly reward item key and
  one first clear item key per stage in place of the two reward lists.
  Layout 2 (client 3474) turns them into lists and adds Combat Secret
  Book (M) to every stage's weekly rewards.
- `padding_04` is the alignment gap of an in-memory entry (u32 key, then a
  u64 count at `+0x08`). `0x00007FF6` is the high half of an x64 image
  address, so the bytes are left over from memory, not set by the data.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`: the
  stage key, the boss texture, the four AP and DP values and both reward
  lists.

## Open Questions

### Which Stage Text Is the Name

`ToClient_getBloodAltarStageName(stageKey)` fills the stage list and the
title of the selected stage, and `ToClient_getBloodAltarStageTitle()` the
HUD title while a stage runs. Both stage texts read as the stage name,
one with a space after `제` and one without, so either getter can read
either string.

### What the Options Are

`unknown_00` equals the stage count on client 3482. The HUD shows
`ToClient_getBloodAltarPlayableCount()` of
`ToClient_getMaxBloodaltarPlayableCount()` retries
(`LUA_BLOODALTAR_HUD_RETRY_LEFT`), but in game a run has 5 retries and no
option holds `5`, so the retry count is not in this file. A party in
the Blood Altar has at most 3 players, the value of `unknown_04`; no Lua
getter ties the two together yet. No Lua call names `unknown_08` (`56`)
or `unknown_0c` (`10`).
