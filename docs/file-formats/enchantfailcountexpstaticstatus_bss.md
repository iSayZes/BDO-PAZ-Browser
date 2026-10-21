# `enchantfailcountexpstaticstatus.bss` Format

## Purpose

A table keyed by enhancement fail stack. On client 3474 each record holds one
`stack` and, for every feed key and enhancement level of
[fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md), a value
that falls as the stack rises and is non-zero only inside that entry's stack
range (see Stack Ranges). Client 1784 ships a different table under the same
stem: the EXP needed per fail stack, from the `FairyFeed_Range` developer
sheet (Layout 1).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes  | Records                              | Row bytes |
| ------ | -------------- | ------- | -------------------------------------------- | ------ | ------------------------------------ | --------- |
| 2      | 3251 and later | 3474    | `enchantfailcountexpstaticstatus.bss`        | 39,620 | 3,600 Entry, 2,800 Group, 400 Record | 5         |
| 1      | 1485 to 3002   | 3002    | `enchantfailcountexpstaticstatus.dbss`       | 5,140  | 321 Row                              | 16        |
| 1      | 1485 to 3002   | 3002    | `enchantfailcountexpstaticstatusoffset.dbss` | 5,140  | 321 Offset Row                       | 16        |

| Layout | File                                         | Known            | Unknown          |
| ------ | -------------------------------------------- | ---------------- | ---------------- |
| 2      | `enchantfailcountexpstaticstatus.bss`        | 25,220 B (63.7%) | 14,400 B (36.3%) |
| 1      | `enchantfailcountexpstaticstatus.dbss`       | 5,140 B (100.0%) | 0 B (0.0%)       |
| 1      | `enchantfailcountexpstaticstatusoffset.dbss` | 5,140 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | No documented layout |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

None on client 3474: the file has no offset index, and no companion is
needed to parse it. Client 1784 ships the table as
`enchantfailcountexpstaticstatus.dbss` with the index
`enchantfailcountexpstaticstatusoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type          | Field          | Notes                                       |
| ------------------- | ------------- | -------------- | ------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                              |
| `+0x04`             | u32           | count          | Number of records; 400 on client 3474       |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back       |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record       |
| `string_table+0x04` | u32           | zero           | Always `0`                                  |

### Record (variable: 12 bytes + groups)

| Offset        | Type               | Field       | Notes                                              |
| ------------- | ------------------ | ----------- | -------------------------------------------------- |
| `+0x00`       | u32                | group_count | 7 on every record (client 3474)                    |
| `+0x04`       | Group[group_count] | groups      | One per `fairy_feed_key`                           |
| `groups+0x00` | u64                | stack       | `Stack`; the record key, after the groups; 0 to 399 on client 3474 |

### Group (variable: 6 bytes + entries)

| Offset  | Type               | Field          | Notes                                         |
| ------- | ------------------ | -------------- | --------------------------------------------- |
| `+0x00` | u16                | fairy_feed_key | `FairyFeedKey`; 1 to 7 in that order (client 3474) |
| `+0x02` | u32                | entry_count    | 2 under keys 1 and 2, 1 under keys 3 to 7 (client 3474) |
| `+0x06` | Entry[entry_count] | entries        |                                               |

### Entry (5 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u8   | enchant_level | `EnchantValue`; 19 (TET) and 20 (PEN) under keys 1 and 2, 0 under keys 3 to 7 |
| `+0x01` | u32  | unknown_01    | 0 to 75 on client 3474; non-zero only inside the entry's stack range |

The entry is unaligned: `unknown_01` starts at an odd offset.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes        |
| ------- | ------------------ | ------------ | -------- | ------------ |
| `+0x00` | u32                | string_count | 0        | Always zero  |
| `+0x04` | pstr[string_count] | strings      |          | Empty        |

## Layout 1

### `enchantfailcountexpstaticstatus.dbss`

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 251 on client 1784                      |
| `+0x04` | Row[count] | rows  | `count` rows of 16 bytes, ending at EOF |

### Row (16 bytes)

| Offset  | Type | Field     | Notes                                       |
| ------- | ---- | --------- | ------------------------------------------- |
| `+0x00` | u64  | stack     | `Stack`; 0 to 250 in order (client 1784)    |
| `+0x08` | u64  | stack_exp | `StackExp`; 1 at stack 0, 99 at stack 1, 691,830 from stack 240 (client 1784) |

### `enchantfailcountexpstaticstatusoffset.dbss`

| Offset  | Type              | Field   | Notes                                                   |
| ------- | ----------------- | ------- | ------------------------------------------------------- |
| `+0x00` | u32               | count   | Equals the `enchantfailcountexpstaticstatus.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 16 bytes                             |

### Offset Row (16 bytes)

| Offset  | Type | Field  | Notes                            |
| ------- | ---- | ------ | -------------------------------- |
| `+0x00` | u64  | stack  | The row's `stack`                |
| `+0x08` | u32  | offset | Where the row starts: `4 + 16 × index` |
| `+0x0C` | u32  | size   | 16 on every entry                |

## Stack Ranges

On client 3474 every record holds the same nine (`fairy_feed_key`,
`enchant_level`) pairs, in the order of the nine entries of
`fairyfeedenchantfailcount.bss`. For each pair, `unknown_01` is non-zero
exactly when `stack` is at least that entry's `feed_value` and below its
`equip_exp`: 0 misses over the 3,600 values. Within a range the value never
rises as `stack` rises. Keys 1 and 2 hold the same values at every stack.

| `stack` (client 3474) | Key 1, 2 TET | Key 1, 2 PEN | Key 3 | Key 4 | Key 5 | Key 6 | Key 7 |
| --------------------- | ------------ | ------------ | ----- | ----- | ----- | ----- | ----- |
| Range                 | 0 to 199     | 0 to 299     | 100 to 299 | 100 to 299 | 100 to 299 | 100 to 299 | 300 to 349 |
| 0                     | 55           | 75           | 0     | 0     | 0     | 0     | 0     |
| 50                    | 13           | 30           | 0     | 0     | 0     | 0     | 0     |
| 100                   | 4            | 10           | 6     | 26    | 13    | 52    | 0     |
| 150                   | 2            | 5            | 3     | 15    | 7     | 30    | 0     |
| 199                   | 1            | 3            | 2     | 10    | 5     | 20    | 0     |
| 250                   | 0            | 2            | 1     | 7     | 3     | 14    | 0     |
| 299                   | 0            | 1            | 1     | 1     | 1     | 1     | 0     |
| 300 to 349            | 0            | 0            | 0     | 0     | 0     | 0     | 1     |
| 350 to 399            | 0            | 0            | 0     | 0     | 0     | 0     | 0     |

The client Lua has the same ranges. `panel_window_enchantstack_all_1.lua`
groups the items of the enchant stack list by `getStartEndStackIndex()` and
titles each group with `PANEL_ENCHANT_RENEWAL_STACK_RANGE`, filled from
`ToClient_GetStartStackByIndex` and `ToClient_GetEndStackByIndex`. An item
with `isPredation()` opens a number pad whose maximum is
`ToClient_GetAvailablePredationStack(index)`. No Lua call reads this table's
values directly.

## Field Names

The server dump of a private server on client 1784
(`Instance_dumpFull.exe`) inserts this table's rows into
`EnchantFailCountExpStaticStatusManager` at VA `0x140b70a20`, which logs
"Insert Fail Stack(%#) , NeedExp(%#)". The `FairyFeed_Range` sheet of the
same server's `DataSheets.bexcel` has the columns `Stack` and `StackExp`:
the client 1784 `.dbss` matches it on 251 of 251 rows, both columns.

On client 3474 the record key is again a u64 stack, 0 to 399, so it keeps
the name `stack`. The client 3474 file has no `StackExp` column.
`fairy_feed_key` and `enchant_level` hold the nine (key, level) pairs of
`fairyfeedenchantfailcount.bss` on the same client, in the same order and
widths, so they take that doc's names. `unknown_01` matches no sheet column.

## Notes

- The record stream ends at `end_of_records`: 400 records of
  `4 + 7 × 6 + 9 × 5 + 8 = 99` bytes are 39,600 bytes after the 8-byte header
  (client 3474), and the 12-byte trailer closes the file.
- `stack` sits after the groups, at the end of each record. The first record
  starts with `group_count` right after the header, and the last `stack`
  (398) sits right before the string table.
- Records are not in `stack` order: 399, 0, 1, 393, 2, 3 at the start of the
  file (client 3474).
- The `.bss` keeps the stem of the client 1784 `.dbss`, but none of its
  values: there is no EXP column and the record count went from 251 to 400.

## Open Questions

### What `unknown_01` Counts

`unknown_01` is the only value per (stack, key, level). It is largest at the
bottom of each range (75 for PEN at stack 0, 52 for key 6 at stack 100) and
falls to 1 before the range ends, which fits the number of fail stacks that
feeding one item adds at the current stack. The client Lua shows a
per-item stack maximum (`ToClient_GetAvailablePredationStack`) but not where
it comes from, so the reading is not confirmed.

### Items Under Keys 3 to 7

Same open point as in
[fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md): which
items carry `FairyFeedKey` 3 to 7 is not known, so the item behind each
column of Stack Ranges is open for those keys.
