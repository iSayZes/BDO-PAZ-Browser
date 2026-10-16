# `employeeexp.bss` Format

## Purpose

Sailor levelling table. One row per sailor (employee) and level holds the EXP
the sailor needs to reach the next level and, per employee ability, a dice
expression from the trailing string table (`1D2`, `1D5+30`) rolled for that
ability on level-up. The top level of each sailor has no growth and a
placeholder EXP value.

Example:

```text
employee_key 20, level 1:  exp_to_next_level 1300  growth 6: 1D2, 7: 1D2, 8: 1D1, 9: 1D5, 14: 1D4, 15: 1D1, 16: 1D1
employee_key 20, level 10: exp_to_next_level 1000  (top level: no growth)
```

## Companion Files

The format is self-contained: no offset table, the dice text lives in the
file's own string table.

| File                       | Required | Role                                                                                 |
| -------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `employeestaticstatus.bss` | Optional | Same 230 `(level, employee_key)` keys; its rows link `employee_key` to the sailor's character key |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table tail of `npcsimply.bss` and `plantexchangegroup.bss`
(`_common/pabr_strings.py`), with one empty u32 between the rows and the table.

| Offset           | Type    | Field              | Notes                                                              |
| ---------------- | ------- | ------------------ | ------------------------------------------------------------------ |
| `+0x00`          | char[4] | magic              | ASCII `PABR`                                                       |
| `+0x04`          | u32     | count              | Number of rows; 230 on client 3458 (23 sailors x 10 levels)        |
| `+0x08`          | row[]   | rows               | 89-byte rows repeated `count` times                                |
| `8 + count * 89` | u32     | footer             | Always `0`; read as an empty counted table, like the `exploration.bss` footer |
| footer + 4       | table   | string_table       | u32 count, then `count` x (u8 is_wide, u32 byte length, payload)   |
| EOF - 8          | u32     | string_table_start | Offset of the string table; equals the end of the footer          |
| EOF - 4          | u32     | zero               | Always 0                                                           |

The file tiles with no gaps: the rows end 4 bytes before `string_table_start`,
and the string table ends exactly at EOF - 8. The parser rejects a file where
this does not hold, since every field would then be suspect.

Rows run level by level (all level 1 rows, then level 2, ...); inside a level
the `employee_key` order is 23 down to 8, then 1 up to 7.

## Record Structure

### Row (89 bytes, repeated `count` times)

Fields are unaligned.

| Offset  | Type      | Field             | Notes                                                                                 |
| ------- | --------- | ----------------- | ------------------------------------------------------------------------------------- |
| `+0x00` | u8        | unknown_00        | Always `0`; the same lead byte as `fairyupgraderate.bss` rows                          |
| `+0x01` | u16       | level             | 1 to 10                                                                                |
| `+0x03` | u16       | employee_key      | Sailor key, 1 to 23; together with `level` unique per row                              |
| `+0x05` | u32       | exp_to_next_level | EXP from this level to the next; `1000` on level 10, see Notes                         |
| `+0x09` | u32       | unknown_09        | Always `0`                                                                             |
| `+0x0D` | u32[19]   | growth_ref        | String table index per employee ability (slot = ability index 0 to 18); `0` is the empty string, the ability does not grow |

### String Table

41 strings on client 3458. Index 0 is the empty string, every other entry is a
dice expression `<n>D<sides>` with an optional `+<bonus>` (`1D1`, `1D3+7`,
`1D15+25`). All are stored wide (UTF-16LE).

### Growth by Ability

Only seven ability slots are used on client 3458:

| Ability index | Rows using it | Notes                                                                                   |
| ------------- | ------------- | --------------------------------------------------------------------------------------- |
| 6, 7          | 207           | Endurance, Wits; every row below the top level                                          |
| 8, 9          | 201           | Awareness, Strength; every row below the top level except sailor 18 on levels 1, 2, 4, 5, 7 and 8 |
| 14, 15, 16    | 36            | Focus, Force, Vision; sailors 5, 8, 15 and 20 only; Vision also rolls large dice (`1D5+30`, `1D15+25`)|

The names come from `employeestaticstatus.bss`, where they are checked
against the Manage Sailors window (see that doc). The client Lua names the
abilities (`__eEmployeeAbility_Servant_*` and others) but their numbers live
in the game binary, so the link is that every growing type is one the
`employeestaticstatus.bss` row of the same sailor and level has, and the
level 6 checks in the Notes, where base plus these dice gives the window's
value stat by stat.

## EXP Curves

Every sailor follows one of four curves on client 3458 (level 1 to 9, then the
level 10 placeholder):

| Level 1 EXP | Levels 1 to 9                                                         | Sailors                                   |
| ----------- | --------------------------------------------------------------------- | ----------------------------------------- |
| 700         | 700, 1050, 1575, 3150, 6300, 12600, 37800, 113400, 340200             | 2, 11, 13                                 |
| 1000        | 1000, 1500, 2250, 4500, 9000, 18000, 54000, 162000, 486000            | 1, 4, 7, 10, 17, 19, 21                   |
| 1000        | Same as above but level 9 is 388800                                   | 22, 23                                    |
| 1300        | 1300, 1950, 2925, 5850, 11700, 23400, 70200, 210600, 631800           | 3, 5, 6, 8, 9, 12, 14, 15, 16, 18, 20     |

Each curve steps x1.5, x1.5, x2, x2, x2, x3, x3, x3 from level 1.

## Notes

- The game calls employees sailors: `employeename.dbss` holds sailor names
  (Guile, Tails), and the client Lua (`panel_window_sailormanager_all*.luac`)
  reads them through `ToClient_getEmployeeWrapperByIndex`, `getLevel` and
  `getExperienceRate`.
- `employee_key` maps to a character key through `employeestaticstatus.bss`:
  sailors 1 to 20 are the plain `Sailor` NPCs 59053 to 59072, 21 is Arkahn
  (59101), 22 is Hetario (59227) and 23 is Pacuna (59228). Every level row of a
  sailor there carries the same character key, which is why `employee_key` is
  the sailor and `level` the level, not the other way round.
- Level 10 is the top level: it is the last row of every sailor, its
  `exp_to_next_level` is `1000` for all 23 sailors, which breaks every curve,
  and it has no growth dice. Read as a placeholder.
- The abilities that grow are always a subset of the abilities the same
  `(level, employee_key)` row of `employeestaticstatus.bss` gives a nonzero
  value. That file stores abilities as `[u8 ability index][u32 value]` pairs
  using the same indices 0 to 18, with 19 as the empty slot; this is what ties
  `growth_ref` slot N to ability index N.
- The u32 at `+0x09` comes before ability 0 and is zero everywhere. Read as
  `growth_ref` slot 0 the indices would be one off from
  `employeestaticstatus.bss` on every row.
- The dice are rolls added to the ability on each level-up, one point = 0.1%
  (stored `1000` in `employeestaticstatus.bss`). The row for level N is
  rolled when reaching level N + 1, and the static file keeps the level 1
  base on every level. Checked in game on two level 6 sailors (2026-10-06):
  base plus the level 1 to 5 dice gives the window's value on all eight
  ship stats, e.g. Confident (`9`) Awareness 3.0% plus
  `1D2+2, 1D2+2, 1D3+2, 1D2+3, 1D2+3` (1.7 to 2.3) reads 5.0%, and
  Treasure-Seeking (`7`) Awareness 4.0% plus `1, 1, 1D2+1, 1D2, 1D2` (0.6
  to 0.9) reads 4.7%.

## Open Questions

### Sailor Names

The table shows `employee_key`. A name column needs the character key from
`employeestaticstatus.bss` (a shared sailor key to character lookup) and LOC
type 6 for that key.
