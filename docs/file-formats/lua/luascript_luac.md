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

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                   | Bytes   | Records                                                 | Row bytes              |
| ------ | -------------- | -------------------------------------- | ------- | ------------------------------------------------------- | ---------------------- |
| 1      | 2134 and later | `panel_tooltip_item.luac`              | 245,350 | 2,146 Constant, 836 Local, 41 Function, 88 Upvalue Name | 1 to 70, 27 on average |
| 1      | 2134 and later | `panel_window_barterinfosearch_2.luac` | 51,932  | 807 Constant, 47 Function, 224 Local                    | 1 to 82, 27 on average |
| 1      | 2134 and later | `panel_window_inventory_all_4.luac`    | 82,107  | 1,243 Constant, 53 Function, 219 Local, 6 Upvalue Name  | 1 to 81, 29 on average |

| Layout | File                                   | Known              | Unknown    |
| ------ | -------------------------------------- | ------------------ | ---------- |
| 1      | `panel_tooltip_item.luac`              | 245,350 B (100.0%) | 0 B (0.0%) |
| 1      | `panel_window_barterinfosearch_2.luac` | 51,932 B (100.0%)  | 0 B (0.0%) |
| 1      | `panel_window_inventory_all_4.luac`    | 82,107 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `22e3c7b99082`  |
| 3482   | Layout 1 | `22e3c7b99082`  |
| 3474   | Layout 1 | `22e3c7b99082`  |
| 3473   | Layout 1 | `22e3c7b99082`  |
| 3464   | Layout 1 | `22e3c7b99082`  |
| 3458   | Layout 1 | `22e3c7b99082`  |
| 3454   | Layout 1 | `22e3c7b99082`  |
| 3444   | Layout 1 | `22e3c7b99082`  |
| 3435   | Layout 1 | `22e3c7b99082`  |
| 3426   | Layout 1 | `22e3c7b99082`  |
| 3418   | Layout 1 | `22e3c7b99082`  |
| 3412   | Layout 1 | `22e3c7b99082`  |
| 3402   | Layout 1 | `22e3c7b99082`  |
| 3396   | Layout 1 | `22e3c7b99082`  |
| 3387   | Layout 1 | `22e3c7b99082`  |
| 3381   | Layout 1 | `22e3c7b99082`  |
| 3373   | Layout 1 | `22e3c7b99082`  |
| 3364   | Layout 1 | `22e3c7b99082`  |
| 3356   | Layout 1 | `22e3c7b99082`  |
| 3349   | Layout 1 | `22e3c7b99082`  |
| 3342   | Layout 1 | `22e3c7b99082`  |
| 3335   | Layout 1 | `22e3c7b99082`  |
| 3326   | Layout 1 | `22e3c7b99082`  |
| 3321   | Layout 1 | `22e3c7b99082`  |
| 3314   | Layout 1 | `22e3c7b99082`  |
| 3303   | Layout 1 | `22e3c7b99082`  |
| 3302   | Layout 1 | `22e3c7b99082`  |
| 3293   | Layout 1 | `22e3c7b99082`  |
| 3283   | Layout 1 | `22e3c7b99082`  |
| 3275   | Layout 1 | `22e3c7b99082`  |
| 3267   | Layout 1 | `22e3c7b99082`  |
| 3258   | Layout 1 | `22e3c7b99082`  |
| 3251   | Layout 1 | `22e3c7b99082`  |
| 3242   | Layout 1 | `22e3c7b99082`  |
| 3235   | Layout 1 | `22e3c7b99082`  |
| 3229   | Layout 1 | `22e3c7b99082`  |
| 3212   | Layout 1 | `22e3c7b99082`  |
| 3203   | Layout 1 | `22e3c7b99082`  |
| 3193   | Layout 1 | `22e3c7b99082`  |
| 3186   | Layout 1 | `22e3c7b99082`  |
| 3177   | Layout 1 | `22e3c7b99082`  |
| 3169   | Layout 1 | `22e3c7b99082`  |
| 3158   | Layout 1 | `22e3c7b99082`  |
| 3151   | Layout 1 | `22e3c7b99082`  |
| 3144   | Layout 1 | `22e3c7b99082`  |
| 3133   | Layout 1 | `22e3c7b99082`  |
| 3125   | Layout 1 | `22e3c7b99082`  |
| 3118   | Layout 1 | `22e3c7b99082`  |
| 3111   | Layout 1 | `22e3c7b99082`  |
| 3103   | Layout 1 | `22e3c7b99082`  |
| 3095   | Layout 1 | `22e3c7b99082`  |
| 3086   | Layout 1 | `22e3c7b99082`  |
| 3072   | Layout 1 | `22e3c7b99082`  |
| 3062   | Layout 1 | `22e3c7b99082`  |
| 3052   | Layout 1 | `22e3c7b99082`  |
| 3045   | Layout 1 | `22e3c7b99082`  |
| 3037   | Layout 1 | `22e3c7b99082`  |
| 3030   | Layout 1 | `22e3c7b99082`  |
| 3021   | Layout 1 | `22e3c7b99082`  |
| 3012   | Layout 1 | `22e3c7b99082`  |
| 3002   | Layout 1 | `22e3c7b99082`  |
| 2995   | Layout 1 | `22e3c7b99082`  |
| 2987   | Layout 1 | `22e3c7b99082`  |
| 2978   | Layout 1 | `22e3c7b99082`  |
| 2970   | Layout 1 | `22e3c7b99082`  |
| 2959   | Layout 1 | `22e3c7b99082`  |
| 2951   | Layout 1 | `22e3c7b99082`  |
| 2942   | Layout 1 | `22e3c7b99082`  |
| 2935   | Layout 1 | `22e3c7b99082`  |
| 2932   | Layout 1 | `22e3c7b99082`  |
| 2923   | Layout 1 | `22e3c7b99082`  |
| 2919   | Layout 1 | `22e3c7b99082`  |
| 2907   | Layout 1 | `22e3c7b99082`  |
| 2900   | Layout 1 | `22e3c7b99082`  |
| 2891   | Layout 1 | `22e3c7b99082`  |
| 2882   | Layout 1 | `22e3c7b99082`  |
| 2872   | Layout 1 | `22e3c7b99082`  |
| 2863   | Layout 1 | `22e3c7b99082`  |
| 2855   | Layout 1 | `22e3c7b99082`  |
| 2849   | Layout 1 | `22e3c7b99082`  |
| 2844   | Layout 1 | `22e3c7b99082`  |
| 2834   | Layout 1 | `22e3c7b99082`  |
| 2825   | Layout 1 | `22e3c7b99082`  |
| 2819   | Layout 1 | `22e3c7b99082`  |
| 2811   | Layout 1 | `22e3c7b99082`  |
| 2803   | Layout 1 | `22e3c7b99082`  |
| 2794   | Layout 1 | `22e3c7b99082`  |
| 2783   | Layout 1 | `22e3c7b99082`  |
| 2774   | Layout 1 | `22e3c7b99082`  |
| 2765   | Layout 1 | `22e3c7b99082`  |
| 2756   | Layout 1 | `22e3c7b99082`  |
| 2750   | Layout 1 | `22e3c7b99082`  |
| 2743   | Layout 1 | `22e3c7b99082`  |
| 2736   | Layout 1 | `22e3c7b99082`  |
| 2726   | Layout 1 | `22e3c7b99082`  |
| 2717   | Layout 1 | `22e3c7b99082`  |
| 2709   | Layout 1 | `22e3c7b99082`  |
| 2703   | Layout 1 | `22e3c7b99082`  |
| 2695   | Layout 1 | `22e3c7b99082`  |
| 2684   | Layout 1 | `22e3c7b99082`  |
| 2672   | Layout 1 | `22e3c7b99082`  |
| 2665   | Layout 1 | `22e3c7b99082`  |
| 2657   | Layout 1 | `22e3c7b99082`  |
| 2649   | Layout 1 | `22e3c7b99082`  |
| 2644   | Layout 1 | `22e3c7b99082`  |
| 2637   | Layout 1 | `22e3c7b99082`  |
| 2629   | Layout 1 | `22e3c7b99082`  |
| 2619   | Layout 1 | `22e3c7b99082`  |
| 2612   | Layout 1 | `22e3c7b99082`  |
| 2606   | Layout 1 | `22e3c7b99082`  |
| 2602   | Layout 1 | `22e3c7b99082`  |
| 2601   | Layout 1 | `22e3c7b99082`  |
| 2592   | Layout 1 | `22e3c7b99082`  |
| 2583   | Layout 1 | `22e3c7b99082`  |
| 2575   | Layout 1 | `22e3c7b99082`  |
| 2567   | Layout 1 | `22e3c7b99082`  |
| 2560   | Layout 1 | `22e3c7b99082`  |
| 2553   | Layout 1 | `22e3c7b99082`  |
| 2545   | Layout 1 | `22e3c7b99082`  |
| 2538   | Layout 1 | `22e3c7b99082`  |
| 2529   | Layout 1 | `22e3c7b99082`  |
| 2519   | Layout 1 | `22e3c7b99082`  |
| 2513   | Layout 1 | `22e3c7b99082`  |
| 2510   | Layout 1 | `22e3c7b99082`  |
| 2507   | Layout 1 | `22e3c7b99082`  |
| 2503   | Layout 1 | `22e3c7b99082`  |
| 2498   | Layout 1 | `22e3c7b99082`  |
| 2492   | Layout 1 | `22e3c7b99082`  |
| 2487   | Layout 1 | `22e3c7b99082`  |
| 2480   | Layout 1 | `22e3c7b99082`  |
| 2474   | Layout 1 | `22e3c7b99082`  |
| 2468   | Layout 1 | `22e3c7b99082`  |
| 2460   | Layout 1 | `22e3c7b99082`  |
| 2453   | Layout 1 | `22e3c7b99082`  |
| 2444   | Layout 1 | `22e3c7b99082`  |
| 2438   | Layout 1 | `22e3c7b99082`  |
| 2434   | Layout 1 | `22e3c7b99082`  |
| 2429   | Layout 1 | `22e3c7b99082`  |
| 2421   | Layout 1 | `22e3c7b99082`  |
| 2414   | Layout 1 | `22e3c7b99082`  |
| 2407   | Layout 1 | `22e3c7b99082`  |
| 2401   | Layout 1 | `22e3c7b99082`  |
| 2397   | Layout 1 | `22e3c7b99082`  |
| 2393   | Layout 1 | `22e3c7b99082`  |
| 2384   | Layout 1 | `22e3c7b99082`  |
| 2378   | Layout 1 | `22e3c7b99082`  |
| 2372   | Layout 1 | `22e3c7b99082`  |
| 2358   | Layout 1 | `22e3c7b99082`  |
| 2352   | Layout 1 | `22e3c7b99082`  |
| 2347   | Layout 1 | `22e3c7b99082`  |
| 2343   | Layout 1 | `22e3c7b99082`  |
| 2335   | Layout 1 | `22e3c7b99082`  |
| 2327   | Layout 1 | `22e3c7b99082`  |
| 2324   | Layout 1 | `22e3c7b99082`  |
| 2319   | Layout 1 | `22e3c7b99082`  |
| 2313   | Layout 1 | `22e3c7b99082`  |
| 2308   | Layout 1 | `22e3c7b99082`  |
| 2302   | Layout 1 | `22e3c7b99082`  |
| 2295   | Layout 1 | `22e3c7b99082`  |
| 2290   | Layout 1 | `22e3c7b99082`  |
| 2284   | Layout 1 | `22e3c7b99082`  |
| 2276   | Layout 1 | `22e3c7b99082`  |
| 2269   | Layout 1 | `22e3c7b99082`  |
| 2259   | Layout 1 | `22e3c7b99082`  |
| 2250   | Layout 1 | `22e3c7b99082`  |
| 2243   | Layout 1 | `22e3c7b99082`  |
| 2235   | Layout 1 | `22e3c7b99082`  |
| 2229   | Layout 1 | `22e3c7b99082`  |
| 2224   | Layout 1 | `22e3c7b99082`  |
| 2218   | Layout 1 | `22e3c7b99082`  |
| 2215   | Layout 1 | `22e3c7b99082`  |
| 2207   | Layout 1 | `22e3c7b99082`  |
| 2203   | Layout 1 | `22e3c7b99082`  |
| 2196   | Layout 1 | `22e3c7b99082`  |
| 2192   | Layout 1 | `22e3c7b99082`  |
| 2189   | Layout 1 | `22e3c7b99082`  |
| 2183   | Layout 1 | `22e3c7b99082`  |
| 2179   | Layout 1 | `22e3c7b99082`  |
| 2171   | Layout 1 | `22e3c7b99082`  |
| 2163   | Layout 1 | `22e3c7b99082`  |
| 2156   | Layout 1 | `22e3c7b99082`  |
| 2151   | Layout 1 | `22e3c7b99082`  |
| 2147   | Layout 1 | `22e3c7b99082`  |
| 2142   | Layout 1 | `22e3c7b99082`  |
| 2138   | Layout 1 | `22e3c7b99082`  |
| 2134   | Layout 1 | `22e3c7b99082`  |

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
