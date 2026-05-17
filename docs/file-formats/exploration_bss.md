# `exploration.bss` Format

## Purpose

Stores exploration knowledge entries. The primary key is a knowledge ID that resolves through LOC `str_type=34`, including the display name, description, and hint/role strings used for knowledge entries and exploration NPCs.

Example:

```text
knowledge_id=65 -> Cron Castle Altar
knowledge_id=1008 -> Altin
```

## Graph

### Tags

- file format
- bss
- exploration
- knowledge

### Connections

- [languagedata.loc](languagedata_loc.md) - resolves `knowledge_id` via LOC `str_type=34`

---

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves `knowledge_id` to knowledge name, description, and hint text |

All multi-byte values are little-endian unless noted otherwise.

---

## File Layout

| Offset  | Type    | Field        | Notes                                                   |
| ------- | ------- | ------------ | ------------------------------------------------------- |
| `+0x00` | char[4] | magic        | `PABR` (ASCII)                                          |
| `+0x04` | u32     | record_count | Observed `1003`                                         |
| `+0x08` | record  | records      | Variable-width records discovered by the anchor pattern |

---

## Record Structure

### Exploration Entry (variable size, repeated `record_count` times)

Records are variable-width. The confirmed anchor is `knowledge_id`, followed six bytes later by the same value. The current parser scans for that anchor and stops when `record_count` entries have been found.

| Offset  | Type | Field                  | Notes                                                                |
| ------- | ---- | ---------------------- | -------------------------------------------------------------------- |
| `+0x00` | u32  | knowledge_id           | LOC `str_type=34`, `str_id1=knowledge_id`                            |
| `+0x04` | u16  | unknown_flags          | Often `1`; variant rows combine bit/flag values such as `0x0201`     |
| `+0x06` | u32  | duplicate_knowledge_id | Repeats `knowledge_id`; used as the structural anchor                |
| `+0x0A` | u32  | group_id               | Small grouping/order value; not globally unique                      |
| `+0x0E` | u8   | enabled                | Observed `0` or `1`                                                  |
| `+0x10` | u8   | unknown_flag_a         | Boolean-like flag                                                    |
| `+0x11` | u8   | unknown_flag_b         | Boolean-like flag                                                    |
| `+0x12` | u8   | unknown_flag_c         | Boolean-like flag                                                    |
| `+0x13` | u8   | unknown_marker         | Small marker/variant byte                                            |
| `+0x17` | u32  | anchor_id_a            | Often repeated by `anchor_id_b`; exact target table is not confirmed |
| `+0x1B` | u32  | anchor_id_b            | Often repeats `anchor_id_a`                                          |
| `+0x1F` | f32  | radius                 | Confirmed float-like value; examples `2700.0`, `9700.0`              |
| `+0x23` | f32  | radius_squared         | Square of `radius` for common rows                                   |

---

## Suggested UI Layout

| Column         | Type | Notes                                   |
| -------------- | ---- | --------------------------------------- |
| Knowledge ID   | num  | Primary LOC key                         |
| Knowledge Name | text | LOC type 34, `str_id4=0` when available |
| Group ID       | num  | Small grouping/order value              |
| Enabled        | num  | Raw enabled byte                        |
| Anchor ID      | num  | `anchor_id_a`                           |
| Radius         | num  | Formatted float                         |

---

## Notes

- The file has no same-stem companion in the current PAZ listing.
- LOC type 34 resolves the first entries as `65` -> `Cron Castle Altar`, `1008` -> `Altin`, and `1053` -> `Rohu`.
- The confirmed anchor scan finds exactly `1003` records, matching the file header count.

---

## Open Questions

### Full Variable Payload Layout

Bytes after the confirmed anchor fields include variable payloads and nested ID lists. The parser exposes stable leading fields for preview/search, but the meaning of all trailing per-record payload data is not fully mapped yet.

### Anchor ID Target

`anchor_id_a` and `anchor_id_b` often repeat each other, but the referenced table or game object namespace has not been confirmed.
