# `purchaselimitgroup.dbss` Format

## Purpose

Purchase limits that several Pearl Shop products share. A product joins a
group through its `PurchaseGroupNo`, and the group's limit then counts the
purchases of every product in it together. One 9-byte row per group: the
group number, who the limit counts for (character or family) and how many
purchases it allows. Companion `purchaselimitgroupoffset.dbss` lists where
every row sits.

On client 1784 the `CashProduct_Table` sheet puts the four head maid and
butler contracts into the two groups: group `1` holds `[Head Storage
Butler] Sebastian` (`98225`) and `[Head Storage Maid] Cecilia` (`89412`),
group `2` holds `[Head Transaction Butler] Sebastian` (`89410`) and `[Head
Transaction Maid] Cecilia` (`89411`). Their English product descriptions
(LOC type 50) end with "Only one Head Storage Maid/Butler per Family" and
"Only one Head Transaction Maid/Butler per Family", which is what both rows
hold: one purchase per family.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ------------ | --------- |
| 1      | 1784 and later | 3474    | `purchaselimitgroup.dbss`       | 22    | 2 Row        | 9         |
| 1      | 1784 and later | 3474    | `purchaselimitgroupoffset.dbss` | 28    | 2 Offset Row | 12        |

| Layout | File                            | Known         | Unknown    |
| ------ | ------------------------------- | ------------- | ---------- |
| 1      | `purchaselimitgroup.dbss`       | 22 B (100.0%) | 0 B (0.0%) |
| 1      | `purchaselimitgroupoffset.dbss` | 28 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                  |
| ------------------------------- | -------- | --------------------------------------------------------------------- |
| `purchaselimitgroupoffset.dbss` | Optional | `group_no -> (data_offset, data_size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                         |
| ------- | ---------- | ----- | --------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2` on client 3474            |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row  |

### Row (9 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | group_no       | Group number, the `PurchaseGroupNo` of a product; unique per row, the index key |
| `+0x04` | u8   | purchase_type  | Who the limit counts for, a `CashPurchaseLimitType`; see Limit Types  |
| `+0x05` | i32  | purchase_count | Purchases the group allows                                            |

The rows are packed with no padding, so `purchase_count` sits at an odd
offset.

### `purchaselimitgroupoffset.dbss`

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `purchaselimitgroup.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row          |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                  |
| ------- | ---- | ----------- | -------------------------------------- |
| `+0x00` | u32  | group_no    | Key of the row it points at            |
| `+0x04` | u32  | data_offset | Start of the row, at its `group_no`    |
| `+0x08` | u32  | data_size   | `9`, the whole row                     |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 the index lists group `2` first and group `1` second,
in the order of the main file, and every index row points at the row with
its key.

## Limit Types

`purchase_type` takes the values of `CppEnums.CashPurchaseLimitType` in
`global_define_cpp_enum.luac`, the same enum (`gc::CashPurchaseLimitType`,
an `unsigned char`) as the 2016 PDB names:

| Value | Name          | Pearl Shop limit line (`panel_pearlshop.luac`)     |
| ----- | ------------- | -------------------------------------------------- |
| `0`   | `None`        | None shown                                         |
| `1`   | `AtCharacter` | `LUA_INGAMECASHSHOP_GOODSDETAILINFO_CHARACTER` (Character) |
| `2`   | `AtAccount`   | `LUA_INGAMECASHSHOP_GOODSDETAILINFO_FAMILY` (Family) |

Both rows hold `2` on clients 1784 and 3474.

## Field Names

The names are the columns of the `PurchaseGroup_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 (`GroupNo`, `PurchaseType`,
`PurchaseCount`), a sheet of its `datasheet_cashproduct.xlsx` workbooks. The sheet's two rows (`1`, `2`, `1`) and (`2`, `2`, `1`) match the
file on 2 of 2 keys on clients 1784 and 3474. The 1784 and 3474 files are
byte for byte the same.

The server dump of the same private server checks the sheet with the
messages `PurchaseGroup_Table GroupNo(%#) : limitType` and `PurchaseGroup_Table
GroupNo(%#) : limitCount`, so `PurchaseType` is a limit type and
`PurchaseCount` a limit count. A product stores the same pair: the 2016
`gc::CashProductStaticStatus` has `_productCashPurchaseLimit`
(`gc::CashPurchaseLimitType`, 1 byte) and `_productCashPurchaseCount` (`int`,
4 bytes), the `PurchaseSubject` and `PurchaseCountLimit` columns of
`CashProduct_Table`, which is why `purchase_count` is read as an `i32`. The
2016 PDB has no purchase group struct.

## Open Questions

### Which Products Belong to a Group

The link from product to group is the `PurchaseGroupNo` column of
`CashProduct_Table`. `cashproduct.dbss` blocks are undecoded past the name
(see [`cashproduct.dbss`](cashproduct_dbss.md)), so the handler cannot list
a group's products. The four grouped products of client 1784 named in
Purpose come from the sheet, not from the client file.

### Group Limit and Product Limit Together

On client 1784 each of the four grouped products also has its own limit in
`CashProduct_Table` (`PurchaseSubject` `2`, `PurchaseCountLimit` `1`). No
client Lua reads the group: the Pearl Shop reads `getCashPurchaseLimitType()`
and `getCashPurchaseCount()` of the product and
`getRemainingLimitCount()` by product number, and no Lua file names a
purchase group.
Whether the server checks the group limit in place of the product limit or
on top of it is open.
