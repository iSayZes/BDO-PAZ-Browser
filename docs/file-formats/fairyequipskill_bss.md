# `fairyequipskill.bss` Format

## Purpose

Defines the fairy skill catalog, the 35 skills a fairy can hold, grouped into 8 skill types with tier progressions (e.g. `Tingling Breath I`–`V`). Each record stores its skill type group and a `gc::SkillKey` (skill level and skill number); the skill number resolves to both the skill name and its effect description, and doubles as the icon filename number.

The remainder of the file is a 200-slot reserved block of null placeholders, so the catalog can grow without changing the layout.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------- | --------- |
| 2      | 2107 and later | 3474    | `fairyequipskill.bss` | 3,636 | 35 Skill Record, 200 Slot | 16        |
| 1      | 1230 to 1784   | 1784    | `fairyequipskill.bss` | 1,576 | 30 Skill Record, 100 Slot | 12        |

| Layout | File                  | Known            | Unknown       |
| ------ | --------------------- | ---------------- | ------------- |
| 2      | `fairyequipskill.bss` | 2,836 B (78.0%)  | 800 B (22.0%) |
| 1      | `fairyequipskill.bss` | 1,576 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2519   | Layout 2             |
| 2107   | Layout 2             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | Layout 1             |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

None. `fairyequipskill.bss` is a standalone catalog with no offset index.

| File                  | Required | Role                                             |
| --------------------- | -------- | ------------------------------------------------ |
| `languagedata_en.loc` | Optional | Skill names (`id4=0`) and descriptions (`id4=1`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

Total file size: 3636 bytes = 4 (magic) + 420 (catalog) + 3200 (reserved block) + 12 (trailer).

Records begin immediately at `+0x04`. There is **no** record count field; the catalog is terminated by the first record whose `equip_skill_id` is `200`.

| Offset              | Type                                      | Field         | Notes                                                       |
| ------------------- | ----------------------------------------- | ------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]                                   | magic         | `PABR` (ASCII)                                              |
| `+0x04`             | Skill Record[while equip_skill_id != 200] | skill_records | 35 x 12-byte skill records, `+0x004` to `+0x1A8`            |
| `skill_records+0x00` | Slot[..data_end]                         | slots         | Reserved block: 200 x 16-byte null placeholders, `+0x1A8` to `+0xE28` |
| `EOF-0x0C` | u32 | string_count | `0`: the PABR string table, here with no strings; `data_end` points at it |
| `EOF-0x08` | u32 | data_end | `0x0E28` (3624) = `file_size - 12`, the offset of `string_count` |
| `EOF-0x04` | u32 | zero | Always `0` |

`petequipskill.bss` carries the identical trailer (`data_end = 0x0EB0 = file_size - 12`), so this is a shared PABR convention rather than a fairy-specific field.

### Skill Record (12 bytes)

| Offset  | Type | Field          | Notes                                                  |
| ------- | ---- | -------------- | ------------------------------------------------------ |
| `+0x00` | u32  | equip_skill_id | Sequential record key, `0` to `34`; `200` marks the end |
| `+0x04` | u32  | skill_type     | Skill group, `1` to `8` (see Skill Types)              |
| `+0x08` | u16  | skill_level    | Skill level of the `gc::SkillKey`; always `1`          |
| `+0x0A` | u16  | skill_no       | Skill number (`SkillNo`); keys the name, description and icon |

Earlier versions of this doc called `skill_level` `tier`.

### Slot (16 bytes)

Two hundred unused catalog slots. Every record is `[u32 200][u32 0][u32 0][u32 0]`, where `200` is the null-entry sentinel. Skip these when parsing.

The stride here is 16 bytes, not the 12 used by live records; it matches the wider Section 2 record shape in `petequipskill.bss`, whose extended catalog is fully populated. In `fairyequipskill.bss` that extended section is entirely null.

| Offset  | Type      | Field          | Notes                                                                                                   |
| ------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32       | equip_skill_id | Always `200`, the null-entry sentinel                                                                   |
| `+0x04` | u32       | skill_type     | Always `0`                                                                                              |
| `+0x08` | u16       | skill_level    | Always `0`                                                                                              |
| `+0x0A` | u16       | skill_no       | Always `0`                                                                                              |
| `+0x0C` | u32       | unknown_0c     | Always `0`; the `petequipskill.bss` Slot's `unknown_0c`, and no extra u32 follows                       |


## Field Names

The client 1784 private server loads `Fairy_EquipSkill_Table` into one 24-byte entry per
record: `Index` (`equip_skill_id`) at `+0x00`, `GroupNo` (`skill_type`) at
`+0x04`, a runtime skill pointer at `+0x08` and a `gc::SkillKey` at `+0x10`.
The loader (VA `0x1409c8f13` to `0x1409c8f19`) writes the key as `(SkillNo << 16) | 1`, so its low u16
is the skill level (always `1`) and its high u16 the sheet's `SkillNo`. The
2016 client's `gc::SkillKey` is one `unsigned int _value` whose `getLevel()`
reads the low u16 and `getSkillNo()` the high u16, which places
`skill_level` at `+0x08` and `skill_no` at `+0x0A`. The server has no reader
for this file; the record is that entry in loader order without the pointer
and the padding. After loading, it looks up every key in the skill table and
logs "펫 착용 스킬에 알수 없는 스킬(%#)의 데이터가 있습니다!" ("pet equip
skill has data for an unknown skill (%#)!") for a missing one.
`petequipskill.bss` and `fairyequipskill.bss` share the entry, the loader
shape and the per-entry checks, which is why the fairy check logs the pet message.

The client 1784 build's own file matches `Fairy_EquipSkill_Table` on all
30 records (Index, GroupNo, level `1`, SkillNo); client 3474 has level `1`
on all 35. The null slots are the same struct with every field `0`.

LOC type 10 keys the skill name by `skill_no`
([`languagedata_loc.md`](languagedata_loc.md)). Earlier versions of this doc
read `+0x08` as two u8 fields (`unknown_08`, `unknown_09`) and named `+0x0A`
`loc_id`.

## Layout 1

On client 1784 the null-entry sentinel was `100`, not `200`, and every
Slot was 12 bytes, the size of a Skill Record. The File Layout and the Slot
differ from Layout 2; the Skill Record is the same. On client 1784 the file
holds 30 Skill Records and 100 Slots.

### File Layout

| Offset               | Type                                      | Field         | Notes                                                          |
| -------------------- | ----------------------------------------- | ------------- | -------------------------------------------------------------- |
| `+0x00`              | char[4]                                   | magic         | `PABR` (ASCII)                                                 |
| `+0x04`              | Skill Record[while equip_skill_id != 100] | skill_records | Ends at the first record whose `equip_skill_id` is `100`       |
| `skill_records+0x00` | Slot[..data_end]                          | slots         | 12-byte null placeholders up to `data_end`                     |
| `EOF-0x0C`           | u32                                       | string_count  | `0`: the PABR string table, here with no strings               |
| `EOF-0x08`           | u32                                       | data_end      | `file_size - 12`, the offset of `string_count`                 |
| `EOF-0x04`           | u32                                       | zero          | Always `0`                                                     |

### Slot (12 bytes)

| Offset  | Type     | Field          | Notes                                 |
| ------- | -------- | -------------- | ------------------------------------- |
| `+0x00` | u32      | equip_skill_id | Always `100`, the null-entry sentinel |
| `+0x04` | u32      | skill_type     | Always `0`                            |
| `+0x08` | u16      | skill_level    | Always `0`                            |
| `+0x0A` | u16      | skill_no       | Always `0`                            |
