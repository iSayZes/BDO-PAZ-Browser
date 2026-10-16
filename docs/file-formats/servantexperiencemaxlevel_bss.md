# `servantexperiencemaxlevel.bss` Format

## Purpose

Top level of each servant (mount or ship): one row per servant character with
the highest level of its [servantexperience.dbss](servantexperience_dbss.md)
records. On client 3464 the file has 418 rows, the same servants as
`servantexperience.dbss`.

Example (client 3464):

```text
9989 Arduanatt:             100
9808 Horse:                  30
31041 Carrack:                1
```

## Companion Files

| File                  | Required | Role                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) |

All multi-byte values are little-endian.

## File Layout

No magic and no trailer: a count, then the rows to the end of the file.

| Offset  | Type  | Field | Notes                                  |
| ------- | ----- | ----- | -------------------------------------- |
| `+0x00` | u32   | count | 418 on client 3464                     |
| `+0x04` | row[] | rows  | `count` rows of 4 bytes, ending at EOF |

## Record Structure

### Row (4 bytes)

| Offset  | Type | Field        | Notes                                           |
| ------- | ---- | ------------ | ----------------------------------------------- |
| `+0x00` | u16  | character_id | Servant character, as in `characterstatic.dbss` |
| `+0x02` | u16  | max_level    | Highest level                                   |

## Notes

- On client 3464 every `max_level` equals the highest `level` that
  `servantexperience.dbss` holds for the same `character_id`, and both files
  list the same 418 servants: 161 at 100, 132 at 30, 95 at 1, 20 at 15,
  3 at 10, 2 at 20 and 5 at 0.
- The parser is `_bss/servantexperiencemaxlevel/parser.py`; the
  `servantexperience.dbss` tests check that both files agree.
