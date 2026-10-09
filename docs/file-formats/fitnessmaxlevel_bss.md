# `fitnessmaxlevel.bss` Format

## Purpose

Max level of every fitness stat. Value N is the max level of fitness type N, numbered as in the Fitness Type table of [fitnesslevel](fitnesslevel_dbss.md) (`0` Breath, `1` Strength, `2` Health). On client 3464 all three values are `50`, and each `fitnesslevel.dbss` block ends on that level (51 rows for levels 0 to 50).

Example:

```text
Breath    Max Level 50
Strength  Max Level 50
Health    Max Level 50
```

All multi-byte values are little-endian.

## File Layout

`PABR` magic, a bare u32 array with no count, then the 12-byte PABR trailer. 28 bytes on client 3464.

| Offset   | Type    | Field     | Notes                                                    |
| -------- | ------- | --------- | -------------------------------------------------------- |
| `+0x00`  | char[4] | magic     | `PABR` (ASCII)                                           |
| `+0x04`  | u32[]   | max_level | One per fitness type; value N is the max level of type N |
| varies   | trailer | trailer   | 12 bytes                                                 |

The array length is not stored; the parser takes it from the trailer's `end_of_data`: `(end_of_data - 4) / 4` values.

### Trailer (12 bytes)

| Offset  | Type | Field       | Observed | Notes                                          |
| ------- | ---- | ----------- | -------- | ---------------------------------------------- |
| `+0x00` | u32  | reserved_a  | `0`      |                                                |
| `+0x04` | u32  | end_of_data | `16`     | Byte offset right after the last `max_level`   |
| `+0x08` | u32  | reserved_b  | `0`      |                                                |

The same trailer closes `acceptquest.bss` and the PABR offset files.

## Suggested UI Layout

| Column     | Type | Notes                                         |
| ---------- | ---- | --------------------------------------------- |
| Fitness ID | num  | Array index (`fitness_type`)                  |
| Fitness    | text | Breath, Strength or Health                    |
| Max Level  | num  | `max_level`                                   |

## Notes

- The fitness type names are the ones in [fitnesslevel](fitnesslevel_dbss.md); both handlers read them through `_dbss/fitnesslevel/labels.py`.
- Level 30 is the soft cap and this file does not store it. It shows only in the EXP column of `fitnesslevel.dbss`; see the [fitnesslevel](fitnesslevel_dbss.md) Notes.
- `lifeexpmaxlevel.bss` is the life skill counterpart, a bare u32 array with no magic and no trailer; see [lifeexpmaxlevel](lifeexpmaxlevel_bss.md).
- `skillexperiencemaxlevel.bss` and `guildskillexperiencemaxlevel.bss` (18 bytes each) also start with `PABR` but hold one u32 (`2000` and `1000`) followed by `00 00 06 00` and 6 zero bytes, a different layout.
