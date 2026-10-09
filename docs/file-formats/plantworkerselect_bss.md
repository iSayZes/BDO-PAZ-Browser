# `plantworkerselect.bss` Format

## Purpose

Worker selection table keyed by town/node LOC IDs. Each group lists workers that can appear for one town/node, each with the silver price to hire that worker there (`hire_cost`).

Example rows:

```text
Calpheon City -> Naive Worker, 1500
Velia -> Giant Worker, 3500
Grana -> Papu Worker, 3500
Bukpo -> Dokkebi Worker, 3500
```

## Companion Files

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `plantworker.bss`     | Optional | Resolves `worker_id` to worker stats and icon paths |
| `languagedata_en.loc` | Optional | Resolves town/node names and worker names           |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type | Field        | Notes                              |
| ------- | ---- | ------------ | ---------------------------------- |
| `+0x00` | u32  | group_count  | Number of selection groups; observed `30` in the pre-2026-09-27 fixture, `31` in the 2026-09-27 client |
| `+0x04` | ...  | group_stream | `group_count` groups packed in row |

The file is fully consumed by `4 + sum(4 + entry_count * 0x10)`.

## Record Structure

### Selection Group

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u32  | entry_count | Number of entries in this group: 8, 12, or 13   |
| `+0x04` | ...  | entries     | `entry_count` 16-byte selection entries         |

Each group repeats one `selection_id` across all entries. Observed group sizes:

| Entry Count | Group Count |
| ----------- | ----------- |
| 8           | 2           |
| 12          | 8           |
| 13          | 20          |

These are the pre-2026-09-27 fixture's 30 groups and 372 entries. The 2026-09-27 client adds Angavu Outpost (`1733`, 13 entries) as group 1, for 31 groups and 385 entries.

### Selection Entry (`0x10` bytes)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | selection_id | Town region key (`regioninfo.bss`), LOC type `17`; same value within group |
| `+0x02` | u16  | worker_id    | Worker ID; matches `plantworker.bss` and LOC type `6` |
| `+0x04` | u32  | zero_a       | Always observed as `0`                                |
| `+0x08` | u32  | hire_cost    | Hire price in silver; observed `1500`, `3500`, `10000`, `30000`, `90000` |
| `+0x0C` | u32  | zero_b       | Always observed as `0`                                |

Derived fields:

```text
selection_name = LOC type 17, str_id1=selection_id, str_id4=0
worker_name = LOC type 6, str_id1=worker_id, str_id4=0
```

## Selection IDs

| Selection ID | Name                   | Entry Count |
| ------------ | ---------------------- | ----------- |
| `5`          | Velia                  | 13          |
| `32`         | Heidel                 | 13          |
| `52`         | Glish                  | 13          |
| `77`         | Calpheon City          | 13          |
| `88`         | Olvia                  | 13          |
| `107`        | Keplan                 | 13          |
| `120`        | Port Epheria           | 13          |
| `126`        | Trent                  | 13          |
| `182`        | Iliya Island           | 13          |
| `202`        | Altinova               | 13          |
| `218`        | Asparkan               | 13          |
| `221`        | Tarif                  | 13          |
| `229`        | Valencia City          | 13          |
| `601`        | Shakatu                | 13          |
| `605`        | Sand Grain Bazaar      | 13          |
| `619`        | Ancado Inner Harbor    | 13          |
| `693`        | Arehaza                | 13          |
| `706`        | Old Wisdom Tree        | 8           |
| `735`        | Grana                  | 8           |
| `873`        | Duvencrune             | 13          |
| `955`        | O'draxxia              | 12          |
| `1124`       | Eilton                 | 12          |
| `1210`       | Dalbeol Village        | 12          |
| `1219`       | Nampo's Moodle Village | 12          |
| `1246`       | Nopsae's Byeot County  | 12          |
| `1375`       | Muzgar                 | 13          |
| `1420`       | Yukjo Street           | 12          |
| `1424`       | Godu Village           | 12          |
| `1444`       | Bukpo                  | 12          |
| `1553`       | Hakinza Sanctuary      | 13          |
| `1733`       | Angavu Outpost         | 13; 2026-09-27 client only |

## Reference Rows

| Group | Selection ID | Selection Name | Worker ID | Worker Name    | Hire Cost |
| ----- | ------------ | -------------- | --------- | -------------- | --------- |
| 0     | `77`         | Calpheon City  | `7501`    | Naive Worker   | `1500`     |
| 0     | `77`         | Calpheon City  | `7502`    | Giant Worker   | `3500`     |
| 0     | `77`         | Calpheon City  | `7571`    | Artisan Giant Worker | `90000`    |
| 18    | `735`        | Grana          | `8001`    | Papu Worker    | `3500`     |
| 20    | `955`        | O'draxxia      | `8020`    | Dwarf Worker   | `3500`     |
| 21    | `1444`       | Bukpo          | `8047`    | Dokkebi Worker | `3500`     |

Group numbers are from the pre-2026-09-27 fixture; in the 2026-09-27 client every group after `0` moves down by one.

## Suggested UI Layout

| Column      | Type | Notes                                                                 |
| ----------- | ---- | --------------------------------------------------------------------- |
| Worker ID   | num  | `worker_id`, right-aligned                                            |
| Worker Name | text | Prefer LOC type `6`; fall back to blank; colored by grade, see below  |
| City ID     | num  | `selection_id`, right-aligned                                         |
| City Name   | text | Prefer LOC type `17`; fall back to `selection_id`                     |
| Hire Cost   | num  | `hire_cost`, right-aligned                                            |

The worker name is shown in its in-game grade color, from the `plantworker.bss` companion's `grade_class` (see [plantworker](plantworker_bss.md), Grade Class; `worker_grade` on the record). All 385 entries of the 2026-09-27 client get a grade, and outside Old Wisdom Tree every grade matches its hire price.

| Grade        | Color  | CSS value |
| ------------ | ------ | --------- |
| Naive        | white  | `#ffffff` |
| Base         | green  | `#8db543` |
| Skilled      | blue   | `#04b3f1` |
| Professional | yellow | `#f6c232` |
| Artisan      | red    | `#ac510b` |
| Named        | yellow | `#f6c232` |

Green is taken from an in-game screenshot of a base Goblin Worker.

## Notes

- Observed file size is `6,076` bytes in the pre-2026-09-27 fixture, `6,288` in the 2026-09-27 client.
- There is no `PABR` magic; the file starts with the top-level group count.
- All `worker_id` values in this file exist in `plantworker.bss`.
- `zero_a` and `zero_b` are invariant zero fields across all observed entries.
- Hire costs map to a small fixed set: `1500`, `3500`, `10000`, `30000`, and `90000`. In most towns the price rises with grade (Naive `1500`, base `3500`, Skilled `10000`, Professional `30000`, Artisan `90000`).
- In game the five grades are colored white (Naive), green (base, e.g. `Papu Worker`), blue (Skilled), yellow (Professional) and red (Artisan); this file stores only the worker ID, the grade comes from `plantworker.bss`.
- Old Wisdom Tree (`706`) prices its Papu and Fadus grades in reverse: Artisan `3500`, Professional `10000`, Skilled `30000`, base `90000`.
- Checked in game on 2026-09-28: in Grána (`735`) a base worker costs 3,500, a Skilled 10,000 and a Professional 30,000; in Old Wisdom Tree an Artisan costs 3,500; in O'draxxia (`955`) a base Dwarf Worker (`8020`) costs 3,500; in Heidel (`32`) a Naive worker costs 1,500, a base 3,500, a Skilled 10,000 and an Artisan Goblin Worker (`7572`) 90,000. All nine match the stored `hire_cost` of that row, covering every price level.

## In-Game Checks

### Old Wisdom Tree Grades After the Event

Needs NPC: [Mathieu](https://bdocodex.com/us/npc/45593/)

Needs zone: Old Wisdom Tree

Old Wisdom Tree (`706`) lists all four Papu and Fadus grades, but on 2026-09-28 only Artisan Papu and Fadus workers came up there (3,500 silver, several rolls), most likely because of an event. Once it ends, roll workers at Mathieu a few times. If base, Skilled and Professional workers come up again, the list is the whole story and the reverse prices hold: a base worker costs 90,000. If only Artisans come up, something outside this file limits the grades there.
