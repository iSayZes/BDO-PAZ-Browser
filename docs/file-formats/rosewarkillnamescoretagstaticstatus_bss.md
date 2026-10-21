# `rosewarkillnamescoretagstaticstatus.bss` Format

## Purpose

The Rose War name titles by score: one row per title with a score, the
GAME sheet key of the title text and an ARGB colour. On client 3474 the
file has 4 rows, score `0` to `100`, from Champion up to Hero.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarkillnamescoretagstaticstatus.bss` | 312   | 4 Row   | 12        |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `rosewarkillnamescoretagstaticstatus.bss` | 312 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Title text, LOC type 37 under the GAME sheet key hash |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (12 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | score         | `0`, `10`, `30` and `100` on client 3474, rising with the title             |
| `+0x04` | u32  | title_key_ref | String table index of a GAME sheet key, `LUA_ROSEWAR_CHARTITLE_RANK_<n>`    |
| `+0x08` | u32  | color         | ARGB colour, alpha `0xFF` on every row                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                       |
| ------- | ------------------ | ------------ | ------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `4` on client 3474       |
| `+0x04` | pstr[string_count] | strings      | Wide strings, the title keys in row order   |

## Titles

The title text is the LOC type 37 entry of the key's GAME sheet hash
(`_common/string_hash.py`). Client 3474:

| `score` | Title key                       | Title (LOC type 37) | `color`      |
| ------- | ------------------------------- | ------------------- | ------------ |
| `0`     | `LUA_ROSEWAR_CHARTITLE_RANK_6`  | Champion            | `0xFFABFF79` |
| `10`    | `LUA_ROSEWAR_CHARTITLE_RANK_5`  | Elite Champion      | `0xFF8AE7F5` |
| `30`    | `LUA_ROSEWAR_CHARTITLE_RANK_4`  | Devourer            | `0xFFECB2FF` |
| `100`   | `LUA_ROSEWAR_CHARTITLE_RANK_3`  | Hero                | `0xFFFFE380` |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. `score` follows the file
name (kill name score tag) and the scoreboard's
`getRoseWarPersonalScore()`; `title_key_ref` points at the
`LUA_ROSEWAR_CHARTITLE_*` keys, which no client Lua file reads, so the
client code reads them from this table. `color` holds four ARGB values with
full alpha.

## Notes

- The file is the same on clients 3002, 3251 and 3474, 312 bytes. It is
  not in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with the title key and its LOC text.

## Open Questions

### What the Score Counts

`score` rises with the title, so each row reads as the lowest score for its
title, but no Lua shows how the client compares the two. Whether the score
is the kill count or the personal score of the scoreboard, and whether a
player at exactly `10` gets Elite Champion, are open.
