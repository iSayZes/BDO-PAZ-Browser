# `weatheractor.dbss` Format

## Purpose

Characters tied to the weather system: weather and time-of-day actors
(45381 Cloudy Day, 45378 Night, 27093 Typhoon, 27063 Sandstorm, 49641
Christmas Snow), Margoria storms, and monsters and bosses (24517 Small Altar
Imp, 27517 Kzarka, 23085 Vell). A row is the character key, a type byte, a
block of floats and small integers, and on three rows the skill the actor
casts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------- | --------- |
| 2      | 3473 and later | 3474    | `weatheractor.dbss`       | 7,579 | 101 Row       | 75        |
| 2      | 3473 and later | 3474    | `weatheractoroffset.dbss` | 1,014 | 101 Index Row | 10        |
| 1      | 1784           | 1784    | `weatheractor.dbss`       | 4,960 | 84 Row        | 59        |
| 1      | 1784           | 1784    | `weatheractoroffset.dbss` | 844   | 84 Index Row  | 10        |

| Layout | File                      | Known            | Unknown         |
| ------ | ------------------------- | ---------------- | --------------- |
| 2      | `weatheractor.dbss`       | 4,145 B (54.7%)  | 3,434 B (45.3%) |
| 2      | `weatheractoroffset.dbss` | 1,014 B (100.0%) | 0 B (0.0%)      |
| 1      | `weatheractor.dbss`       | 3,448 B (69.5%)  | 1,512 B (30.5%) |
| 1      | `weatheractoroffset.dbss` | 844 B (100.0%)   | 0 B (0.0%)      |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`weatheractoroffset.dbss` (see below). Character names and titles come from
LOC type 6, skill names from LOC type 10 and skill icons from the
`SKILL_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then 75-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `101` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (75 bytes)

Value spreads are from client 3464.

| Offset  | Type    | Field         | Notes                                                        |
| ------- | ------- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16     | key           | Row key; equals `character_key` on every row                 |
| `+0x02` | u8      | unknown_02    | `1` on every row                                             |
| `+0x03` | u16     | character_key | Character key, LOC type 6 names it                           |
| `+0x05` | u8      | weather_type  | `gc::EWeatherType`, see Weather Types; `3` on 93 rows          |
| `+0x06` | f32     | radius        | `4000` to `192000`; `10000` on 71 rows, `150000` on the four time-of-day actors |
| `+0x0A` | f32     | rain_amount   | `0`, `0.3`, `0.8` or `1.0`                                   |
| `+0x0E` | f32     | cloud_rate    | `0`, `0.2`, `0.3` or `1.0`                                   |
| `+0x12` | f32     | damage_max    | `10.0` on 2 rows, else `0`                                   |
| `+0x16` | f32     | damage_radius | `12000` or `120000` on 7 rows, else `0`                      |
| `+0x1A` | f32     | damage_radius_rate | `1.0` on 2 rows, else `0`                               |
| `+0x1E` | f32     | push_pull_speed | Always `0`                                                 |
| `+0x22` | u32     | skill_key     | `skill_no << 16 \| level`, the `skill.dbss` key; `0` on 98 rows |
| `+0x26` | u32     | skill_apply_rate | `5000`, `50000` or `1000000` on the skill rows, else `0`  |
| `+0x2A` | u32     | unknown_2a    | `1000000` on 23400 Erebjork, else `0`                        |
| `+0x2E` | f32     | unknown_2e    | `5.0` on 23400 Erebjork, else `0`                            |
| `+0x32` | bytes[12] | unknown_32    | All zero                                                     |
| `+0x3E` | u16     | unknown_3e    | `0` to `99`; `29` on 74 rows                                 |
| `+0x40` | f32     | unknown_40    | `0` to `23.0`; `13.0` on 75 rows                             |
| `+0x44` | u16     | unknown_44    | `99` on 89 rows; `0`, `2` or `10` on the others              |
| `+0x46` | bytes[4] | unknown_46    | All zero                                                     |
| `+0x4A` | u8      | unknown_4a    | `0` or `1` (78 rows)                                         |

The skill rows on client 3464:

| character_key            | skill_key           | Skill                     | skill_apply_rate |
| ------------------------ | ------------------- | ------------------------- | ---------------- |
| 27063 Sandstorm          | 40337 rank 1        | Debuff Sandstorm          | `1000000`  |
| 27109 Margoria Typhoon   | 40438 rank 1        | Typhoon Lightning         | `5000`     |
| 20759 Margoria Storm     | 40438 rank 1        | Typhoon Lightning         | `50000`    |

71 rows share one byte pattern (`radius` `10000`, `unknown_3e` `29`,
`unknown_40` `13.0`, `unknown_44` `99`, `unknown_4a` `1`): monsters from
24405 Red Orc to 24517 Small Altar Imp.

### `weatheractoroffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Row key, the main row's `key`                               |
| `+0x02` | u32  | offset        | Start of the row in `weatheractor.dbss` plus 2, past its key |
| `+0x06` | u32  | size          | Always `73`, the row size minus the 2-byte `key`            |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 21).

## Layout 1

On client 1784 a Row was 59 bytes: between `skill_apply_rate` and
`unknown_3e` it held 4 bytes where Layout 2 holds 20 (`unknown_2a`,
`unknown_2e`, `unknown_32`), so every later field sat 16 bytes earlier. Only
the Row differs from Layout 2; the index rows' `size` is `57` on client 1784.
Field names keep Layout 2's offsets, so `unknown_3e` sits at `+0x2E` here.

### Row (59 bytes)

| Offset  | Type     | Field              | Notes                                                         |
| ------- | -------- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16      | key                |                                                               |
| `+0x02` | u8       | unknown_02         |                                                               |
| `+0x03` | u16      | character_key      |                                                               |
| `+0x05` | u8       | weather_type       |                                                               |
| `+0x06` | f32      | radius             |                                                               |
| `+0x0A` | f32      | rain_amount        |                                                               |
| `+0x0E` | f32      | cloud_rate         |                                                               |
| `+0x12` | f32      | damage_max         |                                                               |
| `+0x16` | f32      | damage_radius      |                                                               |
| `+0x1A` | f32      | damage_radius_rate |                                                               |
| `+0x1E` | f32      | push_pull_speed    |                                                               |
| `+0x22` | u32      | skill_key          |                                                               |
| `+0x26` | u32      | skill_apply_rate   |                                                               |
| `+0x2A` | bytes[4] | unknown_old_2a     | All zero on client 1784; which Layout 2 field it became is not known |
| `+0x2E` | u16      | unknown_3e         |                                                               |
| `+0x30` | f32      | unknown_40         |                                                               |
| `+0x34` | u16      | unknown_44         |                                                               |
| `+0x36` | bytes[4] | unknown_46         |                                                               |
| `+0x3A` | u8       | unknown_4a         |                                                               |

## Notes

- `skill_key` reads as a skill key because both of its skills name the
  weather of their row: 27063 Sandstorm holds 40337 "Debuff Sandstorm" and
  the Margoria Typhoon and Storm hold 40438 "Typhoon Lightning". The level
  half is `1` on all three rows.
- The client Lua holds the weather factor enum `WEATHER_SYSTEM_FACTOR_TYPE`
  (humidity, celsius, cloud rate, rain amount, wind direction and force,
  water, oil, grass) in `global_define_cpp_enum`, but no Lua reads this
  file or names a weather actor field.

## Weather Types

`weather_type` follows `gc::EWeatherType` of the 2016 client (the debug symbols, see Field Names). No current client Lua names the values, and 3 and 4 came after 2016. Rows per value on client 3464:

| Value | Name       | Rows | Actors                                                         |
| ----- | ---------- | ---: | -------------------------------------------------------------- |
| `0`   | Cyclone    | 1    | 27006 Typhoon                                                  |
| `1`   | DesertWind | 1    | 27063 Sandstorm                                                |
| `2`   | Weather    | 5    | Typhoon, Margoria Typhoon, Margoria Storm, Christmas Snow, Blizzard of Christmas |
| `3`   | -          | 93   | Time-of-day actors (Dawn, Morning, Cloudy Day, Night), monsters and objects |
| `4`   | -          | 1    | 23400 Erebjork                                                 |

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::WeatherActorStaticStatus` lists `_key`, `_weatherApplyType`, `_weatherApplyRadius`, `_weatherRainAmount`, `_weatherCloudRate`, `_weatherDamageMax`, `_weatherDamageRadiusMax`, `_weatherDamageRadiusRate`, `_weatherPushPullSpeed`, `_weatherSkillKey` and `_weatherSkillApplyRate` in the order this row stores them from `+0x03`. The server-side `WeatherActor_Table` of a private server on client 519 holds 11 of the 101 actors (the storms, Sandstorm, Vell, Kzarka and the Margoria actors), and on all 11 its columns `Type`, `Radius`, `DamageMax`, `DamageRadius`, `DamageRadiusRate`, `SkillNo` and `SkillApplyRate` equal the fields named after them. Its `RainAmount` and `CloudRate` are the same values in millionths (`800000` for `0.8`), and `PushPullSpeed` is `0` like `push_pull_speed`.

## Open Questions

### unknown_2a and unknown_2e

`unknown_2a` (`1000000`) and `unknown_2e` (`5.0`) are set only on 23400 Erebjork, the only actor of weather type `4`. The server table has `WaveScale` and `Time` after the skill columns, but both are `0` on its 11 rows, so neither can be matched.

### unknown_3e, unknown_40 and unknown_44

`unknown_3e` (u16), `unknown_40` (f32) and `unknown_44` (u16) are set together. `unknown_44` is `99` on 89 rows; on 27517 Kzarka (`2`), 20755 Margoria Phantom Ship (`10`) and 23085 Vell (`99`) it equals `unknown_3e`, and on 10 rows both are `0`. The server's `WeatherColorTable` equals both of them on its 11 rows, so one of the two is the colour table index, but those rows cannot tell which. `unknown_40` (`13.0` on 75 rows, at most `23.0`) fits an hour of the day.
