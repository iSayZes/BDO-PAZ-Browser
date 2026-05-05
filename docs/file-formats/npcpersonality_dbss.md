# `npcpersonality.dbss` Format

## Purpose

Defines NPC personality entries used to parameterise AI behaviour. Each record maps a personality ID to three knowledge group references and four floating-point amity threshold parameters. Used to drive the in-game amity mini-game.

Example:

```text
personality_id: 0x2875  →  personality_type: 101 (Hammer)
interest_groups: Vendors of Serendia (4), Serendia Log II (4), Plants (4)
interest: 11–37, favor: 10–35
```

## Graph

### Tags

- file format
- dbss
- npc
- amity

### Connections

- [zodiacsign.dbss](zodiacsign_dbss.md) — personality_type maps to zodiac_id via `major = personality_type // 100`
- [languagedata_en.loc](languagedata_loc.md) — knowledge group names (str_type=9)

---

## Companion Files

| File                        | Required | Role                                    |
| --------------------------- | -------- | --------------------------------------- |
| `npcpersonalityoffset.dbss` | Required | ID-keyed index (same count, same order) |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                          |
| ------- | ---- | ----- | ---------------------------------------------- |
| `+0x00` | u32  | count | Number of personality records (observed: 1182) |

### Record (34 bytes, repeated `count` times)

| Offset  | Type | Field              | Notes                                                         |
| ------- | ---- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16  | personality_id     | Unique personality identifier                                 |
| `+0x02` | u32  | interest_group_a   | `(item_count << 16) \| group_id` — first amity interest group |
| `+0x06` | u32  | interest_group_b   | Second amity interest group                                   |
| `+0x0A` | u32  | interest_group_c   | Third amity interest group                                    |
| `+0x0E` | u16  | personality_id_dup | Always equal to `personality_id` at `+0x00`; purpose unknown  |
| `+0x10` | f32  | interest_min       | Inclusive lower bound for amity interest (range: 11–37)       |
| `+0x14` | f32  | interest_max_excl  | Exclusive upper bound; usable max = value − 1 (range: 23–70)  |
| `+0x18` | f32  | favor_min          | Inclusive lower bound for amity favor (range: 10–35)          |
| `+0x1C` | f32  | favor_max_excl     | Exclusive upper bound; usable max = value − 1 (range: 14–68)  |
| `+0x20` | u16  | personality_type   | Personality category code (see enum below)                    |

#### interest_group Encoding

Each `interest_group` field is a packed u32:

```text
bits 31–16 : item_count  (knowledge entries from this group the NPC is interested in)
bits 15–0  : group_id    (knowledge group ID — matches node_id in mentalcard.dbss)
```

`item_count` matches the denominator shown in the in-game amity UI (e.g. "Vendors of Serendia (0/4)"). Observed values: 0, 1, 2, 4, 5, 6, 7, 8, 10. All three fields in a record typically share the same `item_count` (1121 of 1182 records). `item_count=0` is valid and still appears in the amity UI.

---

## Enum Values

### personality_type Codes

24 distinct values in the range 101–1202, following the pattern `(major × 100) + variant` where variant is 1 or 2:

| Major | Variant 1 | Variant 2 | Horoscope     |
| ----- | --------- | --------- | ------------- |
| 1     | 101       | —         | Hammer        |
| 2     | 201       | 202       | Boat          |
| 3     | 301       | 302       | Shield        |
| 4     | 401       | 402       | Giant         |
| 5     | 501       | 502       | Camel         |
| 6     | 601       | 602       | Black Dragon  |
| 7     | 701       | 702       | Treant Owl    |
| 8     | 801       | 802       | Elephant      |
| 9     | 901       | —         | Key           |
| 10    | 1001      | 1002      | Wagon         |
| 11    | 1101      | 1102      | Sealing Stone |
| 12    | 1201      | 1202      | Goblin        |

Confirmed by cross-referencing `amity-npcs.json` horoscope fields against `personality_id` values. Majors 1 and 9 have only variant 1.

---

## npcpersonalityoffset.dbss

An index file with one entry per personality record, stored in the same order as the main file.

### Header (4 bytes)

| Offset  | Type | Field | Notes                                  |
| ------- | ---- | ----- | -------------------------------------- |
| `+0x00` | u32  | count | Must equal `npcpersonality.dbss` count |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field          | Notes                                                                          |
| ------- | ---- | -------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | personality_id | Matches `personality_id` in the main record                                    |
| `+0x02` | u32  | data_offset    | Byte offset into main file; 2 bytes past record start (skips `personality_id`) |
| `+0x06` | u16  | data_size      | Always 32 (= record size minus the 2-byte personality_id header)               |
| `+0x08` | u16  | —              | Not parsed; assumed padding                                                    |

`record_start = data_offset - 2`

The offset file's `data_offset` values increment by exactly 34 (the main record stride) for each successive entry — it is a 1-to-1 sequential index providing no reordering.

---

## Suggested UI Layout

| Column           | Type | Notes                                    |
| ---------------- | ---- | ---------------------------------------- |
| Personality ID   | num  | `personality_id` (also show as hex)      |
| Personality Type | num  | `personality_type`                       |
| Horoscope        | text | Decoded from `personality_type` via enum |
| Group A ID       | num  | `interest_group_a & 0xFFFF`              |
| Group A Count    | num  | `interest_group_a >> 16`                 |
| Group B ID       | num  | `interest_group_b & 0xFFFF`              |
| Group B Count    | num  | `interest_group_b >> 16`                 |
| Group C ID       | num  | `interest_group_c & 0xFFFF`              |
| Group C Count    | num  | `interest_group_c >> 16`                 |
| Interest Range   | text | `interest_min` – `interest_max_excl − 1` |
| Favor Range      | text | `favor_min` – `favor_max_excl − 1`       |

---

## Notes

- All 1182 `personality_id` values are unique — it is a true record key.
- `personality_id_dup` at `+0x0E` is always identical to `personality_id` at `+0x00`; appears to be alignment padding or a redundant lookup key.
- The `variant` in `personality_type` (1 or 2) is not exposed in `amity-npcs.json`; its in-game meaning is unknown. Distribution is roughly even (584 variant-1, 598 variant-2).
- Confirmed against Amerigo (NPC ID 41013): all three groups show `item_count=4`, matching the UI display "Vendors of Serendia (0/4)", "Serendia Adventure Log II (0/4)", "Plants (Serendia) (0/4)".
- The in-game behaviour for `item_count=0` groups is not yet fully understood.
