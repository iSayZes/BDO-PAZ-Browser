# `rosewarfiercebattlenodestaticstatus.bss` Format

## Purpose

The links between the Rose War sanctums: one row per fierce battle key with
four u64-counted lists of fierce battle keys, the key itself last. The
first two lists hold the neighbouring sanctums toward the Kamasylvia end
(sanctum `1`) and toward the O'dyllita end (sanctum `11`). On client 3474
sanctums `1` to `7` and `11` to `17` form two lanes per side that meet at
`4`, `7`, `14` and `17`; `8` to `10`, `18` to `20` and the gimmick
sanctums `21` and `22` have empty lists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ------- | ----------------------- |
| 1      | 3002 and later | 3474    | `rosewarfiercebattlenodestaticstatus.bss` | 880   | 22 Row  | 34 to 44, 39 on average |

| Layout | File                                      | Known         | Unknown       |
| ------ | ----------------------------------------- | ------------- | ------------- |
| 1      | `rosewarfiercebattlenodestaticstatus.bss` | 480 B (54.5%) | 400 B (45.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 34 bytes + key lists)

| Offset                      | Type                              | Field                     | Notes                                                                        |
| --------------------------- | --------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| `+0x00`                     | u64                               | kamasylvia_side_key_count | Number of `kamasylvia_side_keys`                                             |
| `+0x08`                     | u16[kamasylvia_side_key_count]    | kamasylvia_side_keys      | Linked sanctums one step toward sanctum `1`; empty on sanctum `1`            |
| `kamasylvia_side_keys+0x00` | u64                               | odyllita_side_key_count   | Number of `odyllita_side_keys`                                               |
| `kamasylvia_side_keys+0x08` | u16[odyllita_side_key_count]      | odyllita_side_keys        | Linked sanctums one step toward sanctum `11`; empty on sanctum `11`          |
| `odyllita_side_keys+0x00`   | u64                               | unknown_list_3_count      | Number of `unknown_list_3`                                                   |
| `odyllita_side_keys+0x08`   | u16[unknown_list_3_count]         | unknown_list_3            | One key of `odyllita_side_keys`, or empty; see Open Questions                |
| `unknown_list_3+0x00`       | u64                               | unknown_list_4_count      | Number of `unknown_list_4`                                                   |
| `unknown_list_3+0x08`       | u16[unknown_list_4_count]         | unknown_list_4            | One key of `kamasylvia_side_keys`, or empty                                  |
| `unknown_list_4+0x00`       | u16                               | fierce_battle_key         | The sanctum the row is for, as in the monster table                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Sanctum Links

Client 3474, by `fierce_battle_key`:

| Key  | `kamasylvia_side_keys` | `odyllita_side_keys` | `unknown_list_3` | `unknown_list_4` |
| ---- | ---------------------- | -------------------- | ---------------- | ---------------- |
| `1`  |                        | `2`, `5`             |                  |                  |
| `2`  | `1`                    | `3`                  | `3`              | `1`              |
| `3`  | `2`                    | `4`                  | `4`              | `2`              |
| `4`  | `3`                    | `14`, `17`           | `14`             | `3`              |
| `5`  | `1`                    | `6`                  | `6`              | `1`              |
| `6`  | `5`                    | `7`                  | `7`              | `5`              |
| `7`  | `6`                    | `14`, `17`           | `17`             | `6`              |
| `11` | `12`, `15`             |                      |                  |                  |
| `12` | `13`                   | `11`                 | `11`             | `13`             |
| `13` | `14`                   | `12`                 | `12`             | `14`             |
| `14` | `4`, `7`               | `13`                 | `13`             | `4`              |
| `15` | `16`                   | `11`                 | `11`             | `16`             |
| `16` | `17`                   | `15`                 | `15`             | `17`             |
| `17` | `4`, `7`               | `16`                 | `16`             | `7`              |

Every link points both ways: a key in another row's `odyllita_side_keys`
has that row's key in its own `kamasylvia_side_keys`, and back.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. `fierce_battle_key` matches
the keys of [`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md),
whose keys `1` to `10` are the Kamasylvia side sanctums (`ElfWar_Kama_N1`
to `N10` images) and `11` to `20` the O'dyllita side ones (`ElfWar_Odyl_S1`
to `S10`). The first two lists are named by the side their keys lie on:
on every linked row the first list leads toward sanctum `1` and the second
toward sanctum `11`.

## Notes

- Client 3002 links all 20 sanctums in three lanes per side: sanctum `1`
  opens to `2`, `5` and `8`, sanctum `11` to `12`, `16` and `19`, and the
  lanes cross at `4`, `7`, `10`, `15`, `18` and `20` (940 bytes). Clients
  3251 and 3474 have the two-lane graph above (880 bytes). The file is not
  in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the key first.

## Open Questions

### The Third and Fourth Lists

`unknown_list_3` holds one key of `odyllita_side_keys` and `unknown_list_4`
one key of `kamasylvia_side_keys` on every linked row except the two end
sanctums, where both are empty. Where a row has two neighbours on a side,
the pick does not follow the key order (`4` takes `14`, `7` takes `17`,
`17` takes `7`). The revive window checks `canRevive()` per sanctum, and the
lists may be the path a team must hold to revive there, but no Lua reads
them.
