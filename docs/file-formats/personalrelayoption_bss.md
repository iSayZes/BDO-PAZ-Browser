# `personalrelayoption.bss` Format

## Purpose

The personal relay fields, the mirror fields of
`__eMirrorFieldContentsKey_PersonalRelayField` in the client Lua. One row
per field: its Korean name in the string table, three points, two times,
the NPC and monster character keys, two item IDs and unnamed counts. On client 3474 the
file has 2 rows, 금돼지굴 (Golden Pig Cave) with Golden Pig and 금돼지굴(일반)
(Golden Pig Cave, normal) with Golden Pigs, both with the NPC Munsik
(title Golden Pig Cave Subjugation).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `personalrelayoption.bss` | 250   | 2 Row   | 98        |

| Layout | File                      | Known        | Unknown       |
| ------ | ------------------------- | ------------ | ------------- |
| 1      | `personalrelayoption.bss` | 86 B (34.4%) | 164 B (65.6%) |

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
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6; item names, LOC type 0 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (98 bytes)

| Offset  | Type | Field                 | Notes                                                                           |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u32  | name_ref              | String table index of the field's Korean name (`name_kr`)                       |
| `+0x04` | f32  | unknown_04            | `-1171716.125` on both rows (client 3474); with `unknown_08` and `unknown_0c` one x, y, z point |
| `+0x08` | f32  | unknown_08            | `3134.306` on both rows                                                         |
| `+0x0C` | f32  | unknown_0c            | `1172652.125` on both rows                                                      |
| `+0x10` | f32  | unknown_10            | `-1163441` on both rows; with `unknown_14` and `unknown_18` a second point      |
| `+0x14` | f32  | unknown_14            | `3322` on both rows                                                             |
| `+0x18` | f32  | unknown_18            | `1169000` on both rows                                                          |
| `+0x1C` | f32  | unknown_1c            | `-1172216` on both rows; with `unknown_20` and `unknown_24` a third point       |
| `+0x20` | f32  | unknown_20            | `2934` on both rows                                                             |
| `+0x24` | f32  | unknown_24            | `1171490` on both rows                                                          |
| `+0x28` | u64  | unknown_28            | `43200000` on both rows (12 hours in milliseconds)                              |
| `+0x30` | u64  | unknown_30            | `14400000` on both rows (4 hours in milliseconds)                               |
| `+0x38` | u16  | npc_character_key     | `characterstatic.dbss` key: `62194` Munsik on both rows                          |
| `+0x3A` | u16  | monster_character_key | `characterstatic.dbss` key: `21948` Golden Pig, `24711` Golden Pigs             |
| `+0x3C` | u32  | summon_item_id        | Item ID: `56336` Rare Treasures, `1` on the second row; see Field Names         |
| `+0x40` | u32  | token_item_id         | Item ID: `56335` Golden Pigs Subjugation Token, `1` on the second row           |
| `+0x44` | u32  | unknown_44            | `0` on both rows                                                                |
| `+0x48` | u16  | unknown_48            | `0` on both rows                                                                |
| `+0x4A` | u32  | unknown_4a            | `1`, `2`                                                                        |
| `+0x4E` | u32  | unknown_4e            | `1`, `0`                                                                        |
| `+0x52` | u32  | unknown_52            | `400`, `999`                                                                    |
| `+0x56` | u32  | unknown_56            | `650`, `999`                                                                    |
| `+0x5A` | u32  | unknown_5a            | `100` on both rows                                                              |
| `+0x5E` | f32  | unknown_5e            | `13000` on both rows                                                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                 |
| ------- | ------------------ | ------------ | ----------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `2` on client 3474                 |
| `+0x04` | pstr[string_count] | strings      | Wide Korean field names, `금돼지굴`, `금돼지굴(일반)` |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which clients 1784 to 2519 do not ship. `name_ref` points to the
field name the relay widget shows with
`ToClient_GetCurrentPersonalRelayFieldName()`
(`panel_widget_personalfield_all`). `npc_character_key` and
`monster_character_key` resolve to LOC type 6 names: `62194` is Munsik with
the title Golden Pig Cave Subjugation, `21948` Golden Pig and `24711`
Golden Pigs, the monsters of the cave.

`summon_item_id` and `token_item_id` follow the LOC type 0 item names and
descriptions of the first row (client 3474), which
[bdocodex](https://bdocodex.com/us/item/56336/) shows the same: `56336`
Rare Treasures, "A magical item that summons rare treasures", used for
Golden Pig Cave Rare Treasures Summon, and `56335` Golden Pigs Subjugation
Token, "A token for clearing out the Golden Pig Cave", obtained from
Golden Pig Cave Subjugation
([bdocodex](https://bdocodex.com/us/item/56335/)). The second row, the
normal field, holds `1` in both (as an item, Silver), so what the fields
mean there is open.

## Notes

- The file is 250 bytes and the same on clients 3002, 3251 and 3474.
- The three points lie near x -1.17 million, z 1.17 million, outside the
  world map; which is the entry, the spawn or the exit is not known.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  the Korean name, the two characters and the two items with icons.

## Open Questions

### Items of the Normal Field

What `summon_item_id` and `token_item_id` mean on the second row, the
normal field, where both are `1`. As item IDs that is Silver; it may also
mark a field without a summon item and token.

### Times and Counts

What `unknown_28` and `unknown_30` (12 and 4 hours as milliseconds) and
`unknown_4a` to `unknown_5e` hold. The second row, the normal field, has
`999` where the first has `400` and `650`, which fits a cap that the normal
field does not apply.
