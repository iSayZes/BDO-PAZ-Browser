# `lifeexpmaxlevel.bss` Format

## Purpose

Max level of every life skill. Value N is the max level of life skill N, numbered as in the Life Skills table of [lifeexp](lifeexp_dbss.md). On client 3464 all 15 values are `180` (Guru 100), and each `lifeexp.dbss` block ends on that level (181 rows for levels 0 to 180).

Example:

```text
Gathering  Max Level 180  Guru 100
Trading    Max Level 180  Guru 100
```

## Companion Files

| File              | Required | Role                                                                |
| ----------------- | -------- | ------------------------------------------------------------------- |
| `stringtable.bss` | Optional | Hashes of the `GAME` sheet keys that name the life skills and ranks |

The life skill names and rank groups are the ones in [lifeexp](lifeexp_dbss.md); the handler imports them from `_dbss/lifeexp/labels.py`.

All multi-byte values are little-endian.

## File Layout

A bare array of u32 values with no header and no `PABR` magic. 60 bytes on client 3464, one value per `lifeexp.dbss` block.

| Offset   | Type | Field     | Notes                     |
| -------- | ---- | --------- | ------------------------- |
| `+N x 4` | u32  | max_level | Max level of life skill N |

## Suggested UI Layout

| Column        | Type | Notes                                       |
| ------------- | ---- | ------------------------------------------- |
| Life Skill ID | num  | Array index (`life_skill`)                  |
| Life Skill    | text | As in `lifeexp.dbss`                        |
| Max Level     | num  | `max_level`                                 |
| Max Rank      | text | Rank of `max_level` (`Guru 100`)            |

## Notes

- Trading (7) gets `180` here although `lifeexp.dbss` holds finite EXP for it only up to level 60; see the [lifeexp](lifeexp_dbss.md) Notes.
- `fitnessmaxlevel.bss` is the matching file for `fitnesslevel.dbss` but has `PABR` magic and a different layout; see [fitnesslevel](fitnesslevel_dbss.md).
