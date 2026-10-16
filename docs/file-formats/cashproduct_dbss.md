# `cashproduct.dbss` Format

## Purpose

The Pearl Shop product catalog. One variable-length block per cash product,
keyed by product ID through a required offset companion. Each block carries
Korean display text, an inline icon path, and the item ID the product grants.

The stored icon is the Pearl Shop tile for the product, **not** the item's own
icon. 16,620 of the 28,689 products (57.9%) share a tile with another product,
so a whole seasonal collection points at one promotional image and 480 unrelated
products all use `loyalties.dds`. For an item icon, follow the linked item ID
into [itemenchant.dbss](itemenchant_dbss.md) instead.

Product IDs are a separate ID space from items because a purchase is not an
item: one product can grant several items, the same item can be sold by several
products, and the tile is marketing art for the offer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes      | Records           | Row bytes                      |
| ------ | -------------- | ------- | ------------------------ | ---------- | ----------------- | ------------------------------ |
| 1      | 3473 and later | 3473    | `cashproduct.dbss`       | 30,636,397 | 29,779 Block      | 504 to 1,996, 1,029 on average |
| 1      | 3473 and later | 3473    | `cashproductoffset.dbss` | 357,352    | 29,779 Offset Row | 12                             |

| Layout | File                     | Known              | Unknown              |
| ------ | ------------------------ | ------------------ | -------------------- |
| 1      | `cashproduct.dbss`       | 1,326,822 B (4.3%) | 29,309,575 B (95.7%) |
| 1      | `cashproductoffset.dbss` | 357,352 B (100.0%) | 0 B (0.0%)           |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                           |
| ------------------------ | -------- | ---------------------------------------------- |
| `cashproductoffset.dbss` | Required | Maps product ID to a block offset and size     |
| `languagedata_en.loc`    | Optional | Product name and description (`str_type=50`), name of the linked item (`str_type=0`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                      |
| ------- | ------------ | ------ | ------------------------------------------ |
| `+0x00` | u32          | count  | Block count; see below                     |
| `+0x04` | Block[count] | blocks | Variable-length blocks, contiguous         |

The first block starts at byte `4` and the last ends exactly at end of file
(29,500,854 bytes observed), so the block stream is gap-free.

Observed blocks: 28,689 in the pre-2026-09-27 test fixture, 28,945 in the
2026-09-27 client (29,769,307 bytes, also gap-free). The other counts in this
doc are from the fixture.

### Block (variable: 12 bytes, size from `cashproductoffset.dbss`)

Only the product ID and the name sit at fixed offsets. The rest of the block
holds further strings and numeric data that a parser finds by scanning, see
Block Strings and Icon Path and Linked Item.

| Offset      | Type        | Field              | Notes                                      |
| ----------- | ----------- | ------------------ | ------------------------------------------ |
| `+0x00`     | u32         | product_id         | Matches the companion key in every sample  |
| `+0x04`     | str16       | name               | UTF-16LE Korean product name. The u64 count is the u32 `name_length`, the character count of the name that follows, and a u32 that is always 0 |
| `name+0x00` | bytes[rest] | unknown_after_name | Further strings and undecoded numeric data. The parser finds the icon path by scanning for the `(length, 0, text)` shape of an ASCII string, and reads `item_id` as a u32 16 bytes after the end of the icon text, see Icon Path and Linked Item |

### `cashproductoffset.dbss`

Unlike most offset companions this file has no `PABR` magic and no trailer: a 4-byte count followed by rows, ending exactly at `4 + count × 12`
(344,272 bytes observed).

| Offset  | Type              | Field | Notes                                               |
| ------- | ----------------- | ----- | --------------------------------------------------- |
| `+0x00` | u32               | count | Number of rows; equals the `cashproduct.dbss` count |
| `+0x04` | Offset Row[count] | rows  | `count` × 12-byte rows                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                          |
| ------- | ---- | ----------- | ---------------------------------------------- |
| `+0x00` | u32  | product_id  | Cash product ID; repeated at the block start   |
| `+0x04` | u32  | data_offset | Byte offset of the block in `cashproduct.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes                          |

Rows are contiguous: `data_offset + data_size` equals the next row's
`data_offset`.

## Block Strings

Both text encodings share one 8-byte prefix, the u64 count of `str16` and
`str8`: a u32 `length`, which counts **characters** in UTF-16 strings and
bytes in ASCII ones, and a u32 that is always 0 in observed data. The text
after it is UTF-16LE or ASCII and not null-terminated.

Strings sit at no fixed offset, so a parser scans for the
`(length, 0, text)` shape rather than seeking a constant. A block holds one to
five strings: the Korean name and its variants, an optional description
carrying `<PAColor…>` tags, and the ASCII icon path.

## Icon Path and Linked Item

The icon path is the block's only ASCII string, and a `u32` item ID follows
16 bytes after the end of that string:

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

This differs from [itemenchant.dbss](itemenchant_dbss.md), whose paths
start at `New_Icon/` and take the prefix `ui_texture/icon/`.

## Icon Coverage

| Measure                                     | Value            |
| ------------------------------------------- | ---------------- |
| Blocks carrying an icon path                 | 28,689 (100%)    |
| Icon paths resolving to a real PAZ file      | 28,613 (99.7%)   |
| Length prefix matching the string length     | 1,435 / 1,435    |
| Blocks with an item ID 16 bytes after the icon | 96.8%          |

## Notes

- Product IDs and item IDs are separate ID spaces. Product 117722 grants item
  340916 and uses icon `00105099`, three unrelated numbers. Only this file ties
  them together.
- The block's display text is Korean only. LOC type 50 holds the product's
  own name and description, keyed by `product_id` and a service code in
  `str_id3` (see `languagedata_loc.md`, Type 50). The product name differs
  from the linked item's name on about a third of the products: `Premium
  Pearl Box - 10,000+1,500` grants `Pearl Box - 10,000+1,500`, and
  `Polar Bear (Tier 3)` grants `[Pet] Polar Bear (Tier 3)`.
- Descriptions embed `<PAColor0xFFE9BD23>` and `<PAOldColor>` markup, the same
  tags as LOC text.
- `cashproductoffset.dbss` has no `PABR` magic and no trailer: a u32 count,
  then u32-keyed rows (`parse_bare_u32_offset_rows()`).
- 17 `gamecommondata` tables store inline icon paths. This file is second by
  volume with 14,750 unique paths, behind `itemenchant.dbss` with 21,768.

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
