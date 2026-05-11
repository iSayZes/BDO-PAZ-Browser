# `petgrade.dbss` Format

## Purpose

Maps each (species, variant) pet combination to a `grade_count` value. 203 records cover all distinct (species, variant) pairs present in `pet.dbss`. The meaning of `grade_count` is not fully confirmed — values range 1–6 and do not directly correspond to the number of grade tiers the pet appears at in `pet.dbss`.

Example:

```text
species=1 (Cat), variant=6  →  grade_count=3
species=2 (Dog), variant=6  →  grade_count=1
species=25 (Airiss), ...    →  grade_count varies
```

## Graph

### Tags

- file format
- dbss
- pet

### Connections

- [pet.dbss](pet_dbss.md) — join on `(species << 8) | variant` to enrich pet records with grade_count
- [petgradeoffset.dbss](petgrade_dbss.md#petgradeoffsetdbss) — keyed offset index for this file

---

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `petgradeoffset.dbss`  | Required | `(species,variant) → (data_offset, data_size)` lookup |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                              |
| ------- | ---- | ----- | ---------------------------------- |
| `+0x00` | u32  | count | Number of records (observed: 203)  |

### Record (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | variant     | Matches `variant` (`+0x02`) in `pet.dbss`                          |
| `+0x02` | u16  | species     | Matches `species` (`+0x03`) in `pet.dbss`                          |
| `+0x04` | u16  | variant_dup | Always equal to `variant`; purpose unknown                         |
| `+0x06` | u16  | species_dup | Always equal to `species`; purpose unknown                         |
| `+0x08` | u32  | grade_count | Number of grade tiers for this (species, variant) — see Open Questions |

> The combined key is `(species << 8) | variant`, stored as a u32 with the upper 2 bytes zero. This matches the key format used in `petgradeoffset.dbss`.

---

## petgradeoffset.dbss

Provides O(1) lookup by (species, variant) key. 203 entries, one per main-file record.

### Header (4 bytes)

| Offset  | Type | Field | Notes                                   |
| ------- | ---- | ----- | --------------------------------------- |
| `+0x00` | u32  | count | Must equal `petgrade.dbss` count        |

### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | key         | `(species << 8) \| variant`; low byte = variant, high byte = species     |
| `+0x02` | u16  | —           | Always 0; padding                                                        |
| `+0x04` | u32  | data_offset | Absolute byte offset in `petgrade.dbss` past the 4-byte key prefix      |
| `+0x08` | u32  | data_size   | Always 8 (= record size minus the 4-byte key prefix)                    |

`record_start = data_offset - 4` gives the position of the full 12-byte record in the main file.

---

## Joining with pet.dbss

To enrich a `pet.dbss` record with its `grade_count`:

```python
lookup_key = (species << 8) | variant  # both from pet.dbss record
grade_count = grade_map.get((species, variant), None)
```

where `grade_map` is built from `petgradeoffset.dbss` as `{(species, variant): grade_count}`.

---

## Notes

- 203 unique (species, variant) pairs; 1782 total pet records → average ~8.8 records per pair (one per grade level × number of grade levels).
- `grade_count` observed range: 1–6. Values do not equal the number of grade tiers a pet appears at in `pet.dbss` — e.g. Cat variant=5 has `grade_count=1` but appears at grades 1–4.
- Record order in the main file differs from offset file order (the offset file is an arbitrary-order index, not sequential).
- The key encoding `(species << 8) | variant` appears only in this file pair; `pet.dbss` stores `variant` and `species` as separate bytes at `+0x02` and `+0x03`.

---

## Open Questions

### `grade_count` semantics

Confirmed range 1–6; does not match the observed number of grade records per (species, variant) in `pet.dbss`. Possible interpretations: number of upgrade stages, a quality tier grouping, or an index into a separate upgrade-cost table. Requires cross-referencing against in-game upgrade UI or another binary file.

