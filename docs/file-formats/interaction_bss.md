# `interaction.bss` Format

## Purpose

Interactions set on single characters, one row per interaction: the
interaction type, a value the interaction executes and the character key. On client
3474 the file has 2 rows, both `InteractionType_Awake` (`61`) on the two
Mirumok Offin characters (`23751` Mirumok Watcher Offin, `23767` Mirumok
Destroyer Offin) with the value `40414`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------- | --------- |
| 1      | 1230 and later | 3474    | `interaction.bss` | 42    | 2 Row   | 11        |

| Layout | File              | Known        | Unknown    |
| ------ | ----------------- | ------------ | ---------- |
| 1      | `interaction.bss` | 40 B (95.2%) | 2 B (4.8%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (11 bytes)

| Offset  | Type | Field            | Notes                                                                    |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | interaction_type | `CppEnums.InteractionType` value; see Interaction Types                   |
| `+0x04` | u8   | unknown_04       | `0` on every row; see Open Questions                                     |
| `+0x05` | u32  | execute          | `40414` on every row; see Notes                                          |
| `+0x09` | u16  | character_key    | `characterstatic.dbss` key; the handler shows its LOC type 6 name         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Interaction Types

`interaction_type` is the client's `CppEnums.InteractionType`
(`global_define_cpp_enum.luac`, client 3474), `InteractionType_GamePlay`
`0` to `InteractionType_ImmediatelySwapCharacter` `76`. The only value in
the file:

| Value | Lua name                |
| ----- | ----------------------- |
| `61`  | `InteractionType_Awake` |

## Field Names

The names follow the `Interaction_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_Interaction.xlsm`: `InteractionType`, `Condition`, `Excute` and
`CharacterKey`, in this order. Its 2 rows (`61`, `<NULL>`, `40414`,
`23751` and `61`, `<NULL>`, `40414`, `23767`) equal the 2 rows of the
client 1784 file value by value, and the client 1784 file is byte for byte
the private server's compiled `binary/interaction.bss`. `execute` spells
out the sheet's `Excute`. The `Condition` column is `<NULL>` on both rows,
so no value shows where it sits; `unknown_04` stays unnamed. The column
comments in the workbook belong to another sheet (`0: 퀘스트 전용`, a
dungeon and a desert prison).

## Notes

- Raw bytes on clients 1230 to 3474:
  `50 41 42 52 02 00 00 00 3D 00 00 00 00 DE 9D 00 00 C7 5C 3D 00 00 00 00 DE 9D 00 00 D7 5C 00 00 00 00 1E 00 00 00 00 00 00 00`
  (42 bytes). The file is not in the archives of client 794.
- `40414` is the item "[Guild] Ancient Contract: Mirumok Watcher" (LOC type
  0) and the skill "Final Damage 400%+Debuff" (LOC type 10, `skill.dbss`
  skill 40414 level 1). The `charactersimply.bss` interaction condition of
  both characters is `getitemcount(40414,0)>0;` (see
  [charactersimply](charactersimply_bss.md)), so the interaction needs that
  item. Whether `execute` is the item or the skill is open.
- The server dump on client 1784 holds the column names `InteractionType`
  and `Excute` next to the error `인터렉션 정보를 등록할 수 없습니다!` ("cannot
  register the interaction info").
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, one row
  per row of the file.

## Open Questions

### Where the Condition Sits

The first five bytes of each row are `3D 00 00 00 00`. They read as a u32
`interaction_type` and a u8 `unknown_04`, or as a u8 `interaction_type`
and a u32. The sheet's `Condition` column is `<NULL>` on both rows, so the
data shows neither its width nor whether a condition is stored here at
all; a PABR string reference would point into the string table, which is
empty.

### What Execute Points At

`execute` is `40414` on both rows, the key of both an item ("[Guild]
Ancient Contract: Mirumok Watcher") and a skill ("Final Damage
400%+Debuff"). The characters' interaction condition checks for the item,
which points to the item; no client Lua reads the value.
