# `itemviewstackenchantgroupss.bss` Format

## Purpose

Groups of [`enchantstaticstatus.dbss`](enchantstaticstatus_dbss.md) enchant
keys. Each row is one enchant key with the full list of keys in its group,
itself included, so every key of a group has its own row with the same list.
A group is one item family across equipment types: the Liverto Longsword,
Longbow, Amulet and Axe keys (57, 257, 457, 657) form one group, the Kzarka
ones (62, 262, 462, 662) another. Every key of a group enhances with the same
success chance, material and failure result at each level (see Groups).

The Another Adventurer's Choice window beside the enhancement window counts
the failstacks other players used per group: every key of a group shows the
same ranges, and keys of different groups show different ones. Its button
shows only for keys in this file (both checked in game on client 3474, see
Another Adventurer's Choice).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes   | Records   | Row bytes                 |
| ------ | -------------- | ------- | --------------------------------- | ------- | --------- | ------------------------- |
| 1      | 3473 and later | 3474    | `itemviewstackenchantgroupss.bss` | 192,732 | 1,146 Row | 20 to 628, 168 on average |

| Layout | File                              | Known             | Unknown        |
| ------ | --------------------------------- | ----------------- | -------------- |
| 1      | `itemviewstackenchantgroupss.bss` | 188,148 B (97.6%) | 4,584 B (2.4%) |

<!-- versions:end -->

## Companion Files

None. The handler names the items of each enchant key through the
`ENCHANT_KEY_ITEMS` lookup index (see `docs/handler.md`), built from
[`itemenchant.dbss`](itemenchant_dbss.md), and LOC type 0 for the item names.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows; 1,146 on client 3473  |
| `+0x04` | Row[count] | rows  | See Row                               |

The rows are not sorted by key: client 3473 opens with keys 1143, 3046 and
25815.

### Row (variable: 16 bytes + group keys)

| Offset  | Type             | Field              | Notes                                                                              |
| ------- | ---------------- | ------------------ | ---------------------------------------------------------------------------------- |
| `+0x00` | u32              | enchant_key        | `enchantstaticstatus.dbss` enchant key; unique                                     |
| `+0x04` | u32              | unknown_04         | Equals `group_count` on all 1,146 rows (client 3473)                               |
| `+0x08` | u64              | group_count        | Number of `group_enchant_keys`; 1 to 153 on client 3473                            |
| `+0x10` | u32[group_count] | group_enchant_keys | Every enchant key of the group, `enchant_key` included                             |

`group_enchant_keys` is in ascending order on 1,084 of the 1,146 rows (client
3473); the others keep an order of their own, the same on every row of the
group (29787, 29784, 29781, 29778, ... and 684, 484, 284, 84).

## Groups

Counted on client 3473:

| Check                                                                 | Result                 |
| --------------------------------------------------------------------- | ---------------------- |
| `enchant_key` found as an `enchantstaticstatus.dbss` enchant key       | 1,146 of 1,146 rows    |
| `enchant_key` stored by an `itemenchant.dbss` base item               | 1,036 of 1,146 rows    |
| Group keys without a row of their own                                 | 0                      |
| Rows whose list differs from the lists of its group keys             | 0                      |
| Groups (distinct lists)                                               | 280, 166 of one key    |
| Groups of two or more keys with the same success chance, material, material count, failure result and downgrade chance at each level | 114 of 114 |
| Of those, with the same max durability at each level                  | 103 of 114             |

Equal enhancement data does not make two keys one group: 18 groups share
their data with another group (the four Blackstar armor groups, each a piece
with its Obsidian version; the Fiery Sovereign two-handed weapons and the
Fiery Sovereign main weapons), and 166 enhanceable keys outside the file
have the same data as a group. Of the 602 enhanceable keys outside the file
that an item stores, 410 hold an item with the name of an item in the file,
such as the `Kzarka Longsword` of key 3222 (items 734408 and 734422) next to
the Kzarka group of key 62.

## Another Adventurer's Choice

The window is `panel_otheruser_additionalrate_all.luac` with
`panel_window_otheruser_additionalrate_all.xml`. It lists the failstack
ranges other players used, five stacks wide
(`ToClient_GetOthersChoiceStackByIndex(i) * 5`), with a percentage each
(`ToClient_GetOthersChoicePercentByIndex(i)`), under "The most frequently
attempted Enhancement Chance for this gear by other Adventurers". The ranges
come from the server (`ToClient_RequestOthersChoice()`); no Lua names this
file, so the link rests on the in-game readings below.

The enhancement window shows the window's button when the exe check
`ToClient_CanShowOthersChoice()` is true (`panel_widget_enchant_main_all_1.luac`),
and hides it for gear that can change to Tuvala or a guaranteed enhancement.
On client 3474 the button showed for every key of this file opened below and
not for a PRI: Tati Godr Sphera (item 14813, key `2103`), a marketable
awakening weapon that enhances to +20 and whose key is not in the file.

On client 3474 the window showed these ranges, each pair read a few minutes
apart at the same enhancement level.

All five at +14:

| Range     | Rosar Longsword (`52`) | Bares Staff (`437`) | Grunil Helmet (`5164`) | Agerian Gloves (`5066`) | Akum Helmet (`5281`) |
| --------- | ---------------------- | ------------------- | ---------------------- | ----------------------- | -------------------- |
| +0 ~ +4   | 22%                    | 22%                 | 24%                    | 24%                     | 17%                  |
| +5 ~ +9   | 20%                    | 20%                 | 28%                    | 28%                     | 19%                  |
| +10 ~ +14 | 16%                    | 16%                 | 16%                    | 16%                     | 15%                  |
| +15 ~ +19 | 15%                    | 15%                 | 10%                    | 10%                     | 13%                  |
| +20 ~ +24 | 6%                     | 6%                  | 6%                     | 6%                      | 9%                   |

Both at PEN:

| Range       | PEN: Sovereign Staff (`3677`) | PEN: Fiery Sovereign Godr Sphera (`3683`) |
| ----------- | ----------------------------- | ----------------------------------------- |
| +265 ~ +269 | 9%                            | 9%                                        |
| +260 ~ +264 | 8%                            | 8%                                        |
| +270 ~ +274 | 6%                            | 7%                                        |
| +225 ~ +229 | 5%                            | 5%                                        |
| +220 ~ +224 | 5%                            | 5%                                        |

At PRI:

| Range     | PRI: Red Coral Ring (`9018`) | PRI: Blue Coral Ring (`9017`) |
| --------- | ---------------------------- | ----------------------------- |
| +30 ~ +34 | 59%                          | 61%                           |
| +35 ~ +39 | 14%                          | 13%                           |
| +40 ~ +44 | 12%                          | 13%                           |
| +25 ~ +29 | 3%                           | 2%                            |
| +20 ~ +24 | 2%                           | 2%                            |

| Items                                        | Same group | Same slot | Same grade | Ranges    |
| -------------------------------------------- | ---------- | --------- | ---------- | --------- |
| Rosar Longsword, Bares Staff                 | yes        | no        | yes        | same      |
| Grunil Helmet, Agerian Gloves                | yes        | no        | yes        | same      |
| Rosar Longsword, Grunil Helmet               | no         | no        | yes        | different |
| Grunil Helmet, Akum Helmet                   | no         | yes       | no         | different |
| Red Coral Ring, Blue Coral Ring              | no         | yes       | yes        | different |
| Sovereign Staff, Fiery Sovereign Godr Sphera | no         | no        | yes        | different |

Rosar, Bares, Grunil and Agerian are grade `1`, Akum and both coral rings
grade `2` (`itemenchant.dbss`). Items of one group give the same ranges
across weapon types and armor slots, and the two coral rings differ although
slot and grade match, so neither slot nor grade decides the count.

## Notes

- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `itemviewstackenchantgroupss.bss`. No client Lua script names the file or
  its rows. The field names come from the join with
  `enchantstaticstatus.dbss` and the counts in the table above.
- Read as item IDs, the group keys name unrelated items (key 10 is Crow
  Coin, 12 and 16 Pure Black Stone, 21 Bartali Gold Bar in one group); as
  enchant keys the same group is the Rusty, Elsh and Azwell longswords.

## Open Questions

### Second Group Count at +0x04

`unknown_04` equals `group_count` on all 1,146 rows (client 3473). Why the
row stores the count twice, once as u32 and once as u64, is unknown.
