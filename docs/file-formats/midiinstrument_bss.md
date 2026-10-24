# `midiinstrument.bss` Format

## Purpose

The instruments of the music composer and the instrument play: per
instrument its Wwise bank and event, the in-game name key, the
articulations it can play, the start, end and loop actions of the playing
character, the composer tab it sits on and whether every player owns it.
The composer Lua (`panel_window_selectinstruments_all_1.luac`,
`panel_window_myinstruments_all_1.luac`) reads it through
`Toclient_MidiInstrumentTrackCount()`, `Toclient_getInstrumentByIndex()`,
`ToClient_getAdvancedTypeByIndex()` and
`ToClient_getInstrumentIsOpenedByIndex()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | ----------------------- |
| 4      | 1846 and later | 3483    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 3      | 1547 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 2      | 1504 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 1      | 1409 to 1838   | 1838    | `midiinstrument.bss` | 1,833 | 15 Row  | 53 to 61, 55 on average |

| Layout | File                 | Known            | Unknown      |
| ------ | -------------------- | ---------------- | ------------ |
| 4      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 3      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 2      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 1      | `midiinstrument.bss` | 1,833 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 4             |
| 3482   | Layout 4             |
| 3474   | Layout 4             |
| 3473   | Layout 4             |
| 3464   | Layout 4             |
| 3458   | Layout 4             |
| 3454   | Layout 4             |
| 3444   | Layout 4             |
| 3435   | Layout 4             |
| 3426   | Layout 4             |
| 3418   | Layout 4             |
| 3412   | Layout 4             |
| 3402   | Layout 4             |
| 3396   | Layout 4             |
| 3387   | Layout 4             |
| 3381   | Layout 4             |
| 3373   | Layout 4             |
| 3364   | Layout 4             |
| 3356   | Layout 4             |
| 3349   | Layout 4             |
| 3342   | Layout 4             |
| 3335   | Layout 4             |
| 3326   | Layout 4             |
| 3321   | Layout 4             |
| 3314   | Layout 4             |
| 3303   | Layout 4             |
| 3302   | Layout 4             |
| 3293   | Layout 4             |
| 3283   | Layout 4             |
| 3275   | Layout 4             |
| 3267   | Layout 4             |
| 3258   | Layout 4             |
| 3251   | Layout 4             |
| 3242   | Layout 4             |
| 3235   | Layout 4             |
| 3229   | Layout 4             |
| 3212   | Layout 4             |
| 3203   | Layout 4             |
| 3193   | Layout 4             |
| 3186   | Layout 4             |
| 3177   | Layout 4             |
| 3169   | Layout 4             |
| 3158   | Layout 4             |
| 3151   | Layout 4             |
| 3144   | Layout 4             |
| 3133   | Layout 4             |
| 3125   | Layout 4             |
| 3118   | Layout 4             |
| 3111   | Layout 4             |
| 3103   | Layout 4             |
| 3095   | Layout 4             |
| 3086   | Layout 4             |
| 3072   | Layout 4             |
| 3062   | Layout 4             |
| 3052   | Layout 4             |
| 3045   | Layout 4             |
| 3037   | Layout 4             |
| 3030   | Layout 4             |
| 3021   | Layout 4             |
| 3012   | Layout 4             |
| 3002   | Layout 4             |
| 2995   | Layout 4             |
| 2987   | Layout 4             |
| 2978   | Layout 4             |
| 2970   | Layout 4             |
| 2959   | Layout 4             |
| 2951   | Layout 4             |
| 2942   | Layout 4             |
| 2935   | Layout 4             |
| 2932   | Layout 4             |
| 2923   | Layout 4             |
| 2919   | Layout 4             |
| 2907   | Layout 4             |
| 2900   | Layout 4             |
| 2891   | Layout 4             |
| 2882   | Layout 4             |
| 2872   | Layout 4             |
| 2863   | Layout 4             |
| 2855   | Layout 4             |
| 2849   | Layout 4             |
| 2844   | Layout 4             |
| 2834   | Layout 4             |
| 2825   | Layout 4             |
| 2819   | Layout 4             |
| 2811   | Layout 4             |
| 2803   | Layout 4             |
| 2794   | Layout 4             |
| 2783   | Layout 4             |
| 2774   | Layout 4             |
| 2765   | Layout 4             |
| 2756   | Layout 4             |
| 2750   | Layout 4             |
| 2743   | Layout 4             |
| 2736   | Layout 4             |
| 2726   | Layout 4             |
| 2717   | Layout 4             |
| 2709   | Layout 4             |
| 2703   | Layout 4             |
| 2695   | Layout 4             |
| 2684   | Layout 4             |
| 2672   | Layout 4             |
| 2665   | Layout 4             |
| 2657   | Layout 4             |
| 2649   | Layout 4             |
| 2644   | Layout 4             |
| 2637   | Layout 4             |
| 2629   | Layout 4             |
| 2619   | Layout 4             |
| 2612   | Layout 4             |
| 2606   | Layout 4             |
| 2602   | Layout 4             |
| 2601   | Layout 4             |
| 2592   | Layout 4             |
| 2583   | Layout 4             |
| 2575   | Layout 4             |
| 2567   | Layout 4             |
| 2560   | Layout 4             |
| 2553   | Layout 4             |
| 2545   | Layout 4             |
| 2538   | Layout 4             |
| 2529   | Layout 4             |
| 2519   | Layout 4             |
| 2513   | Layout 4             |
| 2510   | Layout 4             |
| 2507   | Layout 4             |
| 2503   | Layout 4             |
| 2498   | Layout 4             |
| 2492   | Layout 4             |
| 2487   | Layout 4             |
| 2480   | Layout 4             |
| 2474   | Layout 4             |
| 2468   | Layout 4             |
| 2460   | Layout 4             |
| 2453   | Layout 4             |
| 2444   | Layout 4             |
| 2438   | Layout 4             |
| 2434   | Layout 4             |
| 2429   | Layout 4             |
| 2421   | Layout 4             |
| 2414   | Layout 4             |
| 2407   | Layout 4             |
| 2401   | Layout 4             |
| 2397   | Layout 4             |
| 2393   | Layout 4             |
| 2384   | Layout 4             |
| 2378   | Layout 4             |
| 2372   | Layout 4             |
| 2358   | Layout 4             |
| 2352   | Layout 4             |
| 2347   | Layout 4             |
| 2343   | Layout 4             |
| 2335   | Layout 4             |
| 2327   | Layout 4             |
| 2324   | Layout 4             |
| 2319   | Layout 4             |
| 2313   | Layout 4             |
| 2308   | Layout 4             |
| 2302   | Layout 4             |
| 2295   | Layout 4             |
| 2290   | Layout 4             |
| 2284   | Layout 4             |
| 2276   | Layout 4             |
| 2269   | Layout 4             |
| 2259   | Layout 4             |
| 2250   | Layout 4             |
| 2243   | Layout 4             |
| 2235   | Layout 4             |
| 2229   | Layout 4             |
| 2224   | Layout 4             |
| 2218   | Layout 4             |
| 2215   | Layout 4             |
| 2207   | Layout 4             |
| 2203   | Layout 4             |
| 2196   | Layout 4             |
| 2192   | Layout 4             |
| 2189   | Layout 4             |
| 2183   | Layout 4             |
| 2179   | Layout 4             |
| 2171   | Layout 4             |
| 2163   | Layout 4             |
| 2156   | Layout 4             |
| 2151   | Layout 4             |
| 2147   | Layout 4             |
| 2142   | Layout 4             |
| 2138   | Layout 4             |
| 2134   | Layout 4             |
| 2130   | Layout 4             |
| 2122   | Layout 4             |
| 2107   | Layout 4             |
| 2098   | Layout 4             |
| 2089   | Layout 4             |
| 2081   | Layout 4             |
| 2073   | Layout 4             |
| 2067   | Layout 4             |
| 2063   | Layout 4             |
| 2059   | Layout 4             |
| 2052   | Layout 4             |
| 2044   | Layout 4             |
| 2039   | Layout 4             |
| 2032   | Layout 4             |
| 2025   | Layout 4             |
| 2011   | Layout 4             |
| 2005   | Layout 4             |
| 2000   | Layout 4             |
| 1996   | Layout 4             |
| 1991   | Layout 4             |
| 1985   | Layout 4             |
| 1980   | Layout 4             |
| 1969   | Layout 4             |
| 1964   | Layout 4             |
| 1958   | Layout 4             |
| 1950   | Layout 4             |
| 1945   | Layout 4             |
| 1937   | Layout 4             |
| 1933   | Layout 4             |
| 1927   | Layout 4             |
| 1921   | Layout 4             |
| 1914   | Layout 4             |
| 1908   | Layout 4             |
| 1897   | Layout 4             |
| 1892   | Layout 4             |
| 1886   | Layout 4             |
| 1881   | Layout 4             |
| 1871   | Layout 4             |
| 1866   | Layout 4             |
| 1862   | Layout 4             |
| 1854   | Layout 4             |
| 1846   | Layout 4             |
| 1838   | Layout 3             |
| 1832   | Layout 3             |
| 1826   | Layout 3             |
| 1822   | Layout 3             |
| 1818   | Layout 3             |
| 1804   | Layout 3             |
| 1794   | Layout 3             |
| 1790   | Layout 3             |
| 1784   | Layout 3             |
| 1774   | Layout 3             |
| 1771   | Layout 3             |
| 1762   | Layout 3             |
| 1759   | Layout 3             |
| 1754   | Layout 3             |
| 1749   | Layout 3             |
| 1743   | Layout 3             |
| 1737   | Layout 3             |
| 1731   | Layout 3             |
| 1725   | Layout 3             |
| 1717   | Layout 3             |
| 1710   | Layout 3             |
| 1704   | Layout 3             |
| 1698   | Layout 3             |
| 1690   | Layout 3             |
| 1685   | Layout 3             |
| 1680   | Layout 3             |
| 1674   | Layout 3             |
| 1668   | Layout 3             |
| 1659   | Layout 3             |
| 1649   | Layout 3             |
| 1642   | Layout 3             |
| 1636   | Layout 3             |
| 1628   | Layout 3             |
| 1622   | Layout 3             |
| 1614   | Layout 3             |
| 1608   | Layout 3             |
| 1602   | Layout 3             |
| 1598   | Layout 3             |
| 1594   | Layout 3             |
| 1590   | Layout 3             |
| 1587   | Layout 3             |
| 1584   | Layout 3             |
| 1579   | Layout 3             |
| 1572   | Layout 3             |
| 1565   | Layout 3             |
| 1559   | Layout 3             |
| 1554   | Layout 3             |
| 1547   | Layout 3             |
| 1537   | Layout 2             |
| 1529   | Layout 2             |
| 1524   | Layout 2             |
| 1519   | Layout 2             |
| 1509   | Layout 2             |
| 1506   | Layout 2             |
| 1504   | Layout 2             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
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

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset                       | Type                     | Field              | Notes                                         |
| ---------------------------- | ------------------------ | ------------------ | --------------------------------------------- |
| `+0x00`                      | char[4]                  | magic              | ASCII `PABR`                                  |
| `+0x04`                      | u32                      | row_count          | Number of instruments                         |
| `+0x08`                      | Row[row_count]           | rows               | See Row                                       |
| `rows+0x00`                  | u32                      | action_hash_count  | Number of `action_hashes`                     |
| `rows+0x04`                  | u32[action_hash_count]   | action_hashes      | Every distinct start and loop action hash of the rows, each once; see Notes |
| `action_hashes+0x00`         | String Table             | string_table       | See String Table                              |
| `string_table+0x00`          | u32                      | string_table_start | Offset of the string table, where `action_hashes` ends |
| `string_table+0x04`          | u32                      | zero               | `0`                                           |

### Row (variable: 43 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                        | Notes                                                                                       |
| -------------------------- | ------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| `+0x00`                    | u8                       | index                        | Row key, `0` to `40` with gaps on client 3482; the number in `bank_name` for `0` to `19`    |
| `+0x01`                    | u32                      | bank_name                    | Index into `strings`: the Wwise bank (`MIDI_Instrument_00_AcousticGuitar`)                  |
| `+0x05`                    | u32                      | event_name                   | Index into `strings`: the Wwise event; the same string as `bank_name` on every row          |
| `+0x09`                    | u32                      | ingame_name                  | Index into `strings`: the name key (`AcousticGuitar`, `Advanced_Piano`)                     |
| `+0x0D`                    | u64                      | articulation_count           | Number of `articulations`                                                                   |
| `+0x15`                    | u8[articulation_count]   | articulations                | Articulation numbers; `99` alone for an instrument with one way to play                     |
| `articulations+0x00`       | u32                      | start_action_hash            | `ascii_key_hash` of the start action name (`SHY_MusicStart_Guitar` on client 1784)          |
| `articulations+0x04`       | u32                      | end_action_hash              | `ascii_key_hash` of the end action name                                                     |
| `articulations+0x08`       | u8                       | advanced_type                | Composer tab; see Advanced Type                                                             |
| `articulations+0x09`       | u32                      | instrument_name_type         | Index into `strings`: the tab name key (`AUDIO_MIDI_TAB_NOVICE`), UTF-16LE                  |
| `articulations+0x0D`       | u8                       | is_opened                    | `1` on every row                                                                            |
| `articulations+0x0E`       | u32                      | ing_action_count             | Number of `ing_action_hashes`; `3` on every row                                             |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes            | `ascii_key_hash` of the loop action names (`SHY_MusicIng_Guitar` to `SHY_MusicIng3_Guitar`) |
| `ing_action_hashes+0x00`   | u8                       | is_provided                  | `1` for the instruments every character owns (Acoustic Guitar, Flute, Hand Drum on client 1784) |
| `ing_action_hashes+0x01`   | u8                       | unknown_ing_action_hashes_01 | `0` to `3`; see Open Questions                                                              |
| `ing_action_hashes+0x02`   | u8                       | unknown_ing_action_hashes_02 | The bank number in `bank_name` (`24` for `MIDI_Instrument_24_ProGuitarElectricClean`); `20` to `23` for the sine, triangle, square and saw synths |
| `ing_action_hashes+0x03`   | u8                       | unknown_ing_action_hashes_03 | `0` to `3` for the synth variants Basic, Stereo, Super and SuperOct; `0` on every other row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | Bank, name and tab keys; a string several rows use is stored once; the tab keys are UTF-16LE (`is_wide` `1`), the rest UTF-8 |

## Layout 3

The row ends with `is_provided`: the three bytes after it do not exist yet.
Only the Row differs from Layout 4.

### Row (variable: 40 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `19` with gaps on client 1784            |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u8                       | is_opened            | `1` on every row                                         |
| `articulations+0x0E`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 2

No `is_opened` byte after `instrument_name_type`, and the row ends with
`is_provided` as in Layout 3. Only the Row differs from Layout 3.

### Row (variable: 39 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `8` with gaps on client 1537             |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x11`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 1

No composer tab: the row has no `advanced_type`, `instrument_name_type` or
`is_opened`, and the loop actions follow the end action. Only the Row
differs from Layout 2.

### Row (variable: 34 bytes + articulations and loop actions)

| Offset                     | Type                     | Field              | Notes                                                    |
| -------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index              | Row key, `0` to `8` with gaps on client 1485             |
| `+0x01`                    | u32                      | bank_name          | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name         | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name        | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations      | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash  | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash    | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u32                      | ing_action_count   | Number of `ing_action_hashes`                            |
| `articulations+0x0C`       | u32[ing_action_count]    | ing_action_hashes  | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided        | `1` for the instruments every character owns             |

## Advanced Type

| Value | Tab key (`instrument_name_type`)        | Instruments on client 3482                                  |
| ----- | --------------------------------------- | ----------------------------------------------------------- |
| 0     | `AUDIO_MIDI_TAB_NOVICE`                 | Acoustic Guitar to Violin, the beginner instruments          |
| 1     | `AUDIO_MIDI_TAB_ADVANCED`               | The Marnian instruments (`Advanced_*`) without the electric ones |
| 2     | `AUDIO_MIDI_TAB_ADVANCED_ELECTRONIC`    | Electric bass and guitars, the 16 synths                     |

The composer Lua names `__eInstrumentAdvancedType_Novice`,
`__eInstrumentAdvancedType_Advanced`, `__eeInstrumentAdvancedType_Synth`
(sic) and `__eInstrumentAdvancedType_Count`.

## Field Names

The `MidiInstrument_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Index`, `BankName`, `EventName`,
`ArticulationList`, `IngameName`, `IsOpened`, `ContentsGroupKey`,
`StartAction`, `EndAction`, `IsProvided`, `IngAction`, `SoundEffector`,
`AdvancedType`, `InstrumentNameType` and `InstrumentName`, 20 rows. The
client file holds the 15 rows with `IsOpened` `1`; the five with `0` are
not compiled. On those 15 rows every named field matches its column (15 of
15, client 1784); the action hashes are `ascii_key_hash` of the
`StartAction`, `EndAction` and `IngAction` names. `SoundEffector` holds the
same values as `AdvancedType` on all 20 rows; the field is named after
`AdvancedType`, which sits before `InstrumentNameType` in the sheet as the
field does in the row, and the electronic tab rows of client 3482 hold `2`
there. `ContentsGroupKey` and `InstrumentName`
(`AUDIO_MIDI_INSTRUMENT_0`) are not in the client file.

## Notes

- On client 3482 the start, end and loop action hashes match none of the
  client 1784 action names: the actions were renamed. Rows that share an
  instrument model (Acoustic Guitar and Marnian Acoustic Guitar, the four
  variants of one synth) share their hashes.
- `action_hashes` lists every distinct `start_action_hash` and
  `ing_action_hash` of the rows, each once and in no sorted order; no
  `end_action_hash` is in it (clients 1784 and 3482).

## Open Questions

### Instrument Family Byte

`unknown_ing_action_hashes_01` groups the instruments on client 3482: `0`
piano and the synths, `1` flute, recorder, clarinet and horn, `2` the
string instruments (guitars, harp, violin, basses), `3` the drums, cymbals
and hand pan. No sheet column of client 1784 holds it; the composer may
pick the play animation or the score clef with it.

### Rows Before Client 1409

Clients 1256 to 1390 hold another row (client 1256: two instruments in
144 bytes) that breaks every layout at `articulation_count`. No layout
reads these files yet.
