# `itemequipgroup.bss` Format

## Purpose

Equipment groups: each group key lists the item IDs of one kind of gear across its variants (group 11 holds the Tuvala main weapons of every class, group 14 the Kzarka main weapons). Quest and dialog conditions test a group with `checkequipitemgroup(group, min_level, max_level)` and `checkinventoryitemgroup(group, min_level, max_level)`, so one condition covers every class's version of a weapon. The plain PABR file holds the groups, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records  | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | -------- | ----------------------- |
| 1      | 1784 and later | 3474    | `itemequipgroup.bss` | 5,784 | 61 Group | 8 to 176, 94 on average |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 1      | `itemequipgroup.bss` | 5,784 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                    |
| --------------------- | -------- | --------------------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0 at `str_id1=item_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                                    |
| ------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                             |
| `+0x04`             | u32          | count              | Number of groups                                         |
| `+0x08`             | Group[count] | groups             | Variable-size groups, back to back; see Group            |
| `groups+0x00`       | String Table | string_table       | See String Table                                         |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the groups end           |
| `string_table+0x04` | u32          | zero               | Always `0`                                               |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` groups ends exactly at `string_table_start`.

### Group (variable: 8 bytes + items)

| Offset  | Type             | Field         | Notes                                                                 |
| ------- | ---------------- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16              | group_key     | Unique; the first argument of `checkequipitemgroup` and `checkinventoryitemgroup` |
| `+0x02` | u16              | group_key_dup | Equal to `group_key` in every group                                   |
| `+0x04` | u32              | item_count    | Number of items; `0` on three groups (client 3474)                     |
| `+0x08` | u32[item_count]  | item_ids      | Item IDs, LOC type 0 `str_id1`; no enhancement level packed in        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No group reads a string              |

## Conditions

`quest.dbss` (`condition_script`) and `detail_dialog.dbss` call two script functions with a group key here, the lowest enhancement level and the highest:

| Call                                       | Example                                   |
| ------------------------------------------ | ----------------------------------------- |
| `checkequipitemgroup(group, min, max)`     | `checkequipitemgroup(11,20,20)`           |
| `checkinventoryitemgroup(group, min, max)` | `checkinventoryitemgroup(11,20,20)`       |

On client 3474, `quest.dbss` holds 34 `checkequipitemgroup` and 21 `checkinventoryitemgroup` calls, and `detail_dialog.dbss` 25 and 21. Every group key they name is in the file. The Old Moon's Resplendent weapon quests (chains 41009 to 41011) test both calls with one group: quest 41009 / 1 `Old Moon's Resplendent Main Weapon: Tuvala` checks group 11 at level 20, quest 41009 / 4 `Old Moon's Resplendent Main Weapon: Kzarka` group 14 at level 19. Quest 9110 / 20 `[Edana's Defense Gear] Godslayer of Legend` checks groups 56 to 59 (one Edana armor piece each) at levels 0 to 10, and the dialogs check groups 41 to 43 (Tuvala main weapons, sub-weapons and armor) at levels 16 to 20.

## Field Names

The `Item_Group` sheet of a private server's `DataSheets.bexcel` on client 1784 has two columns: `Group_Index` (`group_key`) and `Item_Index` (`item_ids`, as one comma-separated list). The same server's compiled `itemequipgroup.bss` matches the sheet in all 43 groups, item for item. Against the client 1784 file, 42 of 43 groups match; group 47 is empty in the client and lists 15 items in the sheet. The server executable of that private server names the loader `loadEquipGroupInformation`, the record type `ItemEquipGroupStaticStatus` (keyed by a u16 `KeyType`) with its list `_itemList`, and the script arguments `EquipGroupKey`, `minEnchantLevel` and `maxEnchantLevel`.

On client 3474, 2 of the 43 shared groups (4 and 5) still match the sheet item for item. 24 start with the sheet's list in its order and append newer gear (groups 1 to 3 gained 731628 and 731631, 731728 and 731731, 731828 and 731831). The other 17 were refilled with other items (groups 41 and 42 moved from the 694xxx to the 695xxx Tuvala weapons) or emptied (6 and 8). Groups 53 to 70 are newer than the sheet.

## Notes

- On client 3474 the file is `5,784` bytes: 61 groups with keys 1 to 23 and 33 to 70, 1,319 items, 1,189 distinct. Groups 6, 8 and 53 are empty.
- The groups are not in key order (70, 69, 68, ..., 64, 47, 46, ...).
- An item can sit in more than one group (81 items on client 3474), and groups 21, 44 and 67 list one item twice.
- No client 3474 Lua file (`luacscript/`) calls either function or names the file. The only Lua text with `EquipItemGroup` in it is the drop window control `Static_EquipableDropItemGroup` (`panel_window_renewdropitem_all_1.luac`), which lists a monster's equipment drops.
- Client 1784 has the same layout: `3,400` bytes, 43 groups with keys 1 to 23 and 33 to 52.
