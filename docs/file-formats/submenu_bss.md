# `submenu.bss` Format

## Purpose

The entries of the main menu (Esc menu) categories in
[`menu.bss`](menu_bss.md): one 49-byte entry per menu item, grouped by
category, with its title as a UI string key and its icon as a region of a
shared sprite sheet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File          | Bytes  | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------- | ------ | ------------------------ | --------- |
| 1      | 1784 and later | 3474    | `submenu.bss` | 12,882 | 155 Menu Entry, 12 Group | 49        |

| Layout | File          | Known            | Unknown         |
| ------ | ------------- | ---------------- | --------------- |
| 1      | `submenu.bss` | 11,487 B (89.2%) | 1,395 B (10.8%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                     |
| --------------------- | -------- | ------------------------------------------------------------------------ |
| `menu.bss`            | Optional | Category titles; `menu_id` names its row                                 |
| `stringtable.bss`     | Optional | Hash of the title key in its sheet, for the LOC lookup                   |
| `languagedata_en.loc` | Optional | Title text, LOC type 37 (`str_id1` = key hash, `str_id2` = sheet)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Groups of entries instead of fixed rows, then the shared PABR string table
(`_common/pabr_strings.py`).

| Offset              | Type               | Field        | Notes                                                            |
| ------------------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                                     |
| `+0x04`             | u32                | group_count  | Number of groups; 12 on client 3458, the same as `menu.bss` rows |
| `+0x08`             | Group[group_count] | groups       | See Group                                                        |
| `groups+0x00`       | String Table       | string_table | See String Table                                                 |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where the groups end                 |
| `string_table+0x04` | u32                | zero         | Always 0                                                         |

The groups follow the `menu.bss` categories from Information (menu 2) on;
the last group is empty. Recently Used (menu 1) has no group of its own, so
group `i` holds the entries of menu `i + 2`.

### Group (variable: 4 bytes + entries)

| Offset  | Type                    | Field       | Notes                         |
| ------- | ----------------------- | ----------- | ----------------------------- |
| `+0x00` | u32                     | entry_count | Number of entries that follow |
| `+0x04` | Menu Entry[entry_count] | entries     | See Menu Entry                |

### Menu Entry (49 bytes)

Fields are unaligned.

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | entry_id    | Unique; 155 values on client 3458, not in group order                 |
| `+0x04` | u32  | menu_id     | The `menu.bss` category                                               |
| `+0x08` | u32  | position    | Position in the category, from 1                                      |
| `+0x0C` | u64  | unknown_0c  | `0` on 111 entries; see Open Questions                                |
| `+0x14` | u8   | unknown_14  | Always `0`                                                            |
| `+0x15` | u32  | icon_ref    | String table index of the sprite sheet, relative to `ui_texture/`     |
| `+0x19` | u32  | icon_x1     | Left edge of the icon region in the sheet, in pixels                  |
| `+0x1D` | u32  | icon_y1     | Top edge                                                              |
| `+0x21` | u32  | icon_x2     | Right edge; 151 of 155 regions are 55 x 55                            |
| `+0x25` | u32  | icon_y2     | Bottom edge                                                           |
| `+0x29` | u32  | sheet_ref   | String table index of the title key's sheet (`GAME` or `RESOURCE`)   |
| `+0x2D` | u32  | key_ref     | String table index of the title key (`LUA_MENU_REMAKE_MENU_HELP`)    |

### String Table (variable: 4 bytes + strings)

159 strings on client 3458: the two sprite sheets of `menu.bss`, the sheet
names `GAME` (91 entries) and `RESOURCE` (64), and one title key per entry.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 159 on client 3458  |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- The groups end exactly where the string table starts, and each group's
  entry count equals the `submenu_count` of its `menu.bss` category.
- 152 of the 155 title keys have LOC type 37 text on client 3458 through
  their sheet's `str_id2` (`GAME` = 1, `RESOURCE` = 2).
- Both sprite sheets ship under `ui_texture/combine/icon/`; four regions are
  not 55 x 55 (55 x 57 twice, 55 x 49, 56 x 55).
- The app indexes the icons by entry ID as a sprite kind:
  `IndexKind.SUBMENU_ICON` holds the sheet path and
  `IndexKind.SUBMENU_ICON_REGION` the `(x1, y1, x2, y2)` region, read through
  `icon_path()` and `icon_region()` with `IconKind.SUBMENU`.

## Open Questions

### What does `unknown_0c` hold?

It is `0` on 111 entries. On the other 44 the high word is a small number
(96 to 120) and the low word looks random (`0x8E80E004` on Guild,
`0xEF7A4404` on Settings). The set entries include newer or event windows
(Solare rankings, Black Spirit Adventure, Special Pass, Ticket Shop), so it
may mark a "new" badge or a content switch, but no value decodes as a date and
nothing in the client files seen so far reads it.
