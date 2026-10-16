# `itemcouponreward.dbss` Format

## Purpose

Item coupon reward table placeholder. On client 3464 the file declares zero
records: a u32 count of `0` followed by 12 zero bytes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

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

### Trailing 12 Bytes

The 12 zero bytes after the count in `itemcouponreward.dbss` match no known
layout. They could be a fixed header before the records or three more zero
counts of separate sections. A client that ships records would show which.

### Offset Count of 4

`itemcouponrewardoffset.dbss` declares 4 entries but has only 16 bytes after
the count, too few for 4 key, offset and size rows. Four u32 zeros (one per
entry) fit the size, but no other offset companion uses 4-byte rows.
