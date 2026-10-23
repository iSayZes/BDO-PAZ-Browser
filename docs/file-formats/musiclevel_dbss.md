# `musiclevel.dbss` Format

## Purpose

The music (instrument play) levels: per level the music EXP it takes, the
bar and note counts the composer allows at that level and the rank letter
the Music Board shows. The Music Board Lua (`panel_window_musicboard_all_1.luac`)
reads the player's state with `ToClient_GetMusicLevel()` and
`ToClient_GetMusicRank()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records          | Row bytes               |
| ------ | -------------- | ------- | ----------------------- | ----- | ---------------- | ----------------------- |
| 1      | 1348 and later | 3482    | `musiclevel.dbss`       | 572   | 16 Row, 16 Entry | 30 to 32, 31 on average |
| 1      | 1348 and later | 3482    | `musicleveloffset.dbss` | 196   | 16 Offset Row    | 12                      |

| Layout | File                    | Known          | Unknown    |
| ------ | ----------------------- | -------------- | ---------- |
| 1      | `musiclevel.dbss`       | 568 B (99.3%)  | 4 B (0.7%) |
| 1      | `musicleveloffset.dbss` | 196 B (100.0%) | 0 B (0.0%) |

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
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | Layout 1 |
| 1969   | Layout 1 |
| 1937   | Layout 1 |
| 1914   | Layout 1 |
| 1886   | Layout 1 |
| 1866   | Layout 1 |
| 1838   | Layout 1 |
| 1818   | Layout 1 |
| 1794   | Layout 1 |
| 1784   | Layout 1 |
| 1749   | Layout 1 |
| 1717   | Layout 1 |
| 1698   | Layout 1 |
| 1674   | Layout 1 |
| 1636   | Layout 1 |
| 1608   | Layout 1 |
| 1587   | Layout 1 |
| 1565   | Layout 1 |
| 1537   | Layout 1 |
| 1509   | Layout 1 |
| 1485   | Layout 1 |
| 1466   | Layout 1 |
| 1445   | Layout 1 |
| 1426   | Layout 1 |
| 1409   | Layout 1 |
| 1390   | Layout 1 |
| 1372   | Layout 1 |
| 1360   | Layout 1 |
| 1348   | Layout 1 |
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

| File                    | Required | Role                                                                                    |
| ----------------------- | -------- | --------------------------------------------------------------------------------------- |
| `musicleveloffset.dbss` | Optional | `music_level -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic. Two counts, then the entries back to back to the end of
the file.

| Offset  | Type         | Field      | Notes                                                              |
| ------- | ------------ | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32          | count      | Number of entries                                                  |
| `+0x04` | u32          | unknown_04 | Equals `count` and the highest `music_level` on clients 1784 and 3482 |
| `+0x08` | Entry[count] | entries    | See Entry                                                          |

### Entry (variable: 4 bytes + row)

| Offset  | Type | Field       | Notes                                                                      |
| ------- | ---- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32  | key_prefix  | Equals the row's `music_level`; the offset index points past it           |
| `+0x04` | Row  | row         | See Row                                                                    |

### Row (variable: 28 bytes + rank text)

| Offset  | Type  | Field                   | Notes                                                                 |
| ------- | ----- | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32   | music_level             | Row key, `1` to `16` in order on client 3482                          |
| `+0x04` | u64   | music_level_exp         | Music EXP of the level                                                |
| `+0x0C` | u32   | increasing_bar_number   | `30` at level 1 to `100` at level 6 (clients 1784 and 3482)           |
| `+0x10` | u32   | increasing_note_number  | `500` at level 1 to `1200` at level 6 (clients 1784 and 3482)         |
| `+0x14` | str16 | music_rank              | Rank letter (`F`, `D-`, `C`, `S+`)                                    |

### `musicleveloffset.dbss`

No `PABR` magic and no trailer: a count, then one row per level.

| Offset  | Type              | Field | Notes                       |
| ------- | ----------------- | ----- | --------------------------- |
| `+0x00` | u32               | count | Equals `musiclevel.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32  | music_level | Row key                                                      |
| `+0x04` | u32  | data_offset | Where the Row starts in `musiclevel.dbss`, past `key_prefix` |
| `+0x08` | u32  | data_size   | Length of the Row                                            |

## Levels

Client 3482 holds 16 levels, client 1784 the first six with the same
values:

| Level | EXP           | Bars | Notes | Rank |
| ----- | ------------- | ---- | ----- | ---- |
| 1     | 72            | 30   | 500   | F    |
| 2     | 108           | 34   | 555   | D-   |
| 3     | 162           | 42   | 665   | D    |
| 4     | 243           | 54   | 830   | D+   |
| 5     | 364           | 70   | 1050  | C-   |
| 6     | 546           | 100  | 1200  | C    |
| 7     | 546,750       | 101  | 1201  | C+   |
| 8     | 1,366,875     | 102  | 1202  | B-   |
| 9     | 3,417,187     | 103  | 1203  | B    |
| 10    | 8,542,968     | 104  | 1204  | B+   |
| 11    | 17,085,937    | 105  | 1205  | A-   |
| 12    | 34,171,875    | 106  | 1206  | A    |
| 13    | 68,343,750    | 107  | 1207  | A+   |
| 14    | 136,687,500   | 108  | 1208  | S-   |
| 15    | 273,375,000   | 109  | 1209  | S    |
| 16    | 546,750,000   | 110  | 1210  | S+   |

Level 7 holds 1,000 times the sheet value of level 6 (`546.75`); levels 8
to 10 take 2.5 times the level before, levels 11 to 16 twice (rounded
down).

## Field Names

The `MusicLevel` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `MusicLevel`, `MusicLevelEXPTable`,
`IncreasingBarNumber`, `IncreasingNoteNumber` and `MusicRank`, one row per
level. All five match on 6 of 6 levels (client 1784) and on the same six
levels of client 3482. The sheet writes `364.5` and `546.75` for levels 5
and 6; the file holds the integer part.

## Open Questions

### Second Count

`unknown_04` equals `count` and the highest level on both clients. A file
with a gap in its levels would tell a count from a maximum level.
