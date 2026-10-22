# `siegerevivevalue.bss` Format

## Purpose

One record of Node War and Conquest War revive and liberation options:
revival times, the Conquest War liberation points per fortress, kill and
death, the liberation reward time, the outfit item for entering the
Conquest War and two short-distance revival values. The record grew over
time: clients 1485 and 1636 hold four revival values, client 1784 the
twelve `SiegeOption` columns, and later clients add one or two unnamed
fields at the end.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | -------------- | --------- |
| 5      | 3251 and later | 3482    | `siegerevivevalue.bss` | 97    | 1 String Table | 4         |
| 4      | 2765 to 3002   | 3002    | `siegerevivevalue.bss` | 93    | 1 String Table | 4         |
| 3      | 2313 to 2637   | 2637    | `siegerevivevalue.bss` | 94    | 1 String Table | 4         |
| 2      | 1784 to 2107   | 2107    | `siegerevivevalue.bss` | 92    | 1 String Table | 4         |
| 1      | 1485 to 1636   | 1636    | `siegerevivevalue.bss` | 48    | 1 String Table | 4         |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 5      | `siegerevivevalue.bss` | 92 B (94.8%)  | 5 B (5.2%) |
| 4      | `siegerevivevalue.bss` | 92 B (98.9%)  | 1 B (1.1%) |
| 3      | `siegerevivevalue.bss` | 92 B (97.9%)  | 2 B (2.1%) |
| 2      | `siegerevivevalue.bss` | 92 B (100.0%) | 0 B (0.0%) |
| 1      | `siegerevivevalue.bss` | 48 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 5 |
| 3474   | Layout 5 |
| 3251   | Layout 5 |
| 3002   | Layout 4 |
| 2765   | Layout 4 |
| 2637   | Layout 3 |
| 2519   | Layout 3 |
| 2313   | Layout 3 |
| 2107   | Layout 2 |
| 1937   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Item name of the entry outfit, LOC type 0 |

All multi-byte values are little-endian.

## Layout 5

### File Layout

| Offset              | Type         | Field                                 | Notes                                                       |
| ------------------- | ------------ | ------------------------------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                                                |
| `+0x04`             | u64          | siege_revival_time                    | `1000` on clients 1784 and 3482                             |
| `+0x0C`             | u64          | siege_death_revival_time              | `1000` on clients 1784 and 3482                             |
| `+0x14`             | u64          | siege_recovery_revival_time           | `6000` on clients 1784 and 3482                             |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     | `3000` on client 1784, `6000` on client 3482                |
| `+0x24`             | u64          | siege_resource_revival_time           | `5` on clients 1784 and 3482                                |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point | `50` on clients 1784 and 3482                               |
| `+0x30`             | u32          | major_siege_liberation_kill_point     | `1` on client 1784, `3` on client 3482                      |
| `+0x34`             | u32          | major_siege_liberation_death_point    | `1` on clients 1784 and 3482                                |
| `+0x38`             | u64          | major_siege_liberation_reward_time    | `3600` on clients 1784 and 3482                             |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    | Item key; `607028` (Sun's Resolve) on clients 1784 and 3482 |
| `+0x44`             | f32          | siege_fortress_short_distance_revival | `6500` on clients 1784 and 3482                             |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    | `12000` on client 1784, `9000` on client 3482               |
| `+0x50`             | u8           | unknown_50                            | `1` on clients 2313 to 3482                                 |
| `+0x51`             | u32          | unknown_51                            | `15` on client 3482                                         |
| `+0x55`             | String Table | string_table                          | See String Table                                            |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x55`                          |
| `string_table+0x04` | u32          | zero                                  | Always `0`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 4

No `unknown_51`.

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | u8           | unknown_50                            |                                    |
| `+0x51`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x51` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 3

`unknown_51` is a u8 (`2` on client 2313, `6` on client 2519).

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | u8           | unknown_50                            |                                    |
| `+0x51`             | u8           | unknown_51                            |                                    |
| `+0x52`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x52` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 2

The twelve `SiegeOption` fields only.

### File Layout

| Offset              | Type         | Field                                 | Notes                              |
| ------------------- | ------------ | ------------------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                                 | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time                    |                                    |
| `+0x0C`             | u64          | siege_death_revival_time              |                                    |
| `+0x14`             | u64          | siege_recovery_revival_time           |                                    |
| `+0x1C`             | u64          | major_siege_recovery_revival_time     |                                    |
| `+0x24`             | u64          | siege_resource_revival_time           |                                    |
| `+0x2C`             | u32          | major_siege_liberation_fortress_point |                                    |
| `+0x30`             | u32          | major_siege_liberation_kill_point     |                                    |
| `+0x34`             | u32          | major_siege_liberation_death_point    |                                    |
| `+0x38`             | u64          | major_siege_liberation_reward_time    |                                    |
| `+0x40`             | u32          | major_siege_enter_clothes_item_key    |                                    |
| `+0x44`             | f32          | siege_fortress_short_distance_revival |                                    |
| `+0x48`             | u64          | siege_short_distance_revival_avoid    |                                    |
| `+0x50`             | String Table | string_table                          | See String Table                   |
| `string_table+0x00` | u32          | table_start                           | Offset of the string table; `0x50` |
| `string_table+0x04` | u32          | zero                                  | Always `0`                         |

## Layout 1

Four revival values, before the Conquest War fields.

### File Layout

| Offset              | Type         | Field                       | Notes                              |
| ------------------- | ------------ | --------------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                       | ASCII `PABR`                       |
| `+0x04`             | u64          | siege_revival_time          | `1000` on clients 1485 and 1636    |
| `+0x0C`             | u64          | siege_death_revival_time    | `1000`                             |
| `+0x14`             | u64          | siege_recovery_revival_time | `6000`                             |
| `+0x1C`             | u64          | siege_resource_revival_time | `5`                                |
| `+0x24`             | String Table | string_table                | See String Table                   |
| `string_table+0x00` | u32          | table_start                 | Offset of the string table; `0x24` |
| `string_table+0x04` | u32          | zero                        | Always `0`                         |

## Field Names

The `SiegeOption` sheet of a private server's `DataSheets.bexcel` on
client 1784 has 24 columns and one row. Twelve of them are the twelve
fields of the client 1784 file, in sheet order and with the sheet's
values (12 of 12): `SiegeRevivalTime`, `SiegeDeathRevivalTime`,
`SiegeRecoveryRevivalTime`, `MajorSiegeRecoveryRevivalTime`,
`SiegeResourceRevivalTime`, `MajorSiegeLiberationFortressPoint`,
`MajorSiegeLiberationKillPoint`, `MajorSiegeLiberationDeathPoint`,
`MajorSiegeLiberationRewardTime`, `MajorSiegeEnterClothesItemKey`,
`SiegeFortressShortDistanceRevival` and `SiegeShortDistanceRevivalAvoid`.
The other twelve (`SiegeStartDistanceTeleport`, the
`majorSiegeAttackGuildReward*` columns, `SiegeMaxResource`,
`SiegeKeepCount1` to `5` and `CastellanImpossibleMinorSiege`) are not in
this file.

That server's dump (client 1784) has check messages for the struct
members `SiegeOptionStaticStatus _respawnTimePerMinute`,
`_respawnTimePerDeathCount`, `_respawnTimePerHealingTower`,
`_respawnTimePerHealingTowerMajor`, `_respawnResourcePerCost`,
`_castellanImpossibleTerritoryList`, `_majorSiegeLiberationFortressPoint`
and `_majorSiegeLiberationKillPoint`, stored in the reverse of the sheet's
column order from `SiegeRevivalTime` to `MajorSiegeLiberationKillPoint`.
That order pairs `SiegeRevivalTime` with `_respawnTimePerMinute` through
`SiegeResourceRevivalTime` with `_respawnResourcePerCost`. The field names
follow the sheet columns.

Layout 1 holds the values `1000, 1000, 6000, 5`: the client 1784 record
without `MajorSiegeRecoveryRevivalTime` (`3000`), so its four fields take
the names of the other four. `unknown_50` and `unknown_51` are newer than
client 1784 and have no source; `unknown_51` is a u8 on clients 2313 to
2637, missing on clients 2765 and 3002 and a u32 from client 3251.

## Notes

- `major_siege_enter_clothes_item_key` `607028` is Sun's Resolve
  (LOC type 0).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  one row with every named field and the outfit item with its icon and
  name. It reads Layout 5 only.

## Open Questions

### Units of the Revival Times

By the dump's member order, `siege_revival_time` and
`siege_death_revival_time` are `_respawnTimePerMinute` and
`_respawnTimePerDeathCount`: revive time added per minute of war and per
death. Neither the unit of their `1000` nor how the client combines them
is confirmed. `siege_resource_revival_time` (`_respawnResourcePerCost`,
`5`) reads as a resource cost, not a time.

### The Fields After the Short-Distance Revival

`unknown_50` is `1` from client 2313 on. `unknown_51` is a u8 (`2`, then
`6`) on clients 2313 to 2637, gone on clients 2765 and 3002, and a u32
`15` from client 3251; whether these are one field is open.
