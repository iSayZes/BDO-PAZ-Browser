# `growthpasscategory.dbss` Format

## Purpose

The tabs of the Growth Pass window (`panel_window_growthpass*.luac`): per category a key, a Korean name, an icon texture key and the quest chain its grid holds. Two categories on client 3464:

```text
category 7 -> Game Tips  -> Combine_Etc_GrowthSupport_Icon_Growth -> quest chain 4470
category 9 -> HYPERBOOST -> Combine_Etc_GrowthSupport_Icon_Quest  -> quest chain 4472
```

## Companion Files

| File                            | Required | Role                                                             |
| ------------------------------- | -------- | ---------------------------------------------------------------- |
| `growthpasscategoryoffset.dbss` | Required | `category_key -> (offset, size)` of each record body             |
| `texturestring_combine.xml`     | Optional | Sprite sheet and rectangle of `icon_texture`                     |
| `languagedata_en.loc`           | Optional | Category name, LOC type 107 `str_id1 = category_key`             |

The grid of each category is in [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), keyed by the same `category_key`.

All multi-byte values are little-endian.

## File Layout

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | record_count | `2` on client 3464                                       |
| `+0x04` | ...  | records      | Each record is a u32 copy of its key, then the record body |

## Record Structure

### Record Body (variable)

The offset table points at the body, past the key copy.

| Offset         | Type        | Field          | Notes                                                                |
| -------------- | ----------- | -------------- | -------------------------------------------------------------------- |
| `+0x00`        | u32         | category_key   | Same as the key copy before it and the offset row key                |
| `+0x04`        | u64 + UTF-16 | name_kr       | Length in characters, then the text; keeps `<PAColor>` tags          |
| after name     | u64 + ASCII | icon_texture   | Length in bytes, then a `texturestring_combine.xml` texture ID       |
| after icon     | u16         | quest_chain_id | The quest chain of this category's grid                              |
| `+0x02`        | u8[20]      | unknown tail   | Zero on both records                                                 |

Both strings carry a u64 length prefix, read with `RecordReader.text`.

### Offset Companion: `growthpasscategoryoffset.dbss`

No `PABR` magic and no trailer: a u32 row count, then rows of u32 `category_key`, u32 `offset`, u32 `size`, read by `parse_bare_u32_offset_rows`. On client 3464: key 7 at `8`, 87 bytes; key 9 at `99`, 152 bytes. Sorted by offset, the key copies and bodies fill the file after the count.

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
