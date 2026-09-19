# `petequipskillaquire.dbss` Format

## Purpose

Defines the **skill roll table** for pet equip skills, keyed by `acquire_type_id` from [pet.dbss](pet_dbss.md). Each record holds a weight for every skill in [petequipskill.bss](petequipskill_bss.md), and a weight of `0` means that acquire type cannot roll that skill.

Each acquire type is a themed pool: some favour life skills, others combat and gathering. 21 records cover 5 key groups (`0`–`4`, `101`–`104`, `201`–`204`, `301`–`304`, `401`–`404`), of which key `0` is an empty placeholder.

Example:

```text
acquire_type_id 204 → Karma Recovery +5%: weight 160000 of 750000 = 21.3%
acquire_type_id 401 → Combat EXP +5%:     weight 120000 of 700000 = 17.1%
acquire_type_id 401 → Cooking EXP +5%:    weight  10000 of 700000 =  1.4%
```

## Graph

### Tags

- file format
- dbss
- pet
- equip skill
- drop rate

### Connections

- [pet.dbss](pet_dbss.md), `acquire_type_id` field keys into this file
- [petequipskill.bss](petequipskill_bss.md), the skill catalog; weights are indexed by its `equip_skill_id`
- [petequipskillaquireoffset.dbss](#petequipskillaquireoffsetdbss), keyed offset index
- [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), identical record layout for fairies

---

## Companion Files

| File                             | Required | Role                                                 |
| -------------------------------- | -------- | ---------------------------------------------------- |
| `petequipskillaquireoffset.dbss` | Required | `acquire_type_id → (data_offset, data_size)` index   |
| `petequipskill.bss`              | Optional | Resolves a weight's `equip_skill_id` to a skill name |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                            |
| ------- | ---- | ----- | -------------------------------- |
| `+0x00` | u32  | count | Number of records; observed `21` |

### Record (176 bytes, repeated `count` times)

| Offset  | Type    | Field      | Notes                                          |
| ------- | ------- | ---------- | ---------------------------------------------- |
| `+0x00` | u32     | packed_key | `(acquire_type_id << 16) \| acquire_type_id`   |
| `+0x04` | u32[43] | weights    | Roll weight per `equip_skill_id`               |

`4 + 43 × 4 = 176` bytes exactly. `weights[i]` is the weight of the skill whose `equip_skill_id` is `i` in Section 1 of the catalog; index `0` is the first weight, **not** a reserved field.

The first 2 bytes of each record are the file key prefix. The offset companion points to `record_start + 2`, so use `record_start = data_offset - 2` to read the full u32-aligned record.

---

## Acquire Type IDs

Keys decompose as `group × 100 + tier`, except the low keys `0`–`4` which have group `0`.

| Key group   | Meaning                                              |
| ----------- | ---------------------------------------------------- |
| `0`         | Empty placeholder, all 43 weights are `0`           |
| `1`–`4`     | Life-skill oriented pool                             |
| `101`–`104` | Hunting / Training / Trading / Fishing oriented pool |
| `201`–`204` | Combat, Gathering and Fishing oriented pool          |
| `301`–`304` | Byte-identical to `201`–`204`                        |
| `401`–`404` | Broad, near-even pool across most skills             |

---

## Rollable Skills

Only 14 of the catalog's 43 Section 1 entries carry a non-zero weight in any record, and the same 14 appear in every populated record. Each is the **middle** entry of its three-entry skill type group, the `+5%` tier, or the sole entry where the group has only one.

| equip_skill_id | skill_type | Skill               |
| -------------- | ---------- | ------------------- |
| 1              | 1          | Karma Recovery +5%  |
| 4              | 2          | Combat EXP +5%      |
| 7              | 3          | Gathering EXP +5%   |
| 9              | 4          | Luck +1             |
| 10             | 5          | Fishing Speed +1    |
| 11             | 6          | Gathering Speed +1  |
| 15             | 8          | Fishing EXP +5%     |
| 18             | 9          | Hunting EXP +5%     |
| 21             | 10         | Cooking EXP +5%     |
| 24             | 11         | Alchemy EXP +5%     |
| 27             | 12         | Processing EXP +5%  |
| 30             | 13         | Training EXP +5%    |
| 33             | 14         | Trading EXP +5%     |
| 36             | 15         | Farming EXP +5%     |

Skill types 7, 16, 17, 18, 19 and 20 (Death Penalty Resist, Life EXP, Weight Limit, Durability Resistance, Skill EXP, Knowledge Gain) have no weight in any record and are never rolled here.

---

## Roll Chances

Chance is `weight / total_weight` for that record. Values below are percentages.

| Skill                  | 1    | 2    | 3    | 4    | 101  | 102  | 103  | 104  | 201  | 202  | 203  | 204  | 301  | 302  | 303  | 304  | 401  | 402  | 403  | 404  |
| ---------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Karma Recovery +5%     | 12.4 | 12.4 | 15.8 | 15.8 | 14.5 | 14.1 | 18.0 | 18.0 | 16.9 | 16.9 | 21.3 | 21.3 | 16.9 | 16.9 | 21.3 | 21.3 | 1.4  | 1.4  | 1.4  | 1.4  |
| Combat EXP +5%         | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Gathering EXP +5%      | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Luck +1                | 3.1  | 3.1  | 3.0  | 3.0  | 3.6  | 3.5  | 3.4  | 3.4  | 4.2  | 4.2  | 4.0  | 4.0  | 4.2  | 4.2  | 4.0  | 4.0  | 7.1  | 7.1  | 7.1  | 7.1  |
| Fishing Speed +1       | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 3.5  | 3.4  | 3.4  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 7.1  | 7.1  | 7.1  | 7.1  |
| Gathering Speed +1     | 1.0  | 1.0  | 1.0  | 1.0  | 1.2  | 1.2  | 1.1  | 1.1  | 4.2  | 4.2  | 4.0  | 4.0  | 4.2  | 4.2  | 4.0  | 4.0  | 7.1  | 7.1  | 7.1  | 7.1  |
| Fishing EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 18.1 | 17.6 | 16.9 | 16.9 | 21.1 | 21.1 | 20.0 | 20.0 | 21.1 | 21.1 | 20.0 | 20.0 | 17.1 | 17.1 | 17.1 | 17.1 |
| Hunting EXP +5%        | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 17.1 | 17.1 | 17.1 | 17.1 |
| Cooking EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Alchemy EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Processing EXP +5%     | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Training EXP +5%       | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Trading EXP +5%        | 1.0  | 1.0  | 1.0  | 1.0  | 18.1 | 17.6 | 16.9 | 16.9 | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |
| Farming EXP +5%        | 15.5 | 15.5 | 14.9 | 14.9 | 1.2  | 1.2  | 1.1  | 1.1  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.3  | 1.3  | 1.4  | 1.4  | 1.4  | 1.4  |

### Record Totals

Unlike the fairy table, pet weights are **not** normalised to `1,000,000`:

| Total weight | Acquire types                          |
| ------------ | -------------------------------------- |
| `700,000`    | `401`, `402`, `403`, `404`             |
| `710,000`    | `201`, `202`, `301`, `302`             |
| `750,000`    | `203`, `204`, `303`, `304`             |
| `830,000`    | `101`                                  |
| `850,000`    | `102`                                  |
| `890,000`    | `103`, `104`                           |
| `970,000`    | `1`, `2`                               |
| `1,010,000`  | `3`, `4`                               |
| `0`          | `0` (placeholder)                      |

Because `3` and `4` exceed `1,000,000`, these cannot be parts-per-million probabilities the way the fairy weights are. Treat them as relative weights and normalise by the record total.

---

## `petequipskillaquireoffset.dbss`

### Header (4 bytes)

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Must equal `petequipskillaquire.dbss` count (`21`) |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | key         | `acquire_type_id`                                            |
| `+0x02` | u32  | data_offset | Absolute byte offset in the main file past the 2-byte prefix |
| `+0x06` | u16  | data_size   | Always `174` (`176 - 2-byte key prefix`)                     |
| `+0x08` | u16  | padding     | Always `0`                                                   |

---

## Suggested UI Layout

| Column          | Type | Notes                                               |
| --------------- | ---- | --------------------------------------------------- |
| Acquire Type ID | num  | `acquire_type_id` (right-aligned)                   |
| Skill ID        | num  | `equip_skill_id` the weight indexes                 |
| Skill Name      | text | Resolved via the catalog's `loc_id` (LOC type 10)   |
| Chance          | num  | `weight / total_weight` as a percentage             |
| Weight          | num  | Raw weight value                                    |

Show one row per `(acquire_type_id, equip_skill_id)` and omit zero weights, since a zero means the skill is not rollable.

---

## Notes

- Weights are **roll weights, not costs**. Earlier revisions of this document described the record as a cost table with `cost_a`/`cost_b`/`cost_c` triples and a `reserved` field; that reading was wrong. The record is a flat 43-element weight array and the "reserved" u32 is simply `weights[0]`.
- The layout is shared with [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), where the same structure is confirmed against published per-grade skill availability and every record sums to exactly `1,000,000`.
- Weights index Section 1 of `petequipskill.bss` (`equip_skill_id` `0`–`42`), which is exactly the 43 available slots. The extended Section 2 catalog is not addressable here.
- `301`–`304` are byte-identical to `201`–`204`, and `401`–`404` are identical to each other. Several other keys pair up (`1`=`2`, `3`=`4`, `103`=`104`).
- Only the `+5%` mid-tier of each skill group is rollable; the `+7%` and duplicate `+5%` entries never appear.

---

## Open Questions

### Weight normalisation

Fairy records sum to exactly `1,000,000`, but pet totals range from `700,000` to `1,010,000`. Whether the shortfall represents a chance of no skill being granted, whether the client simply normalises by the record total, or whether `3`/`4` exceeding a million is a data error, is unconfirmed.

### Acquire type grouping

The `group × 100 + tier` split fits the key values, and the pools are clearly themed by skill category, but which pet species or grade maps to which group has not been traced through `pet.dbss`. The exact duplication of `201`–`204` by `301`–`304` suggests one group is a reserved or legacy copy.

### Sub-entry semantic mapping

Resolved. The former "14 sub-entries with `cost_a`/`cost_b`/`cost_c`" structure does not exist; the apparent triples were an artifact of grouping a dense 43-element array into 12-byte rows, and the 14 "active" sub-entries were simply the 14 rollable skills. This entry is retained so the disproven reading is not re-derived.
