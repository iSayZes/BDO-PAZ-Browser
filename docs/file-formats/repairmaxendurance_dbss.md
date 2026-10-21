# `repairmaxendurance.dbss` Format

## Purpose

The materials that restore an item's max durability: one row per item that
can be repaired this way, with a counted list of materials and the max
durability each one restores. Every row starts with the item itself (`10`)
and ends with Memory Fragment (`44195`, `1`). The Max Durability Recovery
window (`panel_window_endurance_recovery_all`) reads it through
`ToClient_getRepairMaxEnduranceCount`. Companion
`repairmaxenduranceoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes   | Records                   | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------- | ------------------------- | --------- |
| 1      | 1485 and later | 3474    | `repairmaxendurance.dbss`       | 108,380 | 5,450 Material, 1,458 Row | 14        |
| 1      | 1485 and later | 3474    | `repairmaxenduranceoffset.dbss` | 17,500  | 1,458 Offset Row          | 12        |

| Layout | File                            | Known              | Unknown    |
| ------ | ------------------------------- | ------------------ | ---------- |
| 1      | `repairmaxendurance.dbss`       | 108,380 B (100.0%) | 0 B (0.0%) |
| 1      | `repairmaxenduranceoffset.dbss` | 17,500 B (100.0%)  | 0 B (0.0%) |

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

| File                            | Required | Role                                                                 |
| ------------------------------- | -------- | -------------------------------------------------------------------- |
| `repairmaxenduranceoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the rows carry their own material count and can be walked without it |
| `languagedata_en.loc`           | Optional | Item names (type `0`, `str_id1` = item ID)                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `1458` on client 3474        |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 22 bytes + materials)

| Offset  | Type                     | Field                   | Notes                                                                 |
| ------- | ------------------------ | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                      | item_key                | Item whose max durability the row restores, packed as `enchant_level << 24 \| item_id`; unique per row, the index key |
| `+0x04` | u32                      | item_key_dup            | Equal to `item_key` in every row; the offset file points here         |
| `+0x08` | i64                      | only_need_money         | Silver for a repair with no material; `0` in every row                |
| `+0x10` | i16                      | only_money_repair_count | Max durability that silver-only repair restores; `0` in every row     |
| `+0x12` | u32                      | material_count          | Number of materials; `2` to `12`                                      |
| `+0x16` | Material[material_count] | materials               | See Material                                                          |

The enchant level byte of `item_key` is `0` in every row on clients 1784
and 3474. The rows are not sorted by `item_key`.

### Material (14 bytes)

| Offset  | Type | Field        | Notes                                                              |
| ------- | ---- | ------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_key     | Material item, packed as the row's `item_key`; enchant level `0` in every entry |
| `+0x04` | i16  | repair_count | Max durability one material restores; see Repair Counts            |
| `+0x06` | i64  | need_money   | Silver per use; `0` in every entry                                 |

### `repairmaxenduranceoffset.dbss`

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `repairmaxendurance.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row       |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                     |
| ------- | ---- | ----------- | --------------------------------------------------------- |
| `+0x00` | u32  | item_key    | Key of the row it points at                               |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_key_dup`                          |
| `+0x08` | u32  | data_size   | The row without its leading `item_key`: `18 + 14 x material_count` |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Repair Counts

`repair_count` values on client 3474, over all 5,450 materials of the 1,458
rows:

| Value | Materials | Items                                                                  |
| ----- | --------- | ---------------------------------------------------------------------- |
| `10`  | 3,749     | The row's own item (first in every row) and other versions of the same gear |
| `5`   | 179       | Refined Black Energy Residue (`9750`, 90 rows), Time-filled Fragment (`721048`, 89 rows) |
| `20`  | 54        | Sandstorm Crystal (`721031`)                                           |
| `1`   | 1,468     | Memory Fragment (`44195`, last in every row), Yona's Fragment (`44350`, 10 rows) |

Material counts per row on client 3474: `3` on 1,212 rows, `8` on 176,
`6` on 22, `4` on 20, `5` on 16, `12` on 8, `2` and `7` on 2 each.

## Field Names

The names follow the 2016 `gc::RepairMaxEnduranceStaticStatus`, keyed by a
`gc::ItemEnchantKey`, with the members `_keyItem` (`ItemEnchantKey`),
`_onlyMoney` (`__int64`), `_repairAmountOnlyMoney` (`short`) and
`_materialList`, a vector of `gc::RepairMaxEnduranceMaterial` (`_itemKey`
as an `ItemEnchantKey`, `_repairAmount` as a `short`, `_needMoney` as an
`__int64`). Their sizes give the 8 + 2 bytes after `item_key_dup` and the
4 + 2 + 8 bytes of a Material. The field names are the columns of the
`RepairMaxEndurance` sheet of a private server's `DataSheets.bexcel` on
client 1784: `BaseItem`, `OnlyNeedMoney`, `OnlyMoneyRepairCount`, then ten
slots of `ItemN`, `RepairCountN` and `NeedMoneyN`.

The sheet lists only the extra materials. A row of the file holds the item
itself with `10`, the sheet's slots in sheet order, then Memory Fragment
with `1`:

| Client | Rows | Shared with the sheet | Rows that match | Misses                                                                    |
| ------ | ---- | --------------------- | --------------- | ------------------------------------------------------------------------- |
| 1784   | 1425 | 1425                  | 1301            | 122 Tuvala gear rows list other Tuvala gear (`10`) where the sheet lists Tuvala Ore (`721051`, `10`); 2 rows (`718600`, `719069`) have no extra material where the sheet lists `721008` with `100` |
| 3474   | 1458 | 1232                  | 1167            | 63 Tuvala gear rows list Time-filled Fragment (`721048`, `5`) where the sheet lists Tuvala Ore (`721051`, `10`); the same 2 rows as on client 1784 |

The sheet has 1,547 rows, 122 of them with no row on client 1784.
`OnlyNeedMoney`, `OnlyMoneyRepairCount` and
every `NeedMoneyN` are `0` in the sheet, as in the file on both clients.

## Notes

- `panel_window_endurance_recovery_all_2.luac` builds the confirmation
  text of a repair: `10` when the material is the item itself, the repaired
  item's `_repairEnduranceCount` (item static status) when the material is
  Memory Fragment (`ItemEnchantKey(44195)` in
  `panel_window_endurance_recovery_all.luac`), and
  `ToClient_getRepairMaxEnduranceCount(repairItemKey, materialItemKey)` for
  any other material. With a cash item the count is multiplied by 5.
  `repair_MaxEndurance()` sends the repair.

## Open Questions

### Whether the Same-Item and Memory Fragment Entries Are Read

Every row holds the item itself with `10` and Memory Fragment with `1`, but
the recovery window Lua hard-codes `10` for the item itself and takes the
Memory Fragment count from the repaired item's `_repairEnduranceCount`. No
client Lua reads the two entries' `repair_count`, so whether the server
uses them, or only checks that the material is allowed, is open.
