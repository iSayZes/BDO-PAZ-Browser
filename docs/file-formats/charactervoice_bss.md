# `charactervoice.bss` Format

## Purpose

The voices a player character can pick in character customization: per
character key, one list of voice names for each of two appearance types
and a voice count for each. The names (`PC_VCE_1Warrior_1`,
`PC_VCE_MN_T01_JP_Warrior_1`) sit in the PABR string table and the rows
point at them by index. On client 3482 the file holds 76 characters and 64
voice names (45 and 55 on client 1784); only Wizard (`29`) and `39859`
fill the second list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                 | Bytes  | Records                | Row bytes                |
| ------ | ------------- | ------- | -------------------- | ------ | ---------------------- | ------------------------ |
| 2      | 805 and later | 3483    | `charactervoice.bss` | 4,801  | 152 Voice List, 76 Row | 4 to 60, 16 on average   |
| 1      | 435 to 794    | 794     | `charactervoice.bss` | 10,952 | 36 Voice List, 18 Row  | 4 to 604, 299 on average |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 2      | `charactervoice.bss` | 4,801 B (100.0%)  | 0 B (0.0%) |
| 1      | `charactervoice.bss` | 10,952 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
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
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 2 |
| 1690   | Layout 2 |
| 1685   | Layout 2 |
| 1680   | Layout 2 |
| 1674   | Layout 2 |
| 1668   | Layout 2 |
| 1659   | Layout 2 |
| 1649   | Layout 2 |
| 1642   | Layout 2 |
| 1636   | Layout 2 |
| 1628   | Layout 2 |
| 1622   | Layout 2 |
| 1614   | Layout 2 |
| 1608   | Layout 2 |
| 1602   | Layout 2 |
| 1598   | Layout 2 |
| 1594   | Layout 2 |
| 1590   | Layout 2 |
| 1587   | Layout 2 |
| 1584   | Layout 2 |
| 1579   | Layout 2 |
| 1572   | Layout 2 |
| 1565   | Layout 2 |
| 1559   | Layout 2 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 2 |
| 1340   | Layout 2 |
| 1338   | Layout 2 |
| 1335   | Layout 2 |
| 1333   | Layout 2 |
| 1329   | Layout 2 |
| 1327   | Layout 2 |
| 1324   | Layout 2 |
| 1321   | Layout 2 |
| 1319   | Layout 2 |
| 1318   | Layout 2 |
| 1316   | Layout 2 |
| 1313   | Layout 2 |
| 1311   | Layout 2 |
| 1309   | Layout 2 |
| 1304   | Layout 2 |
| 1292   | Layout 2 |
| 1286   | Layout 2 |
| 1280   | Layout 2 |
| 1276   | Layout 2 |
| 1267   | Layout 2 |
| 1261   | Layout 2 |
| 1256   | Layout 2 |
| 1250   | Layout 2 |
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
| 1144   | Layout 2 |
| 1137   | Layout 2 |
| 1132   | Layout 2 |
| 1127   | Layout 2 |
| 1122   | Layout 2 |
| 1118   | Layout 2 |
| 1114   | Layout 2 |
| 1109   | Layout 2 |
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
| 829    | Layout 2 |
| 822    | Layout 2 |
| 814    | Layout 2 |
| 805    | Layout 2 |
| 794    | Layout 1 |
| 787    | Layout 1 |
| 780    | Layout 1 |
| 771    | Layout 1 |
| 760    | Layout 1 |
| 748    | Layout 1 |
| 741    | Layout 1 |
| 736    | Layout 1 |
| 731    | Layout 1 |
| 723    | Layout 1 |
| 711    | Layout 1 |
| 707    | Layout 1 |
| 697    | Layout 1 |
| 689    | Layout 1 |
| 683    | Layout 1 |
| 678    | Layout 1 |
| 670    | Layout 1 |
| 661    | Layout 1 |
| 656    | Layout 1 |
| 652    | Layout 1 |
| 643    | Layout 1 |
| 637    | Layout 1 |
| 630    | Layout 1 |
| 627    | Layout 1 |
| 621    | Layout 1 |
| 617    | Layout 1 |
| 615    | Layout 1 |
| 606    | Layout 1 |
| 599    | Layout 1 |
| 592    | Layout 1 |
| 586    | Layout 1 |
| 577    | Layout 1 |
| 569    | Layout 1 |
| 561    | Layout 1 |
| 554    | Layout 1 |
| 542    | Layout 1 |
| 532    | Layout 1 |
| 531    | Layout 1 |
| 526    | Layout 1 |
| 521    | Layout 1 |
| 517    | Layout 1 |
| 510    | Layout 1 |
| 508    | Layout 1 |
| 504    | Layout 1 |
| 497    | Layout 1 |
| 491    | Layout 1 |
| 485    | Layout 1 |
| 478    | Layout 1 |
| 472    | Layout 1 |
| 466    | Layout 1 |
| 457    | Layout 1 |
| 452    | Layout 1 |
| 449    | Layout 1 |
| 435    | Layout 1 |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Character names, LOC type 6                                                 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                  |
| ------------------- | ----------------- | ------------------ | -------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                           |
| `+0x04`             | u32               | record_count       | Number of rows                         |
| `+0x08`             | Row[record_count] | records            | See Row                                |
| `records+0x00`      | String Table      | string_table       | The voice names                        |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`      |
| `string_table+0x04` | u32               | zero               | `0`                                    |

### Row (variable: 10 bytes + voice lists)

| Offset         | Type          | Field         | Notes                                                                        |
| -------------- | ------------- | ------------- | ---------------------------------------------------------------------------- |
| `+0x00`        | u16           | character_key | Row key: a `characterstatic.dbss` character; each key once                   |
| `+0x02`        | Voice List[2] | voices        | Appearance type 0, then appearance type 1; see Voice List                    |
| `voices+0x00`  | u32[2]        | voice_count   | Voice count of appearance type 0, then 1; see Notes                          |

The rows are in no key order; client 3482 opens with 1, 2, 3, 4, 6, 5.

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                  | Field            | Notes                                         |
| ------- | --------------------- | ---------------- | --------------------------------------------- |
| `+0x00` | u32                   | voice_type_count | Number of `voice_types`; `0` for an unused appearance type |
| `+0x04` | u32[voice_type_count] | voice_types      | Index into `strings`, in the sheet's `VoiceType1` to `VoiceType20` order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                      |
| ------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00` | u32                | string_count | 64 on client 3482                                          |
| `+0x04` | pstr[string_count] | strings      | Voice names, UTF-8 (`is_wide` `0`); every string has an index pointing at it (clients 1784 and 3482) |

## Layout 1

No PABR magic and no string table: the file opens with the row count and
each list holds the voice names inline. The Row is the same as in Layout 2.

### File Layout

| Offset  | Type              | Field        | Notes          |
| ------- | ----------------- | ------------ | -------------- |
| `+0x00` | u32               | record_count | Number of rows |
| `+0x04` | Row[record_count] | records      | See Row        |

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                   | Field            | Notes                                          |
| ------- | ---------------------- | ---------------- | ---------------------------------------------- |
| `+0x00` | u32                    | voice_type_count | Number of `voice_types`                        |
| `+0x04` | str8[voice_type_count] | voice_types      | Voice names inline (`PC_VCE_1Warrior_1`)        |

Client 794 stores the file as `gamecommondata/binary/en/charactervoice.bss`
with 18 rows: 7 lists hold 17 names with a `voice_count` of 8 and 11 hold
19 names with a count of 12.

## Field Names

The `CharacterVoice_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `CharName`,
`AppearanceType`, `VoiceCount` and `VoiceType1` to `VoiceType20`, one row
per character and appearance type: 46 rows, 45 of type `0` and one of type
`1` (character `29`). Each row matches one list of the client file.

| Field         | Column                         | Same value (client 1784) | Same value (client 3482) |
| ------------- | ------------------------------ | ------------------------ | ------------------------ |
| character_key | `CharacterKey`                 | 45 of 45                 | 25 of 45                 |
| voice_types   | `VoiceType1` to `VoiceType20`  | 46 of 46 lists           | 24 of 26 lists           |
| voice_count   | `VoiceCount`                   | 46 of 46                 | 25 of 26                 |

`AppearanceType` picks the list (`voices` entry `0` or `1`); `CharName` is
a note (`PC-워리어`) the client file does not hold. On client 3482 the 20
sheet keys `65001` to `65020` are gone; the file lists 33 keys from
`39831` to `39866` in their place. Character `8` (Wukong) holds one voice where the sheet has
`PC_VCE_6Blader_1`, and character `10` (Scholar) one where the sheet lists
eight.

## Notes

- `voice_count` equals the list length on 73 of 76 rows (client 3482). The
  three others (`30` Archer, `39860` and `39863`) list 8, 8 and 1 voices
  with a count of `2`; client 1784 has the same for `30`.
- The client Lua (`panel_customization_voice_renew.luac`, client 3482)
  fills the voice list from `getClassVoiceCount()` and picks a voice with
  `applyVoice(index, ...)`; no Lua call names a field of this table.
- The 33 keys from `39831` to `39866` (client 3482) are named
  `집사 PC-<class>` in `characterstatic.dbss`, with no LOC name; `39859` is
  `집사 PC-위자드`.
