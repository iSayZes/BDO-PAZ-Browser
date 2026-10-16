# `plantexchangegroup.bss` Format

## Purpose

Worker production groups. Each row is one production key: `plantzone.dbss` points at it from `production_key`, and the row links to the `itemsubgroup.dbss` subgroup that lists the items the node produces. Each row also carries a Korean label of the form "node - work type".

The row size and the join fields match [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), which leaves the `+0x5A` tail unmapped; it is the label's string table index.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                              |
| ---------------------- | -------- | ----------------------------------------------------------------- |
| `plantzone.dbss`       | Optional | The zones that use each production key, for the English name      |
| `plantzoneoffset.dbss` | Optional | Index into `plantzone.dbss`                                       |
| `languagedata_en.loc`  | Optional | Node names (LOC type 29) and item names (LOC type 0)              |

Each zone's parent node comes from the `NODE_PARENT` lookup index (see `docs/handler.md`), built from `exploration.bss` and the worldmap links, so the preview opens no worldmap companion. The subgroup key is resolved through [`itemsubgroup.dbss`](itemsubgroup_dbss.md); the preview reads those items from the `PRODUCTION_ITEMS` lookup index (see `docs/handler.md`) instead of opening the 13 MB table as a companion.

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

PABR block with fixed 94-byte rows followed by the same counted string table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md).

| Offset              | Type                        | Field              | Notes                                                 |
| ------------------- | --------------------------- | ------------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]                     | magic              | ASCII `PABR`                                          |
| `+0x04`             | u32                         | count              | Number of rows; `403` on the 2026-09-27 client        |
| `+0x08`             | Production Group Row[count] | rows               | 94-byte rows repeated `count` times                   |
| `rows+0x00`         | String Table                | string_table       | Counted string table, see [`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings) |
| `string_table+0x00` | u32                         | string_table_start | Equals `8 + count * 94` (`37,890`)                    |
| `string_table+0x04` | u32                         | zero               | Always `0`                                            |

Rows are not sorted by key; the file opens with key 1775 and ends with keys 1, 31, 23, 22, 21.

### Production Group Row (94 bytes)

| Offset  | Type      | Field              | Notes                                                                   |
| ------- | --------- | ------------------ | ----------------------------------------------------------------------- |
| `+0x00` | u16       | production_key     | Join from `plantzone.dbss` `production_key`; unique, observed `1`-`2044` |
| `+0x02` | u16       | unknown_02         | Equals `production_key` on all 403 rows                                  |
| `+0x04` | u16       | unknown_04         | Always `0`                                                              |
| `+0x06` | u32       | item_subgroup_key  | First `itemexchangesource.bss` key, read as an `itemsubgroup.dbss` key; observed `40001`-`45019`, see Field Names |
| `+0x0A` | bytes[80] | unknown_0a         | Always all zero; exchange key slots 2 to 21, see Field Names            |
| `+0x5A` | u32       | name_ref           | String table index of the Korean group label; unaligned                 |

`name_ref` covers every one of the 275 strings. Rows that share a label share the index (keys 1773 and 1774 are both "마지막 순례길 - 채집"). Most labels are "node - work type"; some use one phrase with no dash, such as "고대인의 석실 발굴" or "생선 건조장".

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings                    |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, Korean labels   |

## `item_subgroup_key` Values

401 of the 403 subgroup keys are distinct; 42170 is shared by keys 1541 and 1542, 43165 by 1505 and 1930. The thousands band loosely follows the work type of the label, but every band holds exceptions, so it is not a rule:

| Band    | Mostly                                      |
| ------- | ------------------------------------------- |
| `40xxx` | Farming (재배, 농장) and crop specialties    |
| `41xxx` | Mining (채광, 광산, 광맥)                    |
| `42xxx` | Lumbering (벌목)                            |
| `43xxx` | Gathering (채집)                            |
| `44xxx` | Excavation, drying yards, finance, specialties |
| `45xxx` | Keys 1929 (통발) and 1931 (발굴), both missing from the index |

37 subgroup keys are absent from `itemsubgroupoffset.dbss`. 36 of them are the unresolved `plantzone.dbss` zones (see its Open Questions); the 37th is subgroup 45019 of key 1931, which no zone uses.

## English Names

No LOC type holds the labels, and the EU client ships no Korean LOC to match them against. The worker manager (`new_worldmap_workmanager_plant.luac`) reads a per-group description through `ToClient_getPlantWorkableItemExchangeDescriptionByIndex` into `_workName` but never shows it; the panel shows the product's item name. The two halves of the label can be rebuilt in English from the worldmap nodes:

```text
production_key -> plantzone.dbss zone record_id (a sub-node) -> LOC type 29 "Lumbering"
zone -> NODE_PARENT (its one link in mapdata_realexplore2.bwp) -> LOC type 29 "Platerra Mountains"
1928 -> "Platerra Mountains - Lumbering"  (Korean: 플라테르 산맥 - 벌목)
```

Every one of the 439 zones is an `exploration.bss` sub-node with exactly one worldmap link (see [`*.bwp`](waypoint_bwp.md)), so `NODE_PARENT` holds all of them and the preview names a zone with `node_with_parent_name()` from `_common/node.py`. A key gets a name only when every zone using it gives the same one; on client 3458 that is 365 of the 403 keys. The rest keep the Korean label: keys no zone uses (1931 and seven more), and keys shared by zones under different nodes, where the Korean label names a region instead (1231 칼페온 채집, Calpheon gathering, over Karanda Ridge and Longleaf Tree Sentry Post). The `exploration.bss` manager family was used before the links and named 324: it has no main node for some families (Godu Village, 1880) and the wrong one for Specialties 1563 (Areha Palm Forest instead of Arehaza, key 992 아레하자 마을 - 특산품). Investment banks read "Altinova - Gulabi Investment Bank" where the Korean label is only the bank name (928 굴라비 자산 관리소). The English halves follow the worldmap names, not the Korean wording: 1545 "가비냐 대분화구 - 티타늄" (titanium) becomes "Gavinya Great Crater - Mining", and 1203 "칼페온 파프리카 재배" (Calpheon paprika farming) becomes "Northern Wheat Plantation - Paprika Farming".

## Notes

- All 439 `plantzone.dbss` zones on the 2026-09-27 client resolve to a row. 8 keys are not used by any zone: 1503, 1675, 1676, 1931, 2015, 2021, 2036, 2037.
- `production_key` equals the zone's `record_id` for 157 of the 439 zones; the two are separate key spaces, and several zones share one key (1521 and 1934 are used by four zones each).
- LOC type 29 at `str_id1=production_key` gives a node name only by coincidence, when the key equals a node key; use the zone's `record_id` for the node name. That name is the sub-node, the work-type half of the label ("Lumbering", "Teff"); see English Names for the node half.
- bdo-data-extractor calls `+0x06` the "normal-output subgroup". The luck drops are not in this file: they hang off the item exchange (see Field Names).

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::PlantExchangeGroupStaticStatus` holds `_key`, `_isBlockedNpcWork`, `_name` and `_exchangeKeyGroup`, an array of 21 item exchange keys. The server-side `PlantExchangeGroup_Table` of a private server on client 519 has the columns `Index`, `ExchangeGroupName`, `ExchangeKey_0` to `ExchangeKey_20` and `ContentsGroupKey`. It shares 273 production keys with client 3464; on 265 of them `ExchangeKey_0` equals `+0x06`, no other exchange key is set, and `ExchangeGroupName` equals the Korean label. `+0x06` and the 80 zero bytes after it are 21 u32 slots, so `+0x06` is the first exchange key.

The exchange key is the key of an `itemexchangesource.bss` row (`gc::ItemExchangeSourceStaticStatus`, server `ItemExchangeSource`), not an item subgroup. That struct holds `_productItemDropKey` and `_npcWorkerDropKeyForLuck`, both keys of [`itemmaingroup.bss`](itemmaingroup_bss.md) groups, and each group lists the subgroups. The client chain is:

```text
production_key -> exchange key (+0x06)
  -> itemexchangesource.bss row -> product drop key, luck drop key
  -> itemmaingroup.bss group -> itemsubgroup.dbss subgroups -> items
```

The handler reads `+0x06` as a subgroup key. That gives the right items on most rows because the exchange key, its drop group and the group's subgroup often share one number (exchange 1928's key 42356 drops group 42356, which lists subgroup 42356). In client 3464's `itemexchangesource.bss` the product drop key of a worker row is the u32 at row `+0x55` and the luck drop key the u32 at `+0x59` (42356: `42356`, `44961`). Reading those two (found by the doubled-key row head, not by a full reader) gives:

| Rows (client 3464) | Effect of the full chain                                                   |
| ------------------ | -------------------------------------------------------------------------- |
| 37                 | Resolve where the subgroup reading finds nothing: all 36 unresolved zones and key 1931 |
| 18                 | Get other items: 1899 "Neruda Plain - Lumbering" shows Coal today and drops Acacia Timber; 12, 22 and 23 (Excavation) drop group 44013, 44023 and 44025 instead of subgroup 44012, 44022 and 44023 |
| 335                | Gain a luck drop group                                                     |
| 25                 | Stay open: the Investment Bank rows (keys 901 to 936, 1689, 1690) hold no group key at `+0x55`, so their row layout differs |

`+0x02` (equal to `production_key`) and `+0x04` keep their offsets: `+0x04` is `0` on every row while the server's `ContentsGroupKey` is set on 194 of the shared rows. Switching the handler to the full chain needs a reader for `itemexchangesource.bss` first.
