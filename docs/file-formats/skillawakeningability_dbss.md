# `skillawakeningability.dbss` Format

## Purpose

The Skill Add-on effects: one row per ability index, with the buff the
effect applies and its Korean description. The skill window lists the
add-ons of a skill by these indexes (`ToClient_GetAwakeningAbilityIndex`)
and shows their text, so the index is the key other files and the Lua use.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes  | Records      | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------------- | ------ | ------------ | -------------------------- |
| 2      | 3474 and later | 3482    | `skillawakeningability.dbss`       | 15,838 | 96 Row       | 110 to 270, 165 on average |
| 2      | 3474 and later | 3482    | `skillawakeningabilityoffset.dbss` | 1,156  | 96 Index Row | 12                         |
| 1      | 1348 to 3251   | 3251    | `skillawakeningability.dbss`       | 15,598 | 96 Row       | 108 to 252, 162 on average |
| 1      | 1348 to 3251   | 3251    | `skillawakeningabilityoffset.dbss` | 1,156  | 96 Index Row | 12                         |

| Layout | File                               | Known            | Unknown      |
| ------ | ---------------------------------- | ---------------- | ------------ |
| 2      | `skillawakeningability.dbss`       | 15,454 B (97.6%) | 384 B (2.4%) |
| 2      | `skillawakeningabilityoffset.dbss` | 1,156 B (100.0%) | 0 B (0.0%)   |
| 1      | `skillawakeningability.dbss`       | 15,214 B (97.5%) | 384 B (2.5%) |
| 1      | `skillawakeningabilityoffset.dbss` | 1,156 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The rows are read in file order from the count;
`skillawakeningabilityoffset.dbss` (below) only says where each row sits.
LOC type 33 holds the English description of each ability index (see
Field Names), and LOC type 5 the buff text.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 24 bytes + description text)

| Offset                | Type  | Field                     | Notes                                                                 |
| --------------------- | ----- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00`               | u32   | ability_index             | The row key, from `1`; LOC type 33 `str_id1`                          |
| `+0x04`               | u32   | ability_index_dup         | Equal to `ability_index` on every row; the offset index points here   |
| `+0x08`               | u32   | buff_id                   | The `buff.dbss` buff the effect applies                               |
| `+0x0C`               | str16 | description_kr            | Korean effect text with `<PAColor>` tags                              |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on every row of clients 1784 and 3482; see Open Questions         |

### `skillawakeningabilityoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                          |
| ------- | ---------------- | ----- | ------------------------------ |
| `+0x00` | u32              | count | Equals the main file's `count` |
| `+0x04` | Index Row[count] | rows  | See Index Row                  |

### Index Row (12 bytes)

| Offset  | Type | Field         | Notes                                       |
| ------- | ---- | ------------- | ------------------------------------------- |
| `+0x00` | u32  | ability_index | Key of the row it points at                 |
| `+0x04` | u32  | data_offset   | Row start + 4, at `ability_index_dup`       |
| `+0x08` | u32  | data_size     | The row less its leading `ability_index`    |

On clients 1784 and 3482 every index row points at the row with its key,
and the rows tile the file. Index and rows share one order, which is no
key order (96, 79 to 64, 95 to 80, 47 to 32, ... on client 3482).

## Layout 1

`buff_id` is a u16, as `_buffkey` in the 2016 `gc::SkillAwakeningAbilityStaticStatus`.

### Row (variable: 22 bytes + description text)

| Offset                | Type  | Field                     | Notes                                       |
| --------------------- | ----- | ------------------------- | ------------------------------------------- |
| `+0x00`               | u32   | ability_index             | The row key                                 |
| `+0x04`               | u32   | ability_index_dup         | Equal to `ability_index` on every row       |
| `+0x08`               | u16   | buff_id                   | The `buff.dbss` buff the effect applies     |
| `+0x0A`               | str16 | description_kr            | Korean effect text                          |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on every row of client 1784             |

## Field Names

The `Awakening_Ability_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`, `Buff`,
`BuffTarget`, `Description`, `VariedDirectDamage`, `VariedRangeDamage`,
`VariedMagicalDamage`, `VariedDirectHit`, `VariedRangeHit` and
`VariedMagicalHit`. Its 93 rows match the 93 rows of the official client
1784 file on `Index`, `Buff` and `Description` (93 of 93 each).

| Field          | Column        | Same value (client 1784) | Same value (client 3482) |
| -------------- | ------------- | ------------------------ | ------------------------ |
| ability_index  | `Index`       | 93 of 93                 | 93 of 93 (the file adds 94 to 96) |
| buff_id        | `Buff`        | 93 of 93                 | 21 of 93                 |
| description_kr | `Description` | 93 of 93                 | 0 of 93                  |

Client 3482 moved most rows to other buffs and rewrote every text, so
only the index carries over. `BuffTarget` (`0` self, `1` enemy, as
`gc::BuffTargetType`) is `1` on 51 sheet rows and `0` on 42, but
`unknown_description_kr_00` is `0` on all of them, so the column is not in
the file. The six `Varied*` columns are `<null>` on every sheet row.

The 2016 `gc::SkillAwakeningAbilityStaticStatus` has the members `_key`
(u32), `_buffkey` (u16, the width of Layout 1), `_buffTarget`,
`_description`, `_variedDamage` (3 f32) and `_variedHit` (3 f32).

LOC type 33 is the English `description_kr`: `str_id1` is the ability
index, the other ids `0`. Client 3482 has one string for each of the 96
indexes (index 96: "Target's recovery -40% for 7 sec").

## Notes

- `panel_window_reinforceskill_all_1.luac` and
  `panel_window_skillgroup_all_1.luac` (client 3482) read up to two
  add-ons per skill: `ToClient_GetAwakeningAbilityCount(skillNo)`, then
  `ToClient_GetAwakeningAbilityIndex(skillNo, i)` for each, and show
  `getSkillAwakenDescription(index)`. Which indexes a skill may roll is not
  in this file.
- The Korean texts open with `자신` (self, 36 rows on client 3482), `상대`
  (target, 54 rows) or `타격` (on hit, 6 rows), which follows the sheet's
  `BuffTarget` on client 1784; the client gets the target from the buff.

## Open Questions

### What `unknown_description_kr_00` Holds

The u32 after the description is `0` on all 93 rows of client 1784 and all
96 rows of client 3482. The 2016 struct ends with the six `Varied*` floats,
which the sheet leaves empty; a u32 count of an empty list would read as
`0` too, but no row has a non-zero value to tell the two apart.

### Which File Lists the Add-ons of a Skill

`skillawakeningability2.bss` (82 KB on client 3482, not documented yet)
shares the stem and is the likely source of the per-skill index lists the
Lua reads through `ToClient_GetAwakeningAbilityIndex`.
