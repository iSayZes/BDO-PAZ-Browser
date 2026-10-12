# `servantexperience.dbss` Format

## Purpose

Level table of the mounts and ships (servants): one record per servant
character and level, with the EXP to the next level, max HP, stamina and
weight, the four movement stats and the dice that add a random bonus on each
level-up. Each record holds
the stat body of [experience.bss](experience_bss.md) in its middle. On client
3464 the file has 20,885 records for 418 servants.

Example (client 3464):

```text
9989 Arduanatt, level 1:   EXP 22,625     HP 2,140   stamina 3,540   weight 180 LT  accel 137.5%  speed 137.5%  turn 122.5%  brake 122.5%  dice 1D13
9989 Arduanatt, level 30:  EXP 1,282,600  HP 35,200  stamina 19,200  weight 209 LT  accel 137.5%  speed 137.5%  turn 122.5%  brake 122.5%  dice 1D13
31521 Doom, level 1:       EXP 22,625     HP 2,272   stamina 3,496   weight 180 LT  accel 130.0%  speed 130.0%  turn 139.0%  brake 139.0%  dice 1D13
```

## Companion Files

| File                            | Required | Role                                                                          |
| ------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `servantexperienceoffset.dbss`  | Required | Key to `(offset, size)` index of the records                                  |
| `languagedata_en.loc`           | Optional | Servant names (LOC type 6, `str_id1` = `character_id`)                        |

[servantexperiencemaxlevel.bss](servantexperiencemaxlevel_bss.md) holds each
servant's top level; the handler does not need it, since the records give the
same number.

All multi-byte values are little-endian.

## File Layout

### `servantexperience.dbss`

| Offset  | Type     | Field   | Notes                                         |
| ------- | -------- | ------- | --------------------------------------------- |
| `+0x00` | u32      | count   | 20,885 on client 3464; equals the index count |
| `+0x04` | record[] | records | Back to back, variable size                   |

The record sizes sum to the file size minus 4.

### `servantexperienceoffset.dbss`

| Offset  | Type    | Field   | Notes                                |
| ------- | ------- | ------- | ------------------------------------ |
| `+0x00` | u32     | count   | Number of entries                    |
| `+0x04` | entry[] | entries | `count` entries of 12 bytes          |

| Offset  | Type | Field  | Notes                                                      |
| ------- | ---- | ------ | ---------------------------------------------------------- |
| `+0x00` | u32  | key    | `level << 16 \| character_id`; the first 4 bytes of the record |
| `+0x04` | u32  | offset | Byte offset of the record in `servantexperience.dbss`      |
| `+0x08` | u32  | size   | Record size in bytes                                       |

The index is not in file order: the first entry is level 0 of character
31017, whose record sits after its level 1 record.

## Record Structure

### Wide String

| Offset  | Type      | Field  | Notes                                 |
| ------- | --------- | ------ | ------------------------------------- |
| `+0x00` | u64       | length | Character count                       |
| `+0x08` | utf16le[] | text   | `length` characters, no terminator    |

### Level Record (352 to 412 bytes on client 3464)

The record size is 352 plus twice the characters of the six dice strings.
Offsets after `+0x110` follow the strings.

| Offset   | Type             | Field        | Notes                                                                 |
| -------- | ---------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00`  | u16              | character_id | Servant character, as in `characterstatic.dbss`                       |
| `+0x02`  | u16              | level        | 0 to the servant's top level                                          |
| `+0x04`  | u16              | unknown_04   | Always 0                                                              |
| `+0x06`  | u64              | exp          | EXP from `level` to `level + 1` (Notes)                               |
| `+0x0E`  | f32              | max_hp       | Max HP, shown as is; `1.0` at level 0                                 |
| `+0x12`  | u32              | max_mp       | Max stamina (`getMaxMp()`), shown as is; 0 on ships; `1` at level 0   |
| `+0x2A`  | f32              | unknown_2a   | `1.0` at level 0, else 0                                              |
| `+0x42`  | u32[4]           | unknown_42   | Always `5, 5, 5, 5`                                                   |
| `+0x52`  | u32              | max_weight   | Max weight, LT x 10,000; 0 at level 0                                 |
| `+0x5A`  | f32              | unknown_5a   | Always `1.0`                                                          |
| `+0x6E`  | u32[3]           | unknown_6e   | Always `10, 10, 10`                                                   |
| `+0x7A`  | f32              | unknown_7a   | `1.0` at level 0, else 0                                              |
| `+0x8A`  | u32[8]           | stats        | By `ServantStatType` (Enum Values), percent x 10,000                  |
| `+0xAA`  | (wstr, u32) x 3  | unknown_aa   | Always `1D1` and 0                                                    |
| `+0xE0`  | byte[48]         | reserved     | Always 0                                                              |
| `+0x110` | wstr[6]          | growth_dice  | Level-up bonus dice: HP, stamina, then four movement stats (Notes)    |
| after    | byte[32]         | reserved     | Always 0                                                              |

Every byte from `+0x0E` to `+0xA9` that the table leaves out is 0 in every
record on client 3464.

## Enum Values

`stats` follows `CppEnums.ServantStatType`, the order
[sailstatdata.bss](masterystatdata_bss.md) uses for its eight values:

| Index | Offset  | Name                  | Values on client 3464                  |
| ----- | ------- | --------------------- | -------------------------------------- |
| 0     | `+0x8A` | `Type_Acceleration`   | 200,000 to 2,000,000                   |
| 1     | `+0x8E` | `Type_MaxMoveSpeed`   | 200,000 to 2,000,000                   |
| 2     | `+0x92` | `Type_CorneringSpeed` | 200,000 to 2,000,000                   |
| 3     | `+0x96` | `Type_BrakeSpeed`     | 200,000 to 2,000,000                   |
| 4     | `+0x9A` | `Type_CannonCoolTime` | Always 0                               |
| 5     | `+0x9E` | `Type_CannonAccuracy` | Always 0                               |
| 6     | `+0xA2` | `Type_MaxLength`      | Always 0                               |
| 7     | `+0xA6` | `Type_MaxAngle`       | Always 0                               |

## Suggested UI Layout

| Column       | Type | Notes                                         |
| ------------ | ---- | --------------------------------------------- |
| Character ID | num  | `character_id`                                |
| Name         | text | `name`: LOC type 6 name, else the number      |
| Level        | num  | `level`                                       |
| EXP          | num  | `exp`                                         |
| HP           | num  | `max_hp`                                      |
| Stamina      | num  | `max_mp`                                      |
| Weight       | num  | `max_weight / 10000`, `LT`                    |
| Accel.       | num  | `acceleration` (`stats[0]`) / 10000, one decimal, `%` |
| Speed        | num  | `speed` (`stats[1]`) / 10000, one decimal, `%` |
| Turn         | num  | `turn` (`stats[2]`) / 10000, one decimal, `%`  |
| Brake        | num  | `brake` (`stats[3]`) / 10000, one decimal, `%` |
| HP Dice      | text | `hp_dice`: `growth_dice[0]`, `-` when empty   |
| Stamina Dice | text | `stamina_dice`: `growth_dice[1]`, `-` when empty |
| Movement Dice | text | `move_dice`: `growth_dice[2]`, or slots 2 to 5 joined when they differ |

## Notes

- The stable window (`panel_dialog_servantinfo_all_1.luac`, decompiled with
  unluac) shows the four speed stats as
  `servantInfo:getStat(CppEnums.ServantStatType.Type_*) / 10000` with one
  decimal and `%`, so `1375000` reads 137.5%. On every horse the first two
  values are equal and so are the last two; only eleven ships differ
  (Epheria Galleon, Improved Galley, Panokseon, the four Epheria Carracks and
  four rowboats), so the data cannot check the acceleration and speed order,
  which follows the enum.
- On client 3464, 401 of the 418 servants keep the same `stats` on every
  level from 1, and `max_hp`, `max_mp` and `max_weight` grow from level 1 to
  level 30 (312 servants grow all three, 4 keep `max_mp`). On 159 of the 161
  servants with levels 0 to 100, levels 31 to 100 repeat the level 30 values
  of the three.
- I checked the HP, stamina, weight and dice readings on a level 30 Mythical
  Arduanatt (every Arduanatt and Mythical Arduanatt row holds the same values
  and `1D13` x 6, client 3464). The Detailed Stats window shows inherent
  weight 180 LT and current and max 209 LT, the level 1 and level 30
  `max_weight`. The last level-up added HP 1,145, stamina 547 and weight
  1 LT; the table steps from level 29 to 30 are 1,140, 540 and 1 LT, so HP
  and stamina got a roll of 5 and 7 on top and weight none. Speed, Accel.,
  Turn and Brake grew 1.0%, 1.3%, 1.0% and 1.2%, rolls of 10, 13, 10 and 12
  in 0.1% steps, while `stats` stays the same. The max column is the table
  plus 13 on each of the 29 level-ups: HP 36,077 is 35,200 + 500 + 377 and
  stamina 19,578 is 19,200 + 1 + 377, where 500 and 1 are this horse's
  inherent HP 2,640 and stamina 3,541 above the level 1 row; speed and accel
  175.2% and turn and brake 160.2% are 137.5% and 122.5% + 37.7%.
- The Growth Calculator (`panel_dialog_servantsimulator_2.luac`) gives the
  same horse at levels 1, 5 and 10 an HP increase of 1,141 to 1,153 and a
  stamina increase of 541 to 553, 13 values at 7.6923% (1/13) each: the table
  step (1,140 and 540 on every Arduanatt level from 1 to 30) plus a uniform
  `1D13`. The four movement stats show 0.4% to 1.3% in ten steps of 10% with
  Training Artisan 7 selected. The top is the `1D13` maximum; the floor is a
  Training level bonus, since the Lua reads each movement minimum twice
  through `getVariedStat_MinMax(type, isMin, level + 1, applyBonus,
  lifeLevel)`, with and without the bonus, and the HP and stamina minimums
  stay at step + 1. The bonus is `add_servant_stat_rate` of
  [traininglevelskillstat.bss](traininglevelskillstat_bss.md) (Notes
  below).
- The movement floor rises with Training level and every value from the
  floor to the die maximum stays equally likely. The floor die value is
  `1 + round(die max x add_servant_stat_rate / 1,000,000)`. I checked it in
  the calculator on a `1D13` Mythical Arduanatt and a `1D10` tier 6 horse
  (`add_servant_stat_rate` from client 3464):

  | Horse         | Training  | Rate    | Die max x rate | Range shown           |
  | ------------- | --------- | ------- | -------------- | --------------------- |
  | `1D13`        | Artisan 2 | 192,000 | 2.496          | 0.3 to 1.3, 9.0909%   |
  | `1D13`        | Artisan 7 | 214,000 | 2.782          | 0.4 to 1.3, 10%       |
  | `1D13`        | Master 10 | 273,500 | 3.556          | 0.5 to 1.3, 11.1111%  |
  | `1D10`        | Artisan 7 | 214,000 | 2.14           | 0.3 to 1.0, 12.5%     |
  | `1D10`        | Master 10 | 273,500 | 2.735          | 0.4 to 1.0, 14.2857%  |

  Artisan 2 on the `1D13` horse sits just under a rounding boundary, which
  rules out rounding up; the `1D10` horse rules out a fixed 13.
- The tier 6 horse matches the tier 6 rows with 121% in all four movement
  stats (for example character 9815): HP steps of 630 and stamina steps of
  400, so the calculator's 631 to 640 and 401 to 410 are step + `1D10`.
- `growth_dice` slot 1 is stamina: Giorga Viento (9894) has `1D1-1` (0)
  there and a `max_mp` of 999 on every level. `1D1-1` x 6 is also the level 0
  value, and 93 level 0 rows hold six empty strings.
- The EXP bar is `getExp_s64() / getNeedExp_s64()`, so the EXP restarts on
  every level, as in [nodeexperience](nodeexperience_bss.md); `exp` reads as
  that need. It never falls with level on the 416 servants with all levels.
  Level 0 holds 100 or 1 and is a placeholder like `experience.bss` level 0.
- Level counts on client 3464: 161 servants with levels 0 to 100, 132 with
  0 to 30, 95 with 0 to 1, 20 with 0 to 15, 3 with 0 to 10, 2 with 0 to 20
  and 5 with level 0 only. Traveler's Horse (31560) and Doom's Shadow (31577)
  have only levels 0 and 30.
- The six dice are equal on most rows (`1D10` x 6 on 4,943 rows on client
  3464, Doom `1D13` x 6). Beginner's Brown Horse (9001) has
  `1D5, 1D5, 1D3, 1D3, 1D3, 1D3` and Giorga Viento (9894)
  `1D5, 1D1-1, 1D1, 1D1, 1D1, 1D1`. On 331 of the 413 servants with levels
  from 1 every level holds one dice set.
- The parser is `_dbss/servantexperience/parser.py`. The handler splits
  `stats` into `acceleration`, `speed`, `turn`, `brake` and the four
  `cannon_stats`, keeps the three `1D1` strings as `unknown_aa` and their
  u32s as `unknown_aa_values`, and the offset table splits each key into
  `character_id` and `level`.
- Record `+0x0A` is the start of the `experience.bss` stat body: `+0x0E` is
  body `+0x04`, `+0x42` body `+0x38`, `+0x6E` body `+0x64` and `+0xAA` body
  `+0xA0`. The `5` at `+0x42` has no counterpart in `experience.bss`, whose
  body `+0x38` is 0. `max_hp`, `max_mp` and `max_weight` are body `+0x04`,
  `+0x08` and `+0x48`; `characterstatic.dbss` sets body `+0x48` to values
  such as `100000` and `10000000`.
- The three `1D1` strings at `+0xAA` sit where the `experience.bss` body has
  three always-0 u32 pairs, and string index 0 of that file is `1D1`.

## Open Questions

### Which Dice Rolls Which Movement Stat

`growth_dice` slots 2 to 5 roll the four movement stats, but the four are
equal on every servant on client 3464, so the data cannot tie a slot to
acceleration, speed, turn or brake. The `stats` order would put
acceleration first.

### The Inherent HP and Stamina Offset

Both checked horses start 500 HP and 1 stamina above their level 1 row:
the Mythical Arduanatt at 2,640 and 3,541 against 2,140 and 3,540, the tier
6 horse at 2,130 and 3,401 against 1,630 and 3,400. Their maximums carry the
same offset. Nothing in this record holds 500 or 1, so where the offset
comes from is open.

### The Constant Fields

`unknown_2a`, `unknown_42`, `unknown_5a`, `unknown_6e` and `unknown_7a` are
the `experience.bss` constant fields. The `5` and `10` triads are likely
speed ranks and their limits; the evidence is in the
[experience.bss](experience_bss.md#the-constant-fields) Open Questions.
