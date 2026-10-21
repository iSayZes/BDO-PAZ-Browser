# `exptoskillexprate.dbss` Format

## Purpose

An EXP to skill EXP rate per character level, levels `1` to `100`. The
rate is a server-only column, so the client file holds the levels and a
`0` for every rate. Companion `exptoskillexprateoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `exptoskillexprate.dbss`       | 1,204 | 100 Row        | 12        |
| 1      | 1784 and later | 3474    | `exptoskillexprateoffset.dbss` | 1,204 | 100 Offset Row | 12        |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `exptoskillexprate.dbss`       | 1,204 B (100.0%) | 0 B (0.0%) |
| 1      | `exptoskillexprateoffset.dbss` | 1,204 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                  |
| ------------------------------ | -------- | --------------------------------------------------------------------- |
| `exptoskillexprateoffset.dbss` | Optional | `level -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 100 x 12 = 1,204 bytes.

### Row (12 bytes)

| Offset  | Type | Field                 | Notes                                                                       |
| ------- | ---- | --------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | level                 | Character level, the row key; `1` to `count` in order                        |
| `+0x04` | u32  | level_dup             | Equal to `level` on every row; the offset index points here                  |
| `+0x08` | u32  | exp_to_skill_exp_rate | `0` on every row of clients 1784 and 3474, see Field Names                   |

### `exptoskillexprateoffset.dbss`

Bare offset table into `exptoskillexprate.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `exptoskillexprate.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                            |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | level       | Key of the row it points at             |
| `+0x04` | u32  | data_offset | Row start + 4, at `level_dup`           |
| `+0x08` | u32  | data_size   | `8` on every row: the row less its key  |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in level order, as the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The 2016 client's debug symbols have `gc::ExpToSkillExpRateStaticStatus`
as `_level` and `_expToSkillExpRate` (8 bytes): the part of the row the
offset index points at. The `ExpToSkillExpRate_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `Level` and
`ExpToSkillExpRate`; its 100 rows match the file on all 100 levels and
both values, on client 1784 and on client 3474. In the `.xlsm` copy of the
sheet (`datasheet_pcdatatable.xlsm`) the column is `%ExpToSkillExpRate`,
server-only, which the client build writes as `0`; the sheet's values are
`0` as well. Its note columns `#필요 스킬 포인트` (skill points needed) and
`#필요 PC 경험치` (character EXP needed) are not compiled.

## Notes

- No client Lua names the table or a getter for it.
