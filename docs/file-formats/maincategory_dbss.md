# `maincategory.dbss` Format

## Purpose

Defines Pearl Shop / cash shop main category records. Each record stores a category ID, small ordering/link fields, an ASCII DDS icon path, and an observed enabled flag. Companion `maincategoryoffset.dbss` provides the keyed record offsets.

Example:

```text
category_id: 1
icon_path: new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_02.dds
```

## Graph

### Tags

- file format
- dbss
- cash shop
- category
- icon

### Connections

- [maincategoryoffset.dbss](maincategory_dbss.md#maincategoryoffsetdbss) - keyed offset index for this file

---

## Companion Files

| File                      | Required | Role                                                 |
| ------------------------- | -------- | ---------------------------------------------------- |
| `maincategoryoffset.dbss` | Required | `category_id -> (record_offset, record_size)` lookup |

All multi-byte values are little-endian.

---

## File Layout

`maincategory.dbss` begins with a count and then stores fixed-size category records. The count matches `maincategoryoffset.dbss`, and the offset table points to the first record at `0x0004`.

| Offset  | Type | Field   | Notes                                   |
| ------- | ---- | ------- | --------------------------------------- |
| `+0x00` | u32  | count   | Number of category records; observed 15 |
| `+0x04` | row  | records | 102-byte records                        |

---

## Record Structure

### Category Record (102 bytes)

Offsets are relative to `record_offset` from `maincategoryoffset.dbss`.

| Offset  | Type   | Field               | Notes                                                     |
| ------- | ------ | ------------------- | --------------------------------------------------------- |
| `+0x00` | u16    | category_id         | Primary key; matches offset-table key                     |
| `+0x02` | u32    | unknown_02          | Small category/order reference; observed 1-14             |
| `+0x06` | u32    | unknown_06          | Small category/order reference; observed 0, 1, 2, 3, 5, 6 |
| `+0x0A` | u32    | unknown_0A          | Usually mirrors `category_id`; 0 for some records         |
| `+0x0E` | u32    | icon_path_len       | Byte length of `icon_path`; observed 75                   |
| `+0x12` | u32    | reserved_12         | Always 0                                                  |
| `+0x16` | char[] | icon_path           | ASCII DDS path; no null terminator                        |
| varies  | u32    | reserved_after_path | Always 0                                                  |
| varies  | u8     | enabled_flag        | Observed 1 for IDs 1-13, 0 for IDs 14-15                  |

The observed record size is 102 bytes: `0x16 + icon_path_len + 5` for the current data.

---

## Observed Records

| Category ID | unknown_02 | unknown_06 | unknown_0A | Enabled | Icon Path                                                                     |
| ----------- | ---------- | ---------- | ---------- | ------- | ----------------------------------------------------------------------------- |
| 1           | 3          | 2          | 1          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_02.dds` |
| 2           | 5          | 0          | 2          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_03.dds` |
| 3           | 6          | 0          | 3          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_04.dds` |
| 4           | 8          | 0          | 4          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_05.dds` |
| 5           | 9          | 0          | 5          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_08.dds` |
| 6           | 10         | 0          | 6          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_07.dds` |
| 7           | 11         | 0          | 7          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_06.dds` |
| 8           | 12         | 0          | 8          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_09.dds` |
| 9           | 1          | 1          | 9          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_14.dds` |
| 10          | 4          | 3          | 0          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_12.dds` |
| 11          | 7          | 0          | 0          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 12          | 2          | 5          | 0          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_01.dds` |
| 13          | 13         | 6          | 0          | 1       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_17.dds` |
| 14          | 14         | 0          | 0          | 0       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_18.dds` |
| 15          | 5          | 6          | 15         | 0       | `new_ui_common_forlua/window/ingamecashshop/cashshopmenu/CashShopMenu_19.dds` |

---

## maincategoryoffset.dbss

Provides keyed lookup into `maincategory.dbss` and supplies the record count.

### Header (4 bytes)

| Offset  | Type | Field | Notes                                   |
| ------- | ---- | ----- | --------------------------------------- |
| `+0x00` | u32  | count | Number of category records; observed 15 |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field         | Notes                                       |
| ------- | ---- | ------------- | ------------------------------------------- |
| `+0x00` | u16  | category_id   | Key for the category record                 |
| `+0x02` | u32  | record_offset | Absolute byte offset in `maincategory.dbss` |
| `+0x06` | u16  | record_size   | Size of the record in bytes; observed 102   |
| `+0x08` | u16  | reserved_08   | Always 0                                    |

Rows are stored in descending category ID order: 15 down to 1.

---

## Suggested UI Layout

| Column      | Type | Notes                                                                       |
| ----------- | ---- | --------------------------------------------------------------------------- |
| Category ID | num  | Primary key; right-aligned                                                  |
| Icon        | Icon | Render from `icon_path`                                                     |
| Enabled     | bool | From `enabled_flag`                                                         |
| Sort / Link | text | Show `unknown_02`, `unknown_06`, `unknown_0A` until semantics are confirmed |

---

## Notes

- `maincategoryoffset.dbss` is required because it gives the authoritative category IDs and record sizes.
- Records are currently fixed-size because all observed `icon_path` values are 75 ASCII bytes, but the string is length-prefixed and should be parsed as variable-length.
- Category IDs 14 and 15 are present but have `enabled_flag = 0`.

---

## Open Questions

### Category Link Fields

`unknown_02`, `unknown_06`, and `unknown_0A` look like small category IDs, order slots, or UI parent/child links. Their in-game labels and behavior are not confirmed.

### Category Names

No reliable LOC key was confirmed in this record. Category names may be resolved by another cash shop UI file or client script rather than this DBSS file.
