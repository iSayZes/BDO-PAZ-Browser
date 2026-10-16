# `dropuisubcategoryinfo.bss` Format

## Purpose

The filter categories of the drop item window (Monster Zone Info): one fixed
row per filter button with its Korean name and button icon.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) lists the
categories of each hunting ground in `sub_category_keys`. LOC type 115 names
the categories by key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Category names (115)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of fixed 12-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds 15 strings: the Korean
names and the button icon names.

| Offset              | Type                | Field              | Notes                            |
| ------------------- | ------------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]             | magic              | ASCII `PABR`                     |
| `+0x04`             | u32                 | count              | Number of rows; 8 on client 3464 |
| `+0x08`             | Category Row[count] | rows               | See Category Row                 |
| `rows+0x00`         | String Table        | string_table       | 15 wide strings                  |
| `string_table+0x00` | u32                 | string_table_start | Where the rows end               |
| `string_table+0x04` | u32                 | zero               | Always `0`                       |

### Category Row (12 bytes)

| Offset  | Type | Field    | Notes                                                    |
| ------- | ---- | -------- | -------------------------------------------------------- |
| `+0x00` | u32  | key      | Category, 1 to 8; LOC type 115 `str_id1`                 |
| `+0x04` | u32  | name_ref | String table index of the Korean name                    |
| `+0x08` | u32  | icon_ref | String table index of the button icon; 6 and 7 share one |

| Key | Korean               | LOC type 115              | Icon                                           |
| --- | -------------------- | ------------------------- | ---------------------------------------------- |
| 1   | 파티 사냥터          | Party Zones               | `Combine_Etc_DropItem_Icon_Filter_Btn_02_Over` |
| 2   | 엘비아의 영역        | Elvia Realm               | `Combine_Etc_DropItem_Icon_Filter_Btn_03_Over` |
| 3   | 마르니의 밀실        | Marni's Realm             | `Combine_Etc_DropItem_Icon_Filter_Btn_08_Over` |
| 4   | 지역 의뢰            | Region Quests             | `Combine_Etc_DropItem_Icon_Filter_Btn_05_Over` |
| 5   | 추천                 | Suggested                 | `Combine_Etc_DropItem_Icon_Filter_Btn_06_Over` |
| 6   | 데키아의 등불        | Dehkia's Lantern          | `Combine_Etc_DropItem_Icon_Filter_Btn_04_Over` |
| 7   | 데키아의 등불 II     | Dehkia's Lantern II       | `Combine_Etc_DropItem_Icon_Filter_Btn_04_Over` |
| 8   | 엘라 세르빈의 풍경화 | Allan Serbin's Landscape  | `Combine_Etc_DropItem_Icon_Filter_Btn_07_Over` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- No hunting ground stores 5 or 7 on client 3464.
- No handler reads this file; the
  [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) handler
  names the categories from LOC type 115 alone.
