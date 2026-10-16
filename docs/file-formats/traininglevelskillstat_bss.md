# `traininglevelskillstat.bss` Format

## Purpose

Two Training bonuses per Training level, from level 1 (Beginner 1) to 180
(Guru 100): the chance for a mount to learn a skill when it gains a level,
and the chance for a higher minimum movement speed gain on a mount level up.
The Training tooltip in the Character Info Basic tab shows both.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | --------------- | --------- |
| 1      | 3473 and later | 3473    | `traininglevelskillstat.bss` | 1,456 | 180 Level Entry | 8         |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `traininglevelskillstat.bss` | 1,456 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

The file is self-contained. All multi-byte values are little-endian.

## Layout 1

### File Layout

The layout of [`commonlifestatdata.bss`](commonlifestatdata_bss.md): PABR,
then one entry per level with no row count, the empty string table and the
8-byte trailer.

| Offset     | Type               | Field        | Notes                                                                    |
| ---------- | ------------------ | ------------ | ------------------------------------------------------------------------ |
| `+0x00`    | char[4]            | magic        | ASCII `PABR`                                                             |
| `+0x04`    | Level Entry[..table_start] | entries      | One entry per level from level 1, up to `table_start`; 180 on client 3464 |
| `EOF-0x0C` | u32                | string_count | Always `0`                                                               |
| `EOF-0x08` | u32                | table_start  | Offset of `string_count`, where the entries end                          |
| `EOF-0x04` | u32                | zero         | Always `0`                                                               |

### Level Entry (8 bytes)

| Offset  | Type | Field                        | Notes                                                    |
| ------- | ---- | ---------------------------- | -------------------------------------------------------- |
| `+0x00` | u32  | add_vehicle_skill_owner_rate | Mount skill learn chance, `1,000,000` = 100%; `1,000,000` from Guru 20 on client 3464 |
| `+0x04` | u32  | add_servant_stat_rate        | Higher minimum movement speed chance, `1,000,000` = 100%; `470,000` from Guru 50 on client 3464 |

Entry `n` (from 0) belongs to level `n + 1`, as in
[`commonlifestatdata.bss`](commonlifestatdata_bss.md).
`add_vehicle_skill_owner_rate` changes its step per level at every rank
start under that reading (client 3464):

| Levels                       | `add_vehicle_skill_owner_rate` step per level |
| ---------------------------- | --------------------------------------------- |
| Beginner 2 to 10             | 3,000 (from 10,000)                           |
| Apprentice 1 to 10           | 3,300                                         |
| Skilled 1 to 10              | 3,600                                         |
| Professional 1 to 10         | 6,500                                         |
| Artisan 1 to 10              | 7,000                                         |
| Master 1 to 10               | 7,500                                         |
| Master 11 to 20              | 12,800                                        |
| Master 21 to 30              | 13,600                                        |
| Guru 1 to 10                 | 14,400                                        |
| Guru 11 to 19                | 18,000                                        |
| Guru 20 to 100               | `1,000,000` flat                              |

`add_servant_stat_rate` rises in uneven steps from `10,000` at Beginner 2 to
`470,000` at Guru 50 and stays there. Both are 0 at Beginner 1.

`ToClient_getTrainingLevelSkillStatStaticStatus()` returns a wrapper with two
members, read in `panel_characterinfo_basic_all_2.luac` (behind
`_ContentsGroup_EnhanceTraining`):

```lua
skillRate = string.format("%.1f", trainingSKillStatStaticStatus._addVehicleSkillOwnerRate / 10000)
statRate = string.format("%.1f", trainingSKillStatStaticStatus._addServantStatRate / 10000)
```

They fill `rate1` and `rate2` of `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2`:
"+{rate1}% chance for your mount to learn a skill when your mount gains a
level" and "+{rate2}% chance to gain higher minimal movement speed when your
mount gains a level"; `rate3` is `ToClient_GetServantMarketTaxPercent()`.
The stable's skill tooltip in `panel_dialog_servantsimulator_5.luac` shows
`_addVehicleSkillOwnerRate` alone as
`LUA_SERVANTSIMULATOR_LEARNSKILLRATEFROMTRAININGLEVEL` ("- Based on Training
Level: {percent}%").

The Lua reads both members by name, so the in-game tooltip fixes the order:
at Training Artisan 7 (level 47) it shows +21.7% skill learn chance and
+21.4% higher minimum speed chance, entry 46's `+0x00` and `+0x04` (client
3464). Level 46 holds 21.0% for both, so the same tooltip also confirms the
entry `n` = level `n + 1` reading.

## Notes

- The handler is `_bss/traininglevelskillstat/`. It reads the entries with
  `parse_level_entries` from `_bss/commonlifestatdata/parser.py` and the
  rank text with `rank_text` from `_dbss/lifeexp/labels.py`.
- The column labels follow `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2` in each
  language's LOC.
- In the mount Growth Calculator, `add_servant_stat_rate` raises the
  lowest movement gain a level-up can roll to `1 + round(die max x rate /
  1,000,000)` tenths of a percent, where the die is the horse's movement
  dice in [servantexperience.dbss](servantexperience_dbss.md); every value
  from that floor to the die maximum stays equally likely. I checked it on a
  `1D13` and a `1D10` horse at three Training levels (the table is in that
  doc's Notes).
