# `characterobject.dbss` Format

## Purpose

Per-character world-object records for placeable objects: house furniture and crafting tools, crops, houses and other buildings, tents, barricades and guild siege towers. Each record carries the object's kind, its model path and, for most records, an inline icon path. Names come from LOC type `6`, the same table `characterstatic.dbss` uses.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                  |
| ---------------------------- | -------- | ----------------------------------------------------- |
| `characterobjectoffset.dbss` | Required | Maps `character_id` to byte offset and size of record |
| `languagedata_en.loc`        | Optional | Object names via type `6`                             |

All multi-byte values are little-endian. Strings are a u64 length followed by ASCII (`str8`, length in bytes) or UTF-16-LE (`str16`, length in code units) text with no terminator; the high u32 of the length is always `0`.

## Layout 1

### File Layout

Records are contiguous: sorted by offset, each one ends exactly where the next begins, the first starts at `+0x04` and the last ends at end of file. They are **not** stored in key order, so walking the offset table row by row jumps around the file.

| Offset  | Type          | Field   | Notes                                                     |
| ------- | ------------- | ------- | --------------------------------------------------------- |
| `+0x00` | u32           | count   | Record count; observed `5,123` (2026-09-27 client: `5,127`), equal to the offset count |
| `+0x04` | Record[count] | records | Variable-length records, back to back until end of file   |

### Record (variable: 14 bytes + model path and body, size from `characterobjectoffset.dbss`)

`data_offset` points at the record's own ID, unlike `characterstatic.dbss`, where it points just past it.

| Offset                | Type                               | Field          | Notes                                             |
| --------------------- | ---------------------------------- | -------------- | ------------------------------------------------- |
| `+0x00`               | u16                                | character_id   | Matches the offset-table key in all 5,123 records |
| `+0x02`               | u8                                 | object_kind    | Selects the record body; see [Object Kinds](#object-kinds) |
| `+0x03`               | u8                                 | is_siege_tent  | `1` on 45 records, all of kinds 4, 6 and 8 (forts, field HQs, command posts), else `0` |
| `+0x04`               | u8                                 | unknown_04     | `1` on 193 siege buildings (barricades, flame towers, hwachas, factories), else `0` |
| `+0x05`               | u8                                 | unknown_05     | Always `0`                                        |
| `+0x06`               | str8                               | model_path     | ASCII; see below                                  |
| `model_path+0x00`     | Furniture Body if object_kind = 2  | furniture_body | See Furniture Body                                |
| `furniture_body+0x00` | Structure Body if object_kind != 2 | structure_body | See Structure Body                                |

`model_path` extensions: `.pam` (4,479), `.srt` (622), `.r3m` (8), `.pcm` (5). A few paths carry a stray trailing character (`"srt "`, `"pam?"`).

### Furniture Body (variable: 624 bytes + action name and icon path)

The body of the `object_kind = 2` records (3,963 records). Follows `model_path`. Verified for every kind-2 record: walking these fields ends exactly at `data_size`.

| Offset             | Type            | Field       | Notes                                                                  |
| ------------------ | --------------- | ----------- | ---------------------------------------------------------------------- |
| `+0x000`           | Furniture Block | block       | Fixed block; mostly constant, see Furniture Block                      |
| `+0x22C`           | str8            | action_name | Empty in 3,887 records; else `OBJECT_BED_GoingToBed` (73) or `USE_BATHTUB_PREFARE` (3) |
| `action_name+0x00` | u32             | action_hash | `0` exactly when `action_name` is empty                                |
| `action_name+0x04` | str8            | icon_path   | Empty in 9 records                                                     |
| `icon_path+0x00`   | Furniture Tail  | tail        | See Furniture Tail                                                     |

### Furniture Block (556 bytes)

The 556-byte block is constant across all kind-2 records except for the bytes with values in Notes. The rows with "Constant" are zero or a fixed pattern of `1` flags and identity-like `1.0f` rows.

| Offset   | Type       | Field                        | Notes                                                                |
| -------- | ---------- | ---------------------------- | -------------------------------------------------------------------- |
| `+0x000` | bytes[16]  | unknown_000                  | Constant                                                             |
| `+0x010` | u8         | unknown_010                  | `1` (3,566), `0` (397)                                               |
| `+0x011` | bytes[128] | unknown_011                  | Constant                                                             |
| `+0x091` | u8         | unknown_091                  | `0` (3,936), `1` (27)                                                |
| `+0x092` | bytes[43]  | unknown_092                  | Constant                                                             |
| `+0x0BD` | u8         | unknown_0bd                  | 7 values; `0` (3,576), `1` (174), `5` (150), `2`, `10`, `4`, `3`     |
| `+0x0BE` | bytes[119] | unknown_0be                  | Constant                                                             |
| `+0x135` | u8         | installation_type            | `CppEnums.InstallationType`: `0` Default (1,486), `17` Buff (632), `10` Havest (374), `38` MansionTree (243) ... |
| `+0x136` | u8         | unknown_136                  | Constant                                                             |
| `+0x137` | u8         | reference_action_object_type | 11 values; `0` (3,797), `9` (145)                                    |
| `+0x138` | u8         | is_inside                    | Place flag: where it can be placed, `0` or `1`                       |
| `+0x139` | u8         | is_outside                   | Place flag                                                           |
| `+0x13A` | u8         | is_floor                     | Place flag                                                           |
| `+0x13B` | u8         | is_wall                      | Place flag                                                           |
| `+0x13C` | u8         | is_on_the_table              | Place flag                                                           |
| `+0x13D` | u8         | is_carpet                    | Place flag                                                           |
| `+0x13E` | bytes[3]   | unknown_13e                  | Constant                                                             |
| `+0x141` | f32        | installation_effect_radius   | Set on 9 records the server shares (client 3464)                     |
| `+0x145` | u8         | installation_effect_type     | Set on the same 9 records                                            |
| `+0x146` | bytes[16]  | unknown_146                  | Constant                                                             |
| `+0x156` | u32        | product_recipe_key           | `0`, or `57000 + n` on the 385 crop records                          |
| `+0x15A` | u32        | seed_recipe_key              | `0`, or `57100 + n` on the same records                              |
| `+0x15E` | u8         | explore_exp                  | `10` on the crop records, else `0`                                   |
| `+0x15F` | bytes[19]  | unknown_15f                  | Constant                                                             |
| `+0x172` | u64        | using_time                   | Set on 105 records the server shares (client 3464)                   |
| `+0x17A` | u16        | interior_point               | Interior points of the furniture; 136 values; `0` (809), `10` (498), `25`, `125`, `200`, `100`, `50` |
| `+0x17C` | bytes[154] | unknown_17c                  | Constant                                                             |
| `+0x216` | u32        | audio_bank_no                | Set on 30 records the server shares (client 3464)                    |
| `+0x21A` | u8         | unknown_21a                  | Constant                                                             |
| `+0x21B` | u8         | unknown_21b                  | `100`, or `0` in 13 records (client 3464)                            |
| `+0x21C` | u16        | summon_character             | Character the object spawns; `0` when it spawns none                 |
| `+0x21E` | u16        | material_index               | Set on 103 records the server shares (client 3464)                   |
| `+0x220` | f32[3]     | relocate_position            | Where the character stands to use the object; set on 44 of them      |

On client 3464, `summon_character` names a character in 39 records:
Chicken Feed (1248) spawns Chicken (9099), Haystack (1245) spawns Dairy Cow
(9078), and the `[Oasis]` objects 18951 to 18977 spawn their characters 39801
to 39830 (`[Oasis] Ethan the Butler` 18977 -> `Oasis Ethan` 39830). An earlier
version of this doc read `+0x21B` as a u32, which merged this ID into it.

### Furniture Tail (48 bytes)

Observed values are from client 3464, 3,969 kind-2 records.

| Offset  | Type      | Field       | Notes                                                      |
| ------- | --------- | ----------- | ---------------------------------------------------------- |
| `+0x00` | bytes[40] | unknown_00  | Always zero                                                |
| `+0x28` | u32       | unknown_28  | Always `0xFFFFFFFF`                                        |
| `+0x2C` | u32       | repair_item | Item ID of the tool's repair item; `0` except in 6 records |

The 6 `repair_item` records are the crafting tools: Advanced Cooking Utensil
(1033) takes item 757406 Baermalo Hona's Advanced Cooking Repair Tool, and
Morning Light Traditional Alchemy Tool (1535) takes 757574 Morning Light
Traditional Alchemy Repair Tool.

### Structure Body (variable: 390 bytes + paths and hulls)

The body of the `object_kind != 2` records (1,160 records): houses, buildings, farms, tents, barricades and siege towers. Follows `model_path`. Verified for every structure record of client 3464: walking these fields ends exactly at `data_size` (`test_record_walk.py` walks all records of the installed client).

The tail is a House Tail when `hull_name` starts with `HH_`, else a Structure Suffix.

| Offset                 | Type                                  | Field                  | Notes                                                              |
| ---------------------- | ------------------------------------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`                | str8                                  | hull_model_path        | The model path with a `_HH` or `_HH_NR` suffix                     |
| `hull_model_path+0x00` | str8                                  | hull_name              | Empty when `layer_count` is `0`; houses use `HH_<a>_<b>_<c>_<d>_<e>`, other structures a model name such as `Tower_AdBase_01_HH_NR` |
| `hull_name+0x00`       | u8                                    | unknown_flag           | `1` (1,085) or `0` (75)                                            |
| `hull_name+0x01`       | u32                                   | layer_count            | Hull layers that follow; `0` to `4`                                |
| `hull_name+0x05`       | u32                                   | unknown_b              | Always equal to `layer_count`                                      |
| `hull_name+0x09`       | Hull Layer[layer_count]               | layers                 | `layer_count` times, see Hull Layer                                |
| `layers+0x00`          | bytes[333]                            | unknown_block          | Fixed block, not decoded                                           |
| `layers+0x14D`         | str8                                  | material_path          | e.g. `Real_ETC/Material/Icon_Real_ETC_Material_Tent_N_00000000.dds`; never empty |
| `material_path+0x00`   | bytes[16]                             | unknown_after_material_path | Not decoded                                                        |
| `material_path+0x10`   | str8                                  | unknown_digits         | ASCII digits; see below                                            |
| `unknown_digits+0x00`  | House Tail if hull_name ^= HH_        | house              | When `hull_name` starts with `HH_`; see House Tail                 |
| `house+0x00`           | Structure Suffix if hull_name !^= HH_ | suffix                 | When `hull_name` does not start with `HH_`; see Structure Suffix   |

On client 3464, `layer_count` is `0` in 220 records (barricades, siege towers and
other guild structures, all with an empty `hull_name`), `1` in 820, `2` in 102,
`3` in 17 and `4` in 1. The records with two or more layers are houses (kinds
`1`, `5` and `9`). `unknown_digits` is `10` in every record except the 25 kind
`1` records, which hold 21 other values from `60` to `900`.

### Hull Layer (variable: 4 bytes + hulls)

| Offset  | Type             | Field      | Notes                            |
| ------- | ---------------- | ---------- | -------------------------------- |
| `+0x00` | u32              | hull_count | Hulls in this layer; `1` to `17` |
| `+0x04` | Hull[hull_count] | hulls      | See Hull                         |

On client 3464, 2,267 of the 2,321 hulls have 12 faces. Earlier versions of
this doc read `a`, `b` and `hull_count` as one header; the hull count repeats
per layer, so a walk that read it once ended short on every multi-layer house.

### Hull (variable: 4 bytes + faces)

| Offset  | Type             | Field      | Notes              |
| ------- | ---------------- | ---------- | ------------------ |
| `+0x00` | u32              | face_count | Faces in this hull |
| `+0x04` | Face[face_count] | faces      | See Face           |

### Face (140 bytes)

| Offset  | Type    | Field      | Notes                 |
| ------- | ------- | ---------- | --------------------- |
| `+0x00` | f32[35] | unknown_00 | f32 data, not decoded |

### House Tail (variable: 234 bytes + text and paths)

The 865 records whose `hull_name` starts with `HH_` (client 3464: kinds `5`
(815), `1` (25), `9` (17) and `36` (8)).

| Offset                | Type       | Field          | Notes                                                             |
| --------------------- | ---------- | -------------- | ----------------------------------------------------------------- |
| `+0x00`               | str16      | name_kr        | UTF-16-LE Korean text; see below                                  |
| `name_kr+0x00`        | str16      | description_kr | UTF-16-LE Korean text; see below                                  |
| `description_kr+0x00` | bytes[162] | house_block    | Fixed block, not decoded                                          |
| `description_kr+0xA2` | str8       | icon_path      | Set in all 865; e.g. `Icon/New_Icon/03_ETC/06_Housing/2101-1.dds` |
| `icon_path+0x00`      | str8       | icon_path_2    | Set in 17 records, as `<id>-2.dds` or `<id>_2.dds` next to slot 1 |
| `icon_path_2+0x00`    | str8       | unknown_path_3 | Empty in all 865                                                  |
| `unknown_path_3+0x00` | str8       | unknown_path_4 | Empty in all 865                                                  |
| `unknown_path_4+0x00` | bytes[24]  | house_tail     | Not decoded                                                       |

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

### Structure Suffix (234 bytes)

The 295 records whose `hull_name` does not start with `HH_` end in a fixed
234-byte block. Bytes `+0` to `+15` are zero, `+152` is a u16 `0xFFFF` and
`+226` a u32 `0xFFFFFFFF` in all of them; the u8 at `+148` is `0` in the 220
records with an empty `hull_name` and `1` in the other 75. The rest is not
decoded.

| Offset  | Type       | Field      | Notes                                                    |
| ------- | ---------- | ---------- | -------------------------------------------------------- |
| `+0x00` | bytes[16]  | unknown_00 | Always `0`                                               |
| `+0x10` | bytes[132] | unknown_10 | Not decoded                                              |
| `+0x94` | u8         | unknown_94 | `0` with an empty `hull_name` (220), `1` in the other 75 |
| `+0x95` | bytes[3]   | unknown_95 | Not decoded                                              |
| `+0x98` | u16        | unknown_98 | Always `0xFFFF`                                          |
| `+0x9A` | bytes[72]  | unknown_9a | Not decoded                                              |
| `+0xE2` | u32        | unknown_e2 | Always `0xFFFFFFFF`                                      |
| `+0xE6` | bytes[4]   | unknown_e6 | Not decoded                                              |

### `characterobjectoffset.dbss`

PABR index with a 10-byte row, because the key is a u16.

| Offset              | Type             | Field        | Notes                                                           |
| ------------------- | ---------------- | ------------ | --------------------------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR` (ASCII)                                                  |
| `+0x04`             | u32              | count        | Number of rows; observed `5,123` (2026-09-27 client: `5,127`)   |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                                   |
| `rows+0x00`         | String Table     | string_table | Empty; observed zero                                            |
| `string_table+0x00` | u32              | end_of_rows  | Byte offset after rows; `8 + count * 10`; observed `51,238`     |
| `string_table+0x04` | u32              | zero         | Observed zero                                                   |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | character_id | Unique; observed range `1001` to `19617`, unsorted    |
| `+0x02` | u32  | data_offset  | Absolute offset of the record in the main file        |
| `+0x06` | u32  | data_size    | Record size; observed `678` to `56,750`, median `786` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `0`                            |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## Icon Path

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

## Borrowed Item Icons

Many objects store no icon (fences, gardens and tents keep only a material path) or one the client does not ship. The item that places the object usually has a working one, and `itemenchant.dbss` names the placed character at `+0xAA`. When the character icon index is built, a character without a working icon takes its item's icon, if that file exists; a working own icon always wins.

```text
character 2053 [Event] Fence  -> no icon stored
item 58011 [Event] Fence      -> places 2053, icon 06_housing/00058003.dds
character 2053 icon           -> ui_texture/icon/new_icon/03_etc/06_housing/00058003.dds
```

## Object Kinds

Grouped by model folder. Kinds `0` to `9` are the members of `gc::ObjectKind` in the 2016 client; the later kinds have no name. The handler shows the name next to the number.

| Kind | Records | Observed objects                                        |
| ---- | ------: | ------------------------------------------------------- |
| `2` Installation |   3,963 | Furniture, crafting tools and crops (`Interior_House`, `Crafting`) |
| `5` InnRoom |     815 | Town buildings and farms (`*_STR_House_*`, `Products/Farm`) |
| `3` Barricade |      36 | Barricades                                              |
| `8` VillageTent |      28 | Guild citadel small sets                                |
| `1` FixedHouse |      25 | Houses                                                  |
| `0` PersonalTent |      17 | Farming fences and gardens (14, e.g. `[Event] Fence`), plus two tents and a drilling facility; models reuse `Tent/Minifarm_Housing_*` |
| `9` Villa |      17 | Valencia extra houses                                   |
| `10` to `15`, `17` to `19`, `22` to `26`, `29`, `35` | 1 to 23 each | One guild tower or siege structure type each |
| `4` KingTent, `6` LordTent, `7` Trap, `20`, `21`, `27`, `28`, `34`, `36`, `37` | 4 to 16 each | Citadel sets, mines, barricade doors, mixed siege objects, mansion bases |

## Notes

- This file stores icon paths for 4,817 of the 24,418 character IDs in `characterstaticoffset.dbss`; 4,608 of them exist in the PAZ. The rest of the IDs are NPCs, monsters and similar entries with no world-object record.
- Borrowing item icons raises the character index to 6,157 entries, 6,068 of them working (24.9% of all character IDs, up from 18.9%); pets gain icons this way too. 89 paths still point at icons the client does not ship; fix those with `icon_overrides.json`.
- Before the `New_Icon/` form was handled, those 195 records resolved to `ui_texture/icon/03_etc/...`, dropping the `new_icon/` level, and all of them pointed at files that do not exist.
- The `CHARACTER_ITEM` index (the item that places or summons the character, from `itemenchant.dbss` `+0xAA`) links 3,964 of the 5,127 records on client 3458.
- LOC type `6` names 5,020 of the 5,123 records; most of the rest are mansion props (`DecoPropMansion`).
- `product_recipe_key`/`seed_recipe_key` are not item IDs: item `57001` is a Striker costume, while character `1201` with `product_recipe_key = 57001` is Pepper Crop. The 2016 client points both at `gc::ItemExchangeSourceStaticStatus`, the item exchange recipes.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ObjectStaticStatus` starts with `_objectKind`, `_isSiegeTent` and `_isSiegeOrFortressTent`, and further on holds `_installationType`, `_subInstallationType`, `_installationActionNumber`, `_installablePlaceFlag[6]`, `_productionFacilityFlag[3]`, `_installationEffectRadius`, `_installationEffectType`, the recipe keys, `_exploreExp`, `_usingTime`, `_interiorSensePoint`, `_audioBankNo`, `_armorMaterial`, `_summonCharacterKey`, `_materialIndexForInstallation`, `_relocatePosForUsing` and `_usingAction`. The furniture block stores its named fields in that order and ends right before `action_name`. The server-side `Object_Table` of a private server on client 519 shares 2,041 furniture records with client 3464:

| Field                        | `Object_Table` column        | Matching non-zero rows |
| ---------------------------- | ---------------------------- | ---------------------: |
| installation_type            | `InstallationType`           | 1,198 of 1,198         |
| reference_action_object_type | `ReferenceActionObjectType`  | 134 of 134             |
| place flags                  | `IsInside`, `IsOutside`, `IsFloor`, `IsWall`, `IsOnTheTable`, `IsCarpet` | 2,035 to 2,041 of 2,041 rows |
| installation_effect_radius, installation_effect_type | `Effect_Radius`, `Effect_Type` | 9 of 9 |
| product_recipe_key, seed_recipe_key | `ProductRecipe`, `SeedRecipe` | 263 of 263, 244 of 244 |
| explore_exp                  | `ExploreExp`                 | 263 of 263             |
| using_time                   | `UsingTime`                  | 105 of 105             |
| interior_point               | `InteriorPoint`              | 1,659 of 1,664         |
| audio_bank_no                | `AudioBankNo`                | 30 of 30               |
| summon_character             | `SummonCharacterKey`         | 27 of 27               |
| material_index               | `MaterialIndex`              | 103 of 103             |
| relocate_position            | `RelocatePosX`, `Y`, `Z`     | 2,041 of 2,041 rows    |

`installation_type` follows `CppEnums.InstallationType` in `global_define_cpp_enum.luac` (`0` Default to `39` EventPersonalTent). `is_siege_tent` has no server column; it is named from the 2016 order and is set only on the King, Lord and Village tent kinds.

## Open Questions

### Furniture Block Fields

Most varying bytes now have names (see Field Names). `unknown_010`, `unknown_091`, `unknown_0bd` and the u8 `unknown_21b` (`100` almost everywhere) match no server column. In the 2016 order `unknown_21b` sits where `_armorMaterial` is, but the server's `ArmorMaterial` is `0` on every row.

### Structure Body Blocks

The walk crosses `unknown_block` (333 bytes), `unknown_after_material_path` (16), `house_block` (162), `house_tail` (24) and the 234-byte structure suffix without decoding them. Also open: whether a hull layer is a house floor (only houses have two or more), what `unknown_flag` and `unknown_b` select, and what the 21 `unknown_digits` values of the kind `1` records (`60` to `900`) measure.

### Later Kind Names

Kinds `10` to `37` came after the 2016 `gc::ObjectKind` and have no name in any client table found so far. `unknown_04` (set on siege buildings, not on the forts) does not fit the 2016 `_isSiegeOrFortressTent` that sits at its place, and the house `hull_name` parts are also unexplained.
