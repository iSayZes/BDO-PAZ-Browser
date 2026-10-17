# `fairyequipskill.bss` Format

## Purpose

Defines the fairy skill catalog, the 35 skills a fairy can hold, grouped into 8 skill types with tier progressions (e.g. `Tingling Breath I`–`V`). Each record stores its skill type group, an unknown byte (`unknown_08`), and a localization ID that resolves to both the skill name and its effect description, and that doubles as the icon filename number.

The remainder of the file is a 200-slot reserved block of null placeholders, so the catalog can grow without changing the layout.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------- | --------- |
| 2      | 3473 and later | 3474    | `fairyequipskill.bss` | 3,636 | 35 Skill Record, 200 Slot | 16        |
| 1      | 1784           | 1784    | `fairyequipskill.bss` | 1,576 | 30 Skill Record, 100 Slot | 12        |

| Layout | File                  | Known           | Unknown         |
| ------ | --------------------- | --------------- | --------------- |
| 2      | `fairyequipskill.bss` | 1,166 B (32.1%) | 2,470 B (67.9%) |
| 1      | `fairyequipskill.bss` | 716 B (45.4%)   | 860 B (54.6%)   |

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
| `+0x08` | u8   | unknown_08     | Always `1` in all 35 observed records                  |
| `+0x09` | u8   | unknown_09     | Always `0`                                             |
| `+0x0A` | u16  | loc_id         | Localization key to skill name/description, icon number |

Earlier versions of this doc called `unknown_08` `tier`.

### Slot (16 bytes)

Two hundred unused catalog slots. Every record is `[u32 200][u32 0][u32 0][u32 0]`, where `200` is the null-entry sentinel. Skip these when parsing.

The stride here is 16 bytes, not the 12 used by live records; it matches the wider Section 2 record shape in `petequipskill.bss`, whose extended catalog is fully populated. In `fairyequipskill.bss` that extended section is entirely null.

| Offset  | Type      | Field          | Notes                                                                                                   |
| ------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32       | equip_skill_id | Always `200`, the null-entry sentinel                                                                   |
| `+0x04` | bytes[12] | unknown_04     | Always `0`; the place of `skill_type`, `unknown_08`, `unknown_09`, `loc_id` and `unknown_0c` in the `petequipskill.bss` Slot |

`unknown_08` is always `1`, matching `petequipskill.bss` where the same byte is also invariably `1`. Whether it distinguishes fairy grades, marks records as active, or is vestigial cannot be determined from the data alone.

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
| `+0x04` | bytes[8] | unknown_04     | Always `0`                            |
