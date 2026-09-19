# `fairyskillchange.dbss` Format

## Purpose

Defines the cost of **rerolling a fairy's skills**. Each fairy level (`1`–`50`) maps to the number of Theiah's Orbs consumed by a skill change at that level, rising from `1` to `5` in fixed level bands.

This is the data behind the well-known rerolling advice: keep a fairy at a low level while rerolling, because the orb cost scales with its level.

`fairyskillchangeoffset.dbss` provides a level-keyed index into the main file, which is needed because the records are **not** stored in level order.

Example:

```text
level 10  → 1 Theiah's Orb
level 25  → 2 Theiah's Orbs
level 50  → 5 Theiah's Orbs
```

## Graph

### Tags

- file format
- dbss
- fairy
- skill change

### Connections

- [fairyskillchangeoffset.dbss](#fairyskillchangeoffsetdbss), level-keyed offset index
- [fairyequipskill.bss](fairyequipskill_bss.md), the fairy skill catalog whose entries a reroll draws from; no shared key
- [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md), fairy equip-skill acquisition costs

---

## Companion Files

| File                          | Required | Role                                     |
| ----------------------------- | -------- | ---------------------------------------- |
| `fairyskillchangeoffset.dbss` | Optional | `level → (data_offset, data_size)` index |

The main file has a fixed record stride and a count in its header, so it can be scanned linearly without the offset companion. The index only matters for direct seeks by level.

All multi-byte values are little-endian.

---

## File Layout

Total file size: 604 bytes = 4 (count) + 50 × 12 (records).

### Header (4 bytes)

| Offset  | Type | Field | Notes                            |
| ------- | ---- | ----- | -------------------------------- |
| `+0x00` | u32  | count | Number of records; observed `50` |

### Record (12 bytes, repeated `count` times, offset `0x04`)

| Offset  | Type | Field    | Notes                                              |
| ------- | ---- | -------- | -------------------------------------------------- |
| `+0x00` | u32  | key      | Record key, the fairy level; equals `level`       |
| `+0x04` | u32  | level    | Fairy level, `1`–`50`                              |
| `+0x08` | u32  | orb_cost | Theiah's Orbs required to reroll skills, `1`–`5`   |

The leading `key` is the file key prefix and is identical to `level` in all 50 observed records. The offset companion points at `record_start + 4`, so the addressable payload is the trailing 8 bytes (`level`, `orb_cost`).

---

## Level → Orb Cost

All 50 levels are present exactly once.

| Theiah's Orbs | Levels | Count |
| ------------- | ------ | ----- |
| 1             | 1–19   | 19    |
| 2             | 20–29  | 10    |
| 3             | 30–39  | 10    |
| 4             | 40–49  | 10    |
| 5             | 50     | 1     |

The in-game cost table is usually quoted as starting at level 10 (`10`–`19` → 1 orb). The file covers levels `1`–`9` with the same cost of `1`; those rows are simply not reachable in practice, since a fairy is not rerolled below level 10.

---

## Record Order

Records are stored out of level order. The first stored keys are `47, 46, 45, 44, 43, 42, 41, 40`, and the file continues in descending runs that jump between bands. This is why the offset companion exists, a reader seeking a specific level must use the index rather than computing `4 + (level - 1) * 12`.

---

## `fairyskillchangeoffset.dbss`

Total file size: 604 bytes = 4 (count) + 50 × 12 (rows).

### Header (4 bytes)

| Offset  | Type | Field | Notes                                           |
| ------- | ---- | ----- | ----------------------------------------------- |
| `+0x00` | u32  | count | Must equal `fairyskillchange.dbss` count (`50`) |

### Offset Row (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                 |
| ------- | ---- | ----------- | ----------------------------------------------------- |
| `+0x00` | u32  | level       | Fairy level key, `1`–`50`                             |
| `+0x04` | u32  | data_offset | Absolute offset in the main file, past the 4-byte key |
| `+0x08` | u32  | data_size   | Always `8` (`12 - 4-byte key prefix`)                 |

Rows appear in the same order as the main file's records, so `data_offset` runs `8, 20, 32, …` while the keys do not ascend. Recover the full record with `record_start = data_offset - 4`.

---

## Lookup Recipe

```python
def orb_cost_for_level(main: bytes, level: int) -> int | None:
    count = u32(main, 0)
    for index in range(count):
        pos = 4 + index * 12
        if u32(main, pos + 4) == level:
            return u32(main, pos + 8)
    return None
```

---

## Suggested UI Layout

| Column        | Type | Notes                                   |
| ------------- | ---- | --------------------------------------- |
| Level         | num  | `level` (right-aligned)                 |
| Theiah's Orbs | num  | `orb_cost` for a reroll at that level   |

For `fairyskillchangeoffset.dbss`:

| Column       | Type | Notes                       |
| ------------ | ---- | --------------------------- |
| Level        | num  | `level` key (right-aligned) |
| Data Offset  | num  | `data_offset` as hex        |
| Data Size    | num  | `data_size`; always `8`     |
| Record Start | num  | `data_offset - 4` as hex    |

---

## Fairy Background

Context for reading this file and [fairyequipskill.bss](fairyequipskill_bss.md) together. These
mechanics are established in-game behaviour, not values decoded from this file:

Fairies come in four grades, Faint (tier 1, 10 levels, 2 skills), Glimmering (tier 2, 20 levels,
3 skills), Brilliant (tier 3, 30 levels, 4 skills) and Radiant (tier 4, 50 levels, 6 skills). Every
fairy starts with Gift (Luck +1) and learns one random additional skill every 10 levels.

Each learned skill rolls a random level of `1`–`5`, which is what the `I`–`V` ladders in the skill
catalog represent. Higher-grade fairies have better odds of higher skill levels, and only Radiant
fairies can roll level 4 or above.

---

## Notes

- Both files are exactly 604 bytes and carry the same record count, stride, and ordering.
- `key` and `level` are identical in every record, so the two cannot be told apart from this data alone; the split is inferred from where the offset companion points.
- No localization is involved, the format contains no strings and no LOC IDs.
- The cost bands are uneven: 1 orb covers 19 levels while 2–4 orbs cover 10 each and 5 orbs applies only at level 50.
- `orb_cost` is **not** a fairy grade. Fairy grades run `1`–`4` (Faint through Radiant); this field runs `1`–`5` and is keyed by level, not grade.
- The `1`–`5` range coincidentally matches the `I`–`V` skill-level ladders in the catalog. The two are unrelated: this field is a reroll price, and the catalog ladder is the rolled skill's level.

---

## Open Questions

### Relationship to the skill catalog

The two files are **not keyed to each other**. If this file were indexed by `equip_skill_id` it would have to include key `0` and stop at `34`; instead it starts at `1`, runs to `50`, and 16 of its keys (`35`–`50`) match no skill in the catalog, while the catalog's `equip_skill_id 0` has no key here. A reroll clearly draws from the catalog, but the file that constrains *which* entries and at what skill level, the per-grade roll table implied by "only Radiant fairies can roll level 4+", has not been located.

### Record ordering

The data section is stored out of level order in descending runs that jump between cost bands. Whether that order carries meaning (patch history, an authoring-tool artifact, or an intentional grouping) or is simply arbitrary is unknown.
