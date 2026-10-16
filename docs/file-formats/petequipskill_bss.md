# `petequipskill.bss` Format

## Purpose

Defines two pet skill catalogs, both keyed by `equip_skill_id`. 116 skill entries span two sections: Section 1 (the equip skills a pet rolls, IDs 0–42) and Section 2 (the base skills, IDs 15–111, keyed by `base_skill_id` in [pet.dbss](pet_dbss.md)). Each entry records the skill's type group, an unknown byte (`unknown_08`), and a localization ID that resolves to the in-game skill name and pet equip-skill icon number.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records                  | Row bytes               |
| ------ | -------------- | ------- | ------------------- | ----- | ------------------------ | ----------------------- |
| 1      | 3473 and later | 3473    | `petequipskill.bss` | 3,772 | 43 Equip Skill, 200 Slot | 16 to 20, 16 on average |

| Layout | File                | Known           | Unknown         |
| ------ | ------------------- | --------------- | --------------- |
| 1      | `petequipskill.bss` | 2,446 B (64.8%) | 1,326 B (35.2%) |

<!-- versions:end -->

## Companion Files

None; `petequipskill.bss` is a standalone catalog with no offset index.

All multi-byte values are little-endian.

## Layout 1

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
| `+0x08` | u8   | unknown_08     | Always 1 in Section 1                    |
| `+0x09` | u8   | unknown_09     | Always 0                                 |
| `+0x0A` | u16  | loc_id         | Localization key to skill name (type 10 string) |

### Slot (variable: 16 bytes + unknown_10)

Null Block (15 x 16 bytes, offset `0x208`): fifteen placeholder records, the first 15 slots of the 200-slot table that continues as Section 2, so they are the slots for IDs 0 to 14 (see Section 2). Earlier versions of this doc read them as IDs 43 to 57. Each record = `[u32=200][u32=0][u32=0][u32=0]`. The value 200 signals a null/unused entry.

Section 2, Base Skills (variable stream, offset `0x2F8`): covers `equip_skill_id` 15 to 111, the base skills `pet.dbss` keys with `base_skill_id`; IDs 15 to 42 also exist in Section 1 as different skills. Base stride = 16 bytes. Records with `equip_skill_id = 200` are null placeholders. Records with `unknown_0c = 1` carry an additional u32 after the base record.

| Offset  | Type              | Field          | Notes                                            |
| ------- | ----------------- | -------------- | ------------------------------------------------ |
| `+0x00` | u32               | equip_skill_id | Unique skill record key (15 to 111, or 200 = null) |
| `+0x04` | u32               | skill_type     | Skill group (different numbering from Section 1) |
| `+0x08` | u8                | unknown_08     | Always 1                                         |
| `+0x09` | u8                | unknown_09     | Always 0                                         |
| `+0x0A` | u16               | loc_id         | Localization key to skill name (type 10 string)  |
| `+0x0C` | u32               | unknown_0c     | `0` or `1`; `1` means an extra u32 follows       |
| `+0x10` | u32 if unknown_0c = 1 | unknown_10 | Present only when `unknown_0c = 1`               |

Earlier versions of this doc called `unknown_08` `tier`, `unknown_0c` `extra_flag` and `unknown_10` `extra_value`.

The null block and Section 2 together are exactly 200 slots, from `0x208` up to the trailer's `data_end`, and every live Section 2 record sits at the slot whose index equals its `equip_skill_id` (slots `0` to `14` are the null block). Reading one extra u32 after each `unknown_0c = 1` record is what keeps that alignment and lands the last slot exactly on `data_end`. The parser walks the null block and Section 2 as one table starting right after Section 1, and its `slot` field is the table index, so every record in both sections has `slot = equip_skill_id`.

Within each section, skills of the same `skill_type` form a tier group (e.g., all Karma Recovery entries share type 1 in S1). The type numbering is section-local and the mapping from type ID to skill category name is derived empirically from loc IDs. No authoritative mapping table has been found. The grouping itself holds for all 116 records: every record of one `skill_type` in a section resolves to the same effect name through LOC, which is why the field keeps its name while only the type-to-name table is open.
