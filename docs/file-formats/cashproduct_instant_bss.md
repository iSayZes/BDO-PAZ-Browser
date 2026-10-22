# `cashproduct_instant.bss` Format

## Purpose

The cost to finish a timed task at once, by the time it has left: one
group per `CppEnums.InstantCashType` (`0` ChangeHouseUseType, `1`
CompleteServantMating, `2` CompleteNpcWorking, `3` CompleteNpcWorkerUpgrade),
each a list of remaining minutes and the cost. The worker and house Lua
(`new_worldmap_working_progress.luac`, `panel_new_housecontrol.luac`)
asks for the cost with
`ToClient_GetUsingPearlByRemainingPearl(CppEnums.InstantCashType.eInstant_CompleteNpcWorking, remainingTime)`
and shows it as Silver (`LUA_WORLDMAP_WORKDING_PROGRESS_IMMEDIATELY_SILVER`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 1      | 1348 and later | 3482    | `cashproduct_instant.bss` | 3,668 | 226 Entry, 4 Group | 16        |

| Layout | File                      | Known           | Unknown    |
| ------ | ------------------------- | --------------- | ---------- |
| 1      | `cashproduct_instant.bss` | 3,664 B (99.9%) | 4 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The groups sit where other `PABR` files keep their row count: the file
stores no group count, and the four groups of `InstantCashType` follow in
type order (`eInstant_Count` is `4`).

| Offset              | Type         | Field        | Notes                                         |
| ------------------- | ------------ | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                  |
| `+0x04`             | Group[4]     | groups       | See Group; type `0` to `3` in order           |
| `groups+0x00`       | String Table | string_table | See String Table                              |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `groups` ends |
| `string_table+0x04` | u32          | zero         | Always `0`                                    |

### Group (variable: 9 bytes + entries)

| Offset  | Type                | Field       | Notes                                                       |
| ------- | ------------------- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u8                  | unknown_00  | `0` on all four groups of clients 1784 and 3482             |
| `+0x01` | u64                 | entry_count | Number of `entries`: `70`, `70`, `70` and `16` on client 3482 |
| `+0x09` | Entry[entry_count]  | entries     | See Entry; `minute` rises within a group                    |

### Entry (16 bytes)

The 2016 `gc::InstantCashItem::value_type`, 16 bytes with its padding.

| Offset  | Type     | Field       | Notes                                                                                      |
| ------- | -------- | ----------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u16      | minute      | Remaining minutes this entry covers (`_minute`): `10` to `2160` in types `0` to `2`, `30` to `500` in type `3` on client 3482 |
| `+0x02` | bytes[6] | padding_02  | Alignment of `pearl_count` to 8 bytes; one value per file (`70 3D FC 7F 00 00` on client 3482, `8D 36 FA 01 00 00` on 1784), so not zeroed |
| `+0x08` | i64      | pearl_count | Cost (`_pearlCount`): Pearls, and Silver in type `2` on client 3482 (`10000000` for 10 minutes) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                        |
| ------- | ------------------ | ------------ | -------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482                 |
| `+0x04` | pstr[string_count] | strings      | None                                         |

## Field Names

The 2016 `gc::InstantCashItem` holds a vector `_pearlList` of
`value_type { unsigned short _minute; __int64 _pearlCount; }` and a
`gc::InstantCashType _instantType`. The `InstantCashItem` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `InstantType`,
`Pearl`, `Minute`, `Hour` and `Second` (the last two derived from
`Minute`), 70 rows per type. Entry `n` of group `t` is compared with the
`n`-th sheet row of `InstantType` `t`.

| Field       | Column   | Same value (client 1784) | Same value (client 3482) |
| ----------- | -------- | ------------------------ | ------------------------ |
| minute      | `Minute` | 280 of 280               | 210 of 226               |
| pearl_count | `Pearl`  | 210 of 280               | 140 of 226               |

`pearl_count` misses all 70 rows of type `2` on client 1784, where the
sheet has `100` per row and the file `10`; client 3482 changes type `2` to
Silver and type `3` to 16 entries from 30 minutes. Types `0` and `1` match
70 of 70 on both clients, which fixes the group order.

## Open Questions

### What the Group Byte Holds

`unknown_00` is `0` before each of the four groups on clients 1784 and
3482. The 2016 struct ends with the one-byte `_instantType`, which would
read `0` to `3` here; a serializer that writes a vector after a flag would
also give one byte.
