# `npcpersonality.dbss` Format

## Purpose

Defines NPC personality entries used to parameterise AI behaviour. Each record maps a personality ID to three knowledge group references (each with a need count beside it) and four floating-point amity threshold parameters. Used to drive the in-game amity mini-game.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ------ | ------------------- | --------- |
| 1      | 1485 and later | 3474    | `npcpersonality.dbss`       | 40,192 | 1,182 Record        | 34        |
| 1      | 1485 and later | 3474    | `npcpersonalityoffset.dbss` | 11,824 | 1,182 Offset Record | 10        |

| Layout | File                        | Known             | Unknown         |
| ------ | --------------------------- | ----------------- | --------------- |
| 1      | `npcpersonality.dbss`       | 40,192 B (100.0%) | 0 B (0.0%)      |
| 1      | `npcpersonalityoffset.dbss` | 9,460 B (80.0%)   | 2,364 B (20.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                    |
| --------------------------- | -------- | --------------------------------------- |
| `npcpersonalityoffset.dbss` | Required | ID-keyed index (same count, own order)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                          |
| ------- | ------------- | ------- | ---------------------------------------------- |
| `+0x00` | u32           | count   | Number of personality records (observed: 1,182 in the pre-2026-09-27 fixture and in the 2026-09-27 client) |
| `+0x04` | Record[count] | records | See Record                                     |

### Record (34 bytes)

| Offset  | Type | Field              | Notes                                                         |
| ------- | ---- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16  | personality_id     | Unique personality identifier (the NPC's character key)       |
| `+0x02` | u16  | group_a_id         | First amity interest group (knowledge group ID)               |
| `+0x04` | u16  | group_a_need_count | Need count for group A; see below                             |
| `+0x06` | u16  | group_b_id         | Second amity interest group                                   |
| `+0x08` | u16  | group_b_need_count | Need count for group B                                        |
| `+0x0A` | u16  | group_c_id         | Third amity interest group                                    |
| `+0x0C` | u16  | group_c_need_count | Need count for group C                                        |
| `+0x0E` | u16  | personality_id_dup | The row's own key member; always equal to `personality_id` at `+0x00` |
| `+0x10` | f32  | interest_min       | Inclusive lower bound for amity interest (range: 11–37)       |
| `+0x14` | f32  | interest_max       | Upper bound for amity interest (range: 23–70); inclusive or exclusive is open |
| `+0x18` | f32  | favor_min          | Inclusive lower bound for amity favor (range: 10–35)          |
| `+0x1C` | f32  | favor_max          | Upper bound for amity favor (range: 14–68; 15–70 in the 2026-09-27 client); inclusive or exclusive is open |
| `+0x20` | u16  | personality_type   | Personality category code (see enum below)                    |

#### Interest Groups

Each group is a u16 knowledge group ID (matches `node_id` in `mentalcard.dbss`) followed by its u16 need count (`group_a_need_count`, `group_b_need_count`, `group_c_need_count`; source names under Field Names). Earlier versions of this doc read each pair as one packed u32 and called the high half `item_count`.

The same numbers appear on the BDO wiki next to each NPC's interest groups, but the game does not show them: the conversation window lists only the topics you can use, with no per-group count or maximum (I checked in game, 2026-09-27). It is not the number of topics offered either: with Oliviero (`6` for Serendia Adventure Log II) the topic list showed 7 cards of that group. What the current game does with the need count is open. On client 3474 the values are 0, 1, 2, 4, 5, 6, 7, 8 and 10, and all three fields of a record share one value in 1,121 of 1,182 records.

### `npcpersonalityoffset.dbss`

An index file with one entry per personality record.

| Offset  | Type                 | Field   | Notes                                  |
| ------- | -------------------- | ------- | -------------------------------------- |
| `+0x00` | u32                  | count   | Must equal `npcpersonality.dbss` count |
| `+0x04` | Offset Record[count] | records | See Offset Record                      |

### Offset Record (10 bytes)

| Offset  | Type | Field          | Notes                                                                          |
| ------- | ---- | -------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | personality_id | Matches `personality_id` in the main record                                    |
| `+0x02` | u32  | data_offset    | Byte offset into main file; 2 bytes past record start (skips `personality_id`) |
| `+0x06` | u16  | data_size      | Always 32 (= record size minus the 2-byte personality_id header)               |
| `+0x08` | u16  | unknown_08     | Not parsed                                                                     |

`record_start = data_offset - 2`

Every offset row points at a record that repeats its `personality_id`, and every record is indexed exactly once, but the rows are not in main-file order: only the first 53 step by the 34-byte stride, the rest are ordered differently (pre-2026-09-27 fixture and 2026-09-27 client alike). An earlier version of this doc called it a sequential index in main-file order.

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

[`zodiacsignorder.dbss`](zodiacsignorder_dbss.md) stores the sign of every `personality_type` as `zodiac_id`, and it equals the major in all 24 records (client 3464). The names are LOC type 7 sign names from [`zodiacsign.dbss`](zodiacsign_dbss.md). Majors 1 and 9 have only variant 1 here.

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) list the members of
`gc::NpcPersonalityStaticStatus` in this order: `pa::Array<gc::FavoritedTheme,3> _themeList`
(each `gc::FavoritedTheme` is `KeyType<unsigned short> _key`, `unsigned short _needCount`
and a `gc::MentalThemeStaticStatus*`), `KeyType<unsigned short> _key`, `float _minDv`,
`float _maxDv`, `float _minPv`, `float _maxPv` and
`KeyType<unsigned short> _zodiacSignOrderKey`.

The server dump of a private server on client 1784 (`Instance_dumpFull.exe`) fills those
members twice. `NpcPersonalityStaticStatusManager::readFromBinarybyDynamic` (VA
`0x140b98880`) hands each `npcpersonality.dbss` row, past the leading key, to a row reader
(VA `0x140b96530`) that writes the 32 bytes in file order to the 2016 member offsets. The
`Personality_Table` sheet loader reads one column per member (VA `0x140956897` to
`0x1409569fa`) and stores the `Npc` ID column as `_key` (VA `0x140b95fca`):

| Field                | File    | Member (2016)                | Member  | Sheet column         |
| -------------------- | ------- | ---------------------------- | ------- | -------------------- |
| `group_a_id`         | `+0x02` | `_themeList[0]._key`         | `+0x00` | `Theme1`             |
| `group_a_need_count` | `+0x04` | `_themeList[0]._needCount`   | `+0x02` | `NeedCount1`         |
| `group_b_id`         | `+0x06` | `_themeList[1]._key`         | `+0x10` | `Theme2`             |
| `group_b_need_count` | `+0x08` | `_themeList[1]._needCount`   | `+0x12` | `NeedCount2`         |
| `group_c_id`         | `+0x0A` | `_themeList[2]._key`         | `+0x20` | `Theme3`             |
| `group_c_need_count` | `+0x0C` | `_themeList[2]._needCount`   | `+0x22` | `NeedCount3`         |
| `personality_id_dup` | `+0x0E` | `_key`                       | `+0x30` | `Npc`                |
| `interest_min`       | `+0x10` | `_minDv`                     | `+0x34` | `MinDv`              |
| `interest_max`       | `+0x14` | `_maxDv`                     | `+0x38` | `MaxDv`              |
| `favor_min`          | `+0x18` | `_minPv`                     | `+0x3C` | `MinPv`              |
| `favor_max`          | `+0x1C` | `_maxPv`                     | `+0x40` | `MaxPv`              |
| `personality_type`   | `+0x20` | `_zodiacSignOrderKey`        | `+0x44` | `ZodiacSignIndexKey` |

The values agree. The `Personality_Table` sheet in that server's `datasheet_memorycarddatatable.xlsm`
matches its own compiled `npcpersonality.dbss` on every column above in all 1,122 rows. On
the official client 1784 file all 1,055 records are in the sheet, and the group, need count
and `ZodiacSignIndexKey` columns match every one of them; the ten records whose three need
counts differ pin `NeedCount1` to `+0x04`, `NeedCount2` to `+0x08` and `NeedCount3` to
`+0x0C`. The four floats match the sheet exactly on only 230 to 310 of the 1,055, but each lies
within 3 of its column on 838 to 962 of them, a mean distance of 1.4 to 2.1 against 7.2 or
more to each of the other three float columns. The sheet's `NPC등급` and `NPC_Importance`
columns have no field in the file.

`personality_type` keeps its name; the sheet calls it `ZodiacSignIndexKey` and the 2016
member `_zodiacSignOrderKey`, the key of [`zodiacsignorder.dbss`](zodiacsignorder_dbss.md).
`interest_*` and `favor_*` keep theirs too, from the in-game readings under Notes. The server
code of a private server on client 519 reads `Personality_Table` the other way round:
`CardGame` rolls `npcInterest` between `MinPv` and `MaxPv` and `npcSympathy` between
`MinDv` and `MaxDv`. Ornella's in-game Interest of 22 to 23 fits `+0x10`, which holds
`MinDv`, so these names follow the client.

The same server code (`PersonalityT`, `MentalCardHandler.newGame`) reads `NeedCount1` as the
number of `Theme1` knowledge the player must hold to start the conversation game, and as the
number of card slots in that game. That is its own reconstruction of the older game, not
client data. The source sheet puts a reference column `#테마안에 있는 지식 개수` ("number of
knowledge in the theme") before each `NeedCount`; in its first row the three themes hold 14,
13 and 17 knowledge against a need count of 7 each.

## Notes

- All 1182 `personality_id` values are unique; it is a true record key.
- `personality_id_dup` at `+0x0E` is always identical to `personality_id` at `+0x00`: the leading u16 is the dbss row key, and `+0x0E` is the static status's own `_key` member (see Field Names).
- The `variant` in `personality_type` (1 or 2) picks one of the two star orders in `zodiacsignorder.dbss`; any other in-game meaning is unknown. Distribution is roughly even (584 variant-1, 598 variant-2).
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

### What does the need count control in the current game?

The 2016 member is `_needCount` and the sheet column `NeedCount1` to `3` (see Field Names), and the BDO wiki lists the same numbers next to each interest group. The game shows no per-group count, though, and Oliviero's topic list held 7 cards of a group whose need count is `6`. It may be a knowledge count the player needs for the group, cap how many of the group's topics the NPC accepts, or be unused since the conversation game changed. `0` occurs as well.

### Why do the official floats differ from the sheet?

The private server on client 1784 compiled its `npcpersonality.dbss` with every float equal to its `Personality_Table` sheet, but the official client 1784 file matches that sheet exactly on only 230 to 310 of 1,055 records per float, while groups, need counts and `ZodiacSignIndexKey` match on all of them. Whether the official build rolls the ranges when it compiles the sheet, or the private server edited three quarters of the float cells, is open. A roll at compile time would also explain why the stored ranges move between client versions while the groups stay (see Notes).

### Are the upper bounds inclusive?

An earlier version of this doc called `interest_max` and `favor_max` exclusive (usable maximum one less than stored) without recorded evidence. Ornella's in-game favor reached `28`, her stored maximum in the pre-2026-09-27 fixture (`29` in client 3458), which argues against that, but other readings fall below the stored minimums (see Notes), so the stored range may not bound what the game rolls. How the displayed range is derived from the stored one is open; the check for Ornella's current maximum is under In-Game Checks.

## In-Game Checks

### Ornella's Favor Maximum

Needs NPC: [Ornella](https://bdocodex.com/us/npc/41002/)

Ornella's stored favor range is `26` to `29` in client 3458. The NPC rolls Favor at the start of each conversation (see Notes), so start about 20 new conversations with her and write down each Favor. A `29` means `favor_max` is inclusive; `26` to `28` only, with `28` seen, means the usable maximum is one less than stored. Readings below `26` mean the stored range does not bound the roll, as for Oliviero and Cleia.
