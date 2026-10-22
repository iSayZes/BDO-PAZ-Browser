# `letter.bss` Format

## Purpose

The letter window an item opens: one row per letter item with the
`RESOURCE` string sheet key of the letter text, the background texture and
whether the text is centered. The letter Lua
(`panel_window_letterscroll_all_1.luac`) reads a row through
`getItemLetterStaticStatus(ItemEnchantKey(itemkey))` and the getters
`getItemLetterMainDescStringKey()`, `getItemLetterTexturePath()` and
`isItemLetterCenterAlignment()`, and shows the text with
`PAGetString(Defines.StringSheet_RESOURCE, key)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File         | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------ | ----- | ------- | --------- |
| 2      | 1784 and later | 3482    | `letter.bss` | 5,408 | 53 Row  | 13        |
| 1      | 1636           | 1636    | `letter.bss` | 1,248 | 9 Row   | 12        |

| Layout | File         | Known            | Unknown    |
| ------ | ------------ | ---------------- | ---------- |
| 2      | `letter.bss` | 5,408 B (100.0%) | 0 B (0.0%) |
| 1      | `letter.bss` | 1,248 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2519   | Layout 2 |
| 2313   | Layout 2 |
| 2107   | Layout 2 |
| 1937   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 1 |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                 |
| --------------------- | -------- | ---------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) and the letter texts (type 37)   |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of letters                             |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (13 bytes)

| Offset  | Type | Field                  | Notes                                                                                  |
| ------- | ---- | ---------------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key               | The letter item (LOC type 0 name); the rows are in no key order                        |
| `+0x04` | u32  | main_desc_string_index | Index into `strings`: the `RESOURCE` sheet key of the text (`PANEL_LETTER_BADEIN_1`)   |
| `+0x08` | u32  | texture_path_index     | Index into `strings`: the background under `ui_texture/` (`Combine/ETC/Combine_Etc_FugarCheering.dds`) |
| `+0x0C` | u8   | is_center_alignment    | `1` centers the text; `1` on 17 of 53 rows of client 3482                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                      |
| ------- | ------------------ | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                          |
| `+0x04` | pstr[string_count] | strings      | The keys and texture paths, UTF-16LE; a texture several rows share is stored once |

## Layout 1

No `is_center_alignment` byte: a row is 12 bytes. Only the Row differs from
Layout 2.

### Row (12 bytes)

| Offset  | Type | Field                  | Notes |
| ------- | ---- | ---------------------- | ----- |
| `+0x00` | u32  | item_key               |       |
| `+0x04` | u32  | main_desc_string_index |       |
| `+0x08` | u32  | texture_path_index     |       |

## Field Names

The `Letter` sheet of a private server's `DataSheets.bexcel` on client 1784
has the columns `itemkey`, `mainDescStringKey`, `texturePath` and
`CenterAlignment` (`1` or empty), 26 rows.

| Field                  | Column              | Same value (client 1784) | Same value (client 3482) |
| ---------------------- | ------------------- | ------------------------ | ------------------------ |
| item_key               | `itemkey`           | 26 of 26                 | 26 of 26                 |
| main_desc_string_index | `mainDescStringKey` | 26 of 26                 | 24 of 26                 |
| texture_path_index     | `texturePath`       | 26 of 26                 | 26 of 26                 |
| is_center_alignment    | `CenterAlignment`   | 26 of 26                 | 26 of 26                 |

The string columns compare the string an index points at. On client 3482
items `8199` and `8200` point at `PANEL_LETTER_SEASON_FINISH_DESC_NEW_1`
and `_NEW_2` where the sheet has `PANEL_LETTER_SEASON_FINISH_DESC4` and
`DESC5`.

## Notes

- The letter text is LOC type 37 under `key_hash()` of the key and the
  `RESOURCE` sheet's `str_id2`, as for the other `RESOURCE` keys of
  [`stringtable.bss`](stringtable_bss.md).
