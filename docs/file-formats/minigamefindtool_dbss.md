# `minigamefindtool.dbss` Format

## Purpose

The hoe values of the Lakiaro digging minigame
([`minigamefind.bss`](minigamefind_bss.md)): one 9-byte row per hoe item
grade and enhancement level (+0 to PEN), with the number of right clicks,
the slots a click opens and a damage rate. The client Lua asks the table for
the right clicks of the equipped hoe through
`ToClient_MiniGameFindMaxRClickCount(grade, enchantLevel)`. On client 3482
the file holds six grades (0 to 5) of 21 levels each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ---------------------------- | --------- |
| 2      | 2765 and later | 3482    | `minigamefindtool.dbss`       | 1,140 | 126 Level Row, 6 Grade Block | 9         |
| 2      | 2765 and later | 3482    | `minigamefindtooloffset.dbss` | 1,158 | 126 Index Row, 6 Index Group | 9         |
| 1      | 1348 to 2519   | 2519    | `minigamefindtool.dbss`       | 945   | 105 Level Row, 5 Grade Block | 9         |
| 1      | 1348 to 2519   | 2519    | `minigamefindtooloffset.dbss` | 965   | 105 Index Row, 5 Index Group | 9         |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 2      | `minigamefindtool.dbss`       | 1,134 B (99.5%)  | 6 B (0.5%) |
| 2      | `minigamefindtooloffset.dbss` | 1,158 B (100.0%) | 0 B (0.0%) |
| 1      | `minigamefindtool.dbss`       | 945 B (100.0%)   | 0 B (0.0%) |
| 1      | `minigamefindtooloffset.dbss` | 965 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
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

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `minigamefindtooloffset.dbss` | Optional | `(item grade, enchant_level) -> (data_offset, data_size)`; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No count and no `PABR` magic: grade blocks back to back up to the end of the
file. Block `i` holds item grade `i`; the file stores no grade field.

| Offset  | Type               | Field  | Notes                                     |
| ------- | ------------------ | ------ | ----------------------------------------- |
| `+0x00` | Grade Block[..end] | blocks | One block per item grade; see Grade Block |

On client 3482 the file is 6 x 190 = 1,140 bytes.

### Grade Block (190 bytes)

| Offset  | Type          | Field      | Notes                                                   |
| ------- | ------------- | ---------- | ------------------------------------------------------- |
| `+0x00` | u8            | unknown_00 | `1` in every block (client 3482); see Open Questions    |
| `+0x01` | Level Row[21] | rows       | Enhancement levels 0 to 20, in order; see Level Row     |

The block holds 21 rows on every client read; the index gives the count
(`row_count`), the main file does not.

### Level Row (9 bytes)

| Offset  | Type | Field                | Notes                                                        |
| ------- | ---- | -------------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | r_click_count        | Right clicks the hoe allows: `10` to `28` on client 3482      |
| `+0x04` | u8   | open_slot_count      | `1` to `9` on client 3482                                    |
| `+0x05` | u32  | decrease_damage_rate | `20000` to `1000000` on client 3482                          |

### `minigamefindtooloffset.dbss`

Index into `minigamefindtool.dbss` with the same blocks, no magic and no
trailer.

| Offset  | Type               | Field  | Notes                                       |
| ------- | ------------------ | ------ | ------------------------------------------- |
| `+0x00` | Index Group[..end] | groups | Group `i` holds item grade `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                               |
| ------- | -------------------- | --------- | ----------------------------------- |
| `+0x00` | u32                  | row_count | `21` in every group (client 3482)    |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                       |

### Index Row (9 bytes)

| Offset  | Type | Field         | Notes                                                 |
| ------- | ---- | ------------- | ----------------------------------------------------- |
| `+0x00` | u8   | enchant_level | Row key together with the group index: `0` to `20`    |
| `+0x01` | u32  | data_offset   | Start of the Level Row in `minigamefindtool.dbss`     |
| `+0x05` | u32  | data_size     | `9` on every row, the Level Row size                  |

On client 3482 every index row points at the main row of its grade and
level, in file order, and the first row of a block sits one byte past the
block start, after `unknown_00`.

## Layout 1

The grade block has no leading u8: 21 rows and nothing else. On client 1784
the file holds five grades (0 to 4), 5 x 189 = 945 bytes, and the index
points at `0x00` for the first row.

### Grade Block (189 bytes)

| Offset  | Type          | Field | Notes                                |
| ------- | ------------- | ----- | ------------------------------------ |
| `+0x00` | Level Row[21] | rows  | Enhancement levels 0 to 20, in order |

## Field Names

The rows are the `MiniGameFindToolData` sheet of a private server's
`DataSheets.bexcel` on client 1784, keyed by `ItemGrade` and
`EnchantLevel` (105 rows, grades 0 to 4). The group index is `ItemGrade` and
the index key `EnchantLevel`; `r_click_count`, `open_slot_count` and
`decrease_damage_rate` match `RClickCount`, `OpenSlotCount` and
`DecreaseDamageRate` on 105 of 105 keys on clients 1784 and 3482. Grade 5
(client 3482 only) has no sheet rows.

The minigame window Lua (`panel_minigame_find_all_1`, `updateValue`) passes
the equipped hoe's `getGradeType()` and, when its durability is not 0, its
enchant level to `ToClient_MiniGameFindMaxRClickCount` and shows the result
less the clicks used as the right clicks left.

## Notes

- On client 3482 grades 0 and 1 hold `10` right clicks, `2` open slots and
  `210000` on every level except grade 0 +0 (`22`, `7`, `600000`). In
  grades 2 to 5 the right clicks rise from `10` (+0 to +9) to `22` (grade
  2) or `28` (grades 3 to 5) at PEN. Grades 4 and 5 hold the same 21 rows;
  grade 3 differs from them at +0 only (`9` open slots, `1000000`).

## Open Questions

### What the Grade Block's Leading u8 Holds

`unknown_00` is `1` in all six blocks of client 3482. Client 1784 has no
such byte, and the sheet no column for it.
