# `weatheractor.dbss` Format

## Purpose

Characters tied to the weather system: weather and time-of-day actors
(45381 Cloudy Day, 45378 Night, 27093 Typhoon, 27063 Sandstorm, 49641
Christmas Snow), Margoria storms, and monsters and bosses (24517 Small Altar
Imp, 27517 Kzarka, 23085 Vell). A row is the character key, a type byte, a
block of floats and small integers, and on three rows the skill the actor
casts.

```text
27063 Sandstorm          type 1  skill 40337 Debuff Sandstorm (rank 1)
27109 Margoria Typhoon   type 2  skill 40438 Typhoon Lightning (rank 1)
45381 Cloudy Day         type 3
```

## Companion Files

None. The handler reads the rows in file order and does not need
`weatheractoroffset.dbss` (see below). Character names and titles come from
LOC type 6, skill names from LOC type 10 and skill icons from the
`SKILL_ICON` lookup index.

All multi-byte values are little-endian.

## File Layout

No `PABR` magic and no string table. A row count, then 75-byte rows; the
file ends after the last row.

| Offset  | Type  | Field     | Notes                    |
| ------- | ----- | --------- | ------------------------ |
| `+0x00` | u32   | row_count | `101` on client 3464     |
| `+0x04` | row[] | rows      | `row_count` 75-byte rows |

### Row (75 bytes)

Value spreads are from client 3464.

| Offset  | Type    | Field         | Notes                                                        |
| ------- | ------- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16     | key           | Row key; equals `character_key` on every row                 |
| `+0x02` | u8      | unknown_02    | `1` on every row                                             |
| `+0x03` | u16     | character_key | Character key, LOC type 6 names it                           |
| `+0x05` | u8      | unknown_05    | `3` on 93 rows; `0`, `1`, `2` (5 rows) and `4` on the others |
| `+0x06` | f32     | unknown_06    | `4000` to `192000`; `10000` on 71 rows                        |
| `+0x0A` | f32     | unknown_0a    | `0`, `0.3`, `0.8` or `1.0`                                   |
| `+0x0E` | f32     | unknown_0e    | `0`, `0.2`, `0.3` or `1.0`                                   |
| `+0x12` | f32     | unknown_12    | `10.0` on 2 rows, else `0`                                   |
| `+0x16` | f32     | unknown_16    | `12000` or `120000` on 7 rows, else `0`                      |
| `+0x1A` | f32     | unknown_1a    | `1.0` on 2 rows, else `0`                                    |
| `+0x1E` | u8[4]   | unknown_1e    | All zero                                                     |
| `+0x22` | u32     | skill_key     | `skill_no << 16 \| level`, the `skill.dbss` key; `0` on 98 rows |
| `+0x26` | u32     | unknown_26    | `5000`, `50000` or `1000000` on the skill rows, else `0`     |
| `+0x2A` | u32     | unknown_2a    | `1000000` on 23400 Erebjork, else `0`                        |
| `+0x2E` | f32     | unknown_2e    | `5.0` on 23400 Erebjork, else `0`                            |
| `+0x32` | u8[12]  | unknown_32    | All zero                                                     |
| `+0x3E` | u16     | unknown_3e    | `0` to `99`; `29` on 74 rows                                 |
| `+0x40` | f32     | unknown_40    | `0` to `23.0`; `13.0` on 75 rows                             |
| `+0x44` | u16     | unknown_44    | `99` on 89 rows; `0`, `2` or `10` on the others              |
| `+0x46` | u8[4]   | unknown_46    | All zero                                                     |
| `+0x4A` | u8      | unknown_4a    | `0` or `1` (78 rows)                                         |

The skill rows on client 3464:

| character_key            | skill_key           | Skill                     | unknown_26 |
| ------------------------ | ------------------- | ------------------------- | ---------- |
| 27063 Sandstorm          | 40337 rank 1        | Debuff Sandstorm          | `1000000`  |
| 27109 Margoria Typhoon   | 40438 rank 1        | Typhoon Lightning         | `5000`     |
| 20759 Margoria Storm     | 40438 rank 1        | Typhoon Lightning         | `50000`    |

71 rows share one byte pattern (`unknown_06` `10000`, `unknown_3e` `29`,
`unknown_40` `13.0`, `unknown_44` `99`, `unknown_4a` `1`): monsters from
24405 Red Orc to 24517 Small Altar Imp.

## `weatheractoroffset.dbss`

A u32 row count (equal to the main file's), then 10-byte rows:

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Row key, the main row's `key`                               |
| `+0x02` | u32  | offset        | Start of the row in `weatheractor.dbss` plus 2, past its key |
| `+0x06` | u32  | size          | Always `73`, the row size minus the 2-byte `key`            |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 21).

## Suggested UI Layout

| Column       | Type | Notes                                                      |
| ------------ | ---- | ---------------------------------------------------------- |
| Character ID | num  | `character_key`                                            |
| Name         | text | LOC type 6 name, else the ID                               |
| Title        | text | LOC type 6 title (`str_id4` 1); a dash when there is none  |
| Skill ID     | num  | The skill number of `skill_key`; a dash when `0`           |
| Skill        | text | Skill icon and LOC type 10 name; a dash when `0`           |

The table opens in file order.

The offset table shows Character ID, Data Offset and Size.

## Notes

- `skill_key` reads as a skill key because both of its skills name the
  weather of their row: 27063 Sandstorm holds 40337 "Debuff Sandstorm" and
  the Margoria Typhoon and Storm hold 40438 "Typhoon Lightning". The level
  half is `1` on all three rows.
- The client Lua holds the weather factor enum `WEATHER_SYSTEM_FACTOR_TYPE`
  (humidity, celsius, cloud rate, rain amount, wind direction and force,
  water, oil, grass) in `global_define_cpp_enum`, but no Lua reads this
  file or names a weather actor field.

## Open Questions

### unknown_05

Five values, `3` on 93 rows. The weather actors spread over all five
(27006 Typhoon `0`, 27063 Sandstorm `1`, 27093 Typhoon and 49641 Christmas
Snow `2`, 45381 Cloudy Day `3`, 23400 Erebjork `4`), so it is not a plain
weather or monster split.

### unknown_06 to unknown_1a

`unknown_06` runs from `4000` to `192000` and is `150000` on the four
time-of-day actors (45379 Dawn, 45380 Morning, 45381 Cloudy Day, 45378
Night), which would fit a range in centimetres (1.5 km), but no
client text gives the unit. `unknown_0a` and `unknown_0e` sit between `0`
and `1` like weights.

### unknown_26, unknown_2a and unknown_2e

`unknown_26` is set only next to a skill key. `1000000` is 100% on the
client's usual rate scale, but `5000` and `50000` also fit a time in
milliseconds.

### unknown_3e, unknown_40 and unknown_44

`unknown_3e` (u16), `unknown_40` (f32) and `unknown_44` (u16) are set
together. `unknown_44` is `99` on 89 rows; on 27517 Kzarka (`2`), 20755
Margoria Phantom Ship (`10`) and 23085 Vell (`99`) it equals `unknown_3e`,
and on 10 rows both are `0`.
