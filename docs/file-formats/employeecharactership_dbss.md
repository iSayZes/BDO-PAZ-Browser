# `employeecharactership.dbss` Format

## Purpose

Ship settings per boat character: one row per rowboat, raft, sailboat,
frigate, caravel, galleass, carrack and guild galley with its sailor limit,
the number of sailor positions, its rations, the ration and cannonball
recovery values, the cannon and ship skill bar flags and the manual cannon
fire setup. The client Lua reads it through
`ToClient_EmployeeCharacterShipStaticStatusWrapper(characterKey)`.
Companion `employeecharactershipoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records       | Row bytes                |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------- | ------------------------ |
| 2      | 3474 and later | 3474    | `employeecharactership.dbss`       | 3,348 | 38 Ship Row   | 76 to 114, 88 on average |
| 2      | 3474 and later | 3474    | `employeecharactershipoffset.dbss` | 384   | 38 Offset Row | 10                       |
| 1      | 1784           | 1784    | `employeecharactership.dbss`       | 3,446 | 36 Ship Row   | 84 to 122, 96 on average |
| 1      | 1784           | 1784    | `employeecharactershipoffset.dbss` | 364   | 36 Offset Row | 10                       |

| Layout | File                               | Known           | Unknown       |
| ------ | ---------------------------------- | --------------- | ------------- |
| 2      | `employeecharactership.dbss`       | 3,044 B (90.9%) | 304 B (9.1%)  |
| 2      | `employeecharactershipoffset.dbss` | 384 B (100.0%)  | 0 B (0.0%)    |
| 1      | `employeecharactership.dbss`       | 2,870 B (83.3%) | 576 B (16.7%) |
| 1      | `employeecharactershipoffset.dbss` | 364 B (100.0%)  | 0 B (0.0%)    |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                                 |
| ------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| `employeecharactershipoffset.dbss`                | Optional | `character_key -> (data_offset, data_size)` of every row; the rows sit back to back and can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Ship names come from LOC type 6, `str_id1` = `character_key`, `str_id4` 0
("Epheria Caravel" for `31048`).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type            | Field | Notes                                         |
| ------- | --------------- | ----- | --------------------------------------------- |
| `+0x00` | u32             | count | Number of rows; `38` on client 3474           |
| `+0x04` | Ship Row[count] | rows  | Back to back to the end of the file; see Ship Row |

### Ship Row (variable: 76 bytes + condition text)

| Offset    | Type  | Field                                           | Notes                                                                 |
| --------- | ----- | ----------------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`   | u16   | character_key                                   | Boat character; unique per row, the index key                         |
| `+0x02`   | u32   | employee_max                                    | `0` to `150`; see Notes                                               |
| `+0x06`   | u32   | employee_spawn_count                            | `0`, `1`, `3` or `5`; see Notes                                       |
| `+0x0A`   | u32   | food_max                                        | `10000` to `3000000`                                                  |
| `+0x0E`   | u32   | ocean_ship_cannon_setup                         | `0` to `2000`; `0` on boats without cannons                            |
| `+0x12`   | f32   | ship_food_recovery                              | `0` to `5.0`; see Notes                                               |
| `+0x16`   | f32   | ship_cannon_recovery                            | `0` or `1000`; see Notes                                              |
| `+0x1A`   | f32   | damage_diagram_restoration_cost                 | Whole numbers from `100000` to `100000000`, `0` on boats without cannons |
| `+0x1E`   | u32   | unknown_1e                                      | `0` on every row; see Open Questions                                  |
| `+0x22`   | u32   | unknown_22                                      | `0` on every row; see Open Questions                                  |
| `+0x26`   | u8    | is_summon_full                                  | `0` or `1`                                                            |
| `+0x27`   | u8    | new_cannon_ship_ui                              | `0` or `1`                                                            |
| `+0x28`   | u8    | new_cannon_count                                | `0` to `18`                                                           |
| `+0x29`   | f32   | new_cannon_speed                                | Whole numbers from `10` to `17`, `0` on boats without cannons          |
| `+0x2D`   | u8    | ocean_ship_skill_ui                             | `0` or `1`                                                            |
| `+0x2E`   | u8    | manual_cannon_fire                              | `0` or `1`                                                            |
| `+0x2F`   | f32   | manual_cannon_fire_min_length                   | `0` or `3000`                                                         |
| `+0x33`   | f32   | manual_cannon_fire_max_length                   | `0`, `15000` or `20000`                                               |
| `+0x37`   | f32   | manual_cannon_fire_random_dist                  | `0` or `300`                                                          |
| `+0x3B`   | f32   | manual_cannon_fire_random_pos                   | `0` or `100`                                                          |
| `+0x3F`   | u32   | manual_cannon_fire_max_angle                    | `0` or `10`                                                           |
| `+0x43`   | u8    | manual_cannon_fire_decrease_cool_time           | `0` or `1`                                                            |
| `+0x44`   | str16 | manual_cannon_fire_decrease_cool_time_condition | Condition script, `getlifelevel(9)>80;` or empty; see Notes           |

The value ranges are from client 3474. A row with an empty condition is
76 bytes, one with `getlifelevel(9)>80;` 114 bytes. The rows are sorted
neither by key nor in index order.

### `employeecharactershipoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `employeecharactership.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                               |
| ------- | ---- | ------------- | --------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                         |
| `+0x02` | u32  | data_offset   | Absolute offset of the row start, at `character_key` |
| `+0x06` | u32  | data_size     | Row size in bytes, key included                     |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in neither key nor file order (9048, 9032, 9096, 31048 on client
3474); on clients 1784 and 3474 every index row points at the row with its
key and covers it exactly.

## Layout 1

### Ship Row (variable: 84 bytes + condition text)

| Offset                                                 | Type  | Field                                           | Notes                                       |
| ------------------------------------------------------ | ----- | ----------------------------------------------- | ------------------------------------------- |
| `+0x00`                                                | u16   | character_key                                   | Boat character                              |
| `+0x02`                                                | u32   | employee_max                                    |                                             |
| `+0x06`                                                | u32   | employee_spawn_count                            |                                             |
| `+0x0A`                                                | u32   | food_max                                        |                                             |
| `+0x0E`                                                | u32   | ocean_ship_cannon_setup                         |                                             |
| `+0x12`                                                | f32   | ship_food_recovery                              |                                             |
| `+0x16`                                                | f32   | ship_cannon_recovery                            |                                             |
| `+0x1A`                                                | f32   | damage_diagram_restoration_cost                 |                                             |
| `+0x1E`                                                | u32   | unknown_1e                                      | `0` on every row (client 1784)              |
| `+0x22`                                                | u32   | unknown_22                                      | `0` on every row (client 1784)              |
| `+0x26`                                                | u8    | is_summon_full                                  |                                             |
| `+0x27`                                                | u8    | new_cannon_ship_ui                              |                                             |
| `+0x28`                                                | u8    | new_cannon_count                                |                                             |
| `+0x29`                                                | f32   | new_cannon_speed                                |                                             |
| `+0x2D`                                                | u8    | ocean_ship_skill_ui                             |                                             |
| `+0x2E`                                                | u8    | manual_cannon_fire                              |                                             |
| `+0x2F`                                                | f32   | manual_cannon_fire_min_length                   |                                             |
| `+0x33`                                                | f32   | manual_cannon_fire_max_length                   |                                             |
| `+0x37`                                                | f32   | manual_cannon_fire_random_dist                  |                                             |
| `+0x3B`                                                | f32   | manual_cannon_fire_random_pos                   |                                             |
| `+0x3F`                                                | u32   | manual_cannon_fire_max_angle                    |                                             |
| `+0x43`                                                | u8    | manual_cannon_fire_decrease_cool_time           |                                             |
| `+0x44`                                                | str16 | manual_cannon_fire_decrease_cool_time_condition |                                             |
| `manual_cannon_fire_decrease_cool_time_condition+0x00` | f32   | unknown_tail_00                                 | Equal to `ship_food_recovery` on every row  |
| `manual_cannon_fire_decrease_cool_time_condition+0x04` | f32   | unknown_tail_04                                 | Equal to `ship_cannon_recovery` on every row |

Every row is 8 bytes longer than in Layout 2: the two f32 after the
condition are gone on client 3474. Client 1784 has 36 rows; client 3474
adds `9124` (Improved Galley) and `31025` (Panokseon).

## Field Names

The row is the `CharacterShip_Setup` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched by `CharacterKey`. All 36 sheet
keys are rows on both clients. The f32 fields hold the sheet's numbers as
floats (`DamageDiagramRestorationCost` `1000000` is `1000000.0`), and an
empty sheet cell is `0` in the file.

| Field                                           | Column                                      | Same value (client 1784) | Same value (client 3474) |
| ----------------------------------------------- | ------------------------------------------- | ------------------------ | ------------------------ |
| employee_max                                    | `EmployeeMax`                               | 29 of 36                 | 29 of 36                 |
| employee_spawn_count                            | `EmployeeSpawnCount`                        | 36 of 36                 | 36 of 36                 |
| food_max                                        | `FoodMax`                                   | 36 of 36                 | 36 of 36                 |
| ocean_ship_cannon_setup                         | `OceanShipCannonSetup`                      | 36 of 36                 | 35 of 36                 |
| ship_food_recovery                              | `ShipFoodRecovery`                          | 36 of 36                 | 35 of 36                 |
| ship_cannon_recovery                            | `ShipCannonRecovery`                        | 36 of 36                 | 36 of 36                 |
| damage_diagram_restoration_cost                 | `DamageDiagramRestorationCost`              | 36 of 36                 | 35 of 36                 |
| is_summon_full                                  | `IsSummonFull`                              | 36 of 36                 | 36 of 36                 |
| new_cannon_ship_ui                              | `NewCannonShipUI`                           | 36 of 36                 | 36 of 36                 |
| new_cannon_count                                | `NewCannonCount`                            | 36 of 36                 | 35 of 36                 |
| new_cannon_speed                                | `NewCannonSpeed`                            | 36 of 36                 | 35 of 36                 |
| ocean_ship_skill_ui                             | `OceanShipSkillUI`                          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire                              | `ManualCannonFire`                          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_min_length                   | `ManualCannonFireMinLength`                 | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_max_length                   | `ManualCannonFireMaxLength`                 | 36 of 36                 | 35 of 36                 |
| manual_cannon_fire_random_dist                  | `ManualCannonFireRandomDist`                | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_random_pos                   | `ManualCannonFireRandomPos`                 | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_max_angle                    | `ManualCannonFireMaxAngle`                  | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_decrease_cool_time           | `ManualCannonFireDecreaseCoolTime`          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_decrease_cool_time_condition | `ManualCannonFireDecreaseCoolTimeCondition` | 36 of 36                 | 36 of 36                 |

The seven `EmployeeMax` misses are the Carracks `31045`, `31054` to `31057`,
`31084` and `31085`: the bexcel holds `50` where the
`DataSheet_EmployeeDataTable.xlsx` sheet of the same private server and
the client 1784 file hold `100`. Client 3474 keeps `100` on `31045` and
raises the other six to `110`. The other client 3474 misses are all
`31020` (Epheria Galleon), retuned after client 1784: cannon setup `1800`
to `2000`, ration recovery `1.25` to `1.5`, restoration cost `100000` to
`100000000`, `12` to `8` cannons, cannon speed `16` to `10` and maximum
fire length `20000` to `15000`.

`NewCannonShipUI` and `ManualCannonFire` hold the same value on every row,
and so do `ManualCannonFireDecreaseCoolTime` and both of them on all but
one row. From `is_summon_full` on, the row keeps the sheet's column order,
which places `new_cannon_ship_ui` at `+0x27` and `manual_cannon_fire` at
`+0x2E`.

The sheet also has `ShipFoodTentRecovery` and `ShipCannonTentRecovery`,
equal to `ShipFoodRecovery` and `ShipCannonRecovery` on every row, so the
values cannot tell the two pairs apart; see Open Questions. The client Lua
names its getters `getRecoveryFoodCount()` and `getRecoveryCannonCount()`,
without the tent. `OceanShipAngle` and `OceanShipWind` are empty in every
row. `ContentsGroupKey` has no place in the row.

## Notes

- The client Lua calls these getters on the wrapper:
  `getEmployeeMaxCost()` (the sailor manager menu of the wharf shows only
  for a ship above `0`, `panel_dialog_servantlist_all_1.luac`),
  `getRecoveryFoodCount()` and `getRecoveryCannonCount()` (the repair and
  supply price is missing rations times the first plus missing cannonballs
  times the second, `panel_dialog_servantlist_all_2.luac`),
  `getIsSummonFull()`, `getOceanShipSkillUI()` (the ship skill bar for the
  captain's seat, `horsemp.luac`), `getCannonCount()` and
  `getCannonReloadSec()` (the ship upgrade window,
  `panel_window_servantupgradeinfo_1.luac`). The Lua does not show which
  field a getter reads; by name, `getEmployeeMaxCost()` is `employee_max`
  and the two recovery getters are `ship_food_recovery` and
  `ship_cannon_recovery`.
- The condition `getlifelevel(9)>80;` tests life type 9, `sail` in
  `CppEnums.LifeExperienceType` (`global_define_cpp_enum.luac`): Sailing
  level above 80. On client 3474 the 12 rows with a condition are the 12
  rows with manual cannon fire lengths.
- `employee_spawn_count` equals the number of rows per `CharacterKey` in the
  `EmployeeShipSpawnPosition_Table` sheet of the same private server (1 for
  the Epheria Sailboat, 3 for the Caravel and Galleass, 5 for the Carracks).
  The client compiles that sheet to
  [`employeeclientspawn.dbss`](employeeclientspawn_dbss.md), where 12 of
  the 13 ships with a count above `0` have that many rows on client 3474;
  the Panokseon (`31025`, count 5) has none.
- On client 3474, 15 rows hold only `food_max` and `is_summon_full`: the
  rowboats, rafts, fishing boats, the three Epheria Cogs and the Trader
  (`9096`). `is_summon_full` is `1` on all of them but the Trader, and on
  the Old Bartali Sailboat (`31015`), and `0` everywhere else.

## Open Questions

### Which Recovery Pair the Live File Keeps

Client 1784 stores four recovery values: one pair at `+0x12` and a second
pair after the condition text. The sheet has `ShipFoodRecovery`,
`ShipCannonRecovery`, `ShipFoodTentRecovery` and `ShipCannonTentRecovery`,
and on every row the tent pair equals the plain pair, in the sheet and in
both clients. Client 3474 dropped the tail pair. The names `ship_food_recovery`
and `ship_cannon_recovery` follow the sheet's column order and the Lua getter
names; a row where the sheet's two pairs differ would confirm which pair sits
where.

### unknown_1e and unknown_22

Both u32 values are `0` on every row of both clients. The sheet's
`OceanShipAngle` and `OceanShipWind` are empty in every row and would compile
to `0`, but nothing ties them to these bytes, and they could be floats.
