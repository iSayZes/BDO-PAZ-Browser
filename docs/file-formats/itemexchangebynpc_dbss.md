# `itemexchangebynpc.dbss` Format

## Purpose

The item exchanges NPCs offer: each row trades a count of one item for a
count of another. NPC dialogs list these rows by key through
[`displayexchangeitemnpc.dbss`](displayexchangeitemnpc_dbss.md); the
exchange window shows the need and result item, and the worker hire window
shows the need item only. `itemexchangebynpcoffset.dbss` is the index into
it, keyed by the exchange key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `itemexchangebynpc.dbss`       | 5,856 | 209 Row        | 28        |
| 1      | 1485 and later | 3474    | `itemexchangebynpcoffset.dbss` | 2,094 | 209 Offset Row | 10        |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `itemexchangebynpc.dbss`       | 5,856 B (100.0%) | 0 B (0.0%) |
| 1      | `itemexchangebynpcoffset.dbss` | 2,094 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                      |
| ------------------------------- | -------- | --------------------------------------------------------- |
| `itemexchangebynpcoffset.dbss`  | Optional | `item_exchange_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| `displayexchangeitemnpc.dbss`   | Optional | The NPC dialogs that list each exchange key, for the NPC names |
| `languagedata_en.loc`           | Optional | Need and result item names (type `0`) and NPC names (type `6`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                       |
| ------- | ---------- | ----- | ------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `209` on client 3474        |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (28 bytes)

| Offset  | Type | Field                 | Notes                                                        |
| ------- | ---- | --------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | item_exchange_key     | The key `displayexchangeitemnpc.dbss` lists; unique per row   |
| `+0x02` | u16  | item_exchange_key_dup | Equal to `item_exchange_key` in every row; the offset index points here |
| `+0x04` | u32  | need_item_key         | Item paid, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x08` | i64  | need_item_count       | Count of the need item; `1` to `600` (client 3474)            |
| `+0x10` | u32  | result_item_key       | Item received, packed as `need_item_key`; level `0` on every row of clients 1784 and 3474 |
| `+0x14` | i64  | result_item_count     | Count of the result item; `1` on every row but key `193` (`5`, client 3474) |

The rows are not sorted by key.

### `itemexchangebynpcoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemexchangebynpc.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                  |
| ------- | ---- | ----------------- | ------------------------------------------------------ |
| `+0x00` | u16  | item_exchange_key | Key of the row                                         |
| `+0x02` | u32  | data_offset       | Row start + 2, at `item_exchange_key_dup`              |
| `+0x06` | u32  | data_size         | `26`, the row size - 2                                 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The 26 bytes from `+0x02` are the 2016 `gc::ItemExchangeByNpcStaticStatus`
packed without padding: `_itemExchangeByNpcKey` (u16 `gc::KeyType`),
`_needItemEnchantKey` (`gc::ItemEnchantKey`), `_needItemCount` (`__int64`),
`_toItemEnchantKey` (`gc::ItemEnchantKey`) and `_toItemCount` (`__int64`).
The struct's two `gc::ItemEnchantStaticStatus` pointers are not in the file.
The file writes the key once more in front of each row as the index key.

The values match the `ItemExchangeByNpc_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`, and the `ItemExchangeByNpc_Table`
of a private server on client 519 by `Index`:

| Field             | Column              | Same value (client 1784 sheet, 1784 file) | Same value (client 1784 sheet, 3474 file) | Same value (client 519 table, 3474 file) |
| ----------------- | ------------------- | ----------------------------------------- | ----------------------------------------- | ---------------------------------------- |
| item_exchange_key | `Index`             | 222 of 222 rows                           | 209 of 209 rows                           | 207 of 209 rows                          |
| need_item_key     | `Itemkey`           | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| need_item_count   | `ItemCount`         | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| result_item_key   | `ExchangeItemKey`   | 222 of 222                                | 209 of 209                                | 207 of 207                               |
| result_item_count | `ExchangeItemCount` | 222 of 222                                | 209 of 209                                | 207 of 207                               |

The client 519 table has no row for two of the 209 keys of client 3474.

## Notes

- The exchange window Lua (`panel_dialog_exchange_item.luac`) takes each
  row through `getItemExchangeByNpcStaticStatusWrapperAtIndex()` of the
  open dialog's `displayexchangeitemnpc.dbss` row and shows
  `getNeedItemStaticStatusWrapper()` with `getNeedItemCount_s64()` and
  `getToItemStaticStatusWrapper()` with `getToItemCount_s64()`. The worker
  hire window (`panel_dialog_employee_hireitem_all_1.luac`) walks the same
  list and reads only the need item and its count.
- On client 3474 the 209 keys run from `4` to `261`, with 33 distinct need
  items and 175 distinct result items. The most used need items are Horse
  Race Seal (`1001`, 31 rows), Football (`16220`, 25), Shining Medal of
  Honor (`44388`, 22) and Gold Bar 100G (`4`, 18). Key `193` trades one
  [Event] Pet Seal (`16639`) for five Kanpacho's Chewable Tablet (`17728`).
- On client 3474 no `displayexchangeitemnpc.dbss` row lists keys `51`,
  `52`, `53`, `54` and `179`. The keys it lists that have no row here are
  in the [`displayexchangeitemnpc.dbss`](displayexchangeitemnpc_dbss.md)
  Notes.
