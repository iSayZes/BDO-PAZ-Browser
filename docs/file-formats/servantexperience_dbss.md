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
| `+0x02`  | i32              | level        | 0 to the servant's top level                                          |
| `+0x06`  | u64              | exp          | EXP from `level` to `level + 1` (Notes)                               |
| `+0x0E`  | f32              | max_hp       | Max HP, shown as is; `1.0` at level 0                                 |
| `+0x12`  | u32              | max_mp       | Max stamina (`getMaxMp()`), shown as is; 0 on ships; `1` at level 0   |
| `+0x2A`  | f32              | unknown_2a   | `1.0` at level 0, else 0                                              |
| `+0x42`  | u32              | max_critical_rate | Always `5`                                                       |
| `+0x46`  | u32              | max_drop_item_luck | Always `5`                                                      |
| `+0x4A`  | u32              | max_fishing_luck | Always `5`                                                        |
| `+0x4E`  | u32              | max_collection_luck | Always `5`                                                     |
| `+0x52`  | i64              | max_weight   | Max weight, LT x 10,000; 0 at level 0                                 |
| `+0x5A`  | f32              | unknown_5a   | Always `1.0`                                                          |
| `+0x6E`  | u32[3]           | max_varied_speed | Always `10, 10, 10`: attack, movement and casting speed limits (Field Names) |
| `+0x7A`  | f32              | unknown_7a   | `1.0` at level 0, else 0                                              |
| `+0x8A`  | u32[8]           | stats        | By `ServantStatType` (Enum Values), percent x 10,000                  |
| `+0xAA`  | (wstr, u32) x 3  | unknown_aa, unknown_aa_values | Always `1D1` and 0; the parser keeps the strings as `unknown_aa` and the u32s as `unknown_aa_values` |
| `+0xE0`  | byte[48]         | reserved     | Always 0                                                              |
| `+0x110` | wstr[6]          | growth_dice  | Level-up bonus dice: HP, stamina, acceleration, speed, cornering, brake (Notes) |
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
  four rowboats). The bexcel `Servant_Table` settles the acceleration and
  speed order: on the 8 ships where its `AccelerationRate` and
  `MaxMoveSpeedRate` differ, `+0x8A` holds the first and `+0x8E` the second
  (see Field Names).
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

## Field Names

The names follow the `Servant_Table` sheet of a private-server `DataSheets.bexcel` (9,893 (character, level) rows shared with client 3473) and the BdoEmu server's `Servant_Table` (about 2021, 7,241 rows), matched value by value at every offset of the fixed part:

| Column | Field | Equal (bexcel) | Equal (BdoEmu) |
| ------ | ----- | -------------- | -------------- |
| `RequireEXP` | `exp` | 9,887 | 7,235 |
| `HP` | `max_hp` | 9,549 | 6,914 |
| `MP` | `max_mp` | 9,181 | |
| `possessableWeight` | `max_weight` (i64) | 9,879 | 7,225 |
| `AccelerationRate` | `stats[0]` | 9,891 | 7,148 |
| `MaxMoveSpeedRate` | `stats[1]` | 9,891 | 7,148 |
| `CorneringSpeedRate`, `BrakeSpeedRate` | `stats[2]`, `stats[3]` | 9,891 | 7,148 |

`AccelerationRate` equals `stats[1]` on 8 fewer rows than `stats[0]`, and `MaxMoveSpeedRate` the other way round: the 8 ships 9032, 9049, 9050 and 9075 (the four rowboats) and 31054 to 31057 (the four Epheria Carracks) have a lower acceleration than speed in both. `CorneringSpeedRate` and `BrakeSpeedRate` are equal on every row and keep the enum order.

The constants are placed by value: the sheet's only columns that hold `5` on every row are `MaxCriticalRate`, `MaxDropItemLuck`, `MaxFishingLuck` and `MaxCollectionLuck`, the four u32 at `+0x42`, and its only `10` columns are `MaxAttackSpeed`, `MaxMoveSpeed` and `MaxCastingSpeed`, the three at `+0x6E`. The 2016 client (build of 2016-01-11) ships with debug symbols; its `gc::CharacterStatStaticStatus` holds `_maxCriticalHitPoint`, `_maxDropItemPoint`, `_maxFishingPoint` and `_maxCollectionPoint` in that order, which splits the four `5`s, and `_maxVariedSpeedPoint` as one array of three. Which index of `max_varied_speed` is attack, movement or casting is not settled by the data; the [experience.bss](experience_bss.md#the-max_varied_speed-order) Open Questions hold the character window Lua lead.

`growth_dice` follows the sheet columns `VariedMaxHP`, `VariedMaxMP`, `VariedAccelerationRate`, `VariedMaxMoveSpeedRate`, `VariedCorneringSpeedRate` and `VariedBrakeSpeedRate`, and the 2016 `_variedMaxHp`, `_variedMaxMp` and `_variedStat[4]`, which the 2016 `LoadServantExperienceStaticInformation` reads from those columns in that order. The bexcel holds `0` in all six columns and the private server's own file `1D1`, so only the order ties the four movement slots to their stats; client 3473 rolls the same die in all four on every servant.

The private server's own `servantexperience.dbss` (client 1784, 10,869 records) stores the sheet's `StunGauge` (`100`) as an i16 at `+0x16`, after `max_mp` as in the 2016 `_stunGauge`, and every later field 2 bytes further on. Client 3473 has no such field: `+0x16` starts the zero bytes before `unknown_2a`.

`level` is an i32, the 2016 `_level`; its high half (`+0x04`, earlier `unknown_04`) is 0 on every record.

## Open Questions

### The Inherent HP and Stamina Offset

Both checked horses start 500 HP and 1 stamina above their level 1 row:
the Mythical Arduanatt at 2,640 and 3,541 against 2,140 and 3,540, the tier
6 horse at 2,130 and 3,401 against 1,630 and 3,400. Their maximums carry the
same offset. Nothing in this record holds 500 or 1, so where the offset
comes from is open.

### The Constant Fields

`unknown_2a`, `unknown_5a` and `unknown_7a` are `experience.bss` constant fields with no sheet match. `unknown_5a` (`1.0` on every record) sits where the 2016 member order has `_productionHit`, but the bexcel and BdoEmu `ProductionHit` columns hold `0` on every row, and client 1784 stores `1.0` there too, so the value does not come from that column. `unknown_2a` and `unknown_7a` are `1.0` on level 0 and `0` otherwise; no sheet column has that pattern.
