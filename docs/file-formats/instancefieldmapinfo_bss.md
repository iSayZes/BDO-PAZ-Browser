# `instancefieldmapinfo.bss` Format

## Purpose

Map data per instance field: a title and description as UI string keys, a map image, a centre point and radius, an entry item, team spawn
points and several values without a name yet. The key is the
[instancefield.dbss](instancefield_dbss.md) field key.

Example:

```text
key 4001   A1_001
  title INSTANCEDUNGEONDATA_A1_001_NAME  "The Magnus: The Great Single Path"
  desc  INSTANCEDUNGEONDATA_A1_001_DESC  "Everything to one, one returns to everything."
key 101    HorseRace_Glish_Main
  title LUA_HORSERACING_MAP_STAGENAME00  "Mediah: Stonetail Horse Ranch"
  image Combine/Etc/Combine_Etc_horseracing.dds  (1, 1005) to (501, 1165)
key 150    Atoraxion_Desert
  entry item 65992 "Fate Fulfilled: Atoraxxion"
```

## Companion Files

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hashes of the `GAME` sheet keys that `title` and `description` store; without it both columns show the key |
| `languagedata_*.loc`  | Optional | LOC type 37 text under those hashes; item names (LOC type 0) |
| `instancefield.dbss`  | Optional | The internal field name per key, through the `INSTANCE_FIELD_NAME` lookup index |

All multi-byte values are little-endian.

## File Layout

A PABR file with variable-size records and the counted string table that
`exploration.bss` and `npcsimply.bss` also end with (`_common/pabr_strings.py`).
The records end exactly where the string table starts.

| Offset              | Type   | Field              | Notes |
| ------------------- | ------ | ------------------ | ----- |
| `+0x00`             | char[4]| magic              | `PABR` |
| `+0x04`             | u32    | count              | Number of records |
| `+0x08`             | ...    | records            | `count` x record, not sorted by key |
| string_table_start  | ...    | string table       | u32 count, then `count` x (u8 is_wide, u32 byte_length, payload) |
| end - 8             | u32    | string_table_start | Offset of the string table |
| end - 4             | u32    | zero               | `0` |

String table entry 0 is the empty string; a string index of `0` means none.

### Record (196 bytes + lists)

| Offset  | Type     | Field              | Notes |
| ------- | -------- | ------------------ | ----- |
| `+0x00` | u16      | key                | `instancefield.dbss` key |
| `+0x02` | u32      | unknown_02         | `1`, `4`, `6`, `10`, `30`, `40` up to `3000`; see Open Questions |
| `+0x06` | u32      | unknown_06         | `1`, or `2` on team battles (Solare arenas, guild matches, Crimson fields, `PAPUCRIO_ARENA`, `CrewBattle`, `Edania_Field_1vs1`) |
| `+0x0A` | f32[3]   | x, y, z            | World position (centimetres); all `0` when unset |
| `+0x16` | f32      | radius             | Centimetres around that position (`9000` on `Solare_Arena_Reed`); `0` when unset |
| `+0x1A` | u32      | title              | String index of a `GAME` sheet key (`LUA_LOCALWAR_SERVERNAME_MAP_1`, `INSTANCEDUNGEONDATA_A1_001_NAME`) |
| `+0x1E` | u32      | description        | String index of a `GAME` sheet key (`INSTANCEDUNGEONDATA_A1_001_DESC`) |
| `+0x22` | u8       | unknown_22         | `1` on six Crimson field records (keys 11, 12, 17, 18, 22, 24), else `0` |
| `+0x23` | u32      | unknown_23         | Equals `unknown_06` except on `Edania_Field_1vs1` (`1`), horse races (`2`, `3`, `5`) and `Yonggung` (`7`) |
| `+0x27` | u32      | image              | String index of a `.dds` path (`Map_Nest.dds`, `Combine_Etc_horseracing.dds`) |
| `+0x2B` | u16[4]   | image_region       | x1, y1, x2, y2 in pixels of `image`; `0, 0, 1, 1` on the Crimson field maps |
| `+0x33` | u8[106]  | filler             | The same bytes in every record; the 8-byte groups hold `0x00007FFC...` and `0x00000293...` values, which read like memory addresses of the tool that wrote the file |
| `+0x9D` | u8       | unknown_9d         | `1` on the Solare arenas, guild matches, `PAPUCRIO_ARENA` and 8 of the 16 Crimson field records |
| `+0x9E` | u16      | unknown_9e         | `0xFFFF`, or `2`, `4`, `6`, `9` on four `Personal_Instance_*` (Oasis server) maps; see Open Questions |
| `+0xA0` | u8[8]    | zero               | `0` |
| `+0xA8` | u32      | entry_item_id      | Item ID, `0` for none; the "Access Granted" items of Atoraxion |
| `+0xAC` | u32      | unknown_ac         | `1` where `entry_item_id` is set, else `0` |
| `+0xB0` | u32      | zero               | `0` |
| `+0xB4` | u32      | unknown_b4         | `0`, `3600` on the `A1_` fields, `10800` on the Atoraxion Single maps and key 210 |
| `+0xB8` | u32      | zero               | `0` |
| `+0xBC` | u32      | hash_count         | |
| `+0xC0` | u32[n]   | unknown_hashes     | `hash_count` values; only on `A1_` fields (1 to 3 each); not a `stringtable.bss` key hash |
| ...     | u32      | spawn_count        | |
| ...     | f32[3][n]| spawns             | World positions; `2` on every guild match map, one per side, both inside the map's box |
| ...     | f32      | unknown_spawn_f32  | Only when `spawn_count` is not `0`; `200` on all |
| ...     | u32      | unknown_spawn_u32  | Only when `spawn_count` is not `0`; `10` on all |

### Entry items (client 3464)

| Key | Field                          | Item   | LOC name |
| --- | ------------------------------ | -----: | -------- |
| 150, 151, 174 | `Atoraxion_Desert`, `_EZ`, `_Single_Boss` | 65992 | Fate Fulfilled: Atoraxxion |
| 152, 153, 175 | `Atoraxion_SEA`, `_EZ`, `_Single_Boss` | 757260 | Access Granted: Underwater Entrance |
| 154, 155, 176 | `Atoraxion_Jungle`, `_EZ`, `_Single_Boss` | 757313 | Access Granted: Yolu's Nail |
| 156, 157, 177 | `Atoraxion_Thorn`, `_EZ`, `_Single_Boss` | 66948 | Access Granted: Orze's Root |
| 210 | not in `instancefield.dbss`    | 66942  | Access Granted: The Final Gladios |

## Suggested UI Layout

| Column      | Type | Notes |
| ----------- | ---- | ----- |
| Key         | num  | `key`; right-aligned |
| Field       | text | Internal name from `instancefield.dbss` (`INSTANCE_FIELD_NAME`), dash when the key is not there |
| Title       | text | LOC type 37 text of `title`, else the key string |
| Description | text | LOC type 37 text of `description` |
| X / Y / Z   | num  | Position, rounded; dash when unset |
| Radius (m)  | num  | `radius / 100`; dash when `0` |
| Image       | icon | `image` with `image_region` as a sprite region; the whole image for `0, 0, 1, 1` |
| Entry Item  | text | LOC type 0 name of `entry_item_id`, with icon |
| Spawns      | num  | `spawn_count` |

## Notes

- On client 3464 the file holds 192 records and 164 strings (5 `.dds`
  paths). 185 keys are in both tables. Only here: 210, 4067 to 4071 (named
  `INSTANCEDUNGEONDATA_A1_067_NAME` onwards) and 5000. Only in
  `instancefield.dbss`: 1 to 9, 98, 99, 888, 999 and 9876.
- 142 of the 158 UI keys have `GAME` sheet text. Examples:
  `LUA_LOCALWAR_SERVERNAME_MAP_0` to `_3` read Castle Ruins, Garmoth's Nest,
  Valencia City and Sand Castle Shore-Down (the Crimson fields and
  `PAPUCRIO_ARENA`); `LUA_PERSONAL_SERVER_SER` reads Oasis Server: Serendia;
  `INSTANCEDUNGEONDATA_A1_002_NAME` reads Scarlet Thread. The `A1_003` to
  `A1_008` names are placeholders (`Title 003`, `Desc 003`); `A1_058`,
  `A1_063`, `A1_064` and `A1_067` to `A1_071` have no text.
- `image_region` fits its sheet: `Combine_Etc_horseracing.dds` is 1180 x
  1180 and holds the 500 x 160 boxes `(1, 1005)` and `(502, 1005)`;
  `Combine_Etc_horseracing_01.dds` is 512 x 512 and holds `(1, 1)` to
  `(501, 161)`.
- Positions match the `instancefield.dbss` boxes (sector = position /
  12,800, floored): 79 of the 80 set positions and all 22 spawns lie in the
  box of their key. `Solare_Arena_Reed` sits at sector `(-88, 2, 95)` in
  `-90..-86, 0..3, 93..97`. The exception is `HorseRace_SnowyMountain_Main`,
  whose point is at height sector `2` against a box of `-1..-1`.
- The `INSTANCE_FIELD_TITLE` lookup index holds the `GAME` sheet hash of
  each `title` key, so `instancefield.dbss` (Title column) and the
  `buff.dbss` type 176 Effect text (`Teleport to Instance Field The Magnus:
  The Great Single Path (A1_001)`) read the title without this file.
- `unknown_02` matches no single game rule: Solare arenas (3 vs 3) store
  `6`, but guild matches store `30`. The Lua function
  `ToClient_GetInstanceFieldPlayerMaxCountByMapKey` takes this key, so a
  player cap is a candidate.

## Open Questions

### What do `unknown_02`, `unknown_06` and `unknown_23` hold?

`unknown_02` is `6` on all Solare arenas, `30` on guild matches, `ABSO`
and `CS_WorldBoss_Garmoth`, `40` on most Crimson fields, `PAPUCRIO_ARENA`
and six Oasis servers, `50` on the seventh (`_SnowMountain`), `3000` on the
`MajorSiege_*` maps and key 5000, `4` on `Edania_Field_1vs1` and four Crimson
fields, `10` on horse races and `Edania_Field`. `unknown_06` is `2` on team
battles. `unknown_23` mostly repeats `unknown_06` but stores `3` and `5` on
horse races and `7` on `Yonggung`; `Edania_Field_1vs1` stores `2` and `1`.

### What does `unknown_9e` hold?

`0xFFFF` everywhere except `Personal_Instance_Cal` (`2`), `_Val` (`4`),
`_Kama` (`6`) and `_SnowMountain` (`9`); `_Ser`, `_Bal` and `_Media` store
`0xFFFF`. The values grow with the territory order, so a territory or
server key is a candidate; no table checked so far uses these numbers.

### What are `unknown_b4` and the `A1_` hash list?

`unknown_b4` is `3600` on every `A1_` field and `10800` on the Atoraxion
Single maps, which fits a time limit in seconds (the Lua calls
`ToClient_getInstanceFieldRemainTime`). The `unknown_hashes` on 34 `A1_`
fields match no `stringtable.bss` key hash and no LOC type 37 key.
