# `growthpasscategory.dbss` Format

## Purpose

The tabs of the Growth Pass window (`panel_window_growthpass*.luac`): per category a key, a Korean name, an icon texture key and the quest chain its grid holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records                 | Row bytes                 |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------------- | ------------------------- |
| 1      | 3473 and later | 3473    | `growthpasscategory.dbss`       | 251   | 2 Record Body, 2 Record | 87 to 152, 120 on average |
| 1      | 3473 and later | 3473    | `growthpasscategoryoffset.dbss` | 28    | 2 Offset Row            | 12                        |

| Layout | File                            | Known         | Unknown      |
| ------ | ------------------------------- | ------------- | ------------ |
| 1      | `growthpasscategory.dbss`       | 211 B (84.1%) | 40 B (15.9%) |
| 1      | `growthpasscategoryoffset.dbss` | 28 B (100.0%) | 0 B (0.0%)   |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                             |
| ------------------------------- | -------- | ---------------------------------------------------------------- |
| `growthpasscategoryoffset.dbss` | Required | `category_key -> (offset, size)` of each record body             |
| `texturestring_combine.xml`     | Optional | Sprite sheet and rectangle of `icon_texture`                     |
| `languagedata_en.loc`           | Optional | Category name, LOC type 107 `str_id1 = category_key`             |

The grid of each category is in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), keyed by the same `category_key`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field        | Notes              |
| ------- | -------------------- | ------------ | ------------------ |
| `+0x00` | u32                  | record_count | `2` on client 3464 |
| `+0x04` | Record[record_count] | records      | See Record         |

### Record (variable: 4 bytes + body)

| Offset  | Type        | Field | Notes                               |
| ------- | ----------- | ----- | ----------------------------------- |
| `+0x00` | u32         | key   | Copy of the record's key            |
| `+0x04` | Record Body | body  | The offset row points at this field |

### Record Body (variable: 42 bytes + name and icon text)

The offset table points at the body, past the key copy.

| Offset              | Type      | Field           | Notes                                                                |
| ------------------- | --------- | --------------- | -------------------------------------------------------------------- |
| `+0x00`             | u32       | category_key    | Same as the key copy before it and the offset row key                |
| `+0x04`             | str16     | name_kr         | Length in characters, then the text; keeps `<PAColor>` tags          |
| `name_kr+0x00`      | str8      | icon_texture    | Length in bytes, then a `texturestring_combine.xml` texture ID       |
| `icon_texture+0x00` | u16       | quest_chain_id  | The quest chain of this category's grid                              |
| `icon_texture+0x02` | bytes[20] | unknown_tail_02 | Zero on both records                                                 |

Both strings carry a u64 length prefix, read with `RecordReader.text`.

### `growthpasscategoryoffset.dbss`

No `PABR` magic and no trailer: a u32 row count, then rows of u32 `category_key`, u32 `offset`, u32 `size`, read by `parse_bare_u32_offset_rows`. On client 3464: key 7 at `8`, 87 bytes; key 9 at `99`, 152 bytes. Sorted by offset, the key copies and bodies fill the file after the count.

| Offset  | Type                  | Field     | Notes                 |
| ------- | --------------------- | --------- | --------------------- |
| `+0x00` | u32                   | row_count | Number of offset rows |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                              |
| ------- | ---- | ------------ | ---------------------------------- |
| `+0x00` | u32  | category_key | Record key                         |
| `+0x04` | u32  | offset       | Absolute offset of the record body |
| `+0x08` | u32  | size         | Size of the record body            |

## Category Keys

`panel_window_growthpass.luac` sets `_hyperBoostCategoryKeyList = {9}`: the window sorts Hyper Boost categories first, then the rest in file order. It reads the name through `categoryWrapper:getCategoryName()` and the icon through `getIconTextureId()`.

LOC type 107 names keys 1 to 9 (`Quest/`, `PvE`, `Gathering`, `Farming/`, `Hunting/`, `Training`, `Game Tips`, `Guaranteed`, `HYPERBOOST`), but only 7 and 9 have a record on client 3464. `growthpassquestlist.bss` holds nine quest chains, 4464 to 4472; on client 3464 only 4470 and 4472 belong to a category.

## Notes

- Decompressed sizes on client 3464: `251` bytes, offset companion `28` bytes.
- calpheonlabs has no page for this table.
- `test_handler.py` checks that the records fill the file and that every icon key resolves; the layout tests check that each grid's quests are the chain its category names.

## Open Questions

### Unknown Tail

The 20 bytes after `quest_chain_id` are zero on both records. `ToClient_requestCategoryRewardItem(categoryKey, rewardIndex)` in `panel_window_growthpass_2.luac` claims a category reward, so a reward list could live here when a category has one; no record shows it.
