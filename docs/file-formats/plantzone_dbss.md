# `plantzone.dbss` Format

## Purpose

Defines plant-zone records. Each record has a zone ID, several invariant control fields, one variant byte, a linked ID field, and a short list of u8 values that appears to classify the zone's plant/spawn set. `plantzoneoffset.dbss` is required to address the variable-length records.

```text
Observed records: 394. Record payloads are 32, 34, or 37 bytes depending on the trailing value-list length.
```

## Graph

### Tags

- file format
- dbss
- plant
- zone

### Connections

- `plantzoneoffset.dbss` - required offset table for `plantzone.dbss`

---

## Companion Files

| File                   | Required | Role                                                   |
| ---------------------- | -------- | ------------------------------------------------------ |
| `plantzoneoffset.dbss` | Required | Maps `record_id` to byte offset and payload byte count |

All multi-byte values are little-endian unless noted otherwise.

---

## File Layout

| Offset  | Type | Field         | Notes                                      |
| ------- | ---- | ------------- | ------------------------------------------ |
| `+0x00` | u32  | record_count  | Number of records; observed `394`          |
| `+0x04` | ...  | record_stream | Variable-length records, packed back-to-back |

`(file_size - 4) / record_count` is not integral, so records must be sliced with `plantzoneoffset.dbss`.

---

## Record Structure

### Plant Zone Record (32, 34, or 37 bytes)

| Offset  | Type | Field        | Notes                                                                 |
| ------- | ---- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32  | record_id    | Primary zone ID; matches `record_id` in `plantzoneoffset.dbss`        |
| `+0x04` | u32  | unknown_04   | Always observed as `2`                                                |
| `+0x08` | u32  | unknown_08   | Always observed as `0`                                                |
| `+0x0C` | u16  | unknown_0c   | Always observed as `2`                                                |
| `+0x0E` | u8   | variant      | Observed range `0`-`4`                                                |
| `+0x0F` | u16  | unknown_0f   | Always observed as `101`; note unaligned offset                       |
| `+0x11` | u16  | unknown_11   | Always observed as `201`; note unaligned offset                       |
| `+0x13` | u32  | unknown_13   | Always observed as `1`; note unaligned offset                         |
| `+0x17` | u32  | linked_id    | Usually a direct ID; some records use high 16 bits as a small group   |
| `+0x1B` | u32  | value_count  | Number of trailing `values`; observed `1`, `3`, or `6`                |
| `+0x1F` | u8[] | values       | `value_count` one-byte values                                         |

Observed record-size distribution:

| Size | Count | `value_count` | `values` pattern       |
| ---- | ----- | ------------- | ---------------------- |
| 32   | 2     | 1             | `06`                   |
| 34   | 42    | 3             | `06 07 08`             |
| 37   | 350   | 6             | `00 01 02 03 04 05`    |

### `linked_id`

Most `linked_id` values fit in the low 16 bits. Nineteen records use non-zero high 16 bits:

| High 16 bits | Count | Low 16-bit range |
| ------------ | ----- | ---------------- |
| `0`          | 375   | `1`-`2044`       |
| `1`          | 3     | `960`-`1235`     |
| `2`          | 6     | `23`-`1213`      |
| `3`          | 2     | `962`-`970`      |
| `4`          | 2     | `963`-`971`      |
| `5`          | 2     | `972`-`975`      |
| `6`          | 2     | `973`-`976`      |
| `7`          | 2     | `974`-`977`      |

The high bits look intentional rather than padding because the field is otherwise a normal unaligned u32 and the low 16-bit value stays in the same ID range as other records.

---

## `plantzoneoffset.dbss`

Provides the byte ranges for records in `plantzone.dbss`.

| Offset  | Type | Field        | Notes                             |
| ------- | ---- | ------------ | --------------------------------- |
| `+0x00` | u32  | record_count | Must equal `plantzone.dbss` count |
| `+0x04` | ...  | rows         | 12-byte rows repeated `count` times |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                             |
| ------- | ---- | ----------- | ------------------------------------------------- |
| `+0x00` | u16  | record_id   | Matches `plantzone.dbss` record `+0x00`           |
| `+0x02` | u16  | zero        | Always observed as `0`                            |
| `+0x04` | u32  | data_offset | Absolute byte offset into `plantzone.dbss`        |
| `+0x08` | u32  | data_size   | Record payload byte count: `32`, `34`, or `37`    |

Offset rows are not sorted by `data_offset`, but sorted rows cover every byte from `plantzone.dbss +0x04` through EOF with no gaps or overlaps.

---

## Suggested UI Layout

| Column     | Type | Notes                                         |
| ---------- | ---- | --------------------------------------------- |
| Zone ID    | num  | `record_id`                                   |
| Variant    | num  | `variant`                                     |
| Linked ID  | num  | Show as full u32; optionally also show high/low parts |
| Values     | text | Render `values` as comma-separated integers   |
| Data Size  | num  | Useful for debugging `value_count` classes    |

---

## Notes

- `plantzone.dbss` and `plantzoneoffset.dbss` both report `394` records.
- The offset table's `record_id` equals the record payload's first u32 for all records.
- `value_count` always equals the number of trailing bytes.
- Values appear as three fixed sets in observed data: `[0, 1, 2, 3, 4, 5]`, `[6, 7, 8]`, and `[6]`.
- No localization relationship was found; this format appears numeric-only in observed files.

---

## Open Questions

### Semantic Names

The meanings of `variant`, `linked_id`, and the trailing `values` enum are not confirmed. The byte layout is stable, but additional cross-reference data or in-game evidence is needed before naming these as gameplay concepts.
