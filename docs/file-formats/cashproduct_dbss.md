# `cashproduct.dbss` Format

## Purpose

The Pearl Shop product catalog. One variable-length block per cash product,
keyed by product ID through a required offset companion. Each block carries
Korean display text, an **inline icon path**, and the item ID the product grants.

This is the second source of item icons after
[itemenchant.dbss](itemenchant_dbss.md), and the only one that covers cash-shop
products, whose icons are keyed by **product ID rather than item ID** — the
reason thousands of ID-named icons match no item.

Example:

```text
product 117722 -> Icon/New_Icon/09_Cash/03_Product/00105099.dds
               -> item 340916 ([Guardian] Shell Belle Outfit Set)
```

## Graph

### Tags

- file format
- dbss
- item
- cash shop
- icon

### Connections

- [cashproductoffset.dbss](#cashproductoffsetdbss) - required key/offset index into this file
- [itemenchant.dbss](itemenchant_dbss.md) - the primary item ID to icon path source
- [maincategory.dbss](maincategory_dbss.md) - Pearl Shop main category records
- [languagedata_en.loc](languagedata_loc.md) - English item names for the linked item ID

---

## Companion Files

| File                     | Required | Role                                           |
| ------------------------ | -------- | ---------------------------------------------- |
| `cashproductoffset.dbss` | Required | Maps product ID to a block offset and size     |
| `languagedata_en.loc`    | Optional | English name for the linked item (`str_type=0`) |

All multi-byte values are little-endian.

---

## File Layout

| Offset  | Type | Field  | Notes                                      |
| ------- | ---- | ------ | ------------------------------------------ |
| `+0x00` | u32  | count  | Block count; observed 28,689                |
| `+0x04` | —    | blocks | Variable-length blocks, contiguous          |

The first block starts at byte `4` and the last ends exactly at end of file
(29,500,854 bytes observed), so the block stream is gap-free.

---

## `cashproductoffset.dbss`

Unlike most offset companions this file has **no `PABR` magic and no trailer** —
a 4-byte count followed by rows, ending exactly at `4 + count × 12`
(344,272 bytes observed).

| Offset  | Type | Field | Notes                            |
| ------- | ---- | ----- | -------------------------------- |
| `+0x00` | u32  | count | Number of rows; observed 28,689  |
| `+0x04` | —    | rows  | `count` × 12-byte rows           |

### Row (12 bytes)

| Offset  | Type | Field       | Notes                                         |
| ------- | ---- | ----------- | --------------------------------------------- |
| `+0x00` | u32  | product_id  | Cash product ID; repeated at the block start  |
| `+0x04` | u32  | data_offset | Byte offset of the block in `cashproduct.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes                         |

Rows are contiguous: `data_offset + data_size` equals the next row's
`data_offset`.

---

## Block Structure

| Offset  | Type   | Field          | Notes                                      |
| ------- | ------ | -------------- | ------------------------------------------ |
| `+0x00` | u32    | product_id     | Matches the companion key in every sample  |
| `+0x04` | u32    | name_length    | Character count of the name that follows   |
| `+0x08` | u32    | zero           | Always 0                                   |
| `+0x0C` | char16 | name           | UTF-16LE Korean product name               |
| varies  | —      | strings/fields | Further strings and undecoded numeric data |

### Length-prefixed string

Both text encodings share one 8-byte prefix:

| Offset  | Type | Field  | Notes                                             |
| ------- | ---- | ------ | ------------------------------------------------- |
| `+0x00` | u32  | length | UTF-16 strings count **characters**, ASCII **bytes** |
| `+0x04` | u32  | zero   | Always 0 in observed data                         |
| `+0x08` | —    | text   | UTF-16LE or ASCII; not null-terminated            |

Strings sit at no fixed offset, so a parser scans for the
`(length, 0, text)` shape rather than seeking a constant. A block holds one to
five strings: the Korean name and its variants, an optional description
carrying `<PAColor…>` tags, and the ASCII icon path.

### Icon path and linked item

The icon path is the block's only ASCII string, and a `u32` item ID follows
**16 bytes after the end of that string**:

| Element    | Position                          | Observed                    |
| ---------- | --------------------------------- | --------------------------- |
| icon path  | length-prefixed ASCII string      | 100% of blocks              |
| item_id    | `u32` at icon end + 16            | 96.8% of blocks             |

Stored paths always begin with `Icon/`, so the PAZ path is the stored value
prefixed with `ui_texture/`, matched case-insensitively:

```text
Icon/New_Icon/09_Cash/03_Product/00105099.dds
  -> ui_texture/icon/new_icon/09_cash/03_product/00105099.dds
```

Note this differs from [itemenchant.dbss](itemenchant_dbss.md), whose paths
start at `New_Icon/` and take the prefix `ui_texture/icon/`.

---

## Icon Coverage

| Measure                                     | Value            |
| ------------------------------------------- | ---------------- |
| Blocks carrying an icon path                 | 28,689 (100%)    |
| Icon paths resolving to a real PAZ file      | 28,613 (99.7%)   |
| Length prefix matching the string length     | 1,435 / 1,435    |
| Blocks with an item ID 16 bytes after the icon | 96.8%          |

---

## Suggested UI Layout

| Column     | Type | Notes                                              |
| ---------- | ---- | -------------------------------------------------- |
| Product ID | num  | `product_id`                                        |
| Icon       | text | Icon path, prefixed `ui_texture/`                   |
| Product    | text | Korean `name` from the block                        |
| Item ID    | num  | Linked `item_id`; `—` when absent                   |
| Item       | text | LOC `str_type=0`, `str_id1=item_id`                 |
| Block Size | num  | `data_size` from the companion                      |

---

## Notes

- Product IDs and item IDs are separate ID spaces. Product 117722 grants item
  340916 and uses icon `00105099` — three unrelated numbers. Only this file ties
  them together.
- The block's display text is Korean only; English names come from LOC via the
  linked item ID, not from this file.
- Descriptions embed `<PAColor0xFFE9BD23>` and `<PAOldColor>` markup, the same
  convention handled by `_common/pa_color.py`.
- `cashproductoffset.dbss` is the only offset companion observed so far with no
  `PABR` magic and no trailer, so the shared offset-table helpers do not apply.
- 17 `gamecommondata` tables store inline icon paths. This file is second by
  volume with 14,750 unique paths, behind `itemenchant.dbss` with 21,768.

---

## Open Questions

### Remaining Numeric Fields

Everything other than the product ID, the strings, and the linked item ID is
undecoded. Price in Pearls, sale flags, category links and availability dates
are all plausible and none is confirmed.

### Blocks Without a Linked Item

3.2% of blocks have no LOC item ID at the expected position. Whether those
products grant several items, grant none directly, reference an unreleased item,
or simply store the ID elsewhere in the block is unresolved.

### Multiple Granted Items

Only the first item ID after the icon was searched for. Bundle products
plausibly list several, but no block was confirmed to carry more than one, so
the field may be a single link or the head of a list.

### String Roles

Blocks carry between one and five strings. The first is the product name and one
is the icon path, but whether the others are display variants, a subtitle, or a
description is not established.
