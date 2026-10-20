# `maincategory.dbss` Format

## Purpose

`maincategory.dbss` is the list of Pearl Shop main categories, the tabs of the in-game shop. Each record holds the category ID, its tab order and tab image, the category type, an ASCII DDS icon path, an event cart key and whether the tab is shown. Companion `maincategoryoffset.dbss` holds the keyed record offsets.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 2      | 3473 and later | 3474    | `maincategory.dbss`       | 1,534 | 15 Category Record | 102       |
| 2      | 3473 and later | 3474    | `maincategoryoffset.dbss` | 154   | 15 Offset Record   | 10        |
| 1      | 1784           | 1784    | `maincategory.dbss`       | 1,216 | 12 Category Record | 101       |
| 1      | 1784           | 1784    | `maincategoryoffset.dbss` | 124   | 12 Offset Record   | 10        |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 2      | `maincategory.dbss`       | 1,534 B (100.0%) | 0 B (0.0%)   |
| 2      | `maincategoryoffset.dbss` | 124 B (80.5%)    | 30 B (19.5%) |
| 1      | `maincategory.dbss`       | 1,216 B (100.0%) | 0 B (0.0%)   |
| 1      | `maincategoryoffset.dbss` | 100 B (80.6%)    | 24 B (19.4%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `maincategoryoffset.dbss` | Required | `category_id -> (record_offset, record_size)` lookup |

All multi-byte values are little-endian.

## Layout 2

### File Layout

`maincategory.dbss` begins with a count and then stores the category records. The count matches `maincategoryoffset.dbss`, and the offset table points to the first record at `0x0004`.

| Offset  | Type                   | Field   | Notes                      |
| ------- | ---------------------- | ------- | -------------------------- |
| `+0x00` | u32                    | count   | Number of category records |
| `+0x04` | Category Record[count] | records | See Category Record        |

### Category Record (variable: 27 bytes + icon path)

Offsets are relative to `record_offset` from `maincategoryoffset.dbss`. Field Names gives the source of each name.

| Offset           | Type | Field          | Notes                                                                                        |
| ---------------- | ---- | -------------- | -------------------------------------------------------------------------------------------- |
| `+0x00`          | u16  | category_id    | Primary key; matches offset-table key                                                        |
| `+0x02`          | u32  | display_order  | Tab position; the shop sorts the tabs by it, ascending                                       |
| `+0x06`          | u32  | tab_image_no   | Tab button style: the shop copies the `RadioButton_CategoryTab_<tab_image_no>` control       |
| `+0x0A`          | u32  | category_type  | `CppEnums.CashProductCategory` value, see Category Type; `0` for a category without a type   |
| `+0x0E`          | str8 | icon_path      | ASCII DDS path under `ui_texture/`; u64 byte length, no null terminator                      |
| `icon_path+0x00` | u32  | event_category | Event cart key the shop checks with `IngameCashShop_CheckOpenEventCart`; `0` for none        |
| `icon_path+0x04` | u8   | is_display     | `0` hides the category's tab; the name rests on width and the Lua getter, see Field Names    |

Earlier versions of this doc called `display_order`, `tab_image_no`, `category_type` and `event_category` `unknown_02`, `unknown_06`, `unknown_0a` and `unknown_after_icon_path`, and `is_display` `enabled_flag`, then `unknown_icon_path_04`.

The record size is `0x16 + icon_path length + 5`. Every icon path on client 3474 is 75 bytes, so every record is 102 bytes, but the path is length-prefixed and is read as variable-length.

### `maincategoryoffset.dbss`

Provides keyed lookup into `maincategory.dbss` and supplies the record count.

| Offset  | Type                 | Field | Notes                         |
| ------- | -------------------- | ----- | ----------------------------- |
| `+0x00` | u32                  | count | Number of category records    |
| `+0x04` | Offset Record[count] | rows  | See Offset Record; no trailer |

### Offset Record (10 bytes)

| Offset  | Type | Field         | Notes                                       |
| ------- | ---- | ------------- | ------------------------------------------- |
| `+0x00` | u16  | category_id   | Key for the category record                 |
| `+0x02` | u32  | record_offset | Absolute byte offset in `maincategory.dbss` |
| `+0x06` | u16  | record_size   | Size of the record in bytes                 |
| `+0x08` | u16  | unknown_08    | Always 0                                    |

Rows are stored in descending category ID order, the highest ID first.

## Layout 1

On client 1784 a category record ends after `event_category`: it has no `is_display` byte, so `record_size` is 101. Only the Category Record differs from Layout 2.

### Category Record (variable: 26 bytes + icon path)

| Offset           | Type | Field          | Notes                                 |
| ---------------- | ---- | -------------- | ------------------------------------- |
| `+0x00`          | u16  | category_id    | Primary key; matches offset-table key |
| `+0x02`          | u32  | display_order  |                                       |
| `+0x06`          | u32  | tab_image_no   |                                       |
| `+0x0A`          | u32  | category_type  |                                       |
| `+0x0E`          | str8 | icon_path      | ASCII DDS path                        |
| `icon_path+0x00` | u32  | event_category | 0, 3 or 4 on client 1784              |

## Category Type

The in-game shop (`panel_ingamecashshop.luac`) compares `getCategoryType()` with `CppEnums.CashProductCategory` from `global_define_cpp_enum.luac`, for example `eCashProductCategory_Pearl` to find the tab that sells pearls. The enum on client 3474:

| Value | Member                           |
| ----- | -------------------------------- |
| 1     | `eCashProductCategory_Pearl`     |
| 2     | `eCashProductCategory_Mileage`   |
| 3     | `eCashProductCategory_Normal`    |
| 4     | `eCashProductCategory_Costumes`  |
| 5     | `eCashProductCategory_Furniture` |
| 6     | `eCashProductCategory_Servant`   |
| 7     | `eCashProductCategory_Pet`       |
| 8     | `eCashProductCategory_Beauty`    |
| 9     | `eCashProductCategory_HotNew`    |
| 15    | `eCashProductCategory_StepUp`    |

The 2016 client's `enum gc::CashProductCategory : unsigned char` numbers the same first seven members from `0` and ends with `eCashProductCategory_Customize = 7` and `eCashProductCategory_Dye = 8`, so its values do not apply to this file.

## Field Names

The record is one row of the `MainCategory_Table` sheet of a private server on client 1784, in its `DataSheets.bexcel`. The sheet's columns are `Index`, `Display_Order`, `Tab_ImageNo`, `EventCategory`, `EventSlotCategory`, `CategoryType` and `IconPath`; no `.xlsm` in its `DataSheet` folder holds the sheet. The official client 1784 file is byte-identical to that server's compiled `maincategory.dbss`. I matched every record field against every column by value over the shared category IDs:

| Field            | Column          | Lua getter          | Equal, client 1784 | Equal, client 3474 |
| ---------------- | --------------- | ------------------- | ------------------ | ------------------ |
| `category_id`    | `Index`         | `getNoRaw()`        | 12 of 12           | 12 of 12           |
| `display_order`  | `Display_Order` | `getDisplayOrder()` | 12 of 12           | 10 of 12           |
| `tab_image_no`   | `Tab_ImageNo`   | `getTabImageNo()`   | 12 of 12           | 12 of 12           |
| `category_type`  | `CategoryType`  | `getCategoryType()` | 12 of 12           | 12 of 12           |
| `icon_path`      | `IconPath`      | `getIconPath()`     | 12 of 12           | 12 of 12           |
| `event_category` | `EventCategory` | `getEventKey()`     | 12 of 12           | 10 of 12           |
| `is_display`     |                 | `isDisplay()`       |                    |                    |

On client 3474, categories 1 and 10 swap display orders 3 and 4 against the sheet, and `event_category` is `0` on every record. A private server on client 519 has the same `MainCategory_Table` columns in its `bdo.sqlite3`, with all 12 rows equal to the 1784 sheet except `EventCategory`, which is empty there. The 2016 client's debug symbols have no main category static status, and the 1784 server dump (`Instance_dumpFull.exe`) names the manager `MainCategoryStaticStatusManager`; I did not trace its row reader, since every Layout 1 field matches a column by value.

The Lua getters come from `panel_ingamecashshop.luac`, which reads, per category from `ToClient_GetMainCategoryStaticStatusWrapperByKeyRaw`, `getDisplayOrder()`, `getNoRaw()`, `getTabImageNo()`, `getIconPath()`, `getCategoryType()`, `getEventKey()`, `getEventSlotKey()` and `isDisplay()`. It passes both event keys to `IngameCashShop_CheckOpenEventCart`.

`is_display` has no sheet column, so its name rests on width and the Lua, not on values. The client 1784 Lua already calls `isDisplay()` and `getEventSlotKey()` on each category although the 1784 file stores neither, and Layout 2 adds exactly one byte, which holds only `0` and `1` on client 3474. `inGameShop:initTabPos` hides the tab of a category whose `isDisplay()` is false, and the shop counts it in `_hideTabCount`. On client 3474 the two categories with the byte at `0`, 13 and 14, have the two highest display orders, 13 and 14. `EventSlotCategory` (`getEventSlotKey()`) is empty in the 1784 sheet and has no field in either layout; an event key like `EventCategory` is a u32 in the file, not a byte.

## Observed Records

The records on client 3474:

| Category ID | display_order | tab_image_no | category_type | event_category | is_display | Icon Path                                                                     |
| ----------- | ------------- | ------------ | ------------- | -------------- | ---------- | ----------------------------------------------------------------------------- |
| 1           | 3             | 2            | 1             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_02.dds` |
| 2           | 5             | 0            | 2             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_03.dds` |
| 3           | 6             | 0            | 3             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_04.dds` |
| 4           | 8             | 0            | 4             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_05.dds` |
| 5           | 9             | 0            | 5             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_08.dds` |
| 6           | 10            | 0            | 6             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_07.dds` |
| 7           | 11            | 0            | 7             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_06.dds` |
| 8           | 12            | 0            | 8             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_09.dds` |
| 9           | 1             | 1            | 9             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_14.dds` |
| 10          | 4             | 3            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_12.dds` |
| 11          | 7             | 0            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 12          | 2             | 5            | 0             | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 13          | 13            | 6            | 0             | 0              | 0          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_17.dds` |
| 14          | 14            | 0            | 0             | 0              | 0          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_18.dds` |
| 15          | 5             | 6            | 15            | 0              | 1          | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_19.dds` |

## Notes

- `maincategoryoffset.dbss` is required because it gives the authoritative category IDs and record sizes.
- The shop takes a tab's name from `getCashCategoryName(getNoRaw(), CppEnums.CashProductCategoryNo_Undefined)`, not from this file.

## Open Questions

### Category Type 0

Categories 10 to 14 have `category_type` `0` on client 3474, a value no `CppEnums.CashProductCategory` member uses. What the shop does differently for them is not known.

### Category Names

`getCashCategoryName` is a client function; which file it reads the category names from is not known.

## In-Game Checks

### Hidden Tabs

This settles whether `is_display` `0` hides a main category tab. The name rests on the field width and the Lua getter `isDisplay()`, not on a sheet column.

1. Open the Pearl Shop.
2. Compare the main category tab icons with the Observed Records.

On client 3474 no tab shows the `CashShopMenu_17.dds` or `CashShopMenu_18.dds` icon (categories 13 and 14) when `0` hides a tab. A tab with one of those icons means the byte is something else.
