# `servantchecktitle.bss` Format

## Purpose

A title tied to owning a servant: the PABR magic, a u16, a `title.dbss`
title and a servant character key, then an empty string table. On client
3474 it holds title `2705` Captain Epheria ("Title Requirement: Exchange
Epheria Galleon Ship License") and character `31020` Epheria Galleon.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 2519 and later | 3474    | `servantchecktitle.bss` | 24    | 1 String Table | 4         |

| Layout | File                    | Known        | Unknown    |
| ------ | ----------------------- | ------------ | ---------- |
| 1      | `servantchecktitle.bss` | 22 B (91.7%) | 2 B (8.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Title names (LOC type 1), character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field         | Notes                                                             |
| ------------------- | ------------ | ------------- | ----------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic         | ASCII `PABR`                                                      |
| `+0x04`             | u16          | unknown_04    | `1` on every client checked; see Open Questions                   |
| `+0x06`             | u32          | title_id      | `title.dbss` title; the handler shows its LOC type 1 name          |
| `+0x0A`             | u16          | character_key | Servant character key; the handler shows its LOC type 6 name      |
| `+0x0C`             | String Table | string_table  | See String Table                                                  |
| `string_table+0x00` | u32          | table_start   | Offset of the string table; `0x0C` on every client checked        |
| `string_table+0x04` | u32          | zero          | Always `0`                                                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: no sheet of a private server's
`DataSheets.bexcel` on that client and no string of its server dump has
`CheckTitle` in the name. The two names come from the values, which agree
with each other: `2705` is a `title.dbss` title whose LOC type 1
requirement text reads "Exchange Epheria Galleon Ship License", and
`31020` is the LOC type 6 name Epheria Galleon.

## Notes

- Raw bytes on clients 2519 to 3474:
  `50 41 42 52 01 00 91 0A 00 00 2C 79 00 00 00 00 0C 00 00 00 00 00 00 00`
  (24 bytes). The file is not in the archives of clients 794 to 2107.
- No client Lua file on client 3474 has `ServantCheckTitle` or
  `CheckTitle` in a function name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. The
  parser reads one entry and raises when the file holds more bytes.

## Open Questions

### The Leading u16

`unknown_04` is `1`. It reads as a count of (title, servant) entries,
with one entry on every client checked, or as a value of its own such as
a servant type (the Epheria Galleon is a ship). A file with two entries
would settle it.
