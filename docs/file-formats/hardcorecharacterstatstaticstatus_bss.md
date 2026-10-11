# `hardcorecharacterstatstaticstatus.bss` Format

## Purpose

One stat body per class type, in the layout of the
[experience.bss](experience_bss.md) level records. The name ties it to the
Hardcore server (`ToClient_isHardCoreCharacter` in the client Lua), which LOC
type 37 says needs a level 60+ character on a normal server. On client 3464
every row equals the `experience.bss` level 60 body: AP `+1` and DP `+1`.

Example:

```text
class 0 Warrior: AP 1, DP 1
class 25 Kunoichi: AP 1, DP 1
```

## Companion Files

The file is self-contained. The handler reads class names through the shared
LOC lookup:

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type 21, `str_id1` = class type) |

All multi-byte values are little-endian.

## File Layout

A PABR file with no row count after the magic: the rows start at `+0x04`
and fill the space up to the string table.

| Offset  | Type    | Field        | Notes                                                            |
| ------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00` | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04` | row[]   | rows         | 201-byte rows, 47 (class types 0 to 46) on client 3464           |
| after   | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8 | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4 | u32     | zero         | Always 0                                                         |

On client 3464 the 47 rows end at `0x24EB`, the stored `table_start`. The
string table holds one wide string, `1D1`, as in `experience.bss`.

## Record Structure

### Row (201 bytes)

Fields are unaligned.

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Equals the row index; the class type `getClassType()` returns |
| `+0x01` | stat body | stats      | The [experience.bss](experience_bss.md) Stat Body            |

The `unknown_*` fields and `ap_bonus` / `dp_bonus` keep the names and the
body-relative offsets of the `experience.bss` Stat Body table.

## Suggested UI Layout

| Column     | Type | Notes                             |
| ---------- | ---- | --------------------------------- |
| Class Type | num  | `class_type`                      |
| Class      | text | LOC type 21 name, else the number |
| AP         | num  | `ap_bonus`                        |
| DP         | num  | `dp_bonus`                        |

## Notes

- On client 3464 all 47 bodies are byte-identical and equal the
  `experience.bss` level 60 to 130 body, the one with both bonuses.
- bdo-data-extractor describes the same 201-byte rows and the level 60
  match.
- The parser is `_bss/hardcorecharacterstatstaticstatus/parser.py`; it reads
  the body through `_bss/experience/stat_body.py`.

## Open Questions

### What Reads the Table

No client Lua names the file or a function that returns its values. The
Hardcore character info panels (`panel_characterinfo_hardcore_*`) show
titles and survival points, not these stats, so whether the server uses the
row in place of the `experience.bss` record for Hardcore characters is open.
