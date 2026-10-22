# `marblegamediceitemgroup.dbss` Format

## Purpose

The Black Spirit's Adventure dice drop groups: per group key the
[`marblegamediceitemkey.dbss`](marblegamediceitemkey_dbss.md) dice items it
drops. An item whose contents event is `98` grants one group (see Granting
Items). The file holds 44 groups with 55 entries on client 3482, 27 groups
with 38 entries on client 1784. Companion
`marblegamediceitemgroupoffset.dbss` lists where every group sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ---------------- | --------- |
| 1      | 1485 and later | 3482    | `marblegamediceitemgroup.dbss`       | 796   | 55 Entry, 44 Row | 8         |
| 1      | 1485 and later | 3482    | `marblegamediceitemgroupoffset.dbss` | 532   | 44 Offset Row    | 12        |

| Layout | File                                 | Known          | Unknown    |
| ------ | ------------------------------------ | -------------- | ---------- |
| 1      | `marblegamediceitemgroup.dbss`       | 796 B (100.0%) | 0 B (0.0%) |
| 1      | `marblegamediceitemgroupoffset.dbss` | 532 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                 | Required | Role                                                                          |
| ------------------------------------ | -------- | ----------------------------------------------------------------------------- |
| `marblegamediceitemgroupoffset.dbss` | Optional | `dice_drop_group_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `itemenchant.dbss`                   | Optional | The items that grant each group; the handler reads them from the `MARBLE_DICE_GROUP_ITEMS` lookup index, not as a companion |
| `languagedata_en.loc`                | Optional | Item names (type 0)                                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes            |
| ------- | ---------- | ----- | ---------------- |
| `+0x00` | u32        | count | Number of groups |
| `+0x04` | Row[count] | rows  | See Row          |

On client 3482 the file is 4 + 44 x 8 + 55 x 8 = 796 bytes.

### Row (variable: 8 bytes + entries)

| Offset  | Type               | Field               | Notes                                                    |
| ------- | ------------------ | ------------------- | -------------------------------------------------------- |
| `+0x00` | u32                | dice_drop_group_key | Row key; each key once                                   |
| `+0x04` | u32                | entry_count         | Number of `entries`; `1` on every group but `8` (7) and `9` (6), clients 1784 and 3482 |
| `+0x08` | Entry[entry_count] | entries             | See Entry                                                |

### Entry (8 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | dice_item_key | A `marblegamediceitemkey.dbss` key                                 |
| `+0x04` | u32  | rate          | `0` on every entry of clients 1784 and 3482, see Field Names       |

### `marblegamediceitemgroupoffset.dbss`

Bare offset table into `marblegamediceitemgroup.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                          |
| ------- | ----------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32               | count | Equals the `marblegamediceitemgroup.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                 |

### Offset Row (12 bytes)

| Offset  | Type | Field               | Notes                                   |
| ------- | ---- | ------------------- | --------------------------------------- |
| `+0x00` | u32  | dice_drop_group_key | Key of the row it points at             |
| `+0x04` | u32  | data_offset         | Row start, at `dice_drop_group_key`     |
| `+0x08` | u32  | data_size           | The whole row: `8 + 8 * entry_count`    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Groups

On client 3482 the groups hold:

| Groups           | Dice item keys                   |
| ---------------- | -------------------------------- |
| `1` to `7`       | The key of the same number       |
| `8`              | `1` to `7`                       |
| `9`              | `2` to `7`                       |
| `10`             | `8`                              |
| `11` to `31`     | The key of the same number       |
| `1001` to `1006` | `101` to `106`                   |
| `1007` to `1009` | `301` to `303`                   |
| `1010` to `1013` | `401`, `601`, `701`, `801`       |

Groups `1` to `14` and `1001` to `1013` are the 27 groups of client 1784;
`15` to `31` are new on client 3482.

## Granting Items

An item with contents event `98` in
[`itemenchant.dbss`](itemenchant_dbss.md) names a group in
`contents_event_param1`. On client 3482, 42 base items have the event and
each names a group key of this file. Groups `9`, `10` and `1001` to `1013`
are not dice item keys, so the parameter is the group key and not the dice
item key: Black Spirit's Dice `756438` grants group `9`, `756437` group
`10`, and Pace of Delight - 1 Square `756440` group `1001`. Groups `8`,
`18` and `19` have no item on client 3482. The `MARBLE_DICE_GROUP_ITEMS`
lookup index (`build_marble_dice_group_item_index()` in
`_dbss/itemenchant/parser.py`) maps each group to its items, and the view
shows them in the Items column.

## Field Names

The `DiceItemGroup_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `DiceDropGroupKey`, `DiceItemKey` and `Rate`,
one sheet row per entry. Its 38 rows are the 38 entries of the client 1784
file (27 groups), and all 38 are in the client 3482 file. In the `.xlsm`
copy of the sheet (`datasheet_itemdatatable_marblegamedice.xlsm`) the
column is `%Rate`, server-only, which the client build writes as `0`; the
sheet's rates are parts of 1,000,000 (group `8`: `940000` on die `1`,
`10000` on each of `2` to `7`). Its note column `#Desc` is not compiled.
The count in front of the entries has no sheet column; the file groups the
sheet rows by key, so it is `entry_count`.

## Notes

- No client Lua reads the table; Black Spirit's Adventure runs in a web
  control (see [`marblegamediceitemkey.dbss`](marblegamediceitemkey_dbss.md)).
- The view shows one row per group: its key, the items that grant it and its
  dice item keys, each a link to its `marblegamediceitemkey.dbss` row.

## Open Questions

### Groups Without an Item

Groups `8` (die `1` at 94% and the one-face dice `2` to `7` at 1% each, by
the client 1784 sheet), `18` and `19` are granted by no item on client
3482. Whether the web side draws them for the board's free rolls is open.
