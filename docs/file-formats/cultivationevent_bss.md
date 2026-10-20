# `cultivationevent.bss` Format

## Purpose

The farming event types: the keys of the `CultivationEventType_Table`
sheet, the events (pruning, insect removal, bird calls, wilting) a crop
can get. A u32 count follows the PABR magic, then one i16 key per entry.
On every client checked (1784 to 3474) the list is `1`, `0`. The event
ranges of the sheet are not in the client file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `cultivationevent.bss` | 24    | 1 String Table | 4         |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 1      | `cultivationevent.bss` | 24 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                   | Type             | Field                  | Notes                                                      |
| ------------------------ | ---------------- | ---------------------- | ---------------------------------------------------------- |
| `+0x00`                  | char[4]          | magic                  | ASCII `PABR`                                               |
| `+0x04`                  | u32              | type_count             | Number of event types                                      |
| `+0x08`                  | i16[type_count]  | cultivation_event_type | Event type key; unique, not in key order                   |
| `cultivation_event_type+0x00` | String Table | string_table           | See String Table                                           |
| `string_table+0x00`      | u32              | table_start            | Offset of the string table; `0x0C` on every client checked |
| `string_table+0x04`      | u32              | zero                   | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `CultivationEventType_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `CultivationEventType`,
`Pruning_Min`, `Pruning_Max`, `BugRemoval_Min`, `BugRemoval_Max`,
`BirdCall_Min`, `BirdCall_Max` and `Wilt_Harvest`, and two rows,
`CultivationEventType` `0` and `1`. The file holds those 2 of 2 keys and
none of the other columns; the client 1784 file is byte for byte the
private server's compiled `binary/cultivationevent.bss`.

The width comes from the server dump on client 1784: its RTTI names
`gc::CultivationEventStaticStatusManager`, a `StaticStatusManager` keyed by
`KeyType<short,-1>` (`KeyType@F$0?0@` in the mangled name), so the key is
an i16 with `-1` for no type. The loader is
`GameCommonParameterLoaderFromExcel::loadMain(loadCultivationEvent)`.

## Notes

- Raw bytes on clients 1784 to 3474:
  `50 41 42 52 02 00 00 00 01 00 00 00 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes). The file is not in the archives of clients 794, 1230 and 1485.
- The `Object_Table` sheet on client 1784 has a `CultivationEventType`
  column too; one object (`1497`) holds `1`, the other 3,554 rows are empty.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per event type.
