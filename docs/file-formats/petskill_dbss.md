# `petskill.dbss` Format

## Purpose

Pet skill levels. Each record is keyed by `pet_skill_id`, has a skill type that names it in the pet window, and holds ten level entries with two effect parameters each. Companion `petskilloffset.dbss` provides keyed lookup into the variable-size record stream.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------------------------------------- | --------- |
| 2      | 2107 and later | 3474    | `petskill.dbss`       | 9,380 | 490 Level Entry, 49 Payload, 49 Record | 17        |
| 2      | 2107 and later | 3474    | `petskilloffset.dbss` | 494   | 49 Offset Row                          | 10        |
| 1      | 1485 to 1784   | 1784    | `petskill.dbss`       | 8,606 | 460 Level Entry, 46 Payload, 46 Record | 17        |
| 1      | 1485 to 1784   | 1784    | `petskilloffset.dbss` | 464   | 46 Offset Row                          | 10        |

| Layout | File                  | Known           | Unknown      |
| ------ | --------------------- | --------------- | ------------ |
| 2      | `petskill.dbss`       | 8,775 B (93.6%) | 605 B (6.4%) |
| 2      | `petskilloffset.dbss` | 396 B (80.2%)   | 98 B (19.8%) |
| 1      | `petskill.dbss`       | 8,238 B (95.7%) | 368 B (4.3%) |
| 1      | `petskilloffset.dbss` | 372 B (80.2%)   | 92 B (19.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                |
| ---------------------- | -------- | --------------------------------------------------- |
| `petskilloffset.dbss`  | Required | `pet_skill_id -> (data_offset, data_size)` lookup   |
| `stringtable.bss`      | Optional | Key hashes of the skill type names, see Skill Types |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petskilloffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                                |
| ------- | ------------- | ------- | ------------------------------------ |
| `+0x00` | u32           | count   | Number of records; 49 on client 3473 |
| `+0x04` | Record[count] | records | See Record                           |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_skill_id`                                  |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 19 bytes + levels and list, size from `petskilloffset.dbss`)

| Offset        | Type                     | Field              | Notes                                                        |
| ------------- | ------------------------ | ------------------ | ------------------------------------------------------------ |
| `+0x00`       | u16                      | pet_skill_id       | Equals the key prefix and the offset-table key               |
| `+0x02`       | u8                       | skill_type         | 1 to 11 on client 3473, see Skill Types                      |
| `+0x03`       | i32                      | unknown_03         | Always `1`; the place of the 2016 `_petRequireLevel` (Notes) |
| `+0x07`       | u32                      | unknown_07         | Always `10`; the place of the 2016 `_skillMaxCount` (Notes)  |
| `+0x0B`       | u32                      | level_count        | `10` on every record                                         |
| `+0x0F`       | Level Entry[level_count] | levels             | Level 1 first                                                |
| `levels+0x00` | u32                      | unknown_list_count | `0` or `1`                                                   |
| `levels+0x04` | u8[unknown_list_count]   | unknown_list       | `9` or `10` when present                                     |

On client 3473, 32 payloads have an empty list (189 bytes) and 17 hold one
byte (190 bytes): `10` on the three type 9 skills (41 to 43), `9` on 14
skills of types 1, 2, 6, 10 and 11 (44 to 57).

### Level Entry (17 bytes)

One `gc::PetSkillParam` of the 2016 client (`_type`, `_level`, `_param[2]`),
after its map key.

| Offset  | Type | Field      | Notes                                                                          |
| ------- | ---- | ---------- | ------------------------------------------------------------------------------ |
| `+0x00` | i32  | level_dup  | Equals `level`; the key of the 2016 `_skillList` map                           |
| `+0x04` | u8   | skill_type | Equals the payload's `skill_type`                                              |
| `+0x05` | i32  | level      | 1 to 10                                                                        |
| `+0x09` | i32  | param_0    | The sheet's `Param0` (Notes); 2,000 to 500,000 on client 3473                  |
| `+0x0D` | i32  | param_1    | The sheet's `Param1`; 0 to 300,000 on client 3473, 0 on 200 of the 490 entries |

Earlier versions of this doc read the payload one byte off, as eleven 17-byte
rows of u8 `skill_type`, u8 `row_level`, u16 and three u32 (`raw_value_a`,
`raw_value_b`, `unknown_0c`) and a trailing u8 `unknown_bd`. The "baseline
row" was the payload head (`skill_type`, `1`, `10`, `10`) and the level 1
key; `raw_value_a` and `raw_value_b` were `param_0` and `param_1` times 256,
`unknown_0c` the next entry's `level_dup` and `unknown_bd` the list byte.

### `petskilloffset.dbss`

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Equals the `petskill.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                                        |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_skill_id | Matches `pet_skill_id` in the main record                                    |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petskill.dbss` to the payload, after the key prefix |
| `+0x06` | u16  | data_size    | 189 or 190 bytes on client 3473                                              |
| `+0x08` | u16  | unknown_08   | Always 0                                                                     |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix.

## Layout 1

On client 1784 every payload is 185 bytes: it ends after the tenth level
entry, with no `unknown_list_count`. Only the Payload differs from Layout 2.

### Payload (variable: 15 bytes + levels, size from `petskilloffset.dbss`)

| Offset  | Type                     | Field        | Notes                                          |
| ------- | ------------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u16                      | pet_skill_id | Equals the key prefix and the offset-table key |
| `+0x02` | u8                       | skill_type   |                                                |
| `+0x03` | i32                      | unknown_03   | Always `1`                                     |
| `+0x07` | u32                      | unknown_07   | Always `10`                                    |
| `+0x0B` | u32                      | level_count  | `10` on every record                           |
| `+0x0F` | Level Entry[level_count] | levels       | Level 1 first                                  |

## Observed Values

Client 3473:

| Field          | Observed values / range                           |
| -------------- | ------------------------------------------------- |
| `pet_skill_id` | 1 to 6, 11 to 18, 21 to 23, 26 to 57 (49 records) |
| `skill_type`   | 1 to 11                                           |
| `param_0`      | 2,000 to 500,000                                  |
| `param_1`      | 0 to 300,000                                      |
| `unknown_list` | empty, `9` or `10`                                |

`skill_type` is not unique: multiple `pet_skill_id` records share one value while carrying different parameters.

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

The parser yields one record per level entry, ten per pet skill.

## Notes

- File size is 9,380 bytes on client 3473: 4-byte count plus 49 wrapper records.
- `petskilloffset.dbss` size is 494 bytes on client 3473: 4-byte count plus 49 x 10-byte offset rows.
- `unknown_08` of the offset table is 0 in every record.
- Offset rows are sorted descending for high IDs first, not ascending by key.
- The 2016 client's `gc::PetSkillStaticStatus` holds `_petSkillKey` (u16), `_type` (u8), `_petRequireLevel` (i32), `_skillMaxCount` (u32) and `_skillList`, a map from int to `gc::PetSkillParam`. The payload follows that order. `unknown_03` and `unknown_07` stay unnamed: they are `1` and `10` on every record of both clients, and `Pet_Skill_Table` has no column for them.
- `skill_type`, `level`, `param_0` and `param_1` follow the `Pet_Skill_Table` sheet (`PetSkillNo`, `PetSkillType`, `Level`, `Param0`, `Param1`) of a private server's `DataSheets.bexcel` on client 1784. The private server's own file matches it on all 460 level entries. Client 3473 matches `PetSkillType` on all 460 shared entries, `Param0` on 190 and `Param1` on 274; the other values changed since.
- This file is distinct from `petequipskill.bss`, which stores localized equip-skill catalog entries.
- [pet.dbss](pet_dbss.md) keys this file twice per pet: `loot_skill_id` and `race_skill_id`. Every value of both is a `pet_skill_id` here.

## Open Questions

### Parameter Units

`param_0` and `param_1` mean something different per skill type. Loot (type 1) holds 2,000 to 8,000 in `param_0`, and Restore HP (type 11) falls from 14,000 at level 1 to 5,000 at level 10, which reads as an interval in milliseconds. The loot text gets its time from `ToClient_getPetLootingCoolTime(param, lootingType)`, game code that does not show which field `param` is.

### The Trailing List

On client 3473, 17 payloads end with a one-byte list (`9` or `10`), the others with an empty one; client 1784 has no list. The value does not follow `skill_type` alone (type 1 skills hold both an empty list and `9`), so what it selects is open.
