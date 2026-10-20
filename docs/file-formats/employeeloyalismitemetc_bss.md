# `employeeloyalismitemetc.bss` Format

## Purpose

A PABR file with 16 value bytes next to
[`employeeloyalismitem.dbss`](employeeloyalismitem_dbss.md), the items
that restore a sailor's condition. Read as four u32 they are `2, 0, 2, 0`
on every client checked (1485 to 3474). No field is named yet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `employeeloyalismitemetc.bss` | 32    | 1 String Table | 4         |

| Layout | File                          | Known        | Unknown      |
| ------ | ----------------------------- | ------------ | ------------ |
| 1      | `employeeloyalismitemetc.bss` | 16 B (50.0%) | 16 B (50.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32          | unknown_04   | `2` on every client checked                                |
| `+0x08`             | u32          | unknown_08   | `0` on every client checked                                |
| `+0x0C`             | u32          | unknown_0c   | `2` on every client checked                                |
| `+0x10`             | u32          | unknown_10   | `0` on every client checked                                |
| `+0x14`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x14` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 1485 to 3474:
  `50 41 42 52 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00`
  (32 bytes). The file is not in the archives of clients 794 and 1230.
- The client 1784 file is byte for byte the private server's compiled
  `binary/employeeloyalismitemetc.bss` on that client, but no sheet of its
  `DataSheets.bexcel` matches: `Employee_Loyalism` (`Type`,
  `RecoveryItemKey`, `RecoveryCount`, 4 rows) compiles to
  `employeeloyalismitem.dbss`, and `Employee_Option` holds seven other
  sailor options. The server dump has `employeeLoyalismItem` and the
  loader `loadEmployeeLoyalismInfo`, but no `Etc` name.
- The four u32 are a reading of the bytes; each `0` could be part of a
  wider or narrower field.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### What the Values Count

`employeeloyalismitem.dbss` has two items of each loyalism type (type `0`
Chowder and Raisin Bread, type `1` Elixir of Regeneration and Tears of the
Star), so each `2` may be the item count of one type. The client 3474
sailor preset window (`panel_window_sailorpresetmanager_all_2.luac`) reads
two such counts: `ToClient_getRecoveryItemCount()` for the Loyalty items
(type `0`, slots `Static_RecoverySlotBg1` to `N`) and
`ToClient_getResurrectionItemCount()` for the resurrection items (type
`1`, slots `Static_TreatmentSlotBg1` to `N`). That fits `unknown_04` and
`unknown_0c` as these two counts in type order, but the client may as well
count the `employeeloyalismitem.dbss` rows of each type, which also gives
`2` and `2`. The bytes also read as two counted u32 lists (`[0, 2]` and an
empty one). Read as a u32 count `2` and two 6-byte entries (u32 item, u16
value) the item keys are `0`, which no item has, so that reading is
unlikely. A patch that changes the item count of one type would show
whether the file follows it.
