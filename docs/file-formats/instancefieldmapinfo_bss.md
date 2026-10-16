# `instancefieldmapinfo.bss` Format

## Purpose

Map data per instance field: a title and description as UI string keys, a map image, a centre point and radius, participant and team limits, a territory lock, an entry item, team spawn
points and a few values without a name yet. The key is the
[instancefield.dbss](instancefield_dbss.md) field key.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records    | Row bytes                  |
| ------ | -------------- | ------- | -------------------------- | ------ | ---------- | -------------------------- |
| 2      | 3473 and later | 3473    | `instancefieldmapinfo.bss` | 44,266 | 193 Record | 196 to 228, 199 on average |
| 1      | 1784           | 1784    | `instancefieldmapinfo.bss` | 14,496 | 77 Record  | 180                        |

| Layout | File                       | Known            | Unknown          |
| ------ | -------------------------- | ---------------- | ---------------- |
| 2      | `instancefieldmapinfo.bss` | 18,924 B (42.8%) | 25,342 B (57.2%) |
| 1      | `instancefieldmapinfo.bss` | 4,794 B (33.1%)  | 9,702 B (66.9%)  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hashes of the `GAME` sheet keys that `title` and `description` store; without it both columns show the key |
| `languagedata_*.loc`  | Optional | LOC type 37 text under those hashes; item names (LOC type 0) |
| `instancefield.dbss`  | Optional | The internal field name per key, through the `INSTANCE_FIELD_NAME` lookup index |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A PABR file with variable-size records and the counted string table that
`exploration.bss` and `npcsimply.bss` also end with (`_common/pabr_strings.py`).
The records end exactly where the string table starts.

| Offset              | Type          | Field              | Notes                               |
| ------------------- | ------------- | ------------------ | ----------------------------------- |
| `+0x00`             | char[4]       | magic              | `PABR`                              |
| `+0x04`             | u32           | count              | Number of records                   |
| `+0x08`             | Record[count] | records            | `count` x record, not sorted by key |
| `records+0x00`      | String Table  | string_table       | See String Table                    |
| `string_table+0x00` | u32           | string_table_start | Offset of the string table          |
| `string_table+0x04` | u32           | zero               | `0`                                 |

### String Table (variable: 4 bytes + strings)

String table entry 0 is the empty string; a string index of `0` means none.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | Number of strings    |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

### Record (variable: 196 bytes + lists)

| Offset               | Type                     | Field              | Notes |
| -------------------- | ------------------------ | ------------------ | ----- |
| `+0x00`              | u16                      | key                | `instancefield.dbss` key |
| `+0x02`              | u32                      | max_user           | Most participants: `6` on Solare arenas, `30` on guild matches, `40` on most Crimson fields and Oasis servers, `3000` on the `MajorSiege_*` maps |
| `+0x06`              | u32                      | max_team_count     | `1`, or `2` on team battles (Solare arenas, guild matches, Crimson fields, `PAPUCRIO_ARENA`, `CrewBattle`, `Edania_Field_1vs1`) |
| `+0x0A`              | f32                      | x                  | World position (centimetres); all `0` when unset |
| `+0x0E`              | f32                      | y                  | |
| `+0x12`              | f32                      | z                  | |
| `+0x16`              | f32                      | radius             | Centimetres around that position (`9000` on `Solare_Arena_Reed`); `0` when unset |
| `+0x1A`              | u32                      | title              | String index of a `GAME` sheet key (`LUA_LOCALWAR_SERVERNAME_MAP_1`, `INSTANCEDUNGEONDATA_A1_001_NAME`) |
| `+0x1E`              | u32                      | description        | String index of a `GAME` sheet key (`INSTANCEDUNGEONDATA_A1_001_DESC`) |
| `+0x22`              | u8                       | is_season_only     | `1` on six Crimson field records (keys 11, 12, 17, 18, 22, 24), else `0` |
| `+0x23`              | u32                      | min_user           | Fewest participants; equals `max_team_count` except on `Edania_Field_1vs1` (`1`), horse races (`2`, `3`, `5`) and `Yonggung` (`7`). Never above `max_user` |
| `+0x27`              | u32                      | image              | String index of a `.dds` path (`Map_Nest.dds`, `Combine_Etc_horseracing.dds`) |
| `+0x2B`              | u16[4]                   | image_region       | x1, y1, x2, y2 in pixels of `image`; `0, 0, 1, 1` on the Crimson field maps |
| `+0x33`              | bytes[106]               | unknown_33         | The same bytes in every record; the 8-byte groups hold `0x00007FFC...` and `0x00000293...` values, which read like memory addresses of the tool that wrote the file |
| `+0x9D`              | u8                       | is_show_name_when_camouflage | `1` on the Solare arenas, guild matches, `PAPUCRIO_ARENA` and 8 of the 16 Crimson field records: names stay visible under camouflage |
| `+0x9E`              | u16                      | restrict_territory | `territoryinfo.bss` territory key the map is locked to, `0xFFFF` for none; see [Territory locks](#territory-locks-client-3464) |
| `+0xA0`              | bytes[8]                 | unknown_a0         | Always `0` |
| `+0xA8`              | u32                      | entry_item_id      | Item ID, `0` for none; the "Access Granted" items of Atoraxion |
| `+0xAC`              | u32                      | unknown_ac         | `1` where `entry_item_id` is set, else `0`; possibly its count, see [Field Names](#field-names) |
| `+0xB0`              | u32                      | unknown_b0         | Always `0` |
| `+0xB4`              | u32                      | unknown_b4         | `0`, `3600` on the `A1_` fields, `10800` on the Atoraxion Single maps and key 210 |
| `+0xB8`              | u32                      | unknown_b8         | Always `0` |
| `+0xBC`              | u32                      | hash_count         | |
| `+0xC0`              | u32[hash_count]          | unknown_hashes     | `hash_count` values; only on `A1_` fields (1 to 3 each); not a `stringtable.bss` key hash |
| `unknown_hashes+0x00` | u32                     | spawn_count        | |
| `unknown_hashes+0x04` | f32[spawn_count][3]     | spawns             | World positions; `2` on every guild match map, one per side, both inside the map's box |
| `spawns+0x00`        | f32 if spawn_count != 0  | unknown_spawn_f32  | Only when `spawn_count` is not `0`; `200` on all |
| `unknown_spawn_f32+0x00` | u32 if spawn_count != 0 | unknown_spawn_u32 | Only when `spawn_count` is not `0`; `10` on all |

Earlier versions of this doc called `unknown_33` `filler` and the three
always-zero fields `unknown_a0`, `unknown_b0` and `unknown_b8` `zero`.

## Layout 1

On client 1784 a record is 180 bytes with no lists: it has no
`description`, so every later field sits 4 bytes earlier, and it ends after
`unknown_b0`, without `unknown_b4`, `unknown_b8`, the hash list or the spawn
list. `unknown_a0` is 12 bytes.

### Record (180 bytes)

| Offset  | Type       | Field                        | Notes |
| ------- | ---------- | ---------------------------- | ----- |
| `+0x00` | u16        | key                          | `instancefield.dbss` key |
| `+0x02` | u32        | max_user                     | |
| `+0x06` | u32        | max_team_count               | |
| `+0x0A` | f32        | x                            | |
| `+0x0E` | f32        | y                            | |
| `+0x12` | f32        | z                            | |
| `+0x16` | f32        | radius                       | |
| `+0x1A` | u32        | title                        | String index of a `GAME` sheet key |
| `+0x1E` | u8         | is_season_only               | |
| `+0x1F` | u32        | min_user                     | |
| `+0x23` | u32        | image                        | String index of a `.dds` path |
| `+0x27` | u16[4]     | image_region                 | |
| `+0x2F` | bytes[106] | unknown_33                   | |
| `+0x99` | u8         | is_show_name_when_camouflage | |
| `+0x9A` | u16        | restrict_territory           | `0xFFFF` for none |
| `+0x9C` | bytes[12]  | unknown_a0                   | `0` except on keys 150 to 153, where it holds the u32s `66012, 1, 0`: the first item and count of the sheet's `exchangeItemForNormalFieldEnter` |
| `+0xA8` | u32        | entry_item_id                | `65992` on keys 150 and 151, `757260` on 152 and 153 on client 1784 |
| `+0xAC` | u32        | unknown_ac                   | `1` where `entry_item_id` is set, else `0` |
| `+0xB0` | u32        | unknown_b0                   | Always `0` |

On client 1784 the file holds 77 records and 17 strings, none of them a
`_DESC` key.

## Field Names

The names of `max_user`, `max_team_count`, `is_season_only`, `min_user`, `is_show_name_when_camouflage` and `restrict_territory` follow the `InstanceEnterPosition` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `MaxUser`, `MaxTeamCount`, `isSeasonOnly`, `MinUser`, `isShowNameWnehCamoflage`, `restrictTerritory`). Matched by value over the 77 keys the sheet shares with client 3464: five columns equal the file on all 77 keys, every non-zero value included. `MaxUser` equals `max_user` on 57; the other 20 are later rebalances (Crimson fields `30` to `40` and `2` to `4`, `CrewBattle` `10` to `20`, Atoraxion `5` to `1`).

The same sheet has `exchangeItemForNormalFieldEnter` (`66012,0,1,65992,0,1` on key 150, item, enchant and count pairs) whose second item is that key's `entry_item_id`, so `unknown_ac` may be the count; the sheet has no column for `unknown_b4`, `unknown_hashes` or the spawn list, and its `Team_1` to `Team_4` positions are not the `spawns`.

## Territory Locks (Client 3464)

| Key | Field | restrict_territory | LOC name |
| --- | ----- | -----------------: | -------- |
| 131 | `Personal_Instance_Cal` | 2 | Calpheon |
| 134 | `Personal_Instance_Val` | 4 | Valencia |
| 135 | `Personal_Instance_Kama` | 6 | Kamasylvia |
| 136 | `Personal_Instance_SnowMountain` | 9 | Mountain of Eternal Winter |

`_Ser`, `_Bal` and `_Media` store `0xFFFF`.

## Entry Items (Client 3464)

| Key | Field                          | Item   | LOC name |
| --- | ------------------------------ | -----: | -------- |
| 150, 151, 174 | `Atoraxion_Desert`, `_EZ`, `_Single_Boss` | 65992 | Fate Fulfilled: Atoraxxion |
| 152, 153, 175 | `Atoraxion_SEA`, `_EZ`, `_Single_Boss` | 757260 | Access Granted: Underwater Entrance |
| 154, 155, 176 | `Atoraxion_Jungle`, `_EZ`, `_Single_Boss` | 757313 | Access Granted: Yolu's Nail |
| 156, 157, 177 | `Atoraxion_Thorn`, `_EZ`, `_Single_Boss` | 66948 | Access Granted: Orze's Root |
| 210 | not in `instancefield.dbss`    | 66942  | Access Granted: The Final Gladios |

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
- The client Lua function `ToClient_GetInstanceFieldPlayerMaxCountByMapKey`
  takes this key; `max_user` is the player cap it names (Solare arenas,
  3 vs 3, store `6`).

## Open Questions

### What are `unknown_b4` and the `A1_` hash list?

`unknown_b4` is `3600` on every `A1_` field and `10800` on the Atoraxion
Single maps, which fits a time limit in seconds (the Lua calls
`ToClient_getInstanceFieldRemainTime`). The `unknown_hashes` on 34 `A1_`
fields match no `stringtable.bss` key hash and no LOC type 37 key.
