# `npcpersonality.dbss` Format

## Purpose

Defines NPC personality entries used to parameterise AI behaviour. Each record maps a personality ID to three knowledge group references (each with an unknown u16 beside it) and four floating-point amity threshold parameters. Used to drive the in-game amity mini-game.

Example:

```text
personality_id: 0x2875  →  personality_type: 101 (Hammer)
interest_groups: Vendors of Serendia, Serendia Log II, Plants
interest: 11–37, favor: 10–35
```

## Companion Files

| File                        | Required | Role                                    |
| --------------------------- | -------- | --------------------------------------- |
| `npcpersonalityoffset.dbss` | Required | ID-keyed index (same count, own order)  |

All multi-byte values are little-endian.

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                          |
| ------- | ---- | ----- | ---------------------------------------------- |
| `+0x00` | u32  | count | Number of personality records (observed: 1,182 in the pre-2026-09-27 fixture and in the 2026-09-27 client) |

### Record (34 bytes, repeated `count` times)

| Offset  | Type | Field              | Notes                                                         |
| ------- | ---- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16  | personality_id     | Unique personality identifier                                 |
| `+0x02` | u16  | group_a_id         | First amity interest group (knowledge group ID)               |
| `+0x04` | u16  | unknown_04         | Per-group number for group A; see below                       |
| `+0x06` | u16  | group_b_id         | Second amity interest group                                   |
| `+0x08` | u16  | unknown_08         | Per-group number for group B                                  |
| `+0x0A` | u16  | group_c_id         | Third amity interest group                                    |
| `+0x0C` | u16  | unknown_0c         | Per-group number for group C                                  |
| `+0x0E` | u16  | personality_id_dup | Always equal to `personality_id` at `+0x00`; purpose unknown  |
| `+0x10` | f32  | interest_min       | Inclusive lower bound for amity interest (range: 11–37)       |
| `+0x14` | f32  | interest_max       | Upper bound for amity interest (range: 23–70); inclusive or exclusive is open |
| `+0x18` | f32  | favor_min          | Inclusive lower bound for amity favor (range: 10–35)          |
| `+0x1C` | f32  | favor_max          | Upper bound for amity favor (range: 14–68; 15–70 in the 2026-09-27 client); inclusive or exclusive is open |
| `+0x20` | u16  | personality_type   | Personality category code (see enum below)                    |

#### Interest Groups

Each group is a u16 knowledge group ID (matches `node_id` in `mentalcard.dbss`) followed by an unknown u16 (`unknown_04`, `unknown_08`, `unknown_0c`). Earlier versions of this doc read each pair as one packed u32 and called the high half `item_count`.

The same numbers appear on the BDO wiki next to each NPC's interest groups, but the game does not show them: the conversation window lists only the topics you can use, with no per-group count or maximum (I checked in game, 2026-09-27). It is not the number of topics offered either: with Oliviero (`6` for Serendia Adventure Log II) the topic list showed 7 cards of that group. What the number controls is open. Observed values: 0, 1, 2, 4, 5, 6, 7, 8, 10. All three fields in a record typically share the same value (1121 of 1182 records).

## Enum Values

### personality_type Codes

24 distinct values in the range 101–1202, following the pattern `(major × 100) + variant` where variant is 1 or 2:

| Major | Variant 1 | Variant 2 | Horoscope     |
| ----- | --------- | --------- | ------------- |
| 1     | 101       | -         | Hammer        |
| 2     | 201       | 202       | Boat          |
| 3     | 301       | 302       | Shield        |
| 4     | 401       | 402       | Giant         |
| 5     | 501       | 502       | Camel         |
| 6     | 601       | 602       | Black Dragon  |
| 7     | 701       | 702       | Treant Owl    |
| 8     | 801       | 802       | Elephant      |
| 9     | 901       | -         | Key           |
| 10    | 1001      | 1002      | Wagon         |
| 11    | 1101      | 1102      | Sealing Stone |
| 12    | 1201      | 1202      | Goblin        |

Confirmed by cross-referencing `amity-npcs.json` horoscope fields against `personality_id` values. Majors 1 and 9 have only variant 1.

## npcpersonalityoffset.dbss

An index file with one entry per personality record.

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
| `+0x08` | u16  | -              | Not parsed; assumed padding                                                    |

`record_start = data_offset - 2`

Every offset row points at a record that repeats its `personality_id`, and every record is indexed exactly once, but the rows are not in main-file order: only the first 53 step by the 34-byte stride, the rest are ordered differently (pre-2026-09-27 fixture and 2026-09-27 client alike). An earlier version of this doc called it a sequential index in main-file order.

## Suggested UI Layout

| Column            | Type | Notes                                            |
| ----------------- | ---- | ------------------------------------------------ |
| ID                | num  | `personality_id`                                 |
| Row               | num  | Record index within the file                     |
| Group A           | num  | `group_a_id`                                     |
| Group B           | num  | `group_b_id`                                     |
| Group C           | num  | `group_c_id`                                     |
| Int Min           | num  | Interest range lower bound                       |
| Int Max           | num  | Interest range upper bound                       |
| Fav Min           | num  | Favor range lower bound                          |
| Fav Max           | num  | Favor range upper bound                          |
| Horoscope         | text | Zodiac sign resolved from the personality type   |

## Notes

- All 1182 `personality_id` values are unique; it is a true record key.
- `personality_id_dup` at `+0x0E` is always identical to `personality_id` at `+0x00`; appears to be alignment padding or a redundant lookup key.
- The `variant` in `personality_type` (1 or 2) is not exposed in `amity-npcs.json`; its in-game meaning is unknown. Distribution is roughly even (584 variant-1, 598 variant-2).
- The groups and `unknown_*` numbers match the BDO wiki for Amerigo (41013): Vendors of Serendia, Serendia Adventure Log II and Plants (Serendia), `4` each.
- The NPC rolls its Interest Level and Favor at the start of each conversation, and keeps them when the conversation is continued ([Black Desert Foundry, Story Exchange guide](https://www.blackdesertfoundry.com/story-exchange-guide/)). Readings do not always fall inside the stored ranges, though: see the table below.
- They match the wiki for Oliviero (41091) too: Serendia Adventure Log II, Officers of Serendia and Plants (Serendia), `6` each. Each group holds more cards than its `unknown_*` number (18, 13 and 11 here). Sharing a group does not mean sharing topics: Amerigo, who also has Serendia Adventure Log II, did not offer the Log II cards Oliviero did. Which cards an NPC offers is open.
- The stored ranges change between client versions while the group IDs stay, and the ranges seen outside the file fit neither client consistently. Interest / favor, stored minimum to maximum:

  | NPC | Seen | Source of the seen range | Pre-2026-09-27 fixture | Client 3458 (2026-09-27) |
  | --- | --- | --- | --- | --- |
  | Lorenzo Murray (40015) | 32 / 15 | Foundry guide | 31-35 / 16-20 | 30-35 / 17-18 |
  | Ornella (41002) | 22-23 / 27-28 | In game | 22-23 / 25-28 | 22-23 / 26-29 |
  | Amerigo (41013) | 20-24 / 27-29 | Amity tracker dataset | 20-25 / 27-30 | 22-24 / 26-30 |
  | Amerigo (41013) | 22 / 28 | Topic tooltips, 2026-09-27 | 20-25 / 27-30 | 22-24 / 26-30 |
  | Cleia (41056) | 20-23 / 25-29 | Amity tracker dataset | 22-23 / 26-28 | 22-25 / 25-28 |
  | Cleia (41056) | 21 / 26 | Topic tooltips, 2026-09-27 | 22-23 / 26-28 | 22-25 / 25-28 |
  | Oliviero (41091) | 30 / 31 | Topic tooltips, 2026-09-27 | 32-35 / 32-33 | 31-33 / 32-33 |
  | George Fusto (41118) | 22-25 / 26-30 | Amity tracker dataset | 20-23 / 25-29 | 20-24 / 27-29 |

  Ornella and the 2026-09-27 Amerigo reading fit, but Oliviero's and Cleia's current readings sit one or two below the current minimums, and Lorenzo's favor 15 is below both files. The tracker dataset comes from a wiki and may predate both files. An earlier version of this table listed a "Stored" column that matched neither fixture; it was replaced with values read from both files (2026-09-28).

## Open Questions

### What do `unknown_04`, `unknown_08` and `unknown_0c` control?

The per-group number matches the numbers the BDO wiki lists next to each interest group, but the game shows no per-group count, and Oliviero's topic list held 7 cards of a group whose number is `6`. It may cap how many of the group's topics the NPC accepts, weight which topics are offered, or be unused. `0` occurs as well.

### Are the upper bounds inclusive?

An earlier version of this doc called `interest_max` and `favor_max` exclusive (usable maximum one less than stored) without recorded evidence. Ornella's in-game favor reached `28`, her stored maximum in the pre-2026-09-27 fixture (`29` in client 3458), which argues against that, but other readings fall below the stored minimums (see Notes), so the stored range may not bound what the game rolls. How the displayed range is derived from the stored one is open; the check for Ornella's current maximum is under In-Game Checks.

## In-Game Checks

### Ornella's Favor Maximum

Needs NPC: [Ornella](https://bdocodex.com/us/npc/41002/)

Ornella's stored favor range is `26` to `29` in client 3458. The NPC rolls Favor at the start of each conversation (see Notes), so start about 20 new conversations with her and write down each Favor. A `29` means `favor_max` is inclusive; `26` to `28` only, with `28` seen, means the usable maximum is one less than stored. Readings below `26` mean the stored range does not bound the roll, as for Oliviero and Cleia.
