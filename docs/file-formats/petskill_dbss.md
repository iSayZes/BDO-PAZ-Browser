# `petskill.dbss` Format

## Purpose

Defines pet skill effect tables. Each record is keyed by `pet_skill_id`, has a skill type that names it in the pet window, and contains one baseline row plus ten level rows. Companion `petskilloffset.dbss` provides keyed lookup into the variable-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                               | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------------------- | --------- |
| 1      | 3473 and later | 3473    | `petskill.dbss`       | 9,380 | 539 Effect Row, 49 Payload, 49 Record | 17        |
| 1      | 3473 and later | 3473    | `petskilloffset.dbss` | 494   | 49 Offset Row                         | 10        |

| Layout | File                  | Known           | Unknown         |
| ------ | --------------------- | --------------- | --------------- |
| 1      | `petskill.dbss`       | 5,590 B (59.6%) | 3,790 B (40.4%) |
| 1      | `petskilloffset.dbss` | 396 B (80.2%)   | 98 B (19.8%)    |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                |
| ---------------------- | -------- | --------------------------------------------------- |
| `petskilloffset.dbss`  | Required | `pet_skill_id -> (data_offset, data_size)` lookup   |
| `stringtable.bss`      | Optional | Key hashes of the skill type names, see Skill Types |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petskilloffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                          |
| ------- | ------------- | ------- | ------------------------------ |
| `+0x00` | u32           | count   | Number of records; observed 49 |
| `+0x04` | Record[count] | records | See Record                     |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_skill_id`                                  |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 189 bytes, size from `petskilloffset.dbss`)

| Offset  | Type             | Field        | Notes                                                          |
| ------- | ---------------- | ------------ | -------------------------------------------------------------- |
| `+0x00` | u16              | pet_skill_id | Equals the key prefix and the offset-table key                 |
| `+0x02` | Effect Row[11]   | effect_rows  | One baseline row (`row_index=0`) plus ten level rows (`1..10`) |
| `+0xBD` | u8 if size = 190 | unknown_bd   | Observed values 9 and 10                                       |

The 32 records with `data_size=189` end after the eleven 17-byte rows. The 17 records with `data_size=190` have one trailing `unknown_bd` byte.

### Effect Row (17 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | skill_type   | 1–11 on client 3473; same value in all rows of a record, see Skill Types                |
| `+0x01` | u8   | row_level    | Row 0 uses 1; rows 1–10 use 1–10                                                        |
| `+0x02` | u16  | unknown_02   | Always 0                                                                                |
| `+0x04` | u32  | raw_value_a  | Primary effect value. Row 0 is always 2560; rows 1–10 vary by `pet_skill_id`            |
| `+0x08` | u32  | raw_value_b  | Secondary effect value. Row 0 is always 2560; rows 1–10 are 0 or a skill-specific value |
| `+0x0C` | u32  | unknown_0c   | Row 0 = 256; rows 1–9 = `(row_level + 1) * 256`; row 10 is 0 or 256                     |
| `+0x10` | u8   | unknown_10   | Always 0                                                                                |

Earlier versions of this doc called `skill_type` `unknown_00` and before that `skill_group`, `unknown_0c` `row_marker` and the payload's `unknown_bd` `extra_marker`.

### `petskilloffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Must equal `petskill.dbss` count (49) |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                        |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_skill_id | Matches `pet_skill_id` in the main record                                    |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petskill.dbss` to the payload, after the key prefix |
| `+0x06` | u16  | data_size    | 189 or 190 bytes                                                             |
| `+0x08` | u16  | unknown_08   | Always 0                                                                     |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix.

## Observed Values

| Field              | Observed values / range                                      |
| ------------------ | ------------------------------------------------------------ |
| `pet_skill_id`     | 1–6, 11–18, 21–23, 26–57 (49 records total)                  |
| `skill_type`       | 1–11                                                         |
| `row_level`        | baseline row uses 1; level rows use 1–10                     |
| `raw_value_a`      | row 0 always 2560; level rows 512,000–128,000,000            |
| `raw_value_b`      | row 0 always 2560; level rows 0–76,800,000                   |
| `unknown_0c`       | 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 0   |
| `unknown_bd`       | 9 or 10 when present                                         |

`skill_type` is not unique: multiple `pet_skill_id` records share one value while carrying different effect values.

## Skill Types

`skill_type` is the 2016 `gc::PetSkillParam::PetSkillType`, which Lua reads as `skillParam._type`. It equals the `PetSkillType` column of the `Pet_Skill_Table` sheet of a private server on client 1784 on all 46 shared skills. The pet info window (`setPetSkillType` in `panel_window_petinfo_all_1.luac`) shows one GAME sheet string per type, prefixed `LUA_PETINFO_PETSKILLTYPE_`. Types 11 to 14 are newer than the 2016 enum. English text from client 3473:

| Type | 2016 enum | Key suffix | English text |
| ---: | --------- | ---------- | ------------ |
| 1  | `ePetSkill_Looting` | `ITEMGETTIME` | Loot (every {itemGetTime} sec) |
| 2  | `ePetSkill_AlertCollect` | `FINDGATHER` | Finds Resources |
| 3  | `ePetSkill_AlertMurderer` | `FINDPK` | Hostility Detection |
| 4  | `ePetSkill_DetectPosition` | `FINDPLACE` | Location Find |
| 5  | `ePetSkill_Aggro` | `MOBAGGRO` | Taunt Monster |
| 6  | `ePetSkill_FindNamedMonster` | `FINDRAREMONSTER` | Finds Rare Monsters |
| 7  | `ePetSkill_ReduceAutoFishingTime` | `REDUCEAUTOFISHINGTIME` | Auto-fishing Time Reduction |
| 8  | `ePetSkill_RegistForRegionSkill` | `REGISTILL` | Resistance to Desert Illnesses |
| 9  | `ePetSkill_Collecting` | `AUTOGETHERING` | Auto Gathering |
| 10 | `ePetSkill_CollectingBoost` | `GETHERINGINCREASE` | Gathering Quantity Increase |
| 11 | - | `HPRECOVERY` | Restore HP |
| 12 | - | `MPRECOVERY` | Endurance/MP Recovery |
| 13 | - | `FINDLOSTNORMALITEM` | Find Normal Lost Item |
| 14 | - | `FINDLOSTSPECIALITEM` | Find Special Lost Item |

The client fills `{itemGetTime}` from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code the browser cannot reproduce, so the handler shows `?` there. The window prints the first pet skill as "Basic: ..." and the second as "Special: ...".

The parser yields ten level rows per record: 490 rows for the 49 records. Both files are byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Notes

- File size is 9380 bytes: 4-byte count plus 49 wrapper records.
- `petskilloffset.dbss` size is 494 bytes: 4-byte count plus 49 × 10-byte offset rows.
- `unknown_08` of the offset table is 0 in every record.
- Offset rows are sorted descending for high IDs first, not ascending by key.
- `raw_value_a` and `raw_value_b` are named as raw values because the display scale is not confirmed. Some values are multiples of 256, 256,000, or 25,600,000.
- This file is distinct from `petequipskill.bss`, which stores localized equip-skill catalog entries.
- [pet.dbss](pet_dbss.md) keys this file twice per pet: `loot_skill_id` and `race_skill_id`. Every value of both is a `pet_skill_id` here.

## Open Questions

### Raw value scale

`raw_value_a`, `raw_value_b`, and `unknown_0c` appear scaled in several different ways. The correct display formula needs confirmation from UI code or in-game pet skill percentage displays.

### Baseline row meaning

Row 0 is identical across all records except `skill_type`: `raw_value_a=2560`, `raw_value_b=2560`, `unknown_0c=256`. It may be a base display/effect row, but its exact role is not confirmed.

### Extra marker byte

Only 17 records have a trailing `unknown_bd` byte. Values are 9 or 10, but its relationship to `skill_type`, max level, or UI display is unknown.
