# `skillpiece.dbss` Format

## Purpose

Set effect tiers. A record belongs to one set skill: each equipped piece of
the set applies a [`buff.dbss`](buff_dbss.md) type 48 buff that adds points
to that skill, and once the points reach a tier's threshold the skill runs at
the tier's level. A tier also carries the Korean tooltip text: the set title,
the threshold label and the bonus lines.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records              | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ------ | -------------------- | ------------------------- |
| 1      | 1784 and later | 3474    | `skillpiece.dbss`       | 31,628 | 168 Tier, 100 Record | 30 to 534, 180 on average |
| 1      | 1784 and later | 3474    | `skillpieceoffset.dbss` | 1,004  | 100 Index Row        | 10                        |

| Layout | File                    | Known            | Unknown      |
| ------ | ----------------------- | ---------------- | ------------ |
| 1      | `skillpiece.dbss`       | 31,228 B (98.7%) | 400 B (1.3%) |
| 1      | `skillpieceoffset.dbss` | 1,004 B (100.0%) | 0 B (0.0%)   |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                               |
| --------------------- | -------- | ------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Tier text in the user's language, LOC type 52, see [`languagedata_*.loc`](languagedata_loc.md#type-52-item-set-bonus-text-skillpiecedbss); set skill name, LOC type 10 |

The handler walks the records from the start of the file and does not read
`skillpieceoffset.dbss` (see below). The buffs of each tier's
[`skill.dbss`](skill_dbss.md) rank come from the `SKILL_BUFFS` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `100` on client 3464   |
| `+0x04` | Record[count] | records | `count` variable-size records, back to back to the end of the file |

### Record (variable: 14 bytes + tiers)

| Offset       | Type             | Field          | Notes                                                        |
| ------------ | ---------------- | -------------- | ------------------------------------------------------------ |
| `+0x00`      | u16              | key_prefix     | Equals `skill_no`; the index's `data_offset` points past it  |
| `+0x02`      | u16              | skill_no       | The set skill, a `skill.dbss` skill number                   |
| `+0x04`      | u16              | skill_property | `0` in every record (client 3474); see Field Names           |
| `+0x06`      | u32              | tier_count     | Number of tiers; `1` to `13`                                 |
| `+0x0A`      | Tier[tier_count] | tiers          | `tier_count` tiers                                           |
| `tiers+0x00` | u32              | unknown_end    | `0` in every record                                          |

### Tier (variable: 30 bytes + text)

| Offset                | Type  | Field           | Notes                                                       |
| --------------------- | ----- | --------------- | ----------------------------------------------------------- |
| `+0x00`               | u32   | point           | Set points needed; rises from tier to tier; Lua `getPoint()` |
| `+0x04`               | u16   | level           | `skill.dbss` rank of the set skill; `1` to `tier_count` in order |
| `+0x06`               | str16 | group_title_kr  | Set title, `아그리스 세트 효과` ("Agris Set Effect"); the same in every tier of a record; Lua `getGroupTitle()` |
| `group_title_kr+0x00` | str16 | desc_title_kr   | Threshold label: `2부위` ("2 Parts"), `2개` ("x2"), `세트`, `6 포인트`, `목걸이, 허리띠 부위`; Lua `getDescTitle()` |
| `desc_title_kr+0x00`  | str16 | desc_kr         | Bonus lines, values in `<PAColor0xffe9bd23>` tags; Lua `getDesc()` |

A string is a u32 character count, a u32 `0` and that many UTF-16LE code
units with no terminator (`_common/record_reader.py` reads it with a u64
count). A line break is stored as the two characters `\n` (99 times on client
3464) or as a real newline (10 times); the parser turns both into a newline
with `decode_inline_text()`. All three strings are empty in every tier of 13 records (client 3464):
the Ancient Magic Crystal activation conditions `50047` to `50055`, the
matching boss weapons `50060` to `50068`, Serenity `50198`, and the Pearl Shop
outfits `44953` and `44954`.

### `skillpieceoffset.dbss`

| Offset  | Type             | Field | Notes                                     |
| ------- | ---------------- | ----- | ----------------------------------------- |
| `+0x00` | u32              | count | Equals the `skillpiece.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 10-byte rows; no magic, no trailer |

### Index Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | skill_no    | Record key                                               |
| `+0x02` | u32  | data_offset | Record start + 2, past `key_prefix`                      |
| `+0x06` | u32  | data_size   | Record size - 2                                          |

The rows are in neither key nor file order (the first row is `51128`, the
second record). `parse_bare_offset_rows` (`_common/pabr_offset.py`) reads
them, and on client 3464 every row matches the record walked from the start
of the file. `test_every_offset_row_points_past_its_records_key_prefix` in the
handler tests checks this against the installed client.

## Field Names

The record is the `PointSkill_Table` sheet of a private server on client
1784 (`SkillNo`, `SkillProperty`, `Point`, `SkillLevel`, `GroupNo`,
`GroupTitle`, `Title`, `Description`). That server's dump
(`Instance_dumpFull.exe`) reads the client record from `+0x02` (row reader
at VA `0x140c85c00`) as a u16 into `SkillPieceStaticStatus` `+0x00`, a u16
into `+0x02`, the tier count and tiers, then a u32 into `+0x28`. The sheet
loader writes `SkillNo` to `+0x00` and `SkillProperty` to `+0x02` (VA
`0x140c866f6` and `0x140c866fa`), so `skill_no` is a u16 and the next u16 is
`skill_property`. Each tier's `Point` and `SkillLevel` are `point` and
`level`, and its three texts are `GroupTitle`, `Title` and `Description`.

The private server's own file holds 269 of the sheet's 270 set skills; a
sheet `SkillNo` above 65,535 (79223 to 79403) is stored as its low 16
bits (13687 to 13867). `SkillProperty` is `0` on all 315 sheet rows and
`skill_property` on every record of that file and of client 3474. The
struct starts it at `5` before the sheet sets it, and one dump function
uses it as an index into a u32 array; what the values mean is open.

`unknown_end` has no sheet column. The sheet loader sets `+0x28` to `0`,
the reader loads it from the file, and none of the five callers of the
record getter reads it. It is `0` on every record of both clients.

## Notes

- The set effect tooltip Lua (`panel_equiment_seteffecttooltip`) reads one
  entry per tier from `ToClient_GetSkillPieceInfo()` through `getSkillNo()`,
  `getPoint()`, `getGroupTitle()`, `getDescTitle()`, `getDesc()` and
  `getApply()`. The field names here follow those getters. `getApply()` is
  whether the character has the tier active: the Lua stores it as `isApplied`
  and keeps the highest `point` among applied tiers. A stored `level`, `1` or
  more, would mark every tier as applied.
- `level` is the skill rank: all 168 tiers (client 3464) have a
  `skill.dbss` rank `skill_no << 16 | level`, and no record's skill has a rank
  past its last tier. The ranks carry the buffs; the strings here are only the
  tooltip. No getter in the tooltip Lua returns it.
- `point` is the threshold, not a piece count. The type 48 buff of a piece
  adds `param_2` points: `1` on 107 of the 123 buffs (client 3464), `2` to
  `4` on buffs of 7 set skills, most of them Pearl Shop outfits (`59184`
  takes `1` to `4` and one `-4`), and `10` on the one buff of `50049`. A
  label such as `세트` or `6 포인트` stands for a points total. 99 of the 100
  keys are the `param_1` of at least one type 48 buff; `50589` ("[Set] Black
  Eye Skill Activation Requirements") is not. The items that apply those
  buffs are the set's pieces.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  reads the same layout (`internal/tables/skillpiece.go`) with two other
  readings: `pieces` for `point`, the equipped-piece threshold, and `apply` for
  `level`, "the tier ordinal exposed by Lua as `getApply()`". The tooltip Lua
  above uses `getApply()` as the active flag, and the outfit pieces of `59184`
  add up to `4` points each.
- LOC type 52 keys a tier by `str_id1 = skill_no` and `str_id2 = level`. On
  client 3464 the 87 records with Korean text have LOC rows for every tier, and
  the 13 records without text have none. `56050` has LOC rows for levels 3 and
  4 (`x8`, `x10`) that its record and `skill.dbss` lack.
- The English text can differ from the Korean values: `59184` reads `Combat
  EXP +10%` in LOC and `+50%` in `desc_kr`.

## Open Questions

### `unknown_end`

The u32 after the tiers is `0` in all 100 records (client 3474) and in all
269 of client 1784. No sheet column fills it and no code in the client 1784
server dump reads it (Field Names). No field elsewhere points at it.

### Black Eye set points

`50589` has a record (3 points, level 1, `검은눈 효과`) but no type 48 buff
adds points to it, so it is open how the Black Eye pieces count toward it.
