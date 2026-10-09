# `dropuimaincategoryinfo.bss` Format

## Purpose

The region tabs of the drop item window (Monster Zone Info): one fixed row
per tab with its territory and tab icon.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) puts each
hunting ground on a tab through `main_category_key`, and its handler reads
this file for the Region column.

Example:

```text
tab 10  territory 11 Ulukita        icon Combine_Etc_DropItem_Icon_Tab_11
tab 11  territory 10 Land of the Morning Light  icon Combine_Etc_DropItem_Icon_Tab_10
```

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Territory names (12)     |

All multi-byte values are little-endian.

## File Layout

PABR block of fixed 10-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-pool)
(`_common/pabr_strings.py`). The string table holds only the tab icon names.

| Offset  | Type    | Field              | Notes                              |
| ------- | ------- | ------------------ | ---------------------------------- |
| `+0x00` | char[4] | magic              | ASCII `PABR`                       |
| `+0x04` | u32     | count              | Number of rows; 13 on client 3464  |
| `+0x08` | row[]   | rows               | 10 bytes each                      |
| ...     | table   | string_table       | 13 wide strings, one icon per row  |
| EOF - 8 | u32     | string_table_start | Where the rows end                 |
| EOF - 4 | u32     | zero               | Always `0`                         |

## Record Structure

### Tab Row (10 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key           | Region tab, 1 to 13; `main_category_key` in the hunting grounds |
| `+0x04` | u16  | territory_key | LOC type 12 `str_id1`; `str_id4` 1 is the tab name           |
| `+0x06` | u32  | icon_ref      | String table index of the tab icon                          |

| Key | Territory | Name                       | Icon                               |
| --- | --------- | -------------------------- | ---------------------------------- |
| 1   | 0         | Balenos                    | `Combine_Etc_DropItem_Icon_Tab_04` |
| 2   | 1         | Serendia                   | `Combine_Etc_DropItem_Icon_Tab_02` |
| 3   | 2         | Calpheon                   | `Combine_Etc_DropItem_Icon_Tab_01` |
| 4   | 3         | Mediah                     | `Combine_Etc_DropItem_Icon_Tab_03` |
| 5   | 4         | Valencia                   | `Combine_Etc_DropItem_Icon_Tab_05` |
| 6   | 6         | Kamasylvia                 | `Combine_Etc_DropItem_Icon_Tab_06` |
| 7   | 7         | Drieghan                   | `Combine_Etc_DropItem_Icon_Tab_07` |
| 8   | 8         | O'dyllita                  | `Combine_Etc_DropItem_Icon_Tab_08` |
| 9   | 9         | Mountain of Eternal Winter | `Combine_Etc_DropItem_Icon_Tab_09` |
| 10  | 11        | Ulukita                    | `Combine_Etc_DropItem_Icon_Tab_11` |
| 11  | 10        | Land of the Morning Light  | `Combine_Etc_DropItem_Icon_Tab_10` |
| 12  | 12        | Outer Edania               | `Combine_Etc_DropItem_Icon_Tab_12` |
| 13  | 13        | Inner Edania               | `Combine_Etc_DropItem_Icon_Tab_16` |

The Great Ocean (territory 5) has no tab, and tabs 10 and 11 swap the
territory order.

## Suggested UI Layout

| Column    | Type | Notes                                                              |
| --------- | ---- | ------------------------------------------------------------------ |
| Key       | num  | `key`; right-aligned                                               |
| Territory | text | LOC type 12 `str_id4` 1, falling back to `territory_key`           |
| Icon      | text | Tab icon name                                                      |

## Notes

- LOC type 12 `str_id4` 0 is the territory's own name and can differ from the
  tab name: territories 12 and 13 are both `Alyaelli` there, and `Outer
  Edania` / `Inner Edania` only in `str_id4` 1.
- No handler reads this file on its own; the
  [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) handler
  loads it as an optional companion and keeps only key -> territory.
