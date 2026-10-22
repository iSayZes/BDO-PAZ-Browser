# `householdlist.bss` Format

## Purpose

Every house character: a u32 count after the PABR magic, then one u16
character key per house. On client 3482 the 865 keys are the 823 node
houses of [`houseinfo.bss`](houseinfo_bss.md), 25 guild houses and the 17
villas; on client 1784 the list holds 801 keys. The same keys are the room
list of [`innstaticstatus.dbss`](innstaticstatus_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | -------------- | --------- |
| 1      | 1348 and later | 3482    | `householdlist.bss` | 1,750 | 1 String Table | 4         |

| Layout | File                | Known            | Unknown    |
| ------ | ------------------- | ---------------- | ---------- |
| 1      | `householdlist.bss` | 1,750 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | House names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                 | Field           | Notes                                                       |
| -------------------- | -------------------- | --------------- | ----------------------------------------------------------- |
| `+0x00`              | char[4]              | magic           | ASCII `PABR`                                                |
| `+0x04`              | u32                  | character_count | Number of house keys; 865 on client 3482                    |
| `+0x08`              | u16[character_count] | character_key   | A house, a `characterstatic.dbss` key; each key once        |
| `character_key+0x00` | String Table         | string_table    | See String Table                                            |
| `string_table+0x00`  | u32                  | table_start     | Offset of the string table, where `character_key` ends      |
| `string_table+0x04`  | u32                  | zero            | Always `0`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482              |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                   |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after the file; the server dump of that client holds the string
`houseHoldList`. Every key resolves to a house name (LOC type 6), so
`character_key` names the meaning.

## Notes

- On client 3482 the keys are, in file order, the 823 `houseinfo.bss` keys
  in that file's row order, with 42 more keys among them: the 23 guild
  houses of [`guildhouseinfo.dbss`](guildhouseinfo_dbss.md), Grána (`3520`)
  and O'draxxia (`3806`) Guild Houses and the villas `3371` to `3387`
  (Kunid's Villa to Oberin's Villa).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per character key.
