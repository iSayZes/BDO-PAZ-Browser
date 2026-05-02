# npcpersonality.dbss

Defines NPC personality entries used to parameterise AI behaviour. Each record
maps a personality ID to three NPC type references and four floating-point
behavioural parameters.

Companion file: `npcpersonalityoffset.dbss` — provides an ID-keyed index into
the main file (same count, same order).

## Structure

### Header (4 bytes)

| Offset | Type | Field | Notes                                          |
| ------ | ---- | ----- | ---------------------------------------------- |
| 0x00   | u32  | count | Number of personality records (observed: 1182) |

### Record (34 bytes, repeated `count` times)

| Offset | Type | Field              | Notes                                                                                                 |
| ------ | ---- | ------------------ | ----------------------------------------------------------------------------------------------------- |
| 0x00   | u16  | personality_id     | Unique personality identifier (e.g. 0xBA6F)                                                          |
| 0x02   | u32  | interest_group_a   | `(item_count << 16) \| group_id` — first amity interest group (see encoding below)                   |
| 0x06   | u32  | interest_group_b   | Second amity interest group                                                                           |
| 0x0A   | u32  | interest_group_c   | Third amity interest group                                                                            |
| 0x0E   | u16  | personality_id_dup | Always equal to `personality_id` at 0x00    |
| 0x10   | f32  | interest_min       | Inclusive lower bound for amity interest (range: 11–37)            |
| 0x14   | f32  | interest_max_excl  | Exclusive upper bound; usable max = value − 1 (range: 23–70)       |
| 0x18   | f32  | favor_min          | Inclusive lower bound for amity favor (range: 10–35)               |
| 0x1C   | f32  | favor_max_excl     | Exclusive upper bound; usable max = value − 1 (range: 14–68)       |
| 0x20   | u16  | personality_type   | Personality category code (see below)       |

#### interest_group encoding

Each `interest_group` field is a u32 packed field:

```
bits 31-16 : item_count  (number of knowledge entries from this group the NPC is interested in)
bits 15-0  : group_id    (knowledge group ID — matches `id` in knowledge.json)
```

`item_count` matches the denominator shown in the in-game amity UI (e.g. Amerigo
shows "Vendors of Serendia (0/4)" and his `item_count` is 4 for all three
groups). Observed values: 0, 1, 2, 4, 5, 6, 7, 8, 10. All three fields in a
record typically share the same item_count (1121 of 1182 records).

#### personality_type codes

24 distinct values in the range 101–1202 following the pattern
`(major × 100) + variant` where variant is 1 or 2:

| Major | Variant 1 | Variant 2 | Horoscope              |
| ----- | --------- | --------- | ---------------------- |
| 1     | 101       | —         | Hammer                 |
| 2     | 201       | 202       | Boat                   |
| 3     | 301       | 302       | Shield                 |
| 4     | 401       | 402       | Giant                  |
| 5     | 501       | 502       | Camel                  |
| 6     | 601       | 602       | Black Dragon           |
| 7     | 701       | 702       | Treant Owl             |
| 8     | 801       | 802       | Elephant               |
| 9     | 901       | —         | Key                    |
| 10    | 1001      | 1002      | Wagon                  |
| 11    | 1101      | 1102      | Sealing Stone          |
| 12    | 1201      | 1202      | Goblin                 |

All 12 BDO horoscopes are fully mapped. Confirmed by cross-referencing
`amity-npcs.json` horoscope fields against `personality_id` values in this file.
All 12 mappings are directly confirmed. Major 9 has only variant 1 (901)
observed; no 902 exists in the data.

---

## npcpersonalityoffset.dbss

An index file with one entry per personality record, stored in the same order
as the main file.

### Header (4 bytes)

| Offset | Type | Field | Notes                                  |
| ------ | ---- | ----- | -------------------------------------- |
| 0x00   | u32  | count | Must equal `npcpersonality.dbss` count |

### Offset Record (10 bytes, repeated `count` times)

| Offset | Type | Field          | Notes                                                                                                          |
| ------ | ---- | -------------- | -------------------------------------------------------------------------------------------------------------- |
| 0x00   | u16  | personality_id | Matches `personality_id` in the main record                                                                    |
| 0x02   | u32  | data_offset    | Byte offset into main file; points 2 bytes past the record start (i.e. skips the leading `personality_id` u16) |
| 0x06   | u16  | data_size      | Always 32 (= record size minus the 2-byte personality_id header)                                               |
| 0x08   | u16  | padding        | Always 0                                                                                                       |

To locate a record in the main file given an offset record:
`record_start = data_offset - 2`

---

## Notes

- Little-endian throughout.
- All 1182 `personality_id` values are unique — it is a true record key.
- `personality_id_dup` at record offset 0x0E is always identical to
  `personality_id` at 0x00; its purpose appears to be alignment padding or a
  redundant lookup key.
- The `variant` in `personality_type` (1 or 2) is not exposed in
  `amity-npcs.json`; its in-game meaning is unknown. Distribution is roughly
  even (584 variant-1, 598 variant-2 in the observed data). Majors 1 and 9 have
  only variant 1.
- The high 16 bits of each `interest_group` field (`item_count`) encode how many
  knowledge entries from that group the NPC is interested in. Confirmed against
  Amerigo: all three groups show `item_count=4`, matching the in-game amity UI
  display "Vendors of Serendia (0/4)", "Serendia Adventure Log II (0/4)",
  "Plants (Serendia) (0/4)".
- `item_count=0` is valid — NPC 47663 has two groups with `item_count=0` and
  they still appear in the amity UI. The in-game behaviour for `item_count=0`
  groups is not yet fully understood (TODO: verify what the UI shows for the
  denominator in this case).
- The four float parameters encode amity interest/favor thresholds (confirmed
  against Amerigo, NPC ID 41013, knowledge ID 113):
  - `interest_min` — inclusive lower bound, exact match
  - `interest_max_excl` — exclusive upper bound; usable max = value − 1
  - `favor_min` — inclusive lower bound, exact match
  - `favor_max_excl` — exclusive upper bound; usable max = value − 1
- `interest_group_a/b/c` encode the NPC's amity interest groups (low 16 bits =
  knowledge group ID from knowledge.json). Confirmed for Amerigo:
  - `interest_group_a` group_id=113   → Vendors of Serendia
  - `interest_group_b` group_id=20201 → Serendia Adventure Log II
  - `interest_group_c` group_id=10212 → Plants (Serendia)
- The offset file's `data_offset` values increment by exactly 34 (the main
  record stride) for each successive entry, so the offset file provides no
  reordering — it is a 1-to-1 sequential index.
