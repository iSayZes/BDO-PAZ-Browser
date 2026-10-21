# `yachthandrank.bss` Format

## Purpose

The hand ranks (scoring combinations) of Yar!, the card and dice minigame
of [`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md). Each row is one hand
rank: which cards it checks (an eye value, a count of equal cards, a
straight length, two pair or full house), whether it scores a fixed number
of points or the sum of the matching cards, and its icon texture, Korean
name and Korean description. `yachtnpcdiceinfo.bss` and
[`yachtgameboardinfo.bss`](yachtgameboardinfo_bss.md) list hand ranks by
key, and [`yachtautobubbletextinfo.bss`](yachtautobubbletextinfo_bss.md)
keys some lines to one. The plain PABR file holds the rows, then the string
table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `yachthandrank.bss` | 2,951 | 15 Row  | 49        |

| Layout | File                | Known           | Unknown      |
| ------ | ------------------- | --------------- | ------------ |
| 1      | `yachthandrank.bss` | 2,696 B (91.4%) | 255 B (8.6%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                               |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Hand rank names (LOC type 105, `str_id1=hand_rank_key`, `str_id4=0`) and descriptions (`str_id4=1`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Fixed-size rows, back to back; see Row       |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). `count` rows of 49 bytes end exactly at
`string_table_start`.

### Row (49 bytes)

| Offset  | Type     | Field              | Notes                                                                      |
| ------- | -------- | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32      | hand_rank_key      | Unique row key, LOC type 105 `str_id1`                                     |
| `+0x04` | bytes[9] | unknown_04         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x0D` | u32      | unknown_0d         | `1` on every row (clients 1784 and 3474)                                   |
| `+0x11` | bytes[4] | unknown_11         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x15` | u8       | target_eye         | Eye value the hand counts (`1` to `6`); `0` checks no eye                  |
| `+0x16` | u32      | target_count       | Number of equal cards the hand needs (`2` to `5`); `0` for none            |
| `+0x1A` | u32      | straight_count     | Length of the straight the hand needs (`4` or `5`); `0` for none           |
| `+0x1E` | u8       | is_full_house      | `1` on the full house hand (key 11)                                        |
| `+0x1F` | u8       | is_two_pair        | `1` on the two pair hand (key 10)                                          |
| `+0x20` | u32      | made_point         | Fixed points the hand scores; `0` when it scores the card sum              |
| `+0x24` | u8       | is_sum_point       | `1` when the hand scores the sum of its cards                              |
| `+0x25` | u32      | icon_texture_index | String table index of the icon's texture ID (`Combine_Etc_Minigame_Yatzee_Icon_Ones`) |
| `+0x29` | u32      | name_kr_index      | String table index of the Korean name                                      |
| `+0x2D` | u32      | desc_kr_index      | String table index of the Korean description                               |

No field is padded, so the u32 fields after `target_eye` are not 4-byte
aligned.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (45 on client 3474)     |
| `+0x04` | pstr[string_count] | strings      | Per row its icon texture ID (UTF-8), name and description (UTF-16) |

## Hand Ranks

On client 3474 the file holds 15 rows. Names are the LOC type 105 English text.

| Key | Name           | Checks                         | Points       |
| --- | -------------- | ------------------------------ | ------------ |
| 1   | Bit o' Ones    | Eye 1                          | Sum          |
| 2   | Bunch o' Twos  | Eye 2                          | Sum          |
| 3   | Lump o' Threes | Eye 3                          | Sum          |
| 4   | Nest o' Fours  | Eye 4                          | Sum          |
| 5   | Clump o' Fives | Eye 5                          | Sum          |
| 6   | Stack o' Sixes | Eye 6                          | Sum          |
| 7   | Mates          | 2 equal cards                  | Sum          |
| 8   | Peak           | 3 equal cards                  | Sum          |
| 9   | Dragon Claw    | 4 equal cards                  | Sum          |
| 10  | Double Trouble | Two pair                       | 15           |
| 11  | Den of Wolves  | Full house                     | 25           |
| 12  | Yar!           | 5 equal cards                  | 50           |
| 13  | Broken Arrow   | Straight of 4                  | 30           |
| 14  | Straight Shot  | Straight of 5                  | 40           |
| 15  | Chance         | None                           | Sum          |

On every row exactly one of `made_point` and `is_sum_point` is set.

## Field Names

The `HandRanking` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `HandRankKey` (`hand_rank_key`), `HandType`,
`TargetSymbol`, `TargetEye` (`target_eye`), `IsTwoPair` (`is_two_pair`),
`IsFullHouse` (`is_full_house`), `TargetCount` (`target_count`),
`StraightCount` (`straight_count`), `MadePoint` (`made_point`), `SumPoint`
(`is_sum_point`), `UI_Texture`, `~Name` and `~Desc`. Its 15 rows match the
15 rows of clients 1784 and 3474 in every named column and string, with
`<null>` stored as `0`; the file writes `IsFullHouse` before `IsTwoPair`.
The two files are byte for byte the same. The client Lua reads the strings
through `getIconTextureName()`, `getName()` and `getDesc()` on
`ToClient_getHandRankStaticStatusWrapper(key)`
(`panel_window_minigame_yachtdice_invite_1.luac`).

The `#참조` sheet of the same workbook notes the values: `HandType` `0`
checks the eye only, `1` the symbol only, `2` both; `TargetSymbol` is a
card symbol (`1` to `4`, see [`yachtbasecard.dbss`](yachtbasecard_dbss.md)).
Both are `0` or `<null>` on every sheet row, so the data cannot tell which
bytes of `unknown_04` to `unknown_11` hold them.

## Notes

- The LOC type 105 descriptions (`str_id4=1`) follow the Korean ones:
  "Gain the sum of all 1s in points.", "Two pairs. Gain 15 points."

## Open Questions

### Where `HandType` and `TargetSymbol` Sit

The sheet has two columns the named fields do not cover, `HandType` and
`TargetSymbol`, both `0` on every row, and the row has 17 bytes from `+0x04`
to `+0x14` that the named fields do not cover: 13 zero bytes and the u32
`unknown_0d`, `1` on every row. A hand rank with a symbol check would show
which bytes they are; no client has one. `unknown_0d` matches no sheet
column.
