# `repetitionquest.bss` Format

## Purpose

Defines the repeatable-quest list: daily, weekly and contribution quests grouped under names such as `[Contribution] [Lv. 35] Calpheon City` or `[Throne of Edana] [Weekly] For the Throne`, each group named by LOC type 42, with a condition line per quest. 48 groups and 806 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes   | Records                           | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------- | --------------------------------- | --------- |
| 1      | 1784 and later | 3473    | `repetitionquest.bss` | 200,069 | 806 Quest Reference Row, 48 Group | 17        |

| Layout | File                  | Known             | Unknown      |
| ------ | --------------------- | ----------------- | ------------ |
| 1      | `repetitionquest.bss` | 199,877 B (99.9%) | 192 B (0.1%) |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `48`                                                  |
| First group                            | key `51`, `10` rows                                   |
| Group header `group_type`              | `0` on every group                                    |
| Group trailer start / end index        | Index `31`, the empty string: no event period         |
| Row `is_sub_quest`                       | `0` on every row                                      |
| Row `hide_conditions_index`                   | Empty string on 678 rows, a script on 128             |
| Row `visible_conditions_index`                   | Empty string on 517 rows, a script on 289             |
| String table                           | `633` strings; `string_count` at `0x000039DE`         |

The empty string sits at index `31` here, so the script fields read `31` on most rows. The scripts check other quests of a weekly set (`clearquest(9108,2);<or>clearquest(9108,3);...`), life skill levels (`getLifeLevel(6)>80;`), content groups and random rolls (`checkRandom`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `42` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 51 `[Throne of Edana] [Weekly] For the Throne` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `<PAColor0xfff3d900>from 350 AP & 427 DP <PAOldColor>via the <PAColor0xfff3d900>Throne of Aetherion<PAOldColor> ...` |

On client 3458 all 48 groups have a name (type 42 has 54, keys 1 to 54, so some belong to groups no longer in the file) and all 806 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 1); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `200,069` bytes on client 3458.
- One quest sits in two groups, with a condition line under each key: quest 4500 / 131 is in key 3 (`[Contribution] [Lv. 52] Mediah`) and key 45 (`Monster Zone Info`).

## Open Questions

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
