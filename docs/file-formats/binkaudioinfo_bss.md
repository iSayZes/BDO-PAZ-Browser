# `binkaudioinfo.bss` Format

## Purpose

The sound of the Bink movies: per movie (`Goyen`,
`Balenos_Intro_EmmasDream`, the Morning Light cutscenes) the Wwise event
and sound bank that play its audio. The movie name is the stem of the
`.bk2` file under `ui_movie/`, the audio name a `Bink_<movie>` event and a
`bink_<movie>.bnk` bank under `sound2022/windows/<language>/`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------ | ------- | --------- |
| 1      | 2073 and later | 3482    | `binkaudioinfo.bss` | 11,349 | 161 Row | 15        |

| Layout | File                | Known            | Unknown      |
| ------ | ------------------- | ---------------- | ------------ |
| 1      | `binkaudioinfo.bss` | 10,866 B (95.7%) | 483 B (4.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of movies                              |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (15 bytes)

| Offset  | Type | Field          | Notes                                                                            |
| ------- | ---- | -------------- | -------------------------------------------------------------------------------- |
| `+0x00` | u32  | movie_name     | Index into `strings`: the movie (`Goyen` for `ui_movie/pc/cutscene/abyssstory/goyen/goyen.bk2`) |
| `+0x04` | u32  | audio_name     | Index into `strings`: the Wwise event and bank name (`Bink_Goyen`)               |
| `+0x08` | u32  | audio_name_dup | Equals `audio_name` on every row                                                 |
| `+0x0C` | u8   | unknown_0c     | `1` on every row of clients 2107 and 3482                                        |
| `+0x0D` | u8   | unknown_0d     | `1` on every row of clients 2107 and 3482                                        |
| `+0x0E` | u8   | unknown_0e     | `1` on every row of clients 2107 and 3482                                        |

The rows are in no name order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                            |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                |
| `+0x04` | pstr[string_count] | strings      | Movie and audio names, UTF-8, in row order: movie, then audio name |

## Field Names

No sheet of the client 1784 `DataSheets.bexcel` holds the file; client
2073 is the first test client that has it (client 2107: six movies). The names
follow the client files the strings point at (client 3482):

- `movie_name`: 159 of 161 are the stem of a `.bk2` file in the PAZ;
  `RoseWar_Kama_Ranger` and `MorningLand_TheEnd` are not.
- `audio_name`: 160 of 161 are both an event and a bank of
  `sound2022/wwise_ids.h`; `Bink_MorningLand_TheEnd` is neither. 154 have
  a `bink_<movie>.bnk` bank under `sound2022/windows/english(us)/`.

Which of `audio_name` and `audio_name_dup` is the event and which the bank
is not known: the two hold one string on every row.

## Open Questions

### Three Flags

`unknown_0c` to `unknown_0e` are `1` on every row. They may switch the
movie's audio per language or per sound channel; a row with a `0` would
tell.
