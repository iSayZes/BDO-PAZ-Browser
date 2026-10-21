# `specialemployeeinfostaticstatus.dbss` Format

## Purpose

The special sailors: one row per sailor that is hired with an item of its
own instead of the Sailor Contract Certificate of the port sailors in
[`employeespawninfo.dbss`](employeespawninfo_dbss.md). Each row holds the
sailor character, the item and count the hire takes, the success rate and
the Korean lines the sailor says when hired and when it refuses. Client
3474 has three: Arkahn (`59101`, Proix's Old Compass), Hetario (`59227`)
and Pacuna (`59228`). Companion
`specialemployeeinfostaticstatusoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes | Records                      | Row bytes                 |
| ------ | -------------- | ------- | -------------------------------------------- | ----- | ---------------------------- | ------------------------- |
| 1      | 1485 and later | 3474    | `specialemployeeinfostaticstatus.dbss`       | 391   | 3 Row, 2 Group               | 87 to 187, 128 on average |
| 1      | 1485 and later | 3474    | `specialemployeeinfostaticstatusoffset.dbss` | 42    | 3 Offset Row, 2 Offset Group | 10                        |

| Layout | File                                         | Known         | Unknown     |
| ------ | -------------------------------------------- | ------------- | ----------- |
| 1      | `specialemployeeinfostaticstatus.dbss`       | 379 B (96.9%) | 12 B (3.1%) |
| 1      | `specialemployeeinfostaticstatusoffset.dbss` | 42 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                                |
| ------------------------------------------------- | -------- | ------------------------------------------------------------------- |
| `specialemployeeinfostaticstatusoffset.dbss`      | Optional | `type -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |
| `languagedata_en.loc`                             | Optional | Sailor names (LOC type `6`) and item names (LOC type `0`)            |

LOC type 70, which holds the lines of the port sailors, has no lines for
these three characters on client 3474; the handler shows the inline
Korean text.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                                     |
| ------- | ------------ | ------ | --------------------------------------------------------- |
| `+0x00` | Group[..end] | groups | Back to back to the end of the file; see Group            |

The file has no group count; `specialemployeeinfostaticstatusoffset.dbss`
stores it. Client 3474 has two groups, the second empty (its count `0` is
the last 4 bytes of the file); client 1784 has one.

### Group (variable: 4 bytes + rows)

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows in the group           |
| `+0x04` | Row[count] | rows  | See Row                               |

### Row (variable: 41 bytes + line text)

| Offset                       | Type  | Field                          | Notes                                                                 |
| ---------------------------- | ----- | ------------------------------ | --------------------------------------------------------------------- |
| `+0x00`                      | u8    | category                       | `0` on every row of clients 1784 and 3474                              |
| `+0x01`                      | u16   | type                           | Row key, `21` to `23` on client 3474; see Open Questions               |
| `+0x03`                      | u16   | character_key                  | The sailor character                                                  |
| `+0x05`                      | u32   | need_item_key                  | Item the hire takes (LOC type `0`)                                    |
| `+0x09`                      | u64   | need_item_count                | `1` on every row of client 3474                                       |
| `+0x11`                      | u32   | employ_success_rate            | Out of 1,000,000; `1000000` (100%) on every row of client 3474         |
| `+0x15`                      | str16 | employ_success_word_kr         | Korean line when the sailor is hired; real line breaks (`0x0A`)        |
| `employ_success_word_kr+0x00` | str16 | employ_fail_word_kr            | Korean line when the hire fails                                       |
| `employ_fail_word_kr+0x00`   | u32   | unknown_employ_fail_word_kr_00 | `0` on every row of clients 1784 and 3474; the row ends after it       |

### `specialemployeeinfostaticstatusoffset.dbss`

Offset table into `specialemployeeinfostaticstatus.dbss` with a group
count before the same groups (no PABR magic, no trailer).

| Offset  | Type                       | Field       | Notes                                                    |
| ------- | -------------------------- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                        | group_count | Number of groups; `2` on client 3474, `1` on client 1784 |
| `+0x04` | Offset Group[group_count]  | groups      | See Offset Group                                         |

### Offset Group (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes                                                    |
| ------- | ----------------- | ----- | -------------------------------------------------------- |
| `+0x00` | u32               | count | Equals the `count` of the same group in the main file    |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                           |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                           |
| ------- | ---- | ----------- | --------------------------------------------------------------- |
| `+0x00` | u16  | type        | Key of the row it points at                                     |
| `+0x02` | u32  | data_offset | Absolute offset of the row in the main file, at `category`      |
| `+0x06` | u32  | data_size   | Row size in bytes, `category` to `unknown_employ_fail_word_kr_00` |

The index rows are in file order; on clients 1784 and 3474 every index
row points at the row with its type, and the rows and group counts fill
the main file.

## Field Names

The `SpecialEmployee_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Category`, `Type`, `CharacterKey`,
`ActionIndex`, `EmploySuccessRate`, `NeedItemKey`, `NeedItemCount`,
`EmploySuccessWord` and `EmployFailWord`. Its three rows match the file on
all three types and on every column but `ActionIndex`, on client 1784 and
on client 3474; the file stores the columns in its own order. `Category`
is `0` on every row of the sheet and the file, so `category` rests on the
column order alone. `ActionIndex` holds the same values as `Type` (`21` to
`23`), so it has no field of its own in the file, or it is the field named
`type` here. No client Lua names the table, and the 2016 client's debug
symbols have no struct for it.

## Notes

- The row tail matches the hire block of
  [`employeespawninfo.dbss`](employeespawninfo_dbss.md): an item key, a u64
  count, a u32 `1000000`, two Korean lines and a u32 `0`. There the
  `1000000` before the lines is `unknown_28`.
- The hire items of Hetario (`65623`) and Pacuna (`65622`) are named
  `NO USE` in LOC type 0 on client 3474; their descriptions call them a
  fishing rod of the Otters and a honey jar of the Papus.

## Open Questions

### Type or ActionIndex

The u16 at `+0x01` holds `21`, `22` and `23`, the values of both the
`Type` and the `ActionIndex` column of the sheet. A row where the two
differ would show which one the file keeps.

### What the Groups Are

Client 3474 adds a second, empty group that client 1784 does not have.
The groups may split the rows by `category`: every row is in the first
group and has `category` `0`. A row with another category would test it.
