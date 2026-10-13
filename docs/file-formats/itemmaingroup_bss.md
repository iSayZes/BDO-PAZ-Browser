# `itemmaingroup.bss` Format

## Purpose

Item main groups: each group lists one or more [`itemsubgroup.dbss`](itemsubgroup_dbss.md) subgroups, each with an optional condition script. [`characterfunction.dbss`](characterfunction_dbss.md) points its shop, sell, guild shop and trade fields here, so a group is the item list an NPC window shows. The plain PABR file holds the groups, then a string table of the condition scripts.

```text
group 50503 -> subgroup 50503 -> HP Potion (Medium), HP Potion (Large), ...   Benyamin's Shop
group 52001 -> subgroup 52001 -> 11,556 items                                   Shop (Sell) of 683 NPCs
group 54146 -> subgroup 54001 if checkexplore(103, 1)                           Isobelle Encarotia's Trade
```

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `itemsubgroup.dbss`       | Required | The items of each subgroup                                |
| `itemsubgroupoffset.dbss` | Required | Index into `itemsubgroup.dbss`                            |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`               |

All multi-byte values are little-endian.

## File Layout

| Offset   | Type    | Field              | Notes                                                        |
| -------- | ------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`  | char[4] | magic              | ASCII `PABR`                                                 |
| `+0x04`  | u32     | count              | Number of groups; `16,501` on client 3464                    |
| `+0x08`  | group[] | groups             | Variable-size groups, back to back                           |
| ...      | u32     | string_count       | Number of strings; `197` on client 3464                      |
| ...      | entry[] | strings            | `u8 is_wide`, `u32 byte_length`, then the text               |
| EOF - 8  | u32     | string_table_start | Offset of `string_count`, where the groups end               |
| EOF - 4  | u32     | reserved           | Always `0`                                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is wide (UTF-16LE). Walking `count` groups ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

## Record Structure

### Group (`29 + 10 * entry_count` bytes)

| Offset  | Type    | Field       | Notes                                                                      |
| ------- | ------- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32     | group_id    | Unique; `1,309` to `65,535`, not in key order                              |
| `+0x04` | u8      | unknown_04  | `0` on 11,926 groups, `1` on 4,575 (client 3464)                           |
| `+0x05` | u8[8]   | unknown_05  | Always zero                                                                |
| `+0x0D` | i32     | unknown_0d  | `-1`, or `0` on group 50452 only (client 3464)                             |
| `+0x11` | u8[8]   | unknown_11  | Always zero                                                                |
| `+0x19` | u32     | entry_count | `1` to `4`; never `0` on client 3464                                       |
| `+0x1D` | entry[] | entries     | 10-byte entries repeated `entry_count` times                               |

### Entry (10 bytes)

| Offset  | Type | Field         | Notes                                                               |
| ------- | ---- | ------------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00    | Always `0`                                                          |
| `+0x04` | u32  | condition_ref | Index into the string table; string `0` is empty (no condition)     |
| `+0x08` | u16  | subgroup_key  | `itemsubgroup.dbss` subgroup key; every key is in its offset index  |

On client 3464 the 16,501 groups hold 18,906 entries: 15,608 groups have one entry, 121 two, 32 three and 740 four. 15,072 of the one-entry groups list the subgroup with their own key (group 50503 lists subgroup 50503).

The conditions use the script calls of `characterfunction.dbss` conditions (`getIntimacy`, `getLevel`, `clearQuest`, `checkexplore`, `isContentsGroupOpen`), joined with `;` and alternatives split by `<or>`. On client 3464, 16,422 entries have no condition, 2,140 have the text `0`, and 118 have `checkexplore(103, 1)`, node 103 being Bahar Investment Bank.

## Suggested UI Layout

| Column     | Type | Notes                                                                                      |
| ---------- | ---- | ------------------------------------------------------------------------------------------ |
| Group ID   | num  | `group_id`                                                                                 |
| Subgroups  | text | Each `subgroup_key` as a link to its `itemsubgroup.dbss` row, then `: condition` when set   |
| Items      | num  | Number of items over the group's distinct subgroups                                         |
| Item Names | text | Items of the distinct subgroups in entry order, the first eight shown, as in `itemsubgroup.dbss` |

## Notes

- `characterfunction.dbss` stores five group IDs per NPC: `shop_buy_group`, `shop_sell_group`, `guild_shop_buy_group`, `guild_shop_sell_group` and `trade_group`. All 884, 743, 63, 61 and 125 non-zero values on client 3464 are group IDs here; that doc names the fields.
- The trade groups are the 62 IDs from 54002 to 54146 (client 3464). Each has one entry: subgroup 54001 (item 55151, the only subgroup besides 55000 that sets the trade price fields in `itemsubgroup.dbss`) under `checkexplore(103, 1)`. Subgroup 55000 (the trade crates) is in no group.
- A group can list one subgroup more than once: group 57996 lists 57771, then 57357 three times with the condition `0`.
- Group IDs 44059 and 44060 point at subgroups 42339 and 42340 (Trace of Nature with a Rough Translucent or Rough Blue Crystal). `plantzone.dbss` zones reach 44059 and 44060 as subgroup keys that `itemsubgroup.dbss` lacks.

## Open Questions

### Row Flag `unknown_04`

`unknown_04` is `1` on 4,575 groups and `0` on the rest (client 3464). It does not follow the entry count or the subgroup size: both values occur on one-entry groups and on groups whose subgroups list many items. By group ID it is `1` on 3,115 of the 3,828 groups below 10000 and on 1,460 of the 12,673 from 10000 up. Most groups belong to tables not decoded yet (drops, boxes), so what it switches is open.

### Condition `0`

2,140 entries carry the condition text `0` (client 3464), often on the second to fourth entry of a group that repeats one subgroup. It may be a script that never passes, which would turn the entry off, but no client code that evaluates these conditions has been found.

### `unknown_0d`

`unknown_0d` is `-1` on every group but 50452, a furniture list (Four-legged Dining Table and five more) where it is `0`. What the value selects is open.
