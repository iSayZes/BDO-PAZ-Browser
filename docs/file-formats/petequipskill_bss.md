# `petequipskill.bss` Format

## Purpose

Defines two pet skill catalogs, both keyed by `equip_skill_id`. 116 skill entries span two sections: Section 1 (the equip skills a pet rolls, IDs 0–42) and Section 2 (the base skills, IDs 15–111, keyed by `base_skill_id` in [pet.dbss](pet_dbss.md)). Each entry records the skill's type group, an unknown byte (`unknown_08`), and a localization ID that resolves to the in-game skill name and pet equip-skill icon number.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records                  | Row bytes               |
| ------ | -------------- | ------- | ------------------- | ----- | ------------------------ | ----------------------- |
| 2      | 3473 and later | 3474    | `petequipskill.bss` | 3,772 | 43 Equip Skill, 200 Slot | 16 to 20, 16 on average |
| 1      | 1784           | 1784    | `petequipskill.bss` | 1,732 | 43 Equip Skill, 100 Slot | 12                      |

| Layout | File                | Known            | Unknown       |
| ------ | ------------------- | ---------------- | ------------- |
| 2      | `petequipskill.bss` | 2,932 B (77.7%)  | 840 B (22.3%) |
| 1      | `petequipskill.bss` | 1,732 B (100.0%) | 0 B (0.0%)    |

<!-- versions:end -->

## Companion Files

None; `petequipskill.bss` is a standalone catalog with no offset index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

Records begin immediately at `+0x04`.

| Offset              | Type                                     | Field         | Notes                                                           |
| ------------------- | ---------------------------------------- | ------------- | --------------------------------------------------------------- |
| `+0x00`             | char[4]                                  | magic         | `PABR` (ASCII)                                                  |
| `+0x04`             | Equip Skill[while equip_skill_id != 200] | equip_skills  | Section 1, 43 x 12 bytes, `+0x004` to `+0x208`                  |
| `equip_skills+0x00` | Slot[..data_end]                         | slots         | Null block and Section 2, 200 slots from `+0x208` to `data_end` |
| `EOF-0x0C` | u32 | string_count | `0`: the PABR string table, here with no strings; `data_end` points at it |
| `EOF-0x08` | u32 | data_end | `0x0EB0` = `file_size - 12`, the offset of `string_count` |
| `EOF-0x04` | u32 | zero | Always `0` |

### Equip Skill (12 bytes)

Section 1, Equip Skills. Covers `equip_skill_id` 0 to 42 (regular pets). Stride = 12 bytes. The file stores no count: record `n` holds `equip_skill_id = n`, so the section ends at the first record whose ID is not its index, which is the first null placeholder (ID 200) of the slot table below. The parser finds the end this way, so a patch that adds Section 1 skills moves the null block and Section 2 without breaking the walk.

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u32  | equip_skill_id | Unique skill record key (0 to 42)        |
| `+0x04` | u32  | skill_type     | Skill group (1 to 20; see Skill Types table) |
| `+0x08` | u16  | skill_level    | Skill level of the `gc::SkillKey`; always `1` |
| `+0x0A` | u16  | skill_no       | Skill number (`SkillNo`); keys the LOC type 10 name |

### Slot (variable: 16 bytes + unknown_10)

Null Block (15 x 16 bytes, offset `0x208`): fifteen placeholder records, the first 15 slots of the 200-slot table that continues as Section 2, so they are the slots for IDs 0 to 14 (see Section 2). Earlier versions of this doc read them as IDs 43 to 57. Each record = `[u32=200][u32=0][u32=0][u32=0]`. The value 200 signals a null/unused entry.

Section 2, Base Skills (variable stream, offset `0x2F8`): covers `equip_skill_id` 15 to 111, the base skills `pet.dbss` keys with `base_skill_id`; IDs 15 to 42 also exist in Section 1 as different skills. Base stride = 16 bytes. Records with `equip_skill_id = 200` are null placeholders. Records with `unknown_0c = 1` carry an additional u32 after the base record.

| Offset  | Type              | Field          | Notes                                            |
| ------- | ----------------- | -------------- | ------------------------------------------------ |
| `+0x00` | u32               | equip_skill_id | Unique skill record key (15 to 111, or 200 = null) |
| `+0x04` | u32               | skill_type     | Skill group (different numbering from Section 1) |
| `+0x08` | u16               | skill_level    | Skill level of the `gc::SkillKey`; always `1`    |
| `+0x0A` | u16               | skill_no       | Skill number (`SkillNo`); keys the LOC type 10 name |
| `+0x0C` | u32               | unknown_0c     | `0` or `1`; `1` means an extra u32 follows       |
| `+0x10` | u32 if unknown_0c = 1 | unknown_10 | Present only when `unknown_0c = 1`               |

Earlier versions of this doc called `skill_level` `tier`, `unknown_0c` `extra_flag` and `unknown_10` `extra_value`. `unknown_0c` and `unknown_10` are not in the client 1784 build (12-byte slots, Layout 1), so no source names them; on client 3474 `unknown_0c` is `1` on 10 of 73 live slots (IDs 65 to 68, 79 to 82, 104, 107) and `unknown_10` equals that record's `skill_type` on all 10.

The null block and Section 2 together are exactly 200 slots, from `0x208` up to the trailer's `data_end`, and every live Section 2 record sits at the slot whose index equals its `equip_skill_id` (slots `0` to `14` are the null block). Reading one extra u32 after each `unknown_0c = 1` record is what keeps that alignment and lands the last slot exactly on `data_end`. The parser walks the null block and Section 2 as one table starting right after Section 1, and its `slot` field is the table index, so every record in both sections has `slot = equip_skill_id`.

Within each section, skills of the same `skill_type` form a tier group (e.g., all Karma Recovery entries share type 1 in S1). The type numbering is section-local and the mapping from type ID to skill category name is derived empirically from skill numbers. No authoritative mapping table has been found. The grouping itself holds for all 116 records: every record of one `skill_type` in a section resolves to the same effect name through LOC, which is why the field keeps its name while only the type-to-name table is open.

## Field Names

The client 1784 private server loads `Pet_EquipSkill_Table` and `Pet_BaseSkill_Table` into one 24-byte entry per
record: `Index` (`equip_skill_id`) at `+0x00`, `GroupNo` (`skill_type`) at
`+0x04`, a runtime skill pointer at `+0x08` and a `gc::SkillKey` at `+0x10`.
The loader (VA `0x14086beaf` to `0x14086bebc`, and `0x14086c434` for the base skills) writes the key as `(SkillNo << 16) | 1`, so its low u16
is the skill level (always `1`) and its high u16 the sheet's `SkillNo`. The
2016 client's `gc::SkillKey` is one `unsigned int _value` whose `getLevel()`
reads the low u16 and `getSkillNo()` the high u16, which places
`skill_level` at `+0x08` and `skill_no` at `+0x0A`. The server has no reader
for this file; the record is that entry in loader order without the pointer
and the padding. After loading, it looks up every key in the skill table and
logs "펫 착용 스킬에 알수 없는 스킬(%#)의 데이터가 있습니다!" ("pet equip
skill has data for an unknown skill (%#)!") for a missing one.
`petequipskill.bss` and `fairyequipskill.bss` share the entry, the loader
shape and the per-entry checks.

The client 1784 build's own file matches `Pet_EquipSkill_Table` on all
43 equip records and `Pet_BaseSkill_Table` on all 60 base records (Index,
GroupNo, level `1`, SkillNo). Unused entries hold `equip_skill_id` `100`
there, the size of the base array (`200` on client 3474).

LOC type 10 keys the skill name by `skill_no`
([`languagedata_loc.md`](languagedata_loc.md)). Earlier versions of this doc
read `+0x08` as two u8 fields (`unknown_08`, `unknown_09`) and named `+0x0A`
`loc_id`.

## Layout 1

On client 1784 the null-entry sentinel was `100`, not `200`, and every Slot
was 12 bytes: Section 2 records had no `unknown_0c` and no `unknown_10`. The
File Layout and the Slot differ from Layout 2; the Equip Skill is the same.
On client 1784 the file holds 43 Equip Skills and 100 Slots, and every live
Section 2 record still sits at the slot whose index equals its
`equip_skill_id`.

### File Layout

| Offset              | Type                                     | Field        | Notes                                                    |
| ------------------- | ---------------------------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                                  | magic        | `PABR` (ASCII)                                           |
| `+0x04`             | Equip Skill[while equip_skill_id != 100] | equip_skills | Section 1, ends at the first record whose ID is `100`    |
| `equip_skills+0x00` | Slot[..data_end]                         | slots        | Null block and Section 2, 12-byte slots up to `data_end` |
| `EOF-0x0C`          | u32                                      | string_count | `0`: the PABR string table, here with no strings         |
| `EOF-0x08`          | u32                                      | data_end     | `file_size - 12`, the offset of `string_count`           |
| `EOF-0x04`          | u32                                      | zero         | Always `0`                                               |

### Slot (12 bytes)

| Offset  | Type | Field          | Notes                                          |
| ------- | ---- | -------------- | ---------------------------------------------- |
| `+0x00` | u32  | equip_skill_id | Skill record key, or `100` = null              |
| `+0x04` | u32  | skill_type     | Skill group; `0` in a null slot                |
| `+0x08` | u16  | skill_level    | `1` in a live record, `0` in a null slot       |
| `+0x0A` | u16  | skill_no       | Skill number; `0` in a null slot               |
