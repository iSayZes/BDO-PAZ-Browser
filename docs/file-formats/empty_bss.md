# Empty BSS Tables Format

## Purpose

PABR `.bss` tables the client ships with no records:
`enchantlightstone.bss` and `lightstoneenchantgroup.bss`. Each is 20 bytes:
the `PABR` magic, a record count of `0`, a string table with no strings and
the 8-byte PABR trailer. Client 1784 has neither file.

The names point at Lightstone enhancement and Lightstone enhancement groups,
but no record, Lua function or reference source shows what a row would hold.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | -------------- | --------- |
| 1      | 3473 and later | 3474    | `enchantlightstone.bss`      | 20    | 1 String Table | 4         |
| 1      | 3473 and later | 3474    | `lightstoneenchantgroup.bss` | 20    | 1 String Table | 4         |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `enchantlightstone.bss`      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `lightstoneenchantgroup.bss` | 20 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`)
with no rows. No record structure can be inferred because the files hold no
records.

| Offset              | Type         | Field        | Notes                                            |
| ------------------- | ------------ | ------------ | ------------------------------------------------ |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                     |
| `+0x04`             | u32          | count        | Number of records; `0` in both files             |
| `+0x08`             | String Table | string_table | See String Table                                 |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x08` in both files |
| `string_table+0x04` | u32          | zero         | Always 0                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | `0` in both files    |
| `+0x04` | pstr[string_count] | strings      | Empty                |

## Notes

- Raw bytes of both files on client 3473:
  `50 41 42 52 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- Neither file is in the client 1784 archive. The 2016 PDB, a private
  server's `DataSheets.bexcel`, `.xlsm` sheets, compiled `binary/` folder and
  server dump on client 1784 hold no table, file, struct or loader with
  `LightStone` in its name. That `ContentsGroupOption` sheet has no key
  between `1795` and `2000`, so contents group `1801` (below) is newer than
  client 1784 too.
- The installed `BlackDesert64.exe` (client 3473) holds neither file name as
  ASCII or UTF-16 text, so it does not show the loader or its struct.
- The client Lua on client 3473 (3,073 `.luac` files) names neither file.
  `global_contentsoptions.luac` sets
  `_ContentsGroup_EnchantLightStone = ToClient_IsContentsGroupOpen("1801")`,
  and no other Lua file reads `_ContentsGroup_EnchantLightStone`. The
  Lightstone bag (`_ContentsGroup_LightStoneBag`, contents group `1815`) and
  the set lookups (`ToClient_getLightStoneSet`, read from
  [`lightstoneset.bss`](lightstoneset_bss.md)) are separate features.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) with the
  PABR reader in `_bss/empty_tables/parser.py` previews every file in
  `_bss/empty_tables/tables.py`. A file that declares a record or a string
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- The zero-count `.dbss` tables have their own doc:
  [empty](empty_dbss.md).

## Open Questions

### Record Layout

No client checked has a record in either file, so the row layout is
unknown. When a client ships `count > 0`, the file moves to its own doc and
handler, with rows starting at `+0x08` and ending at `table_start`.

### Contents Group 1801

The Lua defines `_ContentsGroup_EnchantLightStone` for contents group `1801`
but never reads it. Whether that group gates whatever reads these two tables
is unknown.
