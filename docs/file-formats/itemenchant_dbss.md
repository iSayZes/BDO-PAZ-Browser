# `itemenchant.dbss` Format

## Purpose

The per-item enchant table, and in practice the closest thing the client data has
to a master item table. It holds one variable-length block per
(item, enchant level) pair, keyed through a required offset companion. Each block
carries the item's **icon path as an inline string**, which makes this file the
authoritative item ID to icon mapping, the one thing that cannot be derived from
an item ID alone.

At roughly 194 MB it is the largest file in the game data.

Example:

```text
item 24626 (King Clam Wall Ornament)
  -> New_Icon/03_ETC/06_Housing/InHouse_Cultivate_Sea_Clam_01_Wall.dds
```

## Graph

### Tags

- file format
- dbss
- item
- enchant
- icon

### Connections

- [itemenchantoffset.dbss](#itemenchantoffsetdbss) - required key/offset index into this file
- [languagedata_en.loc](languagedata_loc.md) - English item names for the record key (`str_type=0`)
- [pet.dbss](pet_dbss.md) - another format that stores an inline icon path per record
- [quest.dbss](quest_dbss.md) - stores inline icon paths using the same convention

---

## Companion Files

| File                      | Required | Role                                          |
| ------------------------- | -------- | --------------------------------------------- |
| `itemenchantoffset.dbss`  | Required | Maps the packed key to a block offset and size |
| `languagedata_en.loc`     | Optional | Item name for the item ID (`str_type=0`)      |

All multi-byte values are little-endian.

---

## File Layout

| Offset  | Type | Field   | Notes                                                |
| ------- | ---- | ------- | ---------------------------------------------------- |
| `+0x00` | u32  | count   | Record count; observed 169,965, matching the companion |
| `+0x04` | —    | blocks  | Variable-length blocks, contiguous, in key order      |

Blocks are addressed only through the companion. The first block starts at byte
`4`, and the last block ends exactly at end of file (203,540,909 bytes observed),
so the block stream is gap-free.

---

## `itemenchantoffset.dbss`

| Offset  | Type  | Field  | Notes                            |
| ------- | ----- | ------ | -------------------------------- |
| `+0x00` | u8[4] | magic  | `PABR` (ASCII)                   |
| `+0x04` | u32   | count  | Number of rows; observed 169,965 |
| `+0x08` | —     | rows   | `count` × 12-byte rows           |
| end-12  | —     | trailer | 12-byte file trailer            |

### Row (12 bytes)

| Offset  | Type | Field       | Notes                                        |
| ------- | ---- | ----------- | -------------------------------------------- |
| `+0x00` | u32  | key         | Packed item ID and enchant level, see below |
| `+0x04` | u32  | data_offset | Byte offset of the block in `itemenchant.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes                        |

Rows are contiguous: `data_offset + data_size` of one row equals the next row's
`data_offset`.

### Trailer (12 bytes)

The same trailer shape used by
[fairyupgraderate.bss](fairyupgraderate_bss.md) and
[zodiacsignindex.bss](zodiacsignindex_bss.md).

| Offset  | Type | Field          | Observed  | Notes                              |
| ------- | ---- | -------------- | --------- | ---------------------------------- |
| `+0x00` | u32  | reserved_a     | 0         | Always zero                        |
| `+0x04` | u32  | end_of_rows    | 2,039,588 | Equals `8 + count × 12`            |
| `+0x08` | u32  | reserved_b     | 0         | Always zero                        |

---

## Key Packing

```text
key = (key_variant << 24) | item_id
```

| Field       | Bits   | Observed range |
| ----------- | ------ | -------------- |
| key_variant | 31..24 | 0-25           |
| item_id     | 23..0  | 1-1,000,827    |

The low 24 bits are confirmed item IDs: 69,292 of them match a name in
`languagedata_en.loc`. **What the high byte means is not confirmed.** Variant `0`
is the base item, with exactly one record per item ID, which is all the icon
index needs.

| Key group     | Rows    | Meaning                     |
| ------------- | ------- | --------------------------- |
| variant 0     | 69,954  | One per base item           |
| variants 1-25 | 100,011 | Unconfirmed, see the open question |

---

## Block Structure

Only the parts needed for the icon mapping are confirmed. A block opens with the
item ID and ends with a large run of enchant-related numeric fields that are not
yet decoded.

| Offset  | Type | Field    | Notes                                    |
| ------- | ---- | -------- | ---------------------------------------- |
| `+0x00` | u32  | item_id  | Repeats the item ID from the key         |
| `+0x04` | —    | unknown  | ~270 bytes of numeric fields             |
| varies  | —    | strings  | One or two length-prefixed ASCII strings |
| varies  | —    | unknown  | Remaining enchant data                   |

### Length-prefixed string

| Offset  | Type   | Field  | Notes                          |
| ------- | ------ | ------ | ------------------------------ |
| `+0x00` | u32    | length | Byte length of `text`          |
| `+0x04` | u32    | zero   | Always 0 in observed data      |
| `+0x08` | char[] | text   | ASCII, not null-terminated     |

The string does **not** sit at a fixed block offset, 47 distinct offsets were
observed across a 400-block sample, so a parser must scan for the
`(length, 0, ascii × length)` shape rather than seek a constant.

A block holds at most two strings:

| Position | Content                                                        |
| -------- | -------------------------------------------------------------- |
| first    | Icon path, relative to `ui_texture/icon/`                       |
| second   | Optional effect tag such as `ITEM_BIC_HIT_1`; absent in most blocks |

**The first string is always the icon path.** In a 400-block sample the length
prefix matched the string length 400 out of 400 times.

### Resolving the icon path

Stored paths always begin with `New_Icon/`, so the PAZ path is the stored value
prefixed with `ui_texture/icon/`, matched case-insensitively:

```text
New_Icon/03_ETC/06_Housing/InHouse_Cultivate_Sea_Clam_01_Wall.dds
  -> ui_texture/icon/new_icon/03_etc/06_housing/inhouse_cultivate_sea_clam_01_wall.dds
```

---

## Icon Coverage

Measured against the 73,947 item IDs in `languagedata_en.loc` (`str_type=0`):

| Measure                                        | Value          |
| ---------------------------------------------- | -------------- |
| Items with a level-0 record                     | 69,292 (93.7%) |
| Sampled icon paths resolving to a real PAZ file | 99.3%          |
| Level-0 records carrying an icon path           | 100%           |

For comparison, deriving `product_icon_png/{item_id:08d}.png` from the ID alone
reaches only 14.9% of items, and indexing every ID-named icon under
`ui_texture/icon` by basename reaches 28.8%. The icon path stored here is the
only approach that covers items whose icon is named after a 3D asset
(furniture) or keyed by a cash-product ID rather than the item ID.

---

## Suggested UI Layout

| Column        | Type | Notes                                             |
| ------------- | ---- | ------------------------------------------------- |
| Item ID       | num  | `item_id` from the key                            |
| Icon          | text | First block string, prefixed `ui_texture/icon/`   |
| Item          | text | LOC `str_type=0`, `str_id1=item_id`               |
| Effect Tag    | text | Second block string when present                  |

---

## Notes

- `itemenchantbackendtest.dbss` (73 MB) contains the identical set of 169,962
  icon path references and 21,768 unique paths, it looks like a test copy and
  adds nothing. `itemenchantbackend.dbss` (121 MB) contains no icon paths at all.
- 17 `gamecommondata` tables store inline icon paths this way. After this file
  the largest are `cashproduct.dbss` (14,750 unique paths, keyed by cash product
  ID rather than item ID), `quest.dbss` (6,366) and `skilltype.dbss` (3,530).
- The icon path is why ~14,400 ID-named icons match no LOC item name: cash-shop
  items reference a product-ID icon such as
  `Icon/New_Icon/09_Cash/03_Product/00105099.dds` while the item itself is a
  different ID. Those icons are reachable only through a stored path.
- Reading the whole file to build an index costs a 194 MB decompress, which is
  too slow to repeat per launch; an index built from this file should be cached
  on disk and invalidated on the PAZ meta version, the way `paz/bdo_cache.py`
  already caches the entry list.
- Blocks are contiguous and the companion is sorted by key, so a targeted lookup
  can read a single block by offset without parsing the whole file.

---

## Open Questions

### Enchant Data Fields

The ~270 bytes before the icon string and the remainder after it are
undecoded. They plausibly carry enchant chance, cost, and stat progression per
level, since the file is keyed by enchant level, but no field has been
confirmed. Decoding them is a much larger job than the icon mapping and was not
attempted.

### Items Without a Record

4,655 of the 73,947 LOC item IDs have no level-0 record. Whether these are
unreleased, region-specific, or simply not enchantable is unknown, and it is
also unconfirmed whether they have an icon reachable some other way.

### Second Block String

The optional second string looks like an effect or sound tag
(`ITEM_BIC_HIT_1` through `ITEM_BIC_HIT_4` were observed) and appeared in 46 of
350 sampled blocks, all of them weapons or armour. What consumes it, and whether
other tag families exist, is unconfirmed.

### Key Variant Meaning

The high byte of the key runs 0-25. It was first read as an enchant level, since
the file is named `itemenchant`, but that does not hold up: BDO's visible
enchant range is narrower than 25, and the values do not line up with enchant
levels in the app. Whether the byte is an enchant step, a different upgrade
track, a variant index, or something else is unresolved, so the field is named
`key_variant` and is not displayed. Variant `0` is reliably the base item, which
is the only property the icon index depends on.
