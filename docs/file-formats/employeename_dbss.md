# `employeename.dbss` Format

## Purpose

Employee name table. Maps small employee name IDs to inline Korean UTF-16LE source names used by employee-related records. English display names are available through LOC `str_type=71`, `str_id1=employee_name_id`, `str_id3=12`.

Example:

```text
employee_name_id: 47 -> name: 가일
employee_name_id: 34 -> name: 필그레이브
LOC type=71 id1=47 id3=12 -> Guile
```

## Graph

### Tags

- file format
- dbss
- employee
- name table

### Connections

- [employeenameoffset.dbss](#employeenameoffsetdbss) - required byte-offset index into this file
- `employeespawnposition.dbss` - employee spawn records use matching small IDs for observed rows `1`-`5` and `41`-`50`
- [languagedata_en.loc](languagedata_loc.md) - English names with `str_type=71`, `str_id1=employee_name_id`, `str_id3=12`
- `employeestaticstatus.bss` - likely shares the same employee ID/name namespace, but the exact field position is not mapped here
- `employeeexp.bss` - likely shares the same employee ID/name namespace, but the exact field position is not mapped here

---

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `employeenameoffset.dbss` | Required | Maps employee name ID -> byte offset and record size |
| `languagedata_en.loc`     | Optional | English display name lookup                          |

Other extracted `employee*` files may reference the same employee ID/name namespace. `employeespawnposition.dbss` has a simple 34-byte fixed record shape and directly includes IDs found in this table; larger employee files need separate reverse-engineering before their foreign-key fields can be confirmed.

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of name records; observed `60` |

### Record Stream

The first record starts immediately at `+0x04`. Records are variable length and should be read through `employeenameoffset.dbss`.

| Offset  | Type               | Field   | Notes                     |
| ------- | ------------------ | ------- | ------------------------- |
| `+0x04` | Name Record[count] | records | Variable-length name rows |

---

## Record Structure

### Name Record (variable, `16 + char_count * 2` bytes)

| Offset  | Type                      | Field            | Notes                                               |
| ------- | ------------------------- | ---------------- | --------------------------------------------------- |
| `+0x00` | u32                       | employee_name_id | Matches ID in `employeenameoffset.dbss`             |
| `+0x04` | u32                       | char_count       | Number of UTF-16 code units in `name`               |
| `+0x08` | u32                       | unknown_0        | Always `0` in observed data                         |
| `+0x0C` | utf16le[`char_count` * 2] | name             | Inline Korean source name                            |
| varies  | u32                       | terminator       | Always `0` after the name text in observed data     |

Observed record sizes are `18`, `20`, `22`, `24`, and `26` bytes, matching names from 1 to 5 UTF-16 code units.

### employeenameoffset.dbss

Required offset index for `employeename.dbss`.

#### Header (4 bytes)

| Offset  | Type | Field | Notes                                                      |
| ------- | ---- | ----- | ---------------------------------------------------------- |
| `+0x00` | u32  | count | Number of offset rows; observed `60`, matching main file   |

#### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field            | Notes                                |
| ------- | ---- | ---------------- | ------------------------------------ |
| `+0x00` | u32  | employee_name_id | Key for a name record                |
| `+0x04` | u32  | offset           | Byte offset into `employeename.dbss` |
| `+0x08` | u32  | size             | Record byte count                    |

To read a name record: seek to `offset` in `employeename.dbss`, read `size` bytes, and parse the Name Record structure above.

---

## Suggested UI Layout

| Column           | Type | Notes                                    |
| ---------------- | ---- | ---------------------------------------- |
| employee_name_id | num  | Right-aligned primary key                                                        |
| Name             | text | Prefer LOC type `71`, id1 `employee_name_id`, id3 `12`; fall back to inline Korean |
| char_count       | num  | Useful for validation; hidden by default                                         |

---

## Notes

- Record order is not numeric: observed order starts `47` down to `32`, then `60` down to `48`, then `15` down to `1`, then `31` down to `16`.
- Every offset-row ID matches the `employee_name_id` stored at the beginning of its target record.
- Every observed `unknown_0` and trailing `terminator` is zero.
- English LOC matches were confirmed for sampled IDs: `47` -> Guile, `34` -> Pilgrave, `15` -> Neil Moss, `1` -> Philav, `60` -> Tails.
- `employeespawnposition.dbss` directly uses IDs from this table for observed rows `1`-`5` and `41`-`50`.

---

## Open Questions

### Employee Foreign Keys

Several related files contain values that overlap this table's IDs (`employeestaticstatus.bss`, `employeeexp.bss`, and other employee DBSS files), but those formats are not decoded enough to name exact fields here.
