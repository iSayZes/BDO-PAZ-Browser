# `yachtgameboardinfo.bss` Format

## Purpose

The game boards (modes) of a Yar! match between two players, picked in the
invite window (`panel_window_minigame_yachtdice_invite_1.luac`). Each row is
one board: the [`yachthandrank.bss`](yachthandrank_bss.md) hand ranks it
plays, how many rolls a turn allows, its difficulty level (stars), its
Korean description, its icon textures and whether it uses matchmaking. The
plain PABR file holds the rows, then the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | ----------------------- |
| 2      | 3474 and later | 3474    | `yachtgameboardinfo.bss` | 2,523 | 9 Row   | 54 to 90, 68 on average |
| 1      | 1784           | 1784    | `yachtgameboardinfo.bss` | 2,220 | 8 Row   | 53 to 89, 64 on average |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 2      | `yachtgameboardinfo.bss` | 2,523 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtgameboardinfo.bss` | 2,220 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachthandrank.bss`   | Optional | Korean hand rank names, where LOC has none                                               |
| `languagedata_en.loc` | Optional | Board descriptions (LOC type 109, `str_id1=game_board_key`), hand rank names (LOC type 105) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row    |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). Walking `count` rows ends exactly at
`string_table_start`.

### Row (variable: 30 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                                              |
| --------------------- | -------------------- | ------------------ | ------------------------------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key, LOC type 109 `str_id1`                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                                               |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`, in sheet order (not always ascending) |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn; `3` or `4` (client 3474)                           |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description                       |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Card01`) |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Big_Card01`) |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars; `1` to `5`                   |
| `hand_rank_keys+0x11` | u8                   | is_use_matching    | `1` when the board offers matchmaking against a stranger           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (27 on client 3474)        |
| `+0x04` | pstr[string_count] | strings      | Per row its description (UTF-16) and two texture IDs (UTF-8) |

## Layout 1

Client 1784 rows have no `is_use_matching`.

### Row (variable: 29 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                      |
| --------------------- | -------------------- | ------------------ | ------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                       |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`                |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn                             |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars       |

## Game Boards

On client 3474 the file holds 9 rows. The descriptions are the first
sentence of the LOC type 109 English text.

| Key | Level | Hand ranks               | Rolls | Matchmaking | Description                                     |
| --- | ----- | ------------------------ | ----- | ----------- | ----------------------------------------------- |
| 1   | 1     | 1 to 6, 15               | 3     | No          | The most basic mode.                            |
| 2   | 2     | 1, 3, 5, 8, 14, 15       | 3     | No          | A mode with only odd-numbered hands.            |
| 3   | 2     | 2, 4, 6, 7, 9, 13, 15    | 3     | No          | A mode with only even-numbered hands.           |
| 4   | 3     | 1 to 6, 10, 11, 15       | 3     | No          | A mode with numbered hands, Double Trouble, and Den of Wolves. |
| 5   | 3     | 1 to 3, 10, 11, 13 to 15 | 3     | No          | A mode that values low-numbered hands.          |
| 6   | 4     | 1 to 6, 13 to 15         | 4     | No          | A mode with numbered hands, Broken Arrow, and Straight Shot. |
| 7   | 4     | 7 to 11, 13 to 15, 12    | 4     | No          | A mode without single-numbered hands.           |
| 8   | 5     | 1 to 11, 13 to 15, 12    | 4     | No          | A mode with all Yar! hands available.           |
| 9   | 5     | 1 to 11, 13 to 15, 12    | 4     | Yes         | A mode with all Yar! hands available.           |

Rows 7 to 9 list hand rank `12` last. Row 9 differs from row 8 only in
`is_use_matching` and its second description line, "Select this when you
want to battle a stranger."

## Field Names

The `PVP_GameBoard` sheet of a private server's `datasheet_minigame.xlsm`
on client 1784 has the columns `GameBoardKey` (`game_board_key`),
`HandRankKeyList` (`hand_rank_keys`, one comma-separated list),
`RollCountMax` (`roll_count_max`), `~Name`, `Level` (`level`), `~Desc`,
`IconTexture` and `BigTexture`. Its 8 rows match rows 1 to 8 of clients
1784 and 3474 in every named column and in the description and texture
strings, hand rank order included. `~Name` holds the level as star text
(`★★<PAColor0xff6c6c6c>☆☆☆<PAOldColor>`) and is not in the file. The file
writes `~Desc` before the textures and `Level` after them.

The client Lua (`panel_window_minigame_yachtdice_invite_1.luac`) reads a
board through `ToClient_getYachtGameBoardStaticStatusWrapperByIndex()` and
`...ByKey()`: `getKey()`, `getLevel()` (the star count), `getDesc()`,
`getHandRankCount()`, `isHaveHandRankKey()`, `getBigTextureId()`,
`getIconNormalTextureId()`, `getIconOverTextureId()` and
`getIconClickTextureId()` (three states of the board button, from the one
`icon_texture_index` string), and `isUseMatching()`, which shows the
matchmaking button.

## Notes

- Client 1784 has rows 1 to 8 and no `is_use_matching`. Client 3474 adds
  row 9 and the byte; row 9 is the only row with `1`.
