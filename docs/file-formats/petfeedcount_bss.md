# `petfeedcount.bss` Format

## Purpose

The number of pet feed items: items whose use is `ContentsType_PetFeed`
(`CppEnums.ContentsEventType` `13`). The value sits in the slot where a
PABR table keeps its record count. On client 3474 it is `10`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `petfeedcount.bss` | 20    | 1 String Table | 4         |

| Layout | File               | Known         | Unknown    |
| ------ | ------------------ | ------------- | ---------- |
| 1      | `petfeedcount.bss` | 20 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field           | Notes                                                      |
| ------------------- | ------------ | --------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic           | ASCII `PABR`                                               |
| `+0x04`             | u32          | feed_item_count | Number of pet feed items; see Field Names                  |
| `+0x08`             | String Table | string_table    | See String Table                                           |
| `string_table+0x00` | u32          | table_start     | Offset of the string table; `0x08` on every client checked |
| `string_table+0x04` | u32          | zero            | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

`feed_item_count` equals the number of items with contents event type `13`
on both clients where the items could be counted:

| Client | `feed_item_count` | Items with event type `13` | Source of the item count                          |
| ------ | ----------------- | -------------------------- | ------------------------------------------------- |
| 1784   | `11`              | 11                         | `ContentsEventType` of the `Item_Table` sheet     |
| 3474   | `10`              | 10                         | `contents_event_type` of `itemenchant.dbss` base blocks |

The `Item_Table` sheet is the one in a private server's `DataSheets.bexcel`
on client 1784, whose compiled `binary/petfeedcount.bss` holds `11` as the
client 1784 archive does. On client 3474 the ten items are `17728`, `18041`,
`18408`, `18409`, `18963`, `54016`, `54017`, `54018`, `757431` and `830088`
(`contents_event_type` at `unknown_61+0x25` of
[`itemenchant.dbss`](itemenchant_dbss.md)). The enum value comes from
`global_define_cpp_enum.luac`: `ContentsType_PetFeed = 13`.

Clients 2107 to 3251 hold `11`, `12`, `12` and `10` (clients 2107, 2519,
3002, 3251); their item tables were not counted.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 0A 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The server dump of the private server on client 1784 reads `petFeedCount`
  in `ItemEnchantStaticStatusManager::readFromBinary()`, next to
  `itemMaxLevel` and `itemEnchantOffset`, and logs "Can't Find petFeedCount"
  when the file is missing. The value so belongs to the item tables.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.

## Open Questions

### Feed Bar Size

The pet window (`panel_window_petlist_all.luac`, client 3474) creates
`ToClient_Pet_GetFeedStaticItemCount() * 2` feed slots and fills them from
`ToClient_Pet_GetFeedItemCount()`, the feed items the player holds. Whether
`ToClient_Pet_GetFeedStaticItemCount()` returns `feed_item_count` or counts
the items itself is not visible in the Lua.
