# `menu.bss` Format

## Purpose

The categories of the main menu (Esc menu): one fixed 40-byte row per category
with its hotkey, its title as a UI string key and its icon as a region of a
shared sprite sheet. The entries of each category are in
[`submenu.bss`](submenu_bss.md).

Example:

```text
category 2, hotkey F1
  title  GAME / LUA_MENU_REMAKE_CATEGORY_1 -> "Information"
  icon   Combine/Icon/Combine_Title_Icon_00.dds, region (2, 457) to (57, 512)
  18 entries in submenu.bss
```

## Companion Files

| File                  | Required | Role                                                                     |
| --------------------- | -------- | ------------------------------------------------------------------------ |
| `stringtable.bss`     | Optional | Hash of the title key in its sheet, for the LOC lookup                   |
| `languagedata_en.loc` | Optional | Title text, LOC type 37 (`str_id1` = key hash, `str_id2` = sheet)        |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset           | Type    | Field        | Notes                                                            |
| ---------------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00`          | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04`          | u32     | count        | Number of rows; 12 on client 3458                                |
| `+0x08`          | row[]   | rows         | 40-byte rows repeated `count` times                              |
| `8 + count * 40` | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8          | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4          | u32     | zero         | Always 0                                                         |

## Record Structure

### Category Row (40 bytes, repeated `count` times)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | menu_id       | 1 to 12, in row order; `submenu.bss` entries name it                   |
| `+0x04` | u32  | icon_x1       | Left edge of the icon region in the sheet, in pixels                   |
| `+0x08` | u32  | icon_y1       | Top edge                                                               |
| `+0x0C` | u32  | icon_x2       | Right edge; every region is 55 x 55 on client 3458                     |
| `+0x10` | u32  | icon_y2       | Bottom edge                                                            |
| `+0x14` | u32  | icon_ref      | String table index of the sprite sheet, relative to `ui_texture/`      |
| `+0x18` | u32  | hotkey_ref    | String table index of the hotkey label (`F1` to `F12`), UTF-16         |
| `+0x1C` | u32  | sheet_ref     | String table index of the title key's sheet (`GAME`)                   |
| `+0x20` | u32  | key_ref       | String table index of the title key (`LUA_MENU_REMAKE_CATEGORY_1`)     |
| `+0x24` | u32  | submenu_count | Number of entries in the category's `submenu.bss` group                |

### String Table

27 strings on client 3458: the two sprite sheets
`Combine/Icon/Combine_Title_Icon_00.dds` and `_01.dds`, the twelve hotkeys,
`GAME` and the twelve title keys.

## Notes

- On client 3458 the categories are Recently Used (F12, no entries: the
  client fills it), Information, Character, Reward, Shop, Adventure, Life,
  War, Function, Community, Settings and Adventurer Support (F11). The title
  keys are not in row order: F3 Reward is `LUA_MENU_REMAKE_CATEGORY_5`.
- `submenu_count` equals the entry count of the matching `submenu.bss` group
  in every row.
- The icons are 55 x 55 regions of two 1.5 MB, 632 x 632 sprite sheets, both
  shipped under `ui_texture/combine/icon/`. The table shows a sprite
  placeholder; a click opens the sprite and its place on the sheet.
- The app indexes the icons by menu ID as a sprite kind: `IndexKind.MENU_ICON`
  holds the sheet path and `IndexKind.MENU_ICON_REGION` the
  `(x1, y1, x2, y2)` region, read through `icon_path()` and `icon_region()`
  with `IconKind.MENU`.
