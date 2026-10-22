# `instancedungeonskillinfo.bss` Format

## Purpose

Skills of an instance dungeon mode, per class type: each class row holds
20 lists of skill keys, and a table after the rows gives some of those
skills a short list of byte values. Client 1784 fills 10 class rows
(class types 16 to 25) with 255 skills; client 3482 ships every list
empty and the table with no entries.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                                         | Row bytes             |
| ------ | -------------- | ------- | ------------------------------ | ------ | ----------------------------------------------- | --------------------- |
| 3      | 3474 and later | 3482    | `instancedungeonskillinfo.bss` | 15,540 | 1,940 Skill List, 97 Class Row                  | 8                     |
| 2      | 2313 to 3251   | 3251    | `instancedungeonskillinfo.bss` | 13,940 | 1,740 Skill List, 87 Class Row                  | 8                     |
| 1      | 1636 to 2107   | 2107    | `instancedungeonskillinfo.bss` | 15,715 | 1,640 Skill List, 82 Class Row, 166 Skill Entry | 8 to 20, 9 on average |

| Layout | File                           | Known             | Unknown        |
| ------ | ------------------------------ | ----------------- | -------------- |
| 3      | `instancedungeonskillinfo.bss` | 15,540 B (100.0%) | 0 B (0.0%)     |
| 2      | `instancedungeonskillinfo.bss` | 13,940 B (100.0%) | 0 B (0.0%)     |
| 1      | `instancedungeonskillinfo.bss` | 14,552 B (92.6%)  | 1,163 B (7.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 3             |
| 3474   | Layout 3             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2765   | Layout 2             |
| 2637   | Layout 2             |
| 2519   | Layout 2             |
| 2313   | Layout 2             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | No documented layout |
| 1348   | No documented layout |
| 1230   | No documented layout |
| 1156   | No documented layout |
| 1058   | No file              |
| 911    | No file              |
| 794    | No file              |
| 606    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10.
[`instancedungeonskillstatic.dbss`](instancedungeonskillstatic_dbss.md)
holds a Korean text for 157 of the 255 skills of client 1784.

All multi-byte values are little-endian.

## Layout 3

### File Layout

The file stores no class row count; see Open Questions.

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[97]                    | rows              | Row `n` is class type `n`; see Class Row        |
| `rows+0x00`          | u32                              | skill_entry_count | Number of `skill_entries`; `0` on client 3482   |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

### Class Row (variable: 0 bytes + lists)

| Offset  | Type            | Field       | Notes                                 |
| ------- | --------------- | ----------- | ------------------------------------- |
| `+0x00` | Skill List[20]  | skill_lists | Lists 0 to 19 in order; see Skill List |

### Skill List (variable: 8 bytes + keys)

| Offset  | Type                   | Field           | Notes                                                    |
| ------- | ---------------------- | --------------- | -------------------------------------------------------- |
| `+0x00` | u64                    | skill_key_count | Number of keys; `0` for an empty list                    |
| `+0x08` | u32[skill_key_count]   | skill_keys      | Skill keys `skill_no << 16 \| level`, level `1` on client 1784 |

### Skill Entry (variable: 8 bytes + values)

| Offset  | Type              | Field      | Notes                                                       |
| ------- | ----------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u16               | skill_no   | A skill of the lists, LOC type `10`                         |
| `+0x02` | u16               | unknown_02 | `1` on every entry of client 1784                           |
| `+0x04` | u32               | unknown_04 | Number of `unknown_08` values; `1` or `2`                   |
| `+0x08` | u8[unknown_04]    | unknown_08 | `2` (127 entries) or `3` (38) on client 1784; one entry holds `1, 2` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482          |
| `+0x04` | pstr[string_count] | strings      | No field reads a string               |

## Layout 2

87 class rows.

### File Layout

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[87]                    | rows              | Row `n` is class type `n`                       |
| `rows+0x00`          | u32                              | skill_entry_count | Number of `skill_entries`                       |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

## Layout 1

82 class rows.

### File Layout

| Offset               | Type                             | Field             | Notes                                           |
| -------------------- | -------------------------------- | ----------------- | ----------------------------------------------- |
| `+0x00`              | char[4]                          | magic             | `PABR`                                          |
| `+0x04`              | Class Row[82]                    | rows              | Row `n` is class type `n`                       |
| `rows+0x00`          | u32                              | skill_entry_count | `166` on client 1784                            |
| `rows+0x04`          | Skill Entry[skill_entry_count]   | skill_entries     | See Skill Entry                                 |
| `skill_entries+0x00` | String Table                     | string_table      | See String Table                                |
| `string_table+0x00`  | u32                              | table_start       | Offset of the string table                      |
| `string_table+0x04`  | u32                              | zero              | Always `0`                                      |

## Field Names

No sheet of the private server's `DataSheets.bexcel` on client 1784 and no
2016 struct has this shape, so only the skill fields are named, by value:
every list key is a skill key whose skill number has a LOC type 10 name,
and every entry's `skill_no` is a skill of the lists (166 of 166 on client
1784). The two halves store a skill differently: a list key has the skill
number in the high half (`01 00 9F 42`, skill 17055 level 1), an entry the
skill number first (`AD 44 01 00`, skill 17581, then `1`).

## Notes

- On client 1784 the filled lists are lists 0 to 3, 8 to 13, 18 and 19 of
  class rows 16 to 25: 110 lists, 80 of three keys and 30 of one.
- All 157 keys of the client 1784 `instancedungeonskillstatic.dbss` are
  skills of these lists. That file is empty from client 2519 on.
- The `InstanceDungeonPcStat` sheet of the same private server indexes its
  32 rows the same way (`0` `F0 파이터`, `4` `E0 레인저`, `16` `P0 금수랑`,
  `24` `K0 발키리`, `28` `N0 백마법사`), four rows per class letter.

## Open Questions

### What Fixes the Class Row Count

The file stores no row count. The rows are 82 on clients 1636 to 2107, 87
on clients 2313 to 3251 and 97 from client 3474, each time the row count
of [`skillquickslotinfo.bss`](skillquickslotinfo_bss.md) of the same
client. Clients 1156 to 1485 fit no layout. On 1348 and 1485 the file is 9,155 bytes,
6,560 (1,640 x 4) shorter than the 15,715 of client 1784 with the same
1,751 non-zero bytes before the string table, so the 1,640 lists of 82
rows may have u32 counts there. The parser reads the newest layout's 97 and fails when the entry table does
not then end at `table_start`.

### What the 20 Lists and the Entry Values Mean

Twenty matches the slot count of the 2016 `gc::QuickSlot`, so a list may
be the skills of one quick slot, but no Lua of client 3482 reads the file.
The entry values `2` and `3` are unknown.
