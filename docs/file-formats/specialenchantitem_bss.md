# `specialenchantitem.bss` Format

## Purpose

The items whose name or icon changes with their enhancement level, one fixed
19-byte row per item key (`enchant_level << 24 | item_id`) with the level the
client shows, the icon path and the Korean name of that level. It is a compact
copy of the per-level blocks of [`itemenchant.dbss`](itemenchant_dbss.md) for
these 551 items, so the per-level icon of a Sovereign weapon or a Fallen God
armor is reachable without walking the 194 MB file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `itemenchant.dbss`    | Optional | Full item records; every row here has a level block there             |
| `languagedata_en.loc` | Optional | English names, LOC type 79, `str_id1` = item ID, `str_id2` = level    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss`, `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset              | Type                  | Field        | Notes                                          |
| ------------------- | --------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]               | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                   | count        | Number of rows; 3,081 on client 3458           |
| `+0x08`             | Item Level Row[count] | rows         | See Item Level Row                             |
| `rows+0x00`         | String Table          | string_table | See String Table                               |
| `string_table+0x00` | u32                   | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                   | zero         | Always 0                                       |

The rows follow `itemenchantoffset.dbss` key order exactly, which is neither
ascending nor descending (the first row is item 736815 at level 20).

### Item Level Row (19 bytes)

Fields are unaligned.

| Offset  | Type     | Field         | Notes                                                                    |
| ------- | -------- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | item_key      | `enchant_level << 24 \| item_id` (`_common/item_key.py`); unique          |
| `+0x04` | u8       | display_level | The level the client shows, on the weapon scale; see Display Level below |
| `+0x05` | u32      | icon_ref      | String table index of the icon path; never empty                         |
| `+0x09` | u32      | name_ref      | String table index of the Korean name; never empty                       |
| `+0x0D` | bytes[4] | unknown_0d    | Always `0`                                                               |
| `+0x11` | u8       | unknown_11    | `1` in 2,481 rows; the same in every row of one item, see Open Questions |
| `+0x12` | u8       | unknown_12    | `1` in 2,409 rows; the same in every row of one item, see Open Questions |

### String Table (variable: 4 bytes + strings)

3,253 strings on client 3458, all referenced. `icon_ref` and `name_ref` index
the same table but never share an entry: 500 are icon paths, the other 2,753
names. Unlike `buffsimply.bss` there is no `"0"` or empty entry. Repeated
values are stored once, so levels that keep an icon point at the same entry.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 3,253 on client 3458 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Display Level

The client reads this byte through `ToClient_getSpecialEnchantDisplayLevel`
(`include/global_util_ui_slot.luac`, the item tooltips, the enhancement window) and
passes it to `HighRomaEnchantLevel_ReplaceString`, so it is the level drawn on
the item slot, which can differ from the stored `enchant_level`. It uses the
weapon scale: `1` to `15` are `+1` to `+15`, `16` to `25` are the grades
below. The grade names are confirmed by LOC type 79, whose name of every row
at display level 16 to 25 starts with that grade (`PRI: Fiery Sovereign
Mareca`), 219 rows each on client 3458.

| Value | Grade |
| ----- | ----- |
| 16    | PRI   |
| 17    | DUO   |
| 18    | TRI   |
| 19    | TET   |
| 20    | PEN   |
| 21    | HEX   |
| 22    | SEP   |
| 23    | OCT   |
| 24    | NOV   |
| 25    | DEC   |

## Notes

- Checked against `itemenchant.dbss` on client 3458: every row's key has a
  block there, and the first string of that block is the same icon path in all
  3,081 rows. 1,356 rows store an icon that differs from the item's level-0
  icon, over 189 paths that no base item uses (`00747201_02.dds`). The
  `ITEM_ICON` index, read from level-0 blocks only, cannot reach them.
- The app builds its per-level item icon lookup index
  (`IndexKind.ITEM_KEY_ICON`, read through `IconKind.ITEM_KEY` and
  `item_key_icon_path()`) from this file.
- LOC type 79 names all 3,081 rows. In 2,250 the name differs from the item's
  LOC type 0 name: a grade prefix (`DEC: Fiery Sovereign Mareca`) or a new
  word for the stage (`Desperate Dahn's Gloves` at level 1, `Wailing Dahn's
  Gloves` at level 4).
- LOC type 79 reaches past this file: 5,298 rows over 925 items on client
  3458, among them accessories such as `Preonne Belt` whose every level
  repeats the item name. Level 0 always matches the LOC type 0 name, and a
  name that differs never repeats across the levels of one item, so
  `item_key_text()` (`_common/item_key.py`) shows it without the level
  suffix in every item list. Five more rows key Fallen God's Armor (719898)
  by its packed item key with `str_id2` 0; they repeat the item ID rows.
- All 500 icon paths exist on client 3458 once resolved under
  `ui_texture/icon/` and lowercased, as for `itemenchant.dbss`.
- The 551 items fall into four shapes on client 3458:

  | Rows per item | Items | `enchant_level` | `display_level`             | `unknown_11`, `unknown_12` | Example                        |
  | ------------- | ----- | --------------- | --------------------------- | -------------------------- | ------------------------------ |
  | 1             | 292   | 20              | 20                          | 0, 0                       | Earthshaking Nouver Shuriken   |
  | 6             | 12    | 0 to 5          | 20 at every level           | 1, 0                       | Dahn's Gloves (930905)         |
  | 11            | 28    | 0 to 10         | same as the level           | 0, 0                       | Preonne Ring                   |
  | 11            | 219   | 0 to 10         | 0, then 16 to 25 (PRI to DEC) | 1, 1                     | Fiery Sovereign Mareca         |

  An item with rows here has a row for every level from 0 to its
  `itemenchant.dbss` maximum, except the 292 single-row items, which list only
  level 20.

## Open Questions

### What do `unknown_11` and `unknown_12` mark?

Both are per-item flags. On client 3458 `unknown_11` is `1` on exactly the
items whose name changes between their levels (231 items; the 28 Preonne-style
items keep one name and store `0`, and the 292 single-row items cannot vary),
and `unknown_12` is `1` on exactly the items whose display level jumps to the
grade scale (0, then 16 to 25). The client Lua names `isSpecialEnchantItem` and
`isSpecialAccessory` next to the display level call, but neither is shown to
read this file, so the correlations are not yet a meaning.
