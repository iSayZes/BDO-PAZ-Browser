# `fairyequipskillaquire.dbss` Format

## Purpose

Defines the **skill roll table** used when a fairy's skills are changed. Each record is one fairy grade and holds a weight for every skill in [fairyequipskill.bss](fairyequipskill_bss.md), expressed in parts-per-million. A weight of `0` means that grade cannot roll that skill.

This is the data behind the "% chance to obtain the new skill" the game shows on the Change Skill window.

Example:

```text
Radiant (504) → Miraculous Cheer V: weight 100000 = 10.0%
Faint   (501) → Morning Star:       weight 250000 = 25.0%
Faint   (501) → Tingling Breath II: weight 0      = cannot roll
```

## Graph

### Tags

- file format
- dbss
- fairy
- equip skill
- drop rate

### Connections

- [fairyequipskill.bss](fairyequipskill_bss.md) — the skill catalog; weights are indexed by its `equip_skill_id`
- [fairyequipskillaquireoffset.dbss](#fairyequipskillaquireoffsetdbss) — keyed offset index
- [petequipskillaquire.dbss](petequipskillaquire_dbss.md) — identical record layout for pets
- [fairyskillchange.dbss](fairyskillchange_dbss.md) — the Theiah's Orb cost of performing the reroll

---

## Companion Files

| File                               | Required | Role                                                  |
| ---------------------------------- | -------- | ----------------------------------------------------- |
| `fairyequipskillaquireoffset.dbss` | Required | `acquire_type_id → (data_offset, data_size)` index    |
| `fairyequipskill.bss`              | Optional | Resolves a weight's `equip_skill_id` to a skill name  |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                           |
| ------- | ---- | ----- | ------------------------------- |
| `+0x00` | u32  | count | Number of records; observed `4` |

### Record (176 bytes, repeated `count` times)

| Offset  | Type    | Field      | Notes                                                 |
| ------- | ------- | ---------- | ----------------------------------------------------- |
| `+0x00` | u32     | packed_key | `(acquire_type_id << 16) \| acquire_type_id`          |
| `+0x04` | u32[43] | weights    | Roll weight per `equip_skill_id`, in parts-per-million |

`4 + 43 × 4 = 176` bytes exactly. `weights[i]` is the chance of rolling the skill whose `equip_skill_id` is `i`; index `0` is the first weight, **not** a reserved field.

The first 2 bytes of each record are the file key prefix. The offset companion points to `record_start + 2`, so use `record_start = data_offset - 2` to read the full u32-aligned record.

---

## Acquire Type IDs — Fairy Grades

The four keys are the four fairy grades, ascending:

| acquire_type_id | Fairy grade | Rollable skills | Max skill rank |
| --------------- | ----------- | --------------- | -------------- |
| `501`           | Faint       | 6               | I              |
| `502`           | Glimmering  | 13              | III            |
| `503`           | Brilliant   | 18              | IV             |
| `504`           | Radiant     | 30              | V              |

Every record's weights sum to exactly `1,000,000`, so each column below is a complete probability distribution.

---

## Roll Chances

`—` means the grade cannot roll that skill.

| equip_skill_id | Skill                  | Faint  | Glimmering | Brilliant | Radiant |
| -------------- | ---------------------- | ------ | ---------- | --------- | ------- |
| 0              | Tingling Breath I      | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 1              | Tingling Breath II     | —      | 7.0%       | 5.0%      | 2.0%    |
| 2              | Tingling Breath III    | —      | —          | 5.0%      | 3.0%    |
| 3              | Tingling Breath IV     | —      | —          | —         | 3.0%    |
| 4              | Tingling Breath V      | —      | —          | —         | 3.0%    |
| 5              | Feathery Steps I       | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 6              | Feathery Steps II      | —      | 7.0%       | 5.0%      | 2.0%    |
| 7              | Feathery Steps III     | —      | —          | 5.0%      | 3.0%    |
| 8              | Feathery Steps IV      | —      | —          | —         | 4.0%    |
| 9              | Feathery Steps V       | —      | —          | —         | 5.0%    |
| 10             | Fairy's Tear I         | 15.0%  | 7.0%       | 5.0%      | 2.0%    |
| 11             | Fairy's Tear II        | —      | 7.0%       | 5.0%      | 3.0%    |
| 12             | Fairy's Tear III       | —      | —          | 5.0%      | 4.0%    |
| 13             | Fairy's Tear IV        | —      | —          | —         | 5.0%    |
| 14             | Inexhaustible Well I   | 15.0%  | 7.0%       | 5.0%      | 1.0%    |
| 15             | Inexhaustible Well II  | —      | 7.0%       | 5.0%      | 2.0%    |
| 16             | Inexhaustible Well III | —      | 7.0%       | 5.0%      | 3.0%    |
| 17             | Inexhaustible Well IV  | —      | —          | 5.0%      | 3.0%    |
| 18             | Inexhaustible Well V   | —      | —          | —         | 4.0%    |
| 19             | Morning Star           | 25.0%  | 15.0%      | 10.0%     | 3.0%    |
| 24             | Miraculous Cheer I     | 15.0%  | 8.0%       | 5.0%      | 3.0%    |
| 25             | Miraculous Cheer II    | —      | 7.0%       | 5.0%      | 4.0%    |
| 26             | Miraculous Cheer III   | —      | 7.0%       | 5.0%      | 5.0%    |
| 27             | Miraculous Cheer IV    | —      | —          | 10.0%     | 6.0%    |
| 28             | Miraculous Cheer V     | —      | —          | —         | 10.0%   |
| 30             | Continuous Care I      | —      | —          | —         | 1.0%    |
| 31             | Continuous Care II     | —      | —          | —         | 2.0%    |
| 32             | Continuous Care III    | —      | —          | —         | 3.0%    |
| 33             | Continuous Care IV     | —      | —          | —         | 4.0%    |
| 34             | Continuous Care V      | —      | —          | —         | 5.0%    |
| **Total**      |                        | 100.0% | 100.0%     | 100.0%    | 100.0%  |

### Never-rolled skills

Five catalog entries carry a weight of `0` in every grade and are therefore unreachable through a skill change:

| equip_skill_id | Skill                       | Why                                     |
| -------------- | --------------------------- | --------------------------------------- |
| 20             | Miraculous Cheer 10 Seconds | Legacy naming, superseded by `I`–`V`    |
| 21             | Miraculous Cheer 9 Seconds  | Legacy naming                           |
| 22             | Miraculous Cheer 8 Seconds  | Legacy naming                           |
| 23             | Miraculous Cheer 7 Seconds  | Legacy naming                           |
| 29             | Gift                        | Every fairy starts with it; never rolled |

---

## `fairyequipskillaquireoffset.dbss`

### Header (4 bytes)

| Offset  | Type | Field | Notes                                               |
| ------- | ---- | ----- | --------------------------------------------------- |
| `+0x00` | u32  | count | Must equal `fairyequipskillaquire.dbss` count (`4`) |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | key         | `acquire_type_id`; observed `504`, `503`, `502`, `501`       |
| `+0x02` | u32  | data_offset | Absolute byte offset in the main file past the 2-byte prefix |
| `+0x06` | u16  | data_size   | Always `174` (`176 - 2-byte key prefix`)                     |
| `+0x08` | u16  | padding     | Always `0`                                                   |

Rows are ordered descending by key and ascending by `data_offset`.

---

## Lookup Recipe

```python
def roll_chance(record, equip_skill_id):
    weight = record["weights"][equip_skill_id]
    return weight / record["total_weight"]  # total is 1,000,000 for fairies
```

---

## Suggested UI Layout

| Column      | Type | Notes                                                |
| ----------- | ---- | ---------------------------------------------------- |
| Fairy Grade | text | Grade name from `acquire_type_id`; falls back to ID  |
| Skill ID    | num  | `equip_skill_id` the weight indexes (right-aligned)  |
| Skill Name  | text | Resolved via the catalog's `loc_id` (LOC type 10)    |
| Chance      | num  | `weight / total_weight` as a percentage              |
| Weight      | num  | Raw parts-per-million value                          |

Show one row per `(acquire_type_id, equip_skill_id)` and omit zero weights, since a zero means the skill is not rollable at all.

---

## Notes

- Weights are **probabilities, not costs**. Earlier revisions of this document described the record as an acquisition cost table with `cost_a`/`cost_b`/`cost_c` triples and a `reserved` field; that reading was wrong. The values are parts-per-million and the "reserved" u32 is simply `weights[0]`.
- The record is a flat 43-element array, not 14 sub-entries of 3 values. The apparent triples were an artifact of grouping a dense array into 12-byte rows.
- Three independent checks confirm the reading: every grade sums to exactly `1,000,000`; the non-zero index set per grade matches the published per-tier skill availability exactly; and the highest rank reachable per grade (I / III / IV / V) matches the published rank caps.
- 43 weight slots cover `equip_skill_id` `0`–`42`, while the fairy catalog only defines `0`–`34`. Slots `35`–`42` are zero in every record — spare capacity shared with the pet table, which uses the same 176-byte record.
- Only Radiant can roll rank IV and V skills, which the weight table encodes directly rather than through a separate cap field.
- Morning Star is weighted far above any other skill at low grades (25% for Faint) and drops to 3% at Radiant.

---

## Open Questions

### Sub-entry semantic mapping

Resolved. The former "14 sub-entries with `cost_a`/`cost_b`/`cost_c`" structure does not exist; the record is a flat weight array indexed by `equip_skill_id`. This entry is retained so the disproven reading is not re-derived.

### Spare weight slots

Slots `35`–`42` are always zero for fairies. Whether they are reserved for future fairy skills or exist only because the record size is shared with `petequipskillaquire.dbss` is unconfirmed.
