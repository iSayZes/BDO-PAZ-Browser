# `itemlinkprice.bss` Format

## Purpose

Items whose price follows another item's price: pairs of item keys, the
item first, then the item whose price it takes. Fiery Kutum Shield
(`694290`) follows Kutum Shield (`10140`). The pairs on client 3474 tie a
gear variant (`Fiery`, `Earthshaking`, `Ultimate`, `of Agony`) or a second
item of the same name to the base item.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records    | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------ | ---------- | --------- |
| 1      | 1485 and later | 3474    | `itemlinkprice.bss` | 29,660 | 3,705 Link | 8         |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `itemlinkprice.bss` | 29,660 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Item names (type `0`)       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type             | Field              | Notes                                                   |
| ------------------- | ---------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]          | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32              | link_count         | Number of rows; `3705` on client 3474                   |
| `+0x08`             | Link[link_count] | links              | See Link                                                |
| `links+0x00`        | String Table     | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32              | string_table_start | Absolute offset of `string_count`; equals `8 + 8 x link_count` |
| `string_table+0x04` | u32              | zero               | Always `0`                                              |

### Link (8 bytes)

| Offset  | Type | Field                 | Notes                                                              |
| ------- | ---- | --------------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | price_follow_item_key | The item whose price follows; unique per row on clients 1784 and 3474 |
| `+0x04` | u32  | price_target_item_key | The item whose price it follows                                    |

Both are item keys below `2^24`, so read as item enchant keys
(`enchant_level << 24 | item_id`) they are level `0` on every row of
clients 1784 and 3474.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The `LinkPrice` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `PriceFollowItem` and `PriceTargetItem`. All 2,366
pairs of client 1784 are sheet rows (the sheet has 2,381; 15 more), and
all 2,381 sheet pairs are pairs of client 3474, in the same column order.
The developer workbook (`datasheet_itemdatatable_equip.xlsm`) adds the note
columns `#가격을따라가는아이템명` ("name of the item that follows the
price") and `#가격대상이되는아이템명` ("name of the item that is the
price target"): `Fiery Kutum Shield` and `Kutum Shield` in the first row.

## Notes

- No client Lua names the table; the market and the NPC shops read item
  prices through C++ calls.

## Open Questions

### Which Price Follows

The sheet names say one item's price follows the other's, but not which
price: the Central Market base price, the NPC sell price, or the price a
repair or a cron stone cost is worked out from. Comparing the
`itemenchant.dbss` prices of a few pairs, or the market prices of a
variant and its base item, could tell which.
