# `recommendationquest.bss` Format

## Purpose

Defines the recommended-quest list: quest IDs grouped under recommendations such as `[ADV Support] Inventory Expansion!` or `[Life 101] The Adventurer That Does It All`, each group named by LOC type 28, with a condition line per quest. 122 groups and 1,291 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records                              | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------- | ------------------------------------ | --------- |
| 1      | 1784 and later | 3474    | `recommendationquest.bss` | 202,171 | 1,290 Quest Reference Row, 122 Group | 17        |

| Layout | File                      | Known             | Unknown      |
| ------ | ------------------------- | ----------------- | ------------ |
| 1      | `recommendationquest.bss` | 201,683 B (99.8%) | 488 B (0.2%) |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `122`                                                 |
| First group                            | key `165`, `9` rows                                   |
| Group header `group_type`              | `0` to `8`, see Open Questions                        |
| Group trailer start / end index        | Index `2`, the empty string: no event period          |
| Row `is_sub_quest`                       | `0` on every row                                      |
| Row `hide_conditions_index`                   | Empty string on 1,149 rows, a script on 142           |
| Row `visible_conditions_index`                   | Empty string on 1,045 rows, a script on 246           |
| String table                           | `1,456` strings; `string_count` at `0x000060B9`       |

The scripts check prerequisite quests, level, class, content groups, knowledge (`getknowledge(9917);`), items (`getItemCount`) and Olvia Academy enrolment (`checkOlviaAcademyStudent`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `28` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 165 `[Life 101] The Adventurer That Does It All` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `<PAColor0xfff3d900>from Lv. 60<PAOldColor>, via <PAColor0xfff3d900>Fughar<PAOldColor>` |

On client 3458 all 122 groups have a name (type 28 has 192, keys 1 to 200, so some belong to groups no longer in the file) and all 1,291 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 2); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `203,307` bytes on client 3458.
- 23 quests sit in two groups, with a condition line under each key: quest 7215 / 1 is in key 13 (`[ADV Support] [Lv. 53] Legendary Leveling with Chenga and Quests`) and key 155 (`[Social Action] Please Read Quietly!`).

## Open Questions

### Group Header Byte `group_type`

`0` on 65 of 122 groups and `1` to `8` on the rest, grouped by theme: 1 holds Olvia Academy and `[ADV Support] [Lv. 53]` leveling groups, 2 mounts and outfits (`[Mount] Shai - Fwuzzy Alpaca`), 3 `[The Great Expedition]`, 4 to 7 the `[Life] [Leap]` gurus split by life skill (cooking and alchemy at 5, hunting at 7) and 8 a mix (`[ADV Support] Inventory Expansion!`, `[Music] ...`). It may be the category tab of the recommendation window; the server calls it `RecommendationQuestType` and sets the same value on 17 of the 19 shared groups where it is not `0`, but no Lua getter reads it.

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
