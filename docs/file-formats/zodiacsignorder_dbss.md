# `zodiacsignorder.dbss` Format

## Purpose

The order in which the stars of a zodiac constellation light up, per
personality type: 2 variants x 12 signs = 24 records. The stars are the
`star_positions` of [`zodiacsign.dbss`](zodiacsign_dbss.md), and
`personality_type` is the one `npcpersonality.dbss` uses.

Example:

```text
personality 701  Owl Treant, variant 1
  triggers 6     0 -> 1 -> 2 -> 3 -> 1 -> 2
```

## Companion Files

| File                         | Required | Role                                          |
| ---------------------------- | -------- | --------------------------------------------- |
| `zodiacsignorderoffset.dbss` | Required | ID-keyed index into this file, see below      |
| `languagedata_en.loc`        | Optional | Zodiac sign names (7)                         |

All multi-byte values are little-endian.

## File Layout

Records are **not** stored sequentially; use the offset file to locate them.

### Header (4 bytes)

| Offset  | Type | Field | Notes                    |
| ------- | ---- | ----- | ------------------------ |
| `+0x00` | u32  | count | Number of records (= 24) |

### Record (variable, 21 to 27 bytes)

| Offset  | Type                      | Field                | Notes                                               |
| ------- | ------------------------- | -------------------- | --------------------------------------------------- |
| `+0x00` | u16                       | personality_type     | `major × 100 + variant`; range 101 to 1202          |
| `+0x02` | u16                       | trigger_count        | Total trigger steps = `1 + len(step_indices)`       |
| `+0x04` | u32                       | reserved_a           | Always 0                                            |
| `+0x08` | u32                       | reserved_b           | 0 for variant 1; variant 2 may have non-zero values |
| `+0x0C` | u16 × (trigger_count − 1) | step_indices         | 0-indexed slot indices for steps 1 onward           |
| -       | u8                        | zodiac_id            | Which zodiac sign (1 to 12)                         |
| -       | u16                       | personality_type_dup | Duplicate of `personality_type` at `+0x00`          |

`trigger_order` (as used in-game) = `[0] + list(step_indices)`. The first trigger is always slot 0.

`slots` = `zodiacsign.float_count` for that `zodiac_id`.

### zodiacsignorderoffset.dbss

#### Offset Record (10 bytes, repeated 24 times)

| Offset  | Type | Field            | Notes                                                              |
| ------- | ---- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | personality_type | Matches `personality_type` in the main record                      |
| `+0x02` | u32  | data_offset      | Byte offset into `zodiacsignorder.dbss`; 2 bytes past record start |
| `+0x06` | u16  | data_size        | Size of record data (excluding leading `personality_type` u16)     |
| `+0x08` | u16  | padding          | Always 0                                                           |

`record_start = data_offset - 2`

## Suggested UI Layout

| Column      | Type | Notes                                                            |
| ----------- | ---- | ---------------------------------------------------------------- |
| Personality | num  | `personality_type`                                               |
| Row         | num  | Record index in the offset file                                  |
| Zodiac      | text | Sign name of `personality_type // 100` (LOC str_type=7, str_id4=0) |
| Variant     | num  | `personality_type % 100`                                         |
| Triggers    | num  | `trigger_count`                                                  |
| Sequence    | text | `trigger_order` joined with arrows (`0→1→2→3→1→2`)               |

## Notes

- Variant 2 `step_indices` typically differ from variant 1; they are an alternate drawing order. Variant 1 is usually the canonical forward order; variant 2 may reverse or reorder steps.
- Major 9 (Key): only `personality_type` 901 exists in `npcpersonality.dbss`, but `zodiacsignorder.dbss` defines both 901 and 902.
