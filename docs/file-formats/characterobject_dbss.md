# `characterobject.dbss` Format

## Purpose

Per-character world-object records for placeable objects: house furniture and crafting tools, crops, houses and other buildings, tents, barricades and guild siege towers. Each record carries the object's kind, its model path and, for most records, an inline icon path. Names come from LOC type `6`, the same table `characterstatic.dbss` uses.

Example:

```text
character 1001  kind 2 -> Metal Processing Tool
                          model 00_Common/Crafting/Crafting_Smithing_01.pam
character 16111 kind 2 -> Golden Hand Vase
                          icon  Icon/New_Icon/03_ETC/06_Housing/Pot_Base_48.dds
character 2101  kind 5 -> Velia 4
                          model 02_balenos/velia/balenos_velia_str_house_05.pam
```

## Companion Files

| File                         | Required | Role                                                  |
| ---------------------------- | -------- | ----------------------------------------------------- |
| `characterobjectoffset.dbss` | Required | Maps `character_id` to byte offset and size of record |
| `languagedata_en.loc`        | Optional | Object names via type `6`                             |

All multi-byte values are little-endian. Strings are a u64 byte length followed by ASCII (or UTF-16-LE, where noted) text with no terminator; the high u32 of the length is always `0`.

## File Layout

### `characterobject.dbss`

| Offset  | Type | Field   | Notes                                                     |
| ------- | ---- | ------- | --------------------------------------------------------- |
| `+0x00` | u32  | count   | Record count; observed `5,123` (2026-09-27 client: `5,127`), equal to the offset count |
| `+0x04` | ...  | records | Variable-length records, back to back until end of file   |

Records are contiguous: sorted by offset, each one ends exactly where the next begins, the first starts at `+0x04` and the last ends at end of file. They are **not** stored in key order, so walking the offset table row by row jumps around the file.

### `characterobjectoffset.dbss`

PABR index with a 10-byte row, because the key is a u16.

| Offset  | Type  | Field | Notes                            |
| ------- | ----- | ----- | -------------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                   |
| `+0x04` | u32   | count | Number of rows; observed `5,123` (2026-09-27 client: `5,127`) |

#### Index Row (10 bytes, repeated `count` times)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | character_id | Unique; observed range `1001` to `19617`, unsorted    |
| `+0x02` | u32  | data_offset  | Absolute offset of the record in the main file        |
| `+0x06` | u32  | data_size    | Record size; observed `678` to `56,750`, median `786` |

#### Trailer (12 bytes)

| Offset  | Type | Field       | Observed | Notes                                    |
| ------- | ---- | ----------- | -------- | ---------------------------------------- |
| `+0x00` | u32  | reserved_a  | `0`      | Observed zero                            |
| `+0x04` | u32  | end_of_rows | `51,238` | Byte offset after rows; `8 + count * 10` |
| `+0x08` | u32  | reserved_b  | `0`      | Observed zero                            |

## Record Structure

### Record Prefix (all kinds)

`data_offset` points at the record's own ID, unlike `characterstatic.dbss`, where it points just past it.

| Offset  | Type   | Field        | Notes                                             |
| ------- | ------ | ------------ | ------------------------------------------------- |
| `+0x00` | u16    | character_id | Matches the offset-table key in all 5,123 records |
| `+0x02` | u8     | object_kind  | Selects the record body; see [Object Kinds](#object-kinds) |
| `+0x03` | u8     | unknown_03   | `0` (5,078) or `1` (45)                           |
| `+0x04` | u8     | unknown_04   | `0` (4,930) or `1` (193)                          |
| `+0x05` | u8     | unknown_05   | Always `0`                                        |
| `+0x06` | string | model_path   | ASCII; see below                                  |

`model_path` extensions: `.pam` (4,479), `.srt` (622), `.r3m` (8), `.pcm` (5). A few paths carry a stray trailing character (`"srt "`, `"pam?"`).

### Furniture Body (`object_kind = 2`, 3,963 records)

Follows `model_path`. Verified for every kind-2 record: walking these fields ends exactly at `data_size`.

| Offset   | Type     | Field       | Notes                                                                  |
| -------- | -------- | ----------- | ---------------------------------------------------------------------- |
| `+0x000` | u8[556]  | block       | Fixed block; mostly constant, see [Furniture Block](#furniture-block)  |
| `+0x22C` | string   | action_name | Empty in 3,887 records; else `OBJECT_BED_GoingToBed` (73) or `USE_BATHTUB_PREFARE` (3) |
| ...      | u32      | action_hash | `0` exactly when `action_name` is empty                                |
| ...      | string   | icon_path   | Empty in 9 records                                                     |
| ...      | u8[48]   | tail        | See [Furniture Tail](#furniture-tail)                                  |

#### Furniture Block

The 556-byte block is constant across all kind-2 records except for these bytes. Everything not listed is zero or a fixed pattern of `1` flags and identity-like `1.0f` rows.

| Offset   | Type | Field       | Observed                                                             |
| -------- | ---- | ----------- | -------------------------------------------------------------------- |
| `+0x010` | u8   | unknown_010 | `1` (3,566), `0` (397)                                               |
| `+0x091` | u8   | unknown_091 | `0` (3,936), `1` (27)                                                |
| `+0x0BD` | u8   | unknown_0bd | 7 values; `0` (3,576), `1` (174), `5` (150), `2`, `10`, `4`, `3`     |
| `+0x135` | u8   | unknown_135 | 35 values; `0` (1,486), `17` (632), `10` (374), `38` (243)           |
| `+0x137` | u8   | unknown_137 | 11 values; `0` (3,797), `9` (145)                                    |
| `+0x138` | u8×6 | flags_138   | Six independent `0`/`1` bytes at `+0x138` to `+0x13D`                |
| `+0x156` | u32  | crop_key_a  | `0`, or `57000 + n` on the 385 crop records                          |
| `+0x15A` | u32  | crop_key_b  | `0`, or `57100 + n` on the same records                              |
| `+0x15E` | u8   | unknown_15e | `10` on the crop records, else `0`                                   |
| `+0x17A` | u16  | unknown_17a | 136 values; `0` (809), `10` (498), `25`, `125`, `200`, `100`, `50`   |
| `+0x21B` | u8   | unknown_21b | `100`, or `0` in 13 records (client 3464)                            |
| `+0x21C` | u16  | summon_character | Character the object spawns; `0` when it spawns none             |

On client 3464, `summon_character` names a character in 39 records:
Chicken Feed (1248) spawns Chicken (9099), Haystack (1245) spawns Dairy Cow
(9078), and the `[Oasis]` objects 18951 to 18977 spawn their characters 39801
to 39830 (`[Oasis] Ethan the Butler` 18977 -> `Oasis Ethan` 39830). An earlier
version of this doc read `+0x21B` as a u32, which merged this ID into it.

#### Furniture Tail

| Offset | Type    | Field       | Observed (client 3464, 3,969 kind-2 records)                    |
| ------ | ------- | ----------- | --------------------------------------------------------------- |
| `+0`   | u8[40]  | reserved    | Always zero                                                     |
| `+40`  | u32     | unknown_28  | Always `0xFFFFFFFF`                                             |
| `+44`  | u32     | repair_item | Item ID of the tool's repair item; `0` except in 6 records      |

The 6 `repair_item` records are the crafting tools: Advanced Cooking Utensil
(1033) takes item 757406 Baermalo Hona's Advanced Cooking Repair Tool, and
Morning Light Traditional Alchemy Tool (1535) takes 757574 Morning Light
Traditional Alchemy Repair Tool.

### Structure Body (`object_kind != 2`, 1,160 records)

Houses, buildings, farms, tents, barricades and siege towers. Follows `model_path`. Verified for every structure record of client 3464: walking these fields ends exactly at `data_size` (`test_record_walk.py` walks all records of the installed client).

| Order | Type        | Field           | Notes                                                              |
| ----- | ----------- | --------------- | ------------------------------------------------------------------ |
| 1     | string      | hull_model_path | The model path with a `_HH` or `_HH_NR` suffix                     |
| 2     | string      | hull_name       | Empty when `layer_count` is `0`; houses use `HH_<a>_<b>_<c>_<d>_<e>`, other structures a model name such as `Tower_AdBase_01_HH_NR` |
| 3     | u8          | unknown_flag    | `1` (1,085) or `0` (75)                                            |
| 4     | u32         | layer_count     | Hull layers that follow; `0` to `4`                                |
| 5     | u32         | unknown_b       | Always equal to `layer_count`                                      |
| 6     | ...         | layers          | `layer_count` times, see [Hull Layers](#hull-layers)               |
| 7     | u8[333]     | unknown_block   | Fixed block, not decoded                                           |
| 8     | string      | material_path   | e.g. `Real_ETC/Material/Icon_Real_ETC_Material_Tent_N_00000000.dds`; never empty |
| 9     | u8[16]      | unknown_after_material | Not decoded                                                 |
| 10    | string      | unknown_digits  | ASCII digits; see below                                            |
| 11    | ...         | tail            | [House Tail](#house-tail) when `hull_name` starts with `HH_`, else [Structure Suffix](#structure-suffix) |

On client 3464, `layer_count` is `0` in 220 records (barricades, siege towers and
other guild structures, all with an empty `hull_name`), `1` in 820, `2` in 102,
`3` in 17 and `4` in 1. The records with two or more layers are houses (kinds
`1`, `5` and `9`). `unknown_digits` is `10` in every record except the 25 kind
`1` records, which hold 21 other values from `60` to `900`.

#### Hull Layers

| Order | Type           | Field      | Notes                                       |
| ----- | -------------- | ---------- | ------------------------------------------- |
| 1     | u32            | hull_count | Hulls in this layer; `1` to `17`            |
| 2     | ...            | hulls      | `hull_count` times: a u32 `face_count`, then `face_count * 140` bytes of f32 data |

On client 3464, 2,267 of the 2,321 hulls have 12 faces. Earlier versions of
this doc read `a`, `b` and `hull_count` as one header; the hull count repeats
per layer, so a walk that read it once ended short on every multi-layer house.

#### House Tail

The 865 records whose `hull_name` starts with `HH_` (client 3464: kinds `5`
(815), `1` (25), `9` (17) and `36` (8)).

| Order | Type    | Field          | Notes                                                  |
| ----- | ------- | -------------- | ------------------------------------------------------ |
| 1     | wstring | name_kr        | UTF-16-LE Korean text; see below                       |
| 2     | wstring | description_kr | UTF-16-LE Korean text; see below                       |
| 3     | u8[162] | house_block    | Fixed block, not decoded                               |
| 4     | string  | icon_path      | Set in all 865; e.g. `Icon/New_Icon/03_ETC/06_Housing/2101-1.dds` |
| 5     | string  | icon_path_2    | Set in 17 records, as `<id>-2.dds` or `<id>_2.dds` next to slot 1 |
| 6     | string  | unknown_path_3 | Empty in all 865                                       |
| 7     | string  | unknown_path_4 | Empty in all 865                                       |
| 8     | u8[24]  | house_tail     | Not decoded                                            |

`name_kr` is not the house name. On client 3464, 817 of the 865 records store
the same placeholder pair: `풋내기 대장장이의 집` ("Novice Blacksmith's House")
and a description of that house. Only these records carry their own text:

| Records | `name_kr`                                            | `description_kr`             |
| ------: | ---------------------------------------------------- | ---------------------------- |
| 25      | Guild house names, e.g. `벨리아 길드 하우스`           | `{TextBind:GUILDHOUSE_01}` to `_25` |
| 17      | Annex lines, e.g. `<PAColor0xFFf3d900>알사비의 별채<PAOldColor>\n주문서 : 신체 강화법\n일일 의뢰 : 토벌` | The placeholder story |
| 6       | `대저택`                                              | `대저택`                      |

`icon_path` names the record's own ID (`2101-1.dds`, `3823.dds`) in 686
records; the rest share one, such as the five Radiant Lands, Angavu and
Cheongsa Island houses 3874 to 3878 on `3873.dds`.

#### Structure Suffix

The 295 records whose `hull_name` does not start with `HH_` end in a fixed
234-byte block. Bytes `+0` to `+15` are zero, `+152` is a u16 `0xFFFF` and
`+226` a u32 `0xFFFFFFFF` in all of them; the u8 at `+148` is `0` in the 220
records with an empty `hull_name` and `1` in the other 75. The rest is not
decoded.

### Icon Path

The icon index does not walk the record body; it scans each record for the first `icon/...(dds|png)` match. 4,817 of 5,123 records contain one, and 17 contain more than one; the index keeps the first. Material paths (`Real_ETC/Material/Icon_...`) have no `icon/` folder, so the scan skips them. On client 3464, the 17 records with two matches are the houses with an `icon_path_2`, and the first match is their `icon_path`.

The walked `icon_path` (furniture body, or slot 1 of the house tail) gives the same PAZ path as the scan for 5,124 of the 5,129 records of client 3464. On the other five the walked path names no file the client ships, so the index keeps the scan:

| Character | Stored `icon_path`                                       | Scan                                    |
| --------- | -------------------------------------------------------- | --------------------------------------- |
| 15267 to 15269 | `Icon/New_Icon/03_ETC/06_Housing/Rot_Island_OBJ_Deco_20.dds?` (`_21`, `_22`) | Drops the stray `?`; the `.dds` file exists |
| 15031     | `Icon/New_Icon/03_ETC/06_Housing/InHouse_Ber_DPFO_Jukebox_01.pam` | No match, so no own icon |
| 4758      | `Icon/New_Icon/03_ETC/06_Housing/Inhouse_Cash_View_035_SetBdds` | No match, so no own icon |

Two stored forms, which resolve to the same PAZ folder:

| Stored prefix | Records | PAZ path                         |
| ------------- | ------: | -------------------------------- |
| `Icon/`       |   4,622 | `ui_texture/` + stored path      |
| `New_Icon/`   |     195 | `ui_texture/icon/` + stored path |

Paths are lowercased to match PAZ entries. 87% of icons live under `icon/new_icon/03_etc/06_housing`, and most of the rest under `07_productmaterial`.

### Borrowed Item Icons

Many objects store no icon (fences, gardens and tents keep only a material path) or one the client does not ship. The item that places the object usually has a working one, and `itemenchant.dbss` names the placed character at `+0xAA`. When the character icon index is built, a character without a working icon takes its item's icon, if that file exists; a working own icon always wins.

```text
character 2053 [Event] Fence  -> no icon stored
item 58011 [Event] Fence      -> places 2053, icon 06_housing/00058003.dds
character 2053 icon           -> ui_texture/icon/new_icon/03_etc/06_housing/00058003.dds
```

## Object Kinds

Grouped by model folder; the kind numbers are observed, not named by the client.

| Kind | Records | Observed objects                                        |
| ---- | ------: | ------------------------------------------------------- |
| `2`  |   3,963 | Furniture, crafting tools and crops (`Interior_House`, `Crafting`) |
| `5`  |     815 | Town buildings and farms (`*_STR_House_*`, `Products/Farm`) |
| `3`  |      36 | Barricades                                              |
| `8`  |      28 | Guild citadel small sets                                |
| `1`  |      25 | Houses                                                  |
| `0`  |      17 | Farming fences and gardens (14, e.g. `[Event] Fence`), plus two tents and a drilling facility; models reuse `Tent/Minifarm_Housing_*` |
| `9`  |      17 | Valencia extra houses                                   |
| `10` to `15`, `17` to `19`, `22` to `26`, `29`, `35` | 1 to 23 each | One guild tower or siege structure type each |
| `4`, `6`, `7`, `20`, `21`, `27`, `28`, `34`, `36`, `37` | 4 to 16 each | Citadel sets, mines, barricade doors, mixed siege objects, mansion bases |

## Suggested UI Layout

| Column       | Type | Notes                                                      |
| ------------ | ---- | ---------------------------------------------------------- |
| Character ID | num  | `character_id`, right-aligned                              |
| Icon         | icon | `IconKind.CHARACTER` lookup, so overrides apply; dash when none |
| Name         | text | LOC type `6`; shown only when LOC is loaded                |
| Item ID      | num  | `lookup(IndexKind.CHARACTER_ITEM, character_id)`; dash for characters named by zero or several items |
| Item         | text | LOC type `0` for the item ID, in its grade colour (`ITEM_GRADE`); shown only when LOC is loaded |
| Kind         | num  | `object_kind`                                              |
| Model        | text | `model_path`                                               |

The handler parses only the record prefix. It does not fall back to `name_kr` when LOC type `6` has no name: on client 3464 the only houses a LOC leaves unnamed are 3874 to 3878 in `languagedata_ru.loc` (the en, de, fr and sp files name all 865), and all five store the placeholder `풋내기 대장장이의 집`.

## Notes

- This file stores icon paths for 4,817 of the 24,418 character IDs in `characterstaticoffset.dbss`; 4,608 of them exist in the PAZ. The rest of the IDs are NPCs, monsters and similar entries with no world-object record.
- Borrowing item icons raises the character index to 6,157 entries, 6,068 of them working (24.9% of all character IDs, up from 18.9%); pets gain icons this way too. 89 paths still point at icons the client does not ship; fix those with `icon_overrides.json`.
- Before the `New_Icon/` form was handled, those 195 records resolved to `ui_texture/icon/03_etc/...`, dropping the `new_icon/` level, and all of them pointed at files that do not exist.
- The `CHARACTER_ITEM` index (the item that places or summons the character, from `itemenchant.dbss` `+0xAA`) links 3,964 of the 5,127 records on client 3458.
- LOC type `6` names 5,020 of the 5,123 records; most of the rest are mansion props (`DecoPropMansion`).
- `crop_key_a`/`crop_key_b` are not item IDs: item `57001` is a Striker costume, while character `1201` with `crop_key_a = 57001` is Pepper Crop.

## Open Questions

### Furniture Block Fields

Only about 20 of the 556 block bytes vary. `unknown_17a` takes round values (`10`, `25`, `50`, `100`, `125`, `200`) that fit interior points, and the u8 `unknown_21b` is `100` almost everywhere, but neither has been matched to in-game data.

### Structure Body Blocks

The walk crosses `unknown_block` (333 bytes), `unknown_after_material` (16), `house_block` (162), `house_tail` (24) and the 234-byte structure suffix without decoding them. Also open: whether a hull layer is a house floor (only houses have two or more), what `unknown_flag` and `unknown_b` select, and what the 21 `unknown_digits` values of the kind `1` records (`60` to `900`) measure.

### Kind Names

The `object_kind` values group cleanly by model folder, but no client table naming them has been found. `unknown_03`, `unknown_04` and the house `hull_name` parts are also unexplained.
