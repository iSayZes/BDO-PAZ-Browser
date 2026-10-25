# `*.luac` Lua Script Format

## Purpose

Every `.luac` file is one client UI script compiled to standard Lua 5.1
bytecode: a 12-byte header, then the main function, which holds its
constants and its nested functions. On client 3473, 3,073 of them ship. The
main function's `source` is the script's path on the developers' machine
(`@d:/bdo/pc_alpha/dev/ui_data\script\window\exchange\panel_window_barterinfosearch_2.lua`),
so every script names its UI folder. `tools/unluac/unluac.jar` decompiles
them back to Lua source.

A script that a table doc relies on gets its own doc in this folder, written
when a table task reads it: what the script calls in client data and which
table fields those calls read (see Script Docs). This doc covers the bytes
every script shares.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

None. A script calls into client data through `ToClient_*` functions and
wrapper objects; the script docs list those calls.

## Layout 1

### File Layout

| Offset  | Type     | Field            | Notes                                                        |
| ------- | -------- | ---------------- | ------------------------------------------------------------ |
| `+0x00` | char[4]  | signature        | `1B 4C 75 61`, ESC then `Lua`                                |
| `+0x04` | u8       | version          | `0x51`, Lua 5.1                                              |
| `+0x05` | u8       | format           | `0`, the official format                                     |
| `+0x06` | u8       | endianness       | `1`, little-endian                                           |
| `+0x07` | u8       | int_size         | `4`: counts and line numbers are 4 bytes                     |
| `+0x08` | u8       | size_t_size      | `8`: string lengths are 8 bytes, so strings read as `str8`   |
| `+0x09` | u8       | instruction_size | `4`                                                          |
| `+0x0A` | u8       | number_size      | `8`: numbers are `f64`                                       |
| `+0x0B` | u8       | is_integral      | `0`: numbers are floating point                              |
| `+0x0C` | Function | main             | The main chunk                                               |

### Function (variable: 44 bytes + source text, code, constants, functions, debug info)

| Offset                | Type                              | Field              | Notes                                                                   |
| --------------------- | --------------------------------- | ------------------ | ----------------------------------------------------------------------- |
| `+0x00`               | str8                              | source             | Count includes the closing `0` byte; the script path on `main`, count `0` (no text) on nested functions |
| `source+0x00`         | i32                               | line_defined       | Source line the function starts on; `0` on `main`                       |
| `source+0x04`         | i32                               | last_line_defined  | Source line it ends on; `0` on `main`                                   |
| `source+0x08`         | u8                                | upvalue_count      |                                                                         |
| `source+0x09`         | u8                                | param_count        |                                                                         |
| `source+0x0A`         | u8                                | is_vararg          | Flag bits; `main` has `2` (vararg)                                      |
| `source+0x0B`         | u8                                | max_stack_size     | Registers the function uses                                             |
| `source+0x0C`         | u32                               | code_count         |                                                                         |
| `source+0x10`         | u32[code_count]                   | code               | Lua 5.1 instructions, opcode in the low 6 bits                          |
| `code+0x00`           | u32                               | constant_count     |                                                                         |
| `code+0x04`           | Constant[constant_count]          | constants          | Strings here are the names of the globals, fields and `ToClient_*` functions it calls |
| `constants+0x00`      | u32                               | function_count     |                                                                         |
| `constants+0x04`      | Function[function_count]          | functions          | Nested functions, each the same structure                               |
| `functions+0x00`      | u32                               | line_info_count    | `code_count`, or `0` when debug info is stripped                        |
| `functions+0x04`      | i32[line_info_count]              | line_info          | Source line of each instruction                                         |
| `line_info+0x00`      | u32                               | local_count        |                                                                         |
| `line_info+0x04`      | Local[local_count]                | locals             |                                                                         |
| `locals+0x00`         | u32                               | upvalue_name_count |                                                                         |
| `locals+0x04`         | Upvalue Name[upvalue_name_count]  | upvalue_names      |                                                                         |

### Constant (variable: 1 byte + value)

| Offset                | Type             | Field         | Notes                                   |
| --------------------- | ---------------- | ------------- | --------------------------------------- |
| `+0x00`               | u8               | type          | `0` nil, `1` boolean, `3` number, `4` string |
| `+0x01`               | u8 if type = 1   | boolean_value | `0` false, `1` true                     |
| `boolean_value+0x00`  | f64 if type = 3  | number_value  |                                         |
| `number_value+0x00`   | str8 if type = 4 | string_value  | Count includes the closing `0` byte     |

### Local (variable: 16 bytes + name text)

| Offset        | Type | Field    | Notes                                     |
| ------------- | ---- | -------- | ----------------------------------------- |
| `+0x00`       | str8 | name     | Local variable name                       |
| `name+0x00`   | i32  | start_pc | First instruction where the local is live |
| `name+0x04`   | i32  | end_pc   | Instruction where it goes out of scope    |

### Upvalue Name (variable: 8 bytes + name text)

| Offset  | Type | Field | Notes        |
| ------- | ---- | ----- | ------------ |
| `+0x00` | str8 | name  | Upvalue name |

## Script Docs

A script doc is named after the script (`panel_window_barterinfosearch_2_luac.md`)
and written while a table task reads that script, never as a sweep. Its
sections, in order:

| Section                     | Content                                                                 |
| --------------------------- | ----------------------------------------------------------------------- |
| `## Purpose`                | Which UI the script drives, and its `source` folder                     |
| `## Calls Into Client Data` | A table: Call, what the script does with it, the format doc field it reads, the client checked |
| `## Enums Used`             | `CppEnums.*` values the script compares against, and what they select; omitted when empty |
| `## Versions`               | The client the script first ships on, and the clients where a call a doc relies on appears or changes |
| `## Open Questions`         | One `###` per question; omitted when empty                              |

A call goes into the table only when it is traced to a field; a guess gets
a `?` after the field and its question under Open Questions. The table doc's
Field Names links the script doc that confirmed a field.

## Notes

- The client Lua is unmodified Lua 5.1 bytecode with debug info, so
  `unluac` restores names of locals and the call shape (which wrapper a
  getter is called on, which arguments a `ToClient_*` function takes).
- `browser.py --file "*.luac" --output <folder>` extracts every script; a
  claim that no script reads something needs all of them, not a subset.
