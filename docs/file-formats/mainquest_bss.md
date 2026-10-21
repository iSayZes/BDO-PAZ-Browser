# `mainquest.bss` Format

## Purpose

Defines the main-quest list: quest IDs grouped into main-quest chains, each group named by LOC type 43, with per quest a condition line (where and when it can be accepted) and two condition scripts. 120 groups and 3,268 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records                              | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ------------------------------------ | --------- |
| 1      | 1485 and later | 3474    | `mainquest.bss` | 447,458 | 3,270 Quest Reference Row, 120 Group | 17        |

| Layout | File            | Known             | Unknown      |
| ------ | --------------- | ----------------- | ------------ |
| 1      | `mainquest.bss` | 446,978 B (99.9%) | 480 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Observed Values

Same layout as [`newquest.bss`](newquest_bss.md), the layout reference: an 8-byte `PABR` header with a group count; per group an 11-byte header, 17-byte quest reference rows and a 12-byte trailer; a string table; an 8-byte file trailer. One handler reads all four quest lists. Values seen on client 3458:

| Field                                  | Observed                                              |
| -------------------------------------- | ----------------------------------------------------- |
| `group_count`                          | `120`                                                 |
| First group                            | key `104`, `14` rows                                  |
| Group header `group_type`              | `0`, except `1` on key 101 `[Invitation from I] Someone Beckons` |
| Group trailer start / end index        | Index `2`, the empty string: no event period          |
| Row `is_sub_quest`                       | `0`, except `1` on 7 rows, see Open Questions         |
| Row `hide_conditions_index`                   | Empty string on 2,667 rows, a script on 601           |
| Row `visible_conditions_index`                   | Empty string on 1,348 rows, a script on 1,920         |
| String table                           | `3,490` strings; `string_count` at `0x0000E3D4`       |

The scripts check prerequisite quests (`clearquest`, `progressquest`), class (`checkClass`), level and content groups (`isContentsGroupOpen`); see String Table in the `newquest.bss` doc for the two script roles.

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `43` holds the English text of this list, keyed by the group's `group_key`:

| Key                                                               | Text                                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`                              | Group name, e.g. key 104 `[Special Growth] Taking My Own Path` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `From <PAColor0xfff3d900>Alustin<PAOldColor> in Velia, complete ...` |

On client 3458 all 120 groups have a name (type 43 has 170, keys 1 to 171, so some belong to groups no longer in the file) and all 3,268 rows have a condition line. Condition lines carry `<PAColor>` tags (all but 6); group names do not. The string table holds the Korean source of both, which the handler shows where LOC has no row.

## Notes

- Decompressed size is `447,790` bytes on client 3458.
- No quest appears twice; every group key is unique.
- Earlier versions of this doc read the later group header as 22 bytes starting one byte later, so each row took its leading flag byte from the byte before it; the row values were the same. Up to client 3464 the flag was still read one row late, see the Notes of [`newquest.bss`](newquest_bss.md). They named the first header's `group_key` `unknown_00` and the later header's `group_key` `unknown_0c`.

## Open Questions

### What Does `is_sub_quest` Change?

`1` on only 7 rows, all in group key 51: quests 6603 / 2 to 8, which share one `hide_conditions` (client 3464). The server's `IsSubQuest` sets the same 7 rows; what the flag changes in the list is not confirmed.

### Shared Fields

What `group_type` selects is open for all four lists; see the Open Questions of [`newquest.bss`](newquest_bss.md).
