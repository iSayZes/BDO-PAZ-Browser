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

| Layout | File                  | Known            | Unknown    |
| ------ | --------------------- | ---------------- | ---------- |
| 1      | `waititem.dbss`       | 5,580 B (100.0%) | 0 B (0.0%) |
| 1      | `waititemoffset.dbss` | 3,940 B (100.0%) | 0 B (0.0%) |

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
| `+0x0D` | u32  | wait_second   | `900` on every row (client 3474); see Field Names            |

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

## Field Names

The row is the `WorldMarketWaitItem` sheet of a private server on client
1784, with the columns `ItemKey`, `EnchantLevel` and `WaitSecond`. That
server's dump (`Instance_dumpFull.exe`) loads the sheet into
`WorldTradeMarketWaitItemStaticStatus` (loader at VA `0x140a70270`) and
fills the struct in file order (VA `0x140cf600f` to `0x140cf6020`): the
packed key `EnchantLevel << 24 | ItemKey` at `+0`, `ItemKey` at `+4`,
`EnchantLevel` as a byte at `+8` and `WaitSecond` as a u32 at `+0x0C`. After
the row's 4-byte `key`, the 13 bytes the index points at are that struct,
so `+0x0D` is `WaitSecond`.

The loader rejects a row whose `ItemKey` is `0`, whose `EnchantLevel` is
21 or more, or whose `WaitSecond` is above 18,000 (5 hours), with
"판매 대기 waitSecond 비정상 입니다" ("sale wait: waitSecond is invalid") for
the last. The server has no reader for the client file; it loads only the
sheet.

The sheet and the private server's own `waititem.dbss` hold the same 101
rows: matched on item and level, `wait_second` equals `WaitSecond` on all
101. Every value is `900` there and on the 328 rows of client 3474, so the
values alone do not place the column; the struct order above does.

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

### wait_second as the Queue Time

Needs zone: any Central Market

`wait_second` is `900` on every row, 15 minutes. This checks that it is the
time an item waits in the Registration Queue.

1. Open the Central Market and list an item from this table.
2. Pick "In Registration Queue" and note the end time of the item, which
   appears at the top of the list.

Expected: the end time is 15 minutes after the item entered the queue.
