# `vehicletrainingskill.bss` Format

## Purpose

The mount training skills: the [`vehicleskill.dbss`](vehicleskill_dbss.md)
keys that a mount raises with training items instead of riding. A u32 count
follows the PABR magic, then one u8 skill key per entry. On every client
checked (1784 to 3474) the list is `49` Skill, `50` Elegance and `51`
Strength.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `vehicletrainingskill.bss` | 23    | 1 String Table | 4         |

| Layout | File                       | Known         | Unknown    |
| ------ | -------------------------- | ------------- | ---------- |
| 1      | `vehicletrainingskill.bss` | 23 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                             |
| --------------------- | -------- | -------------------------------- |
| `languagedata_en.loc` | Optional | Mount skill names, LOC type 8    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | skill_count  | Number of skill keys                                       |
| `+0x08`             | u8[skill_count] | skill_key    | `vehicleskill.dbss` key; the handler shows its LOC type 8 name |
| `skill_key+0x00`    | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table; `0x0B` on every client checked |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `VehicleTrainingSkill_Item_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_vehicleskill.xlsm`, has the columns `ItemKey`, `SkillKey`,
`Experience` and `Desc` and 13 rows. Its `SkillKey` values are `49`, `50`
and `51`, the three keys of the client 1784 file (3 of 3) and of the live
file (client 3474). The file keeps only the distinct skill keys; the item
rows are not in it. The `Desc` texts name the three trainings
(`기술 훈련`, `기품 훈련`, `체력 훈련`), and a note column of the workbook
says one training skill can be raised with several items (dated
2016-12-12).

The keys are the mount skills `기술`, `기품` and `체력` in `vehicleskill.dbss`
on client 3474; LOC type 8 names them Skill, Elegance and Strength (`str_id4`
`0`), with Elegance Training and Strength Training under `str_id4` `1` and
`4`.

## Notes

- Raw bytes on clients 1784 and 3474:
  `50 41 42 52 03 00 00 00 31 32 33 00 00 00 00 0B 00 00 00 00 00 00 00`
  (23 bytes).
- The skill key is one byte here, as in the other tables that list mount
  skills (`_common/vehicle_skill.py`).
- The servant skill window (`panel_dialog_servantskillmanagement_all_1.luac`,
  client 3474) leaves skills with `skillWrapper:isTrainingSkill()` out of the
  learned skill list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per skill key.
