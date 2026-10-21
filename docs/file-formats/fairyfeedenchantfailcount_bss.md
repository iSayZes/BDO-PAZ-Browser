# `fairyfeedenchantfailcount.bss` Format

## Purpose

The equipment feeding table, compiled from the `FairyFeed_Table` developer
sheet: for each feed key and enhancement level, what feeding a piece of
equipment gives. Each record holds the entries of one `fairy_feed_key`, one
11-byte entry per enhancement level. The field names are the sheet's columns
(see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------- | --------- |
| 1      | 3473 and later | 3474    | `fairyfeedenchantfailcount.bss` | 147   | 9 Entry, 7 Record | 11        |

| Layout | File                            | Known          | Unknown    |
| ------ | ------------------------------- | -------------- | ---------- |
| 1      | `fairyfeedenchantfailcount.bss` | 147 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None: the file has no `fairyfeedenchantfailcountoffset.dbss`, and no
companion is needed to parse it. Clients 1485 and 1784 ship the same table as
`fairyfeedenchantfailcount.dbss` with an offset index instead (see Field
Names).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field          | Notes                                        |
| ------------------- | ------------- | -------------- | -------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                               |
| `+0x04`             | u32           | count          | Number of records; observed 7 (see Notes)    |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back        |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings  |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record; observed 135 |
| `string_table+0x04` | u32           | zero           | Always `0`                                   |

Observed file size is 147 bytes: 8-byte header, 127 bytes of records, 12-byte
trailer.

The 12-byte trailer (`string_table`, `end_of_records`, `zero`) is the same
trailer shape used by [fairyupgraderate.bss](fairyupgraderate_bss.md) and
[zodiacsignindex.bss](zodiacsignindex_bss.md).

### Record (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Observed | Notes                              |
| ------- | ------------------ | ----------- | -------- | ---------------------------------- |
| `+0x00` | u32                | entry_count | 1 or 2   | Number of entries that follow      |
| `+0x04` | Entry[entry_count] | entries     |          | `entry_count` × 11-byte entries    |

Records have no key of their own. Every entry in a record repeats the same
`fairy_feed_key`, and on client 3474 that value equals the record index plus
one across all seven records.

### Entry (11 bytes)

| Offset  | Type | Field          | Notes                                                            |
| ------- | ---- | -------------- | ---------------------------------------------------------------- |
| `+0x00` | u16  | fairy_feed_key | `FairyFeedKey`; the same for every entry in a record             |
| `+0x02` | u8   | enchant_level  | `EnchantValue`; enhancement level of the fed item (19 TET, 20 PEN); 0 under keys 3 to 7 |
| `+0x03` | u32  | feed_value     | `FeedValue`                                                      |
| `+0x07` | u32  | equip_exp      | `EquipExp`; a u64 in the 1784 `.dbss`                            |

Earlier versions of this doc called `fairy_feed_key` `unknown_00` (before
that `group_id`), `enchant_level` `unknown_02` (`sub_key`), `feed_value`
`unknown_03` (`value_a`) and `equip_exp` `unknown_07` (`value_b`).

The 11-byte entry is unaligned: `feed_value` starts at an odd offset, so a
parser must read the two u32 fields at `+0x03` and `+0x07` rather than assume
4-byte alignment.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes                       |
| ------- | ------------------ | ------------ | -------- | --------------------------- |
| `+0x00` | u32                | string_count | 0        | Always zero                 |
| `+0x04` | pstr[string_count] | strings      |          | Empty                       |

Earlier versions of this doc called `string_count` the trailer's `unknown_00`
and `zero` its `unknown_08`.

## Decoded Table

All nine entries on client 3474:

| Record | fairy_feed_key | enchant_level | feed_value | equip_exp |
| ------ | -------------- | ------------- | ---------- | --------- |
| 0      | 1              | 19 (TET)      | 0          | 200       |
| 0      | 1              | 20 (PEN)      | 0          | 300       |
| 1      | 2              | 19 (TET)      | 0          | 200       |
| 1      | 2              | 20 (PEN)      | 0          | 300       |
| 2      | 3              | 0             | 100        | 300       |
| 3      | 4              | 0             | 100        | 300       |
| 4      | 5              | 0             | 100        | 300       |
| 5      | 6              | 0             | 100        | 300       |
| 6      | 7              | 0             | 300        | 350       |

The table splits in two. Keys 1 and 2 carry an entry for TET and one for PEN,
both with `feed_value` 0. Keys 3 to 7 carry one entry with `enchant_level` 0
and a non-zero `feed_value`.

## Field Names

The names come from the server dump of a private server on client 1784
(`Instance_dumpFull.exe`). It loads the table twice into one static status,
`FairyFeedEnchantFailCountStaticStatusManager`: from the client's
`FairyFeedEnchantFailCount` binary (row reader at VA `0x140b5b660`, called
from VA `0x140b70433`) and from the `FairyFeed_Table` developer sheet (column
reads at VA `0x14090b999` to `0x14090bac6`). Both write the same members:

| Field            | Member  | Read from the 1784 file | Sheet column   |
| ---------------- | ------- | ----------------------- | -------------- |
| `fairy_feed_key` | `+0x14` | u16                     | `FairyFeedKey` |
| `enchant_level`  | `+0x16` | u8                      | `EnchantValue` |
| `feed_value`     | `+0x10` | u32                     | `FeedValue`    |
| `equip_exp`      | `+0x08` | u64                     | `EquipExp`     |

The reader reads the members in the table's order, and its error message
names the first two: "getXXX key : %# level : %#".

Clients 1485 and 1784 ship the table as `fairyfeedenchantfailcount.dbss`: a
u32 key count, then per key a u32 entry count and 15-byte entries in the
order above. The official files of both clients are byte-identical to each
other and to the private server's copy, and hold the sheet's 28 rows with
every column equal: key 1 at enhancement levels 8 to 20 and key 2 at 6 to
20.

The client 3474 `.bss` keeps that nesting (one record per key, the key
repeated in every entry) and the first three fields at the same offsets and
widths. The entry is 4 bytes shorter, so `equip_exp` is read as a u32. The
values do not match: on the four (key, level) pairs both clients have, keys 1
and 2 at TET and PEN, client 3474 stores `feed_value` 0 and `equip_exp` 200
or 300, where client 1784 stores 50 to 75 and 434,760 to 1,830,510. The names
rest on the reader order and the layout, not on values.

The sheet's cell comments (an English translation in this copy, dated
2019-01-08) say that `FairyFeedKey` matches the column of the same name in
the item sheet, which marks the equipment that can be fed to the Black
Spirit; that `EnchantValue` is the enhancement level; and that `FeedValue`
is the "potential breakthrough stack" an item at that level gives when fed.
`EquipExp` has no comment. The sheet's `#Description` column names the rows
("Weapon potential breakthrough +8" up to PEN for key 1, armor from +6 for
key 2) and is not in the file.

A private server on client 519 has the same sheet without `EquipExp`. Its
`EatEnchantEvent.java` takes weapons from +8 and armor from +6, which are
keys 1 and 2, and adds a fail count by level to the player's enchant fail
count; its hardcoded counts are the sheet's `FeedValue` column on client 519
(34 for a PEN weapon, 30 for PEN armor).

The sibling sheet `FairyFeed_Range` (`Stack`, `StackExp`) goes into a second
static status in the same dump (insert at VA `0x140b70a20`, which logs
"EnchantFailCountExpStaticStatusManager Insert Fail Stack(%#) , NeedExp(%#)").
The client file for it is
[enchantfailcountexpstaticstatus.bss](enchantfailcountexpstaticstatus_bss.md)
(`.dbss` on client 1784). On client 3474 that file is keyed by fail stack
and holds this file's nine (key, level) pairs per stack, each non-zero only
from `feed_value` up to below `equip_exp` (see its Stack Ranges).

The 2016 client PDB has no struct for this table.

## Notes

- The record stream lands exactly on `end_of_records`: `7 × 4 + 9 × 11 = 127`
  bytes of records after the 8-byte header. That exact fit is what confirms the
  4-byte `entry_count` prefix and the 11-byte entry size.
- Records are variable length, so a parser must follow `entry_count` rather than
  assume the 15-byte or 26-byte sizes seen in this file.
- `fairy_feed_key` is redundant with the record index on client 3474, but it
  is stored per entry rather than per record, so it is read from the entry.
- Observed: 7 records and 9 entries in the pre-2026-09-27 fixture and in the
  2026-09-27 client; the file is byte-identical between the two.
- The file stem says fairy; the sheet comments say the equipment is fed to
  the Black Spirit. Nothing in this file links it to
  [fairyupgraderate.bss](fairyupgraderate_bss.md) or
  [fairyfeedingitem.dbss](fairyfeedingitem_dbss.md).
- No LOC lookup applies: every field is a small integer, and none of the values
  match a localization key.

## Open Questions

### Items Under Keys 3 to 7

Keys 1 and 2 are weapons and armor on clients 519 to 1784. Keys 3 to 7 are
new on client 3474 and have `enchant_level` 0, so they key items fed at no
particular level. The item sheet's `FairyFeedKey` column has not been found in
a client item file, so which items carry these keys is open.

### `feed_value` and `equip_exp` as a Stack Range

On client 3474 every entry's `feed_value` and `equip_exp` are the first
stack and one past the last stack at which
[enchantfailcountexpstaticstatus.bss](enchantfailcountexpstaticstatus_bss.md)
holds a non-zero value for that key and level: 0 to 199 for TET, 0 to 299
for PEN, 100 to 299 for keys 3 to 6, 300 to 349 for key 7, with 0 misses
over 3,600 values. The client Lua titles the enchant stack list groups with
a start and end stack (`ToClient_GetStartStackByIndex`,
`ToClient_GetEndStackByIndex`). Whether the client reads these two fields
as that start and end, which would leave the 1784 names wrong for client
3474, is open.

### `equip_exp` Width

The 1784 reader reads `EquipExp` as a u64; the client 3474 entry has room for
a u32 only. No reader for the 3474 file was found, so the narrower field rests
on the entry size alone.
