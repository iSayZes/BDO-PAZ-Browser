# `itemcouponreward.dbss` Format

## Purpose

Item coupon reward table placeholder. On client 3464 the file declares zero
records: a u32 count of `0` followed by 12 zero bytes. The server-side source
is the `ImperialTradeReward` sheet, which gives the coupon drop for selling an
item by one of four sale types; see Field Names for the row the server reads.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `itemcouponreward.dbss`       | 16    | -       | -         |
| 1      | 1784 and later | 3474    | `itemcouponrewardoffset.dbss` | 20    | -       | -         |

| Layout | File                          | Known       | Unknown      |
| ------ | ----------------------------- | ----------- | ------------ |
| 1      | `itemcouponreward.dbss`       | 4 B (25.0%) | 12 B (75.0%) |
| 1      | `itemcouponrewardoffset.dbss` | 4 B (20.0%) | 16 B (80.0%) |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                 |
| ----------------------------- | -------- | -------------------------------------------------------------------- |
| `itemcouponrewardoffset.dbss` | Optional | Offset companion; its count does not match the bytes that follow it |

The handler reads only the main file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

This layout covers only `count = 0`. No record structure can be inferred
because the file holds no records.

| Offset  | Type      | Field      | Notes                                 |
| ------- | --------- | ---------- | ------------------------------------- |
| `+0x00` | u32       | count      | Number of records; `0` on client 3464 |
| `+0x04` | bytes[12] | unknown_04 | All zero on client 3464               |

### `itemcouponrewardoffset.dbss`

20 bytes on client 3464: `04 00 00 00` followed by 16 zero bytes. The count
does not drive the bytes after it.

| Offset  | Type | Field      | Notes              |
| ------- | ---- | ---------- | ------------------ |
| `+0x00` | u32  | count      | `4` on client 3464 |
| `+0x04` | u32  | unknown_04 | `0` on client 3464 |
| `+0x08` | u32  | unknown_08 | `0` on client 3464 |
| `+0x0C` | u32  | unknown_0c | `0` on client 3464 |
| `+0x10` | u32  | unknown_10 | `0` on client 3464 |

Every other bare offset companion has rows of key, u32 offset and u32 size
(9 bytes for `carriagespecoffset.dbss`, 10 for `guildbossoffset.dbss`, 12 for
`itemcollectionscrolloffset.dbss`). Four such rows need at least 36 bytes, so
the 16 bytes after the count are not four offset rows.

## Field Names

The file holds no rows, so these names come from the server and are not
read by the handler. They apply once a client ships rows.

The server dump of a private server on client 1784 (`Instance_dumpFull.exe`)
loads `gc::ItemCouponRewardStaticStatus` rows twice. Its getter
`ItemCouponRewardStaticStatusManager::getXXX(type, key)` (VA `0x140b21080`)
looks the key up in a per-type map of (offset, size) pairs, opens the
`ItemCouponReward` binary at that offset and hands the bytes to the row reader
(VA `0x140b206d0`). The `ImperialTradeReward` sheet of
`DataSheet_CouponReward.xlsm` is loaded by the loop at VA `0x1408b8570`
(`DataSheets.bexcel` has no copy of that sheet; the server tables of a
private server on client 519 have it as `ImperialTradeReward` with the same four columns). Both
loaders write the same members, and the 2016 client's PDB names them:

| File offset | Type | Field                  | Member  | 2016 PDB member      | Sheet column         |
| ----------- | ---- | ---------------------- | ------- | -------------------- | -------------------- |
| `+0x00`     | u32  | `key`                  | `+0x00` | `_key`               | `Key`                |
| `+0x04`     | u16  | `coupon_drop_item_key` | `+0x0C` | `_couponDropItemKey` | `RewardDropGroupKey` |
| `+0x06`     | u8   | `coupon_type`          | `+0x04` | `_couponType`        | `Type`               |
| `+0x07`     | u32  | `reward_rate`          | `+0x08` | `_rewardRate`        | `ExchangeRate`       |

The row is 11 bytes. The file order differs from the member order, so the
file offsets rest on the row reader alone. Member `+0x10` is
`_couponDropItem`, a `gc::ItemMainGroupStaticStatus` pointer the server
links from `coupon_drop_item_key`; the file does not store it.

The row check (VA `0x140b1fd60`) logs "Type is wrong" when `coupon_type` is
`4` or more, "`_couponDropItemKey` is missing" when the drop key is `0`, and
"`_rewardRate` is abnormal" when the rate is above 1,000,000, so the rate is
in parts per million. The link step (VA `0x140b20130`) looks `key` up as an
item key for types 0, 2 and 3 ("coupon item does not exist in the item
table") and skips that check for type 1. For every type it then resolves
`coupon_drop_item_key` as a main drop group ("coupon reward item
MainDropGroup does not exist").

`coupon_type` is `gc::ECouponType` from the 2016 PDB. The sheet's Korean
comment on `Type` says which sale it counts, and on `Key` that selling the
item with that key gives the coupon:

| ID  | Enum                          | Sheet comment                                            |
| --- | ----------------------------- | -------------------------------------------------------- |
| 0   | `ECouponType_TerritorySupply` | Imperial delivery, imperial crafting or fishing delivery |
| 1   | `ECouponType_Vehicle`         | Horse delivery                                           |
| 2   | `ECouponType_NpcWorking`      | House crafting                                           |
| 3   | `ECouponType_Trade`           | General trade                                            |

`ECouponType_Max` is `4`. The 2016 manager holds `pa::Array<..., 4> _list`,
one map per type, and the 1784 manager adds four offset maps after them;
`getXXX` returns nothing for a type of `4` or more.

On the private server's client 1784 data, the sheet holds 2,038 rows of all
four types, and its compiled `itemcouponreward.dbss` and
`itemcouponrewardoffset.dbss` hold the same 16 and 20 bytes as client 3464.
The rows stay on the server. `global_define_cpp_enum.luac` has no coupon
type enum.

## Notes

- `python browser.py --list *coupon*` shows `coupon.dbss` and
  `couponoffset.dbss` as the only other coupon tables; they are separate files
  with their own layout.
- The client Lua has no reference to the table. `widget/coupon/coupon.luac`
  only forwards `FromClient_UseCouponItem(itemWhereType, slotNo)` to
  `ToClient_RegisterCoupon`.
- The other empty DBSS tables ([empty](empty_dbss.md)) are 4 bytes, and
  their offset companions are 4 bytes with a count of `0`. This file is the
  only one with bytes after the count.
- `EmptyTableHandler` previews it like those tables and raises an error when
  `count` is not `0`, so a client that ships records shows up as a parse
  error. `itemcouponrewardoffset.dbss` gets a raw view of its u32 words
  (`_dbss/itemcouponreward/`) until its layout is known.

## Open Questions

### One Block per Coupon Type

The 12 zero bytes after the count in `itemcouponreward.dbss` and the four
zero words after the `4` in `itemcouponrewardoffset.dbss` match no row
layout. The `4` equals `ECouponType_Max`, and the 1784 server keeps one row
map and one offset map per coupon type (Field Names). Read as one block per
type, each a u32 row count and its rows, both files fit exactly with every
block empty:

- `itemcouponreward.dbss`: four row counts of `0` and no block count, the
  shape of [actionexp](actionexp_dbss.md), 4 x 4 = 16 bytes.
- `itemcouponrewardoffset.dbss`: a block count of `4`, then four row counts
  of `0`, the shape of `lifeexpoffset.dbss` in [lifeexp](lifeexp_dbss.md),
  4 + 4 x 4 = 20 bytes.

The server dump reads rows only through `getXXX`, and no reader of either
file's header was found in it, so the words keep their `unknown_<offset>`
names. A client that ships rows would confirm the blocks.
