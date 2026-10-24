# `guildhonorsystem.bss` Format

## Purpose

The Guild Fame system (`_ContentsGroup_GuildHonorSystem`): how many points each guild activity earns or costs, the benefits a guild unlocks at a Guild Fame threshold, and the Bonus Guild Daily Pay steps. The Guild Fame Benefits window (`panel_window_guildhonorbenefitguide_all`) lists all three. The file has no PABR magic and no string table: a head of eight u64 values, then three u32-counted lists. On client 3482 they hold 26 change reasons (12 gains, 14 costs), 22 benefits and 10 daily pay steps.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                                          | Row bytes               |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------------------------------------------ | ----------------------- |
| 1      | 3402 and later | 3483    | `guildhonorsystem.bss` | 3,472 | 26 Change Reason, 22 Benefit, 10 Daily Incentive | 46 to 78, 57 on average |

| Layout | File                   | Known           | Unknown     |
| ------ | ---------------------- | --------------- | ----------- |
| 1      | `guildhonorsystem.bss` | 3,408 B (98.2%) | 64 B (1.8%) |

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
| 3396   | No file              |
| 3387   | No documented layout |
| 3381   | No documented layout |
| 3373   | No documented layout |
| 3364   | No documented layout |
| 3356   | No documented layout |
| 3349   | No file              |
| 3342   | No file              |
| 3335   | No file              |
| 3326   | No file              |
| 3321   | No file              |
| 3314   | No file              |
| 3303   | No file              |
| 3302   | No file              |
| 3293   | No file              |
| 3283   | No file              |
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

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `boss_spawnlevel.bss` | Optional | The boss character of a [`boss_spawn.bss`](boss_spawn_bss.md) key, for the boss summon reasons |
| `languagedata_en.loc` | Optional | Change reason text (type 141), benefit text (type 140), skill names (type 10), the daily pay text (type 37), boss names (type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                                   | Field                 | Notes                                          |
| ------------------- | -------------------------------------- | --------------------- | ---------------------------------------------- |
| `+0x00`             | u64                                    | unknown_00            | A different address on every client; see Notes |
| `+0x08`             | i64                                    | unknown_08            | `-2,000,000`; see Open Questions               |
| `+0x10`             | i64                                    | unknown_10            | `1,000,000`                                    |
| `+0x18`             | u64                                    | unknown_18            | `21,600`                                       |
| `+0x20`             | u64                                    | unknown_20            | `604,800`                                      |
| `+0x28`             | u64                                    | unknown_28            | `172,800`                                      |
| `+0x30`             | u64                                    | unknown_30            | `604,800`                                      |
| `+0x38`             | u64                                    | unknown_38            | `10`                                           |
| `+0x40`             | u32                                    | change_reason_count   | Number of change reasons                       |
| `+0x44`             | Change Reason[change_reason_count]     | change_reasons        | See Change Reason                              |
| `change_reasons+0x00` | u32                                  | benefit_count         | Number of benefits                             |
| `change_reasons+0x04` | Benefit[benefit_count]               | benefits              | See Benefit                                    |
| `benefits+0x00`     | u32                                    | daily_incentive_count | Number of daily pay steps                      |
| `benefits+0x04`     | Daily Incentive[daily_incentive_count] | daily_incentives      | See Daily Incentive; they end at the last byte |

The head values are the ones of clients 3402 to 3482.

### Change Reason (variable: 36 bytes + description text)

One way to gain or spend Guild Fame. The How to Obtain and Uses tabs of the Guild Fame Benefits window list these rows by `ToClient_GetGuildHonorGainValueByIndex` / `ToClient_GetGuildHonorConsumeValueByIndex` and their `...DescByIndex` text.

| Offset                | Type  | Field          | Notes                                                                   |
| --------------------- | ----- | -------------- | ----------------------------------------------------------------------- |
| `+0x00`               | u32   | key            | `0` up, in file order; LOC type 141 `str_id1` of the English text       |
| `+0x04`               | str16 | description_kr | Korean text, `길드원 접속` (`Guild Member Login`) for key `0`            |
| `description_kr+0x00` | i64   | point          | Guild Fame gained (positive) or spent (negative): `50` for a member login, `-400,000` for a war declaration |
| `description_kr+0x08` | u64   | reason_param   | The second argument of `ToClient_GetGuildHonorChangePointByReason(reason_type, reason_param)`: a `boss_spawn.bss` key or a skill key; `0` for the other reasons |
| `description_kr+0x10` | u32   | key_dup        | Same as `key` on every row (client 3482)                                |
| `description_kr+0x14` | u32   | reason_type    | The change reason, see Change Reason Types                              |

### Benefit (variable: 41 bytes + description text)

A benefit a guild gets while its Guild Fame is at or above `point`, read by `ToClient_GetGuildHonorBenefitConditionByIndex`, `ToClient_GetGuildHonorBenefitTypeByIndex` and `ToClient_GetGuildHonorBenefitDescriptionByIndex`.

| Offset                | Type  | Field          | Notes                                                                   |
| --------------------- | ----- | -------------- | ----------------------------------------------------------------------- |
| `+0x00`               | u32   | key            | `0` up, in file order; LOC type 140 `str_id1` of the English text       |
| `+0x04`               | str16 | description_kr | Korean text, `일일 임무 충전 <b>+10</b>` (`Daily Missions <b>+10</b>`) for key `0` |
| `description_kr+0x00` | i64   | point          | The Guild Fame the benefit needs, `50,000` to `900,000` (client 3482)   |
| `description_kr+0x08` | u64   | param_1        | By `benefit_type`, see Benefit Types                                    |
| `description_kr+0x10` | u64   | param_2        | By `benefit_type`, see Benefit Types                                    |
| `description_kr+0x18` | u32   | key_dup        | Same as `key` on every row (client 3482)                                |
| `description_kr+0x1C` | u8    | benefit_type   | See Benefit Types                                                       |

### Daily Incentive (12 bytes)

A Bonus Guild Daily Pay step, read by `ToClient_GetGuildHonorDailyIncentiveBenefitConditionByIndex` and `ToClient_GetGuildHonorDailyIncentiveBenefitPercentByIndex`.

| Offset  | Type | Field         | Notes                                                                    |
| ------- | ---- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | i64  | point         | The Guild Fame the step needs, `50,000` to `900,000` (client 3482)       |
| `+0x08` | u32  | bonus_percent | The bonus on the `CppDefine.e1Percent` scale (`10000` is 1%): `9,000,000` shows as `+900%` |

## Change Reason Types

`reason_type` on client 3482. The rows that earn Guild Fame have `reason_type` equal to their `key`, `0` to `11`; the rows that spend it have `1000` up. LOC type 141 also holds English text with `str_id1 = reason_type` (`str_id2` `8` for `1005`, `1` for `1007`, else `0`), which may be the text of a Guild Fame history line. The Lua names come from the calls of `ToClient_GetGuildHonorChangePointByReason` in `panel_guilddeclarewar_all`, `panel_guild_bosssummon_all_1` and `panel_window_guildmainserverset_1`, matched by their `reason_param` and the LOC text.

| reason_type | Rows (client 3482)                                      | `reason_param`      | Lua name                                                          |
| ----------- | ------------------------------------------------------- | ------------------- | ----------------------------------------------------------------- |
| 0 to 11     | Member login, guild mission, guild boss, Guild League, Blue Battlefield, Node War and Conquest War tiers, War of the Roses | `0` | none found                                                        |
| 1000 to 1003 | Guild maintenance cost by guild size, `-2,500` to `-10,000` | `0`             | none found                                                        |
| 1004        | War Declaration                                         | `0`                 | `__eGuildHonorPointChangeReasonType_Consume_DeclareWar`           |
| 1005        | Gumiho & Duoksini Summon                                | `8`, a `boss_spawn.bss` key | `__eGuildHonorPointChangeReasonType_Consume_CompleteGuildBossSpawnCondition` |
| 1006        | Additional Ferrid, Moghulis, Giant Mudster, Org and Khan Summon | `1` to `5`, `boss_spawn.bss` keys | `__eGuildHonorPointChangeReasonType_Consume_AddGuildBossSpawnCountMax` |
| 1007        | Use Guild Skill: Glorious Command to Gather, Glorious Golden Bell | skill keys of skills 62874 and 62875, level 1 | none found; `ToClient_GetUseGuildHonorPointConsumeSkillNeedPoint(skillNo)` reads the cost |
| 1009        | Reset Guild Base Server Cooldown                        | `0`                 | `__eGuildHonorPointChangeReasonType_Consume_ResetGuildMainServerCooltime` |

No row has `reason_type` `1008`, and LOC type 141 has no text for it.

## Benefit Types

`benefit_type` on client 3482. A skill key is `skill_no << 16 | level`, as in [`guildskill.bss`](guildskill_bss.md); every key here has level `1`.

| benefit_type | Lua name                                       | Rows (client 3482)                        | `param_1`                 | `param_2`                     |
| ------------ | ---------------------------------------------- | ----------------------------------------- | ------------------------- | ----------------------------- |
| 0            | none found                                     | 3: `[Mission] Glorious Subjugation`, `Life` and `Trading` `Unlocked` | First [`guildquest.dbss`](guildquest_dbss.md) `quest_no` of the unlocked missions | Last `quest_no`: `5001` to `5016`, `5501` to `5540`, `6001` to `6008` |
| 1            | `__eGuildHonorBenefitType_MissionChargeIncrease` | 10: `Daily Missions +1` to `+10`        | `1` on every row          | `0`                           |
| 2            | `__eGuildHonorBenefitType_UnlockGuildSkill`    | 6: `[Skill] ... Unlocked`                 | Skill key of the unlocked skill | `0`                     |
| 3            | `__eGuildHonorBenefitType_UpgradeGuildSkill`   | 3: `[Skill] ... Enhanced`                 | Skill key of the base skill | Skill key of the enhanced skill: `62858` Blessing of Fortuna becomes `62864` Generous Blessing of Fortuna |

The Lua shows only the highest `MissionChargeIncrease` benefit the guild has reached as applied, and lists the type 2 and 3 benefits in a list of their own. The guild mission list (`panel_guildquestlist_all_1`) hides a mission whose `isGuildHonorBenefitQuest()` is true until `isUnlockedGuildHonorBenefitQuest(currentGuildHonorPoint)` is. On client 3482, 56 of the 64 `quest_no` in the three type 0 ranges have a `guildquest.dbss` row (`5501` to `5508` have none), and those 56 are every mission with `Glorious` in its title.

## Field Names

The names come from the client Lua (client 3482) and the data. `point` is the `_point` the Lua builds each of the three lists with. `reason_type` and `reason_param` are the two arguments of `ToClient_GetGuildHonorChangePointByReason`, which the boss summon window calls with a boss key and the war declaration window with `0`, the values these rows store. `benefit_type` takes the values the Lua compares with the `__eGuildHonorBenefitType_*` names, and each type's rows have the LOC text of that type. `bonus_percent` is the value the Lua divides by `CppDefine.e1Percent` for the `{percent}` of `LUA_GUILDHONOR_DAILYINCENTIVE_BENEFIT_GUIDE` (`Bonus Guild Daily Pay +{percent}%`). `param_1` and `param_2` hold a mission range or skill keys by type, so they keep a neutral name.

The file is not in the archive of client 1784, and neither a private server's `DataSheets.bexcel` on client 1784 nor the 2016 PDB has a sheet, column or type with `Honor` in its name.

## Notes

- Decompressed size on client 3482: `3,472` bytes, `0x40` head, 26 change reasons, 22 benefits and 10 daily pay steps.
- `unknown_00` is not a game value: `0x00007FF659C7ADE8` on client 3482, `0x00007FF79B062F88` on client 3474, an address in the range a 64-bit Windows program image loads at. The files of clients 3412 to 3482 differ in these 8 bytes only. [`questrandomgroup.bss`](questrandomgroup_bss.md) stores the same kind of address at row `+0x00`.
- Client 3402 has the same layout with 21 change reasons: one `Additional Guild Boss Summon` row (key `17`, `reason_type` `1006`, `reason_param` `0`) where client 3412 has the Gumiho & Duoksini row and the five boss rows, so the three rows after it have keys `18` to `20` in place of `23` to `25`.
- Clients 3356 to 3387 store the file in other shapes, which no layout here reads. Clients 3356 to 3381 write the same kind of address before every change reason, and the gaps between its fields hold bytes that change from row to row (`00 4C 00 B7`, `00 00 AC B9` on client 3356). Client 3387 has the eight-value head and a first list of 12 rows of 16 bytes (key, point, reason type) without text.
- The head of clients 3356 to 3381 holds six u64 values: the address, `-1,000,000` (`-3,000,000` on client 3381), `300,000` (`1,000,000` on client 3381), `21,600`, `604,800` and `172,800` (the last two swapped on client 3356). Client 3387 has the eight values of client 3402 with `-3,000,000` in place of `-2,000,000`.
- No client the doc check read before 3356 has the file in its `.meta`, and neither has client 3396, between 3387 and 3402.

## Open Questions

### What the Head Values Hold

The seven values after `unknown_00` have no getter in the Lua. `unknown_18` (`21,600` seconds, 6 hours), `unknown_20` (`604,800`, 7 days) and `unknown_28` (`172,800`, 48 hours) match the War Declaration tooltip in that order: a declared war lasts 6 hours, declaring war in response extends it to 7 days, and a guild cannot declare war on the same guild for 48 hours after a war ends. `unknown_08` (`-2,000,000`) and `unknown_10` (`1,000,000`) may be the lowest and highest Guild Fame a guild can have; the benefit steps end at `900,000`, and the tooltip waives the declaration cost against a guild with negative Guild Fame. `unknown_30` (`604,800`) may be the 7 days of the Guild Fame log, and `unknown_38` (`10`) matches nothing found.

### `param_1` of the Daily Mission Benefits

The ten `MissionChargeIncrease` benefits store `param_1` `1`, while their text adds `+1` to `+10` daily missions by row. The value may be a mission type, or the charges per step, with the `+N` taken from the number of steps reached.
