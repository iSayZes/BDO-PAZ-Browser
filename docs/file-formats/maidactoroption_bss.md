# `maidactoroption.bss` Format

## Purpose

Options of the maid actor system (`_ContentsGroup_MaidActorSystem` in the
client Lua): two bytes in the slot where a PABR table keeps its record
count, then an empty string table. On client 3474 the bytes are `1` and
`10`; no source confirms what either holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------------- | --------- |
| 1      | 3251 and later | 3474    | `maidactoroption.bss` | 18    | 1 String Table | 4         |

| Layout | File                  | Known        | Unknown     |
| ------ | --------------------- | ------------ | ----------- |
| 1      | `maidactoroption.bss` | 16 B (88.9%) | 2 B (11.1%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u8           | unknown_04   | `1` on clients 3251 and 3474                               |
| `+0x05`             | u8           | unknown_05   | `10` on clients 3251 and 3474                              |
| `+0x06`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x06` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3251 and 3474:
  `50 41 42 52 01 0A 00 00 00 00 06 00 00 00 00 00 00 00` (18 bytes).
- The file is not in the archives of clients 1784, 2107, 2519 and 3002.
- Two u8 fields are a reading of the bytes; one u16 (`2561`) fits them too.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### Maid Actor Limits

The client Lua (client 3474) reads several maid actor numbers from the
client: `ToClient_GetMaidActorNameLengthMax()`,
`ToClient_GetMaidActorSlotCount()`,
`ToClient_GetNeedItemCountForChangeClothForMaidActor()` and
`ToClient_getUsableMaidCountByType()`. Any of them could return `1` or
`10`, and none of them is shown to read this file. Which one, if any, does
is unknown. The name length and the outfit item count are on screen, see
In-Game Checks.

## In-Game Checks

### Maid Actor Name Length and Outfit Item Count

Needs: a character that can make a custom maid from its own appearance (the
`Panel_Window_MaidActorRegist_All` window).

The client Lua shows two of the candidate numbers on screen. This check tests
whether they are the `10` and the `1` of this file.

1. Open the custom maid creation window, or the rename window of a custom
   maid you already have.
2. Read the description line, which names the minimum and maximum name
   length, and type a long name to see where input stops.
3. Open the custom maid outfit change window and pick an outfit item.
4. Read the count after the required item's name, shown as `(needed/owned)`.

A maximum name length of `10` means `unknown_05` is the name length limit
(`ToClient_GetMaidActorNameLengthMax()`). A needed count of `1` means
`unknown_04` is the outfit change item count
(`ToClient_GetNeedItemCountForChangeClothForMaidActor()`). Other numbers
rule both readings out.
