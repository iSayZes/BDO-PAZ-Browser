# `employeestaticstatus.bss` Format

## Purpose

Static stats of every hireable ship crew member: one row per sailor per level, then one row per First Mate. Each row names the character whose name, title and portrait the sailor uses, and carries up to 19 ability values such as the ship stat bonuses shown in the Manage Sailors window.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records                         | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ------ | ------------------------------- | --------- |
| 2      | 3473 and later | 3474    | `employeestaticstatus.bss` | 33,465 | 4,484 Ability, 236 Employee Row | 5         |
| 1      | 1784           | 1784    | `employeestaticstatus.bss` | 29,799 | 3,910 Ability, 230 Employee Row | 5         |

| Layout | File                       | Known            | Unknown        |
| ------ | -------------------------- | ---------------- | -------------- |
| 2      | `employeestaticstatus.bss` | 31,985 B (95.6%) | 1,480 B (4.4%) |
| 1      | `employeestaticstatus.bss` | 28,379 B (95.2%) | 1,420 B (4.8%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Name (LOC type `6`, `str_id4=0`) and title (`str_id4=1`) per character; without one the Korean `characterstatic.dbss` name and title show |
| `stringtable.bss`     | Optional | Key hashes of the First Mate skill texts (`LUA_CAPTAIN_SAILOR_PRESET_SKILL_DESC_*`, LOC type `37`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                 | Type                             | Field                         | Notes                                                            |
| ---------------------- | -------------------------------- | ----------------------------- | ---------------------------------------------------------------- |
| `+0x00`                | char[4]                          | magic                         | `PABR`                                                           |
| `+0x04`                | u32                              | sailor_count                  | Rows in the sailor list; observed `230` (23 sailors x 10 levels) |
| `+0x08`                | Employee Row[sailor_count]       | sailor_rows                   | Employee Row, `job` `0`                                          |
| `sailor_rows+0x00`     | u32                              | first_mate_count              | Rows in the First Mate list; observed `6`                        |
| `sailor_rows+0x04`     | Employee Row[first_mate_count]   | first_mate_rows               | Employee Row, `job` `1`, level `1` only                          |
| `first_mate_rows+0x00` | u32[16]                          | unknown_after_first_mate_rows | Sixteen u32 values, see Open Questions                           |
| `first_mate_rows+0x40` | String Table                     | string_table                  | Counted icon paths, the shared PABR tail                         |
| `string_table+0x00`    | u32                              | table_start                   | String table offset                                              |
| `string_table+0x04`    | u32                              | zero                          | `0`                                                              |

The string table is the same tail as in `npcsimply.bss` and `exploration.bss`: `u32 count`, then per entry `u8 is_wide`, `u32 byte_length` and the text (UTF-16LE when wide). All 29 observed entries are wide icon paths such as `Icon/New_Icon/11_Employee/Employee_59228.dds`. The parser checks that the two lists plus the 64-byte block end exactly where the trailer says the string table starts.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of entries   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

### Employee Row (130 bytes)

| Offset  | Type          | Field          | Notes                                                                 |
| ------- | ------------- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u8            | job            | `0` Sailor, `1` First Mate, see Job                                   |
| `+0x01` | u16           | level          | `1` to `10` for sailors, `1` for First Mates                          |
| `+0x03` | u16           | employee_key   | Sailor type, `1` to `29`; with `level` the row key                    |
| `+0x05` | Ability[19]   | abilities      | Ability slots: type, value. See Abilities                             |
| `+0x64` | u32           | weight         | Weight in 1/10,000 LT (`2,000,000` = 200 LT), same at every level     |
| `+0x68` | u32           | cabin_cost     | Cabin Cost, `3` to `13` for sailors, `0` for First Mates              |
| `+0x6C` | u32           | appetite       | Appetite, `80`, `100`, `120` or `150`, same at every level            |
| `+0x70` | u32           | max_condition  | Condition (max), grows with level (sailor 23: `46` at level 1 to `100` at level 10) |
| `+0x74` | u32           | unknown_74     | Always `5`                                                            |
| `+0x78` | u32           | icon_index     | Zero-based index into the string table                                |
| `+0x7C` | u16           | character_id   | Character key: LOC type 6 name/title, and the portrait file name      |
| `+0x7E` | u16           | employee_key_dup | Repeats `+0x03`; the parser rejects a row where it differs          |
| `+0x80` | u16           | unknown_80     | Always `0`                                                            |

The client Lua reads a sailor's key through `getEmployeeKey()`, and that key object answers `getLevel()`, so `employee_key` and `level` together are the client's employee key.

### Ability (5 bytes)

Each of the 19 slots is `u8 type` followed by `u32 value`.

| Offset  | Type | Field | Notes                    |
| ------- | ---- | ----- | ------------------------ |
| `+0x00` | u8   | type  | Ability type, see Abilities |
| `+0x01` | u32  | value | The type's value         |

## Layout 1

On client 1784 a row holds 17 ability slots, so it is 120 bytes and every
field after `abilities` sits 10 bytes earlier. The file has no First Mate
list, and the block before the string table holds 10 u32 values in place of
16. The File Layout and the Employee Row differ from Layout 2.

### File Layout

| Offset                 | Type                       | Field                         | Notes                                                       |
| ---------------------- | -------------------------- | ----------------------------- | ----------------------------------------------------------- |
| `+0x00`                | char[4]                    | magic                         | `PABR`                                                      |
| `+0x04`                | u32                        | sailor_count                  | `230` on client 1784                                        |
| `+0x08`                | Employee Row[sailor_count] | sailor_rows                   |                                                             |
| `sailor_rows+0x00`     | u32[10]                    | unknown_after_first_mate_rows | `5, 0, 5, 0, 300000, 1, 0, 50, 0, 1000` on client 1784: the first 10 values of the Layout 2 block, with `50` in place of `59`; client 1784 has no `first_mate_rows`, the name follows Layout 2 |
| `sailor_rows+0x28`     | String Table               | string_table                  |                                                             |
| `string_table+0x00`    | u32                        | table_start                   |                                                             |
| `string_table+0x04`    | u32                        | zero                          |                                                             |

### Employee Row (120 bytes)

| Offset  | Type        | Field            | Notes |
| ------- | ----------- | ---------------- | ----- |
| `+0x00` | u8          | job              |       |
| `+0x01` | u16         | level            |       |
| `+0x03` | u16         | employee_key     |       |
| `+0x05` | Ability[17] | abilities        |       |
| `+0x5A` | u32         | weight           |       |
| `+0x5E` | u32         | cabin_cost       |       |
| `+0x62` | u32         | appetite         |       |
| `+0x66` | u32         | max_condition    |       |
| `+0x6A` | u32         | unknown_74       |       |
| `+0x6E` | u32         | icon_index       |       |
| `+0x72` | u16         | character_id     |       |
| `+0x74` | u16         | employee_key_dup |       |
| `+0x76` | u16         | unknown_80       |       |

## Abilities

Every observed row has the same types in the same slots:

```text
slot: 0 1 2 3 4  5 6 7 8 9 10 11 12 13 14 15 16 17 18
type: 0 1 2 3 19 4 6 7 8 9 5  19 19 13 14 15 16 17 18
```

Type `19` fills three slots and is always `0`; it is one past the highest type in use and reads as unused. Types `10` to `12` never appear. The table shows only non-zero slots, as `type: value`.

Observed use of each type:

| Type     | Rows with a value                                  | Meaning                                                                 |
| -------- | -------------------------------------------------- | ----------------------------------------------------------------------- |
| `0`-`5`  | none                                               | Unknown; the four resists are candidates                                |
| `6`      | every sailor, `2,000` to `20,000`                  | Endurance (ship Speed); never set on First Mates                        |
| `7`      | every sailor, `2,000` to `16,000`                  | Wits (Acceleration)                                                     |
| `8`      | every sailor, `2,000` to `40,000`                  | Awareness (Turn)                                                        |
| `9`      | every sailor, `2,000` to `40,000`                  | Strength (Brake)                                                        |
| `13`     | none                                               | Patience (cannon reload time); no sailor has it                         |
| `14`     | sailors 5, 8, 15 and 20                            | Focus (cannon accuracy)                                                 |
| `15`     | sailors 5, 8, 15 and 20                            | Force (cannon range)                                                    |
| `16`     | sailors 5, 8, 15 and 20                            | Vision (cannon angle)                                                   |
| `17`     | First Mate Cleia (`62167`), `100,000`              | Parley reduction for bartering, per million: 10%                        |
| `18`     | First Mate Tranan Underfoe (`62168`), `1`          | Ship auto-repair, a flag                                                |

The labels are the Manage Sailors window's (English client), in its order: Endurance, Wits, Awareness, Strength, then the cannon stats Patience, Focus, Force and Vision. Types `6` to `9` and `13` to `16` follow that order. The window Lua fills them from `_speed`, `_accel`, `_turning`, `_break`, `_cannonCoolTime`, `_cannonAccuracy`, `_cannonMaxLength` and `_cannonMaxAngle`, in that order, which gives the cannon stats their meaning. The client keys confirm the order: `PANEL_SAILORMANAGER_SPEED` reads Endurance, `_ACCELATION` Wits, `_CORNERING` Awareness and `_BRAKING` Strength. Type `13` is read as Patience from its place in that order only, since no row sets it. Condition is `PANEL_SAILORMANAGER_LOYALTY` (the Lua reads it through `getMaxLoyalty()`); the window shows it as a bar, `80 / 80`.

The sailor Lua (`panel_window_sailorpresetmanager_all`) picks the First Mate skill text by character key: `62167` shows `LUA_CAPTAIN_SAILOR_PRESET_SKILL_DESC_02` "-10% Parley required for Bartering", `62168` shows `_03` "Auto-repairs ship (requires materials in ship's inventory)" and `62169` (Proix) shows `_01` "Use a slightly improved BreezySail". Cleia's `17: 100000` is that 10%, and Tranan's `18: 1` the switch; Proix has no ability value, so the improved skill lives elsewhere.

The same Lua shows each ship stat as `value x 0.0001` with one decimal and a `%` sign (`string.format("%.1f", _speed * 0.0001) .. "%"`), so a `16000` speed value reads `1.6%`.

## Job

`job` is `0` on all 230 rows of the first list and `1` on all 6 rows of the second. The second list holds exactly the characters whose LOC title is `<First Mate>` (`62167` to `62169`; `62170` to `62172` have no LOC name yet), and the Lua compares `getJob()` with `__eEmployeeJob_ViceCaptain` to mark First Mates. The labels follow the client's `PANEL_SAILORMANAGER_VICECAPTAIN` ("First Mate").

## Reference Rows

| Sailor ID | Level | Character ID | Name            | Title            | Role       | Icon                  |
| --------- | ----- | ------------ | --------------- | ---------------- | ---------- | --------------------- |
| `1`       | 1     | `59053`      | Sailor          | `<Ambitious>`    | Sailor     | `Employee_59053.dds`  |
| `21`      | 1     | `59101`      | Arkahn          | `<Prepared>`     | Sailor     | `Employee_59101.dds`  |
| `23`      | 1     | `59228`      | Pacuna          | `<Always Happy>` | Sailor     | `Employee_59228.dds`  |
| `24`      | 1     | `62167`      | Cleia           | `<First Mate>`   | First Mate | `Employee_62167.dds`  |
| `25`      | 1     | `62168`      | Tranan Underfoe | `<First Mate>`   | First Mate | `Employee_62168.dds`  |

Sailors `1` to `20` share the LOC name "Sailor"; their title is the sailor type the Sailor Preset filter lists (`LUA_SAILOR_PRESET_CATEGORY_FILTER_01` "Ambitious" and on).

## Notes

- Observed decompressed size is `33,465` bytes (client 3458).
- The sailor list runs level by level: all 23 sailors at level 1, then all at level 2, up to level 10. Inside a level the order is keys `23` down to `8`, then `1` to `7`; from level 5 on, key `7` comes right after `8`.
- `icon_index` runs `0` to `28` in the order of the string table, and every icon file is named after the row's character: `Employee_<character_id>.dds` under `ui_texture/icon/new_icon/11_employee/`.
- Ability values do not change with level on any row; only `max_condition` does.
- `employee_key` is not an `employeename.dbss` ID: those 60 names are given names, and nothing ties name `1` (Philav) to sailor `1`.
- The Manage Sailors window reads, besides the ship stats, `getCost()` (Cabin Cost), `getFoodConsume()` (Appetite), `getBodyWeight()` (Weight, formatted by `makeWeightString`), `getMaxLoyalty()` (Condition) and the four resist values (`Resist_Food`, `Resist_Loyalty`, `Resist_OceanCurrent`, `Resist_WindDirection`). The resists are the candidates for the zero ability types.
- Checked in game (2026-10-06):
  - Pacuna (`23`) at level 1: Condition 46, Appetite 80, Cabin Cost 5, Weight 100 LT, Endurance 0.5%, Wits 0.5%, Awareness 0.2%, Strength 0.2%, every cannon stat 0.0%. Her row: `max_condition 46`, `appetite 80`, `cabin_cost 5`, `weight 1,000,000`, `6: 5000, 7: 5000, 8: 2000, 9: 2000`.
  - Level 6 Confident (`9`) and Treasure-Seeking (`7`) sailors: Condition 110, Appetite 100, Cabin Cost 5, Weight 300 LT, as their level 6 rows read. Their ship stats are the level 1 base plus the `employeeexp.bss` growth rolls (see that doc), so the ability values here are base values.
  - Quick Sailor (`5`) at level 1: Condition 80, Appetite 100, Cabin Cost 10, Weight 250 LT, Endurance 0.2%, Wits 1.5%, Awareness 0.2%, Strength 0.2%, Patience 0.0%, Focus 0.2%, Force 2.0%, Vision 6.0%. Its row: `6: 2000, 7: 15000, 8: 2000, 9: 2000, 14: 2000, 15: 20000, 16: 60000`, which names `14` to `16`.
- The ship stats, Weight, Cabin Cost and Appetite also match the sailor table in GrumpyG's [BDO Sailors Guide](https://grumpygreen.cricket/bdo-sailors-guide/), which lists each plain sailor by title. All 20 match on Speed, Acceleration, Turn, Brake, Weight and Cabin Cost; Appetite matches on 19; the guide gives Treasure-Seeking (`7`) 110, but the game shows 100, as this file does. The guide's titles map to keys as: Ambitious `1`, Diligent `2`, Innocent `3`, Enamored `4`, Quick `5`, Calculating `6`, Treasure-Seeking `7`, Realistic `8`, Confident `9`, Tenacious `10`, Honest `11`, Tough `12`, Strong `13`, Experienced `14`, Curious `15`, Dreaming of a Full Haul `16`, Powerful `17`, Born-in-the-Sea `18`, Smart `19`, Quick-Witted `20`.

## Open Questions

### Field `unknown_74`

`5` on every row; nothing in the window matches it yet.

### The 64-Byte Block

Between the First Mate list and the string table sit sixteen u32 values: `5, 0, 5, 0, 300000, 1, 0, 59, 0, 1000, 5000, 2, 10000, 3, 10, 180`. They may be crew-wide constants such as recovery amounts or fishing timers; no reader in the sailor Lua points at them.
