# `characterstatic.dbss` Format

## Purpose

Variable-length character/NPC static data table: one record per character template (player classes, NPCs, monsters, mounts, objects). Each record is keyed by a character ID and stores display flags, two inline scripts, the character's kind, grade, group and tribe, the karma and naval fame change when it dies, its box and body size, the static stat block it shares with [experience.bss](experience_bss.md), its level, vehicle settings, spawn hours, the AI script, the action-chart path, its Korean name, label and title, the voice bank, the items it can hold, its attribute types and contents groups, the item that places or summons it and, for player characters, the gameplay class type. Many NPC records have a `getknowledge(<id>);` script, which links the character to the knowledge entry the player gains by talking to it.

Most field names follow the `Character_Table` sheet of a private server's `DataSheets.bexcel` on client 1784; see [Field Names](#field-names). `npc_kind` and `class_type` follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`npcKind`, `classType`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes      | Records                                                      | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ---------- | ------------------------------------------------------------ | --------- |
| 3      | 3464 and later | 3483    | `characterstatic.dbss`       | 13,491,651 | 24,445 Character Fields, 24,445 Payload, 24,445 Stream Entry | 287       |
| 3      | 3464 and later | 3483    | `characterstaticoffset.dbss` | 244,470    | 24,445 Index Row                                             | 10        |
| 2      | 3335 to 3458   | 3458    | `characterstatic.dbss`       | 13,339,244 | 24,551 Character Fields, 24,551 Payload, 24,551 Stream Entry | 279       |
| 2      | 3335 to 3458   | 3458    | `characterstaticoffset.dbss` | 245,530    | 24,551 Index Row                                             | 10        |
| 1      | 1685 to 2011   | 2011    | `characterstatic.dbss`       | 10,038,543 | 17,178 Character Fields, 17,178 Payload, 17,178 Stream Entry | 298       |
| 1      | 1685 to 2011   | 2011    | `characterstaticoffset.dbss` | 171,800    | 17,178 Index Row                                             | 10        |

| Layout | File                         | Known               | Unknown             |
| ------ | ---------------------------- | ------------------- | ------------------- |
| 3      | `characterstatic.dbss`       | 9,653,786 B (71.6%) | 3,837,865 B (28.4%) |
| 3      | `characterstaticoffset.dbss` | 244,470 B (100.0%)  | 0 B (0.0%)          |
| 2      | `characterstatic.dbss`       | 9,705,696 B (72.8%) | 3,633,548 B (27.2%) |
| 2      | `characterstaticoffset.dbss` | 245,530 B (100.0%)  | 0 B (0.0%)          |
| 1      | `characterstatic.dbss`       | 6,740,367 B (67.1%) | 3,298,176 B (32.9%) |
| 1      | `characterstaticoffset.dbss` | 171,800 B (100.0%)  | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 3             |
| 3482   | Layout 3             |
| 3474   | Layout 3             |
| 3473   | Layout 3             |
| 3464   | Layout 3             |
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
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | No documented layout |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | No documented layout |
| 1674   | No documented layout |
| 1668   | No documented layout |
| 1659   | No documented layout |
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
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

| File                         | Required | Role                                                   |
| ---------------------------- | -------- | ------------------------------------------------------ |
| `characterstaticoffset.dbss` | Required | Maps `character_id` to byte offset and payload size    |
| `languagedata_en.loc`        | Optional | Resolves display names for `character_id`, `class_type` and `source_item_id` |

Related but not required:

| File                                                   | Role |
| ------------------------------------------------------ | ---- |
| `playercharacterstatic.bss`                            | `PABR` list of player-like character IDs; see [below](#playercharacterstaticbss) |
| `hardcorerandomspawncharacterstaticstatusmanager.bss`  | Small `PABR` data file that references character IDs, including `62223` ("Wandering Merchant"); layout not yet decoded |
| `fuelinsertcharacterstaticstatus.bss`                  | Small related BSS entry; layout not yet decoded |

All multi-byte integer values observed in the DBSS payload are little-endian.

## Layout 3

### File Layout

| Offset  | Type                       | Field         | Notes                                      |
| ------- | -------------------------- | ------------- | ------------------------------------------ |
| `+0x00` | u32                        | record_count  | Number of records; `24553` on client 3474 |
| `+0x04` | Stream Entry[record_count] | record_stream | Repeated inline ID + variable-length payload chunks; see Stream Entry |

The stream is not fixed-width. Use `characterstaticoffset.dbss` to slice records.

### Stream Entry (variable: 2 bytes + payload)

Each logical record occupies `2 + payload_size` bytes in the main stream.

| Offset  | Type    | Field        | Notes |
| ------- | ------- | ------------ | ----- |
| `+0x00` | u16     | character_id | Matches the offset-table `character_id`; unique across observed records |
| `+0x02` | Payload | payload      | Starts at the offset listed in `characterstaticoffset.dbss`; byte count is `payload_size` |

Offset-table `data_offset` values point to the payload, not to the inline `character_id`. In observed data, the two bytes immediately before every `data_offset` equal the row's `character_id`.

### Payload (variable: 430 bytes, size from `characterstaticoffset.dbss`)

Offsets are relative to `data_offset`. Every string is a u64 count and then its text, so everything after the first script moves with the string lengths; the payload has no scan and no field at a guessed position. Counts on client 3474.

| Offset                        | Type                            | Field                             | Notes |
| ----------------------------- | ------------------------------- | --------------------------------- | ----- |
| `+0x00`                       | u8                              | is_hidden_name                    | `1` on 10,373 rows |
| `+0x01`                       | u8                              | is_hidden_hp                      | `1` on 4,054 rows |
| `+0x02`                       | u16                             | dialog_type                       | `1` on 338 rows, else `0` |
| `+0x04`                       | u8                              | is_tamable                        | `1` on 11 rows |
| `+0x05`                       | u8                              | is_render_shadow                  | `1` on 22,103 rows |
| `+0x06`                       | u8                              | use_default_audio                 | `1` on 12,462 rows |
| `+0x07`                       | u8                              | absolute_interaction              | `1` on 692 rows |
| `+0x08`                       | u8                              | unknown_08                        | `0x15` on every row; the parser checks it |
| `+0x09`                       | str16                           | action_script                     | UTF-16LE; empty on 18,733 rows, `getknowledge(<id>);` on 5,684 (client 3464). See [Script Values](#script-values) |
| `action_script+0x00`          | str16                           | condition_script                  | UTF-16LE; non-empty on 403 rows (client 3464) |
| `condition_script+0x00`       | Character Fields                | character_fields                  | See Character Fields |
| `condition_script+0x11F`      | str8                            | ai_script                         | Stem of the character's `.ai` file; see [AI Script](#ai-script) |
| `ai_script+0x00`              | str8                            | model_path                        | Action-chart path, lower case; see [Model Path](#model-path) |
| `model_path+0x00`             | str16                           | name_kr                           | See [Korean Strings](#korean-strings) |
| `name_kr+0x00`                | str16                           | label_kr                          | Internal Korean label |
| `label_kr+0x00`               | str16                           | title_kr                          | Korean title, empty on most rows |
| `title_kr+0x00`               | str8                            | voice_bank                        | Voice bank name (`NPC_VCE_47343`); non-empty on 10,145 rows |
| `voice_bank+0x00`             | u32                             | carriage_type                     | Non-zero on 30 rows (`1` to `5`) |
| `voice_bank+0x04`             | u8                              | unknown_voice_bank_04             | Always `0` |
| `voice_bank+0x05`             | i16                             | team_no                           | `-1` on 567 rows, `1` to `7` on 306, else `0` |
| `voice_bank+0x07`             | u8                              | unknown_voice_bank_07             | `6` on 21,559 rows, `2` on 2,460 (all `npc_kind` `3`), `0` on 492, `1` on 41, `3` on 1 |
| `voice_bank+0x08`             | i16                             | time_attack_type                  | `-1` on 24,536 rows, `1` to `3` on 17 |
| `voice_bank+0x0A`             | u32                             | time_attack_limit_minute          | Non-zero on the 17 rows with a `time_attack_type` (`30`, `7`, `1`) |
| `voice_bank+0x0E`             | u32                             | holdable_item_count               | Non-zero on 78 rows |
| `voice_bank+0x12`             | u32[holdable_item_count]        | holdable_item_keys                | Item keys, e.g. `9056`: `56003, 56007, 56008, 56147` |
| `holdable_item_keys+0x00`     | bytes[8]                        | unknown_holdable_item_keys_00     | Always `0` |
| `holdable_item_keys+0x08`     | u32                             | unknown_holdable_item_keys_08     | `1000000` on 15,819 rows, `0` on 8,734 |
| `holdable_item_keys+0x0C`     | u64                             | attribute_type_mask               | Bit `n` set for each `AttributeType` value `n`; see [Attribute Types](#attribute-types) |
| `holdable_item_keys+0x14`     | u16                             | steal_drop_id                     | Non-zero on 526 rows |
| `holdable_item_keys+0x16`     | u16                             | unknown_holdable_item_keys_16     | Always `0` |
| `holdable_item_keys+0x18`     | u32                             | contents_group_count              | `1` on 22,279 rows, up to `6` |
| `holdable_item_keys+0x1C`     | u32[contents_group_count]       | contents_group_hashes             | One hash per contents group key; see [Contents Groups](#contents-groups) |
| `contents_group_hashes+0x00`  | u8                              | class_type                        | Gameplay class enum; `101` on every non-player row, `0`-`46` on the 106 `playercharacterstatic.bss` members |
| `contents_group_hashes+0x01`  | u8                              | repair_resources                  | `3` on 65 rows (siege structures such as `12821` "Field HQ" and the node forts), else `0` |
| `contents_group_hashes+0x02`  | bytes[7]                        | unknown_contents_group_hashes_02  | Always `0` |
| `contents_group_hashes+0x09`  | u32                             | source_item_id                    | Item that places or summons the character; `0` on most rows. See [Source Item](#source-item) |
| `contents_group_hashes+0x0D`  | bytes[4]                        | unknown_contents_group_hashes_0d  | Always `0` |
| `contents_group_hashes+0x11`  | u8                              | unknown_contents_group_hashes_11  | `1` on 759 rows: 551 of `npc_kind` `3`, 195 of `9`, 13 of `7` (`35129` Horse, `62414` Wooden Fence); else `0` |
| `contents_group_hashes+0x12`  | u8                              | unknown_contents_group_hashes_12  | Always `0` |
| `contents_group_hashes+0x13`  | f32                             | reset_distance                    | `5000.0` on 23,971 rows, `15000.0` on 339, `3000.0` on 157, `1000.0` on 70, `10000.0` on 16 |
| `contents_group_hashes+0x17`  | u8                              | unknown_contents_group_hashes_17  | New in client 3464; `1` on 2,418 rows, 2,388 of them `npc_kind` `1`; else `0` |

The payload ends at `unknown_contents_group_hashes_17` on every row. Observed `payload_size` ranges from `465` to `1042` bytes.

### Character Fields (287 bytes)

The fixed block between `condition_script` and `ai_script`. Earlier versions of this doc wrote its offsets as `p+N` in decimal (`p+195` is `+0xC3`). From `max_hp` to `unknown_8d` the fields sit where the [experience.bss](experience_bss.md#stat-body-200-bytes) Stat Body has them, at Stat Body offset + `0x1D` (`max_hp` `+0x04` is `+0x21` here, `max_varied_speed` `+0x64` is `+0x81`). Counts on client 3474.

| Offset   | Type      | Field                           | Notes |
| -------- | --------- | ------------------------------- | ----- |
| `+0x00`  | u8        | is_developing_contents          | `1` on 335 rows |
| `+0x01`  | u16       | character_id                    | Equals the offset-table key on every row |
| `+0x03`  | i16       | character_group                 | Non-zero on 2,450 rows; see [Character Group](#character-group) |
| `+0x05`  | u8        | npc_kind                        | `gc::CharacterKind` of the 2016 client; see [`npc_kind` Values](#npc_kind-values) |
| `+0x06`  | u8        | grade                           | `CppEnums.CharacterGradeType`; see [Grade](#grade) |
| `+0x07`  | i32       | tendency_on_dead                | Karma change when the character dies; see [Karma](#karma) |
| `+0x0B`  | i32       | ocean_tendency                  | Naval fame value on sea monsters and ships; see [Ocean Tendency](#ocean-tendency) |
| `+0x0F`  | f32[3]    | box_size                        | `100.0, 100.0, 100.0` on most rows |
| `+0x1B`  | u32       | unknown_1b                      | `1` on character `530` only, else `0` |
| `+0x1F`  | u16       | collect_drop_id                 | Non-zero on 886 rows |
| `+0x21`  | f32       | max_hp                          | `1.0` where the sheet cell is `0`; `10000.0` on Ehren (`47791`) |
| `+0x25`  | u32       | max_mp                          | `1` where the sheet cell is `0` |
| `+0x29`  | u32       | sub_resource_point              | Non-zero on 80 rows |
| `+0x2D`  | bytes[16] | unknown_2d                      | Always `0` |
| `+0x3D`  | f32       | unknown_3d                      | `1.0` on 15,064 rows, else `0`; Stat Body `unknown_20` |
| `+0x41`  | bytes[8]  | unknown_41                      | Always `0` |
| `+0x49`  | u32       | regen_sub_resource_point        | Non-zero on 75 rows |
| `+0x4D`  | u32       | active_regen_sub_resource_point | Equal to `regen_sub_resource_point` on every row |
| `+0x51`  | u32       | unknown_51                      | Non-zero on 13 rows (`1`, `10`, `20`, `100`) |
| `+0x55`  | u32       | max_critical_rate               | Always `5` |
| `+0x59`  | u32       | max_drop_item_luck              | Always `5` |
| `+0x5D`  | u32       | max_fishing_luck                | Always `5` |
| `+0x61`  | u32       | max_collection_luck             | Always `5` |
| `+0x65`  | i64       | max_weight                      | `1` on 14,403 rows, `100000` on 1,178; Stat Body `+0x48` |
| `+0x6D`  | f32       | unknown_6d                      | Always `1.0`; Stat Body `unknown_50` |
| `+0x71`  | u32       | suspension                      | `10` on 12,197 rows, `200` on 2,867 |
| `+0x75`  | u32[3]    | unknown_75                      | `5, 5, 5` on 9,535 rows, `9, 5, 5` on 1, else `0, 0, 0`; all `0` on client 1784 |
| `+0x81`  | u32[3]    | max_varied_speed                | Always `10, 10, 10`; attack, movement and casting speed limits as in [servantexperience.dbss](servantexperience_dbss.md) |
| `+0x8D`  | f32       | unknown_8d                      | `1.0` on 15,064 rows, else `0`; Stat Body `unknown_70` |
| `+0x91`  | bytes[12] | unknown_91                      | Always `0` |
| `+0x9D`  | u8        | is_fixed                        | `1` on 4,534 rows |
| `+0x9E`  | u8        | is_catchedable                  | `1` on 813 rows |
| `+0x9F`  | u8        | unknown_9f                      | `1` on 24,344 rows, `0` on 209 |
| `+0xA0`  | u8        | unknown_a0                      | `1` on 21,916 rows; `0` only on `npc_kind` `3` (2,637 rows) |
| `+0xA1`  | u8        | unknown_a1                      | `1` on 59 rows, all `npc_kind` `3` |
| `+0xA2`  | u8        | unknown_a2                      | `1` on 77 rows |
| `+0xA3`  | u8        | is_guild_vehicle                | `1` on 85 rows |
| `+0xA4`  | u8        | is_using_vehicle_in_siege       | `1` on 92 rows |
| `+0xA5`  | u8        | unknown_a5                      | `1` on 8 rows, all `npc_kind` `3` |
| `+0xA6`  | u8        | vehicle_type                    | `CppEnums.VehicleType`; `65` when the character is not a vehicle. See [Vehicle Type](#vehicle-type) |
| `+0xA7`  | u8        | vehicle_sub_type                | Non-zero on 100 rows (`1` to `4`) |
| `+0xA8`  | u8        | unknown_a8                      | Non-zero on 153 rows (`1` to `12`) |
| `+0xA9`  | bytes[7]  | unknown_a9                      | Always `0` |
| `+0xB0`  | u8        | vehicle_seat_count              | `1` on 3,034 rows, up to `15` |
| `+0xB1`  | u8        | vehicle_driver_ridable          | `1` on 3,303 rows |
| `+0xB2`  | u8        | unknown_b2                      | `2` on 24,419 rows, `0` on 132, `1` on 2 |
| `+0xB3`  | u8        | tribe_type                      | See [Tribe Type](#tribe-type) |
| `+0xB4`  | u8        | inventory_max                   | Non-zero on 507 rows |
| `+0xB5`  | u8        | unknown_b5                      | `1` on 5,725 rows, 5,549 of them `npc_kind` `2` |
| `+0xB6`  | u8        | unknown_b6                      | `1` on 2,313 rows, 2,312 of them `npc_kind` `2` |
| `+0xB7`  | u8        | unknown_b7                      | `1` on 133 rows |
| `+0xB8`  | u8        | unknown_b8                      | `1` on 1 row |
| `+0xB9`  | u8        | unknown_b9                      | Always `0` |
| `+0xBA`  | u8        | is_pushable                     | `1` on 1,705 rows |
| `+0xBB`  | u8        | is_carrier                      | `1` on 368 rows |
| `+0xBC`  | u8        | unknown_bc                      | `1` on 334 rows; see [Field Names](#field-names) |
| `+0xBD`  | u8        | unknown_bd                      | `1` on 401 rows, all `npc_kind` `3` |
| `+0xBE`  | u8        | unknown_be                      | `1` on exactly the 61 rows of `npc_kind` `0` |
| `+0xBF`  | u8        | unknown_bf                      | `1` on 353 rows; see [Field Names](#field-names) |
| `+0xC0`  | u8        | unknown_c0                      | `1` on 24,493 rows; `0` only on 60 of `npc_kind` `3` |
| `+0xC1`  | u8        | unknown_c1                      | `1` on 37 rows, all `npc_kind` `3` |
| `+0xC2`  | u8        | unknown_c2                      | `10` on 24,112 rows; other values (`3`, `1`, `8`, `2`) only on `npc_kind` `3` |
| `+0xC3`  | u32       | level                           | `1` on 9,628 rows, `99` on 5,531, `60` on Garmoth (`29929`); see [Level](#level) |
| `+0xC7`  | bytes[8]  | unknown_c7                      | New in client 3464; non-zero on 3,630 rows: bytes `+0xC7` and `+0xC8` vary, `+0xC9` is `1` to `5` on 210 rows, the rest `0` |
| `+0xCF`  | u32       | is_live_collect                 | `-1` on 4 rows, `1` on 3, else `0`; see [Field Names](#field-names) |
| `+0xD3`  | i64       | vanish_time                     | `30000` on Garmoth |
| `+0xDB`  | f32       | body_size                       | |
| `+0xDF`  | f32       | body_height                     | |
| `+0xE3`  | u32       | body_weight                     | `1500000` on Garmoth |
| `+0xE7`  | u32       | obstacle_type                   | `2` on 316 rows, `1` on 242 |
| `+0xEB`  | u32       | overlap_check_type              | `1` on 5 rows |
| `+0xEF`  | f32       | overlap_check_distance          | `500.0` on the 5 rows with an `overlap_check_type` |
| `+0xF3`  | u32       | unknown_f3                      | Always `0` |
| `+0xF7`  | u32       | unknown_f7                      | Always `1` |
| `+0xFB`  | u32       | unknown_fb                      | Always `1` |
| `+0xFF`  | u8        | is_giant                        | `2` on 992 rows, `1` on 421 |
| `+0x100` | i16       | spawn_start_hour                | `-1` on 24,478 rows |
| `+0x102` | i16       | spawn_end_hour                  | `-1` on 24,478 rows |
| `+0x104` | u32       | voice_audio_count               | `1` on 113 rows |
| `+0x108` | u8        | is_attacked_pvp_mode_only       | `1` on 1,290 rows |
| `+0x109` | u8        | is_opti_monster                 | `1` on 54 rows, `2` on 13 |
| `+0x10A` | bytes[3]  | unknown_10a                     | Always `0` |
| `+0x10D` | u8        | is_check_dps                    | `1` on 36 rows |
| `+0x10E` | u16       | character_properties            | Non-zero on 1,703 rows |
| `+0x110` | u16       | unknown_110                     | `1` to `3` on 42 rows |
| `+0x112` | u16       | unknown_112                     | `1` to `3` on 42 rows |
| `+0x114` | u8        | unknown_114                     | Always `0` |
| `+0x115` | u8        | carrier_fishing_level           | `36` on 7 rows |
| `+0x116` | u8        | is_client_ai                    | `1` on 3,582 rows |
| `+0x117` | u32       | model_path_hash                 | Hash of `model_path`; see [Model Path](#model-path) |
| `+0x11B` | u32       | unknown_11b                     | Non-zero on exactly the 61 rows of `npc_kind` `0` |

`class_type` is a different ID from `character_id`: Warrior is character `1` / class `0`, Ranger `2` / `4`, Sorceress `3` / `8`, Berserker `4` / `12`, Tamer `5` / `16`, Musa `21` / `20`, Valkyrie `25` / `24`. The class number resolves through LOC `str_type=21` (class names) and is the value the client's `getClassType()` returns. bdo-data-extractor reads it as a u32; that fails on the 65 rows where `repair_resources` is `3`, so it is read here as a u8. Kunoichi and Ninja are separate classes (`25` and `26` in LOC type 21): character `26` Kunoichi has `25` and character `27` Ninja has `26`, but character `209`, also named Kunoichi with the same female model (`pc/13_pnw/ninjawomenaction_noweaponmain_w`), stores `26`. Whether that is a data slip or means something is not known; it cannot be seen in game.

### `characterstaticoffset.dbss`

Provides lookup rows for `characterstatic.dbss`. Rows sorted by `data_offset` cover the whole main file from `+0x04` through EOF when the two inline ID bytes before each payload are included.

| Offset              | Type             | Field        | Notes |
| ------------------- | ---------------- | ------------ | ----- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR` |
| `+0x04`             | u32              | count        | Number of rows, matching `characterstatic.dbss` |
| `+0x08`             | Index Row[count] | rows         | See Index Row |
| `rows+0x00`         | String Table     | string_table | Empty: `string_count` is `0`, as in `playercharacterstatic.bss` |
| `string_table+0x00` | u32              | table_start  | Equals the end offset of the offset-table rows |
| `string_table+0x04` | u32              | zero         | Always `0` |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u16  | character_id | Matches the two inline ID bytes immediately before `data_offset` |
| `+0x02` | u32  | data_offset  | Absolute byte offset into `characterstatic.dbss` payload data |
| `+0x06` | u32  | payload_size | Payload byte count, excluding the two inline ID bytes |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## Layout 2

Before client 3464 the 8 bytes of `unknown_c7` and the last byte,
`unknown_contents_group_hashes_17`, did not exist. Character Fields was 279
bytes, so `ai_script` started at `condition_script+0x117` and the model path
sat most often at `condition_script+291` (decimal) instead of `+299`. That
the 8 bytes sit right after `level` comes from the client 1784 file, where
`is_live_collect` follows `level` directly; the client before 3464 is not on hand
to check it. Only Payload and Character Fields differ from Layout 3. The
parser reads only Layout 3.

### Payload (variable: 421 bytes, size from `characterstaticoffset.dbss`)

| Offset                        | Type                      | Field                             | Notes |
| ----------------------------- | ------------------------- | --------------------------------- | ----- |
| `+0x00`                       | u8                        | is_hidden_name                    |       |
| `+0x01`                       | u8                        | is_hidden_hp                      |       |
| `+0x02`                       | u16                       | dialog_type                       |       |
| `+0x04`                       | u8                        | is_tamable                        |       |
| `+0x05`                       | u8                        | is_render_shadow                  |       |
| `+0x06`                       | u8                        | use_default_audio                 |       |
| `+0x07`                       | u8                        | absolute_interaction              |       |
| `+0x08`                       | u8                        | unknown_08                        |       |
| `+0x09`                       | str16                     | action_script                     |       |
| `action_script+0x00`          | str16                     | condition_script                  |       |
| `condition_script+0x00`       | Character Fields          | character_fields                  |       |
| `condition_script+0x117`      | str8                      | ai_script                         |       |
| `ai_script+0x00`              | str8                      | model_path                        |       |
| `model_path+0x00`             | str16                     | name_kr                           |       |
| `name_kr+0x00`                | str16                     | label_kr                          |       |
| `label_kr+0x00`               | str16                     | title_kr                          |       |
| `title_kr+0x00`               | str8                      | voice_bank                        |       |
| `voice_bank+0x00`             | u32                       | carriage_type                     |       |
| `voice_bank+0x04`             | u8                        | unknown_voice_bank_04             |       |
| `voice_bank+0x05`             | i16                       | team_no                           |       |
| `voice_bank+0x07`             | u8                        | unknown_voice_bank_07             |       |
| `voice_bank+0x08`             | i16                       | time_attack_type                  |       |
| `voice_bank+0x0A`             | u32                       | time_attack_limit_minute          |       |
| `voice_bank+0x0E`             | u32                       | holdable_item_count               |       |
| `voice_bank+0x12`             | u32[holdable_item_count]  | holdable_item_keys                |       |
| `holdable_item_keys+0x00`     | bytes[8]                  | unknown_holdable_item_keys_00     |       |
| `holdable_item_keys+0x08`     | u32                       | unknown_holdable_item_keys_08     |       |
| `holdable_item_keys+0x0C`     | u64                       | attribute_type_mask               |       |
| `holdable_item_keys+0x14`     | u16                       | steal_drop_id                     |       |
| `holdable_item_keys+0x16`     | u16                       | unknown_holdable_item_keys_16     |       |
| `holdable_item_keys+0x18`     | u32                       | contents_group_count              |       |
| `holdable_item_keys+0x1C`     | u32[contents_group_count] | contents_group_hashes             |       |
| `contents_group_hashes+0x00`  | u8                        | class_type                        |       |
| `contents_group_hashes+0x01`  | u8                        | repair_resources                  |       |
| `contents_group_hashes+0x02`  | bytes[7]                  | unknown_contents_group_hashes_02  |       |
| `contents_group_hashes+0x09`  | u32                       | source_item_id                    |       |
| `contents_group_hashes+0x0D`  | bytes[4]                  | unknown_contents_group_hashes_0d  |       |
| `contents_group_hashes+0x11`  | u8                        | unknown_contents_group_hashes_11  |       |
| `contents_group_hashes+0x12`  | u8                        | unknown_contents_group_hashes_12  |       |
| `contents_group_hashes+0x13`  | f32                       | reset_distance                    |       |

### Character Fields (279 bytes)

| Offset   | Type      | Field                           | Notes |
| -------- | --------- | ------------------------------- | ----- |
| `+0x00`  | u8        | is_developing_contents          |       |
| `+0x01`  | u16       | character_id                    |       |
| `+0x03`  | i16       | character_group                 |       |
| `+0x05`  | u8        | npc_kind                        |       |
| `+0x06`  | u8        | grade                           |       |
| `+0x07`  | i32       | tendency_on_dead                |       |
| `+0x0B`  | i32       | ocean_tendency                  |       |
| `+0x0F`  | f32[3]    | box_size                        |       |
| `+0x1B`  | u32       | unknown_1b                      |       |
| `+0x1F`  | u16       | collect_drop_id                 |       |
| `+0x21`  | f32       | max_hp                          |       |
| `+0x25`  | u32       | max_mp                          |       |
| `+0x29`  | u32       | sub_resource_point              |       |
| `+0x2D`  | bytes[16] | unknown_2d                      |       |
| `+0x3D`  | f32       | unknown_3d                      |       |
| `+0x41`  | bytes[8]  | unknown_41                      |       |
| `+0x49`  | u32       | regen_sub_resource_point        |       |
| `+0x4D`  | u32       | active_regen_sub_resource_point |       |
| `+0x51`  | u32       | unknown_51                      |       |
| `+0x55`  | u32       | max_critical_rate               |       |
| `+0x59`  | u32       | max_drop_item_luck              |       |
| `+0x5D`  | u32       | max_fishing_luck                |       |
| `+0x61`  | u32       | max_collection_luck             |       |
| `+0x65`  | i64       | max_weight                      |       |
| `+0x6D`  | f32       | unknown_6d                      |       |
| `+0x71`  | u32       | suspension                      |       |
| `+0x75`  | u32[3]    | unknown_75                      |       |
| `+0x81`  | u32[3]    | max_varied_speed                |       |
| `+0x8D`  | f32       | unknown_8d                      |       |
| `+0x91`  | bytes[12] | unknown_91                      |       |
| `+0x9D`  | u8        | is_fixed                        |       |
| `+0x9E`  | u8        | is_catchedable                  |       |
| `+0x9F`  | u8        | unknown_9f                      |       |
| `+0xA0`  | u8        | unknown_a0                      |       |
| `+0xA1`  | u8        | unknown_a1                      |       |
| `+0xA2`  | u8        | unknown_a2                      |       |
| `+0xA3`  | u8        | is_guild_vehicle                |       |
| `+0xA4`  | u8        | is_using_vehicle_in_siege       |       |
| `+0xA5`  | u8        | unknown_a5                      |       |
| `+0xA6`  | u8        | vehicle_type                    |       |
| `+0xA7`  | u8        | vehicle_sub_type                |       |
| `+0xA8`  | u8        | unknown_a8                      |       |
| `+0xA9`  | bytes[7]  | unknown_a9                      |       |
| `+0xB0`  | u8        | vehicle_seat_count              |       |
| `+0xB1`  | u8        | vehicle_driver_ridable          |       |
| `+0xB2`  | u8        | unknown_b2                      |       |
| `+0xB3`  | u8        | tribe_type                      |       |
| `+0xB4`  | u8        | inventory_max                   |       |
| `+0xB5`  | u8        | unknown_b5                      |       |
| `+0xB6`  | u8        | unknown_b6                      |       |
| `+0xB7`  | u8        | unknown_b7                      |       |
| `+0xB8`  | u8        | unknown_b8                      |       |
| `+0xB9`  | u8        | unknown_b9                      |       |
| `+0xBA`  | u8        | is_pushable                     |       |
| `+0xBB`  | u8        | is_carrier                      |       |
| `+0xBC`  | u8        | unknown_bc                      |       |
| `+0xBD`  | u8        | unknown_bd                      |       |
| `+0xBE`  | u8        | unknown_be                      |       |
| `+0xBF`  | u8        | unknown_bf                      |       |
| `+0xC0`  | u8        | unknown_c0                      |       |
| `+0xC1`  | u8        | unknown_c1                      |       |
| `+0xC2`  | u8        | unknown_c2                      |       |
| `+0xC3`  | u32       | level                           |       |
| `+0xC7`  | u32       | is_live_collect                 |       |
| `+0xCB`  | i64       | vanish_time                     |       |
| `+0xD3`  | f32       | body_size                       |       |
| `+0xD7`  | f32       | body_height                     |       |
| `+0xDB`  | u32       | body_weight                     |       |
| `+0xDF`  | u32       | obstacle_type                   |       |
| `+0xE3`  | u32       | overlap_check_type              |       |
| `+0xE7`  | f32       | overlap_check_distance          |       |
| `+0xEB`  | u32       | unknown_f3                      |       |
| `+0xEF`  | u32       | unknown_f7                      |       |
| `+0xF3`  | u32       | unknown_fb                      |       |
| `+0xF7`  | u8        | is_giant                        |       |
| `+0xF8`  | i16       | spawn_start_hour                |       |
| `+0xFA`  | i16       | spawn_end_hour                  |       |
| `+0xFC`  | u32       | voice_audio_count               |       |
| `+0x100` | u8        | is_attacked_pvp_mode_only       |       |
| `+0x101` | u8        | is_opti_monster                 |       |
| `+0x102` | bytes[3]  | unknown_10a                     |       |
| `+0x105` | u8        | is_check_dps                    |       |
| `+0x106` | u16       | character_properties            |       |
| `+0x108` | u16       | unknown_110                     |       |
| `+0x10A` | u16       | unknown_112                     |       |
| `+0x10C` | u8        | unknown_114                     |       |
| `+0x10D` | u8        | carrier_fishing_level           |       |
| `+0x10E` | u8        | is_client_ai                    |       |
| `+0x10F` | u32       | model_path_hash                 |       |
| `+0x113` | u32       | unknown_11b                     |       |

## Layout 1

The client 1784 file (15,704 records). Character Fields is 298
bytes: it has a `stun_gauge`, 12 more zero bytes before `max_varied_speed`
(the 12 extra bytes of the [experience.bss](experience_bss.md#layout-1) Layout
1 Stat Body) and four other zero runs, and lacks `unknown_c7`. The tail has
16 more zero bytes before `time_attack_type`, a constant `1000.0` and a
constant `1` around `attribute_type_mask`, and ends before `reset_distance`.
Only Payload and Character Fields differ from Layout 2. Values on client 1784
match the private server's `Character_Table` on every row; see [Field
Names](#field-names).

### Payload (variable: 468 bytes, size from `characterstaticoffset.dbss`)

| Offset                        | Type                      | Field                             | Notes |
| ----------------------------- | ------------------------- | --------------------------------- | ----- |
| `+0x00`                       | u8                        | is_hidden_name                    | |
| `+0x01`                       | u8                        | is_hidden_hp                      | |
| `+0x02`                       | u16                       | dialog_type                       | |
| `+0x04`                       | u8                        | is_tamable                        | |
| `+0x05`                       | u8                        | is_render_shadow                  | |
| `+0x06`                       | u8                        | use_default_audio                 | |
| `+0x07`                       | u8                        | absolute_interaction              | |
| `+0x08`                       | u8                        | unknown_08                        | `0x15` on every row |
| `+0x09`                       | str16                     | action_script                     | |
| `action_script+0x00`          | str16                     | condition_script                  | |
| `condition_script+0x00`       | Character Fields          | character_fields                  | |
| `condition_script+0x12A`      | str8                      | ai_script                         | |
| `ai_script+0x00`              | str8                      | model_path                        | |
| `model_path+0x00`             | str16                     | name_kr                           | |
| `name_kr+0x00`                | str16                     | label_kr                          | |
| `label_kr+0x00`               | str16                     | title_kr                          | |
| `title_kr+0x00`               | str8                      | voice_bank                        | |
| `voice_bank+0x00`             | u32                       | carriage_type                     | |
| `voice_bank+0x04`             | u8                        | unknown_voice_bank_04             | Always `0` |
| `voice_bank+0x05`             | i16                       | team_no                           | |
| `voice_bank+0x07`             | u8                        | unknown_voice_bank_07             | |
| `voice_bank+0x08`             | bytes[16]                 | unknown_old_voice_bank_08         | Always `0` |
| `voice_bank+0x18`             | i16                       | time_attack_type                  | |
| `voice_bank+0x1A`             | u32                       | time_attack_limit_minute          | |
| `voice_bank+0x1E`             | u32                       | holdable_item_count               | |
| `voice_bank+0x22`             | u32[holdable_item_count]  | holdable_item_keys                | |
| `holdable_item_keys+0x00`     | bytes[4]                  | unknown_old_holdable_item_keys_00 | Always `0` |
| `holdable_item_keys+0x04`     | f32                       | unknown_old_holdable_item_keys_04 | Always `1000.0` |
| `holdable_item_keys+0x08`     | bytes[8]                  | unknown_holdable_item_keys_00     | Always `0` |
| `holdable_item_keys+0x10`     | u32                       | unknown_holdable_item_keys_08     | Always `1000000` |
| `holdable_item_keys+0x14`     | bytes[8]                  | unknown_old_holdable_item_keys_14 | Always `0` |
| `holdable_item_keys+0x1C`     | u16                       | unknown_old_holdable_item_keys_1c | Always `1` |
| `holdable_item_keys+0x1E`     | u64                       | attribute_type_mask               | |
| `holdable_item_keys+0x26`     | u16                       | steal_drop_id                     | |
| `holdable_item_keys+0x28`     | u32                       | contents_group_count              | |
| `holdable_item_keys+0x2C`     | u32[contents_group_count] | contents_group_hashes             | |
| `contents_group_hashes+0x00`  | u8                        | class_type                        | |
| `contents_group_hashes+0x01`  | u8                        | repair_resources                  | |
| `contents_group_hashes+0x02`  | bytes[7]                  | unknown_contents_group_hashes_02  | |
| `contents_group_hashes+0x09`  | u32                       | source_item_id                    | |
| `contents_group_hashes+0x0D`  | bytes[4]                  | unknown_contents_group_hashes_0d  | |
| `contents_group_hashes+0x11`  | u8                        | unknown_contents_group_hashes_11  | |
| `contents_group_hashes+0x12`  | u8                        | unknown_contents_group_hashes_12  | |

### Character Fields (298 bytes)

| Offset   | Type      | Field                           | Notes |
| -------- | --------- | ------------------------------- | ----- |
| `+0x00`  | u8        | is_developing_contents          | |
| `+0x01`  | u8        | unknown_old_01                  | Always `0` |
| `+0x02`  | u16       | character_id                    | |
| `+0x04`  | i16       | character_group                 | |
| `+0x06`  | u8        | npc_kind                        | |
| `+0x07`  | u8        | grade                           | |
| `+0x08`  | i32       | tendency_on_dead                | |
| `+0x0C`  | i32       | ocean_tendency                  | |
| `+0x10`  | f32[3]    | box_size                        | |
| `+0x1C`  | u32       | unknown_1b                      | |
| `+0x20`  | u16       | collect_drop_id                 | |
| `+0x22`  | f32       | max_hp                          | |
| `+0x26`  | u32       | max_mp                          | |
| `+0x2A`  | i16       | stun_gauge                      | Non-zero on 4 rows; `StunGauge` |
| `+0x2C`  | u32       | sub_resource_point              | |
| `+0x30`  | bytes[16] | unknown_2d                      | |
| `+0x40`  | f32       | unknown_3d                      | |
| `+0x44`  | bytes[8]  | unknown_41                      | |
| `+0x4C`  | u32       | regen_sub_resource_point        | |
| `+0x50`  | u32       | active_regen_sub_resource_point | |
| `+0x54`  | u32       | unknown_51                      | Always `0` |
| `+0x58`  | u32       | max_critical_rate               | |
| `+0x5C`  | u32       | max_drop_item_luck              | |
| `+0x60`  | u32       | max_fishing_luck                | |
| `+0x64`  | u32       | max_collection_luck             | |
| `+0x68`  | i64       | max_weight                      | |
| `+0x70`  | f32       | unknown_6d                      | |
| `+0x74`  | u32       | suspension                      | |
| `+0x78`  | u32[3]    | unknown_75                      | Always `0` |
| `+0x84`  | bytes[12] | unknown_old_84                  | Always `0` |
| `+0x90`  | u32[3]    | max_varied_speed                | |
| `+0x9C`  | f32       | unknown_8d                      | |
| `+0xA0`  | bytes[8]  | unknown_91                      | Always `0` |
| `+0xA8`  | u8        | is_fixed                        | |
| `+0xA9`  | u8        | is_catchedable                  | |
| `+0xAA`  | u8        | unknown_9f                      | |
| `+0xAB`  | u8        | unknown_a0                      | |
| `+0xAC`  | u8        | unknown_a1                      | |
| `+0xAD`  | u8        | unknown_a2                      | |
| `+0xAE`  | u8        | unknown_old_ae                  | `0` or `1`; no counterpart on client 3474 |
| `+0xAF`  | bytes[7]  | unknown_old_af                  | Always `0` |
| `+0xB6`  | u8        | is_guild_vehicle                | |
| `+0xB7`  | u8        | is_using_vehicle_in_siege       | |
| `+0xB8`  | u8        | unknown_a5                      | |
| `+0xB9`  | u8        | vehicle_type                    | `63` when the character is not a vehicle |
| `+0xBA`  | u8        | vehicle_sub_type                | |
| `+0xBB`  | u8        | unknown_a8                      | Always `0` |
| `+0xBC`  | bytes[7]  | unknown_a9                      | Always `0` |
| `+0xC3`  | u8        | vehicle_seat_count              | |
| `+0xC4`  | u8        | vehicle_driver_ridable          | |
| `+0xC5`  | u8        | unknown_b2                      | |
| `+0xC6`  | u8        | tribe_type                      | `CppEnums.TribeType` numbering |
| `+0xC7`  | u8        | inventory_max                   | |
| `+0xC8`  | u8        | unknown_b5                      | |
| `+0xC9`  | u8        | unknown_b6                      | |
| `+0xCA`  | u8        | unknown_b7                      | |
| `+0xCB`  | u8        | unknown_b8                      | Always `0` |
| `+0xCC`  | u8        | is_pushable                     | |
| `+0xCD`  | u8        | is_carrier                      | |
| `+0xCE`  | u8        | unknown_bc                      | |
| `+0xCF`  | u8        | unknown_bd                      | |
| `+0xD0`  | u8        | unknown_be                      | |
| `+0xD1`  | u8        | unknown_bf                      | |
| `+0xD2`  | u8        | unknown_c0                      | |
| `+0xD3`  | u8        | unknown_c1                      | |
| `+0xD4`  | u8        | unknown_c2                      | |
| `+0xD5`  | u32       | level                           | |
| `+0xD9`  | u32       | is_live_collect                 | |
| `+0xDD`  | i64       | vanish_time                     | |
| `+0xE5`  | f32       | body_size                       | |
| `+0xE9`  | f32       | body_height                     | |
| `+0xED`  | u32       | body_weight                     | |
| `+0xF1`  | u32       | obstacle_type                   | |
| `+0xF5`  | u32       | overlap_check_type              | |
| `+0xF9`  | f32       | overlap_check_distance          | |
| `+0xFD`  | u32       | unknown_f3                      | |
| `+0x101` | u32       | unknown_f7                      | |
| `+0x105` | u32       | unknown_fb                      | |
| `+0x109` | u8        | is_giant                        | |
| `+0x10A` | i16       | spawn_start_hour                | |
| `+0x10C` | i16       | spawn_end_hour                  | |
| `+0x10E` | u32       | voice_audio_count               | |
| `+0x112` | u8        | is_attacked_pvp_mode_only       | |
| `+0x113` | u8        | is_opti_monster                 | |
| `+0x114` | bytes[3]  | unknown_10a                     | |
| `+0x117` | u8        | is_check_dps                    | |
| `+0x118` | u32       | character_properties            | |
| `+0x11C` | u8        | unknown_old_11c                 | Always `0` |
| `+0x11D` | u32       | carrier_fishing_level           | |
| `+0x121` | u8        | is_client_ai                    | |
| `+0x122` | u32       | model_path_hash                 | |
| `+0x126` | u32       | unknown_11b                     | |

## Field Names

The private server's `DataSheets.bexcel` (client 1784) has a `Character_Table`
sheet of 17,471 rows; 16,396 share a key with the client 1784 file and 16,058
with client 3474. Each field below matches its column by value on the shared
rows. The client 1784 file was compiled from the same data, so it matches on
nearly every row; client 3474 differs where characters were changed since.

| Field | `Character_Table` column | Rows that agree, client 1784 | Rows that agree, client 3474 |
| ----- | ------------------------ | ---------------------------- | ---------------------------- |
| `is_hidden_name` | `IsHiddenName` | 16,396 of 16,396 | 15,963 of 16,058 |
| `is_hidden_hp` | `IsHiddenHp` | 16,396 of 16,396 | 15,864 of 16,058 |
| `dialog_type` | `DialogType` | 16,396 of 16,396 | 16,053 of 16,058 |
| `is_tamable` | `Tamable` | 16,396 of 16,396 | 16,058 of 16,058 |
| `is_render_shadow` | `isRenderShadow` | 16,396 of 16,396 | 16,058 of 16,058 |
| `use_default_audio` | `UseDefaultAudio` | 16,396 of 16,396 | 16,017 of 16,058 |
| `absolute_interaction` | `AbsoluteInteraction` | 16,396 of 16,396 | 16,053 of 16,058 |
| `action_script` | `ActiveCondition` | 16,141 of 16,396 | 15,822 of 16,058 |
| `condition_script` | `InteractionCondition` | 16,396 of 16,396 | 15,995 of 16,058 |
| `is_developing_contents` | `IsDevelopingContents` | 16,396 of 16,396 | 16,037 of 16,058 |
| `character_group` | `CharacterGroup` | 16,396 of 16,396 | 15,671 of 16,058 |
| `npc_kind` | `CharKind` | 16,396 of 16,396 | 16,023 of 16,058 |
| `grade` | `GradeType` | 16,396 of 16,396 | 15,828 of 16,058 |
| `tendency_on_dead` | `variedTendencyOnDead` | 16,392 of 16,396 | 12,505 of 16,058 |
| `ocean_tendency` | `variedOceanTendencyOnDead` | 16,396 of 16,396 | 16,052 of 16,058 |
| `box_size` | `BoxSize` | 16,396 of 16,396 | 15,992 of 16,058 |
| `collect_drop_id` | `CollectDropID` | 16,396 of 16,396 | 16,047 of 16,058 |
| `max_hp` | `HP` | 16,396 of 16,396 | 15,931 of 16,058 |
| `max_mp` | `MP` | 16,357 of 16,396 | 16,018 of 16,058 |
| `stun_gauge` | `StunGauge` | 16,396 of 16,396 | - |
| `sub_resource_point` | `SubResourcePoint` | 16,396 of 16,396 | 16,057 of 16,058 |
| `regen_sub_resource_point` | `RegenSubResourcePoint` | 16,396 of 16,396 | 16,057 of 16,058 |
| `active_regen_sub_resource_point` | `ActiveRegenSubResourcePoint` | 16,396 of 16,396 | 16,057 of 16,058 |
| `max_critical_rate` | `MaxCriticalRate` | 16,396 of 16,396 | 16,058 of 16,058 |
| `max_drop_item_luck` | `MaxDropItemLuck` | 16,396 of 16,396 | 15,941 of 16,058 |
| `max_fishing_luck` | `MaxFishingLuck` | 16,396 of 16,396 | 15,941 of 16,058 |
| `max_collection_luck` | `MaxCollectionLuck` | 16,396 of 16,396 | 15,941 of 16,058 |
| `max_weight` | `possessableWeight` | 16,396 of 16,396 | 16,028 of 16,058 |
| `suspension` | `Suspension` | 16,396 of 16,396 | 15,937 of 16,058 |
| `is_fixed` | `IsFixed` | 16,396 of 16,396 | 16,002 of 16,058 |
| `is_catchedable` | `IsCatchedable` | 16,396 of 16,396 | 15,877 of 16,058 |
| `is_guild_vehicle` | `IsGuildVehicle` | 16,396 of 16,396 | 16,058 of 16,058 |
| `is_using_vehicle_in_siege` | `IsUsingVehicleInSiege` | 16,396 of 16,396 | 16,058 of 16,058 |
| `vehicle_type` | `VehicleType` | 16,396 of 16,396 | 16,037 of 16,058 |
| `vehicle_sub_type` | `VehicleSubType` | 16,396 of 16,396 | 16,052 of 16,058 |
| `vehicle_seat_count` | `VehicleSeatCount` | 16,396 of 16,396 | 16,042 of 16,058 |
| `vehicle_driver_ridable` | `VehicleDriverRidable` | 16,396 of 16,396 | 16,053 of 16,058 |
| `tribe_type` | `TribeType` | 16,396 of 16,396 | 10,934 of 16,058 |
| `inventory_max` | `InventoryMax` | 16,396 of 16,396 | 16,048 of 16,058 |
| `is_pushable` | `IsPushable` | 16,396 of 16,396 | 15,869 of 16,058 |
| `is_carrier` | `isCarrier` | 16,396 of 16,396 | 16,050 of 16,058 |
| `level` | `Level` | 16,395 of 16,396 | 14,785 of 16,058 |
| `vanish_time` | `VanishTime` | 16,384 of 16,396 | 15,573 of 16,058 |
| `is_live_collect` | `IsLiveCollect` | - | 16,058 of 16,058 |
| `body_size` | `BodySize` | 16,396 of 16,396 | 15,497 of 16,058 |
| `body_height` | `BodyHeight` | 16,396 of 16,396 | 15,416 of 16,058 |
| `body_weight` | `Weight` | 16,396 of 16,396 | 15,573 of 16,058 |
| `obstacle_type` | `ObstacleType` | 16,396 of 16,396 | 16,048 of 16,058 |
| `overlap_check_type` | `OverrapCheckType` | 16,395 of 16,395 | 16,056 of 16,057 |
| `overlap_check_distance` | `OverrapCheckDistance` | 16,396 of 16,396 | 16,057 of 16,058 |
| `is_giant` | `IsGiant` | 16,396 of 16,396 | 15,700 of 16,058 |
| `spawn_start_hour` | `SpawnStartHour` | 16,396 of 16,396 | 16,057 of 16,058 |
| `spawn_end_hour` | `SpawnEndHour` | 16,396 of 16,396 | 16,057 of 16,058 |
| `voice_audio_count` | `VoiceAudioCounts` | 16,396 of 16,396 | 16,058 of 16,058 |
| `is_attacked_pvp_mode_only` | `IsAttackedPvPModeOnly` | 16,396 of 16,396 | 16,058 of 16,058 |
| `is_opti_monster` | `IsOptiMonster` | 16,396 of 16,396 | 16,054 of 16,058 |
| `is_check_dps` | `IsCheckDPS` | 16,396 of 16,396 | 16,058 of 16,058 |
| `character_properties` | `CharacterProperties` | 16,396 of 16,396 | 15,832 of 16,058 |
| `carrier_fishing_level` | `CarrierFishingLevel` | 16,396 of 16,396 | 16,058 of 16,058 |
| `is_client_ai` | `IsClientAI` | 16,396 of 16,396 | 16,051 of 16,058 |
| `ai_script` | `AiScriptClassName` | 16,394 of 16,396 | 13,751 of 16,058 |
| `model_path` | `ActionScript FilePrefix`, `ActionScript File0` | 16,386 of 16,396 | 15,330 of 16,058 |
| `name_kr` | `DisplayName` | 16,319 of 16,396 | 15,073 of 16,058 |
| `label_kr` | `CharName` | 15,637 of 16,396 | 14,951 of 16,058 |
| `title_kr` | `CharacterTitle` | 16,395 of 16,396 | 15,592 of 16,058 |
| `voice_bank` | `VoiceBankFileName` | 16,387 of 16,396 | 15,667 of 16,058 |
| `carriage_type` | `CarriageType` | 16,396 of 16,396 | 16,057 of 16,058 |
| `team_no` | `TeamNo` | 16,396 of 16,396 | 16,048 of 16,058 |
| `time_attack_type` | `TimeAttackType` | 16,396 of 16,396 | 16,058 of 16,058 |
| `time_attack_limit_minute` | `TimeAttackLimitMinute` | 16,396 of 16,396 | 16,058 of 16,058 |
| `holdable_item_keys` | `HoldableItemKey` | 16,393 of 16,396 | 16,052 of 16,058 |
| `attribute_type_mask` | `AttributeType` | 16,395 of 16,396 | 15,784 of 16,058 |
| `steal_drop_id` | `StealDropID` | 16,396 of 16,396 | 16,055 of 16,058 |
| `contents_group_hashes` | `ContentsGroupKey` | 349 of 349 keys | 344 of 354 keys |
| `repair_resources` | `RepairResources` | 16,396 of 16,396 | 16,058 of 16,058 |
| `reset_distance` | `ResetDistance` | - | 15,791 of 16,058 |

How the compiler writes a column:

- `HP` and `MP` cells of `0` become `1.0` and `1` (6,398 of the 16,396
  client 1784 rows have an `HP` of their own).
- A `VehicleType` of `-1` becomes the member count of the enum: `63` on
  client 1784, `65` on client 3474, which has two more members.
- `AttributeType` is a list (`16, 46`); the file sets one bit per value.
- `ContentsGroupKey` is a list (`6, 1448`); the file stores the client's string
  hash of each key, see [Contents Groups](#contents-groups).
- `model_path` is `ActionScript FilePrefix`, `_` and `ActionScript File0` in
  lower case: `Monster/PartyLeader/Dri_Dragon_Boss` and `Ghost` give
  `monster/partyleader/dri_dragon_boss_ghost` (Garmoth).
- Text cells lose trailing spaces (`Pet_SnowMan ` is stored as `Pet_SnowMan`).

Where client 1784 differs from the sheet, the private server edited the
sheet: the 255 `action_script` rows that differ store `getknowledge(19);`
where the sheet names another knowledge (`50781`: `getknowledge(1626);`).

The names `max_critical_rate`, the three luck limits and `max_varied_speed`
follow [experience.bss](experience_bss.md#stat-body-200-bytes), where the same
fields were named from the `Pc_Table` sheet. `regen_sub_resource_point` and
`active_regen_sub_resource_point` hold the same value on every row; the 2016
client's `gc::CharacterStatStaticStatus` lists `_regenSubResourcePoint` before
`_activeRegenSubResourcePoint`, which splits them.

`unknown_bc` holds `isTaming` on all but 36 of the 16,396 client 1784 rows,
and `unknown_bf` holds `isSiegeVehicle` on all but 57; with that many
exceptions in a file compiled from the sheet, the byte likely holds a value
derived from more than one column, and both stay unnamed. `unknown_1b` holds
`FusionGroupKey` on its one non-zero row (`530`, value `1` in both), which is
too little to name it here; [`charactersimply.bss`](charactersimply_bss.md)
names the same field `fusion_group_key`. `is_live_collect` was matched through
`charactersimply.bss`, which holds the same value for every character: it
agrees with `IsLiveCollect` on 16,058 of 16,058 client 3474 rows and on all
15,704 rows of the client 1784 `charactersimply.bss`.

Sheet columns with no match in the file, such as `DropID`, `ExpectedPrice`,
`AttackRange`, `ReSpawnType`, `IsEventSpawn` and the combat stat
columns (`DDD`, `DPV`), are server data: they stay on zero bytes or match no
offset at all.

## `npc_kind` Values

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::CharacterKind::Type` names `0` to `9`, and the characters that store each
value still fit the name:

| Value | `gc::CharacterKind` | Rows (client 3464) | Model folders | Examples |
| ----- | ------------------- | ----- | ------------- | -------- |
| `0`   | Player              | 61    | `pc` only; exactly the player-character IDs `1`-`47` and `201`-`214` | `1` Warrior |
| `1`   | Monster             | 9,212 | Mostly `monster`, also `infinitydefence`, `pc_summon`, `object` | `29929` Garmoth |
| `2`   | Npc                 | 6,225 | Mostly `npc`, also `object`, `monster` | `47791` Ehren |
| `3`   | Vehicle             | 3,296 | `creature`, `riding`, `cash` (pets and mounts) | `9001` Beginner's Brown Horse, `35423` Crank, carried quest objects |
| `4`   | Collect             | 564   | `object` only | `11982` Rhyolite, trees |
| `5`   | SiegeGate           | 10    |               | `529` Outer Gate |
| `6`   | SiegeSymbol         | 1     |               | `517` Siege Guardian Stone |
| `7`   | Household           | 940   | Mostly `monster` | Field HQ, Command Post, Indomitable Flag |
| `8`   | Installation        | 3,970 | `monster` | `16110` Beautiful Opal Vase, `16640` Dev Plant210 |
| `9`   | InstanceObject      | 220   | `summon` | `12842` Flimsy Wooden Fence, barricades |

`12`, `15` and `17` (1, 1 and 50 rows) came after 2016 and have no name. The
Lua's `CppEnums.ActorType` (`4` Gate, `5` Alterego, `6` Collect, `9` Deadbody)
is a different numbering and fits only `0` to `3`.

## Grade

`grade` is a `CppEnums.CharacterGradeType` value. The enum in `global_define_cpp_enum.luac` names `0` Normal, `1` Elite, `2` Hero, `3` Legend, `4` Boss and `5` Assistant, and the target bar script (`panel_widget_enemygauge_new.luac`) draws the boss HP bar when `getCharacterGradeType()` returns `4`. World bosses store `4`: `29929` Garmoth, `8609` Kzarka, `8608` Nouver.

| Value | Rows (client 3464) | Examples |
| ----- | ------------------ | -------- |
| `0`   | 21,576 | Most characters; Naive workers (`8011` Naive Fadus Worker) |
| `1`   | 552    | Plain workers (`8040` Human Worker), quest characters (`62083` Al Rhundi) |
| `2`   | 554    | Skilled workers (`8041`) |
| `3`   | 171    | Professional workers (`8042`) |
| `4`   | 1,650  | Bosses; Artisan workers (`8043`) |
| `5`   | 3      | `28468` Centaurus Axeman and two other Infinity Tower monsters |
| `6`   | 37     | Traps and towers (`60109` Flame Trap, `62415` Defense Tower) |
| `7`   | 8      | Sacraments and relics (`27134` Forest Sacrament, `26399` Blood Relic) |

Workers store their worker grade here, Naive `0` to Artisan `4`, so the enum names do not fit them. `6` and `7` are not in the enum.

## Character Group

`character_group` is the sheet's `CharacterGroup` and the 2016 client's
`_groupKey` (`gc::KeyType<short,-1>`). It groups monsters by content: `157`
Infinity Tower monsters (199 rows), `96` Savage Rift (89), `95` world and
raid bosses (`29929` Garmoth, `28732` Vell), `84` sea monsters, `121` Dark
Rift bosses (client 3464; Korean labels ending in `_어둠의틈`). It is non-zero on 2,450 rows on client 3474. Earlier
versions of this doc called it `unknown_p3` and read the third-party "tribe
type" note onto it; the tribe is [`tribe_type`](#tribe-type).

The quest condition `killMonsterGroup(group, count)` takes this key. The
2016 `gc::KillMonsterGroup` holds `_characterGroupKey`
(`gc::KeyType<short,-1>`) and `_count`, and on client 3474 the 878 calls
in [`quest.dbss`](quest_dbss.md) completion scripts use 167 keys, the 16
in [`guildquest.dbss`](guildquest_dbss.md) use `84` and `125`, and every
one of these keys is a `character_group` value. No client file lists or
names the groups: membership is this field alone, and
[`monstergroup.dbss`](monstergroup_dbss.md) is a separate key set. The
`#MonsterGroup` sheet of a private server's `datasheet_titletable.xlsm`
(client 1784) names 122 groups in two columns, `CharacterGroup` and
`MonsterGroup`, for example `84` `대양 몬스터` (sea monsters) and `116`
`별무덤` (Star's End); all 122 keys have characters on client 3474. Like the
other `#` sheets of that workbook it is not in the compiled
`DataSheets.bexcel`.

The app groups the characters by this field into the
`CHARACTER_GROUP_MEMBERS` lookup index (`build_character_group_index`), 258
groups on client 3474. The `quest.dbss` and `guildquest.dbss` Kill Groups
columns and the soul collectors' Event Param 1 column of `itemenchant.dbss`
show a group as its key and the distinct names of its members.

## Tribe Type

`tribe_type` is the value `getTribeType()` returns in the target bar script
(`panel_widget_enemygauge_new.luac`), which passes it to
`PaGlobal_GetTribeTypeTextureId` in `global_define.luac`. That function
compares it with the `__eNewTribeType_*` constants (Human, NonHuman, Others,
Kamasilvia, Edania, HuntCreature, SiegeObject), the enum
[dropuihuntinggroundinfo.bss](dropuihuntinggroundinfo_bss.md#tribe_type-values)
numbers `0` to `4`. The values on client 3474 fit it:

| Value | Rows (client 3474) | Examples |
| ----- | ------------------ | -------- |
| `0`   | 1,545  | Player characters, cultists (`35413`) |
| `1`   | 11,111 | Most NPCs, mounts and pets |
| `2`   | 4,161  | Garmoth (`29929`) and other monsters |
| `3`   | 937    | Olun's Silence, Butcher of Gyfin Rhasia, Mutant Swamp Sentinel (`59679`), also Nouver |
| `4`   | 559    | Edania characters (`29304` Aal, Markthanan's Energy) |
| `5`, `7` | 13, 10 | NPCs and vehicles |
| `8`   | 179    | Hunting targets: Blue Whale, Khalk, Rock Elephant, Rubin's Scarecrow (`59213`) |
| `9`   | 694    | Siege objects (`62415` Defense Tower, Hwacha, `61166` Goldmont Medium Battleship) |
| `10`  | 5,344  | Installations (3,915 of `npc_kind` `8`) and other objects |

`8` and `9` fit `HuntCreature` and `SiegeObject`, but the Lua does not give
their numbers. Client 1784 stores the older `CppEnums.TribeType`
(`global_define_cpp_enum.luac`: `0` Human, `1` Ain, `2` ETC, `3` Boss, `4`
Reptile, `5` Untribe, `6` Hunting) in the same byte, which matches the sheet's
`TribeType` on every row. Client 3474 agrees with that sheet on 10,934 of
16,058 rows; on 3,600 a sheet `1` is now `10`.

## Level

`level` is the sheet's `Level` (16,395 of 16,396 rows on client 1784). On
client 3474 it is `1` on 9,628 rows (players, workers, `16640` Dev Plant210),
`99` on 5,531 (mostly NPCs, `47791` Ehren) and monster levels elsewhere
(`29929` Garmoth `60`, `8609` Kzarka `55`).

## Karma

`tendency_on_dead` is the karma change for killing the character. The client calls karma "tendency": the target bar scripts (`panel_widget_enemygauge_new.luac`, `panel_widget_monsterbar_renew.luac`) read `getTendencyOnDead()` from the character static status and warn that attacking the target lowers your karma when the value is below `0`. The stored values follow that sign, on client 3464:

| `npc_kind` | Positive | Zero | Negative |
| ---------- | -------- | ---- | -------- |
| `0` (player) | 0 | 2 | 59 (`-200000` on 47, `-5000` on 12) |
| `1` (monster) | 4,869 | 4,323 | 20 |
| `2` (NPC) | 126 | 6,097 | 2 |
| `3` (pet, mount) | 0 | 363 | 2,933 (`-500` on 2,791) |

Every other kind stores `0`. Values range from `-200000` to `500`. The positive NPC rows are quest objects such as `37062` Old Book from Cron Castle.

The sheet column is `variedTendencyOnDead`. Client 3474 agrees with it on only 12,505 of 16,058 rows because pets and mounts got their `-500` after client 1784.

## Ocean Tendency

`ocean_tendency` is non-zero on 104 rows (client 3464), all of kind `1` or `3`: positive on 62 monsters, nearly all sea monsters and pirate ships (`21418` Hekaru, `21484` Goldmont Large Battleship, `28682` Lyngbakr; up to `10000`), `-200000` on 40 player ships (`9032` Rowboat, `31045` Epheria Carrack) and `-30000` on the two Monsterbane Cannons (`31046`, `31052`). The client's word for naval fame is ocean tendency (`getOceanTendency()` in this table's condition scripts, `FromClient_OceanTendencyChanged` in the Lua). The sheet column is `variedOceanTendencyOnDead`, the naval fame counterpart of `variedTendencyOnDead`.

## Vehicle Type

`vehicle_type` is a `CppEnums.VehicleType` value (`global_define_cpp_enum.luac`). The enum is sparse (`0` to `63` with gaps), and the names fit the characters that store them on client 3464: `0` Horse on 319 rows (`9001` Beginner's Brown Horse), `30` Cat on 778 and `31` Dog on 1,682 (pets), `18` Boat (`9032` Rowboat), `34` SailingBoat (`9090` Galley), `47` CampingTent (`9999` Camp), `58` BossMonster (`31629` Skyrend), `60` Carrack (`31045` Epheria Carrack), `63` GuildDragon (`31125` Doomcaller).

Every record of `npc_kind` `3` stores a vehicle type; every other record stores `65`, except two kind `2` Shrine Relics (`30122`, `30167`) with `5` Bomb. `65` is the sheet's `-1` written as the enum's member count (`63` on client 1784, before two members were added), so it reads as "not a vehicle". The data also holds values the Lua enum does not name: `6` (cranks, `35423`), `8` (Heuklang, `60076`), `20` (`59720` Fwuzzy), `21` and `23` (Catapults `9038`, `9039`) and `27` (`9046` Log). The 2016 client's `gc::VehicleType` names all six, and the names fit: `6` GateCrank, `8` Haetae, `20` QuestDonkey, `21` Catapult, `23` Catapult2, `27` LumberVerticalSaw. The browser uses those names for them (`_common/vehicle_type.py`). Where both enums name a value, the Lua wins (`26` Cow, 2016 MilkCow; `35` Train, 2016 Tank).

## Attribute Types

`attribute_type_mask` sets bit `n` for each value `n` in the sheet's
`AttributeType` list: `0` is bit 0 (the mask is `1` on 20,158 rows of client
3474), Garmoth's `42` is bit 42. The 2016 client names the field
`_attributeType` (`gc::CharacterAttributeType`); its value names are not
mapped here.

## Contents Groups

`contents_group_hashes` holds one u32 per key in the sheet's
`ContentsGroupKey` list. Each is the client's string hash
(`_common/string_hash.py` `key_hash`, lookup3 over the UTF-16LE text with seed
`0xC5EDE`) of the key written in decimal: key `0` is `0x6016CFF7`, key `6` is
`0x991157A2`. All 349 keys on client 1784 hash to the value the file stores,
and on client 3474 all 558 distinct hashes are keys from `0` to `8122`. A
character with no group stores the hash of `0` alone (8,707 rows of client
3474), so `contents_group_count` is never `0`. The browser turns the hashes
back into keys by hashing every key up to `65535`.

## Model Path

Every record holds one model path, a str8 of lower-case ASCII such as `[i64 25] npc/pedu2/npc_pedu2_named`. It is the sheet's `ActionScript FilePrefix` and `ActionScript File0` joined by `_` (see [Field Names](#field-names)), the 2016 client's `_actionScriptFileName`, so it names the character's action chart. Top-level folders on client 3464: `monster` (13,655), `npc` (5,078), `creature` (2,109), `object` (1,359), `riding` (793), `cash` (473). No record holds a second path on client 3474.

`model_path_hash` is `hashlittle` over the model path's ASCII bytes with seed `0xC5EDE` on all 24,553 rows of client 3474. In the 2016 struct `_actionPackageHashKey` follows `_actionScriptFileName`.

The strings after Character Fields come in a fixed order on every record: `ai_script`, `model_path`, the three Korean strings, `voice_bank`. Example rows on client 3474:

| Character | `ai_script` | `model_path` | `voice_bank` |
| --------- | ----------- | ------------ | ------------ |
| `47791` Ehren | `9999` | `npc/pedu2/npc_pedu2_named` | empty |
| `47343` | `NPC_Social_MorningLand` | `npc/npc_named_morningland_stand` | `NPC_VCE_47343` |
| `1` Warrior | `PC` | `pc/1_phm/fighteraction_noweapon` | `PC_VCE_1Warrior` |

## AI Script

`ai_script` is the stem of the character's [`.ai` script](aiscript_ai.md)
without its folder or extension: `9999` for `character/aiscript/9999.ai`,
`Party_Leader_Dragon_Boss` for `29929` Garmoth. Every record on client 3474
names one; the 47 player characters among them name `PC`
(`character/aiscript/pc.ai`). An earlier parser found the strings by a scan
that skipped strings under 3 characters and so reported no script for them.

On client 3464 the names compare with the file stems without case. Of the 5,895 distinct
names, 5,621 match one of the 7,037 distinct stems of the 7,070 `.ai` files;
327 records name one of 274 scripts the client does not ship
(`Hadum_M0519_Demonland_Gimmick`). The most common names are `9999` (8,282
records on client 3474) and `9999_Bow` (1,893).

The app groups these names into the `CHARACTER_AI_SCRIPT` lookup index
(`build_character_ai_script_index`), which the `.ai` view reads for its Used by
box.

## Korean Strings

Three UTF-16 strings follow the model path on all 24,551 records (client
3464), each an i64 code-unit count plus UTF-16LE text like the scripts:

| Field      | Notes |
| ---------- | ----- |
| name_kr    | Korean name (`DisplayName`), never empty: `29929` `가모스` (Garmoth), `1` `워리어` (Warrior). 335 records on client 3474 store the placeholder `UNKNOWN` instead, among them the War of the Roses buildings and the butler copies of the classes (`39840` to `39880`) |
| label_kr   | Longer Korean label with region and role (`CharName`): `47791` `에다니아2_아우리스 해안_거점관리인_idx53`, `29929` `Dri_드리간 월드 레이드 보스 소환용`; never empty |
| title_kr   | Korean title (`CharacterTitle`): `47791` `<거점 관리인>` (Node Manager). Non-empty on 6,242 rows, 6,168 of them in angle brackets |

The LOC type 6 `str_id4=1` title is the translation of `title_kr`
(`<Node Manager>` for `<거점 관리인>`): 6,178 records have both, 64 have only
the Korean one and 3 only the LOC one. The parser reads all three: the Name
column shows the Korean name when LOC has no name for the character, the Title
column `title_kr` when LOC has no title (`47481` `<여관 관리인>`, an unnamed
inn keeper), and the Internal Label column `label_kr` as stored. The Korean
name is `name_kr`, or `label_kr` where `name_kr` is `UNKNOWN` (`12688`
`[장미 전쟁] 화염탑`, `47481` `카르아쉬 협곡 여관 관리인 idx206`);
`korean_name()` in the parser picks it.

The same Korean name is the `CHARACTER_NAME_KR` lookup index
(`build_character_name_kr_index`), the fallback of `character_name()` in
`_common/character.py`, so every table that names a character key shows it
where LOC type 6 has no name: 296 of the 24,553 characters on client 3474
with the English LOC.

`title_kr` is the `CHARACTER_TITLE_KR` lookup index
(`build_character_title_kr_index`, empty titles left out), the fallback of
`character_title()`. On client 3474 with the English LOC it titles the 64
characters above that have only the Korean title, 50 of them `<메이드 통합>`.
No record stores `UNKNOWN` as its title; `korean_title()` drops it like the
name placeholder.

## Source Item

`source_item_id` is the reverse of the `itemenchant.dbss` `+0xAA` `character_id` link
(the `CHARACTER_ITEM` lookup index). On client 3464, 4,874 records store a
non-zero item, and on every one it is the item whose level-0 `itemenchant.dbss`
record names the character: `2053` [Event] Fence -> `58011` [Event] Fence,
`64527` Olvia Academy Pass - Fishing -> `619701`. `CHARACTER_ITEM` holds 5,108
links; the other 234 are mounts, wagons and ships (178 under `riding/horse`)
that store `0` here while a registration item names them: Horse Emblems (165),
Ship Licenses (23), Donkey Emblems (12), Wagon Registrations (11), e.g. `9967`
Horse from `50094` Horse Emblem: Tier 7-4 (Male).

So `CHARACTER_ITEM` gains nothing from `source_item_id` on client 3464: every
character that stores one already has that item in the index. The 4
characters the index leaves out because several items name them are horses
that store `0` here: `31533`, `31544`, `31590` and `31591`, named by 2 to 6
Horse Emblems each. The index stays on `itemenchant.dbss` alone, and
`test_source_item_matches_the_itemenchant_link` checks that the two agree.

The `Character_Table` sheet has no column for it.

## Script Values

`action_script` is the sheet's `ActiveCondition` and holds the interaction action:

| Pattern                 | Rows (client 3464) | Notes |
| ----------------------- | ------------------ | ----- |
| empty                   | `18733`  | Most records |
| `getknowledge(<id>);`   | `5684`   | Knowledge gained on interaction; one row (`50613`) spells it `getKnowledge(933);` |

The app groups these links into the `KNOWLEDGE_CHARACTERS` lookup index (`build_knowledge_character_index`), which the `mentalcard.dbss` Learned From column reads together with the `knowledgelearning.dbss` links. The `getknowledge` argument is a knowledge `entry_id`: 5,680 of the 5,684 arguments exist in `mentalcard.dbss` and 5,683 have a LOC `str_type=34` name, which matches the NPC name (e.g. `47791` "Ehren" -> `15936` "Ehren").

`condition_script` is the sheet's `InteractionCondition`. It is empty on 24,015 rows (client 3464). The other 403 hold semicolon-separated condition expressions, 98 of them alongside a `getknowledge` action. Most common calls: `progressQuest` (239, plus `ProgressQuest`/`progressquest` spellings), `CheckRideCharacter` (188), `getOceanTendency` (38), `getIntimacy` (28), `getLifelevel` (27), `clearQuest` (17). Example: `!CheckRideCharacter(29820);...;getIntimacy(47098)>-2500;`.

The sheet's `ActionScript` columns are the model path, not this script; the names `action_script` and `condition_script` are kept from earlier versions of this doc and match [quest.dbss](quest_dbss.md).

## `playercharacterstatic.bss`

`PABR` membership list of player-like character IDs: the live classes plus reserved, test, mercenary and alternate-mode characters. It is not an active-class list by itself.

| Offset               | Type       | Field         | Notes |
| -------------------- | ---------- | ------------- | ----- |
| `+0x00`              | char[4]    | magic         | ASCII `PABR` |
| `+0x04`              | u32        | count         | Observed `106` (bdo-data-extractor saw `96` on an older client, which matches the 96 non-`101` `class_type` rows in the older fixture) |
| `+0x08`              | u16[count] | character_ids | `count` character IDs |
| `character_ids+0x00` | u32        | string_count  | `0`: an empty PABR string table |
| `character_ids+0x04` | u32        | rows_end      | `220` = `8 + count * 2` |
| `character_ids+0x08` | u32        | zero          | `0` |

Every member has a `characterstatic.dbss` record with `class_type` other than `101`, and no other record does. The members are `1`-`47`, `201`-`214`, the mercenaries `521`, `523`-`528` and `536`, and the unnamed `39831`-`39867`, whose `class_type` values run `0`-`36`.

## Notes

- Record counts: `24017` in an older fixture, `24418` and `24551` on later clients (24,551 on client 3464), `24553` on client 3474, `16485` on client 1784.
- Offset rows are sorted by descending character ID in early data but should be treated as an index, not as a sorted table guarantee.
- `character_id` values are unique u16s; the highest observed is `65302`.
- LOC lookup confirms sample IDs: `47759` is "Yamarko", `16640` is "Dev Plant210", and `62223` is "Wandering Merchant".
- A character ID can be reused for a different character: in the older fixture `47759` was "Edania Merchant" (`getknowledge(14469);`, model `npc/pedu/npc_pedu_named`), and it heads the offset table there; in the 2026-09-27 client `47791` "Ehren" heads it.
- `characterstaticoffset.dbss` uses the same `PABR` 10-byte row pattern as `characterspawntypeoffset.dbss`, but its `data_offset` points after an inline u16 ID.
- The 2016 client fills `gc::CharacterStaticStatus` from the sheet (`CharacterStaticStatus::set`) and has no reader for this file, so its member order does not give the byte order here. The record is a packed serialization, not the 5,944-byte struct.
- Earlier versions of this doc read `p+5` as a u32 `npc_kind` with flag bits above the kind; the "flags" are `grade` and the low half of `tendency_on_dead`. Reading `p+1` as a u32 `character_id` (as bdo-data-extractor does) fails where `character_group` is non-zero.
- Soul collectors (Marni's Stones, `ContentsEventType` `59`) count kills by
  `character_group` too. The Where Used panel
  (`panel_whereuseitemdirection.luac`) calls the stone's
  `_contentsEventParam1` its `monsterGroupKey`; that is
  `contents_event_param1` of [`itemenchant.dbss`](itemenchant_dbss.md#soul-collectors).
  On client 3474 the 105 stones store 38 values from `60` to `186`, each a
  `character_group` whose members are the monsters the stone names (`70`
  Bashim, `107` Protty Cave, `185` the Everfrost animals of Rumbling Marni's
  Stone (Square)). None is a [`monstergroup.dbss`](monstergroup_dbss.md) key
  (`1` to `36`).
- Earlier names: `unknown_00` is the eight flags at `+0x00`, `tag` is `unknown_08`, `unknown_p` is `is_developing_contents`, `unknown_p3` is `character_group`, `unknown_p15` and `unknown_p167` are Character Fields `+0x0F` to `+0x11E` and the strings, `unknown_t23` is `repair_resources`, `unknown_t7` is `unknown_contents_group_hashes_11`, `unknown_tail_f32` is `reset_distance` and `unknown_t1` is `unknown_contents_group_hashes_17`.

## Open Questions

### What do the remaining flag bytes hold?

Character Fields `+0x9F` to `+0xC2` and the tail bytes `unknown_voice_bank_07`, `unknown_holdable_item_keys_08`, `unknown_contents_group_hashes_11` and `_17` match no `Character_Table` column. Most split by `npc_kind` (`unknown_be` is `1` on exactly the player characters; `unknown_a1`, `unknown_a5`, `unknown_bd` and `unknown_c1` are set only on kind `3`), which points to values the compiler derives from other tables, such as `Servant_Table` for mounts. `unknown_b5` (`1` on 5,725 rows, mostly NPCs) is `1` exactly where the sheet's `TalkAble` is non-zero (15,704 of 15,704 client 1784 rows of `charactersimply.bss`, 16,051 of 16,058 on client 3474), but `TalkAble` holds a talk type (`1` to `3`), so the byte stays unnamed.

### What is `unknown_c7`?

The 8 bytes client 3464 added after `level`. The first two vary on 2,630 rows and the third holds `1` to `5` on 210; no sheet of client 1784 can name a field that did not exist yet.

### What is `unknown_11b`?

A u32 next to `model_path_hash`, non-zero on exactly the 61 player characters and different per character (`201` holds `0xA33C0084`). It is not the hash of `model_path`, `ai_script`, `voice_bank` or the Korean strings with seed `0xC5EDE`.

### Related BSS Files

`hardcorerandomspawncharacterstaticstatusmanager.bss` and `fuelinsertcharacterstaticstatus.bss` are related by name, but they are not required to parse `characterstatic.dbss`. Their layouts should be documented separately if needed.
