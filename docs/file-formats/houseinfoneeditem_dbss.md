# `houseinfoneeditem.dbss` Format

## Purpose

What it costs to set a node house to a use and to raise that use a level.
A row is one need item group, the `need_item_key` that
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) rows point at, with six
level slots: slot 0 is level 0 and holds nothing, slots 1 to 5 hold the
transfer time and the items house levels 1 to 5 take. On client 3474 every
item is Silver.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                        | Row bytes               |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------------------------------ | ----------------------- |
| 1      | 1784 and later | 3474    | `houseinfoneeditem.dbss`       | 1,322 | 66 Level, 42 Need Item, 11 Row | 12 to 24, 20 on average |
| 1      | 1784 and later | 3474    | `houseinfoneeditemoffset.dbss` | 114   | 11 Index Row                   | 10                      |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `houseinfoneeditem.dbss`       | 1,322 B (100.0%) | 0 B (0.0%) |
| 1      | `houseinfoneeditemoffset.dbss` | 114 B (100.0%)   | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                                                   |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------- |
| `houseinfoneeditemoffset.dbss` | Optional | Index `need_item_key -> (offset, size)`, see below; the handler walks the rows in order and does not load it |
| `houseinforeceipe.dbss`        | Optional | The house uses whose `need_item_key` names each group                                  |
| `languagedata_en.loc`          | Optional | LOC type 16 house use names, LOC type 0 item names                                     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes               |
| ------- | -------------- | --------- | ------------------- |
| `+0x00` | u32            | row_count | `11` on client 3474 |
| `+0x04` | Row[row_count] | rows      | See Row             |

The rows run from key 11 down to key 1 (client 3474).

### Row (variable: 2 bytes + levels)

| Offset  | Type     | Field         | Notes                                                    |
| ------- | -------- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16      | need_item_key | Unique row key; `houseinforeceipe.dbss` `need_item_key` |
| `+0x02` | Level[6] | levels        | Slots 0 to 5, see Level                                  |

### Level (variable: 12 bytes + items)

| Offset  | Type                   | Field         | Notes                                                    |
| ------- | ---------------------- | ------------- | -------------------------------------------------------- |
| `+0x00` | i32                    | level         | The slot number, `0` to `5`                              |
| `+0x04` | i32                    | transfer_time | Seconds, see Transfer Time                               |
| `+0x08` | u32                    | item_count    | Number of need items                                     |
| `+0x0C` | Need Item[item_count]  | items         | See Need Item                                            |

Slot 0 holds level `0`, transfer time `0` and no items on every row of
clients 1784 and 3474, so every row is at least 74 bytes (`2 + 6 x 12`).

### Need Item (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item enchant key, see Notes; `1` (Silver, LOC type 0) on every item (client 3474) |
| `+0x04` | i64  | count    | Number of that item                                         |

No level holds more than one item on client 3474.

### `houseinfoneeditemoffset.dbss`

| Offset  | Type                 | Field     | Notes                                                    |
| ------- | -------------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count`; `11` on client 3474 |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                                            |

Every index row points at the main row with the same key, in the main
file's order, and the rows tile the main file from `0x04` to the end with
no gap.

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | need_item_key | The main row's `need_item_key`                               |
| `+0x02` | u32  | offset        | Start of the row in `houseinfoneeditem.dbss`, at its `need_item_key` |
| `+0x06` | u32  | size          | Full row length, key included                                |

## Costs

The Silver each level takes (client 3474). A dash is a level with no items.
The [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md#need-item-join) Need
Item Join lists the house uses of each group.

| need_item_key | Lv 1  | Lv 2      | Lv 3   | Lv 4   | Lv 5    |
| ------------- | ----- | --------- | ------ | ------ | ------- |
| 1             | 500   | 1,000     | 2,500  | 5,000  | 10,000  |
| 2             | 2,000 | 3,500     | 7,000  | 10,000 | 15,000  |
| 3             | -     | -         | -      | -      | -       |
| 4             | -     | 1,000     | 3,000  | 7,000  | 15,000  |
| 5             | 2,000 | 1,000,000 | -      | -      | -       |
| 6             | 500   | 10,000    | 30,000 | -      | -       |
| 7             | 5,000 | 25,000    | 45,000 | 70,000 | 100,000 |
| 8             | 3,000 | 6,000     | 10,000 | 15,000 | 25,000  |
| 9             | 5,000 | 15,000    | 25,000 | 35,000 | -       |
| 10            | 1,000 | 3,000     | 7,000  | 18,000 | -       |
| 11            | 1,000 | 2,500     | 5,000  | 10,000 | 20,000  |

## Transfer Time

`transfer_time` is `5` on every priced level from 2 up and `0` on level 1
and on every level with no items (client 3474). On client 1784 it is `60`
times the level (`60` to `300`), `600` on group 5 level 2, `60` on the
empty level 1 of group 4, and `0` on group 3 and on the levels past the
last one groups 5, 6, 9 and 10 price. The house window reads it with
`getTransperTime(receipeKey, fromLevel, toLevel)`, names it `needTime_sec`
and passes it to `Util.Time.timeFormatting`; at `0` it shows `--`
(`panel_new_housecontrol.lua`). So the field is seconds, and a level change
on client 3474 takes 5 seconds. That matches the live game, where a level
change takes a few seconds; on older clients it took longer, as the 1784
values show.

## Field Names

The names follow the 2016 `gc::HouseInfoNeedItemStaticStatus`: `_key`
(u16), then `pa::Array<gc::HouseInfoNeedItemLevelGroup,6> _houseInfoList`.
A `HouseInfoNeedItemLevelGroup` is `int _level`, `int _transferTime` and a
vector of `gc::ItemStaticInformation`, whose `_key` is a
`gc::ItemEnchantKey` and `_count` an `__int64`. The six-slot array is why a
row holds slot 0.

The values match the `House_Transfer_New` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `TransferKey` and `Level`:

| Field         | Column                     | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------- | ------------------------ | ------------------------ |
| need_item_key | `TransferKey`              | 11 of 11 keys            | 11 of 11 keys            |
| level         | `Level`                    | 55 of 55 levels          | 55 of 55 levels          |
| transfer_time | `Time`                     | 55 of 55                 | 12 of 55                 |
| items         | `Itemkey1` to `ItemCount3` | 55 of 55                 | 55 of 55                 |

The sheet has no level 0 row; slot 0 is not compiled from it. Client 3474
sets the time to `0` or `5` (see Transfer Time); the 12 levels that still
match are the ones at `0` on both clients. The sheet holds three item
columns per level and fills only the first; the file counts its items.
The `ReceipeForTown_New` sheet of the same workbook names the
`houseinforeceipe.dbss` `need_item_key` column `TransferKey`: Residence
`3`, Lodging `1`, Storage `4` and Horse Ranch `1`, as on client 3474.

## Notes

- The house window asks for the items by receipe key and level
  (`getNeedItemListCount`, `getNeedItemListItemKey`,
  `getNeedItemListItemCount` in `panel_new_housecontrol.lua`), so the client
  goes from the receipe to its `need_item_key` row. It passes each item key
  to `getItemEnchantStaticStatus`, which takes an item enchant key
  (`enchant_level << 24 | item_id`, the packing `itemenchant.dbss` uses).
- `getNeedAllItemListCount(receipeKey, fromLevel, toLevel)` and the
  `fromLevel, toLevel` pair of `getTransperTime` read a range of levels, for
  a house raised several levels at once.
- Group 9 is the one no `houseinforeceipe.dbss` row names (client 3474).
- The level 2 price of group 5 (1,000,000 Silver) is the same on clients
  1784 and 3474.
- The offset file is the same 114 bytes on clients 1784 and 3474.
