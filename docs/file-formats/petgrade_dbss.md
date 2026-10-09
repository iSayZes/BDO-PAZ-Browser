# `petgrade.dbss` Format

## Purpose

Maps each (species, variant) pet combination to a grade value, one record per pair. 21 `pet.dbss` records have a pair with no grade record. Values 1–5 map to known grade labels; value 6 remains unconfirmed.

Example:

```text
species=1 (Cat), variant=6  →  grade=3 (Premium)
species=2 (Dog), variant=6  →  grade=1 (Classic)
species=25 (Airiss), ...    →  grade varies
```

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `petgradeoffset.dbss`  | Required | `(species,variant) → (data_offset, data_size)` lookup |

All multi-byte values are little-endian.

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                              |
| ------- | ---- | ----- | ---------------------------------- |
| `+0x00` | u32  | count | Number of records (observed: 203 before 2026-09-27, 282 after) |

### Record (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | key         | `(species << 8) \| variant`; low byte = variant, high byte = species |
| `+0x02` | u16  | -           | Always 0; padding                                                  |
| `+0x04` | u16  | key_dup     | Duplicate of `key`                                                 |
| `+0x06` | u16  | -           | Always 0; padding                                                  |
| `+0x08` | u32  | grade       | Pet grade for this (species, variant): 1 Classic, 2 Rare, 3 Premium, 4 Event, 5 Special, see In-Game Checks |

> The combined key is `(species << 8) | variant`, stored as a u16 followed by a zero u16. This matches the key format used in `petgradeoffset.dbss`.

## petgradeoffset.dbss

Provides O(1) lookup by (species, variant) key, one entry per main-file record.

### Header (4 bytes)

| Offset  | Type | Field | Notes                                   |
| ------- | ---- | ----- | --------------------------------------- |
| `+0x00` | u32  | count | Must equal `petgrade.dbss` count        |

### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | key         | `(species << 8) \| variant`; low byte = variant, high byte = species     |
| `+0x02` | u16  | -           | Always 0; padding                                                        |
| `+0x04` | u32  | data_offset | Absolute byte offset in `petgrade.dbss` past the 4-byte key prefix      |
| `+0x08` | u32  | data_size   | Always 8 (= record size minus the 4-byte key prefix)                    |

`record_start = data_offset - 4` gives the position of the full 12-byte record in the main file.
The parser reads `key` and the padding as one u32 (`parse_bare_u32_offset_rows()`).

## Joining with pet.dbss

To enrich a `pet.dbss` record with its `grade`:

```python
lookup_key = (species << 8) | variant  # both from pet.dbss record
grade = grade_map.get((species, variant), None)
```

where `grade_map` is built from `petgradeoffset.dbss` as `{(species, variant): grade}`.

## Notes

- Before the 2026-09-27 client update: 203 (species, variant) pairs for 1,782 pet records, about 8.8 records per pair across pet tiers. After it: 282 pairs for 2,009 pet records; all 79 new pairs have grade 2.
- `grade` observed range: 1–6. Values 1–5 map to Classic, Rare, Premium, Event, Special: the order of `_gradeStrConfig` in `panel_window_petfusion_all.luac` (`LUA_PETCOMPOSE_SAME_GRADETYPE_CLASSIC_TITLE`, `_LIMITED_` shown as "RARE", `_PREMIUM_`, `_EVENT_`, `_SPECIAL_`). Grade 4 is Kuku, Young Rauno, Young Fogan and Young Pomi. Value 6 remains unconfirmed.
- Record order in the main file differs from offset file order (the offset file is an arbitrary-order index, not sequential).
- The key encoding `(species << 8) | variant` appears only in this file pair; `pet.dbss` stores `variant` and `species` as separate bytes at `+0x02` and `+0x03`.

## In-Game Checks

### Grade Value 6

Needs item (all):

- [[Pet] Pit-A-Pat Mole](https://bdocodex.com/us/item/47983/)
- [[Pet] Young Crimson Dragon](https://bdocodex.com/us/item/18480/)

Values 1 to 5 map to the five fusion window grade titles, but the Lua lists no sixth title, and only the 5 Mole records carry value 6. They are the Pit-A-Pat Mole (item 47983, pets 55749 to 55752 and 56594). bdocodex (2026-10-07) shows the Pit-A-Pat Mole as Type: Special. Its pet type follows this field, since it shows Young Rauno (grade 4) as Event and Young Crimson Dragon (grade 5) as Special, but it could map 6 to Special by its own fallback. Its item page also says the Mole "can only be Exchanged with pets of the same kind", a line the Young Crimson Dragon page does not carry.

Put the Pit-A-Pat Mole in the pet exchange window and read the grade title, then try to add the Young Crimson Dragon. A Special title and an accepted Dragon mean 6 is a second Special value. No title, or a window that takes only other Moles, means 6 is a grade of its own that the fusion window has no title for.
