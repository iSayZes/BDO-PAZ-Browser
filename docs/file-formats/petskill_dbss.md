# `petskill.dbss` Format

## Purpose

Defines pet skill effect tables. Each record is keyed by `pet_skill_id` and contains one baseline row plus ten level rows for a single pet skill group. Companion `petskilloffset.dbss` provides keyed lookup into the variable-size record stream.

Example:

```text
pet_skill_id: 47 -> skill_group: 11
level 1 raw_value_a: 3,584,000
level 10 raw_value_a: 1,280,000
```

## Graph

### Tags

- file format
- dbss
- pet
- skill
- companion

### Connections

- [petskilloffset.dbss](petskill_dbss.md#petskilloffsetdbss) — keyed offset index for this file
- [pet.dbss](pet_dbss.md) — pet records reference pet skill systems through related skill fields
- [petequipskill.bss](petequipskill_bss.md) — separate pet equip-skill catalog; not the same table

---

## Companion Files

| File                   | Required | Role                                                |
| ---------------------- | -------- | --------------------------------------------------- |
| `petskilloffset.dbss`  | Required | `pet_skill_id -> (data_offset, data_size)` lookup   |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                         |
| ------- | ---- | ----- | ----------------------------- |
| `+0x00` | u32  | count | Number of records; observed 49 |

Records begin immediately at `+0x04`. Each record is stored as a 2-byte key prefix followed by the data payload addressed by `petskilloffset.dbss`.

---

## Record Structure

### Record Wrapper

| Offset  | Type | Field        | Notes                                                |
| ------- | ---- | ------------ | ---------------------------------------------------- |
| `+0x00` | u16  | key_prefix   | Equals `pet_skill_id`                                |
| `+0x02` | ...  | data_payload | `data_size` bytes; offset table points to this field |

### Data Payload (189 or 190 bytes)

| Offset  | Type      | Field           | Notes                                                                 |
| ------- | --------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16       | pet_skill_id    | Equals the 2-byte key prefix and offset-table key                     |
| `+0x02` | row[11]   | effect_rows     | One baseline row (`row_index=0`) plus ten level rows (`1..10`)        |
| `+0xBD` | u8        | extra_marker    | Present only when `data_size=190`; observed values 9 and 10           |

The 32 records with `data_size=189` end after the eleven 17-byte rows. The 17 records with `data_size=190` have one trailing `extra_marker` byte.

### Effect Row (17 bytes × 11)

Rows start at payload offset `+0x02 + row_index * 17`.

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | skill_group  | Skill group code; observed 1–11. Same value in all rows for a record                    |
| `+0x01` | u8   | row_level    | Row 0 uses 1; rows 1–10 use 1–10                                                        |
| `+0x02` | u16  | —            | Always 0                                                                                |
| `+0x04` | u32  | raw_value_a  | Primary effect value. Row 0 is always 2560; rows 1–10 vary by `pet_skill_id`            |
| `+0x08` | u32  | raw_value_b  | Secondary effect value. Row 0 is always 2560; rows 1–10 are 0 or a skill-specific value |
| `+0x0C` | u32  | row_marker   | Row 0 = 256; rows 1–9 = `(row_level + 1) * 256`; row 10 is 0 or 256                     |
| `+0x10` | u8   | —            | Always 0                                                                                |

---

## petskilloffset.dbss

### Header (4 bytes)

| Offset  | Type | Field | Notes                                  |
| ------- | ---- | ----- | -------------------------------------- |
| `+0x00` | u32  | count | Must equal `petskill.dbss` count (49)  |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_skill_id| Matches `pet_skill_id` in the main record                                   |
| `+0x02` | u32  | data_offset | Absolute byte offset in `petskill.dbss` to the payload, after key prefix    |
| `+0x06` | u16  | data_size   | 189 or 190 bytes                                                            |
| `+0x08` | u16  | —           | Always 0                                                                    |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix.

---

## Observed Values

| Field              | Observed values / range                                      |
| ------------------ | ------------------------------------------------------------ |
| `pet_skill_id`     | 1–6, 11–18, 21–23, 26–57 (49 records total)                  |
| `skill_group`      | 1–11                                                         |
| `row_level`        | baseline row uses 1; level rows use 1–10                     |
| `raw_value_a`      | row 0 always 2560; level rows 512,000–128,000,000            |
| `raw_value_b`      | row 0 always 2560; level rows 0–76,800,000                   |
| `row_marker`       | 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 0   |
| `extra_marker`     | 9 or 10 when present                                         |

`skill_group` is not unique: multiple `pet_skill_id` records can share one group while carrying different effect values.

---

## Suggested UI Layout

| Column        | Type | Notes                                               |
| ------------- | ---- | --------------------------------------------------- |
| Pet Skill ID  | num  | `pet_skill_id`, right-aligned                       |
| Skill Group   | num  | `skill_group` from row 0                            |
| Level         | num  | `row_level`; show level rows 1–10 under each record |
| Value A       | num  | `raw_value_a`; display raw until scale is confirmed |
| Value B       | num  | `raw_value_b`; display raw until scale is confirmed |

For compact browsing, show one expandable row per `pet_skill_id`, with the ten level rows nested beneath it.

---

## Notes

- File size is 9380 bytes: 4-byte count plus 49 wrapper records.
- `petskilloffset.dbss` size is 494 bytes: 4-byte count plus 49 × 10-byte offset rows.
- All offset-table padding fields are 0.
- Offset rows are sorted descending for high IDs first, not ascending by key.
- `raw_value_a` and `raw_value_b` are named as raw values because the display scale is not confirmed. Some values are multiples of 256, 256,000, or 25,600,000.
- This file is distinct from `petequipskill.bss`, which stores localized equip-skill catalog entries.

---

## Open Questions

### Skill group names

`skill_group` values 1–11 likely identify pet skill/effect categories, but the authoritative mapping to UI names has not been confirmed from this file alone.

### Raw value scale

`raw_value_a`, `raw_value_b`, and `row_marker` appear scaled in several different ways. The correct display formula needs confirmation from UI code or in-game pet skill percentage displays.

### Baseline row meaning

Row 0 is identical across all records except `skill_group`: `raw_value_a=2560`, `raw_value_b=2560`, `row_marker=256`. It may be a base display/effect row, but its exact role is not confirmed.

### Extra marker byte

Only 17 records have a trailing `extra_marker` byte. Values are 9 or 10, but its relationship to `skill_group`, max level, or UI display is unknown.
