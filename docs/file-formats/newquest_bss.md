# `newquest.bss` Format

## Purpose

Defines the new-quest (event) list: quest IDs grouped under events such as `[Event] Mastering Life Skills`, each group with an event period, and per quest a condition line and two condition scripts. 232 groups and 1,281 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts, dates); LOC type 58 holds the English names and condition lines.

[`mainquest.bss`](mainquest_bss.md), [`recommendationquest.bss`](recommendationquest_bss.md) and [`repetitionquest.bss`](repetitionquest_bss.md) share this layout, each with its own LOC type; one handler reads all four. This doc is the layout reference for all four.

Example:

```text
group 0 (key 1, "[Event] Mastering Life Skills", 2018-10-3 10:00 to 2018-11-7 09:59)
  -> quest 11059 / 9 -> [Event] Love for Pets
quest 11101 / 11 -> offered while checkperiodbyGmt(0, 2019/9/4-00:00, 2019/9/25-09:00);
                    ruled out by clearQuest(11101,9);<or>clearQuest(11101,10);<or>...
```

## File Layout

All multi-byte values are little-endian unless noted otherwise.

```text
header (8)
group[group_count]:
    group header (10)
    quest reference row (17) x quest_ref_count
    group trailer (13)
string table: u32 string_count, string entry x string_count
file trailer (8)
```

### Header (8 bytes)

| Offset  | Type    | Field       | Notes                                      |
| ------- | ------- | ----------- | ------------------------------------------ |
| `+0x00` | char[4] | magic       | `PABR` (ASCII)                             |
| `+0x04` | u32     | group_count | Number of quest groups; `232` on client 3458 |

### Group Header (10 bytes)

| Offset  | Type | Field           | Notes                                                                   |
| ------- | ---- | --------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | group_key       | The group's key, see Localization; unique per group                     |
| `+0x02` | u32  | name_index      | String table index of the Korean group name (`group_name_kr`); `0` for the first group |
| `+0x06` | u8   | unknown_06      | `0` on most groups; see Open Questions                                  |
| `+0x07` | u16  | quest_ref_count | Number of following rows                                                |
| `+0x09` | u8   | padding         | Observed zero                                                           |

### Quest Reference Row (17 bytes, repeated `quest_ref_count` times)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00     | `0` on every row here; `1` on 7 `mainquest.bss` rows                    |
| `+0x01` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key       |
| `+0x03` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x05` | u32  | condition_index | String table index of the Korean condition line (`condition_kr`), the source of the LOC condition line |
| `+0x09` | u32  | script_1_index | String table index of the first condition script (`script_1`), often the empty string; see String Table |
| `+0x0D` | u32  | script_2_index | String table index of the second condition script (`script_2`), often the empty string; see String Table |

### Group Trailer (13 bytes)

| Offset  | Type | Field        | Notes                                                                  |
| ------- | ---- | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00   | Observed zero                                                          |
| `+0x01` | u32  | event_start_index | String table index of the event start (`event_start`), e.g. `2019-10-16 04:00`; the empty string in the other three lists |
| `+0x05` | u32  | event_end_index   | String table index of the event end (`event_end`), e.g. `2019-11-13 05:59`; always after the start |
| `+0x09` | u32  | unknown_09   | Observed `0` in every group of the four files                          |

The start of group 1 `[Event] Black Desert 2019 Halloween` is `2019-10-16 04:00`, and its English condition lines read `Oct 16 (after maintenance) - ...`.

The times are stored without zero padding (`2018-10-3 10:00`, `2019-7-24 9:00`). The parser pads month, day and hour (`2018-10-03 10:00`) so they sort as text, and keeps text in any other form as stored. All 464 times on client 3458 have the `YYYY-M-D H:MM` form.

### String Table

Follows the last group trailer: a u32 `string_count`, then `string_count` entries, indexed from `0`. It is the counted string table other PABR `.bss` files end with (`exploration.bss`, `npcsimply.bss`, `menu.bss`), read by `_common/pabr_strings.py`.

| Offset  | Type      | Field  | Notes                                     |
| ------- | --------- | ------ | ----------------------------------------- |
| `+0x00` | u8        | is_wide | `1` on every entry here: UTF-16-LE (`0` would be UTF-8) |
| `+0x01` | u32       | length  | Text length in bytes                      |
| `+0x05` | u8[]      | text    | `length` bytes, no terminator             |

The table holds each distinct string once, in first-use order: the group name, then each row's condition line and two scripts, then the trailer's dates. On client 3458 every entry is used (1,840 here). Index `0` is the first group's name, and the empty string sits where it is first used: index `2` here and in `mainquest.bss` and `recommendationquest.bss`, `31` in `repetitionquest.bss`. That is why the script indexes repeat one value on so many rows.

The condition lines are the Korean source of the LOC lines and carry the same `<PAColor>` tags. The scripts are client condition calls separated by `;`, with `<or>` between alternatives and `!` for negation: `checkperiodbyGmt(0, 2019/9/4-00:00, 2019/9/25-09:00);`, `clearquest(40022,1);`, `progressquest(...)`, `getLevel()>59;`, `isContentsGroupOpen(0,2177);`, `checkClass(...)`, `getLifeLevel(6)>80;`. Across the four files:

- `script_2` reads as the condition for the quest to be offered: event periods, content groups, level and class checks, prerequisite quests (`mainquest.bss` quest 40022 / 2 needs `clearquest(40022,1);`), and `!clearquest` / `!progressquest` of the quest itself.
- `script_1` mostly lists the quests that rule this one out: the other branches of a crossroad (7500 / 81 lists 7500 / 82), `do not accept Techthon and Quality Iron` (2001 / 138 lists 2001 / 137), and the other quests of a "once a week per Family" set. No level check ever appears in it.

Calls across the four files on client 3458: `script_1` holds `clearquest` 2,846 times and `progressquest` 1,990 times against 336 negated calls, and never `getLevel` or `checkperiodbyGmt`. `script_2` holds `isContentsGroupOpen` 6,833 times, `checkperiodbyGmt` 5,494, `getLevel` 1,410 and a negated `clearquest` / `progressquest` 4,577 times.

Neither script holds every condition its LOC line names: of 496 `repetitionquest.bss` lines that start `from Lv. N`, 75 have the level check in a script. The rest is likely checked by the quest itself.

### File Trailer (8 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u32  | table offset  | File offset of the string table's `string_count` (`0x69F1` here) |
| `+0x04` | u32  | unknown_04    | Observed `0`                                             |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Localization

LOC type `58` holds the English text of this list, keyed by the group's
`group_key`:

| Key                                              | Text                                         |
| ------------------------------------------------ | -------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`             | Group name, e.g. key 1 `[Event] Mastering Life Skills` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `From <PAColor0xfff3d900>Lara <PAOldColor>during the event, once per Family` |

On client 3458 all 232 groups have a name (type 58 has 265, so some
belong to groups no longer in the file) and all 1,281 rows have a
condition line. A quest in two groups has a line under each key: quest
11060 / 1 sits in the groups with keys 2 (`[Event] Black Desert 2019
Halloween`) and 62 (`[Event] Black Desert 2020 Halloween`). Condition lines carry `<PAColor>`
tags; group names do not. The Korean names and condition lines in the
string table are the source of both, and the handler shows them where LOC has no row.

## Reference Rows

Client 3458:

| Group | Row | Group Key | Quest Chain ID | Quest ID | condition_index | script_1_index | script_2_index | Example LOC Title |
| ----: | --: | --------: | -------------: | -------: | --------------: | -------------: | -------------: | ----------------- |
| 0     | 0   | `1`       | `11059`        | `9`      | `1`        | `2`        | `2`        | `[Event] Love for Pets` |
| 0     | 1   | `1`       | `11059`        | `10`     | `1`        | `2`        | `2`        | `[Event] Savory Good Feed` |

## Suggested UI Layout

| Column       | Type | Notes                                                            |
| ------------ | ---- | ---------------------------------------------------------------- |
| Main ID      | num  | `quest_chain_id`; LOC type 18 `str_id1`                          |
| Sub ID       | num  | `quest_id`; LOC type 18 `str_id2`                                |
| Group Key    | num  | `group_key` of the row's group                                   |
| Group Name   | text | LOC type 58 `str_id1 = group_key`, `str_id4 = 0`; else the Korean `group_name_kr` |
| Event Start  | text | `event_start`; `newquest.bss` only                               |
| Event End    | text | `event_end`; `newquest.bss` only                                 |
| Icon         | text | Quest icon resolved from `packed_quest_id` through the quest icon index |
| Title        | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0`, in its game colours |
| Condition    | text | LOC type 58 `(packed_quest_id, group_key)`, `str_id4 = 1`, in its game colours; else the Korean `condition_kr` |
| Offered When* | text | `script_2` on one line; the `*` marks the role as our reading, not confirmed (see Open Questions) |
| Ruled Out When* | text | `script_1` on one line; the `*` marks the role as our reading, not confirmed (see Open Questions) |

`group` (the index in file order), `unknown_00`, `unknown_06`, the string table indexes and the Korean `group_name_kr` / `condition_kr` stay on the record for search and export but are not shown. The other three lists show the same columns without Event Start and Event End.

## Notes

- Decompressed size is `820,905` bytes on client 3458 (`816,761` with 224 groups and 1,255 rows before 2026-09-27).
- 27 quests sit in two groups (29 before 2026-09-27); each copy has its own condition line in LOC.
- The string table indexes shift whenever a string is added earlier in the file, so `condition_index` / `script_1_index` / `script_2_index` are not stable across patches: quest `77129` had `condition_index = 899` before 2026-09-27 and `896` after.
- Earlier versions of this doc and the handler read a 10-byte first group header and a 23-byte later one: the previous group's trailer followed by the next group's header. The rows were the same. They called the row's `unknown_00` `flags`, called `condition_index` / `script_1_index` / `script_2_index` `sequence_a` / `sequence_b` / `sequence_c` and later `unknown_05` / `unknown_09` / `unknown_0d`, and named the header fields `header_flag`, `unknown_a` to `unknown_d`, `group_key_a` and `group_key_b`.

## Open Questions

### Group Header Byte `unknown_06`

`0` on 227 of 232 groups here, and `1`, `2`, `6` or `8` on the rest (`[Hunting] Sniping, ...` 2, `Krogdalo's Three Seeds` 1, `[Season] Stronger Tuvala Gear` 8). In `recommendationquest.bss` it runs `0` to `8` and groups by theme ([Life] [Leap] gurus at 4 to 7, mounts and outfits at 2), so it may be a category or tab; which UI uses it is not confirmed.

### Script Roles

What we think: `script_2` says when the quest is offered and `script_1` when it is ruled out. This is read from the patterns above, not confirmed in game, so the columns are labelled Offered When* and Ruled Out When*, the `*` (with a header tooltip) marking the role as our reading. The record fields stay `script_1` / `script_2` by position. Some `mainquest.bss` rows put a requirement in `script_1` with a negation (all of chain 4015, `Descendant of Giants` to `Elric Monastery Report`, has `!clearquest(4001,1);`), which fits "hidden while this holds". `Bridle of Destiny` (4001 / 1), the quest that check names, carries it in its own `script_1` too, so under this reading it and the 4015 chain only show for a character that cleared it before. That looks like an older Mediah opening that newer characters skip. The client Lua (`panel_newquest.luac`, `panel_widget_mainquest.luac`) gets the lists through `ToClient_GetQuestList` and names neither script.

The In-Game Checks below would confirm the roles (client 3458 data).

### Duplicate Quest References

A quest in two groups has a condition line under both group keys, so a quest can be listed by two events (11060 / 1 in the 2019 and 2020 Halloween groups). Whether the game shows both copies at once is not confirmed.

## In-Game Checks

Each check says what the game shows if the script roles in Open Questions are right.

### Branch Ruled Out Once the Other Is Taken

Needs quest (any one):

- [Techthon and Quality Iron](https://bdocodex.com/us/quest/2001/137/)
- [Puia and the Wooden Box Design](https://bdocodex.com/us/quest/2001/138/)

In `recommendationquest.bss`, group `[ADV Support] Inventory Expansion!`, each of the two quests lists the other in `script_1` with `clearQuest` or `progressQuest`. Accept one, and the other should leave the group's list right away, not only after the first is completed.

### Crossroad Ruled Out Once the Other Is Cleared

Needs quest (any one):

- [[Everfrost] [Crossroad] One Game is All Yar Need](https://bdocodex.com/us/quest/7500/81/)
- [[Everfrost] [Crossroad] No Silver, No Meal](https://bdocodex.com/us/quest/7500/82/)

In `mainquest.bss`, group `[Mountain of Eternal Winter] In Search of the Flame that Consumes Gods`, the two quests list only `clearquest` of each other. The other branch should stay listed while the first is in progress and leave once it is completed.

### Hidden Until Cleared

Needs quest: [Bridle of Destiny](https://bdocodex.com/us/quest/4001/1/)

In `mainquest.bss`, group `[Lv. 51 Mediah] Dark Energy that Looms Over Mediah`, `Bridle of Destiny` (4001 / 1) and `Descendant of Giants` to `Elric Monastery Report` (4015 / 1 to 7) carry `!clearquest(4001,1);` in `script_1`. On a character that never did `Bridle of Destiny`, none of them should be listed in the group.

### Offered From a Level

Needs quest: [[Life 101] The Adventurer That Does It All](https://bdocodex.com/us/quest/40055/1/)

In `recommendationquest.bss`, group `[Life 101] The Adventurer That Does It All`, every quest (40055 / 1 to 9) has `getLevel()>59;` in `script_2`. On a level 59 character the group's quests should not be offered; once it reaches level 60 they should.
