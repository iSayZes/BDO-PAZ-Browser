# `npcsimply.bss` Format

## Purpose

Stores a compact NPC/knowledge-point lookup table. Each row maps a game object or NPC ID to inline Korean display strings and, for most rows, a `getknowledge(<id>);` action script that links the entry to a knowledge ID.

Example:

```text
npc_id: 113263  ->  name: 잭슨  ->  role: <과일상인>
npc_id: 5094013 ->  name: 자바르  ->  script: getknowledge(14923);
```

## Graph

### Tags

- file format
- bss
- npc
- knowledge

### Connections

- [languagedata_en.loc](languagedata_loc.md) - NPC and knowledge names can be localized through LOC where matching IDs exist
- [characterstatic.dbss](characterstatic_dbss.md) - also stores character/NPC IDs with `getknowledge(<id>);` scripts
- [exploration.bss](exploration_bss.md) - knowledge IDs resolve through LOC `str_type=34`

---

## File Layout

Top-level PABR block with a fixed-width record table followed by an inline string pool.

| Offset  | Type     | Field       | Notes                                      |
| ------- | -------- | ----------- | ------------------------------------------ |
| `+0x00` | char[4]  | magic       | ASCII `PABR`                               |
| `+0x04` | u32      | count       | Number of NPC records (observed: 2169)     |
| `+0x08` | record[] | records     | 33-byte records repeated `count` times     |
| varies  | pool     | string_pool | Counted string table referenced by records |

All multi-byte values are little-endian unless noted otherwise.

---

## Record Structure

### NPC Record (33 bytes, repeated `count` times)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | npc_id            | Row key; observed range includes normal NPC IDs and packed-looking IDs |
| `+0x04` | u32  | kind              | Category/type code; observed values 1-40                              |
| `+0x08` | u32  | script_ref        | String-pool index for a `getknowledge(...)` script on 2101 rows        |
| `+0x0C` | u32  | unknown_id        | Usually 0; non-zero on 58 rows                                         |
| `+0x10` | u16  | unknown_value     | Usually 0; non-zero on the same 58 rows as `unknown_id`                |
| `+0x12` | u16  | sentinel          | Usually `0xFFFF`; 0 on the same 58 rows as `unknown_id`                |
| `+0x14` | u8   | unknown_flag      | Usually 0; 1 on 32 rows                                                |
| `+0x15` | u32  | name_ref          | String-pool index for the Korean display name                          |
| `+0x19` | u32  | role_ref          | String-pool index for Korean role/title text; 0 when absent            |
| `+0x1D` | u32  | padding           | Always 0                                                              |

`script_ref`, `name_ref`, and `role_ref` are unaligned u32 values inside the 33-byte row. `name_ref` is usually `script_ref + 1` when the row has a script. `role_ref=0` means no role/title string.

### String Pool

The string pool begins immediately after the fixed record table:

```text
string_pool_offset = 0x08 + count * 33
```

Observed `string_pool_offset` is `0x117A1`.

| Offset  | Type        | Field        | Notes                                      |
| ------- | ----------- | ------------ | ------------------------------------------ |
| `+0x00` | u32         | string_count | Observed: 4626                             |
| `+0x04` | string[]    | strings      | Counted entries, indexed from 0            |
| EOF - 8 | bytes[8]    | trailer      | Observed trailing bytes after string table |

### String Entry

Most entries are UTF-8 Korean text with no encoding marker. UTF-16LE script entries have a one-byte marker before the length.

| Offset | Type       | Field        | Notes                                                    |
| ------ | ---------- | ------------ | -------------------------------------------------------- |
| `+0x00` | u8        | utf16_marker | Present only when value is `0x01`; omitted for UTF-8     |
| varies | u32        | byte_length  | Payload length in bytes                                  |
| varies | bytes      | payload      | UTF-8 when no marker; UTF-16LE when `utf16_marker=0x01`  |
| varies | u8         | terminator   | `0x00` when present; empty entry 0 is a single null byte |

String index 0 is an empty/null entry. Observed pool contents: 2576 UTF-8 strings and 2050 UTF-16LE strings.

---

## Suggested UI Layout

| Column       | Type | Notes                                                     |
| ------------ | ---- | --------------------------------------------------------- |
| NPC ID       | num  | `npc_id`                                                  |
| Kind         | num  | `kind`                                                    |
| Name         | text | `name_ref`; prefer English LOC match when available       |
| Role         | text | `role_ref`; Korean title/role, blank when `role_ref == 0` |
| Knowledge ID | num  | Parsed from `getknowledge(<id>);` in `script_ref`         |
| Script       | text | Raw script string for debugging/export                    |

---

## Notes

- The record table size is exactly `2169 * 33` bytes; fixed records end at `0x117A1`.
- `script_ref` points to a `getknowledge(<id>);` UTF-16LE string for 2101 of 2169 records.
- `name_ref` and `role_ref` point to Korean UTF-8 strings in the same pool. Role strings are often bracketed labels such as `<과일상인>` or `<거점관리인>`.
- `kind` distribution is heavily weighted toward value 4 (1160 rows), followed by 3 (216), 5 (120), 2 (103), and 16 (96).
- `unknown_id`, `unknown_value`, `sentinel=0`, and `unknown_flag=1` cluster on vendor/manager rows such as warehouse keepers, material vendors, and stable keepers.

---

## Open Questions

### What does `kind` encode?

The numeric `kind` field has 23 observed values in the range 1-40. It appears to classify NPC/simple-object type, but the mapping has not been confirmed.

### What are `unknown_id`, `unknown_value`, and `unknown_flag`?

These fields are mostly default but become non-zero together on 58 rows, with `unknown_flag=1` on 32 of those rows. They correlate with service NPC roles but need another table or runtime behavior to name safely.

### What is the 8-byte string-pool trailer?

The decoded string pool leaves 8 trailing bytes at EOF. Their purpose is not known; they may be padding or a small terminator block.
