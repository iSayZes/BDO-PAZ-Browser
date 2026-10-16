# `itemmaingroup.bss` Format

## Purpose

Item main groups: each group lists one or more [`itemsubgroup.dbss`](itemsubgroup_dbss.md) subgroups, each with an optional condition script. [`characterfunction.dbss`](characterfunction_dbss.md) points its shop, sell, guild shop and trade fields here, so a group is the item list an NPC window shows. The plain PABR file holds the groups, then a string table of the condition scripts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                    | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | -------------------------- | --------- |
| 1      | 3473 and later | 3473    | `itemmaingroup.bss` | 680,658 | 18,960 Entry, 16,555 Group | 10        |

| Layout | File                | Known             | Unknown           |
| ------ | ------------------- | ----------------- | ----------------- |
| 1      | `itemmaingroup.bss` | 339,938 B (49.9%) | 340,720 B (50.1%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `itemsubgroup.dbss`       | Required | The items of each subgroup                                |
| `itemsubgroupoffset.dbss` | Required | Index into `itemsubgroup.dbss`                            |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field              | Notes                                                        |
| ------------------- | ------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]       | magic              | ASCII `PABR`                                                 |
| `+0x04`             | u32           | count              | Number of groups; `16,501` on client 3464                    |
| `+0x08`             | Group[count]  | groups             | Variable-size groups, back to back; see Group                |
| `groups+0x00`       | String Table  | string_table       | See String Table                                             |
| `string_table+0x00` | u32           | string_table_start | Offset of `string_count`, where the groups end               |
| `string_table+0x04` | u32           | zero               | Always `0`                                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is wide (UTF-16LE). Walking `count` groups ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

### Group (variable: 29 bytes + entries)

| Offset  | Type               | Field              | Notes                                                                      |
| ------- | ------------------ | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | group_id           | Unique; `1,309` to `65,535`, not in key order                              |
| `+0x04` | u8                 | do_select_only_one | `1` when the group hands out one of its subgroups; `0` on 11,926 groups, `1` on 4,575 (client 3464) |
| `+0x05` | bytes[8]           | unknown_05         | Always zero; the 2016 `_pickCount` (i64) slot, see Field Names             |
| `+0x0D` | i32                | refresh_start_hour | `-1`, or `0` on group 50452 only (client 3464)                             |
| `+0x11` | bytes[8]           | unknown_11         | Always zero; the 2016 `_refreshInterval` (u64) slot, see Field Names       |
| `+0x19` | u32                | entry_count        | `1` to `4`; never `0` on client 3464                                       |
| `+0x1D` | Entry[entry_count] | entries            | See Entry                                                                  |

### Entry (10 bytes)

| Offset  | Type | Field         | Notes                                                               |
| ------- | ---- | ------------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00    | Always `0`; the 2016 `_selectRate` slot, see Field Names            |
| `+0x04` | u32  | condition_ref | Index into the string table; string `0` is empty (no condition)     |
| `+0x08` | u16  | subgroup_key  | `itemsubgroup.dbss` subgroup key; every key is in its offset index  |

On client 3464 the 16,501 groups hold 18,906 entries: 15,608 groups have one entry, 121 two, 32 three and 740 four. 15,072 of the one-entry groups list the subgroup with their own key (group 50503 lists subgroup 50503).

The conditions use the script calls of `characterfunction.dbss` conditions (`getIntimacy`, `getLevel`, `clearQuest`, `checkexplore`, `isContentsGroupOpen`), joined with `;` and alternatives split by `<or>`. On client 3464, 16,422 entries have no condition, 2,140 have the text `0`, and 118 have `checkexplore(103, 1)`, node 103 being Bahar Investment Bank.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                   |
| ------- | ------------------ | ------------ | --------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `197` on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Every string here is wide (UTF-16LE)    |

## Notes

- `characterfunction.dbss` stores five group IDs per NPC: `shop_buy_group`, `shop_sell_group`, `guild_shop_buy_group`, `guild_shop_sell_group` and `trade_group`. All 884, 743, 63, 61 and 125 non-zero values on client 3464 are group IDs here; that doc names the fields.
- The trade groups are the 62 IDs from 54002 to 54146 (client 3464). Each has one entry: subgroup 54001 (item 55151, the only subgroup besides 55000 that sets the trade price fields in `itemsubgroup.dbss`) under `checkexplore(103, 1)`. Subgroup 55000 (the trade crates) is in no group.
- A group can list one subgroup more than once: group 57996 lists 57771, then 57357 three times with the condition `0`.
- Worker production reaches groups through item exchanges: in the 2016 client a `plantexchangegroup.bss` row lists item exchange keys, and each `gc::ItemExchangeSourceStaticStatus` points at two groups here, `_productItemDropKey` (the product) and `_npcWorkerDropKeyForLuck` (the luck drop). `plantexchangegroup.bss` keeps the exchange key where earlier docs read a subgroup key; see [its Field Names](plantexchangegroup_bss.md#field-names). Group IDs 44059 and 44060 (Tungrad Ruins excavation) point at subgroups 42339 and 42340 (Trace of Nature with a Rough Translucent or Rough Blue Crystal), which is why those two zones resolve here and not in `itemsubgroup.dbss`.
- On client 3464, 4 of the 893 groups with more than one entry set `do_select_only_one`; the other 4,571 are one-entry groups.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ItemMainGroupStaticStatus` holds `_key`, the entry list, `_doSelectOnlyOne` (bool), `_pickCount` (i64), `_refreshStartHour` (i32) and `_refreshInterval` (u64); each entry (`value_type`) holds `_selectRate` (i32), `_conditionString`, a parsed condition list and `_itemSubGroupKey` (u16). The file stores the scalars in that order between `group_id` and `entry_count`, with the list moved to the end, and the entry stores `_selectRate`, the condition string index and `_itemSubGroupKey` in that order. The server-side `ItemMainGroup_Table` of a private server on client 519 shares 6,168 group IDs with client 3464:

| Field              | `ItemMainGroup_Table` column | Matching groups                                    |
| ------------------ | ---------------------------- | -------------------------------------------------- |
| do_select_only_one | `DoSelectOnlyOne`            | 5,703 of 6,168; see below                          |
| refresh_start_hour | `RefreshStartHour`           | `-1` on both sides for every shared group but 50452, the one group set on both (server `12`, client `0`) |
| subgroup_key       | `ItemSubGroupKey0` to `3`    | 6,296 of 7,802 entries                             |

The 465 `do_select_only_one` mismatches sit in key bands: 357 groups the server has at `0` and the client at `1` (1347 to 64037), and 108 the other way, all from 46001 up (46001 to 46015 and on, 65021, 65213 to 65219). 455 of them list the same subgroups on both sides; I read them as flags changed by patches since the server data.

`unknown_05`, `unknown_11` and the entry `unknown_00` sit where the 2016 struct has `_pickCount`, `_refreshInterval` and `_selectRate`, but they keep their offsets: the client stores `0` on every group and entry, while the server sets `SelectRate0` to `1,000,000` on 10,745 of its 11,098 groups and `RefreshInterval` to `-1` on 9,274. The selection weights of a `do_select_only_one` group are not in the client file.

## Open Questions

### Condition `0`

2,140 entries carry the condition text `0` (client 3464), often on the second to fourth entry of a group that repeats one subgroup. It may be a script that never passes, which would turn the entry off, but no client code that evaluates these conditions has been found.

### `refresh_start_hour` on Group 50452

`refresh_start_hour` is `-1` on every group but 50452, a furniture list (Four-legged Dining Table and five more) where it is `0`. The server sets `RefreshStartHour` and `RefreshInterval` to `12` on the same group, so it is a list that refreshes on a timer, but the client keeps no interval (`unknown_11` is zero). What the client does with the start hour alone is open.
