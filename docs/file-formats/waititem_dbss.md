# `waititem.dbss` Format

## Purpose

The item keys (item plus enhancement level) that the Central Market puts in
its Registration Queue before they appear for sale: PEN Blackstar and boss
gear, TRI to PEN Godr-Ayed weapons, TET and PEN accessories, and every level
of Fallen God's Armor.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `waititem.dbss`       | 5,580 | 328 Row       | 17        |
| 1      | 1784 and later | 3474    | `waititemoffset.dbss` | 3,940 | 328 Index Row | 12        |

| Layout | File                  | Known            | Unknown         |
| ------ | --------------------- | ---------------- | --------------- |
| 1      | `waititem.dbss`       | 4,268 B (76.5%)  | 1,312 B (23.5%) |
| 1      | `waititemoffset.dbss` | 3,940 B (100.0%) | 0 B (0.0%)      |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`waititemoffset.dbss` (see below). Item names come from LOC type 0 and 79,
icons from the `ITEM_KEY` and `ITEM_ICON` lookup indexes.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then 17-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `328` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (17 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | key           | Row key; equals `item_key` on every row                      |
| `+0x04` | u32  | item_key      | `enchant_level << 24 \| item_id`, the packed key of `_common/item_key.py` |
| `+0x08` | u32  | item_id       | The low 24 bits of `item_key`                                |
| `+0x0C` | u8   | enchant_level | The top byte of `item_key`                                   |
| `+0x0D` | u32  | unknown_0d    | `900` on every row (client 3464); see Open Questions         |

On client 3464 the 328 rows hold 184 items:

| Levels        | Items | Examples                                                                   |
| ------------- | ----- | -------------------------------------------------------------------------- |
| `20`          | 89    | Blackstar weapons and armor, boss armor, Manos tools and clothes (735001 Blackstar Shield, 11013 Giath's Helmet, 16479 Manos Hoe, 705517 Manos Gatherer's Clothes) |
| `3`, `4`, `5` | 66    | Godr-Ayed weapons (736015 Godr-Ayed Longsword, 738201 Godr-Ayed Shield)    |
| `4`, `5`      | 7     | Accessories (11653 Deboreka Necklace, 12276 Deboreka Belt, 11663 Revived Lunar Necklace) |
| `5`           | 21    | Accessories (11629 Tungrad Necklace, 12061 Tungrad Ring, 705509 Manos Necklace) |
| `0` to `5`    | 1     | 719898 Fallen God's Armor                                                  |

### `waititemoffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

### Index Row (12 bytes)

| Offset  | Type | Field    | Notes                                                        |
| ------- | ---- | -------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_key | Row key, the main row's `key`                                |
| `+0x04` | u32  | offset   | Start of the row in `waititem.dbss` plus 4, at its `item_key` |
| `+0x08` | u32  | size     | Always `13`, the row size minus the 4-byte `key`             |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 4).

## Notes

- The Central Market sell window asks
  `ToClient_GetWorldMarketIsWaitItemPopUp(enchantKey, price)` before it
  lists an item and, when it returns true, warns that the Value Pack may
  expire before the sale (`LUA_MARKETPLACE_VALUEPACKAGE_WARNING_MSG`,
  `panel_window_marketplace_sell_renew`). The function takes the item key
  that this file lists. The Central Market lists the queued items under
  `PANEL_MARKETPLACE_WAITLISTTITME` "In Registration Queue", each with its
  `getWaitEndTime()` (`panel_window_marketplace_itemmarket_renew`).
- The registration warning `LUA_ITEMMARKET_REGISTITEM_CANCELITEM_MSGBOX2`
  says "The waiting time until being posted may vary depending on the
  situation", so the client text gives no fixed queue time.
- Accessory and Godr-Ayed levels `3` to `5` are TRI to PEN in game; the
  Item column shows the raw level in brackets, as `item_key_text()` does for
  every table.

## Open Questions

### Whether the List Is the Whole Rule

`ToClient_GetWorldMarketIsWaitItemPopUp` also takes the price, so the queue
may depend on the price as well as on this list. The client code that reads
the file is not in Lua.

## In-Game Checks

### unknown_0d as the Queue Time

Needs zone: any Central Market

`unknown_0d` is `900` on every row, 15 minutes if it counts seconds. Open the
Central Market, pick "In Registration Queue" and note the end time of an
item that just entered the queue (it appears at the top of the list). An end
time 15 minutes after it appeared means `unknown_0d` is the queue time in
seconds.
