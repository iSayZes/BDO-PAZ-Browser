# `multiplequest.bss` Format

## Purpose

Quest ID ranges: per quest chain a first and a last quest ID. The quests of a range are versions of one quest, and the `condition_script` of each version in `quest.dbss` lets a character see one of them at a time: by life skill level, contribution points, an owned item, a random roll or a knowledge entry (see [Ranges](#ranges)). No quest script names another quest of its own range, while chains 4549 and 9053, two ranges of the same Training quest, exclude each other by script. What the game does with a range is open (see Open Questions). The plain PABR file holds fixed-size rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `multiplequest.bss` | 266   | 41 Row  | 6         |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 1      | `multiplequest.bss` | 266 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                           |
| --------------------- | -------- | ------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=min_quest_id` or `max_quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                                    |
| ------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                             |
| `+0x04`             | u32          | count              | Number of rows                                           |
| `+0x08`             | Row[count]   | rows               | See Row                                                  |
| `rows+0x00`         | String Table | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32          | string_table_start | Absolute offset of `string_count`; equals `8 + 6 × count` |
| `string_table+0x04` | u32          | zero               | Always `0`                                               |

The string table tail is the one `barterlifelevelinfo.bss` and `questprogressgroup.bss` use (`_common/pabr_strings.py`).

### Row (6 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | LOC type 18 `str_id1`; unique per row                                   |
| `+0x02` | u16  | min_quest_id   | First quest of the range, LOC type 18 `str_id2`                          |
| `+0x04` | u16  | max_quest_id   | Last quest of the range, LOC type 18 `str_id2`; never below `min_quest_id` |

`quest_chain_id` with a quest ID is the quest key, the `(quest_id << 16) | quest_chain_id` of `allquestlist.bss` read as two u16 values.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Ranges

On client 3474 the file holds 41 rows. In 39 of them every quest from `min_quest_id` to `max_quest_id` is a `quest.dbss` record; chains 11210 (1 to 23) and 11368 (1 to 3) have no record at all. `min_quest_id` is `1` on 39 rows and `2` on chains 3907 and 11422.

What the `condition_script` of the quests in a range checks, client 3474:

| Chains                       | Range              | Quests                                                                     | Each version needs                                         |
| ---------------------------- | ------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 4549, 9053                   | 1 to 7             | `[Daily] [Beginner]` to `[Guru] No Worries for the Prepared`               | A Training level band, `getLifeLevel(6)`                   |
| 4576, 9054                   | 1 to 8             | `Krogdalo's Origin Stone Support`, then `[Beginner]` to `[Guru] Carrot Confit Support` | A Training level band (quest 1 has none)          |
| 9039                         | 1 to 35            | `[Daily] [Gathering] Researching ...`                                      | Quests 1 to 30 `getLevel()>99`; 31 to 35 a Gathering level band |
| 9044, 9045                   | 1 to 6, 1 to 12    | `[Daily] [Cooking]` and `[Alchemy] Striving Towards Imperial Delivery`     | A Cooking or Alchemy level band and a `checkRandom` roll   |
| 9047, 9048                   | 1 to 6             | `[Weekly Contribution]` quests                                             | A contribution point band, `getAquredExplorepoint()`       |
| 9058                         | 1 to 42            | `[Select One]` weekly quests, 7 kinds (subjugation, gathering, training, farming, barter, sailing, hunting) | A contribution point band, 6 bands per kind |
| 3737, 3738, 3739             | 1 to 4             | `[Crossroad] [Difficulty 0]` to `[Difficulty 3] Otterly-concerned Vellonia Merchants` | Nothing that tells them apart (`getLevel()>1`)  |
| 3907                         | 2 to 11            | `[Daily] Kakuo Paw-doodles!`                                               | Class 10 or not, and a `checkRandom(n,5)` roll; quest 1 is outside the range |
| 8741                         | 1 to 20            | `Big Bad Auntie's Foreign Cuisine Study`                                   | A `checkRandom(n,4)` roll, one knowledge entry not learned yet and the entries of the quests before |
| 8746                         | 1 to 3             | Three `[Daily]` quests with different titles                               | A `checkRandom(n,3)` roll                                  |
| 9022                         | 1 to 9             | `[Crossroad] Adonna's Fortune Telling - First Card` to `Ninth Card`        | The card's knowledge entry not yet learned                 |
| 9026                         | 1 to 11            | `Agris:` quests, one per hunting ground                                    | The same event condition, word for word, on all 11         |
| 11241                        | 1 to 7             | `[Event] What's in the Cards for Today?`                                   | `getLevel()>99` on all 7                                   |
| 11356                        | 1 to 5             | `[Event] [Weekly] Gather ... Samples`                                      | The same event condition, word for word, on all 5          |
| 11422                        | 2 to 3             | `[Crossroad] [Event] Choose Zobadi`, `Choose Afuaru`                       | Quest 11422 / 1 cleared; quest 1 is outside the range      |
| 40027, 40048, 40061, 40064   | 1 to 5             | `[Awakening Weapon EXC]` PRI (I) to PEN (V)                                | The item at that enhancement level, `getitemcount(item,16..20)` |
| 41005 to 41011               | 1 to 5, 1 to 7, 1 to 13 | `Old Moon's Resplendent` armor and weapons, one per boss item         | The item (41011: an item group) owned or equipped at enhancement level 19 or 20 |
| 41013                        | 1 to 13            | `[Weekly] Imperfect Beings`                                                | Quest 1 open; 2 to 13 `getLevel()>99`                      |
| 41017 to 41022               | 1 to 2, 1 to 34, 1 to 30 | `[Once per Family] Old Moon's Resplendent ...`, one per item         | The item owned or equipped at enhancement level 19         |

Outside their range: 4549 / 8 to 11 (Grand Prix quests), 3907 / 1, 11422 / 1, 41021 / 35 to 50 and 41022 / 31 to 48. The last two are newer items of the same `[Once per Family]` quests.

## Field Names

The `Multiple_Quest` sheet of a private server's `DataSheets.bexcel` on client 1784 has three columns: `Multiple_QuestGroup` (`quest_chain_id`), `Min` (`min_quest_id`) and `Max` (`max_quest_id`). Its 26 rows are the 26 rows of the client 1784 file, value for value; the file has them in another order. On client 3474, 17 of the 18 shared chains have the same range; chain 41010 grew from 1 to 9 to 1 to 13. The 8 chains only the sheet has (11262, 11275 to 11279, 40030, 40031) are gone from the client 3474 file, which has 23 newer chains. Every quest workbook (`datasheet_questtable_*.xlsm`) of that private server has a `Multiple_Quest` sheet with the same three columns and a `#^E_Merge Index` note column; only the event, journal, season and season2 workbooks fill it. The server executable names the manager `MultipleQuestStaticStatusManager` and the loader step `loadMultipleQuestInformation`. The 2016 PDB has no `MultipleQuest` symbol.

## Notes

- Decompressed size on client 3474: `266` bytes, 41 rows, `8 + 41 × 6 + 12`. Client 1784 has the same layout: `176` bytes, 26 rows.
- Rows are not in key order, on client 1784 and on client 3474.
- None of the 3,073 client Lua files (`luacscript/x64/`, client 3474) has `MultipleQuest` or `Multiple_Quest` in it, and no `quest.dbss` script calls a function with `multi` in its name.

## Open Questions

### What a Range Does

The rows group versions of one quest, but nothing in the client data says what the game does with a group. Chains 4549 and 9053 hold the same `No Worries for the Prepared` quest and block each other with `!clearQuest` and `!progressQuest` for every quest of the other chain, while no quest names a quest of its own range; 4576 and 9054 do the same. That points to the range making its versions exclusive (one accepted or cleared version blocks the rest, or the daily and weekly reset counts the range as one quest), but the server may also use the range for something the client never sees, such as picking which version an NPC offers. The `[Select One]` title of chain 9058 fits exclusivity across its 7 kinds.

## In-Game Checks

### Chain 9058 Versions as Exclusive

Needs zone: the city where Liana (NPC 59717) stands

This checks whether accepting one quest of a range hides the other quests of that range. bdocodex lists Liana as the start NPC of 9058/1 `[Weekly Subjugation] Subjugation Request for the Villagers` and 9058/7 `[Weekly Gathering] About the Mysterious Fairy's Breath`.

1. Talk to Liana and open her quest list.
2. Note every `[Select One]` quest she offers.
3. Accept one of them.
4. Open her quest list again and note which `[Select One]` quests are left.

Expected result: the other `[Select One]` quests are gone after step 3. Then a range makes its versions exclusive and What a Range Does is answered. If they are still offered, the range does something else.
