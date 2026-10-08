# `employeename.dbss` Format

## Purpose

Employee name table. Maps small employee name IDs to inline Korean UTF-16LE source names used by employee-related records. English display names are available through LOC `str_type=71`, `str_id1=employee_name_id`, `str_id3=12`.

Example:

```text
employee_name_id: 47 -> name: 가일
employee_name_id: 34 -> name: 필그레이브
LOC type=71 id1=47 id3=12 -> Guile
```

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `employeenameoffset.dbss` | Required | Maps employee name ID -> byte offset and record size |
| `languagedata_en.loc`     | Optional | English display name lookup                          |

Other extracted `employee*` files may reference the same employee ID/name namespace. `employeespawnposition.dbss` keys (1 to 5, 41 to 50) fall in this table's ID range but are spawn position keys, not name IDs (see [employeespawnposition](employeespawnposition_dbss.md)); larger employee files need separate reverse-engineering before their foreign-key fields can be confirmed.

All multi-byte values are little-endian.

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of name records; observed `60` in the pre-2026-09-27 fixture and in the 2026-09-27 client |

### Record Stream

The first record starts immediately at `+0x04`. Records are variable length and should be read through `employeenameoffset.dbss`.

| Offset  | Type               | Field   | Notes                     |
| ------- | ------------------ | ------- | ------------------------- |
| `+0x04` | Name Record[count] | records | Variable-length name rows |

## Record Structure

### Name Record (variable, `16 + char_count * 2` bytes)

| Offset  | Type                      | Field            | Notes                                               |
| ------- | ------------------------- | ---------------- | --------------------------------------------------- |
| `+0x00` | u32                       | employee_name_id | Matches ID in `employeenameoffset.dbss`             |
| `+0x04` | u32                       | char_count       | Number of UTF-16 code units in `name`               |
| `+0x08` | u32                       | unknown_08       | Always `0` in observed data                         |
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

## Suggested UI Layout

| Column            | Type | Notes                                          |
| ----------------- | ---- | ---------------------------------------------- |
| Employee Name ID  | num  | `employee_name_id`                             |
| Name              | text | LOC name, falling back to the inline Korean    |

## Notes

- Record order is not numeric: observed order starts `47` down to `32`, then `60` down to `48`, then `15` down to `1`, then `31` down to `16`.
- Every offset-row ID matches the `employee_name_id` stored at the beginning of its target record.
- Every observed `unknown_08` and trailing `terminator` is zero. Earlier versions of this doc called `unknown_08` `unknown_0`.
- English LOC matches were confirmed for sampled IDs: `47` -> Guile, `34` -> Pilgrave, `15` -> Neil Moss, `1` -> Philav, `60` -> Tails.
- Earlier versions of this doc read the `employeespawnposition.dbss` keys `1`-`5` and `41`-`50` as IDs from this table. They are spawn position keys that `employeespawninfo.dbss` lists per sailor character; the overlap is by value only.

## Open Questions

### Employee Foreign Keys

None of the decoded sailor files hold an ID from this table. `employeestaticstatus.bss` and `employeeexp.bss` key their rows by sailor key (`1` to `29` and `1` to `23`), see [employeestaticstatus](employeestaticstatus_bss.md) and [employeeexp](employeeexp_bss.md); `employeespawnposition.dbss` keys are spawn position keys, and `employeespawninfo.dbss` holds a sailor key (`1` to `20`) and spawn position keys, see [employeespawninfo](employeespawninfo_dbss.md). Other employee DBSS files contain values that overlap this table's IDs, but those formats are not decoded enough to name exact fields here.
