# `plantexchangegroup.bss` Format

## Purpose

Worker production groups. Each row is one production key: `plantzone.dbss` points at it from `production_key`, and the row names the [`itemexchangesource.bss`](itemexchangesource_bss.md) exchange the node works, whose product and luck drop groups list the items it produces. Each row also carries a Korean label of the form "node - work type".

The row size and the join fields match [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), which leaves the `+0x5A` tail unmapped; it is the label's string table index.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes  | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------ | ------------------------ | --------- |
| 2      | 3473 and later | 3474    | `plantexchangegroup.bss` | 45,631 | 403 Production Group Row | 94        |
| 1      | 1784           | 1784    | `plantexchangegroup.bss` | 20,224 | 287 Production Group Row | 52        |

| Layout | File                     | Known            | Unknown          |
| ------ | ------------------------ | ---------------- | ---------------- |
| 2      | `plantexchangegroup.bss` | 11,779 B (25.8%) | 33,852 B (74.2%) |
| 1      | `plantexchangegroup.bss` | 8,170 B (40.4%)  | 12,054 B (59.6%) |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                              |
| ---------------------- | -------- | ----------------------------------------------------------------- |
| `plantzone.dbss`       | Optional | The zones that use each production key, for the English name      |
| `plantzoneoffset.dbss` | Optional | Index into `plantzone.dbss`                                       |
| `languagedata_en.loc`  | Optional | Node names (LOC type 29) and item names (LOC type 0)              |

Each zone's parent node comes from the `NODE_PARENT` lookup index (see `docs/handler.md`), built from `exploration.bss` and the worldmap links, so the preview opens no worldmap companion. The exchange key is resolved through [`itemexchangesource.bss`](itemexchangesource_bss.md), [`itemmaingroup.bss`](itemmaingroup_bss.md) and [`itemsubgroup.dbss`](itemsubgroup_dbss.md) (see Field Names); the preview reads the items from the `PRODUCTION_ITEMS` and `PRODUCTION_LUCK_ITEMS` lookup indexes and the exchange name from `EXCHANGE_NAME_KR` (see `docs/handler.md`) instead of opening the 3 MB and 13 MB tables as companions.

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

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
| `+0x06` | u32       | exchange_key       | First item exchange key, an `itemexchangesource.bss` row; observed `40001`-`45019`, see Field Names |
| `+0x0A` | bytes[80] | unknown_0a         | Always all zero; exchange key slots 2 to 21, see Field Names            |
| `+0x5A` | u32       | name_ref           | String table index of the Korean group label; unaligned                 |

`name_ref` covers every one of the 275 strings. Rows that share a label share the index (keys 1773 and 1774 are both "마지막 순례길 - 채집"). Most labels are "node - work type"; some use one phrase with no dash, such as "고대인의 석실 발굴" or "생선 건조장".

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings                    |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, Korean labels   |

## Layout 1

On client 1784 a row is 52 bytes: `unknown_0a` is 38 bytes instead of 80, so
`name_ref` sits at `+0x30`. Only the Production Group Row differs from
Layout 2.

### Production Group Row (52 bytes)

| Offset  | Type      | Field             | Notes                                   |
| ------- | --------- | ----------------- | --------------------------------------- |
| `+0x00` | u16       | production_key    |                                         |
| `+0x02` | u16       | unknown_02        | Equals `production_key` on client 1784  |
| `+0x04` | u16       | unknown_04        | Always `0` on client 1784               |
| `+0x06` | u32       | exchange_key      |                                         |
| `+0x0A` | bytes[38] | unknown_0a        | Always all zero on client 1784          |
| `+0x30` | u32       | name_ref          | String table index of the Korean group label |

## `exchange_key` Values

On client 3474, 401 of the 403 exchange keys are distinct; 42170 is shared by keys 1541 and 1542, 43165 by 1505 and 1930. Every one is an `itemexchangesource.bss` row of `exchange_type` 4 (Plant). The thousands band loosely follows the work type of the label, but every band holds exceptions, so it is not a rule:

| Band    | Mostly                                      |
| ------- | ------------------------------------------- |
| `40xxx` | Farming (재배, 농장) and crop specialties    |
| `41xxx` | Mining (채광, 광산, 광맥)                    |
| `42xxx` | Lumbering (벌목)                            |
| `43xxx` | Gathering (채집)                            |
| `44xxx` | Excavation, drying yards, finance, specialties |
| `45xxx` | Keys 1929 (통발) and 1931 (발굴)               |

The exchange key, its product drop group and that group's subgroup often share one number, but not always: 37 exchange keys have no `itemsubgroup.dbss` subgroup of the same number (client 3474). 36 of them are the exchanges of the 36 `plantzone.dbss` zones that showed no items while the handler read `+0x06` as a subgroup key; the 37th is exchange 45019 of key 1931, which no zone uses. All 37 have a product drop group.

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

The exchange key is the key of an [`itemexchangesource.bss`](itemexchangesource_bss.md) row (`gc::ItemExchangeSourceStaticStatus`, server `ItemExchangeSource`), not an item subgroup. That struct holds `_productItemDropKey` and `_npcWorkerDropKeyForLuck` (`product_drop_key` and `luck_drop_key` in the reader), both keys of [`itemmaingroup.bss`](itemmaingroup_bss.md) groups, and each group lists the subgroups. The client chain, which the handler follows, is:

```text
production_key -> exchange_key (+0x06)
  -> itemexchangesource.bss row -> product_drop_key, luck_drop_key
  -> itemmaingroup.bss group -> itemsubgroup.dbss subgroups -> items
1928 -> exchange 42356 -> product group 42356 (Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap), luck group 44961
```

Earlier versions of the handler read `+0x06` as an `itemsubgroup.dbss` key. That gave the right items on most rows because the exchange key, its drop group and the group's subgroup often share one number, as for 1928 above. On client 3474 the chain changes this against the subgroup reading:

| Rows (client 3474) | Effect of the chain                                                        |
| ------------------ | -------------------------------------------------------------------------- |
| 37                 | Gain items where the subgroup reading found none: the 36 zones of `plantzone.dbss` Open Questions and key 1931 |
| 18                 | Get other items: 1899 "Neruda Plain - Lumbering" (exchange 42194) showed Coal and drops Acacia Timber; 12, 22 and 23 (Excavation) drop group 44013, 44023 and 44025 instead of subgroup 44012, 44022 and 44023 |
| 348                | Keep the same items                                                        |
| 335                | Gain a luck drop group with items                                          |

All 403 exchange keys have a product drop group with items, the Investment Bank rows (keys 901 to 936, 1689, 1690) included. The preview shows the exchange name and links it to its `itemexchangesource.bss` row, then the product items and the luck items.

`+0x02` (equal to `production_key`) and `+0x04` keep their offsets: `+0x04` is `0` on every row while the server's `ContentsGroupKey` is set on 194 of the shared rows.
