# `guildmatchexp.bss` Format

## Purpose

The Combat EXP a Guild League match gives by character level: two rows of
100 values each, value `N` for level `N + 1`. Clients 2519 to 3251 fill
them; row 0 holds the lower values (421,740 on levels 1 to 20) and row 1
the higher (705,375). Both change in steps up to level 40, fall from level
41 and hold `31` from level 68 on. On client 3474 every value is `0`. The ranks are in
[guildmatchrank](guildmatchrank_bss.md), the rewards in
[guildmatchoption](guildmatchoption_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `guildmatchexp.bss` | 828   | 2 Row   | 404       |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 1      | `guildmatchexp.bss` | 828 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `2` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row; no key                               |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 4 bytes + values)

| Offset  | Type              | Field       | Notes                                                       |
| ------- | ----------------- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u32               | level_count | Number of values; `100` on every client checked             |
| `+0x04` | u32[level_count]  | combat_exp  | Combat EXP for character level `N + 1` at position `N`      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it.
`combat_exp` follows the two reward items of clients 2519 to 3251 in
[guildmatchoption](guildmatchoption_bss.md): Guild League Victory Combat
EXP (56276) and Guild League Defeat Combat EXP (56277), whose LOC texts
read "Gain a certain amount of Combat EXP according to level for winning
(losing) in the Guild League". 100 values per row fit one per level, and
the values fall from level 41 on and reach their floor of `31` at level 68
(client 3251), which fits EXP by level; the EXP items' LOC text adds "EXP
gained diminishes from Lv. 60".

## Notes

- Clients 2519 to 3474 have the same 828 bytes, and clients 3002 and 3251
  the same values. Client 2519 matches them on levels 1 to 20 and 68 to
  100 only and is lower in between (row 0 at level 60 is 11,360 against
  49,200 on client 3251).
- Client 3474 replaced the two EXP items in the reward lists of
  [guildmatchoption](guildmatchoption_bss.md) and zeroed every value here.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`, each row's 100 values in one cell.

## Open Questions

### Which Row Is the Victory

Row 1 is higher than row 0 at every level where both are above `31`,
which fits row 1 as the victory EXP and row 0 as the defeat EXP. Nothing
in the file or the Lua names the rows.
