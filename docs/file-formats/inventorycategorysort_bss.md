# `inventorycategorysort.bss` Format

## Purpose

The categories of the inventory's category view: one row per category
with its Korean name and two bytes. The inventory Lua
(`panel_window_inventory_all_6.luac`) builds one group per category type
from `0` to `__eInvenCategoryType_Count - 1`, titles it with
`ToClient_getCategoryNameByType(categoryType)`, and orders the groups by
`ToClient_getCategoryShowIndexByType(categoryType)`. Each item's group
comes from `getInventCategoryType()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | --------------------------- | ----- | ------- | ----------------------- |
| 1      | 2313 and later | 3482    | `inventorycategorysort.bss` | 416   | 20 Row  | 15 to 29, 21 on average |

| Layout | File                        | Known         | Unknown     |
| ------ | --------------------------- | ------------- | ----------- |
| 1      | `inventorycategorysort.bss` | 396 B (95.2%) | 20 B (4.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                           |
| --------------------- | -------- | ------------------------------ |
| `languagedata_en.loc` | Optional | Category names (type 122)      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No PABR magic and no string table.

| Offset  | Type           | Field     | Notes                                       |
| ------- | -------------- | --------- | ------------------------------------------- |
| `+0x00` | u32            | row_count | Number of categories; `20` on client 3482   |
| `+0x04` | Row[row_count] | rows      | See Row                                     |

### Row (variable: 11 bytes + name text)

| Offset         | Type  | Field              | Notes                                                                      |
| -------------- | ----- | ------------------ | -------------------------------------------------------------------------- |
| `+0x00`        | u8    | category_key       | Row key, `0` to `19`, each once; rows run from `15` down to `0`, then `19` down to `16` |
| `+0x01`        | str16 | name_kr            | Korean name (`의뢰`, `가구`)                                               |
| `name_kr+0x00` | u8    | unknown_name_kr_00 | `0` to `19`, each once; see Open Questions                                 |
| `name_kr+0x01` | u8    | category_key_dup   | Equal to `category_key` on every row (client 3482)                         |

## Categories

Client 3482. LOC type 122 holds the name under `str_id1`
`unknown_name_kr_00` and `str_id2` `category_key`.

| `category_key` | `unknown_name_kr_00` | `name_kr`          | LOC type 122 name   |
| -------------- | -------------------- | ------------------ | ------------------- |
| 0              | 19                   | `기타`             | Etc.                |
| 1              | 0                    | `의뢰`             | Quest               |
| 2              | 13                   | `사용 가능 물품`   | Usable              |
| 3              | 2                    | `장착류`           | Equippable          |
| 4              | 4                    | `강화`             | Enhancement         |
| 5              | 3                    | `수정/광명석`      | Crystal/Lightstone  |
| 6              | 15                   | `탑승물/반려동물`  | Mount/Pet           |
| 7              | 14                   | `재료`             | Life Skill Material |
| 8              | 16                   | `무역`             | Trade               |
| 9              | 18                   | `기타`             | Etc.                |
| 10             | 17                   | `가구`             | Furniture           |
| 11             | 1                    | `잡동사니`         | Junk                |
| 12             | 6                    | `투구(의상)`       | Helmet              |
| 13             | 5                    | `개봉 가능 물품`   | Openable            |
| 14             | 7                    | `상의(의상)`       | Armor (Appearance)  |
| 15             | 8                    | `신발(의상)`       | Shoes               |
| 16             | 9                    | `장갑(의상)`       | Gloves              |
| 17             | 10                   | `무기(의상)`       | Weapon              |
| 18             | 11                   | `속옷(의상)`       | Underwear           |
| 19             | 12                   | `악세서리류(의상)` | Accessory           |

## Notes

- The file is not in client 1784.

## Open Questions

### Which Byte Is the Category Type

One of the two bytes is the category type that items carry and the other
the show index. `category_key` is copied at the row's end like other row
keys and starts with `기타` at `0`, which reads as an enum with a default
member; `unknown_name_kr_00` puts Quest first and the two `기타` rows last
(`18`, `19`), which reads as a display order. LOC type 122 keys the names
the other way round, `unknown_name_kr_00` first. An item whose inventory
category is known would settle it.
